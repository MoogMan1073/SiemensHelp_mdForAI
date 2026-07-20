---
title: "WinCC WebNavigator (RT Professional)"
package: WebNavigatorWCCPenUS
topics: 69
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC WebNavigator (RT Professional)

This section contains information on the following topics:

- [Unsupported functions (RT Professional)](#unsupported-functions-rt-professional)
- [The basics (RT Professional)](#the-basics-rt-professional)
- [Installing WebNavigator (RT Professional)](#installing-webnavigator-rt-professional)
- [Configuring the Web Navigator system (RT Professional)](#configuring-the-web-navigator-system-rt-professional)
- [Operating a WinCC project (RT Professional)](#operating-a-wincc-project-rt-professional)
- [Setting up terminal services for Web Navigator (RT Professional)](#setting-up-terminal-services-for-web-navigator-rt-professional)
- [Troubleshooting (RT Professional)](#troubleshooting-rt-professional)

## Unsupported functions (RT Professional)

### Hotkeys

The WebNavigator client does not support any hotkeys configured in WinCC. In the WebNavigator client, you can operate using the tab key.

### Unsupported objects

The "Channel diagnostics" object is not supported by the WinCC WebNavigator option.

### Information about functions

The following list is only an excerpt of the unsupported functions. The lists contains the functions which are explicitly declared as unsupported.

|  |  |  |
| --- | --- | --- |
| GetHWDiag | OnDeactivateExecute | ReportJob |
| GetHWDiagLevel | OnErrorExecute | RPTJobPreview |
| GetKopFupAwl | OnTime | RPTJobPrint |
| GetKopFupAwlLevel | OpenPrevPicture | RptShowError |

### VBScript functions

- HMIRuntime.Stop: Terminates Internet Explorer and WinCCViewerRT, however not WinCC Runtime.
- AlarmLogs object
- DataLogs object
- Logging object
- Project object

### Functions that are unnecessary:

- DeactivateRTProject: Terminates Internet Explorer and WinCCViewerRT, however not WinCC Runtime.
- ExitWinCC
- FillDiagnoseInTags
- InquireLanguage
- TraceText
- TraceTime

### Other functions

These functions are contained in the range of functions in order to guarantee error-free compilation on the WebNavigator client. The functions are not supported by the WebNavigator client.

|  |  |  |
| --- | --- | --- |
| AXC_OnBtnHornAckn | GetCursorMode | GmsgFunction |
| AXC_OnBtnPrint | SetCursorMode | MSRTMsgWinCommand |
| AXC_OnBtnProtocol | ShowLogonDialog | TlgTableWindowPressHelpButton |
| ExportImportUserAdministration |  |  |

---

**See also**

[Using Scripts (RT Professional)](#using-scripts-rt-professional)

## The basics (RT Professional)

This section contains information on the following topics:

- [Function Overview (RT Professional)](#function-overview-rt-professional)
- [Web Navigator Server on the WinCC server (RT Professional)](#web-navigator-server-on-the-wincc-server-rt-professional)
- [WebNavigator diagnostics client (RT Professional)](#webnavigator-diagnostics-client-rt-professional)
- [WinCCViewerRT (RT Professional)](#winccviewerrt-rt-professional)
- [Terminal services and Web Navigator (RT Professional)](#terminal-services-and-web-navigator-rt-professional)

### Function Overview (RT Professional)

#### Introduction

You can use the WinCC WebNavigator option in WinCC Runtime Professional to monitor and control your WinCC project over the Intranet/Internet. This enables you to quickly and easily implement a new type of distribution of controlling and monitoring functions of your automation system. WebNavigator supports current Internet security methods.

The "WebNavigator" add-on package consists of the following components:

- WinCC WebNavigator Server
- WinCC Web Configurator
- WinCC WebNavigator Client
- WinCCViewerRT

#### WinCC WebNavigator Server

The WebNavigator server is installed on a PC along with WinCC Runtime Professional. The required WinCC screens and functions that are displayed on the WinCC WebNavigator Client are stored on the server PC.

#### WinCC Web Configurator

The WebNavigator Server needs the Microsoft Internet Information Service (IIS) for communication with the WebNavigator Clients. The IIS is set up and managed with the WinCC Web Configurator. Accesses of the WebNavigator Client are governed via user administration. You can set a different start screen and language for every user. By assigning user authorizations, a scalable access to different project areas and functions is implemented for the various users.

#### WinCC WebNavigator Client

The WebNavigator Client is started via the MS Internet Explorer with activated ActiveX controls. You control and monitor a running WinCC project without the entire WinCC basic system on the PC.

#### WinCCViewerRT

Instead of the Internet Explorer, you use the Web viewer "WinCCViewerRT" to visualize the WinCC project.

#### WebNavigator diagnostics client

You can use the diagnostics client, for example, for the maintenance of several WebNavigator servers.

#### Licensing

Licensing is managed centrally on the WebNavigator Server in accordance with the number of concurrent accesses of 3, 10, 25, 50, 100 or 150 WebNavigator Clients, for example. A license is not required on the WebNavigator Clients.

### Web Navigator Server on the WinCC server (RT Professional)

#### Structure

WinCC RT Professional and the server components of the WebNavigator are installed on a PC. The WebNavigator client can control and/or monitor the current server project both via the Internet and the Intranet.

To protect against attacks from the Internet, two firewalls are employed. The first firewall protects the WebNavigator Server from Internet attacks. The second firewall provides additional security for the Intranet.

![Structure](images/2992514699_DV_resource.Stream@PNG-en-US.png)

### WebNavigator diagnostics client (RT Professional)

#### Introduction

The WebNavigator diagnostics client enables cost-effective access to several WebNavigator Servers.

Several diagnostics clients and standard clients can be in operation at the same time. This procedure does not demand an additional license for a WebNavigator Server because licensing is handled on the diagnostics client. The diagnostics client can always access the WebNavigator server, regardless of whether the maximum number of simultaneous accesses has been reached. The diagnostics client always has guaranteed access to the WebNavigator server.

Possible applications include:

- Remote maintenance: With the Diagnostics Client, different WinCC systems are accessed for service and maintenance purposes.
- Central Control Room: The diagnostics client is used for simultaneous access to several servers.

  ![Introduction](images/90075105931_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | **Diagnostics client** with the license "WinCC WebDiag Client" |
  | ② | **WinCC / WebNavigator Server** with the license "WinCC WebNavigator" for, e.g., 3 clients |

### WinCCViewerRT (RT Professional)

#### Overview

Don't use Internet Explorer to run the "WinCCViewerRT.exe" application. Run it on the WebNavigator client instead. The WinCCViewerRT is installed along with the WebNavigator client.

WinCCViewerRT uses its own communication to access the WebNavigator server. This prevents Internet users from accessing the system and protects the system against viruses and Trojan horses.

Only the screens which are configured for Web access and published on the WebNavigator server are displayed. Users can operate and monitor the project, depending on their authorizations.

If the user is assigned the authorization no. 1002 "Web access - view only", he/she can only view the project. The WebNavigator client is therefore a so-called "View Only Client".

The cursor is a "View only cursor" and indicates that process-related operations are not possible. Certain operations are still possible, such as opening the properties dialog of an online trend control.

You can also use WinCCViewerRT as terminal server application. For more information, refer to "Setting up terminal services for WebNavigator servers".

### Terminal services and Web Navigator (RT Professional)

#### Introduction

Terminal services in the Windows Server operating systems enable access to the desktop of a Windows server.

The terminal client only handles screen output, while the application runs on the terminal server, for example WinCCViewerRT.

The terminal services transmit only the user interface of the application to the clients. Each client's keyboard inputs and mouse operations are returned back to the server.

This behavior has the following advantages:

- Use of rugged hardware for the clients, for example without fans and hard drives, for application in dusty environments.
- Use of mobile clients with limited power consumption, for example handhelds, palmtops, PDA.
- All applications are located on the server in a secure environment.
- Easy, central administration and system maintenance.
- Support of different operating systems, for example Windows CE, Windows 95.

  ![Introduction](images/25037757451_DV_resource.Stream@PNG-en-US.png)

The WebNavigator client created based on a "THIN²" architecture, i.e. the application running in multiple instances on the terminal server, e.g. WinCCViewerRT, is itself already "thin" with regard to hardware requirements.

For redundant system configurations with terminal services, please consult the corresponding Microsoft documentation.

> **Note**
>
> The terminal client supports only 256 colors.
>
> To reduce the strain on the terminal service, avoid large bitmaps whose size can change ("live video").

## Installing WebNavigator (RT Professional)

This section contains information on the following topics:

- [Software and hardware requirements (RT Professional)](#software-and-hardware-requirements-rt-professional)
- [Licensing (RT Professional)](#licensing-rt-professional)
- [Requirements for the Use of Terminal Services (RT Professional)](#requirements-for-the-use-of-terminal-services-rt-professional)
- [Installation of WebNavigator server (RT Professional)](#installation-of-webnavigator-server-rt-professional)
- [Installation of WebNavigator client (RT Professional)](#installation-of-webnavigator-client-rt-professional)
- [Installing the Web Diagnostics Client (RT Professional)](#installing-the-web-diagnostics-client-rt-professional)

### Software and hardware requirements (RT Professional)

#### Introduction

This section describes the hardware and operating system requirements for WinCC WebNavigator.

#### WebNavigator Server on a WinCC single-station system

Recommended hardware

| Symbol | Meaning |
| --- | --- |
| Processor | Intel® Core™ i3-6100U 3.5 GHz |
| Working memory | 8 GB |

Software

| Symbol | Meaning |
| --- | --- |
| Operating system: | Windows 10 (Professional, Enterprise)  Windows 11 (Professional, Enterprise)  Windows Server 2019   Windows Server 2022 |
| Software: | WinCC V18 Runtime |
| Other: | Access to the intranet/Internet  or TCP/IP connection to the WebNavigator client |

#### WebNavigator Server on the WinCC server

Recommended hardware

| Symbol | Meaning |
| --- | --- |
| Processor | Intel® Core™ i5E, 5 GHz |
| Working memory | 8 GB |

Software

| Symbol | Meaning |
| --- | --- |
| Operating system: | Windows Server 2019   Windows Server 2022 |
| Software: | WinCC Professional V18 |
| Other: | Access to the Intranet / Internet  If you publish in the **intranet**, you need a system for name resolution, which can convert computer names into IP addresses. This allows users to use alias name instead of IP addresses when connecting to the server.  If you publish on the **Internet**, you need a DNS registry for the IP address. This allows users to use alias name instead of IP addresses when connecting to the server. |

#### WebNavigator Client

Hardware

|  | Minimum | Recommended |
| --- | --- | --- |
| CPU | Dual core CPU; 2.5 GHz | Dual core CPU; 3 GHz |
| Working memory | 3 GB | 4 GB |

Software

| Symbol | Meaning |
| --- | --- |
| Operating system: | Windows 10 (Professional, Enterprise)  Windows 11 (Professional, Enterprise)  Windows Server 2019   Windows Server 2022 |
| Other: | Access to the intranet/Internet  or TCP/IP connection to the WebNavigator Server |

#### Web diagnostics client

Software

| Symbol | Meaning |
| --- | --- |
| Operating system: | Windows 10 (Professional, Enterprise)  Windows 11 (Professional, Enterprise)  Windows Server 2019   Windows Server 2022 |
| Other: | Access to the Intranet / Internet |

### Licensing (RT Professional)

#### WebNavigator Client

No license is required with server-end licensing on the WebNavigator Server on the PC with the WebNavigator Client.

#### WebNavigator Server

The WebNavigator server runs without a license in Demo mode for 30 days.  
A license is required, however, if you want to use the WebNavigator server for a longer period. Licenses are available for 1 / 3 / 10 / 30 / 100 clients that can simultaneously access the WebNavigator server. If you have upgraded an older version of WebNavigator, licenses for a different number of clients may also exist. The packages are version-independent and can be combined. Up to 150 clients can simultaneously access the WebNavigator server.

If the number of licensed clients is exceeded during a logon attempt of a Web Navigator client, a message appears. No further logon is allowed.

> **Note**
>
> **Licensing when upgrading to version V14 SP1 or higher**
>
> If you upgrade from an older version to version V14 SP1 or higher, you need a new license for WebNavigator Server.

#### Overview of licenses on the server and client

| Server | WebNavigator Client | Diagnostics client |
| --- | --- | --- |
| WebNavigator server license +  WinCC license | Web Navigator client, no local license required. Maximum number of clients corresponds to the existing license on the server. | Diagnostics client  One license per diagnostics client |
| Web diagnostics server license +  WinCC license | WebNavigator client in Demo mode Number unlimited Valid for 30 days | Diagnostics client  One license per diagnostics client |
| No WebNavigator license or  no WinCC license | WebNavigator client in Demo mode Number unlimited Valid for 30 days | Diagnostics client in Demo mode  Number unlimited Valid for 30 days |

#### Restarting the Web client after changing licenses

If you change the WebNavigator licenses on the WebNavigator server, for example, by transferring a power pack, you must restart the Web viewer or Internet Explorer, if it used, on all connected WebNavigator Clients. Otherwise, the WebNavigator Client goes to Demo mode. This also applies to automatic reconnection of the WebNavigator Client.

#### Web diagnostics client

A diagnostics client license is required on the client PC for the diagnostics client. The diagnostics client can simultaneously access up to 12 WebNavigator Servers.

When a license for WebNavigator Server or Web diagnostics server is installed on the server, the diagnostics client also has access even when the maximum number of clients is exceeded.

#### Web diagnostics server

This license allows the diagnostics Web client to access the WebNavigator Server when no WebNavigator Server license is installed on the Web Navigator server for the WebNavigator Client.

A total of 50 clients per server is allowed at the most for simultaneous access by diagnostics clients.

> **Note**
>
> **Diagnostics client without corresponding license**
>
> If you install the diagnostics client without its license, a message appears approximately 1 hour after each start of the PC. Install the diagnostics client license or remove the diagnostics client software.
>
> **PC with WinCC Runtime Professional and diagnostics client**
>
> If you install a diagnostics client on a PC with WinCC Runtime Professional, you have to reinstall the diagnostics client after removing WinCC.

### Requirements for the Use of Terminal Services (RT Professional)

WebNavigator Client is authorized for use with Windows Terminal Services. A maximum of 25 sessions per terminal server are permitted.

#### Terminal server

Hardware

|  | Minimum | Recommended |
| --- | --- | --- |
| CPU | Dual Core CPU; 2 GHz | Multi Core; 2.4 GHz |
| Working memory | 2 GB | 4 GB |

Software

| Symbol | Meaning |
| --- | --- |
| **Operating system** | Windows Server 2019 Windows Server 2022  It must be possible to open and execute applications that are run on the clients multiple times. |
| **Miscellaneous:** | If numerous users want to access the server, you need to use a high performance network adapter. |

> **Note**
>
> The memory requirements and processor load increased with each terminal client. You therefore need to ensure that the terminal server has adequate memory and processor load reserves.

#### Terminal client

| Symbol | Meaning |
| --- | --- |
| **Minimum requirement:** | Network adapter with TCP/IP Terminal client RDP 5.0 Display or screen Pointing device |

Device recommended for use as a client: SIMATIC Mobile Panel PC 12".

> **Note**
>
> As is the case with Windows Server Client Access License CAL, there are two different terminal service CALs:
>
> - The TS Device CAL permits one device user-independent Windows sessions on a Windows server.
> - The TS User CAL permits one user device-independent Windows sessions on a Windows server.
>
> A Windows Server Terminal Server "TS CAL" is required for every user or every device.
>
> You can find more information under "http://www.microsoft.com/licensing/about-licensing/client-access-license.aspx".

### Installation of WebNavigator server (RT Professional)

This section contains information on the following topics:

- [Overview (RT Professional)](#overview-rt-professional)
- [Installing Internet Information Services (IIS) (RT Professional)](#installing-internet-information-services-iis-rt-professional)
- [Installing Microsoft Message Queuing (MSMQ) (RT Professional)](#installing-microsoft-message-queuing-msmq-rt-professional)
- [Installing the WebNavigator Server (RT Professional)](#installing-the-webnavigator-server-rt-professional)

#### Overview (RT Professional)

##### Requirements

- The software requirements with regard to the Windows operating system apply.  
  The following operating systems have been authorized:

  Windows 10 (Professional, Enterprise)

  Windows 11 (Home, Professional, Enterprise)

  Windows Server 2019 Standard Edition

  Windows Server 2022 Standard (full installation)
- Local administrator rights

##### Installation sequence for the WebNavigator Server

When you install a WebNavigator Server on a PC, adhere to the following installation sequence:

1. Install the Internet Information Service (IIS).
2. Install Microsoft Message Queuing (MSMQ).
3. Install the WebNavigator Server.  
   To install the WebNavigator Server, you also need to install WinCC Runtime Professional. Microsoft SQL Server is automatically installed.

---

**See also**

[Installing Microsoft Message Queuing (MSMQ) (RT Professional)](#installing-microsoft-message-queuing-msmq-rt-professional)
  
[Installing Internet Information Services (IIS) (RT Professional)](#installing-internet-information-services-iis-rt-professional)
  
[Installing the WebNavigator Server (RT Professional)](#installing-the-webnavigator-server-rt-professional)

#### Installing Internet Information Services (IIS) (RT Professional)

##### Introduction

Before installing the WebNavigator Server, you need to install the Internet Information Service (IIS). You specify the settings for the WebNavigator Server during installation.

##### Settings under Windows or Windows Server

Activate the following settings under Windows or Windows Server:

- Web management tools:

  - IIS management service
  - IIS management console
  - IIS management scripts and tools
  - IIS compatibility to IIS metabasis and IIS 6 management
  - Compatibility with WMI for IIS 6
- WWW Services > Shared HTTP Features:

  - Standard document
  - Static content
- WWW services > Application development features:

  - ASP
  - ISAPI extensions
  - ISAPI filters
- WWW services > Security:

  - Request filter
  - Standard authentication

    > **Note**
    >
    > If the logging functions are active with IIS, the log files must be monitored and deleted, if necessary. The event views should be configured so that the log files do not become too large.

##### Settings under Windows or Windows Server

Additionally activate the following settings in Windows 10 or Windows Server 2016:

- WWW services > Application development features:

  - .NET extensibility 3.5
  - .NET extensibility 4.6
  - ASP.NET 3.5
  - ASP.NET 4.6

##### Requirements

- Administrator rights
- Write access for the registry

##### Procedure

1. Open the dialog for the activation of Windows features from the Windows 10 Control Panel. In Windows Server 2016, use the settings for the server manager. For detailed information, refer to the help of the operating system.
2. In the settings for the Internet Information Services, enable the settings described above.
3. Close the dialog with the "OK" button. The required data is transferred and the IIS is configured accordingly.

##### Alternative procedure

You can also use the command line "Start > Run > cmd" to install the IIS components located on the installation data carrier:

pkgmgr.exe /iu:IIS-WebServerRole;IIS-WebServer;IIS-CommonHttpFeatures;IIS-RequestFiltering;IIS-StaticContent;IIS-DefaultDocument;IIS-HttpErrors;IIS-ASPNET;IIS-ASP;IIS-ISAPIExtensions;IIS-ISAPIFilter;IIS-BasicAuthentication;IIS-WindowsAuthentication;IIS-ManagementConsole;IIS-ManagementService;IIS-IIS6ManagementCompatibility;IIS-Metabase;IIS-WMICompatibility;IIS-ManagementScriptingTools

---

**See also**

[Software and hardware requirements (RT Professional)](WinCC%20WebUX%20%28RT%20Professional%29.md#software-and-hardware-requirements-rt-professional)
  
[Overview (RT Professional)](#overview-rt-professional)

#### Installing Microsoft Message Queuing (MSMQ) (RT Professional)

##### Introduction

WinCC uses the Message Queuing services from Microsoft. This component is a part of the operating system.

However, MS Message Queuing is not part of the default setting of the Windows installation and might have to be installed retrospectively.

> **Note**
>
> WinCC is generally authorized for use in a domain or workgroup.
>
> However, be aware that domain group policies and restrictions of the domain can hinder the installation. In this case, remove the computer from the domain prior to installing Microsoft Message Queuing, Microsoft SQL Server and WinCC. Log onto the computer in question locally with administrative rights. Then perform the installation. After successful installation, you can enter the WinCC computer back into the domain. If the domain group policies and restrictions of the domain do not impede the installation, the computer need not be removed from the domain during the installation.
>
> Be aware that domain group policies and restrictions of the domain can also hinder operation. If you cannot avoid these restrictions, run the WinCC computer in a workgroup.
>
> Consult with the domain administrator if needed.

##### Requirement

- Administrator rights
- Write access for the registry

##### Windows Procedure

1. Go to "Control Panel > Programs".
2. Click the "Enable or disable Windows features" button on the left menu bar.

   The "Windows Features" dialog box opens.
3. Activate the "Microsoft Message Queue (MSMQ) Server" component.

   The "Microsoft Message Queue Server Core Components" entry is activated.

   The subcomponents remain deactivated.
4. Click "OK" to confirm.

##### Windows Server  Procedure

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

[Overview (RT Professional)](#overview-rt-professional)

#### Installing the WebNavigator Server (RT Professional)

##### Requirements

- Local administrator rights
- Internet Information Services is installed
- Microsoft Message Queuing is installed

##### Procedure

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

   - WinCC Runtime Professional
   - WebNavigator Server
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
15. If the computer does not reboot, click "Exit".

**Note**

"English" is always installed as the basic product language.

**Note**

If no license key is found during installation, you have the option to transfer it to your PC. If you skip the license transfer, you can register it later with the Automation License Manager.

If the installation was successful, a message to this effect is displayed on the screen. If errors occurred during installation, an error message is displayed informing you of the type of errors.

##### WebNavigator server: WNUSR_DC92D7179E29 user

The "WNUSR_DC92D7179E29" user is created during the installation of the WinCC/WebNavigator server.

The user is only used internally. To keep the function of the web server, do not delete or change this user.

To increase the security of the system, change the password for the user regularly. Use the "CCSetWebNavPwd.exe" tool for this.

For more detailed information, refer to the WinCC/WebNavigator documentation:

- "WinCC/WebNavigator documentation > Configuring the WebNavigator system > Configuring the WebNavigator server > Setting up the WebNavigator website > [WinCC Web Configurator](#wincc-web-configurator-rt-professional)

##### Result

WinCC Runtime Professional and the WebNavigator Server are installed.

### Installation of WebNavigator client (RT Professional)

This section contains information on the following topics:

- [Installing the WebNavigator Client (RT Professional)](#installing-the-webnavigator-client-rt-professional)
- [User rights, user groups and optional installation possibilities (RT Professional)](#user-rights-user-groups-and-optional-installation-possibilities-rt-professional)
- [Internet Explorer Settings (RT Professional)](#internet-explorer-settings-rt-professional)
- [Installation from the DVD (RT Professional)](#installation-from-the-dvd-rt-professional)
- [Installation via the Intranet/Internet (RT Professional)](#installation-via-the-intranetinternet-rt-professional)

#### Installing the WebNavigator Client (RT Professional)

##### Introduction

You can install the WebNavigator Client as follows:

- Installation from the WinCC Runtime Professional Product DVD.

  In this case, certain Windows user rights are necessary, depending on the operating system.
- Installation via Intranet/Internet.

  In this case, certain Windows user rights are necessary, depending on the operating system.
- Installation without user interaction:

  - With the Windows user rights of the current user
  - Or using group policy based software distribution in networks

You can also install the WebNavigator Client additionally on the WebNavigator server . This is useful, for example, if you want to check your WinCC project locally on the server in the Internet Explorer.

> **Note**
>
> **.Net controls on the WebNavigator Client**
>
> If you want to use .Net controls on the WebNavigator client, you must install the .Net framework 4.0 or higher on the client from the WinCC product DVD.
>
> The .Net controls must not be copied into the Windows folder "Common Files". Use the following path instead:
>
> - <installation directory>WinCC\WebNavigator\Client\bin

##### WinCCViewerRT

The "WinCCViewerRT" web viewer is installed together with the WebNavigator Client.

##### Procedure

1. Entry and check of the settings of the client computer in Internet Explorer.
2. Installation of the WebNavigator Client.

   > **Note**
   >
   > When you install from the DVD or through group policy based software distribution, you can upgrade an older version of the WebNavigator Client directly without removal.  
   > If you install Web Navigator Server on a computer after the WebNavigator Client, you need to reinstall the client.
   >
   > **Plug-in reinstallation**
   >
   > With the installation of WebNavigator Client V7.0 or higher, the "User Archive Control", "FunctionTrend Control", "Hardcopy" and "Web Client" plug-ins are already integrated in the client.
   >
   > If a WebNavigator Client V7.0 or higher is connected to a WebNavigator Server less than V7.0 (e.g. V6.2 SP3), these plug-ins are available for installation in the download section of the Web navigation interface.
   >
   > The plug-ins are already installed. Do not reinstall the plug-ins.

##### Setup and installation of the WebNavigator Client

- Before installing a new version on the WebNavigator Client via a download, check the languages installed on the client and connected server.  
  After installing the client via download, only the languages of the connected server are available on the client computer.
- The setup of the WebNavigator Client is canceled with the error message "WinCC Active" if:

  - the local WinCC project is open
  - the local WinCC project has been opened since the computer was last restarted.

  Restart the computer.   
  Check if WinCC has been entered in the Autostart directory. If required, remove the item and reboot the computer. The WebNavigator Client is being installed.
- At least 70 MB free disk space must be available on the local hard drive to install the WebNavigator Client.   
  Otherwise, the installation aborts with a corresponding message.
- When installing the WebNavigator Client by downloading it from the Intranet/Internet, you can select between "Open" and "Save" for the Setup file. If you subsequently install plug-ins or ActiveX controls, you must choose the procedure that was selected when you installed the software for the first time. Otherwise, the error message "Error 1316" of the "MSI Installer" appears.
- The latest cumulative security update for Internet Explorer must be installed before installing via download.  
  For more information, see the Microsoft Update [KB3072449](#installation-via-the-intranetinternet-rt-professional).
- In the download area of the Web Navigation user interface, the Plug-Ins which can be installed are displayed.   
  At least the same minimum user rights are required as for installation of the WebNavigator Client to install this plug-in.   
  If you select a plug-in in the Web Navigation user interface, the WebNavigator Client Setup starts. You have to confirm the selected plug-in again.

##### Upgrading the WebNavigator Client

When you connect a web client to a web server, the system checks that the client has the same version installed as the web server.

If an older version is available, you can upgrade the WebNavigator client when accessing the web project.

If the client is a 64-bit computer, an additional link for installing "Visual C++ Redistributable" is displayed during installation via an intranet or the Internet.

You must perform this installation first, because the installation is a prerequisite for the web client.

##### Upgrade from WinCC V6.2 SP3

Perform a repair installation after upgrading from WinCC V6.2 SP3.

Start the WinCC/WebNavigator Client installation in the control panel via "Uninstall or change program" and select "Repair".

Otherwise, controls may have to be installed subsequently during operation.

Then restart the computer.

##### Installing the WebNavigator Client under Windows Server

You cannot install the WebNavigator Client under Windows Server with user rights lower than "Administrator" with the default setting for group policies.   
In the group policy, enable the installation of WebNavigator client by

- Assigning and publishing the software
- Under "Administrative Templates / Windows Components / Windows Installer", enable the setting "Always install with elevated privileges". You must activate "Never" for the "Disable Windows Installer" option.
- You must activate "Never" for the "Disable Windows Installer" option.

---

**See also**

[Microsoft Update KB3072449](https://support.microsoft.com/en-us/help/3072449/installation-of-activex-controls-may-fail-in-internet-explorer)

#### User rights, user groups and optional installation possibilities (RT Professional)

##### Windows user rights required for installation and initial registration of the WebNavigator client

"Administrator" rights are required to install the WebNavigator client via Intranet/Internet or using the WinCC Runtime Professional Product DVD. For the initial registration of the client on the WebNavigator server, you need to use the same name as that used during installation and must log on with the same or higher Windows user rights. The connections must be established successfully. All subsequent logons can then be performed by users with different Windows user rights, which may be more restricted.

##### Installing the WebNavigator client with restricted user rights

With the employed MSI technology, you can also install the WebNavigator client with restricted Windows user rights. This procedure can be set during the installation using the group policy based software distribution in networks.

The add-ons and plug-ins for the WebNavigator client can also be installed this way.

##### Installation for a configured group of users or computers

Using the Microsoft Systems Management server or group policy on a Domain Controller, it is possible to install a group of users or computers configured by the Administrator.

- For this the MSI file "WinCCWebNavigatorClient.msi" is published at the Domain Controller and enabled for a user group. Then, depending on the configuration of the group policy based software distribution, you perform the installation either during logon of the specified users or when the computer boots.
- When using a Microsoft Systems Management Server, the installation is configured by the administrator, triggered and executed when the relevant computer boots.

##### Group policy based software distribution

The software installation is normally executed with the access rights of the current Windows user. When using MSI technology, the installation is performed by an operating system service with a higher level of rights. This enables you to perform installations for which the Windows user is lacking permission. Applications which require higher-level permissions for installation are referred to as "privileged installations" in MSI technology. Installation of these applications is possible when a Windows user is assigned the "Always install with elevated privileges" permission.

To use group policy based software distribution, a group policy is created on the domain controller. The software to be distributed is assigned or published using the active directory .

- Assignment: The software distribution can be assigned to a user or a computer. The software to be distributed is automatically installed when the user logs on or computer boots.
- Publication: The software distribution can be published for single users. When the user logs onto the client computer, the software to be distributed appears in a dialog and can be selected for installation.

##### Installation without user interaction

During installation of the WebNavigator client, the user is normally prompted to enter information, for examples, about the components to be installed. By implementing a configuration file, installation is possible without user interaction. The required path specification and user information are provided in the "options.ini" configuration file. The file must be in the same folder as the WebNavigator client Setup.   
This installation procedure is advantageous when using the group policy based software distribution.

Installation from the product DVD requires user interaction.

The settings given predefined in the table are used under the following conditions:

- The "options.ini" configuration file is missing and there is no corresponding entry available in the client registry, for example, due to another SIMATIC HMI product installed.
- Alternatively, the installation is performed via the group policy based software distribution with assignment to the computer.

| Information | Parameters |
| --- | --- |
| Target directory for the WebNavigator client | INSTALLDIR=" <syspath1>\Siemens\Automation\SCADA-RT_V11\WinCC\WebNavigator" |
| Target directory for common components | COMMONDIR=" <syspath2>\Siemens " |
| User information / user name | USER |
| User information / organization | COMPANYNAME |

The "<syspath?>" parameter is derived from the setting in the registry under the key "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion":

- "<syspath1>" corresponds to the key "ProgramFilesDir" e.g. "C:\\Program Files"
- "<syspath2>" corresponds to the key "CommonFilesDir", e.g. "C:\\Program Files\\Common Files"

##### Example of a configuration file "options.ini" for Windows

`[USERINFO]`

`USER=Integration`

`COMPANYNAME=Siemens AG`

`[INSTALLPATH]`

`COMMONDIR="C:\Program Files\Common Files\Siemens"`

`INSTALLDIR="C:\Program Files\Siemens\Automation\SCADA-RT_V11\WinCC\WebNavigator"`

`[FEATURES]`

`FUNCTIONTRENDCONTROL=0`

`HARDCOPY=0`

`WINCCUSERARCHIVES=0`

`DEU=0`

`FRA=0`

`ITA=0`

`ESP=0`

---

**See also**

[Installation via the Intranet/Internet (RT Professional)](#installation-via-the-intranetinternet-rt-professional)

#### Internet Explorer Settings (RT Professional)

##### Introduction

To have the full functionality available on the WebNavigator client, you need to adapt the security settings in Internet Explorer.

##### Procedure

1. Click "Tools" > "Internet Options" in the Internet Explorer.
2. Select the "Security" tab. Select the corresponding zone, e.g. "Local Intranet" or "Internet".

   ![Procedure](images/27041231243_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/27041231243_DV_resource.Stream@PNG-en-US.png)
3. Click "Custom Level".

   ![Procedure](images/27041226763_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/27041226763_DV_resource.Stream@PNG-en-US.png)
4. Select the options "Script ActiveX controls marked safe for scripting" and "Download signed ActiveX controls".
5. Select the "Active Scripting" option under "Scripting".
6. Click "OK". Carry out the modifications in the subsequent dialog.
7. Select the "Trusted Sites" icon. Open the "Trusted Sites" with the "Sites" button.
8. Enter the address of the WebNavigator server in the "Add this Website to the zone" field. Possible formats and wildcards include "*://157.54.100 - 200", "ftp://157.54.23.41", or "http://*.microsoft.com". If necessary, clear the "Require server verification for all sites in this zone (https:) check box. Click "Add". Click "Close".
9. Select the "Trusted Sites" icon. Click the "Standard level" button and then the "Custom Level" button. Activate the "Activate" option under "Initialize and script ActiveX controls not marked as safe". Click "OK".
10. Click on the "General" tab. Click on the "Settings" button in the "Browser History" area . Select the "Automatic" option under "Check for newer versions of stored pages". Click "OK".
11. Close the "Internet Options" dialog by clicking "OK".

#### Installation from the DVD (RT Professional)

##### Requirements

- The information provided in [Software and hardware requirements](#software-and-hardware-requirements-rt-professional) applies to the installation and use of the WebNavigator client.
- Minimum user rights are required to install the WebNavigator Client depending on the operating system, see [User rights, user groups and optional installation possibilities](#user-rights-user-groups-and-optional-installation-possibilities-rt-professional).

##### Procedure

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
7. Open the program group "SIMATIC WinCC WebNavigator" and select the "Web Navigator Client" component.
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
15. If the computer does not reboot, click "Exit".

**Note**

"English" is always installed as the basic product language.

**Note**

If no license key is found during installation, you have the chance to transfer it to your PC. If you skip the license transfer, you can register it later with the Automation License Manager.

If the installation was successful, a message to this effect is displayed on the screen. If errors occurred during installation, an error message is displayed informing you of the type of errors.

##### Result

The WebNavigator Client is installed and has been added as a function in the navigation window of the WinCC Explorer.

#### Installation via the Intranet/Internet (RT Professional)

##### Requirements

- The information provided in [Installing the WebNavigator Client](#installing-the-webnavigator-client-rt-professional) applies to the installation and use of the WebNavigator Client.
- Minimum user rights are required to install the WebNavigator client depending on the operating system, see [User rights, user groups and optional installation possibilities](#user-rights-user-groups-and-optional-installation-possibilities-rt-professional).
- WebNavigator Server must be installed on a computer. The Internet Information Server must be configured with the WinCC Web Configurator. Users must be registered in the WinCC User Administrator. The WinCC project must be in runtime.
- The most recent Microsoft cumulative security update for Internet Explorer must be installed. This applies to all installed versions of Internet Explorer.  
  For more information, see the following Microsoft article [KB3072449](https://support.microsoft.com/en-us/help/3072449/installation-of-activex-controls-may-fail-in-internet-explorer).
- The required Microsoft Visual C++ Redistributable must be installed on the WebNavigator client with 64-bit computer before the connection to the WebNavigator server is established.

##### Procedure

1. Enter the address of the WebNavigator server in the address line of the Internet browser. When installing in a virtual directory, the address can be as follows: "http://www.servername/WebNavigator/".
2. Enter the user name and the password.
3. If you are accessing the WebNavigator Server for the first time you will be prompted to install the WebNavigator Client.   
   If the client is a 64-bit computer, an additional link is displayed to install "Visual C++ Redistributable". You must perform this installation first, because the installation is a prerequisite for the web client.
4. Click the "Click here to install WebNavigator Client" link. In the "File Download" dialog, click "Save". It is recommended to save the client setup on the target computer because the setup need not be downloaded again if a restart of the client computer is required.
5. Leave the Internet Explorer open and open Windows Explorer. Navigate to the directory in which you saved the setup file. Start Setup by double-clicking the file.
6. Follow the instructions on the screen. Enter the required information and settings. The client-end controls of the WebNavigator are installed. Close the Setup dialog.

**Note**

If you have installed the WebNavigator client without installing the Visual C++ Redistributable beforehand, you can install the software later.   
Select the "Web Navigator and System Updates" menu in the "Download area" of the navigation interface of "MainControl.asp".

If you want to install a more current version for an existing WebNavigator client via the Intranet/Internet, go directly to the client setup. You do not need to save the installation file on the target computer. If you want to save the new installation file, remove the old installation file. Or save the new version of the file in another directory.

##### Result

When the installation is completed successfully, the WebNavigator client switches to the WinCC project currently in runtime.

> **Note**
>
> If you want to use the screen keyboard, you must also install .net 4.0 or higher. If the WebNavigator Client is installed via the WinCC DVD, .net 4.0 is already included.

---

**See also**

[Installing the WebNavigator Client (RT Professional)](#installing-the-webnavigator-client-rt-professional)
  
[User rights, user groups and optional installation possibilities (RT Professional)](#user-rights-user-groups-and-optional-installation-possibilities-rt-professional)

### Installing the Web Diagnostics Client (RT Professional)

#### Introduction

The software for the Web Diagnostics Client is installed from the WinCC Runtime Professional Product DVD on the client computer.

#### Requirements

- To do this, you must have administrator rights.

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
7. Open the program group "SIMATIC WinCC Web Navigator" and select the "Diagnostics Client" component.
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
15. If the computer does not reboot, click "Exit".

**Note**

"English" is always installed as the basic product language.

**Note**

If no license key is found during installation, you have the chance to transfer it to your PC. If you skip the license transfer, you can register it later with the Automation License Manager.

If the installation was successful, a message to this effect is displayed on the screen. If errors occurred during installation, an error message is displayed informing you of the type of errors.

#### Result

1. The Web Diagnostics Client is installed.

## Configuring the Web Navigator system (RT Professional)

This section contains information on the following topics:

- [Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)
- [Configuring a WinCC project (RT Professional)](#configuring-a-wincc-project-rt-professional)
- [Transferring a WinCC project (RT Professional)](#transferring-a-wincc-project-rt-professional)
- [Configuring the Web Navigator Server (RT Professional)](#configuring-the-web-navigator-server-rt-professional)
- [Differences to the WinCC Basic System (RT Professional)](#differences-to-the-wincc-basic-system-rt-professional)
- [Functions (RT Professional)](#functions-rt-professional)

### Overview of configuration steps (RT Professional)

#### Requirements

- The server PC and client PC are interconnected via TCP/IP.
- On the server PC

  - Internet Information Service is installed.
  - The WebNavigator server is installed.
  - A license key is installed.
  - WinCC Runtime Professional is installed.
- On the client PC

  - Internet Explorer V11 is installed.

  or

  - WinCCViewerRT is installed.

#### Basic procedure

The following configurations are required to set up a WebNavigator system:

1. Configure the WinCC project in the TIA Portal. For more information about the TIA Portal, refer to "Getting started with the TIA Portal"

   - Configure WinCC screens for Web access.
   - Create users for WebNavigator client access
   - Observe restrictions
   - Compiling a project
2. Transfer your WinCC project to the server PC. If the configuration PC and the WebNavigator server are interconnected, transfer the WinCC project using the command "Load to device > Software (all)".
3. Configure the WebNavigator Web page on the WebNavigator server.
4. Operate the WinCC project.

   - Using WinCCViewerRT
   - Using Internet Explorer

### Configuring a WinCC project (RT Professional)

This section contains information on the following topics:

- [Configuring WinCC screens for Web access (RT Professional)](#configuring-wincc-screens-for-web-access-rt-professional)
- [WinCC screens as a gadget (RT Professional)](#wincc-screens-as-a-gadget-rt-professional)
- [Configuring runtime settings (WebNavigator) (RT Professional)](#configuring-runtime-settings-webnavigator-rt-professional)
- [Managing users for the Web Navigator Client (RT Professional)](#managing-users-for-the-web-navigator-client-rt-professional)
- [Limitations (RT Professional)](#limitations-rt-professional)

#### Configuring WinCC screens for Web access (RT Professional)

##### Configuring individual WinCC screens for Web access

1. Double-click the desired screen in the project tree. The screen opens and the screen properties are shown in the Inspector window.
2. In the Inspector window, click "Properties > Properties > Web access".
3. Activate "Web access".

or

1. Select the desired screen in the project tree.
2. Select "Web access" command in the shortcut menu.

##### Configuring several screens for Web access

1. Select "Screens" in the project tree.
2. Select the "Web access for all" command in the shortcut menu.

##### Result

The WinCC screens are configured for Web access. During compilation of the project, the WinCC screens are adapted for access via the Intranet/Internet and published on the WebNavigator server.

For more information, refer to "[Transferring a WinCC project](#transferring-a-wincc-project-rt-professional)".

##### Start screen and start language on the WebNavigator client

> **Note**
>
> You have the option to define a start screen and a start language for the WebNavigator client in the ActiveX control UserAdminControl.

---

**See also**

[Transferring a WinCC project (RT Professional)](#transferring-a-wincc-project-rt-professional)

#### WinCC screens as a gadget (RT Professional)

This section contains information on the following topics:

- [Gadget on the Web Navigator Server (RT Professional)](#gadget-on-the-web-navigator-server-rt-professional)
- [Gadget on the Web Navigator Client (RT Professional)](#gadget-on-the-web-navigator-client-rt-professional)

##### Gadget on the Web Navigator Server (RT Professional)

###### Introduction

Using the "Gadget" property, you define which screens to group in a gadget. Gadgets are mini applications for the Windows sidebar. In order to use gadgets, a WebNavigator client must always be installed as well on the WebNavigator server.

The following operating systems support gadgets:

- Windows 10 (Professional, Enterprise)
- Windows 11 (Professional, Enterprise)
- Windows Server 2019
- Windows Server 2022

###### Procedure

To configure WinCC screens as a gadget, proceed as follows:

1. Double-click the desired screen in the project tree. The screen is opened and the screen properties are shown in the Inspector window.
2. In the Inspector window, click "Properties > Properties > Web access".
3. Enable "Gadget" and "Web access".
4. Save the WinCC project.
5. Select the "Compile > Software" command in the shortcut menu of the HMI device.

###### Result

The screens are assembled for the gadget on the WebNavigator server. As soon as the project is in runtime, the WebNavigator server generates a jpg snapshot image "pdlImage.jpg" of each screen at cyclic intervals and in consecutive order.

The file is stored in the directory "\WinCC\Webnavigator\Server\Web\image\_gadget". The gadget accesses this file cyclically.

Note that user interactions are not possible in the screens displayed. This includes, for example, calls from login dialogs or notice dialogs via functions.

The following objects are not supported for the display in a gadget:

- GSC diagnostics window
- Media Player

  > **Note**
  >
  > The WinCC project shown in the gadget cannot be operated.

##### Gadget on the Web Navigator Client (RT Professional)

###### Introduction

In order to use gadgets, a WebNavigator client must always be installed as well on the WebNavigator server. A preconfigured gadget for displaying WinCC screens is located on the WebNavigator client in the installation directory under "\WinCC\Webnavigator\GADGET".

The following operating systems support gadgets:

- Windows 10 (Professional, Enterprise)
- Windows 11 (Professional, Enterprise)
- Windows Server 2019
- Windows Server 2022

###### Requirement

The screens have been published and configured as a "Gadget" on the WebNavigator Server.

###### Procedure

To access the gadget with the WebNavigator client, proceed as follows:

1. Double-click on the "_WebNavigator.gadget" gadget in the installation directory under "\WinCC\Webnavigator\GADGET". The Gadget is installed under Windows in the Sidebar.
2. Define the update cycle in which the gadget loads a screen from the WebNavigator server, every 17 seconds for example.
3. Enter the address of the WebNavigator server. The gadget establishes a connection to the WebNavigator server.
4. If necessary, drag-and-drop the gadget onto the desktop.

#### Configuring runtime settings (WebNavigator) (RT Professional)

##### Introduction

You can configure the behavior in runtime in the "Runtime settings" editor.

##### Procedure

1. Open the "Runtime Settings > Web Navigator" editor.

   ![Procedure](images/96374677771_DV_resource.Stream@PNG-en-US.png)
2. To use the "WinCC Classic" design, activate "Use "WinCC-classic" design".
3. To use your own cursor as a "View only cursor", enter the path and file name of the cursor at "View only" cursor. Alternatively, navigate to the file of the desired cursor using the "…" button.
4. To change the maximum number of concurrent connections, enter the desired number in the "Maximum number of concurrent connections" field.
5. To change the maximum number of open tabs in the browser, enter a suitable value in the "Maximum number of tabs per browser" field. Internet Explorer V11 supports this setting.

   > **Note**
   >
   > **Server load settings**
   >
   > Each tab that calls the server homepage uses a license on the server PC. A connection setting of "10" and a tab setting of "2" corresponds to 20 clients. A license for at least 20 clients must be available on the server PC.
6. Define whether the local user group is disabled on the WebNavigator Server.
7. To output an appropriate system message when a WebNavigator logs on and off, activate "Enable event log messages".

##### Result

The settings for Runtime are configured.

---

**See also**

[Operating a WinCC project (RT Professional)](#operating-a-wincc-project-rt-professional-1)
  
[Setting up WinCCViewerRT (RT Professional)](#setting-up-winccviewerrt-rt-professional)

#### Managing users for the Web Navigator Client (RT Professional)

This section contains information on the following topics:

- [Administration of users for the WebNavigator client (RT Professional)](#administration-of-users-for-the-webnavigator-client-rt-professional)
- [Administration of user groups for the WebNavigator client (RT Professional)](#administration-of-user-groups-for-the-webnavigator-client-rt-professional)

##### Administration of users for the WebNavigator client (RT Professional)

###### Introduction

You must configure the following for each user to be logged on to the Web client (WebNavigator or WebUX):

- A start screen of your choice enabled for web access
- A language of your choice
- Number of reserved licenses (for WebUX)

This allows you to make various sections of a project immediately accessible or inaccessible for users.

> **Note**
>
> New users who want to access through a Web client or a WebUX client on the system, can only be created in the engineering system.
>
> When you create a user in Runtime with the user view, it is not possible to assign a Web startup screen to this user. This user is therefore not authorized to access the Web.
>
> Neither can existing users be granted web access rights in Runtime.

###### Requirements

- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.

###### Procedure

1. Double-click the "Runtime settings" editor in the project window.
2. Click "User administration".
3. In the "Users" tab, select a user for whom you want to make the settings.
4. In the Inspector window, select "Properties > Properties > Web options".
5. Under "WebNavigator settings", click the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Start screen" selection list.

   A dialog box for selecting the start screen opens.
6. Select the "Start" screen.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Repeat steps 5 to 7 to set a start screen for WebUX.
9. Under "Reserved number of licenses", you configure the number of reserved WebUX licenses for the selected user using the ![Procedure](images/84603730955_DV_resource.Stream@PNG-de-DE.png) button.
10. To configure a language for the user, click the ![Procedure](images/84609363851_DV_resource.Stream@PNG-de-DE.png) button under "Options" in the "Web language" selection list.

    A dialog box for selecting the language opens.
11. Select the desired language as the runtime language of the web user.

**Note**

If more reserved licenses are configured than are available on the WebUX server, only the first users listed under the user administration are taken into consideration.

**Note**

If the "Use WebNavigator licenses for WebUX" option is selected, no reserved WebUX licenses can be guaranteed.

Alternatively, you can make these settings in the shortcut menu by selecting the columns "WebNavigator start screen", "WebUX start screen" and "Web language" and "Licenses reserved for WebUX" and making the respective configuration.

> **Note**
>
> The language setting is retained when the user becomes part of a new group. However, the start screen is overwritten.

> **Note**
>
> By default, the WebNavigator licenses are used for WebUX. If you want to use these licenses separately, clear the "Use WebNavigator licenses for WebUX" check box under "Runtime settings > Web access".

> **Note**
>
> Users can now also log off manually from the WebNavigator client using the ODK function "PWRTLogout()". You can find one description of the function in the Runtime API documentation under "Functions of the user administration > Functions for logon, logoff".

##### Administration of user groups for the WebNavigator client (RT Professional)

###### Introduction

For each user group to be administered for web clients, you must configure the following:

- A start screen of your choice enabled for web access
- A language of your choice
- Number of reserved licenses (for WebUX)

This allows you to make various sections of a project immediately accessible or inaccessible for users.

> **Note**
>
> The name of the user group has to be unique within the project. Otherwise the input is not accepted.

###### Requirements

- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.
- The "Web operators" user group has been created.

###### Procedure

1. Double-click the "Runtime settings" editor in the project window.
2. Click "User administration".
3. In the "User groups" tab, select the user group "Web operators".
4. In the Inspector window, select "Properties > Properties > Web options".
5. Under "WebNavigator settings", click the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Start screen" selection list.

   A dialog box for selecting the start screen opens.
6. Select the "Start" screen for runtime.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Repeat steps 5 to 7 to set a start screen for WebUX.
9. To configure a language for the user group, click the ![Procedure](images/84609363851_DV_resource.Stream@PNG-de-DE.png) button under "Options" in the "Web language" selection list.

   A dialog box for selecting the language opens.
10. Select the desired language as the runtime language of the user group.

Alternatively, you can make these settings in the shortcut menu by selecting the columns "WebNavigator start screen", "WebUX start screen" and "Web language" and making the respective configuration.

> **Note**
>
> The name of the user group is language-dependent. You can specify the name in several languages and switch between languages in runtime.

#### Limitations (RT Professional)

##### Introduction

You can use your projects already created with WinCC to also make them available via the Internet/ Intranet.

Essentially, the step consists in publishing the already created WinCC screens and using user administration to set up Web users.

The current version of the Web Navigator has a number of restrictions with regard to functionality, and as a "thin client" solution does not support all the functions offered by a standard WinCC basic system.

You may therefore have to check your existing WinCC projects for these restrictions and if applicable, adapt them.

##### Functionality restrictions

When using non-supported functions, the user will be informed of this in Runtime with plain text messages.

- The Web Navigator Client only offers the view of a running WinCC project. A configuration of the WinCC Server projects via the Web Navigator Client is not possible.
- Only those WinCC option packages/add-ons can run on the Web Navigator Client, whose documentation expressly states that.
- Not all Runtime API functions are supported on the Web Navigator Client. A list of the functions supported is provided in the Appendix.
- The "Reports" editor is an integrated reporting system of WinCC for the time-triggered or event-triggered documentation of alarm messages, operations and log contents. This reporting system is not supported via the Intranet/Internet. Thus, the output of reports is, for example, only possible on the Web Navigator Server and WinCC client.
- No separate logging system is running on the Web Navigator Client. The message log and message system can only be operated and monitored.
- C functions are created and executed in the project of the WinCC server. Functions cannot run on the Web Navigator Client.
- If VB functions are used, there are only minor restrictions due to non-supported functions. If non-supported functions are used in a VB function, an alarm is output.

##### Use of special characters

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

> **Note**
>
> **Names of screens**
>
> The names of screens must not contain double underscores, e.g. "__furnace_overview.pdl".
>
> The string before the two underscores is interpreted as a server prefix.

### Transferring a WinCC project (RT Professional)

#### Requirement

- A WinCC project is configured
- WebNavigator server is installed on the server PC.
- The configuration PC and server PC are interconnected.

#### Online transfer

Transfer the WinCC project using the command "Load to device > Software (all)". The project is compiled prior to the download. The screens are adapted for access via Intranet/Internet during compilation.

During the download to the server PC, the configured WinCC project is transferred and the screens are published on the WebNavigator server. For more information, refer to "[Compiling and loading](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#runtime-professional-rt-professional)".

---

**See also**

[Runtime Professional (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#runtime-professional-rt-professional)
  
[Configuring WinCC screens for Web access (RT Professional)](#configuring-wincc-screens-for-web-access-rt-professional)

### Configuring the Web Navigator Server (RT Professional)

This section contains information on the following topics:

- [Setting up the Web Navigator Web site (RT Professional)](#setting-up-the-web-navigator-web-site-rt-professional)
- [Setting up a firewall (RT Professional)](#setting-up-a-firewall-rt-professional)
- [Checking the Activated Web Site (Web) (RT Professional)](#checking-the-activated-web-site-web-rt-professional)

#### Setting up the Web Navigator Web site (RT Professional)

This section contains information on the following topics:

- [WinCC Web Configurator (RT Professional)](#wincc-web-configurator-rt-professional)
- [Creating a New Standard Web site (Stand-Alone) (RT Professional)](#creating-a-new-standard-web-site-stand-alone-rt-professional)
- [Creating a virtual folder (RT Professional)](#creating-a-virtual-folder-rt-professional)

##### WinCC Web Configurator (RT Professional)

###### Introduction

The Internet Information Service (IIS) is set up and managed with the WinCC Web Configurator.

###### Requirement

- WebNavigator Server is installed.
- Internet Information Service is installed.

###### Starting WinCC Web Configurator:

In the Start menu, select "Start > All Programs > Siemens Automation > Option and Tools > HMI Tools" > WinCC Web Configurator".

###### Initial configuration with the WinCC Web Configurator

During the initial configuration, you specify whether you want to create a new default Web site or a new virtual folder.

![Initial configuration with the WinCC Web Configurator](images/2992242443_DV_resource.Stream@PNG-en-US.png)

- If you only wish to operate the WinCC WebNavigator Web site on your server, activate the option "Create a new standard Web site (stand-alone)".
- If the WinCC WebNavigator Web site is to be added as a subdirectory to your existing Web, activate the option "Add to an existing Web site (virtual folder)".

  This option is necessary if the previous default Web site must remain active or if the operating system supports only the operation of one website.

###### Configuration management with the WinCC Web Configurator

If the IIS is already configured, change the settings of the existing Web server or virtual directory with the WinCC Web Configurator.

The Web Configurator automatically detects whether a configuration already exists. If a configuration already exists, the dialog for changing the configuration opens.

> **Note**
>
> **Web folder has been changed or deleted**
>
> If you have deleted the web folder, restart the computer before you create a new web folder with the Web Configurator.
>
> Note the following:
>
> - When you change the Web folder and your Web communication is no longer established, the Web Configurator attempts to correct the settings.
> - If this does not work, follow these steps:
>
>   - Exit the IIS console.
>   - To delete the WebNavigator website, enter the following command line in the Windows "Run" window:
>
>     "<wincc_installation_path>\WebNavigator\Server\bin\WinCCWebConfigurator.exe" deinstall="yes".
>   - Start the desired website in the IIS console, for example, the standard website.

###### Internal user "WNUSR_DC92D7179E29"

The "WNUSR_DC92D7179E29" user is created during the installation of the WinCC/WebNavigator server.

The user is only used internally. To keep the function of the web server, do not delete or change this user.

To increase the security of the system, you can currently only change the password for the user once. Use the "CCSetWebNavPwd.exe" tool for this.

###### Password requirements

Make sure that the passwords comply with the usual security policies.

Minimum requirements:

- 8 characters
- 1 uppercase letter
- 1 lowercase letter
- 1 number
- 1 special character

###### Requirements

- You have administrator rights on the web server.
- The website is configured with the WinCC Web Configurator .

###### Procedure: Changing the password

1. Open the following file in the installation path:

   - ...\WinCC\Webnavigator\Server\bin\CCSetWebNavPwd.exe

   The Windows command prompt opens.
2. Enter the new password.
3. Confirm the password.
4. To close the window, press any key.

For help with the tool, enter the following line in the Windows command prompt:

- CCSetWebNavPwd.exe /?

##### Creating a New Standard Web site (Stand-Alone) (RT Professional)

###### Requirement

- WinCC WebNavigator is installed.
- Internet Information Service is installed
- WinCC Web Configurator is started

  > **Note**
  >
  > If you have any questions or experience problems with the following settings, contact your Intranet/Internet administrator.

###### Procedure

Proceed as follows to create a standard Web site:

1. Select "Create a new standard Web site (stand-alone)" and click "Next".

   ![Procedure](images/2992261515_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/2992261515_DV_resource.Stream@PNG-en-US.png)
2. Enter the name of your Web site in the "Name of the Web site" field.
3. In the "Port" field, enter the port number used for access.
4. In the "IP address" field specify whether the PC is to be reached in the Intranet, Internet or in both networks. Only use addresses from the selection list.

   If you want to make your PC accessible via the Intranet and the Internet, select "All not assigned".
5. Define the standard Web site that is displayed after selecting the Web server on the WebNavigator Client

   - MainControl.asp

     Starts the WinCC Navigation interface. You need the navigation interface, for example, for download installation.
   - WebClient.asp

     Opens the start screen configured in user administration after login.
6. Define the time interval after which the WebNavigator Clients automatically start to establish a connection following a connection breakdown. If "0 s" is set, the "Automatic connection establishment" function is disabled.
7. Define the way the Web site is started after configuration.
8. If you have not activated a firewall, click "Finish". If you have installed a firewall, click "Next".

###### Result

The Web directory has been created and the Web page is activated. If you have activated the firewall, configure the firewall settings with the Web Configurator.

##### Creating a virtual folder (RT Professional)

###### Requirement

- Internet Information Service is installed
- WinCC WebNavigator is installed.
- WinCC Web Configurator is started

  > **Note**
  >
  > If you have any questions or experience problems with the following settings, contact your Intranet/Internet administrator.

###### Procedure

Proceed as follows to create a virtual directory:

1. Select "Add to an existing Web site (virtual folder)". Click "Browse."
2. In the following dialog, select the active Web site to which the virtual directory is to be added.

   ![Procedure](images/2992325259_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/2992325259_DV_resource.Stream@PNG-en-US.png)
3. Click "OK" to close the dialog box. Click the "Next" button in the following dialog.

   ![Procedure](images/2992350603_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/2992350603_DV_resource.Stream@PNG-en-US.png)
4. Enter the name of your Web site in the "Name of the Web site" field.
5. The WinCC Web Configurator takes the IIS settings for the port number and IP address.
6. Define the standard Web site that is displayed after selecting the Web server on the WebNavigator Client.

   - MainControl.asp

     Starts the WinCC Navigation interface. You need the navigation interface, for example, for download installation.
   - WebClient.asp

     Opens the start screen configured in user administration after logon.
7. Define the time interval after which the WebNavigator Clients automatically start to establish a connection following a connection breakdown. If "0 s" is set, the "Automatic connection establishment" function is disabled.
8. Define the way the Web site is started after configuration.
9. Click "Finish" to complete the configuration.

###### Result

The virtual Web directory has been created and the Web site is activated. To access the Web site, with the WebNavigator Client, add the name of the virtual Web directory to the URL, for example http://WebServer/WebNavigator.

###### No Active Website

If no active Web is found, the WinCC Web Configurator terminates with a message.

![No Active Website](images/2992267787_DV_resource.Stream@PNG-en-US.png)

Click "OK" to close the dialog box.

To execute the Web Configurator again, first activate a Web site. For additional information, refer to "Checking of Activated Web site".

#### Setting up a firewall (RT Professional)

##### Introduction

This section describes only the activation of the "HTTP" and "HTTPS" services for port 80 in the respective operating system.

To set up the Windows firewall with advanced security, or for a different port, contact your network administrator.

##### Requirement

- You have created a standard Web site using the Web Configurator.
- The firewall is activated.
- A logged on Windows user has administrator rights

##### Procedure

To set up the firewall for a standard port, proceed as follows:

1. Click "Windows Firewall" in the "WinCC Web Configurator".
2. The "Windows Firewall" dialog will open.
3. In Windows or Windows Server, click "Allow an app or feature through Windows Firewall".
4. Activate "Secure WWW Services (HTTPS)" or "WWW Services (HTTP)".
5. Exit the open Windows dialogs with "OK".
6. Click "Finish" in the Web Configurator. The configuration of the server will be completed.

#### Checking the Activated Web Site (Web) (RT Professional)

> **Note**
>
> Note that the operating system settings shown depend on the language set for the operating system.

##### Procedure

Proceed as follows to check the activated website:

1. In the Start menu, select "Programs" > "Administrative Tools" > "Internet Services Manager".

   ![Procedure](images/23020422539_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23020422539_DV_resource.Stream@PNG-en-US.png)
2. Click the name of the PC in the "Connections" area.
3. Click "Default Web Site".
4. Check the information displayed for the websites. If "Stopped" is displayed next to the desired Web site, e.g. "WebNavigator", start the Web site.
5. To start the Web site, select the "Start" command in the shortcut menu.

### Differences to the WinCC Basic System (RT Professional)

This section contains information on the following topics:

- [Functional restrictions (RT Professional)](#functional-restrictions-rt-professional)
- [Using Scripts (RT Professional)](#using-scripts-rt-professional)
- [Using tags (RT Professional)](#using-tags-rt-professional)

#### Functional restrictions (RT Professional)

##### Introduction

The WebNavigator has certain functional restrictions compared to the WinCC basic system. You should therefore check your WinCC projects for these restrictions and adjust the project settings as required.

##### Overview

When you use functions that are not supported in a project, corresponding messages are generated in Runtime to draw your attention to the fact.

The following restrictions apply to the WebNavigator Client:

- The client provides only a view of the running WinCC project.

  It is not possible to configure the WinCC Server projects.
- You can only use WinCC options and WinCC add-ons if specified explicitly in the documentation.
- Not all "Runtime API functions" are supported.
- The message archive and message system can only be operated and monitored.
- "Alarm view" does not support the property "Loop-in alarm".

  For the correct display of message blocks, the "Apply project settings" option cannot be activated. You will find the option in the "Alarm view" Inspector window under "Properties > Properties > Blocks".
- The hotkeys configured in WinCC are not supported. Operator control using the tab key is supported.
- National special characters in names of process pictures or referenced graphics are not supported on the Internet.
- The overlap lock in process pictures is not supported.
- The advanced zoom functions cannot be disabled. If you do not want to employ the zoom functions, do not use a wheel mouse with "auto-scroll" setting on the client.
- The redundancy switch is only supported on the dedicated web server.

---

**See also**

[Using Scripts (RT Professional)](#using-scripts-rt-professional)
  
[Using tags (RT Professional)](#using-tags-rt-professional)

#### Using Scripts (RT Professional)

##### Scripts running exclusively for the WebNavigator

In order to run scripts only on the WebNavigator, use the pre-processor definition "RUN_ON_WEBNAVIGATOR" in the script in ANSI-C or the function "IsWebNavigator" in the script in VBS.

**Example for ANSI-C**

Copy code

void OnOpenPicture (char* lpszPictureName, char* lpszObjectName, char* lpszPropertyName)

{

#ifdef RUN_ON_WEBNAVIGATOR

// Code used for WebNavigator

#else

// Code used for WinCC without WebNavigator

#endif

}

**Example for VBS**

Copy code

If IsWebNavigator() Then

// Code used for WebNavigator

Else

// Code used for WinCC without WebNavigator

End If

##### Visual Basic Script

There are only slight restrictions imposed by unsupported functions when VBS is used. A list of these functions is available at "[Unsupported functions](#unsupported-functions-rt-professional)".

##### Global user-defined functions

You configure the functions on the WinCC server in the server project.

Global functions cannot run on the WebNavigator client. Global functions on the server are supported.

User-defined functions may contain unsupported functions and in this case cannot run on the WebNavigator client. Check and correct the scripts, if necessary. Insert the following condition, for example: "#ifdef RUN_ON_WEBNAVIGATOR".

> **Note**
>
> The maximum number for global functions is 8 for the type "sub" and 7 for the type "func". The restrictions do not apply to Runtime Professional.

##### Functions with a tag trigger

The WebNavigator queries tags at cyclic intervals of "1 second". The update cycle of trigger tag "upon change" is also one second.

This can temporarily result in an increased communication load. Take into account the increased load if communication is run at full capacity.

If additional tags are requested in tag-triggered functions and their names are generated with string functions, for example, unknown tags can only be read synchronously. Enter the tag names you are using in the trigger list in order to avoid extended selection times.

##### Functions for picture selection and deselection

In contrast to the basic system, a picture is downloaded in asynchronous mode when WebNavigator is used. Account for this fact when using scripts that contain picture changes.

If picture selection is triggered for a picture window within a function, objects of the new picture cannot subsequently be accessed from within that function. The picture is not yet loaded at this time. A time delay such as "Sleep(2000)" does not help as the function and Internet Explorer wait. Execute the subsequent parts of the function in the "OpenPicture" function, which is triggered once the picture is loaded.

If you call further functions following picture selection in a function, the functions will be executed with error or not at all. The picture context is lost due to the picture deselection.

##### Synchronous functions

Synchronous functions produce a very high system load.

You should therefore not use the "SetTagxxx" function in cyclic functions. The server will be overloaded when many clients call the "SetTagxxx" functions in a fast cycle, e.g. 1 sec or less.

Note that the following function calls are sent to the server synchronously:

- Functions that write a tag in synchronous mode and then wait for the result, e.g. "xxxWait"
- C-API calls

Frequent use of these functions reduces the performance of the WebNavigator client. In the case of an Internet connection, the duration of these calls may even be in the seconds range.

Script functions that manipulate the objects in the displayed picture are of no concern since no data traffic takes place between the client and server.

##### Nested picture technique and cyclic functions

Many synchronous calls in a picture may reduce performance, for example, in the following cases:

- More than ten windows are configured in a picture window.
- Cyclic functions are used in the windows with synchronous calls, for example "SetTagxxx".

Timeouts may mean that some functions cannot be executed.

The following elements are supported in a window:

- 16 windows with cyclic functions.
- 31 windows without cyclic functions.

---

**See also**

[Functional restrictions (RT Professional)](#functional-restrictions-rt-professional)
  
[Using tags (RT Professional)](#using-tags-rt-professional)

#### Using tags (RT Professional)

##### Computer-local tags

The WebNavigator Client supports computer-local tags with the following restrictions:

- When a dedicated web server is used, only the computer-local tags of that server are available on the client. The tags on the client cannot assume their own values.
- Computer-local tags of the subordinate WinCC servers cannot have their own values on the client.
- The start value of computer-local text tags can only contain characters that are allowed in tag names. If the start value of a text tag contains a colon, for example, the tag is not recognized on the client.
- Computer-local tags are not supported on the client when User Archives are used, because User Archives can only identify the local tags of the server, but not the tags of the WebNavigator Client.

##### Defining the local picture function tag

Do not use WinCC tags for the WebNavigator if picture-specific data is saved in functions.

The reading or writing of data in scripts always generates data traffic to the server. This places a load on the communication.

You can save picture-specific data as follows:

- Configure "hidden" graphic objects so that you can use their properties as picture-specific tags. Actions are executed at the object properties upon changes to the stored values.
- You have created the hidden "static text" object, for example. The "Text" property is used to store any texts, while the color properties are used to store any colors. The properties are read and written using functions. These properties affect the status of the picture without a round trip to the server being required.

---

**See also**

[Functional restrictions (RT Professional)](#functional-restrictions-rt-professional)
  
[Using Scripts (RT Professional)](#using-scripts-rt-professional)

### Functions (RT Professional)

This section contains information on the following topics:

- [Supported functions (RT Professional)](#supported-functions-rt-professional)
- [WaitForDocumentReady (RT Professional)](#waitfordocumentready-rt-professional)
- [Unsupported Functions (RT Professional)](#unsupported-functions-rt-professional-1)

#### Supported functions (RT Professional)

##### Introduction

The following list shows the functions supported by WebNavigator.

Functions not included in this list are not automatically enabled for the WebNavigator.

##### Functions

| Symbol | Meaning |
| --- | --- |
| WaitForDocumentReady |  |

| Symbol | Meaning |
| --- | --- |
| Get_Focus | GetTagChar |
| GetAssignments | GetTagCharState |
| GetBasePicture | GetTagCharStateWait |
| GetFlashPicture | GetTagCharWait |
| GetFontName | GetTagMultiStateWait |
| GetInputValueChar | GetTagMultiWait |
| GetLastChange | GetText |
| GetOutputFormat | SetTagMultiWait |
| GetOutputValueChar | SetTagMultiStateWait |
| GetPictureName | SetTagRaw |
| GetPropChar | SetTagRawState |
| GetServerName | SetTagRawStateWait |

| Symbol | Meaning |
| --- | --- |
| AXC_OnBtnArcLong | AXC_OnBtnMsgNext |
| AXC_OnBtnArcShort | AXC_OnBtnMsgPrev |
| AXC_OnBtnComment | AXC_OnBtnMsgWin |
| AXC_OnBtnEmergAckn | AXC_OnBtnScroll |
| AXC_OnBtnInfo | AXC_OnBtnSelect |
| AXC_OnBtnLock | AXC_OnBtnSinglAckn |
| AXC_OnBtnLoop | AXC_OnBtnVisibleAckn |
| AXC_OnBtnMsgFirst | AXC_SetFilter |
| AXC_OnBtnMsgLast |  |

| Symbol | Meaning |
| --- | --- |
| OnBtnArcLong | OnBtnMsgLast |
| OnBtnArcShort | OnBtnMsgNext |
| OnBtnComment | OnBtnMsgPrev |
| OnBtnEmergAckn | OnBtnMsgWin |
| OnBtnHornAckn | OnBtnPrint |
| OnBtnInfo | OnBtnScroll |
| OnBtnLanguage | OnBtnSelect |
| OnBtnLock | OnBtnSinglAckn |
| OnBtnLoop | OnBtnVisibleAckn |
| OnBtnMsgFirst |  |

| Symbol | Meaning |
| --- | --- |
| TLGGetTemplateParameter | TlgTableWindowPressPrevButton |
| TLGPressToolbarButton | TlgTableWindowPressPrevItemButton |
| TlgGetColumnPosition | TlgTableWindowPressStartStopButton |
| TlgGetNumberOfColumns | TlgTrendWindowPressFirstButton |
| TlgGetNumberOfRows | TlgTrendWindowPressLastButton |
| TlgGetNumberOfTrends | TlgTrendWindowPressLinealButton |
| TlgGetRowPosition | TlgTrendWindowPressNextButton |
| TlgGetRulerArchivNameTrend | TlgTrendWindowPressNextItemButton |
| TlgGetRulerTimeTrend | TlgTrendWindowPressOneToOneButton |
| TlgGetRulerValueTrend | TlgTrendWindowPressOpenArchiveVariableSelectionDlgButton |
| TlgGetRulerVariableNameTrend | TlgTrendWindowPressOpenDlgButton |
| TlgGetTextAtPos | TlgTrendWindowPressOpenItemSelectDlgButton |
| TlgTableWindowPressFirstButton | TlgTrendWindowPressOpenTimeSelectDlgButton |
| TlgTableWindowPressLastButton | TlgTrendWindowPressPrevButton |
| TlgTableWindowPressNextButton | TlgTrendWindowPressPrevItemButton |
| TlgTableWindowPressNextItemButton | TlgTrendWindowPressStartStopButton |
| TlgTableWindowPressOpenArchiveVariableSelectionDlgButton | TlgTrendWindowPressZoomInButton |
| TlgTableWindowPressOpenItemSelectDlgButton | TlgTrendWindowPressZoomOutButton |
| TlgTableWindowPressOpenTimeSelectDlgButton |  |

| Symbol | Meaning |
| --- | --- |
| GetLanguage | GetParentPicture |
| SetLanguage | GetParentPictureWindow |
| GetLink | GetServerTagPrefix |
| SetLink | OpenPicture |
| GetLinkedVariable | SetPictureDeactivated |
| GetLocalPicture | SetPictureDown |
| SetMultiLink | SetPictureUp |
| RPTJobPrint |  |

|  |  |  |
| --- | --- | --- |
| _makepath | fscanf | setvbuf |
| _splitpath | fsetpos | sprintf |
| abs | ftell | srand |
| abort | fwrite | sscanf |
| asctime | getc | strcat |
| atexit | getchar | strcmp |
| atof | getenv | strcpy |
| atoi | gets | strchr |
| atol | gmtime | strcspn |
| bsearch | labs | strerror |
| calloc | ldiv | strftime |
| clearerr | localtime | strlen |
| clock | malloc | strncat |
| ctime | memchr | strncmp |
| difftime | memcmp | strncpy |
| div | memcpy | strpbrk |
| exit | memmove | strrchr |
| fclose | memset | strspn |
| feof | mktime | strstr |
| ferror | perror | strtod |
| fflush | printf | strtok |
| fgetc | putc | strtol |
| fgetpos | putchar | strtoul |
| fgets | puts | SysMalloc |
| fopen | qsort | system |
| fprintf | rand | time |
| fputc | realloc | ungetc |
| fputs | remove | vfprintf |
| freopen | rename | vprintf |
| fread | rewind | vsprintf |
| free | scanf |  |
| fseek | setbuf |  |

| Symbol | Meaning |
| --- | --- |
| Check | ProgramExecute |

|  |  |  |
| --- | --- | --- |
| GetActualPointLeft | GetExponent | GetPicDeactTransparent |
| GetActualPointTop | GetExtendedOperation | GetPicDeactUseTransColor |
| GetAdaptBorder | GetFillColor | GetPicDownReferenced |
| GetAdaptPicture | GetFilling | GetPicDownTransparent |
| GetAdaptSize | GetFillingIndex | GetPicDownUseTransColor |
| GetAlarmHigh | GetFillStyle | GetPicReferenced |
| GetAlarmLow | GetFillStyle2 | GetPicTransColor |
| GetAlignment | GetFlashBackColor | GetPicUpReferenced |
| GetAlignmentLeft | GetFlashBorderColor | GetPicUpTransparent |
| GetAlignmentTop | GetFlashFlashPicture | GetPicUpUseTransColor |
| GetAssumeOnExit | GetFlashForeColor | GetPicUseTransColor |
| GetAssumeOnFull | GetFlashPicReferenced | GetPictureDeactivated |
| GetAverage | GetFlashPicTransColor | GetPictureDown |
| GetAxisSection | GetFlashPicUseTransColor | GetPictureUp |
| GetBackBorderWidth | GetFlashRateBackColor | GetPointCount |
| GetBackColor | GetFlashRateBorderColor | GetPosition |
| GetBackColor2 | GetFlashRateFlashPic | GetPressed |
| GetBackColor3 | GetFlashRateForeColor | GetProcess |
| GetBackColorBottom | GetFontBold | GetPropBOOL |
| GetBackColorTop | GetFontItalic | GetPropDouble |
| GetBackFlashColorOff | GetFontSize | GetPropLong |
| GetBackFlashColorOn | GetFontUnderline | GetPropWord |
| GetBasePicReferenced | GetForeColor | GetRadius |
| GetBasePicTransColor | GetForeFlashColorOff | GetRadiusHeight |
| GetBasePicUseTransColor | GetForeFlashColorOn | GetRadiusWidth |
| GetBitNumber | GetGrid | GetRangeMax |
| GetBorderBackColor | GetGridColor | GetRangeMin |
| GetBorderColor | GetGridHeight | GetReferenceRotationLeft |
| GetBorderColorBottom | GetGridWidth | GetReferenceRotationTop |
| GetBorderColorTop | GetHeight | GetRightComma |
| GetBorderEndStyle | GetHiddenInput | GetRotationAngle |
| GetBorderFlashColorOff | GetHotkey | GetRoundCornerHeight |
| GetBorderFlashColorOn | GetHysteresis | GetRoundCornerWidth |
| GetBorderStyle | GetHysteresisRange | GetScaleColor |
| GetBorderWidth | GetIndex | GetScaleTicks |
| GetBoxAlignment | GetInputValueDouble | GetScaling |
| GetBoxCount | GetItemBorderBackColor | GetScalingType |
| GetBoxType | GetItemBorderColor | GetScrollBars |
| GetButtonColor | GetItemBorderStyle | GetSelBGColor |
| GetCaption | GetItemBorderWidth | GetSelTextColor |
| GetCheckAlarmHigh | GetLanguageSwitch | GetSizeable |
| GetCheckAlarmLow | GetLayer | GetSmallChange |
| GetCheckLimitHigh4 | GetLeft | GetStartAngle |
| GetCheckLimitHigh5 | GetLeftComma | GetToggle |
| GetCheckLimitLow4 | GetLimitHigh4 | GetToleranceHigh |
| GetCheckLimitLow5 | GetLimitHigh5 | GetToleranceLow |
| GetCheckToleranceHigh | GetLimitLow4 | GetTop |
| GetCheckToleranceLow | GetLimitLow5 | GetTrend |
| GetCheckWarningHigh | GetLimitMax | GetTrendColor |
| GetCheckWarningLow | GetLimitMin | GetTypeAlarmHigh |
| GetClearOnError | GetListType | GetTypeAlarmLow |
| GetClearOnNew | GetLongStrokesBold | GetTypeLimitHigh4 |
| GetCloseButton | GetLongStrokesOnly | GetTypeLimitHigh5 |
| GetColorAlarmHigh | GetLongStrokesSize | GetTypeLimitLow4 |
| GetColorAlarmLow | GetLongStrokesTextEach | GetTypeLimitLow5 |
| GetColorBottom | GetMarker | GetTypeToleranceHigh |
| GetColorChangeType | GetMax | GetTypeToleranceLow |
| GetColorLimitHigh4 | GetMaximizeButton | GetTypeWarningHigh |
| GetColorLimitHigh5 | GetMin | GetTypeWarningLow |
| GetColorLimitLow4 | GetMoveable | GetUnselBGColor |
| GetColorLimitLow5 | GetNumberLines | GetUnselTextColor |
| GetColorToleranceHigh | GetOffsetLeft | GetUpdateCycle |
| GetColorToleranceLow | GetOffsetTop | GetVisible |
| GetColorTop | GetOnTop | GetWarningHigh |
| GetColorWarningHigh | GetOperation | GetWarningLow |
| GetColorWarningLow | GetOperationMessage | GetWindowBorder |
| GetCursorControl | GetOperationReport | GetWindowsStyle |
| GetDataFormat | GetOrientation | GetWidth |
| GetDirection | GetOutputValueDouble | GetZeroPoint |
| GetEditAtOnce | GetPasswordLevel | GetZeroPointValue |
| GetEndAngle | GetPicDeactReferenced | GetZoom |

|  |  |  |
| --- | --- | --- |
| Set_Focus | SetEditAtOnce | SetPicDownUseTransColor |
| SetActualPointLeft | SetEndAngle | SetPicTransColor |
| SetActualPointTop | SetExponent | SetPicUpTransparent |
| SetAlarmHigh | SetExtendedOperation | SetPicUpUseTransColor |
| SetAlarmLow | SetFillColor | SetPicUseTransColor |
| SetAlignment | SetFilling | SetPictureName |
| SetAlignmentLeft | SetFillingIndex | SetPointCount |
| SetAlignmentTop | SetFillStyle | SetPosition |
| SetAssumeOnExit | SetFillStyle2 | SetPressed |
| SetAssumeOnFull | SetFlashBackColor | SetProcess |
| SetAverage | SetFlashBorderColor | SetPropBOOL |
| SetAxisSection | SetFlashFlashPicture | SetPropDateTime |
| SetBackBorderWidth | SetFlashForeColor | SetPropChar |
| SetBackColor | SetFlashPicTransColor | SetPropDouble |
| SetBackColor2 | SetFlashPicUseTransColor | SetPropLong |
| SetBackColor3 | SetFlashRateBackColor | SetPropWord |
| SetBackColorBottom | SetFlashRateBorderColor | SetRadius |
| SetBackColorTop | SetFlashRateFlashPic | SetRadiusHeight |
| SetBackFlashColorOff | SetFlashRateForeColor | SetRadiusWidth |
| SetBackFlashColorOn | SetFontBold | SetRangeMax |
| SetBasePicTransColor | SetFontItalic | SetRangeMin |
| SetBasePicUseTransColor | SetFontName | SetRightComma |
| SetBitNumber | SetFontSize | SetReferenceRotationLeft |
| SetBorderBackColor | SetFontUnderline | SetReferenceRotationTop |
| SetBorderColor | SetForeColor | SetRotationAngle |
| SetBorderColorBottom | SetForeFlashColorOff | SetRoundCornerHeight |
| SetBorderColorTop | SetForeFlashColorOn | SetRoundCornerWidth |
| SetBorderEndStyle | SetHeight | SetScaleColor |
| SetBorderFlashColorOff | SetHiddenInput | SetScaleTicks |
| SetBorderFlashColorOn | SetHysteresis | SetScaling |
| SetBorderStyle | SetHysteresisRange | SetScalingType |
| SetBorderWidth | SetIndex | SetSelBGColor |
| SetBoxAlignment | SetItemBorderBackColor | SetSelTextColor |
| SetBoxCount | SetItemBorderColor | SetSmallChange |
| SetBoxType | SetItemBorderStyle | SetStartAngle |
| SetButtonColor | SetItemBorderWidth | SetText |
| SetCheckAlarmHigh | SetLeft | SetTop |
| SetCheckAlarmLow | SetLeftComma | SetTrend |
| SetCheckLimitHigh4 | SetLimitHigh4 | SetTrendColor |
| SetCheckLimitHigh5 | SetLimitHigh5 | SetToleranceHigh |
| SetCheckLimitLow4 | SetLimitLow4 | SetToleranceLow |
| SetCheckLimitLow5 | SetLimitLow5 | SetToggle |
| SetCheckToleranceHigh | SetLimitMax | SetTypeAlarmHigh |
| SetCheckToleranceLow | SetLimitMin | SetTypeAlarmLow |
| SetCheckWarningHigh | SetLongStrokesBold | SetTypeLimitHigh4 |
| SetCheckWarningLow | SetLongStrokesOnly | SetTypeLimitHigh5 |
| SetClearOnError | SetLongStrokesSize | SetTypeLimitLow4 |
| SetClearOnNew | SetMarker | SetTypeLimitLow5 |
| SetColorAlarmHigh | SetMax | SetTypeToleranceHigh |
| SetColorAlarmLow | SetMin | SetTypeToleranceLow |
| SetColorBottom | SetNumberLines | SetTypeWarningHigh |
| SetColorChangeType | SetOffsetLeft | SetTypeWarningLow |
| SetColorLimitHigh4 | SetOffsetTop | SetUnselBGColor |
| SetColorLimitHigh5 | SetOperation | SetUnselTextColor |
| SetColorLimitLow4 | SetOperationMessage | SetVisible |
| SetColorLimitLow5 | SetOperationReport | SetWarningHigh |
| SetColorToleranceHigh | SetOrientation | SetWarningLow |
| SetColorToleranceLow | SetOutputValueChar | SetWindowsStyle |
| SetColorTop | SetOutputValueDouble | SetWidth |
| SetColorWarningHigh | SetPasswordLevel | SetZeroPoint |
| SetColorWarningLow | SetPicDeactTransparent | SetZeroPointValue |
| SetCursorControl | SetPicDeactUseTransColor | SetZoom |
| SetDirection | SetPicDownTransparent |  |

|  |  |  |
| --- | --- | --- |
| GetTagBit | GetTagDateTime | GetTagByteStateQCWait |
| GetTagByte | GetTagDoubleWait | GetTagCharStateQC |
| GetTagDouble | GetTagDWordWait | GetTagCharStateQCWait |
| GetTagDWord | GetTagFloatWait | GetTagDoubleStateQC |
| GetTagFloat | GetTagRawWait | GetTagDoubleStateQCWait |
| GetTagRaw | GetTagSByteWait | GetTagDWordStateQC |
| GetTagSByte | GetTagSDWordWait | GetTagDWordStateQCWait |
| GetTagSDWord | GetTagSWordWait | GetTagFloatStateQC |
| GetTagSWord | GetTagWordWait | GetTagFloatStateQCWait |
| GetTagWord | GetTagBitStateWait | GetTagRawStateQC |
| GetTagBitState | GetTagByteStateWait | GetTagRawStateQCWait |
| GetTagByteState | GetTagDoubleStateWait | GetTagSByteStateQC |
| GetTagDoubleState | GetTagDWordStateWait | GetTagSByteStateQCWait |
| GetTagDWordState | GetTagFloatStateWait | GetTagSDWordStateQC |
| GetTagFloatState | GetTagRawStateWait | GetTagSDWordStateQCWait |
| GetTagRawState | GetTagSByteStateWait | GetTagSWordStateQC |
| GetTagSByteState | GetTagSDWordStateWait | GetTagSWordStateQCWait |
| GetTagSDWordState | GetTagSWordStateWait | GetTagValueStateQC |
| GetTagSWordState | GetTagWordStateWait | GetTagValueStateQCWait |
| GetTagWordState | GetTagBitStateQC | GetTagWordStateQC |
| GetTagBitWait | GetTagBitStateQCWait | GetTagWordStateQCWait |
| GetTagByteWait | GetTagByteStateQC | GetTagMultiStateQCWait |

|  |  |  |
| --- | --- | --- |
| SetTagBit | SetTagFloatState | SetTagSWordWait |
| SetTagByte | SetTagRawState | SetTagWordWait |
| SetTagDouble | SetTagSByteState | SetTagBitStateWait |
| SetTagDWord | SetTagSDWordState | SetTagByteStateWait |
| SetTagFloat | SetTagSWordState | SetTagDoubleStateWait |
| SetTagRaw | SetTagWordState | SetTagDWordStateWait |
| SetTagSByte | SetTagBitWait | SetTagFloatStateWait |
| SetTagSDWord | SetTagByteWait | SetTagRawStateWait |
| SetTagSWord | SetTagDoubleWait | SetTagSByteStateWait |
| SetTagWord | SetTagDWordWait | SetTagSDWordStateWait |
| SetTagBitState | SetTagFloatWait | SetTagSWordStateWait |
| SetTagByteState | SetTagRawWait | SetTagWordStateWait |
| SetTagDoubleState | SetTagSByteWait |  |
| SetTagDWordState | SetTagSDWordWait |  |

##### Supported ODK Functions

PWRTCheckPermission

PWRTCheckAreaPermission

PWRTCheckPermissionOnArea

PWRTCheckPermissionOnPicture // Only the "permlevel" parameter is evaluated.

MSRTStartMsgService

MSRTStopMsgService

MSRTCreateMsg

MSRTCreateMsgInstanceWithComment

MSRTSetComment

PDLRTGetLink

PDLRTSetLink

PDLRTSetMultiLink

PDLRTGetPropEx // Only reading is supported.

PDLRTSetPropEx // Only setting is supported.

TXTRTConnect

TXTRTDisconnect

TXTRTGetInfoText

TXTRTGetInfoTextMC

##### Supported User Archive-Functions

> **Note**
>
> User archive functions must always start with "ua" in lower case.
>
> Functions beginning with the uppercase letters "UA" are ODK functions. These ODK functions are not supported on the WebNavigator Client.

|  |  |  |
| --- | --- | --- |
| uaArchiveClose | uaArchiveGetName | uaArchiveSetFieldValueLong |
| uaArchiveDelete | uaArchiveGetSort | uaArchiveSetFieldValueString |
| uaArchiveExport | uaArchiveImport | uaArchiveSetFilter |
| uaArchiveGetCount | uaArchiveInsert | uaArchiveSetSort |
| uaArchiveGetFieldLength | uaArchiveMoveFirst | uaArchiveUpdate |
| uaArchiveGetFieldName | uaArchiveMoveLast | uaArchiveWriteTagValues |
| uaArchiveGetFields | uaArchiveMoveNext | uaArchiveWriteTagValuesByName |
| uaArchiveGetFieldType | uaArchiveMovePrevious | uaConnect |
| uaArchiveGetFieldValueDate | uaArchiveOpen | uaDisconnect |
| uaArchiveGetFieldValueFloat | uaArchiveReadTagValues | uaGetLastError |
| uaArchiveGetFieldValueDouble | uaArchiveReadTagValuesByName | uaGetLastHResult |
| uaArchiveGetFieldValueLong | uaArchiveRequery | uaQueryArchive |
| uaArchiveGetFieldValueString | uaArchiveSetFieldValueDate | uaQueryArchiveByName |
| uaArchiveGetFilter | uaArchiveSetFieldValueDouble | uaReleaseArchive |
| uaArchiveGetID | uaArchiveSetFieldValueFloat |  |

##### Supported MBCS Functions

|  |  |  |
| --- | --- | --- |
| _ismbcalnum | _mbscat | _mbsncmp |
| _ismbcalpha | _mbschr | _mbsncpy |
| _ismbcdigit | _mbscmp | _mbsnicmp |
| _ismbcgraph | _mbscpy | _mbspbrk |
| _ismbclower | _mbsdec | _mbsrchr |
| _ismbcprint | _mbsicmp | _mbsspn |
| _ismbcpunct | _mbsinc | _mbsstr |
| _ismbcspace | _mbslen | _mbstok |
| _ismbcupper | _mbscspn | _mbctolower |
| _mbclen | _mbsncat | _mbctoupper |

#### WaitForDocumentReady (RT Professional)

##### Function

The function checks whether a picture is loaded in the specified picture window.

A difference must be made in the scripts of process pictures or project functions between the runtime environment of WinCC and of the WebNavigator Client. The following Compiler commands exist to this purpose:

- #ifdef RUN_ON_WEBNAVIGATOR
- #ifndef RUN_ON_WEBNAVIGATOR

This allows you to distinguish between WinCC and the WebNavigator Client in your configuration as follows:

- Script delay with "WaitForDocumentReady"
- Differing picture addressing
- Different function names for control system functions
- Functions that are not supported on the WebNavigator Client

##### Syntax in ANSI-C

int WaitForDocumentReady(LPCSTR lpszPictureWindow)

##### Parameters

**lpszPictureWindow**

Pointer to the name of the picture window that is opened in the WebNavigator Client.

The following addressing syntax is possible:

- Picture window "xxx" in the current screen: `./xxx`
- Picture window "yyy" in the child screen "xxx”: `./xxx/yyy`
- Picture window "xxx" in the parent screen: `../xxx`
- Picture window "xxx" in the parent picture of the parent screen: `../../xxx`
- Absolute path compatible with WinCC

##### Return value

|  | Value | Explanation |
| --- | --- | --- |
| TRUE | 0 | The picture window has been found and the status checked. |
| FALSE | -1 | The picture window has not been found. |

##### Example for ANSI-C

#ifdef RUN_ON_WEBNAVIGATOR

SetPropChar("../", "View", "PictureName", szViewName);

WaitForDocumentReady("../View");

#else

SetPropChar(lpszParent, "View", "PictureName", szViewName);

#endif

> **Note**
>
> The syntax of the code section for WebNavigator is not checked during compilation of the WinCC script and is checked only when the pictures are published.

##### Syntax in VBS

`Print.WaitForDocumentReady()`

##### Example for VBS

`If IsWebNavigator() Then`

`WaitForDocumentReady(PictureName) 'Byref`

`End If`

#### Unsupported Functions (RT Professional)

The following list is only an extract of the unsupported functions. The list contains the functions that are explicitly stated as being unsupported.

##### Functions

|  |  |  |
| --- | --- | --- |
| GetHWDiag | OnDeactivateExecute | ReportJob |
| GetHWDiagLevel | OnErrorExecute | RPTJobPreview |
| GetKopFupAwl | OnTime | RptShowError |
| GetKopFupAwlLevel | OpenPrevPicture |  |

**VBScript functions**

- HMIRuntime.Stop: Terminates Internet Explorer and WinCCViewerRT, but not WinCC Runtime.
- AlarmLogs Object
- DataLogs Object
- Logging Object
- Project Object

##### Functions That Are not Required:

- DeactivateRTProject: Terminates Internet Explorer and WinCCViewerRT, but not WinCC Runtime.
- ExitWinCC
- FillDiagnoseInTags
- InquireLanguage
- TraceText
- TraceTime

##### Other Functions

These functions are included in the functional scope in order to ensure error-free compilation on the WebNavigator Client. The functions are not supported by the WebNavigator Client.

|  |  |  |
| --- | --- | --- |
| AXC_OnBtnHornAckn | GetCursorMode | GmsgFunction |
| AXC_OnBtnPrint | SetCursorMode | MSRTMsgWinCommand |
| AXC_OnBtnProtocol |  | TlgTableWindowPressHelpButton |

## Operating a WinCC project (RT Professional)

This section contains information on the following topics:

- [Operating projects using WinCCViewerRT (RT Professional)](#operating-projects-using-winccviewerrt-rt-professional)
- [Operating projects in Internet Explorer (RT Professional)](#operating-projects-in-internet-explorer-rt-professional)
- [Use the "Hardcopy" function (RT Professional)](#use-the-hardcopy-function-rt-professional)

### Operating projects using WinCCViewerRT (RT Professional)

This section contains information on the following topics:

- [Setting up WinCCViewerRT (RT Professional)](#setting-up-winccviewerrt-rt-professional)
- [Operating a WinCC project (RT Professional)](#operating-a-wincc-project-rt-professional-1)

#### Setting up WinCCViewerRT (RT Professional)

##### Requirement

- On the server PC

  - The WebNavigator server is installed.
  - A license key is installed.
  - The WinCC project is in Runtime.
  - The WinCC screens are configured for Web access and published.
- On the client PC

  - WebNavigator client is installed.

##### Procedure

Set up WinCCViewerRT as follows:

1. In the Start menu, select "Start > All Programs > Siemens Automation > Option and Tools > HMI Tools" > WinCCViewerRT".
2. Enter the logon data in the "General" tab:

   ![Procedure](images/25756275595_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25756275595_DV_resource.Stream@PNG-en-US.png)

   - Server address: http://<server name>, or http://<IP address>
   - User name and password
3. In the "Parameters" tab, specify the Runtime language and whether to disable keystrokes that the operator uses to change to other programs.
4. Define the WinCC Runtime Professional properties in the "Graphics Runtime" tab:

   - Start screen
   - Configuration file for screen navigation
   - Window attributes
   - Illegal user actions
5. Specify additional user actions on the "Runtime" tab:

   - Automatic logout
   - Enable screen keyboard.
   - Use <Ctrl+Alt+Del> to switch to the Task Manager and to the operating system. This setting is only valid for the on-screen keyboard.
   - Open the "WinCCRTViewer" by means of keystroke. You can change the default keystroke <Ctrl+Alt+P>.
   - Define the printer via which you can print with the configured print job from the WinCC Controls.

     Alternatively, you can print the print job using the "RPTJobPrint" function. A preview via "RPTJobPreview" is not possible on the Web client.

   Close the dialog with "OK".

##### Result

WinCCViewerRT is configured. When the dialog is closed, the connection to the WebNavigator server is established. The settings are saved to the configuration file "WinCCViewerRT.xml". The settings in the configuration file are used at the next start of WinCCViewerRT.

The configuration file is stored in the directory "C:\Users\<User name>\Appdata\LocalLow\Siemens\SIMATIC.WinCC\WebNavigator\Client" . Under <User name>, enter the name of the user logged-on when the file is created. This allows different configurations to be used, depending on the logged on user. WinCCViewerRT applies the interface language from WinCC.

**Renaming or removing WinCCViewerRT.xml**

When you rename or remove the file WinCCViewerRT.xml, the configuration dialog of WinCCViewerRT is opened during the start. Reconfigure WinCCViewerRT, or select a different configuration file.

---

**See also**

[Configuring runtime settings (WebNavigator) (RT Professional)](#configuring-runtime-settings-webnavigator-rt-professional)

#### Operating a WinCC project (RT Professional)

##### Requirement

- On the server PC:

  - The "WinCC WebNavigator license is installed.
  - The WinCC project is in Runtime.
  - The WinCC screens are configured for Web access and published.
  - A user is created in WinCC.
- On the client PC

  - WinCCViewerRT is configured.

##### Procedure

To view screens, proceed as follows:

1. In the Start menu, select "Start > All Programs > Siemens Automation > Option and Tools > HMI Tools" > WinCCViewerRT".
2. Log on to the WebNavigator server:

   - If the user and password are configured in the "WinCCViewerRT" dialog, no logon dialog displayed.
   - If no user and password was configured in the "WinCCViewerRT" dialog, the logon dialog displayed. Enter the user name and password of the WinCC user. Click "OK".
3. Press the <Ctrl+Alt+P> keystroke to change the user. The "WinCCViewerRT" dialog opens.

   Enter the user name and password in the "General" tab.

   You can also select the xml file that contains this data.

##### Result

WinCCViewerRT connects to the selected WinCC project. The start screen configured for the user is displayed. Users can operate and monitor the project, depending on their authorizations.

If the user is assigned the authorization no. 1002 "Web access - view only", he/she can only view the project.

The cursor is a "View only cursor" and indicates that process-related operations are not allowed.

![Result](images/24565485195_DV_resource.Stream@PNG-de-DE.png)

Certain operations are still possible, such as opening the properties dialog of an online trend control.

If necessary, you can use your own cursor symbol as a "View only cursor". You can find more detailed information on this under "[Configuring runtime settings (WebNavigator)](#configuring-runtime-settings-webnavigator-rt-professional)".

---

**See also**

[Configuring runtime settings (WebNavigator) (RT Professional)](#configuring-runtime-settings-webnavigator-rt-professional)

### Operating projects in Internet Explorer (RT Professional)

This section contains information on the following topics:

- [Operating a WinCC project (RT Professional)](#operating-a-wincc-project-rt-professional-2)
- [Working with the Web navigation interface (RT Professional)](#working-with-the-web-navigation-interface-rt-professional)
- [Diagnosis of the Connections with "Status.html" (RT Professional)](#diagnosis-of-the-connections-with-statushtml-rt-professional)

#### Operating a WinCC project (RT Professional)

##### Requirement

- WebNavigator client is installed.
- A user for the WebNavigator Client has been created.
- Internet Explorer as of V11

##### Procedure

To operate the WinCC project, proceed as follows:

1. Enter the address of the WebNavigator Server in the address bar of Internet Explorer:

   - Standard website: "http://servername"
   - Web site in the virtual directory: "http://servername"
2. Confirm your entry
3. Type in the user name and password. Confirm your entry.

##### Result

The standard Web site is displayed. The appearance depends on the configuration.

If "WebClient.asp" is set, the WebNavigator Client starts with the start screen defined in user administration. For more information, refer to "[Managing users for the Web Navigator Client](#managing-users-for-the-web-navigator-client-rt-professional)".

If "MainControl.asp" is set, the WebNavigator client starts with the Web navigation interface. For more information, refer to "[Working with the Web navigation interface](#working-with-the-web-navigation-interface-rt-professional)".

---

**See also**

[Managing users for the Web Navigator Client (RT Professional)](#managing-users-for-the-web-navigator-client-rt-professional)
  
[Working with the Web navigation interface (RT Professional)](#working-with-the-web-navigation-interface-rt-professional)

#### Working with the Web navigation interface (RT Professional)

This section contains information on the following topics:

- [Structure (RT Professional)](#structure-rt-professional)
- [Functions (RT Professional)](#functions-rt-professional-1)

##### Structure (RT Professional)

###### Navigation interface menu

The Web Navigation interface combines various Web functions. The various functions are grouped in menus.

![Navigation interface menu](images/2992705419_DV_resource.Stream@PNG-en-US.png)

- "Change Server" menu:

  Switch to a different WebNavigator server or Sm@rtServer.
- Menu of the current server:

  - Screens: Display or screen navigation of the current WebNavigator Server.
  - Report tools: Installed tools such as "DataWorkbook" for the display and analysis of current process values and historic data.
  - Analysis tools: Installed tools such as "Dat@View" for the display of log data in tables and trends.
  - Diagnostics tools: Status.html for diagnosing the WinCC project and the connection to the WebNavigator server.
  - Additional tools: This can be expanded by the user.
  - Download area:

    The plug-ins which are stored on the WebNavigator Server in the directory "Install / Customize" are available, e.g download of add-ons for WebNavigator.
- "Settings" menu:

  - Settings for the WebNavigator Client, e.g. adaptation of screen size.
  - Define the printer via which you can print with the configured print job from the WinCC Controls.

    Alternatively, you can print the print job using the "RPTJobPrint" function. A preview via "RPTJobPreview" is not possible on the Web client.
- "Current" menu:

  Links to Web pages, such as "SIMATIC HMI", "WinCC" or "WinCC flexible".

  > **Note**
  >
  > The contents of the websites under "News" can be displayed based on the settings both in a new window as well as in an window already open in Internet Explorer. You can make the settings for opening new pages in the Internet Explorer or in your operating system.
- "Language" menu:

  Changing the language of the navigation interface. The standard version of the program includes five languages.

##### Functions (RT Professional)

###### User logon

When logging onto the WebNavigator server, the user can determine - through the address entered in Internet Explorer - whether he logs on via the Web navigation interface or the start page configured in the WinCC project.

- The address "http://<server_name>/webnavigator" opens the start page configured in the User Administrator following the logon.
- The address "http://<server_name>/webnavigator/maincontrol.asp" starts the Web navigation interface.

###### Change of the Server

A different server can be selected via the menu command "Change Server". Enter the address of the new WebNavigator server in the upper input box. Examples of possible input formats are described under "User Logon".   
In the lower field, a symbolic name can be entered, which is shown in the menu as the current WebNavigator server. If the name is not specified, the address of the WebNavigator server is displayed.

###### Expansion Options

**Menu**

The menu of the navigation interface can be expanded by additional menu entries and functions, for example, depending on the operational area. Extensions are configured in an XML file for this purpose. The XML file is saved on the WebNavigator server in the subdirectory "_custom_data". Further information is available in the topic "Extending the Web Navigation User Interface".

**Tools**

The menu command "Additional tools" can be expanded by the user to provide additional tools on the WebNavigator client.

**Plug-Ins**

The "Download Plug-Ins" menu command provides plug-ins that have been stored on the WebNavigator server in the folder "Install/Customize". In order to display the version name of a plug-in, it must have been assigned the format "Vxx.xx.xx.xx" or "xx.xx.xx.xx".

**Languages**

Adjustment of language options may be facilitated by adjusting the "Menu.xml" file. The languages are stored as CSV files on the WebNavigator server in the folder "_languages / <language_identifier>". When adding, these language files have to be referenced in the file "maincontrol.asp".

#### Diagnosis of the Connections with "Status.html" (RT Professional)

##### Introduction

You can call up status information via the WebNavigator server and the WebNavigator clients from a WebNavigator server or any WebNavigator client. The status information will provide information about which users access the WebNavigator server by which Web Navigator clients.

Access to this page is restricted to the users created in the "User Management" by WinCC.

##### Requirement

User is created in user administration.

##### Display "Status.html"

To view the "Status.html" diagnostic site, enter the appropriate address of the WinCC server on which WinCC Runtime runs in the address line:

- Standard website: "http://www.server_name.de/status.html"
- Web site in the virtual directory: "http://www.server_name.de/WebNavigator/status.html"
- Log in with your WinCC user name and password.

##### Status information

The status information is displayed in blocks within the HTML page. There is one information block for the WebNavigator server and one information block for each connected WebNavigator client. The information is only displayed in English.

![Status information](images/2992826891_DV_resource.Stream@PNG-de-DE.PNG)

Time specification is in UTC (i.e. minus one hour to CET; minus 2 hours to CEST).

**Structure of the Information Block of the WebNavigator server**

| Field | Description |
| --- | --- |
| Server Version | Displays the version number of the WebNavigator server (build no.) |
| Server File Date | reserved |
| License Count | Displays the number of licenses |
| Runtime Mode | Displays the status of Runtime, e.g. activated |
| Last Update | Date and time of the last refresh of the display |
| Connected WebNavigator client | Number of connected WebNavigator clients |
| Connected diagnostic clients | Number of connected diagnostic clients |
| Connected DataMonitor clients | Number of connected DataMonitor clients |

**Structure of the information blocks of the Web Navigator clients**

The information blocks of the connected clients are listed below the text "Logged on Users:". Each block has the name of the client as a header.

| Field | Description |
| --- | --- |
| Login | Login name of the current user |
| Time | Login time of the current user or also time of the most recent automatic reconnect. |
| Type | Type of WebNavigator client, such as Default, Demo, View Only |
| PID | Process ID of instance of WebNavigatorRT.exe on the WebNavigator server communicating with this WebNavigator client. |

##### Save status information

The displayed status information can be saved. To do this, use the "Save As" menu command in Internet Explorer and select "(*.txt)" as the file type.

If "(*.htm, *.html)" are selected, the contents displayed are not saved.

### Use the "Hardcopy" function (RT Professional)

#### Introduction

On the WebNavigator client it is possible to generate a hardcopy of the entire screen, of a section, or of the active window.

The hardcopy is output to the default printer by executing the "PrtScr.exe" application.

> **Note**
>
> **Limited functionality on the Web client**
>
> The "Hardcopy" function can be executed using the "Print" button on the WinCC Controls toolbar on the Web client. However, a screenshot of the web server will be taken if you click this button.
>
> Use the "PrtScr.exe" application instead of the "Print" button.

#### Requirement

- WebNavigator client is installed.

#### Starting the hardcopy application

The program is started on the WebNavigator client, for example, using the command input line, or a user-defined function.

The application is saved to the folder "...\Common Files\Siemens\BIN\". The hardcopy is triggered depending on the parameters used.

#### Examples of the command line

"C:\Program Files\Common Files\Siemens\BIN\PrtScr.exe" –infinit –hotkey="<ALT>+p"

Starts PrtScr.exe and waits for the <ALT>+p keystroke. The entire screen is printed when you press the keystroke.

#### Parameters

| Parameters | Function |
| --- | --- |
| -infinit | Used as parameter for launching PrtScr.exe on a system without WinCC. Always use the parameter in combination with "hotkey".  The print keystroke and output parameters are not determined in the WinCC project. They are transferred instead via command line input. The PrtScr.exe application is started and waits for the input of the print keystroke. The parameters were transferred once during startup. To edit these parameters close the PrtScr.exe application. Change the parameters and then restart PrtScr.exe . |
| -end | terminates an active instance of PrtScr.exe |
| -hardcopy | Starts PrtScr.exe, directly initiates a hard copy, and then waits for the keystroke.  Always use the parameters in combination with "infinit" and "hotkey". |
| -nomcp | Starts PrtScr.exe , creates the hardcopy, and closes PrtScr.exe. |
| /C= left;top;right;bottom | Starts PrtScr, directly triggers a hardcopy of the specified screen area, and then ends PrtScr.exe ( |
| -l | Prints in landscape format. |
| -hotkey="x" | Specifies the keystroke.   Valid characters and combinations:   <ALT>, <SHIFT>,<CTRL> +  {0-9, A-Z, 0xXX}  The hexadecimal notation "0xXX" can be used to specify the "Virtual Key Code". For more information on "Virtual-Key Codes", refer to the MSDN Library. |

## Setting up terminal services for Web Navigator (RT Professional)

This section contains information on the following topics:

- [Communication Using Terminal Services (RT Professional)](#communication-using-terminal-services-rt-professional)
- [Activating terminal services on the Windows server (RT Professional)](#activating-terminal-services-on-the-windows-server-rt-professional)
- [Setting Up a User with Access Rights to the Terminal Server (RT Professional)](#setting-up-a-user-with-access-rights-to-the-terminal-server-rt-professional)
- [Starting the Terminal Server Application on the Terminal Client (RT Professional)](#starting-the-terminal-server-application-on-the-terminal-client-rt-professional)

### Communication Using Terminal Services (RT Professional)

#### Communication by means of terminal services

To use the WebNavigator Client as a terminal client, do not use a proxy server between the terminal server and WebNavigator Server.

If the terminal server and WebNavigator Server are not installed on the same PC, the WebNavigator Client cannot access the Web Navigation server via the terminal services.

This problem can be solved in various ways:

- A minimal installation of WinCC without licenses is installed on the terminal server.
- After installing the WebNavigator Client, the file "CCEClient_service.vbs" is executed once on the terminal server. The file is located on the WebNavigator product DVD in the "\WebNavigator" directory. The Windows user right "Administrators" is required to execute the VBS file.

#### Access from the WebNavigator Client and WinCC clients to the WebNavigator Server

If a WebNavigator Client and a WinCC client access the WebNavigator Server, via terminal services in the former case, the WebNavigator Client, as a terminal client, may not open a Windows Desktop in its session.

The following options are available to ensure the Windows desktop is not opened on the WebNavigator Client when beginning a session:

- Direct entry in the terminal services configuration for all users.
- Enter Internet Explorer as the start program in computer management for individual users.

For more information, refer to the FAQs on the Internet, contribution ID 17498344.

### Activating terminal services on the Windows server (RT Professional)

#### Requirement

- Windows user with administrator rights
- Windows Server 2019 / Windows Server 2022

#### Procedure

Proceed as follows to activate terminal services:

1. Open Control Panel and double-click "Software".
2. Open the "Add or Remove Programs" dialog and click "Add or Remove Windows Components". The "Windows Components Wizard" opens.
3. Activate "Terminal server" and "Terminal server licensing".
4. Click "Next". Follow the instructions.

**Note**

Activate the terminal services on the server PC before you install the actual applications. Install the applications on the server PC via the "Add or Remove Programs" dialog of the Control Panel. If you install the application via the Control Panel, the application can be configured for all users. Otherwise, the application can only be used for the user who installed the application.

### Setting Up a User with Access Rights to the Terminal Server (RT Professional)

#### Requirements

The terminal server is installed.

#### Procedure

To set up a user for access to the terminal server, proceed as follows:

1. Go to "Control Panel > Administrative Tools > Computer Management > Local Users and Groups".
2. Select "New User" from the "Users" shortcut menu. The "New User" dialog is opened.
3. Click the "User" icon. Double-click the corresponding user. The user properties dialog opens.
4. Click the "Member of" tab. Click "Add". The "Select Group" dialog opens.
5. Add the group "Remote Desktop Users". Click "OK" to close all the open dialogs.
6. Check the membership of the new user in other groups. If required, add the user to a corresponding group to ensure that the user is assigned the necessary user rights.
7. Close "Computer Management".

### Starting the Terminal Server Application on the Terminal Client (RT Professional)

#### Requirement

- The terminal service on the Windows server is started.
- A user is set up for access to the terminal server.

#### Procedure

To start an application on the terminal server from the terminal client, proceed as follows:

1. On the terminal client, from the Start menu select the menu command "Programs" > Accessories > Communication > Remote Desktop Connection". The "Remote Desktop Connection" dialog opens.
2. Enter the name of the terminal server.
3. Click the "Connect" button. Log on as the user who was created for access to the terminal server.

#### Result

The connection is now established. The desktop of the terminal server is displayed. On the terminal server, start an application, e.g. the Web Navigator Client via Internet Explorer.

## Troubleshooting (RT Professional)

### No communication between Web Navigator server and client

If a provider (participating proxy, firewall) has activated Content Filtering for an Internet connection, Web Navigator communication is no longer possible. With content filtering, only certain contents of HTML pages are permitted. The communication is directed via a defined port to a certain IP address, e.g. of the WinCC server.

- You have to deactivate Smart Filtering for the IP address of the Web Navigator Server - as there are no viruses or HTML contents on the WinCC Server, filtering is not useful in this case.
- If the customer uses SSL technology, the data is transferred in encrypted form. Smart Filtering for content is therefore not possible.

### Connection Abort

In an Internet environment, aborted connections, delays and communication fluctuations may occur.

If the communication between the Web Navigator Client and Web Navigator Server is defect, the user receives an alarm on the Web Navigator Client.

The WebNavigator Client then automatically tries to establish a connection in order to restore the connection.

The delay between attempts to establish a connection can be configured with the Web Configurator. If the value "0" is set, the Web Navigator Client does not attempt to reconnect automatically. In this case a message appears on the web client asking you whether the connection is to be reestablished.

![Connection Abort](images/2993524107_DV_resource.Stream@PNG-de-DE.png)

Confirm this query to reestablish the connection.

### No Screens are Displayed

Make sure the correct Web site is activated on the PC running the Web Navigator Server.

### Wrong Start Screen

You have edited a new screen in the "Screens" editor.

- Compile and load the screen on the server PC.
- Delete the temporary Internet files in the Internet Explorer via "Tools" > "Internet Options".
