---
title: "Compiling and loading (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: TransferWCCPenUS
topics: 245
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Compiling and loading (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Establishing a connection to the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#establishing-a-connection-to-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Basic Panels (Basic Panels)](#basic-panels-basic-panels)
- [Runtime Advanced and Panels (Panels, Comfort Panels, RT Advanced)](#runtime-advanced-and-panels-panels-comfort-panels-rt-advanced)
- [Runtime Professional (RT Professional)](#runtime-professional-rt-professional)
- [Jumping to the configuration (RT Advanced)](#jumping-to-the-configuration-rt-advanced)
- [Jumping to the configuration (RT Professional)](#jumping-to-the-configuration-rt-professional)
- [Servicing the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#servicing-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Printer driver (Comfort Panels)](Printer%20driver%20%28Comfort%20Panels%29.md#printer-driver-comfort-panels)

## Establishing a connection to the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Introduction

To download a WinCC project to an HMI device, a properly configured connection must be set up between the configuration PC and HMI device. The connection cannot be set up, the download is cancelled.

### Setting up a connection between the configuration PC and HMI device

1. Check the cable connection between the HMI device and configuration PC.
2. Open the "Devices &amp; Networks" editor in WinCC and start the network view.
3. Select the subnet in the network view and check the settings for the subnet.
4. Select the interface of the HMI device in the network view or device view and check the connection parameters in the Inspector window.
5. Switch on the HMI device and press the "Control Panel" button in the loader.

   The Control Panel opens.
6. Press "Transfer" twice in the Control Panel.

   The "Transfer Settings" dialog box opens.
7. Check the settings and then press "Advanced".

   The [Protocol*] Settings" dialog opens.

   *: The title of the dialog depends on the protocol used, for example, "PROFIBUS Settings".
8. Check the advanced settings and close the dialog with "OK".

### Important settings

Check the connection settings and in particular the following parameters:

- Network and station addresses
- Selected transmission rate
- Master on the bus; as a general rule, only one master is permitted.

> **Note**
>
> **Connections over Ethernet**
>
> For Ethernet-based communication, check the required network settings. You can find additional information under "Readme &gt; WinCC &gt; Security information".

If using a configurable adapter for the connection, check the adapter settings, for example, transmission rate, master on the bus.

---

**See also**

[Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)

## Basic Panels (Basic Panels)

This section contains information on the following topics:

- [Runtime settings (Basic Panels)](#runtime-settings-basic-panels)
- [Overview of compiling and loading projects](#overview-of-compiling-and-loading-projects)
- [Compiling a project (Basic Panels)](#compiling-a-project-basic-panels)
- [Simulating projects (Basic Panels)](#simulating-projects-basic-panels)
- [Loading projects (Basic Panels)](#loading-projects-basic-panels)
- [Compiling and loading with Multiuser Engineering (Basic Panels)](#compiling-and-loading-with-multiuser-engineering-basic-panels)
- [Starting Runtime (Basic Panels)](#starting-runtime-basic-panels)
- [Error messages during loading of projects (Basic) (Basic Panels)](#error-messages-during-loading-of-projects-basic-basic-panels)
- [Adapting the project for another HMI device (Basic Panels)](#adapting-the-project-for-another-hmi-device-basic-panels)
- [Reducing the project size (Basic Panels)](#reducing-the-project-size-basic-panels)
- [Basics of operating in Runtime (Basic Panels)](#basics-of-operating-in-runtime-basic-panels)
- [Entering bar codes with optical handheld readers (Basic Panels)](#entering-bar-codes-with-optical-handheld-readers-basic-panels)
- [Security on the HMI device (Basic Panels)](#security-on-the-hmi-device-basic-panels)

### Runtime settings (Basic Panels)

This section contains information on the following topics:

- [Runtime settings (Basic Panels)](#runtime-settings-basic-panels-1)
- [Configuring display in Runtime](#configuring-display-in-runtime)
- [Configuring operation in Runtime (Basic Panels)](#configuring-operation-in-runtime-basic-panels)
- [Compatibility check with the controller](#compatibility-check-with-the-controller)
- [Password protection in runtime (Basic Panels)](#password-protection-in-runtime-basic-panels)

#### Runtime settings (Basic Panels)

##### Introduction

To edit the runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree.

> **Note**
>
> **Device dependency**
>
> The options available for selection in the runtime settings depend on the HMI device.

##### Overview

You configure options from different areas of your project in the runtime settings:

- Display in runtime

  - Start screen
  - Default template
  - Default style of the project and style of the HMI device
  - Screen resolution
  - Full-screen mode
  - Project graphics
  - Bit selection for color and flashing
  - Bit selection for text and graphic lists
- Project ID for compatibility check with the controller
- Logging language
- Remote control via Sm@rt server in the "Services" area

  You can find additional information on this in the WinCC online help under "Options &gt; Sm@rt options"
- Operator control in runtime

  - Task switching
  - Load additional information for debugging scripts: Object names and comments in scripts
  - Show limits as a tooltip
  - Screen keyboard
  - Disable function keys
  - Release buttons when cursor leaves the button
  - Keyboard layout and shortcuts
- GMP-compliant configuration

  You can find additional information on this in the WinCC online help under "Options &gt; WinCC Audit".
- Alarms

  - Buffer overflow
  - Acknowledgment group text
  - Log
  - Colors of the alarm classes
  - Download S7 diagnostic help texts
  - Configuration of the system events: Display duration
  - Persistent alarm buffer
- User administration

  - Configuration password and logoff time
  - Limit for login attempts
  - Hierarchy levels
  - Configuration of SIMATIC Logon
- Language and font

  - Available runtime languages
  - Order of language switching
  - Default font
  - Download font with valid license
- Configuration of the OPC Unified Architecture Server
- Settings for synchronization of PLC and HMI tags

---

**See also**

[Configuring display in Runtime](#configuring-display-in-runtime)
  
[Configuring operation in Runtime (Basic Panels)](#configuring-operation-in-runtime-basic-panels)
  
[Compatibility check with the controller](#compatibility-check-with-the-controller)
  
[Editing system events (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#editing-system-events-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring alarm buffer overflow (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-alarm-buffer-overflow-panels-comfort-panels-rt-advanced)
  
[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-the-user-administration-basic-panels)
  
[Managing languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring display in Runtime

##### Introduction

In the Runtime settings you specify how screens, alarms and language are displayed.

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree. The options available for selection depend on the HMI device.

##### Display on the target system

In WinCC, configure the visual representation of the generated project in Runtime:

- Select the full-screen or window mode for the project. The window has a smaller size than the screen. In full-screen mode, the project is zoomed to the full screen. There will be no window and operator controls for this view.   
  Click "General" in the "Settings" editor to activate the full-screen display at startup. Activate the "Full-screen mode" check box in the "Screen" field.

  > **Note**
  >
  > **Truncated view**
  >
  > If the HMI screen does not match the configured size (in pixels), the project only appears on part of the screen in full-screen mode.
- Under "General &gt; Screen", you specify whether the HMI device uses the default style of the project or another pre-defined style.

##### Screen settings

In the Runtime settings, specify the start screen and default template. You can find additional information in the online help for WinCC under "Working with screens".

##### Language settings

- Logging language

  Under "General &gt; Logs", you specify the language in which you want to write the logs. The selected logging language always remains the same, even if the user switches the language in Runtime.

  If you select "Startup language", the logging language remains the same until Runtime is stopped, even if the user has switched the language. However, the next time Runtime is started, the last configured Runtime language is used as the logging language.
- Runtime language

  Under "Language &amp; font", you specify all Runtime languages and their display. Text entries may be truncated if you selected an unsuitable font size or style. This setting can, for example, affect the following texts:

  - Tooltips
  - Long alarm text
  - Text in dialogs

##### Setting for specific screen objects

- Specify bit selection

  Under "Screens &gt; Bit selection", you specify whether bit selection will be used on this HMI device for the following:

  - Text and graphics (text lists and graphic lists)
  - Color and flashing (appearance analysis)

    When you enable an option, the selection that is configured in the set bit with the least significance is displayed:

    When you disable an option and several bits are set, the selection that has been configured only for the set bit is displayed.
- Tooltips for I/O fields

  Under "Screens &gt; Display", you specify whether configured limit values are displayed as tooltips in Runtime when values are entered in I/O fields.
- Colored objects

  You specify the color depth of your HMI device under "General &gt; Screens &gt; Color depth". As needed, you assign screen objects a colored appearance. The range of colors is determined by the color depth supported on your selected HMI device.

#### Configuring operation in Runtime (Basic Panels)

##### Introduction

In the Runtime settings you specify how screens are operated, and how you use keys for operation in Runtime.

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree. The options available for selection depend on the HMI device.

##### Locking task switching

Depending on the HMI device, you can lock task switching on the HMI device. This will prevent the operator from opening other applications in Runtime.

In the Runtime settings of the HMI device, enable the "Lock task switching" option under "General &gt; Screen".

> **Note**
>
> **Stop Runtime**
>
> If you lock program switching, always configure in your project the system function "StopRuntime" for an object, e.g. a softkey or button.

##### Settings for data transfer to the HMI device

- Transferring names of the screen objects in scripts

  If you enable the "Load names" option under "General &gt; Screen", the object names of the screen objects are transferred instead of coded addressing information. You need the object names, if you want to address the screen objects in a script via the object names. When you test a script in the debugger, the code becomes more comprehensible by displaying the object names.
- Displaying comments in scripts

  Under "Screens &gt; Display", you specify whether the comments in scripts are also transferred to the HMI device.

  If you do not transfer the comments, you save storage space on your HMI device.

  If you transfer the comments, the script is more easily understood during testing in the debugger.

##### Operation using function keys

To symbolize the function of a function key for keyboard devices, you configure a graphic next to the function key in the display. Under "Screens &gt; Function keys &gt; User-defined pictogram size", you specify whether you want to use a graphic size that deviates from the standard size.

##### Operation with keyboard

Under "Keyboard &gt; General &gt; Use screen keyboard", you specify whether the screen keyboard is available on your HMI device.

Under "Keyboard &gt; General &gt; Release button on exit", you specify whether the "Release" event is triggered when the user exits a button without releasing it.

Under "Keyboard &gt; Disable function keys in dialogs", you specify for keyboard HMI devices whether the function keys are disabled for the duration of the displayed dialog. Large dialogs can hide explanatory areas or graphics at function keys or that border function keys. Functions keys can be unintentionally pressed due to this.

#### Compatibility check with the controller

##### Introduction

The "Project ID" area pointer is used to configure the project ID for checking the consistency of the project with the PLC. The area pointer reads the project version from the PLC. You can find additional information in the online help for WinCC under "Communicating with controllers".

##### Compatibility check with the controller

You select the project ID in the Runtime settings of the HMI device under "General &gt; Identification &gt; Project ID".

At startup, Runtime checks whether the project ID of the project matches the PLC project version. Runtime will only start if the two values match.

An area pointer "Project ID" is created for connections whose address you specify in the PLC. The value that you store at this address will become the project ID.

The project ID is not available on all HMI devices.

#### Password protection in runtime (Basic Panels)

This section contains information on the following topics:

- [Password protection in runtime: Basics (Basic Panels)](#password-protection-in-runtime-basics-basic-panels)
- [Configuring a password for transport (Basic Panels)](#configuring-a-password-for-transport-basic-panels)
- [Resetting the password for transport (Basic Panels)](#resetting-the-password-for-transport-basic-panels)

##### Password protection in runtime: Basics (Basic Panels)

###### Overview

The connection establishment can be protected with passwords in the TIA Portal. The configured passwords are saved in encrypted form. During transfer to the target system, the passwords are also protected against unauthorized access and cannot be read. These passwords are decrypted securely on the HMI devices in Runtime.

Password protection can be created for the following connections:

- SIMATIC S7-1200
- SIMATIC S7-1500
- SIMATIC S7-1500 software controller (WinAC)
- PC Station 2.0 (station manager)

> **Note**
>
> The passwords become invalid at a change to an older version.

###### Downloading certificates

The certificate for decrypting the passwords is saved in the certificate store of the HMI device. A system alarm is output if the certificate is not available.

You can restore the certificate by downloading the configuration again.

---

**See also**

[Configuring a password for transport (Basic Panels)](#configuring-a-password-for-transport-basic-panels)
  
[Resetting the password for transport (Basic Panels)](#resetting-the-password-for-transport-basic-panels)

##### Configuring a password for transport (Basic Panels)

###### Introduction

To protect the private password key during transport, you can configure a password for transport under "Runtime settings".

###### Creating password

1. Open the "Runtime settings &gt; General" editor in the Project window.
2. Enter the password in the "Enter password" field in the "Transport password" area.
3. Confirm the password in the "Confirm password" field.

> **Note**
>
> If there was no previous password, the "Old password" field is disabled.

###### Result

You have now configured the password for transport. If a password for transport has been configured and you transfer the project to the HMI device, a dialog with a password prompt will appear once in runtime.

If the password entered is correct, the certificate is saved in the certificate store of the HMI device.

When you change the password, load the project with the changed password into the HMI device and start Runtime. No password prompt appears.

---

**See also**

[Password protection in runtime: Basics (Basic Panels)](#password-protection-in-runtime-basics-basic-panels)
  
[Resetting the password for transport (Basic Panels)](#resetting-the-password-for-transport-basic-panels)

##### Resetting the password for transport (Basic Panels)

###### Introduction

If you have moved the transport password, for example, you can create a new security certificate. To do so, reset the transport password.

###### Reset password

1. Click the "Reset password" button.

   The password is reset. A new certificate without a password is generated.
2. Enter the new password and confirm it in the "Confirm password" field.

**Note**

Other passwords, for example the password for the PLC, will become invalid. The next time you compile, an error message will appear telling you that these passwords are no longer valid.

**Note**

The certificate is not password-protected until you enter a new password for transport.

After download of the project to the HMI device, you will be prompted for the password.

---

**See also**

[Password protection in runtime: Basics (Basic Panels)](#password-protection-in-runtime-basics-basic-panels)
  
[Configuring a password for transport (Basic Panels)](#configuring-a-password-for-transport-basic-panels)

### Overview of compiling and loading projects

#### Overview

The project is compiled in the background even as you are configuring it in WinCC. This reduces the time for final compilation. When you start compilation, you create a file that can be run on the corresponding HMI device.

If an error occurs during compilation, WinCC provides support in locating and correcting it.

Once you have corrected any problems, you download the compiled project to the HMI devices on which the project is to run. If the configuration PC is not connected to the HMI device, save the compiled project on a data medium of your choice. The compiled project is then transferred from a PC connected to the HMI device to the HMI device.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile all modified S7 blocks with the command "Compile &gt; Software" in the shortcut menu before you compile the HMI device.

#### Project

The term "project" has two different meanings in the contexts of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of an HMI device

The figure below illustrates the link between WinCC projects and Runtime projects using the example of the "Compile and load" process:

![Project](images/46298521483_DV_resource.Stream@PNG-en-US.png)

#### Runtime

Runtime is the software for process visualization. In Runtime, you execute the project in process mode.

A distinction is made between two types of Runtime:

1. Runtime on a panel

   Before running a Runtime project on a panel, you have to transfer the Runtime project to the panel before startup.
2. Runtime on a PC

   You can execute the Runtime project directly on the configuration PC if Runtime has been installed on the configuration PC.

   If you want to execute the Runtime project on a different PC, you have to transfer the Runtime project to the PC before startup.

#### Runtime version

The Runtime version depends on the image of the configured HMI device. The Runtime version of the compiled project is displayed under "Info" in the Inspector window.

#### Simulation

You test your configuration with a simulation. You can start a simulation without a link to the active process.

In a simulation, you test configured tags or screen changes, for example. During the simulation, the configured tags can be manipulated, activated and deactivated with the help of the tag simulator.

There are two types of simulation:

1. Simulating a panel

   If you created a panel in your project, the panel is displayed in the simulation. With the help of this type of simulation, you can test your configuration on the HMI device without transferring the project to the panel.
2. Simulating Runtime

   Simulating Runtime allows you to test the project directly on the configuration PC.

### Compiling a project (Basic Panels)

#### Introduction

The changes made to the project are compiled in the background even as you are configuring a project in WinCC. Projects are compiled automatically when you load them. This ensures that the latest version of the project is loaded at all times.

WinCC checks consistency of the project during compilation. The error locations in the project are listed in the Inspector window. You can jump directly to the source of the error from the entry in the Inspector window. Check and correct errors found.

#### Scope of the compilation

Configuration data is compiled in the background as soon as you start configuring an HMI device. If you compile a project manually, only the changes in the configuration made since the last compilation process are compiled in the background.

You can start complete project compilation manually at any time; this may, for example, be done to test the consistency of the configured data.

#### Requirement

- A project is open.

#### Procedure

Proceed as follows to compile a project:

1. If you want to compile several HMI devices at the same time, select all the relevant HMI devices with multiple selection in the project tree.
2. Compile the project:

   - To only compile changes in the project, select the "Compile &gt; Software (only changes)" command from the shortcut menu of the HMI device.
   - To compile all project data, select the "Compile &gt; Software (compile all)" command from the shortcut menu.

#### Result

The configuration data of all selected HMI devices is compiled. Any errors that occur during compilation are shown in the Inspector window.

### Simulating projects (Basic Panels)

This section contains information on the following topics:

- [Simulation basics (Basic Panels)](#simulation-basics-basic-panels)
- [Simulating a project](#simulating-a-project)
- [Working with the tag simulator (Basic Panels)](#working-with-the-tag-simulator-basic-panels)
- [Simulation restrictions (Basic Panels)](#simulation-restrictions-basic-panels)

#### Simulation basics (Basic Panels)

##### Introduction

You can use the simulator to test the performance of your configuration on the configuration PC. This allows you to quickly locate any logical configuration errors before productive operation.

You can start the simulator as follows:

- In the shortcut menu of the HMI device, or in a screen: "Start simulation"
- Menu command "Online &gt; Simulation &gt; [Start|With tag simulator|With script debugger]"
- Under "Visualization &gt; Simulate device" in the portal view.

##### Requirements

The simulation/runtime component is installed on the configuration PC.

##### Field of application

Use the simulator to test various functions of the operator control and monitoring system, such as:

- Checking limit levels and alarm outputs
- Consistency of interrupts
- Configured interrupt simulation
- Configured warnings
- Configured error messages
- Check of status displays
- Interconnection and screen layout

---

**See also**

[Simulating a project](#simulating-a-project)

#### Simulating a project

##### Introduction

You simulate your project with one of the following two methods:

- Without a connected PLC

  You change the value of area pointers and tags in a tag simulator that is read for the simulation of WinCC Runtime.
- With a connected PLC without a running process

  You simulate your project by running it directly in Runtime. The tags and area pointers become active. This allows you to create an authentic simulation of your configured HMI device in Runtime.

  > **Note**
  >
  > **Simulation restrictions**
  >
  > You cannot simulate the following system functions:
  >
  > - CalibrateTouchScreen
  >
  > You cannot simulate the Media Player. A static screen appears in the simulation window instead of the Media Player.
  >
  > File access via scripts is not possible for HMI devices with Windows CE.

##### Requirement

- Simulation without a connected PLC: Tags have been created
- Simulation with a connected PLC but no active process: A project with tags and area pointers has been created

##### Procedure

To simulate a project using the tag simulator, follow these steps:

1. Open the project on the configuration PC.
2. Select the "Online &gt; Simulation &gt; With tag simulator" menu command.

   For initial project simulation, the simulator is started with a new, empty table. The project is opened simultaneously in Runtime.

   Toggle between the tag simulator and Runtime using the &lt;Alt +Tab&gt; key combination.
3. To simulate a process value, select the corresponding "tag" from the tag simulator.

   The table lists all configured tags. You can simulate up to 300 tags simultaneously.
4. Select the simulation mode in the "Simulation" column.
5. Change the value of tags and area pointers in the respective columns.
6. Activate the "Start" check box to start the simulation for this tag.
7. To save the simulation, select the menu command "File &gt; Save" and enter a descriptive name, for example, "Mixing".

   The file name is assigned the extension "*.cors".

##### Result

The process values are simulated in Runtime. The tag values are created at random, or incremented, depending on the simulation mode.

To specify tag values, change the simulation mode to "&lt;Display&gt;" and enter a value at "Set value".

The following figure shows a tag simulator with four tags whose values can be determined at random in a range of values from 10 to 1000:

![Result](images/23309309707_DV_resource.Stream@PNG-en-US.png)

##### Managing simulation data

If you have saved data from a previous simulation, you can open the file at a later point in time and simulate your project again. The tags and area pointers listed in the tag simulator must still be available in the project.

Proceed as follows to open a simulation file:

1. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".
2. Select the menu command "File &gt; Open" in the tag simulator.
3. Select the corresponding simulation file and click "Open".

   The simulator loads the stored data.

##### Enabling and disabling tags

Start and stop the simulation for each tag separately in order to facilitate the transition from offline to online engineering. Activate "Start" in the corresponding row.

If a tag is activated, the simulation values are calculated and transferred to the WinCC simulator.

##### Deleting a tag

To delete a tag from the tag simulator, follow these steps:

1. Select the cell that contains the tag name.
2. Select the "Edit &gt; Cut" menu command.

   The tag is removed from the table.

---

**See also**

[Simulation basics (Basic Panels)](#simulation-basics-basic-panels)
  
[Working with the tag simulator (Basic Panels)](#working-with-the-tag-simulator-basic-panels)

#### Working with the tag simulator (Basic Panels)

##### About the tag simulator

The tag simulator has the following columns:

| Column | Description |
| --- | --- |
| Tag | Specifies the tags for the simulation. |
| Data type | Shows the data type of the selected tag. |
| Current value | Shows the simulated value of the defined tags. |
| Format | Specifies the selected format in which the tag values are simulated:   - Decimal (1, 2, 3, 4, ...) - Hexadecimal (03CE, 01F3, ...) - Binary (0 and 1) |
| Write cycle | Specifies the selected time interval at which the current tag values are simulated. If you enter "2", for example, the current value of the tag will be shown every 2 seconds. |
| Simulation | Shows the method by which the tag values are processed during simulation. |
| Set value | Sets the selected value for the respective tag. The simulation start with the specified value. |
| minValue   maxValue | Specifies the value range of the tag. You set a minimum and maximum value for this range. The default values are -32768 for the minimum and 32767 for the maximum. |
| Period | Contains the period during which the value of the tag is repeated for the "Increment" and "Decrement" simulation modes. |
| Start | Starts simulation of the tag based on the previously entered information. |

##### Simulation modes

The simulator has six different simulation modes. The configured tags are supplied with nearly realistic values during the simulation.

| Simulation mode | Description |
| --- | --- |
| Sinusoidal | Changes the tag value to form a sinusoidal curve. The value is visualized as a periodic, non-linear function. |
| Random | Provides randomly generated values. The tag value is changed by means of a random function. |
| Increment | Increases the value of the tag continuously up to a specified maximum value. Begins again at the minimum after the maximum has been reached. The value trend corresponds to a positive saw-tooth curve. |
| Decrement | Reduces the value of the tag continuously down to a specified minimum value. Begins again at the maximum after the minimum has been reached. The value curve corresponds to a negative saw-tooth curve. |
| Shift bit | Shifts a set bit continuously by one position. The previous position is always reset. This lets you test the alarms of an HMI device, for example. |
| &lt;Display&gt; | The current tag value is displayed statically. |

##### Example: Simulate tags with the "Shift bit" simulation mode

Proceed as follows to simulate tags with the "Shift bit" simulation mode:

1. Open the project you want to simulate.
2. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".

   The tag simulator opens.
3. In the "Tag" column, select a tag from your project.
4. Select "Bin" in the "Format" column.
5. Enter the value "1" in the "Write cycle" column.
6. Select the "Shift bit" simulation mode in the "Simulation" column.
7. Enter the value "1" in the "Set value" column.
8. Enable the tag with the "Start" check box.

##### Result

The simulator tests the selected tag bit-by-bit as follows:

| Simulation values | Byte for alarms |
| --- | --- |
| Set start value | 00000001 |
| 1. Simulation value | 00000010 |
| 2. Simulation value | 00000100 |
| 3. Simulation value | 00001000 |
| .... | ... |

In Runtime you see if the desired alarm is output at a given value.

#### Simulation restrictions (Basic Panels)

##### Connection

The connection to PLCSim is only possible via an integrated connection.

##### Alarms with dynamic parameters

If you use tags or text lists as external tags for alarms, the dynamic parameters of the alarms are not displayed.

Only internal tags are enabled for the simulation of alarms in the tag simulator .

Use PLCSim to simulate dynamic parameters.

##### Panels

If you want to use PLCSim with version V14 or higher for simulation with a panel, the device version of the panel must be 14.0.0.0 or higher.

### Loading projects (Basic Panels)

This section contains information on the following topics:

- [Overview for loading of projects (Basic Panels)](#overview-for-loading-of-projects-basic-panels)
- [Loading a project (Basic Panels)](#loading-a-project-basic-panels)
- [Loading project from external storage medium (Basic Panels)](#loading-project-from-external-storage-medium-basic-panels)

#### Overview for loading of projects (Basic Panels)

##### Overview

Delta data of the project is automatically compiled before you download it to one or several HMI devices. This always ensures that the latest version of the project is transferred.

##### Loading a project to an HMI device

The following steps are completed prior to downloading:

1. The download settings are verified. The "Extended download to device" dialog box is opened automatically during the initial download of a project to an HMI device. You use this dialog to define the protocol and interface or destination path for the project in accordance with the HMI device Runtime used.

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens.
2. The project is compiled. Warnings and errors during compilation are displayed in the Inspector window and in the "Load preview" dialog box.
3. The "Load preview" dialog box shows you the following information for each HMI device:

   - The individual steps for loading
   - If the image of the target HMI device does not match the image from the configuration, a prompt is displayed asking whether you want to now change the image.

     | Symbol | Meaning |
     | --- | --- |
     |  | **Notice** |
     | **Changing the image deletes all data from the HMI device.**  Data is deleted on the target system if you change the image. For this reason, first back up the following data, if necessary: - User administration - Recipes |  |
   - Presettings that take effect at loading. You can change the default settings for this download process, if necessary.
   - Occurring warnings (optional).

     You can download a project while ignoring the "warnings". The functionality may be restricted in runtime.
   - Occurring errors (optional).

     You cannot load the project.

     WinCC will open the invalid configuration in the corresponding editor if you double-click the error message in the Inspector window. Correct the errors and reload the project.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile the user program before you compile the HMI device.

##### Loading with S7 routing

Configure the S7 routing settings in the "Devices &amp; Networks" editor in the relevant controller. The settings depend on the device configured.

S7 routing supports the following protocols:

- MPI/PROFIBUS
- Ethernet

##### Loading a project without a connected HMI device

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to an external storage medium, such as a USB stick, and then load it onto the HMI device.

This function is available in connection with an HMI device image which is compatible with TIA Portal version V14 or higher.

Generate the required project data in WinCC by configuring the HMI device and then dragging the HMI device folder (such as "HMI_1 [&lt;Device type&gt;]") to an external storage medium under "Card Reader/USB memory".

##### Transferring Runtime add-ons

Projects can contain Runtime add-ons in the form of controls or CSP (Communication Support Packages). These Runtime add-ons are automatically transferred with the project.

---

**See also**

[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Loading a project (Basic Panels)

##### Introduction

Before a project can run on an HMI device, you must first load it to the HMI device. During loading, you must most importantly specify whether existing data on the HMI device such as "user administration" and "recipe data" is to be overwritten.

If the HMI device supports PROFINET, the name of the HMI device entered in the project tree is used as the device name for the PROFINET communication. The name is written to the HMI device during download. If a device name for the PROFINET communication has already been entered in the HMI device, it will be overwritten.

As a general rule, only one project can be active in Runtime on an HMI device. An HMI device is generally configured to exit Runtime automatically when loading is started. If this is not the case, you will have to exit Runtime manually on the HMI device.

If the image of the target HMI device does not match the image from the configuration, a prompt is displayed asking whether you want to now change the image.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the image deletes all data from the HMI device.**  Data is deleted on the target system if you change the image. For this reason, first back up the following data, if necessary:  - User administration - Recipes |  |

##### Controlling the transfer behavior on the HMI device

As a general rule, only one project can be active in Runtime on an HMI device. An HMI device is generally configured to exit Runtime automatically when loading is started. If this is not the case, you will have to exit Runtime manually on the HMI device.

You define how the HMI device reacts when the project is loaded in the "Start Center" under "Settings" on the HMI device:

| Transfer mode | Effect |
| --- | --- |
| Off | The project cannot be loaded to the HMI device. |
| Manually | The project can only be loaded to the HMI device if the following requirements are met:  - Runtime is not running - The HMI device is in "Transfer" mode. |
| Automatic | The project can always be loaded to the HMI device.   If a transfer is started on the configuration PC and a project is in runtime on the HMI device, the running project is automatically closed.   For Mobile Panels, this transfer mode is disabled for security reasons. |

> **Note**
>
> **Closing Runtime automatically**
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the "Start Center".

Please refer to the documentation for the HMI device used for more detailed information on transfer settings.

##### Requirement

- You have created an HMI device in the project.
- The HMI device is connected to the configuration PC.
- The "Start Center" has been started on the HMI device.
- The protocol by which the project is loaded is set on the HMI device in the "Start Center" under "Settings".
- Transfer mode is set as "Automatically" or "Manually" in the HMI device.

##### Procedure

Proceed as follows to load a project:

1. To download a project simultaneously to several HMI devices, select the HMI devices by means of multiple selection in the project tree.
2. Select the "Download to device &gt; Software" command from the shortcut menu of an HMI device.
3. If the "Extended download to device" dialog is open, configure the "Settings for loading". Make sure that the "Settings for loading" correspond to the "Transfer settings in the HMI device".

   - Select the protocol used, for example, Ethernet or HTTP.
   - Configure the relevant interface parameters on the configuration PC.
   - Make any interface-specific or protocol-specific settings required in the HMI device.
   - Click "Load".

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens. The project is compiled at the same time. The result is displayed in the "Load preview" dialog box.
4. Check the displayed presettings and change them as necessary.
5. Click "Load".

##### Result

The project is loaded to all selected HMI devices. Any existing project is replaced. The data for user administration and / or recipes is replaced in accordance with the settings in the "Load preview" dialog box.

During the download, you can keep track of the files that are transferred.

If errors or warnings occur during the download, corresponding alarms are displayed under "Info &gt; Load" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device.

> **Note**
>
> If the transfer is interrupted, WinCC automatically ensures that no data is lost and that existing data is deleted on the HMI device only after complete transmission.

---

**See also**

[Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backing-up-and-restoring-data-of-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Error messages during loading of projects (Panels, Comfort Panels, RT Advanced)](#error-messages-during-loading-of-projects-panels-comfort-panels-rt-advanced)
  
[Adapting the project for another HMI device (Basic Panels)](#adapting-the-project-for-another-hmi-device-basic-panels)
  
[Establishing a connection to the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#establishing-a-connection-to-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Loading project from external storage medium (Basic Panels)

##### Introduction

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to an external storage medium, such as a USB stick, and load it from the USB stick onto the HMI device.

This function is available in connection with a HMI device image that is compatible with TIA Portal version V14 or higher.

This function is available for Basic Panels 2nd Generation.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss**  If you load a project with the option "Upgrade or downgrade Firmware", the operating system of the HMI device is updated. Existing data on the HMI device including the HMI device password is deleted. Settings in the Start Center are retained, license keys are stored on the external storage medium before the operating system is updated.  If required, back up the data before loading. |  |

You create the required project data in WinCC by configuring the HMI device and then dragging and dropping or copying and pasting the folder of the HMI device (e.g. "HMI_1 [&lt;device type&gt;]") to an external storage medium under "Card Reader/USB memory".

##### Requirements

- You have started the Start Center on the HMI device.
- The storage medium with the saved project is inserted in the HMI device.

##### Procedure

1. Click "Settings".
2. Open the "Service &amp; Commissioning" dialog.
3. Confirm with the "Project Download" button.

   With "Project Download", you have the option of downloading a single project from an external storage medium to the HMI device.
4. Select the storage medium on which the project data is saved.
5. Select the project file.
6. Select the options for loading the project:

   - "User administration:"  
     Overwrite user administration on the HMI device with the user administration of the project
   - "Recipe data:"  
     Overwrite HMI device recipes with project recipes
   - "Upgrade or downgrade Firmware:"  
     Update firmware on the HMI device if the firmware version of the HMI device is not incompatible with the firmware version of the project
7. Confirm with the "Accept" button.

**Note**

If no storage medium is inserted in the HMI device, the "Projects" list is empty.

**Note**

You can only change the settings for overwriting the user management or recipes if they were not previously interlocked in the configuration.

##### Result

After the loading process, the new project is started on the HMI device.

### Compiling and loading with Multiuser Engineering (Basic Panels)

This section contains information on the following topics:

- [Compiling and loading with multiuser engineering (overview) (Basic Panels)](#compiling-and-loading-with-multiuser-engineering-overview-basic-panels)
- [Compiling in the server project view (Basic Panels)](#compiling-in-the-server-project-view-basic-panels)
- [Compiling in the local session (Basic Panels)](#compiling-in-the-local-session-basic-panels)

#### Compiling and loading with multiuser engineering (overview) (Basic Panels)

##### Introduction

When using multiuser engineering for your projects, you should take into account the response when compiling the Runtime projects and the response when downloading them to HMI devices.

You can compile and download to an HMI device in both the server project view and in the local session.

You can find more information about the topic of "multiuser engineering" under "Using Multiuser Engineering".

##### Basics

For HMI devices and RT Advanced, the following scenarios are possible in multiuser engineering:

- Compiling in the server project view
- Compiling in the local session
- Loading from the server project view
- Loading from the local session

> **Note**
>
> Complete download from the server project view or local session is no different to complete download in a single-user project. With a complete download, the current Runtime project is loaded from the currently active view to an HMI device.

> **Note**
>
> Compiling and downloading in a local session is no different from compiling and downloading in a single-user project.

In principle, you can execute all commands for compiling and loading in multiuser engineering projects:

- "Software (rebuild all)"
- "Compile &gt; Software (only changes)"
- Software (all)

**The term "project"**

The term "project" has two different meanings in the contexts of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of one HMI device

##### Rules

The following basic rules apply to compiling and downloading in multiuser engineering:

- The Runtime project that has been compiled in a local session always remains local and is not uploaded to the multiuser server. It cannot be saved in the multiuser server project.
- Only Runtime projects compiled in the server project view can be saved in the multiuser server project.

You can find additional information on Multiuser Engineering on the Siemens YouTube channel: [Multiuser Engineering - one team working simultaneously on a project](https://www.youtube.com/watch?v=n4oTZ2Gzg6U).

---

**See also**

[Compiling in the server project view (Basic Panels)](#compiling-in-the-server-project-view-basic-panels)
  
[Compiling in the local session (Basic Panels)](#compiling-in-the-local-session-basic-panels)

#### Compiling in the server project view (Basic Panels)

##### Basics

Compiling and downloading in the server project view is no different from compiling and downloading in a single-user project.

During the compiling of a project in the server project view, the multiuser server project is blocked. Other users cannot make changes to this server project during this time. The Runtime project compiled in the server project view is stored along with the engineering project in the central multiuser server. Blocking the multiuser server project ensures that the configuration data and the Runtime project remain in sync.

> **Note**
>
> When you compile and save in the server project view, other users obtain the Runtime project you have updated along with the engineering project when they "refresh" their local session. Other users do not have to recompile the changes you have made after an update.

##### Example: **Compiling during check-in**

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

If there are no compilation errors, both projects - the modified engineering project (with the modified tags) and the compiled Runtime project - are saved in the central multiuser server project with the "Save changes" command.

If you skip compiling during the check-in, the project contains the changes that have been saved on the server.

The next user who creates a local session from the server project or updates an existing local session must compile your two changes in addition to his or her own changes.

> **Note**
>
> Working on a shared project through multiple local sessions increases the probability of error. It is therefore recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors.

---

**See also**

[Compiling and loading with multiuser engineering (overview) (Basic Panels)](#compiling-and-loading-with-multiuser-engineering-overview-basic-panels)
  
[Compiling in the local session (Basic Panels)](#compiling-in-the-local-session-basic-panels)

#### Compiling in the local session (Basic Panels)

##### **Basics**

Compiling and downloading projects in the local session is no different from compiling and downloading in a single-user project.

Since the local session is a copy of the server project, the first compilation status of the local session is identical to that of the server project. If the server project contains contents that are not compiled or error messages occurred during the compiling, they are transferred to the local session.

> **Note**
>
> It is recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors and avoid spreading errors.

##### **Updating in the** **local session**

If you update a project in the local session, the local session - including the compilation status - is completely replaced by the content of the server project. Only the changes marked for check-in are retained in the updated local session and generate additional compiling steps in the local session.

##### Example: Updating the local session

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

You update the content of the local session by clicking the "Update" button. After the update, the local session obtains the compilation status of the server project. There are also compiling tasks for the acquisition of the modified tags.

---

**See also**

[Compiling and loading with multiuser engineering (overview) (Basic Panels)](#compiling-and-loading-with-multiuser-engineering-overview-basic-panels)
  
[Compiling in the server project view (Basic Panels)](#compiling-in-the-server-project-view-basic-panels)

### Starting Runtime (Basic Panels)

This section contains information on the following topics:

- [Starting Runtime on the HMI device (Basic Panels)](#starting-runtime-on-the-hmi-device-basic-panels)

#### Starting Runtime on the HMI device (Basic Panels)

##### Introduction

On completion of the project download to the HMI device, you can start the project in Runtime. The project is saved in the HMI device to a file with the following extension:

- Basic Panels: "*.srt"

The project settings defined in the "Runtime settings" of the HMI device are activated when the project is started in Runtime.

The programs that you can use to start projects on the HMI device are available in the Runtime installation folder.

> **Note**
>
> **Closing Runtime automatically**
>
> If automatic transfer is activated on the HMI device and a transfer is started on the configuration PC, the running project is automatically terminated.
>
> The HMI device then automatically switches to "Transfer" operating mode.
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the "Start Center".

##### Requirements

- WinCC Runtime is installed on the HMI device.
- The project was downloaded to the HMI device.
- The "Start Center" has been started.

##### Procedure

The project is stored on a panel in a folder you specify in the HMI device transfer settings. The "Start Center" application is started on a panel. The project loaded is started automatically after expiration of the configured delay.

If the project does not start automatically:

1. Click on "Start" in the "Start Center" to start the loaded project.

Refer to the documentation for the HMI device for additional information on startup of projects.

### Error messages during loading of projects (Basic) (Basic Panels)

#### Possible problems during the download

When a project is being downloaded to the HMI device, status messages regarding the download progress are displayed in the output window.

Usually, problems arising during the download of the project to the HMI device are caused by one of the following errors:

- Incorrect download settings on the HMI device
- Incorrect HMI device type in the project
- The HMI device is not connected to the configuration PC.

The most common download failures and possible causes and remedies are listed below.

#### The serial download is cancelled

Possible remedy: Select a lower baud rate.

#### The download is cancelled due to a compatibility conflict

| Possible cause | Remedy |
| --- | --- |
| The configuration PC is connected to the wrong device, e.g. a controller. | Check the cabling.   Correct the communication parameters. |

#### Project download fails

| Possible cause | Remedy |
| --- | --- |
| Connection to the HMI device cannot be established (alarm in the output window) | Check the physical connection between the configuration PC and the HMI device.   Check whether the HMI device is in transfer mode. Exception: Remote control |
| The default communication driver is not listed in the Windows Device Manager. | Check the device status of the COM connection in the properties window of the Device Manager. |

#### Download over MPI/DP interface fails

| Possible cause | Remedy |
| --- | --- |
| "Configured mode" is set on the CP, for example, if you are using the SIMATIC NET CD. | Set the CP to "PG mode" using the "Set PC station" application.  Check the "baud rate" and "MPI address" network parameters.  Download the project from WinCC to the CP.  Set the CP back to "configured mode". |
| On the programming device/PC panel, the "S7ONLINE" access point is not set to a hardware device such as CP5611 (MPI). The cause may be the installation of "SIMATIC NET CD 7/2001". | Set the access point "S7ONLINE" on the selected device using the "PG/PC Panel" or "Set PC station" application.  Check the "baud rate" and "MPI address" network parameters.  Download the project from WinCC to the HMI device.  Restore the "S7ONLINE" access point to the original device. |

#### The configuration is too complex

| Possible cause | Remedy |
| --- | --- |
| The configuration contains too many different objects or options for the HMI device selected. | Remove all objects of a type, e.g. all graphic views. |

### Adapting the project for another HMI device (Basic Panels)

#### Introduction

When you download a WinCC project to an HMI device, WinCC checks whether this is compatible with the HMI device type used in the project. If the types of HMI device do not match, you will see a message before the download starts.

The download is aborted.

#### Adapting the project for the HMI device

You need to adapt the project accordingly to be able to download the project to the connected HMI device.

- Add a new HMI device in the project tree. Select the correct type of HMI device from the HMI device selection.
- Copy the configured components from the previous to the new HMI device.

  Copy large amounts of components directly in the project navigation and details view.

  For example, copy the "Screens" folder to the screens folder of the new HMI device with the help of the shortcut menu.
- Use the detail view to copy entries in the project tree for which the "Copy" command is not available in the shortcut menu.
- Select the "Recipes" entry in the project tree, for example. The recipes are displayed in the detail view.
- Select the recipes in the detail view and drag them to the "Recipes" entry of the new HMI device. The recipes are copied. You can also select multiple objects in the detail view.
- Configure the components that cannot be copied, e.g. connections, area pointers, and alarms.
- Save the project at various points in time.
- Compile the full project.
- When the compilation is successfully completed, download the project to the HMI device.

#### Linking references

References to linked objects are included in the copying. The references are linked again once the linked objects are copied.

Example:

You copy a screen in which objects are linked to tags. The tag names are entered at the individual objects after the screen is added to the new HMI device. The tag names are marked in red because the references are open. When you then copy the tags and insert them into the new HMI device, the open references are closed. The red marking for the tag names disappears.

For complete references to connected objects in the PLC, you first need to configure a connection to the PLC.

#### Using the information area

When you compile the project for the HMI device, errors and warnings are displayed in the "Info" tab of the Inspector window. You can use the shortcut menu command "Go to" to go directly to the location where the error or warning can be corrected.

Work through the list of errors and warnings from top to bottom.

When the compilation is successfully completed, download the project to the HMI device.

### Reducing the project size (Basic Panels)

#### Introduction

When loading a large-scale project to an HMI device, the memory of the HMI device may be insufficient for the project. There are several ways to reduce the size of your project.

#### Options for reducing the project size

There are several ways to reduce the size of the project and save space:

- Reduce the number of available Runtime languages

  Check whether all selected Runtime languages are actually needed. You can disable the languages that you do not need under "Runtime settings &gt; Language &amp; Font &gt; Runtime language and font selection".
- Do not use help texts for S7 diagnostic alarms

  To reduce the size of the project, you can disable the download of help texts for the S7 diagnostic alarms. In order to avoid downloading the help texts to the HMI device, disable the option "Download S7 diagnostics help texts" under "Runtime settings &gt; Alarms &gt; General".
- Rebuild all software

  In order to optimize the project data and to clean up obsolete changes, compile the entire project using the "Compile &gt; Software (rebuild all)" command from the shortcut menu of the HMI device.
- Harmonize the presentation using styles (as of WinCC V13)

  It is recommended to harmonize screen objects using styles. Standardize the appearance of screen objects in a project to optimize project data. Use the specified preset or customized style for the configuration of the screen objects throughout the project.
- Enable automatic update of PLC alarms (for S7-1500 controllers and V14 HMI devices)

  To save space, you can specify that the PLC alarm texts are only to be loaded in Runtime when needed. To do this, enable the "Automatic update" option under "Runtime settings &gt; Alarms &gt; Controller alarms". Make sure that automatic update of alarms is also enabled in the corresponding controller.

  The "Automatic update" option is not available on Basic Panels.

  The amount of space that can be saved depends on the number of PLC alarms and the number of Runtime languages.
- Reduce the number of fonts loaded

  Check whether the number of downloaded user-defined fonts can be reduced. If necessary, configure only the standard fonts for the required Runtime languages under "Runtime settings &gt; Language &amp; font &gt; Runtime language and font selection".

  To save space, use fewer font groups for the configuration.
- Reduce the size of the graphics

  Check the size of the graphics that you use in the project. If necessary, reduce the size of the graphics by reducing the resolution or choose a higher compression format without noticeable loss of quality for the project graphics.

  To keep the project size small for Basic HMI devices, harmonize the sizes of graphics used in the project.

  Select appropriate graphic formats for your screens: For example, use PNG images for drawings that are not vector graphics and JPEG images for photos.

### Basics of operating in Runtime (Basic Panels)

This section contains information on the following topics:

- [Overview (Basic Panels)](#overview-basic-panels)
- [Operation with the touch screen (Basic Panels)](#operation-with-the-touch-screen-basic-panels)
- [Operation with keys (Basic Panels)](#operation-with-keys-basic-panels)
- [Navigating in the display (BS) (Basic Panels)](#navigating-in-the-display-bs-basic-panels)
- [Triggering an action (Basic Panels)](#triggering-an-action-basic-panels)
- [Entering a value (Basic Panels)](#entering-a-value-basic-panels)
- [Moving operator controls (Basic Panels)](#moving-operator-controls-basic-panels)
- [Displaying infotext (Basic Panels)](#displaying-infotext-basic-panels)
- [Changing Runtime language (Basic Panels)](#changing-runtime-language-basic-panels)

#### Overview (Basic Panels)

##### Overview of operator control of a project

Depending on the HMI device, the following options are available for the input with Basic HMI devices.

- Touch screen
- Function keys
- Mouse and keyboard

Use the touch screen and function keys or mouse and keyboard to operate the Control Panel / Start Center or the project running on your HMI device.

> **Note**
>
> **Incorrect operation**
>
> A project can contain certain operations that require in-depth knowledge about the specific plant on the part of the operator.  
> Make sure that your plant is only operated by qualified personnel.

##### Operating options for an HMI device

Depending on your HMI device, operate your plant as follows:

- Touch screen operation

  The display of the device is touch-sensitive. You operate the operating elements in the display with your finger or a stylus.
- Operation with control keys and function keys

  Control keys and function keys are integrated into the housing of the device.

  - Control keys have a specified function, for example, navigation or the acknowledgment of alarms.
  - Function keys are freely user-assignable and their function is therefore project-specific.
- Mouse and keyboard operation

  Mouse and keyboard are connected via an integrated USB port. You operate the operating objects with mouse and keyboard.

##### Individually configured operation

The configuration engineer has various options available for setting up operation.

Examples of actions whose execution is always determined on a project-specific basis:

- Screen change
- Reporting
- Changing Runtime language

There are no specific operating elements to execute certain functions. The configuration engineer specifies the project-specific execution. A screen change can be triggered with a button or a function key, for example.

Information on project-specific operations can be found in the system documentation.

#### Operation with the touch screen (Basic Panels)

This section contains information on the following topics:

- [Overview of operation with the touch screen (Basic Panels)](#overview-of-operation-with-the-touch-screen-basic-panels)
- [Screen keyboard (Basic Panels)](#screen-keyboard-basic-panels)
- [Screen keyboard for Basic Panels 2nd Generation (Basic Panels)](#screen-keyboard-for-basic-panels-2nd-generation-basic-panels)

##### Overview of operation with the touch screen (Basic Panels)

Use the touch screen to operate the HMI device of the project that is running on your HMI device.

###### Operating the touch screen

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to the touch screen**  Do not touch the touch screen with sharp or pointed objects.   Avoid tapping the touch screen with hard objects, and avoid constantly using motion control.   Both can significantly reduce the useful life or even cause the failure of the touch screen.  **Triggering unintended actions**  You can trigger unintended actions if you touch several operating elements at the same time. Always touch only one operating element on the screen.  Operating elements are touch-sensitive symbols on the screen of the HMI device. |  |

###### Special features of operation using the touch screen

Operation with the touch screen is characterized by the following special features:

- Enable

  To enable an operator control, touch the touch screen with your fingers or with a stylus. To generate a double-click, touch the operator control twice in rapid succession.
- Value input

  You enter numbers and letters on the touch screen with a screen keyboard.
- Careful operation

  If you touch multiple operator controls at the same time, you may trigger unintentional actions.

###### Value input using the screen keyboard

The screen keyboard is displayed as soon as you operate a screen object that requires an input. Depending on the HMI device and the configured operating element, the system displays different screen keyboards for entering numerical or alphanumerical values. The screen keyboard is hidden again when input is complete.

###### File browser (Windows 8 or higher)

You can only operate the file browser dialog with a mouse, keyboard or on-screen keyboard (without using the touch function) on a Windows 8 or higher PC with touch screen. Use the file browser dialog of the Windows operating system with the help of a script on a touch screen PC with Windows 8 or higher.

##### Screen keyboard (Basic Panels)

###### Layout

The figure below shows the basic layout of a screen keyboard on a TP1500 Basic.

| Symbol | Meaning |
| --- | --- |
| ![Layout](images/43205639947_DV_resource.Stream@PNG-de-DE.png) | ![Layout](images/43205619467_DV_resource.Stream@PNG-de-DE.png) |
| Numbers | Letters |

###### Operator controls

The following keys are available on the screen keyboard of all HMI devices:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/69852074123_DV_resource.Stream@PNG-de-DE.png) | Cursor left | Navigates to the left |
| ![Operator controls](images/69852078475_DV_resource.Stream@PNG-de-DE.png) | Cursor right | Navigates to the right |
| ![Operator controls](images/69852083339_DV_resource.Stream@PNG-de-DE.png) | Backspace | Deletes a character |
| ![Operator controls](images/69852305291_DV_resource.Stream@PNG-de-DE.png) | Escape | Cancels the input |
| ![Operator controls](images/69852309643_DV_resource.Stream@PNG-de-DE.png) | Enter | Confirms the input |
| ![Operator controls](images/69891602315_DV_resource.Stream@PNG-de-DE.png) | Help | Displays the infotext  This key is only displayed when an infotext has been configured for the operator control. |

##### Screen keyboard for Basic Panels 2nd Generation (Basic Panels)

###### Layout

The figure below shows the basic layout of a screen keyboard on a Basic Panel 2nd Generation.

| Symbol | Meaning |
| --- | --- |
| ![Layout](images/70914504715_DV_resource.Stream@PNG-de-DE.png) |  |
| **Numbers** |  |

| Symbol | Meaning |
| --- | --- |
| ![Layout](images/70914512395_DV_resource.Stream@PNG-de-DE.png) |  |
| **Letters** |  |

###### Operator controls

The following keys are available on the screen keyboard of all HMI devices:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/70914520075_DV_resource.Stream@PNG-de-DE.png) | Cursor left | Navigates to the left |
| ![Operator controls](images/70914527755_DV_resource.Stream@PNG-de-DE.png) | Cursor right | Navigates to the right |
| ![Operator controls](images/70914535435_DV_resource.Stream@PNG-de-DE.png) | Backspace | Deletes a character |
| ![Operator controls](images/70914543115_DV_resource.Stream@PNG-de-DE.png) | Escape | Cancels the input |
| ![Operator controls](images/70914550795_DV_resource.Stream@PNG-de-DE.png) | Enter | Confirms the input |
| ![Operator controls](images/70914558475_DV_resource.Stream@PNG-de-DE.png) | Help | Displays the infotext  This key is only displayed when an infotext has been configured for the operator control. |

#### Operation with keys (Basic Panels)

This section contains information on the following topics:

- [Overview of operation with keys (Basic Panels)](#overview-of-operation-with-keys-basic-panels)
- [Control keys and shortcuts (Basic Panels)](#control-keys-and-shortcuts-basic-panels)
- [Function Keys (Basic Panels)](#function-keys-basic-panels)

##### Overview of operation with keys (Basic Panels)

###### Introduction

Use the keys of the HMI device to operate the Control Panel / Start Center of your HMI device or the project that is running on your device. Depending on the device, control keys and function keys are available.

For more detailed information, refer to the operating instructions for your HMI device.

##### Control keys and shortcuts (Basic Panels)

###### Introduction

The following tables list the control keys available to operate the project.

> **Note**
>
> The availability of control keys is determined by the HMI device used.

You trigger functions on keyboard HMI devices either with a key or a shortcut. With shortcuts, you keep the first key pressed. Then you press the second key.

###### Navigating in the display

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) |  | Tabulator | Selects the next operating element in the tab sequence |
| ![Navigating in the display](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) | Tabulator | Selects the previous operating element in the tab sequence |
| ![Navigating in the display](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204938379_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43205122699_DV_resource.Stream@PNG-de-DE.png) |  | Cursor keys | Selects the next operating element to the left, to the right, above or below the current screen object  Navigating in the operating element |

###### Operation of operating elements

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) |  | ENTER key | - Controls buttons. - Applies and ends an entry - Opens a selection list - Toggles between character mode and standard mode within an input field   A single character is selected in character mode. In this mode, you can scroll within the character set using the cursor keys. |
| ![Operation of operating elements](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43205122699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Positioning cursor | Positioning the cursor within an operating element, for example, in an I/O field |
| ![Operation of operating elements](images/43204907659_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the character to the left of the current cursor position |
| ![Operation of operating elements](images/43205030539_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the next character to the right of the current cursor position |
| ![Operation of operating elements](images/43205007499_DV_resource.Stream@PNG-de-DE.png) |  | Cancel | - Deletes the input characters of a value and restores the original value - Closes the active dialog. |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) | Scroll to start | Scrolls to the start page of a list |
| ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling back | Scrolls the list back by one page |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) | Scroll to end | Scrolls to the end of a list. |
| ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling up | Scrolls the list up by one page |
| ![Operation of operating elements](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Open selection list | Opens a selection list |
| ![Operation of operating elements](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) | Accept value | Accepts the value selected in the selection list without closing the list |

###### Enter shortcut

| Key | Function | Purpose |
| --- | --- | --- |
| ![Enter shortcut](images/43204874379_DV_resource.Stream@PNG-de-DE.png) | Toggle (numbers/letters) | Toggles the assignment from numbers to letters  - No LED is lit:   The number assignment is enabled. Pressing the key once switches to letter assignment. - The right or left LED is lit:   The left or right letter assignment is enabled.   Each time the key is pressed, the system toggles between the left letter assignment, the right letter assignment and the number assignment. |
| ![Enter shortcut](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | Shift (upper/lower case) | Used in shortcuts, for example, for switching to uppercase letters |
| ![Enter shortcut](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | Toggle to additional keyboard layout | Some of the keys contain a blue special character in their bottom left corner, for example, the percent sign "%". To input these characters, press the relevant key in combination with the special character key shown on the left. |
| ![Enter shortcut](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example, for navigating trend views |
| ![Enter shortcut](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example for the "Watch table" screen object |

###### Acknowledge alarms

| Key | Function | Purpose |
| --- | --- | --- |
| ![Acknowledge alarms](images/43204851339_DV_resource.Stream@PNG-de-DE.png) | Acknowledge | Acknowledges the currently displayed alarm or all alarms of an alarm group  The LED is lit as long as an unacknowledged alarm is active. |

###### Displaying infotext

| Key | Function | Description |
| --- | --- | --- |
| ![Displaying infotext](images/43205130379_DV_resource.Stream@PNG-de-DE.png) | Displaying infotext | For the selected object, opens a window with the configured infotext, for example, for an alarm or an I/O field  The LED is lit if an infotext is available for the selected object. |

Key or shortcut

##### Function Keys (Basic Panels)

The assignment of the function keys (F1, F2, F3, etc.) is defined during configuration.

###### Function keys with global function assignment

A globally assigned function key always triggers the same action on the HMI device or in the PLC regardless of the screen displayed. The activation of a screen or the closing an alarm window, for example, is such an action.

###### Function keys with local function assignment

A function key with local function assignment is screen-specific and is therefore only effective within the active screen.

The function of a locally assigned function key can vary from screen to screen.

Within a screen, a function key has only one function assignment, either a global or local one. The project planner specifies which assignment has priority.

###### Operating function keys

> **Note**
>
> **Operating function key after screen change**
>
> If you press a function key after a screen change, the associated function may be triggered in the new screen before the new screen is fully displayed.

#### Navigating in the display (BS) (Basic Panels)

##### Introduction

You navigate on the display of your HMI device as follows:

- between configured screen objects
- within screen objects

  When you select a complex screen object, the cursor focus switches to the screen object and follows the tab sequence there.
- in tables of screen objects

##### Procedure

- To navigate in the specified tab sequence, press the &lt;TAB&gt; key.
- To navigate freely between the operator controls, press the cursor keys.

Depending on the configuration of your HMI device, you can also use function keys or shortcuts for navigation.

When you operate your HMI device with the touch screen or with the mouse, you implicitly navigate by triggering a desired action. For this purpose, touch or click the operator control.

##### Result

The operator controls receive the cursor focus according to the selected sequence. You can trigger an action on the selected operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Triggering an action (Basic Panels)

##### Introduction

Triggering an action at an operator control can mean the following:

- A command is executed.

  Example: Click a button to trigger a script or to execute a predefined function.
- An object is enabled.

  Example: To enter a value, select a table cell with the &lt;Enter&gt; key.

##### Requirement

- You have navigated to the operator control on which you want to trigger the action.
- The operator control has the cursor focus.

##### Procedure

- Press &lt;Enter&gt;.

  Or
- Touch the operator control on the touch screen once or twice in rapid succession.

  Or
- Click or double-click the operator control with the mouse.

##### Result

The following results are possible:

- The requested command is executed.
- The screen keyboard is opened and/or the cursor blinks in the input area of the operator control.
- The element is selected and can be moved.

For more detailed information, refer to the operating instructions for your HMI device.

#### Entering a value (Basic Panels)

##### Introduction

Depending on the input format, you enter numerical or alphanumerical values in an input field.

You enter these values depending on the existing hardware using the screen keyboard, the control keys of the HMI device or an external keyboard.

##### Requirement

- The object is an input field or table field.
- The operator control is enabled.

##### Entering a value

1. Enter the desired value.
2. To confirm the value and exit the field, press the &lt;Enter&gt; key.
3. To discard the value and exit the field, press the &lt;Esc&gt; key.

##### Result

A value is entered or discarded. You navigate as needed to the next operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Moving operator controls (Basic Panels)

##### Introduction

In Runtime, you can move the movable operator controls of a screen object with the mouse or using the touch screen, for example, a slider or a scroll bar. Operation with the keyboard is described below.

##### Requirement

- A movable operator control is selected.

##### Procedure

- To move the operator control, proceed as follows depending on the operating element:

  - Standard for touch screen: Press the cursor keys.
  - Standard for keyboard devices: Press &lt;SHIFT&gt; and the cursor keys.
  - Switches: Press &lt;ENTER&gt;
  - Slider: Press &lt;PgUp&gt; or &lt;PgDn&gt;

1. To finish the movement, navigate to another screen object or operator control.

##### Slider procedure

1. To move the operator control, press the cursor keys.
2. To finish the movement, navigate to another screen object or operator control.

##### Result

The position of the movable operator control and the display in the screen object have changed.

For more detailed information, refer to the operating instructions for your HMI device.

#### Displaying infotext (Basic Panels)

##### Introduction

Depending on the configuration, additional information and operating instructions are available as infotext. The infotext is assigned to an operating element, an alarm or to the open screen. The infotext of an I/O field may contain, for example, information about the value to be entered.

As an alternative to the &lt;Help&gt; key of the HMI device, use the &lt;Help&gt; key of the screen keyboard for input objects.

##### Requirement

- An infotext is configured for the operating element, the screen or an alarm.

##### Calling the infotext

1. Enable the desired operating element.
2. Press the &lt;Help&gt; key of the HMI device.

   The infotext for the operating element is displayed.

If you are operating your input object with the touch screen, the screen keyboard opens. If the &lt;Help&gt; key appears, an infotext is configured for the operating element or the current screen.

If there is no infotext for the selected screen object, the infotext for the current screen is displayed, if it has been configured.

Use the scroll bar for long infotexts.

Depending on your configuration, infotext can also be retrieved by means of a configured operating element.

##### Switching between infotexts

- To switch between the infotexts of the operating elements and the screen, enable the infotext window.

##### Hiding infotext

- To hide the infotext, press the &lt;Esc&gt; key or press the &lt;Help&gt; key again.

#### Changing Runtime language (Basic Panels)

##### Introduction

The HMI device supports multilingual projects. A corresponding operating element which lets you change the language setting on the HMI device in Runtime has been configured.

The project always starts with the language set in the previous session.

##### Requirement

- The required language for the project is available on the HMI device.
- The language switching function is linked to an operating element, for example, to a button.

##### Selecting a language

You can change project languages at any time. Language-specific objects are immediately displayed on the screen in the new language when you switch languages.

You can switch the language in Runtime in one of the following ways:

- Use a configured operating element to switch from one language to the next in a list.
- Use a configured operating element to directly set the required language.

### Entering bar codes with optical handheld readers (Basic Panels)

#### Introduction

With the optical handheld readers you can identify components, machines and other objects optically and enter them directly into multiple operating elements on your HMI device.

Optical handheld reading devices read two dimensional data matrix codes, one dimensional barcodes and postal bar codes.

The following optical handheld readers are supported:

- SIMATIC MV320
- SIMATIC MV340

You can find templates for the settings and instructions on configuration in the manual for your optical handheld reader.

> **Note**
>
> The optical handheld reader is connected to the USB port of the HMI device. Only one device at a time can use the USB port. This is why it is not possible to use a USB keyboard and an optical handheld reader or two optical readers at the same time.

> **Note**
>
> When you connect the optical reader to a configuration PC, ensure that the USB port provides sufficient power for the reader.

#### Procedure

You read the marking of an object using the connected optical handheld reader. The value is entered in the object on the HMI device which has the focus during runtime.

After it has been read in, confirm the value with the Enter key or with the "Suffix - Enter" that you have previously configured in the settings of your optical handheld reader.

#### Basic Panels, Comfort Panels, Mobile Panels, RT Advanced

The following objects support input with optical handheld readers:

| Object | Preconditions for input |
| --- | --- |
| I/O field  Date/time field | The corresponding data type is selected.  The object and the tag length are configured accordingly.  The operator element has the cursor focus. |
| Recipe view | The recipe data record has the cursor focus. |
| User view | The logon dialog is open.  The user name or password has the cursor focus. |
| HTML browser | The operator element has the cursor focus. |
| Runtime dialogs which support keyboard entry | The dialog is open and the corresponding input field has the cursor focus. |

#### Comfort Panels, Mobile Panels, RT Advanced

The following objects support input with optical handheld readers:

| Object | Preconditions for input |
| --- | --- |
| Sm@rtClient view | Write access is configured for Sm@tClient.  The operator element has the cursor focus. |
| File browser | The field "File path" has the cursor focus. |
| Watch table | The input field "Control value" has the cursor focus. |
| PDF view | The search field has the cursor focus. |
| SINUMERIK NC operator display | The operator element has the cursor focus. |

#### Result

The code is read and entered into the corresponding input field.

### Security on the HMI device (Basic Panels)

This section contains information on the following topics:

- [Signature basics (Basic Panels)](#signature-basics-basic-panels)
- [Switching off the signature check (Basic Panels)](#switching-off-the-signature-check-basic-panels)

#### Signature basics (Basic Panels)

##### Overview

The HMI device software and the runtime and device options are protected from manipulation by signatures. The device options available over ProSave are also signed.

**HMI device signature**

The validity of the HMI device signature is checked when the HMI device software is loaded. If the HMI device signature is invalid, loading of the HMI device software is canceled and an error message is output.

**Signature for runtime and device options**

If the signature check finds that the signature is invalid, an error message to this effect is output. An error message indicating an invalid signature is also output in ProSave.

> **Note**
>
> To allow loadingof the HMI device software or the options without a signature (for versions prior to V14), you will need to switch off the signature check.

For details of how to do this, see [Switching off the signature check](#switching-off-the-signature-check-basic-panels).

---

**See also**

[Switching off the signature check (Basic Panels)](#switching-off-the-signature-check-basic-panels)

#### Switching off the signature check (Basic Panels)

##### Procedure

1. Press "Transfer" twice in the control panel of the HMI device.

   The "Transfer Settings" dialog box opens.

   The option "Validate signatures" is enabled by default.
2. To allow the HMI device software to be loaded without a signature or to allow the download of a trustworthy option from a third-party provider, disable the "Validate signatures" option.

**Note**

If you wish to load an older WinCC project to an HMI device, you will need to check the settings for the signature check.

---

**See also**

[Signature basics (Basic Panels)](#signature-basics-basic-panels)

## Runtime Advanced and Panels (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Runtime settings (Panels, Comfort Panels, RT Advanced)](#runtime-settings-panels-comfort-panels-rt-advanced)
- [Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)
- [Compiling a project (Panels, Comfort Panels, RT Advanced)](#compiling-a-project-panels-comfort-panels-rt-advanced)
- [Simulating projects (Panels, Comfort Panels, RT Advanced)](#simulating-projects-panels-comfort-panels-rt-advanced)
- [Loading projects (Panels, Comfort Panels, RT Advanced)](#loading-projects-panels-comfort-panels-rt-advanced)
- [Compiling and loading with Multiuser Engineering (Panels, Comfort Panels, RT Advanced)](#compiling-and-loading-with-multiuser-engineering-panels-comfort-panels-rt-advanced)
- [Starting Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-panels-comfort-panels-rt-advanced)
- [Error messages during loading of projects (Panels, Comfort Panels, RT Advanced)](#error-messages-during-loading-of-projects-panels-comfort-panels-rt-advanced)
- [Adapting the project for another HMI device (Panels, Comfort Panels, RT Advanced)](#adapting-the-project-for-another-hmi-device-panels-comfort-panels-rt-advanced)
- [Reducing the project size (Panels, Comfort Panels, RT Advanced)](#reducing-the-project-size-panels-comfort-panels-rt-advanced)
- [Supported network cameras and settings (Panels, Comfort Panels, RT Advanced)](#supported-network-cameras-and-settings-panels-comfort-panels-rt-advanced)
- [Viewing memory card data (Panels, Comfort Panels, RT Advanced)](#viewing-memory-card-data-panels-comfort-panels-rt-advanced)
- [Working with HMI device images (Panels, Comfort Panels, RT Advanced)](#working-with-hmi-device-images-panels-comfort-panels-rt-advanced)
- [Basics of operating in Runtime (Panels, Comfort Panels, RT Advanced)](#basics-of-operating-in-runtime-panels-comfort-panels-rt-advanced)
- [Entering bar codes with optical handheld readers (Panels, Comfort Panels, RT Advanced)](#entering-bar-codes-with-optical-handheld-readers-panels-comfort-panels-rt-advanced)
- [Security on the HMI device (Panels, Comfort Panels, RT Advanced)](#security-on-the-hmi-device-panels-comfort-panels-rt-advanced)

### Runtime settings (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Runtime settings (Panels, Comfort Panels, RT Advanced)](#runtime-settings-panels-comfort-panels-rt-advanced-1)
- [Configuring display in Runtime (Comfort Panels)](#configuring-display-in-runtime-comfort-panels)
- [Configuring operation in Runtime (Panels, Comfort Panels, RT Advanced)](#configuring-operation-in-runtime-panels-comfort-panels-rt-advanced)
- [Compatibility check with the controller (Panels, Comfort Panels, RT Advanced)](#compatibility-check-with-the-controller-panels-comfort-panels-rt-advanced)
- [Setting time base (Panels, Comfort Panels, RT Advanced)](#setting-time-base-panels-comfort-panels-rt-advanced)
- [Printing in Runtime (Panels, Comfort Panels, RT Advanced)](#printing-in-runtime-panels-comfort-panels-rt-advanced)
- [Password protection in Runtime (Panels, Comfort Panels, RT Advanced)](#password-protection-in-runtime-panels-comfort-panels-rt-advanced)

#### Runtime settings (Panels, Comfort Panels, RT Advanced)

##### Introduction

To edit the runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree.

> **Note**
>
> **Device dependency**
>
> The options available for selection in the runtime settings depend on the HMI device.

##### Overview

You configure options from different areas of your project in the runtime settings:

- Display in runtime

  - Start screen
  - Default template
  - Default style of the project and style of the HMI device
  - Screen resolution
  - Full-screen mode
  - Project graphics
  - Bit selection for color and flashing
  - Bit selection for text and graphic lists
- Project ID for compatibility check with the controller
- Logging language
- Remote control via Sm@rt server in the "Services" area

  You can find additional information on this in the WinCC online help under "Options &gt; Sm@rt options"
- Operator control in runtime

  - Task switching
  - Load additional information for debugging scripts: Object names and comments in scripts
  - Show limits as a tooltip
  - Screen keyboard
  - Disable function keys
  - Release buttons when cursor leaves the button
  - Keyboard layout and shortcuts
- GMP-compliant configuration

  You can find additional information on this in the WinCC online help under "Options &gt; WinCC Audit".
- Alarms

  - Buffer overflow
  - Acknowledgment group text
  - Log
  - Colors of the alarm classes
  - Download S7 diagnostic help texts
  - Configuration of the system events: Display duration, S7 diagnostic messages with/without displayed message text, SIMOTION diagnostic messages
  - Configuration of the controller alarms:
  - Persistent alarm buffer
- User administration

  - Configuration password and logoff time
  - Limit for login attempts
  - Hierarchy levels
  - Configuration of SIMATIC Logon
- Language and font

  - Available runtime languages
  - Order of language switching
  - Default font
  - License status of the fonts
- Configuration of the OPC Unified Architecture Server
- Settings for synchronization of PLC and HMI tags

---

**See also**

[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring display in Runtime (Comfort Panels)](#configuring-display-in-runtime-comfort-panels)
  
[Configuring operation in Runtime (Panels, Comfort Panels, RT Advanced)](#configuring-operation-in-runtime-panels-comfort-panels-rt-advanced)
  
[Configuring alarm buffer overflow (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-alarm-buffer-overflow-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Editing system events (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#editing-system-events-panels-comfort-panels-rt-advanced)
  
[Editing controller alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#editing-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Configuration in WinCC (Panels, Comfort Panels, RT Advanced)](WinCC%20Sm%40rtServer%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#configuration-in-wincc-panels-comfort-panels-rt-advanced)
  
[GMP compliance (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gmp-compliance-panels-comfort-panels-rt-advanced)
  
[Compatibility check with the controller (Panels, Comfort Panels, RT Advanced)](#compatibility-check-with-the-controller-panels-comfort-panels-rt-advanced)
  
[Configuring the display of security events (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-display-of-security-events-panels-comfort-panels-rt-advanced-rt-professional)
  
[Activating system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#activating-system-diagnostics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring display in Runtime (Comfort Panels)

##### Introduction

In the Runtime settings, you specify how screens, alarms and language are displayed.

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree. The options available for selection depend on the HMI device.

##### Display on the target system

In WinCC, configure the visual representation of the generated project in Runtime:

- Select the full-screen or window mode for the project. The window has a smaller size than the screen. In full-screen mode, the project is zoomed to the full screen. There will be no window and operator controls for this view.   
  Click "General" in the "Settings" editor to activate the full-screen display at startup. Activate the "Full-screen mode" check box in the "Screen" field.

  > **Note**
  >
  > **Truncated view**
  >
  > If the HMI screen does not match the configured size (in pixels), the project only appears on part of the screen in full-screen mode.
- To hide the taskbar, disable the taskbar under Windows.
- Under "General &gt; Screen", you specify whether the HMI device uses the default style of the project or another pre-defined style.

##### Language settings

- Logging language

  Under "General &gt; Logs", you specify the language in which you want to write the logs. The selected logging language always remains the same, even if the user switches the language in Runtime.

  If you select "Startup language", the logging language remains the same until Runtime is stopped, even if the user has switched the language. However, the next time Runtime is started, the last configured Runtime language is used as the logging language.
- Runtime language

  Under "Language &amp; font", you specify all Runtime languages and their display.

  > **Note**
  >
  > **"Bold" and "Italic" fonts**
  >
  > "Bold" and "italic" fonts are not supported on all HMI devices in Runtime.

  > **Note**
  >
  > **Basic Panels**
  >
  > Text entries may be truncated if you select an unfavorable font size or style. This setting may have an effect on the following text entries:
  >
  > - Tooltips
  > - Long alarm text
  > - Text in the dialogs

##### Setting for specific screen objects

- Specify bit selection

  Under "Screens &gt; Bit selection", you specify whether bit selection will be used on this HMI device for the following:

  - Text and graphics (text lists and graphic lists)
  - Color and flashing (appearance analysis)

    When you enable an option, the selection that is configured in the set bit with the least significance is displayed:

    When you disable an option and several bits are set, the selection that has been configured only for the set bit is displayed.
- Tooltips for I/O fields

  Under "Screens &gt; Display", you specify whether configured limit values are displayed as tooltips in Runtime when values are entered in I/O fields.
- Colored objects

  You specify the color depth of your HMI device under "General &gt; Screens &gt; Color depth". As needed, you assign screen objects a colored appearance. The range of colors is determined by the color depth supported on your selected HMI device.

##### Design settings in the Windows Control Panel

Select the "Windows 7" design for the configuration PC and the Runtime PC in the system settings of Windows. Use this setting to ensure correct representation of the dialogs and the on-screen keyboard in Runtime.

#### Configuring operation in Runtime (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the Runtime settings you specify how screens are operated, and how you use keys for operation in Runtime.

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree. The options available for selection depend on the HMI device.

##### Locking task switching

Depending on the HMI device, you can lock task switching on the HMI device. This will prevent the operator from opening other applications in Runtime.

In the Runtime settings of the HMI device, enable the "Lock task switching" option under "General &gt; Screen".

To use the "Lock task switching" option on a Runtime PC, disable the Aero theme in Windows 7 and Windows 8.x. To disable the Aero theme, right-click on the desktop and select "Personalize". In the "Personalization" menu, select the designs "Windows Basic" or "Windows - Classic".

> **Note**
>
> **Stop Runtime**
>
> If you lock program switching, always configure in your project the system function "StopRuntime" for an object, e.g. a softkey or button.

> **Note**
>
> The option "Lock task switching" affects the Runtime Advanced on-screen keyboard, but not the Windows on-screen keyboard.

##### Deactivating the Windows screen keyboard

To lock task switching for the Windows on-screen keyboard, you have to completely deactivate the Windows on-screen keyboard.

Proceed as follows to deactivate the Windows on-screen keyboard:

1. Open the on-screen keyboard.
2. Open the “Options” dialog via “Tools &gt; Options".
3. In the "Initialization" tab, deactivate the options "Touch input, show the icon next to the textbox", "Show the icon on the taskbar", "Use the input panel" tab.

The Runtime Advanced on-screen keyboard is not affected by these changes and can continue to be opened and operated.

> **Note**
>
> To activate the Windows on-screen keyboard again, open Start &gt; Programs &gt; Accessories &gt; Ease of Access &gt; On-screen keyboard”.

##### Settings for data transfer to the HMI device

- Transferring names of the screen objects in scripts

  If you enable the "Load names" option under "General &gt; Screen", the object names of the screen objects are transferred instead of coded addressing information. You need the object names if you want to address the screen objects in a script using the object names. When you test a script in the debugger, the code becomes more comprehensible through the display of object names.
- Displaying comments in scripts

  Under "Screens &gt; Display", you specify whether the comments in scripts are also transferred to the HMI device.

  If you do not transfer the comments, you save storage space on your HMI device.

  If you transfer the comments, the script is more easily understood during testing in the debugger.

##### Operation using function keys

To symbolize the function of a function key for keyboard devices, you configure a graphic next to the function key in the display. Under "Screens &gt; Function keys &gt; User-defined pictogram size", you specify whether you want to use a graphic size that deviates from the standard size.

##### Operation with keyboard

Under "Keyboard &gt; General &gt; Use screen keyboard", you specify whether the screen keyboard is available on your HMI device.

Under "Keyboard &gt; General &gt; Release button on exit", you specify whether the "Release" event is triggered when the user exits a button without releasing it.

Under "Keyboard &gt; Disable function keys in dialogs", you specify for key devices whether the function keys are disabled for the duration of the displayed dialog. Large dialogs can hide explanatory areas or graphics at function keys or bordering function keys. Functions keys can be unintentionally pressed due to this.

#### Compatibility check with the controller (Panels, Comfort Panels, RT Advanced)

##### Introduction

The "Project ID" area pointer is used to configure the project ID for checking the consistency of the project with the PLC. The area pointer reads the project version from the PLC. You can find additional information in the online help for WinCC under "Communicating with controllers".

##### Compatibility check with the controller

You select the project ID in the Runtime settings of the HMI device under "General &gt; Identification &gt; Project ID".

At startup, Runtime checks whether the project ID of the project matches the PLC project version. Runtime will only start if the two values match.

An area pointer "Project ID" is created for connections whose address you specify in the PLC. The value that you store at this address will become the project ID.

The project ID is not available on all HMI devices.

#### Setting time base (Panels, Comfort Panels, RT Advanced)

##### Setting the time base for the time of day

You set the time in the Control Panel of your HMI device. For more detailed information, refer to the operating instructions for your HMI device.

##### Synchronize date and time with the PLC

You can find additional information on this subject in the online help for WinCC under "Communicating with the PLC".

#### Printing in Runtime (Panels, Comfort Panels, RT Advanced)

##### Print functions

Print functions available in online mode:

- Hardcopy

  You print out the currently displayed screen by means of an operator control that triggers the "PrintScreen" system function.
- Printing alarms

  Every alarm that has occurred and its state changes are reported along on a printer.
- Printing reports

  Reports are output in graphic mode. The use of a serial printer is not recommended because of the accumulated data volume.

  For proper output, the printer must support the paper format and page layout of the report.

  > **Note**
  >
  > The value of a tag in the report is read and output at the moment of printing. A substantial time may elapse between printing out the first and the last page of a report consisting of several pages. This may lead to the same tag on the last page being output with a different value from that on the first page.

#### Password protection in Runtime (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Password protection in Runtime (Advanced) (Panels, Comfort Panels, RT Advanced)](#password-protection-in-runtime-advanced-panels-comfort-panels-rt-advanced)
- [Configuring a password for transport (Panels, Comfort Panels, RT Advanced)](#configuring-a-password-for-transport-panels-comfort-panels-rt-advanced)
- [Resetting the password for transport (Panels, Comfort Panels, RT Advanced)](#resetting-the-password-for-transport-panels-comfort-panels-rt-advanced)

##### Password protection in Runtime (Advanced) (Panels, Comfort Panels, RT Advanced)

###### Overview

The connection establishment can be protected with passwords in the TIA Portal. The configured passwords are saved in encrypted form. During transfer to the target system, the passwords are also protected against unauthorized access and cannot be read. These passwords are decrypted securely on the HMI devices in Runtime.

Password protection can be created for the following connections:

- SIMATIC S7-1200
- SIMATIC S7-1500
- SIMATIC S7-1500 Software Controller (WinAC)
- PC Station 2.0 (station manager)
- SIMATIC HMI HTTP

Password protection can also be created for the following system function:

- "SendEMail" system function

> **Note**
>
> The passwords become invalid at a change to an older version.

###### Download certificate

The certificate for decrypting the passwords is saved in the certificate store of the HMI device. You will be informed by a system message if the certificate is not available.

You restore the certificate by downloading the configuration once again.

##### Configuring a password for transport (Panels, Comfort Panels, RT Advanced)

###### Introduction

To protect the private password key during transport, you can configure a password for transport under "Runtime settings".

###### Creating password

1. Open the "Runtime settings &gt; General" editor in the Project window.
2. Enter the password in the "Enter password" field in the "Transport password" area.
3. Confirm the password in the "Confirm password" field.

> **Note**
>
> If there was no previous password, the "Old password" field is disabled.

###### Result

You have now configured the password for transport. If a password for transport has been configured and you transfer the project to the HMI device, a dialog with a password prompt will appear once in runtime.

If the password entered is correct, the certificate is saved in the certificate store of the HMI device.

When you change the password, load the project with the changed password into the HMI device and start Runtime. No password prompt appears.

##### Resetting the password for transport (Panels, Comfort Panels, RT Advanced)

###### Introduction

If you have moved the transport password, for example, you can create a new security certificate. To do so, reset the transport password.

###### Reset password

1. Click the "Reset password" button.

   The password is reset. A new certificate without a password is generated.
2. Enter the new password and confirm it in the "Confirm password" field.

**Note**

Other passwords, for example the password for the PLC, will become invalid. The next time you compile, an error message will appear telling you that these passwords are no longer valid.

**Note**

The certificate is not password-protected until you enter a new password for transport.

After download of the project to the HMI device, you will be prompted for the password.

### Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)

#### Overview

The project is compiled in the background even as you are configuring it in WinCC. This reduces the time for final compilation. When you start compilation, you create a file that can be run on the corresponding HMI device.

If an error occurs during compilation, WinCC provides support in locating and correcting it.

Once you have corrected any problems, you download the compiled project to the HMI devices on which the project is to run. If the configuration PC is not connected to the HMI device, save the compiled project on a data medium of your choice. The compiled project is then transferred from a PC connected to the HMI device to the HMI device.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile all modified S7 blocks with the command "Compile &gt; Software" in the shortcut menu before you compile the HMI device.

#### Project

The term "project" has two different meanings in the contexts of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of an HMI device

The figure below illustrates the link between WinCC projects and Runtime projects using the example of the "Compile and load" process:

![Project](images/46298521483_DV_resource.Stream@PNG-en-US.png)

#### Runtime

Runtime is the software for process visualization. In Runtime, you execute the project in process mode.

A distinction is made between two types of Runtime:

1. Runtime on a panel

   Before running a Runtime project on a panel, you have to transfer the Runtime project to the panel before startup.
2. Runtime on a PC

   You can execute the Runtime project directly on the configuration PC if Runtime has been installed on the configuration PC.

   If you want to execute the Runtime project on a different PC, you have to transfer the Runtime project to the PC before startup.

#### Runtime version

The Runtime version depends on the image of the configured HMI device. The Runtime version of the compiled project is displayed under "Info" in the Inspector window.

#### Simulation

You test your configuration with a simulation. You can start a simulation without a link to the active process.

In a simulation, you test configured tags or screen changes, for example. During the simulation, the configured tags can be manipulated, activated and deactivated with the help of the tag simulator.

There are two types of simulation:

1. Simulating a panel

   If you created a panel in your project, the panel is displayed in the simulation. With the help of this type of simulation, you can test your configuration on the HMI device without transferring the project to the panel.
2. Simulating Runtime

   Simulating Runtime allows you to test the project directly on the configuration PC.

### Compiling a project (Panels, Comfort Panels, RT Advanced)

#### Introduction

The changes made to the project are compiled in the background even as you are configuring a project in WinCC. Projects are compiled automatically when you load them. This ensures that the latest version of the project is loaded at all times.

WinCC checks consistency of the project during compilation. The error locations in the project are listed in the Inspector window. You can jump directly to the source of the error from the entry in the Inspector window. Check and correct errors found.

#### Scope of the compilation

Configuration data is compiled in the background as soon as you start configuring an HMI device. If you compile a project manually, only the changes in the configuration made since the last compilation process are compiled in the background.

You can start complete project compilation manually at any time; this may, for example, be done to test the consistency of the configured data.

#### Requirement

- A project is open.

#### Procedure

Proceed as follows to compile a project:

1. If you want to compile several HMI devices at the same time, select all the relevant HMI devices with multiple selection in the project tree.
2. Compile the project:

   - To only compile changes in the project, select the "Compile &gt; Software (only changes)" command from the shortcut menu of the HMI device.
   - To compile all project data, select the "Compile &gt; Software (compile all)" command from the shortcut menu.

#### Result

The configuration data of all selected HMI devices is compiled. Any errors that occur during compilation are shown in the Inspector window.

---

**See also**

[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)

### Simulating projects (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Simulation basics (Panels, Comfort Panels, RT Advanced)](#simulation-basics-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced simulation (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-simulation-panels-comfort-panels-rt-advanced)
- [Simulating a project (Panels, Comfort Panels, RT Advanced)](#simulating-a-project-panels-comfort-panels-rt-advanced)
- [Simulating a screen (Panels, Comfort Panels, RT Advanced)](#simulating-a-screen-panels-comfort-panels-rt-advanced)
- [Working with the tag simulator (Panels, Comfort Panels, RT Advanced)](#working-with-the-tag-simulator-panels-comfort-panels-rt-advanced)
- [Simulation restrictions (Panels, Comfort Panels, RT Advanced)](#simulation-restrictions-panels-comfort-panels-rt-advanced)

#### Simulation basics (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can use the simulator to test the performance of your configuration on the configuration PC. This allows you to quickly locate any logical configuration errors before productive operation.

You can start the simulator as follows:

- In the shortcut menu of the HMI device or in a screen: "Start simulation"
- Menu command "Online &gt; Simulation &gt; [Start|With tag simulator|With script debugger]"
- Under "Visualization &gt; Simulate device" in the portal view.

##### Requirement

The simulation/runtime component is installed on the configuration PC.

##### Field of application

You can use the simulator to test the following functions of the HMI system, for example:

- Checking limit levels and alarm outputs
- Consistency of interrupts
- Configured interrupt simulation
- Configured warnings
- Configured error messages
- Check of status displays

---

**See also**

[Simulating a project (Panels, Comfort Panels, RT Advanced)](#simulating-a-project-panels-comfort-panels-rt-advanced)
  
[Simulating a project (RT Professional)](#simulating-a-project-rt-professional)
  
[Working with the tag simulator (Panels, Comfort Panels, RT Advanced)](#working-with-the-tag-simulator-panels-comfort-panels-rt-advanced)
  
[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)

#### WinCC Runtime Advanced simulation (Panels, Comfort Panels, RT Advanced)

##### Introduction

There are two different simulation modes for Runtime Advanced simulation:

- Device simulation
- Tag simulation

Both types of simulation simulate the project without a direct process link to the configuration PC. Data such as logs or recipes generated during simulation are not deleted. This data is saved on the configuration PC in the paths configured in the project.

##### Device simulation

Use device simulation to simulate operator control of the HMI device. Device simulation is, for example, used to test screen switching.

##### Tag simulation

Use tag simulation to simulate the configured process tags. You can either have tag values generated automatically by a simulation table or define tag values yourself.

#### Simulating a project (Panels, Comfort Panels, RT Advanced)

##### Introduction

You simulate your project with one of the following two methods:

- Without a connected PLC

  You change the value of area pointers and tags in a tag simulator that is read for the simulation of WinCC Runtime.
- With a connected PLC without a running process

  You simulate your project by running it directly in Runtime. The tags and area pointers become active. This allows you to create an authentic simulation of your configured HMI device in Runtime.

  > **Note**
  >
  > **Simulation restrictions**
  >
  > You cannot simulate the following system functions:
  >
  > - CalibrateTouchScreen
  >
  > You cannot simulate the Media Player. A static screen appears in the simulation window instead of the Media Player.
  >
  > File access via scripts is not possible for HMI devices with Windows CE.

##### Requirement

- Simulation without a connected PLC: Tags have been created
- Simulation with a connected PLC but no active process: A project with tags and area pointers has been created

##### Procedure

To simulate a project using the tag simulator, follow these steps:

1. Open the project on the configuration PC.
2. Select the "Online &gt; Simulation &gt; With tag simulator" menu command.

   For initial project simulation, the simulator is started with a new, empty table. The project is opened simultaneously in Runtime.

   Toggle between the tag simulator and Runtime using the &lt;Alt +Tab&gt; key combination.
3. To simulate a process value, select the corresponding "tag" from the tag simulator.

   The table lists all configured tags. You can simulate up to 300 tags simultaneously.
4. Select the simulation mode in the "Simulation" column.
5. Change the value of tags and area pointers in the respective columns.
6. Activate the "Start" check box to start the simulation for this tag.
7. To save the simulation, select the menu command "File &gt; Save" and enter a descriptive name, for example, "Mixing".

   The file name is assigned the extension "*.cors".

##### Result

The process values are simulated in Runtime. The tag values are created at random, or incremented, depending on the simulation mode.

To specify tag values, change the simulation mode to "&lt;Display&gt;" and enter a value at "Set value".

The following figure shows a tag simulator with four tags whose values can be determined at random in a range of values from 10 to 1000:

![Result](images/23309309707_DV_resource.Stream@PNG-en-US.png)

##### Managing simulation data

If you have saved data from a previous simulation, you can open the file at a later point in time and simulate your project again. The tags and area pointers listed in the tag simulator must still be available in the project.

Proceed as follows to open a simulation file:

1. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".
2. Select the menu command "File &gt; Open" in the tag simulator.
3. Select the corresponding simulation file and click "Open".

   The simulator loads the stored data.

##### Enabling and disabling tags

Start and stop the simulation for each tag separately in order to facilitate the transition from offline to online engineering. Activate "Start" in the corresponding row.

If a tag is activated, the simulation values are calculated and transferred to the WinCC simulator.

##### Deleting a tag

To delete a tag from the tag simulator, follow these steps:

1. Select the cell that contains the tag name.
2. Select the "Edit &gt; Cut" menu command.

   The tag is removed from the table.

---

**See also**

[Simulation basics (Panels, Comfort Panels, RT Advanced)](#simulation-basics-panels-comfort-panels-rt-advanced)

#### Simulating a screen (Panels, Comfort Panels, RT Advanced)

##### Introduction

If you have only made changes to one screen, you can temporarily specify this screen as the start screen for simulation. In this way, you can debug changes without having to modify the start screen, or opening the screen on the HMI device.

##### Requirements

You created a project that contains at least one screen.

##### Procedure

To define a screen as temporary start screen for simulation, follow these steps:

1. In the project navigation, select the image to display as the start screen in the simulation.
2. Select the "Start simulation" command from the shortcut menu of the screen.

##### Result

Project simulation is started. Instead of the configured start screen, the simulation window the screen you selected in the project navigation.

#### Working with the tag simulator (Panels, Comfort Panels, RT Advanced)

##### About the tag simulator

The tag simulator has the following columns:

| Column | Description |
| --- | --- |
| Tag | Specifies the tags for the simulation. |
| Data type | Shows the data type of the selected tag. |
| Current value | Shows the simulated value of the defined tags. |
| Format | Specifies the selected format in which the tag values are simulated:   - Decimal (1, 2, 3, 4, ...) - Hexadecimal (03CE, 01F3, ...) - Binary (0 and 1) |
| Write cycle | Specifies the selected time interval at which the current tag values are simulated. If you enter "2", for example, the current value of the tag will be shown every 2 seconds. |
| Simulation | Shows the method by which the tag values are processed during simulation. |
| Set value | Sets the selected value for the respective tag. The simulation start with the specified value. |
| minValue   maxValue | Specifies the value range of the tag. You set a minimum and maximum value for this range. The default values are -32768 for the minimum and 32767 for the maximum. |
| Period | Contains the period during which the value of the tag is repeated for the "Increment" and "Decrement" simulation modes. |
| Start | Starts simulation of the tag based on the previously entered information. |

##### Simulation modes

The simulator has six different simulation modes. The configured tags are supplied with nearly realistic values during the simulation.

| Simulation mode | Description |
| --- | --- |
| Sinusoidal | Changes the tag value to form a sinusoidal curve. The value is visualized as a periodic, non-linear function. |
| Random | Provides randomly generated values. The tag value is changed by means of a random function. |
| Increment | Increases the value of the tag continuously up to a specified maximum value. Begins again at the minimum after the maximum has been reached. The value trend corresponds to a positive saw-tooth curve. |
| Decrement | Reduces the value of the tag continuously down to a specified minimum value. Begins again at the maximum after the minimum has been reached. The value curve corresponds to a negative saw-tooth curve. |
| Shift bit | Shifts a set bit continuously by one position. The previous position is always reset. This lets you test the alarms of an HMI device, for example. |
| &lt;Display&gt; | The current tag value is displayed statically. |

##### Example: Simulate tags with the "Shift bit" simulation mode

Proceed as follows to simulate tags with the "Shift bit" simulation mode:

1. Open the project you want to simulate.
2. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".

   The tag simulator opens.
3. In the "Tag" column, select a tag from your project.
4. Select "Bin" in the "Format" column.
5. Enter the value "1" in the "Write cycle" column.
6. Select the "Shift bit" simulation mode in the "Simulation" column.
7. Enter the value "1" in the "Set value" column.
8. Enable the tag with the "Start" check box.

##### Result

The simulator tests the selected tag bit-by-bit as follows:

| Simulation values | Byte for alarms |
| --- | --- |
| Set start value | 00000001 |
| 1. Simulation value | 00000010 |
| 2. Simulation value | 00000100 |
| 3. Simulation value | 00001000 |
| .... | ... |

In Runtime you see if the desired alarm is output at a given value.

---

**See also**

[Simulation basics (Panels, Comfort Panels, RT Advanced)](#simulation-basics-panels-comfort-panels-rt-advanced)

#### Simulation restrictions (Panels, Comfort Panels, RT Advanced)

##### Connection

The connection to PLCSim is only possible via an integrated connection.

##### Alarms with dynamic parameters

If you use tags or text lists as external tags for alarms, the dynamic parameters of the alarms are not displayed.

Only internal tags are enabled for the simulation of alarms in the tag simulator .

Use PLCSim to simulate dynamic parameters.

##### Panels

If you want to use PLCSim with version V14 or higher for simulation with a panel, the device version of the panel must be 14.0.0.0 or higher.

### Loading projects (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
- [Overview for loading of projects (RT Advanced)](#overview-for-loading-of-projects-rt-advanced)
- [Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)
- [Generating a "Pack&amp;Go" file (Panels, Comfort Panels)](#generating-a-packgo-file-panels-comfort-panels)
- [Downloading projects from a "Pack&amp;Go" file to the HMI device (Panels, Comfort Panels)](#downloading-projects-from-a-packgo-file-to-the-hmi-device-panels-comfort-panels)
- [Loading via USB interface (Panels, Comfort Panels, RT Advanced)](#loading-via-usb-interface-panels-comfort-panels-rt-advanced)
- [Load project from external storage medium (Panels, Comfort Panels, RT Advanced)](#load-project-from-external-storage-medium-panels-comfort-panels-rt-advanced)
- [Installing a USB driver in Windows 7 (Panels, Comfort Panels, RT Advanced)](#installing-a-usb-driver-in-windows-7-panels-comfort-panels-rt-advanced)

#### Overview for loading of projects (Panels, Comfort Panels)

##### Overview

Delta data of the project is automatically compiled before you download it to one or several HMI devices. This always ensures that the latest version of the project is transferred.

##### Loading a project to an HMI device

The following steps are completed prior to downloading:

1. The download settings are verified. The "Extended download to device" dialog box opens automatically during the initial download of a project to an HMI device. You use this dialog to define the protocol and interface or destination path for the project in accordance with the HMI device Runtime used.

   If the HMI device is part of a subnet, for example, you also select the subnet and the first gateway.

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens.
2. The project is compiled. Warnings and errors during compilation are displayed in the Inspector window and in the "Load preview" dialog box.
3. The "Load preview" dialog box shows you the following information for each HMI device:

   - The individual steps for loading
   - If the device version of the target HMI device does not match the configured device version, you are queried if you want to change the device version at this time.

     As long as the project with the selected device version of the target HMI device is not executable, you cannot start the download.

     | Symbol | Meaning |
     | --- | --- |
     |  | **Notice** |
     | **Changing the device version deletes all data on the HMI device.**   Data is deleted on the target system if you change the device version. For this reason, you should first back up the following data: - User administration - Recipes - License keys With Comfort devices, the licenses can only be deleted when resetting to factory settings. Back up the license keys before you restore the factory settings. |  |
   - Presettings that take effect at loading. You can change the default settings for this download process, if necessary.
   - Warning events (optional). You can download a project while ignoring the "warnings". The functionality may be restricted in runtime.
   - Error events (optional). You cannot load the project. Eliminate the errors and then reload the project.

     WinCC will open the invalid configuration in the corresponding editor if you double-click the error message in the Inspector window. Correct the errors and reload the project.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile the user program before you compile the HMI device.

> **Note**
>
> **Interruption of a download**
>
> If the download is interrupted, WinCC automatically ensures that no data is lost and that existing data is deleted on the HMI device only after complete transmission.

##### Loading a project without a connected HMI device

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to an external storage medium, e.g. a USB stick, and load it from the USB flash drive to the HMI device.

This function is available in connection with an HMI device image which is compatible with TIA Portal version V14 or higher.

Generate the required project data in WinCC by configuring the HMI device and then dragging the HMI device folder (such as "HMI_1 [&lt;Device type&gt;]") to an external storage medium under "Card Reader/USB memory".

##### Loading of projects without recipe data records

You are using recipes in a project. You transfer the project to a Basic Panel without recipe data records.

You may encounter inconsistencies if you have altered the structure of the recipe in the engineering system and the device already held recipe data records.

Check the consistency of the data records in this case. The device will not issue a note for all structural changes.

##### Pack&amp;Go

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to a PC that is connected to the HMI device, for example via a network. Download the project from this PC to the HMI device.

##### Loading with S7 routing

Configure the S7 routing settings in the "Devices &amp; Networks" editor in the relevant PLC. The settings depend on the device configured.

S7 routing supports the following protocols:

- MPI/PROFIBUS
- PN/IE

##### Transferring Runtime add-ons in WinCC

Projects can contain Runtime add-ons in the form of controls or CSP (Communication Support Packages). These Runtime add-ons are automatically transferred with the project.

---

**See also**

[Loading via USB interface (Panels, Comfort Panels, RT Advanced)](#loading-via-usb-interface-panels-comfort-panels-rt-advanced)
  
[Installing a USB driver in Windows 7 (Panels, Comfort Panels, RT Advanced)](#installing-a-usb-driver-in-windows-7-panels-comfort-panels-rt-advanced)
  
[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)
  
[Load project from external storage medium (Panels, Comfort Panels, RT Advanced)](#load-project-from-external-storage-medium-panels-comfort-panels-rt-advanced)
  
[Downloading projects from a "Pack&amp;Go" file to the HMI device (Panels, Comfort Panels)](#downloading-projects-from-a-packgo-file-to-the-hmi-device-panels-comfort-panels)
  
[Overview of online delta transfers (RT Professional)](#overview-of-online-delta-transfers-rt-professional)
  
[Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)
  
[Downloading the project to an HMI device (RT Professional)](#downloading-the-project-to-an-hmi-device-rt-professional)
  
[Generating a "Pack&amp;Go" file (Panels, Comfort Panels)](#generating-a-packgo-file-panels-comfort-panels)
  
[Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-advanced-and-panel-runtime-panels-comfort-panels-rt-advanced)

#### Overview for loading of projects (RT Advanced)

##### Overview

Delta data of the project is automatically compiled before you download it to one or several HMI devices. This always ensures that the latest version of the project is transferred.

##### Connection establishment

Ensure that the device version configured in the engineering system matches the installed Runtime version, otherwise, communication will not be established or will be delayed when the project is loaded.

If the device version does not match the installed Runtime version, you have the following options:

1. Change the device version configured in the engineering system.
2. Install the version of WinCC Runtime Advanced corresponding to the configured device version.

##### Loading a project to an HMI device

The following steps are completed prior to downloading:

1. The download settings are verified. The "Extended download to device" dialog box opens automatically during the initial download of a project to an HMI device. You use this dialog to define the protocol and interface or destination path for the project in accordance with the HMI device Runtime used.

   If the HMI device is part of a subnet, for example, you also select the subnet and the first gateway.

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens.
2. The project is compiled. Warnings and errors during compilation are displayed in the Inspector window and in the "Load preview" dialog box.
3. The "Load preview" dialog box shows you the following information for each HMI device:

   - The individual steps for loading
   - Check the runtime version of the target HMI device  
     If the version of WinCC Runtime Advanced installed on the target device does not match the configured device version, you cannot load the project.
   - Default settings that take effect when loading

     You can change the default settings for this download process, if necessary.
   - Occurring warnings (optional).

     You can download a project while ignoring the "warnings". The functionality may be restricted in runtime.
   - Occurring errors (optional).

     You cannot load the project. WinCC will open the invalid configuration in the corresponding editor if you double-click the error message in the Inspector window. Correct the errors and reload the project.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile the user program before you compile the HMI device.

> **Note**
>
> **Interruption of a download**
>
> If the download is interrupted, WinCC automatically ensures that no data is lost and that existing data is deleted on the HMI device only after complete transmission.

##### Loading a project without a connected HMI device

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to the HMI device.

##### Loading with S7 routing

Configure the S7 routing settings in the "Devices &amp; Networks" editor in the relevant PLC. The settings depend on the device configured.

S7 routing supports the following protocols:

- MPI/PROFIBUS
- PN/IE

##### Transferring Runtime add-ons in WinCC

Projects can contain Runtime add-ons in the form of controls or CSP (Communication Support Packages). These Runtime add-ons are automatically transferred with the project.

---

**See also**

[Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)

#### Loading a project (Panels, Comfort Panels, RT Advanced)

##### Introduction

Before a project can run on an HMI device, you must first load it to the HMI device. During loading, you must most importantly specify whether existing data on the HMI device such as "user administration" and "recipe data" is to be overwritten.

If the HMI device supports PROFINET, the name registered in the project tree is used for the PROFINET communication. The use of the name corresponds to the default settings of the PROFINET interface of the HMI device. For devices with more than one PROFINET interface, the name of the IE CP is automatically added to the device name with a separating period. The name is written to the HMI device during download. If a device name for the PROFINET communication has already been entered in the HMI device, it will be overwritten.

You can find additional information about these settings in the information system in the "Assigning a device name and IP address" section.

If the device version of the target HMI device does not match the configured device version, you are asked whether you wish to change the device version at this time.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the device version deletes all data on the HMI device.**  Data is deleted on the target system if you change the device version. For this reason, you should first back up the following data:  - User administration - Recipes - Licenses   Resetting to factory settings also deletes the license keys. Back up the license keys before you reset the system to factory settings.  With Comfort devices, the licenses can only be deleted when resetting to factory settings. Back up the licenses and license keys before you reset the system to factory settings. |  |

> **Note**
>
> **Transfer to an HMI device with PC station V1.0 or PC station V2.0**
>
> The version of the PC station set in the device settings of the HMI device must match the version installed on the HMI device.
>
> Additional information on configuration settings for "PC Station" on the HMI device is available in the "SIMATIC NET" documentation.

> **Note**
>
> **Overwriting existing data during loading**
>
> During loading, you must specify whether existing data on the HMI device is to be overwritten. By selecting the check boxes in the "Load preview" dialog you can always overwrite the following data during loading:
>
> - Existing user administration data on the device
> - Existing recipe data on the device

##### Establishing a connection to WinCC Runtime Advanced

Ensure that the device version configured in the engineering system matches the installed Runtime version; otherwise, communication when the project is loaded will not be established or will be delayed.

If the device version does not match the installed Runtime version, you have the following options:

1. Change the device version configured in the engineering system.
2. Install the version of WinCC Runtime Advanced corresponding to the configured device version.

> **Note**
>
> If your HMI device is a PC, the device version of the target system is not automatically updated during the download.
>
> Verify that the configured device version corresponds to the one of the target HMI device before you compile and download your project. If necessary, install the matching Runtime version on your HMI device or change the device version manually using the properties of the HMI device.

##### Controlling the transfer behavior on the HMI device

As a general rule, only one project can be active in Runtime on an HMI device. An HMI device is generally configured to exit Runtime automatically when loading is started. If this is not the case, you will have to exit Runtime manually on the HMI device.

You define how the HMI device reacts when the project is loaded in the "Start Center" under "Settings" on the HMI device:

| Transfer mode | Effect |
| --- | --- |
| Off | The project cannot be loaded to the HMI device. |
| Manually | The project can only be loaded to the HMI device if the following requirements are met:  - Runtime is not running - The HMI device is in "Transfer" mode. |
| Automatic | The project can always be loaded to the HMI device.   If a transfer is started on the configuration PC and a project is in runtime on the HMI device, the running project is automatically closed.   For Mobile Panels, this transfer mode is disabled for security reasons. |

> **Note**
>
> **Closing Runtime automatically**
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the "Start Center".

Please refer to the documentation for the HMI device used for more detailed information on transfer settings.

##### Requirement

- You have created an HMI device in the project.
- The HMI device is connected to the configuration PC.
- The "Start Center" has been started on the HMI device.
- The protocol by which the project is loaded is set on the HMI device in the "Start Center" under "Settings".
- Transfer mode is set as "Automatically" or "Manually" in the HMI device.

##### Procedure

Proceed as follows to load a project:

1. To download a project simultaneously to several HMI devices, select the HMI devices by means of multiple selection in the project tree.
2. Select the "Download to device &gt; Software" command from the shortcut menu of an HMI device.
3. If the "Extended download to device" dialog is open, configure the "Settings for loading". Make sure that the "Settings for loading" correspond to the "Transfer settings in the HMI device".

   - Select the protocol used, for example, Ethernet or HTTP.
   - Configure the relevant interface parameters on the configuration PC.
   - Make any interface-specific or protocol-specific settings required in the HMI device.
   - Click "Load".

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens. The project is compiled at the same time. The result is displayed in the "Load preview" dialog box.
4. Check the displayed presettings and change them as necessary.
5. Click "Load".

##### Result

The project is loaded to all selected HMI devices. In WinCC V13, the project with the Runtime add-ons is loaded to the selected HMI devices.

During the download, you can keep track of the files that are transferred.

If errors or warnings occur during the download, corresponding alarms are displayed under "Info &gt; Load" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device.

> **Note**
>
> If the transfer is interrupted, WinCC V13 automatically ensures that no data is lost and that existing data is deleted on the HMI device only after complete transmission.

---

**See also**

[Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)
  
[Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-advanced-and-panel-runtime-panels-comfort-panels-rt-advanced)
  
[Starting Runtime Professional (RT Professional)](#starting-runtime-professional-rt-professional)
  
[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
  
[Installing a USB driver in Windows 7 (Panels, Comfort Panels, RT Advanced)](#installing-a-usb-driver-in-windows-7-panels-comfort-panels-rt-advanced)
  
[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview for loading of projects (RT Advanced)](#overview-for-loading-of-projects-rt-advanced)

#### Generating a "Pack&Go" file (Panels, Comfort Panels)

##### Introduction

Create a "Pack&amp;Go" file if you cannot connect the HMI device to the configuration PC. The "Pack&amp;Go" file is a ZIP file containing the following data:

- The compiled project
- A program for transferring the project to the HMI device
- Image for the configured HMI device

Typical example of an application: An engineering company creates a project variant for a new HMI device. The project engineer of the engineering company does not have direct access to the plant. The project engineer therefore e-mails the "Pack&amp;Go" file to his local contact. The contact unpacks the "Pack&amp;Go" file on a PC connected to the HMI device via a network. He then transfers the project from the PC to the HMI device.

##### Requirement

- You have created an HMI device in the project.

##### Procedure

To create a "Pack&amp;Go" file, follow these steps:

1. Select the HMI device in the project tree.
2. Select the "Pack&amp;Go" command from the menu under "Online &gt; HMI Device maintenance".
3. The "Create Pack&amp;Go file" opens.
4. Verify that the displayed device version corresponds with that of the target HMI device.
5. Select a protocol as transfer mode.
6. Select the storage location under "Pack&amp;Go file" and enter the file name.
7. If necessary, specify if the "Pack&amp;Go" file is split into several files.
8. Click "Create".

> **Note**
>
> To unzip a "Pack&amp;Go" file which is distributed over several files, you need a compression program. The compression program integrated into the operating system is not adequate to unzip distributed files.

##### Result

The "Pack&amp;Go" file is created and saved to the specified folder in the file system. Now copy the "Pack&amp;Go" file to the PC connected to the HMI device.

#### Downloading projects from a "Pack&Go" file to the HMI device (Panels, Comfort Panels)

##### Introduction

Pack&amp;Go is a 64-bit application that can only run on a 64-bit operating system.

If the TIA Portal is not installed on your PC, install Microsoft Visual C++ 2015 Redisitributable Package (x64) and .Net Framework 4.6.1 to run the Pack&amp;Go application.

- You can find the Microsoft Visual C++ 2015 Redistributable Package (x64) in the Download Center of Microsoft at the following URL:  
  http://www.microsoft.com/en-us/download/details.aspx?id=48145
- You can find .Net Framework 4.6.1 at the following URL:   
  https://www.microsoft.com/en-us/download/details.aspx?id=49982

##### Requirement

- .NET Framework with version 4.6.1
- ProSave is installed on the PC
- The "Pack&amp;Go" file has been stored in the file system of a PC.
- The PC is connected to the HMI device.
- The device version of the HMI device is consistent with the device version in the project

> **Note**
>
> To unzip a "Pack&amp;Go" file which is distributed over several files, you need a compression program. The compression program integrated into the operating system is not adequate to unzip distributed files.

##### Procedure

To download the project from a "Pack&amp;Go" file to an HMI device, follow these steps:

1. Unpack the "Pack&amp;Go" file to a folder of your choice in the file system of the PC.
2. From the "PackNGo" subfolder of this directory, run "Siemens.Simatic.Hmi.PackNgo.exe".

   The "Pack'n Go" dialog opens. The settings for loading are set by default. Exception: You must select the target device if you are using an S7 USB connection.
3. Adjust the settings for loading appropriately if they differ from the interfaces or protocols available on the PC.
4. Specify whether or not to overwrite the user management and recipe data already stored on the HMI device.
5. Click "Transfer".

##### Result

The connection to the HMI device is set up via the selected path. An alarm is output if the device version used in the project differs from that of HMI device.

If this is the case, update the operating system on the HMI device. To update the operating system on the HMI device, you need ProSave. A prompt for operating system update will appear automatically if ProSave has been installed and the selected connection supports the update of the operating system.

---

**See also**

[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)

#### Loading via USB interface (Panels, Comfort Panels, RT Advanced)

##### Introduction

When you load a project via a USB port, connect the configuration PC and the HMI device with a USB cable.

##### Requirements for transfer via USB

The following conditions must be met to ensure successful data transfer using a USB port:

- Use a USB host-to-host cable, USB 2.0 standard.
- You have installed the provided USB driver.

  You can find the driver on the WinCC Product DVD under "Support\DeviceDriver\USB".
- The HMI device being used is based on Windows CE and has a USB port.

You can find more information on the cables used and the manufacturers/suppliers in the Internet at:

- [http://support.automation.siemens.com](http://support.automation.siemens.com/WW/view/en/19142034)

  > **Note**
  >
  > **Driver installation**
  >
  > To avoid problems when transferring projects, only use the USB driver provided on the WinCC Product DVD.

  > **Note**
  >
  > **Comfort HMI devices**
  >
  > Use the mini USB port to load projects via USB with Comfort HMI devices. This driver is installed automatically.

##### Restrictions

A project can always be transferred to an HMI device. Simultaneous transfer to several HMI devices is not possible.

---

**See also**

[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)

#### Load project from external storage medium (Panels, Comfort Panels, RT Advanced)

##### Introduction

If you cannot establish a direct connection from the configuration PC to the HMI device, copy the compiled project to an external storage medium, such as a USB stick, a memory card or network folder, and then load it onto your HMI device.

This function is available in connection with an HMI device image which is compatible with the TIA Portal version V14 or higher.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of data**  When you activate the "Firmware upgrade" or "Firmware downgrade" options, then the operating system of the HMI device is updated. Existing data on the HMI device including the HMI device password is deleted. Settings in the Start Center are retained, license keys are saved to the external storage medium before update of the operating system.  If required, save this data before loading. |  |

You create the required project data in WinCC by configuring the HMI device and then dragging and dropping or copying and pasting the folder of the HMI device (e.g. "HMI_1 [&lt;device type&gt;]") to an external storage medium under "Card Reader/USB memory".

##### Requirements

- You have started the Start Center on the HMI device.
- The storage medium with the backed up project is inserted in the HMI device.
- For Runtime Advanced you have manually copied the files to a directory and adjusted the configuration path under "Start Center &gt; Settings".

##### Procedure

1. Click "Settings".
2. Open the "Service &amp; Commissioning" dialog.
3. Select the "Load Project" tab.
4. Press "Next".

   The "Load from external memory device" dialog opens.
5. In the "Accessible devices" group, select the storage medium to which the project data has been backed up.
6. Press "Next".

   An overview of all projects which are compatible with the HMI device and are located on the storage medium is displayed.
7. Select the project that you want to load into the HMI device.
8. Press "Next".

   The HMI device checks whether the project data can be loaded. The result of the check is displayed in the "Load Preview" dialog.

   The project can be loaded to the HMI device if no alarms of the type "Error" are issued.
9. Select "Load", to transfer the project data to the HMI device with the project data.

**Note**

Use "Details" to receive additional information about the selected project.

**Note**

If a downgrade or upgrade is necessary, the "Update OS Image" dialog informs you about the possible loss of data and gives you further instructions.

After the loading process the new project is started on the HMI device.

##### Alarms in the "Load Preview dialog"

The following messages can be displayed in the "Load Preview" dialog:

- Alarms of the type "Information":
- Alarms of the type "Warning", with options
- Alarms of the type "Error", with options

The following table shows alarms of the type "Information":

| Icon | Status | Alarm | Meaning |
| --- | --- | --- | --- |
| ![Alarms in the "Load Preview dialog"](images/94831701771_DV_resource.Stream@PNG-de-DE.png) | Info | Firmware version ... Runtime version ... | Firmware and Runtime version on the HMI device |
| ![Alarms in the "Load Preview dialog"](images/94831701771_DV_resource.Stream@PNG-de-DE.png) | Info | Ready For Loading | Project data is suitable for the HMI device |

The following table shows alarms of the type "Warning", with options:

| Icon | Status | Alarm | Meaning |
| --- | --- | --- | --- |
| ![Alarms in the "Load Preview dialog"](images/94831710219_DV_resource.Stream@PNG-de-DE.png) | Overwrite | Select project data | The following lines contain options for overwriting data on the HMI device. |
| ![Alarms in the "Load Preview dialog"](images/94831889163_DV_resource.Stream@PNG-de-DE.png) |  | Recipes | Overwrite recipes of the HMI device with the recipes of the project (optional).  It is only possible to change this setting if the "Lock the settings on the HMI device?" setting was not activated when loading to the storage medium. |
| ![Alarms in the "Load Preview dialog"](images/94831889163_DV_resource.Stream@PNG-de-DE.png) |  | User administration data | Overwrite the user administration on the HMI device with the user administration of the project (optional).  It is only possible to change this setting if the "Lock the settings on the HMI device?" setting was not activated when loading to the storage medium. |
| ![Alarms in the "Load Preview dialog"](images/94831880715_DV_resource.Stream@PNG-de-DE.png) | Upgrade | Runtime upgrade | Runtime version on the HMI device is older than the Runtime version of the project, versions are compatible, upgrade of Runtime version on the HMI device is optional. |
| ![Alarms in the "Load Preview dialog"](images/94831880715_DV_resource.Stream@PNG-de-DE.png) | Upgrade | Firmware upgrade | Firmware version on the HMI device is older than the firmware version of the project, versions are compatible, upgrade of firmware on the HMI device is optional. |
| ![Alarms in the "Load Preview dialog"](images/94831880715_DV_resource.Stream@PNG-de-DE.png) | Downgrade | Runtime downgrade | Runtime version on the HMI device is newer than the Runtime version of the project, versions are compatible, downgrade of Runtime version on the HMI device is optional. |
| ![Alarms in the "Load Preview dialog"](images/94831880715_DV_resource.Stream@PNG-de-DE.png) | Downgrade | Firmware downgrade | Firmware version on the HMI device is newer than the firmware version of the project, versions are compatible, downgrade of firmware on the HMI device is optional. |

The following table shows alarms of the type "Error", with options:

| Icon | Status | Alarm | Meaning |
| --- | --- | --- | --- |
| ![Alarms in the "Load Preview dialog"](images/94831872267_DV_resource.Stream@PNG-de-DE.png) | Upgrade | Runtime upgrade | Runtime version on the HMI device is older than the Runtime version of the project, versions are incompatible, upgrade of Runtime version on the HMI device is required. |
| ![Alarms in the "Load Preview dialog"](images/94831872267_DV_resource.Stream@PNG-de-DE.png) | Upgrade | Firmware upgrade | Firmware version on the HMI device is older than the firmware version of the project, versions are incompatible, upgrade of firmware on the HMI device is required. |
| ![Alarms in the "Load Preview dialog"](images/94831872267_DV_resource.Stream@PNG-de-DE.png) | Downgrade | Runtime downgrade | Runtime version on the HMI device is newer than the Runtime version of the project, versions are incompatible, downgrade of Runtime version on the HMI device is required. |
| ![Alarms in the "Load Preview dialog"](images/94831872267_DV_resource.Stream@PNG-de-DE.png) | Downgrade | Firmware downgrade | Firmware version on the HMI device is newer than the firmware version of the project, versions are incompatible, downgrade of firmware on the HMI device is optional. |
| ![Alarms in the "Load Preview dialog"](images/94831872267_DV_resource.Stream@PNG-de-DE.png) | Download | Runtime download | There is no Runtime software on the HMI device, e.g. after update of the operating system. Runtime software must be downloaded. |

> **Note**
>
> When loading projects to your HMI device, please note that there are compatible and incompatible firmware and Runtime versions.
>
> If you are loading a compatible firmware and Runtime version of the project to your HMI device, an upgrade or downgrade is optional. You can download the project to the HMI device without an upgrade or downgrade. In this case, you can ignore the alarm of the type "Warning".
>
> If you are loading an incompatible firmware and Runtime version of the project to your HMI device, an upgrade or downgrade is mandatory. Otherwise, you cannot download the project to the HMI device. An alarm of the type "Error" is displayed:

> **Note**
>
> Alarms of the type "Warning" also appear in the event of a potential overwriting of user data and recipes if this setting was not locked in the configuration.

---

**See also**

[Overview for loading of projects (RT Advanced)](#overview-for-loading-of-projects-rt-advanced)
  
[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)

#### Installing a USB driver in Windows 7 (Panels, Comfort Panels, RT Advanced)

##### Introduction

To load a project via the USB port, install the USB drivers provided on the WinCC product DVD.

> **Note**
>
> **Driver installation**
>
> To avoid problems when transferring projects, only use the USB driver provided on the WinCC product DVD.

> **Note**
>
> **Comfort HMI devices**
>
> Use the mini USB port to load projects via USB with Comfort HMI devices. This driver is installed automatically.

##### Requirement

- The WinCC product DVD is available.
- You are using a USB host-to-host cable, USB 2.0 standard.
- The HMI device has a USB port.

##### Procedure

To install the USB driver under Windows 7, follow these steps:

1. Connect the USB host-to-host cable to the PC's USB port.

   The USB cable is detected, but the wizard for the driver installation does not find the driver.
2. Open the Device Manager in the Control Panel.
3. Select "Other devices &gt; USB host-to-host cable".
4. Select "USB host-to-host cable" and then select "Update driver software..." in the shortcut menu.
5. When the "How do you want to search for driver software?" prompt appears, select "Search for driver software on the computer".
6. Click "Update driver software &gt; Browse...".
7. Insert the WinCC product DVD as the source for driver installation.
8. Select "Include subfolders" and then click "Next".

   The system will search the WinCC product DVD for the corresponding driver for the USB host-to-host cable.

   The drivers available on the WinCC product DVD are displayed. The wizard highlights the appropriate driver for Windows 7.
9. Check the selection and click "Next".
10. To continue with the installation, click "Hardware Installation &gt; Continue installation".

    The driver is installed.
11. Click "Finish".

    The installation is complete.

**Note**

Connect the HMI device only when the driver has been completely installed on the PC.

##### Result

The driver required for the USB host-to-host cable has been installed. To load the project, now connect the HMI device to the USB cable.

---

**See also**

[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
  
[Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)

### Compiling and loading with Multiuser Engineering (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Compiling and loading with multiuser engineering (overview) (Panels, Comfort Panels, RT Advanced)](#compiling-and-loading-with-multiuser-engineering-overview-panels-comfort-panels-rt-advanced)
- [Compiling in the server project view (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-server-project-view-panels-comfort-panels-rt-advanced)
- [Compiling in the local session (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-local-session-panels-comfort-panels-rt-advanced)

#### Compiling and loading with multiuser engineering (overview) (Panels, Comfort Panels, RT Advanced)

##### Introduction

When using multiuser engineering for your projects, you should take into account the response when compiling the Runtime projects and the response when downloading them to HMI devices.

You can compile and download to an HMI device in both the server project view and in the local session.

You can find more information about the topic of "multiuser engineering" under "Using Multiuser Engineering".

##### Basics

For HMI devices and RT Advanced, the following scenarios are possible in multiuser engineering:

- Compiling in the server project view
- Compiling in the local session
- Loading from the server project view
- Loading from the local session

> **Note**
>
> Complete download from the server project view or local session is no different to complete download in a single-user project. With a complete download, the current Runtime project is loaded from the currently active view to an HMI device.

> **Note**
>
> Compiling and downloading in a local session is no different from compiling and downloading in a single-user project.

In principle, you can execute all commands for compiling and loading in multiuser engineering projects:

- "Software (rebuild all)"
- "Compile &gt; Software (only changes)"
- Software (all)

**The term "project"**

The term "project" has two different meanings in the contexts of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of one HMI device

##### Rules

The following basic rules apply to compiling and downloading in multiuser engineering:

- The Runtime project that has been compiled in a local session always remains local and is not uploaded to the multiuser server. It cannot be saved in the multiuser server project.
- Only Runtime projects compiled in the server project view can be saved in the multiuser server project.

You can find additional information on Multiuser Engineering on the Siemens YouTube channel: [Multiuser Engineering - one team working simultaneously on a project](https://www.youtube.com/watch?v=n4oTZ2Gzg6U).

---

**See also**

[Compiling in the server project view (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-server-project-view-panels-comfort-panels-rt-advanced)
  
[Compiling in the local session (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-local-session-panels-comfort-panels-rt-advanced)

#### Compiling in the server project view (Panels, Comfort Panels, RT Advanced)

##### Basics

Compiling and downloading in the server project view is no different from compiling and downloading in a single-user project.

During the compiling of a project in the server project view, the multiuser server project is blocked. Other users cannot make changes to this server project during this time. The Runtime project compiled in the server project view is stored along with the engineering project in the central multiuser server. Blocking the multiuser server project ensures that the configuration data and the Runtime project remain in sync.

> **Note**
>
> When you compile and save in the server project view, other users obtain the Runtime project you have updated along with the engineering project when they "refresh" their local session. Other users do not have to recompile the changes you have made after an update.

##### Example: **Compiling during check-in**

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

If there are no compilation errors, both projects - the modified engineering project (with the modified tags) and the compiled Runtime project - are saved in the central multiuser server project with the "Save changes" command.

If you skip compiling during the check-in, the project contains the changes that have been saved on the server.

The next user who creates a local session from the server project or updates an existing local session must compile your two changes in addition to his or her own changes.

> **Note**
>
> Working on a shared project through multiple local sessions increases the probability of error. It is therefore recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors.

---

**See also**

[Compiling and loading with multiuser engineering (overview) (Panels, Comfort Panels, RT Advanced)](#compiling-and-loading-with-multiuser-engineering-overview-panels-comfort-panels-rt-advanced)
  
[Compiling in the local session (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-local-session-panels-comfort-panels-rt-advanced)

#### Compiling in the local session (Panels, Comfort Panels, RT Advanced)

##### **Basics**

Compiling and downloading projects in the local session is no different from compiling and downloading in a single-user project.

Since the local session is a copy of the server project, the first compilation status of the local session is identical to that of the server project. If the server project contains contents that are not compiled or error messages occurred during the compiling, they are transferred to the local session.

> **Note**
>
> It is recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors and avoid spreading errors.

##### **Updating in the** **local session**

If you update a project in the local session, the local session - including the compilation status - is completely replaced by the content of the server project. Only the changes marked for check-in are retained in the updated local session and generate additional compiling steps in the local session.

##### Example: Updating the local session

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

You update the content of the local session by clicking the "Update" button. After the update, the local session obtains the compilation status of the server project. There are also compiling tasks for the acquisition of the modified tags.

---

**See also**

[Compiling and loading with multiuser engineering (overview) (Panels, Comfort Panels, RT Advanced)](#compiling-and-loading-with-multiuser-engineering-overview-panels-comfort-panels-rt-advanced)
  
[Compiling in the server project view (Panels, Comfort Panels, RT Advanced)](#compiling-in-the-server-project-view-panels-comfort-panels-rt-advanced)

### Starting Runtime (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)
- [Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-advanced-and-panel-runtime-panels-comfort-panels-rt-advanced)

#### Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can start a project in Runtime on the configuration PC if Runtime has been installed. The project settings defined in the "Runtime settings" of the HMI device are activated when the project is started in Runtime.

> **Note**
>
> You can only simulate HMI devices with Runtime Panels on the configuration PC. Select the "Online &gt; Start simulation" menu command.

> **Note**
>
> **Exiting Runtime automatically**
>
> If automatic transfer is activated on the HMI device and if a transfer is started on the configuration PC, the running project is automatically ended.
>
> The HMI device then switches autonomously to the "Transfer" operating mode.
>
> Deactivate automatic transfer after the commissioning phase so that the HMI device does not inadvertently go into transfer mode.
>
> Transfer mode can cause undesired reactions in the system.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the Start Center.

##### Requirement

- A project is open on the configuration PC.
- Runtime is installed on the configuration PC.
- There is no project in Runtime on the configuration PC.

##### Procedure

To start runtime on the configuration PC, follow these steps:

1. Select the desired HMI device in the project navigation.
2. Select the "Online &gt; Start Runtime" menu command.

##### Result

Runtime is started and the project is displayed on the configuration PC.

---

**See also**

[Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-advanced-and-panel-runtime-panels-comfort-panels-rt-advanced)
  
[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)

#### Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can start the project in Runtime as soon as you have downloaded the project to the HMI device. The project is generally started automatically on the HMI device.

There may be several projects in the file system of the HMI device for HMI devices with Runtime Advanced. You can start one of these projects in Runtime.

The project settings defined in the "Runtime settings" of the HMI device are activated when the project is started in Runtime. Make sure when defining the Runtime settings "Lock task switching" and "Full screen" that you will be able to stop Runtime again. You can, for example, configure a button with the system function "StopRuntime".

> **Note**
>
> **Closing Runtime automatically**
>
> If automatic transfer is activated on the HMI device and a transfer is started on the configuration PC, the running project is automatically terminated.
>
> The HMI device then automatically switches to "Transfer" operating mode.
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> In order to restrict access to the transfer settings and thus avoid unauthorized changes, enter a password in the "Start Center".

> **Note**
>
> **Using encrypted communication connections in Runtime**
>
> A Runtime project with encrypted communication connections to S7 PLCs must be loaded for each Windows user who wants to use these connections in Runtime.

##### Requirements

- WinCC Runtime Advanced or Panel Runtime is installed on the HMI device.
- The project was downloaded to the HMI device.
- The "Start Center" has been started.

##### Starting Runtime on a PC

The compiled project is saved in the PC file system with the extension "*.fwc" and is freely accessible.

1. Enter the project file with complete path information in the "Start C​​enter" under "Settings &gt; Configuration path".
2. To start the project automatically after booting the HMI device:

   - Select the required delay time in seconds under "Wait until Autostart".
   - Add the "Start Center" application to the "Autostart" group in the Windows Start menu.
3. Click on "Start" in the "Start Center" to manually start the project in the HMI device.

##### Starting Runtime on a panel

The project is stored on a panel in a folder you specify in the HMI device transfer settings. The "Start Center" application is started on a panel. The project loaded is started automatically after expiration of the configured delay.

If the project does not start automatically:

1. Click on "Start" in the "Start Center" to start the loaded project.

Refer to the documentation for the HMI device for additional information on startup of projects.

##### Result

Runtime is started on the HMI device.

---

**See also**

[Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)

### Error messages during loading of projects (Panels, Comfort Panels, RT Advanced)

#### Possible problems during the download

When a project is being downloaded to the HMI device, status messages regarding the download progress are displayed in the output window.

Usually, problems arising during the download of the project to the HMI device are caused by one of the following errors:

- Wrong operating system version on the HMI device
- Incorrect download settings on the HMI device
- Incorrect HMI device type in the project
- The HMI device is not connected to the configuration PC.

The most common download failures and possible causes and remedies are listed below.

#### The serial download is cancelled

Possible remedy: Select a lower baud rate.

#### The download is cancelled due to a compatibility conflict

| Possible cause | Remedy |
| --- | --- |
| Conflict between versions of the configuration software and the operating system of the HMI device | Synchronize the operating system of the HMI device with the version of the configuration software.  To update the operating system on the HMI device, select the "Update operating system" command from the "Online &gt; HMI device maintenance" menu in WinCC. You can also use ProSave.   For additional information, refer to the operating instructions for the HMI device. |
| The configuration PC is connected to the wrong device, e.g. a controller. | Check the cabling.   Correct the communication parameters. |

#### Project download fails

| Possible cause | Remedy |
| --- | --- |
| Connection to the HMI device cannot be established (alarm in the output window) | Check the physical connection between the configuration PC and the HMI device.   Check whether the HMI device is in transfer mode. Exception: Remote control |
| The default communication driver is not listed in the Windows Device Manager. | Check the device status of the COM connection in the properties window of the Device Manager. |

#### Download over MPI/DP interface fails

| Possible cause | Remedy |
| --- | --- |
| "Configured mode" is set on the CP, for example, if you are using the SIMATIC NET CD. | Set the CP to "PG mode" using the "Set PC station" application.  Check the "baud rate" and "MPI address" network parameters.  Download the project from WinCC to the CP.  Set the CP back to "configured mode". |
| On the programming device/PC panel, the "S7ONLINE" access point is not set to a hardware device such as CP5611 (MPI). This may be due to the installation of "SIMATIC NET CD". | Set the access point "S7ONLINE" on the selected device using the "PG/PC Panel" or "Set PC station" application.  Check the "baud rate" and "MPI address" network parameters.  Download the project from WinCC to the HMI device.  Restore the "S7ONLINE" access point to the original device. |

#### The configuration is too complex

| Possible cause | Remedy |
| --- | --- |
| The configuration contains too many different objects or options for the HMI device selected. | Remove all objects of a specific type, for example all HTML browsers.  Alternatively, remove options such as Sm@rtServer or OPC server. |

---

**See also**

[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)
  
[Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)

### Adapting the project for another HMI device (Panels, Comfort Panels, RT Advanced)

#### Introduction

When you download a WinCC project to an HMI device, WinCC checks whether this is compatible with the HMI device type used in the project. If the types of HMI device do not match, you will see a message before the download starts.

The download is aborted.

#### Adapting the project for the HMI device

You need to adapt the project accordingly to be able to download the project to the connected HMI device.

- Add a new HMI device in the project tree. Select the correct type of HMI device from the HMI device selection.
- Copy the configured components from the previous to the new HMI device.

  Copy large amounts of components directly in the project navigation and details view.

  For example, copy the "Screens" folder to the screens folder of the new HMI device with the help of the shortcut menu.
- Use the detail view to copy entries in the project tree for which the "Copy" command is not available in the shortcut menu.
- Select the "Recipes" entry in the project tree, for example. The recipes are displayed in the detail view.
- Select the recipes in the detail view and drag them to the "Recipes" entry of the new HMI device. The recipes are copied. You can also select multiple objects in the detail view.
- Configure the components that cannot be copied, e.g. connections, area pointers, and alarms.
- Save the project at various points in time.
- Compile the full project.
- When the compilation is successfully completed, download the project to the HMI device.

#### Linking references

References to linked objects are included in the copying. The references are linked again once the linked objects are copied.

Example:

You copy a screen in which objects are linked to tags. The tag names are entered at the individual objects after the screen is added to the new HMI device. The tag names are marked in red because the references are open. When you then copy the tags and insert them into the new HMI device, the open references are closed. The red marking for the tag names disappears.

For complete references to connected objects in the PLC, you first need to configure a connection to the PLC.

#### Using the information area

When you compile the project for the HMI device, errors and warnings are displayed in the "Info" tab of the Inspector window. You can use the shortcut menu command "Go to" to go directly to the location where the error or warning can be corrected.

Work through the list of errors and warnings from top to bottom.

When the compilation is successfully completed, download the project to the HMI device.

---

**See also**

[Loading a project (Panels, Comfort Panels, RT Advanced)](#loading-a-project-panels-comfort-panels-rt-advanced)

### Reducing the project size (Panels, Comfort Panels, RT Advanced)

#### Introduction

When loading a large-scale project to an HMI device, the memory of the HMI device may be insufficient for the project. There are several ways to reduce the size of your project.

#### Options for reducing the project size

There are several ways to reduce the size of the project and save space:

- Reduce the number of available Runtime languages

  Check whether all selected Runtime languages are actually needed. You can disable the languages that you do not need under "Runtime settings &gt; Language &amp; Font &gt; Runtime language and font selection".
- Do not use help texts for S7 diagnostic alarms

  To reduce the size of the project, you can disable the download of help texts for the S7 diagnostic alarms. In order to avoid downloading the help texts to the HMI device, disable the option "Download S7 diagnostics help texts" under "Runtime settings &gt; Alarms &gt; General".
- Rebuild all software

  In order to optimize the project data and to clean up obsolete changes, compile the entire project using the "Compile &gt; Software (rebuild all)" command from the shortcut menu of the HMI device.
- Harmonize the presentation using styles (as of WinCC V13)

  It is recommended to harmonize screen objects using styles. Standardize the appearance of screen objects in a project to optimize project data. Use the specified preset or customized style for the configuration of the screen objects throughout the project.
- Enable automatic update of PLC alarms (for S7-1500 controllers and V14 HMI devices)

  To save space, you can specify that the PLC alarm texts are only to be loaded in Runtime when needed. To do this, enable the "Automatic update" option under "Runtime settings &gt; Alarms &gt; Controller alarms". Make sure that automatic update of alarms is also enabled in the corresponding controller.

  The "Automatic update" option is not available on Basic Panels.

  The amount of space that can be saved depends on the number of PLC alarms and the number of Runtime languages.
- Reduce the number of fonts loaded

  Check whether the number of downloaded user-defined fonts can be reduced. If necessary, configure only the standard fonts for the required Runtime languages under "Runtime settings &gt; Language &amp; font &gt; Runtime language and font selection".

  To save space, use fewer font groups for the configuration.
- Reduce the size of the graphics

  Check the size of the graphics that you use in the project. If necessary, reduce the size of the graphics by reducing the resolution or choose a higher compression format without noticeable loss of quality for the project graphics.

  To keep the project size small for Basic HMI devices, harmonize the sizes of graphics used in the project.

  Select appropriate graphic formats for your screens: For example, use PNG images for drawings that are not vector graphics and JPEG images for photos.

### Supported network cameras and settings (Panels, Comfort Panels, RT Advanced)

#### Recommended cameras and settings

In the "Camera view" object you display screens of a connected network camera on your HMI device. Use the "Camera view" object with the network cameras which support the streaming protocol RTP/RTPS and codecs MJPEG, H.264 and MPEG4.

Depending on the camera and HMI device, the settings which provide the optimum image quality vary.

> **Note**
>
> **Device dependency of the "Camera view" object**
>
> The "Camera view" object is available for Comfort Panels, KTP Mobile Panels (as of device version V13) and RT Advanced.

The following tables show you the settings for the tested cameras and the resulting recommendations for optimum display in the "Camera view" object:

**Siemens CCMS2025**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- |
| Codec | MJPEG | MJPEG | MPEG-4 | H.264 | H.264 | MJPEG |
| Resolution of camera view | 320x240 | 320x240 | 640x480 | 640x480 | 320x240 | 800x600 |
| Camera resolution | 320x240 | 320x240 | 640x480 | 640x480 | 320x240 | 800x600 SVGA |
| Frame rate (fps) | 10 | 10 | 10 | 10 | 10 | Not relevant |
| Screen delay (seconds) | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable | Suitable | Suitable | Suitable | Suitable | Suitable |

**AXIS M1011**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- |
| Codec | MJPEG | H.264/MJPEG | H.264 | MJPEG | MJPEG | MJPEG |
| Resolution of camera view | 320x240 | 320x240 | 640x480 | 640x480 | 480x360 | 640x480 |
| Camera resolution | 320x240 | 320x240 | 640x480 | 640x480 | 480x360 | 640x480 |
| Frame rate (fps) | 10 | 10 | 10 | 10 | 10 | Not relevant |
| Screen delay (seconds) | &gt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable with restrictions | Suitable | Suitable | Suitable | Suitable | Suitable |

**AXIS M1013**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- |
| Codec | MJPEG | MJPEG | MJPEG | MJPEG | MJPEG | MJPEG |
| Resolution of camera view | 320x240 | 320x240 | 800x600 | 800x600 | 480x360 | 800x600 |
| Camera resolution | 320x240 | 320x240 | 800x600 | 800x600 | 480x360 | 800x600 |
| Frame rate (fps) | 10 | 10 | 10 | 10 | 10 | Not relevant |
| Screen delay (seconds) | &lt;1 | &lt;1 | &gt;1 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable | Suitable | Suitable with restrictions | Suitable | Suitable | Suitable |

**D-Link DCS-942L**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- |
| Codec | MJPEG | MJPEG | MJPEG | MJPEG | MPEG4 | MPEG4 |
| Resolution of camera view | 320x240 | 320x240 | 320x240 | 640x480 | 320x240 | 640x480 |
| Camera resolution | 320x240 | 320x240 | 320x240 | 640x480 | 320x240 | 640x480 |
| Frame rate (fps) | 10 | 10 | 10 | 10 | 10 | Not relevant |
| Screen delay (seconds) | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable | Suitable | Not suitable | Suitable | Suitable | Suitable |

**D-Link 4701E**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' |  | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codec | H.264 | MJPEG | H.264/MJPEG | H.264 | MJPEG | MJPEG | MJPEG |
| Resolution of camera view | 320x240 | 320x240 | 320x240 | 640x480 | 640x480 | 320x240 | 960x720 |
| Camera resolution | 320x240 | 320x240 | 320x240 | 640x480 | 640x480 | 320x240 | 960x720 |
| Frame rate (fps) | 25 | 25 | 25 | 7 | 25 | 25 | Not relevant |
| Screen delay (seconds) | &lt;1 | &lt;1 | &lt;1 | &lt;2 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable | Suitable | Suitable | Suitable | Suitable | Suitable | Suitable |

**D-Link DCS-4201**

|  | Comfort Panels 15'' - 22'' | RT Advanced |
| --- | --- | --- |
| Codec | MJPEG | MJPEG |
| Resolution of camera view | 640x480 | 960x720 |
| Camera resolution | 640x480 | 960x720 |
| Screen delay (seconds) | &lt;1 | &lt;1 |
| Quality | Standard | Standard |
| Recommendation with panel | Suitable | Suitable |

**TL-SC2020**

|  | RT Advanced |
| --- | --- |
| Codec | MJPEG |
| Resolution of camera view | 640x480 |
| Camera resolution | 640x480 |
| Screen delay (seconds) | &lt;1 |
| Quality | Standard |
| Recommendation with panel | Suitable |

**VANDERBILT CCMW3025**

|  | Comfort Panels 4'' | Mobile F Panels 4'' | Comfort Panels 7'' - 12'' | Comfort Panels 15'' - 22'' | KTP Mobile Panels 7'' - 9'' | RT Advanced |
| --- | --- | --- | --- | --- | --- | --- |
| Codec | H.264 | MJPEG | MJPEG | MJPEG | MJPEG | MJPEG |
| Resolution of camera view | 320x240 (QVGA) | 320x240 (QVGA) | 640x480 | 1280x720 | 640x480 (VGA) | 1280x720 |
| Camera resolution | 320x240  (QVGA) | 320x240 (QVGA) | 320x240 | 1280x720 | 640x480 (VGA) | 1280x720 |
| Frame rate (fps) | 5 | 5 | 5 | 5 | 5 | 5 |
| Screen delay (seconds) | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 | &lt;1 |
| Quality | Standard | Standard | Standard | Standard | Standard | Standard |
| Recommendation with panel | Suitable | Suitable | Suitable | Suitable | Suitable | Suitable |

> **Note**
>
> **Test results**
>
> The optimum settings for RT Advanced were determined in tests on an IPC427D with the Windows 7 Ultimate operating system and cameras with default settings.
>
> The test results are configuration-specific and depend on the hardware, operating system and installed codecs.
>
> You may be able to obtain the missing codecs from the camera manufacturer, for example.

> **Note**
>
> The "Camera view" object can only be used with network cameras and will not work with USB cameras. The ITP1000 camera integrated into the tablet PC can not be used with RT Advanced.

### Viewing memory card data (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels)](#basics-panels-comfort-panels)
- [Working with backups (Panels, Comfort Panels, RT Advanced)](#working-with-backups-panels-comfort-panels-rt-advanced)

#### Basics (Panels, Comfort Panels)

##### Introduction

WinCC provides you with the possibility of viewing data stored on your memory card. The function supports the use of memory cards of the HMI device and of the CPU.

You have the following options:

[Viewing a backup](#viewing-a-backup)

[Renaming and deleting backups](#renaming-and-deleting-backups)

[Viewing HMI device images](#viewing-hmi-device-images-panels-comfort-panels-rt-advanced)

[Deleting HMI device images](#deleting-hmi-device-images-panels-comfort-panels-rt-advanced)

[Creating HMI device images on memory card](#creating-hmi-device-images-on-memory-card-panels-comfort-panels-rt-advanced)

---

**See also**

[Viewing a backup](#viewing-a-backup)
  
[Renaming and deleting backups](#renaming-and-deleting-backups)
  
[Viewing HMI device images (Panels, Comfort Panels, RT Advanced)](#viewing-hmi-device-images-panels-comfort-panels-rt-advanced)
  
[Deleting HMI device images (Panels, Comfort Panels, RT Advanced)](#deleting-hmi-device-images-panels-comfort-panels-rt-advanced)
  
[Creating HMI device images on memory card (Panels, Comfort Panels, RT Advanced)](#creating-hmi-device-images-on-memory-card-panels-comfort-panels-rt-advanced)

#### Working with backups (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Viewing a backup](#viewing-a-backup)
- [Renaming and deleting backups](#renaming-and-deleting-backups)

##### Viewing a backup

###### Introduction

The backup of a Basic Panel that is stored on a memory card can also be viewed in the TIA Portal.

###### Requirements

- WinCC is installed.
- A memory card with a backup is available.
- The card reader is connected to the configuration PC.
- The project view is open.

###### Backup on the memory card in the card reader

1. Insert the memory card into the card reader.
2. Open "SIMATIC Card Reader" in the project navigation.
3. Select the card reader drive.

   The "Online Card Data" folder is displayed.
4. Open the "Online Card Data" folder
5. Click the backup to open the shortcut menu.
6. Select "Properties".

###### Backup on the memory card of the PLC

Proceed as follows if the backup is stored on the memory card of the PLC:

1. Connect the PLC with the configuration PC.
2. Click on the PLC in the project navigation.
3. Select "Connect online" from the shortcut menu.

   A connection to the PLC is established.

   Once the PLC is connected, the "Online Card Data" folder is displayed.
4. Open the "Online Card Data" folder.

   > **Note**
   >
   > **Accessing a password-protected PLC**
   >
   > When you attempt to access a PLC that is protected by a password, you will be prompted to enter the password.
   >
   > You need at least read access rights in order to view the data that is stored on the memory card.
5. Click the backup to open the shortcut menu.
6. Select "Properties".

###### Result

The backup properties are displayed in a separate dialog.

![Result](images/53550178059_DV_resource.Stream@PNG-en-US.png)

##### Renaming and deleting backups

###### Introduction

You can rename and delete backups from a memory card in the project navigation of the TIA Portal.

###### Requirements

- WinCC is installed.
- The card reader is connected to the configuration PC.

  Or The PLC is connected online with the configuration PC.
- A memory card with a backup is available.
- The project view is open.
- The backup is displayed in the project navigation.

  > **Note**
  >
  > **Accessing a password-protected PLC**
  >
  > When you attempt to access a PLC that is protected by a password, you will be prompted to enter the password.
  >
  > You need write access rights to rename or delete memory card data.

###### Procedure

1. Click on the backup in the project navigation.
2. Open the shortcut menu.
3. Select "Rename" to rename the file.
4. Enter a new name.
5. Select "Delete" to delete the file.

###### Result

The backup file is now renamed or deleted.

### Working with HMI device images (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Viewing HMI device images (Panels, Comfort Panels, RT Advanced)](#viewing-hmi-device-images-panels-comfort-panels-rt-advanced)
- [Deleting HMI device images (Panels, Comfort Panels, RT Advanced)](#deleting-hmi-device-images-panels-comfort-panels-rt-advanced)
- [Creating HMI device images on memory card (Panels, Comfort Panels, RT Advanced)](#creating-hmi-device-images-on-memory-card-panels-comfort-panels-rt-advanced)
- [HMI device images V15 and higher (Panels, Comfort Panels, RT Advanced)](#hmi-device-images-v15-and-higher-panels-comfort-panels-rt-advanced)

#### Viewing HMI device images (Panels, Comfort Panels, RT Advanced)

##### Introduction

The HMI device image of a Comfort Panel that is stored on a memory card can be viewed in the TIA Portal.

##### Requirements

- WinCC is installed.
- The card reader is connected to the configuration PC.
- A memory card with the HMI device image is available.
- The project view is open.

##### Procedure

1. Insert the memory card into the card reader.
2. Open "SIMATIC Card Reader" in the project navigation.
3. Select the card reader drive.

   The "Online Card Data" dialog is displayed.
4. Open the "Online Card Data" folder.

   The available images of the HMI device are displayed in additional folders.
5. Click the required HMI device image.
6. Select "Properties" in the shortcut menu.

##### Result

The properties of the HMI device image are displayed in a separate dialog.

![Result](images/111986688139_DV_resource.Stream@PNG-en-US.PNG)

---

**See also**

[HMI device images V15 and higher (Panels, Comfort Panels, RT Advanced)](#hmi-device-images-v15-and-higher-panels-comfort-panels-rt-advanced)

#### Deleting HMI device images (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can delete the HMI device image of a Comfort Panel from a memory card in the project navigation of the TIA Portal.

##### Requirements

- WinCC is installed.
- The card reader is connected to the configuration PC.
- A memory card with an HMI device image is available.
- The project view is open.
- The HMI device image is displayed in the project navigation.

##### Procedure

1. Click the HMI device image in the project navigation.
2. Open the shortcut menu.
3. Select "Delete" to delete the file.

##### Result

The HMI device image is deleted.

---

**See also**

[HMI device images V15 and higher (Panels, Comfort Panels, RT Advanced)](#hmi-device-images-v15-and-higher-panels-comfort-panels-rt-advanced)

#### Creating HMI device images on memory card (Panels, Comfort Panels, RT Advanced)

##### Introduction

You may edit the HMI device image of a Comfort Panel without connecting the Comfort Panel to the configuration PC.

Simply create the HMI device image on an external memory card or USB stick and then transfer it from there to the Comfort Panel.

##### Requirements

- WinCC is installed.
- The card reader is connected to the configuration PC.
- The project view is open.

##### Procedure

1. Insert the memory card into the card reader.
2. Click on the memory card in the project navigation.
3. Open the shortcut menu.
4. Select "Create HMI OS image on memory card".

   A dialog opens.

   ![Procedure](images/75063049739_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/75063049739_DV_resource.Stream@PNG-en-US.png)
5. Select an HMI device image.
6. Select the settings for the restoration.

   - Activate "Retain installed settings of the Control Panel"

     The settings you have made on the Comfort Panel are retained.
   - Activate "Retain installed licenses":

     The licenses on the Panel are retained.
   - Activate "Lock settings on the Panel"

     You can no longer change the selected settings for "Retain installed settings of the Control Panel" and "Retain installed licenses" on the Comfort Panel.

##### Result

You have created an HMI device images on memory card. You may use a USB stick instead of a memory card.

---

**See also**

[HMI device images V15 and higher (Panels, Comfort Panels, RT Advanced)](#hmi-device-images-v15-and-higher-panels-comfort-panels-rt-advanced)

#### HMI device images V15 and higher (Panels, Comfort Panels, RT Advanced)

##### Introduction

As TIA Portal V15 and higher not all HMI device images of the previous versions are included in the standard WinCC installation. This helps us reduce the size of the TIA Portal installation package and the subsequent updates compared to the previous versions. The HMI device images that are no longer included in the WinCC installation are supplied on two additional DVDs, DVD 1 and DVD 3, and can be installed at any time.

You also have the option of downloading the respective HMI device image for installation from the [SIOS](https://support.industry.siemens.com/cs/ww/en/).

##### Availability of the HMI device images

The following table shows the availability of the HMI device images in combination with the device version:

| HMI devices | V12.0 | V13.0 | V13.0.1 | V13.0.2 | V14.0 | V14.0.1 | V15.0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Basic Panels | DVD 1 | - | - | - | - | - | - |
| Mobile Panels | DVD 1 | - | - | - | - | - | - |
| Basic Panels 2nd Generation | - | DVD 3 | DVD 3 | DVD 3 | DVD 3 | DVD 1 | DVD 1 |
| 2nd Generation Mobile Panels | - | - | DVD 3 | DVD 3 | DVD 3 | DVD 1 | DVD 1 |
| Comfort Panels | DVD 1 | DVD 3 | DVD 3 | DVD 3 | DVD 3 | DVD 1 | DVD 1 |

##### Installation options

Note the following options available for selection when installing TIA Portal:

- "SIMATIC WinCC Panel Images (current)": Can be selected during installation of DVD 1
- "SIMATIC WinCC Legacy Panel Images for V15.0": Can be selected during installation of DVD 3

The following table shows the availability of the device versions in combination with the two options that can be selected during installation:

| DVD | Installation option | Available device version |
| --- | --- | --- |
| DVD 1 | "SIMATIC WinCC Panel Images (current)" activated | V12.0, V14.01., V15.0 |
| DVD 1 | "SIMATIC WinCC Panel Images (current)" deactivated | V12.0 |
| DVD 1 and DVD 3 | "SIMATIC WinCC Panel Images (current)" deactivated  "SIMATIC WinCC Legacy Panel Images for V15.0" activated | V12.0, V13.0, V13.0.1, V14.0, V14.0.1, V15 |
| DVD 1 and DVD 3 | "SIMATIC WinCC Panel Images (current)" activated  "SIMATIC WinCC Legacy Panel Images for V15.0" deactivated | V12.0, V13.0, V13.0.1, V14.0 |

If the respective HMI device image was not installed during installation of WinCC, the following actions can only be executed after the missing HMI device image has been installed:

- Create a "Pack&amp;Go" file for the respective HMI device.
- Trigger an OS update for the respective HMI device.
- Download a project offline from a USB data storage medium to the respective HMI device.
- Download a project to the respective HMI device.
- Create an HMI device image on the memory card for the respective HMI device.

An alarm informs you that the missing HMI device image must be installed first.

---

**See also**

[Viewing HMI device images (Panels, Comfort Panels, RT Advanced)](#viewing-hmi-device-images-panels-comfort-panels-rt-advanced)
  
[Deleting HMI device images (Panels, Comfort Panels, RT Advanced)](#deleting-hmi-device-images-panels-comfort-panels-rt-advanced)
  
[Creating HMI device images on memory card (Panels, Comfort Panels, RT Advanced)](#creating-hmi-device-images-on-memory-card-panels-comfort-panels-rt-advanced)

### Basics of operating in Runtime (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Overview (Panels, Comfort Panels, RT Advanced)](#overview-panels-comfort-panels-rt-advanced)
- [Operation with the touch screen (Panels, Comfort Panels, RT Advanced)](#operation-with-the-touch-screen-panels-comfort-panels-rt-advanced)
- [Operation with keys (Panels, Comfort Panels, RT Advanced)](#operation-with-keys-panels-comfort-panels-rt-advanced)
- [Navigating in the display (BS) (Panels, Comfort Panels, RT Advanced)](#navigating-in-the-display-bs-panels-comfort-panels-rt-advanced)
- [Triggering an action (Panels, Comfort Panels, RT Advanced)](#triggering-an-action-panels-comfort-panels-rt-advanced)
- [Entering a value (Panels, Comfort Panels, RT Advanced)](#entering-a-value-panels-comfort-panels-rt-advanced)
- [Moving operator controls (Panels, Comfort Panels, RT Advanced)](#moving-operator-controls-panels-comfort-panels-rt-advanced)
- [Displaying infotext (Panels, Comfort Panels, RT Advanced)](#displaying-infotext-panels-comfort-panels-rt-advanced)
- [Changing Runtime language (Panels, Comfort Panels, RT Advanced)](#changing-runtime-language-panels-comfort-panels-rt-advanced)
- [Web browser of WebKit engine: Overview (Panels, Comfort Panels)](#web-browser-of-webkit-engine-overview-panels-comfort-panels)

#### Overview (Panels, Comfort Panels, RT Advanced)

##### Operating options for an HMI device

Depending on your HMI device, operate your plant as follows:

- Operation with the touch screen

  The display of the device is touch-sensitive. You operate the operating elements in the display with your finger or a stylus.
- Operation with control keys and function keys

  Control keys and function keys are integrated into the housing of the device.

  - Control keys have a specified function, for example, navigation or the acknowledgment of alarms.
  - Function keys are freely user-assignable and their function is therefore project-specific.
- Mouse and keyboard operation

  You connect the mouse and keyboard to the HMI device and operate the operating elements in the display as with a PC.

##### Individually configured operation

The configuration engineer has various options available for setting up operation.

Examples of actions whose execution is always determined on a project-specific basis:

- Screen change
- Reporting
- Changing Runtime language

There are no specific operating elements to execute certain functions. The configuration engineer specifies the project-specific execution. A screen change can be triggered with a button or a function key, for example.

Information on project-specific operations can be found in the system documentation.

#### Operation with the touch screen (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Overview of operation with the touch screen (Panels, Comfort Panels, RT Advanced)](#overview-of-operation-with-the-touch-screen-panels-comfort-panels-rt-advanced)
- [Screen keyboard (RT Advanced)](#screen-keyboard-rt-advanced)
- [Using multi-touch functions (Panels, Comfort Panels, RT Advanced)](#using-multi-touch-functions-panels-comfort-panels-rt-advanced)

##### Overview of operation with the touch screen (Panels, Comfort Panels, RT Advanced)

Use the touch screen to operate the HMI device of the project that is running on your HMI device.

###### Operating the touch screen

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to the touch screen**  Do not touch the touch screen with sharp or pointed objects.   Avoid tapping the touch screen with hard objects, and avoid constantly using motion control.   Both can significantly reduce the useful life or even cause the failure of the touch screen.  **Triggering unintended actions**  You can trigger unintended actions if you touch several operating elements at the same time. Always touch only one operating element on the screen.  Operating elements are touch-sensitive symbols on the screen of the HMI device. |  |

###### Special features of operation using the touch screen

Operation with the touch screen is characterized by the following special features:

- Enable

  To enable an operator control, touch the touch screen with your fingers or with a stylus. To generate a double-click, touch the operator control twice in rapid succession.
- Value input

  You enter numbers and letters on the touch screen with a screen keyboard.
- Careful operation

  If you touch multiple operator controls at the same time, you may trigger unintentional actions.

###### Value input using the screen keyboard

The screen keyboard is displayed as soon as you operate a screen object that requires an input. Depending on the HMI device and the configured operating element, the system displays different screen keyboards for entering numerical or alphanumerical values. The screen keyboard is hidden again when input is complete.

###### File browser (Windows 8 or higher)

You can only operate the file browser dialog with a mouse, keyboard or on-screen keyboard (without using the touch function) on a Windows 8 or higher PC with touch screen. Use the file browser dialog of the Windows operating system with the help of a script on a touch screen PC with Windows 8 or higher.

##### Screen keyboard (RT Advanced)

###### Layout

The following figure shows the principal structure of a screen keyboard on a Runtime Advanced HMI device.

###### Alphanumeric screen keyboard

![Alphanumeric screen keyboard](images/47673100683_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Language switching**
>
> Language switching in the project has no influence on the alphanumerical screen keyboard. The entry of Cyrillic or Asian characters is therefore not possible.

###### Numerical screen keyboard

![Numerical screen keyboard](images/47673091595_DV_resource.Stream@PNG-de-DE.png)

###### Operator controls

The following keys are available on the screen keyboard of all HMI devices:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/68892650379_DV_resource.Stream@PNG-de-DE.png) | Cursor left | Navigates to the left |
| ![Operator controls](images/68892653707_DV_resource.Stream@PNG-de-DE.png) | Cursor right | Navigates to the right |
| ![Operator controls](images/68892657035_DV_resource.Stream@PNG-de-DE.png) | Backspace | Deletes a character |
| ![Operator controls](images/68892660363_DV_resource.Stream@PNG-de-DE.png) | Escape | Cancels the input |
| ![Operator controls](images/68902289291_DV_resource.Stream@PNG-de-DE.png) | Enter | Confirms the input |
| ![Operator controls](images/68902292619_DV_resource.Stream@PNG-de-DE.png) | Help | Displays the infotext  This key is only displayed when an infotext has been configured for the operator control. |

##### Using multi-touch functions (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Multi-touch operation (Panels, Comfort Panels, RT Advanced)](#multi-touch-operation-panels-comfort-panels-rt-advanced)
- [Supported gestures (Panels, Comfort Panels, RT Advanced)](#supported-gestures-panels-comfort-panels-rt-advanced)
- [Two-hand operation of operator controls (Panels, Comfort Panels, RT Advanced)](#two-hand-operation-of-operator-controls-panels-comfort-panels-rt-advanced)
- [Restrictions in Sm@rtServer/Client mode (Panels, Comfort Panels, RT Advanced)](#restrictions-in-smrtserverclient-mode-panels-comfort-panels-rt-advanced)

###### Multi-touch operation (Panels, Comfort Panels, RT Advanced)

###### Introduction

RT Advanced supports multi-touch operation under Windows 7, Windows 8 and Windows 10. You operate objects on the multi-touch screens by touching them with one or two fingers. Multi-touch operation is supported by TIA Portal as of V13. Versions V12 or older only support single-touch operation.

###### Requirements

The used monitor must support multi-touch functions.

###### Scrolling in lists and controls

You can scroll through lists and controls by dragging the screen margin.

You use horizontal dragging to move the content of the screen to the left or right. You use vertical dragging to scroll up or down in the view. An indicator appears during scrolling to indicate your position. When you drag a list diagonally on the screen, the content is moved horizontally and vertically at the same time.

Horizontal scrolling is not supported in the "Trend view" object.

You scroll five times faster up or down on a page when you use two fingers to drag up or down.

> **Note**
>
> **Scrolling in Windows 8.1**
>
> On the multitouch HMI devices with Windows 8.1, you can scroll continuously by double-tapping on the display and then dragging.

> **Note**
>
> **Current view is not persistent**
>
> The position in the trend window changed by scrolling is not saved.   
> In case of a screen change, the trend view is reset to the default setting.

###### Zoom in and out

You enlarge or reduce the view in "Trend view" and "f(x) trend view" objects by pinch-to-zoom with two fingers.

Double tap to switch from the magnified trend view back to the normal view.

The zooming function is limited to the time axis in the "Trend view" object.

If you have enabled the option "Range &gt; Auto-size" during configuration of the value axes in f(x) trend view, the axes are constantly calculated during zooming.

> **Note**
>
> **Current view is not persistent**
>
> The changes of the zoom factor are not saved.
>
> In case of a screen change, the trend view is reset to the default setting.

###### Supported gestures (Panels, Comfort Panels, RT Advanced)

###### Supported gestures

The following gestures are supported.

| Gesture |  | Function |
| --- | --- | --- |
| ![Supported gestures](images/60374196747_DV_resource.Stream@PNG-de-DE.png) | Tap | You can select a button, for example, by tapping. |
| ![Supported gestures](images/122714110219_DV_resource.Stream@PNG-de-DE.png) | Drag | Use one finger to scroll horizontally and vertically, for example, in lists.   You scroll horizontally and vertically at the same time with a vertical drag. |
| ![Supported gestures](images/60578502667_DV_resource.Stream@PNG-de-DE.png) |  | Use two fingers to scroll up or down a page quickly. |
| ![Supported gestures](images/60374205451_DV_resource.Stream@PNG-de-DE.png) | Scale | Pinch-to-zoom to enlarge or reduce the display of the control. |
| ![Supported gestures](images/60374214155_DV_resource.Stream@PNG-de-DE.png) | Double tap | Double tap the display to reset the view to the default zoom factor 100%. |

> **Note**
>
> **Operating with three of more fingers**
>
> Do not use three or more fingers to operate the device. This can lead to incorrect operations.

###### Two-hand operation of operator controls (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Two-hand operation of operator controls (Panels, Comfort Panels, RT Advanced)](#two-hand-operation-of-operator-controls-panels-comfort-panels-rt-advanced-1)
- [Locking and unlocking operator controls (Panels, Comfort Panels, RT Advanced)](#locking-and-unlocking-operator-controls-panels-comfort-panels-rt-advanced)
- [Configuring release button in screen or template (Panels, Comfort Panels, RT Advanced)](#configuring-release-button-in-screen-or-template-panels-comfort-panels-rt-advanced)

###### Two-hand operation of operator controls (Panels, Comfort Panels, RT Advanced)

###### Introduction

WinCC supports two-hand operation of operator controls with RT Advanced. It ensures safe operation of operator controls which are used to change critical system settings, for example, control tags with machine limits.

###### Locked and unlocked operator controls

You define specific operator controls as "locked operator controls" for two-hand operation of operator controls. Locked operator controls usually cannot be operated in runtime. The operator can only operate the locked operator controls if he presses a release button at the same time.

In runtime, locked operator controls can only be accessed with the tab sequence if a release button is pressed at the same time.

###### Locked operator controls and release buttons

You can configure the following operator controls as locked operator controls:

- I/O field as input field or input/output field
- Button (visible)
- Button (invisible)
- Slider
- Date/time field

You must configure at least one button in the screen as release button. This can be any unlocked button.

> **Note**
>
> You cannot configure operator controls or release buttons in the permanent area.

###### Templates with locked operator controls

You can also use locked operator controls in screen templates. To lock or unlock operator controls in templates, proceed as you would with operator controls in screens.

You can also implement a release button in the template. Use the same approach as for release buttons in screens.

In a screen created from the template, the release buttons from the template and any release buttons of the screen are active.

###### Display in runtime

The locked operator controls are displayed as dimmed in runtime. The release buttons are optically highlighted as soon as the operator presses a locked operator control. The locked operator controls are completely visible when they are unlocked by means of the release buttons.

This means you can configure the release buttons as invisible operator controls.

###### Simulation of projects with multi-touch functions

WinCC supports the simulation of configured multi-touch functions. Requirement is that your monitor supports multi-touch operation.

###### Locking and unlocking operator controls (Panels, Comfort Panels, RT Advanced)

You can lock and unlock operator controls in projects for multi-touch devices. Locked operator controls can only be operated in runtime if the operator presses a release button at the same time.

You can lock and unlock individual operator controls or several operator controls simultaneously.

###### Procedure

1. Configure operator controls of the type I/O field, button or slider.
2. Select the required operator control(s).
3. To lock the operator controls, enable the "Activate two-hand operation" option under "Properties &gt; Properties &gt; Security".

   ![Procedure](images/104486184971_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/104486184971_DV_resource.Stream@PNG-en-US.png)
4. To unlock the operator controls, disable the "Activate two-hand operation" option under "Properties &gt; Properties &gt; Security".

In runtime, locked operator controls can only be operated if a release button is pressed at the same time.

###### Defining release button

To use the locked operator controls, you must configure at least one release button in the same screen.

If no release button is configured, WinCC makes you aware of this fact during compilation of the project.

###### Configuring release button in screen or template (Panels, Comfort Panels, RT Advanced)

For the operator to operate locked operator controls on multi-touch devices, at least one release button must be configured in the same screen.

If the screen is based on a template and a release button is already defined in the template, the release button from the template is automatically in effect as release button of the screen. You can then configure an additional release button in the actual screen.

###### Requirement

At least one unlocked button is configured in the screen or in the template.

###### Procedure

1. Select the required button of the screen or template under "Release button" under "Properties &gt; Properties &gt; General".

   ![Procedure](images/72514540555_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72514540555_DV_resource.Stream@PNG-en-US.png)

   If the screen is based on a template and a release button is already defined in this template, this button is automatically in effect as release button of the screen.

**Note**

You can also select a button from a group for this purpose. Buttons from faceplates, however, are not available.

The selected button can also be displayed as invisible. It is optically highlighted in runtime when you press a locked operator control.

Locked operator controls can only be operated in runtime if the operator presses one of the configured release buttons at the same time.

###### Restrictions in Sm@rtServer/Client mode (Panels, Comfort Panels, RT Advanced)

###### Multi-touch server and single-touch client

The single-touch client device does not support operation by touch with two or more fingers as well as multi-touch functions. Single-touch client cannot be operated with gestures of the multi-touch Sm@rtServer.

Single-touch gestures work the same way as in WinCC V12.

###### Single-touch server and multi-touch client

The single-touch server device does not support operation by touch with two or more fingers as well as multi-touch functions. Multi-touch client cannot be operated with gestures of the single-touch Sm@rtServer.

Single-touch gestures work the same way as in WinCC V12.

#### Operation with keys (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Overview of operation with keys (Panels, Comfort Panels, RT Advanced)](#overview-of-operation-with-keys-panels-comfort-panels-rt-advanced)
- [Control keys and shortcuts (Panels, Comfort Panels, RT Advanced)](#control-keys-and-shortcuts-panels-comfort-panels-rt-advanced)
- [Function Keys (Panels, Comfort Panels, RT Advanced)](#function-keys-panels-comfort-panels-rt-advanced)
- [Direct keys (Advanced) (Panels, Comfort Panels, RT Advanced)](#direct-keys-advanced-panels-comfort-panels-rt-advanced)
- [Operator controls on the Mobile Panel (Panels, Comfort Panels, RT Advanced)](#operator-controls-on-the-mobile-panel-panels-comfort-panels-rt-advanced)

##### Overview of operation with keys (Panels, Comfort Panels, RT Advanced)

###### Introduction

Use the keys of the HMI device to operate the Control Panel / Start Center of your HMI device or the project that is running on your device. Depending on the device, control keys and function keys are available.

For more detailed information, refer to the operating instructions for your HMI device.

##### Control keys and shortcuts (Panels, Comfort Panels, RT Advanced)

###### Introduction

The following tables list the control keys available to operate the project.

> **Note**
>
> The availability of control keys is determined by the HMI device used.

You trigger functions on keyboard HMI devices either with a key or a shortcut. With shortcuts, you keep the first key pressed. Then you press the second key.

###### Navigating in the display

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) |  | Tabulator | Selects the next operating element in the tab sequence |
| ![Navigating in the display](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) | Tabulator | Selects the previous operating element in the tab sequence |
| ![Navigating in the display](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204938379_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43205122699_DV_resource.Stream@PNG-de-DE.png) |  | Cursor keys | Selects the next operating element to the left, to the right, above or below the current screen object  Navigating in the operating element |

###### Operation of operating elements

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) |  | ENTER key | - Controls buttons. - Applies and ends an entry - Opens a selection list - Toggles between character mode and standard mode within an input field   A single character is selected in character mode. In this mode, you can scroll within the character set using the cursor keys. |
| ![Operation of operating elements](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43205122699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Positioning cursor | Positioning the cursor within an operating element, for example, in an I/O field |
| ![Operation of operating elements](images/43204907659_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the character to the left of the current cursor position |
| ![Operation of operating elements](images/43205030539_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the next character to the right of the current cursor position |
| ![Operation of operating elements](images/43205007499_DV_resource.Stream@PNG-de-DE.png) |  | Cancel | - Deletes the input characters of a value and restores the original value - Closes the active dialog. |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) | Scroll to start | Scrolls to the start page of a list |
| ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling back | Scrolls the list back by one page |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) | Scroll to end | Scrolls to the end of a list. |
| ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling up | Scrolls the list up by one page |
| ![Operation of operating elements](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Open selection list | Opens a selection list |
| ![Operation of operating elements](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) | Accept value | Accepts the value selected in the selection list without closing the list |

###### Enter shortcut

| Key | Function | Purpose |
| --- | --- | --- |
| ![Enter shortcut](images/43204874379_DV_resource.Stream@PNG-de-DE.png) | Toggle (numbers/letters) | Toggles the assignment from numbers to letters  - No LED is lit:   The number assignment is enabled. Pressing the key once switches to letter assignment. - The right or left LED is lit:   The left or right letter assignment is enabled.   Each time the key is pressed, the system toggles between the left letter assignment, the right letter assignment and the number assignment. |
| ![Enter shortcut](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | Shift (upper/lower case) | Used in shortcuts, for example, for switching to uppercase letters |
| ![Enter shortcut](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | Toggle to additional keyboard layout | Some of the keys contain a blue special character in their bottom left corner, for example, the percent sign "%". To input these characters, press the relevant key in combination with the special character key shown on the left. |
| ![Enter shortcut](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example, for navigating trend views |
| ![Enter shortcut](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example for the "Watch table" screen object |

###### Acknowledge alarms

| Key | Function | Purpose |
| --- | --- | --- |
| ![Acknowledge alarms](images/43204851339_DV_resource.Stream@PNG-de-DE.png) | Acknowledge | Acknowledges the currently displayed alarm or all alarms of an alarm group  The LED is lit as long as an unacknowledged alarm is active. |

###### Displaying infotext

| Key | Function | Description |
| --- | --- | --- |
| ![Displaying infotext](images/43205130379_DV_resource.Stream@PNG-de-DE.png) | Displaying infotext | For the selected object, opens a window with the configured infotext, for example, for an alarm or an I/O field  The LED is lit if an infotext is available for the selected object. |

Key or shortcut

##### Function Keys (Panels, Comfort Panels, RT Advanced)

The assignment of the function keys (F1, F2, F3, etc.) is defined during configuration.

###### Function keys with global function assignment

A globally assigned function key always triggers the same action on the HMI device or in the PLC regardless of the screen displayed. The activation of a screen or the closing an alarm window, for example, is such an action.

###### Function keys with local function assignment

A function key with local function assignment is screen-specific and is therefore only effective within the active screen.

The function of a locally assigned function key can vary from screen to screen.

Within a screen, a function key has only one function assignment, either a global or local one. The project planner specifies which assignment has priority.

###### Operating function keys

> **Note**
>
> **Operating function key after screen change**
>
> If you press a function key after a screen change, the associated function may be triggered in the new screen before the new screen is fully displayed.

##### Direct keys (Advanced) (Panels, Comfort Panels, RT Advanced)

###### Introduction

Direct keys on the HMI device are used to set bits in the I/O area of a SIMATIC S7.

Direct keys enable operations with short reaction times that are, for example, a jog mode requirement.

> **Note**
>
> Direct keys are still active when the HMI device is in "offline" mode.

> **Note**
>
> If you operate a function key with direct key functionality in a running project, the direct key function is always executed, independent of the current screen contents.

> **Note**
>
> You can only use direct keys when there is a connection via PROFIBUS DP or PROFINET IO.
>
> Direct keys result in additional basic load on the HMI device.

###### Direct keys

The following objects can be configured as a direct key:

- Buttons
- Function keys

You can also define image numbers in the case of HMI devices with touch operation. In this way, the project engineer can configure the direct keys on an image-specific basis.

For additional information on configuring direct keys, refer to "WinCC communication".

##### Operator controls on the Mobile Panel (Panels, Comfort Panels, RT Advanced)

###### Operator controls on the Mobile Panel

The following operator controls are available to you depending on your type of mobile panel:

- Function keys

  The number and assignment of the function keys depend on the selected device type. The respective function is project-specifically assigned.
- Handwheel (optional)

  The handwheel can be turned without an end stop, and has no zero position. In a running project you enter incremental values using the handwheel.
- Key switch (optional)

  The key switch permits locking functions, which you can trigger using the HMI device.
- Illuminated pushbutton

  The function of the illuminated pushbutton is specified by the running project.

For more detailed information, refer to the operating instructions for your HMI device, and to the plant documentation.

#### Navigating in the display (BS) (Panels, Comfort Panels, RT Advanced)

##### Introduction

You navigate on the display of your HMI device as follows:

- between configured screen objects
- within screen objects

  When you select a complex screen object, the cursor focus switches to the screen object and follows the tab sequence there.
- in tables of screen objects

##### Procedure

- To navigate in the specified tab sequence, press the &lt;TAB&gt; key.
- To navigate freely between the operator controls, press the cursor keys.

Depending on the configuration of your HMI device, you can also use function keys or shortcuts for navigation.

When you operate your HMI device with the touch screen or with the mouse, you implicitly navigate by triggering a desired action. For this purpose, touch or click the operator control.

##### Result

The operator controls receive the cursor focus according to the selected sequence. You can trigger an action on the selected operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Triggering an action (Panels, Comfort Panels, RT Advanced)

##### Introduction

Triggering an action at an operator control can mean the following:

- A command is executed.

  Example: Click a button to trigger a script or to execute a predefined function.
- An object is enabled.

  Example: To enter a value, select a table cell with the &lt;Enter&gt; key.

##### Requirement

- You have navigated to the operator control on which you want to trigger the action.
- The operator control has the cursor focus.

##### Procedure

- Press &lt;Enter&gt;.

  Or
- Touch the operator control on the touch screen once or twice in rapid succession.

  Or
- Click or double-click the operator control with the mouse.

##### Result

The following results are possible:

- The requested command is executed.
- The screen keyboard is opened and/or the cursor blinks in the input area of the operator control.
- The element is selected and can be moved.

For more detailed information, refer to the operating instructions for your HMI device.

#### Entering a value (Panels, Comfort Panels, RT Advanced)

##### Introduction

Depending on the input format, you enter numerical or alphanumerical values in an input field.

You enter these values depending on the existing hardware using the screen keyboard, the control keys of the HMI device or an external keyboard.

##### Requirement

- The object is an input field or table field.
- The operator control is enabled.

##### Entering a value

1. Enter the desired value.
2. To confirm the value and exit the field, press the &lt;Enter&gt; key.
3. To discard the value and exit the field, press the &lt;Esc&gt; key.

##### Result

A value is entered or discarded. You navigate as needed to the next operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Moving operator controls (Panels, Comfort Panels, RT Advanced)

##### Introduction

In Runtime, you can move the movable operator controls of a screen object with the mouse or using the touch screen, for example, a slider or a scroll bar. Operation with the keyboard is described below.

##### Requirement

- A movable operator control is selected.

##### Procedure

- To move the operator control, proceed as follows depending on the operating element:

  - Standard for touch screen: Press the cursor keys.
  - Standard for keyboard devices: Press &lt;SHIFT&gt; and the cursor keys.
  - Switches: Press &lt;ENTER&gt;
  - Slider: Press &lt;PgUp&gt; or &lt;PgDn&gt;

1. To finish the movement, navigate to another screen object or operator control.

##### Slider procedure

1. To move the operator control, press the cursor keys.
2. To finish the movement, navigate to another screen object or operator control.

##### Result

The position of the movable operator control and the display in the screen object have changed.

For more detailed information, refer to the operating instructions for your HMI device.

#### Displaying infotext (Panels, Comfort Panels, RT Advanced)

##### Introduction

Depending on the configuration, additional information and operating instructions are available as infotext. The infotext is assigned to an operating element, an alarm or to the open screen. The infotext of an I/O field may contain, for example, information about the value to be entered.

As an alternative to the &lt;Help&gt; key of the HMI device, use the &lt;Help&gt; key of the screen keyboard for input objects.

##### Requirement

- An infotext is configured for the operating element, the screen or an alarm.

##### Calling the infotext

1. Enable the desired operating element.
2. Press the &lt;Help&gt; key of the HMI device.

   The infotext for the operating element is displayed.

If you are operating your input object with the touch screen, the screen keyboard opens. If the &lt;Help&gt; key appears, an infotext is configured for the operating element or the current screen.

If there is no infotext for the selected screen object, the infotext for the current screen is displayed, if it has been configured.

Use the scroll bar for long infotexts.

Depending on your configuration, infotext can also be retrieved by means of a configured operating element.

##### Switching between infotexts

- To switch between the infotexts of the operating elements and the screen, enable the infotext window.

##### Hiding infotext

- To hide the infotext, press the &lt;Esc&gt; key or press the &lt;Help&gt; key again.

#### Changing Runtime language (Panels, Comfort Panels, RT Advanced)

##### Introduction

The HMI device supports multilingual projects. A corresponding operating element which lets you change the language setting on the HMI device in Runtime has been configured.

The project always starts with the language set in the previous session.

##### Requirement

- The required language for the project is available on the HMI device.
- The language switching function is linked to an operating element, for example, to a button.

##### Selecting a language

You can change project languages at any time. Language-specific objects are immediately displayed on the screen in the new language when you switch languages.

You can switch the language in Runtime in one of the following ways:

- Use a configured operating element to switch from one language to the next in a list.
- Use a configured operating element to directly set the required language.

#### Web browser of WebKit engine: Overview (Panels, Comfort Panels)

##### Introduction

In the "HTML browser" object, you have the option in RT Advanced to select between two Web browser types. Specify the type of the Web browser under "Properties &gt; Properties &gt; General &gt; HTML browser type" in the Inspector window.

Only the Web browser of the WebKit engine is available on Panels.

The Web browser, which is based on a WebKit engine, offers no Active X support.

##### HTML5 functions

The following HTML5 standard functions are fully or partly supported by the Web browser of the WebKit engine:

- Parsing rules
- Elements
- Forms and fields
- Output
- Communication
- User interactions
- Performance
- Security
- History and Navigation
- 2D graphics
- Memory
- Animations
- Web applications
- Memory
- Files and file systems

> **Note**
>
> Microdata, input, peer to peer, position and orientation, video, audio, responsive images, 3D graphics, streams and web components are not supported in the Web browser of the WebKit engine.

The table below shows the availability of the HTML5 functions in the Web browser of the WebKit engine in detail:

| Parsing rules | Available |
| --- | --- |
| &lt;!DOCTYPE html&gt; triggers the standard mode | Yes |
| HTML5 tokenizer | Yes |
| HTML 5 tree building | Yes |
| Parsing Inline SVG | Yes |
| Parsing Inline MathML | Yes |

| Elements | Available |
| --- | --- |
| Embedded invisible data | Yes |
| **New or modified elements** |  |
| Section elements | Yes |
| Grouping content elements that belong together | Partly |
| Semantic elements of the text level | Partly |
| Interactive elements | Partly |
| **Global attributes and methods** |  |
| Hidden attributes | Yes |
| Inserting dynamic markups | Yes |

| Forms and fields | Available |
| --- | --- |
| **Field types** |  |
| type = text | Yes |
| type = search | Yes |
| type = tel | Yes |
| type = URL | Yes |
| type = email | Yes |
| type = date | No |
| type = month | No |
| type = week | No |
| type = time | No |
| type = datetime | No |
| type = datetime-local | No |
| type = number | Yes |
| type = range | Yes |
| type = color | Yes |
| type = checkbox | Yes |
| type = image | Yes |
| type = file | Yes |
| textarea | Yes |
| select | Yes |
| fieldset | Yes |
| datalist | Yes |
| keygen | Yes |
| output | Yes |
| progress | Yes |
| meter | Yes |
| **Fields** |  |
| Field validation | Yes |
| Assignment of forms and controls | Yes |
| Other attributes | Yes |
| CSS sectors | Yes |
| Events | Yes |
| **Forms** |  |
| Form validation | Yes |

| Output | Available |
| --- | --- |
| Full-screen support | No |
| Web notifications | Yes |

| Communication | Available |
| --- | --- |
| Server-sent events | Yes |
| Web beacons | No |
| **XML HttpRequest Level 2** |  |
| File upload | Yes |
| Response type | Yes |
| **WebSocket** |  |
| Basic Socket Communication | Yes |
| ArrayBuffer and Blob | Yes |

| User interactions | Available |
| --- | --- |
| **Drag-and-drop** |  |
| Attributes | Yes |
| Events | Yes |
| **Editing HTML** |  |
| Editing elements | Yes |
| Editing documents | Yes |
| CSS sectors | No |
| APIs | Yes |
| **Clipboard** |  |
| Clipboard for API and events | No |
| **Spell check** |  |
| Spelling attributes | Yes |

| Performance | Available |
| --- | --- |
| Native binary data | Yes |
| **Workers** |  |
| Web workers | Yes |
| Shared workers | Yes |

| Security | Available |
| --- | --- |
| Web Cryptography API | No |
| Content Security Policy 1.0 | Yes |
| Content Security Policy 1.1 | No |
| Cross-Origin Resource Sharing | Yes |
| Cross-Document Messaging | Yes |
| **Iframes** |  |
| Sandboxes Iframe | Yes |
| Seamless Iframe | Yes |
| Iframe with Inline contents | Yes |

| History and Navigation | Available |
| --- | --- |
| Session history | Yes |

| 2D graphics | Available |
| --- | --- |
| Canvas 2D graphics | Yes |
| **2D primitives** |  |
| Text input in graphics | Yes |
| Path input in graphics | No |
| Drawing an ellipse in graphics | No |
| Drawing a dashed line in graphics | Yes |
| System focus ring | No |
| **Functions** |  |
| Hit testing | No |
| Aperture mode | No |
| **Formats for image export** |  |
| PNG | Yes |
| JPEG | Yes |
| JPEG-XR | No |
| WebP | No |

| Animation | Available |
| --- | --- |
| window.requestAnimationFrame | Yes |

| Web applications | Available |
| --- | --- |
| **Offline resources** |  |
| Application cache | Yes |
| Service workers | No |
| **Content and scheme handlers** | No |

| Memory | Available |
| --- | --- |
| **Key value storage** |  |
| Session memory | Yes |
| Local storage | No |
| **Database storage** |  |
| IndexedDB | No |
| Blob object store | No |
| ArrayBuffer object store | No |
| Web SQL database | Yes |

| Files and file systems | Available |
| --- | --- |
| **Reading files** |  |
| Basic support for reading files | Yes |
| Creating a blob from a file | Yes |
| Creating a data URL from a blob | Yes |
| Creating an ArrayBuffer from a blob | Yes |
| Creating a blob URL from a blob | Yes |
| **Accessing a file system** |  |
| API file system | No |
| File API: Folders and system | No |

| Additional functions | Available |
| --- | --- |
| **Styles** |  |
| Style items | No |
| **Scripts** |  |
| Asynchronous script execution | Yes |
| Signaling script errors in Runtime | Yes |
| Events for script execution | No |
| Base 64 encoding and decoding | Yes |
| JSON coding and decoding | Yes |
| URL API | Yes |
| MutationObserver | "Yes" (pre-selected) |
| Promises | No |
| Page visibility | "Yes" (pre-selected) |
| Text selection | Yes |
| Scrolling (Scroll into view) | Yes |

---

**See also**

[HTML browser (Basic Panels, Panels, Comfort Panels, RT Advanced)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#html-browser-basic-panels-panels-comfort-panels-rt-advanced)

### Entering bar codes with optical handheld readers (Panels, Comfort Panels, RT Advanced)

#### Introduction

With the optical handheld readers you can identify components, machines and other objects optically and enter them directly into multiple operating elements on your HMI device.

Optical handheld reading devices read two dimensional data matrix codes, one dimensional barcodes and postal bar codes.

The following optical handheld readers are supported:

- SIMATIC MV320
- SIMATIC MV340

You can find templates for the settings and instructions on configuration in the manual for your optical handheld reader.

> **Note**
>
> The optical handheld reader is connected to the USB port of the HMI device. Only one device at a time can use the USB port. This is why it is not possible to use a USB keyboard and an optical handheld reader or two optical readers at the same time.

> **Note**
>
> When you connect the optical reader to a configuration PC, ensure that the USB port provides sufficient power for the reader.

#### Procedure

You read the marking of an object using the connected optical handheld reader. The value is entered in the object on the HMI device which has the focus during runtime.

After it has been read in, confirm the value with the Enter key or with the "Suffix - Enter" that you have previously configured in the settings of your optical handheld reader.

#### Basic Panels, Comfort Panels, Mobile Panels, RT Advanced

The following objects support input with optical handheld readers:

| Object | Preconditions for input |
| --- | --- |
| I/O field  Date/time field | The corresponding data type is selected.  The object and the tag length are configured accordingly.  The operator element has the cursor focus. |
| Recipe view | The recipe data record has the cursor focus. |
| User view | The logon dialog is open.  The user name or password has the cursor focus. |
| HTML browser | The operator element has the cursor focus. |
| Runtime dialogs which support keyboard entry | The dialog is open and the corresponding input field has the cursor focus. |

#### Comfort Panels, Mobile Panels, RT Advanced

The following objects support input with optical handheld readers:

| Object | Preconditions for input |
| --- | --- |
| Sm@rtClient view | Write access is configured for Sm@tClient.  The operator element has the cursor focus. |
| File browser | The field "File path" has the cursor focus. |
| Watch table | The input field "Control value" has the cursor focus. |
| PDF view | The search field has the cursor focus. |
| SINUMERIK NC operator display | The operator element has the cursor focus. |

#### Result

The code is read and entered into the corresponding input field.

### Security on the HMI device (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Signature basics (Panels, Comfort Panels, RT Advanced)](#signature-basics-panels-comfort-panels-rt-advanced)
- [Download of add-ons from third parties (Panels, Comfort Panels, RT Advanced)](#download-of-add-ons-from-third-parties-panels-comfort-panels-rt-advanced)
- [Switching off the signature check (Panels, Comfort Panels, RT Advanced)](#switching-off-the-signature-check-panels-comfort-panels-rt-advanced)

#### Signature basics (Panels, Comfort Panels, RT Advanced)

##### Overview

The HMI device software and the runtime and device options are protected from manipulation by signatures. The device options available over ProSave are also signed.

**HMI device signature**

The validity of the HMI device signature is checked when the HMI device software is loaded. If the HMI device signature is invalid, loading of the HMI device software is canceled and an error message is output.

**Signature for runtime and device options**

If the signature check finds that the signature is invalid, an error message to this effect is output. An error message indicating an invalid signature is also output in ProSave.

> **Note**
>
> To allow loadingof the HMI device software or the options without a signature (for versions prior to V14), you will need to switch off the signature check.

For details of how to do this, see [Switching off the signature check](#switching-off-the-signature-check-panels-comfort-panels-rt-advanced).

---

**See also**

[Switching off the signature check (Panels, Comfort Panels, RT Advanced)](#switching-off-the-signature-check-panels-comfort-panels-rt-advanced)

#### Download of add-ons from third parties (Panels, Comfort Panels, RT Advanced)

##### Basics

By default, download of add-ons from third parties is not permitted due to a missing signature. To enable the download of add-ons from third parties anyway, you must disable the signature check for the time of the download.

For details of how to do this, see [Switching off the signature check](#switching-off-the-signature-check-panels-comfort-panels-rt-advanced).

> **Note**
>
> We recommend that you reactivate the signature check once you have downloaded the add-ons.

---

**See also**

[Switching off the signature check (Panels, Comfort Panels, RT Advanced)](#switching-off-the-signature-check-panels-comfort-panels-rt-advanced)

#### Switching off the signature check (Panels, Comfort Panels, RT Advanced)

##### Procedure

1. Press "Transfer" twice in the control panel of the HMI device.

   The "Transfer Settings" dialog box opens.

   The option "Validate signatures" is enabled by default.
2. To allow the HMI device software to be loaded without a signature or to allow the download of a trustworthy option from a third-party provider, disable the "Validate signatures" option.

**Note**

If you wish to load an older WinCC project to an HMI device, you will need to check the settings for the signature check.

---

**See also**

[Download of add-ons from third parties (Panels, Comfort Panels, RT Advanced)](#download-of-add-ons-from-third-parties-panels-comfort-panels-rt-advanced)
  
[Signature basics (Panels, Comfort Panels, RT Advanced)](#signature-basics-panels-comfort-panels-rt-advanced)

## Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Runtime settings (RT Professional)](#runtime-settings-rt-professional)
- [Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)
- [Compiling a project (RT Professional)](#compiling-a-project-rt-professional)
- [Simulating projects (RT Professional)](#simulating-projects-rt-professional)
- [Loading projects (RT Professional)](#loading-projects-rt-professional)
- [Compiling and loading with Multiuser Engineering (RT Professional)](#compiling-and-loading-with-multiuser-engineering-rt-professional)
- [Starting Runtime (RT Professional)](#starting-runtime-rt-professional)
- [Basics of operating in Runtime (RT Professional)](#basics-of-operating-in-runtime-rt-professional)
- [Certificate creation with WinCC Certificate Manager (RT Professional)](#certificate-creation-with-wincc-certificate-manager-rt-professional)

### Runtime settings (RT Professional)

This section contains information on the following topics:

- [Settings in the Runtime software (RT Professional)](#settings-in-the-runtime-software-rt-professional)
- [Configuring display in Runtime (Professional) (RT Professional)](#configuring-display-in-runtime-professional-rt-professional)
- [Configuring operation in Runtime (RT Professional)](#configuring-operation-in-runtime-rt-professional)
- [Setting up the start sequence (RT Professional)](#setting-up-the-start-sequence-rt-professional)
- [Activating time synchronization (RT Professional)](#activating-time-synchronization-rt-professional)
- [Setting the time base (RT Professional)](#setting-the-time-base-rt-professional)
- [Configuring persistence (RT Professional)](#configuring-persistence-rt-professional)
- [Working with service mode (RT Professional)](#working-with-service-mode-rt-professional)
- [Password protection in runtime (RT Professional)](#password-protection-in-runtime-rt-professional)
- [Configuring WinCC REST Service (RT Professional)](#configuring-wincc-rest-service-rt-professional)

#### Settings in the Runtime software (RT Professional)

##### Introduction

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree.

> **Note**
>
> **Device dependency**
>
> The options available for selection in the Runtime settings depend on the HMI device.

##### Overview

You configure options from different areas of your project in the Runtime settings:

- Display in Runtime

  - Start screen
  - Menus and toolbars
  - Independent screen windows
  - Designs
  - Properties of windows
  - Bit selection for color and flashing
  - Screen buffer
  - Project graphics
- Scripts in Runtime

  - Start even with corrupt script
  - Value source for SmartTags
  - Language of the C scripts with "Use device setting"
- Options for compiling projects

  - Do not check deleted HMI tags in screens: If disabled, a warning is output during compiling when HMI tags are deleted in screens.
  - Hide WebUX warnings
- Start sequence

  Use the start sequence to specify the applications that will be started on activation of the project.
- Operating in Runtime

  - Window controller
  - Availability of online help in Runtime
  - On-screen keyboard
  - Keyboard layout and keyboard shortcuts
  - Cursor control
  - Zoom functions
- Alarms

  - Duration of display suppression
  - Alarm list entries after power failure
  - OPC alarms and events
  - Controller alarms
- Logging

  - Update cycle
  - Properties of log segments
- Configuration of the REST interface
- Configuration of the WinCC OPC servers
- User administration

  - Dynamic logon
  - SIMATIC Logon
- Language and font

  - Available Runtime languages
  - Runtime language for single-language objects
  - Sequence of language switching
  - Default font
  - Character set for menus
- Web access

  - Appearance
  - Server utilization
  - Local user groups
  - Alarms in the event view
  - Licenses

  For more information on the Runtime settings, refer to the online help for the options "WebNavigator", "WebUX" and "DataMonitoring".
- Settings for synchronization of PLC and HMI tags
- Redundancy

  - Redundant servers and partners
  - Client switchover
  - Down time for synchronization
  - Synchronization of logs and alarms
  - Recipes

  You can find additional information on the configuration of redundant servers in the online help for the option "Redundancy".
- Process Historian

  - Server selection
  - Buffer path

  You can find additional information on the Runtime settings in the online help for the option "Process Historian and Information Server".

---

**See also**

[Configuring display in Runtime (Professional) (RT Professional)](#configuring-display-in-runtime-professional-rt-professional)
  
[Setting up the start sequence (RT Professional)](#setting-up-the-start-sequence-rt-professional)
  
[Setting the Display Suppression Timeout (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#setting-the-display-suppression-timeout-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basic settings for OPC (RT Professional)](OPC%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-settings-for-opc-rt-professional)
  
[Settings for the user administration (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-the-user-administration-rt-professional)
  
[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring runtime settings for Process Historian (RT Professional)](Process%20Historian%20and%20Information%20Server%20%28RT%20Professional%29.md#configuring-runtime-settings-for-process-historian-rt-professional)
  
[Configuring runtime settings (WebNavigator) (RT Professional)](WinCC%20WebNavigator%20%28RT%20Professional%29.md#configuring-runtime-settings-webnavigator-rt-professional)
  
[Configuring runtime settings (DataMonitor) (RT Professional)](WinCC%20DataMonitor%20%28RT%20Professional%29.md#configuring-runtime-settings-datamonitor-rt-professional)
  
[Configuring operation in Runtime (RT Professional)](#configuring-operation-in-runtime-rt-professional)
  
[OPC for Runtime Professional (RT Professional)](OPC%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#opc-for-runtime-professional-rt-professional)
  
[Working with Logs (RT Professional)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-rt-professional)
  
[Managing languages (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-languages-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring redundant servers (RT Professional)](WinCC%20Redundancy%20%28RT%20Professional%29.md#configuring-redundant-servers-rt-professional)

#### Configuring display in Runtime (Professional) (RT Professional)

##### Introduction

In the Runtime settings you specify how the start screen, independent screen windows, menus and toolbars, etc. will be displayed.

To edit the Runtime settings for your HMI device, select "Runtime settings" under your HMI device in the project tree. The options available for selection depend on the HMI device.

##### Start screen settings

The start screen is the initial screen that is displayed after Runtime starts. The screen resolution is automatically adjusted to suit the HMI device when the screen is selected. You specify the start screen in the Runtime settings of the HMI device under "General &gt; Settings".

You can find additional information in the online help for WinCC under "Defining the project's start screen".

##### Design settings in the Runtime settings

Under "General &gt; Settings", you specify whether the HMI device uses the default design of the project or another predefined design. You can find more detailed information in "Working with designs".

##### Design settings in the Windows Control Panel

Select the "Windows 7" design for the configuration PC and the Runtime PC in the system settings of Windows. Use this setting to ensure correct representation of the dialogs and the on-screen keyboard in Runtime.

##### Menu and toolbar settings

Under "Screen management", you configure user defined menus and toolbars in the "Menus and Toolbars" editor.

For menus and toolbars, you make the following settings:

- Text
- Graphic
- Data: This data is passed to the function as user data.

For toolbars, the following setting options are also available to you:

- Button type: You specify whether the button consists of a graphic only, text only, or both.
- Screen size
- Transparent colors: You specify the color value that will be displayed as transparent in the selected graphic.

You can find additional information on this subject in the online help for WinCC under "Overview of working with menus and toolbars".

##### Settings for independent screen windows

If you enable the "Hide main window" option under "General &gt; Independent screen windows", you specify that Runtime runs in the background. The Runtime window is hidden and is also not visible in the taskbar.

##### Settings for screens

Change the settings of the Runtime window under "Screens" and specify how additional functions are used.

The submenu "Screens &gt; General" allows you to make general settings. The general settings include:

- Enable background effects in runtime
- Use shadows for screen objects in Runtime
- Use WinCC classic design in runtime
- Bit selection for appearance

In the menu "Screens &gt; Screen buffer" you can define the number of screens to be buffered via "Number of screens". The screens saved in the screen buffer are displayed using the screen navigation keys.

The submenu "Screens &gt; Window behavior" gives you options via the Runtime window. You have the following setting options here:

- Display of the title
- Showing a border
- Maximizing and minimizing

  > **Note**
  >
  > Activating the "Maximize" or "Minimize" properties simultaneously activates the "Title" property.
- Displaying in a full screen

  > **Note**
  >
  > The full screen display excludes the options "Title", "Border", "Maximize", "Minimize" and "Status bar".
- Displaying a slider
- Displaying a status bar
- Adjusting the screen

##### Graphic settings

Under "Graphic settings &gt; Loaded project graphics", you specify which graphics from the project graphics are downloaded to the HMI device.

#### Configuring operation in Runtime (RT Professional)

This section contains information on the following topics:

- [Configuring operation in Runtime (Professional) (RT Professional)](#configuring-operation-in-runtime-professional-rt-professional)
- [Select keyboard layout (Professional) (RT Professional)](#select-keyboard-layout-professional-rt-professional)
- [Configuring shortcut for operating and screen navigation (RT Professional)](#configuring-shortcut-for-operating-and-screen-navigation-rt-professional)
- [Configuring the cursor control (Professional) (RT Professional)](#configuring-the-cursor-control-professional-rt-professional)
- [Activating the zoom functions (Professional) (RT Professional)](#activating-the-zoom-functions-professional-rt-professional)

##### Configuring operation in Runtime (Professional) (RT Professional)

###### Introduction

Numerous functions are available to you for operation in Runtime. For some of these functions you can define specific shortcut keys.

###### Window control keys

These shortcut key changes are activated after system restart.

**Changing windows**

This shortcut key is used to navigate between multiple screen windows, which are configured in a main screen. Whenever the shortcut key is actuated, the next screen window will be activated for an operation.

> **Note**
>
> The &lt;DEL&gt; and &lt;HOME&gt; keys cannot be used as shortcut keys.

###### Making help available in Runtime

Under Runtime settings &gt; General, you specify that online help is available in Runtime. For this purpose you enable the "Make help available in Runtime" option.

Some objects in Runtime have an online help system. You can centrally disable calls to online help. You thereby prevent the online help on the hard disk from being accessed in Runtime.

###### Preventing access to Windows in Runtime

To prevent the user from accessing the Windows user interface with familiar shortcuts, such as &lt;Ctrl&gt;+&lt;Alt&gt;+&lt;Del&gt;, activate the function "Disable keyboard commands" under "Runtime settings &gt; Keyboard &gt; Keyboard commands of the operating system". In addition, deactivate the "Keep the taskbar on top of other windows" setting in Windows.

###### Using the screen keyboard

If you enable the "Use screen keyboard" option under General, the screen keyboard will be displayed in Runtime.

To enter data in Runtime, a screen keyboard will be displayed on the screen. The operator presses the individual keys with the mouse, or directly via the touch screen.

> **Note**
>
> The screen keyboard is not available with all HMI devices.

###### Disabling keyboard commands

The "Disable keyboard commands" function is not supported by the activatable Windows on-screen keyboard. Instead, use the on-screen keyboard provided by WinCC Runtime Professional.

###### Start even with corrupt scripts

Using the "Start even with corrupt scripts" option, you specify that Runtime Professional will be started even when a function in the project is corrupt.

###### Load names

Under General, you use the "Load names" option to specify that the objects' name information will be loaded along with them.

If the check box is activated, the objects' name information will be transferred to the HMI device.

If the check box is deactivated, then instead of the objects' name information only encoded addressing information will be transferred to the HMI device.

You need the objects' name information, if you want to address the objects in a script by the object name. When you test a script in the debugger, the code becomes more comprehensible by displaying the object names.

###### Hide main window

The "Screen window" object is used to display other screens from the project in the current screen. You can find the "Hide main window" function under "General &gt; Independent screen windows". With this option, you specify that Runtime runs in the background. The Runtime window is hidden and is also not visible in the taskbar.

##### Select keyboard layout (Professional) (RT Professional)

###### Introduction

You can define various shortcuts to operate the project. The shortcuts can be used as an alternative to the mouse.

- Keyboard commands of the operating system

  In the "Keyboard commands of the operating system", specify whether the operating system can be accessed with keyboard shortcuts.
- Action keys

  - "Logon" opens a window for user logon in Runtime.
  - "Logoff" opens a window for user logoff in Runtime.
  - "Hardcopy" opens a dialog for printing the screen in Runtime.
- Windows control keys

  In the "Windows control keys" area, determine whether the next screen window is activated using a specified keyboard shortcut in Runtime.
- Screen navigation keys

  - "Forward" moves to the next screen in the configured screen sequence.
  - "Back" moves to the previous screen in the configured screen sequence.
  - "Store screen" saves the currently displayed screen.
  - "Recall screen" opens to the previously saved screen.
  - "Start screen" opens the start screen.
- Keys for tab sequences

  - "Tab sequence mode" changes the cursor mode.
  - "Focus display of active object" activates the runtime cursor.
- Cursor control keys

  - "Enable hotkeys in Runtime" activates the shortcut keys for cursor control in Runtime.
  - "Up" makes a cursor movement up.
  - "Down" makes a cursor movement down.
  - "Left" makes a cursor movement left.
  - "Right" makes a cursor movement right.

###### Requirement

The "Runtime settings" editor is open.

###### Procedure

Set up the shortcuts as follows:

1. Click on "Runtime settings &gt; Keyboard".
2. Select the desired action in the "Action keys" area, for example.

   ![Procedure](images/72269634699_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72269634699_DV_resource.Stream@PNG-en-US.png)
3. Open the drop-down list.  
   The dialog for defining the shortcut is opened.
4. Define the required shortcuts.

   ![Procedure](images/72510139787_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72510139787_DV_resource.Stream@PNG-en-US.png)
5. Accept the settings.  
   The dialog for specifying the shortcut closes itself.

##### Configuring shortcut for operating and screen navigation (RT Professional)

###### Introduction

Screens can also be operated if mouse control is not available. Define corresponding shortcuts for the required operating functions. The operator calls the specific function by operating the shortcut.

The most important shortcuts for operation without mouse in Runtime are defined in the "Runtime settings &gt; Keyboard" editor.

###### Procedure

Set up the operator shortcuts as follows:

1. Click in the input field of the selected function.
2. Click the button in the selection list. The dialog for defining shortcuts opens.
3. Define the required shortcuts.
4. Click the button to close the dialog.

You can also define one of the function keys &lt;F1&gt; to &lt;F12&gt; instead of a shortcut.

> **Note**
>
> The function key F12 may not be configured as a system wide hotkey.

###### Window control keys

These shortcut changes are activated after system restart.

###### Changing windows

This hotkey is used to navigate between multiple screen windows, which are configured in a main picture. Whenever the hotkey is pressed, the next screen window is activated for operation.

> **Note**
>
> The &lt;DEL&gt; and &lt;HOME&gt; keys cannot be used as hotkeys.

###### Screen navigation keys

The "Forward" and "Back" buttons of most Internet browsers allow the navigation between Internet pages most recently called. A similar technique can be implemented in WinCC to navigate between individual process screens.

Configure corresponding shortcuts in the "Screen selection" dialog to facilitate screen navigation in Runtime. Screens are logged to a temporary list after they are called. You can page through this list using the "Forward" and "Back" functions, for example, to recall the last five screens. The valid maximum number of entries in this list is set in the field "Screen selection buffer". If this number is exceeded, the oldest entry is replaced after a new screen is called.

> **Note**
>
> The list logs up to 30 screen calls if the default is set for "Screen selection buffer". As a rule, it does not usually make sense to substantially increase this value, since the switchover can only be done in single steps. You can achieve more efficient screen navigation using faceplates.

##### Configuring the cursor control (Professional) (RT Professional)

###### Introduction

You can configure object navigation without mouse using defined cursor control functions in screens with tabular layout of the objects.

Define the cursor control shortcuts in the "Runtime settings &gt; Keyboard" editor. You specify the response of the cursor in tables under "Screens &gt; Cursor response in tables".

![Introduction](images/72512739723_DV_resource.Stream@PNG-en-US.png)

###### Procedure

Set up the operator shortcuts as follows:

1. Click in the input field of the selected function.
2. Open the drop-down list.  
   The dialog for defining the shortcut is opened.
3. Define the required shortcuts.
4. Accept the settings.  
   The dialog for specifying the shortcut closes itself.

You can also define one of the function keys &lt;F1&gt; to &lt;F12&gt; instead of a shortcut.

##### Activating the zoom functions (Professional) (RT Professional)

###### Introduction

Zooming in Runtime is supported by three techniques:

- Declutter  
  The layers and their embedded objects can be shown and hidden.

  For additional information, refer to "[Dynamic visualization of an object](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#dynamizing-the-visibility-of-an-object-panels-comfort-panels-rt-advanced-rt-professional)".
- Extended Zooming  
  A screen's view in Runtime can be enlarged or reduced using the scroll wheel of the mouse. For this purpose, hold down &lt;CTRL&gt; and move the mouse scroll wheel in the desired direction.
- Panning

  If a screen has a zoom factor that causes the screen to be displayed with scroll bars, then you can move a screen detail within the document. A navigation crosshair appears upon clicking on the mouse wheel. Moving the mouse pointer scrolls in the desired direction. The distance between mouse pointer and navigation crosshair determines the scrolling speed. A second click cancels panning.

###### Requirement

- A driver for a Logitech mouse or Microsoft Intellimouse
- The mouse wheel must be set to "Autoscroll" mode.
- The "Runtime settings" editor is open.

###### Enabling the zoom function

1. Click on "Screens".
2. Deactivate "Declutter" and "Extended zoom".

   The functions are disabled if you activate "Declutter" and "Extended zoom".

   ![Enabling the zoom function](images/63908405515_DV_resource.Stream@PNG-en-US.png)

   ![Enabling the zoom function](images/63908405515_DV_resource.Stream@PNG-en-US.png)

###### Configuring Extended Zooming Screen-Specific

The "Extended Zoom" function can be enabled/disabled for specific screens. Make the corresponding setting in the inspector window of a screen under "Properties &gt; Properties &gt; Miscellaneous".

---

**See also**

[Dynamizing the visibility of an object (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#dynamizing-the-visibility-of-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Setting up the start sequence (RT Professional)

##### Introduction

When you activate a project, additional program modules will be loaded to execute Runtime.

Select "Start sequence of WinCC Runtime" to specify the applications that will be started on activation of a project. "Graphics in Runtime" is always started and is enabled by default.

Start only the applications required in Runtime to obtain a high performance level.

##### Procedure

Set up the startup list as follows:

1. Open the "Runtime settings &gt; Services" editor.

   ![Procedure](images/72513304203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72513304203_DV_resource.Stream@PNG-en-US.png)
2. Enable the display of the online help in Runtime by activating "Enable help in Runtime".
3. Select the applications to load at the start of Runtime in the "Start sequence of WinCC Runtime" area.
4. You can load additional tasks or applications at the start of Runtime by clicking in the table row at "Additional tasks/application".
5. Enter a name for the additional task or application. Specify the working directory.
6. The project folder is used as working directory if you select the check box in the "Project directory" column.
7. If you clear the check box in the "Project directory" column, use the "Find" button to specify the folder in the "Working directory" column.
8. Specify any necessary parameters.
9. Specify the startup size of the task or application window in the "Window style" column, e.g. minimized, maximized or standard size.

#### Activating time synchronization (RT Professional)

##### Introduction

To have the same time throughout the plant, you can synchronize the time on various plant components using time synchronization. WinCC time synchronization is operated as a master-slave system.

One system component must be a clock for all components of a plant to work with identical time. The component functioning as the clock is referred to as the time master. The components that receive the time are time slaves.

The time master can be a computer or an external clock, such as a SICLOCK. This master transmits the time signal to the other components. Only one time master can be the active clock in the network.

To prevent the failure of time synchronization, two components can be configured as the time master. The redundant time master is a time slave as long as the active time master is transmitting the time frames.

The time slaves receive the time signal transmitted by the time master via the bus and use it to synchronize their own time.

##### Time synchronization in runtime

The time synchronization of the computer is entered in the start sequence of the computer for the following events:

- After configuration of time synchronization

> **Note**
>
> Time synchronization takes effect a few minutes after activation in runtime. If you require precise time synchronization during startup, synchronize the local PC clocks before activating Runtime. This is the case, for example, if you wish to receive process control messages during startup in chronological order.

##### Activating time synchronization

Proceed as follows to activate time synchronization:

1. Select the runtime "Properties" command from the shortcut menu in the project navigation and then select "Time synchronization &gt; General".
2. Under "Synchronization", activate "Activate time synchronization".

   ![Activating time synchronization](images/64828333067_DV_resource.Stream@PNG-en-US.png)

   ![Activating time synchronization](images/64828333067_DV_resource.Stream@PNG-en-US.png)
3. Under "Time information", select a time source, for example, "No external sources".
4. Specify how often the time message frame should be transmitted by the time master.

##### Synchronization via the terminal bus

Proceed as follows to synchronize the time via the terminal bus:

1. Select the runtime "Properties" command from the shortcut menu in the project navigation and then select "Time synchronization &gt; Via terminal bus".

   ![Synchronization via the terminal bus](images/88752692747_DV_resource.Stream@PNG-en-US.png)

   ![Synchronization via the terminal bus](images/88752692747_DV_resource.Stream@PNG-en-US.png)
2. Under "Synchronization", activate the "Activate" check box.
3. If you also want to synchronize redundant components, activate the "Synchronize redundant partners" check box.
4. Under "Server 1", select the server from which the HMI device should receive the time message frame as the time slave.
5. Click "OK" or configure the synchronization via the system bus.

##### Synchronization via the system bus

Proceed as follows to synchronize the time via the system bus:

1. Select the runtime "Properties" command from the shortcut menu in the project navigation and then select "Time synchronization &gt; Via system bus".

   ![Synchronization via the system bus](images/88752697099_DV_resource.Stream@PNG-en-US.png)

   ![Synchronization via the system bus](images/88752697099_DV_resource.Stream@PNG-en-US.png)
2. Under "Synchronization", activate the "Activate" check box.
3. Activate the "Show symbolic names of access points" check box.
4. Under "Access point 1", select an access point and assign it a role as master or slave.
5. You also select a second access point under the following conditions:

   - If you want to use a redundant device.
   - If you want to synchronize two system buses via a "bridge".
   - If you want to synchronize two system buses as the master.
6. Also assign this access point a role as master or slave. The combination of these roles defines the response as shown in the table below.

**Note**

If you configure time synchronization from another computer, the installed access points are unknown. The symbolic names are shown, however, and assigned to the physical names of the access points when runtime starts.

| Access point 1 | Access point 2 | Behavior |
| --- | --- | --- |
| Slave | Slave | The device always functions as a time slave. |
| Master | Master | The device functions as a cooperative master at both access points. |
| Master | Slave | The devices functions at access point 1 as the master and transmits time message frames; at access point 2 the device synchronizes with the time signals received there. |
| Slave | Master | The device functions at access point 2 as the master and transmits time message frames; at access point 1, the device synchronizes with the time signals received there. |

##### Performance tags: Synchronization status

You can find the tags in the standard tag table of the HMI device in the "System tags" tab.

You can also display these performance tags as counters in the Windows system monitor.

| System tag | Description |
| --- | --- |
| @PRF_TIMESYNC_CURRENT_STATE | Time synchronization status. The value depends on the role of the device.  Standby:  - 0: No master available. Synchronization is not possible. - 1: Master for synchronization is connected.   Master:  - 0: It is not possible to send time frames over the system bus. - 1: Time frames are sent via the system bus. |
| @PRF_TIMESYNC_SIGNAL_QUALITY | Quality of the external signal with which the local time is synchronized.  The tag is only updated if the following conditions are fulfilled:  - The "DCF77" time signal receiver is installed. - The "Use time reception service" option is enabled. - Time synchronization is only configured as master.   - No standby is configured in the system.   - No synchronization via terminal bus is configured in the system.   Values:  - 0: No signal received, or the tag is not updated. - 1: Signal quality is very weak. - 2: Signal quality is weak.   Synchronization may not run without problems. - 3: Signal quality is adequate. - 4: Signal quality is very good. |
| @PRF_TIMESYNC_TIME_DIFF | Time difference between the local system and the time specified in the message frame of the master.  The tag is updated when one of the following conditions is met:  - At least one device is running as a standby at one of the access points. - Synchronization via terminal bus is enabled.   Unit: millisecond |
| @PRF_TIMESYNC_RESET | Currently not used. |

---

**See also**

[System diagnostics with performance tags (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-diagnostics-with-performance-tags-rt-professional)

#### Setting the time base (RT Professional)

##### Setting the time base for the time of day

To set the time display on the HMI device, proceed as follows:

1. Select "Properties &gt; Time information" from the Runtime shortcut menu in the project navigation.

   ![Setting the time base for the time of day](images/64831049355_DV_resource.Stream@PNG-en-US.png)

   ![Setting the time base for the time of day](images/64831049355_DV_resource.Stream@PNG-en-US.png)
2. Select one of the following options under "Basis for time information in Runtime":

   - Time zone of server (migrated projects)
   - Local time zone
   - Coordinated Universal Time
3. Select one of the following options for the display format of the date and time:

   - "Configure individual": If you want to display the date in the configured format.
   - "Formatting to ISO 8610": If you want to display the date in ISO 8610 format on all components.

#### Configuring persistence (RT Professional)

##### Introduction

You use the persistence to determine how long configuration changes that were configured directly on the HMI device in Runtime are saved.

The changes configured in Runtime are saved separately from the screen in the engineering system. The screen is thus retained in its original configuration.

##### Persistence defaults

Persistence can be configured in the engineering system, and depending on the configuration, in Runtime. There are three defaults for persistence:

- "No persistence": The online configurations are lost the next time the screen changes, and when the configuration is disabled/enabled.
- "Persistence": In Runtime, this default allows the user the options of "discard", "retain" or "reset". With the "retain" option the online configurations are retained the next time the screen changes, and when the project is disabled/enabled.
- "Persistence in Runtime": In Runtime, this default allows the user the options of "discard", "retain" or "reset". With the "retain" option the online configurations are retained the next time the screen changes, but are lost when the project is disabled/enabled.

> **Note**
>
> **Changing a control**
>
> If you change a configured control and load it onto the HMI device, the changes are overwritten in Runtime regardless of the settings.

##### Online delta loading

In WinCC you can edit a project on the configuration PC while the same project is active in Runtime. If you change the project on the configuration PC, for most configuration changes you can load the changed components onto the HMI device by means of "Online delta loading". Online delta loading requires less time compared to the loading of the entire project.

During online delta loading, The "Load preview" dialog box opens. In this dialog you specify whether user administration or logs, which have been changed on the HMI device in the meantime, are overwritten or retained during online delta loading.

> **Note**
>
> **Changes on the HMI device**
>
> Interim changes in user administration or in the logs are lost during online delta loading.

#### Working with service mode (RT Professional)

This section contains information on the following topics:

- [Basic information on service mode and autostart (RT Professional)](#basic-information-on-service-mode-and-autostart-rt-professional)
- [Configurations for a service project (RT Professional)](#configurations-for-a-service-project-rt-professional)
- [Use of a server project and restrictions (RT Professional)](#use-of-a-server-project-and-restrictions-rt-professional)
- [How a service project works (RT Professional)](#how-a-service-project-works-rt-professional)
- [Configuring service mode (RT Professional)](#configuring-service-mode-rt-professional)

##### Basic information on service mode and autostart (RT Professional)

###### Overview

Service mode provides you with the option of running WinCC Runtime Professional as service. As service, WinCC Runtime Professional can also be active when no interactive user is logged onto the computer.

In conjunction with the "Autostart" option, the service mode can be helpful in a power failure, for example, because the system is automatically powered up and the server is again available for the clients.

WinCC Runtime Professional can also be run on the computer if no interactive user is logged onto the computer.

In service mode, WinCC Runtime Professional can also be operated with logged on user, in which case interactive user inputs are possible.

> **Note**
>
> **WinCC cannot run during interventions in the system**
>
> Changes to the processes and services of WinCC are not permitted in the Control Panel or in the Windows task manager. The following changes are affected:
>
> - Changes to properties
> - Manual interventions:
>
>   - Starting
>   - Close
>   - Stop
>   - Continue
>   - Restart
> - Change of priority
>
> Dependencies exist between the individual processes and services.
>
> Do not execute any changes.

---

**See also**

[Configuring service mode (RT Professional)](#configuring-service-mode-rt-professional)
  
[Use of a server project and restrictions (RT Professional)](#use-of-a-server-project-and-restrictions-rt-professional)
  
[How a service project works (RT Professional)](#how-a-service-project-works-rt-professional)

##### Configurations for a service project (RT Professional)

###### Overview

WinCC Runtime Professional can be run as service project in service mode in the following configurations on the server:

- WinCC Server with Windows Server 2008 R2 SP1 (64-bit)

  - Clients with Windows 7 SP1 (32-bit, 64-bit)
- WinCC Server with Windows Server 2012 R2 Standard Edition, full installation (64-bit)

  - Clients with Windows 10 (32-bit, 64-bit)
- WinCC Server with Windows Server 2016 Standard Edition, full installation (64-bit)

  - Clients with Windows 10 (32-bit, 64-bit)
- WinCC Server with Windows Server 2019 Standard Edition, full installation (64-bit)

  - Clients with Windows 10 (32-bit, 64-bit)
- WinCC WebNavigator Server

  - WinCC Web clients
- WebUX server

  - WebUX clients
- DataMonitor server

  - DataMonitor clients

##### Use of a server project and restrictions (RT Professional)

###### Use of a service project

The project is operated as service project in service mode on the server. WinCC Runtime Professional starts as service. A service project is started automatically or manually.

A service project is available for the following operations:

- Operation without logged-on user

  A service project can be run without an interactive logged onto the computer. If no interactive user is logged on, no interactive operation is possible.
- Operation with logged-on user

  In service projects, interactive operation is generally not desired. An interactive user can, for example, log on for service purposes. In this case, the user can enable the interactive operation of the service project.
- Automatic start

  With the automatic start, WinCC Runtime Professional is loaded automatically after the system has been switched on and the specified project is started. If it is a WinCC client, it may be necessary to wait after the system start until the WinCC server is ready. Then the project is started.
- Manual start

  With manual start, the user has to log on to the server and then enable the project. When the user logs off again from the server, WinCC Runtime Professional continues to be active.
- Logging users on and off

  Interactive users can log on and log off at any time while the service project is enabled.

###### Restrictions

A service project is subject to the following restrictions:

- VB scripts and C scripts lead to problems when they require interactions, such as inputs, or display massage boxes.

  In service mode, there is also no common data area for C scripting. This means, for example, that no global C tags can be exchanged between user-defined C functions in the scheduled tasks and user-defined functions in the "Screens" editor.
- Additional tasks or applications cannot be loaded during starting of Runtime.
- OPC access is not enabled.
- Diagnostic information of a service project cannot be displayed on the server.
- In service mode, printing reports via PDF Writer is not possible.

> **Note**
>
> **Editing or migrating service projects**
>
> To edit or migrate a service project, you have to manage the service mode user appropriately on the computer. When the service mode user is not present, the logged on Window user must be managed accordingly so that the project can be edited or migrated.

---

**See also**

[Basic information on service mode and autostart (RT Professional)](#basic-information-on-service-mode-and-autostart-rt-professional)

##### How a service project works (RT Professional)

###### Basics

With a service project, WinCC Runtime Professional is started as service. Depending on the setting, these services are started at the following times:

- Automatically when the operating system starts.
- After a user has logged on and WinCC Runtime Professional has started.

WinCC Runtime Professional is still active even when the user logs off.

The Runtime data is still accessible.

The logged-on user can enable Runtime operation when required.

---

**See also**

[Basic information on service mode and autostart (RT Professional)](#basic-information-on-service-mode-and-autostart-rt-professional)

##### Configuring service mode (RT Professional)

###### Introduction

When you load the project, you specify in the "Load preview" dialog box whether the project is operated as service project and whether autostart is set up for the project.

###### Configuring projects as service projects

1. Activate the "Enable service mode" option in the "Load preview" dialog box.
2. Enter your user name under "User".
3. Enter your password under "Password".

To be able to log on, you must be created as user in the SIMATIC HMI group on the HMI device.

> **Note**
>
> In the redundant system, you must log on in Runtime with the same user data.

> **Note**
>
> If the project has been loaded and service mode enabled, the "Enable service mode" option is already activated.
>
> The "User" and "Password" fields are not filled in.

###### Setting up autostart

Autostart can be activated for a WinCC Professional Runtime project on the WinCC server and on a WinCC client. If autostart is enabled, the set WinCC project is automatically started after the system start. With autostart on a WinCC client, the system attempts to reach the WinCC server and to start the project after the system start until it can be successfully completed.

You have the option to activate a CancelButton for the autostart. The "Cancel" button appears in the autostart dialog; users can use this button to cancel the Runtime start (with connection attempt to the server if necessary). If the Cancel button is not enabled, the "Cancel" button is displayed only after a timeout (after 4-20 minutes, depending on the scenario).

**Setting up on the engineering system**

1. Activate the autostart option in the "Load preview" dialog box.

   WinCC activates the required project when the computer is powered up.

**Note**

If the project has been loaded and autostart was enabled, the option is already selected.

**Setting up with WinCC RT Start**

1. Open the "WinCC RT Start" tool.
2. Select your project in the "Autostart" tab.
3. To activate the CancelButton, select the option "Allow 'Cancel' during activation".

> **Note**
>
> **Special features when loading offline**
>
> With offline loading or when initializing a WinCC client, the autostart option can only be carried out using the "WinCC RT Start" tool on the corresponding operating computer.

---

**See also**

[Basic information on service mode and autostart (RT Professional)](#basic-information-on-service-mode-and-autostart-rt-professional)

#### Password protection in runtime (RT Professional)

This section contains information on the following topics:

- [Password protection in runtime: Basics (RT Professional)](#password-protection-in-runtime-basics-rt-professional)
- [Configuring a password for transport (RT Professional)](#configuring-a-password-for-transport-rt-professional)
- [Resetting the password for transport (RT Professional)](#resetting-the-password-for-transport-rt-professional)

##### Password protection in runtime: Basics (RT Professional)

###### Overview

The connection establishment can be protected with passwords in the TIA Portal. The configured passwords are saved in encrypted form. During transfer to the target system, the passwords are also protected against unauthorized access and cannot be read. These passwords are decrypted securely on the HMI devices in Runtime.

Password protection can be created for the following connections:

- SIMATIC S7-1200
- SIMATIC S7-1500
- SIMATIC S7-1500 Software Controller (WinAC)
- PC Station 2.0 (Station Manager)
- OPC UA connection (V15.0 and higher)

> **Note**
>
> The passwords become invalid at a change to an older version.

> **Note**
>
> If the user name on a HMI device is changed locally in V14 during configuration, the password becomes invalid and has to be entered again.

---

**See also**

[Configuring a password for transport (RT Professional)](#configuring-a-password-for-transport-rt-professional)
  
[Resetting the password for transport (RT Professional)](#resetting-the-password-for-transport-rt-professional)

##### Configuring a password for transport (RT Professional)

###### Introduction

To protect the private password key during transport, you can configure a password for transport under "Runtime settings".

###### Creating password

1. Open the "Runtime settings &gt; General" editor in the Project window.
2. Enter the password in the "Enter password" field in the "Transport password" area.
3. Confirm the password in the "Confirm password" field.

> **Note**
>
> If there was no previous password, the "Old password" field is disabled.

###### Result

You have now configured the password for transport. If a password for transport has been configured and you transfer the project to the HMI device, a dialog with a password prompt will appear once in runtime.

If the password entered is correct, the certificate is saved in the certificate store of the HMI device.

When you change the password, load the project with the changed password into the HMI device and start Runtime. No password prompt appears.

---

**See also**

[Password protection in runtime: Basics (RT Professional)](#password-protection-in-runtime-basics-rt-professional)
  
[Resetting the password for transport (RT Professional)](#resetting-the-password-for-transport-rt-professional)

##### Resetting the password for transport (RT Professional)

###### Introduction

If you have moved the transport password, for example, you can create a new security certificate. To do so, reset the transport password.

###### Reset password

1. Click the "Reset password" button.

   The password is reset. A new certificate without a password is generated.
2. Enter the new password and confirm it in the "Confirm password" field.

**Note**

Other passwords, for example the password for the PLC, will become invalid. The next time you compile, an error message will appear telling you that these passwords are no longer valid.

**Note**

The certificate is not password-protected until you enter a new password for transport.

After download of the project to the HMI device, you will be prompted for the password.

---

**See also**

[Password protection in runtime: Basics (RT Professional)](#password-protection-in-runtime-basics-rt-professional)
  
[Configuring a password for transport (RT Professional)](#configuring-a-password-for-transport-rt-professional)

#### Configuring WinCC REST Service (RT Professional)

You can configure the REST service in the runtime settings.

To use secure communication over HTTPS, select an installed certificate.

##### Licensing

A license for the WinCC Option Connectivity Pack is required to operate the REST service.

##### WinCC users and authorizations

**HMI tags: Authorizations for tag access**

For each tag, you can limit reading or writing of values to specific authorizations.

In the Inspector window, under "Properties &gt; Properties &gt; Settings &gt; REST API", select the desired authorization in the following fields:

- REST API read authorization
- REST API write authorization

**User management: Assigning authorizations**

For access via WinCC as a REST service, create a user in the user administration.

In order to access a tag, give the user the authorizations set in the tag properties.

##### Procedure

1. Open the Runtime settings:
2. Select the "Runtime settings &gt; General" area.
3. Under "REST settings", activate the option "Turn on".
4. Specify the connection data:

   - **Host name**: Name of the host device
   - **Port number**: Port number used for access

   The path to the server is displayed in the "Service URL" field.
5. To set up a secure connection, open the drop-down list in the "Certificate" field.

   The available certificates are displayed.
6. Select a certificate and confirm with "OK".
7. Select the "Runtime settings &gt; Services" area.
8. Under "Start sequence of WinCC Runtime", activate the "REST service" application.

### Overview of compiling and loading projects (RT Professional)

#### Overview

The project is compiled in the background even as you are configuring it in WinCC. This reduces the time for final compilation. When you start compilation, you create a file that can be run on the corresponding HMI device.

If an error occurs during compilation, WinCC provides support in locating and correcting it.

Once you have corrected any problems, you download the compiled project to the HMI devices on which the project is to run. If the configuration PC is not connected to the HMI device, save the compiled project on a data medium of your choice. The compiled project is then transferred from a PC connected to the HMI device to the HMI device.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile all modified S7 blocks with the command "Compile &gt; Software" in the shortcut menu before you compile the HMI device.

> **Note**
>
> **WinCC version compatibility**
>
> To compile a project of a predecessor WinCC version, upgrade the project to your WinCC version. You can then no longer open the project in the predecessor WinCC version.

#### Project

The term "project" has two different meanings in the contexts of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of an HMI device

The figure below illustrates the link between WinCC projects and Runtime projects using the example of the "Compile and load" process:

![Project](images/46298521483_DV_resource.Stream@PNG-en-US.png)

#### Runtime

Runtime is the software for process visualization. In Runtime, you execute the project in process mode.

A distinction is made between two types of Runtime:

1. Runtime on a panel

   Before running a Runtime project on a panel, you have to transfer the Runtime project to the panel before startup.
2. Runtime on a PC

   You can execute the Runtime project directly on the configuration PC if Runtime has been installed on the configuration PC.

   If you want to execute the Runtime project on a different PC, you have to transfer the Runtime project to the PC before startup.

#### Simulation

You test your configuration with a simulation. You can start a simulation without a link to the active process.

In a simulation, you test configured tags or screen changes, for example. During the simulation, the configured tags can be manipulated, activated and deactivated with the help of the tag simulator.

There are two types of simulation:

1. Simulating a panel

   If you created a panel in your project, the panel is displayed in the simulation. With the help of this type of simulation, you can test your configuration on the HMI device without transferring the project to the panel.
2. Simulating Runtime

   Simulating Runtime allows you to test the project directly on the configuration PC.

---

**See also**

[Compiling a project (Panels, Comfort Panels, RT Advanced)](#compiling-a-project-panels-comfort-panels-rt-advanced)
  
[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
  
[Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)
  
[Simulation basics (Panels, Comfort Panels, RT Advanced)](#simulation-basics-panels-comfort-panels-rt-advanced)
  
[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Error messages during loading of projects (Panels, Comfort Panels, RT Advanced)](#error-messages-during-loading-of-projects-panels-comfort-panels-rt-advanced)
  
[Generating a "Pack&amp;Go" file (Panels, Comfort Panels)](#generating-a-packgo-file-panels-comfort-panels)
  
[Starting Runtime Advanced and Panel Runtime (Panels, Comfort Panels, RT Advanced)](#starting-runtime-advanced-and-panel-runtime-panels-comfort-panels-rt-advanced)
  
TRANSFER_FLASH (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Load files using the "HMI files" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#load-files-using-the-hmi-files-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Compiling a project (RT Professional)

#### Introduction

The changes made to the project are compiled in the background even as you are configuring a project in WinCC. Projects are compiled automatically when you load them. This ensures that the latest version of the project is loaded at all times.

WinCC checks consistency of the project during compilation. The error locations in the project are listed in the Inspector window. You can jump directly to the source of the error from the entry in the Inspector window. Check and correct errors found.

#### Scope of the compilation

Configuration data is compiled in the background as soon as you start configuring an HMI device. If you compile a project manually, only the changes in the configuration made since the last compilation process are compiled in the background.

You can start complete project compilation manually at any time; this may, for example, be done to test the consistency of the configured data.

#### Requirement

- A project is open.

#### Procedure

Proceed as follows to compile a project:

1. If you want to compile several HMI devices at the same time, select all the relevant HMI devices with multiple selection in the project tree.
2. Compile the project:

   - To only compile changes in the project, select the "Compile &gt; Software (only changes)" command from the shortcut menu of the HMI device.
   - To compile all project data, select the "Compile &gt; Software (compile all)" command from the shortcut menu.

#### Result

The configuration data of all selected HMI devices is compiled. Any errors that occur during compilation are shown in the Inspector window.

---

**See also**

[Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)

### Simulating projects (RT Professional)

This section contains information on the following topics:

- [Simulation basics (RT Professional)](#simulation-basics-rt-professional)
- [Runtime Professional simulation (RT Professional)](#runtime-professional-simulation-rt-professional)
- [Simulating a project (RT Professional)](#simulating-a-project-rt-professional)
- [Simulating a screen (RT Professional)](#simulating-a-screen-rt-professional)
- [Simulation restrictions (RT Professional)](#simulation-restrictions-rt-professional)
- [Simulating tags with the Tag Simulator (RT Professional)](#simulating-tags-with-the-tag-simulator-rt-professional)

#### Simulation basics (RT Professional)

##### Introduction

You can use the simulator to test the performance of your configuration on the configuration PC. This allows you to quickly locate any logical configuration errors before productive operation.

You can start the simulator as follows:

- In the shortcut menu of the HMI device or in a screen: "Start simulation"
- Menu command "Online &gt; Simulation &gt; [Start|With tag simulator|With script debugger]"
- Under "Visualization &gt; Simulate device" in the portal view.

##### Requirement

The simulation/runtime component is installed on the configuration PC.

##### Field of application

You can use the simulator to test the following functions of the HMI system, for example:

- Checking limit levels and alarm outputs
- Consistency of interrupts
- Configured interrupt simulation
- Configured warnings
- Configured error messages
- Check of status displays

---

**See also**

[Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)

#### Runtime Professional simulation (RT Professional)

##### Introduction

Simulating Runtime Professional allows you to test the project with process link directly on the configuration PC. You can also test the tags using the tag simulator.

##### Function

Both process values and alarms are saved to a simulation log. The data generated is deleted from this log when you exit simulation mode.

The Runtime database is restored to the original state it had prior to simulation. Any changes to project data made during Runtime will be lost. You use the tag simulator to simulate the assignment of various values to the tags in your project.

Project logging and backup operations are continued during simulation.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Possible damage to the plant**  If you have changed tag values during the simulation with a PLC connection, unforeseen plant states can result in irreparable damage to the plant. Therefore, limit manual value manipulation to a minimum and select the test values carefully. |  |

##### Limitations

Client-server operation is not possible during simulation.

#### Simulating a project (RT Professional)

##### Requirement

The project is open in the configuration PC.

> **Note**
>
> The tag values of faulty connections to the process cannot be simulated.

##### Procedure

Proceed as follows to simulate a project:

| Symbol | Meaning |
| --- | --- |
| 1. Disconnect the connection to the controller or switch the controller off if you do not want to test the function of the entire process. 2. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".    Runtime starts and the simulator opens with all the configured tags. 3. Select the "New tag" command in the "Edit" menu to add a tag to the tag simulator. 4. Select the tag from the WinCC tag management. 5. In the tag simulator, select the required tag on the "Tags" tab to supply a tag with simulated values. 6. Configure the simulation mode on the "Properties" tab:    - Select the simulation mode.    - Enter values for the simulation.    - Click "Active" to include the tag in the simulation.        | Symbol | Meaning |      | --- | --- |      |  | **Warning** |      | Make sure once again that the configuration computer cannot pass any changed tags to the PLC in the active process. If you have not switched the PLC off, the simulated tag values will be passed to the PLC and the runtime process. |  | 7. Click the "Start simulation" button on the "Properties" tab. 8. Observe the effect the simulation has on your project in Runtime. 9. Click on the "Stop simulation" button to stop the simulation. 10. To save the settings for the simulation, select the menu command "File &gt; Save" and enter a corresponding name.     The file is automatically given the *.sim extension. |  |

##### Managing simulation data

If you have saved data from a previous simulation, you can open the file at a later point in time and simulate your project again. The tags and area pointers to be simulated must remain unchanged in the project, otherwise the saved simulation data will no longer match your project.

Proceed as follows to open a simulation file:

1. Select the menu command "Online &gt; Simulate Runtime &gt; With tag simulator".
2. Select the menu command "File &gt; Open" in the tag simulator.
3. Select the corresponding simulation file and click "Open".

   The simulator loads the stored data.

##### Enabling and disabling tags

You can start and stop the simulation for each individual tag to enable a bumpless transition from the offline configuration to online configuration. Enable the "Active" check box in the "Properties" tab for this purpose.

When a tag is enabled, the simulation values are calculated and transferred to the tag simulator.

##### Deleting a tag

To delete a tag from the tag simulator, follow these steps:

1. Select the tag name.
2. Select the menu command "Edit &gt; Delete".

The tag is removed from the table.

---

**See also**

[Simulation basics (Panels, Comfort Panels, RT Advanced)](#simulation-basics-panels-comfort-panels-rt-advanced)

#### Simulating a screen (RT Professional)

##### Introduction

If you have only made changes to one screen, you can temporarily specify this screen as the start screen for simulation. In this way, you can debug changes without having to modify the start screen, or opening the screen on the HMI device.

##### Requirements

You created a project that contains at least one screen.

##### Procedure

To define a screen as temporary start screen for simulation, follow these steps:

1. In the project navigation, select the image to display as the start screen in the simulation.
2. Select the "Start simulation" command from the shortcut menu of the screen.

##### Result

Project simulation is started. Instead of the configured start screen, the simulation window the screen you selected in the project navigation.

#### Simulation restrictions (RT Professional)

##### Connection

The connection to PLCSim is only possible via an integrated connection.

##### Alarms with dynamic parameters

If you use tags or text lists as external tags for alarms, the dynamic parameters of the alarms are not displayed.

Only internal tags are enabled for the simulation of alarms in the tag simulator .

Use PLCSim to simulate dynamic parameters.

##### Panels

If you want to use PLCSim with version V14 or higher for simulation with a panel, the device version of the panel must be 14.0.0.0 or higher.

#### Simulating tags with the Tag Simulator (RT Professional)

This section contains information on the following topics:

- [The WinCC Runtime Professional Tag Simulator (RT Professional)](#the-wincc-runtime-professional-tag-simulator-rt-professional)
- [The "Tag simulation" editor (RT Professional)](#the-tag-simulation-editor-rt-professional)
- [Inserting tags in the "Tag simulation" editor (RT Professional)](#inserting-tags-in-the-tag-simulation-editor-rt-professional)
- [Configuring functions for the simulation (RT Professional)](#configuring-functions-for-the-simulation-rt-professional)
- [How to simulate tags (RT Professional)](#how-to-simulate-tags-rt-professional)
- [Simulating tags via script (RT Professional)](#simulating-tags-via-script-rt-professional)
- [Setting the language (RT Professional)](#setting-the-language-rt-professional)

##### The WinCC Runtime Professional Tag Simulator (RT Professional)

The WinCC Runtime Professional Tag Simulator is used to simulate internal tags and process tags. You use it, for example, to simulate the behavior of objects and scripts in the WinCC project.

To configure and activate the simulation, use the "Tags simulation" simulator.

###### Brief description

The following general conditions apply for the simulator:

| Symbol | Meaning |
| --- | --- |
| Tag types | Process tags, internal tags and structure tags can be simulated.  You can find unsupported tag types under "[Inserting tags in the "Tag simulation" editor](#inserting-tags-in-the-tag-simulation-editor-rt-professional)". |
| Quantity structure | A maximum of 300 tags can be simulated at the same time.  However, you can configure and save more tags in the simulator. |
| Update cycle | The update time for tag values is one second.  Specify a multiple of a second using the "Cycle" parameter. |
| Online configuration | Configuration changes of the simulation are immediately visible in Runtime. |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Effects on connected controls**  Simulated tag values can be transferred to connected controllers.  When the WinCC project is connected to a controller, WinCC writes the simulated process values to the automation system.  This can lead to a reaction of the connected process I/Os.  **Disconnect hardware**  Before using the simulator, ensure that  - No hardware is connected, if possible. - The connected hardware represents no danger even when values are extreme.   **Recommendation**  Simulate the process values without process connection. |  |

###### Application examples

Typical fields of applications for the Simulator:

- Testing the configuration without connected process I/Os
- Testing of the configuration with connected process I/Os, but without running process

You can simulate process tags both with and without connected process I/Os.

**Testing a WinCC project**

Use the simulator to test a configuration without connected process I/O or without running process.

When process I/Os are connected, the process tags can be directly supplied with values using the simulator.

A function test of the operating and monitoring system with connected hardware offers the following options, for example:

- Check of limit levels and message outputs.
- Test the integration of alarms, warnings, and error messages and check of status displays.
- Preset, readout, and change of digital and analog inputs and outputs.
- Alarm simulation.

**Presenting a WinCC project**

Another application of the simulator is the implementation of a project for demonstration purposes.

A process connection is usually not available for the presentation of the operator control and monitoring system.

In this case the simulation takes over the control of the internal tags and the process tags.

---

**See also**

[Inserting tags in the "Tag simulation" editor (RT Professional)](#inserting-tags-in-the-tag-simulation-editor-rt-professional)

##### The "Tag simulation" editor (RT Professional)

###### Start WinCC Runtime Professional Tag Simulator

To configure and activate the simulation, use the "Tags simulation" simulator. The simulator opens in a separate window.

You have several options to start the simulator.

**From the TIA Portal**

In the menu bar, select "Online &gt; Simulation &gt; With Tag Simulator".

A simulation is started and the "Tags simulation" simulator opens.

**Via the Windows user interface**

Select one of the following options:

- In the Windows program group "Siemens Automation", select the entry "WinCC Runtime Professional Tag Simulator".
- Search via the task bar for "WinCC Runtime Professional Tag Simulator" and start the simulator.

The "Tags simulation" simulator opens. No simulation is started.

###### Simulation file

You can save a configured simulation as a file in "*.sim" format and call it up again later.

**Save simulation file**

1. In the simulator, select "File &gt; Save" or "Save as".
2. Select a target directory and a file name.

Target directory:

- If you have started the simulator from the TIA Portal together with the simulation, a default folder is proposed as target directory.
- If you started the simulator via the Windows user interface while a project is in RUN in Runtime, the simulation file is saved to the following directory:

  &lt;Path to the active RT project&gt;\Simulation

  > **Note**
  >
  > **Overwrite the simulation file by full download**
  >
  > Simulation files saved in the Project folder are overwritten by calling the "Load (complete)" command.

**Open simulation file**

1. In the simulator, select "File &gt; Load".
2. Select the desired simulation file or the path to the desired file.

If you have started the simulator from the TIA Portal together with the simulation, the default directory for saving will be suggested. If you have saved the file in another directory, select this directory.

###### Areas of the simulator

The simulator consists of the data area and the Properties window.

![Areas of the simulator](images/139538953355_DV_resource.Stream@PNG-en-US.png)

**Window "Properties - Tag"**

To display and edit the properties of a tag in a clear form, use the Properties window.

The property window contains no simulation values or runtime values of the tags.

The "..." button in the "Tag name" column loads the tag selected in the "Properties - Tags" window into the Tags editor.

**Data area**

To set the same property for multiple tags, work in the data area and use, for example, the automatic continuation ("Drag Down").

The data area additionally contains the simulation values and runtime values of the tags.

**"Simulation" menu**

The menu bar contains the entry "Simulation".

When the WinCC project is activated in runtime, the "Start" and "Stop" entries are active. This allows you to start and stop the configured simulation.

###### Tag properties

You edit the properties in the data area or in the properties window.

| Name | Property | Description |
| --- | --- | --- |
| Tag name | Inserted tag | Enter the name of a tag or select a tag in the tag selection dialog.  You can find additional information under "[Inserting tags in the "Tag simulation" editor](#inserting-tags-in-the-tag-simulation-editor-rt-professional)". |
| Object type | Tag | - |
| Object name | Tag name | Display: Inserted tag |
| Data type | Tag type | Display: Data type of the inserted tag |
| Active | Activating the tag for the simulation | A maximum of 300 tags can be simulated at the same time.  To activate all inserted tags, select the "Active" column in the data area and select the entry "Select all" in the shortcut menu.  When more than 300 tags are inserted, the first 300 tags are activated. |
| Cycle | Update cycle | Base is 1 second.  To extend the cycle, enter a value &gt; 1. |
| Function | Simulation function | Select the function from the drop-down list. |
| Parameters of the simulation functions |  | You can find the description of the parameters under "[Configuring functions for the simulation](#configuring-functions-for-the-simulation-rt-professional)".  In the data area, the parameters of the simulation functions are hidden in the standard view. To show these columns, select "Show" from the column header shortcut menu. |

###### Runtime values in the data area

The runtime values of the simulated tags are only displayed or entered in the data area.

These fields are not included in the properties window.

| Column | Description |
| --- | --- |
| Value set | Value transferred by the simulator.  "User input" function  - If Runtime is activated, enter the required value in the field. - To display the slider, click the displayed button: ![Runtime values in the data area](images/141015712651_DV_resource.Stream@PNG-de-DE.png) |
| Current value | Current tag value in runtime |
| Time stamp | Current time stamp of the tag value in runtime |
| Quality set | Quality code set by the simulator.  Select the quality code from the drop-down list.  Default setting:  - 0x60: Uncertain; Simulated value <sup>1)</sup> |
| Quality code | Current quality code of the tag in runtime |
| Tag status | Current tag status in runtime |

###### Quality code in runtime

When the controller is connected and active when simulating a process tag, the displayed quality code is influenced by the actual values.

The simulator sets the quality code according to the update cycle.

As soon as the value is read by the controller, the "Quality Code" field shows the actual quality code until the simulator sets the next value.

**No quality code with S7-1500 controllers**

The "SIMATIC S7-1500" controllers do not support the WinCC Quality Code.

As long as there is no connection to the S7-1500 controller, you can simulate a quality code.

With an active S7-1500 connection, the default value is always displayed as the quality code.

---

**See also**

[Inserting tags in the "Tag simulation" editor (RT Professional)](#inserting-tags-in-the-tag-simulation-editor-rt-professional)
  
[Configuring functions for the simulation (RT Professional)](#configuring-functions-for-the-simulation-rt-professional)

##### Inserting tags in the "Tag simulation" editor (RT Professional)

###### Inserting tags

You have the following options for inserting tags in the WinCC Runtime Professional Tag Simulator:

- Enter tag name
- Applying tags from the tag selection dialog

**Tag Management: Consistency**

You can only add tags that have been created and compiled in the engineering system in the Tag Management.

If a tag has been renamed or deleted in the Tag Management, the line in the simulator is highlighted in red.

###### Supported tags

The following tags can be simulated:

- Process tags
- Internal tags
- Structure tags
- Structure tag elements

**Insert structure tags**

When you insert complete structures in the form of structure tags, note the following.

- A structure tag is inserted collapsed.

  To expand the structure, click the arrow in front of the tag name.
- Simulate the contained structure tag elements independently of each other, like single tags.
- You can only delete inserted structure tags as complete structures.

  You cannot delete lower-level elements individually.

**Restrictions**

Simulation of the following tag types is not supported:

- Raw data tag
- Text reference
- Date/time

###### Tag name

Enter the name in the "Tag name" field. Make sure that the name is case-sensitive.

The tag or structure tag is searched for in Tag Management and inserted.

###### Tag selection dialog

Open the tag selection dialog and apply the required tags.

**Procedure**

1. In the "Tag Name" field, click the button that appears: ![Tag selection dialog](images/141015712651_DV_resource.Stream@PNG-de-DE.png)
2. Select one or more tags and click "Apply".

   The tag selection dialog can remain open for additional selections.
3. To add more tags, click the next empty line in the data area.

   When an already filled line is selected in the data area, this tag is overwritten during insertion.

###### Delete tag

To delete a tag in the data area, click the corresponding line number. The line is highlighted.

Select "Delete" from the shortcut menu or press the &lt;Del&gt; key.

The tag is deleted, without further prompt, from the list of tags to be simulated.

##### Configuring functions for the simulation (RT Professional)

###### Functions for the simulation

Select how the tag value is simulated for each tag.

The following functions are available:

- Sine
- Oscillation
- Random values
- Increment
- Decrement
- User input (slider)
- Script

**"Binary tag" data type**

The "Sine" and "Oscillation" function are not supported by binary tags.

###### Sine function

Periodic, non-linear function:

| Parameters | Description |
| --- | --- |
| Amplitude | Value range |
| Offset | Zero point for the value range |
| Oscillation period | Duration of period in seconds |

###### Oscillation

Simulation of jumps of a setpoint:

| Parameters | Description |
| --- | --- |
| Overshoots | Maximum deviation from the rated value |
| Rated value | Value around which the oscillations are occurring |
| Oscillation period | Time interval of the oscillation in seconds.  The oscillation restarts after the specified time has elapsed. |
| Damping | Reduction of amplitude within the oscillation period |

###### Random values

Randomly generated values:

| Parameters | Description |
| --- | --- |
| Random minimum value | Smallest possible value |
| Random maximum value | Greatest possible value |

###### Increment

Up counter which restarts at the minimum value when it reaches the maximum value:

| Parameters | Description |
| --- | --- |
| Initial value Increment | Minimum value  The start value is applied at runtime start. |
| End value Increment | Maximum value |
| Step Increment | Value increase, e.g. in increments of 10 |

###### Decrement

Down counter; restarts the maximum value after having reached the minimum value:

| Parameters | Description |
| --- | --- |
| Initial value Decrement | Maximum value  The start value is applied at runtime start. |
| End value Decrement | Minimum value |
| Step Decrement | Value reduction, e.g. in decrements of 10 |

###### User input

Enter in the "Value set" table field or use the slider:

| Parameters | Description |
| --- | --- |
| Slider minimum value | Lowest value that can be entered or selected with the slider |
| Slider initial value | Value at runtime start |
| Slider maximum value | Highest value that can be entered or selected with the slider. |

**Slider**

1. To open the slider in runtime, click in the "Value set" field in the table area.
2. Click the displayed button: ![User input](images/141015712651_DV_resource.Stream@PNG-de-DE.png)
3. Move the bar with the mouse or the cursor keys.
4. Close the slider using the "x" in the top-right.

**Text tags**

In addition to numbers, you can also set letters as start value for text tags.

The slider is not displayed. The "Minimum value" and "Maximum value" fields are inactive.

###### Script

VBScript function with the return value that is written to the WinCC tag:

| Symbol | Meaning |
| --- | --- |
| Apply code | Deactivated: Only the "VBS function" option is active.  Activated: Only the "VBS code" option is active. |
| VBS function | Selection of a created VBS function  To select a VBS function, click on the button displayed in the field: ![Script](images/141015712651_DV_resource.Stream@PNG-de-DE.png) |
| VBS code | Entering a new VBS function  The function is stored in the simulation file.  To open the VBS editor, click on the button displayed in the field: ![Script](images/141015712651_DV_resource.Stream@PNG-de-DE.png) |

##### How to simulate tags (RT Professional)

In the WinCC Runtime Professional Tag Simulator, select the tags you want to simulate.

Select the simulation type and the update cycle for each tag.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Effects on connected controls**  Simulated tag values can be transferred to connected controllers.  When the WinCC project is connected to a controller, WinCC writes the simulated process values to the automation system.  This can lead to a reaction of the connected process I/Os.  **Disconnect hardware**  Before using the simulator, ensure that  - No hardware is connected, if possible. - The connected hardware represents no danger even when values are extreme.   **Recommendation**  Simulate the process values without process connection. |  |

###### Requirement

A simulation is running or a project is running in Runtime.

###### Procedure

1. Insert the required tags.

   To open the tag selection dialog, click the displayed button in the "Tag name" column: ![Procedure](images/141015712651_DV_resource.Stream@PNG-de-DE.png)

   Other possible procedures:

   - "[Inserting tags in the "Tag simulation" editor](#inserting-tags-in-the-tag-simulation-editor-rt-professional)"
2. Select the function for the simulation.
3. Select the other function parameters in the "Tag properties" area.

   ![Procedure](images/139538953355_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/139538953355_DV_resource.Stream@PNG-en-US.png)
4. To change the update cycle, enter a number &gt; 1 in the "Cycle" field.

   An update cycle of 1 second is the basis. To change the simulated value, every 5 seconds for example, enter "5".
5. If necessary, select the quality code in the "Quality set" column.

   The selected quality code is also set each time a simulated tag value is written.
6. Activate the simulation of the required tags in the "Active" column.

   You can simulate a maximum of 300 tags simultaneously, even if more tags are configured in the simulator.
7. Save the simulation using the menu command "File &gt; Save as".

   This allows you to reuse the projected simulation later, for example, to test a changed configuration.
8. Start the simulation using the menu command "Simulation &gt; Start".

   - The simulated values are displayed in the "Value set" column.
   - The actual values of the tags are displayed in the "Current value" column.
   - The respective, actual quality code is displayed in the "Quality Code" column.

   ![Procedure](images/164174451851_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164174451851_DV_resource.Stream@PNG-en-US.png)
9. To stop the simulation, select the menu command "Simulation &gt; Stop".

   The simulation is also closed when WinCC Runtime is deactivated.

---

**See also**

[Inserting tags in the "Tag simulation" editor (RT Professional)](#inserting-tags-in-the-tag-simulation-editor-rt-professional)

##### Simulating tags via script (RT Professional)

The "Script" simulation function provides the following options to simulate tag values:

- Setting a tag value using a VBScript function
- Read out or set values from other WinCC tags

The following VBS objects are supported:

- Tags object
- SmartTags object.
- HMIruntime object: Trace function

  Other functions of the HMIruntime object are not supported.

###### VBS function: Select source

Use the "Apply code" property in the "Tag properties" window to select the source:

| "Apply code" field | Source | Procedure |
| --- | --- | --- |
| disabled | The "VBS function" field contains the name of the selected VBS function. | Create a function in the VBScript editor.  To select the function in the simulator, click the displayed button in the "VBS function" field. |
| enabled | The "VBS code" field contains the code of the VBS function. | To open the internal VBS editor, click the displayed button in the "VBS Code" field.  Create the required function.  The function is saved in the simulation file and is only available in the simulator. |

###### Restrictions

- Tags whose name starts with the prefix "@" cannot be addressed in scripts via the simulator.
- You cannot deactivate a tag with the "Script" simulation function as long as the simulation is active in runtime.
- If the script cannot be processed in the current cycle, it is not called up again until of next update cycle after processing has been completed.

  To deactivate the tag simulation and correct the script, stop the simulation using the menu item "Simulation &gt; Stop".

###### Transfer parameters

The VBS function must have a transfer parameter.

An object with the following properties is transferred to the script during the execution:

| Read/write access | Property | Description |
| --- | --- | --- |
| Read and write | Value <sup>1)</sup> | The script reads or writes the last calculated tag value. |
| UserData | The script can cache a value. |  |
| QualityCode | Quality code as numeric value which is set when the tag is written. |  |
| Read only | Tag name | Name of the WinCC tag with the value the script calculates |
| Data type | The data type of the tag as numerical value |  |
| Counter | Counter with which the cycle is increased |  |
| 1) In the simulator you can only create procedures of the "Sub" type. The value to be set is written in the "Value" parameter. The "Function" type is only supported in the project modules or standard modules. In this case, the return value is written to the tag. |  |  |

###### Example script: Set tag value

Set a calculated value as "MyCalculatedValue" with the quality code "0x48: Uncertain - Substitute set".

If you do not formulate a calculation, the value is incremented by +1.

'VBS378

Sub Tag_Simulation_01 (Byval Item)

MyCalculatedValue = Item.Counter

' do your own calculation

' ...

' write the calculated value to be set by WinCC Runtime Professional Tag Simulator

Item.Value = MyCalculatedValue

Item.QualityCode = 72

End Sub

###### Example script: Access to tags

To read out or set the tag value of WinCC tags, use the Tags object or SmartTags object.

You use the trace function via the HMIruntime object. The text is displayed in the diagnostic window of the simulator.

**Tags object**

'VBS379

Sub SimulatedTag_address_02 (Byval Item)

Dim group

Set group = Tags.CreateTagSet

' add tags "Simulation_x" to the collection

group.Add "Simulation_3"

group.Add "Simulation_4"

' set the values of the tags

group("Simulation_3").Value = Item.Counter

group("Simulation_4").Value = Item.Counter +1

' write the values to the DataManager

group.Write

' write trace text

HMIruntime.Trace "Simulation: Tag values set"

End Sub

**SmartTags object**

'VBS380

SmartTags("Simulation_5") = 7

##### Setting the language (RT Professional)

To change the interface language in the WinCC Professional Runtime Tag Simulator, proceed as follows:

1. Start the "WinCC RT Start" tool.
2. Select "View &gt; Language".
3. Select a language.
4. Restart the simulator.

The simulator adopts the changed language setting.

### Loading projects (RT Professional)

This section contains information on the following topics:

- [Overview for loading of projects (RT Professional)](#overview-for-loading-of-projects-rt-professional)
- [Downloading the project to an HMI device (RT Professional)](#downloading-the-project-to-an-hmi-device-rt-professional)
- [Downloading the project to a file system (RT Professional)](#downloading-the-project-to-a-file-system-rt-professional)
- [Online delta transfer for Runtime Professional (RT Professional)](#online-delta-transfer-for-runtime-professional-rt-professional)
- [Updating a runtime project on an HMI device to V13 SP1 (RT Professional)](#updating-a-runtime-project-on-an-hmi-device-to-v13-sp1-rt-professional)

#### Overview for loading of projects (RT Professional)

##### Overview

Delta data of the project is automatically compiled before you download it to one or several HMI devices. This always ensures that the latest version of the project is transferred.

When you execute the "Load (complete)" command, you need to confirm overwriting of the project.

> **Note**
>
> **Loading Runtime onto another PC**
>
> After the installation, you must activate remote communication in the "Simatic Shell" dialog before loading a project onto another PC for the first time. To do so, proceed as follows:
>
> 1. Open the communication settings in Windows Explorer using the shortcut menu of Simatic Shell.
> 2. Activate the option "Remote communication".
> 3. Configure encrypted communication in the network: Select the PSK and the port.
> 4. Select the network adapter and, if necessary, the multicast settings.

##### Loading a project to an HMI device

The following steps are completed prior to downloading:

1. The download settings are verified. The "Extended download to device" dialog box opens automatically during the initial download of a project to an HMI device. You use this dialog to define the protocol and interface or destination path for the project in accordance with the HMI device Runtime used.

   If the HMI device is part of a subnet, for example, you also select the subnet and the first gateway.

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens.
2. The project is compiled. Warnings and errors during compilation are displayed in the Inspector window and in the "Load preview" dialog box.
3. The "Load preview" dialog box shows you the following information for each HMI device:

   - The individual steps for loading
   - Check the runtime version of the target HMI device  
     If the version of WinCC Runtime Professional installed on the target device does not match the configured device version, you cannot start the loading.
   - Presettings that take effect at loading. You can change the default settings for this download process, if necessary.
   - Warning events (optional). You can download a project while ignoring the "warnings". The functionality might be restricted in runtime.
   - Error events (optional). You can download a project even if it has errors. In the "Load preview" dialog under "Actions", select the check box "The project has not been compiled without errors. Do you want to continue loading?" and click "Load".

     WinCC will open the invalid configuration in the corresponding editor if you double-click the error message in the Inspector window. Correct the errors and reload the project.

If you are using HMI tags in your project that are connected to PLC tags, you should also compile the user program before you compile the HMI device.

##### Loading a project without a connected HMI device

If you cannot establish a direct connection from the configuration PC to the HMI device, load the compiled project on a USB stick and then copy it to the appropriate directory on the HMI device using the Windows Explorer.

##### Loading with S7 routing

Configure the S7 routing settings in the "Devices &amp; Networks" editor in the relevant PLC. The settings depend on the device configured.

S7 routing supports the following protocols:

- MPI/PROFIBUS
- PN/IE

##### Transferring Runtime add-ons in WinCC

Projects can contain Runtime add-ons in the form of controls or CSP (Communication Support Packages). These Runtime add-ons are automatically transferred with the project.

##### Loading inconsistent projects

Loading inconsistent projects to a device can result in the loss of the online delta load capability of the device. Therefore, the system prevents the loading of inconsistent projects in Runtime Professional. You can only simulate a Runtime project or load it onto a device if no errors were output during compiling. The options "Complete load", "Online delta loading" and the loading via data carrier are not available with inconsistent projects. If the system determines inconsistencies, an error message in the "Load preview" dialog box informs you that the project cannot be loaded on the device.

Inconsistencies in VB scripting and C scripting are an exception. You can load or simulate a project with errors in VB scripting and C scripting on a device if you have selected the check box "Start even with corrupt scripts" under "Runtime settings &gt; General &gt; Script options".

---

**See also**

[Settings for the multi-user system (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#settings-for-the-multi-user-system-rt-professional)

#### Downloading the project to an HMI device (RT Professional)

##### Introduction

Before a project can run on an HMI device, you must first load it to the HMI device. During loading, you must most importantly specify whether existing data on the HMI device such as "user administration" and "recipe data" is to be overwritten. As a general rule, only one project can be active in Runtime on an HMI device.

You can use a project from engineering system to an HMI device using the command "Download (complete)" or with the command "Delta load".

If the HMI device supports PROFINET, the name of the HMI device entered in the project tree is used as the device name for the PROFINET communication. The name is written to the HMI device during download. If a device name for the PROFINET communication has already been entered in the HMI device, it will be overwritten.

Please note the following when downloading a project to an HMI device:

- You can download a project from the configuration PC to the HMI device if no project is open or in Runtime on the HMI device.
- If the configuration PC also serves as HMI device, download the project to your project directory in the file system.
- If a project is open on the HMI device, you can only completely reload this particular project from the configuration PC to the HMI device. Close the project open on the HMI device to download a different project to the HMI device.

  Example: The project "Mixing" is open on the HMI device but not in Runtime. If you change the project, download the changes to the HMI device with "Software (all)". Close the project "Mixing" on the HMI device to download the project "Bottling" to the HMI device, for example.
- You can load certain changes to the configuration data without stopping Runtime (delta loading) if a project is in Runtime on the HMI device. You will be notified if a change means delta loading is no longer possible. If delta loading is no longer possible, you will only be able to download the project to the HMI device using "Download (complete)". Runtime is thereby disabled and started again, which may result in plant downtime.

  You will have to exit Runtime and close the project on the HMI device to download another project to the HMI device.
- To load a project of a predecessor WinCC version, first upgrade the project to your WinCC version.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Device version**  If the device version of the target HMI device does not correspond to that of the configured device version, Runtime cannot be started after loading.  Verify that the device version of the target HMI device conforms to your configuration before you compile and download your project.   If necessary, change the device version manually via the properties of the HMI device. |  |
- If the selected destination directory on the HMI device is empty, The "Download to device (complete)" command is executed automatically once the "Extended download to device" dialog is filled out.
- If the selected directory contains a runtime project of the same name and you execute the "Download (complete)" command, you need to confirm overwriting of the project.
- If the selected directory contains a runtime project of the same name and Runtime is activated, you can alternatively execute the "Delta load" command.
- If the name of the runtime project does not match the project name on the engineering project, the project is not loaded.
- Loading inconsistent projects is prevented by the system in Runtime Professional. You can only simulate a Runtime project or load it onto a device if no errors were output during compiling. If the system determines inconsistencies, an error message in the "Load preview" dialog box informs you that the project cannot be loaded on the device.

  Inconsistencies in VB scripting and C scripting are an exception. You can load or simulate a project with errors in VB scripting and C scripting on a device if you have selected the check box "Start even with corrupt scripts" under "Runtime settings &gt; General &gt; Script options".

##### Requirement

- You have created an HMI device in the project.
- The HMI device is connected to the configuration PC or the configuration PC serves as HMI device.
- The same type of communication is set, for example, encrypted communication, on the configuration PC and the HMI device. Alternatively, use the migration mode on one of the devices (see [Remote access and encrypted communication](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#remote-access-and-encrypted-communication-rt-professional)).
- The same password is assigned at both ends with encrypted communication.

##### Procedure

Proceed as follows to load a project:

1. To download a project simultaneously to several HMI devices, select the HMI devices by means of multiple selection in the project tree.
2. Select the "Download to device &gt; Software" command from the shortcut menu of an HMI device.
3. If the "Extended download to device" dialog opens:

   - Select the "destination path" for the compiled project on the HMI device.

     The Windows user group "SIMATIC HMI" must have full access to this destination path.

     Full access is usually set during installation of WinCC Runtime for the "WinCC Projects" file. The location of this folder in the file system depends on the operating system of the HMI device.
   - Click "Load".

   You can open the "Extended download to device" dialog at any time with the menu command "Online &gt; Extended download to device...".

   The "Load preview" dialog box opens. The project is compiled at the same time. The result is displayed in the "Load preview" dialog box.
4. Check the displayed defaults and change them as necessary:

   - Select the data to be transferred.
   - Select whether Runtime is to be started on the target system after loading.
   - Select whether the autostart can be canceled.
   - Select whether the operating system can be accessed during startup.
5. Click "Load".

**Note**

With multiple runtime projects, create a separate directory for each project. The directory must be empty when you load a project to an HMI device for the first time.

##### Result

The project is loaded to all selected HMI devices. If errors or warnings occur during the download, corresponding alarms are displayed under "Info &gt; Load" in the Inspector window.

On completion of the successful download of the project, you can execute it on the HMI device. If starting of Runtime on the target system was activated in the "Load preview" dialog box, the project is started in Runtime after loading.

---

**See also**

[Activating and deactivating projects on the WinCC server (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#activating-and-deactivating-projects-on-the-wincc-server-rt-professional)
  
[Overview of online delta transfers (RT Professional)](#overview-of-online-delta-transfers-rt-professional)
  
[Settings for the multi-user system (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#settings-for-the-multi-user-system-rt-professional)

#### Downloading the project to a file system (RT Professional)

##### Introduction

If the configuration PC has no connection to the HMI device, download the project to the HMI device offline via a USB data storage medium or a CD. To do this, first copy the Runtime project to your HMI device and start the project in Runtime Professional with "WinCC RT Start".

The PC on which Runtime is activated is referred to as the HMI device.

During loading, the "Load preview" dialog box opens. In this dialog, you can specify whether the user administration or logs, which have been changed on the HMI device in the meantime, are to be overwritten or retained.

> **Note**
>
> Existing data in the user management or in the logs are overwritten when you start the downloaded runtime project.
>
> To retain changes of the user administration, export the user administration and import the data again after starting the copied runtime project. You make the settings for overwriting in the "Overwrite" area of the "Load preview" dialog.

##### Requirement

A project is open.

##### Procedure

To download a project to a file system, follow these steps:

1. Select the project in the project tree.
2. Select the "Online &gt; Download to file system" menu command.

   A dialog opens.
3. Select the storage path and click "OK".

   The project is compiled.
4. When the "Load preview" dialog box opens, select the data to be transferred.
5. Select one of the following options under "Options for data logging":

   - "Retain": If the project has already been transferred from the Engineering System to the PC, the data on the PC is not overwritten by the data of the Engineering System.
   - "Reset": The data on the PC is overwritten by the data of the Engineering System.
   - "Transfer": The data is transferred from the Engineering System to the PC.
6. Click "Load".

   The Runtime project is saved on the drive.

   If necessary, transfer the runtime project to a USB data storage medium or burn the project on a CD.
7. Transfer the runtime project to your HMI device.
8. Start Runtime and open the downloaded project.

---

**See also**

[WinCC RT Start (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#wincc-rt-start-rt-professional)

#### Online delta transfer for Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Overview of online delta transfers (RT Professional)](#overview-of-online-delta-transfers-rt-professional)
- [Use and limitations of online delta loading (RT Professional)](#use-and-limitations-of-online-delta-loading-rt-professional)

##### Overview of online delta transfers (RT Professional)

###### Online delta loading

WinCC lets you edit a project on the configuration PC while the same project is active in Runtime. If you change the project on the configuration PC, for most configuration changes you can load the changed components onto the HMI device by means of "Online delta loading". Online delta loading requires less time compared to the loading of the entire project. During online delta loading, The "Load preview" dialog box opens. In this dialog you specify whether user administration or logs, which have been changed on the HMI device in the meantime, are overwritten or retained during online delta loading.

> **Note**
>
> Changes to the project made in the meantime on the HMI device, for example in the user administration or in the logs, are lost during the online delta loading.
>
> To retain changes to the user administration, export the user administration and import again following the online delta loading.

> **Note**
>
> **Device version**
>
> If the device version of the target HMI device does not correspond to that of the configured device version, delta transfer is not possible.
>
> Before the delta transfer of your project, check whether the device version of the target HMI device corresponds to your configuration and, if necessary, update the version of your HMI device.

Note the following for online delta loading:

- If online delta loading is initiated without Runtime being active, the complete project is loaded.
- Online delta loading is not possible during a simulation.

  To terminate the simulation automatically before loading and to resume after loading, select the appropriate option in the "Load preview" dialog box.

> **Note**
>
> Loading inconsistent projects to a device can result in the loss of the online delta load capability of the device. Therefore, the system prevents the loading of inconsistent projects in Runtime Professional.

###### Complete transfer

Fundamental changes to configuration data may prevent the online delta transfer. In this case, a message informs you of the failure of the online delta loading after you initiated the transfer. You then have to reload the entire project to the HMI device. You must explicitly confirm this Runtime restart on the HMI device in the "Load" dialog. You can cancel loading at this point.

The following will happen if you start complete loading while the project on the configuration PC is in Runtime on the HMI device:

- Runtime is stopped
- The entire project is downloaded to the HMI device
- Runtime is restarted

Note that starting and stopping of Runtime can result in plant downtime.

###### Application scenarios

You will have to adapt your configuration in various different phases of your project, for example, commissioning, operation and maintenance. You can then transfer these changes to the HMI device online without having to exit Runtime.

Cases in which online delta loading is used include:

- Continuous automation tasks:

  All changes should be made online from a central configuration PC. This saves you having to make changes to the configuration locally. You can also add, change and delete Runtime objects such as tags, alarms and logs without having to exit Runtime.
- Testing changes in a protected environment:

  You can perform the planned changes offline on the configuration PC before these are downloaded to the HMI device. Configuration engineers can simulate the changes in a protected environment before activating the delta data in the process. This allows you to identify and clear configuration errors before they can cause any problems in the process or lead to a plant shutdown.

---

**See also**

[Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)
  
[Use and limitations of online delta loading (RT Professional)](#use-and-limitations-of-online-delta-loading-rt-professional)
  
[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
  
[Exporting the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#exporting-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#importing-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)

##### Use and limitations of online delta loading (RT Professional)

###### Introduction

The online delta loading capability is lost in some configurations.

###### Files and elements

The table below shows for which actions the online delta transfer capability is retained and for which actions it is not retained:

| Element | Create | Delete | Edit | Remarks |
| --- | --- | --- | --- | --- |
| Project name/properties of the project | - | - | No | - |
| HMI device | Yes | No | No | - |
| Properties of the HMI device | - | - | No | Edit:  Changes are only activated in Runtime by deactivating the project and restarting Runtime. |
| User cycle  (project properties) | No | No | No | - |
| Connections  ("HMI Tags" editor) | No | No | No | - |
| Parameter of a connection  ("HMI Tags" editor) | No | No | No | - |
| Alarms | - | - | - | See the "Online configuration for alarms" table below |
| Menus and toolbars | No | No | No | - |

###### Online configuration for alarms

| Element | Attribute | Create | Delete | Edit | Remarks |
| --- | --- | --- | --- | --- | --- |
| - | - Alarm number - Alarm group | - | - | No | - |
| - | - Alarm class | Yes | No | Yes | Inactive alarms are updated immediately if you change the alarm class without changing mandatory acknowledgment.  If the mandatory acknowledgment of a currently active alarm and of an unacknowledged alarm is changed, the system acknowledges the active alarm.  An active alarm that is changed to an alarm without "deactivated" state will be deactivated. |
| User-defined alarm group | - | Yes | No | Yes | - |
| Limit values for analog alarms | - | No | No | No | - |
| Alarm classes | - | Yes | No | Yes | Edit:  Valid for most attributes. Exceptions are listed individually: |

> **Note**
>
> **Displaying PLC alarms**
>
> If you change the configuration of the option "Automatic update" after compiling and loading under "Runtime settings &gt; Alarms &gt; PLC alarms", the online delta load capability is lost.

---

**See also**

[Overview of online delta transfers (RT Professional)](#overview-of-online-delta-transfers-rt-professional)
  
[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Rules on online delta loading (RT Professional)](#rules-on-online-delta-loading-rt-professional)

#### Updating a runtime project on an HMI device to V13 SP1 (RT Professional)

##### Introduction

If you have updated a TIA Portal V13 project to V13 SP1 on your engineering system, you can also update your runtime project on the HMI device from V13 to V13 SP1. The project is completely transferred from engineering system to the destination directory of your HMI device. The existing runtime data can be transferred as well.

To transfer an updated V13 SP1 project from engineering system to an HMI device, note the following:

- The corresponding old version of the runtime project must be available in the selected destination directory. In this case, you need to confirm the overwriting of the runtime project in the "Load preview" dialog.

##### Procedure

To transfer to an updated V13 SP1 project from engineering system to an HMI device and update an existing runtime project on the HMI device to version 13 SP1, follow these steps:

1. Select the project in the project tree on the engineering system.
2. Select the "Online &gt; Download to device" menu command.

   Alternatively, you can select the command "Download to device &gt; Software (all)" from the shortcut menu of the HMI device.

   The "Extended download to device" dialog opens.
3. Select the destination directory of the old runtime project under "Path of the target folder".
4. Click "OK".

   The project is compiled.
5. When the "Load preview" dialog box opens, select the data to be transferred.
6. Confirm the overwriting of the target project.
7. Click "Load".

   The updated runtime project is transferred to the HMI device.

### Compiling and loading with Multiuser Engineering (RT Professional)

This section contains information on the following topics:

- [Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
- [Compiling in the server project view (RT Professional)](#compiling-in-the-server-project-view-rt-professional)
- [Compiling in the local session (RT Professional)](#compiling-in-the-local-session-rt-professional)
- [Rules on online delta loading (RT Professional)](#rules-on-online-delta-loading-rt-professional)
- [Online delta loading from the server project view (RT Professional)](#online-delta-loading-from-the-server-project-view-rt-professional)
- [Online delta loading from the local session (RT Professional)](#online-delta-loading-from-the-local-session-rt-professional)

#### Compiling and loading with Multiuser Engineering (overview) (RT Professional)

##### Introduction

When using Multiuser Engineering for your projects, you should take into account the response when compiling the Runtime projects and the response when downloading them to HMI devices.

Compilation and loading to an HMI device is possible both in the server project view and the local session.

You can find more information on Multiuser Engineering in "Using Multiuser Engineering".

##### Basics

For HMI devices and RT Advanced, the following scenarios are possible in Multiuser Engineering:

- Compiling in the server project view
- Compiling in the local session
- Loading from the server project view
- Loading from the local session

> **Note**
>
> Complete loading from the server project view or from the local session does not differ from complete loading in a single-user project. With complete loading, the current Runtime project is loaded from the currently active view to an HMI device.

The following additional scenarios are possible for RT Professional:

- Online delta loading from the server project view
- Online delta loading from the local session

> **Note**
>
> Compiling and loading projects in a local session does not differ from compiling and loading in a single-user project, with the exception of online delta loading.
>
> All rules, e.g. actions which revoke and restrictions for online delta loading capability also apply to online delta loading in Multiuser Engineering.
>
> You can find additional information in [Use and limitations of online delta loading](#use-and-limitations-of-online-delta-loading-rt-professional).

In principle, you can execute all commands for compiling and loading in Multiuser Engineering projects:

- "Software (rebuild all)"
- "Compile &gt; Software (only changes)"
- "Software (all)"
- "Online delta loading" (RT Professional only)

##### The term "project"

The term "project" has two different meanings in the context of compilation and loading. "Project" is the WinCC project on the configuration PC. "Project" is also the Runtime project that you create by compiling the configuration data of an HMI device and download to the HMI device.

- WinCC project: contains the configuration data of one or more HMI devices
- Runtime project: contains the compiled configuration data of an HMI device

##### Rules

The following basic rules apply to compiling and downloading in Multiuser Engineering:

- The Runtime project which was compiled in a local session always remains local and is not uploaded to the multiuser server. It cannot be saved in the multiuser server project.
- Only the Runtime projects which were compiled in the server project view are saved in the multiuser server project.

> **Note**
>
> Observe the rules on online delta loading.
>
> You can find additional information in [Online delta transfer for Runtime Professional](#online-delta-transfer-for-runtime-professional-rt-professional).

You can find additional information on Multiuser Engineering on the Siemens YouTube channel: [Multiuser Engineering - one team working simultaneously on a project](https://www.youtube.com/watch?v=n4oTZ2Gzg6U).

---

**See also**

[Compiling in the server project view (RT Professional)](#compiling-in-the-server-project-view-rt-professional)
  
[Compiling in the local session (RT Professional)](#compiling-in-the-local-session-rt-professional)
  
[Rules on online delta loading (RT Professional)](#rules-on-online-delta-loading-rt-professional)
  
[Online delta transfer for Runtime Professional (RT Professional)](#online-delta-transfer-for-runtime-professional-rt-professional)
  
[Online delta loading from the server project view (RT Professional)](#online-delta-loading-from-the-server-project-view-rt-professional)
  
[Online delta loading from the local session (RT Professional)](#online-delta-loading-from-the-local-session-rt-professional)
  
[Use and limitations of online delta loading (RT Professional)](#use-and-limitations-of-online-delta-loading-rt-professional)

#### Compiling in the server project view (RT Professional)

##### Basics

Compiling and downloading in the server project view is no different from compiling and downloading in a single-user project.

During the compiling of a project in the server project view, the multiuser server project is blocked. Other users cannot make changes to this server project during this time. The Runtime project compiled in the server project view is stored along with the engineering project in the central multiuser server. Blocking the multiuser server project ensures that the configuration data and the Runtime project remain in sync.

> **Note**
>
> When you compile and save in the server project view, other users obtain the Runtime project you have updated along with the engineering project when they "refresh" their local session. Other users do not have to recompile the changes you have made after an update.

##### Example: **Compiling during check-in**

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

If there are no compilation errors, both projects - the modified engineering project (with the modified tags) and the compiled Runtime project - are saved in the central multiuser server project with the "Save changes" command.

If you skip compiling during the check-in, the project contains the changes that have been saved on the server.

The next user who creates a local session from the server project or updates an existing local session must compile your two changes in addition to his or her own changes.

> **Note**
>
> Working on a shared project through multiple local sessions increases the probability of error. It is therefore recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors.

---

**See also**

[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Compiling in the local session (RT Professional)](#compiling-in-the-local-session-rt-professional)

#### Compiling in the local session (RT Professional)

##### **Basics**

Compiling and downloading projects in the local session is no different from compiling and downloading in a single-user project.

Since the local session is a copy of the server project, the first compilation status of the local session is identical to that of the server project. If the server project contains contents that are not compiled or error messages occurred during the compiling, they are transferred to the local session.

> **Note**
>
> It is recommended to compile the project at check-in and eliminate any errors that are reported during compiling. In this way, you provide the next user with a project free of errors and avoid spreading errors.

##### **Updating in the** **local session**

If you update a project in the local session, the local session - including the compilation status - is completely replaced by the content of the server project. Only the changes marked for check-in are retained in the updated local session and generate additional compiling steps in the local session.

##### Example: Updating the local session

You make changes to a tag in a local session. All prior changes have been compiled in the associated server project.

You update the content of the local session by clicking the "Update" button. After the update, the local session obtains the compilation status of the server project. There are also compiling tasks for the acquisition of the modified tags.

---

**See also**

[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Compiling in the server project view (RT Professional)](#compiling-in-the-server-project-view-rt-professional)

#### Rules on online delta loading (RT Professional)

##### Overview

Online delta loading is only supported by WinCC RT Professional. All rules and restrictions for online delta loading also apply to online delta loading in Multiuser Engineering.

Observing these rules helps you to identify any potential errors in good time and prevent them. You can find additional information in [Use and limitations of online delta loading](#use-and-limitations-of-online-delta-loading-rt-professional).

The following figure shows an overview of online delta loading with Multiuser-Engineering:

![Overview](images/86837235467_DV_resource.Stream@PNG-en-US.png)

##### Rules for online delta loading from the server project view

- All rules and restrictions for online delta loading of the single-user projects also apply to online delta loading in Multiuser Engineering.
- Continuous online delta loading is only possible via the server project view without loading from local sessions.
- If you make a change in the server project view which revokes the online delta loading capability, the online delta loading capability in the multiuser server project is lost.

##### Rules for online delta loading from the local session

- All rules and restrictions for online delta loading of the single-user projects also apply to online delta loading in Multiuser Engineering.
- The local session must be created from a server project which features online delta loading capability.
- A local session itself has online delta loading capability.
- If you make a change in the local session which revokes the online delta loading capability, the local session loses the online delta loading capability.
- The online delta loading capability in the local session is lost during update.

---

**See also**

[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Online delta transfer for Runtime Professional (RT Professional)](#online-delta-transfer-for-runtime-professional-rt-professional)
  
[Use and limitations of online delta loading (RT Professional)](#use-and-limitations-of-online-delta-loading-rt-professional)

#### Online delta loading from the server project view (RT Professional)

##### **Basics**

To maintain online delta loading capability of the server project, all users may only make changes to the configuration which do not impair the online delta loading capability.

As long as all the users in the engineering project only make changes which do not revoke online delta loading capability, you can load the changed sections of configurations in WinCC Runtime Professional from different local sessions to the same HMI device via the server project view.

> **Note**
>
> With complete loading, the online delta loading capability of the HM device is lost.

Several users can make configuration changes in parallel in different local sessions. The steps "Compile &gt; Software (only changes)" or "Online delta loading" must, however, be executed in succession in the server project view, as exclusive access rights are required for this.

You can find more information on Multiuser Engineering in "Using Multiuser Engineering".

> **Note**
>
> Continuous online delta loading from different local sessions is only supported via the server project view.

When you load to an HMI device from the server project view and close the server project view with "Discard changes", the online delta loading capability is lost. During the next load process to this device, the command "Load all" is executed.

---

**See also**

[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Loading projects (RT Professional)](#loading-projects-rt-professional)
  
[Online delta transfer for Runtime Professional (RT Professional)](#online-delta-transfer-for-runtime-professional-rt-professional)

#### Online delta loading from the local session (RT Professional)

##### Basics

Online delta loading to an HMI device is not only possible from the server project view, but also from the local session.

Online delta loading from a local session is subject to the following restrictions:

- After online delta loading from a local session, online delta loading can only be executed for this HMI device from this local session in the future.
- After this, only complete loading of the HMI device is possible in the server project view.
- Each update of the local session makes complete loading of the HMI device necessary.
- The Runtime project of the local session is never transferred to the multiuser server project and cannot be stored there.

> **Note**
>
> Online delta loading to an HMI device from the local session is not suitable for all configuration scenarios. An exact inspection of the configuration scenario beforehand is therefore recommended.

> **Note**
>
> Continuous online delta loading is only supported via loading from the server project view.

During the first load process or after the creation or the update of the local session, the warning "Projects do not match" is displayed in the "Load preview" dialog box. Carry out complete loading.

![Basics](images/86425513739_DV_resource.Stream@PNG-en-US.png)

##### Preventing the loss of online delta loading capability in the server project

To maintain online delta loading capability of an HMI device in the server project, all users may only make changes to the configuration which do not impair the online delta loading capability.

If the online delta loading capability of an HMI device in the local session is lost due to a change, the online delta loading capability of this HMI device in the server project is only lost when you check in the change in question. Not all the errors reported in the local session lead to the loss of online delta loading capability in the server project on check-in of this change. If the check-in would result in the loss of online delta loading capability in the server project, automatic check-in is stopped. An error message will inform you of this. You can then decide whether you wish to continue or cancel check-in.

If you cancel check-in using "Discard changes", the online delta loading capability of the HMI device is retained. Your configuration changes are not applied in the server project.

You can find more information on the topic of "checking in objects in the server project" under "Working in the local session".

---

**See also**

[Compiling and loading with Multiuser Engineering (overview) (RT Professional)](#compiling-and-loading-with-multiuser-engineering-overview-rt-professional)
  
[Online delta transfer for Runtime Professional (RT Professional)](#online-delta-transfer-for-runtime-professional-rt-professional)

### Starting Runtime (RT Professional)

This section contains information on the following topics:

- [Starting Runtime on the configuration PC (RT Professional)](#starting-runtime-on-the-configuration-pc-rt-professional)
- [Starting Runtime Professional (RT Professional)](#starting-runtime-professional-rt-professional)
- [Starting Runtime via Windows command prompt (RT Professional)](#starting-runtime-via-windows-command-prompt-rt-professional)

#### Starting Runtime on the configuration PC (RT Professional)

##### Introduction

Once you have loaded your project locally you can start your project in Runtime on the configuration PC while you are performing configuration in WinCC. The following restrictions apply to online configuration:

- The project cannot be compiled in the background while Runtime is running on the configuration PC.
- The delta data of the project is compiled automatically when you load the project to an HMI device after having closed Runtime. You can also start compilation manually.
- The project settings defined in the "Runtime settings" of the HMI device are activated when the project is started in Runtime.
- If Runtime is running on the configuration PC, the changes are applied in the simulation after compilation. After loading, all changes are applied to the Runtime project.

  - Certain changes require a restart of Runtime for their activation.
  - Changes to the screen that is currently open become visible after a screen change.
  - With some changes, the option to compile configuration changes to the active Runtime is lost. If your changes lead to the loss of the delta load capability, you are notified accordingly during configuration.

> **Note**
>
> **Closing Runtime automatically**
>
> If automatic transfer is activated on the HMI device and a transfer is started on the configuration PC, the running project is automatically terminated.
>
> The HMI device then automatically switches to "Transfer" operating mode.
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> To block access to the transfer settings and thus avoid unauthorized changes, assign a password in the Control Panel.

##### Requirement

- A project is open on the configuration PC.
- Runtime is installed on the configuration PC.

##### Procedure

To start Runtime on the configuration PC and to apply changes to the configuration to the active Runtime, follow these steps:

1. Activate the HMI device in the project tree.
2. Select "Online &gt; Download to device".
3. When the "Load preview" dialog box opens, select to start Runtime after loading.

   ![Procedure](images/111987115787_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111987115787_DV_resource.Stream@PNG-en-US.png)
4. Click "Load".

Alternatively, use the "WinCC StartTool" to start the project.

##### Result

Runtime is started and the updated project displayed on the configuration PC.

---

**See also**

[Starting Runtime Professional (RT Professional)](#starting-runtime-professional-rt-professional)
  
[Use and limitations of online delta loading (RT Professional)](#use-and-limitations-of-online-delta-loading-rt-professional)
  
[Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)
  
[Starting Runtime via Windows command prompt (RT Professional)](#starting-runtime-via-windows-command-prompt-rt-professional)

#### Starting Runtime Professional (RT Professional)

##### Introduction

If WinCC Runtime is also installed on a configuration PC, you start Runtime during loading. To do this, activate the corresponding option in the "Load preview" dialog box.

If only WinCC Runtime is installed on an HMI device, load the project to the HMI device. To start WinCC Runtime on the HMI device use the "WinCC StartTool" or activate the subsequent start of WinCC Runtime during loading.

##### Requirements

"WinCC Runtime" is installed on the HMI device.

> **Note**
>
> A least 100 MB free memory must be available on the storage medium before the Runtime of a project can be started.

> **Note**
>
> **Closing Runtime automatically**
>
> If automatic transfer is activated on the HMI device and a transfer is started on the configuration PC, the running project is automatically terminated.
>
> The HMI device then automatically switches to "Transfer" operating mode.
>
> After the commissioning phase, disable the automatic transfer function to prevent the HMI device from switching inadvertently to transfer mode.
>
> Transfer mode can trigger unwanted responses in the plant.
>
> To block access to the transfer settings and thus avoid unauthorized changes, assign a password in the Control Panel.

##### Starting Runtime at an Engineering Station

1. Select the required project in the WinCC project tree.
2. Select "Online &gt; Download to device".
3. Activate the start of WinCC Runtime after loading.

   ![Starting Runtime at an Engineering Station](images/111987115787_DV_resource.Stream@PNG-en-US.png)

   ![Starting Runtime at an Engineering Station](images/111987115787_DV_resource.Stream@PNG-en-US.png)
4. Click "Load".

##### Result

The project is compiled and loaded. During loading, all Runtime services that you selected in the Runtime settings of the HMI devices are started.

---

**See also**

[Starting Runtime on the configuration PC (Panels, Comfort Panels, RT Advanced)](#starting-runtime-on-the-configuration-pc-panels-comfort-panels-rt-advanced)
  
[Activating and deactivating projects on the WinCC server (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#activating-and-deactivating-projects-on-the-wincc-server-rt-professional)
  
[Starting Runtime via Windows command prompt (RT Professional)](#starting-runtime-via-windows-command-prompt-rt-professional)

#### Starting Runtime via Windows command prompt (RT Professional)

##### Introduction

With the "CCStartStop.exe" tool, WinCC enables you to change the status of a project via a command line in the Windows command prompt:

- Open project
- Activate project in Runtime
- Deactivating a project

  When working with redundant systems, you can have the status of the redundant servers checked before deactivating them.
- Closing a project
- Output information about the project or export it to a log file
- ServiceMode: Configure ServiceMode users

##### Starting Runtime with CCStartStop.exe

1. Type the following text in the "Windows command prompt" window:

   `CCStartStop /a`

   The project is started in Runtime.

##### Stopping Runtime with CCStartStop.exe

1. Type the following text in the "Windows command prompt" window:

   `CCStartStop /d`

   Runtime stops.

##### Command prompt: CCStartStop.exe

You can start basic actions with the "CCStartStop.exe" tool:

| Parameter | Meaning |
| --- | --- |
| `/?` | List of parameters |
| `/o <`Project file`>` | Open project in WinCC Explorer.  Specify the full storage path.  Example:  - `CCStartStop /o D:\Siemens\WinCCProjects\Quick_Start.mcp` |
| `/a` | Activate open project in Runtime |
| `/d` | Deactivating Runtime  To disable Graphics Runtime only, use the "SIMATIC WinCC" icon in the tray area. |
| `/td` | Deactivate Runtime after checking redundancy status.  If, for example, the redundant partner has failed, the deactivation is canceled. |
| `/c` | Close open project.  The parameter is executed only if the project is deactivated. |
| `/i` | Show information about the opened project.  Alternatively, enter only "CCStartStop" without parameters. |
| `/out:<`File name`>` | Output of the project information as a log file.  Example of output to a "LogWinCC_01.txt" file in the "D:\Temp" folder:  - `CCStartStop /out:D:\Temp\LogWinCC_01.txt` |
| `/su` | Change configuration of the ServiceMode user in the project:  - Configure new ServiceMode user. - Accept changed Windows password of the current ServiceMode user in the project.   The "/su" parameter is only relevant for projects in WinCC ServiceMode.  For the configuration, use the supplementary parameters "/domain", "/user" and "/password".  Requirement:  - The ServiceMode is configured with a valid ServiceMode user. - The project is open, but not active.   Example:  - `CCStartStop /o D:\Siemens\WinCCProjects\Quick_Start.mcp /su /domain:plant011 /user:operator02 /password:MYpa$$w0rd`    The "Quick_Start" project is open.   The "plant011\operator02" user is accepted as ServiceMode user with the password "MYpa$$w0rd".   If the project is already open, you can omit the "/o" parameter and the project name. |
| `/domain:<`Domain`> *` | Domain of the ServiceMode user.  The local user is configured without specifying a domain. |
| `/user:<`User name`> *` | Name of the new ServiceMode user  The password of the currently configured ServiceMode user is changed without specifying a user name. |
| `/password:<`Password`> *` | Password of the ServiceMode user  The specified password must be the same as the user's current Windows password.  To change only the password of the configured ServiceMode user, omit the "/domain" and "/user" parameters.  Example:  - `CCStartStop /su  /password:NEWpa$$w0rd`    In the open project, the password of the logged-in user is changed to the new password "NEWpa$$w0rd". |
| *) Parameter only valid in combination with the "/su" parameter and only relevant for projects in WinCC ServiceMode. |  |

##### Example: Manage WinCC project with "CCStartStop"

To open, activate and close a project again, follow these steps:

1. In the "Windows system" program group, select the "Command prompt" entry.

   The DOS window opens.
2. Enter the following command lines:

   - Open project:

     `CCStartStop /o <`Project path`>\<`Project name`>.mcp`
   - Activate project:

     `CCStartStop /a`
   - Deactivate project:

     `CCStartStop /d`
   - Close project:

     `CCStartStop /c`
3. To close the window, type "exit" or click the "X" button.

---

**See also**

[Starting Runtime Professional (RT Professional)](#starting-runtime-professional-rt-professional)
  
[Starting Runtime on the configuration PC (RT Professional)](#starting-runtime-on-the-configuration-pc-rt-professional)

### Basics of operating in Runtime (RT Professional)

This section contains information on the following topics:

- [Overview of operating in Runtime (Professional) (RT Professional)](#overview-of-operating-in-runtime-professional-rt-professional)
- [Operation with the touch screen (RT Professional)](#operation-with-the-touch-screen-rt-professional)
- [Operation with keys (RT Professional)](#operation-with-keys-rt-professional)
- [Navigating in the display (BS) (RT Professional)](#navigating-in-the-display-bs-rt-professional)
- [Triggering an action (RT Professional)](#triggering-an-action-rt-professional)
- [Entering a value (RT Professional)](#entering-a-value-rt-professional)
- [Moving operator controls (RT Professional)](#moving-operator-controls-rt-professional)
- [Displaying infotext (Professional) (RT Professional)](#displaying-infotext-professional-rt-professional)
- [Changing Runtime language (RT Professional)](#changing-runtime-language-rt-professional)
- [Runtime data (RT Professional)](#runtime-data-rt-professional)

#### Overview of operating in Runtime (Professional) (RT Professional)

##### Operation options

The hardware configuration determines how you operate the HMI device:

- Touch screen

  The operating elements shown in the dialogs are touch-sensitive. Touch objects are basically operated in the same way as mechanical keys. You activate operating elements by touching them with your finger. To double-click them, touch an operating element twice in succession.
- HMI device keyboard

  The operating elements shown in the screens are selected and operated using the keys of the HMI device.
- External keyboard
- External mouse

##### Operation feedback from operating elements

The HMI device provides optical feedback as soon as it detects that an operating element has been selected. The operating element receives the focus and is selected. This selection is independent of any communication with the PLC. Therefore this selection does not indicate whether the relevant action is actually executed or not.

The configuration engineer can also configure the selection of an operating element so that it deviates from the standard.

##### Optical feedback from operating elements

The type of optical feedback depends on the operating element:

- Buttons

  The HMI device outputs different views of the "Pressed" and "Unpressed" states, provided the configuration engineer has configured a 3D effect:

  - "Pressed" state:

    ![Optical feedback from operating elements](images/43205569931_DV_resource.Stream@PNG-de-DE.png)
  - "Unpressed" state:

    ![Optical feedback from operating elements](images/43205577611_DV_resource.Stream@PNG-de-DE.png)

  The configuration engineer determines the appearance of a selected field, for example, line width and color for the focus.
- Invisible buttons

  By default, invisible buttons are not displayed as pressed when they are touched. No optical operation feedback is provided in this case.

  The configuration engineer may, however, configure invisible buttons so that their outline appears as lines when touched. This outline remains visible until you select another operating element.
- I/O fields

  When you select an I/O field, the content of the I/O field is displayed against a colored background. With touch operation, a screen keyboard is displayed for the entering of values.

#### Operation with the touch screen (RT Professional)

This section contains information on the following topics:

- [Overview of operation with the touch screen (RT Professional)](#overview-of-operation-with-the-touch-screen-rt-professional)
- [Screen keyboard](#screen-keyboard)
- [Using multi-touch functions (RT Professional)](#using-multi-touch-functions-rt-professional)

##### Overview of operation with the touch screen (RT Professional)

Use the touch screen to operate the HMI device of the project that is running on your HMI device.

###### Operating the touch screen

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to the touch screen**  Do not touch the touch screen with sharp or pointed objects.   Avoid tapping the touch screen with hard objects, and avoid constantly using motion control.   Both can significantly reduce the useful life or even cause the failure of the touch screen.  **Triggering unintended actions**  You can trigger unintended actions if you touch several operating elements at the same time. Always touch only one operating element on the screen.  Operating elements are touch-sensitive symbols on the screen of the HMI device. |  |

###### Special features of operation using the touch screen

Operation with the touch screen is characterized by the following special features:

- Enable

  To enable an operator control, touch the touch screen with your fingers or with a stylus. To generate a double-click, touch the operator control twice in rapid succession.
- Value input

  You enter numbers and letters on the touch screen with a screen keyboard.
- Careful operation

  If you touch multiple operator controls at the same time, you may trigger unintentional actions.

###### Value input using the screen keyboard

The screen keyboard is displayed as soon as you operate a screen object that requires an input. Depending on the HMI device and the configured operating element, the system displays different screen keyboards for entering numerical or alphanumerical values. The screen keyboard is hidden again when input is complete.

###### File browser (Windows 8 or higher)

You can only operate the file browser dialog with a mouse, keyboard or on-screen keyboard (without using the touch function) on a Windows 8 or higher PC with touch screen. Use the file browser dialog of the Windows operating system with the help of a script on a touch screen PC with Windows 8 or higher.

##### Screen keyboard

###### Layout

The following figure shows the principal structure of a screen keyboard on a Runtime Professional HMI device.

| Symbol | Meaning |
| --- | --- |
| ![Layout](images/71157164555_DV_resource.Stream@PNG-de-DE.png) |  |
| Numbers |  |
|  |  |
| ![Layout](images/71132131467_DV_resource.Stream@PNG-de-DE.png) |  |
| Letters |  |

##### Using multi-touch functions (RT Professional)

This section contains information on the following topics:

- [Multi-touch operation (RT Professional)](#multi-touch-operation-rt-professional)
- [Supported gestures (RT Professional)](#supported-gestures-rt-professional)
- [Two-hand operation of operator controls (RT Professional)](#two-hand-operation-of-operator-controls-rt-professional)

###### Multi-touch operation (RT Professional)

###### Introduction

RT Professional supports multi-touch operation under Windows 7, Windows 8 and Windows 10. You operate objects on the multi-touch screens by touching them with one or two fingers. Multi-touch operation is supported by TIA Portal as of V13. Versions V12 or older only support single-touch operation.

###### Requirement

The used monitor must support multi-touch functions.

###### Basics of multi-touch operation

The multi-touch capable monitor can be operated by tapping, dragging, opening and pinching and swiping and detects the type of contact exactly. Tapping is briefly touching the screen with one finger and activating a button in this way, for example. Dragging is pressing a finger on the screen and moving it in a constant direction, similar to the drag-and-drop with the mouse. Opening and pinching involves touching the screen with two fingers and widening or narrowing the fingers. Swiping is briefly touching the screen with one finger and moving your finger in one direction.

You can use multi-touch in screens to scroll, enlarge or reduce screen sections or switch between screens in a screen stack. You use horizontal dragging to move the content of the screen to the left or right. You use vertical dragging to scroll up or down in the view. While you scale, an indicator is displayed to show the scale factor.

###### Supported gestures (RT Professional)

###### Supported gestures

The following gestures are supported.

| Gesture |  | Function |
| --- | --- | --- |
| ![Supported gestures](images/71110986763_DV_resource.Stream@PNG-de-DE.png) | Tap | You can select a button, for example, by typing. |
| ![Supported gestures](images/71110995467_DV_resource.Stream@PNG-de-DE.png) | Drag | Use one finger to scroll horizontally and vertically, for example, in screens.   You scroll horizontally and vertically at the same time by dragging vertically in screens. |
| ![Supported gestures](images/71110978059_DV_resource.Stream@PNG-de-DE.png) | Scale | Pinch-to-zoom to enlarge or reduce the display of the screen.  Objects can be displayed or hidden when scaling based on the configured zoom factor. This means, for example, that an object is only shown if a sufficient zoom factor allows the required object to also be displayed. |
| ![Supported gestures](images/71388555915_DV_resource.Stream@PNG-de-DE.png) | Swipe | By swiping from the center to the right or to the left, you can navigate between the screens within a screen stack. |

> **Note**
>
> **Operating with three of more fingers**
>
> Do not use three or more fingers to operate the device. This can lead to incorrect operations.

> **Note**
>
> **Settings for dragging and scaling**
>
> To unlock the "Drag" and "Scale" functions, select the "Slider" check box and clear the "Extended zoom" check box under "Runtime Settings &gt; Screens &gt; Properties Window". Also select the "Extended zoom" check box under "Properties &gt; Properties &gt; Miscellaneous" in the Inspector window of each screen.

---

**See also**

[Hiding layers and objects in Runtime (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#hiding-layers-and-objects-in-runtime-rt-professional)

###### Two-hand operation of operator controls (RT Professional)

This section contains information on the following topics:

- [Two-hand operation of operator controls (RT Professional)](#two-hand-operation-of-operator-controls-rt-professional-1)
- [Locking and unlocking operator controls (RT Professional)](#locking-and-unlocking-operator-controls-rt-professional)
- [Configuring release button in screen or template (RT Professional)](#configuring-release-button-in-screen-or-template-rt-professional)

###### Two-hand operation of operator controls (RT Professional)

###### Introduction

WinCC supports two-hand operation of operator controls with RT Professional. It ensures safe operation of operator controls which are used to change critical system settings, for example, control tags with machine limits.

###### Locked and unlocked operator controls

You define specific operator controls as "locked operator controls" for two-hand operation of operator controls. Locked operator controls usually cannot be operated in runtime. The operator can only operate the locked operator controls if he presses a release button at the same time.

In runtime, locked operator controls can only be accessed with the tab sequence if a release button is pressed at the same time.

###### Locked operator controls and release buttons

You can configure all operator controls as locked.

You must configure at least one button in the screen as release button. This can be any unlocked button.

###### Display in runtime

The locked operator controls are displayed as dimmed in runtime. The locked operator controls are completely visible when they are unlocked by means of the release buttons.

###### Simulation of projects with multi-touch functions

WinCC supports the simulation of configured multi-touch functions. Requirement is that your monitor supports multi-touch operation.

###### Locking and unlocking operator controls (RT Professional)

You can lock and unlock operator controls in projects for multi-touch devices. Locked operator controls can only be operated in runtime if the operator presses a release button at the same time.

You can lock and unlock individual operator controls or several operator controls simultaneously.

###### Procedure

1. Configure operator controls of the type I/O field,button or slider.
2. Select the required operator control(s).
3. To lock the operator controls, disable the "Allow operator control" option under "Properties &gt; Properties &gt; Security".

   ![Procedure](images/88767936651_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88767936651_DV_resource.Stream@PNG-en-US.png)

   In Runtime, locked operator controls can only be operated by simultaneously pressing a release button that has been made dynamic with a corresponding system function.
4. To unlock the operator controls, enable the "Allow operator control" option under "Properties &gt; Properties &gt; Security".

###### Configuring release button in screen or template (RT Professional)

For the operator to operate locked operator controls on multi-touch devices, at least one release button must be configured in the same screen.

Configure a release button so that when you press the button it releases the operator controls and locks them when it is no longer pressed.

If several objects have to be unlocked in a screen with a release button, expand the function list of the release button with an additional entry for each object.

###### Requirement

- One or more buttons are created in a screen or a template.

###### Procedure

1. Select the button that you want to configure as the release button.
2. Click "Properties &gt; Events" in the Inspector window.
3. Select the "Press left mouse button" event.
4. Click on "Add function" in the table.
5. Select the "SetPropertyByConstant" system function.
6. Select the respective screen from the "Screen name" list.
7. Select the respective button from the "Screen object" list.
8. Select the "Allow operator control" property from the "Property name" list.
9. Enter "1" for the value.

   ![Procedure](images/71400713227_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/71400713227_DV_resource.Stream@PNG-en-US.png)
10. To have the control enable revoked when you let go of the release button, select the "Release left mouse button" event and enter "0" for the value.

    ![Procedure](images/71410667915_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/71410667915_DV_resource.Stream@PNG-en-US.png)

Locked operator controls can only be operated in runtime if the operator presses one of the configured release buttons at the same time.

#### Operation with keys (RT Professional)

This section contains information on the following topics:

- [Overview of operation with keys (RT Professional)](#overview-of-operation-with-keys-rt-professional)
- [Control keys and shortcuts (RT Professional)](#control-keys-and-shortcuts-rt-professional)
- [Function Keys (RT Professional)](#function-keys-rt-professional)
- [Direct keys (RT Professional)](#direct-keys-rt-professional)

##### Overview of operation with keys (RT Professional)

###### Introduction

Use the keys of the HMI device to operate the Control Panel / Start Center of your HMI device or the project that is running on your device. Depending on the device, control keys and function keys are available.

For more detailed information, refer to the operating instructions for your HMI device.

##### Control keys and shortcuts (RT Professional)

###### Introduction

The following tables list the control keys available to operate the project.

> **Note**
>
> The availability of control keys is determined by the HMI device used.

You trigger functions on keyboard HMI devices either with a key or a shortcut. With shortcuts, you keep the first key pressed. Then you press the second key.

###### Navigating in the display

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) |  | Tabulator | Selects the next operating element in the tab sequence |
| ![Navigating in the display](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Navigating in the display](images/43204835979_DV_resource.Stream@PNG-de-DE.png) | Tabulator | Selects the previous operating element in the tab sequence |
| ![Navigating in the display](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43204938379_DV_resource.Stream@PNG-de-DE.png)     ![Navigating in the display](images/43205122699_DV_resource.Stream@PNG-de-DE.png) |  | Cursor keys | Selects the next operating element to the left, to the right, above or below the current screen object  Navigating in the operating element |

###### Operation of operating elements

| Key or shortcut |  | Function | Description |
| --- | --- | --- | --- |
| ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) |  | ENTER key | - Controls buttons. - Applies and ends an entry - Opens a selection list - Toggles between character mode and standard mode within an input field   A single character is selected in character mode. In this mode, you can scroll within the character set using the cursor keys. |
| ![Operation of operating elements](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204930699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204923019_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43205122699_DV_resource.Stream@PNG-de-DE.png)     ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Positioning cursor | Positioning the cursor within an operating element, for example, in an I/O field |
| ![Operation of operating elements](images/43204907659_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the character to the left of the current cursor position |
| ![Operation of operating elements](images/43205030539_DV_resource.Stream@PNG-de-DE.png) |  | Delete characters | Deletes the next character to the right of the current cursor position |
| ![Operation of operating elements](images/43205007499_DV_resource.Stream@PNG-de-DE.png) |  | Cancel | - Deletes the input characters of a value and restores the original value - Closes the active dialog. |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) | Scroll to start | Scrolls to the start page of a list |
| ![Operation of operating elements](images/43205022859_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling back | Scrolls the list back by one page |
| ![Operation of operating elements](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) | Scroll to end | Scrolls to the end of a list. |
| ![Operation of operating elements](images/43204953739_DV_resource.Stream@PNG-de-DE.png) |  | Scrolling up | Scrolls the list up by one page |
| ![Operation of operating elements](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204938379_DV_resource.Stream@PNG-de-DE.png) | Open selection list | Opens a selection list |
| ![Operation of operating elements](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | ![Operation of operating elements](images/43204987019_DV_resource.Stream@PNG-de-DE.png) | Accept value | Accepts the value selected in the selection list without closing the list |

###### Enter shortcut

| Key | Function | Purpose |
| --- | --- | --- |
| ![Enter shortcut](images/43204874379_DV_resource.Stream@PNG-de-DE.png) | Toggle (numbers/letters) | Toggles the assignment from numbers to letters  - No LED is lit:   The number assignment is enabled. Pressing the key once switches to letter assignment. - The right or left LED is lit:   The left or right letter assignment is enabled.   Each time the key is pressed, the system toggles between the left letter assignment, the right letter assignment and the number assignment. |
| ![Enter shortcut](images/43204843659_DV_resource.Stream@PNG-de-DE.png) | Shift (upper/lower case) | Used in shortcuts, for example, for switching to uppercase letters |
| ![Enter shortcut](images/43205015179_DV_resource.Stream@PNG-de-DE.png) | Toggle to additional keyboard layout | Some of the keys contain a blue special character in their bottom left corner, for example, the percent sign "%". To input these characters, press the relevant key in combination with the special character key shown on the left. |
| ![Enter shortcut](images/43204915339_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example, for navigating trend views |
| ![Enter shortcut](images/43204866699_DV_resource.Stream@PNG-de-DE.png) | General control function | Used in shortcuts, for example for the "Watch table" screen object |

###### Acknowledge alarms

| Key | Function | Purpose |
| --- | --- | --- |
| ![Acknowledge alarms](images/43204851339_DV_resource.Stream@PNG-de-DE.png) | Acknowledge | Acknowledges the currently displayed alarm or all alarms of an alarm group  The LED is lit as long as an unacknowledged alarm is active. |

###### Displaying infotext

| Key | Function | Description |
| --- | --- | --- |
| ![Displaying infotext](images/43205130379_DV_resource.Stream@PNG-de-DE.png) | Displaying infotext | For the selected object, opens a window with the configured infotext, for example, for an alarm or an I/O field  The LED is lit if an infotext is available for the selected object. |

Key or shortcut

##### Function Keys (RT Professional)

The assignment of the function keys (F1, F2, F3, etc.) is defined during configuration.

###### Function keys with global function assignment

A globally assigned function key always triggers the same action on the HMI device or in the PLC regardless of the screen displayed. The activation of a screen or the closing an alarm window, for example, is such an action.

###### Function keys with local function assignment

A function key with local function assignment is screen-specific and is therefore only effective within the active screen.

The function of a locally assigned function key can vary from screen to screen.

Within a screen, a function key has only one function assignment, either a global or local one. The project planner specifies which assignment has priority.

###### Operating function keys

> **Note**
>
> **Operating function key after screen change**
>
> If you press a function key after a screen change, the associated function may be triggered in the new screen before the new screen is fully displayed.

##### Direct keys (RT Professional)

###### Introduction

Direct keys on the HMI device are used to set bits in the I/O area of a SIMATIC S7.

Direct keys enable operations with short reaction times that are, for example, a jog mode requirement.

> **Note**
>
> Direct keys are still active when the HMI device is in "offline" mode.

> **Note**
>
> If you operate a function key with direct key functionality in a running project, the direct key function is always executed, independent of the current screen contents.

> **Note**
>
> You only use direct keys when there is a connection via PROFIBUS DP or PROFINET IO.
>
> Direct keys result in additional basic load on the HMI device.

###### Direct keys

The following objects can be configured as a direct key:

- Buttons
- Function keys

Depending on the HMI device and the configuration, direct keys are screen-specifically configured.

Additional information on direct keys can be found in your plant documentation.

#### Navigating in the display (BS) (RT Professional)

##### Introduction

You navigate on the display of your HMI device as follows:

- between configured screen objects
- within screen objects

  When you select a complex screen object, the cursor focus switches to the screen object and follows the tab sequence there.
- in tables of screen objects

##### Procedure

- To navigate in the specified tab sequence, press the &lt;TAB&gt; key.
- To navigate freely between the operator controls, press the cursor keys.

Depending on the configuration of your HMI device, you can also use function keys or shortcuts for navigation.

When you operate your HMI device with the touch screen or with the mouse, you implicitly navigate by triggering a desired action. For this purpose, touch or click the operator control.

##### Result

The operator controls receive the cursor focus according to the selected sequence. You can trigger an action on the selected operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Triggering an action (RT Professional)

##### Introduction

Triggering an action at an operator control can mean the following:

- A command is executed.

  Example: Click a button to trigger a script or to execute a predefined function.
- An object is enabled.

  Example: To enter a value, select a table cell with the &lt;Enter&gt; key.

##### Requirement

- You have navigated to the operator control on which you want to trigger the action.
- The operator control has the cursor focus.

##### Procedure

- Press &lt;Enter&gt;.

  Or
- Touch the operator control on the touch screen once or twice in rapid succession.

  Or
- Click or double-click the operator control with the mouse.

##### Result

The following results are possible:

- The requested command is executed.
- The screen keyboard is opened and/or the cursor blinks in the input area of the operator control.
- The element is selected and can be moved.

For more detailed information, refer to the operating instructions for your HMI device.

#### Entering a value (RT Professional)

##### Introduction

Depending on the input format, you enter numerical or alphanumerical values in an input field.

You enter these values depending on the existing hardware using the screen keyboard, the control keys of the HMI device or an external keyboard.

##### Requirement

- The object is an input field or table field.
- The operator control is enabled.

##### Entering a value

1. Enter the desired value.
2. To confirm the value and exit the field, press the &lt;Enter&gt; key.
3. To discard the value and exit the field, press the &lt;Esc&gt; key.

##### Result

A value is entered or discarded. You navigate as needed to the next operator control.

For more detailed information, refer to the operating instructions for your HMI device.

#### Moving operator controls (RT Professional)

##### Introduction

In Runtime, you can move the movable operator controls of a screen object with the mouse or using the touch screen, for example, a slider or a scroll bar. Operation with the keyboard is described below.

##### Requirement

- A movable operator control is selected.

##### Procedure

- To move the operator control, proceed as follows depending on the operating element:

  - Standard for touch screen: Press the cursor keys.
  - Standard for keyboard devices: Press &lt;SHIFT&gt; and the cursor keys.
  - Switches: Press &lt;ENTER&gt;
  - Slider: Press &lt;PgUp&gt; or &lt;PgDn&gt;

1. To finish the movement, navigate to another screen object or operator control.

##### Slider procedure

1. To move the operator control, press the cursor keys.
2. To finish the movement, navigate to another screen object or operator control.

##### Result

The position of the movable operator control and the display in the screen object have changed.

For more detailed information, refer to the operating instructions for your HMI device.

#### Displaying infotext (Professional) (RT Professional)

##### Application

The configuration engineer uses tooltips to provide additional information and operating instructions. The configuration engineer can configure tooltips for screens and operating elements.

The tooltip of an I/O field may, for example, contain information about the value to be entered.

![Application](images/43407689355_DV_resource.Stream@PNG-en-US.png)

##### Procedure

Depending on your configuration, tooltips can be called via a configured operating element.

Additional information on this topic may be available in your plant documentation.

#### Changing Runtime language (RT Professional)

##### Introduction

The HMI device supports multilingual projects. A corresponding operating element which lets you change the language setting on the HMI device in Runtime has been configured.

The project always starts with the language set in the previous session.

##### Requirement

- The required language for the project is available on the HMI device.
- The language switching function is linked to an operating element, for example, to a button.

##### Selecting a language

You can change project languages at any time. Language-specific objects are immediately displayed on the screen in the new language when you switch languages.

You can switch the language in Runtime in one of the following ways:

- Use a configured operating element to switch from one language to the next in a list.
- Use a configured operating element to directly set the required language.

#### Runtime data (RT Professional)

##### Export data

To export data to a CSV file in Runtime, follow these steps:

1. Click "Export data" button in the toolbar of the display and operating object.  
   A dialog opens, depending on the configuration.
2. If you have the appropriate permissions, select the file and the directory for the export.
3. Start the export.

**Note**

**File name**

Even if you specify a file name extension other than "*.csv" for the file name, the runtime data are exported to a CSV file.

> **Note**
>
> **Export dialog**
>
> If no dialog is displayed, the data export to the predefined file begins automatically.

### Certificate creation with WinCC Certificate Manager (RT Professional)

This section contains information on the following topics:

- [Introduction (RT Professional)](#introduction-rt-professional)
- [Making certificates available (RT Professional)](#making-certificates-available-rt-professional)
- [Installing a root certificate manually (RT Professional)](#installing-a-root-certificate-manually-rt-professional)
- [Structure of the user interface (RT Professional)](#structure-of-the-user-interface-rt-professional)

#### Introduction  (RT Professional)

WinCC Runtime Professional supports the use of CA-based HMI certificates (CA = Certificate Authority). You provide these certificates with the WinCC Certificate Manager application.

> **Note**
>
> **No external certificate authority**
>
> Issuance, distribution and installation of these certificates requires the use of the Certificate Manager.
>
> The use of an external certificate authority or an intermediate certificate authority is not supported.

##### Functionality of WinCC Certificate Manager

- Central creation and management of certificates in the network
- Creation of a certificate authority with:

  - Private key
  - Public key (root certificate)
  - CRL file (CRL = Certificate Revocation List)
- Issuance of the application certificates of the HMI devices
- Renewing existing certificates
- Encrypted export of the application certificates as well as the root certificate for manual distribution to HMI devices
- Encrypted import and installation of the certificates on the HMI devices
- Encrypted export and import of the root certificate, CRL file, and private key, as well as all device certificates for data backup and restore.
- Export of the root certificate and its CRL file for distribution to external communication partners of the HMI device
- Export of an updated CRL file for distribution to the HMI devices and their external communication partners

##### Available application certificates

With WinCC Certificate Manager you can create the following CA-based application certificates for WinCC Professional HMI devices:

- WebUX | WebNavigator certificate
- OPC UA server certificate
- OPC UA client certificate
- OPC UA tag import certificate

---

**See also**

[Making certificates available (RT Professional)](#making-certificates-available-rt-professional)
  
[Structure of the user interface (RT Professional)](#structure-of-the-user-interface-rt-professional)

#### Making certificates available (RT Professional)

##### Procedure

The procedure for providing the certificates as well as the operation of the Certificate Manager interface is largely the same for WinCC Professional and WinCC Unified. Proceed as described in the WinCC Unified user help: Visualize processes (RT Unified) &gt; Runtime and simulation &gt; Certificates in WinCC Unified Runtime.

You can find more information about WinCC Unified Certificate Manager under the contribution ID [109813308](https://support.industry.siemens.com/cs/document/109813308/simatic-hmi-wincc-unified-engineering-v18?dti=0&lc=en-WW) in the Siemens Industry Online Support Portal in the help "SIMATIC HMI WinCC Unified Engineering V19" under "Runtime and Simulation &gt; Certificates in WinCC Unified Runtime" under the keyword "Use CA-based certificates".

##### Restrictions and special features

Deviating from the procedures and facts described in the user help for WinCC Unified, the following applies to WinCC Professional:

**Generation of certificates**

You can only generate the application certificates listed in section [Introduction](#introduction-rt-professional) .

You cannot generate general certificates.

**Device binding of the certificates**

When adding a device to the certificate authority, you specify what information is used to bind its certificates to the device.

In the "New device" dialog, you have the option of entering multiple IP addresses in the "IP" field. Use ";" as separator.

> **Note**
>
> Enter the IP address of the device (own IP) as the first IP address.

The IP addresses are added to the Subject Alternative Name of the certificate.

Example: An HMI device is an OPC UA server and has a NAT router. The OPC UA clients communicate with the server via the NAT router. Enter the private IP address of the OPC UA Server HMI device (own IP) and the public IP address in Certificate Manager.

**Distribution and installation of the application certificates**

To distribute the certificate configuration of the certification authority to the HMI devices and to install the certificate configuration of an HMI device on the device, follows the steps described in the WinCC Unified user help under the keyword "Exporting certificates of a Unified PC" and "Importing and installing certificates of a Unified PC".

**Binding of the WebUX | WebNavigator certificate to the Runtime web page**

If the Runtime Server web page has already been set up and you install the WebUX | WebNavigator certificate on the HMI device with Certificate Manager, the installation automatically binds the certificate to the Runtime web page.

If the website has not been set up yet, the binding cannot be performed successfully. Certificate Manager logs this via an entry in the "Output" area.

**Installation of the root certificate on the WebUX/WebNavigator clients**

To display Runtime in a WebUX/WebNavigator client, the root certificate of the WebUX/WebNavigator application certificate must be installed as trustworthy on the client. It is not necessary to install the root certificate manually in the following cases:

| Runtime access | Display via | Requirement |
| --- | --- | --- |
| Local | WinCCViewerRT   or   Internet Explorer | The WebNavigator certificate has been installed on the HMI device with Certificate Manager. |
| Chrome or Edge | The WebUX certificate has been installed on the HMI device with Certificate Manager. |  |
| Remote | WinCCViewerRT   or   Internet Explorer | The WebNavigator client device is also an HMI device. It has the same certificate authority as the HMI device, whose Runtime it displays in WinCCViewerRT or Internet Explorer.   The server HMI device has a WebNavigator certificate.  On both HMI devices the certificate configuration of the respective device has been installed with Certificate Manager. |
| Chrome or Edge | The device of the WebUX client is also an HMI device. It has the same certificate authority as the HMI device, whose Runtime it displays in Chrome or Edge.   The server HMI device has a WebUX certificate.  On both HMI devices the certificate configuration of the respective device has been installed with Certificate Manager. |  |

In other cases, install the root certificate manually on the WebNavigator clients and WebUX clients. Follow the steps described in section [Installing a root certificate manually](#installing-a-root-certificate-manually-rt-professional).

#### Installing a root certificate manually (RT Professional)

This section describes how to install the root certificate in order to display Runtime Professional in a WebUX/WebNavigator client.

##### Requirements

- On the certificate authority device:

  - A certificate authority has been created with WinCC Certificate Manager.
  - The Runtime Server HMI device has been added to the certificate authority and a WebUX | WebNavigator certificate has been added to the HMI device.
  - The certificate configuration of the HMI device has been exported.
- On the HMI device:

  The certificate configuration of the HMI device has been installed with WinCC Certificate Manager.
- On the WebUX/WebNavigator client devices:

  - To display Runtime in a browser, the desired browser must be installed on the WebUX client device.
  - To display Runtime in Internet Explorer, the WebNavigator client must also be installed on the WebUX client device.
  - To display Runtime with WinCCViewerRT, the WebNavigator client must be installed on the WebNavigator client device.

##### Procedure

1. Export the root certificate on the certificate authority device using Certificate Manager. Follow the steps described in the WinCC Unified Certificate Manager user help.
2. Transfer the exported root certificate file to a storage location that the WebUX/WebNavigator client device can access, such as a network folder or external storage medium. Follow the steps described in the WinCC Unified Certificate Manager user help.

   Your further procedure depends on which client you are using.
3. Edge and Chrome as the WebUX client:

   - Double-click the root certificate file on the WebUX client device.

     ​The root certificate is opened with the Windows standard form.
   - Select "Install Certificate".
   - In the certificate import wizard, select "Local Machine" as the storage location, "Trusted Root Certification Authority" as the certificate store.
   - Start the import.
4. Browser with its own certificate store as a WebUX client:

   Manually install the root certificate on the WebUX client device in the certificate store of the browser. Follow the steps described in the user help of the browser.

   For Firefox, for example, follow these steps:

   - In Firefox, click "Display certificates" under "Settings &gt; Privacy &amp; Security" under "Certificates".
   - In the "Certificate Management" window, select the "Certification authorities" tab.
   - Click "Import" and select the root certificate file.
   - ​In the window that opens, select the option "This certificate can identify websites" and confirm your selection.
5. Internet Explorer or WinCCViewerRT as WebNavigator client:

   On the WebNavigator client device, manually copy the root certificate file in the Windows system certificate store to the trusted certificate authorities folder.

##### Result

The next time the client tries to connect the WebUX/WebNavigator client with Runtime, the client trusts the root certificate and thus also the WebUX certificate or the WebNavigator certificate from Runtime.

#### Structure of the user interface (RT Professional)

##### Overview

The interface of WinCC Unified Certificate Manager has the following structure:

![Overview](images/163462320139_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Menu bar |
| ② | Toolbar |
| ③ | Work area with the "CA configuration" and "Installed certificates" tabs |
| ④ | "Details" area (fixed)  The "Details" area shows you detailed information about the certificate selected in the work area. |
| ⑤ | Information bar |
| ⑥ | "Output" area (hidden)  The "Output" area logs operator control actions. |

You can customize the display of the interface to suit your needs. Follow the steps described in the WinCC Unified Certificate Manager user help.

##### Menu bar

| Menu | Description |
| --- | --- |
| "File &gt; Exit" | Closes Certificate Manager. |
| "View" | Configure which Certificate Manager interface elements you see.  You can open or close the following interface elements:  - "Output" area - "Details" area - "CA configuration" tab - "Installed certificates" tab |
| "Help" | "About Certificate Manager"  Opens a dialog with information about the installed software version. |

##### Toolbar

| Button |  |
| --- | --- |
| ![Toolbar](images/151127983115_DV_resource.Stream@PNG-de-DE.png) | To change the user interface language |

## Jumping to the configuration (RT Advanced)

This section contains information on the following topics:

- [Jumping to the configuration (RT Advanced)](#jumping-to-the-configuration-rt-advanced-1)
- [Read mode in the TIA Portal (RT Advanced)](#read-mode-in-the-tia-portal-rt-advanced)

### Jumping to the configuration (RT Advanced)

#### Introduction

With WinCC Runtime Advanced, you have the option of defining a context-related switch from HMI to the configuration in the TIA Portal Engineering System. An operator can use this to jump to a specific project or a block in the engineering system from runtime or to check or modify the data. In addition, the operator can open or edit other objects of the opened project in the corresponding editors of the TIA Portal. Changing to the configuration enable fast and simple diagnostics of faults.

Depending on requirements, you can configure read/write access or read-only access in read mode.

#### Configuring jump to the TIA Portal

You configure the system function ShowBlockinTIAPortal for the jump from an alarm view or a GRAPH overview.

You switch to the project in the TIA Portal using the system function which you configure either at a button for the alarm view or at a GRAPH overview.

#### System function

You configure a change to an event in your program that triggered a hardware interrupt using the system function ShowBlockInTIAPortalFromAlarm. This provides you with the possibility to respond appropriately to this event and check the program for faults, such as a missing contact in the interlock.

You configure this system function at a screen object, for example, a button or a button of the toolbar in an alarm view. When you click the button, the necessary context is stored by the system. The corresponding position is automatically displayed in the program code after the switch to the engineering system.

For a description of the system function, refer to ["System functions for Runtime Advanced &gt; ShowBlockInTIAPortal"](System%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#showblockintiaportal-rt-advanced)

#### Jumping to a protected project

You enable project protection for your entire project and configure roles and users for access. When a user switches from runtime to a protected project, access is granted on the basis of function rights that you have defined for the user in question. For example, the function right "Open the project in read-only" set in project protection disables the read and write access that you have configured in WinCC.

Enter the user name and the password in a logon dialog when you open a protected project.

### Read mode in the TIA Portal (RT Advanced)

#### Introduction

With WinCC Runtime Advanced, you configure a context-related switch from HMI to the TIA Portal. You have the option here of configuring the jump with two different access types

- Read and write access

  After the jump to the TIA Portal, the operator can edit all project data in the engineering system and has read and write access to the hardware.
- Read-only access

  After the jump to the TIA Portal, the operator has only restricted access to the project data. The operator may not change the data in the engineering system and has only online read access to the hardware.

  Read-only access is implemented using read mode. It is not possible to change the project data in read mode.

#### Read mode

In read mode, the operator can only perform those configuration and diagnostic tasks that require no change to the project and online data. Online read access is also possible in read mode for the additional criteria analysis in the case of process error.

In read mode, the operator can use the navigation functions of the TIA Portal for the diagnostics of faults and analysis of the program.

- Project tree in the open project.

  The operator can access all available objects in the project through the project tree and can open these as read-only in the editors that support read mode. Editors that do not support read mode are not opened.
- Functions "Go to", read/write access, definition and device.

  The go-to functions help the operator to analyze the process states and data.
- Editors "Cross references", "Cross-reference information" and "Program information".

  The cross-reference functions provide the operator with an overview of the use of objects within the project.

#### Actions in read mode

In read mode, the operator can perform the following actions in the engineering system:

- Switch between the portal view and the project view.
- Open another project in TIA Portal using main menu command or using toolbar button.
- Access any connected device.
- Exit TIA Portal engineering system using main menu command.

#### Editors in read mode

The following TIA Portal editors can be opened in read mode:

- Program editor for displaying

  - Program blocks in the FBD, LAD, GRAPH, STL, SCL programming languages
  - Data blocks and UDTs
  - ProDiag function blocks
- Tag table
- Program information
- Cross-reference list
- Cross-reference information
- Devices &amp; networks
- HMI editors
- Safety Administration Editor
- Search in project

#### Restrictions in read mode

In read mode, the operator cannot perform the following actions in the TIA Portal:

- Upload project, download project, compile project
- Start simulation
- Create new objects
- Edit project
- Modify tags in the program status
- Display watch table and force table
- Open "Online &amp; diagnostics" editor
- Open editors of technology objects
- Open editors of local modules

## Jumping to the configuration (RT Professional)

This section contains information on the following topics:

- [Jumping to the configuration (RT Professional)](#jumping-to-the-configuration-rt-professional-1)
- [Read mode in the TIA Portal (RT Professional)](#read-mode-in-the-tia-portal-rt-professional)
- [Configuring read mode (RT Professional)](#configuring-read-mode-rt-professional)
- [Example: Configuring read mode using the API function (RT Professional)](#example-configuring-read-mode-using-the-api-function-rt-professional)

### Jumping to the configuration (RT Professional)

#### Introduction

With WinCC Professional, you have the option of defining a context-related switch from HMI to the configuration in the TIA Portal Engineering System. An operator can use this to jump to a specific project or a block in the engineering system from Runtime or to check or modify the data. In addition, the operator can open or edit other objects of the opened project in the corresponding editors of the TIA Portal. Changing to the configuration enable fast and simple diagnostics of faults.

Depending on requirements, you can configure read/write access or read-only access in read mode.

#### Configuring jump to the TIA Portal

Depending on the application, two options are available for the change to the project in the TIA Portal:

- Change using the four Runtime API functions

  You configure a screen object that executes one of four available API functions in a C script.
- Change using the system function

  You configure a system function which enables the operator to switch to the program position that triggered the hardware interrupt after this interrupt has occurred.

#### Runtime API functions

You can use the API function to switch from a screen in WinCC Runtime directly to the program code. A check is first made at the jump to determine whether the TIA Portal is already open. If this is not the case, the TIA Portal is started automatically. The corresponding editor opens in the TIA Portal and a search is performed for the point of use, assignment, call or step.

Use one of the four API functions to open a project in the TIA Portal:

- OpenTIAPortalProject opens the project in the TIA Portal.
- OpenTIAPortalIECPLByCall is used for the LAD and FBD languages and shows the preceding logic of a network input of a standard block.
- OpenTIAPortalIECPLByAssignment is used for the LAD and FBD languages and shows the assignment to an operand and its preceding logic.
- OpenTIAPortalS7GraphByBlock is used for the GRAPH language and shows a step in a GRAPH sequencer.

For a description of the API functions, refer to ["Interfaces &gt; Runtime API &gt; Functions for displaying the PLC code"](Runtime%20API%20%28RT%20Professional%29.md#functions-for-displaying-the-plc-code-rt-professional)

#### System function

You configure a change to an event in your program that triggered a hardware interrupt using the system function ShowBlockInTiaPortalFromAlarm. This provides you with the possibility to respond appropriately to this event and check the program for faults, such as a missing contact in the interlock.

You configure this system function at a screen object, for example, a button or a button of the toolbar in an alarm view. When you click the button, the necessary context is stored by the system. The corresponding position is automatically displayed in the program code after the switch to the engineering system.

For a description of the system function, refer to ["System functions for Runtime Professional &gt; ShowBlockInTiaPortalFromAlarm"](System%20functions%20%28RT%20Professional%29.md#showblockintiaportalfromalarm-rt-professional)

#### Accessing a protected project

You enable project protection for your entire project and configure roles and users for access. When a user switches from Runtime to a protected project, access is granted on the basis of function rights that you have defined for the user in question. For example, the function right "Open the project in read-only" set in project protection disables the read and write access that you have configured in WinCC.

Enter the user name and the password in a logon dialog when you open a protected project.

### Read mode in the TIA Portal (RT Professional)

#### Introduction

With WinCC Professional, you configure a context-related switch from HMI to the TIA Portal. You have the option here of configuring the jump with two different access types

- Read and write access

  After the jump to the TIA Portal, the operator can edit all project data in the engineering system and has read and write access to the hardware.
- Read-only access

  After the jump to the TIA Portal, the operator has only restricted access to the project data. The operator may not change the data in the engineering system and has only online read access to the hardware.

  Read-only access is implemented using read mode. It is not possible to change the project data in read mode.

#### Read mode

In read mode, the operator can only perform those configuration and diagnostic tasks that require no change to the project and online data. Online read access is also possible in read mode for the additional criteria analysis in the case of process error.

In read mode, the operator can use the navigation functions of the TIA Portal for the diagnostics of faults and analysis of the program.

- Project tree in the open project.

  The operator can access all available objects in the project through the project tree and can open these as read-only in the editors that support read mode. Editors that do not support read mode are not opened.
- Functions "Go to", read/write access, definition and device.

  The go-to functions help the operator to analyze the process states and data.
- Editors "Cross references", "Cross-reference information" and "Program information".

  The cross-reference functions provide the operator with an overview of the use of objects within the project.

#### Actions in read mode

In read mode, the operator can perform the following actions in the engineering system:

- Switch between the portal view and the project view.
- Open another project in TIA Portal using main menu command or using toolbar button.
- Access any connected device.
- Exit TIA Portal engineering system using main menu command.

#### Editors in read mode

The following TIA Portal editors can be opened in read mode:

- Program editor for displaying

  - Program blocks in the FBD, LAD, GRAPH, STL, SCL programming languages
  - Data blocks and UDTs
  - ProDiag function blocks
- Tag table
- Program information
- Cross-reference list
- Cross-reference information
- Devices &amp; networks
- HMI editors
- Safety Administration Editor
- Search in project

#### Restrictions in read mode

In read mode, the operator cannot perform the following actions in the TIA Portal:

- Upload project, download project, compile project
- Start simulation
- Create new objects
- Edit project
- Modify tags in the program status
- Display watch table and force table
- Open "Online &amp; diagnostics" editor
- Open editors of technology objects
- Open editors of local modules

### Configuring read mode (RT Professional)

#### Introduction

In WinCC Professional, you have the option of configuring a context-sensitive switch to the TIA Portal in read mode. Read mode does not permit the operator to make any changes to project data.

#### Configuring read mode via a Runtime API function

If you implement the change to the TIA Portal using the API functions in C scripts, configure the use of read mode as a parameter of the API function. Set the read-only access or the read/write protection for the operators using a bit in the bit field dwFlags. Depending on the bit value, the TIA Portal is opened in read mode (TRUE) or not in read mode (FALSE).

For a description of the API functions refer to ["Interfaces &gt; Runtime API &gt; Functions for displaying the PLC code"](Runtime%20API%20%28RT%20Professional%29.md#functions-for-displaying-the-plc-code-rt-professional).

#### Configuring read mode via the system function

If you configure the jump to the TIA Portal using the system function ShowBlockInTiaPortalFromAlarm, set the parameter Read mode:

- TRUE (default): TIA Portal is opened in read mode, the user cannot make any changes to project data.
- FALSE: TIA Portal is opened with read and right authorization.

For a description of the system function refer to ["System functions for Runtime Professional &gt; ShowBlockInTiaPortalFromAlarm".](System%20functions%20%28RT%20Professional%29.md#showblockintiaportalfromalarm-rt-professional)

---

**See also**

[Functions for displaying the PLC code (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#functions-for-displaying-the-plc-code-rt-professional)
  
[ShowBlockInTiaPortalFromAlarm (RT Professional)](System%20functions%20%28RT%20Professional%29.md#showblockintiaportalfromalarm-rt-professional)

### Example: Configuring read mode using the API function (RT Professional)

#### Introduction

The example below shows the program code for the call of the change to the TIA Portal. Activation of the read mode depends on the access authorization of the operator who logged on.

#### Requirements

- The "Supervisors" group is created in the user administration
- The "Supervisors" group is assigned the authorization "Go to TIA Portal" with the number 4

#### Example

`#pragma code("kopapi.dll")`
  
`#include "kopapi.h"`
  
`#pragma code()`
  
`#pragma code("UseAdmin.dll")`
  
`#include "pwrt_api.h"` 
  
`#pragma code()`

`BOOL result;` 
  
`CMN_ERROR error;`

`const DWORD permLevelTiaP = 4;`

`DWORD dwFlags = KOPAPI_FLAG_TIAPORTAL_OPEN_BRINGINFRONT |`

`KOPAPI_FLAG_TIAPORTAL_OPEN_READONLY;`
  
`char* plc = "PLC_1";` 
  
`char* contBlock = "OPC1_DB";` 
  
`char* operand = "#s1";`

`if(PWRTCheckPermission(permLevelTiaP, 1))` 
  
`{`

`dwFlags &= ~KOPAPI_FLAG_TIAPORTAL_OPEN_READONLY;` 
  
`}`

`result = OpenTIAPortalIECPLByAssignment(dwFlags,` 
  
 `GetTagChar("TiaPortalProjectPath"), plc, contBlock, operand, 444 "TIAPErrorTag", &error);`

#### Result

Checks whether the logged on user has the operator authorization.

An operator who is assigned to the "Supervisors" group has the authorization to change to the TIA Portal. A user who is not assigned to this group cannot change to the TIA Portal.

## Servicing the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Overview of HMI device maintenance tasks (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-tasks-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Maintenance overview of the HMI device (RT Adv, RT Prof) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#maintenance-overview-of-the-hmi-device-rt-adv-rt-prof-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Backup of HMI data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backup-of-hmi-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backing-up-and-restoring-data-of-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating the operating system of the HMI device from a data carrier (Panels, Comfort Panels)](#updating-the-operating-system-of-the-hmi-device-from-a-data-carrier-panels-comfort-panels)
- [Transferring license keys (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#transferring-license-keys-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing licenses (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-licenses-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Installing and uninstalling an option (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#installing-and-uninstalling-an-option-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Loading Asian fonts to the HMI device (Panels, Comfort Panels, RT Advanced)](#loading-asian-fonts-to-the-hmi-device-panels-comfort-panels-rt-advanced)

### Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Structure

The following figure shows the software components of an HMI device and their relation to the engineering system.

![Structure](images/9778628747_DV_resource.Stream@PNG-en-US.png)

#### Runtime data

The Runtime data is generated during operation of the plant and stored on the HMI device. This data includes, for example, recipes and data for the user administration. This data is overwritten during loading. If required, save this data before loading a Runtime project.

#### Runtime project

The Runtime project contains the compiled configuration data for an HMI device. You download the Runtime project from WinCC to the HMI device.

#### Runtime software and operating system

Together, the Runtime software and operating system of an HMI device form the image. Various images are available for the HMI device. All images of an HMI device are available in WinCC. Depending on the configuration, download the appropriate image along with the Runtime project to the HMI device as required.

#### Firmware and hardware

The HMI device is delivered with preconfigured firmware and hardware.

### Overview of HMI device maintenance tasks (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Structure

The following figure shows the software components of an HMI device and their relation to the engineering system.

![Structure](images/40236159115_DV_resource.Stream@PNG-en-US.png)

#### Runtime data

The Runtime data is generated during operation of the plant and stored on the HMI device. This data includes, for example, recipes and data for the user administration. This data is overwritten during loading. If required, save this data before loading a Runtime project.

#### Runtime project and Runtime software

The Runtime project contains the compiled configuration data for an HMI device. Download the Runtime project along with the Runtime software from WinCC to the HMI device.

#### Operating system

The HMI operating system is referred to as image. Various images are available for the HMI device. All images of an HMI device are available in WinCC. Depending on the configuration, download the appropriate image along with the Runtime project to the HMI device as required.

#### Firmware and hardware

The HMI device is delivered with preconfigured firmware and hardware.

### Maintenance overview of the HMI device (RT Adv, RT Prof) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Structure

The following figure shows the software components of an HMI device and their relation to the engineering system.

![Structure](images/40235878667_DV_resource.Stream@PNG-en-US.png)

#### Runtime data

The Runtime data is generated during operation of the plant and stored on the HMI device. This data includes, for example, recipes and data for the user administration. This data is overwritten during loading. If required, save this data before loading a Runtime project.

#### Runtime project

The Runtime project contains the compiled configuration data for an HMI device. You download the Runtime project from WinCC to the HMI device.

#### Operating system and runtime software

The HMI device operating system and runtime software are installed on the HMI device independently of WinCC. This software is maintained in the same way as with every other PC.

#### Firmware and hardware

The HMI device is delivered with preconfigured firmware and hardware.

### ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The "ProSave" service tool is installed by default when WinCC is installed. The ProSave functions are accessed in WinCC with the menu "Online &gt; HMI Device maintenance".

#### Functional scope

ProSave provides all of the functions you need to manage data on the HMI device:

- Data backup and restoration of backed-up data
- Operating system update for HMI devices with Windows CE or below
- Transferring License Keys
- Installing and uninstalling drivers and options as well as information on installed options and options that can be installed on an HMI device
- Communication settings (transferred from WinCC)

---

**See also**

[Backup of HMI data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backup-of-hmi-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backing-up-and-restoring-data-of-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Updating the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Transferring license keys (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#transferring-license-keys-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing licenses (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-licenses-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Installing and uninstalling an option (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#installing-and-uninstalling-an-option-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of compiling and loading projects (RT Professional)](#overview-of-compiling-and-loading-projects-rt-professional)
  
[Overview of compiling and loading projects (Panels, Comfort Panels, RT Advanced)](#overview-of-compiling-and-loading-projects-panels-comfort-panels-rt-advanced)

### Backup of HMI data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Regular backups of HMI device data keep downtimes to a minimum, for example, when you replace a device. You simply transfer the backup data to the HMI device, restoring the original status.

#### Data backup with WinCC

If an HMI device is connected to the configuration PC, you can back up and restore HMI device data from the configuration PC using WinCC.

#### Scope of data backup

Which data is backed up and restored depends on the type of HMI device:

- Complete backup

  Depending on the HMI device: Runtime, firmware, operating system, configuration, recipes, user administration, settings

  > **Note**
  >
  > License Keys can only be stored only in the following HMI devices:
  >
  > - Mobile Panel Wireless
  > - Comfort Panel
  >
  > The License Keys are not saved for the following HMI devices:
  >
  > - all other Windows CE HMI devices
- Firmware/configuration
- Recipes only
- Only recipes in CSV format
- User administration only

A backup file with the extension *.psb is generated when you backup the data of an HMI device.

As a general rule, you can backup the data to any storage medium. If the HMI device is networked, you can also backup the data to a server.

> **Note**
>
> **Scope of data backup for Windows CE HMI devices**
>
> Data backup secures the contents of the flash memory. Alarm logs and process value logs are generally saved on the external storage medium. Alarm logs and process value logs are therefore not backed up. If necessary, back up the contents of the memory card separately.
>
> Please note the following when performing a complete data file backup and restore operation for Windows CE devices:
>
> - A full backup includes all options installed. As a rule, the backup includes all options data that is still available after "POWER OFF".
> - All data on the device, including License Keys and the operating system, are permanently deleted when you perform complete data restoration.
> - If the data restoration was interrupted, execute the command "Reset to factory settings". Restart data restoration.

> **Note**
>
> Use interfaces with high bandwidths, e.g. USB or Ethernet to backup and restore data.

> **Note**
>
> For Windows CE devices, you can also backup the data directly to a CF or PC card, independent of ProSave and WinCC. For additional information, refer to the relevant operating instructions.

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backing-up-and-restoring-data-of-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

> **Note**
>
> Use the restore function for project data only on operating devices which were configured using the same configuration software.

#### Requirement

- The HMI device is connected to the configuration PC
- The HMI device is selected in the project tree.
- If a server is used for data backup: The configuration PC has access to the server

#### Backup of the data of the HMI device

Proceed as follows to backup the data of the HMI device:

1. Select the "Backup" command from the "Online &gt; HMI Device maintenance" menu.

   The "Create backup" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Create".

   The "SIMATIC ProSave" dialog box opens.
3. Select the data to backup for the HMI device under "Data type".
4. Enter the name of the backup file under "Save as".
5. Click "Start Backup".

This starts the data backup. The backup operation takes some time, depending on the connection selected.

#### Restoring the data of the HMI device

Proceed as follows to restore the data of the HMI device:

1. Select the "Restore" command from the "Online &gt; HMI Device maintenance" menu.

   The "Restore backup" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Load".

   The "SIMATIC ProSave" dialog box opens.
3. Enter the name of the backup file under "Save as".

   Information about the selected backup file is displayed under "File information".
4. Click "Start Restore".

This starts the restoration. This operation takes some time, depending on the connection selected.

#### Backup/Restore from the "Backup/Restore" dialog in the Start Center of the HMI device

The "Backup/Restore" function is enabled for MMC, SD memory cards and USB mass storage devices. The storage media supported depend on the HMI device.

> **Note**
>
> **Connections between Basic Panels and controllers**
>
> If you use the "Backup/Restore" function, a maximum of two connections from Basic Panels to the following controllers are possible at any given time:
>
> - SIMATIC S7-1200
> - SIMATIC S7-1500

For more information on this topic, refer to the device manual of the employed HMI device.

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Backup of HMI data (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backup-of-hmi-data-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Updating the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Update the HMI device image if the version is incompatible with the configuration. The image version matches the device version.

Update the operating system and Runtime software of the HMI device with the help of the device version. While loading the project, you may be prompted to run an automatic update of the device version, depending on the protocol used.

Loading will then continue. Loading of the project is otherwise aborted. In this case, perform the update of the device version manually.

> **Note**
>
> A device version can only be updated on HMI devices that are not PC-based.

#### Updating the device version

Connect the HMI device to the configuration PC to update the device version. If possible, use the interface providing the highest bandwidth for this connection, e.g. Ethernet. An update of the device version via serial connection may take up to an hour.

#### "Reset to factory settings"

If the operating system on the HMI device is no longer operational, update the operating system and reset the HMI device to the factory settings.

> **Note**
>
> **Resetting to factory settings via Ethernet for Basic Panels**
>
> You require the following to reset the HMI device to the factory settings via Ethernet:
>
> - the MAC address of the HMI device
> - the available IP address
> - the programming device/PC interface of the configuration PC set to Ethernet TCP/IP
>
> The programming device/PC interface is configured using the control panel of the configuration PC. Select" "S7ONLINE (STEP7) -&gt; TCP/IP" in the "Access point of the application" field.

> **Note**
>
> **Reset to factory settings for Comfort Panels**
>
> To reset the Comfort Panels to factory settings, please use ProSave.
>
> With the exception of Comfort Panels, you can reset all HMI devices to factory settings with the menu item "Online &gt; HMI Device maintenance &gt; Reset factory settings".

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-on-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Updating the operating system on the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

If possible, you should use the interface with the highest bandwidth for this connection, such as Ethernet. Updating the operating system via a serial connection can take up to an hour. When you update the operating system, the Runtime software on the HMI device is also updated and the device version is changed.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Updating the operating system deletes all data on the HMI device**  When you update the operating system you delete data on the target system. For this reason, you should back up the following data beforehand:  - User administration - Recipes   Resetting to factory settings also deletes the License Keys. Back up the License Keys before you reset the system to factory settings. |  |

#### Requirement

- The HMI device is connected to the configuration PC.
- The HMI device is selected in the project tree.

#### Updating the operating system

Proceed as follows to update the operating system:

1. Select the "Update operating system" command from the "Online &gt; HMI Device maintenance" menu.

   The "Update operating system" dialog box opens.
2. Select the type of the PG/PC interface and the target device, and click "Update".

   The "SIMATIC ProSave [OS-Update]" dialog opens. The path to the image is preset.
3. If required, you can select a different path for the image that you want to transfer to the HMI device.
4. Click "Update OS".

This starts the update. The update operation can take time, depending on the connection selected.

#### Resetting the HMI device to factory settings

To reset the HMI device to factory settings, proceed as follows:

1. Switch off power to the HMI device.
2. Connect the HMI device to the Engineering Station.
3. Select the "Update operating system" command from the menu under "Online &gt; HMI Device maintenance" on the configuration PC in WinCC.

   The "Update operating system" dialog box opens.
4. Select the type of the PG/PC interface and the target device, and click "Update".

   The "SIMATIC ProSave [OS-Update]" dialog opens. The path to the image is preset.
5. If required, you can select a different path for the image that you want to transfer to the HMI device.
6. Activate "Reset to factory settings".
7. Click "Update OS".
8. To reset to factory settings, switch on the power to the HMI device again.

   This operation can take time.

#### Result

The operating system of the HMI device is operational and up-to-date.

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Updating the operating system (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-the-operating-system-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Transferring license keys (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#transferring-license-keys-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing licenses (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-licenses-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview for loading of projects (Panels, Comfort Panels)](#overview-for-loading-of-projects-panels-comfort-panels)
  
[Backing up and restoring data of the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#backing-up-and-restoring-data-of-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of HMI device maintenance (Basic Panels) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-device-maintenance-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Updating the operating system of the HMI device from a data carrier (Panels, Comfort Panels)

#### Introduction

You can update the operating system using a data carrier for Comfort Panels and Mobile Panels.

You can find the HMI image files, for example, in the installation directory of WinCC under: "\Siemens\Automation\Portal V1x\Data\Hmi\Transfer\&lt;HMI device image version&gt;\Images".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss**  All data on the HMI device, including the project and HMI device password, is deleted during a restore operation. License keys are only deleted after a security prompt.  Back up your data before the restore operation, if necessary. |  |

#### Requirements

- The HMI device image file is located in the "SIMATIC.HMI\Firmware\" directory on your data carrier, e.g. a SIMATIC HMI Memory card or an industry-grade USB stick.
- The data carrier with the relevant HMI device image file including operating system is inserted in the HMI device.

#### Procedure

1. Open the "Control Panel" on your HMI device.
2. Open the "Service &amp; Commissioning" dialog using the "Service &amp; Commissioning" icon.
3. Change to the "OS Update" tab.
4. Press "Next".

   The "Update OS image from external memory" dialog opens.
5. Press the "Refresh" button, if necessary.

   The "Accessible devices:" group is updated. The HMI device checks the storage medium. You can find information on this storage medium in the "status information" field.
6. Select the storage medium with the required HMI device image in the "Accesible devices:" group.
7. Press "Next".

   The "Update OS image from:\Storage Card USB" dialog opens.
8. Select the required HMI device image file in the "Firmware files on" group.
9. If you need information about the selected file, press the "Details" button.

   The "Properties of image file" dialog containing the following information is displayed:

   - "Supported": HMI devices that are compatible with the HMI device image
   - "Image version": Version of the HMI device image
   - "Image size": Size of the image file
   - "Creation": Date the image file was created
10. To delete the selected file, press the "Delete" button.  
    The "Delete confirmation" dialog is displayed. The file will be deleted when you press "OK".
11. To restore the data of the selected file, press the "Update" button.

    The "Update settings" dialog informs you that the settings in the Control Panel will be kept and offers you the option of keeping or deleting license keys present on the HMI device.
12. Press "Update".

    The "Update OS Image" dialog opens.
13. To start restoring the operating system, press "Yes".  
    The "Transfer" dialog is displayed. A progress bar shows the course of the restore. The HMI device then restarts.

**Note**

If there is no storage medium or a defective storage medium in the HMI device, the "0 devices found" message is displayed. Insert the storage medium or replace the storage medium.

> **Note**
>
> After the restore, it may be necessary to recalibrate the touch screen.

### Transferring license keys (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You need a license for certain WinCC Runtime options you may want to install on an HMI device. Usually, the necessary licenses supplied as "License Keys" on a data medium, e.g. USB stick. The "License Keys" can also be made available on a license server.

Use "Automation License Manager" to transfer the "License Keys" to or from an HMI device. The "Automation License Manager" is included automatically when you install WinCC.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Backing up License Keys**  In the following cases you have to backup the "License Keys" in order to prevent deletion of the "License Keys":  - Prior to the update of the operating system of a Windows CE HMI device - Prior to restoring the data from a full backup   "License Keys" on an HMI device are backed up depending on the HMI device configuration. For more information, refer to the operating instructions of the corresponding HMI device. |  |

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing licenses (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-licenses-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Managing licenses (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Requirement

- The HMI device is connected to the configuration PC or the PC running the "Automation License Manager".
- If you are using the configuration PC: The HMI device is selected in the project tree.

#### Procedure

To transfer license keys, follow these steps:

1. Open the "Automation License Manager". Go to the Windows Start menu and start "Automation License Manager" on a PC on which WinCC is not installed.

   The "Automation License Manager" starts.
2. Select the "Connect HMI device" command from the "Edit &gt; Connect target system" menu.

   The "Connect target system" dialog opens.
3. Select the HMI device type in the "Device type" area.
4. Select the "Connection".
5. Configure the "connection parameters" associated with the selected connection.

   ![Procedure](images/108151556491_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/108151556491_DV_resource.Stream@PNG-en-US.png)
6. Click "OK".

   The connection to the HMI device is now set up. The connected HMI device is displayed in the left pane of "Automation License Manager".
7. Transfer the "License Keys" to the HMI device:

   - In the left pane, select the drive on which the "License Keys" are located.

     The "License Keys" are displayed on the right pane.
   - Select the "License Keys"
   - Drag-and-drop the "License Keys" to the HMI device.

You can also remove License Keys from the HMI device using drag-and-drop.

#### Alternative procedure

You can also start the "Automation License Manager" from WinCC on a PC with a WinCC installation: Select the "Authorize/License" command in the "Online &gt; HMI Device maintenance" menu.

#### Result

The "License Keys" are transferred to the HMI device.

To backup the "License Keys" from the HMI device, drag-and-drop the "License Keys" from the HMI device to an available drive.

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Transferring license keys (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#transferring-license-keys-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Installing and uninstalling an option (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can install the following options on an HMI device:

- Additional options supplied with WinCC
- Options purchased in addition to WinCC

Which options you can install depends on the HMI device type.

#### Requirement

- The HMI device is connected to the Engineering Station, or to the PC with ProSave.
- The HMI device is selected in the project tree.

#### Procedure

To install an option on the HMI device, proceed as follows:

1. Select the "Options" command from the "Online &gt; HMI Device maintenance" menu.

   The "Load options" dialog opens.
2. Select the type of the PG/PC interface and the target device, and click "Load".

   The "SIMATIC ProSave" dialog box opens.

   All available options and the previously installed options are displayed.
3. To display the installed options on the HMI device, click "Device status".
4. To install an option on the HMI device, select the option under "Available options" and click "&gt;&gt;".
5. To uninstall an option from the HMI device, select the option under "Available options" and click "&lt;&lt;".

#### Result

The selected options are installed on or uninstalled from the HMI device.

---

**See also**

[ProSave (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#prosave-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Loading Asian fonts to the HMI device (Panels, Comfort Panels, RT Advanced)

#### Introduction

When using Asian languages, only the Asian characters that were used in configuring the HMI device are loaded to the HMI device during the transfer. If the texts are sent directly from the controller to the HMI device as with controller alarms or with ProDiag, you may encounter display problems. You can load the complete Asian font to the HMI device in these cases.

#### Procedure

1. Select the HMI device in the project tree.
2. Select the "Options" command from the "Online &gt; HMI device maintenance" menu.

   The "Load options" dialog opens.
3. Select the type of the PG/PC interface and the target device, and click "Load".

   The "SIMATIC ProSave" dialog box opens.
4. Select the respective font under "Available options" and click "&gt;&gt;".

   The font is loaded to the HMI device.

---

**See also**

[Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-rt-professional)
  
[Sending a complete alarm from the controller to the HMI device and automatic update (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-panels-comfort-panels-rt-advanced)
  
[Making characters available for HMI tags of the type WString/WChar (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#making-characters-available-for-hmi-tags-of-the-type-wstringwchar-panels-comfort-panels-rt-advanced-rt-professional)
