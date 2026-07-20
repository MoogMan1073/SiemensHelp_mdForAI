---
title: "Configuring parameter sets (RT Unified)"
package: ParametersetsWCCUenUS
topics: 21
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring parameter sets (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring parameter sets (RT Unified)](#configuring-parameter-sets-rt-unified-1)
- [Using parameter sets in runtime (RT Unified)](#using-parameter-sets-in-runtime-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Basics of parameter control (RT Unified)](#basics-of-parameter-control-rt-unified)
- [Limitations (RT Unified)](#limitations-rt-unified)
- ["Parameter set types" editor (RT Unified)](#parameter-set-types-editor-rt-unified)
- [Parameter set control (RT Unified)](#parameter-set-control-rt-unified)

### Basics of parameter control (RT Unified)

#### Introduction

The parameter control is a comprehensive function for the control of parameter sets for configuration engineers, operators and recipe creators. The parameter control brings you the following benefits:

- You can apply the structure of a user data type for one or more parameter set types.
- You can change the structure of one or more parameter set types automatically via a new user data type version.
- You can exchange a large number of parameters manually or automatically between HMI device and PLC to set up a machine for a production.
- You can create parameter sets simply and uniformly for products to be manufactured in the works during engineering or during ongoing operation.
- By structuring the associated parameters/setpoints, you can easily transfer parameters.

#### Elements of the parameter control

- Parameter set type

  A parameter set type with parameter set type items determines the structure that is used for parameter sets on a machine. You create a parameter set type with parameter set type items on the basis of a released HMI or PLC user data type that has user data type elements.
- Parameter set type item

  Element of a parameter set type that is based on a user data type element. A parameter set type item has the same name and data type as the corresponding user data type element.
- Parameter record

  Set of parameters with concrete values that can be activated on a machine.
- Parameters

  Element of a parameter set that is based on a parameter set type item. A parameter has the same display name and data type as well as the same unit of measure as the corresponding parameter set type item. A parameter has a concrete value that can be activated on a machine.

#### Tools of the parameter control

- "Parameter set types" editor

  In the "Parameter set types" editor, you create parameter set type items on the basis of an HMI or PLC application data type. In addition, you configure the properties of parameter set types and parameter set type items in the editor.
- Parameter set control

  The parameter set control is a control with which you can display and manage parameter sets in runtime and exchange them with the PLC.

#### Parameter set memory

Part of the parameter control is the parameter set memory. The parameter set memory can be configured depending on the device.

#### Parameter control in the Engineering System

Perform the following tasks in Engineering System for the parameter control:

- You create a parameter set type to specify the structure of parameter sets.
- You change a parameter set type to change the structure of parameter sets.
- You assign a tag of the data type user data type to a parameter set type to transfer parameter sets between HMI device and PLC in runtime.
- You create local scripts in screen objects or tasks to transfer parameter sets in runtime between the HMI device and PLC.
- You assign control tags to a parameter set type to automatically transfer or delete parameter sets between HMI device and PLC in runtime.
- You configure a parameter set control to display parameter sets, manage them and exchange them with the PLC through the Control in runtime.
- In a screen, you configure an individual input mask to display, manage and exchange parameter sets with the PLC without using the control "Parameter set control".

#### Parameter control in runtime

The following options are available in runtime with the parameter control:

- You create, change and delete parameter sets in a parameter set control to manage parameter sets for different productions.
- Alternatively, create, change and delete parameter sets in an individual input mask to manage them for different productions.
- You export parameter sets from the parameter set memory into a "*.tsv" file to edit them in a text editor.

  > **Note**
  >
  > A "*.tsv" file is a text file that uses the tabulator as a list separator.
- You import parameter sets from a "*.tsv" file into the parameter set memory.
- You transfer parameter sets manually or automatically to the control system to set up machines with values for different productions.
- You read parameter sets manually or automatically from the PLC to call up currently used values of production machines for later use.
- You automatically delete parameter sets from the parameter set memory.

---

**See also**

[Configuring parameter sets (RT Unified)](#configuring-parameter-sets-rt-unified-1)
  
[Using parameter sets in runtime (RT Unified)](#using-parameter-sets-in-runtime-rt-unified)
  
[Configuring user data types (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-user-data-types-rt-unified)

### Limitations (RT Unified)

#### Unsupported data types in the parameter data set

Structure data types are not supported in a parameter data set:

- Struct, Array of Struct
- ErrorStruct
- CREF
- NREF

#### Restrictions on the PLC user data type

Observe the following restrictions when creating the PLC user data type:

- The user data type may have a maximum of 1000 elements.
- No user data type item may have the data type Time_Of_Day.
- The ARRAY data type is supported.

  The use of a user data type is not supported in an ARRAY.
- The user data type may have a maximum of 8 levels.

### "Parameter set types" editor (RT Unified)

#### Introduction

In the "Parameter set types" editor, you create a parameter set type with elements on the basis of an HMI or PLC application data type. In addition, you configure the properties of parameter set types and parameter set type items in the editor.

> **Note**
>
> Alternatively create the parameter set type items on the basis of a user data type in the Inspector window. In addition, you configure the properties of parameter set types and parameter set type items also alternatively in the Inspector window.

#### Structure of the "Parameter set types" editor

The "Parameter set types" editor is a tabular editor. The editor always contains only a single parameter set type and, if applicable, its elements. To view hidden columns, activate the column titles using the shortcut menu.

![Structure of the "Parameter set types" editor](images/115040713867_DV_resource.Stream@PNG-en-US.png)

#### Properties of parameter set types

In the "Parameter set types" editor, you can configure the following properties:

| Property | Description |
| --- | --- |
| ID | Number of a parameter set type. The ID uniquely identifies a parameter set type within the HMI device. The ID appears in the parameter set control in runtime. |
| Name | Name of a parameter set type. The name uniquely identifies a parameter set type within the HMI device. |
| Display name | Display name of a parameter set type. The display name appears in the parameter set control in runtime. You can configure display names in multiple languages. The property is optional. If you do not set a display name, the value from the "Name" property appears in the parameter set control in runtime. |
| Data type | Enabled HMI or PLC user data type with which you define the structure of a parameter set type. |
| Tag | External HMI tag of the data type HMI or PLC user data type. In runtime you transfer parameter sets between HMI device and PLC via the HMI tag. |
| Edit tag | Local session HMI tag used to manage the values of a parameter set in a screen.  Edit tags can be read from or written to the PLC.  The HMI tag must not contain any information about the range (Upper 2, Lower 2).  The property is optional. |
| Parameter ID | Control tag with numerical data type. The control tag is used to define an ID of a parameter set which is the target of one of the following control jobs in runtime:  - Control job with job ID "6": Reading a parameter set from the PLC and storing it in the parameter set memory. - Control job with job ID "7": Loading a parameter set from the parameter set memory and writing it to the PLC. - Control job with job ID "8": Deleting a parameter set from the parameter set memory.   The property is optional. |
| Job ID | Control tag with numerical data type. The control tag is used to define a control job which is applied to a parameter set in runtime. In runtime, you can apply the following control jobs to a parameter set:   - Control job with job ID "6": Reading a parameter set from the PLC and storing it in the parameter set memory. - Control job with job ID "7": Loading a parameter set from the parameter set memory and writing it to the PLC. - Control job with job ID "8": Deleting a parameter set from the parameter set memory.   The property is optional. |
| Author | Author of a parameter set type. The property is optional. By default, the property is pre-assigned with the logged-on Windows user. By default, the column is hidden. |
| Version | Version of a parameter set type. The property is optional. By default, the property is pre-assigned with the date and time of creation of the parameter set type. By default, the column is hidden. |
| Storage medium | For Unified PC, the storage medium is internal. The parameter set type is saved in the system default directory.   For Unified Comfort Panel, you choose between the internal storage medium and various external storage media. |
| Memory folder | Internal storage medium: System standard folder in runtime, in which the parameter set memory is located. The folder refers to the folder of the runtime project. The property is write-protected.   External storage medium: Freely selectable memory folder. |

#### Properties of parameter set type items

In the "Parameter set types" editor, you can configure the following properties for parameter set type items:

| Property | Description |
| --- | --- |
| Name | Name of a parameter set type item. The name uniquely identifies a parameter set type item. The name is write-protected and identical to the name of the corresponding user data type element. |
| Display name | Display name of a parameter set type item and a corresponding parameter in a parameter set. The display name appears in the table of the parameter set control in runtime. You can configure display names in multiple languages. The property is pre-assigned with the value from the "Name" property. |
| Data type | Data type of a parameter set type item and a corresponding parameter in a parameter set. The name is write-protected and identical to the data type of the corresponding user data type element. |
| Start value | Start value of a parameter set type item. The start value is used to pre-assign a corresponding parameter in a newly created parameter set in runtime.  If you have not set a start value in a user data type element with numerical data type or bit sequence data type, the corresponding parameter set type item receives "0" as the start value.   When parameter set type items with the data type ARRAY are used, only the start value for the items of the array can be defined.  The property is optional for parameter set type items with string data types. |
| Minimum value | Minimum permissible value of a parameter set type item and a corresponding parameter in a parameter set.  The minimum value of a parameter set type item may not be below the minimum value of the data type of the parameter set type item.   When parameter set type items with the data type ARRAY are used, only the minimum value for the items of the respective lowest level can be defined.  The property is optional and is disabled for parameter set type items with string data types and bit sequence data types. |
| Maximum value | Maximum permissible value of a parameter set type item and a corresponding parameter in a parameter set.  The maximum value of a parameter set type item may not be above the maximum value of the data type of the parameter set type item.   When parameter set type items with the data type ARRAY are used, only the maximum value for the elements of the respective lowest level can be defined.  The property is optional and is disabled for parameter set type items with string data types and bit sequence data types. |
| Value required | If the check box of the property "Value required" is selected in a parameter set type item, a corresponding parameter must have a value in a parameter set. Otherwise, a corresponding parameter must have no value in a parameter set.   The check box of the property is selected by default for parameter set type items with numerical data types. In this case, you cannot clear the check box.   The check box of the property is cleared by default for parameter set type items with string data types. In this case, however, you can select the check box if required.  When parameter set type items with the data type ARRAY are used, only the check box for the items of the respective lowest level can be defined. |
| Unit of measure | Unit of measure of a parameter set type item and a corresponding parameter in a parameter set. The unit of measure appears in the table of the parameter set control in runtime.   When parameter set type items with the data type ARRAY are used, only the unit of measurement for the items of the respective lowest level can be defined.  The property is optional. |

---

**See also**

[Creating a parameter set type with elements via an HMI user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-an-hmi-user-data-type-rt-unified)
  
[Creating a parameter set type with elements via a PLC user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-a-plc-user-data-type-rt-unified)

### Parameter set control (RT Unified)

#### Use

You can use the "Parameter set control" object to display and manage parameter sets in runtime and to exchange them with the controller.

![Use](images/160282434571_DV_resource.Stream@PNG-en-US.png)

#### Layout

You can change the settings for the position, geometry, style, color, and font of the object in the Inspector window. Under "Miscellaneous", adapt the following properties:

- "Editing mode": Defines the activation status of the toolbar buttons.
- "Toolbar": Defines the buttons of the parameter set control.
- "Information bar": Specifies the representation of the information bar.
- "Parameter view": Specifies the display of the parameter table in the object.

#### Using a parameter set type

If you only want to use a particular parameter set type with its parameter sets in runtime, select the desired parameter set type under "Properties > General > Fixed parameter set type".

#### Configuring the time zone

To configure the time zone, follow these steps:

Under "Properties > Miscellaneous > Time zone", set the desired time zone by entering a numerical value.

The numerical value stands for a time zone, for example:

- "-1" stands for UTC-1h (Central European Time, standard time)
- "1" stands for UTC-12h (International Date Line West)
- "2" stands for UTC-11h (Hawaii)

#### Defining the editing mode

To specify the editing mode and to enable or disable the buttons, follow these steps:

Under "Properties > Miscellaneous > Editing mode", configure the activation status of the toolbar buttons "Create", "Save", "Save as", "Rename" and "Delete". These toolbar buttons are used to edit parameter sets.

You can select between the following settings:

- "None": Deactivates all buttons.
- "Update": Activates the "Save" and "Rename" buttons.
- "Create": Activates the "Create" and "Save as" buttons.
- "Delete": Activates the "Delete" button.

#### Configuring reordering of the columns

Configure whether operators can reorder the table columns in runtime using drag-and-drop. More information is available in the section [Configuring reordering of the columns](Configuring%20screens%20%28RT%20Unified%29.md#configuring-reordering-of-the-columns-rt-unified).

#### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

#### Configuring the information bar

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties > Miscellaneous > Information bar".
2. To adjust the height of the "Status text" element, specify the height under "Properties > Miscellaneous > Information bar > Elements > [0] Element".

The "Status Text" element is the only status line element of the parameter set control. Status messages are displayed in this element in runtime.

#### Toolbar

You can define the buttons of the parameter set control in runtime and their operator authorizations in the Inspector window under "Properties > Miscellaneous > Toolbar > Elements". By default, all buttons are displayed in the toolbar. To hide specific buttons, deactivate the "Visibility" property in the settings of the corresponding button.

"Toolbar": Defines the buttons of the parameter set control.

> **Note**
>
> **Visibility of buttons in runtime**
>
> Buttons for which the "Visibility" option is deactivated during the configuration cannot be made visible again in runtime by a script. After loading into a device, the array of available items contains only those buttons that are configured as visible.

The following buttons are available for the parameter set control:

|  | Button | Function |
| --- | --- | --- |
| ![Toolbar](images/110181830795_DV_resource.Stream@PNG-de-DE.png) | Create | Creates a new parameter set. |
| ![Toolbar](images/110183221771_DV_resource.Stream@PNG-de-DE.png) | Save | Saves a parameter set. |
| ![Toolbar](images/110183230347_DV_resource.Stream@PNG-de-DE.png) | Save as | Saves an existing parameter set under a new name and new ID. |
| ![Toolbar](images/110183264523_DV_resource.Stream@PNG-de-DE.png) | Rename | Renames the selected parameter set. |
| ![Toolbar](images/110183337099_DV_resource.Stream@PNG-de-DE.png) | Write to PLC | Writes the values of the selected parameter set to the PLC. |
| ![Toolbar](images/110183345675_DV_resource.Stream@PNG-de-DE.png) | Read from PLC | Writes the values of the selected parameter set from the PLC. |
| ![Toolbar](images/110183443851_DV_resource.Stream@PNG-de-DE.png) | Import | Imports parameter sets from a "*.tsv" file. |
| ![Toolbar](images/110183503627_DV_resource.Stream@PNG-de-DE.png) | Export | Exports parameter sets to a "*.tsv" file. |
| ![Toolbar](images/110183512203_DV_resource.Stream@PNG-de-DE.png) | Cancel | Cancels the process. |
| ![Toolbar](images/154713266059_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected parameter set. |

> **Note**
>
> A "*.tsv" file is a text file that uses the tabulator as a list separator.

---

**See also**

[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)

## Configuring parameter sets (RT Unified)

This section contains information on the following topics:

- [Creating a parameter set type with elements via an HMI user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-an-hmi-user-data-type-rt-unified)
- [Creating a parameter set type with elements via a PLC user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-a-plc-user-data-type-rt-unified)
- [Changing a parameter set type with elements (RT Unified)](#changing-a-parameter-set-type-with-elements-rt-unified)
- [Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-hmi-user-data-type-to-a-parameter-set-type-rt-unified)
- [Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-plc-user-data-type-to-a-parameter-set-type-rt-unified)
- [Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
- [Transferring parameter sets via scripts (RT Unified)](#transferring-parameter-sets-via-scripts-rt-unified)
- [Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
- [Assigning an edit tag to a parameter set item (RT Unified)](#assigning-an-edit-tag-to-a-parameter-set-item-rt-unified)
- [Configuring parameter sets without parameter set control (RT Unified)](#configuring-parameter-sets-without-parameter-set-control-rt-unified)

### Creating a parameter set type with elements via an HMI user data type (RT Unified)

#### Introduction

You have created an HMI user data type with elements. You can assign the user data type to one or more parameter set types and this way apply the elements of the user data type for the parameter set type or types. A parameter set type with elements determines the structure that is used for parameter sets on a machine. Because you do not have to create the elements of the user data type again separately for the parameter set type(s), efficiency and reusability are a given.

> **Note**
>
> Observe the following restrictions when creating the HMI user data type:
>
> - The user data type may have a maximum of 1000 elements.
> - No user data type item may have the data type Textref, Time_Of_Day, or Raw.

> **Note**
>
> You can also create a parameter set type with elements via a PLC user data type that is created in a SIMATIC S7-1200/1500 control system.

#### Requirement

- An HMI device has been created.
- An HMI user data type with a user data type element is created.
- The communication driver SIMATIC S7-300/400 or SIMATIC S7-1200/1500 is set for the HMI user data type.
- The HMI user data type is released.

#### Creating a parameter set type with elements via an HMI user data type

Proceed as follows to create a parameter set type with elements via an HMI user data type:

1. Open the "Parameter set types" folder in the project tree of the HMI device.
2. Double-click "Add new parameter set type".

   A parameter set type with unique standard name and unique ID is created. The "Parameter set types" editor opens.
3. Select the released HMI user data type in the "Data type" column in the "Parameter set types" editor.

   In the editor, parameter set elements which are based on the user data type elements are added to the parameter set type.

   ![Creating a parameter set type with elements via an HMI user data type](images/115290096779_DV_resource.Stream@PNG-en-US.png)

   ![Creating a parameter set type with elements via an HMI user data type](images/115290096779_DV_resource.Stream@PNG-en-US.png)

**Note**

The parameter set type items have the same name and data type as the user data type elements. The name and data type of the parameter set type items are write-protected in the editor.

#### Configuring a parameter set type

To configure the created parameter set type, proceed as follows:

1. Enter a meaningful name for the parameter set type in the "Name" column in the "Parameter set types" editor

   The name uniquely identifies the parameter set type within the HMI device.
2. Enter a language-dependent name for the parameter set type in the "Display name" column.

   The display name appears in the parameter set control in runtime.
3. If required, enter an own number for the parameter set type in the "ID" column.

   The ID uniquely identifies the parameter set type within the HMI device. The ID appears in the parameter set control in runtime.

   ![Configuring a parameter set type](images/115290107147_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a parameter set type](images/115290107147_DV_resource.Stream@PNG-en-US.png)

#### Configuring parameter set type items

To configure the created parameter set type items, proceed as follows:

1. In the "Display name" column of the "Parameter set types" editor configure a language-dependent name for the parameter set type items and corresponding parameters in a parameter set.

   The display name appears in the table of the parameter set control in runtime.
2. Configure a unit of measure In the "Unit of measure" column for parameter set type items and corresponding parameters in a parameter set.

   The unit of measure appears in the table of the parameter set control in runtime.
3. Configure a start value in the "Start value" column for parameter set type items.

   The start value is used to pre-assign the corresponding parameters in a newly created parameter set in runtime.

   ![Configuring parameter set type items](images/115291294859_DV_resource.Stream@PNG-en-US.png)

   ![Configuring parameter set type items](images/115291294859_DV_resource.Stream@PNG-en-US.png)

#### Result

You have created a parameter set type with elements via an HMI user data type.

---

**See also**

[Creating an HMI user data type (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-an-hmi-user-data-type-rt-unified)
  
[Creating HMI user data type elements (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-hmi-user-data-type-elements-rt-unified)
  
["Parameter set types" editor (RT Unified)](#parameter-set-types-editor-rt-unified)
  
[Changing a parameter set type with elements (RT Unified)](#changing-a-parameter-set-type-with-elements-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-hmi-user-data-type-to-a-parameter-set-type-rt-unified)

### Creating a parameter set type with elements via a PLC user data type (RT Unified)

#### Introduction

You have created a PLC user data type with elements. You can assign the user data type to one or more parameter set types and this way apply the elements of the user data type for the parameter set type or types. A parameter set type with elements determines the structure that is used for parameter sets on a machine. Because you do not have to create the elements of the user data type again separately for the parameter set type(s), efficiency and reusability are a given.

> **Note**
>
> Observe the following restrictions when creating the PLC user data type:
>
> - The user data type may have a maximum of 1000 elements.
> - No user data type item may have the data type Time_Of_Day.
> - The ARRAY data type is supported.
>
>   The use of a user data type is not supported in an ARRAY.
>
>   The user data type may have a maximum of 8 levels.

> **Note**
>
> You can also create a parameter set type with elements via an HMI user data type for which the SIMATIC S7-300/400 or SIMATIC S7-1200/1500 communication driver is set.

#### Requirement

- The HMI device has been created.
- A PLC user data type with user data type elements is created in a SIMATIC S7-1200/1500 PLC.
- The "Libraries" task card is open.
- The project library is open.

#### Adding a PLC user data type to the project library

To add a PLC user data type to the project library, follow these steps:

1. Open the PLC's folder in the project tree.
2. Open the folder "PLC data types" in the folder of the controller.

   The created PLC user data type is displayed in the "PLC data types" folder.
3. Move the PLC user data type to the "Types" folder in the project library.

   The "Add type" dialog opens.

   ![Adding a PLC user data type to the project library](images/115291961867_DV_resource.Stream@PNG-en-US.png)

   ![Adding a PLC user data type to the project library](images/115291961867_DV_resource.Stream@PNG-en-US.png)
4. Make the following settings in the dialog:

   - Enter a unique name for the PLC user data type under "Type name".
   - Enter a valid version number for the PLC user data type under "Version".
   - Enter the author responsible for the PLC user data type under "Author".
   - Enter a comment for the PLC user data type under "Comment".
5. Click the "OK" button.

   The PLC user data type is added with a released version to the "Types" folder in the project library.

**Note**

When you use other user data types within the user data type that are not yet available in the library, these user data types are also applied to the library.

#### Creating a parameter set type with elements via a PLC user data type

Proceed as follows to create a user data type with elements via a PLC user data type:

1. Open the "Parameter set types" folder in the project tree.
2. Double-click "Add new parameter set type".

   A parameter set type with unique standard name and unique ID is created. The "Parameter set types" editor opens.
3. Select the released PLC user data type in the "Data type" column in the "Parameter set types" editor.

   In the editor, parameter set elements which are based on the user data type elements are added to the parameter set type.

   ![Creating a parameter set type with elements via a PLC user data type](images/115303491979_DV_resource.Stream@PNG-en-US.png)

   ![Creating a parameter set type with elements via a PLC user data type](images/115303491979_DV_resource.Stream@PNG-en-US.png)

**Note**

The parameter set type items have the same name and data type as the user data type elements. The name and data type of the parameter set type items are write-protected in the editor.

#### Configuring a parameter set type

To configure the created parameter set type, proceed as follows:

1. Enter a meaningful name for the parameter set type in the "Name" column in the "Parameter set types" editor

   The name uniquely identifies the parameter set type within the HMI device.
2. Enter a language-dependent name for the parameter set type in the "Display name" column.

   The display name appears in the parameter set control in runtime.
3. If required, enter an own number for the parameter set type in the "ID" column.

   The ID uniquely identifies the parameter set type within the HMI device. The ID appears in the parameter set control in runtime.

   ![Configuring a parameter set type](images/115303822091_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a parameter set type](images/115303822091_DV_resource.Stream@PNG-en-US.png)

#### Configuring parameter set type items

To configure the created parameter set type items, proceed as follows:

1. In the "Display name" column of the "Parameter set types" editor configure a language-dependent name for the parameter set type items and corresponding parameters in a parameter set.

   The display name appears in the table of the parameter set control in runtime.
2. Configure a unit of measure In the "Unit of measure" column for parameter set type items and corresponding parameters in a parameter set.

   The unit of measure appears in the table of the parameter set control in runtime.
3. Configure a start value in the "Start value" column for parameter set type items.

   The start value is used to pre-assign the corresponding parameters in a newly created parameter set in runtime.

   ![Configuring parameter set type items](images/115304190603_DV_resource.Stream@PNG-en-US.png)

   ![Configuring parameter set type items](images/115304190603_DV_resource.Stream@PNG-en-US.png)

#### Result

You have created a parameter set type with elements via a PLC user data type.

---

**See also**

[Configuring user data types (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-user-data-types-rt-unified)
  
["Parameter set types" editor (RT Unified)](#parameter-set-types-editor-rt-unified)
  
[Changing a parameter set type with elements (RT Unified)](#changing-a-parameter-set-type-with-elements-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-plc-user-data-type-to-a-parameter-set-type-rt-unified)

### Changing a parameter set type with elements (RT Unified)

#### Introduction

You have created one or more parameter set types with elements via a user data type. A parameter set type with elements determines the structure that is used for parameter sets on a machine. You have the following options to change parameter set types with elements:

- You can change one or more parameter set types automatically via a new version of the user data type.
- You can change a parameter set type manually via a new version of the user data type.
- You can change a parameter set type via another user data type.

#### Requirement

- One or more parameter set types with elements are created on the basis of an HMI or PLC user data type.

#### Changing parameter set types automatically via a new version of the user data type

To change parameter set types with elements automatically via a new version of the user data type, follow these steps:

1. Select the released user data type in the project library.
2. Select "Edit type" in the shortcut menu.

   In the case of an HMI user data type the "HMI user data types" editor is opened and a new user data type version with the "In process" status is generated in the project library. In the case of a PLC user data type the "Edit type" dialog is opened.
3. In the case of a PLC user data type click "OK" in the "Edit type" dialog.

   The "PLC data type" editor opens. A new user data type version with the "Testing" status is generated in the project library.
4. Change the user data type in the case of an HMI user data type in the "HMI user data types" editor and in the case of a PLC user data type in the "PLC data types" editor.
5. Select the new user data type version in the project library.
6. Select "Release version" in the shortcut menu.

   The "Release type version" dialog box opens.

   ![Changing parameter set types automatically via a new version of the user data type](images/115305137419_DV_resource.Stream@PNG-en-US.png)

   ![Changing parameter set types automatically via a new version of the user data type](images/115305137419_DV_resource.Stream@PNG-en-US.png)
7. If necessary, change the properties of the version:

   - Enter a unique name for the user data type in the "Type name" field.
   - Enter a valid version number for the version to be released in the "Version" field.
   - Under "Author" enter the editor of the version to be released.
   - Under "Comment" enter a comment on the version to be released.
8. If you want to revise the version management of the user data type, enable the "Delete unused type versions from the library".
9. To automatically change the parameter set type or types via the new user data type version, activate the option "Update instances in the project".
10. Click the "OK" button.

    The parameter set type or types are changed in the following way via the user data type version:

    - An element that you have not changed in the user data type, also remains in the parameter set type with all its settings.
    - An element that you have added new to the user data type is also added to the parameter set type.
    - The element that you have deleted from the user data type is also deleted from the parameter set type.
    - If you have changed the name of an element in the user data type, the parameter set type of the element's name is changed as well. All other properties of the element remain unchanged such as the start value or the display name.
    - If you have changed the data type of an element in the user data type, the parameter set type of the element's data type is changed as well. Other properties of the elements remain unchanged.
    - If you have changed a numerical data type of an element into a string data type in the user data type, the minimum and maximum values previously specified of the element are also removed.

**Note**

An element whose data type you have changed is treated like a new element in runtime. Consequently the values of the element are deleted in the existing parameter sets and the start values are assigned as default to the element.

#### Changing the parameter set type manually via a new version of the user data type

Proceed as follows to change a parameter set type with elements manually via a new version of the user data type:

1. Execute Steps 1 to 8 and 10 of the description above.
2. Open the "Parameter set types" folder in the project navigation.
3. Double-click a created parameter set type.

   The "Parameter set types" editor opens.
4. Select the new user data type version in the "Data type" column in the "Parameter set types" editor.

   The parameter set type is changed via the new user data type version as described in Step 10 of the above description.

#### Changing parameter set type via another user data type

Proceed as follows to change a parameter set type with elements manually via another user data type:

1. Open the "Parameter set types" folder in the project navigation.
2. Double-click a created parameter set type.

   The "Parameter set types" editor opens.
3. Select another released user data type in the "Data type" column in the "Parameter set types" editor.

   The structure of the parameter set type is created completely new in accordance with the structure of the other user data types.

---

**See also**

[Creating a parameter set type with elements via an HMI user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-an-hmi-user-data-type-rt-unified)
  
[Creating a parameter set type with elements via a PLC user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-a-plc-user-data-type-rt-unified)

### Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)

#### Introduction

To exchange parameter sets between an HMI device and PLC in runtime, assign an external HMI tag to a parameter set type created via an HMI user data type in the Engineering System. To this purpose the HMI tag uses the HMI user data type as the data type with which you created the parameter set type.

> **Note**
>
> You can also assign an external HMI tag to a parameter set type that was created via a PLC user data type. In doing so the HMI tag uses the PLC user data type as the data type with which you created the parameter set type.

#### Requirement

- An HMI user data type is created in the HMI device.
- The SIMATIC S7-300/400 or SIMATIC S7 1200/1500 communication driver is set for the HMI user data type.
- User data type elements are added to the HMI user data type.
- The HMI user data type is released.
- A parameter set type with elements is created on the basis of the HMI user data type.
- An external HMI tag is created that uses the HMI user data type as the data type.

#### Procedure

To assign an external HMI tag of the data type HMI user data type to a parameter set type, proceed as follows:

1. Open the "Parameter set types" folder in the project tree.
2. Double-click the created parameter set type.

   The "Parameter set types" editor opens. The Inspector window opens.
3. Select the created HMI tag of the data type "HMI user data type" in the column "Tag" in the "Parameter set types" editor.

   ![Procedure](images/115315493003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/115315493003_DV_resource.Stream@PNG-en-US.png)

#### Result

You have assigned an external HMI tag of the data type "HMI user data type" to a parameter set type.

---

**See also**

[Creating a parameter set type with elements via an HMI user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-an-hmi-user-data-type-rt-unified)
  
[Creating tags with a HMI user data type (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-tags-with-a-hmi-user-data-type-rt-unified)
  
[Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-plc-user-data-type-to-a-parameter-set-type-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)

#### Introduction

To exchange parameter sets between an HMI device and PLC in runtime, assign an external HMI tag to a parameter set type created via a PLC user data type in the Engineering System. In doing so the HMI tag uses the PLC user data type as the data type with which you created the parameter set type.

> **Note**
>
> You can also assign an external HMI tag to a parameter set type which was created via a HMI user data type. To this purpose the HMI tag uses the HMI user data type as the data type with which you created the parameter set type.

#### Requirement

- An HMI device has been created.
- A PLC user data type with user data type items is created in a SIMATIC S7-1200/1500 PLC.
- A parameter set type with elements is created on the basis of the PLC user data type.
- An external HMI tag is created that uses the PLC user data type as the data type.

  > **Note**
  >
  > You have the following possibilities to create an external HMI tag of the data type "PLC user data type":
  >
  > - Assign a PLC tag to an HMI tag, whereby the PLC tag is based on a PLC user data type.
  > - Assign a PLC data block that is based on a PLC user data type to an HMI tag.
  > - Assign a PLC data block element that is based on a PLC user data type to an HMI tag.

#### Procedure

To assign an external HMI tag of the data type "PLC user data type" to a parameter set, follow these steps:

1. Open the "Parameter set types" folder in the project tree.
2. Double-click the created parameter set type.

   The "Parameter set types" editor opens. The Inspector window opens.
3. Select the created HMI tag of the data type "PLC user data type" in the "Tag" column in the "Parameter set types" editor.

   ![Procedure](images/115331797515_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/115331797515_DV_resource.Stream@PNG-en-US.png)

#### Result

You have assigned an external HMI tag of the data type "PLC user data type" to a parameter set type.

---

**See also**

[Creating a parameter set type with elements via a PLC user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-a-plc-user-data-type-rt-unified)
  
[External tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#external-tags-rt-unified)
  
[Creating external tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-external-tags-rt-unified)
  
[Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-hmi-user-data-type-to-a-parameter-set-type-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Transferring and deleting parameter sets automatically (RT Unified)

#### Introduction

In the Engineering System you assign control tags to a parameter set type with elements. The control tags serve to automatically transfer or delete parameter sets between an HMI device and PLC in runtime. In the process either the control program or the HMI device controls the automatic transfer or deleting via control requests.

#### Requirement

- A parameter set type with elements is created on the basis of an HMI or PLC user data type.
- An external HMI tag that uses the HMI or PLC user data type as the data type is assigned to the parameter set type.
- Two control tags with numerical data type are created, for example, "ParameterSetIDTag" and "JobIDTag".

  > **Note**
  >
  > If you want to automatically transfer or delete parameter sets by means of the control program, create 2 external control tags. If you want to automatically transfer or delete parameter sets by means of the HMI device, however, create 2 internal control tags.

  > **Note**
  >
  > The control tags must use a signed data type.
- The "Toolbox" task card is open.

#### Assigning control tags to a parameter set type with elements

Proceed as follows to assign control tags to a parameter set type with elements in the Engineering System:

1. Open the "Parameter set types" folder in the project tree.
2. Double-click the created parameter set type.

   The "Parameter set types" editor opens. The Inspector window opens.
3. Select the control tag "ParameterSetIDTag" in the "Parameter set ID" column in the "Parameter set types" editor.
4. Select the "JobIDTag" control tag in the "Job ID" column.

   ![Assigning control tags to a parameter set type with elements](images/115363551755_DV_resource.Stream@PNG-en-US.png)

   ![Assigning control tags to a parameter set type with elements](images/115363551755_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Please observe each of the following rules to not obtain any errors when compiling the project:
>
> - If you set a control tag in the "Parameter set ID" column of the "Parameter set types" editor, you also set a control tag in the "Job ID" column.
> - Do not set the same control tag in the columns "Parameter set ID" and "Job ID" in the "Parameter set types" editor.
> - If you assign a control tag to a parameter set type in the "Parameter set types" editor, do not assign the same control tag to another parameter set type.

#### Reading a parameter set from the PLC

Proceed as follows to automatically read a parameter set from the PLC and store it in the parameter set memory in runtime:

1. Automatically set the control tag "ParameterSetIDTag" to an ID of an existing parameter set.
2. Automatically set the control tag "JobIDTag" to the control job ID "6".

   The control job is executed. In the case of success the control tag "JobIDTag" is set to the value "0", otherwise to the value "-1".

> **Note**
>
> If you set a non-existing parameter set ID and the control job ID to "6", a new parameter set is created with the parameter set values available in the PLC.

#### Writing a parameter set to the PLC

To automatically load a parameter set from the parameter set memory in runtime and write it into the PLC, follow these steps:

1. Automatically set the control tag "ParameterSetIDTag" to an ID of an existing parameter set.
2. Set the control tag "JobIDTag" automatically to the control job ID "7".

   The control job is executed. In the case of success the control tag "JobIDTag" is set to the value "0", otherwise to the value "-1".

#### Deleting a parameter set

To automatically delete a parameter set from the parameter set memory in runtime, follow these steps:

1. Automatically set the control tag "ParameterSetIDTag" to an ID of an existing parameter set.
2. Set the control tag "JobIDTag" automatically to the control job ID "8".

   The control job is executed. In the case of success the control tag "JobIDTag" is set to the value "0", otherwise to the value "-1".

#### Result

You have assigned control tags to a parameter set type with items in the engineering system and automatically transferred and deleted parameter sets between the HMI device and PLC via the control tags in runtime.

---

**See also**

[Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-hmi-user-data-type-to-a-parameter-set-type-rt-unified)
  
[Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-plc-user-data-type-to-a-parameter-set-type-rt-unified)
  
[External tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#external-tags-rt-unified)
  
[Creating external tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-external-tags-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Transferring parameter sets via scripts (RT Unified)](#transferring-parameter-sets-via-scripts-rt-unified)
  
[Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Transferring parameter sets via scripts (RT Unified)

#### Introduction

In runtime, you can transfer parameter sets via local scripts between the HMI device and PLC. To do so configure the local scripts in the Engineering Systems at events of screen objects or at the "Update" event of tasks.

> **Note**
>
> You can also use system functions in the function list or in scripts to transfer parameter sets between HMI device and PLC:
>
> - With the system function "ReadAndSaveParameterSet" or "ReadAndSaveParameterSet", a parameter set is read from the PLC and saved in the parameter set memory.
> - With the system function "LoadAndWriteParameterSet" or "LoadAndWriteParameterSet", a parameter set is loaded from the parameter set memory and written to the PLC.

#### Code examples for transferring parameter sets

To load a parameter set from the parameter set memory and write it into the PLC, use the following code example:

let ps1 = HMIRuntime.ParameterSetTypes('MyPST1').ParameterSets(1);

ps1.LoadAndWrite(true);

To read a parameter set from the PLC and store it in the parameter set memory, use the following code example:

let ps1 = HMIRuntime.ParameterSetTypes('MyPST1').ParameterSets(1);

ps1.ReadAndSave(HMIRuntime.ParameterSetTypes.Enums.hmiOverwrite.Disabled, true);

| Symbol | Meaning |
| --- | --- |
| ![Code examples for transferring parameter sets](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| You can find the code examples in the shortcut menu of the "Scripts" editor under "Snippets > HMI Runtime > Parameter Set". |  |

---

**See also**

[Local scripts (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#local-scripts-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)
  
[LoadAndWriteParameterSet (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#loadandwriteparameterset-rt-unified)
  
[ReadAndSaveParameterSet (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#readandsaveparameterset-rt-unified)

### Configuring the parameter set view (RT Unified)

#### Introduction

To display, manage and exchange parameter sets with the PLC in runtime, use a parameter set control. You configure a parameter set control in the engineering system.

#### Requirement

- At least one parameter set type with elements has been created.
- A screen is open.
- The "Toolbox" task card is open.

#### Procedure

To configure a parameter set control, proceed as follows:

1. Insert the "Parameter set control" object from the "Tools" task card into the screen.

   ![Procedure](images/130507702795_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/130507702795_DV_resource.Stream@PNG-en-US.png)
2. Set the desired height, width and position for the parameter set control in the Inspector window under "Properties > Size and Position".
3. If you only want to use a particular parameter set type with its parameter sets in runtime, select the desired parameter set type under "Properties > General > Fixed parameter set type".
4. Change the labels of the fields, if required.
5. If required, change the display of the parameter table under "Properties > Miscellaneous > Parameter view".
6. In "Properties > Miscellaneous > Editing mode", configure the activation status of the toolbar buttons "Create", "Save", "Save as", "Rename" and "Delete" as required.

   These toolbar buttons are used to edit parameter sets.
7. If you want to hide specific buttons in the toolbar, deactivate the "Visibility" property under "Properties > Miscellaneous > Toolbar > Elements" in the settings of the corresponding button.
8. Under "Properties > Miscellaneous > Time zone", change the time zone as required by entering a different numerical value.

   The numerical value stands for a time zone, for example:

   - "-1" stands for UTC-1h (Central European Time, standard time)
   - "1" stands for UTC-12h (International Date Line West)
   - "2" stands for UTC-11h (Hawaii)

**Note**

The parameter set type is only visible in the parameter set control in runtime when the extended style is used in the runtime settings under "General > Screen".

**Note**

A tag that you use as a dynamization tag of the fixed parameter set type in the parameter set control must have the data type "String" or "WString".

**Note**

To change the visibility of columns, click on "Columns" under "Properties > Miscellaneous > Parameter view". In the extended parameter control display, you can enable or disable the visibility of individual columns under "Visibility". Changing the visibility via the preset value in the "Blocks" property is not supported.

---

**See also**

[Configuring reordering of the columns (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#configuring-reordering-of-the-columns-rt-unified)
  
[Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
  
[Creating a parameter set type with elements via an HMI user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-an-hmi-user-data-type-rt-unified)
  
[Creating a parameter set type with elements via a PLC user data type (RT Unified)](#creating-a-parameter-set-type-with-elements-via-a-plc-user-data-type-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)
  
[Exporting and importing parameter sets (RT Unified)](#exporting-and-importing-parameter-sets-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Assigning an edit tag to a parameter set item (RT Unified)

#### Introduction

To adjust the values of the parameter sets in the HMI device and the PLC in runtime, you can assign a local session HMI tag to a parameter set type in the Engineering System.

The edit tag enables you to manage the values of a parameter set in a screen. To do this, you use system functions or scripts to transfer values between the HMI device and the PLC.

#### Requirement

- An HMI device has been created.
- An HMI or PLC user data type with user data type items is created in a SIMATIC S7-1200/1500 PLC.
- A parameter set type with parameter set items based on the HMI or PLC user data type is created.
- A local session HMI tag with the same number of items and the same data type is created.

  The HMI tag must not contain any information about the range (Upper 2, Lower 2).

#### Procedure

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| To create the same structure for the edit tag as for the parameter set tag, copy the corresponding data type in the library. Change the connection to "Internal connection" in the copy. In this way, you make the data type available for a local session edit tag. |  |

To assign a local session HMI tag to a parameter set, follow these steps:

1. Open the "Parameter set types" folder in the project tree.
2. Double-click the created parameter set type.

   The "Parameter set types" editor opens.
3. In the "Parameter set types" editor, select a local session HMI tag in the "Edit tag" column.

#### Result

You have assigned a local session HMI tag to a parameter set type.

### Configuring parameter sets without parameter set control (RT Unified)

#### Introduction

In one or more screens, you configure an individual input mask as an extension or replacement of the parameter set control. You create the input mask from I/O fields and other display and operating objects. System functions or scripts are used to configure the parameter set functionality, such as saving parameter sets.

#### Use

Configuring directly in screens allows you to display and manage parameter sets according to your needs. You can spread parameter sets containing lots of entries across several screens to create a better overview. For example, you can configure a separate screen with the corresponding input masks for the parameter sets for each area of the plant.

You can visually map your machine in a screen using graphical screen objects. This enables you to display parameter settings clearly by positioning I/O fields directly next to machine elements such as axes or guide rails. This is how you produce a direct relationship between the values and the machine.

You configure system functions and scripts with which you call up system information, create and manage parameter sets or adapt active parameter sets via edit tags.

#### Requirement

- The parameter set type is created.
- The "Screens" editor is open.

#### Procedure

To configure a screen with which you can display and manage parameter sets, follow these steps:

1. Configure a screen and create the I/O fields for the recipe input mask in it.

   You can create multiple screens to suit the size and complexity of the recipe.
2. Configure the I/O fields with the tags that you have connected to the parameter set items.
3. Configure I/O fields for the parameter set type and parameter set selection.
4. Configure the system functions for editing parameter sets on the configured operator controls.

   Operator controls are configured buttons in the screen or function keys on the HMI device.

   In the "Scripts" editor, you will find snippets with the system functions under "HMI Runtime > Parameter set".

#### Alternative procedure

1. Configure a parameter set control as a selection list for parameter set types and parameter sets.
2. Hide the buttons that are not required in the parameter set control.
3. Configure the system functions for editing parameter sets on the configured operator controls.

#### Result

A screen that offers the possibility to display and manage parameter sets has been created.

With the use of scripts and the use of system functions, you have the following possibilities:

- Reading the name of a parameter set
- Reading the name of a type of parameter set
- Reading a selected parameter set
- Writing a parameter set to the PLC
- Trigger event on parameter set
- Display of system information of the status display in a separate screen

---

**See also**

[System functions (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified)
  
[ParameterSetTypes (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#parametersettypes-rt-unified)
  
[ParameterSetType (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#parametersettype-rt-unified)

## Using parameter sets in runtime (RT Unified)

This section contains information on the following topics:

- [Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)
- [Exporting and importing parameter sets (RT Unified)](#exporting-and-importing-parameter-sets-rt-unified)
- [Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Managing parameter sets (RT Unified)

#### Introduction

You manage parameter sets for different productions in a parameter set control in runtime. You have the following options for managing parameter sets:

- Create new parameter sets
- Copy parameter sets
- Change parameter sets
- Delete parameter sets
- Rename parameter sets

#### Requirement

- At least one parameter set type with elements has been created.
- A parameter set control has been configured.
- The project is in runtime.

#### Creating a new parameter set

To create a new parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type for which you want to create a new parameter set.

   The elements of the selected parameter set type are displayed in the table.

   ![Creating a new parameter set](images/115373673227_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115373673227_DV_resource.Stream@PNG-en-US.png)
2. Click the "Create" button.

   The "Create parameter set" dialog opens.

   ![Creating a new parameter set](images/115378931339_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115378931339_DV_resource.Stream@PNG-en-US.png)
3. Enter a unique parameter set name under "Parameter set name".
4. Enter a unique parameter set ID under "Number".
5. Confirm the dialog.

   A new parameter set has been created and saved. The parameters of the new parameter set are displayed in the table. The parameters have the same values in the columns "Name" and "Unit of measurement" as the elements of the previously selected parameter set type. The defined start values are applied for the "Value" column. If you have not defined start values, the corresponding default values are used.

   ![Creating a new parameter set](images/115379043851_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379043851_DV_resource.Stream@PNG-en-US.png)
6. Enter values for the parameters in the "Value" column.

   Depending on the configuration, the parameters already contain start values.

   ![Creating a new parameter set](images/115379053963_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379053963_DV_resource.Stream@PNG-en-US.png)
7. Click the "Save" button.

   ![Creating a new parameter set](images/115379448075_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379448075_DV_resource.Stream@PNG-en-US.png)

**Note**

If you do not make any entries in the "Create parameter set" dialog and confirm the dialog, a new parameter set is also created and saved. In this case the new parameter set, however, has a unique parameter set name and a unique parameter set ID which were both automatically assigned by the system.

**Note**

The character ' is not permitted in the value of a parameter set.

#### Copying a parameter set

To copy a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to copy an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to copy.

   The parameters of the selected parameter set are displayed in the table.
3. Click the "Save as" button.

   The "Save parameter set" dialog opens. A unique parameter set name is pre-assigned to the "Parameter set name" field.

   ![Copying a parameter set](images/115379637387_DV_resource.Stream@PNG-en-US.png)

   ![Copying a parameter set](images/115379637387_DV_resource.Stream@PNG-en-US.png)
4. Enter a different unique parameter set name under "Parameter set name" as required.
5. Enter a unique parameter set ID under "Number" as required.
6. Confirm the dialog.

**Note**

If you do not enter a parameter set ID in the "Save parameter set" dialog and confirm the dialog, a unique parameter set ID is automatically assigned to the new parameter set.

#### Changing the parameter set

To change a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to change an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to change.

   The parameters of the selected parameter set are displayed in the table.
3. Edit the values of the parameters in the "Value" column.
4. Click the "Save" button.

#### Deleting a parameter set

To delete a parameter set, proceed as follows:

1. In the "Parameter set type" field select the parameter set type in which you want to delete an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to delete.

   The parameters of the selected parameter set are displayed in the table.
3. Click "Delete".

#### Renaming a parameter set

To rename a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to rename an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to rename.

   The parameters of the selected parameter set are displayed in the table.
3. Click the "Rename" button.

   The "Rename parameter set" dialog opens.

   ![Renaming a parameter set](images/115379941899_DV_resource.Stream@PNG-en-US.png)

   ![Renaming a parameter set](images/115379941899_DV_resource.Stream@PNG-en-US.png)
4. Enter a different unique name for the parameter set under "Parameter set name".
5. Confirm the dialog.

---

**See also**

[Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Exporting and importing parameter sets (RT Unified)](#exporting-and-importing-parameter-sets-rt-unified)
  
[Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)

### Exporting and importing parameter sets (RT Unified)

#### Introduction

In a parameter set control in runtime you export parameter sets from the parameter set memory to a "*.tsv" file to be able to edit them a text editor. In a parameter set control in runtime you furthermore import parameter sets from a "*.tsv" file into the parameter set memory. A "*.tsv" file is a text file that uses the tabulator as a list separator.

> **Note**
>
> To export and import the parameter sets, you can also use the system functions in the function list or in the scripts:
>
> - With the system function "ExportParameterSets" or "ExportParameterSets", the parameter sets are exported from the parameter set memory to a "*.tsv" file.
> - With the system function "ImportParameterSets" or "ImportParameterSets", the parameter records are imported from a "*.tsv" file into the parameter set memory.
>
> If the parameter `OutputStatus` is set to `True`, a status message is output in an alarm control configured in the screen.

#### Requirement

- At least one parameter set type with elements has been created.
- A parameter set control has been configured.
- The project is in runtime.

#### Exporting parameter sets of a parameter set type

Follow these steps to export the parameter sets of a parameter set type:

1. In the "Parameter set type" field, select the parameter set type whose parameter sets you want to export.

   ![Exporting parameter sets of a parameter set type](images/115380273035_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/115380273035_DV_resource.Stream@PNG-en-US.png)
2. Click the ![Exporting parameter sets of a parameter set type](images/137222023435_DV_resource.Stream@PNG-de-DE.png) "Export" button.

   The "Export parameter set" dialog box opens. The name of the parameter set control is pre-assigned in the "File name" field.

   ![Exporting parameter sets of a parameter set type](images/143206337291_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/143206337291_DV_resource.Stream@PNG-en-US.png)
3. If appropriate, change the name of the file to which you want to export the parameter sets under "File name".
4. Enable "Generate checksum" to export the parameter data set with a checksum.

   Parameter data sets with a checksum cannot be imported if they have been manipulated in the meantime.
5. Confirm the dialog.

   The parameter sets are exported to a ".tsv" file.

   This file is stored according to the download settings.

   The file has the following structure:

   - The first line contains the file header. The file header consists of identifier, delimiter, version of the exported file, decimal symbol and information on the number of languages in which the name of the parameter sets is stored.

     The line must not be changed. Otherwise, it is not possible to import parameter sets.
   - The second line contains the name of the parameter set type.
   - The third row contains the headers for parameter sets. LCID of the language and the names of the parameter set type items are listed.

     The header for parameter sets must not be changed.
   - From the fourth line on the parameter sets are listed.

   ![Exporting parameter sets of a parameter set type](images/115381790859_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/115381790859_DV_resource.Stream@PNG-en-US.png)

#### Edit exported file

1. You can customize the file to meet your needs:

   - Change the values of existing parameters.
   - Add parameter sets.

   To be able to import the parameter sets after editing, note the following information:
2. Save the changes.

**Note**

- The parameters must be valid for the defined data type.
- The parameters must be within the limits defined in the parameter set type item.
- ID and name of the individual parameter sets must be unique.

#### Importing parameter sets into a parameter set type

To be able to import parameter sets, note the following requirements:

> **Note**
>
> - The import file must have the same file header and the same header for parameter sets as the export file. Otherwise, it is not possible to import parameter sets.
> - There is no parameter set with the same display name in any of the configured languages.
> - The numerical values in the import file are within the permitted value range of the corresponding configured data type.

To import parameter sets into a parameter set type, follow these steps:

1. In the "Parameter set type" field, select the parameter set type into which you want to import the parameter sets.
2. Click the ![Importing parameter sets into a parameter set type](images/137222031627_DV_resource.Stream@PNG-de-DE.png) "Import" button.

   The "Import parameter set" dialog box opens.

   ![Importing parameter sets into a parameter set type](images/143206326667_DV_resource.Stream@PNG-en-US.png)

   ![Importing parameter sets into a parameter set type](images/143206326667_DV_resource.Stream@PNG-en-US.png)
3. Select the file from which you want to import the parameter sets.
4. To overwrite parameter sets in the parameter set control that have the same ID as the imported parameter sets, activate the "Overwrite" option.

   Any added parameter sets whose IDs and parameter set names deviate from the existing parameter sets are imported regardless of the "Overwrite" option.
5. Enable "Check checksum" when importing a parameter data set exported with the "Generate checksum" option.
6. Confirm the dialog.

   The parameter sets are imported to the parameter set type.

**Note**

If you deactivate overwriting and if a parameter set with the same ID or the same parameter set name exists in the parameter set control, the import of parameter sets is not possible.

---

**See also**

[SysFct.ExportParameterSets() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexportparametersets-rt-unified)
  
[SysFct.ImportParameterSets() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctimportparametersets-rt-unified)
  
[Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)

### Transferring parameter sets (RT Unified)

#### Introduction

You have assigned an external HMI tag of the data type HMI or PLC user data type to a parameter set type. In a parameter set control in runtime you transfer the values of parameter sets to the PLC via the HMI tag. The parameter set values are used to set up machines for different productions.

In a parameter set control in runtime you furthermore read active parameter sets from the PLC into the parameter set control via the HMI tag. The read parameter set values are stored in the parameter set memory. By reading from the PLC, you call up currently used values from production machines for later use.

> **Note**
>
> You can also use system functions in the function list or in scripts to transfer parameter sets between HMI device and PLC:
>
> - With the system function "ReadAndSaveParameterSet" or "ReadAndSaveParameterSet", a parameter set is read from the PLC and saved in the parameter set memory.
> - With the system function "LoadAndWriteParameterSet" or "LoadAndWriteParameterSet", a parameter set is loaded from the parameter set memory and written to the PLC.

#### Requirement

- A parameter set type with elements has been created.
- An external HMI tag of the data type HMI or PLC user data type is assigned to the parameter set type.
- A parameter set control has been configured.
- The project is in runtime.
- At least one parameter set has been created in the parameter set type.

#### Transferring a parameter set to the PLC

To transfer a parameter set to the PLC, follow these steps:

1. In the "Parameter set type" field, select the parameter set type.
2. In the "Parameter set" field, select the parameter set whose values you want to transfer to the PLC.

   ![Transferring a parameter set to the PLC](images/115381863307_DV_resource.Stream@PNG-en-US.png)

   ![Transferring a parameter set to the PLC](images/115381863307_DV_resource.Stream@PNG-en-US.png)
3. Click the "Write to PLC" button.

#### Reading a parameter set from PLC

To read a parameter set from the PLC, follow these steps:

1. In the "Parameter set type" field, select the parameter set type.
2. In the "Parameter set" field, select the parameter set whose values you want to read from the PLC.
3. Click the "Read from PLC" button.

**Note**

If do you not select a parameter set in the in the "Parameter set" field, a new parameter set is created in the parameter set control while reading from the PLC.

> **Note**
>
> A parameter set cannot be read from the PLC if minimum and/or maximum values are defined for a parameter set type item and the value in the parameter set to be transferred is outside this range. An alarm is triggered.

#### Result

You have transferred the values of parameter sets between the HMI device and PLC.

---

**See also**

[LoadAndWriteParameterSet (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#loadandwriteparameterset-rt-unified)
  
[ReadAndSaveParameterSet (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#readandsaveparameterset-rt-unified)
  
[Assigning a tag of the data type HMI user data type to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-hmi-user-data-type-to-a-parameter-set-type-rt-unified)
  
[Assigning a tag of the data type "PLC user data type" to a parameter set type (RT Unified)](#assigning-a-tag-of-the-data-type-plc-user-data-type-to-a-parameter-set-type-rt-unified)
  
[Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
  
[Configuring the parameter set view (RT Unified)](#configuring-the-parameter-set-view-rt-unified)
  
[Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)
  
[Transferring and deleting parameter sets automatically (RT Unified)](#transferring-and-deleting-parameter-sets-automatically-rt-unified)
  
[Transferring parameter sets via scripts (RT Unified)](#transferring-parameter-sets-via-scripts-rt-unified)
