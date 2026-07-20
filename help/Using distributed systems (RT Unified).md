---
title: "Using distributed systems (RT Unified)"
package: RemoteWCCUenUS
topics: 45
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using distributed systems (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Unified Collaboration (RT Unified)](#unified-collaboration-rt-unified)
- [Web Client (RT Unified)](#web-client-rt-unified)
- [WinCC Smart Server (RT Unified)](#wincc-smart-server-rt-unified)

## Overview (RT Unified)

### Unified Collaboration

Unified Collaboration gives you the option to monitor and operate the runtime of an HMI device within the runtime of another HMI device.

Both HMI devices must be configured accordingly and located in one network. Unified Collaboration supports cross-project access.

To display the screens of the Collaboration device in runtime, use screen windows.

### Web client

By using the web client you can access the runtime of an HMI device from any device.

Each web client is autonomous and independent of the runtime displayed locally on the HMI device. We are distinguishing here between synchronous and asynchronous functions.

### SmartServer

With the "SmartServer" option you can access a Unified Comfort Panel using an application.

You activate the SmartServer in the TIA Portal in the runtime settings of the Unified Comfort Panel. You download the application to the device from which you want to access the Panel and execute it.

The user interface of the Panel is mirrored. It will give you access to the entire device including Control Panel and runtime. All actions that you are executing via the application are immediately visible on the Unified Comfort Panel.

## Unified Collaboration (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Preparing Unified Collaboration (RT Unified)](#preparing-unified-collaboration-rt-unified)
- [Using Unified Collaboration (RT Unified)](#using-unified-collaboration-rt-unified)
- [Example: Connecting HMI devices from two projects with Unified Collaboration (RT Unified)](#example-connecting-hmi-devices-from-two-projects-with-unified-collaboration-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Requirements (RT Unified)](#requirements-rt-unified)
- [Restrictions (RT Unified)](#restrictions-rt-unified)
- [User management (RT Unified)](#user-management-rt-unified)
- [System functions and scripts (RT Unified)](#system-functions-and-scripts-rt-unified)

#### Basics (RT Unified)

##### Introduction

You can use Unified Collaboration to access Unified Runtime objects, such as screens of another HMI device. You can display and operate the screens.

You use Unified Collaboration together with:

- SIMATIC WinCC Unified PC
- SIMATIC Unified Comfort Panel

The collaboration devices can be created in the same project or in different projects. The configuration steps are different for both variants.

![Introduction](images/152830215947_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
| ![Introduction](images/152802899083_DV_resource.Stream@PNG-de-DE.png) |  | Unified PC |
| ![Introduction](images/152802903563_DV_resource.Stream@PNG-de-DE.png) |  | Unified Comfort Panel |
| ![Introduction](images/152803496843_DV_resource.Stream@PNG-de-DE.png) |  | Screen window |

##### Configuration steps for HMI devices in the same project

1. Create a project.
2. Add multiple HMI devices.
3. Create screens for the HMI devices.
4. Making certificates available.
5. Define collaboration settings.
6. Assign the screens to the screen windows.
7. Compile and load all HMI devices.

##### Configuration steps for HMI devices in different projects

1. Creating multiple projects.
2. Add multiple HMI devices.
3. Create screens for the HMI devices.
4. Making certificates available.
5. Define collaboration settings.
6. Export screen references for Unified Collaboration.
7. Import screen references for Unified Collaboration.
8. Assign the screens to the screen windows.
9. Compile and load all HMI devices.

##### OPC UA Collaboration

If several HMI devices operate in collaboration as OPC UA servers, the collaboration devices can read and write tags and alarms from the OPC UA servers.

---

**See also**

[Restrictions (RT Unified)](#restrictions-rt-unified)
  
[Creating certificates (RT Unified)](#creating-certificates-rt-unified)
  
[Configuring a screen window within a project (RT Unified)](#configuring-a-screen-window-within-a-project-rt-unified)
  
[Defining collaboration settings (RT Unified)](#defining-collaboration-settings-rt-unified)
  
[Configuring screen windows from different projects (RT Unified)](#configuring-screen-windows-from-different-projects-rt-unified)

#### Requirements (RT Unified)

To use Unified Collaboration among several devices, the following requirements must be fulfilled:

- The following software is installed on each participating device:

  SIMATIC WinCC Unified Runtime V19 (basic package, license required)

  > **Note**
  >
  > **Collaboration certificates and Runtime version**
  >
  > Runtime Collaboration requires that the Collaboration certificates of 2 Collaboration partners have been created with a Certificate Authority device whose installed Runtime version is equal to or higher than the installed Runtime version of the Collaboration partner with the higher Runtime version.
  >
  > This is why upgrading Collaboration devices may require re-creation, distribution, and installation of Collaboration certificates.
  >
  > Example:
  >
  > - A Unified PC and a Unified Panel with a V18 Runtime are Collaboration partners.
  > - You upgrade the Unified Panel to V19.
  > - On a certificate authority device with an installed Runtime version V19 or higher, create new Collaboration certificates for both HMI devices.   
  >   Distribute and install them on the devices.
- All devices connected via Unified Collaboration must be on the same network and have access to one another.
- Firewall settings of the Unified PC: During TIA Portal setup, the components of the Unified Collaboration are released to the firewall. The security release for the local subnet and can be adapted manually if required. Note the firewall rules "WinCC RTIL dist" and "WinCC RTIL proxy" in this regard.

  The firewall settings are relevant for the collaboration between multiple Unified PCs and for the collaboration between Unified PCs and Unified Comfort Panels.
- Local session tags are supported for V18 or later devices. In a multi-user environment, session-related data is processed independently in each local session. Data from local session tags is not saved after a session is closed.

---

**See also**

[Creating certificates (RT Unified)](#creating-certificates-rt-unified)
  
[Using WinCC version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#using-wincc-version-compatibility-rt-unified)

#### Restrictions (RT Unified)

Note the following restrictions when using Unified Collaboration and associated Runtimes:

##### Screen objects

Unified Collaboration does not support all screen objects. The following screen objects cannot be used in screens that are displayed in another Runtime via Unified Collaboration:

- My controls:

  - Plant overview

##### System functions and scripts

Executing scripts and system functions depends on the objects used. You can find additional information in the section [System functions and scripts](#system-functions-and-scripts-rt-unified).

##### Subsequent changes to collaboration settings

The following data must not be changed after a connection has been established:

- System ID
- Collaboration name
- IP address / Host name

##### Synchronicity of the system times

The system times of the interconnected HMI devices must not differ by more than 180 seconds. If the difference is greater, no connection is established between the devices.

##### Configured languages

The configured and activated languages for Runtime must be the same for all participating devices.

##### Audit

Audit is not supported in Unified Collaboration.

---

**See also**

[Defining collaboration settings (RT Unified)](#defining-collaboration-settings-rt-unified)
  
[Configuring user management in the engineering system for Runtime (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#configuring-user-management-in-the-engineering-system-for-runtime-rt-unified)

#### User management (RT Unified)

Collaboration supports the cross-project use of multiple users.

> **Note**
>
> **Central user management (UMC)**
>
> If you want to use Unified Collaboration across projects, make use of central user management and the following advantages:
>
> - Low configuration effort
> - Organization of users in user groups
> - High security through consistency

You can restrict access to screen objects by using function rights. You configure and manage function rights in the user management.

When you limit the operation of a screen object with a function right and make the screen object available in another HMI device using Unified Collaboration, the user logged into Runtime must have the function right through the assigned roles.

The name of the function right at the screen object is compared to the name of a function right that can be assigned to the logged in user to see whether they match. Access is granted as configured when there is an agreement. It does not matter in this case whether Unified Collaboration is used in one project or across projects.

To avoid confusion, use the same roles and function rights within a system.

#### System functions and scripts (RT Unified)

##### Introduction

You use system functions and scripts in Unified Collaboration in the usual way. Depending on the object, there are some restrictions and special features.

Executing system functions and scripts depends on the objects used.

The objects are arranged in four categories:

- Objects of the Runtime system with system name prefix
- Objects of the Runtime system without system name prefix
- Objects related to the current session
- System functions under "HMIRuntime.Device.SysFct"

##### "Screen name" parameter

In system functions and scripts, you specify the "Screen name" parameter of a collaboration device in the format "Collaboration Name :: Screen name", e.g. "HMI_RT_1 :: Screen_1".

##### "SetPropertyValue" system function

The "SetProperty Value" system function, for example, can be used to change the "Screen" property of a screen window. For the "Value" parameter, you can specify the screen of a collaboration device in the format "Collaboration Name :: Screen name".

> **Note**
>
> The collaboration name and the associated screen name are not referenced in the "SetPropertyValue" system function. If you change the collaboration name or the screen name, you must adapt the system function.

##### Objects of the Runtime system with system name prefix

Scripts and system functions that use objects with a system name prefix are executed on the local HMI device. The objects are read from the collaboration device or written to the collaboration device.

The following objects have a system name prefix, for example:

- "Alarm"
- "AlarmLogging"
- "Tag"
- "TagLogging"
- "LoggedTag"
- "Connection"
- "PlantObject"
- "Report"
- "TextList"
- "Screen" and "ScreenItem"
- "FaceplateInterface"
- "ParameterSetTypes"

##### Example: Objects of the Runtime system with system name prefix

You configure two HMI devices and activate Collaboration:

- "HMI_1" with a "Screen_1" screen
- "HMI_2" with a "Screen_Collaboration" screen and "Tag_1" tag

Configure a button in the "Screen_Collaboration" screen. Configure the "SetTagValue" system function to an event of the button. Enter the following parameters:

- Tag: "Tag_1"
- Value: "1"

In the "Screen_1" screen, configure a screen window in which the "Screen_Collaboration" screen is displayed.

If Runtime is operating and the event is triggered, the system function is executed on the "HMI_1" HMI device. The value of the "Tag_1" tag changes on the "HMI_2" HMI device.

##### Objects of the Runtime system without system name prefix

No collaboration device can be addressed for objects without a system name prefix. The relevant system functions and scripts are executed on the local HMI device. The objects are also obtained from the local HMI device. The following objects have no system name prefix:

- "Database"
- "FileSystem"
- "Timers"
- "Traces"

##### Objects related to the current session

System functions and scripts that contain objects related to the current session are executed on the local HMI device. When executing the scripts and system functions, the effects will show up in the current session of the user currently logged on.

The following objects refer to the current session, for example:

- "DataSet"
- "Language"

The following system functions relate to the current session:

- "Logoff"

##### System functions under "HMIRuntime.Device.SysFct"

System functions under "HMIRuntime.Device" are disabled in Unified Collaboration. The following system functions cannot be used:

- "CreateScreenshot"
- "EjectStorageMedium"
- "GetBrightness"
- "GetDHCPState"
- "GetIPV4Address"
- "GetNetworkInterfaceState"
- "GetSmartServerState"
- "SetBrightness"
- "SetDHCPState"
- "SetIPV4Address"
- "SetNetworkInterfaceState"
- "SetSmartServerState"
- "ShowControlPanel"
- "ShowSoftwareVersion"
- "StartProgram"
- "StopRuntime"

---

**See also**

[Restrictions (RT Unified)](#restrictions-rt-unified)

### Preparing Unified Collaboration (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified-1)
- [Creating certificates (RT Unified)](#creating-certificates-rt-unified)
- [Distributing and installing certificates (RT Unified)](#distributing-and-installing-certificates-rt-unified)
- [Configuring system events for Unified Collaboration (RT Unified)](#configuring-system-events-for-unified-collaboration-rt-unified)
- [Defining collaboration settings (RT Unified)](#defining-collaboration-settings-rt-unified)
- [Changing the collaboration settings (RT Unified)](#changing-the-collaboration-settings-rt-unified)

#### Overview (RT Unified)

Below you will find out which steps are required to use Unified Collaboration. You create and distribute certificates, configure system alarms and specify the settings for collaboration.

This section includes information on the following topics:

- [Creating certificates](#creating-certificates-rt-unified)
- [Distributing and installing certificates](#distributing-and-installing-certificates-rt-unified)
- [Configuring system events for Unified Collaboration](#configuring-system-events-for-unified-collaboration-rt-unified)
- [Defining collaboration settings](#defining-collaboration-settings-rt-unified)
- [Changing the collaboration settings](#changing-the-collaboration-settings-rt-unified)

For more information, refer to the online documentation for the "Certificate Manager".

#### Creating certificates (RT Unified)

##### Introduction

To enable collaboration between different collaboration devices, the corresponding certificates must be provided in advance. All certificates are issued by a common Certification Authority (CA) to simplify the trust relationship between the communication partners.

The root certificate of the CA is classified as trustworthy on each device for each application. When accessing WinCC Unified Runtime via websites, the root certificate must be configured as trustworthy once in the web browser.

To enable collaboration, you need a "Runtime Collaboration certificate" for each collaboration device in addition to the root certificate.

You create and manage the certificates with the WinCC Unified Certificate Manager.

> **Note**
>
> **Renewal of the Runtime Collaboration certificate after upgrading to V19**
>
> After a Runtime Collaboration device has been upgraded to V19, its Runtime Collaboration certificate must be renewed.
>
> Additional information is available under [Using WinCC version compatibility](WinCC%20Unified%20%28RT%20Unified%29.md#using-wincc-version-compatibility-rt-unified).

> **Note**
>
> **Cross-version use of collaboration**
>
> Screens of an HMI device with installed Runtime version V18 can be displayed in a screen window of an HMI device with installed Runtime version V19 via Unified Collaboration.
>
> So that an HMI device with installed Runtime version V18 can participate in collaboration, a Collaboration certificate must be created with a Certificate Manager V19 and transferred to the HMI device with installed Runtime version V18.

##### Creating a root certificate

1. Select a WinCC Unified PC device in your network that is to serve as the certification authority.

   The root certificate and the associated key are only available on this device. The configuration of additional application certificates for other devices is only possible on this device.
2. Open WinCC Unified Certificate Manager on this device.
3. Create a new root certificate. Double-click the "Create new certification authority" button.
4. Enter the properties of the root certificate in the "New certification authority" dialog. The fields are freely editable.

   Mandatory fields:

   - "Certification authority"
   - "Password" for the private key

   If necessary, select a different key length and runtime for the certificate.
5. Click "Create".

The root certificate and its key are stored on the device and used to generate the device certificates.

> **Note**
>
> If the "WinCC Certificate Manager" is restarted on this device, the root certificate and the device certificates generated with it are loaded automatically.

##### Adding devices

1. Right-click the root certificate and select "Add device ...".

   ![Adding devices](images/158237795211_DV_resource.Stream@PNG-en-US.png)

   ![Adding devices](images/158237795211_DV_resource.Stream@PNG-en-US.png)
2. Enter the name and/or IP address of the device in the "New device" dialog box.

   The specification of the IP address is sufficient for Unified Comfort Panel.

   For devices with dynamic IP addresses, enter only the host name.
3. Repeat steps 1 and 2 until all collaboration devices have been added.

**Note**

**Permitted names**

Either the host name or the "Fully qualified domain name" can be used as the name. The name is inserted in the certificates created for the device and used for validation. To avoid validation errors when accessing the web pages, the "Fully qualified domain name" must be used within a domain.

Using the name "localhost" is not permitted and is automatically replaced with the name of the local device by the Certificate Manager.

##### Adding a "Runtime Collaboration certificate"

1. Right-click on a device and select "Add Runtime Collaboration certificate ...".

   ![Adding a "Runtime Collaboration certificate"](images/158216664203_DV_resource.Stream@PNG-en-US.png)

   ![Adding a "Runtime Collaboration certificate"](images/158216664203_DV_resource.Stream@PNG-en-US.png)
2. Enter the properties of the certificate in the dialog.

   If necessary, select a different key length and runtime for the certificate.
3. Create a "Runtime Collaboration certificate" for each collaboration device.
4. If necessary, create additional certificates, e.g. web server certificates.

   You can find additional information in the "WinCC Unified Certificate Manager" operating manual.

##### Result

- You have created the root certificate.
- You have added all collaboration devices.
- You have added a "Runtime Collaboration certificate" for all collaboration devices.
- You have created additional certificates as required.

---

**See also**

[Basics (RT Unified)](#basics-rt-unified-1)
  
[Requirements (RT Unified)](#requirements-rt-unified)
  
[Using WinCC version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#using-wincc-version-compatibility-rt-unified)

#### Distributing and installing certificates (RT Unified)

##### Introduction

To distribute the configured certificates to the corresponding devices, the certificates must be exported to a secure storage file. This file must be transferred manually to the respective device and imported there. The procedure is different for Unified PC and Unified Comfort.

##### Trust communication partners

For successful communication, the collaboration device must trust the root certificates of its communication partners and vice versa.

**Trust relationship between collaboration devices**

Collaboration devices whose certificate configuration comes from the same certificate authority automatically trust each other after the certificate configuration is installed.

**Trust relationship with external communication partners**

To establish the trust relationship with an external communication partner, follow these steps:

1. On the certificate authority device or on the collaboration device:

   Export the root certificate and CRL file to an external data storage medium.
2. On the external communication partners:

   - Connect the external communication partner to the external data storage medium.
   - Copy the files and trust them. To do this, proceed as described in the user help of the device.
   - Export the root certificate of the external communication partner and its CRL file to the external data storage medium.
3. Connect the external data storage medium to the collaboration device.
4. Import the root certificate and the CRL file of the external communication partner into the collaboration device and trust it:

   - Unified PC: Use SIMATIC Runtime Manager.
   - Unified Comfort Panel: In the Control Panel of the device, under "Security", use the "Certificates" > "Import" function.

During the next connection attempt, the communication partners mutually accept their application certificates.

##### Exporting the certificate configuration

After you have completed the certificate configuration of the devices, export the certificate configuration.

The procedures differ for PC devices and Panel devices.

> **Note**
>
> **Distribution of root certificate and CRL file**
>
> Root certificate and CRL file are part of the certificate configuration of a device. They are exported or imported with the certificate configuration, installed and classified as trusted.
>
> On Unified PCs, you can also export the root certificate and the CRL file via the SIMATIC Runtime Manager.

##### Exporting all certificates for Unified PC

1. Right-click the root certificate and select "Export..." > "CA container" in the menu.

   ![Exporting all certificates for Unified PC](images/158222613131_DV_resource.Stream@PNG-en-US.png)

   ![Exporting all certificates for Unified PC](images/158222613131_DV_resource.Stream@PNG-en-US.png)
2. Assign a password in the "Export all" dialog.

   ![Exporting all certificates for Unified PC](images/158225059339_DV_resource.Stream@PNG-en-US.png)

   ![Exporting all certificates for Unified PC](images/158225059339_DV_resource.Stream@PNG-en-US.png)
3. Click on "Export" and select the storage location and file name.

   The data is stored encrypted with the specified password.

##### Exporting the certificate for a device

1. Right-click on the certificate and select "Export certificate" in the menu.

   ![Exporting the certificate for a device](images/158238188939_DV_resource.Stream@PNG-en-US.png)

   ![Exporting the certificate for a device](images/158238188939_DV_resource.Stream@PNG-en-US.png)
2. Select the format for the exported certificate.
3. Select the storage location.

##### Exporting the certificate for Unified Panel

1. Right-click a device and select "Export device > To Panel..." in the menu.

   ![Exporting the certificate for Unified Panel](images/170447108875_DV_resource.Stream@PNG-en-US.png)

   ![Exporting the certificate for Unified Panel](images/170447108875_DV_resource.Stream@PNG-en-US.png)
2. Select a password for encryption and repeat the input.
3. Save the export of the certificates of the device for installation for the Unified Panel.

##### Making certificates available on the Unified devices

The procedures differ for PC devices and Panel devices.

Depending on the device, use the following tool:

- Unified PC: WinCC Unified Certificate Manager
- Unified Comfort Panel: Control Panel > "Security" function

To make the certificates of a Unified HMI device available on the Unified PC, follow these steps:

1. Transfer the CA container or the certificates to the Unified PC.
2. Open the Certificate Manager.
3. Import the certificate configuration.

   ![Making certificates available on the Unified devices](images/158241925003_DV_resource.Stream@PNG-en-US.png)

   ![Making certificates available on the Unified devices](images/158241925003_DV_resource.Stream@PNG-en-US.png)

To install an individual certificate of the device:

1. Under the local machine node, right-click the certificate.
2. Select "Install".

##### Result

You have distributed and installed the required certificates on all collaboration devices.

The Runtime Collaboration certificate only becomes effective after a restart of the WinCC Unified Runtime.

#### Configuring system events for Unified Collaboration (RT Unified)

##### Introduction

An alarm log must be configured in advance in order to display system events relating to collaboration in the alarm view of a collaboration device. The alarm log supports you in identifying connection problems, for example, when a connection cannot be established due to an incorrect system ID.

> **Note**
>
> **System events for collaboration**
>
> System events for collaboration are only available for the current HMI device and the HMI devices that you select in the collaboration settings under "Connect actively to".

##### Requirement

- A Unified device has been configured.

##### Procedure

1. Open the "Logs" editor in the project tree.
2. Switch to the "Alarm logs" tab.
3. Create an alarm log.
4. Make the required settings for the alarm log.
5. Open the "HMI alarms" editor in the project tree.
6. For the alarm class "SystemNotification", define the alarm log created in the "Log" column.
7. If required, you can define the alarm log for other classes.

##### Result

System events for collaboration are displayed in Runtime as logged alarms in the alarm view of the collaboration device.

The system events contain, for example, information on the connection status. Alarms for each connected device are displayed.

---

**See also**

[Log basics (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#log-basics-rt-unified)
  
[Logging alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#logging-alarms-rt-unified)

#### Defining collaboration settings (RT Unified)

A device must be uniquely identifiable in order for it to participate in Unified Collaboration. You make the settings in the "Collaboration" or "Remote access > Collaboration" area of the Runtime settings of the HMI device.

![Figure](images/158246137739_DV_resource.Stream@PNG-en-US.png)

##### Identification

> **Note**
>
> The following information must be different for all devices participating in Unified Collaboration:
>
> - System ID
> - Collaboration name
> - IP address / Host name
>
> If a collaboration device cannot be uniquely identified in all of its information, the configuration is invalid. Errors can occur during the further configuration.

- System ID

  This ID is used for communication between the devices.

  The value can be between 1 and 2046. The system ID must be unique for devices within the project.
- Collaboration name

  If "Generate collaboration name automatically" is enabled, the collaboration name corresponds to the device name. Changes to the device name are transferred automatically.

  If "Generate collaboration name automatically" is disabled, assign the collaboration name manually. The assigned name must be unique across the system and can consist of up to 128 characters.
- IP address / Host name

  The IP address must correspond to the IPv4 format. All devices connected via Unified Collaboration must be in the same network. The IP address or the host name must be unique.

##### Connect actively to

Lists all HMI devices available for collaboration and shows the system ID and IP address/host name.

To select a device as collaboration device, activate the device.

> **Note**
>
> **System events for collaboration**
>
> System events for collaboration are only available for the current HMI device and the HMI devices that you select under "Connect actively".
>
> The system events contain, for example, information on the connection status. Alarms from each connected device are displayed. System events are displayed in the "Alarm view" control as logged alarms.

##### Requirement

- An HMI device has been created.

##### Procedure

To define the settings for Unified Collaboration, follow these steps:

1. Open the "Devices" tab in the project tree.
2. Open the Runtime settings of the respective HMI device.
3. Switch to the "Collaboration" area.

   With Unified Comfort Panel you will find the "Collaboration" area under "Remote access".
4. Select the check box "Enable collaboration" under "General settings".
5. Assign a system ID for the HMI device under "Identification".
6. Specify the collaboration name.
7. Enter the IP address or the hostname of the device.
8. Select the collaboration devices under "Connect actively to".

   In order for a device to be visible under "Connect actively to", the "Enable collaboration" option must be activated for this device.

**Note**

The system ID is incremented separately for different projects. To ensure a unique assignment, change the ID manually.

---

**See also**

[Restrictions (RT Unified)](#restrictions-rt-unified)
  
[Basics (RT Unified)](#basics-rt-unified-1)
  
[Changing the collaboration settings (RT Unified)](#changing-the-collaboration-settings-rt-unified)

#### Changing the collaboration settings (RT Unified)

##### Introduction

A device must be identifiable by a unique system ID for it to participate in Unified Collaboration. When you make changes in the Runtime settings of the HMI device under "Collaboration", you must ensure that the information is valid for all devices participating in Unified Collaboration.

> **Note**
>
> When you change the collaboration settings of a device participating in Unified Collaboration, you must completely compile and download the projects of all participating devices.

##### Changing the collaboration settings

To change the collaboration settings, follow these steps:

1. Change the collaboration settings of an HMI device.
2. Check whether the following information is different for all devices participating in Unified Collaboration:

   - System ID
   - Collaboration name
   - IP address / Host name

   Invalid entries are highlighted in red.
3. If all devices participating in Unified Collaboration are in one project, follow these steps:

   - Perform a full compilation and download of the projects of all participating HMI devices.
4. If the screen references of the device whose collaboration settings were changed are made available in other projects, follow these steps:

   - Export the screen references of the HMI device.
   - Import the screen references of the HMI device into another project.

     The existing data is overwritten.
   - Perform a full compilation and download of the projects of all participating HMI devices.

---

**See also**

[Defining collaboration settings (RT Unified)](#defining-collaboration-settings-rt-unified)
  
[Complete reloading of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#complete-reloading-of-a-project-rt-unified-1)
  
[Basics of downloading projects (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-of-downloading-projects-rt-unified)
  
[Basics for downloading projects (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-for-downloading-projects-rt-unified)
  
[Complete reloading of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#complete-reloading-of-a-project-rt-unified)

### Using Unified Collaboration (RT Unified)

This section contains information on the following topics:

- [Configuring a screen window within a project (RT Unified)](#configuring-a-screen-window-within-a-project-rt-unified)
- [Configuring screen windows from different projects (RT Unified)](#configuring-screen-windows-from-different-projects-rt-unified)
- [Display messages from participating devices (RT Unified)](#display-messages-from-participating-devices-rt-unified)

#### Configuring a screen window within a project (RT Unified)

##### Requirement

- The collaboration devices are in the same network and have access to one another.
- The required certificates are provided.
- The Runtime settings of the collaboration devices are configured.
- Screens are configured for the collaboration devices.

##### Procedure

1. Open the screen on the device on which you want to display screens of the collaboration device.
2. Add a screen window to the screen.
3. Open the Inspector window under "Properties > Properties > General > Screen".
4. Click the selection button in the "Static value" column.

   A new dialog opens.
5. Select the collaboration device in the left area of the window.
6. Select the screen to be displayed in the right area of the window.
7. Confirm your selection.

> **Note**
>
> When you delete a device that is participating in collaboration, the links of its screens to the screen windows of other HMI devices are removed as well.
>
> When the same device is to participate in collaboration again, the screens must be linked once again to the screen windows.

##### Using scripts

Alternatively, you can also configure screen windows via a script:

1. Perform steps 1 and 2 as described above.
2. Open the Inspector window.
3. Configure a script:

   - For an event
   - For an object property
4. Enter the following line:

   `Screen.Windows("Screen window_1").Screen = "HMI_RT_1::Screen_1";`

   Alternatively, use the snippet "Change Screen in Screen window of current screen".
5. Adapt the name of the screen window, the HMI device and the screen.

   In the example, "Screen window_1" is the screen window of the current device and "HMI_RT_1::Screen_1" is the screen of the device connected via Unified Collaboration.

##### Result

After compiling and downloading, the screen of the collaboration device is displayed in screen window in Runtime.

---

**See also**

[Basics (RT Unified)](#basics-rt-unified-1)
  
[Restrictions (RT Unified)](#restrictions-rt-unified)

#### Configuring screen windows from different projects (RT Unified)

This section contains information on the following topics:

- [Export screen references for Unified Collaboration (RT Unified)](#export-screen-references-for-unified-collaboration-rt-unified)
- [Import screen references for Unified Collaboration (RT Unified)](#import-screen-references-for-unified-collaboration-rt-unified)
- [Configuring screen windows from different projects (RT Unified)](#configuring-screen-windows-from-different-projects-rt-unified-1)

##### Export screen references for Unified Collaboration (RT Unified)

###### Introduction

To use Unified Collaboration, the screen references of the screens that are to be available in the Runtime of another HMI device must be exported.

Once this file has been imported into a project, you can use the screens for Unified Collaboration.

###### Requirement

- In the Runtime settings, the IP address or host name of the HMI device that provides the screens for collaboration is specified under "Collaboration".
- At least one screen is configured.
- The required certificates are provided.

###### Procedure

1. Expand the folder of the device in the "Devices" tab of the project navigation.
2. Open the "Collaboration data" editor.
3. Expand the device.

   All available screens of the device are listed.

   ![Procedure](images/158251648011_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158251648011_DV_resource.Stream@PNG-en-US.png)
4. Select the screens you want to export. To do this, put a check mark in the "Export" column of the screen or the group.
5. Click the export icon ![Procedure](images/152230929675_DV_resource.Stream@PNG-de-DE.png).

   A new window opens.
6. Enter a name under which the file is to be saved.

   The "Export completed" dialog box appears.

**Note**

If collaboration is disabled in the Runtime settings of the HMI device, the "Unified Collaboration Export" dialog appears. The export can only be continued when the entries in the Runtime settings are complete:

- System ID
- Collaboration name
- IP address / Host name

> **Note**
>
> Only screen references from a single device can be exported with each export operation. To export the screen references of another device, switch to the device and repeat the operation.

###### Result

You have exported the screen references of the device. You can import the screens into any project.

> **Note**
>
> The exported xml file must not be modified manually.

##### Import screen references for Unified Collaboration (RT Unified)

###### Introduction

To use Unified Collaboration, import screen references from collaboration devices. These devices can be either HMI devices of the same project or of another project.

###### Requirement

- The required certificates are provided.
- The screen references of a collaboration device are exported.

  > **Note**
  >
  > The exported XML file must not be modified manually to ensure error-free import and use of the screens in Runtime.

###### Procedure for initial import

1. In the "Devices" tab of the project navigation, expand the "Common data" folder > "Collaboration devices".
2. Open the "Collaboration Devices" editor.
3. Click the import icon ![Procedure for initial import](images/129951734027_DV_resource.Stream@PNG-de-DE.png).

   A new window opens.
4. Select the xml file you want to import.
5. Confirm all dialogs.

   The "Import completed" dialog box appears.

   The HMI device whose screen references you have imported now appears in the list.

   ![Procedure for initial import](images/158253655691_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for initial import](images/158253655691_DV_resource.Stream@PNG-en-US.png)
6. Expand the list of the newly imported HMI device to see the screens.

> **Note**
>
> Only screen references from a single device can be imported with each import process. If you want to import the screen references of another device, repeat the procedure.

###### Procedure for repeated import

If you want to once again import screen references that have already been imported, the procedure is the same as for the initial import. The following collaboration settings must not differ from the previously imported device and must be unique across the system:

- Collaboration name
- System ID
- IP address / Host name

If a value is used more than once, the data import cannot be performed. The import is aborted with an error message in this case.

The previous data is overwritten by the successful import.

###### Deleting a collaboration device

To delete imported Unified devices from the list, click ![Deleting a collaboration device](images/129956649227_DV_resource.Stream@PNG-de-DE.png) or use the "Delete" command on the shortcut menu. Individual screen references cannot be deleted. Attempting to delete a single screen reference will delete the entire device from the list.

###### Result

You have made the screens of a collaboration device available for Runtime of an HMI device of the project.

> **Note**
>
> The imported screen references of an HMI are visible to all HMI devices of the current project.

##### Configuring screen windows from different projects (RT Unified)

###### Requirement

- Screens are configured for the collaboration devices.
- Export and import of the screen references are completed.
- All Runtime settings are configured and the collaboration devices are connected.
- The users in the participating projects are identical.

  > **Note**
  >
  > **Using the central user administration (UMC)**
  >
  > If you want to use HMI devices in multiple projects for Unified Collaboration, use the central user administration (UMC). This reduces the configuration effort.

###### Procedure

1. Open the screen on the device on which you want to display screens of the collaboration device.
2. Add a screen window to the screen.
3. Open the Inspector window under "Properties > Properties > General > Screen".
4. Click the selection button in the "Static value" column.

   A new dialog opens.
5. Select the collaboration device in the left area of the window.
6. Select the screen to be displayed in the right area of the window.

   ![Procedure](images/158254880011_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158254880011_DV_resource.Stream@PNG-en-US.png)
7. Confirm your selection by clicking on the green check mark.

> **Note**
>
> When you delete a device that is participating in collaboration, the links of its screens to the screen windows of other HMI devices are removed as well.
>
> When the same device is to participate in collaboration again, the screens must be linked once again to the screen windows.

###### Using scripts

Alternatively, you can also configure screen windows via a script:

1. Open the screen on the device on which you want to display screens of the collaboration device.
2. Add a screen window to the screen.
3. Open the Inspector window.
4. Configure a script:

   - For an event
   - For an object property
5. Enter the following line:

   `Screen.Windows("Screen window_1").Screen = "HMI_RT_1::Screen_1";`

   Alternatively, use the snippet "Change Screen in Screen window of current screen".
6. Adapt the name of the screen window, the HMI device and the screen.

   In the example, "Screen window_1" is the screen window of the current device and "HMI_RT_1::Screen_1" is the screen of the device connected via Unified Collaboration.

###### Result

After compiling and downloading, the screen of the connected HMI device is displayed in Runtime in the screen window via Unified Collaboration.

---

**See also**

[Export screen references for Unified Collaboration (RT Unified)](#export-screen-references-for-unified-collaboration-rt-unified)
  
[Restrictions (RT Unified)](#restrictions-rt-unified)

#### Display messages from participating devices (RT Unified)

##### Requirement

Several HMI devices are configured as participating devices for Unified Collaboration.

##### Procedure

1. Configure a screen for one of the devices.
2. Place an alarm control on the screen.
3. Select the "Systems" property for the alarm control.
4. Expand the list box.

   The participating devices are displayed.
5. Enable the devices whose alarms are to be displayed.

   ![Procedure](images/158256586123_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158256586123_DV_resource.Stream@PNG-en-US.png)

   At least one device must be selected.

   Default setting: The local device is selected.

##### Result

In runtime, the alarm control shows the alarms from the selected participating devices.

### Example: Connecting HMI devices from two projects with Unified Collaboration (RT Unified)

This example shows how to access screen objects of a Unified PC and two Unified Comfort Panels using Unified Collaboration across devices and projects.

Screens of the two Unified Comfort Panels should be operable in the Runtime project of the Unified PC. One of the Unified Comfort Panels is created in another project. The screens of the Unified Comfort Panels are displayed in a screen window. You switch the display of the screens in the screen window by clicking on buttons.

#### Preparation

- All devices are located in a network and are uniquely identifiable.
- The Unified Collaboration components are enabled in the Windows Firewall.
- The system times of the individual devices differ by less than 3 minutes.

Create and distribute the required certificates using the Certificate Manager:

1. Open the Certificate Manager on the Unified PC.
2. Create a new root certificate for your plant.
3. Create a "Runtime Collaboration certificate" for each device.
4. Transfer the root certificate and one "RT Collaboration certificate" each to the collaboration devices.

#### Creating projects and adding devices

1. Create two projects: "Project1" and "Project2".
2. Configure a "PC-System_1" Unified PC in "Project1".

   "PC-System_1" is created with the HMI device "HMI_RT_1".
3. Configure a "HMI_2" Unified Comfort Panel in "Project1".
4. Configure a "HMI_3" Unified Comfort Panel in "Project2".
5. Create a "Screen_1" screen for each of the two Unified Comfort Panels.

#### Runtime settings of the "PC-System_1" Unified PC

1. Expand the folder "PC-System_1" in the "Project tree" under "Devices".
2. Expand the folder "HMI_RT_1".
3. Open the "Runtime settings" of the "HMI_RT_1".
4. Switch to the "Collaboration" area.
5. Activate "Enable collaboration".
6. Check and amend the following settings:

   - The "System ID" is 1.
   - "Generate collaboration name automatically" is selected.

     The "Collaboration name" is "HMI_RT_1".

     This setting cannot be changed.
   - Specify IP address or host name.

     The address must correspond to the IPv4 format.

#### Runtime settings of the "HMI_2" Unified Comfort Panel

1. Expand the folder "HMI_2" in the "Project tree" under "Devices".
2. Open the "Runtime settings".
3. Switch to the "Collaboration" area.
4. Activate "Enable collaboration".
5. Check and amend the following settings:

   - The "System ID" is 2.
   - "Generate collaboration name automatically" is selected.

     The "Collaboration name" is "HMI_RT_2".

     This setting cannot be changed.
   - Specify IP address or host name.

     The address must correspond to the IPv4 format.

#### Runtime settings of the "HMI_3" Unified Comfort Panel

1. Open "Project2".
2. Expand the folder "HMI_3" in the "Project tree" under "Devices".
3. Open the "Runtime settings".
4. Switch to the "Collaboration" area.
5. Activate "Enable collaboration".
6. Check and amend the following settings:

   - The "System ID" is 3.
   - "Generate collaboration name automatically" is cleared.

     The "Collaboration name" is "HMI_RT_3".
   - Specify IP address or host name.

     The address must correspond to the IPv4 format.

#### Exporting screen references

To operate the screens of the Unified Comfort Panels in the Runtime of the Unified PC, the screen references of the Unified Comfort Panel "HMI_3" must be exported from "Project2".

Follow these steps:

1. In the project tree, expand the folder of the respective devices in the "Devices" tab.
2. Open the "Collaboration data" editor.
3. Expand the device by clicking on the arrow.

   All available screens are listed.
4. Select the "Screen_1" screen. To do this, put a check mark in the "Export" column of the corresponding screen.
5. Click Export ![Exporting screen references](images/129951785227_DV_resource.Stream@PNG-de-DE.png).

   A new window opens.
6. Enter a name under which the file is to be saved.

   The "Export completed" dialog box appears.

#### Importing screen references

To operate the screens of the Unified Comfort Panels in Runtime of the Unified PC, the screen references of the Unified Comfort Panel "HMI_RT_3" must be imported into "Project1".

To import screen references, follow the steps below:

1. In the "Devices" tab of the project navigation, expand the "Common data" folder > "Collaboration devices".
2. Open the "Collaboration Devices" editor.
3. Click Import ![Importing screen references](images/129951734027_DV_resource.Stream@PNG-de-DE.png).

   A new window opens.
4. Select the xml file you want to import.
5. Confirm all dialogs.

   The "Import completed" dialog box appears.

   The HMI device whose screen references you have imported now appears in the list.
6. Expand the list of the newly imported HMI device to see the screens.

#### Connecting actively to collaboration devices

Once the import of the "HMI_RT_3" collaboration device is complete, the devices must be actively connected in the Runtime settings. Follow these steps:

1. Open the Runtime settings of the "HMI_RT_1" Unified PC.
2. Switch to the "Collaboration" area.
3. Activate the collaboration devices "HMI_RT_2" and "HMI_RT_3" under "Connect actively to".

   The collaboration devices "HMI_RT_2" and "HMI_RT_3" are available for collaboration.

#### Configuring the screen window

In the following, a screen is configured for the Unified PC in which a screen window is inserted. Screens of the two Unified Comfort Panels can be displayed and operated in this screen window.

1. Expand the folder "PC-System_1" in the "Project tree" under "Devices".
2. Expand the folder "HMI_RT_1" and the "Screens" folder.
3. Add a screen.

   The editor of the screen opens.
4. Add a screen window.
5. Select a screen window.
6. Open the Inspector window under "Properties > Properties > General > Screen".
7. Click the selection button in the "Static value" column.

   A new dialog opens.
8. Select "HMI_2 > Screens" in the left area of the window.
9. Select the "Screen_1" screen in the right area of the window.
10. Confirm your selection.

#### Configuring buttons

To configure the buttons for the screen change in the screen window, follow these steps:

1. Open the screen of the "HMI_RT_1" Unified PC in which the screen window is located.
2. Configure a "HMI_2" button.
3. Configure a "HMI_3" button.
4. Select the "HMI_2" button.
5. Open the Inspector window under "Properties > Events".
6. Select the "Click left mouse button" event.

   The function list is displayed.
7. Select the "ChangeScreen" system function.
8. Open the selection window of the "Screen name" parameter.
9. Select "HMI_2 > Screens" in the left area of the window and confirm the selection.

   The "Screen name" parameter contains the value "HMI_RT_2 :: Screen_1".
10. Specify the type of "Screen window" for the "Screen window path" parameter.
11. Open the selection menu and select the screen window.
12. Select the "HMI_3" button.
13. Open the Inspector window under "Properties > Events".
14. Select the "Click left mouse button" event.

    The function list is displayed.
15. Select the "ChangeScreen" system function.
16. Open the selection window of the "Screen name" parameter.
17. Select "HMI_3 > Screens" in the left area of the window and confirm the selection.

    The "Screen name" parameter contains the value "HMI_RT_3 :: Screen_1".
18. Specify the type of "Screen window" for the "Screen window path" parameter.
19. Open the selection menu and select the screen window.

#### Starting Runtime

1. Compile and download all HMI devices.
2. Open Unified PC Runtime.

#### Result

- In Runtime, the screen of the "HMI_2" Unified Comfort Panel is initially displayed in the screen window.
- When you click the "HMI_2" button, the screen of the Unified Comfort Panel "HMI_2" is displayed in the screen window.
- When you click the "HMI_3" button, the screen of the Unified Comfort Panel "HMI_3" is displayed in the screen window.

---

**See also**

[Defining collaboration settings (RT Unified)](#defining-collaboration-settings-rt-unified)
  
[Export screen references for Unified Collaboration (RT Unified)](#export-screen-references-for-unified-collaboration-rt-unified)
  
[Import screen references for Unified Collaboration (RT Unified)](#import-screen-references-for-unified-collaboration-rt-unified)
  
[Configuring screen windows from different projects (RT Unified)](#configuring-screen-windows-from-different-projects-rt-unified-1)
  
[Creating certificates (RT Unified)](#creating-certificates-rt-unified)
  
[Distributing and installing certificates (RT Unified)](#distributing-and-installing-certificates-rt-unified)

## Web Client (RT Unified)

This section contains information on the following topics:

- [Web client basics (RT Unified)](#web-client-basics-rt-unified)
- [Mode of operation of the web client (RT Unified)](#mode-of-operation-of-the-web-client-rt-unified)
- [Activate web client for Unified Comfort Panel (RT Unified)](#activate-web-client-for-unified-comfort-panel-rt-unified)
- [Using the web client (RT Unified)](#using-the-web-client-rt-unified)
- [Installing a certificate in the browser when accessing via web client (Unified PC) (RT Unified)](#installing-a-certificate-in-the-browser-when-accessing-via-web-client-unified-pc-rt-unified)
- [Installing a certificate in the browser when accessing via web client (UCP) (RT Unified)](#installing-a-certificate-in-the-browser-when-accessing-via-web-client-ucp-rt-unified)
- [SwacLogin: Errors after complete download (RT Unified)](#swaclogin-errors-after-complete-download-rt-unified)
- [Logging out user (RT Unified)](#logging-out-user-rt-unified)

### Web client basics (RT Unified)

By using the web client you can access the runtime of a Unified PC or Unified Comfort Panel in the network from any device. The accessing device can be a PC or a smartphone, for example.

#### Access to the web client

By default, you use the web client for local access to your Unified PC runtime.

For Unified Comfort Panel, you must activate the web client in the TIA Portal in the Runtime settings of the Unified Comfort Panel. Alternatively, you can manage the web client directly in the Control Panel of the Unified Comfort Panel.

When you access a Unified PC or a Unified Comfort Panel for the first time, you load a certificate to enable a secure connection. Afterwards, you operate the runtime as always.

Each web client is autonomous and independent of the runtime displayed locally on the HMI device. We are distinguishing here between synchronous and asynchronous functions.

You can access a runtime simultaneously from multiple web clients.

> **Note**
>
> **Use the latest web browser version**
>
> Use the latest version of your web browser to access the web client.

#### License

For remote access to a WinCC Unified Runtime with web client, you need a license depending on the HMI device used, the number and the type of accesses.

---

**See also**

[Opening local user management in the "Browser" screen object (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#opening-local-user-management-in-the-browser-screen-object-rt-unified)

### Mode of operation of the web client (RT Unified)

Each web client is autonomous and partially independent of other web clients and the runtime displayed locally on the HMI device. For the runtime to run without errors and expediently, we distinguish between asynchronous and synchronous functions. Some functions are not supported at all or only partially supported in the web client.

All languages configured for the runtime project are supported in the web client.

#### Synchronous functions

When synchronous functions are executed, the change is applied to the local runtime and in the runtime of other web clients.

Synchronous functions are all changes that change process data and project-related properties, such as:

- Change tag values
- Acknowledging alarms
- Changing log entries

> **Note**
>
> **Changes of properties at screen objects**
>
> Properties of screen objects that were changed through a user action are not applied to the local Runtime and other web clients.
>
> Example: Color, height and width of screen objects

#### Asynchronous functions

Asynchronous functions are executed independent of the local runtime and other web clients.

Asynchronous functions are mainly customizable display settings, such as:

- Change screen
- Change language
- Zoom
- Filter
- Display in screen windows

#### Scripts and system functions

Scripts and system functions are mainly executed on the HMI device on which the runtime is running.

A few system functions are executed on the device on which the web client is run, such as:

- "ExportParameterSets"
- "ImportParameterSets"

#### System functions under "HMIRuntime.Device.SysFct"

The following system functions under "HMIRuntime.Device.SysFct" are partially supported:

- "SetDHCPState":

  The "mode" parameter can be changed.
- "SetNetworkInterfaceState":

  The "adapterName" parameter can be changed.

The following device-dependent system functions under "HMIRuntime.Device.SysFct" are executed on the HMI device that is accessed via the web client. The effect of these system functions is not visible via the web client.

- "EjectStorageMedium"
- "StopRuntime"
- "ShowControlPanel"
- "ShowSoftwareVersion"
- "StartProgram"

#### Web client on the Unified Comfort Panel

If you want to access another HMI device from the Unified Comfort Panel using the web client, use the "Browser" control.

#### Option to changer user

If you use runtime locally on the Unified Comfort Panel, you will be shown an option to switch the user if you do not have sufficient functional rights. This option does not apply to access via a web client. In this case, a note about insufficient authorizations is displayed in the web client.

### Activate web client for Unified Comfort Panel (RT Unified)

#### Requirement

- A project has been created.
- A Unified Comfort Panel has been configured.

#### Enabling the web client in the TIA Portal

1. Open the runtime settings of the Unified Comfort Panel.
2. Expand the "Remote access".
3. Select "Web Client".
4. Enable the "Enable web access to runtime" option.

   A note about licensing is displayed.

#### Enabling the web client in the Control Panel

1. Open the Control Panel of the Unified Comfort Panel.
2. Select "Runtime properties > Web client".
3. Select "Enable web access to runtime".

### Using the web client (RT Unified)

#### Requirement

- The web client is enabled when a Unified Comfort Panel is used.
- The project has been compiled without errors and loaded.
- The project runs in runtime.

#### Procedure

To access the runtime of a different HMI device using the web client, follow these steps:

1. In the web browser, specify the IP address or the fully qualified name (name and domain) of the HMI device running runtime.

   If you want to access the runtime of a Unified Comfort Panel, use the IP address, for example "https://141.73.65.245/".

   If you are using a browser that runs directly on the HMI device, you can also use "localhost" instead of the IP address.

   To access the Runtime project directly, use "https://<ip>/device/WebRH", note the use of lowercase/uppercase letters, and use the IP address of the HMI device instead of the placeholder "<ip>".
2. If you access the runtime of the HMI device from this device for the first time and there is no corresponding certificate, you will receive a security warning. Follow these steps:

   - Continue loading the web page.
   - Select "Certificate Authority" or the symbol or the message "Not secure" in the address line of the browser.

     The certificate is downloaded.
   - Install the certificate in the web browser.
   - Reload the page.

   The WinCC Unified home page is displayed.

   After complete download of a project, an error can occur when you open the WinCC Unified home page (SwacLogin).

   You can find additional information at [SwacLogin: Errors after complete download](#swaclogin-errors-after-complete-download-rt-unified).
3. Select "WinCC Unified RT".

   The user login appears.
4. Enter the user name and password and select "Log in".

**Note**

If you reset the time on the web client after installing the certificate so that it is before the time the certificate was created, the certificate is invalid. Install a valid certificate.

**Note**

If you experience display problems in the web client, completely delete the browser data (history, form entries, etc.).

#### Result

The runtime of the remote HMI device is displayed.

The Runtime project is displayed in the language that is set in the "User login" dialog. If this language is not configured in the Runtime settings of the HMI device, the language that has the lowest number in the "Order" column under "Runtime settings > Language & font" in the TIA Portal is used.

Depending on the access authorization, you the option to monitor and operate the runtime.

---

**See also**

[Installing a certificate in the browser when accessing via web client (Unified PC) (RT Unified)](#installing-a-certificate-in-the-browser-when-accessing-via-web-client-unified-pc-rt-unified)
  
[Installing a certificate in the browser when accessing via web client (UCP) (RT Unified)](#installing-a-certificate-in-the-browser-when-accessing-via-web-client-ucp-rt-unified)

### Installing a certificate in the browser when accessing via web client (Unified PC) (RT Unified)

#### Using root certificates

To enable web browsers to establish a secure connection to WinCC Unified, the current root certificate of the WinCC Runtime must be known in the web browser as a trusted certification authority.

By installing the web server certificate on the PC device, the public root certificate is made available as a download for installation in web browsers on the WinCC Unified home page.

The procedure for installing the root certificate differs depending on your web browser.

#### Use of self-signed certificates

As an alternative to the root certificate, you can use a self-signed certificate.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security risk from self-signed certificate**  A self-signed certificate is not issued by a trusted certification authority.   If you use a self-signed certificate from an untrustworthy source, the data transfer is not protected from attacks.   Before using self-signed certificates, check the source.   Depending on the firewall and network settings, the use of self-signed certificates may be prohibited. |  |

The installation of self-signed certificates is not supported by all web browsers. Depending on the web browser, it is possible to define exceptions.

For more detailed information, refer to the operating instructions of the web browser.

#### Installing the root certificate for Chrome and Microsoft Edge

Chrome and Microsoft Edge use the Windows system certificate store.

- On devices **with WinCC Unified installation** that have been configured with the Certificate Manager, these web browsers can immediately establish a secure connection to the WinCC Unified web pages because the root certificate has already been installed in the system certificate store.
- On devices **without WinCC Unified Installation** the root certificate must be installed manually.

To install manually, follow these steps (for example, Microsoft Edge):

1. Open the WinCC Unified home page via the URL https://<host name>

   At first, an error message appears:

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129763286923_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129763286923_DV_resource.Stream@PNG-de-DE.png)
2. Open the field with the error details and confirm that you want to open the web page.
3. On the WinCC Unified home page, select the field "Certificate Authority" and confirm "Open file" in the download dialog.

   The root certificate is downloaded to the pre-selected download directory.
4. Open the downloaded file.

   The root certificate is opened with the Windows standard form.

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
5. To import the root certificate into Windows, select "Install Certificate".
6. In the certificate import wizard, select "Local Machine" as the storage location, "Trusted Root Certification Authority" as the certificate store and start the import process.

#### Installing the root certificate for Firefox

Firefox uses its own certificate store and must therefore be configured manually on each device once:

1. Open the WinCC Unified home page via the URL https://<host name>

   At first, an error message appears:
2. Open the field "Advanced" and confirm the field "Accept the Risk and Continue".

   An exception is entered for this page in the Firefox certificate management.
3. On the WinCC Unified home page, select the field "Certificate Authority".
4. Save the root certificate. To do this, click "Save file" in the Firefox dialog that follows.
5. Store the certificate in the Firefox certificate store. Proceed as follows:

   - Open the "Settings" page of Firefox.
   - Select "Privacy & Security". There you will find the "Certificates" area further down. Open "Show certificates...".
   - In the "Certificate Management" window, select the "Certification authorities" tab:

     ![Installing the root certificate for Firefox](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Installing the root certificate for Firefox](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate you saved in step 3.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.
   - Click "Server" and remove the exception that was created by step 2.

#### Installing the root certificate on iOS devices

iOS uses its own certificate store and must therefore be configured manually on each device once. An error message also appears when the WinCC Unified home page is opened.

1. Open the field "Advanced" and confirm the field "Accept the Risk and Continue".
2. On the WinCC Unified home page, select the field "Certificate Authority".

   ![Installing the root certificate on iOS devices](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
3. Select "Install".

   ![Installing the root certificate on iOS devices](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
4. Select "Install" again.

   ![Installing the root certificate on iOS devices](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   You see the entry "Trusted".

   ![Installing the root certificate on iOS devices](images/129772977419_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772977419_DV_resource.Stream@PNG-de-DE.png)
5. Select "General > Info > Certificate Trust Settings".

   ![Installing the root certificate on iOS devices](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
6. Activate "WinCC Unified CA" and select "Next".

   ![Installing the root certificate on iOS devices](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Using the web client (RT Unified)](#using-the-web-client-rt-unified)

### Installing a certificate in the browser when accessing via web client (UCP) (RT Unified)

#### Using the web server certificates

To enable web browsers to establish a secure connection to the Runtime of the Unified Comfort Panel, the certificate in the web browser must be known as trusted.

The procedure for installing the certificate differs depending on your web browser.

#### Use of self-signed certificates

When accessing the Unified Comfort Panel via web client, a self-signed certificate is used.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security risk from self-signed certificate**  A self-signed certificate is not issued by a trusted certification authority.   If you use a self-signed certificate from an untrustworthy source, the data transfer is not protected from attacks.   Before using self-signed certificates, check the source.   Depending on the firewall and network settings, the use of self-signed certificates may be prohibited. |  |

The installation of self-signed certificates is not supported by all web browsers. Depending on the web browser, it is possible to define exceptions.

For more detailed information, refer to the operating instructions of the web browser.

---

**See also**

[Using the web client (RT Unified)](#using-the-web-client-rt-unified)

### SwacLogin: Errors after complete download (RT Unified)

After complete download of a project to a Unified PC, an error can occur when you open the WinCC Unified home page. The error can occur regardless of whether you open the home page locally on the PC or from a different device.

A possible cause of the error is the deletion of the browser cache.

#### Error description

In "Chrome" and "MS Edge", the error is displayed with the following alarm:

![Error description](images/142866988171_DV_resource.Stream@PNG-en-US.png)

In "Firefox", the error is displayed with the following alarm:

![Error description](images/142866998283_DV_resource.Stream@PNG-en-US.png)

After accepting the warning of a potential security risk, the page remains empty in Firefox. Only the background screen is visible.

#### Remedy the error in "Chrome" and "MS Edge"

To remedy the error in "Chrome" and "MS Edge", follow these steps:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server in the address line of the browser. The URL is the same as the one in the error message without "/swaclogin", for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. The page with a warning regarding the secure connection is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/142879731595_DV_resource.Stream@PNG-en-US.png)
4. Accept the warning by clicking on "Proceed to uadtbf-01.asrd-lab.net (unsafe)".
5. The home page with the "User login" dialog is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/142879972107_DV_resource.Stream@PNG-en-US.png)

#### Remedy the error in "Firefox"

To remedy the error in "Firefox", follow these steps:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server (ring server) in the address line of the browser, for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. A blank page opens. Close the page.
4. Refresh the home page with the function key <F5>. The home page with the "User login" dialog is displayed.

---

**See also**

[Using the web client (RT Unified)](#using-the-web-client-rt-unified)

### Logging out user (RT Unified)

If you want to end your Runtime session, you have the following options to log out completely:

- Use the "Logout" system function.
- Log out in the user management.
- Close all instances, i.e. open windows, of the browser in use.

#### Requirement

- You are logged in to Runtime.
- When you want to log out in the Runtime project, the system function "Logout" is configured, for example, to the event "Click left mouse button".

#### Logging out in the Runtime project with the system function "Logout"

- Select the button at which the system function "Logout" is configured.

#### Logging out in the user management

- Select "Logout" from the menu.

  Your session is ended.

  ![Logging out in the user management](images/142349702027_DV_resource.Stream@PNG-de-DE.png)

  New data downloaded from the TIA Portal is applied during the next login.

## WinCC Smart Server (RT Unified)

This section contains information on the following topics:

- [General](#general)
- [Application scenarios](#application-scenarios)
- [Security concept for the Smart Server (RT Unified)](#security-concept-for-the-smart-server-rt-unified)
- [Settings in the TIA Portal](#settings-in-the-tia-portal)
- [Settings in the Control Panel of the Smart Server (RT Unified)](#settings-in-the-control-panel-of-the-smart-server-rt-unified)
- [Configuring the Smart Client application (RT Unified)](#configuring-the-smart-client-application-rt-unified)
- [Remote control by means of the Smart Client application (RT Unified)](#remote-control-by-means-of-the-smart-client-application-rt-unified)
- [Use and limitations of the Smart Server](#use-and-limitations-of-the-smart-server)

### General

#### Introduction

With WinCC Smart Server, you can communicate between and with HMI systems via TCP/IP connections (e.g. LAN).

You can use the Smart Server in combination with SIMATIC Unified Comfort Panels.

#### Use of the SmartServer

You use Smart Server in the following application scenarios:

- Distributed HMI devices with Smart Client applications for controlling large machines or machines that are spread out over a large area.
- Remote control of an HMI device via the Internet or Intranet

User benefits:

- Flexible solution for access to HMI devices from any location
- Reduction of load on the field bus:

  For example, Unified Runtime and Unified Comfort Panels provide a control system with access to process data. No load is placed by the factory level on the sensitive field level with respect to the necessary communication requirements. These requirements are handled by Unified Runtime as well as with the Unified Comfort Panels.
- Expensive on-site service visits to be avoided by using the remote control. Unplanned non-operation periods are reduced and the system productivity is increased.

### Application scenarios

#### Remote diagnostics

A factory has a service contract with an external service company. The Unified Comfort Panel and the service technician's PC are linked together over a TCP/IP-ready network. The service technician accesses the Unified Comfort Panel via the Internet and executes remote diagnostics.

![Remote diagnostics](images/146594871051_DV_resource.Stream@PNG-en-US.png)

#### Application example

Among other things, flow rates are measured in the process control of a cooling unit. Contamination in a feed line reduces the flow of coolant. When the flow rate drops below the configured threshold value, the Unified Comfort Panel displays a warning.

The service technician then establishes a connection with the remote Unified Comfort Panel and takes the appropriate actions.

Advantage: The downtime is reduced to a minimum by remote maintenance.

#### Distributed HMI devices

Distributed devices, so-called Smart Clients, are used for controlling large machines or machines that are spread out over a large area.

The Smart Client establishes the connection to the Smart Server via the Smart Client application.

The operator can control and monitor the system with the Smart Client application and the Unified Comfort Panel. The operator sees the same screen with each Smart Client application and on the Unified Comfort Panel.

### Security concept for the Smart Server (RT Unified)

Remote monitoring and remote control of the Smart Server is protected by two functions:

- Encryption of communication with the Smart Server
- Passwords

#### Passwords for the Smart Server

Remote monitoring and remote control of the Smart Server is password protected. You create a password for each of two users.

- A password consists of exactly 8 characters.
- It contains at least one number (0-9)
- It contains at least one lowercase letter (a-z)
- It contains at least one uppercase letter (A-Z)
- It contains at least one of the following characters:

  !$%&()*+,-./:;<=>?@[\]_{|}~^
- Passwords cannot be entered using copy & paste.
- The passwords for User1 and User2 cannot be identical.
- Passwords must not be empty.

> **Note**
>
> **Passwords for the Smart Server**
>
> No passwords have been preset.
>
> You cannot use Smart Server if both passwords are not assigned.

#### Encrypt communication to the Smart Server

The option "Secure communication via self-signed certificates" enables an encrypted connection between Smart Client and Smart Server. When establishing the communication, the Smart Server sends a self-signed certificate to the Smart Client. The certificate must be accepted by the Smart Client.

Connections on Smart Client to Smart Server are then only possible on the basis of the exchanged certificate.

### Settings in the TIA Portal

#### Introduction

In the "Runtime settings" editor, you configure the requirements for using the Smart Server.

As an alternative, configure the settings in the Control Panel of the Unified Comfort Panel.

Note that the settings on the Unified Comfort Panel are overwritten when a project is downloaded from the TIA Portal.

#### Requirement

- A project is open in the TIA Portal.
- A Unified Comfort Panel has been created.

#### Procedure

To configure the Smart Server, follow these steps:

1. Open the "Runtime settings" of the Unified Control Panels in the project tree.
2. In the "Runtime settings", expand the "Remote access" menu command.
3. Click "Smart Server".
4. Enable the "Enable Smart Server" setting in the "Smart Server Configuration" group.
5. Assign a password for "User1" and "User2" respectively.

   Note the [Rules for passwords](#security-concept-for-the-smart-server-rt-unified).
6. Activate "Secure communications via self-signed certificates".

   > **Note**
   >
   > If "Secure communication using self-signed certificates" is not enabled, the communication is not encrypted.
7. If you do not want to use automatic port configuration, disable the option and assign a port manually.
8. Compile and download the project onto the Unified Comfort Panel.

![Procedure](images/143083768715_DV_resource.Stream@PNG-en-US.PNG)

### Settings in the Control Panel of the Smart Server (RT Unified)

The settings on the Control Panel of the Unified Comfort Panel regulate which remote operator is permitted to access the Smart Server application.

The options in the Control Panel are analogous to the runtime settings in the TIA Portal.

Note that the settings on the Unified Comfort Panel are overwritten when a project is downloaded from the TIA Portal.

#### Procedure

To configure the Smart Server in the Control Panel of the Unified Comfort Panel, follow these steps:

1. In the Control Panel of the Unified Control Panel, open the menu item "Network and Internet".
2. In the area "Remote access > Smart Server" enable the setting "Enable Smart Server".
3. Select one or more users for remote access.
4. Assign a password for each user.

   Note the [Rules for passwords](#security-concept-for-the-smart-server-rt-unified).
5. Activate "Secure communication via self-signed certificate".
6. If you do not want to use automatic port configuration, disable the option and assign a port manually.

**Note**

If "Secure communication via self-signed certificate" is not enabled, the communication is not encrypted.

### Configuring the Smart Client application (RT Unified)

This section contains information on the following topics:

- [Dialog "New SmartServer: Connection"](#dialog-new-smartserver-connection)
- ["Options" dialog, "Connections" tab](#options-dialog-connections-tab)
- ["Options" dialog, "Globals" tab](#options-dialog-globals-tab)

#### Dialog "New SmartServer: Connection"

This dialog opens when you click the "SmartClient" button in the taskbar.

It is used to set the desired Smart Server and to select the connection method.

The following configuration options are available to you:

**SmartServer**

Enter the address of the server to which the connection is to be established. You can find the various options for entering the address under [Remote control by means of the Smart Client application](#remote-control-by-means-of-the-smart-client-application-rt-unified) .

**Connection profil**

Select the type of connection to the Smart Server according to the network you are using.

**Options**

Opens the "Smart Client Options" dialog box with the technical settings for the Smart Client application.

#### "Options" dialog, "Connections" tab

The settings for the Smart Client application are specified in this dialog.

The following configuration options are available to you:

**Format and encodings**

Settings for compressing the screen data of the Smart Server.

- Use encoding

  Preassigned based on the selection under "Connection profile".

  Select the desired compression or "Raw" (no compression).
- Use 8-bit color

  Reduces the color depth at the client to 8 bits (256 colors). The data are then transferred faster. However, incorrect colors may result.
- Custom Compression level

  Allows individual customizing of the compression level in the "Level" input field:

  1 = least compression (faster); 9 = maximum compression (slower).
- Allow JPEG compression

  Allows the use of JPEG compression (involves losses).

  Enter the "Screen quality" in the input field underneath:   
  1 = least compression (faster); 9 = maximum compression (slower).
- Allow CopyRect encoding

  Allows compression while using "similar rectangles".

**Restrictions**

- View only (inputs ingnored)

  Sets the view mode for this Smart Client irrespective of the settings on the Smart Server. This allows you to prevent unintended control operations.
- Disable clipboard transfer

  Turns off the clipboard.

  Applies only to the copying and pasting of texts.

**Display**

Settings for the screen display

- Scale by

  Zooms in or zooms out the desktop to be displayed.
- Full-screen Mode

  Displays the desktop to be shown in full-screen mode. If the display on the Smart Server is larger than the screen of the Smart Client, it is scrolled automatically by the mouse movement.

**Mouse**

Settings for the evaluation of mouse actions

- Emulate 3 Buttons (with 2-button click)

  Emulation of a three-button mouse by a two-button mouse.
- Swap mouse buttons 2 and 3

  Mouse buttons 2 and 3 are swapped.

**Mouse cursor**

Settings for the display of the cursor

Select the type of transfer of the mouse actions:

- Track remote cursor locally

  The information on the location of the cursor is transferred separately from the screen information. This speeds up the transfer of the cursor.
- Let remote server deal with mouse cursor

  Moves the Smart Server mouse pointer to the Smart Client mouse pointer. This allows more accurate cursor positioning.
- Don't show remote cursor

  The cursor at the Smart Server is not included in the transfer.

#### "Options" dialog, "Globals" tab

Technical settings for the Smart Client application are made in this dialog.

The following configuration options are available to you:

**Interface options**

- Show toolbars by default

  Shows the toolbar.
- Warn at switching to the full-screen mode

  Outputs a message before the full-screen mode is activated.
- Number of connections to remember

  The Smart Client creates a list of the recently used connections. This setting specifies the number of connections listed.
- Clear the list of saved connections

  The list is cleared.

**Local cursor shape**

Specifies the appearance of the local cursor. This makes it easier to differentiate between the local mouse pointer and the remote mouse pointer.

**Logging**

- Write log to a file

  Writes information to the logbook of the Smart Client application.
- Verbosity level

### Remote control by means of the Smart Client application  (RT Unified)

#### Introduction

On the Smart Client, the Smart Client application provides the connection to the remote Unified Comfort Panel.

#### Requirement

- Both devices are connected with via a TCP/IP capable network.
- In the TIA Portal project of the Smart Server or in the Unified Comfort Panel, the setting "Enable Smart Server" is selected in the runtime settings under "Remote access > Smart Server".

  Note that the settings on the Unified Comfort Panel are overwritten when a project is downloaded from the TIA Portal.

#### Sequence

Remote monitoring or remote control is supported on the Smart Server.

Remote monitoring or remote control can be implemented on the Smart Client using the Smart Client application.

Remote control via the Smart Client application works as follows:

- Start the Smart Client application
- Establish connection
- Password input
- Operator control and monitoring on the Unified Comfort Panel

#### Install SmartClient application

The SmartClient application is executed via the "SmartClient.exe" file.

- If WinCC Runtime is installed on the SmartClient, the SmartClient application is also installed.
- If WinCC Runtime is not installed on the SmartClient, you have several options:

  - You copy the SmartClient application from the WinCC Runtime product DVD.
  - You copy the SmartClient application from the installation path from another PC.

#### Start the Smart Client application

- To connect to the remote Unified Comfort Panel, call the Smart Client application and enter the IP address of the Smart Server.

  - IP address or server name:port number

    - or -
  - IP address or server name:display number

  Example: "192.168.0.1::5800"

Other options to start the Smart Client application:

- Enter the name of the executable file and the IP address in the command line:  
  `smartclient.exe 192.168.0.1`.

  The Logon dialog box appears.

  - or -
- Enter the name of the executable file, the IP address and the password in the command line:  
  `smartclient.exe 192.168.0.1 /password <Password>`.

#### Password input

- Password input at the Smart Server

  Instead of the on-screen keyboard, the following message is displayed on the Smart Client when you enter the password directly at the Smart Server: "Remote access by Smart Options is in Progress. Please wait until the input of values has been ended." This measure prevents keyboard input for entering the password from being displayed on the Smart Client.
- Password input at the Smart Client

  The display of the screen keyboard on the Smart Server by actions on the Smart Client is suppressed. Use the local on-screen keyboard for entries at the Smart Client. The local on-screen keyboard on the Smart Client is automatically displayed. Close the on-screen keyboard manually. Select "Input > Hide Input Panel" to hide the local on-screen keyboard.

  > **Note**
  >
  > The entries with full-screen keyboard are not protected on devices with a screen size of ≤ 6''.
  >
  > Entries in Control Panel Applets which do not use the full-screen keyboard are protected.

  > **Note**
  >
  > Hidden password input is not supported by the on-screen keyboards of third-party products.

  > **Note**
  >
  > It is not possible to enter special characters in combination with [AltGr].

#### Operation with the keyboard

For operator control via the keyboard, the following is available:

| Keyboard shortcut | Function |
| --- | --- |
| <Alt+Ctrl+SHIFT+O> | Opens the "SmartClient options" dialog. |
| <Alt+Ctrl+SHIFT+F> | Switches over to full screen mode |
| <Alt+Ctrl+SHIFT+R> | Updates the display |
| <Alt+Ctrl+SHIFT+N> | Opens the "New SmartServer Connection" dialog |
| <Alt+Ctrl+SHIFT+S> | Save as |
| <Alt+Ctrl+SHIFT+T> | Displays and hides the toolbar |

#### Result

The entire layout of the remote Unified Comfort Panel is shown in the application window. Depending on the configuration, you can specify monitoring only or operator control of all keys with the mouse.

### Use and limitations of the Smart Server

#### Use restrictions

When using the Smart Server, observe the following notes:

- Smart Server and Smart Client

  - Use only simple projects.
  - Avoid photographs and color gradients in screens.
  - Avoid heavy background loads during operation, for example, those from user-defined functions or logs.
  - A maximum of 3 parallel connections to Smart Clients are supported. Additional connections are not prevented, but lead to a reduction in performance.
  - To improve the performance of the Smart Server, you can disable the hardware acceleration of the graphics card.
  - For client access of a PC with touch screen to a SmartServer, the following applies to the touch operation of the SmartClient:

    Standard touch operation such as clicking or scrolling in lists is possible, but touch gestures and events such as "Press" and "Release" are not supported.
  - If you access a Unified Comfort Panel via the Smart Client, this leads to reduced performance on the HMI device.
- Access protection

  To protect access to an Unified Comfort Panel using different passwords, use the first password for protected access and the second password for unprotected access; for example, remote control with password and remote monitoring without password.

  Passwords must be assigned. It is not permitted to leave passwords blank.
- Port

  The connection to the web server is established via port 443 (HTTPS over SSL / TLS) or via port 80 (HTTP, unencrypted). For the web server to start without problems, make sure that port is not in use by any other application, such as the IIS World Wide Web Publishing Service.
- Timeout

  If the connection between the Smart Server and a Smart Client is interrupted, the server will register this disconnection only with a certain delay. The delay is based on the Windows standard configuration of TCP/IP Timeout.

#### Use-requirements in the company network

If the company network is protected by a Firewall, the system administrator must enable the corresponding port:

- The Smart Server is connected to the network via port 5900.

You change the port number in the Runtime settings under "Remote access > Smart Server" in the settings for "Communication" or in the same way on the Comfort Panel.
