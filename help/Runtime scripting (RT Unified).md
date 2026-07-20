---
title: "Runtime scripting (RT Unified)"
package: ScriptingWCCUenUS
topics: 54
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Runtime scripting (RT Unified)

This section contains information on the following topics:

- [Introduction to runtime scripting (RT Unified)](#introduction-to-runtime-scripting-rt-unified)
- [Basics (RT Unified)](#basics-rt-unified)
- [Lowest device version of a script module type (RT Unified)](#lowest-device-version-of-a-script-module-type-rt-unified)
- [Notes on creating scripts (RT Unified)](#notes-on-creating-scripts-rt-unified)
- ["Scripts" editor (RT Unified)](#scripts-editor-rt-unified)
- [Examples (RT Unified)](#examples-rt-unified)
- [Troubleshooting (RT Unified)](#troubleshooting-rt-unified)
- [Debugging scripts (RT Unified)](#debugging-scripts-rt-unified)
- [Debugging scripts with Visual Studio Code (RT Unified)](#debugging-scripts-with-visual-studio-code-rt-unified)

## Introduction to runtime scripting (RT Unified)

### Area of application

You use Runtime Scripting in WinCC for the following tasks in runtime:

- Dynamization of properties
- Triggering functions for an event

Runtime Scripting uses JavaScript as the programming language. Runtime Scripting is supported at the following objects:

- Screen
- Screen object
- Task

### Global modules for frequently required functions

Global modules contain scripts which are available in the entire project. Global modules are therefore suitable for configuring frequently required functions.

### Using scripts for dynamization

The properties of screens and screen items can be dynamized via local scripts. In addition, a screen or screen item has its own script area to create a "Global definition".

The "Global definition" is used to define modules, local tags and functions and to import other modules with "Import".

![Using scripts for dynamization](images/104105801739_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Global definition for screen or screen item |
| ② | Local scripts per property |

### Input support

The "Scripts" editor assists you in entering code through:

- Syntax highlighting
- Snippets
- System functions
- Referencing HMI objects
- Tooltips
- Autocomplete
- Error marking and correction
- Find and replace

---

**See also**

[Global modules (RT Unified)](#global-modules-rt-unified)
  
[Local scripts (RT Unified)](#local-scripts-rt-unified)
  
[Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
  
[Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)
  
[Input support (RT Unified)](#input-support-rt-unified)

## Basics (RT Unified)

### Scripting environment

WinCC provides you with a modern scripting environment that you can use to automate a variety of system components, such as the graphical runtime system.

In the process, the scripting environment forms individual elements of the system components, such as the screens of the graphical runtime system, through an object model. You use this object model in your scripts to solve a variety of tasks or to control processes.

The script environment in WinCC offers:

- Efficiency and current technologies  
  The scripting environment supports Unicode and uses JavaScript (JS) as the scripting language. The scripting environment is object-oriented and offers numerous asynchronous operations for high-performance and secure script execution.
- Support of mass data  
  The script environment is optimized for the processing of mass data, for example the writing of 1000 tags in one pass. Special script objects are available to this purpose that record numerous HMI objects of the same type. These script objects execute operations on all the HMI objects simultaneously instead of processing each HMI object individually.

### JavaScript

The script environment supports JavaScript according to the ECMAScript Language Specification. Google V8 is used as the script engine.

To find out which version of Node.js you are using, follow these steps:

1. Opens the file explorer.
2. Switch to "C:\Program Files\Siemens\Automation\WinCCUnified\WebRH\bin"

   The path may differ depending on the installation settings.
3. Open the shortcut menu of the file: "node.exe".
4. You can find the version used under "Details > Product version".

An overview of the functions that can be used in the individual versions of Node.js can be found under: <https://node.green/>.

### Scripts in WinCC

As a rule the script environment executes all the scripts on the server side (NodeJS). Referenced external resources such as files used in the script therefore have to be available in the server environment.

### Restrictions

The use of JavaScript is restricted when used with WinCC.

Functions that access external resources are not available:

- Access to the file system via the Node.js module "fs".

  Use WinCC Unified functions instead, for example `HMIRuntime.FileSystem.WriteFile()`, `HMIRuntime.FileSystem.ReadFile()`
- Connection to other web servers and access to content on the Internet, e.g. via `XMLHttpRequest` or `fetch()`.
- Import of other Node.js modules, e.g. via "import ... from ...".

  This applies to both Node.js modules provided by third-party vendors and Node.js modules provided with the current Node.js version.

  Only global modules of the runtime in TIA Portal can be imported.

To access other web servers and to import other Node.js modules, follow these steps:

- Create your own application.

  - On the Panel: Edge app
  - on the PC: any app, JavaScript is recommended.
- Run the application independently of WinCC Unified.
- Results of the application are passed to the runtime via OpenPipe and corresponding HTML tags.

## Lowest device version of a script module type (RT Unified)

### Introduction

### Available functions depending on the device version

## Notes on creating scripts (RT Unified)

This section contains information on the following topics:

- [General information (RT Unified)](#general-information-rt-unified)
- [Data types (RT Unified)](#data-types-rt-unified)
- [Object instances (RT Unified)](#object-instances-rt-unified)
- [Enumerations (RT Unified)](#enumerations-rt-unified)
- [Asynchronous operations (RT Unified)](#asynchronous-operations-rt-unified)
- [Support for errors (RT Unified)](#support-for-errors-rt-unified)
- [Global modules (RT Unified)](#global-modules-rt-unified)
- [Local scripts (RT Unified)](#local-scripts-rt-unified)

### General information (RT Unified)

#### Tips and tricks in SiePortal

Get to know the options for creating scripts (JavaScript) in SIMATIC WinCC Unified and how you can quickly and easily create scripts with snippets. Tips and tricks on using objects via JavaScript are available for selected objects.

Tips and tricks in SiePortal: [Tips and tricks for scripting (JavaScript)](https://support.industry.siemens.com/cs/ww/en/view/109758536)

#### Global search in scripts

Find and replace functions are available in a script.

1. To find strings that appear in a script or in the global definition range, use the global search in the project.
2. To open the "Find and replace" function, use menu "Edit > Search in project".

   - or -

   Press <Ctrl> + <F>.

   ![Global search in scripts](images/160682782731_DV_resource.Stream@PNG-en-US.png)

The search is run on the script opened in the script editor.

The Find and replace function is also available if you open a script module type from a library for editing.

#### Floating-point numbers in JavaScript

JavaScript supports floating-point numbers with a mantissa of up to 54 bits. In scripting and Web client, values with a mantissa greater than 54 bits are therefore rounded.

This includes:

- Tag values
- Constants in the properties of screen objects

> **Note**
>
> Values with a mantissa up to 64-bit are correctly displayed by IO fields.

#### Triggering scripts

To improve performance, trigger the execution of scripts with tags. Avoid cyclic triggers.

#### Scripts with trigger tags

A script triggered by a tag is not allowed to write to this tag.

#### Using scripts during short cycle times

Calls of scripts with a short cycle time can lead to overloads.

#### Memory allocation by scripts

Memory usage by scripts is not limited in runtime. Pay particular attention to the size of the allocated memory when creating tags dynamically.

#### Application of graphic objects in runtime

Only those graphic objects which are referenced at least once, for example as an object reference in a script, are loaded in runtime. The assignment of a graphic to a tag and the referencing of the tag does not function.

**Example of correct referencing of a graphic object in a script:**

`Screen.Items("Graphic view_1").Graphic = HMIRuntime.Resources.Graphics("GraphicCollection.Up_Arrow").Name;`

**Examples of incorrect referencing of a graphic object in a script:**

`let name = "GraphicCollection.Up_Arrow";`
  
`Screen.Items("Graphic view_1").Graphic = HMIRuntime.Resources.Graphics(name).Name;`

or

`let name = "Up_Arrow";`
  
`Screen.Items("Graphic view_1").Graphic = HMIRuntime.Resources.Graphics("GraphicCollection."+ name ).Name;`

### Data types (RT Unified)

#### Data types in the object model

Unlike the basic JavaScript data types String, Number and Boolean, the data types in the WinCC object model are more typified.

The following table lists the utilized data types of the object model:

| Data type | Description |
| --- | --- |
| Bool | Logical values (True/False) |
| UInt8 | Unsigned 8-bit integer |
| Int8 | Signed 8-bit integer |
| UInt16 | Unsigned 16-bit integer |
| Int16 | Signed 16-bit integer |
| UInt32 | Unsigned 32-bit integer |
| Int32 | Signed 32-bit integer |
| Float | Signed 32-bit floating-point number <sup>1)</sup> |
| String | Sequence of characters |
| Variant | Object that can have any data type. |
| DateTime | Date/time information |
| StringStringMap | Map: Value pairs from strings |
| Promise | Object |
| Object | Object |
| Function | Method |
| ErrorCode | Error code |
| <sup>1)</sup> JavaScript supports floating-point numbers with a mantissa up to 54 bits. In scripting and Web client, values with a mantissa greater than 54-bit are therefore rounded. This affects tag values and constants in the properties of screen objects.   Values with a mantissa of up to 64 bits are correctly displayed by I/O fields. |  |

### Object instances (RT Unified)

#### Create objects

In the object model, all object instances are returned via access methods. There are no constructors that create objects.

**Example**

var t1 = Tags("Tag_1"); // returns HMITag object

var screenItem1 = Screen.FindItem("Button_1"); // returns HMIScreenItem object

**Error example**

var t1 = new Tag("Tag_1"); // Error!

### Enumerations (RT Unified)

#### Description

Enumerations are enumeration types. Objects of this data type consist of elements with static values. Each permissible value has a unique name and an assigned integer.

Here is an example for the background fill pattern of screen objects. The enumeration has the name "HmiFillPattern" and defines the following 16 values with name and integer.

- Solid (0)
- Transparent (65536)
- Horizontal (131072)
- Vertical (131073)
- ForwardDiagonal (131074)
- BackwardDiagonal (131075)
- Cross (131076)
- DiagonalCross (131077)
- GradientHorizontal (1048576)
- GradientVertical (1048577)
- GradientForwardDiagonal (1048578)
- GradientBackwardDiagonal (1048579)
- GradientHorizontalTricolor (1048832)
- GradientVerticalTricolor (1048833)
- GradientForwardDiagonalTricolor (1048834)
- GradientBackwardDiagonalTricolor (1048835)

#### Use of enumerations

All enumeration can be found directly in context of their respective property.

Values of enumerations can be reference in scripts using the name or integer.

By way of example, the "GetSpecialFolder()" method of the "FileSystem" object is used for this in the following. This method can return the current temporary directory or the user directory according to the "FolderId" enumeration:

- TempDir (0): Directory for the temporary files
- HomeDir (1): Directory for the files of the current user

**Referencing the value using the name of the element**

Every enumeration can be addressed using the "Enums" object. This is followed by the name of the enumeration and the name of the desired element to reference the value:

Copy code

let tempDir = HMIRuntime.FileSystem.GetSpecialFolder(HMIRuntime.FileSystem.Enums.FolderId.TempDir);

HMIRuntime.Trace("Temp folder path: " + tempDir);

**Referencing the value using the integer of the element**

The value can also be directly referenced using the integer of the element:

Copy code

let tempDir = HMIRuntime.FileSystem.GetSpecialFolder(0);

HMIRuntime.Trace("Temp folder path: " + tempDir);

### Asynchronous operations (RT Unified)

#### Promises in JavaScript

Promises are used in the script environment to handle asynchronous operations. A `Promise` object contains placeholders for results of an operation that are not yet known.

A `Promise` has the following status:

- Pending: Operation of the `Promise` object is still being executed.
- Settled: Operation of the `Promise` object has been completed.

  - Fulfilled: Operation was successful. Result is a value.
  - Rejected: Operation was unsuccessful. Result is a `reason`.

    `reason` may contain an error code for an object with text, links or any other conceivable contents of an object. For this reason, for targeted error processing, it is advisable for `reason` to use an instance of an `Error` object.

As soon as the operation has been completed, a corresponding Handler with the available result is called.

Promises minimize latencies (delay times caused by signal processing), because the script continues to be executed during evaluation. In contrast, a script stops with asynchronous calls. Promises allow clean error handling with the "`catch`" method.

Promises can be cascaded in order to transform results or to sequence asynchronous operations.

#### Using promises

In the simplest form, promises return a value or error which is processed with the "then" and "catch" methods of the `Promise` object:

getPromise()

.then(function(Value) {

...

})

.catch(function(ErrorCode) {

...

});

Cascaded promises each return a Promise and allow a sequence of asynchronous calls:

getPromise()

.then(return p1)

.then(return p2)

.then(return p3)

.catch();

The functions of the `Promise` objects are executed in the order p1 > p2 > p3 and the "catch" method is called in case of error. All tags of the calling function are also available in the internal functions.

### Support for errors (RT Unified)

The user has various options of diagnosing errors and then rectifying them.

#### Trace Log

WinCC writes a log file for every subsystem. This file contains helpful information of the respective subsystem for narrowing down possible error causes.

> **Note**
>
> The log files are located in the directory "%PROGRAMDATA%\Siemens\Automation\Logfiles\WinCC_Unified_SCADA_V*".

#### Trace Viewer

The Trace Viewer is an external application for the display and targeted filtering of Trace alarms.

---

**See also**

[RTIL Trace Viewer (RT Unified)](#rtil-trace-viewer-rt-unified)

### Global modules (RT Unified)

Global modules can only be linked with the global definition (script). All scripts except the global definition are simple functions.

The "import" statement must be a top-level statement.

#### Description

A global module is a container for one or more global functions with a shared definition area.

Several global modules can be created for each device.

Global modules are suitable for categorizing or grouping global functions.

> **Note**
>
> **Consider context when using global modules**
>
> After the import, a global module behaves like a local script. For example, it is not possible to use a global module on a task if a screen or screen object is referenced in the global module or an associated function. If an invalid reference to a screen or screen object is contained in a global module imported at a task, an error is output.

#### Call and view

Global modules are represented in the project tree in the respective device under "Scripts" as folder icons with the letters "JS" ![Call and view](images/112361925387_DV_resource.Stream@PNG-de-DE.png).

![Call and view](images/133762160651_DV_resource.Stream@PNG-en-US.png)

You can create new global modules via the shortcut menu of "Scripts".

You can create new global functions via the shortcut menu of the desired global module.

You can also add new global modules and functions via "Add ... new" in the project tree.

#### References to global modules

When you rename a global module, the alias is automatically renamed in all places where the global module is referenced.

References to functions defined in a global module are automatically updated in:

- Local scripts
- Global scripts
- Global definitions

Naming within the project remains consistent and runtime errors are avoided.

#### Examples

- General mathematical operations
- General logic operations
- Conversions of units of measurement

---

**See also**

[Local scripts (RT Unified)](#local-scripts-rt-unified)

### Local scripts (RT Unified)

A local script is a function written in JavaScript which is assigned to the object in question.

#### Starting local scripts

A local script is always started by a trigger:

- an event at a screen object
- a trigger on dynamization of object properties (cycle or change of a tag value)
- the event "Update" of a task in the Scheduler (cycle, change to a tag value or alarm)

#### Access to global modules

Local scripts can call functions which are contained in the scripts of global modules.

#### Applications

For example, local scripts can be used to

- dynamize object properties,
- process user entries and
- automatize complex operations

---

**See also**

[Script and execution context (RT Unified)](#script-and-execution-context-rt-unified)
  
[Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
  
[Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)
  
[Creating a global definition in a local script (RT Unified)](#creating-a-global-definition-in-a-local-script-rt-unified)
  
[Basics of cycles (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#basics-of-cycles-rt-unified)

## "Scripts" editor (RT Unified)

This section contains information on the following topics:

- [Structure of the "Scripts" editor (RT Unified)](#structure-of-the-scripts-editor-rt-unified)
- [Input support (RT Unified)](#input-support-rt-unified)
- [Script and execution context (RT Unified)](#script-and-execution-context-rt-unified)
- [Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
- [Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)
- [Creating a global definition in a local script (RT Unified)](#creating-a-global-definition-in-a-local-script-rt-unified)

### Structure of the "Scripts" editor (RT Unified)

In the "Scripts" editor, you create and edit customized JavaScript functions.

The "Scripts" editor can be opened in the following execution contexts:

- Global functions in global modules

  You open the "Scripts" editor via the project tree by double-clicking a script.
- Local scripts which are triggered by events ("Images" editor and Scheduler)

  The "Scripts" editor is opened in the Inspector window under "Properties > Events" as soon as you have selected an event and selected the ![Figure](images/151911935115_DV_resource.Stream@PNG-de-DE.png) "Convert function list to script" button.

  Additional local scripts which are triggered by events can be triggered for each property under "Properties > Properties" for the events "Change" and "Quality code change".
- Local scripts for dynamizing object properties

  The "Scripts" editor is opened in the Inspector window under "Properties > Properties" as soon as you select the "Scripts" entry in the "Dynamization" column.

#### Different representation formats

Depending on the application, the "Scripts" editor is shown in different areas of TIA Portal and contains different operator controls.

Depending on the execution context, the code area opens either as a new editor window in the working area (global modules) or embedded in the Inspector window (local script).

#### Overview

![Overview](images/137828256523_DV_resource.Stream@PNG-en-US.png)

The code area represents the actual JavaScript code.

Buttons are located above the code area. Depending on the application context, buttons are available with specific functions:

| Button | Description | Global modules | Event-related functions | Dynamization of object properties |
| --- | --- | --- | --- | --- |
| ![Overview](images/137828534923_DV_resource.Stream@PNG-de-DE.png) | Syntax check | ✓ | ✓ | ✓ |
| ![Overview](images/137828825099_DV_resource.Stream@PNG-de-DE.png) | Shows / hides the code area for the global definition. | × | ✓ | ✓ |
| ![Overview](images/137828948875_DV_resource.Stream@PNG-de-DE.png) | Specifies whether the function is synchronous/asynchronous | ✓ | ✓ | ✓ |
| ![Overview](images/137828957451_DV_resource.Stream@PNG-de-DE.png) | Enables the auto-completion of entries | ✓ | ✓ | ✓ |
| ![Overview](images/137828966027_DV_resource.Stream@PNG-de-DE.png) | Shows information or provides a tip for the place in the code where the insertion point is located | ✓ | ✓ | ✓ |
| ![Overview](images/137828987403_DV_resource.Stream@PNG-de-DE.png) | Deletes the script | × | ✓ | × |
| ![Overview](images/137829051531_DV_resource.Stream@PNG-de-DE.png) | Selects the trigger of dynamization (cycle or tag) | × | × | ✓ |
| ![Overview](images/137828995979_DV_resource.Stream@PNG-de-DE.png) | Sets the insertion point to the previous error in the code | ✓ | ✓ | ✓ |
| ![Overview](images/137829017355_DV_resource.Stream@PNG-de-DE.png) | Sets the insertion point to the next error in the code | ✓ | ✓ | ✓ |

> **Note**
>
> Asynchronous functions cannot be used if the function returns a value.
>
> Alternatively, the value can be specified via the respective property.

#### Shortcut menu

The shortcut menu contains so-called "snippets". Snippets provide frequently required code templates.

---

**See also**

[Global modules (RT Unified)](#global-modules-rt-unified)
  
[Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
  
[Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)
  
[Input support (RT Unified)](#input-support-rt-unified)

### Input support (RT Unified)

#### Introduction

You create the JavaScript code of your scripts in the code area of the "Scripts" editor.

The editor supports you with the following functions:

- Syntax highlighting
- Snippets (code templates)
- System functions
- Referencing HMI objects
- Tooltips
- Autocomplete
- Error marking and correction
- Find and replace

#### Syntax highlighting

![Syntax highlighting](images/85807786763_DV_resource.Stream@PNG-de-DE.png)

The JavaScript code in the code area of the editor is highlighted in different colors to make it easier to read.

#### Snippets for programming support

Snippets are code templates for frequently required instructions: Snippets are divided into the following groups:

- HMIRuntime

  Contains Snippets for accessing the object model, e.g. "`Change base screen`" or "`Set Connection Mode`".
- Logic

  Contains Snippets such as "`If...Else`" or "`For loop`".
- Faceplate

  Only available in a faceplate.

You insert a Snippet in the local script via the shortcut menu.

#### System functions

The system functions are provided in the "Scripts" editor. For more information, refer to "System functions".

#### Referencing HMI objects

HMI objects (e.g. tags and screens) are referenced in scripts.

Therefore, you perform the following actions without editing the script:

- Rename HMI object
- Re-create a previously deleted HMI object
- Create HMI object used as text reference in the script

#### Info tips

While you compose the code, additional information about all objects of the WinCC Unified object model is displayed. For example, you receive information on the required parameters of the system functions.

#### Autocomplete

![Autocomplete](images/126485988619_DV_resource.Stream@PNG-de-DE.PNG)

Autocomplete supports you in entering your code. Suitable objects of the WinCC Unified object model are displayed.

You call up autocomplete using the shortcut <Ctrl + I> or <Ctrl + Spacebar>.

#### <Ctrl+J>

The object selection can be called context-specifically by using the shortcut <Ctrl+J>. For example, you select screens, screen objects, tags, or graphics.

#### Error marking and correction

Errors can occur during compiling or during compiling and loading:

- Error while configuring

  Your JavaScript code is checked immediately during input for a variety of criteria and highlighted in color in case of errors.

  - To get a tooltip, move the cursor over the marking.
- Errors during compiling and loading

  Alarms during the compiling and loading of a project are displayed in the Inspector window in the "Info > Compile" tab.

  The "Scripts" editor supports you by displaying faulty scripts directly for editing:

  - To go directly to the "Scripts" editor, select the green arrow ![Error marking and correction](images/125111278731_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[System functions (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified)

### Script and execution context (RT Unified)

#### Introduction

Scripts are functions in the form of JavaScript code that you develop yourself.

You can use scripts to solve individual tasks, e.g.

- Automating processes
- Dynamizing objects
- Evaluating events, such as user input

The execution of a script is triggered by:

- An event
- A tag change
- A scheduled job

#### Preparation for creating and using scripts

In advance of creating the script, consider where you will enter the script and how it will be executed.

Depending on the objects and system components addressed, you enter the JavaScript code in different editors. The editors have a similar structure.

Depending on the execution context, the script is executed with different scopes.

> **Note**
>
> Each module has its own namespace, which means it is possible to use the same function name and global tag name in two modules.
>
> The functions are distinguished by the symbol name of the imported module.
>
> Example:
>
> `import * as modA from 'ModuleA';`
>
> `import * as modB from 'ModuleB';`
>
> `modA.function1();`
>
> `modB.function1();`

| Execution context of the editor | Script context and referencing |
| --- | --- |
| "Script" editor in the "Screens" editor | Each screen has two independent script contexts:  - Context for dynamization of properties - Context for evaluation of events   The script of a property cannot access global tags of an event even in the same screen.  Each script context references the modules that it has imported using the 'import' statement. However, each script context receives its own copy of the tags defined there. |
| "Script" editor for "Scheduled tasks" | All jobs share a script context.  Different tasks can access common global tags.  Each required module must be referenced by means of the 'import' statement. |

#### Create "import" statement

A module can be referenced in a script or another module:

- Drag-and-drop the module to be referenced into the "Global Definition" area of the script or into the definition area of the module.

> **Note**
>
> **Copying the "import" statement together with objects**
>
> If you copy a screen object and paste it into another screen, then the "import" statement is copied and pasted when the imported global module is used on the source object.
>
> If the copied module has already been referenced under a different alias at the target, the copied module is inserted additionally.

---

**See also**

[Local scripts (RT Unified)](#local-scripts-rt-unified)
  
[Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
  
[Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)
  
[Creating a global definition in a local script (RT Unified)](#creating-a-global-definition-in-a-local-script-rt-unified)
  
[WinCC Unified object model (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#wincc-unified-object-model-rt-unified-1)
  
[Simulating value changes in tags (RT Unified)](#simulating-value-changes-in-tags-rt-unified)
  
[Converting values (RT Unified)](#converting-values-rt-unified)

### Configuring a script to an event (RT Unified)

> **Note**
>
> **Restriction of "activated" and "deactivated" events**
>
> If the focus is on the affected screen item, scripts are executed at the "activated" and "deactivated" events.

#### Requirement

- One of the following objects is configured:

  - Task
  - Screen
  - Screen object

#### Procedure

To configure a script to an event, follow these steps:

1. Open the relevant editor.
2. Select the object.
3. Select the event under "Properties > Events" in the Inspector window.
4. Generate the local script.
5. Write the code.
6. Perform a syntax check.
7. Save the project.

---

**See also**

[Introduction to runtime scripting (RT Unified)](#introduction-to-runtime-scripting-rt-unified)
  
[Local scripts (RT Unified)](#local-scripts-rt-unified)
  
[Script and execution context (RT Unified)](#script-and-execution-context-rt-unified)
  
[Creating a global definition in a local script (RT Unified)](#creating-a-global-definition-in-a-local-script-rt-unified)

### Dynamizing object properties by script (RT Unified)

#### Requirement

- One of the following objects is configured:

  - Screen
  - Screen object
- The selected object property supports the dynamization type "Script".

#### Procedure

1. Open the editor of the object in question.
2. Select the object.
3. Select the desired object property under "Properties > Properties" in the Inspector window.
4. Dynamize the object property:

   - Select the "Script" entry in the "Dynamization" column.

     The editor creates a script and is displayed in the Inspector window.
   - Write the code.
5. Select the trigger that triggers the dynamization in runtime.

#### Result

The script changes the selected property dynamically in line with the written code.

---

**See also**

[Local scripts (RT Unified)](#local-scripts-rt-unified)
  
[Creating a global definition in a local script (RT Unified)](#creating-a-global-definition-in-a-local-script-rt-unified)

### Creating a global definition in a local script (RT Unified)

#### Procedure

1. Open the local script.
2. Click "Global definition".
3. Write the code.
4. Perform a syntax check.
5. Edit the function.

---

**See also**

[Local scripts (RT Unified)](#local-scripts-rt-unified)
  
[Script and execution context (RT Unified)](#script-and-execution-context-rt-unified)
  
[Configuring a script to an event (RT Unified)](#configuring-a-script-to-an-event-rt-unified)
  
[Dynamizing object properties by script (RT Unified)](#dynamizing-object-properties-by-script-rt-unified)

## Examples (RT Unified)

This section contains information on the following topics:

- [Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)
- [Dynamizing the position of an object (RT Unified)](#dynamizing-the-position-of-an-object-rt-unified)
- [Reading and writing tag values (RT Unified)](#reading-and-writing-tag-values-rt-unified)
- [Simulating value changes in tags (RT Unified)](#simulating-value-changes-in-tags-rt-unified)
- [Using tag values globally (RT Unified)](#using-tag-values-globally-rt-unified)
- [Converting values (RT Unified)](#converting-values-rt-unified)
- [Change language (RT Unified)](#change-language-rt-unified)
- [Dynamically changing the output format of an object (RT Unified)](#dynamically-changing-the-output-format-of-an-object-rt-unified)
- [Reading and writing binary files (RT Unified)](#reading-and-writing-binary-files-rt-unified)
- [Reading and writing text files (RT Unified)](#reading-and-writing-text-files-rt-unified)
- [Setting bits (RT Unified)](#setting-bits-rt-unified)
- [Changing the date format (RT Unified)](#changing-the-date-format-rt-unified)
- [Monitoring alarms (RT Unified)](#monitoring-alarms-rt-unified)
- [Set alarm filter (RT Unified)](#set-alarm-filter-rt-unified)
- [Creating an alarm subscription (RT Unified)](#creating-an-alarm-subscription-rt-unified)
- [Creating alarms with multilingual alarm texts (RT Unified)](#creating-alarms-with-multilingual-alarm-texts-rt-unified)
- [Opening and closing a screen in a pop-up window (RT Unified)](#opening-and-closing-a-screen-in-a-pop-up-window-rt-unified)
- [Triggering a screen change with a tag (RT Unified)](#triggering-a-screen-change-with-a-tag-rt-unified)
- [Connecting Unified Comfort Panel with SQL database (RT Unified)](#connecting-unified-comfort-panel-with-sql-database-rt-unified)

### Notes on the code examples (RT Unified)

#### General

The comments at the beginning of each code example are required for technical reasons.

At the same time these comments show the relationships between various code examples within a chapter.

Further comments in the code examples explain individual program code lines.

#### Executing examples

1. Set the language of the develop environment to "English", so that the object names used in the examples are automatically assigned correctly.
2. Create a project with corresponding screens in which you can configure buttons, I/O fields, etc. These elements are required to carry out the code examples.
3. Apply the code examples to the associated script areas.
4. Compile the project.
5. Start the simulation of the project.
6. Start the tracer to diagnose potential errors.

---

**See also**

[RTIL Trace Viewer (RT Unified)](#rtil-trace-viewer-rt-unified)

### Dynamizing the position of an object (RT Unified)

#### Introduction

The example shows how to dynamically change an object position using JavaScript.

One classic application would be the adjustment of the object position to the size and/or position of adjacent objects on a screen.

#### Execution of example

1. Configure 4 tags with the names "HMI_Tag1" to "HMI_Tag_4".
2. Configure a screen with the following objects:

   - 4 objects of the type I/O field with the process values "HMI_Tag_1" to "HMI_Tag_4"
   - 1 object of the type "Circle" with the name "Circle_1"
   - 1 object of the type "Button" with the name "Button_1"
3. Dynamize the parameters "Position X" and ""Position" Y" of the objects "Circle_1" and "Button_1" using scripts.
4. Set the triggers for dynamization with the tags

   - HMI_Tag_1 for Button_1/Position X,
   - HMI_Tag_2 for Button_1/Position Y,
   - HMI_Tag_3 for Circle_1/Position X,
   - HMI_Tag_4 for Circle_1/Position Y.

   The scripts are started accordingly by changing the tag.
5. Copy the sample code below to your project.

#### Reading out and returning the tag `HMI_Tag_1`

The script with the function "`Circle_1_CenterX_Trigger(item)`" is created when the parameter "Position X" is dynamized by a script in the properties of the object "Circle_1".

//JEx: "Position X dynamization of a Circle with tags"

//TagsRequired: "HMI_Tag_1"

export function Circle_1_CenterX_Trigger(item) {

    var value = Tags("HMI_Tag_1").Read();

    return value;

}

#### Reading out and returning the tag `HMI_Tag_2`

The script with the function "`Circle_1_CenterY_Trigger(item)`" is generated when the parameter "Position Y" is dynamized by a script in the properties of the object "Circle_1".

//JEx: "Position Y dynamization of a Circle with tag"

//TagsRequired: "HMI_Tag_2"

export function Circle_1_CenterY_Trigger(item) {

    var value = Tags("HMI_Tag_2").Read();

    return value;

}

#### Reading out and returning the tag `HMI_Tag_3`

The script with the function "`Button_1_Left_Trigger(item)`" is generated when the parameter "Position X" is dynamized by a script in the properties of the object "Button_1".

//JEx: "Position X dynamization of a Button with tag"

//TagsRequired: "HMI_Tag_3"

export function Button_1_Left_Trigger(item) {

    var value = Tags("HMI_Tag_3").Read();

    return value;

}

#### Reading out and returning the tag `HMI_Tag_4`

The script with the function "`Button_1_Top_Trigger(item)`" is generated when the parameter "Position Y" is dynamized by a script in the properties of the object "Button_1".

//JEx: "Position Y dynamization of a Button with tag"

//TagsRequired: "HMI_Tag_4"

export function Button_1_Top_Trigger(item) {

    var value = Tags("HMI_Tag_4").Read();

    return value;

}

#### Result (in runtime)

The position of the object in question changes in accordance with the values entered in the I/O fields.

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Reading and writing tag values (RT Unified)

#### Introduction

The example shows how to read, multiply and write the values from two tags ("HMI_Tag_2", "HMI_Tag_3") to another tag ("HMI_Tag_1").

In practical use, the tags could represent the following parameters:

- "HMI_Tag_1": Apparent power S
- "HMI_Tag_2": Electrical voltage U
- "HMI_Tag_3": Electrical current I

#### Executing an example

1. Configure three tags "HMI_Tag_1" to "HMI_Tag_3" of the type "Int".
2. You configure the following objects on a screen:

   - 1 button (in the example "Button_1")
   - 3 I/O fields with the process values "HMI_Tag_1" to "HMI_Tag_3"
3. Create a script for the event "Click left mouse button".

   The JavaScript editor creates the function "`Button_1_OnTapped(item, x, y, modifiers, trigger)`".
4. Insert the example code.

#### Sample code

//JEx: "Reading and writing tag values"

//Tags_Required: "HMI_Tag_1"; "HMI_Tag_2"; "HMI_Tag_3"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

Tags("HMI_Tag_1").Write(Tags("HMI_Tag_2").Read() * Tags("HMI_Tag_3").Read());

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Simulating value changes in tags (RT Unified)

#### Introduction

This example shows how tags are supplied with values in defined time intervals by a simulation.

With the simulation, demo projects can be created or tested without process integration.

> **Note**
>
> **Connection of existing process tags leads to influencing of processes**
>
> The simulation writes the calculated values to the tags without further test steps.
>
> - Do not link any external tags; these remain linked to any existing process.
>
>   The simulation thus influences the process in which the external tag is integrated.
> - If you purposely want to influence a process with simulation, note that the external tag of the process can only be reached for simulation if the following requirements are met:
>
>   - The connection to the controller (PLC) is established.
>   - The controller (PLC) is in "RUN" mode.

The global functions for generating sine and sawtooth waves use 5 parameters:

- `counter`: Counter that uses the current date in milliseconds.
- `phase`: Phase offset as a factor between 0.0 and 1.0

  The factor 0.0 to 1.0 corresponds to a phase offset of 0° to 360°.
- `period`: Duration of a full vibration cycle in milliseconds
- `amp`: Strength of the amplitude
- `offset`: Shift of the amplitude on the y-axis

#### Executing an example

1. Create a global "Simulator" module.
2. Configure the two functions "sinWave" and "sawTooth" in this global module.

   Use the source codes from the following sections for the functions:

   - "Example code > Simulate sine wave (global script)"
   - "Example code > Simulate sawtooth wave (global script)"
3. Create a script for the "Loaded" event for the screen.
4. Go to the "Global definition" view of the event.
5. Insert the sample code under "Sample code > Event - Global definition area" in the "Global definition" view of the event.
6. If necessary, adapt the copied sample code to your project. For example, if you use more than 2 tags, you must add more lines with the function `ts.Add(...)`.
7. Go back to the "Function" view of the event.
8. Insert the source code from "Example code > Event".

The tags HMI_Tag_1 and HMI_Tag_2 can now be connected to any objects in the screen that can display the values, such as:

- Function trend control
- Gauges
- Bar graphs
- Text fields

#### Result

1. When the application is loaded in runtime, the `import` function initializes the scripts from the global module "Simulator" for the "Loaded" event of the screen.

   The example code can be found under "Event - Global definition area".
2. If the event is triggered when the screen is loaded, the function "simulateTags()" starts at the specified intervals.

   In the example, the interval is 500 ms.

   The call of the function "simulateTags()" is stopped as soon as the screen is deselected.

   The example code can be found under "Event" and "Event - Global definition area".
3. The function "simulateTags()" starts with each call of the functions "sinWave" and "sawTooth" and transfers the new values to the tags.

   The example code can be found under "Simulate sine wave (global script)" and "Simulate sawtooth wave (global script)".

#### Sample code

**Simulate sine wave (global script)**

//JEx: "Simulate Sine Wave"

export function sinWave(counter, phase, period, amp, offset) {

 return offset + amp * Math.sin((phase + ((counter % period) / period)) * (2*Math.PI));

}

**Simulate sawtooth wave (global script)**

//JEx: "Simulate Saw Tooth Wave"

export function sawTooth(counter, phase, period, amp, offset) {

 return offset + amp * (((counter + phase * period) % period) / period);

}

**Global event definition area**

//JEx: "Generate signals"

//SOM_OM_"HmiTrendControl"

//JExRequired: "Simulate Sine Wave", "Simulate Saw Tooth Wave"

import * as sim from "Simulator";

function simulateTags() {

 let counter = Date.now();

 let ts = Tags.CreateTagSet();

 ts.Add([['HMI_Tag_1', sim.sinWave(counter, 0.00, 10000, 25, 25)]]);

 ts.Add([['HMI_Tag_2', sim.sawTooth(counter, 0.25, 37000, 30, 15)]]);

 ts.WriteAsync();

}

**Event**

//JEx: "Event Screen_1 OnLoad"

//SOM_OM_"HmiTrendControl"

//JExRequired: "Generate signals"

export function Screen_1_OnLoad(item) {

 HMIRuntime.Timers.SetInterval(simulateTags, 500);

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Using tag values globally (RT Unified)

#### Introduction

The example shows how to use tag values globally. A tag value can therefore be shared between screens and tasks, for example.

The basic procedure is as follows:

1. The tag value is written into an internal tag via a script.
2. The tag value is read by another script at the desired place.

You can save and read the values of all data types supported by the object model in internal tags.

#### Executing an example

The following example writes a structured value of a JavaScript tag to an internal tag. Another member is added to the structured value in the sample code on button 2.

1. Configure an HMI tag "Tag".
2. Configure two buttons (in the example "Button_1" and "Button_2") on a screen.
3. Create a script for each "Click left mouse button" event of the buttons.

   The JavaScript editor creates the functions "`Button_1_OnTapped(item, x, y, modifiers, trigger)`" and `Button_2_OnTapped(item, x, y, modifiers, trigger)`.
4. Insert the sample code "Write structured value into internal tag" into the script of the first button.
5. Insert the sample code "Enhance structure by member "c"" into the script of the second button.
6. Compile and load it in runtime.
7. Trigger the event "Click left mouse button" on both buttons.

#### Result

**Button 1**

1. The JavaScript tag "tag" is created and initialized with the HMI tag "Tag".
2. The JavaScript tag "myObj" is created and initialized.
3. The JavaScript tag "myObj" is converted into a JSON string and assigned to the JavaScript tag "json".
4. The value of the JavaScript tag "json" is written into the HMI tag "Tag".

**Button 2**

1. The JavaScript tag "tag" is created and initialized with the HMI tag "Tag".
2. The JavaScript tag "myObj" is created and initialized.
3. The JavaScript tag "myObj" is extended by the member "c".
4. The JavaScript tag "myObj" is converted into a JSON string and assigned to the JavaScript tag "json".
5. The value of the JavaScript tag "json" is written into the HMI tag "Tag".

#### Sample code

**Write structured value into internal tag**

//JEx: "set initial values without 'c'"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

let tag = Tags('Tag');

let myObj = {a:10, b:20, pos: {x:100, y:200}, layers: [1, 8, 18, 24, 33]};

let json = JSON.stringify(myObj);

HMIRuntime.Trace('Jason ' + json);

tag.Write(json, 1);

}

**Enhance structure by member "c"**

//JEx: "add member 'c'"

export function Button_2_OnTapped(item, x, y, modifiers, trigger) {

const tag = Tags('Tag');

let myObj = JSON.parse(tag.Read(1));

myObj.c = (myObj.c || 0) + 1; // increment 'c'

let json = JSON.stringify(myObj);

HMIRuntime.Trace("New JSON: " + json);

tag.Write(json, 1);

}

### Converting values (RT Unified)

#### Introduction

The example shows how temperature values can be converted into a different unit with JavaScript.

#### Executing an example

1. Create a global module "TemperatureConversions" with 2 global scripts:

   - "celsiusToFahrenheit(t_celsius)"
   - "fahrenheitToCelsius(t_fahrenheit)"
2. Copy the corresponding sample code to the global scripts.
3. Copy the sample code from the "Global definition range" to the global definition range of the global module "TemperatureConversion".
4. Create a screen with 2 elements of the type "I/O field".
5. Dynamize the "Process value" property of the two "I/O field" elements using scripts.
6. Copy the sample code of both scripts.

#### Celsius to Fahrenheit (global script)

//JEx: "CelsiusToFahrenheit"

//JExRequired: "TempConv_GlobalDefRange"

export function celsiusToFahrenheit(t_celsius) {

return t_celsius * 1.8 + 32;

}

#### Fahrenheit to Celsius (global script)

//JEx: "FahrenheitToCelsius"

//JExRequired: "TempConv_GlobalDefRange"

export function fahrenheitToCelsius(t_fahrenheit) {

return (t_fahrenheit - 32) / 1.8;

}

#### Global definition range

//JEx: "TempConv_GlobalDefRange"

import * as tempConv from 'TemperatureConversion';

#### Celsius to Fahrenheit (dynamization of process value)

The JavaScript function is triggered by the tag 'celsius1'.

//JEx: "DynCelsiusToFahrenheit"

//SOM_OM_"HmiIOField"

//TagsRequired: "celsius1"

//JExRequired: "celsiusToFahrenheit"

//JExRequired: "TempConv_GlobalDef"

export function I_O_field_1_ProcessValue_Trigger(item) {

const tagCelsius = Tags('celsius1');

tagCelsius.Read();

return tempConv.celsiusToFahrenheit(tagCelsius.Value);

}

#### Fahrenheit to Celsius (dynamization of process value)

The JavaScript function is triggered by the tag 'fahrenheit1'.

//JEx: "DynFahrenheitToCelsius"

//SOM_OM_"HmiIOField"

//TagsRequired: "fahrenheit1"

//JExRequired: "fahrenheitToCelsius"

//JExRequired: "TempConv_GlobalDef"

export function I_O_field_2_ProcessValue_Trigger(item) {

const tagFahrenheit = Tags('fahrenheit1');

tagFahrenheit.Read();

return tempConv.fahrenheitToCelsius(tagFahrenheit.Value);

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Change language (RT Unified)

#### Introduction

The example shows how the interface language is changed by JavaScript.

#### Executing an example

1. Configure a button "Button_1".
2. Activate the project languages required for the example:

   - English
   - German
   - Hungarian
   - French
3. Create a script for the event "Left mouse button clicked" of the button "Button_1".
4. Define the tag "step" under "Global definition" and assign the value "2" to it.

#### Global definition

//JEx: "LanguageChangeGlobalDef"

var step = 2;

#### Sample code

Clicking the button increments the tag "step". The stored code for the language is assigned to `HMIRuntime.Language` according to its value.

//JEx: "LanguageChange"

//JExRequired: "LanguageChangeGlobalDef"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

//change to English

if (step == 1) {HMIRuntime.Language = "1033";}

//change to Hungarian

if (step == 2) {HMIRuntime.Language = "1038";}

//change to German

if (step == 3) {HMIRuntime.Language = "1031";}

//change to French

if (step == 4) {HMIRuntime.Language = "1036";}

step ++; //step

if (step == 5) {step = 1;} //reset

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Dynamically changing the output format of an object (RT Unified)

#### Introduction

This example shows how to dynamically change the output format of an object of the type "I/O field" using JavaScript.

The output in the example is switched between the following formats:

- Hexadecimal
- Decimal
- Binary

#### Executing an example

1. Configure a screen page with 3 buttons with the names "Button_1" to "Button_3".
2. Configure max. nine objects of the "I/O field" type with the names "HmiIOField_1" to "HmiIOField_9".
3. Create a script for the event "Button pressed" for each button.
4. Define the constants as described in the section "Global definition of constants".
5. Create 2 global scripts:

   - toggleOutputFormat()
   - setOutputFormat(format)
6. Transfer the source code from the following sections.

#### Global script "toggleOutputFormat()"

//JEx: "Toggle Output Format"

//SOM_OM_"HmiIOField"

//JExRequired: "Set Output Format";"GlobalConstants for OutputFormat"

function toggleOutputFormat() {

let index = outputFormats.indexOf(Screen.FindItem(screenItemNameBase + minScreenItemIndex).OutputFormat);

index = (index + 1) % outputFormats.length;

setOutputFormat(outputFormats[index]);

}

#### Global script "setOutputFormat(format)"

//JEx: "Set Output Format"

//SOM_OM_"HmiIOField"

//JExRequired: "GlobalConstants for OutputFormat"

function setOutputFormat(format) {

for(let i = minScreenItemIndex; i <= maxScreenItemIndex; i++) {

let name = screenItemNameBase + i;

Screen.FindItem(name).OutputFormat = format;

}

}

#### Global definition of constants

//JEx: "GlobalConstants for SetOutputFormat"

const outputFormats = ['{I}', '{H2,2}', '{B8,4}'];

// Creating dynamic object names which differ by a number at the end

const screenItemNameBase = 'HmiIOField_';

// the screen item names begin with the prefix 'HmiIOField_'

const minScreenItemIndex = 1; // range of the screen items: min

const maxScreenItemIndex = 9; // range of the screen items: max

#### Switch to hexadecimal output format

//JEx: "Switch Output Format Hex"

//SOM_OM_"HmiIOField"

//JExRequired: "Set Output Format"

export function Button_1_OnDown(item, x, y, modifiers, trigger) {

setOutputFormat('{H2,2}');

}

#### Switch to decimal output format

//JEx: "Switch Output Format Dec"

//SOM_OM_"HmiIOField"

//JExRequired: "Set Output Format"

export function Button_2_OnDown(item, x, y, modifiers, trigger) {

setOutputFormat('{I}');

}

#### Switch to the next output format

//JEx: "Switch Output Format Bin"

//SOM_OM_"HmiIOField"

//JExRequired: "Toggle Output Format"

export function Button_3_OnDown(item, x, y, modifiers, trigger) {

toggleOutputFormat();

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Reading and writing binary files (RT Unified)

#### Introduction

The example shows how to write a binary file to the file system with JavaScript.

> **Note**
>
> - For access to the data, use the class "DataView" or one of the "*Array" classes together with the class "arrayBuffer".
> - If the Endianess of the computer systems used for development (Compiler) and execution (Runtime) are different, use the class "DataView".
> - The method HMIRuntime.Trace(text) outputs whether the function was successful via the Tracer.

#### Executing an example

1. Configure 3 buttons with the names "Button_10", "Button_11" and "Button_14".
2. Create a script for the event "Print" for each button.
3. Copy the sample code below to your project.

#### Writing a binary file

//JEx: Write a binary file with class "Int32Array" into file system

export function Button_10_OnDown(item, x, y, modifiers, trigger) {

var arrayBuffer = new Int32Array([1,2,3]);

HMIRuntime.FileSystem.WriteFileBinary('C:\\Users\\Public\\binaryfile.bin', arrayBuffer).then(

function() {

HMIRuntime.Trace('Write file finished successfully');

}).catch(

function(e) {

HMIRuntime.Trace(`Write file failed with error code ${e}`);

});

}

#### Reading a binary file with the class `Int32Array`

//JEx: Read a binary file with class "Int32Array" from file system

export function Button_11_OnDown(item, x, y, modifiers, trigger) {

var arrayBuffer = new Int32Array([1,2,3]);

HMIRuntime.FileSystem.ReadFileBinary('C:\\Users\\Public\\binaryfile.bin', arrayBuffer).then(

function(arrayBuffer) {

let intView = new Int32Array(arrayBuffer);

    for(let i in intView) {

HMIRuntime.Trace('intView[' + i  + '] = ' + intView[i]);

}

}).catch(

function(e) {

HMIRuntime.Trace(`Read file failed with error code ${e}`);

});

}

#### Reading a binary file with the class `DataView`

//JEx: Read a binary file with class "DataView" from file system

export function Button_14_OnDown(item, x, y, modifiers, trigger) {

HMIRuntime.FileSystem.ReadFileBinary('C:\\Users\\Public\\binaryfile.bin').then(

function(arrayBuffer) {

let dv = new DataView(arrayBuffer, 0, arrayBuffer.length);

HMIRuntime.Trace('Int32[0] LE:' + dv.getInt32(0, true).toString(16));

HMIRuntime.Trace('Int32[0] BE:' + dv.getInt32(0      ).toString(16));

HMIRuntime.Trace('Int16[2] LE:' + dv.getInt16(2, true).toString(16));

}).catch(

function(e) {

HMIRuntime.Trace(`Read file failed with error code ${e}`);

});

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Reading and writing text files (RT Unified)

#### Introduction

This example shows how text files can be read and written with JavaScript.

#### Execution of example

> **Note**
>
> The method HMIRuntime.Trace(text) outputs whether the function was successful via the Tracer.

1. Configure 2 buttons "Button_12" and "Button_13".
2. Create a script for the event "Print" for each button.
3. Copy the sample code below to your project.

#### Writing sample code for text file

//JEx: "Write Text File"

export function Button_12_OnDown(item, x, y, modifiers, trigger) {

HMIRuntime.FileSystem.WriteFile('C:\\Users\\Public\\textfile.txt', 'my utf8 string', 'utf8').then(

function() {

HMIRuntime.Trace('Write file finished successfully');

}).catch(function(errorCode) {

HMIRuntime.Trace('Write failed errorcode=' + errorCode);

});

}

#### Reading sample code for text file

//JEx: "Read Text File"

export function Button_13_OnDown(item, x, y, modifiers, trigger) {

HMIRuntime.FileSystem.ReadFile('C:\\Users\\Public\\textfile.txt', 'utf8').then(

function(text) {

HMIRuntime.Trace('Text=' + text);

}).catch(function(errorCode) {

HMIRuntime.Trace('Read failed errorcode=' + errorCode);

});

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Setting bits (RT Unified)

#### Introduction

The example shows how single and multiple bits are masked and set with JavaScript.

> **Note**
>
> **Using different methods for integer data types**
>
> The methods of the "`Math.Uint64`" object and the standard model are available for setting and resetting multiple bits.
>
> The methods of the "`Math.Uint64`" object work with all integer data types.
>
> - For values < 2<sup>31</sup> use the standard methods of JavaScript.
> - For values ≥ 2<sup>31</sup> use `BigInt` of the standard model or the methods of the `Math.Uint64` object.
>
> `BigInt` of the standard model is used in the following examples.

#### Executing an example

1. Create 6 buttons in a project.
2. Create a tag of the "Int" type.
3. For all 6 buttons create local scripts for the event "Left mouse button pressed".
4. Transfer the source code for the examples to the respective script areas.
5. To retain a clear overview assign descriptive texts to the buttons.

#### Setting a single bit (no error handling)

The "`Tag.SetBit()`" and "`Tag.ResetBit()`" methods are available for setting and resetting single bits.

//JEx: "SetSingleBit"

//SOM_OM_"

//TagsRequired: "HMI_Tag_1"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

Tags('HMI_Tag_1').SetBit(37);

}

#### Setting a single bit

When error handling is included, a corresponding message is output with the `HMIRuntime.Trace()` method.

//JEx: "SetSingleBitWithErrorHandling"

//SOM_OM_"

//TagsRequired: "HMI_Tag_1"

export function Button_5_OnTapped(item, x, y, modifiers, trigger) {

const tag1 = Tags('HMI_Tag_1');

const bitNum = 37;

tag1.SetBit(bitNum).then(() => {HMIRuntime.Trace('SetBit succeeded');})

.catch((e) => {HMIRuntime.Trace(`SetBit failed, error=${e}`);});

}

#### Changing bits with "Xor" without error handling

Changing multiple bits with 64 bits without error handling.

Copy code

//JEx: "SetMultipleBits"

//SOM_OM_"

//TagsRequired: "HMI_Tag_1"

export function Button_6_OnTapped(item, x, y, modifiers, trigger) {

    const tag1 = Tags('HMI_Tag_1');

    // Define a 64-bit mask using a binary constant

    const mask = 0b0110011000000000000000000000000000001n;

    // Read LWord Tag

    tag1.Read();

    let newValue = BigInt(tag1.Value);

    newValue ^= mask; // use Bit-operations for clearing / setting bits

    tag1.Write(newValue);

}

#### Setting bits with "Or"

The function sets every bit in the mask that has the value "1".

The example uses asynchronous writing and includes an extended error handling.

//JEx: "SetMultipleBitsWithErrorHandlingOr"

//TagsRequired: "HMI_Tag_1"

// set bits with 'Or': sets every bit which is '1' in mask

export function Button_16_OnTapped(item, x, y, modifiers, trigger) {

const tag1 = Tags('HMI_Tag_1');

const mask = 0b0110011000000000000000000000000000001n;

tag1.Read();

if(tag1.LastError != 0) {

HMIRuntime.Trace(`Read failed, error=${tag1.LastError}`);

} else if((tag1.QualityCode & 0x80) == 0) {

// Check whether QC is 'good' or 'good cascade'

HMIRuntime.Trace(

`Read succeeded, but Quality is not 'good', QC=${tag1.QualityCode}`

);

} else {

let newValue = BigInt(tag1.Value);

newValue |= mask; // Set bits

const ts = Tags.CreateTagSet([[tag1.Name, newValue]]);

ts.WriteAsync().then(()=>{HMIRuntime.Trace('Write succeeded')})

.catch((e)=>{HMIRuntime.Trace(`Write failed, error=${e}`)});

}

}

#### Deleting bits with "AND"

The script deletes each masked bit with the value "1".

//JEx: "ClearMultipleBitsWithErrorHandlingAnd"

//TagsRequired: "HMI_Tag_1"

export function Button_17_OnTapped(item, x, y, modifiers, trigger) {

const tag1 = Tags('HMI_Tag_1');

let mask = 0b0110011000000000000000000000000000001n;

// invert all bit of mask for 'And' operation

mask ^= 0xffffffffffffffffn;

tag1.Read();

if(tag1.LastError != 0) {

HMIRuntime.Trace(`Read failed, error=${tag1.LastError}`);

} else if((tag1.QualityCode & 0x80) == 0) {

// Check whether QC is 'good' or 'good cascade'

HMIRuntime.Trace(

`Read succeeded, but Quality is not 'good', QC=${tag1.QualityCode}`

);

} else {

let newValue = BigInt(tag1.Value);

newValue &= mask; // Delete bits

const ts = Tags.CreateTagSet([[tag1.Name, newValue]]);

ts.WriteAsync().then(()=>{HMIRuntime.Trace('Write succeeded')})

.catch((e)=>{HMIRuntime.Trace(`Write failed, error=${e}`)});

}

}

#### Replacing bits with "Xor"

The script replaces each bit in the mask that has the value "1".

//JEx: "FlipMultipleBitsWithErrorHandlingXor"

//TagsRequired: "HMI_Tag_1"

export function Button_12_OnTapped(item, x, y, modifiers, trigger) {

const tag1 = Tags('HMI_Tag_1');

const mask = 0b0110011000000000000000000000000000001n;

tag1.Read();

if(tag1.LastError != 0) {

HMIRuntime.Trace(`Read failed, error=${tag1.LastError}`);

} else if((tag1.QualityCode & 0x80) == 0) {

// Check whether QC is 'good' or 'good cascade'

HMIRuntime.Trace(

`Read succeeded, but Quality is not 'good', QC=${tag1.QualityCode}`

);

} else {

let newValue = BigInt(tag1.Value);

newValue ^=mask;

const ts = Tags.CreateTagSet([[tag1.Name, newValue]]);

ts.WriteAsync().then(()=>{HMIRuntime.Trace('Write succeeded')})

.catch((e)=>{HMIRuntime.Trace(`Write failed, error=${e}`)});

}

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Changing the date format (RT Unified)

#### Introduction

The example shows how the date format is changed using JavaScript.

#### Executing an example

1. Create 2 I/O fields and 1 button.
2. Configure 2 global tags:

   - HMI_Tag_1 of the type "Int"
   - HMI_Tag_2 of the type "WString"
3. Create a script for the event "Press" of the button "Button_1".

#### Sample code

//JEx: "ChangeDateformat"

//SOM_OM_"HmiIOField_1", SOM_OM"HmiIOField_2"

//TagsRequired: "HMI_Tag_1:Int","HMI_Tag_2:WString"

export function Button_1_OnDown(item, x, y, modifiers, trigger) {

//Create array with all month names

var monthNames = [

"January", "February", "March",

"April", "May", "June", "July",

"August", "September", "October",

"November", "December"

];

var date = new Date(); //Create tag with current date

var day = date.getDate(); //Separation of the individual date components

var monthIndex = date.getMonth();

var year = date.getFullYear();

var month = monthIndex + 1;

//The "getMonth()" object contains 12 values from "0" to "11".

//Set the date format

switch (Tags("HMI_Tag_1").Read()) {

case 1: Tags("HMI_Tag_2").Write(day +'/' +month +'/' +year); break;

case 2: Tags("HMI_Tag_2").Write(year +'-'  +month+ '-' +day); break;

case 3:

Tags("HMI_Tag_2").Write(year +'-'  +monthNames[monthIndex] + '-' +day);

break;

default:

Tags("HMI_Tag_2").Write(day + ' ' + monthNames[monthIndex] + ' ' + year);

break;

}

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Monitoring alarms (RT Unified)

#### Introduction

This example shows how to create and monitor active alarms.

The reason (NotificationReason) for which the alarms were sent can have the following values:

- `Unknown` (1)
- `Add` (1)

  The alarm was added to the filtered result list. The alarm meets the filter criteria that apply to the monitoring, for example "State = 1".
- `Modify` (2)

  Properties of the alarm were changed, but the alarm is still part of the filtered result list.
- `Remove` (3)

  The alarm was part of the result list, but it no longer meets the filter criteria due to changes to its properties.

  > **Note**
  >
  > Changes to the alarm will not result in notifications until the alarm meets the filter criteria again, such as "State = 1". In this case, "NotificationReason" is set to `Add`.

**State-based and event-based monitoring**

The respective client application determines whether or not notifications of alarms with the "NotificationReason" `Modify` or `Remove` are ignored.

For example:

- State-based monitoring: A customer wants to create a list of incoming alarms. All notification reasons are relevant. The client removes an alarm from the list as soon as the notification reason is `Remove`.
- Event-based monitoring: If an alarm is received, an email should be sent. Only the notification reason `Add` is relevant.

#### Execution of example

1. Configure a button (in the example "Button_1") on a screen.
2. Create a script for the event "Click left mouse button".

   The JavaScript editor creates the function "`Button_1_OnTapped(item, x, y, modifiers, trigger)`".
3. Insert the example code.
4. Compile and load it in Runtime.
5. Trigger the event "Click left mouse button" on the button.

#### Result

| 1. A customer begins monitoring with the filter criterion "State = 1". 2. An alarm is triggered. Runtime notifies the customer of the "NotificationReason" as follows:       | NotificationReason | Description |    | --- | --- |    | Add | "State" is 1 The alarm has arrived. |    | Modify | "State" property has not changed.  Another property that is not part of the filter criterion has changed, e.g. "Priority". |    | Remove | "State" has changed. The alarm is removed. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Sample code

//JEx: "A client starts an alarm subscription with filter criterion “State = 1” (Raised alarms)."

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

var subs = HMIRuntime.Alarming.CreateSubscription();

subs.Filter = 'State=1';

subs.Language = 1033;

subs.OnAlarm = function(Errorcode, SystemNames, ResultSet) {

  for (let index in ResultSet)

  {

    HMIRuntime.Trace('Alarm Name_' + (index+1) + ' = ' + ResultSet[index].Name);

    HMIRuntime.Trace(' Alarm State_' + (index+1) + '= ' + ResultSet[index].State);

    HMIRuntime.Trace(' Notification Reason_' + (index+1) + '= ' + ResultSet[index].NotificationReason);

  }

}

subs.Start();

}

### Set alarm filter (RT Unified)

#### Introduction

The example shows how the alarm filter is set by a JavaScript function.

To make the examples easy, the filters are set by pressing a button.

Classic application example: Setting alarm filters using check boxes on a screen page.

#### Executing an example

1. Configure a screen with the following elements:

   - 1 alarm control ("Alarm control_1")
   - 2 buttons (in the example "Button_7" and "Button_8")
2. Configure the generation of alarms of the alarm class "Warning" and "Alarm".
3. Ensure that the alarms in the alarm control "Alarm control_1" are displayed.

#### Filtering sample code for "Warning"

In the sample code, alarms of the alarm class "Warning" are filtered.

//JEx: "Alarm Filter Control with Warnings"

//SOM_OM_"Alarm control" (Alarm control_1);

//JExRequired: "Alarm Subscription"

export function Button_7_OnDown(item, x, y, modifiers, trigger) {

let alarmControl = Screen.FindItem('Alarm control_1');

alarmControl.Filter = "AlarmClassName='Warning'";

}

#### Filtering sample code for "Warning" and "Alarm"

In the sample code, alarms of the alarm class "Warning" and "Alarm" are filtered.

//JEx: "Alarm Filter Control with Warnings and Alarms"

//SOM_ON_"Alarm control" (Alarm control_1);

//JExRequired: "Alarm Subscription"

export function Button_8_OnDown(item, x, y, modifiers, trigger) {

let alarmControl = Screen.FindItem('Alarm control_1');

alarmControl.Filter = "AlarmClassName IN ('Warning','Alarm')";

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Creating an alarm subscription (RT Unified)

#### Introduction

The example shows how an "Alarm subscription" is programmed in JavaScript.

#### Executing an example

1. Configure a task in the Scheduler with the time interval for the update.
2. Create a script for the event "Update" at the configured task.
3. Create the tag "subs" under "Global definition" (compare section "Global definition").
4. Copy the code under "Example code" to the script for the "Update" event.

#### Global definition

//JEx: "AlarmSubscriptionDef"

// A global tag is required for the Alarm Subscription,

// to be able to end the subscription

var subs;

#### Sample code

The JavaScript function in the example is started via the event "Update" of a task in the Scheduler.

//JEx: "AlarmSubsciption"

//JExRequired: "AlarmSubscriptionDef"

//TagsReqired: "HMI_Tag_1_Int"

// Function will be generated when you create a script on event "Update" of a task

export function Task_Task_1_Update() {

let tag = Tags("HMI_Tag_1_Int");

tag.Read();

if(tag.Value == 1) {

    // start subscription

    if(subs) {

// stop already existing subscription

subs.Stop();

subs =  undefined;

    }

    subs = HMIRuntime.Alarming.CreateSubscription();

    subs.Filter = 'AlarmClassName=\'Warning\'';

    //subs.Language = 1033; // For explicit setting of a specific language

    subs.OnAlarm = function(Errorcode, SystemNames, ResultSet) {

// Callback function is performed as soon as the alarm attribute changes

for (let index in ResultSet) {

        HMIRuntime.Trace('Alarm[' + index + '] Name="' + ResultSet[index].Name + '"');

        HMIRuntime.Trace('Alarm[' + index + '] State="' + ResultSet[index].State + '"');

        HMIRuntime.Trace('Alarm[' + index + '] EventText="' + ResultSet[index].EventText + '"');

}

    }

    subs.Start();

} else if(tag.Value == 2) {

    // stop subscription

    if(subs) {

// Stop already existing Alarm Subscription

      subs.Stop();

      subs = undefined;

}

}

}

---

**See also**

[Notes on the code examples (RT Unified)](#notes-on-the-code-examples-rt-unified)

### Creating alarms with multilingual alarm texts (RT Unified)

#### Introduction

The example shows how you transfer multilingual alarm text to the system function "CreateSystemAlarm" using text lists.

In the first sample code, you are using a text list entry in the "AlarmText" parameter. In this entry, you refer to the "AlarmParameterValue1" parameter.

In the second sample code, you are also using a text list entry in the "AlarmText" parameter. In this entry, you refer to an additional text list.

This example can be transferred to the system functions "CreateSystemInformation" and "CreateOperatorInputInformation".

The system functions "CreateSystemInformation", "CreateSystemAlarm" and "CreateOperatorInputInformation" have the following parameters:

- "AlarmText": Specifies the alarm text.

  You have the option of establishing references to the parameter values.
- "Area" (optional): Specifies the scope.
- "AlarmParameterValue1" to "AlarmParameterValue7" (optional): Specifies the alarm parameters.

> **Note**
>
> **Include reference in alarm text**
>
> References to "AlarmParameterValue1" to "AlarmParameterValue7" are not implemented directly in the "AlarmText" parameter of the system functions, e.g. "Alarm text: @1%s@". Use references in referenced text lists and access the list entries in the "AlarmText" parameter.

| ![Introduction](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for working efficiently |
| --- | --- |
| You can find the following snippets for the system function "CreateSystemInformation" in the shortcut menu of the "Scripts" editor under "Snippets > HMI Runtime > Alarming":  - "CreateSystemInformation with monolingual Alarm Text" - "CreateSystemInformation with multilingual Alarm Text and Parameter Value" - "CreateSystemInformation with multilingual Alarm Text and embedded Text List" |  |

#### Executing an example

1. Create multiple project languages. One of the languages is English.
2. Activate the desired project languages in the Runtime settings of the HMI device under "Language & Font".
3. Create a text list "Text_list_3" of the type "Value/Area".
4. Create an entry in the text list.
5. Set the value to "1".
6. Specify the English text: "Parameter value 1: @1%s@".  
   "Parameter value 1 :" can be displayed in multiple languages.  
   "@1%s@" is the reference to the parameter "AlarmParameterValue1". "1" indicates the number and "s" the data type. The data type is String.
7. You can define the text for additional languages under "Properties > Texts" in the Inspector window.
8. Create a text list "Text_list_1" of the type "Value/Area".
9. Create an entry in the text list.
10. Set the value to "1".
11. Specify the text for all required languages: "@1%t#2T@".  
    "@1%t#2T@" is the reference to the parameters "alarmParameterValue1" and "alarmParameterValue2".   
    The name of the text list is transferred in "AlarmParameterValue2".  
    The value of the text list entry is transferred in "AlarmParameterValue1".
12. Create a text list "Text_list_2" of the type "Value/Area".
13. Create an entry in the text list.
14. Set the value to "1".
15. Specify the English text: "MyText".
16. You can define the text for additional languages under "Properties > Texts" in the Inspector window.
17. Configuring the buttons "Button_1" and "Button_2".
18. Configure an alarm control.
19. Configure the alarm control so that current alarms of the alarm class "SystemAlarm" are displayed.
20. Create a script for the event "Click left mouse button" at each of the buttons.
21. Add the respective sample code.
22. Configure buttons for switching the language.
23. Compile and load the project.
24. Trigger the events at the buttons.

#### Result

**"Button_1"**

- When the runtime language "English" is active, the alarm of the alarm class "SystemAlarm" is displayed as follows in the alarm control:

  - The area is "MyArea".
  - The alarm text is "Parameter value 1: My Parameter Value 1".

    The alarm text comes from the entry of the text list "Text_list_3".
- When you switch the language in runtime, the language-dependent alarm text is displayed. "My Parameter Value 1" is language-neutral.

**"Button_2"**

- When the runtime language "English" is active, the alarm of the alarm class "SystemAlarm" is displayed as follows in the alarm control:

  - The area is "MyArea".
  - The alarm text is "MyText".

    The alarm text comes from the entry of the text list "Text_list_2".
- If you switch the language in runtime, the language-dependent alarm text is displayed.

#### Example codes

**"Button_1"**

`//JEx: "CreateSystemAlarm with multilingual Alarm Text and Parameter Value"`

`//TextListsRequired: "Text_list_3"`

`//EntryRequired: value: "1", Text: "Parameter value 1: @1%s@"`

`export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`
  
`let value = 1;`

`HMIRuntime.Alarming.SysFct.CreateSystemAlarm(`
  
`HMIRuntime.Resources.TextLists("Text_list_3").Item(value), "MyArea", "My Parameter Value 1");`

`}`

**"Button_2"**

`//JEx: "CreateSystemAlarm with multilingual Alarm Text and Parameter Value"`

`//TextListsRequired: "Text_list_1", "Text_list_2"`

`//Text_list_1: value: "1", Text: "@1%t#2T@"`

`//Text_list_2: value: "1", Text: "MyText"`

`export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`
  
`let value = 1;`

`HMIRuntime.Alarming.SysFct.CreateSystemAlarm(`

`HMIRuntime.Resources.TextLists("Text_list_1").Item(value),`

`"MyArea", 1, HMIRuntime.Resources.TextLists("Text_list_2"));`

`}`

---

**See also**

[CreateOperatorInputInformation (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#createoperatorinputinformation-rt-unified)
  
[CreateSystemAlarm (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#createsystemalarm-rt-unified)
  
[CreateSystemInformation (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#createsysteminformation-rt-unified)

### Opening and closing a screen in a pop-up window (RT Unified)

#### Introduction

The example shows you how to open and close a screen in a pop-up window. To do this, you use the system functions "OpenScreenInPopup" and "ClosePopup".

#### OpenScreenInPopup

The system function "OpenScreenInPopup" has the following parameters:

- "popupWindowName": Specifies the name of the pop-up window.

  The name must be unique within the parent screen.
- "screenName": Specifies the name of the screen that is opened in the pop-up window.
- "toggleOpen": Indicates whether the pop-up window is closed when the function is called again.
- "Caption": Specifies the title of the pop-up window.
- "Left": Defines the window position as offset from the left margin.
- "Top": Defines the window position as offset from the top margin.
- "hideCloseButton": Specifies whether to display the "Close" button.
- "parentScreenPath" (optional): Path of the parent screen. With this parameter you specify whether the popup window closes when a screen change is executed in the screen or screen window.

  You can specify the path absolute or relative:

  - Absolute path of the parent screen: "~/Screen"
  - Relative path of the parent screen: "./Screen"
  - Absolute path of the parent screen in a screen window: e.g. "~/Screen window_1/Screen"

    "Screen window_1" is the name of the screen window.
  - Relative path of the parent screen in a screen window: e.g. "./Screen window_1/Screen"

    "Screen window_1" is the name of the screen window.

  Relative path information is used in the following sample codes.

#### ClosePopup

The system function "ClosePopup" has the parameter "popupWindowPath". The parameter specifies the path of the pop-up window to be closed.

The "popupWindowPath" value is the result of the parameters "popupWindowName" and "parentScreenPath" of the system function "OpenScreenInPopup".

The parameter "popupWindowPath" is specified accordingly as relative or absolute path:

- Absolute path of the popup window: e.g. "~/MyPopup"

  "MyPopup" is the name of the popup window.
- Relative path of the popup window: e.g. "./MyPopup"

  "MyPopup" is the name of the popup window.
- Absolute path of the popup window with screen window: "~/Screen window_1/MyPopup"

  "MyPopup" is the name of the popup window and "Screen window_1" is the name of the screen window.
- Relative path of the popup windows with screen window: "./Screen window_1/MyPopup"

  "MyPopup" is the name of the popup window and "Screen window_1" is the name of the screen window.

> **Note**
>
> When the "parentScreenPath" parameter of the system function "OpenScreenInPopup" is not defined, the parameter is "popupWindowPath", for example, "/MyPopup". "MyPopup" is the name of the popup window.

#### Executing an example

1. Configure five screens: "Screen_1", "Screen_2", "Screen_3", "Screen_4" and "Screen_5".
2. Configure the following objects in the screen "Screen_1":

   - Five buttons: "Button_1", "Button_2", "Button_3", "Button_4" and "Button_5"
   - One screen window "Screen window_1"
3. Configure a screen change to "Screen_5" at the button "Button_5".
4. Add a button in "Screen_5" that triggers a screen change to "Screen_1".
5. Add a button in "Screen_3" that triggers a screen change to "Screen_4".
6. Add a button in "Screen_4" that triggers a screen change to "Screen_3".
7. Select "Screen_3" for the "Screen" property of the screen window.
8. Create a script for the event "Click left mouse button" at the buttons "Button_1", "Button_2", "Button_3" and "Button_4".
9. Add the respective sample code.
10. Compile and load the project.
11. Trigger the events at the buttons.

#### Result

- "Button_1":

  - "Screen_2" is opened in the pop-up window.
  - The pop-up window is closed when you change the screen by clicking "Button_5".
- "Button_2":

  - The pop-up window that was opened with "Button_1" is closed.
- "Button_3":

  - "Screen_2" is opened in the pop-up window.
  - When you change the screen in the screen window, the pop-up window is closed.
- "Button_4":

  - The pop-up window that was opened with "Button_3" is closed.

#### Sample code "Button_1"

//JEx: "OpenScreenInPopup with linked parentScreen"

export async function Button_1_OnTapped(item, x, y, modifiers, trigger) {

HMIRuntime.UI.SysFct.OpenScreenInPopup("MyPopup", "Screen_2", true, "Popup", 100, 100, false, "./Screen");

}

#### Sample code "Button_2"

//JEx: "ClosePopup with linked parent screen"

export async function Button_2_OnTapped(item, x, y, modifiers, trigger) {

HMIRuntime.UI.SysFct.ClosePopup("./MyPopup");

}

#### Sample code "Button_3"

//JEx: "OpenScreenInPopup with linked parent screen in screen window"

//SOM_OM_"hmiScreenWindowInterface"

export async function Button_3_OnTapped(item, x, y, modifiers, trigger) {

HMIRuntime.UI.SysFct.OpenScreenInPopup("MyPopup", "Screen_2", true, "Popup", 100, 100, false, "./Screen window_1/Screen");

}

#### Sample code "Button_4"

//JEx: "ClosePopup with linked parent screen in screen window"

//SOM_OM_"hmiScreenWindowInterface"

export async function Button_4_OnTapped(item, x, y, modifiers, trigger) {

HMIRuntime.UI.SysFct.ClosePopup("./Screen window_1/MyPopup");

}

---

**See also**

[ClosePopup (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#closepopup-rt-unified)
  
[OpenScreenInPopup (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#openscreeninpopup-rt-unified)

### Triggering a screen change with a tag (RT Unified)

#### Introduction

The example shows how you can trigger a screen change in a screen window using a tag. In the example, the tag value is changed by clicking on the buttons.

Application example: The system contains a motor that is controlled with a PLC. As soon as the motor displays a fault, a detailed view of the motor is displayed on the HMI device.

#### Executing an example

1. Configure three screens: "Screen_Motor", "Screen_Error" and "Screen_NoError".
2. Define different background colors for the screens "Screen_Error" and "Screen_NoError".
3. Create the tag "PLC_State_Tag" of the data type "Int".
4. Configure the following objects in the screen "Screen_Motor":

   - Two buttons, "Error" and "NoError"
   - One screen window
5. At the "Error" button configure the system function "SetTagValue" for the event "Click left mouse button":

   - Tag: "PLC_State_Tag"
   - Value: "1" (data type "Int")
6. At the "NoError" button configure the system function "SetTagValue" for the event "Click left mouse button":

   - Tag: "PLC_State_Tag"
   - Value: "0" (data type "Int")
7. Select the screen window.
8. Under "Properties > Properties > General" in the Inspector window, select the "Screen" property.
9. In the "Dynamization" column, select the "Script" option.
10. Add a trigger.
11. Select "PLC_State_Tag" as the trigger tag.
12. Insert the sample code.
13. Compile and load the project.
14. Trigger the events at the buttons.

#### Result

- The screen window shows the screen "Screen_Error" by default.
- When you click the "Error" button, the screen in the screen window changes to "Screen_Error".
- When you click the "NoError" button, the screen in the screen window changes to "Screen_NoError".

#### Sample code

`//JEx: "ActivateScreenByNumber"`

//TagsRequired: "PLC_State_Tag"

`//SOM_OM_"HMIScreenWindowInterface"`

`export function Screen_window_1_Screen_Trigger(item) {`

`let screenName;`

`// Read the state tag first which is the same as the trigger tag`

`let tag1 = Tags("PLC_State_Tag");`

`let value1 = tag1.Read();`

`// Convert state to screen name`

`switch(value1)`

`{`

`case 0: screenName = "Screen_NoError";`

`break;`

`case 1: screenName = "Screen_Error";`

`break;`

`default: screenName = "Screen_NoError";`

`break;`

`}`

`return screenName;`

`}`

### Connecting Unified Comfort Panel with SQL database (RT Unified)

#### Introduction

You can access MS SQL databases and SQLite databases via JavaScript functions from the Unified Comfort Panel. Note that the resource utilization is directly proportional to the number of the requests to the database and the size of the data to be read or written. This means that frequent access to databases can also affect the performance in Runtime.

The following database options are available for Unified Comfort Panels:

- Microsoft SQL with the driver:

  | ODBC driver name | Description |
  | --- | --- |
  | {ODBC Driver 17 for SQL Server} | Microsoft ODBC driver for SQL Server version 17.9  Included in this version are: - Azure SQL Database - Azure Synapse Analytics - Azure SQL Managed Instance - SQL Server 2019 - SQL Server 2017 - SQL Server 2016 - SQL Server 2014 - SQL Server 2012 |
- SQLite with the driver:

  | ODBC driver name | Description |
  | --- | --- |
  | {SQLITE3} | SQLite3 ODBC driver |

To create a connection to the database with the "CreateConnection" method, a "connectionString" parameter of type "String" is transferred. The "connectionString" parameter has the form:

| Symbol | Meaning |
| --- | --- |
| MS SQL | `let connectionstring = "DRIVER={ODBC Driver 17 for SQL Server}; DATABASE=UCP; UID=userid; PWD=password; trusted_connection=no; SERVER=ipaddress,port_number;";`   Example: `let connectionstring = "DRIVER={ODBC Driver 17 for SQL Server}; DATABASE=UCP; UID=TestUser; PWD=test; trusted_connection=no; SERVER=192.168.0.115,1433;";` |
| SQLite | `let connectionstring = "Driver={SQLite3}; Database=PathToDatabase; trusted_connection=yes;";`   Example: `let connectionstring = "Driver={SQLite3}; Database=/media/simatic/X51/MyUCP.db; trusted_connection=yes;";` |

#### Example

The example shows how you can use a button to establish a connection between a Unified Comfort Panel and an SQL server. You create a table there and then close the connection to the server.

1. Configure a button.
2. Specify "Click right mouse button" as event.
3. Convert the event into a script.
4. Insert the sample code into the script.

#### Result

By clicking the button you establish a connection with an MS SQL database. You create a table and close the connection again.

#### Sample code

`//JEx: "CreateConnection"`

`//SOM_OM_"HMIDatabaseConnection"`

`(async function() {`

`try{`

`HMIRuntime.Trace("Open MS SQL DB");`

`let connectionstring = "DRIVER={ODBC Driver 17 for SQL Server}; DATABASE=UCP; UID=TestUser; PWD=test; trusted_connection=no; SERVER=192.168.0.115,1433;";`

`let conn = await HMIRuntime.Database.CreateConnection(connectionstring);`

`let query = "Create Table TableMotorData (Name varchar(50), ID char, Temp float);";`

`let results = await conn.Execute(query);`

`conn.Close();`

`HMIRuntime.Trace("Close MS SQL DB");`

`}`

`catch(e)`

`{`

`let res = e.Results;`

`for(let statement in res)`

`{`

`let errors = res[statement].Errors;`

`for (let i in errors)`

`{`

`let detailed = errors[i];`

`HMIRuntime.Trace("Errors state : " + detailed.State);`

`HMIRuntime.Trace("Errors Message : " + detailed.Message);`

`}`

`}`

`}`

`})();`

## Troubleshooting (RT Unified)

This section contains information on the following topics:

- [RTIL Trace Viewer (RT Unified)](#rtil-trace-viewer-rt-unified)
- [Integrate RTIL Trace Viewer as an external application (RT Unified)](#integrate-rtil-trace-viewer-as-an-external-application-rt-unified)
- [Tracing with the RTIL Trace Viewer (RT Unified)](#tracing-with-the-rtil-trace-viewer-rt-unified)

### RTIL Trace Viewer (RT Unified)

#### Core statement

The RTIL Trace Viewer is a separate application which runs independently of the TIA Portal, but which can be integrated into the TIA Portal as an "external application".

#### Principle

During runtime, the RTIL Trace Viewer displays all alarms which are listed in the configurable TraceCatalog.

**Layout**

The traces are displayed in tabular form and can be sorted in ascending and descending order by the columns displayed.

**Filters**

The required alarms can be filtered using filters. Alarms in non-selected categories are hidden.

**File functions**

You export alarms as trace logs in the following formats:

- Text file (.txt, .log): Loading and evaluation in the RTIL Trace Viewer
- .csv file: Evaluation in conventional spreadsheet programs or other csv-compatible applications

---

**See also**

[Support for errors (RT Unified)](#support-for-errors-rt-unified)

### Integrate RTIL Trace Viewer as an external application (RT Unified)

#### Procedure

1. Open the settings via "Tools > Settings".
2. Open the category "External applications".
3. Double-click in the first empty line.

   An input mask for the external application opens.
4. Assign a descriptive name for the application, e.g. "RTIL Trace Viewer" in the field "Name".
5. Insert the following path under "Command": `%ProgramFiles%\Siemens\Automation\WinCCUnified\bin\RTILtraceViewer.exe`
6. Leave the fields "Arguments" and "Start in" empty.
7. Click "Add" and then close the "Settings" dialog.

The application is now available via the menu "Tools > External applications".

### Tracing with the RTIL Trace Viewer (RT Unified)

There is a "Trace Viewer" for finding errors in the JavaScript code.

#### Preparation

The "Trace Viewer" are located in the following path:

- %ProgramFiles%\Siemens\Automation\WinCCUnified\bin\RTILtraceViewer.exe

#### Requirement

- Simulation or runtime are started.
- RTILtraceViewer.exe has been started.

#### Procedure

1. Carry out an action in the simulation which starts a JavaScript function.
2. Filter by the trace messages "Subsystem > ScriptFW".
3. Define additional filter criteria if required.
4. Evaluate trace messages if actions in the simulation lead to errors.

**Note**

As long as no JavaScript function was executed in the simulation during the runtime of the Trace Viewer, the entry "ScriptFW" is missing in the "Filter > Subsystem" menu.

**Note**

If no messages are displayed in the Trace Viewer despite errors in the simulation, reset the filters:

- Only in the submenu, e.g. "Subsystem": "Filter > Subsystem > Clear filter" menu
- All filters: "Filter > Clear all filters" menu

![Procedure](images/112795519371_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Integrate RTIL Trace Viewer as an external application (RT Unified)](#integrate-rtil-trace-viewer-as-an-external-application-rt-unified)

## Debugging scripts (RT Unified)

This section contains information on the following topics:

- [Basics of debugging (RT Unified)](#basics-of-debugging-rt-unified)
- [Design and function of the debugger (RT Unified)](#design-and-function-of-the-debugger-rt-unified)
- [Enabling the debugger (RT Unified)](#enabling-the-debugger-rt-unified)
- [Starting the debugger (RT Unified)](#starting-the-debugger-rt-unified)
- [Working with breakpoints (RT Unified)](#working-with-breakpoints-rt-unified)
- [Step-by-step execution of scripts (RT Unified)](#step-by-step-execution-of-scripts-rt-unified)
- [Show values (RT Unified)](#show-values-rt-unified)

### Basics of debugging (RT Unified)

#### Introduction

For example, you can use a debugger to test whether correct values are being transferred to tags and whether abort conditions are being correctly implemented. Check the following in the debugger:

- Source code of functions
- Function sequence
- Values

> **Note**
>
> Your code is displayed in the debugger but is write-protected.

#### Basic procedure

To find an error, check the script with the debugger.

The following options are available for your support:

- Setting breakpoints
- Step-by-step execution
- Viewing values parallel to execution of the script

You do not edit the code of your scripts directly in the debugger. When you find an error, follow these steps:

1. Correct the error in the engineering system.
2. Compile the changed code.
3. Load the runtime.
4. Update the debugger.

---

**See also**

[Starting the debugger (RT Unified)](#starting-the-debugger-rt-unified)

### Design and function of the debugger (RT Unified)

Google Chrome provides the user interface of the debugger. Not all functions of the user interface of the debugger are relevant for debugging WinCC Unified Scripts. Only the functions that are needed to debug scripts in WinCC Unified are explained below.

You can find more information on Chrome DevTools under: <https://developers.google.com/web/tools/chrome-devtools/>.

The debugger is divided into two areas:

- Debugger for screens
- Debugger for jobs

With the debugger for screens you view scripts at screens and screen objects. With the debugger for jobs, you view scripts that you have configured in the Scheduler.

#### Start page of the debugger

After the debugger has been started, its start page is displayed.

The available contents differ depending on the selected area.

On the start page of the debugger for screens you can see two different contexts:

- Dynamizations (e.g. "UMCadmin@192.168.116.144 VCS_1 Dynamics")
- Events (e.g. "UMCadmin@192.168.116.144 VCS_1 Events")

The name of the contexts is composed as follows:

- UMCadmin: User name
- 192.168.116.144: IP address of the computer
- VCS: Name of the graphic component
- _1: Number of the open client
- Events/Dynamics: Scripts at events or dynamizations

> **Note**
>
> A client corresponds to a tab in Google Chrome in which the runtime is open. When you have opened runtime in multiple tabs, multiple clients are used. The client opened first is given the number 1. Numbering is reset when the runtime is restarted.

On the start page of the debugger for jobs you can see the context "JobsExecution".

#### User interface of the debugger

![User interface of the debugger](images/133867069451_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Navigation area |
| ② | Code display area |
| ③ | Console |
| ④ | Debugging area |

#### Navigation area

In the navigation area, the available contents for the screen shown in runtime are displayed in groups. The available groups vary depending on the use of scripts and functions.

**Groups in the debugger for screens**

The debugger for screens can contain the following groups in the dynamizations context:

- A group for scripts that were configured for dynamizations.
- One group per screen window in which scripts were configured for dynamizations.

The debugger for screens can contain the following groups in the events context:

- A group for scripts that were configured for events.
- One group for functions that were configured for events using the function list.
- One group per screen window in which scripts were configured for events.
- One group per screen window in which functions were configured for events using the function list.

**Groups in the debugger for jobs**

The debugger for jobs can contain the following groups:

- A group for scripts that were configured for tasks.
- One group for functions that were configured for tasks using the function list.

#### Code display area

Your code is displayed in the code display area. The rows are numbered.

#### Debugging area

The debugging area offers the following relevant options for WinCC Unified:

- Toolbar: Control for executing the script
- "Watch": Display of values
- "Callstack": Display of the current call stack
- "Scope": Available local values ("Local"), functions ("Module") and global values ("Global"),
- "Breakpoints": List of set breakpoints

### Enabling the debugger (RT Unified)

#### Requirement

- SIMATIC Runtime Manager is installed.
- The logged-on user belongs to the Windows user group "SIMATIC HMI".

> **Note**
>
> The debugger is only available locally.
>
> Remote access from the debugger to other devices is not possible.

#### Procedure

The debugger is disabled by default.

> **Note**
>
> The debugger should be disabled in production operation, as using the debugger can endanger system stability and security. Actions can accumulate if the debugger is, for example, at a breakpoint for a long time or the screen is not refreshed.

To enable the debugger, follow these steps:

1. Start the SIMATIC Runtime Manager application.
2. Click the ![Procedure](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
3. Switch to the "Scripts Debugger" tab.
4. To enable the debugger for screens, select the "Enable" check box in the "Screen debugger" area.
5. To enable the debugger for scheduled tasks, select the "Enable" check box in the "Scheduler debugger" area.
6. Assign an available port number to the debugger for screens (default port number: 9222).
7. Assign an available port number to the debugger for jobs (default port number: 9224).
8. Confirm your entries.

> **Note**
>
> Start Runtime after enabling the debugger.

### Starting the debugger (RT Unified)

#### Requirement

- Google Chrome (as of version 70) is installed.
- A project is opened in runtime.
- The debugger was activated in SIMATIC Runtime Manager.

> **Note**
>
> The debugger is only available locally.
>
> Remote access from the debugger to other devices is not possible.

#### Procedure

1. In a new tab, call up the URL chrome://inspect in Google Chrome.
2. The home page of the Chrome DevTools is loaded in the tab.
3. Click "Devices".
4. Select the "Discover network targets" check box.
5. Click "Configure".
6. In the "Target discovery settings" dialog box, enter one of the following strings:

   - `127.0.0.1:`
     `<Port number>`
   - `localhost:`
     `<Port number>`

   Use the port entered for the Script Debugger in SIMATIC Runtime Manager.
7. Press <Enter>.
8. Click "Done".
9. Under "Remote Target", click "inspect" for the desired target.

   The DevTools open in a separate window with the selected target.
10. In the DevTools, select "Sources".

    The debugger is displayed.
11. Click "Toggle screencast".
12. In the navigation area under "Page", select the desired script module.

#### Updating the debugger

The debugger must be updated:

- After starting a new project
- After restarting a running project, for example, because you have reloaded the project in engineering with "Download to device > Software (all)".
- After a screen change in Runtime

The connection to the debugger is lost in each case. Google Chrome therefore shows an error message and asks whether you want to restore the connection.

To restore the connection, proceed as follows:

1. Close the DevTools window.
2. On the DevTools start page under "Remote Target", click "inspect" again for the desired target.

#### Stopping the debugger

Exit the debugger by closing the DevTools window and, if necessary, the DevTools homepage.

This does not stop runtime.

---

**See also**

[Design and function of the debugger (RT Unified)](#design-and-function-of-the-debugger-rt-unified)

### Working with breakpoints (RT Unified)

Set breakpoints to stop the execution of the script at certain points and thus localize errors step-by-step. Previously set breakpoints are still available after updating the debugger.

#### Requirement

- Runtime has started.
- The debugger has been started.
- The group you want to debug is selected.

#### Pause script

To pause the execution of a script, you have 2 options:

- To pause the script immediately, click the ![Pause script](images/153087836939_DV_resource.Stream@PNG-de-DE.png) "Pause script execution" button while the script is being executed.
- Set a breakpoint in the desired line.

  The script pauses when a breakpoint is reached.

To pause a script at a breakpoint that is configured to an event, follow these steps:

1. Set a breakpoint in the script.
2. Trip the respective event in runtime.

   The script pauses at the breakpoint.

#### Setting breakpoints

You have several options to set a breakpoint in a line of the script:

- Click on the line number.
- Right-click the line number and select "Add Breakpoint".

All set breakpoints are displayed in the debugging area under "Breakpoints".

#### Linking breakpoints to conditions

To link a breakpoint to a condition, proceed as follows:

1. Open the shortcut menu of the relevant line.
2. Select the entry "Add conditional breakpoint".

   Execution of the script is stopped at the breakpoint when the condition is fulfilled.

Edit conditions as follows:

1. Open the shortcut menu of the relevant line.
2. Select the entry "Edit breakpoint...".

To prevent the script from pausing at a selected line, proceed as follows:

1. Open the shortcut menu of the respective line.
2. Select the entry "Never pause here".

#### Showing and hiding breakpoints

When you hide a breakpoint, its position is retained. The script then ignores the hidden breakpoint. When you need the breakpoint again, it can simply be shown.

In the debugging area, all breakpoints set in the selected group are displayed under "Breakpoints".

You have several options to show a breakpoint:

- Set the check mark in front of the relevant breakpoint in the debugging area under "Breakpoints".
- Alternatively, right-click the number of the respective line in the code display area and then select "Enable breakpoint".

You have several options to hide a breakpoint:

- Remove the check mark in front of the relevant breakpoint in debugging area under "Breakpoints".
- Alternatively, right-click the number of the respective line in the code display area and then select "Disable breakpoint".

To show or hide all breakpoints, follow these steps:

1. Open the shortcut menu in the debugging area under "Breakpoints".
2. Select "Enable all breakpoints" or "Disable all breakpoints"

#### Enabling and disabling breakpoints

You can enable or disable all breakpoints independent of showing or hiding individual breakpoints.

You have several options to enable or disable all breakpoints:

- Click on the ![Enabling and disabling breakpoints](images/153087832971_DV_resource.Stream@PNG-de-DE.png) "Deactivate breaktpoints" button in the debugging area.
- Open the shortcut menu of a breakpoint in the debugging area and select "Activate breakpoints" or "Deactivate breakpoints".
- Press <Ctrl + F8>.

#### Deleting breakpoints

You have several options to delete a breakpoint:

- Click on the breakpoint in the code display area.
- Open the shortcut menu of the breakpoint in the code display area and select "Remove breakpoint".
- Open the shortcut menu in the debugging area under "Breakpoints" and select "Remove breakpoint"..

To delete breakpoints, the shortcut menu offers the following additional options in the debugging area under "Breakpoints":

- Delete all breakpoints ("Remove all breakpoints​")
- Delete all breakpoints except the selected breakpoint ("Remove other breakpoints​")

### Step-by-step execution of scripts (RT Unified)

#### Introduction

The following options are available to execute your script step-by-step:

- Execute script to the next breakpoint
- Force execution of a script
- Execute script to the next function call
- Jump into a function
- Jump out of a function
- Execute script up to a selected line
- Pause at Exceptions
- Use call stack

#### Requirement

- The group you want to debug is selected.
- The script pauses at a breakpoint.

#### Execute script to the next breakpoint

To pause the continuation of a script, you have several options:

- Click on the ![Execute script to the next breakpoint](images/153085429387_DV_resource.Stream@PNG-de-DE.png) "Resume script execution" button in the debugging area.
- Press the <F8> key.

  The script is executed to the next breakpoint. If there is no other breakpoint, the script is executed completely.

#### Force execution of a script

To ignore the following breakpoints when resuming execution of a paused script, proceed as follows:

1. Click and hold down the ![Force execution of a script](images/153085429387_DV_resource.Stream@PNG-de-DE.png) "Resume script execution" button.

   The ![Force execution of a script](images/153087788555_DV_resource.Stream@PNG-de-DE.png) "Force script execution" button appears.
2. Move the mouse pointer to the ![Force execution of a script](images/153087788555_DV_resource.Stream@PNG-de-DE.png) "Force script execution" button while keeping the mouse button pressed.
3. Now release the mouse button.

   The script is executed to the end.

#### Execute script to the next function call

If a line with a breakpoint contains a function that you are not interested in, you can suppress the debugging of this function:

- Click on the ![Execute script to the next function call](images/153077472907_DV_resource.Stream@PNG-de-DE.png) "Step over next function call" button in the debugging area.
- Press the <F10> key.

  The function is executed without the script pausing within the function.

#### Jumping into a function

If the script pauses in a line containing a function that interests you, you can pause the script in that function:

- Click on the ![Jumping into a function](images/153087792523_DV_resource.Stream@PNG-de-DE.png) "Step into next function call" button in the debugging area.
- Press the <F11> key.

  The script pauses in the first line of the function.

> **Note**
>
> You can only jump into functions that you have defined yourself.

#### Jump out of a function

If the script pauses within a function that you are not interested in, you can suppress further debugging of this function:

- Click on the ![Jump out of a function](images/153087796491_DV_resource.Stream@PNG-de-DE.png) "Step out of current function" button in the debugging area.
- Press the key combination <Shift + F11>.

> **Note**
>
> You can only jump out of a function that you have defined yourself.

#### Execute script up to a selected line

To pause a paused script again at a selected line, proceeds as follows:

1. Right-click the number of the line in the code display area.
2. Select the entry "Continue to here".

   The script pauses at the selected line.

#### Pause at Exceptions

- To pause the script at Exceptions, click on the ![Pause at Exceptions](images/153087800459_DV_resource.Stream@PNG-de-DE.png) "Pause on exceptions" button in the debugging area.

#### Use call stack

- To jump into a function of the call stack, click on the corresponding entry under "Call Stack".

> **Note**
>
> You can only jump into functions that you have defined yourself.

### Show values (RT Unified)

#### Introduction

To identify errors in your script efficiently, have current values displayed while the script is being executed. This way you can view properties of objects or parameters of functions, for example. You can find additional information on objects and their properties under "WinCC Unified Object Model".

#### Requirements

- The group you want to debug is selected.
- The script pauses at a breakpoint.

#### Procedure

You view values by moving the mouse over the label in the code display area.

You also have the following options to view values:

- In the debugging area under "Scope"
- In the debugging area under "Watch"
- In the console

#### "Scope" area

All local values ("Local"), functions ("Module") and global values ("Global") that are defined at this time are displayed in the "Scope" area.

The values cannot be edited.

#### "Watch" area

In the "Watch" area, you view how values change in the course of a script.

The following buttons are available to you:

- !["Watch" area](images/123343572619_DV_resource.Stream@PNG-de-DE.png) "Add expression": Add a value
- !["Watch" area](images/123343581195_DV_resource.Stream@PNG-de-DE.png) "Refresh": Refresh the "Watch" area
- !["Watch" area](images/123355558027_DV_resource.Stream@PNG-de-DE.png) "Delete watch expression": Delete a value from the "Watch" area. Available when the mouse pointer is located above the respective value.

#### Console

The values available at the current time can be called in the console.

- You show or hide the console with <Esc>.

Call the current values in the console as follows:

1. Enter the name of a local or global value in the console.
2. Press <Enter>.

---

**See also**

[WinCC Unified object model (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#wincc-unified-object-model-rt-unified-1)

## Debugging scripts with Visual Studio Code (RT Unified)

This section contains information on the following topics:

- [Extension for Visual Studio Code (RT Unified)](#extension-for-visual-studio-code-rt-unified)

### Extension for Visual Studio Code (RT Unified)

#### Extension for Visual Studio Code

Some scripting functions are not supported in the "Scripts" editor of the TIA Portal.

Therefore, an extension for Visual Studio Code will be provided in the future.
