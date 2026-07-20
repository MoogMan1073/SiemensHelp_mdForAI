---
title: "Import SIMATIC AX libraries into TIA Portal"
package: ProgAXenUS
topics: 6
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Import SIMATIC AX libraries into TIA Portal

This section contains information on the following topics:

- [Overview of SIMATIC AX](#overview-of-simatic-ax)
- [Workflow for creating and opening libraries with SIMATIC AX program elements](#workflow-for-creating-and-opening-libraries-with-simatic-ax-program-elements)
- [Object-oriented programming in SIMATIC AX libraries](#object-oriented-programming-in-simatic-ax-libraries)
- [Generating a global library with SIMATIC AX program elements](#generating-a-global-library-with-simatic-ax-program-elements)
- [Opening the global library in the TIA Portal](#opening-the-global-library-in-the-tia-portal)

## Overview of SIMATIC AX

### Overview

With AX Code, SIMATIC AX provides a development environment for developing, compiling and testing programs in a text-based and object-oriented manner. While the focus of STEP 7 (TIA Portal) is more on the area of OT (Operation Technology), SIMATIC AX consistently concentrates on the area of IT (Information Technology).

Programs created with SIMATIC AX can be integrated in STEP 7 in TIA Portal.

The development, the test and the compilation of the program code are performed with SIMATIC AX in this way. The hardware configuration, the compilation of the machine code and the loading of the program onto the hardware are performed with STEP 7 (TIA Portal).

![Overview](images/160166622987_DV_resource.Stream@PNG-de-DE.png)

The first expansion stage of SIMATIC AX involves compiling libraries in the development environment and exporting them with AX2TIA. Handover library documents are created, which are transferred to the TIA Portal. The TIA Portal Library Generator generates global libraries from these documents. The libraries can be opened and used in TIA Portal.

You can find fundamental information on programming with SIMATIC AX in the Help on SIMATIC AX.

To stay up-to-date, you become part of the SIMATIC AX community.

You can find both at: <https://axciteme.siemens.com/>

---

**See also**

[Community](https://github.com/simatic-ax)

## Workflow for creating and opening libraries with SIMATIC AX program elements

### Workflow

The following figure shows how SIMATIC AX libraries can be imported into the TIA Portal.

You need the following tools:

- AX2TIA  
  The tool is included in the scope of delivery of SIMATIC AX.
- TIA Portal Library Importer  
  The tool is included in the scope of delivery of the TIA Portal. It can be opened from SIMATIC AX via a script if SIMATIC AX and the TIA Portal are installed on the same computer.

![Workflow](images/170768080907_DV_resource.Stream@PNG-de-DE.png)

### Basic procedure

To import SIMATIC AX libraries into TIA Portal, the following steps are required. You can find a detailed description of the entire workflow in the SIMATIC AX documentation at: <https://axciteme.siemens.com/>

1. Programming libraries with SIMATIC AX

   You use the "Structured Text (ST)" language for programming.

   The libraries can contain the following program elements:

   - Code blocks
   - PLC data types (UDT)
2. Create handover library documents

   To do this, use the "AX2TIA" tool. This tool is included in the scope of delivery of SIMATIC AX.
3. Generating a global library with SIMATIC AX program elements

   You use the TIA Portal Library Importer for this. You can find this tool in the TIA Portal installation directory. From there, you can call it directly via the command prompt. If SIMATIC AX is installed on the same computer as the TIA Portal, you can also open the tool from SIMATIC AX via a script.

   You can find information on generating global TIA Portal libraries with the TIA Portal Library Importer here:

   [Generating a global library with SIMATIC AX program elements](#generating-a-global-library-with-simatic-ax-program-elements).
4. Opening the global library in the TIA Portal

   You can find information on opening libraries in TIA Portal here:

   [Opening the global library in the TIA Portal](#opening-the-global-library-in-the-tia-portal).
5. Use program elements in the TIA Portal project

   You can use SIMATIC AX program elements in your PLC program in the TIA Portal and load them into the CPU. The program elements are write-protected in the TIA Portal.

   When object-oriented programs are imported, additional program elements are created, for example, FBs for classes and FCs for methods. The program elements are displayed in the "Program blocks" folder of the project tree, but they cannot be used in the program.
6. Debug PLC program with SIMATIC AX

   To fix errors in the PLC program, you access the CPU online with SIMATIC AX. You then have the possibility to observe the PLC program and set watch points.
7. Versioning SIMATIC AX libraries

   SIMATIC AX libraries can be versioned. The version information is applied in the global library in TIA Portal.

   If you want to use a versioned library in more than one instance of the TIA Portal, first generate the handover library documents and the file .al[version number] centrally. Then distribute the file .al[version number] to the TIA Portal instances.

   To generate additional versions of the library, follow the same process. In this way, you achieve consistent versioning of the library in all TIA Portal instances.

You can also use the AX web IDE in a cloud workspace to create handover library documents. You must then transfer the handover library documents to a Windows computer on which TIA Portal is installed. In this case, you can call the TIA Portal Library Importer manually to generate the Global Library.

### Restrictions

The following restrictions apply to SIMATIC AX libraries in the TIA Portal:

- Program elements from SIMATIC AX libraries run on S7-1500 with FW version 2.9 or higher.
- PLC data types (UDT) from SIMATIC AX libraries can only be assigned to PLC data types of the same type. Assignment to structurally identical PLC data types of other types is not possible. However, you can assign individual elements to each other.
- If you change the name or namespace of an imported program element in TIA Portal, you can no longer debug the program element with SIMATIC AX afterwards.
- Namespaces in the TIA Portal can only be used within Software Units. If you use an imported program element outside Software Units, it loses its namespace. This means that you cannot debug the program element with SIMATIC AX.

You can find information on additional restrictions in the Help on SIMATIC AX. <https://axciteme.siemens.com/>

## Object-oriented programming in SIMATIC AX libraries

### Overview

SIMATIC AX offers the option of object-oriented programming. Object-oriented programming (OOP) supports the creation of clearly arranged and modularly structured PLC programs.

Detailed information on OOP in SIMATIC AX can be found here: [https://axciteme.siemens.com/](https://console.simatic-ax.siemens.io/docs/st/language/oop)

### Classes and methods in imported libraries

Object-oriented PLC programs can be imported into TIA Portal. After the import, classes are represented as function blocks (FB) and methods as functions (FC).

Depending on the structure of the object-oriented AX program, additional program elements, for example, FCs, are created during import.

> **Note**
>
> **Errors when using program elements from object-oriented programs**
>
> Function blocks that represent classes and functions that represent methods are displayed in the project tree in the "Program blocks" folder, but they cannot be used in the program. This also applies to all other program elements that are created during the import of object-oriented programs. You are notified by an error message if you still try to use such an element.

## Generating a global library with SIMATIC AX program elements

### Requirement

You have handover library documents in *.json and *.impl format.

### Procedure

1. Open the command prompt in Windows.
2. Navigate to the "bin" folder in the installation directory of the TIA Portal.
3. Run the file "Siemens.Simatic.Lang.Library.Importer.exe" and enter at least the parameters `-i` and `-o` for the input and output directory.

   The following parameters are supported:

   `-i` Input directory containing the source files (impl and json)

   `-o` Output directory and name of the global library

   `-h` Show help

   If a global library with this name already exists, a prompt appears asking if the existing global library should be overwritten or updated:

   - The "Overwrite" option deletes the existing library and creates a new library.
   - The "Update" option keeps the existing library and creates a new, additional version of the library.
   - The "Cancel" option aborts the import.

### Result

The global library is created in the *.al[version number] format in the specified output directory.

## Opening the global library in the TIA Portal

### Requirements

- The "Libraries" task card is opened.
- You have a global library in the format ".al[version number]".

### Procedure

To open a global library, follow these steps:

1. Click the "Open global library" icon in the toolbar of the "Global libraries" pane or select the command "Global libraries > Open library" in the "Options" menu.

   The "Open global library" dialog box opens.
2. Select the global library you want to open. Library files are identified by the file name extension ".al[version number]".
3. Click "Open".

### Result

The global library is displayed in the "Global libraries" palette.

The global library is write-protected.

The types in the library have the "Structured Text (ST)" compilation language.
