---
title: "Declaring named value data types (S7-1500)"
package: ProgNamedValueTypesenUS
topics: 5
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Declaring named value data types (S7-1500)

This section contains information on the following topics:

- [Document-based programming (S7-1500)](#document-based-programming-s7-1500)
- [Creating named value data types (S7-1500)](#creating-named-value-data-types-s7-1500)
- [Declaring named value data types (S7-1500)](#declaring-named-value-data-types-s7-1500-1)
- [Renaming named value data types (S7-1500)](#renaming-named-value-data-types-s7-1500)

## Document-based programming (S7-1500)

### Introduction

You declare named value data types in text documents. The documents have the file name extension *.nvt.

### Advantages

For example, document-based programming offers the following advantages:

- Documents are compatible with all TIA Portal versions as of V19.

  This supports the creation of standardized modules or libraries.
- You can edit documents outside the TIA Portal.

  Program changes can be made with a standard editor. No installation of the TIA Portal is required.
- You can create documents automatically.
- You can exchange data with other engineering applications.

### Basics for programming in documents

You can create, open, or delete documents in two different ways:

- In the project tree of the TIA Portal

  Documents for named value data types are located in the "PLC data types" subfolder.
- In the file system outside of the TIA Portal

  Documents for named value data types are located in the project directory, in the subfolder "src\&lt;PLC name&gt;\UNITS\&lt;Software unit name&gt;\TYPES".

You also have two options for editing documents:

- A text editor is available in the TIA Portal.
- Outside the TIA Portal, you can edit documents with standard text editors.

Changes to documents are automatically synchronized:

- Changes that you make in the TIA Portal are transferred to the document in the file system after the project has been saved.
- Changes that you make outside the TIA Portal are transferred to the TIA Portal after the document has been saved.

  In the Inspector window of the TIA Portal, you receive messages about all changes that have been made outside.

  If you create, rename or delete the documents outside TIA Portal, the action stack of TIA Portal for redoing actions is emptied. This means that the actions which were performed before this time in TIA Portal cannot be undone anymore.

The figure below shows the storage of the documents "nvtTrafficLight.nvt" and "nvtColors.nvt" in the project tree and in the file system:

![Basics for programming in documents](images/170627543435_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Storage of the documents in the project tree |
| ② | Storage of the documents in the file system |

> **Note**
>
> **No automatic updating of reference locations**
>
> Since named value data types are programmed document-based, reference locations are not updated automatically. If you, for example, rename a named value data type, the reference locations in the PLC program are not modified automatically. Instead, a syntax error is reported during compilation. Then update the reference locations manually.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **No user management by the TIA Portal**  The user management available in TIA Portal under "Security settings" does not relate to documents in the file system. Therefore, you should use standard Windows user management and access protection tools for this. |  |

### Versioning using Version Control Interface (VCI)

Versioning of Named value data types using Version Control Interface is possible if you export and import the documents from the file system. Named value data types cannot be exported or imported together with the project from the TIA Portal to VCI.

---

**See also**

[Basics of named value data types (S7-1500)](Data%20types.md#basics-of-named-value-data-types-s7-1500)
  
[Using the keyboard in the program editor](Program%20editor.md#using-the-keyboard-in-the-program-editor)

## Creating named value data types (S7-1500)

### Requirement

The "PLC data types" folder within a software unit is open. You can create named value data types only within software units.

### Procedure

To create a named value data type, follow these steps:

1. In the "PLC data types" folder, double-click the "Add new data type" command.

   The "Add new data type" dialog opens.
2. Select the category "Named value data type".
3. Type a name for the named value data type.
4. Optional: Enter a namespace for the new named value data type or apply the default namespace of the software unit that is already entered in the input field.

   You can find information on namespaces, in particular on the naming conventions according to IEC 61131-3, here: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)
5. Select a base data type.
6. Optional: Activate the "Published" option if you also want to reference the data type outside the software unit as well.

### Result

A document is created that contains the new named value data type. It has the file name extension "*.nvt".

The document appears in the following locations:

- In the project tree of the TIA Portal
- In the file system outside TIA Portal after you save the project.

  The documents are located under the following path: `<myProject>\src\<myPLC>\UNITS\<mySoftwareUnit>\TYPES`

---

**See also**

[Document-based programming (S7-1500)](#document-based-programming-s7-1500)
  
[Basics of named value data types (S7-1500)](Data%20types.md#basics-of-named-value-data-types-s7-1500)
  
[Using the keyboard in the program editor](Program%20editor.md#using-the-keyboard-in-the-program-editor)

## Declaring named value data types (S7-1500)

You declare named value data types in text documents. The documents have the file name extension *.nvt.

By default, a document contains a named value data type. However, it is also possible to combine multiple data types into one document. The following descriptions assume that each document contains one data type.

### Requirement

- The "PLC data types" folder in the project tree is open.
- A document (*.nvt) is created.

### Procedure

To declare a named value data type, follow these steps:

1. Double click a document (*.nvt) in the project tree.

   The document opens. It already contains a template for declaration.
2. Declare the named value data type and the named values it contains according to the expected syntax.  
   See also: [Basics of named value data types](Data%20types.md#basics-of-named-value-data-types-s7-1500)  
   Please also observe the naming rules according to IEC 61131-3, which apply within software units.

   See also: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

### Result

The named value data type is declared and can now be used in the program.

---

**See also**

[Document-based programming (S7-1500)](#document-based-programming-s7-1500)
  
[Using the keyboard in the program editor](Program%20editor.md#using-the-keyboard-in-the-program-editor)

## Renaming named value data types (S7-1500)

You declare named value data types in text documents. The documents have the file name extension *.nvt. By default, a document contains a named value data type. However, it is also possible to combine multiple data types into one document. Renaming documents in the project navigation therefore does not result in the included named value data types also being renamed.

### Requirement

The "PLC data types" folder within a software unit is open and contains a document (*.nvt).

### Procedure

To rename a named value data type, follow these steps:

1. Double click a document (*.nvt) in the project tree.

   The document opens.
2. Enter a new name in the declaration.
3. To synchronize the name change with the file system, save the project.

### Result

The named value data type is renamed.

> **Note**
>
> **No automatic updating of reference locations**
>
> Since named value data types are programmed document-based, reference locations are not updated automatically. If you, for example, rename a named value data type, the reference locations in the PLC program are not modified automatically. Instead, a syntax error is reported during compilation. Then update the reference locations manually.

---

**See also**

[Document-based programming (S7-1500)](#document-based-programming-s7-1500)
  
[Basics of named value data types (S7-1500)](Data%20types.md#basics-of-named-value-data-types-s7-1500)
