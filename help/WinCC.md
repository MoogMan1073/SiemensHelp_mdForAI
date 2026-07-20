---
title: "WinCC"
package: ReadMeWCCPenUS
topics: 41
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC

This section contains information on the following topics:

- [Upgrade unsupported HMI devices](#upgrade-unsupported-hmi-devices)
- [WinCC Basic, Advanced, Professional](#wincc-basic-advanced-professional)
- [WinCC Unified](WinCC%20Unified.md#wincc-unified)
- [Visualizing Processes with View of Things](#visualizing-processes-with-view-of-things)

## Upgrade unsupported HMI devices

If a project contains an unsupported device or a device with an unsupported HMI device version, a message is issued when the project is upgraded. To use the project in the current version, you do not need to delete all the unsupported HMI devices in the project or replace them with a supported device. Note that unsupported devices may also be present in the master copies.

### Replacing a device in the project tree

1. Open the project with a version of the TIA Portal in which the device or HMI device version is supported.
2. In the shortcut menu of the device in the project tree click on "Replace device".
3. As the new device, select a device supported in the current version with an HMI device version supported by the current version.
4. Save the project.
5. Open the project in the current version of the TIA Portal

### Replacing a device in a master copy

1. Open the project with a version of the TIA Portal in which the device or device version is supported.
2. Drag the device from the master copy to the project tree.
3. Delete the device in the master copy.
4. In the shortcut menu of the device in the project tree click on "Replace device".
5. As the new device, select a device supported in the current version with a device version supported by the current version.
6. Drag the device from the project tree to the master copy.
7. Delete the device in the project tree.
8. Save the project.
9. Open the project in the current version of the TIA Portal

### Upgrade across multiple versions

With bigger version jumps, e.g. from V13 to V18, it may happen that none of the device versions configurable in V13 is supported in the current version. In this case, you need another WinCC version, e.g. V15.1.

1. Upgrade the project to V15.1.
2. In V15.1, replace the device or device version with a device version supported in the current version.
3. Save the project.
4. Upgrade the project to the latest version.
5. If required, replace the device version with a device version supported in the current version.

### Unsupported HMI devices as of TIA Portal V18

The following HMI devices are no longer supported as of TIA Portal V18:

### Unsupported HMI devices as of TIA Portal V17

The following HMI devices are no longer supported as of TIA Portal V17:

### Unsupported HMI devices as of TIA Portal V16

The following HMI devices are no longer supported as of TIA Portal V16:

- Mobile Panel with device version 12.x
- Comfort Panel with device version 12.x
- KP1500 Comfort with device version 13.x
- TP1500 Comfort with device version 13.x
- TP1900 Comfort with device version 13.x
- TP2200 Comfort with device version 13.x

### Unsupported HMI devices as of TIA Portal V15.1

The following HMI devices are no longer supported as of TIA Portal V15.1:

- WinCC Runtime Advanced V11

### Unsupported HMI devices as of TIA Portal V15

All HMI devices with version 11.x are no longer supported as of TIA Portal V15.

The following HMI devices are no longer supported as of TIA Portal V15:

- WinAC MP 177, WinAC MP 277, WinAC MP 377
- Panels: OP and TP of the 70 series, 170 series and 270 series
- Multi Panels: Multi Panels of the 170, 270 and 370 series

## WinCC Basic, Advanced, Professional

This section contains information on the following topics:

- [Security information](#security-information)
- [Data protection](#data-protection)
- [Notes on use](#notes-on-use)
- [Screens and Screen Objects](#screens-and-screen-objects)
- [Tags and connections](#tags-and-connections)
- [Alarm system and alarm displays](#alarm-system-and-alarm-displays)
- [System functions and scripts](#system-functions-and-scripts)
- [Reports](#reports)
- [Recipes](#recipes)
- [User administration](#user-administration)
- [Communication](#communication)
- [System-wide functions](#system-wide-functions)
- [Compiling and loading](#compiling-and-loading)
- [Runtime](#runtime)
- [Add-ons](#add-ons)
- [Migration](#migration)
- [HMI devices](#hmi-devices)

### Security information

#### Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines, and networks.

In order to protect plants, systems, machines, and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens' products and solutions only form one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary, and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For more information on protective industrial cybersecurity measures for implementation, visit:

[www.siemens.com/industrialsecurity](https://www.siemens.com/industrialsecurity)

Siemens' products and solutions undergo continuous development to make them more secure. Siemens strongly recommends applying product updates as soon as they are available and always using only the latest product versions. Use of product versions that are no longer supported, and failure to apply latest updates may increase customer's exposure to cyber threats.

To stay informed about product updates at all times, subscribe to the Siemens Industrial Cybersecurity RSS Feed under.

[www.siemens.com/cert](https://www.siemens.com/cert)

#### Passwords

Various passwords are set by default in WinCC. For security reasons, you should change these passwords.

- For HMI devices with version 12, the default password for the Sm@rtServer and for the integrated Web server is "100". A default password is not preset for HMI devices with version V13.
- For the user "Administrator", the default password is "administrator".

#### Integrated Web server

It is always possible on a PC to access HTML pages in runtime, although the option "HTML pages" is deactivated. Setup always installs the standard pages of the Web Server on the PC. Assign an administrator password to prevent unauthorized access to the pages.

#### Communication via Ethernet

In Ethernet-based communication, end users themselves are responsible for the security of their data network. The proper functioning of the device cannot be guaranteed in all circumstances; targeted attacks, for example, can lead to overload of the device.

#### Use of SSL 3.0

For security reasons, the use of the protocol SSL 3.0 is not recommended on Comfort Panels or in Runtime Advanced. The use of the protocol SSL 3.0 is disabled by default on Comfort Panels. If you nevertheless wish to activate the use of SSL 3.0, select the following in Internet Explorer or in "Start Center &gt; Settings: Internet Options &gt; Advanced &gt; Use SSL 3.0".

For RT Advanced, the use of SSL 3.0 can be disabled in Internet Explorer or in the Control Panel under "Internet Options &gt; Advanced" by deactivating the "Use SSL 3.0" option.

#### Network settings

The following tables show the network settings of each product which you need in order to analyze the network security and for the configuration of external firewalls:

| WinCC Professional (without simulation) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| ALM | 4410* | TCP | Inbound, Outbound | License service | This service provides the complete functionality for software licenses and is used by both the Automation License Manager as well as all license-related software products. |
| HMI Load | 1033 | TCP | Outbound | HMI Load (RT Basic) | This service is used to transmit images and configuration data to Basic Panels. |
| HMI Load | 2308 | TCP | Outbound | HMI Load  (RT Advanced) | This service is used to transmit images and configuration data to panels. |
| RPC | ** | UDP | Inbound, Outbound | Client / server &amp; ES communication (CCAgent) | This service is used by WinCC Professional and WinCC Runtime Professional. |
| * Default port that can be changed by user configuration  ** Port is assigned automatically |  |  |  |  |  |

| WinCC Simulation for Basic Panels |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| HMI Load | 1033 | TCP | Inbound | HMI Load  (RT Basic) | This service is used to transmit images and configuration data to Basic Panels. |
| EtherNet/IP | 44818 | TCP | Outbound | Ethernet/IP channel | The Ethernet/IP protocol is used for connections to Allen Bradley PLCs. |
| 2222 | UDP | Inbound | Ethernet/IP channel | The Ethernet/IP protocol is used for connections to Allen Bradley PLCs. |  |
| Modbus TCP | 502 | TCP | Outbound | Modbus TCP channel | The Modbus TCP protocol is used for connections to Schneider PLCs. |
| RFC 1006 | 102 | TCP | Outbound | S7 channel | Communication with the S7 controller via Ethernet/PROFINET |
| Mitsubishi MC | 5002 | TCP | Outbound | Mitsubishi MC channel | The Mitsubishi protocol is used for connections to Mitsubishi PLCs. |

| WinCC Simulation for Panels and Runtime Advanced |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| DCP | --- | Ethernet | Outbound | PROFINET | The DCP protocol (Discovery and basic Configuration Protocol) is used by PROFINET and provides the basic functionality for locating and configuring PROFINET devices. |
| LLDP | --- | Ethernet | Inbound, Outbound | PROFINET | The LLDP protocol (Link Layer Discover Protocol) is used by PROFINET for topology detection. |
| SMTP | 25 | TCP | Outbound | SMTP  Communication | This service is used by WinCC Runtime Advanced to send e-mails. |
| HTTP | 80* | TCP | Inbound | HTTP channel server  HTML pages | The web server is only available when HTTP channel servers or HTML pages are activated The used port may differ depending on automatically selected settings. |
| RFC 1006 | 102 | TCP | Outbound | S7 channel | Communication with the S7 controller via Ethernet/PROFINET |
| NTP | 123 | UDP | Outbound | Time synchronization | The NTP protocol (Network Time Protocol) is used for time synchronization in IP-based networks. |
| SNMP | 161 | UDP | Outbound | PROFINET | The SNMP client functionality is used by STEP 7 to read status information from PROFINET devices. |
| HMI Load | 2308 | TCP | Outbound | HMI Load (RT Advanced) | This service is used to transmit images and configuration data to panels. |
| HTTPS | 443* | TCP | Inbound | HTTP channel server  HTML pages | The web server with HTTPS protocol is only available when HTTP channel servers or HTML pages are activated. The used port may differ depending on automatically selected settings. |
| VNC server | 5900* | TCP | Inbound | Sm@rtServer | This service is only available when Sm@rtService is activated. |
| 5800* | TCP | Inbound | Sm@rtServer | This service is only available when Sm@rtService is activated. |  |
| VNC client | 5500 | TCP | Outbound | Sm@rtServer | This service is only available when Sm@rtService is activated. |
| * Default port that can be changed by user configuration |  |  |  |  |  |

| WinCC Simulation for Runtime Professional |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| RPC | ** | UDP | Inbound, Outbound | Client / server &amp; ES communication (CCAgent) | This service is used by WinCC Professional and WinCC RT Professional. |
| RPC | ** | UDP | Inbound, Outbound | Client / server communication (CCEServer / CCEClient) | This service is used by WinCC Runtime Professional. |
| HTTP | 80 | TCP | Inbound, Outbound | Client / server communication (CCEServer / CCEClient) | This service is used by WinCC Runtime Professional. |
| RFC 1006 | 102 | TCP | Outbound | S7 channel | Communication with the S7 controller via Ethernet/PROFINET |
| OPC UA | 4840 | TCP | Inbound | OPC UA server | This service is required for primary communication via OPC UA. It is activated and configured during installation. |
| OPC UA discovery | 52601 | TCP | Inbound | OPC UA server | This service provides information about the installed OPC server. It is installed and configured by the OPC UA server. |
| DCOM | 135 | TCP | Inbound | OPC server | This service is part of the Windows operating system. Since communication via OPC (DA) is based on DCOM, this service is required to initialize OPC (DA) connections. |
| DCOM | ** | TCP | Inbound | OPC server | The communication via OPC (DA) is based on DCOM and uses unspecified ports assigned by the system. This should be taken into consideration when using OPC (DA) and creating rules for the firewall. |
| NetBIOS | 137 | UDP | Inbound | OPC server | This service is part of the Windows operating system. Access to this service is required by OPC-Scout, for example, for browsing. |
| NetBIOS | 138 | UDP | Inbound | OPC server | This service is part of the Windows operating system. Access to this service is required by OPC-Scout, for example, for browsing. |
| SNMP | 161 | UDP | Outbound | SNMP OPC server | This service is used by the SNMP OPC server to change or query data on network drives, for example. |
| SNMP Traps | 162 | UDP | Inbound | SNMP OPC server | This service is used by the SNMP OPC server to query events from network drives, for example. |
| ** Port is assigned automatically |  |  |  |  |  |

| PROFINET protocols for Panels and Runtime Advanced |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| DCP | --- | Ethernet | Outbound | Lifelist,   PROFINET Discovery and configuration | The DCP protocol (Discovery and basic Configuration Protocol) is used by PROFINET and provides the basic functionality for locating and configuring PROFINET devices. |
| LLDP | --- | Ethernet | Inbound, Outbound | PROFINET Link Layer Discovery protocol | The LLDP protocol (Link Layer Discover Protocol) is used by PROFINET for topology detection. |
| MRP | --- | Ethernet | Outbound | PROFINET medium redundancy | The MRP protocol (Medium redundancy protocol) enables control of redundant transmission paths using a ring topology. |
| PROFINET IO Data | --- | Ethernet | Inbound, Outbound | PROFINET Cyclic IO data transfer | Cyclic data exchange is used by panels for direct keys and LEDs. |
| ARP | --- | Ethernet | Inbound, Outbound | Name Address Resolution | This protocol is used to resolve network names and assign IP addresses. |
| PROFINET Context Manager | 34964 | UDP | Inbound, Outbound | PROFINET connection less RPC | The PROFINET Context Manager provides an endpoint mapper in order to establish an application relation (PROFINET AR). |

| Communication connections for Panels and WinCC Runtime Advanced |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| Telnet | 23 | TCP | Inbound | Telnet | This service can be used for maintenance. |
| SMTP | 25 | TCP | Outbound | SendEMail | This service is used by Windows CE / PC Runtime to send e-mails. |
| HTTP | 80* | TCP | Inbound | Hypertext Transfer Protocol | The HTTP protocol is used for communication with the HMI web server. |
| RFC 1006 | 102 | TCP | Outbound | S7 channel | Communication with the S7 controller via Ethernet/PROFINET. |
| NTP | 123 | UDP | Outbound | Time synchronization | The NTP protocol (Network Time Protocol) is used for time synchronization in IP-based networks. |
| DCOM*** | 135 | TCP | Inbound | OPC server | This service is a component of the Microsoft Windows operating system. Communication via OPC (DA) is based on DCOM. This service is therefore required to initialize OPC (DA) connections. |
| DCOM*** | ** | TCP | Inbound | OPC server | The communication via OPC (DA) is based on DCOM and uses unspecified ports assigned by the system. This should be taken into consideration when using OPC (DA) and creating rules for the firewall. |
| NetBIOS over TCP/IP | 137 | UDP | Outbound | With the use of Remote File Share | Register / log on to a remote server. |
| NetBIOS over TCP/IP | 138 | UDP | Outbound | With the use of Remote File Share | Register / log on to a remote server. |
| SNMP | 161 | UDP | Outbound | Simple Network Management Protocol | The SNMP client functionality is used by STEP 7 to read status information from PROFINET devices. |
| HTTPS | 443* | TCP | Inbound | Secure Hypertext Transfer Protocol | The HTTP protocol is used for communication with the HMI web server via Secure Socket Layer (SSL). |
| Modbus TCP | 502* | TCP | Outbound | Modbus TCP channel | The Modbus TCP protocol is used for connections to Schneider PLCs. |
| Mitsubishi MC | 1025* | TCP | Outbound | Mitsubishi MC channel | The Mitsubishi protocol is used for connections to Mitsubishi PLCs. |
| Printing | 1032 | TCP | Outbound | Printing | Printing on the control panel (via Ethernet). |
| HMI Load | 2308 | TCP | Outbound | Transfer | This service is used to transmit images and configuration data to panels. On Comfort Panels, this service has been replaced by DeviceManager and SCS as of V13. This service is used to transmit configuration data to WinCC Runtime Advanced. |
| HMI Load | 50523 | TCP | Outbound | Transfer | This port is used if port 2308 is not available.  This service is used to transmit images and configuration data to panels. On Comfort Panels, this service has been replaced by DeviceManager and SCS as of V13.  This service is used to transmit configuration data to WinCC Runtime Advanced. |
| ALM | 4410* | TCP | Inbound, Outbound | Application License Manager | This service of RT Advanced makes available the complete functionalities for software licenses and is used by the Automation License Manager. |
| OPC UA | 4870* | TCP | Inbound | OPC UA server | This service is required for communication via OPC UA. |
| HMI Load | 5001 | TCP | Outbound | Device Manager | This service is used to transmit images and Runtime to panels. |
| HMI Load | 5002 | TCP | Outbound | SCS (System Configuration Server) | This service is used to transmit configuration data to panels. |
| VNC client | 5500 | TCP | Outbound | Sm@rtServer | VNC client connection |
| VNC server | 5800* | TCP | Inbound | Sm@rtServer | VNC server connection HTTP |
| 5900* | TCP | Inbound | Sm@rtServer | VNC server connection |  |
| SIMATIC Logon | 16389* | TCP | Outbound | UMAC (User Management to the Access Control) | Register / log on to a remote server. |
| Allen Bradley Ethernet IP | 44818 | TCP | Outbound | Ethernet/IP channel | The Ethernet/IP protocol is used for connections to Allen Bradley PLCs. |
| Reserved | 49152 ... 65535 | TCP/UDP | Outbound |  | Dynamic port range is used, for example, to connect to the remote file sharing. |
| * Default port that can be changed by user configuration  ** Port is assigned automatically.  *** Supported by WinCC Runtime Advanced only. |  |  |  |  |  |

### Data protection

Siemens observes the data protection guidelines, especially the requirements regarding data minimization (privacy by design). This means the following for this SIMATIC product: The product does not process / save any personal information, but only technical functional data (e.g. time stamps). If the user links this data to other data (e.g. shift plans) or if the user saves personal information on the same medium (e.g. hard disk) and therefore creates a personal reference in the process, the user has to ensure meeting the guidelines regarding data protection.

### Notes on use

#### Contents

Information that could not be included in the online help and important information about product features.

#### Change in response after upgrading

The new WinCC version contains new features and improvements as compared to the previous version. The new version might therefore demonstrate slight differences in the names or the response of properties and functions after the upgrade. Unlike in previous versions, the standard properties of newly created objects can also be changed.

These differences in response can lead to errors when compiling the project.

#### **Upgrading user data types**

During an upgrade, only the user data types that are used in a project are upgraded.

#### Installation path

If you had the simulation installed in an earlier version, you cannot adjust the installation path during the installation.

#### Working with standard user rights

If you are working with standard user rights in Windows 7, "User Account Control (UAC)" must not be disabled.

The "User Account Control" is enabled in Windows 7 by default.

For more information on the "User Account Control", refer to the online help for Windows 7.

#### On-screen keyboard (RT Advanced)

Once you have opened TIA Portal, you can no longer access the on-screen keyboard.

To access the on-screen keyboard in Windows, use the following command: "Start &gt; All Programs &gt; Accessories &gt; Ease of Access &gt; On-screen keyboard".

#### Device change – character sets (RT Professional)

If you have configured different fonts on screen objects for multilingual texts in the various project languages, you should check the screens after an HMI device replacement from a panel to a PC-based runtime. The configured fonts might change if the device is replaced.

#### Texts in the simulation (RT Professional)

If a runtime language which does not correspond to an installed product language is used in the simulation, system texts are shown in an installed product language. Depending on the operating system and the installed product languages, this will be either English or Chinese.

If you wish to see all texts in Japanese, Korean or Taiwanese in the relevant language in the simulation, you should first install WinCC without simulation. Then install WinCC Runtime Professional with the required languages.

#### Online delta loading with user-defined cycles (RT Professional)

If you have configured new custom cycles in the "Cycles" editor, "Load &gt; Software (compile all)" command when loading the project. Online delta loading is not possible.

#### License transfer via S7USB

You always need to run WinCC to transfer a license to a panel via S7USB.

#### Transferring licenses to a panel on 64-bit operating systems

If you are running a 64-bit operating system and the "Edit &gt; Connect target systems &gt; Connect HMI device" menu command is not available in Automation License Manager, open command line input and run the following command with administrator rights:

"%WINDIR%\system32\RegSvr32.exe" "%CommonProgramFiles%\siemens\AlmPanelPlugin\ALMPanelParam.dll"

#### PostScript fonts

Only fonts that contain TrueType data can be used in TIA Portal. PostScript fonts and open type fonts that contain PostScript data are not supported.

#### Tasks with tag trigger

A task with tag trigger is executed when the value of the internal tag is written, even if the value of the internal tag does not change.

### Screens and Screen Objects

#### Contents

Information that could not be included in the online help and important information about product features.

#### Number of characters in text fields, lists and alarm texts

The number of characters that can be used in the text of a screen object is not constant. Control instructions and formatting are taken into consideration when entering text data and the maximum number of characters is reduced accordingly.

#### Screen objects after HMI device replacement

If you upgrade a device to the new HMI device versions, you should check the screens contained in the project. Because of the new appearance and improved operability, texts of symbolic I/O fields might not be completely legible and can be concealed by operator controls.

#### Updating faceplates with the UDTs of the type "IEC timer"

The "ST" element was automatically removed from the user-defined PLC data types (UDT) that use the "IEC timer" data type. Adapt the faceplates containing these UDTs to a new version of the UDT without an ST element.

A detailed description of this can be found in the FAQ with the entry ID "109740393" in the SIMATIC Customer Online Support.

#### Display differences between the configuration and the display on the HMI device

The display of the text configured in a screen object might be different on the HMI device due to the display configuration. If you are using the options for automatic size adjustment in the configuration, check the display on your HMI device in every language.

If texts that were configured with the "Fit object to contents" option cannot be displayed in full, they are reduced slightly on the HMI device. If this reduction leads to a distorted display of texts, disable the "Fit object to contents" option and expand the text with additional blanks. Optionally, you can increase the width of the object or use a shorter formulation for the text.

#### Dynamization of faceplates (RT Professional)

The dynamization of a faceplate instance with user data type connection is not intended, but can be realized in certain scenarios using an auxiliary tag. Read the information about this in [FAQ 109766634](https://support.industry.siemens.com/cs/ww/en/view/109766634).

Events cannot be dynamized at a faceplate instance via a function list or a C script.

When using a VB script, you must use SmartTag functions.

#### Dynamization of grouped objects (RT Professional)

For groupings with multiple nestings (group in group, faceplate in group, group in faceplate, etc.), only the events of the outermost group and the innermost objects can be used for dynamization with system functions. System functions that are configured at events of the lower-level group or lower-level faceplate are not executed.

The configuration of simultaneous motion animation of an object group within this group can be executed in runtime in a way other that what is expected. Check the sequence of the execution in runtime and adapt the configuration if necessary.

#### My controls

"My controls" might not be displayed correctly in the engineering system. However, they can be configured without restrictions. There are also no restrictions for the representation and operability in Runtime. If this control is based on OCX technology, a switch to .Net is recommended.

#### GRAPH overview (RT Professional)

When upgrading to V14, the signature of the C function at the "Click" event is changed. The propertyName parameter from the previous versions has been removed. Functions that access this parameter are shown as faulty after the upgrade.

#### Grouping of screen objects

When you group screen objects in WinCC, performance problems can arise in WinCC in the case of large nesting depths.

#### Multilingual graphics in faceplates

In a faceplate, insert a graphic in a screen object. This graphic is used in all specified project languages.

If you open the graphic using the shortcut menu command "Edit" with the option "Edit graphic centrally", the graphic is changed only for the currently set project language after editing and saving in an external editor, such as MS Paint. The change of the corresponding graphic is visible in all objects that use this graphic.

#### Network changes in the PLC code view (RT Professional)

When a ProDiag alarm is pending, network changes in the PLC code view are updated in runtime.

In order for network changes in the PLC code view to be displayed correctly for criteria analysis, the message must be triggered again.

#### PLC code view

When a ProDiag alarm is displayed, network changes in the PLC code display are updated in Runtime. In order for network changes in the PLC code display to be displayed correctly for criteria analysis, the alarm must be triggered again.

#### Fonts in the header of window objects (Panels, Runtime Advanced)

The font that you configure in the runtime settings of the device is not used in the alarm window, system diagnostics window and dialog headers.

#### Displaying SIMOTION PLC websites in the HTML browser

If the SIMOTION PLC websites are not displayed correctly in the HTML browser, insert "/basic" after the website URL to display the websites in basic mode.

#### System diagnostics view: "HMI access" access protection

When using the "HMI access" protection level in conjunction with the SIMATIC S7-1200 PLC, correct display of the diagnostic data can only be ensured as of firmware version 4.1.

#### Transparency in WinCC as of V13

Transparent graphics can be displayed without any problems in runtime. This is true for all Comfort Panels and WinCC Runtime Advanced as of version 13.0.  
To use the transparency in a graphic view or in a graphic I/O field, the "Fill pattern" property must be set to "Transparent" and the property "Use transparent color" must be disabled.

#### Higher-level controls with visibility animation

The higher-level configuration of table-based controls with visibility animation can lead to problems for touch operation with devices using the operating system Windows CE/Embedded Compact.

#### Invalid graphic types in graphic lists after upgrading (Runtime Professional)

When you upgrade your project to TIA Portal version V16, invalid graphic types in the graphic list result in compiling errors that were displayed as warnings in V14.

To avoid error messages during compiling, you need to correct the graphic type in the graphic list if necessary.

#### Many visually different screen objects

The use of screen objects with many visually different properties (e.g. many different styles) can reduce performance in runtime and can increase the amount of available memory space used. Avoid using, for example, very many different corner radii: 0 pixel, 1 pixel, 2 pixels, 3 pixels, etc.

#### Connection to Char data type

If you connect the I/O field to a controller tag of data type "Char", the following restrictions apply:

- The input accepts only digits: 0 … 9.

  The entered string of digits is converted to the corresponding character according to the ASCII table.

  Example: Input 6 + 5 becomes "A".
- Only enter digit sequences between 0 and 129.

To input alphanumeric characters directly, use the alternative data type "WChar", for example.

### Tags and connections

#### Contents

Information that could not be included in the online help and important information about product features.

#### Multiplexing tags (Basic Panels)

If you multiplex a tag with an external tag on a Basic Panel, the address is read from the PLC in runtime during the first read cycle. The value of the address read is not available until the second read cycle.

#### Tags with symbolic addressing and "Char Array" data type (RT Professional)

Tags with symbolic addressing and the "WString" data type are not released for communication of RT Professional and SIMATIC S7-1200 V3.

#### Length restriction for variable names (RT Professional)

The variable name must not exceed 128 characters.

#### Length specification for tags of the "String" type (RT Professional)

The length specification for the internal HMI tags of the "String" type have no effect in the "Tag" editor. If you want to limit the tag length of an input field or output field, for example, do so using VB scripting or C scripting.

#### Tag of the "String" type for connections with SIMOTION PLCs (Panels, RT Advanced)

The length of the String tags must not exceed 210 characters for SIMOTION controllers.

It is possible to create a String tab with more than 210 character in the engineering system. However, the tag in question is not written in Runtime. A message stating that the value limit is outside the tag is displayed.

In this case, adjust the length of the String tag.

#### Tags under "Tag box ID" (Mobile Panel)

The tag that you configure under "Tag box ID" with "Runtime Settings &gt; General" may only be used in read-only mode.

No values may be written in this tag, however, they may be read in scripts, for example, or output to screens.

#### Array elements in WinCC

If you have connected an HMI tag with an array from a STEP 7 data block which does not start with a low limit of 0, the array elements are mapped in WinCC to the low limit of 0.

To ensure that you do not have to rethink between the STEP 7 indices and the WinCC indices when accessing the individual array elements, the low limits of arrays should also start at 0 in STEP 7.

#### Using 64-bit data types

The use of 64-bit data types may result in a slight loss of accuracy as these data types are mapped in the HMI channel to the data type Double. It is possible that integer data types are displayed with decimal places.

#### System diagnostics of PLCs in the R/H system in non-redundant mode

Two PLCs and two corresponding connections are configured in an R/H system. If the R/H system is not in redundant mode, it may happen that the system diagnostics views of the connections show different diagnostics status symbols for the same PLC.

### Alarm system and alarm displays

#### Contents

Information that could not be included in the online help and important information about product properties.

#### Boolean tags in alarm logs

Bool type tags are recognized as 0 and -1 in the alarm log. If you use a text list that is controlled by a tag of the type Bool in an alarm log, then add the entry for the value -1 to the corresponding text list.

#### PLC alarms

A PLC alarm is only visible in the "Alarms" editor of an HMI device if there is an instance data block for this FB.

#### Controller alarms in runtime (WinCC Professional)

If you upgrade a project from versions V13SP1 or V13 SP2 to versions V14, V14 SP1, V15, V15.1, V16, you need to compile the project and load it in the controller and HMI device. Otherwise, the controller alarms are shown crossed out in the alarm view.

#### Copying projects with integrated connections

If you copy the devices with their integrated connections (between HMI devices and controllers) from a project to a global library and insert it from there in a new project, then the information about controller alarms can get lost on the HMI device. To avoid this loss of information, first copy all controllers and only then all HMI devices to the new project.

### System functions and scripts

#### Contents

Information that could not be included in the online help and important information about product features.

#### Simulation with script debugger

To start the "Simulation with script debugger" from TIA Portal, the registry key   
HKEY_CLASSES_ROOT\CLSID\{834128A2-51F4-11D0-8F20-00805F2CD064}\LocalServer32 must contain an entry "(Default)" of the type "String", which contains the whole path of the default script debugger "devenv.exe". The debugger can be connected to a simulation which is already running without this registry key.

#### Trigger tags of user-defined functions (RT Professional)

If you have configured an HMI or PLC user data type on a screen, you cannot use the elements of the user data type as trigger tags in newly created or changed user-defined user functions.

#### User-defined functions in faceplates

If you want to access tags in a faceplate with a user-defined function, you cannot dynamically compose the name of the tag.

#### System functions of the bit processing (Mobile Panels and RT Advanced)

Because of events it is not possible to manipulate bit arrays. System functions, e.g. InvertBit, SetBit etc., must not contain any elements of a bit array as argument.

#### Properties no longer used (Comfort Panels and RT Advanced)

In WinCC V13, many new visual properties have been introduced and many existing properties have been harmonized.

In the course of revision of the object properties, some properties that could be used in VB scripts in earlier versions of WinCC are no longer supported for use in WinCC V13. Scripts that use properties that are no longer supported remain valid, but the relevant calls within the scripts have no function. These limitations pertain exclusively to Comfort Panels and RT Advanced in device version V13.0.

The following table shows the properties of screen objects that are no longer being used:

| Property | Screen object |
| --- | --- |
| BorderBrightColor3D | Slider |
| BorderColor | Text field, I/O field, symbolic I/O field,  date/time field |
| BorderInnerWidth3D | Slider |
| BorderOuterWidth3D | Slider |
| BorderShadeColor3D | Slider |
| BorderStyle3D | Text field, I/O field, button, symbolic I/O field, graphic I/O field, date/time field, bar, switch |
| BorderWidth | Text field, symbolic I/O field |
| CenterColor | Gauge |
| DialColor | Gauge |
| EdgeStyle | Text field, I/O field |

#### Transferring parameters to VBScripts (Panels and RT Advanced)

In WinCC, you can define whether the parameters of VB scripts "ByRef" (address of the parameter) or "ByVal" (value of the parameter) are transferred.

Transferring the address of the parameter using "ByRef" (Call by Reference) is possible only for the internal tags of the VB script. With HMI tags, the value of the parameter is always transferred regardless of whether the parameter was defined as "ByRef" or as "ByVal".

#### Supply trend view by means of user-defined function

When you read values from a log with a VBS function to display them in a trend view, you must ensure that the difference between the time stamps is greater than zero.

#### Maximum number of parameters (Panels and RT Advanced)

The maximum number of parameters of a global function is 8 for the type "sub" and 7 for the type "func".

#### Scripts on the WebUX or WebNavigator server

C or VBS scripts triggered by services such as Global Script, Alarm Logging or Tag Logging are independent of Graphics Runtime and therefore run only on WebUX or WebNavigator servers.

- Any output of such functions, e.g. via printf() or HMIRuntime.Trace(), is not visible in the script diagnostics window on a WebUX or WebNavigator client.
- All accesses to Graphics Runtime from such functions are always made to the local Graphics Runtime of the WinCC server.

#### Addressing the "WaitForDocumentReady" function

When using the "WaitForDocumentReady" function, if you address the screen window via an absolute path, you must put a colon ":" at the end of the path.

Example: WaitForDocumentReady("Start.Picture:")

---

**See also**

[Debug](https://msdn.microsoft.com/en-us/library/wk3y866c(v=vs.84).aspx)
  
[Err](https://msdn.microsoft.com/en-us/library/sbf5ze0e(v=vs.84).aspx)

### Reports

#### Contents

Information that could not be included in the online help and important information about product features.

### Recipes

#### Contents

Information that could not be included in the online help and important information about product features.

#### Recipe synchronization (Basic Panels, Panels, Comfort Panels and RT Advanced)

When data record values are sent to the controller, the values are only validated if the "Manual transfer of individually modified values (teach-in mode)" option is selected for the recipe under "General &gt; Synchronization &gt; Settings".

#### Requirements for using recipes in redundant systems (Runtime Professional)

- Recipes are only synchronized if WinCC components are used, e.g. functions of the UA API, control tags, WinCC recipe control. Recipes are not synchronized if the data is accessed via ODBC, for example.
- For online synchronization, the "Last access" option must be selected in the Inspector window of the recipe under "System fields".

### User administration

#### Contents

Information that could not be included in the online help and important information about product features.

#### UMAC domain user

In WinCC V16.0, only local UMAC users may be used, no UMAC domain users.

### Communication

#### Contents

Information that could not be included in the online help and important information about product features.

#### Secure communication

Secure communication via the TLS protocol can only be established via integrated connections.

If you use Inter-Project Engineering (IPE) in your project, i.e. an HMI device is connected to a device proxy PLC, and an error message about inconsistent certificates appears during compiling, you need to correct the certificates of the associated PLC in the original project. Then you have to compile, export and re-import the PLC.

#### Establishing a connection to WinCC Runtime Advanced

Ensure that the device version configured in the Engineering System matches the installed Runtime version; otherwise, communication when the project is loaded will not be established or will be delayed.

If the device version does not match the installed Runtime version, you have the following options:

1. Change the device version configured in the Engineering System.
2. Install the version of WinCC Runtime Advanced corresponding to the configured device version.

#### Connection changing for non-integrated connections

If you want to change the communication from a non-integrated connection to another non-integrated connection, for example from Omron to Mitsubishi, you must ensure that the data types of the tags are also supported in the new connection.

#### Connection interruptions with Mitsubishi PLCs

After multiple connection interruptions, a situation might arise where all the connection resources of the Mitsubishi PLC are in use and the connection can no longer be established. We recommend that you check these connection resources in the PLC program of the controller and enable them again.

#### Self-signed certificates (RT Professional)

Self-signed certificates are no longer supported.

If a self-signed certificate is detected on the server side, the authentication takes place via the previously distributed PSK key (pre-shared key). If the PSK keys of the communication partners do not match, no communication is established.

#### Accuracy of the "DTL" data type

The "DTL" data type supports time information down to the nanosecond range. Because panels only support time information down to the millisecond, the following restrictions arise when used at the area pointers:

- Area pointer "Date/time"  
  For the transmission of time information from a panel to the PLC, the smallest unit of time is 1 millisecond. The value range from microseconds to nanoseconds of the "DTL" data type is filled with zeros.
- Area pointer "Date/time PLC"  
  For the transmission of time information from a PLC to a panel, the range from microseconds to nanoseconds is ignored. The time information down to and including milliseconds continues to be processed on the panel.

#### Limited number of possible HMI connections

An error message is displayed during compilation of a device indicating that the configuration of the HMI connection in the "Devices &amp; Networks" editor is invalid. The reason might be that the maximum number of possible connections of the HMI device or PLC has been exceeded.

Check the maximum number of available connections. Consult the device manuals of the devices you are using.

#### Use of PROFINET IO with panel HMI devices

When using PROFINET IO to connect the direct keys and LEDs of HMI devices to the PLC, you can define an offset for the address area of the inputs and outputs during configuration in HW Config.

The following restriction applies when a PROFINET IO-capable S7-400 CPU is used with one of the HMI devices listed below:

The offset for the start of the address area of the inputs must not be greater than the offset for the start of the address area of the outputs.

To configure the address parameters, open the PLC that contains the CPU of the 400 series in HW Config. Select the HMI device that is connected via PROFINET IO from the station window of HW Config. A table with the properties of the HMI device is displayed at the bottom of the station window in the detail view. Select the line containing the addresses of the HMI device in the table and open the object properties using the shortcut menu.

Enable the "Addresses" tab in the "Object properties" dialog. Configure the offset for the inputs under "Inputs &gt; Start". Configure the offset for the outputs under "Outputs &gt; Start".

#### RT Advanced communication via Station Manager (SIMATIC NET) with an S7-1200

For communication of a SIMATIC S7-1200 with a PC with WinCC RT Advanced via a router, the following restrictions apply to the PC:

- Windows 7: Only with installed SIMATIC NET 8.1

These restrictions also apply when you use the Station Manager. Connections with the help of the Station Manager of Runtime Advanced are always treated as routed connections.

#### Changing the IP settings and device name of a PLC in the Control Panel of the HMI device (Basic Panels)

The Control Panel is open in the "Service and Commissoning &gt; IP-Adaptation" menu on the HMI device. If you want to change the IP settings or the device name of a PLC, note:

In the Engineering System, you need to have selected the following options in the Inspector window of the PLC under "Properties &gt; General &gt; PROFINET interface &gt; Ethernet addresses":

- "Set IP address using a different method"
- "Set PROFINET device name using a different method"

#### "Set the IP suite (address) of the PLC in the Control Panel" with SIMATIC S7-1200 V1 (Basic Panels)

The function "Set the IP suite (address) of the PLC in the Control Panel" has not been approved for the following PLCs:

- SIMATIC S7-1200 V1

#### Connections via PROFIBUS DP

When a connection between a PLC and an HMI device via PROFIBUS DP is interrupted and then re-established, sporadically all other PROFIBUS DP connections in the communication network are interrupted and re-established.

De-energize the disconnected station before reconnecting it.

#### Switching a connection

A connection can be interrupted when it is switched from an HMI device to a SIMATIC S7-300/400, SIMATIC S7-1500 or SIMATIC S7-1200 controller.

Note the following settings in the SIMATIC S7-1500 or SIMATIC S7-1200 PLCs:

- Absolute addressing of tags
- The "Disable PUT-GET communication" option must be selected
- The "Complete protection" protection level must not be set

#### Communication of Runtime Professional with SIMATIC S7-1200

In productive operation, communication of WinCC Runtime Professional with SIMATIC S7-1200 is only released for single-station systems.

#### RT Advanced in the Station Manager

If RT Advanced and WinAC RTX use the same communication processor of a PC, HMI communication with SIMATIC S7-1200 and SIMATIC S7-1500 is not possible.

#### Raw data communication in redundant projects (RT Professional)

Simatic.NET, Named Connections and various communication blocks, such as BSEND/BRCV, for example, can only be used to a limited extent in a redundantly configured PC station because the connection parameters for the redundant partner server cannot be configured.

#### Non-integrated connection to a SIMATIC S7-1500 software PLC (RT Advanced)

A non-integrated connection between an HMI device and a SIMATIC S7-1500 software PLC is not supported in WinCC.

#### Transfer areas of the operating mode IO device and DP slave of the HMI devices

If you have activated the operating mode "IO device" or "DP slave" for HMI devices, no transfer areas should be added or deleted in the properties of the HMI device. If you have inadvertently deleted or added a transfer area, disconnect and reconnect the controller.

#### PROFIenergy communication

To set up PROFIenergy communication, contact Customer Support.

#### Number of SmartClient connections

Even if the Basic Panel allows an unlimited number of SmartClient connections, configuring a maximum of two connections is recommended. Any additional connection affects performance.

#### Integrated Web server: Communication via OPC UA

If the error message 8010_0000 occurs during the communication of the integrated Web server via OPC UA, check the length of the transmitted arrays. If arrays are to be transmitted via OPC UA, the array may only have a maximum of 20 elements.

#### Communication with controllers from third-party providers

For communication with controllers from third-party providers, HMI user data types do not support any settings with regard to offset.

### System-wide functions

#### Contents

Information that could not be included in the online help and important information about product features.

#### **Using system diagnostics in the device proxy**

To use the system diagnostics function in an IPE device proxy, for example, a system diagnostics view, insert the PLC alarms as content of a device proxy.

#### Initialize the device proxy with data from a project of the previous version

A device proxy cannot be initialized with the data from a project of the associated full version in a project with the Service Pack version.   
Upgrade the source project to the Service Pack version to initialize the device proxy in the target project with the data from the source project.

#### Import and export of library texts

The following objects are not supported when importing and exporting library texts:

- Import: Recipes, Recipe elements, Recipe data records, HMI alarms, Text list entries, Screens, Reports.
- Export: Text list entries, Screens, Reports.
- Import and export of library type "Screen".

### Compiling and loading

#### Contents

Information that could not be included in the online help and important information about product features.

#### Compiling and loading

If internal errors or warnings occur during compiling, compile the complete project using the command "Compile &gt; Software (rebuild all)" in the shortcut menu of the HMI device.

Before you start productive operation with your project, compile the entire project using the "Compile &gt; Software (rebuild all)" command from the shortcut menu of the HMI device.

If you are using HMI tags that are connected to control tags in your project, compile all modified blocks with the command "Compile &gt; Software" in the shortcut menu before you compile the HMI device.

#### Checking the address parameters

When an HMI device is compiled in the project tree with the command "Compile &gt; Hardware and software (changes only)" in the shortcut menu, the address parameters of the HMI device, such as the IP address, are not checked. If you want to ensure that the address parameters are checked as well, you will have to compile the HMI device using the "Compile" button in the "Devices &amp; networks" editor of the toolbar.

#### Error message when downloading data to the PLC

A panel and a PLC are connected and communicating with other.

If a tag is accessed while downloading data from the panel to the PLC, an error message is displayed on the panel.

#### Comfort panels as of device version 13.0: Backing up data while loading projects

If the transfer is interrupted for Comfort Panels with a device version 13.0 or higher, WinCC automatically ensures that no data is lost and that existing data is only deleted on the HMI device after complete transmission.

#### Displaying characters in transfer alarms

If characters are not displayed correctly in the transfer alarms during transfers to HMI devices with the device version V12 or older, please check the region and language settings in Windows. Set the corresponding language under "Language for non-Unicode programs".

#### Reducing the project size

When you compile your HMI device, an alarm appears informing you that the size of your project is approaching the system limits for the corresponding HMI device. In this case, perform a complete compilation of the software to reduce the project size. To do this, use the command "Compile &gt; Software (rebuild all)".

#### Transport password

The transport password protects other passwords from unauthorized access during loading in the target system. Therefore, the transport password is only prompted for if at least one other password – for example, an access password – has been defined.

---

**See also**

[Microsoft KB3083806](https://support.microsoft.com/en-us/kb/3083806)

### Runtime

This section contains information on the following topics:

- [Notes on operation in Runtime](#notes-on-operation-in-runtime)
- [Notes on operation of panels in Runtime](#notes-on-operation-of-panels-in-runtime)
- [Notes on operation of Runtime Advanced](#notes-on-operation-of-runtime-advanced)
- [Notes on operation of Runtime Professional](#notes-on-operation-of-runtime-professional)
- [Secure communication via certificate (RT Professional)](#secure-communication-via-certificate-rt-professional)

#### Notes on operation in Runtime

##### Contents

Information that could not be included in the online help and important information about product features.

> **Note**
>
> If Runtime is operated in Kiosk mode with disabled shortcut keys in full-screen, you should disable access to online help in the ActiveX controls, otherwise the operator can gain access to the operating system.

##### Focus in runtime

If you have configured a low-contrast combination of focus color and border color for an HMI device with version 12.0.0 or earlier, the focus may no longer be identifiable in runtime after you change the device version in the TIA Portal. Change one of the two colors.

##### Language behavior - Layout of on-screen keyboard

The layout of the on-screen keyboard does not change when you switch to a runtime language that is not installed for the keyboard layout.

In this case, the language setting for the keyboard remains set at the most recent valid language or the language setting for the default keyboard layout of Windows is used.

##### Tag values exceed the maximum length

You enter a character string in a string tag via an I/O field. If the character string exceeds the configured number of tags, the character string will be shortened to the configured length.

##### Empty alarm texts

Runtime is running with a project. The project is saved on a network drive.

In the event of interruptions to the network drive connection, Runtime may attempt to load alarm texts from the network drive.

In the event of disconnection, the alarm window or the alarm view remains empty.

To avoid this, copy the project to a local drive before the starting the project in Runtime.

##### Duration of log initialization (Panels, RT Advanced)

Initialization of the logs on some storage media can take up to 5 minutes. The successful completion of initialization is immediately confirmed by a system event. If there is no storage medium for logging when runtime starts, the appearance of the system event can also take up to 5 minutes.

##### Large logs delay the ending of runtime (Basic Panels 2nd Generation)

When very large logs are used, ending runtime can take a long time. Use segmented logs as an alternative to very large circular logs.

##### Slow reaction of SmartServer

The following programs may start and respond very slowly with Windows 7:

- HMI TouchInputPC
- SmartServer: &lt;Ctrl+Alt+Del&gt; shortcut in the logon dialog

The delay is caused by the callback for the Internet certificate validation.

Remedy:

You can find the following files on the product DVD under:  
Support\Windows\CRL_Check or CD_RT\ Support\Windows7\CRL_Check\ :

- DisableCRLCheck_LocalSystem.cmd
- DisableCRLCheck_CurrentUser.cmd

1. Run the "DisableCRLCheck_LocalSystem.cmd" file with administrator rights. Select the command "Run as administrator" from the shortcut menu of the file.
2. Reboot the PC.

If the problem persists, follow these steps:

1. Double-click the file and run the "DisableCRLCheck_CurrentUser.cmd" file with user rights.
2. Reboot the PC.

   > **Note**
   >
   > The callback for the certificate validation is disabled for all users or PCs. To restore the original state, perform the following files:
   >
   > - RestoreDefaults_LocalSystem.cmd
   > - RestoreDefaults_CurrentUser.cmd
   >
   > You can find the files in the following directory of the product DVD:
   >
   > - Support\Windows\CRL_Check or CD_RT\Support\Windows7\CRL_Check\

##### Ending screensaver on the Sm@rtServer

When the screensaver is active on the Sm@rtServer on the server HMI device, you require write access to the Sm@rtClient side in order to end the screensaver on the server HMI device.

##### Avoiding corrupt files during power failure

If a power failure occurs in Windows systems while the WinCC system is active, files may be corrupt or destroyed. Operation with the NTFS file system provides better security.

Secure, continuous operation is only ensured by using an uninterruptible power supply (UPS).

##### Variable fonts on HMI devices

Windows 10 supports variable fonts ("OpenType Font Variations") since version 1709. You can also use the variants of a variable font in the engineering system. The actual display in Runtime depends on the HMI device and the installation conditions:

- Basic Panels, Comfort Panels: Variable fonts are not supported. The basic version is always displayed.
- Runtime Advanced, Runtime Professional: Variable fonts are supported if at least Windows 10 Version 1709 is used as the operating system and the font is installed with administrator rights.

##### Deactivating NTLMv1 and SMBv1

The NTLMv1 and SMBv1 protocols can be disabled. Deactivating the protocols does not have any effect on the operation of WinCC Runtime Professional.

> **Note**
>
> **Security risk from NTLMv1 and SMBv1**
>
> Use of the NTLMv1 and SMBv1 protocols is a significant security risk. Communications in the network could be compromised, for example, by man-in-the-middle attacks.

Depending on the operating system, the procedure for deactivating protocols may differ.

##### Encryption with TLS

Always use the latest version of TLS. Disable older versions.

The use of older versions (TLS 1.0 and 1.1) is at your own risk.

#### Notes on operation of panels in Runtime

##### Contents

Information that could not be included in the online help and important information about product features.

##### Using the mouse wheel in Runtime

The use of the mouse wheel in Runtime is not supported on all panels.

##### Backup on the memory card of the PLC (Basic Panels)

Create the backup file "A.psb" on the memory card of the PLC. An error, for example a connection break, occurs when creating the backup.  
This will create a corrupt file on the memory card of the PLC. Such a file has "~$" as prefix.   
Delete the file with the prefix "~$" if you want to save a backup again under the same name "A.psb".

##### Panel Data Storage and S7-1500F (Basic Panels)

The "Panel Data Storage" PDS function cannot be used on Basic Panels in conjunction with S7-1500F when the password for the protection level "Full access incl. fail-safe" is used.

##### "Panel Data Storage" function (Basic Panels)

The "Panel Data Storage" (PDS) function provided by Basic Panels is only supported by SIMATIC S7-1200 as of firmware V4.0 and SIMATIC S7-1500. For the PDS function, the panel must be connected directly with the CPU and must not be connected via the CP.

##### Fonts with file extension ".ttx"

The fonts with the file extension ".ttx" are available on all panels and Runtime Advanced and can be correctly displayed on all devices, for example, the "WinCC_flexible_smart" font.

##### Mass data transfer with USB

If you have installed Windows 10 on the configuration PC, the "USB" transfer channel is not available.

This restriction applies to the following devices and tools:

- Basic Panels: KP300 Basic, KP400 Basic, TP1500 Basic
- WinCC Engineering System
- "ProSave" service tool

> **Note**
>
> The "USB" transfer channel remains available if Windows 7 is installed on the configuration PC.

**Solution**

Use other transfer channels to transfer the project data, such as the "Industrial Ethernet" or "PROFIBUS DP" channel.

##### Modifying the IP address and device name for Panels

On Comfort Panels, the IP address or the device name can be modified even during runtime.

On Basic Panels, modification of the IP address or the device name during runtime is not possible.

##### Status change of an alarm

In case of status changes of the alarm, the existing text lists and variable fields are updated, if necessary.

#### Notes on operation of Runtime Advanced

##### Contents

Information that could not be included in the online help and important information about product features.

##### Starting runtime

Only WinCC Runtime V17 can be started from the Engineering System. Other versions of WinCC Runtime can only be simulated.

##### Authorization for starting Runtime Advanced

On a computer running the Windows operating system, WinCC Runtime Advanced can only be started if a user starting runtime is a member and has the rights of the group "Siemens TIA Engineer".

##### Screen saver on computers with Windows 10

On a computer with Windows 10, an activated screen saver is no longer terminated when an alarm of the "error" class is output.

##### Windows 10 in tablet mode

It is not recommended to use Windows 10 in tablet mode.

When running applications in tablet mode in Windows 10, for example Runtime Advanced, Sinumerik Operate, etc., these applications are minimized after starting.

##### .Net-Controls in Runtime

If you have incorporated a .Net control in your project as "Custom .Net control", you have to copy the files belonging to these controls to the installation directory of WinCC Runtime, e.g. "C:\ProgramFiles\Siemens\Automation\WinCC RT Advanced". Otherwise, the control cannot be loaded in runtime.

##### Disabling automatic checking for software updates

If the Engineering System is installed together with Runtime on a PC, the operator gets notifications above software updates. For the system to run reliably on a multi-station system, the same software version must be installed on all PCs.

It is possible to disable the automatic checking for software updates and to thus improve performance.

To disable the automatic checking for software updates, go to "Settings &gt; General &gt; Software updates" and deactivate the "Check for updates daily" option.

##### Access to array variables via OPC

If you use WinCC Runtime Advanced as OPC UA server, reading array tags is only supported when the "OPC UA Server Array index range access" setting is activated.

Array variables can only be written if the OPC UA client supports the setting "Write array elements without IndexRange".

##### Autostart of Runtime Advanced with Open Controller

Autostart of WinCC Runtime Advanced cannot be configured with connected Open Controller.

Start Runtime manually or add "HmiRTM.exe" to the Windows Autostart folder.

##### Entry of LINT (Long integer) data type at an I/O field

If you have used a LINT data type at an I/O field and enter a floating-point number into the I/O field, then the decimal places are neglected.

##### Status change of an alarm

In case of status changes of the alarm, the existing text lists and variable fields are updated, if necessary.

#### Notes on operation of Runtime Professional

##### Contents

Information that could not be included in the online help and important information about product features.

##### User authorizations within the operating system

1. All user must be added to the "SIMATIC HMI" user group. This also applies to users who want to open WinCC projects remotely.
2. The storage folders of the projects must have the NTFS authorizations "SIMATIC HMI" with full access and "SIMATIC HMI Viewer" with read access. The authorizations must be inherited for all subordinate objects.

##### Locking shortcuts

If you want to lock shortcut keys in Windows, you must change the group policies in the administrative tools of the operating system.

A detailed description of this can be found in the FAQ with the entry ID "44027453" in the SIMATIC Customer Online Support:

[Internet: WinCC FAQ 44027453](http://support.automation.siemens.com/WW/view/en/44027453)

##### Undocked toolbars

If the setting "Always on Top" is used for the Windows taskbar, undocked toolbars can be hidden behind the Windows taskbar in Runtime. Follow the steps below to show the toolbars again:

1. Select the "Properties" command in the shortcut menu of the taskbar.
2. Disable "Keep taskbar on top of other windows".

##### Fault in the connection between the server and the client

If the connection between the server and client is faulty, check the settings of the PG/PC interface. TCP/IP(Auto) should not be used for the "Interface Parameter Assignment Used". Used fixed IP addresses instead.

##### Fault in the connection between the server and the client

If the computer is simultaneously used as a server with the engineering system and a client cannot establish the connection to the server, you should check the releases set on the server.

1. Exit Runtime on the server.
2. Select the command "Find computer..." in the shortcut menu of the network environment on the desktop of the server.
3. Enter the name of the server as the computer to be found.
4. Open the computer found to see the shared directories.
5. Remove all the releases that begin with "WinCC_Project_HMI". Information on this is available in the documentation for the operating system.

This malfunction is caused by the use of the command "Save as..." in conjunction with the startup of the Runtime of this new project. You can make copies of the projects for backup purposes using the "Save as..." command. You should, however, continue to work with the original project.

##### Starting WinCC Runtime Professional

If Engineering System and Runtime are operated on one computer, Runtime or simulation for a project opened in the Engineering System should only be started and ended using the TIA Portal. Other options, for example, the symbol in the taskbar information area, should not be used.

When you configure autostart on the client, you are required to enter the logon name and password for each registered server project. To assign each server a logon name, the entry of the respective project path must be confirmed with the "Apply" button. This means that you must enter a logon name and password twice for redundant or alternative projects.

##### Setting the services for the SQL server

In order to ensure the full functionality of the SQL server for WinCC and WinCC Runtime, you need to check the SQL server settings.

1. Start "Programme &gt; Microsoft SQL Server.. &gt; Configuration Tools &gt; SQL Server.. Configuration Manager" in the Start menu.
2. Click "SQL Server Services" in the tree.
3. Check the services "SQL Server (WinCC)", "SQL Server (WINCCPLUSMIG)" and "SQL Server Browser".   
   "Automatic" must be entered for "Start Mode".   
   "Log On As" must be entered for "LocalSystem" for "SQL Server (WinCC)".  
   "SQL Server Browser" must be entered for "LOCALSERVICE".  
   Change the settings, if necessary.
4. Click "SQL Server Network Configuration" in the tree.
5. Click "Protocols for WinCC".
6. Check the "TCP/IP" protocol. "Enabled" must be entered for "Status". Change the settings, if necessary.

##### "Report system error" in WinCC Runtime Professional

The "Report system error" functionality is limited in WinCC Runtime Professional in conjunction with an S7-300 or S7-400. In an alarm view, only one alarm is ever displayed for each diagnostics type. Alarms on other errors of the same diagnostics type are not displayed.

##### WinCC interface and 64-bit operating system

The open interfaces of WinCC Runtime Professional do not offer native 64-bit support. Runtime API, VBS and the WinCC OleDB provider are primarily affected by this. To be able to use WinCC interfaces with a 64-bit operating system, note the following:  
- VB scripts cannot be started by simply double-clicking. You must explicitly use the 32-bit version under "syswow64\wscript.exe".  
- .NET applications that use the WinCC API have to be explicitly compiled as 32-bit applications, not with "AnyCPU", but with "x86".  
- C++ applications must not be compiled as 64-bit applications.

##### Dynamic graphics in WinCCViewer RT

If you use dynamic graphics from a graphics collection, e.g. linked with scripts, these graphics are not updated in the WinCCViewer RT.

Select the "User-defined" option under "Runtime Settings &gt; Graphic Settings".

##### Runtime Professional: Loading a project without connection to the configuration PC

Before you begin to load a project on the operator station, backup data such as "User administration" and "Recipe data".

1. User administration data are overwritten by default.

   Therefore, configure two buttons in your project for exporting and importing the user administration with the system function "ExportUserManagement". The data only needs to be exported if you have made changes to the user view in Runtime.
2. In the "Load preview" dialog, specify whether recipe data should be overwritten when loading the project.

   You can save recipe data in the recipe view using the operator controls "Export log" and "Import log".

Note that the most recently imported or loaded data are used in Runtime.

##### Connection with S7-1200 in system diagnostics

Only a WinCC Runtime Professional HMI system can be connected with an S7-1200 (up to V3) when you use system diagnostics.

##### Disabling automatic checking for software updates

If the Engineering System is installed together with Runtime on a PC, the operator gets notifications above software updates. For the system to run reliably on a multi-station system, the same software version must be installed on all PCs.

It is possible to disable the automatic checking for software updates and to thus improve performance.

To disable the automatic checking for software updates, go to "Settings &gt; General &gt; Software updates" and clear the "Check daily for updates" check box.

##### Restriction in the online delta loading capability

When you replace a design, the online delta loading capability of the project is lost. TIA Portal does not output an error message in this case.

##### Screen objects in reports as PDF

The quality of the screen objects in the reports that you generate in Runtime as PDF files depends on the PDF printer drivers used.

##### Projects in Runtime after Windows 10 update

You have installed Windows 10 version 1709 on a PC with WinCC Professional V15 and a PC with WinCC Professional RT V15. You have performed a Windows 10 update to version 1803 on the Runtime PC. After the Windows 10 update, it may no longer be possible in Runtime to manually open a project loaded from the engineering system PC.

Remedy: Set the start type of the service for the WinCC SQL instance manually to "Automatic (Delayed Start)" and restart the system.

##### Memory requirement of logs

To calculate the memory requirement for alarms across all segments and for individual segments, you need information on how many alarms are received as average per second. The maximum memory requirement of an alarm of approx. 4000 bytes is taken into account. The following applies:  
Memory requirement = Number of alarms/s * 4000 bytes * 60 s/min * 60 min/h * 24 h/day * 31 days/month * y months.

The example is based on one alarm per second:

- The maximum size across all segments for 2 months is approx. 20 GB
- For a single segment it is approx. 330 MB per day

To calculate the storage requirements for data logs across all segments and for individual segments, you need information about how many values are logged per second and the average length of a process value. The following applies:  
Memory requirement = number of log values/s * x bytes * 60 s/min * 60 min/h * 24 h/day * 31 days/month * y months

The example is based on 750 log values per second:

- For process values with 16 bytes, this results in a memory requirement of approx. 60 GB
- For process value with 6 bytes, this results in a memory requirement of approx. 22 GB

##### Automatic logout on multitouch devices

To ensure that a configured automatic logout works on devices with a multi-touch screen even when using SIMATIC Logon V1.6 Update 3, configure any function, for example, to set a bit of a tag to the "Touched" event of the screen. This resets the logoff time timer when the screen is touched.

#### Secure communication via certificate (RT Professional)

Runtime Professional certificate-based communication has been enhanced.

##### Overview

**Supported S7 PLCs**

WinCC Runtime Professional can communicate with the following S7 PLCs via certificates:

- S7-1500 PLCs as of firmware 2.9
- S7-1200 PLCs as of firmware 4.5

> **Note**
>
> All of the following statements apply only to S7 PLCs with this firmware.

**Expansions**

Certificate-based communication between Runtime Professional and S7 PLCs has been enhanced as follows:

- Communication between HMI devices and S7 PLCs with a non-integrated connection now supports self-signed certificates.
- Upgrading S7 PLCs has been simplified. Upgrading in the TIA Portal is no longer mandatory.

  An S7 PLCs that was only upgraded in the field now communicates with the HMI device via a self-signed certificate. The self-signed certificate is automatically loaded from the PLC into the certificate store of the HMI device.

To use these functions, enable the "ForceSecure" option on the HMI device.

**Using self-signed certificates**

The following self-signed certificate options are available:

- Use a self-signed certificate generated in the TIA Portal.

  Use the certificate created automatically when adding an S7 PLC or upgrading an existing S7 PLC. Or select certificate settings that differ from the default settings and generate a self-signed certificate yourself.

  When loaded, the certificate is copied to the Runtime project folder.
- Use a self-signed default certificate.

  Do not provide a certificate for the PLC in the TIA Portal and instead enable the "ForceSecure" option on the HMI device for the PLC connection type.

  A self-signed certificate is generated when loading to the PLC. The certificate is copied to the certificate store of the HMI device during the first attempt to make a connection between the PLC and the HMI device. After the certificate is copied to the folder with trusted certificates, it is used for communication.

##### Enabling or disabling the "ForceSecure" option

**Introduction**

The "ForceSecure" option ensures that communication between the HMI device and the S7 PLC is protected by a certificate for the following connections:

- Non-integrated connections

- Connections for which no certificate has been configured in the TIA Portal

If the option is enabled and no PLC certificate is found in the Runtime project folder, Runtime searches for a suitable certificate in the "trusted" folder of the HMI device's certificate store.

> **Note**
>
> This option does not affect communication with S7 PLCs that do not support certificates.

**Default setting**

This option is disabled by default for integrated connections, non-integrated connections and device proxies.

**Procedure**

> **Note**
>
> It is recommended to enable the option for all connection types.

To configure the option for an HMI device, proceed as follows:

1. Create the "ForceSecure.xml" file.
2. Copy the following XML structure into the file:

   `<?xml version="1.0"?>`

   `<root>`

   `<NonIntegrated>true</NonIntegrated>`

   `<Integrated>true</Integrated>`

   `<IntegratedProxy>true</IntegratedProxy>`

   `</root>`
3. To disable certificate store evaluation for one of the connection types, set its node to "false".

   > **Note**
   >
   > Certificate-protected communication for non-integrated connections is not possible in this case.
   >
   > For integrated connections and device proxy, certificate-protected communication is possible only after upgrading the PLCs in the TIA Portal.
4. Copy the file on the engineering device into the TIA project directory of the project to which the HMI device was added into the following folder:

   "`…\AdditionalFiles\Rdp`"
5. Compile and download the HMI device.

   Your settings will be applied to the communication between the HMI device and its connected S7 PLCs.

To configure the "ForceSecure" option centrally for all projects created in the TIA Portal, proceed as follows:

1. Perform steps 1 to 3 as described above.
2. Copy the file on the engineering device into the program directory "C:\ProgramData\Siemens\Automation\ConfigFiles\RDP".
3. To use a different configuration for individual projects, proceed as described in steps 1 to 4 above.

If the XML file is located in the program directory and in the TIA project directory, the configuration from the project directory takes effect.

##### Upgrading S7 PLCs

The following options are available when using self-signed certificates.

**Upgrading in the field without upgrading the S7 PLC in the TIA Portal**

Requirement:   
On the HMI device connected to an S7 PLC, the "ForceSecure" option is enabled for the S7 PLC connection type.

Procedure:

1. Upgrade the HMI device in the TIA Portal.
2. Replace the S7 PLC and the HMI device in the field.
3. Download the S7 PLC and the HMI device.

   After the download, the Runtime project folder does not contain a certificate for this S7 PLC.
4. Start Runtime.

   At the first attempt to make a connection, the self-signed certificate is automatically loaded from the S7 PLC. It ends up in the certificate store of the HMI device in the following folder:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\untrusted`
5. Copy the PLC certificate in the certificate store of the HMI device to the folder with the trusted certificates manually or per script:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\trusted\certs`

**Upgrading in the field and upgrading in the TIA Portal**

Procedure for integrated connections and device proxy:

1. Upgrade the S7 PLC and HMI device in the TIA Portal.
2. Replace the S7 PLC and the HMI device in the field.
3. Download the S7 PLC and the HMI device.

   After the download, the Runtime project folder contains the certificate for this S7 PLC.
4. Start Runtime.

   HMI device and PLC trust each other's certificates. There are no further steps for you.

Procedure for non-integrated connections:

1. Upgrade the S7 PLC and HMI device in the TIA Portal.
2. Enable the option "ForceSecure" for the non-integrated connection type for the HMI device.
3. Replace the PLC and the HMI device in the field.
4. Download the PLC and the HMI device.

   After the download, the Runtime project folder does not contain a certificate for this S7 PLC.
5. Start Runtime.

   At the first attempt to make a connection, the self-signed certificate is automatically loaded from the S7 PLC. It ends up in the certificate store of the HMI device in the following folder:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\untrusted`
6. Copy the PLC certificate in the certificate store of the HMI device to the folder with the trusted certificates manually or per script:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\trusted\certs`

   HMI device and PLC trust each other's certificates.

Alternatively, you can export the PLC certificate from the TIA Portal in advance and copy it to the "`...\trusted\certs`" folder before starting Runtime. The certificate file must have the following name:

"S7PlusChannel_&lt;PLC_IP&gt;.der", e.g. "S7PlusChannel_192.168.0.1.der"

### Add-ons

This section contains information on the following topics:

- [Sm@rtServer](#smrtserver)
- [Audit](#audit)
- [DataMonitor](#datamonitor)
- [WebNavigator](#webnavigator)
- [Redundancy](#redundancy)
- [SIMATIC Information Server](#simatic-information-server)
- [WebUX](#webux)

#### Sm@rtServer

##### Content

Information that could not be included in the online help and important information about product features.

##### Opening SmartClient *.sac files under Windows 10

You save the data of the current SmartServer connection using the executable file SmartClient.exe with the *.sac format. To open the files generated in this way automatically under Windows 10, a *.sac file with SmartClient.exe must be opened once manually via the selection button and dialog in SmartClient.exe.

#### Audit

##### Contents

Information that could not be included in the online help and important information about product properties.

##### WinCC Audit Viewer 7.2 Update

An update for manual installation is available for WinCC Audit Viewer 7.2, which can be installed optionally.

Install the update for WinCC Audit Viewer 7.2 by running the "AuditViewer_V72_00_Upd1.exe" file from the Support directory on the product DVD.

#### DataMonitor

##### Contents

Information that could no longer be included in the online help and important information about product features.

##### Removal of WinCC Runtime

If you also want to use DataMonitor after removing WinCC Runtime Professional, you have to perform a repair of the installation as follows:

1. Open the Control Panel.
2. Double-click on "Add/Remove Programs".
3. Select "SIMATIC WinCC/DataMonitor client" in the list of programs installed
4. Click on the "Change/Remove" button.
5. Select the "Repair" setting in the WinCC/DataMonitor setup.

##### Excel Workbook on a PC with Windows 7

If you use Excel Workbook on a PC with Windows 7, you must disable the "Aero Glass" display mode.

##### Working with reports: Excel workbooks

If you want to make an Excel workbook available as the reporting tool or want to create a report with an Excel workbook, the file size of the Excel workbook must be smaller than 4 MBytes.

##### Time zone of Web parts

When you create and configure a Web part in a specific time zone in the Web center, the time zone is stored in the Web center.

If the time zone is changed in the operating system, this can lead to an incorrect display of the time in the Web part.

#### WebNavigator

This section contains information on the following topics:

- [General information about WebNavigator](#general-information-about-webnavigator)
- [Notes on WebNavigator installation](#notes-on-webnavigator-installation)
- [General notes on WebNavigator client](#general-notes-on-webnavigator-client)
- [Notes on Internet Explorer for WebNavigator](#notes-on-internet-explorer-for-webnavigator)

##### General information about WebNavigator

###### Introduction

These release notes contain important information.

The statements in these release notes take precedence over information provided in the manuals and in the online help.

Read these release notes carefully as they contain useful information.

###### Notes on the security of the system

**Cybersecurity information**

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept.

Siemens’ products and solutions constitute one element of such a concept.

You can find additional information about industrial cybersecurity under:

- AUTOHOTSPOT

###### Security restrictions with the WebNavigator client

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security restrictions and response times in Internet Explorer**  Please note the Internet-specific security restrictions when using the WebNavigator client.  The WebNavigator client may take significantly longer (&gt;20 seconds) than a regular WinCC client to recognize that the WebNavigator server is down or that the communication is faulty. |  |

###### Using a secure connection via HTTPS

To increase the security of your communication, configure the WebNavigator server in such a way that only HTTPS connections are supported.

You need a digital certificate for the WebNavigator server for this. Also use the SSL certificate on the WebNavigator client.

You can find more detailed information under "Setting up a secure connection via HTTPS".

###### Communication via proxy server

When communicating through a proxy server, the following applies:

- The WebNavigator client must be a member of the server domain.
- If the users registered on the WebNavigator client have no access to the proxy server, logon to the proxy server with NTLM authentication is as follows:

  1. The logon dialog for the proxy server appears.

  2. The logon dialog for the WinCC user appears.

  3. The logon dialog for the proxy server appears again.

###### Avoid cross-site request forgery for the WebNavigator

Cross-site request forgery is similar to the vulnerability caused by cross-site scripting (XSS, Cross Site Scripting).

The attack is triggered when an authenticated user clicks on a malicious link. However, this vulnerability also works if the user has disabled scripting in the browser.

Siemens recommends:

- Do not work with other applications or services that have anything to do with the Internet.
- Log off when you no longer need the WebNavigator.

###### Defense in depth

Follow the instructions on "Industrial Cybersecurity" on the Siemens website:

- AUTOHOTSPOT

###### WebNavigator server: Do not configure the standard port "80"

When configuring the port in the WinCC Web Configurator, use "8080", for example, rather than the standard port "80".

###### General information about WebNavigator

###### Project Change

Following a change of projects, a sporadic inoperable period of the Internet Information Services (IIS) may occur.

The computer must then be restarted.

###### Terminal server: Login with user certificate

The following group policy affects the logon behavior of a user with a user certificate:

| Local group policy | Setting |
| --- | --- |
| Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Local Policies &gt; Security Options:  "System cryptography: Force strong key protection for user keys stored on the computer" | User must enter a password each time they use a key |

This setting can cause the password prompt for the user certificate to be displayed in the session of another logged-on user when the terminal session is established.

**Corrective measure**

To prevent this Windows behavior, use the default setting "Not defined" on the system that is used as the terminal server.

This behavior occurs only when this group policy is activated.

###### Custom ActiveX controls (Industrial X)

Compatibility with WinCC and WebNavigator server or WebNavigator client must be ensured if custom ActiveX controls (Industrial X) are used:

- Direct installation of the ActiveX control on the computer with WinCC and WebNavigator server or client.

  You must install the ActiveX control before installing WinCC and the WebNavigator server or client.

  If the ActiveX control does not function without errors after this step, there is no compatibility.
- Installation as a plug-in via the Web Navigation user interface on the WebNavigator client.

  If the ActiveX Control is packaged in a plug-in and installed via download, an upgrade of WinCC and the WebNavigator server or client will also require the generation of a new plug-in using this ActiveX control.

  Ensure compatible binaries (DLL, OCX, etc.) are used when creating the plug-in.

**Visual C++ Redistributable for Visual Studio**

Microsoft Redistributable Packages for Visual Studio C++ 2015 are installed along with WinCC.

For example, if you are using ActiveX controls or Visual Basic projects created with versions prior to Visual Studio 2015, you must install the corresponding package.

The installation files for redistributables &lt; Visual Studio 2015 are included in the WinCC scope of delivery:

- "Additional Content" DVD:

  "VCRedist" folder

Select the setup for the required version:

- 2005x86 / 2005x64
- 2008x86 / 2008x64
- 2010x86 / 2010x64
- 2012x86 / 2012x64

##### Notes on WebNavigator installation

###### Notes on installation

###### Uninstalling WinCC: WebNavigator client must be installed later

If you uninstall WinCC, you will need to post-install the WebNavigator client.

###### Message after installation of a plug-in

The Program Compatibility Wizard may possibly output an message during installation of a plug-in.

The plug-in is installed correctly.

Therefore, confirm this message with "The program was installed correctly."

###### WebNavigator client: WinCC Computer with "Basic Process Control"

The plug-in "WinCC Basic Process Control" must be installed on the WebNavigator client if the client is connected to a computer with WinCC Basic Process Control.

Without the plug-in, the functionality of WinCC Basic Process Control will not be available on the WebNavigator client. For example, the relevant ActiveX controls and the group display will not be available.

**Installing the plug-in**

The plug-in is located on the WebNavigator server in the folder &lt;wincc_installationpath&gt;"\WebNavigator\Server\Web\Install\Custom".

You can download the plug-in via the WebNavigator navigation user interface from the download area.

A description of the functions supported/not supported can be found in the WinCC Information System:

- "Options for Process Control &gt; Overview of process control system options &gt; Configuration in the PCS 7 environment &gt; Web client"

**Dedicated Web server with WinCC Basic Process Control**

If the WebNavigator client is to be installed on a dedicated web server with WinCC Basic Process Control, the plug-in "WinCC Basic Process Control" must be installed immediately after installation of the WebNavigator client.

The download page for the plug-in is displayed. You will only be able to exit this page after installation of the plug-in for displaying the process pictures.

For more information on the supported functionalities of the WebNavigator client when connected to a PCS 7 OS, please refer to the PCS 7 documentation.

###### WebNavigator server: User WNUSR_DC92D7179E29

After the installation of the WinCC/WebNavigator server, the user "WNUSR_DC92D7179E29" is created during the initial configuration with the WinCC Web Configurator.

The user is only used internally. To maintain the functioning of the Web server, do not delete or modify this user.

To increase the security of the system, change the password for the user on a regular basis. To do this, use the tool "CCSetWebNavPwd.exe".

You can find more information in the documentation for WinCC/WebNavigator:

- "WinCC/WebNavigator Documentation &gt; Configuring the WebNavigator system &gt; Configuring the WebNavigator Server &gt; Configuring the WebNavigator web page &gt; WinCC Web Configurator"

**Setting a password for the configuration**

To define your own password before configuration, you can create a temporary key in the PC's registry.

You can find more information in the "Industry Support Siemens".

##### General notes on WebNavigator client

###### Notes on the web client

###### Security restrictions with the WebNavigator client

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security restrictions and response times in Internet Explorer**  Please note the Internet-specific security restrictions when using the WebNavigator client.  The WebNavigator client may take significantly longer (&gt;20 seconds) than a regular WinCC client to recognize that the WebNavigator server is down or that the communication is faulty. |  |

###### Windows Server operating system: Loading process pictures in WinCCViewerRT

It is possible that the web client does not display any process pictures in WinCCViewerRT on PCs with the "Windows Server 2016 / 2019 / 2022" operating systems.

Check the settings of the web client:

1. To display the icons in the control system, select, for example, "Small icons" in the "View by" drop-down list.
2. Click the "Internet options" entry.

   The property dialog opens.
3. Deactivate the following entry in the "Advanced" tab in the "Security" area:

   - Do not save encrypted pages to the disk
4. Close the dialog with "OK".

**Changing setting via group policy**

If you manage the web clients via group policies, follow these steps:

1. To open the editor for local group policies, enter "gpedit.msc" in the Windows search field.
2. Select the following entry in the navigation area:

   - Computer configuration &gt; Administrative templates &gt; Windows components &gt; Internet Explorer &gt; Internet control system &gt; "Advanced" Page

   To sort the list alphabetically, click the column header "Setting".
3. Double-click "Do not save encrypted pages to disk".
4. Select the "Disabled" or "Not Configured" option.
5. Close the dialog with "OK".

###### WebNavigator client: Firewall settings for printing from WinCC controls

To be able to print out on the client, you need to define the following Firewall settings for the profiles used:

1. Open "Control system &gt; System and security &gt; Windows firewall".
2. In the navigation bar, click "Allow a program or feature through Windows Firewall".
3. In the "Allowed programs and features:" list, activate the entry "File and printer sharing" for the relevant profile.
4. Return to the Windows Firewall start page.
5. In the navigation bar, click "Turn Windows Firewall on or off".
6. If the firewall is enabled, disable the setting "Block all incoming connections, including those in the list of allowed programs".

###### WebNavigator client: ODK function "PWRTCheckPermissionOnPicture"

In order to use the ODK function "PWRTCheckPermissionOnPicture" on a WebNavigator client, install the plug-in "WinCC Basic Process Control" and "Advanced Process Control".

###### WebNavigator client: WinCC Alarm Control on a WebNavigator server in WinCC ServiceMode

**Initial Situation**

The WebNavigator client is connected with a WebNavigator server operated in WinCC ServiceMode.

**Behavior**

If you are using WinCC Alarm Control prior to WinCC V7 that is connected via a server prefix, you will not be able to open the selection dialog.

**Solution**

Use the WinCC AlarmControl that is offered as of WinCC V7.

###### WebNavigator client: Diagnostics file "WebNavReconnnect.log"

After installation of the WebNavigator client, the diagnostics file "WebNavReconnnect.log" is saved in the folder "&lt;User&gt;\Application Data\LocalLow\Siemens\SIMATIC.WinCC\WebNavigator\Client".

The diagnostics file will be saved into the respective user profile so that this user no longer requires administrator rights.

###### WebNavigator client: Control "WinCC Channel Diagnosis"

You cannot use the "WinCC Channel Diagnosis" Control on a web client without WinCC installation.

###### WebNavigator client: "FLAG_COMMENT_DIALOG" of the "GCreateMyOperationMsg" function

The WebNavigator client does not support the parameter "FLAG_COMMENT_DIALOG" for the "GCreateMyOperationMsg" function.

###### WinCC/ODK: SSMRT functions in the web client

The "SSMRT" functions of the Split Screen Manager do not work in the WebNavigator client.

Instead, use the appropriate "SSM" function.

The "SSMRTOpenTopFieldEx" ODK function is not available in the WebNavigator client.

**Example**

The following script checks the environment and can thus be called in the WebNavigator client and in WinCC Runtime.

void OnClick(char* lpszPictureName, char* lpszObjectName, char* lpszPropertyName)

{

    #pragma code("ssmrt.dll")

        #include "ssmrt.h"

    #pragma code()

    char szFullTopfieldPath[MAXFULLPATHLEN] = { 0 };

    long lBufferLen = MAXFULLPATHLEN;

    OPENTOPFIELDSTYLE MyStyle;

    CMN_ERRORA Err;

    BOOL bResult;

    DWORD dwTopfieldStyle = 0;

    long lTopfieldUsed;

    #ifndef RUN_ON_WEBNAVIGATOR

        MyStyle.bAdaptSize = TRUE;

        bResult = SSMRTOpenTopFieldEx (SSMGetScreen(lpszPictureName), "PictureA.pdl", szFullTopfieldPath, lBufferLen, &amp;MyStyle, &amp;Err);

    #else

        // Declaration of _SSMOpenTopField3:

        //     BOOL _SSMOpenTopField3 (TCHAR Screen, TCHAR* PictureName, DWORD dwStyle, TCHAR* retPictureName, DWORD dwReturnPathLen, long* plTopfieldUsed, LPCMN_ERROR Err, long lXPos, long lYPos, BOOL bDefaultPos)

        // dwTopfieldStyle can be 0, TOP_FIELDFIXEDSIZE, TOP_ATTACHTOWORKFIELD, or TOP_FIELDFIXEDSIZE + TOP_ATTACHTOWORKFIELD

        dwTopfieldStyle = TOP_FIELDFIXEDSIZE;

        bResult = _SSMOpenTopField3 (SSMGetScreen(lpszPictureName), "PictureA.pdl", dwTopfieldStyle, szFullTopfieldPath, lBufferLen, &amp;lTopfieldUsed, &amp;Err, 0, 0, TRUE);

    #endif

}

clipboard

##### Notes on Internet Explorer for WebNavigator

###### Notes on Internet Explorer

###### Security settings in Internet Explorer: Installation via SSL connection

If you want to download the WebNavigator from an ASP portal via an SSL connection, note that the download is not possible under certain conditions.

You can correct this with one of the following settings:

- Deactivate the "Do not save encrypted pages to disk" option in the "Advanced" tab for the Internet options of the Internet Explorer.
- Deactivate the "Internet Explorer Enhanced Security Configuration" option in the "Control Panel/Add/Remove Programs/Windows Components".

###### WebNavigator server: Display virtual folder in Internet Explorer

Note the following when using Internet Explorer as WebNavigator browser:

To add a virtual folder to an existing website, create this website in a subdirectory of the drive.

When the website is created in the root directory, e.g. under D:\, Internet Explorer may not show the contents of the virtual folder.

To always display the contents, change the .NET settings in the IIS:

1. Open the Internet Information Services (IIS) Manager.
2. In the navigation, click on the entry "Application pools".
3. In the shortcut menu of "WebNavigatorAppPool", select the "Basic settings" entry.
4. In the ".NET CLR version" list, select the .NET version "v2", for example:

   ![WebNavigator server: Display virtual folder in Internet Explorer](images/123688955531_DV_resource.Stream@PNG-de-DE.png)

###### WebNavigator client: Display of ActiveX controls in Internet Explorer

ActiveX controls are disabled in Internet Explorer by default.

For this reason, the WinCC controls are not displayed correctly in Internet Explorer on a WebNavigator client.

To display the WinCC controls correctly, add the Web server as a trusted website and enable the ActiveX controls only for the "Trusted sites" zone.

To continue protecting Internet Explorer from foreign ActiveX controls, check that the restricted security settings still apply to the other zones after making the changes.

For more information, refer to the following documentation:

- WinCC/WebNavigator: "WinCC/WebNavigator Installation Notes &gt; Installation of WebNavigator Client &gt; AUTOHOTSPOT"

###### WebNavigator client: Updating pictures with faceplates

To display changed faceplates in process pictures, refresh the view of the web client in the browser, e.g. with &lt;F5&gt; or using the ![WebNavigator client: Updating pictures with faceplates](images/152318311947_DV_resource.Stream@PNG-de-DE.png) button.

#### Redundancy

##### Contents

Information that could not be included in the online help and important information about product features.

##### Name in configuration of a redundant system

Only the computer name of the HMI devices is relevant for the configuration of a redundant system. You set the computer name of the HMI device in its operating system. The name of the HMI device from the project tree is only used for identification of the HMI device in the project.

#### SIMATIC Information Server

##### Contents

Information that could not be included in the online help and important information about product features.

##### Installation of SIMATIC Information Server and WinCC Runtime Professional on one PC

To set up the SIMATIC Information Server and WinCC Runtime Professional on one PC, adhere to the following installation sequence:

1. Install WinCC Runtime Professional.
2. Install the Information Server.

If you do not follow the installation sequence, connection problems may occur.

#### WebUX

##### Contents

Information that could not be included in the online help and important information about product features.

##### Functional scope

The following functions are supported for WebUX:

- C scripts
- Local session tags
- Faceplates
- Alarm filters in the alarm view

### Migration

#### Contents

Information that could not be included in the online help and important information about product features.

#### Migrating a project created with WinCC V7

A prerequisite for the migration is that this project was processed with at least WinCC V7.5 Update 3.

#### Progress bar

As long as the progress bar still shows a value of 100%, the software is still busy running remaining tasks such as the closing of references. The software will not respond to user input while this status is given.

### HMI devices

This section contains information on the following topics:

- [Notes on HMI devices](#notes-on-hmi-devices)
- [Notes on Basic Panels](#notes-on-basic-panels)
- [Notes on Mobile Panel](#notes-on-mobile-panel)
- [Notes on Comfort Panels](#notes-on-comfort-panels)

#### Notes on HMI devices

##### Contents

Information that could not be included in the online help and important information about product features.

##### Unsupported HMI devices (as of TIA Portal V15)

All HMI devices with version 11.x are no longer supported as of TIA Portal V15.

The following HMI devices are no longer supported as of TIA Portal V15:

- WinAC MP 177, WinAC MP 277, WinAC MP 377
- Panels: OP and TP of the 70 series, 170 series and 270 series
- Multi Panels: Multi Panels of the 170 series, 270 series and 370 series

In order to use other devices in TIA Portal V15, for example Basic, Comfort or Mobile Panels, that have been configured with version 11.x, change the device version of the device in question.

The storage structure in the installation directory also no longer contains data for 11.0. This helps to reduce the size of the TIA Portal installation package compared to the previous versions.

##### Unsupported HMI devices (as of TIA Portal V15.1)

The following HMI devices are no longer supported as of TIA Portal V15.1:

- WinCC Runtime Advanced V11

##### Unsupported HMI devices (as of TIA Portal V16)

The following HMI devices are no longer supported as of TIA Portal V15.1:

- Mobile Panel with device version 12.x
- Comfort Panel with device version 12.x
- KP1500 Comfort with device version 13.x
- TP1500 Comfort with device version 13.x
- TP1900 Comfort with device version 13.x
- TP2200 Comfort with device version 13.x

##### Multi-key operation

Unintentional actions can be triggered by multi-key operation:

- When you are using a key device, you cannot press more than two function keys at the same time.
- When you are using a touch device, a standard PC or a panel PC, you can only press one function key or button at the same time.

##### HMI devices with high communication load

S7 Diagnostics should be enabled if a Panel is assigned many connections to PLCs or other HMI devices. Otherwise, you will risk overloading the panel.

##### Simulation with real PLC connection

The access point used by the simulation is independent from the settings of the engineering system and can only be altered in the Control Panel with the "Setting PG/PC Interface" tool. If the PLC connection is terminated right after the start of the simulation with alarm 140001, you should check the access point used by the simulation with "Setting PG/PC Interface".

1. Double-click "Setting PG/PC Interface" in the Control Panel. A dialog opens.
2. Select "S7ONLINE" in the "Access point of application" field as standard for HMI.
3. Select the interface in the "Interface Parameter Assignment Used" area.
4. Exit the "Set PG/PC Interface" dialog with OK.

##### HMI devices with operating system Windows CE 5.0 or higher

Owing to a modified client-server communication security setting, the time difference between the HMI device (client) and PC (server) must not exceed 1 day. If you back up recipe data from the HMI device on a network drive, for example, make sure that the time is set correctly on the PC (server) and the HMI device (client).

##### Installing fonts

If you have installed new fonts on a panel with ProSave, you will need to restart the panel. The duration of the runtime startup process depends on the number and size of fonts.

---

**See also**

[PI Mobile](https://support.industry.siemens.com/cs/ww/en/view/109758056)

#### Notes on Basic Panels

##### Contents

Information that could not be included in the online help and important information about product features.

##### Simulation of the Basic Panels

Use an output field in an alarm text to output an external tag. The content of this output field will then always be displayed with "0" during simulation.

##### Simulation of Basic Panels 2nd Generation

3D hardware acceleration of the graphics card should be enabled for simulating the Basic Panels 2nd Generation.

##### Connection switch in the Control Panel with Basic Panels

If you use the "Override protected connection information" function, the following restriction applies:

You cannot perform a connection switch in the Control Panel of a Basic Panel from a PLC without a protection level to a PLC with a "Complete protection" level.

##### Basic Panels 2nd Generation

Basic Panel 2nd Generation support the Sm@rtServer option.

If you are not using a USB hub, select the USB port USB_X60.1 as storage path.

Even if you do not need a license for the Sm@rtServer option on a Basic Panel 2nd Generation as of WinCC V17, the "Load preview" dialog will display a note indicating a missing license under certain circumstances.

##### DHCP on KTP 400 PN, KTP 700 PN and KTP 900 PN

Operation with DHCP is not recommended for the KTP 400 PN, KTP 700 PN and KTP 900 PN devices.

In some circumstances, it is possible that the device will no longer boot. If that is the case, detach the network cable and reboot the device. After successfully startup, assign a fixed IP address.

##### Dynamic parameters in text lists

Dynamic parameters in text lists are not supported with Basic Panels.

#### Notes on Mobile Panel

##### Contents

Information that could not be included in the online help and important information about product features.

##### Printing alarms

It is not possible to print alarms as PDF or HTML when the internal memory "/flash" is selected as "Storage Location". To print alarms as PDF or HTML, select an SD memory card or a USB stick as storage location.

##### Mobile Panel

Mobile Panels 2nd Generation can be configured with TIA Portal V16 in the device version V15. The compiled project cannot be downloaded to these devices, however.

To work with Mobile Panels 2nd Generation in TIA Portal V16, an upgrade to at least device version V15.1 is necessary.

##### Sm@rtServer with Mobile Panels

The evaluation of the safety operation via PROFIsafe is only guaranteed if the Sm@rtServer is disabled on the panel.

The use of Sm@rtServer on devices without a safety function is not recommended.

#### Notes on Comfort Panels

##### Contents

Information that could not be included in the online help and important information about product features.

##### Interruption of the DH485 connection

If you connect the Ethernet cable to the "PN_X1" connector of the HMI panel with Comfort Panels, the DH485 connection might be interrupted.

Remedy for Comfort Redesign/PRO Panels: When running the DH485 project on the HMI Panel, use the connector "PN_X3(Gigabit)" for Ethernet communication.

##### VB function "CDate"

You can only use the VB "CDate" function with static parameters on the following HMI devices:

- TP1200 Comfort Pro
- TP1500 Comfort Pro / V2
- TP1900 Comfort Pro / V2
- TP2200 Comfort Pro / V2

## Visualizing Processes with View of Things

### Contents

Information that could not be included in the online help and important information about product features.

### Performance features of the View of Things web application

The number of screens and tags used in a web application is displayed during compiling. A warning is issued if any of the following limits are exceeded:

- You have used more than 10 screens.
- You have used more than 100 tags. This includes all HMI tags displayed in the overview table. This also includes all automatically created tags that are not currently required, for example, because the associated dynamization has been deleted.

### Tags of the DTL data type

The tags of the DTL data type cannot be read or written with View of Things.

### Error diagnostics with View of Things

For View of Things no error diagnosis is possible with the WinCC Unified Trace Viewer.

Instead select one of the following options:

- Use the development console of the browser which is used as the Unified web client.
- In the web client press [Shift]+F12.

  The internal WinCC Unified diagnostics opens. The right side of the web browser lists the "HMIRuntime.Traces", warnings and errors.

Script debugging is not supported for View of Things.
