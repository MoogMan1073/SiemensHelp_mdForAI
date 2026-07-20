---
title: "Configuring plant hierarchies (RT Unified)"
package: TIAPCPMenUS
topics: 55
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring plant hierarchies (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Elements and basic settings (RT Unified)](#elements-and-basic-settings-rt-unified)
- [Object- and technology-oriented configuration (RT Unified)](#object--and-technology-oriented-configuration-rt-unified)
- [Visualizing plant objects in runtime (RT Unified)](#visualizing-plant-objects-in-runtime-rt-unified)
- [Options (RT Unified)](#options-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Applications (RT Unified)](#applications-rt-unified)
- [Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)
- [Configuration concept (RT Unified)](#configuration-concept-rt-unified)
- [Plant model and target systems (RT Unified)](#plant-model-and-target-systems-rt-unified)
- [Structure of a plant model (RT Unified)](#structure-of-a-plant-model-rt-unified)
- [Contexts (RT Unified)](#contexts-rt-unified)

### Introduction (RT Unified)

#### Object-oriented configuration

The option of object-oriented configuration is available to you with SIMATIC WinCC Unified PC RT. Define reusable plant object types and assign the associated plant object instances in hierarchical plant views.

In this way, you can model the plant view of your machine or unit/plant, for example, based on user-defined or standardized technological objects.

The plant structure is created from individual objects, each of which represents a specific component or unit. You configure each object in the context of the operator control and monitoring solution.

In plant object types, you combine all required configuration elements for visualization, such as faceplates, tags, alarms, scripts, etc. Changes to the plant object type automatically affect all instances. This translates into real time savings, especially for plants with a high degree of standardization.

You can start object-oriented plant modeling based on the engineering data, if necessary, and can derive the configuration of the HMI devices and automation systems from this.

Break the machine or unit/plant up into reusable technological units and arrange them hierarchically in a technological plant view according to the plant structure.

![Object-oriented configuration](images/118706724235_DV_resource.Stream@PNG-de-DE.png)

The following options are available to you in technology-oriented and object-oriented configuration:

- Creating various hierarchical plant views: technological view, building view, independent of the HMI device that is used.
- Configuration of plant objects and plant object types with data elements for mapping the actual plant configuration
- Access to plant objects (data elements, HMI alarms, logs, screens, etc.)
- Generation of the screen hierarchy
- Expansion of configured plant objects and types using Plant Intelligence options, e.g. WinCC Unified Performance Insight or WinCC Unified Sequence Execution

#### Software requirements

You acquire the following products to use technology- and object-oriented configuration:

- TIA Portal V16 or higher with WinCC Unified

The "Plant objects" area is visible under Project tree after the installation of WinCC Unified.

#### Supported devices

The following SIMATIC S7 controllers are supported:

- SIMATIC S7-1500 with the exception of the SIMATIC S7-1500 Software Controller

---

**See also**

[Applications (RT Unified)](#applications-rt-unified)
  
[Overview (RT Unified)](#overview-rt-unified)
  
[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)

### Applications (RT Unified)

#### Overview

You use technology-oriented and object-oriented configuration for automation solutions to increase overall effectiveness.

In particular, in plants with high level of standardization, the object-oriented approach increases the configuration efficiency through the reuse of objects, the capability of changing objects centrally, and the integration of manufacturing execution system functionalities such as the calculation of individual key indicators for separate machines.

Technology-oriented and object-oriented configuration supports you in the following operating phases:

- Planning phase: Efficient plant configuration and simple plant expansion through integration of part models from other projects
- Plant maintenance: Transparency through mapping of the exact plant structure
- Quality management: Continuous optimization of your projects

#### Advantages

- Creation and generation of modular projects based on standardized plant objects
- Reduced engineering workloads and fewer inconsistencies with a shared model in Engineering and Runtime
- Simple plant expansion through integration of part models from other projects
- Creating the screen hierarchy
- Transparent access to all objects and their properties and methods, independent of device assignment
- Targeted corrective measures through transparent relationships of individual plant objects
- Intelligent use of information from the entire manufacturing environment in combination with Plant Intelligence options

#### Operation in runtime

Depending on your configuration, the following possibilities are available to you in runtime:

- Display hierarchy path of alarm source
- Filter alarm control by plant objects
- Display alarm status of a line and navigation to the alarm source
- Display the most frequently occurring alarms, filtered by plant object or plant object type
- Area-based access protection
- Screen navigation via the plant model
- Determine the energy consumption of a line and compare with another line
- Analysis based on plant objects

The plant hierarchy is also available for scripting in runtime.

![Operation in runtime](images/113018336395_DV_resource.Stream@PNG-de-DE.png)

#### Requirements on the configuration engineer

The following prior knowledge is required for using technology-oriented and object-oriented configuration:

- You have experience performing configuration in STEP 7 and WinCC.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified)
  
[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)

### Type/instance concept in object-oriented configuration (RT Unified)

#### Introduction

The object-oriented approach of WinCC based on the type-instance concept. In types, you create central properties for an object. The instances represent local places of use for the types.

Plant objects are instances of a plant object type.

The plant object type is the central, object-oriented definition of a reusable plant component (such as conveyor robot). As instances of the plant object type, the plant objects generally map concrete, physically existing plant components (e.g. conveyor robot_A and conveyor robot_B).

If you change a property of a plant object type, the property is saved centrally and also changed in all instances.

#### Effect of the type instance concept on object-oriented configuration

The use of a type is called an instance. The common plant model is generated from instances. Each instance inherits all the properties of the type. The Common Plant Model with high level of standardization is characterized by the use of many instances of few types in the model.

The general types of the plant units are configured and these are reused when required in the configuration and adapted to the specific plant objects. The plant structure hereby specifies the addressing of the plant objects.

![Effect of the type instance concept on object-oriented configuration](images/111356211851_DV_resource.Stream@PNG-de-DE.png)

In the object-oriented approach of WinCC the following correspondences apply:

- Type = Plant object type
- Instance = Plant object

The following figure shows the basic structure of a plant model:

![Effect of the type instance concept on object-oriented configuration](images/79747326219_DV_resource.Stream@PNG-de-DE.png)

#### Plant objects and plant object types

A plant object is a technological unit. In a plant object, the components are stored in a typical form which is required for modeling a plant.

A valid plant object must be created from a plant object type. The plant structure is created from plant objects.

The definition of a plant object type consists of the data structure and context information:

- Alarms
- Logging
- Visualization
- Data member (internal and external)
- Facets (e.g. performance indicators)

#### Type definition in terms of high reuse

A plant object type is used to describe a plant object independently of its use in the Common Plant Model. Define a plant object type as generally as possible and as specifically as required. Take into account the following aspects:

- Identical data structure in PLC (function block or PLC UDT)

  Example: Pumps that have different performance ranges are installed in a plant. The data structure in the PLC is identical for each pump. Map these pumps with a common plant object type. At each instance you configure the specific value ranges for the respective performance ranges.

  A pump function block (standard FB for a pump) is available on the control side. The customer defines the plant object type "Pump" based on this function block. The data structure of the plant object type is taken over directly from the block. Only the HMI relevant properties from the function block are hereby transferred. They are automatically updated when the block changes. Simply parameterize an instance of the function block as process connection of the plant objects.
- Similarity

  When you have similar plant object types, check if it possible to map these with a common plant object type:

  ![Type definition in terms of high reuse](images/79747334155_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Example: A pump is installed in a plant in two different variants: - Variant 1 only measures the flow rate. - Variant 2 measures the temperature in addition to the flow rate. Effects on the definition of the plant object types:  - You map each of the two pumps with a single plant object type. The representation in the Common Plant Model hereby corresponds to reality. - There is more configuration work. |
  | ② | The common intersection of the two pumps is measuring the flow. |
  | ③ | If, for example, you can do without measuring the temperature for operation, define only one plant object type: - There is less configuration work. - The two variants of the pumps are not fully represented in the Common Plant Model. |

#### Effects of changes on plant object types

The following figure shows how changes to the plant object type affect its instances, i.e. plant objects:

![Effects of changes on plant object types](images/79747330187_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Overview (RT Unified)](#overview-rt-unified)
  
[Options for creating plant objects (RT Unified)](#options-for-creating-plant-objects-rt-unified)
  
[Introduction (RT Unified)](#introduction-rt-unified)
  
[Applications (RT Unified)](#applications-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)
  
[Plant model and target systems (RT Unified)](#plant-model-and-target-systems-rt-unified)

### Configuration concept (RT Unified)

#### Requirements

- You have experience in configuring with WinCC and STEP 7.
- The TIA Portal project has been created.
- The WinCC Unified PC RT HMI device has been created.
- A SIMATIC S7-1500 PLC has been created.
- Data blocks are configured in the PLC.

#### Workflow for configuration

The starting point for the definition of a standardized object-oriented plant model in object oriented configuration is the existing plant structure.

If you want to create a plant structure, use the following sequence of steps as a guide:

- Analyze the plant structure and break it down into units and components (plant objects)
- Identify required plant object types
- Define data of the plant object types based on FBs and PLC UDTs
- Define hierarchical plant view using instances
- Create a target system
- Map the plant structure
- Position plant objects in the plant structure
- Add functional facets to object types, e.g. assign shift calendars for all machines of a line or plant

![Workflow for configuration](images/118729947019_DV_resource.Stream@PNG-de-DE.png)

| ![Workflow for configuration](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| If you are using pre-planning and automation engineering tools, you can have your plant structure automatically created via TIA Portal Openness. Next, set up the process connection of the plant objects via TIA Portal Openess. |  |

#### Differences between device-oriented and object-oriented configuration

In technology- and object-oriented configuration, you work with objects with relevant names instead of individual tags or faceplates, for example.

You have access to all objects and their properties, methods, etc. in the hierarchy, independent of HMI device assignment.

The equipment from different products and versions is integrated in the object-oriented configuration.

#### Using multiuser engineering

If you use multiuser engineering in object oriented configuration, you can save your changes only in the server project view. You cannot check the changes you make in the local session into the server project.

You can find more information on Multiuser Engineering in "Using Multiuser Engineering".

---

**See also**

[Creating plant objects (RT Unified)](#creating-plant-objects-rt-unified)
  
[Structure of a plant model (RT Unified)](#structure-of-a-plant-model-rt-unified)
  
[Creating plant object types (RT Unified)](#creating-plant-object-types-rt-unified)
  
[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Creating a plant hierarchy (RT Unified)](#creating-a-plant-hierarchy-rt-unified)
  
[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)
  
[Plant model and target systems (RT Unified)](#plant-model-and-target-systems-rt-unified)
  
[Applications (RT Unified)](#applications-rt-unified)

### Plant model and target systems (RT Unified)

#### Configuration of the plant model

When the configuration of a visualization solution begins, the development of the automation solution often takes place in the final phase. Initially, only the actual plant structure is relevant for mapping the plant model. Whether this involves one or multiple target systems is initially irrelevant.

There are always two views in a WinCC project:

- Device view with configured target systems
- Object-oriented view (common plant model)

You can perform configuration independently in both views.

#### Process connection of the plant model

The target systems are the interface between the common plant model and the process. One or more connections to PLCs are configured on each target system. The plant objects communicate with the PLCs over the target systems.

Your project must meet the following conditions for productive use:

- Each plant view is assigned to a HMI device.
- Each plant object with a process connection is also connected to a PLC.

The following figure shows a schematic representation of the mapping of plant objects to the configured target systems and PLCs:

![Process connection of the plant model](images/130340483979_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Process connection of the plant model](images/80842258187_DV_resource.Stream@PNG-de-DE.png) | Plant objects without a process connection as representation of a unit |
| ![Process connection of the plant model](images/80842262155_DV_resource.Stream@PNG-de-DE.png) | Plant objects with process connection |
| ![Process connection of the plant model](images/80842266123_DV_resource.Stream@PNG-de-DE.png) | Runtime server (target system) |
| ![Process connection of the plant model](images/80842334091_DV_resource.Stream@PNG-de-DE.png) | PLC |

---

**See also**

[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)

### Structure of a plant model (RT Unified)

#### Basic principles

With object oriented configuration, a configured plant object corresponds to a real plant object. Basically, the number of plant objects is determined by the plant hierarchy.

Whether you need to map each plant object with a plant object type is determined by the following factors:

- Relevance of the plant object type for the process visualization
- Depth of the plant hierarchy that is to be mapped
- Degree of reuse

The specific function of a plant object is clear from its position in the plant hierarchy.

For example, the function of a "Drive" plant object is only revealed in the plant hierarchy:

![Basic principles](images/108808547595_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Process for filling beer into bottles |
| ② | Drive for conveyor belt |
| ③ | Drive for robot |

#### Depth of the plant hierarchy

Define any depth of the plant hierarchy The depth of the plant hierarchy depends essentially on the number of plant objects. A deep plant hierarchy leads to a precise fault localization. You can then, for example, formulate the concise alarm text.

The context of the plant object is also taken into account in runtime, for example, in the localization of faults. The following figure uses the example of the "Temperature exceeded" alarm to show the advantage a deep hierarchy offers in runtime:

![Depth of the plant hierarchy](images/130341855115_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Representation of the message in an alarm control:  "Brewery.Filling.Paletting.Robots.Drive.Temperature exceeded"  The Common Plant Model with deeper hierarchy leads to a precise fault localization. You can therefore formulate the alarm text concisely. |
| ② | Since the drive for the robot is based on the same plant object type, the context of the alarm is automatically correct when a fault occurs:  "Brewery.Filling.Paletting.Robots.Drive.Temperature exceeded" |

#### Configuration data at the plant object type

The following configuration data are created during the definition of a plant object type:

- Properties through which data is exchanged inside and outside of WinCC Unified PC RT.
- HMI visualization: Alarms, logs
- KPIs

---

**See also**

[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)

### Contexts (RT Unified)

Contexts allow you to view plant units according to a certain viewpoint, e.g. according to a certain customer, product, job or shift.

#### Principle

Contexts always belong to a plant object. They are indicated as follows:

- User-defined contexts:

  Using a program created with the ODK API
- System-generated contexts:

  For installed Performance Insight and Calendar option packages: Automatically in Runtime

  Example: When a shift starts in Calendar, an archived context value is created with the shift ID

Each time a context (e.g. "Product") is executed, a log entry is generated in the context log. The logged context saves:

- The context value (e.g. "orange lemonade")
- Start time and end time of the execution time
- The quality code

#### Contexts in the trend control and alarm control

You can filter the content of these controls so that only data that has been generated in a specific plant unit and for the context you have selected is displayed. To do this, select a plant object, a context and one of its logged context values.

Example:

A press house produces juices for various beverage brands. Using contexts, employees can display in Runtime which alarms have occurred:

- During the production of a specific product (e.g. natural apple juice, clear apple juice, pear juice)
- For orders for a specific customer (e.g. Johnson, Smith or Miller).
- During a specific shift (e.g. early shift, late shift, night shift).

#### Contexts in the "Reports" control

You have the option of linking the generation of reports to the execution of contexts.

If the templates are configured appropriately, the reports available in the control can also contain information about contexts. If a report was generated as an Excel file and reads both contexts and alarms or tag values, you can then use the Excel filter function to filter the alarms and tags by context.

---

**See also**

[Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)

## Elements and basic settings (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Options for creating plant objects (RT Unified)](#options-for-creating-plant-objects-rt-unified)

### Overview (RT Unified)

#### "Plant objects" area

To access object-oriented configuration, click on "Plant objects" in "Project tree".

!["Plant objects" area](images/130344350603_DV_resource.Stream@PNG-en-US.png)

① "Plant objects" area for object-oriented configuration

② Plant object specific tabs, e.g. "Interface", "Visualization", etc.

③ "Plant object types" task card

④ Tabs for the configuration of alarms and logs for plant objects

Create the plant view under "Project tree > Plant objects". You can create a plant view in a project. The plant view is filled with plant nodes and thus maps your plant. Plant nodes act as structural elements. Create plant objects based on the plant object types created in the project.

In the "Plant objects" area you assign an HMI device to the plant view.

#### "Plant object types" task card

Under "Plant object types", create the plant object types from which you create plant objects.

!["Plant object types" task card](images/106510283787_DV_resource.Stream@PNG-en-US.png)

#### "Interface" tab

Plant object types are edited in "Interface" create tags for the communication between a PLC and an HMI device, create members for plant object types, and create alarms and logging tags.

!["Interface" tab](images/131141244683_DV_resource.Stream@PNG-en-US.png)

#### "Visualization" tab of the plant object types

In the "Visualization" tab of a plant object type, you link a faceplate type with the plant object type.

#### "Visualization" tab of the plant objects

Under "Visualization", you configure a screen for each plant object. In the Inspector window you edit the properties and events of the screen.

The faceplate type associated with the plant type is displayed. The configured tags of the interface are displayed, but cannot be edited.

!["Visualization" tab of the plant objects](images/130358379019_DV_resource.Stream@PNG-en-US.png)

If you open a screen under "Visualization" by double-clicking, the view is identical to the view on an HMI device. The "Toolbox" and "Layout" task cards are also identical.

Use the "Toolbox" task card to configure in predefined objects in your screens, with which you map your plant, display process sequences and define process values.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified)
  
[Options for creating plant objects (RT Unified)](#options-for-creating-plant-objects-rt-unified)
  
[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)

### Options for creating plant objects (RT Unified)

#### Basics

You have several options for creating plant objects on the basis of plant object types:

- Creation of plant object types from the function blocks or PLC user data types of an S7-1500 and creation of plant objects from the instance data blocks

  ![Basics](images/130382548747_DV_resource.Stream@PNG-de-DE.png)
- Creation of plant object types within WinCC without an S7-1500

  ![Basics](images/111035861131_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Overview (RT Unified)](#overview-rt-unified)
  
[Type/instance concept in object-oriented configuration (RT Unified)](#typeinstance-concept-in-object-oriented-configuration-rt-unified)

## Object- and technology-oriented configuration (RT Unified)

This section contains information on the following topics:

- [Working with plant views (RT Unified)](#working-with-plant-views-rt-unified)
- [Working with plant objects and plant object types (RT Unified)](#working-with-plant-objects-and-plant-object-types-rt-unified)
- [Configuring screens (RT Unified)](#configuring-screens-rt-unified)
- [Configuring the controls (RT Unified)](#configuring-the-controls-rt-unified)
- [Configuring alarms (RT Unified)](#configuring-alarms-rt-unified)
- [Configuring the logging of plant object types (RT Unified)](#configuring-the-logging-of-plant-object-types-rt-unified)
- [Good Manufacturing Practice (RT Unified)](#good-manufacturing-practice-rt-unified)
- [Example (RT Unified)](#example-rt-unified)

### Working with plant views (RT Unified)

This section contains information on the following topics:

- [Creating a plant hierarchy (RT Unified)](#creating-a-plant-hierarchy-rt-unified)
- [Assigning a plant hierarchy to a HMI device (RT Unified)](#assigning-a-plant-hierarchy-to-a-hmi-device-rt-unified)
- [Creating plant nodes (RT Unified)](#creating-plant-nodes-rt-unified)

#### Creating a plant hierarchy (RT Unified)

##### Introduction

Create a plant view to map the structure of your plant. You fill the plant view with plant objects and plant nodes and thus map your plant. Plant nodes act as structural elements.

Assign the plant view to a HMI device.

##### Requirement

- The TIA Portal project has been created.

##### Procedure

1. Under "Project tree > Plant objects", click on "Add new plant view".

   An empty plant view is created.
2. Rename the plant view accordingly.

**Note**

A plant view is supported in each project.

**Note**

The following options are not available for the "Plant view" object:

- Paste
- Cut
- Drag-and-drop

---

**See also**

[Assigning a plant hierarchy to a HMI device (RT Unified)](#assigning-a-plant-hierarchy-to-a-hmi-device-rt-unified)
  
[Creating plant objects (RT Unified)](#creating-plant-objects-rt-unified)
  
[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)

#### Assigning a plant hierarchy to a HMI device (RT Unified)

##### Introduction

To operate the plant in runtime, always assign a plant view to an HMI device.

A plant view can only be assigned to a HMI device.

##### Requirement

- A plant view has been created.
- The WinCC Unified PC RT HMI device has been created.

##### Procedure

1. Select the "Plant view" node.
2. Select the "Assign HMI device" entry from the shortcut menu.

   A "Select an HMI device for assignment" dialog appears.

   ![Procedure](images/108344257291_DV_resource.Stream@PNG-en-US.png)
3. Select the HMI device.

   The plant view and all lower-level plant objects are assigned to the HMI device.

   If a plant view was assigned to a HMI device, the assignment is visible under "Project tree > Plant objects".

---

**See also**

[Creating plant objects (RT Unified)](#creating-plant-objects-rt-unified)
  
[Creating plant object types (RT Unified)](#creating-plant-object-types-rt-unified)
  
[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Creating a plant hierarchy (RT Unified)](#creating-a-plant-hierarchy-rt-unified)

#### Creating plant nodes (RT Unified)

##### Introduction

Plant nodes help you structure your plant.

##### Requirement

- The plant view has been created and is displayed.

##### Procedure

1. Open the shortcut menu in the plant view.
2. Select "Add new node".

   The plant node is created.
3. Rename the plant node.

### Working with plant objects and plant object types (RT Unified)

This section contains information on the following topics:

- [Creating plant object types (RT Unified)](#creating-plant-object-types-rt-unified)
- [Creating plant objects (RT Unified)](#creating-plant-objects-rt-unified)
- [Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
- [Configuring plant object types from the data blocks of an S7-1500 (RT Unified)](#configuring-plant-object-types-from-the-data-blocks-of-an-s7-1500-rt-unified)
- [Assigning process data to plant objects (RT Unified)](#assigning-process-data-to-plant-objects-rt-unified)

#### Creating plant object types (RT Unified)

##### Introduction

You create plant object types.

Then define the "Communications driver" property of the interface:

- "<Internal communication>": Create data members for internal communication.
- "SIMATIC S7 1200/1500": Use either function blocks or the PLC user data types of an S7-1500.

  You can add further data members to the linked structure.

##### Requirement

- A project is open.
- A SIMATIC S7-1500 PLC has been created.

##### Procedure

Create plant object types in the "Plant object types" task card.

1. To display the "Plant object types" task card, click the "Show plant object types" button under "Project tree > Plant objects".
2. To create a plant object type, click "Add new plant object type".

   An empty plant object type is created.
3. Rename the created plant object type accordingly.
4. To edit the plant object type or create lower-level objects and members for the plant object type, double-click the plant object type in the "Plant object types" tab.

   The plant object type appears under "Interface".

**Note**

The "Communications driver" property is editable for the plant object types. The property "PLC tag" can only be edited with the communications driver "SIMATIC S7 1200/1500".

---

**See also**

[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Example: Determine plant object type (RT Unified)](#example-determine-plant-object-type-rt-unified)
  
[Assigning a plant hierarchy to a HMI device (RT Unified)](#assigning-a-plant-hierarchy-to-a-hmi-device-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)

#### Creating plant objects (RT Unified)

##### Introduction

You create plant objects from a plant object type using drag-and-drop operation.

Plant objects are specific versions or instances of a plant object type.

##### Requirement

- A project is open.
- A plant object type has been created.

##### Procedure

1. Open the "Plant objects" tab in the "Project tree" area.
2. Open the "Plant object types" task card.
3. Drag the plant object type from the task card to the plant view.

   An empty plant object is created.
4. Rename the plant object accordingly.

**Note**

The name of a plant object must only be assigned once within a project.

---

**See also**

[Configuration concept (RT Unified)](#configuration-concept-rt-unified)
  
[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Assigning a plant hierarchy to a HMI device (RT Unified)](#assigning-a-plant-hierarchy-to-a-hmi-device-rt-unified)
  
[Creating a plant hierarchy (RT Unified)](#creating-a-plant-hierarchy-rt-unified)

#### Configure plant object types (RT Unified)

##### Introduction

Configure the plant object types either from the function blocks and PLC user data types of an S7-1500 or create the properties and the external and internal data members for the plant object types.

In both cases you can extend the structure the created plant object types with additional internal or external data members.

Configuration without using function blocks is described below.

##### Requirement

- The WinCC Unified PC RT HMI device has been created.
- A plant view has been created and assigned to the HMI device.
- A plant object type has been created.
- A SIMATIC S7-1500 PLC has been created.
- Tags have been configured in the S7-1500.

##### Procedure

1. Double-click the plant object type in the "Plant object types" editor.

   An empty plant object type with the "Struct" data type appears under "Interface".
2. To add data members to the plant object type, select the plant object type and click "Insert object".

   ![Procedure](images/131141244683_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131141244683_DV_resource.Stream@PNG-en-US.png)

   The created data member inherits all properties from the higher level plant object type.

   "Internal communication" is selected by default in the column "Communications driver" for the newly created data members of the plant object types.
3. If you want to configure an external data member, select "SIMATIC S7-1500" in the "Communication driver" column.
4. Assign a PLC tag to the external data member in the "Tag" column.

> **Note**
>
> If an HMI device is assigned to the plant view, it is possible to view the data members in the "HMI tags" editor in the "Plant object tags" tab. You also have write rights for the "Comment" column.
>
> You can also use the configured data members in screens of an assigned HMI device, e.g., for dynamization instead of tags.

| ![Procedure](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Differentiate between identically named plant objects and plant object types using the "Insert object" button in the "Interface" tab. If the "Insert object" button is enabled, you have selected a plant object type. If you have selected a plant object, the "Insert object" button is disabled. |  |

---

**See also**

[Creating plant object types (RT Unified)](#creating-plant-object-types-rt-unified)
  
[Structure of a plant model (RT Unified)](#structure-of-a-plant-model-rt-unified)
  
[Creating plant objects (RT Unified)](#creating-plant-objects-rt-unified)
  
[Assigning a plant hierarchy to a HMI device (RT Unified)](#assigning-a-plant-hierarchy-to-a-hmi-device-rt-unified)
  
[Configuration concept (RT Unified)](#configuration-concept-rt-unified)
  
[Creating a plant hierarchy (RT Unified)](#creating-a-plant-hierarchy-rt-unified)
  
[Configuring plant object types from the data blocks of an S7-1500 (RT Unified)](#configuring-plant-object-types-from-the-data-blocks-of-an-s7-1500-rt-unified)
  
[Assigning process data to plant objects (RT Unified)](#assigning-process-data-to-plant-objects-rt-unified)

#### Configuring plant object types from the data blocks of an S7-1500 (RT Unified)

##### Introduction

Configure the plant object types either from the data blocks of an S7-1500 or define the properties and the external and internal data members for the plant object types without connection to a PLC.

In both cases you can extend the structure the created plant object types with additional internal or external data members.

Configuration from the data blocks of an S7-1500 PLC is described below.

Configure plant object types from the configured program blocks of an S7-1500 PLC using drag-and-drop operation.

##### Requirement

- The WinCC Unified PC RT HMI device has been created.
- A plant view has been created and assigned to the WinCC Unified PC RT.
- A plant object type has been created.
- A SIMATIC S7-1500 PLC has been created.
- A function block is configured in the SIMATIC S7-1500 PLC.

##### Procedure

1. Open the plant object type in the "Interface" tab.
2. Set the "Communication driver" parameter to the SIMATIC S7-1500 PLC that contains a configured function block.
3. Navigate to the function block in the PLC.
4. Select the function block.
5. Drag the function block to the "PLC tags" field in the "Interface" tab.

   The corresponding structure with data members based on the function block is created in the "Interface" tab.

   When you edit the blocks of the PLC, these changes are automatically transferred to the plant object types.
6. To add additional data members to the plant object type, select the plant object type and click "Insert object".
7. If necessary, adjust the data type of the data member.
8. To clear the connection between of a controller and the data members object, delete the block in the "PLC tag" column or select "None".

**Note**

You can create additional data member for each plant object type.

Function blocks (FBs) or PLC user data types act as basis for the configuration of the plant object types and their data members.

A member structure can also be connected to a PLC type, for example, function block (FB) or PLC user data type.

"Raw" data types and arrays are also supported.

An assignment of the controller blocks to the external data members of the plant object types is only possible if names and data types are identical in the PLC and in the plant object type.

| ![Procedure](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Differentiate between identically named plant objects and plant object types using the "Insert object" button in the "Interface" tab. If the "Insert object" button is enabled, you have selected a plant object type. If you have selected a plant object, the "Insert object" button is disabled. |  |

> **Note**
>
> If an HMI device is assigned to the plant view, it is possible to view the data members in the "HMI tags" editor in the "Plant object tags" tab. You also have write rights for the "Comment" column.
>
> You can also use the configured data members in screens of an assigned HMI device, e.g., for dynamization instead of tags.

---

**See also**

[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Assigning process data to plant objects (RT Unified)](#assigning-process-data-to-plant-objects-rt-unified)

#### Assigning process data to plant objects (RT Unified)

##### Introduction

To establish the communication between a S7-1500 controller and a WinCC Unified PC RT device, connect a plant object with a PLC tag or a data block of the PLC.

##### Requirement

- An S7-1500 PLC and a WinCC Unified PC RT HMI device are configured and connected.
- At least one plant object type in the project contains PLC user data types or function blocks (FBs).

##### Procedure

1. Drag a plant object type to the plant view.

   The plant object is created based on the plant object type.
2. Double-click the plant object.
3. In the "Interface" tab, in the "Connection" column, select the configured HMI connection for all external data members of the plant object type.

   Select only between the HMI connections that are created for the S7-1500 controllers available in the project.
4. In the "PLC tag" column, select a PLC tag.

> **Note**
>
> In the "Interface" tab, similar to in the "HMI tags" editor, you can view or edit the properties in the following areas:
>
> - "General"
> - "Settings"
> - "Range"
> - "Linear scaling"
> - "Values"
> - "Comment"

---

**See also**

[Configure plant object types (RT Unified)](#configure-plant-object-types-rt-unified)
  
[Configuring plant object types from the data blocks of an S7-1500 (RT Unified)](#configuring-plant-object-types-from-the-data-blocks-of-an-s7-1500-rt-unified)

### Configuring screens (RT Unified)

This section contains information on the following topics:

- [Basic information on configuring screens (RT Unified)](#basic-information-on-configuring-screens-rt-unified)
- [Configuring screens for plant objects (RT Unified)](#configuring-screens-for-plant-objects-rt-unified)

#### Basic information on configuring screens (RT Unified)

##### Overview

The configuration of screens for operating and monitoring is also available to you in object-oriented configuration. This means that you are working in two areas, under "Project tree> Devices" and "Project tree > Plant objects > Visualization". Here you work with both screens and faceplates that also support the type-instance concept.

In the area "Project tree > Devices", configure screens for HMI devices as usual. In the screens, also configure companion controls that are relevant for the display of screens of the plant objects.

In the "Project tree > Plant objects > Visualization" area, you configure screens for plant objects.

In the "Plant object types > Visualization" area, configure faceplates for plant object types.

In the areas under "Project tree > Devices" and "Project tree > Plant Objects > Visualization", the same predefined screen objects are available in the "Toolbox" task card.

When configuring faceplates, a minimized tool area is available under "Toolbox".

##### Configuration options

Under "Project tree > Devices", you configure a screen for the created HMI device with the "Plant overview" control and one of the companion controls, such as a screen window. In runtime, navigate the plant structure to the plant objects via the "Plant overview" control. The screen windows in the plant overview display the screens that you have previously configured for the plant object.

The companion controls are connected to one another and supplement one another in displaying the data values.

The following controls can act as companion control for the plant overview:

- Alarm control
- Screen window
- Calendar control (when using the WinCC Unified Calendar option)

When required, configure controls as usual, e.g. screen windows, alarm control, or trend control. Select the specific plant object in the plant hierarchy as data source for the alarm control and trend control. Configure the alarm control and trend control for plant objects on the basis of the data members of the plant object types. The procedure for configuring these controls does not differ from the procedure for the device-specific configuration.

The following options are available in runtime:

- Display the hierarchy path of the alarm source
- Display the hierarchy path of the trend values
- Filter the alarm control by plant objects
- Display process values for the selected plant object

Use the "Visualization" tab for the direct visualization of plant objects and plant object types. You can create one screen for each plant object, and you can link one faceplate type for each plant object type. The type-instance concept is used for configuring the screens for plant objects and plant object types. All relevant elements are contained in the faceplate type of a plant object type. Drag a plant object into the screen. A faceplate container is created. For example, several faceplates can be integrated into one visualization of a higher-level plant object.

![Configuration options](images/128942649483_DV_resource.Stream@PNG-en-US.png)

##### Configuration steps

In general, proceed in the following order when configuring the screens for your plant:

1. Configure plant object types.
2. Configure faceplates for plant object types.
3. Create plant objects from plant object types.
4. Create screens for plant objects.
5. For the display in runtime, configure the "Plant hierarchy" and "Screen window" controls in a screen of the HMI device.

##### Displaying plant objects and plant object types

In general, you do not have to create a screen for each plant object. Create an overview for the higher-level plant object. Then create faceplates for the plant object types and drag them to the overview screen of the higher-level plant object using drag-and-drop.

If the screens of the plant objects need to differ from the screens used for the plant object types, you can use the faceplates of the plant object types as a basis and configure additional elements.

In runtime, select a plant object in the "Plant overview" control to display its screen.

---

**See also**

[Configuring screens for plant objects (RT Unified)](#configuring-screens-for-plant-objects-rt-unified)
  
[Configuring faceplates (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#configuring-faceplates-rt-unified)
  
[Example: Configuring screens for brewery production lines (RT Unified)](#example-configuring-screens-for-brewery-production-lines-rt-unified)

#### Configuring screens for plant objects (RT Unified)

##### Introduction

You configure an overview screen for the higher-level plant object with multiple faceplate containers for lower-level plant objects, for example, for a station that has lower-level objects motor and conveyor belt.

For each plant object you can configure a screen in which all lower-level plant objects are visible. To do this, use the faceplate containers of the plant object types.

If necessary, you also configure basic objects, elements and controls in the screen. For example, you use I/O fields to display process values such as status, temperature and rate.

In the following, you will obtain the data to be processed, such as temperature measurements or speed values from the data blocks of a controller.

You represent lower-level plant objects using faceplates in the overview screen of the higher-level plant hierarchy.

In runtime, the screen window technology assists you in switching between plant objects and representing multiple plant objects in a screen.

You can also use the "Plant overview" control to set up screen navigation via the plant. In runtime, you monitor the plant in this manner and see the overall progress at a glance.

##### Requirement

- A SIMATIC S7-1500 has been configured in the project.
- WinCC Unified Runtime is configured in the project.
- A plant object type has been created.
- The plant view has been created with the plant objects and assigned to WinCC Unified PC RT.
- The interface tags of the plant object types are linked to the S7-1500.

##### Procedure

1. Open the plant object editor.
2. In the "Visualization" tab, click "Add new screen".

   A screen is created.
3. If necessary, edit the width and height of the screen under "Properties" in the inspector window.
4. If necessary, configure the required elements and controls for the plant object, such as I/O fields and text fields.
5. Change to the "Libraries" task card.
6. Open the project library.
7. Create a faceplate type.
8. Configure the required screen objects, interface tags and interface properties in the faceplate type and release the version.
9. Open the editor of the plant object type.
10. In the "Visualization" tab, drag the faceplate type from the project library to the "Drop faceplates here" button.
11. Connect the faceplate tags to the interface tags of the plant object type.
12. Create a plant object from the plant object type using a drag-and-drop operation.
13. Open the plant object editor.
14. Assign the plant object a PLC tag under "Interface" in the "PLC tag" column:
15. To display the faceplate container of the plant object type in the screen, drag the plant object from the plant view to the configured screen.

| ![Procedure](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Adjust the position of the faceplate container in the overview screen using the mouse or the corresponding icons on the toolbar. - You can zoom in and out of the faceplate container in the overview screen. - You can at any time delete and reconfigure the overview screen which contains the faceplate container for lower-level plant objects. You can reuse the faceplate types at any time. |  |

> **Note**
>
> If the screen area is not sufficient for all faceplate containers, the faceplate containers are superimposed on each other in runtime.

> **Note**
>
> If additional basic objects, elements and controls are required specifically for a plant object, you can use the faceplates of the plant object types as a basis and configure additional objects.

> **Note**
>
> Note that interface mapping is deleted during updates of faceplate types used in plant objects.

##### Result

You have created a screen with a faceplate instance for the plant project.

---

**See also**

[Operating "Plant overview" in runtime (RT Unified)](#operating-plant-overview-in-runtime-rt-unified)
  
[Basic information on configuring screens (RT Unified)](#basic-information-on-configuring-screens-rt-unified)
  
[Configuring an alarm control for plant objects (RT Unified)](#configuring-an-alarm-control-for-plant-objects-rt-unified)
  
[Example: Configuring screens for brewery production lines (RT Unified)](#example-configuring-screens-for-brewery-production-lines-rt-unified)

### Configuring the controls (RT Unified)

This section contains information on the following topics:

- [Configuring "Plant overview" control and companion controls (RT Unified)](#configuring-plant-overview-control-and-companion-controls-rt-unified)
- [Configuring an alarm control for plant objects (RT Unified)](#configuring-an-alarm-control-for-plant-objects-rt-unified)
- [Configuring trend control for plant objects (RT Unified)](#configuring-trend-control-for-plant-objects-rt-unified)

#### Configuring "Plant overview" control and companion controls (RT Unified)

##### Introduction

You require the control "Plant overview" when you want to navigate through the plant.

The companion controls are connected to one another and supplement one another in displaying the data values.

You require the companion controls for the following displays:

- Display plant object screens and screen windows using the navigation option throughout the entire plant (plant overview and screen windows)
- Display alarms for plant objects using the navigation option throughout the entire plant (plant overview and alarm view)

The following controls can act as companion control for the plant overview:

- Alarm control
- Screen window
- Calendar view (when using the WinCC Unified Calendaroption)

##### Requirement

- A screen is open.
- The "Toolbox" task card is open.

##### Procedure

1. Insert the "Plant overview" control from the "Toolbox > My controls" task card into the screen.

   ![Procedure](images/140103831179_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/140103831179_DV_resource.Stream@PNG-de-DE.png)
2. Add a companion control.

   Select from the following controls:

   - Alarm control
   - Screen window
   - Calendar control
3. Select the "Plant overview" control.
4. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface > Companion control".

   The "Companion control" editor opens on the right-hand side of the Inspector window.
5. Click "Add".

   An element (starting with 0) is created.
6. Create an element for each companion control:
7. Specify the control type for each element:

   - Alarm control
   - Display window (for screen windows)
   - Calendar control (for calendar control)
8. Define the respective companion control as control reference for each element.
9. Specify a filter:

   - No filters: You see all plant objects
   - By plant objects for which alarms are available
   - By plant objects for which screen windows are configured
10. Specify the navigation type:

    - Static: The plant tree is displayed completely in runtime.
    - Dynamic: In runtime, you specify as of which level the plant tree is displayed by double-clicking a plant object.

      The levels below the selected plant object are available and are expanded.

      You can always navigate to the next higher level in runtime.

    The buttons of the toolbar and the filter bar relate to the displayed area.
11. Specify the root node. You have the following options:

    - In the "Static value" column, specify the path of the plant object according to the following schema "HMI_device.hierarchy::Plant view/Plant object", for example, "HMI_RT_1.hierarchy::Brewery/Bottling".
    - Specify the root node dynamically using a tag or a script.

    If a root node is configured, the root node and all objects below the root node are available in the plant overview.
12. Specifies whether the toolbar is shown.
13. Specifies whether the menu bar is shown.

**Note**

As companion controls, you can only select controls already configured in the screen.

##### Result

In runtime you see the screen with the "Plant overview" control and the companion controls. When you navigate to the respective plant object in the "Plant overview" control, the content of this plant object is displayed in the companion controls.

If you have configured the screen window as companion control, navigate in runtime in the "Plant overview" control through the plant and display the screens you have configured for the respective plant object.

If you have configured the alarm control as companion control, navigate in runtime in the "Plant overview" control through the plant and have the alarms for the plant objects displayed in the alarm view.

#### Configuring an alarm control for plant objects (RT Unified)

##### Overview

Configure an alarm control, as in the device-specific configuration in a HMI device screen. In order that the alarm control can display the alarms of the plant objects, assign the plant hierarchy to your HMI device.

To directly jump to the alarms of the plant objects in runtime, configure the alarm control is companion control to the "Plant overview" control.

To filter by plant object alarms in the alarm control, configure a filter with the criterion "Area" with one of the following two conditions:

- "Equal" - only shows the alarms of the selected plant object in runtime.
- "Begins with" - shows the alarms of the underlying objects of the selected plant object in runtime.

##### Configuring a filter for plant objects

To filter by plant object alarms in the alarm control, configure a filter as follows:

1. In the Inspector window under "Properties > Filter", click in the "Static value" column.

   The "Alarm filter configuration" dialog opens.
2. Select the "Area" criteria.
3. Select the condition "Equal"
4. Click on the selection list in the "Operand" column.
5. Select the plant object whose alarms you want to display in runtime.

> **Note**
>
> You can also create filter criteria directly in runtime and use them as filters.

##### Result

Alarms for the selected plant object are displayed in runtime.

---

**See also**

[Configuring screens for plant objects (RT Unified)](#configuring-screens-for-plant-objects-rt-unified)
  
[Configuring the alarm control (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-alarm-control-rt-unified-1)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)

#### Configuring trend control for plant objects (RT Unified)

##### Overview

A trend control, as in the device specific configuration in a HMI device screen. Assign the plant view to your HMI device in order that the trend control can graphically represent the values of the data members of the individual plant objects in runtime.

The trend control allows you to display current and logged values for a specific time window, for example.

As with device-specific configuration, when you configure the trend control for the display of the data values you define the sources from which the values are obtained on the HMI device in runtime. The following sources are available:

- Current process values from data members of the plant object types
- Archived values from logging tags

![Overview](images/131150977291_DV_resource.Stream@PNG-en-US.png)

The path of the plant object is shown in the trend control when displayed in runtime.

---

**See also**

[Configuring the logging of plant object types (RT Unified)](#configuring-the-logging-of-plant-object-types-rt-unified)
  
[Configuring a trend control (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-a-trend-control-rt-unified)
  
[Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)

### Configuring alarms (RT Unified)

This section contains information on the following topics:

- [Basic information on configuring alarms (RT Unified)](#basic-information-on-configuring-alarms-rt-unified)
- [Configure discrete alarms for plant objects (RT Unified)](#configure-discrete-alarms-for-plant-objects-rt-unified)
- [Configuring analog alarms for plant objects (RT Unified)](#configuring-analog-alarms-for-plant-objects-rt-unified)

#### Basic information on configuring alarms (RT Unified)

##### Overview

In object-oriented configuration, as in device-specific configuration via the alarming, events from the monitoring function in WinCC are displayed in form of alarms. The alarms can be acknowledged by the operator and, if necessary, logged. To do this, configure alarms that are separated into alarm classes.

For plant objects you can configure the following alarms that are used to monitor the plant:

- Discrete alarms: Display status changes
- Analog alarms: Display limit value violations (value changes),

Configure bit or analog alarms for plant object types on the basis of internal or external data members. From these plant object types you create plant objects.

If you have configured an alarm system for plant objects you can display the hierarchy path of the alarm source and the alarm status of a line or a machine in runtime, filter the alarm control by plant objects and navigate to the alarm source.

You can also filter the most frequently occurring alarms by plant object and only permit the alarm of the respective object and all lower-level objects to be displayed.

##### Configuration steps

In general, proceed in the following order when configuring the alarms for the plant objects:

- Configure plant object types
- Configuring bit or analog alarms for plant object types on the basis of data members.
- Creating plant objects from plant object types
- Configuring alarm control in a screen
- Configuring "Plant view" control as companion control for the alarm control.

> **Note**
>
> An alarm is linked to the respective plant object type. If you delete the plant object type the alarm will also be deleted.

##### Configuring an alarm view

The alarm view is configured for a screen. Current or logged alarms are displayed in the alarm view in runtime. More than one alarm can be displayed simultaneously, depending on the configured size. Configure the criteria for alarm filtering.

You can also configure multiple alarm views with different contents and in different screens.

---

**See also**

[Configure discrete alarms for plant objects (RT Unified)](#configure-discrete-alarms-for-plant-objects-rt-unified)
  
[Configuring analog alarms for plant objects (RT Unified)](#configuring-analog-alarms-for-plant-objects-rt-unified)

#### Configure discrete alarms for plant objects (RT Unified)

##### Introduction

If you have configured an alarm system for plant objects you can display the hierarchy path of the alarm source and the alarm status of a line or a machine in runtime, filter the alarm control by plant objects and navigate to the alarm source.

You can also filter the most frequently occurring alarms by plant object and only permit the alarm of the respective object and all lower-level objects to be displayed.

An alarm is linked to the respective plant object type. If you delete the plant object type the alarm will also be deleted.

##### Requirement

- A plant object type with associated external or internal data members (with elementary data types) has been created.
- The plant structure has been assigned to a device.

##### Procedure

1. Select the respective data member of the plant object type on the basis of which you want to configure an alarm.
2. To create a new discrete alarm, double-click on "<Add>" under "Discrete alarms" in the table.

   A new discrete alarm is created.
3. Assign a name for the alarm.
4. To configure the alarm, select "Properties > General" in the Inspector window:

   - Enter the alarm text.
   - Change the name of the alarm as required.
   - Select the alarm class.
   - Configure the priority of the alarm (a value of between "0" and "16").
5. Select "Properties > Trigger" in the Inspector window to select the tag and the bit that triggers the alarm.
6. Select "Trigger mode" to specify whether to trigger the alarm at a rising or falling edge.
7. To configure the alarm text, select "Properties > General > Alarm text".

   - Enter the text for the alarm under "Alarm text".

     ![Procedure](images/131148296203_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/131148296203_DV_resource.Stream@PNG-en-US.png)

**Note**

The name of a discrete alarm can contain up to 128 characters.

**Note**

The alarm text must be unique in the context of the plant object type. Hierarchical information is not permitted in the alarm text.

**Note**

You can use the priority to sort or filter the alarms in the alarm control. With sorting by priority, you can ensure that the most important alarm (high priority) is shown in the display area in a single-line alarm control.

If you filter the alarm control by priority "16", only the alarms with priority "16" will appear.

**Note**

Only the data member of the plant object type is permitted as trigger tag.

---

**See also**

[Configuring analog alarms for plant objects (RT Unified)](#configuring-analog-alarms-for-plant-objects-rt-unified)
  
[Basic information on configuring alarms (RT Unified)](#basic-information-on-configuring-alarms-rt-unified)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)

#### Configuring analog alarms for plant objects (RT Unified)

##### Introduction

If you have configured an alarm system for plant objects you can display the hierarchy path of the alarm source and the alarm status of a line or a machine in runtime, filter the alarm control by plant objects and navigate to the alarm source.

You can also filter the most frequently occurring alarms by plant object and only permit the alarm of the respective object and all lower-level objects to be displayed.

An alarm is linked to the respective plant object type. If you delete the plant object type the alarm will also be deleted.

##### Requirement

- A plant object type with associated external or internal data members (with elementary data types) has been created.
- The plant structure has been assigned to a device.

##### Procedure

1. Select the respective data member of the plant object type on the basis of which you want to configure an alarm.
2. Enter the alarm text under "Properties > General".
3. To create a new analog alarm, double-click in the table on "<Add>" under "Analog alarms" in the table.

   A new alarm is displayed.
4. To configure the alarm, select "Properties > General" in the Inspector window:

   - Enter the alarm text.
   - Change the name of the alarm as required.
   - Select the alarm class.
   - Configure the priority of the alarm (a value of between "0" and "16").

     ![Procedure](images/131147291147_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/131147291147_DV_resource.Stream@PNG-en-US.png)
5. In the Inspector window, select the tag that triggers the alarm, e.g. a data member, under "Properties > Trigger".
6. In the Inspector window under "Properties > Trigger", enter a limit in the "Value" field in the "Limits" area.
7. Select the trigger mode in the "Mode" field:

   - "Lower": The alarm is triggered if the limit is undershot.
   - "Upper": The alarm is triggered if the limit is exceeded.
   - "Equal": The alarm is triggered when the limit is reached.
   - "Not equal": The alarm is triggered if the limit is not reached.
   - "Lower or equal": The alarm is triggered if the limit is undershot or reached.
   - "Greater or equal": The alarm is triggered if the limit is exceeded or reached.
8. You can create additional limits for the alarm, if necessary. Note the following:

   - A tag is monitored using only one alarm type. You should therefore create either analog alarms **or** discrete alarms for a tag.
   - If the object included in the selection does not yet exist, create it in the object list and change its properties later.
9. Select the analog alarm to which you want to assign the limits.

**Note**

The alarm text must be unique in the context of the plant object type. Hierarchical information is not permitted in the alarm text.

**Note**

You can use the priority to sort or filter the alarms in the alarm control. With sorting by priority, you can ensure that the most important alarm (high priority) is shown in the display area in a single-line alarm control.

If you filter the alarm control by priority "16", only the alarms with priority "16" will appear.

**Note**

Only the data member of the plant object type is permitted as trigger tag.

---

**See also**

[Configure discrete alarms for plant objects (RT Unified)](#configure-discrete-alarms-for-plant-objects-rt-unified)
  
[Basic information on configuring alarms (RT Unified)](#basic-information-on-configuring-alarms-rt-unified)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)
  
[Example: Configuring analog alarms for temperature monitoring (RT Unified)](#example-configuring-analog-alarms-for-temperature-monitoring-rt-unified)

### Configuring the logging of plant object types (RT Unified)

#### Introduction

Save the values of the data members of the plant object types in logs for later evaluation. Alarm logging can be used to analyze error states, to optimize maintenance cycles, and to document the process.

Create a logging tag for each data member of the plant object type. These logging tags are saved in the data log of the assigned device.

You can analyze the logged tag values directly in your project, such as in a trend view, or in another user program, such as Excel.

The logging tags are created for the plant object types. This means that the plant objects are automatically supplied with the logging tags of the plant object types.

#### Requirement

- The plant hierarchy has been created and assigned to a device.
- A plant object type with associated external or internal data members (with elementary data types) has been created.

#### Procedure

1. Under "Interface", jump to the "Logging tags" tab in the middle part of the work area.
2. Under "Interface", select a data member of a plant object type that you want to log.
3. Click "Add" under "Logging tags".

   A logging tag is created.

   The logging tag is linked to the tag. The data type of the logging tag corresponds to the data type of the connected tag.
4. Specify the logging mode.
5. When the "Cyclic" logging mode is set, define the logging mode and the factor under "Properties > Properties > Cycle".
6. Define the tag trigger depending on the logging mode.
7. Define the limit values.
8. Define the smoothing.
9. If you have selected the "Cyclic" logging mode, define the compression.

**Note**

A logging tag is automatically assigned to a data log. This assignment cannot be changed.

The assignment is only possible if the plant hierarchy is assigned to a HMI device.

**Note**

Depending on the configuration, the database can grow very quickly. This can occur, for example, when you select a short cycle without smoothing and without compression.

**Note**

Process values that are outside the set limit range will not be logged.

Logging tags and logging is available under "Visualizing processes with Runtime Unified".

---

**See also**

[Configuring trend control for plant objects (RT Unified)](#configuring-trend-control-for-plant-objects-rt-unified)

### Good Manufacturing Practice (RT Unified)

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors such as the pharmaceutical industry, the food and beverage industry, and the related mechanical engineering industry.

Therefore, sector-specific and cross-industry standards have been developed for the electronic documentation of production data.

The most important set of regulations is the FDA guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration. In addition, different EU regulations apply, such as EU 178/2002, depending on the industry.

Requirements for production systems in these industries have been developed on the basis of 21 CFR Part 11 and the corresponding layout to comply with GMP (Good Manufacturing Practice). They are also required for other industries.

The following main requirements are derived from these directives and regulations:

- Creation of an Audit Trail or operating trace in runtime

  Based on this document, it is possible to trace the user who carried out the operator action on the machine at what time.
- Important process steps must also be assigned to a clear responsibility, for example, via an electronic signature.

#### GMP (Good Manufacturing Practice)

If necessary, activate the GMP-compliant configuration in the Runtime settings.

GMP is also displayed in the properties of a tag of a PLC user data type used in an HMI device even if it is not enabled in the specific device but the tag is used in an additional device that uses GMP. The menu command "GMP" is grayed out in this case and cannot be edited.

### Example (RT Unified)

This section contains information on the following topics:

- [Example: Scenario (RT Unified)](#example-scenario-rt-unified)
- [Example: Implementation concept (RT Unified)](#example-implementation-concept-rt-unified)
- [Example: Determine plant object type (RT Unified)](#example-determine-plant-object-type-rt-unified)
- [Example: Creating a plant view (RT Unified)](#example-creating-a-plant-view-rt-unified)
- [Example: Creating plant objects and plant object types (RT Unified)](#example-creating-plant-objects-and-plant-object-types-rt-unified)
- [Example: Configuring screens for brewery production lines (RT Unified)](#example-configuring-screens-for-brewery-production-lines-rt-unified)
- [Example: Configuring plant overview and companion controls (RT Unified)](#example-configuring-plant-overview-and-companion-controls-rt-unified)
- [Example: Configuring analog alarms for temperature monitoring (RT Unified)](#example-configuring-analog-alarms-for-temperature-monitoring-rt-unified)
- [Example: Configuring the alarm control for fill level monitoring (RT Unified)](#example-configuring-the-alarm-control-for-fill-level-monitoring-rt-unified)
- [Example: Configuring a trend view for temperature monitoring (RT Unified)](#example-configuring-a-trend-view-for-temperature-monitoring-rt-unified)
- [Example: Configuring the logging of production values (RT Unified)](#example-configuring-the-logging-of-production-values-rt-unified)

#### Example: Scenario (RT Unified)

The production lines "Bottling" and "Packaging" exist alongside other lines in a brewery and are connected to one another in the production chain. The production lines consist of multiple units.

You configure plant objects in the plant view from the plant object types based on the data blocks.

Screens must be configured for all plant objects relevant for the monitoring. In addition, a screen navigation should be set up so that the user can navigate from one plant object screen to another in runtime using the "Plant overview" control. The production value should also be monitored, for example the temperature in the filling tank or the weight of the product after the filling. Make sure to notify the operator in case of deviations.

The relevant production values must be logged for quality assurance purposes and for Food Authority audits.

The "Bottling" production line consists of the following units:

- Conveyor belt 1 ("Conveyor_1")
- Robot 1 ("Robot_1"): Places the bottles on the conveyor.
- Filling tank ("Filling Tank"): Fills the bottles, the temperature in the filling tank is monitored.
- Robot 2 ("Robot_2"): Closes the bottles.
- Robot 3 ("Robot_3"): Performs quality checks (weight and light barrier)

![Figure](images/111862843787_DV_resource.Stream@PNG-de-DE.png)

The bottles are sorted from the conveyor belt into beverage crates on the "Packaging" production line.

The "Packaging" production line consists of the following units:

- Conveyor belt 2 ("Conveyor_2"): Makes the filled bottles available.
- Conveyor belt 3 ("Conveyor_3"): Conveys filled crates.
- Robot 4 ("Robot_4"): Places the crates on the conveyor belt.
- Robot 5 ("Robot_5"): Places the bottles in the crates.
- Robot 6 ("Robot_6"): Places the crates on the pallet.
- Robot 7 ("Robot_7"): Performs quality checks (weight and light barrier)

![Figure](images/111862852363_DV_resource.Stream@PNG-de-DE.png)

#### Example: Implementation concept (RT Unified)

##### Creating a plant view

They map the plants, units and production lines of the brewery in the plant view. To do this, you first create the plant object types that you can reuse for plant objects. Based on the plant object types, you then create the "Brewery" plant view from the plant objects. The two production lines "Bottling" and "Packaging" contain the units according to the following concept:

- Bottling

  - Robot_1
  - Robot_2
  - Robot_3
  - Conveyor_1
  - Filling Tank_1
- Packaging

  - Robot_4
  - Robot_5
  - Robot_6
  - Robot_7
  - Conveyor_2
  - Conveyor_3

##### Visualization

You create faceplate types for the "Conveyor", "Robot" and "Filling Tank" plant object types.

The faceplate types of the plant object types are instantiated in the screens of the plant objects.

According to the structure of the production line, the "Robot" faceplate type is reused three times in the "Bottling" production line and four times in the "Packaging" production line.

You also configure an overview screen called "Overview" with the "Plant overview" control. The plant overview gives you direct access to the unit data in runtime.

##### Temperature monitoring

You want to monitor the temperature in the filling container and to notify the operator if changes occur.

To monitor the temperature, configure a trend control and an alarm control for the filling tank as companion controls for the plant overview.

Because a specific temperature must not be exceeded during the bottling of beverages, configure analog alarms for the filling tank that can be output via the alarm view.

The trend view provides you with an overview of the temperature trend of the filling tank.

##### Logging

The production values are logged for the Food Authority inspections. It must be verified that the temperature was complied with and that quality checks were regularly performed. To this end, configure logging tags for the relevant plant objects.

#### Example: Determine plant object type (RT Unified)

##### Scenario

For a new brewery location, two employees of an engineering office configure the process visualization and plant-specific parameters. The employees develop a configuration concept for this.

The following examples shows how process visualization and object-oriented configured mesh with each other.

##### Determining plant object types

How you determine plant object types by analyzing the plant structure depends on the context:

- In the WinCC Runtime Unified context, you view the plant "from the bottom" in the process view. Functional units are in the background compared to plant objects of the field and process levels. The functional units are still necessary for a complete mapping of the plant.
- In the context of plant-specific KPIs, look at the plant "from the top" in the plant view. Plant objects of the field and process levels may no longer be relevant.

The following figure is a schematic representation of the analysis sequence of the plant structure for defining the plant object types:

![Determining plant object types](images/79747342091_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Analyze the plant structure: The brewery consists of the three plant units, "Delivery/Storage", "Processing" and "Bottling". Various processes run in the plant sections. |  |
| ② | Determining relevant plant objects for monitoring process and productivity: These plant objects are the basis for mapping the plant hierarchy. |  |
| ③ | Defining plant object types: Plant objects used multiple times are mapped using a common plant object type. The data structure and context information is configured for each plant object type. |  |
|  | ![Determining plant object types](images/80849377419_DV_resource.Stream@PNG-de-DE.png) | Brewery  - Plant-specific parameters: Cumulative characteristics of productivity |
|  | ![Determining plant object types](images/80849381387_DV_resource.Stream@PNG-de-DE.png) | Unit for delivery and storage of ingredients  - Plant-specific parameters: Characteristics for duration of delivery |
|  | ![Determining plant object types](images/80852610955_DV_resource.Stream@PNG-de-DE.png) | Tank for storage of ingredients   - Process visualization: Monitoring temperature and fill level |
|  | ![Determining plant object types](images/80852614923_DV_resource.Stream@PNG-de-DE.png) | Unit for processing  - Plant-specific parameters: Characteristics of productivity |
|  | ![Determining plant object types](images/80852618891_DV_resource.Stream@PNG-de-DE.png) | "Mashing"  - "Batches taken out of mash" Process visualization: Monitoring temperature and pressure - "Pump back batches taken out of mash", check: "Iodine test": Process visualization: Monitoring temperature and pressure |
|  | ![Determining plant object types](images/80852622859_DV_resource.Stream@PNG-de-DE.png) | "Purifying" Process visualization: Monitoring temperature and pressure |
|  | ![Determining plant object types](images/80852626827_DV_resource.Stream@PNG-de-DE.png) | "Wort boiling" Process visualization: Monitoring temperature and pressure   - Whirlpooling - Addition of yeast and fermenting - Storage |
|  | ![Determining plant object types](images/80852630795_DV_resource.Stream@PNG-de-DE.png) | Unit for bottling and packaging   - Plant-specific parameters: Characteristics for period of change in production, unplanned downtime and produced quantities |
|  | ![Determining plant object types](images/80852634763_DV_resource.Stream@PNG-de-DE.png) | Bottling process  - Process visualization: Monitoring temperature / control of filling |
|  | ![Determining plant object types](images/80852638731_DV_resource.Stream@PNG-de-DE.png) | Process for packaging the beer bottles on pallets  - Process visualization: Monitoring packaging |

> **Note**
>
> The data structure of a plant object type is often reflected in the function blocks of the user program. In such a case you can create plant object types automatically. Consultation with the programmer is recommended especially for plant object types with strong links to the PLC.

---

**See also**

[Creating plant object types (RT Unified)](#creating-plant-object-types-rt-unified)

#### Example: Creating a plant view (RT Unified)

##### Task

You map the brewery plant with its units and production lines with the plant view and make the unit data available for the entire project.

You create the "Brewery" plant view and assign it to the HMI device.

##### Requirement

- A project has been created.
- An HMI device has been created.

##### Introduction

1. Under "Project tree > Plant objects", click "Add new plant view".

   An empty plant view is created.
2. According to our example, call the plant view "Brewery".
3. Assign the plant view to the HMI device.

##### Result

You have created the "Brewery" plant view and assigned it to the HMI device:

![Result](images/139260882187_DV_resource.Stream@PNG-en-US.png)

#### Example: Creating plant objects and plant object types (RT Unified)

##### Task

You create plant object types from which you will create plant objects in the plant view in the next step. The plant objects represent the units and production lines of the brewery. These are the following elements in our example:

- Filling tank (unit)
- Conveyor (unit)
- Robot (unit)
- Bottling (production line)
- Packaging (production line)

Next, you define the "Communication driver" property of the interfaces.

##### Requirement

- The project is open.
- A SIMATIC S7-1500 PLC has been created.
- At least one program block is configured in the PLC.
- The "Brewery" plant view is created, assigned to an HMI device and open.

##### Procedure

1. To display the "Plant object types" task card, click the "Show plant object types" button under "Project tree > Plant objects".
2. Create a plant object type for each unit and assign the following names:

   - Conveyor
   - Robot
   - Filling Tank
   - Bottling
   - Packaging
3. Specify "SIMATIC S7 1200/1500" as communication driver for each plant object type.
4. As PLC tag, specify the function block that contains tags which match the unit.
5. Now create the following plant objects from the plant object types by dragging the respective plant object type to the plant view and adapting the name:

   - Packaging
   - Bottling
6. In the "Bottling" plant object, create the following lower-level plant objects by dragging the respective plant object type to the "Bottling" plant object:

   - Robot_1
   - Robot_2
   - Robot_3
   - Conveyor_1
   - Tank_1
7. In the "Packaging" plant object, create the following lower-level plant objects by dragging the respective plant object type to the "Packaging" plant object:

   - Robot_4
   - Robot_5
   - Robot_6
   - Robot_7
   - Conveyor_2
   - Conveyor_3
8. Under "Connection", assign each plant object the HMI connection and an instance data block as PLC tag.

##### Result

You have created plant object types for the units and production lines of the brewery. From the plant object types, you have created plant objects in the plant view.

The plant view should have the following structure:

![Result](images/139067870987_DV_resource.Stream@PNG-en-US.png)

#### Example: Configuring screens for brewery production lines (RT Unified)

##### Task

To visualize the plant objects, configure faceplate types for each plant object type.

##### Procedure

1. Under "Project tree > Plant objects", configure the screens for the "Bottling" and "Packaging" production lines.

   - Open the "Bottling" plant object and switch to the "Visualization" tab.
   - You press the "Add new screen" button to create a new screen.
   - Repeat the procedure for the "Packaging" plant object.
2. In the project library, you create a faceplate type for the plant object type "Robot" and release it.

   The faceplate could look as follows according to the example scenario:

   ![Procedure](images/139067879563_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/139067879563_DV_resource.Stream@PNG-de-DE.png)
3. Under "Project tree > Plant objects", open the plant object type "Robot" and drag the created faceplate type to the "Save faceplates here" button in the "Visualization" tab.
4. Create faceplate instances for all the robots you need for the two production lines:

   - Open the "Bottling" screen.
   - Then drag all lower-level plant objects that are based on the "Robot" plant object type one after the other to the screen.
   - Repeat the procedure for the "Packaging" screen.
5. In the project library, you create a faceplate type for the plant object type "Conveyor" and release it.

   The faceplate could look as follows according to the example scenario:

   ![Procedure](images/139070806539_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/139070806539_DV_resource.Stream@PNG-de-DE.png)
6. Create faceplate instances for all the conveyors you need for the two production lines:

   - Open the "Bottling" screen.
   - Then drag all lower-level plant objects that are based on the "Conveyor" plant object type one after the other to the screen.
   - Repeat the procedure for the "Packaging" overview screen.
7. In the project library, you create a faceplate for the plant object type "Filling tank" and release it.

   The faceplate could look as follows according to the example scenario:

   ![Procedure](images/139071864715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/139071864715_DV_resource.Stream@PNG-de-DE.png)
8. Under "Project tree > Plant objects", open the plant object type "Filling tank" and drag the created faceplate type to the "Drop faceplates here" button in the "Visualization" tab.
9. From the "Filling tank" plant object, create a faceplate instance for the filling container:

   - Open the "Bottling" overview screen.
   - Then drag the plant object that is based on the "Tank" type to the screen.

##### Result

You have successfully configured screens and faceplates for the plant objects of the brewery and can display the plant objects in the runtime.

---

**See also**

[Configuring screens for plant objects (RT Unified)](#configuring-screens-for-plant-objects-rt-unified)
  
[Basic information on configuring screens (RT Unified)](#basic-information-on-configuring-screens-rt-unified)

#### Example: Configuring plant overview and companion controls (RT Unified)

##### Task

To access the unit data directly from the "Overview" screen in runtime, configure a plant overview control in the overview screen.

To directly jump to the alarms of the "Filling Tank" plant object in runtime, create the alarm control as companion control to the "Plant overview" control. The alarm control is configured in the next step.

##### Procedure

1. Change to the project tree.
2. Under "Project tree > Devices", create an "Overview" screen.
3. Configure the "Plant overview" control in the "Overview" screen.
4. Also add the "Alarm control" and "Screen window" controls as companion controls to the "Overview" screen.

##### Result

You have configured an overview screen and added a screen window and an alarm control. Next, configure the alarm control.

#### Example: Configuring analog alarms for temperature monitoring (RT Unified)

##### Task

The temperature of the beer brewing ingredients in the brewery must be strictly maintained. One of your tasks is to configure the temperature monitoring of the filling tank.

The following requirements apply to temperature monitoring of the filling tank:

- The setpoint for the temperature is 5 °C.
- When the temperature rises above 5 °C, the operator of the plant is notified.
- If the temperature reaches 7 °C, the operator is notified immediately. The operator has to confirm the notification.

Temperature deviations of the filling tank should be output on the HMI device.

You plan several escalation levels for the alarms to be output according to the requirements:

- Temperature is at 5 °C.
- Temperature is above 5 °C: An alarm that does not require acknowledgment is output.
- Temperature exceeds the critical temperature of 7 °C: An alarm that requires acknowledgment is output.

The temperature sensor of the filling tank returns analog values. Use these values to specify the triggers. The triggers determine when an alarm is triggered.

##### Requirement

- A trigger tag is configured for temperature monitoring, for example, "temperature".
- The "Filling Tank" plant object type is open.
- The "Analog alarms" editor is open.

##### Procedure for creating an alarm for exiting the setpoint range

1. Create a new alarm and call it "Critical Temperature", for example.
2. Select the alarm class "Notification".

   Alarms of this alarm class do not require acknowledgment.
3. Select the trigger tag.
4. Define the trigger with a limit "5".

   This corresponds to the setpoint of 5 °C. Limits are always without units. The physical unit depends on the plant component which delivers the values.
5. Configure "Not equal" as the mode limit.

   When the value of the trigger tag is not equal to 5, an alarm is output.

##### Procedure for creating an alarm for exceeding the critical temperature

1. Create the "Action required" alarm.
2. Select "Alarm" as the alarm class.

   Alarms of this alarm class are displayed flashing in red on the HMI device and require acknowledgment.
3. Define the trigger with limit "7".

   This corresponds to a critical temperature of 7 °C.
4. Configure "Higher" as the mode limit.

   When the value of the trigger tag is higher than 7, an acknowledgeable alarm is output.

##### Result

You have configured alarms for the temperature monitoring:

![Result](images/139263059851_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring analog alarms for plant objects (RT Unified)](#configuring-analog-alarms-for-plant-objects-rt-unified)

#### Example: Configuring the alarm control for fill level monitoring (RT Unified)

##### Task

The configured alarms for temperature monitoring are to be output in an alarm control in runtime.

To filter by plant object alarms in the alarm control, configure a filter with the criterion "Area" with one of the following two conditions:

- "Equal" - only shows the alarms of the selected plant object in runtime.
- "Begins with" - shows the alarms of the underlying objects of the selected plant object in runtime.

##### Requirement

- The "Overview" screen is created and open for editing.
- Configure a "Plant overview" control in the "Overview" screen.
- The "Alarm control" control is created as companion control of the plant overview.

##### Configuring a filter for the "Filling Tank" plant object

To filter by alarms of the "Filling Tank" plant object in the alarm control, configure a filter as follows:

1. In the Inspector window under "Properties > Filter", click in the "Static value" column.

   The "Alarm filter configuration" dialog box opens.
2. Select the "Area" criterion.
3. Select the condition "Equal".
4. Click on the selection list in the "Operand" column.
5. Select the "Filling Tank" plant object whose alarms are to be displayed in runtime.

![Configuring a filter for the "Filling Tank" plant object](images/111904420491_DV_resource.Stream@PNG-en-US.png)

##### Result

You have configured an alarm control for alarms of the "Filling Tank" plant object. The alarms of the plant object can be displayed in runtime.

#### Example: Configuring a trend view for temperature monitoring (RT Unified)

##### Introduction

To visualize the tag values of the temperature monitoring in runtime, you have added a trend view in the "Overview" screen. You can display the current temperature of the "Filling Tank" plant object with the trend view.

##### Requirement

- The HMI tag for temperature measurement has been configured, for example "temperature".
- The "Overview" screen is open for editing.

##### Configuring the trend area and axes

1. Create a trend view in the "Overview" screen by dragging the control from the "Tools" task card to the screen.
2. Go to "Properties" and set the required height, width and position of the trend view.
3. Open the "Trend areas" group under "Properties".

   The index numbers of the trend area are displayed.
4. Expand the index number of the trend area.

   The properties of the trend area are displayed.
5. Define the colors for displaying the trend area and the reference lines.
6. Configure the time axis and value axis settings under "Bottom time axis" and "Left value axis".

##### Configuring trends

1. Go to "Properties > Properties > General > Trend areas > [0] trend areas > Trends" and click on the selection button in the "Static value" column.

   A dialog opens.
2. Click "Add" in the "Index" column.

   This adds another trend. Close the dialog.
3. Expand the index number of the trend [0]. The trend settings are displayed.
4. Specify the name of the trend under "Display name", for example "Temperature".
5. Under "Data source Y > Source", select the "temperature" tag in the "Static value" column.
6. Configure the line color for the trend, for example, blue.

![Configuring trends](images/139272635787_DV_resource.Stream@PNG-en-US.png)

##### Result

The trend control is now configured. In runtime, you monitor the temperature changes over time based on the trend.

Configure an additional value display if you want to evaluate the data of the trend control in runtime. You can also configure the value display as a "Ruler".

#### Example: Configuring the logging of production values (RT Unified)

##### Task

You want to log the temperature values of the "Filling Tank" plant object to be able to use them later for controls, for example.

To this end, you create a logging tag for the data member you want to log. This logging tag is saved in the data log of the assigned device.

You can analyze the logged tag values directly in your project, such as in a trend view, or in another user program, such as Excel.

Logging tags are created for the plant object types. This means that the plant objects are automatically supplied with the logging tags of the plant object types.

##### Requirement

- The "Brewery" plant view has been created and assigned to a device.
- The "Filling Tank" plant object type is created, and the "temperature" member has been configured.

##### Procedure

1. Open the "Conveyor" plant object type.
2. Under "Interface", jump to the "Logging tags" tab in the middle part of the work area.
3. Under "Interface" select the "Rate" data member, for example, to log it.
4. Click "Add" under "Logging tags".

   ![Procedure](images/139272957323_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/139272957323_DV_resource.Stream@PNG-en-US.png)

   A logging tag is created.

   The logging tag is linked to the tag. The data type of the logging tag corresponds to the data type of the connected tag.
5. Specify the logging mode, for example, "Upon change".
6. Define the tag trigger depending on the logging mode.
7. Define the limit values.
8. Define the smoothing.

Additional information on logging tags and logging is available under "Visualizing processes with Runtime Unified".

##### Result

You have created a logging tag that logs tag values for the defined period and within the parameters you have specified.

## Visualizing plant objects in runtime (RT Unified)

This section contains information on the following topics:

- [Displaying plant objects in runtime (RT Unified)](#displaying-plant-objects-in-runtime-rt-unified)
- [Operating "Plant overview" in runtime (RT Unified)](#operating-plant-overview-in-runtime-rt-unified)
- [Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)
- [Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)

### Displaying plant objects in runtime (RT Unified)

#### Overview

Depending on your configuration, the following possibilities are available to you in runtime:

- Screen navigation via the plant model
- Analysis based on plant objects
- Filter alarm control by plant objects
- Display alarm status of a line and navigation to the alarm source
- Display the most frequently occurring alarms, filtered by plant object or plant object type
- Area-based access protection
- Determine the energy consumption of a line and compare with another line

You can display the configured plant hierarchy in runtime using the "Plant overview" control. If a screen window was configured as companion control for the "Plant overview", you can navigate between the screens of the plant objects and show them alternately in the screen window.

Display process data of the plant objects in a trend control. Switch between the following display modes directly in runtime:

- Device view and plant hierarchy
- Online values and log values

You can view alarms on plant objects in an alarm control.

![Overview](images/113018336395_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Operating "Plant overview" in runtime (RT Unified)](#operating-plant-overview-in-runtime-rt-unified)
  
[Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)

### Operating "Plant overview" in runtime (RT Unified)

#### Introduction

Display the configured plant view in runtime using the "Plant overview" controls.

You use it to navigate to the plant objects within the plant structure and get an overview of your plant at one glance.

If you have configured screens or alarms for the lower-level plant objects and have linked them to the "Plant overview" control, display these screens and alarms in runtime.

If you have configured events for the "Plant overview" control and linked these to scripts, the scripts are called when the events occur.

An event can, for example, be linked to the operation of the buttons in the control.

#### Requirement

- The plant view has been created and assigned to a device.
- The "Plant overview" control and the corresponding companion controls are configured in the screen of the assigned device.
- Runtime is active.

#### Procedure

The plant view is displayed in the "Plant overview" control.

1. To display all lower-level plant objects, click [[ICON]] "Expand all".
2. To display the configured screen or screen window for a selected plant object, click on the respective plant object in the "Plant overview" control.
3. In case of an alarm, the plant path of the alarm source is displayed in the "Range" column of the connected alarm view.

   The alarm icon only appears an alarm has actually occurred at the respective plant object. The alarm icon disappears again when the alarm is no longer present.

   ![Procedure](images/140106257931_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/140106257931_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Configuring screens for plant objects (RT Unified)](#configuring-screens-for-plant-objects-rt-unified)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)
  
[Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)
  
[Displaying plant objects in runtime (RT Unified)](#displaying-plant-objects-in-runtime-rt-unified)

### Display process data of the plant objects in a trend control (RT Unified)

#### Introduction

The process data or the logging data of the plant objects are displayed graphically in a trend control in runtime.

You switch between the following display modes in runtime:

- Device view and plant hierarchy
- Online values and log values

#### Requirement

- The plant hierarchy has been created and assigned to a device.
- A trend control is configured in the screen by the assigned device.
- The "Select data connection" button is displayed in the control.
- The "Select context" button is displayed in the control.
- Runtime is active.

#### Display process data of the plant objects

1. Click "Select data connection" in the trend control.

   A "Selection of logs/tags" dialog opens.
2. To open the list of available tags, click "Tag".

   The "Browser view" dialog opens.

   ![Display process data of the plant objects](images/118555404811_DV_resource.Stream@PNG-en-US.png)

   ![Display process data of the plant objects](images/118555404811_DV_resource.Stream@PNG-en-US.png)
3. To jump to the plant view dialog, click on the "CPM" icon in the toolbar.

   The plant objects and the available data members for the plant objects are displayed.
4. Select the respective plant object whose process data you want to display in the trend control.
5. Select the data members that you want to display as trend in the trend control.
6. Confirm with "OK".

   The process values for the selected plant object are displayed in the trend control.

   ![Display process data of the plant objects](images/110988270475_DV_resource.Stream@PNG-en-US.png)

   ![Display process data of the plant objects](images/110988270475_DV_resource.Stream@PNG-en-US.png)

**Note**

If you have assigned a descriptive display name for the trend when you configured the trend control, only the display name is shown in runtime. All plant objects are visible at a glance in the selection list.

#### Display context data of the plant objects in a trend control

For analysis purposes, display the value range of the resulting data using the context data.

The evaluation is relevant, for example, in connection with WinCC Unified Performance Insight to analyze the effectiveness or the fault rate of the plant.

1. In the trend control, click "Select context".

   The "Trend context" dialog opens.
2. In the "Plant objects" selection list, select the respective plant object whose data you want to display in the trend control.
3. In the "Context" selection list, select the data assigned to the plant object.

   The list of the data appears under "Logged context values".
4. Select the value that you want to display.
5. Confirm with "OK".

   ![Display context data of the plant objects in a trend control](images/110988279051_DV_resource.Stream@PNG-en-US.png)

   ![Display context data of the plant objects in a trend control](images/110988279051_DV_resource.Stream@PNG-en-US.png)

   The trend control displays the trends for the selected data.

---

**See also**

[Operating "Plant overview" in runtime (RT Unified)](#operating-plant-overview-in-runtime-rt-unified)
  
[Displaying alarms for plant objects in runtime (RT Unified)](#displaying-alarms-for-plant-objects-in-runtime-rt-unified)
  
[Configuring trend control for plant objects (RT Unified)](#configuring-trend-control-for-plant-objects-rt-unified)
  
[Displaying plant objects in runtime (RT Unified)](#displaying-plant-objects-in-runtime-rt-unified)
  
[Contexts (RT Unified)](#contexts-rt-unified)

### Displaying alarms for plant objects in runtime (RT Unified)

#### Introduction

The "Alarm control" object displays alarms that occur during the production process in a plant.

Depending on your configuration, the following possibilities are available to you in runtime:

- Display hierarchy path of the alarm source
- Filter alarm control by plant objects
- Display alarm status of a line
- Navigate to the alarm source
- Display the most frequently occurring alarms, filtered by plant object or plant object type

#### Requirement

- The plant hierarchy has been created and assigned to a device.
- An alarm control with the filter "Range" is configured in the screen by the assigned device.
- Runtime is active.

- The alarm view has been configured.
- Runtime is active.

#### Filter alarms by plant objects

1. If you want to filter alarms by plant objects, click "Selection display" in runtime.

   The "Selection" dialog opens.
2. Under "Criterion", select the criterion "Range".

   All plant objects of the plant hierarchy are displayed.
3. Select the respective plant object to which you want to display the alarms.

   ![Filter alarms by plant objects](images/110346800651_DV_resource.Stream@PNG-en-US.png)

   ![Filter alarms by plant objects](images/110346800651_DV_resource.Stream@PNG-en-US.png)

   Only alarms for the selected plant object are displayed in the alarm control.

#### Display alarm context of the plant objects

For analysis purposes, display the value range of the resulting data using the context data.

The evaluation is relevant, for example, in connection with the WinCC Unified Performance Insight to analyze the effectiveness or the fault rate of the plant.

1. In the alarm control, click "Select context".

   The "Alarm context" dialog box opens.
2. In the "Plant objects" selection list, select the respective plant object whose data you want to display in the alarm control.
3. In the "Context" selection list, select the data assigned to the plant object.

   The list of the logging data appears under "Logged context values".
4. Select the value that you want to display.

   ![Display alarm context of the plant objects](images/110988279051_DV_resource.Stream@PNG-en-US.png)

   ![Display alarm context of the plant objects](images/110988279051_DV_resource.Stream@PNG-en-US.png)
5. Confirm with "OK".

   The alarm control displays the alarms that match your selection.

**Note**

Make sure that the filter settings match the setting of the alarm context.

If no alarms appear in the alarm control, check your settings by clicking "Selection display".

---

**See also**

[Operating "Plant overview" in runtime (RT Unified)](#operating-plant-overview-in-runtime-rt-unified)
  
[Display process data of the plant objects in a trend control (RT Unified)](#display-process-data-of-the-plant-objects-in-a-trend-control-rt-unified)
  
[Configuring an alarm control for plant objects (RT Unified)](#configuring-an-alarm-control-for-plant-objects-rt-unified)
  
[Configuring analog alarms for plant objects (RT Unified)](#configuring-analog-alarms-for-plant-objects-rt-unified)
  
[Configure discrete alarms for plant objects (RT Unified)](#configure-discrete-alarms-for-plant-objects-rt-unified)
  
[Displaying plant objects in runtime (RT Unified)](#displaying-plant-objects-in-runtime-rt-unified)

## Options (RT Unified)

This section contains information on the following topics:

- [Plant Intelligence Options (RT Unified)](#plant-intelligence-options-rt-unified)

### Plant Intelligence Options (RT Unified)

#### Overview

The Plant Intelligence options offer optional enhancements to the WinCC Unified Basic System. These can be combined freely in line with your requirements.

The options allow you to plan production processes and analyze and optimize the overall effectiveness of your plant. In addition, you can design flexible production processes and coordinate complex and interlinked production processes.

#### Plant Intelligence options

![Plant Intelligence options](images/157327528587_DV_resource.Stream@PNG-de-DE.png)

- WinCC Unified Performance Insight

  Define, calculate and analyze plant-specific key performance indicators (KPIs) for individual aggregates, machines or entire production lines in machine-oriented or line-oriented manufacturing plants.
- WinCC Unified Calendar

  Plan, configure and manage events and actions together in a shared calendar in WinCC and combine these with WinCC tags or scripts.
- WinCC Unified Sequence

  Control step-based and sequence-based processes, define the production steps of the production units and adapt the production processes flexibly in runtime.
- WinCC Unified Line Coordination

  Coordinate and supervise processes in the production line in your plant. Control and manage recipes, processes and jobs for the production of various end products.

#### Note

The Plant Intelligence options are successively released as add-on packages. To use the Plant Intelligence options, you require the relevant software packages and licenses.

You can find information on the licenses in the TIA Portal installation instructions in the section "Licensing of Plant Intelligence options".

#### Requirements

Please note the following requirements for using the options:

- SIMATIC WinCC Runtime Unified is installed.
- STEP7 Professional is installed.
- Plant Intelligence option, including license, is installed.
- The plant hierarchy is configured.
- License for the respective option is available.
- The configuration engineer has WinCC experience.

---

**See also**

[Configuring a calendar (RT Unified)](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#configuring-a-calendar-rt-unified)
  
[Configuring KPIs (RT Unified)](Performance%20Insight%20-%20Optimizing%20processes%20with%20KPIs%20%28RT%20Unified%29.md#configuring-kpis-rt-unified)
  
[Structuring the plant (RT Unified)](Line%20Coordination%20and%20Sequence%20-%20Flexible%20handling%20of%20production%20processes%20%28RT%20Unified%29.md#structuring-the-plant-rt-unified)
