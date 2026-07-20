---
title: "Technology objects"
package: TOOpennessenUS
topics: 51
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology objects

This section contains information on the following topics:

- [Overview of functions for technology objects](#overview-of-functions-for-technology-objects)
- [Overview of technology objects and versions](#overview-of-technology-objects-and-versions)
- [Overview of data types](#overview-of-data-types)
- [Querying the composition of technology objects](#querying-the-composition-of-technology-objects)
- [Creating technology object](#creating-technology-object)
- [Deleting technology object](#deleting-technology-object)
- [Creating group for technology objects](#creating-group-for-technology-objects)
- [Deleting group for technology objects](#deleting-group-for-technology-objects)
- [Compiling technology object](#compiling-technology-object)
- [Enumerating technology object](#enumerating-technology-object)
- [Enumerating groups for technology objects](#enumerating-groups-for-technology-objects)
- [Finding technology object](#finding-technology-object)
- [Enumerating parameters of technology object](#enumerating-parameters-of-technology-object)
- [Finding parameters of technology object](#finding-parameters-of-technology-object)
- [Reading parameters of technology object](#reading-parameters-of-technology-object)
- [Writing parameters of technology object](#writing-parameters-of-technology-object)
- [S7-1200 Motion Control](#s7-1200-motion-control)
- [S7-1500 Motion Control](#s7-1500-motion-control)
- [PID control](#pid-control)
- [Counting](#counting)
- [Easy Motion Control](#easy-motion-control)

## Overview of functions for technology objects

TIA Portal Openness supports a selection of technology object functions for defined tasks that you can call outside the TIA Portal by means of the Public API.

In the following chapters you will find code sample, that can be adapted to your openness program.

### Functions

The following functions are available for technology objects:

- [Querying the composition of technology objects](#querying-the-composition-of-technology-objects)
- [Creating technology object](#creating-technology-object)
- [Deleting technology object](#deleting-technology-object)
- [Creating group for technology objects](#creating-group-for-technology-objects)
- [Deleting group for technology objects](#deleting-group-for-technology-objects)
- [Compiling technology object](#compiling-technology-object)
- [Enumerating technology object](#enumerating-technology-object)
- [Enumerating groups for technology objects](#enumerating-groups-for-technology-objects)
- [Finding technology object](#finding-technology-object)
- [Enumerating parameters of technology object](#enumerating-parameters-of-technology-object)
- [Finding parameters of technology object](#finding-parameters-of-technology-object)
- [Reading parameters of technology object](#reading-parameters-of-technology-object)
- [Writing parameters of technology object](#writing-parameters-of-technology-object)
- [Exporting technology objects](Technology%20objects.md#exporting-technology-objects)
- [Importing technology objects](Technology%20objects.md#importing-technology-objects)
- [Connecting to Hardware components](#s7-1500-motion-control)

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[Applications](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#applications)
  
[TIA Portal Openness object model](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#tia-portal-openness-object-model)

## Overview of technology objects and versions

### Technology objects

The following table shows the available technology objects in the Public API.

| CPU | Technology | Technology object | Version of technology object | CPU FW |
| --- | --- | --- | --- | --- |
| S7-1200 | Motion Control | TO_PositioningAxis | ≥ V6.0 | ≥ V4.2 |
| TO_CommandTable |  |  |  |  |
| PID Control | PID_Compact | ≥ V2.3 | ≥ V4.2 |  |
| PID_3Step | V2.3 |  |  |  |
| PID_Temp | V1.1 |  |  |  |
| S7-1500 | Motion Control | TO_SpeedAxis | ≥ V3.0 | ≥ V2.0 |
| TO_PositioningAxis |  |  |  |  |
| TO_ExternalEncoder |  |  |  |  |
| TO_SynchronousAxis |  |  |  |  |
| TO_OutputCam |  |  |  |  |
| TO_CamTrack |  |  |  |  |
| TO_MeasuringInput |  |  |  |  |
| TO_Cam (S7-1500T)<sup>1)</sup> |  |  |  |  |
| TO_Kinematics (S7-1500T) | ≥ V4.0 | ≥ V2.6 |  |  |
| TO_LeadingAxisProxy (S7-1500T) | ≥ V5.0 | ≥ V2.8 |  |  |
| TO_Cam_10k (S7-1500T)<sup>1)</sup> | ≥ V6.0 | ≥ V2.9 |  |  |
| TO_Interpreter (S7-1500T) | ≥ V8.0 | ≥ V3.1 |  |  |
| TO_InterpreterMapping (S7-1500T)<sup>2)</sup> |  |  |  |  |
| TO_InterpreterProgram (S7-1500T)<sup>2)</sup> |  |  |  |  |
| Counting and measurement | High_Speed_Counter | ≥ V4.1 | Any |  |
| SSI_Absolute_Encoder | ≥ V3.1 |  |  |  |
| PID Control | PID_Compact | ≥ V2.3 | ≥ V2.0 |  |
| PID_3Step | V2.3 |  |  |  |
| PID_Temp | V1.1 |  |  |  |
| CONT_C | V1.1 | Any |  |  |
| CONT_S |  |  |  |  |
| TCONT_CP |  |  |  |  |
| TCONT_S |  |  |  |  |
| S7-300/400 | PID Control | CONT_C | V1.1 | Any |
| CONT_S |  |  |  |  |
| TCONT_CP |  |  |  |  |
| TCONT_S |  |  |  |  |
| TUN_EC<sup>2)</sup> |  |  |  |  |
| TUN_ES<sup>2)</sup> |  |  |  |  |
| PID_CP<sup>2)</sup> | V2.0 |  |  |  |
| PID_ES<sup>2)</sup> |  |  |  |  |
| EMC | AXIS_REF | V2.0 |  |  |
| <sup>1)</sup> The technology object does not support the following Openness functions: Writing parameters.   <sup>2)</sup> The technology object does not support the following Openness functions: Enumerating parameters, Finding parameters, Reading parameters, Writing parameters. |  |  |  |  |

---

**See also**

[S7-1500 Motion Control](#s7-1500-motion-control)

## Overview of data types

The data types of technology object parameters in TIA Portal are mapped to C# data types in the Public API.

### Data types

The following table shows the data type mapping:

| Format | Data type in TIA Portal | Data type in C# |
| --- | --- | --- |
| Binary numbers | Bool | bool |
|  | BBool | bool |
|  | Byte | byte |
|  | Word | ushort |
|  | DWord | uint |
|  | LWord | ulong |
| Integers | SInt | sbyte |
|  | Int | short |
|  | Dint | int |
|  | LInt | long |
|  | USInt | byte |
|  | UInt | ushort |
|  | UDint | uint |
|  | ULInt | ulong |
| Floating-point numbers | Real | float |
|  | LReal | double |
|  | Time | double |
| Character strings | Char | char |
|  | WChar | char |
|  | String | string |
|  | WString | string |
| Hardware data types | HW_* | ushort |
|  | Block_* | ushort |
| * Placeholder for device type extension in TIA Portal project |  |  |

## Querying the composition of technology objects

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Program code

Modify the following program code to get all technology objects of a PLC:

// Retrieves all technology objects of a PLC

private static void GetTechnologicalObjectsOfPLC(PlcSoftware plcSoftware)

{

    TechnologicalInstanceDBGroup technologicalObjectGroup = plcSoftware.TechnologicalObjectGroup;

    TechnologicalInstanceDBComposition technologicalObjects = technologicalObjectGroup.TechnologicalObjects;

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)

## Creating technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Application

Only technology objects that are listed in the section [Overview of technology objects and versions](#overview-of-technology-objects-and-versions) can be created. An exception is thrown for unsupported technology objects or invalid parameters. See also [Handling exceptions](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#handling-exceptions).

### Program code

Modify the following program code to create a technology object and add it to an existing PLC:

// Create a technology object and add to technology object composition

private static void CreateTechnologicalObject(PlcSoftware plcSoftware)

{

    TechnologicalInstanceDBComposition technologicalObjects = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects;

    string nameOfTO = "PID_Compact_1"; // How the technology object should be named

    string typeOfTO = "PID_Compact"; // How the technology object type is called, e.g. in  
    // "Add new technology object"-dialog

    Version versionOfTO = new Version("2.3"); // Version of technology object

    TechnologicalInstanceDB technologicalObject = technologicalObjects.Create(nameOfTO, typeOfTO, versionOfTO);

}

Possible values and combinations of name, type and version of the technology object can be found in the section [Overview of technology objects and versions](#overview-of-technology-objects-and-versions).

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[S7-1500 Motion Control](#s7-1500-motion-control)

## Deleting technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- The technology object exists.  
  See [Finding technology object](#finding-technology-object)

### Program code

Modify the following program code to delete a technology object:

// Delete a technology object from DB composition and from PLC

private static void DeleteTechnologicalObject(TechnologicalInstanceDB technologicalObject)

{

    technologicalObject.Delete();

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)

## Creating group for technology objects

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Program code

Modify the following program code to create a group for technology objects:

private static void CreateTechnologicalObjectGroup(PlcSoftware plcsoftware)

//Create a user group for technology objects

{

TechnologicalInstanceDBGroup systemGroup = plcsoftware.TechnologicalObjectGroup;

TechnologicalInstanceDBUserGroupComposition groups = systemGroup.Groups;

TechnologicalInstanceDBUserGroup myGroup = groups.Create("MySubGroupName");

}

## Deleting group for technology objects

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Program code

Modify the following program code to delete a group for technology objects:

private static void DeleteTechnologicalObjectGroup(PlcSoftware plcsoftware)

// Delete groups for technology objects

{

TechnologicalInstanceDBGroup group

= plcsoftware.TechnologicalObjectGroup.Groups.Find("myGroup");

TechnologicalInstanceDBUserGroupComposition subgroups = group.Groups;

TechnologicalInstanceDBUserGroupComposition subgroup = subgroups.Find("myUserGroup");

if (subgroup != null)

{

subgroup.Delete();

}

}

## Compiling technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- The technology object exists.  
  See [Creating technology object](#creating-technology-object)

### Program code: Compiling a technology object

Modify the following program code to compile a technology object:

// Compile a single technology object

private static void CompileSingleTechnologicalObject(TechnologicalInstanceDB technologicalObject)

{

    ICompilable singleCompile = technologicalObject.GetService&lt;ICompilable&gt;();

    CompilerResult compileResult = singleCompile.Compile();

}

### Program code: Compiling the technology object group

Modify the following program code to compile the technology object group:

// Compile technology object group

private static void CompileTechnologicalObjectGroup(PlcSoftware plcSoftware)

{

    TechnologicalInstanceDBGroup technologicalObjectGroup = plcSoftware.TechnologicalObjectGroup;

    ICompilable groupCompile = technologicalObjectGroup.GetService&lt;ICompilable&gt;();

    CompilerResult compileResult = groupCompile.Compile();

}

### Compile results

Technology objects compilation results are stored recursively.

You can find an example of recursive evaluation of compilation results in the section "[Compiling a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#compiling-a-project)".

> **Note**
>
> **Further parameters**
>
> Imported data will be expanded after compiling. For example, You can use Openness to create motion control technology objects with different versions. After the compiling of technology objects, the motion control versions of other technology objects are adapted to those of the last technology object created.

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)

## Enumerating technology object

### Requirement

You can enumerate the top level TOs like "TO_Axis" and "TO_Cam". To find sub level TOs like "TO_OutputCam" see [Creating and finding TO_OutputCam, TO_CamTrack and TO_MeasuringInput](#creating-and-finding-to_outputcam-to_camtrack-and-to_measuringinput).

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Program code

Modify the following program code to enumerate technology objects:

// Enumerate all technology objects

private static void EnumerateTechnologicalObjects(PlcSoftware plcSoftware)

{

    TechnologicalInstanceDBComposition technologicalObjects = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects;

    foreach (TechnologicalInstanceDB technologicalObject in technologicalObjects)

    {

     // Do something ...

    }

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[S7-1500 Motion Control](#s7-1500-motion-control)

## Enumerating groups for technology objects

### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Application

Subgroups are taken into account recursively for enumeration.

### Program code: Enumerating all groups

Modify the following program code to enumerate the groups for technology objects:

//Enumerates all groups for technology objects

private static void EnumerateRecursively(PlcSoftware sw)

{

foreach (TechnologicalInstanceDBUserGroup group in sw.TechnologicalObjectGroup.Groups)

{

EnumerateRecursivelySubGroups (group);

}

}

//Enumerates all included sub groups

private static void EnumerateRecursivelySubGroups(TechnologicalInstanceDBUserGroup group)

{

foreach (TechnologicalInstanceDBUserGroup subGroup in group.Groups)

{

EnumerateRecursivelySubGroups (subGroup);

// recursion

}

}

### Program code: Accessing a group

Modify the following program code to access a selected user-defined group for technology objects:

//Gives individual access to a specific group for technology objects

private static void AccessTechnologicalInstanceDBUserGroup(PlcSoftware sw)

{

TechnologicalInstanceDBUserGroupComposition groups = sw.TechnologicalObjectGroup.Groups;  
 TechnologicalInstanceDBUserGroup userGroup = groups.Find("MyUserfolder");

}

## Finding technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)

### Program code

Modify the following program code to find a specific technology object:

// Find a specific technology object by its name

private static void FindTechnologicalObject(PlcSoftware plcSoftware)

{

    TechnologicalInstanceDBComposition technologicalObjects = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects;

    string nameOfTO = "PID_Compact_1";

    TechnologicalInstanceDB technologicalObject = technologicalObjects.Find(nameOfTO);

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)

## Enumerating parameters of technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- A technology object exists.  
  See [Creating technology object](#creating-technology-object) or [Finding parameters of technology object](#finding-parameters-of-technology-object)
- The [technology object](#overview-of-technology-objects-and-versions) supports this function.

### Program code

Modify the following program code to enumerate parameters of a specific technology object:

// Enumerate parameters of a technology object

private static void EnumerateParameters(PlcSoftware plcSoftware)

{

    string nameOfTO = "PID_Compact_1";

    TechnologicalInstanceDB technologicalObject = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find(nameOfTO);

    foreach (TechnologicalParameter parameter in technologicalObject.Parameters)

    {

     // Do something ...

    }

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[Finding technology object](#finding-technology-object)

## Finding parameters of technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- A technology object exists.  
  See [Creating technology object](#creating-technology-object)
- The [technology object](#overview-of-technology-objects-and-versions) supports this function.

### Program code

Modify the following program code to find parameters of a specific technology object:

// Find parameters of a technology object

private static void FindParameterOfTechnologicalObject(PlcSoftware plcSoftware)

{

    string nameOfTO = "PID_Compact_1";

    TechnologicalInstanceDB technologicalObject = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find(nameOfTO);

    string nameOfParameter = "Config.InputUpperLimit";

    TechnologicalParameter parameter = technologicalObject.Parameters.Find(nameOfParameter);

}

### Parameters of different technology objects

[Parameters of S7-1200 Motion Control](#s7-1200-motion-control)

[Parameters of S7-1500 Motion Control](#s7-1500-motion-control)

[Parameters of PID Control](#pid-control)

[Parameters of Counting](#counting)

[Parameters of Easy Motion Control](#easy-motion-control)

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[Finding technology object](#finding-technology-object)

## Reading parameters of technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- A technology object exists.  
  See [Creating technology object](#creating-technology-object)
- The [technology object](#overview-of-technology-objects-and-versions) supports this function.

### Program code

Modify the following program code to read parameters of a specific technology object:

// Read parameters of a technology object

private static void ReadParameterOfTechnologicalObject(PlcSoftware plcSoftware)

{

    string nameOfTO = "PID_Compact_1";

    TechnologicalInstanceDB technologicalObject = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find(nameOfTO);

    string nameOfParameter = "Config.InputUpperLimit";

    TechnologicalParameter parameter = technologicalObject.Parameters.Find(nameOfParameter);

    // Read from parameter

    string name = parameter.Name;

    object value = parameter.Value;

}

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[Finding technology object](#finding-technology-object)

## Writing parameters of technology object

### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A PLC is determined in the project.  
  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- A technology object exists.  
  See [Creating technology object](#creating-technology-object)
- The [technology object](#overview-of-technology-objects-and-versions) supports this function.

### Exception

An EngineeringException is thrown if:

- You set a new value for a parameter that does not provide write access.
- A new value for a parameter is of an unsupported type.

### Program code

Modify the following program code to write parameters of a specific technology object:

// Write parameters of a technology object

private static void WriteParameterOfTechnologicalObject(PlcSoftware plcSoftware)

{

    string nameOfTO = "PID_Compact_1";

    TechnologicalInstanceDB technologicalObject = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find(nameOfTO);

    string nameOfParameter = "Config.InputUpperLimit";

    TechnologicalParameter parameter = technologicalObject.Parameters.Find(nameOfParameter);

    // Write to parameter if the value is writable

    object value = 3.0;

    parameter.Value = value;

}

### Parameters of different technology objects

[Parameters of S7-1200 Motion Control](#s7-1200-motion-control)

[Parameters of S7-1500 Motion Control](#s7-1500-motion-control)

[Parameters of PID Control](#pid-control)

[Parameters of Counting](#counting)

[Parameters of Easy Motion Control](#easy-motion-control)

---

**See also**

[Standard libraries](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#standard-libraries)
  
[Finding technology object](#finding-technology-object)

## S7-1200 Motion Control

This section contains information on the following topics:

- [Connecting PTO-Outputs](#connecting-pto-outputs)
- [Connecting PROFIdrives by hardware address](#connecting-profidrives-by-hardware-address)
- [Connecting encoders for PROFIdrives by hardware address](#connecting-encoders-for-profidrives-by-hardware-address)
- [Connecting analog drives by hardware address](#connecting-analog-drives-by-hardware-address)
- [Connecting encoders for analog drives by hardware address](#connecting-encoders-for-analog-drives-by-hardware-address)
- [Connecting drives by data block](#connecting-drives-by-data-block)
- [Connecting encoders by data block](#connecting-encoders-by-data-block)
- [Parameters for TO_PositioningAxis and TO_CommandTable](#parameters-for-to_positioningaxis-and-to_commandtable)

### Connecting PTO-Outputs

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC with PTO-Outputs is determined in the project.
- The technology object exists.  
  See [Creating technology object](#creating-technology-object).

#### **Program code**

Modify the following program code to connect a PTO-Output to the "TO_PositioningAxis".

//An instance of the technology object axis is already available in the program before

private static void ConnectingDrive(TechnologicalInstanceDB technologicalObject)

{

   //Set axis to PTO mode

   technologicalObject.Parameters.Find("Actor.Type").Value = 2;

   //Set PTO-Output

   technologicalObject.Parameters.Find("_Actor.Interface.PTO").Value = 0; // select Pulse_1

   // 0 = Pulse_1

   // 1 = Pulse_2

   // 2 = Pulse_3

   // 3 = Pulse_4

}

### Connecting PROFIdrives by hardware address

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- A PROFIdrive is available in the project and connected with the S7-1200 PLC.
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect a PROFIdrive by hardware address to the "TO_PositioningAxis".

//An instance of the technology object axis is already available in the program before

private static void ConnectingDrive(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to PROFIdrive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 1;

    //Set axis to drive mode

    technologicalObject.Parameters.Find("_Actor.Interface.DataConnection").Value = 0;

    //Set connection to address of drive. The output will be set automatically.

    technologicalObject.Parameters.Find("_Actor.Interface.ProfiDriveIn").Value = "%I68.0";

    technologicalObject.Parameters.Find("Sensor[1].Interface.Number").Value = 1;

    // 1 = Encoder1, 2 = Encoder2;

}

### Connecting encoders for PROFIdrives by hardware address

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- A PROFIdrive is available in the project and connected with the S7-1200 PLC.
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect an encoder by hardware address to the "TO_PositioningAxis":

//An instance of the technology object axis is already available in the program before

private static void ConnectingEncoder(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to PROFIdrive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 1;

    //Set the encoder mode

    technologicalObject.Parameters.Find("_Sensor[1].Interface.EncoderConnection").Value = 7;

    //Set axis to use PROFINET encoder

    technologicalObject.Parameters.Find("_Sensor[1].Interface.DataConnection").Value = 0;

    //Set connection to address of drive. The output will be set automatically.

    technologicalObject.Parameters.Find("_Sensor[1].Interface.ProfiDriveIn").Value = "%I68.0";

    technologicalObject.Parameters.Find("Sensor[1].Interface.Number").Value = 1;

    // 1 = Encoder1, 2 = Encoder2;

}

### Connecting analog drives by hardware address

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- An analog drive is available in the project and connected with the S7-1200 PLC.
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect an analog drive by hardware address to the "TO_PositioningAxis":

//An instance of the technology object axis is already available in the program before

private static void ConnectingEncoder(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to analog drive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 0;

    //Set axis to drive mode

    technologicalObject.Parameters.Find("_Actor.Interface.DataConnection").Value = 0;

    //Set connection to analog address of drive

    technologicalObject.Parameters.Find("_Actor.Interface.Analog").Value = "%QW64";

}

### Connecting encoders for analog drives by hardware address

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- An analog drive is available in the project and connected with the S7-1200 PLC.
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect an encoder by hardware address to the "TO_PositioningAxis":

//An instance of the technology object axis is already available in the program before

//Connecting by High Speed Counter mode

private static void ConnectingEncoder(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to analog drive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 0;

    //Set encoder for high-speed counter mode

    technologicalObject.Parameters.Find("_Sensor[1].Interface.EncoderConnection").Value = 4;

    technologicalObject.Parameters.Find("_Sensor[1].Interface.HSC.Name").Value = "HSC_1";

}

    //An instance of the technology object axis is already available in the program before

    //Connecting by PROFINET/PROFIBUS telegram

    private static void ConnectingEncoder(TechnologicalInstanceDB

    technologicalObject)

{

    //Set axis to analog drive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 0;

    //Set encoder for PROFINET/PROFIBUS mode

    technologicalObject.Parameters.Find("_Sensor[1].Interface.EncoderConnection").Value = 7;

    technologicalObject.Parameters.Find("_Sensor[1].Interface.DataConnection").Value = "Encoder";

    technologicalObject.Parameters.Find("_Sensor[1].Interface.ProfiDriveIn").Value = "%I68.0";

    technologicalObject.Parameters.Find("Sensor[1].Interface.Number").Value = 1;

    // 1 = Encoder1, 2 = Encoder2;

}

### Connecting drives by data block

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- A data block is available in the project and set to "Not optimized".

  For the PROFIdrive axis type, the data block contains a tag of the type e. g. PD_TEL3.

  For an analog drive, the data block contains a tag with the word data type.
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect a PROFIdrive by data block to the "TO_PositioningAxis".

//An instance of the technology object axis is already available in the program before

private static void ConfigureDrivewithDataBlock(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to PROFIdrive mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 1;

    //Set axis to data block mode

    technologicalObject.Parameters.Find("_Actor.Interface.DataConnection").Value = 1;

    //Set the tag in the data block

    technologicalObject.Parameters.Find("_Actor.Interface.DataBlock").Value = "Data_block_1.Member_of_type_PD_TEL3";

}

#### Program code

Modify the following program code to connect an analog drive by data block to the "TO_PositioningAxis".

//An instance of the technology object axis is already available in the program before

//Connecting an analog drive with data block.

private static void ConfigureDrivewithDataBlock(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to analog mode

    technologicalObject.Parameters.Find("Actor.Type").Value = 0;

    //Set the tag in the data block

    technologicalObject.Parameters.Find("_Actor.Interface.Analog").Value = "Data_block_1.Static_1";

}

### Connecting encoders by data block

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1200 PLC is determined in the project.
- A data block is available in the project and set to "Not optimized".

  In case of PROFIdrive the data block contains a tag of the type e. g. PD_TEL3
- The technology object exists.

  See [Creating technology object](#creating-technology-object).

#### Program code

Modify the following program code to connect an encoder by data block:

//An instance of the technology object axis is already available in the program before

private static void ConfigureEncoderwithDataBlock(TechnologicalInstanceDB technologicalObject)

{

    //Set axis to PROFIdrive mode depending by axis type. 1 = PROFIdrive, 0 = Analog Drive.

    technologicalObject.Parameters.Find("Actor.Type").Value = 1;

    //Set the encoder mode

    technologicalObject.Parameters.Find("_Sensor[1].Interface.EncoderConnection").Value = 7;

    //Set axis to data block mode

    technologicalObject.Parameters.Find("_Sensor[1].Interface.DataConnection").Value = 1;

    //Set the tag in the data block. For PD_TEL3 and PD_TEL4 "Encoder1" or "Encoder2".

    technologicalObject.Parameters.Find("_Sensor[1].Interface.DataBlock").Value = "Data_block_1.Member_of_Type_PD_TEL3";

}

### Parameters for TO_PositioningAxis and TO_CommandTable

You can find a list of all available variables in SIMATIC STEP 7 S7-1200 Motion Control function manual on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109773400).

> **Note**
>
> In TIA Portal in the Parameter view of the technology object configuration you can find the column "Name in Openness".

## S7-1500 Motion Control

This section contains information on the following topics:

- [Creating and finding TO_OutputCam, TO_CamTrack and TO_MeasuringInput](#creating-and-finding-to_outputcam-to_camtrack-and-to_measuringinput)
- [Parameters of S7-1500 Motion Control](#parameters-of-s7-1500-motion-control)
- [Connecting drives](#connecting-drives)
- [Connecting telegram 750](#connecting-telegram-750)
- [Connecting encoders](#connecting-encoders)
- [Connecting output cams and cam tracks to hardware](#connecting-output-cams-and-cam-tracks-to-hardware)
- [Connecting measuring inputs to hardware](#connecting-measuring-inputs-to-hardware)
- [Connecting synchronous axis with leading values](#connecting-synchronous-axis-with-leading-values)
- [Connecting conveyor tracking of kinematics with leading values](#connecting-conveyor-tracking-of-kinematics-with-leading-values)
- [Exporting and importing technology object cam (S7-1500T)](#exporting-and-importing-technology-object-cam-s7-1500t)
- [Load and save the source code of an interpreter program (S71500T)](#load-and-save-the-source-code-of-an-interpreter-program-s71500t)

### Creating and finding TO_OutputCam, TO_CamTrack and TO_MeasuringInput

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500 PLC is determined in the project.
- A technology object of the type TO_PositioningAxis, TO_SynchronousAxis or TO_ExternalEncoder is determined in the project.

#### Application

The output cam, cam track and measuring input technology objects are associated with positioning axis, synchronous axis or external encoder technology objects. In order to access an output cam, cam track or measuring input technology object you use the service OutputCamMeasuringInputContainer.

#### Program code: Creating and finding output cam, cam track and measuring input technology objects

Modify the following program code to create or find an output cam, cam track or measuring input technology object:

/*An instance of the technology object under which the TO_OutputCam, TO_CamTrack or TO_MeasuringInput should be created is already available in the program before*/

private static void CreateFind_OutputcamCamtrackMeasuringinput(TechnologicalInstanceDB technologyObject)

{

    //Retrieve service OutputCamMeasuringInputContainer

    OutputCamMeasuringInputContainer container =

    technologyObject.GetService&lt;OutputCamMeasuringInputContainer&gt;();

    //Get access to TO_OutputCam / TO_CamTrack container

    TechnologicalInstanceDBComposition outputcamCamtrackContainer = container.OutputCams;

    //Find technology object TO_OutputCam or TO_CamTrack

    TechnologicalInstanceDB outputCam = outputcamCamtrackContainer.Find("OutputCamName");

    TechnologicalInstanceDB camTrack = outputcamCamtrackContainer.Find("CamTrackName");

    //Create new technology object TO_OutputCam or TO_CamTrack

    TechnologicalInstanceDB newOutputCam =

    outputcamCamtrackContainer.Create("NewOutputCamName", "TO_OutputCam",

    new Version(3, 0));

    TechnologicalInstanceDB newCamTrack =

    outputcamCamtrackContainer.Create("NewCamTrackName", "TO_CamTrack", new Version(3, 0));

    //Get access to TO_MeasuringInput container

    TechnologicalInstanceDBComposition measuringInputContainer = container.MeasuringInputs;

    //Find technology object TO_MeasuringInput

    TechnologicalInstanceDB measuringInput =

    measuringInputContainer.Find("MeasuringInputName");

    //Create new technology object TO_MeasuringInput

    TechnologicalInstanceDB newMeasuringInput =

    measuringInputContainer.Create("NewMeasuringInput", "TO_MeasuringInput",

    new Version(3, 0));

}

You create the S7-1500 technology objects OutputCam, CamTrack and MeasuringInput as a master copy from Siemens.Engineering.Library.MasterCopies.MasterCopy.

/*An instance of the technology object under which the TO_OutputCam, TO_CamTrack or TO_MeasuringInput should be created is already available in the program before*/

// sourceMasterCopy contains master copy object output cam

private static void CreateFind_OutputcamCamtrackMeasuringinput(TechnologicalInstanceDB technologyObject, MasterCopy sourceMasterCopy)

{

    //Retrieve service OutputCamMeasuringInputContainer

    OutputCamMeasuringInputContainer container = technologyObject.GetService&lt;OutputCamMeasuringInputContainer&gt;();

    TechnologicalInstanceDB result = container.OutputCams.CreateFrom(sourceMasterCopy);

}

### Parameters of S7-1500 Motion Control

This section contains information on the following topics:

- [Basics](#basics)
- [Axis and Encoder](#axis-and-encoder)
- [Leading axis proxy](#leading-axis-proxy)
- [Measuring input](#measuring-input)
- [Output cam and cam track](#output-cam-and-cam-track)
- [Kinematics](#kinematics)
- [Interpreter](#interpreter)

#### Basics

##### Parameters of S7-1500 Motion Control

Most parameters of S7-1500 Motion Control technology objects are directly mapped to data block tags, but there are also some additional parameters that do not map directly to data blocks.

##### Parameters mapped directly to technology object data block tags

You have access to all technology object data block tags as described in general except of:

- Read-only tags
- Tags of data type VREF
- Tags of "InternalToTrace" structure
- Tags of "ControlPanel" structure

Some technology parameters that map to read-only data block tags are writeable in the PublicAPI. The allowed values are the same ones as for the underlying data block tags.

The affected parameters are listed for all technology objects in the following chapters.

##### Program code

Modify the following program code to access the directly mapped parameters:

//An instance of the technology object is already available in the program before

private static void ReadWriteDataBlockTag(TechnologicalInstanceDB technologyObject)

{

    //Read value from data block tag "ReferenceSpeed"

    double value =

    (double)technologyObject.Parameters.Find("Actor.DriveParameter.ReferenceSpeed").Value;

    //Write data block tag "ReferenceSpeed"

    technologyObject.Parameters.Find("Actor.DriveParameter.ReferenceSpeed").Value = 3000.0;

}

##### Parameters not mapped directly to technology object data block tags

S7-1500 Motion Control technology objects are connected to other devices or technology objects. The information about this connections is stored in additional parameters as well as informations about units of measure. Additional paremeters are not dircetly mapped to technology object data block tags.

The affected parameters are listed for all technology objects in the following chapters.

##### Program code: Additional parameters

Modify the following program code to access the additional parameters:

//An instance of the technology object is already available in the program before

private static void ReadWriteAdditionalParameter(TechnologicalInstanceDB technologyObject)

{

    //Read additional parameter "_Properties.MotionType"

    uint value = (uint)technologyObject.Parameters.Find("_Properties.MotionType").Value;

    //Write additional parameter "_Properties.MotionType"

    technologyObject.Parameters.Find("_Properties.MotionType").Value = 1;

}

##### Additional information

You can find additional information in SIMATIC S7-1500 Motion Control function manuals:

[https://support.industry.siemens.com/cs/ww/en/view/109751049](https://support.industry.siemens.com/cs/ww/en/view/109751049)

#### Axis and Encoder

##### Parameters mapped directly to technology object data block tags

For axis and external encoder technology objects, the following read-only data block tags are writable in the PublicAPI.

| Name in Openness | Name in function view | Possible value | Data type in Openness | TO_SpeedAxis | TO_PositioningAxis  TO_SynchronousAxis | TO_ExternalEncoder |
| --- | --- | --- | --- | --- | --- | --- |
| Actor.Type | Drive type | 0: Analog output  1: PROFIdrive telegram | int | X | X | - |
| Actor.Interface.EnableDriveOutput | "Enable output" for analog drives | True, False | bool | X | X | - |
| Actor.Interface.DriveReadyInput | "Ready input" for analog drives | True, False | bool | X | X | - |
| Actor.Interface.EnableTorqueData | Torque data | True, False | bool | - | X | - |
| VirtualAxis.Mode | Virtual axis | 0, 1 | uint | X | X | - |
| Sensor[n].Existent<sup>1)</sup> | Use encoder | True, False | bool | - | X | - |
| Sensor[n].Interface.Number<sup>1)</sup> | Number of the encoder in the telegram | 1 … 2 | uint | - | X | - |
| Sensor[n].Type<sup>1)</sup> | Encoder type | 0: Incremental  1: Absolute  2: Cyclic absolute | int | - | X | - |
| Sensor.Interface.Number | Number of the encoder in the telegram | 1 … 2 | uint | - | - | X |
| Sensor.Type | Encoder type | 0: Incremental  1: Absolute  2: Cyclic absolute | int | - | - | X |
| CrossPlcSynchronousOperation.Interface[n].EnableLeadingValueOutput<sup>5)</sup> | Provide cross-PLC leading value | True, False | bool | - | X | X |
| <sup>1)</sup> S7-1500 PLC: n=1; S7-1500T PLC: 1≤n≤4   <sup>5)</sup> V5.0 n=1; ≥V6.0 1≤n≤8 |  |  |  |  |  |  |

##### Parameters not mapped directly to technology object data block tags

For axis and external encoder technology objects, the following additional parameters are available.

| Name in Openness | Name in function view | Possible value | Data type in Openness | TO_SpeedAxis | TO_PositioningAxis  TO_SynchronousAxis | TO_ExternalEncoder |
| --- | --- | --- | --- | --- | --- | --- |
| _Actor.DataAdaptionOffline | Automatically apply... | True, False | bool | X | X | - |
| _Actor.Interface.Telegram | Drive telegram | Telegram number<sup>2)</sup> | uint | X | X | - |
| _Actor.Interface.EnableDriveOutputAddress | Drive output address | PublicAPI-object | SW.Tags.PlcTag | X | X | - |
| _Actor.Interface.DriveReadyInputAddress | Drive ready input address | PublicAPI-object | SW.Tags.PlcTag | X | X | - |
| _Units.LengthUnit | Position units | See tag Units.LengthUnit<sup>3)</sup> | uint | - | X | X |
| _Units.VelocityUnit | Velocity units | See tag Units.VelocityUnit<sup>3)</sup> | uint | X | X | X |
| _Units.TorqueUnit | Torque units | See tag Units.TorqueUnit<sup>3)</sup> | uint | X | X | - |
| _Units.ForceUnit | Force units | See tag Units.ForceUnit<sup>3)</sup> | uint | - | X | - |
| _Sensor[n].DataAdaptionOffline<sup>1)</sup> | Automatically apply... | True, False | bool | - | X | - |
| _Sensor[n].Interface.Telegram<sup>1)</sup> | Encoder telegramm | Telegram number<sup>2)</sup> | uint | - | X | - |
| _Sensor[n].ActiveHoming.DigitalInputAddress<sup>1)</sup> | Digital input | PublicAPI-object | SW.Tags.PlcTag | - | X | - |
| _Sensor[n].PassiveHoming.DigitalInputAddress<sup>1)</sup> | Digital input | PublicAPI-object | SW.Tags.PlcTag | - | X | - |
| _Sensor.DataAdaptionOffline | Automatically apply... | True, False | bool | - | - | X |
| _Sensor.Interface.Telegram | Encoder telegram | Telegram number<sup>2)</sup> | uint | - | - | X |
| _Sensor.ActiveHoming.DigitalInputAddress | Digital input | PublicAPI-object | SW.Tags.PlcTag | - | - | X |
| _Sensor.PassiveHoming.DigitalInputAddress | Digital input | PublicAPI-object | SW.Tags.PlcTag | - | - | X |
| _Properties.MotionType | Axis type respectively "Technological unit of the position" | 0: Linear  1: Rotary | int | - | X | X |
| _Properties.UseHighResolutionPositionValues<sup>4)</sup> | Use position values with higher resolution | True, False | bool | - | X | X |
| _PositionLimits_HW.MinSwitchAddress | Hardware low limit switch input | PublicAPI-object | SW.Tags.PlcTag | - | X | - |
| _PositionLimits_HW.MaxSwitchAddress | Hardware high limit switch input | PublicAPI-object | SW.Tags.PlcTag | - | X | - |
| _CrossPlcSynchronousOperation.Interface[n]. AddressOut<sup>5)</sup> | Output address for the leading value telegram | PublicAPI-object | SW.Tags.PlcTag | - | X | X |
| _CrossPlcSynchronousOperation. ActivateLocalLeadingValueDelayTimeCalculation<sup>4)</sup> | Allow system calculation | True, False | bool | - | X | X |
| <sup>1)</sup> S7-1500 PLC: n=1; S7-1500T PLC: 1≤n≤4   <sup>2)</sup> possible values are described in the function manual S7-1500 Motion Control on chapter PROFIdrive telegrams   <sup>3)</sup> possible values are described in the function manual S7-1500 Motion Control on chapter units tags (TO)   <sup>4)</sup> ≥V5.0   <sup>5)</sup> V5.0 n=1; ≥V6.0 1≤n≤8 |  |  |  |  |  |  |

#### Leading axis proxy

##### Parameters mapped directly to technology object data block tags

For leading axis proxy technology object, no read-only data block tags are writable in the PublicAPI.

##### Parameters not mapped directly to technology object data block tags

For leading axis proxy technology object, the following additional parameters are available.

| Name in Openness | Name in function view | Possible value | Data type |
| --- | --- | --- | --- |
| _Interface.AddressIn<sup>1)</sup> | Transfer area | PublicAPI-object | SW.Tags.PlcTag |
| <sup>1)</sup> S7-1500T PLC |  |  |  |

#### Measuring input

##### Parameters mapped directly to technology object data block tags

For measuring input technology object, the following read-only data block tags are writable in the PublicAPI.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| Parameter.MeasuringInputType | Measuring input type | 0: Measurement by using time stamp (STANDARD)  1: Measurement by using PROFIdrive telegrams of drive or external encoder (PROFIDRIVE)  2: Measurement by listening to measuring input<sup>1)</sup> | Int |
| 1) ≥V8.0 |  |  |  |

##### Parameters not mapped directly to technology object data block tags

For measuring input technology objects, the following additional parameters are available.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| _AssociatedObject | Associated object | PublicAPI-object | SW.TechnologicalObjects.TechnologicalInstanceDB |
| _ListenToMeasuringInput | Listen to measuring input | Technology objects of type TO_MeasuringInput | SW.TechnologicalObjects.TechnologicalInstanceDB |

#### Output cam and cam track

##### Parameters mapped directly to technology object data block tags

For output cam technology objects the following read-only data block tags are writable in the PublicAPI.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| Interface.LogicOperation | Logical operation of the output cam signal at the output | 0: Logical OR  1: Logical AND | int |

For camtrack technology object, no read-only data block tags are writable in the PublicAPI.

##### Parameters not mapped directly to technology object data block tags

For output cam and cam track technology objects, the following additional parameters are available.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| _AssociatedObject | Associated object | PublicAPI-object | SW.TechnologicalObjects.TechnologicalInstanceDB |

#### Kinematics

##### Parameters mapped directly to technology object data block tags

For kinematics technology object, the following read-only data block tags are writable in the PublicAPI.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| Kinematics.TypeOfKinematics | Kinematics type | See tag Kinematics.TypeOfKinematics<sup>1)</sup> | int |
| MotionQueue.MaxNumberOfCommands | Maximum number of jobs | 1..10 | Int |
| <sup>1)</sup> Possible values are described in the version specific function manual S7-1500T Kinematics functions on chapter "Kinematics tags". |  |  |  |

##### Parameters not mapped directly to technology object data block tags

For kinematics technology object, the following additional parameters are available:

| Name in Openness | Name in function view | Possible value | Data type |
| --- | --- | --- | --- |
| _KinematicsAxis[n]<sup>1)</sup> | Kinematics axis A1 .. A6 | Axis that can be connected to TO_Kinematics objects | SW.TechnologicalObjects.TechnologicalInstanceDB |
| _Units.LengthUnit | Units of measurement &gt; Position | See tag Units.LengthUnit<sup>2)</sup> | uint |
| _Units.LengthVelocityUnit | Units of measurement &gt; Velocity | See tag Units.LengthVelocityUnit<sup>2)</sup> | uint |
| _Units.AngleUnit | Units of measurement &gt; Angle | See tag UnitsAngleUnit<sup>2)</sup> | uint |
| _Units.AngleVelocityUnit | Units of measurement &gt; Angle velocity | See tag Units.AngleVelocityUnit<sup>2)</sup> | uint |
| _Properties.UseHighResolutionPositionValues<sup>1)</sup> | Use position values with higher resolution | True, False | bool |
| _X_Minimum<sup>3)</sup> | x minimum | -1.00E+12 .. +1.00E+12 | double |
| _X_Maximum<sup>3)</sup> | x maximum | -1.00E+12 .. +1.00E+12 | double |
| _Y_Minimum<sup>3)</sup> | y minimum | -1.00E+12 .. +1.00E+12 | double |
| _Y_Maximum<sup>3)</sup> | y maximum | -1.00E+12 .. +1.00E+12 | double |
| _Z_Minimum<sup>3)</sup> | z minimum | -1.00E+12 .. +1.00E+12 | double |
| _Z_Maximum<sup>3)</sup> | z maximum | -1.00E+12 .. +1.00E+12 | double |
| _A3_Maximum<sup>3)</sup> | A3 maximum | -1.00E+12 .. +1.00E+12 | double |
| <sup>1)</sup> &lt;V7.0 n=1≤n≤4; ≥V7.0 1≤n≤6; Kinematics axes A5 and A6 can only be used with "S7-1500T Motion Control KinPlus".   <sup>2)</sup> Possible values are described in the version specific function manual S7-1500T Kinematics functions on chapter "Units tags".   <sup>3)</sup> ≥V5.0 |  |  |  |

#### Interpreter

##### Parameters mapped directly to technology object data block tags

For Interpreter technology object, the following read-only data block tags are writable in the PublicAPI.

| Name in Openness | Name in function view | Possible value | Data type in Openness |
| --- | --- | --- | --- |
| Parameter.MaxNumberOfCommands | Maximum number of jobs | 10..100 | Int |

### Connecting drives

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- An S7-1500 PLC is determined in the project.

  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets).
- A technology object of the type TO_SpeedAxis, TO_PositioningAxis or TO_SynchronousAxis is determined in the project.
- A drive is determined in the project.

#### Application

To connect an axis with a drive, it is necessary to specify several values together in a single call.

**Sensor interface and Telegram 750**

- If the actor interface contains a sensor interface, the sensor interface is connected automatically by using these methods.
- If the actor interface contains torque data, the additional telegramm 750 is connected automatically by using these methods.
- To access the sensor interface you can use SensorInterface[m] with 0≤m≤3.

The public API type AxisEncoderHardwareConnectionInterface provides the following methods which can be used to connect and disconnect the actor or sensor interfaces:

| Method | Description |
| --- | --- |
| void Connect(HW.DeviceItem moduleInOut) | Connects to input and output addresses at the same module.  To connect drives that are configured by using a GSD file use this method. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut) | Connects to input and output addresses at separate modules.  To connect drives that are configured by using a GSD file use this method. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut, ConnectOption connectOption) | Connects to input and output addresses at separate modules, specifying an additional ConnectOption.  To connect drives that are configured by using a GSD file use this method. |
| void Connect(HW.Channel channel) | Connects to a channel  To connect technology modules use this method. |
| void Connect(MC.Drives.Telegram telegram) | Connects to a telegram provided by StartDrive drive object  To connect drives that are configured by Startdrive as of V19 use this method. |
| void Connect(MC.Drives.Telegram telegram, ConnectOption connectOption) | Connects to a telegram provided by StartDrive drive object, specifying an additional ConnectOption.  To connect drives that are configured by Startdrive as of V19 use this method. |
| void Connect(int addressIn, int addressOut, ConnectOption connectOption) | Connects specifying bit addresses directly  You can use this method in any cases.  If the drive is configured with Startdrive &lt; V19, you must use this method.  Read the Byte address of the telegram from the hardware configuration and use the corresponding Bit address.  Bit address = Byte address * 8 |
| void Connect(string pathToDBMember) | Connects to a data block tag  To connect an axis to a drive via data block use this method. The data block for the connection must exist. |
| void Connect(SW.Tags.PlcTag outputTag) | Connects to a PLC tag  To connect a drive with analog setpoint interface to tags use this method. You can connect tags for "analog output", "enable output", and "ready input". |
| void Disconnect() | Disconnects an existing connection |

**ET200SP PTO 2**

If you connect an ET200SP PTO 2 module to a drive by specifying bit addresses directly, you must use the following offsets:

| Channel | Telegram | Bit offset to InputAddress | Bit offset to OutputAddress |
| --- | --- | --- | --- |
| 0 | 1 | 0 | 0 |
| 81 | 32 | 32 |  |
| 1 | 1 | 128 | 64 |
| 81 | 160 | 96 |  |

**Attribute**

To determine how the technology object is connected you can use the following read-only attributes. The respective connection values are set only if the connection of the specific kind exists.

| Attribute | Data type | Description |
| --- | --- | --- |
| IsConnected | bool | TRUE: Interface is connected  FALSE: Interface is not connected |
| InputOutputModule | HW.DeviceItem | Connected module that contains input and output addresses |
| InputModule | HW.DeviceItem | Connected module that contains input addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| OutputModule | HW.DeviceItem | Connected module that contains output addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| InputAddress | int | Logical input address of connected object, for example 256. |
| OutputAddress | int | Logical output address of connected object, for example 256. |
| ConnectOption | ConnectOption | Value of the ConnectOption that has been set when the connection was made:  - Default   Only modules that are recognized as valid connection partners can be selected. - AllowAllModules   This option corresponds to selecting "Show all modules" in the user interface. |
| Channel | HW.Channel | Connected channel |
| Telegram | MC.Drives.Telegram | Connected telegram of drive object |
| PathToDBMember | string | Connected technology object data block tag |
| OutputTag | SW.Tags.PlcTag | Connected PLC tag (analog connection) |
| SensorIndexInActorTelegram | int | Connected sensor interface in actor telegram  The attribute is only relevant for sensor interfaces.   0: Encoder is not connected  1: Encoder is connected to first sensor interface in telegram  2: Encoder is connected to second sensor interface in telegram  For the actor interface the value is always 0. |

#### Program code to connect a mixed module with input and output addresses at the same module

Modify the following program code to connect a servo drive object from GSDML drive with input and output addresses at the same module:

public void Connect_ModuleInOut()

{

   var deviceItem = GsdmlDevice.DeviceItems.First(x =&gt; x.Name == "SIEMENS telegram 105, PZD-10/10");

   var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");

   syncAxis

    .GetService&lt;AxisHardwareConnectionProvider&gt;()

    .ActorInterface

    .Connect(deviceItem);

}

#### Program code to connect input and output addresses at separate modules

Modify the following program code to connect a servo drive object from GSDML drives with input and output addresses at different modules:

//"Input module", "Output module" and "syncAxis" must be replaced with the names in your project.

public void Connect_ModuleIn_ModuleOut()

{

    var deviceItemOut = Plc.DeviceItems.First(di =&gt; di.Name == "Input module").DeviceItems[0];

    var deviceItemIn = Plc.DeviceItems.First(di =&gt; di.Name == "Output module").DeviceItems[0];

    var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");

    syncAxis

    .GetService&lt;AxisHardwareConnectionProvider&gt;()

    .ActorInterface

    .Connect(deviceItemIn, deviceItemOut, ConnectOption.AllowAllModules);

}

If TIA Portal does not detect the module as a standard telegram, the connectOption AllowAllModules must be used.

#### Program code to connect technology modules

Modify the following program code to connect a technology module:

public void Connect_Channel()

{

   var tmTimer = Plc.DeviceItems.First(di =&gt; di.Name== "TM Timer DIDQ 16x24V_1").DeviceItems[0];

   var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");

    syncAxis.GetService&lt;OutputCamMeasuringInputContainer&gt;()

    .OutputCams.Find("OutputCam_1")

    .GetService&lt;OutputCamHardwareConnectionProvider&gt;()

    .Connect(tmTimer.Channels[0]);

}

#### Program code to connect drives configured via Startdrive as of V19

Startdrive as of V19 must be installed.

Modify the following program code to connect a servo drive object from Startdrive by telegram:

public void Connect_To_Startdrive(PlcSoftware plcsoftware)

{

var mainTelegram = StartdriveDevice.DeviceItems.First(di =&gt; di.PositionNumber == 0)  
 .GetService&lt;DriveObjectContainer&gt;().DriveObjects[0].Telegrams.Find(TelegramType.MainTelegram);

var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");  
 syncAxis.GetService&lt;AxisHardwareConnectionProvider&gt;().ActorInterface.Connect(mainTelegram);

}

#### Program code to connect drives configured via Startdrive &lt; V19

Startdrive must be installed.

Modify the following program code to connect a servo drive object from StartDrive:

public void Connect_To_Startdrive()

{

  var mainTelegram = StartdriveDevice.DeviceItems.First(di =&gt; di.PositionNumber == 0)

.GetService&lt;DriveObjectContainer&gt;().DriveObjects[0].Telegrams.Find(TelegramType.MainTelegram);

  var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");

  var inputAddress = mainTelegram.Addresses.First(x =&gt; x.IoType == AddressIoType.Input).StartAddress;

  var outputAddress = mainTelegram.Addresses.First(x =&gt; x.IoType == AddressIoType.Output).StartAddress;

  syncAxis

   .GetService&lt;AxisHardwareConnectionProvider&gt;()

   .ActorInterface

//Byte adresses must be multiplied by 8 to get Bit addresses

   .Connect(inputAddress * 8, outputAddress * 8, ConnectOption.Default);

}

#### Program Code to connect data block tags

In this example the sensor of an external encoder is connected to the data block named "InstDBTel83". InstDBTel83 contains one member "Telegram" of typ "PD_Tel83":

Modify the following program code to connect to a data block tag.

public void Connect_PathToDBMember()

{

   var extEnc = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("ExternalEncoder_1");

   extEnc

    GetService&lt;EncoderHardwareConnectionProvider&gt;()

    .SensorInterface

    .Connect("InstDBTel83.Telegram.Sensor_1");

}

### Connecting telegram 750

#### Requirement

- The Openness application is connected to the TIA Portal.   
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- An S7-1500 PLC is determined in the project.
- A technology object of the type TO_SpeedAxis, TO_PositioningAxis or TO_SynchronousAxis V4.0 is determined in the project.
- A drive that supports telegram 750 is determined in the project.

#### Application

If telegram 750 was added after connecting the drive and the axis, it is necessary to connect telegram 750 separately. EnableTorqueData is set to TRUE automatically. The public API type TorqueHardwareConnectionInterface provides the following methods which can be used to connect and disconnect telegram 750:

| Method | Description |
| --- | --- |
| void Connect(HW.DeviceItem moduleInOut) | Connects to input and output addresses at the same module.  To connect telegram 750 for drives that are configured by using a GSD file use this method. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut) | Connects to input and output addresses at separate modules. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut, ConnectOption connectOption) | Connects to input and output addresses at separate modules, specifying an additional ConnectOption. |
| void Connect(int addressIn, int addressOut, ConnectOption connectOption) | Connects specifying bit addresses directly.  You can use this method in any cases.  If the drive is configured with StartDrive, you must use this method.  Read the Byte address of the telegram from the hardware configuration and use the corresponding Bit address.  Bit address = Byte address * 8 |
| void Connect(string pathToDBMember) | Connects to a data block tag.  To connect telegram 750 via data block use this method.   The data block for the connection must exist. |
| void Disconnect() | Disconnects an existing connection. |

The TorqueHardwareConnectionInterface can be retrieved via the property TorqueInterface at the type AxisHardwareConnectionProvider. If the connection to telegram 750 is not supported, the property value is “null”.

If the drive is connected by data block tags, you cannot connect telegram 750 by module. You can use the following read-only attributes to determine how the technology object is connected. The respective connection values are set only if the connection of the specific kind exists:

| Attribute | Data type | Description |
| --- | --- | --- |
| IsConnected | bool | TRUE: Interface is connected  FALSE: Interface is not connected |
| InputOutputModule | HW.DeviceItem | Connected module that contains input and output addresses |
| InputModule | HW.DeviceItem | Connected module that contains input addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| OutputModule | HW.DeviceItem | Connected module that contains output addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| InputAddress | int | Logical input address of connected object, for example 256 |
| OutputAddress | int | Logical output address of connected object, for example 256 |
| ConnectOption | ConnectOption | Value of the ConnectOption that has been set when the connection was made:  - Default Only modules that are recognized as valid connection partners can be selected. - AllowAllModules This option corresponds to selecting "Show all modules" in the user interface. |
| PathToDBMember | string | Connected technology object data block tag |

#### Program Code: Connect telegramm 750

Modify the following program code to connect a mixed module that contains input and output addresses:

//An instance of technology object and device item is already available in the program before

private static void ConnectTorqueInterface(TechnologicalInstanceDB technologyObject, DeviceItem devItem)

{

    //Retrieve service AxisHardwareConnectionProvider

    AxisHardwareConnectionProvider connectionProvider =

    technologyObject.GetService&lt;AxisHardwareConnectionProvider&gt;();

    //Connect TorqueInterface with DeviceItem

    connectionProvider.TorqueInterface.Connect(devItem);

}

### Connecting encoders

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- An S7-1500 PLC is determined in the project.
- A technology object of the type TO_ExternalEncoder is determined in the project.
- An object is determined in the project that provides PROFIdrive telegram 81 or 83.

#### Application

To connect an external encoder technology object with the encoder hardware, it is necessary to specify several values together in a single call. The public API type AxisEncoderHardwareConnectionInterface provides the following methods which can be used to connect and disconnect the sensor interface:

| Method | Description |
| --- | --- |
| void Connect(HW.DeviceItem moduleInOut) | Connects to input and output addresses at the same module.  To connect encoders that are configured by using a GSD file use this method. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut) | Connects to input and output addresses at separate modules.  To connect encoders that are configured by using a GSD file use this method. |
| void Connect(HW.DeviceItem moduleIn, HW.DeviceItem moduleOut, ConnectOption connectOption) | Connects to input and output addresses at separate modules, specifying an additional ConnectOption  To connect encoders that are configured by using a GSD file use this method. |
| void Connect(HW.Channel channel) | Connects to a channel.  To connect technology modules use this method. |
| void Connect(int addressIn, int addressOut, ConnectOption connectOption) | Connects specifying bit addresses directly.  You can use this method in any cases.  If the encoder is configured with StartDrive, you must use this method.  Read the Byte address of the telegram from the hardware configuration and use the corresponding Bit address.  Bit address = Byte address * 8 |
| void Connect(string pathToDBMember) | Connects to a data block tag.  To connect an external encoder via data block use this method. The data block for the connection must exist. |
| void Connect(SW.Tags.PlcTag outputTag) | Not relevant for connecting encoders |
| void Disconnect() | Disconnects an existing connection. |

You can use the following read-only attributes to determine how the technology object is connected. The respective connection values are set only if the connection of the specific kind exists.

| Attribute | Data type | Description |
| --- | --- | --- |
| IsConnected | bool | TRUE: Interface is connected  FALSE: Interface is not connected |
| InputOutputModule | HW.DeviceItem | Connected module that contains input and output addresses |
| InputModule | HW.DeviceItem | Connected module that contains input addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| OutputModule | HW.DeviceItem | Connected module that contains output addresses  The value is also set in case of an existing connection to a module containing input and output addresses. |
| InputAddress | int | Logical input address of connected object, for example 256. |
| OutputAddress | int | Logical output address of connected object, for example 256. |
| ConnectOption | ConnectOption | Value of the ConnectOption that has been set when the connection was made:  - Default   Only modules that are recognized as valid connection partners can be selected. - AllowAllModules   This option corresponds to selecting "Show all modules" in the user interface. |
| Channel | HW.Channel | Connected channel |
| PathToDBMember | string | Connected data block tag |
| OutputTag | SW.Tags.PlcTag | Not relevant for connecting encoders |
| SensorIndexInActorTelegram | int | Connected sensor telegram  The attribute is only relevant for sensor interfaces.   0: Encoder is not connected  1: Encoder is connected to first sensor interface in telegram  2: Encoder is connected to second sensor interface in telegram  For the actor interface the value is always 0. |

#### Program code: Connect an encoder

Modify the following program code to connect an external encoder technology object:

//An instance of technology object and device item is already available in the program before

private static void UseServiceEncoderHardwareConnectionProvider(TechnologicalInstanceDB technologyObject, DeviceItem devItem)

{

    //Retrieve service EncoderHardwareConnectionProvider

    EncoderHardwareConnectionProvider connectionProvider =

    technologyObject.GetService&lt;EncoderHardwareConnectionProvider&gt;();

    //Connect SensorInterface with DeviceItem

    connectionProvider.SensorInterface.Connect(devItem);

    //Check ConnectionState of SensorInterface

    bool sensorInterfaceConnectionState = connectionProvider.SensorInterface.IsConnected;

}

### Connecting output cams and cam tracks to hardware

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500 PLC is determined in the project.
- A technology object of the type TO_OutputCam or TO_CamTrack is determined in the project.
- A digital output module is determined in the project, for example TM Timer DIDQ.

#### Application

To connect an output cam or cam track technology object with a digital output, it is necessary to specify several values together in a single call. The public API type OutputCamHardwareConnectionProvider provides the following methods which can be used to connect and disconnect the actor or sensor interfaces:

| Method | Description |
| --- | --- |
| void Connect(HW.Channel channel) | Connects to a channel |
| void Connect(SW.Tags.PlcTag outputTag) | Connects to a PLC tag |
| void Connect(int address) | Connects specifying bit addresses directly |
| void Disconnect() | Disconnects an existing connection |

You can use the following read-only attributes to determine how the technology object is connected:

| Attribute | Data type | Description |
| --- | --- | --- |
| IsConnected | bool | TRUE: Technology object is connected  FALSE: Technology object is not connected |
| Channel | HW.Channel | Connected channel |
| OutputTag | SW.Tags.PlcTag | Connected PLC tag |
| OutputAddress | int | Logical output address of connected object, for example 256. |

#### Program code: Connect output cam or cam track technology object

Modify the following program code to connect an output cam or cam track technology object:

//An instance of technology object and channel item is already available in the program before

private static void UseServiceOutputCamHardwareConnectionProvider(TechnologicalInstanceDB technologyObject, Channel channel)

{

    //Retrieve service OutputCamHardwareConnectionProvider

    OutputCamHardwareConnectionProvider connectionProvider =

    technologyObject.GetService&lt;OutputCamHardwareConnectionProvider&gt;();

    //Connect technology object with Channel

    connectionProvider.Connect(channel);

    //Check ConnectionState of technology object

    bool connectionState = connectionProvider.IsConnected;

}

#### Program Code to connect PLC tags

Modify the following program code to connect an output cam to a PLC tag. The PLC tag points to the output address:

public void Connect_PlcTag(PlcSoftware plcSoftware)

{

   var outputCamTag = plcSoftware.TagTableGroup.TagTables.Find("My Tag Table").Tags.Find("OutputCamTag");

   var syncAxis = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects.Find("SynchronousAxis_1");

   syncAxis.GetService&lt;OutputCamMeasuringInputContainer&gt;()

    .OutputCams.Find("OutputCam_1")

    .GetService&lt;OutputCamHardwareConnectionProvider&gt;()

    .Connect(outputCamTag);

}

### Connecting measuring inputs to hardware

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500 PLC is determined in the project.
- A technology object of the type TO_MeasuringInput is determined in the project.
- A digital input module is determined at drive or in the project, for example TM Timer DIDQ.

#### Application

To connect a measuring input technology object with a digital input, it is necessary to specify several values together in a single call. The public API type MeasuringInputHardwareConnectionProvider provides the following methods which can be used to connect and disconnect the actor or sensor interface:

| Method | Description |
| --- | --- |
| void Connect(HW.Channel channel) | Connects to a channel |
| void Connect(HW.DeviceItem moduleIn, int channelIndex) | Connects to a module, specifying an additional channel index |
| void Connect(int address) | Connects specifying bit addresses directly  - For TM Channels, the bit address can be calculated via the formula bit_address = module_start_address * 8 + channel_index - For telegram 39x, the associated formula is  bit_address = module_start_address * 8 + 24 + number_of_measuringinput_in_telegram |
| void Disconnect() | Disconnects an existing connection |

You can use the following read-only attributes to determine how the technology object is connected:

| Attribute | Data type | Description |
| --- | --- | --- |
| IsConnected | bool | TRUE: Technology object is connected  FALSE: Technology object is not connected |
| InputModule | HW.DeviceItem | Connected module that contains input addresses |
| ChannelIndex | int | Index of connected channel with respect to InputModule |
| Channel | HW.Channel | Connected channel |
| InputAddress | int | Logical input address of connected object, for example 256. |

#### Program code: Connect a measuring input technology object

Modify the following program code to connect a measuring input technology object:

//An instance of technology object and channel item is already available in the program before

private static void UseServiceMeasuringInputHardwareConnectionProvider(TechnologicalInstanceDB technologyObject, Channel channel)

{

    //Retrieve service MeasuringInputHardwareConnectionProvider

    MeasuringInputHardwareConnectionProvider connectionProvider =

    technologyObject.GetService&lt;MeasuringInputHardwareConnectionProvider&gt;();

    //Connect technology object with Channel

    connectionProvider.Connect(channel);

    //Check ConnectionState of technology object

    bool connectionState = connectionProvider.IsConnected;

}

### Connecting synchronous axis with leading values

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500 PLC is determined in the project.
- A technology object of the type TO_PositioningAxis, TO_SynchronousAxis, TO_ExternalEncoder or TO_LeadingAxisProxy as leading axis is determined in the project.
- A technology object of the type TO_SynchronousAxis as following axis is determined in the project.

#### Application

To connect a synchronous axis technology object with leading values, it is necessary to specify several values together in a single call. The public API type SynchronousAxisMasterValues provides the following methods which can be used to connect and disconnect leading values. Leading values can be connected as setpoint coupling (S7-1500 PLC, S7-1500T PLC) or actual value coupling (S7-1500T PLC). All methods and attributes are relevant for both types of coupling.

| Method | Description |
| --- | --- |
| int IndexOf (TechnologicalInstanceDB element) | Returns the corresponding index of a leading value |
| bool Contains (TechnologicalInstanceDB element) | TRUE: The container contains the leading value   FALSE: The container does not contain the leading value |
| IEnumerator GetEnumerator &lt;TechnologicalInstanceDB&gt;() | Used to support each iteration |
| void Add (TechnologicalInstanceDB element) | Connects following axis to leading value |
| bool Remove (TechnologicalInstanceDB element) | Disconnects following axis from leading value  TRUE: Disconnection was succesfully  FALSE: Disconnection was not succesfully |

You can use the following read-only attributes:

| Attribute | Data type | Description |
| --- | --- | --- |
| Count | int | Count of leading values |
| IsReadonly | bool | TRUE: The container is read-only  FALSE: The container is not read-only |
| Parent | IEngineeringObject | Returns the parent of the container.  In this case parent means the service SynchronousAxisMasterValues. |
| this [ id ] { get; } | TechnologicalInstanceDB | Index-based access to leading values |

You can use the following attributes to connect a synchronous axis with a leading​ value:

| Attribute | Data type | Description |
| --- | --- | --- |
| SetPointCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute gets container of connected leading axis with setpoint coupling. |
| ActualValueCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute gets container of connected leading axis with actual value coupling. |
| DelayedCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute contains all master values that are coupled via delayed values. |

#### Program code: Connect a synchronous axis with a leading​ value

Modify the following program code to connect a synchronous axis with a leading​ value:

//An instance of leading axis and following axis is already available in the program before

private static void UseServiceSynchronousAxisMasterValues(TechnologicalInstanceDB masterTechnologyObject, TechnologicalInstanceDB synchronousTechnologyObject)

{

    //Retrieve service SynchronousAxisMasterValues

    SynchronousAxisMasterValues masterValues =

    synchronousTechnologyObject.GetService&lt;SynchronousAxisMasterValues&gt;();

    //Connect following axis and leading axis with setpoint coupling

    masterValues.SetPointCoupling.Add(masterTechnologyObject);

    //Get container of connected leading axis with setpoint coupling

    TechnologicalInstanceDBAssociation setPointMasterValues =

    masterValues.SetPointCoupling;

    //Remove connected leading axis with setpoint coupling

    masterValues.SetPointCoupling.Remove(masterTechnologyObject);

    //Connect following axis and leading axis with actual value coupling

    masterValues.ActualValueCoupling.Add(masterTechnologyObject);

    //Get container of connected leading axis with actual value coupling

    TechnologicalInstanceDBAssociation actualValueMasterValues =

    masterValues.ActualValueCoupling;

    //Remove connected leading axis with actual value coupling

    masterValues.ActualValueCoupling.Remove(masterTechnologyObject);

}

### Connecting conveyor tracking of kinematics with leading values

#### Requirement

- The Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500T PLC is determined in the project.

  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets).
- A technology object of the type TO_PositioningAxis, TO_SynchronousAxis or TO_ExternalEncoder as leading axis is determined in the project.
- A technology object of the type TO_Kinematics as following axis is determined in the project.

#### Application

To configure leading values for conveyor tracking, use the service SW.TechnologicalObjects.Motion.ConveyorTrackingLeadingValues for TO Kinematics ≥ V5.0.

| Method | Description |
| --- | --- |
| int IndexOf (TechnologicalInstanceDB element) | Returns the corresponding index of a leading value |
| bool Contains (TechnologicalInstanceDB element) | TRUE: The container contains the leading value   FALSE: The container does not contain the leading value |
| IEnumerator GetEnumerator &lt;TechnologicalInstanceDB&gt;() | Used to support each iteration |
| void Add (TechnologicalInstanceDB element) | Connects following axis to leading value |
| bool Remove (TechnologicalInstanceDB element) | Disconnects following axis from leading value  TRUE: Disconnection was succesfully  FALSE: Disconnection was not succesfully |

You can use the following read-only attributes:

| Attribute | Data type | Description |
| --- | --- | --- |
| Count | int | Count of leading values |
| IsReadonly | bool | TRUE: The container is read-only  FALSE: The container is not read-only |
| Parent | IEngineeringObject | Returns the parent of the container.  In this case parent means the service SynchronousAxisMasterValues. |
| this [ id ] { get; } | TechnologicalInstanceDB | Index-based access to leading values |

You can use the following attributes to connect a kinematics axis with a leading​ value:

| Attribute | Data type | Description |
| --- | --- | --- |
| SetPointCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute gets container of connected leading axis with setpoint coupling. |
| ActualValueCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute gets container of connected leading axis with actual value coupling. |
| DelayedCoupling | SW.TechnologicalObjects.TechnologicalInstanceDBAssociation | The attribute contains all master values that are coupled via delayed values. |

#### Connect conveyor tracking axis of a kinematics with a leading value

An example of the interconnection is included in the topic [Connecting synchronous axis with leading values](#connecting-synchronous-axis-with-leading-values).

### Exporting and importing technology object cam (S7-1500T)

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- An S7-1500 PLC is determined in the project.

  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets)
- The technology object exists.

#### Application

To export or import the data of a technology object cam of typ TO_Cam or TO_Cam_10k you have to specify the format and which separator should be used. The public API type CamDataSupport provides the following methods which can be used to export the data of technology object cam. For more information on export format of cam, Refer function manual Using S7-1500/S7-1500T Synchronous Operations Functions on chapter Importing / exporting cam.

| Method | Description |
| --- | --- |
| void SaveCamDataBinary(System.IO.FileInfo destinationFile) | Saves the cam data in binary format in the destination file. |
| void SaveCamDataPointList(System.IO.FileInfo destinationFile, CamDataFormatSeparator separator, int samplePoints) | Saves the cam data in format “PointList” in the destination file. |
| void SaveCamData(System.IO.FileInfo destinationFile, CamDataFormat format, CamDataFormatSeparator separator) | Saves the cam data in the destination file. You can specify data format as “MCD”, “SCOUT” or “Pointlist” and separator as “tab” or “comma”.  If you choose “PointList” 360 interpolation points will be exported. |
| void LoadCamData(System.IO.FileInfo sourceFile, CamDataFormatSeparator separator) | Loads the cam data in the format “MCD”, “SCOUT” or “Pointlist” to the project. |
| void LoadCamDataBinary(System.IO.FileInfo sourceFile) | Loads the cam data from a binary file to the project. |

You can use the following attributes:

| Attribute | Data type | Description |
| --- | --- | --- |
| separator | CamDataFormatSeparator | Allowed values  - tab - comma |
| samplePoints | int | Number of interpolation points that should be exported. |
| format | CamDataFormat | Allowed values  - MCD - SCOUT - Pointlist |
| destinationFile | System.IO.FileInfo | Name of target file. Must not be null. Access rights and enough space on storage medium must be given. An existing file will be overwritten. |
| sourceFile | System.IO.FileInfo | Name of source file. Must not be null. Access rights must be given. Content must be in specified format. |

#### Program code: Save cam data

Modify the following program code to save cam data:

//An instance of technology object is already available in the program before

private static void ExportCamData(TechnologicalInstanceDB technologyObject, System.IO.FileInfo destinationFile)

{

    //Retrieve service CamDataSupport

    CamDataSupport camData = technologyObject.GetService&lt;CamDataSupport&gt;();

    //Save cam data in MCD format, using the separator Tab

    camData.SaveCamData(destinationFile, CamDataFormat.MCD, CamDataFormatSeparator.Tab);

}

#### Program code: Load cam data

Modify the following program code to load cam data:

//An instance of technology object is already available in the program before

private static void ImportCamData(TechnologicalInstanceDB technologyObject, System.IO.FileInfo sourceFile)

{

    //Retrieve service CamDataSupport

    CamDataSupport camData = technologyObject.GetService&lt;CamDataSupport&gt;();

    //Load cam data from source file, using the separator Tab

    camData.LoadCamData(sourceFile, CamDataFormatSeparator.Tab);

}

### Load and save the source code of an interpreter program (S71500T)

#### Requirement

- The Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- A S7-1500T PLC is determined in the project.

  See [Querying PLC and HMI targets](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#querying-plc-and-hmi-targets).
- A technology object of the type TO_InterpeterProgram is determined in the project.

#### **Application**

The public API type InterpreterProgramSupport provides the following methods which can be used to load the MCL program from a text file into a TO_InterpreterProgram technology object or save it in a text file.

The MCL program is provided by a path to the source file.

| Method | Description |
| --- | --- |
| void SaveSource(System.IO.FileInfo fileInfo) | Saves the MCL program from the TO_InterpreterProgram technology object to the specified txt-file. |
| void LoadSource(System.IO.FileInfo fileInfo) | Loads the specified txt-file with the MCL program into the TO_InterpreterProgram technology object. |

#### Program code to save an MCL program

Modify the following program code to connect a technology module:

//An instance of technology object is already available in the program before

private static void ExportIprProgramSourceCode(TechnologicalInstanceDB technologyObject, System.IO.FileInfo destinationFile)

{

//Retrieve service InterpreterProgramSupport

InterpreterProgramSupport iprProgramSourceCode = technologyObject.GetService&lt;InterpreterProgramSupport&gt;();

//Save source code in the destination file

iprProgramSourceCode.SaveSource(destinationFile);

}

#### Program code to load an MCL program

Modify the following program code to connect a technology module:

//An instance of technology object is already available in the program before

private static void ImportIprProgramSourceCode(TechnologicalInstanceDB technologyObject, System.IO.FileInfo sourceFile)

{

//Retrieve service InterpreterProgramSupport

InterpreterProgramSupport iprProgramSourceCode = technologyObject.GetService&lt;InterpreterProgramSupport&gt;();

//Load source code from source file

iprProgramSourceCode.LoadSource(sourceFile);

}

## PID control

This section contains information on the following topics:

- [Parameters for PID_Compact, PID_3Step, PID_Temp, CONT_C, CONT_S, TCONT_CP and TCONT_S](#parameters-for-pid_compact-pid_3step-pid_temp-cont_c-cont_s-tcont_cp-and-tcont_s)

### Parameters for PID_Compact, PID_3Step, PID_Temp, CONT_C, CONT_S, TCONT_CP and TCONT_S

You can find a list of all available variables in SIMATIC S7-1200/S7-1500 PID control function manual on the [internet](https://support.industry.siemens.com/cs/ww/en/view/108210036).

> **Note**
>
> In TIA Portal in the Parameter view of the technology object configuration you can find the column "Name in Openness".

## Counting

This section contains information on the following topics:

- [Parameters for High_Speed_Counter and SSI_Absolute_Encoder](#parameters-for-high_speed_counter-and-ssi_absolute_encoder)

### Parameters for High_Speed_Counter and SSI_Absolute_Encoder

You can find a list of all available parameters in the product information “Parameters of technology objects in TIA Portal Openness“ on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109744932).

For each parameter the following properties are provided:

- Name in configuration (TIA Portal)
- Name in Openness
- Data type in Openness
- Default access
- Range of values

#### Additional information

You can find additional information in SIMATIC S7-1500, ET 200MP, ET 200SP Counting, measurement and position input function manual on the [internet](http://support.automation.siemens.com/WW/view/en/59709820).

## Easy Motion Control

This section contains information on the following topics:

- [Parameters for AXIS_REF](#parameters-for-axis_ref)

### Parameters for AXIS_REF

You can find a list of all available parameters in the product information “Parameters of technology objects in TIA Portal Openness“ on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109744932).

For each parameter the following properties are provided:

- Name in configuration (TIA Portal)
- Name in Openness
- Data type in Openness
- Default access
- Range of values

> **Note**
>
> In TIA Portal in the Parameter view of the technology object configuration you can find the column "Name in Openness".

#### Additional information

You can find additional information for Easy Motion Control in the Information system of STEP 7 (TIA Portal).
