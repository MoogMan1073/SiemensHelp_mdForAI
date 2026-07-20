---
title: "WinCC Unified (RT Unified)"
package: BasicsWCCUenUS
topics: 119
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Unified (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Additional documentation (RT Unified)](#additional-documentation-rt-unified)
- [Creating a user interface efficiently (RT Unified)](#creating-a-user-interface-efficiently-rt-unified)
- [Controlling with parameter sets (RT Unified)](#controlling-with-parameter-sets-rt-unified)
- [Using distributed systems (RT Unified)](#using-distributed-systems-rt-unified)
- [Dynamization and automation through scripts (RT Unified)](#dynamization-and-automation-through-scripts-rt-unified)
- [Central user management (RT Unified)](#central-user-management-rt-unified)
- [Connectivity (RT Unified)](#connectivity-rt-unified)
- [Logging and traceability (RT Unified)](#logging-and-traceability-rt-unified)
- [Configuring plant hierarchies (RT Unified)](#configuring-plant-hierarchies-rt-unified)
- [Working with libraries (RT Unified)](#working-with-libraries-rt-unified)
- [Using WinCC version compatibility (RT Unified)](#using-wincc-version-compatibility-rt-unified)
- [Using cross-references (RT Unified)](#using-cross-references-rt-unified)
- [Configuring cycles (RT Unified)](#configuring-cycles-rt-unified)
- [Configuring in multiple languages (RT Unified)](#configuring-in-multiple-languages-rt-unified)
- [Performance features (RT Unified)](#performance-features-rt-unified)

## Introduction (RT Unified)

WinCC Unified helps you meet the challenges of digitization in machine and plant construction. Based on native web technologies such as HTML5, SVG and JavaScript, you can work independently of devices and environment.

**An integrated system - from Panel to PC**

For you, this means being able to efficiently configure a large number of mobile end devices on one engineering platform, such as Unified Comfort Panels, Unified PCs, Control Centers or applications in View of Things. In this way, WinCC Unified combines the advantages of strong products like WinCC Advanced, WinCC Professional and WinCC Comfort in one software and offers you maximum flexibility, scalability and efficiency.

Overview of advantages of the uniform engineering system in the TIA Portal:

- Reuse of components on all WinCC Unified platforms
- End-to-end usability of UI controls
- Uncomplicated device replacement between all devices that work with WinCC Unified

![Figure](images/155270704523_DV_resource.Stream@PNG-en-US.png)

From the panel on the machine to the complex SCADA solution: WinCC Unified offers various options for industry-specific requirements and can be extended by user-specific applications through its open interfaces.

### What makes WinCC Unified so special?

WinCC Unified combines SIMATIC HMI and SCADA in one product. This means WinCC Unified users can configure runtimes for device types across classes with one engineering system. An engineering system that is installed on a Unified PC, for example, can be used to configure runtimes for Unified Comfort Panels and Unified PCs. WinCC Unified therefore offers tremendous scalability and flexibility in the use of device classes within a system or via remote access for distributed systems.

![What makes WinCC Unified so special?](images/155277271563_DV_resource.Stream@PNG-en-US.png)

## Additional documentation (RT Unified)

Siemens Industry Online Support will provide you with the latest documentation, which will help you with the initial working with and migrating to WinCC Unified.

### Getting Started

A guideline to getting started quickly with WinCC Unified is available online: [Getting Started](https://support.industry.siemens.com/cs/us/en/view/109801175).

### Guideline for migrating to WinCC Unified

You can get support for migrating to WinCC Unified here: [Guideline for migrating from Comfort Panel to Unified Comfort Panel and from WinCC Runtime Advanced to WinCC Unified PC Runtime](https://support.industry.siemens.com/cs/us/en/view/109768002).

Familiarize yourself with the differences between Comfort Panel/Runtime Advanced and Unified Comfort Panel/Unified PC Runtime. In addition, you will learn how you can migrate the essential elements (for example, pop-ups, slide-ins) to WinCC Unified.

### Data2Unified

Continue to use the project content you have created when you switch to SIMATIC WinCC Unified and save engineering time with the "Data2Unified" add-in.

Information and download are available from Industry Online Support: [Data2Unified](https://support.industry.siemens.com/cs/us/en/view/109770510)

The "Data2Unified" add-in is being continuously developed further (see the last change), so that even more TIA Portal project elements will be gradually supported.

The latest version of the add-in is provided for downloading in this contribution.

## Creating a user interface efficiently (RT Unified)

### "Screens" editor

With the Unified "Screens" editor, you can create user interfaces for various applications with a uniform structure. You will receive support particularly in the following areas:

- Operation and display in the "Screens" editor, e.g.:

  - Labeling of screen objects for direct editing
  - Display of catch lines
  - Drawing of lines and polygons
- Drag-and-drop, e.g.:

  - An IO field is created during drag-and-drop of tags into the "Screens" editor.
  - A parameter set control view is created during drag-and-drop of parameter set types.
- Changing properties of screen objects:

  - If multiple screen objects are selected, you can edit the properties at the same time.

Information on configuring screens can be found under "[Basics of screens](Configuring%20screens%20%28RT%20Unified%29.md#basics-of-screens-rt-unified)" and the following sections.

- [Configuring screen objects](Configuring%20screens%20%28RT%20Unified%29.md#configuring-screen-objects-rt-unified)
- [Configuring text lists and graphics lists](Configuring%20screens%20%28RT%20Unified%29.md#configuring-text-lists-and-graphics-lists-rt-unified)
- [Configuring dynamization](Configuring%20screens%20%28RT%20Unified%29.md#configuring-dynamization-rt-unified)

### Faceplates

Unified Faceplates are the new generation of HMI picture modules. Faceplates are user-defined groups of display and operating objects that can be reused as needed and thus reduce the configuration effort.

Faceplates are saved in a library and are managed there. The advantages of the type-instance concept are fully used. All functions that you are already familiar with from the library, such as updating of types, are supported.

You can create different versions of a faceplate type for use in screens or as a pop-up. Flexibly replace faceplate versions that are already in use with updated versions.

To connect the tags and interface properties defined in the faceplate individually to the process for each instance, use the different faceplate interfaces. For interface properties, use the pre-defined data types or the interface properties of the type "Configuration string" to assign the properties of each data type to a faceplate or the screen object in it using a script.

You can find more information under "[Configuring faceplates](Configuring%20screens%20%28RT%20Unified%29.md#configuring-faceplates-rt-unified)".

### Styles

WinCC Unified provides you with styles during the configuration to enable a user-friendly and flexible design of your runtime.

You can use these styles to easily customize the appearance of the runtime for each HMI device. While runtime is running, the style, for example, switches to a dark mode during a shift change.

You can find more information under "[Using styles](Configuring%20screens%20%28RT%20Unified%29.md#using-styles-rt-unified) ".

### Custom web controls

Custom web controls are independent web pages with an interface to Unified Runtime. Custom web controls offer you the option of adding your own elements to the visualization elements provided. Custom web controls thus extend usability and functionality to achieve an optimal visualization result.

Custom web controls are run on the web client and hosted in Runtime Unified. A custom web control can be displayed as an independent web page in any web browser and on any mobile end device.

You can find more information under "[Custom web controls](Programming%20Custom%20Web%20Controls%20%28RT%20Unified%29.md#custom-web-controls-rt-unified)" and in the following sections.

### Dynamic SVG graphics

You can use dynamic SVG graphics in WinCC Unified. The Siemens Graphic Library offers a large selection of dynamic SVG graphics in the "Dynamic widgets". You use these graphics to design screens for your runtime that you can then configure as needed.

![Dynamic SVG graphics](images/155305270795_DV_resource.Stream@PNG-de-DE.png)

You can find more information under "[Managing dynamic SVG graphics](Configuring%20screens%20%28RT%20Unified%29.md#managing-dynamic-svg-graphics-rt-unified)".

## Controlling with parameter sets (RT Unified)

A parameter set represents a recipe. Parameter sets are used for higher-level control.

Parameter sets are based on parameter set types which, in turn, are based on user data types. In this way you can achieve a high degree of reuse. Use the control "Parameter set control" to control the parameter set.

![Figure](images/159613801995_DV_resource.Stream@PNG-en-US.png)

Parameter set types support the nesting of complex data types. You can, for example, assign another user data type to a user-data-type element as the data type.

You can find more information under "[Configuring parameter sets](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#configuring-parameter-sets-rt-unified-1)".

## Using distributed systems (RT Unified)

WinCC Unified offers remote access options.

Unified Collaboration allows the cross-device display and operation of individual screens.

With the web client, runtime access is possible from any device.

### Unified Collaboration

With Unified Collaboration you can avoid redundant configuring. You have the option to create an overview with content from different Unified HMI devices. To this end, you access screens of a different HMI device across devices. You can display and operate screens of a different HMI device. Screen windows and alarms are supported here.

![Unified Collaboration](images/155301966475_DV_resource.Stream@PNG-de-DE.png)

An HMI device that participates in collaboration is referred to as a collaboration device.

Unified Collaboration is supported by Unified PC and Unified Comfort Panel and allows cross-project access.

You can find more information under "[Unified Collaboration](Using%20distributed%20systems%20%28RT%20Unified%29.md#unified-collaboration-rt-unified)".

### Web client

You use the web client to access a Unified PC or a Unified Comfort Panel via remote access. Access is possible from any device. The web client is used as standard remote access for Unified PC. The clients are independent of one another and independent of the locally displayed runtime. This means the runtime can be operated by multiple users simultaneously. To prevent overlaps and undesirable effects, we distinguish between synchronous and asynchronous functions.

![Web client](images/157586729739_DV_resource.Stream@PNG-de-DE.png)

You can find more information under "[Web Client](Using%20distributed%20systems%20%28RT%20Unified%29.md#web-client-rt-unified)".

## Dynamization and automation through scripts (RT Unified)

WinCC Unified provides a modern scripting environment that you can use to automate system components, such as the graphical runtime system. The scripting environment maps individual elements of the system components, such as the screens of the graphical runtime system, via the object model. The object model supports you in solving different tasks through runtime scripting and in controlling processes.

![Figure](images/155432509835_DV_resource.Stream@PNG-de-DE.png)

The scripting environment offers:

- Efficiency and the latest technologies

  The scripting environment supports Unicode and uses JavaScript (JS) as the scripting language. The scripting environment is object-oriented and offers asynchronous operations for high-performance and secure script execution.
- Support of mass data

  The scripting environment is optimized for the processing of mass data, for example, writing 1000 tags in one pass. Special script objects are available to this purpose that handle numerous HMI objects of the same type. These script objects execute operations on all the HMI objects simultaneously instead of processing each HMI object individually.
- Input support:

  - Syntax highlighting
  - Snippets (code templates)
  - Referencing HMI objects
  - Tooltips
  - Autocomplete
  - Error marking and correction
  - [System functions](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified)

You can find more information under "[Introduction to runtime scripting](Runtime%20scripting%20%28RT%20Unified%29.md#introduction-to-runtime-scripting-rt-unified)" and in the following sections.

Here you will find [Notes on creating scripts](Runtime%20scripting%20%28RT%20Unified%29.md#notes-on-creating-scripts-rt-unified), a description of the [Script editor](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified) and [examples of scripts](Runtime%20scripting%20%28RT%20Unified%29.md#examples-rt-unified).

In the SiePortal, your can find support for creating scripts in JavaScript: [Tips and tricks for creating scripts](https://support.industry.siemens.com/cs/ww/en/view/109758536).

## Central user management (RT Unified)

The user management of WinCC Unified allows for the plant-wide, central management of users including optional connection of Microsoft Active Directories. The user management forms the basis for the efficient and integrated management of personalized access rights in a plant. Security risks are significantly reduced. The person-specific assignment of roles and rights minimizes the maintenance effort. At the same time, a high level of transparency is achieved.

![Figure](images/155305279371_DV_resource.Stream@PNG-de-DE.png)

The User Management Component (UMC) option allows for the setup of a project-wide, central user management.

The user management of WinCC Unified offers:

- Central, cross-project management of user groups and users in a system.
- Import of user groups and users from Microsoft Active Directory.
- Failsafe performance thanks to redundant design of a User Management Control domain (UMC domain).
- Load distribution thanks to multiple UMC stations in one UMC domain.

You can find more information under "[User management in the TIA Portal](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#user-management-in-the-tia-portal-rt-unified)" and in the following sections.

## Connectivity (RT Unified)

WinCC Unified offers you the highest level of integration of SIMATIC PLCs. The TIA Portal of WinCC Unified offers you an easy connection of

- Up to 128 PLCs for Unified PC systems

  If more than 10 connections are used, SIMATIC NET PC software must be installed.

  A maximum of 16 connections is supported for Ethernet-based communication drivers of third-party providers. This number can be a combination of communication drivers or 16 individual communication drivers.
- Up to 16 PLCs for Unified Comfort Panel systems
- S7-1500 Software Controller
- S7-1200/1500
- S7-300/400
- Support of native 3<sup>rd</sup> party products via

  - Modbus TCP
  - Allen-Bradley EtherNet/IP
  - Mitsubishi
  - Omron
  - Support of additional products via the Channel Support Package

You can find more information under "[Basics of communication](Basics%20%28RT%20Unified%29.md#basics-of-communication-rt-unified)" and in the following sections.

### OPC UA

OPC UA is a standardized manufacturer-independent software interface for data exchange in automation engineering and is the technology succeeding OPC. OPC UA is platform-independent and supports different protocols as communication medium.

![OPC UA](images/152782252683_DV_resource.Stream@PNG-de-DE.png)

With WinCC Unified you can use OPC UA as connection standard for WinCC Unified PC and Unified Comfort Panels.

You can use WinCC Unified PCs and Unified Comfort Panels as needed:

- OPC UA DA server
- OPC UA DA client
- OPC UA A&C server

The WinCC Unified security concept guarantees your data security through secure OT/IT connections via OPC UA for connections to 3<sup>rd</sup> party applications.

You can find more information under "[WinCC Unified OPC UA server](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#wincc-unified-opc-ua-server-rt-unified)" and "[WinCC Unified OPC UA client](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#wincc-unified-opc-ua-client-rt-unified)".

## Logging and traceability (RT Unified)

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors such as the pharmaceutical industry, the food and beverage industry, and the related mechanical engineering industry.

![Figure](images/155360427659_DV_resource.Stream@PNG-de-DE.png)

Logging of production data in electronic form offers many advantages compared to paper documents, such as simple acquisition and logging of data. WinCC Unified supports the two database types Microsoft SQL and SQLite.

However, it is also important to ensure that data cannot be falsified and that it can be read at any time.

Therefore, sector-specific and cross-industry standards have been developed for the electronic documentation of production data. The most important set of regulations is the FDA Guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration.

In addition, different EU regulations apply, such as EU 178/2002, depending on the industry. Requirements for production systems in these industries have been developed based on 21 CFR Part 11 and the corresponding interpretation to comply with GMP (Good Manufacturing Practice). They are also required for other industries.

With WinCC Unified, you can configure projects in compliance with GMP and thus ensure traceability and data integrity.

WinCC Unified provides you with the optimal logging solution for each of your applications. You can start your application with file-based logging and extend it by a database option. File-based logging is especially suited for small and medium applications.

You can find more information under "[Log basics](Logging%20data%20%28RT%20Unified%29.md#log-basics-rt-unified)" and in the following sections.

Detailed descriptions can be found at "[Logging alarms](Configuring%20alarms%20%28RT%20Unified%29.md#logging-alarms-rt-unified)" and "[Logging tags](Configuring%20tags%20%28RT%20Unified%29.md#logging-tags-rt-unified)".

## Configuring plant hierarchies (RT Unified)

### Plant Model

WinCC Unified offers you object-oriented configuration. With the plant model, you can define reusable plant object types by arranging the associated plant object instances in hierarchical plant views.

![Plant Model](images/155384914571_DV_resource.Stream@PNG-de-DE.png)

In this way, you can model the technological hierarchy of your machine or unit/plant, for example, based on user-defined or standardized technology objects.

You create the plant structure from individual objects, each of which represents a component or a plant unit. Each object is configured in the context of the operator control and monitoring solution.

In plant object types, you combine all required configuration elements for visualization, e.g. faceplates, tags, alarms, scripts. Changes to the plant object type automatically affect all instances. This translates into significant time savings, especially for plants with a high degree of standardization.

If necessary, you can start object-oriented plant modeling based on the engineering data and derive the configuration of the HMI devices and automation systems from this.

Break the machine or unit/plant up into reusable technological units and arrange them hierarchically in a technological plant view according to the plant structure.

The following options are available to you in technology-oriented and object-oriented configuration:

- Creating various hierarchical plant views: technological view, building view, independent of the HMI device that is used.
- Configuration of plant objects and plant object types with data elements for mapping the actual plant configuration
- Access to plant objects (data elements, HMI alarms, logs, screens, etc.)
- Generation of the screen hierarchy
- Expansion of configured plant objects and types using Plant Intelligence options

You can find more information under "[Visualizing plant objects in runtime](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#visualizing-plant-objects-in-runtime-rt-unified)" and in the following sections.

### Plant Intelligence options

The Plant Intelligence options supplement the WinCC Unified visualization system with efficient functions:

- Calendar: For the visualization of structured planning of the production processes.

  You can find more information under "[Calendar Basics](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#basics-rt-unified)" and in the following sections.
- Performance Insight: For the calculation of individual Key Performance Indicators (KPIs) according to ISO standard 22400 and comprehensive selection of WinCC controls for their display and analysis.

  ![Plant Intelligence options](images/155386459275_DV_resource.Stream@PNG-de-DE.png)

  You can find more information under "[Basics of Performance Insight](Performance%20Insight%20-%20Optimizing%20processes%20with%20KPIs%20%28RT%20Unified%29.md#basics-rt-unified)" and in the following sections.
- Line Coordination: Automation of recipe-controlled and batch-controlled production processes.

  You can find more information under "[Introduction to Line Coordination (LCS)](Line%20Coordination%20and%20Sequence%20-%20Flexible%20handling%20of%20production%20processes%20%28RT%20Unified%29.md#introduction-to-line-coordination-lcs-rt-unified)" and in the following sections.
- Sequence: Fast and easy change of production processes and parameters without changing the PLC program.

  You can find more information under "[Introduction to Sequence (SES)](Line%20Coordination%20and%20Sequence%20-%20Flexible%20handling%20of%20production%20processes%20%28RT%20Unified%29.md#introduction-to-sequence-ses-rt-unified)" and in the following sections.

## Working with libraries (RT Unified)

This section contains information on the following topics:

- [Re-using libraries (RT Unified)](#re-using-libraries-rt-unified)
- [Basics on libraries (RT Unified)](#basics-on-libraries-rt-unified)
- [Types and master copies (RT Unified)](#types-and-master-copies-rt-unified)
- [Creating types and master copies (RT Unified)](#creating-types-and-master-copies-rt-unified)
- [Managing libraries (RT Unified)](#managing-libraries-rt-unified)
- [Managing objects in a library (RT Unified)](#managing-objects-in-a-library-rt-unified)
- [Using types and their versions (RT Unified)](#using-types-and-their-versions-rt-unified)
- [Using master copies (RT Unified)](#using-master-copies-rt-unified)

### Re-using libraries (RT Unified)

The object-oriented HMI concept of WinCC Unified allows you a high degree of reusability of elements both within and across projects. The new library concept contains the following elements that you can configure and reuse in your projects as needed:

- HMI Faceplates
- HMI user data types
- HMI styles
- HMI style sheets
- Graphics and dynamic SVG graphics
- Script modules

![Figure](images/159622118027_DV_resource.Stream@PNG-de-DE.png)

#### Types and instances

You can create instances from types that you have created in a library and which you manage and edit there. Use them in your project. The instances are linked to the respective type.

#### Master copies and copies

In addition, you can access many master copies for cross-project configurations in the global libraries. You can also yourself create master copies and manage them in the project library or in a global library that you have yourself created.

From a master copy, you can create an independent copy in the project, which you can edit independently of the underlying library object.

### Basics on libraries (RT Unified)

#### Introduction

Store all objects you need frequently in the libraries. An object that is stored in the library only has to be configured once. It can then be used repeatedly as often as required. Library objects extend the number of available screen objects and increase the effectiveness during configuration through multiple use.

Your WinCC software package is supplied with comprehensive libraries that contain, for example, "Motor" or "Valve" objects. You can also define library objects yourself.

Libraries are managed in the "Libraries" task card or in the library management. The following libraries are available:

- Project library
- Global libraries

![Introduction](images/149537177867_DV_resource.Stream@PNG-en-US.png)

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

- HMI Faceplates

  If you want to use configurable object groups several times in screens and change them centrally, create faceplates for them. If you change the properties of a faceplate in the library, the changes affect all screens and scripts that use this faceplate.
- HMI user data types
- HMI styles
- HMI style sheets
- Graphics and dynamic SVG graphics
- Script modules

Examples of master copies:

- Complete HMI device
- Screen
- Tag
- Parameter set type
- Script

### Types and master copies (RT Unified)

#### Introduction

Both the "Project library" and the "Global library" contain the two folders "Master copies" and "Types". You can create or use the library objects either as a master copy or a type.

#### Types

Create instances of objects of the "Types" folder and use these in your project. The instances are bound to their respective type.

More information is available [here](#using-types-and-their-versions-rt-unified).

#### Master copies

Use master copies to create independent copies of a library object.

More information is available [here](#using-master-copies-rt-unified).

#### Administration of the library objects

You can copy and move library objects to other libraries. You copy master copies to the "Master copies" folder or any subfolder of "Master copies". You can only insert types in the "Types" folder or any sub-folder of "Types".

### Creating types and master copies (RT Unified)

#### Creating a new type

You can create a new type in the project library.

You can later copy the type into a global library that you yourself have created.

1. To create a new type, select "Add new type" in the project library.

   The "Add new type" dialog is displayed.
2. Select the class of the type.
3. Provide further information on usage.

- or -

1. Drag and drop an object from the project tree to the "Types" folder in the project library.

   The object must be suitable for creating a type, for example, a user data type.

More information: [Using types and their versions](#using-types-and-their-versions-rt-unified)

#### Create a new master copy

1. To create a master copy, drag and drop an object from the project tree to the "Master copies" folder of the project library or a self-created global library.

   The object must be suitable for creating a type. You can use objects that you yourself have created in the project tree as a master copy.

   The cursor indicates if creating the master copy is possible.

   ![Create a new master copy](images/159648424331_DV_resource.Stream@PNG-de-DE.png)

More information: [Using master copies](#using-master-copies-rt-unified)

### Managing libraries (RT Unified)

This section contains information on the following topics:

- [Overview of the library management (RT Unified)](#overview-of-the-library-management-rt-unified)
- [Opening library management (RT Unified)](#opening-library-management-rt-unified)
- [Filtering types in the library management (RT Unified)](#filtering-types-in-the-library-management-rt-unified)
- [Creating a global library (RT Unified)](#creating-a-global-library-rt-unified)
- [Saving a Shared Library (RT Unified)](#saving-a-shared-library-rt-unified)
- [Opening a global library (RT Unified)](#opening-a-global-library-rt-unified)
- [Showing logs of global libraries (RT Unified)](#showing-logs-of-global-libraries-rt-unified)
- [Updating a project with the contents of a project library (RT Unified)](#updating-a-project-with-the-contents-of-a-project-library-rt-unified)
- [Updating a library with the contents of another library (RT Unified)](#updating-a-library-with-the-contents-of-another-library-rt-unified)
- [Exporting and importing library texts (RT Unified)](#exporting-and-importing-library-texts-rt-unified)

#### Overview of the library management (RT Unified)

##### Function of the library management

Master copies and types with dependencies on other library elements are subject to functional restrictions. For example, they cannot be deleted while dependencies still exist. This prevents other library elements from becoming useless. The library management is used to identify the dependencies and to create an overview of the work progress.

The library management offers the following functions:

- Display of the correlations of types and master copies

  If a type is referenced in other types or master copies, the relationships are displayed in the library management. You will also be able to see which library elements reference a type or a master copy.
- Display of points of use of types in the project
- Display all types that include a version with the "In test" or "In progress" status

##### Layout of the library management

The figure shows the library management, which consists of the following components:

- Toolbar of the library management
- "Types" area
- "Use" area

![Layout of the library management](images/152090976395_DV_resource.Stream@PNG-en-US.png)

##### Toolbar of the library management

You can perform the following tasks in the toolbar of the library management:

- Update view

  If the project was changed, you can update the view of the library management.
- Clean up library

  You can clean up the project library and global libraries. Cleaning up a library deletes all types and type versions that are not linked to any instance in the project.
- Harmonize project

  By harmonizing a project, you adapt the names and the path structures of type uses in the project to the corresponding names and path structures of the types within a library.
- Collapse all

  Shows only the top node
- Expand all

  Shows all nodes (types and versions)

##### "Types" area

The "Types" area displays the contents of the folder or type you selected in the "Libraries" task card.

The selection list following filters:

- Show all types
- Types with pending changes
- Released types
- Types with multiple versions
- Types not used in the project
- Types with inconsistencies in the default version
- Highest version of the type without "default" identifier.

For each type, the types that it references are displayed.

##### "Uses" area

The "Uses" area gives you an overview of the points of use of the selected types. The "Uses" area is divided into two tabs:

- "Uses in the project" tab

  In the "Uses in the project" tab, display the instances of type versions and the path to the point of use in the project.

  To get to the instance in the project, click the entry under "Path".
- "Uses in the library" tab

  The "Uses in the library" tab is used to show all points within the library at which a type is used.

#### Opening library management (RT Unified)

##### Procedure

To open the library management, follow these steps:

1. Open the "Libraries" task card.
2. Select a type or any folder that contains types.
3. Select the "Open library management" button ![Procedure](images/149431843723_DV_resource.Stream@PNG-de-DE.png).

   - or -
4. In the shortcut menu, select "Library management element".

##### Result

The library management opens and the types are displayed with their versions.

##### Working with large or multiple monitors

The library management window can be detached and moved as desired.

#### Filtering types in the library management (RT Unified)

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
3. Select "Types with pending changes" in the drop-down list.

   The "Types" area only displays types that have the "in progress" status.

##### Filter by released types

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Released types" in the drop-down list.

   The "Types" area only displays types that have released versions.

##### Filtering for types with multiple versions

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types with multiple versions" in the drop-down list.

   The "Types" area only displays types that have more than one version.

##### Filtering for types that have no instances in the project

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types not used in project" in the drop-down list.

   The "Types" area only displays types that have no instances in the project.

##### Filtering by types with inconsistencies in the default version

1. Select the "Types" folder in the project library.
2. Open the library management.
3. Select "Types with inconsistencies in the default version" in the drop-down list.

   Only the types whose default version is inconsistent are displayed in the "Types" area.

##### Filter by types whose highest version is not the default version

1. Select the "Types" folder in the project library.
2. Open the library management.
3. In the drop-down list, select "Highest version of the type without default identifier".

   In the "Types" area, only those types are displayed whose highest version is not the default version.

#### Creating a global library (RT Unified)

##### Introduction

In the libraries you store the configured objects that you want to use several times in your configuration. To use objects in several projects, create a global library.

##### Requirement

- A project is open.
- The "Libraries" task card is opened.

##### Procedure

1. Click the ![Procedure](images/14162763531_DV_resource.Stream@PNG-de-DE.png) icon under "Global library".

   The "Create new global library" dialog opens.

   ![Procedure](images/149577997707_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/149577997707_DV_resource.Stream@PNG-en-US.png)
2. Enter a name.
3. Select the path where the new library is to be stored.
4. Click "Create".

##### Result

The new library is shown in the "Global libraries" palette. The global library contains the "Types", "Master copies" and "Common data" folders. Under "Common data" you can reports for the global library.

A folder with the name of the global library is created in the file system at the storage location of the global library. This actual library file is given the file name extension ".alxx", whereby "xx" stands for the current WinCC version number.

#### Saving a Shared Library (RT Unified)

##### Introduction

A global library is saved as a separate file. This file contains all the objects of the global library, including the referenced objects. For example, the reference of a tag which was configured on an I/O field is also saved in the library.

WinCC prompts you to save the global libraries when you close WinCC or your project without saving. You also can store the global library during configuration, without storing the entire project.

##### Requirement

- A project with at least one global library is open.
- The "Libraries" task card is opened.
- A global library has been changed.

##### Procedure

1. Select the global library that you want to save.
2. Click the ![Procedure](images/25535164043_DV_resource.Stream@PNG-de-DE.png) icon in the "Global library" palette.

   You can alternatively select the "Save Library" command in the shortcut menu.

Save as:

1. To save the global library to another folder, select "Save as" from the shortcut menu.
2. Select the path in which you want to store the new library and enter a file name.

##### Result

The global library is saved under the current file name or the newly assigned file name.

#### Opening a global library (RT Unified)

##### Introduction

In WinCC, the global libraries are stored in separate files. You can use a global library in every project.

##### Requirement

- You have saved a global library.
- A project is open.
- The "Libraries" task card is opened.

##### Procedure

1. Click the ![Procedure](images/70981237771_DV_resource.Stream@PNG-de-DE.png) icon in the "Global library" palette.

   The "Open global library" dialog box is displayed.
2. Select the path in which the library is stored.
3. Click "Open".

**Note**

To have the access to a global library from multiple projects, open the global library in write-protected mode. When a global library is read-only, access from other projects is blocked.

##### Result

The global library is displayed in the "Global libraries" palette.

#### Showing logs of global libraries (RT Unified)

Logs listing all changes made to the global library are created when global libraries are updated. The logs are stored together with the global library and are always available once you have opened the global library.

##### Procedure

To open the logs of a global library, follow these steps:

1. Open the global library in the "Libraries" task card.
2. Open "Common data > Logs" in the lower-level folder.
3. Double-click on a log.

   The log is opened in the editor.

#### Updating a project with the contents of a project library (RT Unified)

##### Introduction

After you have edited several types in the project library, update all instances in the project to the most recent version of the types from the project library.

Each of the following elements can be selected as source for the update:

- Individual folders within a library
- Individual types

##### Requirement

The "Libraries" task card or the library management is opened.

##### Procedure

1. Select a folder within the project library or individual types.
2. Select "Update types > Project..." from the shortcut menu.

   A dialog opens.
3. Select either the entire project or individual devices for the update.
4. Select "Update instances in project".
5. To delete all older versions of the updated types from the project library, select the check box "Delete unused type versions without "default" identifier from the library".
6. Confirm with "OK".

##### Result

All instances of the types are updated in the project to the most recent version of the selected types in the project library.

You can find a log of the update process in the project tree under "Common data".

#### Updating a library with the contents of another library (RT Unified)

The following options are available for updating libraries:

- Updating a global library with types from another global library
- Updating the project library with types from a global library

Each of the following elements can be selected as source for the update:

- Individual folders within a library
- Individual types

##### Requirement

- The "Libraries" task card or the library management is opened.

##### Procedure

To update a library with the contents of a different library, follow these steps:

1. Select a folder within the library or individual types.
2. Right-click the source and select the "Update types > Library..." command from the shortcut menu.

   The "Update library" dialog box opens.
3. Select the type of library you want to update:

   - Select "Update project library" to update the project library with types from a global library.
   - Select "Update global library" if you want to update a global library.
4. Optional: Select the global library you want to update from the drop-down list.
5. Enable the desired update options:

   - Updating instances in the project
   - Delete unused type versions without "Default" label from the library
   - Force update

     Types are updated including their dependent types regardless of their version number.
6. Confirm with "OK".

##### Result

- Types not yet available in the target library are supplemented there with all their versions. More recent versions are added to the types that already exist in the target library.

  If a more recent version of a type already exists in the target library, the latest version is nevertheless copied from the source library and automatically assigned a newer version number.
- A log listing all performed changes to the target library is created for the update process.

  If you have updated the project library, you can find the log in the project tree under "Common data > Logs".

  If you have updated a global library, you can find the log in the "Common data > Logs" folder in the level below the global library.

#### Exporting and importing library texts (RT Unified)

##### Introduction

You can export the texts of the library objects to an .xlsx file to edit them in MS Excel, for example, or export them for compilation.

You export and import texts of the following objects in the library:

- Individual library types and master copies
- Multiple library types and master copies
- All library objects of the project library or a global library

After editing or external compilation, you import the texts into the TIA Portal.

When the texts are imported, all texts from the import file are imported for the entire library, even if you have only selected one library object. The target languages of the import file must be activated in the project.

During import to a master copy, the texts of the template are overwritten in the library with the new texts from the import file. During import of the texts to a library type, the latest version is overwritten in the library with the new texts from the import file. If a version of a type has not been released yet in a project library, no texts can be imported for the entire project library.

##### Defining the source language and target language

You define the source language and target language for export of the texts in the Export dialog. The selection of available languages depends on the project languages defined.

With the global library, the selection of available source and target language depends on the languages defined by the creator of the library. To see the available languages of the global library, double-click the entry "Library languages" in the project folder "Language and Resources" of the library in question.

##### Exporting texts

To export the texts of a single or several library objects, follow these steps:

1. Open the project library or a global library.
2. Select the library object in the library.
3. Select the command "Export library texts" in the shortcut menu of the object.

   Alternatively, click the ![Exporting texts](images/152091872011_DV_resource.Stream@PNG-de-DE.png) "Export library texts" button in the toolbar.

   The "Export" dialog box opens.
4. Select the source language and the target language for export in the dialog.
5. Enter the name and path for the export file.

   ![Exporting texts](images/152092117515_DV_resource.Stream@PNG-en-US.png)
6. Click "Export".  
   After successful export, the export file is stored under the specified path.

##### Importing texts

> **Note**
>
> **Restrictions for text import**
>
> The texts which belong to the following library objects cannot be imported:
>
> - Type instances which are contained in a master copy
> - Library types whose versions have not yet been released and which have the status "In progress" or "In test"
> - Write-protected global library
>
> If importing into a project library, all versions must be released in this project library.

To import the texts after editing or compilation into the TIA Portal again, follow these steps:

1. Open the project library or the global library.
2. Select the command "Import library texts" in the shortcut menu of the object.

   Alternatively, click the ![Importing texts](images/152091879563_DV_resource.Stream@PNG-de-DE.PNG) "Import library texts" button in the toolbar.

   The "Import" dialog box opens.
3. Select the path and the name of the import file from the "Select file for import" field.

   Activate the "Import source language" check box if you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes.
4. Click on "Import".

### Managing objects in a library (RT Unified)

This section contains information on the following topics:

- [Displaying library objects (RT Unified)](#displaying-library-objects-rt-unified)
- [Storing an object as master copy (RT Unified)](#storing-an-object-as-master-copy-rt-unified)
- [Inserting a library object (RT Unified)](#inserting-a-library-object-rt-unified)

#### Displaying library objects (RT Unified)

##### Introduction

The elements of a library can be displayed in the folder structure under the library or in the "Elements" palette.

##### Requirement

- At least one library object has been created in a library.
- The "Libraries" task card is opened.

##### Displaying parts of the library objects

| 1. Select the folder of a library whose elements are to be displayed. 2. Click ![Displaying parts of the library objects](images/14161014411_DV_resource.Stream@PNG-de-DE.png).    The objects contained are displayed in the "Elements" palette. 3. To display components of an element, click on an element in the "Elements" palette.    The parts of the element are displayed in the "Elements" palette.               ![Displaying parts of the library objects](images/152092160139_DV_resource.Stream@PNG-en-US.png)         ![Displaying parts of the library objects](images/152092160139_DV_resource.Stream@PNG-en-US.png) 4. Select a view:       | Icon | View |    | --- | --- |    | ![Displaying parts of the library objects](images/14161806219_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161806219_DV_resource.Stream@PNG-de-DE.png) | Details mode |    | ![Displaying parts of the library objects](images/14161567627_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161567627_DV_resource.Stream@PNG-de-DE.png) | List mode |    | ![Displaying parts of the library objects](images/14161559691_DV_resource.Stream@PNG-de-DE.png)      ![Displaying parts of the library objects](images/14161559691_DV_resource.Stream@PNG-de-DE.png) | Overview with icons | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The library objects are displayed with the selected view in the "Elements" palette.

#### Storing an object as master copy (RT Unified)

##### Introduction

In libraries you can store WinCC objects, e.g. screens, tags, alarms, scripts or parameter set types as master copies. To do this, drag and drop the object from the project tree, the work area or the detail view into the library. If you have created subfolders in the library, you can also insert an object directly there.

##### Requirement

- The project tree or the work area is open.
- An object has been created.
- The "Libraries" task card is displayed.

##### Procedure

1. Select the object in the project tree or in the work area.
2. Drag and drop the object into the "Master copies" folder in the library.

   The mouse pointer is transformed into a crosshair with an appended object icon.

   ![Procedure](images/152092481291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/152092481291_DV_resource.Stream@PNG-en-US.png)

**Note**

**Objects from the project tree as master copy**

You can use all objects as master copy, which you can create new in the project tree:

- HMI devices, PLCs, technology objects, ...
- Screens
- Tag tables
- Parameter set types
- Scripts

**Note**

**Objects from a work area as master copy**

You can use objects as master copy, which you can create new in a work area:

- Tags
- HMI alarms
- Tasks
- Cycles
- Text and graphic lists

##### Result

The object is saved to the library for further use in multiple instances of your configuration.

![Result](images/97192066443_DV_resource.Stream@PNG-en-US.png)

#### Inserting a library object (RT Unified)

##### Introduction

The system always assigns the inserted library object a name which consists of the name of the object type and of a consecutive number.

If the inserted object already exists, you have the option of replacing the object or of saving it under a new name.

You cannot insert library objects that are not supported by the HMI device.

> **Note**
>
> If you insert a screen with interconnected template from the library, the template will also be inserted. An existing, suitable template is not used.

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

### Using types and their versions (RT Unified)

This section contains information on the following topics:

- [Status of versions of a type (RT Unified)](#status-of-versions-of-a-type-rt-unified)
- [Adding types to a project library (RT Unified)](#adding-types-to-a-project-library-rt-unified)
- [Create a new version of a type (RT Unified)](#create-a-new-version-of-a-type-rt-unified)
- [Editing a type (RT Unified)](#editing-a-type-rt-unified)
- [Consistency status of types (RT Unified)](#consistency-status-of-types-rt-unified)
- [Generating a faceplate as a type (RT Unified)](#generating-a-faceplate-as-a-type-rt-unified)
- [Generating a HMI user data type as type (RT Unified)](#generating-a-hmi-user-data-type-as-type-rt-unified)
- [Generating HMI user data type from PLC data type (RT Unified)](#generating-hmi-user-data-type-from-plc-data-type-rt-unified)
- [Creating a graphic and dynamic SVG as type (RT Unified)](#creating-a-graphic-and-dynamic-svg-as-type-rt-unified)
- [Editing dynamic SVG type (RT Unified)](#editing-dynamic-svg-type-rt-unified)
- [Creating a script module as a type (RT Unified)](#creating-a-script-module-as-a-type-rt-unified)

#### Status of versions of a type (RT Unified)

##### Introduction

Depending on the point of use, the version of a type has different states.

##### Released version

The "Released version" status is available for all types, regardless of the point of use.

If you want to edit a released version, you must first create a new test version or an "in progress" version.

Released type versions of scripts and screens can be opened and viewed at their instance.

##### "In progress" version

When you create a new type or a new version of a released type, the type is set to the "In progress" state.

Types with the "in progress" state can be edited in the library management without the need for a reference to an instance in the project. Upon release, the compatibility of the type is tested by a consistency check.

##### "In test" version

Versions of HMI user data types can be in the "in test" state.

If you create a new PLC data type and add it as HMI user data type to a library, then this type is set to the "In test" state during editing. Select a device as the test environment before opening the editor for the type.

A version with "In test" status is linked to an instance in the project. You can set only one version to "In test" for each type at a given time.

An "In test" version may only be linked to a single instance in the project. Therefore, it is not possible to copy an instance to the clipboard, to duplicate it or to create an additional type from the instance as long as it has "In test" status.

#### Adding types to a project library (RT Unified)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card or the library management is opened.

##### Procedure

1. In the "Project Library" palette, select a folder that contains types

   - or -

   Open a folder from the project library that contains types in the library management.
2. Select "Add new type..." from the shortcut menu.

   - or -

   Click "Add new type" in the "Project library" palette.

   The "Add new type" dialog is displayed.
3. Select the type.
4. Specify the device for which the type is being created.
5. Click "OK".

   Depending on the selected type, the editor for editing the type opens.
6. Close the note at the top of the window and edit the type.
7. Release the version of the type after the editing.

##### Result

You have added a type to the project library.

#### Create a new version of a type (RT Unified)

If you create a new version of a type, the point of use of the type determines the status of the newly created version.

##### Requirement

- The "Libraries" task card is opened.
- A type has been created and released.

##### Procedure

1. Select the released type.
2. Select "Edit type" from the shortcut menu.

##### Result

- A new version of the type is created.
- The version of a type has the state "In progress".

  - or -

  The version of an HMI user data type has the state "In test".
- The editor opens.

#### Editing a type (RT Unified)

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

#### Consistency status of types (RT Unified)

Types may no longer be consistent after changes. The "Status" column in libraries indicates whether a type is consistent or inconsistent. The following statuses are displayed:

| Icon | Meaning |
| --- | --- |
| ![Figure](images/140596194443_DV_resource.Stream@PNG-de-DE.png) | The type is consistent. |
| ![Figure](images/140613088011_DV_resource.Stream@PNG-de-DE.png) | The type has more than one inconsistency. |
| ![Figure](images/140613459339_DV_resource.Stream@PNG-de-DE.png) | The default version of the type does not use the default version of its dependent type. |
| ![Figure](images/143118756363_DV_resource.Stream@PNG-de-DE.png) | The type has duplicate versions. |
| ![Figure](images/143118760075_DV_resource.Stream@PNG-de-DE.png) | More than one version of the type is instantiated in the device. |
| ![Figure](images/143118763787_DV_resource.Stream@PNG-de-DE.png) | A version other than the default version of the type is instantiated in the device. |

#### Generating a faceplate as a type (RT Unified)

##### Introduction

To define a new faceplate type, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "HMI faceplate".
4. Specify the device for the new type.
5. Assign a descriptive name to the new faceplate type.

##### Result

The new faceplate type is created and displayed under the selected name in the project library.

The faceplate type is assigned the status "In progress" and the version 0.0.1.

The editor for a faceplate opens.

##### Using a faceplate type

- Open a screen to edit.
- Drag and drop the type from the "Libraries" task card into the screen.

  A faceplate container is created.

#### Generating a HMI user data type as type (RT Unified)

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

![Result](images/152221551499_DV_resource.Stream@PNG-de-DE.png)

The new HMI user data type is created and displayed under the selected name in the project library.

The user data type is assigned the status "In progress" and the version 0.0.1.

The editor for the user data type opens.

##### Using an HMI user data type

The released default version of the type is available in the tag tables for HMI tags as data type for internal tags.

#### Generating HMI user data type from PLC data type (RT Unified)

##### Introduction

To create a new HMI user data type based on a PLC data type, add a PLC data type in the project library.

##### Requirement

- A PLC is created in the project.
- A PLC data type with at least one element is configured.

##### Procedure

1. Navigate in the project tree to the PLC and here to the "PLC data types" node.
2. Drag and drop the PLC data type node to the "Types folder" in the project library.
3. In the "Add type" dialog you specify the properties of the new type.

##### Result

![Result](images/152221542923_DV_resource.Stream@PNG-de-DE.png)

The new HMI user data type is created and displayed under the selected name in the project library.

The User data type is assigned the status "Released" and the version 0.0.1.

##### Editing HMI user data type based on PLC data type

1. Select "Edit type" in the shortcut menu of the type.

   This can be occur in the project tree or in the "Libraries" task card.
2. To open the editor for editing, you must set a test environment.

   The version is in the "In test" state and can be edited.
3. Release the version after editing.

##### Using an HMI user data type

- To use the PLC data type stored in the library at another PLC, drag and drop the node from the library to the "PLC data types" node of a PLC in the project tree.

  > **Note**
  >
  > PLC data types can only be instantiated at PLCs of the same type.

  The PLC data type is available as data type in the tag tables for PLC tags.

The new HMI user data type can be stored in a global library.

#### Creating a graphic and dynamic SVG as type (RT Unified)

##### Introduction

To define a new graphic type or define a dynamic SVG as a type, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   A dialog opens.
3. Select "Graphic/Dynamic SVG".

   ![Procedure](images/159225063307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159225063307_DV_resource.Stream@PNG-en-US.png)
4. Select whether you are adding a graphic or a dynamic SVG as type.

##### Result

The new type is created and displayed in the project library. The type is assigned the status "In progress" and the version 0.0.1.

For graphics, the [editor for graphics](#project-graphics-editor-rt-unified) opens.

For dynamic SVG graphics, the [editor for dynamic SVG graphics](#editing-dynamic-svg-type-rt-unified) opens and a dynamic standard SVG is displayed.

Graphics and dynamic SVGs can be instantiated in screens and faceplates.

#### Editing dynamic SVG type (RT Unified)

Create dynamic SVGs as type to be able to exchange and update SVGs conveniently.

The type instance concept is implemented for dynamic SVGs. The selection of the dynamic SVG is defined in the type, and the dynamization of the properties takes place at the instance.

A type contains exactly one dynamic SVG.

Dynamic SVGs are language-neutral.

In contrast to using SVGs from the "Graphics" task card, using types in faceplates allows different SVGs with the same name in one faceplate.

> **Note**
>
> **Version compatibility of dynamic SVG types**
>
> Dynamic SVG types have been introduced with WinCC Unified V18. They cannot be used with faceplates < V18. They cannot be used with device versions or project versions < V16.
>
> If you load a project that uses an instance of a dynamic SVG type in a faceplate into a Runtime V17, this results in an error during loading.

> **Note**
>
> **Faceplates and dynamic SVGs**
>
> If you create a faceplate type from a group of selected screen objects, dynamic SVGs are not included. To insert a dynamic SVG into a faceplate, open the faceplate type in the editor and insert the SVG from the library here.

> **Note**
>
> **Manual assignment of a type version**
>
> If you manually assign a type version to a dynamic SVG type or rename the type, a DELTA download is no longer possible.

##### Introduction

After a new type is created, a dynamic standard SVG is displayed. You replace this SVG with the SVG you need.

No properties are displayed for the standard SVG.

To replace an SVG that has already been created or edit its properties, open the type in the editor.

##### Procedure

1. To replace the dynamic standard SVG or the SVG of the previous version, select "Replace with other dynamic SVG" in the shortcut menu of the SVG.

   Other shortcut menu options are not available in V18.
2. Select a dynamic SVG in the file system.

   The existing SVG is replaced by the SVG you selected.

   For an instance of the dynamic SVG type, the properties are displayed in the Inspector window of the "Screens" editor or "Faceplate types". It is possible to dynamize properties here.

If the selected SVG cannot be fully displayed in the visible area of the screen, scroll bars will be displayed so that the view can be shifted horizontally and vertically.

If you select a file that does not contain a valid dynamic SVG, an error message is output in the Inspector window.

##### Release version

1. To release the version of the type, open the note at the top.

   ![Release version](images/149594229387_DV_resource.Stream@PNG-de-DE.png)
2. When releasing the type, enable the "Set dependent types to edit mode" option.

   Faceplate types in which the dynamic SVG is used are set to edit mode and thus use the current version of the dynamic SVG.

##### Notes on dynamization

- The dynamization of properties, e.g. color, affects the instance, not the type.
- The dynamization of properties is retentive if the new SVG has the same properties as the previous version when the type is changed.

  If the properties of the new SVG differ from the previous version, default values are used. In this case, no dynamization is specified.
- When a type is instantiated in a screen, the "Contained type - name" property in the Inspector panel under "Properties > Miscellaneous" shows the name and version of the instantiated type.

#### Creating a script module as a type (RT Unified)

##### Introduction

To define a new script module type, add a new type in the project library.

##### Procedure

1. Open the "Libraries" task card.
2. Select the "Add new type" command under "Types" in the shortcut menu of the project library.

   The "Add new type" dialog opens.
3. Select "Script module".
4. Define the lowest device version.

##### Result

The new script module type is created and displayed in the project library.

The script module type is assigned the status "In progress" and the version 0.0.1.

The editor for a script module opens.

##### Working with script modules

In the editor for script modules, you create functions in which you can define parameters. You select these functions when dynamizing screens, screen images or tasks via events in the function list. If you change or delete functions or parameters in the script module type, the referenced functions will be adapted automatically.

To check the syntax, click on ![Working with script modules](images/160610527627_DV_resource.Stream@PNG-de-DE.png) "Syntax check" in the editor.

Error messages that allow you to analyze the script are displayed in the Inspector window under "Info > Compile".

When creating scripts, you are supported by snippets that you access from the shortcut menu under "Snippets" and which contain logic blocks for the following groups:

- Faceplate
- HMIRuntime
- Logic

---

**See also**

["Scripts" editor (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified)

### Using master copies (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Using a script as a master copy (RT Unified)](#using-a-script-as-a-master-copy-rt-unified)
- [Using a screen as a master copy (RT Unified)](#using-a-screen-as-a-master-copy-rt-unified)

#### Basics (RT Unified)

You can save objects that you have created in the project tree as a master copy in a library. Based on the master copy, you can create a new object in the project tree.

Master copies allow you to efficiently create the same or similar objects. By using master copies in a global library, these objects can be used in other projects.

##### Basics

You can use all objects as master copy, which you can create new in the project tree:

- HMI devices, PLCs, technology objects, ...

  and the objects contained in these objects, e.g. cams
- Screens
- Tag tables
- Parameter set types
- Scripts

You can use objects as master copy, which you can create new in a work area:

- Tags
- HMI alarms
- Tasks
- Cycles
- Text and graphic lists

Objects can be added as a master copy in the project library or in an open global library.

##### Basic procedure

Once you have used this method to create and edit an object that you want to use it as a master copy, drag and drop it onto the "Master copy" folder in a library.

Then drag and drop the master copy back into the project tree to create a new object that you can further customize.

#### Using a script as a master copy (RT Unified)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is opened.

##### Procedure

You can store a global module, a global definition area or a function as a master copy.

1. Open the "Scripts" editor in the project tree.
2. Drag and drop a script into the "Master copies" folder of a library.

##### Result

You have created a master copy from a script in the library.

##### Using a master copy

1. Drag and drop the master copy from the library into the "Scripts" folder in the project tree.

   A new script is created.
2. Edit the script.

#### Using a screen as a master copy (RT Unified)

##### Requirement

- A project is open.
- An HMI device has been created and opened.
- The project tree is open.
- The "Libraries" task card is opened.

##### Procedure

1. Open the "Screens" editor in the project tree.
2. Drag and drop the screen into the "Master copies" folder of a library.

##### Result

In a library you have created a master copy from a screen.

##### Using a master copy

1. Drag and drop the master copy from the library into the "Screens" folder in the project tree.

   A new screen has been created.
2. Edit the screen.

## Using WinCC version compatibility (RT Unified)

This section contains information on the following topics:

- [Basics on version compatibility (RT Unified)](#basics-on-version-compatibility-rt-unified)
- [Upgrade project (RT Unified)](#upgrade-project-rt-unified)
- [Devices not fully supported (RT Unified)](#devices-not-fully-supported-rt-unified)
- [Unsupported devices (RT Unified)](#unsupported-devices-rt-unified)
- [Matching objects after upgrading (RT Unified)](#matching-objects-after-upgrading-rt-unified)
- [Replacing the configured HMI device (RT Unified)](#replacing-the-configured-hmi-device-rt-unified)
- [Upgrading a global library](#upgrading-a-global-library)
- [Changing the configured runtime version](#changing-the-configured-runtime-version)
- [Upgrading the installed Runtime version of a device (RT Unified)](#upgrading-the-installed-runtime-version-of-a-device-rt-unified)
- [Replacing a device (RT Unified)](#replacing-a-device-rt-unified)

### Basics on version compatibility (RT Unified)

This section contains information on the following topics:

- [Basics on version compatibility (RT Unified)](#basics-on-version-compatibility-rt-unified-1)
- [Installed Runtime version for Unified Comfort Panel (RT Unified)](#installed-runtime-version-for-unified-comfort-panel-rt-unified)
- [Installed Runtime version for Unified PC (RT Unified)](#installed-runtime-version-for-unified-pc-rt-unified)
- [Use cases (RT Unified)](#use-cases-rt-unified)

#### Basics on version compatibility (RT Unified)

##### Introduction

The interaction of the following versions is of importance for version compatibility:

- WinCC version
- Project version
- Configured Runtime version
- Installed Runtime version

##### WinCC version

The WinCC version is the WinCC version installed on the configuration PC for TIA Portal, for example, WinCC Unified V18.

![WinCC version](images/159648434187_DV_resource.Stream@PNG-en-US.png)

The installed version is displayed under "Help > Installed software …".

##### Project version

The project version is the version of a WinCC project.

- When you create a new WinCC project, the project version is always the same as the WinCC version.
- A project successfully opened in WinCC Unified always has the version of the software used. Projects with older versions are automatically upgraded at the time of opening.
- An existing project can have a project version that is older than the WinCC version.

  You can make out the version of a project from the file ending of the project file.

  ![Project version](images/159655963019_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> To open a WinCC project that was created with an older version of TIA Portal, you must first upgrade its project version to the WinCC version of the currently installed TIA Portal.
>
> After the upgrade, the functions of the current WinCC version are available in the project. You can then open, edit, save, compile, download or simulate the project.
>
> You can find additional information at [Upgrade project](#upgrade-project-rt-unified).
>
> If the project version cannot be changed, open the project in a TIA Portal whose WinCC version is the same as the project version. There, you edit, save, compile, download or simulate the project.

##### Configured Runtime version

The configured Runtime version is the version of the runtime configured in a WinCC project for an HMI device.

A WinCC project can contain HMI devices with differently configured Runtime versions. HMI devices whose configured Runtime version is older than the current version can be restricted in their functions when compared to the HMI devices with the current version.

The configured Runtime version must be compatible with the Runtime version installed on the target device for the project to be downloaded.

When you add a new HMI device to a WinCC project, its pre-selected, configured Runtime version is always the highest available Runtime version.

To add a new device with an older version, select the desired version in the "Add new device" dialog.

You can change the configured Runtime version in the "Devices & Networks" editor or the device properties in the project tree.

![Configured Runtime version](images/159657520395_DV_resource.Stream@PNG-en-US.png)

You can find additional information at [Changing the configured runtime version](#changing-the-configured-runtime-version).

##### Installed Runtime version

The installed Runtime version is the version of Runtime installed on the HMI device. The version is displayed on the HMI device. You can find information on this in the documentation of the hardware.

An installed Runtime version V18 or higher supports backward compatibility up to V17.

You can find more information about the installed Runtime version under:

- [Installed Runtime version for Unified Comfort Panel](#installed-runtime-version-for-unified-comfort-panel-rt-unified)
- [Installed Runtime version for Unified PC](#installed-runtime-version-for-unified-pc-rt-unified)

##### Version compatibility

The following diagram shows the interaction of the different versions:

![Version compatibility](images/159652284555_DV_resource.Stream@PNG-en-US.png)

When downloading to a target device, make sure that the configured and the installed Runtime versions are compatible.

TIA Portal checks the compatibility during the download. The following applies when incompatible versions are detected:

- Unified Comfort Panel: In the "Load preview" dialog, you are given the option to install an image with a compatible version on the Panel.

  You can find additional information at [Basics for downloading projects](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-for-downloading-projects-rt-unified).
- Unified PC: Download is not possible

> **Note**
>
> When loading from an external storage medium, compatibility is checked while you load the project to the device (Unified PC).

##### Simulation

With an installed Runtime as of version V17, backward compatibility is also supported for simulations.

You can simulate Runtime projects with a configured Runtime version of V16 onwards.

#### Installed Runtime version for Unified Comfort Panel (RT Unified)

> **Note**
>
> **Changing the installed Runtime version deletes all data on the Unified Comfort Panel**
>
> When an image is installed, the data on the Unified Comfort Panel is deleted.
>
> Back up the following data before you install an image.
>
> - Database for the tag persistence
> - Data logs
> - Alarm logs
> - Parameter sets

For Unified Comfort Panels, the operating system and the runtime are bundled into one image with a device version that can be transferred to the HMI device if necessary. The device version determines which version of the operating system and Runtime can be installed with the image.

The Runtime version installed with the image on the Unified Comfort Panel must be compatible with the configured Runtime version for the project to be downloaded.

> **Note**
>
> **Installing image with compatible version**
>
> There are several ways to install an image with a compatible version:
>
> - When TIA Portal detects an incompatible runtime version during online loading, you have the option in the "Load Preview" dialog to install an image with a compatible, installed Runtime version on the Unified Comfort Panel before the download.
>
>   You can find additional information at [Basics for downloading projects](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-for-downloading-projects-rt-unified).
> - Independent of the download, you have the following options for installing an image:
>
>   - [Updating the operating system of the HMI device](Compiling%20and%20loading%20%28RT%20Unified%29.md#updating-the-operating-system-of-the-hmi-device-rt-unified)
>   - [Updating the operating system of the HMI device from a data storage medium](Compiling%20and%20loading%20%28RT%20Unified%29.md#updating-the-operating-system-of-the-hmi-device-from-a-data-storage-medium)

##### Backwards compatibility

HMI devices starting from the installed Runtime version V17 are backward compatible. Runtime projects with a configured Runtime version V16 or higher can run on them.

> **Note**
>
> **Conversion of the logging data with backward compatibility**
>
> When a project is started for the first time in runtime in the backward compatibility mode, its logging data is adapted to the new database schema. This process is irreversible.
>
> Example:   
> A project with configured Runtime V17 is loaded to a device on which Runtime V18 is installed. During the project start, the logging data is adapted to match the database schema of V18. You can no longer transfer the log to a device with Runtime V17 and run it there.

---

**See also**

[Basics on version compatibility (RT Unified)](#basics-on-version-compatibility-rt-unified-1)
  
[Basics for downloading projects (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-for-downloading-projects-rt-unified)
  
[Updating the operating system of the HMI device (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#updating-the-operating-system-of-the-hmi-device-rt-unified)
  
[Updating the operating system of the HMI device from a data storage medium](Compiling%20and%20loading%20%28RT%20Unified%29.md#updating-the-operating-system-of-the-hmi-device-from-a-data-storage-medium)

#### Installed Runtime version for Unified PC (RT Unified)

For Unified PC, the operating system and Runtime are installed independently of each other. The installed Runtime version must be compatible with the configured Runtime version.

##### Backwards compatibility

HMI devices starting from the installed Runtime version V17 are backward compatible. Runtime projects with a configured Runtime version V16 or higher can run on them.

> **Note**
>
> **Conversion of the logging data with backward compatibility**
>
> When a project is started for the first time in runtime in the backward compatibility mode, its logging data is adapted to the new database schema. This process is irreversible.
>
> Example:
>
> A project with configured Runtime V17 is loaded to a device on which Runtime V18 is installed. During the project start, the logging data is adapted to match the database schema of V18. You can no longer transfer the log to a device with Runtime V17 and run it there.

---

**See also**

[Basics on version compatibility (RT Unified)](#basics-on-version-compatibility-rt-unified-1)

#### Use cases (RT Unified)

##### Introduction

When commissioning a plant, the following versions are usually identical:

- WinCC version
- Project version
- Configured Runtime version
- Installed Runtime version

If you want to replace an HMI device or expand your system, the versions can differ. In such cases, WinCC version compatibility helps you to continue operating your plant with as little modification work as possible.

##### Example: Replacing the HMI device

Your system contains a Unified Comfort Panel with an installed Runtime version V17.

You want to replace this Unified Comfort Panel with another Unified Comfort Panel with an already preinstalled Runtime version V18. Nothing should be changed in the configuration.

To be able to download your Runtime project V18 to the HMI device, use the backwards compatibility.

More information can be found in the section [Replacing a Unified Comfort Panel](#replacing-a-unified-comfort-panel-rt-unified).

##### Example: Expanding an existing system with an HMI device with an installed Runtime version

You want to expand your system with a Unified Comfort Panel with an installed Runtime version V17.

You are already using WinCC V18 on your configuration PC.

To use the HMI device, follow these steps:

1. Upgrade the project version.
2. Configure a Unified Comfort Panel V17 in the Engineering System.
3. Compile and download the Runtime project to the Unified Comfort Panel with an installed Runtime version V17.

##### Example: Expanding an existing system with an HMI device with a later Runtime version installed

You want to expand your system with a Unified Comfort Panel with an installed Runtime version V18 and use the functionalities of the current version.

You are using WinCC V17 on your configuration PC.

To use the HMI device, follow these steps:

1. Install WinCC V18 on your configuration PC.
2. Upgrade the project version.
3. Configure a Unified Comfort Panel V18 in the Engineering System.
4. Compile and download the Runtime project to the Unified Comfort Panel with an installed Runtime version V18.

##### Example: Upgrading an HMI device

Your system contains a Unified PC with an installed Runtime version V16 or V17.

You want to use the functionalities of the current version on the Unified PC.

You can find additional information at [Upgrading a Unified PC](#upgrading-a-unified-pc-rt-unified).

---

**See also**

[Replacing a Unified Comfort Panel (RT Unified)](#replacing-a-unified-comfort-panel-rt-unified)
  
[Upgrading a Unified PC (RT Unified)](#upgrading-a-unified-pc-rt-unified)
  
[Upgrading a Unified Comfort Panel (RT Unified)](#upgrading-a-unified-comfort-panel-rt-unified)
  
[Replacing a Unified PC (RT Unified)](#replacing-a-unified-pc-rt-unified)

### Upgrade project (RT Unified)

#### Introduction

To open a WinCC project that was created with an older version of the Engineering System, you must first upgrade the project version to the WinCC version of the currently opened Engineering System.

#### Requirements

- The project version is a predecessor of your WinCC version.

  > **Note**
  >
  > **No version skips**
  >
  > You cannot skip any version when upgrading. A project with version V16 must first be upgraded in a TIA Portal version V17 before you can upgrade it in a TIA Portal version V18 to the current version.
- You have write access to your project drive.
- The project drive has sufficient storage capacity for another project of this size.

#### Procedure

To upgrade a project from TIA Portal V17 or higher to your WinCC version, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open Project" dialog box opens and the list of recently used projects is displayed.
2. Select a project from the list and click "Open".
3. If the project is not included in the list, click the "Browse" button. Navigate to the project folder and open the project file.

   The "Open Project" dialog opens.
4. Click "Upgrade".

   ![Procedure](images/159659220363_DV_resource.Stream@PNG-en-US.png)

   The project is upgraded to the current project version and opened. The procedure can take time, depending on the number of devices and objects used in the project.

   > **Note**
   >
   > **Unsupported devices**
   >
   > If there are devices in the project that are not supported by the current version, an upgrade is not possible.
   >
   > Open the project in the version of the TIA Portal in which it was created, and remove the unsupported devices or replace them with supported devices.
   >
   > More information: [Unsupported devices](#unsupported-devices-rt-unified)

   > **Note**
   >
   > **Devices not fully supported**
   >
   > If devices are configured in the project that are only partially supported, an upgrade is possible.
   >
   > In the upgraded project, replace the devices with fully supported devices.
   >
   > More information: [Devices not fully supported](#devices-not-fully-supported-rt-unified)
5. Check whether devices and library objects have to be adapted to the new version.

#### Result

- The content of the old WinCC project is saved in a new project with the current project version.

  The original project is not overwritten and can still be edited with a compatible older version of the TIA Portal.
- You can open, edit, save, compile, download or simulate the project.
- All functions of the current WinCC version are available in the project.
- If necessary, match the Runtime version of the HMI devices.

---

**See also**

[Upgrading the installed Runtime version of a device (RT Unified)](#upgrading-the-installed-runtime-version-of-a-device-rt-unified)

### Devices not fully supported (RT Unified)

#### Error during upgrade

If a project contains devices or device versions that are no longer fully supported in the current version of WinCC, the project can be upgraded to the current version of WinCC.

Unsupported devices may be present in a project in the following locations:

- Devices in the project tree
- Devices in the master copies of the project library

Devices that are no longer fully supported are flagged with a symbol:![Error during upgrade](images/159233723403_DV_resource.Stream@PNG-de-DE.png)

If you compile a device that is no longer complete, you get an error message:

- The device is not supported. Compilation is therefore not possible. Please switch to a supported device.
- The Runtime version is not supported. Compilation is therefore not possible. Switch to a supported version.

#### Changing the device type or the device version in the project tree

To change the device type or the device version of a device in the project tree, follow these steps:

1. Select the "Change device/version" command in the shortcut menu of the outdated device.
2. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.

#### Devices and device versions not fully supported

| Symbol | Meaning |
| --- | --- |
| KTP400 Basic 2nd Generation | 15.0.0.0 |
| KTP700 Basic 2nd Generation | 15.0.0.0 |
| KTP900 Basic 2nd Generation | 15.0.0.0 |
| KTP1200 Basic 2nd Generation | 15.0.0.0 |
| KTP400F Mobile | 15.0.0.0 |
| KTP700 Mobile | 15.0.0.0 |
| KTP700F Mobile | 15.0.0.0 |
| KTP900 Mobile | 15.0.0.0 |
| KTP900F Mobile | 15.0.0.0 |
| Mobile Panel 177 |  |
| Mobile Panel 277 |  |
| KP400 Comfort | 15.0.0.0 |
| KP700 Comfort | 15.0.0.0 |
| KP900 Comfort | 15.0.0.0 |
| KP1200 Comfort | 15.0.0.0 |
| KP1500 Comfort | 15.0.0.0 |
| KP1500 Comfort V2 | 15.0.0.0 |
| KTP400 Comfort | 15.0.0.0 |
| TP700 Comfort | 15.0.0.0 |
| TP700 Comfort INOX PCT |  |
| TP700 Comfort Outdoor | 15.0.0.0 |
| TP900 Comfort | 15.0.0.0 |
| TP900 Comfort INOX PCT | 15.0.0.0 |
| TP1200 Comfort | 15.0.0.0 |
| TP1200 Comfort INOX PCT | 15.0.0.0 |
| TP1200 Comfort PRO | 15.0.0.0 |
| TP1500 Comfort | 15.0.0.0 |
| TP1500 Comfort Outdoor | 15.0.0.0 |
| TP1500 Comfort V2 | 15.0.0.0 |
| TP1900 Comfort PRO | 15.0.0.0 |
| TP2200 Comfort | 15.0.0.0 |
| TP2200 Comfort V2 | 15.0.0.0 |

You can find detailed compatibility lists of all HMI devices using the [compatibility tool](https://support.industry.siemens.com/cs/ww/en/view/64847781).

### Unsupported devices (RT Unified)

#### Error during upgrade

If a project contains devices or device versions that are no longer supported in the current version of WinCC, upgrading is not possible. To upgrade the project to the current version, you need to open the project in an older version of WinCC and change the device type or version to a value supported by the current version of WinCC.

Devices that are no longer supported are identified with a symbol: ![Error during upgrade](images/159233723403_DV_resource.Stream@PNG-de-DE.png)

Unsupported devices may be present in a project in the following locations:

- Devices in the project tree
- Devices in the master copies of the project library

#### Changing the device type or the device version in the project tree

To change the device type or the device version of a device in the project tree, follow these steps:

1. Select the "Change device/version" command in the shortcut menu of the outdated device.
2. In the "Change device" dialog, select as new device a device or device version that is supported in the current version.

#### Changing the device type or device version in the library

To change the device type or the device version of a device in the project library, follow these steps:

1. Search for the outdated device in the master copies of the project library.
2. Copy the master copy from the project library to the project tree.
3. Make a note of the name of the master copy. Delete the master copy in the project library.
4. Select the "Change device/version" command in the shortcut menu of the outdated device.
5. In the "Change device" dialog, select as new device a device or device version that is supported in the current version of WinCC.
6. Create a new master copy of the project library from this device.
7. Give the new master copy the same name as the deleted master copy.

#### Devices and device versions not supported

| Symbol | Meaning |
| --- | --- |
| KTP400 Basic 2nd Generation | 13.0.0.0, 14.0.0.0 |
| KTP700 Basic 2nd Generation | 13.0.0.0, 14.0.0.0 |
| KTP900 Basic 2nd Generation | 13.0.0.0, 14.0.0.0 |
| KTP1200 Basic 2nd Generation | 13.0.0.0, 14.0.0.0 |
| KTP400F Mobile | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP700 Mobile | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP700F Mobile | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP900 Mobile | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KTP900F Mobile | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| Mobile Panel 177 | 11.0.0.0, 12.0.0.0 |
| Mobile Panel 277 | 11.0.0.0, 12.0.0.0 |
| KP400 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP700 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP900 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP1200 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| KP1500 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| KP1500 Comfort V2 | 11.0.0.0, 12.0.0.0 |
| KTP400 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP700 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP700 Comfort INOX PCT | 11.0.0.0, 12.0.0.0 |
| TP700 Comfort Outdoor | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP900 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP900 Comfort INOX PCT | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1200 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 14.0.0.0 |
| TP1200 Comfort INOX PCT | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1200 Comfort PRO | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1500 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| TP1500 Comfort Outdoor | 11.0.0.0, 12.0.0.0, 14.0.0.0 |
| TP1500 Comfort V2 | 11.0.0.0, 12.0.0.0 |
| TP1900 Comfort PRO | 11.0.0.0, 12.0.0.0 |
| TP2200 Comfort | 11.0.0.0, 12.0.0.0, 13.0.0.0, 13.0.1.0, 14.0.0.0 |
| TP2200 Comfort V2 | 11.0.0.0, 12.0.0.0 |
| WinCC Runtime Advanced | 11.0.0.0, 12.0.0.0 |

You can find detailed compatibility lists of all HMI devices using the [compatibility tool](https://support.industry.siemens.com/cs/ww/en/view/64847781).

### Matching objects after upgrading (RT Unified)

After the successful upgrading of a project, you must match the versions of individual devices and objects if required.

#### Matching devices after upgrading

1. In the project tree for a device, in the shortcut menu, select "Replace device ....".
2. Check whether the device is available in a newer version.

   ![Matching devices after upgrading](images/159712904587_DV_resource.Stream@PNG-en-US.png)

   More information:

   - [Replacing the configured HMI device](#replacing-the-configured-hmi-device-rt-unified)
   - [Replacing a device](#replacing-a-device-rt-unified)
3. Then compile each device in the project.

   > **Note**
   >
   > **Sequence of compilation**
   >
   > Compile the PLCs first and then the HMI devices in your project. In this way, you ensure that the controller data required to compile the HMI devices is available.

#### Upgrading global libraries

1. Open a global library that was created with an older version of the TIA Portal.

   The "Open Library" dialog is displayed.

   ![Upgrading global libraries](images/159739013899_DV_resource.Stream@PNG-en-US.png)
2. Click "Upgrade".

   The library is upgraded and saved as a new global library with the appendage "_V18".

   The library of the predecessor version is retained.

   ![Upgrading global libraries](images/159744361867_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Upgrading a global library](#upgrading-a-global-library)

### Replacing the configured HMI device (RT Unified)

This section contains information on the following topics:

- [Basics for replacing the configured HMI device (RT Unified)](#basics-for-replacing-the-configured-hmi-device-rt-unified)
- [Replacing the configured HMI device (RT Unified)](#replacing-the-configured-hmi-device-rt-unified-1)
- [Adapting the configuration of the connection (RT Unified)](#adapting-the-configuration-of-the-connection-rt-unified)

#### Basics for replacing the configured HMI device (RT Unified)

##### Introduction

When you replace the devices, you can use existing configurations for your new HMI devices.

For example, you replace a Unified PC for a Unified Comfort Panel or a 7" Unified Comfort Panel for a 12" Unified Comfort Panel.

All data configured by you is retained in the configuration data. This means you do not need to copy individual objects of one device and paste them to another.

> **Note**
>
> When you replace a Unified Comfort Panel and select a PC station as your new device, for example, WinCC Unified PC RT is automatically moved below the PC Station in the project tree.

##### Adjusting the screen size

If the new device supports a different resolution than the previous device when you replace a device, adjust the screen size.

##### Customizing a connection

When you have configured a connection to a PLC and are replacing the HMI device with a different device type, error messages may occur, for example "The object 'IE general' is not supported in the new configuration and will be removed".

This may happen, for example, when you replace a Unified PC with a Unified Comfort Panel because the configured communications module is not supported after the exchange.

Therefore, check the configured connections and make adaptations if necessary.

---

**See also**

[Basics on version compatibility (RT Unified)](#basics-on-version-compatibility-rt-unified-1)

#### Replacing the configured HMI device (RT Unified)

##### Requirement

- A project has been created and opened.
- A Unified PC or a Unified Comfort Panel is used in the project.
- The screens have been adapted.

##### Procedure

To replace an HMI device with another HMI device, follow these steps:

1. In the project tree, select the HMI device to be replaced.

   Alternatively, select the HMI device to be exchanged in the "Devices & Networks" editor.
2. Depending on the device, select "Change device / version" or "Change device" from the shortcut menu.

   The "Change device" dialog opens.
3. Select the desired device.

   Details of hardware differences can be found in the "Compatibility information".

   If necessary, adapt the version.

   You can find additional information at [Changing the configured runtime version](#changing-the-configured-runtime-version).
4. Confirm the dialog.

##### Result

You have replaced the HMI device used in the project.

If needed, make the following adaptations:

- If you have exchanged a Unified Comfort Panel with a Unified PC or vice versa, for example, you need to adapt the configured connections.
- If you have selected an HMI device with a different screen resolution, adjust the screens.

##### Further procedure

To complete the device change, the following further steps are necessary:

- If necessary, replace the HMI device in your plant.
- Transfer the stored data to the new HMI device.

  > **Note**
  >
  > **Data transfer**
  >
  > Note that when changing the device type (changing from Unified Comfort Panel to a Unified PC or vice versa), the transfer of databases is not supported.
  >
  > Data of the central user administration (UMC) cannot be transferred and must be loaded together with the Runtime project.
- Compile and load the Runtime project into the new HMI device.

---

**See also**

[Changing the configured runtime version](#changing-the-configured-runtime-version)

#### Adapting the configuration of the connection (RT Unified)

##### Introduction

If an HMI device is changed, error messages may occur, for example "The object 'IE general' is not supported in the new configuration and will be removed".

These alarms refer to configured connections of the device and are triggered, for example, by different interfaces when replacing the Unified Comfort Panel with a Unified PC.

These connections are marked red after a device replacement. If you would like to continue to use these connections, you have to adapt the configuration of the connection.

##### Procedure

To connect a PLC to the HMI device again after the device replacement, follow these steps:

1. Open the "Devices and Networks" editor.
2. Click "Network" in the toolbar of the network view.
3. If necessary, add a communications module.
4. Network the interface of the HMI device with the interface of the PLC.
5. In the table area of the network view, click on the "Connections" table.
6. Select the connection marked red.
7. Enter the new interface under "Properties > General > General > Connection path" in the Inspector window.

### Upgrading a global library

#### Introduction

To process objects of a global library in a project, you must first upgrade the version of the global library to the project version. You are prompted accordingly when you open the global library.

#### Requirements

- The version of the global library is a predecessor version of your project version.
- You have write access to your project drive.
- All types in the library have been released.

#### Procedure

To upgrade a global library from TIA Portal V16 or V17, proceed as follows:

1. Open the global library.

   The "Upgrade global library" dialog box opens.
2. Click "OK".

#### Result

A copy of the global library is created and upgraded. The global library opens.

### Changing the configured runtime version

#### Introduction

If you want to upgrade or exchange the HMI device, change the configured Runtime version of an HMI device.

Change, for example, the configured Runtime version of a Unified Comfort Panel from V17 to V18.

#### Requirements

- A project has been created and opened.
- The project contains an HMI device.

#### Procedure

To change the configured Runtime version, follow these steps:

1. Double-click on "Devices & Networks" in the project tree.

   The editor opens.
2. Select the desired HMI device in the device view.
3. Select "Change device/version" in the device shortcut menu of the HMI device.

   A dialog opens.
4. Select the required HMI device.
5. Depending on the Runtime version installed on the target device, select a compatible Runtime version under "Version".
6. Confirm your selection with "OK".

**Note**

**Selection of Runtime versions**

The project version determines which Runtime versions are offered to you.

Alternatively, you can also change the configured Runtime version in the device properties in the project tree.

#### Result

You have changed the configured Runtime version of the HMI device in the WinCC project.

To successfully download the project, a compatible Runtime version must be installed on the target device.

In the next step, you upgrade the installed Runtime version of the HMI device or exchange the device.

---

**See also**

[Replacing the configured HMI device (RT Unified)](#replacing-the-configured-hmi-device-rt-unified-1)
  
[Replacing the configured HMI device (RT Unified)](#replacing-the-configured-hmi-device-rt-unified)

### Upgrading the installed Runtime version of a device (RT Unified)

This section contains information on the following topics:

- [Upgrading a Unified PC (RT Unified)](#upgrading-a-unified-pc-rt-unified)
- [Upgrading a Unified Comfort Panel (RT Unified)](#upgrading-a-unified-comfort-panel-rt-unified)

#### Upgrading a Unified PC (RT Unified)

##### Introduction

To use the new functionalities of the current Runtime version, you must upgrade the Unified PC.

##### Requirement

- No project is running in Runtime on the Unified PC.

> **Note**
>
> **No version skips**
>
> You cannot skip any version when upgrading.

##### Procedure

1. Install the higher Runtime version on the Unified PC.

   The existing data is retained, e.g. logs and parameter sets.
2. Upgrade the engineering system to the WinCC version that corresponds to the Runtime version installed on the Unified PC.
3. Upgrade the project version of the project to the WinCC version.
4. Upgrade the configured Runtime version of the HMI device.
5. Compile and download the project into the Unified PC.
6. Start the project on the Unified PC in Runtime.

**Note**

**Converting logging databases**

When a project is started for the first time in Runtime after upgrading, its logging data is adapted to the new database schema. This process is irreversible.

---

**See also**

[Use cases (RT Unified)](#use-cases-rt-unified)
  
[Changing the configured runtime version](#changing-the-configured-runtime-version)

#### Upgrading a Unified Comfort Panel (RT Unified)

##### Introduction

To use the new functionalities of the current Runtime version, you must upgrade the Unified Comfort Panel.

> **Note**
>
> **Protection against loss of data**
>
> To simplify data transmission, save the following data to external storage media:
>
> - Database for the tag persistence
> - Data logs
> - Alarm logs
> - Parameter sets
>
> Data from central user administration (UMC) cannot be backed up and must be loaded with the Runtime project.

> **Note**
>
> **No version skips**
>
> You cannot skip any version when upgrading.

##### Requirement

- No project is running in Runtime on the Unified Comfort Panel.

##### Procedure

To upgrade a Unified Comfort Panel, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Store the above-mentioned data of the Runtime project on external storage media. 2. Load an image with the higher Runtime version.      | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Data loss** All data stored internally on the Unified Comfort Panel will be lost. |  | 3. Make the backed up data available to the Unified Comfort Panel again.    Do not save the tag persistence database and the parameter sets on the same storage medium as the logs. 4. Upgrade the engineering system to the WinCC version that corresponds to the Runtime version installed on the Unified Comfort Panel. 5. Upgrade the project version of the project to the WinCC version. 6. Upgrade the configured Runtime version of the device. 7. Compile and load the project into the Unified Comfort Panel. 8. Start the project on the Unified Comfort Panel in Runtime. |  |

---

**See also**

[Use cases (RT Unified)](#use-cases-rt-unified)
  
[Changing the configured runtime version](#changing-the-configured-runtime-version)

### Replacing a device (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Replacing a Unified Comfort Panel (RT Unified)](#replacing-a-unified-comfort-panel-rt-unified)
- [Replacing a Unified PC (RT Unified)](#replacing-a-unified-pc-rt-unified)
- [Adjusting screens to the new HMI device (RT Unified)](#adjusting-screens-to-the-new-hmi-device-rt-unified)

#### Basics (RT Unified)

##### Introduction

When replacing the Unified HMI devices, you can use existing configurations for your new devices and optimize these configurations with very little manual effort. The configuration data are retained.

If you replace an HMI device, for example, a Unified Comfort Panel, and select a PC station as the new device, the configured data is automatically moved under the PC station. The adaptation of the screens to the new screen size takes place in one step after the device replacement. You can find additional information at "[Adjusting screens to the new HMI device](#adjusting-screens-to-the-new-hmi-device-rt-unified)".

##### Requirement

- A project has been created and opened.
- In the project, Unified Control Panels or WinCC Unified PCs are used for the visualization.

##### Introduction

1. Double-click "Devices" in the project navigation.   
   The editor opens.
2. Click the required HMI device.
3. Select "Change device/version" in the device shortcut menu.   
   A dialog opens.

   ![Introduction](images/159179314827_DV_resource.Stream@PNG-en-US.png)
4. Select the new HMI device and the FW version. Details of hardware differences can be found in the "Compatibility information" at the bottom of the table.
5. Click "OK".   
   Replacement of the device is started.

##### Result

You have replaced the device used in the project.

#### Replacing a Unified Comfort Panel (RT Unified)

##### Introduction

If you replace a Unified Comfort Panel with Runtime version V17 installed, you can replace the device with a Unified Comfort Panel with Runtime version V17 or V18 installed.

HMI devices starting from the installed Runtime version V17 are backward compatible. Runtime projects with a configured Runtime version V16 or higher can run on them. Compile and download existing Runtime projects without any additional adaptation.

> **Note**
>
> **Data transfer**
>
> Save the following data on external storage media:
>
> - Database for the tag persistence
> - Data logs
> - Alarm logs
> - Parameter sets
>
> Data from central user management (UMC) cannot be backed up and must be loaded with the Runtime project.

Alternatively, replace the Unified Comfort Panel with a Unified PC. To do this, follow the steps under [Replacing a Unified PC](#replacing-a-unified-pc-rt-unified) . Note that when replacing the device type, the transfer of databases is not supported.

##### Requirement

- The desired WinCC version is used.
- The project is available in the engineering system.
- The project version and the WinCC version are identical.

##### Procedure

> **Note**
>
> **Conversion of the logging databases with backward compatibility**
>
> When a project is started for the first time in Runtime in the backward compatibility mode, its logging data is adapted to the new database schema. This process is irreversible.

1. Store the above-mentioned data of the Runtime project on external storage media.
2. Make the backed up data available to the new Unified Comfort Panel.

   Do not save the tag persistence database and the parameter sets on the same storage medium as the logs.
3. Load the project in the new Unified Comfort Panel.
4. Start the project on the new Unified Comfort Panel in Runtime.

If you have replaced a Unified Comfort Panel with an installed Runtime version V17 with a Unified Comfort Panel with an installed Runtime version V18, the projects are automatically started in the backward compatibility mode at the start.

##### Result

You have replaced a Unified Comfort Panel.

The project runs on the new device in runtime.

If needed, make further adaptations, e.g. [Upgrading a Unified Comfort Panel](#upgrading-a-unified-comfort-panel-rt-unified).

---

**See also**

[Use cases (RT Unified)](#use-cases-rt-unified)

#### Replacing a Unified PC  (RT Unified)

##### Introduction

If you replace a Unified PC with an installed Runtime version V17, you can replace the device with a Unified PC with an installed Runtime version V17 or V18.

HMI devices starting from the installed Runtime version V17 are backward compatible. Runtime projects whose configured Runtime version is ≥ V16 can run on them. Compile and download existing Runtime projects without any additional adaptation.

> **Note**
>
> **Data transfer**
>
> Do not save databases directly on a network drive. Power supply can be interrupted at any time. Reliable operation is therefore not guaranteed.
>
> Save the following data on external storage media:
>
> - Database for the tag persistence
> - Data logs
> - Alarm logs
> - Parameter sets
>
>   On Unified PC, parameter sets are saved in the directory of the Runtime project.
>
> Data from central user management (UMC) cannot be backed up and must be loaded with the Runtime project.

Alternatively, replace the Unified PC with a Unified Comfort Panel. To do this, follow the steps under [Replacing a Unified Comfort Panel](#replacing-a-unified-comfort-panel-rt-unified). Note that when replacing the device type, the transfer of databases is not supported.

##### Requirement

- The desired WinCC version is used.
- The project is available in the engineering system.
- The project version and the WinCC version are identical.

##### Procedure

> **Note**
>
> **Conversion of the logging databases with backward compatibility**
>
> When a project is started for the first time in Runtime in the backward compatibility mode, its logging data is adapted to the new database schema. This process is irreversible.

1. Install the desired Runtime version on the new PC.
2. Store the above-mentioned data of the Runtime project on external storage media.
3. Make the backed up data available to the new Unified PC.

   On the new PC, select the log directory configured in the "WinCC Unified Configuration" tool during Runtime installation as the storage location for the logs.
4. Compile and download the project into the Unified PC.
5. Start the project on the new unified PC in Runtime.

If you have replaced a Unified PC with an installed Runtime version V17 with a Unified PC with an installed Runtime version V18, the projects are automatically started in backward compatibility mode at the start.

##### Result

You have replaced a Unified PC.

The project runs on the new device in runtime.

If needed, make further adaptations, e.g. [Upgrading a Unified PC](#upgrading-a-unified-pc-rt-unified).

---

**See also**

[Upgrading a Unified PC (RT Unified)](#upgrading-a-unified-pc-rt-unified)
  
[Use cases (RT Unified)](#use-cases-rt-unified)

#### Adjusting screens to the new HMI device (RT Unified)

If you replace an HMI device with a smaller or larger display, the configured screen sizes do not fit the new HMI device. The Unified Comfort Panels and Unified PCs offer an easy adaptation of the screen size, the objects and fonts used, all in one step.

##### Requirement

- A project has been created and opened.
- Unified Control Panels or WinCC Unified PCs are used in the project for the visualization.
- A screen is configured.
- You have exchanged an HMI device for another Unified Control Panel or a WinCC Unified PC.

##### **Adjusting the screen size**

1. Double-click "Devices" in the project navigation.   
   The editor opens.
2. Click the HMI device.
3. Select a screen under "Screens" and, on the bottom edge of the window, set the scale "Fit to screen".

   - If the new screen size is smaller than the screen size of the exchanged device, a part of the screen is framed by a thin black line. In this case, only the part in the frame would be shown on the display of the new device.
   - If the new screen size is larger than the screen size of the exchanged device, the screen only fills a part of the display area.

   ![Adjusting the screen size](images/142805313547_DV_resource.Stream@PNG-en-US.png)

   ![Adjusting the screen size](images/142805313547_DV_resource.Stream@PNG-en-US.png)
4. Select a screen, a screen group or several screens. Right-click the selected screens and select "Resize to display".

If you scale a large number of screens, an information window is shown that informs you about the progress of the change.

##### Result

The screen size, the objects, and fonts used are scaled in one step in all the selected screens.

![Result](images/142805594507_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> After replacing the HMI device with a substantially larger or smaller variant, check the appearance of the configured screens. Changed display sizes can result, for example, in the fonts being too small or too large.

## Using cross-references (RT Unified)

This section contains information on the following topics:

- [General notes about cross-references (RT Unified)](#general-notes-about-cross-references-rt-unified)
- [Textual cross-references (RT Unified)](#textual-cross-references-rt-unified)
- [Invalid cross-references (RT Unified)](#invalid-cross-references-rt-unified)
- [Displaying the "Cross-references" editor (RT Unified)](#displaying-the-cross-references-editor-rt-unified)
- [Display cross-references in the Inspector window (RT Unified)](#display-cross-references-in-the-inspector-window-rt-unified)
- [Restoring cross-references after project upgrade (RT Unified)](#restoring-cross-references-after-project-upgrade-rt-unified)

### General notes about cross-references (RT Unified)

#### Introduction

The cross-references provide an overview of the use of objects and devices within the project and the project library. The relationships and the dependencies between the objects can be displayed using the cross-references.

![Introduction](images/159947182347_DV_resource.Stream@PNG-de-DE.png)

- To open the "Cross-references" editor, select "Cross-references" in the shortcut menu of the navigation object in the project tree.

  - or -

  Press <F11>

  - or -

  In the Inspector window, select "About > Cross-references".
- To open the "Cross-reference information", select "Cross-reference information" in the shortcut menu of an object, tag, alarm, etc.

  - or -

  Press <⇑ + F11>.

#### Benefits of cross-references

Cross-references offer the following advantages:

- When creating the project and when there are changes, you maintain an overview of the devices, objects, tags, faceplate types, alarms, scripts, etc. that you have used.
- From the cross-references, you can jump directly to the respective location of use of objects.
- You can see whether the respective object uses other objects or is itself used.
- During troubleshooting you will learn, for example, the following:

  - Which objects are used in which screen and on which devices.
  - Which alarms and parameter sets are displayed in which display.
  - Which tag is used in which alarm or which object.

---

**See also**

[Displaying the "Cross-references" editor (RT Unified)](#displaying-the-cross-references-editor-rt-unified)
  
[Display cross-references in the Inspector window (RT Unified)](#display-cross-references-in-the-inspector-window-rt-unified)

### Textual cross-references (RT Unified)

#### Introduction

Textual cross-references are cross-references that are stored as pure text. With the help of textual cross-references, you cannot navigate to a different object. These cross-references are shown in red.

![Introduction](images/135553336203_DV_resource.Stream@PNG-en-US.png)

Textual cross-references are created as follows:

- You create a textual cross-reference for a non-existent object manually by entering the object name under Property and updating the cross-reference list.
- The object used has already been deleted, and the connection to it is shown as textual cross-reference.

#### Basics

When references and subordinate objects of a source object are deleted, they are converted into textual cross-references. A textual cross-reference is not stored when the source object itself is deleted.

> **Note**
>
> Almost all objects, with the exception of tag and alarm logs, support textual cross-references.

> **Note**
>
> Textual cross-references cannot be deleted.

You can also create a textual cross-reference manually to establish a connection to a non-existent object. This procedure can be helpful if you want to access tags directly using scripts.

#### Using textual cross-references when working with scripts

When working with scripts, you can reference tags directly with the help of textual cross-references.

When you enter an object name, the referenced object is searched for.

#### Sample code

export async function IO_Field_1_OnTapped(item, x, y, modifiers, trigger)

{

HMIRuntime.Tags.SysFct.IncreaseTag("HMI_Tag_1", 0);

}

If a tag exists under the name "Variable_Test", it is referenced.

If there is no tag with the name "Variable_Test", the system creates a textual cross-reference for the tag.

The textual cross-reference is assigned to the tag that you create under this name. The textual cross-reference becomes a linked cross-reference.

### Invalid cross-references (RT Unified)

A cross-reference can become invalid as a result of certain changes to the configuration. Invalid cross-references are shown as grayed out.

![Figure](images/159391106187_DV_resource.Stream@PNG-en-US.png)

Invalid cross-references do not have any negative implications for your project.

If an object or location of use is invalid, you cannot navigate to that object or location of use. You cannot change the properties of an invalid location of use. No shortcut menu is available for invalid locations of use.

### Displaying the "Cross-references" editor (RT Unified)

#### Introduction

Depending on the object selected in the project tree, all the cross-references available for the object are displayed. In the project tree you can show cross-references for HMI devices, folders, and all editors. The detail view also lets you select individual objects of the editors, for example, individual screens.

Cross-references are always displayed for the selected object and for all lower-level objects.

The display of the cross-references for an object is specific to the project and device. You can display multiple cross-reference editors at the same time.

![Introduction](images/159391117067_DV_resource.Stream@PNG-en-US.png)

#### Requirement

- A project has been created.
- Multiple objects with references have been created.

#### Procedure

1. Select the required entry in the project tree or detail view.
2. Select "Cross-references" in the shortcut menu.

   Alternatively, select the "Cross-reference" command from the "Tools" menu.

   The "Cross-references" editor is opened in the working area.

   - The relevant selected object is the "source object" and is at the top in the "Object" column.
   - Point of use: Shows the locations at which the objects shown in the cross-reference list are used.
   - Type of use: Indicates whether the object is used.
3. To go to the location of use for a specific object, click on the cross-reference shown in blue in the "Point of use" column.
4. To go to the specific object, select the required object and select "Open editor" from the shortcut menu.

   The editor in which the object can be processed opens.
5. You can perform the following actions using the icons in the toolbar:

   - Updating
   - Collapse all
   - Expand all
   - Define filters for the cross-reference list
   - Show overlapping access
   - Check overlapping access
   - Add new source object
   - Save window settings

> **Note**
>
> **Restoring cross-references after a project upgrade.**
>
> After a project upgrade to a higher TIA Portal version, you have the option of recreating the associated cross-reference data for the updated project.
>
> This happens automatically at the end of the upgrade process. The updated project is opened and the cross-references are available again.
>
> If the cross-reference data is inconsistent or incomplete, you will receive information. A banner text with a link to this information is displayed when the cross-reference list is opened. In this case, you can reorganize the cross-references yourself.

#### Delete

If you select a source object and "Delete" in the shortcut menu or press <Del>, then the object and not only the cross-reference is deleted.

A warning is displayed before the deletion.

After an object has been deleted, the cross-reference list is updated.

You cannot delete cross-reference lists.

### Display cross-references in the Inspector window (RT Unified)

#### Introduction

In the Inspector window, the cross-reference information for a selected object is displayed in the "Info > Cross-references" tab. In this way, you can see at a glance all the cross-references of the respective object without changing the cross-reference list.

All included elements and their use in the cross-reference list are displayed for structured tags, user data types and instances of a PLC data type.

#### Requirement

- A project has been created.
- Multiple objects with references have been created.

#### Procedure

1. Select an object.
2. Select "Cross-reference information" in the shortcut menu.

   The cross-references are opened in the Inspector window.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| If you select another object, the contents of the Inspector window are automatically refreshed. The cross-references to the selected object are displayed. |  |

> **Note**
>
> **"Inspector window" restrictions**
>
> The Inspector window provides you with almost the same functions as in the "Cross-references" editor.
>
> With more than 10,000 objects, the source objects and referenced objects are not sorted alphabetically in the Inspector window.

#### Example

When you select an object in the screen and an HMI tag is being used as the process tag at the object, the object and the linked HMI tag are displayed in the cross-references.

When the HMI tag is interconnected with a PLC tag or a data block tag, the locations of use of the interconnected PLC tag or data block tag are also displayed.

#### Result

The instances where and the other objects by which the selected object is being used are displayed.

The table below shows the additional information listed in the "About > Cross-reference" tab:

| Column | Content/meaning |
| --- | --- |
| Object | Name of the object that uses the lower-level objects or that is being used by the lower-level objects. |
| Point of use | Each point of use, for example, an object or event |
| Type of use | Object relationships between the source object and its uses:  - "Used by": The source object uses this object - "Uses": The source object is used by this object - "Type instance": The source object is a type or an instance of the referenced object - "Belongs to": The source object belongs to the reference object - "Contains": The source object contains the reference object |
| As | Shows additional information about objects, for example, that a tag is used by several devices |
| Access | Shows whether access to the object is read (R) and/or write (W) |
| Address | Displays the address of the object |
| Type | Displays information about the type and language used to create the object |
| Device | Displays the associated device name |
| Path | Displays the path of the object in the project tree with specification of folders and groups. |
| Comment | Displays user comments on individual objects, if available. |

Depending on the installed products and the selected objects, additional columns or different columns are displayed for the cross-references.

### Restoring cross-references after project upgrade (RT Unified)

#### Introduction

After a project upgrade to a higher TIA Portal version, you have the option of recreating the associated cross-reference data for the updated project.

This happens automatically at the end of the upgrade process. The updated project is then opened and the cross-references are available again.

If the cross-reference data is inconsistent or incomplete, you will receive information. A banner text with this information and a further link is displayed when you display the cross-references.

In this case, you can reorganize the cross-references yourself.

#### Requirement

You have performed a project upgrade and received the message that the cross-reference data is inconsistent or incomplete.

#### Recreate cross-reference information

To create new cross-reference information, follow these steps:

1. Click the link to restore the cross-reference information in the displayed message.

   As an alternative, you can also navigate to "Cross-references" under "Tools > Settings > General".
2. Click the displayed "Recreate the cross-reference information" button.
3. Once the restore process is complete, check the message in the Inspector window to see if the operation was successful.

   If the process was not successful, you receive an error message.
4. In the cross-reference list, click the "Update" button to close the displayed banner again.

#### Result

The cross-references for the selected project have been recreated.

## Configuring cycles (RT Unified)

This section contains information on the following topics:

- [Basics of cycles (RT Unified)](#basics-of-cycles-rt-unified)
- [Defining cycles (RT Unified)](#defining-cycles-rt-unified)

### Basics of cycles (RT Unified)

Cycles are used to control actions that reoccur regularly in runtime. Classic applications include:

- The acquisition cycle
- The logging cycle
- The screen cycle

You can also define your own cycles in addition to those already provided in WinCC.

#### Principle

Typical applications for cycles:

- Acquisition of external tags  
  The acquisition cycle determines when the HMI device will read the process value of an external tag from the PLC. Set the acquisition cycle to suit the rate of change of the process values. The temperature of an oven, for example, changes much more slowly than the speed of an electrical drive.  
  Do not set the acquisition cycle too low, since this will unnecessarily increase the communication load of the process.
- Triggering scheduled tasks  
  In scheduled tasks you have the option to configure a task with a cyclical trigger. Use the cycle time to determine when the scheduled task is executed.
- Logging process values  
  The logging cycle determines when a process value is saved in the logging database. The logging cycle is always an integer multiple of the acquisition cycle.

The smallest value for a cycle in Runtime Unified is 100 ms. You can configure all other values with an increment of 50 ms. The default value for the setting is 500 ms.

#### Application example

You can use cycles for the following tasks:

- To record and archive process values
- To trigger tasks
- To regularly log a process
- To draw attention to maintenance intervals

### Defining cycles (RT Unified)

#### Introduction

Use cycles to control actions that are run at regular intervals in runtime. You can also define your own cycles in addition to those already provided in WinCC.

#### Requirement

The project is open.

#### Procedure

To define a cycle, follow these steps:

1. Double-click the "Cycles" entry in the project navigation.  
   The "Cycles" editor opens.
2. In the "Name" column of the "Cycles" editor, double-click "Add".  
   A new cycle time is created.
3. Enter a unique name in the "Name" field.
4. Select the desired cycle unit.
5. Select the desired value for the cycle time.

   The available selection of values varies depending on the cycle unit selected.
6. As an option, you can enter a comment regarding the use of the cycle.
7. Save the project.

#### Result

The cycle you configured is created and beside the default cycles in WinCC for use during configuration.

## Configuring in multiple languages (RT Unified)

This section contains information on the following topics:

- [Languages in WinCC (RT Unified)](#languages-in-wincc-rt-unified)
- [Settings for languages in the operating system (RT Unified)](#settings-for-languages-in-the-operating-system-rt-unified)
- [Settings for Asian languages in the operating system (RT Unified)](#settings-for-asian-languages-in-the-operating-system-rt-unified)
- [Setting project languages (RT Unified)](#setting-project-languages-rt-unified)
- [Creating one project in multiple languages (RT Unified)](#creating-one-project-in-multiple-languages-rt-unified)
- [Using language-specific graphics (RT Unified)](#using-language-specific-graphics-rt-unified)
- [Languages and fonts in runtime (RT Unified)](#languages-and-fonts-in-runtime-rt-unified)

### Languages in WinCC (RT Unified)

#### User interface language and project languages

A distinction is drawn between two different language levels in WinCC:

- User interface language

  During configuration, the text in the WinCC menus and dialogs is displayed in the user interface language. The user interface language also affects the labeling of operating elements, the parameters of the system functions, the online help, etc.
- Project languages

  Project languages are all languages in which a project will later be used. Project languages are used to create a project in multiple languages.

The two language levels are completely independent of one another. For example, you can create English projects at any time using a German user interface and vice versa.

![User interface language and project languages](images/159801926795_DV_resource.Stream@PNG-de-DE.png)

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

  You must provide appropriate operator controls so that the operator can switch between languages in Runtime.

### Settings for languages in the operating system (RT Unified)

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

### Settings for Asian languages in the operating system (RT Unified)

#### Settings on Western operating systems

If you want to enter Asian characters, you must enable support for this language in the operating system.

The Input Method Editor (IME) is available in Windows for configuring Asian texts. Without this editor, you can display Asian text but not edit it. For more information on the Input Method Editor, refer to the documentation for Windows. To enter Asian characters when configuring, switch to the Asian entry method in the "Input Method Editor".

Switch the operating system to the appropriate language to have language-specific project texts, such as alarm texts, displayed in the simulator in Asian characters.

#### Settings on Asian operating systems

If you are configuring on an Asian operating system, you must switch to the English default input language to enter ASCII characters, for example, for object names. As the English default input language is included in the basic installation of the operating system, you do not need to install an additional input locale.

#### Enabling language support

1. Open "Settings" from the Windows Start menu.
2. Select "Time & Language > Language".
3. Select "Preferred languages > Add a language".
4. Select the language.

   The "Install language features" dialog box is displayed.
5. Install the selected language pack and enable additional options, if necessary
6. Under "Related settings > Administrative language settings", you can find settings for programs that do not support Unicode.

> **Note**
>
> The options may be named or arranged differently depending on the operating system.

### Setting project languages (RT Unified)

This section contains information on the following topics:

- [Selecting the user interface language (RT Unified)](#selecting-the-user-interface-language-rt-unified)
- [Enabling project languages (RT Unified)](#enabling-project-languages-rt-unified)
- [Selecting the reference language and editing language (RT Unified)](#selecting-the-reference-language-and-editing-language-rt-unified)

#### Selecting the user interface language (RT Unified)

##### Introduction

The user interface language is used for displaying menu entries, title bars, infotext, dialog texts and other designations in the WinCC user interface.

You can switch between the installed user interface languages during configuration. The labeling of the operating elements remains in the language you set when you added the object even if you change the user interface language.

##### Procedure

1. Select "Options > Settings" in the menu.

   The "Settings" dialog box is opened.
2. Select the user interface language under "General > General".

##### Result

WinCC will use the selected language as user interface language.

#### Enabling project languages (RT Unified)

##### Introduction

The project languages are set in the "Project languages" editor. You define which project language is to be the reference language and which the editing language.

##### Enabling project languages

1. Click on the arrow to the left of "Languages & resources" in the project tree.

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

#### Selecting the reference language and editing language (RT Unified)

##### Introduction

The project languages are set in the "Project languages" editor. You define which project language is to be the reference language and which the editing language. You can change the editing language at any time.

##### Requirements

The "Project languages" editor is open.

Several project languages have been activated.

##### Selecting the reference language and editing language

1. Click the arrow in the drop-down list in the "General > Editing language" section.
2. Click the required language in the drop-down list, for example, German.
3. Click on the arrow in the drop-down list in the "General > Reference language" section.
4. Click the required language in the drop-down list, for example, English.

The language selection is displayed in the list box.

![Selecting the reference language and editing language](images/162759386123_DV_resource.Stream@PNG-en-US.png)

##### Result

You have now selected the editing and reference languages.

If you change the editing language, all future text input will be stored in the new editing language.

---

**See also**

[Configuring multilingual alarm texts (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-multilingual-alarm-texts-rt-unified)

### Creating one project in multiple languages (RT Unified)

This section contains information on the following topics:

- [Working with multiple languages (RT Unified)](#working-with-multiple-languages-rt-unified)
- [Basics of project texts (RT Unified)](#basics-of-project-texts-rt-unified)
- [Translating texts directly (RT Unified)](#translating-texts-directly-rt-unified)
- [Translating texts using reference texts (RT Unified)](#translating-texts-using-reference-texts-rt-unified)
- [Exporting project texts (RT Unified)](#exporting-project-texts-rt-unified)
- [Importing project texts (RT Unified)](#importing-project-texts-rt-unified)

#### Working with multiple languages (RT Unified)

##### Multilingual configuration in WinCC

You can configure your projects in multiple languages using WinCC. There are various reasons for creating a project in multiple languages:

- You would like to use a project in more than one country.

  You would like to create the project in multiple languages. When the HMI device is commissioned, only the language spoken by the operators at the respective site is transferred to the HMI device.
- The operators of a system speak different languages.

  Example: An HMI device is used in Germany, but the operating personnel understand only English.

##### Translating project texts

With WinCC, you can enter project texts directly in multiple languages in various editors, for example, in the "Project texts" editor. WinCC also allows you to export and import your configuration for translation purposes. This is advantageous if you configure projects containing a large amount of text and want to have it translated.

##### Language management and translation in WinCC

The following editors are used to manage languages and translate texts in WinCC:

| Editor | Short description |
| --- | --- |
| Project languages | Selection of project languages, editing language and reference language. |
| Languages and fonts | Selection of Runtime languages and the fonts used on the HMI device. |
| Project texts | Central management of configured texts in all project languages. |
| Project graphics | Project graphics for managing graphics and their language-specific versions. |

---

**See also**

[Configuring multilingual alarm texts (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-multilingual-alarm-texts-rt-unified)

#### Basics of project texts (RT Unified)

##### Texts in different languages in the project

Texts that are output on HMI devices during process operation are typically entered in the language in which the automation solution is programmed. Comments and the names of objects are also entered in this language.

If operators do not understand this language, they require a translation of all operator-relevant texts into a language they understand. You can therefore translate all the texts into any language. In this way, you ensure that anyone who is subsequently confronted with the texts in the project sees the texts in his/her language of choice.

##### User texts and system texts

In the interests of clarity, a distinction is drawn between user texts and system texts:

- User texts are texts created by the user.
- System texts are texts created automatically and which are a product of configuration in the project.

The project texts are managed in the project text editor. This can be found in the project tree under "Languages & Resources > Project texts".

##### Examples of multilingual project texts

You can create and manage the following text types in multiple languages:

- Display texts
- Alarm texts
- Comments in tables
- Labels of screen objects
- Texts in text lists

##### Translating texts

There are two ways of translating texts.

- Translating texts directly

  You can enter the translations for the individual project languages directly in the "Project texts" editor.
- Translating texts using reference texts

  You can change the editing language for shorter texts. You can enter the new texts in the editing language while the texts of the reference language are displayed.

##### Missing translation for texts of screen elements

> **Note**
>
> If no translation in the current user interface language exists for a text of a screen element, the text entered for the default language is displayed.

---

**See also**

[Configuring multilingual alarm texts (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-multilingual-alarm-texts-rt-unified)

#### Translating texts directly (RT Unified)

##### Translating texts

If you use several languages in your project, you can translate individual texts directly. As soon as you change the language of the software user interface, the translated texts are available in the selected language.

##### Requirements

- You are in the project view.
- A project is open.
- You have selected at least two other project languages.

##### Procedure

Proceed as follows to translate individual texts:

1. Click on the arrow to the left of "Languages & resources" in the project tree.

   The elements below this are displayed.
2. Double-click on "Project texts".

   A list with the texts in the project is displayed in the work area. There is a separate column for each project language.

   ![Procedure](images/162767374987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/162767374987_DV_resource.Stream@PNG-en-US.png)
3. To group identical texts and translate them simultaneously, click "![Procedure](images/102568451851_DV_resource.Stream@PNG-de-DE.png)" in the toolbar.
4. To hide texts that do not have a translation, click ![Procedure](images/102568460171_DV_resource.Stream@PNG-de-DE.png) in the toolbar.
5. Click a cell and enter the translation.

##### Result

You have translated individual texts in the "Project texts" editor. The texts will then be displayed in the runtime language.

---

**See also**

[Configuring multilingual alarm texts (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-multilingual-alarm-texts-rt-unified)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)

#### Translating texts using reference texts (RT Unified)

##### Introduction

After changing the editing language, all texts are shown in input boxes in the new editing language. If there is not yet a translation available for this language, the input boxes are empty or filled with default values.

If you enter text again in an input field, this is saved in the current editing language. Following this, the texts exist in two project languages for this input field, in the previous editing language and in the current editing language. This makes it possible to create texts in several project languages.

You can display existing translations for an input box in other project languages. These serve as a comparison for text input in the current editing language and they are known as the reference language.

##### Requirement

There is at least one translation into a different project language for an input field.

##### Procedure

To display the translation of an input cell in a reference language, follow these steps:

1. Select "Tasks > Languages & resources" in the task card.
2. Select a reference language from the "Reference language" drop-down list.

##### Result

The reference language is preset. If you click in a text field, translations that already exist in other project languages are shown in the "Tasks > Reference language" task card.

#### Exporting project texts (RT Unified)

Project texts are exported for translation. Texts are exported to Office Open XML files ending in ".xlsx". These can be edited in Microsoft Excel, for example.

You can exchange the file with the translators and import it directly back into the project after translation.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor, e.g. Italian and French.

##### Exporting project texts

To export individual project texts, proceed as follows:

1. Click on the arrow to the left of "Languages & resources" in the project tree.

   The child elements are displayed.
2. Double-click on "Project texts". The "Project texts" editor will open.
3. Select the texts you want to export.
4. Click on the ![Exporting project texts](images/102568515467_DV_resource.Stream@PNG-de-DE.png) button. The "Export" dialog box opens.

   ![Exporting project texts](images/160499889675_DV_resource.Stream@PNG-en-US.png)

   ![Exporting project texts](images/160499889675_DV_resource.Stream@PNG-en-US.png)
5. Select the language you want to translate from in the "Source language" drop-down list.
6. Select the check box(es) for the target language(s) into which you want the texts to be translated.
7. Under "Select content", select the categories of texts you want to translate.
8. In the "Export file" input field, specify the file name for the export file.
9. Enter a file path for the export file in the "Path" input field.
10. Click "Export".

##### Result

The texts selected in the "Project texts" editor are written to an xlsx file. The xlsx file will be stored in the specified folder.

> **Note**
>
> Project texts in library objects cannot be exported.

---

**See also**

[Configuring optional parameters for discrete and analog alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)

#### Importing project texts (RT Unified)

Once translation is complete, import the xlsx file with the translated texts. The target languages are imported to the corresponding object in the project.

> **Note**
>
> In WinCC, you import previously exported project texts only into the source project. Importing into a different project is not supported.

##### Requirements

- At least two languages have been enabled in the "Project languages" editor.

##### Importing project texts

To import a file with project texts, proceed as follows:

1. Click on the arrow to the left of "Languages & resources" in the project tree.

   The lower-level elements will be displayed.
2. Double-click on "Project texts".

   The "Project texts" editor will open.
3. Click on the ![Importing project texts](images/102568533259_DV_resource.Stream@PNG-de-DE.png) button. The "Import" dialog box opens.
4. Select the path and the file name of the import file from the "Select file for import" field.
5. Activate the "Import source language" check box if you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes.
6. Click on "Import".

##### Result

You have imported the project texts.

---

**See also**

[Configuring multilingual alarm texts (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-multilingual-alarm-texts-rt-unified)

### Using language-specific graphics (RT Unified)

This section contains information on the following topics:

- ["Project graphics" editor (RT Unified)](#project-graphics-editor-rt-unified)
- [Storing an image in the project graphics (RT Unified)](#storing-an-image-in-the-project-graphics-rt-unified)
- [Storing an external image in the project graphics (RT Unified)](#storing-an-external-image-in-the-project-graphics-rt-unified)
- [Editing a graphic (RT Unified)](#editing-a-graphic-rt-unified)

#### "Project graphics" editor (RT Unified)

##### Introduction

You use the "Project graphics" editor to manage the configured graphic objects in different language versions. Multilingual projects require language-dependent versions of the graphics, for example, if:

- The graphics contain text
- Cultural aspects play a role

##### Opening the "Project graphics" editor

- Double-click in the project tree on "Languages and resources > Project graphics".

##### Work area

The work area displays all configured graphic objects in a table. There is a separate column in the table for each project language. Each column in the table contains the versions of the graphics for one particular language.

In addition, you can specify a default graphic for each graphic to be displayed whenever a language-specific graphic for a project language does not exist.

##### Preview

The preview shows you how the graphics will look on various HMI devices.

#### Storing an image in the project graphics (RT Unified)

##### Introduction

You use the "Graphics" editor to import graphics for use in screen objects in the "Screens" editor. Here you import and manage language-dependent graphic versions. A preview shows how the graphic looks on various HMI devices.

> **Note**
>
> **File names for language-dependent graphics**
>
> Case is relevant in the file names of language-dependent graphics. Make sure to use the same spelling for all languages.

> **Note**
>
> **File format of language-dependent graphics**
>
> In the language-dependent versions of a graphic, use only graphic files with the same format. Graphic versions with different file formats are not supported.

##### Requirement

- The language-dependent versions of a graphic are available.
- Multiple languages have been enabled in the "Project languages" editor.
- The "Graphics" editor is open.

##### Adapting the view of the project graphics

1. To show/hide the columns with language-dependent graphics, click on ![Adapting the view of the project graphics](images/158416421899_DV_resource.Stream@PNG-de-DE.png).
2. To add another project language to the table, click on ![Adapting the view of the project graphics](images/158418670475_DV_resource.Stream@PNG-de-DE.png).

##### Inserting graphics

1. Click "<Add>" in the "Project graphics" table.

   The dialog for selecting a file opens.
2. Select the graphic file and click "Open."

   The graphic is inserted into the project as a standard graphic and displayed in all cells of this row in the "Graphics" editor.

   The standard graphic is displayed in Runtime for languages for which there is no language-specific graphic.
3. Right-click in the cell of a language for which a language-dependent version of this graphic is to be imported.
4. Select "Replace with graphic" in the shortcut menu.

   The dialog for selecting a file opens.
5. Select the graphic file and click "Open."

   The language-dependent version of the graphic is inserted in the table.

Alternatively, you can drag&drop a graphic from Windows Explorer to the desired position in the "Project graphics" table.

##### Inserting graphics by copying

1. Select "Copy" in the shortcut menu of an existing graphic.
2. Select "Paste" in the shortcut menu of an empty cell.

   A new row is inserted. The copied graphic is inserted for all languages.
3. Select "Paste" in the shortcut menu of a filled cell.

   The existing graphic is replaced by the copied graphic.

##### Displaying graphics in the device preview

1. Select an HMI device in the "Select device for preview" drop-down list in the editor.
2. Click on a graphic in the table.

   In the Inspector window under "Properties > General > Preview for HMI device", you see the graphic as it will appear in Runtime on the selected HMI device.

##### Result

The inserted graphics are available in the project. The graphic assigned to the respective editing language will be displayed during editing. The standard graphic is displayed in editing languages for which no screen has been imported.

The screens assigned to the respective Runtime language are displayed in Runtime. The standard graphic is displayed in Runtime languages for which no screen has been imported.

> **Note**
>
> If you disable a project language, all previously inserted graphics in this language are deleted in the current project.

#### Storing an external image in the project graphics (RT Unified)

##### Introduction

To use a graphic created in an external graphics program in screens, you add it to the project graphics.

##### Requirement

- Multiple languages have been enabled in the "Project languages" editor.
- The "Graphics" editor is open.
- There is a graphic in the "Graphics" editor.

##### Creating and adding a new graphic as an OLE object

1. Right-click in a cell containing a graphic.
2. Select "Replace with object" in the shortcut menu.

   The "Insert object" dialog box opens.
3. Select "Insert object > Create new" and an object type in the dialog.
4. Click "OK."

   The graphics program assigned by the operating system opens.
5. Create the graphic.
6. Close the graphics program.

   The graphic is saved in the standard format of the graphics program and inserted into the project graphics.

**Note**

In addition, the "External application running..." dialog opens. The dialog is closed when the external application has finished.

##### Result

The inserted OLE objects are available in the "Graphics" editor.

Versions of the graphics for the current editing language are displayed in the "Screens" editor. The default graphic is displayed in all editing languages for which no screen has been imported.

The graphic is displayed in Runtime in the set Runtime language. The default graphic is displayed in all Runtime languages for which no graphic has been imported.

#### Editing a graphic (RT Unified)

Graphics can be edited directly from the project graphics with an external graphics program.

##### Requirement

- The "Graphics" editor is open.
- There is a graphic in the "Graphics" editor.

##### Editing a graphic

1. Select "Edit" in the shortcut menu for a graphic.

   The assigned program, e.g. "Paint", opens.
2. Edit the graphic.
3. Close the external program, e.g. with the "Close and return to document" command.

   The edited graphic is available in the project graphics.

**Note**

In addition, the "External application running..." dialog opens. The dialog is closed when the external application has finished.

### Languages and fonts in runtime (RT Unified)

This section contains information on the following topics:

- [Using multiple runtime languages (RT Unified)](#using-multiple-runtime-languages-rt-unified)
- [Own fonts (RT Unified)](#own-fonts-rt-unified)
- [Methods for language switching (RT Unified)](#methods-for-language-switching-rt-unified)
- [Starting a project in a different language (RT Unified)](#starting-a-project-in-a-different-language-rt-unified)
- [Enabling the runtime language (RT Unified)](#enabling-the-runtime-language-rt-unified)
- [Standardizing font for all languages (RT Unified)](#standardizing-font-for-all-languages-rt-unified)
- [Specific features of Asian and Eastern languages in runtime (RT Unified)](#specific-features-of-asian-and-eastern-languages-in-runtime-rt-unified)

#### Using multiple runtime languages (RT Unified)

In the Runtime settings, you define which project languages are used in Runtime on a particular HMI device. The number of Runtime languages that are available at one time on the HMI device depends on the device. To enable the operator to switch between languages in Runtime, you need to configure a corresponding operator control.

1. In "Languages & Resources", you configure project languages that are available as Runtime languages for the respective device.
2. In "Runtime settings > Language & Font", you define the order in which the languages are switched.

![Figure](images/162768083723_DV_resource.Stream@PNG-en-US.png)

At Runtime start, the Runtime project is displayed in the language that is set in the "User login" dialog. If this language is not configured in the Runtime settings of the HMI device, the language with the lowest number in the "Order" column is used.

You change the order with ![Figure](images/134928713995_DV_resource.Stream@PNG-de-DE.png). Four predefined fonts are stored for each language. The fixed font 1 is always provided for the respective HMI device.

#### Own fonts (RT Unified)

This section contains information on the following topics:

- [Downloading your own font (RT Unified)](#downloading-your-own-font-rt-unified)
- [Loading fonts onto the HMI device (RT Unified)](#loading-fonts-onto-the-hmi-device-rt-unified)

##### Downloading your own font (RT Unified)

###### Using fonts that require licenses on HMI devices

When a font that requires a license is installed on your configuration PC, you can load this font onto your HMI device under certain conditions. Whether or not you can load the font onto your HMI device depends on the embeddability of the font.

Check the properties of the font in Windows:

1. Open the "C:\Windows\Fonts" folder in Windows Explorer.
2. Select the desired font.

   If several fonts are grouped into a font family, click on the entry for the font family. The individual fonts are now displayed.
3. Right-click the entry for the font.
4. Select "Properties".
5. In the "Details" tab, you find information about the embeddability of the font and the license terms and conditions.

The embeddability of fonts can have the following statuses:

- "Installable" status: Font can be installed on your HMI device without an additional license.
- "Editable" status: Font can be installed on your HMI device without an additional license.
- "Preview/Print" status: Warning during compilation that the font cannot be installed on your HMI device.
- "Restricted license embedding" status: Font can be installed on your HMI device with an additional license.
- "Bitmap embedding only" status: Compilation of the project is aborted with an error; the font cannot be installed on your HMI device.
- "No subsetting" status: Warning during compilation that the font can only be loaded onto the HMI device as a complete set. Substitute fonts and options for partial fonts cannot be used during compilation.

> **Note**
>
> The fonts configured in the Engineering System (TrueType fonts) are converted into web fonts and both TrueType fonts and web fonts are downloaded to the Runtime machine: WinCC Unified PC (Windows) or Unified Comfort Panel (Linux). The user is responsible for ensuring that the license of the fonts used allows this.

Additional information is available under [Font redistribution](https://docs.microsoft.com/en-us/typography/fonts/font-faq#document-embedding) and [OpenType_fsType](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype).

##### Loading fonts onto the HMI device (RT Unified)

###### Introduction

When a font that requires a license is installed in Windows on your configuration PC, you can also use this font on your HMI device under certain conditions. You are responsible for ensuring that your devices have valid licenses.

###### Downloading a customer-specific font

The TIA Portal project does not include any configured TrueType or Web fonts. The Runtime font conversion uses an RDF filed that was written in the RDF language (Resource Description Framework) and is used for displaying information on the resources. The RDF file contains metadata in a structured format; the metadata comprise the font file (ttf) as CSD resource.

The result of the GetNearestFont mechanism is transferred to the Runtime. The GetNearestFont function first searches for the font of the same name. If such a font does not exist, other fonts are checked one after the other.

> **Note**
>
> The fonts configured in the Engineering System (TrueType fonts) are converted into web fonts and both TrueType fonts and web fonts are downloaded to the Runtime machine: WinCC Unified PC (Windows) or Unified Comfort Panel (Linux). The user is responsible for ensuring that the license of the fonts used allows this.

Additional information is available under [Font redistribution](https://docs.microsoft.com/en-us/typography/fonts/font-faq#document-embedding) and [OpenType_fsType](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype).

#### Methods for language switching (RT Unified)

##### Introduction

To enable switching between configured Runtime languages on the HMI device, you provide a language switching means. This is necessary to enable the operator to switch between the various Runtime languages.

##### Methods for language switching

You can configure the following methods for language switching:

- Direct language selection

  Each language is set by means of a separate button. You create a button for each Runtime language.
- Language switching

  The operator switches the languages using a button. Each click of the button changes the Runtime language to the next Runtime language.

Regardless of the method used, the button names must be translated into each of the languages used. You can also configure an output field that displays the current language setting.

#### Starting a project in a different language (RT Unified)

##### Introduction

If the language "German" is configured in Unified Comfort Panel, the Runtime project is always started in German, regardless of the defined language sequence.

To start the project in another language, use the "HMIRuntime.Language" system function.

##### Procedure

Proceed as follows to start a project once automatically in English:

1. Create a "Bool" type tag, for example, "doOnlyAtStartup".
2. For the project start screen, link the "Loaded" event with the following script:

export function Screen_1_OnLoaded(item)

{

if(!Tags('doOnlyAtStartup').Read())

{

HMIRuntime.Language = 1033;

Tags('doOnlyAtStartup').Write(true);

}

}

To start the project in another language, enter the decimal Windows Locale Code (LCID=Locale ID) for the desired language instead of "1033". You can find the LCIDs on the Internet, for example.

#### Enabling the runtime language (RT Unified)

##### Introduction

The "Language & Font" editor shows all project languages available in the project. You select which project languages are to be available as Runtime languages on the HMI device.

##### Requirements

Multiple languages have been selected in the "Project languages" editor.

##### Procedure

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language & Font".
3. Select the following languages:

   - English
   - French
   - Italian

     ![Procedure](images/102568617611_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/102568617611_DV_resource.Stream@PNG-en-US.png)

##### Result

You have now set three Runtime languages. A number is automatically assigned to each language in the "Order" column. The enabled Runtime languages are loaded onto the HMI device with the compiled project.

If the number of languages selected exceeds the number that can be transferred to the HMI device, the table background changes color.

#### Standardizing font for all languages (RT Unified)

##### Introduction

You can standardize the font for all project languages during configuration with the "Use same font for all languages" option.

##### Requirement

- Multiple languages have been selected in the "Project languages" editor.
- Multiple languages have been selected in the "Language & font" editor.
- The same font is defined for the selected runtime languages under "Configured font".

##### Procedure

1. In the "Options > Settings > Visualization > General" menu, select the "Use same font for all languages" option.

   ![Procedure](images/102568684939_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/102568684939_DV_resource.Stream@PNG-en-US.png)

##### Result

You have enabled the option "Use same font for all languages". If you change the font of an object in one language during configuration, this font will be applied to all active languages.

#### Specific features of Asian and Eastern languages in runtime (RT Unified)

##### Introduction

Note the following special considerations for the operation in Runtime of projects for Asian languages.

> **Note**
>
> During configuration, only use the Asian fonts that your configuration computer supports.

##### Memory requirement for Asian character sets

The memory requirement is greater when using Asian languages. Therefore look out for corresponding error messages when compiling the project.

##### Font size for Asian character sets

Use at least a font size of 10 points to display the text of projects created for Asian languages in Runtime. Asian characters will become illegible if smaller font sizes are used. This also applies to the default font in the Runtime settings under "Language & font".

## Performance features (RT Unified)

This section contains information on the following topics:

- [Resources Monitor (RT Unified)](#resources-monitor-rt-unified)
- [General technical data (RT Unified)](#general-technical-data-rt-unified)
- [Permitted special characters (RT Unified)](#permitted-special-characters-rt-unified)

### Resources Monitor (RT Unified)

#### Resources Monitor of HMI devices

The resources monitor of HMI devices calculates the current number of screens, the HMI tags used, logging tags, connections and the current project size.

The calculated values are evaluated by means of the recommended and maximum permissible limits:

- OK: The number of used resources of the type lies within the recommendation.
- Warning: The number of used resources of the type exceeds the recommended value. To ensure a better performance, reduce the number.
- Error: The number of used resources of the type exceeds the maximum value. You can only load the project once you have reduced the number of affected resource types.

An overall rating is output on the basis of the evaluations of the individual resource types.

> **Note**
>
> The current project size is only displayed if you have compiled the project beforehand.

#### Procedure

1. Select the HMI device in the topology view, network view or device view.
2. In the Inspector window, navigate to "Properties > General > Resources Monitor".
3. Click "Calculate".
4. Check the comments and the overall evaluation.
5. If necessary, reduce the number of used resources of individual types.

   ![Procedure](images/170889720715_DV_resource.Stream@PNG-en-US.png)

### General technical data (RT Unified)

This section contains information on the following topics:

- [Unsupported functions (Unified Basic Panel) (RT Unified)](#unsupported-functions-unified-basic-panel-rt-unified)
- [SIMATIC Unified Basic Panel (RT Unified)](#simatic-unified-basic-panel-rt-unified)
- [SIMATIC Unified Comfort Panel (RT Unified)](#simatic-unified-comfort-panel-rt-unified)
- [SIMATIC Unified PC (RT Unified)](#simatic-unified-pc-rt-unified)

#### Unsupported functions (Unified Basic Panel) (RT Unified)

The following tables show which functions are currently not supported on a Unified Basic Panel.

##### Screen objects

- Function trend control
- Trend companion
- Media player
- Custom Web Controls
- Plant overviews

##### System functions

The following system functions can be configured in the engineering system, but are not supported by Unified Basic Panel:

- Create screenshot

##### Runtime functions

- Audit
- Reporting
- Runtime Collaboration

##### Connectivity

Unified Basic Panels can only be used as OPC UA clients and not as OPC UA servers.

Unified Basic Panels can only be used as SmartClient and not as SmartServer.

#### SIMATIC Unified Basic Panel (RT Unified)

The following tables of performance features help you to assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

Furthermore, the complexity of configuring the screens, such as the number of objects per screen, the number of tag connections, cycle times and scripts, has a significant influence on the open screen times and the performance in runtime.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

##### Tags

|  | Unified Basic 4-12" |
| --- | --- |
| Number of tags in the project | 1000 |
| Number of elements per array | 1600 ??? |

Currently, due to an error, tag arrays and tags based on user data types (UDT) are counted as 1 tag when using faceplates.

##### Alarms

|  | Unified Basic 4-12" |
| --- | --- |
| Number of alarm classes | 32 |
| Number of discrete alarms | 9000 |
| Number of analog alarms | 300 |
| Size of the alarm buffer<sup> 1)</sup> | 2000 |
| Length of an alarm in characters | 512 |
| Number of alarm texts per alarm | 10 |
| Number of process values per alarm | 10 |
| Number of queued alarm events | 750 |
| Number of controller alarms | 160000 |
| Number of OPC UA A&C alarms | 20000 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the messages of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

##### Number of alarms that can be displayed in an alarm view

The maximum number of alarms that can be displayed in runtime depends on the selected view.

|  | Unified Basic 4-12" |
| --- | --- |
| Show active alarms | No restriction |
| Show defined alarms | No restriction |
| Alarm statistics - view | No restriction |
| Show logged alarms | 1000 |
| Show and update logged alarms | 100 |

##### Screens

|  | Unified Basic 4-12" |
| --- | --- |
| Maximum size in the engineering system | 20,000 * 20,000 pixels ??? |
| Maximum size in runtime | 20,000 * 20,000 pixels ??? |
| Number of screens | 300 |
| Number of lower-level screen windows | 10 ??? |
| Number of objects per screen | 800 ??? |
| Number of objects from the "Controls" area per screen | 40 ??? |
| Number of tags per screen | 600 ??? |

##### Parameter sets

|  | Unified Basic 4-12" |
| --- | --- |
| Number of parameter set types | 750 |
| Number of parameter set type elements | 1000 |
| Number of parameter sets | 2000 |
| Reserved memory for data records in the internal Flash | 12 MB |

##### Libraries

|  | Unified Basic 4-12" |
| --- | --- |
| Number of versions of dynamic SVGs | 1000 with an average size of 10 KB |

##### Logs

|  | Unified Basic 4-12" |
| --- | --- |
| Number of logs | 50 |
| Maximum size of a log | 4 TB |
| Maximum size of a segment | 4 TB |
| Number of logging tags: | SQLite: 5000 |
| **Memory requirements of the data log** |  |
| Size of entry of logging tag | The size of the entry of a logging tag is largely determined by the data type. Depending on the data type, the following memory requirements apply:   - 32-bit value, e.g. Bool, Int, LReal, ... : ~ 80 byte / entry - 64-bit value, e.g. LInt, DateTime, LTime, … ~ 106 byte / entry - Text value (any length), e.g. WString, WChar: ~ 586 bytes/entry |
| Additional memory requirement of a segment: | SQLite: Approx. 0.5 MB |
| **Memory requirements of the alarm log** |  |
| Basic entry in the alarm log without alarm text: | SQLite: Approx. 300 bytes |
| Memory requirement of the alarm text per character and language: | SQLite: at least 1 byte |
| Additional memory requirement per language (one-off): | SQLite: Approx. 100 bytes |

##### Trends

|  | Unified Basic 4-12" |
| --- | --- |
| Number of trends | 600 |
| Number of trends per trend control | 20 |
| Number of trend areas per trend control | 2 |

##### Text lists and graphics lists

|  | Unified Basic 4-12" |
| --- | --- |
| Number of graphics lists | 750 |
| Number of text lists | 750 |
| Number of entries per text or graphics list | 750 |
| Number of graphic objects | 6000 |
| Number of text elements | 60000 |

##### Scripts

|  | Unified Basic 4-12" |
| --- | --- |
| Number of scripts | 600 |
| Number of functions per function list | 25 |

##### Scheduler

|  | Unified Basic 4-12" |
| --- | --- |
| Number of tasks, time- or event-triggered | 70 |

##### Communication

|  | Unified Basic 4-12" |
| --- | --- |
| Number of S7 connections | 8 |

##### Reporting

Reporting on Unified Basic Panels is currently not supported.

##### OPC UA

|  | Unified Basic 4-12" |
| --- | --- |
| Number of connected OPC UA clients | Unified Basic Panels can currently only be used as an OPC UA client |
| Maximum address length of OPC UA server variables for addressing by a Unified OPC UA Client | 256 characters |

##### Languages

|  | Unified Basic 4-12" |
| --- | --- |
| Number of runtime languages | 32 |

##### User management

|  | Unified Basic 4-12" |
| --- | --- |
| Number of roles | 50 |
| Number of predefined function rights | 20 |
| Number of users | 200 |

##### Project

|  | Unified Basic 4-12" |
| --- | --- |
| Size of the project files on the device | < 100 MB |

#### SIMATIC Unified Comfort Panel (RT Unified)

The following tables of performance features help you to assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

Furthermore, the complexity of configuring the screens, such as the number of objects per screen, the number of tag connections, cycle times and scripts, has a significant influence on the open screen times and the performance in runtime.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

##### Tags

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of tags in the project | 8000 |  |
| Number of elements per array | 1600 |  |

Currently, due to an error, tag arrays and tags based on user data types (UDT) are counted as 1 tag when using faceplates.

##### Alarms

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of alarm classes | 32 |  |
| Number of discrete alarms | 9000 |  |
| Number of analog alarms | 300 |  |
| Size of the alarm buffer<sup> 1)</sup> | 2000 |  |
| Length of an alarm in characters | 512 |  |
| Number of alarm texts per alarm | 10 |  |
| Number of process values per alarm | 10 |  |
| Number of queued alarm events | 750 |  |
| Number of controller alarms | 160000 |  |
| Number of OPC UA A&C alarms | 20000 |  |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the messages of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

##### Number of alarms that can be displayed in an alarm view

The maximum number of alarms that can be displayed in runtime depends on the selected view.

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Show active alarms | No restriction |  |
| Show defined alarms | No restriction |  |
| Alarm statistics - view | No restriction |  |
| Show logged alarms | 1000 |  |
| Show and update logged alarms | 100 |  |

##### Screens

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Maximum size in the Engineering System | 20,000 * 20,000 pixels |  |
| Maximum size in runtime | 20,000 * 20,000 pixels |  |
| Number of screens | 1200 |  |
| Number of lower-level screen windows | 10 |  |
| Number of objects per screen | 800 | 1200 |
| Number of objects from the "Controls" area per screen | 40 | 80 |
| Number of tags per screen | 600 | 800 |

##### Parameter sets

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of parameter set types | 750 |  |
| Number of parameter set type elements | 1000 |  |
| Number of parameter sets | 2000 |  |
| Reserved memory for data records in the internal Flash | 12 MB |  |

##### Libraries

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of versions of dynamic SVGs | 1000 with an average size of 10 KB |  |

##### Logs

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of logs | 50 |  |
| Maximum size of a log | 4 TB |  |
| Maximum size of a segment | 4 TB |  |
| Number of logging tags: | SQLite: 5000 |  |
| **Memory requirements of the data log** |  |  |
| Size of entry of logging tag | The size of the entry of a logging tag is largely determined by the data type. Depending on the data type, the following memory requirements apply:   - 32-bit value, e.g. Bool, Int, LReal, ... : ~ 80 byte / entry - 64-bit value, e.g. LInt, DateTime, LTime, … ~ 106 byte / entry - Text value (any length), e.g. WString, WChar: ~ 586 bytes/entry |  |
| Additional memory requirement of a segment: | SQLite: Approx. 0.5 MB |  |
| **Memory requirements of the alarm log** |  |  |
| Basic entry in the alarm log without alarm text: | SQLite: Approx. 300 bytes |  |
| Memory requirement of the alarm text per character and language: | SQLite: at least 1 byte |  |
| Additional memory requirement per language (one-off): | SQLite: Approx. 100 bytes |  |

##### Trends

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of trends | 600 |  |
| Number of trends per trend control | 20 |  |
| Number of trend areas per trend control | 2 | 5 |

##### Text lists and graphics lists

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of graphics lists | 750 |  |
| Number of text lists | 750 |  |
| Number of entries per text or graphics list | 750 |  |
| Number of graphic objects | 6000 |  |
| Number of text elements | 60000 |  |

##### Scripts

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of scripts | 600 |  |
| Number of functions per function list | 25 |  |

##### Scheduler

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of tasks, time- or event-triggered | 70 |  |

##### Communication

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of S7 connections | 16 |  |
| Number of connections with drivers of third-party providers <sup>1)</sup> | 16 |  |

| Symbol | Meaning |
| --- | --- |
| 1) | Only applies to Ethernet-based communication drivers  Depends on the maximum number of connections supported by the PLC type  Can be a combination of 16 different drivers of third-party providers |

##### Reporting

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of templates | 500 |  |
| Number of report tasks | 500 |  |
| Number of report tasks started at the same time | 20 |  |
| Number of reports executed at the same time | 5 |  |

##### OPC UA

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of connected OPC UA clients | 3 |  |
| Maximum address length of OPC UA server variables for addressing by a Unified OPC UA Client | 256 characters |  |

##### Languages

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of runtime languages | 32 |  |

##### User management

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Number of roles | 50 |  |
| Number of predefined function rights | 20 |  |
| Number of users | 200 |  |

##### Project

|  | Unified Comfort 7-12" | Unified Comfort 15-22" |
| --- | --- | --- |
| Size of the project files on the device | < 500 MB |  |

#### SIMATIC Unified PC (RT Unified)

The following tables of performance features help you to assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

Furthermore, the complexity of configuring the screens, such as the number of objects per screen, the number of tag connections, cycle times and scripts, has a significant influence on the open screen times and the performance in runtime.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

##### Tags

|  | SIMATIC Unified PC |
| --- | --- |
| Number of PowerTags | 600000 (depends on the license) |
| Number of internal tags | 200000 |
| Number of elements per array | 2000 |

##### Alarms

|  | SIMATIC Unified PC |
| --- | --- |
| Number of alarm classes | 32 |
| Number of discrete alarms | 200000 |
| Number of analog alarms | 10000 |
| Length of an alarm in characters | 512 |
| Number of alarm texts per alarm | 10 |
| Number of process values per alarm | 10 |
| Number of alarms for every second (continuous load) | 20 |
| Number of queued alarm events | unlimited |
| Number of alarms for every 10 seconds (alarm burst) | 8000 |
| Number of controller alarms | 160000 |
| Number of OPC UA A&C alarms | 20000 |

##### Number of alarms that can be displayed in an alarm view

The maximum number of alarms that can be displayed in runtime depends on the selected view.

|  | SIMATIC Unified PC |
| --- | --- |
| Show active alarms | No restriction |
| Show defined alarms | No restriction |
| Alarm statistics - view | No restriction |
| Show logged alarms | 1000 |
| Show and update logged alarms | 100 |

##### Screens

|  | SIMATIC Unified PC |
| --- | --- |
| Maximum size in the Engineering System | 20,000 * 20,000 pixels |
| Maximum size in runtime | 20,000 * 20,000 pixels |
| Number of screens | 2000 |
| Number of lower-level screen windows | unlimited |
| Number of objects per screen | 1500 |
| Number of tags per screen | 1000 |

##### Parameter sets

|  | SIMATIC Unified PC |
| --- | --- |
| Number of parameter set types | 1000 |
| Number of parameter set type elements | 1000 |
| Number of parameter sets | 5000 |

##### Libraries

|  | SIMATIC Unified PC |
| --- | --- |
| Number of versions of dynamic SVGs | 1000 with an average size of 10 KB |

##### Logs

|  | SIMATIC Unified PC |
| --- | --- |
| Number of logs | 100 |
| Maximum size of a log | 4 TB |
| Maximum size of a segment | 4 TB |
| Number of logging tags: | SQLite: 5000  Microsoft SQL: maximum number of PowerTags |
| Number of entries in the data log per second with Microsoft SQL | Microsoft SQL: 30000 |
| **Memory requirements of the data log** |  |
| Size of entry of logging tag | The size of the entry of a logging tag is largely determined by the data type. Depending on the data type, the following memory requirements apply:   - 32-bit value, e.g. Bool, Int, LReal, ... : ~ 80 byte / entry - 64-bit value, e.g. LInt, DateTime, LTime, … ~ 106 byte / entry - Text value (any length), e.g. WString, WChar: ~ 586 bytes/entry |
| Additional memory requirement of a segment: | SQLite: Approx. 0.5 MB  Microsoft SQL: Approx. 5 MB |
| **Memory requirements of the alarm log** |  |
| Basic entry in the alarm log without alarm text: | SQLite: Approx. 300 bytes  Microsoft SQL: Approx. 2000 bytes |
| Memory requirement of the alarm text per character and language: | SQLite: at least 1 byte  Microsoft SQL: at least 2 bytes |
| Additional memory requirement per language (one-off): | SQLite: Approx. 100 bytes  Microsoft SQL: Approx. 200 bytes |
| Additional memory requirement of a segment: | Microsoft SQL: Approx. 3.5 MB |

##### Trends

|  | SIMATIC Unified PC |
| --- | --- |
| Number of trends | 1000 |
| Number of trends per trend control | 60 |
| Number of trend areas per trend control | 5 |

##### Text lists and graphics lists

|  | SIMATIC Unified PC |
| --- | --- |
| Number of graphics lists | 1000 |
| Number of text lists | 2000 |
| Number of entries per text or graphics list | 3500 |
| Number of graphic objects | unlimited |
| Number of text elements | unlimited |

##### Scripts

|  | SIMATIC Unified PC |
| --- | --- |
| Number of scripts | unlimited |
| Number of functions per function list | 50 |

##### Scheduler

|  | SIMATIC Unified PC |
| --- | --- |
| Number of tasks, time- or event-triggered | 200 |

##### Communication

|  | SIMATIC Unified PC |
| --- | --- |
| Number of S7 connections<sup> 1)</sup> | 128 |
| Number of connections with drivers of third-party providers <sup>2)</sup> | 50 |
| <sup>1)</sup> SIMATIC NET is required to use more than 10 connections.    <sup>2)</sup>Only applies to Ethernet-based communication drivers  Depends on the maximum number of connections supported by the PLC type  Can be a combination of 50 different drivers of third-party providers |  |

##### Reporting

|  | SIMATIC Unified PC |
| --- | --- |
| Number of templates | 500 |
| Number of report tasks | 500 |
| Number of report tasks started at the same time | 20 |
| Number of reports executed at the same time | 5 |

##### OPC UA

|  | SIMATIC Unified PC |
| --- | --- |
| Number of connected OPC UA clients | 10 |
| Maximum address length of OPC UA server variables for addressing by a Unified OPC UA Client | 256 characters |

##### Languages

|  | SIMATIC Unified PC |
| --- | --- |
| Number of runtime languages | 32 |

##### Account management

|  | SIMATIC Unified PC |
| --- | --- |
| Number of roles | 50 |
| Number of predefined function rights | 20 |
| Number of users | 200 |

##### Plant objects

|  | SIMATIC Unified PC |
| --- | --- |
| Number of plant object types | 400 |
| Number of plant object instances | 65000 |
| Number of hierarchy levels | unlimited |

### Permitted special characters (RT Unified)

#### Introduction

The following table shows the restrictions that must be observed when allocating names.

#### Permitted characters

| Name | Restriction |
| --- | --- |
| Device name | The following constraints apply to the assignment of the device name:  - Do not use the following characters:   - , ; : ! ? " ' ^ ´ ` ~ _+ = / \ ¦ @ * # $ % & § ° ( ) [ ] { } < >   - Spaces - Use upper case only. - The first character must be a letter. - The first 12 characters of the device name must be unique. |
| Object names | The use of the following special characters is not supported:  - Pipe | - Forward slash / - Inverted slash \ - Dot . - Comma , - Semicolon ; - Colon : - Quotes " - Apostrophe ' - Angle brackets < > - Tilde ~ - Hash # - Dollar $ - Star * - Question mark ?   The use of the following control characters is not supported:  - \x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F   \x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F   When creating scripts, also consider the restrictions relating to special characters of the programming language. |
| User name | The use of the following special characters is not supported:  - Forward slash / - Comma , - Parenthesis { } |
| Password for Sm@rt Server | The use of the following special character is not supported:  - Hash # |
