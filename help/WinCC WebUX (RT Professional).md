---
title: "WinCC WebUX (RT Professional)"
package: WebUXWCCPenUS
topics: 20
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC WebUX (RT Professional)

This section contains information on the following topics:

- [WebUX - Overview (RT Professional)](#webux---overview-rt-professional)
- [Installing WebUX (RT Professional)](#installing-webux-rt-professional)
- [Supported functions (RT Professional)](#supported-functions-rt-professional)
- [Configuring a project for WebUX (RT Professional)](#configuring-a-project-for-webux-rt-professional)
- [Using WebUX (RT Professional)](#using-webux-rt-professional)

## WebUX - Overview (RT Professional)

### Overview

WebUX provides a solution for device-independent and browser-independent operator control and monitoring of the automation system.

In the interests of process reliability, only HTTPS connections with SSL certificates are supported.

The Web technology used leads to restrictions compared to the TIA Portal. You can find additional information in [Functions supported in WebUX](#functions-supported-in-webux-rt-professional)

### Distinction WebUX - WebNavigator

| WebUX | WebNavigator |
| --- | --- |
| Based on generally established Web standards | Based on ActiveX technology from Microsoft |
| Can be used regardless of browser. | Supports Microsoft Edge or Chrome. |
| Runs on a wide variety of devices, regardless of operating system, for example on tablets, PCs and smart phones. | Runs only on Windows computers. |
| Does not require a client installation. | Requires a client installation. |
| Default user rights are sufficient | Requires administrative rights to install. |

### Visualization in WebUX

Supported screen objects are displayed in the Web browser with the "HTML5" and "SVG" standards:

- The graphic elements are created with SVG elements.
- The dynamic updating of the process picture is performed via a permanent connection between the browser and server.

> **Note**
>
> **Browser-dependent representation**
>
> Minor differences in display and behavior are possible for the different browser versions.

### Working with WebUX

Carry out the following steps to use WebUX:

1. [Installing WinCC and WinCC/WebUX on the WebUX server.](#installing-the-webux-server-rt-professional)
2. [Set up a WebUX Website.](#configuring-the-webux-website-rt-professional)
3. [Configure a project for WebUX.](#configuring-a-project-for-webux-rt-professional)
4. [Create users and user groups for WebUX.](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#administering-users-for-web-client-rt-professional)
5. [Access the WebUX server with the terminal device.](#how-to-use-webux-rt-professional)

### Performance data

The performance of the WebUX system depends on the employed hardware of the WebUX server and the volume of graphic objects and scripts.

Configuration

As a typical scenario, we tested the simultaneous access of 100 WebUX clients to one WebUX server.

**Screen change in Runtime**

The performance on a WebUX client basically corresponds to the behavior on a WinCC client.

However, the load times during picture changes on a WebUX client are influenced by the following factors:

- Number of WebUX clients that access the WebUX server simultaneously
- Performance of the WebUX clients
- Utilized browser

  Depending on the browser, the picture setup time can vary by several seconds.
- Number of scripts in the process pictures

  Unlike with WinCC clients, all scripts are executed on the WebUX server.
- Number of graphic objects in the process pictures
- Type of graphic objects in the process pictures

  Web Controls can prolong the loading time.

> **Note**
>
> **Loss of connection as a result of performance load**
>
> A high performance load can result in a timeout. This cancels the WebUX client connection to the WebUX server.

### Migration (as of V14)

WebUX is supported for migration from WinCC V7.3.

---

**See also**

[Functions supported in WebUX (RT Professional)](#functions-supported-in-webux-rt-professional)
  
[How to use WebUX (RT Professional)](#how-to-use-webux-rt-professional)
  
[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)
  
[Installing the WebUX server (RT Professional)](#installing-the-webux-server-rt-professional)
  
[Configuring a project for WebUX (RT Professional)](#configuring-a-project-for-webux-rt-professional)
  
[Administering users for Web Client (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#administering-users-for-web-client-rt-professional)
  
[http://support.automation.siemens.com/WW/view/de/109480708](https://support.industry.siemens.com/cs/ww/en/view/109480708)

## Installing WebUX (RT Professional)

This section contains information on the following topics:

- [Licensing (RT Professional)](#licensing-rt-professional)
- [Software and hardware requirements (RT Professional)](#software-and-hardware-requirements-rt-professional)
- [Installing Microsoft Message Queuing (MSMQ) (RT Professional)](#installing-microsoft-message-queuing-msmq-rt-professional)
- [Installing the WebUX server (RT Professional)](#installing-the-webux-server-rt-professional)
- [WebUX Configurator (RT Professional)](#webux-configurator-rt-professional)
- [Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)
- [Communication: SSL certificate for HTTPS connections (RT Professional)](#communication-ssl-certificate-for-https-connections-rt-professional)

### Licensing (RT Professional)

The WinCC/WebUX basic package with an integrated WinCC WebUX Monitor license is included in WinCC.

#### WebUX client

The WebUX clients are licensed on the WebUX server.

No license is required for the WebUX client on the computer.

#### WebUX server

The WebUX server is installed on a WinCC system. The WinCC basic system requires at least the WinCC Runtime Professional license.

The license keys are differentiated as described below and run in parallel on the WinCC/WebUX server:

| License | Function | Remarks |
| --- | --- | --- |
| WinCC WebUX Monitor | The user has only read access. | The user has the authorization level "Web access - monitoring only".  If the available "Monitor" licenses have been allocated, an "Operate" license or a WebNavigator license can also be allocated to a WebUX client for read access. |
| WinCC WebUX Operate | User has read and write access | If the available "Operate" licenses have been allocated, a WebNavigator license can also be allocated to a WebUX client for read or write access. |
| WinCC/WebNavigator | The user's authorizations determine whether write access is possible in addition to read access. | If a WinCC/WebNavigator license is also installed in the WinCC system, the WebNavigator license can also be allocated to a WebUX client.  First, however, all available WebUX licenses are used. |

The license packages are available with 1, 3, 10, 30 and 100 clients.

If the number of licensed clients is exceeded during the logon attempt by a WebUX client, no further logon is permitted.

The packages are version-independent and can be combined.

> **Note**
>
> By default, the WebNavigator licenses are used for WebUX. If you want to use these licenses separately, clear the "Use WebNavigator licenses for WebUX" check box under "Runtime settings > Web access".

#### Reserved license

A reserved WebUX license always gives the user guaranteed access to the WebUX server.

A connection remains reserved for the user. The number of freely available WebUX licenses is reduced by each configured reserved license.

> **Note**
>
> If the "Use WebNavigator licenses for WebUX" option is selected, no reserved WebUX licenses can be guaranteed.

Possible applications include:

- Remote operator access:

  If the connections to the WebUX server are occupied by read-only access, a connection remains reserved for operation.
- Remote maintenance:

  Several different plants are accessed for service and maintenance one after another with the reserved license.
- Central maintenance:

  Reserved licenses are used for simultaneous access to multiple servers.
- Central display:

  Central client stations are always connected, for example to display the status of the plant.

#### Reserve WebUX license

You assign one of the available licenses to a WebUX user as a reserved license under "Runtime settings > Web Navigator".

To do so, enable the option "Reserve WebUX license" for a selected user. The "Number of reserved licenses" field shows how many WebUX licenses are reserved.

Reserved WebUX licenses can only be configured for individual users and not for user groups.

If more reserved licenses are configured than are available on the WebUX server, the licenses are assigned to the first users to log on.

---

**See also**

[Managing users for the Web client (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-users-for-the-web-client-rt-professional)
  
[Administering user groups for Web Client (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#administering-user-groups-for-web-client-rt-professional)

### Software and hardware requirements (RT Professional)

#### Software requirements

Certain requirements concerning operating system and software configuration must be met for the installation.

**WebUX server: Operating system**

| Software | Requirements |
| --- | --- |
| Operating systems* | **Windows 10 (64-bit)**   - Windows 10 (Professional, Enterprise) - Windows 11 (Professional, Enterprise) |
| **Windows Server (64-bit)**   - Windows Server 2019 - Windows Server 2022 |  |

* Including all security updates up to Microsoft Security Bulletin Summary for August 2019 (MS19-Aug). For more detailed information on operating systems, refer to the help on Microsoft Windows or the Microsoft homepage.

**Additional software requirements**

|  | Version / setting | Relevant for | Remarks |
| --- | --- | --- | --- |
| Web browser | The browser must support HTML5. | WebUX client / terminal | WebUX can be used with any browser. |
| TIA Portal version | V18 | WebUX server | The WebUX server is supported as an option as of V14. |
| SIMATIC Logon version (optional) | SIMATIC Logon V1.5 SP3 | WebUX server | Only relevant if you are using SIMATIC Logon for central user administration. |
| User rights for installation | Administrator rights | WebUX server | Required rights for installing the WebUX server. |
| User rights for operation | Default user rights | WebUX client  WebUX server | Required rights on the WebUX server and WebUX client. |
| Microsoft Internet Information Service (IIS) | WWW Services > Common HTTP Features:  - HTTP error - HTTP redirect - Standard document - Static content   WWW Services > Performance Features:  - Compression of dynamic content - Compression of static content   WWW services > Application development features (only for Windows Server 2019 Windows Server 2022):  - WebSocket protocol | WebUX server | The WebUX server requires the Microsoft Internet Information Service (IIS).  Enable the settings listed for the IIS. |
| Microsoft Message Queuing (MSMQ) | In Control Panel in the dialog box for activating Windows features (Windows 10):  - "Microsoft Message Queue (MSMQ) Server" component   In the server manager (Windows Server 2019 / Windows Server 2022):  - "Message Queuing" option - Below this, the "Message Queuing Services" option - Below this, the "Message Queuing Server" option | WebUX server | The WebUX server requires the Message Queuing service from Microsoft.  Activate the listed settings for Microsoft Message Queuing. |

#### WebUX client (terminal)

On a terminal device that accesses the WebUX server, you only require an HTML5-compatible web browser, for example Chrome, Edge, Firefox or Safari.

#### Installation sequence for the WebUX server

Follow the installation sequence below when you install a WebUX server on a PC:

1. Install the Internet Information Service (IIS).

   You can find more information in: [Installing Internet Information Services (IIS)](WinCC%20WebNavigator%20%28RT%20Professional%29.md#installing-internet-information-services-iis-rt-professional)
2. Install Microsoft Message Queuing (MSMQ).

   You can find more information in: [Installing Microsoft Message Queuing (MSMQ)](#installing-microsoft-message-queuing-msmq-rt-professional)
3. Install the WebUX server.

   To install the WebUX server, you also need to install WinCC Runtime Professional. Microsoft SQL Server is automatically installed.

> **Note**
>
> A WebUX server can be installed on a WinCC server or a single-user system. Do not install the WebUX server on a WinCC client.

---

**See also**

[Installing Internet Information Services (IIS) (RT Professional)](WinCC%20WebNavigator%20%28RT%20Professional%29.md#installing-internet-information-services-iis-rt-professional)
  
[Installing Microsoft Message Queuing (MSMQ) (RT Professional)](#installing-microsoft-message-queuing-msmq-rt-professional)
  
[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)

### Installing Microsoft Message Queuing (MSMQ) (RT Professional)

#### Introduction

Before installing the WebUX server, you must install Microsoft Message Queuing (MSMQ).

#### Requirement

- Administrator rights
- Write access for the registry

#### Windows Procedure

1. Go to "Control Panel > Programs".
2. Click the "Enable or disable Windows features" button on the left menu bar.

   The "Windows Features" dialog box opens.
3. Activate the "Microsoft Message Queue (MSMQ) Server" component.

   The "Microsoft Message Queue Server Core Components" entry is activated.

   The subcomponents remain deactivated.
4. Click "OK" to confirm.

#### Windows Server Procedure

1. Start the Server Manager.
2. Click "Add Roles and Features".

   The "Add Roles and Features Wizard" opens.
3. Click "Server Selection" in the navigation area.

   Ensure that the current computer is selected.
4. Click "Features" in the navigation area.
5. Activate the following options:

   - "Message Queuing"
   - Below this, the "Message Queuing Services" option
   - Below this, the "Message Queuing Server" option
6. Click "Install".

---

**See also**

[Software and hardware requirements (RT Professional)](#software-and-hardware-requirements-rt-professional)

### Installing the WebUX server (RT Professional)

#### Requirements

- Local administrator rights
- Internet Information Services is installed
- Microsoft Message Queuing is installed

#### Procedure

1. Insert the installation disk into the appropriate drive.  
   Setup runs automatically unless you have disabled autostart on the PC.
2. If the setup program does not start up automatically, start it manually by double-clicking the "Start.exe" file.  
   The dialog to select the setup language opens.
3. Choose the language in which you want the setup program dialogs to be displayed.
4. To read the information on the product and installation, click the "Read Notes" or "Installation Notes" button.  
   The corresponding help file opens with instructions.
5. Once you have read the notes, close the help file and click the "Next" button.  
   The dialog for the selection of product languages opens.
6. Select the languages for the product user interface, and click the "Next" button. The dialog for selecting the product configuration opens.
7. Select the following components for installation:

   - SIMATIC WinCC Runtime Professional V15
   - SIMATIC WinCC/WebUX
8. Choose whether you want a desktop shortcut to be created, and select a different destination directory for the installation if needed. Note that the length of the installation path must not exceed 89 characters.
9. Click the "Next" button.  
   The dialog for the licensing conditions opens.
10. To continue the installation, read and accept all license agreements and click "Next".  
    In the event that the security and permission settings need to be changed for the installation, the dialog for the security settings opens.
11. To continue the installation, accept the changes to the security and permissions settings, and click the "Next" button.
12. Check the selected installation settings. If you want to make any changes, click the "Back" button until you reach the point in the dialog where you want to make changes. Once you have completed the desired changes, return to the overview by clicking "Next".
13. Click the "Install" button.  
    The installation begins.
14. It may be necessary to restart the computer. If this is the case, select the "Yes, restart my computer now." option button. Then click "Restart".

    "WinCC WebUX Configurator" is started automatically when the system is restarted.

**Note**

"English" is always installed as the basic product language.

**Note**

If no license key is found during installation, you have the chance to transfer it to your PC. If you skip the license transfer, you can register it later with the Automation License Manager.

If the installation was successful, a message to this effect is displayed on the screen. If errors occurred during installation, an error message is displayed informing you of the type of errors.

> **Note**
>
> You can also start the "WinCC WebUX Configurator" manually with Options and Tools > HMI Tools > SCADA WebUX Configuration manager.

#### Result

WinCC Runtime Professional and the WebUX server are installed.

---

**See also**

[WebUX - Overview (RT Professional)](#webux---overview-rt-professional)
  
[WebUX Configurator (RT Professional)](#webux-configurator-rt-professional)
  
[Communication: SSL certificate for HTTPS connections (RT Professional)](#communication-ssl-certificate-for-https-connections-rt-professional)
  
[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)

### WebUX Configurator (RT Professional)

#### Introduction

Configure the WebUX Website on the WebUX server and the connection via HTTPS to communicate with the WebUX clients. The WinCC WebUX Configurator provides assistance.

#### Principle

Once WinCC Runtime Professional and WebUX are installed, the WinCC WebUX Configurator opens.

To make changes later, you can find the WinCC WebUX Configurator in the "Siemens Automation" program group:

- Options and Tools > HMI Tools > SCADA WebUX Configuration manager

The WebUX Configurator is used to set up the standard configuration for using WebUX:

- Configuration of the Microsoft Internet Information Service
- Settings of the Web server
- SSL certificate for HTTPS connections
- Virtual folder

Read the information about digital certificates at:

- [Communication: SSL certificate for HTTPS connections](#communication-ssl-certificate-for-https-connections-rt-professional)

During the course of initial configuration, you specify whether you wish to create a new default Website or a new virtual directory.

If you set up the Website as a virtual folder, there must already be at least one Website on the PC with SSL encryption enabled. The Websites that meet this criterion are shown in the "Select the higher level website" selection list. When you select one of these Websites, the WebUX Configurator takes the port number and the SSL settings from the settings of the IIS.

For accessing the Website with a terminal device, you need to add the name of the virtual directory to the URL in the browser.

---

**See also**

[Communication: SSL certificate for HTTPS connections (RT Professional)](#communication-ssl-certificate-for-https-connections-rt-professional)
  
[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)
  
[Installing the WebUX server (RT Professional)](#installing-the-webux-server-rt-professional)

### Configuring the WebUX website (RT Professional)

#### Introduction

For communication with the WebUX clients, you configure the WebUX Website and connection over HTTPS on the WebUX server using the [WinCC WebUX Configurator](#webux-configurator-rt-professional).

#### Requirement

- Microsoft Internet Information Service (IIS) is installed.
- WinCC Runtime Professional is installed.
- The "WinCC WebUX" program package is installed.
- The "WinCC WebUX" license is installed.

#### Procedure

Once WinCC Runtime Professional and WebUX are installed, the WinCC WebUX Configurator will open after a PC restart.

1. Click "Apply configuration".

   The standard configuration is set up.

   The "IIS configuration" dialog opens.
2. Enter a name for the Website.
3. If you only operate the WebUX Web page on the server, select the "Create a new website" option.

   If you work with virtual folders, proceed to step 6.
4. Enter the number of the port used for access in the "Port" field.

   The HTTPS standard port "443" is set by default.

   If you select a different port number, the address must be adapted on the WebUX client: When logging on to the terminal, this number is added into the browser address bar after the server name.
5. Select the settings for the digital certificate of the server.
6. If you set up the Website as a virtual directory, select a higher level Website.

   The WebUX Configurator takes the port number and the SSL settings from the IIS settings.
7. Confirm with "OK".
8. When the configuration has been set up, click "Exit".
9. Restart the computer.

#### Result

The WebUX server has been configured and the WebUX Website set up.

The WinCC project must be activated in Runtime in order to access the WebUX server.

---

**See also**

[WebUX - Overview (RT Professional)](#webux---overview-rt-professional)
  
[Communication: SSL certificate for HTTPS connections (RT Professional)](#communication-ssl-certificate-for-https-connections-rt-professional)
  
[How to use WebUX (RT Professional)](#how-to-use-webux-rt-professional)
  
[Installing the WebUX server (RT Professional)](#installing-the-webux-server-rt-professional)
  
[Software and hardware requirements (RT Professional)](#software-and-hardware-requirements-rt-professional)

### Communication: SSL certificate for HTTPS connections (RT Professional)

To improve the security of your communication, WebUX only supports HTTPS connections.

You need a digital SSL certificate for the WebUX server.

You can find more information in the Microsoft Support under "How to Set Up an HTTPS Service in IIS":

- <http://support.microsoft.com/kb/324069>

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Protecting the infrastructure**  Setting up a Web server could allow access to your plant infrastructure.  Therefore, protect the computer on which the Web server is installed. Make sure that the following rules are followed:  - The computer is only accessible via secure connections. - The check mechanisms provided by software vendors are activated and are not bypassed under any circumstances. |  |

#### Install a SSL certificate

You have the following options when setting up the WebUX Website:

- Select an existing certificate
- Create self-signed certificates:
- Install a certificate after setting it up

**Creating a new certificate**

1. Activate the "Create a new certificate" option.
2. Enter a name of your choice.

When the configuration is completed, a self-signed certificate is created. The certificate is valid for one year.

> **Note**
>
> **Restricted authentication**
>
> The certificates that you create when you configure the WebUX Website itself are not verified by an official certification body. Depending on your browser settings, a warning message is displayed when you access the Website.
>
> To better secure the server authentication, install the certificate of an official certification body.

---

**See also**

[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)
  
[WebUX Configurator (RT Professional)](#webux-configurator-rt-professional)
  
[Installing the WebUX server (RT Professional)](#installing-the-webux-server-rt-professional)
  
<http://support.microsoft.com/kb/324069>

## Supported functions (RT Professional)

This section contains information on the following topics:

- [Functions supported in WebUX (RT Professional)](#functions-supported-in-webux-rt-professional)
- [Supported functions: Screen objects (RT Professional)](#supported-functions-screen-objects-rt-professional)
- [Supported functions: Dynamization (RT Professional)](#supported-functions-dynamization-rt-professional)
- [Supported system functions (RT Professional)](#supported-system-functions-rt-professional)

### Functions supported in WebUX (RT Professional)

#### Restrictions compared to WinCC Runtime Professional

The following restrictions apply compared to the functional scope of WinCC Runtime Professional:

- Touch operation is not optimized.

  You can, however, use all the touch gestures that are supported by WinCC Runtime Professional.
- Design settings are not supported.

  Please note that the standard design is selected by default in WinCC projects.
- Not all elements and controls or their properties are supported, for example the system diagnostics view and user display are not supported.

  (For details, see "[Supported functions: Screen objects](#supported-functions-screen-objects-rt-professional)")
- Dynamization (for details, see "[Supported functions: Dynamization](#supported-functions-dynamization-rt-professional)"):

  Global script: VB scripting is supported with certain restrictions.
- Simulation only works if Runtime Professional and WebUX are also installed and WebUX is configured in the Engineering System. Otherwise, WebUX simulation is not possible.

All unsupported objects are hidden in WebUX.

> **Note**
>
> If unsupported objects are used, warnings are output on the "Info" tab in the Inspector window during compilation.
>
> If you do not want to display the WebUX warnings, they can be hidden. Go to "Runtime settings > Compiler options" and select the "Hide WebUX warnings" check box.

**Faceplates**

WebUX supports faceplates without restrictions.

---

**See also**

[Supported functions: Screen objects (RT Professional)](#supported-functions-screen-objects-rt-professional)
  
[Supported functions: Dynamization (RT Professional)](#supported-functions-dynamization-rt-professional)
  
[Supported system functions (RT Professional)](#supported-system-functions-rt-professional)

### Supported functions: Screen objects (RT Professional)

WebUX supports most of the screen objects.

#### Restrictions for all screen objects

The following restrictions apply to all screen objects in WebUX:

- Object events are not supported for controls.
- The print function is not supported.
- The central color palette and design settings are not supported.

  The configured colors are displayed instead.
- "Tooltip text" is not supported for grouped objects.
- The ends of the lines do not flash.
- Screen or background screen: The graphics formats TIF(F), EMF and WMF are not supported. The formats JPG, JPEG, PNG, GIF, BMP, ICO and SVG can be used.
- The shadow is not sketched.
- Styles are not supported.

The following object properties are not supported:

| Object property | OLE Automation Name | Comment |
| --- | --- | --- |
| Languages configured | DataLanguage |  |
| Draw inside frame | DrawInsideFrame | The border lines are always drawn inside the frame. |
| Global color scheme | GlobalColorScheme |  |
| Global shadow | GlobalShadow | The shadow is not sketched. |
| Server name | ServerName |  |
| Windows style | WindowsStyle | Instead, the object is displayed according to your settings. |

#### Supported screen objects

The following table shows the availability of basic objects in WebUX:

| Basic objects | WebUX | Unsupported properties <sup>1)</sup> |
| --- | --- | --- |
| All objects except "Connector" | Yes | See "Restrictions for all screen objects" |
| Connector | No | For dynamized objects that are connected over the "Connector" object, dynamization is not displayed over WebUX.  The connector is treated like the static object "Line". The ends of a line cannot have different designs. |

The following table shows the availability of elements in WebUX:

| Elements | ActiveX control | WebUX control | WebUX | Unsupported properties <sup>1)</sup> |
| --- | --- | --- | --- | --- |
| I/O field |  | - | Yes | - Unit - Clear on new input (Edge only) - Accept on full input - Clear on invalid input - Cursor control |
| Button |  | - | Yes |  |
| Round button |  | - | Yes |  |
| Symbolic I/O field |  | - | Yes | - Dynamization of the property "TextList" |
| Graphic I/O field |  | - | Yes |  |
| Bar |  | - | Yes |  |
| Symbol library |  | - | No |  |
| Slider | Slider Control | Slider Web Control | Yes | - Object events |
| Scroll bar |  | - | Yes |  |
| Check box |  | - | Yes |  |
| Option button |  | - | Yes |  |
| Gauge | Gauge Control | Gauge Web Control | Yes | - Object events - DialColor - BackPicture - BorderOuterStyle3D - BorderWidth3D - BorderWidth - CenterSize - DialSize - AngleMin - AngleMax - ScaleTickLabelPosition - ScaleTickPosition - ScaleTickLength - ShowDecimalPoint - BackFillStyle |
| Clock | Clock Control | Digital/Analog Web Clock Control | Yes | - Object events |

The following table shows the availability of controls in WebUX:

| Controls | ActiveX control | WebUX control | WebUX | Unsupported properties<sup>1)</sup> |
| --- | --- | --- | --- | --- |
| All controls |  |  |  | Object events |
| Picture window |  |  | Yes | - Foreground - Scaling factor - Window mode - Monitor number - Independent window - Menu/Toolbar Configuration |
| f(t) trend view | OnlineTrendControl | OnlineTrend Web Control | Yes | - Object events - Export of Runtime data - Online configuration in Runtime - Operator authorization for key functions in the toolbar - Print function - VB scripting: No methods - User scaling - Trend display:   - The trend type "Display values" - Trend selection |
| f(x) trend view | FunctionTrendControl | FunctionTrend Web Control | Yes | - Object events - Export of Runtime data - Online configuration in Runtime - Operator authorization for key functions in the toolbar - Print function - VB scripting: No methods - Data from user archives - Trend selection |
| Alarm view | AlarmControl | Alarm Web Control | Yes | - Object events - Export of Runtime data - Online configuration in Runtime - Operator authorization for key functions in the toolbar - Print function - VB scripting: No methods - Alarm text blocks   - Daylight saving time/standard time   - Logging   - Reporting   - Class priority   - Frequency   - Total +/-, total +/*1, total +/*2, total +/+   - Average +/-, average +/*1, average +/*2, average +/+   - Accepting project settings - Acknowledgment of alarm annunciator - Configuration of filters in Runtime - Configuration of lock list in Runtime - User-defined sorting of the displayed alarms - Scrolling in the historical alarm list (long-term) - The contents of the columns "Class", "Type", "Date" and "Time" are shown in a joint column in each case |
| Table view | OnlineTableControl | OnlineTable Web Control | Yes | - Object events - Export of Runtime data - Online configuration in Runtime - Print function - VB scripting: No methods |
| Value table | TrendRuler Control | TrendRuler Web Control | Yes | - Object events - Export of Runtime data - Online configuration in Runtime - Operator authorization for key functions in the toolbar - Print function - VB scripting: No methods |
| HTML browser | WebBrowser Control | WebBrowser Control | Yes | - Object events - Only HTTPS connections are possible.   You can find additional information in "Displaying files in WebBrowser Control". - The browse dialog for finding the URL is not offered. - Depending on the Web browser, unsupported buttons and functions are grayed out. |
| Print job/Script diagnostics |  | - | No |  |
| Recipe view | UserArchiveControl | - | No |  |
| Media Player |  | - | No |  |
| Memory space view |  | - | No |  |
| Channel diagnostics view | ChannelDiagnose | - | No |  |
| System diagnostics view | SysDiagControl | - | No |  |
| User view | UserAdminControl | - | No |  |
| Symbol library | Symbol Library | - | No |  |
| PLC Code Viewer |  | - | No |  |
| ProDiag overview |  | - | No |  |
| GRAPH overview |  | - | No |  |

1) Restrictions for all screen objects are not listed again.

#### Displaying files in the WebBrowser Control

Proceed as follows to display a file in the WebBrowser Control:

1. Save the file in a sub-folder at the following path

   - C:\inetpub\wwwroot\siemens\WebRH\public\<folder>
2. Use the following call in the WebBrowser Control:

   - https://<server name>/<folder>/<file name>

**Example**

The PDF file "WinCC.pdf" is located in the sub-folder "WebUXFiles":

- C:\inetpub\wwwroot\siemens\WebRH\public\WebUXFiles

Call using the following URL:

- https://localhost/WebUXFiles/WinCC.pdf

> **Note**
>
> **No access restrictions for "public" folder**
>
> Please note that files in the "C:\inetpub\wwwroot\siemens\WebRH\public" folder are accessible to all users.
>
> WinCC authorizations do not apply to files in this folder.

---

**See also**

[Functions supported in WebUX (RT Professional)](#functions-supported-in-webux-rt-professional)

### Supported functions: Dynamization (RT Professional)

#### Dynamization with scripts

WebUX supports screen objects in which the following dynamization is configured:

- Trigger: The trigger "On demand" is not supported. Instead, a 2-second trigger is used.

  > **Note**
  >
  > When accessing via WebUX, the refresh of the dynamics that use the screen cycle is always 2 seconds, even if a different screen cycle is configured.
- Tag connection
- Direct connection
- VBS action

The following restrictions apply to the dynamization:

- VB scripting:

  - Scripts cannot open interactive applications, e.g. MS Excel. Operating system restrictions prevent this function.
  - WebUX Web Controls do not support any methods.

    Instead, you address the elements of the controls through an assigned index.
  - The method "HMIRuntime.Stop" for ending WinCC Runtime is not supported.
  - Calling message boxes with the "MsgBox" function is suppressed. (Message box)
  - The VBS object "DataSet" may only contain global tags with a scalar data type, e.g. "BOOL", "DOUBLE", "LONG INT".

    OLE Automation data types are not processed, e.g. "VARIANT" or an Excel table.
  - Certain object properties cannot be dynamized or use a different value format.

    You can find details about this on the Customer Support pages on the Internet, entry ID=109481796: [http://support.automation.siemens.com/WW/view/en/109481796](http://support.automation.siemens.com/WW/view/de/109481796)
- C scripting:

  - C actions are not supported

> **Note**
>
> **Scripts always run on the WebUX server**
>
> No scripts are run locally on a WebUX client. Scripts that run locally on a WinCC client are executed on the WebUX server with access via WebUX.
>
> The following factors can affect the performance of the WebUX server:
>
> - Number of scripts running
> - Number of accessing WebUX clients
>
> If necessary, reduce the scripts in the process pictures that are saved for WebUX.

> **Note**
>
> The option "SmartTags reads PLC value via cache" under "Runtime settings > General" is irrelevant for WebUX. In WebUX, the process tags are always read from the buffer, in other words asynchronously.

---

**See also**

[Functions supported in WebUX (RT Professional)](#functions-supported-in-webux-rt-professional)

### Supported system functions (RT Professional)

#### System functions in WebUX

WebUX supports the following system functions:

| System function | Status | Support in VB scripting | Comment |
| --- | --- | --- | --- |
| ActivateScreen | available | available |  |
| ActivateScreenInCurrentScreenWindow | available | not available |  |
| ActivateScreenInScreenWindow | available | available |  |
| DecreaseTag | available | available |  |
| ExportImportUserAdministration | not available | not available |  |
| GetLocalScreen | not available | not available |  |
| GetParentScreen | not available | available |  |
| GetParentScreenWindow | not available | available |  |
| GetPLCMode | not available | not available |  |
| GetTag | not available | not available |  |
| IncreaseTag | available | available |  |
| InverseLinearScaling | available | available |  |
| InvertBit | available | available |  |
| InvertBitInTag | available | available |  |
| IsUserAuthorized | not available | not available |  |
| LinearScaling | available | available |  |
| LookupText | available | available |  |
| ResetBit | available | available |  |
| ResetBitInTag | available | available |  |
| SetBit | available | available |  |
| SetBitInTag | available | available |  |
| SetLanguage | available | available |  |
| SetPropertyByConstant | available | available |  |
| SetPropertyByProperty | available | available |  |
| SetPropertyByTag | available | available |  |
| SetPropertyByTagIndirect | available | available |  |
| SetPropertyOfCurrentWindow | available | not available |  |
| SetPropertyOfCurrentWindowByProperty | available | not available |  |
| SetPropertyOfCurrentWindowByTagIndirect | available | not available |  |
| SetScreenKeyboardMode | not available | not available | No virtual keyboard is available for WebUX. |
| SetTag | available | available |  |
| SetTagByProperty | available | available |  |
| SetTagByTagIndirect | available | available |  |
| SetTagIndirect | available | available |  |
| SetTagIndirectByProperty | available | available |  |
| SetTagIndirectByTagIndirect | available | available |  |
| SetTagWithOperatorEvent | available | available |  |
| ShowBlockInTIAPortalFromAlarm | not available | not available | TIA Portal cannot be opened on a client. |
| ShowLogonDialog | not available | not available | The login window is displayed automatically when you connect. |
| ShowPLCCodeViewFromAlarm | not available | not available | The PLC code view is not available for WebUX. |
| StartProgram | not available | not available |  |
| StopRuntime | not available | not available |  |

---

**See also**

[Functions supported in WebUX (RT Professional)](#functions-supported-in-webux-rt-professional)

## Configuring a project for WebUX (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Configuring WinCC screens for WebUX (RT Professional)](#configuring-wincc-screens-for-webux-rt-professional)

### Basics (RT Professional)

#### Basics

Before you can use WebUX on terminal devices, the project must be correctly configured:

- The WebUX users are set up.
- The process pictures are optimized for viewing on the Web.

> **Note**
>
> **Windows**
>
> IIS on Windows supports a maximum of ten connections or instances. WebUX requires more than one connection for a client. Therefore, a maximum of three or four WebUX clients can connect to the WebUX server.
>
> If the limit is exceeded, you can no longer operate the instances already connected.
>
> Use a server operating system for Web applications with multiple WebUX clients.

#### Use of special characters

Depending on the language and components, only specific characters are permitted in names. You can use all characters of the ASCII character set. Always avoid using national special characters, such as umlauts. Avoid using special characters especially in the following cases:

- In object names, if you are using object names in scripts.
- In object names, if you are using object names as URL in the Web browser.
- In project names and screen names, if you are using WebNavigator or WebUX.

> **Note**
>
> **Special characters in project names**
>
> The following special characters are not permitted in the project names:
>
> . , ; : ! ? " '   
> + = / \ @ *   
> [ ] { } < >  
> space  
> Uppercase and lowercase are relevant in the project names.

---

**See also**

[Administering user groups for Web Client (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#administering-user-groups-for-web-client-rt-professional)
  
[Managing users for the Web client (RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-users-for-the-web-client-rt-professional)
  
[Configuring WinCC screens for WebUX (RT Professional)](#configuring-wincc-screens-for-webux-rt-professional)

### Configuring WinCC screens for WebUX (RT Professional)

#### Introduction

You need to configure screens for WebUX so that they can be run on the Web browser.

#### Procedure

1. Double-click the desired screen in the project tree.

   The screen opens and the screen properties are shown in the Inspector window.
2. In the Inspector window, click "Properties > Properties > Web access".
3. Select the "Web access" check box under "WebUX".

   or
4. Select the desired screen in the project tree.
5. Select the "Web access > WebUX" command from the shortcut menu.

   The pictures are additionally saved in "*.rdf" format. Faceplate types are additionally stored in the "*.json" format. When a process picture is saved as Web-enabled, the properties of the picture and the objects are checked. The result is stored in the output window.
6. Check the alarms in the output window.

   The alarms contain a list of graphics objects that cannot be saved with Web compatibility. Double-click on the entry in the output window to edit the objects.

> **Note**
>
> You can also configure multiple screens for Web access by selecting the "Screens" entry in the project tree and then the "Web access > WebUX enabled" command from the shortcut menu.

> **Note**
>
> Only Web-enabled objects are displayed in WebUX Runtime.

#### Result

The WinCC screens are configured for Web access. During compilation of the project, the WinCC screens are adapted for access via the Intranet/Internet and published on the WebUX server.

#### Start screen and start language on the WebUX client

> **Note**
>
> You have the option to define a start screen and a start language for the WebUX client in the ActiveX control UserAdminControl.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)

## Using WebUX (RT Professional)

This section contains information on the following topics:

- [How to use WebUX (RT Professional)](#how-to-use-webux-rt-professional)

### How to use WebUX (RT Professional)

#### Introduction

To use WinCC/WebUX on terminal devices, all you need is a Web browser with access to the WebUX server network.

> **Note**
>
> **Windows on the WebUX server: Limited number of WebUX clients**
>
> IIS on Windows supports a maximum of ten connections or instances. WebUX requires more than one connection for a client. Therefore, a maximum of three or four WebUX clients can connect to the WebUX server.
>
> If the limit is exceeded, you can no longer operate the instances already connected.

> **Note**
>
> **Operation in Runtime**
>
> - Before closing the browser, remember to end your session so that the license is free again.
> - Close the browser to reduce power consumption for mobile devices and reduce the volume of data transferred.
>
>   The display is continuously updated for as long as a process picture is open in the browser.
> - Avoid the following operator inputs because they would end the session:
>
>   - Browser navigation (back/next)
>   - Reloading the Web page (refresh or <F5>)

#### Requirement

- The "WinCC WebUX" license installed on WebUX server.
- The WinCC project is configured for WebUX.
- The WinCC project is in Runtime.

#### Procedure

1. Go to the address bar of the browser and enter the address of the WebUX server.

   - https://<servername>

   If you do not use the default port, add the port number to the URL:

   - https://<servername>:<portnummer>

   If you are using a virtual folder instead of a Website, add the name of the virtual Web folder:

   - https://<servername>/<directoryname>
2. Type in the user name and password.

Depending on the user rights, you can observe or operate the WinCC project.

#### Notes on handling

- If the automatic login is no longer desired, you must delete the browser history of the respective browser.
- If the configuration of the user rights has been changed in the system, runtime must be closed and restarted in order for the changes to take effect.

---

**See also**

[WebUX - Overview (RT Professional)](#webux---overview-rt-professional)
  
[Configuring the WebUX website (RT Professional)](#configuring-the-webux-website-rt-professional)
