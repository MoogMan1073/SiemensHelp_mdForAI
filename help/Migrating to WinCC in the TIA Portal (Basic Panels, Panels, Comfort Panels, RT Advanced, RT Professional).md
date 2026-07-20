---
title: "Migrating to WinCC in the TIA Portal (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: UpdaterWCCPenUS
topics: 17
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating to WinCC in the TIA Portal (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [WinCC V7 (RT Professional)](#wincc-v7-rt-professional)
- [WinCC flexible (Basic Panels, Panels, Comfort Panels, RT Advanced)](#wincc-flexible-basic-panels-panels-comfort-panels-rt-advanced)

## Overview (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Overview of the section "Migration to WinCC in the TIA Portal"

SIMATIC WinCC offers a number of functional changes in the TIA Portal. Some functions differ from the functions that you know from familiar environments such as WinCC V7 or WinCC flexible.

This document provides an overview of the special functions and procedures in SIMATIC WinCC in the TIA Portal.

These functions and procedures are fundamentally different from the WinCC V7 and WinCC flexible version, or have a different name.

## WinCC V7 (RT Professional)

This section contains information on the following topics:

- [Actions (RT Professional)](#actions-rt-professional)
- [User objects (RT Professional)](#user-objects-rt-professional)
- [User administration (RT Professional)](#user-administration-rt-professional)
- [Direct connection (RT Professional)](#direct-connection-rt-professional)
- [Dynamic Wizard (RT Professional)](#dynamic-wizard-rt-professional)
- [Dynamics dialog (RT Professional)](#dynamics-dialog-rt-professional)
- [Working efficiently (RT Professional)](#working-efficiently-rt-professional)
- [Structures and structure tags (RT Professional)](#structures-and-structure-tags-rt-professional)

### Actions (RT Professional)

#### Actions in WinCC V7

WinCC supports the use of actions for dynamic response of the processes in your WinCC project. These actions are written in ANSI-C code. Actions are started by a trigger, i.e. a triggering event.

![Actions in WinCC V7](images/30516767243_DV_resource.Stream@PNG-en-US.png)

Actions can be used to run the following background tasks independent of the screen:

- Daily printout of a report
- Tag monitoring
- Calculations

#### How do I configure tasks with WinCC in the TIA Portal?

To configure tasks in the TIA Portal, the WinCC Scheduler is used.

You can use the Scheduler to configure tasks to run independent of the screen in the background. Actions are mapped to tasks of the function list type.

![How do I configure tasks with WinCC in the TIA Portal?](images/88841726987_DV_resource.Stream@PNG-en-US.png)

At each task, you configure exactly one function list which is processed line by line. Alternatively, you configure a C or VB script. To start the task, you define a trigger.

For more detailed information, see:

[Work area of the "Scheduler" editor](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#work-area-of-the-scheduler-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

[Example: Reading the current user name](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-reading-the-current-user-name-rt-professional)

---

**See also**

[Work area of the "Scheduler" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#work-area-of-the-scheduler-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Reading the current user name (RT Professional)](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-reading-the-current-user-name-rt-professional)

### User objects (RT Professional)

#### User objects in WinCC V7

Objects of the object pallet can be combined to form a group or user object based on a multiple selection. You can also insert a group or combined object into the project library.

![User objects in WinCC V7](images/30435710987_DV_resource.Stream@PNG-de-DE.png)

In contrast to a group, a user object enables the individual customization of properties and events that can be displayed and edited in the "Object properties" window. A user object can be edited in Graphics Designer, similar to an individual object of the object pallet.

![User objects in WinCC V7](images/76072025867_DV_resource.Stream@PNG-en-US..png)

#### How do I configure faceplates with WinCC in the TIA Portal?

Faceplates are used to create individually configured display and operating objects in WinCC. In contrast to user objects, faceplates can be modified centrally.

WinCC provides the "Faceplates" Editor within the project library for creating faceplates and editing their properties.

Faceplates are based on a type-instance model to support the centralized editing. You create central properties for a faceplate in the types. The instances represent local places of use for the types.

![How do I configure faceplates with WinCC in the TIA Portal?](images/88842393995_DV_resource.Stream@PNG-en-US.png)

For more detailed information, see:

[Basics on faceplates](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)

[Example: Configuring a faceplate](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### User administration (RT Professional)

#### User administration in WinCC V7

The "User Administrator" editor is used to set up and manage user administration.

The user administrator enables the setup and management of access rights for WinCC functions and WinCC users.

In the user administration, you can assign functions such as login timeout, or log in using a key switch / smart card to the users.

The "User Administrator" editor is used for engineering and in runtime.

![User administration in WinCC V7](images/128944149771_DV_resource.Stream@PNG-en-US.png)

#### How do I configure user administration with WinCC in TIA Portal?

- User administration in the engineering system

  You manage users, user groups and authorizations centrally in the WinCC user administration. You transfer users and user groups along with the project to the HMI device.

  Users are always assigned to a group and therefore inherit the group authorizations.

  ![How do I configure user administration with WinCC in TIA Portal?](images/122144375179_DV_resource.Stream@PNG-en-US.png)
- User administration in runtime

  You can employ a user view in a screen to manage users in runtime as well. You manage users and passwords directly in the user view on the HMI device.

  ![How do I configure user administration with WinCC in TIA Portal?](images/30450864907_DV_resource.Stream@PNG-de-DE.png)

For more detailed information, see:

[Form of the user administration](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#form-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

[User view](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#user-view-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Form of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#form-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User view (Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#user-view-panels-comfort-panels-rt-advanced-rt-professional)

### Direct connection (RT Professional)

#### Direct connections in WinCC V7

A direct connection is used to respond to events. Whenever this event occurs in runtime, the value of a source element is applied to a target element.

Example of the "Mouse click" event:

- The fill pattern of the "Rectangle1" object is synchronized with the fill pattern of the "Circle1" object.
- A screen change is executed.

  ![Direct connections in WinCC V7](images/76072278027_DV_resource.Stream@PNG-en-US..png)

#### How do I configure system functions with WinCC in the TIA Portal?

In WinCC, direct connections are mapped to system functions.

You use system functions in a function list or in a user-defined function. When the event occurs, execute the configured system functions using the function list.

When configuring a function list, select the system functions from a selection list that is sorted by categories.

For the implementation of the direct connection, specific functions are integrated, such as "SetPropertyByProperty".

![How do I configure system functions with WinCC in the TIA Portal?](images/88850891659_DV_resource.Stream@PNG-en-US.png)

For more detailed information, see:

[System functions](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

[Configuring a function list](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Dynamic Wizard (RT Professional)

#### Dynamic Wizard in WinCC V7

The Dynamic Wizard can be used to set up the dynamic response of an object by means of C-script actions. When a wizard runs, prepared C-script actions such as set bit/reset bit and trigger events are defined and saved in the object properties.

You can always edit the C-script actions in the Events tab of the object properties.

![Dynamic Wizard in WinCC V7](images/30515924235_DV_resource.Stream@PNG-en-US.png)

#### How do I configure system functions with WinCC in the TIA Portal?

In WinCC, objects are provided with dynamic properties, for example, using system functions.

You use system functions in a function list or in a user-defined function. When the event occurs, execute the configured system functions using the function list.

When configuring a function list, select the system functions from a selection list that is sorted by categories.

![How do I configure system functions with WinCC in the TIA Portal?](images/88853819659_DV_resource.Stream@PNG-en-US.png)

For more detailed information, see:

[System functions](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

[Configuring a function list](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Dynamics dialog (RT Professional)

#### Dynamic dialog in WinCC V7

The Dynamic dialog is used to configure dynamic object properties. In the Dynamic dialog, you formulate an expression by using tags, functions and arithmetic operators.

The value of the expression, the status, as well as the quality code of the tags used in the expression are used to generate the value of the object property in runtime.

![Dynamic dialog in WinCC V7](images/128962973451_DV_resource.Stream@PNG-en-US.png)

The Dynamic dialog is used, for example, for the following purposes:

- Mapping the range of values of a tag to colors.
- Monitoring of individual tag bits and mapping the bit value to colors or texts.
- Monitoring of a Boolean tag and mapping the tag value to colors or texts.
- Monitoring the status of a tag.
- Monitoring the quality code of a tag.

#### How do I configure animations with WinCC in TIA Portal?

Dynamic object properties can be realized, for example, using animations that you configure in the object property list, "Properties &gt; Animations".

These animations dynamically change the background color of an object, for example.

![How do I configure animations with WinCC in TIA Portal?](images/88855159947_DV_resource.Stream@PNG-en-US.png)

The function "Animate property" is of particular help to you when configuring dynamic properties for the dynamic dialog.

Simple animations are also possible via a tag connection at display and operating objects.

For more detailed information, see:

[Basics on dynamization in the property list](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-dynamization-in-the-property-list-rt-professional)

[Configuring a new animation](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Basics on dynamization in the property list (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-dynamization-in-the-property-list-rt-professional)
  
[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Working efficiently (RT Professional)

#### Mass data processing in WinCC V7

The WinCC Configuration Tool is an Excel add-in. The tool enables the simple configuration of mass data, such as tags.

![Mass data processing in WinCC V7](images/128945790603_DV_resource.Stream@PNG-en-US.png)

#### How do I work efficiently with WinCC in TIA Portal?

WinCC enables efficient processing of process data in table editors. WinCC provides the following corresponding functions:

- Importing and exporting project data

  ![How do I work efficiently with WinCC in TIA Portal?](images/30530837771_DV_resource.Stream@PNG-en-US.png)
- Multiple selection
- Global changes to a property

You export or import the following project data:

- Recipe data records
- Alarms
- Tags
- Text lists
- Project texts for translations

Exporting and importing reduces the workload.

Instead of creating new data records, use the data you have already created in previous projects.

For more detailed information, see:

[Data exchange between projects and external applications](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-exchange-between-projects-and-external-applications-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Data exchange between projects and external applications (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-exchange-between-projects-and-external-applications-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Structures and structure tags (RT Professional)

#### Structure tags in WinCC V7

Structures are used to enable grouping of a larger number of tags and tag types that form a logical unit.

In WinCC V7, you also create structures which you can address by their names at the tag.

![Structure tags in WinCC V7](images/128961184651_DV_resource.Stream@PNG-en-US.png)

#### How do I configure user data types with WinCC in TIA Portal?

In WinCC, user data types enable you to group different tags that form a logical unit.

You create user data types as a type and use instances of this type in the project.

User data types are project-specific data and are available for all HMI devices of the project.

You create user data types and user data type elements in the project library. User data types must be enabled before they can be used in the project.

The configured properties of a user data type are used in the instances of the user data type. If needed, you can change individual properties directly at the point of use, for example, at a tag. Changes to a property at the tag do not affect the user data type created.

![How do I configure user data types with WinCC in TIA Portal?](images/111987879691_DV_resource.Stream@PNG-en-US.png)

#### Checking tags

In order to determine whether a tag with the specified name exists, a check takes place at the point of use.

If the tag does not exist, the point of use is marked. The compiler does not output a warning.

If the tag name at the point of use begins with ".", no check takes place in the engineering system.

In this case, it is assumed that the name is formed for Runtime Professional from a tag prefix and the string at the point of use and therefore does not exist in the engineering system.

For user data types, the name of the instance of the user data type is typically used for the tag prefix. You use the name of the relevant user data type elements preceded by a period at the points of use in the screen.

For more detailed information, see:

[Basics on user data types](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)

## WinCC flexible (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Libraries (Basic Panels, Panels, Comfort Panels, RT Advanced)](#libraries-basic-panels-panels-comfort-panels-rt-advanced)
- [Screens and templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screens-and-templates-basic-panels-panels-comfort-panels-rt-advanced)
- [Scripts in faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#scripts-in-faceplates-basic-panels-panels-comfort-panels-rt-advanced)
- [Synchronization of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Special considerations for converting (Basic Panels, Panels, Comfort Panels, RT Advanced)](#special-considerations-for-converting-basic-panels-panels-comfort-panels-rt-advanced)

### Libraries (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Libraries in WinCC flexible

Libraries are a collection of pre-configured screen objects. They expand the number of available screen objects and increase engineering efficiency, because library objects are always available for reuse; there is no need to reconfigure them.

![Libraries in WinCC flexible](images/30642529035_DV_resource.Stream@PNG-en-US.png)

WinCC flexible enables you to create two library types:

- Project library
- Global library

A library can contain all the WinCC flexible objects, such as screens, tags, graphic objects, or alarms.

#### How do I configure libraries with WinCC in the TIA Portal?

In WinCC, you also configure the "Project library" and the "Global library".

You can no longer store any system functions in libraries, as was the case in WinCC flexible.

![How do I configure libraries with WinCC in the TIA Portal?](images/111988361099_DV_resource.Stream@PNG-en-US.png)

Both the "Project library" and the "Global library" contain the two folders, "Copy templates" and "Types". You can create or use the library objects as a copy template, or as a type.

- Copy templates

  Use copy templates to create independent copies of the library object.
- Types

  Create instances of objects of the "Types" folder and use the instances in your project. The instances are bound to their respective type. Changes to an instance also change all other instances. Types are marked by a green triangle in the "Libraries" task card.
- Managing the library objects

  You can only copy and move library objects within the same library.

For more detailed information, see:

[Libraries in WinCC](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#libraries-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Libraries in WinCC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#libraries-in-wincc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Screens and templates (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Screens and templates in WinCC flexible

In WinCC flexible, you create screens that an operator can use to control and monitor machines and plants. When you create your screens, the object templates provided support you in visualizing your plant, displaying processes and defining process values.

![Screens and templates in WinCC flexible](images/113388371211_DV_resource.Stream@PNG-en-US.png)

The project has a template for every HMI device. You can centrally configure the function keys and objects for your project in these templates.

Every screen based on this template will contain the function keys and objects that you configured in the template. Changes to an object or of a function key assignment in the template are applied to the object in all the screens, which are based on this template.

#### How do I configure screens and templates with WinCC in the TIA Portal?

In WinCC, you also configure "Templates" and a "Global screen" along with the "Screens".

You determine functions and objects in the template which then apply to all screens based on this template. You can create multiple templates in WinCC.

In the "Global screen", define the elements which are independent of the template used for all screens of an HMI device. The "Alarm window" and "Alarm indicator" objects are available for use as global objects. For HMI devices with function keys, configure the function keys in the "Global Screen" editor.

You can also configure a "System Diagnostics Window" in the global screen of Comfort Panels.

![How do I configure screens and templates with WinCC in the TIA Portal?](images/111988598411_DV_resource.Stream@PNG-en-US.png)

Excluding the controls, the screens are displayed in runtime in the following order:

![How do I configure screens and templates with WinCC in the TIA Portal?](images/53254180235_DV_resource.Stream@PNG-en-US.png)

For more detailed information, see:

[Screen basics](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#screen-basics-rt-professional)

---

**See also**

[Screen basics (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#screen-basics-rt-professional)

### Scripts in faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Scripts in faceplates in WinCC flexible

You configure a script in the "Scripts" tab of the "Faceplate configuration" dialog. This script is only available within the faceplate.

Interconnect the script directly to the events of the objects contained in the faceplate, for example, with the "Click" event of a button. If you use the faceplate in a screen, a faceplate instance is generated.

![Scripts in faceplates in WinCC flexible](images/1480953355_DV_resource.Stream@PNG-en-US.png)

#### How do I configure scripts in faceplates with WinCC in the TIA Portal?

In the configuration area of the "Faceplates" editor, you create scripts that you only use within a faceplate type.

In contrast to WinCC flexible, WinCC allows you to configure several scripts for a faceplate.

![How do I configure scripts in faceplates with WinCC in the TIA Portal?](images/33066681739_DV_resource.Stream@PNG-en-US.png)

### Synchronization of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### How do I configure a synchronization of recipes with WinCC in the TIA Portal?

You configure the synchronization of recipes in the "Recipes" editor in WinCC.

A few terms have changed in WinCC as compared to WinCC flexible.

**Synchronization for Panels and RT Advanced**

![How do I configure a synchronization of recipes with WinCC in the TIA Portal?](images/89028627211_DV_resource.Stream@PNG-en-US.png)

- To synchronize recipe tags that are configured in I/O fields with the recipe view in Runtime, activate "Synchronize recipe view and recipe tags".
- Deactivate "Direct transfer of individually modified values" to specify that the recipe tags are automatically transferred to the PLC when you edit the I/O fields (teach-in mode).
- Activate "Coordinated data transfer" to monitor the transfer of recipe data in Runtime using area pointers.

> **Note**
>
> If "Synchronization" &gt; "Synchronize recipe tags" is deactivated and "Show table" is deactivated in the recipe control under "Properties &gt; Table", then recipe data records cannot be sent to or from the PLC in the Runtime using the "Write to PLC" and "Read from PLC" buttons.

For more detailed information, see:

[Synchronization of recipe data records with the PLC](Working%20with%20recipes%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)

---

**See also**

[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20recipes%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)

### Special considerations for converting (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Project languages in WinCC

WinCC does not support all project languages that were available in WinCC flexible, such as Arabic. If you receive an empty project as the result of your migration, you may want to check the set editing language. Do not set the project languages that are not supported as editing language in the source project. Proceed as follows:

1. Open the project with WinCC flexible.
2. Change the editing language to English, for example.
3. Save the project.
4. Restart the migration.

#### Objects with object references in the project library

Two copying methods can be used in WinCC flexible.

- With "simple copy", a WinCC flexible screen including an IO field is copied, for example. Only the object name of a tag configured on the IO field is copied, as this is a reference.
- With "copy", a screen, an IO field contained there and a tag configured on the IO field together with its properties are copied.

These two methods can also be used for storing an object in a library. Project libraries and the objects contained there are migrated during migration and can be used in WinCC.

In WinCC, however, only one copying method is available. With regard to tags, it functions like "simple copy" in WinCC flexible. With regard to graphics, graphics lists and text lists, it functions like "copy" in WinCC flexible.

If you stored objects with references to tags in a library in WinCC flexible, you must reconfigure the referenced objects when using them in WinCC.

#### Changing the names of alarm classes

In contrast to WinCC flexible, the names of the predefined alarm classes are not dependent on the user interface language currently in use. During migration, the names of the alarm classes are assigned as follows:

| WinCC flexible | WinCC |
| --- | --- |
| Errors | Errors |
| System | System |
| Warnings | Warnings |

The display names of the alarm classes can be changed as necessary after migration.

#### Objects with object references in the project library

Two copying methods can be used in WinCC flexible.

- With "simple copy", a WinCC flexible screen including an IO field is copied, for example. Only the object name of a tag configured on the IO field is copied, as this is a reference.
- With "copy", a screen, an IO field contained there and a tag configured on the IO field together with its properties are copied.

These two methods can also be used for storing an object in a library. Project libraries and the objects contained there are migrated during migration and can be used in WinCC.

In WinCC, however, only one copying method is available. It functions like "simple copy" in WinCC flexible.

If you have stored objects with references to other objects in a library in WinCC flexible, you must reconfigure the referenced objects when using them in WinCC.
