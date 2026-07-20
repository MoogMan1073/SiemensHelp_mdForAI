---
title: "Using global functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: BasicsWCCPenUS
topics: 196
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using global functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Working with the HMI Device Wizard (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-the-hmi-device-wizard-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with libraries
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting project data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-project-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using cross-references
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-cross-references-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Replacing devices
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#replacing-devices-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying between devices and editors
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-between-devices-and-editors-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using WinCC version compatibility
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-wincc-version-compatibility-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing colors centrally
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-colors-centrally-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Load files using the "HMI files" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#load-files-using-the-hmi-files-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Exchanging controller data from other projects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exchanging-controller-data-from-other-projects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Recognizing the project status by the SIMATIC WinCC RT symbol (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#recognizing-the-project-status-by-the-simatic-wincc-rt-symbol-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with the HMI Device Wizard (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)
- [HMI device wizard basics (RT Advanced, RT Professional)](#hmi-device-wizard-basics-rt-advanced-rt-professional)

### HMI device wizard basics (Basic Panels, Panels, Comfort Panels)

#### Introduction

The HMI device wizard will automatically start when you create a new HMI device in your project.

#### HMI device wizard

The HMI device wizard will guide you through each dialog step by step and help you set up a device. You use the HMI device wizard to specify the basic settings for your HMI device, such as screen layout and the connection to your PLC.

![HMI device wizard](images/111980277771_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> When you create a device with a color display using the HMI device wizard, the graphics of the navigation buttons may be displayed in black and white. This error only occurs, however, if the new device is created with the same name as a device with a monochrome display which has been deleted in the meantime.
>
> You can avoid this error by always deleting the associated graphics in the Graphics collection whenever you delete a device from the project.

> **Note**
>
> **Multiple languages in the HMI device wizard**
>
> If you create multilingual screen navigation with the HMI device wizard, WinCC uses the user interface language for user-defined labels in all project languages.
>
> If the character set of the user interface language is not supported in a project language, these names will not appear in this project language, for example, with a Chinese interface language and English project language.

> **Note**
>
> **Interface type of the connection**
>
> If possible, the HMI device wizard makes a connection between the HMI device and controller with the default interface type of the HMI device.
>
> After configuration with the HMI device wizard, check the connection in the "Devices &amp; Networks" editor.

---

**See also**

[HMI device wizard basics (RT Advanced, RT Professional)](#hmi-device-wizard-basics-rt-advanced-rt-professional)
  
[General information about cross references (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#general-information-about-cross-references-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### HMI device wizard basics (RT Advanced, RT Professional)

#### Introduction

The HMI device wizard will guide you through each dialog step by step and help you set up a device. You use the HMI device wizard to specify the basic settings for your HMI device, such as screen layout and the connection to your PLC.

![Introduction](images/111981225483_DV_resource.Stream@PNG-en-US.png)

#### Opening the HMI device wizard

1. Add a new device to your project, for example, RT Advanced.
2. Click on the device in the project tree.
3. Select "Start the HMI device wizard" in the shortcut menu. The "HMI device wizard" opens.

   > **Note**
   >
   > If you make changes after adding the device, such as adding a new screen, the HMI device wizard will not open again.

   > **Note**
   >
   > When you create a device with a color display using the HMI device wizard, the graphics of the navigation buttons may be displayed in black and white. This error only occurs, however, if the new device is created with the same name as a device with a monochrome display which has been deleted in the meantime.
   >
   > You can avoid this error by always deleting the associated graphics in the Graphics collection whenever you delete a device from the project.

   > **Note**
   >
   > **Device dependency - quotation marks in project names**
   >
   > WinCC Professional projects whose names are in quotation marks have not been compiled.
   >
   > When you create an HMI device for WinCC RT Professional, do not use quotation marks within the project name.

   > **Note**
   >
   > **Multiple languages in the HMI device wizard**
   >
   > If you create multilingual screen navigation with the HMI device wizard, WinCC uses the user interface language for user-defined labels in all project languages.
   >
   > If the character set of the user interface language is not supported in a project language, these names will not appear in this project language, for example, with a Chinese interface language and English project language.

---

**See also**

[HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)
  
[Load files using the "HMI files" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#load-files-using-the-hmi-files-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Master copies and types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#master-copies-and-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Libraries in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#libraries-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing objects in a library
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-objects-in-a-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using types and their versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-types-and-their-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using master copies (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-master-copies-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can store library elements you want to reuse in libraries. For each project there is a project library that is connected to the project. In addition to the project library, you can create any number of global libraries that can be used over multiple projects. Since the libraries are compatible with each other, library elements can be copied and moved from one library to another. Libraries are used, for example, to create templates for blocks that you first paste into the project library and then further develop there. Finally, you copy the blocks from the project library to a global library. You can make the global libraries available to other collaborators working on your project. The other collaborators continue to use the blocks and adapt them to their individual requirements as needed.

Both the project library and global libraries distinguish between two different types of library elements:

- Types

  Objects that are required to run user programs, for example, blocks, PLC data types (UDT), HMI user data types or faceplates are suitable as types. Types can be versioned and therefore support professional further development. Projects using the types can be updated as soon as new type versions are available.
- Master copies

  Almost every object can be saved as a master copy and pasted into the project again later. You can, for example, save entire devices with their contents or cover pages for plant documentation as master copies.

Your WinCC software package is supplied with comprehensive libraries that contain, for example, "Motor" or "Valve" objects. You can also, however, define your own library objects.

Libraries are managed in the library management or in the "Libraries" task card.

#### Project library

There is one library for each project. Objects of the project library are stored alongside with the project data and are available only for the project in which the library was created. If the project is moved to another PC, any project library created in it is also moved.

To use the library object of the project library in other objects, move or copy the object into a global library.

#### Global libraries

A global library is saved independently of the project data in its own file with the extension ".aIxx", whereby "xx" stands for the current WinCC version number.

A project can access several global libraries. A global library may be used concurrently in several projects.

When a library object is changed by a project, this library will be changed in all projects in which these libraries are open.

#### Library objects

A library can contain various WinCC objects.

Examples of types:

- Faceplates

  If you want to use configurable object groups multiple times in screens and change them centrally, create faceplates for them. If you change the properties of a faceplate in the library, the changes affect all screens that contain this faceplate.
- User data types
- Styles
- Style sheets

Examples of master copies:

- HMI device
- Screens
- Tags
- Parameter set types
- Scripts

---

**See also**

[Screen basics (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#screen-basics-rt-professional)
  
[Inserting a library object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-a-library-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Saving a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#saving-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Opening a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#opening-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Master copies and types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#master-copies-and-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-the-library-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Master copies and types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Both the "Project library" and the "Global library" contain the two folders "Master copies" and "Types". You can create or use the library objects either as a master copy or a type.

#### Master copies

Use master copies to create independent copies of the library object.

#### Types

Create instances of objects of the "Types" folder and use these in your project. The instances are bound to their respective type.

#### Administration of the library objects

You can copy and move library objects to other libraries. You can only copy master copies to the "Master copies" folder or any sub-folder of "Master copies". You can only insert types in the "Types" folder or any sub-folder of "Types".

---

**See also**

[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Libraries in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

WinCC provides you with global libraries with frequently used templates. Sorted by topic into folders, they contain preassembled graphic objects which you can use in screens for operation and monitoring of your plant.

#### Global library "Buttons and Switches"

The libraries "Buttons and Switches" offer a wide selection of buttons and switches.

![Global library "Buttons and Switches"](images/97185060235_DV_resource.Stream@PNG-en-US.png)

The folders divide switches and buttons into categories. The "DiagnosticsButtons" folder contains the object "System diagnostics indicator", for example. You use the "System diagnostics indicator" object for system diagnostics in your plant.

> **Note**
>
> You can only use the objects in the "DiagnosticsButtons" folder on Comfort Panels.
>
> You cannot use objects which have "Switch" in the object name or in the associated folder name in Runtime Professional.

#### Global library "Monitoring and Control objects"

The "Monitoring and Control objects" library offers more complex display and operating objects in several designs and corresponding control lights, buttons and switches.

![Global library "Monitoring and Control objects"](images/76071139595_DV_resource.Stream@PNG-en-US.png)

In addition, graphics views for the designs are stored in the "Design_Backgrounds" folder; they can be used as object backgrounds for the custom extension of the scope of the library.

> **Note**
>
> You cannot use objects which have "Switch" in the object name in Runtime Professional. The same applies for the object "D5_Display_3" with the date/time field it contains.

### Managing libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of the library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-the-library-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Opening library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#opening-library-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Filtering types in the library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#filtering-types-in-the-library-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Saving a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#saving-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Opening a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#opening-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Displaying logs of global libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-logs-of-global-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating a project with the contents of a library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-a-project-with-the-contents-of-a-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating a library with the contents of another library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-a-library-with-the-contents-of-another-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Exporting and importing library texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-and-importing-library-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of the library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Function of the library management

Master copies and types with dependencies to other library elements are subject to some functional restrictions. They can, for example, not be deleted as long as dependencies still exist. This prevents other library elements from becoming useless. The library management is used to identify the dependencies and to create an overview of the work progress.

The library management offers the following functions:

- Display of the correlations of types and master copies

  If a type is referenced in other types or master copies, the correlations are displayed in the library management. You will also be able to see which library elements reference a type or a master copy.
- Display of reference locations of types in the project
- Display all types that include a version with the "in test" or "in progress" status

##### Layout of the library management

The figure shows the library management, consisting of the following components:

- Toolbar of the library management
- "Types" area
- "Use" area

![Layout of the library management](images/97420353419_DV_resource.Stream@PNG-en-US.png)

##### Toolbar of the library management

You can perform the following tasks in the toolbar of the library management:

- Update view

  If the project was changed, you can update the view of the library management.
- Clean up library

  You can clean up the project library and global libraries. By cleaning up a library, you delete all types and type versions that are not linked to an instance in the project.
- Harmonize project

  By harmonizing a project, you adapt the names and the path structures of type uses in the project to the corresponding names and path structures of the types within a library.
- Expand or collapse view of the types

  You can open or close all types using the buttons in the toolbar.

##### "Types" area

The "Types" area displays the contents of the folder you selected in the "Libraries" task card.

You can use the "Filter" drop-down list to filter the view, e.g. by pending changes, released types, or types without use.

##### "Uses" area

The "Uses" area gives you an overview of the reference locations of the selected types and master copies. The "Uses" area is divided into two tabs:

- "Uses in the project" tab

  The "Uses in the project" tab is used to show the instances of type versions and their respective reference locations in the project. When you select an instance, you can show the cross references of the instance in the project in the Inspector window.
- "Uses in the library" tab

  The "Uses in the library" tab is used to show all points within the library at which a type or a master copy is used.

#### Opening library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Procedure

To open the library management, follow these steps:

1. Open the "Libraries" task card.
2. Select a type or any folder that contains types.
3. Select the "Open library management" button ![Procedure](images/149431843723_DV_resource.Stream@PNG-de-DE.png).

   - or -

   Select the "Library management" command from the shortcut menu.

##### Result

The library management opens and the types are displayed with their versions.

##### Working with large or multiple monitors

The library management window can be detached and moved as desired.

#### Filtering types in the library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

A filter function in the library management enables you to limit the displayed types. The following filters are available:

- Show all types
- Types with pending changes
- Released types
- Types with multiple versions
- Types not used in the project
- Types with inconsistencies in the default version
- Highest version of the type without "default" identifier.

##### Requirement

At least one type has been created.

##### Filtering by types with pending changes

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types with pending changes" from the "Filter" drop-down list.

   The "Types" area only displays types that have the "in progress" status.

##### Filtering by released types

1. Select the "Types" folder in the project library.
2. Open the library management.
3. In the "Filter" drop-down list, select the entry "Released types".

   The "Types" area only displays types that have released versions.

##### Filtering by types with multiple versions

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types with multiple versions" from the "Filter" drop-down list.

   The "Types" area only displays types that have more than one version.

##### Filtering by types that have no instances in the project

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types not used in the project" from the "Filter" drop-down list.

   The "Types" area only displays types that have no instances in the project.

##### Filtering by types with inconsistencies in the default version

1. Select the "Types" folder in the project library.
2. Open the library management.
3. In the "Filter" drop-down list, select the "Types with inconsistencies in the default version" entry.

   Only those types whose default version is inconsistent are displayed in the "Types" area.

##### Filtering by types whose highest version is not the default version

1. Select the "Types" folder in the project library.
2. Open the library management.
3. In the "Filter" drop-down list, select the "Highest version of the type without default identifier" entry.

   In the "Types" area, only those types are displayed whose highest version is not the default version.

---

**See also**

[Opening library management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#opening-library-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the libraries, you can store the configured objects that you want to use multiple times in your configuration. To use objects in multiple projects, create a global library.

##### Requirement

- A project is open.
- The "Libraries" task card is opened.

##### Procedure

1. Click the ![Procedure](images/14162763531_DV_resource.Stream@PNG-de-DE.png) icon under "Global library".

   The "Create new global library" dialog opens.

   ![Procedure](images/149600080395_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/149600080395_DV_resource.Stream@PNG-en-US.png)
2. Enter a name.
3. Select the path where the new library is to be stored.
4. Click "Create".

##### Result

The new library is shown in the "Global libraries" pane. The global library contains the "Types", "Master copies" and "Common data" folders. Under "Common data" you can find reports for the global library.

A folder with the name of the global library is created in the file system at the storage location of the global library. This actual library file is given the file name extension ".alxx", whereby "xx" stands for the current WinCC version number.

---

**See also**

[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Saving a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

A global library is saved as a separate file. This file contains all the objects of the global library, including the referenced objects. For example, the reference of a tag which was configured on an I/O field is also saved in the library.

WinCC prompts you to save the global libraries when you close WinCC or your project without saving. You also can store the global library during configuration, without storing the entire project.

##### Requirement

- You have opened a project which contains at least one library.
- The "Libraries" task card is opened.
- A library has been changed.

##### Procedure

1. Select the global library that you want to save.
2. Click the ![Procedure](images/25535164043_DV_resource.Stream@PNG-de-DE.png) icon in the "Global library" pane.

   Alternatively, you can select the "Save Library" command in the shortcut menu.

Save as:

1. To save the global library to another folder, select "Save as" in the shortcut menu.
2. Select the path in which you want to store the new library and enter a file name.

##### Result

The global libraries are saved under their current file name or a file name you have specified.

---

**See also**

[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Opening a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In WinCC, the global libraries are stored in separate files. You can use a global library in any project.

##### Requirement

- You have saved a global library.
- A project is open.
- The "Libraries" task card is opened.

##### Procedure

1. Click the ![Procedure](images/70981237771_DV_resource.Stream@PNG-de-DE.png) icon in the "Global libraries" pane.

   The "Open global library" dialog is displayed.
2. Select the path in which the library is stored.
3. Click "Open".

**Note**

To have access to a global library from multiple projects, open the global library in write-protected mode. If a global library is not open as write-protected, access from other projects is blocked.

##### Result

WinCC displays the opened global library in the "Global libraries" pane.

---

**See also**

[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Displaying logs of global libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Logs listing all changes made to the global library are created when global libraries are updated. The logs are stored together with the global library and are always available once you have opened the global library.

##### Procedure

To open the logs of a global library, follow these steps:

1. Open the global library in the "Libraries" task card.
2. Open "Common data &gt; Logs" in the lower-level folder.
3. Double-click the required log.

   The log opens in the work area.

#### Updating a project with the contents of a library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

After you have edited several types in the project library, update all instances in the project to the most recent version of the types from the project library.

Each of the following elements can be selected as source for the update:

- Individual folders within a library
- Individual types

##### Requirement

The "Libraries" task card or the library management is open.

##### Procedure

1. Select a folder within the project library or individual types.
2. Select "Update types &gt; Project..." from the shortcut menu.

   A dialog opens.
3. Select either the entire project or individual devices for the update.
4. Select "Update instances in the project".
5. To delete all older versions of the updated types from the project library, select the check box "Delete unused type versions without the "default" identifier from the library".
6. Click "OK" to confirm.

##### Result

All instances of the types are updated in the project to the most recent version of the selected types in the project library.

You can find a log of the update process in the project tree under "Common data".

#### Updating a library with the contents of another library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

The following options are available for updating libraries:

- Updating a global library with types from another global library
- Updating the project library with types from a global library

Each of the following elements can be selected as source for the update:

- Individual folders within a library
- Individual types

##### Requirement

- The "Libraries" task card or the library management is open.
- To update a global library, open the library with write permission.

##### Procedure

To update a library with the contents of a different library, follow these steps:

1. Select a folder within the library or individual types.
2. Right-click the source and select the "Update types &gt; Library..." command from the shortcut menu.

   The "Update library" dialog opens.
3. Select the type of library you want to update:

   - Select "Update project library" to update the project library with types from a global library.
   - Select "Update global library" to update a global library.
4. Optional: Select the global library you want to update from the drop-down list.
5. Enable the desired update options:

   - Updating instances in the project
   - Delete unused type versions without the "default" identifier from the library
   - Force update

     Types are updated including their dependent types, regardless of their version number.
6. Click "OK" to confirm.

##### Result

- Types not yet available in the target library are supplemented there with all their versions. More recent versions are added to the types that already exist in the target library.

  If a more recent version of a type already exists in the target library, the latest version is nevertheless copied from the source library and automatically assigned a newer version number.
- A log listing all performed changes to the target library is created for the update process.

  If you have updated the project library, you can find the log in the project tree under "Common data &gt; Logs".

  If you have updated a global library, you can find the log in the "Common data &gt; Logs" folder in the level below the global library.

#### Exporting and importing library texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can export the texts of the library objects to an .xlsx file to edit them in MS Excel, for example, or export them for compilation.

You export and import texts of the following objects in the library:

- Individual library types and master copies
- Multiple library types and master copies
- All library objects of the project library or a global library

After editing or external compilation, you import the texts into the TIA Portal.

When the texts are imported, all texts from the import file are imported for the entire library, even if you have only selected one library object. The target languages of the import file must be activated in the project.

During import to a master copy, the texts of the template are overwritten in the library with the new texts from the import file. During import of the texts to a library type, the latest version is overwritten in the library with the new texts from the import file. If a version of a type has not been released yet in a project library, no texts can be imported for the entire project library.

> **Note**
>
> **Restrictions for text import**
>
> Texts belonging to the following library objects cannot be imported:
>
> - Type instances which are contained in a master copy
> - Library types whose versions have not yet been released and which have the status "in progress" or "in test"
> - Write-protected global library

##### Defining the source language and target language

You define the source language and target language for export of the texts in the Export dialog. The selection of available languages depends on the project languages defined.

With the global library, the selection of available source and target language depends on the languages defined by the creator of the library. To see the available languages of the global library, double-click the entry "Library languages" in the project folder "Language and Resources" of the library in question.

##### Exporting texts

To export the texts of a single or several library objects, follow these steps:

1. Open the library.
2. Select the desired library object in the library.
3. Select the command "Export library texts" in the shortcut menu of the object.

   Alternatively, click the ![Exporting texts](images/152091872011_DV_resource.Stream@PNG-de-DE.png) "Export library texts" button in the toolbar.

   The "Export" dialog opens.
4. Select the source language and the target language for export in the dialog.
5. Enter the name and path for the export file.

   ![Exporting texts](images/152092117515_DV_resource.Stream@PNG-en-US.png)
6. Click "Export".  
   After successful export, the export file is stored under the specified path.

##### Importing texts

To import the texts after editing or compilation into the TIA Portal again, follow these steps:

1. Open the project library or the global library.
2. Select the command "Import library texts" in the shortcut menu of the object.

   Alternatively, click the ![Importing texts](images/152091879563_DV_resource.Stream@PNG-de-DE.PNG) "Import library texts" button in the toolbar.

   The "Import" dialog opens.
3. Select the path and the name of the import file from the "Select file for import" field.

   Activate the "Import source language" check box if you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes.
4. Click on "Import".

### Managing objects in a library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying library objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-library-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Storing an object as master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-object-as-master-copy-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Inserting a library object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-a-library-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Displaying library objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The elements of a library can be displayed in the folder structure under the library or in the "Elements" pane.

##### Requirement

- At least one library object has been created in a library.
- The "Libraries" task card is opened.

##### Displaying parts of the library objects

| 1. Select the folder of a library whose elements are to be displayed. 2. Click ![Displaying parts of the library objects](images/14161014411_DV_resource.Stream@PNG-de-DE.png).    The objects contained are displayed in the "Elements" pane. 3. To display components of an element, click on an element in the "Elements" pane.    The parts of the element are displayed in the "Elements" pane.               ![Displaying parts of the library objects](images/152092160139_DV_resource.Stream@PNG-en-US.png)         ![Displaying parts of the library objects](images/152092160139_DV_resource.Stream@PNG-en-US.png) 4. Select a view:       | Icon | View |    | --- | --- |    | ![Displaying parts of the library objects](images/14161806219_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161806219_DV_resource.Stream@PNG-de-DE.png) | Details mode |    | ![Displaying parts of the library objects](images/14161567627_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161567627_DV_resource.Stream@PNG-de-DE.png) | List mode |    | ![Displaying parts of the library objects](images/14161559691_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161559691_DV_resource.Stream@PNG-de-DE.png) | Overview with icons | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The library objects are displayed with the selected view in the "Elements" pane.

#### Storing an object as master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In libraries you can store WinCC objects, e.g. screens, tags, alarms, scripts or parameter set types as master copies. To do this, drag-and-drop the object from the project tree, the work area or the detail view into the library. If you have created subfolders in the library, you can also insert an object directly there.

##### Requirement

- The project tree or the work area is open.
- An object has been created.
- The "Libraries" task card is displayed.

##### Procedure

1. Select the object in the project tree or in the work area.
2. Drag-and-drop the object into the "Master copies" folder in the library.

   The mouse pointer is transformed into a crosshair with an appended object icon.

   ![Procedure](images/152092481291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/152092481291_DV_resource.Stream@PNG-en-US.png)

**Note**

**Objects from the project tree as master copy**

You can use all objects as a master copy for recreation in the project tree:

- HMI devices, PLCs, technology objects, ...
- Screens
- Tag tables
- Parameter set types
- Scripts

**Note**

**Objects from a work area as master copy**

You can use objects as a master copy for recreation in a work area:

- Tags
- HMI alarms
- Tasks
- Cycles
- Text and graphic lists

##### Result

The object is saved to the library for further use in multiple instances of your configuration.

![Result](images/97192066443_DV_resource.Stream@PNG-en-US.png)

#### Inserting a library object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The system always assigns the inserted library object a name which consists of the name of the object type and of a consecutive number.

If the inserted object already exists, you have the option of replacing the object or of saving it under a new name.

You cannot insert library objects that are not supported by the HMI device.

> **Note**
>
> If you insert a screen with interconnected template from the library, the template will also be inserted. Any existing matching template is not used.

##### Requirement

- The "Libraries" task card is opened.
- The editor in which you want to insert the library object is open.

##### Procedure

1. Select a library object from the library.
2. Drag-and-drop the library object to the position in the work area where you want to insert the object.

   The library object is inserted.

##### Result

If the object was contained in the "Copy templates" folder, you have inserted an independent copy of the library object in the editor.

If the object was contained in the "Types" folder, you have inserted an instance of the library object in the editor.

---

**See also**

[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Using types and their versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Adding a type to a project library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adding-a-type-to-a-project-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a new type version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-new-type-version-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Consistency status of types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#consistency-status-of-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Generating a script as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#generating-a-script-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Generating a screen as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#generating-a-screen-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating an HMI faceplate as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-hmi-faceplate-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Generating a HMI user data type as type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#generating-a-hmi-user-data-type-as-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating an HMI style as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-hmi-style-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating an HMI style sheet as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-hmi-style-sheet-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Depending on the reference location, the version of a type has different states.

##### Released version

The "Released version" status is available for all types, regardless of the reference location.

If you want to edit a released version, you must first create a new test version or a snapshot.

Released type versions of scripts and screens can be opened and viewed at their instance.

##### "In progress" version

The "in progress" status is possible for the following types:

- HMI faceplate
- HMI user data type (HMI UDT)
- HMI style
- HMI style sheets

When you create a new type or a new version of a released type, the type is set to the "in progress" state.

Types with the "in progress" state can be edited in the library management without the need for a reference to an instance in the project. Upon release, the type compatibility undergoes a consistency check.

##### "in test" version

Only versions of scripts and HMI screens have the "in test" status.

When you create a new version of a type, the type is assigned the status "in test".

A version with "in test" status is linked to an instance in the project. You can set only one version to "in test" for each type at a given time.

An "in test" version may only be linked to a single instance in the project. Therefore, it is not possible to copy an instance to the clipboard, to duplicate it or to create an additional type from the instance as long as it has "in test" status.

---

**See also**

[Generating a script as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#generating-a-script-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Generating a screen as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#generating-a-screen-as-a-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a new type version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-new-type-version-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Master copies and types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#master-copies-and-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Adding a type to a project library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

A project is open.

An HMI device has been created and opened.

The project tree is open.

The "Libraries" task card or the library management is open.

##### Procedure

1. In the "Project library" pane, select a folder that contains types.

   - or -

   Open a folder from the project library that contains types in the library management.
2. Select "Add new type..." in the shortcut menu.

   - or -

   Click "Add new type" in the "Project library" pane.

   The "Add new type" dialog is displayed.
3. Select the type.
4. Specify the device for which the type is being created.
5. Click "OK".

   Depending on the selected type, the editor for editing the type opens.
6. Close the note at the top of the window and edit the type.
7. After editing, release the version of the type.

##### Result

You have added a type to the project library.

#### Creating a new type version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Principle

If you create a new version of a type, the reference location of the type determines the status of the newly created version.

##### Requirement

The "Libraries" task card is opened.

A type has been created and released.

##### Procedure

1. Select the released type.
2. Select "Edit type" in the shortcut menu.

##### Result for types of faceplates, user data, and styles

A new version of the type is created.

The version has the status "in progress". The library management opens.

##### Result for types of scripts and screens

A dialog opens.

After you have selected the settings in the dialog, the version is set to the status "in test". The instance used in the project is set to the status "in test". The library management opens.

---

**See also**

[State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Editing a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To edit a type, open the type in the library management or in the "Project library" task card.

The editor for the type opens. In the note at the top of the editor you can find information about the status of the type as well as about additional options for editing.

##### Requirement

At least one type is created in the project library.

##### Procedure

1. Select "Open" in the shortcut menu of the type.

   For types of the "User data type" type, the dialog for setting the test environment is displayed.

   The editor for the type is displayed.
2. Close the note at the top.
3. Edit the type.
4. To release the version of the type or to discard the changes, reopen the note at the top.

   ![Procedure](images/149594229387_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/149594229387_DV_resource.Stream@PNG-de-DE.png)

#### Consistency status of types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Types may no longer be consistent after changes. The "Status" column in libraries indicates whether a type is consistent or inconsistent. The following statuses are displayed:

| Icon | Meaning |
| --- | --- |
| ![Figure](images/140596194443_DV_resource.Stream@PNG-de-DE.png) | The type is consistent. |
| ![Figure](images/140613088011_DV_resource.Stream@PNG-de-DE.png) | The type has more than one inconsistency. |
| ![Figure](images/140613459339_DV_resource.Stream@PNG-de-DE.png) | The default version of the type does not use the default version of its dependent type. |
| ![Figure](images/143118756363_DV_resource.Stream@PNG-de-DE.png) | The type has duplicate versions. |
| ![Figure](images/143118760075_DV_resource.Stream@PNG-de-DE.png) | More than one version of the type is instantiated in the device. |
| ![Figure](images/143118763787_DV_resource.Stream@PNG-de-DE.png) | A version other than the default version of the type is instantiated in the device. |

#### Generating a script as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is open.

##### Procedure

1. Open the "Scripts" editor in the project tree.
2. Create a new script.
3. Select the script in the project tree.
4. Drag-and-drop the script into a library in the "Libraries" task card.

   A dialog opens.
5. Enter a name.
6. Enter a comment.

##### Result

You have created a type version of a script in the library. The created type is stored as a released version in the library. An instance of the type is used in the project.

To change the script, create a new version of the script.

---

**See also**

[State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Generating a screen as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is open.

##### Procedure

1. Open the "Screens" editor in the project tree.
2. Create a new screen.
3. Select the screen in the project tree.
4. Drag-and-drop the screen into a library in the "Libraries" task card.

   A dialog opens.
5. Enter a name.
6. Enter a comment.

##### Result

You have created a type of a screen in the library.

The created type is stored as a released version in the library. An instance of the type is used in the project.

To change the screen create a new version of the screen.

---

**See also**

[State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating an HMI faceplate as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To define a new faceplate type, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "HMI faceplate".
4. Specify the device for the new type.
5. Give the new faceplate type a descriptive name.

##### Result

The new faceplate type is created and displayed under its selected name in the project library.

The faceplate type is assigned the status "in progress" and the version 0.0.1.

The faceplates editor opens.

#### Generating a HMI user data type as type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To define a new HMI user data type, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "HMI user data type".
4. Specify the device for the new type.
5. Assign a descriptive name to the new HMI user data type.

##### Result

The new HMI user data type is created and displayed under the selected name in the project library.

The user data type is assigned the status "in progress" and the version 0.0.1.

The editor for the user data type opens.

#### Creating an HMI style as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To define a new HMI style, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "HMI style".

##### Result

The new style is created and displayed under its selected name in the project library. The HMI style type is assigned the status "in progress" and the version 0.0.1.

#### Creating an HMI style sheet as a type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To define a new HMI style sheet, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "HMI style sheet".
4. Select the type of style sheet.
5. Assign a meaningful name to the style sheet.
6. Select the style sheet category from the list.

##### Result

The new style sheet is created and displayed under its selected name in the project library.

The HMI style sheet type is assigned the status "in progress" and the version 0.0.1.

### Using master copies (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using a script as a master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-a-script-as-a-master-copy-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using a screen as a master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-a-screen-as-a-master-copy-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

You can save objects that you have created in the project tree as a master copy in a library. Based on the master copy, you can create a new object in the project tree.

Master copies allow you to efficiently create the same or similar objects. By using master copies in a global library, these objects can be used in other projects.

##### Basics

You can use all objects as a master copy for recreation in the project tree:

- HMI devices, PLCs, technology objects, ...

  and the objects contained in these objects, e.g. cams
- Screens
- Tag tables
- Parameter set types
- Scripts

You can use objects as a master copy for recreation in a work area:

- Tags
- HMI alarms
- Tasks
- Cycles
- Text and graphic lists

Objects can be added as a master copy in the project library or in an open global library.

##### Basic procedure

Once you have used this method to create and edit an object that you want to use it as a master copy, drag-and-drop it onto the "Master copy" folder in a library.

Then drag-and-drop the master copy back into the project tree to create a new object that you can further customize.

#### Using a script as a master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is open.

##### Procedure

You can store a global module, a global definition area or a function as a master copy.

1. Open the "Scripts" editor in the project tree.
2. Drag-and-drop a script into the "Master copies" folder of a library.

##### Result

You have created a master copy from a script in the library.

##### Using a master copy

1. Drag-and-drop the master copy from the library into the "Scripts" folder in the project tree.

   A new script is created.
2. Edit the script.

#### Using a screen as a master copy (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is open.

##### Procedure

1. Open the "Screens" editor in the project tree.
2. Drag-and-drop the screen into the "Master copies" folder of a library.

##### Result

You have created a master copy from a screen in the library.

##### Using a master copy

1. Drag-and-drop the master copy from the library into the "Screens" folder in the project tree.

   A new screen has been created.
2. Edit the screen.

## Importing and exporting project data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Data exchange between projects and external applications (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#data-exchange-between-projects-and-external-applications-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting alarms
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing and exporting project texts
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-and-exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Data exchange between projects and external applications (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

WinCC gives you the option of exchanging project data between the projects or copying them to external applications.

#### Exporting and importing between projects

You can export the following project data from a project and import them into another project.

- Recipe data records
- Alarms
- Tags
- Text lists
- Project texts

Exporting and importing reduces the workload. Instead of creating new data records, you use data already created in previous projects.

#### Editing the export file

The following file formats are available for export and import depending on the editor:

- *.xlsx for alarms, tags, project texts and text lists
- *.csv for recipe data records

You can edit the import file in Excel, for example.

#### XLSX file format

XLSX format is a file format for Excel tables based on the Open XML format. XLSX files are optimized for Microsoft Excel 2007.

You can sort the columns as required in the XLSX file.

#### CSV file format

CSV stands for Comma Separated Value. In this format, the columns of the table that contain the names and the value of the entry are separated by semicolons. Each table row terminates with a line break. You can also open the CSV file for editing in Excel.

#### Importing project data

When project data is imported, the objects in the project are created.

The syntax of the import file is checked during import. The accuracy of the values imported and dependencies between the imported values are not checked.

Any errors found in the imported data are reported when the project is compiled.

#### Copying in Excel format

In all spreadsheet editors you can copy the content in Excel format into the buffer of your PC. Then you insert the project data in Excel format directly into any application outside the TIA Portal. To this purpose you use the corresponding command in the shortcut menu of the work area:

- If you select the command in the shortcut menu of the line header, the complete line is copied into the buffer.
- If you select the command in the shortcut menu of a cell, only the cell content is copied into the buffer.
- If you select several lines and select the command, all marked data are always copied into the buffer.

This data exchange is only possible as an export.

---

**See also**

[HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)

### Importing and exporting recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Exporting recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#exporting-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
- [Importing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
- [Exporting recipe data records (RT Professional)](#exporting-recipe-data-records-rt-professional)
- [Importing recipe data records (RT Professional)](#importing-recipe-data-records-rt-professional)
- [Editing exported recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-exported-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Format of data from recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#format-of-data-from-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Exporting recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

WinCC features an export function for exporting data records from recipes.

##### Requirements

- The WinCC project for the export is open.
- Recipes have been created in a project.
- The "Recipes" editor is open.

##### Exporting recipes

1. In the "Recipes" editor, select the recipe with the data records you want to export.
2. Click ![Exporting recipes](images/70947296011_DV_resource.Stream@PNG-de-DE.png).

   The "Export" dialog box opens.

   ![Exporting recipes](images/70613039755_DV_resource.Stream@PNG-en-US.png)

   ![Exporting recipes](images/70613039755_DV_resource.Stream@PNG-en-US.png)

   The selected recipe is shown under "Recipe selection".
3. Under "Content selection", specify if all or only selected data records are to be exported.
4. Under "File selection", specify the file in which the recipe data is to be stored.
5. Specify the list separator and decimal separator under "Data separation".
6. Click "Export."

   The export will start.

##### Result

The exported data has been written to a CSV file. The CSV file will be stored in the specified directory.

---

**See also**

[Importing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)

#### Importing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Recipes are identified by their name. The recipe name must therefore be unique. Open the import file in a simple text editor to check that it has the correct data structure.

Specify whether or not existing data records should be overwritten by records with the same name during the import.

##### Requirements

- A CSV file containing at least one recipe has been created.
- The WinCC project for the import is open.
- The "Recipes" editor is open with at least one recipe.

##### Importing a recipe

1. In the "Recipes" editor, select the recipe with the data records you want to import.
2. Click ![Importing a recipe](images/70960625547_DV_resource.Stream@PNG-de-DE.png).

   The "Import" dialog box opens.

   ![Importing a recipe](images/70625217931_DV_resource.Stream@PNG-en-US.png)

   ![Importing a recipe](images/70625217931_DV_resource.Stream@PNG-en-US.png)

   The selected recipe is shown under "Recipe selection".
3. Select the file you want to import under "File selection".
4. Under "Strategy", specify if existing data records should be overwritten by records of the same name.
5. Under "Data separation", select the list separator and the decimal separator to use in the CSV file.
6. Click "Import".

   The import will start.

**Note**

**Overwriting disabled**

If, when importing data records, it is determined that a data record ID to be imported already exists in the user archive, an error message is generated. An entry for the error message is stored in the log file "UALogFile.txt". The data records whose IDs do not exist in the user archive are added as new data records.

**Note**

**No check of import file for inconsistencies**

The import function doesn't check whether values that were changed in the CSV file between the export and import are still valid, e.g. whether these are still within the defined limits.

##### Result

The data records are created in the selected recipe. Depending on the setting for "Strategy", existing data records are overwritten by records with the same name from the CSV file.

Existing data records with the same name will also be imported from the CSV file if you deactivate the "Overwrite existing data records" option.

---

**See also**

[Exporting recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#exporting-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)

#### Exporting recipe data records (RT Professional)

##### Introduction

WinCC features an export function for exporting data records from recipes.

##### Requirements

- The WinCC project for export is open.
- Recipes have been created in a project.
- The "Recipes" editor is open.

##### Exporting recipes

1. In the "Recipes" editor, select the recipe with the data records you want to export.
2. Click ![Exporting recipes](images/70947296011_DV_resource.Stream@PNG-de-DE.png).

   The "Export" dialog box opens.

   ![Exporting recipes](images/22611557003_DV_resource.Stream@PNG-en-US.png)

   ![Exporting recipes](images/22611557003_DV_resource.Stream@PNG-en-US.png)

   The selected recipe is displayed under "Recipe name".
3. Under "File name", specify the file in which the recipe data is to be stored.
4. Under "Content selection", specify if all or only selected data records are to be exported.
5. Click "Export."

   The export will start.

##### Result

The exported data has been written to a CSV file. The CSV file will be stored in the specified directory.

#### Importing recipe data records (RT Professional)

##### Introduction

Recipes are identified by their name. The recipe name must therefore be unique. Open the import file in a simple text editor to check that it has the correct data structure.

Specify whether or not existing data records should be overwritten by records with the same name during the import.

##### Requirements

- A CSV file containing at least one recipe has been created.
- The WinCC project for import is open.
- The "Recipes" editor is open with at least one recipe.

##### Importing a recipe

1. In the "Recipes" editor, select the recipe with the data records you want to import.
2. Click ![Importing a recipe](images/70960625547_DV_resource.Stream@PNG-de-DE.png).

   The "Import" dialog box opens.

   ![Importing a recipe](images/22618278667_DV_resource.Stream@PNG-en-US.png)

   ![Importing a recipe](images/22618278667_DV_resource.Stream@PNG-en-US.png)

   The selected recipe is displayed under "Recipe name".
3. Select the file you want to import under "File name".
4. Under "Strategy", specify if existing data records should be overwritten by records of the same name.
5. Click "Import".

   The import will start.

**Note**

**Overwriting disabled**

If, when importing data records, it is determined that a data record ID to be imported already exists in the user archive, an error message is generated. An entry for the error message is stored in the log file "UALogFile.txt". The data records whose IDs do not exist in the user archive are added as new data records.

**Note**

**No check of import file for inconsistencies**

The import function doesn't check whether values that were changed in the CSV file between the export and import are still valid, e.g. whether these are still within the defined limits.

##### Result

The data records are created in the selected recipe. Existing data records may be overwritten by records with the same name from the CSV file depending on the setting for "Strategy".

#### Editing exported recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can edit the exported recipe data records and import them again. You can, for example, add new data records to the file or modify existing records. You edit the exported recipe data records in CSV files in Microsoft Excel.

##### Procedure

1. Start Microsoft Excel.
2. In the "File" menu, click "Open".

   The "Open File" dialog box opens.
3. Select the path in which the exported data record file is stored.

   In the "Open" dialog, select "All Files (*. *)" option in the drop-down list so that the exported file is detected.
4. Click "Open".

   The "Text Conversion Wizard" dialog opens.
5. Click the "Next" button in the next step.
6. In the second step, select the semicolon as a delimiter.

   Click "Next".
7. Close the wizard with the "Finish" button.
8. Make the desired changes to the file.
9. Save the changed file in CSV format (comma delimited).
10. Import the changed file.

    If you have saved the file under a different name, adapt the file name in the "Import" dialog before importing.

##### Result

The exported recipe data records were edited and saved in a recipe.

---

**See also**

[Importing recipe data records (RT Professional)](#importing-recipe-data-records-rt-professional)

#### Format of data from recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

This section describes the required format of the file for the import of recipes. The file containing the data of the recipes must be available in "*.csv" format. :

##### Structure of recipe data

The structure of the import file is fixed. The following example shows the structure of a recipe containing two recipe elements, each with two data records:

"ID";&lt;**Name, recipe element 1**&gt;;&lt; **Name, recipe element 2**&gt;;"LastUser";"LastAccess[UTC]"&lt;Line break&gt;

&lt;**Recipe data record number 1**&gt;;&lt;**Recipe data record 1 value 1**&gt;;&lt;**Recipe data record 1 value 2**&gt;;"**&lt;Last user 1&gt;**";**&lt;Date and time 1&gt;**&lt;Line break&gt;

&lt;**Recipe data record number 2**&gt;;&lt;**Recipe data record 2 value 1**&gt;;&lt;**Recipe data record 2 value 2**&gt;;"**&lt;Last user 2&gt;**";**&lt;Date and time 2&gt;**&lt;Line break&gt;

##### ID of the language

The recipe always has the first line, which is the header and describes the column headings. Only the names of the recipe elements are added dynamically.

Each additional line represents one recipe data record with its recipe element values and change information.

### Importing and exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Importing alarms (RT Professional)](#importing-alarms-rt-professional)
- [Format of the analog alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#format-of-the-analog-alarm-data-basic-panels-panels-comfort-panels-rt-advanced)
- [Format of the discrete alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#format-of-the-discrete-alarm-data-basic-panels-panels-comfort-panels-rt-advanced)
- [Format of the analog alarm data (RT Professional)](#format-of-the-analog-alarm-data-rt-professional)
- [Format of the discrete alarm data (RT Professional)](#format-of-the-discrete-alarm-data-rt-professional)

#### Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC has an export function for alarms.

##### Requirements

- The WinCC project for the export is open.
- Alarms have been created in the project.
- The "HMI alarms" editor is open.

##### Exporting alarms

1. Click the ![Exporting alarms](images/70613019147_DV_resource.Stream@PNG-de-DE.png) button in "Discrete alarms" or "Analog alarms".

   The "Export" dialog box opens.

   ![Exporting alarms](images/70627232267_DV_resource.Stream@PNG-en-US.png)

   ![Exporting alarms](images/70627232267_DV_resource.Stream@PNG-en-US.png)
2. Click the "..." button and specify in which file the data are saved.
3. Specify whether you want to export "Disrete alarms" or "Analog alarms".
4. Click "Export". The export will start.

##### Result

The exported data has been written to an xlsx file. The xlsx file will be stored in the specified folder.

---

**See also**

[Format of the analog alarm data (RT Professional)](#format-of-the-analog-alarm-data-rt-professional)
  
[Format of the discrete alarm data (RT Professional)](#format-of-the-discrete-alarm-data-rt-professional)

#### Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Alarms are identified by their alarm number. The alarm numbers must be unique in the analog and discrete alarm types. Alarms with redundant alarm numbers will be overwritten. An alarm without an existing alarm number is created.

Any empty list entries for existing alarms contained in an xlsx file will be ignored for the purposes of the import. The entries of the existing alarms remain active and will not be replaced by empty ones.

##### Requirements

- An xlsx file with alarms has been created.
- The structure of the xlsx file meets the requirements.
- The WinCC project for the import is open.
- The "HMI alarms" editor is open.

##### Importing alarms

1. Click the ![Importing alarms](images/70613888907_DV_resource.Stream@PNG-de-DE.png) button in "Discrete alarms" or "Analog alarms". The "Import" dialog box opens.

   ![Importing alarms](images/70630913291_DV_resource.Stream@PNG-en-US.png)

   ![Importing alarms](images/70630913291_DV_resource.Stream@PNG-en-US.png)
2. Click the "..." button and select the file that you want to import.
3. Click on the "Import" button. The import will start. A progress bar indicates the progress of the import operation.

##### Result

The corresponding alarms including alarm texts are created in WinCC on the basis of the import data. Alarms relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example dynamic parameters such as tags. These parameters must be available in all languages to be imported.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

> **Note**
>
> The syntax of the import file is checked during xlsx file import. The meaning of the properties or dependencies between the properties is not checked. It is possible to assign an alarm a trigger tag of the incorrect type, such as String. An error will be reported during compilation.

---

**See also**

[Format of the analog alarm data (RT Professional)](#format-of-the-analog-alarm-data-rt-professional)
  
[Format of the discrete alarm data (RT Professional)](#format-of-the-discrete-alarm-data-rt-professional)

#### Importing alarms (RT Professional)

##### Introduction

Alarms are identified by their alarm name. An existing alarm will be overwritten with the data from the xlsx file if the alarm name already exists in the project. A new alarm is created if the alarm does not yet exist.

The alarm numbers must be unique in the project. If an alarm number is assigned more than once by import, the alarm is imported and the alarm number marked as invalid.

##### Requirements

- An xlsx file with alarms has been created.
- The structure of the xlsx file meets the requirements.
- The WinCC project for the import is open.
- The "HMI alarms" editor is open.

##### Importing alarms

1. Click the ![Importing alarms](images/70613888907_DV_resource.Stream@PNG-de-DE.png) button in "Discrete alarms" or "Analog alarms". The "Import" dialog box opens.

   ![Importing alarms](images/70630913291_DV_resource.Stream@PNG-en-US.png)

   ![Importing alarms](images/70630913291_DV_resource.Stream@PNG-en-US.png)
2. Click the "..." button and select the file that you want to import.
3. Click on the "Import" button. The import will start. A progress bar indicates the progress of the import operation.

**Note**

There are no option settings for alarm import.

##### Result

The corresponding alarms including alarm texts are created in WinCC on the basis of the import data. Messages relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example, dynamic parameters such as tags.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

> **Note**
>
> The syntax of the import file is checked during xlsx file import. The meaning of the properties or dependencies between the properties is not checked. It is possible to assign a trigger tag of an incorrect type, such as string, to an alarm. An error will be reported during compilation.

#### Format of the analog alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

This chapter describes the required format of the file for the import of analog alarms. The file containing the analog alarm data must be in "*.xlsx" format.

##### Structure of the alarm data

The import file in Microsoft Excel consists of a number of worksheets:

- Analog alarms(Analog alarms)
- Limits (Limits)

Each alarm is assigned a separate row in the import file. The import file with the analog alarms must be formatted as follows:

##### Example of the worksheet "Analog alarms"

![Example of the worksheet "Analog alarms"](images/76071169803_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| ID | The alarm number is used to reference an alarm. The alarm number is unique. Alarms with identical alarm numbers are overwritten during import. An alarm without an existing alarm number is created. |
| Name | Name of the analog alarm |
| Event text [de-DE], Alarm text | Displays the alarm text. The field designation contains a language ID. Alarm texts must be assigned a language ID for import.  An expression with a reference ID will be added to the alarm text if the text has a dynamic parameter. Example: text &lt;field ref="0" /&gt;. Use the ID to assign dynamic parameters to alarm texts. |
| FeldInfo | Specifies whether the alarm text contains dynamic parameters. The settings are separated by a semicolon ";".   Example of dynamic parameters:  Tag: &lt;ref id = 0; type = AlarmTag; Tag = Tag1; DisplayType = Decimal; Length = 5;&gt;  Text list: &lt;ref id = 1; type = CommonTextList; TextList = Textlist1; Tag = tag 2; Length = 5;&gt; |
| Class | The class of an alarm determines whether or not the alarm must be acknowledged. It can also be used to determine how the alarm appears when it is displayed on the HMI device. The alarm class also determines whether and where the corresponding alarm will be logged. |
| Group | Indicates the allocation to an alarm group. If an alarm belongs to a group with other alarms, it can be acknowledged together with these alarms of the same group in a single operation. |
| Trigger tag | Specifies the tag monitored for limit value violation. |
| Delay time value | Specifies the delay time. The alarm is not triggered until the duration of the limit value violation equals the specified delay time. |
| Delay time unit | Specifies the time unit for the delay. |
| Report | Enables reporting of the specific alarm on a printer.  True or "1" = Reporting enabled.  False or "0" = Reporting disabled.  Reporting must also be globally enabled in the project. |
| Info text [de-DE], Info text | The tooltip is an optional property of an alarm. Tooltips can contain additional information about the alarm. A tooltip will be displayed in a separate window on the HMI device when the operator presses the &lt;HELP&gt; key.  The field designation contains a language ID. |

##### Example of the worksheet "Limits"

![Example of the worksheet "Limits"](images/76071174923_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Alarm ID | Alarm number  The alarm number is used to reference an alarm. The alarm number is unique. Alarms with identical alarm numbers are overwritten during import. An alarm without an existing alarm number is created. |
| Limit mode | Trigger mode  Indicates the method used for monitoring the limit value. |
| Limit type | Specifies the limit that will be monitored. Both a tag and a constant can be used as limit value. |
| Limit value | Limit value  Indicates the tag or constant monitored for limit violation. |
| Deadband mode | Hysteresis mode  Specifies whether and in which cases hysteresis will be used.  For "Outgoing"  For "Incoming"  For "Incoming" and "Outgoing" |
| Deadband in percent | 0 = The value specified for "Hysteresis" is considered to be absolute.  1 = The value specified for "Hysteresis" is referred to as a percentage of the limit value. |
| Deadband mode | Hysteresis  Specifies a constant as a value of the hysteresis. |
|  |  |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing alarm of the same name.

---

**See also**

[Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Format of the discrete alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#format-of-the-discrete-alarm-data-basic-panels-panels-comfort-panels-rt-advanced)

#### Format of the discrete alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

This chapter describes the required format of the file for the import of discrete alarms. The file containing the discrete alarm data must be in "*.xlsx" format.

##### Structure of the alarm data

The import file in Microsoft Excel consists of the worksheets "Discrete alarms" (discrete alarms). Each alarm is assigned a separate row in the import file. Structure of the import file containing the discrete alarms:

##### Example of the worksheet "Discrete alarms"

![Example of the worksheet "Discrete alarms"](images/111982039819_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| ID | The alarm number is used to reference an alarm. The alarm number is unique. Alarms with identical alarm numbers are overwritten during import. An alarm without an existing alarm number is created. |
| Name | Name of the analog alarm |
| Event text [de-DE], Alarm text | Displays the alarm text. The field designation contains a language ID. For import, a language ID must be assigned to alarm text.  An expression with a reference ID will be added to the alarm text if the text has a dynamic parameter. Example: text &lt;field ref="0" /&gt;. Use the ID to assign dynamic parameters to alarm texts. |
| FeldInfo | Specifies whether the alarm text contains dynamic parameters. The settings are separated by a semicolon ";".   Example of dynamic parameters:  Tag: &lt;ref id = 0; type = AlarmTag; Tag = Tag1; DisplayType = Decimal; Length = 5;&gt;  Text list: &lt;ref id = 1; type = CommonTextList; TextList = Textlist1; Tag = tag 2; Length = 5;&gt; |
| Class | The class of an alarm determines whether or not the alarm must be acknowledged. It can also be used to determine how the alarm appears when it is displayed on the HMI device. The alarm class also determines whether and where the corresponding alarm will be logged. |
| Group | Indicates the allocation to an alarm group. If an alarm belongs to a group with other alarms, it can be acknowledged together with these alarms of the same group in a single operation. |
| Trigger tag | Specifies the tag containing the bit that triggers the alarm. |
| Trigger bit | Specifies the number of the bit that triggers the alarm. |
| Acknowledge tag | Specifies the tag containing the bit that is set by the operator upon acknowledgment. Only available if the selected alarm class requires alarm acknowledgment. |
| Acknowledgment bit | Specifies the number of the bit that is set when the operator acknowledges the alarm. |
| PLC acknowledgement tag | Specifies the tag containing the bit that acknowledges the alarm of the control program. Only available if the selected alarm class requires alarm acknowledgment. |
| PLC acknowledgment bit | Specifies the number of the bit that acknowledges the alarm of the control program. |
| Delay time value | Specifies the delay time. The alarm is not triggered until the duration of the limit value violation equals the specified delay time. |
| Delay time unit | Specifies the time unit for the delay. |
| Report | Enables reporting of the specific alarm on a printer.  True or "1" = Reporting enabled.  False or "0" = Reporting disabled.  Reporting must also be globally enabled in the project. |
| Info text [de-DE], Info text | The tooltip is an optional property of an alarm. Tooltips can contain additional information about the alarm. A tooltip will be displayed in a separate window on the HMI device when the operator presses the &lt;HELP&gt; key.  The field designation contains a language ID. |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing alarm of the same name.

---

**See also**

[Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Format of the analog alarm data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#format-of-the-analog-alarm-data-basic-panels-panels-comfort-panels-rt-advanced)

#### Format of the analog alarm data (RT Professional)

##### Introduction

This chapter describes the required format of the file for the import of analog alarms. The file containing the analog alarm data must be in "*.xlsx" format.

##### Structure of the alarm data

The import file in Microsoft Excel consists of two worksheets:

- Analog alarms(Analog alarms)
- Limits (Limits)

Each alarm is assigned a separate line in the import file. The import file with the analog alarms must be formatted as follows:

##### Example of the worksheet "Analog alarms"

![Example of the worksheet "Analog alarms"](images/111982242187_DV_resource.Stream@PNG-en-US.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| ID | Shows the number of the analog alarm. The alarm number must be unique in the project. |
| Name | Shows the name of the analog alarm. The name is used to reference an alarm. Alarms with identical names are overwritten during import. An alarm without an existing name is created. |
| Event text [de-DE], Alarm text | Displays the alarm text. The field designation contains a language ID. Alarm texts must be assigned a language ID for import.  An expression with a reference ID will be added to the alarm text if the text has a dynamic parameter. Example: text &lt;field ref="0" /&gt;. Use the ID to assign dynamic parameters to alarm texts. |
| FeldInfo | Specifies whether the alarm text contains dynamic parameters. The settings are separated by a semicolon ";".   Example of dynamic parameters:  Parameter: &lt;ref id = 0; type = AlarmAnalogParameter; Parameter = Limit; DisplayType = Decimal; Length = 1; Precision = 0; Alignment = Right; ZeroPadding = False;&gt;  System parameters: &lt;ref id = 0; type = CommonSystemParameter; SystemParameter = UserName;&gt; |
| Class | The alarm class of an alarm determines whether or not the alarm has to be acknowledged. It can also be used to determine how the alarm appears when it is displayed on the HMI device. The alarm class also determines whether and where the corresponding alarm will be logged. |
| Group | Indicates the allocation to an alarm group. If an alarm belongs to a group with other alarms, it can be acknowledged along with these alarms of the same group in a single operation. |
| Priority | Indicates alarm priority. You can sort the alarms in the alarm view by priority. Range: 0 -16 |
| CPU number | Specifies the CPU number. This option is only activated if you have enabled the "CPU/PLC number" alarm text block in the "Alarm blocks &gt; System blocks" tab in the "HMI alarms" editor. |
| PLC number | Shows the PLC number. This option is only activated if you have enabled the "CPU/PLC number" alarm text block in the "Alarm blocks &gt; System blocks" tab in the "HMI alarms" editor. |
| Trigger tag | Specifies the tag monitored for limit value violation. |
| Verzögerung | Specifies the delay time. The alarm is not triggered until the duration of the limit value violation equals the specified delay time. |
| Delay time unit | Specifies the time unit for the delay. |
| Acknowledge tag | Specifies the tag containing the bit that is set by the operator upon acknowledgment. Only available if the selected alarm class requires alarm acknowledgment. |
| Acknowledgment bit | Specifies the number of the bit that is set when the operator acknowledges the alarm. |
| Single acknowledgment | Specifies whether each individual alarm must be acknowledged.  True = Alarms must be acknowledged individually. |
| Status tag | Shows the tag which saves the Incoming and Outgoing alarm statuses and the  Acknowledgement request saved. |
| Status bit | Specifies the number of the bit that is set and acknowledges the alarm. |
| Alarm annonciation | Indicates whether an alarm is being suppressed.  True = suppressed alarm. |
| Display suppresion mask | Indicates the display suppression method. |
| Additonal Text | Shows the additional alarm text. |
| Info text [de-DE], Info text | The tooltip is an optional property of an alarm. Tooltips can contain additional information about the alarm. A tooltip will be displayed in a separate window on the HMI device when the operator presses the &lt;HELP&gt; key.  The field designation contains a language ID. |

##### Example of the worksheet "Limits"

![Example of the worksheet "Limits"](images/111982246795_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Alarm ID | The alarm number is used to reference an alarm. The alarm number is unique. The alarm number allows alarms to be assigned limits. |
| Name | Shows the name of the analog alarm. |
| Limit mode | Indicates the method used for monitoring the limit value. |
| Grenzen  Limit type | Specifies the limit that will be monitored. Both a tag and a constant can be used as limit value. |
| Limit value | Indicates the tag or constant monitored for limit violation. |
| Suppression | Indicates whether an alarm is being suppressed.  True = suppressed alarm. |
| Deadband mode | Specifies whether and in which cases hysteresis will be used.  For "Outgoing"  For "Incoming"  For "Incoming" and "Outgoing" |
| Deadband in percent | 0 = The value specified for "Hysteresis" is interpreted as absolute.  1 = The value specified for "Hysteresis" is a percentage value of the limit value. |
| Deadband mode | Specifies a constant as value of the hysteresis. |
|  |  |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing alarm of the same name.

---

**See also**

[Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-alarms-basic-panels-panels-comfort-panels-rt-advanced)

#### Format of the discrete alarm data (RT Professional)

##### Introduction

This chapter describes the required format of the file for the import of discrete alarms. The file containing the discrete alarm data must be in "*.xlsx" format.

##### Structure of the alarm data

The import file in Microsoft Excel consists of the worksheet "Discrete alarms" (discrete alarms). Each alarm is assigned a separate line in the import file. Structure of the import file containing the discrete alarms:

##### Example of the worksheet "Discrete alarms"

![Example of the worksheet "Discrete alarms"](images/22647437707_DV_resource.Stream@PNG-en-US.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| ID | Shows the number of the discrete alarm. The alarm number is unique. |
| Name | Shows the name of the discrete alarm. The name is used to reference an alarm. Alarms with identical names are overwritten during import. An alarm without an existing name is created. |
| Event text [de-DE], Alarm text | Displays the alarm text. The field designation contains a language ID. Alarm texts must be assigned a language ID for import.  An expression with a reference ID will be added to the alarm text if the text has a dynamic parameter. Example: text &lt;field ref="0" /&gt;. Use the ID to assign dynamic parameters to alarm texts. |
| FeldInfo | Specifies whether the alarm text contains dynamic parameters. The settings are separated by a semicolon ";".   Example of dynamic parameters:  Parameter: &lt;ref id = 0; type = AlarmDiscreteParameter; Parameter = Parameter 1; Tag = HMI_Variable_1; DisplayType = Decimal; Length = 5; Precision = 0; Alignment = Right; ZeroPadding = False;&gt;  System parameters: &lt;ref id = 0; type = CommonSystemParameter; System Parameter = UserName;&gt; |
| Class | The alarm class of an alarm determines whether or not the alarm has to be acknowledged. It can also be used to determine how the alarm appears when it is displayed on the HMI device. The alarm class also determines whether and where the corresponding alarm will be logged. |
| Group | Indicates the allocation to an alarm group. If an alarm belongs to a group with other alarms, it can be acknowledged along with these alarms of the same group in a single operation. |
| Priority | Indicates alarm priority. You can sort the alarms in the alarm view by priority. Range: 0 -16 |
| CPU number | Specifies the CPU number. This option is only activated if you have enabled the "CPU/PLC number" alarm text block in the "Alarm blocks &gt; System blocks" tab in the "HMI alarms" editor. |
| PLC number | Shows the PLC number. This option is only activated if you have enabled the "CPU/PLC number" alarm text block in the "Alarm blocks &gt; System blocks" tab in the "HMI alarms" editor. |
| Trigger tag | Specifies the tag containing the bit that triggers the alarm. |
| Trigger bit | Specifies the number of the bit that triggers the alarm. |
| Trigger mode | Indicates the method used for monitoring the limit value. |
| Alarm parameter | Indicates tag assigned to a parameter block to issue process values in alarm texts. |
| Acknowledge tag | Specifies the tag containing the bit that is set by the operator upon acknowledgment. Only available if the selected alarm class requires alarm acknowledgment. |
| Acknowledgment bit | Specifies the number of the bit that is set when the operator acknowledges the alarm. |
| Single acknowledgment | Specifies whether each individual alarm must be acknowledged.  True = Alarms must be acknowledged individually. |
| Status tag | Shows the tag which saves the Incoming and Outgoing alarm statuses and the  Acknowledgement request saved. |
| Status bit | Specifies the number of the bit that is set and acknowledges the alarm. |
| Alarm annonciation | Indicates whether an alarm is being suppressed.  True = suppressed alarm. |
| Display suppresion mask | Indicates the display suppression method. |
| Additonal Text | Shows the additional alarm text. |
| Info text [de-DE], Info text | The tooltip is an optional property of an alarm. Tooltips can contain additional information about the alarm. A tooltip will be displayed in a separate window on the HMI device when the operator presses the &lt;HELP&gt; key.  The field designation contains a language ID. |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing alarm of the same name.

---

**See also**

[Exporting alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-alarms-basic-panels-panels-comfort-panels-rt-advanced)

### Importing and exporting tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Exporting tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing tags (WinCC V13 SP1 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-tags-wincc-v13-sp1-or-higher-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing tags (prior to WinCC V13 SP1) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-tags-prior-to-wincc-v13-sp1-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Format of the tag data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#format-of-the-tag-data-basic-panels-panels-comfort-panels-rt-advanced)
- [Format of the tag data (RT Professional)](#format-of-the-tag-data-rt-professional)

#### Exporting tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC has an export function for tags.

##### Requirements

- The WinCC project for the export is open.
- Tags have been created in the project.
- The "HMI tags" editor is open.

##### Exporting tags

1. Click on the ![Exporting tags](images/70613019147_DV_resource.Stream@PNG-de-DE.png) button in the "HMI Tags" tab.

   The "Export" dialog box opens.

   ![Exporting tags](images/75166390539_DV_resource.Stream@PNG-en-US.png)

   ![Exporting tags](images/75166390539_DV_resource.Stream@PNG-en-US.png)
2. Click the "..." button and specify in which file the data are saved.
3. Click "Export". The export will start.

> **Note**
>
> The version number of the xlsx file with the exported tags depends on the TIA Portal version. If the xlsx file was exported from a project in WinCC V13 SP1, it has the version number 1.2. If the xlsx file was exported from a project prior to WinCC V13 SP1, it has the version number 1.1.

> **Note**
>
> It is not possible to export HMI tags of the data type "UDT" which contain structured elements via Excel for subsequent editing.
>
> After export, only the higher-level HMI tag appears in Excel. Its lower-level elements cannot be edited.

##### Result

The exported data has been written to an xlsx file. The xlsx file will be stored in the specified folder.

#### Importing tags (WinCC V13 SP1 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Tags are identified by the tag name. An existing tag is overwritten with the data from the xlsx file if the tag name already exists in the project. A new tag is created if the tag does not yet exist.

##### Requirements

- An xlsx file with tags has been created.
- The structure of the xlsx file meets the requirements.
- The WinCC project for the import is open.

##### Importing tags

1. Click "HMI tags" in the project navigation.
2. Double-click "Show all tags". The "HMI tags" editor opens.
3. Click the ![Importing tags](images/70613888907_DV_resource.Stream@PNG-de-DE.png) button. The "Import" dialog box opens.

   ![Importing tags](images/76071197963_DV_resource.Stream@PNG-en-US.PNG)

   ![Importing tags](images/76071197963_DV_resource.Stream@PNG-en-US.PNG)
4. Click the "..." button and select the file that you want to import.
5. Click on the "Import" button. The import will start.

##### Result

The relevant tags have been created in WinCC. Alarms relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example, dynamic parameters such as tags.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

> **Note**
>
> The syntax of the import file is checked during xlsx file import. The meaning of the properties or dependencies between the properties is not checked. It is possible to assign a tag a trigger tag of the wrong type, for example, string. An error will be reported during compilation.

#### Importing tags (prior to WinCC V13 SP1) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Tags are identified by the tag name. An existing tag is overwritten with the data from the xlsx file if the tag name already exists in the project. A new tag is created if the tag does not yet exist.

The version number of the xlsx file depends on the TIA Portal version. If the xlsx file was exported from a project in WinCC V13 SP1, it has the version number 1.2. If the xlsx file was exported from a project prior to WinCC V13 SP1, it has the version number 1.1.

To import files with the version number 1.2 into a project that was created prior to WinCC V13 SP1, you must prepare the files.

##### Requirements

- An xlsx file with tags has been created.
- The structure of the xlsx file meets the requirements.
- The WinCC project for the import is open.

##### Preparing files for the import

1. Open the corresponding file in Microsoft Excel.
2. Select "File &gt; Properties &gt; Advanced properties".

   The "Properties" dialog is opened.
3. Switch to the "Fit to size" task card.
4. Select "TIA_Version" in the "Properties" area.
5. Change the value in the column from "1.2" to "1.1".
6. Click the "Change" button.
7. Click "OK".
8. Delete the right column "Synchronization" in the file.
9. Save the file.

##### Importing tags

1. Click "HMI tags" in the project navigation.
2. Double-click "Show all tags". The "HMI tags" editor opens.
3. Click the button. The "Import" dialog box opens.
4. Click the "..." button and select the file that you want to import.
5. Click on the "Import" button. The import will start.

##### Result

The relevant tags have been created in WinCC. Alarms relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example, dynamic parameters such as tags.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

> **Note**
>
> The syntax of the import file is checked during xlsx file import. The meaning of the properties or dependencies between the properties is not checked. It is possible to assign a tag a trigger tag of the wrong type, for example, string. An error will be reported during compilation.

#### Format of the tag data (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

This section describes the format required for the file with tag data used for imports. The tag data file must be in "*.xlsx" format.

##### Tag data structure

The import file in Microsoft Excel consists of a number of worksheets:

- HMI Tags (HMI tags)
- Multiplexing (multiplex tags)

Each tag is on a separate line in the import file. The import file with the tag data must have the following format:

##### Example of the worksheet "HMI Tags"

![Example of the worksheet "HMI Tags"](images/111983227659_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Indicates the configured name of an HMI tag. |
| Path | Specifies which folders in the project tree contain the tag. The folder structure is represented by "\" : "FolderName1\FolderName2\TagName". |
| PLC Tag | Indicates whether the tag is linked to a PLC tag. |
| Connection | Indicates the name of the connection to the PLC. |
| Data type | Specifies the data type of a tag. The data types allowed depend on the communication driver being used. See the "Communication" section of the documentation for additional information on the data types permitted for the various communication drivers. |
| Length | Specifies the length of the tag. This entry is only useful for data types with a dynamic length such as strings; it is left empty for all other data types. |
| Address | Specifies the tag address in the PLC. The tag address must exactly match the one used in WinCC, for example, "%DB1.DBW0". The tag address is empty for internal tags. |
| Multiplexing | Specifies whether multiplexing is used. |
| Index tag | Shows the name of the index tag for multiplexing.   In Runtime, the system first reads the value of the index tag. It then accesses the tag in the corresponding place in the tag list. |
| StartValue | Specifies the start value of a tag. |
| ID tag | The update ID updates the value of a tag with the aid of a function or a PLC job. The update ID must be unique within an HMI device. |
| Coding | Shows the coding method. |
| DiplayName [de_DE] | Shows the display name of an HMI tag. The field designation contains a language ID. The field designation contains a language ID. Display names must be assigned a language ID for import. Texts are imported to the corresponding project language. |
| Acquisition mode | Specifies the tag acquisition mode. |
| Acquisition cycle | Specifies the tag acquisition cycle. The acquisition cycle must correspond exactly to the one used in WinCC. The value is not language-dependent and should therefore be the same in every language. The default value is "1 s". The acquisition cycle is undefined if the tag acquisition mode is "on demand".  User-defined acquisition cycles must be created beforehand as the file will otherwise not be imported. |
| High High Limit type | Indicates whether the limit value "High high" is monitored by a constant, a tag or not at all. |
| High High Limit | Displays the limit value "High High". |
| High Limit type | Indicates whether the limit value "High" is monitored by a constant, a tag or not at all. |
| High Limit | Displays the limit value "High". |
| Low Limit type | Indicates whether the limit value "Low" is monitored by a constant, a tag or not at all. |
| Low Limit | Displays the limit value "Low". |
| Low Low Limit type | Indicates whether the limit value "Low Low" is monitored by a constant, a tag or not at all. |
| Low Low Limit | Displays the limit value "Low Low". |
| Linear scaling | Indicates whether linear scaling is enabled. This entry can only be used for external tags. |
| End value PLC | Specifies the end value of the PLC tag. |
| Start value PLC | Specifies the start value of the PLC tag. |
| End value HMI | Specifies the end value of the HMI tag. |
| Start value HMI | Specifies the start value of the HMI tag. |

##### Example of the worksheet "Multiplexing"

![Example of the worksheet "Multiplexing"](images/22652016395_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Indicates the configured name of an HMI tag which uses indirect addressing. The HMI tag must be available in the "HMI Tags" worksheet. |
| Index | Shows the value which governs which tag is selected. |
| Multiplex Tag | Displays the tag from the tag list corresponding to the index value. |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing tag of the same name.

#### Format of the tag data  (RT Professional)

##### Introduction

This section describes the format required for the file with tag data used for imports. The tag data file must be in "*.xlsx" format.

##### Tag data structure

The import file in Microsoft Excel consists of a number of worksheets:

- HMI Tags (tags)
- SubstituteValueUsage (substitute value)

Each tag is on a separate line in the import file. The import file with the tag data must have the following format:

##### Example of the worksheet "HMI Tags"

![Example of the worksheet "HMI Tags"](images/111983504907_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Indicates the configured name of an HMI tag. |
| Path | Specifies which folders in the project tree contain the tag. The folder structure is represented by ",": "FolderName1,FolderName2,TagName". |
| PLC Tag | Specifies which PLC tag is linked to the HMI tag. |
| Connection | Indicates the name of the connection. |
| Date type | Specifies the data type of the PLC tag. The data types allowed depend on the communication driver being used. See the "Communication" section of the documentation for additional information on the data types permitted for the various communication drivers. |
| HMI Data type | Specifies the data type of the HMI tag. The data types allowed depend on the communication driver being used. See the "Communication" section of the documentation for additional information on the data types permitted for the various communication drivers. |
| Length | Specifies the length of the tag in bytes. This entry is only useful for data types with a dynamic length such as strings; it is left empty for all other data types. |
| Address | Specifies the tag address in the PLC. The tag address must exactly match the one used in WinCC, for example, "%DB1.DBW0". The tag address is empty for internal tags. |
| Start Value | Specifies the start value of a tag. |
| Substitute Value | Indicates the substitute value. The substitute value is used when a process value with errors is read. |
| ID tag | The update ID updates the value of a tag with the aid of a function or a PLC job within a device. The update ID must be unique. |
| High High Limit type | Indicates whether the limit value "High high" is monitored by a constant or not at all. |
| High High Limit | Displays the limit value "High High". |
| High Limit type | Indicates whether the limit value "High" is monitored by a constant or not at all. |
| High Limit | Displays the limit value "High". |
| Low Limit type | Indicates whether the limit value "Low" is monitored by a constant or not at all. |
| Low Limit | Displays the limit value "Low". |
| Low Low Limit type | Indicates whether the limit value "Low Low" is monitored by a constant or not at all. |
| Low Low Limit | Displays the limit value "Low Low". |
| Linear scaling | Indicates whether linear scaling is enabled. This entry can only be used for external tags. |
| End value PLC | Specifies the end value of the PLC tag. |
| Start value PLC | Specifies the start value of the PLC tag. |
| End value HMI | Specifies the end value of the HMI tag. |
| Start value HMI | Specifies the start value of the HMI tag. |

##### Example of the worksheet "SubstituteValueUsage"

![Example of the worksheet "SubstituteValueUsage"](images/31177091211_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Parent | Specifies the tag for which a substitute value has been defined. The tag must be available in the "HMI-Tags" worksheet. |
| Substitute Value Usage | Indicates the substitute value. The substitute value can be used in the following situations:  - As start value - After communication error - High High limit value - Low Low limit value |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing tag of the same name.

### Importing and exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Format of text list data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#format-of-text-list-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC has an export function for text lists.

##### Requirements

- The WinCC project for the export is open.
- Text lists have been created in the project.
- The "Text &amp; graphics lists" editor is open.

##### Exporting text lists

1. Click on the ![Exporting text lists](images/70613019147_DV_resource.Stream@PNG-de-DE.png) button in the "TextLists" tab.

   The "Export" dialog box opens.

   ![Exporting text lists](images/60868141451_DV_resource.Stream@PNG-en-US.png)

   ![Exporting text lists](images/60868141451_DV_resource.Stream@PNG-en-US.png)
2. Click the "..." button and specify in which file the data are saved.
3. By default, texts are exported in all defined project languages.

   If you do not want to export specific languages, disable the unnecessary languages in the dialog.
4. Click "Export". The export will start.

##### Result

The exported data has been written to an xlsx file. The xlsx file will be stored in the specified folder.

---

**See also**

[Importing text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Format of text list data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#format-of-text-list-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Importing text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You then import text lists from an xlsx file to WinCC.

##### Requirements

- An xlsx file with text lists has been created.
- The structure of the xlsx file meets the requirements.
- The WinCC project for the import is open.
- The "Text &amp; graphics lists" editor is open.

##### Importing text lists

1. Click on the ![Importing text lists](images/70613888907_DV_resource.Stream@PNG-de-DE.png) button in the "Text lists" tab.

   The "Import" dialog box opens.

   ![Importing text lists](images/70636427275_DV_resource.Stream@PNG-en-US.png)

   ![Importing text lists](images/70636427275_DV_resource.Stream@PNG-en-US.png)
2. Select the file you want to import under "File selection".
3. Click on the "Import" button. The import will start.

##### Result

You have now imported the text lists. The relevant text lists have been created in WinCC. Alarms relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example, dynamic parameters such as tags.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

---

**See also**

[Exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Format of text list data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

This section describes the format required for the file with the text lists used for imports. The text list data file must be in "*.xlsx" format.

##### Tag data structure

The import file in Microsoft Excel consists of two worksheets:

- TextList (Text lists)
- TextListEntry (Text list entry)

Each text list is assigned a separate line in the import file. The import file containing the data must be structured as follows:

##### Example of the worksheet "TextList"

![Example of the worksheet "TextList"](images/76071215499_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Shows the name of the text list. |
| ListRange | Shows the text list range: Number = Bit number (0-31) Range = value/range (...-...) Bit = Bit (0;1) |
| Comment | Any comments on the text list. You can use up to 500 characters |

##### Example of the worksheet "TextListEntry"

![Example of the worksheet "TextListEntry"](images/111983783947_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Shows the name of the text list entry. |
| Parent | Specifies the name of the corresponding text list. |
| DefaultEntry | Indicates whether the text list entry is a default entry. The default entry is always displayed when the tag has an undefined value. |
| Value | Specifies the tag integer values or value ranges which are assigned to the text entries in the text list. |
| Text | Shows the text list entry. The field designation contains a language ID. Text list entries must be assigned a language ID for import.   An expression with a reference ID will be added to the text if the text list entry has a dynamic parameter. Example: text &lt;field ref="0" /&gt;. Use the ID to assign the dynamic parameter to a text list entry. |
| FeldInfo | Specifies whether the text list contains dynamic parameters. The settings are separated by a semicolon ";".   Example of dynamic parameters:  Tag: &lt;ref id = 0; type = CommonTagDisplayFormat; Tag = tag 1; DisplayType = Decimal; DisplayFormat = 9;&gt;  Text list: &lt;ref id = 1; type = CommonTextList; TextList = Textliste_1; Tag = tag 2; Length = 5;&gt;  PLC tag: &lt;ref id = 0; type = CommonControlTagDisplayFormat; DisplayType = Decimal; DisplayFormat = 9;&gt; |

---

**See also**

[Exporting text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Importing and exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Edit the xlsx file or send it to a translator. Import the texts once they have been translated. The foreign languages will be imported to the relevant object in the project.

> **Note**
>
> In WinCC, you only import the previously exported project texts into the same project. Importing into a different project is not supported.

> **Note**
>
> Once a project has been saved under a new name with "Save as …", the import of texts is no longer possible.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor, e.g. Italian and French.

##### Importing project texts

To import a file with project texts, proceed as follows:

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The lower-level elements will be displayed.
2. Double-click on "Project texts". The "Project texts" editor will open.
3. Click the ![Importing project texts](images/24534696459_DV_resource.Stream@PNG-de-DE.png) button. The "Import" dialog box opens.
4. Select the path and file name of the import file from the "Import file" field.
5. Activate the "Import source language" check box if you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes.
6. Click on "Import".

##### Result

You have imported the project texts.

#### Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Project texts are exported for translation. Texts are exported to Office Open XML files ending in ".xlsx". These files can be edited in Microsoft Excel, for example.

You can exchange the file with the translators and import it back to the project as soon as it has been translated.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor, for example, German and English.

##### Exporting project texts

To export individual project texts, proceed as follows:

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The child elements are displayed.
2. Double-click on "Project texts". The "Project texts" editor will open.
3. Select the texts you want to export.
4. Click ![Exporting project texts](images/70981258635_DV_resource.Stream@PNG-de-DE.png). The "Export" dialog opens.

   ![Exporting project texts](images/135167224971_DV_resource.Stream@PNG-en-US.png)

   ![Exporting project texts](images/135167224971_DV_resource.Stream@PNG-en-US.png)
5. Select the required source language.
6. Select the required target languages.

   Select the "Select all" check box if you want to export all target languages.
7. Give the export file a name.
8. Set the path to the storage location of the export file.
9. Click "Export".

##### Result

The texts selected in the "Project texts" editor are written to an xlsx file. The xlsx file will be stored in the specified folder.

You can alternatively select and export all project texts from categories. Select "User texts" or "System texts" in the "Export" dialog in accordance with the type of texts you wish to export. In this case, export can additionally be limited by categories.

> **Note**
>
> Project texts in library objects cannot be exported.

## Using cross-references (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [General information about cross references (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#general-information-about-cross-references-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Special features when working with cross-reference lists in WinCC (Panels, Comfort Panels, RT Advanced, RT Professional)](#special-features-when-working-with-cross-reference-lists-in-wincc-panels-comfort-panels-rt-advanced-rt-professional)
- [Textual cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)](#textual-cross-references-panels-comfort-panels-rt-advanced-rt-professional)
- [Invalid cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)](#invalid-cross-references-panels-comfort-panels-rt-advanced-rt-professional)
- [Rewiring tags in the screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rewiring-tags-in-the-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### General information about cross references (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The cross-reference list provides an overview of the use of objects and devices within the project and project library. The cross-reference list can be used to show the relationships and the dependencies of objects among themselves.

#### Uses of cross-reference list

The cross-reference list offers you the following advantages:

- When creating and changing a program, you retain an overview of the devices, objects, tags, alarms, scripts, etc. that you have used.
- From the cross-references, you can jump directly to the object location of use.
- You can see whether the object uses other objects or is used by itself.
- You can learn the following when debugging:

  - Which objects are used in which screen and on which devices.
  - The alarms and recipes shown in a specific display.
  - The tags used in a specific alarm or object.
- As part of the project documentation, the cross-references provide a comprehensive overview of all object, alarms, recipes, tags and screens.

For additional information on working with cross-reference lists, please refer to "Displaying cross-reference lists".

---

**See also**

[HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)

### Special features when working with cross-reference lists in WinCC (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Working with cross-references in WinCC

In WinCC, there are a number of special features that you must take into account when working with cross-references.

For additional information on working with cross-reference lists, please refer to "Displaying cross-reference lists".

#### "Change cross-reference" dialog

You can change the references of tags in the properties of screen objects using the "Change object references" dialog.

#### Using textual cross-references when working with VB scripts

When working with VB scripts, you can reference tags directly with the help of textual cross-references without having to access the SmartTags list.

#### Adding a new object to the cross-reference list

The auto-complete function only offers HMI tags for selection. Array elements of an HMI tag are not displayed in auto-complete. You can only add array elements by entering the name of an array element.

#### Displaying cross-references in the Inspector window

If you select an object in the screen and an HMI tag is being used as the process tag at the object, the object and the linked HMI tag are displayed in the cross-references. All locations of use of the object and the HMI tags are also listed.

If the HMI tag is interconnected with a PLC tag or a DB tag, the locations of use of the interconnected PLC tag or DB tag are displayed.

#### Shortcut menu in the cross-reference list

The shortcut menu is object-oriented. The shortcut menu is available for each row when the "Object" column actually contains an object.

### Textual cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Textual cross-references are cross-references that are stored as pure text. You cannot navigate to a different object with the help of textual cross-references. Such cross-references are displayed in red in the cross-reference list.

Textual cross-references are created as follows:

- You create a textual cross-reference for a non-existent object manually by entering the object name under Property.
- The object used has already been deleted, and the connection to it is shown as textual cross-reference.

#### Basics

When references and subordinate objects of a source object are deleted, they are converted into textual cross-references. A textual cross-reference is not stored when the source object itself is deleted.

![Basics](images/83341054987_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Almost all objects, with the exception of data logs, support textual cross-references.

> **Note**
>
> Textual cross-references cannot be deleted.

You can also create a textual cross-reference manually to establish a connection to a non-existent object. This procedure can be helpful if you want to access tags directly in VB scripts without SmartTags.

> **Note**
>
> **Textual cross-references for tags in RT Professional**
>
> If no user data type (UDT) is assigned to a screen or the tags are referenced as user data type element with @NOP, @NOTP, @NOSP, textual cross-references appear for the tags.

#### Using textual cross-references when working with VB scripts

When working with VB scripts, you can reference tags directly with the help of textual cross-references without having to access the SmartTags list.

When you enter an object name, the script parser looks for the referenced object.

For example: `DIM x`

`x = MyObject`

A reference is made to any VB script or tag that already exists under this name. If a VB script and a tag exist under this name, the script parser establishes the reference to the VB script.

If neither a tag nor a VB script exists under this name, the system creates two textual cross-references: one for the tag and one for the VB script.

The first object that is created under this name (a tag or a VB script) is assigned one of the two textual cross-references. The textual cross-reference turns into an actual cross-reference. The second textual cross-reference is deleted.

> **Note**
>
> In RT Professional, only one textual cross-reference is created for the VB script, because direct addressing of tags is not possible in this context.

---

**See also**

[Invalid cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)](#invalid-cross-references-panels-comfort-panels-rt-advanced-rt-professional)

### Invalid cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

A cross-reference can become invalid as a result of certain changes to the configuration. Invalid cross-references are shown grayed out in the cross-reference list and in the Inspector window. A question mark is displayed beside the cross-reference text. Clicking on the question mark opens the online help.

Invalid cross-references do not have any negative implications for your project.

#### Basics

A cross-reference can become invalid for the following reasons:

- A change of device type
- Copying a cross-reference from another HMI device to an HMI device that does not support the object in question or object property.
- A change to an object property or the assignment of invalid values

The following objects can be invalid in the cross-reference list:

- Source and target object
- Subordinate objects and their higher-level objects
- Location of use

![Basics](images/86556384011_DV_resource.Stream@PNG-en-US.png)

If an object or location of use is invalid, you cannot navigate to that object or location of use. You cannot change the properties of an invalid location of use. For invalid objects, you can access the commands "Delete" and "Properties" over the shortcut menu. No other shortcut menu commands are available. No shortcut menu is available for invalid locations of use.

> **Note**
>
> **Textual cross-reference invalid**
>
> An object can be an invalid object and a textual cross-reference in the cross-reference list at the same time. In such a case, the invalid cross-reference is shown in red like a textual cross-reference.

#### Examples

**Source object invalid**

You have created a screen for a Comfort Panel and added a VB scripts reference to the function list. You change the device type from "SIMATIC Comfort Panel" to "SIMATIC Basic Panel". As VB scripts are not available for Basic Panels, the cross-reference for the VB script is invalid.

**Target object invalid**

For a Comfort Panel, you have created a screen that has a cross-reference to the audit trail log with the system function "ClearLog". You copy this screen to Runtime Professional. As the audit trail log is not available for Runtime Professional, the cross-reference is invalid.

**Property that links the source object to the target object is invalid**

In Runtime Professional, you have created an entry in the graphics list that has a cross-reference to the "Flashing" property. You copy this graphics list to a Comfort Panel. As this property is not available on Control Panels, the cross-reference from the graphics list to the "Flashing" propery is invalid.

**Property invalid if source object invalid**

For a Comfort Panel, you have saved a slide-in screen that has a cross-reference to a tag over an I/O field. You change the device type from "SIMATIC Comfort Panel" to "SIMATIC Basic Panel". As the slide-in screen is not available on Basic Panels, the cross-reference is invalid.

**Textual cross-reference invalid**

You have created a tag for a Comfort Panel and linked the VB function "SetTag" to that tag. You have also created a screen that is connected to the "SetTag" VB function over the "Established" event. You delete the VB function. A textual cross-reference is created for the deleted VB function. You change the device type from "SIMATIC Comfort Panel" to "SIMATIC Basic Panel". As VB scripts are not available for Basic Panels, the textual cross-reference for the VB script is invalid. The invalid cross-reference is shown in red.

---

**See also**

[Textual cross-references (Panels, Comfort Panels, RT Advanced, RT Professional)](#textual-cross-references-panels-comfort-panels-rt-advanced-rt-professional)

### Rewiring tags in the screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can change the references of tags in the properties of screen objects using the "Change object references" dialog.

This function lets you to replace a large number of tags in various screen objects. Replacing references is useful, for example, if you have created a screen by copying and pasting and need to adapt its references.

You search for and replace individual or multiple characters in the tag names.

You can open the "Change object references" dialog with the command in the shortcut menu. You can open the dialog for one or more screen objects or a screen.

The "Change object references" dialog is available for the following screens.

- Overview screen (permanent area)
- Templates
- Pop-up screens
- Slide-in screens
- Global screen

#### How to replace a tag

1. Select an object in the screen that contains a tag that you want to change.
2. Select the "Change object references" command in the shortcut menu or in the "Edit" menu.

   The "Change object references" dialog opens. You can see the selected screen objects and the tags used in the "Object" column.

   ![How to replace a tag](images/74921408907_DV_resource.Stream@PNG-en-US.png)

   ![How to replace a tag](images/74921408907_DV_resource.Stream@PNG-en-US.png)
3. Enter the name or part of the name you want to find in the "Find in reference" input box.
4. Start the search with the "Find next" button. If a reference is found, it is highlighted in the "Reference" column.

   Another click on the "Find next" button continues the search process until the list has been completely searched.

   After this, the search process starts again from the top of the list.
5. Enter the name or part of the name you want to replace for the found name in the "Replace with" input box.
6. Click the "Replace" button to replace the selected tag.

   All references found are replaced by clicking the "Replace all" button. In this way, you can replace a large number of references with another

   reference.
7. To select a tag from the list of all tags created in the project, click on the ![How to replace a tag](images/61213169547_DV_resource.Stream@PNG-de-DE.png) button in the "Replace" column.
8. To select a tag from the object list or to create a new tag, click on the ![How to replace a tag](images/61230163979_DV_resource.Stream@PNG-de-DE.png) button in the "Replace" column.
9. Confirm your entry with "OK".

The rewiring of the tags is applied in the project.

Alternatively, you can enter a tag to replace the existing tag directly in the "Replace" column. You are supported by the auto-complete function in this process.

> **Note**
>
> When you search for a tag in the "Replace" column, you are supported by the auto-completion. After entering the first letter of the tag name in the "Replace", the auto-completion list contains the tags whose names contain the letters. Depending on the context, the auto-completion list only contains the tags that are permitted for the intended purpose.

> **Note**
>
> The tags shown in the column are displayed as read-only if the reference object is read-only, for example, a tag in a screen that has been stored in the library.

> **Note**
>
> It is possible to manually create a tag that does not yet exist. You create this tag at a later time.

#### Additional options for searching

You can narrow down your search by enabling the following options:

- Use wildcards

  Enter * for any number of characters. Example: You want to search for all tags starting with "HMI". Enter "HMI*" in the search key box.

  Enter ? for an individual character.
- Find whole words

  To search only for full names, enable the "Find whole words" option.

#### Replacing arrays and user-defined tags

Tags with names containing the special characters . [ ] are shown in quotation marks.

Array type tags and tags of user-defined data types (UDT) contain special characters to separate tags from their elements. However, they are not shown in quotation marks. To replace an array or a UDT with an HMI tag with special characters, enter the name of the HMI tag in quotation marks in the "Replace" input box. If you type the name without quotation marks, a reference to a non-existent array or UDT is created instead of a reference to the desired HMI tag with special characters.

#### Correcting entries

If an incorrect entry is made in the "Replace with" input box, the existing references can be replaced by references to non-existent tags.

If you detect an incorrect entry before confirming with "OK", you can correct the error. To do this, select the "Replace" column and press the "Remove" button. Any incorrect entries in the "Reference" column are deleted.

If you confirm the dialog with "OK", the affected properties of the screen objects are marked in red. Non-existent tags are highlighted in red in the "Change cross references" dialog.

If the new tag does not yet exist, you must subsequently create the tag.

## Managing languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Language settings in the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#language-settings-in-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Operating system settings for Asian languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#operating-system-settings-for-asian-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting project languages
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-project-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating one project in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-one-project-in-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using language-specific graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-language-specific-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Languages in Runtime
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example of multilingual configuration
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-of-multilingual-configuration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### User interface language and project languages

A distinction is drawn between two different language levels in WinCC:

- User interface language

  During configuration, the text in the WinCC menus and dialogs is displayed in the user interface language. The user interface language also affects the labeling of operating elements, the parameters of the system functions, the online help, etc.
- Project languages

  Project languages are all languages in which a project will later be used. Project languages are used to create a project in multiple languages.

The two language levels are completely independent of one another. For example, you can create English projects at any time using a German user interface and vice versa.

#### Project languages

The following languages are differentiated within the project languages:

- Reference language

  The reference language is the language that you use to configure the project initially.

  During configuration, you select one of the project languages as the reference language. You use the reference language as a template for translations. All of the texts for the project are first created in the reference language and then translated. While you are translating the texts, you can have them displayed simultaneously in the reference language.
- Editing language

  You produce translations of the texts in the editing language.

  Once you have created your project in the reference language, you can translate the texts into the remaining project languages. Select a project language respectively as an edit language and edit the texts for the appropriate language variant. You can change the editing language at any time.

  > **Note**
  >
  > When switching the project languages, the assignment to the keys on the keyboard also changes. For some languages (for example, Spanish), the operating system does not allow you to switch to the corresponding keyboard assignment. In this case, the keyboard assignment is switched to English.
- Runtime languages

  Runtime languages are those project languages that are transferred to the HMI device. You decide which project languages to transfer to the HMI device depending on your project requirements.

  You must provide appropriate controls so that the operator can switch between languages in runtime.

---

**See also**

[Language settings in the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#language-settings-in-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Operating system settings for Asian languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#operating-system-settings-for-asian-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the user interface language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-user-interface-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
["Project graphics" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-graphics-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)
  
[Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Language settings in the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The configuration PC operating system settings influence WinCC language management in the following areas:

- Selection of project languages
- Regional format of dates, times, currency, and numbers
- Displaying ASCII characters

#### Project language selection

A language is not available as a project language unless it is installed in the operating system.

#### Regional format of dates, times, currency, and numbers

WinCC specifies a fixed date and time format in the Date - Time field for the selected project language and runtime language.

In order for dates, times, and numbers to be presented correctly in the selected editing language, this language must be set in the Regional Options in the Control Panel.

#### Displaying ASCII characters

With text output fields, the display of ASCII characters as of 128 depends on the set language and the operating system being used.

If the same special characters are to be displayed on different PCs, the PCs must use the same operating system and regional settings.

#### Missing fonts (panels)

The following fonts no longer belong to the standard installation pack in Windows 10 and are not pre-installed:

- MS PGothic (is used as standard for displaying Japanese characters)
- Gulim (is used as standard for displaying Korean characters)
- MingLiU (is used as standard for displaying traditional Chinese characters)

If a font is not installed, an error message is displayed in the engineering system. The error message appears in every TIA Portal session if you navigate to "Runtime settings &gt; Language and font" or open screen objects which use the missing font. The missing font is replaced with a suitable font by the TIA Portal.

Missing fonts cause problems during compilation and in Runtime.

For example, if you open an error-free V13 SP1 project that was created on a configuration PC with Windows 7 on a configuration PC of V14 SP1 with the Windows 10 operating system, error messages can be output during compilation because of the fonts that are not installed.

You can find more detailed information on fonts in Windows 10 at [https://support.microsoft.com/en-us/kb/3083806](https://support.microsoft.com/en-us/kb/3083806)

Solution:

1. Compile the project before you transfer it to your HMI device. This determines whether the fonts you require are missing.
2. Install these fonts and/or the corresponding Windows language pack.

Alternatively, you can also compile the projects with substitute fonts.

The missing font is saved in the configuration. As soon as this font is available again, it is displayed and used in the configuration.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Operating system settings for Asian languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#operating-system-settings-for-asian-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Operating system settings for Asian languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Settings on Western operating systems

If you want to enter Asian characters, you must activate the support for this language in the operating system.

The Input Method Editor (IME) is available in Windows for configuring Asian texts. Without this editor, you can display Asian text but not edit it. For more information on the Input Method Editor, refer to the documentation for Windows. To enter Asian characters when configuring, switch to the Asian entry method in the "Input Method Editor".

Switch the operating system to the appropriate language to have language-specific project texts, such as alarm texts, displayed in the simulator in Asian characters.

#### Settings on Asian operating systems

If you are configuring on an Asian operating system, you must switch to the English default input language to enter ASCII characters, for example, for object names. As the English default input language is included in the basic installation of the operating system, you do not need to install an additional input locale.

#### Enable language support

1. Open the system controller.
2. Select "Regional and Language Options".
3. On the "Languages" tab, activate the check box "Install files for East Asian languages".
4. Then click on "Details" under "Text Services and Input Languages". The dialog "Text Services and Input Languages" is opened.
5. On the "Settings" tab add the required default input language under the "Installed Services".
6. Select the language of the operating system in the "Language for non-Unicode programs" area in the "Advanced" tab.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Language settings in the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#language-settings-in-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Setting project languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Selecting the user interface language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-user-interface-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Enable project languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enable-project-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Selecting the reference language and editing language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-reference-language-and-editing-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Selecting the user interface language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The user interface language is used for displaying menu entries, title bars, infotexts, dialog texts and other designations in the WinCC user interface.

You can switch between the installed user interface languages during configuration. The labeling of the operating elements remains in the language you set when you added the object even if you change the user interface language.

##### Procedure

1. Select "Options &gt; Settings" in the menu.

   The "Settings" dialog box is opened.
2. Select the desired user interface language under "General &gt; General settings".

##### Result

WinCC will use the selected language as user interface language.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enable project languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enable-project-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the reference language and editing language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-reference-language-and-editing-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Enable project languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The project languages are set in the "Project languages" editor. You define which project language is to be the reference language and which the editing language.

##### Enable project languages

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The lower-level elements will be displayed.
2. Double-click on "Project languages".

   The possible project languages will be displayed in the working area.
3. Enable the relevant project languages.

**Note**

**Copying multilingual objects**

The copies of multilingual objects to a different project only include text objects in the project languages which are activated in the target project. Activate all project languages in the target project to include the corresponding text objects when transferring the copy.

##### Disabling project languages

| Symbol | Meaning |
| --- | --- |
| 1. Disable the languages which are not relevant for the project.       | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | If you disable a project language, all text and graphic objects you have already created in this language will be deleted from the current project. |  | |  |

---

**See also**

[Selecting the user interface language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-user-interface-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the reference language and editing language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-reference-language-and-editing-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Selecting the reference language and editing language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The project languages are set in the "Project languages" editor. You define which project language is to be the reference language and which the editing language. You can change the editing language at any time.

##### Requirements

The "Project languages" editor is open.

Several project languages have been activated.

##### Selecting the reference language and editing language

1. Click the arrow in the drop-down list in the "General &gt; Editing language" section.
2. Click on the required language in the drop-down list, for example, German.
3. Click on the arrow in the drop-down list in the "General &gt; Reference language" section.
4. Click on the required language in the drop-down list, for example, English.

The language selection is displayed in the list box.

![Selecting the reference language and editing language](images/111984061835_DV_resource.Stream@PNG-en-US.png)

##### Result

You have now selected the editing and reference languages.

If you change the editing language, all future text input will be stored in the new editing language.

---

**See also**

[Selecting the user interface language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-user-interface-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enable project languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enable-project-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Creating one project in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-using-reference-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Multilingual configuration in WinCC

You can configure your projects in multiple languages using WinCC. There are various reasons for creating a project in multiple languages:

- You would like to use a project in more than one country.

  You create the project in multiple languages but when the HMI device is commissioned, only the language spoken by the operators at the respective site will be transferred to the HMI device.
- The operators of a system speak a range of different languages.

  Example: An HMI device is used in China, but the service personnel understand only English.

##### Translating project texts

With WinCC, you can enter project texts directly in several languages in various different editors, for example, in the "Project texts" editor. WinCC also allows you to export and import your configuration for translation purposes. This is particularly advantageous if you configure projects containing a large amount of text and want to have it translated.

##### Language management and translation in WinCC

The following editors are used to manage languages and translate texts in WinCC:

| Editor | Short description |
| --- | --- |
| Project languages | Selection of project languages, editing language and reference language. |
| Languages and fonts | Management of runtime languages and fonts used on the HMI device. |
| Project texts | Central management of configured texts in all project languages. |
| Graphics | Graphic library for managing graphics and their language-specific versions. |

---

**See also**

[Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-using-reference-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Texts in different languages in the project

Texts that are output on display devices during processing are typically entered in the language in which the automation solution is programmed. Comments and the names of objects are also entered in this language.

If operators do not understand this language, they require a translation of all operator-relevant texts into a language they understand. You can therefore translate all the texts into any language. In this way, you can ensure that anyone who is subsequently confronted with the texts in the project sees the texts in his/her language of choice.

##### User texts and system texts

In the interests of clarity, a distinction is drawn between user texts and system texts:

- User texts are texts created by the user.
- System texts are texts created automatically and which are a product of configuration in the project.

The project texts are managed in the project text editor. This can be found in the project tree under "Languages &amp; Resources &gt; Project texts".

##### Examples of multilingual project texts

You can, for example, manage the following types of text in more than one language:

- Display texts
- Alarm texts
- Comments in tables
- Labels of screen objects
- Text lists

##### Translating texts

There are two ways of translating texts.

- Translating texts directly

  You can enter the translations for the individual project languages directly in the "Project texts" editor.
- Translating texts using reference texts

  You can change the editing language for shorter texts. You can enter the new texts in the editing language while the texts of the reference language are displayed.

---

**See also**

[Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-using-reference-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Translating texts

If you use several languages in your project, you can translate individual texts directly. As soon as you change the language of the software user interface, the translated texts are available in the selected language.

##### Requirements

- You are in the project view.
- A project is open.
- You have selected at least two further project languages.

##### Procedure

Proceed as follows to translate individual texts:

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The elements below this are displayed.
2. Double-click on "Project texts".

   A list with the texts in the project is displayed in the work area. There is a separate column for each project language.

   ![Procedure](images/70639090955_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70639090955_DV_resource.Stream@PNG-en-US.png)
3. To group identical texts and translate them simultaneously, click on the "![Procedure](images/22300349963_DV_resource.Stream@PNG-de-DE.png)" button in the toolbar.
4. To hide texts that do not have a translation, click on the ![Procedure](images/22301968011_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
5. Click on an empty column and enter the translation.

##### Result

You have translated individual texts in the "Project texts" editor. The texts will then be displayed in the runtime language.

---

**See also**

[Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

After changing the editing language, all texts are shown in input boxes in the new editing language. If there is not yet a translation available for this language, the input boxes are empty or filled with default values.

If you enter text again in an input field, this is saved in the current editing language. Following this, the texts exist in two project languages for this input field, in the previous editing language and in the current editing language. This makes it possible to create texts in several project languages.

You can display existing translations for an input box in other project languages. These serve as a comparison for text input in the current editing language and they are known as the reference language.

##### Requirement

There is at least one translation into a different project language for an input field.

##### Procedure

To display the translation of an input cell in a reference language, follow these steps:

1. Select "Tasks &gt; Languages &amp; resources" in the task card.
2. Select a reference language from the "Reference language" drop-down list.

##### Result

The reference language is preset. If you click in a text block, translations that already exist in other project languages are shown in the "Tasks &gt; Reference text" task card.

---

**See also**

[Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Project texts are exported for translation. Texts are exported to Office Open XML files ending in ".xlsx". These files can be edited in Microsoft Excel, for example.

You can exchange the file with the translators and import it back to the project as soon as it has been translated.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor, for example, German and English.

##### Exporting project texts

To export individual project texts, proceed as follows:

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The child elements are displayed.
2. Double-click on "Project texts". The "Project texts" editor will open.
3. Select the texts you want to export.
4. Click ![Exporting project texts](images/70981258635_DV_resource.Stream@PNG-de-DE.png). The "Export" dialog opens.

   ![Exporting project texts](images/135167224971_DV_resource.Stream@PNG-en-US.png)

   ![Exporting project texts](images/135167224971_DV_resource.Stream@PNG-en-US.png)
5. Select the required source language.
6. Select the required target languages.

   Select the "Select all" check box if you want to export all target languages.
7. Give the export file a name.
8. Set the path to the storage location of the export file.
9. Click "Export".

##### Result

The texts selected in the "Project texts" editor are written to an xlsx file. The xlsx file will be stored in the specified folder.

You can alternatively select and export all project texts from categories. Select "User texts" or "System texts" in the "Export" dialog in accordance with the type of texts you wish to export. In this case, export can additionally be limited by categories.

> **Note**
>
> Project texts in library objects cannot be exported.

---

**See also**

[Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-using-reference-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Importing project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Edit the xlsx file or send it to a translator. Import the texts once they have been translated. The foreign languages will be imported to the relevant object in the project.

> **Note**
>
> In WinCC, you only import the previously exported project texts into the same project. Importing into a different project is not supported.

> **Note**
>
> Once a project has been saved under a new name with "Save as …", the import of texts is no longer possible.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor, e.g. Italian and French.

##### Importing project texts

To import a file with project texts, proceed as follows:

1. Click on the arrow to the left of "Languages &amp; resources" in the project tree.

   The lower-level elements will be displayed.
2. Double-click on "Project texts". The "Project texts" editor will open.
3. Click the ![Importing project texts](images/24534696459_DV_resource.Stream@PNG-de-DE.png) button. The "Import" dialog box opens.
4. Select the path and file name of the import file from the "Import file" field.
5. Activate the "Import source language" check box if you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes.
6. Click on "Import".

##### Result

You have imported the project texts.

---

**See also**

[Working with multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Project text basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-text-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts directly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts using reference texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-using-reference-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Exporting project texts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-project-texts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### Using language-specific graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- ["Project graphics" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-graphics-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Storing an image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### "Project graphics" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You use the "Project Graphics" editor to manage the configured graphic objects in different language versions. Multilingual projects sometimes also require language-specific versions of the graphics, for example, if

- the graphics contain text;
- cultural aspects play a role in the graphics.

##### Opening the "Project graphics" editor

Double-click in the project tree on "Languages and resources &gt; Project graphics".

##### Work area

The work area displays all configured graphic objects in a table. There is a separate column in the table for each project language. Each column in the table contains the versions of the graphics for one particular language.

In addition, you can specify a default graphic for each graphic to be displayed whenever a language-specific graphic for a project language does not exist.

##### Preview

The preview shows you how the graphics will look on various devices.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Storing an image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Storing an image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You use the "Graphics" editor to import graphics you want to use in screens in the "Screens" editor. It also allows you to manage language-specific versions of graphics. A preview shows the graphic displays on various HMI devices.

> **Note**
>
> **File names for language-dependent graphics**
>
> Case is relevant in the file names of language-dependent graphics. Make sure that the format is consistent for all languages.

##### Requirement

- The language-dependent versions of a graphic are available.
- Multiple languages have been enabled in the "Project languages" editor.
- The "Graphics" editor is open.

##### Inserting graphics

1. Click "Add" in the "Graphics library" table. A dialog opens.
2. Select the required graphic file.
3. Click "Open" in the dialog box.

   The graphic will be imported to the project and displayed in all cells in this row in the "Graphics" editor.
4. Click in the corresponding cell of a language for which a language-dependent version of this graphic exists.
5. Select "Add graphic" from the shortcut menu. A dialog box opens.
6. Select the desired graphic file and click "Open."

   The language-dependent version is inserted in the table in place of the reference language graphic.
7. Then, in the "Default graphic" column, import a graphic to be displayed in runtime for those languages for which there is no language-specific graphic.

You can also drag&amp;drop a graphic from Windows Explorer to the relevant position in the "Graphics library" table.

##### Displaying graphics in the HMI device preview

1. Click on a graphic in the table.
2. Select the required HMI device under "Properties &gt; Graphics settings &gt; Device preview" in the Inspector window.

   The graphic will then be displayed as it will appear in runtime on the selected HMI device.

##### Result

The graphics added are available in the "Graphics" editor. The graphic assigned to the respective editing language will be displayed during editing. The default screen will be displayed in all editing languages for which no screen has been imported.

To display the language-dependent graphics correctly in runtime, a C script must be triggered.

The default screen is displayed in all runtime languages for which a screen has not been imported.

> **Note**
>
> If you disable a project language, all of the graphic objects you have already created in this language will be deleted from the current project.

---

**See also**

["Project graphics" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-graphics-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To display graphics that have been created in an external graphics program in your screens, you will first have to store these graphics in the graphics browser of the WinCC project.

##### Requirement

- Multiple languages have been enabled in the "Project languages" editor.
- The "Graphics" editor is open.
- There is a graphic in the "Graphics" editor.

##### Creating and adding a new graphic as an OLE object

1. Click "Add" in the "Graphics library" table. A dialog box opens.
2. Navigate to the folder in which the graphic is stored.
3. Click "Open" in the dialog box.

   The graphic will be imported to the project and displayed in all cells in this row in the "Graphics" editor.
4. Click in the corresponding cell of a language for which a language-dependent version of this graphic exists.
5. Select "Insert object" from the shortcut menu. The "Insert object" dialog box opens.
6. Select "Insert object &gt; Create new" and an object type in the dialog.
7. Click "OK." The associated graphic program is opened.
8. Close the graphics program once you have created the graphic.

   The graphic will be stored in the graphic programming software standard format and added to the graphic browser.

**Note**

In addition, the dialog "External application running..." will open. The dialog will not close until you exit the external application.

##### Inserting created graphics in WinCC

1. Click in the corresponding cell of a language for which a language-dependent version of this graphic exists.
2. Select "Insert object" from the shortcut menu. The "Insert object" dialog box opens.
3. From the "Insert object" dialog box, select "Create from file."
4. Click the "Browse" button.
5. Navigate to the created graphic and select it.

**Note**

In addition, the dialog "External application running..." will open. The dialog will not close until you exit the external application.

**Note**

To import graphics files, note the following size restrictions:

*.bmp, *.tif, *.emf, *.wmf ≤4 MB

*.jpg, *.jpeg, *.ico, *.gif "*≤1 MB

##### Result

The OLE objects added are available in the "Graphics" editor.

Versions of the graphics for the current editing language are displayed in the "Screens" editor. The default graphic is displayed in all editing languages for which no screen has been imported.

The graphic is displayed in runtime in the set runtime language. The default graphic is displayed in all runtime languages for which no graphic has been imported.

You can double-click OLE objects in your library to open them for editing in the corresponding graphic editor.

---

**See also**

["Project graphics" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#project-graphics-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Languages in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enabling-the-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-default-font-for-a-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Standardizing font for all languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#standardizing-font-for-all-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Specific features of Asian and Eastern languages in Runtime (Panels, Comfort Panels, RT Advanced)](#specific-features-of-asian-and-eastern-languages-in-runtime-panels-comfort-panels-rt-advanced)

#### Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Using multiple Runtime languages

You can decide which project languages are to be used in Runtime on a particular HMI device. The number of Runtime languages that are available at one time on the HMI device depends on the device. To enable the operator to switch between languages in Runtime, you need to configure a corresponding operator control.

When Runtime starts, the project is displayed according to the most recent language setting. When Runtime starts the first time, the language with the lowest number in the "Order for language setting" is displayed.

##### "Language &amp; font" Runtime setting

Configure the following under "Language &amp; font":

- The project languages available as Runtime languages for the respective HMI device.
- The order in which the languages are switched.
- Default font for a Runtime language

The license status of the fonts is also shown in the "Download font" area. If a specific license is required for a protected font, this is indicated in the "License status" column.

> **Note**
>
> **Post installing fonts**
>
> When a configured font on the configuration computer is missing, the project is not compiled. Re-installation is required.
>
> After installing a font, restart the TIA Portal and completely re-compile your project. Only then can the HMI device be compiled without errors.

> **Note**
>
> **Runtime language in controls (RT Professional)**
>
> If you have configured a control in a specific Runtime language that is not a user-interface language, it can happen that some texts, for example, system texts in the status bar, appear in the English language.

> **Note**
>
> **Specify Runtime languages as input languages**
>
> To enter and edit data in Runtime, configure the specified Runtime languages also as input languages for the keyboard of your PC.

##### Use of multilingual graphics (RT Professional)

Graphics are stored in the runtime project in the language that you specified in the Runtime settings under "Language &amp; font &gt; Language selection &gt; Runtime language for non-multilingual objects".

The use of different graphics for individual runtime languages has no effect when switching languages in runtime.

Solution: Configure individual graphic displays with the desired graphic in the set runtime language for non-multilingual objects and switch these to visible or invisible according to the runtime language in the script.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enabling-the-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-default-font-for-a-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You need to configure language switching if you want to have multiple runtime languages available on the HMI device. This is necessary to enable the operator to switch between the various Runtime languages.

##### Methods for language switching

You can configure the following methods for language switching:

- Direct language selection

  Each language is set by means of a separate button. In this case, you create a button for each Runtime language.
- Language switching

  The operator switches the languages using a button.

Regardless of the method used, the button names must be translated into each of the languages used. You can also configure an output field that displays the current language setting.

---

**See also**

[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enabling-the-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-default-font-for-a-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The "Language &amp; Font" editor shows all project languages available in the project. Here you select which project languages are to be available as runtime languages on the HMI device.

##### Requirements

Multiple languages have been selected in the "Project languages" editor.

##### Procedure

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language &amp; Font".
3. Select the following languages:

   - English
   - French
   - Italian

     ![Procedure](images/111984923147_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/111984923147_DV_resource.Stream@PNG-en-US.png)

##### Result

You have now set three runtime languages. A number is automatically assigned to each language in the "Order" column. The enabled runtime languages are transferred with the compiled project to the HMI device.

If the number of languages selected exceeds the number that can be transferred to the HMI device, the table background changes color.

> **Note**
>
> **Languages in Runtime (Comfort Panels)**
>
> If the language set under "Region and Language" is not supported in Runtime on the HMI, all dialogs are displayed in the default language "English".

---

**See also**

[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You specify the language order for Runtime language switching. The first time Runtime starts, the project is displayed in the language with the lowest number in the "Order" column.

##### Requirements

- Multiple languages have been enabled in the "Project languages" editor.
- The "Language &amp; Font" editor is open and three Runtime languages have been set in the following order:

  1. English

  2. Italian

  3. French

##### Procedure

1. Select the runtime language "English".
2. Click the ![Procedure](images/70640328331_DV_resource.Stream@PNG-de-DE.png) button. The runtime language "English" is moved down a place. The number will automatically be changed to "1" in the "Order" column.

   ![Procedure](images/68285359755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/68285359755_DV_resource.Stream@PNG-en-US.png)

##### Result

You have changed the order of Runtime languages. The first time runtime starts, the project will be displayed in the language with the lowest number. If the language is switched, this will happen in numerical order.

---

**See also**

[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enabling-the-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-default-font-for-a-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can specify the font used to display the texts for each runtime language on the HMI device in the "Language &amp; Font" editor. The default font is used in all texts, such as dialog texts, for which you cannot define a specific font.

WinCC offers only fonts supported by the HMI device.

> **Note**
>
> **"Bold" and "Italic" fonts**
>
> "Bold" and "italic" fonts are not supported on all HMI devices in Runtime.

##### Requirements

- Multiple languages have been enabled in the "Project languages" editor.
- Three runtime languages have been enabled in the "Language &amp; Font" editor.

  1. Chinese

  2. German

  3. French

##### Procedure

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language &amp; Font". The table shows the runtime languages and fonts set.
3. Click in the "French" row in the "Default font" column.
4. Select the font to be used by default if a font cannot be selected for a given text.

##### Result

The project texts for the runtime language "French" are displayed on the HMI device in the selected font.

These fonts are transferred to the HMI device during a transfer operation.

The default font is also used for the representation of dialogs in the operating system of the HMI device. Select a smaller font as default if the full length of the dialog texts or headers is not displayed.

---

**See also**

[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-the-log-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Standardizing font for all languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can standardize the font for all project languages during configuration with the "Use same font for all languages" option.

##### Requirement

- Multiple languages have been selected in the "Project languages" editor.
- Multiple languages have been selected in the "Language &amp; font" editor.
- The same font is defined for the selected runtime languages under "Configured font".

##### Procedure

1. In the "Options &gt; Settings &gt; Visualization &gt; General" menu, select the "Use same font for all languages" option.

   ![Procedure](images/70031488139_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70031488139_DV_resource.Stream@PNG-en-US.png)

##### Result

You have enabled the option "Use same font for all languages". If you change the font of an object in one language during configuration, this font will be applied to all active languages.

#### Selecting the log language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the "Runtime settings &gt; General" editor, select the language to be used for writing to logs in runtime.

##### Requirements

- The languages used in your project are activated in the "Project languages" editor, for example "German" and "English" .

##### Procedure

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language &amp; Font".
3. Activate the runtime languages, for example, "German" and "English".
4. Specify the "order":

   - 1 German
   - 2 English
5. Click on "Runtime settings &gt; General".
6. Select "German" for "Logs &gt; Log language".

##### Result

After loading, the project will start in the runtime language "German". The logs are now written in German. During runtime, the operator switches the runtime language to English. The logs will still to be written in German.

---

**See also**

[Languages and fonts in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-and-fonts-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Methods for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#methods-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Enabling the runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#enabling-the-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the runtime language order for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-runtime-language-order-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the default font for a runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-default-font-for-a-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Specific features of Asian and Eastern languages in Runtime (Panels, Comfort Panels, RT Advanced)

##### Introduction

Note the following special considerations for the operation in Runtime of projects for Asian languages.

> **Note**
>
> During configuration, only use the Asian fonts that your configuration computer supports.

##### Memory requirement for Asian character sets

The memory requirement is greater when using Asian languages. Therefore look out for corresponding error messages when compiling the project.

##### Font size for Asian character sets

Use at least a font size of 10 points to display the text of projects created for Asian languages in Runtime. Asian characters will become illegible if smaller font sizes are used. This also applies to the default font in the Runtime settings under "Language &amp; font".

##### Text field length for Asian languages

Make allowances for an appropriate length of the text fields when working on multilingual projects with Asian languages. Field contents may be partially hidden, depending on the font and the font size.

1. Open the "Properties &gt; Appearance" text box in the Inspector window.
2. Under "Fit to size", disable the "Auto-size" option.
3. Verify the proper display in Runtime.

### Example of multilingual configuration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring a button in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-in-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring a button for language switching for each runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-for-each-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example, you configure a button that can be used to toggle between multiple runtime languages during runtime.

##### Requirements

- You have completed the "Configuring a button in multiple languages" example.
- The "Screen_1" screen is open.
- The button on the screen has been selected.

##### Procedure

1. In the Inspector window, select "Properties &gt; Events &gt; Press".
2. Click on "Add function" in the table.
3. Select the "SetLanguage" system function and the "Switch" setting.

##### Result

You have assigned the button the function "SetLanguage". Pressing the button during runtime will switch the runtime language. The runtime languages are switched in the order specified by the number sequence in the "Languages and fonts" editor.

---

**See also**

[Languages in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#languages-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-in-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button for language switching for each runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-for-each-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a button in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example, you configure a "Sprache umschalten" button in German and "Switch language" button in English.

##### Requirements

- The languages "German" and "English" have been enabled in the "Project languages" editor.
- German has been set as editing and reference language.
- You have created and opened the "Screen_1" screen.
- The Inspector window is open.

##### Procedure

1. Drag-and-drop a button from the "Tools" task card into the screen.

   The button will be added to the screen.
2. In the Inspector window, open "Properties &gt; Properties &gt; General".
3. Enter the text ""Sprache umschalten" under "Text &gt; off".
4. Press &lt;Enter&gt; to confirm. The button is named.
5. Open the "Tasks" task card.
6. Select "English" under "Languages &amp; Resources &gt; Editing language".
7. Enter the label "Switch Language" under "Properties &gt; Properties &gt; General &gt; Text &gt; Off" in the Inspector window.

##### Result

The button name is configured in German and English language. The button name corresponding with the current Runtime language is shown in Runtime.

---

**See also**

[Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button for language switching for each runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-for-each-runtime-language-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a button for language switching for each runtime language (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example, you configure a "Sprache umschalten" button in German and "Switch language" button in English.

##### Requirements

- The following languages have been enabled in the "Project languages" editor

  - German
  - English
  - Italian
- All languages have been set as runtime languages in the "Runtime settings &gt; Language &amp; Font" editor.
- You have created and opened the "Screen_1" screen.
- Three buttons have been created on the screen:

  - Button_1 labelled "Deutsch"
  - Button_2 labelled "English"
  - Button_3 labelled "Italiano"
- The Inspector window is open.

##### Procedure

1. Select "Button_1".
2. In the Inspector window, select "Properties &gt; Events &gt; Press".
3. Click on &lt;Add function&gt; in the table.
4. Select the "SetLanguage" system function.
5. Click on the "Switch" field.
6. Click on the ![Procedure](images/22300229003_DV_resource.Stream@PNG-de-DE.png)button.
7. Select "Runtime language". The field will be highlighted in red.
8. Select "German" from the drop-down list.
9. Repeat steps 1 - 8 for the other two buttons and select the corresponding runtime language.

##### Result

You have configured three buttons for switching language in runtime. Each button will switch to a different runtime language. For example, clicking on the "English" button during runtime will switch the runtime language to English.

---

**See also**

[Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button in multiple languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-in-multiple-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Replacing devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Customizing the configuration of connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#customizing-the-configuration-of-connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-specific-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Adjusting screens to the new device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adjusting-screens-to-the-new-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Replacing devices
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-replacing-devices-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can use existing configurations for new devices and optimize these configurations with little manual effort.

All data configured by you is retained in the configuration data. This means you do not need to copy individual objects of one device and paste them to another.

#### Principle

The following applies when you replace devices:

- Only functions supported by the new device are available. Only configuration data supported by the new device are displayed.

  This affects

  - recipes,
  - objects available on the screens,
  - available system functions,
  - available communication logs, etc.
- The number of supported objects, such as screens or tags, may be limited on the new device. If the existing objects exceed the limitations on the new device, the objects are displayed in full. The objects are, however, highlighted in color in the individual editors. An error is generated when the project data is compiled.

  Manual post processing is required when switching to a device with fewer features.

  Example: Limited number of connections

  All connections will be highlighted in color as invalid if fewer connections are supported on the new device than have been configured. Delete any excess connections.
- After an HMI device has been replaced, you should check the appearance of the configured screens. Changing the size of the display may result in changes to the position and appearance of screen objects, e.g. the recipe view and alarm view.

> **Note**
>
> If you replace a Panel and select a PC Station as your new device, for example, WinCC Runtime Advanced will automatically be moved below the PC Station in the project tree.

> **Note**
>
> **Controller alarms after a Basic Panel device replacement**
>
> For the controller alarms (PLC monitoring alarms, program alarms or system alarms) to be displayed after a device replacement ("Device view &gt; Change device") from a Basic Panel to a Comfort Panel, Mobile Panel or WinCC RT Advanced, you need to activate the "Display classes" setting for the respective connections under "Runtime settings &gt; Alarms &gt; Controller alarms".

---

**See also**

[Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced)](#device-specific-functions-basic-panels-panels-comfort-panels-rt-advanced)
  
[HMI device wizard basics (Basic Panels, Panels, Comfort Panels)](#hmi-device-wizard-basics-basic-panels-panels-comfort-panels)
  
[Basic Panel (Basic Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-panel-basic-panels)
  
[Mobile Panel (Panels, Comfort Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#mobile-panel-panels-comfort-panels)
  
[Comfort Panel (Panels, Comfort Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#comfort-panel-panels-comfort-panels)
  
[WinCC Runtime Advanced (RT Advanced)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#wincc-runtime-advanced-rt-advanced)
  
[Customizing the configuration of connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#customizing-the-configuration-of-connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Replacing devices (Panels, Comfort Panels, RT Advanced)](#example-replacing-devices-panels-comfort-panels-rt-advanced)

### Customizing the configuration of connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

If an HMI device is replaced, error messages of the type "... are not supported in the new configuration and will therefore be removed" may be generated. These alarms refer to configured connections of the device and are triggered, for example, if the HMI devices have a different number of interfaces. These connections are marked red after a device replacement. If you would like to continue to use these connections, you have to change the configuration of the connection.

#### Procedure

1. Open the "Devices and Networks" editor.
2. Click "Network" in the toolbar of the network view.
3. Network the interface of the HMI device with the interface of the CPU.
4. Click in the table area of the network view on the "Connections" table.
5. Select the connection marked red.
6. Enter the new interface under "Properties &gt; General &gt; Interface" in the Inspector window.

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced)](#device-specific-functions-basic-panels-panels-comfort-panels-rt-advanced)
- [Key assignment when replacing devices (Basic Panels)](#key-assignment-when-replacing-devices-basic-panels)

#### Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Functions dependent on the device

Functions dependent on the device are implemented as follows:

- Colors

  The color is changed automatically when you switch from a device with full color display to one with a smaller color range.

  If you change the color manually and then change back again to a device with a larger range of colors, the reduced range of colors will be retained.
- Fonts

  Any configured font not available on a device will be replaced by a similar one or by the configured default font. The default font depends on the device selected.
- Font size

  Use small Windows fonts to display the text on devices. If you use large Windows fonts, then, depending on the size of the display, the text will not be displayed in full.

  The character scope is much greater for Asian languages. The use of different font sizes therefore has serious implications on the memory requirements of all devices.

  Use the same font type for all large characters throughout the project to ensure effective and efficient configuration.
- Screens and screen objects

  If the new device supports a different resolution than the previous device when you replace a device, there are several ways to adjust the screens.

  Adjust the size of the screens to the new device in the menu under "Options &gt; Settings &gt; Visualization &gt; Fit to size screen".

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Screen adjustment options (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-adjustment-options-basic-panels-panels-comfort-panels-rt-advanced)

#### Key assignment when replacing devices (Basic Panels)

##### Introduction

The devices available each have different function keys. The functions configured for these keys will be mapped to the available function keys of the new device if the device is replaced.

##### Function key mapping

The function keys below the display are mapped from left to right to the new device. If the new device has fewer keys, the keys it does not have are not mapped.

> **Note**
>
> **HMI devices without LED keys**
>
> If you replace a device with configured LED keys with a device without LED keys in the Engineering System, runtime will not start after the project data have been transferred to the device.
>
> Delete the LED key configuration before you replace the device.

##### Example: Replacing a KTP1000 Basic with a KTP600 Basic

You have configured a function for F2 in KTP1000 Basic. This function is triggered by F2 following replacement with a KTP600 Basic.

If you have used F7 in a KTP1000 Basic, this function will no longer be available if the panel is replaced with a KTP600 Basic.

![Example: Replacing a KTP1000 Basic with a KTP600 Basic](images/26427350027_DV_resource.Stream@PNG-de-DE.png)

##### Mapping of control keys and cursor keys

The following keys are mapped only to the same keys of the new device:

- HELP
- ESC
- ACK
- ENTER
- PAGE UP
- PAGE DOWN
- CURSOR UP
- CURSOR DOWN

---

**See also**

[Device-specific functions (Basic Panels, Panels, Comfort Panels, RT Advanced)](#device-specific-functions-basic-panels-panels-comfort-panels-rt-advanced)

### Adjusting screens to the new device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Screen adjustment options (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-adjustment-options-basic-panels-panels-comfort-panels-rt-advanced)
- [Fit objects to contents (Basic Panels, Panels, Comfort Panels, RT Advanced)](#fit-objects-to-contents-basic-panels-panels-comfort-panels-rt-advanced)
- [Specifying the position of screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](#specifying-the-position-of-screen-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### Screen adjustment options (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Select fit to size for screens before you replace a device. Fit to size is particularly important when switching devices with different display resolutions.

Object adjustment to content can be prevented for objects such as graphic views or text fields.

> **Note**
>
> The objects are distorted if you replace a device with a landscape format display with a device with a portrait format display. The difference in display format can, for example, result in object labels being cut off and content not being fitted to the object. You must therefore adjust the screens to the new device once you have replaced devices.

##### Screen adjustment when replacing devices

Adjust the size of the screens to the new device in the menu under "Tools &gt; Settings &gt; Visualization &gt; Resize screen".

![Screen adjustment when replacing devices](images/58776494987_DV_resource.Stream@PNG-en-US.png)

Select one of the following settings.

##### None (default setting)

The screens are not scaled. The objects in the screen retain their position and size. Use this setting as first test for checking of a possible exchange result because there are no rounding losses during forth and back exchange.

This option may result in objects being outside the configurable area if the display of the new device is smaller than the old one.

##### Fit to screen

The position and object size are adjusted to the new display size. Resizing takes place along the x-axis and the y-axis. Graphics and font size are adjusted accordingly.

##### Fit to height

The aspect ratio is maintained and the screens are adjusted to the height of the new device.

Use this option when you are replacing a device with display format 4:3, for example, with a device with widescreen.

##### Fit to width

The aspect ratio is maintained and the screens are adjusted to the width of the new device.

Use this option when you are replacing a device with widescreen, for example, with a device with display format 4:3.

##### Free scale factor

You select a free scale factor for screen adjustment. You can specify a factor for the x-axis and the y-axis.

Using a free scale factor of &lt; 1 may distort the objects. Object labels may, for example, be cut off and the content may not be fitted to the object.

You must therefore adjust the screens to the new device once you have replaced devices.

> **Note**
>
> The aspect ratio is not adjusted for objects with a fixed aspect ratio, for example, gauge, circle. The objects are displayed on the new device with the same aspect ratio as prior to the replacement of the device.

---

**See also**

[Specifying the position of screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](#specifying-the-position-of-screen-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### Fit objects to contents (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For some objects, you can specify fit to respective content in the Inspector window, for example:

- Text field: fit to text content
- I/O field: fit to text content
- Symbolic I/O field: fit to text content or to text list
- Graphic view: fit to included graphic

##### Fit to size for text and graphic objects

Disable automatic fit to size of the individual objects in the menu under "Options &gt; Settings &gt; Visualization &gt; Resize screen and screen objects &gt; Fit to content". This results in scaling of the objects as specified under "Options &gt; Settings &gt; Visualization &gt; Resize screen and screen objects".

Select the objects which are not automatically fitted to size.

![Fit to size for text and graphic objects](images/25893491595_DV_resource.Stream@PNG-en-US.png)

- If "Disable 'fit to size' for text objects" is activated, automatic fit to size is ignored in the text object properties.

  If you have activated "Fit screen to window height", the text field along with the other objects is scaled in accordance with the height of the new device.
- If "Disable 'fit to size' for graphic objects" is activated, automatic fit to size is ignored in the graphic object properties.

  If you have activated "Fit screen to window width", the graphics view along with the other objects is scaled in accordance with the width of the new device.

  > **Note**
  >
  > The settings have no effect on screen objects whose size cannot be changed, such as alarm indicators or screen objects with a fixed aspect ratio.

"Disable 'fit to size' for text objects" and "Disable 'fit to size' for graphic objects" have no effect if:

- You have activated "Resize screen and screen objects &gt; None".

- You have activated "Fit screen to window width and height" and the new device has the same resolution as the current device.

- You have activated "Fit screen to window height" and the new device has the same resolution as the current device.

- You have activated "Fit screen to window width" and the new device has the same resolution as the current device.

- You have selected "Resize screen and screen objects &gt; None" and position "Top left" which means an adaptation is not necessary.

##### Example

The figure below shows the effects of automatic sizing using a graphic object with two buttons aligned as an example:

![Example](images/29513122187_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Initial situation:   - Two buttons are aligned on a graphic object. - The option "Fit object size to graphic" or "Adjust object size to graphic" is activated in the object properties of the graphic object under "Display &gt; Sizing". |
| ② | Option 1: The original properties of the graphic object are to be maintained after switching the HMI device.  - Deactivate the option "Disable 'fit to size' for graphical objects" in the settings under "Size adaptation of objects".   Effect: The graphic object retains its original size after switching the HMI device. The alignment to the buttons is lost. |
| ③ | Option 2: The graphic object is to be placed relative to the new screen resolution after switching the HMI device.  - Activate the option "Disable 'fit to size' for graphical objects" in the settings under "Size adaptation of objects".   The option "Fit graphic to object size" is activated automatically in the object properties of the graphic object. The two buttons are properly aligned on the graphic object even after switching the HMI device. |

---

**See also**

[Specifying the position of screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](#specifying-the-position-of-screen-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### Specifying the position of screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

There are various ways to adjust the position of screen objects to the new device.

![Introduction](images/25893652619_DV_resource.Stream@PNG-de-DE.png)

##### Select position

Adjust the position of the screen objects to the new device in the menu under "Options &gt; Settings &gt; Visualization &gt; Fit to size screen &gt; Select position".

##### Example

The following option aligns the objects with the top left edge.

![Example](images/25893950091_DV_resource.Stream@PNG-de-DE.png)

The following object centers the objects in the middle of the screen.

![Example](images/25893957515_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Screen adjustment options (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-adjustment-options-basic-panels-panels-comfort-panels-rt-advanced)
  
[Fit objects to contents (Basic Panels, Panels, Comfort Panels, RT Advanced)](#fit-objects-to-contents-basic-panels-panels-comfort-panels-rt-advanced)

### Example: Replacing devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Example: Procedures overview (Panels, Comfort Panels, RT Advanced)](#example-procedures-overview-panels-comfort-panels-rt-advanced)
- [Example: Adjusting screens (Panels, Comfort Panels, RT Advanced)](#example-adjusting-screens-panels-comfort-panels-rt-advanced)
- [Example: Replacing devices (Panels, Comfort Panels, RT Advanced)](#example-replacing-devices-panels-comfort-panels-rt-advanced)

#### Example: Procedures overview (Panels, Comfort Panels, RT Advanced)

##### Introduction

The following example shows you how to replace a KTP700 Basic 7" PN with a TP1500 Comfort PRO.

##### Procedures overview

The procedure when replacing a device is as follows:

1. Adjust screens to the new device
2. Replacing devices

---

**See also**

[Example: Adjusting screens (Panels, Comfort Panels, RT Advanced)](#example-adjusting-screens-panels-comfort-panels-rt-advanced)
  
[Example: Replacing devices (Panels, Comfort Panels, RT Advanced)](#example-replacing-devices-panels-comfort-panels-rt-advanced)

#### Example: Adjusting screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

Adapt the screen before you replace a device. Screen adaptation is required as the display formats are different.

The KTP700 Basic format is 800 x 480 pixels while the format of the TP1500 Comfort PRO is 1366 x 768 pixels.

##### Requirements

- A project is open.
- The KTP700 Basic 7'' PN device is used in the project.

##### Adjusting screens

1. Open the "Options &gt; Settings" menu.
2. Click on "Visualization &gt; Resize screen".
3. Activate "Fit to height".

   ![Adjusting screens](images/58776494987_DV_resource.Stream@PNG-en-US.png)

   ![Adjusting screens](images/58776494987_DV_resource.Stream@PNG-en-US.png)
4. Select "Disable fit to size for text objects".
5. Select "Disable fit to size for graphical objects".

##### Result

You have carried out screen adjustment in preparation for replacing devices.

---

**See also**

[Example: Procedures overview (Panels, Comfort Panels, RT Advanced)](#example-procedures-overview-panels-comfort-panels-rt-advanced)
  
[Example: Replacing devices (Panels, Comfort Panels, RT Advanced)](#example-replacing-devices-panels-comfort-panels-rt-advanced)

#### Example: Replacing devices (Panels, Comfort Panels, RT Advanced)

##### Introduction

The following example shows you how to replace a device.

##### Requirements

- A project has been created and opened.
- The KTP700 Basic 7'' PN device is used in the project.

##### Procedure

1. Double-click on "Devices &amp; Networks" in the project navigation. The editor opens.
2. Click on the "KTP700 Basic PN" device.
3. Select "Change Device/Version" in the device shortcut menu. A dialog opens.
4. Select the TP1500 Comfort PRO device.
5. Select the matching image for the HMI device version that suits your configuration under "Version".

   When you change the image, the new image is automatically transferred to the target system with the next download. All runtime files are deleted during this step.

   Details of hardware differences can be found in the "Compatibility information".

   ![Procedure](images/111886759307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111886759307_DV_resource.Stream@PNG-en-US.png)
6. Click "OK". Device replacement is started.

##### Result

You have replaced the KTP700 BASIC device used in the project. You are now using the TP1500 Comfort PRO device.

---

**See also**

[Updating the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#updating-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Changing the runtime version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#changing-the-runtime-version-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Changing between device versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#changing-between-device-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Example: Procedures overview (Panels, Comfort Panels, RT Advanced)](#example-procedures-overview-panels-comfort-panels-rt-advanced)
  
[Example: Adjusting screens (Panels, Comfort Panels, RT Advanced)](#example-adjusting-screens-panels-comfort-panels-rt-advanced)

## Copying between devices and editors (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-2)
- [Copying and pasting
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-and-pasting-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying and pasting between Runtime Advanced and Panels and Runtime Professional
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-and-pasting-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying between different RT and ES versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-between-different-rt-and-es-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)
- [Copy and paste options (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copy-and-paste-options-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Unsupported objects and functionalities (Professional) (RT Professional)](#unsupported-objects-and-functionalities-professional-rt-professional)
- [Unsupported objects and functionalities (Panels, Comfort Panels, RT Advanced)](#unsupported-objects-and-functionalities-panels-comfort-panels-rt-advanced)

#### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Copying and pasting within an HMI device

You can copy and paste objects, such as display objects, within an HMI device. If the object is already created in the editor, when the object name is inserted a number is automatically attached, in accordance with the following principle:

- "&lt;Object_name&gt;_1" is renamed to "&lt;Object_name&gt;_2".
- "&lt;Object_name&gt;_2" is renamed to "&lt;Object_name&gt;_3".

##### Copying and pasting between HMI devices

You can also copy and paste between HMI devices. If an object with the same name already exists, you have the following options:

![Copying and pasting between HMI devices](images/73130371595_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Exception to this basic rule**
>
> Copying and pasting of an alarm class that has been generated from a common alarm class is handled differently than with this basic rule. When the copied alarm class already exists in the target HMI device within the same project, the "Paste" command is not performed.

##### Copying user-defined folders

You can create user-defined folders for editors, for example, for HMI tags, screens, etc.

You can copy user-defined folders and paste them into another HMI device. The objects contained in a user-defined folder may exceed the limitations applying to the other HMI device, such as the number of supported screens. After they have been pasted, all the objects are displayed. An error is displayed when the project data is compiled.

System folders cannot be copied.

---

**See also**

[Unsupported objects and functionalities (Panels, Comfort Panels, RT Advanced)](#unsupported-objects-and-functionalities-panels-comfort-panels-rt-advanced)
  
[Copying objects with linked objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-objects-with-linked-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Linked objects copied automatically (Basic Panels)](#linked-objects-copied-automatically-basic-panels)
  
[Copying screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

#### Copy and paste options (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Copy and paste options

Copy and pasting individual objects simplifies configuration.

WinCC offers a number of options for copying and pasting objects.

##### Shortcut menu

To copy and paste objects using the shortcut menu, proceed as follows:

1. Select an object, for example a button.
2. Select "Copy" in the shortcut menu.
3. Move the mouse cursor to the place on the screen where you want to paste the button.
4. Select "Paste" in the shortcut menu.

   The button will be pasted together with all properties already defined.

##### Drag&amp;drop

To drag-and-drop objects, proceed as follows:

1. Click on "Screens &gt; Start" in the project tree of a device.
2. Drag-and-drop the "Start" screen into the "Screens" folder of another device.
3. A dialog will appear if the second device already contains a screen with the same name.
4. Choose whether to replace or rename the existing screen.

#### Unsupported objects and functionalities (Professional) (RT Professional)

##### Introduction

When an object is copied, all its properties and settings are transferred to the target HMI device.

##### Unsupported objects

Objects that are not supported in the target HMI device cannot be pasted.

> **Note**
>
> When you copy a screen containing objects which are not supported by the destination HMI device, the objects remain in the background. When you copy the screen again and the new device supports the objects, they are displayed again.

##### Invalid objects

The following objects become invalid once they have been pasted into the target HMI device:

- Referenced objects that do not exist in the target HMI device.
- Objects with settings that are not supported in the target HMI device.
- System functions that were configured for objects and that are not supported in the target HMI device.

Invalid objects are highlighted by a color coding. Select a supported object or create a new one. If you retain an invalid object, an error will be displayed when the project data is compiled.

##### Colors and fonts

Colors and fonts are supported to varying degrees by HMI devices. When unsupported colors and fonts are pasted, they are replaced by supported colors and fonts. When you paste the same object back into the source HMI device, the original settings become active again.

#### Unsupported objects and functionalities (Panels, Comfort Panels, RT Advanced)

##### Introduction

When an object is copied, all its properties and settings are transferred to the target HMI device.

##### Unsupported objects

Objects that are not supported in the target HMI device cannot be pasted.

> **Note**
>
> When you copy a screen containing objects which are not supported by the destination HMI device, the objects remain in the background. When you copy the screen again and the new device supports the objects, they are displayed again.

##### Invalid objects

The following objects become invalid once they have been pasted into the target HMI device:

- Referenced objects that do not exist in the target HMI device.
- Objects with settings that are not supported in the target HMI device.
- System functions that were configured for objects and that are not supported in the target HMI device.

Invalid objects are highlighted by a color coding. Select a supported object or create a new one. If you retain an invalid object, an error will be displayed when the project data is compiled.

##### Colors and fonts

Colors and fonts are supported to varying degrees by HMI devices. When unsupported colors and fonts are pasted, they are replaced by supported colors and fonts. When you paste the same object back into the source HMI device, the original settings become active again.

##### Alarm classes

Only some of the enabled alarm classes are enabled.

When you configure an alarm window, for example, in the global screen in Project_1, you copy the alarm window and paste it to the global screen in Project_2.

Only some of the enabled alarm classes are enabled after pasting.

This behavior applies to the following display objects:

- Alarm window
- Alarm indicator
- Alarm view

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

### Copying and pasting (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Copying objects with linked objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-objects-with-linked-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Linked objects copied automatically (Basic Panels)](#linked-objects-copied-automatically-basic-panels)
- [Linked objects copied automatically (Panels, Comfort Panels, RT Advanced)](#linked-objects-copied-automatically-panels-comfort-panels-rt-advanced)
- [Copying HMI devices with HMI connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-hmi-devices-with-hmi-connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying linked screen objects with user data types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-linked-screen-objects-with-user-data-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Drag &amp; drop from the details view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#drag-drop-from-the-details-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying recipes within an HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-recipes-within-an-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Differences between Runtime Advanced and Panels and Runtime Professional (Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-panels-comfort-panels-rt-advanced-rt-professional)

#### Copying objects with linked objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

An object is linked to another object in the following situations, for example:

- You specify a tag for an alarm as a trigger tag.

  The alarm is the object. The tag is the linked object.
- You specify a connection for an external tag.

  The tag is the object. The connection is the linked object.

The object is always fully inserted during copying and pasting. Whether or not the linked object is pasted depends on the command used to insert it.

##### Simple pasting

The linked object is not copied. The linked object is transferred and handled as follows in the target HMI device:

- If an object with the same name exists, the existing object with its settings is used.
- If no object with the same name exists, the name of the object will be displayed. The object becomes invalid.

For some objects, linked objects are pasted automatically during simple pasting.

---

**See also**

[Linked objects copied automatically (Basic Panels)](#linked-objects-copied-automatically-basic-panels)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

#### Linked objects copied automatically (Basic Panels)

##### Copying linked objects

The following table shows the objects for which linked objects are pasted automatically in simple pasting.

| Object | Linked object |
| --- | --- |
| Screen | Template |
| Symbolic I/O field | Text list |
| Graphic I/O field | Graphics list |
| Graphic view | Graphic |
| Tag | Alarm |
| Logging tag <sup>1)</sup> |  |
| Cycle |  |
| Log <sup>1)</sup> | Logging tag <sup>1)</sup> |
| Recipe element | Text list |
| Scheduler | Triggers |

<sup>1) </sup>Only applies to Basic Panels 2nd Generation

---

**See also**

[Copying objects with linked objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-objects-with-linked-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

#### Linked objects copied automatically (Panels, Comfort Panels, RT Advanced)

##### Copying linked objects

The following table shows the objects for which linked objects are pasted automatically in simple pasting.

| Object | Linked object |
| --- | --- |
| Screen | Cycle |
| Template |  |
| Symbolic I/O field | Text list |
| Graphic I/O field | Graphics list |
| Graphic view | Graphic |
| Tag | Alarm |
| Logging tag |  |
| Cycle |  |
| Log | Logging tag |
| Logging tag | Log type |
| Recipe element | Text list |
| Scheduler | Triggers |

#### Copying HMI devices with HMI connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

If you copy an HMI device with HMI connections to a PLC, the HMI connection in the new HMI device is not automatically connected to an existing PLC with the same name. This applies to copying within a project as well as copying across projects.

##### Completing the configuration of the HMI connection

To also access the PLC tag via an HMI tag in the new HMI device, follow these steps:

1. Open the "Devices &amp; Networks" editor.
2. Connect the new HMI device to the required network.
3. Open the connection table.
4. Select the HMI connection of the new HMI device.
5. Select the required PLC under "Partner".

> **Note**
>
> If you compile the new HMI device or connect additional PLC tags in between copying the HMI device and completing the connection, there may be some instances in which an additional HMI connection to the same PLC is created. This is especially true if you connect HMI tags with DB array elements.

#### Copying linked screen objects with user data types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If you copy a screen object from a screen that uses a user data type to a screen that does not use a user data type, the tag references in the target screen are shown with the prefix "@NOP::".

##### Interconnection of the user data type

If you want the tag references to function in Runtime, interconnect a user data type to the target screen. The interconnection of the target screen to the user data type can then be deleted afterwards.

#### Drag & drop from the details view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can improve configuration efficiency with just a few simple measures. Below are a few examples of efficient configuration.

##### Pasting objects to a screen from the details view

You can drag objects in the details view from various different editors to other editors.

##### Pasting a symbolic I/O field

1. Open a screen.
2. Click on the "Text and graphics lists" editor in the project tree. All existing text and graphics lists will be shown in the details view.
3. Click on a text list, for example, "Textlist1" in the Details view.
4. Drag-and-drop a text list from the Details view to a screen. A symbolic I/O field has been created and connected to the text list "Textlist1".

##### Pasting a graphic I/O field

1. Open a screen.
2. Click on the "Text and graphics lists" editor in the project tree. All existing text and graphics lists will be shown in the details view.
3. Click on a graphics list in the Details view, for example "Graficlist1".
4. Drag-and-drop a graphics list from the Details view to a screen. A graphic I/O field has been created and connected to the graphics list "Graficlist1".

##### Pasting an I/O field

1. Open a screen.
2. Click on the "HMI tags" editor in the project tree. All existing HMI tags will be shown in the Details view.
3. Click on an HMI tag in the Details view, for example "Tag1".
4. Drag-and-drop the HMI tag from the Details view to a screen. An I/O field has been created and connected to the HMI tag "Tag1".

#### Copying screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You copy one or more screens from the "Screens" folder and paste them into the "Screens" folder of another device.

##### Type and size of the displays

In the case of HMI devices with keys, the available keys are displayed automatically in the screen. When a screen is copied between HMI devices, the keys are either displayed or hidden; functions configured for function keys are not transferred.

If there is less space for the screen in the target HMI device than in the source HMI device, you can adjust the size of and the spacing between existing objects.

##### Automatic fit to size for objects

1. Select "Options &gt; Settings &gt; Visualization &gt; Resize screen and screen objects" in the menu.
2. Activate, for example, "Fit to height".

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

#### Copying recipes within an HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### "Recipes" Editor

You can copy recipes, recipe elements and recipe data records within each table. You copy a recipe element to another recipe.

Only WinCC Runtime Professional: You can copy a recipe view element to another recipe view. If a recipe view element of the same name already exists, a conflict dialog is displayed. You can select whether to replace or rename the recipe element. You can copy recipe elements to the first empty row of the "Recipe views" editor, "Elements" tab.

You can copy a recipe data record to another recipe, if the other recipe contains the same number of recipe elements. If the data types differ, the value will be copied to the target data record but it is assigned an error flag.

##### "Tags" editor

You can drag-and-drop a tag to a recipe element in the "Tag" column. The tag is linked to the recipe element. If a tag is already linked, an error message will be generated.

##### "Screens" editor

If you drag-and-drop a recipe to a screen, a new recipe display will be created and linked to the recipe.

#### Differences between Runtime Advanced and Panels and Runtime Professional (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Overview

The following table shows the availability of the various functions in Runtime Advanced and Panels and Runtime Professional.

| Function in WinCC | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Logs | Yes  Data log  Alarm log | Yes  Data log  Compressed log  Alarm log |
| Scheduler | Yes | Yes |
| User administration | Yes | Yes |
| Screens | Yes | Yes |
| Settings | Yes | Yes |
| Global elements | Yes | No |
| Alarms | Yes  Alarm indicator  Alarm window  Alarm view | Yes  Alarm view with more functions than in Runtime Advanced and Panels |
| Menus and toolbars | No | Yes |
| Reports | Yes  Printout using the "PrintReport" system function | Yes  Printout using print job and scheduler |
| Recipes | Yes | User archives from WinCC V6.2 |
| Scripts | Yes  VBS | Yes  VBS  C |
| Structures | Yes | Yes |
| Text and graphics lists | Yes | Yes |
| Tags | Yes | Yes |
| Connections | Yes  Different communication drivers | Yes  Different communication drivers |
| Templates | Yes | No |
| Cycles | Yes | Yes |

### Copying and pasting between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
- [System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Limitations during copying (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#limitations-during-copying-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Objects in screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Connections
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Tag data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#tag-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Structures
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structures-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarms
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#logs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying VB scripts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-vb-scripts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying recipes between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-recipes-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying cycles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-cycles-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Reports
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Text and graphics lists
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#text-and-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User management
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Scheduled tasks
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#scheduled-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can copy and paste project data such as screens, objects and tags between devices in different runtimes.

##### Properties and settings

Objects that are supported in both Runtimes can have different properties and settings. During copying and pasting these differences are implemented as follows:

- Properties not supported by the target HMI device are not displayed.
- Default settings are specified for properties that are only supported by the target HMI device.
- Settings which are not supported by the target HMI device are replaced by default settings.

If you copy an object back to the source HMI device without manually changing the settings in the target HMI device, all properties and settings originally set in the source HMI device will be reactivated.

##### Unsupported events and animations

When you paste an object into a different Runtime, the following cases are possible:

- The target HMI device does not support events or animations for the object copied.

  Events or animations configured for the copied object are not displayed in the target HMI device.
- Events or animations for the object copied are only supported by the target HMI device.
- Certain events and animations are not supported by the target HMI device for the object copied.

  Events or animations that were configured for the copied object and are not supported by the target HMI device are not displayed on the target HMI device.
- Certain events and animations for the object copied are only supported by the target HMI device.

All events and animations originally set will be reactivated if you copy the same object back to the source HMI device.

---

**See also**

[Linked objects copied automatically (Basic Panels)](#linked-objects-copied-automatically-basic-panels)
  
[Limitations during copying (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#limitations-during-copying-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-elements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
  
[Copying tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

#### System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Supported system functions

The following system functions are supported in Runtime Advanced and Panels as well as Runtime Professional:

- ActivateScreen
- IncreaseTag
- InvertBit
- InvertBitInTag
- InverseLinearScaling
- LinearScaling
- ResetBit
- ResetBitInTag
- SetBit
- SetBitInTag
- SetTag
- StopRuntime
- DecreaseTag
- ShowLogonDialog

Additional system functions are supported in Runtime Advanced and Panels.

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Limitations during copying (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Differences between the Runtimes

Some functions are supported exclusively in one Runtime. Some functionalities are supported in both Runtimes, but have different concepts. You cannot copy and paste These functions between the Runtimes.

##### Functionalities only supported by Runtime Advanced and Panels

- Templates
- Global elements

You cannot copy these functions to Runtime Professional.

##### Functionalities only supported in Runtime Professional

- Menus and toolbars
- C scripts

You cannot copy these functions to Runtime Advanced and Panels.

##### Functions with different concepts

- Configuration
- Recipes

These functions cannot be copied between the Runtimes.

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

#### Objects in screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you copy an object from a screen and paste it into another screen, the object is inserted at the same position in the screen.

##### Text and graphics lists

When you copy a symbolic I/O field with a text list or a graphic I/O field with a graphics list and paste it into another runtime, the text list or graphics list will be copied to the target HMI device.

##### Copying objects from reports

You can copy objects that are supported in the screen from a report into a screen. Unsupported settings are replaced by supported settings. When you copy a copied object back into a report, the changed settings remain active.

##### Recipe view and alarm view

The "Recipe view" and "Alarm view" objects have such different concepts that you cannot copy and paste these objects between the two Runtimes.

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Supported objects

The following table shows which objects in screens are supported in which Runtime:

Basic objects

| Object | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Line | Yes | Yes |
| Polyline | Yes | Yes |
| Polygon | Yes | Yes |
| Ellipse | Yes | Yes |
| Ellipse segment | No | Yes |
| Circle segment | No | Yes |
| Ellipse arc | No | Yes |
| Circular arc | No | Yes |
| Circle | Yes | Yes |
| Rectangle | Yes | Yes |
| Connector | No | Yes |
| Text field | Yes | Yes |
| Graphic view | Yes | Yes |
| Pipe | No | Yes |
| Double T-piece | No | Yes |
| T piece | No | Yes |
| Pipe bends | No | Yes |

Elements

| Object | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| I/O field | Yes | Yes |
| Editable text field | No | Yes |
| List box | No | Yes |
| Combo box | No | Yes |
| Button | Yes | Yes |
| Date/time field | Yes | No |
| Round button | No | Yes |
| Symbolic I/O field | Yes | Yes |
| Graphic I/O field | Yes | Yes |
| Bar | Yes | Yes |
| Switch | Yes | No |
| Symbol library | Yes | Yes |
| Slider | Yes | Yes |
| Scroll bar | No | Yes |
| Check box | No | Yes |
| Option buttons | No | Yes |
| Gauge | Yes | Yes |
| Clock | Yes | Yes |
| Disk space view | No | Yes |
| Charge condition | Yes | No |
| Effective range name | Yes | No |
| Effective range name (RFID) | Yes | No |
| Effective range signal | Yes | No |
| Zone name | Yes | No |
| Zone signal | Yes | No |

Controls

| Object | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Screen window | No | Yes |
| Trend view | Yes | No |
| User view | Yes | Yes |
| HTML browser | Yes | Yes |
| Print job/Script diagnostics | No | Yes |
| Sm@rtClient view | Yes | No |
| Watch table | Yes | No |
| Recipe view | Yes | Yes |
| Alarm view | Yes | Yes |
| f(x) trend view | Yes | Yes |
| f(t) trend view | No | Yes |
| Table view | No | Yes |
| Value table | No | Yes |
| System diagnostics view | Yes | Yes |
| Media Player | No | Yes |
| Channel diagnostics view | No | Yes |
| PLC code view | Yes | Yes |
| GRAPH overview | Yes | Yes |
| ProDiag overview | Yes | Yes |
| Criteria analysis view | Yes | Yes |
| Camera view | Yes | No |
| PDF view | Yes | No |

---

**See also**

[Objects in reports (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Events for scheduled tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#events-for-scheduled-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#tag-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Communication drivers

Please refer to the communications manual for information about the communication drivers possible in the Runtimes. Runtime Advanced and Panels and Runtime Professional support different communication drivers. There is no common communication driver for both runtimes.

###### Area pointer

The area pointers are not supported in Runtime Professional.

---

**See also**

[Objects in screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
  
[Copying connections (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-connections-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Copying connections  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a connection in the "Connections" editor and paste it in the "Connections" editor of another Runtime.

###### Integrated connections

Integrated connections are created under "Devices &amp; networks" in the network view. An integrated connection is displayed in the "Connections" editor. However, you cannot edit the integrated connection in the "Connections" editor. Any integrated connection you copy and paste from the "Connections" editor to another Runtime will become invalid in the target HMI device as it lacks a communication partner. You can only edit the copied integrated connection in the network view of the target device.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Copying tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can copy a tag in the "Tags" editor and paste it in the "Tags" editor of another Runtime.

##### Unsupported data types

If you copy a tag with a data type that is not supported in the other Runtime, then the data type will become invalid.

##### Logging tags

If you have linked the tag to a logging tag, this logging tag will be copied to the target HMI device together with the tag. A logging tag has to be assigned to a data log. A new log will be created if there is no corresponding data log in the target HMI device.

##### Alarms

Any analog or discrete alarms you have configured for a tag will be copied to the target HMI device together with the tag.

##### System tags

System tags are supported in Runtime Professional only.

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
  
[Tag data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#tag-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Archive tags (Panels, Comfort Panels, RT Advanced, RT Professional)](#archive-tags-panels-comfort-panels-rt-advanced-rt-professional)

#### Tag data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Data types

The following table shows which data types are supported in which Runtime.

| Data type | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Boolean | Yes | Yes |
| Byte (Signed Byte) | Yes | Yes |
| UByte (Unsigned Byte) | Yes | Yes |
| Short (Signed Int) | Yes | Yes |
| UShort (Unsigned Int) | Yes | Yes |
| Long (Signed Long) | Yes | Yes |
| ULong (Unsigned Long) | Yes | Yes |
| Float | Yes | Yes |
| Double | Yes | Yes |
| String | Yes | Yes |
| UString (Unicode String) | No | Yes |
| Raw (Raw Data Type) | No | Yes |
| Ref (Text Reference) | No | Yes |
| Date Time | Yes | Yes |

##### Properties

The following properties are supported in Runtime Advanced and Panels as well as Runtime Professional:

- Address
- Content (comment)
- Connection
- Control variable
- Data type
- Length
- Limits:

  - Upper error
  - Generate analog alarm for upper error
  - Upper warning
  - Generate analog alarm for upper warning
  - Low
  - Generate analog alarm for lower warning
  - Lower error
  - Generate analog alarm for lower error
- Linear scaling
- Name
- HMI device end value
- HMI device start value
- PLC end value
- PLC start value
- Start value

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Structures (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Structure elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-elements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Structure types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Structure data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Structure elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a structural element in the "Structures" editor and paste it in the "Structures" editor of another Runtime.

###### Unsupported data types

If you copy a structural element with a data type that is not supported in the other Runtime, the data type becomes invalid in the "Structure" editor.

---

**See also**

[Structure types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure data types and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-data-types-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

##### Structure types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a structure type from the "Structures" folder and paste it into the "Structures" folder of another Runtime.

###### Unsupported controller types

Since no controller type is supported in both Runtimes, the controller type will be invalid in the target HMI device.

###### Device family

The device family is adapted to the target HMI device when copied. If you copy a structure type from Runtime Advanced and Panels to Runtime Professional, for example, the "SmartCE" entry automatically becomes "SCADA."

###### Internal and external data types

In Runtime Advanced and Panels, a structure type can contain either exclusively internal data types or exclusively external ones. In Runtime Professional, both internal and external data types can be contained in one structure type.

If you copy a structure type that contains internal and external data types from Runtime Professional to Runtime Advanced and Panels, all internal data types become invalid. Since no communication peer is supported in both Runtimes, all external data types become invalid as well.

---

**See also**

[Structure elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-elements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Structure data types and properties  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Data types

The following table shows which data types are supported in which Runtime.

| Data type | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Boolean | Yes | Yes |
| Byte (Signed Byte) | Yes | Yes |
| UByte (Unsigned Byte) | Yes | Yes |
| Short (Signed Int) | Yes | Yes |
| UShort (Unsigned Int) | Yes | Yes |
| Long (Signed Long) | Yes | Yes |
| ULong (Unsigned Long) | Yes | Yes |
| Float | Yes | Yes |
| Double | Yes | Yes |
| String | Yes | Yes |
| UString (Unicode String) | No | Yes |
| Raw (Raw Data Type) | No | Yes |
| Ref (Text Reference) | No | Yes |
| Date Time | Yes | No |

###### Properties

The following properties are supported in Runtime Advanced and Panels as well as Runtime Professional:

Structure types:

- Comment: Contents
- Name
- Type of controller
- Device family

Structural elements:

- Comment: Contents
- Data type
- Length
- Linear scaling
- Name
- HMI device end value
- HMI device start value
- PLC end value
- PLC start value
- Error upper limit
- Error lower limit
- Start value
- Bit offset
- Offset

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Controller alarms and system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-and-system-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Differences between Runtime Advanced and Panels and Runtime Professional  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Supported objects in the screen

You can configure the following objects for screen alarm display in Runtime Advanced and Panels:

- Alarm view
- Alarm window
- Alarm indicator

In Runtime Professional, you can only configure an alarm view.

The concepts of the alarm view in the Runtimes are so different that it is not possible to copy an alarm view between the Runtimes.

###### Alarm text blocks

Alarm blocks are supported in Runtime Professional only.

---

**See also**

[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Controller alarms and system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-and-system-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

##### Discrete alarms  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a discrete alarm in the "Alarms" editor in the "Discrete alarms" tab and paste it to another Runtime. Pasting a tag with configured discrete alarms to the "Tags" editor will automatically also paste the corresponding discrete alarms to the "Alarms" editor.

###### Supported properties

The following properties are supported in Runtime Advanced and Panels as well as Runtime Professional:

- ID
- Alarm class
- Alarm group
- Acknowledgment: Tag
- Acknowledgment: Bit
- Tooltip
- Trigger: Tag
- Trigger: Bit
- Event text

###### Alarm number

Alarm numbers which do not yet exist in the target HMI device are transferred unchanged when copied. If the alarm number already exists, the next free number is assigned automatically as the alarm number for the discrete alarm.

###### Tooltip

Copying a tooltip with more than 255 characters to Runtime Professional will make the entire tooltip invalid.

###### Event text

The event text is displayed in the following dialog boxes of the Inspector window:

- Runtime Panels and Advanced:

  "Properties &gt; Properties &gt; General &gt; Settings &gt; Event text"
- Runtime Professional:

  "Properties &gt; Properties &gt; Texts &gt; Settings &gt; Event text"

The event texts are copied into the corresponding dialog boxes with all the format data.

Event texts will become invalid:

- if you copy an event text with more than 254 characters to Runtime Advanced and Panels.
- if you copy an event text with a dynamic parameter to Runtime Panels and Advanced.
- if you copy an event text with a text list from Runtime Panels and Advanced to Runtime Professional.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy an analog alarm in the "Alarms" editor in the "Analog alarms" tab and paste it to another Runtime. Pasting a tag with configured analog alarms to the "Tags" editor will automatically also paste the corresponding analog alarms to the "Alarms" editor.

###### Supported properties

The following properties are supported in Runtime Advanced and Panels as well as Runtime Professional:

- Alarm number "ID"
- Event text
- Alarm class
- Alarm group
- Tooltip
- Trigger: Tag
- Delay
- Limit value
- Trigger mode
- Synchronize limit value
- Hysteresis mode
- Hysteresis
- Hysteresis as a percentage

###### Alarm number "ID"

Alarm numbers which do not yet exist in the target HMI device are transferred unchanged when copied. If the alarm number already exists, the next free number is assigned automatically as the alarm number for the analog alarm.

###### Event text

The event text is displayed in the following dialog boxes of the Inspector window:

- Runtime Advanced and Panels:

  "Properties &gt; Properties &gt; General &gt; Settings &gt; Event text"
- Runtime Professional:

  "Properties &gt; Properties &gt; Texts &gt; Settings &gt; Event text"

The event texts are copied into the corresponding dialog boxes with all the format data.

Event texts will become invalid:

- if you copy an event text with more than 254 characters to Runtime Advanced and Panels.
- if you copy an event text with a dynamic parameter to Runtime Panels and Advanced.
- if you copy an event text with a text list from Runtime Panels and Advanced to Runtime Professional.

###### Tooltip

Copying a tooltip with more than 255 characters to Runtime Professional will make the entire tooltip invalid.

###### Delay

If you copy a delay with the "Minute" or "Hour" unit from Runtime Professional to Runtime Advanced and Panels, the setting becomes invalid.

---

**See also**

[Copying tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Controller alarms and system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Controller alarms

Since controller alarms are configured in the controller, it is not possible to copy controller alarms.

###### System alarms

Because system alarms are dependent on the HMI device, it is not possible to copy system alarms.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy an alarm class in the "Alarms" editor in the "Alarm classes" tab and paste it to another Runtime.

###### Predefined alarm classes

You cannot copy and paste predefined alarm classes.

###### Log

In Runtime Advanced and Panels, you configure an archive in which the alarm is stored. In Runtime Professional, you specify whether the alarm is logged for each alarm of an alarm class.

During the copying process the logging specifications are implemented as follows:

- Copying from Runtime Advanced and Panels to Runtime Professional:

  If a log has been created in Runtime Advanced and Panels, "Log" is activated in Runtime Professional.

  If no log has been created in Runtime Advanced and Panels, "Log" is deactivated in Runtime Professional.
- Copying from Runtime Professional to Runtime Advanced and Panels:

  If "Log" is activated in Runtime Professional, you need to specify a log in Runtime Advanced and Panels.

  If "Log" is deactivated in Runtime Professional, the entry &lt;No log&gt; is specified in Runtime Advanced and Panels.

###### Flashing

The settings for the flash behavior are not copied.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Alarm groups  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Copying and pasting

You can copy an alarm group in the "Alarms" editor in the "Alarm groups" tab and paste it to another Runtime.

###### Alarm groups from alarm classes

Alarm groups from alarm classes are only supported in Runtime Professional and cannot be copied and pasted to Runtime Advanced and Panels.

###### Hierarchy

Hierarchies of alarm groups are only supported in Runtime Professional. When copied between the Runtimes the hierarchy order is implemented as follows:

- Copying from Runtime Advanced and Panels to Runtime Professional

  If you copy an alarm group into the "Alarm groups" tab of the "Alarms" editor, the alarm group is inserted regardless of any existing alarm groups.

  If you copy an alarm group into a line containing an existing alarm group, the alarm group is inserted as an alarm group that is subordinate in the hierarchy.
- Copying from Runtime Professional to Runtime Advanced and Panels

  Hierarchies cannot be shown in Runtime Advanced and Panels. Alarm groups from all hierarchy levels are inserted independently of each other.

###### ID of the alarm group

Alarm numbers which do not yet exist in the target HMI device are transferred unchanged when copied.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-2)
- [Data logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#data-logs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Archive tags (Panels, Comfort Panels, RT Advanced, RT Professional)](#archive-tags-panels-comfort-panels-rt-advanced-rt-professional)

##### Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Logs

Data logs are supported in both Runtimes. You can copy and paste alarm logs and compressed logs between the runtimes.

###### Properties

The following properties are supported in Runtime Advanced and Panels as well as Runtime Professional:

Data logs

- Name
- Comment
- Storage location

Logging tags

- Name
- Process variable
- Triggers
- Logging cycle
- High limit
- Low limit
- Comment

###### Events

You cannot copy configured events between Runtime Advanced and Panels and Runtime Professional.

---

**See also**

[Data logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#data-logs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Archive tags (Panels, Comfort Panels, RT Advanced, RT Professional)](#archive-tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

##### Data logs  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Copying and pasting

You can copy a data log in the "Historical Data" editor in the "Data log" tab and paste it to another Runtime. All logging tags contained in the data log are included automatically.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-2)

##### Archive tags (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a logging tag in the "Historical Data" editor in the "Data log" tab and paste it in another Runtime.

In addition, you can copy a logging tag in the "Tags" editor of Runtime Professional and paste it into the "Historical Data" editor in Runtime Advanced and Panels. To copy a logging tag in Runtime Professional, open the "Tags" editor and select the "Alarms &amp; Logs" tab in the upper work area. Copy the desired logging tag in the lower work area of the "Data logs" tab.

###### Tags used in the logging tags

Any logging tag you have linked to a tag will be automatically also copied if the tag is copied to the target HMI device. A new log will be created if there is no corresponding data log in the target HMI device. There may be performance problems if too much of this additional data is copied.

###### Multiple logging of tags

When copying from Runtime Professional to Runtime Advanced and Panels, the process tags of a logging tag become invalid in the following situations:

- The tag has been logged more than once in Runtime Professional.
- Several logging tags are linked to the same process tag.

###### Triggers

If you paste a logging tag with a cycle, the cycle will be included in the target HMI device.

In Runtime Professional, configure the log cycle of logging tags in the form "factor x cycle", for example, twice an hour. The "Factor" property is not supported in Runtime Advanced and Panels. The Factor property is therefore set to the default of "1" when copying from Runtime Advanced and Panels to Runtime Professional. When copying from Runtime Professional to Runtime Advanced and Panels, only the cycle can be seen in Runtime Advanced and Panels; the factor is not taken into consideration. If you copy a cycle of "3 x 1h" from Runtime Professional to Runtime Advanced and Panels, for example, this is set in Runtime Advanced and Panels as "1h".

###### Copying logging tags from the "Tags" editor

When you copy a logging tag from the "Tags" editor in Runtime Professional into the "Historical Data" editor in Runtime Advanced and Panels, the "Process tag" property is linked to an existing tag with the same name. If there is no tag with the same name, the "Process tag" property becomes invalid. The "Data log" property is linked to the selected data log.

If you copy a logging tag from the "Tags" editor in Runtime Professional to the "Tags" editor of another HMI device, the "Data log" property will not be transferred.

###### Copying logging tags from the "Historical Data" editor

When you copy a logging tag from the "Historical Data" editor in Runtime Advanced and Panels into the "Tags" editor in Runtime Professional, the "Data log" property will not be transferred.

When you copy a logging tag from the "Historical Data" editor into the "Logs" editor of another HMI device, the "Process tag" property is linked to an existing tag with the same name. If there is no tag with the same name, the "Process tag" property becomes invalid. The "Data log" property is linked to the selected data log.

###### Logging tags used in compressed logging tags

When you copy a logging tag used in a compressed logging tag in Runtime Professional to Runtime Advanced and Panels, the settings for the compressed logging tag are also copied in the background. There may be performance problems if too many of these unnecessary settings are copied to Runtime Advanced and Panels.

---

**See also**

[Copying tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-2)

#### Copying VB scripts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Object types, properties and methods in VB script

The objects, object types, properties and methods supported in Runtime Advanced and Panels and Runtime Professional are listed in the VBS reference.

##### Pasting

You can copy VB scripts

- using the shortcut menu or by drag &amp; drop from the project tree
- from the code of an open VB script to another open VB script.

##### Objects called in VB script

You copy a VB script. Objects and their properties which do not exist in or are not supported by the target HMI device are called in the VB script. The syntax check reports an error. Correct the invalid object references.

##### Variables called up in a VB script

The syntax check will report errors if tags are called in the copied VB script that do not exist in the target HMI device or only exist with a different data type. Replace the invalid tags with tags that exist in the target HMI device.

If you are planning to copy scripts into different Runtimes, use the same variables in the Runtimes.

#### Copying recipes between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Recipe and recipe element

The recipe elements and recipe data records will also be copied if a recipe is copied.

> **Note**
>
> **Inconsistent data**
>
> Properties not supported by the HMI device, for example data type, will be formally copied but will appear with an error flag.
>
> Check the properties and reassign those flagged.

You can drag-and-drop a recipe element into the first empty line of the "Recipes Element" editor of another HMI device. The recipe element is inserted into the other recipe. If the recipe does not have the "Tags" communication type, the associated tag will be copied but it is assigned an error flag.

##### Points to note when copying from WinCC Runtime Advanced and Panels to WinCC Runtime Professional

The properties below are preset as follows and may subsequently be edited:

- "Tags" communication type
- "Limited" size type
- Number of data records

The storage location of the recipe is changed to "Database".

With a recipe element, the link will be copied but not the linked tag. You need to copy the tag separately or create a new tag with the same name. The same applies to the text list.

> **Note**
>
> **Inconsistent data**
>
> Array tags are not supported in WinCC Runtime Professional. After copying the recipe, create as many recipe elements and tags as there are array elements in the linked array tag. Link the new recipe elements to the tags. Copy the values of the source recipe data records to the target recipe data records.

##### Points to note when copying from WinCC Runtime Professional to WinCC Runtime Advanced and Panels

The following properties will be changed but cannot be edited:

- "Tags" communication type
- "Limited" size type
- Number of data records per HMI device
- "File" storage location with default path

##### Recipe data record and recipe query

You can copy a recipe data record to another recipe, if the other recipe contains the same number of recipe elements. If the data types differ, the value will be copied to the target data record but it is assigned an error flag.

##### Features specific to WinCC Runtime Professional

You can drag-and-drop a recipe query into the first empty row of the "Recipe queries" editor of another HMI device. The recipe query is copied but not the linked recipe elements and their recipes.

#### Copying cycles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can copy cycle in the "Cycles" editor and paste it in the "Cycles" editor of another Runtime. Referenced cycles are also copied whenever tags, logging tags or tasks are copied. The cycles are then displayed in the "Cycles" editor.

##### Supported properties

The date and time of the last change are updated during pasting.

##### Properties

The "Starting point" property is only supported in Runtime Professional.

##### Cycle units

Runtime Professional and Runtime Advanced and Panels support different cycle units.

---

**See also**

[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

#### Reports (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Copying a report (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-a-report-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Objects in reports (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

When you copy an object from a report and paste it into another report, the object is inserted at the same position in the report.

###### Supported properties

The concepts of the "Recipe display" and "Alarm view" objects differ so greatly that they cannot be copied and pasted between the various Runtimes.

###### Text and graphics lists

Text and graphics lists are automatically copied along with symbolic and graphic I/O fields and are then displayed in the "Text and graphics lists" editor.

###### Copying objects from screens

You can copy objects supported in the report from a screen to a report. Unsupported settings are replaced by supported settings. When you copy a copied object back into a screen, the changed settings remain active.

---

**See also**

[Objects in screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Copying a report (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-a-report-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects in reports (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

##### Copying a report (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a report from the "Reports" folder and paste it into another "Reports" folder.

###### Watermarks

Watermarks are only supported in Runtime Professional. When you copy a report from Runtime Professional to Runtime Advanced and Panels, the areas for the watermarks will no longer be shown.

###### Print jobs

The print jobs in the "Reports" folder are only supported in Runtime Professional and cannot be copied and pasted between Runtimes.

---

**See also**

[Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Objects in reports (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Supported objects

The following table shows which objects are supported in which Runtime:

| Basic object | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Line | Yes | Yes |
| Polyline | Yes | Yes |
| Ellipse | Yes | Yes |
| Circle | Yes | Yes |
| Ellipse segment | No | Yes |
| Circle segment | No | Yes |
| Elliptical arc | No | Yes |
| Circular arc | No | Yes |
| Rectangle | Yes | Yes |
| Polygon | Yes | Yes |
| Text field | Yes | Yes |
| I/O field | Yes | Yes |
| Symbolic I/O field | Yes | No |
| Date/time field | Yes | No |
| Graphic I/O field | Yes | No |
| Alarm view | No | Yes |
| Recipe view | No | Yes |
| Table view | No | Yes |
| f(t) trend view | No | Yes |
| f(x) trend view | No | Yes |
| Page number | Yes | Yes |
| Report name | No | Yes |
| Project name | No | Yes |
| Hardcopy | No | Yes |
| ODBC database field | No | Yes |
| ODBC database table | No | Yes |
| CSV provider tables | No | Yes |
| CSV provider trends | No | Yes |
| Alarm report | Yes | No |
| Recipe report | Yes | No |
| Control data | No | Yes |
| Control hard copy | No | Yes |
| Control Information | No | Yes |

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Text and graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)
- [Copying text lists and graphic lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-text-lists-and-graphic-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Differences between Runtime Advanced and Panels and Runtime Professional  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Ranges in text lists

When specifying a range the following settings are supported in both Runtimes:

- Individual value
- Range

The following settings are supported in Runtime Professional:

- To (&lt;=)
- From (&gt;=)

---

**See also**

[Copying text lists and graphic lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-text-lists-and-graphic-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

##### Copying text lists and graphic lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a text or graphics list in the "Text and graphics lists" editor and paste it to the same editor in another runtime. Text and graphics lists are also automatically copied along with symbolic and graphic I/O fields and displayed in the "Text and graphics lists" editor.

###### List entries

When a text or graphics list is copied, the corresponding list entries are included in copying. You can also copy and paste the list entries individually.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

#### User management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
- [Copying users, user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-users-user-groups-and-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Users

Properties for dynamic logon and web client administration are only supported in Runtime Professional.

###### User groups

The "DisplayName" and "Number" properties are only supported in Runtime Advanced and Panels.

Properties for web client administration are only supported in Runtime Professional.

---

**See also**

[Copying users, user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-users-user-groups-and-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-3)

##### Copying users, user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Copying and pasting

You can copy users, user groups and authorizations in the "User administration" editor.

When you copy a user, the corresponding user group is not copied.

When you copy a user group, the corresponding authorizations are not copied.

###### Default entries and system authorizations

The following users, user groups and authorizations are predefined. They cannot be deleted and may only be edited to a limited extent:

- predefined user "Administrator"
- predefined groups "Administrator" and "Operators"
- predefined authorizations, such as "Operate" and "Enable remote control"

You can copy the predefined entries and paste them into another Runtime. The entries copied are pasted as user-defined entries and can then be edited.

---

**See also**

[Differences between Runtime Advanced and Panels and Runtime Professional (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#differences-between-runtime-advanced-and-panels-and-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)

#### Scheduled tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Copying tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#copying-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Events for scheduled tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#events-for-scheduled-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Copying tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can copy a scheduled task in the "Scheduler" editor and paste it to the "Scheduler" editor of another device.

###### Task type

The "Print job" task type is supported in Runtime Professional only. Types that are not supported in both Runtimes become invalid after they have been pasted.

---

**See also**

[Events for scheduled tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#events-for-scheduled-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-4)
  
[System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Events for scheduled tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Events

The following table shows which events are supported in which Runtime:

| Event | Runtime Advanced and Panels | Runtime Professional |
| --- | --- | --- |
| Screen change | Yes | No |
| User change | Yes | No |
| Alarm buffer overflow | Yes | No |
| Runtime stop | Yes | Yes |
| When a dialog is opened | Yes | No |
| When a dialog is closed | Yes | No |
| Disabled | Yes | Yes |
| Once | Yes | Yes |
| 250 milliseconds | No | Yes |
| 500 milliseconds | No | Yes |
| 1 second | No | Yes |
| 2 seconds | No | Yes |
| 5 seconds | No | Yes |
| 10 seconds | No | Yes |
| 1 minute | Yes | Yes |
| 5 minutes | No | Yes |
| 10 minutes | No | Yes |
| 1 hour | Yes | Yes |
| Once daily | Yes | Yes |
| Once weekly | Yes | Yes |
| Once monthly | Yes | Yes |
| Once yearly | Yes | Yes |
| Tag triggers | No | Yes |

---

**See also**

[Screen objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Copying between different RT and ES versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can copy and paste project data such as screens, objects or tags between projects with different WinCC versions.

All configurations that are supported in the target version are retained when you copy data between projects of different WinCC versions. Configurations that are not supported by the target version are marked as invalid with a color code.

#### Copy of control between HMI devices from different device versions

WinCC supports all configurations of a previous WinCC version.

The following applies when copying within different ES versions:

- All the configurations that are also supported in the respective RT version are retained.
- Default settings are defined for configurations that are only supported in the WinCC version of the target project.
- Configurations that are not supported by the respective RT version are marked by color as invalid or are not displayed.

  All properties and settings originally defined in the source HMI device are reactivated when you copy an object back to the source HMI device unchanged.

  ![Copy of control between HMI devices from different device versions](images/53306460171_DV_resource.Stream@PNG-en-US.png)
- The HMI device must be valid for the current Runtime version.

#### Copying between different ES versions

To copy between two TIA projects, open a second instance of the TIA Portal. You can only copy between projects that have the same ES version. The ES version of a project is indicated by the file extension *.ap&lt;version_number&gt;.

![Copying between different ES versions](images/53305525387_DV_resource.Stream@PNG-en-US.png)

![Copying between different ES versions](images/53306447499_DV_resource.Stream@PNG-en-US.png)

## Using WinCC version compatibility (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on version compatibility (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-version-compatibility-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Upgrading projects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#upgrading-projects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Upgrading a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#upgrading-a-global-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Changing between device versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#changing-between-device-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Changing the runtime version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#changing-the-runtime-version-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Upgrading the runtime project with logging data (RT Professional)](#upgrading-the-runtime-project-with-logging-data-rt-professional)
- [Version compatibility of devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#version-compatibility-of-devices-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on version compatibility (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The interaction of the following versions is of importance for version compatibility:

- WinCC version
- Project version
- Runtime version
- Device version

#### WinCC version

The WinCC version is that installed on the configuration PC for TIA Portal, for example, WinCC V17.

#### Project version

The project version is the version of a WinCC project.

**New projects**

When you create a new WinCC project, the project version is always the same as the WinCC version.

**Existing projects**

An existing project can have a project version that is older than the WinCC version.

> **Note**
>
> **Upgrading a project with an older project version**
>
> To open a WinCC project that was created with an older TIA Portal, you must first upgrade its project version to the WinCC version of the currently installed TIA Portal.
>
> After the upgrade, the functions of the current WinCC version are available in the project. You can then open, edit, save, compile, download or simulate the project.
>
> See also section [Upgrading projects](#upgrading-projects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional).
>
> If the project version may not be changed, open the project in a TIA Portal whose WinCC version is the same as the project version. Edit, save, compile, download or simulate the project there.

#### Runtime version

The runtime version is that configured in a WinCC project for an HMI device.

A WinCC-project can include HMI devices for which different runtime versions were configured. HMI devices whose runtime version is older than the current version can be restricted in their functions when compared to the HMI devices with the current version.

The runtime version must be compatible with the device version of the target device so that the project can be loaded.

**Runtime version in the case of newly added devices**

When you add a new HMI device in a WinCC project, the default runtime version is always the same as the WinCC version.

To add a new device with an older version, select the desired version in the "Add New Device" dialog.

**Changing the runtime version**

You can change the runtime version in the "Devices &amp; Networks" editor or in the device properties in the project tree. See also section [Changing the runtime version](#changing-the-runtime-version-basic-panels-panels-comfort-panels-rt-advanced-rt-professional).

#### Device version

**Panel as HMI device**

For Panels, the operating system and the runtime version are bundled with a device version in an image, which, if required, can be uploaded to the HMI device. The selection of the device version determines which version of the operating system and the runtime are installed with the image.

The device version installed with the image on the Panel must be compatible with the runtime version configured in WinCC so that the project can be loaded.

> **Note**
>
> **Installing image with compatible version**
>
> When TIA Portal detects incompatible versions during online loading, you have the option, in the "Load Preview" dialog, to install an image with a compatible device version to the Panel before the loading.
>
> See also Chapters [Overview for loading of projects](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-for-loading-of-projects-basic-panels) and [Overview for loading of projects](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-for-loading-of-projects-panels-comfort-panels).

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the device version deletes all data on the Panel.**  When you install an image on the Panel, the data on the Panel is deleted.   Backup any existing runtime data before you install an image with a different device version. |  |

**Personal computer as HMI device**

For PCs, the operating system and runtime are installed independently of one another. The version installed on the PC for runtime must be compatible with the runtime version configured in WinCC.

#### Version compatibility

The following figure shows the interaction of the different versions:

![Version compatibility](images/137542930059_DV_resource.Stream@PNG-en-US.png)

During a download to a target device, make sure that the runtime version and the device version are compatible.

TIA Portal checks the compatibility during the download. The following applies when incompatible versions are detected:

- Target device Panel: In the "Load Preview" dialog, you are given the option to install an image with a compatible version on the Panel.
- Target device PC: Upload is not possible

### Upgrading projects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

To open a WinCC project that was created with an older engineering system, you must first upgrade its project version to the WinCC version of the currently open engineering system.

#### Requirements

- The project version is a predecessor of your WinCC version.
- You have write access to your project drive.
- The project drive provides sufficient storage capacity for another project of this size.

#### Procedure

To upgrade a project from TIA Portal V16 or higher to your WinCC version, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open Project" dialog box opens and the list of recently used projects is displayed.
2. Select a project from the list and click "Open".
3. If the project you require is not included in the list, click the "Browse" button. Navigate to the desired project folder and open the project file.

   The "Open Project" dialog opens.
4. Click "Upgrade".

   The project is upgraded to the current project version and opened.
5. Then compile each device in the project with the command "Edit &gt; Compile".

**Note**

If devices that are not supported in the project are configured, the project is not upgraded. An error message will inform you of this.

To nevertheless upgrade a project, change the device version of the affected device or the device itself with the menu command "Change device/version".

**Note**

**Sequence of compilation**

Compile the controllers first, and then the HMI devices in your project. In this way, you ensure that the controller data required to compile the HMI devices is available.

#### Result

- The content of the old WinCC project is saved in a new project with the current project version.

  The original project is not overwritten and can still be edited with a compatible older version of the TIA Portal.
- You can open, edit, save, compile, download or simulate the project.
- All functions of the current WinCC version are available in the project.
- If necessary, also apply the WinCC version as a configured runtime version for the configured HMI devices.

### Upgrading a global library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

To process objects of a global library in a project, you must first upgrade the version of the global library to the project version. You are prompted accordingly when you open the global library.

#### Requirements

- The version of the global library is a predecessor of your WinCC version.
- You have write access to your project drive.
- All types in the library have been released.

> **Note**
>
> **Upgrading a user library**
>
> If you want to use a user library from an earlier version of WinCC, you must upgrade it. Make sure that all types of the library have been released. The library being upgraded cannot contain a type with the "in progress" status.

#### Procedure

Proceed as follows to upgrade a global library from TIA Portal V12.x or lower:

1. Open the global library.

   The "Upgrade global library" dialog box opens.
2. Click "OK".

#### Result

A copy of the global library is created and upgraded. The global library opens.

---

**See also**

[Managing libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Changing between device versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Selection of the device version

When you configure a new HMI device, WinCC automatically selects the latest version of the device.

If you want to use a device version other than the one set in WinCC, transfer an image to the HMI device. WinCC provides the images required for the supported HMI devices.

Information on the device versions used in WinCC is available in the FAQs on the Internet, entry ID 21742389.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the device version deletes all data on the HMI device.**  Data is deleted on the target system if you change the device version. For this reason, you should save existing Runtime data before changing the device version. |  |

#### HMI device configuration

The following figure shows the software components of an HMI device:

![HMI device configuration](images/9778628747_DV_resource.Stream@PNG-en-US.png)

### Changing the runtime version (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Depending on the required device version, select the runtime version suitable for your configuration.

#### Requirements

- A project has been created and opened.
- The project contains an HMI device.

#### Procedure

To change the device version, follow these steps:

1. Double-click on "Devices &amp; Networks" in the project tree.

   The editor opens.
2. Select the required HMI device from the device view.
3. Select "Change Device/Version" in the device shortcut menu of the HMI device.

   A dialog opens.
4. Select the required HMI device.
5. Depending on the device version installed on the target device, select a compatible runtime version under "Version".
6. Confirm your selection with "OK".

**Note**

**Selection of runtime versions**

The project version determines which runtime versions are offered to you.

#### Result

You have changed the runtime version of the device in the WinCC project.

### Upgrading the runtime project with logging data (RT Professional)

The following section describes how you can upgrade a runtime project including its logging data to a higher, installed runtime version in WinCC Runtime Professional. Your procedure depends on whether you run the project on the same device after the upgrade, or replace the device with a device that has a higher runtime version.

#### Upgrading on the same device.

1. In the engineering system: Install the desired WinCC version.
2. In the engineering system: Upgrade the project version of the project to the WinCC version.
3. On the HMI device: Exit runtime and back up the runtime data and logging data of the runtime project to an external storage medium.
4. On the HMI device: Install the desired runtime version.
5. On the HMI device: Copy the backed up data back to the HMI device.
6. In the engineering system: Compile the project completely and download it (all).

   When loading, select the target directory to which you have previously copied the saved project.

#### Upgrading through device replacement

1. In the engineering system: Install the desired WinCC version.
2. In the engineering system: Upgrade the project version of the project to the WinCC version.
3. On the old HMI device: Back up the runtime data and logging data of the runtime project to an external storage medium.
4. On the new HMI device: Install the desired runtime version.
5. On the new HMI device: Copy the backed up data to the HMI device.
6. In the engineering system: Compile the project completely and download it (all).

   When loading, select the target directory to which you have previously copied the saved project.

#### Result

The project including its logging data is available on the HMI device in the upgraded runtime version.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Conversion of the logging data during the project start**  When the project is started for the first time, its logging data are adapted to the new database schema. This process is irreversible.   You can no longer transfer the log to a device with a lower runtime version and run it there. |  |

### Version compatibility of devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Unsupported devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#unsupported-devices-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Devices not fully supported (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#devices-not-fully-supported-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Unsupported devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Error during upgrade

If a project contains devices or device versions that are no longer supported in the current version of WinCC, you get the error message "Open the project with an older version of WinCC and change the device or the device version in the project and the library." To upgrade the project to the current version, you need to open the project in an older version of WinCC and change the device type or version to a value supported by the current version of WinCC.

Unsupported devices may be present in a project in the following locations:

- Devices in the project tree
- Devices in the master copies of the project library

##### Changing the device type or the device version in the project tree

To change the device type or the device version of a device in the project tree, follow these steps:

1. Select the "Change device/version" command in the shortcut menu of the outdated device.
2. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.

##### Changing the device type or device version in the library

To change the device type or the device version of a device in the project library, follow these steps:

1. Search for the outdated device in the master copies of the project library.
2. Copy the master copy from the project library to the project tree.
3. Make a note of the name of the master copy. Delete the master copy in the project library.
4. Select the "Change device/version" command in the shortcut menu of the outdated device.
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

|  | WinCC V16 | WinCC V17 | WinCC V18 |
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

You can find detailed compatibility lists of all HMI devices using the compatibility tool in Industry Online Support.

---

**See also**

[New external topic](https://support.industry.siemens.com/kompatool/pages/main/index.jsf)

#### Devices not fully supported (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Error during upgrade

If a project contains devices or device versions that are no longer fully supported in the current version of WinCC, the project can be upgraded to the current version of WinCC.

Unsupported devices may be present in a project in the following locations:

- Devices in the project tree

Devices that are no longer fully supported are marked with a special symbol:![Error during upgrade](images/159233723403_DV_resource.Stream@PNG-de-DE.png)

If you compile a device that is no longer complete, you get one of the two error messages:

- The device is not supported. Compilation is therefore not possible. Switch to a supported device.
- The Runtime version is not supported. Compilation is therefore not possible. Switch to a supported version.

##### Changing the device type or the device version in the project tree

To change the device type or the device version of a device in the project tree, follow these steps:

1. Select the "Change device/version" command in the shortcut menu of the outdated device.
2. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.

##### Devices and device versions not fully supported

|  | WinCC V16 | WinCC V17 | WinCC V18 |
| --- | --- | --- | --- |
| KTP400 Basic 2nd Generation |  |  | 15.0.0.0 |
| KTP700 Basic 2nd Generation |  |  | 15.0.0.0 |
| KTP900 Basic 2nd Generation |  |  | 15.0.0.0 |
| KTP1200 Basic 2nd Generation |  |  | 15.0.0.0 |
| KTP400F Mobile |  |  | 15.0.0.0 |
| KTP700 Mobile |  |  | 15.0.0.0 |
| KTP700F Mobile |  |  | 15.0.0.0 |
| KTP900 Mobile |  |  | 15.0.0.0 |
| KTP900F Mobile |  |  | 15.0.0.0 |
| Mobile Panel 177 |  |  |  |
| Mobile Panel 277 |  |  |  |
| KP400 Comfort |  |  | 15.0.0.0 |
| KP700 Comfort |  |  | 15.0.0.0 |
| KP900 Comfort |  |  | 15.0.0.0 |
| KP1200 Comfort |  |  | 15.0.0.0 |
| KP1500 Comfort |  |  | 15.0.0.0 |
| KP1500 Comfort V2 |  |  | 15.0.0.0 |
| KTP400 Comfort |  |  | 15.0.0.0 |
| TP700 Comfort |  |  | 15.0.0.0 |
| TP700 Comfort INOX PCT |  |  |  |
| TP700 Comfort Outdoor |  |  | 15.0.0.0 |
| TP900 Comfort |  |  | 15.0.0.0 |
| TP900 Comfort INOX PCT |  |  | 15.0.0.0 |
| TP1200 Comfort |  |  | 15.0.0.0 |
| TP1200 Comfort INOX PCT |  |  | 15.0.0.0 |
| TP1200 Comfort PRO |  |  | 15.0.0.0 |
| TP1500 Comfort |  |  | 15.0.0.0 |
| TP1500 Comfort Outdoor |  |  | 15.0.0.0 |
| TP1500 Comfort V2 |  |  | 15.0.0.0 |
| TP1900 Comfort PRO |  |  | 15.0.0.0 |
| TP2200 Comfort |  |  | 15.0.0.0 |
| TP2200 Comfort V2 |  |  | 15.0.0.0 |
| WinCC Runtime Advanced |  |  | 15.0.0.0 |

You can find detailed compatibility lists of all HMI devices using the compatibility tool in Industry Online Support.

## Managing colors centrally (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basic principles for color management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-for-color-management-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Finding and replacing colors (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#finding-and-replacing-colors-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basic principles for color management (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

WinCC provides the option of changing the colors used in a project centrally. The "Change color reference" dialog box contains a hierarchical overview of all color-relevant properties contained in the selected object. In the display, you can navigate within the display and operating objects that are shown and thus get an overview of all colors used. Using search and filter you can specify a color selection and replace it with other colors, if necessary.

#### Supported objects

You have access to all colors used and configured in the project with the "Change color reference" dialog. Excluded from this are colors that are used as follows:

- In types and instances from a library
- In faceplates
- In scripts
- In designs
- In screens with write protection

### Finding and replacing colors (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The scope of the objects displayed in the "Change color references" dialog depends on the location at which the dialog is called.

- If you select an HMI device and call the dialog, all color references used on the HMI device are displayed.
- If you select a display object within a screen and call the dialog, only those color references that are included in the display object are displayed.

#### Requirement

- You have created a project.
- Screens have been created.

#### Procedure

1. Select the object that contains the required color references.
2. Select "Change object color" in the shortcut menu.

   A dialog opens.
3. Select the color that you want to change.

   - Click the color field in the search box.

     The project color selection opens.
   - To select a standard color or a user-defined color, click "More colors".
   - To use a color directly from the selected object, drag a color field from the overview table to the search box.
   - To select similar colors as well, set a tolerance.

     ![Procedure](images/80024925195_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/80024925195_DV_resource.Stream@PNG-en-US.png)
4. Filter the displayed table.
5. In the table column "Replace with" select the new color for the individual properties.
6. Click "OK".

#### Result

The new color references are configured in the selected object.

## Load files using the "HMI files" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Introduction

You upload files of any data format from your computer to your project using the "HMI files" editor. These files are transferred to the PC during "Download to device". This way you link useful additional information such as system manuals, video tutorials, etc. with the respective project or distribute them to different devices. If required, you overwrite the downloaded files at any time with current files or delete them from the project.

Create folders to design a clear work area in the "HMI files" editor. Then you save the files in the folders.

If you modify these files or folders on your computer, the changes also appear in the "HMI files" editor.

> **Note**
>
> The "HMI files" editor is only visible in the project tree when a device is created with Runtime Professional in the project.

### Requirements

The files that you want to download to the project are located on your computer.

### Downloading files

1. Double-click "Common data" in the project tree.
2. Double-click the "HMI files" editor.

   The editor opens.

   ![Downloading files](images/68241635979_DV_resource.Stream@PNG-en-US.png)

   ![Downloading files](images/68241635979_DV_resource.Stream@PNG-en-US.png)
3. Click "Add new" in the work area.

   The Windows Explorer opens.
4. Navigate to the directory in which the files are stored that you want to download to the project.
5. Select one or more files.
6. Click "Open".

   The files appear in the work area numbered in alphabetical order and are saved under "&lt;TIAProjectname&gt;\UserFiles\HMI_globalFiles".

You can also open the Windows Explorer using the "Open in Windows Explorer" button and move the required files from the Windows Explorer into the work area with drag&amp;drop.

> **Note**
>
> To go directly to the storage folder "&lt;TIAProjectname&gt;\UserFiles\HMI_globalFiles", click on the button "Open in Windows Explorer".

### Overwriting files

You overwrite files by downloading files with the same name into the project folder.

1. You download files as described under "Downloading files".
2. Confirm the prompt with "Yes" for the files to be overwritten.

### Deleting files

1. Select the line of the file to be deleted in the work area.
2. Select "Delete" from the shortcut menu.

> **Note**
>
> You delete multiple files by selecting several lines and executing the "Delete" command from the shortcut menu.

### Creating folders

You must first create folders and then fill them with files.

1. Select an empty line in the work area.
2. Select "Create new folder" from the shortcut menu.

   The "Create new folder" dialog opens.
3. Enter a name for the folder.
4. Click "OK" to confirm your input.

   The folder appears in the work area.

> **Note**
>
> You create subfolders by selecting the line with the respective folder and executing the command "Create new folder" from the shortcut menu.

### Saving files in folders

1. In the work area, select a folder that you want to fill with files.
2. Select "Insert object" from the shortcut menu.

   The Windows Explorer opens.
3. You download files as described under "Downloading files".

   The files are stored in the folder.

### Result

The files and folders as well as their changes are transferred to all devices in the project after the following actions:

- Compilation of the project
- Downloading the project
- Starting runtime
- Starting the simulation

The contents of the "&lt;TIAProjectname&gt;\UserFiles\HMI_globalFiles" folder is mirrored under "&lt;RTProject&gt;\AdditionalFiles".

> **Note**
>
> When a file is being used in runtime, this file is not overwritten in the "&lt;RTProject&gt;\AdditionalFiles" folder. A warning informs you about it.

---

**See also**

[Overview of compiling and loading projects (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-compiling-and-loading-projects-rt-professional)

## Exchanging controller data from other projects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Inter-project engineering

You can use the IPE (Inter Project Engineering) function to read in controller data from other TIA Portal projects and use it for configuring.

IPE enables you to transfer and merge the HMI configuration and PLC programming communication into various TIA Portal projects.

![Inter-project engineering](images/57962891915_DV_resource.Stream@PNG-en-US.png)

You can find more information and notes on configuration under: Basics of Inter Project Engineering (IPE)

## Recognizing the project status by the SIMATIC WinCC RT symbol (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Introduction

WinCC displays the "SIMATIC WinCC RT" symbol in the notification area of the taskbar. This symbol provides information about the Runtime status.

### Project status

The following table shows which project status goes with which symbol:

| Symbol | Status |
| --- | --- |
| ![Project status](images/104836504459_DV_resource.Stream@PNG-de-DE.png) | WinCC runtime is started. |
| ![Project status](images/104863330827_DV_resource.Stream@PNG-de-DE.png) | WinCC Runtime is not active.  No Runtime project is open. |
| ![Project status](images/104863595659_DV_resource.Stream@PNG-de-DE.png) | WinCC Runtime is active. |
| ![Project status](images/104863604491_DV_resource.Stream@PNG-de-DE.png) | WinCC Runtime is active and the server has the "Fault" status. |
| ![Project status](images/104863805323_DV_resource.Stream@PNG-de-DE.png) | WinCC changes the status. |
| ![Project status](images/104863916555_DV_resource.Stream@PNG-de-DE.png) | WinCC opens a Runtime project. |
| ![Project status](images/104863925387_DV_resource.Stream@PNG-de-DE.png) | WinCC activates a Runtime project. |
| ![Project status](images/104863985419_DV_resource.Stream@PNG-de-DE.png) | WinCC deactivates a Runtime project. |
| ![Project status](images/104864096651_DV_resource.Stream@PNG-de-DE.png) | WinCC closes a Runtime project. |

### Control Options via the Pop-up Menu

You can operate an open Runtime project depending on its status. You have the following operating options from the shortcut menu of the "SIMATIC WinCC RT" symbol:

- Enable Runtime / Disable Runtime
- Exit Graphics Runtime / Start Graphics Runtime
- Open diagnostics window
- Runtime start options
- WinCC license analysis

When you click on the "SIMATIC WinCC RT" symbol, you can see the current project status and, in the case of a redundant project, the status of the partner server or client.
