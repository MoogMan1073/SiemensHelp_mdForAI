---
title: "Using libraries"
package: PELibraryenUS
topics: 97
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using libraries

This section contains information on the following topics:

- [Library basics](#library-basics)
- [Using libraries in different TIA products](#using-libraries-in-different-tia-products)
- [Using the "Libraries" task card](#using-the-libraries-task-card)
- [Using library management](#using-library-management)
- [Using global libraries](#using-global-libraries)
- [Using master copies](#using-master-copies)
- [Using types and their versions](#using-types-and-their-versions)
- [Updating library with the types of another library](#updating-library-with-the-types-of-another-library)
- [Multiuser Engineering in libraries](#multiuser-engineering-in-libraries)
- [Using library texts](#using-library-texts)
- [Comparing libraries and library elements](#comparing-libraries-and-library-elements)
- [Filtering the display of library elements](#filtering-the-display-of-library-elements)
- [Creating folders in a library](#creating-folders-in-a-library)
- [Editing library elements](#editing-library-elements)
- [Harmonizing names and path structure](#harmonizing-names-and-path-structure)
- [Clean up library](#clean-up-library)

## Library basics

### Introduction

You can store library elements you want to reuse in libraries. For each project there is a project library that is connected to the project. In addition to the project library, you can create any number of global libraries that can be used over several projects. Since the libraries are compatible with each other, library elements can be copied and moved from one library to another. Libraries are used, for example, to create templates for blocks that you first paste into the project library and then further develop there. Finally, you copy the blocks from the project library to a global library. You make the global libraries available to other employees working on your project. The other employees continue to use the blocks and adapt them to their individual requirements as needed.

Both the project library and global libraries distinguish between two different types of library elements:

- Types

  Objects that are required to run user programs, for example, blocks, PLC data types (UDT), user-defined data types or faceplates are suitable as types. Types can be versioned and therefore support professional further development. Projects using the types can be updated as soon as new versions of the types are available.
- Master copies

  Almost every object can be saved as a master copy and pasted into the project again later. You can, for example, save entire devices with their contents or cover sheets for plant documentation as master copies.

### Project library

Each project has its own library, the project library. In the project library, you store the objects you want to use more than once in the project. The project library is always opened, saved, and closed together with the current project.

### Global libraries

In addition to the project library, you use global libraries if you want to use libraries over several projects. Global libraries exist in three versions:

- System libraries

  Siemens supplies global libraries for its own software products. These include off-the-peg functions and function blocks that you can use within your project. The supplied libraries cannot be changed. The supplied libraries are loaded automatically matching the project.
- Corporate libraries

  Corporate libraries are made available centrally by your organization, for example, in a central folder on a network drive. The TIA Portal manages the corporate libraries automatically. As soon as a more recent version of an existing corporate library becomes available, you receive a prompt to update the corresponding corporate library to the more recent version.
- User libraries

  Global user libraries are independent of a specific project and can therefore be passed on to other users. Shared access to global user libraries is also possible, for example on a network drive, if all users open the global user library with write protection.

  Global user libraries from older versions of the TIA Portal that you created yourself can still be used. To continue using global user libraries from older versions of the TIA Portal, they must first be upgraded.

### Comparing library elements

You can compare blocks and PLC data types (UDT) with the objects of a device. This allows you to determine, for example, whether certain blocks or PLC data types (UDT) have been used in a project and whether they have been modified.

---

**See also**

[Overview of the "Libraries" task card](#overview-of-the-libraries-task-card)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Basics on master copies](#basics-on-master-copies)
  
[Basics on types](#basics-on-types)

## Using libraries in different TIA products

### Description

You can use different TIA products (e.g. STEP 7 Professional, Safety, WinCC Advanced, etc.) within a TIA Portal version (e.g. V19). You can also open projects with project libraries and global libraries that you have created with one TIA product with a different TIA product at any time. However, the library elements can only be edited and used in the project if they are supported in the current project and when all necessary licenses and support packages are available. You cannot, for example, edit STL program blocks, with STEP 7 Basic.

If a master copy or a type or its versions are not supported, the block icon in the library and in the project tree is also marked with the ![Description](images/95915010955_DV_resource.Stream@PNG-de-DE.png) icon for library elements that are not supported.

If a master copy or a type is marked as unsupported, the following functions are then available to you:

- rename
- delete
- move within the library
- copy to a different library, as long as this library also supports the library element

Even if a type is marked as unsupported, the following functions are also available to you:

- The "Go to type" function
- The library management
- "Clean up library" function
- Upgrade library as long as it does not contain a type version that is not supported
- Assign type version as long as it does not contain a type version that is not supported

### Example

The example below shows you what it looks like when you open a project library from a more comprehensive product in a less comprehensive product:

![Example](images/114946204939_DV_resource.Stream@PNG-en-US.png)

The project library was created with STEP 7 Professional and includes types that are specific to Professional.

When you open the STEP 7 Professional project with STEP 7 Basic you will see a note that the contained libraries cannot be edited without restrictions.

- Representation in the project library:

  ![Example](images/114912345867_DV_resource.Stream@PNG-en-US.png)
- Representation in the project tree:

  ![Example](images/114946101003_DV_resource.Stream@PNG-en-US.png)

All STEP 7 Professional specific types are marked accordingly as not supported and can only be edited with restrictions.

## Using the "Libraries" task card

This section contains information on the following topics:

- [Overview of the "Libraries" task card](#overview-of-the-libraries-task-card)
- [Using the element view](#using-the-element-view)
- [Showing and hiding columns](#showing-and-hiding-columns)

### Overview of the "Libraries" task card

#### Function of the "Libraries" task card

The "Libraries" task card enables you to work efficiently with the project library and the global libraries.

#### Layout of the "Libraries" task card

The "Libraries" task card consists of the following components:

![Layout of the "Libraries" task card](images/154850068235_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar in the "Libraries" task card |
| ② | "Project library" pane |
| ③ | "Global libraries" pane |
| ④ | "Elements" pane |
| ⑤ | "Info" pane |
| ⑥ | Table header |
| ⑦ | Text filter |
| ⑧ | "Types" folder |
| ⑨ | "Master copies" folder |

#### Toolbar in the "Libraries" task card

You can perform the following tasks in the toolbar of the "Libraries" task card:

- Open library management

  Use the "Library management" button to open the library management. The library management is available when a type, a folder that contains types or the "Types" folder of a library is selected.

  See also: [Using library management](#using-library-management)
- Clean up library

  By cleaning up a library, you delete all types and type versions that are not linked to an instance in the project.
- Harmonize project

  By harmonizing a project, you adapt the names and the path structures of type uses in the project to the corresponding names and path structures of the types within a library.

#### "Project library" pane

In the "Project library" pane, you can store the library elements that you want to use more than once in the project.

#### "Global libraries" pane

In the "Global libraries" pane, you manage the global libraries whose library elements you want to reuse over several projects.

The "Global libraries" pane also lists libraries that were shipped together with the products you purchased. These libraries provide you with ready-made functions and function blocks, for example. The supplied global libraries cannot be edited.

#### "Elements" pane

In this pane, you can display the contents of folders in the library. The "Elements" pane is not displayed by default. If you want to display the "Elements" pane, you have to enable it first. Three view modes are available in the "Elements" pane:

- Details mode

  The properties of folders, master copies and types are shown in table form in details mode.
- List mode

  In list mode, the contents of folders are listed.
- Overview mode

  In overview mode, the contents of folders are displayed with large symbols.

See also: [Using the element view](#using-the-element-view)

#### "Info" pane

You can display the contents of the library elements in the "Info" pane. The individual versions of types and the last revision date of the version are also displayed.

#### Text filter

You can use the text filter to filter the display of library elements by text characteristics by entering text. The text filter records types and master copies and the library elements below them in the hierarchy.

See also: [Filtering the display of library elements](#filtering-the-display-of-library-elements)

#### "Types" folder

In the "Types" directories, you can manage types and type versions of library elements that you use as instances in the project.

See also: [Using types](#basics-on-types)

#### "Master copies" folder

In the "Master copies" directories, you can manage master copies of library elements that you can use as copies in the project.

See also: [Using master copies](#basics-on-master-copies)

### Using the element view

#### Introduction

When you open the "Libraries" task card the first time, the "Project library" and "Global libraries" palettes are opened and the "Info" palette is closed. You can display the "Elements" palette if needed.

The elements view shows the elements of the selected library. Three view modes are available in the elements view:

- Details

  The properties of folders, master copies and types are shown in table form in details mode.
- List

  In list mode, the contents of folders are listed.
- Overview

  In overview mode, the contents of folders are displayed with large symbols.

The "Info" palette shows the contents of the selected library element. If you select a type in the elements view, for example, the type versions are displayed in the "Info" palette.

#### Requirement

The "Libraries" task card is displayed.

#### Procedure

To use the element view, follow these steps:

1. Click "Open or close the element view" in the "Project library" or "Global libraries" pane.
2. To change the view mode from the details view to the list mode or overview mode, click the corresponding icon on the toolbar.

---

**See also**

[Library basics](#library-basics)
  
[Overview of the "Libraries" task card](#overview-of-the-libraries-task-card)
  
[Comparing devices and library elements in the compare editor](#comparing-devices-and-library-elements-in-the-compare-editor)
  

  
[Using global libraries](#using-global-libraries)

### Showing and hiding columns

You can show or hide additional columns in the project library or in the global libraries, if necessary. In the additional columns, you see, for example, the version number of the type belonging to an instance.

#### Procedure

To show or hide columns in the project library or in global libraries, follow these steps:

1. Right-click the table header in the library.
2. Select the "Show/Hide" command in the shortcut menu, and select the columns you want to display.

   Alternatively, clear the columns you want to hide.

   The selected columns are displayed or hidden.

## Using library management

This section contains information on the following topics:

- [Overview of the library management](#overview-of-the-library-management)
- [Opening library management](#opening-library-management)
- [Displaying instances in the project](#displaying-instances-in-the-project)
- [Displaying cross references of an instance](#displaying-cross-references-of-an-instance)
- [Displaying relations to other library objects](#displaying-relations-to-other-library-objects)

### Overview of the library management

#### Function of the library management

Master copies and types with dependencies to other library elements are subject to some functional restrictions. They cannot be deleted, for example, as long as dependencies still exist. This prevents other library elements from becoming useless. The library management is used to identify the dependencies and to create an overview of the work progress.

The library management offers the following functions:

- Display of the correlations of types and master copies

  If a type is referenced in other types or master copies, the correlations are displayed in the library management. You will also be able to see which library elements reference a type or a master copy.
- Display of points of use of types in the project
- Upgrading types
- Using filters to narrow down the displayed types

#### Layout of the library management

The following figure shows the components of the library management:

![Layout of the library management](images/155488765579_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar of the library management |
| ② | "Use in the project" tab |
| ③ | "Use in the library" tab |
| ④ | "Types" area |
| ⑤ | "Uses" window |
| ⑥ | Text filter |

#### Toolbar of the library management

You can perform the following tasks in the toolbar of the library management:

- Update uses

  If the project was changed, you can update the view of the library management.
- Clean up library

  By cleaning up a library, you delete all types and type versions that are not linked to an instance in the project.
- Harmonize project

  By harmonizing a project, you adapt the names and the path structures of type uses in the project to the corresponding names and path structures of the types within a library.
- Collapse all

  Hides all subentries of the uppermost node in the "Types" area. The lower-level elements, such as types and individual type versions, are no longer displayed.
- Expand all

  Expands all lower-level elements in the "Types" area. The lower-level elements, such as types and type versions, are displayed in full.

#### "Use in the project" tab

The "Use in the project" tab is used to show the instances of type versions and their respective point of use in the project. When you select an instance, you can show the cross references of the instance in the project in the Inspector window.

You can find additional information here:

[Displaying cross references of an instance](#displaying-cross-references-of-an-instance)

[Displaying instances in the project](#displaying-instances-in-the-project)

#### "Use in the library" tab

The "Use in the library" tab is used to show all points within the library at which a type or a master copy is used.

You can find additional information here: [Displaying relations to other library objects](#displaying-relations-to-other-library-objects)

#### "Types" area

The "Types" area displays the contents of the folder that you have selected in the "Libraries" task card. For each type, the types that it references are displayed. You can expand or collapse all type nodes by using the buttons in the toolbar of the "Types" area.

You can also filter the view with the "Filter" drop-down list. You can find more information on the individual filter settings here: [Filtering the display of library elements](#filtering-the-display-of-library-elements).

#### Text filter

You can use the text filter to filter the display of library elements by text characteristics by entering text. The text filter records types and master copies and the library elements below them in the hierarchy.

You can find additional information here: [Filtering the display of library elements](#filtering-the-display-of-library-elements)

---

**See also**

[Opening library management](#opening-library-management)

### Opening library management

#### Procedure

To open the library management, follow these steps:

1. Select a type or any folder that contains types.
2. Select the "Library management" command from the shortcut menu.

Or:

1. Click the "Types" folder in the project library or a global library.
2. Select the "Library management" command from the shortcut menu.

#### Result

The library management opens and the types are displayed with their versions.

---

**See also**

[Overview of the library management](#overview-of-the-library-management)

### Displaying instances in the project

In the library management, you can have the instances of all versions of a type or an individual type version displayed. You can jump directly to each instance in the project.

#### Requirement

The library management is open.

#### Procedure

To display the instances of a type or its versions, follow these steps:

1. In the "Types" area select the required folders, types or versions.
2. Open the "Use in the project" tab.

   The instances in the project are displayed for each type version. The "Path" column shows the path at which the respective instance is located in the project.
3. Click the path to jump directly to the respective instance in the project tree.

   The library management is hidden and the instance is selected in the project tree.

---

**See also**

[Displaying cross references of an instance](#displaying-cross-references-of-an-instance)
  
[Using types of the project library](#using-types-of-the-project-library)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Displaying relations to other library objects](#displaying-relations-to-other-library-objects)

### Displaying cross references of an instance

You can display the cross references of an instance without exiting the library management.

#### Requirement

The library management is open.

#### Procedure

To display the cross references of an instance in the project, follow these steps:

1. In the "Types" area, select a type version whose instances you want to display.
2. Select the instance of the required type version in the "Uses in the project" tab.
3. Open the "Info > Cross-references" tab in the inspector window.

   The cross reference of the instance are displayed in the project.

---

**See also**

[Using cross-references](Editing%20project%20data.md#using-cross-references-1)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Displaying instances in the project](#displaying-instances-in-the-project)

### Displaying relations to other library objects

You can display relations between individual library objects in the library management. The references of the individual type versions to the other library objects are automatically displayed in the "Types" area. In the "Uses in the library" tab, you can also view the other library objects in which the respective type version is referenced.

#### Requirement

The library management is open.

#### Procedure

To display the other library objects from which a type version is referenced, follow these steps:

1. In the "Types" area select the required folders, types or versions.
2. Open the "Uses in the library" tab.

   In the "Uses" window, you can now see which other library objects are referenced by the individual type versions.
3. To jump to the referenced library object, click on the respective path in the "Path" column.

---

**See also**

[Displaying instances in the project](#displaying-instances-in-the-project)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Referencing of objects within a block](#referencing-of-objects-within-a-block)

## Using global libraries

This section contains information on the following topics:

- [Creating a global library](#creating-a-global-library)
- [Create write-protected global library](#create-write-protected-global-library)
- [Compatibility of global libraries](#compatibility-of-global-libraries)
- [Opening a global library](#opening-a-global-library)
- [Defining library languages](#defining-library-languages)
- [Displaying properties of global libraries](#displaying-properties-of-global-libraries)
- [Displaying logs of global libraries](#displaying-logs-of-global-libraries)
- [Saving a global library](#saving-a-global-library)
- [Closing a global library](#closing-a-global-library)
- [Deleting a global library](#deleting-a-global-library)
- [Archiving and retrieving global libraries](#archiving-and-retrieving-global-libraries)
- [Using global corporate libraries](#using-global-corporate-libraries)
- [Using Multiuser Engineering for global libraries](#using-multiuser-engineering-for-global-libraries)

### Creating a global library

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To create a new global library, follow these steps:

1. Click the "Create new global library" icon in the toolbar of the "Global libraries" palette or select the command "Global libraries > Create new library" in the "Options" menu.

   The "Create new global library" dialog opens.
2. Specify the name and the storage location for the new global library.
3. Confirm your entries with "Create".

#### Result

The new global library is generated and pasted into the "Global libraries" palette. A folder with the name of the global library is created in the file system at the storage location of the global library. The actual library file is given the file name extension ".al19".

---

**See also**

[Library basics](#library-basics)
  
[Opening a global library](#opening-a-global-library)
  
[Displaying properties of global libraries](#displaying-properties-of-global-libraries)
  
[Saving a global library](#saving-a-global-library)
  
[Closing a global library](#closing-a-global-library)
  
[Deleting a global library](#deleting-a-global-library)

### Create write-protected global library

You can protect global libraries by exporting them as protected libraries. These libraries are then provided with a write protection. This means the types contained in them and the global libraries are also then protected against changes. Write protection of protected global libraries cannot be revoked.

#### Requirements

- The "Libraries" task card is opened.
- A global library that is not write-protected exists.

#### Procedure

Follow these steps to create a write-protected global library:

1. Select the global library from which you want to create a write-protected global library.
2. Right-click to call up the shortcut menu.
3. Select the command "Export as protected library" in the shortcut menu of the global library.

   The "Export as protected library" dialog is opened.
4. Specify the name and the storage location for the write-protected global library.
5. Confirm your entries with "Export".

#### Result

The write-protected global library is generated and pasted into the "Global libraries" palette. A folder with the name you assigned to the protected global library is created at the location of the global library in the file system. The actual library file is given the file name extension ".al19".

The types and the master copies from the original global library are copied as write-protected types and master copies to the new global library.

> **Note**
>
> **Preventing changes in write-protected types**
>
> Write-protected types can possibly be changed when they are overwritten by more up-to-date, non-write-protected versions of the same type.
>
> Therefore, if you want to supply write-protected types to customers, create write-protected libraries with types in a newer version if possible before supplying them.
>
> This ensures that the customer does not already use write-protected versions of this type and cannot make changes.

### Compatibility of global libraries

#### Libraries from TIA Portal V13 or earlier

Global libraries that were created with TIA Portal V13 or earlier cannot be used in the current version of TIA Portal. First, upgrade the libraries with version V13 SP1 of TIA Portal to the current library version. You can then open the library and upgrade once again.

#### Libraries from TIA Portal V13 SP1 or later

You can use TIA Portal to open global libraries that were created with TIA Portal V13 SP1 or higher. When you open the library, you are prompted to upgrade the library to the current version of TIA Portal. Once the global library is upgraded, it cannot be opened with earlier versions of TIA Portal.

#### Backward compatibility of the current library version

Global libraries saved with the library format of the current TIA Portal product version are not backward compatible with older versions due to their enhanced functionality. Global libraries in the current library format can only be used in connection with TIA Portal V19 projects.

---

**See also**

[Using projects created with optional software](Editing%20projects.md#using-projects-created-with-optional-software)
  
[Opening a global library](#opening-a-global-library)
  
[Upgrading projects](Editing%20projects.md#upgrading-projects-1)
  
[General information on upgrading projects](Editing%20projects.md#general-information-on-upgrading-projects)

### Opening a global library

Global libraries can be further developed centrally and used over several projects. Several persons can open a global library simultaneously from a central storage location, provided all users open the global library in write-protected mode.

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To open a global library, follow these steps:

1. Click the "Open global library" icon in the toolbar of the "Global libraries" pane or select the command "Global libraries > Open library" in the "Options" menu.

   The "Open global library" dialog box opens.
2. Select the global library you want to open. Library files are identified by the file name extension ".al[version number]". This means that global libraries that were saved with the current TIA Portal product version have the file name extension ".al19".
3. Write protection is activated for the library. If you want to modify the global library, clear the option "Open as read-only".
4. Click "Open".

   If the library is saved in the library version for TIA Portal V19, the Global library is opened and pasted into the "Global libraries" palette. The "Upgrade global library" dialog opens if you have selected a global library from TIA Portal V13 SP1 or later. Upgrade the library to the current version of TIA Portal in this case.

#### Result

The global library is displayed in the "Global libraries" palette.

If the global library was opened write-protected, it and all its subfolders are grayed out.

---

**See also**

[Retrieving global libraries](#retrieving-global-libraries)
  
[Opening projects](Editing%20projects.md#opening-projects)
  
[Compatibility of global libraries](#compatibility-of-global-libraries)
  
[Library basics](#library-basics)
  
[Creating a global library](#creating-a-global-library)
  
[Displaying properties of global libraries](#displaying-properties-of-global-libraries)
  
[Saving a global library](#saving-a-global-library)
  
[Closing a global library](#closing-a-global-library)
  
[Deleting a global library](#deleting-a-global-library)

### Defining library languages

You can define various library languages for global libraries and select an editing language for all comments from them. The selection of the library languages is valid for all library elements (types, type versions and master copies) within the global library.

The comments of the types and their type versions can be translated into multiple library languages and managed in the global library. The selected editing language specifies the languages in which the comments are displayed. The comments of a type can be edited at any time. As soon as the version of a type is released, it comments can no longer be edited and are displayed in ready-only mode.

If you change the editing language of a global library, the comments of all types are displayed in the newly selected editing language, provided translations are available.

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To define the library languages of a global library, follow these steps:

1. Click the "Open global library" icon in the toolbar of the "Global libraries" pane or select the command "Global libraries > Open library" in the "Options" menu.

   The "Open global library" dialog box opens.
2. Select the global library you want to open.
3. Disable the write protection of the global library by clearing the option "Open as read-only".

   If you do not clear the "Open as read-only" option, you can see the selection of library languages in the global library, but you cannot change them.
4. Click "Open".

   The global library is displayed.
5. Open the "Languages & Resources" folder.
6. Double-click the "Library languages" entry or select "Open" from the shortcut menu.

#### Result

The library languages are displayed in the working area of the library.

### Displaying properties of global libraries

Global libraries contain properties for describing the respective library in more detail. Properties include the following:

- General information about the library

  This includes the following information: creation time, author, file path, file size, copyright, etc. Many of the attributes can be changed.
- Library history

  The library history contains an overview of the migrations performed. Here you can also call the log file for the migrations. The library history also contains information on updates of the global library.
- Support packages in the library

  You can display an overview of additional software. The additional software is needed to process all devices of the project.
- Software products in the library

  You can display an overview of all installed software products needed for the project.

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To display the properties of a global library, follow these steps:

1. Right-click the global library whose properties you want to display.
2. Select the "Properties" command in the shortcut menu.

   A dialog containing the properties of the global libraries opens.
3. Select the properties in the area navigation that you want to have displayed.

---

**See also**

[Opening a global library](#opening-a-global-library)
  
[Library basics](#library-basics)
  
[Creating a global library](#creating-a-global-library)
  
[Saving a global library](#saving-a-global-library)
  
[Closing a global library](#closing-a-global-library)
  
[Deleting a global library](#deleting-a-global-library)

### Displaying logs of global libraries

Logs are created when you update or clean up global libraries or assign a shared version to several types. The logs list all changes you have made to the global library. The logs are created in ZIP-files and are stored together with the global library. They are always available once you have opened the global library.

#### Procedure

To open the logs of a global library, follow these steps:

1. Open the global library in the "Libraries" task card.
2. Open "Common data > Logs" in the lower-level folder.
3. Double-click the required log.

   The log opens in the work area.

---

**See also**

[Updating library with the types of another library](#updating-library-with-the-types-of-another-library)

### Saving a global library

After you have changed a global library, you need to save it. You can save a global library under another name using the "Save library as" command.

> **Note**
>
> **Backward compatibility with older versions of the TIA Portal**
>
> Note that global libraries can no longer be opened in older versions of the TIA Portal once they have been saved in the current version.

#### Requirement

The "Libraries" task card is opened.

#### Saving changes

To save a global library, follow these steps:

1. Right-click on the global library you want to save.
2. Select the "Save library" command in the shortcut menu.

#### Saving a global library under another name

To save a global library under another name, follow these steps:

1. Right-click the global library that you want to save under a different name.
2. Select the "Save library as" command in the shortcut menu.

   The "Save global library as" dialog opens.
3. Select the storage location and enter the file name.
4. Confirm your entries with "Save".

   The library is saved in the specified location under the new name. The original library is retained.

---

**See also**

[Working with archives of global libraries](#working-with-archives-of-global-libraries)
  
[Archiving global libraries](#archiving-global-libraries)
  
[Library basics](#library-basics)
  
[Creating a global library](#creating-a-global-library)
  
[Opening a global library](#opening-a-global-library)
  
[Displaying properties of global libraries](#displaying-properties-of-global-libraries)
  
[Closing a global library](#closing-a-global-library)
  
[Deleting a global library](#deleting-a-global-library)

### Closing a global library

Global libraries are independent of projects. This means that global libraries are not closed together with your project. You must therefore close global libraries explicitly.

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To close a global library, follow these steps:

1. Right-click on the global library you want to close.
2. Select the "Close library" command in the shortcut menu.

   If you have made changes to the global library, select whether or not you want to save the changes.

   The global library is closed.

---

**See also**

[Creating a global library](#creating-a-global-library)
  
[Opening a global library](#opening-a-global-library)
  
[Displaying properties of global libraries](#displaying-properties-of-global-libraries)
  
[Saving a global library](#saving-a-global-library)
  
[Library basics](#library-basics)
  
[Deleting a global library](#deleting-a-global-library)

### Deleting a global library

If you no longer require a global library, you can delete it. Libraries supplied by Siemens cannot be deleted.

#### Requirement

The "Libraries" task card is opened.

#### Procedure

To delete a global library, follow these steps:

1. Right-click the global library you want to delete.
2. Select the "Delete" command in the shortcut menu.
3. Click "Yes" to confirm.

#### Result

The global library is removed from the "Global libraries" palette. The entire library for the global library is deleted from the file system.

---

**See also**

[Library basics](#library-basics)
  
[Creating a global library](#creating-a-global-library)
  
[Opening a global library](#opening-a-global-library)
  
[Displaying properties of global libraries](#displaying-properties-of-global-libraries)
  
[Saving a global library](#saving-a-global-library)
  
[Closing a global library](#closing-a-global-library)

### Archiving and retrieving global libraries

This section contains information on the following topics:

- [Working with archives of global libraries](#working-with-archives-of-global-libraries)
- [Archiving global libraries](#archiving-global-libraries)
- [Retrieving global libraries](#retrieving-global-libraries)

#### Working with archives of global libraries

If you want to back up global libraries on an external hard drive or send them via e-mail, for example, use the archiving function to reduce the storage space of the library.

##### Options for reducing the size of the project

There are two ways to reduce the space required to store global libraries:

- Creating a compressed archive of global libraries

  Archives of global libraries are compressed files, each containing an entire global library, including the entire folder structure of the library. Before the directory with the global library is compressed into the archive file, all files are reduced to their essential components to further decrease the storage space. Compressed archives of global libraries are therefore well suited for sending via e-mail.

  Compressed archives of global libraries of the current product version have the file extension ".zal19".

  To open a compressed archive of a global library, retrieve the archive. The archive file is extracted to a location you have selected with the entire folder structure and all files.
- Minimizing global libraries

  You can skip additional compression in an archive file, and instead create a copy of the global library directory. The included files can be reduced to the essential elements. This minimizes the required storage space. The full functionality of the global library is retained and the global library can be loaded as usual.

  Minimized global libraries are especially well suited for archiving, for example, on an external medium.

---

**See also**

[Archiving global libraries](#archiving-global-libraries)
  
[Retrieving global libraries](#retrieving-global-libraries)
  
[Protection concept for project data](Editing%20project%20data.md#protection-concept-for-project-data)

#### Archiving global libraries

Global libraries can be archived as compressed or uncompressed files. The global libraries to be archived do not have to be open in TIA Portal.

The memory requirements of global libraries can be reduced by archiving the global libraries in compressed files.

##### Procedure

To archive a global library, follow these steps:

1. Select the "Archive ..." command from the "Project" menu.

   Alternatively, select the "Archive library" command from the shortcut menu of the global library you want to archive.

   The "Archive" dialog opens.
2. Select a library file with the extension ".al19" in the "Source path" field.
3. To create a compressed archive file, select the option "Archive as compressed file".
4. If you do not want to archive restorable data, select the "Discard restorable data" option.
5. To add date and time automatically, select the option "Add date and time to the file name".
6. In the "Destination path" box, select the location where you want to save the archive file or the new directory of the global library.

   The directory must not be located in a project directory or within the directory of a global library.

   You can set the default directory under "Options > Settings > General > Archive settings > Storage location for library archives".
7. Click "Archive".

##### Result

An archive is created for the global library. Compressed global libraries get the file extension ".zal19". The file includes the complete directory of the global library. The individual files of the global library are also reduced to the essential components in order to save space.

For uncompressed global libraries, only a copy of the original directory of the global library is created in the desired location.

---

**See also**

[Working with archives of global libraries](#working-with-archives-of-global-libraries)
  
[Retrieving global libraries](#retrieving-global-libraries)

#### Retrieving global libraries

Before you can use an archived global library, you have to retrieve it. The global library is extracted and then opened in the TIA Portal.

##### Procedure

To extract the archive of a global library, follow these steps:

1. Select the "Global libraries > Open library" command in the "Options" menu.

   The "Open global library" dialog box is displayed.
2. Select the "Compressed libraries" entry in the "File type" drop-down list.
3. Select the archive file.
4. Select the check box "Open read-only" if you want to load the global library write-protected.
5. Click "Open".
6. The "Select target directory" dialog box is displayed.
7. Select the target directory to which the archived global library should be extracted.
8. Click "Select folder".

##### Result

The global library is extracted to the selected directory and opened immediately.

---

**See also**

[Working with archives of global libraries](#working-with-archives-of-global-libraries)
  
[Archiving global libraries](#archiving-global-libraries)
  
[Opening a global library](#opening-a-global-library)
  
[Compatibility of global libraries](#compatibility-of-global-libraries)

### Using global corporate libraries

This section contains information on the following topics:

- [Basics of corporate libraries](#basics-of-corporate-libraries)
- [Creating a configuration file for corporate libraries](#creating-a-configuration-file-for-corporate-libraries)

#### Basics of corporate libraries

##### Introduction

Corporate libraries are global libraries made available by an administrator and assigned to TIA Portal. The administrator can assign new libraries or change libraries at any time. New libraries are automatically loaded in TIA Portal following your confirmation. As soon as more recent versions of corporate libraries are available, the existing corporate libraries are automatically updated to the more recent version, also following your confirmation.

The corporate libraries are located just like normal global libraries in the "Global libraries" palette of the "Libraries" task card.

##### Providing corporate libraries

Corporate libraries can be saved in any directory on the hard drive of the computer or on a network drive. To include corporate libraries in TIA Portal, use an XML file. The XML file includes the directories and names of the assigned corporate libraries. The XML file must be saved in the following directory on the hard drive of the computer:

`C:\ProgramData\Siemens\Automation\Portal V19\CorporateSettings\`

The XML file must be named "`CorporateSettings.xml`".

You either copy the configuration file yourself to the corresponding directory or the configuration file is assigned to you through the company network. The valid configuration is automatically applied when TIA Portal is started. When TIA Portal is started, it continuously monitors the directory for configuration files. If the configuration file has changed, you receive a prompt to apply the new configuration. You can reject this prompt twice. You will always receive the next prompt three hours later. You must apply the new configuration at the third prompt. You receive a changed configuration file from the project administrator, for example, if corporate libraries have been added or deleted.

If you access company libraries stored on a network drive, you only need network access to update them. The company libraries that are stored locally are automatically loaded after a restart. If you do not have network access, you can only use locally stored copies of your company libraries.

##### Options as project administrator

You can automatically assign the configuration file or the corporate libraries to the computers of the team members or distribute updates to the team members. This function is not part of TIA Portal and requires a corresponding IT infrastructure in your company. If you want to administer the configuration file centrally, discuss this approach with the IT managers at your company.

The archive function for global libraries can be used to pass corporate libraries to employees of the project team. However, you must retrieve corporate libraries prior to their use in TIA Portal.

The following figure shows an example of how you can distribute corporate libraries to individual employees within your organization:

![Options as project administrator](images/163928418699_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Working with archives of global libraries](#working-with-archives-of-global-libraries)
  
[Archiving global libraries](#archiving-global-libraries)
  
[Retrieving global libraries](#retrieving-global-libraries)

#### Creating a configuration file for corporate libraries

You use a configuration file in XML format to make the corporate libraries available in TIA Portal. The configuration file includes the directories and file names of the libraries to be loaded. The XML file is the same file that you use for user-defined documentation settings.

Below you will learn how you create the XML configuration file and where to save it.

##### Procedure

To provide a configuration file for corporate libraries, follow these steps:

1. Create an XML configuration file with the content listed below. Use the coding "UTF-8".
2. Replace the paths mentioned in the example in the "<CorporateLibraryPaths>" section below with the paths where your libraries are stored.
3. Save the XML file under the name "CorporateSettings.xml".
4. Save the file in the following directory on your computer:

   C:\ProgramData\Siemens\Automation\Portal V19\CorporateSettings\

##### Content of the XML configuration file

The XML configuration file must have the following content:

XML

<?xml version="1.0" encoding="utf-8"?>

<Document>

<Settings.Settings ID="0">

<ObjectList>

<Settings.General ID="1" AggregationName="General">

<!-- Here you find the settings for global company libraries, if available. -->

<!-- Section for corporate libraries -->

    <AttributeList>

     <CorporateLibraryPaths>

     <!-- Example for two entries -->

     <Item>F:\CorporateLibraries\Corporate_Library_1\Corporate_Library_1.al19</Item>     <Item>F:\CorporateLibraries\Corporate_Library_2\CorporateLibraries.al19</Item>

     <!-- Here you enter additional global libraries, if any. -->     </CorporateLibraryPaths>

    </AttributeList>

<!-- Section for corporate libraries ends -->

<ObjectList>

<!-- Section for user-defined documentation -->

     <Settings.UserDocumentation ID="2" AggregationeName="UserDocumentation">

      <!-- In the following section, you specify the values for display of the user-defined documentation. -->

      <AttributeList>

       <!-- Activates or deactivates the display of the access log. -->

       <DisplayLogInformation>

        <Value>true</Value>

       </DisplayLogInformation>

       <!-- Activates or deactivates the search for user-defined documentation in a central directory. -->

       <EnableLookupFromCentralStorageLocation>

        <Value>true</Value>

       </EnableLookupFromCentralStorageLocation>

       <!-- Specifies the central directory for user-defined documentation. -->

       <CentralStorageLocation>

        <Value>D:\CorporateDocumentation\UserDocumentation\</Value>

       </CentralStorageLocation>

      </AttributeList>

     </Settings.UserDocumentation>

<!-- Section for user-defined documentation ends -->

    </ObjectList>

</Settings.General>

</ObjectList>

</Settings.Settings>

</Document>

##### Result

As soon as you have saved the XML configuration file in the respective directory, you will receive a prompt in TIA Portal to load the corporate libraries.

---

**See also**

[Specifying settings with an XML file](Editing%20project%20data.md#specifying-settings-with-an-xml-file)

### Using Multiuser Engineering for global libraries

This section contains information on the following topics:

- [Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
- [Managing the project server](#managing-the-project-server)
- [Starting the server project](#starting-the-server-project)
- [Creating a new server library](#creating-a-new-server-library)
- [Creating a local session](#creating-a-local-session)
- [Opening a local session](#opening-a-local-session)
- [Synchronizing changes with the server library](#synchronizing-changes-with-the-server-library)

#### Managing global libraries in the project server

With Multiuser Engineering in TIA Portal, several users can work together and simultaneously on server libraries and projects. The server libraries and projects are managed on an external TIA project server or the local project server. The various users work independently in local sessions based on the libraries and projects managed by the server. The changes from the local sessions are transferred to the server library or project. Changes from other users are displayed in the local session and can be adopted.

You can find additional information under [Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering).

To work with Multiuser Engineering, you need a project server that manages your server libraries and projects as well as the local sessions. An external TIA project server can be configured and integrated for this. Each version of TIA Portal includes a version-specific local project server with corresponding functionality, which is installed by default.

You can find additional information at [Introduction to the project server](Using%20Multiuser%20Engineering.md#introduction-to-the-project-server) and [Introduction to the local project server](Using%20Multiuser%20Engineering.md#introduction-to-the-local-project-server).

---

**See also**

[Managing the project server](#managing-the-project-server)
  
[Starting the server project](#starting-the-server-project)
  
[Creating a new server library](#creating-a-new-server-library)
  
[Creating a local session](#creating-a-local-session)
  
[Opening a local session](#opening-a-local-session)
  
[Synchronizing changes with the server library](#synchronizing-changes-with-the-server-library)

#### Managing the project server

To use Multiuser Engineering for global libraries, you need a project server that manages your server libraries. You can use the local project server or configure an external TIA project server.

##### Requirements

- The TIA project server is installed, configured and started.
- The "Libraries" task card is opened.

##### Configure the TIA project server

1. Click the ![Configure the TIA project server](images/158199520779_DV_resource.Stream@PNG-de-DE.png) icon (Manage server global libraries) in the toolbar of the "Global libraries" palette.

   The "Manage server global libraries" dialog opens.
2. Click on the "Manage server" button.

   The settings for the project server open.
3. Click in the "Add server connection" cell in the "Connection" area of the table.

   The "Add new project server connection" dialog opens.
4. Enter the data for the new project server connection.

   You can find additional information under [Set network profiles for project server](Using%20Multiuser%20Engineering.md#set-network-profiles-for-project-server).
5. Click the "Add" button.

##### Result

The new project server connection can be selected in the "Manage global libraries in the TIA project server" dialog.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Starting the server project](#starting-the-server-project)

#### Starting the server project

Before you can create a new server library, you need to start a project server. You can use the local project server or an external TIA project server.

##### Requirement

The "Libraries" task card is opened.

##### Starting the server project

1. Click the ![Starting the server project](images/158199520779_DV_resource.Stream@PNG-de-DE.png) icon (Manage server global libraries) in the toolbar of the "Global libraries" palette.

   The "Manage server global libraries" dialog opens.
2. Select a project server in the "Select server" drop-down list.
3. Confirm the "Start TIA project server" or "Start local project server" dialog by clicking "Yes".

##### Result

The project server is started.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Creating a new server library](#creating-a-new-server-library)

#### Creating a new server library

Once you have started the project server, you can select a global library and create a server library.

##### Requirements

- The local project server or an external TIA project server is started.
- The "Libraries" task card is opened.

##### Creating a new server library

1. Click the ![Creating a new server library](images/158199520779_DV_resource.Stream@PNG-de-DE.png) icon (Manage server global libraries) in the toolbar of the "Global libraries" palette.

   The "Manage server global libraries" dialog opens.
2. Click in the "Add global library to server" cell in the "Global server libraries" area of the table.

   Alternatively, open the shortcut menu and select the "Add global library to server" menu command.

   The "Add global library to project server {project server}" dialog opens.
3. In the "Select global library" area, click the "..." button (Add global library to server) in the "Source path" column.
4. Navigate to a global library in your file directory and click "Open".
5. To create a local session, select the "Create local session" check box.
6. Add a comment if needed.
7. Click the "Add" button.

##### Result

The global library is added to the project server.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Creating a local session](#creating-a-local-session)

#### Creating a local session

After you have created a server library, you can create a local session. Local sessions are required to enable multiple users to work on server libraries together and simultaneously in Multiuser Engineering.

##### Requirements

- You have created a server library.
- The "Libraries" task card is opened.

##### Creating a local session

1. Click the ![Creating a local session](images/158199520779_DV_resource.Stream@PNG-de-DE.png) icon (Manage server global libraries) in the toolbar of the "Global libraries" palette.

   The "Manage server global libraries" dialog opens.
2. Expand the server library.

   Alternatively, open the shortcut menu and select the "Create local session" menu command.

   The "Create local session" dialog box opens.
3. Select the type for the local session.

   - The "Contribute Session" setting causes changes to the local session and the server library to be synchronized in both directions.
   - The "Consume Session" setting causes only changes to the server library to be transferred to the local session.

     This setting is not selectable.
4. Enter the details of the local session.

   - Enter the path of the local session by clicking the "..." button and selecting a directory in your file system.
   - Enter the name of the local session.
5. To open the local session after it is created, select the "Open local session" check box.
6. Click the "Create" button.

##### Results

- The local session is created.
- If you select the "Open local session" option, the local session opens immediately and can be used.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Opening a local session](#opening-a-local-session)

#### Opening a local session

Once you have created a local session, you can open and use the local session.

##### Requirements

- You have created a local session.
- The "Libraries" task card is opened.

##### Opening a local session

1. Click the ![Opening a local session](images/158199520779_DV_resource.Stream@PNG-de-DE.png) icon (Manage server global libraries) in the toolbar of the "Global libraries" palette.

   The "Manage server global libraries" dialog opens.
2. Expand the server library.
3. Double-click a local session.

   Alternatively, open the shortcut menu of a local session and select the "Open local session" menu command.

##### Results

- The local session is opened and can be used.

  You can find additional information under [Editing objects in the local session](Using%20Multiuser%20Engineering.md#editing-objects-in-the-local-session).
- The local session is presented in the "Libraries" task card of the "Global Libraries" tab by the library symbol with overlay icon ![Results](images/158552365451_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Synchronizing changes with the server library](#synchronizing-changes-with-the-server-library)

#### Synchronizing changes with the server library

This section contains information on the following topics:

- [Multiuser markings in the user interface](#multiuser-markings-in-the-user-interface)
- [Checking in changes](#checking-in-changes)
- [Refreshing the local session](#refreshing-the-local-session)

##### Multiuser markings in the user interface

In the "Libraries" task card and in the Library Management, multiuser markings are shown in the left-hand column. These multiuser markings flag changes or conflicts of library objects between local sessions and server libraries. An overview of the markings can be found in [Multiuser icons in the user interface](Using%20Multiuser%20Engineering.md#multiuser-icons-in-the-user-interface-1).

Aggregated multiuser markings are shown for local sessions of server libraries, the "Types" and "Copy templates" folders as well as for user folders subordinate to them. These aggregated markings indicate the respective multiuser status of the subordinate library objects with the highest priority. The symbol corresponds to the respective multiuser marking and is supplemented by an overlay icon.

The priority hierarchy is as follows:

1. ![Figure](images/160024682891_DV_resource.Stream@PNG-de-DE.png) (Conflict: At least one object is marked simultaneously in multiple sessions)
2. ![Figure](images/160026253067_DV_resource.Stream@PNG-de-DE.png) (At least one object is marked in the own local session)
3. ![Figure](images/160026376843_DV_resource.Stream@PNG-de-DE.png) (At least one object is marked in a different local session that is part of the same server library)
4. ![Figure](images/160026385419_DV_resource.Stream@PNG-de-DE.png) (There is no object marked)

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Checking in changes](#checking-in-changes)
  
[Refreshing the local session](#refreshing-the-local-session)

##### Checking in changes

Changes in your local session can be transferred to the server library.

###### Requirements

- You have changed library elements in your local session.
- The local session is open.

###### Checking in changes

1. To transfer changes in your local session to the server library, click the ![Checking in changes](images/158202210187_DV_resource.Stream@PNG-de-DE.png) button (Check in selected changes).

   The "Check-in" work area opens.
2. Review the pending changes.
3. To do this, select the "Library objects" node in the upper part of the work area.
4. In the "Library objects" section, expand the local session and the folders below it.
5. In the left column, you can select or deselect objects to check in by clicking the icon.

   - Selected objects are indicated by the ![Checking in changes](images/158209257483_DV_resource.Stream@PNG-de-DE.png) icon.
   - Deselected objects are indicated by the ![Checking in changes](images/158209266059_DV_resource.Stream@PNG-de-DE.png) icon.
6. Click the "Start check-in" button.

   The changes are checked in.

   Once the check-in is successfully completed, the "Check-in" dialog opens.
7. Perform one of the following actions:

   - To overwrite your local session with the server library data, click the "OK" button.
   - To keep your local session, click the "Keep local session" button.

   The dialog closes.

###### Result

The changes of the local session have been checked in to the server library.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Refreshing the local session](#refreshing-the-local-session)

##### Refreshing the local session

Changes made by other users can be displayed and applied in your local session.

###### Requirements

- Library elements in the server library were changed.
- The local session is open.

###### Refreshing the local session

1. To transfer changes in the server library to your local session, click the ![Refreshing the local session](images/158204330763_DV_resource.Stream@PNG-de-DE.png) button (Refresh local session).

   The "Refresh view" work area opens.
2. Click the "Start refresh" button.

   The update is performed.

   A message about the completed update opens.
3. Close the message with "OK".

###### Result

The local session has been updated with the server library changes.

---

**See also**

[Managing global libraries in the project server](#managing-global-libraries-in-the-project-server)
  
[Checking in changes](#checking-in-changes)

## Using master copies

This section contains information on the following topics:

- [Basics on master copies](#basics-on-master-copies)
- [Adding master copies](#adding-master-copies)
- [Using master copies](#using-master-copies-1)

### Basics on master copies

Master copies are used to create standardized copies of frequently used elements. You can create as many elements as needed and insert them into the project based on a master copy. The elements inherit the properties of the master copy.

You store master copies either in the project library or in a global library. Master copies in the project library can only be used within the project. When you create the master copy in a global library, it can be used in different projects.

The following elements can be created as master copies in the library, for example:

- Devices with their device configuration
- Tag tables or individual tags
- Instruction profiles
- Watch tables
- Elements from the documentation settings, for example, cover sheets and frames
- Blocks and groups containing multiple blocks
- PLC data types (UDTs) and groups which contain multiple PLC data types
- Text lists
- Alarm classes
- Technology objects

In many cases, the objects you add as master copy contain additional elements. A CPU, for example, can contain blocks. If the included elements are uses of a type version, the used versions of the types are automatically created in the library. The elements contained therein are then used as an instance and linked to the type.

---

**See also**

[Adding master copies](#adding-master-copies)
  
[Using master copies](#using-master-copies-1)
  
[Basics on types](#basics-on-types)
  
[Filtering the display of library elements](#filtering-the-display-of-library-elements)

### Adding master copies

If you want to use objects multiple times, copy them as master copies in the project library or in a global library. You can choose from the following methods for creating master copies:

- You select one or more elements and create individual master copies from them
- You select multiple elements and create a single master copy from them that contains all selected elements.

#### Requirement

- The "Libraries" task card is displayed.
- If you add a device as a master copy, this device meets the following requirements:

  - The device is compiled and consistent.
  - The device contains no test instance of a type.
- If you add the master copy to a global library, the global library is opened with write permission.

#### Creating master copies from one or more elements

To create a master copy for one or more elements, follow these steps:

1. Open the library in the "Libraries" task card.
2. Select the desired elements.
3. Using a drag-and-drop operation, move the elements to the "Master copies" folder or any subfolder of "Master copies".

Alternative:

1. Select the desired elements.
2. Copy the elements to the clipboard and paste the elements at the required location.

   Each element is pasted in the library as a master copy. A type is created automatically in each case from any objects contained (such as referenced blocks).

#### Creating a single master copy from several elements

To create a single master copy for all elements from multiple elements, follow these steps:

1. Open the library in the "Libraries" task card.
2. Copy to the clipboard the elements that you want to create as master copies.
3. Right-click on the "Master copies" folder or any of its subfolders in the library.
4. In the shortcut menu, select "Paste as a single master copy" command.

Alternative:

1. Select the desired elements.
2. Using a drag-and-drop operation, move the elements to the "Master copies" folder or any subfolder of "Master copies". Meanwhile, keep the <Alt> key pressed.

   The elements are pasted in the library as a single master copy. The single master copy contains all selected elements. A type is created automatically in each case from any objects contained (such as referenced blocks).

> **Note**
>
> **Avoiding complex structures of master copies**
>
> To prevent name conflicts and conflicts regarding the folder structure during subsequent use of master copies, avoid complex master copies. Complex master copies are, for example, master copies that consist of multiple elements and nested folders.

#### Creating master copies from elements in folders or hierarchies

To create a master copy from a folder that contains one or more elements or subfolders, follow these steps:

1. Open the library in the "Libraries" task card.
2. Copy to the clipboard the folder or the hierarchy with the elements that you want to create as master copies.
3. Right-click on the "Master copies" folder or any of its subfolders in the library.
4. Select the "Insert as hierarchy" command from the shortcut menu.

   The folder, with all subordinate elements, including subfolders, is inserted into the library.

Alternative:

1. Select the required folder.
2. Using a drag-and-drop operation, move the elements to the "Master copies" folder or any subfolder of "Master copies". Meanwhile, keep the <Ctrl> and <Shift> keys pressed.

   Unsupported elements or empty folders cannot be inserted as master copy. You receive a message with additional information.

---

**See also**

[Basics on master copies](#basics-on-master-copies)
  
[Using master copies](#using-master-copies-1)
  
[Library basics](#library-basics)
  
[Adding types to the project library](#adding-types-to-the-project-library)

### Using master copies

Master copies are contained either in the project library or in a global library. You can paste one or more master copies in the project at the same time. If you insert multiple master copies at the same time, ensure that all master copies are compatible with the desired point of use.

#### Requirement

The "Libraries" task card is displayed.

#### Procedure

To paste a master copy into the project, follow these steps:

1. In a library, open the "Master copies" folder or any subfolder of "Master copies".
2. Using a drag-and-drop operation, move the desired master copies or complete folders to the point of use.

Or:

1. Open the element view.
2. Using a drag-and-drop operation, move the desired master copies or whole folders from the "Elements" pane to the point of use.

#### Result

A copy of the master copies is inserted. If incompatible master copies were included in a multiple selection, these are omitted and a copy is not created in the project.

---

**See also**

[Basics on master copies](#basics-on-master-copies)
  
[Adding master copies](#adding-master-copies)
  
[Filtering the display of library elements](#filtering-the-display-of-library-elements)
  
[Library basics](#library-basics)
  
[Using the element view](#using-the-element-view)

## Using types and their versions

This section contains information on the following topics:

- [Basics on types](#basics-on-types)
- [State of type versions](#state-of-type-versions)
- [Displaying a released type version](#displaying-a-released-type-version)
- [Displaying properties of a type or version](#displaying-properties-of-a-type-or-version)
- [Consistency status of types](#consistency-status-of-types)
- [Working with types in the project library](#working-with-types-in-the-project-library)
- [Working with types in global libraries](#working-with-types-in-global-libraries)
- [Setting version as "default"](#setting-version-as-default)
- [Assigning a version](#assigning-a-version)

### Basics on types

#### Using types

Types are elements that are required for the execution of user programs. Types can be versioned and further developed from a central location.

The following elements can be stored as type in the project library or the global library:

- Functions (FCs)
- Function blocks (FBs)
- PLC data types (UDTs)
- Faceplates
- Screens
- Styles
- User-defined functions

You can use the same version of a type only once within a CPU. If various versions of a type are available, these can also be used within a CPU. Depending on the number of CPUs used, any number of instances can be derived within a project. The instances are then connected with the version of the type in the library. If you are using types from a global library, the type is also created in the project library. If the type already exists in the project library, missing type versions are added if necessary. The instance is then linked only to the respective type version in the project library.

Types and their instances are marked with a black triangle. The following figure shows an instance, marked with a black triangle, and an ordinary program block:

![Using types](images/52106643211_DV_resource.Stream@PNG-de-DE.png)

#### Basics on versioning of types

Type versioning provides you with the means to develop types centrally and then roll out the most recent version to the individual projects as an update. In this way, error corrections and added functions can be easily integrated into existing projects. If you have created a new version of a global library, you can update existing projects in an automatic process. This minimizes errors and reduces the amount of maintenance work for large automation solutions that contain numerous individual projects.

Versioning allows you to trace the development process of individual types. Before you release a version, you can try it out in a test environment to determine whether changes made to a type integrate smoothly into an existing project. You only release a version for productive use after you have made sure that everything operates without errors. You can view the history of individual instances in the project at any time and determine the version from which the instance was derived.

The TIA Portal also checks automatically whether there are associated objects with individual versions of a type. Associated objects can be, for example, PLC data types (UDTs) or other blocks referenced in a block. All associated objects are already taken into consideration during the creation of a type or during copying between libraries. Before being released, versions of types are checked for their consistency to ensure that no inconsistencies arise in the project.

#### Versions of types

Versions are assigned to each type. The version number is displayed in both the "Libraries" task card as well as the project tree next to the respective type. You can also display the version of a type in the project tree next to the instances. To do this, select the "Version" column in the project tree. This allows you to see at all times which version of an instance is used in the project.

The version number consists of three numbers separated by periods. You can randomly assign the first two digits. Numbers from 1 to 999 are permitted as the first two numbers. The third digit is the build number. It is automatically incremented by one when you edit an instance related to the version. The build number is reset to 1 when you release the version.

> **Note**
>
> **Library setting: "Disable editing of the type version number"**
>
> You can use the library setting "Disable editing of the type version number" to prevent that the type version number can be assigned by the user for the actions "Release version" and "Assign version". By activating the library setting, the type version number can not be changed by the user. The build number is still incremented automatically when a version is released or assigned. When the high limit of the build number in a block (999) has been reached, the version number is incremented in the next block.

The versions of types can have three states:

- In work (faceplates and HMI user data types)
- In test (all sorts of types except faceplates and HMI user data types)
- Released

The following figure shows a type with two versions. One version is "in test" and one version is released:

![Versions of types](images/105134712203_DV_resource.Stream@PNG-en-US.png)

If you use functions (FCs) or function blocks (FBs) as types in the project library, observe the following when compiling the block if you use different instruction versions:

- You can recompile know-how-protected blocks without password if the interfaces of the block versions are identical.
- You can recompile blocks that are not know-how-protected if the supply is not lost for any actual parameters and if no new actual parameters that you need to supply are added by the new version.
- If it is not possible to compile the type with a different instruction version, a new version of the type is required that contains the required adjustments.

---

**See also**

[State of type versions](#state-of-type-versions)
  
[Basics on master copies](#basics-on-master-copies)
  
[Adding types to the project library](#adding-types-to-the-project-library)
  
[Using types of the project library](#using-types-of-the-project-library)
  
[Editing library elements](#editing-library-elements)
  
[Duplicating types](#duplicating-types)

### State of type versions

The versions of types can be in three different states. The states can be determined from the instance or in the library.

#### "In work" status

Only versions of faceplates and HMI user data types have the "In work" status. If a version is in progress, "In work" appears next to the version in the library.

When you create a new type or a new version of a released type, the type is assigned the status "In work". A reference to an instance in the project does not have to exist. Upon release, the compatibility of the type is tested by a consistency check.

#### "In test" status

All types except for faceplates and HMI user data types can have the "in test" status. If a version is in test, "in test" appears next to the instance and in the library. A version in the test state is linked to a test instance in the project. This allows you try out the effects of your changes in a test environment including all online functions before you release a type for use in actual operations.

#### "Released" status

The "released" status is available for all types, regardless of the point of use. If a version has been released, the symbol of the version is marked with a seal in the library:

!["Released" status](images/52230270987_DV_resource.Stream@PNG-de-DE.png)

Released versions can be opened with write protection in their instance. If you want to edit a released version, you must first create a new "In work" or "In test" version.

---

**See also**

[Basics on types](#basics-on-types)
  
[Using types of the project library](#using-types-of-the-project-library)
  
[Creating a test version of a type](#creating-a-test-version-of-a-type)
  
[Editing a test version of a type](#editing-a-test-version-of-a-type)
  
[Creating an editing version of a type](#creating-an-editing-version-of-a-type)
  
[Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)
  
[Discarding versions](#discarding-versions)
  
[Release versions](#release-versions)
  
[Assigning a version](#assigning-a-version)
  
[Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)
  
[Remove the link between instance and type](#remove-the-link-between-instance-and-type)
  
Filtering the display of types

### Displaying a released type version

If you display a released version but do not want to edit it, open the instance with write protection. All types except faceplates and HMI user data types can be opened directly at the instance. Faceplates and HMI user data types can only be opened in the "Libraries" task card.

#### Requirement

The released version has an instance in the project, except the type is a faceplate or an HMI user data type.

#### Opening a type version at an instance

To open a released version of a type with write protection starting from an instance, follow these steps:

1. Select the released version at the instance in the project tree.
2. To do this, right-click the instance and select the "Open" command from the shortcut menu.

   The instance is opened with write protection.

#### Opening a type version in the "Libraries" task card

To open a released version of a type in the "Libraries" task card, follow these steps:

1. Select the version.
2. To do this, right-click the version and select the "Open" command from the shortcut menu.

   If it is a faceplate or HMI user data type, it is opened directly. In this case, skip the remaining steps. If it is any other type, the "Open type" dialog opens.
3. Select the instance with the version that you want to display from the list of instances.
4. Click "OK" to confirm.

   The instance is opened with write protection.

### Displaying properties of a type or version

You can display the properties of a type or version.

#### Procedure

To display the properties of a type or a version and to enter a comment, follow these steps:

1. Select a type or the version of a type in the "Libraries" task card.
2. To do this, right-click on the type or one of its versions and select the "Properties" command from the shortcut menu.

   The "Properties" dialog box opens.
3. If needed, enter a comment on the type in the "Comment" field or edit an existing comment.

#### Visible and changeable properties

The following table shows the properties that you can see or change for a type or version:

| Property | Description | Version | Types |
| --- | --- | --- | --- |
| Name | Name of the type | - | Visible and changeable |
| Version | Version number | Visible | - |
| Last change | If you create, release, duplicate or assign a version, this is recorded as a change to the type. The date and time of the change are entered in the "Last change" field. | Visible | - |
| Author | The creator of the version is indicated as the author. | Visible | - |
| Original library | The project and the library from which the current version of the type was generated are indicated. This information is important, for example, for finding the original of the type after it has been copied from another library. | Visible | - |
| Version GUID or Type GUID | The GUID is used to uniquely identify the type or the version of the type, even if, for example, there are types or versions with an identical name within the project library or the global library. The GUID cannot be changed and is assigned automatically. | Visible | Visible |
| Namespace | If program blocks or PLC data types are created in the project within software units, the names of these program elements can be expanded by a namespace.   Types that are created from program elements with a namespace show this namespace in the properties. However, the "Namespace" field cannot be changed. | - | Visible |
| Lowest device version | Types that are created with WinCC Unified support the definition of the lowest device version in the project. The "Lowest device version" field shows the version but cannot be changed. | - | Visible |
| Comment | Comments on the type or version  Comments from versions are only visible if the interface language set is the same as the one set when the comment was entered. | Visible and, for versions whose status is "in test" or "in work", changeable | Visible and changeable |

### Consistency status of types

Types might no longer be consistent after changes. If types are inconsistent, the ![Figure](images/142594874507_DV_resource.Stream@PNG-de-DE.png) symbol is displayed in the "Libraries" task card on the right edge of the screen. In this way, you can recognize inconsistencies even when the "Libraries" task card is closed.

The "Status" column in libraries indicates whether a type is consistent or inconsistent. The following statuses are displayed:

| Icon | Meaning | Solution |
| --- | --- | --- |
| ![Figure](images/140596194443_DV_resource.Stream@PNG-de-DE.png) | The type is consistent. | - |
| ![Figure](images/140613088011_DV_resource.Stream@PNG-de-DE.png) | The type has more than one inconsistency. | You can find additional information on solutions in section [Fix inconsistencies](#fix-inconsistencies) |
| ![Figure](images/140613459339_DV_resource.Stream@PNG-de-DE.png) | The default version of the type does not use the default version of its dependent type. | You can find additional information on solutions in section [Fix inconsistencies](#fix-inconsistencies) |
| ![Figure](images/143118756363_DV_resource.Stream@PNG-de-DE.png) | The type has duplicate versions. | Manually clean up or delete unneeded versions |
| ![Figure](images/143118760075_DV_resource.Stream@PNG-de-DE.png) | More than one version of the type is instantiated in the device. | Use only one version in the device, preferably the default version, by deleting unneeded versions |
| ![Figure](images/143118763787_DV_resource.Stream@PNG-de-DE.png) | A version other than the default version of the type is instantiated in the device. | You can find additional information on solutions in section [Updating the project to the latest versions](#updating-the-project-to-the-latest-versions) |

---

**See also**

[Showing and hiding columns](#showing-and-hiding-columns)
  
[Setting version as "default"](#setting-version-as-default)
  
[Release versions](#release-versions)
  
[Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)

### Working with types in the project library

This section contains information on the following topics:

- [Adding types to the project library](#adding-types-to-the-project-library)
- [Block requirements](#block-requirements)
- [Referencing of objects within a block](#referencing-of-objects-within-a-block)
- [Duplicating types](#duplicating-types)
- [Using types of the project library](#using-types-of-the-project-library)
- [Displaying types for an instance](#displaying-types-for-an-instance)
- [Compatible and incompatible changes of referenced types](#compatible-and-incompatible-changes-of-referenced-types)
- [Creating a test version of a type](#creating-a-test-version-of-a-type)
- [Editing a test version of a type](#editing-a-test-version-of-a-type)
- [Creating an editing version of a type](#creating-an-editing-version-of-a-type)
- [Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)
- [Discarding versions](#discarding-versions)
- [Discarding all versions within a folder](#discarding-all-versions-within-a-folder)
- [Release versions](#release-versions)
- [Releasing all versions within a folder](#releasing-all-versions-within-a-folder)
- [Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)
- [Fix inconsistencies](#fix-inconsistencies)
- [Remove the link between instance and type](#remove-the-link-between-instance-and-type)
- [Replace type](#replace-type)

#### Adding types to the project library

Types for reuse in the project can be created in the project library for various elements. You can create the following elements as types, for example:

- Program blocks (FCs/FBs)
- PLC data types (UDTs)
- Faceplates
- HMI user data type
- Screens
- Styles

New types and versions of existing types can be added to the project library with drag-and-drop or copy & paste. Independent of their version number and other properties, type versions can be added to the project library if the GUID of the versions is different. This means, for example, that multiple versions with identical version number can be added to the project library.

If you add an element as a type to the project library and this element has dependencies to other elements, the dependent elements are automatically created as a type as well.

After a type has been added to the project library, the type is linked to the added element from the project. The element from the project is thus the instance of the type.

##### Requirement

- The "Libraries" task card is displayed.
- The elements that you want to add as type are compiled.
- The elements are consistent.
- All other requirements for blocks are met, as described in section "[Block requirements](#block-requirements)"

##### Procedure

To add an existing element to the project library as a type, follow these steps:

1. Open the project library in the "Libraries" task card.
2. Drag-and-drop one or more elements into the "Types" folder or any subfolder of "Types".

   Alternative: Copy the elements in the project tree to the clipboard and add the elements in the desired project library folder.

   The "Add type" dialog opens.
3. Enter the properties of the new type:

   - Enter a name for the new type in the "Name of type" field.
   - Enter a version number for the new type in the "Version" field.
   - Enter the name of the editor who is responsible for the type in the "Author" field.
   - Enter a comment on the type in the "Comment" field.
4. Click "OK" to confirm.

**Note**

**Creating a name for the author**

You can enter a user name in the [settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-program-settings). If you add types, create and release type versions or create master copies in the library, the user entered in the settings is stored in the properties as the author by default.

**Note**

**Adding blocks from software units as types with the same name**

When software units are used, blocks with the same name in different namespaces are supported in the project. However, blocks with the same name and different namespaces cannot be added to the same library or the same library folder as types with the same name.

In this case, you are recommended to create a correspondingly named folder in the library for each namespace. This allows blocks to be retained as types with the same name and structured clearly.

##### Result

The new type is generated with a released version. This version has the "default" identifier. The version is linked to the element (instance) that has been added.

---

**See also**

[Basics on types](#basics-on-types)
  
[Duplicating types](#duplicating-types)
  
[Block requirements](#block-requirements)
  
[Referencing of objects within a block](#referencing-of-objects-within-a-block)
  
[Managing software units in libraries (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#managing-software-units-in-libraries-s7-1500)
  
[Creating and managing software units (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#creating-and-managing-software-units-s7-1500)
  
[Library basics](#library-basics)
  
[Adding master copies](#adding-master-copies)

#### Block requirements

##### Permitted blocks for creating a type

You can create types of the following blocks in the project library:

- Function blocks (FBs)
- Functions (FCs)
- PLC data types (UDTs)

##### Consistency and compilation

To create a type from a block, the block must be consistent and compiled. When you create a type, the consistency of the block is checked automatically and the block is compiled if necessary.

##### Block requirements

To create a type from a block, the block must meet the following requirements:

- The block must match the type of CPU.

  A block which does not match a CPU can be identified by an incompatibility symbol to the right of the block in the project tree. The case occurs, for example, if you copy a block from a S7-1500 CPU to an S7-300 CPU. A block of an S7-1500 is not compatible with an S7-300 CPU and cannot be compiled. This means that you cannot create a type from the block.
- The block is not a system data block.
- The block does not contain an individual instance call of an instance data block or a call of a data block within an STL block with the "OPN" command.

##### Special aspects for know-how-protected blocks

You can also create types of know-how-protected blocks. However, keep in mind the following additional requirements for know-how-protected blocks:

- Release of the block for use as type

  Know-how-protected blocks must be released to be used in a library. You make the necessary settings in the block properties.
- The block does not include access to data blocks, PLC tags or PLC constants.

  Because you cannot create types from data blocks, PLC tags or PLC constants, you also cannot create a type from know-how-protected blocks with access to the objects listed above. The instance of a know-how-protected block does not work without the associated data blocks, PLC tags or PLC constants.
- If you edit the test version of a type in the "Libraries" task card, you can enable know-how protection in the block properties.

  The know-how protection can be removed later via the block properties in the project navigation.

---

**See also**

[Adding types to the project library](#adding-types-to-the-project-library)
  
[Referencing of objects within a block](#referencing-of-objects-within-a-block)

#### Referencing of objects within a block

In many cases you reference other objects within a type. For example, call a tag or a data block within block. Accordingly, there is a dependence between the block and the referenced object. The block is only consistent if all dependent objects are also available.

##### Referencing other types

If you call other program blocks, faceplates, PLC data types (UDTs) or HMI user data types in a block these dependent objects are also stored automatically as type in the project library. When the referenced block is reused later as instance in the project, an instance of the referenced object is also created. The TIA Portal thus automatically ensures that the block state is consistent at all times and that the user program can be executed.

##### Referencing additional objects

Access to data blocks, PLC tags or PLC constants is permitted in blocks without know-how protection, Therefore, types can be created from the blocks. While function blocks referenced in a block, for example, are also automatically created as type in the project library, this is not the case for access to data blocks, PLC tags and PLC constants. If data blocks, PLC tags or PLC constants are referenced in a block, only the block itself is created as type. The referenced objects are not created as type. If you reference objects which are not stored as type, note the following:

- Use the block at a different point of use

  If you create an instance from the type at another point of use (such as a different CPU), the referenced objects are missing at the later point of use. This means that you should create referenced objects at the later point of use again (for example, data blocks or tag tables). Make sure that the referenced objects have the same name at the later point of use.
- Subsequent name changes to referenced objects

  If you subsequently change the name of the referenced objects, the block is no longer consistent. The referenced object (for example, a tag) is no longer found. In the case of already released versions of the type, you can no longer correct the call of the object. In this case create a new version of the type and correct the name of the called object. Then update all the instances of the type in the project to the latest version.

---

**See also**

[Block requirements](#block-requirements)
  
[Adding types to the project library](#adding-types-to-the-project-library)
  
[Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)
  
[Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)
  
[Displaying relations to other library objects](#displaying-relations-to-other-library-objects)

#### Duplicating types

Types in the project library can be duplicated. If you duplicate a type, the following applies to the duplicate:

- The duplicate is created in the same folder.
- The duplicate is created from the version of the type with the "default" identifier.
- The duplicate does not have an instance in the project.

##### Requirement

The type is released.

##### Procedure

To duplicate a type in the project library, follow these steps:

1. Right-click on a type.
2. Select the "Duplicate type" command in the shortcut menu.

   The "Duplicate type" dialog opens.
3. Enter the properties of the new type:

   - Enter a name for the new type in the "Name of the type" field.
   - Enter a version number for the new type in the "Version" field.
   - Enter the name of the editor who is responsible for the type in the "User" field.
   - Enter a comment on the type in the "Comment" field.
4. Click "OK" to confirm.

   The new type is generated with a released version.

---

**See also**

[Adding types to the project library](#adding-types-to-the-project-library)
  
[Editing library elements](#editing-library-elements)

#### Using types of the project library

Types from the project library can be used any number of times within a project. The use of types is always linked to a version of the respective type in the project library. If the type contains dependent elements, these are also created as a type of use at a suitable point in the project. Examples of dependent elements are PLC data types referenced in a block.

You can only assign a version of the same type to a device. If necessary, you can create uses of several types at the same time.

Uses of a type are called instances in the project tree.

##### Possible points of use for type versions

To use a type, create an instance of a particular version of the type at a suitable point in the project. Suitable points of use are:

- Folder in the project tree

  An instance of a type can be created in a folder in the project tree. The folder must be suitable for the particular type. If the type is a user data type, for example, you can only create the instance in the "PLC data types" folder.
- Editor

  An instance can be created from a type in a suitable editor. For example, you can create an instance from the type of a function block in another block. The type of the function block is called from another block in this way.

##### Options for creating an instance

You have two options for creating type instances:

- Drag the required type version from the project library and drop it at the location where you want to use it.

  Instances of the types and their dependent elements are generated and pasted at the location where you want to use them. The instances are connected to the respective type version in the project library. If you have created the instances in an editor, instances of the types are also created at the appropriate points in the project tree. By default, the folder structure from the library is reproduced in the project tree. If you want to select a different folder in the project tree, you will find the instances in the same folders as in the library.
- Copying and pasting type instances

  You can copy type instances to the clipboard and paste them at another point. This way you create another instance of the type version. The instance is still connected to the same type version in the project library. When you copy the instance of a type to the clipboard and paste it in another project, all required type versions are accepted in the project library of the other project.

##### Requirement

- The desired versions have been released.
- A device which supports the category of desired type is already available in the project
- The device is not yet assigned any further instance of the same type.

##### Procedure

To create an instance of a type, follow these steps:

1. In the project library, select the versions from which you want to create an instance.
2. Using a drag-and-drop operation, move the versions from the project library to the point of use in the project tree or an editor.

   Alternative: To automatically use the default version, move the types from the project library to the point of use with a drag-and-drop operation.

   For example, use a drag-and-drop operation to move the type of a function block to the block folder of the CPU in the project tree. To call the type directly from another block, for example, move the type from the project library to the point of use in the program editor using a drag-and-drop operation.

**Note**

**Using types with namespace in project**

A namespace can be defined in the project for blocks within software units. For types in libraries, the namespace is displayed in the properties and in the "Namespace" column, but it cannot be edited.

Note the following information about using types in the project:

- If you use types in the project within a software unit, the namespace of the type is adopted.
- If you use types in the project outside a software unit, the namespace of the type is not adopted.

Alternative:

1. Copy one or more instances to the clipboard.
2. Paste the instances at a suitable point in the same project or in a different project.

##### Result

The versions are used in the project.

When the default version of a type is used in the project, the "Version" column shows the symbol ![Result](images/141808550923_DV_resource.Stream@PNG-de-DE.png) and the version used.

When a version other than the default version of the type is used or several versions of the same type are used in the same PLC, the "Version" column shows the symbol ![Result](images/141808725899_DV_resource.Stream@PNG-de-DE.png) and the version used.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Displaying types for an instance](#displaying-types-for-an-instance)
  
[Setting version as "default"](#setting-version-as-default)
  
[Fix inconsistencies](#fix-inconsistencies)
  
[Managing software units in libraries (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#managing-software-units-in-libraries-s7-1500)
  
[Creating and managing software units (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#creating-and-managing-software-units-s7-1500)
  
[Library basics](#library-basics)
  
[Using master copies](#using-master-copies-1)

#### Displaying types for an instance

You can jump from the project tree to the type in the library that belongs to instance in the project tree.

##### Procedure

To jump to the type in the project library, follow these steps:

1. Right-click the instance of the type in the project tree.
2. Select the "Go to type" command from the shortcut menu.

   The referenced type version is displayed in the project library.

---

**See also**

[Using types of the project library](#using-types-of-the-project-library)

#### Compatible and incompatible changes of referenced types

In previous versions of the TIA Portal, all types that directly or indirectly reference a type to be edited are set to the state "In test" or "In work" when editing a type.

As of V17, only the type to be edited is set to the state "In test" or "In work" when a type is being edited. The system does not check whether compatible or incompatible changes have been made to program modules (function blocks and functions) until the type is released:

- If incompatible changes have been made to the edited type, all direct-referencing types are set to the state "In test" or "In work" when you release them.
- If compatible changes were made to the edited type, the state of the direct and indirect referencing types is not changed.

##### Compatible and incompatible changes

The following table shows an overview of the compatible and incompatible changes of objects:

| Object | Compatible changes | Incompatible changes |
| --- | --- | --- |
| Function (FC)  Safety function (F-FC) | Changes to the following types of local data:  - Temp - Constant   Changes to titles (block titles, network titles) and comments (block comments, network comments) in the program window | Changes to the following types of block parameters:  - Input - Output - InOut - Return |
| Function block (FB)  Safety function block (F-FB) | Changes to the following types of local data:  - Temp - Constant - Static   Changes to titles (block titles, network titles) and comments (block comments, network comments) in the program window | Changes to the following types of block parameters:  - Input - Output - InOut - Return |
| PLC data type (UDT) | Changes to comments | Changes to user-defined data types (UDT) used in program blocks |

All changes to HMI types are treated as incompatible changes.

---

**See also**

[Editing a test version of a type](#editing-a-test-version-of-a-type)
  
[Release versions](#release-versions)
  
[Releasing all versions within a folder](#releasing-all-versions-within-a-folder)

#### Creating a test version of a type

Before you release a type for productive use, you need to test the type within a project and on the automation system. The test is conducted in a specific test environment. This test environment can be a CPU, for example.

Create a version with "in test" status for the test. The creation of a version "in test" is suitable for all sorts of types except for faceplates and HMI user data types. On the other hand, versions "In work" can be created from faceplates and HMI user data types.

There are two ways to create a test version of a type and define the test environment:

- In the "Libraries" task card

  Generate the new version with "in test" status in the "Libraries" task card. You can generate the new version either directly from the type or from a specific version of the type.
- At an instance in the project tree

  You can also create the test version directly at the instance in the project tree. Since the instance is always used in a specific version in the project, a new version of the type is generated from the version used at the instance.

You can also create test versions from several types at the same time.

The following rules apply to a version "in test":

- You can set only one version to "in test" for each type at a given time.
- A version in testing may only be linked to a single instance in the project. Therefore, it is not possible to copy an instance to the clipboard, to duplicate it or to create an additional type from the instance as long as it has "in test" status.

##### Requirement

- There is at least one instance of the type within the project in a given version.
- If you want to create the new version from a particular version of the type, the instance must be used in this version in the project.

##### Procedure

To generate a new test version of a type or the version of a type, follow these steps:

1. Select the type, a version of the type, or the instance.

   When you create the test version directly at the instance, you can select several elements or folders with multiple selection. You can skip steps 3 and 4 because the test environment is already defined by the selected instance.
2. Right-click the selected element and select the "Edit type" command from the shortcut menu.

   The "Edit type" dialog opens. If you have started the editing at the instance in the project tree, the test instance is immediately opened for editing.
3. Select an instance of the type from the list in the project.

   If you have started editing at the type itself, the following applies:

   - The location at which the instance is used (for example, the CPU) is also used as test environment for the subsequent editing of the type.
   - Selecting the test instance also defines the version to be edited.

   The following applies to editing a specific version:

   If your starting point is a specific version, you can only select from the list instances that are used in the same version.
4. Click "OK" to confirm.

##### Result

A new version of the type is created. The new version is "in test" and is identified as such in the user interface.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)

#### Editing a test version of a type

When you edit a version "in test", a new version is not created. You can start the editing of the test version at the instance in the project tree or in the "Libraries" task card.

> **Note**
>
> **Deleting and renaming interface parameters**
>
> You can add new parameters. However, if you rename or delete existing parameters, these parameters will not be supplied when the block is called.
>
> When you make changes to the interface parameters or other incompatible changes, all type versions that reference this version are set to the "In test" status when the version is released.

> **Note**
>
> **Changing types in protected projects**
>
> If your project is protected, you need the corresponding function rights to change types. Additional information can be found at "[Basics of user management in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)" and "[Overview of function rights](Managing%20users%20and%20roles.md#overview-of-function-rights)".

##### Procedure

To edit the test version of a type, follow these steps:

1. Right-click the test version or the instance.
2. Select the "Edit type" command from the shortcut menu.

   The test instance is opened and can be edited.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)
  
[Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)
  
[Discarding versions](#discarding-versions)
  
[Release versions](#release-versions)

#### Creating an editing version of a type

If you want to edit a type with faceplates or HMI user data types, create a new "In work" version of the type. To check the compatibility of the changes, a consistency check is automatically performed for the type prior to the release.

##### Requirement

The project library is opened in the "Libraries" task card.

##### Procedure

To create a new version of a type in work, follow these steps:

1. Right-click the type or the version of the type.
2. Select the "Edit type" command from the shortcut menu.

   A new "in work" version is created and opened for editing.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)

#### Performing a consistency check for a version

A type version can unintentionally obtain an inconsistent state during editing. To notice errors in the development process in good time, you can regularly perform a consistency check. However, the consistency check always takes place automatically as soon as you release a version.

Details of how to start the consistency check manually for the version of a type are provided below.

##### Requirement

- The project library is opened in the "Libraries" task card.
- The version is "In work" or "In test".

##### Procedure

To perform a consistency check for the version of a type, follow these steps:

1. Right-click on the version that you want to check for consistency.
2. Select the "Check consistency" command in the shortcut menu.

   The consistency check is carried out. You receive a message with the result of the consistency check.

---

**See also**

[Release versions](#release-versions)
  
[Discarding versions](#discarding-versions)
  
[Editing a test version of a type](#editing-a-test-version-of-a-type)
  
[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)

#### Discarding versions

Discard versions of a type "In test" or "In work" when you no longer need the version. You can also select several types or folders and discard all test or working versions contained therein. All uses of the deleted versions are reset to the last released status.

##### Requirements

- The "Libraries" task card or the library management is opened.
- The version that you want to discard is in the state "In test" or "In work".

##### Procedure

To discard one version, follow these steps:

1. Right-click the version that you want to discard.
2. Select the "Discard changes and delete version" command from the shortcut menu.

   The version is deleted.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)
  
[Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)

#### Discarding all versions within a folder

You can discard all versions with the "In test" or "In work" status at the same time within a folder. All uses of the deleted version are reset to the last released status.

##### Requirement

The "Libraries" task card or the library management is opened.

##### Discarding a version of a single type

To discard all versions within a folder, follow these steps:

1. Right-click the folder.
2. Select the "Discard all" command from the shortcut menu.

   All "In test" or "In work" versions are deleted.

#### Release versions

When you are finished editing a type version, release the version for productive use. Assign a version number for the release. You can also use a multiple selection to release several versions at the same time.

If you have made structural changes to the type version to be released, such as changes at the interfaces, only the types that reference the changed type version and are affected by the change are set to the "In test" or "In work" status. To set all referencing types by default to the "In test" or "In work" status when they are released, select the check box "Set all dependent types to 'In test' status" in the settings under "General > Library settings".

##### Requirements

- The "Libraries" task card or the library management is opened.
- The versions that you want to release are "In test" or "In work" status.
- The versions are consistent.

  A consistency check is performed as soon as you start the release. If errors that prevent a release occur during the consistency check, a message is displayed indicating how you can correct the errors.

##### Procedure

To release type versions, follow these steps:

1. Select the versions you want to release.
2. Right-click your selection.
3. Select the "Release version" command from the shortcut menu.

   The "Release type version" dialog box opens.
4. If necessary, change the properties of the version:

   - Enter a name for the type in the "Type name" field. If you have selected several versions for release, the "Name" field cannot be changed.
   - In the "Version" field, define a main and an intermediate version number for the version to be released. If you have selected several versions for release, the "Version" field cannot be changed and the last version number is used for the release.
   - In the "Author" field, enter the editor of the version to be released.
   - In the "Comment" field, enter a comment on the version to be released.
5. If necessary, change additional options of the version:

   - "Set dependent types to edit mode" option: If you have made incompatible changes to the type version to be released, such as changes at the interfaces, this check box is selected by default. Types that reference the changed type version are set to the "In test" or "In work" status by default. Clear the check box if you do not want to set the referencing types to the "In test" or "In work" status.

     If you have made compatible changes to the type version to be released, this check box is cleared by default.
   - "Update instances in the project" option: Select the check box to update all instances in the project to the most recent version.
   - "Delete unused type versions from the library" option: Select the check box to delete all versions from the library that are not connected to any instance in the project. Versions with dependencies on other types or master copies are not deleted.
6. Click "OK" to confirm.

##### Results

- The selected versions are released.
- The properties are applied for the types themselves, the versions to be released, and for all future versions. Versions already released remain unaffected by the changes.
- The released version has the "default" identifier.
- If needed, all instances with the same original version are updated to the most recent version and the unused versions of the type are deleted.
- Depending on the changes you have made, releasing the type version has effects on types that reference this version:

  - If you have made incompatible changes to the type version to be released, such as changes at the interfaces, the types that directly reference the changed type version are set to the "In test" or "In work" status. The calling types still reference the last released version.
  - If you have made compatible changes to the type version to be released, the types that directly reference the changed type version are not changed. The calling types reference the newly released version in this case.
- A icon in the "Status" column indicates whether a type is consistent or inconsistent. You can find more information on the displayed status in [Consistency status of types](#consistency-status-of-types).

---

**See also**

[Releasing all versions within a folder](#releasing-all-versions-within-a-folder)
  
[Compatible and incompatible changes of referenced types](#compatible-and-incompatible-changes-of-referenced-types)
  
[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)
  
[Performing a consistency check for a version](#performing-a-consistency-check-for-a-version)
  
[Assigning a version](#assigning-a-version)
  
[Adding types to a global library](#adding-types-to-a-global-library)
  
[Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)

#### Releasing all versions within a folder

When you are finished editing all types within a folder, release all versions simultaneously.

If you have made incompatible changes to the type version to be released, such as changes at the interfaces, only the types that reference the changed type version and are affected by the change are set to the "In test" or "In work" status. To set all directly referencing types by default to the "In test" or "In work" status when they are released, select the check box "Set all dependent types to 'Processing' status" in the settings under "General > Library settings".

##### Requirements

- The "Libraries" task card or the library management is opened.
- The folder includes versions "In test" or "In work" status.
- All versions "In test" or "In work" are consistent.

  A consistency check is performed as soon as you start the release. If errors that prevent release occur during the consistency check, a message is displayed indicating how to correct the errors.

##### Procedure

To release all type versions within a folder, follow these steps:

1. Right-click the required folder.
2. Select the "Release all" command from the shortcut menu.

   The "Release type version" dialog box opens.
3. If necessary, change the properties of the version:

   - In the "Author" field, enter the editor of the versions to be released.
   - In the "Comment" field, enter a comment on the versions to be released.
4. If necessary, change additional options of the version:

   - "Set dependent types to edit mode" option: If you have made incompatible changes to the type versions to be released, such as changes at the interfaces, this check box is selected by default. If types with compatible and incompatible changes have been selected for release, the check box shows an ambiguous status instead of a check mark. Types that directly reference an incompatible changed type version are set to the "In test" or "In work" status by default.

     Clear the check box if you do not want to set the directly referencing types to the "In test" or "In work" status.

     If you have made compatible changes to the type version to be released, this check box is cleared by default.
   - "Update instances in the project" option: Select the check box to update all instances in the project to the most recent version.
   - "Delete unused type versions from the library" option: Select the check box to delete all versions from the library that are not connected to any instance in the project. Versions with dependencies on other types or master copies are not deleted.
5. Click "OK" to confirm.

##### Results

All type versions "In test" or "In work" status within the selected folder are released.

The properties are applied for the versions to be released and for all future versions. Versions already released remain unaffected by the changes.

Versions of types not used in the project may be deleted.

Depending on the changes you have made, releasing the type version has effects on types that reference this version:

- If you have made incompatible changes to the type version to be released, such as changes at the interfaces, the types that directly reference the changed type version are set to the "In test" or "In work" status. The calling types still reference the last released version.
- If you have made compatible changes to the type version to be released, the types that reference the changed type version are not changed. The calling types reference the newly released version in this case.

---

**See also**

[Release versions](#release-versions)

#### Updating the project to the latest versions

After you have updated several types in the project library, update all instances in the project to the most recent version of the types from the project library. If you do not want to apply the changes to the entire project, restrict the update to individual devices in the project.

Each of the following elements can be selected as source for the update:

- The entire project library
- Individual folders within the project library
- Individual types

  You can select multiple types.

> **Note**
>
> **Deleting unused type instances from the project**
>
> By default, when the project is updated to the latest type instances, unused type instances are deleted from the project.
>
> In order to prevent deleting unused type instances from the project, under "General > Library settings" select the check box "Do not remove unused type version instances when updating the project from the library".

##### Requirements

The "Libraries" task card or the library management is opened.

##### Procedure

To update instances in a project with the contents from the project library, follow these steps:

1. Select the entire project library or elements from it.
2. Right-click the required elements and select the "Update types > Project" command from the shortcut menu.

   The "Update types in the project" dialog box opens.
3. Select either the entire project or individual devices for the update.
4. Select options for the update:

   - The "Update instances in the project" check box is always selected during this process.
   - Select the "Delete unused type versions from the library" check box to delete all older versions of the updated types from the project library.
5. Click "OK" to confirm.

   If you have made compatible changes, the update is performed.

   If you have made incompatible changes, a warning appears due to an inconsistent state of the project library. In this case, you need to [correct the inconsistencies](#fix-inconsistencies).

##### Results

The following changes are made to the project:

- All instances within the selected devices are updated to the most recent version of the linked type.
- All older versions are deleted from the project library as needed.
- If a CPU does not include block instances that are called in the user program, the block instances are removed from the CPU. The types still exist in the library and can be used in the project again as needed.
- If you have made incompatible changes to the type versions to be updated, such as changes at the interfaces, the instances in the project that directly reference the changed type versions are set to the "In test" or "In work" status. The calling types still reference the last released version.
- If you have made compatible changes to the type versions to be updated, the instances in the project that reference the changed type versions are not changed. The calling types reference the most recent compatible version in this case.
- A icon in the "Status" column indicates whether a type is consistent or inconsistent. You can find more information on the displayed status in [Consistency status of types](#consistency-status-of-types).
- You can find a log of the update in the project tree under "Common data".

---

**See also**

[Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)
  
[Using logs](Editing%20projects.md#using-logs)
  
[Updating library with the types of another library](#updating-library-with-the-types-of-another-library)
  
[Basics on types](#basics-on-types)
  
[Library basics](#library-basics)
  
[State of type versions](#state-of-type-versions)

#### Fix inconsistencies

Changes to types in the project library or in a global library can cause inconsistencies when the project is updated. This happens, for example, when you make incompatible changes to a type.

**Example**

You have made changes to a type in a global library and created a new default version (e.g. V0.0.2).

The instance of a dependent type in the project references the previous default version (e.g. V0.0.1).

You update the project with the new version from the global library using the function "Update types > Project". Depending on the changes, the referencing types in the project are consistent or inconsistent:

- If you have made compatible changes to the type in the library, the referencing type is consistent. The default version of the type references the new default version of the dependent type (e.g. V0.0.2). The "Status" column shows the consistent status with a green symbol.
- If you have made incompatible changes to the type in the library, the referencing type is inconsistent. The default version of the type references the previous default version of the dependent type (e.g. V0.0.1). The "Status" column shows the inconsistent status with a yellow symbol. In this case, you need to correct the inconsistencies.

##### Requirements

- You have made incompatible changes to a type in the project library or in a global library.
- You have created a new default version of the changed type.
- You have run the "Update types > Project" command to update the project.
- You have received a warning due to an inconsistent state of the project library.

##### Correcting inconsistencies before updating the project

To correct the inconsistencies before updating the project, proceed as follows:

1. Click the "Yes" button in the warning.

   The instances in the project are not updated with the inconsistent versions from the library.
2. Correct the inconsistencies and update the project again.

##### Correcting inconsistencies after updating the project

If you do not want to correct the inconsistencies and nevertheless want to update the project, proceed as follows:

1. Click the "No" button in the warning.

   The "Status" column in the project library displays a yellow symbol for the inconsistent type. This status indicates that the default version of the type does not reference the default version of the changed type.

   The project is updated with the inconsistent versions from the library.

   The instance of the directly referencing type is not set to the "In test" status.
2. Open the shortcut menu of the inconsistent type in the project library.

   To fix all inconsistent types within a folder, open the shortcut menu of the folder.
3. Select one of the functions described below from the "Fix inconsistencies" shortcut menu.

##### Using the default version

To use the default version of the referenced type for compatible changes, select the "Use default version" command from the "Fix inconsistencies" shortcut menu.

##### Adapt inconsistent type

1. To adapt the inconsistent type, select "Adapt inconsistent type" from the "Fix inconsistencies" shortcut menu.

   The "Edit type" dialog opens.
2. Select an instance of the type from the list in the project.
3. Click "OK" to confirm.

   The following actions are performed:

   - The default version of the inconsistent type is updated in the project.
   - The default version of the referenced type is updated in the project.
   - The default version of the inconsistent type is set to the "In test" status.

     > **Note**
     >
     > **Adapting inconsistent types of HMI objects**
     >
     > Inconsistent types of HMI objects in the project are not updated with the "Adapt inconsistent type" function. The default version of the inconsistent type is set to the "In test" status.
4. Release the version.

   You can find additional information in the section "[Release versions](#release-versions)".
5. If an error message appears during compiling, correct the errors and release the version again.

   You can find additional information in the section "[Editing test version of a type](#editing-a-test-version-of-a-type)".

##### Setting the currently referenced version as "default"

To set and use the currently referenced version of the type as "default", select "Set the currently referenced version as 'default'" from the "Fix inconsistencies" shortcut menu.

---

**See also**

[Consistency status of types](#consistency-status-of-types)

#### Remove the link between instance and type

Instances of types are always connected to the version of the corresponding types. They cannot be edited like an ordinary object. If you edit the instance, a new version of the type is created automatically in the project library and the changes therefore affect the entire project.

If you remove the link between the instance and its type, you then edit the object like an ordinary object in the project tree.

> **Note**
>
> **Disable "Terminate connection to type"**
>
> If you want to prevent instances of your types getting separated in the project, you can also deactivate the "Terminate connection to type" option.
>
> Select the option "Shortcut menu entry 'Terminate connection to type'" under "Options > Settings > General > Library settings".

##### Requirement

The instance must not be in the "in test" state.

##### Procedure

To remove the link between instances and their type versions, follow these steps:

1. Select one or more instances in the project tree.
2. Right-click the selection and select the "Terminate connection to type" command from the shortcut menu.
3. The link to the corresponding type versions is removed.

---

**See also**

[Basics on types](#basics-on-types)
  
[Library basics](#library-basics)
  
[State of type versions](#state-of-type-versions)

#### Replace type

The "Replace type" function replaces a type instance in a project with a selected target instance. The function is available for HMI types.

The source for replacing types is always a type version; the target is always the released version of a type.

If a type is selected for replacing instead of a type version, the default version is used as the source version to be replaced.

##### Requirements

- The project library is opened in the "Libraries" task card.
- A source version of a type is available.
- A target version of a type is available.

##### Procedure

1. Right-click on the source type or a version of the source type.
2. Select the "Replace type" command from the shortcut menu.

   The "Replace target selection" dialog opens.

   All compatible target types are displayed.
3. Select a type in the left-hand part of the dialog.
4. Select a version of the target type in the list view in the right-hand part of the dialog.
5. Confirm your selection by clicking on the green check mark.

   A status message is displayed in the Inspector window in the "Info > General" tab.

##### Result

All instances of the source type are replaced on all devices with the selected versions of the target type.

### Working with types in global libraries

This section contains information on the following topics:

- [Adding types to a global library](#adding-types-to-a-global-library)
- [Using types from a global library](#using-types-from-a-global-library)
- [Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)

#### Adding types to a global library

Global libraries are used as a central resource when working on multiple projects. Among the types, only the types in the project library can be edited directly. Therefore, use the project library if you want to work on types. When you are finished editing a type in the project library, you can add the type to a global library. Adding types from the project library corresponds to a normal copy process from the project library. The default versions in the target library remain the same.

New types and versions of existing types can be added to global libraries with drag-and-drop or copy & paste. Independent of their version number and other properties, type versions can be added to the global libraries if the GUID of the versions is different. This means, for example, that multiple versions with identical version number can be added to a global library.

##### Requirement

- The "Libraries" task card is opened.
- The global library to which you want to add types is opened and can be written to.

##### Procedure

To add types to a global library, follow these steps:

1. Open the required folder in the global library in the "Libraries" task card.
2. Drag one or more types from the project library to the "Types" folder or any subfolder of the global library.

Alternative:

1. Copy the required types from the project library to the clipboard.
2. Open the required global library in the "Global library" pane of the "Libraries" task card.
3. Right-click the "Types" folder or any subfolder of "Types".
4. Select "Paste" in the shortcut menu.

##### Result

The types are inserted in the global library. Dependent types, such as types of HMI user data types or tags, are also copied to the global library, provided they do not already exist there. This ensures that all necessary elements for generating an instance are present in the global library.

If a type already exists in the global library, the described action corresponds to an update of the global library. In this case, the most recent released versions of the types are added to the global library. The default versions in the global library are not changed.

---

**See also**

[Basics on types](#basics-on-types)
  
[Release versions](#release-versions)
  
[Assigning a version](#assigning-a-version)
  
[Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)
  
[Library basics](#library-basics)

#### Using types from a global library

To use types from the global library, create an instance of a particular version of the type at a suitable point in the project. If necessary, you can create uses of several types at the same time. Uses of a type are called instances in the project tree.

##### Possible points of use for type versions

Suitable points of use for types from the global libraries are:

- Folder in the project tree

  An instance of a type can be created in a folder in the project tree. The folder must be suitable for the particular type. If the type is a user data type, for example, you can only create the instance in the "PLC data types" folder.
- Editor

  An instance can be created from a type in a suitable editor. For example, you can create an instance from the type of a function block in another block. The type of the function block is called from another block in this way.

##### Linking the instance with the project library

In the project, instances of types from a global library are not linked to the type in the global library. Instead, a copy of the type and its dependent elements is generated in the project library when an instance is created. Dependent elements, for example, can be PLC data types that are referenced in a block. In each case, the copy of the type and the dependent elements in the project library contains the version that you have linked to the instances. If the type or a dependent element already exists in the project library, only the missing version is added in the project library, if necessary.

The instance is finally linked to the copy of the type in the project library. You can only assign a type to a device once irrespective of the version.

##### Requirement

- A device which supports the category of the type is already available in the project.
- The device is not assigned to any further instances of the same type.

##### Procedure

To use the version of a type in the project, follow these steps:

1. In the global library, select the versions from which you want to create an instance.
2. Using a drag-and-drop operation, move the desired versions of the types to the point of use.

   Alternative: To automatically use the default version, move the types from the library to the point of use with a drag-and-drop operation.

   For example, use a drag-and-drop operation to move the type of a function block to the block folder of the CPU in the project tree. To call the type directly from another block, for example, move the type from the library to the point of use in the program editor using a drag-and-drop operation.

**Note**

**Using types with namespace in project**

A namespace can be defined in the project for blocks within software units. For types in libraries, the namespace is displayed in the properties and in the "Namespace" column, but it cannot be edited.

Note the following information about using types in the project:

- If you use types in the project within a software unit, the namespace of the type is adopted.
- If you use types in the project outside a software unit, the namespace of the type is not adopted.

##### Result

Missing types or individual versions are added in the project library. If a type is not yet present in the project library, it is stored in the same folder as before in the global library. An instance is created from the types and their dependent elements and inserted at the point of use. The instances are connected to the respective type version in the project library.

If you have created the instances in an editor, instances of the types are also created at the appropriate points in the project tree. The folder structure from the library is reproduced in the project tree. You will therefore find the instances in the same folders as in the global library.

---

**See also**

[Basics on types](#basics-on-types)
  
[Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)
  
[Setting version as "default"](#setting-version-as-default)
  
[Managing software units in libraries (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#managing-software-units-in-libraries-s7-1500)
  
[Creating and managing software units (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#creating-and-managing-software-units-s7-1500)
  
[Library basics](#library-basics)
  
[Using the element view](#using-the-element-view)

#### Updating the project to the latest type versions

In large enterprises with numerous automation projects. the global libraries are frequently edited from a central location. The updated global libraries of the individual projects are made available after the completion of a new version. If you have received a more recent version of a global library, replace the outdated instances in your project with the most recent version.

If you do not want to apply the changes to the entire project, restrict the update to individual devices in the project.

If you want to distribute types to different users or make updated types available only to specific users, you can select or deselect individual types specifically for updating.

The project library is also updated with the new versions of the types in the global library during the updating of the project or individual devices.

In certain cases, you may want to overwrite types in the project while updating with versions from a global library. Selecting the "Force update" option has the following effects:

- When the source version with the "default" identifier has the same or a lower version level than the target version with the "default" identifier, this source version from the global library becomes the new "default" version in the project after the update.
- When different editors of a type in different source libraries create identical version statuses, these versions with identical version numbers are merged in the project if the GUID of the versions is different.

The following elements can be selected as source for the updating:

- The root node of global libraries
- Individual folders within a global library
- Individual types

  You can select multiple types.

> **Note**
>
> **Deleting unused type instances from the project**
>
> By default, when the project is updated to the latest type instances, unused type instances are deleted from the project.
>
> In order to prevent deleting unused type instances from the project, under "General > Library settings" select the check box "Do not remove unused type version instances when updating the project from the library".

##### Requirements

- The "Libraries" task card or the library management is opened.
- The updated global library is open.

##### Procedure

To update instances in a project with the contents from a global library, follow these steps:

1. Select the updated global library or the individual elements from it.
2. To exclude types from the update, right-click on the type and select "Select for updating > No" from the shortcut menu.

   Alternatively, or if you want to exclude several types from the update, select the check box for each type in the "Select for updating" column.
3. Right-click the global library or the required elements and select the "Update types > Project" command from the shortcut menu.

   The "Update types in the project" dialog box opens.
4. Select either the entire project or individual devices for the update.
5. Select options for the update:

   - The "Update instances in the project" check box is always selected during this process.
   - Select the "Delete unused type versions from the library" check box to delete all older versions of the updated types from the project library.
   - Select the check box "Force update" to update type versions regardless of their version.
6. Click "OK" to confirm.

   If you have made compatible changes, the update is performed.

   If you have made incompatible changes, a warning appears due to an inconsistent state of the project library. In this case, you need to [correct the inconsistencies](#fix-inconsistencies).

##### Results

The following changes are made to the project:

- All instances within the selected devices are updated to the most recent version of the linked type.
- The most recent version of the select types is present in the project library. All older versions are deleted as needed.
- When there is a lower default version in the global library and you have selected the "Force update" option, the higher default version in the project is updated with the lower default version from the global library.
- When there is an identical version in the global library and you have selected the "Force update" option, then both versions are instantiated with the same version number in the project.
- If you have made incompatible changes to the type versions to be updated, such as changes at the interfaces, the instances in the project that directly reference the changed type versions are set to the "In test" or "In work" status. The calling types still reference the last released version.
- If you have made compatible changes to the type versions to be updated, the instances in the project that reference the changed type versions are not changed. The calling types reference the most recent compatible version in this case.
- A icon in the "Status" column indicates whether a type is consistent or inconsistent. You can find more information on the displayed status in [Consistency status of types](#consistency-status-of-types).
- You can find a log of the update in the project tree under "Common data".

---

**See also**

[Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)
  
[Using logs](Editing%20projects.md#using-logs)
  
[Updating library with the types of another library](#updating-library-with-the-types-of-another-library)
  
[Basics on types](#basics-on-types)
  
[Library basics](#library-basics)
  
[Adding types to a global library](#adding-types-to-a-global-library)

### Setting version as "default"

When you release or update versions, the highest released version is used as "default". Alternatively, you can specify a different released version as "default".

#### Requirements

- You have opened the project library or a global library.
- The desired type version is released.

#### Procedure

1. Select a version.
2. Right-click to call up the shortcut menu.
3. Select the shortcut menu command "Set as 'default'".

#### Results

When instantiating, creating, releasing and updating the type, the default version is used instead of the highest released version. The default version is also used when you create newer versions.

A icon in the "Status" column indicates whether a type is consistent or inconsistent. You can find more information on the displayed status in [Consistency status of types](#consistency-status-of-types).

### Assigning a version

A library is more clearly structured if types related by content have the same version number. The identical version number reflects the work progress. When you have completed the work on multiple associated types, you can assign the same version number to these types.

You have the following options to assign a common version to types:

- One or more folders in a library
- One or more types

#### Requirement

- The "Libraries" task card or the library management is opened.

#### Procedure

To assign several types the same version, follow these steps:

1. Select the types to which you want to assign a common version.
2. Select the "Assign version" command from the shortcut menu.

   The "Assign version" dialog box opens.
3. If necessary, change the properties of the version:

   - In the "Version" field, determine the new version number. The version number must be higher than the highest version number of all selected types.
   - In the "Author" field, enter the person responsible for the version to be released.
   - In the "Comment" field, enter a comment on the version to be released.
4. Click "OK" to confirm.

#### Result

The selected type versions are changed as follows:

- A new version of all selected types is created with the specified version number.
- The properties are applied to all selected types, the new version and to all future versions. Lower versions remain unaffected by the changes. If you make no changes to the properties, the properties of the last released version or the version specified by the user as "default" of each type are applied.
- If a version is set as "default" by the user, the new version of the selected type is created from the default version with the specified version number. This newly created version will then have the "default" identifier.
- The build number of dependent types is incremented to the next free build number as long as the dependent types were not in your selection. If you had selected a dependent type as well, the version number you specified will be assigned.

A log of the changes is created. If you have versioned the types in the project library, you find the log in the project tree under "Common data > Logs". If you have versioned types in a global library, you find the log in the "Common data > Logs" folder in the level below the global library.

---

**See also**

[Basics on types](#basics-on-types)
  
[State of type versions](#state-of-type-versions)
  
[Library basics](#library-basics)
  
[Release versions](#release-versions)
  
[Adding types to a global library](#adding-types-to-a-global-library)
  
[Using logs](Editing%20projects.md#using-logs)
  
[Displaying logs of global libraries](#displaying-logs-of-global-libraries)

## Updating library with the types of another library

An existing library can be updated with the contents of another library. The following options are available for updating libraries:

- Updating a global library with types from another global library or from the project library
- Updating the project library with types from a global library

Each of the following elements can be selected as source for the update:

- Root nodes in the project library
- Root nodes of global libraries
- "Types" folder
- Individual folders within the "Types" folder
- Individual types

  You can select multiple types.

During the update, new versions are added to the types that already exist in the target library. Types that do not yet exist in the target library are copied together with all their versions to the target library.

In certain cases, you might want types in a library to be overwritten with versions from a different library. Selecting the "Force update" option has the following effects:

- When the source version with the "default" identifier has a lower version level than the target version with the "default" identifier, the lower source version becomes the new "default" version in the target library after the update.
- When different editors of a type in different source libraries create identical version statuses, these versions with identical version numbers are merged in the target library.

If you want to distribute types to different users or make updated types available only to specific users, you can select or deselect individual types specifically for updating.

> **Note**
>
> **User-defined documentation when copying types**
>
> User-defined documentation is not copied together with a type to another library. You need to copy the user-defined documentation for types to the corresponding directory.
>
> For additional help on using the user-defined documentation, refer to the section "[Using user-defined documentation](Editing%20project%20data.md#using-user-defined-documentation)".

### Requirement

If you want to update a global library, you have to open it with write permission.

### Procedure

To update a library with the contents of a different library, follow these steps:

1. Select the "Types" folder or individual elements from this folder as source for the update.
2. To exclude types from the update, right-click on the type and select "Select for updating > No" from the shortcut menu.

   Alternatively, or if you want to exclude several types from the update, select the check box for each type in the "Exclude from update" column.
3. Right-click the source and select the "Update types > Library" command from the shortcut menu.

   The "Update types in a library" dialog box opens.
4. Select the type of library you want to update:

   - Select "Update project library" to update the project library with types from a global library.
   - Select "Update global library" if you want to update a global library.
5. Optional: In the drop-down list, select the global library that you want to update, if you want to update a global library.
6. Select the options for the update:

   - The option "Update instances in the project" is always deactivated in this process.
   - Activate the "Delete unused type versions from the library" option if you want to delete all non-default versions from the target library that do not have dependencies to other types.
   - Activate the "Force updates" option if you wish to set a lower default version from the source library as the new default version in the target library.

     Deactivate this option if you wish to get a higher default version in the target library after the update as the default version.
7. Click "OK" to confirm.

   The update is performed.

### Result

The following changes were made to the target library:

- Types not yet available in the target library were copied together with all their type versions. More recent type versions were added to the types that already existed in the target library. If a more recent version of a type already existed in the target library, the latest version was nevertheless copied and automatically assigned a newer version number.
- If needed, all versions of types were deleted from the project library if these were not used in any instance in the project.
- When there is a lower default version in the source library and you have selected the "Force update" option, the higher default version in the target library is updated with the lower default version from the source library.
- If there is a type version in the source library with the same version number as in the central library, and a different version GUID, then both versions are present with the same version number in the target library. In this case:

  - If you have activated the "Force updates" option, the default version from the source library is the new default version in the target library.
  - If you have deactivated the "Force updates" option, the default version in the target library is retained.
- If you have made incompatible changes to the type versions to be updated, such as changes at the interfaces, the types that directly reference the changed type version are set to the "In test" or "In work" status. The calling types still reference the last released version.
- If you have made compatible changes to the type versions to be updated, the types that reference the changed type version are not changed. The calling types reference the newly released version in this case.
- The icon in the "Status" column shows whether the references of the type are consistent with other types:

  - Green: The references of the type are consistent. The default version of the type references the default version of the dependent type.
  - Yellow: The references of the type are inconsistent. The default version of the type does not reference the default version of the dependent type.
- A log listing all performed changes to the target library was created for the update.

  If you have updated the project library, you can find the log in the project tree under "Common data > Logs".

  If you have updated a global library, you can find the log in the "Common data > Logs" folder in the level below the global library.

---

**See also**

[Using logs](Editing%20projects.md#using-logs)
  
[Updating the project to the latest versions](#updating-the-project-to-the-latest-versions)
  
[Updating the project to the latest type versions](#updating-the-project-to-the-latest-type-versions)
  
[Displaying logs of global libraries](#displaying-logs-of-global-libraries)
  
[Library basics](#library-basics)
  
[Using user-defined documentation](Editing%20project%20data.md#using-user-defined-documentation)
  
[Conventions for the creation](Editing%20project%20data.md#conventions-for-the-creation)

## Multiuser Engineering in libraries

This section contains information on the following topics:

- [Multiuser Engineering with library elements](#multiuser-engineering-with-library-elements)
- [Checking in types and master copies](#checking-in-types-and-master-copies)

### Multiuser Engineering with library elements

Library elements in the project library can be used in Multiuser Engineering.

More information on working with Multiuser Engineering can be found in section "[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)".

#### Markings for the check-in

Individual library elements within the project library are marked for Multiuser Engineering in the same way as in the project tree. You can mark library elements in the following areas of the TIA Portal:

- "Libraries" task card
- Library management
- At the respective point of use, e.g. at type instances

Always mark the library elements manually.

The figure below shows the "Libraries" task card with the marking column and marked library elements for the multiuser function:

![Markings for the check-in](images/95843094027_DV_resource.Stream@PNG-en-US.png)

#### Library elements that can be marked

The following table shows which types can be marked for check-in in the project library and in the instance in the project:

|  | Type can be marked in the library | Instance can be marked |
| --- | --- | --- |
| Function blocks (FB) | Yes | Yes |
| PLC Block Library Type (FC) | Yes | Yes |
| PLC data types (UDT) | Yes | Yes |
| HMI faceplates | Yes | By marking the screen in which the instance of the block is located |
| HMI user-defined data type (UDT) | Yes | By marking the object (e.g. screen or HMI tag), in which the UDT is used. |
| HMI style | Yes | No |
| HMI style sheet | Yes | Not available |
| HMI screen | Yes | Yes |
| HMI C script | Yes | Yes |
| HMI VB script | Yes | Yes |

#### Deleting types in the local session

If you want to delete types in the local session, note the following:

- Release the type if a version is still being tested or edited.
- To delete the type in the assigned server project, mark the type in the local session before deletion.

Individual versions can be deleted in the local session, but these are retained in the server project. Because deleting is an administrative activity, you delete the types and their versions in the server project.

#### Updating the project

If you want to update the project, note the following:

- Mark the types before you update the project.
- Mark the HMI user data types at the point of use before you update the project.
- Changes to HMI styles are not applied in the local session when you update the project. Update the HMI style in the server project view.

---

**See also**

[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)

### Checking in types and master copies

Check changes to types and master copies into the multiuser server project in the same way as all other objects within the local session. When you check in a type, all versions of the type are always checked in. When you check in an instance, the type is also checked in automatically.

#### Update the server project

Types and master copies are identified and synchronized based on the unique GUID in the server project. When types and master copies are checked in, their changes from the local session are applied in the server project:

- The properties of the type or the master copy, e.g. the name, are applied in the server project
- Missing versions of types are added.
- The folder structure within the library is applied in the server project. However, empty folders are not deleted.

Conflicts can occur through updating the server project. Any conflicts are resolved as follows:

- Naming conflicts

  Two types with identical names cannot be checked in. The names of the respective types automatically receive an extension (<_1>, etc.).

  Two types instances with identical names are not permitted and result in an error when checking in.

- A type is "In test" or "In work" status.

  If a type is in one of these two states in the server project or in the local session, you cannot update the server project. First release all marked types before you update the server project.

- Version conflicts

  A message will notify you if both the server project and local session have versions with the identical version number but different content. Change the version numbers so that these exist only once.

More information on Multiuser Engineering can be found in section "[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)".

---

**See also**

[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)

## Using library texts

This section contains information on the following topics:

- [Exporting library texts](#exporting-library-texts)
- [Importing library texts](#importing-library-texts)
- [Defining the project languages in the project library](#defining-the-project-languages-in-the-project-library)
- [Updating imported library tests for type instances](#updating-imported-library-tests-for-type-instances)

### Exporting library texts

#### Description

You can export library element texts for translation and then reimport them. The texts are exported to an Office Open XML file with the extension ".xlsx". This can be edited in Microsoft Excel or a number of other spreadsheet programs.

The following export options are available:

- Exporting texts of selected types and master copies

  You can select individual types or master copies, and use the shortcut menu to export only the texts of the selected object.

  Or you can select and export multiple or all types or master copies by making multiple selections.
- Exporting texts of all library elements of the project library or a global library

  You can use the buttons in the toolbar of the "Project library" or "Global libraries" pane to export all texts of a project library or a global library.

If multiple versions of one type exist, the texts of the default version are exported.

If the current version of a type has not been released yet and has the extension "In test" or "In work", you will receive a message. Click "Cancel" to cancel the export or "OK" to continue the export from the default version.

#### Defining the source and target languages in a project library

The selection of possible source and target languages in the project library depends on the languages you have defined as project languages.

You can find additional information here: [Select project languages](Editing%20project%20data.md#select-project-languages)

#### Defining the source and target languages in global libraries

In a global library you can define the library languages yourself unless the library has write protection.

You can display the selection of possible languages by double-clicking on the "Library languages" item in the "Languages & Resources" subfolder. For a write-protected library the library languages are displayed as read-only.

You can find additional information here: [Defining library languages](#defining-library-languages)

#### Requirement

Activate required target languages:

- For a project library in the project languages
- For a global library in the library languages

#### Exporting texts of library elements

To export the texts of the selected library elements, follow these steps:

1. Select the required library elements (individual library element, multiple library elements, a folder or a complete library).
2. Either right-click and select "Export library texts" from the shortcut menu or click the "Export library texts" button in the toolbar.

   The "Export" dialog box opens.

   ![Exporting texts of library elements](images/114687716363_DV_resource.Stream@PNG-en-US.png)

   ![Exporting texts of library elements](images/114687716363_DV_resource.Stream@PNG-en-US.png)
3. Select the required source language.
4. Select the required target language.

   Select the "Select all" check box if you want to export all target languages.
5. Give the export file the required name.
6. Set the required path to the storage location of the export file.
7. Click "Export".

#### Result

The export was successfully completed and the ".xlsx" file was created in the storage location.

![Result](images/96533588875_DV_resource.Stream@PNG-en-US.png)

Write the English translations in the "en-US" column, in order to be able to then import them.

### Importing library texts

#### Description

After external translation in a spreadsheet program, you import the texts into the TIA Portal. You can import the texts in the project library or a global library at the following locations:

- Using the "Import library texts" shortcut menu command
- Using the "Import library texts" button.

Regardless of how many library elements you have selected, all texts from the import file are imported for the entire library. The library elements from the import file must match the library elements of the library into which the texts are to be imported. The target languages you want to import must be enabled in the project or in the global library.

When you import texts for master copies, the existing texts are overwritten with the new texts. When you import texts for types, only the texts of the default version are overwritten with the new texts.

> **Note**
>
> **No import of library texts possible**
>
> No import of library texts possible if one of the following options applies:
>
> - The library texts belong to a type instance which is contained in a master copy.
> - A version of a type has not yet been released within the project library and has the extension "in test" or "in work".
> - The type version was edited after export of the library texts.
> - The global library is write-protected.
> - It is a system library.

> **Note**
>
> **Importing library texts for a multiuser project.**
>
> To also import library texts from objects that are not marked, the library texts in a multiuser project must be imported in the server project view.

#### Requirement

You have entered the translations in the target language in the export file.

![Requirement](images/96536270219_DV_resource.Stream@PNG-en-US.png)

If you want to import library texts into a project library, you must activate the required target languages in the project languages.

If you want to import library texts into a global library, you must activate the required target languages in the global library.

#### Importing all texts of a project library or a global library

To import all translated library texts, follow these steps:

1. Select the project library or a global library.
2. Either right-click and select "Import library texts" from the shortcut menu or click the "Import library texts" button in the toolbar.

   The "Import" dialog box opens.
3. Select the file to be imported.
4. You have the option to also import the source language by enabling the option "Import source language".
5. Click "Import".

   The "Import completed" dialog opens after the import.

#### Result

- Import completed successfully:

  The latest type version contains the translated texts after a successful import.
- Import completed with warnings:

  The reason for the error is either indicated directly in the dialog or you can click the link "Click here to view the log file" to view the causes of the error.
- Import failed:

  To find the log with the causes of the error, click the link "Click here to view the log file".

### Defining the project languages in the project library

All defined project languages are also available in the project library.

You can define and change the project languages centrally for the entire project library. In this case, all changes to the project languages affect all existing and newly created types and master copies in the project library.

However, you can also change the project languages for individual type versions without affecting the rest of the project library.

#### Defining the project language for the project library

1. Open or edit a type or master copy.
2. Open the "Tasks" card.
3. Under "Languages & resources" either select another project language from the existing editing languages or click "Add new editing language".
4. If you click "Add new editing language", the list of all available project languages will be displayed.
5. Select the editing language you want to use.

#### Defining a project language for a type version

1. Select the appropriate type version from the project library.
2. Select the command "Tools > Project languages" from the menu bar.

   Shows the list of all available project languages.
3. Select the editing language you want to use.

**Note**

The version must be in "In test" or "In work" state. The project language of a released version cannot be changed.

#### Result

The project library or the type version has the requested project or editing languages.

### Updating imported library tests for type instances

If you export texts of type versions and then import them to the same type version again, the changes made are not displayed in the type instances. Due to the same versions of the type and instance, for example V 0.0.1, no changes to the texts are detected on update of the project or the library.

#### Displaying texts from the project library in the project

You have the following options for displaying the changes from imported tests from the project library in the project:

- Delete the instance in the project and then create a new instance of the same version in the project using drag & drop. This procedure is necessary if you want to display imported texts in a different device or object in the project.
- Import the modified texts directly into the instances in the project. To do this, create test versions of the types in the project library. Export the texts of the test versions with the function "Export project texts" in the "Tools" menu. After you have changed the texts in the exported Microsoft Excel file, import the texts with the function "Import project texts" in the "Tools" menu.

#### Displaying imported texts from global libraries

You can display changes of imported texts from global libraries in the project library or in an instance in the project. For this, create a new version of the imported object, e.g. V 0.0.2. You have the following options for displaying the imported texts:

- To display the imported texts in the project library, update the project library. For this, open the shortcut menu of the object and select the menu entry "Update types > Library".
- To display the imported texts in the project, update the project. For this, open the shortcut menu of the object and select the menu entry "Update types > Project".

## Comparing libraries and library elements

This section contains information on the following topics:

- [Basics of comparing libraries and library elements](#basics-of-comparing-libraries-and-library-elements)
- [Perform detailed comparison of types and instances](#perform-detailed-comparison-of-types-and-instances)
- [Comparing devices and library elements in the compare editor](#comparing-devices-and-library-elements-in-the-compare-editor)
- [Comparing libraries in the compare editor](#comparing-libraries-in-the-compare-editor)

### Basics of comparing libraries and library elements

The TIA Portal provides several options to compare libraries or elements from libraries with one another, or with elements from the project. You can use the comparison options to determine possible differences and display them.

In principle, the following comparison methods are available:

- Detailed comparison

  In this comparison method, you can compare two types or two instances with one another. It is also possible to use a detailed comparison to compare a type with an instance. You can start the detailed comparison either in the project tree or in a library.
- Overview of the compare editor

  In this comparison method, you can compare a device with a library or with library elements. It is also possible to compare two libraries and their elements with other libraries in the compare editor, for example, the project library with a global library, or two global libraries with one another. You can start the compare editor either in the project tree or in a library, depending on the objects to be compared.

---

**See also**

[Perform detailed comparison of types and instances](#perform-detailed-comparison-of-types-and-instances)
  
[Comparing devices and library elements in the compare editor](#comparing-devices-and-library-elements-in-the-compare-editor)
  
[Comparing libraries in the compare editor](#comparing-libraries-in-the-compare-editor)

### Perform detailed comparison of types and instances

You can perform a detailed comparison for types and instances. You can start the detailed comparison either in the project tree or in a library. You can compare an instance with a type, a type with an instance or a type with different type. The compared versions of types and instances are opened beside each other in the compare editor and the differences are highlighted.

#### Starting detailed comparison in the project tree

To start a detailed comparison for an instance directly in the project tree, follow these steps:

1. Right-click the instance you want to compare in the project tree.
2. Select the command "Quick compare > Select as left object" in the shortcut menu.
3. In the project library or in a global library, right-click the type that you want to compare with the previously selected instance.
4. Select the command "Quick compare > Compare with <selected object>" in the shortcut menu. "<selected object>" stands for the left comparison object.

   The instance and its associated comparison partners are opened in their appropriate editors. The editors are arranged next to each other to provide you with a quick overview of the differences.

#### Starting detailed comparison in a library

To start a detailed comparison for a type directly in the project library or in a global library, follow these steps:

1. In the library, right-click the type that you want to compare.
2. Select the command "Quick compare > Select as left object" in the shortcut menu.
3. In a library or in an instance in the project tree, right-click a type that you want to compare with the previously selected type.
4. Select the command "Quick compare > Compare with <selected object>" in the shortcut menu. "<selected object>" stands for the left comparison object.

   The type and its associated comparison partners are opened in their appropriate editors. The editors are arranged next to each other to provide you with a quick overview of the differences.

---

**See also**

[Running a detailed comparison](Editing%20project%20data.md#running-a-detailed-comparison)

### Comparing devices and library elements in the compare editor

You can compare devices from libraries with devices from both the current project as well as from the same or another libraries or reference projects. Note, however, that reference projects are write-protected. You can also compare instances in a device with their type version in a library. Not all actions are available for the comparison with types. You cannot, for example, overwrite an instance of a newer version with an older type version from the library.

When comparing library elements, you can always switch between automatic and manual comparison. For some library elements, you can perform a detailed comparison. A quick comparison is also available.

#### Procedure

To compare library elements with the device data of a project, follow these steps:

1. In the project tree, select the device whose data you want to compare to a library element and which allows offline/offline comparison.
2. Select the "Compare > Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Open the "Libraries" task card.
4. Drag the project library, a global library or devices from the task card into the right drop area of the compare editor.

   You can identify the status of the objects based on the symbols in the status and action area. When you select an object, the object properties and the corresponding object of the assigned device are clearly shown in the property comparison.
5. If needed, start a detailed comparison of the elements which support the detailed comparison.

   See also: [Running a detailed comparison](Editing%20project%20data.md#running-a-detailed-comparison)

   Take into account any existing restrictions for specific elements. For information on this topic refer to the respective products.

You can drag other devices or libraries into the drop areas at any time to start a new comparison.

---

**See also**

[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  

  
[Using global libraries](#using-global-libraries)

### Comparing libraries in the compare editor

You can compare libraries and their elements with other libraries in the compare editor. You can compare the project library with a global library or two global libraries with each other and execute a variety of actions.

#### Procedure

To compare two libraries, follow these steps:

1. In the "Libraries" task card, select the project library or a global library.
2. Select the "Start comparison" command in the shortcut menu.

   The compare editor opens, and the selected library is displayed in the left area.
3. Drag-and-drop an additional library to the drop area of the right pane.
4. Open the "Types" folder.

   You can identify the status based on the symbols in the status and action area. You can define certain actions depending on the status of the objects. Note, however, that you can only perform actions in one direction in a synchronization action.

---

**See also**

[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)

## Filtering the display of library elements

To make it easier to keep track of a large number of library elements, you can use filters in the "Libraries" task card and in the library management.

Filter templates provide you with the option of limiting the displayed types.

The following filter templates are available in the "Libraries" task card and in the library management:

- Types with pending changes

  The filter displays all types that have a version "In test" or "In work".
- Released types

  The filter displays all released types that do not have versions "In test" or "In work".
- Types with multiple versions

  The filter displays all types that have more than one version.
- Types not used in the project

  The filter displays all types which have no instance in the project.
- Types with inconsistencies in the "default" version

  The filter displays all types whose default versions do not reference the default versions of the dependent types.
- Highest version of the type without "default" identifier.

  The filter displays the highest version of a type that does not have the "default" identifier.

The following filter templates are available in the "Libraries" task card for master copies:

- Documentation
- Devices & networks
- OPC UA communication
- PLC programming
- Visualization

The text filter records types and master copies and the library elements below them in the hierarchy.

The status filter records types according to their status.

### Requirement

The "Libraries" task card or the library management is opened.

### Using filter templates

To filter the view by filter templates, follow these steps:

1. Open the drop-down list box in the toolbar.
2. Under "Master copies", select the type of master copy you want to view.

   Master copies can only be displayed in the "Libraries" task card.
3. Under "Types", select the state of the types you want to view.
4. You can set the filter to "All" to return to an unfiltered view.

### Using text filters

To filter the view by text features, follow these steps:

1. Enter a search term in the search field in the "name" column.

   The text search can be applied to entries in the "Name" and "Version" columns.
2. To deactivate the text filter, click on the menu item "*" or clear the search field.

   To deactivate all filters, click the symbol ![Using text filters](images/141863621515_DV_resource.Stream@PNG-de-DE.png).

### Using status filters

To filter the view by status, follow these steps:

1. Open the drop-down list in the "Status" column.
2. Select a status.
3. To deactivate the status filter, click on the menu item "*".

   To deactivate all filters, click the symbol ![Using status filters](images/141863621515_DV_resource.Stream@PNG-de-DE.png).

### Result

The selected type of library elements and matching search hits are displayed. Filter templates, text filters and status filters can be combined.

If you use the text filter, library elements above the search hit in the hierarchy are displayed, and library elements below the search hit are hidden.

---

**See also**

[Library basics](#library-basics)
  
[Basics on master copies](#basics-on-master-copies)
  
[Basics on types](#basics-on-types)

## Creating folders in a library

The library elements are stored in the libraries according to their type in the "Types" and "Master copies" folders. Create additional folders below "Types" and "Master copies" to further organize master copies and types.

### Requirements

- The "Libraries" task card or the library management is opened.
- If you want to create new folders within a global library, you have to open the global library with write permission.

### Procedure

To create a new folder, follow these steps:

1. Right-click any folder within the library.
2. Select "Add folder" from the shortcut menu.

   A new folder is created.
3. Enter a name for the new folder.

---

**See also**

[Filtering the display of library elements](#filtering-the-display-of-library-elements)
  

  
[Working with types in the project library](#working-with-types-in-the-project-library)

## Editing library elements

Types, master copies and folder can be cut, copied, pasted, moved, renamed or deleted in the usual way within the "Libraries" task card. Global libraries must be opened with write permission for each of the above-described processes.

> **Note**
>
> **User-defined documentation for types and master copies**
>
> User-defined documentation is not affected by any of the operations within the library. If you move a master copy or a type to a different location, you also move the associated user-defined documentation in the file system to the corresponding location.
>
> For additional help on using the user-defined documentation, refer to the section "[Using user-defined documentation](Editing%20project%20data.md#using-user-defined-documentation)".

### Copying types

The following rules apply when you copy types to the clipboard:

- Types are always copied to the clipboard with all associated versions. However, only versions that have previously been released are copied.
- Types are always copied to the clipboard with all dependent elements.
- Master copies are always copied to the clipboard with all type versions used in them.

### Copying and pasting type versions

When you copy type versions to another library, the following rules apply:

- The types must already exist in the target library.
- The versions can be pasted independent of their version number and other properties if the GUID of the versions is different.

### Cutting elements

You can only paste previously cut library elements into the same library. In so doing, you can only paste master copies into the "Master copies" folder or any of its subfolders. Likewise, you can only paste types into the "Types" folder or any of its subfolders.

### Pasting types

The following rules apply when paste a type into a different library:

- A type is always pasted with all its versions.
- If the type already exists in the target library, all versions that are not yet available are added to the corresponding types in the target library.
- If there is already a version with released status in the target library, this version is not pasted again.
- If the same version exists with "In test" or "In work" status in the target library, it is replaced by the released version.
- If a type needs other types, these are also added at the respective location.

### Pasting master copies

When you paste master copies, all type versions contained in these copies are also pasted. If the corresponding types already exist in the library, only the missing versions are added to the individual types. If one of the types used does not yet exist, it is pasted at the highest level in the library. The type includes the type version that was used in the master copy.

### Moving elements

When you move an element from one library to another, the element is copied and not moved. The same rules apply as described under "Pasting types" and "Pasting master copies".

### Deleting of types and type versions

Note the following when you delete types or type versions:

- A type or a type version can only be deleted if there are no dependencies to other types.
- When you delete a type, all versions of the type are deleted.
- If you delete all versions of a type, the type is also deleted.
- If you delete a version that has instances in the project, the instances are also deleted from the project.
- If you delete a type that is also stored at the same time as a master copy, the master copy is also deleted.
- When you delete a default version and no additional versions of this type exist, the type is also deleted.
- When you want to delete a default version and other versions of this type exist, the "default" identifier must first be assigned to a different version. Default versions cannot be deleted if additional versions of the type exist.

### Deleting instances

If you delete an instance that has dependencies to other instances, this instance is restored during the next compilation. The instance is then linked again to the original type version. This restores the consistency of the project.

---

**See also**

[Library basics](#library-basics)
  
[Remove the link between instance and type](#remove-the-link-between-instance-and-type)
  
[Updating library with the types of another library](#updating-library-with-the-types-of-another-library)
  
[Conventions for the creation](Editing%20project%20data.md#conventions-for-the-creation)
  
[Using user-defined documentation](Editing%20project%20data.md#using-user-defined-documentation)
  
[Duplicating types](#duplicating-types)

## Harmonizing names and path structure

You can harmonize the project with a library. This helps you correct the following items:

- Names of the instances:

  Instances can be created during the development phase of a library, the names of which are appended by "_1", "_2", etc. due to an automatic correction. This extension is used to prevent duplicate names in the project. During harmonization, the instances once again receive the names of their associated types.
- Path structure:

  The original path structure can be lost due to parallel development or copying of dependent instances. This affects the clarity of the project. During harmonization, the path structure within the project is adapted to the path structure of the library.

### Procedure

To harmonize the names and the path structure, follow these steps:

1. Open the "Libraries" task card or the library management.
2. Click "Harmonize project" in the toolbar.

   The "Harmonize project" dialog box opens.
3. Select the device with which you wish to harmonize the library.
4. Select the "Harmonize paths between project and library" check box if you want to restore the path structure.
5. Select the "Harmonize names between project and library" check box if you want to have the names corrected.
6. Confirm your entries with "OK".

### Result

Depending on your settings, the names and the path structure in the project are harmonized with the library.

The changes to the project are logged. The log is available under "Common data > Logs" in the project navigation.

---

**See also**

[Library basics](#library-basics)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Using logs](Editing%20projects.md#using-logs)

## Clean up library

You can clean up the project library and the global libraries to remove types or versions that are not connected to any instance in the project. This step provides more clarity within the libraries and decreases the size of the library.

### Cleaning up the project library

To clean up the project library, follow these steps:

1. Open the "Libraries" task card or the library management.
2. Click on "Clean up library" in the toolbar.

   The "Clean up project library" dialog box opens.
3. Select the scope in which types or types versions are to be deleted:

   - To retain the default version even if it has no instance, select the option "Delete unused type versions without the "default" identifier".
   - Select the option "Delete complete types" to delete the complete type if no version is connected to an instance.
4. Confirm your entry with "OK".

   Depending on your selection, either unused type versions or types are removed from the project library.

   The changes are logged. The log is available under "Common data > Logs" in the project navigation.

### Clean up global library

To clean up a global library, follow these steps:

1. Open the global library in not write-protected mode.
2. Open the "Libraries" task card or the library management.
3. Click on "Clean up library" in the toolbar.

   The "Clean up global library" dialog box opens.
4. Click "OK".

   Unused type versions are deleted. The default version of a type is always retained.

   The changes are logged. The log is available in the "Common data > Logs" folder in the level below the global library.

---

**See also**

[Library basics](#library-basics)
  
[Overview of the library management](#overview-of-the-library-management)
  
[Using logs](Editing%20projects.md#using-logs)
  
[Displaying logs of global libraries](#displaying-logs-of-global-libraries)
