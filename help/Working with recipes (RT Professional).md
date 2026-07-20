---
title: "Working with recipes (RT Professional)"
package: UserArchivesWCCPenUS
topics: 58
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with recipes (RT Professional)

This section contains information on the following topics:

- [Principles (RT Professional)](#principles-rt-professional)
- [Configuring Recipes (RT Professional)](#configuring-recipes-rt-professional)
- [Configuring the visualization of recipes (RT Professional)](#configuring-the-visualization-of-recipes-rt-professional)
- [Data transfer to the PLC (RT Professional)](#data-transfer-to-the-plc-rt-professional)
- [Operation in Runtime (RT Professional)](#operation-in-runtime-rt-professional)
- [Examples (RT Professional)](#examples-rt-professional)

## Principles (RT Professional)

This section contains information on the following topics:

- [Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
- [Recipe structure (RT Professional)](#recipe-structure-rt-professional)
- [Displaying Recipes in Runtime (RT Professional)](#displaying-recipes-in-runtime-rt-professional)
- [Communication with the PLC (RT Professional)](#communication-with-the-plc-rt-professional)
- ["Recipes" Editor (RT Professional)](#recipes-editor-rt-professional)
- [SQL language (RT Professional)](#sql-language-rt-professional)
- [SQL keywords (RT Professional)](#sql-keywords-rt-professional)

### Definition and applications (RT Professional)

#### Introduction

Recipes are collections of related data, for example, machine parameter settings or production data.

Examples:

- Machine parameter settings that are needed to convert production to a different product variant.
- Product components that result in different compositions for different end products.
- Data from technical processes that is continuously stored at longer intervals.

A recipe has a fixed data structure. The structure of a recipe is defined once at the configuration stage. A recipe contains recipe data records. These differ in terms of their values, but not their structure.

The project data is stored in an SQL database. Recipe data records are always transferred completely and in a single pass between the HMI device and the PLC. You can import the production data in Runtime additionally by a CSV file.

#### Using recipes

Recipes can be used in the following situations:

- Manual production

  You select the required recipe data and display it on the HMI device. You modify the recipe data as required and save it on the HMI device. You transfer the recipe data to the PLC.
- Automatic production

  The control program starts transfer of the recipe data between the PLC and HMI device. You can also start the transfer from the HMI device. Production is then implemented automatically. It is not essential to display or modify the data.
- Saving project data

  You are using a recipe which is not interconnected with the PLC to save project data. Project data saved to the recipe can be accessed using scripts in Runtime.

#### Views

Views relate data from existing recipes that have at least one common feature. They are used to compile data from the recipes.

#### Display recipes and views

The recipes and views can be displayed and edited on the HMI device in the following ways:

- A recipe view within a process screen
- A recipe screen

#### Entering and modifying the recipe data

You enter the data in the individual recipe data records and modify it as required. The following options are available:

- Enter the data during configuration

  If the production data exists already, enter it in the "Recipes" editor during recipe configuration.
- Entering the data in Runtime

  Frequent adaptations of production data should be handled directly in Runtime.

  - Enter the data directly on the HMI device.
  - Set the parameters directly on the machine. You then transfer the data from the PLC to the HMI device and save it in the recipe.
  - You import the recipe data from already swapped-out CSV files.

---

**See also**

["Recipes" Editor (RT Professional)](#recipes-editor-rt-professional)
  
[General configuration procedure (RT Professional)](#general-configuration-procedure-rt-professional)
  
[Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)
  
[Recipe structure (RT Professional)](#recipe-structure-rt-professional)
  
[Displaying Recipes in Runtime (RT Professional)](#displaying-recipes-in-runtime-rt-professional)
  
[Communication with the PLC (RT Professional)](#communication-with-the-plc-rt-professional)
  
[Recipe view in reports (RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#recipe-view-in-reports-rt-professional)
  
[Recipe report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#recipe-report-panels-comfort-panels-rt-advanced)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Recipe structure (RT Professional)

#### Introduction

The basic structure of a recipe is illustrated with reference to a filling station in a fruit juice plant.

There may be several different recipes in an HMI device. A recipe can be compared to an index card box that contains several index cards. The index card box contains several variants for manufacturing a product family. The complete data of a manufacturer variant are contained on one file card.

Example:

In a soft drinks production plant, a recipe is needed for different flavors. Drink variants include fruit juice drink, juice, and nectar.

#### Recipe

![Recipe](images/7581210507_DV_resource.Stream@PNG-en-US.png)

#### Recipe data records

Each index card represents a recipe data record needed to manufacture a product variant.

#### Recipe elements

Each index card in a drawer is printed identically. All the index cards contain fields for the different ingredients. Each field corresponds to a recipe element. Each recipe data record contains the same elements. The records differ, however, in the value of the individual elements.

Example:

All beverages contain the same elements:

- Water
- Concentrate
- Sugar
- Flavoring

The records for juice drink, fruit juice, or nectar differ, however, in the quantity of sugar used in production.

| Recipe | Recipe data record | Recipe elements | Value |
| --- | --- | --- | --- |
| Drinks | 1 | Item | Juice |
| Water | 5 |  |  |
| Sugar | 30 |  |  |
| Flavoring | 23 |  |  |
| Concentrate | 80 |  |  |
| Coloring | F30 |  |  |
| 2 | Item | Nectar |  |
| Water | 15 |  |  |
| Sugar | 35 |  |  |
| Flavoring | 20 |  |  |
| Concentrate | 70 |  |  |
| Coloring | F35 |  |  |

#### Recipe queries

A recipe query is a recipe whose elements are made up of various recipes. Example:

Recipe query Element1 = Recipe1_Recipe element 3

Recipe query Element2 = Recipe3_Recipe element 7

Recipe query Element3 = Recipe2_Recipe element 10

The used recipes must already exist.

A recipe query is displayed in a recipe view. Instead of having its own data records, however, a recipe query combines all the recipe data records of the recipes used. Example: If there are 10 recipe data records for each recipe in the example above, the recipe query covers 10*10*10 = 1000 data records. You can define a relation in the recipe query to limit these data records. Example:

Recipe query Element2 = Recipe query Element3

The relation acts as a filter for the recipe query (see also example below).

#### Example

A "Label" recipe query is created from the "Drinks" and "Order" recipe for label printing.

![Example](images/27522912907_DV_resource.Stream@PNG-en-US.png)

The figure below shows the "Label" recipe query. The necessary information for the label is contained in the "Drinks" and "Order" recipes. The recipe elements "Article", "Sugar", "Colorant" and "Best before" are transferred to the "Label" recipe query from the "Drinks" recipe, the recipe elements "Article" and "Net weight" from the "Order" recipe.

The "Article" recipe element is double:

Drinks.Article, Order.Article, Drinks.Water, Order.Net weight...

The recipe view first shows every combination of these data in its own line. However, the recipe data of the ordered article and not of another article must be on the label which is ensured by the following condition:

Drinks.Article = Order.Article

The recipe view is filtered and only the ordered articles with their recipe data displayed line by line.

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Displaying Recipes in Runtime (RT Professional)

You have the following options of displaying recipe data in Runtime:

- In I/O fields at any position in plant screens
- In a recipe view in table format

You can connect a recipe view to a selected recipe and/or recipe query during configuration. The recipe view can only access this recipe and/or recipe query.

You can assign various authorizations for access.

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Communication with the PLC (RT Professional)

#### Introduction

Data are transmitted in two ways between recipes and the PLC:

- By recipe tags with the aid of control tags
- By message frames with the aid of raw data tags

#### "Control tags" communication type

A complete recipe data record is transferred to the recipe tags and vice versa by control tags. The recipe tags have a communication connection to the PLC

#### "Raw data tag" communication type

The PLC and the HMI device exchange raw data tags as message frames with a fixed structure.

Raw data tags offer the following advantages:

- Several data records transferred between the PLC and the HMI device.
- Parts of a recipe data record transmitted.
- Use the same raw data tag for several recipes.

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### "Recipes" Editor (RT Professional)

#### Introduction

You can create, configure and edit the following objects in the "Recipes" editor.

- Recipes and the corresponding recipe elements and recipe data records.
- Recipe queries and the corresponding recipe query elements and relations

The "Recipes" editor also allows you to enter values in recipe data records.

#### Structure of the "Recipes" editor

The upper part of the working area in the "Recipes" editor contains the "Recipes" and "Recipe queries" tabs.

Create the recipes and/or recipe queries in the "Recipes" and "Recipe queries" tabs and configure these in the Inspector window.

The tab called in the upper area of the working area determines the tabs to display in the bottom area of the working area.

"Recipes" tab

- Recipe elements

  Define the recipe elements of the selected recipe using the table cells provided here. You can move recipe elements within the table with the shortcut menu commands, "Up" and "Down".
- Recipe data records

  Define the values of the data records of the selected recipe using the table cells provided here.

"Recipe queries" tab

- Recipe query elements

  Here, you define the recipe query elements of the selected recipe query via the table cells. You move recipe queries and recipe query elements within the table using the "Up" and "Down" shortcut menu commands.

  You define the relations between the recipe query elements in the "Conditions" field.

#### Inspector window

In the Inspector window, you configure each element that is selected in one of the tables, e.g. a recipe query or recipe data record.

#### Recipe settings

The following settings are available for recipes:

| Setting | Description |
| --- | --- |
| Recipe name | This is a unique identification for the recipe within the HMI device. |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Enter meaningful names or designations which you can assign directly to a product, such as "Fruit_juice_Orange". |
| Recipe number | This is a unique identification for the recipe within the HMI device.  For the "Raw data tag" communication type, the "PLC" field in the message frame must correspond to a valid recipe number. |
| Version | Information about the recipe. The date and time of the last change to the recipe is set by default. |
| Path | Defines the storage location for recipes. The recipes are not saved in a file but in a database. |
| Type | You can limit the recipe data records to a maximum number you select yourself. |
| Maximum number of data records | Maximum number of data records in a recipe. This limits the required recipe memory of the HMI device. The value "0" appears for the "Unlimited" size type. |
| Communication type | Define how the HMI device and PLC exchange recipe data as a rule:  - No communication - Raw data tags - Tags |
| Raw data tag | Tag which transfers the recipe data as a frame between the PLC and the HMI device in the "raw data tag" communication type. |
| Control tag task, ID, field, value | Four tags which control the data transmission between the recipe and recipe tags and therefore the PLC in the "tags" communication type. |
| For reading  For writing | Name of the authorization which has read, write access to the recipe in runtime. |
| Last access  Last user | Change information or access to a recipe is displayed in Runtime. |
| Tooltip | Infotext on recipe for the configuration engineer |

#### Recipe element settings

The following settings are available for recipe elements:

| Setting | Description |
| --- | --- |
| Recipe element name | Identifies a recipe element uniquely within the recipe. Enter meaningful names or labels that you can allocate uniquely, such as axis labels on a machine or ingredients such as "Flavoring". |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Enter meaningful names or designations which you can assign directly to a product, such as "Fruit_juice_Orange". |
| Recipe tag | An assigned tag in Runtime stores the current value of the recipe element in the recipe data record. You cannot use a tag of the data type "DateTime". |
| Data type | Data type of the recipe tag. |
| Data length | Data length of the recipe tag, depending on the data type. |
| Default value | This is used as the default entry when you create a new recipe data record. |
| Minimum value | The smallest representable value of a number-based recipe tag, depending on the data type. |
| Maximum value | The largest representable value of a number-based recipe tag, depending on the data type. |
| For reading  For writing | Name of the authorization which has read, write access to the recipe in runtime. |
| Value required | The recipe element has a value other than zero. |
| Unique values | A value for the recipe element can only occur once in all recipe data records. Example recipe element "Order number". |
| Fast search | The value of the recipe element is indexed for faster searching. |
| Tooltip | Infotext on recipe element for the configuration engineer |

#### Recipe data record settings

The following settings are available for recipe data records:

| Setting | Description |
| --- | --- |
| Recipe data record name | Identifies a recipe data record uniquely within the recipe. |
| Display name | Appears in the recipe view, for example, in Runtime. You can configure display names in multiple languages. Enter meaningful names or labels that you can assign directly to a product, such as "Product_numbers". |
| Recipe data record number | Identifies a recipe data record uniquely within the recipe. |
| Recipe element name | Name of the created recipe element The values which the recipe element has in the different recipe data records (lines) are saved under this name. A value forms a recipe data record respectively with the values of the other recipe elements in a line. You can already save the values during the configuring. |
| Last access  Last user | Change information or access to a recipe data record is displayed in Runtime. |
| Comment | Comment about the recipe data record |

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)

### SQL language (RT Professional)

SQL (Structured Query Language) is an efficient and widely distributed database language. The SQL language is used for database queries in the functions of the WinCC script language. You will find further information in the relevant technical manuals.

In some standard functions and some functions in the "Recipes" editor, you must specify conditions in the database language SQL to specify the data records to be edited. A few examples of how provide an SQL instruction are given below:

> **Note**
>
> **Name convention**
>
> Suffixes, extensions and the name of a recipe, recipe query or a recipe element may only consist of letters, numbers and underscores "_" and may not exceed a length of 20 characters. The first character must always be a letter.

- `FieldA`
   `> '1992-12-31 23:45:12.12'`

  The instruction selects all data records whose value in the "FieldA" column is greater than the specified value. FieldA is is of the data type DB_TYP_TIME.
- `FieldB`
   `like '`
  `tank`
  `%'`

  Then the data records for which the "FieldB" column contains the value "tank1" or "tank4" or "tank12" etc. are selected for example. FieldB is of the data type DB_TYP_CHAR.
- `FieldC`
   `> 100`

  With a condition of this type, all data records are selected for which the "FieldC" column contains a value greater than 100. FieldC is of the data type DB_TYP_INTEGER.
- `BETWEEN FieldC`
   `= 20 AND` 
  `FieldC = 200`

  The statement selects all data records for which the "FieldC" column contains a value between 20 and 200. FieldC is of the data type DB_TYP_INTEGER.
- `FieldD`

  Sorting then takes place by column "FieldD".
- `FieldE desc`

  Sorting then takes place by column "FieldE" in reverse alphabetical order (descending order).

---

**See also**

[SQL keywords (RT Professional)](#sql-keywords-rt-professional)

### SQL keywords (RT Professional)

#### SQL keywords

> **Note**
>
> Do not use the following terms and keywords of the SQL language as names for a recipe, recipe query or recipe element:
>
> - "Archive"
> - "View"
> - "Field"
> - "ViewCol"

| Keywords of the SQL language |  |  |  |
| --- | --- | --- | --- |
| add | all | alter | and |
| any | as | asc | begin |
| between | binary | break | by |
| call | cascade | cast | char |
| char_convert | character | check | checkpoint |
| close | comment | commit | connect |
| constraint | continue | convert | create |
| cross | current | cursor | date |
| dba | dbspace | deallocate | dec |
| decimal | declare | default | delete |
| desc | distinct | do | double |
| drop | else | elseif | encrypted |
| end | endif | escape | exception |
| exec | execute | exists | fetch |
| first | float | for | foreign |
| from | full | goto | grant |
| group | having | holdlock | identified |
| if | in | index | inner |
| inout | insert | instead | int |
| integer | into | is | isolation |
| join | key | left | like |
| lock | long | match | membership |
| message | mode | modify | named |
| natural | noholdlock | not | null |
| numeric | of | off | on |
| open | option | options | or |
| order | others | out | outer |
| passthrough | precision | prepare | primary |
| print | privileges | proc | procedure |
| raiserror | readtext | real | reference |
| references | release | remote | rename |
| resource | restrict | return | revoke |
| right | rollback | save | savepoint |
| schedule | select | set | share |
| smallint | some | sqlcode | sqlstate |
| start | stop | subtrans | subtransaction |
| synchronize | syntax_error | table | temporary |
| then | time | tinyint | to |
| tran | trigger | truncate | tsequal |
| union | unique | unknown | update |
| user | using | validate | values |
| varbinary | varchar | variable | varying |
| view | when | where | while |
| with | work | writetext |  |

---

**See also**

[SQL language (RT Professional)](#sql-language-rt-professional)

## Configuring Recipes (RT Professional)

This section contains information on the following topics:

- [General configuration procedure (RT Professional)](#general-configuration-procedure-rt-professional)
- [Creating a New Recipe (RT Professional)](#creating-a-new-recipe-rt-professional)
- [Creating Recipe Elements and Data Records (RT Professional)](#creating-recipe-elements-and-data-records-rt-professional)
- [Importing recipes into the configuration and exporting them again (RT Professional)](#importing-recipes-into-the-configuration-and-exporting-them-again-rt-professional)
- [Procedure for changing the recipe structure (RT Professional)](#procedure-for-changing-the-recipe-structure-rt-professional)
- [Creating recipe queries (RT Professional)](#creating-recipe-queries-rt-professional)

### General configuration procedure  (RT Professional)

#### Configuring steps

Follow the steps outlined below to create a recipe:

| Step | Task |
| --- | --- |
| 1 | Define the structure of the recipe. |
| 2 | Define the communication mode for the recipe. |
| 3 | Define the control tags or raw data tags according to the communication mode selected. |
| 4 | Create the recipe and define its properties. |
| 5 | Create the recipe elements in accordance with the structure planned. |
| 6 | Create the recipe data records. |
| 7 | Configure views of multiple recipes, if required. |
| 8 | Configure a screen which contains a recipe view and interconnect this recipe view with the recipe or view.  Or:  Configure a screen which contains I/O fields and buttons. Configure button functions for reading and writing the values of recipe data records. |

> **Note**
>
> **Runtime API**
>
> The Runtime API provides you with extensive uaArchive functions to edit recipes and recipe queries (see section "Interfaces > Runtime API", subsection "[Recipe functions](Runtime%20API%20%28RT%20Professional%29.md#recipe-functions-rt-professional)").

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Creating a New Recipe (RT Professional)](#creating-a-new-recipe-rt-professional)
  
[Creating recipe queries (RT Professional)](#creating-recipe-queries-rt-professional)
  
[Recipe functions (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#recipe-functions-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Creating a New Recipe (RT Professional)

#### Introduction

Create the new recipes using the "Recipes" tab of the "Recipes" editor.

#### Naming the recipe

Do not use keywords or reserved words of the SQL database language for recipe names (see section "[SQL keywords](#sql-keywords-rt-professional)").

#### Recipes with date or time stamp

If you use data or time data, make sure that the system setting for time and date on the configuring computer matches that on the target system. Example: You load a recipe data record on the target system at 13:55 in which the processing time 14 h is stored. If it already 14:05 on the target computer, the recipe will not be processed. If an operator processes the recipe, modification information is not written back correctly into the database.

After loading to the target system, check the recipes with date or time stamps on the target system.

#### Requirement

- You have created the control tags or the raw data tag.
- The "Recipes" editor is open.

#### Procedure

Create a recipe as follows:

1. Double-click the first empty table row in the "Recipes" tab of the "Recipes" editor.
2. Select "Properties > General > Settings > Name" in the Inspector window and enter a descriptive recipe name.

   The name identifies the recipe uniquely within the project.

   ![Procedure](images/97444313611_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97444313611_DV_resource.Stream@PNG-en-US.png)
3. Select the "Display name" field to enter the language-specific name to be displayed in Runtime.
4. Define whether or not the recipe data records are limited to a specified maximum number in the area "Size" under "Type".
5. If the size type is limited, specify the maximum number of recipe data records of a recipe under "Number of data records".
6. Specify the "Communication type" under "Properties > Communication":

   - If you have selected "Raw data tag", create a raw data tag and select it under "Raw data tag".
   - Select "No communication" if you use the recipe only to save project data.

     ![Procedure](images/97446299531_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/97446299531_DV_resource.Stream@PNG-en-US.png)
7. Select the control tags for access to the recipe under "Properties > Control tags" if you have selected the "Tags" communication type.

   ![Procedure](images/97449078539_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97449078539_DV_resource.Stream@PNG-en-US.png)
8. Define under "Properties > Security" which operator authorizations have read and write access to the recipe in Runtime.

   ![Procedure](images/97449295755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97449295755_DV_resource.Stream@PNG-en-US.png)
9. Under "System fields", specify whether to display the "Last access" and "Last user" entries in Runtime.

#### Result

You have created the recipe.

---

**See also**

[General configuration procedure (RT Professional)](#general-configuration-procedure-rt-professional)
  
[Creating Recipe Elements and Data Records (RT Professional)](#creating-recipe-elements-and-data-records-rt-professional)
  
[Importing recipes into the configuration and exporting them again (RT Professional)](#importing-recipes-into-the-configuration-and-exporting-them-again-rt-professional)
  
[SQL keywords (RT Professional)](#sql-keywords-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Creating Recipe Elements and Data Records (RT Professional)

#### Introduction

Select the "Recipe elements" tab in the bottom area of the "Recipes" editor to set up the elements for the selected recipe. You can also enter the recipe element values in the "Recipe data records" tab.

#### Requirement

- The tags for the recipe have been created.
- You have created the recipe.
- The recipe is selected in the "Recipes" editor.

#### Procedure

Create a recipe element as follows:

1. Double-click the first empty table row in the "Recipe elements" tab.
2. Select "Properties > General > Settings > Name" in the Inspector window and enter a descriptive name for the recipe element. This name must be unique within a recipe.
3. Select the "Display name" to enter the language-specific name to be displayed in Runtime.

   ![Procedure](images/97453961099_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97453961099_DV_resource.Stream@PNG-en-US.png)
4. When the recipe has the "Tags" communication type:

   To link the recipe element to a tag, select a tag under "Properties > Basic settings > Settings". The data type will be displayed below.
5. For a "String" data type, also specify the maximum length of the string under "Data length". The "Settings" area on the right shows the value range for number-based data types, for which you can also specify a default value.

   ![Procedure](images/111899618699_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111899618699_DV_resource.Stream@PNG-en-US.png)
6. When the recipe has the "Raw data tag" communication type or "No communication": Select the "Data type" and also the "Data length" of the recipe element for the "String" data type.
7. Define under "Properties > Security" which operator authorizations have read and write access to the recipe element in Runtime.
8. Define in "Properties > Extras" which conditions the values of the recipe element must satisfy. For faster search, the values can be indexed:

   ![Procedure](images/97453268491_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97453268491_DV_resource.Stream@PNG-en-US.png)
9. Double-click the first empty table row in the "Recipe data records" tab to set up a recipe data record.
10. Enter the desired value for the recipe element in the table editor.

**Note**

You cannot connect recipe elements to tags of the data type "DateTime".

#### Result

The recipe element and a corresponding recipe data record are created with one value.

---

**See also**

[Creating a New Recipe (RT Professional)](#creating-a-new-recipe-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Importing recipes into the configuration and exporting them again (RT Professional)

#### Introduction

You can export recipes as a CSV file and import them again into the configuration.

> **Note**
>
> You cannot import or export data records from recipe queries.

#### Application case

You export recipe data to store and back up recipe data long-term on a computer.

You export the recipe data to an HMI device to standardize and distribute recipe data. You change the CSV file Microsoft Excel and import the CSV file to all HMI devices which require the same recipe data.

You want to exchange recipe data between different projects. You change the recipe data in Runtime. To transfer the changed recipe data to WinCC ES, export the recipe data records to Runtime and copy the CSV file to the configuring computer. There you import the CSV file containing the recipe data records into the recipe. And in the opposite direction, you transfer the modified recipe data records to the HMI device in WinCC ES in Runtime.

#### Requirement

- You have created the recipe.
- The structures of the exported CSV file and the recipe in WinCC ES match; name, number and data type of the recipe elements are identical.
- The "Recipes" editor is open.

#### Importing CSV files

To import recipe data records into a recipe, proceed as follows:

1. Select the row which contains the desired recipe in the "Recipes" tab.
2. Select the "Import recipe data" command from the shortcut menu.

   The "Import" dialog box opens.

   ![Importing CSV files](images/67209738123_DV_resource.Stream@PNG-en-US.png)

   ![Importing CSV files](images/67209738123_DV_resource.Stream@PNG-en-US.png)
3. Select the desired CSV file with the recipe data under "File name".
4. Under "Strategy", define whether a recipe data record in the CSV file overwrites an existing recipe data record in WinCC with the same recipe data record number.
5. Click "Import" to start the operation.

#### Result

The recipe will be amended by recipe data records from the CSV file that have not yet been entered. If the option is selected, existing recipe data records will be overwritten.

An error message is shown in the "Info" of the Inspector window if the structure of the recipe does not match the structure of the CSV file.

#### Exporting CSV files

1. Select the row which contains the recipe to export in the "Recipes" tab.
2. Select the "Export recipe data" command from the shortcut menu.

   The "Export" dialog box opens.

   ![Exporting CSV files](images/67209742603_DV_resource.Stream@PNG-en-US.png)

   ![Exporting CSV files](images/67209742603_DV_resource.Stream@PNG-en-US.png)
3. Select a path for the CSV file under "File name".
4. Select the desired recipe under "Recipe name".
5. Select all recipe data records or limit the selection to certain recipe data record numbers under "Select content".
6. Click "Export" to start the operation.

#### Result

The configuration is exported as a CSV file. The list separator is the semicolon "RecipeElement_1;RecipeElement_2". The decimal separator is a period, e.g. "3.14".

---

**See also**

[Creating a New Recipe (RT Professional)](#creating-a-new-recipe-rt-professional)

### Procedure for changing the recipe structure (RT Professional)

#### Introduction

Different recipe structures can occur in the following situations:

- Due to changes during commissioning
- If a machine is upgraded by the machine manufacturer (retrofit)
- When CSV files are imported, the structure of the CSV file can differ from the recipe structure.

Nevertheless, you can still use any recipe data records already created.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| When a tag is renamed, the assignment is lost. |  |

#### Effects

If the structure of the CSV file differs from the structure of the recipe, deviations are handled as follows:

- If the old recipe data record or the CSV file contains additional values, these values will be discarded.
- If the old recipe data record or the CSV file contains values of the wrong data type, the configured default value will be used in the recipe data record.

  Example: The recipe data record contains values that show the tank contents and were input as floating point numbers. However, the corresponding recipe tag expects an integer value. In this case, the system discards the transferred value and the configured default value is used.
- If the old recipe data record or the CSV file contains too few values, the configured default value will also be used in the recipe data record.

### Creating recipe queries (RT Professional)

#### Introduction

A recipe query is a set of recipe elements from various recipes. Example: Recipe query "Water consumption":

- Water from the "Fruit juice drink" recipe
- Water from the "Juice" recipe
- Water from the "Nectar" recipe

You can link recipe elements to form relations, such as "Nectar.Water > FruitJuiceDrink.Water". In the recipe query, only the data records that satisfy the relation are displayed in Runtime. In the example, these are the records in which the water requirement of the "Nectar" recipe is greater than that of "Fruit juice drink".

You can assemble recipe queries from recipe elements in the "Recipes" editor in the "Recipe queries" tab. Select the recipe elements from the recipes that are included in the recipe query and set their relation. The relation expresses a condition. Only those combinations of recipe elements which satisfy the condition (true) are displayed in the recipe view.

You can also edit the recipe query data in Runtime. The data you have edited are applied to the original recipe in Runtime.

The recipe query does not support the following actions:

- Creating new recipe data
- Deleting recipe data

#### Requirement

- You have created at least two recipes.
- The recipes are in the same database on the same HMI device.
- The recipes have at least one identical recipe element in the same data format.

#### Creating recipe queries

Create a recipe query as follows:

1. In the "Recipes" editor, double-click the first empty table row in the "Recipe queries" tab.

   A new recipe query is created.
2. In the inspection window, enter a name for the recipe query under "Properties > General > Name " to indicate its function.

   ![Creating recipe queries](images/100708744459_DV_resource.Stream@PNG-en-US.png)

   ![Creating recipe queries](images/100708744459_DV_resource.Stream@PNG-en-US.png)
3. Select the "Display name" to enter the language-specific name to be displayed in Runtime.

#### Creating recipe query elements and relations

To create a new element for the recipe query and the relation, follow these steps:

1. Double-click on the first free table row in the "Recipe query elements" tab.
2. Under "Properties > General > Recipe element", select the recipe element to insert into the query.
3. Create other recipe query elements as required.
4. Select the recipe query in the "Recipe queries" index.
5. Select a recipe query element and the desired operator as a left and right operand in the Inspector window under "Properties > Relation > Relation".

   ![Creating recipe query elements and relations](images/61731071883_DV_resource.Stream@PNG-en-US.png)

   ![Creating recipe query elements and relations](images/61731071883_DV_resource.Stream@PNG-en-US.png)
6. Click the "Add" button.

   The relation appears under "Condition". If a condition was already defined there, the new relation with the logical operator "AND" is added. You can edit the condition.
7. Change the order of the recipe query elements as required using drag-and-drop.

#### Result

The recipe query is created and a condition is defined. Only those combinations of recipe elements which satisfy the condition are displayed.

![Result](images/61731258251_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[General configuration procedure (RT Professional)](#general-configuration-procedure-rt-professional)

## Configuring the visualization of recipes  (RT Professional)

This section contains information on the following topics:

- [Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
- [Properties of the recipe view (RT Professional)](#properties-of-the-recipe-view-rt-professional)
- [Configuring a recipe view (RT Professional)](#configuring-a-recipe-view-rt-professional)
- [Exporting recipe data in runtime (RT Professional)](#exporting-recipe-data-in-runtime-rt-professional)
- [Importing recipe data (RT Professional)](#importing-recipe-data-rt-professional)
- [Configuring persistence (RT Professional)](#configuring-persistence-rt-professional)

### Displaying recipes (RT Professional)

#### Introduction

Recipes and recipe queries are displayed on the HMI device as follows:

- In a recipe view
- In individual I/O fields

#### Recipe view

The recipe view displays the recipes and queries in tabular format. Each recipe data record uses one line.

The picture below contains an example of a recipe view.

![Recipe view](images/22296151435_DV_resource.Stream@PNG-en-US.png)

Operators use the recipe view in Runtime and, for example, create new data records or import recipes. You transfer a recipe data record to the recipe tags and vice versa with two buttons in the recipe view.

> **Note**
>
> You select a recipe or recipe query when configuring a recipe view. The operator can change the selection and other properties in Runtime.

> **Note**
>
> **Data source**
>
> The recipe view only accesses one recipe or recipe query respectively.
>
> **Recipe query**
>
> An operator can only change the displayed recipe data in Runtime. The creation and deletion of data records and their transfer from/to the PLC is not possible.

#### Recipes in the screen

You can show recipe elements in I/O fields alternatively instead of a preconfigured recipe display. The following screen shows an example for a screen with configured I/O fields in the "Tags" communication type.

![Recipes in the screen](images/111901232011_DV_resource.Stream@PNG-de-DE.png)

The blue fields at the top show the values of the recipe tags which have a communication connection with the PLC. The yellow fields at the bottom show the contents of the four control tags. In the example the blue recipe values were written into recipe data record number 3 (task = 6) and the number of errors = 0 returned.

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Properties of the recipe view (RT Professional)](#properties-of-the-recipe-view-rt-professional)
  
[Configuring a recipe view (RT Professional)](#configuring-a-recipe-view-rt-professional)
  
[Control tags (RT Professional)](#control-tags-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Properties of the recipe view (RT Professional)

#### Introduction

The recipe view visualizes recipe elements in table format on the screens. Operators can edit recipe data in the recipe view in Runtime.

#### Configuration of the recipe view

The following optional recipe view configurations are available:

- General > Display: You select a recipe or recipe query as a data source and define whether recipe data records can be edited, inserted or deleted.
- General > Print job

  The recipe view is automatically linked by logical operation with the system print job for recipe views. Create a logical link to the recipe view for any custom print jobs or system print jobs.
- General > Time

  Define the time base for the "Last access" display, for example the coordinated universal time (UTC). You can include the time base selected for output in Runtime.
- Appearance, layout, text format

  You define colors and design, size and position of the recipe display, font type and font size.
- Window

  You define the font size, window header of the recipe display and other window properties.
- Table

  You define the appearance of the column headers, table and boundary lines and the behavior for selecting and sorting data records.
- Table > Mark

  Determine whether lines or only cells can be marked with the mouse.

  Configure the properties of the selection rectangle which can be shown around the marked cells or lines of the table.

  Configure the marking colors for the markable cells and/or lines as required. The color defined by the system for the marking is used with the "Automatic coloring" property.
- Table > Sorting

  Determine whether sorting is to take place and if so, with click or double-click on the column header. Define the order of sorting which is to run cyclically when clicking or double-clicking the column header: either sorting ascending - descending or ascending - descending - no sorting

  Configure the sorting symbol and sorting index which are to be shown right-justified in the column header. You show sorting sequence and sorting order of the columns.

  If you activate the "Use sorting key" option, the sorting symbol is displayed as a sorting key above the vertical scrollbar. Click this sorting button to sort the selected column based on the configured sorting criteria. The sorting button is not displayed if the table does not contain a vertical scroll bar.
- Columns

  You determine which recipe elements are displayed in what order in Runtime. You apply write protection to certain elements and determine the width and formatting.

  Some columns can also show the content and header as symbols. Determine how these columns are displayed in the "Layout" field. The text and symbol can be displayed together.
- Filter

  As a filter criterion you define a condition for a recipe element and link several conditions. The data record is not displayed until all the filter criteria are satisfied.
- Toolbar

  In addition to the appearance of the toolbar you define which buttons are visible in what order in Runtime and with what operator authorization they can be operated.

  Activate the buttons in the list which you need for operating the WinCC-Control in Runtime. Information about the function of the individual buttons can be found in the subsection "Operation in Runtime"

  Define a hotkey for a button if necessary.

  If you assign operator authorizations to the individual buttons, the button is only released in Runtime for the users who have the appropriate operator authorization.

  If you deactivate the "Active" option for a button, the activated button is displayed in Runtime but cannot be operated.
- Status bar

  In addition to the appearance of the status line, you define what information is displayed in the status line in Runtime, e.g. the recipe data record number.
- Data export

  A standard file name and a standard directory are already entered by switch tags. However, you can assign your own file names and directory names.

  You can use the following switch tags.

  @OBJECTNAME: Object name of the recipe display, see "Properties > Miscellaneous"

  @PROJECTPATH: Project directory

  @CURRENTDATE: Current date

  @CURRENTTIME: Current time
- Security

  You determine whether and how changes to the properties of the recipe display can be saved in Runtime and after a screen change and which authorization is necessary for changing.
- Miscellaneous

  You define the visibility and layer for the recipe display.

---

**See also**

[Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Configuring a recipe view (RT Professional)

#### Requirement

- You have created a recipe or a recipe query.
- A screen is created and open in the "Screens" editor.

#### Procedure

Configure a recipe view as follows:

1. Drag the "Recipe display" object from the "Controls" palette of the "Tools" task card into the screen.
2. Select the desired recipe or recipe query in the Inspector window under "General > Display".

   ![Procedure](images/111903672587_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111903672587_DV_resource.Stream@PNG-en-US.png)
3. Define the write and read rights for the recipe display in Runtime under "General > Allow in Runtime".
4. Select "Appearance," "Layout," and "Text format" to define additional display options for the recipe view.
5. Select "Properties" > Columns" to define the recipe elements which will be visible and write-protected in Runtime.

   ![Procedure](images/111904447755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111904447755_DV_resource.Stream@PNG-en-US.png)
6. Select "Toolbar" to define the recipe view buttons to be available in Runtime.

   ![Procedure](images/111905185035_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111905185035_DV_resource.Stream@PNG-en-US.png)
7. Select "Status bar" to define the scope of information to display in the status bar in Runtime.

   ![Procedure](images/111906242059_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111906242059_DV_resource.Stream@PNG-en-US.png)
8. Select "Filter" to define the filter criteria for recipe elements in Runtime.
9. Select "Sort" to define the sorting criteria for recipe elements in Runtime.

**Note**

Some columns can also show the content as symbol. In "Content as", determine how these columns are displayed. Text and symbol can also be displayed together.

#### Result

The recipe view is configured.

---

**See also**

[Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Exporting recipe data in runtime (RT Professional)

#### Introduction

In Runtime you export the recipe data with a button in the recipe display. You configure operation of the data export in Runtime.

#### How to configure the operation of the data export

1. Define a file name and a directory for the export file under "Properties > Data export".

   The file name may be made up of names you select yourself and the following switch tags:

   @OBJECTNAME: Object name of the recipe display

   @PROJECTPATH: Project directory

   @CURRENTDATE: Current date

   @CURRENTTIME: Current time

1. Define the file extension, e.g. "CSV".
2. Define the scope of the data export:

   - All Runtime data are exported.
   - Selected Runtime data are exported.
3. Configure the operation of the data export during runtime. Define:

   - The "Data export defaults" are displayed in runtime.
   - The user may change the file name or the directory.
4. If "Show dialog" is deactivated, the data are exported immediately to the defined export file on pressing the "Export log" button.
5. Save the project.
6. Activate the "Export log" button under "Properties > Toolbar".

#### Results

In Runtime you can export all or selected recipe data to a defined file with the ![Results](images/9490994187_DV_resource.Stream@PNG-de-DE.png) button.

### Importing recipe data (RT Professional)

#### Introduction

You can import runtime recipe data that originates from a WinCC database back to a recipe.

To enable an unambiguous assignment of the imported recipe data when importing, data record IDs have been entered for the recipe data during the import. If WinCC detects during the import that an ID to be imported already exists in the recipe, an error message is generated along with an entry in the log file "UALogFile.txt". Data with a new data record ID is added as new data records in the recipe.

#### Requirement

- The file you want to import contains no information regarding data type and number of fields.
- Therefore, the import data and the target recipe must have the same structure.  
  Or, alternatively, import the data into the recipe from which you exported it previously.

> **Note**
>
> You have edited the exported runtime data of a recipe outside of WinCC and want to now overwrite the data of this recipe. If you want to import the modified data, you must first delete all data records of the recipe. Otherwise, error messages are output during the import due to the same data record IDs.

> **Note**
>
> If in a client-server project the recipe is located on the server, e.g. in "c:\Projects\Test\UA", the recipe is enabled in this default path. The client maps the enable via a network drive, e.g. "I:\Test\UA". The default path of the recipe is, thus, on the client "I:\Test\UA". This directory exists, but not under this name on the server. If you want to import recipe data to the client, you must changed the default path on the client (in the example to "C:\Projects\Test\UA").

#### Requirement

- A CSV file containing at least one recipe has been created.
- The WinCC project for import is open.
- The "Recipes" editor is open with at least one recipe.

#### Importing recipe data

1. In the "Recipes" editor, select the recipe with the data records you want to import.
2. Click ![Importing recipe data](images/70960625547_DV_resource.Stream@PNG-de-DE.png).

   The "Import" dialog box opens.

   ![Importing recipe data](images/22618278667_DV_resource.Stream@PNG-en-US.png)

   The selected recipe is displayed under "Recipe name".
3. Select the file you want to import under "File name".
4. Under "Strategy", specify if existing data records should be overwritten by records of the same name.
5. Click "Import".

   > **Note**
   >
   > **No check of import file for inconsistencies**
   >
   > The import function doesn't check whether values that were changed in the CSV file between the export and import are still valid, e.g. whether these are still within the defined limits.

   The import will start.

#### Result

The data is loaded into the user archive.

#### Import of configuration data of recipes and views

To import configuration data of recipes and views, select the command "Edit" > "Import" in the main menu of the WinCC Configuration Studio.

### Configuring persistence (RT Professional)

#### Introduction

A user can configure WinCC-Controls in Runtime. You define what effect the online configuration has in Runtime.

The changes configured in Runtime are saved separately from the screen in the engineering system. The screen is thus retained in its original configuration.

#### Procedure

1. Select "Properties > Safety > Persistence > Online configuration" which you can only operate in the engineering system. The online configuration can then be defined permanently in Runtime:

   - "No persistence" The online configurations are not retained in Runtime. This default leaves the user no option in Runtime. The online configurations are lost the next time the screen changes and with deactivate/activate.
   - "Persistence" This default leaves the user the options of "reject", "retain" or "reset". With the "retain" option the online configurations are retained the next time the screen changes and with deactivate/activate.
   - "Persistence in Runtime". This default leaves the user the options of "reject", "retain" or "reset". With the "retain" option the online configurations are retained the next time the screen changes but are lost when the project is deactivated/activated.
2. Define what operator authorization the user must have to carry out online configuration.
3. "Screen change characteristics" can be operated in the engineering system and in Runtime with the defaults "Persistence" and "Persistence during Runtime". The "reset" option can only be operated in Runtime because the original configuration is in the engineering system.  
   Select one of the three effects of the online configuration in the next screen change:

   - Activate "Reject changes" so that the online configuration only exists for as long as the screen is selected. The changes are rejected at the next screen change. The recipe display appears as configured if you select the screen again.
   - Activate "Retain changes" so that the online configuration is not lost at the next screen change.
   - Activate "Reset" so that the configured screen is saved again in Runtime. All online configured changes are lost.
4. Save the configuration.

**Note**

In case of a user change, the different configurations are not saved until you have executed a screen change.

**Note**

The screen is also replaced in Runtime when saving the screen or in Delta compiling (change loading). All online configured changes are lost.

## Data transfer to the PLC (RT Professional)

This section contains information on the following topics:

- [Data transfer basics (RT Professional)](#data-transfer-basics-rt-professional)
- [Raw data tag (RT Professional)](#raw-data-tag-rt-professional)

### Data transfer basics (RT Professional)

This section contains information on the following topics:

- [Overview (RT Professional)](#overview-rt-professional)
- [Control tags (RT Professional)](#control-tags-rt-professional)
- [Differences between data formats (RT Professional)](#differences-between-data-formats-rt-professional)

#### Overview (RT Professional)

The options for transferring recipe values between the PLC and HMI device are as follows:

- No data transfer
- "Tags" communication type
- "Raw data tag" communication type

##### No data transfer

The recipe is not used for transferring recipe data to the PLC but as a data memory and user log: You store values which belong together in data records to which you have multiple access. In the simplest case an operator switches between the recipes in a recipe view. The respective recipe data are loaded into the recipe tags and processed further there.

##### "Tags" communication type

Recipe tags transfer the recipe values to the PLC. Vice versa the values from the PLC are written into a recipe data record by recipe tags. Control tags control the data transfer. The following tasks are started automatically by the desired entry into the corresponding control tags.

- Write data records into the recipe tags and therefore into the PLC
- Read data records out of the recipe tags and therefore out of the PLC
- Delete data records
- Create new data records

  > **Note**
  >
  > A complete data record is always transferred in the "Tags" communication type. You cannot transfer recipe data from a recipe query.

##### "Raw data tag" communication type

The automation system sends the raw data tag as a message frame to the HMI device as an active partner. The message frame contains the following:

- Desired target recipe
- Desired target recipe data records
- Job e.g. "Read", "Write" or "Delete"
- New recipe values, e.g. for "Write" job

The HMI device returns recipe and acknowledgement data as a message frame.

The "BSEND/BRCV" function of the S7 communication is used for the data exchange. The consecutive number of the recipe serves to identify the recipe uniquely in the PLC (PLCID).

The PLC requires a user program which executes the following in Runtime:

- Collect data if necessary via I/O fields in the HMI device.
- Check data.
- Create raw data tag as a message frame.
- Send message frame.

If you want to start creation of the message frame from the HMI device, you configure functions in the screen which start the user program.

> **Note**
>
> The following is possible in the "Raw data tag" communication type:
>
> - Transfer of an individual recipe element
> - Transfer of an entire recipe data record
> - Transfer of multiple recipe data records
>
> Data transfer from the recipe view or by control tags is not possible.

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Data Transfer via Raw Data Tags (RT Professional)](#data-transfer-via-raw-data-tags-rt-professional)
  
[Control tags (RT Professional)](#control-tags-rt-professional)
  
[Differences between data formats (RT Professional)](#differences-between-data-formats-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

#### Control tags (RT Professional)

##### Introduction

With the "Tags" communication type in the recipe, you transfer the recipe data between the PLC and the HMI device using recipe tags. The data transfer is controlled by four control tags which are assigned fixed to a recipe. Other control tags can be assigned to another recipe.

Data transfer is started automatically once you have entered the required value at the corresponding control tag.

> **Note**
>
> All four control tags must always be specified in a recipe to ensure that it works. Do not change the data type of the control tags.

> **Note**
>
> You must implement access protection for the control tags of a protected recipe separately using the object properties of the screen, I/O field or button, for example.

##### Control tags

| Control tag | Required data type | Meaning |  |
| --- | --- | --- | --- |
| ID | Long | Number of the recipe data record within the assigned recipe |  |
| Job | Long | Read out of the recipe tags, write into the recipe memory: | 6 |
| Read out of the recipe memory, write into the recipe tags: | 7 |  |  |
| Delete in the recipe memory: | 8 |  |  |
| After the job has been carried out, an error ID can be seen in the "Job" control tag: |  |  |  |
| No error | 0 |  |  |
| Error | -1 |  |  |
| Field | String | The name of the recipe element Make sure that you do not use the display name. |  |
| Value | String | The value of the recipe element |  |

##### Requirement

- Communication type is set to "Tags" in the recipe.
- You have configured a process screen with all I/O fields required for process tags and control tags of the recipe.

  Example:

  ![Requirement](images/111901232011_DV_resource.Stream@PNG-de-DE.png)

##### Inserting the control tag

The following control tag combinations are supported:

- "ID" and "Job" control tags

  The control tag "ID" indicates the number of the recipe data record which is transferred.

  The "Job" control tag indicates whether the selected recipe data record is written, read or deleted (6, 7, 8) in the recipe memory of the HMI device.
- "Job", "Field" and "Value" control tags

  The recipe data record is selected for the data transfer whose recipe element "Field" has the recipe value "Value". Example field = "Water", value = "5 liters".

  The "Job" control tag indicates whether the selected recipe data record is written, read or deleted (6, 7, 8) in the recipe memory of the HMI device.

  > **Note**
  >
  > Different data records may not contain the same recipe value in the "Field" recipe element You have to activate the "Unique values" checkbox under "Properties > Options" for the recipe element. Otherwise no clear assignment of the recipe data record by the value is possible and the first data record which satisfies the "Value in field" condition is used.

##### More combinations of values for the "ID" and "Job" control tags

| ID | Job = 6 | Job = 7 | Job = 8 |
| --- | --- | --- | --- |
| -1 | Data record from the recipe tags is read and appended **to the end** in the recipe in the recipe memory. | - | Data record with the **lowest** ID is deleted in the recipe in the recipe memory. |
| -6 | Data record from the recipe tags is read and written into the recipe data record with the **lowest** ID in the recipe. | Data record with the **lowest** ID is written in the recipe into the recipe tags. | Data record with the **lowest** ID is deleted in the recipe in the recipe memory. |
| -9 | Data record from the recipe tags is read and written into the recipe data record with the **highest** ID in the recipe. | Data record with the **highest** ID is written in the recipe into the recipe tags. | Data record with the **highest** ID is deleted in the recipe in the recipe memory. |

---

**See also**

[Overview (RT Professional)](#overview-rt-professional)
  
[Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
  
[Using the recipe screen (RT Professional)](#using-the-recipe-screen-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

#### Differences between data formats (RT Professional)

##### Introduction

The data formats in WinCC conform to the Intel and Microsoft data formats. The least significant byte is saved first and the most significant byte is saved last. This data format is very common and is generally known as the "Intel format".

The data formats in WinCC differ fundamentally from the data formats in the PLCs.

##### Intel format

In the Intel format, the decimal number 300 is stored as follows:

| Bit | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Hex | 0 | 1 | 2 | C |

According to the Intel Format, the decimal number 300 corresponds to the hex-number 12C (1*256 + 2*16 + 12*1).

##### SIMATIC format

In SIMATIC format, the least significant byte is are stored in the most significant digits. In SIMATIC format, decimal number 300 is stored as follows:

| Bit | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Hex | 2 | C | 0 | 1 |

According to the SIMATIC format, decimal number 300 corresponds to hex number 2C01.

If hex number 2C01 is interpreted according to Intel format, it corresponds to decimal number 11265.

There are function blocks that convert the data for PLCs from the SIMATIC S7 series. You must always call up the blocks before and after data transfers between the PLC and WinCC. The function blocks are available for download from the Siemens Customer Support website in the Internet. The compressed file ANSI_S5.EXE is then loaded. ANSI_S5.EXE contains the "IEEE:GP" function block.

Active sending is described in the reference manuals for the PLCs or CPs (communication processors).

---

**See also**

[Overview (RT Professional)](#overview-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Raw data tag (RT Professional)

This section contains information on the following topics:

- [Basics on data transfer via raw data tags (RT Professional)](#basics-on-data-transfer-via-raw-data-tags-rt-professional)
- [Message Frame Structure for Jobs (RT Professional)](#message-frame-structure-for-jobs-rt-professional)
- [Message Frame Format for Acknowledgements (RT Professional)](#message-frame-format-for-acknowledgements-rt-professional)
- [Configuring raw data tag (RT Professional)](#configuring-raw-data-tag-rt-professional)

#### Basics on data transfer via raw data tags (RT Professional)

This section contains information on the following topics:

- [Data Transfer via Raw Data Tags (RT Professional)](#data-transfer-via-raw-data-tags-rt-professional)
- [Job types and error codes (RT Professional)](#job-types-and-error-codes-rt-professional)

##### Data Transfer via Raw Data Tags (RT Professional)

This section describes the transfer of recipe data between the HMI device, and PLC using raw data tags. The BSEND/BRCV function is used in the PLC. The message frame containing the raw data tag is actively sent by the PLC.

The message frames may contain one or more write or read jobs.

###### Data transfer procedure

1. The PLC sends the message frame to the HMI device.
2. The HMI device returns the following:

   - Data, if requested
   - A processing acknowledgement

The HMI device returns a separate acknowledgement for every job.

> **Note**
>
> The PLC is the active partner in this data transfer, so it is the PLC that must start the required function. On the HMI device, you can start the required function by means of a change in value of an external tag, for example, and the corresponding analysis in the PLC.
>
> Do not use the "Job type" parameter to start the data transfer. The "Job type" parameter used in the job, or acknowledgement header only works with respect to recipes.

> **Note**
>
> Raw data communication to an S7-300 is not possible.

---

**See also**

[General message frame structure (RT Professional)](#general-message-frame-structure-rt-professional)
  
[General Structure of an Acknowledgement Message Frame (RT Professional)](#general-structure-of-an-acknowledgement-message-frame-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

##### Job types and error codes (RT Professional)

###### Description of the job types

| Symbol | Meaning |
| --- | --- |
| **Type** | **Description** |
| 4 | The existence of the recipe is checked. |
| 5 | All data records are deleted from the recipe. |
| 6 | The data record is requested from the HMI device and is written to the PLC. |
| 7 | The data record from the PLC is written to the required data record. |
| 8 | The data record is deleted from the recipe. |
| 9 | The element of the required data record is requested from the HMI device and is written to the PLC. |
| 10 | The element of the required data record is written to the required data record. |

###### Description of the error codes

|  |  |  |  |
| --- | --- | --- | --- |
| **Group** | **No.** | **Description** | **Possible Fault Causes** |
| General | 0 | The function has been executed. | -- |
| Recipe | 2 | Data not available | No recipe configured with this PLCID. |
| Data record | 101 | Data not allowed | Recipe structure does not tally, such as number or type of fields. |
| Failed data record insertion or update.  Possible causes:  - Recipe is of the "limited" type. - A min. or a max. value is configured for a field. |  |  |  |
| Incorrect criterion |  |  |  |
| Data record | 102 | Data not available | For job type 6 only:  - No data available - Criterion is incorrect. |
| Field | 201 | Data not allowed | For job type 10 only:   Criterion is incorrect.  Possible causes:  - Field not found. - A min. or a max. value is configured for a field. |
| Field | 202 | Data not available | For job type 9 only:   - Criterion is incorrect. - No field found corresponding to criterion. |
| General | 254 | Function not found | -- |
| General | 255 | Undefined error | -- |

---

**See also**

[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

#### Message Frame Structure for Jobs (RT Professional)

This section contains information on the following topics:

- [General message frame structure (RT Professional)](#general-message-frame-structure-rt-professional)
- [Structure of the message frame header (RT Professional)](#structure-of-the-message-frame-header-rt-professional)
- [Structure of a job header (RT Professional)](#structure-of-a-job-header-rt-professional)

##### General message frame structure (RT Professional)

Structure of a message frame for sending jobs:

|  | Length |
| --- | --- |
| Message frame header | 16 bytes |
|  |  |
| Job header 1 | 12 bytes |
| Data for job 1 | n bytes |
|  |  |
| Job header 2 | 12 bytes |
| Data for job 2 | n bytes |
|  |  |
|  |  |
|  |  |
| Job header n | 12 bytes |
| Data for job n | n bytes |

###### Example

The total length of a message frame with a job, and 10 bytes of job data is 38 bytes.

16 bytes +12 bytes +10 bytes = 38 bytes

---

**See also**

[Data Transfer via Raw Data Tags (RT Professional)](#data-transfer-via-raw-data-tags-rt-professional)
  
[Structure of the message frame header (RT Professional)](#structure-of-the-message-frame-header-rt-professional)
  
[Structure of a job header (RT Professional)](#structure-of-a-job-header-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

##### Structure of the message frame header (RT Professional)

16 bytes are needed for a message frame header.

| Function of the field | Comment | Byte |
| --- | --- | --- |
| Message frame length in bytes LSB <sup>1</sup>) | Max. length 4091 bytes | 1 |
| Message frame length in bytes | 2 |  |
| Message frame length in bytes | 3 |  |
| Message frame length in bytes MSB <sup>2</sup>) | 4 |  |
| Transfer type | "1" from the HMI device   "2" from the PLC | 5 |
| Reserved |  | 6 |
| Number of jobs in the message frame LSB <sup>1</sup>) |  | 7 |
| Number of jobs in the message frame MSB <sup>2</sup>) |  | 8 |
| Number of the recipe (PLCID) | 1. character, in ASCII | 9 |
| Number of the recipe (PLCID) | 2. character, in ASCII | 10 |
| Number of the recipe (PLCID) | 3. character, in ASCII | 11 |
| Number of the recipe (PLCID) | 4. character, in ASCII | 12 |
| Number of the recipe (PLCID) | 5. character, in ASCII | 13 |
| Number of the recipe (PLCID) | 6. character, in ASCII | 14 |
| Number of the recipe (PLCID) | 7. character, in ASCII | 15 |
| Number of the recipe (PLCID) | 8. character, in ASCII | 16 |

| Symbol | Meaning |
| --- | --- |
| ① | Least significant byte |
| ② | Most significant byte |

> **Note**
>
> The number of the recipe is defined automatically in the "Recipes" editor during configuration, but can later be changed as needed. Enter the number in ASCII format in the message frame.

---

**See also**

[General message frame structure (RT Professional)](#general-message-frame-structure-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

##### Structure of a job header (RT Professional)

12 bytes are needed for a job header.

| Function of the field | Comment | Byte |
| --- | --- | --- |
| Job length in bytes LSB <sup>1</sup>) |  | 1 |
| Job length in bytes MSB <sup>2</sup>) |  | 2 |
| Job type | see   "Description of job types and error codes" | 3 |
| Reserved |  | 4 |
| Field number LSB<sup>1</sup>) |  | 5 |
| Field number MSB<sup>2</sup>) |  | 6 |
| Data record number LSB<sup>1</sup>) |  | 7 |
| Data record number |  | 8 |
| Data record number |  | 9 |
| Data record number MSB<sup>2</sup>) |  | 10 |
| Selection criterion LSB<sup>1</sup>) | Element value entered or element number as selection criterion. | 11 |
| Selection criterion MSB<sup>2</sup>) | not if 0 | 12 |

| Symbol | Meaning |
| --- | --- |
| ① | Least significant byte |
| ② | Most significant byte |

The field number corresponds to the consecutive number of the recipe element.

---

**See also**

[General message frame structure (RT Professional)](#general-message-frame-structure-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

#### Message Frame Format for Acknowledgements (RT Professional)

This section contains information on the following topics:

- [General Structure of an Acknowledgement Message Frame (RT Professional)](#general-structure-of-an-acknowledgement-message-frame-rt-professional)
- [Structure of an acknowledgment header (RT Professional)](#structure-of-an-acknowledgment-header-rt-professional)
- [Acknowledgement data (RT Professional)](#acknowledgement-data-rt-professional)

##### General Structure of an Acknowledgement Message Frame (RT Professional)

Structure of the acknowledgment message frame to the PLC:

|  | Length |
| --- | --- |
| Acknowledgement header | 24 bytes |
| Acknowledgement data |  |

---

**See also**

[Data Transfer via Raw Data Tags (RT Professional)](#data-transfer-via-raw-data-tags-rt-professional)
  
[Structure of an acknowledgment header (RT Professional)](#structure-of-an-acknowledgment-header-rt-professional)
  
[Acknowledgement data (RT Professional)](#acknowledgement-data-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

##### Structure of an acknowledgment header (RT Professional)

24 bytes are needed for an acknowledgement header

| Function of the field | Comment | Byte |
| --- | --- | --- |
| Message frame length in bytes LSB <sup>1</sup>) | Max. length 4091 bytes | 1 |
| Message frame length in bytes | 2 |  |
| Message frame length in bytes | 3 |  |
| Message frame length in bytes MSB <sup>2</sup>) | 4 |  |
| Transfer type | "1" from HMI device,  "2" from the PLC | 5 |
| Reserved |  | 6 |
| Job type | See  Description of "Job Types and Error Codes" | 7 |
| Error code | See  Description of "Job Types and Error Codes" | 8 |
| Reserved |  | 9 |
| Reserved |  | 10 |
| Field number LSB<sup>1</sup>) |  | 11 |
| Field number MSB<sup>2</sup>) |  | 12 |
| Data record number LSB<sup>1</sup>) |  | 13 |
| Record number |  | 14 |
| Record number |  | 15 |
| Data record number MSB<sup>2</sup>) |  | 16 |
| Number of the recipe (PLCID) | 1st character, in ASCII | 17 |
| Number of the recipe (PLCID) | 2nd character, in ASCII | 18 |
| Number of the recipe (PLCID) | 3rd character, in ASCII | 19 |
| Number of the recipe (PLCID) | 4th character, in ASCII | 20 |
| Number of the recipe (PLCID) | 5th character, in ASCII | 21 |
| Number of the recipe (PLCID) | 6th character, in ASCII | 22 |
| Number of the recipe (PLCID) | 7th character, in ASCII | 23 |
| Number of the recipe (PLCID) | 8th character, in ASCII | 24 |

| Symbol | Meaning |
| --- | --- |
| ① | Least significant byte |
| ② | Most significant byte |

---

**See also**

[General Structure of an Acknowledgement Message Frame (RT Professional)](#general-structure-of-an-acknowledgement-message-frame-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

##### Acknowledgement data (RT Professional)

The acknowledgement can contain the following:

- The required recipe data record
- The required content of the element
- No data

---

**See also**

[General Structure of an Acknowledgement Message Frame (RT Professional)](#general-structure-of-an-acknowledgement-message-frame-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

#### Configuring raw data tag (RT Professional)

This section contains information on the following topics:

- [Raw data tags of the "SIMATIC S7" channel (RT Professional)](#raw-data-tags-of-the-simatic-s7-channel-rt-professional)
- [Creating raw data tag (RT Professional)](#creating-raw-data-tag-rt-professional)
- [Raw data tag for BSEND/BRCV functions of S7 communication (RT Professional)](#raw-data-tag-for-bsendbrcv-functions-of-s7-communication-rt-professional)

##### Raw data tags of the "SIMATIC S7" channel (RT Professional)

###### Introduction

A tag of the type raw data type is a data telegram on a transport level. The contents of the raw data tag are not fixed and therefore only the sender and the receiver can interpret the transmitted data. There are no format changes in WinCC for this data type. Maximum length is 65535 Byte.

WinCC distinguishes between two types of raw data tags: Raw data tag for free application use and raw data tag for handling S7 functions.

###### Raw data tag for free application use

Raw data tags for free application use are used for transferring user data blocks between WinCC and PLC and handle only user data. It distinguishes between:

- Raw data tag as byte array
- Raw data tag for BSEND/BRCV functions

###### Raw data tag for handling S7 functions

These raw data tags do not have any channel-specific header and are normally used by the message system and for process data entry in WinCC.

No further description is needed here as these are tags and functions internal to the channel.

##### Creating raw data tag (RT Professional)

###### Procedure

1. Create a new connection, for example, "SIMATICS7".
2. In the "Parameters" tab, select "WinCC RT Prof connection > Send/receive raw data block".

   ![Procedure](images/100542129931_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/100542129931_DV_resource.Stream@PNG-en-US.png)
3. Under "Connection", specify the hexadecimal value of the connection ID for the connection resource that was assigned during the configuration of the controller.
4. Create a new tag "Raw data tag_1".

   ![Procedure](images/111908358923_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111908358923_DV_resource.Stream@PNG-en-US.png)
5. Select "SIMATICS7" as "Connection".
6. Select the "Raw" "Data type" and specify a sufficient "Length" in bytes.
7. Select "BSEND / BRCV" under "Raw data."

   ![Procedure](images/61886561675_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61886561675_DV_resource.Stream@PNG-en-US.png)
8. Specify the "R_ID" parameter, which was assigned in the configuration of the controller.
9. Create a new recipe.
10. In the Inspector window under "Properties > Communication" select "Raw data tag" as communication type and "Raw data tag_1" as raw data tag.
11. Create the recipe elements and recipe data records. Ensure that the recipe number matches the "PLC" field in the message frame.

##### Raw data tag for BSEND/BRCV functions of S7 communication (RT Professional)

###### Introduction

Raw data tags for "BSEND/BRCV" functions are used for transferring user data blocks between WinCC and AS and handle only user data.

This raw data type can be used to access the "BSEND/BRCV" functions of S7 communication. The functions are available in a S7-400 or a S7-300 using CP343. The initiative of data transfer always lies with the sending partner; hence "BSEND/BRCV" functions can also be used to implement event-controlled or sporadic data block transfers.

For resource reasons, it is advisable to keep the number of BSEND/BRCV raw data tags low.

**Resource limitations when using S7 functions "AR_SEND" and "BSEND/BRCV" for communication with S7-400**

The maximum data volume that can be sent simultaneously using AR_SEND and/or BSEND/BRCV functions from AS to WinCC is limited to 16 kByte.

Example:

- 1x BSEND with a max. of 16 Kbytes
- 1x AR_SEND with 8 kBytes + 1x BSEND with 8 kBytes
- 1x AR_SEND with 10 Kbytes + 1x AR_SEND with 2 Kbytes + 1x BSEND with 4 Kbytes

  > **Note**
  >
  > If the data block of a write job is transferred to AS and has not yet been deleted or fully deleted from the receiving buffer, then the next write job will be rejected with an error message. During such an error display, write jobs with R_ID > 0x8000 0000 are written to a connection-specific queue and the system tries to repeat the write job for 6 seconds.
  >
  > The responsibility for time co-ordination for transfer rests with the user and needs to be noted as shorter time intervals for write jobs.

###### Configuring a PBK Connection for Using "BSEND/BRCV" functions

"BSEND/BRCV" functions can only be used via a "hard-configured connection", a so-called PBK connection (programmed component communication). To configure a hard-configured connection, you must mention a connection resource (hex: 10 ... DF). This connection resource will be assigned by STEP 7 when the connection is configured within the PLC. The connection must be configured in AS as passive connection end-point.

A hard-configured connection can also be used to handle "normal" read and write jobs. If very large data areas are to be transferred via the connection, then the data blocks are transferred in multiple PDUs. For performance reasons, it would therefore be better to create a separate connection for "BSEND/BRCV" functions.

###### Raw data tag for "BSEND/BRCV" functions with the "R_ID" parameter

Raw data tags for transferring "BSEND/BRCV" data blocks are configured as raw data of type "BSEND/BRCV" with a "R_ID". The data length is derived implicitly from the sent or received data volume.

![Raw data tag for "BSEND/BRCV" functions with the "R_ID" parameter](images/61886561675_DV_resource.Stream@PNG-en-US.png)

A decimal value of 1 to 999999 must be specified for "R_ID". The R_ID is assigned at the time of configuration in AS and is used for distinguishing multiple data block transfers over one connection. The send and receive calls are always notified with reference to this R_ID in the underlying communication sub-system (SIMATIC Device Drivers). A raw data tag is thus assigned to one unique R_ID.

###### Sending a "BSEND/BRCV" raw data tag

Sending a "BSEND/BRCV" raw data tag takes place in the same way as writing a "normal" process tag. After sending the data block and receiving a positive acknowledgement from AS, the data block is transferred to the image of the Data Manager.

###### Receiving a "BSEND/BRCV" raw data tag

"BSEND/BRCV" raw data is sproradically sent to the channel on the initiative of the AS. Hence it is not possible to explicitly read S7 raw data tags.

The BSEND/BRCV mechanisms do not include any synchronization functions. If no user has logged in to receive the data during the start-up phase, the data blocks sent by AS will bounce on the receiver side. Hence, the user has to take care of the synchronization and, for example, release the sending direction on the AS by setting a flag with a data word.

## Operation in Runtime (RT Professional)

This section contains information on the following topics:

- [Recipe view (RT Professional)](#recipe-view-rt-professional)
- [Using the recipe screen (RT Professional)](#using-the-recipe-screen-rt-professional)
- [Mouse and keyboard operation (RT Professional)](#mouse-and-keyboard-operation-rt-professional)
- [Editing recipe data (RT Professional)](#editing-recipe-data-rt-professional)
- [Selecting and configuring data (RT Professional)](#selecting-and-configuring-data-rt-professional)
- [Select data (RT Professional)](#select-data-rt-professional)
- [Sorting data (RT Professional)](#sorting-data-rt-professional)

### Recipe view (RT Professional)

#### Functional scope

The recipe display offers access to user archives, the recipes and recipe queries.

In runtime, you can:

- Online configuration of recipe view

  The changes configured in runtime are saved separately from the screen in the configuration system on a user-specific basis. The screen is thus retained in its original configuration in the configuration system.
- Create, delete or modify new data records
- Scrolling in recipes
- Read and write tags for direct tag link
- Importing and exporting recipes
- Defining selection criteria to display only a certain part of the recipes
- Defining sorting conditions for the displayed recipe elements

  ![Functional scope](images/56795284107_DV_resource.Stream@PNG-en-US.png)

#### Properties

You connect a recipe view to a recipe or recipe query during the configuration. The online configuration and changing of selected recipe values in Runtime can be protected against unauthorized access respectively by own operator authorizations. If you cancel the access protection, you must reconnect the recipe view with the recipe in the configuration dialog box.

The access protection is queried when the recipe view screen opens.

- If the user has no authorization to read a recipe element, the corresponding column is not displayed in the table.

- If the user has no authorization to write a recipe element, the user cannot edit the data of the the corresponding column in the table.

Access protection for the control tags must be configured separately by the object properties, e.g. of a screen, an I/O field or a button.

### Using the recipe screen (RT Professional)

#### Introduction

You use the recipe screen with the control objects you have configured. The section describes the operation of the recipe screen with control tags from the section "[Control tags](#control-tags-rt-professional)".

> **Note**
>
> **Runtime API**
>
> Runtime API provides you with extensive uaArchive functions to edit recipes and recipe queries in Runtime (see section "Interfaces > Runtime API", subsection "Control tags").

#### Requirement

- Communication type is set to "Tags" in the recipe.
- The "Unique values" checkbox is activated under "Options" in the properties of the recipe element "Coloring 7".
- Recipe tags and control tags are set up.
- A process picture with the required I/O fields is configured.
- The I/O fields are connected with the recipe tags and control tags.

Example:

![Requirement](images/111901232011_DV_resource.Stream@PNG-de-DE.png)

#### Procedure

To transfer recipe data to the recipe memory of the HMI device, follow these steps:

1. Enter the recipe values displayed in the blue fields "Water", "Sugar", "Aroma", "Coloring 7" and "Concentrate". The recipe values form the recipe data record you want to transfer.
2. Enter "3" as "ID" for the target recipe data record.
3. Enter "6" as job for reading in the "Instruction" field.

The entered recipe data are transferred as complete data record. The recipe data record number 3 is overwritten in the recipe memory. The job mailbox returns the value "0" (no error) in the "Job" control tag.

#### Alternative procedure

1. Enter new recipe values in the blue fields " Water", "Sugar", "Aroma", "Coloring 7" and "Concentrate".
2. Enter the recipe element "Coloring 7" as the "Field".
3. Enter the recipe element "020" as the value in the "Value" field.
4. Enter "6" as job for reading in the "Instruction" field.

The entered recipe data are transferred as complete data record. The recipe data record whose recipe element " Coloring 7" has the recipe value "020" - in the example the recipe data record number 3 in the recipe memory - will be overwritten. The job mailbox returns the value "0" (no error) in the "Job" control tag.

---

**See also**

[Displaying recipes (RT Professional)](#displaying-recipes-rt-professional)
  
[Recipe functions (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#recipe-functions-rt-professional)
  
[Control tags (RT Professional)](#control-tags-rt-professional)
  
[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Mouse and keyboard operation (RT Professional)

#### Introduction

You operate the recipe view in Runtime by buttons in the toolbar. If you do not want to use the toolbar, you can write the "ID" of the required button using any type of dynamization in the object property "ToolbarButtonClick" .

#### Overview

|  |  |  |
| --- | --- | --- |
| **Symbol** | **Description** | **ID** |
| ![Overview](images/67385995915_DV_resource.Stream@PNG-de-DE.png) | "Tooltip"  Calls the help for the recipe view. | 1 |
| ![Overview](images/67388091019_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog"  Opens the configuration dialog box in which you change the properties of the recipe view. | 2 |
| ![Overview](images/67388094859_DV_resource.Stream@PNG-de-DE.png) | "Select data connection"  Opens a dialog for selecting a recipe or recipe query. The recipe data are then shown in the table of the recipe view. | 3 |
| ![Overview](images/67388098699_DV_resource.Stream@PNG-de-DE.png) | "First line"  The first data record is displayed in the table by the button. | 4 |
| ![Overview](images/67388307339_DV_resource.Stream@PNG-de-DE.png) | "Previous line"  The previous data record is displayed in the table by the button. | 5 |
| ![Overview](images/67388311179_DV_resource.Stream@PNG-de-DE.png) | "Next line"  The next data record is displayed in the table by the button. | 6 |
| ![Overview](images/67388315147_DV_resource.Stream@PNG-de-DE.png) | "Last line"  The last data record is displayed in the table by the button. | 7 |
| ![Overview](images/67388318987_DV_resource.Stream@PNG-de-DE.png) | "Delete line"  The content of the marked lines are deleted. | 8 |
| ![Overview](images/67388322827_DV_resource.Stream@PNG-de-DE.png) | "Cut line"  The content of the marked lines are cut out. | 9 |
| ![Overview](images/67388326667_DV_resource.Stream@PNG-de-DE.png) | "Copy line"  The content of the marked lines are copied. | 10 |
| ![Overview](images/67388330507_DV_resource.Stream@PNG-de-DE.png) | "Insert line"  The content of the copied or cut-out lines is inserted starting from the marked line. | 11 |
| ![Overview](images/67388334347_DV_resource.Stream@PNG-de-DE.png) | "Read tags"  The contents of the connected WinCC tags are read and written into the recipe elements by the button. The "Tags" communication type must be activated in the displayed recipe to be able to use the button. The recipe elements must be connected with tags. | 12 |
| ![Overview](images/67388338187_DV_resource.Stream@PNG-de-DE.png) | "Write tags"  The contents of the recipe elements are written into the connected WinCC tags. The "Tags" communication type must be activated in the displayed recipe to be able to use the button. The recipe elements must be connected with tags. | 13 |
| ![Overview](images/67388342027_DV_resource.Stream@PNG-de-DE.png) | "Import Archive"  Using a button, a CSV file is imported from the "ua" directory of the project folder into the table of the recipe view. | 14 |
| ![Overview](images/67388345867_DV_resource.Stream@PNG-de-DE.png) | "Export archive"  The original contents of the table are exported with table headers by the button when loading. The recipe is stored as a CSV file in the "ua" directory of the project folder. | 15 |
| ![Overview](images/67388349707_DV_resource.Stream@PNG-de-DE.png) | "Sorting"  Opens a dialog box for setting a customized sorting of the displayed columns. | 16 |
| ![Overview](images/67390464395_DV_resource.Stream@PNG-de-DE.png) | "Selection dialog"  Specifies selection criteria for the columns of the recipe view to be displayed in the table. | 17 |
| ![Overview](images/67388353547_DV_resource.Stream@PNG-de-DE.png) | "Print"  Starts the printout of the displayed values. The print job used during printing is defined in the configuration dialog in the "General" tab. | 18 |
| ![Overview](images/67388361227_DV_resource.Stream@PNG-de-DE.png) | "Set time base"  Opens a dialog box for setting the time base for the used times. | 19 |
| ![Overview](images/67388357387_DV_resource.Stream@PNG-de-DE.PNG) | "Export data"  You can use this button to export the current Runtime data of a recipe or recipe query to a CSV file.  If the "Display dialog" option is activated, a dialog opens in which you can view the settings for export and start the export. With the appropriate operator authorizations you can also select the file and the directory for the export. If no dialog box is displayed, the data export to the preset file starts immediately. | 20 |
| ![Overview](images/67388365067_DV_resource.Stream@PNG-de-DE.PNG) | "User-defined 1"  Displays the first button created by the user. The function of the button is customized. | 1001 |

#### Possible elements of the status bar

The following elements may appear in the status bar of the recipe view:

![Possible elements of the status bar](images/10519163147_DV_resource.Stream@PNG-en-US.png)

| Symbol | Name | Description |
| --- | --- | --- |
| ![Possible elements of the status bar](images/10519153803_DV_resource.Stream@PNG-en-US.png) | Archive name | Displays the name of the selected recipe or recipe query. |
| ![Possible elements of the status bar](images/10519036171_DV_resource.Stream@PNG-en-US.png) | Row | Shows the number of the marked line. |
| ![Possible elements of the status bar](images/10519083915_DV_resource.Stream@PNG-en-US.png) | column | Shows the number of the marked column. |
| ![Possible elements of the status bar](images/43396379531_DV_resource.Stream@PNG-de-DE.png) | Date | Shows the system date. |
| ![Possible elements of the status bar](images/10419608075_DV_resource.Stream@PNG-de-DE.png) | Time | Shows the system time. |
| ![Possible elements of the status bar](images/8580568971_DV_resource.Stream@PNG-de-DE.png) | Time Base | Shows the time base used in the display of times. |

#### Navigation in the table

You can navigate in the table as follows:

- You enter the next cell with the "ENTER" key or with the "Right" cursor key.
- You enter the previous cell with "SHIFT+ENTER" key or with the "Left" cursor key.
- You enter the next line by clicking with the mouse in the line or with the "Down" cursor key.
- You enter the previous line by clicking with the mouse in the line or with the "Up" cursor key.

  > **Note**
  >
  > If the "Error while connecting the data!" error message appears when Runtime starts, the recipe view has no connection to a recipe or recipe query. Check the following:
  >
  > - The name is specified correctly.
  > - The configuration is not changed.
  > - The connected recipe or recipe query still exists.

### Editing recipe data (RT Professional)

#### Introduction

You can edit data in the Data recipe view. The following options are available:

- Enter new data
- Change existing data
- Delete lines
- Cut-out, copy and insert lines

#### Requirement

- You have permitted editing in the configuration dialog in the "General" tab.
- You have deactivated the "Write-protected" property for the column to be edited in the configuration dialog in the "Columns" tab.
- The "ID" column cannot be edited.
- If the recipe view is connected to a recipe query, you cannot delete and cut out a row.

#### Entering new data in the table

1. Click on ![Entering new data in the table](images/67388315147_DV_resource.Stream@PNG-de-DE.png) to move to the last line. The line is marked.
2. Double-click on the first cell of the marked line. You can also press on "F2", "Alt+Enter" or Ctrl+Enter" in the cell.
3. You enter the values in the cells one after the other and confirm each time by pressing Enter. After you have entered all values in the line and selected another line, the new data record is written into the recipe. You move to another line by clicking with the mouse, with the "ENTER" key or with the "Up" and "Down" cursor keys.
4. You can copy the data of a marked line with "CTRL+C" or "CTRL+X" into the clipboard. The copied data is inserted into a marked line with "CTRL+V".

#### Changing existing data in the table

1. Click on ![Changing existing data in the table](images/67388311179_DV_resource.Stream@PNG-de-DE.png) or ![Changing existing data in the table](images/67388307339_DV_resource.Stream@PNG-de-DE.png) to move to the desired line. You can also use the scrollbars to move to the desired line.
2. Double-click on the desired cell of the marked line. You can also press on "F2", "Alt+Enter" or Ctrl+Enter" in the cell.
3. You enter the values in the cells one after the other and confirm each time by pressing Enter. After you have entered all values in the line and selected another line, the changed data record is written into the recipe.

#### Deleting a line in the table

1. Click on ![Deleting a line in the table](images/67388311179_DV_resource.Stream@PNG-de-DE.png) or ![Deleting a line in the table](images/67388307339_DV_resource.Stream@PNG-de-DE.png) to move to the desired line. You can also use the scrollbars to move to the desired line.
2. Click on ![Deleting a line in the table](images/67388318987_DV_resource.Stream@PNG-de-DE.png) to delete the marked line.

#### Cutting, copying and inserting lines

1. Click on ![Cutting, copying and inserting lines](images/67388311179_DV_resource.Stream@PNG-de-DE.png) or ![Cutting, copying and inserting lines](images/67388307339_DV_resource.Stream@PNG-de-DE.png) to move to the desired line. You can also use the scrollbars to move to the desired line.
2. Click on ![Cutting, copying and inserting lines](images/67388322827_DV_resource.Stream@PNG-de-DE.png) or ![Cutting, copying and inserting lines](images/67388326667_DV_resource.Stream@PNG-de-DE.png) to cut or copy the data of the line. As an alternative, you can also use key combination "CTRL+ALT+X" or "CTRL+ALT+C".
3. Go to the desired line into which you want to copy the data. Click on ![Cutting, copying and inserting lines](images/67388330507_DV_resource.Stream@PNG-de-DE.png) to insert the cut-out or copied data. If you do not want to overwrite the data of the marked line, move into the last line to insert the data.

### Selecting and configuring data (RT Professional)

#### Introduction

The recipe view shows the data of the connected recipe in a table. The displayed content of the table is determined by the selected columns and the selection of contents of the columns.

#### Requirement

- You have created one or more recipes and/or recipe queries.
- You have connected the recipe view to a recipe or recipe query.

#### Configuring the columns

1. Go to the "Columns" tab.

   ![Configuring the columns](images/10519706379_DV_resource.Stream@PNG-en-US.png)
2. In the "Columns" list you see the fields of the connected recipe or recipe query. If you select the check box in front of the name of the column, the column is displayed in the table. Deactivate the check box if you do not want it to appear.
3. Determine the order of the columns in the table using the "Up" and "Down" buttons.
4. Select a column to configure the properties and the format.
5. If necessary, change the width of the column in the table. Enter a value in the "Length in chars" field.
6. Some columns can also show the content and the header as a symbol. Determine how these columns are displayed in the "Display" field. Text and symbols can be displayed at the same time.
7. Save the configuration.

#### Selection of column content that will be displayed in the table

Configure criteria used to display the content in the columns in the "Selection" area.

#### Procedure

1. Click "Edit...". The selection dialog is opened.

   ![Procedure](images/10519715723_DV_resource.Stream@PNG-en-US.png)
2. Specify the criteria for the display. You can find more detailed information on the selection of columns under "[Select data](#select-data-rt-professional)".
3. Click "OK" to close the selection dialog. The selection is considered at the start of Runtime in the table of the recipe view.

#### Configuring the Sorting of Columns

You configure the sorting of the columns in the table in the "Sorting" area. You can also specify the sorting criteria in Runtime using the key functions.

1. Click "Edit...". The sorting dialog opens.

   ![Configuring the Sorting of Columns](images/10519601547_DV_resource.Stream@PNG-en-US.png)
2. Set a sorting sequence.
3. Click "OK" to close the sorting dialog.
4. Save the configuration of the contents.

---

**See also**

[Select data (RT Professional)](#select-data-rt-professional)

### Select data (RT Professional)

#### Introduction

Which contents of the recipe you want to show or export in the recipe view table can be defined in Runtime by the selection dialog box. In the selection dialog box you defie selection criteria with regard to the displayed columns of the recipe.

#### Requirement

- The selection dialog is open (see section "[Selecting and configuring data](#selecting-and-configuring-data-rt-professional)").

  ![Requirement](images/10519715723_DV_resource.Stream@PNG-en-US.png)

#### Procedure

Proceed as follows:

1. Double-click in the first empty line in the "Criteria" column. The list with the columns of the recipe view is shown. Select the desired columns, e.g. "field1".
2. Double-click in the "Operand" column to select an operand.
3. Double-click in the "Setting" column to enter a comparison value.
4. Double click in the "Logic operator" column to select an "AND" or "OR" function.
5. Repeat the procedure if you want to define further criteria.
6. Click "OK" to close the selection dialog. The selection is displayed in the table of the recipe view.

   > **Note**
   >
   > **Ensuring the display of column content**
   >
   > Make sure of proper use of the settings and connections of criteria.
   >
   > Incorrect logical operations can lead to the data of the connected recipe not being displayed in the recipe view.
   >
   > Therefore test every criterion separately before the logical operation and then the logically operated criteria respectively. Check that all expected contents are also displayed in combination.
   >
   > This ensures that the selection is displayed completely in the recipe view.

---

**See also**

[Selecting and configuring data (RT Professional)](#selecting-and-configuring-data-rt-professional)

### Sorting data (RT Professional)

#### Introduction

The data in the recipe view can be sorted by columns in Runtime. You sort the columns either via the "Sort dialog" button function or directly via the column headers.

> **Note**
>
> You can define the sorting criteria already in the configuration in the recipe view by clicking the "Edit..." button under "Sorting" on the "Columns" tab.

#### How to sort with the Sort dialog

#### Requirement

- You have activated the "Sorting dialog" button on the "Toolbar" tab of the UserArchive Control.

#### Procedure

1. Click the "Sort Dialog" button ![Procedure](images/67388349707_DV_resource.Stream@PNG-de-DE.png).
2. Select the column of the connected recipe from the "Sort by" list which is to be used for sorting first. Select the relevant check box to specify sorting in ascending or descending order. If you want to sort by more than one column, select the other columns in the desired order in the "Then sort by" lists.

   ![Procedure](images/10519601547_DV_resource.Stream@PNG-en-US.png)

#### How to sort the column contents with the column heading

When sorting using the column header, you are able to specify the sort order for more than four columns. A sorting icon and sorting index, displayed with right-justification in the column heading, show sorting order and sorting sequence of the column contents.

#### Requirement

- You have allowed sorting in the list field "Sort by column header" by click or double click on the "Parameters" tab of the recipe view.
- You have activated the "Show sorting icon" and "Show sorting index" checkboxes.

#### Procedure

1. Click the column header of the column you want to sort as first column. The sorting index "1" is displayed, and the sorting icon points upwards for ascending sort order.
2. If you want to sort in descending order, click the column header again.
3. If the sorting order has been defined with "up/down/none", you can undo the sorting of the column with a third click.
4. If you want to sort several message blocks, click the respective header columns in the desired sequence.

## Examples (RT Professional)

This section contains information on the following topics:

- [Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)
- [Example: Creating recipe queries (RT Professional)](#example-creating-recipe-queries-rt-professional)
- [Example: Configuring a recipe view (RT Professional)](#example-configuring-a-recipe-view-rt-professional)
- [Example: Recipe functions (RT Professional)](#example-recipe-functions-rt-professional)
- [Using control tags (RT Professional)](#using-control-tags-rt-professional)

### Example: Creating recipes (RT Professional)

#### Task

In this example, you will create two recipes.

- A "Beverage" recipe for drinks. The drinks mixing plant produces various drinks. You create a recipe data record for each item.
- An "Orders" recipe for orders. The orders contain the current order data.

#### Settings

The settings relate to an HMI device which is connected to a SIMATIC S7-300 or SIMATIC S7-400.

In this example, you will need the following tags, recipes, recipe entries and recipe data records:

Tags:

| Name | PLC connection | Address | Type |
| --- | --- | --- | --- |
| article | Yes | DB 120, DBW 0 | String |
| litrewater | Yes | DB 120, DBW 4 | Integer |
| kilosugar | Yes | DB 120, DBW 8 | Integer |
| gramaroma | Yes | DB 120, DBW 12 | Integer |
| litreconcentrate | Yes | DB 120, DBW 16 | Integer |
| coloring | Yes | DB 120, DBW 20 | Integer |
| customer | Yes | DB 120, DBW 24 | String |
| numbercustomer | Yes | DB 120, DBW 28 | String |
| numberorder | Yes | DB 120, DBW 32 | Integer |
| quantitiy | Yes | DB 120, DBW 36 | Integer |
| filling | Yes | DB 120, DBW 40 | Integer |
| dateorder | Yes | DB 120, DBW 44 | Date |
| status | Yes | DB 120, DBW 48 | Integer |

"Beverage" recipe:

| Recipe element | Associated tag |
| --- | --- |
| Article | article |
| Water | litrewater |
| Sugar | kilosugar |
| Aroma | gramaroma |
| Concentrate | litreconcentrate |
| Coloring | coloring |

| Data record ID | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Article | Juice | Nectar | Cola Light |
| Water | 5 | 50 | 72 |
| Sugar | 5 | 10 | 35 |
| Aroma | 100 | 300 | 240 |
| Concentrate | 95 | 50 | 35 |
| Coloring | FS 0063 | FS 0063 | FS 1007 |

"Orders" recipe:

| Recipe element | Associated tag |
| --- | --- |
| Customer | customer |
| Number | numbercustomer |
| Order | numberorder |
| Article | article |
| Quantitiy | quantitiy |
| Filling | filling |
| Status | status |
| Date | dateorder |

#### Procedure

1. Create the tags listed above with the settings described above.
2. Create the "Beverage" and "Orders" recipes with the settings indicated above.
3. Select the following properties for the recipes:

   - Under "General > Size" the "Unlimited" type
   - Under "Communication > Communication type" the "Tags" communication type
4. Create the recipe entries in each recipe.

   ![Procedure](images/61789021707_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61789021707_DV_resource.Stream@PNG-en-US.png)
5. Activate the "Unique values" check box for the following elements in the property window under "Extras".

   - In the "Beverage" recipe for the "Article" recipe element
   - In the "Orders" recipe for the "Order" recipe element
6. Create the data records indicated above in the "Beverage" recipe. Enter the values indicated above in each of the data records.

#### Result

The "Beverage" and "Orders" recipes are created.

![Result](images/61789182475_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Definition and applications (RT Professional)](#definition-and-applications-rt-professional)
  
[Example: Creating recipe queries (RT Professional)](#example-creating-recipe-queries-rt-professional)
  
[Example: Configuring a recipe view (RT Professional)](#example-configuring-a-recipe-view-rt-professional)
  
[Using control tags (RT Professional)](#using-control-tags-rt-professional)

### Example: Creating recipe queries (RT Professional)

#### Task

In this example, you create the "Label" recipe query. The following recipe elements are displayed in the recipe query:

| Recipe element | Recipe |
| --- | --- |
| Article | Beverage, Orders |
| Customer | Orders |
| Status | Orders |
| Order | Orders |
| Filling | Orders |
| Sugar | Beverage |
| Coloring | Beverage |

The "Article" recipe element is contained as a common element of both recipes.

#### Requirements

The "Beverage" and "Orders" recipes are created.

#### Procedure

1. Create the "Label" recipe query. Create the elements listed above.

   ![Procedure](images/100708744459_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/100708744459_DV_resource.Stream@PNG-en-US.png)
2. Enter the following conditions under "Properties > Relations":

   Beverage.Article = Orders.Article

   ![Procedure](images/61731071883_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61731071883_DV_resource.Stream@PNG-en-US.png)

#### Result

The "Label" recipe query is created.

---

**See also**

[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Example: Configuring a recipe view (RT Professional)

#### Task

In this example, you will add a plant screen with recipe view to the "Label" view.

#### Requirement

The "Create recipes" and "Create recipe query" examples are created.

You have created and opened the "Drinks mixing plant" process picture.

#### Procedure

1. Insert the recipe view in the process picture. You will find the recipe display in the toolbox under "Controls".
2. In the Inspector window, use the arrow to select the "Recipe query" type in the "Data source" input field of the "General > View" group.
3. Select the "Label" recipe query.
4. Define additional display options for the recipe view in the "Properties" > "Appearance" group in the Inspector window.
5. Go to the "Properties" > "Columns" group in the Inspector window.

   - Activate the check box in the "Visible" and "Protected" columns for all recipe elements.
6. In the Inspector window, switch to the "Properties" > "Toolbar" group. Activate the check box in the "Visible" column for the following buttons under "Toolbar - Buttons".

   - "First line"
   - "Previous line"
   - "Next line"
   - "Last line"
   - "Sort dialog"
   - "Selection dialog"
7. Go to the "Properties" > "Columns" group in the Inspector window. Enter the following sorting in the "Sort" column.

   - By job number
   - Ascending

#### Result

In Runtime,the recipe view is opened with the "Label" recipe query in the "Drinks mixing plant" process picture. The data records are displayed sorted by job number. You can use the buttons to switch between the data records.

Use the "Status" data field to display the current job or jobs that have been run.

You can adapt the recipe display to the data records as required with the "Sort dialog" and "Selection dialog" buttons.

---

**See also**

[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)

### Example: Recipe functions (RT Professional)

#### Introduction

Here is a script example that uses some of the standard functions of recipes. The example includes functions for reading and writing a recipe in Runtime, which are called by clicking on the buttons:

- The "UAReadFromArchive" function reads the first record of the recipe.
- The "UAWriteToArchive" function writes a data record to the recipe.

The data are displayed in the WinCC recipe display, and the script outputs in the diagnostics window.

![Introduction](images/15766145035_DV_resource.Stream@PNG-de-DE.png)

#### Requirement

- You know the basics of the editors "Recipe Display", "Graphics Designer" and "Global Script".
- You have created a recipe, e.g. "color" from the example on the "Example of using the control variables" page.
- You have opened the Graphics Designer and configured an image with a WinCC recipe display, e.g. from the example on the "Example for using the control variables" page.
- You have enabled the "Global Script Runtime" option in the startup list in the WinCC properties of the computer.

#### Procedure

1. Open the C editor of "Global Script" in the WinCC Explorer.
2. Click on the "New Project Function" command in the "File" menu of the editor.
3. Copy one of the example scripts below into the editor window. Click on ![Procedure](images/45399737739_DV_resource.Stream@PNG-de-DE.png) to compile the function.
4. Click ![Procedure](images/45379944715_DV_resource.Stream@PNG-de-DE.png) to save the compiled, error-free function with the name "UAReadFromArchive".
5. Proceed with the second script using the same procedure.
6. Insert the "Application window" smart object from the object palette into the screen in the Graphics Designer. The application window serves as a diagnostic window for the scripts.
7. In the "Window Contents" dialog , select the entry "Global Script" and select "GSC Diagnostics" as a template. Set all the properties to "yes" in the "Miscellaneous" tab in the properties of the application window.
8. Create the "Read" and "Write" buttons with the "Button" object from the object palette under "Windows Objects".
9. Right-click on the "Read" button and select the "Properties" menu item.
10. Open the "Event" tab. Click "Mouse".
11. At "Mouse click", right-click in the "Action" column and select "C-action". The "Edit action" window opens.
12. In the editor window, click in the "OnClick" action between "{" and "}".
13. Double-click on "UAReadFromArchive" in the "Project functions" directory in the navigation window.
14. Click ![Procedure](images/45399737739_DV_resource.Stream@PNG-de-DE.png) and then "OK" at the bottom right. The example script is now integrated in the action for the mouse click on the button.
15. Proceed with the "Write" button using the same procedure.
16. Save the screen in Graphics Designer.
17. Activate the example project for runtime.

#### Example script "UAReadFromArchive"

#include "apdefap.h"

void UAReadFromArchive()

{

UAHCONNECT hConnect = 0;

UAHARCHIVE hArchive = 0;

LONG IndexArchive;

LONG FieldLength;

LONG FieldType;

LONG NumberOfFields;

LONG Index;

long IntValue;

float FloatValue;

double DoubleValue;

char ArchivName[255], StringField[255];

SYSTEMTIME SysDate;

//******* Connect to Component User Archives ****************************

if (uaConnect( &hConnect ) == FALSE )

{

printf("uaConnect error: %d\n", uaGetLastError() );

return;

}

if (hConnect == NULL)

{

printf("Handle UAHCONNECT equals NULL\n" );

return;

}

//******* Connect to Archive via Archive Name ****************************

if (uaQueryArchiveByName( hConnect, "color", &hArchive ) == FALSE )

{

printf("uaQueryArchive Error: %d\n" , uaGetLastError() );

goto finish;

}

//******* Opens Archive ******************************************************

if ( uaArchiveOpen( hArchive ) == FALSE )

{

printf("uaArchive Open Error\n" );

goto finish;

}

//******* Move to first record set ****************************************************

if (uaArchiveMoveFirst(hArchive) == FALSE )

{

printf("uaArchiveMoveFirst Error = %d\n" , uaGetLastError() );

goto finish;

}

//******* Get Number of Fields **********************************************

NumberOfFields = uaArchiveGetFields( hArchive );

printf("Number of Fields = %u\n", NumberOfFields );

//******* Read and show Data Fields ****************************************

for ( Index = 1; Index < NumberOfFields; Index++ )

{

printf("Data of Field %u: \n", Index );

FieldType = uaArchiveGetFieldType( hArchive, Index );

switch ( FieldType )

{

case UA_FIELDTYPE_INTEGER :

printf("Field Type = Integer\n");

if ( uaArchiveGetFieldValueLong ( hArchive, Index, &IntValue ) == TRUE )

printf( "Field Value = %u\n", IntValue );

else

printf("Error callinguaArchiveGetFieldValueLong: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_FLOAT :

printf("Field Type = Float\n");

if (uaArchiveGetFieldValueFloat ( hArchive, Index, &FloatValue ) == TRUE )

printf("Field Value = %f\n", FloatValue );

else

printf("Error callinguaArchiveGetFieldValueFloat: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_DOUBLE :

printf("Field Type = Double\n");

if (uaArchiveGetFieldValueDouble (hArchive, Index, &DoubleValue ) == TRUE )

printf("Field Value = %g\n", DoubleValue );

else

printf("Error calling uaArchiveGetFieldValueDouble: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_STRING :

printf("Field Type = String\n");

if (uaArchiveGetFieldValueString ( hArchive, Index, StringField, 20 ) == TRUE )

printf("Field Value = %s\n", StringField );

else

printf("Error callinguaArchiveGetFieldValueString: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_DATETIME :

printf("Field Type = Date & Time\n");

if (uaArchiveGetFieldValueDate ( hArchive, Index, &SysDate ) == TRUE )

printf("%d.%d.%d\n ",SysDate.wDay, SysDate.wMonth, SysDate.wYear );

else

printf("Error calling uaArchiveGetFieldValueLong: %d\n", uaGetLastError() );

break;

case -1 :

default:

printf("Error executing uaArchiveGetFieldType\n");

}

//******* Read and show Field Length **************************************

FieldLength = uaArchiveGetFieldLength( hArchive, Index );

if ( FieldLength != -1 )

printf("Field Length = %u\n", FieldLength );

else

printf("Error executing uaArchiveGetFieldLength\n");

}

//******* Close all handles and connections ***************************

finish:;

//******* Close Archive *******************************************************

if( NULL != hArchive )

{

if (uaArchiveClose ( hArchive ) == FALSE )

{

printf("error on closing archive\n" );

}

}

//****** Release Connection to Archive *************************************

if( NULL != hArchive )

{

if (uaReleaseArchive ( hArchive ) == FALSE )

{

printf("error on releasing archive\n" );

}

hArchive = 0;

}

//******* Disconnect to Component User Archives *************************

if( NULL != hConnect )

{

if (uaDisconnect ( hConnect ) == FALSE )

{

printf("error on disconnection\n" );

}

hConnect = 0;

}

}

#### Example script "UAWriteToArchive"

#include "apdefap.h"

void UAWriteToArchive()

{

UAHCONNECT hConnect = 0;

UAHARCHIVE hArchive = 0;

LONG IndexArchive;

LONG FieldLength;

LONG FieldType;

LONG NumberOfFields;

LONG Index;

long IntValue;

char StringField[255];

SYSTEMTIME SysDate;

//******* Connect to Component User Archives ****************************

if (uaConnect( &hConnect ) == FALSE )

{

printf("uaConnect error: %d\n", uaGetLastError() );

return;

}

if (hConnect == NULL)

{

printf("Handle UAHCONNECT equals NULL\n" );

return;

}

//******* Connect to Archive via Name ****************************

if (uaQueryArchiveByName( hConnect, "color", &hArchive ) == FALSE )

{

printf("uaQueryArchive Error: %d\n" , uaGetLastError() );

goto finish;

}

//******* Opens Archive ******************************************************

if ( uaArchiveOpen( hArchive ) == FALSE )

{

printf("uaArchive Open Error\n" );

goto finish;

}

//******* Get Number of Fields **********************************************

NumberOfFields = uaArchiveGetFields( hArchive );

printf("Number of Fields = %u\n", NumberOfFields );

//******* Read Last Data Set ************************************************

if (uaArchiveMoveLast( hArchive ) == TRUE )

printf("Number of Fields = %u\n", NumberOfFields );

else

{

printf("uaArchiveMoveLast Error: %d\n" , uaGetLastError() );

goto finish;

}

//******* Write into Data Fields *********************************************

IntValue = 105;//RGB for darkgray

strcpy(StringField, "darkgray" );

GetSystemTime( &SysDate );

for ( Index = 1; Index < NumberOfFields; Index++ )

{

printf("Data of Field %u: \n", Index );

FieldType = uaArchiveGetFieldType( hArchive, Index );

switch ( FieldType )

{

case UA_FIELDTYPE_INTEGER :

printf("Field Type = Integer\n");

if (uaArchiveSetFieldValueLong ( hArchive, Index, IntValue ) == TRUE )

printf( "Field Value = %u\n", IntValue );

else

printf("Error callinguaArchiveSetFieldValueLong: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_FLOAT :

printf("Field Type = Float\n");

if (uaArchiveSetFieldValueFloat ( hArchive, Index, FloatValue ) == TRUE )

printf("Field Value = %f\n", FloatValue );

else

printf("Error callinguaArchiveSetFieldValueFloat: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_DOUBLE :

printf("Field Type = Double\n");

if (uaArchiveSetFieldValueDouble (hArchive, Index, DoubleValue ) == TRUE )

printf("Field Value = %g\n", DoubleValue );

else

printf("Error calling uaArchiveSetFieldValueDouble: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_STRING :

printf("Field Type = String\n");

if (uaArchiveSetFieldValueString ( hArchive, Index, StringField ) == TRUE )

printf("Field Value = %s\n", StringField );

else

printf("Error callinguaArchiveSetFieldValueString: %d\n", uaGetLastError() );

break;

case UA_FIELDTYPE_DATETIME :

printf("Field Type = Date & Time\n");

if (uaArchiveSetFieldValueDate ( hArchive, Index, &SysDate ) == TRUE )

printf("%d.%d.%d\n ",SysDate.wDay, SysDate.wMonth, SysDate.wYear );

else

printf("Error calling uaArchiveSetFieldValueLong: %d\n", uaGetLastError() );

break;

case -1 :

default:

printf("Error executing uaArchiveSetFieldType\n");

}

FieldLength = uaArchiveGetFieldLength( hArchive, Index );

if ( FieldLength != -1 )

printf("Field Length = %u\n", FieldLength );

else

printf("Error executing uaArchiveGetFieldLength\n");

}

// ******* Update Archive *******************************************

if (uaArchiveUpdate(hArchive) == FALSE )

{

printf("uaArchiveUpdate Error:\n" );

}

//******* Close all handles and connections ***************************

finish:;

//******* Close Archive *******************************************************

if( NULL != hArchive )

{

if (uaArchiveClose ( hArchive ) == FALSE )

{

printf("error on closing archive\n" );

}

}

//****** Release Connection to Archive *************************************

if( NULL != hArchive )

{

if (uaReleaseArchive ( hArchive ) == FALSE )

{

printf("error on releasing archive\n" );

}

hArchive = 0;

}

//******* Disconnect to Component User Archives *************************

if( NULL != hConnect )

{

if (uaDisconnect ( hConnect ) == FALSE )

{

printf("error on disconnection\n" );

}

hConnect = 0;

}

}

### Using control tags (RT Professional)

#### Example for the use of control tags:

You need to perform the following steps to work through the example with the control tags:

#### Requirement

You have created the "Drinks" recipe.

| Symbol | Meaning |
| --- | --- |
| **Properties of the "Cola" recipe** |  |
| Log type | "Unlimited" |
| Communication | "Tags" |
| Data type for the "ID" control tag | Long |
| Data type for the "Job" control tag | Long |
| Data type for the "Field" control tag | String (1 character) |
| Data type for the "Value" control tag | String (1 character) |

#### Procedure

1. Create the control tag with the following properties:

|  |  |  |
| --- | --- | --- |
| **Control tag** | **Data Format** | **Output format** |
| ID | decimal | 0999 |
| Job | decimal | s9 |
| Field | String | * |
| Value | String | * |

1. Select the "Update for changes" object property for each control tag.
2. Connect the control tags to the "Drinks" recipe.
3. Create a new screen and add a recipe view.

   - Select the "Drinks" recipe.
   - Check the "Paste", "Change" and "Delete" check boxes under "General".
4. Create an I/O field for every configured recipe element.
5. Connect the I/O fields to the associated tags.

   For example, connect the I/O field for "Colorant" to the "Coloring" process tag.

   - Create a text field for the label of every configured I/O field.

     By doing so, you assign the I/O fields to the individual recipe elements in Runtime.
6. Create an I/O field for every control tag.

   - Create a text field for the label of every configured I/O field.

     By doing so, you assign the I/O fields to the individual control tags in Runtime.
7. Start Runtime or load the project into the HMI device and start the project.

#### Result

The configuration for the recipe is completed.

#### Accessing the recipe

You can now access the recipe in the following ways:

- In the table view of the recipe view

  ![Accessing the recipe](images/24039284619_DV_resource.Stream@PNG-en-US.PNG)
- Using the configured I/O fields

  ![Accessing the recipe](images/111901232011_DV_resource.Stream@PNG-de-DE.png)

#### Write the data record to the process tags using the ID

- Enter the ID "3" in the "ID" I/O field and enter a "7" in the "Job" I/O field.

  The values of data record "3" will be written to the process tags in the I/O fields and displayed in the I/O fields.

  If the data record values were read without error from the recipe, error number "0" is displayed in the "Job" field.

  Error number "-1" is output if an error occurs.

  The "Field" and "Value" control tags are not required.

  > **Note**
  >
  > The current contents of the process tags are read into the recipe by entering the ID "-1" and the job "6". The new values are appended at the end of the table. The data record IDs are continuously incremented.

#### Read the process tags via the ID

- Change the values in the I/O fields of the process tags and enter a "5" in the "ID" field. Enter "6" in the "Job" I/O field.

  The changed values of the process tag are written to data record "5" of the recipe. The values that were previously contained in this data record are overwritten.

  The "Field" and "Value" control tags are not required.

#### Write a data record to the process tag using the "Field" and "Value" control tags

> **Note**
>
> For an element that is referenced with the "Value" control tag, you must select the "Field must possess a unique value" check box under "Properties > Memory options". Otherwise it will not be possible to create a unique assignment between the recipe data record and the value in the element.

- In the "Field" I/O field, enter the word "Item" and write "Cola Light" to the "Value" I/O field. Enter "7" in the "Job" I/O field.

  The values of the "Cola Light" data record will be written to the process tags in the I/O fields and displayed in the I/O fields.

  The "ID" control tag is not needed, so it must be set to 0.

---

**See also**

[Example: Creating recipes (RT Professional)](#example-creating-recipes-rt-professional)
