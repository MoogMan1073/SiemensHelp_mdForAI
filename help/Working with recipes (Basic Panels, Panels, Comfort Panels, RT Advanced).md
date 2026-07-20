---
title: "Working with recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)"
package: RecipesWCCAenUS
topics: 59
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Recipes in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipes-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring Recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Examples (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-basic-panels-panels-comfort-panels-rt-advanced)

## Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
- [Examples for using recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-for-using-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-structure-basic-panels-panels-comfort-panels-rt-advanced)
- [Display of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#display-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Special features of some devices (Basic Panels, Panels, Comfort Panels, RT Advanced)](#special-features-of-some-devices-basic-panels-panels-comfort-panels-rt-advanced)
- [Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
- ["Recipes" editor (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipes-editor-basic-panels-panels-comfort-panels-rt-advanced)

### Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Recipes are collections of related data, for example, machine parameterizations or production data.

Examples:

- Machine parameter settings that are needed to convert production to a different product variant.
- Product components that result in different compositions for different end products.

A recipe has a fixed data structure. The structure of a recipe is defined during configuration. A recipe contains recipe data records. These differ in terms of their values, but not their structure.

Recipes are stored on the HMI device or on an external storage medium. Recipe data records are always transferred complete and in a single pass between the HMI device and the PLC. In addition, production data can be imported in runtime, in the form of a CSV file.

> **Note**
>
> **Restrictions for Import / Export**
>
> It is not possible to export or import the recipes for the following HMI devices:
>
> - Basic Panels
>
> Complete recipe data, but not single recipe data records, can be exported and imported using ProSave in CSV format and transferred to the HMI device. Thereby, Runtime is interrupted.

#### Using recipes

Recipes can be used in the following situations:

- Manual production

  You select the required recipe data and display it on the HMI device. You modify the recipe data as required and save it on the HMI device. You transfer the recipe data to the PLC.
- Automatic production

  The control program starts transfer of the recipe data between the PLC and HMI device. You can also start the transfer from the HMI device. Production is then implemented automatically. It is not essential to display or modify the data.
- Teach-in mode

  You optimize production data that was optimized manually on the system, e.g. axis positions or filling volumes. The values thus determined are transferred to the HMI device and saved in a recipe data record. You can then transfer the saved recipe data back to the PLC at a later date.

#### Entering and modifying the recipe data

You enter the data in the individual recipe data records and modify it as required. The following options are available:

- Data entry during configuration

  If the production data exists already, you enter the data in the "Recipes" editor during recipe configuration.
- Entering the data in Runtime

  If you have to frequently modify production data, you can do this directly in Runtime as follows:

  - Enter the data directly on the HMI device.
  - Set the parameters directly on the machine. You then transfer the data from the PLC to the HMI device and save it in the recipe.

---

**See also**

[General configuration procedure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#general-configuration-procedure-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-structure-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Special features of some devices (Basic Panels, Panels, Comfort Panels, RT Advanced)](#special-features-of-some-devices-basic-panels-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
["Recipes" editor (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipes-editor-basic-panels-panels-comfort-panels-rt-advanced)
  
[Display of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#display-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)
  
[Examples for using recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-for-using-recipes-basic-panels-panels-comfort-panels-rt-advanced)

### Examples for using recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

Recipes are used in the manufacturing industry and mechanical engineering, for example. The following recipes show typical applications which you can implement with the recipe function of WinCC:

- Machine parameter assignment

  One field of application for recipes is the assignment of machine parameters in the manufacturing industry: A machine cuts wooden boards to a certain size and drills holes. The guide rails and drill have to be moved to new positions according to the board size. The required position data are stored as data records in a recipe. You reassign the machine parameters using "Teach in" mode if, for example, a new board size is to be processed. You transfer the new position data directly from the PLC to the HMI device and save it as a new data record.
- Batch production

  Batch production in the food processing industry represents another field of application for recipes: A filling station in a fruit juice plant produces juice, nectar, and fruit drinks in a variety of flavors. The ingredients are always the same, differing only in their mixing ratios. Each flavor corresponds to a recipe. Each mixing ratio corresponds to a data record. All of the required data for a mixing ratio can be transferred to the machine control at the touch of a button.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

The basic structure of a recipe is illustrated with reference to the filling station in a fruit juice plant.

There may be several different recipes in an HMI device. A recipe can be compared to an index card box that contains several index cards. The index card box contains several variants for manufacturing a product family. All the data for each manufacturing variant is contained on a single index card.

Example:

In a soft drinks production plant, a recipe is needed for different flavors. Drink variants include fruit juice drink, juice and nectar.

#### Recipe

The recipe contains all the recipe data records for the different drink variants.

![Recipe](images/7581210507_DV_resource.Stream@PNG-en-US.png)

#### Recipe data records

Each index card represents a recipe data record needed to manufacture a product variant.

#### Recipe entries

Each index card in a drawer has the same structure. All the index cards contain fields for the different ingredients. Each field corresponds to a recipe entry. All the records of a recipe thus contain the same entries. The records differ, however, in the value of the individual entries.

Example:

All the drinks contain the following ingredients:

- Water
- Concentrate
- Sugar
- Flavoring

The records for juice drink, fruit juice or nectar differ, however, in the quantity of sugar used in production.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Display of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You can display recipes in the following ways:

- Recipe view
- Recipe screen

#### Input in the recipe view and recipe screen

You change the values of a recipe in the recipe screen or recipe view and thus modify the manufacturing process or a machine.

The recipe view and recipe screen can perform the same functions when using recipes. They differ in the following respects:

- Display options
- Operation
- Possibility of transferring data between the PLC and the HMI device

#### Recipe view

The recipe view is suitable for viewing simple recipes.

The recipe view is an off-the-shelf WinCC display and operator control object for managing recipe data records. The recipe view is always part of a screen. The recipe view shows recipe data records in tabular form. You adapt the appearance and the possible operations to suit your specific needs.

![Recipe view](images/72836687243_DV_resource.Stream@PNG-en-US.png)

If you are editing recipes with a recipe view in your project, the values are saved in recipe data records. The values are not transferred between the HMI device and PLC until you use the relevant operator control object.

#### Recipe screen

The recipe screen is an individual screen that contains:

- Input fields for recipe variables
- Operator control objects for using the recipes, e.g. "SaveDataRecord"

  ![Recipe screen](images/72836363019_DV_resource.Stream@PNG-en-US.png)

The recipe screen is suitable in the following situations:

- Large recipes
- Allocation of recipe fields to the graphic display of the relevant plant area
- Breakdown of the recipe data into several screens

  > **Note**
  >
  > The values of recipe variables are transferred between the PLC and recipe screen at the following times depending on the configuration:
  >
  > - Immediately after modification
  > - When a relevant operator control object is used

#### Synchronizing recipe view and recipe screen

There may be differences in Runtime between the values displayed in the recipe view and the values saved in the associated tags when you edit recipes in both a recipe view and a recipe screen. To prevent this, you must synchronize the recipe data record values with the values of the recipe tags.

A complete recipe data record will always be saved or synchronized.

> **Note**
>
> Recipe tags can only be synchronized in the advanced recipe view. Synchronization only takes place if the "Synchronize recipe view and recipe tags" setting is activated for the recipe.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Flow of data in recipes

The following picture illustrates the flow of data in recipes:

![Flow of data in recipes](images/24576721547_DV_resource.Stream@PNG-en-US.png)

#### Interaction between the components

There is interaction between the following components at runtime:

- Recipe view / recipe screen

  On the HMI device, recipes are displayed and edited in the recipe view or in a recipe screen:

  - The recipe data records from the internal memory of the HMI device are displayed and edited in the recipe view.
  - The values of the recipe tags are displayed and edited in the recipe screen.

  You synchronize the values displayed in the recipe view with the values of recipe tags according to the configuration.
- HMI device recipe memory

  Recipes are saved in the form of recipe data records in the HMI device's recipe memory.
- Recipe tags

  The recipe tags contain recipe data. When you edit recipes in a recipe screen, the recipe values are stored in recipe tags. The point at which the values of the recipe tags are exchanged with the PLC depends on the configuration.

  > **Note**
  >
  > You can synchronize the recipe tags with the recipe data records so that the same values are saved in both.

#### Loading and saving recipe data

Complete recipe data records are loaded from or saved to the recipe memory on the HMI device in the recipe view.

![Loading and saving recipe data](images/24581446411_DV_resource.Stream@PNG-en-US.png)

The values of the recipe data record are loaded from the recipe memory to the recipe tags in the recipe screen. When they are saved, the values of the recipe tags are saved to a recipe data record in the recipe memory.

#### Transferring the recipe values between the HMI device and the PLC

Complete recipe data records are transferred between the recipe view and PLC.

![Transferring the recipe values between the HMI device and the PLC](images/24582843275_DV_resource.Stream@PNG-en-US.png)

The following transfers are possible between the recipe screen and PLC, depending on the configuration:

- Transferring recipe data records between recipe view and recipe tags
- Immediate transfer of individual modified values between the recipe tags and PLC. The following settings are needed in the recipe in order to do this:

  - "Synchronizing recipe view and recipe tags" is activated.
  - "Manual transfer of individual modified values (teach-in mode)" is deactivated.

Recipe data records can be transferred directly between the HMI device and PLC. In these situations, the display on the HMI device is not essential.

#### Exporting and importing recipe data records

Recipe data records are exported from the HMI device recipe memory and are saved to a CSV file on the external storage medium. The records can be reimported from the storage medium to the recipe memory.

![Exporting and importing recipe data records](images/24583190539_DV_resource.Stream@PNG-en-US.png)

The following external storage media may be used, depending on the HMI device:

- No storage medium, for example, for basic panels
- Memory card
- USB stick
- Hard disk

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Recipes are configured differently according to the intended use:

- If you are editing recipes with a recipe view in your project, the values are only saved in recipe data records.
- If you are editing recipes in a recipe screen in your project, the values are saved in recipe tags.

The following possible settings determine how the recipe data records, recipe tags and PLC all interact.

#### "Synchronizing recipe view and recipe tags" deactivated

The data in a data record is only displayed and can only be edited in the recipe view. If you use data outside the recipe view, they are not synchronized with the recipe view.

> **Note**
>
> When "Synchronization" &gt; "Synchronize recipe tags" is deactivated and "Display table" is deactivated in the recipe control under "Properties &gt; Table", then recipe data records cannot be sent to or from the PLC in Runtime using the "Write to PLC" and "Read from PLC" buttons.

#### "Synchronizing recipe view and recipe tags" activated

There may be differences in Runtime between the values displayed in the recipe view and the values saved in the associated tags when you edit recipes in both a recipe view and a recipe screen. To prevent this, you must synchronize the recipe data record values with the values of the recipe tags.

!["Synchronizing recipe view and recipe tags" activated](images/24584070411_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Recipe tags can only be synchronized in the advanced recipe view.

The values of the recipe view and the associated recipe tags are not synchronized automatically. The recipe tags and the recipe view are not synchronized until you use the operating element with the "RecipeViewSynchronizeDataRecordWithTags" function.

#### "Synchronize recipe view and recipe tags" activated and "Manual transfer of individual modified values (teach-in mode)" activated

With this setting, modified recipe values are not synchronized immediately between the recipe tags in the recipe screen of the HMI device,and PLC.

There must be an operating element with the "SetDataRecordToPLC" and "GetDataRecordFromPLC" functions present in order to synchronize the values.

If recipe values are changed in the controller, the modified values are displayed immediately in the recipe screen if you use the operating element with the "GetDataRecordFromPLC" function.

#### "Synchronize recipe view and recipe tags" activated and "Manual transfer of individual modified values (teach-in mode)" deactivated

With this setting, modified recipe values are synchronized immediately between the recipe tags on the HMI device and PLC.

When you change recipe values in the recipe screen, these changes are applied immediately by the PLC and immediately influence the process.

If recipe values are changed in the PLC, the changed values are displayed immediately in the recipe screen.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Special features of some devices (Basic Panels, Panels, Comfort Panels, RT Advanced)

![Figure](images/24584084875_DV_resource.Stream@PNG-en-US.png)

Basic Panels behave differently to other HMI devices in the following respects:

- Only the simple recipe view is supported.
- Recipe tags are always synchronized with the recipe view (see figure above): When the operator changes a value of the recipe element in recipe view, the value of the associated recipe tag will also change.
- Recipe tags are not automatically transferred between the PLC and HMI device when they are modified. Recipe tags are always transferred manually in teach-in mode.

  There must be an operator control object with the "SetDataRecordToPLC" and "GetDataRecordFromPLC" functions present in order to synchronize the values with the PLC.

  > **Note**
  >
  > **Restrictions for recipe tags**
  >
  > Generally, recipe tags cannot be used in Basic Panels, except in a recipe.

  > **Note**
  >
  > **Restrictions for Import / Export**
  >
  > It is not possible to export or import the recipes for the following HMI devices:
  >
  > - Basic Panels
  >
  > Complete recipe data, but not single recipe data records, can be exported and imported using ProSave in CSV format and transferred to the HMI device. Thereby, Runtime is interrupted.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Data loss with several recipe views in the screen**  Only applies for Basic Panels: If two or more recipe views show the same recipe in a screen, you have a conflict when accessing the data.  The result is data loss and unpredictable status of recipe data.  Make sure the operators do not select and edit the same recipe in different recipe views.  - Display only one recipe in a recipe view. - Display a different recipe in each recipe view. |  |

  > **Note**
  >
  > **Saving recipes on Comfort Panels**
  >
  > Recipes should be preferably saved on the SD card rather than in the built-in flash memory.

#### Interaction between the components

There is interaction between the following components at runtime:

- Recipe view

  Recipes are displayed and edited in the recipe view on the HMI device.

  The recipe data records from the internal memory of the HMI device are displayed and edited in the recipe view.
- HMI device recipe memory

  Recipes are saved in the form of recipe data records in the HMI device's recipe memory.
- Recipe tags

  The recipe tags contain the values of recipe elements.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Overview

When recipe data records are transferred between the HMI device and PLC, both communication peers access common communication areas on the other peer.

Recipe data records are always transferred directly. The values of the tags are written directly to or read directly from the configured addresses without being placed on the clipboard.

#### Data transfer types

There are two ways to transfer recipe data records between the HMI device and PLC:

- Transfer without coordination
- Coordinated transfer via the "Data record" area pointer.

  > **Note**
  >
  > **Coordinated transfer**
  >
  > Transfer with coordinated transfer is used to prevent the uncontrolled overwriting of data in either direction in your control program.

  > **Note**
  >
  > **Automatic/manual synchronization**
  >
  > The "Manual transfer of individual modified values (teach-in mode)" option gives you control over how recipes are synchronized. If you select this option, you can make changes manually and then transfer them to the controller. If you deactivate this option, the recipes synchronize automatically and manual changes generate an error message.

#### Requirements for coordinated transfer

The following requirements apply to coordinated transfer:

- The "Data record" area pointer must be set up for the required connection in the "Communication &gt; Connections" editor.
- In the properties of the recipe "Coordinated transfer of data records" is activated.
- The connection to the PLC is specified in the properties of the recipe with which the HMI device coordinates the transfer.

#### Coordinated transfer

In the case of coordinated transfer, both the PLC and the HMI device set the status bits in the shared data compartment.

Coordinated transfer of recipe data records can be a useful solution in the following cases:

- The PLC is the "active partner" for the transfer of recipe data records.
- The PLC evaluates information about the recipe number and name, as well as the recipe data record number and name.
- The transfer of recipe data records is started by the following PLC jobs:

  - "Set_data_record_in_PLC"
  - "Get_data_record_from_PLC"

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### "Recipes" editor (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You can create, configure and edit recipes, recipe entries and recipe data records in the "Recipes" editor. The "Recipes" editor also allows you to enter values in recipe data records.

#### Structure of the "Recipes" editor

You create recipes in the top part of the table editor. You can also configure them there or in the Inspector window.

The bottom part of the table editor has the following tabs:

- Elements

  Define the recipe elements of the selected recipe using the table cells provided here. You can move recipe elements within the table with the shortcut menu commands, "Up" and "Down".
- Data records

  Define the values of the data records of the selected recipe using the table cells provided here.

  ![Structure of the "Recipes" editor](images/170767461515_DV_resource.Stream@PNG-en-US.png)

You can then configure the selected recipe, the recipe element or the recipe data record in the Inspector window. You will find further notes on configuring the components of a recipe under "Configuring Recipes".

#### Recipe settings

The following settings are available for recipes:

| Setting | Description |
| --- | --- |
| Name of the recipe | This is a unique identification for the recipe within the HMI device. |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Assign descriptive names or designations which the operator can associate directly with a recipe, e.g. "fruit juice drink". |
| Recipe number | This is a unique identification for the recipe within the HMI device. |
| Version | Information about the recipe. The date and time of the last change to the recipe is set by default. |
| Path | Defines the storage location for recipes. The recipes are stored as a file. |
| Size type [fixed] | The recipe data records are limited to a predetermined number by default. |
| Number of data records [fixed] | Maximum number of data records in a recipe in Runtime. The number is limited by the recipe memory of the HMI device. |
| Communication type [fixed] | The recipe data records are written directly to the addresses of the recipe tags and read from there. |
| Tooltip | Tooltip for the recipe which is shown to the operator in Runtime. |

> **Note**
>
> **Path**
>
> The storage location depends on the storage media available on the HMI device.
>
> **Basic Panels**
>
> These HMI devices have no external memory. Recipes are always saved in the internal Flash memory. The "Path" setting is therefore not available.

#### Recipe element settings

You can make the following settings on the "Elements" tab:

| Setting | Description |
| --- | --- |
| Name of the recipe element | Identifies a recipe element uniquely within the recipe. Enter meaningful names or labels that you can allocate uniquely, such as axis labels on a machine or ingredients such as "Flavoring". |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Assign meaningful names or designations which the operator can associate directly, e.g. "fruit juice flavoring". |
| Recipe tag | An assigned tag in Runtime stores the current value of the recipe element in the recipe data record. |
| Data type | Data type of the recipe tag. |
| Data length [fixed] | Data length of the recipe tag, depending on the data type. |
| Text list | Text is assigned to a value or range of values in a text list. You can display this text in an output field, for example.   The assigned recipe tag must have the data type of a number. The tag value must be within the range of values of the text list.  Text lists with parameter fields are not permitted. |
| Default value | This is used as the default entry when you create a new recipe data record. |
| Minimum value [fixed] | The smallest representable value of a number-based recipe tag, depending on the type of data. |
| Maximum value [fixed] | The largest representable value of a number-based recipe tag, depending on the type of data. |
| Decimal places | Determines how many places a decimal number is rounded to, e.g. 3 decimal places and vice versa by what power of ten an integer value is multiplied, e.g. 1,000. |
| Tooltip | Tooltip about the recipe element which is shown to the operator in Runtime. |

#### Recipe data record settings

You can make the following settings on the "Data records" tab:

| Setting | Description |
| --- | --- |
| Name of the recipe data record | Identifies a recipe data record uniquely within the recipe. |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Assign meaningful names or product numbers which the operator can associate directly with a product, e.g. "yellow fruit juice E231". |
| Recipe data record number | Identifies a recipe data record uniquely within the recipe. |
| Recipe elements 1 to n | You can store various values for each recipe element even during configuration. Together with the values of the other recipe elements, a value always forms a recipe data record. You can store multiple recipe data records.  If enabled in the transfer settings, the recipe data records are transferred to the HMI device when downloading the project and existing data records on the HMI device are overwritten. |
| Comment | Comment about the recipe data record |

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)

## Recipes in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Recipe screen and recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-screen-and-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Advanced recipe view (prior to V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#advanced-recipe-view-prior-to-v13-basic-panels-panels-comfort-panels-rt-advanced)
- [Advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
- [Exporting and importing recipe data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#exporting-and-importing-recipe-data-basic-panels-panels-comfort-panels-rt-advanced)

### Recipe screen and recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics on the recipe screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-the-recipe-screen-basic-panels-panels-comfort-panels-rt-advanced)
- [Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)

#### Basics on the recipe screen (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The recipe screen contains an individual screen form for entering the recipes. The screen form contains I/O fields and other display and operator control objects. The recipe functionality is implemented with system functions, e.g. for saving recipe data records.

The picture below contains an example of a recipe screen:

![Introduction](images/72836363019_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Availability**
>
> Basic Panels do not support recipe screens.

##### Designing recipe screens

Configuring a recipe screen allows you to customize the display. You can spread large recipes over several screens according to topic and display them clearly using features such as graphical display and operator control objects.

- Spreading recipes over several screens according to topic

  - You can spread recipe data records containing lots of entries across several screens. For example, for each plant area you can configure a screen containing the associated screen forms for the recipe data records.

  Spreading recipes over several screens is useful for HMI devices with small displays as they avoid having to scroll through tables in Runtime.
- Visual machine simulation

  You can visually simulate your machine in a screen using graphical screen objects. This enables you to display parameter settings more clearly by positioning I/O fields immediately next to machine elements such as axes or guide rails. which produces a direct relationship between the values and the machine.

##### Synchronizing recipe values

To enter recipe data record values outside the advanced recipe view in the configured I/O fields, activate "Synchronize recipe view and recipe tags" under "Properties &gt; Synchronization" in the recipe properties.

The "Synchronize recipe view and recipe tags" option is not available for the simple recipe view.

![Recipes_Synchronization_Advanced](images/89645763851_DV_resource.Stream@PNG-en-US.png)

Recipes_Synchronization_Advanced

##### Transferring recipe values automatically

If the entered recipe values must be immediately transferred to the connected PLC in Runtime, deactivate "Manual transfer of individual modified values (teach-in mode)" under "Properties &gt; Options".

Configure the "SetRecipeTags" system function if you want to enable and disable the immediate transfer of entered recipe values in Runtime.

##### System functions

The system functions for loading, saving and transferring recipe data records and recipes are located in the "Recipes" group.

The following system functions are available for operator control of a recipe screen:

- ImportDataRecords
- ExportDataRecords
- LoadDataRecord
- GetDataRecordFromPLC
- ClearDataRecord
- SaveDataRecord
- SetDataRecordToPLC
- SetDataRecordTagsToPLC
- SetRecipeTags
- GetDataRecordTagsFromPLC

The following system functions are available for operator control of the recipe view when it is being used in the recipe screen:

- RecipeViewSaveDataRecord
- RecipeViewSaveAsDataRecord
- RecipeViewSynchronizeDataRecordWithTags
- RecipeViewClearDataRecord
- RecipeViewNewDataRecord
- RecipeViewGetDataRecordFromPLC
- RecipeViewSetDataRecordToPLC
- RecipeViewRenameDataRecord
- RecipeViewShowOperatorNotes
- RecipeViewMenu (for simple recipe view only)
- RecipeViewOpen (for simple recipe view only)
- RecipeViewBack (for simple recipe view only)

---

**See also**

[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### **Introduction**

The recipe view is a WinCC display and operating object. The recipe view is used to display, edit and manage data records.

The layout of the recipe views is dependent on the device and the device version.

**HMI devices with simple recipe view**

| HMI device | Type |
| --- | --- |
| Basic Panels | KP300 Basic mono PN  KP400 Basic color PN |
| KTP400 Basic mono PN  KTP400 Basic color PN  KTP400 Basic mono PN Portrait  KTP400 Basic color PN Portrait |  |
| KTP600 Basic |  |
| KTP1000 Basic |  |
| TP1500 Basic |  |
| <sup>1) </sup>The simple recipe view display can be changed to the advanced recipe view |  |

**HMI devices with advanced recipe view as of device version V13**

| HMI device | Type |
| --- | --- |
| Basic Panels | KTP400 Basic PN  KTP400 Basic PN Portrait |
| KTP700 Basic |  |
| KTP900 Basic |  |
| KTP1200 Basic |  |
| Comfort Panels | KP400 Comfort  KTP400 Comfort |
| KP700 Comfort  TP700 Comfort |  |
| KP900 Comfort  TP900 Comfort |  |
| KP1200 Comfort  TP1200 Comfort |  |
| KP1500 Comfort  TP1500 Comfort |  |
| TP1900 Comfort |  |
| TP2200 Comfort |  |
| Mobile Panels | KTP400F Mobile |
| KTP700 Mobile  KTP700F Mobile |  |
| KTP900 Mobile  KTP900F Mobile |  |

---

**See also**

[Basics on the recipe screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-the-recipe-screen-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuration options of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Using the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
- [Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#read-recipe-data-record-from-plc-basic-panels-panels-comfort-panels-rt-advanced)
- [Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-a-recipe-data-record-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced)

#### Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Recipe view

The simple recipe view is a display and operating object that is used to manage recipe data records. The recipe view shows recipe data records in tabular form.

The buttons and information displayed in the columns are adjustable.

The values displayed or entered in the recipe view are saved in recipe data records. The recipe data record displayed can be written to the PLC and values read in from the PLC using buttons.

##### Layout of the display

The simple recipe view consists of the following display areas:

- Recipe list
- Data record list
- Element list

This application is illustrated below:

![Layout of the display](images/7603695755_DV_resource.Stream@PNG-en-US.png)

In the simple recipe view, each area is shown separately on the HMI device. You can use the shortcut menu to operate each of these display areas.

The simple recipe view always begins with the recipe list.

##### Operation

You have the following options for using the simple recipe view, according to the configuration:

- Create, change, copy or delete recipe data records
- Read recipe data records from the PLC or transfer to the PLC

##### Using the display area and shortcut menu

Toggle between the display areas and the shortcut menus to operate the simple recipe views.

Operation of the display area

| Button | Key | Function |
| --- | --- | --- |
|  | &lt;Enter&gt; | The next lowest display area is opened, i.e. the data record list or the element list. |
| ![Using the display area and shortcut menu](images/7603115915_DV_resource.Stream@PNG-de-DE.png) | &lt;Esc&gt; | The previous display area opens. |
|  | &lt;INS&gt; | Creates a new data record for the selected recipe if the list of recipes or recipe data records is displayed. Then changes to the list of recipe element.  Requirement: "Properties &gt;General &gt; Processing mode" is activated.  The button can be simulated with the "Key SimulateSystemKey" function even on devices without keys. |
|  | &lt;DEL&gt; | Deletes the selected recipe data record in the list of recipe data records.  Requirement: "Properties &gt;General &gt; Processing mode" is activated. |
|  | &lt;Up&gt;/&lt;Down&gt; | Selects the previous/next entry. |
|  | &lt;Pg Up&gt;/&lt;Pg Down&gt; | Moves the display up or down one page. |
|  | &lt;Home&gt;/&lt;End&gt; | Selects the first/last entry. The first/last entry is selected. |

Operation of the shortcut menu

| Button | Key | Function |
| --- | --- | --- |
| ![Using the display area and shortcut menu](images/7603316235_DV_resource.Stream@PNG-de-DE.png) | &lt;Right&gt; | The shortcut menu of the display area opens. |
| ![Using the display area and shortcut menu](images/7603115915_DV_resource.Stream@PNG-de-DE.png) | &lt;Esc&gt; | The menu is closed.  The display area opens. |
|  | Input of the number of the menu command | The menu command is executed. |

##### Shortcut menus of the simple recipe view

You can click the ![Shortcut menus of the simple recipe view](images/7603316235_DV_resource.Stream@PNG-de-DE.png) button in each display area to call up a selection of commands. The command selection lists those commands that are available in the current display area. A number is assigned to each command. The command is executed when you enter this number. Alternatively select the command and press the &lt;Return&gt; key.

##### Shortcut menus in the recipe list

| Menu command | Function |
| --- | --- |
| New | A new recipe data record is created for the selected recipe. If a start value is configured, it is displayed in the input field. |
| Display tooltip | The tooltip configured for the recipe is displayed. |
| Open | The record list of the selected recipe opens. |

##### Shortcut menus of the recipe data record list

| Menu command | Function |
| --- | --- |
| New | Creates a new recipe data record. If a start value is configured, it is shown in the input field. |
| Delete | The displayed record is deleted. |
| Save as | The selected data record is saved under a different name. A dialog box opens where you can enter the name. |
| Rename | Renames the selected data record. A dialog box opens where you can enter the name. |
| Open | The element list of the selected data record opens. |
| Previous | The recipe list opens. |

##### Shortcut menus of the recipe element list

| Menu command | Function |
| --- | --- |
| Save | The selected data record with the recipe element is saved. |
| To PLC | The displayed values of the selected data record are transferred from the HMI device to the PLC. |
| From PLC | The recipe values from the PLC are displayed in the recipe view of the HMI device. |
| Save as | The data record is saved under a new name. A dialog box opens where you can enter the name. |
| Display tooltip | The tooltip configured for the recipe element is displayed. |
| Rename | The selected recipe element is renamed. A dialog box opens where you can enter the name. |
| Previous | The data record list opens. |

##### Shortcut menus in the data record list

> **Note**
>
> **HMI device dependency**
>
> The following menu commands are configured in Basic Panels.

| Menu command | Function |
| --- | --- |
| To PLC | The displayed values of the selected data record are transferred from the HMI device to the PLC. |
| From PLC | The recipe values from the PLC are displayed in the recipe view of the HMI device. |

##### Updating and displaying values

> **Note**
>
> **Processed recipe data record is changed in the background**
>
> Only applies for Basic Panels: If an operator has changed a recipe data record and a PLC job wants to read or write any recipe data record of this recipe, the PLC job is stopped and a system alarm is output. On the other hand, the changed value is displayed immediately if only the PLC job and no operator has changed recipe data.
>
> Does not apply for Basic Panels: If an operator has changed a recipe data record and a PLC job has changed values of the recipe data record concerned, the recipe view is not updated automatically. To update the recipe view, reselect the relevant recipe data record.

---

**See also**

[Using the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-a-recipe-data-record-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#read-recipe-data-record-from-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration options of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuration options of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

The response of the simple recipe view can be defined in the recipe view inspector window. Some devices, for example basic panels, only support the simple recipe view.

Please note the following for devices with a simple recipe view:

1. In the Inspector window, under "Properties &gt; Display &gt; Mode", select "Simple view" as "View type".
2. The "Properties &gt; Simple view" area contains additional properties only applicable to the simple recipe view.
3. All other properties are also applicable to the advanced recipe view.

##### Displaying recipe data record values only

To display the recipe data in a recipe view for checking only, proceed as follows:

1. Deselect "Edit mode" in the "General" group.

   ![Displaying recipe data record values only](images/111894363147_DV_resource.Stream@PNG-en-US.png)

You cannot create, rename, edit or delete recipe data.

##### Writing a recipe data record number or name to a tag

A tag to each recipe data record can be configured in the advanced recipe view. Depending on the "String" or "Int" data type of the tag, the name or number of the recipe data record is stored in the tag. Conversely, the tag can also be used to select a recipe data record by entering the corresponding value. For example, the tag can be transferred as a parameter for a system function.

Follow these steps:

1. Enter a tag of the "Int" type in the field "Tag", under "Properties &gt; General &gt; Recipe data record".

The number of the recipe data record is stored in a tag.

##### Configuring an event on the recipe view

> **Note**
>
> **Events and buttons**
>
> The "Events" register is faded out when a minimum of one button is enabled.

To configure an event on the recipe view, follow these steps:

1. Select the recipe view that was added to the screen in the "Screens" editor.

   The properties of the recipe view are displayed in the Inspector window.
2. Deactivate all buttons under "Properties &gt; Toolbar" and "Properties &gt; Simple view".
3. In the Inspector window, under "Properties &gt; Events", click the event to be configured, e.g. "Enable".
4. Configure a function list for the event.

The function list is processed when the operator enables the recipe view.

##### Animation properties of the recipe view

To configure an animation of a recipe view, proceed as follows:

1. Select the recipe view that was added to the screen in the "Screens" editor.

   The properties of the recipe view are displayed in the Inspector window.
2. Click under "Properties &gt; Animations" in the Inspector window.

   ![Animation properties of the recipe view](images/72836830219_DV_resource.Stream@PNG-en-US.png)
3. Link a tag to one or more of the following properties.

   - X-Position and y-Position
   - Design: Colors, flashing
   - Operability
   - Visibility

     In the "Animations&gt; Overview" area, all animations are summarized in tabular form. Under "Animations&gt; Tag links &gt; Tag linkage", as well as visibility and position a tag can also be linked to height and width.

     > **Note**
     >
     > **Animations and buttons**
     >
     > If all buttons are not disabled, an error message appears whilst compiling the project for windows-CE HMI devices.

##### Constraints on the simple recipe view

The following functions are not possible in the simple recipe view:

- Synchronizing recipe view and recipe tags
- Writing a recipe number / name to a tag
- Display status bar
- Display data record number
- Display label
- Display table

---

**See also**

[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Using the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Controlling the simple recipe view with mouse or touchpad

To control the simple recipe view with mouse or touchpad, proceed as follows:

1. Select the desired recipe from the recipe view.
2. Click the ![Controlling the simple recipe view with mouse or touchpad](images/7603316235_DV_resource.Stream@PNG-de-DE.png)button.

   The shortcut menu is opened.
3. Select the desired menu command.

   The menu command is executed.

##### Controlling the simple recipe view with the keyboard

To control the simple recipe view with the keyboard, proceed as follows:

1. Press the &lt;Tab&gt; key until the simple recipe view is selected.
2. Select the desired recipe with the cursor keys.
3. Press &lt;Right&gt;.

   The shortcut menu is opened.
4. Press the &lt;Down&gt; key until the desired menu command is selected.
5. Press &lt;Enter&gt; to confirm the command.

##### Key shortcuts for the simple recipe view

The following key shortcuts are activated for the simple recipe view in Runtime if "Activate keyboard operation" is enabled in the ES.

| Key shortcut | Effect | Menu command |
| --- | --- | --- |
| &lt;Insert&gt; | Generates a new recipe data record | New |
| &lt;Del&gt; | Deletes the recipe data record displayed. | Delete |

##### Operating the recipe view with function keys

The recipe view can be operated with function keys, for example if the HMI device does not have touch functionality. You can assign functions such as "SaveDataRecord" to the function keys on the HMI device.

---

**See also**

[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Administration of recipe data records

You have the following options for managing the simple recipe view, according to the configuration:

- Creating new recipe data records
- Copy recipe data records
- Edit recipe data records
- Delete recipe data records

##### Creating new recipe data records

To create a new recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to create a new recipe data record.
2. Select the "New" command from the shortcut menu for the recipe list.

   A new data record with the next available number will be created.

   The element list of the new recipe data record opens.
3. Enter values for the elements of the recipe data record.

   The configuration data may already contain default values for the recipe data record.
4. Select the "Save" command from the shortcut menu for the element list.

   The dialog "Save as" opens.
5. Enter the name and number of the recipe data record.
6. Click the "OK" button.

   The data record is saved under the new name.

   If the recipe data record already exists, a dialog is opened. In this dialog, specify whether the existing data record is to be overwritten.

##### Copying a recipe data record

To copy a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to copy an existing recipe data record.
2. On the HMI device, select the recipe data record of which you want to save a copy.
3. Select the "Save As" command from the shortcut menu for the data record list.

   The dialog "Save as" opens. The recipe data record is automatically given the next free recipe data record number.
4. Under name, enter the name of the record.
5. Click the "OK" button.

##### Modifying a recipe data record

To change a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to edit an existing recipe data record.
2. Select the recipe data record that you want to edit on the HMI device.
3. Select the recipe data record.

   The element list of the recipe data record is displayed.
4. Replace the old values with new ones.
5. Select the "Save" command from the shortcut menu for the element list.

##### Deleting a recipe data record

To delete a recipe data record, proceed as follows:

1. Select the recipe on the HMI device from which you want to delete an existing recipe data record.
2. Select the recipe data record that you want to delete on the HMI device.
3. Select the "Delete" command from the shortcut menu for the data record list.
4. Confirm this security prompt to delete the data record.

---

**See also**

[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In Runtime, you can change values directly in the plant that are also stored in recipes in the HMI device. This applies if a valve was opened further directly in the plant than was specified in the recipe. The values of the recipe data records saved in the HMI device possibly no longer match the values in the PLC.

You can read the values of the recipe tags from the PLC and write them to a recipe data record.

The read values are written to the recipe data record that is currently displayed on the HMI device.

##### Procedure

To read a recipe data record from the PLC, proceed as follows:

1. Open the recipe on the HMI device.

   The data record list opens.
2. Select the element list of the recipe data record to which you want to apply the values from the PLC.
3. Select the "From PLC" command from the shortcut menu for the element list.

   The values are read from the PLC and displayed in the current recipe data record.
4. If you want to save the values, select the "Save" or "Save As" command.

##### Result

The values are read from the PLC, visualized on the HMI device and saved to the recipe data record.

> **Note**
>
> **Basic Panels**
>
> With Basic Panels, the "From PLC" menu command can also be configured for the data record list. In this case, you can also select the "From PLC" menu command in the data record list.

---

**See also**

[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For the values of a data record that was changed in the recipe view to take effect, you must transfer the values to the PLC.

The values displayed in the recipe view are always transferred to the PLC.

##### Procedure

To transfer a recipe data record to the PLC, proceed as follows:

1. Open the recipe you want to use.

   The data record list opens.
2. Select the element list of the recipe data record whose values you want to transfer to the PLC.
3. Select the "To PLC" command from the shortcut menu for the element list.

##### Result

The values of the recipe data record are transferred to the PLC.

> **Note**
>
> **Basic Panels**
>
> With Basic Panels, the "From PLC" menu command can also be configured for the data record list. In this case, you can also select the "From PLC" menu command in the data record list.

---

**See also**

[Description of the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Advanced recipe view (prior to V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
- [Configuration options of the advanced recipe view (Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
- [Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-advanced-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-1)
- [Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronizing-recipe-data-record-basic-panels-panels-comfort-panels-rt-advanced)
- [Reading recipe data records from the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#reading-recipe-data-records-from-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
- [Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-a-recipe-data-record-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced-1)

#### Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)

##### Recipe view

The advanced recipe view is a display and operating object that is used to manage recipe data records. The recipe view shows recipe data records in tabular form.

The buttons, headers and information displayed in the columns can be set.

The values displayed or entered in the recipe view are saved in recipe data records.

The layout of the recipe views is dependent on the device and the device version.

##### Application

The recipe view is used to display, edit and manage data records.

##### Layout of the display

The figure below shows an example of the advanced recipe view on an HMI device prior to device version V13.

![Layout of the display](images/72837113483_DV_resource.Stream@PNG-en-US.png)

##### Operation

Depending on the configuration you can:

- Create, edit, copy or delete recipe data records
- Read recipe data records from or transfer to the PLC
- Synchronize recipe data records with the associated recipe tags

##### Operating elements

The following operating elements can be configured in the recipe view:

| Operating object | Key combination | Function |
| --- | --- | --- |
| ![Operating elements](images/14829503371_DV_resource.Stream@PNG-de-DE.png) |  | The configured tooltip is displayed. |
| ![Operating elements](images/72283805323_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Spacebar&gt; | Creates a new recipe data record. If a start value is configured, it is shown in the input field. |
| ![Operating elements](images/72283874187_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Enter&gt; | Saves the displayed values of the recipe data record. The storage location is predefined by the project. |
| ![Operating elements](images/72283908619_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+*&gt; | The recipe data record is saved under a different name regardless of the recipe view. A dialog box opens where you can enter the name. |
| ![Operating elements](images/72283591691_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Del&gt; | Deletes the recipe data record displayed. |
| ![Operating elements](images/72283981451_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+=&gt; | The system always updates the current value of the recipe view with the up-to-date recipe tag value.  When the value shown in the recipe view is more recent than the current recipe tag value, the system writes this value to the recipe tag.  "Synchronize recipe view and recipe tags" must be activated in the recipe properties before this function can be used. |
| ![Operating elements](images/72283582859_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Down Arrow&gt; | The values of the set recipe data record displayed in the recipe view are transferred to the PLC. |
| ![Operating elements](images/72283865355_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Up Arrow&gt; | The recipe values from the PLC are displayed in the recipe view. |

##### Updating and displaying values

If values of the corresponding recipe data record are changed by a job mailbox, the recipe view is not updated automatically. The values are changed in the background. To update the recipe view, reselect the relevant recipe data record.

---

**See also**

[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-advanced-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronizing-recipe-data-record-basic-panels-panels-comfort-panels-rt-advanced)
  
[Reading recipe data records from the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#reading-recipe-data-records-from-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-a-recipe-data-record-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Configuration options of the advanced recipe view (Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuration options of the advanced recipe view (Panels, Comfort Panels, RT Advanced)

You can specify the behavior of the advanced recipe view in the Inspector window of the recipe view.

The layout of the recipe views is dependent on the device and the device version.

Please note the following for devices with an advanced recipe view:

1. In the Inspector window under "Properties &gt; Display &gt; Mode", select "Advanced view" as the "View type".
2. The "Properties &gt; Simple view" area contains properties only applicable to the simple recipe view.
3. All other properties apply to the advanced recipe view.

##### Displaying a recipe

To only allow access to the recipe data records of a specific recipe in a screen, follow these steps:

1. Enter the required recipe or select an existing recipe in the "Recipe" field under "Properties &gt; General".
2. When a recipe is entered in the "Recipe" field, you will have to enable the "Selection list" if you want to display the recipe name in runtime.

   ![Displaying a recipe](images/88397431179_DV_resource.Stream@PNG-en-US.png)

The selected recipe appears in the recipe view.

##### Writing a recipe number or name and recipe data record number or name to a tag

Both the recipe and the recipe data record can each be configured to a tag in the recipe view. Depending on the "String" or "Int" data type of the tag, the name or number of the recipe or recipe data record is stored in the tag. Conversely, the tag can be used to select the recipe or recipe data record by entering the corresponding value. For example, the tag can be transferred as a parameter for a system function.

Follow these steps:

1. Enter a tag of the "String" type in the field "Recipe tag", under "Properties &gt; General &gt; Recipe".
2. Enter a tag of the "Int" type in the field "Tag", under "Properties &gt; General &gt; Recipe data record".

The name of the recipe and the number of the recipe data record are each stored in a tag.

##### Using the recipe view as a drop-down list

To use the recipe view as a selection field for recipes and recipe data records in a recipe screen, follow these steps:

1. Select the tag for the recipe name under "General &gt; Recipe &gt; Recipe tag".
2. Select the tag for the recipe data record name under "General &gt; Recipe data record &gt;Tag".
3. Disable the "Editing mode". You cannot create, rename, edit or delete recipe data.
4. In order to select recipes, enable "Display selection list" and make sure that no recipe is selected under "Properties &gt; General &gt; Recipe".
5. Deactivate all buttons under "Properties &gt; Toolbar".

   ![Using the recipe view as a drop-down list](images/88396456715_DV_resource.Stream@PNG-en-US.png)

##### Configuring an event on the recipe view

To configure an event on the recipe view, follow these steps:

1. Select the recipe view that was added to the screen in the "Screens" editor.

   The properties of the recipe view are displayed in the Inspector window.
2. In the Inspector window, click the event you want to configure under "Properties &gt; Events".
3. Configure a function list for the selected event.   
   The function list is processed when the configured event occurs.

---

**See also**

[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can control the recipe view using both mouse or touchpad or with the keyboard.

The layout of the recipe views is dependent on the device and the device version.

##### Controlling the recipe view with mouse or touchpad

To control the recipe view with mouse or touchpad, proceed as follows:

1. Select the recipe you want to use.

   The records for the recipe are displayed.
2. Click on the data record you wish to edit.
3. Click the button whose function you want to run.

##### Controlling the recipe view with the keyboard

To control the recipe view with the keyboard, proceed as follows:

1. Press the &lt;Tab&gt; key until the cursor reaches the field for selecting the recipe.
2. Press &lt;Enter&gt;.

   The drop-down list box for the recipes opens.
3. Select a recipe. You navigate between the next or previous entry in the list by using the cursor keys &lt;Left&gt;, &lt;Right&gt;, &lt;Up&gt; and &lt;Down&gt;.
4. Select a data record.
5. Press the &lt;Tab&gt; key until the operator control object you wish to use is selected.

Alternatively you can control the recipe view using certain key combinations.

##### Operating the recipe view with function keys

The recipe view can be operated with function keys, for example if the HMI device does not have touch functionality. You can assign functions such as "SaveDataRecord" to the function keys on the HMI device.

##### Key shortcuts for the advanced recipe view

The following key shortcuts are activated for the advanced recipe view in Runtime if "Activate keyboard operation" is enabled in the ES.

| Keys  shortcut | Effect | Menu command | Button |
| --- | --- | --- | --- |
| &lt;HELP&gt; | Calls up the configured tooltip for the selected recipe. | Tooltip | ![Key shortcuts for the advanced recipe view](images/14829503371_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Spacebar&gt; | Generates a new recipe data record. Any configured start value is displayed in the input field. | Add data record | ![Key shortcuts for the advanced recipe view](images/72283805323_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Enter&gt; | Saves the modified record with its current name. | Save | ![Key shortcuts for the advanced recipe view](images/72283874187_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+*&gt; | Saves the modified record with a new name. | Save as | ![Key shortcuts for the advanced recipe view](images/72283908619_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Del&gt; | Deletes the recipe data record displayed. | Delete data record | ![Key shortcuts for the advanced recipe view](images/72283591691_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+=&gt; | Compares the values of the selected data record with the values on the PLC.  Any value in the recipe view which is more recent compared to the current recipe tag value is written to the recipe tag. | Synchronize recipe tags | ![Key shortcuts for the advanced recipe view](images/72283981451_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Down Arrow&gt; | Sends the current value to the PLC. | Write to PLC | ![Key shortcuts for the advanced recipe view](images/72283582859_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Up Arrow&gt; | Reads the current value from the PLC. | Read from PLC | ![Key shortcuts for the advanced recipe view](images/72283865355_DV_resource.Stream@PNG-de-DE.png) |

##### Screen change

If you change to another screen and have not yet saved changes to the recipe data in the recipe view, you will be prompted to save the recipe data. The recipe name and the name of the recipe data record are displayed to show which recipe data have not been saved yet.

---

**See also**

[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Administration of recipe data records

You have the following options for managing recipe data records, according to the configuration:

- Creating new recipe data records
- Copy recipe data records
- Edit recipe data records
- Delete recipe data records

##### Creating new recipe data records

To create a new recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to create a new recipe data record.
2. Click ![Creating new recipe data records](images/72283805323_DV_resource.Stream@PNG-de-DE.png) or press &lt;Ctrl+Spacebar&gt;.

   A new recipe data record with the next available number is created.

   If you change the new data record number to an existing data record number, the existing data record is overwritten.
3. Enter values for the elements of the data record.

   The elements of the recipe data record can be assigned default values depending on the configuration.
4. Click ![Creating new recipe data records](images/72283908619_DV_resource.Stream@PNG-de-DE.png) or press &lt;Ctrl+*&gt;.

   The dialog "Save as" opens.
5. Enter a name for the data record.
6. Click "OK" to confirm your input.

   The data record is saved under the new name.

   If the recipe data record already exists, a dialog is opened. In this dialog, specify whether the existing data record is to be overwritten.

##### Copying a recipe data record

To copy a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to copy an existing recipe data record.
2. Select the recipe data record that you want to copy on the HMI device.
3. Click ![Copying a recipe data record](images/72283908619_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+*&gt;.

   The dialog "Save as" opens.
4. Enter a name for the data record.
5. Click "OK" to confirm your input.

##### Modifying a recipe data record

To change a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to edit an existing recipe data record.
2. Select the recipe data record that you want to edit on the HMI device.
3. Replace the old values with new ones.
4. Click ![Modifying a recipe data record](images/72283874187_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Enter&gt;.

##### Deleting a recipe data record

To delete a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to delete an existing recipe data record.
2. Select the recipe data record that you want to delete on the HMI device.
3. Click ![Deleting a recipe data record](images/72283591691_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Del&gt;.

---

**See also**

[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Differences between the following values may occur during runtime:

- The values displayed in the recipe view
- The actual values of the recipe tags

Depending on the configuration, the values displayed in the recipe view are synchronized with the recipe tags. Synchronization encompasses all tags of a recipe data record.

> **Note**
>
> **Changed tag name**
>
> The tag and the value of the recipe data record cannot be associated if you have renamed the tag you want to synchronize. The tags in question are not synchronized.

> **Note**
>
> Recipe tags can only be synchronized in the advanced recipe view.

##### Requirement

- A recipe data record is displayed in the recipe view.
- The values of recipe tags were modified by teaching, for example.

##### Procedure

To synchronize a recipe data record, proceed as follows:

- Click ![Procedure](images/72283981451_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+=&gt;.

The system always updates the current value of the recipe view with the up-to-date recipe tag value.

When the value shown in the recipe view is more recent than the current recipe tag value, the system writes this value to the recipe tag.

---

**See also**

[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Reading recipe data records from the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In runtime, you can change values directly in the plant that are also stored in recipes in the HMI device. This applies for example if a valve was opened right at the plant wider than specified in the recipe. The values of the recipe data records saved in the HMI device may then possibly no longer match the values in the PLC.

You can read the values of the recipe tags from the PLC and write them to a recipe data record.

The values read are written to the recipe data record that is currently displayed on the HMI device.

##### Procedure

Proceed as follows to read a recipe data record from the PLC:

1. Select the recipe on the HMI device.
2. On the HMI device, select the recipe data record whose values you want to read from the PLC.
3. Click ![Procedure](images/72283865355_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Up Arrow&gt;.

---

**See also**

[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Transferring a recipe data record to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For the values of a data record that was changed in the recipe view to take effect, you must transfer the values to the PLC.

The values displayed in the recipe view are always transferred to the PLC.

##### Procedure

Proceed as follows to transfer a recipe data record to the PLC:

1. Select the recipe on the HMI device.
2. On the HMI device, select the recipe data record whose values you want to transfer to the PLC.
3. Click ![Procedure](images/72283582859_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Down Arrow&gt;.

---

**See also**

[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuration options of the advanced recipe view (V13 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-advanced-recipe-view-v13-or-higher-basic-panels-panels-comfort-panels-rt-advanced)
- [Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-advanced-recipe-view-basic-panels-panels-comfort-panels-rt-advanced-1)
- [Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-2)
- [Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronizing-recipe-data-record-basic-panels-panels-comfort-panels-rt-advanced-1)
- [Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#read-recipe-data-record-from-plc-basic-panels-panels-comfort-panels-rt-advanced-1)
- [Transferring recipe data records to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced)

#### Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The advanced recipe view is a display and operating object that is used to manage recipe data records. The recipe view shows recipe data records in tabular form.

The buttons, headers and information displayed in the columns can be set.

The values displayed or entered in the recipe view are saved in recipe data records.

The layout of the recipe views is dependent on the device and the device version.

##### Application

The recipe view is used to display, edit and manage data records.

##### **Layout of the display**

The figure below shows an example of the advanced recipe view on an HMI device, device version V13 or later.

![Layout of the display](images/74777852811_DV_resource.Stream@PNG-en-US.png)

##### Operation

Depending on the configuration you can:

- Create, edit, copy or delete recipe data records
- Read recipe data records from or transfer to the PLC
- Synchronize recipe data records with the associated recipe tags

##### Operator controls

The following operating elements can be configured in the recipe view:

| Operator controls | Keyboard shortcut | Function |
| --- | --- | --- |
| ![Operator controls](images/72271575691_DV_resource.Stream@PNG-de-DE.png) | &lt;HELP&gt; | The configured tooltip is displayed. |
| ![Operator controls](images/72273232139_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Spacebar&gt; | Creates a new recipe data record. If a start value is configured, it is shown in the input field. |
| ![Operator controls](images/72273238539_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Enter&gt; | Saves the displayed values of the recipe data record. The storage location is predefined by the project. |
| ![Operator controls](images/72273267979_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+*&gt; | The recipe data record is saved under a different name regardless of the recipe view. A dialog box opens where you can enter the name. |
| ![Operator controls](images/72273271819_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Del&gt; | Deletes the recipe data record displayed. |
| ![Operator controls](images/68659792523_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Shift+T&gt; | The selected recipe data record is renamed. A dialog box opens where you can enter the name. |
| ![Operator controls](images/72273275659_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+=&gt; | If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is activated, the following applies:    - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view. - If the value displayed in the recipe view is more recent than the value of the tag, this value is transferred to the tag. Synchronization only takes place within the HMI device.   In this case, the process tag named above as an example in the I/O field is not automatically read from the PLC. <sup>1)</sup>    If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is deactivated, the following applies:    - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view. - If the value shown in the recipe view is more recent than the value of the tag, this value is transferred to the tag.   Synchronization with the PLC also takes place.<sup> 2)</sup> |
| ![Operator controls](images/72273292299_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Down Arrow&gt; | The values of the set recipe data record displayed in the recipe view are transferred to the PLC. |
| ![Operator controls](images/72273296139_DV_resource.Stream@PNG-de-DE.png) | &lt;Ctrl+Up Arrow&gt; | The recipe values from the PLC are displayed in the recipe view. |

1) For the recipe, the options "Synchronize recipe tags" and "Manual transfer of individually modified values (teach-in mode)" are activated under "General &gt; Synchronization &gt; Settings".

2) For the recipe, the option "Synchronize recipe tags" is activated under "General &gt; Synchronization &gt; Settings" and the option "Manual transfer of individually modified values (teach-in mode)" is deactivated.

##### Updating and displaying values

If values of the corresponding recipe data record are changed by a job mailbox, the recipe view is not updated automatically. The values are changed in the background. To update the recipe view, reselect the relevant recipe data record.

---

**See also**

[Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-advanced-recipe-view-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced-2)
  
[Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronizing-recipe-data-record-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#read-recipe-data-record-from-plc-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Transferring recipe data records to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration options of the advanced recipe view (V13 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-advanced-recipe-view-v13-or-higher-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuration options of the advanced recipe view (V13 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced)

You can specify the behavior of the advanced recipe view in the Inspector window of the recipe view.

##### Displaying a recipe

To only allow access to the recipe data records of a specific recipe in a screen, follow these steps:

1. Enter the required recipe or select an existing recipe in the "Recipe" field under "Properties &gt; General".
2. When a recipe is entered in the "Recipe" field, you will have to enable the "Selection list" if you want to display the recipe name in runtime.

![Displaying a recipe](images/69349913227_DV_resource.Stream@PNG-en-US.png)

The selected recipe appears in the recipe view.

##### Writing a recipe number or name and recipe data record number or name to a tag

Both the recipe and the recipe data record can each be configured to a tag in the recipe view. Depending on the "String" or "Int" data type of the tag, the name or number of the recipe or recipe data record is stored in the tag. Conversely, the tag can be used to select the recipe or recipe data record by entering the corresponding value. For example, the tag can be transferred as a parameter for a system function.

Follow these steps:

1. Enter a tag of the "String" type in the field "Recipe tag", under "Properties &gt; General &gt; Recipe".
2. Enter a tag of the "Int" type in the field "Tag", under "Properties &gt; General &gt; Recipe data record".

The name of the recipe and the number of the recipe data record are each stored in a tag.

##### Using the recipe view as a drop-down list

To use the recipe view as a selection field for recipes and recipe data records in a recipe screen, follow these steps:

1. Select the tag for the recipe name under "General &gt; Recipe &gt; Recipe tag".
2. Select the tag for the recipe data record name under "General &gt; Recipe data record &gt;Tag".
3. Disable the "Editing mode". You cannot create, rename, edit or delete recipe data.
4. In order to select recipes, enable "Display selection list" and make sure that no recipe is selected under "Properties &gt; General &gt; Recipe".
5. Deactivate all buttons under "Properties &gt; Toolbar".

![Using the recipe view as a drop-down list](images/88398124043_DV_resource.Stream@PNG-en-US.png)

##### Configuring an event on the recipe view

To configure an event on the recipe view, follow these steps:

1. Select the recipe view that was added to the screen in the "Screens" editor.

   The properties of the recipe view are displayed in the Inspector window.
2. In the Inspector window, click the event you want to configure under "Properties &gt; Events".
3. Configure a function list for the selected event.   
   The function list is processed when the configured event occurs.

---

**See also**

[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Using the advanced recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can control the recipe view using both mouse or touchpad or with the keyboard.

##### Controlling the recipe view with mouse or touchpad

To control the recipe view with mouse or touchpad, proceed as follows:

1. Select the recipe you want to use.

   The records for the recipe are displayed.
2. Click on the data record you wish to edit.
3. Click the button whose function you want to run.

##### Controlling the recipe view with the keyboard

To control the recipe view with the keyboard, proceed as follows:

1. Press the &lt;Tab&gt; key until the cursor reaches the field for selecting the recipe.
2. Press &lt;Enter&gt;.

   The drop-down list box for the recipes opens.
3. Select a recipe. You navigate between the next or previous entry in the list by using the cursor keys &lt;Left&gt;, &lt;Right&gt;, &lt;Up&gt; and &lt;Down&gt;.
4. Select a data record.
5. Press the &lt;Tab&gt; key until the operator control object you wish to use is selected.

Alternatively you can control the recipe view using certain key combinations.

##### Operating the recipe view with function keys

The recipe view can be operated with function keys, for example if the HMI device does not have touch functionality. You can assign functions such as "SaveDataRecord" to the function keys on the HMI device.

##### Key shortcuts for the advanced recipe view

The following key shortcuts are activated for the advanced recipe view in Runtime if "Activate keyboard operation" is enabled in the ES.

| Keys  shortcut | Effect | Menu command | Button |
| --- | --- | --- | --- |
| &lt;HELP&gt; | Calls up the configured tooltip for the selected recipe. | Tooltip | ![Key shortcuts for the advanced recipe view](images/72271575691_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Spacebar&gt; | Generates a new recipe data record. Any configured start value is displayed in the input field. | Add data record | ![Key shortcuts for the advanced recipe view](images/72274020747_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Enter&gt; | Saves the modified record with its current name. | Save | ![Key shortcuts for the advanced recipe view](images/72274036363_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+*&gt; | Saves the modified record with a new name. | Save as | ![Key shortcuts for the advanced recipe view](images/72274044427_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Del&gt; | Deletes the recipe data record displayed. | Delete data record | ![Key shortcuts for the advanced recipe view](images/72274028555_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Shift+T&gt; | Changes the name of selected data record. | Rename data record | ![Key shortcuts for the advanced recipe view](images/68659792523_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+=&gt; | If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is activated, the following applies:    - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view. - If the value displayed in the recipe view is more recent than the value of the tag, this value is transferred to the tag. Synchronization only takes place within the HMI device.   In this case, the process tag named above as an example in the I/O field is not automatically read from the PLC. <sup>1)</sup>    If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is deactivated, the following applies:    - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view. - If the value shown in the recipe view is more recent than the value of the tag, this value is transferred to the tag.   Synchronization with the PLC also takes place.<sup> 2)</sup> | Synchronizing recipe view and recipe tags | ![Key shortcuts for the advanced recipe view](images/72274052235_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Down Arrow&gt; | Sends the current value to the PLC. | Write to PLC | ![Key shortcuts for the advanced recipe view](images/72274111243_DV_resource.Stream@PNG-de-DE.png) |
| &lt;Ctrl+Up Arrow&gt; | Reads the current value from the PLC. | Read from PLC | ![Key shortcuts for the advanced recipe view](images/72274119051_DV_resource.Stream@PNG-de-DE.png) |

1) For the recipe, the options "Synchronize recipe tags" and "Manual transfer of individually modified values (teach-in mode)" are activated under "General &gt; Synchronization &gt; Settings".

2) For the recipe, the option "Synchronize recipe tags" is activated under "General &gt; Synchronization &gt; Settings" and the option "Manual transfer of individually modified values (teach-in mode)" is deactivated.

##### Screen change

If you change to another screen and have not yet saved changes to the recipe data in the recipe view, you will be prompted to save the recipe data. The recipe name and the name of the recipe data record are displayed to show which recipe data have not been saved yet.

---

**See also**

[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Administration of recipe data records

You have the following options for managing recipe data records, according to the configuration:

- Creating new recipe data records
- Copy recipe data records
- Edit recipe data records
- Delete recipe data records
- Rename recipe data records

##### Creating new recipe data records

To create a new recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to create a new recipe data record.
2. Click ![Creating new recipe data records](images/72274215307_DV_resource.Stream@PNG-de-DE.png) or press &lt;Ctrl+Spacebar&gt;.

   A new recipe data record with the next available number is created.

   If you change the new data record number to an existing data record number, the existing data record is overwritten.
3. Enter values for the elements of the data record.

   The elements of the recipe data record can be assigned default values depending on the configuration.
4. Enter a name for the data record.
5. Click on the ![Creating new recipe data records](images/72274222987_DV_resource.Stream@PNG-de-DE.png) button or press the keyboard shortcut &lt;Ctrl+Enter&gt;.

   Alternatively, click on the ![Creating new recipe data records](images/72274219147_DV_resource.Stream@PNG-de-DE.png) button or press the keyboard shortcut &lt;Ctrl+*&gt; to save the data record.

   The dialog "Save as" opens. Enter the name for the data record and confirm your entries with "OK".
6. The data record is saved under the new name.

   If the recipe data record already exists, a dialog is opened. In this dialog, specify whether the existing data record is to be overwritten.

##### Copying a recipe data record

To copy a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to copy an existing recipe data record.
2. Select the recipe data record that you want to copy on the HMI device.
3. Click ![Copying a recipe data record](images/72274219147_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+*&gt;.

   The dialog "Save as" opens.
4. Enter a name for the data record.
5. Click "OK" to confirm your input.

> **Note**
>
> When you use the "Save as …" function, the system assigns the recipe data record number automatically.
>
> A user-defined recipe data record number can only be assigned if a new recipe data record is created.

##### Modifying a recipe data record

To change a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to edit an existing recipe data record.
2. Select the recipe data record that you want to edit on the HMI device.
3. Replace the old values with new ones.
4. Click ![Modifying a recipe data record](images/72274222987_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Enter&gt;.

##### Deleting a recipe data record

To delete a recipe data record, proceed as follows:

1. Select the recipe on the HMI device in which you want to delete an existing recipe data record.
2. Select the recipe data record that you want to delete on the HMI device.
3. Click ![Deleting a recipe data record](images/72274226827_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Del&gt;.

##### Renaming recipe data records

Proceed as follows to rename a recipe data record:

1. Select the recipe on the HMI device in which you want to rename an existing recipe data record.
2. Select the recipe data record that you want to rename on the HMI device.
3. Click ![Renaming recipe data records](images/68659792523_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Shift+T&gt;.
4. Enter a new name in the dialog window.

---

**See also**

[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Synchronizing recipe data record (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Differences between the following values may occur during runtime:

- The values displayed in the recipe view
- The actual values of the recipe tags

Depending on the configuration, the values displayed in the recipe view are synchronized with the recipe tags. Synchronization encompasses all tags of a recipe data record.

> **Note**
>
> **Changed tag name**
>
> The tag and the value of the recipe data record cannot be associated if you have renamed the tag you want to synchronize. The tags in question are not synchronized.

> **Note**
>
> Recipe tags can only be synchronized in the advanced recipe view.

##### Requirement

- A recipe data record is displayed in the recipe view.
- The values of recipe tags were modified by teaching, for example.

##### Procedure

To synchronize a recipe data record, proceed as follows:

- Click ![Procedure](images/72274320395_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+=&gt;.

##### Result

The result depends on your settings:

- For the recipe, the options "Synchronize recipe tags" and "Manual transfer of individually modified values (teach-in mode)" are activated under "General &gt; Synchronization &gt; Settings".

  If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is activated, the following applies:

  - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view.
  - If the value displayed in the recipe view is more recent than the value of the tag, this value is transferred to the tag. Synchronization only takes place within the HMI device.

  In this case, the process tag named above as an example in the I/O field is not automatically read from the PLC.
- For the recipe, the option "Synchronize recipe tags" is activated under "General &gt; Synchronization &gt; Settings" and the option "Manual transfer of individually modified values (teach-in mode)" is deactivated.

  If tags on the HMI device are used in a recipe and at an additional point in the configuration (for example, as process tags in an I/O field) and the recipe-specific option "Manual transfer of individually modified values (teach-in mode)" is deactivated, the following applies:

  - If the value of a tag has a more recent value than in the recipe view, this value is transferred to the recipe view.
  - If the value shown in the recipe view is more recent than the value of the tag, this value is transferred to the tag.

  Synchronization with the PLC also takes place.

---

**See also**

[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Read recipe data record from PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In runtime, you can change values directly in the plant that are also stored in recipes in the HMI device. This applies for example if a valve was opened right at the plant wider than specified in the recipe. The values of the recipe data records saved in the HMI device may then possibly no longer match the values in the PLC.

You can read the values of the recipe tags from the PLC and write them to a recipe data record.

The values read are written to the recipe data record that is currently displayed on the HMI device.

##### Procedure

Proceed as follows to read a recipe data record from the PLC:

1. Select the recipe on the HMI device.
2. On the HMI device, select the recipe data record whose values you want to read from the PLC.
3. Click ![Procedure](images/72273296139_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Up Arrow&gt;.

---

**See also**

[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Transferring recipe data records to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For the values of a data record that was changed in the recipe view to take effect, you must transfer the values to the PLC.

The values displayed in the recipe view are always transferred to the PLC.

##### Procedure

Proceed as follows to transfer a recipe data record to the PLC:

1. Select the recipe on the HMI device.
2. On the HMI device, select the recipe data record whose values you want to transfer to the PLC.
3. Click ![Procedure](images/72274341643_DV_resource.Stream@PNG-de-DE.png) in the recipe view or press &lt;Ctrl+Down Arrow&gt;.

---

**See also**

[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Synchronization of recipe data records with the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#synchronization-of-recipe-data-records-with-the-plc-basic-panels-panels-comfort-panels-rt-advanced)
  
[Transferring recipe data records (Basic Panels, Panels, Comfort Panels, RT Advanced)](#transferring-recipe-data-records-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Exporting and importing recipe data (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Exporting and importing recipe data records (Panels, Comfort Panels, RT Advanced)](#exporting-and-importing-recipe-data-records-panels-comfort-panels-rt-advanced)
- [Reactions to modifications of the recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#reactions-to-modifications-of-the-recipe-structure-basic-panels-panels-comfort-panels-rt-advanced)
- [Response of the recipe view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#response-of-the-recipe-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)

#### Exporting and importing recipe data records (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can either export recipe data records to a CSV file or TXT file for editing in MS Excel, for example, or import them from a file.

Recipe export and import depends on the configuration of the device and the device version.

##### List separators

A list separator is used to separate the data records during importing and exporting. The list separator used as the default depends on the setting for formats and numbers in the operating system.

Select "Start &gt; Settings &gt; Control Panel &gt; Regional and Language Options".

If you want to import or export recipe data records, do not use this list separator in the display name of the recipe data records.

The following operating elements can, for example, be configured for using the export/import function:

- Selection field for the recipe
- Selection field for the recipe data record
- Operating element with the "ExportDataRecords" functionality
- Operating element with the "ImportDataRecords" functionality

##### Exporting a recipe data record

Proceed as follows to export a recipe data record to a CSV file:

1. Select the relevant recipe and recipe data record from the selection boxes.
2. Click the control element with the "ExportDataRecords" functionality.

##### Importing recipe data records

To import a recipe data record, proceed as follows:

1. Select the relevant recipe and recipe data record from the selection boxes.
2. Click the control element with the "ImportDataRecords" functionality.

**Display after import of recipes**

If you open the recipe view during the import of recipe data, only the recipe data that is already completely imported will be displayed. The recipe view is not automatically updated following a data import. In order to have a complete view of all the recipe data, do not open the recipe view until the system reports that the recipe data has been imported successfully.

Alternatively, you can update the recipe view after successful completion of the import process.

##### Restrictions on import/export

On Basic Panels you have the possibility of exporting the recipes to a TXT file and importing them from a TXT file with the help of the system functions "ExportDataRecords" and “ImportDataRecords".

> **Note**
>
> **Exporting and importing with ProSave to CSV format**
>
> Individual recipe data records cannot be exported or imported to CSV format with ProSave.
>
> Only complete recipe data can be exported and imported to CSV format with ProSave and transferred to the HMI device.  
> Runtime is paused while this is done.

---

**See also**

[Reactions to modifications of the recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#reactions-to-modifications-of-the-recipe-structure-basic-panels-panels-comfort-panels-rt-advanced)
  
[Response of the recipe view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#response-of-the-recipe-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Reactions to modifications of the recipe structure (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Different recipe structures can occur in the following situations:

- In the event of changes during commissioning
- When work is carried out on the machine by the machine manufacturer (retrofit)
- When CSV files are imported, the structure of the CSV file can differ from the recipe structure.

Nevertheless, you can still use any recipe data records already created.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| When a tag is renamed, the assignment is lost. |  |

##### Effects

Handle any structural differences as follows:

- If the old recipe data record or the CSV file contains additional values, these values will be discarded.
- If the old recipe data record or the CSV file contains values of the wrong data type, the configured default value will be used in the recipe data record.

  Example: The recipe data record contains values that show the tank contents and were input as floating point numbers. However, the corresponding recipe tag expects an integer value. In this case, the system discards the transferred value and the configured default value is used.
- If the old recipe data record or the CSV file contains too few values, the configured default value will also be used in the recipe data record.

---

**See also**

[Exporting and importing recipe data records (Panels, Comfort Panels, RT Advanced)](#exporting-and-importing-recipe-data-records-panels-comfort-panels-rt-advanced)
  
[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Response of the recipe view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Screen change

If you change to another screen and have not yet saved changes to the recipe data in the recipe view, you will be prompted to save the recipe data. The recipe name and the name of the recipe data record are displayed to show which recipe data have not been saved yet.

##### Create, change, copy or delete recipe data records

If you attempt to create a new recipe data record and a recipe data record already exists, a system alarm will appear on screen.

##### Operating the recipe view with function keys

The Recipe view can be operated with function keys, e.g. if the HMI device does not have touch functionality. You can assign functions such as "SaveDataRecord" to the function keys on the HMI device.

##### Display after import of recipe data

> **Note**
>
> **Availability**
>
> Recipe data import and export is not available for Basic Panels.

If you open the recipe view during the import of recipe data, only the recipe data that is already completely imported will be displayed. The recipe view is not automatically updated with a data import. In order to have a complete view of all the recipe data, do not open the recipe view until the system prompts you that the recipe data has been imported successfully. Alternatively, update the recipe view after successful completion of the import procedure.

##### Updating tag for recipes and recipe data records

> **Note**
>
> **Availability**
>
> Tags for recipes and recipe data records are not available for Basic Panels.

The current recipe data record or its number can be saved to a tag, depending on the configuration. The tag will be updated under the following conditions:

- The recipe data record has been loaded.
- The screen with the recipe view was not exited during loading.

This operation may take some time.

---

**See also**

[Exporting and importing recipe data records (Panels, Comfort Panels, RT Advanced)](#exporting-and-importing-recipe-data-records-panels-comfort-panels-rt-advanced)
  
[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Description of advanced recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#description-of-advanced-recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
  
[Recipe view basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

## Configuring Recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Creating and Editing Recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-and-editing-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring the display of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-the-display-of-recipes-basic-panels-panels-comfort-panels-rt-advanced)

### Creating and Editing Recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [General configuration procedure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#general-configuration-procedure-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a new recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-recipe-basic-panels-panels-comfort-panels-rt-advanced)
- [Editing a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#editing-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipes-basic-panels-panels-comfort-panels-rt-advanced)
- [Importing recipes into the configuration and exporting them (Basic Panels, Panels, Comfort Panels, RT Advanced)](#importing-recipes-into-the-configuration-and-exporting-them-basic-panels-panels-comfort-panels-rt-advanced)

#### General configuration procedure (Basic Panels, Panels, Comfort Panels, RT Advanced)

Carry out the following configuration steps when you create a new recipe:

| Step | Description |
| --- | --- |
| 1 | Define the structure of the recipe. |
| 2 | Create tags according to the recipe structure.   Assign process names to these tags. |
| 3 | Create the recipe. |
| 4 | Enter the required properties for the recipe:  - Language-dependent view name of the recipe - "Coordinated transfer of data records" option   Not for Basic Panels:  - Recipe storage location - "Synchronize recipe view and recipe tags" option - "Manual transfer of individual modified values (teach-in mode)" option |
| 5 | Create the recipe elements and enter the required properties:  - Language-dependent view name of the recipe elements - Tag binding of the recipe elements - Standard values and decimal places (power of ten) for the recipe elements |
| 6 | Create the recipe data records.  Enter the language-specific display names for the recipe data records. |
| 7 | Configure a screen with recipe view or a recipe screen. |

> **Note**
>
> **Basic Panels**
>
> The selection of the storage location is not available for these devices. The recipes are always saved in the internal Flash memory.
>
> Recipe tags cannot be used outside a recipe, e.g. not in I/O fields, not in alarms as trigger tags, not in systems functions as parameters, etc.

> **Note**
>
> **Restrictions recipe view and recipe image**
>
> Only the simple recipe view is available in Basic Panels. Recipe screens are not available in Basic Panels.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring the Advanced Recipe View (Panels, Comfort Panels, RT Advanced)](#configuring-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
  
[Creating a new recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-recipe-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a new recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

To create a complete recipe, start by creating a new recipe, assign the corresponding recipe elements and then define the associated values in a recipe data record.

> **Note**
>
> **Character strings that can be imported**
>
> Recipe data that contains semicolons or commas cannot be imported.
>
> Only ever used character strings without semicolons or commas for recipes and recipe data records.

##### Requirement

- The tags for the recipe have been created.
- The "Recipes" editor is open.

##### Creating a recipe

Proceed as follows to create a recipe:

1. Click "Add" in the first free row of the table in the "Recipes" editor.

   The new recipe is created and displayed on a line.

   ![Creating a recipe](images/74786997643_DV_resource.Stream@PNG-en-US.png)

   ![Creating a recipe](images/74786997643_DV_resource.Stream@PNG-en-US.png)
2. Enter a descriptive name for the recipe under "Name" in the "General" area.

   This name identifies the recipe unambiguously within the project.
3. Select "Display name" to enter the language-specific name to be displayed in runtime.
4. Select a recipe number in "Number".

   The number identifies the recipe unambiguously within the HMI device.

   The recipe is automatically assigned a version that indicates the date and time of the last change. As an alternative, you can enter specific information relating to the recipe.
5. Specify the storage location for recipe data records in "Data medium". The options offered depend on the specific HMI device used.
6. Enter a tooltip that is shown to the operator in runtime.
7. To compare recipe tags which are configured in I/O fields with the recipe view in Runtime, activate "Synchronize recipe view and recipe tags" in the Inspector window under "Properties &gt; Synchronization".

   ![Creating a recipe](images/74805904651_DV_resource.Stream@PNG-en-US.png)

   ![Creating a recipe](images/74805904651_DV_resource.Stream@PNG-en-US.png)
8. Deactivate "Manual transfer of individual modified values (teach-in mode)" to specify that the recipe tags are automatically transferred to the PLC when editing the I/O fields.
9. Activate "Coordinated transfer of data records" to monitor the transfer of recipe data in Runtime using area pointers.
10. Select the appropriate connection to the PLC for coordinated transfer under "Synchronize with".

**Note**

**Basic Panels**

The selection of the storage location is not available for these devices. The recipes are always saved in the internal Flash memory.

Recipe tags cannot be used outside a recipe, e.g. not in I/O fields, not in alarms as trigger tags, not in systems functions as parameters, etc.

**Note**

When "Synchronization" &gt; "Synchronize recipe tags" is deactivated and "Display table" is deactivated in the recipe control under "Properties &gt; Table", then recipe data records cannot be sent to or from the PLC in Runtime using the "Write to PLC" and "Read from PLC" buttons.

**Note**

**Basic Panels**

Because the recipe tags cannot be additionally used in I/O fields in screens for Basic Panels, the "Synchronize recipe view and recipe tags" is not available; you will also not be able to use the "Manual transfer of individual modified values (teach-in mode)" option.

##### Create recipe element

To create recipe elements, proceed as follows:

1. Click the "Elements" tab.
2. Click "Add" in the first free line of the table editor.

   A new recipe element is created.
3. Enter a descriptive name for the element under "Name".

   The name identifies the element uniquely within the recipe.
4. Enter a language-specific display name for the element under "Display name".

   The display name appears in the recipe view, for example, in runtime.
5. Select the tag you want to link to the recipe element under "Tag".

   The value of the recipe data element is saved in Runtime in this tag, which is stored in a recipe data record.

   ![Create recipe element](images/97439974667_DV_resource.Stream@PNG-en-US.png)

   ![Create recipe element](images/97439974667_DV_resource.Stream@PNG-en-US.png)
6. Enter a tooltip.

   The tooltip is shown to the operator in Runtime.
7. Under "Default value", enter the value that you want to use as the default entry when you create a new recipe data record.
8. To assign text to a value or range of values, select the relevant text list here. The assigned recipe tag must have the data type of a number. The tag value must be within the range of values of the text list.

   The text stored in the text list is displayed in an output field, for example, in Runtime.
9. Determine exactly how many places a decimal number is rounded to in the "Decimal places" column, e.g. 3 decimal places and vice versa by what power of ten an integer value is multiplied, e.g. 1,000.  
   Examples for 3 decimal places: Entering "5" for a recipe element with the "Integer" data type gives the value "5000". Entering "5.6789" for a recipe element with the "Real" data type gives the value "5.679".
10. Create as many recipe entries as needed for the recipe. The maximum number of recipe entries possible depends on the HMI device being used.

    ![Create recipe element](images/74818295691_DV_resource.Stream@PNG-en-US.png)

    ![Create recipe element](images/74818295691_DV_resource.Stream@PNG-en-US.png)

##### Create recipe data record with known recipe values

To create recipe elements, proceed as follows:

1. Click the "Data records" tab.
2. Click "Add" in the first free line of the table editor.

   A new recipe data record is created. The recipe data record has a separate column for every recipe element created in the recipe.

   ![Create recipe data record with known recipe values](images/14182266251_DV_resource.Stream@PNG-en-US.png)

   ![Create recipe data record with known recipe values](images/14182266251_DV_resource.Stream@PNG-en-US.png)
3. Enter a descriptive name under "Name".

   The name identifies the data record uniquely within the recipe.
4. Enter a language-specific name under "Display name".

   The display name appears in the recipe view, for example, in runtime.
5. Enter a recipe data record number under "Number".

   The recipe data record number identifies the recipe data record uniquely within the recipe.
6. If you already know the recipe values at the configuration stage, you can enter the relevant value for each recipe element.

   ![Create recipe data record with known recipe values](images/14182275339_DV_resource.Stream@PNG-en-US.png)

   ![Create recipe data record with known recipe values](images/14182275339_DV_resource.Stream@PNG-en-US.png)
7. Create as many data records as you need for the recipe.

   ![Create recipe data record with known recipe values](images/14182540427_DV_resource.Stream@PNG-en-US.png)

   ![Create recipe data record with known recipe values](images/14182540427_DV_resource.Stream@PNG-en-US.png)

##### Enter the values in runtime

The following options are available for entering values in the recipe data records at runtime:

- Transfer data directly from the PLC (Teach-in mode)
- Import of values from a CSV file
- Input values on the HMI device

  > **Note**
  >
  > **Basic Panels**
  >
  > The import of values is not available for these devices.

##### Result

The complete recipe is configured.

##### Recipe data records with date or time stamp

If you use date or time data, make sure that the system setting for time and date on the configuring computer match those on the target system. Example: You load a recipe data record on the target system at 13:55 in which 14 h is stored as the processing time. If it is already 14:05 on the target computer, the recipe will not be processed. If an operator processes the recipe, change information will not written back correctly into the database.

After loading to the target system, check the recipes with date or time stamps on the target system.

---

**See also**

[Managing recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-recipes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Editing a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#editing-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)
  
[General configuration procedure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#general-configuration-procedure-basic-panels-panels-comfort-panels-rt-advanced)

#### Editing a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Purpose

You want to modify, extend or delete parts of a recipe.

##### Requirement

- You have created at least one recipe.
- The "Recipes" editor is open.

##### Changing recipe settings

To change the recipe settings, proceed as follows:

1. Select the recipe that you want to change in the "Recipes" editor.

   The Inspector window opens.
2. Change the recipe configuration in the Inspector window.

You change recipe elements and recipe data records in the same way.

##### Change recipe values

To change recipe values, proceed as follows:

1. Select the recipe whose values you want to change.
2. Click the "Data records" tab.
3. Enter the new values in the value columns.

##### Adding a recipe element

To add more recipe elements to a recipe, proceed as follows:

1. Select the recipe to which you want to add more elements in the "Recipes" editor.
2. Click the "Elements" tab.
3. Click "Add" in the first free line.

   The recipe element is created.
4. Configure the recipe element.

You add recipe data records in the same way.

---

**See also**

[Creating a new recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Requirement

- You have created a recipe with recipe elements and recipe data record.
- The "Recipes" editor is open.

##### Renaming recipes

We distinguish between internal names and display names for recipes, recipe entries and recipe data records.

To rename recipe elements, proceed as follows:

1. Select the recipe that you want to rename.

   The Inspector window opens.
2. Select the "Rename" command from the shortcut menu.
3. Enter the new name.

   You rename recipe elements and recipe data records on the relevant tab in the same way.

**Note**

The view names in the "Recipes" editor can also be renamed under "Languages &amp; Resources &gt; Project Texts". This possibility is useful when you have already configured in several languages for example.

##### Copying and pasting recipes

To copy and paste recipes, proceed as follows:

1. Select the recipe that you want to copy.
2. Select the "Copy" command from the shortcut menu.
3. Select the "Paste" command from the shortcut menu in the first free table row.

The copied recipe is pasted into the table. The recipe elements and recipe data records are also copied in the appropriate tab with the recipe.

You also copy the recipe elements and recipe data records on the appropriate tab in the same way.

If a recipe data record of the same name already exists, the name of the copied recipe data record is extended by one digit. This ensures that the name is unique. Recipe data records can only be copied or pasted within the same recipe.

##### Deleting a recipe

To delete a recipe, proceed as follows:

1. Select the recipe that you want to delete.
2. Select the "Delete" command from the shortcut menu.

   The recipe is deleted.

You delete recipe elements and recipe data records on the relevant tab in the same way.

> **Note**
>
> When a recipe is deleted, the recipe data records contained in the recipe are also deleted.

> **Note**
>
> When you delete a recipe element, the associated values in the recipe data records are also deleted. The assigned tags are retained.

---

**See also**

[Creating a new recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Importing recipes into the configuration and exporting them (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can export recipes as a CSV file and import them again into the configuration.

##### Application case

Recipe data is exported for long-term storage and backup on a computer.

In order to unify and distribute recipe data, export the recipe data to an HMI device. Change the CSV file in Microsoft Excel and import the CSV file to all HMI devices that require the same recipe data.

You want to exchange recipe data between different projects. You change the recipe data in Runtime. To transfer the modified recipe data to WinCC ES, export the recipe data records in Runtime and copy the CSV file to the configuring computer. There you import the CSV file containing the recipe data records into the recipe. And in the opposite direction, you transfer the modified recipe data records to the HMI device in WinCC ES in Runtime.

##### Requirement

- You have created the recipe.
- The structures of the exported CSV file and the recipe in WinCC ES match; name, number and data type of the recipe elements are identical.
- The "Recipes" editor is open.
- Any semicolons or commas in the import file are used as separators only.

##### Importing CSV files

To import recipe data records into a recipe, proceed as follows:

1. Select the row which contains the desired recipe in the "Recipes" tab.
2. Select the "Import recipe data" command from the shortcut menu.

   The "Import" dialog box opens.

   ![Importing CSV files](images/83113330827_DV_resource.Stream@PNG-en-US.png)

   ![Importing CSV files](images/83113330827_DV_resource.Stream@PNG-en-US.png)
3. To select the desired CSV file, go to "File name".
4. Under "Strategy", specify whether a recipe data record with the same recipe number in WinCC ES should be overwritten.
5. Specify the list separator and decimal separator under "Data separation". The list separator separates individual recipe elements in the CSV file. The decimal separator separates integers and decimal places.
6. Click "Import" to start the operation.

**Note**

Use the same list separator for import as in the CSV file for export.

##### Result

The recipe will be amended by recipe data records from the CSV file that have not yet been entered. If the option is selected, existing recipe data records will be overwritten.

An error message is shown in the "Info" of the Inspector window if the structure of the recipe does not match the structure of the CSV file.

##### Exporting CSV files

1. Select the row which contains the recipe to export in the "Recipes" tab.
2. Select the "Export recipe data" command from the shortcut menu.

   The "Export" dialog box opens.

   ![Exporting CSV files](images/83113335307_DV_resource.Stream@PNG-en-US.png)

   ![Exporting CSV files](images/83113335307_DV_resource.Stream@PNG-en-US.png)
3. Under "File name", specify the path of the CSV file.
4. Select all recipe data records under "Selection content", or restrict the selection to specific record numbers of the recipe data.
5. Specify the list separator and decimal separator under "Data separation". The list separator separates individual recipe elements in the CSV file. The decimal separator separates integers and decimal places.
6. Click "Export" to start the operation.

##### Result

The configuration is exported as a CSV file.

### Configuring the display of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring the Advanced Recipe View (Panels, Comfort Panels, RT Advanced)](#configuring-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
- [Configuring a recipe screen (Panels, Comfort Panels, RT Advanced)](#configuring-a-recipe-screen-panels-comfort-panels-rt-advanced)

#### Configuring the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Requirement

- The recipe has been created.
- The "Screens" editor is open.
- The screen has been created and opened.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Data loss with several recipe views in the screen**  Only applies for Basic Panels: If two or more recipe views show the same recipe in a screen, you have a conflict when accessing the data.  The result is data loss and unpredictable status of recipe data.  Make sure the operators do not select and edit the same recipe in different recipe views.  - Display only one recipe in a recipe view. - Display a different recipe in each recipe view. |  |

##### Procedure

To configure a simple recipe view, proceed as follows:

1. Paste the recipe view into the screen. You will find the recipe view under "Controls" in the "Tools" task card.
2. Only in devices which also support the extended recipe view: Activate "Simple view" under "Properties &gt; Display &gt; Mode".
3. If you want to display only the recipe data records of a specific recipe in the recipe view, select the specific recipe under "Properties &gt; General &gt; Recipe".

   ![Procedure](images/111894363147_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111894363147_DV_resource.Stream@PNG-en-US.png)
4. If you only want to display the recipe data in the recipe view, deactivate "Processing mode" in the "Recipe data record" area.
5. You can define additional options for the recipe view under "Properties &gt; Appearance" and "Properties &gt; Layout".
6. Under "Properties &gt; Toolbar" specify which menu commands are available in the recipe view in Runtime.

   ![Procedure](images/97444184203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97444184203_DV_resource.Stream@PNG-en-US.png)

##### Result

The simple recipe view is configured. You can use the recipe view to display and edit recipe data during runtime.

Deactivation of the editing mode in "Properties &gt; Properties &gt; General" has no impact on the toolbar icons. The buttons activated under "Properties &gt; Toolbar" can still be used even if editing mode is disabled.

---

**See also**

[Configuring the Advanced Recipe View (Panels, Comfort Panels, RT Advanced)](#configuring-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring the Advanced Recipe View (Panels, Comfort Panels, RT Advanced)

##### Requirement

- The recipe has been created.
- The "Screens" editor is open.
- The screen has been created and opened.

##### Procedure

To configure an advanced recipe view, proceed as follows:

1. Paste the recipe view into the screen. The recipe view is found in the task card "Tools" &gt; "Controls".
2. Select "Properties &gt; Display &gt; Mode &gt; Advanced view" in the Inspector window.

   ![Procedure](images/88397431179_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88397431179_DV_resource.Stream@PNG-en-US.png)
3. Select the required settings from the "General" group in the Inspector window.

   - If you want to display only the recipe data records for a particular recipe in the recipe view, select the recipe under "Recipe" in the "Recipes" area.
   - If you want to save the recipe name or the recipe number in a tag, select the tag under "Recipe tag" in the "Recipe" area.
   - If you want to save the recipe data record name or number in a tag, select the tag under "Tag" in the "Recipe data record" area.
   - If you only want to display the recipe data in the recipe view, deselect "Edit mode".
   - If you only want to use the recipe view to select recipes, disable "Display table" under "Properties &gt; Table".
4. You can define additional options for the recipe view under "Properties &gt; Appearance" and "Properties &gt; Layout".
5. If you want to change the label in the recipe view, enter a suitable text under "Properties" &gt; "Label".
6. Under "Properties" &gt; Toolbar" specify which buttons are available in the recipe view in Runtime.

   ![Procedure](images/88396456715_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88396456715_DV_resource.Stream@PNG-en-US.png)

**Note**

If you select the "Edit" command in the context menu of the recipe view, the recipe view becomes active. To activate the recipe view, the zoom factor must be set to 100%.

You can set the column width and the position of the "Entry name" and "Value" columns in active mode.

##### Result

The recipe view is configured. You can use the recipe view to display and edit recipe data during runtime.

Deactivation of the editing mode in "Properties &gt; Properties &gt; General" has no impact on the toolbar icons. The buttons you activated in "Properties &gt; Toolbar" can still be used even if editing mode is disabled.

---

**See also**

[Configuring the simple recipe view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-the-simple-recipe-view-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a recipe screen (Panels, Comfort Panels, RT Advanced)](#configuring-a-recipe-screen-panels-comfort-panels-rt-advanced)
  
[General configuration procedure (Basic Panels, Panels, Comfort Panels, RT Advanced)](#general-configuration-procedure-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring a recipe screen (Panels, Comfort Panels, RT Advanced)

##### Introduction

The recipe screen is a screen in which you configure a customized screen form in the "Screens" editor. You create the screen form from input/output fields and other display and operator control objects. System functions are used to configure the recipe functionality, such as saving recipe data records.

> **Note**
>
> **Availability**
>
> Recipe screens cannot be created for Basic Panels.

##### Application

You can spread recipe data records containing lots of entries across several screens. For example, for each plant you can configure a screen containing the associated screen forms for the recipe data records.

You can visually simulate your machine in a screen using graphical screen objects. This enables you to display parameter settings more clearly by positioning I/O fields immediately next to machine elements, such as axes or guide rails. You can use this to produce a direct reference between the values and the machine.

##### Requirement

- You have created the recipe.
- The "Screens" editor is open.

##### Procedure

To configure a recipe screen, proceed as follows:

1. Configure the screen and create the I/O fields for the input mask of the recipe.

   You can create multiple screens to suit the size and complexity of the recipe.
2. Configure the I/O fields with the tags you have linked to the recipe element.
3. Configure I/O fields for selecting recipes and recipe data records.

Alternatively:

1. Configure a recipe view as a selection list for recipe data records and recipes.
2. Hide the buttons that are not required in the recipe view.
3. Configure the system functions for editing recipe data records on the configured control elements.

   Control elements are configured buttons in the screen or function keys on the HMI device.

   You will find the system functions for editing recipe data records under "Recipes" and "Keyboard operation for screen objects".

##### Result

The recipe screen is created.

---

**See also**

[Configuring the Advanced Recipe View (Panels, Comfort Panels, RT Advanced)](#configuring-the-advanced-recipe-view-panels-comfort-panels-rt-advanced)
  
[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

## Examples (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)
- [Example of configuring a recipe screen (Panels, Comfort Panels, RT Advanced)](#example-of-configuring-a-recipe-screen-panels-comfort-panels-rt-advanced)
- [Scenario for Entering Recipe Data Records in Runtime (Panels, Comfort Panels, RT Advanced)](#scenario-for-entering-recipe-data-records-in-runtime-panels-comfort-panels-rt-advanced)
- [Scenario for a manual production sequence (Panels, Comfort Panels, RT Advanced)](#scenario-for-a-manual-production-sequence-panels-comfort-panels-rt-advanced)
- [Scenario for an Automatic Production Sequence (Panels, Comfort Panels, RT Advanced)](#scenario-for-an-automatic-production-sequence-panels-comfort-panels-rt-advanced)

### Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Task

In this example, you create three recipes for a fruit juice mixing machine. The fruit juice mixing machine produces drinks with "orange", "apple" and "tropical" flavors. You create a recipe for each flavor.

Each recipe contains a recipe data record for the following mixing ratios:

- Beverage
- Nectar
- Juice

#### Settings

The settings relate to an HMI device which is connected to a SIMATIC S7-300 or SIMATIC S7-400.

In this example, you will need the following tags, recipes, recipe entries and recipe data records:

**Tags:**

| Name | PLC connection | Address | Type |
| --- | --- | --- | --- |
| Liter water | Yes | DB 120, DBW 0 | Integer |
| Liter concentrate | Yes | DB 120, DBW 4 | Integer |
| Kilo sugar | Yes | DB 120, DBW 8 | Integer |
| Gram flavoring | Yes | DB 120, DBW 12 | Integer |

**Recipes:**

- Orange
- Apple
- Tropical

**Recipe entries:**

| Recipe element | Associated tag |
| --- | --- |
| Liter water | Liter water |
| Liter concentrate | Liter concentrate |
| Kilo sugar | Kilo sugar |
| Gram flavoring | Gram flavoring |

**Recipe data records for drink, nectar and juice:**

| Data record name | Liter water | Liter concentrate | Kilo sugar | Gram flavoring |
| --- | --- | --- | --- | --- |
| Beverage | 30 | 70 | 45 | 600 |
| Nectar | 50 | 50 | 10 | 300 |
| Juice | 5 | 95 | 3 | 100 |

#### Procedure

To create a recipe, proceed as follows:

1. Create the following tags with the settings specified above: "LiterWater", "LiterConcentrate", "KiloSugar" and "GramFlavoring".
2. Create the "Orange", "Apple" and "Tropical" recipes with the settings indicated above. Create the recipe entries in each recipe.

   ![Procedure](images/74818295691_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74818295691_DV_resource.Stream@PNG-en-US.png)
3. Not for Basic Panels: Configure each recipe so that you can synchronize the recipe data records between the recipe screen and recipe view. The values of the recipe tags should not be transferred automatically to the PLC.

   You will have to make the following settings in the Properties dialog for the recipe concerned:

   Under "Properties &gt; Options":

   - Activate the "Synchronize recipe view and recipe tags" option.
   - Activate the "Manual transfer of individual modified values (teach-in mode)" option.
4. Create the data records indicated above in each recipe. Enter the values indicated above in each of the data records.

   ![Procedure](images/14182540427_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/14182540427_DV_resource.Stream@PNG-en-US.png)

#### Result

The "Orange", "Apple" and "Tropical" recipes have been created.

---

**See also**

[Definition and applications (Basic Panels, Panels, Comfort Panels, RT Advanced)](#definition-and-applications-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuration options of the advanced recipe view (V13 or higher) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuration-options-of-the-advanced-recipe-view-v13-or-higher-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example of configuring a recipe screen (Panels, Comfort Panels, RT Advanced)](#example-of-configuring-a-recipe-screen-panels-comfort-panels-rt-advanced)
  
[Scenario for Entering Recipe Data Records in Runtime (Panels, Comfort Panels, RT Advanced)](#scenario-for-entering-recipe-data-records-in-runtime-panels-comfort-panels-rt-advanced)
  
[Scenario for a manual production sequence (Panels, Comfort Panels, RT Advanced)](#scenario-for-a-manual-production-sequence-panels-comfort-panels-rt-advanced)
  
[Scenario for an Automatic Production Sequence (Panels, Comfort Panels, RT Advanced)](#scenario-for-an-automatic-production-sequence-panels-comfort-panels-rt-advanced)

### Example of configuring a recipe screen (Panels, Comfort Panels, RT Advanced)

#### Task

In this example, you create a recipe screen for the visualization of values of the fruit juice mixing machine. You use a recipe view to select the recipes and their associated recipe data records.

You should be able to use the following functions with the buttons:

- "Load" Button

  The selected recipe data record is loaded from the recipe memory on the HMI device and displayed in the recipe screen.
- "Save" Button

  The displayed recipe tags are saved in the recipe memory of the HMI device.
- "Data to PLC" button

  The displayed tags are transferred to the PLC.
- "Data from PLC" button

  The current recipe data record in the PLC is transferred to the recipe variables and displayed on the HMI device.

  ![Task](images/12894893067_DV_resource.Stream@PNG-en-US.png)

#### Requirement

- The "Creating a recipe" sample application has been carried out.
- You have created and opened the "Fruit juice mixing plant" screen.

#### Settings

In this example, you need the following tags and buttons with the indicated settings:

**Tags:**

| Name | PLC connection | Type |
| --- | --- | --- |
| RecipeNumber | No | Integer |
| Data record number | No | Integer |

**Buttons:**

| Labeling | Configured event | System function |
| --- | --- | --- |
| Load | Click | LoadDataRecord |
| Save | Click | SaveDataRecord |
| Data to PLC | Click | SetDataRecordTagsToPLC |
| Data from PLC | Click | GetDataRecordTagsFromPLC |

#### Procedure

To configure a recipe screen, proceed as follows:

1. Drag-and-drop the "Liter water", "Liter concentrate", "Kilo sugar" and "Gram flavoring" tags from the object view to the "Fruit juice mixing machine" process screen.

   Four IO fields are created and linked by the specified tags.
2. Add a recipe view containing selection fields for the recipe name and data record name only.

   Make the following settings in the Inspector window for the recipe view:

   - Select the "Advanced view" display type under "General".
   - Deselect "Edit mode" under "Properties &gt; General" and "Display table" under "Properties &gt; Table".
   - Connect the "Recipe tag" field to the "RecipeNumber" tag.
   - Connect the "Tag" field to the "DataRecordNumber" tag.
   - Disable all the buttons under "Properties &gt; Buttons".
3. Assign the above settings to four buttons. Transfer each "Recipe number" and "Data record number" tag as a parameter for the recipe number and recipe data record number.

#### Result

You can select the recipe and the associated recipe data record from the recipe view and modify the recipe values at runtime. You can load, save and transfer the recipe data records using the buttons.

---

**See also**

[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Scenario for Entering Recipe Data Records in Runtime (Panels, Comfort Panels, RT Advanced)

#### Objective

You want to enter production data on the HMI device without disturbing the process that is currently underway. Therefore, the production data should not be transferred to the PLC.

#### Requirement

- The recipe has been created.
- The recipe has the following settings:

  - "Synchronizing recipe view and recipe tags" is activated or deactivated.
  - If "Synchronize recipe view and recipe tags" is activated, "Manual transfer of individual modified values (teach-in mode)" has to be activated.

    This will prevent the recipe tags being transferred automatically between the HMI device and PLC.
- A recipe screen or a screen with recipe view is available.
- There is an operating element for saving the recipe data records.

#### Sequence

![Sequence](images/24584887051_DV_resource.Stream@PNG-en-US.png)

1. Enter the production data in the recipe view or recipe screen.
2. Save the modified recipe data record.

#### Transfer the recipe data to the PLC

The configuration may provide operating elements for transferring recipe data to the PLC.

---

**See also**

[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Scenario for a manual production sequence (Panels, Comfort Panels, RT Advanced)

#### Objective

A reading device connected to the PLC reads a bar code on the work piece to be processed. The recipe data record names correspond to the respective bar code names. This will enable the PLC to load the necessary recipe data record from the storage medium of the HMI device. The recipe data record is displayed for inspection on screen.

You want to be able to correct the transferred production data online, if necessary.

#### Requirement

- You have created the recipe.
- The recipe has the following settings:

  - "Synchronizing recipe view and recipe tags" is activated.
  - "Manual transfer of individual modified values (teach-in mode)" is deactivated.

    > **Note**
    >
    > The changes are immediately transferred to the PLC
- There is a recipe screen available.

  There may also be an operating element for saving the recipe data records in the recipe screen.

#### Sequence

![Sequence](images/24584910731_DV_resource.Stream@PNG-en-US.png)

#### Behavior when the recipe view is used

If the recipe view is used, it is not possible to transfer changes immediately. You must use the operating element to transfer the recipe data record to the PLC.

---

**See also**

[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)

### Scenario for an Automatic Production Sequence (Panels, Comfort Panels, RT Advanced)

#### Objective

You want production to be executed automatically. The production data is to be transferred directly to the PLC, either from the recipe memory in the HMI device or from an external storage medium. The screen display is not necessary.

#### Requirement

- You have created the recipe.
- The recipe has the following settings:

  - "Coordinated transfer of data records" is activated.

    The production data is transferred to the PLC, so a coordinated transfer with the PLC in necessary to prevent the data from being accidentally overwritten.

#### Sequence

![Sequence](images/24584914699_DV_resource.Stream@PNG-en-US.png)

#### Implementation

You can control the flow of data in the following ways:

- The control program controls the automatic transfer via control jobs or via WinCC system functions, if necessary.

  The sequence is controlled via the status information in the mailbox and via return values from the functions used.
- One or more scripts control the automatic transfer via WinCC system functions.

  The sequence can be checked using the values returned by the functions used.

You can implement the automatic production sequence with available system functions:

- "ImportDataRecords"

  This function loads data records from a *.CSV file into the recipe memory of the HMI device.
- "SetDataRecordToPLC"

  This function transfers a data record from the HMI device's recipe memory to the PLC.

---

**See also**

[Example of creating a recipe (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-of-creating-a-recipe-basic-panels-panels-comfort-panels-rt-advanced)
