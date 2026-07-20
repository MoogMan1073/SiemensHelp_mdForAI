---
title: "Working with system functions and Runtime scripting (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: RTScriptingWCCPenUS
topics: 108
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with system functions and Runtime scripting (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Principles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#principles-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with Function Lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with customized functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-customized-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating customized VB functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-customized-vb-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating user-defined C functions (RT Professional)](#creating-user-defined-c-functions-rt-professional)
- [Protecting user-defined functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#protecting-user-defined-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating local scripts (RT Professional)](#creating-local-scripts-rt-professional)
- [Debugging (Panels, Comfort Panels, RT Advanced, RT Professional)](#debugging-panels-comfort-panels-rt-advanced-rt-professional)
- [Runtime behavior in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-behavior-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#examples-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reference-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Principles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)
- [System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User-defined functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-defined-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Local scripts (RT Professional)](#local-scripts-rt-professional)

### Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Term definition

The following terms are used in the documentation:

| Term |  |
| --- | --- |
| Runtime scripting | Generic term for all activities in user-defined functions and local scripts. |
| Function | Generic term for system functions and user-defined functions. |
| System functions | System functions are all functions supplied with WinCC. The system functions are used either in function lists, user-defined functions or local scripts. |
| User-defined functions | User-defined functions are functions written in the "Scripts" editor. For more precise specification, the term "User-defined VB function" and "User-defined C function" is used in the documentation. |
| Local script | A local script is created directly at the point of use, e.g. an object property, and has a cyclic or acyclic trigger. For more precise specification, the terms "local VB script" and "local C script" are used in the documentation. |
| VBS/VBScript | Abbreviation for Visual Basic Script |

#### Availability

|  | WinCC RT Advanced and Panels | WinCC RT Professional |
| --- | --- | --- |
| Customized VB functions | X | X |
| Customized C functions | -- | X |
| Local VB scripts | -- | X |
| Local C scripts | -- | X |

#### Applying Runtime scripting

The following figure serves as a decision guide for programming tasks at hand:

![Applying Runtime scripting](images/36119231755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| * | Local scripts are not supported in WinCC RT Advanced and Panels. |

#### Customized function or local script?

Whether you accomplish your programming task with a user-defined function or a local script depends on the application purpose and ultimately on the number of user-defined functions or local scripts.

Use local scripts for background activities, e.g. for daily printing or logs, for the monitoring of tags or for the execution of calculations.

Use customized functions to make codes available in several places in your project but only create them once. Instead of entering the code several times, you just call the appropriate customized function. Your code is clearer and easier to maintain.

![Customized function or local script?](images/36119243659_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Access to HMI tags (Panels, Comfort Panels, RT Advanced, RT Professional)](#access-to-hmi-tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[Accessing objects with VBS (Panels, Comfort Panels, RT Advanced, RT Professional)](#accessing-objects-with-vbs-panels-comfort-panels-rt-advanced-rt-professional)
  
[Accessing objects with C (RT Professional)](#accessing-objects-with-c-rt-professional)
  
[Testing the syntax of customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#testing-the-syntax-of-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[User-defined functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-defined-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Local scripts (RT Professional)](#local-scripts-rt-professional)

### System functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Applications

- Function lists

  When the event occurs, the configured system functions can be performed with the function list.
- User-defined functions

  If the HMI device supports user-defined functions, you use system functions in combination with instructions and conditions in the code of the user-defined function. In this way you execute a customized function depending on a specific system state. In addition, you can evaluate return values of system functions, for example. Depending on the return value, you then perform test functions, for example, that in turn affect the function flow.

#### Application examples of system functions

- Calculations, increase tag value by a defined or variable amount.
- Log function, e.g. to start a process value log.
- Settings, e.g. to switch the PLC or set a bit in the PLC.
- Alarms, e.g after a different user logs on.

#### Application

You use system functions in a function list or in a user-defined function.

- Function list

  When configuring a function list, you select the system functions from a selection list that is sorted by categories:

  ![Application](images/51957762443_DV_resource.Stream@PNG-en-US.png)
- User-defined functions

  If you are using a system function in a user-defined function, you choose it from a selection list. To open the selection list, use the key shortcut &lt;Ctrl+Space&gt; or click ![Application](images/36119289355_DV_resource.Stream@PNG-de-DE.png).

  ![Application](images/36119281675_DV_resource.Stream@PNG-de-DE.png)

#### Language dependency

In the function list, the names of the system functions are dependent on the set project language. The functionality can then be recognized immediately by the project planner.

You use the English name of the system function in user-defined functions. You will find the English name of the system function in the reference.

#### Availability for WinCC Runtime Advanced and Panels

Which system functions are available depends on the selected HMI device.

#### HMI device changeover

If you use system functions in a function list that are not available on the set HMI device, these system functions are marked in color.

If you use a system function in a user-defined function which is not available on the set HMI device, a warning is issued. In addition, the respective system function will be underlined with a wavy blue line.

---

**See also**

[System functions for logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-logs-basic-panels-panels-comfort-panels-rt-advanced)

### User-defined functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Applications

You use customized functions for the following for example:

- Configuring a function list

  In a customized function you have the option to have customized functions and system functions executed depending on conditions or executed repeatedly. You then add the user-defined function to a function list, for example.
- Programming new functions

  Customized functions are only valid in the project in which they are defined. For user-defined functions you define transfer parameters and return values, for example, to convert values.

> **Note**
>
> You can only use user-defined functions of a programming language in a function list. Your selection of the first user-defined function determines whether VB functions or C functions can be selected in the function list.

#### Application examples of customized functions

- Convert values

  You use functions to convert values between different measurement units, e.g., temperatures.
- Evaluating tag values statistically
- Drawing a trend in a f(t) trend view

#### Properties of customized functions

A customized function has the following properties:

- Name
- Parameter (optional)
- Return value and type (optional)
- Can be modified centrally
- has no trigger. You have to call the user-defined function explicitly, e.g. in a function list.

#### Organization of customized functions

You create customized functions with the "Scripts" editor. For more information, refer to "["Scripts" editor](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)".

Customized functions are saved in the project. To protect user-defined functions, set up know-how protection. See [Setting up know-how protection](#setting-up-know-how-protection-panels-comfort-panels-rt-advanced-rt-professional) for additional information.

- Project tree

  The user-defined functions are listed in the project tree under "VB scripts" or "C scripts".

  ![Organization of customized functions](images/36119310731_DV_resource.Stream@PNG-en-US.png)
- Function list

  The user-defined functions are listed in a function list under "VB functions" or "C functions".
- User-defined function

  If you are using a system function in a user-defined function, you choose it from a selection list. To open the selection list, use the key shortcut &lt;Ctrl+Space&gt; or click ![Organization of customized functions](images/36119324171_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting up know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-up-know-how-protection-panels-comfort-panels-rt-advanced-rt-professional)
  
["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)

### Local scripts (RT Professional)

#### Applications

You can use local scripts for the following:

- Dynamizing objects

  You use a local script to determine the value of an object property in Runtime. Use this approach, for example, to change the color depending on a tag value.
- Performing tasks at any point in time.

  You use a local script to plan jobs, e.g. daily printout of a log at the end of the shift.

#### Application examples of local scripts

- Configuring desired values for tags for operator control of a graphic object, e.g., in order to assign a value for the PLC via a mouse click.
- Configuring the Runtime language switch for operator control of a graphic object.
- Status monitoring of tags, e.g. to ensure that a value is valid.

#### Properties of local scripts

You create a local script directly at the point of use. A local script has the following properties:

- Predefined name
- Predefined parameters
- Predefined return value (optional)
- Can only be changed at the point of use
- has no trigger
- Calling customized functions, system functions

#### Triggers

Triggers are necessary to execute local scripts in Runtime. The trigger is either determined automatically when creating a local script or specified by the project manager.

The following triggers are supported by WinCC:

- Acyclic triggers, e.g. you plan a one-time stop of Runtime for maintenance work.
- Cyclic triggers, e.g. you plan a job which starts daily printing of a log.
- Events, e.g. when clicking the button.

The following figure shows different types of triggers:

![Triggers](images/36119342987_DV_resource.Stream@PNG-en-US.png)

Triggers are used in the following editors:

- Scheduler

  First you need to configure the trigger in the Scheduler. Then connect the trigger to the local script or a function list.
- Screens

  To dynamize an object property, first configure a local script in the property list of the screen.

  The trigger is determined automatically when creating the local script. You can change the trigger, e.g. to tag trigger.

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)

## Working with Function Lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-the-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Properties of a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#properties-of-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

A function list performs one or more system functions and user-defined functions when the configured event occurs.

#### Principle

The function list is configured for an event of an object, for example, for a screen object or a task. You can configure a function list precisely on every event. The events which are available depend on the selected object and the HMI device.

![Principle](images/51957762443_DV_resource.Stream@PNG-en-US.png)

Events occur only when the project is in Runtime. Events include:

- Execution of a task
- Pressing of a button
- Acknowledging an alarm

  > **Note**
  >
  > The choice of configurable system functions in a function list is dependent on the selected HMI device. For additional information, refer to "Availability for specific devices of system functions".

---

**See also**

[Properties of a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#properties-of-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
ES2RT Event (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Properties of a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Status information

During configuration the project data is tested in the background.

With the following causes the function list is not executed in Runtime and the incorrect entries are marked red:

- At least one system function or one user-defined function is not completely supplied with parameters.
- At least one system function or one user-defined function is contained which is not supported by the selected HMI device, e.g. by changing the device type.

#### Processing of system functions and user-defined functions (WinCC Runtime Advanced and Panels)

A function list is executed from top to bottom in Runtime. If a function list includes system functions with longer runtime, these are processed asynchronously. You can find additional information about this in the sections "[Calling system functions](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)" and "[Calling user-defined functions](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)".

---

**See also**

[Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-the-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You configure a function list by selecting the system functions and customized functions from a drop-down list. The system functions are arranged in the selection list according to categories.

You only use customized functions of a programming language in a function list. Your selection of the first user-defined function determines whether user-defined VB functions or user-defined C functions can be selected in the function list. Which programming languages are available depends on the selected HMI device.

If you have created a user-defined VB function, for example, the user-defined function is available under the entry "VB functions".

#### Requirement

Object has at least one configurable event.

#### Procedure

Proceed as follows to configure a function list:

1. Open the editor in which the object is located.
2. Select the object.
3. Click "Properties &gt; Events" in the Inspector window. Choose the event for which you want to configure the function list.
4. Mark the "&lt;Add function&gt;" entry in the inspector window in the drop-down list.
5. Select the desired system function or the desired user-defined function from the selection list. You can also enter the name of the system function or the user-defined function.

   ![Procedure](images/51957762443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/51957762443_DV_resource.Stream@PNG-en-US.png)

   The system function or the customized function is entered in the function list.
6. If the system function or the customized function has parameters, select the appropriate values for the parameters.

   ![Procedure](images/51958406411_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/51958406411_DV_resource.Stream@PNG-en-US.png)
7. If you want to add other system functions or user-defined functions to the function list, repeat steps 4) to 6).

#### Result

The function list is configured. In addition, to the configured event, the status of the function list is displayed in the Inspector window. When the configured event occurs in Runtime, the function list is completed from top to bottom.

---

**See also**

[Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-the-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Changing the operating mode on the HMI device with the current display (Panels, Comfort Panels, RT Advanced)](#example-changing-the-operating-mode-on-the-hmi-device-with-the-current-display-panels-comfort-panels-rt-advanced)

### Editing a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

A function list can be edited as follows:

- Change the order of system functions and user-defined functions.
- Remove system functions or user-defined functions.

#### Requirement

The function list is configured and opened.

#### Changing the order of a system function or a customized function

1. Select the desired system function or customized function in the function list.
2. Then click the appropriate direction arrow in the inspector window until the system function or customized function is in the desired position.

   ![Changing the order of a system function or a customized function](images/52216991755_DV_resource.Stream@PNG-en-US.png)

   ![Changing the order of a system function or a customized function](images/52216991755_DV_resource.Stream@PNG-en-US.png)

#### Changing the order of several system functions and customized functions

1. Hold down the &lt;Shift&gt; key.
2. Click desired system functions or customized functions one after another with the mouse.
3. Move the selection to the desired position by drag&amp;drop.

#### Removing a system function or customized function

1. Select the desired system function or customized function in the function list.
2. Select "Delete" in the shortcut menu.

---

**See also**

[Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-the-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with customized functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- ["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)
- [Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Access to HMI tags (Panels, Comfort Panels, RT Advanced, RT Professional)](#access-to-hmi-tags-panels-comfort-panels-rt-advanced-rt-professional)
- [Testing the syntax of customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#testing-the-syntax-of-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)

### "Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The "Scripts" editor supports you in the creating of user-defined functions with functionalities such as auto-completion and syntax highlighting. You can insert code templates for frequently used instructions with the "Instructions" task card for example.

![Introduction](images/74962590219_DV_resource.Stream@PNG-en-US.png)

#### Autocompletion and parameter entry

The "Scripts" editor provides you context-dependent programming support with autocompletion parameter entry support.

When you use system functions, the parameters of the function are shown as a tooltip.

#### &lt;Ctrl+J&gt;

The object list can be called context-specifically by using the shortcut &lt;Ctrl+J&gt;. Use the object list to supply values to system functions, methods, and properties: For example, you select screens, screen objects, tags, or colors. You transfer a selected object from the object list into the code by double-clicking it.

> **Note**
>
> Tags and screens can also be inserted using a drag-and-drop operation. Use, for example, drag-and-drop to assign values to parameters.

#### &lt;Ctrl+Space&gt;

With the key combination &lt;Ctrl+Space&gt; you call a list with the following contents:

- Constants and functions of the programming language used in the "Scripts" editor.
- User-defined functions
- System functions

#### Integrating control characters in strings

If you want to use control characters such as tabs or line breaks in strings, use the function "Chr()". Transfer the decimal ASCII code of the required control character as parameter:

Example:

- Chr(9) returns "Tab".
- Chr(15) returns "SI" (Shift in).
- Chr(20) returns "DC4" (Device Control 4).

You will find more detailed information on this VBS function on the [Internet](https://msdn.microsoft.com/en-us/library/ws6aa3sf(v=vs.84).aspx).

#### "Instructions" task card

The "Instructions" task card contains the "Code templates" and "Function list" palettes.

- Code templates

  To insert frequently used instructions, double click the desired instruction in the "Code templates" palette. Replace the space holders with the used expressions.
- Function list

  In the function list you select the system functions and user-defined functions from a drop-down list. Proceed as for configuring a function list. To transfer the function list to the code, click the "Transfer" button. The function list is automatically converted into the correct syntax.

  > **Note**
  >
  > Not all system functions are available in the "Scripts" editor. For additional information, refer to the reference.

#### Edit functions

Use the buttons of the toolbar "Advanced Edit" to make the code more readable by means of indentation and the use of comments.

Bookmarks help you keep an overview, even of many lines of code.

Further information regarding each button can be obtained in the accompanying direct help.

#### Synchronization of tags and objects

If you change tag names or object names in the project which you use in a user-defined function, the names are adapted automatically in the user-defined function.

If you change the tag name or object name in the function, the tag names or object names are not adapted in the project. An appropriate error message is output when executing the user-defined function.

#### Syntax highlighting

Keywords in the "Scripts" editor are highlighted using different colors. Unknown words are underlined with a red wavy line.

The table shows the preset colors for the most important keywords:

| Color | Meaning | Example |
| --- | --- | --- |
| Blue | Keyword | If, Then |
| Dark violet | Function | FahrenheitToCelsius |
| Chocolate | System function | SetTag |
| Orange | HMI tag | Tag_1 |
| Green | Comment | 'This is a comment' |

#### Adapting display properties

When you have opened a user-defined function, you can customize the display properties in the editor. Select the "Options &gt; Settings" menu command. Click "General &gt; Text editors" in the "Settings" editor. For example, you can change the colors for syntax highlighting or adapt the indents for code in the work area.

---

**See also**

[Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Create customized C functions (RT Professional)](#create-customized-c-functions-rt-professional)
  
[Local scripts (RT Professional)](#local-scripts-rt-professional-1)
  
[Editor for local scripts (RT Professional)](#editor-for-local-scripts-rt-professional)

### Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can call system functions in a customized function. The syntax depends on the used programming language. Which programming language is supported depends on the selected HMI device.

You have the following options for calling a system function in a customized function:

- With &lt;Ctrl+Space&gt; or with ![Introduction](images/36119289355_DV_resource.Stream@PNG-de-DE.png)
- Direct input
- With the "Function list" palette

#### With &lt;Ctrl+Space&gt; or with

![With &lt;Ctrl+Space> or with](images/36119289355_DV_resource.Stream@PNG-de-DE.png)

Open the selection list with &lt;Ctrl+Space&gt; and select the desired system function.

#### Direct input

You enter the system functions directly into the code. You use the English name of the system function. You can find the English name of the system function in the system function reference under "Syntax". The editing language setting is not taken into consideration.

References to objects, e.g. screens, connections and logs are transferred in inverted commas:

- Calling system functions without return value in VBS

SetTag "Tag1",64

- Calling system functions with return value in VBS

InverseLinearScaling "Xvalue","Tag1", 0, 1

- Calling system functions without return value in C

SetTag ("Tag1",64);

- Calling system functions with return value in C

InverseLinearScaling ("Xvalue","Tag1", 0, 1);

#### With the "Function list" palette

Select the desired system function from a drop-down list in the "Function list" palette. Proceed as for configuring a function list. You will find further information about this under "Configuring a function list".

To transfer the list to the code, click the "Transfer" button. The list is automatically converted into the correct syntax.

#### HMI device replacement (Runtime Panels and Advanced)

The code of a customized function depends on the selected HMI device. If you use system functions in the customized function which are not supported by the selected HMI device, you receive an error message in the output window.

---

**See also**

[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Executing customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Executing customized C functions (RT Professional)](#executing-customized-c-functions-rt-professional)

### Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can insert user-defined functions of the same programming language in a user-defined function, e.g. only user-defined C functions in a user-defined C function.

The syntax depends on the used programming language. Which programming language is supported depends on the selected HMI device.

You have the following options for calling a customized function in a customized function:

- With &lt;Ctrl+Space&gt; or with ![Introduction](images/36119324171_DV_resource.Stream@PNG-de-DE.png)
- Direct input
- With the "Function list" palette

#### With &lt;Ctrl+Space&gt; or with

![With &lt;Ctrl+Space> or with](images/36119324171_DV_resource.Stream@PNG-de-DE.png)

Open the selection list with &lt;Ctrl+Space&gt; or with ![With &lt;Ctrl+Space> or with](images/36119324171_DV_resource.Stream@PNG-de-DE.png) and select the desired user-defined function.

#### Direct input

You enter the customized function directly into the code. References to objects, e.g. screens, connections and logs are transferred in inverted commas.

#### Calling customized functions without return value in VBS

Average 4,10

#### Calling customized functions with return value in VBS

Dim ValueA

ValueA = Average (4,10)

If you do not want to evaluate the return value, use the call as for a customized function without return value.

#### Calling customized functions without return value in C

Average(4,10);

#### Calling customized functions with return value in C

SetTagDouble("AverageValue",Average (4, 10));

If you do not want to evaluate the return value, use the call as for a customized function without return value.

#### With the "Function list" palette

Select the desired customized function from a drop-down list in the "Function list" palette.

Proceed as for configuring a function list. For more information, refer to "[Configuring a function list](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

To transfer the list to the code, click the "Transfer" button. The list is automatically converted into the correct syntax.

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)
  
[Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Executing customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Executing customized C functions (RT Professional)](#executing-customized-c-functions-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Access to HMI tags (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

With VBS or C you can access the HMI tags which you have created in the project. Change or read the value of an HMI tag with a user-defined function in Runtime.

You can also create local tags as counters or buffers. Every local tag must be initialized to prevent errors by writing local tags incorrectly.

#### HMI tags

- WinCC Runtime Advanced and Panels

  The tag value which is created in the tag map is saved in the user-defined function. Next, the tag value will be updated to the set cycle time. The customized function first accesses the tag values which were read at the previous cycle time.

  If the tag name matches the VBS name conventions in the project, you can use the tag in the user-defined function as follows.

  `'VBS_Example_03`

  `If BeltDriveOilTemperature > 100 Then [instruction]`

  If the tag name in the project does not match the VBS name conventions, you must reference the tag with the "SmartTags" list. In the following example, the tag name contains the "&amp;" character, which is not allowed according to the VBS naming conventions.

  `'VBS_Example_04`

  `SmartTags("Test&Trial")= 2005`
- WinCC Runtime Professional

  You have the same access possibilities as in the HMI devices with WinCC Runtime Advanced and Panels. You can also access the tag values asynchronously. The tag value in the PLC is accessed directly in asynchronous access. You access the tag value as follows in a local script or a user-defined C function:

  - SmartTags list (VBS)
  - Tags listing with Read-/Write method (VBS)
  - GetTag function (C)
  - SetTag function (C)

  The tag value is read once from the PLC when the method or user-defined function is called. The tag value is not updated regularly, in contrast to when it is read from the tag image.

  ![Synchronous: Tag value directly from the PLC](images/36119528715_DV_resource.Stream@PNG-en-US.png)

  Synchronous: Tag value directly from the PLC

  ![Asynchronous: Tag value from the tag image](images/36119516811_DV_resource.Stream@PNG-en-US.png)

  Asynchronous: Tag value from the tag image

> **Note**
>
> **Runtime scripting**
>
> The index of the PLC array elements can begin with any number. In WinCC, indexing always starts with 0.
>
> A PLC tag "Array [1..3] of Int", for example, is mapped to "Array [0..2] of Int" in WinCC.
>
> When you access an array in a script, pay attention to the correct indexing.

#### Local tags

You can only use local tags within user-defined functions or local scripts.

You use local tags for the following:

- Buffers
- Counters, for example For instruction

Initialize every tag according to the programming language syntax.

Example: Dim objTagFillLevel

Initialize every tag with a value to avoid errors due to empty HMI tags. To use the value of the local tag outside, link it with an internal or external HMI tag.

#### Access to HMI tags with dynamic names (WinCC Runtime Advanced and Panels)

The user-defined VB function accesses the tag value using the tag name. You can specify the tag name in such a way that the tag name is composed during the runtime of the user-defined function.

If you only call the user-defined VB function in a screen in which the HMI tag is also used elsewhere, for example in an I/O field, you should for performance reasons configure the HMI tag with "Cyclic in operation" acquisition mode.

If the user-defined VB function is accessed and the HMI tag is not being used in the screen currently displayed, configure the HMI tag with "Cyclic continuous" acquisition mode. This ensures that the current value of the tag is always available.

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)

### Testing the syntax of customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

During programming, the code is tested in the background. Syntactical errors are marked with a wavy red line. The customized function is checked for correct syntax and valid object references.

Check the syntax in the "Scripts" editor to identify all the errors in the code and output the appropriate error messages. In this case, error messages generated by the script parser are output.

Use a separate debugger to check customized VB functions for logical programming errors.

#### Error types

The following error types are detected in the syntax test and output in the "output window":

- Unknown string (e.g., not a keyword)
- Assignment of value to a constant
- The name of a local tag created with the Dim instruction is already known, e.g.: as a parameter, object, or component of the object model
- Syntax error

#### Requirements

- Customized function is open.

#### Procedure

Proceed as follows to check the syntax:

1. Click ![Procedure](images/36119552395_DV_resource.Stream@PNG-de-DE.png) to start the syntax check.

   The syntax is checked. The result of the syntax check is displayed in the Inspector window under "Info &gt; Compilation." Syntax errors are output with the line number.
2. Correct the errors in the customized function if necessary.

#### Special consideration in the syntax checking of customized functions

Customized functions are not interpreted until in Runtime. When an HMI device is being compiled, the system checks its user-defined functions for correct syntax. However, runtime errors may occur in certain circumstances.

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)

## Creating customized VB functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Accessing objects with VBS (Panels, Comfort Panels, RT Advanced, RT Professional)](#accessing-objects-with-vbs-panels-comfort-panels-rt-advanced-rt-professional)
- [Use of VB tags (RT Professional)](#use-of-vb-tags-rt-professional)
- [Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Renaming customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#renaming-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Executing customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Transfer and return of values in VBS (Panels, Comfort Panels, RT Advanced, RT Professional)](#transfer-and-return-of-values-in-vbs-panels-comfort-panels-rt-advanced-rt-professional)

### Accessing objects with VBS (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The objects of the VBS object model with the appropriate properties and methods are available in user-defined VB functions.

The object properties can be read and changed in Runtime.

#### Referencing objects

In customized VB functions you reference the objects by the corresponding list. To identify the object, use its name or the position number within the list.

If you access the properties of an object more often, create an object reference. You can access object properties with and without object reference.

With the following instruction the first object is referenced in the "MainScreen":

'VBS_Example_01

Dim objObject

'Change to Screen "MainScreen"

HMIRuntime.BaseScreenName = "MainScreen"

Set objObject = HMIRuntime.Screens(1).ScreenItems(1)

With the following instruction an object is referenced by its name and an object property is changed. You must have created the object with this name in the screen.

'VBS_Example_02

Dim objCircle

HMIRuntime.BaseScreenName = "MainScreen"

Set objCircle = HMIRuntime.Screens(1).ScreenItems("Circle_01")

objCircle.BackColor = vbGreen

---

**See also**

[Runtime scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-scripting-panels-comfort-panels-rt-advanced-rt-professional)

### Use of VB tags (RT Professional)

#### Definition of VB tags

VB tags are declared by inserting definition lines in front of the function name of a user-defined VB function.

Dim objScreen

Dim objScrItem

The validity range of a VB tag depends on where it was declared.

#### User-defined VB functions

In the "Scripts" editor, lines 1 and 2 are by default the declaration range. You can add any number of lines.

![User-defined VB functions](images/36119629451_DV_resource.Stream@PNG-de-DE.png)

You can use a VB tag defined in this manner in user-defined VB functions. When you check the syntax in the "Scripts" editor, you receive a message that the VB tag is not known.

The VB tag is only known in Runtime. It is created as soon as Runtime is started, even if the user-defined VB function itself is not called.

To prevent inconsistencies, the VB tags must be unique within the user-defined VB functions.

#### Local VB scripts

The declaration area of a local script belongs to the screen. All scripts can access the tags declared in this area within the screen . Whenever a local script is used to copy a screen object to a different screen or to the library, the script but not the declaration area is copied also.

You can show and hide the declaration range in the editor for local VB scripts. For more information, refer to "[Editor for local scripts](#editor-for-local-scripts-rt-professional)".

- Local VB scripts with acyclic trigger

  Every VB tag defined in this manner is automatically transferred to the declaration range of every local script with acyclic trigger. The declaration range remains empty for local scripts with cyclic trigger.
- Local VB scripts with cyclic trigger

  Every VB tag defined in this manner is automatically transferred to the declaration range of every local VB script with cyclic trigger. The declaration range remains empty for local scripts with acyclic trigger.

#### Example

A local VB script is configured for the property "Background color". The local VB script has a cyclic trigger.

The VB tags a and b are declared in the declaration range.

![Example](images/36119638411_DV_resource.Stream@PNG-en-US.png)

When you configure a local VB script for the "Changed" event, this VB script has an acyclic trigger. The declaration range is empty.

![Example](images/36119652491_DV_resource.Stream@PNG-en-US.png)

When you configure a local VB script with cyclic trigger for a different property, the VB tags a and b are already declared in the declaration range.

![Example](images/36119666571_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Editor for local scripts (RT Professional)](#editor-for-local-scripts-rt-professional)

### Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

When you create a customized VB function, you define the following settings:

- The name with which you call the user-defined VB function.
- The type of user-defined VB function.
- The parameters which are transferred to the user-defined VB function in Runtime.

Use only the following characters for the name:

- "A" to "Z"
- "a" to "z"
- "0" to "9"
- "_" as a separator

  > **Note**
  >
  > When you change the parameters or the function type, the change is color marked at the point of use, e.g. in the function list.

#### Procedure

To create a user-defined VB function, follow these steps:

1. Open "Scripts" in the project tree.
2. Double click "Add new VB function" in the project tree under "VB scripts".

   ![Procedure](images/36119694731_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36119694731_DV_resource.Stream@PNG-en-US.png)

   The user-defined VB function is created as a new tab in the work area. The input mask for the configuration settings of the user-defined VB function opens in the Inspector window.
3. Configure the user-defined VB function in the Inspector window "Properties &gt; General &gt; General".
4. Enter a descriptive "Name" for the user-defined VB function.
5. Select the "Type" of the user-defined VB function.

   - "Function" have a return value.
   - "Sub" have no return value.
6. Click "&lt;Add&gt;" in the "Parameters" list to add parameters. Enter the parameter name and specify the parameter type.

   You will find further information in "[Transfer and return of values in VBS](#transfer-and-return-of-values-in-vbs-panels-comfort-panels-rt-advanced-rt-professional)".

   - "ByVal" transfers the parameter value.
   - "ByRef" transfers the address of the parameter.
7. Enter its code in the work area.

   See ["Scripts" editor](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional) for additional information.

#### Result

The user-defined VB function has been created. The type, name, and function parameters are displayed in the title bar.

The start and end are inserted automatically when the user-defined function is created.

If you have protected the user-defined VB functions by a password, it is saved encrypted in the project. For more information, refer to "[Protecting user-defined functions](#protecting-user-defined-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

The figure below shows a user-defined VB function which converts the temperature from "Fahrenheit" to "Degrees Celsius":

![Result](images/36119708171_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Transfer and return of values in VBS (Panels, Comfort Panels, RT Advanced, RT Professional)](#transfer-and-return-of-values-in-vbs-panels-comfort-panels-rt-advanced-rt-professional)
  
["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Protecting user-defined functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#protecting-user-defined-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)

### Renaming customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Renaming a user-defined VB function in the project tree

Proceed as follows to rename a user-defined VB function in the project tree:

1. Select the desired user-defined VB function in the project tree.
2. Select the "Rename" (F2) command in the shortcut menu of the user-defined VB function.
3. Enter a new name for the user-defined VB function.

#### Renaming a user-defined VB function in the Inspector window

Proceed as follows to rename a user-defined VB function in the Inspector window:

1. Open the user-defined VB function in the "Scripts" editor.
2. In the Inspector window, click "Properties &gt; Properties &gt; General".
3. Enter the new function name.

#### Result

The user-defined VB function is renamed. The application points are adapted automatically.

### Executing customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

In WinCC you have the following options to execute a customized function:

- Function list
- Customized VB function
- Local VB script (only for WinCC Runtime Professional)

#### Calling a customized VB function in a function list

1. Add the user-defined VB function to a function list like a system function.

   You will find the customized VB functions in the drop-down list under "VB functions".

   You will find further information about this in "Configuring a function list".
2. If the user-defined VB function has parameters, supply the parameters with static values or HMI tags.
3. If the user-defined VB function has a return value, select an HMI tag. The value to be processed is transferred to the HMI tag.

**Note**

You can only use customized functions of the same programming language in a function list. You specify the programming language with the selection of the first customized function.

#### Calling a customized VB function in a customized VB function

1. Open the user-defined VB function in which you want to call the user-defined VB function.
2. Call the customized VB function in the syntax of the programming language. You will find further information about this in "Calling customized functions".
3. If the user-defined VB function has a return value, assign an expression, such as a local tag, to the VB function.

**Note**

You can only call user-defined functions of the same programming language in a user-defined VB function.

#### Calling a customized VB function in a local VB function

1. The function list is converted into a local VB script.
2. Call the customized VB function in the syntax of the programming language. You will find further information about this in "Calling customized functions".
3. If the user-defined VB function has a return value, assign an expression, such as a local tag, to the VB function.

**Note**

You can only call user-defined functions of the same programming language in a local VB script.

---

**See also**

[Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Transfer and return of values in VBS (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Transfer of a value

The following options are available for transferring parameters.

- "Call by Value" - ByVal

  ByVal transfers the parameter value. If you transfer a tag as a parameter, the tag value is transferred to the user-defined function when the user-defined function is executed.
- "Call by Reference" - ByRef

  ByRef transfers the address of the parameter. If you transfer a tag as a parameter, the tag address is transferred to the user-defined function when the user-defined function is executed.

  When user-defined functions and system functions are called in user-defined functions, the parameter is transferred as ByRef.

#### Return of a value

Return values can return the result of a calculation (e.g., average value of two numbers). But a return value can also give information about whether an instruction was executed correctly.

Therefore, the system functions that perform file operations such as "Delete" also have return values.

For a user-defined function to return a value, you must set the "Function" type. You assign the function name to the return value in the user-defined function:

![Return of a value](images/36119756043_DV_resource.Stream@PNG-de-DE.png)

To form an average value of two numbers, call the user-defined VB function Average and transfer the result to the HMI tag for example AverageValue.

- In a customized VB function

SmartTags("AverageValue") = Average ("4", "10")

- In the function list

  ![Return of a value](images/36119764747_DV_resource.Stream@PNG-en-US.png)

You can output the value of the HMI tag AverageValue in an I/O field.

---

**See also**

[Create customized VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-customized-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Converting Fahrenheit into degrees Celsius (Panels, Comfort Panels, RT Advanced)](#example-converting-fahrenheit-into-degrees-celsius-panels-comfort-panels-rt-advanced)
  
[Example: Converting inches into meters (Panels, Comfort Panels, RT Advanced)](#example-converting-inches-into-meters-panels-comfort-panels-rt-advanced)

## Creating user-defined C functions (RT Professional)

This section contains information on the following topics:

- [Accessing objects with C (RT Professional)](#accessing-objects-with-c-rt-professional)
- [Creating a C-Header (RT Professional)](#creating-a-c-header-rt-professional)
- [Use of Global C-Tags (RT Professional)](#use-of-global-c-tags-rt-professional)
- [Calling functions from DLLs in a user-defined C function (RT Professional)](#calling-functions-from-dlls-in-a-user-defined-c-function-rt-professional)
- [Set up code page for C function (RT Professional)](#set-up-code-page-for-c-function-rt-professional)
- [Create customized C functions (RT Professional)](#create-customized-c-functions-rt-professional)
- [Renaming customized C functions (RT Professional)](#renaming-customized-c-functions-rt-professional)
- [Executing customized C functions (RT Professional)](#executing-customized-c-functions-rt-professional)
- [Transfer and return of values in C (RT Professional)](#transfer-and-return-of-values-in-c-rt-professional)

### Accessing objects with C (RT Professional)

#### Introduction

Use the following system functions to access the properties of objects:

- "[GetProp](C%20scripting%20%28RT%20Professional%29.md#getprop-rt-professional)": System functions which begin with "GetProp" get a value.
- "[SetProp](C%20scripting%20%28RT%20Professional%29.md#setprop-rt-professional)": System functions which begin with "SetProp" set a value.

There is a separate system function with GetProp and SetProp for every data type.

#### Addressing an object property

You can open the object list for assigning parameters with &lt;Ctrl+J&gt; and select the available objects and properties from the list. The data types of the transferred parameters are checked for plausibility in a syntax validation.

#### Writing an object property

The following example shows how a circle is moved to layer "4":

SetPropLong("Screen_1", "Circle_1", "Layer", 4);

---

**See also**

[SetPropLong (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setproplong-rt-professional)
  
[GetProp (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#getprop-rt-professional)
  
[SetProp (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setprop-rt-professional)
  
[Example of accessing objects in the Screens editor (RT Professional)](#example-of-accessing-objects-in-the-screens-editor-rt-professional-1)

### Creating a C-Header (RT Professional)

#### Introduction

Use the "GlobalDefinitions.h" header file to define functions, tags and constants which you need in all local C scripts and customized C functions. In this way local C scripts and customized C functions remain slim and you avoid redundancy. Changes are carried out at a central point in the header file.

Customized C functions which you have defined in the project are automatically available. You do not need to define these C functions in the "GlobalDefinitions.h".

C libraries such as "Math" are reference by default.

You can also:

- create additional C header files.
- integrate external C header files.

#### Creating an additional C header file

1. Double click "Add new header" under "Scripts &gt;C headers" in the project tree".
2. Enter a "Name" for the C header in the Inspector window under "Properties &gt;General &gt;General".
3. Insert the required declarations of tags and constants in the work area.

#### Using the C header file in a C function

1. To use the declarations of the C header file in a C function, insert the C header in the global area of the C function. C header is integrated with an #include instruction. C header files may not be read in several times, to avoid errors in the tag access. Multiple reading of header files is prevented for example by the following structure.  
   #ifndef _myHeader_h  
   #define _myHeader_h  
   #include "myheader.h"  
   #endif

#### Include path for external C header files

You must specify the Include path to use external C header files. Proceed as follows:

1. Select the required HMI device.
2. Select the "Options &gt; Settings" menu command.
3. Select the path for the additional C header in the area navigation under "Visualization &gt; Runtime Scripting".
4. Close WinCC and start it again.
5. Select the "Compile &gt; Software (compile all)" command in the shortcut menu of the HMI device.

> **Note**
>
> **Copying a project in which an external C header file is used**
>
> The path specification for the external header file is not saved in the project and is only valid on the computer on which it was set. If you copy this project to another computer, you must reassign the Include path for external C header files in the copied project.

### Use of Global C-Tags (RT Professional)

#### Definition of global C tags

A global C tag is inserted by adding the definition line in front of the function name of a function:

int global_a; //The tag global_a is defined as integer

void myfunction()

{

//insert the code starting here

}

#### Use of global C tags

You use global C tags in user-defined C functions or local C scripts by declaring the C tags within the header file "GlobalDefinitions.h" as external:

**GlobalDefinitions.h**

`extern int global_a;`

**Customized C function**

// Insert the header starting here

#include "GlobalDefinitions.h"

void myFunction()

{

//insert the code starting here

printf ("C2: %i\r\n", ++ global_a);

}

This tells the compiler that it does not need to create the tag global_a, rather that it will be created elsewhere in Runtime.

If the value of the global_a tag is now changed, the changed value is available in all user-defined C functions and local C scripts.

You can also declare C tags directly within a function. However, for reasons of clarity and to avoid duplicate definitions, we recommend defining global C tags in only one location.

> **Note**
>
> A maximum of 64 Kbytes is available to a user-defined function and the global C tag defined with it.

#### Validity range

All tags in GlobalDefinitions.h declared as external are known to all user-defined C functions and local C scripts in Runtime. It is created as soon as Runtime is started, even if the user-defined function itself was not called.

> **Note**
>
> In WinCC service mode, global C tags cannot be exchanged between user-defined C functions in the Scheduler and user-defined functions in the Screens Editor.
>
> If you want to address tags via the WebNavigator, you need to call up the C function via the globally declared C tag.

### Calling functions from DLLs in a user-defined C function (RT Professional)

#### Introduction

You can use functions from DLLs in user-defined C functions. This lets you use the range of functions from existing DLLs and avoid redundancy.

> **Note**
>
> **Release and debug DLLs**
>
> WinCC is supplied as a Release version and therefore uses the Release versions of system DLLs. If you want to use your own DLLs in the Debug version, you can also load the Release DLL. Always use the Release version of the DLL when using your own DLLs to avoid a system overload.

#### Requirement

DLL is in the "..\Common Files\Siemens\bin" folder or in a folder which is defined in the PATH system tag. This tag is specified by the system properties of the operating system.

#### Procedure

Proceed as follows to call functions from DLLs:

1. Open the user-defined C function in which you want to call DLL functions.
2. Add the following code to the beginning of the user-defined C function:

#pragma code("&lt;Name&gt;.dll")

//Declare functions stored in DLL:

&lt;Return value&gt; &lt;Function name 1&gt;(...);

&lt;Return value&gt; &lt;Function name 2&gt;(...);

...

&lt;Return value&gt; &lt;Function name n&gt;(...);

#pragma code

#### Result

The functions &lt;Function name 1&gt; ... &lt;Function name n&gt; from &lt;Name.dll&gt; are declared. You can call the functions in the user-defined C function.

#### Example

The following example shows how to integrate the "kernel32.dll" file and call the "GetLocalTime" function:

#pragma code("kernel32.dll")

VOID GetLocalTime(LPSYSTEMTIME lpSystemTime);

#pragma code()

SYSTEMTIME st;

GetLocalTime(&amp;st);

### Set up code page for C function (RT Professional)

#### Introduction

You can use your WinCC project in several languages​. You define for each C script which code page is used to translate which language. The code page affects the display of all texts, which are output in runtime in the C script.

When you create a C function, you decide whether to select the settings of the HMI device or one of the configured runtime languages​​.

The following options are available in the runtime settings of the HMI device:

- Operating system language for non-Unicode programs

  The C function is translated into English in the ES.

  Texts are displayed in the code page of this language in runtime.
- Currently set WinCC Runtime language

  The C function is translated into English in the ES.

  Texts are displayed in the code page of this language in runtime.
- Configured runtime language

  The C function is translated into this language in the ES.

#### Requirement

- The required languages are enabled in the "Project Languages​​" editor.
- The required runtime languages ​​are enabled in the "Language &amp; Font" editor.

#### Select code page for the HMI device

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language &amp; Font".
3. Under "Language setting for script &gt; Language of C scripts with 'Use device setting'", set the selection window using ![Select code page for the HMI device](images/67834322699_DV_resource.Stream@PNG-de-DE.png):

   - Selection of all runtime languages
   - Selection of all the other options
4. Select the required code page.

#### Result

If texts are output in runtime via C function, the code page set for the script is used.

### Create customized C functions (RT Professional)

#### Introduction

When you create a customized C function, you define the following settings:

- The name with which you call the user-defined C function.
- The type of user-defined C function.
- The parameters which are transferred to the user-defined C function in Runtime.

  > **Note**
  >
  > When you change the parameters or the function type, the change is color marked at the application point, e.g. in the function list.
- The code page for the C function.

Use only the following characters for the name:

- "A" to "Z"
- "a" to "z"
- "0" to "9"
- "_" as a separator

  > **Note**
  >
  > Names are not case-sensitive. It is not possible to create two user-defined C functions with the same name but different notation.

  > **Note**
  >
  > **Invalid tag names**
  >
  > The following designations are already assigned to the "char" data type in Runtime and must not therefore be used as internal tags in C scripting:
  >
  > - "Object"
  > - "Property"
  > - "Tag"
  > - "Picture"

#### Procedure

Proceed as follows to create a new customized C function:

1. Open "Scripts" in the project tree.
2. Double click "Add new C function" in the project tree under "C scripts".

   ![Procedure](images/36119863435_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36119863435_DV_resource.Stream@PNG-en-US.png)

   The user-defined C function is created as a new tab in the work area. The input mask for the configuration settings of the function opens in the Inspector window.
3. Select the required language setting under "Code page".

   ![Procedure](images/67834334091_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/67834334091_DV_resource.Stream@PNG-en-US.png)
4. Configure the function in the Inspector window "Properties &gt; General &gt; General".
5. Enter a descriptive "Name" for the user-defined C function.

   Select the "Type" of the user-defined C function. Further information can be found in "Transfer and return of values in C".

   - Void: Function has no return value.
   - Tag: Return value is returned as a tag value.
   - Pointer: Return value points on the address of the tag.
6. Double click "&lt;Add&gt;" in the "Parameters" list to add parameters. Enter the parameter name. Further information can be found in "Transfer and return of values in C".

   - Tag transfers the parameter value.
   - Pointer transfers the address of the parameter.
7. Write the code in the work area.

#### Result

The user-defined C function is created. The type, name, and function parameters are displayed in the title bar.

The start and end are inserted automatically when the user-defined function is created.

If you have protected the user-defined C functions by a password, it is saved encrypted in the project. For more information, refer to "[Protecting user-defined functions](#protecting-user-defined-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

The figure below shows a user-defined C function which converts the temperature from "Fahrenheit" to "Degrees Celsius":

![Result](images/36119837195_DV_resource.Stream@PNG-en-US.png)

---

**See also**

["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Protecting user-defined functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#protecting-user-defined-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Renaming customized C functions (RT Professional)

#### Renaming a user-defined C function in the project tree

Proceed as follows to rename a user-defined C function in the project tree:

1. Select the user-defined C function in the project tree.
2. Select the "Rename" (F2) command in the shortcut menu of the user-defined C function.
3. Enter a new name for the user-defined C function.

#### Renaming a user-defined C function in the Inspector window

Proceed as follows to rename a user-defined C function in the Inspector window:

1. Open the user-defined C function in the "Scripts" editor.
2. In the Inspector window, click "Properties &gt; General &gt; General".
3. Enter the new function name.

#### Result

The user-defined C function is renamed. The application points are adapted automatically.

### Executing customized C functions (RT Professional)

#### Introduction

In WinCC you have the following options to execute a customized C function:

- Function list
- Customized C function
- Local C script

#### Calling a customized C function in a function list

1. Add the user-defined C function to a function list like a system function.

   You will find the customized C functions in the drop-down list under "C functions".

   You will find further information about this in "Configuring a function list".
2. Supply the parameters with static values or HMI tags.
3. If the user-defined C function has a return value, select an HMI tag. The value to be processed is transferred to the HMI tag.

**Note**

You can only use customized functions of the same programming language in a function list. You specify the programming language with the selection of the first customized function.

#### Calling a user-defined C function in a user-defined C function

1. Open the user-defined C function in which you want to call the user-defined C function.
2. Call the customized C function in the syntax of the programming language. You will find further information about this in "Calling customized functions".
3. If the user-defined C function has a return value, assign an expression, such as a local tag, to the function.

**Note**

You can only call user-defined C functions of the same programming language in a user-defined C function.

#### Calling a customized C function in a local C script

1. The function list is converted into a local C script.
2. Call the customized C function in the syntax of the programming language. You will find further information about this in "Calling customized functions".
3. If the user-defined C function has a return value, assign an expression, such as a local tag, to the C function.

**Note**

You can only use user-defined functions of the same programming language in a local C script.

---

**See also**

[Calling system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Calling customized functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#calling-customized-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Transfer and return of values in C (RT Professional)

#### Transfer of a value

You have the following possibilities for transferring parameters:

- Tag (Call by value)

  The tag name and the data type are specified to save values in the tag. But this tag is not transferred directly but a copy made. When executing the user-defined C function, the tag value of the copy is transferred to the C function. If you change the tag value, the change is only valid within the user-defined C function.
- Pointer (Call by reference)

  A pointer is a tag which points on the address of a tag. Pointers are defined like tags. The * character is added to the data type, e.g. Double*. The user-defined C function accesses the tag to which the pointer is pointing. If you change the tag value, the changed tag value is written into the tag.

#### Return of a value

A user-defined C function can execute simple instructions and return no value. The return value is then a "void" data type.

If a return value is required, the value can be returned as a tag or a pointer.

But a return value can also give information about whether an instruction was executed correctly. Therefore, the system functions that perform file operations such as write to a file also have return values.

For a user-defined C function to return a value, you must set the "Double" type, for example. The result is transferred to the user-defined C function with the return instruction.

![Return of a value](images/36119907979_DV_resource.Stream@PNG-de-DE.png)

To form an average value from two numbers, call the user-defined C function Average and transfer the result to the HMI tag, for example, AverageValue.

- In a customized C function

SetTagDouble("AverageValue",Average (4, 5));

- In the function list

  ![Return of a value](images/36119764747_DV_resource.Stream@PNG-en-US.png)

You can output the value of the HMI tag AverageValue in an I/O field.

## Protecting user-defined functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Setting up know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-up-know-how-protection-panels-comfort-panels-rt-advanced-rt-professional)
- [Opening user-defined functions with know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)](#opening-user-defined-functions-with-know-how-protection-panels-comfort-panels-rt-advanced-rt-professional)
- [Removing know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-know-how-protection-panels-comfort-panels-rt-advanced-rt-professional)
- [Changing a password (Panels, Comfort Panels, RT Advanced, RT Professional)](#changing-a-password-panels-comfort-panels-rt-advanced-rt-professional)

### Setting up know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Procedure

To set up know-how protection for user-defined functions, follow these steps:

1. Select the user-defined function without know-how protection that you want to protect.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Know-how protection" dialog will open.
3. Click "Define".

   The "Define password" dialog box opens.
4. Enter a password in the "New" field.
5. Enter the same password in the "Confirm" field.
6. Confirm your entries with "OK".
7. Close the "Know-how protection" dialog by clicking on "OK".

#### Result

The user-defined function receives know-how protection. User-defined functions with know-how protection are marked with a lock in the project tree. The password entered is valid for all user-defined functions selected.

### Opening user-defined functions with know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)

You can only open multiple user-defined functions with know-how protection at once if they are protected with the same password.

#### Procedure

To open a know-how-protected user-defined function, follow these steps:

1. Double-click the user-defined function you want to open.

   The "Access protection" dialog will open.
2. Enter the password for the user-defined function with know-how protection.
3. Confirm your entry with "OK".

#### Result

The user-defined function with know-how protection will open provided you have entered the correct password. However, the function will remain know-how protected.

Once you have opened the user-defined function, you can edit it for as long as the user-defined function or TIA portal is open. You must enter the password again the next time you open the user-defined function. If you close the "Access protection" dialog with "Cancel" or "Close", the user-defined function is opened but the code is not displayed. You cannot edit the user-defined function.

### Removing know-how protection (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Procedure

To remove the know-how protection of a user-defined function, follow these steps:

1. Select the user-defined function for which you want to remove know-how protection.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Know-how protection" dialog will open.
3. Deactivate the check box "Hide code (know-how protection)".
4. Enter the password.
5. Confirm your entries with "OK".

**Note**

To remove know-how protection for several user-defined functions at once, all selected user-defined functions must have the same password.

#### Result

Know-how protection will be disabled for the selected user-defined function.

### Changing a password (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Procedure

To change the password, follow these steps:

1. Select the user-defined function with know-how protection for which you want to change the password.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Know-how protection" dialog will open.
3. Click the "Change" button.
4. Enter the old password in the "Old" field.
5. Enter the new password in the "New" field.
6. Enter the new password again in the "Confirm" field.
7. Confirm your entries with "OK".
8. Close the "Know-how protection" dialog by clicking on "OK".

**Note**

To change the password for several user-defined functions at once, all selected user-defined functions must have the same password.

## Creating local scripts (RT Professional)

This section contains information on the following topics:

- [Local scripts (RT Professional)](#local-scripts-rt-professional-1)
- [Editor for local scripts (RT Professional)](#editor-for-local-scripts-rt-professional)
- [Converting a function list to a local script (RT Professional)](#converting-a-function-list-to-a-local-script-rt-professional)
- [Dynamizing an object property with a local script (RT Professional)](#dynamizing-an-object-property-with-a-local-script-rt-professional)

### Local scripts (RT Professional)

#### Definition

Local scripts are bound to a single object, such as an object property, and have a cyclic or acyclic trigger. A local script is created directly at the point of use:

- Scheduler
- Screens

  - Event (converted function list)
  - Object property (property list)
  - Property change (property list)
- Menus and toolbars
- Only C script: Reports

  - I/O field at the process value property

Local scripts are not displayed in the project navigation and are only available at the point of use.

#### Application

Local scripts are used for the following:

- Property list (screen object): Dynamic control of object properties

  A local script is used to dynamize an object property in Runtime by means of its return value. Example: Changing the object position in dependence of several parameters.
- Function list (screen object): Converting a function list to a local script

  Convert a function list to a local script in order to configure conditional instructions or loops at an event.
- Scheduler (task): Execute local script cyclically or acyclically

  Use the Scheduler to execute a script at a specified point in time.

Local scripts are not loaded into the memory of the HMI device until they are used, for example when loading a screen. Local scripts thus reduce memory requirements on the HMI device.

#### Programming

When a local script is created at an object property, a local script with return value is generated. The return value supplies the value for the object property.

When a local script is created at an event, a local script without return value is generated.

The parameters which are transferred to the local script depend on the used programming language and the application point.

**Typical parameters of a local VB script**

**Item**: Contains the object reference:

- Scheduler (task): No object is transferred.
- Menu &amp; toolbars: The object that triggers the event is transferred.
- Screens (screen object):

  - Property list (screen object): In dynamizations, the screen object whose property you dynamize is transferred.
  - Converted function list (screen object): The screen object whose event you configure is transferred.

  To access the properties of the transferred screen object, enter "item.". The available properties are listed. Use ScreenItems to access another object of the object model..

  Further information about parameters of events are available in the reference.

**Typical parameters of a local C script**

**Char* screenName**: Contains the name of the screen that contains the object whose property is being dynamized.

**Char* objectName**: contains the name of the object whose property you dynamize.

**Char* propertyName**: Contains the property that is being dynamized.

Further information about parameters of events are available in the reference.

#### Execution of local scripts

Local scripts require a trigger. The trigger specifies when the script will be executed. The point of use of the local script determines which trigger is used:

- Local scripts of a converted function list are executed when the event occurs, for example, printing.
- Local scripts in the property list get the trigger automatically. You can change the trigger, e.g. to tag trigger.
- Local scripts of a task are assigned a trigger by the project engineer.

---

**See also**

[Editor for local scripts (RT Professional)](#editor-for-local-scripts-rt-professional)
  
[Dynamizing an object property with a local script (RT Professional)](#dynamizing-an-object-property-with-a-local-script-rt-professional)
  
[Converting a function list to a local script (RT Professional)](#converting-a-function-list-to-a-local-script-rt-professional)
  
["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)

### Editor for local scripts (RT Professional)

#### Properties of the editor for local scripts

The editor for local scripts has no own setting possibilities but "inherits" the settings from "Runtime Scripting".

The editor offers similar functions to the "Scripts" editor. You will find further information in "["Scripts" editor](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)".

The following functions are not available in the toolbar:

- Drop-down lists for properties and functions

The editor for local VB scripts contains the following additional icons:

- ![Properties of the editor for local scripts](images/36119947403_DV_resource.Stream@PNG-de-DE.png) Shows declaration range.
- ![Properties of the editor for local scripts](images/36119955723_DV_resource.Stream@PNG-de-DE.png) Hides declaration range.

You define local VB tags in the declaration range. For more information, refer to "[Use of VB tags](#use-of-vb-tags-rt-professional)".

#### Availability

The editor for local scripts can be called in the following places:

- Scheduler

  - Event: Execute
- Screens

  - Event
  - Object property (property list)
  - Property change (property list)
- Menus and toolbars

  - Event: Click
- Only C script: Reports

  - I/O field at the process value property

---

**See also**

[Local scripts (RT Professional)](#local-scripts-rt-professional-1)
  
["Scripts" editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#scripts-editor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Use of VB tags (RT Professional)](#use-of-vb-tags-rt-professional)

### Converting a function list to a local script (RT Professional)

#### Introduction

When you convert a function list to a local script, you can configure conditional instructions or loops for an event. A function list is converted either to a local VB or C script.

If the function list does not contain a customized function, the programming language is determined by the function.

If a C function is contained, for example, the function list is converted into a local C script.

> **Note**
>
> **Error message in the Global Script diagnostics window**
>
> If a tag of the type WString is used in a SetTagsystem function that was converted into a C script, an error message is output in the Global Script diagnostics window when executing the function. The message does not affect the execution of the function.
>
> The following SetTagfunctions are affected:
>
> - SetTagWithOperatorEvent
> - SetTagIndirect
> - SetTagByTagIndirect
> - SetTagIndirectByTagIndirect
> - SetTagByProperty
> - SetTagIndirectByProperty

#### Requirement

The function list is opened.

#### Procedure

Proceed as follows to convert a function list to a local script:

1. Select the event whose function list you want to convert to a script.
2. Configure system functions at the event as required.
3. To convert the function list to a local script, click ![Procedure](images/36119976459_DV_resource.Stream@PNG-de-DE.png) or ![Procedure](images/36119984139_DV_resource.Stream@PNG-de-DE.png).
4. Write the program code.

Alternatively you use the "Convert VB script" or "Convert C script" command in the shortcut menu.

#### Result

If the event occurs, the local script is processed automatically.

#### Deleting a local script

Proceed as follows to delete a local script:

1. Select the event with the local script.
2. Select "Function list" in the shortcut menu of the event.

The local script is deleted.

---

**See also**

[Local scripts (RT Professional)](#local-scripts-rt-professional-1)

### Dynamizing an object property with a local script (RT Professional)

#### Introduction

With a local script you dynamize an object property in Runtime by the return value of the script.

#### Requirement

- The object with the property to be dynamized is selected.
- The Inspector window is open.

#### Procedure

1. Click ![Procedure](images/36120004235_DV_resource.Stream@PNG-de-DE.png) in the Inspector window.
2. Select the object property to be dynamized.
3. Select the "VB script" or "C script" entry in the "Dynamization" column.

   A dialog opens.
4. Write the program code.
5. Click "![Procedure](images/36120011915_DV_resource.Stream@PNG-de-DE.png)" in the toolbar to change the trigger.

#### Result

The object property changes in Runtime according to how the property list is configured.

#### Deleting the dynamization

1. Select the dynamized object property in the property list.
2. Select the "None" entry in the "Dynamization" column.

---

**See also**

[Local scripts (RT Professional)](#local-scripts-rt-professional-1)

## Debugging (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Debugging of user-defined VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#debugging-of-user-defined-vb-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Principles of Debugging (Panels, Comfort Panels, RT Advanced, RT Professional)](#principles-of-debugging-panels-comfort-panels-rt-advanced-rt-professional)
- [Activating the debugger (Panels, Comfort Panels, RT Advanced, RT Professional)](#activating-the-debugger-panels-comfort-panels-rt-advanced-rt-professional)
- [Structure of VBScript files (Panels, Comfort Panels, RT Advanced)](#structure-of-vbscript-files-panels-comfort-panels-rt-advanced)
- [Structure of VBScript files (RT Professional)](#structure-of-vbscript-files-rt-professional)
- [Names in the debugger (Panels, Comfort Panels, RT Advanced, RT Professional)](#names-in-the-debugger-panels-comfort-panels-rt-advanced-rt-professional)
- [Breakpoints (Panels, Comfort Panels, RT Advanced, RT Professional)](#breakpoints-panels-comfort-panels-rt-advanced-rt-professional)
- [Working step-by-step (Panels, Comfort Panels, RT Advanced, RT Professional)](#working-step-by-step-panels-comfort-panels-rt-advanced-rt-professional)
- [Executing commands (Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-commands-panels-comfort-panels-rt-advanced-rt-professional)
- [Determining tag and property values (Panels, Comfort Panels, RT Advanced, RT Professional)](#determining-tag-and-property-values-panels-comfort-panels-rt-advanced-rt-professional)
- [Diagnostics (RT Professional)](#diagnostics-rt-professional)

### Debugging of user-defined VB functions (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Overview

To test a user-defined VB function in Runtime, you can use the debugger of "Microsoft Visual Studio 2008", for example.

The debugger is included in the WinCC Setup. If another Visual Studio version is already installed, Microsoft Visual Studio 2010 for example, use the debugger of this version.

#### Debugger for WinCC Runtime Professional

The Microsoft Visual Studio 2008 Shell (Integrated Mode) debugger is located on the DVD of WinCC Runtime Professional the Support directory.

#### Debugger for WinCC Runtime Advanced

You can download the Microsoft Visual Studio 2008 Shell (Integrated Mode) debugger for free from the Microsoft homepage. In doing so, make sure that you use the English version.

The latest versions from Microsoft are generally recommended for the purpose of debugging.

#### Installing the debugger for WinCC

**Procedure**

1. Start the Setup of Microsoft Visual Studio 2008 Shell (Integrated Mode)
2. Follow the instructions and accept the default settings.

   The following program is installed: Microsoft Visual Studio 2008 Shell (Integrated Mode) - ENU
3. When you start the debugger the first time, the "Visual Studio Just-In-Time Debugger" dialog opens.

   Select the entry "New instance of Visual Studio 2008".

   To specify "Visual Studio 2008" as the default debugger, select the "Set the currently selected debugger as the default." setting.

**Microsoft Visual Studio 2008 Debugger**

![Installing the debugger for WinCC](images/111974408843_DV_resource.Stream@PNG-de-DE.png)

### Principles of Debugging (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

For example, you can use a debugger to test whether correct values are being transferred to tags and whether abort conditions are being correctly implemented. You can do the following in the debugger:

- Inspect the source code of the function
- Check the step-by-step execution of the functions
- View and change tags and property values
- See and check function sequence

The debugger is only intended for identifying error locations in the user-defined VB function. To do this, you use breakpoints, for example, or you execute the user-defined VB function step-by-step. For detailed information, refer to the documentation of the debugger you are using. In order to correct errors, you change to the "Scripts" editor in WinCC. After compiling and downloading again, you test the user-defined VB function again with the debugger.

> **Note**
>
> Please note that the code displayed in the debugger is write-protected. The code cannot be changed directly in the debugger but only test the necessary changes.

#### Difference with regard to VBScript for Windows and Windows CE

The debugger checks the syntax for VBScript for Windows. If the function contains a VBScript function for Windows CE, a corresponding error message is output. Some VBScript functions are different, e.g. CreateObject.

#### Debugging VB scripts

You can use the "Debug" object to enter custom texts in a debugger. The object has the methods "Write" and "WriteLine". You can find additional information about the "Debug" object on the [internet](https://msdn.microsoft.com/en-us/library/wk3y866c(v=vs.84).aspx).

You can use the "Err" object to respond to error messages that are generated by another object. The object has the methods "Raise" and "Clear". You can find additional information about the "Err" object on the [internet](https://msdn.microsoft.com/en-us/library/sbf5ze0e(v=vs.84).aspx).

#### Error types

A distinction is made between the following types of error by the debug:

- Syntax error  
  Syntax errors arise, for example, when you misspell a keyword or fail to close parentheses. If you use the syntax check of WinCC, you can eliminate syntax errors before testing your functions in Runtime.

  The syntax check in WinCC parses a function without executing it. The function is parsed again immediately before its execution in Runtime. All sections are parsed, including those that are not executed until a particular action occurs at a later time.

  If a function contains syntax errors, you cannot start Runtime.

  > **Note**
  >
  > For Runtime Professional you can specify in "Runtime settings &gt; General &gt; Script options" that Runtime will be started even when a function contains syntax errors.
- Runtime error

  A runtime error occurs when an invalid/incorrect command is to be executed, e.g. because a tag is not defined. To intercept runtime errors, you can use the "On Error Resume Next" instruction in a function. This instruction causes the subsequent instruction to be executed after a runtime error. In the subsequent line, the error code can then be checked using the Err object. To switch off the handling of runtime errors in the script, use the "On Error Goto 0" instruction.
- Logical errors

  The debugger is particularly helpful in clearing up logical errors. A logical error occurs when an unexpected result is received because, for example, a condition was incorrectly checked. To eliminate logical errors, execute your function step-by-step in order to identify the section of the script that is not functioning properly.

#### Example of error handling

Sub OnClick(ByVal Item)

'VBS27

Dim objScreenItem

'

'Activation of errorhandling:

On Error Resume Next

For Each objScreenItem In ScreenItems

If "HMIRectangle" = objScreenItem.Type Then

'

'=== Property "RoundCornerHeight" only available for RoundRectangle

objScreenItem.RoundCornerHeight = objScreenItem.RoundCornerHeight * 2

If 0 &lt;&gt; Err.Number Then

HMIRuntime.Trace objScreenItem.Name &amp; ": no RoundedRectangle" &amp; vbCrLf

'

'Delete error message

Err.Clear

End If

End If

Next

On Error Goto 0  'Deactivation of errorhandling

End Sub

#### Basic Procedure

When an error has occurred and the debugger is open, the script appears in a window, write-protected. It is possible to navigate through the script document, set breakpoints, execute the script again in Runtime and to process the script step-by-step.

The source codes of the scripts cannot be edited directly in the scripts. If you have found an error, you can correct the error in the function in WinCC, download the picture again and update the picture in the debugger.

#### Change Picture During Debug

If a picture change is executed during debugging, the script document of the "old" picture remains open but is no longer valid. If necessary, invalid errors are displayed because the objects called following the picture change are no longer available.

---

**See also**

[VBScript for Windows CE (Panels, Comfort Panels)](VBScript%20for%20Windows%20CE%20%28Panels%2C%20Comfort%20Panels%29.md#vbscript-for-windows-ce-panels-comfort-panels-1)
  
[VBScript for Windows (Panels, Comfort Panels, RT Advanced, RT Professional)](VBScript%20for%20Windows%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#vbscript-for-windows-panels-comfort-panels-rt-advanced-rt-professional-1)

### Activating the debugger (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Principle

There are several ways of activating the debugger:

- Automatic activation of the debugger when an error occurs in Runtime.
- Opening an error box in Runtime via which the debugger can be activated.
- Starting the debugger from the Start menu and opening a running Runtime scripts.

#### Connecting Visual Studio to Runtime

1. Start Runtime.
2. Open "Microsoft Visual Studio 2008".
3. In the "File &gt; New" menu, click on "File".
4. Select "Windows Script Host" and click on "Open".
5. In the "Debug" menu, click on "Attach to Process".
6. Select:  
   HmiRTm.exe: for a panel or WinCC Runtime Advanced  
   PdlRt.exe: for WinCC Runtime Professional
7. Double-click one of the script files in the "Solution Explorer".

#### Visual Studio as Just-In-Time debugger

1. Open "Microsoft Visual Studio 2008".
2. In the "Tools" menu, click on "Options".
3. In the tree, click on "Debugging" and "Just-In-Time".
4. Under "Just-In-Time Debugging", select the "Script" option.
5. Close Visual Studio.
6. Start the simulation using "Online &gt; Simulation &gt; With script debugger".

#### Stopping the debugger

It is possible to stop the debugger without exiting the WinCC Runtime.

### Structure of VBScript files (Panels, Comfort Panels, RT Advanced)

#### Structure of VBScript files

All user-defined functions configured in a device are contained in a script file.

### Structure of VBScript files (RT Professional)

#### Principle

To enable simultaneous execution of cyclic and event-driven VBScript files in Runtime Professional, event-driven VBScript files and cyclic/tag-triggered VBScript files are strictly separated during their execution. A cyclic local script cannot interfere with the execution of a user-defined function which is to be triggered by clicking a button, for example.

To ensure this, the event-driven local scripts and cyclic local scripts as well as the tag-triggered local scripts are stored in separate VBScript files. Any global screen element you have defined for VBScript files in the "Screens" editor is copied to both VBScript files.

> **Note**
>
> Because the two VBScript files are handled separately, they have no common data area. Therefore, there is no synchronization of global tags between the two VBScript files. Implement any synchronization function which may be required using the DataSet object or internal HMI tags.

#### Structure of VBScript files

When VBScript files are debugged with a debugger, the VBScript files always open the different Runtime systems.

In the case of the graphical Runtime system, this means that you receive two files per picture:

- &lt;ScreenName&gt;.pdl_events: Contains the event-driven scripts.
- &lt;ScreenName&gt;.pdl_triggers: Contains the cyclic and tag-driven VBScript files.

The following section describes the structure of script files within the graphical Runtime system:

- Content of the VBScript file &lt;ScreenName&gt;.pdl_events

  General code

  Event-driven scripts
- Content of the VBScript file &lt;ScreenName&gt;.pdl_triggers

  General code

  Cyclic or tag-triggered scripts

  > **Note**
  >
  > Note that the local scripts and user-defined functions of the graphical Runtime system are not displayed by their names in the VBScript file to which they were saved in WinCC.

### Names in the debugger (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Names in the debugger

The names of user-defined functions in the debugger differ from the names by which you saved your user-defined functions in WinCC.

The function and script names in the script files are compiled according to the following rules:

| Action type | Name of the script file |
| --- | --- |
| Cyclic or tag-triggered scripts at a property | ObjectName_PropertyName_Trigger |
| Mouse events | ObjectName_OnClick  ObjectName_OnLButtonDown  ObjectName_OnLButtonUp  ObjectName_OnRButtonDown  ObjectName_OnRButtonUp |
| Keyboard events | ObjectName_OnKeyDown  ObjectName_OnKeyUp |
| Object events | ObjectName_OnObjectChanged  ObjectName_OnSetFocus |
| Events on properties | ObjectName_PropertyName_OnPropertyChanged  ObjectName_PropertyName_OnPropertyStateChanged |
| Picture events | Document_OnOpen  Document_OnClosed |

#### Valid length of the script names

The name of scripts in the script files is limited to 255 characters. Each special character used in an object name is converted to five characters. The special character appended to the leading X is represented as four-digit hexadecimal code. If you configure a button action named "PushMe" with mouse click trigger, the "DrXFFFCckMe_OnClick" script is written to the script file.

If the composite object name is too long, the syntax check in WinCC returns an error message. Because of this restriction, you cannot configure graphic object names of unlimited length.

> **Note**
>
> To ascertain the name of an object in Runtime, click &lt;Ctrl+Alt+Shift&gt; and position the mouse over the corresponding object. The screen name and the object name are displayed in a tooltip.

### Breakpoints (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

To stop the execution of the VBScript file at certain points and to localize logical errors step-by-step, set breakpoints.

When a VBScript file is updated in the debugger, all the breakpoints are lost.

> **Note**
>
> When you set a breakpoint in script file "&lt;Picturename&gt;.pdl_trigger" in Runtime Professional, all trigger-driven procedures are stopped.
>
> When you set a breakpoint in script file "&lt;Picturename&gt;.pdl_event" in Runtime Professional, all event-driven procedures are stopped.

#### Requirement

- Runtime is activated.
- The screen to be debugged is active.

#### Setting a breakpoint

1. Start the debugger and select the VBScript file.

   If automatic activation of the debuggers in WinCC has been selected, the debugger is called in as soon as an erroneous script is executed.
2. Place the cursor in the line in which you want to set a breakpoint.
3. In the "Debug" menu, select the "Toggle Breakpoint" command.

   The line is marked with a red dot.
4. Change to WinCC Runtime and execute the VBScript file to be debugged.

   The debugger stops at the first breakpoint. The current line is displayed on a yellow background.

   Simulate the program code step-by-step.

#### Deleting a breakpoint

1. Position the cursor in a line with a breakpoint.
2. In the "Debug" menu, select the "Toggle Breakpoint" command.

To delete all breakpoints in a file, select the "Delete All Breakpoints" command in the "Debug" menu.

### Working step-by-step (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You use the debugger in order to execute your VBScript files (user-defined function or local script) step-by-step, for example, to systematically localize logical errors. Simulate the effect of each code line in Runtime.

#### Requirements

- Runtime is activated.
- The screen to be debugged is active.

#### The Procedure in Principle

1. Start the debugger and select the VBScript file.

   If you have selected automatic activation of the debugger in WinCC, the debugger is called as soon as a script with error is executed.
2. Set a breakpoint in the VBScript file. Breakpoints are normally set in front of code lines in which errors are suspected.
3. Change to WinCC Runtime and trigger an action that initiates execution of the VBScript files.

   The debugger stops at the first break point and marks the current line.
4. To continue working step-by-step, select one of the following menu commands:

   - "Debug &gt; Step Over": goes to the next code line. If a user-defined function is called in this line, you skip the called user-defined function. The user-defined function is executed but the debugger does not guide you through the individual lines of the function. Instead, you jump to the first line after the function was executed.
   - "Debug &gt; Step Into": goes to the next code line. If a user-defined function is called in this line, you jump to this function. Execute the called function step-by-step.
   - Select the "Debug &gt; Step Out" menu command to cancel step-by-step execution of a called function. The function is executed completely. The debugger jumps to the first line after the function was executed.
5. Go through the document step-by-step until you reach the end, or select the "Debug &gt; Run" menu command to execute the VBScript file to the end.

### Executing commands (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Commands are entered and directly executed in the "Command Window". You can:

- Call methods
- Call procedures
- Change object properties

The "Command Window" is used to execute all commands which can also be executed in a VBScript.

> **Note**
>
> If you want to determine the name of a WinCC object in WinCC Runtime Professional, press &lt;Ctrl+Alt+Shift&gt; and move the mouse over the corresponding object. The picture name and the object name are then displayed in a tooltip.

#### Requirement

- The VBScript file runs in Runtime.
- The debugger is open.

#### Procedure

1. Set at least one breakpoint in the VBScript file.
2. Change to WinCC Runtime and trigger an action that initiates execution of the VBScript file.

   The debugger stops at the first breakpoint.
3. Select "View &gt; Other Windows &gt; Command Window". "Command Window" opens.
4. Enter the desired command and confirm with "&lt;Enter&gt;".

**Note**

An error message will not be generated in runtime if you enter an invalid command in the "Command Window". The "&lt;Script Error&gt;" message will appear in the Command Window instead.

#### Example

Dim i

For i = 1 to 10

HMIRuntime.Trace i &amp; vbnewline

Next

When this VBScript is executed and the debugger is in the loop at the breakpoint, you can use

- ?i  
  to read out the value of variable i
- i = 5  
  to set the value of variable i to 5.

### Determining tag and property values (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can determine and change the values of tags or properties in the "Command Window". You reset a process value for the user-defined function to zero without having to stop the process, for example.

> **Note**
>
> If you want to determine the name of a WinCC object in WinCC Runtime Professional, press &lt;Ctrl+Alt+Shift&gt; and move the mouse over the corresponding object. The screen name and the object name are displayed in a tooltip.

#### Requirement

- The VBScript file runs in Runtime.
- The debugger is open.

#### Procedure

1. Set at least one breakpoint in the VBScript file.
2. Change to WinCC Runtime and trigger an action that initiates execution of the VBScript file.

   The debugger stops at the first breakpoint.
3. Select "View &gt; Other Window &gt; Command Window". "Command Window" opens.
4. To determine the value of a tag or property, enter the following character string

   - ? myTag
   - ? myObject

   Note the space in front of the object name.
5. Press &lt;Enter&gt;.

### Diagnostics (RT Professional)

This section contains information on the following topics:

- [Diagnostics (RT Professional)](#diagnostics-rt-professional-1)
- [GSC diagnostics (RT Professional)](#gsc-diagnostics-rt-professional)
- [Inserting a GSC diagnostics window in a screen (RT Professional)](#inserting-a-gsc-diagnostics-window-in-a-screen-rt-professional)

#### Diagnostics (RT Professional)

##### Introduction

If you execute your local VB scripts and C scripts in Runtime, you output a quick analysis with the aid of the "Print job/Script diagnostics" object.

##### Diagnostics tools

WinCC provides you with tools to analyze the runtime behavior in local C scripts and VB scripts:

- The print job/script diagnostics "GSC diagnostics" object
- Using a debugger

##### Application

To use the GSC Diagnostics, you insert the "Print job/Script diagnostics" object in a screen. Use the "GSC diagnostics" template.

This can be a dedicated screen which is designed for diagnostics and which is called in Runtime.

##### GSC diagnosis of VBS

GSC diagnostics returns the trace methods contained in the local scripts in the order in which they were called. Trace instructions in user-defined VB functions, which are called in local scripts, are also output. Explicit implementation of trace instructions, e.g. for output of the tag values, enables the tracing of script execution and of the functions called within those scripts. You enter the trace instruction in the form "HMIRuntime.Trace(&lt;Output&gt;)". Error situations which result in calling of the OnErrorExecute function are also displayed in the diagnostic window.

##### GSC diagnosis of C

GSC diagnosis outputs the printf methods contained in the local scripts in chronological order of their being called. printf instructions in user-defined C functions, which are called in local scripts, are also output. By targeted use of printf instructions, e.g. for outputting tag values, the sequence of scripts and the functions called in them can be tracked.

---

**See also**

[GSC diagnostics (RT Professional)](#gsc-diagnostics-rt-professional)
  
[Inserting a GSC diagnostics window in a screen (RT Professional)](#inserting-a-gsc-diagnostics-window-in-a-screen-rt-professional)
  
[Example of configuring a diagnostics output via a trace (RT Professional)](#example-of-configuring-a-diagnostics-output-via-a-trace-rt-professional)

#### GSC diagnostics (RT Professional)

##### Introduction

GSC Diagnostics outputs the trace instructions of the scripts to the diagnostics view in the chronological order of their call. The application also outputs trace instructions in functions which are called in the scripts. Explicit implementation of trace instructions, e.g. for output of the tag values, enables the tracing of script execution and of the functions called within those scripts.

##### Application

Insert the "Print job/Script diagnostics" object of the type GSC Diagnostics in a screen to enable the use of GSC Diagnostics. Control the appearance of the GSC Diagnostics window by means of the GSC Diagnostics properties.

In the case of a picture change, the content of the GSC Diagnostics window is deleted.

> **Note**
>
> Messages are also displayed in the "GSC Diagnostics" window when the debugger is activated.

---

**See also**

[Diagnostics (RT Professional)](#diagnostics-rt-professional-1)

#### Inserting a GSC diagnostics window in a screen  (RT Professional)

##### Introduction

To use the GSC Diagnostics, you insert the "Print job/Script diagnostics" object in a screen. Use either any existing screen, or create a screen that is dedicated to diagnostics functions. In the Inspector window of the "Print job/Script diagnostics" object, you specify that the object is used for GSC Diagnostics.

##### Requirement

- The required screen is open.
- The "Tools" task card is open.

##### Procedure

Proceed as follows to insert the GSC diagnostics window:

1. Insert the "Print job/Script diagnostics" object from the "Controls" palette of the "Tools" task card into the screen.
2. Assign a name to the GSC diagnostics window at "Miscellaneous &gt; Name".
3. Select the "Functions" option in the inspector window under "Properties &gt; Properties &gt; General &gt; Content &gt; Window content".
4. Select the "GSC diagnostics" option under "Template".
5. Specify the further settings for the GSC diagnostics window under "General", "Layout", and "Miscellaneous".

---

**See also**

[Diagnostics (RT Professional)](#diagnostics-rt-professional-1)

## Runtime behavior in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Executing user-defined functions in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-user-defined-functions-in-runtime-panels-comfort-panels-rt-advanced-rt-professional)
- [Executing a function list in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#executing-a-function-list-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Execution of functions and local scripts in Runtime (RT Professional)](#execution-of-functions-and-local-scripts-in-runtime-rt-professional)
- [Processing sequence for user-defined functions and system functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#processing-sequence-for-user-defined-functions-and-system-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [Making object properties dynamic in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)](#making-object-properties-dynamic-in-runtime-panels-comfort-panels-rt-advanced-rt-professional)

### Executing user-defined functions in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Principle

Only one user-defined function at a time is executed in Runtime. If several user-defined functions are waiting to be executed, they are lined up in a queue and executed one after the other.

> **Note**
>
> A loop in a user-defined function therefore blocks the execution of the other functions in the queue even if the functions were initiated asynchronously.

WinCC supports a maximum nesting depth of eight user-defined functions. Note that the nesting depth is not checked.

> **Note**
>
> If a user-defined function is configured for the "Runtime stop" event, the only system functions that may be used in this user-defined function are those which are available at the "Runtime stop" event.
>
> Ensure that the ending of the Runtime is not interfered with by the execution of the user-defined function.

> **Note**
>
> **Configuration of user-defined functions**
>
> During configuration make sure that not too many user-defined functions are activated at the same time. Avoid a continuous system load of 100%.
>
> User-defined functions are processed at a lower priority so as not to interfere with the display of values and operability. If system utilization is extreme, the user-defined functions to be executed are therefore first only reserved for execution. The maximum size of the reservation list is dependent on the HMI device and is limited by the maximum permitted number of user-defined functions. For additional information, see the performance features. If more user-defined functions are activated at one time than can be reserved, excess calls are discarded and a system alarm displayed.

#### HMI device changeover

If you use system functions in a customized function which are not available on the set HMI device, you get a warning. In addition, the corresponding system function in the user-defined function will be underlined with a wavy blue line.

---

**See also**

[User-defined functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-defined-functions-panels-comfort-panels-rt-advanced-rt-professional)

### Executing a function list in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Principle

A function list is executed from top to bottom in Runtime. A distinction is made between synchronous and asynchronous execution, so that no waiting periods ensue during execution. The distinction is made by the system by evaluating the different runtimes of the system functions. User-defined functions are always executed synchronously independent of the runtime. If a system function returns an error status, the execution of the function list is cancelled.

#### Synchronous execution

During synchronous execution, the system functions in a function list are executed one after the other. The previous system function must be finished before the next system function can be executed.

#### Asynchronous execution

System functions that perform file operations such as saving and reading have a longer runtime than system functions that, for example, set a tag value.

Therefore, system functions with longer runtimes are executed asynchronously. For example, while a system function is writing a recipe data record to a storage medium, the next system function is already being executed. Due to the parallel execution of system functions, waiting periods at the HMI device are avoided.

### Execution of functions and local scripts in Runtime (RT Professional)

#### Processing local scripts in Runtime

Two locale scripts of the same type cannot be executed simultaneously in Runtime. Event-triggered and cyclic/tag-triggered scripts in screens are executed separately to prevent any script from interfering with cyclic scripts.

> **Note**
>
> The script types in WinCC are synchronized exclusively by the DataSet object or internal HMI tags. Separate execution prevents the generation of any shared data areas for event-triggered and cyclic/tag-triggered scripts.

If high system load or other scripts interfere with cyclic execution of local scripts in the screens, the local script is executed once at the next opportunity. Cycles which are not executed are not retained in a queue but rejected.

After a screen change any active scripts are stopped automatically on expiration of 1 minute.

Local scripts which are still active at the end of Runtime are stopped after 5 seconds.

#### Executing functions in Runtime

Functions are executed successively in Runtime after being triggered. If a function is initiated while another is active, the second function is queued until it can be executed.

> **Note**
>
> The local scripts and functions are synchronized exclusively by the DataSet object or internal HMI tags. Local scripts and functions do not share any data areas.

---

**See also**

[User-defined functions (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-defined-functions-panels-comfort-panels-rt-advanced-rt-professional)
  
[Local scripts (RT Professional)](#local-scripts-rt-professional)

### Processing sequence for user-defined functions and system functions (Panels, Comfort Panels, RT Advanced, RT Professional)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Adherence to the expected processing sequence for user-defined functions and system functions in Runtime cannot always be guaranteed. This fact may lead to unexpected operating states.  Please note the following description in which the correlations are explained. Instructions for a solution are available under "Remedy". |  |

#### Use of user-defined functions for events

It is not always possible to adhere to the processing sequence for user-defined functions and system functions expected in the configuration, for example, when the processing of a user-defined function lasts beyond the trigger time of a subsequent event. In this case, system functions that are configured for the following event may be executed before the system functions that were configured with the user-defined function for the same event.

#### Background

User-defined functions are arranged in a low-priority queue. The queue is processed in sequence. If system functions and user-defined functions are configured for an event, all system functions and user-defined functions configured for this event are executed in this queue.

#### Example

On a button, you have configured:

|  | Event | Functions |
| --- | --- | --- |
| ![Example](images/36120439563_DV_resource.Stream@PNG-de-DE.png) | Press | User-defined function (1)  SetBit(Tag) (2) |
| ![Example](images/36120447243_DV_resource.Stream@PNG-de-DE.png) | Release | ResetBit(Tag) (3) |

![Example](images/36120454923_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| (1) | Execution time of the user-defined function |
| (2) | Execution time of system function SetBit(Tag) |
| (3) | Execution time of system function ResetBit(Tag) |

A: Expected execution of the user-defined function and system functions in the configuration.

When you press the button, user-defined function (1) and then system function SetBit(Tag) (2) are executed. When you release the key, system function ResetBit(Tag) (3) is then executed.

B: Processing of the user-defined function is not yet complete when you release the key.

When you press the key, the user-defined function (1) is then executed. The execution of the user-defined function (1) is not yet complete and you have already released the key. System function ResetBit(Tag) (3) interrupts the execution of the function. In this case, system function ResetBit(Tag) (3) is executed before system function SetBit(Tag) (2). As a result, the bit remains placed.

System function "SetBitWhileKeyPressed" shows the same behavior, if the system function is configured together with user-defined functions.

#### Remedy

The processing sequence of the previous Example A is adhered to, if you additionally configure a user-defined function for the "Release" event. The user-defined function does not require functionality for this purpose.

|  | Event | Functions |
| --- | --- | --- |
| ![Remedy](images/36120439563_DV_resource.Stream@PNG-de-DE.png) | Press | User-defined function (1)  SetBit(Tag) (2) |
| ![Remedy](images/36120447243_DV_resource.Stream@PNG-de-DE.png) | Release | User-defined function_2 (3)  ResetBit(Tag) (4) |

> **Note**
>
> Make sure that the user-defined function queue does not overflow; otherwise the system function for the following event may not be executed.
>
> An overflow is recognizable by "Overload: Script &lt;name&gt; is rejected" or "Adherence to the expected processing order for user-defined functions and system functions in Runtime cannot always be ensured".

### Making object properties dynamic in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can use user-defined functions to access object properties of screen objects as well as tags in Runtime. If you use a user-defined function to change values of object properties, this will not affect the project data.

#### Changes to object properties

If you use a user-defined function in Runtime to change an object property of a screen element, this change will only remain effective while the screen is active. If you change to the screen, or reload the screen, the configured object properties are displayed once more.

#### Language switching

If you switch the language in Runtime, the foreign language labels are loaded from the project data. If you use a user-defined function to change texts, the texts changed by the user-defined function are overwritten again.

## Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Examples of VBS (Panels, Comfort Panels, RT Advanced)](#examples-of-vbs-panels-comfort-panels-rt-advanced)
- [Examples of VBS (RT Professional)](#examples-of-vbs-rt-professional)
- [Examples of C (RT Professional)](#examples-of-c-rt-professional)

### Examples of VBS (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Example: Converting Fahrenheit into degrees Celsius (Panels, Comfort Panels, RT Advanced)](#example-converting-fahrenheit-into-degrees-celsius-panels-comfort-panels-rt-advanced)
- [Example: Converting inches into meters (Panels, Comfort Panels, RT Advanced)](#example-converting-inches-into-meters-panels-comfort-panels-rt-advanced)
- [Example: Changing the operating mode on the HMI device with the current display (Panels, Comfort Panels, RT Advanced)](#example-changing-the-operating-mode-on-the-hmi-device-with-the-current-display-panels-comfort-panels-rt-advanced)

#### Example: Converting Fahrenheit into degrees Celsius (Panels, Comfort Panels, RT Advanced)

##### Scheduled task

In this example, create a user-defined VB function which converts the values of a temperature sensor from Fahrenheit to degrees Celsius. The temperature is displayed in an output field on the HMI device.

##### Settings

For the example you need two HMI tags and a user-defined VB function with the following settings:

HMI tags:

| Name | PLC connection | Type |
| --- | --- | --- |
| Fahrenheit | Yes | Real |
| Centigrade | No | Real |

User-defined VB function:

| Name | Type | Parameters |
| --- | --- | --- |
| FahrenheitToCelsius | Function | Fahrenheit |

##### Procedure

1. Create the two HMI-tags "Fahrenheit" and "Celsius" with the settings named above.

   ![Procedure](images/36120537355_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36120537355_DV_resource.Stream@PNG-en-US.png)
2. Create the user-defined VB function "FahrenheitToCelsius" with the settings given above.

   ![Procedure](images/36120563595_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36120563595_DV_resource.Stream@PNG-en-US.png)
3. Write the following VBS code:

   `FahrenheitToCelsius = (Fahrenheit-32) * (5/9)`

   ![Procedure](images/36120589835_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/36120589835_DV_resource.Stream@PNG-de-DE.png)

##### Interim result

The HMI tags and the VB user-defined function are created.

##### Procedure

1. Open the "HMI Tag"editor and click on the "Fahrenheit" tag.
2. Click the "Properties &gt; Events" tab in the Inspector window. Select the "Value change" event.
3. Configure the user-defined VB function "FahrenheitToCelsius" to the "Value change" event.
4. Select the tag "Fahrenheit" for the parameter "Fahrenheit".
5. Select the HMI-tag "Celsius" for the return value "Fahrenheit to Celsius".
6. Configure an output field in a screen and connect it with the tag "Celsius".

##### Alternative procedure

Instead of using a user-defined VB function of the "Function" type, you can also use the "Sub" type. In this case, assign the converted value directly to the HMI-tag "Celsius".

`SmartTags("Celsius") = (Fahrenheit-32) * (5/9)`

In this case the return value of the user-defined VB function is not applicable.

##### Result

When the tag value of "Fahrenheit" changes in Runtime, the user-defined VB function "Fahrenheit to Celsius" is performed. The converted temperature value is returned to the HMI-tag "Celsius" and displayed in the output field.

#### Example: Converting inches into meters (Panels, Comfort Panels, RT Advanced)

##### Scheduled task

In this example you create a user-defined VB function that converts the value of a length measuring system from inches into meters. The length in meters is displayed on the HMI device in an output field.

##### Settings

For the example you need two HMI tags and a user-defined VB function with the following settings:

HMI tags:

| Name | PLC connection | Type |
| --- | --- | --- |
| VarInch | Yes | Real |
| VarMeter | No | Real |

Customized VB function

| Name | Type | Parameters |
| --- | --- | --- |
| InchToMeter | Sub | Inch |

##### Procedure

1. Create the two HMI tags "VarInch" and "VarMeter" with the above settings.

   ![Procedure](images/36120610443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36120610443_DV_resource.Stream@PNG-en-US.png)
2. Create the user-defined VB function "InchToMeter" with the settings given above.

   ![Procedure](images/36120636683_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36120636683_DV_resource.Stream@PNG-en-US.png)
3. Write the following VBS code:

   `VarMeter = Inch*0.0254`

   ![Procedure](images/36120650123_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/36120650123_DV_resource.Stream@PNG-de-DE.png)

##### Interim result

The tags and the user-defined VB function are created.

##### Procedure

1. Open the "HMI tags" editor and click the "VarInch" tag.
2. Click "Properties&gt; Events" in the Inspector window. Select the "Value change" event.
3. Configure the user-defined VB function "InchToMeter" to the "Value change" event.
4. Select the "VarInch" HMI tag for the "Inch" parameter.
5. Configure an output field in a screen and connect it with the "VarMeter" HMI tag.

##### Result

When the tag value of "VarInch" changes in Runtime, the "InchToMeter" user-defined VB function is performed. The calculated value is written into the "VarMeter" HMI tag and displayed in the output field.

#### Example: Changing the operating mode on the HMI device with the current display (Panels, Comfort Panels, RT Advanced)

##### Scheduled task

In this example, you use the "SetDeviceMode" system function to switch between the "online" and "offline" modes on the HMI device. You also display the current set operating mode on the HMI device.

##### Requirements

A screen has been created.

##### Settings

For this example you require a HMI-tag and a text list with the following settings:

HMI tag:

| Name | PLC connection | Type |
| --- | --- | --- |
| OperatingMode | No | Bool |

Text list:

| Name | Contains | Values |
| --- | --- | --- |
| ShowOperatingMode | Bit (0/1) | 1: Operating mode: "Online"  0: Operating mode: "Offline" |

##### Procedure

1. Create the "OperatingMode" HMI-tag indicated above.

   ![Procedure](images/36120672395_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/36120672395_DV_resource.Stream@PNG-en-US.png)
2. Create the "ShowOperatingMode" text list indicated above.

   ![Procedure](images/70594956299_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70594956299_DV_resource.Stream@PNG-en-US.png)
3. Open the screen and insert a button for which you configure the operating mode change to "online".
4. Click "Properties&gt; Events" in the Inspector window. Select the "Press" event.
5. Configure the "SetDeviceMode" system function for the "Press" event. The system function is found in the selection list under "Settings".
6. For the "Mode" parameter, select the "Online" entry.
7. Configure the system function "SetBit" on the event "Press". The system function is found in the selection list under "Bit processing".
8. Select the HMI-tag "Operating mode" from the selection list for the parameter "Tag".

   ![Procedure](images/70594976139_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70594976139_DV_resource.Stream@PNG-en-US.png)
9. Add a button in the process screen for which you configure the operating mode change to "offline".
10. Repeat steps four to seven. For the "Mode" parameter, select the "Offline" entry. Configure the system function "ResetBit" in place of the system function "SetBit."

    ![Procedure](images/70596160779_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/70596160779_DV_resource.Stream@PNG-en-US.png)

##### Interim result

You can toggle the operating mode of the HMI device with the two buttons in Runtime.

You want to display the current set operating mode in an output field on the HMI device.

##### Procedure

1. Create a "Symbolic I/O field" in the process image. Click "Properties &gt; Properties" in the Inspector window.
2. Make the following settings in the "General" group:

   - Select "Output" as the "Mode".
   - Select the text list "Show operating mode" as "Text list".
   - Select "Operating mode" as "Tag".

     ![Procedure](images/70598753419_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/70598753419_DV_resource.Stream@PNG-en-US.png)

##### Result

When you change the operating mode with the buttons, the currently set operating mode on the HMI device is always shown.

---

**See also**

[Configuring a function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Examples of VBS (RT Professional)

This section contains information on the following topics:

- [Overview (RT Professional)](#overview-rt-professional)
- [Example of accessing objects in the Screens editor (RT Professional)](#example-of-accessing-objects-in-the-screens-editor-rt-professional)
- [Example of defining object colors (RT Professional)](#example-of-defining-object-colors-rt-professional)
- [Example of configuring a language switch (RT Professional)](#example-of-configuring-a-language-switch-rt-professional)
- [Example of deactivating Runtime (RT Professional)](#example-of-deactivating-runtime-rt-professional)
- [Example of configuring a screen change via a property (RT Professional)](#example-of-configuring-a-screen-change-via-a-property-rt-professional)
- [Example of configuring a diagnostics output via a trace (RT Professional)](#example-of-configuring-a-diagnostics-output-via-a-trace-rt-professional)
- [Example of writing tag values (RT Professional)](#example-of-writing-tag-values-rt-professional)
- [Example of reading tag values (RT Professional)](#example-of-reading-tag-values-rt-professional)
- [Example of writing object properties (RT Professional)](#example-of-writing-object-properties-rt-professional)
- [Example of configuring the recipe view (RT Professional)](#example-of-configuring-the-recipe-view-rt-professional)
- [Example of configuring the alarm view (RT Professional)](#example-of-configuring-the-alarm-view-rt-professional)
- [Example of statistically evaluating tag values (RT Professional)](#example-of-statistically-evaluating-tag-values-rt-professional)
- [Example of the start of a script at the server (Logging object) (RT Professional)](#example-of-the-start-of-a-script-at-the-server-logging-object-rt-professional)
- [Example for opening the PLC code view from the GRAPH overview (RT Professional)](#example-for-opening-the-plc-code-view-from-the-graph-overview-rt-professional)
- [Example of deleting the browser cache (RT Professional)](#example-of-deleting-the-browser-cache-rt-professional)

#### Overview (RT Professional)

##### Introduction

You can find the following examples for VBS:

- Access to objects in the "Screens" editor (e.g., color or text change)
- Determining color of objects
- Configuring a language switch
- Deactivating Runtime
- Configuring a screen change via a property
- Configuring diagnostic output via a trace
- Writing tag values
- Reading tag values
- Writing object properties
- Configuring a recipe view
- Configuring an alarm view
- Drawing a trend
- Evaluating tag values statistically
- Deleting the browser cache

---

**See also**

[Example of accessing objects in the Screens editor (RT Professional)](#example-of-accessing-objects-in-the-screens-editor-rt-professional)
  
[Example of defining object colors (RT Professional)](#example-of-defining-object-colors-rt-professional)
  
[Example of configuring a language switch (RT Professional)](#example-of-configuring-a-language-switch-rt-professional)
  
[Example of deactivating Runtime (RT Professional)](#example-of-deactivating-runtime-rt-professional)
  
[Example of configuring a screen change via a property (RT Professional)](#example-of-configuring-a-screen-change-via-a-property-rt-professional)
  
[Example of configuring a diagnostics output via a trace (RT Professional)](#example-of-configuring-a-diagnostics-output-via-a-trace-rt-professional)
  
[Example of writing tag values (RT Professional)](#example-of-writing-tag-values-rt-professional)
  
[Example of reading tag values (RT Professional)](#example-of-reading-tag-values-rt-professional)
  
[Example of writing object properties (RT Professional)](#example-of-writing-object-properties-rt-professional)
  
[Example of configuring the recipe view (RT Professional)](#example-of-configuring-the-recipe-view-rt-professional)
  
[Example of configuring the alarm view (RT Professional)](#example-of-configuring-the-alarm-view-rt-professional)
  
[Example of statistically evaluating tag values (RT Professional)](#example-of-statistically-evaluating-tag-values-rt-professional)
  
[Example of deleting the browser cache (RT Professional)](#example-of-deleting-the-browser-cache-rt-professional)

#### Example of accessing objects in the Screens editor (RT Professional)

##### Introduction

To make the graphic Runtime environment dynamic, you can use VBS scripting to access all objects in the "Screens" editor in WinCC. In doing so, you can make graphic objects dynamic in response to an operator input, e.g., in response to a mouse click or depending on tag values.

##### Procedure

In the following example, the radius of a circle is set to 20 in Runtime per mouse click:

'VBS121

Dim objCircle

Set objCircle= ScreenItems("Circle1")

objCircle.Radius = 20

---

**See also**

[Overview (RT Professional)](#overview-rt-professional)

#### Example of defining object colors (RT Professional)

##### Introduction

The object colors are defined by means of RGB values (Red/Green/Blue). The color values for graphic objects can be set or read.

##### Procedure

The following example defines the fill color for "ScreenWindow1" to blue:

'VBS122

Dim objScreen

Set objScreen = HMIRuntime.Screens("ScreenWindow1")

objScreen.FillColor = RGB(0, 0, 255)

---

**See also**

[Screens (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of configuring a language switch (RT Professional)

##### Introduction

The Runtime language can be changed by means of VBS. Use buttons with corresponding country markings that you place on the start page of your project.

Using VBS, define the Runtime language by means of country code, e.g., 1031 for German - Default, 1033 for English - USA, etc. An overview of all country codes is available in the Basics of VBScript, "Regional Scheme ID (LCID) Diagram".

##### Procedure

Configure a local VBS script for a "Mouse click" event on a button and enter the following code to change the Runtime language to German:

'VBS123

HMIRuntime.Language = 1031

---

**See also**

[Language (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#language-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of deactivating Runtime (RT Professional)

##### Introduction

You can use VBS to exit Runtime, e.g. by means of mouse click, or depending on tag values, or on other events.

##### Procedure

The following example terminates WinCC Runtime:

'VBS124

HMIRuntime.Stop

---

**See also**

[Stop (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#stop-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of configuring a screen change via a property (RT Professional)

##### Introduction

If using split screens in your configuration, e.g. the title and operating bar for the user interface in a basic screen and an embedded screen window for the actual screen display, configure a screen change using the properties of the screen window.

The property of screen window "ScreenName" must be changed so that the other screen is displayed. The local script and the screen window must be configured in the same screen.

##### Procedure

In the following example you show the "test" screen in a "ScreenWindow" when executing the local VB script:

'VBS126

Dim objScrWindow

Set objScrWindow = ScreenItems("ScreenWindow")

objScrWindow.ScreenName = "test"

---

**See also**

[ScreenName (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#screenname-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of configuring a diagnostics output via a trace (RT Professional)

##### Introduction

If you have inserted the Print job/Script diagnostics" object in your screen, you can use the trace command to display diagnostics outputs in the diagnostics window in Runtime.

Print job/Script diagnostics returns the trace methods contained in the user-defined functions in the order in which they were called. This also applies to trace instructions in functions that are called in user-defined functions. The targeted use of trace instructions allows you to trace the flow of user-defined functions and the functions called therein. You enter the trace instruction in the form "HMIRuntime.Trace&lt;Output&gt;".

The "Print job/Script diagnostics" object displays trace outputs from C and VBS.

##### Outputting text

The following example writes a text in the diagnostics window:

'VBS127

HMIRuntime.Trace "Customized error message"

##### Outputting alarms

The following example writes the alarms of a "Control2" alarm view to the diagnostics window:

Sub TraceMsg

Dim objAlarmControl

Dim lIndex

Dim lCellIndex

'create reference to the alarm control

Set objAlarmControl = ScreenItems("Control2")

'enumerate and trace out row numbers

For lIndex = 1 To objAlarmControl.GetRowCollection.Count

HMIRuntime.Trace "Row: " &amp; (objAlarmControl.GetRow(lIndex).RowNumber) &amp; " "

'enumerate and trace out column titles and cell texts

For lCellIndex = 1 To objAlarmControl.GetRow(lIndex).CellCount

HMIRuntime.Trace objAlarmControl.GetMessageColumn(lCellIndex -1).Name &amp; " "

HMIRuntime.Trace objAlarmControl.GetRow(lIndex).CellText(lCellIndex) &amp; " "

Next

HMIRuntime.Trace vbNewLine

Next

End Sub

##### Output information about HMI tags

The following example uses the "VarArch100" log tag to write information to the diagnostics window:

Sub ReadTagInfo

Dim Tag

Set Tag = HMIRuntime.Tags("TagLoggingfast\VarArch100")

HMIRuntime.Trace "Last Error = " + CStr(Tag.LastError) + vbNewLine

HMIRuntime.Trace "Name = " + Tag.Name + vbNewLine

HMIRuntime.Trace "QualityCode = " + CStr(Tag.QualityCode) + vbNewLine

End Sub

---

**See also**

[Trace (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#trace-panels-comfort-panels-rt-advanced-rt-professional)
  
[Diagnostics (RT Professional)](#diagnostics-rt-professional-1)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of writing tag values (RT Professional)

##### Introduction

You can use VBScript to write the tag value to the PLC, for example, by mouse click on a setpoint button or to set internal tag values for triggering other user-defined functions.

Various write variations are mentioned and explained below.

##### Simple writing

In the following example, a value is written to the "Tag1" tag:

'VBS128

HMIRuntime.Tags("Tag1").Write 6

This is the simplest form of writing since no object reference is generated.

##### Writing with object reference

In the following example, a local copy of the tag object is generated and a value is written to "Tag1":

'VBS129

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Write 7

Referencing offers the advantage of being able to work with the tag object before writing. You can read the tag value, perform calculations, and write the tag value again.

'VBS130

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Read

objTag.Value = objTag.Value + 1

objTag.Write

##### Synchronous writing

The value to be written is usually transferred to tag management and execution of the script is continued. In certain cases, however, it must be ensured that the value has actually been written before script execution continues.

This type of writing is realized by specifying the value 1 for the additional, optional parameters:

'VBS131

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Write 8.1

or

'VBS132

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Value = 8

objTag.Write ,1

> **Note**
>
> Note that the call takes longer in comparison to the standard call. The duration is also dependent on the channel and AS, among other things.
>
> This type of writing corresponds to the SetTagXXXWait() call in C scripting.

##### Writing with status handling

In order to ensure that a value has been written successfully, you perform an error check or evaluate the tag status after the write operation was completed.

This is done by checking the value of the LastError property after writing. The tag status is checked if the check was completed successfully, i.e., if the job was successfully output.

In the case of a write job, the current status from the process is not determined. To determine this, it is necessary to read the tag. The value specified in the QualityCode property after the read process provides an indication of the tag status and, if necessary, makes reference to a failed AS connection.

In the following example, the "Tag1" tag is written. If an error occurs during writing, the error value and error description appear in the Global Script diagnostics window. Finally, the QualityCode is checked. If the QualityCode is not OK (0x80), it will be displayed in the diagnostics window.

'VBS133

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Write 9

If 0 &lt;&gt; objTag.LastError Then

HMIRuntime.Trace "Error: " &amp; objTag.LastError &amp; vbCrLf &amp; "ErrorDescription: " &amp; objTag.ErrorDescription &amp; vbCrLf

Else

objTag.Read

If &amp;H80 &lt;&gt; objTag.QualityCode Then

HMIRuntime.Trace "QualityCode: 0x" &amp; Hex(objTag.QualityCode) &amp; vbCrLf

End If

End If

> **Note**
>
> After writing a tag, the QualityCode property of the local tag object is set to "BAD Out of Service" because it is not known which QualityCode the tag handles in the process. The new QualityCode can be determined by reading again.
>
> The Quality Code cannot be written from VBS.

---

**See also**

[Tags (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[Trace (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#trace-panels-comfort-panels-rt-advanced-rt-professional)
  
[Read (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#read-panels-comfort-panels-rt-advanced-rt-professional)
  
[Value (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#value-panels-comfort-panels-rt-advanced-rt-professional)
  
[Write (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#write-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of reading tag values (RT Professional)

##### Introduction

VBS can be used to read and further process a tag value. This allows you to click a button, for example, to obtain information on the system status or to perform calculations.

Various read variations are mentioned and explained below.

##### Simple reading

In the following example, the value of "Tag1" is read and displayed in the Global Script diagnostics window:

'VBS134

HMIRuntime.Trace "Value: " &amp; HMIRuntime.Tags("Tag1").Read &amp; vbCrLf

This is the simplest form of reading since no object reference is generated.

##### Reading with object reference

In the following example, a local copy of the tag object is created, and the tag value is read and displayed in the "Print job/Script diagnostics" object:

'VBS135

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

HMIRuntime.Trace "Value: " &amp; objTag.Read &amp; vbCrLf

Referencing offers the advantage of being able to work with the tag object. You can read the tag value, perform calculations, and write the tag value again.

'VBS136

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Read

objTag.Value = objTag.Value + 1

objTag.Write

Using the Read method, process tags that have been read are added to the image, from this moment on they are cyclically requested from the automation system (AS). If the tag is already in the image, the value it contains is returned.

When the screen is exited, the tags are logged off.

> **Note**
>
> If a tag is requested in a function, it remains logged on as long as WinCC Runtime is running.

##### Direct reading

Normally, the tag values are read from the tag image. In certain situations, however, it may be necessary to read the value directly from the AS, e.g., to synchronize fast processes.

The tag is not logged on cyclically if you set the optional parameter to 1 when reading the value. Instead, the value is requested once from the AS.

'VBS137

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

HMIRuntime.Trace "Value: " &amp; objTag.Read(1) &amp; vbCrLf

> **Note**
>
> Note that the call takes longer in comparison to the standard call. The duration is also dependent on the channel and AS, among other things.
>
> This type of call must be avoided in cyclic C scripts as this is the major cause of performance problems.
>
> This read mode corresponds to the GetTagXXXWait() call used in C scripting.

##### Reading with status handling

Always validate the value after reading it. This occurs by checking the QualityCode.

In the following example, the "Tag1" tag is read and the QualityCode then checked. When the Quality Code does not correspond to OK (0x80) the LastError, ErrorDescription, and QualityCode properties are displayed in the Global Script diagnostics window.

'VBS138

Dim objTag

Set objTag = HMIRuntime.Tags("Tag1")

objTag.Read

If &amp;H80 &lt;&gt; objTag.QualityCode

  Then

    HMIRuntime.Trace "Error: " &amp; objTag.LastError &amp; vbCrLf &amp; "ErrorDescription: " &amp; objTag.ErrorDescription &amp; vbCrLf &amp; "QualityCode: 0x" &amp; Hex(objTag.QualityCode) &amp; vbCrLf

  Else

    HMIRuntime.Trace "Value: " &amp; objTag.Value &amp; vbCrLf

End If

> **Note**
>
> If an error occurs during reading, QualityCode is set to BAD Out of Service". Therefore, it is sufficient to check the QualityCode following reading.

---

**See also**

[Tags (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[Read (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#read-panels-comfort-panels-rt-advanced-rt-professional)
  
[Trace (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#trace-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of writing object properties (RT Professional)

##### Introduction

VBS provides access to the properties of all display and operating objects in the "Screens" editor. You can read out properties or change them during Runtime.

The following examples illustrate various forms of access.

##### Simple setting of a property

In the next example, the background color of the "Rectangle1" object in the screen is set to red:

'VBS139

ScreenItems("Rectangle1").BackColor = RGB(255,0,0)

This is the simplest form of writing since no object reference is generated.

> **Note**
>
> If you are working without an object reference, only the standard properties are provided by autocompletion.
>
> The mode of expression used in this example can only be executed in the "Screens" editor. By analogy, you address the objects in the scheduler using the HMIRuntime object.

##### Setting a property with object reference

In the following example, a reference is created to the "Rectangle1" object contained in the picture and the background is set to red using the VBS standard function RGB():

'VBS140

Dim objRectangle

Set objRectangle = ScreenItems("Rectangle1")

objRectangle.BackColor = RGB(255,0,0)

Additional information on RGB is available in "VBScript for Windows".

Referencing is useful if you want to edit several object properties. In this way all of the properties of the object will be listed with the autocompletion feature.

> **Note**
>
> The mode of expression used in this example can only be executed in the "Screens" editor. By analogy, you address the objects in the scheduler using the HMIRuntime object.

##### Setting properties across screen windows

VBS in the "Screens" editor offers two options of global screen addressing:

- Using the screen object of a screen window with "ScreenItems"
- From the root screen with "HMIRuntime.Screens"

##### Referencing via the screen window

In the following example, the color of a rectangle is changed in an subordinate screen window. The user-defined VB function is executed in the "BaseScreen" screen in which "ScreenWindow1" is located. The screen window displays a screen, which contains an object of the type "Rectangle" with the name "Rectangle1".

'VBS199

Sub OnLButtonUp(ByVal Item, ByVal Flags, ByVal x, ByVal y)

  Dim objRectangle

  Set objRectangle = ScreenItems("ScreenWindow1").Screen.ScreenItems("Rectangle1")

  objRectangle.BackColor = RGB(255,0,0)

End Sub

##### Referencing from the root screen

You can reference the screen with the object to be modified via HMIRuntime.Screens. The specification of the screen is defined relative to the root screen via the following access code:

[&lt;Root screen name&gt;.]&lt;Screen window name&gt;[:&lt;Screen name&gt;]... .&lt;Screen window name&gt;[:&lt;Screen name&gt;]

In the following example, a reference is created to the "Screen2" object contained in the "Rectangle1" picture and the background color is set to red.

The screen "Screen2", in this case, is in "Screen1". "Screen1" is displayed in the "BaseScreen" root screen.

'VBS141

Dim objRectangle

Set objRectangle = HMIRuntime.Screens("BaseScreen.ScreenWindow1:Screen1.ScreenWindow1:Screen2").ScreenItems("Rectangle1")

objRectangle.BackColor = RGB(255,0,0)

It is not necessary to specify the screen name. It is possible to address a screen uniquely using the screen window name. Therefore, it is sufficient to specify the name of the screen window, as in the following example:

'VBS142

Dim objRectangle

Set objRectangle = HMIRuntime.Screens("ScreenWindow1.ScreenWindow2").ScreenItems("Rectangle1")

objRectangle.BackColor = RGB(255,0,0)

This type of addressing enables objects in screen windows to be addressed in different pictures. This is a particularly interesting aspect for the faceplate system.

##### Making the property dynamic using the return value

In addition to initiating local scripts for properties by means of an event trigger or cyclic trigger, you can also make properties dynamic directly by means of a local script.

In the next example, the background color of an object made dynamic by means of return value. The value transferred can be derived from the evaluation of events in the PLC, for example, and can be used for graphic visualization of an operating state:

'VBS146

Function BackColor_Trigger(ByVal Item)

BackColor_Trigger = RGB(125,0,0)

End Function

> **Note**
>
> If you use a user-defined function to make an object property dynamic by means of the return value of a user-defined function, the value of the object property is only written if it has changed compared to the last function session. It is not considered if the value had been changed from another location.
>
> For this reason, properties that have been made dynamic by means of the return value with user-defined functions must not be changed from another location (e.g. other user-defined functions). Incorrect values could be displayed if you ignore this rule.

---

**See also**

[BackColor (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#backcolor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of configuring the recipe view (RT Professional)

##### Introduction

Recipe data records are output in the recipe view.

You can add, copy, edit or delete data records.

##### Loading and displaying a recipe

The following example loads the "Juice" recipe in the "Control1" recipe view. The recipe is displayed in the recipe view.

Sub loadUserArchive()

Dim objUAC

Set objUAC = ScreenItems("Control1")

objUAC.BorderColor = RGB(255,0,0)

objUAC.BorderWidth = 3

objUAC.Closeable = False

objUAC.Datasource = "Juice"

End Sub

##### Copying a recipe data record

The following example copies the recipe data record of line 3. The copy is inserted at the end of the table.

Sub CopyRow

Dim objUAC

Set objUAC = ScreenItems("Control1")

Dim iRowCount

objUAC.AutoCompleteRows = True

objUAC.SelectRow(3)

objUAC.CopyRows

iRowCount = objUAC.GetRowCollection.Count

objUAC.SelectRow(iRowCount + 1)

objUAC.PasteRows

objUAC.SelectRow(1)

objUAC.UnselectAll

End Sub

---

**See also**

[PasteRows   (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#pasterows-panels-comfort-panels-rt-advanced-rt-professional)
  
[SelectRow (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#selectrow-panels-comfort-panels-rt-advanced-rt-professional)
  
[UnselectAll (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#unselectall-panels-comfort-panels-rt-advanced-rt-professional)
  
[BorderColor (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#bordercolor-panels-comfort-panels-rt-advanced-rt-professional)
  
[BorderWidth (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#borderwidth-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of configuring the alarm view (RT Professional)

##### Introduction

The alarm view displays alarms. You can show, hide, sort, and filter alarms.

##### Filtering alarms

In this example, only the alarms of alarm number 2 are displayed in the "Control2" alarm view.

Sub Filter

Dim objAlarmControl

'create reference to AlarmControl

Set objAlarmControl = ScreenItems("Control2")

'set / reset the filter and create a trace

If (objAlarmControl.MsgFilterSQL = "") Then

objAlarmControl.MsgFilterSQL = "MSGNR = 2"

Else

objAlarmControl.MsgFilterSQL = ""

End If

End Sub

##### Removing alarms

In this example, alarms 1-3 will be removed from the alarm view.

Sub ResetAlarm

Dim objAlarm

'reset alarm 1 - 3

Set objAlarm = HMIRuntime.Alarms(1)

objAlarm.State = 2 'hmiAlarmStateGone

objAlarm.Create

Set objAlarm = HMIRuntime.Alarms(2)

objAlarm.State = 2 'hmiAlarmStateGone

objAlarm.Create

Set objAlarm = HMIRuntime.Alarms(3)

objAlarm.State = 2 'hmiAlarmStateGone

objAlarm.Create

End Sub

##### Adding alarms

In this example, alarms 1-3 will be added to the alarm view. Alarms 1-3 must be created.

Sub SetAlarm

Dim objAlarm

'create Alarm 1 - 3

Set objAlarm = HMIRuntime.Alarms(1)

objAlarm.State = 1 'hmiAlarmStateCome

objAlarm.Create

Set objAlarm = HMIRuntime.Alarms(2)

objAlarm.State = 1 'hmiAlarmStateCome

objAlarm.Create

Set objAlarm = HMIRuntime.Alarms(3)

objAlarm.State = 1 'hmiAlarmStateCome

objAlarm.Create

End Sub

---

**See also**

[Create (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#create-panels-comfort-panels-rt-advanced-rt-professional)
  
[State (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#state-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of statistically evaluating tag values (RT Professional)

##### Introduction

You can use the value table to display the coordinates of trends and the statistical evaluation of tag values in tabular form. You connect the value table to the corresponding object for this purpose. The evaluated data can be printed out and exported.

##### Procedure

In the following example, the tag values of the f(t) trend view "Control2" are statistically evaluated. To display the result in the statistics area window of the value table, you set the following in the value table properties:

- Data source: "Control2"
- Mode: "Statistic area" window"

Add a new button in f(t) trend view and configure the user-defined VB function for it.

Sub OnToolbarButtonClicked(ByVal Item, ByVal lId)

Dim objTrend

Set objTrend = ScreenItems("Control2")

objTrend.CalculateStatistic()

End Sub

---

**See also**

[CalculateStatistic (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#calculatestatistic-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Example of the start of a script at the server (Logging object) (RT Professional)

##### Introduction

In multi-station projects, the Logging object currently works only on the server. The following examples shows how you start a script from the client and thus also store and delete log segments at the client.

The following example shows a global script that is started with a control tag. The content of the control tag determines whether the method "Restore" or the method "Remove" is called. The control tag is set to "0" at the end of the script. A query prevents the script from starting on client computers. Path and period are transferred by internal tags.

'VBS180

'StartLoggingOnServer

Dim StartLogging

Dim SourcePath

Dim TimeFrom

Dim TimeTo

Dim RetVal

'Exit when running on client

If (Left(HMIRuntime.ActiveProject.Path, 1) = "\") Then

Exit Function

End If

'read parameters

StartLogging = HMIRuntime.Tags("StartLogging").Read

SourcePath = HMIRuntime.Tags("SourcePath").Read(1)

TimeFrom = HMIRuntime.Tags("TimeFrom").Read(1)

TimeTo = HMIRuntime.Tags("TimeTo").Read(1)

'restore or remove depends on the parameter

If (StartLogging = 1) Then

RetVal = HMIRuntime.Logging.Restore(SourcePath, TimeFrom, TimeTo, -1)

HMIRuntime.Tags("RetVal").Write RetVal, 1

HMIRuntime.Tags("StartLogging").Write 0,1

Elseif (StartLogging = 2) Then

RetVal = HMIRuntime.Logging.Remove(TimeFrom, TimeTo, -1)

HMIRuntime.Tags("RetVal").Write RetVal, 1

HMIRuntime.Tags("StartLogging").Write 0,1

End If

A network enable can also be specified as path. The log segments to be stored do not, therefore, have to be located locally on the server. However, it must be ensure that the server can access the path correctly.

> **Note**
>
> The example shows a proposed solution and is to be adjusted if necessary.

##### Procedure

1. Create the following internal tags with project-wide update in the WinCC Explorer:

   - StartLogging (Unsigned 8-bit value)
   - SourcePath (Text tag, 8-bit character set)
   - TimeFrom (Text tag, 8-bit character set)
   - TimeTo (Text tag, 8-bit character set)
   - RetVal (Signed 32-bit value)
2. Create the script "StartLoggingOnServer".
3. Configure the tag "StartLogging" the script "StartLoggingOnServer" at the event "Value change".

You can start the script on the client, for example, with the following script:

'VBS181

'Prerequisite: set parameters

HMIRuntime.Tags("SourcePath").Write "\\client_pc\temp",1

HMIRuntime.Tags("TimeFrom").Write "2004",1

HMIRuntime.Tags("TimeTo").Write "2004",1

'start action

HMIRuntime.Tags("StartLogging").Write 1,1

> **Note**
>
> The tags are mainly written and read in "direct" mode. Thus, the processes are synchornized. As these are internal tags, this mode can be used without hesitation.

#### Example for opening the PLC code view from the GRAPH overview (RT Professional)

##### Introduction

With VBS, even when using screen windows, you have the option of switching from the GRAPH overview to the PLC code view.

For this purpose, you create a VB script at a graph overview, a screen with a screen window, and an additional screen with a PLC code view that shows the corresponding program code.

##### Opening PLC code view from a screen window

In the following example, the PLC code view "PLC code view_1" in the screen "CodeViewScreen" is called with an event from the GRAPH overview in the screen window "Screen window_1".

Sub OnPlcCodeViewButtonClick(ByVal item, ByVal codeViewerDiagnosticsContext)

Dim objScreenWindow

Set objScreenWindow = ScreenItems("Screen window_1")

objScreenWindow.ScreenName = "CodeViewScreen"

objScreenWindow.Screen.ScreenItems("PLC code view_1").NavigateTo = codeViewerDiagnosticsContext

End Sub

#### Example of deleting the browser cache (RT Professional)

##### Introduction

If you notice with Panels that the loading of websites in the HTML browser takes significantly longer, this might be caused by the browser cache. Execute the following VBS function in Runtime to delete the browser cache. You can also configure this VBS function as regular task in the Task Scheduler.

##### Procedure

The following example deletes the browser cache:

Sub T7_DeleteBrowserCache()

' delete Browsercache filled temporary objects

Dim fso, nFileIndex,sFileName, nFileAttr, folder

On Error Resume Next

' Variable to show script is active

SmartTags("DeleteBrowserCacheActive") = True

folder = "\flash\simatic\Browsercache\data7\"

' Windows CE

Set fso = CreateObject("FileCtl.FileSystem")

' Get first item that matches path

sFileName = fso.Dir(folder &amp; "*.*")

nFileIndex = 0

'Get the rest of matches

Do While sFileName &lt;&gt; ""

nFileAttr = fso.GetAttr(folder &amp; sFileName)

If (nFileAttr And 16) &lt;&gt; 0 Then

fso.Kill("\flash\simatic\Browsercache\data7\"&amp;sFileName&amp;"\*.*")

If Err.Number &lt;&gt;0 Then

Err.Clear

End If

End If

nFileIndex = nFileIndex + 1

sFileName = fso.Dir

Loop

Set fso = Nothing

SmartTags("DeleteBrowserCacheActive") = False

End Sub

### Examples of C (RT Professional)

This section contains information on the following topics:

- [Overview (RT Professional)](#overview-rt-professional-1)
- [Example of accessing objects in the Screens editor (RT Professional)](#example-of-accessing-objects-in-the-screens-editor-rt-professional-1)
- [Example of defining object colors (RT Professional)](#example-of-defining-object-colors-rt-professional-1)
- [Example of configuring a language switch (RT Professional)](#example-of-configuring-a-language-switch-rt-professional-1)
- [Example of deactivating Runtime (RT Professional)](#example-of-deactivating-runtime-rt-professional-1)
- [Example of configuring a screen change via a property (RT Professional)](#example-of-configuring-a-screen-change-via-a-property-rt-professional-1)
- [Example of configuring a diagnostics output via a trace (RT Professional)](#example-of-configuring-a-diagnostics-output-via-a-trace-rt-professional-1)
- [Example of writing tag values (RT Professional)](#example-of-writing-tag-values-rt-professional-1)
- [Example of reading tag values (RT Professional)](#example-of-reading-tag-values-rt-professional-1)
- [Example of writing object properties (RT Professional)](#example-of-writing-object-properties-rt-professional-1)

#### Overview (RT Professional)

##### Introduction

You can find examples for C functions:

- Access to objects in the "Screens"editor (e.g. color or text change)
- Determining color of objects
- Configuring a language switch
- Deactivating Runtime
- Configuring a screen change via a property
- Configuring diagnostic output via a trace
- Writing tag values
- Reading tag values
- Writing object properties

---

**See also**

[Example of accessing objects in the Screens editor (RT Professional)](#example-of-accessing-objects-in-the-screens-editor-rt-professional-1)
  
[Example of defining object colors (RT Professional)](#example-of-defining-object-colors-rt-professional-1)
  
[Example of configuring a language switch (RT Professional)](#example-of-configuring-a-language-switch-rt-professional-1)
  
[Example of deactivating Runtime (RT Professional)](#example-of-deactivating-runtime-rt-professional-1)
  
[Example of configuring a screen change via a property (RT Professional)](#example-of-configuring-a-screen-change-via-a-property-rt-professional-1)
  
[Example of configuring a diagnostics output via a trace (RT Professional)](#example-of-configuring-a-diagnostics-output-via-a-trace-rt-professional-1)
  
[Example of writing tag values (RT Professional)](#example-of-writing-tag-values-rt-professional-1)
  
[Example of reading tag values (RT Professional)](#example-of-reading-tag-values-rt-professional-1)
  
[Example of writing object properties (RT Professional)](#example-of-writing-object-properties-rt-professional-1)

#### Example of accessing objects in the Screens editor (RT Professional)

##### Introduction

To make the graphic Runtime environment dynamic, you can use C scripting to access all objects in the "Screens" editor in WinCC. In doing so, you can make graphic objects dynamic in response to an operator input, e.g., in response to a mouse click or depending on tag values.

##### Procedure

In the following example, the radius of a circle is set to 10 in Runtime per mouse click:

'C121

SetPropDouble(screenName,"Kreis_1","Radius",10);

---

**See also**

[SetPropDouble (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setpropdouble-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of defining object colors (RT Professional)

##### Introduction

The object colors are defined by means of RGB values (Red/Green/Blue). The color values for graphic objects can be set or read.

##### Procedure

The following example defines the fill color for "Roundbutton1" to blue:

'C122

SetPropertyByConstant (screenName, " Roundbutton1", "FillPatternColor", "65035");

---

**See also**

[SetPropertyByConstant (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setpropertybyconstant-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of configuring a language switch (RT Professional)

##### Introduction

The Runtime language can be changed by means of VBS. Use buttons with corresponding country markings that you place on the start page of your project.

Define the Runtime language by means of country code, for example, 1031 for German - Default, 1033 for English - USA etc. An overview of all country codes is available in the basics of VBScript, "Regional Scheme ID (LCID) Diagram".

##### Procedure

Create a user-defined C function for a button for the "Mouse click" event, and enter the following code to switch the Runtime language to German:

'C123

SetLanguageByLocaleID(1033);

---

**See also**

[SetLanguageByLocaleID (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setlanguagebylocaleid-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of deactivating Runtime (RT Professional)

##### Introduction

You can use C functions to exit Runtime, for example, by means of mouse click, or depending on tag values, or on other events.

##### Procedure

The following example terminates WinCC Runtime:

'C124

StopRuntime(hmiStopRuntime);

---

**See also**

[StopRuntime (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#stopruntime-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of configuring a screen change via a property (RT Professional)

##### Introduction

If using split screens in your configuration, for example, the title and operating bar for the user interface in a basic screen and an embedded screen window for the actual screen display, configure a screen change using the properties of the screen window.

The property of screen window "ScreenName" must be changed so that the other screen is displayed. The C function and screen window must be configured in the same screen.

##### Procedure

In the next example, the "test" screen is displayed in a "ScreenWindow" when you execute the C function:

'C126

ActivateScreenInScreenWindow (screenName, "ScreenWindow", "test");

---

**See also**

[ActivateScreenInScreenWindow (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#activatescreeninscreenwindow-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of configuring a diagnostics output via a trace (RT Professional)

##### Introduction

If you have inserted a GSC diagnostics window in your screen, you can use the trace command to display diagnostics outputs in the diagnostics window in Runtime.

GSC diagnostics returns the trace methods contained in the functions in the order in which they were called. This also applies to trace instructions in functions that are called in user-defined functions. The targeted use of trace instructions allows you to trace the execution of user-defined functions and the functions called therein. You enter the trace instruction in the form "printf(&lt;Output&gt;)".

The GSC diagnostics window displays trace outputs of C functions.

##### Outputting text

The following example writes a text in the diagnostics window:

'C127

printf("Customized C script error message\r\n");

---

**See also**

[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of writing tag values (RT Professional)

##### Introduction

You can use C functions to write the tag value to the PLC, foe example, by mouse click on a setpoint button, or to set internal tag values for triggering other functions.

##### Simple writing

In the following example, a value is written to the "Tag1" tag:

'C128

int value;

value = 7;

SetTagSDWord("Tag1", value);

---

**See also**

[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of reading tag values (RT Professional)

##### Introduction

C functions can be used to read and further process a tag value. This allows you to click a button, for example, to obtain information on the system status or to perform calculations.

##### Simple reading

In the following example, the value of "Tag1" is read and displayed in the Global Script diagnostics window:

'C134

int value;

value = GetTagGetTagSDWord("Tag1");

---

**See also**

[Overview (RT Professional)](#overview-rt-professional-1)

#### Example of writing object properties (RT Professional)

##### Introduction

C functions provide access to the properties of all display and operating objects in the "Screens" editor. You can read out properties or change them during Runtime.

The following example shows how to access a property.

##### Simple setting of a property

In the next example, the background color of the "Button1" object in the screen is set to red:

'C139

SetPropLong("Screen_1","Button1","ForeColor",65333);

---

**See also**

[SetPropLong (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#setproplong-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional-1)

## Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Events%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [VB scripting (Panels, Comfort Panels, RT Advanced, RT Professional)](#vb-scripting-panels-comfort-panels-rt-advanced-rt-professional)
- [C scripting (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#c-scripting-rt-professional)

### Function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Device dependency (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [System functions (Basic Panels, Panels, Comfort Panels, RT Advanced)](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#system-functions-basic-panels-panels-comfort-panels-rt-advanced)
- [System functions (RT Professional)](System%20functions%20%28RT%20Professional%29.md#system-functions-rt-professional)

#### Device dependency (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [System functions for Basic Panels (Basic Panels)](#system-functions-for-basic-panels-basic-panels)
- [System functions for Basic Panels 2nd Generation (Basic Panels)](#system-functions-for-basic-panels-2nd-generation-basic-panels)
- [System functions for Comfort Panels (Panels, Comfort Panels)](#system-functions-for-comfort-panels-panels-comfort-panels)
- [System functions for Mobile Panels (Panels, Comfort Panels)](#system-functions-for-mobile-panels-panels-comfort-panels)
- [System functions for Runtime Advanced (RT Advanced)](#system-functions-for-runtime-advanced-rt-advanced)
- [System functions for Runtime Professional (RT Professional)](#system-functions-for-runtime-professional-rt-professional)

##### System functions for Basic Panels (Basic Panels)

###### Availability of system functions

The following table shows the availability of the system functions on the Basic Panels.

Technical data subject to change.

###### Overview

|  | KP300 Basic PN | KP400 Basic PN | KTP600 Basic PN / DP | KTP1000 Basic PN / DP | TP1500 Basic PN |
| --- | --- | --- | --- | --- | --- |
| User-defined functions | No | No | No | No | No |
| [Logoff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logoff-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ActivateScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ActivateScreenByNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreenbynumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ActivateCleanScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatecleanscreen-basic-panels-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes |
| [ActivatePreviousScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatepreviousscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [UpdateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#updatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [AdjustContrast](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#adjustcontrast-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes <sup>1)</sup> | Yes | Yes |
| [Logon](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logon-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ArchiveLogFile](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#archivelogfile-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [LogTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logtag-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [EditAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#editalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [ScreenObjectCursorDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursordown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorleft-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ScreenObjectCursorRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorright-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ScreenObjectPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [Encode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encode-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [EncodeEx](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encodeex-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [Direct key](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkey-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [DirectKeyScreenNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkeyscreennumber-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PrintScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printscreen-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PrintReport](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printreport-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [NotifyUserAction](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#notifyuseraction-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [IncreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [IncreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ExportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ExportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ExportImportUserAdministration](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportimportuseradministration-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [GoToHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotohome-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [GoToEnd](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotoend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [SafelyRemoveHardware](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#safelyremovehardware-basic-panels-panels-comfort-panels) | No | No | No | No | No |
| [HTMLBrowserStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserstop-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrolldown-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserrefresh-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollup-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserforward-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserback-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomin-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomout-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollleft-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollright-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpageup-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpagedown-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ImportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ImportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [InvertBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [InvertBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [InvertLinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertlinearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [CalibrateTouchScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#calibratetouchscreen-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes |
| [CopyLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#copylog-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [TrendViewScrollForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewScrollBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewExtend](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewextend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewCompress](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewcompress-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewRulerLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewRulerRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewSetRulerMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewsetrulermode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewStartStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewstartstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [TrendViewBackToBeginning](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewbacktobeginning-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [LoadDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#loaddatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetUserName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getusername-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetDataRecordName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordname-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [GetDataRecordTagsFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordtagsfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetGroupNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getgroupnumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getbrightness-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ReadPassword](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#readpassword-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [GetPLCMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getplcmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [LinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#linearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ClearLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearlog-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ClearDataRecordMemory](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecordmemory-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ClearAlarmBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ClearAlarmBufferProTool](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbufferprotool-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewUpdate](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewupdate-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [AlarmViewLoopInAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewloopinalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewAcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewacknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewshowoperatornotes-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [OpenAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openalllogs-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenScreenKeyboard](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openscreenkeyboard-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenControlPanelDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpaneldialog-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenCommandPrompt](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencommandprompt-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenInternetExplorer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openinternetexplorer-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenControlPanel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpanel-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [OpenTaskManager](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opentaskmanager-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [AcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#acknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [PDFScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrolldown-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollup-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFFitToWidth](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittowidth-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFFitToHeight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittoheight-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFGoToFirstPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotofirstpage-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFGoToLastPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotolastpage-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFGoToNextPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotonextpage-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFGoToPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopage-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFGoToPreviousPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopreviouspage-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomin-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomout-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollleft-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollright-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [PDFZoomOriginal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomoriginal-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [RecipeViewNewDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewnewdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewGetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewgetdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewcleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewMenu](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewmenu-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewOpen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewopen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsetdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsavedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSaveAsDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsaveasdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSynchronizeDataRecordWithTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsynchronizedatarecordwithtags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewRenameDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewrenamedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewshowoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ResetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ResetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [PressButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pressbutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [ReleaseButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#releasebutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [ShiftAndMask](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#shiftandmask-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [CloseAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#closealllogs-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetDataRecordTagsToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtagstoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [PageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [PageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [SendEMail](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#sendemail-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetAcousticSignal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setacousticsignal-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetDisplayMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdisplaymode-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetDeviceMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdevicemode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetBitWhileKeyPressed](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitwhilekeypressed-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetBacklightColor](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbacklightcolor-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | No | No | No |
| [SetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbrightness-panels-comfort-panels-rt-advanced) | No | Yes | Yes | No | No |
| [SetScreenKeyboardMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setscreenkeyboardmode-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetAlarmReportMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setalarmreportmode-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetRecipeTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setrecipetags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetDaylightSavingTime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdaylightsavingtime-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetLanguage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setlanguage-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetConnectionMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setconnectionmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SetWebAccess](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setwebaccess-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [BackupRAMFileSystem](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#backupramfilesystem-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SimulateSystemKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatesystemkey-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [SimulateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewrefresh-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SmartClientViewReadOnlyOff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyoff-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SmartClientViewReadOnlyOn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyon-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SmartClientViewDisconnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewdisconnect-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SmartClientViewConnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewconnect-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SmartClientViewLeave](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewleave-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#savedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [StartLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startlogging-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StartNextLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startnextlog-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StartProgram](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startprogram-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StatusForceGetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcegetvalues-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StatusForceSetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcesetvalues-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ControlSmartServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlsmartserver-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ControlWebServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlwebserver-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StopLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stoplogging-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [StopRuntime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stopruntime-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SystemDiagnosticViewUpdatePLCBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewupdateplcbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ActivateSystemDiagnosticsView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SystemDiagnosticViewDetailView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdetailview-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [SystemDiagnosticsViewDiagnosticBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdiagnosticbuffer-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SystemDiagnosticViewDeviceView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdeviceview-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SystemDiagnosticsViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewback-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [LookupText](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#lookuptext-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ResetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resettagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [SetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [TraceUserChange](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#traceuserchange-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [DecreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | No |
| [DecreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ChangeConnection](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnection-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ChangeConnectionEIP](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnectioneip-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ShowLogonDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showlogondialog-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ShowAlarmWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showalarmwindow-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes |
| [ShowPopupScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreen-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ShowPopupScreenSizable](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreensizable-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ShowSlideInScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showslideinscreen-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ShowSoftwareVersion](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsoftwareversion-panels-comfort-panels-rt-advanced) | No | No | No | No | No |
| [ShowSystemDiagnosticsWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemdiagnosticswindow-panels-comfort-panels) | No | No | No | No | No |
| [ShowSystemEvent](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemalarm-panels-comfort-panels-rt-advanced) | No | No | No | No | No |

| Symbol | Meaning |
| --- | --- |
| 1) | For KTP600 Basic mono PN only |

##### System functions for Basic Panels 2nd Generation (Basic Panels)

###### Availability of system functions

The following table shows the availability of the system functions on the Basic Panels.

Technical data subject to change.

###### Overview

|  | KTP400 Basic PN | KTP700 Basic PN / DP | KTP900 Basic PN | KTP1200 Basic PN / DP |
| --- | --- | --- | --- | --- |
| User-defined functions | No | No | No | No |
| [Logoff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logoff-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ActivateScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ActivateScreenByNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreenbynumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ActivateCleanScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatecleanscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ActivatePreviousScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatepreviousscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [UpdateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#updatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [AdjustContrast](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#adjustcontrast-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [Logon](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logon-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ArchiveLogFile](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#archivelogfile-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [LogTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logtag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [EditAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#editalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursordown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ScreenObjectPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [Encode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encode-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [EncodeEx](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encodeex-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [Direct key](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkey-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [DirectKeyScreenNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkeyscreennumber-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PrintScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printscreen-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PrintReport](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printreport-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [NotifyUserAction](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#notifyuseraction-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [IncreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [IncreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ExportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ExportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ExportImportUserAdministration](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportimportuseradministration-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [GoToHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotohome-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GoToEnd](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotoend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SafelyRemoveHardware](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#safelyremovehardware-basic-panels-panels-comfort-panels) | Yes | Yes | Yes | Yes |
| [HTMLBrowserStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrolldown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserrefresh-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomin-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomout-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [HTMLBrowserBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ImportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ImportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [InvertBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [InvertBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [InvertLinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertlinearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [CalibrateTouchScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#calibratetouchscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [CopyLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#copylog-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [TrendViewScrollForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewScrollBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewExtend](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewextend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewCompress](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewcompress-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewRulerLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewRulerRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewSetRulerMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewsetrulermode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewStartStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewstartstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [TrendViewBackToBeginning](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewbacktobeginning-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [LoadDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#loaddatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GetUserName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getusername-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GetDataRecordName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordname-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [GetDataRecordTagsFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordtagsfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GetGroupNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getgroupnumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [GetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getbrightness-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ReadPassword](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#readpassword-basic-panels-panels-comfort-panels-rt-advanced) | No <sup>1)</sup> | No <sup>1)</sup> | No <sup>1)</sup> | No <sup>1)</sup> |
| [GetPLCMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getplcmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [LinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#linearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ClearLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearlog-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ClearDataRecordMemory](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecordmemory-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ClearAlarmBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ClearAlarmBufferProTool](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbufferprotool-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [AlarmViewUpdate](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewupdate-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [AlarmViewLoopInAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewloopinalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [AlarmViewAcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewacknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [AlarmViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewshowoperatornotes-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [OpenAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openalllogs-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [OpenScreenKeyboard](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openscreenkeyboard-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [OpenControlPanelDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpaneldialog-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [OpenCommandPrompt](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencommandprompt-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [OpenInternetExplorer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openinternetexplorer-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [OpenControlPanel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpanel-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [OpenTaskManager](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opentaskmanager-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrolldown-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFFitToWidth](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittowidth-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFFitToHeight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittoheight-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollup-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFGoToFirstPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotofirstpage-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFGoToLastPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotolastpage-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFGoToNextPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotonextpage-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFGoToPreviousPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopreviouspage-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFGoToPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopage-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomin-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomout-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollleft-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollright-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [PDFZoomOriginal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomoriginal-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [AcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#acknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewNewDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewnewdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewGetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewgetdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewcleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewMenu](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewmenu-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewOpen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewopen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewSetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsetdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewSaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsavedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewSaveAsDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsaveasdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewSynchronizeDataRecordWithTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsynchronizedatarecordwithtags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewRenameDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewrenamedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewshowoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [RecipeViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ResetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ResetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [PressButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pressbutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ReleaseButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#releasebutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ShiftAndMask](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#shiftandmask-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [CloseAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#closealllogs-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetDataRecordTagsToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtagstoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [PageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [PageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SendEMail](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#sendemail-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetAcousticSignal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setacousticsignal-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetDisplayMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdisplaymode-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetDeviceMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdevicemode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetBitWhileKeyPressed](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitwhilekeypressed-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetBacklightColor](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbacklightcolor-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbrightness-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetScreenKeyboardMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setscreenkeyboardmode-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetAlarmReportMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setalarmreportmode-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetRecipeTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setrecipetags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetDaylightSavingTime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdaylightsavingtime-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetLanguage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setlanguage-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetConnectionMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setconnectionmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SetWebAccess](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setwebaccess-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [BackupRAMFileSystem](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#backupramfilesystem-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SimulateSystemKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatesystemkey-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SimulateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SmartClientViewRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewrefresh-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SmartClientViewReadOnlyOff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyoff-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SmartClientViewReadOnlyOn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyon-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SmartClientViewDisconnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewdisconnect-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SmartClientViewConnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewconnect-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SmartClientViewLeave](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewleave-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#savedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [StartLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startlogging-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [StartNextLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startnextlog-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [StartProgram](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startprogram-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [StatusForceGetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcegetvalues-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [StatusForceSetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcesetvalues-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ControlSmartServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlsmartserver-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ControlWebServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlwebserver-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [StopLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stoplogging-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [StopRuntime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stopruntime-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ActivateSystemDiagnosticsView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SystemDiagnosticViewUpdatePLCBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewupdateplcbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SystemDiagnosticsViewDetailView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdetailview-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [SystemDiagnosticsViewDiagnosticBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdiagnosticbuffer-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SystemDiagnosticViewDeviceView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdeviceview-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SystemDiagnosticsViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewback-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [LookupText](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#lookuptext-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ResetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resettagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [SetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [TraceUserChange](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#traceuserchange-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [DecreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [DecreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ChangeConnection](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnection-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ChangeConnectionEIP](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnectioneip-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ShowLogonDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showlogondialog-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ShowAlarmWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showalarmwindow-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes |
| [ShowPopupScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreen-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ShowPopupScreenSizable](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreensizable-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ShowSlideInScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showslideinscreen-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ShowSoftwareVersion](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsoftwareversion-panels-comfort-panels-rt-advanced) | No | No | No | No |
| [ShowSystemDiagnosticsWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemdiagnosticswindow-panels-comfort-panels) | No | No | No | No |
| [ShowSystemEvent](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemalarm-panels-comfort-panels-rt-advanced) | No | No | No | No |

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | Not available for devices as of device version V14.0 |

##### System functions for Comfort Panels (Panels, Comfort Panels)

###### Availability of system functions

The following table shows the availability of the system functions on the Comfort Panels.

Technical data subject to change.

###### Overview

|  | KTP400   KP400 | TP700 TP900 TP1200  TP1500 TP1900 TP2200 | KP700 KP900 KP1200 KP1500 |
| --- | --- | --- | --- |
| User-defined functions | Yes | Yes | Yes |
| [Logoff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logoff-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ActivateScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ActivateScreenByNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreenbynumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ActivatePLCCodeViewer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activateplccodeviewer-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [ActivateCleanScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatecleanscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes <sup>1)</sup> | Yes | No |
| [ActivatePreviousScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatepreviousscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [UpdateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#updatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AdjustContrast](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#adjustcontrast-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No |
| [Logon](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logon-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ArchiveLogFile](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#archivelogfile-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [LogTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logtag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [EditAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#editalarm-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [ScreenObjectCursorDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursordown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ScreenObjectCursorUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ScreenObjectCursorLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorleft-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [ScreenObjectCursorRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorright-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [ScreenObjectPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ScreenObjectPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [Encode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encode-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [EncodeEx](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encodeex-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [DirectKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkey-panels-comfort-panels-rt-advanced) | Yes <sup>1)</sup> | Yes | No |
| [DirectKeyScreenNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkeyscreennumber-panels-comfort-panels-rt-advanced) | Yes <sup>1)</sup> | Yes | No |
| [PrintScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printscreen-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PrintReport](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printreport-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [NotifyUserAction](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#notifyuseraction-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [IncreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [IncreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ExportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ExportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ExportImportUserAdministration](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportimportuseradministration-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GoToHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotohome-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [GoToEnd](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotoend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [SafelyRemoveHardware](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#safelyremovehardware-basic-panels-panels-comfort-panels) | Yes | Yes | Yes |
| [HTMLBrowserStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserstop-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrolldown-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserrefresh-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollup-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserforward-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserback-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomin-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomout-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollleft-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollright-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpagedown-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpageup-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [ImportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ImportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [InvertBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [InvertBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [InvertLinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertlinearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [CalibrateTouchScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#calibratetouchscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes <sup>1)</sup> | Yes | No |
| [CopyLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#copylog-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewScrollForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewScrollBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewExtend](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewextend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewCompress](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewcompress-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewRulerLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewRulerRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewSetRulerMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewsetrulermode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewStartStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewstartstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [TrendViewBackToBeginning](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewbacktobeginning-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [LoadDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#loaddatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetUserName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getusername-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetDataRecordName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordname-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetDataRecordTagsFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordtagsfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetGroupNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getgroupnumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [GetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getbrightness-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ReadPassword](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#readpassword-basic-panels-panels-comfort-panels-rt-advanced) | No <sup>2)</sup> | No <sup>2)</sup> | No <sup>2)</sup> |
| [GetPLCMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getplcmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [LinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#linearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ClearLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearlog-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ClearDataRecordMemory](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecordmemory-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ClearAlarmBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ClearAlarmBufferProTool](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbufferprotool-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AlarmViewUpdate](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewupdate-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AlarmViewLoopInAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewloopinalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AlarmViewAcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewacknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AlarmViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewshowoperatornotes-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openalllogs-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenScreenKeyboard](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openscreenkeyboard-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenFileBrowser](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openfilebrowser-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenControlPanelDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpaneldialog-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenCommandPrompt](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencommandprompt-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenInternetExplorer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openinternetexplorer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenControlPanel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpanel-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [OpenTaskManager](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opentaskmanager-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [AcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#acknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [PDFScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrolldown-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollup-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFFitToWidth](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittowidth-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFFitToHeight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittoheight-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFGotoFirstPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotofirstpage-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFGotoLastPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotolastpage-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFGotoNextPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotonextpage-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFGotoPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopage-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFGotoPreviousPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopreviouspage-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomin-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomout-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollleft-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollright-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PDFZoomOriginal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomoriginal-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PLCCodeViewDetails](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewdetails-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewNextNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewnextnetwork-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewStepMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewstepmode-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewSymbols](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewsymbols-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewTransitionInterlock](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewtransitioninterlock-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomin-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomout-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeViewPreviousNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewpreviousnetwork-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [PLCCodeDisplayMonitoringOrFBCall](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodedisplaymonitoringorfbcall-panels-comfort-panels-rt-advanced) | No | Yes | Yes |
| [RecipeViewNewDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewnewdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewGetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewgetdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewcleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewMenu](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewmenu-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewOpen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewopen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewSetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsetdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewSaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsavedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewSaveAsDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsaveasdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewSynchronizeDataRecordWithTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsynchronizedatarecordwithtags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewRenameDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewrenamedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewshowoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [RecipeViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ResetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ResetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PressButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pressbutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ReleaseButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#releasebutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShiftAndMask](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#shiftandmask-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [CloseAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#closealllogs-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetDataRecordTagsToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtagstoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [PageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [PageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [SendEMail](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#sendemail-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetAcousticSignal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setacousticsignal-panels-comfort-panels-rt-advanced) | Yes <sup>1)</sup> | Yes | No |
| [SetDisplayMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdisplaymode-panels-comfort-panels-rt-advanced) | No | No | No |
| [SetDeviceMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdevicemode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetBitWhileKeyPressed](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitwhilekeypressed-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetBacklightColor](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbacklightcolor-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No |
| [SetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbrightness-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetScreenKeyboardMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setscreenkeyboardmode-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetPLCMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setplcmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetAlarmReportMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setalarmreportmode-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetRecipeTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setrecipetags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetDaylightSavingTime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdaylightsavingtime-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetLanguage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setlanguage-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetConnectionMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setconnectionmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SetWebAccess](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setwebaccess-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [BackupRAMFileSystem](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#backupramfilesystem-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SimulateSystemKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatesystemkey-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [SimulateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewrefresh-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewReadOnlyOff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyoff-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewReadOnlyOn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyon-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewDisconnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewdisconnect-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewConnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewconnect-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SmartClientViewLeave](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewleave-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#savedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StartLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startlogging-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StartNextLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startnextlog-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StartProgram](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startprogram-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StatusForceGetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcegetvalues-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StatusForceSetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcesetvalues-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ControlSmartServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlsmartserver-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ControlWebServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlwebserver-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StopLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stoplogging-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [StopRuntime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stopruntime-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ActivateSystemDiagnosticsView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SystemDiagnosticViewUpdatePlcBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewupdateplcbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SystemDiagnosticViewDetailView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdetailview-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SystemDiagnosticViewDiagnosticBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdiagnosticbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SystemDiagnosticViewDeviceView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewdeviceview-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [SystemDiagnosticViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#systemdiagnosticviewback-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [LookupText](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#lookuptext-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ResetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resettagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No |
| [SetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settagtohandwheel-panels-comfort-panels-rt-advanced) | No | No | No |
| [TraceUserChange](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#traceuserchange-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [DecreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | No | Yes |
| [DecreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ChangeConnection](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnection-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ChangeConnectionEIP](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnectioneip-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowLogonDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showlogondialog-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowAlarmWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showalarmwindow-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowPopupScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreen-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowPopupScreenSizable](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreensizable-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowSlideInScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showslideinscreen-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowSoftwareVersion](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsoftwareversion-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |
| [ShowSystemDiagnosticsWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemdiagnosticswindow-panels-comfort-panels) | Yes | Yes | Yes |
| [ShowSystemAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes |

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | Only on KTP 400 Comfort |
| <sup>2)</sup> | Not available for devices as of device version V14.0 and higher |

##### System functions for Mobile Panels (Panels, Comfort Panels)

###### Availability of system functions

The following table shows the availability of the system functions on the mobile panels.

Technical data subject to change.

###### Overview

|  | Mobile Panel 177 DP | Mobile Panel 177 PN | Mobile Panel 277 Mobile Panel 277 IWLAN Mobile Panel 277 F IWLAN | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- | --- | --- | --- |
| User-defined functions | No | No | Yes | Yes | Yes | Yes |
| [Logoff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logoff-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ActivateScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ActivateScreenByNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreenbynumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ActivatePLCCodeViewer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activateplccodeviewer-panels-comfort-panels-rt-advanced) | No | No | No | No | Yes | Yes |
| [ActivateCleanScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatecleanscreen-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No | No |
| [ActivatePreviousScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatepreviousscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [UpdateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#updatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [AdjustContrast](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#adjustcontrast-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | No | No | No | No |
| [Logon](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logon-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ArchiveLogFile](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#archivelogfile-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [LogTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logtag-basic-panels-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [EditAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#editalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursordown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ScreenObjectCursorRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [Encode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encode-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [EncodeEx](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encodeex-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [DirectKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkey-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [DirectKeyScreenNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkeyscreennumber-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [PrintScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printscreen-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [PrintReport](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printreport-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [NotifyUserAction](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#notifyuseraction-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [IncreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [IncreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ExportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ExportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [ExportImportUserAdministration](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportimportuseradministration-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GoToHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotohome-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GoToEnd](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotoend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SafelyRemoveHardware](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#safelyremovehardware-basic-panels-panels-comfort-panels) | No | No | Yes | Yes | Yes | Yes |
| [HTMLBrowserStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserstop-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrolldown-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserrefresh-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollup-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomin-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomout-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollleft-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollright-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpagedown-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpageup-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserforward-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [HTMLBrowserBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserback-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ImportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ImportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [InvertBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [InvertBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [InvertLinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertlinearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [CalibrateTouchScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#calibratetouchscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes <sup>1)</sup> | Yes | Yes | Yes |
| [CopyLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#copylog-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [TrendViewScrollForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewScrollBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewExtend](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewextend-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewCompress](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewcompress-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewRulerLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewRulerRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerright-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewSetRulerMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewsetrulermode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewStartStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewstartstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [TrendViewBackToBeginning](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewbacktobeginning-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [LoadDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#loaddatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetUserName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getusername-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetDataRecordName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordname-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetDataRecordTagsFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordtagsfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetGroupNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getgroupnumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [GetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getbrightness-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ReadPassword](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#readpassword-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No <sup>2)</sup> | No <sup>2)</sup> | No <sup>2)</sup> |
| [ClearLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearlog-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [ClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ClearDataRecordMemory](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecordmemory-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ClearAlarmBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbuffer-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ClearAlarmBufferProTool](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbufferprotool-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewUpdate](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewupdate-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewLoopInAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewloopinalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewAcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewacknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [AlarmViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewshowoperatornotes-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [OpenAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openalllogs-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [OpenFileBrowser](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openfilebrowser-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [OpenScreenKeyboard](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openscreenkeyboard-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [OpenCommandPrompt](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencommandprompt-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [OpenControlPanelDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpaneldialog-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [OpenInternetExplorer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openinternetexplorer-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [OpenTaskManager](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opentaskmanager-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [OpenControlPanel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpanel-panels-comfort-panels-rt-advanced) | No | No | Yes <sup>1)</sup> | No | Yes/No <sup>3)</sup> | Yes/No <sup>3)</sup> |
| [AcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#acknowledgealarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [PDFScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrolldown-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollup-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFFitToWidth](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittowidth-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFFitToHeight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittoheight-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFGotoFirstPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotofirstpage-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFGotoLastPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotolastpage-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFGotoNextPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotonextpage-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFGotoPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopage-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFGotoPreviousPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopreviouspage-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomin-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomout-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollleft-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollright-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PDFZoomOriginal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomoriginal-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [PLCCodeViewDetails](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewdetails-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewNextNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewnextnetwork-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewStepMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewstepmode-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewSymbols](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewsymbols-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewTransitionInterlock](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewtransitioninterlock-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomin-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomout-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [PLCCodeViewPreviousNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewpreviousnetwork-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | Yes | Yes |
| [RecipeViewNewDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewnewdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewGetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewgetdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewcleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewMenu](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewmenu-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewOpen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewopen-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsetdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsavedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSaveAsDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsaveasdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewSynchronizeDataRecordWithTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsynchronizedatarecordwithtags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewRenameDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewrenamedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewshowoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [RecipeViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewback-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ResetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ResetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [PressButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pressbutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ReleaseButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#releasebutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ShiftAndMask](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#shiftandmask-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [CloseAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#closealllogs-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [SetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetDataRecordTagsToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtagstoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [PageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [PageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SendEMail](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#sendemail-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SetAcousticSignal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setacousticsignal-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [SetDisplayMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdisplaymode-panels-comfort-panels-rt-advanced) | No | No | No | No | No | No |
| [SetDeviceMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdevicemode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetBitWhileKeyPressed](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitwhilekeypressed-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetBacklightColor](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbacklightcolor-basic-panels-panels-comfort-panels-rt-advanced) | No | No | No | No | No | No |
| [SetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbrightness-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [SetScreenKeyboardMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setscreenkeyboardmode-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [SetAlarmReportMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setalarmreportmode-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [SetRecipeTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setrecipetags-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetDaylightSavingTime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdaylightsavingtime-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [SetLanguage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setlanguage-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetConnectionMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setconnectionmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SetWebAccess](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setwebaccess-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [BackupRAMFileSystem](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#backupramfilesystem-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [SimulateSystemKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatesystemkey-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SimulateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewrefresh-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewReadOnlyOff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyoff-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewReadOnlyOn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyon-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewDisconnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewdisconnect-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewConnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewconnect-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SmartClientViewLeave](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewleave-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [SaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#savedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [StartLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startlogging-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [StartNextLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startnextlog-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [StartProgram](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startprogram-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [StatusForceGetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcegetvalues-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [StatusForceSetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcesetvalues-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ControlSmartServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlsmartserver-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [ControlWebServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlwebserver-panels-comfort-panels-rt-advanced) | No | Yes | Yes | Yes | Yes | Yes |
| [StopLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stoplogging-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [StopRuntime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stopruntime-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [LookupText](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#lookuptext-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ActivateSystemDiagnosticsView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ResetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resettagtohandwheel-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | No | No |
| [SetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settagtohandwheel-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | No | No |
| [TraceUserChange](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#traceuserchange-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | No | No | No |
| [DecreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [DecreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ChangeConnection](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnection-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ChangeConnectionEIP](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnectioneip-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ShowLogonDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showlogondialog-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ShowAlarmWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showalarmwindow-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |
| [ShowPopupScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreen-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ShowPopupScreenSizable](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreensizable-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ShowSlideInScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showslideinscreen-panels-comfort-panels-rt-advanced) | No | No | No | Yes | Yes | Yes |
| [ShowSoftwareVersion](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsoftwareversion-panels-comfort-panels-rt-advanced) | No | No | Yes | Yes | Yes | Yes |
| [ShowSystemDiagnosticsWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemdiagnosticswindow-panels-comfort-panels) | No | No | No | Yes | Yes | Yes |
| [ShowSystemAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemalarm-panels-comfort-panels-rt-advanced) | Yes | Yes | Yes | Yes | Yes | Yes |

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | Only for Mobile Panel 277, Mobile Panel 277 IWLAN |
| <sup>2)</sup> | Not available for devices as of device version V14.0 and higher |
| <sup>3)</sup> | Not for F Panels |

---

**See also**

[LinearScaling (Basic Panels, Panels, Comfort Panels, RT Advanced)](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#linearscaling-basic-panels-panels-comfort-panels-rt-advanced)
  
[TerminatePROFIsafe (Panels, Comfort Panels, RT Advanced)](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#terminateprofisafe-panels-comfort-panels-rt-advanced)

##### System functions for Runtime Advanced (RT Advanced)

###### Availability of system functions

The following table shows the availability of the system functions for WinCC RT Advanced.

Technical data subject to change.

###### Overview

|  | WinCC RT Advanced |
| --- | --- |
| User-defined functions | Yes |
| [Logoff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logoff-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ActivateScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ActivateScreenByNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatescreenbynumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ActivatePLCCodeViewer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activateplccodeviewer-panels-comfort-panels-rt-advanced) | Yes |
| [ActivateCleanScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatecleanscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ActivatePreviousScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatepreviousscreen-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [UpdateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#updatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [AdjustContrast](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#adjustcontrast-basic-panels-panels-comfort-panels-rt-advanced) | No |
| [Logon](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logon-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ArchiveLogFile](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#archivelogfile-panels-comfort-panels-rt-advanced) | Yes |
| [LogTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logtag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [EditAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#editalarm-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectCursorDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursordown-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectCursorUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorup-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectCursorLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectCursorRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectcursorright-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ScreenObjectPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#screenobjectpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [Encode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encode-panels-comfort-panels-rt-advanced) | Yes |
| [EncodeEx](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#encodeex-panels-comfort-panels-rt-advanced) | Yes |
| [DirectKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkey-panels-comfort-panels-rt-advanced) | No |
| [DirectKeyScreenNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#directkeyscreennumber-panels-comfort-panels-rt-advanced) | No |
| [PrintScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printscreen-panels-comfort-panels-rt-advanced) | Yes |
| [PrintReport](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printreport-panels-comfort-panels-rt-advanced) | Yes |
| [NotifyUserAction](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#notifyuseraction-panels-comfort-panels-rt-advanced) | Yes |
| [IncreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [IncreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#increasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ExportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ExportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | No |
| [ExportImportUserAdministration](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#exportimportuseradministration-panels-comfort-panels-rt-advanced) | Yes |
| [GoToHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotohome-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GoToEnd](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gotoend-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SafelyRemoveHardware](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#safelyremovehardware-basic-panels-panels-comfort-panels) | No |
| [HTMLBrowserStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrolldown-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserrefresh-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollup-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomin-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserzoomout-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserscrollright-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserPageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserPageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserpageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserHome](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserhome-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [HTMLBrowserBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#htmlbrowserback-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ImportDataRecords](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecords-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ImportDataRecordsWithChecksum](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced) | Yes |
| [InvertBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [InvertBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [InvertLinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#invertlinearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [CalibrateTouchScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#calibratetouchscreen-basic-panels-panels-comfort-panels-rt-advanced) | No |
| [CopyLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#copylog-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewScrollForward](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollforward-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewScrollBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewscrollback-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewExtend](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewextend-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewCompress](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewcompress-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewRulerLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerleft-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewRulerRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewrulerright-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewSetRulerMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewsetrulermode-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewStartStop](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewstartstop-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [TrendViewBackToBeginning](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#trendviewbacktobeginning-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [LoadDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#loaddatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GetUserName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getusername-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GetDataRecordName](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordname-panels-comfort-panels-rt-advanced) | Yes |
| [GetDataRecordTagsFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getdatarecordtagsfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GetGroupNumber](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getgroupnumber-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [GetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#getbrightness-panels-comfort-panels-rt-advanced) | No |
| [ReadPassword](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#readpassword-basic-panels-panels-comfort-panels-rt-advanced) | No <sup>1)</sup> |
| [LinearScaling](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#linearscaling-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ClearLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearlog-panels-comfort-panels-rt-advanced) | Yes |
| [ClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ClearDataRecordMemory](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#cleardatarecordmemory-panels-comfort-panels-rt-advanced) | No |
| [ClearAlarmBuffer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbuffer-panels-comfort-panels-rt-advanced) | Yes |
| [ClearAlarmBufferProTool](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#clearalarmbufferprotool-panels-comfort-panels-rt-advanced) | Yes |
| [AlarmViewUpdate](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewupdate-panels-comfort-panels-rt-advanced) | Yes |
| [AlarmViewLoopInAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewloopinalarm-panels-comfort-panels-rt-advanced) | Yes |
| [AlarmViewAcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewacknowledgealarm-panels-comfort-panels-rt-advanced) | Yes |
| [AlarmViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#alarmviewshowoperatornotes-panels-comfort-panels-rt-advanced) | Yes |
| [OpenAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openalllogs-panels-comfort-panels-rt-advanced) | Yes |
| [OpenScreenKeyboard](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openscreenkeyboard-panels-comfort-panels-rt-advanced) | Yes |
| [OpenControlPanelDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpaneldialog-panels-comfort-panels-rt-advanced) | No |
| [OpenCommandPrompt](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencommandprompt-panels-comfort-panels-rt-advanced) | No |
| [OpenInternetExplorer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#openinternetexplorer-panels-comfort-panels-rt-advanced) | No |
| [OpenControlPanel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opencontrolpanel-panels-comfort-panels-rt-advanced) | No |
| [OpenTaskManager](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opentaskmanager-panels-comfort-panels-rt-advanced) | Yes |
| [AcknowledgeAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#acknowledgealarm-panels-comfort-panels-rt-advanced) | Yes |
| [PDFScrollDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrolldown-panels-comfort-panels-rt-advanced) | Yes |
| [PDFScrollUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollup-panels-comfort-panels-rt-advanced) | Yes |
| [PDFFitToWidth](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittowidth-panels-comfort-panels-rt-advanced) | Yes |
| [PDFFitToHeight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdffittoheight-panels-comfort-panels-rt-advanced) | Yes |
| [PDFGotoFirstPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotofirstpage-panels-comfort-panels-rt-advanced) | Yes |
| [PDFGotoLastPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotolastpage-panels-comfort-panels-rt-advanced) | Yes |
| [PDFGotoNextPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotonextpage-panels-comfort-panels-rt-advanced) | Yes |
| [PDFGotoPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopage-panels-comfort-panels-rt-advanced) | Yes |
| [PDFGotoPreviousPage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfgotopreviouspage-panels-comfort-panels-rt-advanced) | Yes |
| [PDFZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomin-panels-comfort-panels-rt-advanced) | Yes |
| [PDFZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomout-panels-comfort-panels-rt-advanced) | Yes |
| [PDFScrollLeft](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollleft-panels-comfort-panels-rt-advanced) | Yes |
| [PDFScrollRight](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfscrollright-panels-comfort-panels-rt-advanced) | Yes |
| [PDFZoomOriginal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pdfzoomoriginal-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewDetails](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewdetails-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewNextNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewnextnetwork-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewStepMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewstepmode-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewSymbols](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewsymbols-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewTransitionInterlock](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewtransitioninterlock-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewZoomIn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomin-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewZoomOut](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewzoomout-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeViewPreviousNetwork](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodeviewpreviousnetwork-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewNewDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewnewdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewGetDataRecordFromPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewgetdatarecordfromplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewClearDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewcleardatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [PLCCodeDisplayMonitoringOrFBCall](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#plccodedisplaymonitoringorfbcall-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewMenu](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewmenu-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewOpen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewopen-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewSetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsetdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewSaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsavedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewSaveAsDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsaveasdatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewSynchronizeDataRecordWithTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewsynchronizedatarecordwithtags-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewRenameDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewrenamedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewshowoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [RecipeViewBack](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#recipeviewback-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ResetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ResetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resetbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [PressButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pressbutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ReleaseButton](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#releasebutton-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ShiftAndMask](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#shiftandmask-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [CloseAllLogs](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#closealllogs-panels-comfort-panels-rt-advanced) | Yes |
| [SetDataRecordToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetDataRecordTagsToPLC](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdatarecordtagstoplc-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [PageDown](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pagedown-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [PageUp](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#pageup-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SendEMail](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#sendemail-panels-comfort-panels-rt-advanced) | Yes |
| [SetAcousticSignal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setacousticsignal-panels-comfort-panels-rt-advanced) | No |
| [SetDisplayMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdisplaymode-panels-comfort-panels-rt-advanced) | Yes |
| [SetDeviceMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdevicemode-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetBit](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbit-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetBitInTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitintag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetBitWhileKeyPressed](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbitwhilekeypressed-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetBacklightColor](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbacklightcolor-basic-panels-panels-comfort-panels-rt-advanced) | No |
| [SetBrightness](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setbrightness-panels-comfort-panels-rt-advanced) | No |
| [SetScreenKeyboardMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setscreenkeyboardmode-panels-comfort-panels-rt-advanced) | Yes |
| [SetAlarmReportMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setalarmreportmode-panels-comfort-panels-rt-advanced) | Yes |
| [SetRecipeTags](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setrecipetags-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetDaylightSavingTime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setdaylightsavingtime-panels-comfort-panels-rt-advanced) | Yes |
| [SetLanguage](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setlanguage-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetConnectionMode](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setconnectionmode-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SetWebAccess](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#setwebaccess-panels-comfort-panels-rt-advanced) | Yes |
| [BackupRAMFileSystem](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#backupramfilesystem-panels-comfort-panels-rt-advanced) | No |
| [SimulateSystemKey](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatesystemkey-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SimulateTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#simulatetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewRefresh](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewrefresh-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewReadOnlyOff](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyoff-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewReadOnlyOn](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewreadonlyon-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewDisconnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewdisconnect-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewConnect](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewconnect-panels-comfort-panels-rt-advanced) | Yes |
| [SmartClientViewLeave](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#smartclientviewleave-panels-comfort-panels-rt-advanced) | Yes |
| [SaveDataRecord](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#savedatarecord-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [StartLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startlogging-panels-comfort-panels-rt-advanced) | Yes |
| [StartNextLog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startnextlog-panels-comfort-panels-rt-advanced) | Yes |
| [StartProgram](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#startprogram-panels-comfort-panels-rt-advanced) | Yes |
| [StatusForceGetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcegetvalues-panels-comfort-panels-rt-advanced) | Yes |
| [StatusForceSetValues](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#statusforcesetvalues-panels-comfort-panels-rt-advanced) | Yes |
| [ControlSmartServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlsmartserver-panels-comfort-panels-rt-advanced) | Yes |
| [ControlWebServer](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#controlwebserver-panels-comfort-panels-rt-advanced) | Yes |
| [StopLogging](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stoplogging-panels-comfort-panels-rt-advanced) | Yes |
| [StopRuntime](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#stopruntime-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ActivateSystemDiagnosticsView](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced) | Yes |
| [LookupText](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#lookuptext-panels-comfort-panels-rt-advanced) | Yes |
| [ResetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#resettagtohandwheel-panels-comfort-panels-rt-advanced) | No |
| [SetTagToHandWheel](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#settagtohandwheel-panels-comfort-panels-rt-advanced) | No |
| [TraceUserChange](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#traceuserchange-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [DecreaseFocusedValue](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasefocusedvalue-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [DecreaseTag](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#decreasetag-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ChangeConnection](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnection-panels-comfort-panels-rt-advanced) | Yes |
| [ChangeConnectionEIP](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#changeconnectioneip-panels-comfort-panels-rt-advanced) | Yes |
| [ShowBlockInTiaPortal](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showblockintiaportal-rt-advanced) | Yes |
| [ShowLogonDialog](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showlogondialog-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ShowOperatorNotes](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showoperatornotes-basic-panels-panels-comfort-panels-rt-advanced) | Yes |
| [ShowAlarmWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showalarmwindow-panels-comfort-panels-rt-advanced) | Yes |
| [ShowPopupScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreen-panels-comfort-panels-rt-advanced) | Yes |
| [ShowPopupScreenSizable](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showpopupscreensizable-panels-comfort-panels-rt-advanced) | Yes |
| [ShowSlideInScreen](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showslideinscreen-panels-comfort-panels-rt-advanced) | Yes |
| [ShowSoftwareVersion](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsoftwareversion-panels-comfort-panels-rt-advanced) | Yes |
| [ShowSystemDiagnosticsWindow](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemdiagnosticswindow-panels-comfort-panels) | Yes |
| [ShowSystemAlarm](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showsystemalarm-panels-comfort-panels-rt-advanced) | Yes |

| Symbol | Meaning |
| --- | --- |
| 1) | Not available for devices as of device version V14.0 and higher |

---

**See also**

[TerminatePROFIsafe (Panels, Comfort Panels, RT Advanced)](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#terminateprofisafe-panels-comfort-panels-rt-advanced)

##### System functions for Runtime Professional (RT Professional)

###### Availability of system functions

The following table shows the availability of the system functions for WinCC Runtime Professional.

Technical data subject to change.

###### Overview

|  | WinCC RT Professional |
| --- | --- |
| User-defined functions | Yes |
| [ActivateScreen](System%20functions%20%28RT%20Professional%29.md#activatescreen-rt-professional) | Yes |
| [ActivateScreenInCurrentScreenWindow](System%20functions%20%28RT%20Professional%29.md#activatescreenincurrentscreenwindow-rt-professional) | Yes |
| [ActivateScreenInScreenWindow](System%20functions%20%28RT%20Professional%29.md#activatescreeninscreenwindow-rt-professional) | Yes |
| [IncreaseTag](System%20functions%20%28RT%20Professional%29.md#increasetag-rt-professional) | Yes |
| [ExportImportUserAdministration](System%20functions%20%28RT%20Professional%29.md#exportimportuseradministration-rt-professional) | Yes |
| [InvertBit](System%20functions%20%28RT%20Professional%29.md#invertbit-rt-professional) | Yes |
| [InvertBitInTag](System%20functions%20%28RT%20Professional%29.md#invertbitintag-rt-professional) | Yes |
| [InvertLinearScaling](System%20functions%20%28RT%20Professional%29.md#invertlinearscaling-rt-professional) | Yes |
| [LinearScaling](System%20functions%20%28RT%20Professional%29.md#linearscaling-rt-professional) | Yes |
| [ResetBit](System%20functions%20%28RT%20Professional%29.md#resetbit-rt-professional) | Yes |
| [ResetBitInTag](System%20functions%20%28RT%20Professional%29.md#resetbitintag-rt-professional) | Yes |
| [SetBit](System%20functions%20%28RT%20Professional%29.md#setbit-rt-professional) | Yes |
| [SetBitInTag](System%20functions%20%28RT%20Professional%29.md#setbitintag-rt-professional) | Yes |
| [SetPropertyCurrentWindow](System%20functions%20%28RT%20Professional%29.md#setpropertycurrentwindow-rt-professional) | Yes |
| [SetPropertyCurrentWindowByProperty](System%20functions%20%28RT%20Professional%29.md#setpropertycurrentwindowbyproperty-rt-professional) | Yes |
| [SetPropertyCurrentWindowByTagIndirect](System%20functions%20%28RT%20Professional%29.md#setpropertycurrentwindowbytagindirect-rt-professional) | Yes |
| [SetPropertyByProperty](System%20functions%20%28RT%20Professional%29.md#setpropertybyproperty-rt-professional) | Yes |
| [SetPropertyByConstant](System%20functions%20%28RT%20Professional%29.md#setpropertybyconstant-rt-professional) | Yes |
| [SetPropertyByTag](System%20functions%20%28RT%20Professional%29.md#setpropertybytag-rt-professional) | Yes |
| [SetPropertyByTagIndirect](System%20functions%20%28RT%20Professional%29.md#setpropertybytagindirect-rt-professional) | Yes |
| [SetTag](System%20functions%20%28RT%20Professional%29.md#settag-rt-professional) | Yes |
| [SetTagByProperty](System%20functions%20%28RT%20Professional%29.md#settagbyproperty-rt-professional) | Yes |
| [SetTagByTagIndirect](System%20functions%20%28RT%20Professional%29.md#settagbytagindirect-rt-professional) | Yes |
| [SetTagWithOperatorEvent](System%20functions%20%28RT%20Professional%29.md#settagwithoperatorevent-rt-professional) | Yes |
| [SetTagIndirect](System%20functions%20%28RT%20Professional%29.md#settagindirect-rt-professional) | Yes |
| [SetTagIndirectByProperty](System%20functions%20%28RT%20Professional%29.md#settagindirectbyproperty-rt-professional) | Yes |
| [SetTagIndirectByTagIndirect](System%20functions%20%28RT%20Professional%29.md#settagindirectbytagindirect-rt-professional) | Yes |
| [StopRuntime](System%20functions%20%28RT%20Professional%29.md#stopruntime-rt-professional) | Yes |
| [DecreaseTag](System%20functions%20%28RT%20Professional%29.md#decreasetag-rt-professional) | Yes |
| [ShowLogonDialog](System%20functions%20%28RT%20Professional%29.md#showlogondialog-rt-professional) | Yes |
| [ShowPLCCodeViewFromAlarm](System%20functions%20%28RT%20Professional%29.md#showplccodeviewfromalarm-rt-professional) | Yes |
| [ShowBlockInTiaPortalFromAlarm](System%20functions%20%28RT%20Professional%29.md#showblockintiaportalfromalarm-rt-professional) | Yes |

---

**See also**

[ActivateScreen (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#activatescreen-panels-comfort-panels-rt-advanced-rt-professional)
  
[ActivateScreenInScreenWindow (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#activatescreeninscreenwindow-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetPropertyByConstant (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setpropertybyconstant-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetPropertyByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setpropertybyproperty-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetPropertyByTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setpropertybytag-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetPropertyByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setpropertybytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagindirect-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagIndirectByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagindirectbyproperty-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagIndirectByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagindirectbytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagWithOperatorEvent (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagwithoperatorevent-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagbyproperty-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetTagByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settagbytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
  
[IncreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#increasetag-panels-comfort-panels-rt-advanced-rt-professional)
  
[InvertBit (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#invertbit-panels-comfort-panels-rt-advanced-rt-professional)
  
[InvertBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#invertbitintag-panels-comfort-panels-rt-advanced-rt-professional)
  
[InverseLinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#inverselinearscaling-panels-comfort-panels-rt-advanced-rt-professional)
  
[LinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#linearscaling-panels-comfort-panels-rt-advanced-rt-professional)
  
[ResetBit (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#resetbit-panels-comfort-panels-rt-advanced-rt-professional)
  
[ResetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#resetbitintag-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetBit (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setbit-panels-comfort-panels-rt-advanced-rt-professional)
  
[SetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setbitintag-panels-comfort-panels-rt-advanced-rt-professional)
  
[StopRuntime (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#stopruntime-panels-comfort-panels-rt-advanced-rt-professional)
  
[DecreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#decreasetag-panels-comfort-panels-rt-advanced-rt-professional)

### VB scripting (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [System functions (Panels, Comfort Panels, RT Advanced)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#system-functions-panels-comfort-panels-rt-advanced)
- [System functions (Panels, Comfort Panels, RT Advanced, RT Professional)](System%20functions%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-panels-comfort-panels-rt-advanced-rt-professional)
- [VBScript for Windows (Panels, Comfort Panels, RT Advanced, RT Professional)](VBScript%20for%20Windows%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#vbscript-for-windows-panels-comfort-panels-rt-advanced-rt-professional)
- [VBScript for Windows CE (Panels, Comfort Panels)](VBScript%20for%20Windows%20CE%20%28Panels%2C%20Comfort%20Panels%29.md#vbscript-for-windows-ce-panels-comfort-panels)
- [VBS object model (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#vbs-object-model-panels-comfort-panels-rt-advanced-rt-professional)
