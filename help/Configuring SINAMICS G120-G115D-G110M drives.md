---
title: "Configuring SINAMICS G120/G115D/G110M drives"
package: StdrG120ConfenUS
topics: 144
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring SINAMICS G120/G115D/G110M drives

This section contains information on the following topics:

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Operating Startdrive](#operating-startdrive)
- [Commissioning drives](#commissioning-drives)
- [Going online and performing diagnostics](#going-online-and-performing-diagnostics)

## Overview

This section contains information on the following topics:

- [Startdrive - Overview](#startdrive---overview)
- [Drive components](#drive-components)
- [Drive interfaces enabled for Startdrive](#drive-interfaces-enabled-for-startdrive)
- [HSP online help](#hsp-online-help)
- [Using the help and function diagrams](#using-the-help-and-function-diagrams)
- [Application examples for SINAMICS drives](#application-examples-for-sinamics-drives)

### Startdrive - Overview

The Startdrive integrated engineering tool is available for the configuration and parameter assignment of drives in the TIA Portal.

You can perform the following tasks, for example, with Startdrive:

- Create projects for drive-specific solutions.
- Insert drives in the project as single drives or link the drives to higher-level controllers.
- Configure drives by entering the used power units, motors and encoders.
- Assign parameters to the drives by specifying command sources, setpoint sources and control type.
- Extend the parameter assignment with drive-specific functions such as the free function blocks and a technology controller.
- Go online on the drive and test the parameter assignment via the drive control panel.
- Perform diagnostics when an error occurs.

#### Startdrive user interface

Startdrive is integrated seamlessly in the TIA Portal. The graphic user interface provides support during the configuration and parameter assignment:

- Use the "Drive wizard" to configure the drive and select motors and the operating mode.
- Use the "Parameterization editor" to optimally adapt the drive according to the drive task.
- Insert specific components such as power modules in the "Device configuration".
- In the "Network view", network the drive with a higher-level controller and assign parameters for the communication.
- In online mode, test the drive with the drive control panel and load the parameter assignment to the drive.

### Drive components

#### Drive components in the drive line-up

Usually a drive system comprises several components:

- Control Unit

  The Control Unit controls and monitors the Power Module and the connected motor using several different selectable control types. The Control Unit is used to control the converter locally or centrally.
- Power unit (Power Module)

  Power units supply the motor in a defined power range.
- Motor

  A wide range of motor models are available.
- Encoder

  Encoders determine the current position of the drive shaft.
- Reactors and filters

  - The converter achieves a higher radio interference class with an external line filter.
  - The line reactor supports the overvoltage protection, smoothes the harmonics in the power supply and bridges commutation notches.
  - The braking resistor allows fast braking of loads with a high moment of inertia.
  - Output reactors reduce the voltage load on the motor windings.
  - The sine-wave filter at the converter output supplies practically sinusoidal voltages at the motor so that you can use standard motors without special cables.

You can edit the various drive components in Startdrive via the wizard, the function view, or the parameter view.

### Drive interfaces enabled for Startdrive

#### Drive interfaces

Various interfaces are available on the CU depending on the drive. The table shows which interface has been enabled for working with Startdrive.

| Interface/connector (type available or not depending on the CU) | Type | Protocol | Enable for Startdrive |
| --- | --- | --- | --- |
| Mini USB | USB | USB | Yes |
| Sub-D | RS232 | USS | No |
| Sub-D | RS485 | USS/Modbus/BacNet | No |
| Sub-D | RS485 | PROFIBUS DP | Yes |
| RJ45 | Ethernet | PROFINET | Yes |

### HSP online help

#### Installing HSP

You install a new firmware version for SINAMICS drives with an HSP (Hardware Support Package). A set of online helps and function diagrams corresponding to the drive firmware is also installed with the drive firmware.

After the installation, the online helps are displayed in the "Support Packages" directory in the TIA Portal online help.

### Using the help and function diagrams

This section contains information on the following topics:

- [Online helps for drives](#online-helps-for-drives)
- [Using Function Diagrams](#using-function-diagrams)

#### Online helps for drives

Additional information can be found in the online helps for the special requirements of the drive commissioning, which you can call via links:

- Information about drive parameters and alarms/faults
- Function diagrams

##### Drive parameters and alarms/faults

These helps provide information on all parameters and alarms/faults used for this drive. The helps are updated for each drive version. However, only the most recent version of these descriptions is available.

##### Function diagrams

The function diagrams are available in PDF format, which has the advantage that diagrams can be printed in high quality. The function diagrams are also updated for each version.

#### Using Function Diagrams

A block with function diagrams is available for each drive family. Function diagrams are signal flow charts that represent a controller, for example, and arranged side-by-side display the structure of the closed-loop control. The masks of the program user interface are based on these function diagrams, but usually do not display all parameters for reasons of clarity.

Function diagrams have the following structure:

![Function diagrams](images/103316951947_DV_resource.Stream@PNG-en-US.png)

Function diagrams

Function diagram description

| Field |  | Meaning |
| --- | --- | --- |
| In the footer |  |  |
| ① | DO | Displays the DOs (drive objects) for which the function diagram applies, e.g. SERVO or CU. |
| ② | Description | Describes the contents of the function diagram, e.g. servo control - speed controller with encoder. |
| ③ | Date/version | Displays the date when saved and the firmware version. In principle, function diagrams are only available for the current SINAMICS firmware. |
| ④ | Device | Displays the device for which the function diagram applies. |
| ⑤ | Diagram number | Displays the diagram number. |
| Diagram contents |  |  |
| ⑥ | Signal path number | The signal path number is displayed in the footer. The function diagram is divided into eight (not subdivided) fields. These fields are used for navigation within the diagram. Links to other function diagrams always contain the signal path number in addition to the diagram number so that it is easier to find the link target. |
| ⑦ | Links to other diagrams | The links to other diagrams can also be seen in the diagram. The structure of the links is as follows:  - Function block number - Signal path number (separated by a dot) |
| ⑧ | Footnotes | Footnotes are identified in the text by angular brackets, e.g. &lt;1&gt; |
| ⑨ | Sampling Times | If required, the sampling times that apply for this diagram are shown in the diagrams (rounded rectangle). |
| ⑩ | BICO interconnections | Signals are interconnected via BICO. |
| ⑪ | Icons | The signal flow in the function diagram is illustrated by various symbols. An overview of these symbols can be found in diagrams 1020 - 1025. |

### Application examples for SINAMICS drives

Application examples for SINAMICS drives can be found [at](https://www.automation.siemens.com/mc-app/sinamics-application-examples/Home/Index?language=en).

## Getting Started

This section contains information on the following topics:

- [Getting Started - Startdrive](#getting-started---startdrive)

### Getting Started - Startdrive

#### Information on Startdrive

You can find information on Startdrive, including a link to the "Getting Started" section for Startdrive, on the online product page.

You can find the product page at [Getting Started - Startdrive](http://w3.siemens.com/mcms/mc-solutions/en/engineering-software/startdrive/Pages/getting-started.aspx).

## Operating Startdrive

This section contains information on the following topics:

- [Structure of the user interface - overview](#structure-of-the-user-interface---overview)
- [Parameterization](#parameterization)
- [Commissioning](#commissioning)
- [Online and diagnostics](#online-and-diagnostics)
- [Device view and network view](#device-view-and-network-view)

### Structure of the user interface - overview

This section contains information on the following topics:

- [Structure of the user interface for the drive parameterization](#structure-of-the-user-interface-for-the-drive-parameterization)
- [Drives in the project navigation](#drives-in-the-project-navigation)

#### Structure of the user interface for the drive parameterization

##### Project view in Startdrive

As part of the TIA Portal, the project view for Startdrive is structured accordingly.

The following figure shows an example of the components of the project view:

![Project view in Startdrive](images/103317108363_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Project navigation |
| ② | Detail view |
| ③ | Working area |
| ④ | Inspector window |

#### Drives in the project navigation

##### Description

The project navigation is used to display and edit components and project data.

After being inserted, drives are displayed as follows in the project navigation:

![Project navigation](images/103317147531_DV_resource.Stream@PNG-en-US.png)

Project navigation

| Entry | Description |
| --- | --- |
| [Device view and network view](#device-view-and-network-view) | Opens the device configuration of the drive. |
| [Parameter](#parameterization) | Opens the parameterization editor to assign the drive parameters via the wizard, the function view or the parameter view. |
| [Commissioning](#commissioning) | Opens the commissioning editor in which you can run through the online wizard, operate the drive control panel or perform the motor optimization. |
| [Online and diagnostics](#online-and-diagnostics) | Opens the diagnostics editor with which you can diagnose the online access, acknowledge alarms or view the message history. |
| Trace | Opens the trace with which you can record signals. |

##### Shortcut menu

The shortcut menu of a drive in the project navigator contains the following entries:

| Menu item | Description |
| --- | --- |
| Open | Opens the device view of the drive. |
| Parameter | Opens the parameter view in the working area. |
| Cut | Cuts out the selected content and copies it to the clipboard. |
| Copy | Copies the content to the clipboard. |
| Paste | Pastes the contents of the clipboard to the project navigator. |
| Delete | Deletes the selected content from the project navigator. |
| Rename | Allows a name to be changed |
| Go to topology view | Opens the topology view for drives that are networked via PROFINET. |
| Go to network view | Opens the network view. |
| Download to device | Downloads the data from the project to the drive (online only). |
| Upload from device (software) | Uploads the data from the device to the project (online only). |
| Compile | Compiles existing programs. |
| Download to device | Downloads the changes in the programs to the device. |
| Go online | Establishes an online connection to the drive. |
| Go offline | Cancels the online connection, the drive goes offline. |
| Commissioning | Opens the commissioning editor. |
| Online &amp; diagnostics | Opens the Online &amp; diagnostics editor; if the drive is not online, Startdrive tries to establish an online connection. |
| Properties | Opens the Properties dialog box of the drive. You can set, for example, the bus parameters there. |

### Parameterization

This section contains information on the following topics:

- [Parameterization editor](#parameterization-editor)
- [Wizard](#wizard)
- [Function view](#function-view)
- [Parameter view](#parameter-view)

#### Parameterization editor

##### Parameterization editor

The parameterization editor comprises two tabs in which the drive is parameterized:

- You use screen forms in the function view to parameterize the drive. They are similar to function diagrams, but do not contain all the parameters.
- All the drive parameters are listed in the parameter view, so that the drive can be completely parameterized there.

##### Structure of the parameterization editor

The following figure shows the structure of the parameterization editor:

![Structure of the parameterization editor](images/117625290507_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Function view tab |
| ③ | Parameter view tab |

##### Secondary navigation

In the secondary navigation, navigate through the individual areas of the selected tab sorted according to topic.

##### Menu bar

The menu bar provides the following functions:

- "Command data set"; allows the command data set to be selected.
- "Drive data set"; allows the drive data set to be selected.
- "Start safety commissioning"; allows the parameterization function for Safety Integrated to be activated

##### Function view tab

You parameterize the drive using a graphical user interface in the "Function view" tab. The masks are derived from the respective function diagrams.

##### Parameter view tab

You parameterize the drive via the settings that you make directly on the parameters in the "Parameter view" tab.

#### Wizard

##### Wizard for configuring the drive

You configure the drive with the wizard. For example, you select the control type, the motor or the drive data set.

##### Structure of the wizard

The following figure shows the structure of the wizard:

![Structure of the wizard](images/103317207691_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Table of contents |
| ② | Working area |
| ③ | Navigation area |

##### Table of contents

The individual steps are listed in the table of contents. The settings that have already been run through are highlighted in color.

##### Working area

You enter the settings in the working area.

##### Navigation area

Use the buttons in the navigation area as follows:

- To call the previous dialog box, click "Back". The settings are retained.
- To call the next dialog box, click "Next".
- To exit the wizard and accept the settings, click "Finish". The button is only active after running through the wizard.
- To exit the wizard and reject the settings, click "Cancel".

#### Function view

##### Masks for the parameterization of drives

You parameterize the drive using a graphical user interface in the "Function view". The individual masks are based on function diagrams and contain the most important parameters.

##### Structure of the masks

The following figure shows an example of a mask structure:

![Structure of the masks](images/173770205835_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1) | Secondary navigation |
| 2) | Select command and drive data sets |
| 3) | Title of the mask |
| 4) | Button for assigning safety parameters |
| 5) | Button for the next mask |
| 6) | Button for the previous mask |
| 7) | Fields for entering parameters / interconnecting BICO signals |

#### Parameter view

##### Parameter view (expert list)

The "Parameter view" provides a clearly organized display of the parameters available for the device. To facilitate the locating of parameters, the parameters are assigned to menu items according to topic in the secondary navigation.

##### Parameter display

The fields of the individual parameters are displayed in the list in color as follows:

| Editing level | Offline color | Online color |
| --- | --- | --- |
| Read only | Gray | Pale orange |
| Read/write | White | Orange |
| Dynamically locked | White with lock symbol | Orange with lock symbol |

##### Structure of the parameter view

The following figure shows the structure of the parameter view:

![Parameter list](images/163409899147_DV_resource.Stream@PNG-en-US.png)

Parameter list

| Symbol | Meaning |
| --- | --- |
| 1) | Secondary navigation: limits the parameter display to the required parameter group. |
| 2) | Drop-down list to restrict the parameter views:  - Display standard parameters - Display extended parameters - Display service parameters: password is required to access these parameters. |
| 3) | Filter to restrict the display. The filter can be edited in each column and turned on and off globally at the filter symbol. |
| 4) | Parameter number |
| 5) | Start a comparison of parameter sets:  - Factory setting - Online/offline   Differences are displayed via the symbol |
| 6) | Starts a CSV export |
| 7) | Creates a user-defined parameter list |
| 8) | Save the user-defined parameter list |
| 9) | Open user-defined parameter list |
| 10) | Add comment in the user-defined parameter list |
| 11) | Accept values; transfer's user-defined parameter values into the device |
| 12) | Disable the comparison of the parameter values |
| 13) | Parameter text; displays name of the parameter |
| 14) | Parameter value. Dynamically locked parameters are identified by a "lock" symbol |
| 15) | Comparison; a symbol indicates whether the values differ (factory setting - online value; factory setting - offline value). |
| 16) | Factory setting; displays the parameter values of the factory setting |
| 17) | Unit; displays the unit of the parameter |
| 18) | Data set; currently displays data set of the parameter |
| 19) | Access level; displays the access level of the parameter |
| 20) | Minimum value |
| 21) | Maximum value |

##### Show columns

The information displayed for the parameters can be shown or hidden.

1. To show the shortcut menu, right-click the title bar of the table.
2. Select the columns that are to be shown in the parameter view.

---

**See also**

[Parameter description](#parameter-description)
  
[Editing the parameter list](#editing-the-parameter-list)

### Commissioning

This section contains information on the following topics:

- [Wizard](#wizard-1)

#### Wizard

##### Wizard for configuring the drive

You configure the drive with the wizard. For example, you select the control type, the motor or the drive data set.

##### Structure of the wizard

The following figure shows the structure of the wizard:

![Structure of the wizard](images/103317207691_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Table of contents |
| ② | Working area |
| ③ | Navigation area |

##### Table of contents

The individual steps are listed in the table of contents. The settings that have already been run through are highlighted in color.

##### Working area

You enter the settings in the working area.

##### Navigation area

Use the buttons in the navigation area as follows:

- To call the previous dialog box, click "Back". The settings are retained.
- To call the next dialog box, click "Next".
- To exit the wizard and accept the settings, click "Finish". The button is only active after running through the wizard.
- To exit the wizard and reject the settings, click "Cancel".

### Online and diagnostics

This section contains information on the following topics:

- [Diagnostics editor](#diagnostics-editor)

#### Diagnostics editor

##### Diagnostics editor

In the diagnostics editor, you work in online mode and, for example, view the drive alarms or drive history.

##### Structure of the diagnostics editor

The following figure shows the structure of the diagnostics editor:

![Structure of the diagnostics editor](images/103317332875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Online access |
| ② | Secondary navigation |
| ③ | Editor for the online access and diagnostics |

##### Online access

The currently used interface and parameters are displayed under "Online access".

##### General diagnostics

The general diagnostics lists the devices and manufacturer data.

##### Active messages

The "Active messages" dialog box shows currently active messages in online mode.

##### Message history

The "Message history" lists already acknowledged messages for a specific period.

##### Control and status words

"Control and status words" lists the signals that have been used.

##### Drive enables

"Drive enables" lists the drive enables that have already been set and those that are still missing.

##### Interconnections

The various BICO interconnections of the drive are listed in "Interconnections".

##### Commissioning interface

The properties of the commissioning interface used are shown in "Commissioning interface".

##### Safety diagnostics

The current state of the safety settings is shown in "Safety diagnostics".

##### Assign name (PROFINET IO only)

A PROFINET name can be assigned for the module under "Assign name".

##### Assign IP address (PROFINET IO only)

An IP address can be assigned for the module under "Assign IP address".

##### Backing up/reset

You can reset the parameters to the factory settings and back up the settings via "Copy RAM to ROM" under "Backing up/reset".

---

**See also**

[General diagnostics](#general-diagnostics)
  
[Active alarms and faults](#active-alarms-and-faults)
  
[Alarm and fault history](#alarm-and-fault-history)
  
[Control/status words](#controlstatus-words)
  
[Drive enables](#drive-enables)
  
[Commissioning interface](#commissioning-interface)
  
[Safety Integrated](#safety-integrated)

### Device view and network view

This section contains information on the following topics:

- [Device view](#device-view)
- [Network view](#network-view)

#### Device view

##### Device configuration

The device view is opened via the "Device configuration" entry in the project navigation.

![Drives in the device view](images/103317368587_DV_resource.Stream@PNG-en-US.png)

Drives in the device view

| Number | Description |
| --- | --- |
| ① | Drop-down list with the configured devices |
| ② | Device with configured modules |
| ③ | Device data |

The specific parameters of the selected element are displayed in the inspector window.

#### Network view

##### Displaying devices in the network view

The network view is opened via the "Devices &amp; networks" entry in the project navigation.

![Drives in the network view](images/103317405323_DV_resource.Stream@PNG-en-US.png)

Drives in the network view

| Number | Description |
| --- | --- |
| ① | Drive that is assigned as the IO device of a higher-level controller via fieldbus (here, PROFINET IO). |
| ② | Fieldbus (here, PROFINET IO) |
| ③ | Higher-level controller, a SIMATIC S7-1500 in this case, that is configured as IO controller. |
| ④ | Data from drive and controller |

The specific parameters of the selected element are displayed in the inspector window.

## Commissioning drives

This section contains information on the following topics:

- [Parameterizing drives](#parameterizing-drives)
- [Using the drive control panel](#using-the-drive-control-panel)
- [Motor optimization](#motor-optimization)
- [Save/Reset](#savereset)
- [Operating the drive on a controller](#operating-the-drive-on-a-controller)
- [Drives in the hardware catalog](#drives-in-the-hardware-catalog)
- [Using drive libraries](#using-drive-libraries)
- [Using know-how protection](#using-know-how-protection)
- [Upgrading devices and firmware](#upgrading-devices-and-firmware)

### Parameterizing drives

This section contains information on the following topics:

- [Parameter description](#parameter-description)
- [Using the parameter view](#using-the-parameter-view)
- [Using the function view](#using-the-function-view)
- [Data sets and BICO technology](#data-sets-and-bico-technology)

#### Parameter description

##### Parameter description

Parameters are the access points for the adaptation of the converters/drives and function blocks to the application, for interconnecting function blocks via connectors and binectors and for monitoring internal signals.

There are two types of parameters, display and adjustable parameters. The following figure shows the parameter list with r and p parameters.

![Parameter description](images/103317468427_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Display parameters (r) |
| ② | Adjustable parameters (p) |

##### Display parameters

Display parameters are preceded with the letter "r". You cannot change the value of these parameters.

Example: r0027 is the parameter for the converter output current. The converter measures the current and writes the current value to the parameter. You can display the parameter value, e.g. via an analog output on the converter.

##### Adjustable parameters

Adjustable parameters are preceded with the letter "p". You can change the value of these parameters within a defined range.

Example: p0305 is the parameter for the rated motor current in amps. The value of this parameter is specified during commissioning. You can enter values between 0 and 10000.

The process of changing parameter values is subject to certain conditions. The changing of the parameter may be rejected by the converter.

##### BICO parameters

See [BICO technology](#bico-technology) for a description of the BICO parameters.

##### Parameters with follow-on parameterization

When you change certain parameter values, the system may automatically change further parameters accordingly. This makes it much easier to parameterize complex functions. Parameters that are mutually dependent are then dynamically locked and cannot be changed.

##### Structure of the drive parameters

The drive parameters can be divided into the following categories:

- Arithmetic parameters; these parameters have a value that is displayed with the required accuracy.
- Enumeration parameters; these parameters have several values (enums) that are displayed via drop-down lists.
- Index parameters (array); these parameters contain an index which can be used to display several properties. These parameters are displayed in a tree structure.

  Example: r39[0] "Energy balance (sum)" and r39[1] "Energy drawn"
- Bit-coded parameters; these parameters contain a bit array which can be used to display settings with "0/1" or "True/False". These parameters are displayed in a tree structure.

  Example: "Missing enables" r46.0...31
- BiCO parameters; these parameters can be interconnected to other parameters.

##### Access levels

An access level is assigned to each parameter in the drive in order to be able to assign parameter access to certain roles. For further information, see [Editing the parameter list](#editing-the-parameter-list).

---

**See also**

[Parameter view](#parameter-view)
  
[BICO technology](#bico-technology)

#### Using the parameter view

This section contains information on the following topics:

- [Editing the parameter list](#editing-the-parameter-list)
- [Filtering the parameter list](#filtering-the-parameter-list)
- [Comparing parameter sets](#comparing-parameter-sets)
- [Searching for parameters](#searching-for-parameters)
- [User- defined parameter list](#user--defined-parameter-list)

##### Editing the parameter list

###### Working with the parameter list

The parameter list provides the following functions:

- Monitoring and editing of parameter values
- Restricting the parameter view
- Exporting as CSV file
- Showing and hiding columns

For information on the user interface, see also [Parameter view](#parameter-view).

###### Monitoring and editing of parameter values online

The input fields of the parameters that you can change online are displayed in orange after you have established an online connection with Startdrive.

To change the parameters online, follow these steps:

1. Establish an online connection.

   The display of the parameters changes to "orange".
2. Change the values, if required.
3. Accept the settings by pressing the ENTER key. The settings then take immediate effect in the drive.

###### Restricting the parameter view

The views of the parameter list are not identical to the access levels of the parameters. The "Standard parameters" view displays not only parameters of access level 1.

The parameter list provides the following views in Startdrive:

- Display standard parameters; this view displays the most important and typical parameters of the drive. This is the default setting.
- Display extended parameters; this view contains parameters that are required by experts for extended settings.
- Display service parameters; this view contains parameters that are required by service employees. Access is password-protected.

###### Exporting the parameter list as CSV file

CSV files can be opened in table calculation programs or editors.

To export the parameter list as a CSV file (comma separated values), proceed as follows:

1. Click the "Export displayed list as CSV file" button.

   The Export window opens:
2. Assign a name and click "Save".

   The list is saved as a CSV file.

##### Filtering the parameter list

###### Adapting the parameter view

The parameter list can be adapted in numerous ways through filters and sorting mechanisms so that only those parameters are displayed that you need. You can specify the displayed columns via the shortcut menu.

###### Using filters

There is a drop-down list below the header of every column to edit the filters. "&lt;All&gt;" is displayed as default setting.

To edit a filter, proceed as follows:

1. Click in the field and enter a value.

   The values are stored so that you can use the filters again.
2. If the drop-down list already contains values, select the appropriate value.
3. After entering the value, change to another field and press the "Enter" key on the keyboard.

   The parameter list is updated.
4. To display all parameters again, select "&lt;All&gt;" in the relevant drop-down list.
5. As soon as you have set a filter, a check mark is shown at the filter symbol in the first column.

You set the filters in the column headers of the parameter view:

| Column | Settings |
| --- | --- |
| Number | Filters the parameters according to the entered number |
| Parameter text | Filters the list according to the entered text |
| Comparison | Displays the parameters that are equal or unequal in a comparison |
| Factory setting | Filters the list according to the entered factory setting |
| Unit | Filters the list according to the entered unit |
| Data set | Filters the list according to the following data sets:  - Command data set (CDS) - Drive data set (DDS) - Motor data set (MDS) - Encoder data set (EDS) - Power unit data set (PDS) |
| Access level | Filters the list according to the entered access level |
| Minimum | Filters the list according to the entered minimum value |
| Maximum | Filters the list according to the entered maximum value |

##### Comparing parameter sets

###### Comparing parameters

The parameter list compares the values of online/offline parameter sets with the factory settings.

In the "Comparison" column, symbols indicate whether the parameter values are "equal", "unequal" or "unknown".

| Symbol | Description |
| --- | --- |
| ![Comparing parameters](images/103317558795_DV_resource.Stream@PNG-en-US.png) | The two parameter values are identical. |
| ![Comparing parameters](images/103317562507_DV_resource.Stream@PNG-en-US.png) | The offline parameter values are not the same as the factory settings. |
| ![Comparing parameters](images/103317569931_DV_resource.Stream@PNG-en-US.png) | The online parameter values are not the same as the factory settings. |
| ![Comparing parameters](images/103317566219_DV_resource.Stream@PNG-en-US.png) | The status is unknown. Parameters are being compared that have different units. |

###### Comparing online parameter values with offline parameter values

To compare the current online parameter values with the offline values, proceed as follows:

1. Go online.
2. Click the "Comparison" button.
3. Select "Offline values" in the displayed list.
4. Use the filter of the "Comparison" column to display the equal, unequal or unknown parameters.

###### Comparing offline parameter values with factory settings

To compare the current offline parameter values with the factory settings, proceed as follows:

1. Go online with the drive.
2. Click the "Comparison" button.
3. Select "Factory setting" in the displayed list.

   Use the filter of the "Comparison" column to display the equal, unequal or unknown parameters.

##### Searching for parameters

###### Searching for parameters

To display specific parameters in the parameter list, the following functions are available:

- Standard search of the TIA Portal
- Search mechanism in the parameter list

###### Using the standard search of the TIA Portal

The standard search is displayed below "Tasks" in the right-hand editor of the program user interface.

To use the standard search of the TIA Portal, proceed as follows:

1. Enter &lt;Ctrl+F&gt; via the keyboard to open the search dialog box.
2. Enter the parameter number that you want to find.

   Or
3. Enter a text that you want to find.
4. Click "Find" to start the search.

   If the parameter or text is found, the cursor jumps automatically to the position in the parameter list.
5. Press &lt;F3&gt; to jump to the next search result.

###### Search mechanism of the parameter list

The parameter list searches implicitly for entered parameter numbers.

To jump to a specific parameter, proceed as follows:

1. Set the cursor in the parameter list.
2. Enter the parameter number.

   The cursor jumps automatically to the entered parameter. If the search does not find the parameter, the closest parameter is displayed.

##### User- defined parameter list

This section contains information on the following topics:

- [Overview](#overview-1)
- [Creating user-defined parameter list](#creating-user-defined-parameter-list)
- [User-defined parameter list without values](#user-defined-parameter-list-without-values)
- [User-defined parameter list with values](#user-defined-parameter-list-with-values)
- [Editing the user-defined parameter list](#editing-the-user-defined-parameter-list)
- [Example 1 - Updating motor parameters](#example-1---updating-motor-parameters)
- [Example 2- Dynamic array parameters](#example-2--dynamic-array-parameters)

###### Overview

The user-defined parameter list is used to create list of favorite parameters. The list contains subset of the specific parameters from an native parameter list.

You can edit the values of the shortlisted parameters. For example: You can create a user-defined parameter list saved with values for a device and open the list in another device (preferably of same hardware configuration). You can compare the device values with the saved values and can accept the saved value for the device if required.

> **Note**
>
> Use the user-defined parameter list to edit the parameters across the device and do not use it to perform serial commissioning.

You can perform the following actions in the user-defined parameter list:

- Add the required parameters
- Assign a comment or heading to group the parameters

Parameters can also occur several times in the list with sorted or unsorted order. You can save user-defined parameter list in CSV (*.csv) format.

> **Note**
>
> - The list created is termed as user-defined list only when saved.
> - The user-defined parameter list can be saved with or without parameter values.

###### Creating user-defined parameter list

###### Procedure

To create user-defined parameter list, proceed as follows:

**Method 1**

1. In "Parameter View", click the "Create new user-defined parameter list" on the toolbar.  
   The "User list_#" tab opens (for example: User list_1, User list_2).
2. Enter the parameter number in the list or copy and paste the required parameters to the "User list_#".
3. Click "Save user-defined parameter list" on the toolbar.  
   The "Save result" dialog box appears as bellow:

   ![Procedure](images/116683147147_DV_resource.Stream@PNG-en-US.png)
4. Select the required option and click "Yes".  
   The "Save As" window opens.
5. Assign the path, name, and click "Save".
6. The list is saved as a CSV file.

**Method 2**

1. Select the required parameters from the list using "shift+click" or "ctrl+click".
2. Right-click and select "Create new user-defined parameter list" from the context menu.

   ![Procedure](images/116683373323_DV_resource.Stream@PNG-en-US.png)

   The "User list_#" tab opens with selected parameters added in the list.
3. Click "Save user-defined parameter list" on the toolbar.  
   The "Save result" dialog box appears as below:

   ![Procedure](images/116683147147_DV_resource.Stream@PNG-en-US.png)
4. Select the required option and click "Yes".  
   The "Save As" window opens.
5. Assign the path, name, and click "Save".  
   The list is saved as a CSV file.

**Method 3**

Each filtered group of parameters can also be saved as user-defined parameter list. To do this, proceed as follows:

1. Right-click on the expert list and select "Create new user-defined parameter list" from the context menu.

Or

1. Right-click on the expert list and select "Copy" from the context menu.
2. Open "User list_#".
3. Right-click in "User list_#" and select "Paste" from the context menu.

###### User-defined parameter list without values

In user-defined parameter list saved without values, the parameter values are also saved in the CSV file. The values are only for reference and are not displayed after opening the list. When parameter values are modified in the list, the values in the native parameter list also changes automatically. For more information on editing the user-defined parameter list, see also [Editing the user-defined parameter list](#editing-the-user-defined-parameter-list)

CSV file is as shown below:

![CSV file saved without values](images/116719194891_DV_resource.Stream@PNG-en-US.png)

CSV file saved without values

###### User-defined parameter list with values

If the user-defined parameter list is saved with values, then values and the units are stored for each parameter in the list. In this way, parameter settings can be saved and restored later or transferred to another device.

You can also edit the parameter value in the CSV file and restore to the device. CSV file is as shown below:

![CSV file saved with values](images/116683586955_DV_resource.Stream@PNG-en-US.png)

CSV file saved with values

> **Note**
>
> - The CSV file can get corrupted if you modify the general information.
> - In the CSV file, if the edited parameter value is invalid, then upon opening the file the user-defined parameter value will be reset to its default value. For numeric values the invalid entries will be highlighted in red color.

When you open the file in the "Parameter View", the current device values are compared with the values from the user-defined parameter list. If the device is online, the comparison is made with the online values; if the device is offline, the comparison is made with the offline values.

For information on how to work with user-defined parameter list, see also [Editing the user-defined parameter list](#editing-the-user-defined-parameter-list)

In the "Comparison" column, symbols indicate whether the parameter values are equal or not.

| Symbol | Parameter |
| --- | --- |
| ![Figure](images/103317558795_DV_resource.Stream@PNG-en-US.png) | The two parameter values are identical. |
| ![Figure](images/115670297355_DV_resource.Stream@PNG-en-US.png) | The two parameter values are not identical. |

Before opening a user-defined parameter list with values, perform the minimum commissioning of the drive which includes the following:

1. Add required DDS and CDS, see also [Data sets](#data-sets)
2. Select required function modules (applicable for CU250S-2)

###### Working with user defined parameter values

You need to accept the user-defined parameter values to further work on the user-defined parameter list.

To accept the user defined values, proceed as follows:

1. Click "Accept values" button on the toolbar.  
   The user-defined parameter values are transferred to the device.

> **Note**
>
> - You can accept values only once.
> - The user-defined values can be modified, but the parameter values are non-editable.

To edit the opened user-defined list with value, proceed as follows:

1. Click the "User value comparison / edit list" on the toolbar after accepting the values.  
   Comparison is removed and you can edit the list.

> **Note**
>
> Comparison can be removed only once you accept the values.

###### Working with unit parameters

If the saved list has different value for the unit parameters (p100, p505, and p595), then a dialog box appears with corresponding differences:

![Working with unit parameters](images/116719490827_DV_resource.Stream@PNG-en-US.png)

The corresponding parameters units get updated based on the value set in p100, p505, and p595. The parameters which can have different units based on the current setting of p100, p505 &amp; p595 are highlighted in red as shown below:

![Working with unit parameters](images/116719499403_DV_resource.Stream@PNG-en-US.png)

If you click on "Accept values", then a dialog box appears for confirmation as below:

![Working with unit parameters](images/116725408779_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If you save the user-defined parameter list in a lanuage and later open the list in a application with different language, then the units remain in the original language and are not converted.

###### Editing the user-defined parameter list

###### Working with user-defined parameter list

The user-defined parameter list provides the following functions:

- Adding a row
- Deleting a row
- Appending parameters to list
- Adding comments to list
- Opening the user-defined parameter list.

###### Adding a row

You can add a new row only at the end of the list.

###### Deleting a row

To delete a parameter, proceed as follows:

1. Select the parameter or a row.
2. Righ- click and select "Delete" from the context menu.

###### Appending parameters

To append parameter, procced as follows:

1. Select the required parameter  
   You can either select an native parameter list from the secondary navigation or any other required parameters available in "Parameter View".
2. Right-click and select "Append to user-defined parameter list".  
   The context menu provides options to select from the available user-defined parameter lists.
3. Select the required user-defined list.

The selected parameter is appended in the last row of the user defined list.

###### Adding comments

To add comment in user-defined parameter list, proceed as follows:

1. Right-click in "User list#" and select "Add comment" from the context menu.

Or

1. Click the "Add comment" on the toolbar.

The comment line is always added in the last row of the list.

###### Opening user-defined parameter list

To open the CSV file, proceed as follows:

1. Click "Open user-defined parameter list" on the toolbar.  
   "Open Result" dialog box appears.

   ![Opening user-defined parameter list](images/116726236555_DV_resource.Stream@PNG-en-US.png)
2. Select the required option and click "Yes".   
   "Open" window opens.
3. Select the CSV file and click "Open".

You can view the user defined parameter list in "Parameter View".

> **Note**
>
> - While opening, if a parameter in the CSV file is not present in the drive's parameter list, then the parameter is removed from the opened list and a message is displayed.
> - Configure the number of dynamic parameter (DDS, CDS, EDS) before opening user-defined parameter list.

###### Example 1 - Updating motor parameters

Create a user-defined parameter list with values in the below sequence to update motor parameters in drive. For more information, refer [Creating user-defined parameter list](#creating-user-defined-parameter-list).

![Parameter sequence to update motor parameters in drive](images/117195465995_DV_resource.Stream@PNG-en-US.png)

Parameter sequence to update motor parameters in drive

The parameter p10 is added twice to perform the commissioning. The first occurrence of p10 is to start quick commissioning and the second occurrence is to set the drive to "Ready" state.

To update motor parameters follow the below procedure:

1. Open the CSV file and edit the first occurrence of p10 value to "[1] Quick Commissioning".
2. Edit other parameter values as required.
3. Save the CSV file.
4. Select the drive in the project navigator.
5. Click "Go online".  
   An online connection is established, the color of the title bar changes to orange.
6. Open the user-defined parameter list saved in "Parameter View".

   ![Figure](images/117198299147_DV_resource.Stream@PNG-en-US.png)
7. Click "Accept values".  
   The motor parameters are edited and the comparison column shows the differences of values after accept.

   ![Figure](images/117202164747_DV_resource.Stream@PNG-en-US.png)

###### Example 2- Dynamic array parameters

Configure the dynamic parameters before opening the user-defined list to retain the values. If you miss to configure the dynamic parameters, below is the example to explain the behavior:

1. In the native parameter list set the parameter p180 value to 2.

   ![Figure](images/117468159243_DV_resource.Stream@PNG-en-US.png)
2. Create a user-defined parameter list with values by adding below parameters:

   ![Figure](images/117468590219_DV_resource.Stream@PNG-en-US.png)
3. Save and close the user-defined parameter list.
4. In the native parameter list modify the parameter p180 value to 1.

   ![Figure](images/117468624395_DV_resource.Stream@PNG-en-US.png)
5. Open the user-defined list saved earlier.   
   You can view DDS1 parameters in the list. All the DDS2 related parameters are filtered out and a message is displayed in "Info" tab.

   ![Figure](images/117468633227_DV_resource.Stream@PNG-en-US.png)

#### Using the function view

This section contains information on the following topics:

- [Editing parameters in the function view](#editing-parameters-in-the-function-view)

##### Editing parameters in the function view

###### Working in the function view

You edit the parameters in a straightforward graphical user interface in the function view. The screen forms are based on function diagrams that map the functions in signal flow diagrams. The signal flow is from left to right. The following can be performed on a screen form:

- Monitoring of parameter values
- Input of values
- Interconnection of BICO parameters, see also [Interconnecting binector and connector inputs](#interconnecting-binector-and-connector-inputs) and [Interconnecting binector and connector outputs](#interconnecting-binector-and-connector-outputs).

###### Working online

The input fields of the parameters that you can change online are displayed in orange after you have established an online connection with Startdrive.

To change the parameters online, follow these steps:

1. Establish an online connection.

   The display of the parameters changes to "orange".
2. Change the values, if required.
3. Accept the settings by pressing the ENTER key. The settings then take immediate effect in the drive.

###### Working offline

The function view does not show any online parameter values in offline mode, only the offline values currently saved in the project.

If you want to edit the parameter values offline with the function view, you must download the settings to the drive.

To establish an online connection with the function view, proceed as follows:

1. Click the "Go online" button.
2. To download the settings to the drive, click the "Download to device" button.

   The settings are downloaded to the drive.
3. If required, save the values retentively to the drive via "Save RAM data to EEPROM".

#### Data sets and BICO technology

This section contains information on the following topics:

- [BICO technology for drives](#bico-technology-for-drives)
- [Data sets](#data-sets)

##### BICO technology for drives

This section contains information on the following topics:

- [BICO technology](#bico-technology)
- [Interconnecting binector and connector inputs](#interconnecting-binector-and-connector-inputs)
- [Interconnecting binector and connector outputs](#interconnecting-binector-and-connector-outputs)
- [BICO technology: example](#bico-technology-example)

###### BICO technology

###### Operating principle of the BICO technology

Open/closed-loop control functions, communication functions as well as diagnostic and operator functions are implemented in the converter. Every function comprises one or more BICO blocks that are interconnected with one another. The following figure shows the typical structure of a mask with BICO interconnections:

![Operating principle of the BICO technology](images/103317853707_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Inputs |
| ② | Output |
| ③ | BICO block |
| ④ | Call Interconnection dialog box |

The following figure shows an example as a section of the function diagram.

![Example of a BICO block: Motorized potentiometer (MOP)](images/103317857419_DV_resource.Stream@PNG-en-US.png)

Example of a BICO block: Motorized potentiometer (MOP)

Most of the BICO blocks can be parameterized. You can adapt the blocks to your application via the parameters.

The signal interconnections within a block cannot be changed. However, the interconnection between blocks can be changed by interconnecting the inputs of one block with the appropriate outputs of another block.

In contrast to electric circuitry, the signal interconnections of the blocks is not via cables, but by means of the software.

For this purpose, there is an Interconnection dialog box in Startdrive that provides the suitable BICO parameters (binectors and connectors) for each interconnection.

![Example: Signal interconnection of two BICO blocks for digital input 0](images/103317869323_DV_resource.Stream@PNG-en-US.png)

Example: Signal interconnection of two BICO blocks for digital input 0

###### Binectors and connectors

Connectors and binectors are used to exchange signals between the individual BICO blocks:

- A connector is a digital signal, e.g. in the 32-bit format. It can be used to emulate words (16 bits), double words (32 bits), or analog signals. Connectors are subdivided into connector inputs (signal sink) and connector outputs (signal source).

  They are used, for example, to interconnect "analog" signals (e.g. "MOP output speed").
- A binector is a unitless digital (binary) signal that can assume a value of 0 or 1. It is subdivided into binector inputs (signal sink) and binector outputs (signal source).

  Binectors are used to interconnect "digital" signals (e.g. "Enable MOP raise" command).

###### Definition of BICO technology

BICO technology represents a type of parameterization that can be used to disconnect all internal signal interconnections between BICO blocks or establish new connections. This is realized using **Bi**nectors and **Co**nnectors. Hence the name **BICO** technology. (English: Binector Connector Technology)

###### BICO parameters

You can use the BICO parameters to define the sources of the input signals of a block. Using BICO parameters you define from which connectors and binectors a block reads-in its input signals. This is how you "interconnect" the blocks stored in the devices according to your particular application requirements. The five different BICO parameter types are shown in the following diagram:

![BICO symbols](images/103317881227_DV_resource.Stream@PNG-en-US.png)

BICO symbols

**When do you need to use BICO technology?**

BICO technology allows you to adapt the converter to a wide range of different requirements. This does not necessarily have to involve highly complex functions.

Example 1: Assign a different function to a digital input.

Example 2: Switch the speed setpoint from the fixed speed to the analog input.

**What precautions should you take when using BICO technology?**

Always apply caution when handling internal interconnections. Note which changes you make as you go along since the process of analyzing them later can be quite difficult.

Startdrive contains various screens that make it much easier for you to use BICO technology. The signals that you can interconnect are displayed in plain text, which means that you do not need any prior knowledge of BICO technology.

**What sources of information do you need to help you set parameters using BICO technology?**

- Refer to the operating instructions of the respective converter for simple signal interconnections, e.g. assigning a different meaning to digital inputs.
- The parameter list of the "Parameter view" is sufficient for comprehensive signal interconnections.
- The function diagrams available in the function diagram overviews of the respective converter provide the information required for comprehensive signal interconnections.

---

**See also**

[Parameter description](#parameter-description)

###### Interconnecting binector and connector inputs

###### Interconnection dialog box for binector inputs

The following figure shows the structure of the Interconnection dialog box for binector inputs:

![Interconnecting BICO inputs](images/134215414027_DV_resource.Stream@PNG-en-US.png)

Interconnecting BICO inputs

| Symbol | Meaning |
| --- | --- |
| ① | Parameter field in the mask |
| ② | Button for calling the Interconnection dialog box |
| ③ | Parameter (signal sink) |
| ④ | Currently interconnected parameter |

###### Procedure

To interconnect a binector or connector input, proceed as follows:

1. Call the Interconnection dialog box.

   The dialog box displays the current interconnection highlighted in color.
2. Select the parameter that you want to interconnect.
3. Confirm with "OK".

###### Result

The binector or connector input is interconnected to the selected parameter.

###### Interconnecting binector and connector outputs

###### Interconnection dialog box for binector outputs

The following figure shows the Interconnection dialog box for binector outputs:

![Interconnecting BICO outputs](images/103317976075_DV_resource.Stream@PNG-en-US.png)

Interconnecting BICO outputs

| Symbol | Meaning |
| --- | --- |
| ① | Parameter field in the mask |
| ② | Button for calling the Interconnection dialog box |
| ③ | Parameter (signal source) |
| ④ | Currently interconnected parameter |
| ⑤ | List of parameters that can be interconnected |

###### Procedure

To interconnect a binector or connector output, proceed as follows:

1. Call the Interconnection dialog box.

   The dialog box displays the current interconnection and provides further signals for the interconnection at "BICO".
2. Select the parameter that you want to interconnect.
3. Confirm with "OK".

###### Result

The binector or connector output is interconnected to the selected parameter.

###### BICO technology: example

###### Example: Shifting a basic PLC functionality into the converter

A conveyor system is to be configured in such a way that it can only start when two signals are present simultaneously. These could be the following signals, for example:

- The oil pump is running (the required pressure level is not reached, however, until after five seconds)
- The protective door is closed

The task is performed by inserting free blocks between digital input 0 and the internal ON/OFF1 command and interconnecting them.

![Example: Signal interconnection for interlock   Interlock](images/103318017419_DV_resource.Stream@PNG-en-US.png)

Example: Signal interconnection for interlock

The signal of digital input 0 (DI 0) is fed through a time block (PDE 0) and is interconnected with the input of a logic block (AND 0). The signal of digital input 1 (DI 1) is interconnected to the second input of the logic block. The logic block output issues the ON/OFF1 command to switch on the motor.

Parameterizing an interlock

| Parameter | Description |
| --- | --- |
| P20161 = 5 | The time block is enabled by assigning to runtime group 5 (time slice of 128 ms) |
| P20162 = 430 | Run sequence of the time block within runtime group 5 (processing before the AND logic block) |
| P20032 = 5 | The AND logic block is enabled by assigning to runtime group 5 (time slice of 128 ms) |
| P20033 = 440 | Run sequence of the AND logic block within runtime group 5 (processing after the time block) |
| P20159 = 5000.00 | Setting the delay time [ms] of the time module: 5 seconds |
| P20158 = 722.0 | Connect the status of DI 0 to the input of the time block  r0722.0 = Parameter that displays the status of digital input 0. |
| P20030 [0] = 20160 | Interconnecting the time block to the 1st AND input |
| P20030 [1] = 722.1 | Interconnecting the status of DI 1 to the 2nd AND input  r0722.1 = Parameter that displays the status of digital input 1. |
| P0840 = 20031 | Interconnecting the AND output to the control command ON/OFF1 |

**Explanation of the example using the ON/OFF1 command**

Parameter P0840[0] is the input of the "ON/OFF1 command" block of the converter. Parameter r20031 is the output of the AND block. To interconnect the ON/OFF1 command with the output of the AND block, set P0840 to 20031.

![Interconnecting two BICO blocks by setting p0840[0] = 20031](images/103318029707_DV_resource.Stream@PNG-en-US.png)

Interconnecting two BICO blocks by setting p0840[0] = 20031

**Principle when connecting BICO blocks using BICO technology**

An interconnection between two BICO blocks comprises a connector or binector and a BICO parameter. The interconnection is always established from the perspective of the input of a particular BICO block. This means that the output of an upstream block must always be assigned to the input of a downstream block. The assignment is always made by entering the number of the connector/binector from which the required input signals are read in a BICO parameter.

This interconnection logic involves the question: **Where does the signal come from?**

---

**See also**

[Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks)

##### Data sets

This section contains information on the following topics:

- [Drive data sets](#drive-data-sets)
- [Command data sets](#command-data-sets)
- [Switching data sets for the parameterizing](#switching-data-sets-for-the-parameterizing)

###### Drive data sets

This section contains information on the following topics:

- [Drive data sets (DDS)](#drive-data-sets-dds)
- [Adding drive data sets](#adding-drive-data-sets)
- [Copying drive data sets](#copying-drive-data-sets)
- [Deleting drive data sets](#deleting-drive-data-sets)

###### Drive data sets (DDS)

###### Drive data sets

You can use different drive configurations, for example, to parameterize and use several motors.

To switch between the drive configurations, parameterize two or more drive data sets. The number depends on the drive used. Binector inputs p0820 and p0821 are used to select a drive data set. They form the number of the drive data set (0 … 3) in binary format (where p0821 is the most significant bit).

###### Selecting a drive data set

To select a drive data set, interconnect bit 0 and bit 1 appropriately.

- Bit 0

  Selection of the parameter that supplies the signal for bit 0 (p820) for the drive data set selection.
- Bit 1

  Selection of the parameter that supplies the signal for bit 1 (p821) for the drive data set selection.

---

**See also**

[Switching data sets for the parameterizing](#switching-data-sets-for-the-parameterizing)

###### Adding drive data sets

The number of possible drive data sets depends on the drive used.

###### Procedure

To add a drive data set, proceed as follows:

1. Click "Add new drive data set".  
   The "Add drive data set" dialog box opens.
2. Select from the following options:
3. Activate "As copy of".  
   With this option, you create the new drive data set (DDS) as a copy of an existing drive data set. All the relevant parameters are copied.
4. In the drop-down list, select the source data set.
5. To add a new drive data set, deactivate "As copy of".
6. Click "OK".

   The new drive data set is added.

###### Result

A new drive data set is added and the number of drive data sets at "DDS" is incremented by 1.

###### Copying drive data sets

###### Procedure

Often drive data sets only differ in individual parameters. Therefore, to create the various data sets, it is recommended to create and parameterize a data set and then to copy it.

To copy a drive data set, proceed as follows:

1. In the "From drive data set" drop-down list, select the source data set.
2. In the "To drive data set" drop-down list, select the target data set.
3. Click the "Copy" button to copy the settings of one data set to another data set. All the relevant parameters of the source data set are copied to the target data set.

###### Result

A copy of the drive data set is added to the list of drive data sets. Now assign parameters to the copy of the drive data set.

###### Deleting drive data sets

###### Procedure

You can delete the drive data sets you no longer require. However, because of the data structure, it is not possible to delete an arbitrary data set, only the last one in the list.

If the relevant drive data set is addressed by a higher-level controller, you must adapt the user program of the controller accordingly.

###### Procedure

1. To delete a drive data set, proceed as follows:
2. Select the data set to be deleted (last) under "Data set selection" in the "Drive data set" drop-down list.
3. Click "Delete existing drive data set".

   The "Delete DDS" dialog box opens.
4. Click "Continue" to delete the data set.

###### Result

The data set is deleted from the list. An error message is output if you have not selected the last data set.

###### Command data sets

This section contains information on the following topics:

- [Command data sets (CDS)](#command-data-sets-cds)
- [Adding command data sets](#adding-command-data-sets)
- [Copying command data sets](#copying-command-data-sets)
- [Delete command data set](#delete-command-data-set)
- [Switching over the converter control (command data set)](#switching-over-the-converter-control-command-data-set)

###### Command data sets (CDS)

Parameterize the settings for the command sources, setpoint sources and status messages in two or more command data sets. The number depends on the drive used. Binector inputs p0810 to p0811 are used to select a command data set. They form the number of the command data set (0 … 3) in binary format (where p0811 is the most significant bit).

###### Selecting a command data set

To select a command data set, interconnect bit 0 and bit 1 appropriately.

- Bit 0

  Selection of the parameter that supplies the signal for bit 0 (p810) for the command data set selection.
- Bit 1

  Selection of the parameter that supplies the signal for bit 1 (p811) for the command data set selection.

###### Example

For example, to parameterize CDS1 in DDS2, you must make the following settings for the parameters.

| Command data set CDS | Drive data set DDS |
| --- | --- |
| p0810[0] = 1 | p0820[1] = 0 |
| p0811[0] = 0 | p0821[1] = 1 |
| r50 = 1 | r51 = 2 |

---

**See also**

[Copying command data sets](#copying-command-data-sets)
  
[Adding command data sets](#adding-command-data-sets)
  
[Delete command data set](#delete-command-data-set)
  
[Switching data sets for the parameterizing](#switching-data-sets-for-the-parameterizing)

###### Adding command data sets

###### Procedure

To add a command data set, proceed as follows:

1. Click "Add new command data set".  
   The "Add command data set" dialog box opens.
2. Activate "As copy of".

   With this option, you create the new command data set (CDS) as a copy of an existing command data set. All the relevant parameters are copied.
3. In the drop-down list, select the source data set.
4. To add a new command data set, deactivate "As copy of".
5. Click "OK". The new command data set is added.

---

**See also**

[Command data sets (CDS)](#command-data-sets-cds)

###### Copying command data sets

###### Procedure

Often command data sets only differ in individual parameters. Therefore, to create the various data sets, it is recommended to create and parameterize a data set and then to copy it.

To copy a command data set, proceed as follows:

1. In the "From command data set" drop-down list, select the source data set.
2. In the "To command data set" drop-down list, select the target data set.
3. Click the "Copy" button to copy the settings of one data set to another data set. All the relevant parameters of the source data set are copied to the target data set.

###### Result

A copy of the command data set is added to the list of command data sets. Now assign parameters to the copy of the command data set.

---

**See also**

[Command data sets (CDS)](#command-data-sets-cds)

###### Delete command data set

###### Delete command data set

You can delete the command data sets you no longer require. However, because of the data structure, it is not possible to delete an arbitrary data set, only the last one in the list.

###### Procedure

1. To delete a command data set, proceed as follows:
2. Select the data set to be deleted (last) under "Data set selection" in the "Command data set" drop-down list.
3. Click "Delete existing command data set".

###### Result

The data set is deleted from the list. An error message is output if you have not selected the last data set.

---

**See also**

[Command data sets (CDS)](#command-data-sets-cds)

###### Switching over the converter control (command data set)

In several applications, the inverter must be able to be operated from different, higher-level control systems.

**Example: Switchover from automatic to manual operation**

A motor is switched on and off, and its speed varied either from a central control system via a fieldbus or from a local control box.

###### Command data set (CDS)

You can set the inverter control in various ways and toggle between the settings. For instance, as described above, the inverter can either be operated via the fieldbus or via the terminal strip.

The settings in the inverter which are associated with a certain control type of the inverter, are known as a command data set.

**Example:**

Command data set 0: Controlling the inverter via the fieldbus  
Command data set 1: Controlling the inverter via the terminal strip

| Symbol | Meaning |
| --- | --- |
| You can set the inverter control in various ways and toggle between the settings. For instance, as described above, the inverter can either be operated via the fieldbus or via the terminal strip.  The settings in the inverter, which are associated with a certain control type of the inverter, are called command data set. | ![Command data set (CDS)](images/103318327947_DV_resource.Stream@PNG-en-US.png) |

You select the command data set using parameter p0810. To do this, you must interconnect parameter p0810 with a control command of your choice, e.g. a digital input.

![Example: Switchover from control via terminal strip to control via PROFIBUS or PROFINET](images/103318338827_DV_resource.Stream@PNG-en-US.png)

Example: Switchover from control via terminal strip to control via PROFIBUS or PROFINET

You obtain the interconnection as in the example above if you configured the interfaces of the inverter with p0015 = 7 in the basic commissioning.

An overview of all the parameters that belong to the command data sets is provided in the List Manual.

> **Note**
>
> It takes approximately 4 ms to toggle between command data sets.

---

**See also**

[Command sources](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#command-sources-1)

###### Switching data sets for the parameterizing

###### Requirements

Several data sets, e.g. drive data sets, must be created for a data set switchover. Each dialog box that contains data-set-dependent settings, displays the following drop-down lists:

![Requirements](images/103318377355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Switch command data set |
| ② | Switch drive data set |

Use these drop-down lists to assign the parameterization to the selected data set.

###### Procedure

1. To assign the dialog box settings to a data set, proceed as follows:
2. In the drop-down list, select the appropriate data set.
3. Change the parameters or BICO interconnections and assign these to the data set.

###### Result

For the dialog box, specific parameterizations are available for each of the various data sets.

You can activate the parameterizations of a data set by selecting this data set in the respective drive object. As an alternative, a parameter assignment is also possible via parameters. See [Command data sets (CDS)](#command-data-sets-cds) and [Drive data sets (DDS)](#drive-data-sets-dds).

###### Parameters of the data set switchover

| Parameter | Description |
| --- | --- |
| p0010 = 15 | **Drive commissioning:** Data sets |
| p0170 | **Number of command data sets** (factory setting: 2) p0170 = 2, 3 or 4 |
| p0010 = 0 | **Drive commissioning:** Ready |
| r0050 | **Display of the number of the currently active command data set** |
| p0809[0] | **Number of the command data set to be copied  (source)** |
| p0809[1] | **Number of the command data set to receive the copy  (target)** |
| p0809[2] = 1 | **Copying is started** At the end of the copying, the inverter sets p0809[2] = 0. |
| p0810 | **Command data set selection, CDS bit 0** |
| p0811 | **Command data set selection, CDS bit 1** |
| r0050 | **Display of the number of the currently active command data set** |

---

**See also**

[Drive data sets (DDS)](#drive-data-sets-dds)

### Using the drive control panel

This section contains information on the following topics:

- [Control panel - Overview](#control-panel---overview)
- [Using the control panel](#using-the-control-panel)
- [Drive control panel operating modes](#drive-control-panel-operating-modes)
- [Speed specification](#speed-specification)
- [Basic positioner operating mode](#basic-positioner-operating-mode)
- [Motor measurement](#motor-measurement)

#### Control panel - Overview

##### Drive control panel

The drive control panel is used for the control and monitoring of individual drives. You traverse drives with the control panel by specifying values. Depending on the operating mode, these are, for example, speed setpoints.

The following figure shows the various components of the control panel:

![Drive control panel](images/103318425739_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control panel |
| ② | Enables |
| ③ | Operating mode |
| ④ | Motor OFF |
| ⑤ | Modify |
| ⑥ | Drive status |
| ⑦ | Actual values |

##### Calling up the control panel

Call up the control panel via "&lt;Drive unit&gt; &gt; Commissioning &gt; Control panel". If there is no online connection, Startdrive attempts to establish a connection.

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active after you have activated the control panel and set the enables.

#### Using the control panel

##### Operating the control panel

You can use the drive control panel to traverse the drive and test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **This control panel may be used only when the associated safety instructions are observed! Failure to comply with these instructions can result in injury to persons or material damage!**  The function is released exclusively for commissioning, diagnostic and service purposes. The function should generally only be used by authorized technicians. The safety shutdowns from the higher-level controller have no effect.  The **Stop with spacebar** function is not guaranteed in all operating modes. Therefore, there must be an EMERGENCY STOP circuit in the hardware. The appropriate measures must be taken by the user. |  |

> **Note**
>
> **Drive reacts immediately**
>
> Although all enables are removed before returning the control priority, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

##### Activating the control panel

When you activate the control panel, you assume master control of the drive. The control panel can always only be activated for one drive.

To activate the control panel, proceed as follows:

1. Activate the control panel at "Control panel". The "Activate master control" message window opens.
2. Read the warning carefully and check the value for the monitoring time. The monitoring time specifies the time during which the connection from the PG/PC to the drive is monitored. The minimum value is 1000 ms.
3. Confirm with "Continue". The operating panel is then active.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> Additionally, the automatic project lock due to inactivity will not take effect while the control panel is active.

##### Deactivating the control panel

When you deactivate the control panel, you return the master control. The control panel cannot be deactivated until the drive is switched off ("0" button).

To deactivate the control panel, proceed as follows:

1. Click "Deactivate" to return the master control.
2. The user interface of the control panel is grayed out.

##### Enables

To set the required enables for the control panel, proceed as follows.

1. Click "Set" under "Drive enables".

   Further areas of the control panel are activated.
2. Click "Acknowledge faults" to acknowledge the currently pending faults.
3. If you no longer require the enables, click "Reset" under "Drive enables".

##### Result

You can now traverse the drive with the control panel. Enables and faults are displayed at "Drive status". In addition to "Active fault", the currently pending fault is displayed.

#### Drive control panel operating modes

Go online and enable the control panel in order to select the operating mode, see also [Using the control panel](#using-the-control-panel).

##### Drive control panel operating modes

The drive control panel has two operating modes:

- Speed specification
- Basic positioner

If the drive does not have the "Basic positioner" technology or it is deactivated, then the "Operating mode" drop-down list is not active.

##### "Speed specification" operating mode

In the "Speed specification" operating mode, you traverse the drive as follows:

- Speed control: Endless or via Jog, see also [Traversing the drive with speed specification](#traversing-the-drive-with-speed-specification)
- V/f control: By entering a defined speed

##### "Basic positioner" operating mode (only for drives with basic positioner)

In the "Basic positioner" operating mode, the drive control panel has the following sub-modes:

- [Manual positioning](#manual-positioning)
- [Direct homing](#absolute-positioning)
- [Active homing](#modify-traversing-block)
- [Relative positioning](#direct-homing)
- [Absolute positioning](#active-homing)
- [Modify traversing block](#relative-positioning)

#### Speed specification

This section contains information on the following topics:

- [Traversing the drive with speed specification](#traversing-the-drive-with-speed-specification)

##### Traversing the drive with speed specification

###### Traversing the drive

After you have set the drive enables, specify the operating mode and switch the motor on.

###### Selecting the operating mode

1. To traverse the drive via a speed specification, proceed as follows:
2. Select the "Speed specification" entry in the "Operating mode" drop-down list.

###### Specifying the setpoint

To specify the setpoint, proceed as follows:

1. Enter a speed setpoint under "Speed" at which the motor should operate.  
   After specifying the speed setpoint, the drive is switched on when the mouse is clicked on one of the "Start backward", "Start forward", "Jog forward" or "Jog backward" buttons for the first time.
2. Click "Backward" to turn the motor backwards.
3. Click "Forward" to turn the motor forwards.
4. Click "Jog forward" to inch the motor forwards.
5. Click "Jog backward" to inch the motor backwards.

###### Stopping the drive

- Click "Stop" to stop the drive again.

###### Switching off the drive

- Click on "Off" to switch off the motor.

###### Viewing actual values of the drive

The current values of various parameters are displayed at "Actual values".

#### Basic positioner operating mode

This section contains information on the following topics:

- [Manual positioning](#manual-positioning)
- [Direct homing](#direct-homing)
- [Active homing](#active-homing)
- [Relative positioning](#relative-positioning)
- [Absolute positioning](#absolute-positioning)
- [Modify traversing block](#modify-traversing-block)

##### Manual positioning

###### Performing manual positioning in the drive control panel

With manual positioning, you traverse the drive endlessly or with jog position-controlled with a defined velocity and acceleration.

For further information, see AUTOHOTSPOT and [Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi).

###### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control.

###### Procedure

To traverse the drive via manual positioning, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Manual positioning".

   The "Velocity" and "Acceleration" entries are displayed.
3. At "Velocity", enter a value in LU/min and press the ENTER key. The length unit is an internal length unit of the drive.
4. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key.
5. Use the buttons to traverse the motor forward and backward.

###### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

###### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

###### Additional parameters

---

---

**See also**

[Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi)

##### Direct homing

###### Using direct homing

With direct homing, you home the configured encoder system to a freely selectable position. In this way, you can move the working area to a freely definable area. The encoder type is not relevant. Use this function, for example, when you want to test traversing blocks outside of the real working area or danger area.

Direct homing corresponds to the EPOS "Set home position" functionality.

A homed encoder system is essential for the correct use of "Absolute positioning" and "Modify traversing block". For information on home position setting, see also [Set reference point](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#set-reference-point).

###### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control.

###### Procedure

To perform direct homing, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Direct homing".

   The "Home position" entry and the "Set home position" button are displayed.
3. Click "Set home position" to traverse the drive to the home position.

###### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

###### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

###### Additional parameters

---

##### Active homing

###### Using active homing

For an incremental encoder / re​solver, you home the configured encoder system via a homing procedure. If you use an absolute encoder, you home the configured encoder system via an absolute encoder adjustment. "Active homing" uses the standard functionality of the basic positioner. You only have to trigger the start of the homing procedure in the control panel.

The homing is also retained after the deactivation of the master control and serves as the basis for all position-controlled applications.

For further information, see AUTOHOTSPOT, [Setting the reference point approach](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-reference-point-approach) and [Absolute encoder adjustment](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#absolute-encoder-adjustment).

###### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control. You have configured an encoder:

- Incremental encoder / resolver for active homing
- Absolute encoder for absolute encoder adjustment

###### "Active homing" procedure (only incremental encoders / resolvers)

To perform active homing, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Active homing".

   The "Start homing procedure" entry is displayed.
3. Click "Start homing procedure" to traverse the drive to the home position.

###### "Absolute encoder adjustment" procedure (only absolute encoders)

To perform an absolute encoder adjustment, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Active homing".

   The "Start adjustment" entry is displayed.
3. Click "Start adjustment" to traverse the drive to the home position.

###### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

###### Actual values

The values currently active in the drive are displayed at "Actual values". In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists. If the required parameters are not displayed in the list, call a dialog box for extended parameter selection via the "Additional values..." list item.

###### Additional parameters

---

##### Relative positioning

###### Using relative positioning

Use the "Relative positioning" function to traverse an axis a defined distance with the aid of the control panel. For further information, see also AUTOHOTSPOT and [Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi).

###### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control.

###### Procedure

To traverse the drive via relative positioning, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Relative positioning".

   The "Distance", "Velocity" and "Acceleration" entries are displayed.
3. At "Distance", enter a value in LU and press the ENTER key.
4. At "Velocity", enter a value in LU/s and press the ENTER key.
5. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key. The value is used for acceleration and deceleration.
6. Use the buttons to start the positioning job forward and backward.

###### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

###### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

###### Additional parameters

---

##### Absolute positioning

###### Using absolute positioning

With "Absolute positioning" you traverse the axis to an absolute position. The function is oriented towards "Direct setpoint specification / MDI". For further information, see AUTOHOTSPOT and [Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi).

###### Requirement

You have established an online connection to the drive, have called the drive control panel, activated the master control and the configured encoder system has been referenced.

###### Actual values

The currently active values in the drive are displayed in the "Actual values" area. In addition to the default parameter values, parameters are also available for free selection in two drop-down lists. If the required parameters are not displayed in the list, call a dialog box for extended parameter selection via the "Additional values..." list item.

###### Procedure

To traverse the drive via absolute positioning, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Absolute positioning".

   The "Target position:", "Velocity", and "Acceleration" entries are displayed.
3. At "Target position", enter a value in LU and press the ENTER key.
4. At "Velocity", enter a value in LU/s and press the ENTER key.
5. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key. The value is used for acceleration and deceleration.
6. Click "Start" to start the positioning job.

###### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

###### Additional parameters

---

##### Modify traversing block

###### Using modify traversing blocks

You traverse the programmed traversing blocks with "Modify traversing blocks". You can test individual traversing blocks or all programmed traversing blocks in an automatic run.

###### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control.

The configured encoder system is homed.

###### Procedure

To modify the traversing blocks, proceed as follows:

1. Select "Basic positioner" in the "Operating mode" drop-down list.
2. Then select "Modify traversing blocks".
3. Enter the number of the traversing block under "Traversing block no.".
4. Click "Start" to start the traversing blocks.

###### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

###### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

###### Additional parameters

---

#### Motor measurement

##### Performing a motor measurement

A motor measurement is used to perform the motor data identification. You set the motor measurement in the wizard.

For further information, see also [Motor optimization](#motor-optimization-1).

##### Requirement

You have established an online connection to the drive, have called the drive control panel and activated the master control.

##### Procedure

If a motor measurement is active, the "Motor measurement" LED is displayed at "Drive status". Most of the control options are deactivated and cannot be used.

To perform a motor measurement, proceed as follows:

1. Switch the drive on by clicking "1".
2. The drive starts the motor measurement. As long as the motor measurement is running, the "Motor measurement active" dialog box is displayed.

##### Result

As soon as the motor measurement has been performed, you can use the drive control panel to control the drive.

### Motor optimization

This section contains information on the following topics:

- [Motor optimization](#motor-optimization-1)

#### Motor optimization

##### Description

The motor optimization assists with the determination of motor data, for example, for third-party motors. The motor optimization should be performed to improve the control properties of the motor. In particular for the sensorless vector control, at least the stator resistance (including the supply cable resistance) and the power unit parameters must be determined for each drive. This is required so that the observer model can operate correctly even for very low speeds.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Incorrect details for current values**  Incorrect details for the rated current or the maximum current can damage the motor!  Make sure that the entered values are correct. |  |

**Screen form layout**

- "Configuration area": To enter the configuration data and perform the measurement.
- "Status area": To follow the progress of the measurement (parameter r47).
- "Result area": To view the results of the motor optimization.

**Perform measurement**

The "Measuring type" drop-down list shows the available measuring types. When the dialog box is opened, a check is made to determine whether a measurement is already active and, if so, it will be displayed. If no measurement is selected, a check is made as to which measurement has already been performed and then used as recommendation.

After executing the drive wizard and the subsequent download, the selection in measuring type is set to "stationary measurement", because the "complete calculation of the motor/control parameters" has already been performed. The selection list is not active, but the measurement is active (button set to Deactivate measurement). The next step then involves performing the measurement.

- If necessary, click "Activate measurement", if it is not yet active to initiate the motor data identification with the next ON command, for example, from the drive control panel.

The center of the screen form contains the status display that shows the progress of the measurement (parameter r47).

The motor optimization ends independently and the message appears that the drive is in the Switching on inhibited state.

After the measurement, the new parameter values are displayed in the results table. You can view and check the new values.

**Start measurement in the drive control panel**

If you open the screen form in ONLINE mode, you switch to the drive control panel.

To start the measurement, proceed as follows:

1. First activate the master control in the drive control panel.
2. Set the drive enables.

   The motor measurement is started. You can see the status of the motor measurement under "Drive status".

**Start next measurement**

To start the next measurement, proceed as follows:

1. Click "Next measurement".

   The next measurement is suggested by Startdrive and the corresponding entry displayed in the "Measuring type" list.
2. Perform the measurement as described above.
3. Continue to perform Next measurement until the entry None appears in the "Measuring type" drop-down list. You have then performed all required measurements.

**Select measurements yourself**

- Only if you are an experienced user should you manually select the measurement in the list. This allows you to repeat a measurement.
- The specified measuring types depend on the motor.
- Perform the measurement as described above.

### Save/Reset

This section contains information on the following topics:

- [Saving RAM data to EEPROM](#saving-ram-data-to-eeprom)
- [Restoring the factory setting](#restoring-the-factory-setting)
- [Saving settings on memory card](#saving-settings-on-memory-card)
- [Transferring settings from the memory card](#transferring-settings-from-the-memory-card)

#### Saving RAM data to EEPROM

##### Saving RAM data to the EEPROM

The parameter values are normally saved as volatile data in the RAM of the drive.

To save the data retentively, proceed as follows:

1. Go online with the converter.
2. Open "Commissioning &gt; Save/reset".
3. ① In the "Save/reset" dialog box, click "Save" under "Save RAM data to EEPROM".

   ![RAM data to EEPROM](images/103318931595_DV_resource.Stream@PNG-en-US.png)

   ![RAM data to EEPROM](images/103318931595_DV_resource.Stream@PNG-en-US.png)

   RAM data to EEPROM

The data is saved retentively in the EEPROM.

#### Restoring the factory setting

There are cases where something goes wrong when commissioning a drive system e.g.:

- The line voltage was interrupted during commissioning and you were not able to complete commissioning.
- You got confused when setting the parameters and you can no longer understand the individual settings that you made.
- You do not know whether the converter was already operational.

In cases such as these, reset the converter to the factory settings.

##### Restoring factory settings

This function resets the settings in the converter to the factory settings.

![Restoring factory settings](images/103318983435_DV_resource.Stream@PNG-en-US.png)

Restoring factory settings

> **Note**
>
> The communication settings and the settings of the motor standard (IEC/NEMA) are retained even after restoring the factory setting.

To restore the factory settings, proceed as follows:

1. Go online with the drive.
2. Select "Commissioning &gt; Save/Reset" in the project navigator.
3. In the "Save/Reset" dialog box, click "Restore factory settings".
4. Select "Reset parameters" in the drop-down list.
5. Click the "Start" button.

   The settings are reset to the as-delivered, factory settings.

##### Resetting settings of the safety functions

The settings of the safety functions are protected by a password. In order to reset all settings of the converter to the factory settings, you must begin with the safety functions.

To reset the safety settings to the factory settings, proceed as follows:

1. Establish an online connection to the drive.
2. In the "Save/Reset" dialog box, click "Restore factory settings".
3. Select "Reset safety parameters" in the drop-down list.
4. Click the "Start" button. p0010 is set to 30 and p0970 to 5.

   The safety settings are reset to the as-delivered state.

##### **Resetting to delivered state**

This option is available only for G115D Motor mount delivered with a SIMMOGEAR motor.

To reset the settings in the converter to the delivered state, proceed as follows

1. Establish an online connection to the drive.
2. In the "Save/Reset" dialog box, click "Restore factory settings".
3. Select "Reset to delivered state" in the drop-down list.
4. Click the "Start" button.

   The parameters are reset to the delivered state with SIMOGEAR parameters.

#### Saving settings on memory card

##### Saving settings on memory card

You can save parameter sets on the memory card and transfer these to other converters, for example, to converters with identical parameter assignments, or for the transfer of settings after replacing a converter.

There are two options available for the data backup:

- Automatic backup
- User-defined backup

##### Automatic backup

We recommend that you insert the memory card before switching on the converter. The converter always also backs up its settings on an inserted card.

To automatically back up the settings, proceed as follows:

1. If required, switch off the converter power supply.
2. To automatically save the settings of the converter on the memory card, insert the memory card into the converter.
3. Switch the power supply on again.

   After it has been switched on, the converter copies its settings to the memory card, to parameter set "0".

**Note**

**Data loss in the converter**

If the memory card that you insert contains a parameter backup with the value "0", the converter accepts this data from the memory card. The current setting in the converter will be irretrievably deleted.

Before inserting the memory card, make sure that there is no data on the card, or only data that you want to accept.

##### Manual backup of the settings

![Data from the drive on the memory card](images/103319020939_DV_resource.Stream@PNG-en-US.png)

Data from the drive on the memory card

To manually back up the settings, proceed as follows:

1. If required, switch on the converter power supply.
2. Insert the memory card into the converter.
3. Go online with the drive.
4. Select "Commissioning &gt; Save/Reset" in the project navigator.
5. Select a parameter set at "Parameter set in the drive".
6. Enter a value at "Parameter set on memory card".
7. Click "Save" to save the data to the memory card.
8. Click "Safely remove card" to ensure that there is currently no access to the memory card and the card can be safely removed.

#### Transferring settings from the memory card

##### Transferring settings from the memory card

Transfer a parameter set that you have saved to the memory card to other converters, or load the settings of a specific data set back to the converter.

There are two options available for the data transfer:

- Automatic transfer
- Manual transfer

##### Automatic transfer of data from the memory card to the converter

To automatically transfer the settings, proceed as follows:

1. If required, switch off the converter power supply.
2. Insert the card into the converter.
3. To automatically transfer a parameter backup with the number "0", switch the power supply of the converter on again.

   If there is valid parameter data on the memory card, then the converter accepts the data from the memory card.

##### Manual transfer of data from the memory card to the converter

![Loading data from the memory card to the drive](images/103319071243_DV_resource.Stream@PNG-en-US.png)

Loading data from the memory card to the drive

To automatically transfer the settings, proceed as follows:

1. If required, switch on the converter power supply.
2. Insert the memory card into the converter.
3. Go online with Startdrive.
4. Select "Commissioning &gt; Save/Reset".
5. Enter a number for the parameter set at "Parameter set on memory card".
6. Select a parameter set at "Parameter set in the drive".
7. Click "Load" to load the data from the memory card to the converter.
8. Click "Safely remove card" to ensure that there is currently no access to the memory card and the card can be safely removed.

The data from the memory card is now saved in the converter.

### Operating the drive on a controller

This section contains information on the following topics:

- [Using a higher-level controller](#using-a-higher-level-controller)

#### Using a higher-level controller

##### Using drives

Depending on the fieldbus used, the higher-level controller is configured as DP master (PROFIBUS DP) or as IO controller (PROFINET IO). A drive is then configured accordingly as DP device or as IO device.

Run through the "Drive on motion control axis" wizard on the drive.

You make the following settings in this drive:

- Motor standard
- Motor
- PROFIdrive telegram and reference data

For more information about the wizard, see also [Commissioning wizard](Running%20through%20the%20wizard.md#commissioning-wizard).

The drive connection for SIMATIC controllers is described at "Using S7-1500 motion control".

### Drives in the hardware catalog

This section contains information on the following topics:

- [Drives in the hardware catalog](#drives-in-the-hardware-catalog-1)
- [GSD/GSDML drives](#gsdgsdml-drives)
- [Installing the GSD file](#installing-the-gsd-file)

#### Drives in the hardware catalog

##### Selecting devices via the hardware catalog

Devices are administered in the TIA Portal via the hardware catalog. This is anchored as a tab in the right-hand margin of the TIA Portal.

For example, you can insert drive units and power units using drag and drop in the device view and network view using the hardware catalog. Currently not all SINAMICS drives have been integrated in the TIA Portal, see also [GSD/GSDML drives](#gsdgsdml-drives).

All devices are listed in the catalog view which can be restricted via filters:

![Hardware catalog](images/103319167243_DV_resource.Stream@PNG-en-US.png)

Hardware catalog

#### GSD/GSDML drives

##### Using drives via GSD

You can import drives that are not integrated in the TIA Portal by Startdrive using GSD files (generic station description). These drives, such as the SINAMICS S120, are currently not parameterizable via Startdrive and must be assigned parameters in external engineering tools, such as STARTER.

The GSD drives can be selected in the hardware catalog under "Additional field devices":

![GSD drives in the hardware catalog](images/103319192843_DV_resource.Stream@PNG-en-US.png)

GSD drives in the hardware catalog

You can install additional drives by importing the GSD file of the relevant device, see also [Installing the GSD file](#installing-the-gsd-file).

#### Installing the GSD file

##### Introduction

A GSD file (device data file) contains all the device properties. If you want to configure a device that does not appear in the hardware catalog, you must install the GSD file provided by the manufacturer. Devices installed via GSD files are displayed in the hardware catalog and can then be selected and configured.

The properties of PROFINET IO devices are not stored in a keyword-based text file (as for PROFIBUS DP devices), but in an XML file whose structure and rules are determined by a GSDML schema.

The language to describe the GSD files is GSDML (Generic Station Description Markup Language). It is defined by the GSDML schema.

A GSDML schema contains validation rules that allow it, for example, to check the syntax of a GSD file. GSDML schemas (as schema files) are acquired by IO device manufacturers from PROFIBUS International.

Functional enhancements in the area of PROFINET IO have an effect on the GSDML specification and the corresponding schema. A new version of the specification and of the schema is created by the functional enhancement.

##### Requirement

- The hardware and network editor is closed.
- You have access to the required GSD files in a directory on the hard disk.

##### Procedure

To install a GSD file, proceed as follows:

1. In the "Options" menu, select the "Install device master data files" command.
2. In the "Install device master data files" dialog box, select the folder in which you want to save the GSD files.
3. Select one or more files from the list of displayed GSD files.
4. Click "Install".
5. To create a log file for the installation, click "Save log file".

   Any problems during the installation can be tracked down using the log file.

You will find the new device installed by means of the GSD file in a new folder in the hardware catalog.

> **Note**
>
> Installation of a GSD file cannot be undone.

---

**See also**

[GSD/GSDML drives](#gsdgsdml-drives)

### Using drive libraries

This section contains information on the following topics:

- [Using libraries with drives - overview](#using-libraries-with-drives---overview)
- [Creating copy templates](#creating-copy-templates)
- [Using copy templates](#using-copy-templates)

#### Using libraries with drives - overview

##### Using drives in libraries

In the TIA Portal, libraries are used to store objects that you want to use again. It is possible to reuse the stored objects throughout a project or across projects.

In the drive context, working with libraries enables copies of drives/devices with networks to be created in the libraries. These copy templates are then inserted again in the respective context of the project.

A detailed description of libraries can be found in "Using libraries".

##### Library types

The following library types are available:

- Project libraries

  You can use a project library when you only want to use the objects in the opened project.
- Global libraries

  You can use global libraries when you want to use the objects across projects.

##### Devices and drives

The following objects are possible as copy templates in the drive context:

- One or more devices from the project navigator
- Devices and networks from the network view or the device configuration

The copy templates contain the entire parameterization. You can therefore create copies of the initial drive with the copy template of a completely parameterized drive.

#### Creating copy templates

##### Requirement

You can create one or more copies of a device with copy templates from a library, if required, with networks. Therefore, first configure the device or devices that you want to use as copy templates.

##### Creating a copy template in a project library

To create a copy template in a project library, proceed as follows:

1. Open the "Libraries" task card.
2. Click "Project library" to open the palette.
3. Select the device in the project navigator.
4. Drag the selection to the "Copy templates" folder or any of its subfolders.

   Or
5. Select a device or several devices with or without network in the network view (lasso is possible).
6. Drag the selection to the "Copy templates" folder or any of its subfolders.

##### Creating a copy template in a global library

To create a copy template in a global library, proceed as follows:

1. Open the "Libraries" task card.
2. Click "Global libraries" to open the palette.
3. Open the global library or create a new global library.
4. Select the device in the project navigator.
5. Drag the selection to the "Copy templates" folder or any of its subfolders.

   Or
6. Select a device or several devices with or without network in the network view (lasso is possible).
7. Drag the selection to the "Copy templates" folder or any of its subfolders.

##### Result

The selected elements are inserted into the project library or global library as copy templates. Only one entry per object is created. A selection with several devices also only creates one entry. The symbol in front of the copy template indicates the source.

Each element is assigned a default name that you can change.

#### Using copy templates

##### Using copy templates from project libraries and global libraries

Use copy templates in order to be able to use the objects several times in the same project. After an export of the library, you can also use the objects in other projects and other PG/PCs. In this way, you can perform series commissionings with copy templates of parameterized drives and networks. If you have created a network with devices as copy template via the network view, it can only be inserted again in the network view.

The TIA Portal allows you to insert the copy templates at the appropriate positions.

##### Using a copy template from a project library

To use a copy template from a project library, proceed as follows:

1. Open the "Libraries" task card.
2. Click "Project library" to open the palette.
3. Select the copy template.
4. Drag the selection to the project folder in the project navigator.

   Or
5. Drag the selection to the network view if the copy template originates from there.

##### Using a copy template from a global library

To use a copy template from a global library, proceed as follows:

1. Open the "Libraries" task card.
2. Click "Global libraries" to open the palette.
3. Open a global library.
4. Select the copy template.
5. Drag the selection to the project folder in the project navigator.

   Or
6. Drag the selection to the network view if the copy template originates from there.

##### Result

The objects contained in the copy template, e.g. devices, networks, are created in the project.

### Using know-how protection

This section contains information on the following topics:

- [Know-how protection overview](#know-how-protection-overview)
- [Activating/deactivating know-how protection](#activatingdeactivating-know-how-protection)

#### Know-how protection overview

##### Know-how protection in the drive unit

As of SINAMICS V4.5, know-how protection for drive units is available in Startdrive. This only applies online and is for the protection of intellectual property, specifically the proprietary knowledge of machine manufacturers, against unauthorized use or product reproduction. The know-how protection settings are made in the parameter view.

If the "Drive unit" know-how protection is set, the following functions are no longer available:

- Drive wizard
- Function view
- Commissioning

The drive cannot be configured in the TIA Portal while know-how protection is active.

For further information, see [Activating/deactivating know-how protection](#activatingdeactivating-know-how-protection).

#### Activating/deactivating know-how protection

##### Activating know-how protection with password

You can activate know-how protection in Startdrive in the parameter view. The required parameters are service parameters. You must first display them by entering the appropriate password.

Required parameters:

- p7767 "KHP password new"
- p7768 "KHP password confirmation"
- p7766 "KHP password input"
- r7760[1] "Know-how protection active"
- p7761 "Write protection"

The parameters to be used are enumeration parameters. Each character of the password must be entered in an enum. The passwords can be up to 30 characters long [0 ... 29]. If you do not enter 30 characters, you must enter "0" in the enum [29]. The parameters require characters in ASCII code. You must therefore convert the characters of the password that you have specified into ASCII code. To do this, use e.g. Windows Character Map ("All programs &gt; Accessories &gt; System Tools &gt; Character Map").

Example: Enter password "G120" in parameter p7767

| Character | ASCII code |
| --- | --- |
| G | 47 |
| 1 | 31 |
| 2 | 32 |
| 0 | 0 |

Entries in the parameter view for p7767:

| Parameter | Enum | ASCII code | Character |
| --- | --- | --- | --- |
| p7767 | [0] | 47 | G |
|  | [1] | 31 | 1 |
|  | [2] | 32 | 2 |
|  | [3] | 0 | 0 |
|  | ... |  |  |
|  | [29] | 0 |  |

##### Displaying service parameters

To display the service parameters in Startdrive, proceed as follows:

1. Open the parameter view.
2. Select "Display service parameters" from the drop-down list above the parameter view.

   The "Access level" dialog box is displayed.
3. Enter the password. The service parameters are displayed.

##### Entering password and activating know-how protection

To assign a new password for the know-how protection, proceed as follows:

1. Display the service parameters in the parameter view.
2. Convert the characters of your password to ASCII code.
3. Enter the ASCII code in p7767 (see above).
4. Repeat the input in p7768 to confirm the input of the password.
5. Open r7760.1 to display the status of the know-how protection.
6. To prevent the password being overwritten, set the write protection with p7761.

   The know-how protection is now set.

##### Deactivating know-how protection

To deactivate the know-how protection, proceed as follows:

1. Deactivate the write protection in p7761.
2. Enter the password in p7766 in the same way as described above (ASCII code in the enumeration parameters).
3. Check whether the know-how protection has been temporarily withdrawn in r7760.2.

### Upgrading devices and firmware

This section contains information on the following topics:

- [Upgrading G120/G115D/G110M drives](#upgrading-g120g115dg110m-drives)
- [Upgrading G120C drives](#upgrading-g120c-drives)

#### Upgrading G120/G115D/G110M drives

##### Upgrading firmware

You can upgrade the firmware of G120/G115D/G110M drives to a newer version in the project. This is the case when you replace a faulty Control Unit by a newer Control Unit with newer firmware, without having to reconfigure the project completely.

> **Note**
>
> **Lower firmware version**
>
> It is not possible to downgrade to a lower firmware version.

> **Note**
>
> **G120C drives**
>
> G120C Compact drives can also be replaced by another drive, see [Upgrading G120C drives](#upgrading-g120c-drives).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Parameter values are reset**  The values of read-only parameters are reset to the factory settings. The correct values are then restored in the project after an upload. |  |

##### Procedure

To upgrade the firmware, proceed as follows:

1. Right-click the device to open the shortcut menu.
2. Execute "Change device". The dialog with the same name opens.

   If the device is already using the latest firmware, the menu item "Change device" is not active.
3. Select the required firmware version at "New device" in the structure tree.
4. Confirm your selection with "OK".
5. Check the successful upgrade in the inspector window at "Info" &gt; "General". Warnings may be displayed.
6. To complete the upgrade, first perform a download and then an upload from the device. The read-only parameters are then displayed with correct values.

##### Upgrading using drag-and-drop

Alternatively, you can also drag the drive version from the hardware catalog and drop it on the drive in the device view. This also calls the "Change device" dialog.

#### Upgrading G120C drives

##### Devices and firmware of G120C drives

A G120C drive comprises a Control Unit and a Power Module that are installed as a unit.

You can either upgrade the firmware of G120C drives to a newer version in the project or replace the device with another device. This is possible because the G120C drives are very similar.

> **Note**
>
> **Lower firmware version**
>
> It is not possible to downgrade to a lower firmware version.
>
> The bus systems of the old and the new device must be the same. For example, you cannot replace a PROFINET device with a PROFIBUS device and vice versa.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Parameter values are reset**  The values of read-only parameters are reset to the factory settings. The correct values are then restored in the project after an upload.  If you replace a device with another device, relevant parameter values may be recalculated. If this case, you must recommission the drive. Note the information in the inspector window that refer to such cases. |  |

##### Procedure

To upgrade a G120C, proceed as follows:

1. Right-click the device to open the shortcut menu.
2. Execute "Change device". The dialog with the same name opens.

   If the dialog at "New device" displays an empty list, the device is already using the latest firmware.
3. Select the required firmware version at "New device" in the structure tree.
4. Confirm your selection with "OK".
5. Check the successful upgrade in the inspector window at "Info" &gt; "General". Warnings may be displayed.
6. To complete the upgrade, first perform a download and then an upload from the device. The read-only parameters are then displayed with correct values.

##### Upgrade using drag-and-drop

Alternatively, you can also drag the drive from the hardware catalog and drop it on the existing drive in the device view. This also calls the "Change device" dialog. The cursor indicates whether the drive can be replaced.

## Going online and performing diagnostics

This section contains information on the following topics:

- [Online access/updating accessible devices](#online-accessupdating-accessible-devices)
- [Entering parameters in the project offline](#entering-parameters-in-the-project-offline)
- [Go online, upload and download](#go-online-upload-and-download)
- [Online &amp; diagnostics](#online-diagnostics)
- [Fault and alarm concept for SINAMICS drives](#fault-and-alarm-concept-for-sinamics-drives)

### Online access/updating accessible devices

This section contains information on the following topics:

- [Online connection via USB](#online-connection-via-usb)
- [Online connection via PROFINET IO](#online-connection-via-profinet-io)
- [Online connection via PROFIBUS DP](#online-connection-via-profibus-dp)

#### Online connection via USB

##### Online access via USB

The simplest way to go online with the drive is via the USB interface.

Connect the drive to your PG/PC via a USB cable. If the USB driver is not installed, the installation is started automatically.

##### Establishing an online connection between the PG/PC and the drive

The device must be sought via USB for an online connection.

- Drive and computer must be connected via a USB cable.

##### Procedure

To establish an online connection via USB, proceed as follows:

1. Open the "Online access" entry in the project navigator.
2. Select the "USB [S7USB]" interface as the connection type.
3. Run the "Update accessible devices" command.

   The USB device is displayed. You can establish an online connection.

   ![USB online access](images/103319528971_DV_resource.Stream@PNG-en-US.png)

   USB online access

##### Uploading the device to the project

When you have made all the settings, you can upload the device to the project, see also [Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software).

#### Online connection via PROFINET IO

This section contains information on the following topics:

- [Going online via PROFINET IO](#going-online-via-profinet-io)
- [Going online on a single drive unit](#going-online-on-a-single-drive-unit)
- [Drive to higher-level controller](#drive-to-higher-level-controller)
- [Restoring factory settings](#restoring-factory-settings)
- [Setting the PG/ PC interface](#setting-the-pg-pc-interface)

##### Going online via PROFINET IO

###### Using PROFINET IO

In principle, there are two types of online connection via PROFINET IO:

- Establishing an online connection to a single drive.
- Establishing an online connection to a drive via a higher-level controller.

###### Establishing an online connection between the PG/PC and a single drive

The following procedure is recommended for establishing an online connection between a PG/PC and a single drive:

- Search for the device via "Online access"
- Assign an IP address and a device name
- Upload the device to the project

See also [Online access via PROFINET](#online-access-via-profinet).

###### Online connection via a higher-level controller

The following procedure is recommended for establishing an online connection between a PG/PC and a controller with drives:

- Create the controller and drive(s) offline in the project with a PROFINET subnet
- Enter the IP addresses and device names of the drives offline in the interface properties
- Search for the devices via "Online access" ("Update accessible devices")
- Assign device names in the network view of the respective drive
- Load the settings to the controller

See also [Drive to higher-level controller](#drive-to-higher-level-controller).

---

**See also**

[Setting the PG/ PC interface](#setting-the-pg-pc-interface)
  
[Assigning an IP address](#assigning-an-ip-address)
  
[Assigning PROFINET device names](#assigning-profinet-device-names)
  
[Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software)

##### Going online on a single drive unit

This section contains information on the following topics:

- [Online access via PROFINET](#online-access-via-profinet)
- [Assigning an IP address](#assigning-an-ip-address)
- [Assigning PROFINET device names](#assigning-profinet-device-names)

###### Online access via PROFINET

###### Using online access

The TIA Portal can search for the drive via the online access of your computer.

###### Requirement

A connection has been established between computer and drive.

###### Procedure via "Online access"

To search for a drive, proceed as follows:

1. Open the "Online access" entry in the project navigator.
2. Select the network interface of your computer.
3. Double-click "Update accessible devices".

   The drive is displayed in the project navigator.

   ![PROFINET online access](images/103319628299_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET online access](images/103319628299_DV_resource.Stream@PNG-en-US.png)

   PROFINET online access

   If the communication parameters are at their factory settings (IP address 0.0.0.0 and no device name), then the default device names of the TIA Portal ("Node" in this case) and the MAC address are displayed.

   If you want to go online on the device, you must assign an IP address and a device name.
4. Select the drive and, if required, assign an IP address and a device name, see also [Assigning an IP address](#assigning-an-ip-address) and [Assigning PROFINET device names](#assigning-profinet-device-names).

   ![PROFINET with IP address](images/103319632011_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET with IP address](images/103319632011_DV_resource.Stream@PNG-en-US.png)

   PROFINET with IP address

   The drive is displayed with the device name (in this case, drive_1) and the IP address (in this case, 198.168.0.21).

   If you cannot assign an IP address and device name, you may have to check the IP address of your PG/PC. It must be in the same address range as the address of the drive, see also [Setting the PG/ PC interface](#setting-the-pg-pc-interface).

###### Result

An online connection is established. Now edit the drive communication settings and upload the drive to the project, see also [Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software).

###### Assigning an IP address

###### Adapting the IP address in the drive

Before you can go online on a drive via PROFINET, you must assign the drive a suitable IP address.

- The drive does not have an IP address in the delivered state.
- If the drive already has an IP address, perform "Restore factory settings" to reset it to 0.0.0.0.

> **Note**
>
> **Assign IP address without "Restore factory settings"**
>
> If the drive already has an IP address, you can overwrite it with a new address. However, you must perform a **Power off/on** for the setting to take effect.

###### Requirement

There is an online connection to the drive and you have already searched for the device under "Online access" in the appropriate interface with "Update accessible devices".

The device is displayed.

###### Procedure

To assign an IP address, proceed as follows:

1. Open "Online &amp; diagnostics" in the appropriate interface under "Online access" in the project navigator.
2. Open the "Functions" entry.
3. Double-click the "Assign IP address" entry in the secondary navigation.

   ![Assigning an IP address](images/103319693835_DV_resource.Stream@PNG-en-US.png)

   ![Assigning an IP address](images/103319693835_DV_resource.Stream@PNG-en-US.png)

   Assigning an IP address
4. ① Enter a suitable IP address for your computer.
5. ② Enter a suitable subnet mask.
6. ③ Click "Assign IP address".
7. Update the display at "Online access". The IP address is now displayed.

   The MAC address is read out automatically.

###### Result

The IP address has been assigned to the drive.

###### Assigning PROFINET device names

###### Assigning a name

In addition to the IP address, the drive must also be assigned a device name.

The name must comply with the DNS naming convention, for detailed information refer to the online help of the TIA Portal.

- The drive does not have a device name in the delivered state.
- If the drive already has a name, perform "Restore factory settings". The name is deleted.

###### Requirement

An online connection has been established to the device.

###### "Online access" procedure

To assign a name, proceed as follows:

1. Open "Online &amp; diagnostics" in the appropriate interface under "Online access" in the project navigator.
2. Open the "Functions" entry.
3. Double-click the "Assign name" entry in the secondary navigation.

   ![Assigning names](images/103319780107_DV_resource.Stream@PNG-en-US.png)

   ![Assigning names](images/103319780107_DV_resource.Stream@PNG-en-US.png)

   Assigning names
4. ① Enter a device name.
5. ② Click "Assign name" to assign a name to the drive.
6. Update the interface at "Online access". The name is now displayed.

###### Result

The name has been assigned to the drive.

##### Drive to higher-level controller

This section contains information on the following topics:

- [Creating a project offline](#creating-a-project-offline)
- [Searching for a controller and drives](#searching-for-a-controller-and-drives)
- [Assigning PROFINET device names in the network view](#assigning-profinet-device-names-in-the-network-view)

###### Creating a project offline

###### Overview

The following example shows how you can establish an online connection to drives via a higher-level controller:

- An S7-1500 is used as the controller.
- Two SINAMICS G120 CU240-2 drives communicate with the controller via a PROFINET subnet.
- You go online via the controller.
- The online connection to the drives is established via the controller.

###### Adding a controller and drives

To create the project offline, proceed as follows:

1. Create a new project and set up a controller, a CPU 1513-1 PN in this case.
2. Add two drives, e.g. two SINAMICS G120 CU240-2 with their power units.
3. Switch to the network view and assign the controller interface to the drives.

   ![PROFINET sample project](images/103319852299_DV_resource.Stream@PNG-en-US.png)

   PROFINET sample project
4. If required, switch to the topology view and interconnect the ports there for the PROFINET communication.
5. Open the drive in the project navigator and double-click "Parameters".

   The settings for this drive are shown in the inspector window.
6. Click the "General" tab in the foreground and check the settings of the PROFINET interface for the drive.

   ![Drive inspector window](images/103319856011_DV_resource.Stream@PNG-en-US.png)

   Drive inspector window

   ① Check the automatically assigned IP address and adapt it when necessary.

   ② If you have activated this checkbox, a PROFINET device name is assigned automatically.

   ③ The generated device name is displayed here. If you want to assign the name yourself, deactivate the "Generate PROFINET device name automatically" checkbox.

   ④ The drive with this device name together with the drive type is displayed in the project navigator. If you change the device name in the project navigator ("Rename"), this change is also reflected in the inspector window (see ③).

###### Searching for a controller and drives

###### Requirement

You have inserted the devices offline and created a PROFINET subnet. The devices have been switched on, wired and connected to the PG/PC.

###### Update accessible devices

Search for the devices for further configuration using the "Update accessible devices" function.

To display the devices of the PROFINET subnet, proceed as follows:

1. Open "Online access" in the project navigator.
2. Perform "Update accessible devices" at the interface that you use to go online.

   The TIA Portal browses the interface for the connected devices and displays them below the interface.

   The figure below displays the following details:

   - ① The devices are shown in the network view with their offline device names.
   - ② The devices are shown with their device names and device types in the project navigator.
   - ③ The devices found are listed under "Online access". The PLC already has an IP address.   
     The two drives are shown with the default device names assigned by the TIA Portal ("Node") and the MAC address. The factory settings are active for the two drives.  
     Therefore, they do not have an IP address or a device name.

   ![Controller with drive under "Online access"](images/103319942667_DV_resource.Stream@PNG-en-US.png)

   Controller with drive under "Online access"

In the next step, assign device names to the drives.

###### Assigning PROFINET device names in the network view

###### Assigning PROFINET device names in the network view

The devices are connected to a higher-level controller via a PROFINET subnet. In the next step, assign the device names to the drives that you have assigned offline, see also [Creating a project offline](#creating-a-project-offline).

When the drives have a device name, you can download the project to the controller. The IP addresses assigned in the project are automatically assigned to the drives.

###### Requirement

A connection has been established to the device.

###### Assigning a name

To assign the PROFINET device name, proceed as follows:

1. Open the network view.
2. Right-click the subnet and execute "Assign device name" in the shortcut menu.

   ![Assigning a device name](images/103320020491_DV_resource.Stream@PNG-en-US.png)

   Assigning a device name

   The "Assign PROFINET device name" dialog opens.

   ![Assign PROFINET device name dialog](images/103320049803_DV_resource.Stream@PNG-en-US.png)

   Assign PROFINET device name dialog
3. ① Select the device name that you want to assign.
4. ② Click "Update list" to search for the device in the PROFINET subnet. It is then displayed in the "Accessible devices in the network" list.

   Note the MAC addresses of the devices in your system so that you can determine the drive to which you have assigned the device name. The MAC address is on the rating plate of the drive.
5. ③ Select the device.
6. ④ Click "Assign name" to assign the selected name to the device.

   The device name is then also displayed at "Online access".

   If required, check the drive in the system to which you have assigned the name with "LED flashing".

   ![Device name assigned](images/103320053515_DV_resource.Stream@PNG-en-US.png)

   Device name assigned
7. Assign device names to all the other drives in the same way.
8. Click "Close" to accept the new settings.

###### Result

When you have assigned all the device names, they are displayed in the project navigator at "Online access". The drives still do not have an IP address and therefore the MAC address is still displayed.

![Device name assigned](images/103320057227_DV_resource.Stream@PNG-en-US.png)

Device name assigned

###### IP address assigned

After you have assigned the device names in the network view, download the settings to the controller. The controller automatically assigns the IP addresses to the drives that you have entered in the project.

![IP addresses assigned](images/103320060939_DV_resource.Stream@PNG-en-US.png)

IP addresses assigned

The IP addresses are only assigned in the project.

---

**See also**

[Setting PROFINET parameters](#setting-profinet-parameters)

##### Restoring factory settings

###### Restoring factory settings

If problems occur during the commissioning via PROFINET, it is recommended that the IP settings of the drive be restored to the factory settings. This provides a defined basis for an error-free commissioning.

###### Requirement

An online connection has been established to the drive.

###### Procedure

To restore the factory settings, proceed as follows:

1. Open the "Online &amp; diagnostics" entry at "Online access".
2. Double-click the entry.
3. Open the "Functions" entry.
4. Double-click the "Restore factory settings" entry in the secondary navigation.

   The dialog box with the current settings is displayed.

   ![Restoring factory settings](images/103320137611_DV_resource.Stream@PNG-en-US.png)

   ![Restoring factory settings](images/103320137611_DV_resource.Stream@PNG-en-US.png)

   Restoring factory settings
5. Click "Reset".

   The drive communication settings are reset to the factory settings.
6. Go offline and then establish an online connection again. The factory settings of the IP address and the device name are now displayed at "Online access".

###### Result

The communication settings show the factory settings again.

- Then assign an IP address and a device name to the drive, see [Assigning an IP address](#assigning-an-ip-address) and [Assigning PROFINET device names](#assigning-profinet-device-names).

##### Setting the PG/ PC interface

An Ethernet interface is required for the communication between the drive and the PG/PC via PROFINET.

You have the following functions to assign the PG/PC interface:

- "Go online" function (function is available until the PG/PC interface is set up successfully)
- "Online &amp; diagnostics" function
- "Online access" function

> **Note**
>
> **Accessible devices**
>
> If you search for the device via "Accessible devices", the PG/PC is automatically assigned a temporary IP address.

###### Assigning the PG/PC interface

The following procedure describes the process for the Ethernet interface type by using the "Online access" function.

To assign the interfaces, proceed as follows:

1. Navigate to the appropriate interface in the project navigator under "Online access".
2. In the shortcut menu, click "Properties".

   ![Online access properties](images/103320163979_DV_resource.Stream@PNG-en-US.png)

   Online access properties
3. In the next step, select the subnet and apply the setting with "OK" where applicable.

   ![Assigning a subnet](images/103320180491_DV_resource.Stream@PNG-en-US.png)

   Assigning a subnet

###### Adding an IP address in the subnet

1. Click ![Adding an IP address in the subnet](images/103320184203_DV_resource.Stream@PNG-en-US.png) on the toolbar.  
   The "Select devices for setting up the online connection" dialog box opens.

   ![Selecting a device for online connection](images/103320187915_DV_resource.Stream@PNG-en-US.png)

   Selecting a device for online connection
2. Select the device and confirm with "Connect".
3. Assign an IP address to the PG/PC within the subnet of the drive unit.  
   If you have not already done so, it is now possible to temporarily assign a suitable IP address from the subnet of the device via Windows Control Panel. Two dialogs then follow that illustrate the pending changes.
4. Confirm with "Yes".

###### Result

- You have assigned the PG/PC interface.
- The TIA Portal has assigned an IP address within a project.
- The online connection has been established.

###### Displaying and deleting temporary IP addresses

You can display and also delete all temporarily assigned addresses.

1. Navigate in the project navigator under "Online access" to the appropriate interface.
2. In the shortcut menu, click "Properties".
3. Under Configuration, select the "IE-PG Access" item.

   ![Displaying and deleting temporary IP addresses](images/103320191627_DV_resource.Stream@PNG-en-US.png)

   Displaying and deleting temporary IP addresses

---

**See also**

[Assigning an IP address](#assigning-an-ip-address)

#### Online connection via PROFIBUS DP

This section contains information on the following topics:

- [Online access via PROFIBUS DP](#online-access-via-profibus-dp)
- [Searching for a device via PROFIBUS](#searching-for-a-device-via-profibus)
- [Configuring the PROFIBUS interface](#configuring-the-profibus-interface)

##### Online access via PROFIBUS DP

###### Using PROFIBUS DP

Devices with a PROFIBUS interface allow the following:

- Establishing an online connection between the PG/PC and the drive
- Linking a drive to a PROFIBUS DP subnet with a higher-level controller.

###### Establishing an online connection between the PG/PC and the drive

The following requirements must be fulfilled for an online connection:

1. The drive and computer must be connected via a PROFIBUS cable.
2. The PROFIBUS interface must be configured correctly.

> **Note**
>
> **DIP switches on the drive**
>
> If you want to set the PROFIBUS address in Startdrive, the DIP switches on the device must all be set to "OFF". It is only possible to assign a PROFIBUS address via p918 in this setting.

###### Settings

You must make the following settings:

1. Configure the PROFIBUS interface on the PG/PC (PROFIBUS address, transmission rate).
2. Search for the device via "Online access".
3. Upload device to project
4. If required, restore factory settings.

###### Result

When you have established an online connection to the drive, check the settings. To do this, select "Online &amp; diagnostics &gt; Diagnostics &gt; Commissioning interface".

![PROFIBUS commissioning interface](images/103320239883_DV_resource.Stream@PNG-en-US.png)

PROFIBUS commissioning interface

The current PROFIBUS address of the drive is displayed.

---

**See also**

[Configuring the PROFIBUS interface](#configuring-the-profibus-interface)
  
[Searching for a device via PROFIBUS](#searching-for-a-device-via-profibus)

##### Searching for a device via PROFIBUS

###### Using online access

The TIA Portal can search for the drive via the online access of your computer.

###### Requirement

A connection has been established between computer and drive.

###### Procedure for online access

To search for a drive, proceed as follows:

1. Open the "Online access" entry in the project navigator.
2. Select the PROFIBUS interface of your computer.
3. If required, configure the interface.
4. Double-click "Update accessible devices".

   The "Select devices" dialog box is displayed.
5. Select the drive that you want to edit.

###### Procedure via accessible devices

To search for a drive via "Accessible devices", proceed as follows:

1. Click "Accessible devices".

   The dialog box with the same name opens.
2. Select the PROFIBUS interface of your PG/PC.
3. Click "Start search" to search for the device.

   The connected devices are displayed under "Accessible devices of the selected interface".
4. Select the device from the list and click "Display".

   The name is now displayed under "Online access".

###### Result

An online connection is established. Now edit the drive communication settings and upload the drive to the project, see also [Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software).

##### Configuring the PROFIBUS interface

###### Configuring the interface at "Online access"

To be able to go online on a drive via PROFIBUS DP, your computer requires a PROFIBUS interface. The interface is displayed in the TIA Portal at "Online access".

Before you go online via PROFIBUS, make sure that the interface settings are correct for your current task.

###### Procedure

To configure the interface, proceed as follows:

1. Right-click the interface entry and open "Properties".

   ![Properties of the PROFIBUS interface](images/103320361099_DV_resource.Stream@PNG-en-US.png)

   ![Properties of the PROFIBUS interface](images/103320361099_DV_resource.Stream@PNG-en-US.png)

   Properties of the PROFIBUS interface
2. Select "General" in the secondary navigation.
3. Select the PROFIBUS interface variant in "Configuration" at "Active configuration". A drive is not found in the "MPI" setting.
4. Click "PROFIBUS" in the secondary navigation.

   ![Parameterizing the PROFIBUS interface](images/103320365067_DV_resource.Stream@PNG-en-US.png)

   ![Parameterizing the PROFIBUS interface](images/103320365067_DV_resource.Stream@PNG-en-US.png)

   Parameterizing the PROFIBUS interface
5. Select the "Is the only master" option under "Local settings" if your computer is the only master within the PROFIBUS subnet.
6. Click "OK".

For more detailed information, see "Using online and diagnostic functions".

### Entering parameters in the project offline

This section contains information on the following topics:

- [Setting PROFINET parameters](#setting-profinet-parameters)
- [Setting PROFIBUS parameters](#setting-profibus-parameters)

#### Setting PROFINET parameters

##### Entering PROFINET parameters in the project

In addition to online parameterization, you can also create drives offline in the project.

If you want to go online on these drives, you must set their PROFINET interface parameters. If the factory settings still apply for the drive, you must first assign the IP address and the PROFINET device name (initialization), see also [Online connection via PROFINET IO](#online-connection-via-profinet-io).

If an IP address and device name have already been assigned in your drive, you can enter these parameters offline in the PROFINET interface screen forms. See [Creating a project offline](#creating-a-project-offline) and [Assigning PROFINET device names in the network view](#assigning-profinet-device-names-in-the-network-view).

##### Requirement

You have already created a project and configured the drive.

##### Entering the IP address and device name

To enter the IP address and the device name for the drive, proceed as follows:

1. Double-click "Parameter" under the drive in the project navigator.

   The parameterization editor is displayed.
2. Click "General" in the inspector window.
3. Select "Ethernet addresses" under the PROFINET interface.
4. Enter the IP address into the "IP protocol" section.
5. Enter a PROFINET device name.

   The automatically generated device name is displayed under "Converted name". Any illegal characters in the device name are converted to permissible characters. Detailed information can be found in the online help of the TIA Portal.
6. After you have made the settings, go online on the drive.
7. To do this, click "Go online".

#### Setting PROFIBUS parameters

##### Entering PROFIBUS parameters in the project

In addition to online parameterization, you can also create drives in the project offline and then go online.

If you want to go online on these drives, you must set the parameters of the drive PROFIBUS interface, see [Online connection via PROFIBUS DP](#online-connection-via-profibus-dp).

You can set the PROFIBUS address of the converter using the address switches (DIP switches) on the Control Unit, via parameter p0918 or in Startdrive. You can set the address via parameter p0918 (factory setting: 126) or via Startdrive when all address switches are set to "OFF" (0) or "ON" (1). If you set a valid address using the address switches, this address is always valid and parameter p0918 cannot be changed.

##### Requirement

You have already created a project and configured the drive.

##### Entering the address and transmission rate

To enter the PROFIBUS address for the drive, proceed as follows:

1. Double-click "Parameter" under the drive in the project navigator.

   The parameterization editor is displayed.
2. Click "General" in the inspector window.
3. Select "PROFIBUS address" under the PROFIBUS interface.
4. Select the address from the drop-down list.
5. Select a value at "Transmission rate".
6. After you have made the settings, go online on the drive.
7. To do this, click "Go online".

### Go online, upload and download

This section contains information on the following topics:

- [Go online](#go-online)
- [Going offline](#going-offline)
- [Upload from device (software)](#upload-from-device-software)
- [Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software)
- [Performing a download](#performing-a-download)

#### Go online

##### Requirement

The wiring between the PG/PC and the drive has been performed correctly. The drive is already inserted in the project.

Detailed information on the online mode can be found in the online help under "Online and diagnostics".

##### Establishing an online connection to a drive/device

To establish an online connection to a drive/device, proceed as follows:

1. Select the drive in the project navigator.
2. Click "Go online".

   An online connection is established, the color of the title bar changes to "orange".

##### Establishing an online connection to several drives/devices

To establish an online connection to several drives/devices, proceed as follows:

1. Select the project in the project navigator.
2. Click "Go online".

   The "Select devices" dialog box is displayed.
3. Select the devices to which you want to establish an online connection.
4. Click "Connect".

##### Result

Startdrive establishes an online connection to the selected drives/devices.

#### Going offline

##### Requirement

There is an online connection to one or more drives/devices. If you want to save the online settings permanently, upload the settings or perform "Save RAM data to EEPROM".

##### Disconnecting the online connection to a drive/device

To disconnect an online connection to a drive/device, proceed as follows:

1. Select the drive in the project navigator.
2. Click the "Go offline" button.

   The online connection is disconnected, the color of the title bar changes to "blue".

##### Disconnecting the online connection to several drives/devices

To disconnect an online connection to several drives/devices, proceed as follows:

1. Select the project in the project navigator.
2. Click the "Go offline" button.

   The "Select devices" dialog box is displayed.
3. Select the devices to which you want to disconnect the online connection.
4. Click "Disconnect".

##### Result

Startdrive disconnects the online connection to the selected drives/devices.

#### Upload from device (software)

##### Loading device and parameter settings from the drive to the project

During an upload, device data and parameter settings are loaded from the drive to the project. If you start the upload, the device must be offline. Multiple selection with subsequent upload of all devices is possible.

A distinction is made between two cases:

- Upload of an entire device that was found via the "Online access" function, see [Uploading the device as a new station (hardware and software)](#uploading-the-device-as-a-new-station-hardware-and-software).
- Upload of the parameter settings of a device to the project.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of data**  If you upload the parameter settings from the drive to the project, the offline settings are overwritten. |  |

If inconsistencies could occur in the project as a result of the upload, the "Upload preview" dialog is displayed. Check whether the requirements displayed in this dialog are correct for your project.

The following cases can occur, for example:

- The version of the device found online is different to the device that was inserted offline in the project.
- The article number of the Power Module found online is not found in the hardware catalog.
- The control panel is active.
- The telegram configurations differ.
- Unit settings are different.

##### Uploading parameter settings

To upload the parameter settings of a drive to your project, proceed as follows:

1. Select the drive in the project navigator.
2. Click "Upload from device".

   If there are preconditions, the "Upload preview" dialog is displayed.
3. If the requirements for the upload are satisfied, activate the option.
4. Click "Upload from device" to upload the device to the project.

##### Result

The parameter settings are accepted in the project.

#### Uploading the device as a new station (hardware and software)

##### Uploading a single drive unit from "Online access"

Single drives can be uploaded to the project together with the configured settings.

To upload a device, proceed as follows:

1. Click "Online access" in the project navigator.
2. Select the interface used.
3. Double-click "Update accessible devices".

   Startdrive goes online and searches for devices via the selected interface.

   The found devices are displayed below the interface in the project navigator.
4. Select the device. Then perform "Online &gt; Upload device as new station (hardware and software)".

   The "Upload preview" dialog box is displayed.
5. If the requirements for the upload are satisfied, activate the option.
6. Click "Upload from device" to upload the device to the project.

##### Uploading the controller and drive (station upload)

If your drive is connected to a controller, e.g. an S7-1500, via PROFIBUS DP or PROFINET IO, you can accept the devices in the project.

> **Note**
>
> **For G110M/G115D connected to a controller**
>
> A complete station upload of the controller creates a proxy of the drive via AS-i master.
>
> The configuration can be compiled and downloaded again but the proxy object cannot be edited.

You can then restore your project using runtime data without having the original project data. The configuration is created in a new TIA Portal project. You can then obtain an overview of the currently active configuration in the TIA Portal and perform diagnostics.

The following cases can occur:

1. Upload of the controller with a proxy object of the drive. If you upload the controller first, a proxy object is created for the drive in the network view. The configuration can be compiled and downloaded again.
2. Upload of the drive if a proxy object has already been created with the controller. To do this, you must upload the drive using the "Online &gt; Upload device as new station (hardware and software)" function under "Online access". An upload from the network view is not supported.
3. Upload of the controller when the drive has already been loaded.

> **Note**
>
> **Requirement for the upload to a proxy object**
>
> The device name, the fieldbus address and the I/O configuration and/or the telegram configuration must be identical. Otherwise the proxy object is not updated, and instead a new drive is created in the project.

Example:

"Drive_1" is stored as device name in the drive, but the drive was assigned "Conveyor belt" as device name via the CPU. The combination prevents the upload because the settings are different in the drive and in the project. If the upload does not function, check the settings in the drive, for example, by going online on the drive via USB.

##### Uploading the controller with drives (station upload)

The controller and the drives are already preconfigured, e.g. on a system. The following example illustrates the procedure:

- S7-1500 CPU1515 PN/DP
- Two G120 CU240-2 PN
- PROFINET subnet

To upload the configuration, proceed as follows:

1. Click "Online access" in the project navigator.
2. Select the online access.
3. Double-click "Update accessible devices".

   Startdrive goes online and searches for devices via the selected interface.
4. Select the controller found at the interface.
5. Perform "Online &gt; Upload device as new station (hardware and software)".

   The controller is uploaded and displayed. The available drives are uploaded as proxy objects (see following figure).

   ![Station upload with proxy](images/103320625419_DV_resource.Stream@PNG-en-US.png)

   Station upload with proxy
6. Select the drive at "Go online" and perform "Online &gt; Upload device as new station (hardware and software)".

   The configuration is uploaded and the proxy object replaced by the drive.

   ![Uploading the drive](images/103320629131_DV_resource.Stream@PNG-en-US.png)

   Uploading the drive
7. Perform step 6 again to upload the second drive.

##### Result

The devices are uploaded to the project and the parameter settings are uploaded to the project.

The device names are uploaded and supplemented by the device type.

---

**See also**

[Upload from device (software)](#upload-from-device-software)
  
[Online connection via USB](#online-connection-via-usb)

#### Performing a download

##### Requirement

You have set up an online connection to all devices on which you plan a download. As soon as you initiate a download offline, Startdrive automatically attempts to establish an online connection.

> **Note**
>
> If your project contains several devices, you can select these devices in the project navigator and trigger a download to the selected devices.

##### Loading parameter settings to the device

With a download, you load the parameter settings made offline to the drive.

If inconsistencies can occur because of the download, the "Download preview" dialog box is displayed. Check whether the requirements displayed in this dialog box are correct for your project.

The following cases can occur, for example:

- The version of the device connected online is different to the device that was inserted offline in the project:

  - The firmware version in the device is newer than the version in the project. The download can be forced.
  - The firmware version in the device is older than the version in the project. A download is then not possible.
- The control panel is active.
- The telegram configurations differ.
- Unit settings are different.

As soon as the download is completed, the "Download result" dialog box opens. The download status is displayed there.

##### Procedure

To download the parameter settings of a project to the drive, proceed as follows:

1. Select the drive in the project navigator. Click "Load to device".

   If there are preconditions, the "Download preview" dialog box is displayed.
2. If the requirements for the upload are satisfied, activate the option.
3. Click "Load to device" to transfer the parameter settings to the device.

##### Result

The parameter settings are the same online and offline.

### Online & diagnostics

This section contains information on the following topics:

- [Online access status](#online-access-status)
- [General diagnostics](#general-diagnostics)
- [Active alarms and faults](#active-alarms-and-faults)
- [Alarm and fault history](#alarm-and-fault-history)
- [Control/status words](#controlstatus-words)
- [Drive enables](#drive-enables)
- [Commissioning interface](#commissioning-interface)
- [Safety Integrated](#safety-integrated)
- [Displaying diagnostics status and comparison status](#displaying-diagnostics-status-and-comparison-status)

#### Online access status

##### Checking the online access

"Online access" displays the current status of the online connection for the drive unit. The required information is provided here to establish an online connection when problems occur.

##### Status

The status of the online connection is shown here:

- An online connection is represented by a solid green line.

  ![Status](images/120454983563_DV_resource.Stream@PNG-en-US.png)
- An interrupted connection is represented by a gray line with interruption symbol.

  ![Status](images/103320702475_DV_resource.Stream@PNG-en-US.png)

"LED flashing" can be used to identify the device in the hardware configuration. This function is only possible when the connected device supports "LED flashing" (refer to the device description).

#### General diagnostics

##### General diagnostics

The drive data is displayed at "General diagnostics". You can therefore identify the drive and are supplied with the most important drive data.

![General diagnostics](images/103320727179_DV_resource.Stream@PNG-en-US.png)

General diagnostics

> **Note**
>
> **PROFINET drives without node initialization**
>
> If you have established an online connection to a PROFINET drive, and the drive has not been assigned an IP address or a device name (no node initialization), then the general diagnostics view is empty.

#### Active alarms and faults

##### Description

"Active alarms and faults" displays the currently pending alarms and faults.

- With a fault, the parameterized fault reaction is started and the ZSW1.3 status signal is issued. The fault is also entered in the fault buffer. Faults must be acknowledged after the cause has been corrected.
- With an alarm, status signal ZSW1.7 is set. The alarm is also entered in the alarm buffer.

  ![Description](images/171259892107_DV_resource.Stream@PNG-en-US.png)

##### Faults and alarms

| Column | Description |
| --- | --- |
| Fault buffer / alarm buffer | Designation of the fault |
| Fault code / alarm code | Number of the fault/alarm |
| Message | Description of the fault/alarm |
| Fault time / alarm time | Time stamp that shows when the fault/alarm occurred |

##### Acknowledging faults

- ① Click this button to acknowledge all active faults.

After acknowledgement, faults and alarms are moved to the message history, see also [Alarm and fault history](#alarm-and-fault-history).

#### Alarm and fault history

##### Alarm and fault history

The individual drive components have a message history in which all alarms and faults are recorded. You can read out this history in online mode.

History made up of faults and alarms.

##### Delete fault buffer

1. ① Click the button to delete the fault buffer.
2. ② Click the button to export the fault buffer to a CSV file.

![Alarm and fault history](images/171260037387_DV_resource.Stream@PNG-en-US.png)

Alarm and fault history

##### Faults

| Column | Description |
| --- | --- |
| Fault buffer | Designation of the fault |
| Fault code | Number of the fault |
| Message | Description of the message |
| Fault time "received" | Time stamp that shows the time when a fault occurred |
| Fault time "resolved" | Time stamp that shows the time when the cause of the fault was corrected. The fault must be acknowledged in addition. |

##### Alarms

| Column | Description |
| --- | --- |
| Alarm buffer | Designation of the alarm |
| Alarm code | Number of the alarm |
| Message | Description of the message |
| Alarm time "received" | Time stamp that shows the time when an alarm occurred |
| Alarm time "resolved" | Time stamp that shows the time when the cause of the alarm was corrected. |

#### Control/status words

##### Displaying control/status words

The "Control/status words" dialog box displays the various control and status words for the diagnostics.

The signals that are actually used by the converter are highlighted by LED displays. The display is only relevant when the drive is controlled via fieldbus.

#### Drive enables

##### Display of the drive enables

The "Drive enables" dialog box displays the missing drive enables required for the operation of the converter.

#### Commissioning interface

##### Interface overview

The various commissioning interfaces are clearly displayed here.

![Commissioning interface](images/103320943883_DV_resource.Stream@PNG-en-US.png)

Commissioning interface

##### Display of the USB data

The device name and the serial number are displayed for the USB interface. They are read out automatically.

##### PROFIBUS

The PROFIBUS interface is displayed for the PROFIBUS address:

Analogous to the position of the DIP switches on the device, the PROFIBUS address is displayed graphically in this screen form.

If you want to set the PROFIBUS address via Startdrive, the DIP switches on the device must all be set to "OFF" (address 0) or to "ON" (address 127). In this setting, it is possible to assign a PROFIBUS address via parameter p918.

**Changing the PROFIBUS address**

You can only change the PROFIBUS address in the parameter view.

- To do so, go online with the drive.
- Enter the address in parameter p918.

#### Safety Integrated

##### Diagnostics of the safety functions

This screen form displays the current state of the drive safety functions:

| Display | Description |
| --- | --- |
| STO active | Safe torque off is active. |
| SS1 active | Safe stop 1 is active. |
| SLS active | Safely-limited speed is active; also displays the active level. |
| Active SLS limit value | Displays the active SLS value. |
| Velocity below SSM limit value | Displays whether the currently active speed is below the value configured in SSM. |
| SDI positive active | Safe direction in positive direction is active. |
| SDI negative active | Safe direction in negative direction is active. |
| Test of the shutdown paths | Displays whether a test of the shutdown paths is required. |
| Internal event | - |

![Safety diagnostics](images/103320981515_DV_resource.Stream@PNG-en-US.png)

Safety diagnostics

#### Displaying diagnostics status and comparison status

This section contains information on the following topics:

- [Diagnostics and comparison icons](#diagnostics-and-comparison-icons)

##### Diagnostics and comparison icons

###### Icons in the TIA Portal and Startdrive

The diagnostics status and comparison status of drives and higher-level controllers are displayed via icons in the user interface.

A description of the icons can be found at "Displaying diagnostics status and comparison status using icons".

### Fault and alarm concept for SINAMICS drives

This section contains information on the following topics:

- [SINAMICS faults and alarms](#sinamics-faults-and-alarms)
- [Explanations for SINAMICS Faults and Alarms](#explanations-for-sinamics-faults-and-alarms)

#### SINAMICS faults and alarms

##### Fault and alarm displays

If a fault occurs, the drive indicates the fault and/or alarm.

The following methods for displaying faults and alarms are available:

- Via the fault and alarm buffer with PROFIBUS.
- Online via the commissioning software. If a fault occurs, the drive displays the fault(s)/alarm(s).

##### Differences between faults and alarms

The differences between faults and alarms are as follows:

| Type | Description |
| --- | --- |
| Faults | What happens when a fault occurs?  - The appropriate fault response is initiated. - Status signal ZSW1.3 is set. - The fault is entered in the fault buffer.   How are faults eliminated?  - Remove the original cause of the fault. - Acknowledge the fault. |
| Alarms | What happens when an alarm occurs?  - Status signal ZSW1.7 is set. - The alarm is entered in the alarm buffer.   How are alarms eliminated?  - Alarms acknowledge themselves. If the causes of the alarms are no longer present, they automatically reset themselves. |

##### Fault reactions

The following fault reactions are defined:

| List | PROFIdrive | Reaction | Description |
| --- | --- | --- | --- |
| NONE | - | None | No reaction when a fault occurs. Note: When the "Basic positioner" function module is activated (r0108.4 = 1), the following applies: When a fault occurs with fault reaction "NONE", an active motion command is aborted and the system switches to follow-up mode until the fault has been rectified and acknowledged. |
| OFF1 | ON/OFF | Brake along the ramp-function generator deceleration ramp followed by pulse disable | **Closed-loop speed control (p1300 = 20, 21)**   - The immediate specification of n_set = 0 at the ramp generator return ramp (p1121) causes the drive to be braked. - When zero speed is detected, the motor holding brake (if parameters have been assigned for it) is closed (p1215). The pulses are suppressed when the brake closing time (p1217) expires. Standstill is detected when the actual speed value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint ≤ speed threshold (p1226) has expired.    **Closed-loop torque control (p1300 = 23)**   - The following applies to closed-loop torque control mode: Reaction as for OFF2 - When the system switches to closed-loop control with p1501, the following applies:   No separate braking reaction.   If the actual speed value falls below the speed threshold (p1226) or the timer stage (p1227) has expired, the motor holding brake (if one is being used) is closed. The pulses are suppressed when the brake closing time (p1217) expires. |
| OFF2 | COAST STOP | Internal/external pulse disable | **Closed-loop speed and torque control**   - Instantaneous pulse suppression, the drive "coasts" to a standstill. - The motor holding brake (if one is being used) is closed immediately. - Power-on inhibit is activated. |
| OFF3 | QUICK STOP | Brake along the OFF3 deceleration ramp followed by pulse disable | **Closed-loop speed control (p1300 = 20, 21)**   - The drive is braked along the OFF3 down ramp (p1135) by immediately entering n_set = 0. - When zero speed is detected, the motor holding brake (if parameterized) is closed. The pulses are suppressed when the closing time of the holding brake (p1217) expires. Standstill is detected when the actual speed value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint ≤ speed threshold (p1226) has expired. - Power-on inhibit is activated. Closed-loop torque control (p1300 = 23) - Switchover to speed-controlled operation and other reactions as described for speed-controlled operation. |
| STOP1 | - | - | In preparation |
| STOP2 | - | n_set = 0 | - The drive is braked along the OFF3 down ramp (p1135) by immediately entering n_set = 0. - The drive remains in closed-loop speed control mode. |
| IASC/DC BRAKING | - | - | - For synchronous motors, the following applies:   If a fault occurs with this fault reaction, an internal armature short-circuit is triggered.   The conditions for p1231 = 4 must be observed. - For induction motors, the following applies:   If a fault occurs with this fault reaction, DC braking is triggered.   DC braking must have been commissioned (p1232, p1233, p1234). |
| ENCODER | - | Internal/external pulse disable (p0491) | The fault reaction ENCODER is applied as a function of the setting in p0491.  Factory setting:  p0491 = 0 -&gt; encoder error results in OFF2   **Important**:  When changing p0491, it is imperative that the information in the description of this parameter is carefully observed. |

##### Acknowledgement of faults

The list of faults and alarms specifies how to acknowledge each fault after the cause has been remedied.

| Acknowledgement | Description |
| --- | --- |
| POWER ON | The fault is acknowledged by a POWER ON process (switch drive unit off and on again).  Note:  If this action has not eliminated the fault cause, the fault is displayed again immediately after power up. |
| IMMEDIATELY | Faults can be acknowledged on one drive object (Points 1 to 3) or on all drive objects (point 4) as follows:  1. Acknowledging by setting a parameter:    p3981 = 0 -&gt; 1 2. Acknowledging via binector inputs:    p2103 BI: 1. Acknowledge faults    p2104           BI: 2. Acknowledge faults    p2105           BI: 3. Acknowledge faults 3. Acknowledging via a PROFIBUS control signal:    STW1.7 = 0 -&gt; 1 (edge) 4. Acknowledge all faults    p2102 BI: Acknowledge all faults    All of the faults on all of the drive objects of the drive system can be acknowledged using this binector input.   Note:  - These faults can also be acknowledged by a POWER ON operation. - If this action has not eliminated the fault cause, the fault will continue to be displayed after acknowledgement. -  Safety Integrated faults   The "Safe Standstill" (SH) function must be deselected before acknowledging these faults. |
| PULSE INHIBIT | The fault can only be acknowledged with a pulse inhibit (r0899.11 = 0).  The same possibilities are available for acknowledging as described under acknowledge IMMEDIATELY. |

#### Explanations for SINAMICS Faults and Alarms

##### Online help for the alarms and faults

An example is used to explain the relevant terms. The data in the following example has been chosen at random. A description can contain the information listed below. Some of the information is optional.

##### Example

| Field | Description |
| --- | --- |
| **Axxxxx (F,N)** | Fault location (optional): Name |
| **Message value:** | Component number: %1, cause: %2 |
| **Drive object:** | List of objects. |
| **Reaction:** | NONE |
| **Acknowledgement:** | NONE |
| **Cause:** | Description of possible causes.  Fault value (r0949, interpret format): or alarm value (r2124, interpret format): (optional)  Information about fault or alarm values (optional). |
| **Remedy:** | Description of possible remedies. |
| **Reaction to F:** | A_INFEED: OFF2 (OFF1, NONE)  SERVO: NONE (OFF1, OFF2, OFF3)  VECTOR: NONE (OFF1, OFF2, OFF3) |
| **Acknowledgement for F:** | IMMEDIATELY (POWER ON) |
| **Reaction to N:** | NONE |
| **Acknowledgement for N:** | NONE |

##### General structure

| Field | Description |
| --- | --- |
| **Axxxxx** | Alarm xxxxx |
| **Axxxxx (F,N)** | Alarm xxxxx (message type can be changed to F or N) |
| **Fxxxxx** | Fault xxxxx |
| **Fxxxxx (A, N)** | Fault xxxxx (message type can be changed to A or N) |
| **Nxxxxx** | No message |
| **Nxxxxx (A)** | No message (message type can be changed to A) |
| **Cxxxxx** | Safety message (dedicated message buffer) |

A message comprises a letter followed by the relevant number. The letters have the following meaning:

- A means "Alarm"
- F means "Fault"
- N means "No report" or "Internal report"
- C means "Safety message"

The optional brackets indicate whether the type specified for this message can be changed and which message types can be adjusted via parameter (p2118, p2119). Information about reaction and acknowledgement is specified independently for a message with adjustable message type (e.g. reaction to F, acknowledgement for F).

| Term | Description |
| --- | --- |
| Fault location (optional):  Name | The fault location (optional), the name of the fault or alarm and the message number are all used to identify the message (e.g. with the commissioning software). |
| Message value | The information provided under message value informs you about the composition of the fault/alarm value.  Example:  Message value: Component number: %1, cause: %2  This fault value or alarm value contains information about the component number and cause. The entries %1 and %2 are placeholders, which are filled appropriately in online operation with the commissioning software. |
| Drive object | For each message (fault/alarm) it is specified in which drive object this message is present. A message can belong to either one, several or all drive objects. |
| Reaction:  Default fault reaction (adjustable fault reaction) | Specifies the default reaction in the event of a fault.  The optional brackets indicate whether the default fault reactions can be changed and which fault reactions can be adjusted via parameters (p2100, p2101). |
| Acknowledgement:  Default acknowledgement (adjustable acknowledgement) | Specifies the default method of acknowledging faults after the cause has been eliminated.  The optional brackets indicate whether the default acknowledgement can be changed and which acknowledgement can be adjusted via parameter (p2126, p2127). |
| Cause | Description of the possible causes of the fault/alarm. A fault or alarm value can also be specified (optional).  Fault value (r0949, format):  The fault value is entered in the fault buffer in r0949[0...63] and specifies additional, precise information about a fault.  Alarm value (r2124, format):  The alarm value specifies additional, precise information about an alarm.  The alarm value is entered in the alarm buffer in r2124[0...7] and specifies additional, precise information about an alarm. |
| Remedy | Description of the methods available for eliminating the cause of the active fault or alarm.   **Warning:**   In certain cases, the servicing and maintenance personnel are responsible for choosing a suitable method for eliminating the cause of faults. |
