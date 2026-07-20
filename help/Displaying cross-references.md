---
title: "Displaying cross-references"
package: ProgCrossRef2MenUS
topics: 25
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Displaying cross-references

This section contains information on the following topics:

- [General information about cross references](#general-information-about-cross-references)
- [Structure of the cross-reference list](#structure-of-the-cross-reference-list)
- [Settings in the cross-reference list](#settings-in-the-cross-reference-list)
- [Displaying the cross-reference list](#displaying-the-cross-reference-list)
- [Sorting the cross-reference list](#sorting-the-cross-reference-list)
- [Filter options for cross-references](#filter-options-for-cross-references)
- [Printing the cross-reference list](#printing-the-cross-reference-list)
- [Adding a new object to the cross-reference list](#adding-a-new-object-to-the-cross-reference-list)
- [Show overlapping accesses in the cross-reference list](#show-overlapping-accesses-in-the-cross-reference-list)
- [Filter overlapping accesses in the cross-reference list](#filter-overlapping-accesses-in-the-cross-reference-list)
- [Recreating the existing cross-reference list](#recreating-the-existing-cross-reference-list)
- [Displaying and editing cross-references in the Inspector window](#displaying-and-editing-cross-references-in-the-inspector-window)

## General information about cross references

### Introduction

The cross-reference list provides an overview of the use of objects and devices within the user program.

You can see which objects are interdependent, what relationships they have with one another and where the individual objects are located.

You can also jump directly to the reference location of an object.

### Uses of cross-references

The cross-reference list offers you the following advantages:

- When creating programs and making changes, keep track of the devices and objects used, such as blocks, operands, and tags.
- You can see whether the object uses other objects or is used by itself.
- You can filter the displayed cross-reference information by specific criteria.

  Predefined filters for source and reference objects are available to you to this purpose.
- To find relevant references more easily, use user-defined filters.
- From the cross-references, you jump directly to the reference location of the selected object via the link highlighted in blue.
- During a program test or when troubleshooting, you are informed of the following, for example:

  - In which block and by which command is an operand processed.
  - Which tag is used how and where.
  - Which block is called by which other block.
  - Cross-reference information for subordinate and higher-level structures.
- As part of the project documentation, the cross-references provide a comprehensive overview of all operands, memory areas, blocks, tags, screens etc. used.

> **Note**
>
> **Objects displayed in the cross-reference list**
>
> - Which objects you can display in the cross-reference list depends on the installed products.
> - As of TIA Portal V15 instructions with version identification can also be displayed with the cross-references.
>
>   Instructions without version identification are **not** displayed.

### Project upgrade

When upgrading a project to a higher TIA Portal version, the associated cross-reference information is automatically recreated.

This happens at the end of the upgrade process. The current project is opened after this and the cross-references are then available again.

To reorganize the cross-reference information yourself, use the "Recreate the cross-reference information" function.

---

**See also**

[Structure of the cross-reference list](#structure-of-the-cross-reference-list)
  
[Displaying the cross-reference list](#displaying-the-cross-reference-list)
  
[Editing cross-references in the Inspector window](#editing-cross-references-in-the-inspector-window)

## Structure of the cross-reference list

### Introduction

The cross-reference list enables the display of reference objects and lower-level objects for a source object selected in the project tree.

The source object is the object displayed first in the cross-reference list.

The display of the cross-references for an object is project- and device-specific.

You can also have multiple cross-reference lists open at the same time.

### Structure of the cross-reference list

The cross-reference list is opened as a table in an editor in the work area. A simpler version of the cross-reference list is displayed in the Inspector window in the "Info" tab.

When you have selected a source object and open the cross-reference list, the objects are displayed as follows:

- The source object is displayed as the first object in a grayed line.

  The source object is the object for which you have opened the cross-references.
- The source object and all the lower-level objects of this source object and the associated references are structured in a standard view.
- Lower-level objects are marked with a preceding blue square.
- If lower-level objects also have reference objects, they are displayed with a gray background in the object column and in an hierarchical structure.
- If an object is used several times, it is also displayed several times.
- The "Add new source object" button is displayed at the end of a filled cross-reference list.

  When you click on this button, you can add a new object to the cross-reference list.
- The source object and the lower-level object are collapsed in the Inspector window.

  Lower-level objects with reference objects are show with a gray background in the object column.

### Example

The graphic shows an example of the structure of the cross-reference list for a source object:

![Example](images/95918955531_DV_resource.Stream@PNG-en-US.png)

### Display of the newly added source objects

Objects which were inserted using the "Add new source object" button are displayed as follows:

- The newly added source objects are at the end of the cross-reference list and are automatically expanded.
- The source objects are initially displayed independently of the selected filter setting.
- Newly added objects are correctly sorted and the filter settings displayed accordingly after an update or upon selecting another filter.

### Columns in the cross-reference list

The cross-reference list has the following structure:

| Column | Content/meaning |
| --- | --- |
| Object | Name of the source object that was selected upon opening the cross-reference list.  The lower-level objects and the relevant reference objects are shown below it. |
| Reference location | The respective reference location of the objects, for example, a network |
| Reference type | Relationship between the source object and the referenced objects:  - "Uses": The source object uses this object. - "Used by": The source object is used by this object. - "Type -> Instance": The source object is a type of the referenced object. - "Instance -> Type": The source object is an instance of the referenced object. - "Group -> Element": The source object is a group of the referenced object. - "Element -> Group": The source object is an element of the referenced object. - "Defines": The source object defines the referenced object. - "Defined by": The source object is defined by the referenced object. |
| As | Additional information about the referenced objects, for example when a tag is used by several devices. |
| Access | Access type, for example:  - Read access to an operand (R) - Write access to an operand (W) - Call |
| Address | Address of the relevant object |
| Type | Type and language used to create the object |
| Device | Relevant device name, for example, "CPU_1" |
| Path | Path of the object in the project tree with specification of folders and groups |
| Comment | Comments on individual objects, if present |

---

**See also**

[General information about cross references](#general-information-about-cross-references)
  
[Displaying the cross-reference list](#displaying-the-cross-reference-list)

## Settings in the cross-reference list

### Settings in the cross-reference list

You can change the settings in the cross-reference list using the buttons in the toolbar and by selecting predefined filters.

### Settings using the buttons in the cross-reference list

The following settings can be made using the buttons:

- **"Update" button**

  Updates the contents displayed in the open cross-reference list.

  The displayed contents of the cross-reference list are updated with the current contents from the associated project.

  Automatic update is not carried out within the cross-reference list if data management has changed in the project.
- **"Expand all" button**

  Expands the entries in the current cross-reference list by opening all lower-level objects.
- **"Collapse all" button**

  Reduces the entries in the current cross-reference list by closing the lower-level objects.
- **"Save window settings" button**

  Saves the current window settings in the cross-reference list.

  This includes, for example, the columns displayed, the width of the columns and the arrangement of the columns.

  The relevant filter settings in the cross-reference list are **not** saved.

### Filter settings in the cross-reference list

You have the option of selecting predefined filters for displaying objects.

You have the following options for filter selection, which relate to source objects:

- **Show objects with references:**

  This setting shows all the lower-level objects below the source object with existing references.

  The setting is preset by default when the cross-reference list is opened. You can select a filter other than the default in the cross-reference editor.
- **Show objects without references:**

  This setting shows all the lower-level objects below the source object without references.

  These non-referenced objects are assigned the entry "no references available" in the column "Reference location".

  Lower-level elements without references are also displayed if their parent objects contain references.
- **Show unused objects:**

  This setting shows all the lower-level but unused objects below the source object.

  These unused objects are assigned the entry "Object is not used" in the column "Reference location".
- **Show all objects:**

  This setting shows all the lower-level objects below the source object with or without references.

You have the following options for filter selection, which relate to reference objects:

- **Show only "uses":**

  This setting only shows the used reference objects with the reference type "Uses", "Element -> Group", "Instance -> Type" and "Defines".
- **Show only "used by":**

  This setting shows all the reference objects with the usage type "Used by", "Group -> Element", "Type -> Instance" and "Defined by".
- **Show only local references:**

  This setting only shows local references that belong to a specific device (for example, to CPU_1).

### Sorting in the cross-reference list

The entries are displayed in alphabetical order, depending on the associated object, the associated device and the object type.

Associated objects are displayed one after another.

The following sorting criteria are applied:

- Sorting for source objects:

  - Object type
  - Object name
  - Number
- Sorting for referenced objects:

  - Assignment to device
  - Object name
  - Number

> **Note**
>
> **No sorting by name if more than 10,000 objects are displayed**
>
> If more than 10,000 objects are displayed in the cross-reference list, sorting by name is not done.
>
> In this case, a banner text notifies you that no sorting is currently available for the displayed objects.
>
> To activate sorting by name, click the link in the banner text. A dialog notifies you about the progress of the sorting.

### Display of columns in the cross-reference list

You can adapt the columns displayed in the cross-reference list in a user-specific manner in the shortcut menu.

The shortcut menu offers the following options:

- Showing or hiding selected columns
- Displaying all existing columns
- Optimizing the column width for the selected column or for all columns.

You can save the settings that you have made using the "Save window settings" button.

> **Note**
>
> **Showing or hiding selected columns**
>
> The columns "Object" and "Reference location" cannot be hidden in the cross-reference list.

### Adding new objects to the cross-reference list

You have the following options for inserting new source objects in an existing cross-reference list:

- By clicking the "Add new source object" button in the toolbar.
- By clicking in the first empty line at the end of the cross-reference list, which contains the text "Add new source object".

> **Note**
>
> **Multiple insertion of identical objects**
>
> If you insert an identical object multiple times in the cross-reference list, the duplicates are automatically removed after the next update.

## Displaying the cross-reference list

### Introduction

Depending on the object selected in the project tree or in the "Instructions" task card, all the cross-references belonging to this source object are displayed.

Alternatively, you have the following option to open the cross-reference list:

- Select the "Cross-reference" command from the "Tools" menu.
- Select "Cross-references" in the shortcut menu.
- Click on the icon for cross-references in the toolbar.
- Select an object in the project tree and click "F11".
- Select an instruction with version identification in the "Instructions" task card and click "F11".
- A simpler version of the cross-reference list is also displayed in the Inspector window in the "Info" > "Cross-references" tab.

  Click "Cross-reference information" in the shortcut menu of the object.

The cross-references for the respective selected object and for all its lower-level objects are always displayed.

The display of the cross-references for an object is project- and device-specific.

You can also have multiple cross-reference lists open at the same time.

> **Note**
>
> **Displaying cross-references**
>
> - Which objects you can display in the cross-reference list depends on the installed products.
> - If more than 50 objects were selected, these are collapsed in the cross-reference list.
> - If fewer than 50 objects were selected, these are expanded in the cross-reference list.

### Requirement

You have created a project which contains objects with references.

### Displaying cross-references

Proceed as follows to display cross-references in the cross-reference list:

1. Select the required object and open the cross-references, for example, using the shortcut menu.
2. The cross-reference list for the selected object is opened.

   - The relevant selected object is the "source object" and is at the top in the "Object" column.
   - In the column "Reference location", you can see the locations at which the objects shown in the cross-reference list can be used.
   - "Used by" and "Uses", for example, show the relations between the objects in the "Reference type" column.
3. To jump to the reference location of the relevant object, click the corresponding link.
4. The icons in the toolbar facilitate the following actions:

   - Update cross-reference list
   - Defining filters for the cross-reference list
   - Collapse entries
   - Expand entries
   - Saving settings for the cross-reference list
   - Checking whether the currently opened cross-reference list contains overlapping accesses.
   - Display of the overlapping accesses in a separate area below the project window
   - Adding new source objects
5. To sort the entries in the "Object" column, for example, in ascending or descending order, click the corresponding column header.

---

**See also**

[General information about cross references](#general-information-about-cross-references)
  
[Structure of the cross-reference list](#structure-of-the-cross-reference-list)

## Sorting the cross-reference list

### Introduction

Sorting for the displayed source and reference objects is executed by default for the cross-reference list.

This sorting is also displayed accordingly in the Inspector window.

> **Note**
>
> **No sorting by name if more than 10,000 objects are displayed**
>
> Please note that no sorting by name is possible if more than 10,000 objects are displayed in the cross-reference list.
>
> In this case, a banner text notifies you that no sorting is currently available for the displayed objects.
>
> If you click the link in the banner text, you can switch on the sorting. A dialog box is then displayed which informs you about the progress of the sorting.

### Sorting criteria for displaying cross-references

Sorting takes place according to the following criteria:

**For source objects and assigned objects:**

- By object type: The source objects are ordered by their object type and displayed together.
- By name: In alphanumeric order

**For reference objects:**

- By device: The reference objects for a device are displayed together.
- By object type: The reference objects are ordered by their object type and displayed together.
- By name: In alphanumeric order

**For the reference location:**

- By name: In alphanumeric order

### Requirements

You have created a project which contains objects with references.

### Sorting the cross-reference list

To sort the cross-reference list when more than 10,000 objects are displayed, follow these steps:

1. To sort the cross-reference list by name, click the link in the displayed banner text.

   Result: A dialog notifies you about the progress in sorting the cross-references.
2. The displayed objects are also shown sorted by name after the completion of the sorting process.

## Filter options for cross-references

This section contains information on the following topics:

- [Introduction to filtering of cross-references](#introduction-to-filtering-of-cross-references)
- [Structure of the filter dialog](#structure-of-the-filter-dialog)
- [Attributes, operators and values in the filter dialog](#attributes-operators-and-values-in-the-filter-dialog)
- [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)
- [Editing user-defined filters](#editing-user-defined-filters)
- [Deleting user-defined filters](#deleting-user-defined-filters)
- [Exporting and importing user-defined filters](#exporting-and-importing-user-defined-filters)
- [Setting a filter as the default setting](#setting-a-filter-as-the-default-setting)
- [Duplicating a filter](#duplicating-a-filter)
- [Filtering the cross-reference list](#filtering-the-cross-reference-list)

### Introduction to filtering of cross-references

#### Introduction

You have the option of filtering the cross-reference list in order to simplify the search for specific cross-references and to structure it better.

The valid filter setting is displayed in the drop-down list in the toolbar with a yellow background.

- System filter:

  You can select various system-defined filter settings for displaying the cross-references.

  These so-called "system filters" are always available in the drop-down list of the toolbar and cannot be deleted.
- User-defined filters:

  In addition, you can also create user-defined filters according to your own requirements.

  After they are created, user-defined filters are displayed in the drop-down list for filter selection below the system filters.

  You can modify, rename and delete the filters as required.

In the figure below you can see the system filters that are always available as well as two user-defined filters "Filter_1" and "Filter_2".

![Introduction](images/132355676299_DV_resource.Stream@PNG-en-US.png)

#### System-defined filter settings in the cross-reference list

The system filters shown in the upper area of the drop-down list are applicable to the displayed source objects.

The filter options shown in the lower area are used for the reference objects.

The following system filters are available:

- **Show objects with references:**

  This setting shows all the lower-level objects below the source object with existing references.

  The setting is preset by default when the cross-reference list is opened. You can select a filter other than the default in the cross-reference editor.
- **Show objects without references:**

  This setting shows all the lower-level objects below the source object without references.

  These non-referenced objects are assigned the entry "no references available" in the column "Reference location".

  Lower-level elements without references are also displayed if their parent objects contain references.
- **Show unused objects:**

  This setting shows all the lower-level but unused objects below the source object.

  These unused objects are assigned the entry "Object is not used" in the column "Reference location".
- **Show all objects:**

  This setting shows all the lower-level objects below the source object with or without references.
- **Show only "uses":**

  This setting only shows the used reference objects with the reference type "Uses", "Element -> Group", "Instance -> Type" and "Defines".
- **Show only "used by":**

  This setting shows all the reference objects with the usage type "Used by", "Group -> Element", "Type -> Instance" and "Defined by".
- **Show only local references:**

  This setting only shows local references which belong to a specific device (e.g. to CPU_1).

As soon as you have selected one of these system filters via the drop-down list, the associated cross-references are filtered and displayed in accordance with the selected criteria.

See also [Filtering the cross-reference list](#filtering-the-cross-reference-list).

#### User-defined filters in the cross-reference list

You can also create user-defined filters for the cross-references in addition to the system filters that are always available.

This is possible both in the cross-reference editor and in the Inspector window in the "Info > Cross-references" tab.

1. Open the cross-references and click the filter icon in the toolbar of the cross-reference editor.
2. In the subsequent dialog click "Create new filter" and enter the desired filter criteria.
3. Click "Apply" to display the associated cross-references in accordance with the selected filter criteria.

User-defined filters are displayed in the drop-drop-down list below the system filters with the preset name, for example as "Filter_1".

In contrast to the system filters, user-defined filters can be renamed, modified and deleted freely.

Invalid filters are displayed with a red background after being opened. These filters cannot be applied.

See also [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references).

### Structure of the filter dialog

#### Introduction

You can also create user-defined filters to display the cross-references.

Below you can find information on the structure of the filter dialog and the symbols used in the filter dialog.

#### Structure of the filter dialog

The filter dialog has the following structure:

![Structure of the filter dialog](images/95964013835_DV_resource.Stream@PNG-en-US.png)

The filter dialog contains:

- The drop-down list for selecting existing filters.

  The filter displayed at the top in the drop-down list is the system filter taken from the open cross-reference list.
- The icons for creating, duplicating and deleting filters.
- The icon for specifying a filter as the default.
- The icons for adding, deleting and moving filter criteria.
- The columns "Seq." (sequence), "Attributes", "Operator " and "Value".

  The "Seq." column shows the number of the respective filter criteria.

  In the remaining columns you define the criteria required for new filters.
- "Apply" button: When you exit the filter dialog with "Apply", the changes are saved in the current user profile and are applied in the lower-level editor in the cross-reference list.
- "Close" button: When you exit the filter dialog with "Close", the changes are applied in the current user profile but are not applied in the editor.

#### Icons in the filter dialog

The filter dialog shows the following icons in the toolbar:

| Icon | Meaning | Action |
| --- | --- | --- |
| ![Icons in the filter dialog](images/95936525835_DV_resource.Stream@PNG-de-DE.png) | Create new filter | Creates a new user-defined filter. |
| ![Icons in the filter dialog](images/95969335051_DV_resource.Stream@PNG-de-DE.png) | Duplicate selected filter | Duplicates the selected filter so that existing filter criteria can be applied and processed further. |
| ![Icons in the filter dialog](images/95969907083_DV_resource.Stream@PNG-de-DE.png) | Delete filter | Deletes the selected user-defined filter. The filter cannot be restored after it has been deleted!  Note: System filters cannot be deleted! |
| ![Icons in the filter dialog](images/95969155467_DV_resource.Stream@PNG-de-DE.png) | Apply filter as default setting | Applies the selected filter as default setting.   This filter is used when the cross-references are opened again. |
| ![Icons in the filter dialog](images/95969915915_DV_resource.Stream@PNG-de-DE.png) | Insert new criterion | Inserts a new filter criterion. |
| ![Icons in the filter dialog](images/95971883147_DV_resource.Stream@PNG-de-DE.png) | Delete criterion | Deletes the selected filter criterion. |
| ![Icons in the filter dialog](images/95971955979_DV_resource.Stream@PNG-de-DE.png) | Move criterion up | Moves the selected filter criterion one line up. |
| ![Icons in the filter dialog](images/95971964811_DV_resource.Stream@PNG-de-DE.png) | Move criterion down | Moves the selected filter criterion one line down. |

### Attributes, operators and values in the filter dialog

#### Core statement

You can also create user-defined filters to display the cross-references.

Below you can find information on attributes, operators and values in the filter dialog, as well as on the criteria you can use.

#### Attributes, operators and values in the filter dialog

To create a valid filter you have to define the associated attributes, operators and values.

When you click in the column "Attribute" or "Operator", a drop-down list is displayed from which you can select the desired entries.

The "Value" column is displayed with a red background when you have selected an attribute and an operator, but have not yet entered a valid value.

![Attributes, operators and values in the filter dialog](images/102498440331_DV_resource.Stream@PNG-en-US.png)

#### Rules for criteria in the filter dialog

The rules specified below have to be observed when creating a new user-defined filter:

- Filter criteria can be defined for source objects, for reference objects and for references.
- Source objects are not affected when a criterion only applies to one reference object or one reference.
- The filter criteria are applied in the specified order.

  > **Note**
  >
  > Note that the result of the first criterion is used as a specification for the second criterion, etc. Therefore the sequence of the criteria is also decisive.
  >
  > You can move the existing criteria "up" or "down" by using the corresponding symbols in the toolbar. To do so, select the criterion and then click the desired icon.
- Individual criteria are added in sequence, depending on the corresponding sequence number.

  Example: The first criteria has the sequence number "1", the second criteria "2" etc.
- The permissible operators for the respective attribute can be selected from the drop-down list in the "Operator" column. The drop-down list is displayed as soon as you click the corresponding line in the filter dialog.
- If a filter is invalid because no valid value has been entered as a criterion yet, for example, the "Value" column is displayed with a red background. Such an invalid filter can be stored but cannot be applied. In this case, you can only exit the filter dialog by using "Close".
- When a criterion applies to a structured source object, this source object is displayed with all the parents and child objects and their references.
- The parent objects of the structured source object are, if they are not affected, only displayed because of the hierarchy and thus without references and in gray.
- When a criterion applies to a structured reference object, this reference object is displayed with all its lower-level reference locations.
- When a criterion only applies to elements of a structured reference object, only the respective lower-level reference location is displayed.

### Creating user-defined filters for cross-references

#### Introduction

You can also create user-defined filters to display the cross-references.

After user-defined filters have been created and stored, they can also be selected via the drop-down list in the toolbar.

Newly created user-defined filters are available immediately in all currently open cross-reference editors.

This allows you to reduce the number of objects displayed in the cross-reference list and to search specifically for certain objects.

> **Note**
>
> **Creating user-defined filters**
>
> You can create user-defined filters in all cross-reference editors as well as in the Inspector window under "Info > Cross-references".
>
> The procedure is identical in all cross-reference editors.

#### Requirement for the creation of a user-defined filter

You have created a project which contains objects with references.

#### Creating a user-defined filter

To create user-defined filters for the cross-reference list, follow these steps:

1. Select the program blocks folder and open the cross-reference list by using the "Cross-references" shortcut menu command.
2. Click the filter icon in the toolbar of the open cross-reference list.

   The filter dialog opens and shows the criteria that meet the selected system filter.

   Example: You have selected the system filter "Show objects with references" before opening the filter dialog in the drop-down list. You now see the Attributes, Operators and Values defined for this system filter in the filter dialog.
3. Click the "Create new filter" icon.

   The newly defined filter name "Filter_1" is displayed in the drop-down list. The icons for adding new filter criteria are activated.
4. Define the associated attributes, operators and values.

   Permissible attributes and operators can be selected from drop-down lists. The drop-down lists are displayed as soon as you click in the corresponding line in the filter dialog.
5. If you need several criteria, click the "Create new criterion" icon:
6. Enter all criteria required for the new filter.
7. Assign a name for the new filter if you do not want to use the default name "Filter_1". You can enter the desired name directly in the drop-drop-down list.
8. Click "Close" if you want to store the new filter settings, but do not want them displayed immediately in the lower-level cross-reference editor.
9. Click "Apply" to display the new filter settings immediately in all lower-level cross-reference editors.

**Note**

Note that the result of the first criterion is used as a specification for the second criterion, etc. Therefore the sequence of the criteria is also decisive.

You can move the existing criteria "up" or "down" by using the corresponding symbols in the toolbar. To do so, select the criterion and then click the desired icon.

**Note**

If you enter a name in the drop-down list that already exists as a filter name, this filter is applied in the cross-reference editor.

The new filter is saved under the name suggested by the system (for example, "Filter_10") and can be selected via the drop-down list in the editor.

#### Result

When the filter dialog is exited with "Close", the new filter is stored but not applied. The new filter is not used until you select it from the drop-down list in the cross-reference editor.

When the filter dialog is exited with "Apply", the new filter is stored and is applied in the open cross-reference editors.

### Editing user-defined filters

#### Introduction

User-defined filters for the display of cross-references can be selected after they have been created via the drop-down list in the toolbar of the cross-reference editor.

In contrast to system filters, user-defined filters can be edited and renamed.

The toolbar contains the icons for creating and editing filters and filter criteria.

> **Note**
>
> **Renaming filters in the cross-references**
>
> Only user-defined filters can be renamed; system filters cannot be renamed and cannot be deleted either.

#### Requirement for editing a user-defined filter

You have created a project which contains objects with references.

At least one user-defined filter has been created for the cross-references.

For additional details, see: [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

#### Editing and renaming user-defined filters

To edit user-defined filters for the cross-reference list, follow these steps:

1. Select the program blocks folder and open the cross-reference list by using the "Cross-references" shortcut menu command.
2. Select the user-defined filter that you want to edit from the drop-down list.
3. Click the filter icon in the toolbar of the open cross-reference list.

   The filter dialog opens and shows the criteria that meet the selected filter.
4. Click the "Insert new criterion" icon in the toolbar.
5. Define the associated attributes, operators and values.

   Permissible attributes and operators can be selected from the drop-down lists. The drop-down lists are displayed as soon as you click in the corresponding line in the filter dialog.
6. Enter all criteria required for the new filter.
7. Click "Delete criterion" if you want to delete a filter criterion.
8. If you wish, assign a name for the new filter. You can enter the desired name directly in the drop-drop-down list.
9. Click "Close" if you want to store the new filter settings, but do not want them applied immediately in the lower-level cross-reference editor.
10. Click "Apply" to apply the new filter settings immediately in all lower-level cross-reference editors.

**Note**

Note that the result of the first criterion is used as a specification for the second criterion, etc. Therefore the sequence of the criteria is also decisive.

You can move the existing criteria "up" or "down" by using the corresponding symbols in the toolbar. To do so, select the criterion and then click the desired icon.

**Note**

If you enter a name in the drop-down list that already exists as a filter name, this filter is applied in the cross-reference editor.

The new filter is saved under the name suggested by the system (for example, "Filter_10") and can be selected via the drop-down list in the editor.

#### Result

When the filter dialog is exited with "Close", the modified filter is stored but not applied. The filter is not used until you click "Update" in the cross-reference editor.

When the filter dialog is exited with "Apply", the new filter is stored and is applied in the open cross-reference editors.

#### Invalid user-defined filters

If a user-defined filter becomes invalid through editing, for example, because a value has not been entered yet, the corresponding line in the filter dialog has a red background. This has the following effects:

- The filter cannot be used because the "Apply" button is not active.
- After the filter dialog has been closed, no changes are displayed in the editor.
- If you click "Update" in the cross-reference editor, the filter defined as the default setting is applied for the display of the cross-references.
- If no user-defined filter is defined as the default setting, the system filter "Show objects with references" is applied.

---

**See also**

[Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

### Deleting user-defined filters

#### Introduction

User-defined filters for the display of cross-references can be selected after they have been created via the drop-down list in the toolbar of the cross-reference editor.

In contrast to system filters, user-defined filters can also be deleted.

The toolbar contains the icons for deleting filters and filter criteria.

> **Note**
>
> **Renaming and deleting filters in the cross-references**
>
> Only user-defined filters can be deleted; system filters cannot be renamed and cannot be deleted either.

#### Requirement for deleting a user-defined filter

You have created a project which contains objects with references.

At least one user-defined filter has been created for the cross-references.

For more details, see: [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

#### Deleting user-defined filters

To delete user-defined filters for the cross-reference list, follow these steps:

1. Select the program blocks folder and open the cross-reference list by using the "Cross-references" shortcut menu command.
2. Select the user-defined filter that you want to delete from the drop-down list.
3. Click the filter icon in the toolbar of the open cross-reference list.

   The filter dialog opens and shows the criteria that meet the selected filter.
4. Click the "Delete filter" icon in the toolbar if you want to delete the selected filter irrevocably.
5. Exit the dialog with "Close" or "Apply".

**Note**

Keep in mind that the filter is deleted irrevocably without any further prompts as soon as the "Delete filter" icon is clicked.

#### Result

The selected filter was deleted and is no longer shown in the drop-down list.

### Exporting and importing user-defined filters

#### Introduction

After they have been created, user-defined filters for the display of cross-references can be exported and then imported again.

This has the advantage that you can also pass a filter on to other users when it has been created.

You use the functionality of the TIA Portal for the export and import of user-defined filters.

#### Requirement for exporting a user-defined filter

You have created a project which contains objects with references.

At least one user-defined filter has been created for the cross-references.

For more details, see: [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

#### Exporting user-defined filters

To export user-defined filters, follow the steps below:

1. Select the "Settings" command in the "Options" menu.

   The settings of the TIA Portal are displayed.
2. Select the "General" entry in the area navigation.
3. In the "Import/export settings" area, click on the "Export settings ..." button.

   The "Export settings" dialog opens.
4. Click "Deselect all" to select only the desired filter settings for the export.
5. Select the desired filter for the export under "Cross-references > User-defined filters".

   If you want to accept the settings selected from previous export operations, activate the check box "Use selection from a previous export file". Enter the file in the field.
6. Enter a file name for the initialization file in the "File name" box.
7. Click "Export" to export the selected filters.

#### Result

Settings are exported to a file with the extension ".tps14".

#### Importing user-defined filters

To import user-defined filters, follow the steps below:

1. Select the "Settings" command in the "Options" menu.

   The settings of the TIA Portal are displayed.
2. Select the "General" entry in the area navigation.
3. Click the "Import settings ..." button in the "Import/export settings" area.

   The "Export settings" dialog opens.
4. Select the desired file with the extension ".tps14".
5. Click "Open" to import the file.

**Note**

If a filter with an identical name already exists, it is overwritten by the import and is no longer available.

#### Result

The selected file is imported and, after a restart of the TIA Portal, the user-defined settings are applied to the cross-references.

### Setting a filter as the default setting

#### Introduction

You can select various system-defined filter settings for displaying the cross-references. You can select these so-called "system filters" from the drop-down list in the toolbar.

In addition, you can also create user-defined filters in accordance with your own requirements.

You have the option of setting any filter as the default setting for the display of cross-references.

If a filter is set as the default setting, this filter is always applied when the cross-references are opened.

> **Note**
>
> **Cross-reference list in the Inspector window: No user-defined default**
>
> When you open cross-reference information in the Inspector window in the "Info > Cross-references" tab, the standard filter "Show objects with references" is always applied.
>
> Setting default filters has no effect.
>
> After the first time that the cross-reference information is opened, the last selected filter remains active every time. Only upon closing the project is the filter reset to the system filter "Show objects with references".

#### Rules for the default setting of filters

The following rules apply for the default setting of filters:

- Only one filter can be selected as the default setting.
- The default filter is identified with the corresponding icon.
- Invalid filters can also be set as the default setting, but they cannot be applied.

  Instead of the invalid filter, the system filter "Show objects with references" is applied automatically when the cross-reference list is opened.

#### Requirements

You have created a project which contains objects with references.

#### Setting a filter as the default setting

To set a filter as the default setting for the display of cross-references, follow these steps:

1. Select the program blocks folder and open the cross-reference list by using the "Cross-references" shortcut menu command.
2. Select the filter that you want to set as the default from the drop-down list.
3. Click the filter icon in the toolbar of the open cross-reference list.

   The filter dialog opens and shows the criteria that meet the selected filter.
4. Click the "Apply filter as default setting" icon in the toolbar.
5. Click "Close" if you want to store the new default setting, but do not want it applied immediately in the lower-level cross-reference editor.
6. Click "Apply" to apply the new filter settings immediately in all lower-level cross-reference editors.

#### Result

When the filter dialog is exited with "Close", the new default setting is stored but not applied. The new default setting is not used until you click "Update" in the cross-reference editor.

When the filter dialog is exited with "Apply", the new default setting is stored and is applied in the open cross-reference editors.

---

**See also**

[Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

### Duplicating a filter

#### Introduction

You can use various system-defined filter settings (called system filters below), which can be selected via the drop-down list in the toolbar, to display the cross-references. In addition, you can also create user-defined filters in accordance with your own requirements.

You can duplicate an existing filter.

This facilitates the adding of further filter criteria.

#### Requirements

You have created a project which contains objects with references.

#### Duplicating a filter

Proceed as follows to duplicate a filter:

1. Select the program blocks folder and open the cross-reference list by using the "Cross-references" shortcut menu command.
2. Select the filter that you want to duplicate from the drop-down list.
3. Click the filter icon in the toolbar of the open cross-reference list.

   The filter dialog opens and shows the criteria that meet the selected filter.
4. On the toolbar, click the "Duplicate selected filter" icon.

   The filter is then duplicated and is displayed in the drop-down list under the new name "Filter_x".
5. Enter additional filter criteria as required or change the existing attributes, operators or values.

#### Result

When the filter dialog is exited, the duplicated filter is stored and is applied in the open cross-reference editors.

### Filtering the cross-reference list

#### Introduction

You can use various system-defined filter settings (called system filters below), which can be selected via the drop-down list in the toolbar, to display the cross-references.

In addition to the filter options already offered, you can also create user-defined filters in accordance with your own requirements.

The system filters are always available in the drop-down list for filter selection and cannot be deleted.

User-defined filters are displayed after creation in the drop-down list for filter selection below the system filters and can be deleted.

See also: [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)

#### Requirements

You have created a project which contains objects with references.

#### Filtering the cross-reference list

To filter the cross-reference list, follow these steps:

1. Select the required source object and open the associated cross-reference list using the "Cross-references" shortcut menu command.
2. Alternatively, you can open the cross-references by selecting objects in the project tree for which cross-references exist, for example:

   - A device
   - The "Program blocks" folder
   - A block
3. Then click the "Cross-references" icon in the toolbar of the TIA Portal.
4. In the opened cross-reference list, select the required filter setting via the drop-down list.

#### Result

The selected filter setting is applied for the objects displayed in the lower-level cross-reference editors.

## Printing the cross-reference list

### Introduction

In the print preview, you can view and print out the project documentation contents shown in the cross-reference list.

The "Project" > "Print preview" and "Project" > "Print" commands are available for this purpose in the TIA Portal.

The following rules apply to printing out:

- The cross-reference list is always expanded and printed with all existing columns (including the hidden columns).
- The set filter criteria are applied at the same time.
- The column width is automatically optimized.
- Any overlapping accesses displayed are not printed.
- Regardless of which object is selected in the cross-reference list, the printout always starts with the displayed source object.

> **Note**
>
> **Printing an empty cross-reference list**
>
> If the cross-reference list selected for printing contains no entries, an empty cross-reference list is printed out.
>
> A cross-reference list which is printed out without contents contains the note "There are no entries in cross reference list".

### Requirements

You have created a project which contains objects with references.

### Printing the cross-reference list

To print the cross-reference list, follow these steps:

1. Select an object from the cross-reference list and start the print preview via the "Project" > "Print preview" command.
2. Make sure that you print out the required cross-reference list and select the required options.
3. Start the printout using the "Project" > "Print" command.
4. In the following dialog box, select the required print options and click "OK".

### Result

The selected cross-reference list is printed out with the set print options.

## Adding a new object to the cross-reference list

### Introduction

Depending on the selected object, all cross-references belonging to this source object are displayed when the cross-reference list is opened.

You have the following options for inserting new source objects in an existing cross-reference list:

- By clicking the "Add new source object" button in the toolbar.
- By clicking in the first empty line at the end of the cross-reference list, which contains the text "Add new source object".

> **Note**
>
> **No undoing or repeating when inserting source objects**
>
> Note that the "Undo and redo operations" functionality is not available for newly inserted source objects.

### Requirement

You have created a project which contains objects with references.

### Adding a new object to the cross-reference list

To add new objects to the cross-reference list, follow these steps:

1. Open an existing cross-reference list.
2. Click the "Add new source object" button and enter the required object.

   When an existing object is inserted, you are supported by the intelligent preselection.

   The object is inserted as the last object in the cross-reference list.
3. To apply the current filter selection to the new object, click the "Refresh" button in the toolbar.

**Note**

**Multiple insertion of identical objects**

If you insert an identical object multiple times in the cross-reference list, the duplicates are automatically removed after the next update.

### Result

The newly added object is displayed at the end of the cross-reference list, unfolded.

## Show overlapping accesses in the cross-reference list

### Introduction

The overlapping access to a selected object can be displayed in a second window in the lower part of the cross-reference list.

The display of the overlapping access cannot be saved and is no longer available after the cross-reference list is opened again.

### Definition

Overlapping access for tags and structured tags is determined based on the absolute addresses.

We refer to "overlapping access" if the address for a tag or structured tag is partly or completely in the address space of the associated source object.

> **Note**
>
> **Displaying "overlapping access"**
>
> - Overlapping accesses are only displayed for structured objects whose assigned memory area overlaps with the memory area of other structured objects.
> - The overlapping accesses are only displayed for a single selected object in the cross-reference list.
> - If several objects are selected in the cross-references shown, no overlapping access is displayed.

### Example

The following graphic shows the cross-reference list with the display of the overlapping accesses of "StructuredTag_1":

![Example](images/139680195595_DV_resource.Stream@PNG-en-US.png)

### Requirement

A project is created that contains overlapping accesses to objects.

### Showing overlapping access in the cross-reference list

Proceed as follows to display overlapping access in the cross-reference list:

1. Open the cross-reference list and click the "Check overlapping accesses" button in the toolbar.

   Result: All objects that have overlapping access are marked with the corresponding overlapping access symbol in the "Object" column.
2. In the upper part of the cross-reference list, select a marked object and click the "Show overlapping access" button.

   Result: The overlapping access to the selected object is displayed in a second window with the header "Overlapping accesses of: <ObjectName>".

   > **Note**
   >
   > **Display of the overlapping access**
   >
   > The display of the overlapping access cannot be saved and is no longer shown after the cross-reference list is opened again.
   >
   > To show the overlapping access again, perform the steps described above.
3. To only show the write access for the overlapping tags, click the "Write access only" checkbox.

   Result: The lower window of the cross-reference list only shows the overlapping accesses that have only "write" or "read and write" access to the selected object.

![Showing overlapping access in the cross-reference list](images/139684698763_DV_resource.Stream@PNG-en-US.png)

## Filter overlapping accesses in the cross-reference list

### Introduction

The overlapping accesses to a selected object displayed in the lower part of the cross-reference list can be filtered.

The following filter criteria for overlapping accesses are available:

- Write access
- Read and write access

This allows you to filter for overlapping objects that have either write or read and write access.

Overlapping objects that have read-only access are not displayed.

If the "Write access only" option is cleared, you will see all existing overlapping objects, regardless of whether there is read access, write access, or read and write access.

### Requirement

A project is created that contains overlapping accesses to objects.

### Filter overlapping accesses in the cross-reference list

Proceed as follows to filter overlapping access in the cross-reference list:

1. Open the cross-reference list and click the "Check overlapping accesses" button in the toolbar.

   Result: All objects that have overlapping access are marked with the corresponding overlapping access symbol in the "Object" column.
2. In the upper part of the cross-reference list, select a marked object and click the "Show overlapping access" button.

   Result: The overlapping access to the selected object is displayed in a second window with the header "Overlapping accesses of: <ObjectName>".
3. In the detail view header of the overlapping objects, click the "Write access only" button to enable the filter function.

   Result: The detail view shows only the overlapping accesses that have write access or read and write access.

![Filter overlapping accesses in the cross-reference list](images/139684698763_DV_resource.Stream@PNG-en-US.png)

## Recreating the existing cross-reference list

### Introduction

You can perform a reorganization of the cross-reference information. This involves recreating an existing cross-reference list.

Reorganization is useful in the following cases, for example:

- Entries are missing
- Entries are displayed twice in the cross-reference list.
- The referenced object is no longer found.

This function is also performed during a project upgrade to a higher TIA Portal version.

### Recreate the cross-reference information

To create new cross-references, follow these steps:

1. In the menu bar of the Project view, select "Options > Settings > General > Cross-references".

   The settings for TIA Portal under "Cross-references" open.
2. To start the process, click the "Recreate the cross-reference information" button.
3. Check the message in the Inspector window when the restore is complete:

   - If the process was successful, you receive a message which you confirm with "OK".
   - If the process was not successful, you receive an error message.
4. To close the displayed banner text, click the "Refresh" button in the cross-reference list.

### Result

The new cross-reference information for the selected project was created.

**Performance**

This function takes only a short time regardless of the size of the project.

In a typical system configuration, an existing cross-reference list is fully created again within seconds.

## Displaying and editing cross-references in the Inspector window

This section contains information on the following topics:

- [Displaying cross-references in the Inspector window](#displaying-cross-references-in-the-inspector-window)
- [Editing cross-references in the Inspector window](#editing-cross-references-in-the-inspector-window)

### Displaying cross-references in the Inspector window

#### Introduction

The Inspector window displays cross-reference information about an object you have selected in the "Info > Cross-references" tab.

If you select an object in any editor in the TIA Portal or in the "Instructions" or "Extended Instructions" task card, the associated references to the selected object are shown in this tab.

To display the tab in the Inspector window, select the option "Cross-reference information" in the shortcut menu of the object. The option "Cross-references" opens the cross-reference editor in the work area.

> **Note**
>
> **Displaying instructions**
>
> - From TIA Portal V15 onward, instructions with version identification can also be displayed for the cross-references and in the Inspector window.
> - Instructions without version identification are not displayed.

#### Toolbar

You can perform the following actions from the toolbar:

| Object | Meaning |
| --- | --- |
| "Collapse all" icon | Collapse all the entries of the displayed source objects |
| "Expand all" icon | Expand all the entries of the displayed source objects |
| Filter drop-down list | Select system filters or user-defined filters |
| "Filter" icon | Create or edit a user-defined filter |
| "Freeze/unfreeze cross-reference list" icon | Freezing the display of the cross-reference list in the Inspector window  As long as the button is activated, the same source object is always displayed, even if, for example, you click another object in the navigation tree. |
| Option "Show parent objects" | Displaying parent objects for the selected reference  This option is only displayed in the toolbar on the right-hand border if parent objects exist for the reference. |

#### Layout of the table area

The Inspector window displays the cross-reference information in tabular format.

The table consists of the following columns:

| Column | Content/meaning |
| --- | --- |
| Object | Name of the source object that was selected upon opening the cross-reference list.  The lower-level objects and the relevant reference objects are shown below it. |
| Reference location | The respective reference location of the objects, for example, a network |
| Reference type | Relationship between the source object and the referenced objects:  - "Uses": The source object uses this object. - "Used by": The source object is used by this object. - "Type -> Instance": The source object is a type of the referenced object. - "Instance -> Type": The source object is an instance of the referenced object. - "Group -> Element": The source object is a group of the referenced object. - "Element -> Group": The source object is an element of the referenced object. - "Defines": The source object defines the referenced object. - "Defined by": The source object is defined by the referenced object. |
| As | Additional information about the referenced objects, for example when a tag is used by several devices. |
| Access | Access type, for example:  - Read access to an operand (R) - Write access to an operand (W) - Call |
| Address | Address of the relevant object |
| Type | Type and language used to create the object |
| Device | Relevant device name, for example, "CPU_1" |
| Path | Path of the object in the project tree with specification of folders and groups |
| Comment | Comments on individual objects, if present |

#### Displaying cross-references in the Inspector window

To display cross-reference information in the Inspector window, follow these steps:

1. Select the required object, for example, in the project tree or in the program editor.
2. Click "Cross-reference information" in the shortcut menu.

   Result: The references to the selected object are displayed in the Inspector window in the "Info" > "Cross-references" tab.

> **Note**
>
> Only the cross-reference information for supported objects is displayed in the Inspector window.
>
> If, for example, you select a folder, you will not receive any cross-reference information for it.

### Editing cross-references in the Inspector window

#### Introduction

The Inspector window displays cross-reference information about an object you have selected in the "Info > Cross-references" tab.

You can customize the display of the cross-references, for example, to display parent objects of the source object.

#### Displaying cross-references in the Inspector window

To display cross-reference information in the Inspector window, follow these steps:

1. Select the required object, for example, in the project tree or in the program editor.
2. Click "Cross-reference information" in the shortcut menu.

   Result: The references to the selected object are displayed in the Inspector window in the "Info" > "Cross-references" tab.

   > **Note**
   >
   > Only the cross-reference information for supported objects is displayed in the Inspector window.
   >
   > If, for example, you have selected a folder, you will not receive any cross-reference information for it.

#### Freezing the display of the cross-reference list in the Inspector window

To freeze the displayed cross-reference list in the Inspector window, follow these steps:

1. Select the required object, for example, in the project tree or in the program editor.
2. Click "Cross-reference information" in the shortcut menu.

   Result: The references to the selected object are displayed in the Inspector window in the "Info" > "Cross-references" tab.
3. Select the reference for which you want to display the cross-reference information.
4. Click the "Freeze/unfreeze cross-reference list" button.

   The displayed information on the currently selected object remains visible and is not changed, even if you select other objects in the list.

   The view then remains frozen until you unfreeze it or close the editor.
5. Click the "Freeze/unfreeze cross-reference list" button again to unfreeze the view.

> **Note**
>
> **Frozen view even when the filter is changed**
>
> When you change the filter for the view of the cross-reference information when the view is "frozen", the selected object still remains frozen even if the display of the newly filtered objects changes.

#### Displaying parent objects for selected cross-references

Proceed as follows to display to a selected structured object along with the parent objects in the cross-reference list:

1. Select the required object, for example, in the project tree or in the program editor.
2. Click "Cross-reference information" in the shortcut menu.

   Result: The references to the selected object are displayed in the Inspector window in the "Info" > "Cross-references" tab.
3. Select the reference for which you want to display the parent cross-reference information.

   If parent objects exist for the reference, the option "Show parent objects" is displayed on the right-hand border of the toolbar.
4. Select the "Show parent objects" check box to display existing parent objects.

   Result: The parent and child objects of the selected objects are displayed.

   > **Note**
   >
   > **Restrictions when displaying parent objects**
   >
   > - If the selected object does not have any parent objects, the "Show parent objects" option is not displayed.
   > - If more than one object has been selected for which the cross-references are to be displayed, the "Show parent objects" option is not displayed.
   > - Display of the parent objects depends on the filters set in the cross-reference list.
   >
   >   Only if the selected filter permits the display of parent objects are they displayed.

#### Editing and filtering cross-references in the Inspector window

You also have the option of editing and filtering cross-reference information in the Inspector window.

**Filtering cross-references in the Inspector window**

The procedure for filtering cross-reference information is identical to the procedure in the cross-reference editor.

However, in contrast to what happens in the cross-reference editor, upon opening the tab, the standard filter "Show objects with references" is always applied. Setting default filters has no effect.

After the first time that the cross-reference information is opened, the last selected filter remains active every time. Only upon closing the project is the filter reset to the system filter "Show objects with references".

See also:

- [Creating user-defined filters for cross-references](#creating-user-defined-filters-for-cross-references)
- [Deleting user-defined filters](#deleting-user-defined-filters)
- [Filtering the cross-reference list](#filtering-the-cross-reference-list)

---

**See also**

[Inspector window](Configuring%20devices%20and%20networks.md#inspector-window)
