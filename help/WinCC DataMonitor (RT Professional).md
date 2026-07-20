---
title: "WinCC DataMonitor  (RT Professional)"
package: DataMonitorWCCPenUS
topics: 88
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC DataMonitor  (RT Professional)

This section contains information on the following topics:

- [The basics (RT Professional)](#the-basics-rt-professional)
- [Installing DataMonitor (RT Professional)](#installing-datamonitor-rt-professional)
- [Configuring the DataMonitor system (RT Professional)](#configuring-the-datamonitor-system-rt-professional)
- [Working with WinCCViewerRT (RT Professional)](#working-with-winccviewerrt-rt-professional)
- [Working with the WebCenter (RT Professional)](#working-with-the-webcenter-rt-professional)
- [Working with Trends and Alarms (RT Professional)](#working-with-trends-and-alarms-rt-professional)
- [Working with Excel Workbooks (RT Professional)](#working-with-excel-workbooks-rt-professional)
- [Working with reports (RT Professional)](#working-with-reports-rt-professional)

## The basics (RT Professional)

This section contains information on the following topics:

- [DataMonitor (RT Professional)](#datamonitor-rt-professional)
- [WinCCViewerRT (RT Professional)](#winccviewerrt-rt-professional)
- [WebCenter (RT Professional)](#webcenter-rt-professional)
- [Trends and Alarms (RT Professional)](#trends-and-alarms-rt-professional)
- [Excel workbooks (RT Professional)](#excel-workbooks-rt-professional)
- [Reports (RT Professional)](#reports-rt-professional)
- [Access rights (RT Professional)](#access-rights-rt-professional)
- [Checking certificates (RT Professional)](#checking-certificates-rt-professional)

### DataMonitor (RT Professional)

#### Introduction

WinCC DataMonitor consists of a server component and a client component. The DataMonitor Server makes functions for analyzing and displaying data available to the DataMonitor client. Access rights govern access to the functions.

- WinCCViewerRT

  Program for monitoring WinCC projects. The DataMonitor client is therefore a so-called "View Only Client".
- Excel Workbooks  
  Display of logged process values in an Excel table for analysis and storage in the Web or as a print template for reports
- Published Reports

  Creation of reports from WinCC print jobs, or from published Excel worksheets. This allows you, for example, to generate statistics and analyses of specific process or history data. The reports are saved in PDF format and can be forwarded by e-mail.
- WebCenter

  Central information portal for access to WinCC data via user-specific views, clearly structured WebCenter pages through user groups with individual user rights for reading, writing and creating WebCenter pages.
- Trends &amp; Alarms

  Serves to display logged process values and alarms. The data is displayed in tables and diagrams on predefined WebCenter pages.

#### Your benefit:

- Display and analysis of current process statuses on office PCs with, for example, MS Internet Explorer or MS Excel
- No additional configuration effort, as screens from the WinCC project are used directly.
- Evaluation via centrally administered templates for detailed analyses of corporate processes, e.g. reports, statistics
- Creation of event-driven or time-driven reports
- Information from the process is individually compiled online in runtime (information portal) and distributed to various people by e-mail.
- User administration with user groups and individual access authorizations, e.g. read, write, and creation of WebCenter pages

### WinCCViewerRT (RT Professional)

#### Overview

The Web Viewer is solely a display program for WinCC projects that is installed using the DataMonitor Client. DataMonitor Client is therefore a so-called "View Only Client".

Don't use Internet Explorer to run the "WinCCViewerRT.exe" application. Run it on the DataMonitor client instead.

The Web Viewer uses its own communication resources to access the DataMonitor server. This prevents Internet users from accessing the system and protects the system against viruses and Trojan horses.

Only the screens which are configured for Web access and published on the DataMonitor server are displayed.

The WinCC user needs the authorization no. 1002 "Web access - view only". The cursor is a "View only cursor" and indicates that process-related operations are not possible. Certain operations are still possible, such as opening the properties dialog of an online trend control.

If the WinCC user is not assigned authorization no. 1002, the DataMonitor Client runs in demo mode after logon.

You can also use the WebViewer as terminal services application. For more information, refer to "Setting up terminal services for WebNavigator servers".

---

**See also**

[Configuring runtime settings (DataMonitor) (RT Professional)](#configuring-runtime-settings-datamonitor-rt-professional)

### WebCenter (RT Professional)

#### Overview

The WebCenter is the central information portal for access to WinCC data via Intranet/Internet.

With the help of WebCenter pages and Web parts, the user can arrange and save his view of the WinCC data. WebCenter pages are stored in directories.

WebCenter pages are like a construction kit. The form of the construction kit is specified by layout master copies. Users can use either the supplied or self-created layout master copies.

Web parts are the individual building blocks that prepare and display data. Within the WebCenter pages, the parameter definitions are stored for the respective Web parts and can be called up again at any time. A multiple use of the same web part is also possible with different parameter definitions. The WebCenter pages that have been created in this way can be opened by different users with the same parameter definitions depending on the assignment of rights.

To transfer the configuration data to a different computer, copy the corresponding project directory:

- ..\WebCenter\App_Data\Webcenter

  ![Overview](images/23190457099_DV_resource.Stream@PNG-de-DE.png)

#### Web parts

Up to 15 of the following Web objects can be combined into one screen view:

- Process value table

  The available process values for the specified period are displayed.
- Process values in table (time step)

  The full archive name and the tag name are displayed as a tooltip in the header of the column.

  The process values are summarized beginning with the starting time in the specified time interval.

  The interval result is displayed for the interval depending on the specified aggregate type.

  For example, a process value was logged every 30 seconds. You have chosen an interval of 60 seconds and "Mean value" as the aggregate type. Now the mean of the two log values is formed and displayed in the table with the first time stamp of the period of calculation.

  If you select a aggregate type without interpolation and no value is available in the interval, no interval result is displayed. If you select a aggregate type with linear interpolation, an interval result is displayed for each interval.
- Statistics functions for process values

  All available process values are used for the specified time period, for example, to calculate and display the mean value.
- Trend process values

  The process values are displayed in trends.
- Trend (time step)

  Concise presentation of precompressed values in trends with aggregate functions, for example, as sums or averages.
- Bar chart (aggregates)
- Pie chart (aggregates)
- Alarm table

  Presentation of the accumulated alarms.
- Alarm hit list

  Presentation of statistical information about the alarms.
- Link to Web Center pages
- Links (external)

  Links to internal Web Center pages and external Internet sites, for example, stock market news.
- Display information

  For example, news reports
- Static process screens

  WinCC screens are integrated into the Web Center with no installation download. A screenshot of the process screen is created as a JPG on the DataMonitor server at regular intervals.
- Display graphic

  JPG images, e.g. company logos.
- The most recent reports

  Display the most recently generated reports. For example, the last ten print jobs generated with "Reports" in PDF format.

#### Basic procedure

1. [Set up a directory for a WebCenter page](#creating-directories-rt-professional)
2. [Assign access rights](#assigning-access-rights-rt-professional)
3. [Establish a connection to the WinCC data](#establish-a-connection-to-the-wincc-data-rt-professional)
4. [Publish screens for the WebCenter](#creating-static-process-screens-for-the-web-center-rt-professional)
5. [Create a layout template for WebCenter pages](#create-a-layout-template-for-webcenter-pages-rt-professional)
6. [Create a WebCenter page](#create-a-webcenter-page-rt-professional)
7. [Insert Web parts into the WebCenter page](#insert-web-parts-into-the-webcenter-page-rt-professional)
8. [Configure Web parts within WebCenter pages](#configure-web-parts-within-webcenter-pages-rt-professional)

---

**See also**

[Trends and Alarms (RT Professional)](#trends-and-alarms-rt-professional)

### Trends and Alarms (RT Professional)

#### Overview

"Trends &amp; Alarms" are used to display and analyze logged process values and messages in trends and tables and for evaluation with statistics functions.

Predefined Web pages contain the following:

- [Display of a process value in a table](#displaying-process-values-in-a-table-rt-professional).
- [Display of a maximum of three process values in a diagram.](#displaying-process-values-in-a-diagram-rt-professional).
- [Statistics functions for process values](#displaying-statistics-function-for-process-values-rt-professional).
- [Alarm hit list](#displaying-the-hit-list-of-messages-rt-professional).
- [Display of messages in a table](#displaying-messages-in-the-alarm-table-rt-professional).

The functions of "Trends &amp; Alarms" are configured with web parts. The same Web parts are used here as are used in the [WebCenter pages](#webcenter-rt-professional).

### Excel workbooks (RT Professional)

#### Overview

With "Excel Workbooks", it is possible to display process data such as alarms and values of process or logging tags in an Excel table on the DataMonitor client. Data of logging tags of swapped out logs is not displayed.

The data is analyzed using Excel functions or graphically formatted trend view, e.g. mean value calculation, diagram presentation.

You configure the Excel Workbook for displaying the process data using the Excel Add-In "Excel Workbook Wizard". The online display of the process data is performed via the Excel Add-In "Excel Workbook".

The created Excel workbooks can also be configured as templates for the function "Reports".

> **Note**
>
> You need the DataMonitor client to use the "Excel Workbooks" function. The installation file can be found on the DataMonitor start page under "Reports &gt; Download area", on the installation medium, or at the download installations.

> **Note**
>
> The following 32-bit and 64-bit versions of Microsoft Office are approved for "Excel Workbook":
>
> - MS Office 2019
> - MS Office 2021
> - Microsoft 365

#### Configuring with XML file or online

Simultaneous online access to process data of different WinCC servers is possible using the Excel worksheet. This requires that you either take the data from an XML file or from a local WinCC project during the configuration in the Excel Workbook Wizard.

#### Separation between process and analysis by configuring with XML file

By using the XML file for the project-relevant data, a separation between the process and the analysis is possible.

You create the XML file on a DataMonitor server. Afterwards, transfer the XML file to a PC with Microsoft Excel, located in operation management for instance. You can configure the process data display in the sheet on the PC.

Afterwards, transfer the workbook to a DataMonitor client where the process data is to be displayed online.

#### Configuration steps

The configuration of this function is carried out with the following steps:

1. In order to configure using the online data, configure directly on the WinCC server or on a WinCC client with an online connection to the respective WinCC server.
2. You have to create the XML file in order to configure with the data of an XML file. Use the "WinCC DataMonitor Configurator Export" application to create an XML file with the relevant data of the opened WinCC project on the DataMonitor server.
3. Use the Excel add-in "Excel Workbook Wizard" to import the project-relevant data to an Excel workbook.
4. Configure the display of process data such as alarms and tag values.
5. To display process data in the Excel workbook in online mode, use the Excel add-in "Excel Workbook" on a DataMonitor Client. The values can also be further processed in Excel.

> **Note**
>
> If you rename a table in an Excel workbook, the configuration data of the table will be lost.

### Reports (RT Professional)

#### Introduction

Using Reports , you can use WinCC print jobs and published Excel Workbooks to output analysis results and process data. The data is output in PDF or XLS file format

When the reports are created is defined on the DataMonitor Server. The following options are available:

- Manually, for example, by a plant operators.
- Event-driven, for example, when a tag value has changed-
- Time-driven, for example, daily.

You can also transmit a report as e-mail attachment The various directories can only be accessed with the appropriate authorization; including access over an Intranet or the Internet.

#### Requirement

**Output as PDF file (WinCC print jobs)**

- PDF Reader The PDF reader can be obtained from www.adobe.com, for example.

**Output as XLS file (Excel workbook)**

- MS Excel as of Office XP is installed.

  To use the DataMonitor Server for the automatic creation of Excel reports, you must install MS Excel on the server PC.
- The Excel workbook is created at and published as template at the DataMonitor Server.

  For more information, refer to "[Configuring an Excel workbook](#configuring-an-excel-workbook-rt-professional)".

  > **Note**
  >
  > **Displaying data on the DataMonitor Client**
  >
  > In the Excel worksheet, the creation time and periods are always displayed in the local time zone of the DataMonitor Server.

---

**See also**

[Configuring an Excel workbook (RT Professional)](#configuring-an-excel-workbook-rt-professional)

### Access rights (RT Professional)

#### Introduction

When using DataMonitor, different authentications are required. You have to define specific users and user rights for this.

- For the functions "Trends and Alarms", "Reports" and "Webcenter", a Windows user.
- For the functions "WinCCViewerRT" and "Excel Workbooks", a WinCC user.

SIMATIC logon allows the central administration of users. To use SIMATIC logon in conjunction with DataMonitor, the DataMonitor user is added to the user group "SIMATIC HMI VIEWER". The user group "SIMATIC HMI VIEWER" is created during the installation of WinCC Runtime Professional.

### Checking certificates (RT Professional)

#### Introduction

You must adjust settings in Internet Explorer before you work with the DataMonitor.

#### Procedure

1. Open the Internet Explorer.
2. Open the "Internet Options" dialog under:

   "Tools &gt; Internet Options"
3. Select the "Advanced" tab.
4. Deactivate the following option in the "Security" area:

   "Check for publisher's certificate revocation".

   ![Procedure](images/34604628491_DV_resource.Stream@PNG-en-US.png)

## Installing DataMonitor (RT Professional)

This section contains information on the following topics:

- [Licensing (RT Professional)](#licensing-rt-professional)
- [Installation of the DataMonitor server (RT Professional)](#installation-of-the-datamonitor-server-rt-professional)
- [Installation of the DataMonitor client (RT Professional)](#installation-of-the-datamonitor-client-rt-professional)

### Licensing (RT Professional)

#### DataMonitor client

DataMonitor client does not need a license.

#### DataMonitor server

Licenses must be installed on the DataMonitor server for the DataMonitor clients. The license check is different for the following function groups.

- "DataMonitor" with the functions:

  "WinCCViewerRT" and "Excel Workbooks"

  A "WinCC DataMonitor" license is required on the server computer for each DataMonitor client.
- "Webcenter" with functions:

  "Webcenter", "Trends and Alarms", "Reports"

  It is not the number of clients but the number of connections that is relevant for the license count with the "Webcenter" function group.

> **Note**
>
> **Licensing when upgrading to V14 or higher**
>
> If you upgrade from an older version to version V14 or higher, you need a new license for DataMonitor Server.

The following table shows the number of possible clients based on the function group and license.

| License | "DataMonitor" function group | "WebCenter" function group |
| --- | --- | --- |
| 1 Client | 1 | 3 |
| 3 Clients | 3 | 6 |
| 10 Clients | 10 | 20 |
| 25 Clients | 25 | 50 |
| 50 Clients | 50 | 100 |

#### Example

With a "3 Clients" license, the following users can log on simultaneously:

- 3 users of the "DataMonitor" function group
- 6 users of the "WebCenter" function group

#### Operation without valid license

If no license is available, DataMonitor displays a page requiring acknowledgement indicating the missing license at start-up.

- Click the "OK" button to acknowledge the notice.

  The start page of the DataMonitor is displayed.

Help:

- Check the existing licenses. If necessary, install the required licenses.

  > **Note**
  >
  > If the user does not log out with the "Logout" button and the browser is closed, the connection is maintained and the license remains occupied. The license will only be released again after approximately 20 minutes.

### Installation of the DataMonitor server (RT Professional)

This section contains information on the following topics:

- [Installing DataMonitor server (RT Professional)](#installing-datamonitor-server-rt-professional)
- [Installing the Internet Information Service (RT Professional)](#installing-the-internet-information-service-rt-professional)

#### Installing DataMonitor server (RT Professional)

##### Requirements

- Administrator rights
- Internet Information Service is installed.
- Installation disk with WinCC RT Professional

##### Procedure

Proceed as follows to install the DataMonitor server:

1. Place the installation disk in the drive.

   The disk starts automatically if auto-run is enabled in the operating system. If auto-run is not activated, start the Setup.exe program on the disk.
2. Select "User defined" for "Installation mode".
3. Select the "DataMonitor Server" program package.
4. Start the installation.

   You can track the status of the installation in the displayed dialog. Select "Cancel" to cancel the installation.
5. After installing the DataMonitor server, you can transfer the license key for the product. Click on "Transfer License Key" to do this. If you have already transferred the license key or you want to install it subsequently, select "Next".

   > **Note**
   >
   > License keys are not transferred automatically. Transfer the missing license keys during or after installation using Automation License Manager.
6. Reboot the PC when prompted by Setup.

##### Result

The DataMonitor server is installed.

#### Installing the Internet Information Service (RT Professional)

##### Settings

Before installing the DataMonitor server, you must install the Internet Information Service (IIS). During installation, you specify the settings for the DataMonitor server.

Activate the following settings:

- Web management tools:

  - IIS management service
  - IIS management console
  - IIS management scripts and tools
  - Compatibility with IIS Metabasis and IIS 6 configuration
  - Compatibility with WMI for IIS 6
- WWW services &gt; General HTTP features:

  - Standard document
  - Static content
- WWW services &gt; Application development features:

  - .NET extension capability 3.5 and 4.5
  - ASP
  - ASP.NET 3.5 and 4.5
  - ISAPI extensions
  - ISAPI filters
- WWW services &gt; Security:

  - Requirement filtering
  - Standard authentication
  - Windows authentication

    > **Note**
    >
    > If the logging functions are active with IIS, the log files must be monitored and deleted, if necessary. The event views should be configured in such a way that the log files do not become too large.

##### Requirements

- Windows user with administrator rights
- Write access for the registry database

##### Procedure

To install the IIS, follow these steps:

1. Insert the Windows installation disk into the drive.

Open the Control Panel. Click the "Programs and Features" entry.

1. Click the "Turn Windows features on or off" entry.
2. Activate the settings mentioned above.
3. Close the dialog with the "OK" button. The required data is transferred and the IIS is configured accordingly.

##### Alternative procedure

You can also use the command line "Start &gt; Run &gt; cmd" to install the IIS components located on the installation data carrier:

pkgmgr.exe /iu:IIS-WebServerRole;IIS-WebServer;IIS-CommonHttpFeatures;IIS-StaticContent;IIS-DefaultDocument;IIS-HttpErrors;IIS-ASPNET;IIS-NetFxExtensibility;IIS-ASP;IIS-ISAPIExtensions;IIS-ISAPIFilter;IIS-BasicAuthentication;IIS-WindowsAuthentication;IIS-ManagementConsole;IIS-ManagementService;IIS-IIS6ManagementCompatibility;IIS-Metabase;IIS-WMICompatibility;IIS-ManagementScriptingTools

### Installation of the DataMonitor client (RT Professional)

This section contains information on the following topics:

- [Installation of the DataMonitor client (RT Professional)](#installation-of-the-datamonitor-client-rt-professional-1)
- [Configuring security settings in Internet Explorer (RT Professional)](#configuring-security-settings-in-internet-explorer-rt-professional)
- [Installing with the installation disk (RT Professional)](#installing-with-the-installation-disk-rt-professional)
- [Installing via the Intranet/Internet (RT Professional)](#installing-via-the-intranetinternet-rt-professional)
- [User rights, user groups and optional installation possibilities (RT Professional)](#user-rights-user-groups-and-optional-installation-possibilities-rt-professional)

#### Installation of the DataMonitor client (RT Professional)

##### Installation Conditions DataMonitor Client

You need not install the DataMonitor client if you only want to use "Webcenter" and "Trends and Alarms".

You can install "Excel Workbook Wizard" on the client PC as an add-on. For "Excel Workbook", "Microsoft Office" is required for the installation on the client PC, as "Excel Workbook" and "Excel Workbook Wizard" are installed as Excel add-ins.

> **Note**
>
> **Installation of the DataMonitor client on the DataMonitor server**
>
> To also install DataMonitor client or WebNavigator client on a DataMonitor server, you need to proceed as follows:
>
> 1. Switch the start type of the service to manual in the service manager.
> 2. Reboot the PC.
> 3. Install the DataMonitor client.
>
>    During the installation, ensure that no WebNavigator clients or DataMonitor clients access the server.
> 4. When the installation is successfully completed, switch the start type of the "CCArchiveConnMon" service back to automatic.

##### Requirements

- Software and hardware requirements are met.
- Security settings in Internet Explorer are configured.

##### Installation options

The following options are available for installing the DataMonitor client.

- Installation via the installation disk

  In this case, certain Windows user rights are necessary, depending on the operating system.
- Installation via the Intranet/Internet

  In this case, certain Windows user rights are necessary, depending on the operating system.
- Additional installation options.

  The installation can also be performed without user interaction, under the Windows user rights of the current user or in networks using group policy-based software distribution.

#### Configuring security settings in Internet Explorer (RT Professional)

##### Requirement

Internet Explorer is open.

##### Procedure

To configure the security settings in Internet Explorer, follow these steps:

1. Select the command "Internet Options" from the "Tools" menu in Internet Explorer.
2. Select the "Security" tab. Select the corresponding zone, e.g. "Local Intranet" or "Internet".

   ![Procedure](images/2992457995_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/2992457995_DV_resource.Stream@PNG-en-US.png)
3. Click on the "Custom level" button. The "Security settings" dialog opens.

   ![Procedure](images/2992464267_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/2992464267_DV_resource.Stream@PNG-en-US.png)
4. Select the "Enable" option for "Script ActiveX controls marked safe for scripting" and "Download signed ActiveX controls".
5. Select the "Enable" option under "Scripting &gt; Active Scripting".
6. Click the "OK" button. Carry out the modifications in the subsequent dialog.
7. Select the "Trusted Sites" icon. Click the "Sites" button. The "Trusted sites" dialog opens.
8. Enter the address of the web server in the field "Add this web site to the zone". Possible formats and placeholders include "*://157.54.100 - 200", "ftp://157.54.23.41", or "http://*.microsoft.com". Deactivate the "Require server verification (https:) for all sites in this zone" check box. Click "Add". Confirm your entries with "OK".
9. Select the "Trusted Sites" icon. Click the "Standard level" button and then the "Custom Level" button. The "Security settings" dialog opens.
10. Select the "Enable" option for "Initialize and script ActiveX controls not marked as safe for scripting". Confirm your entries with "OK".
11. Click on the "General" tab. Click on the "Settings" button in the "Temporary internet files" area . Select the "Automatic" option for "Check for newer versions of stored pages". Confirm the entry using the "OK" button.
12. Click "OK" to close the "Internet Options" dialog.

##### Result

The security settings in Internet Explorer are configured.

#### Installing with the installation disk (RT Professional)

##### Requirements

- Security settings in Internet Explorer are configured.
- User possesses the necessary rights for installation.

##### Procedure

To install the DataMonitor client using the installation disk, follow these steps:

1. Place the installation disk in the drive.

   The disk starts automatically if auto-run is enabled in the operating system. If auto-run is not activated, start the Setup.exe program on the installation disk.
2. Select "User defined" in the "Installation mode" dialog.
3. Select the "DataMonitor Client" program package.
4. Start the installation.

   You can track the status of the installation in the displayed dialog. Select "Cancel" to cancel the installation.
5. Reboot the PC when prompted by Setup.

##### Result

DataMonitor client is installed. The "WinCCViewerRT" function is activated.

#### Installing via the Intranet/Internet (RT Professional)

##### Requirements

- Security settings in Internet Explorer are configured.
- User possesses the necessary rights for installation.
- DataMonitor server is installed and configured.
- User is created in user administration.
- The WinCC project is in Runtime on the DataMonitor server.
- The server PC and client PC are interconnected via a TCP/IP-capable network.

##### Procedure

To install the DataMonitor client via the Intranet/Internet, follow these steps:

1. Enter the address of the DataMonitor server in the address bar.

   - Standard website: "http://www.server_name.de"
   - Web site in the virtual directory: "http://www.server_name.de/DataMonitor"
2. Log in with your user name and password on the DataMonitor server. If you are accessing the DataMonitor server for the first time, you will be prompted to install the DataMonitor client.
3. Click the "Click here to install" link.
4. Click the "Save" button in the "File Download" dialog to store the client setup on the client PC. It is recommended that you save the setup file. Then if the client PC needs to be restarted, it is not necessary to download the setup again.
5. Leave the Internet Explorer open and open Windows Explorer. Navigate to the directory in which you saved the setup file. Double-click the setup file.
6. Follow the instructions on the screen and enter the information and settings necessary. The client-end controls of the DataMonitor are installed. Close the Setup dialog.

##### Result

After the successful completion of the installation, the DataMonitor client switches to the WinCC project currently in Runtime.

> **Note**
>
> If you have already installed the DataMonitor client and wish to install a current version of the client via the Intranet/Internet, open the Client Setup straight away without saving the installation file on the target PC. If you want to save the new installation file, uninstall the old installation file first or save the new file version to a different directory than the older version of the file. (necessary)

> **Note**
>
> When downloading the DataMonitor server client software, select the "Save" option to save the client setup on the client PC. It is recommended to save the Setup file because, in the event of a restart of the client computer being necessary, the Setup need not be downloaded again.
>
> If the DataMonitor client was installed previously from the DVD and you want to install an updated version of the client via the Intranet/Internet, the client setup must also be saved on the target PC.

#### User rights, user groups and optional installation possibilities (RT Professional)

##### User rights, user groups and optional installation possibilities

The following conditions apply for the installation of the DataMonitor client:

- Windows user rights required for installation and first registration of the DataMonitor client
- Installation of the DataMonitor client with restricted windows user rights
- Installation for a configured group of users or PCs
- Group policy based software distribution
- Installation without user interaction

##### Windows user rights required for installation and first registration of the DataMonitor client

To install the DataMonitor client via Intranet/Internet or from the installation disk, you require certain minimum user rights.

| Operating system | Required minimum user rights |
| --- | --- |
| Windows Server 2019 / Windows Server 2022 | "Power user" |
| Windows 10 / Windows 11 | "Power user" |

Use the following for the first logon of the DataMonitor client to the DataMonitor server:

- The user identification of the installation
- A user with equal or higher Windows user rights

  If the first logon was successful, subsequent logons can be performed for a user without "Power user" or "Administrator" rights.

##### Installation of the DataMonitor client without "Power user" or "Administrator" rights

By using Microsoft Windows Installer technology (MSI), DataMonitor clients can also be installed with limited Windows user rights i.e. without possessing the "Power user" or "Administrator" rights. The add-ons and plug-ins for the DataMonitor client can also be installed this way.

This procedure can be used for the following installations:

- Installation via group policy-based software distribution in networks
- Installation for a configured group of users or PCs.

##### Installation for a configured group of users or PCs

Using the Microsoft Systems Management server or group policy on a domain controller, it is possible to install a group of users or PCs configured by the administrator.

- The MSI file "WinCCDataMonitorClient.msi" is published on the domain controller and enabled for a user group. The installation is then performed according to the configuration of the group policy based software distribution either during logon of the defined users or when the computer is started.
- When using a Microsoft Systems Management Server, the installation is configured and triggered by the administrator, and executed when the relevant PC boots. More information on Microsoft Systems Management server is available on the Microsoft home page.

##### Group policy based software distribution

The software installation is normally executed with the access rights of the current Windows user. When using MSI technology, the installation is performed by an operating system service with higher rights. This enables installations to be performed for which the Windows user has no permission. Applications which require higher-level permissions for installation are referred to as "privileged installations" in MSI technology. Installation of these applications is possible when a Windows user is assigned the "Always install with elevated privileges" permission.

To use group policy-based software distribution, a group policy is created on the domain controller. The software to be distributed is assigned or published using the active directory .

- Assignment: The software distribution can be assigned to a user or a PC. The software to be distributed is automatically installed when the user logs on or the PC boots.
- Publication: The software distribution can be published for single users. When the user logs onto the client PC, the software to be distributed appears in a dialog and can be selected for installation.

##### Installation without user interaction

During installation of the DataMonitor client, the user is normally prompted to enter information, e.g. the target directories, the agreement to the software license conditions or components to be installed.

By implementing a configuration file, installation is possible without user interaction. The required path specification and user information are provided in the "options.ini" configuration file. The INI file must be located in the same directory as the setup file of the DataMonitor client.   
This installation procedure is advantageous when using the group policy-based software distribution.

Installation from the product DVD occurs with user interaction.

The settings given predefined in the table are used under the following conditions:

- The "options.ini" configuration file is missing and there is no corresponding entry available in the registry of the client PC, e.g. due to another SIMATIC HMI product installed.
- Alternatively, the installation is performed via the group policy-based software distribution with assignment to the PC.

| Information | Parameter |
| --- | --- |
| Target directory for the DataMonitor client | INSTALLDIR=" &lt;syspath1&gt;\Siemens\WinCC" |
| Target directory for common components | COMMONDIR=" &lt;syspath2&gt;\Siemens " |
| User information / user name | USER |
| User information / organization | COMPANYNAME |

The "&lt;syspath?&gt;" parameters result from the settings in the registry under the key "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion":

- "&lt;syspath1&gt;" corresponds to the key "ProgramFilesDir" e.g. "C:\\Program Files"

- "&lt;syspath2&gt;" corresponds to the key "CommonFilesDir", e.g. "C:\\Program Files\\Common Files"

##### Example of an "options.ini" configuration file

`[USERINFO]`

`USER=Integration`

`COMPANYNAME=Siemens AG`

`[INSTALLPATH]`

`COMMONDIR=" C:\Programs\Common files\Siemens "`

`INSTALLDIR=" C:\Programs\Siemens\WinCC "`

`[FEATURES]`

`FUNCTIONTRENDCONTROL=0`

`HARDCOPY=0`

`WINCCUSERARCHIVES=0`

`DEU=0`

`FRA=0`

`ITA=0`

`ESP=0`

## Configuring the DataMonitor system (RT Professional)

This section contains information on the following topics:

- [Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)
- [Configuring a WinCC project (RT Professional)](#configuring-a-wincc-project-rt-professional)
- [Transferring a WinCC project (RT Professional)](#transferring-a-wincc-project-rt-professional)
- [Configuring the DataMonitor Server (RT Professional)](#configuring-the-datamonitor-server-rt-professional)
- [Starting the DataMonitor on the DataMonitor client (RT Professional)](#starting-the-datamonitor-on-the-datamonitor-client-rt-professional)

### Overview of configuration steps (RT Professional)

#### Introduction

For the use of the WinCC DataMonitor, the data and process screens are made available on the DataMonitor Server to be accessed and displayed on the DataMonitor client.

#### Requirement

- The server PC and client PC are interconnected.
- On the server PC

  - Internet Information Service is installed.
  - The DataMonitor Server is installed.
  - A license key is installed.
  - WinCC Runtime Professional is installed.
- On the client PC

  - Internet Explorer V11 is installed.

#### Configuration steps

The following configuration steps are required to set up a DataMonitor system.

1. Configure the WinCC project.

   - Configuring WinCC screens for Web access
   - For WinCCViewerRT and the "Excel Workbooks" function, define the users and access rights in the "User administration" dialog.
   - Configure Runtime settings
2. Transfer your WinCC project to the server PC. If the configuration PC and the WebNavigator server are interconnected, transfer the WinCC project using the command "Download to device &gt; Software (all)".
3. Configure the DataMonitor Server.

   - Setting up the Web folder
   - Define users and access rights in Windows for the functions "Trend and Alarms", "Reports" and "WebCenter".
4. Start WinCC Runtime on the server PC.
5. Use the DataMonitor functions on the DataMonitor Client.

   - Check the Internet Explorer security settings on the client PC
   - Start Internet Explorer on the client PC and enter the address of the DataMonitor Server.
   - After logging on to the DataMonitor Server you can access the DataMonitor functions.
6. Monitor the WinCC project at the DataMonitor Client.

   - Setting up WinCCViewerRT
   - Displaying screens

### Configuring a WinCC project (RT Professional)

This section contains information on the following topics:

- [Configuring WinCC screens for Web access (RT Professional)](#configuring-wincc-screens-for-web-access-rt-professional)
- [WinCC screens as a gadget (RT Professional)](#wincc-screens-as-a-gadget-rt-professional)
- [Configuring runtime settings (DataMonitor) (RT Professional)](#configuring-runtime-settings-datamonitor-rt-professional)
- [Defining users in WinCC (RT Professional)](#defining-users-in-wincc-rt-professional)

#### Configuring WinCC screens for Web access (RT Professional)

##### Configuring individual WinCC screens for Web access

1. Double-click the desired screen in the project tree. The screen is opened and the screen properties are shown in the Inspector window.
2. In the Inspector window, click "Properties &gt; Properties &gt; Web access".
3. Activate "Web access".

or

1. select the desired screen in the project tree.
2. Select "Web access" command in the shortcut menu.

##### Configuring several screens for Web access

1. Select "Screens" in the project tree.
2. Select "Web access all" command in the shortcut menu.

##### Result

The WinCC screens are configured for Web access. During the transfer of the project, the WinCC screens are adapted for access via the Intranet/Internet and published on the DataMonitor Server.

For more information, refer to "Transferring when WinCC projects".

---

**See also**

[Creating static process screens for the Web Center (RT Professional)](#creating-static-process-screens-for-the-web-center-rt-professional)

#### WinCC screens as a gadget (RT Professional)

This section contains information on the following topics:

- [Gadget on the Data Monitor Server (RT Professional)](#gadget-on-the-data-monitor-server-rt-professional)
- [Gadget on the Data Monitor Client (RT Professional)](#gadget-on-the-data-monitor-client-rt-professional)

##### Gadget on the Data Monitor Server (RT Professional)

###### Introduction

Using the "Preview" property, you define which screens to group in a gadget. Gadgets are mini applications for the Windows sidebar. In order to use gadgets, a DataMonitor client must always be installed as well on the DataMonitor server.

The following operating systems support gadgets:

- Windows 10
- Windows 11
- Windows Server 2019
- Windows Server 2022

###### Procedure

To configure WinCC screens as a gadget, proceed as follows:

1. Double-click the desired screen in the project tree. The screen is opened and the screen properties are shown in the Inspector window.
2. In the Inspector window, click "Properties &gt; Properties &gt; Web access".
3. Activate "Preview" and "Web access".
4. Save the WinCC project.
5. Select the "Compile &gt; Software" command in the shortcut menu of the HMI device.

###### Result

The screens are assembled for the gadget on the WebNavigator server. As soon as the project is in runtime, the WebNavigator server generates a jpg snapshot image "pdlImage.jpg" of each screen at cyclic intervals and in consecutive order.

The file is stored in the directory "\WinCC\Webnavigator\Server\Web\image\_gadget". The gadget accesses this file cyclically in the directory again.

Note that user interactions are not possible in the screens displayed. This includes, for example, calls from login dialogs or notice dialogs via functions.

The following objects are not supported for the display in a gadget:

- GSC diagnostics window
- Media Player

  > **Note**
  >
  > The WinCC project shown in the gadget cannot be operated.

##### Gadget on the Data Monitor Client (RT Professional)

###### Introduction

In order to use gadgets, a DataMonitor client must always be installed as well on the DataMonitor server. A preconfigured gadget for displaying WinCC screens is located on the DataMonitor client in the installation directory under ""\WinCC\Webnavigator\GADGET".

The following operating systems support gadgets:

- Windows 10
- Windows 11
- Windows Server 2019
- Windows Server 2022

###### Requirement

The screens are published on the Data Monitor server and configured as "Preview".

###### Procedure

To access the gadget with the Data Monitor Client, follow these steps:

1. Double-click on the "_WebNavigator.gadget" gadget in the installation directory under "\WinCC\Webnavigator\GADGET". The Gadget is installed under Windows in the Sidebar.
2. Define the update cycle in which the gadget loads a screen from the Data Monitor Server, every 17 seconds for example.
3. Enter the address of the Data Monitor Server. The gadget establishes a connection to the Data Monitor Server.
4. If necessary, drag-and-drop the gadget onto the desktop.

#### Configuring runtime settings (DataMonitor) (RT Professional)

##### Introduction

You can configure the behavior in runtime in the "Runtime settings" editor.

##### Procedure

1. Open the "Runtime Settings &gt; Web Navigator" editor.

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

[Display screens (RT Professional)](#display-screens-rt-professional)

#### Defining users in WinCC (RT Professional)

This section contains information on the following topics:

- [Managing a user group for DataMonitor (RT Professional)](#managing-a-user-group-for-datamonitor-rt-professional)
- [Managing users for DataMonitor (RT Professional)](#managing-users-for-datamonitor-rt-professional)

##### Managing a user group for DataMonitor (RT Professional)

###### Introduction

A different start screen and the language can be set for each user group. This allows you to make various sections of a project immediately accessible or inaccessible for users.

> **Note**
>
> The name of the user group has to be unique within the project. Otherwise the input is not accepted.

###### Requirements

- The "User groups" work area is open.
- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.

###### Procedure

1. Position the mouse cursor on the title of the "Groups" table.
2. Open the shortcut menu with the right mouse button and select the display of the "Start screen" and "Language" columns.
3. Double-click "Add..." in the "Groups" table.
4. Enter "DataMonitor operators" as the name of the user group. Activate at least the "DataMonitor - View only" authorization in the "Authorizations" table.
5. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Start screen" column. A dialog box for selecting the start screen opens.
6. Select a start screen for Runtime.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Language" column. A dialog box for selecting the language opens.
9. Select the language.

As an alternative, select the user group in the work area; the properties of the user group are then displayed in the Inspector window. In the Inspector window, select "Properties &gt; Properties &gt; Web options". Select the start screen and the language.

> **Note**
>
> The name of the user group is language-dependent. You can specify the name in several languages and switch between languages in runtime.

##### Managing users for DataMonitor (RT Professional)

###### Introduction

Create a corresponding user in user administration to enable the use of the "WinCCViewerRT" and "Excel Workbooks" functions.

###### Requirements

- DataMonitor is installed.
- The "Users" work area is open.
- The "DM_Demo" user is created and assigned view-only rights.
- The "DataMonitor operators" user group has been created.
- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.

###### Setting the start screen and language

1. Position the mouse cursor on the title of the "Users" table.
2. Open the shortcut menu with the right mouse button and select the display of the "Start screen" and "Language" columns.
3. In the "Start screen" column, click on the ![Setting the start screen and language](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the row of the "DM_Demo" user. A dialog box for selecting the start screen opens.
4. Select the "Start" screen.
5. Close the dialog box by using the ![Setting the start screen and language](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
6. Click the ![Setting the start screen and language](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Language" column. A dialog box for selecting the language opens.
7. Select "Spanish" as the Runtime language.
8. Activate the "DataMonitor operators" user group in the "Groups" table.

As an alternative, select the user in the work area; the properties of the user are then displayed in the Inspector window. In the Inspector window, select "Properties &gt; Properties &gt; Web options". Select the start screen and the language.

> **Note**
>
> The language setting is retained when a user is moved from one group to another. The start screen will be overwritten.

### Transferring a WinCC project (RT Professional)

#### Requirement

- A WinCC project is configured
- DataMonitor Server is installed on the server PC.
- The configuration PC and server PC are interconnected.

#### Online transfer

Transfer the WinCC project using the command "Load to device &gt; Software (all)". The project is compiled prior to the download. The screens are adapted for access via Intranet/Internet during compilation.

During the download to the server PC, the configured WinCC project is transferred and the screens are published on the DataMonitor Server. For more information, refer to "Compiling and loading".

### Configuring the DataMonitor Server (RT Professional)

This section contains information on the following topics:

- [Setting up the DataMonitor Web page (RT Professional)](#setting-up-the-datamonitor-web-page-rt-professional)
- [Setting up a firewall (RT Professional)](#setting-up-a-firewall-rt-professional)
- [Defining users in Windows (RT Professional)](#defining-users-in-windows-rt-professional)

#### Setting up the DataMonitor Web page (RT Professional)

##### Requirement

- Internet Information Service is installed.
- The WinCC DataMonitor is installed.

##### Procedure

Set up the DataMonitor Web page as follows:

1. In the Start menu select the command "Start &gt; All Programs &gt; Siemens Automation &gt; Option and Tools &gt; HMI Tools" &gt; WinCC Web Configurator". This starts the Web Configurator.
2. The Web Configurator detects whether a configuration already exists.

   - No configuration available: Select "Create a new standard website (stand-alone)" and click "Next".
   - A configuration exists: Check the configuration
3. Define the desired settings.

   ![Procedure](images/23240596875_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23240596875_DV_resource.Stream@PNG-en-US.png)
4. Enter the name of your Web site in the "Name of the Web site" field.
5. In the "Port" field, enter the port number used for access.
6. In the "IP address" field specify whether the PC is to be reached in the Intranet, Internet or in both networks. Only use addresses from the selection list.

   If you want to make your PC accessible via the Intranet and the Internet, select "All not assigned".
7. Select "DataMonitor.asp" as the standard Web site.
8. Define the time interval after which the Web Navigator Clients automatically start to establish a connection following a connection breakdown. If "0 s" is set, the "Automatic connection establishment" function is disabled.
9. Define the way the Web site is started after configuration.
10. If you have not activated a firewall, click "Finish". If you have installed a firewall, click "Next".

##### Result

The Web directory has been created and the Web page is activated. If you have activated the firewall, configure the firewall settings with the Web Configurator. See "Setting up a firewall" for additional information.

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

#### Defining users in Windows (RT Professional)

This section contains information on the following topics:

- [User groups (RT Professional)](#user-groups-rt-professional)
- [Defining Users and Access Rights in Windows (RT Professional)](#defining-users-and-access-rights-in-windows-rt-professional)

##### User groups (RT Professional)

###### User groups in Windows

The following user groups are created automatically in Windows when the DataMonitor server is installed:

**"**
**SIMATIC Report Administrators**
**"**

The membership in the user group "SIMATIC Report Administrators" is required for extended rights, especially for configuration purposes. You must create at least one user and assign the user group "SIMATIC Report Administrators".

- The following is possible in the "Webcenter" function:

  - Configuration of connections
  - Creation of templates for WebCenter pages
  - Creation and configuration of public and private WebCenter pages
- The following is possible in the "Reports" function:

  - Configuration of reports on the basis of print jobs or Excel workbooks.

**"**
**SIMATIC Report Users**
**"**

The membership in the user group "SIMATIC Report Users" or in your own user group is required for the functions "Webcenter", "Trends and Alarms" and "Reports".

- The following is possible in the "Webcenter" function:

  - Setting and configuration of WebCenter pages. WebCenter pages are stored in different directories.
  - Opening public pages
- The following is possible in the "Reports" function:

  - Opening reports on the basis of print jobs or Excel workbooks.

##### Defining Users and Access Rights in Windows (RT Professional)

###### Requirement

- WinCC Runtime Professional is installed
- DataMonitor Server is installed

###### Procedure

Proceed as follows to create a user under Windows:

1. Open the Control Panel. Double-click the "Administration" entry.
2. Double-click "Computer Management" in the "Administration" dialog.

   The "Computer Management" dialog opens.
3. Navigate to the directory "System &gt; Local Users and Groups / Groups". Select the "New User..." command in the shortcut menu.
4. Enter the name "DM_Demo" in the "User Name" field in the "New User" dialog. Enter the description "User for DataMonitor" in the "Complete Name" field. Type the desired password into the "Password" field and then repeat it in the "Repeat password" field. Create the user with "Create". Close the "New user" dialog.
5. In the right part of the table window, click the newly created user. Open the shortcut menu and select the command "Properties". Go to the "Member of" tab. Click "Add".
6. Click the "Advanced &gt;" button in the dialog "Select Groups" and then "Find now".
7. In the dialog below, select the two entries "SIMATIC Report Administrators" and "SIMATIC HMI VIEWER" from the list. To close the dialog, click "OK" twice.
8. The groups "SIMATIC Report Administrators" and "SIMATIC HMI VIEWER" are added to the membership list in the user properties. Click "OK."
9. Close the dialog "Computer Management" with the menu command "File &gt; Exit".
10. Close the dialog "Management" with the menu command "File &gt; Close".

###### Result

The user "DM_Demo" with membership of the user groups "SIMATIC Report Administrators" and "SIMATIC HMI VIEWER" has been set up.

### Starting the DataMonitor on the DataMonitor client  (RT Professional)

This section contains information on the following topics:

- [Configuring security settings in Internet Explorer (RT Professional)](#configuring-security-settings-in-internet-explorer-rt-professional-1)
- [Starting the DataMonitor startup page on the DataMonitor client (RT Professional)](#starting-the-datamonitor-startup-page-on-the-datamonitor-client-rt-professional)
- [General Operations of the DataMonitor Client (RT Professional)](#general-operations-of-the-datamonitor-client-rt-professional)

#### Configuring security settings in Internet Explorer (RT Professional)

##### Introduction

To have the full functionality available on the DataMonitor client, adapt the security settings in Internet Explorer.

- Internet Explorer V11

##### Procedure

To configure the security settings in Internet Explorer, proceed as follows:

1. Click "Tools" &gt; "Internet Options" in the Internet Explorer. The "Internet Options" dialog opens.
2. Click the "Security" tab.
3. Select the "Trusted Sites" icon and click the "Sites..." button. The "Trusted Sites" dialog opens.
4. Enter the address of the DataMonitor Server in the "Add this Website to the zone" field.

   Possible formats and wildcards include "*://157.54.100 - 200", "ftp://157.54.23.41", or "http://*.microsoft.com".
5. If necessary, clear the "Require server verification for all sites in this zone (https:)". Click "Add". Confirm the entry by clicking "OK".
6. Select the "Trusted Sites" icon.
7. Click "Default Level". Click "Customize Level" in the following dialog.

   The "Security settings" dialog box opens.

   - Activate the "Activate" option under "Initialize and script ActiveX controls not marked as safe".
   - Confirm the entry by clicking "OK".
8. Close the "Internet Options" dialog by clicking "OK".

##### Result

The necessary settings of the DataMonitor client in the Internet Explorer are configured.

#### Starting the DataMonitor startup page on the DataMonitor client (RT Professional)

##### Introduction

The start page of the DataMonitor summarizes the functions of the DataMonitor.

- "[Working with reports](#working-with-reports-rt-professional)":

  Creation and output of the analysis results and process data in print jobs and in published [Working with Excel Workbooks](#working-with-excel-workbooks-rt-professional).
- "[Working with the WebCenter](#working-with-the-webcenter-rt-professional)"

  Configuration of connections and creation of WebCenter pages for the display of logged data.
- "[Working with Trends and Alarms](#working-with-trends-and-alarms-rt-professional) "

  Display of alarms and process values from logs in tables and diagrams.

You start the DataMonitor client on a standalone PC or on a DataMonitor server.

##### Requirements

- User has been created in the Windows user group "SIMATIC Report Administrators".
- The WinCC project on the DataMonitor Server is in Runtime.
- A user is created in WinCC.

##### Procedure

To access the Web page of the DataMonitor Server, proceed as follows:

1. Open the MS Internet Explorer on the DataMonitor client.
2. Enter the name of the DataMonitor server in the format "http://&lt;servername&gt;" in the URL. Confirm the entry with "Enter".
3. The logon dialog opens. Enter the name of a Windows user in the "User name" field. Enter the respective password and confirm with "OK".

   The start page with the DataMonitor functions will be displayed.

   ![Procedure](images/60943065355_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/60943065355_DV_resource.Stream@PNG-en-US.png)

##### Result

The start page with the DataMonitor functions will be displayed on the DataMonitor client. The use of the functions depends on the user's access right.

---

**See also**

[Working with WinCCViewerRT (RT Professional)](#working-with-winccviewerrt-rt-professional)

#### General Operations of the DataMonitor Client (RT Professional)

##### Introduction

The DataMonitor Web pages have the following structure:

![Introduction](images/23125780363_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Header |
| ② | Current user |
| ③ | Link to logoff |
| ④ | Navigation control |
| ⑤ | Icon to hide the header |
| ⑥ | Interface language selection field |
| ⑦ | Tabs depending on the currently displayed contents |
| ⑧ | Contents |

##### Switching the user interface language

1. Choose the desired language from the selection field in the header.

   The GUI language is changed.

##### Hide and show the header

1. To hide the header line, click the symbol ![Hide and show the header](images/10223386891_DV_resource.Stream@PNG-de-DE.png).

   This provides more room for displaying the content.
2. To show the header line again, click the symbol ![Hide and show the header](images/10223395083_DV_resource.Stream@PNG-de-DE.png).

##### Logoff

1. To log off from the DataMonitor server, click the "Log off" link.
2. Close Internet Explorer.

   When you close Internet Explorer, the used license will be released immediately.

## Working with WinCCViewerRT (RT Professional)

This section contains information on the following topics:

- [Setting up WinCCViewerRT (RT Professional)](#setting-up-winccviewerrt-rt-professional)
- [Display screens (RT Professional)](#display-screens-rt-professional)

### Setting up WinCCViewerRT (RT Professional)

#### Requirement

- On the server PC

  - The DataMonitor Server is installed.
  - A license key is installed.
  - The WinCC project is in Runtime.
  - The WinCC screens are configured for Web access and published.
- On the client PC

  - DataMonitor Client is installed.

#### Procedure

Set up WinCCViewerRT as follows:

1. In the Start menu, select "Start &gt; All Programs &gt; Siemens Automation &gt; Option and Tools &gt; HMI Tools" &gt; WinCCViewerRT".
2. Enter the logon data in the "General" tab:

   ![Procedure](images/25756275595_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25756275595_DV_resource.Stream@PNG-en-US.png)

   - Server address: http://&lt;server name&gt;, or http://&lt;IP address&gt;
   - User name and password:
3. In the "Parameters" tab, specify the Runtime language and whether to disable keystrokes that the operator uses to change to other programs.
4. Define the WinCC Runtime Professional properties in the "Graphics Runtime" tab:

   - Start screen
   - Configuration file for screen navigation
   - Window attributes
   - Illegal user actions
5. Define additional user actions in the "Runtime" tab.

   - Automatic logout
   - Enable screen keyboard.
   - Use &lt;Ctrl+Alt+Del&gt; to switch to the Task Manager and to the operating system. This setting is only valid for the on-screen keyboard.
   - Open the "WinCCRTViewer" dialog by means of keystroke.

     You can change the default keystroke &lt;Ctrl+Alt+P&gt;.
6. Close the dialog with "OK".

#### Result

The WinCCViewerRT is configured. When the dialog is closed, the connection to the DataMonitor server is established. The settings are saved to the configuration file "WinCCViewerRT.xml". The settings in the configuration file are used at the next start of WinCCViewerRT.

The configuration file is stored in the directory "C:\Users\&lt;User name&gt;\Appdata\LocalLow\Siemens\SIMATIC.WinCC\WebNavigator\Client". Under &lt;User name&gt;, enter the name of the user logged-on when the file is created. This allows different configurations to be used, depending on the logged on user. WinCCViewerRT applies the interface language from WinCC.

**Renaming or removing WinCCViewerRT.xml**

When you rename or remove the file WinCCViewerRT.xml, the configuration dialog of WinCCViewerRT is opened during the start. Reconfigure WinCCViewerRT, or select a different configuration file.

### Display screens (RT Professional)

#### Requirements

- A license key is installed on the DataMonitor Server.
- The WinCC project on the DataMonitor Server is in Runtime.
- The WinCC screens are configured for Web access and published.
- A WinCC user with the authorization no. 1002 "Web access - view only" is created.

> **Note**
>
> The "Channel diagnostics view" object is not supported by the WinCC DataMonitor option.

#### Procedure

To view screens, proceed as follows:

1. In the Start menu, select "Start &gt; All Programs &gt; Siemens Automation &gt; Option and Tools &gt; HMI Tools &gt; WinCCViewerRT".
2. Log on to the WebNavigator server:

   - If the user and password are configured in the "WinCCViewerRT" dialog, no logon dialog displayed.
   - If no user and password was configured in the "WinCCViewerRT" dialog, the logon dialog displayed. Enter the user name and password of the WinCC user. Click "OK".
3. Press the &lt;Ctrl+Alt+P&gt; keystroke to change the user. The "WinCCViewerRT" dialog opens.

   Enter the user name and password in the "General" tab.

   You can also select the xml file that contains this data.

#### Result

The Web Viewer connects to the activated WinCC project. The screens of the WinCC project are displayed.

The cursor is a "View only cursor" and indicates that process-related operations are not allowed.

![Result](images/24565485195_DV_resource.Stream@PNG-de-DE.png)

Certain operations are still possible, such as opening the properties dialog of an online trend control.

If necessary, you can use your own cursor symbol as a "View only cursor". You can find more detailed information on this under "[Configuring runtime settings (DataMonitor)](#configuring-runtime-settings-datamonitor-rt-professional)".

---

**See also**

[Configuring runtime settings (DataMonitor) (RT Professional)](#configuring-runtime-settings-datamonitor-rt-professional)

## Working with the WebCenter (RT Professional)

This section contains information on the following topics:

- [Administration (RT Professional)](#administration-rt-professional)
- [Creating static process screens for the Web Center (RT Professional)](#creating-static-process-screens-for-the-web-center-rt-professional)
- [Create a layout template for WebCenter pages (RT Professional)](#create-a-layout-template-for-webcenter-pages-rt-professional)
- [Create a WebCenter page (RT Professional)](#create-a-webcenter-page-rt-professional)
- [Insert Web parts into the WebCenter page (RT Professional)](#insert-web-parts-into-the-webcenter-page-rt-professional)
- [Configure Web parts within WebCenter pages (RT Professional)](#configure-web-parts-within-webcenter-pages-rt-professional)
- [Deleting WebCenter Pages and Layout Templates (RT Professional)](#deleting-webcenter-pages-and-layout-templates-rt-professional)
- [Exporting and importing WebCenter pages (RT Professional)](#exporting-and-importing-webcenter-pages-rt-professional)

### Administration (RT Professional)

This section contains information on the following topics:

- [User Groups and Directories (RT Professional)](#user-groups-and-directories-rt-professional)
- [Creating Directories (RT Professional)](#creating-directories-rt-professional)
- [Assigning Access Rights (RT Professional)](#assigning-access-rights-rt-professional)
- [Establish a connection to the winCC data (RT Professional)](#establish-a-connection-to-the-wincc-data-rt-professional)

#### User Groups and Directories (RT Professional)

##### Overview

WebCenter pages and reports are stored in directories on the DataMonitor Server.

Its standard complement of directories is as follows:

- "Public"
- "Private"

  Every user has a "Private" directory. Only the respective user has access rights to this directory.

You can find additional information on setting up directories in the section "[Creating Directories](#creating-directories-rt-professional)".

##### Windows User Groups

The user groups "SIMATIC Report Administrators" and "SIMATIC Report Users" are created during the installation of the DataMonitor Server. You can create more user groups. You can find additional information on setting up user groups and users in the section"[Assigning Access Rights](#assigning-access-rights-rt-professional)".

To access the DataMonitor, you can assign all members of a user group with the same access rights to the directory of the DataMonitor server.

The following access authorization is possible:

- Read
- "Change"
- "Create"

A user, as a member of a user group, only has access to a directory if the respective user group has access rights to that directory. This permits user group-specific access. You can find additional information on assigning access rights in the section "[Defining users in Windows](#defining-users-in-windows-rt-professional).

The following screen shows the basic user administration for the WebCenter.

![Windows User Groups](images/41326771979_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating Directories (RT Professional)](#creating-directories-rt-professional)
  
[Assigning Access Rights (RT Professional)](#assigning-access-rights-rt-professional)
  
[Defining users in Windows (RT Professional)](#defining-users-in-windows-rt-professional)

#### Creating Directories (RT Professional)

##### Introduction

You store WebCenter pages in directories. The following directories exist as defaults:

- "Public"
- "Private"

  Every Windows user has their own "Private" directory.

##### Requirement

- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".
- The DataMonitor start page is open.

##### Procedure

1. Click in the start page "Webcenter &gt; Administration".
2. Click the "Directory administration" tab.

   ![Procedure](images/23154831243_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23154831243_DV_resource.Stream@PNG-en-US.png)
3. Enter the name "mypart" in the "New directory" field.
4. Click the "Create" button.

##### Result

You have created the directory "mypart". The user administration is opened automatically. Specify the access rights for the folder. You can also exit the page and configure the access rights at a later time.

#### Assigning Access Rights (RT Professional)

##### Introduction

In the WebCenter, directories are created in which, for example, the WebCenter pages are stored. You can assign different access rights for the individual directories to Windows user groups.

The following access authorization is possible:

- Read
- "Change"
- "Create"

##### Requirement

- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".

##### Procedure

1. Click in the start page "Webcenter &gt; Administration".
2. Click the "User administration" tab.

   ![Procedure](images/60953194379_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/60953194379_DV_resource.Stream@PNG-en-US.png)
3. Select the desired directory from the "Current Directory".

   All existing Windows user groups are listed.
4. Activate the access rights in the line of the desired Windows user group.
5. Click "Save".

##### Result

The access rights have been configured for the desired directory.

#### Establish a connection to the winCC data (RT Professional)

This section contains information on the following topics:

- [Create connection and set up language (RT Professional)](#create-connection-and-set-up-language-rt-professional)
- [Connecting and Disconnecting Swapped Logs (RT Professional)](#connecting-and-disconnecting-swapped-logs-rt-professional)

##### Create connection and set up language (RT Professional)

###### Introduction

A connection is configured for access to the data in the "Webcenter". A connection is set up for each data source, e.g. WinCC server. The connection is required for example for the function "Trends and Alarms" and the WebCenter page.

###### Requirement

The logged on user is a member of the Windows user group "SIMATIC Report Administrators".

###### Procedure

1. Click in the start page "Webcenter &gt; Administration".
2. Click the "Connection administration" tab.

   ![Procedure](images/23145031179_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23145031179_DV_resource.Stream@PNG-en-US.png)
3. Choose the language that corresponds with the linguistic region of the server or log to be linked in "Linguistic region".

   If you do not select the language that corresponds with the respective linguistic region, characters may be displayed incorrectly on the page.
4. Select "New connection".

   After the new installation, no selection is possible in the "Connection" field, as no connections have been configured yet.
5. Enter a name in the field "Connection name", e.g. "WinCC1_ Runtime".

   Any name can be selected. However, it should contain a reference to the selected connection type. Do not use spaces and special characters in the connection name.
6. Enter the name of the PC whose data you would like to access in the "Computer name" field. As an alternative, select the name of the PC using the "Find" button.
7. Enter the desired database in the "Database" field. Alternatively, select the database using the "Find" button.
8. Choose the desired option in the "Connection type" area.

   - "Swapped WinCC Log"

     Further steps are required to access data from logs. You can find more detailed information on this under "[Connecting and Disconnecting Swapped Logs](#connecting-and-disconnecting-swapped-logs-rt-professional)"
   - "WinCC Runtime"

     The Runtime database of the selected WinCC project is entered in the "Database" field.
   - CAS

     CAS is not available in this version.
   - WinCC Runtime + all segments

     "CC_ExternalBrowsing" is entered in the "Database" field.
9. Activate "Automatic adaption of RT database". When a segment is changed, the name of the database is adjusted in the connection administration.
10. Click the "Create" button.

###### Result

The connection to the data source is created and can be selected in "Connections".

---

**See also**

[Connecting and Disconnecting Swapped Logs (RT Professional)](#connecting-and-disconnecting-swapped-logs-rt-professional)

##### Connecting and Disconnecting Swapped Logs (RT Professional)

This section contains information on the following topics:

- [Configuring a directory (RT Professional)](#configuring-a-directory-rt-professional)
- [Connecting and Disconnecting Logs (RT Professional)](#connecting-and-disconnecting-logs-rt-professional)
- [Connecting Logs using WinCC Archive Connector (RT Professional)](#connecting-logs-using-wincc-archive-connector-rt-professional)

###### Configuring a directory (RT Professional)

###### Introduction

To access data from swapped WinCC logs (log backup file), these logs must be connected to an SQL server again.

You can connect all or individual log backup files of a directory to the SQL server.

###### Requirement

- Write protection of the log backup file has been removed

  Archive backup files are write protected. Create a backup copy of the file before connecting and remove the write protection of the copied log backup file.
- The log backup files are available on the local drive.
- The directories in which the log backup files are set for sharing.

  - The directory must be set for sharing in the Windows Explorer before you start the DataMonitor Server.
  - If you set the directories for sharing later, restart the DataMonitor Server.
- The user group "SIMATIC HMI VIEWER" must have "full access" to the directories.
- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".
- Windows Server: "Network service" has been added to the "Print operators" group.
- Windows: "Network service" has been added to the "Power user" group.

###### Procedure

Proceed as follows to create a symbolic directory:

1. Click in the start page "Webcenter &gt; Administration".
2. Click the "Archive administration" tab.

   ![Procedure](images/23162330123_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23162330123_DV_resource.Stream@PNG-en-US.png)
3. Enter a unique symbolic name in the "Symbolic Name" field.

   The name should only contain the characters permitted in the SQL syntax. You use the symbolic name for access via the DataMonitor client.
4. In "Directory", select the directory in which the log backups are located.

   You can only select directories that have been set for sharing.
5. To connect all existing log backups of the directory, select "Automatically connect all logs in this directory".

   To connect all individual log backup files of the directory, clear "Automatically connect all logs in this directory".
6. Click "Add".

###### Result

You have created the symbolic directory "Test". If you have cleared "Automatically connect all logs in this directory", define the log backups to be connected on the page "[Connect/disconnect logs](#connecting-and-disconnecting-logs-rt-professional)".

To disconnect logs, clear the desired logs on the page "Connect/disconnect logs"

> **Note**
>
> **Connected logs on changeable media**
>
> Before changing the media in the drive you need to disconnect the logs on this medium. After changing the medium, check whether the logs are connected on the new medium.

###### Deleting a symbolic directory

To remove a directory containing logs from the list of symbolic names, disconnect all logs contained in the list. The status of the logs can be seen on the page "Connect/disconnect logs".

###### Connecting and Disconnecting Logs (RT Professional)

###### Requirement

- Write protection of the log backup has been removed

  Log backups are write protected. Create a backup copy of the log before connecting and remove the write protection of the copied archive.
- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".
- [You have configured the symbolic directory "Test"](#configuring-a-directory-rt-professional).

###### Procedure

To connect or disconnect individual log backups, proceed as follows:

1. Click in the start page "Webcenter &gt; Administration".
2. Click the "Connect/disconnect logs" tab.

   ![Procedure](images/23163029515_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23163029515_DV_resource.Stream@PNG-en-US.png)
3. Select the directory "Test" in "Symbolic directories". Existing logs are displayed in a list. The "Info" column provides information about the status.

   - Green: Connected
   - Red: Disconnected
4. To restrict the display, click "Filter".

   ![Procedure](images/23163543819_DV_resource.Stream@PNG-en-US.PNG)

   ![Procedure](images/23163543819_DV_resource.Stream@PNG-en-US.PNG)
5. Enter the desired time period and click "Refresh display".
6. To connect a single archive, select the desired log in the "List of existing logs". Click "Save". The status "Green" indicates that the log is connected.
7. To disconnect a single archive, clear the desired log in the "List of existing logs". Click "Save". The status "Red" indicates that the log is disconnected.

###### Alternative procedure

Archive backups can be connected in the following ways:

- VB function using the "Restore" method. For detailed information, refer to "Restore".
- Automatic Connection: If you copy the log backups to the "CommonArchiving" folder, the logs are connected to the project in Runtime.
- Using [Archive Connector](#connecting-logs-using-wincc-archive-connector-rt-professional).

###### Result

Logs are connected. If you connect signed logs, which have been changed after the swap, an alarm is output.

---

**See also**

[Configuring a directory (RT Professional)](#configuring-a-directory-rt-professional)
  
[Connecting Logs using WinCC Archive Connector (RT Professional)](#connecting-logs-using-wincc-archive-connector-rt-professional)

###### Connecting Logs using WinCC Archive Connector (RT Professional)

###### Introduction

With the Archive Connector, already swapped out WinCC logs can be reconnected to an SQL Server.

###### Requirement

- Write protection of the log backup file has been removed

  Archive backup files are write protected. Create a backup copy of the file before connecting and remove the write protection of the copied log backup file.
- The log backup files are available on the local drive.
- The directories in which the log backup files are set for sharing.
- The user group "SIMATIC HMI VIEWER" must have "full access" to the directories.
- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".

###### Procedure

To connect log backup files, proceed as follows:

1. Start the "Archive Connector".

   ![Procedure](images/4360478987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/4360478987_DV_resource.Stream@PNG-en-US.png)
2. Click "Add" in the "Configuration" tab. The "New Directory" dialog is opened.
3. Navigate to the directory in which the log backup files are stored.
4. Enter a symbolic name for the directory. Click "OK." The directory is displayed on the "Configuration" tab.
5. Click the "Connect/Disconnect Logs" tab. All the logs in the selected directory are listed in the "Connect/Disconnect Logs" tab.

   ![Procedure](images/91635391755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/91635391755_DV_resource.Stream@PNG-en-US.png)
6. Select the desired log and click "Connect".

###### Result

A connection has been created and the desired log backup files are connected to the SQL server.

The connection status of each log is displayed on the "Connect/Disconnect Logs tab". "From" and "To" columns contain the archiving period denoted in the local time zone.

The "Type"column contains the details for log type.

| Symbol | Meaning |
| --- | --- |
| "A" | Alarm logs |
| "TF" | Fast data log |
| "TS" | Slow data log |

### Creating static process screens for the Web Center (RT Professional)

#### Introduction

In the screen management, specify the screens that you need for the Web element "Static process screens".

The DataMonitor Server generates copies of the screens at configurable cyclic intervals and provides these to the DataMonitor Client and the form of static process screens.

#### Requirement

- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".
- The WinCC screens are configured for Web access and published. You can find more detailed information on this under "[Configuring WinCC screens for Web access](#configuring-wincc-screens-for-web-access-rt-professional)".
- The DataMonitor start page is open.
- The "Screen management" tab is open.

#### Creating static process screens for the Web Center

1. Select the screens.

   - To select all screens, activate the check box in the column header.
   - To select individual screens screens, activate the check box leading the relevant screen.

     ![Creating static process screens for the Web Center](images/60946841995_DV_resource.Stream@PNG-en-US.png)

     ![Creating static process screens for the Web Center](images/60946841995_DV_resource.Stream@PNG-en-US.png)
2. To display only part of the screen, define the following:

   - X position: Start positions in x direction in pixels
   - Y position: Start positions in y direction in pixels
   - Width: Width of screen in pixels
   - Height: Height of screen in pixels
3. To set a language for a process screen, select the required language in the drop-down list.
4. To output the time at which the static process screen screen was created by the DataMonitor Server, activate "Stamp".

   The date time are shown in the static process screen.
5. To change the update cycle, enter the desired value in "Update time interval".

   Select this cycle as large as possible. A cycle that is too small leads to performance problems.
6. Click "Save".

#### Result

The DataMonitor Server generates the static process screens from the selected screens. The static process screens can be configured in the Web part "Static process screens".

#### Removing static process screens

To remove static process screens, select the check box at the relevant entry in the "Delete graphic object" column. Click "Save" to remove the static process screen or copy. The deleted static process screens can no longer be configured in the Web part "Static process screens".

#### Finding screen names or limiting the view

Use a filter to find screen names, or to limit the view to specific screen names.

At the "Filter" entry, click ![Finding screen names or limiting the view](images/23239916043_DV_resource.Stream@PNG-de-DE.png) to show the filter above the table. Enter the search term in the text field and then click &lt;Enter&gt;.

To hide the filter, click ![Finding screen names or limiting the view](images/23239908619_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Configuring WinCC screens for Web access (RT Professional)](#configuring-wincc-screens-for-web-access-rt-professional)

### Create a layout template for WebCenter pages (RT Professional)

#### Introduction

You require a layout template to create a WebCenter page. Many prefabricated layouts have been installed during the installation. Additionally, you can create your own Layout Templates.

#### Requirements

- The logged on user is a member of the Windows user group "SIMATIC Report Administrators".
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to create your own layout template:

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Create layout" tab.

   ![Procedure](images/23195043211_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23195043211_DV_resource.Stream@PNG-en-US.png)
3. Define the number of columns and rows.
4. Enter the name "mylayout_23" in the "Name of the layout file" field. Click "Next."
5. If required, group the table fields. For this, click the appropriate arrow symbol, such as "Arrow up", in the desired field, for example line 3 / column 1.

   The modified view will be displayed.

   ![Procedure](images/23195039499_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23195039499_DV_resource.Stream@PNG-en-US.png)

   To restore the original table form, click "Reset configuration".
6. Click "Next."

   ![Procedure](images/23195649675_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23195649675_DV_resource.Stream@PNG-en-US.png)
7. You define the order of the Web parts in the table fields.

   If necessary, select the corresponding symbol in a table field to place the web parts vertically or horizontally.
8. Click "Save".

#### Result

The layout template "mylayout_23" is created. You can use the layout template as a template for creating a WebCenter page.

### Create a WebCenter page (RT Professional)

#### Introduction

#### Requirements

- The directory "myPart" is set up.
- The user logged on is a member of the Windows user group "SIMATIC Report Administrators" or "SIMATIC Report Users".
- The Windows user groups have the "Change" or "Create" access rights to the directory.
- The DataMonitor start page is open.

#### Procedure

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Create Page" tab.
3. Click the desired layout template. The file name is displayed in the "Layout file" field.
4. Enter a name in the "WebCenter page" field, for example "My_Webcenter".
5. Click the directory in which the WebCenter page is stored. The selected directory is displayed in the field "Save WebCenter page as".

   ![Procedure](images/23195047051_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23195047051_DV_resource.Stream@PNG-en-US.png)
6. Click "Save".

#### Result

The WebCenter page has been created and saved.

### Insert Web parts into the WebCenter page (RT Professional)

#### Introduction

You combine Web parts to create the contents of the WebCenter pages.

#### Requirements

- The directory "myPart" is set up.
- The WebCenter page "My_Webcenter" is stored in the directory.
- The user logged on is a member of the Windows user group "SIMATIC Report Administrators" or "SIMATIC Report Users".
- The Windows user groups have the "Change" or "Create" access rights to the directory.
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to insert Web parts in the WebCenter page:

1. Click "WebCenter &gt; Pages" in the start page.
2. Click the "myPart" tab.

   ![Procedure](images/23200556427_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23200556427_DV_resource.Stream@PNG-en-US.png)
3. Click the "My_Webcenter" entry.
4. To add Web parts, click the symbol ![Procedure](images/23200894347_DV_resource.Stream@PNG-de-DE.png) on the right side.

   The available Web parts are listed.

   If you have exported web parts that have already been configured, they are listed under "Imported web parts". If necessary, insert these web parts into your WebCenter page.

   ![Procedure](images/23195641611_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23195641611_DV_resource.Stream@PNG-en-US.png)
5. Select "Trend (Timestamp)".
6. Select the entry "WPZ_01_01" and click "Add".
7. Select "Alarm hit list".

   If you insert several Web parts in a spreadsheet field, they are arranged horizontally or vertically. Specify this arrangement when creating the layout template.
8. Select the entry "WPZ_02_01" and click "Add".
9. Click "Close."

#### Result

Web parts to display data have been inserted into the WebCenter page "My_Webcenter". The current summary of the WebCenter page is displayed.

![Result](images/23200565387_DV_resource.Stream@PNG-en-US.png)

### Configure Web parts within WebCenter pages  (RT Professional)

#### Requirement

- The user logged on is a member of the Windows user group "SIMATIC Report Administrators" or "SIMATIC Report Users".
- The Windows user groups have the "Change" or "Create" access rights to the directory.
- The WebCenter page "My_Webcenter" is open.
- The WinCC project is in Runtime.

#### Procedure

To configure Web parts within WebCenter pages, proceed as follows:

1. Click the icon ![Procedure](images/27002906891_DV_resource.Stream@PNG-de-DE.png) in the desired Web part. The configuration dialog opens.

   ![Procedure](images/23201191691_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23201191691_DV_resource.Stream@PNG-en-US.png)
2. Configure the web part.

   - [Displaying process values in a table](#displaying-process-values-in-a-table-rt-professional)
   - [Displaying process values in a diagram](#displaying-process-values-in-a-diagram-rt-professional)
   - [Displaying messages in the alarm table](#displaying-messages-in-the-alarm-table-rt-professional)
   - [Displaying the hit list of messages](#displaying-the-hit-list-of-messages-rt-professional)
   - [Displaying statistics function for process values](#displaying-statistics-function-for-process-values-rt-professional)
3. To change the position of the web part, move the web part to the desired position with the mouse.

#### More Operational Capabilities

The following operating options are available:

| Symbol | Meaning |
| --- | --- |
| ![More Operational Capabilities](images/10245736715_DV_resource.Stream@PNG-de-DE.png) | Delete Web part |
| ![More Operational Capabilities](images/10245677323_DV_resource.Stream@PNG-de-DE.png) | Minimize Web part |
| ![More Operational Capabilities](images/10245669131_DV_resource.Stream@PNG-de-DE.png) | Maximize Web part |
| ![More Operational Capabilities](images/27003225611_DV_resource.Stream@PNG-de-DE.png) | Export Web part |
| ![More Operational Capabilities](images/10245942539_DV_resource.Stream@PNG-de-DE.png) | Export configuration of the Web part as an XML file |
|  |  |

### Deleting WebCenter Pages and Layout Templates (RT Professional)

#### Requirement

**Deleting layout templates**

- The user is a member of the Windows user group "SIMATIC Report Administrators".
- The DataMonitor start page is open.

**Deleting a WebCenter page**

- The logged-in user must have "Create" access rights for the directory in which the page to be deleted is stored.
- The DataMonitor start page is open.

#### Deleting layout templates

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Delete layout" tab.

   ![Deleting layout templates](images/25184860939_DV_resource.Stream@PNG-en-US.png)

   ![Deleting layout templates](images/25184860939_DV_resource.Stream@PNG-en-US.png)
3. Delete the selected files.

   - To delete several layout files, select the "Selection" check box for the files to be deleted. Click "Delete".
   - To delete all the layout files, click "Select All". Click "Delete".
   - To delete individual layout files, click the respective "Delete" button in the "Action" column.

#### Result

The selected layout file is deleted. Note that this also applies to the layout files included in your package.

Existing WebCenter pages which use this layout template are retained. You cannot use this layout to create new WebCenter pages.

#### Deleting a WebCenter page

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Delete page" tab.
3. Activate the respective check box to mark the pages to be deleted.
4. Click "Delete".

### Exporting and importing WebCenter pages (RT Professional)

#### Requirement

- The logged-on user has access rights.
- The WebCenter page is open.

#### Exporting a WebCenter page

1. Click ![Exporting a WebCenter page](images/53302105355_DV_resource.Stream@PNG-de-DE.png)
2. Select if you want to open or save the file as a WebCenter page in the dialog that opens.

   If you save the file, a file is generated with the format "*.Export".

   To open the file, select a program that can display "*.xml" format.

#### Importing a WebCenter page

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Import page" tab.
3. Enter a file name or click "Browse".
4. To load the file, click "Upload".
5. Enter a name for the WebCenter page.
6. Select the storage location for the WebCenter pages.
7. Click on "Import".

#### Result

The selected WebCenter page is imported and displayed in the DataMonitor.

## Working with Trends and Alarms   (RT Professional)

This section contains information on the following topics:

- [Displaying process values in a table (RT Professional)](#displaying-process-values-in-a-table-rt-professional)
- [Displaying process values in a diagram (RT Professional)](#displaying-process-values-in-a-diagram-rt-professional)
- [Displaying messages in the alarm table (RT Professional)](#displaying-messages-in-the-alarm-table-rt-professional)
- [Alarm Log Column Names (RT Professional)](#alarm-log-column-names-rt-professional)
- [Displaying the hit list of messages (RT Professional)](#displaying-the-hit-list-of-messages-rt-professional)
- [Displaying statistics function for process values (RT Professional)](#displaying-statistics-function-for-process-values-rt-professional)

### Displaying process values in a table (RT Professional)

#### Requirements

- [A connection to the WinCC data is established](#establish-a-connection-to-the-wincc-data-rt-professional)
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to display process values in a table:

1. Click "Trends &amp; Alarms " in the start page. Click the "Process value table" tab. The Web part "Process Value Table" is displayed.
2. Click ![Procedure](images/23239774987_DV_resource.Stream@PNG-de-DE.png). The configuration dialog of the Web part opens.
3. Change the title in the "Header" field. Enter a brief tip in the field "Tooltip".
4. Select the desired connection in the "Connection" field. The logging tags available via this connection will be displayed. You can limit the number of tags using the "Archive selection" and "Tag filter" fields.
5. Click "Add" for the desired logging tags.
6. Define the time range in the "Time period" area.

   With relative times, enter a negative value in the respective field. To obtain additional information on the time specification, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.

   To check the set time range in the column "Preview time frame", click "Preview".
7. Define the number of decimal places in the "Displaying decimal places" section.
8. In the "Table size" area, define the size of the display window. For example, enter a height of "200" and a width of "400".

   If the value "0" is entered into both fields, the size is determined automatically. The size is oriented on spatial requirements of the Web part.
9. The available WebCenter pages are displayed in the "Links to WebCenter Pages" area. To assign the Web part to one or more WebCenter pages, click the ![Procedure](images/23237662219_DV_resource.Stream@PNG-de-DE.png) symbol.
10. Confirm your entries.

#### Result

The values of the logging tags are output in the process value table.

![Result](images/23240257291_DV_resource.Stream@PNG-en-US.png)

Use the arrow keys to skip backward and forward with multi-page tables. You can export the displayed table in CSV format using the ![Result](images/23239782411_DV_resource.Stream@PNG-de-DE.png) icon. Click the ![Result](images/23239774987_DV_resource.Stream@PNG-de-DE.png) symbol to change your settings.

### Displaying process values in a diagram (RT Professional)

#### Requirements

- [A connection to the WinCC data is established](#create-connection-and-set-up-language-rt-professional)
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to display process values in a trend view:

1. Click "Trends &amp; Alarms " in the start page. Click the "Trend (process values)" tab. The Web part "Trend (process values)" is displayed.
2. Click ![Procedure](images/23239774987_DV_resource.Stream@PNG-de-DE.png). The configuration dialog of the Web part opens.
3. Change the title in the "Header" field. Enter a brief tip in the field "Tooltip".
4. Select the desired connection in the "Connection" field. The logging tags available via this connection will be displayed. You can limit the number of tags using the "Archive selection" and "Tag filter" fields.
5. Click "Add" for the desired logging tags, e.g. "TREND_1", "TREND_2", "TREND_3. The logging tags are listed in the "Current selection" area.
6. Define the following for the individual logging tags in the "Current selection" area:

   - color of time and value axis
   - form of the trend display
7. In the section "Value axis editor", you can select the automatic scaling for the different value axes or you can assign a minimum and a maximum value to each axis.
8. Define the time range in the "Time period" area.

   With relative times, enter a negative value in the respective field. To obtain additional information on the time specification, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol. To check the set time range in the column "Preview time frame", click "Preview".
9. In the section "Diagram settings", define the size of the display window. If the value "0" is entered into both fields, the size is determined automatically. The size is oriented on spatial requirements of the Web part.
10. To display the legend, select "Show legend".
11. The available WebCenter pages are displayed in the "Links to WebCenter Pages" area. To assign the Web part to one or more WebCenter pages, click the ![Procedure](images/23237662219_DV_resource.Stream@PNG-de-DE.png) symbol.
12. Confirm your entries.

#### Result

The selected process values are displayed as trends in a diagram.

![Result](images/23240320011_DV_resource.Stream@PNG-en-US.png)

The legend shows the assignment of the colors to the logging tags. Skip forward or back by the selected time frame in the absolute time using the ![Result](images/23239834379_DV_resource.Stream@PNG-de-DE.png) and ![Result](images/23239826955_DV_resource.Stream@PNG-de-DE.png) buttons.

Enlarge the display and you can zoom into the diagram area to the left and right of the center line using the "Zoom left" ![Result](images/23239804683_DV_resource.Stream@PNG-de-DE.png) and "Zoom right" ![Result](images/10303882507_DV_resource.Stream@PNG-de-DE.png) buttons. The ![Result](images/23239819531_DV_resource.Stream@PNG-de-DE.png) button is used to restore the original view.

Export the table displayed in CSV format using the ![Result](images/23239782411_DV_resource.Stream@PNG-de-DE.png) icon.

Click the ![Result](images/23239774987_DV_resource.Stream@PNG-de-DE.png) symbol to change your settings.

### Displaying messages in the alarm table (RT Professional)

#### Requirement

- [A connection to the WinCC data is established.](#create-connection-and-set-up-language-rt-professional)
- The DataMonitor start page is open.

#### Procedure

To display alarms in the alarm table, proceed as follows:

1. Click "Trends &amp; Alarms " in the start page. Click the "Alarm table" tab. The Web part "Alarm Table" is displayed.

   Click ![Procedure](images/23239774987_DV_resource.Stream@PNG-de-DE.png). The configuration dialog of the Web part opens.
2. Change the title in the "Header" field. Enter a brief tip in the field "Tooltip".
3. Select the connection in the "Connection" field.
4. Select the corresponding WinCC server in the "Selection of WinCC Servers" area.

   You need this setting to be able to select a connection to a swapped out archive that contains log files from several WinCC servers.
5. Define the time range in the "Time period" area. With relative times, enter a negative value in the respective field. To obtain additional information on the time specification, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol. To check the set time range in the column "Preview time frame", click "Preview".
6. In the section "Language of the alarm texts", select the language in which the alarms are displayed.
7. In the section "Filter selection", limit the expected search results by means of filter conditions in SQL syntax. To obtain additional information on the filter conditions, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.
8. Define the following for displaying the data:

   - Sorting order: To obtain additional information on sorting, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.
   - Visible columns: To display all the columns, click "Select All". You can find more detailed information on this under "[Alarm Log Column Names](#alarm-log-column-names-rt-professional)".
   - Number of decimal places
9. In the "Table size" area, define the size of the display window.
10. The available WebCenter pages are displayed in the "Links to WebCenter Pages" area. To assign the Web part to one or more WebCenter pages, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.
11. Confirm your entries.

    ![Procedure](images/23240424075_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/23240424075_DV_resource.Stream@PNG-en-US.png)

#### Result

Use the arrow keys to skip backward and forward with multi-page tables. You can export the displayed table in CSV format using the ![Result](images/23239782411_DV_resource.Stream@PNG-de-DE.png) icon. Click the ![Result](images/23239774987_DV_resource.Stream@PNG-de-DE.png) symbol to change your settings.

---

**See also**

[Create connection and set up language (RT Professional)](#create-connection-and-set-up-language-rt-professional)
  
[Alarm Log Column Names (RT Professional)](#alarm-log-column-names-rt-professional)

### Alarm Log Column Names (RT Professional)

#### Introduction

You can select the alarm log columns while displaying alarms in "Trends and Alarms".

#### Overview of column names

| Position | Name | Type | Comments |
| --- | --- | --- | --- |
| 1 | MsgNo | Integer 4 Bytes | Alarm number |
| 2 | State | Small Integer 2 Bytes | Alarm Log Status |
| 3 | DateTime | DateTime 8 Bytes | Time stamp of alarm (Date/time without milliseconds) |
| 4 | Ms | Small Integer 2 Bytes | Time stamp of alarm (milliseconds) |
| 5 | Instance | VarChar (255) | Instance Name of the Alarm Log |
| 6 | Flags1 | Integer 4 Bytes | (only for internal use) |
| 7 | PValueUsed | Integer 4 Bytes | Process Values used |
| 8 to 17 | PValue1 to PValue10 | Real 8 Bytes | Numerical Process Value 1 to 10 |
| 18 to 27 | PText1 to PText10 | VarChar (255) | Process Value Text 1 to 10 |
| 28 | Computer name | VarChar (255) | Computer Name |
| 29 | Application | VarChar (255) | Application Name |
| 30 | Comment | VarChar (255) | Comments |
| 31 | UserName | VarChar (255) | User Name |
| 32 | Counter | Integer 4 Bytes | Running Alarm Message Counter |
| 33 | TimeDiff | Integer 4 Bytes | Time difference to "Incoming" status |
| 34 | ClassName | VarChar (255) | Alarm class name |
| 35 | Type name | VarChar (255) | Alarm type name |
| 36 | Class | Small Integer 2 Bytes | Alarm class ID |
| 37 | Type | Small Integer 2 Bytes | Message type ID |
| 38 to 47 | Text1 to Text10 | VarChar (255) | Alarm Text 1 to 10 |
| 48 | AG_NR | Small Integer 2 Bytes | Number of the PLC |
| 49 | CPU_NR | Small Integer 2 Bytes | Number of the CPU |
| 50 | CrComeFore | Integer 4 Bytes | Foreground Color for the "Incoming" Status |
| 51 | CrComeBack | Integer 4 Bytes | Background Color for the "Incoming" Status |
| 52 | CrGoFore | Integer 4 Bytes | Foreground Color for the "Outgoing" Status |
| 53 | CrGoBack | Integer 4 Bytes | Background Color for the "Outgoing" Status |
| 54 | CrAckFore | Integer 4 Bytes | Foreground Color for the "Acknowledged" Status |
| 55 | CrAckBack | Integer 4 Bytes | Background Color for the "Acknowledged" Status |
| 56 | LocaIID | Integer 4 Bytes | Location of the Alarm |
| 57 | Priority | Integer 4 Bytes | Priority |
| 58 | AP_type | Integer 4 Bytes | Loop-in alarm |
| 59 | AP_name | VarChar (255) | Loop-in-Alarm Function Name |
| 60 | AP_PAR | VarChar (255) | Loop-in-Alarm Screen |
| 61 | InfoText | VarChar (255) | Info text |
| 62 | TxtCame | VarChar (255) | Incoming text |
| 63 | TxtWent | VarChar (255) | Outgoing text |
| 64 | TxtCameNWent | VarChar (255) | Text came in and went out |
| 65 | TxtAck | VarChar (255) | Text acknowledged |
| 66 | AlarmTag | Integer 4 Bytes | Alarm tag |
| 67 | AckType | Small Integer 2 Bytes | Acknowledgment Type |
| 68 | Params | Integer 4 Bytes | Parameter |

---

**See also**

[Displaying messages in the alarm table (RT Professional)](#displaying-messages-in-the-alarm-table-rt-professional)

### Displaying the hit list of messages (RT Professional)

#### Requirements

- [A connection to the WinCC data is established](#create-connection-and-set-up-language-rt-professional)
- The DataMonitor start page is open.

#### Procedure

To display alarms in a hit list, proceed as follows:

1. Click "Trends &amp; Alarms " in the start page. Click the "Alarm hit list " tab. The web part "Hit list of the alarms" is displayed.

   Click ![Procedure](images/23239774987_DV_resource.Stream@PNG-de-DE.png). The configuration dialog of the Web part opens.
2. Change the title in the "Header" field. Enter a brief tip in the field "Tooltip".
3. Select the desired connection in the "Connection" field:
4. Define the time range in the "Time period" area. With relative times, enter a negative value in the respective field. To obtain additional information on the time specification, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol. To check the set time range in the column "Preview time frame", click "Preview".
5. In the section "Language of the alarm texts", select the language in which the alarms are displayed.
6. Select the corresponding WinCC server in the "Selection of the WinCC Server" area.

   You need this setting to be able to select a connection to a swapped out archive that contains log files from several WinCC servers.
7. In the section "Filter selection", limit the expected search results by means of filter conditions in SQL syntax. To obtain additional information on the filter conditions, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.
8. Define the following for displaying the data:

   - Sorting order: To obtain additional information on sorting, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.
   - Visible columns: To display all the columns, click "Select All".
   - Number of decimal places
9. In the "Table size" area, define the size of the display window. If the value "0" is entered into both fields, the size is determined automatically. The size is oriented on spatial requirements of the table.
10. The available WebCenter pages are displayed in the "Links to WebCenter Pages" area. To assign the Web part to one or more WebCenter pages, click the ![Procedure](images/23237662219_DV_resource.Stream@PNG-de-DE.png) symbol.
11. Confirm your entries.

#### Result

The analysis values for the alarms are displayed in a hit list:

![Result](images/23240374155_DV_resource.Stream@PNG-en-US.png)

The table contains configured data and statistical values, e.g. InfoText, frequency of the alarm.

Explanations for the columns are displayed as a tool tip when the mouse is moved over the respective column header. Use the arrow keys to skip backward and forward with multi-page tables.

With the icon ![Result](images/23239782411_DV_resource.Stream@PNG-de-DE.png), the displayed analysis values of the alarms can be exported in CSV format. Click the ![Result](images/23239774987_DV_resource.Stream@PNG-de-DE.png) symbol to change your settings.

> **Note**
>
> The display of alarms in the hit list may take some time and may place a strong load on the CPU. A note is displayed in "Trends and Alarms" if the data volume is too high. You may then confirm the alarm and continue without any changes, or you may cancel the process to modify the filter criteria and thus reduce the expected amount of data.

### Displaying statistics function for process values (RT Professional)

#### Requirements

- [A connection to the WinCC data is established](#create-connection-and-set-up-language-rt-professional)
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to display statistics functions for process values:

1. Click "Trends &amp; Alarms " in the start page. Click the "Statistics functions for process values" tab. The Web part "Statistics functions for process values" is displayed.
2. Click ![Procedure](images/23239774987_DV_resource.Stream@PNG-de-DE.png). The configuration dialog of the Web part opens.
3. Change the title in the "Header" field. Enter a brief tip in the field "Tooltip".
4. Select the desired connection in the "Connection" field. The logging tags available via this connection will be displayed. You can limit the number of tags using the "Archive selection" and "Tag filter" fields.
5. Click "Add" for the desired logging tags.
6. Define the time range in the "Time period" area.

   With relative times, enter a negative value in the respective field. To obtain additional information on the time specification, click the ![Procedure](images/23239666443_DV_resource.Stream@PNG-de-DE.png) symbol.

   To check the set time range in the column "Preview time frame", click "Preview".
7. Define the following for displaying the data:

   - Number of decimal places
   - Aggregate selection: Define the analysis function for the process values.
8. In the "Table size" area, define the size of the display window. For example, enter a height of "200" and a width of "400". If the value "0" is entered into both fields, the size is determined automatically. The size is oriented on spatial requirements of the table.
9. The available WebCenter pages are displayed in the "Links to WebCenter Pages" area. To assign the Web part to one or more WebCenter pages, click the ![Procedure](images/23237662219_DV_resource.Stream@PNG-de-DE.png) symbol.
10. Confirm your entries.

#### Result

Statistics functions for the selected process values were executed and output in the table.

The log name and tag name are displayed as a tool tip when the mouse is moved over the respective column header.

![Result](images/23240486795_DV_resource.Stream@PNG-en-US.png)

You can export the displayed table in CSV format using the ![Result](images/23239782411_DV_resource.Stream@PNG-de-DE.png) icon. Click the ![Result](images/23239774987_DV_resource.Stream@PNG-de-DE.png) symbol to change your settings.

## Working with Excel Workbooks (RT Professional)

This section contains information on the following topics:

- [Configuring an Excel workbook (RT Professional)](#configuring-an-excel-workbook-rt-professional)
- [Displaying process data in an Excel Workbook online (RT Professional)](#displaying-process-data-in-an-excel-workbook-online-rt-professional)
- [Alarm Attributes (RT Professional)](#alarm-attributes-rt-professional)
- [VBA Functions of the Excel Workbook (RT Professional)](#vba-functions-of-the-excel-workbook-rt-professional)

### Configuring an Excel workbook (RT Professional)

This section contains information on the following topics:

- [Importing data from a WinCC project (RT Professional)](#importing-data-from-a-wincc-project-rt-professional)
- [Importing data from an xml file (RT Professional)](#importing-data-from-an-xml-file-rt-professional)
- [Configuring the display of tag values (RT Professional)](#configuring-the-display-of-tag-values-rt-professional)
- [Configuring the display of logging tags (RT Professional)](#configuring-the-display-of-logging-tags-rt-professional)
- [Configuring the display of alarms (RT Professional)](#configuring-the-display-of-alarms-rt-professional)
- [Publishing an Excel workbook (RT Professional)](#publishing-an-excel-workbook-rt-professional)

#### Importing data from a WinCC project (RT Professional)

##### Introduction

You need the WinCC configuration data to configure Excel workbooks.

Import this data from a local WinCC project for configuration in Excel Workbook Wizard .

##### Requirement

- Server PC

  - Microsoft Office 2019 or Microsoft Office 2021 installed
  - The Excel add-In "Excel Workbook" is installed.
  - DataMonitor Server is installed.
  - The WinCC project is in Runtime.
  - A user is created in WinCC.
- On the configuration PC

  - Microsoft Office 2019 or Microsoft Office 2021 installed
  - The Excel add-In "Excel Workbook Wizard" is installed.

> **Note**
>
> Due to safety settings, the automatic connection of an Excel workbook with the server does not work in Excel.
>
> To enable automatic connection, disable the "Enable protected view for files originating from the internet" and "Enable Protected View for files located in potential unsafe locations" settings in Excel under "Files &gt; Options &gt; Trust Center &gt; ProtectedView".

##### Procedure

To import data from a WinCC project, proceed as follows on the configuration PC:

1. Open an empty Excel workbook. Select the "Excel Workbook Wizard..." command in the "DataMonitor" menu.
2. Activate the option "Establish connection with WinCC server".
3. The "WinCC Server" field is shown. Enter the name of the server PC and then click "Connect". The log in dialog is displayed.
4. Enter the name and password of a WinCC user.
5. Click "Next &gt;". The "Add / delete tags" dialog opens.

##### Result

The Excel workbook is configured. Create the view of process data.

#### Importing data from an xml file (RT Professional)

##### Introduction

You can create the Excel workbook on a PC if, for example, Excel is not installed on the server PC. Create the corresponding xml file on the DataMonitor Server.

##### Requirements

- Server PC

  - DataMonitor Server is installed.
  - The WinCC project is in Runtime.
  - A user is created in WinCC.
- On the configuration PC

  - MS Office 2019 or MS Office 2021 ist installed.
  - The Excel add-in "Excel Workbook Wizard" is installed.

##### Creating an XML file on the server PC

1. In the Start menu, select the command "Start &gt; All Programs &gt; Siemens Automation &gt; Option and Tools &gt; HMI Tools &gt; WinCC DataMonitor Configurator Export".

   The function creates an XML file and stores it in subdirectory "Web Navigator\Reports" of the current project. The file name is automatically generated using the format "&lt;projectname&gt;.XML".
2. If no Excel installation exists on the server PC, transfer the XML file to another PC on which MS Excel and the Excel Workbook Wizard are installed.

##### Configuring data access using an XML file

1. Open an empty Excel workbook. Select the "Excel Workbook Wizard..." command in the "DataMonitor" menu.
2. Activate the option "Load configuration data from file". Click "Next &gt;".
3. Navigate to the required XML file.
4. Click "Next &gt;". The "Add / delete tags" dialog opens.

##### Result

The Excel workbook is configured. Create the view of process data. Transfer the Excel workbook to the client PC. The DataMonitor Client displays the process data of the server PC.

#### Configuring the display of tag values (RT Professional)

##### Requirements

- The dialog "Add / delete tags" is open.

##### Procedure

Proceed as follows to display tag values in Excel:

1. Check the option for the insert sequence of tag groups in the "Add tags" area.

   ![Procedure](images/23230785419_DV_resource.Stream@PNG-en-US.PNG)

   ![Procedure](images/23230785419_DV_resource.Stream@PNG-en-US.PNG)
2. In the "Tag tree" area, click the directory icon. The object list opens.
3. Select the desired tag in the object list and drag the tag to a field of the Excel table.
4. Close the object list. The tag will be displayed in the window "Tag list".
5. In the "Tag list" window, select the tag and the "Server settings" command from the shortcut menu.
6. In the "Server settings" dialog, enter the name and password of a WinCC user. Activate "Activate automatic login". Confirm your entries.
7. In the window "Tag list", select the tag and select the menu command "Properties" from the shortcut menu. The dialog "Tag properties" will be opened.

   ![Procedure](images/23230719499_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23230719499_DV_resource.Stream@PNG-en-US.png)
8. Define the properties for the view in the table, e.g. the arrangement of headers, time stamps, and quality code.
9. To apply the set update cycle to all tags, select "Save as default".

   Settings in the areas "Display in sheet" and "Additional Data" are not valid for all tags.
10. Confirm your entries. Click the "Next &gt;" button in the dialog "Add tag". The dialog "[Add/delete logging tags](#configuring-the-display-of-logging-tags-rt-professional)" is opened.

##### Result

The display of tag values in an Excel sheet is configured.

In the Excel workbook, each table cell is assigned a short text and a comment which was configured for displaying a tag value.

With tag values, the short text "OV" stands for online tags.

In the comments, the source of the displayed values is shown in the format "WDWx_&lt;number&gt;_&lt;tagname&gt;".   
The value for x means:

- O = Online value

  > **Note**
  >
  > After deleting/moving cells filled with configuration data or deleting/inserting new lines/columns in the Excel worksheet, the Excel Workbook Wizard must be executed again. The configuration data is checked and automatically adapted as a result. Confirm the data displayed simply by using the "Next &gt;" button. Save the workbook and close Excel.

#### Configuring the display of logging tags (RT Professional)

> **Note**
>
> If you have connected logs using the WinCC objects "f(x) trend view", "f(t) trend view" or "table view", you can no longer connect these logs with the DataMonitor.
>
> If you have connected logs using the DataMonitor, you can no longer connect these logs using the WinCC objects "f(x) trend view", f(t) trend view" or "table view".

##### Requirement

- The dialog "Add / delete logging tags" is open.

##### Procedure

Proceed as follows to display logging tags in Excel:

1. In the "Tag tree" area, click the directory icon. The object list opens.
2. Select the desired logging tag in the object list and drag the logging tag into a field of the Excel table.
3. Close the object list. The logging tag will be displayed in the window "Tag list".
4. In the window "Tag list", select the logging tag and select the menu command "Properties" from the shortcut menu. The dialog "Archive tag properties" will be opened.

   ![Procedure](images/23229602443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23229602443_DV_resource.Stream@PNG-en-US.png)
5. Define properties for display in the table, e.g. the insert sequence, data resolution, display time window.
6. To save the settings, select "Save as default". The settings in the "Additional data" area are not saved.
7. Confirm your entries. Click the "Next &gt;" button in the dialog "Add logging tag". The dialog "[Add/remove alarms](#configuring-the-display-of-alarms-rt-professional)" will open.

**Note**

If you use the option "Number of data" for Data resolution &gt; User-defined resolution", enter an even value in the input box. Even values ensure proper trend display.

##### Result

The display of logging tag values in an Excel sheet is configured.

In the Excel workbook, each table cell is assigned a short text and a comment which was configured for displaying a tag value.

With tag values, the short text "AV" stands for logging tags.

In the comments, the source of the displayed values is shown in the format "WDWx_&lt;number&gt;_&lt;tagname&gt;".   
The value for x means:

- A = Log value

  > **Note**
  >
  > After deleting/moving cells filled with configuration data or deleting/inserting new lines/columns in the Excel worksheet, the Excel Workbook Wizard must be executed again. The configuration data is checked and automatically adapted as a result. Confirm the data displayed simply by using the "Next &gt;" button. Save the workbook and close Excel.

---

**See also**

[Configuring the display of tag values (RT Professional)](#configuring-the-display-of-tag-values-rt-professional)

#### Configuring the display of alarms (RT Professional)

> **Note**
>
> If you have connected logs using the WinCC object "alarm view", you can no longer connect these logs with the DataMonitor.
>
> If you have connected logs using the DataMonitor, you can no longer connect these logs with the WinCC object "alarm view".

##### Requirement

The dialog "Add / Delete Alarms" is open.

##### Procedure

Proceed as follows to display alarms in Excel:

1. Select the required cell in the Excel table. Click "Add alarm".
2. In the "Add alarm" area, click the directory icon. The dialog "Alarm - properties" will be opened.

   ![Procedure](images/23230727563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23230727563_DV_resource.Stream@PNG-en-US.png)
3. Define the properties for the display of alarms in the Excel table, such as headings and insertion sequence of attributes.
4. Enter a filter condition in the "Filter string" field or use the selection dialog to define specific alarms to be displayed, for example.
5. Use the "Maximum number of alarms" option to limit the number of most recent alarms displayed. You can display maximum 1,000 alarms.
6. Activate the desired attributes in the list. For additional information, refer to "[Alarm Attributes](#alarm-attributes-rt-professional)".
7. To save the setting, select "Save as default".
8. Confirm your entries. Click the "Next &gt;" button in the dialog "Add logging tag": The "Description" dialog box will open.

##### Result

The display of alarms in an Excel sheet is configured.

In the Excel workbook, each table cell is assigned a short text and a comment which was configured for displaying an alarm.

With alarms, the short text "AL" and the comment are shown in the format "WDWL_&lt;number&gt;_&lt;field name&gt;".

> **Note**
>
> After deleting/moving cells filled with configuration data or deleting/inserting new lines/columns in the Excel worksheet, the Excel Workbook Wizard must be executed again. The configuration data is checked and automatically adapted as a result. Confirm the data displayed simply by using the "Next &gt;" button. Save the workbook and close Excel.

---

**See also**

[Configuring the display of logging tags (RT Professional)](#configuring-the-display-of-logging-tags-rt-professional)
  
[Alarm Attributes (RT Professional)](#alarm-attributes-rt-professional)

#### Publishing an Excel workbook (RT Professional)

##### Requirement

The display of tag values, logging tags and alarms is configured.

The "Description" dialog box is open.

##### Procedure

To access Excel workbooks on the DataMonitor Server, proceed as follows:

1. Click "Publish". The Excel workbook is made available for download on the DataMonitor Server.
2. Use the "Template" button to provide the Excel Workbook for the function "Published Reports".
3. Exit the Excel Workbook Wizard
4. Save the workbook and close Excel.

##### Alternative procedure

You publish the Excel template on the DataMonitor client. For additional information, refer to "[Preparing an Excel Workbook as a Template](#preparing-an-excel-workbook-as-a-template-rt-professional)".

##### Result

The Excel workbook is made available on the DataMonitor Server. If required, the Excel workbook is downloaded on the DataMonitor clients or opened directly in Internet Explorer.

---

**See also**

[Preparing an Excel Workbook as a Template (RT Professional)](#preparing-an-excel-workbook-as-a-template-rt-professional)

### Displaying process data in an Excel Workbook online (RT Professional)

#### Requirements

- The Excel workbook with the configuration of the process value display must be available on the PC.
- One of the following Excel versions is necessary for online display in the Excel Workbook:

  - MS Office 2019
  - MS Office 2021
- WinCC Runtime Professional is installed.
- DataMonitor Server is installed.
- The WinCC project is in Runtime.
- The DataMonitor start page is open.
- [The user "DM_Demo" has been created](#defining-users-in-wincc-rt-professional).

#### Procedure

1. Click "WebCenter &gt; Configuration" in the start page.
2. Click the "Report tools" tab.

   The Excel workbooks that were published in the Excel Workbook Wizard, are shown in an overview.

   ![Procedure](images/25134131211_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25134131211_DV_resource.Stream@PNG-en-US.png)
3. Select a workbook.
4. Click the Excel workbook symbol in the "Open / Save" column.
5. Click "Open &gt;" in the next dialog. The Excel workbook opens.
6. Select the "Excel Workbook" command in the "DataMonitor" menu.
7. The name of one of the servers, whose tags are configured in the Excel table, is displayed in the "WinCC Server" field.

   The following options are available for the server name:

   - Access via domain

     In case of accesses from outside the network domain, the domain is indicated along with the server name.
   - The DataMonitor start page is the standard Web page.

     Only the server name is entered in the "WinCC Server" field.
   - The DataMonitor start page is in the virtual directory:

     The name of the virtual folder needs to be specified after the server name, e.g. "/webnavigator".
8. Activate the "All servers" check box when the tags from several servers are configured in an Excel sheet. The tag values of all the servers are updated in the online display.
9. Activate the connection to the WinCC project via the button "Connect". After a successful connection, the log-in dialog will be opened. Type in the user name "DM_Demo" and the corresponding password. When several servers are used, the logon dialogs of the servers concerned open one after the other.

   If no connection is established, a corresponding message is displayed. Clicking on the dialog will display further information about the error (if available).
10. The connection status will be displayed in the dialog. To update the respective values or displays, click the buttons "Read tags", "Read logging tags" and "Read alarms" buttons.

    ![Procedure](images/3973515019_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/3973515019_DV_resource.Stream@PNG-en-US.png)

    To update the tag values in cycles, select the "Read cyclically" check box.
11. Close the dialog "Excel Workbook" after ending your calculations in Excel.
12. Save the results in the workbook and close Excel.

**Note**

To establish connections to all the servers, select "All servers" before pressing the "Connect" button to establish the connection.

**Note**

The Excel Workbook dialog must not be closed as long as the logon dialog for connection establishment to the server persists.

#### Result

The values of an online tag, a logging tag as well as a message window are displayed in the Excel table.

---

**See also**

[Defining users in WinCC (RT Professional)](#defining-users-in-wincc-rt-professional)

### Alarm Attributes (RT Professional)

#### Introduction

While displaying messages in Excel Workbook you can select the attributes to be displayed in the Excel sheet in the Excel Workbook Wizard .

#### Overview

| Position | Attribute | Type | Comments |
| --- | --- | --- | --- |
| 1 | Alarm class name | VarChar (255) |  |
| 2 | Alarm type name | VarChar (255) |  |
| 3 | Foreground color | Integer 4 Bytes |  |
| 4 | Background color | Integer 4 Bytes |  |
| 5 | Flashing color | Integer 4 Bytes |  |
| 6 to 15 | Alarm Text 1 to 10 | VarChar (255) |  |
| 16 to 25 | Process value 1 to 10 | Real 8 Bytes | Numerical Process Value 1 to 10 |
| 26 | State | VarChar (255) | Status text |
| 27 | Info text | VarChar (255) |  |
| 28 | Alarm class ID | Integer 4 Bytes |  |
| 29 | Message type ID | Integer 4 Bytes |  |
| 30 | AS Number | Small Integer 2 Bytes |  |
| 31 | CPU Number | Small Integer 2 Bytes |  |
| 32 | Duration | Integer 4 Bytes | Time difference to "Incoming" status |
| 33 | Alarm counter | Integer 4 Bytes | Consecutive alarm counter |
| 34 | Acknowledgment Status | VarChar (255) | Text of the acknowledgement status |
| 35 | Priority | Integer 4 Bytes |  |
| 36 | Application |  | Application with which the comment was created. |
| 37 | Computer | VarChar (255) | Computer on which the comment was created. |
| 38 | Users | VarChar (255) | User who created the comment. |
| 39 | Comments | VarChar (255) |  |

---

**See also**

[Configuring the display of alarms (RT Professional)](#configuring-the-display-of-alarms-rt-professional)

### VBA Functions of the Excel Workbook (RT Professional)

#### Excel workbooks: VBA functions of the Excel workbook

The following functions are available to you in an Excel workbook if you have generated an instance of the Excel workbook object using the "Application.COMAddIns.Item("ExcelWorkbook.Connect").Object".

- ShowDialog(0): Opens the "Excel Workbook" dialog with a normal size.
- ShowDialog(1): Opens the "Excel Workbook" dialog with a minimized size.
- ShowDialog(2): Opens the "Excel Workbook" dialog hidden.
- CloseDialog: Closes the "Excel Workbook" dialog.
- GetServerID(server name): Gets the ID of the WinCC server with a specified name, for example: "http://Local_PC".
- Connect(ServerID): Connects the specified WinCC server to the Excel workbooks. You can get the "ServerID" using the "GetServerID(server name)" function. The "Excel Workbook" dialog must be opened before establishing a connection.
- ConnectAll: Connects all WinCC servers to Excel workbooks. The "Excel Workbook" dialog must be opened before establishing a connection.
- Disconnect(ServerID): Disconnects the Excel workbook from the specified WinCC server.
- DisconnectAll: Disconnects the Excel workbook from all WinCC servers.
- ReadTags(ServerID): Reads the tags from WinCC server with "ServerID". The connection must be established before tags can be read.
- ReadArchives(ServerID): Reads the logs from WinCC server with "ServerID". The connection must be established before logs can be read.
- ReadAlarms(ServerID): Reads the alarms from WinCC server with "ServerID". The connection must be established before alarms can be read.

As soon as a connection is established or closed, the event "ServerConnected(ServerID)" or "ServerDisconnected(ServerID)" is output by the "ExcelWorkbook.Connect" object. These events can be integrated, for example, using "WithEvents" (VB standard).

## Working with reports (RT Professional)

This section contains information on the following topics:

- [Preparing an Excel Workbook as a Template (RT Professional)](#preparing-an-excel-workbook-as-a-template-rt-professional)
- [Making an Excel workbook available as a report tool (RT Professional)](#making-an-excel-workbook-available-as-a-report-tool-rt-professional)
- [Making Settings for Reports (RT Professional)](#making-settings-for-reports-rt-professional)
- [Displaying a report with an Excel Workbook (RT Professional)](#displaying-a-report-with-an-excel-workbook-rt-professional)
- [Creating a report with a print job (RT Professional)](#creating-a-report-with-a-print-job-rt-professional)

### Preparing an Excel Workbook as a Template (RT Professional)

#### Requirement

- The Excel workbook is created.
- The start page of the DataMonitor is open.
- The regional settings of the operating system match the installed Office language.

#### Procedure

Proceed as follows to prepare Excel workbooks as a template:

1. Click "Reports" in the start page.
2. Click the "Upload templates" tag.

   ![Procedure](images/23240088587_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23240088587_DV_resource.Stream@PNG-en-US.png)
3. Select a directory, in which the template will be stored in the "Target directory" field.

   Only the directories, for which the user that is logged in has "Create" access rights, can be selected.
4. Click the "Browse" button in the "Selected template" field. Navigate to the required Excel workbook.
5. Click the "Upload" button.

#### Result

The template is prepared for the function "Published Reports".

---

**See also**

[Publishing an Excel workbook (RT Professional)](#publishing-an-excel-workbook-rt-professional)
  
[Configuring an Excel workbook (RT Professional)](#configuring-an-excel-workbook-rt-professional)

### Making an Excel workbook available as a report tool (RT Professional)

#### Requirement

- The Excel workbook is created.
- The start page of the DataMonitor is open.
- The regional settings of the operating system match the installed Office language.

#### Procedure

Proceed as follows to prepare Excel workbooks as a report tool:

1. Click "Reports" in the start page.
2. Click the "Upload templates" tag.

   ![Procedure](images/23240088587_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23240088587_DV_resource.Stream@PNG-en-US.png)
3. Click the "Browse" button in the "Excel Workbook" field. Navigate to the required Excel workbook
4. Click the "Upload" button.

#### Result

The Excel workbook is ready in the "Report tools" section.

### Making Settings for Reports (RT Professional)

#### Introduction

Different settings are required for using the function "Reports" from DataMonitor.

#### Requirements

- PDF Reader is installed.
- The WinCC project is selected on the DataMonitor server.
- The WinCC project is selected in "Scheduled print jobs in Runtime".
- The DataMonitor start page is open.

#### Procedure

To configure the reports settings, proceed as follows:

1. Click "Reports " in the start page. Click the "Settings" tab.

   The "Settings" page is displayed.

   ![Procedure](images/23239923467_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23239923467_DV_resource.Stream@PNG-en-US.png)
2. Check the entries in the section "General project settings".

   To enable output to a PDF file, select "Activate API print".
3. Enter the data for sending mail in the "Mail" area:

   - Server

     Outgoing mail server (SMTP)
   - User name

     Name for the sender
   - Password
   - Sender

     Email account, through which you send your Email
4. Click the disk icon in the section "General project settings" to save your settings.
5. In the "Circular buffer" area, you can define how many reports can be stored for the selected target directory. The field has a pre-assigned value of 20.
6. Click the disk icon in this section to save your settings.

#### Result

The settings for "Reports" have now been made.

### Displaying a report with an Excel Workbook (RT Professional)

#### Requirements

- PDF Reader is installed.
- The WinCC project is selected on the DataMonitor server.
- The WinCC project is selected in "Scheduled print jobs in runtime".
- The DataMonitor start page is open.

#### Procedure

Proceed as follows to create a report with Excel workbooks:

1. Click "Reports" in the start page. Click the "Excel Workbooks" tab.

   The "Excel Workbooks" page is displayed.

   ![Procedure](images/23240055307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23240055307_DV_resource.Stream@PNG-en-US.png)

   The icons in front of the lists "List of time-controlled Excel Workbooks" and "List of event-controlled Excel Workbooks" are cleared and show that currently, no reports are triggered.
2. Select the desired Excel workbooks, e.g. "My_workbook_1.xls" in the "Existing Excel Workbooks" field.

   This field only shows Excel Workbooks that meet the following conditions:

   - Workbooks that are published as templates in the Excel Workbook Wizard
   - Workbooks in directories for which the current user has the "Read" access right.
3. Select the directory, in which the reports will be stored in the "Target directory" field.

   Only the directories, for which the user that is logged in has "Create" access rights, can be selected.
4. Enter an e-mail address in the field "E-mail recipient". The report is e-mailed to this address.
5. To configure time-controlled triggering, define the following in the "Time-controlled Excel Workbooks" area.

   - Date:

     Enter the date in the field or define the date using the calendar. To open the calendar, click the "calendar" symbol.
   - Time

     Define the triggering time.
   - Repetition

     Define the repetition rate, e.g. "Once" or "Weekly".
6. Click the "Add" button in the "Time-controlled Excel Workbooks" area. The report is displayed in the "List of time-controlled Excel workbooks".
7. To create the report immediately, click the symbol ![Procedure](images/23239878923_DV_resource.Stream@PNG-de-DE.png).
8. To configure event-controlled triggering, define the following in the "Event-controlled Excel Workbooks" area.

   - Selected WinCC tag

     Click ![Procedure](images/23267207435_DV_resource.Stream@PNG-de-DE.png). The object list opens. Select the desired tag from the object list.
   - Define the event control

     Define the triggering event, e.g. change of the tag value.

     If you selected "Low limit", "High limit", or "Both limits" for event control, you need corresponding limit values.
9. Click the "Add" button in the "Event-controlled Excel Workbooks" area. The report is displayed in the "List of event-controlled Excel workbooks"

#### Result

A time-controlled or event-controlled report has been triggered with an Excel workbook.

The report is displayed in one of the lists "List of time-controlled Excel workbooks" and "List of event-controlled Excel workbooks". The report can be changed or deleted in the list.

> **Note**
>
> An event-controlled print job will not be initiated if the time, in which the tag changes, is less than one minute.
>
> Note that frequent initiation of the event-controlled print job OR simultaneous initiation of several print jobs over an extended period will lead to heavy load on memory space and resources, e.g. frequent signal changes of a tag.

### Creating a report with a print job (RT Professional)

#### Requirements

- PDF Reader is installed.
- The WinCC project is selected on the DataMonitor Server.
- The WinCC project is selected in "Scheduled print jobs in runtime".
- The DataMonitor start page is open.

#### Procedure

1. Click "Reports" in the start page. Click the "Print jobs" tab.

   The "Print Jobs Configuration" page is displayed.

   ![Procedure](images/23240071947_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23240071947_DV_resource.Stream@PNG-en-US.png)

   The icons in front of the lists "List of time-controlled print jobs" and "List of event-controlled print jobs" are cleared. The icons indicate that no reports are currently triggered.
2. Select the desired print job, such as "Report OnlineTableControl-CP" in the "Existing print jobs" field.

   You can create the report immediately via the ![Procedure](images/23239871499_DV_resource.Stream@PNG-de-DE.png) icon.
3. In "Target directory: ", select the directory in which the reports are created.

   Only the directories, for which the user that is logged in has "Create" access rights, can be selected.
4. Enter an e-mail address in the field "E-mail recipient". The report is e-mailed to this address.
5. To configure time-controlled triggering, define the following in the "Time-controlled print jobs" area.

   - Date:

     Enter the date in the field or define the date using the calendar. To open the calendar, click the "calendar" symbol.
   - Time

     Define the triggering time.
   - Repetition

     Define the repetition rate, e.g. "Once" or "Weekly".
6. Click the "Add" button in the "Time-controlled print jobs" area. The report is displayed in the "List of time-controlled print jobs".
7. To configure event-controlled triggering, define the following in the "Event-controlled print jobs" area.

   - Selected WinCC tag

     Click the ![Procedure](images/23267207435_DV_resource.Stream@PNG-de-DE.png) icon. The object list opens. Select the desired tag from the object list.
   - Define the event control

     Define the triggering event, when the tag value is changed, for example
   - Low limit and high limit

     If you selected "Only low limit", "Only high limit" or "Both limits" for event control, limits are required.
8. Click the "Add" button in the "Time-controlled print jobs" area. The report is displayed in the "List of event-controlled print jobs".

#### Result

A time-controlled or event-controlled report with print job in PDF format has been created.

Depending on the type, the report is displayed in one the "List of time-controlled print jobs" or "List of event-controlled print jobs". The report can be changed or deleted in the list.

> **Note**
>
> An event-controlled print job will not be initiated if the time, in which the tag changes, is less than one minute.
>
> Please consider that a frequent triggering of the event-controlled print job over a long time period will use a lot of memory and resources, such as the frequent signal change of a tag.
