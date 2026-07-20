---
title: "Declaring PLC data types (UDT)"
package: ProgPLCDatatypesenUS
topics: 23
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Declaring PLC data types (UDT)

This section contains information on the following topics:

- [Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)
- [PLC data types in the project tree](#plc-data-types-in-the-project-tree)
- [Creating PLC data types](#creating-plc-data-types)
- [Opening PLC data types](#opening-plc-data-types)
- [Copying or moving PLC data types](#copying-or-moving-plc-data-types)
- [Delete PLC data types](#delete-plc-data-types)
- [Renumbering PLC data types](#renumbering-plc-data-types)
- [Programming the structure of PLC data types](#programming-the-structure-of-plc-data-types)
- [Editing tag properties in PLC data types](#editing-tag-properties-in-plc-data-types)
- [Editing the declaration table for PLC data types](#editing-the-declaration-table-for-plc-data-types)

## Structure of the declaration table for PLC data types

### Structure of the declaration table for PLC data types

The figure below shows the structure of the declaration table for PLC data types.

![Structure of the declaration table for PLC data types](images/83551405451_DV_resource.Stream@PNG-en-US.png)

### Meaning of the columns

The following table shows the meaning of the individual columns. You can show or hide the columns as required. The number of columns displayed varies depending on the CPU series.

| Column | Explanation |
| --- | --- |
| ![Meaning of the columns](images/45636405771_DV_resource.Stream@PNG-de-DE.png) | Symbol you can click to move or copy the tag. |
| Name | Name of the tags. |
| Data type | Data type of the tags. |
| Default value | Value with which you predefine the tag in the declaration of the PLC data type.  Specification of the default value is optional. If you do not specify any value the predefined value for the indicated data type is used. For example, the value "false" is predefined for BOOL. |
| Visible in HMI engineering | Shows whether the tag is visible by default in the HMI selection list. |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime. |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |
| Setpoint value | Setpoint values are the values that will probably have to be fine tuned during commissioning. After commissioning, the values of these tags can be transferred to the offline program as start values and stored there. |
| Monitoring | Indicates whether monitoring for process diagnostics was created for the tag. |
| Comment | Comment to document the tags. |

---

**See also**

[Creating PLC data types](#creating-plc-data-types)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)
  
[Using setpoints during commissioning](Programming%20data%20blocks.md#using-setpoints-during-commissioning)

## PLC data types in the project tree

### "PLC data types" folder

The project tree contains a "PLC data types" folder in which you can create and manage the following PLC data types (UDT):

- User-created PLC data types

  PLC data types that you create yourself are located directly in the folder and can be opened, deleted and renamed there.
- System data types

  PLC data types created by the system are located in the "System data types" subfolder. This folder is created when you create a data block based on a system data type for the first time or when you drag an instruction that uses a system data type into the program. If the system data type is no longer being used in the program, it is deleted automatically during compilation. The "System data types" folder is deleted when it no longer contains any data types.

  > **Note**
  >
  > **Visibility of system data types in the project tree**
  >
  > Note that not all system data types are visible in the project tree. Internal system data types such as "IEC_COUNTER" are not displayed in the "System data types" folder.

### Moving or copying PLC data types

You can move or copy PLC data types between the "System data types" folder and other folders. However, the following rules must be observed:

- Moving or copying PLC data types to the "System data types" folder:

  PLC data types in the "System data types" folder that are not required for user program execution are removed during the next compilation. This may cause your moved PLC data type to be deleted.
- Moving data types from the "System data types" folder:

  System data types can be moved, but not copied, from the "System data types" folder to the "PLC data types" folder above it. Data types not located in the "System data types" folder are not managed by the system, however. They are thus not automatically deleted when they are no longer used in the program.

---

**See also**

[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)
  
[Creating PLC data types](#creating-plc-data-types)
  
[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)

## Creating PLC data types

### Requirement

The "PLC data types" folder opens in the project tree.

### Procedure

To create a PLC data type, proceed as follows:

1. In the "PLC data types" folder, double-click the "Add new data type" command.

   The "Add new data type" dialog opens.
2. Select the category "PLC data type".
3. Enter the name of the PLC data type.
4. Optional within software units: Enter a namespace for the new PLC data type or use the default namespace of the software unit.

   You can find information on namespaces, in particular on the naming conventions according to IEC 61131-3, here: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

The new PLC data type is created. You can find the PLC data type in the project tree in the "PLC data types" folder.

### Adding comments for a PLC data type

To enter a comment for a PLC data type, proceed as follows:

1. Right-click the PLC data type in the project tree.
2. Select the "Properties" command in the shortcut menu.

   A dialog containing the properties of the PLC data type opens.
3. Select the "Information" entry in the area navigation.
4. Enter the comment in the "Comment" text box.
5. Confirm your entry with "OK".

---

**See also**

[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)

## Opening PLC data types

### Opening a PLC data type directly

To open a PLC data type directly, follow these steps:

1. In the project tree or in the overview window, select the PLC data type that you want to open.
2. Double-click on the PLC data type that you want to open.

   The PLC data type is being opened.

### Finding and opening a PLC data type

To find a PLC data type and then open it, follow these steps:

1. You can start the search process for the following three types:

   - Select the command "Open block/PLC data type" in the project tree in the shortcut menu of the project, a device or the "PLC data types" folder, or press the &lt;/F7&gt; button.
   - Press the &lt;F7&gt; key in the open program editor.

   The "Open block/PLC data type" dialog box opens.
2. Enter the name of the PLC data type you want to find. You can also enter only parts of the name.

   The list is filtered further with each letter entered. All PLC data types are displayed whose names contain the text entered. It makes no difference here in which position the text occurs. No distinction is made between upper and lower case. Blocks which begin with the entered text are displayed at the start of the list.

   The list is closed if there is no PLC data type that matches your input. You can show them at any time by clicking the button to the right of the text box. Keep in mind that there is no filtering in this case. If you want to filter for your inputs again, click the button once again.
3. In the list, click on the PLC data type that you wish to open.

   The PLC data type is being opened.

## Copying or moving PLC data types

### Copying PLC data types

To copy a PLC data type, follow these steps:

1. Right-click the PLC data type that you want to copy.
2. Select the "Copy" command in the shortcut menu.
3. In the project tree, right-click the "PLC data types" folder into which you want to insert the copied PLC data type.
4. Select the "Paste" command in the shortcut menu.

   - If you paste the PLC data type into the same CPU, the copy is pasted with the name extension "_&lt;consecutive number&gt;".
   - If you paste the PLC data type into a different CPU where a PLC data type of the same name already exists, the "Paste" dialog box opens. Select the desired option and confirm your selection with "OK".

Alternatively, you can also copy the PLC data type via drag-and-drop while holding down the &lt;Ctrl&gt; key.

### Moving PLC data types

To move a PLC data type, follow these steps:

1. Select the PLC data type you want to move.
2. Drag the PLC data type to the new position.

> **Note**
>
> **Copy or move PLC data types into namespaces**
>
> You can find information about how namespaces are handled when copying or moving PLC data types under "[Basics for copying or moving program elements](Using%20software%20units%20%28S7-1500%29.md#basics-for-copying-or-moving-program-elements-s7-1500)".

## Delete PLC data types

### Requirement

The PLC data type you want to delete is not open.

### Procedure

To delete a PLC data type, follow these steps:

1. In the project tree, open the "PLC data types" folder.
2. Select the PLC data type to be deleted. You can also select several PLC data types by clicking on them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking on the first and last data type.
3. Select the "Delete" command in the shortcut menu.

> **Note**
>
> If you delete a PLC data type, the blocks that use the data type will become inconsistent. These inconsistencies are marked in red in the block used. To remedy these inconsistencies, the data blocks have to be updated.

---

**See also**

[Updating the block interface](Declaring%20the%20block%20interface.md#updating-the-block-interface)
  
[Updating data blocks](Programming%20data%20blocks.md#updating-data-blocks)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)

## Renumbering PLC data types

For performance reasons, PLC data types are processed internally with numbers. If there are number conflicts, these are resolved automatically. But this is not possible for a PLC data type which is used by a know-how protected block. The block must be recompiled when you change the number of the PLC data type which results in a password prompt for the know-how protected block. You can bypass this step by setting up a separate numbering scheme for your PLC data types. Use numbers greater than 5000.

### Procedure

To change the default number of a PLC data type, follow these steps:

1. Open the project library in the "Libraries" task card.
2. Drag the compilable PLC data type to the "Types" folder.

   The "Add type" dialog opens.
3. Enter the properties of the new type.
4. Click "OK" to confirm.
5. Right-click the PLC data type in the project library and select the "Edit type" command from the shortcut menu.
6. Click "OK" to confirm your selection of the instance.

   The extension "in test" is now added to the name of the PLC data type.
7. Right-click the PLC data type and select the "Properties" command from the shortcut menu.
8. Select the "General" group in the area navigation.

   You can now edit the number of the PLC data type.
9. Change the number of the PLC data type.
10. Click "OK" to confirm.
11. Right-click the PLC data type in the project library and select the "Release version" command from the shortcut menu.

    The PLC data type has a new number. The assigned number is retained even if the type of the PLC data type is revoked.

## Programming the structure of PLC data types

This section contains information on the following topics:

- [Declaring tags of elementary data type](#declaring-tags-of-elementary-data-type)
- [Declaring tags of the ARRAY data type](#declaring-tags-of-the-array-data-type)
- [Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
- [Declaring tags based on a different PLC data type](#declaring-tags-based-on-a-different-plc-data-type)

### Declaring tags of elementary data type

#### Requirement

A PLC data type is open.

#### Procedure

To declare a tag, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the required data type in the "Data type" column. You will be supported by autocompletion during input.
3. Optional: Change the properties of the tags that are displayed in the other columns.
4. Repeat steps 1 to 3 for all tags that are to be declared.

---

**See also**

[Declaring tags of the ARRAY data type](Declaring%20the%20block%20interface.md#declaring-tags-of-the-array-data-type)
  
[Declaring tags of STRUCT data type](Declaring%20the%20block%20interface.md#declaring-tags-of-struct-data-type)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Editing the declaration table for PLC data types](#editing-the-declaration-table-for-plc-data-types)

### Declaring tags of the ARRAY data type

#### Requirement

A PLC data type is open.

#### Procedure

To declare a tag of the ARRAY data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the "Array" data type in the "Data type" column. You will be supported by Autocomplete in this step.

   The "Array" dialog opens.
3. In the "Data type" text box, specify the data type of the array elements.
4. In the "ARRAY limits" input field, specify the high and low limit for each dimension.

   Example of a one-dimensional ARRAY:

   `[0..3]`

   Example of a three-dimensional ARRAY:

   `[0..3, 0..15, 0..33]`
5. Confirm your entry.
6. Optional: Change the properties of the tags that are displayed in the other columns.

The tag is created but remains collapsed. To expand the ARRAY, click the triangle in front of the tag. Note that you cannot expand ARRAYs with more than 10,000 elements for reasons of clarity.

#### Entering default values of ARRAY elements

To pre-assign default values to the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the desired values in the "Default value" column.

#### Adding comments for ARRAYs

To add a comment for the entire ARRAY, enter the comment in the top line of the ARRAY declaration. The comment is used as a preset comment for all lower-level ARRAY elements.

To provide specific comments for the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the desired values in the "Comment" column.

#### Displaying ARRAYs in expanded mode

In "Expanded mode" all ARRAYs are displayed expanded by default.

To enable the expanded mode, follow these steps:

1. Click the "Expanded mode" button in the toolbar.

> **Note**
>
> **Restriction in "Expanded mode" display**
>
> Depending on the amount of RAM available on your computer, the following maximum limits apply to expanded mode:
>
> - RAM &lt; 8 GB: A maximum of 10,000 rows are displayed.
> - RAM &gt;= 8 GB: A maximum of 40,000 rows are displayed.

---

**See also**

[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)
  
[ARRAY](Data%20types.md#array)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Declaring tags of STRUCT data type

#### Requirements

A PLC data type is open.

#### Procedure

To declare a tag of the STRUCT data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter "Struct" in the "Data type" column. You will be supported by autocompletion during input.

   An empty, indented row is inserted after the new tag.
3. Insert the first structural element in the first empty row.

   An additional empty row is inserted after the element.
4. Select a data type for the structure element.
5. Optional: Change the properties of the structural element that is displayed in the other columns.
6. Repeat steps 3 to 5 for all additional structure elements.

   It is not necessary to end the structure explicitly. The structure ends with the last element that is entered.
7. To insert a new tag after the structure, leave a blank row after the end of the structure and then start the new tag in the second empty row.

#### Result

The tag of STRUCT data type is created.

---

**See also**

[Basic information on STRUCT](Data%20types.md#basic-information-on-struct)
  
[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Declaring tags based on a different PLC data type

#### Requirement

- A global data block is open.
- A PLC data type is declared in the current CPU.

#### Procedure

To declare a tag based on a different PLC data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the PLC data type in the "Data type" column. You will be supported by Autocomplete during input.

   The tag is created.
3. Optional: change the properties of the tags that are displayed in the other columns of the table.

   If you have already defined default values or comments for the tags within a PLC data type during declaration of the PLC data type, these are shown in gray. You can change these values here.

   The changed values are displayed in black and apply only to the specific point of use.

> **Note**
>
> If you change or delete PLC data types that are being used in the data block, the data block becomes inconsistent. To eliminate this inconsistency, you must recompile the program.

---

**See also**

[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

## Editing tag properties in PLC data types

This section contains information on the following topics:

- [Properties of tags in PLC data types](#properties-of-tags-in-plc-data-types)
- [Changing the properties of tags in PLC data types](#changing-the-properties-of-tags-in-plc-data-types)
- [Editing multilingual comments in the PLC data type (S7-1500)](#editing-multilingual-comments-in-the-plc-data-type-s7-1500)

### Properties of tags in PLC data types

#### Properties

The following table gives an overview of tag properties in PLC data types:

| Group | Property | Description |
| --- | --- | --- |
| General | Name | Name of the tags. |
| Data type | Data type of the tags. |  |
| Default value | Default value of the tag in the interface of a higher-level code block or in a PLC data type.   The values contained in the "Default value" column can only be changed in the higher-level code block or PLC data type. The values are only displayed in the data block. |  |
| Start value | Not relevant in PLC data types |  |
| Comment | Comment on the tag. |  |
| Attributes | Retain | Not relevant in PLC data types |
| User-defined attributes | CFC_Visible | Visible  Indicates whether a parameter is visible in CFC. |
| CFC_Configurable | Configurable  Indicates whether a parameter is configurable in CFC. |  |
| CFC_ForTest | For test  Indicates whether a parameter is registered for the CFC test mode. |  |
| CFC_Interconnectable | Interconnectable  Indicates whether a parameter is interconnectable in CFC. |  |
| CFC_EnableTagReadback | Enable tag readback  Indicates whether a parameter is relevant for the "Read back chart" function in CFC. |  |
| CFC_EnumerationTexts | Enumeration texts  The attribute is only used internally. |  |
| CFC_EngineeringUnit | Engineering unit  Assigns a parameter to a unit in CFC. |  |
| CFC_LowLimit | Low limit  Defines the low limit for the parameter in CFC. |  |
| CFC_HighLimit | High limit  Defines the high limit for the parameter in CFC. |  |

---

**See also**

[Changing the properties of tags in PLC data types](#changing-the-properties-of-tags-in-plc-data-types)
  
[Structure of the declaration table for PLC data types](#structure-of-the-declaration-table-for-plc-data-types)

### Changing the properties of tags in PLC data types

#### Editing general properties in the declaration table

To edit the general properties of one or more tags, follow these steps:

1. Open the PLC data type.
2. Change the entries in the columns.

#### Editing detailed properties in the properties window

To edit the detailed properties of an individual tag, follow these steps:

1. Select a tag in the table.
2. Select the "Properties" command in the shortcut menu.

   The inspector window shows the properties of the tag in the "General" and "Attributes" areas.
3. Select the required area in the area navigation.
4. Change the entries in the text boxes.

---

**See also**

[Updating the block interface](Declaring%20the%20block%20interface.md#updating-the-block-interface)
  
[Updating data blocks](Programming%20data%20blocks.md#updating-data-blocks)

### Editing multilingual comments in the PLC data type (S7-1500)

You can edit the comments from the PLC data type in all project languages that you have activated in the project language settings. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

Note that the texts must not exceed a length of 32767 Unicode characters even after translation.

#### Requirement

- You have activated multiple project languages.
- The PLC data type is open and it contains at least one comment.
- The data type does not have know-how protection.

#### Procedure

To edit a comment in all project languages, follow these steps:

1. Click on the comment whose translation you want to edit.

   If you want to edit the translations of several comments at the same time, select all the desired comments.
2. Open the "Properties" tab in the Inspector window.
3. Open the "Texts" tab.

   The "Texts" tab displays the selected comments in the active project languages and, if available, the translations of the comments.
4. You can edit the translations directly in the table in the "Texts" tab.
5. To edit the translations with an external editor, you can export the displayed texts to OOXML format using the "Export/Import project texts" buttons.

> **Note**
>
> **Editing all project texts in the global "Project texts" table**
>
> You can also edit the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts". It contains all translatable texts of the entire project.
>
> You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

## Editing the declaration table for PLC data types

This section contains information on the following topics:

- [Inserting table rows](#inserting-table-rows)
- [Inserting table rows](#inserting-table-rows-1)
- [Deleting tags](#deleting-tags)
- [Automatically filling in successive cells](#automatically-filling-in-successive-cells)
- [Show and hide table columns](#show-and-hide-table-columns)

### Inserting table rows

#### Procedure

Proceed as follows to insert a row above the selected row:

1. Select the row in front of which you want to insert a new row.
2. Click the "Insert row" button on the toolbar of the table.

#### Result

A new row is inserted above the selected row.

### Inserting table rows

#### Procedure

Proceed as follows to insert a row below the selected row:

1. Select the row below which you want to insert a new row.
2. Click the "Add row" button on the table toolbar.

#### Result

A new empty row will be inserted below the selected row.

### Deleting tags

#### Procedure

To delete a tag, follow these steps:

1. Select the row with the tag to be deleted. You can also select several rows by clicking on them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking on the first and last row.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Updating the block interface](Declaring%20the%20block%20interface.md#updating-the-block-interface)
  
[Updating data blocks](Programming%20data%20blocks.md#updating-data-blocks)

### Automatically filling in successive cells

You can load the contents of one or several table cells into the cells below, automatically filling in the successive cells.

If you automatically fill in cells in the "Name" column, a consecutive number will be appended to each name. For example, "Motor" will become "Motor_1".

You can define individual or more cells as well as entire rows as source area.

If less rows exist in the open table than you want to fill, then you will first have to insert additional empty rows.

#### Requirement

- The table is open.
- Sufficient declaration rows are available.

#### Procedure

To automatically fill in successive cells, follow these steps:

1. Select the cells to be loaded.
2. Click the "Fill" symbol in the bottom right corner of the cell.

   The mouse pointer is transformed into a crosshair.
3. Keep the mouse button pressed and drag the mouse pointer downwards over the cells that you want to fill in automatically.
4. Release the mouse button.

   The cells are filled in automatically.
5. If entries are already present in the cells that are to be automatically filled in, a dialog appears. In this dialog you can indicate whether you want to overwrite the existing entries or insert new rows for the new tags.

### Show and hide table columns

You can show or hide the columns in a table as needed.

#### Procedure

To show or hide table columns, follow these steps:

1. Click a column header.
2. Select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
3. To show a column, select the column's check box.
4. To hide a column, clear the column's check box.
5. To hide or show several columns, click "More" and activate or deactivate the check box of the corresponding columns in the "Show/Hide" dialog.
