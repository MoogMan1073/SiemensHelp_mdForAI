---
title: "Visualizing Processes with View of Things (RT Unified)"
package: VoTWCCUenUS
topics: 25
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Visualizing Processes with View of Things (RT Unified)

This section contains information on the following topics:

- [WinCC Unified View of Things for PLC (RT Unified)](#wincc-unified-view-of-things-for-plc-rt-unified)
- [Installation and functionalities (RT Unified)](#installation-and-functionalities-rt-unified)
- [Configuring WinCC Unified VoT for PLC (RT Unified)](#configuring-wincc-unified-vot-for-plc-rt-unified)

## WinCC Unified View of Things for PLC (RT Unified)

View of Things (VoT) for PLC is a web application in the memory of the SIMATIC S7-1500 PLC. View of Things displays in a web browser the data that you have configured for a PLC in the TIA Portal with WinCC Unified.

The WinCC Unified process visualization is based on the HTML5 web technology. With VoT you can use the web-based HMI concept for devices that have a web server, e.g. a SIMATIC PLC.

You use WinCC Unified Engineering in the TIA Portal to create a web application for various devices and to map the process. With VoT, you build a basic web-based visualization with the look and feel of WinCC Unified. You connect to the device's web server via a web browser. You operate the objects in the View of Things web application.

### WinCC Unified View of Things (VoT)

You use the "Screens" editor of WinCC Unified Engineering in the WinCC Unified View of Things web application.

In the VoT application, you have access to:

- Screens
- Tags

You use the same types of dynamization as in the "Screens" editor to dynamize the screens and screen objects:

- Tags
- System functions
- Scripts

### VoT version

TIA Portal always uses the current version of VoT. The version of the VoT application is not visible. You cannot change the version.

### Updating VoT

If you create a project with VoT in V17 and open the project in V18, the VoT application will be updated to the latest version of V18. The update takes effect when you edit or compile the VoT application in V18.

If you download the VoT application from V17 and do not compile it, the result from V17 will be retained.

## Installation and functionalities (RT Unified)

### Installing View of Things

The VoT application is included with the installation of the TIA Portal in the Engineering System. To use VoT, you need at least one license for configuring Unified devices.

### Functionalities of View of Things

The following table shows an overview of the supported and non-supported functionalities of VoT:

|  | Supported | Not supported |
| --- | --- | --- |
| PLC of the S7-1500 family  Firmware Version ≥ 2.9 and with web server functionality | SIMATIC S7-1500, incl. SIPLUS and SIPLUS RAIL  SIMATIC ET 200 CPU, incl. SIPLUS and SIPLUS RAIL  SIMATIC Drive Controller  SINUMERIK ONE  Software Controller  Motion Control | SIMATIC ET 200pro CPU  Software PLC |
| Screens and screen objects | You can find an overview of supported screen objects in [Supported screen objects](#supported-screen-objects-rt-unified). | You can find an overview of non-supported screen objects in [Supported screen objects](#supported-screen-objects-rt-unified). |
| Dynamizations | You can find an overview of supported dynamizations in [Supported types of dynamization](#supported-types-of-dynamization-rt-unified). | - |
| System functions in the runtime model | You can find an overview of supported system functions in [Use system functions](#use-system-functions-rt-unified). | You can find an overview of non-supported system functions in [Use system functions](#use-system-functions-rt-unified). |
| Scripts in the runtime model | Objects and functions with regard to tags and screen objects | - |
| Texts and graphics | Multilingual texts and graphics | Text and graphic lists |
| Project languages | Several languages | - |
| Cycles | Only system-defined cycles | - |

> **Note**
>
> You can find all information on the web server in the "[Web server](https://support.industry.siemens.com/cs/ww/en/view/59193560)" Function Manual.

## Configuring WinCC Unified VoT for PLC (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring View of Things (RT Unified)](#configuring-view-of-things-rt-unified)
- [Error diagnostics with View of Things (RT Unified)](#error-diagnostics-with-view-of-things-rt-unified)

### Basics (RT Unified)

In the VoT application, the data that you configured for a PLC in the TIA Portal with WinCC Unified is displayed in a web browser.

You can only create one VoT application for a PLC.

#### VoT version for PLC

The VoT application requires a PLC with firmware V2.9 or higher.

#### Memory requirements

You need a SIMATIC Memory Card. The memory of the PLC is not used by your VoT application. The files generated in the VoT application are stored on the SIMATIC Memory Card.

Regardless of the size of the application, VoT occupies at least 8 MB for basic functions. Icons and graphics require additional memory.

#### Automatic scaling in the web browser

A VoT application starts in "Automatic scaling" mode by default. The screen content is always scaled so that the complete screen is visible in the web browser window.

To switch off the automatic scaling, you can use the following script line, e.g. in the "Loaded" event on the start screen: "UI.RootWindow.Adaption = 0".

#### Restriction

If a PLC is located in the "Modules not plugged in" data storage in the device view, the VoT application only functions to a limited extent. Delete the VoT application before moving a PLC into the "Modules not plugged in" data storage.

If the PLC is located in the "Modules not plugged in" data storage, do not create a VoT application.

![Restriction](images/143047524875_DV_resource.Stream@PNG-en-US.png)

### Configuring View of Things (RT Unified)

This section contains information on the following topics:

- [Configuring VoT - Overview (RT Unified)](#configuring-vot---overview-rt-unified)
- [Configuring user management (RT Unified)](#configuring-user-management-rt-unified)
- [Creating VoT (RT Unified)](#creating-vot-rt-unified)
- [Configuring screens and screen objects (RT Unified)](#configuring-screens-and-screen-objects-rt-unified)
- [Configuring dynamizations (RT Unified)](#configuring-dynamizations-rt-unified)
- [Compiling VoT (RT Unified)](#compiling-vot-rt-unified)
- [Loading VoT onto the PLC (RT Unified)](#loading-vot-onto-the-plc-rt-unified)
- [Opening VoT in the web browser (RT Unified)](#opening-vot-in-the-web-browser-rt-unified)

#### Configuring VoT - Overview (RT Unified)

This section contains an overview of the individual steps involved in configuring the VoT application for PLCs.

##### Configuring a VoT application – overview

To configure a VoT application for displaying the PLC data, follow these steps:

1. Configuring user management:

   - For PLCs with CPUs firmware version ≤ V3.0, static user management applies.
   - For PLCs with CPUs firmware version ≥ V3.1, local user management applies.
2. Create a VoT application.
3. Configure screens and screen objects.
4. Configure dynamization.
5. Compile the VoT application.
6. Load the VoT application onto the PLC.
7. Open the VoT application in the web control.

The detailed description of the individual steps can be found in the following sections.

#### Configuring user management (RT Unified)

This section contains information on the following topics:

- [Static user management for PLCs configured with firmware version ≤ V3.0 (RT Unified)](#static-user-management-for-plcs-configured-with-firmware-version-v30-rt-unified)
- [Local user administration for PLCs configured with firmware version ≥ V3.1 (RT Unified)](#local-user-administration-for-plcs-configured-with-firmware-version-v31-rt-unified)

##### Static user management for PLCs configured with firmware version = V3.0 (RT Unified)

For PLCs with CPUs configured with firmware version ≤ V3.0, configure static user management. In order to manage the static user management, activate the web server.

###### Configuring static user management

To configure the static user management, follow these steps:

1. Double-click "Device configuration" of the PLC.
2. In the Inspector window, under "Properties &gt; General &gt; Web server &gt; General", select the option "Activate web server on this module"

   The "Permit access only with HTTPS" option has no effect on the connection to the VoT application.

   ![Configuring static user management](images/172492096267_DV_resource.Stream@PNG-en-US.png)

   ![Configuring static user management](images/172492096267_DV_resource.Stream@PNG-en-US.png)
3. Activate the required web server access rights in the "Access level" column under "Properties &gt; General &gt; Web server &gt; User management".

   The following access rights are required:

   - Read tags
   - Write tags
   - Open user-defined web pages

   ![Configuring static user management](images/172492091659_DV_resource.Stream@PNG-en-US.png)

   ![Configuring static user management](images/172492091659_DV_resource.Stream@PNG-en-US.png)

**Note**

The function level "Write tags" is required if the user is to change the values. Without the function level "Write tags", the user can only observe the processes.

> **Note**
>
> Observe the requirements for activating the web server. You can find more information in the "[Web server](https://support.industry.siemens.com/cs/ww/en/view/59193560)" Function Manual.

###### Managing the user list

You can manage the user list under "Web server &gt; User management":

- Create users
- Specify access rights
- Assign passwords

  ![Managing the user list](images/172493817099_DV_resource.Stream@PNG-en-US.png)

Users only have access to the options that are permanently linked to the access rights.

Depending on the PLC and firmware used, you can assign different user rights.

---

**See also**

[Opening VoT in the web browser (RT Unified)](#opening-vot-in-the-web-browser-rt-unified)

##### Local user administration for PLCs configured with firmware version = V3.1 (RT Unified)

For PLCs with CPUs configured with firmware version ≥ V3.1, configure local user management under "Security settings &gt; Users and roles".

You can disable access control in the properties of the PLC. To configure user management, configure access control.

###### Configuring access control

You can configure access control in the following ways:

- Disable access control

  - Under "General &gt; Protection &amp; Security &gt; Access control configuration", select the option "Disable access control".

  When access control is disabled, there is no user management in the project. Users who are defined under "Users and roles" are not taken into account, and authentication is not possible. The PLC itself creates an "Anonymous" user that has full access rights to the functions of the web server and the PLC.
- Enable access control

  - Under "General &gt; Protection &amp; Security &gt; Access control configuration", select the option "Enable access control".

  When access control is enabled, you can manage all users in the "Security settings &gt; Users and roles" editor.

  Access control is enabled by default.

![Configuring access control](images/172522293643_DV_resource.Stream@PNG-en-US.png)

###### Configuring local user management

To configure local user management, follow these steps:

1. Click on the "Security settings &gt; Users and roles" editor in the project tree.
2. Add users in the "Users" tab.

   ![Configuring local user management](images/172581008139_DV_resource.Stream@PNG-en-US.png)

   ![Configuring local user management](images/172581008139_DV_resource.Stream@PNG-en-US.png)
3. Define the user data: User name, password, Runtime timeout, Comment.
4. Add a user-defined role in the "Roles" tab.

   ![Configuring local user management](images/172577842187_DV_resource.Stream@PNG-en-US.png)

   ![Configuring local user management](images/172577842187_DV_resource.Stream@PNG-en-US.png)
5. Assign the user a user-defined role in the "Users" and "Assigned roles" tabs.

   ![Configuring local user management](images/172584926603_DV_resource.Stream@PNG-en-US.png)

   ![Configuring local user management](images/172584926603_DV_resource.Stream@PNG-en-US.png)
6. Assign the user-defined roles function rights in the "Roles" and "Runtime rights" tabs.

   The following Runtime rights are particularly relevant for View of Things:

   - Read process data
   - Write process data
   - Open user pages

   ![Configuring local user management](images/172580999563_DV_resource.Stream@PNG-en-US.png)

   ![Configuring local user management](images/172580999563_DV_resource.Stream@PNG-en-US.png)
7. Load the configuration to the PLC.

###### Information on configuring local user management

You can find detailed information on configuring local user management in the online help:

- On STEP 7 in the "Basics of user management in the TIA Portal" section.
- On WinCC Unified in the "Configuring user management in the Engineering System for Runtime" section.

#### Creating VoT (RT Unified)

##### Requirement

- A project is open.
- A SIMATIC S7-1500 PLC is configured.

##### Configuring a VoT application

You can configure the VoT application in the engineering system in the project tree under "Web applications", then "Add new VoT application".

To create a VoT application, follow these steps:

1. Click "Web applications" in the project tree.
2. Add a VoT application. The web application "ViewOfThings (WinCC Unified VoT)" is created.

   ![Configuring a VoT application](images/162073410827_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a VoT application](images/162073410827_DV_resource.Stream@PNG-en-US.png)
3. Rename the VoT application. Take the following into consideration:

   - The name must not be longer than 25 characters.
   - Valid characters are A-Z a-z 0-9 _ -.

   The name of the VoT application must be unique in a TIA Portal project.

**Note**

The following names are not allowed as VoT application names:

"CON", "CLOCK$", "PRN", "AUX", "NUL", "COM0", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT0", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9", "Context", "Saved".

If you use one of these names, a "_" character is appended to the name during the compilation. The application can be called under the changed name (e.g. https://192.168.0.1/~con_/index.html).

##### Specifying runtime settings

Specify the Runtime settings of the VoT application.

![Specifying runtime settings](images/172784644747_DV_resource.Stream@PNG-en-US.png)

The application cycle is the time interval in milliseconds at which the user interface in the VoT application is updated. Note that small cycle times cause a higher processor load.

##### Deleting a VoT application

You can delete the VoT application by using "Delete" in the shortcut menu or in the toolbar of the engineering system.

#### Configuring screens and screen objects (RT Unified)

This section contains information on the following topics:

- [Configuring screens (RT Unified)](#configuring-screens-rt-unified)
- [Supported screen objects (RT Unified)](#supported-screen-objects-rt-unified)
- [Supported functionalities (RT Unified)](#supported-functionalities-rt-unified)

##### Configuring screens (RT Unified)

Like with other devices in WinCC Unified, you can configure screens and screen objects in the VoT application and use different functionalities.

You can use convenient editing functions in the VoT application:

- Create a screen change button by dragging-and-dropping a screen onto another screen in the VoT project tree.
- Create an IO field with a tag by dragging-and-dropping a PLC tag onto the screen.
- Copy screens and screen objects between the VoT application and other Unified devices.

###### Configuring screens

To configure a screen in a VoT application, follow these steps:

1. Create a new screen under "ViewOfThings (WinCC Unified VoT)". The "Screens" editor opens.
2. Configure the screen objects.
3. Select the required PLC tags. The associated HMI tags are created automatically.

   In the project tree, you can open an overview table in the "HMI tags" area under "ViewOfThings (WinCC Unified VoT)". You cannot edit the HMI tags in the table. You can only delete them.
4. Connect the screen objects with the tags.

##### Supported screen objects (RT Unified)

###### Supported screen objects

The following screen objects are supported in the VoT application:

- All basic objects
- All elements except the symbolic IO field
- Controls:

  - Screen window
  - Web browser
- All graphics including SVG graphics
- Dynamic widgets
- Multilingual texts with language-dependent configuration of the fonts
- Multilingual graphics

###### Non-supported screen objects

The following screen objects are not supported in the VoT application:

- Controls, except for the screen window and browser
- My Controls
- Faceplates

##### Supported functionalities (RT Unified)

###### Supported functionalities

The following functionalities are supported in the VoT application:

- Configuring screen resolution
- Select predefined style in "Runtime settings"
- Renaming layers
- Toggling visibility of layers
- Using hotkeys
- Dynamize graphics property of the screen objects

###### Non-supported functionalities

The following functionalities are not supported in the VoT application:

- Two-hand operation
- Access protection for screen objects
- User-defined styles
- Conversion of values via bit masks and expressions
- Grouping of the objects
- Dynamic parameter fields for objects with the "Text" property
- Text and graphic lists

#### Configuring dynamizations (RT Unified)

This section contains information on the following topics:

- [Supported types of dynamization (RT Unified)](#supported-types-of-dynamization-rt-unified)
- [Supported dynamization languages (RT Unified)](#supported-dynamization-languages-rt-unified)
- [Using HMI tags (RT Unified)](#using-hmi-tags-rt-unified)
- [Using scripts (RT Unified)](#using-scripts-rt-unified)
- [Use system functions (RT Unified)](#use-system-functions-rt-unified)

##### Supported types of dynamization (RT Unified)

###### Supported types of dynamization

The following types of dynamization are supported in the VoT application:

- Tag
- Script
- System function

##### Supported dynamization languages (RT Unified)

The languages are supported to a limited extent when formatting the language-dependent output formats, e.g. for the data format "date" and "time".

###### Supported languages

The following languages are supported in the VoT application:

- German
- English
- French
- Italian
- Spanish
- Japanese
- Chinese
- Korean
- Russian
- Turkish
- Portuguese

###### Non-supported languages

English is used for the non-supported languages in the VoT application.

##### Using HMI tags (RT Unified)

In the VoT application you can use simple PLC tags:

- For displaying the value
- For dynamizing screen objects
- To dynamize the graphic properties
- For reading and writing accesses in function lists and scripts

If you use a PLC tag in the VoT application, the associated HMI tag is created automatically.

###### HMI tags in the VoT application

In the VoT application you cannot directly configure the HMI tags that you need for the visualization.

Select the PLC tags for the properties of the screen elements.

![HMI tags in the VoT application](images/143018267019_DV_resource.Stream@PNG-en-US.png)

###### HMI tags overview table

In the project navigation, you open an overview table in the "HMI tags" area under "ViewOfThings (WinCC Unified VoT)". All automatically created HMI tags are displayed in this table.

![HMI tags overview table](images/143021733643_DV_resource.Stream@PNG-en-US.png)

During compilation all tags used are validated. Tag-specific errors are displayed.

If you delete a dynamization, the associated HMI tag is not deleted. These unused tags are ignored during compiling and are also not loaded onto the device.

If you no longer need the HMI tags, you can delete the respective tags in the table.

###### Non-supported tags

- In the VoT application, PLC tags with PLC user data types cannot be used. Access is not possible either to the user data type or to individual elements.

  PLC user data types in the data blocks can be used without restriction.
- The tags of the DTL data type cannot be read or written in the VoT application.

##### Using scripts (RT Unified)

The usage of scripts is restricted in a VoT application.

The scripts run in a browser and must be converted. The conversion can lead to incompatibilities and it cannot be guaranteed that the scripts will run exactly as they do in Unified PC Runtime.

Some tag operations and scripts to change screen objects are supported.

###### Supported scripts

The following scripts are supported in the VoT application:

- At the events of screen objects
- For dynamization of the properties of screen objects
- To dynamize the visibility of layers
- To inform about the resolution of the screen (GetClientInfo).
- To configure a tag as a trigger for the property dynamization via script

###### Non-supported scripts

The following scripts are not supported in the VoT application:

- Global scripts
- To change the style in Runtime

###### Triggering scripts

To improve performance, trigger the execution of scripts with tags. Avoid cyclic triggers.

###### Asynchronous operations

In a VoT application, you cannot use asynchronous operations in scripts. The scripts run in VoT in a browser and are converted to an asynchronous version.

##### Use system functions (RT Unified)

###### Supported system functions

The following system functions are supported in the VoT application:

Screens:

- Logoff
- OpenScreenInPopup
- ClosePopup
- SetPropertyValue
- SetLanguage
- ChangeScreen

Tags:

- IncreaseTag
- InvertBitInTag
- ResetBitInTag
- ShiftAndMask
- SetBitInTag
- SetTagValue
- DecreaseTag

###### Non-supported system functions

Other system functions that are not listed as supported system functions here are not supported in the VoT application, e.g.:

Tags:

- UpdateTag

#### Compiling VoT (RT Unified)

When the PLC is compiled, the VoT application is not included automatically in the compilation. You must explicitly compile the VoT application after changes. When the PLC is loaded, the last compiled status of the VoT application is considered.

##### Compiling a VoT application

To compile the VoT application, follow these steps:

1. Select the VoT application or its subnode.
2. In the popup menu of the VoT application select the command "Compile &gt; Software (only changes)" or "Compile &gt; Software (compile all)" from the shortcut menu.

   Alternatively, click the icon for compilation in the toolbar.

> **Note**
>
> A VoT application cannot by compiled if the "Input finished" event is dynamized at an I/O field.

##### Maximum number of files

If the maximum permissible number of files is exceeded while compiling the VoT application, an error is generated.

A warning is issued if any of the following limits is exceeded:

- You have configured more than 10 screens.
- You have used more than 100 tags.

  The tags include all HMI tags displayed in the overview table. This also includes all automatically created tags that are not currently required, for example, because the associated dynamization has been deleted.

To reduce the number of files, you have to delete the screens or the tags.

Note that for language-dependent graphics a file is created for each language.

#### Loading VoT onto the PLC (RT Unified)

##### Loading a VoT application for the first time

To load the VoT application into the PLC for the first time, follow these steps:

1. Compile and load the project into the PLC.
2. Click "Load into device" in the "Load preview" dialog in the "Web applications" area.
3. Activate the "Load into device" option.
4. Click "Load". The VoT application is loaded.

   ![Loading a VoT application for the first time](images/143017911051_DV_resource.Stream@PNG-en-US.png)

   ![Loading a VoT application for the first time](images/143017911051_DV_resource.Stream@PNG-en-US.png)

##### Reloading a PLC program with VoT application

You have made the changes in the VoT application.

To load the VoT application again, follow these steps:

1. Compile the VoT application.
2. Compile and load the project into the PLC.
3. Click "Update online?" in the "Load preview" dialog in the "Web applications" area.
4. Activate the "Update" option.
5. Click "Load". The changes in the VoT application are loaded.

   ![Reloading a PLC program with VoT application](images/143017683339_DV_resource.Stream@PNG-en-US.png)

   ![Reloading a PLC program with VoT application](images/143017683339_DV_resource.Stream@PNG-en-US.png)

##### Reloading the PLC program with another VoT application.

If another VoT application already exists on the PLC, you have to delete this VoT application.

To load a new VoT application, follow these steps:

1. Compile the VoT application.
2. Compile and load the project into the PLC.
3. Click "Delete online?" in the "Load preview" dialog in the "Web applications" area.
4. Activate the "Delete" option.
5. Click "Load". The new VoT application is loaded.

   ![Reloading the PLC program with another VoT application.](images/143289790475_DV_resource.Stream@PNG-en-US.png)

   ![Reloading the PLC program with another VoT application.](images/143289790475_DV_resource.Stream@PNG-en-US.png)

##### Reloading the PLC program without VoT application

If another VoT application already exists on the PLC and you load a PLC program without VoT application, the "Load preview" dialog offers no possibility to delete the VoT application.

To delete the previous VoT application, follow these steps:

1. Click "Add VoT application".
2. Delete the VoT application immediately afterwards.
3. During the next loading process, the option is offered in the "Load preview" dialog to delete an existing VoT application.

   ![Reloading the PLC program without VoT application](images/143294037387_DV_resource.Stream@PNG-en-US.png)

   ![Reloading the PLC program without VoT application](images/143294037387_DV_resource.Stream@PNG-en-US.png)

Alternatively, you can also deactivate the web server of the PLC. The VoT application then exists on the PLC, but cannot be addressed.

##### Uploading a PLC with VoT application

The VoT application does not support uploads. If a VoT application exists on the PLC, the PLC in TIA Portal does not contain the VoT application after the upload.

##### Offline loading

You can also save a project with VoT application offline to a SIMATIC Memory Card.

#### Opening VoT in the web browser (RT Unified)

##### Opening a VoT application in the web browser

To open the VoT application in the web browser, follow these steps:

1. Start a web browser.
2. The URL results from the IP address of the PLC, the name of the VoT application and the name of the default page, e.g. "https://&lt;PLC IP address&gt;/~&lt;VoT application name&gt;/index.html".  
   Example: "https://192.168.0.1/~ViewOfThings/index.html".
3. Log in to the VoT application. After logging on, the start screen is displayed.

##### Opening a VoT application via the standard web pages of the PLC

To open the VoT application via the standard web pages of the PLC in the web browser, follow these steps:

1. Start a web browser.
2. Enter the IP address of the PLC in the URL field of the web browser.

   Example: "https://192.168.0.1/
3. The connection is set up and the "Intro" page opens. Click "NEXT" to go to the web server start page.
4. Log in to the web server of the PLC.
5. Select "User-defined pages" in the navigation of the PLC. Click "Homepage of the ViewOfThings application".

   ![Opening a VoT application via the standard web pages of the PLC](images/143059161867_DV_resource.Stream@PNG-en-US.png)

   ![Opening a VoT application via the standard web pages of the PLC](images/143059161867_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The "User pages" selection is visible to you if you have activated the access right "Open user-defined web pages" in the "Access level" column under "Properties &gt; General &gt; Web server &gt; User management" in the Inspector window of the device configuration of the PLC.

---

**See also**

[Static user management for PLCs configured with firmware version ≤ V3.0 (RT Unified)](#static-user-management-for-plcs-configured-with-firmware-version-v30-rt-unified)

### Error diagnostics with View of Things (RT Unified)

For the VoT application, no error diagnostics is possible with the WinCC Unified Trace Viewer.

#### Error diagnostics options with View of Things

Select one of the following options to perform error diagnostics:

- Use the development console of the web browser which is used as the Unified web client.
- In the web client, press &lt;Shift + F12&gt;.

  The internal WinCC Unified diagnostics opens. The right side of the web browser lists the "HMIRuntime.Traces", warnings and errors.

Script debugging is not supported for View of Things.
