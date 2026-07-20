---
title: "WinCC Unified"
package: ReadMeWCCUenUS
topics: 23
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Unified

This section contains information on the following topics:

- [Security Information](#security-information)
- [Breaking changes](#breaking-changes)
- [Notes on use](#notes-on-use)
- [Screens and screen objects](#screens-and-screen-objects)
- [Simple object "Text"](#simple-object-text)
- [Alarms and alarm view](#alarms-and-alarm-view)
- ["Smoothing" property for logging tags](#smoothing-property-for-logging-tags)
- [System functions and scripts](#system-functions-and-scripts)
- [Parameter sets and parameter set display](#parameter-sets-and-parameter-set-display)
- [WinCC Unified PC](#wincc-unified-pc)
- [Notes on the operation of Unified Panel](#notes-on-the-operation-of-unified-panel)
- [Remote access to a Unified device](#remote-access-to-a-unified-device-1)
- [Working with plant objects and plant views](#working-with-plant-objects-and-plant-views)
- [Audit](#audit)
- [View of Things](#view-of-things)

## Security Information

### Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines, and networks.

In order to protect plants, systems, machines, and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions only form one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary, and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For more information on protective industrial cybersecurity measures for implementation, visit:

[https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html)

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends applying product updates as soon as they are available and always using only the latest product versions. Use of product versions that are no longer supported, and failure to apply latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates at all times, subscribe to the Siemens Industrial Cybersecurity RSS Feed under.

[https://new.siemens.com/global/en/products/services/cert.html](https://new.siemens.com/global/en/products/services/cert.html)

### Network settings

The following table shows the network ports that are used by WinCC Unified for internal and external communication. These ports must not be used for any other purpose.

The setup configures the firewall to ensure smooth operation.

| WinCC Unified |  |  |
| --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** |
| ILScs Manager | 20008 | TCP |
| UMC | 20009 | TCP |
| ILPmon Manager | 4999 | TCP |
| ILEvent Manager | 1235 | TCP |
| ILDist Manager | 4777 | TCP |
| ILDataManager | 1234  5001 | TCP |
| Node Processes | 3103  443  8888 | TCP |
| Graphics Runtime | 1339  1345 | TCP |
| License server | 1366 | TCP |
| Screen debugger | 9222 | TCP |
| Job debugger | 9224 | TCP |
| WCCIL Proxy Manager | 5678 | TCP |
| Network Discovery (IS) | 137 | TCP |
| UMC AttachAgent | 4002 | TCP |
| OPC UA Discovery | 4840 | TCP |
| RFID | 5003 | TCP |
| GraphQL | 4000 | TCP |

| Unified Comfort Panel |  |  |
| --- | --- | --- |
| Name | Port number | Transport protocol |
| HmiRuntime | 1234 | TCP |
| HmiRuntime | 1235 | TCP |
| HmiRuntime | 1344 | TCP |
| HmiRuntime | 4700 | TCP |
| HmiRuntime | 4701 | TCP |
| HmiRuntime | 4776 | TCP |
| HmiRuntime | 4777 | TCP |
| HmiRuntime | 4778 | TCP |
| HmiRuntime | 4999 | TCP |
| HmiRuntime | 5678 | TCP |
| Snmpd | 162 | TCP |
| FwPnManager | 34964 | UDP |

> **Note**
>
> **Block HTTP port**
>
> For security reasons, it is recommended that Port 80 be disabled on the IIS server.
>
> 1. Start "Internet Information Services (IIS) Manager" on the Unified PC.
> 2. Right-click "Default Web Site".
> 3. Select "Remove" or "Manage Website &gt; Stop".

## Breaking changes

### PI options in ODK

ODK does not support any PI options in V19.

### Scrolling behavior for pop-ups

If you move the visible screen section of a process screen in Runtime and a pop-up window is visible there, for example a faceplate container, Runtime behaves as follows:

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | The pop-up window is moved together with the screen section. |
| As of WinCC Unified V18 | The pop-up window is not moved with it. |
| Simulation of an HMI device with installed device version V17 in a WinCC project V18 or higher | The pop-up window is moved together with the screen section. |

### Operation of objects behind a screen window

If a screen window has an empty area and the screen or faceplate displayed in the screen window has the "transparent" setting as the fill pattern for the background, Runtime behaves as follows:

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | Objects that are in the background of the screen window in the empty area of the screen window are visible. The objects cannot be operated by clicking. |
| As of WinCC Unified V18 | The objects can be operated by clicking.  Application example: You use a round menu with a button next to it. To prevent the rectangular border surrounding the menu from obscuring the button, make the menu available in a screen window. |

### Zoom behavior of screen windows on touch devices

Runtime now supports panning and zooming with a two-finger gesture.

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | No panning and zooming with two-finger gestures. |
| As of WinCC Unified V18 | Panning and zooming with two-finger gestures is supported.  Default: Activated   If you want, you can disable this feature by clearing "Format &gt; Allow zoom" property for the screen window. |

### Exclusion of "Uncertain - initial value" quality code as trigger

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | If a tag is used as a trigger for a script and the tag is used in a screen, e.g. by an I/O field, the script is executed twice in quick succession when the screen is loaded:  - When reporting the initial value - When reporting the process value |
| As of WinCC Unified V18 | Default setting: QualityCode 0x4C (Quality status: Uncertain, Substatus: Initial value) is ignored as a tag trigger.   If a tag is used as a trigger for a script and the variable is used in a screen, e.g. by an I/O field, the script is only executed when the process value is reported as the screen is loaded.  To enable the quality code as a trigger, proceed as described below. |

To enable QualityCode 0xC4 as a trigger in V18 or higher, do the following:

1. Open a file browser and navigate to the following folder:

   `C:\Program Files\Siemens\Automation\WinCCUnified\bin\_config`
2. Open the following configuration file:

   - For scripts in screens: `IOWA_GfxComponentConfigurationSrv.xml`
   - For scheduled tasks: `IOWA_SchedComponentConfiguration.xml`
3. Delete the line for &lt;Attribute key&gt;:

   `<ComponentConfiguration componentKey="GfxTriggerManager" name="Trigger Manager">`
     
    `<AttributeList>`
     
    `<Attribute key="IgnoredTagQualities" value="0x4c"/> <!— 0x4c: “Initial Value” quality >`
     
    `</AttributeList>`
     
   `</ComponentConfiguration>`

### Simulation of Runtime

To use the simulation, you must install WinCC Unified Runtime. If no license is found for Runtime, start the simulation in demo mode.

### OPC UA with OpenSSL 3.0

WinCC Unified uses OPC UA OpenSSL 3.0 from V18 Update 3 and higher.

If the OPC UA certificate of an HMI device has been created before V18 Update 3, it becomes incompatible through the device upgrade and has to be recreated. Follow these steps.

IF the HMI device uses a CA-based OPC UA certificate:

1. Upgrade the certificate authority device and the HMI device.
2. Re-create the OPC UA certificate of the HMI device on the certificate authority device with WinCC Unified Certificate Manager.
3. Install the certificate on the HMI device.

   If the communication partner already trusts the root certificate of the certificate authority, it automatically also trusts the newly created OPC UA certificate of the HMI device.

If the HMI device uses a self-signed OPC UA certificate:

1. Delete the certificate from the certificate store before upgrading the HMI device:

   - For Unified PCs:

     The certificate store is located in the folder with the Runtime projects in the subfolder "`certstore`".

     Default: `C:\ProgrammData\SCADAProjects\certstore`​
   - For Unified Panel:

     Select "Control Panel &gt; Security &gt; Certificates" and as the "Certificate store" the entry "My Certificates". Select the certificate and delete it.
2. Upgrade the HMI device.

   For Unified PC: The certificate is automatically generated and installed.
3. For Unified Panel: Start Runtime.

   The certificate is automatically generated and installed.
4. Trust the certificate at the communication partner.

## Notes on use

### Contents

Information that could not be included in the online help and important information about product features.

### Copying between WinCC Unified and other devices

Copying data via the clipboard or via the library, for example is only supported between Unified devices. Copying data between Unified devices and other devices is not supported.

### Secure communication

If you use Inter-Project Engineering (IPE) in your project, i.e. an HMI device is connected to a device proxy PLC, and an error message about inconsistent certificates appears during compiling, you need to correct the certificates of the associated PLC in the original project. Then you have to compile, export and re-import the PLC.

### Changing HMI device names or log paths

If you make the following changes in the engineering system for a project that is already loaded in Runtime, the existing log data is lost when you load the device again:

- You rename the HMI device in the project navigation
- You rename a log folder or change the log path in the Runtime settings

The data from the old log is not available in the new log after reloading.

### Storage location for databases

If the Runtime project folder is configured as the storage location for a database and you change the location of the project folder, this results in data loss.

To avoid data losses select a different storage location for databases than that of the project folder or do not change the project folder.

For more information, refer to the help "SIMATIC Unified PC Installation" under the keyword "Loading projects".

### Access to subnets via TCP/IP Auto

Use the TCP/IP Auto setting on your engineering device (programming device) when you connect the device to a local subnet. (Control Panel &gt; Set PG/PC interface)

The engineering device then allows additional IP addresses from the subnet to be added to its network adapter.

> **Note**
>
> This setting cannot be used if you use a router.

No setting is necessary on the devices belonging to the external network.

For stationary operation, use the TCPI/IP setting.

### Fault in the connection between the server and the client

If there is a fault in the connection between the server and client, check the settings of the PG/PC interface. TCP/IP Auto should not be used for the setting "Interface parameter assignment used". Use fixed IP addresses instead.

### Changes at a PLC user data type

After a change to a PLC user data type, the PLC must be compiled to make this change known to all Unified devices that use this user data type. If compilation of the PLC does not take place, error messages can occur during the compilation of the HMI devices.

### Inter Project Engineering (IPE) in faceplates

Inter Project Engineering is not supported by faceplates. User data types of a device proxy PLC cannot be interconnected with a faceplate.

### Collaboration certificates and Runtime version

Runtime Collaboration requires that the Collaboration certificates of 2 Collaboration partners have been created with a Certificate Authority device whose installed Runtime version is equal to or higher than the installed Runtime version of the Collaboration partner with the higher Runtime version.

This is why upgrading Collaboration devices may require re-creation, distribution, and installation of Collaboration certificates.

Example:

- A Unified PC and a Unified Panel with a V17 Runtime are Collaboration partners.
- You upgrade the Panel to V18.
- On a Certificate Authority device with an Runtime version V18 or higher, create new Collaboration certificates for both HMI devices. Distribute and install them on the devices.

### Starting Runtime

Runtime cannot be started via WinCC Runtime Start if the "Load preview" dialog is displayed in the engineering system.

### Status "Partly running"

If it is not possible to start the simulation or the Unified Runtime, open the Runtime Manager. If the status of the project is displayed as "partly running", check

- whether the user currently logged on in Runtime has sufficient rights. Is the user entered in the following Windows user groups:  
  PLCSimUsers  
  RTIL Tracing Users  
  Siemens TIA Engineer  
  SIMATIC HMI  
  SIMATIC HMI VIEWER
- whether the computer name is not longer than 15 characters.
- whether "OPC UA" is activated in the Runtime settings and a certificate exists.
- whether "Runtime Collaboration" is enabled in the Runtime settings of a Unified Panel and a certificate is available.

### Simulation with S7-PLCSIM

Always start the simulation in WinCC and then S7-PLCSIM.

### WinCC Unified Tag Simulator

The WinCC Unified Tag Simulator is not part of WinCC Unified V18 and higher.

### Dynamic SVG types

If you manually assign a type version to a dynamic SVG type or rename the type, a delta download is no longer possible.

### Encryption with TLS

Always use the most current version of TLS. Disable the older version.

The use of older versions (TLS 1.0 und 1.1) is at your own risk.

### Assigning text lists and graphics lists for reports

It is not possible to read in values from texts lists and graphics lists, neither in the add-in nor when generating the report.

### Page numbering in audit

Because of a problem with the page numbering, the system functions "ReadElectronicRecord" and "ExportElectronicRecordAsCSV" only deliver the first 1000 electronic data records on the provided filter.

### Protecting drives through UWF

If you are using UWF (Unified Write Filter) on a Unified PC, exclude the following folders from UWF:

- Project folder

  Preset project folder: C:\ProgramData\SCADAProjects
- C:\ProgramData\Siemens

In accordance with the UWF implementation of Microsoft, all write accesses are then written directly into these folders, but also into the overlay. If the size of the overlay approaches or exceeds the upper limit, this causes problems when loading projects or in Runtime.

You have the following options:

- Start WinCC Unified Configuration and, in the "Storage location for projects" step, select a folder whose drive is not protected by UWF as the project folder.
- Increase the size of the overlay.
- Change the type of overlay from RAM-based to disk-based.
- Start the Unified PC before reloading a project into the device.

  The overlay is emptied during the restart. This may slow down the restart.

### Communication with LOGO! PLC

For the communication with a LOGO! PLC, select “Standard Modbus TCP/IP” in the connection as the communications driver.

---

**See also**

[SIOS - WinCC manuals](https://support.industry.siemens.com/cs/products?dtp=Manual&mfn=ps&pnid=24212&lc=en-WW)

## Screens and screen objects

### Contents

Information that could not be included in the online help and important information about product features.

### Adaptations to screens and screen objects

The settings that you define under "Settings &gt; Visualization" in the "Resize screen" area have no effect on the HMI devices:

- SIMATIC Unified PC
- SIMATIC Unified Comfort Panel

### Text box

In the Engineering System, in the task card "Tools", the "Text box" object was moved to the "Elements" pallet and is identified by the following icon ![Text box](images/173009190923_DV_resource.Stream@PNG-de-DE.png).

### SVG graphics

SVG graphics and dynamic SVG graphics support the SVG 1.2 Tiny standard. The use of SVG graphics that include the elements or commands according to the SVG 2.0 standard can lead to unexpected behavior.

The file names of SVG graphics must not include German umlauts or Chinese characters.

### Faceplates: Passing interface properties of the "Resource list" data type to pop-ups

When you call pop-up windows outside a faceplate type, you pass the interface properties by script. For interface properties of the "Resource List" data type, text and graphic lists can be passed.

To specify graphic lists, use the prefix "GraphicListCollection", for example, "GraphicListCollection.Graphic_List_1".

To specify text lists, use "@Default" as a prefix, e.g. "@Default.Text_list_1".

### Faceplates: Passing interface properties of the "Multilingual text" data type to pop-ups

When you call pop-up windows outside a faceplate type, you pass the interface properties by script. Interface properties of the "Multilingual text" data type cannot be passed.

In this case, use the interface property of the "configuration string" data type. The configuration string contains the different values of the text in the respective language separated by a semicolon. Use the script to read the active Runtime language and then use the "Case" command to make a case distinction depending on the active Runtime language.

### Faceplates: "Cleared" event

The "Cleared" event occurs when the faceplate is closed. The relevant faceplate container is dissolved.

Therefore, no interface tags or interface properties can be passed on the "Cleared" event.

### Trend view: Bit-triggered trends

Bit-triggered trends are not supported in the control "Trend view".

## Simple object "Text"

### Use

The "Text" object is a closed object used for displaying simple texts and has a limited number of properties. The object is particularly well suited for use on small devices.

You can find the "Text" object in the "Toolbox" task card in the "Simple objects" pallet. The object is marked with the following icon ![Use](images/173008490635_DV_resource.Stream@PNG-de-DE.png).

### Important properties of the "Text" object

The "Text" object facilitates:

- Entering text directly
- Entering multi-line text
- Entering multilingual text
- Dynamizing an object with a text list

## Alarms and alarm view

### Contents

Information that could not be included in the online help and important information about product features.

### Alarms and alarm view

**Controller alarms**

If the connection between HMI device and controller is interrupted, only the last occurring controller message can be sent and displayed after restarting the runtime software. When the connection is re-established, all controller messages are transmitted correctly again.

**Alarm block "Duration"**

Alarm block "Duration" is not supported in V17.

**Text lists**

If you assign a text list, whose entries point to a tag, to an alarm text, the contents of the alarm view are not shown correctly in Runtime. This also applies to nesting, when, for example, a text list points to another text list which in turn points to a tag. The use of parameterized text lists in alarm texts is not recommended.

## "Smoothing" property for logging tags

### Contents

Information that could not be included in the online help and important information about product features.

### Smoothing (Unified Comfort Panel)

The following applies to logging tags and PLC tags: If the value "No smoothing" is set in the Logging tag properties under "Smoothing &gt; Mode", the values are nevertheless smoothed.

**Example:**

A logging tag changes its value as follows: "100" &gt; "101" &gt; "101".

Even if "No smoothing" is set in the properties of the tag, the values [100, 101] are stored in the log.

## System functions and scripts

### Contents

Information that could not be included in the online help and important information about product features.

### JavaScript arguments of specific object events

The following applies to the rectangle, gauge, button and circle objects: If you configure a JavaScript to an event, only the "Item" argument is passed correctly to the script. You can process the event in the script, but not the other arguments.

### "StartProgram" in the Scheduler - Unified Comfort Panel

Calling up a program via the "StartProgram" system function in the Scheduler is not supported by Unified Comfort Panel. Instead, use a "Tag" trigger in the Scheduler to initiate the system function.

### Methods of the "ProDiag" object

With the "OpenTIAPortal" methods of the "ProDiag" object, TIA Portal can be opened from the Runtime. Prerequisite for this is that the "Allow start of external processes via Unified Runtime" setting is activated on the HMI device in SIMATIC Runtime Manager.

The following system functions are reserved for future versions:

- "ResetToConfiguration"
- "OpenPlcCodeViewByFCCall"
- "OpenProDiagDetailsByCall"

With the parameter "screenltemPath" of the " IsJumpableAlarm" method, you transfer the path of the screen object which is activated when the alarm that is selected in the alarm display is a ProDiag alarm – not the path of the code viewer as described in the user help.  
Example: Transfer the path of a button for which a jump into the PLC code display was configured. If the selected alarm is a ProDiag alarm, operators jump to the PLC code display in Runtime by clicking the button.

The system function "OpenViewerGraphByBlock" expects the name of the data block of the GRAPH function block as second parameter.

### ExportParameterSets

The system function "ExportParameterSets" expects as third parameter the path plus file name of the file to which the ParameterSets are exported.

### Uniform display of custom web controls

To make the display of a Custom Web Control independent of the browser you are using, you must use a stylesheet when programming the Custom Web Control.

### TextsByValues

The "TextsByValues" method returns a list of all the texts of a language for the given values from a text list. To achieve this, the parameter "lcid" for the language and the parameter "values" for the desired values have to be transferred (passed). The method can be used in scripts for objects of type "HMITextList".

### OpenFaceplateInPopup

The following optional parameters were inserted in the "OpenFaceplateInPopup" method:

| Parameters | Description |
| --- | --- |
| popupWindowName | Name of the popup window.   Note that the name must be unique in the project.  If the parameter is omitted, a unique name is generated automatically. |
| adaptWindow | If `true`, the size of the popup window is automatically matched to the size of the faceplate and cannot be defined by the "width" and "height" parameters.  The default value is `true`. |
| left | Left coordinate of the position of the popup window.  The default value is 10. |
| top | Upper coordinate of the position of the popup window.  The default value is 10. |
| width | Width of the popup window.  Is used if the "adaptWindow" parameter is `false`.  The default value is 100. |
| height | Height of the popup window.  Is used if the adaptWindow parameter is `false`.  The default value is 100. |

By using the new parameters, faceplates are shown in the correct size in popup windows.

Since the parameters are optional, this has no effect on existing scripts.

## Parameter sets and parameter set display

### Contents

Information that could not be included in the online help and important information about product features.

### Using parameter set display from V16 project

If you have configured a parameter set control in WinCC V16 without updates, open this project with WinCC V17 and download it to the HMI device, then the numbers of the parameter sets are not displayed on the HMI device. Proceed as follows to continue using this parameter set control:

1. Create a new project in a new instance of WinCC V16 with installed update.
2. Insert a Unified Comfort Panel or a SIMATIC Unified PC into the project.
3. Copy the devices from the original project into the new project.

### Configuring a storage medium for parameter sets

Select the same storage medium that you have configured for tag persistence or alarm logging under "Properties &gt; Information" for parameter set types. If you specify different storage media, the "EjectStorageMedium" system function is not available.

## WinCC Unified PC

This section contains information on the following topics:

- [Breaking changes](#breaking-changes-1)
- [GDPR - General Data Protection Regulations](#gdpr---general-data-protection-regulations)
- [Notes on installation](#notes-on-installation)
- [Notes on the operation of Unified PC](#notes-on-the-operation-of-unified-pc)
- [Internet browsers for WinCC Unified PC](#internet-browsers-for-wincc-unified-pc)
- [Activating and testing ASIA licenses](#activating-and-testing-asia-licenses)
- [Remote access to a Unified device](#remote-access-to-a-unified-device)

### Breaking changes

#### PI options in ODK

ODK does not support any PI options in V19.

#### Scrolling behavior for pop-ups

If you move the visible screen section of a process screen in Runtime and a pop-up window is visible there, for example a faceplate container, Runtime behaves as follows:

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | The pop-up window is moved together with the screen section. |
| As of WinCC Unified V18 | The pop-up window is not moved with it. |
| Simulation of an HMI device with installed device version V17 in a WinCC project V18 or higher | The pop-up window is moved together with the screen section. |

#### Operation of objects behind a screen window

If a screen window has an empty area and the screen or faceplate displayed in the screen window has the "transparent" setting as the fill pattern for the background, Runtime behaves as follows:

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | Objects that are in the background of the screen window in the empty area of the screen window are visible. The objects cannot be operated by clicking. |
| As of WinCC Unified V18 | The objects can be operated by clicking.  Application example: You use a round menu with a button next to it. To prevent the rectangular border surrounding the menu from obscuring the button, make the menu available in a screen window. |

#### Zoom behavior of screen windows on touch devices

Runtime now supports panning and zooming with a two-finger gesture.

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | No panning and zooming with two-finger gestures. |
| As of WinCC Unified V18 | Panning and zooming with two-finger gestures is supported.  Default: Activated   If you want, you can disable this feature by clearing "Format &gt; Allow zoom" property for the screen window. |

#### Exclusion of "Uncertain - initial value" quality code as trigger

| Symbol | Meaning |
| --- | --- |
| WinCC Unified V17 | If a tag is used as a trigger for a script and the tag is used in a screen, e.g. by an I/O field, the script is executed twice in quick succession when the screen is loaded:  - When reporting the initial value - When reporting the process value |
| As of WinCC Unified V18 | Default setting: QualityCode 0x4C (Quality status: Uncertain, Substatus: Initial value) is ignored as a tag trigger.   If a tag is used as a trigger for a script and the variable is used in a screen, e.g. by an I/O field, the script is only executed when the process value is reported as the screen is loaded.  To enable the quality code as a trigger, proceed as described below. |

To enable QualityCode 0xC4 as a trigger in V18 or higher, do the following:

1. Open a file browser and navigate to the following folder:

   `C:\Program Files\Siemens\Automation\WinCCUnified\bin\_config`
2. Open the following configuration file:

   - For scripts in screens: `IOWA_GfxComponentConfigurationSrv.xml`
   - For scheduled tasks: `IOWA_SchedComponentConfiguration.xml`
3. Delete the line for &lt;Attribute key&gt;:

   `<ComponentConfiguration componentKey="GfxTriggerManager" name="Trigger Manager">`
     
    `<AttributeList>`
     
    `<Attribute key="IgnoredTagQualities" value="0x4c"/> <!— 0x4c: “Initial Value” quality >`
     
    `</AttributeList>`
     
   `</ComponentConfiguration>`

#### Simulation of Runtime

To use the simulation, you must install WinCC Unified Runtime. If no license is found for Runtime, start the simulation in demo mode.

#### OPC UA with OpenSSL 3.0

WinCC Unified uses OPC UA OpenSSL 3.0 from V18 Update 3 and higher.

If the OPC UA certificate of an HMI device has been created before V18 Update 3, it becomes incompatible through the device upgrade and has to be recreated. Follow these steps.

IF the HMI device uses a CA-based OPC UA certificate:

1. Upgrade the certificate authority device and the HMI device.
2. Re-create the OPC UA certificate of the HMI device on the certificate authority device with WinCC Unified Certificate Manager.
3. Install the certificate on the HMI device.

   If the communication partner already trusts the root certificate of the certificate authority, it automatically also trusts the newly created OPC UA certificate of the HMI device.

If the HMI device uses a self-signed OPC UA certificate:

1. Delete the certificate from the certificate store before upgrading the HMI device:

   - For Unified PCs:

     The certificate store is located in the folder with the Runtime projects in the subfolder "`certstore`".

     Default: `C:\ProgrammData\SCADAProjects\certstore`​
   - For Unified Panel:

     Select "Control Panel &gt; Security &gt; Certificates" and as the "Certificate store" the entry "My Certificates". Select the certificate and delete it.
2. Upgrade the HMI device.

   For Unified PC: The certificate is automatically generated and installed.
3. For Unified Panel: Start Runtime.

   The certificate is automatically generated and installed.
4. Trust the certificate at the communication partner.

### GDPR - General Data Protection Regulations

Siemens takes data privacy principles, such as the privacy by design and default principle, into account when developing its products and services. For this product WinCC Unified Runtime this means the following:

#### Personal data processed by the Application

This product collects and processes the following personal data:

- User names, i. e. login data, which might directly contain or establish a reference to the family name and/or first name
- Timestamps: date / time of login, logoff and access
- Location data (time zone)
- Computer name
- IP addresses
- Optional: With UMC, the following additional personal data can be added in the tool:

  - Full name
  - Comment

  This data is not needed for the product functionality and should not be stored on the same medium.

If the user links the above-mentioned data with other data, e. g. shift plans, or stores personal data on the same medium, e. g. hard disk, and thus establishes a personal reference, the user must ensure compliance with data protection regulations.

#### Purposes

The above data is required for the following purposes:

- Access protection and security measures (e. g. Login, IP address)
- Process synchronization and integrity (e. g. time zone information, IP addresses)
- Archiving system for traceability and verification of processes (e. g. access timestamps)
- Alarm system for traceability and availability (for example, e-mail notification)

The storage of data is appropriate and limited to what is necessary, as it is essential to identify the authorized operators and process events.

#### Data configuration

The customer can configure the data collected via the product as follows:

- Display data in process pictures
- Data output in form of reports, e. g. for printing or display as electronic file
- Data collection and evaluation in form of graphics, e. g. for KPI analysis

#### Deletion policy

The product does not provide an automatic deletion of the above data.

If necessary, these can be deleted manually if desired. To do this, refer to the product documentation or contact customer support.

#### Securing of data

The above data will not be stored anonymously or pseudonymized, because the purpose of access and event identification cannot be achieved otherwise.

For WinCC Unified PC-based, the data specified above should be secured by appropriate technical measures:

- Encryption of log data
- Storing the process data in access-protected SQL databases

  The user must ensure the access protection as part of their process configuration.

You can find information on data backup on the WinCC Unified Comfort Panel in the operating instructions for the Comfort Panel.

### Notes on installation

#### Contents

Important notes on installation.

#### Previously installed versions of WinCC Unified

The installation of Unified V18 is possible on devices for which the following applies:

- No Unified installed yet, or
- WinCC Unified V17 installed  
  The V17 installation must not have been upgraded from V16.

#### Special characters in the installation path

Special characters in the installation path may lead to objects not being visible when inserted into a screen. To see the object, you have to close the screen and open it again.

#### Record/play function

When the record/play function is used, the Runtime system settings made in WinCC Unified Configuration Manager during or after installation are not recorded.

Silent installation of Runtime using the record/play function is not supported.

### Notes on the operation of Unified PC

#### Contents

Information that could not be included in the online help and important information about product features.

#### Generic logon error due to browser language settings

If a language that is not supported by Unified Runtime is set as the browser language, the "Generic error" occurs during logon.

Follow these steps:

1. Open the browser language settings.
2. Select one of the languages supported by Unified Runtime.
3. Log on in Runtime.

#### Restoring log segments

The following requirements apply to restoring log segments with SIMATIC Runtime Manager:

- A project that is in the "Running" status is loaded into runtime.
- At least one backup of a tag or alarm log is available for the project.
- If the project was loaded several times, no logs were reset during complete loading in the "Load preview" dialog.

#### TraceViewer

If the user logged on in Runtime belongs to the "RTIL Tracing Users" and "SIMATIC HMI" user groups, all trace messages are visible in the TraceViewer, otherwise only the trace messages from SIMATIC Runtime Manager.

#### My WinCC Unified

After login, My WinCC Unified has the user interface language that you selected in the login dialog. If you have not selected a language, the language that is set for the browser is used.

#### Kiosk

The following contents could not be taken into consideration before the editorial deadline for the online help "My WinCC Unified":

- The display of Runtime in kiosk mode is supported on all client devices with Windows operating system (PCs, Notebooks, etc.).
- The application "SIMATIC Unified Control Center" has been renamed to "WinCC Unified Station Configurator".
- To install WinCC Unified Station Configurator on a client device that is to use the kiosk mode, proceed as follows:

  - Copy the following file from the WinCC Unified Runtime server that is to be displayed as a kiosk onto the client device:

    C:\Program Files\Siemens\Automation\WinCCUnified\StationConfigurator\SIMATIC_WinCC_Unified_StationConfigurator.exe
  - On the client device, right-click the "Start" application and select "Run as administrator".
  - Select the required installation language and follow the installation instructions.
  - Reboot the device.
- For a client device with several monitors, the main screen shows Runtime in kiosk mode. The other monitors show the Windows desktop.
- The following restrictions apply to the import of YAML files with kiosk settings:

  Restrictions for `BreakOutData`:

  | Symbol | Meaning |
  | --- | --- |
  | `Keys` | Mandatory specification.   Only ALT+F4 is supported. |
  | `IsEnabled` | - `IsEnabled = true`     `SelectedKey` must have a valid value. - `IsEnabled = false`     `SelectedKey` must have an empty value. |
  | `SelectedKey` | Only keys that are supported in the `Keys` property are allowed. |
  | `IsPinConfigured` | - `IsPinConfigured = true`     `Pin` must have a valid value. - `IsPinConfigured = false`    Does not expect a property `Pin` or `Pin` with empty value. |

  Restrictions for `FolderData`:

  | Symbol | Meaning |
  | --- | --- |
  | `FolderData` | `FolderItems` must have at least 1 item. |
  | `FolderItems` | Per item: - `Path`    Mandatory specification - `IsDefault`    Mandatory specification   Only 1 item can have `IsDefault = true`. |

#### Adding a project offline

Users who add a project in SIMATIC Runtime Manager through the offline transfer and enable the option "Overwrite UMC data with the context of the offline loading", must be members of the Windows user group "umcd_global_admin".

Note that changes to the membership of a Windows user group only take effect with the next Windows login of the user.

### Internet browsers for WinCC Unified PC

Ensure you have the latest operating system and browser version if you want to access Runtime Unified with this device.

WinCC Unified displays the runtime elements in HTML5. The browser used also has to support this standard. Since the browsers interpret HTML5 differently, it is possible that objects are displayed differently depending on the browser and the browser version used. For example, browsers sometimes display fonts differently.

Compatibility tests were performed for the following browsers. The focus of the compatibility tests was on the browsers marked with *:

| Operating system | Browser |
| --- | --- |
| Microsoft Windows | - Google Chrome* - Microsoft Edge - Mozilla Firefox, Mozilla Firefox ESR |
| Android | - Google Chrome* - Firefox - Edge |
| iOS, Mac | - Safari* - Google Chrome - Firefox - Edge |

**Browser recommendation**

In view of the performance and support of the Runtime standard elements, Google Chrome has proven to be the preferred browser. Its memory requirements are slightly higher than those of the other browsers.

> **Note**
>
> **Operating system and browser version**
>
> For Runtime operation via Android or iOS, always use the latest operating system.
>
> Use the latest browser version.

> **Note**
>
> **Performance differences in different versions of individual browsers**
>
> The browser versions can differ from each other, which can result in different behavior regarding the memory requirements and speed.

> **Note**
>
> **Suitability for continuous operation**
>
> Mozilla Firefox has proven to be problematic in continuous operation.

#### Known browser problems

The following restrictions apply to the following browsers:

| Internet browser | Limitation |
| --- | --- |
| MS Edge | - If you want to start Runtime in Microsoft Edge and enter the address "https://localhost", the error message "INET_E_RESOURCE_NOT_FOUND" appears. In this case, use the address "https://localhost/WebRH". |
| Mozilla Firefox | - High memory capacity utilization in continuous operation |
| Mozilla Firefox ESR | - Support of touch gestures for touch panels as of Firefox ESR V59 |
| Google Chrome | - High memory capacity utilization in uninterrupted duty depending on the version. - On Android: Grid lines with a line width ≤1 are not displayed correctly. This is due to the browser's own line thickness representation. As a solution, it is helpful to use a line width ≥1. - No correct representation of elements that use an SVG graphic as background graphic scaled in the Engineering System. |

Restrictions to the various functions can also occur, such as the availability of the before and after buttons in the controls.

#### Current information on browser problems

You can find up-to-date information on display problems in browsers at the Siemens Online Support under the entry ID 109757952.

### Activating and testing ASIA licenses

#### Overview

The license keys for WinCC Runtime Unified are available on the "License Key USB Hardlock" license storage medium.

The licensed ASIA version is executable in parallel to the European version by switching to Unicode.

The "License Key USB Hardlock" (dongle) checks the following conditions:

- WinCC GUI language
- Runtime language
- Asian characters are used in the WinCC project.
- Operating system settings

> **Note**
>
> It is not allowed to run WinCC in process mode without a valid license.
>
> **Delete configuration languages**
>
> If you do not have a license for an ASIA version and delete the Asian configuration languages, the WinCC project continues to run in demo mode.
>
> To disable Demo mode, close the WinCC project. When reopened it is recognized that the WinCC project no longer requires licenses for an ASIA version.

#### Testing the validity of the licenses

If you start a correctly licensed WinCC version without the connected dongle, an error message appears. The same error message appears after a few minutes if you disconnect the dongle from the computer with a correctly licensed WinCC version.

If this error message does not appear, a non-licensed WinCC version is installed. No right of usage for WinCC is available in this case. Uninstall this WinCC version and purchase a legally licensed version of WinCC.

If necessary, contact WinCC Support and provide the serial number of your software version:

- http://www.automation.siemens.com/partner/index.asp

You can find the serial number on the "Certificate of License" (CoL).

#### Working with the "License Key USB Hardlock"

Please note the following:

- Do not edit data on the "License Key USB Hardlock".

  The actions not allowed include:

  - Rename data
  - Delete data
  - Copy data to the "License Key USB Hardlock"
- Do not format the "License Key USB Hardlock".
- Do not remove the "License Key USB Hardlock" from the PC while WinCC is running.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Do not remove the "License Key USB Hardlock" dongle**  If you remove the dongle from the computer, an error message is generated and WinCC switches to Demo mode.  If you re-connect the dongle to the computer, the error message disappears and Demo mode is disabled. WinCC works once again in licensed mode. |  |

### Remote access to a Unified device

#### Contents

Information that could not be included in the online help and important information about product features.

#### Synchronize client values with server time

By default, the following controls display values with client time:

- Alarm control
- Trend companion
- Trend control
- f(x) trend control
- Process control

To synchronize the time displayed on the client with the server, proceed as follows:

- iOS devices:

  To prevent an iOS device from synchronizing with time.apple.com, create a profile file and upload it to the device.

  Profile files enable time synchronization within a secure corporate network.
- Android devices:

  Use a third-party app for time synchronization.

#### Access to a Unified device

Ensure you have the latest operating system and browser version if you want to access Runtime Unified with this device.

WinCC Unified displays the runtime elements in HTML5. The browser used also has to support this standard. Since the browsers interpret HTML5 differently, it is possible that objects are displayed differently depending on the browser and the browser version used.

Compatibility tests were performed for the following browsers. The focus of the compatibility tests was on the browsers marked with *:

| Operating system | Browser |
| --- | --- |
| Microsoft Windows | - Google Chrome* - Microsoft Edge - Mozilla Firefox, Mozilla Firefox ESR |
| Android | - Google Chrome* - Firefox - Edge |
| iOS, Mac | - Safari* - Google Chrome - Firefox - Edge |

With respect to the performance and support of the standard Runtime elements, Google Chrome has proven to be the preferred browser. Its memory requirements are slightly higher than those of the other browsers.

> **Note**
>
> **Performance differences in different versions of individual browsers**
>
> The browser versions can differ from each other, which can result in different behavior regarding the memory requirements and speed.

> **Note**
>
> **Suitability for continuous operation**
>
> Mozilla Firefox has proven to be problematic in continuous operation.

#### Unified Collaboration

Unified Collaboration is only permitted between devices with the same device version (starting from V16).

If Unified Collaboration uses local user management and the Collaboration partners are configured in different projects, it is possible to create users with the same name but different function rights. If one of these users logs on to a device in Runtime, the user has the function rights configured for this device as well as the function rights configured for the Collaboration partner. If you use several projects, you should configure the local user management identically in all projects.

## Notes on the operation of Unified Panel

### Contents

Information that could not be included in the online help and important information about product features.

### Changes to the settings of the SOC1 interface (X1)

The following changes to the settings of the SOC1 interface (X1) require a manual restart of the Panel:

- Settings related to the mode and speed of the SOC1 ports
- Media redundancy settings
- Deactivating the forwarding of DCP broadcasts
- Deactivating the sending of LLDP

### Objects with buttons

Some objects such as the trend control or the parameter set control have buttons for which you can configure access rights. To operate access-protected buttons, a user with the required authorization must log on via the Control Panel or a configured operating object.

### Alarm control - Displaying logged alarms

Logged alarms are not displayed after starting the Runtime software if the static value "Logged alarms updated" is configured in the properties of the alarm control under "General &gt; Alarm source". To make logged alarms visible in the alarm control, click the "Show logged alarms" or "Show and update logged alarms" button in the alarm control.

The "Update and display logged alarms" list shows a maximum of 100 alarms.

### "StopRuntime" system function

The StopRuntime system function only works if encrypted transfer has been configured in the Runtime settings of the Panel.

### System function "StartProgram" in the Scheduler

Calling up a program via the "StartProgram" system function in the Scheduler is not supported by Unified Comfort Panel. Instead, use a "Tags" trigger in the Scheduler to initiate the system function.

### Access to MS SQL databases and SQLite databases

You can access MS SQL databases and SQLite databases via JavaScript functions from Unified Comfort Panel. Note that the resource utilization is directly proportional to the number of the requests to the database and the size of the data to be read or written. This means that the accesses to databases also affect the performance in Runtime. In order to not impair the operation as a visualization system the possibility to access databases should be used prudently.

From a Unified Comfort Panel you can only access databases which support the driver "Microsoft ODBC Driver for SQL Server" in Version 17.9.

These include:

- Azure SQL Database
- Azure Synapse Analytics
- Azure SQL Managed Instance
- SQL Server 2019
- SQL Server 2017
- SQL Server 2016
- SQL Server 2014
- SQL Server 2012

### Gauge output format

If you specify the value {H} (Hexadecimal) in the Inspector window of a gauge under "Properties &gt; General &gt; Scale &gt; Output format", negative values in the gauge will not be displayed correctly. If you want to output negative values via a gauge, use {F}, {N} or {I} as output format.

### Runtime Collaboration - function trend control

If a function trend control is configured in a screen to display logged data and you access this screen with Runtime Collaboration, no existing logged data is displayed in the trend control. The first value displayed is the value that will be written to the log after the screen is opened.

### Differences between simulation and Unified Comfort Panel

There are differences in the simulation regarding the following screen objects as compared to the Unified Comfort Panel Runtime:

- Alarm control:

  - Filter options
- Faceplates:

  - Scaling in JavaScript method "OpenFaceplateInPopup"
  - Arrangement of the faceplate containers for JavaScript method "OpenFaceplateInPopup"
- Screen window:

  - Scaling with system function "OpenScreenInPopup"
- I/O field: Default display for Word and DWord data types
- Parameter set display: Default display for Word data type
- Browser:

  - The display of pages of the S7 WebServer is not possible in the simulation.

### Simulation in connection with SD-X51

The simulation of tag retentivity and alarm logging in connection with the "SD-X51" storage medium is not supported.

### Incorrect counting of tags

When using faceplates in Unified Panels, tag arrays and tags based on User Data Types (UDT) are incorrectly counted as 1 tag.

## Remote access to a Unified device

### Contents

Information that could not be included in the online help and important information about product features.

### Synchronize client values with server time

By default, the following controls display values with client time:

- Alarm control
- Trend companion
- Trend control
- f(x) trend control
- Process control

To synchronize the time displayed on the client with the server, proceed as follows:

- iOS devices:

  To prevent an iOS device from synchronizing with time.apple.com, create a profile file and upload it to the device.

  Profile files enable time synchronization within a secure corporate network.
- Android devices:

  Use a third-party app for time synchronization.

### Access to a Unified device

Ensure you have the latest operating system and browser version if you want to access Runtime Unified with this device.

WinCC Unified displays the runtime elements in HTML5. The browser used also has to support this standard. Since the browsers interpret HTML5 differently, it is possible that objects are displayed differently depending on the browser and the browser version used.

Compatibility tests were performed for the following browsers. The focus of the compatibility tests was on the browsers marked with *:

| Operating system | Browser |
| --- | --- |
| Microsoft Windows | - Google Chrome* - Microsoft Edge - Mozilla Firefox, Mozilla Firefox ESR |
| Android | - Google Chrome* - Firefox - Edge |
| iOS, Mac | - Safari* - Google Chrome - Firefox - Edge |

With respect to the performance and support of the standard Runtime elements, Google Chrome has proven to be the preferred browser. Its memory requirements are slightly higher than those of the other browsers.

> **Note**
>
> **Performance differences in different versions of individual browsers**
>
> The browser versions can differ from each other, which can result in different behavior regarding the memory requirements and speed.

> **Note**
>
> **Suitability for continuous operation**
>
> Mozilla Firefox has proven to be problematic in continuous operation.

### Unified Collaboration

Unified Collaboration is only permitted between devices with the same device version (starting from V16).

If Unified Collaboration uses local user management and the Collaboration partners are configured in different projects, it is possible to create users with the same name but different function rights. If one of these users logs on to a device in Runtime, the user has the function rights configured for this device as well as the function rights configured for the Collaboration partner. If you use several projects, you should configure the local user management identically in all projects.

## Working with plant objects and plant views

### Contents

Information that could not be included in the online help and important information about product features.

### Introduction

You have the possibility to upgrade the project to V17 when opening your V16 project with a system configuration. The configured Runtime version of the HMI devices must be changed separately to V17.

### Updating blocks

If blocks from a global or from a project library are used in the project, do the following:

1. Open the plant object type that uses a block from a library.
2. Delete the interconnection of the PLC tag.
3. Open the "Library" task card.
4. In the library, open the shortcut menu of the block used.
5. Click on "Project" under "Update types".

   The "Update types in the project" dialog opens.
6. Select the option "Force update (types including their dependent types are updated regardless of their version number)".

   All other options are already selected by default.
7. Click "OK".
8. Compile the PLC.
9. Interconnect the PLC tag for the plant object type.
10. Compile and download your project.

> **Note**
>
> Alternatively, delete all plant objects (instances) from the plant hierarchy, perform the update and create all plant objects (instances) again in the plant hierarchy. If you have linked a screen to the plant object in the "Visualization" tab, deleting the plant object not only deletes the link, but also entire screen. Create a copy of the screen and link the screen to the new plant object after updating the blocks.

## Audit

### Contents

Information that could not be included in the online help and important information about product features.

### Restore database segments in Runtime

To analyze the logged and deferred data, as an HMI Administrator of an HMI device, you can restore backed up audit database segments in Runtime. After the analysis, these segments can be discarded again to empty the memory space.

## View of Things

### Contents

Information that could not be included in the online help and important information about product features.

### Supported functionalities

The following functionalities are supported in the VoT application:

- Event "Input finished" for the object I/O field
- Simple object "Label"
- Multiuser support for configuration of screens

### Improvements in the screen editor

The following improvements in the screen editor are supported in the VoT application:

- Functions in the toolbar:

  - Font
  - Text alignment
  - Determining the border width or line width
  - Line type
- "Hide change events" function
- Resetting the properties of screens and screen objects from the manually set value to the default value of the style
- Centrally configuring the background color for all screens in the project
- Moving objects between layers by means of the "Layer" property

### Displaying the properties of a collection

Some screen objects contain a collection of similar elements under the properties. The properties of the elements in the collection are displayed and managed in a table in the Inspector window.

When managing the properties of the elements in a collection, you can:

- Show or hide the individual properties
- Show all columns
- Optimize the width of a column
- Optimize the width of all columns

### Unsupported functionalities

The following functionalities are not supported in the VoT application:

- Configuring of the screen management
- Controls:

  - System diagnostics view
  - ProDiag overview
- Number of failed login attempts
- User-defined styles
- Zooming without holding down the Control key
