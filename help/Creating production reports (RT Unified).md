---
title: "Creating production reports (RT Unified)"
package: ReportsWCCUenUS
topics: 101
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating production reports (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Complete workflow for using production reports (RT Unified)](#complete-workflow-for-using-production-reports-rt-unified)
- [Configuring production reports in the engineering system (RT Unified)](#configuring-production-reports-in-the-engineering-system-rt-unified)
- [Creating report templates for production reports (RT Unified)](#creating-report-templates-for-production-reports-rt-unified)
- [Working with production reports in Runtime (RT Unified)](#working-with-production-reports-in-runtime-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Basics of Reporting (RT Unified)](#basics-of-reporting-rt-unified)
- [Version compatibility (RT Unified)](#version-compatibility-rt-unified)

### Introduction (RT Unified)

#### Introduction

With WinCC Unified Reporting, you can generate tabular production reports in Runtime for the following project data:

- Logging tags and tags
- Log alarms

  Log the alarm properties of the recorded alarms and statistical calculations for display duration and frequency of the recorded alarms.
- Contexts:

  On Unified PCs, log the contexts which were running during a specific period or which project data occurred during the runtime of a specific context.

  - User-defined contexts:

    These contexts are created and executed by a program created with the ODK API.
  - System-generated contexts

    When the Performance Insight and Calendar option packages are installed, these contexts are executed by the system during Runtime.
- Audit Trail of the Runtime device
- If Plant Intelligence options are installed, you can use the WinCC Unified Local Reporting option to generate production reports for additional project data.

  You can find more information in the Help for the respective Plant Intelligence option.

The production reports can be generated as XLSX file or PDF file and sent automatically as an email to a specified group of recipients. For example, you can generate an XLSX report that outputs all alarms occurring in a production line. You then distribute or archive the report for analysis purposes.

![Introduction](images/115612377099_DV_resource.Stream@PNG-de-DE.png)

#### Functional scope in the add-in

You create the report templates in an Excel add-in. For this purpose, Reporting offers the following functions in the add-in:

- Selecting a data source:

  - Online: A connection to a Runtime server on which a Runtime project is running.
  - Offline: A configuration file that contains the data of a Runtime project
- Definition of single value segments and time series segments
- Selection of the data source items of the segments

  Possible data source items:

  - Logging tags and tags
  - Log alarms
  - Contexts
- Definition of the report period (absolute or relative)
- Creation of type-specific data source item configurations
- Execution of individual segments or all segments for test purposes

![Functional scope in the add-in](images/137734522635_DV_resource.Stream@PNG-en-US.png)

#### Functional scope in Runtime

In the "Reports" control in Runtime, you configure report jobs that use the report templates defined in the Excel add-in. To do so, Reporting offers the following functions in Runtime:

- Maintenance of the global email settings (contact data and SMTP server configuration)
- Maintenance of job parameters, especially import and export of report templates
- Creating new report jobs and managing existing report jobs
- Overview of the generated reports
- Download or deletion of the reports

---

**See also**

[Local reporting for Performance Insight (RT Unified)](Performance%20Insight%20-%20Optimizing%20processes%20with%20KPIs%20%28RT%20Unified%29.md#local-reporting-for-performance-insight-rt-unified)
  
[Local reporting for Line Coordination (LCS) (RT Unified)](Line%20Coordination%20and%20Sequence%20-%20Flexible%20handling%20of%20production%20processes%20%28RT%20Unified%29.md#local-reporting-for-line-coordination-lcs-rt-unified)

### Basics of Reporting (RT Unified)

#### Report templates

A report template is an Excel file (.xslx) that was created with the WinCC Unified Excel add-in. The report template has access to the data of the data source with which the add-in is connected.

For each report template, you define which segments are contained in the reports using the template and which data source items are evaluated by the segments.

After you have imported report templates into the "Reports" control in Runtime, you can select them for configuring report jobs.

#### Data sources

The data source is the source from which you select data source items when you configure the report template.

The following connection modes and data sources are available:

- Connection mode: Online

  The data source is the project that is running on the Runtime server to which the add-in is connected.
- Connection mode: Offline

  Data source is a configuration file. You generate the configuration file by exporting the data source items of the project to a file in the "Reports" control in Runtime. You can use this file to create additional report templates without connecting to a runtime server.

#### Options and data source items

Options control the types of data source items to which the report template has access.

Data source items are the specific objects whose data is read from the Runtime project during report generation.

The following options and types of data source items are available in Reporting, depending on the installed software:

| Software | Option | Types of data source items |
| --- | --- | --- |
| WinCC Unified basic installation | Alarms | Logging alarms  Alarm statistics for logging alarms |
| WinCC Unified basic installation | Logging tag | Logging tags |
| WinCC Unified basic installation | Tag | Tags |
| WinCC Unified basic installation | User-defined column | User-defined texts or Excel formulas |
| WinCC Unified basic installation | Context | User-defined contexts<sup>1</sup> |
| WinCC Unified basic installation | Audit | Audit |
| Performance Insight option package | Performance Insight | Local KPIs and operands of the PI option Performance Insight:  - KPIs - Logged KPIs - Operands (counters and numerical operands) - Machine states - Downtime analysis - System-generated contexts |
| Line Coordination option package | Line Coordination | Jobs |
| Calendar option package | Context | System-generated contexts |
| <sup>1</sup> Only for Unified PC |  |  |

#### Report jobs and job parameters

A report job is a job for generating reports in Runtime. A new report is generated each time the report job is performed.

The job parameters of the report order determine the details of its execution, such as which trigger it has, which report template it uses and the format of the report.

Report jobs are executed automatically when their trigger event occurs or manually by the user.

#### Reports

A report (production report) is an XLSX file or PDF file that is generated when a report job is executed in Runtime. The data source items from the Runtime project defined in the report template are read during generation, and their data are imported into a table in the report.

#### Using general Excel functions

In addition to the specific add-in functions, you also have access to the standard Excel functions in a report template. These include:

- Layout functions
- Functions for graphical preparation or analysis of the data imported from Runtime, such as charts, pivot tables and formulas

See also [Tips on design and layout](#tips-on-design-and-layout-rt-unified).

### Version compatibility (RT Unified)

#### Introduction

When loading a Runtime project for which the "Reports" control has been configured, the general rules for version compatibility of WinCC Unified apply.

The rules described here also apply for the interaction between add-in, data source, report template and runtime version of the project in which reports are generated.

#### Compatibility between add-in and data source

The add-in can use the following data sources:

| Add-in | Online data source | Offline data source |
| --- | --- | --- |
| V16 | Runtime project V16 | Configuration file generated with a Runtime project V16 |
| V17 | Runtime project V16 or V17 | Configuration file generated with a Runtime project V16 or V17 |

#### Compatibility between add-in and report template

The following report templates can be opened and edited in the add-in:

| Add-in | Report template |
| --- | --- |
| V16 | Created with a V16 add-in |
| V17 | - Created with a V17 add-in - Created with a V16 add-in   If the add-in is connected to a V17 data source when you open the report template, you will be prompted to migrate the report template to V17.    If the add-in is connected to a V16 data source when the report template is opened, no migration is necessary. |

> **Note**
>
> **Migration of report templates**
>
> The migration of the report template is not reversible. A report template migrated from V16 to V17 can no longer be opened in a V16 add-in.
>
> If migration is not desired, connect the add-in to a V16 data source before opening the report template.

> **Note**
>
> **Scope of functions of report templates**
>
> The functions available in the configuration of the report template in the add-in depend on the version of the data source used by the add-in.

#### Compatibility between report template and runtime project

In a runtime project, reports can be generated using the following report templates:

| Report template | Version of the runtime project |
| --- | --- |
| V16 | V16 and V17 |
| V17 | V17 |

---

**See also**

[Basics on version compatibility (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#basics-on-version-compatibility-rt-unified)

## Complete workflow for using production reports (RT Unified)

### Introduction

The use of reports (production reports) requires preliminary work in the Engineering System, in the Excel add-in and in Runtime. The exact workflow depends on where the report template for generating the report is used:

- Internally in the project

  A report template is based on Project A. It is used in Runtime in Project A to generate reports.
- Across projects

  A report template is based on Project A. It is used in Runtime in Project B to generate reports. Project A and Project B were downloaded into the same Runtime.

  The data source items added to the report template must be findable in both projects. Make sure that the names are consistent or that you have a uniform plant model.
- Across Runtimes

  A report template is based on Project A. It is used in Project B to generate reports. Project A and Project B were downloaded into different Runtimes.

  In this case, the following applies:

  - The data source items added to the report template must be findable in both projects. Make sure that the names are consistent or that you have a uniform plant model.
  - In both Runtimes, the same options that are used in the report template must be installed.

### Workflow for cross-project use of report templates in the same Runtime

1. In the Engineering System, configure the HMI device that serves as data source for the Excel add-in during configuration of the report templates.

   - Configure alarms and tags.
   - When reports are to evaluate context data, configure the plant model as well as other objects and settings that are necessary to start system-generated contexts.

     Example: To evaluate shift contexts of the Calendar PI option, you configure the plant model, the time model, a calendar and a calendar control.
   - Enable Reporting in the Runtime settings of the device.
2. Select one of the following options:

   - To create the report template before the HMI device goes live, start a simulation for the HMI device.

     Requirement: The engineering system and Runtime are installed on the same device.

     The device is downloaded to Runtime. Its project (project A) is started in simulation mode.
   - To create the report template during productive operation of the HMI device, load the device from the Engineering System into the Runtime and start its project (project A).
   > **Note**
   >
   > **Evaluation of context-relevant data**
   >
   > To ensure that reports generated in runtime evaluate context-relevant data, contexts must be executed in the project during runtime.
   >
   > The system-generated contexts of the PI options Performance Insight and Calendar are started automatically while a project is running in Runtime.
   >
   > You can also use the ODK API to write a program that defines, starts and stops user-defined contexts for a project.
3. (Optional) To work with an offline connection in the Excel add-in, export an offline configuration file in the "Reports" control in Runtime.
4. Start the Excel add-in and set up the data source.

   Select one of the following options:

   - Online connection: Select the Runtime server onto which you loaded the HMI device.
   - Offline connection: Load the offline configuration file created in Step 3 as the data source.
5. Configure a report template in the Excel add-in.
6. (Optional) Test a report template by running it in the Excel add-in and reading the project data into Excel.
7. In the Engineering System, configure the HMI device for which you want to generate reports in Runtime:

   - Place the "Reports" control in one of the screens of the HMI device.
   - Configure alarms, tags and the plant model if the reports are to evaluate context data.

     Make sure that this data matches the data of the HMI device from step 1.
   - Enable Reporting in the Runtime settings of the device.
   - (Optional) In the Runtime settings of the device, configure the storage location for reports and the storage location of the reporting database.
8. Load the HMI device from the engineering system into Runtime and start its project (Project B).
9. In Runtime, go to the screen with the "Reports" control.
10. (Optional) To send emails when reports are created, configure the global email settings.
11. Configure the job parameters.

    To do this, import the report template defined in step 4, among others.
12. Configure a report job that uses the report template.
13. (Optional) Perform report orders manually.
14. In the control, get an overview of which reports have been generated.
15. Download the reports, if necessary.
16. (Optional) To reuse the configuration of the "Reports" control, such as on a device in another network, transfer the existing configuration from the control from one device to the control of the other device.

---

**See also**

[Reporting (Unified Comfort Panel) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-comfort-panel-rt-unified)
  
[Reporting (Unified PC) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-pc-rt-unified)
  
[Exporting an offline configuration file (RT Unified)](#exporting-an-offline-configuration-file-rt-unified)
  
[Setting up a data source (RT Unified)](#setting-up-a-data-source-rt-unified)
  
[Workflow for configuring report templates (RT Unified)](#workflow-for-configuring-report-templates-rt-unified)
  
[Configuring production reports in the engineering system (RT Unified)](#configuring-production-reports-in-the-engineering-system-rt-unified)
  
[Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified-1)
  
[Configuring task parameters (RT Unified)](#configuring-task-parameters-rt-unified)
  
[Configuring report tasks (RT Unified)](#configuring-report-tasks-rt-unified)
  
[Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
  
[Downloading reports (RT Unified)](#downloading-reports-rt-unified)
  
[Transferring the control configuration (RT Unified)](#transferring-the-control-configuration-rt-unified)
  
[Workflow for working with reports in Runtime (RT Unified)](#workflow-for-working-with-reports-in-runtime-rt-unified)

## Configuring production reports in the engineering system (RT Unified)

This section contains information on the following topics:

- [Configuring Reporting-specific Runtime settings (RT Unified)](#configuring-reporting-specific-runtime-settings-rt-unified)
- [Inserting a "Reporting" control in a screen (RT Unified)](#inserting-a-reporting-control-in-a-screen-rt-unified)

### Configuring Reporting-specific Runtime settings (RT Unified)

#### Procedure

1. Open "Runtime settings &gt; Reporting" in the project tree below the HMI device.
2. Select the "Enable Runtime" option.

   When the option is disabled, it is not possible to use the Runtime project as data source for report templates or configure report jobs in Runtime and generate reports.
3. (Optional) Configure the storage location of the reporting database.
4. (Optional) Configure the storage location for the reports generated in Runtime.

You can find more information on configuring these storage locations for Unified Comfort Panel [here](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-comfort-panel-rt-unified), for Unified PC [here](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-pc-rt-unified).

### Inserting a "Reporting" control in a screen (RT Unified)

#### Procedure

1. Select the HMI device on the "Devices" tab.
2. Open the "Screens" folder.
3. Open the screen.
4. In the "My controls" pane, select the "Reporting" control and place it on the screen.

## Creating report templates for production reports (RT Unified)

This section contains information on the following topics:

- [Requirements (RT Unified)](#requirements-rt-unified)
- [Login (RT Unified)](#login-rt-unified)
- [Setting up a data source (RT Unified)](#setting-up-a-data-source-rt-unified)
- [Configuring report templates (RT Unified)](#configuring-report-templates-rt-unified)
- [Making general settings (RT Unified)](#making-general-settings-rt-unified)
- [Undo and redo (RT Unified)](#undo-and-redo-rt-unified)
- [Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)

### Requirements (RT Unified)

This section contains information on the following topics:

- [General requirements and restrictions (RT Unified)](#general-requirements-and-restrictions-rt-unified)
- [Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)
- [Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
- [Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
- [Adding the Reporting add-in in Excel (RT Unified)](#adding-the-reporting-add-in-in-excel-rt-unified)
- [Configuring Internet Explorer and Edge (RT Unified)](#configuring-internet-explorer-and-edge-rt-unified)

#### General requirements and restrictions (RT Unified)

The following requirements and restrictions apply to the configuration of report templates.

##### Installing the Excel add-in

The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.

If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.

Update the operating system and the Excel version if necessary.

To install the add-in with a local Excel installation, MS Excel with build 16.0.6769 or higher is required.

> **Note**
>
> **Note the Microsoft upgrade restrictions**
>
> If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.

##### IIS settings for standalone installation of the Excel Add-In

To install the Excel Add-In on a PC without Unified Runtime, the same IIS (Internet Information Services) settings must be active in Windows that are required to install WinCC Unified Runtime on a PC.

You can find additional information in the "SIMATIC Unified PC Installation" user help section on the software and hardware requirements.

##### Enable Reporting

The Runtime project that is the data source of a report template must have reporting functionality enabled.

You activate the reporting functionality of a Runtime project before loading it into the device in TIA Portal: "Runtime settings" of the HMI device &gt; "Reporting" &gt; "Enable Reporting" option

> **Note**
>
> **Devices with a device version lower than V18**
>
> Reporting is always enabled for HMI devices with a device version lower than V18.

##### Unified Comfort Panel

Contexts are not supported for Unified Comfort Panel. This option is not available in a report template with a Unified Comfort Panel as data source.

---

**See also**

[Version compatibility (RT Unified)](#version-compatibility-rt-unified)
  
[Reporting (Unified PC) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-pc-rt-unified)
  
[Reporting (Unified Comfort Panel) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-comfort-panel-rt-unified)

#### Installation of the Reporting add-in (RT Unified)

> **Note**
>
> **Regular updates of operating system and MS Excel**
>
> The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.
>
> If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.
>
> Update the operating system and the Excel version if necessary.
>
> To install the add-in with a local Excel installation, MS Excel with build 16.0.6769 or higher is required.

> **Note**
>
> **Note the Microsoft upgrade restrictions**
>
> If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.

##### Procedure

1. Install the Excel manifest on the computer.
2. Set up read access to the installation path of the Excel manifest.
3. Add the add-in to Excel.

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
  
[Adding the Reporting add-in in Excel (RT Unified)](#adding-the-reporting-add-in-in-excel-rt-unified)
  
[MS help for autoloop](https://docs.microsoft.com/en-us/office/troubleshoot/error-messages/cannot-open-add-in-from-localhost)

#### Installing the Excel manifest (RT Unified)

##### Procedure

1. In the installation package of WinCC Unified on "DVD_2", double-click the file "Support\Reporting\SIMATIC_WinCC_Unified_Reporting_&lt;Version number&gt;.exe".
2. Select the target directory to which the underlying ZIP file is extracted and confirm your input.

   The ZIP file is extracted and setup starts automatically.
3. Follow the setup instructions.
4. In the "Configuration" step, select the option for the Excel add-in.
5. Click "Next" and follow the setup instructions.

**Note**

**Start setup manually**

To start the setup manually after the file was extracted, select the option "Extract the setup files without being installed".

Start the setup later by running the "Setup.exe" file as administrator in the target directory.

---

**See also**

[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

#### Setting up read access to the Excel manifest (RT Unified)

##### Requirement

The Excel manifest is installed.

##### Procedure

Give the users that create templates with the Excel add-in read access to the installation path of the Excel manifest: &lt;target directory&gt;\WinCCUnifiedReporting\Excelmanifest

> **Note**
>
> This step is also necessary if the user belongs to a group in the user management with general read permission.

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

#### Adding the Reporting add-in in Excel (RT Unified)

##### Requirement

- The Excel manifest is installed on the PC.
- Read access to the installation path of the Excel manifest is set up.
- The following software is available on the computer:

  - Local Excel

    MS Excel (Build 16.0.6769 or higher)

    > **Note**
    >
    > **Regular updates of operating system and MS Excel**
    >
    > The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.
    >
    > If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.
    >
    > Update the operating system and the Excel version if necessary.

    > **Note**
    >
    > **Note the Microsoft upgrade restrictions**
    >
    > If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.
  - Or Office online

##### Procedure

1. Open Microsoft Excel.
2. Open the "Trust Center" under "File" &gt; "Options".
3. Click "Trust Center Settings".
4. Click "Catalogs of trusted add-ins".
5. Add the catalog using the URL "\\&lt;Computer name&gt;\Excelmanifest".

   ![Procedure](images/142754073355_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142754073355_DV_resource.Stream@PNG-en-US.png)
6. Make sure that the check mark in the "Show in Menu" column is set.
7. End and restart Excel.
8. In the "Insert" menu, click "My Add-ins".

   ![Procedure](images/142759971979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142759971979_DV_resource.Stream@PNG-en-US.png)

   In the "Office Add-ins" dialog box, the Siemens add-in is displayed under "Shared folders".
9. Select the add-in and click "Add".

   ![Procedure](images/142760213003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142760213003_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
  
[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

#### Configuring Internet Explorer and Edge (RT Unified)

The Reporting Excel add-in uses the certificate that was selected during installation of WinCC Unified Runtime or later in "WinCC Unified Configuration".

Some browsers do not consider self-signed certificates as trusted. If you use a self-signed certificate for WinCC Unified Runtime, you must add the certificate to the list of trusted certificates in Internet Explorer or Edge on the device on which the Excel add-in is installed.

For detailed information on handling certificates, see the Runtime Readme.

##### Procedure

The following section describes the procedure for adding a self-signed certificate to the list of trusted certificates, using Internet Explorer as an example:

1. Start Internet Explorer.
2. In the address line, enter the host name or the IP when creating the certificate.

   You will receive a security warning.
3. Click "Continue to this website (not recommended)".
4. Click "Install certificate".
5. Click "Place all certificates in the following store" and "Browse".
6. Click "Trusted Root Certification Authorities" followed by "OK".
7. Exit the dialog.
8. If you receive a security warning as to whether you want to trust the certificate, confirm it with "Yes".
9. Load the page again.

**Note**

Do not use the preset options for automatic selection of the certificate store.

---

**See also**

[MicrosoftHelp_IE_ZertifikatInstallieren](https://medium.com/@ali.dev/how-to-trust-any-self-signed-ssl-certificate-in-ie11-and-edge-fa7b416cac68)

### Login (RT Unified)

A login dialog opens in the Excel add-in in the following cases:

- After start of Excel and the add-in
- When using an online connection: When the connection to the Runtime server must be re-established.

  Examples:

  - Runtime has been reloaded.
  - The security token has expired due to a timeout.

#### Requirement

- The add-in is installed.
- When using an online connection:

  - A Runtime server is accessible.
  - A Runtime project is running on the server for which reporting is enabled.

#### Procedure

In order to use an online connection, log onto a Runtime server:

1. Under "Server", enter the device name or FQDN (Fully qualified domain name) or the IP address of the server on which the project is running that is to serve as the data source for the report template:

   - If the device name/FQDN is used to address the Runtime web page, use Device Name/FQDN.
   - If IP address is used for addressing, enter the IP address.
2. Enter the user name and password of a user that is registered on the server in the Runtime user management.
3. Click "Login".

**Note**

If Runtime is installed on the same computer as the add-in, it is not allowed to enter the string "localhost" under "Server" to register the add-in.

In order to use an offline connection, click "Go offline".

#### Result

**Online connection**

The add-in is connected to the Runtime server and the options available there are loaded.

You can now create report templates.

**Offline connection**

Before you create report templates, set up the offline connection.

---

**See also**

[Setting up an offline connection (RT Unified)](#setting-up-an-offline-connection-rt-unified)
  
[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

### Setting up a data source (RT Unified)

This section contains information on the following topics:

- [Using an online connection (RT Unified)](#using-an-online-connection-rt-unified)
- [Using an offline connection (RT Unified)](#using-an-offline-connection-rt-unified)

#### Using an online connection (RT Unified)

This section contains information on the following topics:

- [Introduction to online connection (RT Unified)](#introduction-to-online-connection-rt-unified)
- [Setting up an online connection (RT Unified)](#setting-up-an-online-connection-rt-unified)
- [Removing options (RT Unified)](#removing-options-rt-unified)

##### Introduction to online connection (RT Unified)

When an online connection is present, the add-in establishes a connection to a Runtime server. The project running on the server serves as data source for the add-in.

The connection settings allow you to:

- Change the connected Runtime server to another Runtime server
- When a report template that was created with a different Runtime server than the currently connected server is reused: check the options available on the server and delete the options that were not loaded

##### Setting up an online connection (RT Unified)

###### Requirements

- A Runtime server is accessible.
- A Runtime project is running on the server.

###### Procedure

1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections".
2. Click "Online" under "Connections" in the add-in.
3. Under "Server", enter the server name.

   Use the same spelling as when the Runtime server certificate was created.
4. Click "Load".

**Note**

If Runtime is installed on the same computer as the add-in, use of the name "localhost" is not permitted.

###### Result

- A server node is created.
- The add-in is connected to the Runtime server and its options are loaded.

  Data source items of these options can be added to report templates. Their data can be read in from Runtime to Excel.

  > **Note**
  >
  > To check which options were loaded, click on the server node.
  >
  > Options that are being used in the currently open report template but are not available on the connected server have a red icon. You can remove the option:
- If no connection can be established or an incorrect server name has been entered, the add-in will display a corresponding error message.

---

**See also**

[Removing options (RT Unified)](#removing-options-rt-unified)

##### Removing options (RT Unified)

###### Introduction

If you reuse report templates across servers, e.g. in order to adapt an existing template for another project, it may be necessary to remove unavailable options from the connection settings.

The procedure for this is presented using the Performance Insight option as an example.

###### Requirement

- The add-in was connected to a server on which the Performance Insight (PI) option is installed.
- A report template that uses KPIs was created with the add-in.
- The add-in was then connected to a server without the Performance Insight option installed for the purpose of adapting the template to the project running there.

###### Removing an option

| Symbol | Meaning |
| --- | --- |
| 1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections". 2. Under "Connections", click on "Online". 3. Select the server node.    You see the loaded options under the server node:       | Symbol | Meaning |    | --- | --- |    | ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png) | Available options  The following applies to data source items of these options: - They can be added to the report template. - Their data can be read in from Runtime to Excel in the add-in. |    | ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png) | Unavailable options In the example: Performance Insight  The following applies to data source items of these options: - They cannot be added to the report template. - If the report template already has a data source element of this option, its data cannot be read in from Runtime to Excel. | 4. Select the "Performance Insight" option under the server node. 5. Click the "Delete" button next to the option. 6. Confirm your input. |  |

###### Result

The option is removed from the connection settings.

Next, remove all data source items of this option from the report template.

###### Reloading an option

When the add-in is connected to a Runtime server, all options available on the server are loaded.

To reload an option that was deleted in the connection settings but is available on the server, select the server node and click "Load".

#### Using an offline connection (RT Unified)

This section contains information on the following topics:

- [Introduction to offline connection (RT Unified)](#introduction-to-offline-connection-rt-unified)
- [Setting up an offline connection (RT Unified)](#setting-up-an-offline-connection-rt-unified)
- [Removing options (RT Unified)](#removing-options-rt-unified-1)

##### Introduction to offline connection (RT Unified)

With the offline connection, the add-in uses a configuration file as data source.

The connection settings allow you to:

- Change the configuration file used
- When reusing a report template with a configuration based on a Runtime server different to that of the currently selected configuration file: Check the available options and delete the options that were not loaded.

##### Setting up an offline connection (RT Unified)

###### Requirement

An offline configuration file was created in the "Reports" control in Runtime. The configuration file is available on the device.

###### Procedure

1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections".
2. Under "Connections", click on "Offline".
3. Click "Open offline configuration".
4. Select the desired file in the window that opens and confirm your entries.
5. Click "Load".
6. Select the desired options.
7. Confirm your entries.

###### Result

- A server node is created. The node bears the name of the server on which the configuration file is based.
- The configuration file, together with its options, is loaded into the add-in. The data of the configuration file is available for configuring the report template.

  > **Note**
  >
  > To check which options were loaded, click on the server node.
  >
  > Options that are being used in the currently open report template but are not available in the configuration file have a red icon. You can remove the option:

---

**See also**

[Removing options (RT Unified)](#removing-options-rt-unified-1)
  
[Exporting an offline configuration file (RT Unified)](#exporting-an-offline-configuration-file-rt-unified)

##### Removing options (RT Unified)

###### Introduction

If you reuse report templates across servers, e.g. in order to adapt an existing template for another project, it may be necessary to remove unavailable options from the connection settings.

The procedure for this is presented using the Performance Insight option as an example.

###### Requirement

- The add-in was changed over to an offline connection whose configuration file does not include Performance Insight.
- A report template was opened in the add-in whose configuration is based on a connection to a Runtime server on which Performance Insight is installed.

###### Removing an option

| Symbol | Meaning |
| --- | --- |
| 1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections". 2. Under "Connections", click on "Offline". 3. Select the server node.    You see the loaded options under the server node:       | Symbol | Meaning |    | --- | --- |    | ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png) | Available options  The following applies to data source items of these options: - They can be added to report templates. - Their data can be read in from the configuration file to Excel. |    | ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png) | Unavailable options In the example: Performance Insight  The following applies to data source items of these options: - They cannot be added to the report template. - If the report template already has a data source element of this option, its data cannot be read in from the configuration file to Excel. | 4. Select the "Performance Insight" option under the server node. 5. Click the "Delete" button next to the option. 6. Confirm your input. |  |

###### Result

The option is removed from the connection settings.

Next, remove all data source items of this option from the report template.

###### Reloading an option

When a configuration file is loaded, all options available in the file are loaded.

To reload an option that was deleted in the connection settings but is available in the configuration file, select the server node and click "Load".

### Configuring report templates (RT Unified)

This section contains information on the following topics:

- [Workflow for configuring report templates (RT Unified)](#workflow-for-configuring-report-templates-rt-unified)
- [User interface of the add-in (RT Unified)](#user-interface-of-the-add-in-rt-unified)
- [Working with segments (RT Unified)](#working-with-segments-rt-unified)
- [Adding data source elements (RT Unified)](#adding-data-source-elements-rt-unified)
- [Setting a display name for standard column (RT Unified)](#setting-a-display-name-for-standard-column-rt-unified)
- [Delete data source elements (RT Unified)](#delete-data-source-elements-rt-unified)
- [Working with configurations (RT Unified)](#working-with-configurations-rt-unified)
- [Changing the column sequence (RT Unified)](#changing-the-column-sequence-rt-unified)
- [Reading Runtime data in Excel (RT Unified)](#reading-runtime-data-in-excel-rt-unified)
- [Calculation modes for data source elements (RT Unified)](#calculation-modes-for-data-source-elements-rt-unified)

#### Workflow for configuring report templates (RT Unified)

##### Requirement

An online connection or offline connection has been established.

##### Procedure

To create a new report template, proceed as follows:

1. Open a new Excel file.
2. Add a segment.

   You can choose between time series segments and single value segments.
3. Add data source items to the segment.

   The exact procedure depends on the type of the data source item.
4. Optional: If you do not want a data source item to use the default configuration, determine its configuration.

   You have the following options:

   - Select an existing configuration.
   - Create a new configuration and select it.
   - Define a local configuration.
5. Optional: To define additional segments, repeat steps 2 to 4.
6. Optional: When using an online connection, test the template by reading the runtime data of selected segments or all segments.

#### User interface of the add-in (RT Unified)

##### Requirement

- The "WinCC Unified" tab is visible in Excel.

##### Structure

If you click on "Segments" in the "Configuration" group, you see the following interface:

![Structure](images/142022624523_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Work area |

Toolbar buttons:

| Button | Tooltip | Description |
| --- | --- | --- |
| ![Structure](images/142025031051_DV_resource.Stream@PNG-de-DE.png) | "Segment configuration" | Loads the interface to add and edit segments in the work area. |
| ![Structure](images/142024796299_DV_resource.Stream@PNG-de-DE.png) | "Data source item configuration" | Loads the interface for adding and editing the configuration of a data source item in the work area. |
| ![Structure](images/142024587787_DV_resource.Stream@PNG-de-DE.png) | "Basic settings" | Loads the interface for setting the language settings in the work area. |
| ![Structure](images/142023530251_DV_resource.Stream@PNG-de-DE.png) | "Update all" | Reads the Runtime data of the connected data source into the data tables of the segments. |
| ![Structure](images/142024787723_DV_resource.Stream@PNG-de-DE.png) | "Delete Runtime data" | Removes all Runtime data from the report template. |
| ![Structure](images/142024907275_DV_resource.Stream@PNG-de-DE.png) | Logoff | Logs out the user currently logged in to the add-in. |
| ![Structure](images/142025039627_DV_resource.Stream@PNG-de-DE.png) | Help | Opens the user help for the add-in. |

#### Working with segments (RT Unified)

This section contains information on the following topics:

- [Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)
- [Standard column (RT Unified)](#standard-column-rt-unified)
- [The segment user interface (RT Unified)](#the-segment-user-interface-rt-unified)
- [Create segments (RT Unified)](#create-segments-rt-unified)
- [Formats for relative time information (RT Unified)](#formats-for-relative-time-information-rt-unified)
- [Edit segments (RT Unified)](#edit-segments-rt-unified)
- [Delete segments (RT Unified)](#delete-segments-rt-unified)

##### Basic information on segments (RT Unified)

###### Definition

A report template consists of any number of segments. Each segment is a container to which you can add any number of data source items. The segment reads the data from its data source items.

There are time series segments and single value segments.

> **Note**
>
> **Hierarchical segments of PI options**
>
> Hierarchical segments are also available with PI Options installed. For more information on this, refer to the PI Options help.

###### Time series segments

A time series segment documents the data of its data source items in a defined time period.

It has a legend table and a data table.

**Data source items**

Time series segments can have the following data source items:

- Logging alarms
- Alarm statistics
- Logging tags
- User-defined columns
- Contexts
- Audit

> **Note**
>
> **Data source items of the PI options**
>
> If PI options are installed, additional data source items can be added. For more information on this, refer to the PI Options help.

**Legend table**

The table header row provides general information about the segment and its data source items.

You decide which type of information is provided when you create or edit the segment.

**Data table**

The data table outputs the data of the data source items. It documents how the data source items have changed in the defined time period.

The data table of a time series segment has the following columns:

| Columns |  | Description |
| --- | --- | --- |
| Time stamp column |  | Always output  Always output as the first column |
| Per data source item | Standard column | The standard column provides the standard property of the data source item. This property depends on the type of data source item.  For a data source item of the Tag type, e.g. the tag value |
| Optional columns | Provide more information about the data source item. What information this is depends on the type of the data source item.  For a data source item of the Tag type, e.g. the quality code of the tag value  You change the default settings for visibility, column title and order of these columns in the configuration of the data source item. |  |

In the default setting, the data source items in the data table have the order in which they were added to the segment.

> **Note**
>
> When the standard columns and optional columns provide numerical values, you can have the actual values replaced with texts or graphics from a text list or graphic list when importing the Runtime data.

###### Single value segments

A single value segment documents exactly one value for its data source items.

**Data source items**

Single value segments can have the following data source items:

- Logging tags
- Tags

> **Note**
>
> **Data source items of the PI options**
>
> If PI options are installed, additional data source items can be added. For more information on this, refer to the PI Options help.

**Data table**

The data table of a single value segment has the following columns per data source item:

| Columns | Description |
| --- | --- |
| Standard column | The standard column provides the standard property of the data source item.   For tags and logging tags: the tag value |
| Optional columns | Provide more information about the data source item.  For tags and logging tags:   - Time stamp - Data source item - Quality code of the tag value   You change the default settings for the visibility of these columns in the configuration of the data source item. |

The data table of a single value segment shows the data source items in the order in which they were added to the segment.

> **Note**
>
> When the standard columns and optional columns provide numerical values, you can have the actual values replaced with texts or graphics from a text list or graphic list when importing the Runtime data.

Single row segments do not have a table header row. However, in the configurations of their data source items, you can determine whether a caption is inserted for the displayed columns and the position at which this occurs.

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)

##### Standard column (RT Unified)

###### Introduction

For each data source item of a segment, a standard column is added in the data table of the segment.

###### Content of the standard column

The standard column provides the standard property of the data source item and depends on the type of the data source item:

| Data source item type | Default column title | Value |
| --- | --- | --- |
| Logging alarm | "Alarm ID" | Alarm IDs of the displayed alarms |
| Alarm statistics | "Alarm statistics [ID]" | Alarm IDs of the alarms displayed in the alarm statistics |
| Tag or logging tag | "&lt;Name of the tags or logging tags&gt;" | Value of the tag or logging tag |
| Context | "&lt;Name of the context object&gt;" | Context name |
| Audit | "Audit [&lt;object name&gt;]" | The name of the object monitored by the Audit Trail |
| User-defined column | Name entered when creating the data source item | As set in the configuration of the data source item:  - A fixed string.  Or - A dynamically calculated string |

###### Changing the column title

You can replace the default column title with a localizable display name. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Replacing numerical values

If the standard column provides numeric values, you have the option to have the actual values replaced with texts or graphics from a text list or graphic list when the Runtime data is read in. See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

User-defined columns are excluded from this.

---

**See also**

[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)

##### The segment user interface (RT Unified)

###### Structure

The interface for creating and editing segments has the following structure:

![Structure](images/143835346443_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Filter  Filters the list of segments by name. |
| ② | Button for creating a segment |
| ③ | List of segments  Each segment has buttons for reading in, editing and deleting the segment.  The following configuration is displayed for each segment:  - Segment name - Number of data source items - Insertion location of the segment in the Excel file - Time span - If context filters have been configured: The filter string   A click on the segment opens the area with the data source items. |

##### Create segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- The data source is set up.
- To filter the time interval of the time series segment depending on the context: There are contexts in the project that run on the connected Runtime server or are the basis of the configuration file.

###### Procedure

|  |  |  |
| --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group. 2. Click "New segment". 3. Select "New time series segment" or "New single value segment". 4. Enter a segment name.       |  |  |  |    | --- | --- | --- |    | **Note**  Note the Excel restrictions for naming tables (for example, do not use blanks). Change the segment name only via the add-in, not via the Excel property "Table name". Do not change the name of the worksheet after creating the segment. The add-in addresses the segment by the segment name and the worksheet name. |  |  | 5. For a time series segment, make the following settings in addition:     - Under "File location" you determine where the segment will be inserted in the file. Enter the name of the worksheet and the cell.      Alternatively, click "Select a cell" and use the cell currently selected in the Excel file:                 ![Procedure](images/129293998859_DV_resource.Stream@PNG-de-DE.png)           ![Procedure](images/129293998859_DV_resource.Stream@PNG-de-DE.png)    - Under "Start" and "End", you determine the time period for which values are read into the segment.          |  |  |  |      | --- | --- | --- |      | ![Procedure](images/129294283275_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129294283275_DV_resource.Stream@PNG-de-DE.png) | "Absolute date/time" | Select a date and a time. The information is absolute to the current date. |      | ![Procedure](images/129293991435_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129293991435_DV_resource.Stream@PNG-de-DE.png) | "Relative date/time" | Select a reference time and a time interval. The information is relative to the current date. See also [Formats for relative time information](#formats-for-relative-time-information-rt-unified). |      | ![Procedure](images/129293995147_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129293995147_DV_resource.Stream@PNG-de-DE.png) | "Date/Time of the cell" | Applies the value of the cell currently highlighted in the Excel file. Make sure that the cell supplies a valid time. |      | ![Procedure](images/129294850187_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129294850187_DV_resource.Stream@PNG-de-DE.png) | "Date/Time of the tag" | Applies the value of the set tag. Make sure that the tag supplies a valid time. Possible data types:  - DateTime - String - Integer |    - (Optional) Under "Properties of the legend table", you configure the contents to be displayed in the table header row of the segment:         |  |  |  |      | --- | --- | --- |      | "Name" "Start" "End" "State" | General information on the segment |  |      | "Context filter" | If the segment time was limited by a context filter: The filter string is output. See step 6. |  |      | "Audit status" | If the segment has an audit data source item, the field shows the overall status of the audit data: - Green field: No manipulations of the Audit Trail were found in the queried time range. - Red field: Manipulations of the Audit Trail were found in the queried time range. Single or multiple entries have been deleted, added or changed. |  |      | "Header" | The table header row includes a list of the segment's data source items showing general information about these data source items. The information displayed for the data source items depends on their type. Example of contexts: Display name of the context, context provider, hierarchy path, short name of the context, full name of the context, option |  |       Use the check boxes to remove information from or add information to the legend table.      To change the sorting in the table header row, move the mouse pointer to a row and shift it using the arrow buttons or drag-and-drop. 6. (Optional) You can filter the time interval of the time series segment depending on the context. You can define up to two filter conditions.    Proceed as follows:    - Under "Context filter", click "+" or "Add new condition row".       The condition line is added.    - Click on "+" in the condition line.    - Under "Select context", select the root of the common plant model.       In the next row, you see the top level of the common plant model.    - Navigate through the common plant model to plant objects with contexts.      Plant objects and contexts can be recognized by the following icons:         |  |  |  |      | --- | --- | --- |      | ![Procedure](images/133490847499_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/133490847499_DV_resource.Stream@PNG-de-DE.png) | Plant object |  |      | ![Procedure](images/133490838923_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/133490838923_DV_resource.Stream@PNG-de-DE.png) | Context |  |    - Select a context.    - Select an operator.    - Enter a value.    - (Optional) Use "+" or "Add new condition row" to create a second condition and select whether the two conditions are to be linked with a logical AND or OR. 7. (Optional) Under "Autofit", configure whether the column width and row height of the data table is automatically adapted to the text read from Runtime. 8. Confirm your entries with "OK". |  |  |

###### Result

The segment is created and added to the list of segments:

Next, add data source items to the segment. Your procedure depends on the type of the new data source item.

---

**See also**

[Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)
  
[Adding data source elements (RT Unified)](#adding-data-source-elements-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Formats for relative time information (RT Unified)

###### Definition of a relative time information

The relative times are entered using a reference time and a time interval.

![Definition of a relative time information](images/129297375883_DV_resource.Stream@PNG-de-DE.png)

###### Reference time

Use one of the following characters for the reference time:

- "*" - Now
- "t" (today) - Today at midnight
- "y" (yesterday) - Yesterday at midnight
- "1-31" - Specific day of the current month

###### Time interval

- "y" (year): +1y = plus 1 year
- "mo" (month): +1mo = plus 1 month
- "w" (week): +1w = plus 1 week
- "d" (day): +1d = plus 1 day
- "h" (hour): +1h = plus 1 hour
- "m" (minute): +1m = plus 1 minute
- "s" (second): +1s = plus 1 second
- "ms" (milliseconds): +250ms = plus 250 milliseconds

###### Examples

- *-1y: One year ago today
- t+8h: Today at 8:00 am
- y+8h: Yesterday at 8:00 am
- 1+8h: The first day of the current month at 8:00 am
- *-1d: One day ago
- *-2h-30m-30s: 2 hours, 30 minutes and 30 seconds ago

---

**See also**

[Create segments (RT Unified)](#create-segments-rt-unified)

##### Edit segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Edit" next to a segment in the list of segments.
3. Edit the segment.

   You can make the same settings as when creating the segment.

##### Delete segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Delete" next to a segment in the list of segments.
3. Confirm your entries with "OK".

#### Adding data source elements (RT Unified)

This section contains information on the following topics:

- [Adding log alarms (RT Unified)](#adding-log-alarms-rt-unified)
- [Adding alarm statistics (RT Unified)](#adding-alarm-statistics-rt-unified)
- [Add logging tags (RT Unified)](#add-logging-tags-rt-unified)
- [Adding tags (RT Unified)](#adding-tags-rt-unified)
- [Adding contexts (RT Unified)](#adding-contexts-rt-unified)
- [Adding user-defined columns (RT Unified)](#adding-user-defined-columns-rt-unified)
- [Add Audit (RT Unified)](#add-audit-rt-unified)

##### Adding log alarms (RT Unified)

###### Requirement

- There are logging alarms in the project that runs on the connected Runtime server or is the basis of the configuration file.
- The "Alarm" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Adding logging alarms

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded into the add-in.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Alarms" option.
5. Select the "Alarm" entry under "Select alarms".
6. Under "Select alarms", select the entry "Alarm [ID]".
7. To cancel your selection, select the entry "Alarm [ID]" under "Selected data source items" and click "Delete".
8. Confirm with "OK".

**Note**

**Change selection criteria**

After you have added alarms, you can change the selection criteria and add more data source items to the segment.

For example: Output tags and alarms in the same segment.

###### Result

- The data source item for logging alarms is added to the add-in below the segment.
- The configuration of the data source item controls which data is added when importing the runtime data into the data table.

  > **Note**
  >
  > With the default setting, the data source item uses the default configuration. It shows all logging alarms of the project.

To display data that deviates from the default configuration, select one of the following options:

- Select a different matching configuration.
- Create your own configuration.
- Edit a configuration.
- Overwrite a configuration locally.

---

**See also**

[Creating or editing configurations for log alarms (RT Unified)](#creating-or-editing-configurations-for-log-alarms-rt-unified)
  
[Select configuration (RT Unified)](#select-configuration-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Adding alarm statistics (RT Unified)

###### Introduction

To output statistical calculations for logging alarms in a report, add alarm statistics to a report template. The following calculations are available:

- Frequency of an alarm
- Average display time per state machine
- Total display time per state machine
- Maximum display time per state machine
- Minimum display time per state machine

The alarm statistics add columns with statistical calculations and columns with general alarm properties of the recorded alarms to the reports.

You can find more information about calculations in alarm statistics in the help for the alarm control.

###### Requirement

- The "Alarm" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded.
2. Select a time series segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Alarm" option.
5. Under "Select alarms", select the entry "Alarm statistic [ID]".
6. Under "Select alarm statistic" select the entry "Alarm statistic [ID]".
7. (Optional) To cancel your selection, select the entry "Alarm statistic [ID]" under "Selected data source items" and click "Delete".
8. Confirm with "OK".

**Note**

**Change selection criteria**

After adding the alarm statistics, you can change the selection criteria and add more data source items.

###### Result

The added data source item for alarm statistics is displayed below the segment and inserted into the data table.

First, the data table shows the contents configured in the default configuration for alarm statistics. To output other contents, select or create a configuration.

---

**See also**

[Creating or editing configurations for an alarm statistics (RT Unified)](#creating-or-editing-configurations-for-an-alarm-statistics-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Add logging tags (RT Unified)

###### Requirement

- The project on which the connected Runtime server runs or the basis of the configuration file has logging tags.
- The "Logging tag" option was selected while setting up of the connection.
- The "WinCC Unified" tab is visible in Excel.
- A single value segment or time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Logging tag" option.
5. Optional: To reduce the load time, filter which tags are loaded to the selection under "Add filter".

   The preset filters "*" return all logging tags of the project.

   - "Tag name": Enter the name of the tag whose logging tags you want to add.
   - "Logging tag name": Enter the name of the logging tags you want to add.

   Note that the entry is case-sensitive.
6. Click "Load".

   The logging tags of the project are filtered and provided under "Select tags".
7. Optional: Further reduce the number of tags that are offered for selection by clicking next to "Select logging tags" and entering another filter string.

   The list of tags you are being offered is filtered while you type.
8. Select one or more tags under "Select logging tags".

   The tags are added to the "Selected data source items" list.
9. To remove one or more data source items from "Selected data source items", select them and click "Delete".
10. Confirm with "OK".

    The added logging tags are shown below the segment and added to the Excel table.
11. If you have added the logging tag to a single value segment:

    - In the Excel worksheet, select the cell in which the logging tag is to be inserted.
    - Click the "Select a cell" button on the data source item of the logging tag.

      Alternatively, enter the name of the worksheet and the cell.

**Note**

**Filter by partial string**

You use the wildcard "*" to filter by partial strings.

For example:

- *T* returns all tags with a "T" in their name.
- *T returns all tags that end in "T".
- T* returns all tags that start with "T".

When filtering for structures, the separators must be part of the filter string.

For example: The following filters return the logging tags for all tags of the device "HMI_RT_1":

- Filter for tag: "HMI_RT_1::*"
- Filter for logging tag: "*"

**Note**

**Change selection criteria**

After you have added a tag, you can select a different option or a different filter and add additional data source items.

For example: Output KPIs and logging tags in the same segment.

---

**See also**

[Create segments (RT Unified)](#create-segments-rt-unified)
  
[Select configuration (RT Unified)](#select-configuration-rt-unified)
  
[Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Adding tags (RT Unified)

###### Requirement

- The project on which the connected Runtime server runs or the basis of the configuration file has tags.
- The "Tag" option was enabled when the connection was set up.
- The "WinCC Unified" tab is visible in Excel.
- A single value segment is available.

###### Procedure

|  |  |  |
| --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group.    The list of segments is loaded. 2. Select the single value segment.    The segment is extended by the area for the data source items. 3. Click "+". 4. Select the "Tag" option. 5. Optional: To reduce the load time, filter which tags are loaded to the selection under "Add filter".    Under "Tag name", enter a filter, e.g. the name of the tag. Note that the entry is case-sensitive.    The default filter "*" returns all tags of the project.      |  |  |  |    | --- | --- | --- |    | **Note**  **Filter by partial string** You use the wildcard "*" to filter by partial strings. For example: - *T* returns all tags with a "T" in their name. - *T returns all tags that end in "T". - T* returns all tags that start with "T".When filtering for structures, the separators must be part of the filter string. For example: The filter "HMI_RT_1::*" returns all tags of the device "HMI_RT_1". |  |  | 6. Click "Load".    The tags of the project are filtered and provided under "Select tags".    You can recognize structs and arrays in the list by the following items:                ![Procedure](images/142101483915_DV_resource.Stream@PNG-de-DE.png)         ![Procedure](images/142101483915_DV_resource.Stream@PNG-de-DE.png)        |  |  |  |    | --- | --- | --- |    | ① | Button to display the members of the struct or array |  |    | ② | "Select all included data source items" Button that adds all members with a simple data type to the list of selected data source items |  | 7. Optional: Further reduce the number of tags that are offered for selection by clicking next to "Select tags" and entering another filter string.               ![Procedure](images/142126586763_DV_resource.Stream@PNG-en-US.png)         ![Procedure](images/142126586763_DV_resource.Stream@PNG-en-US.png)      The list of tags you are being offered is filtered while you type. 8. Select which tags will be added to the segment. You have the following options:       | Target | Procedure | Result |    | --- | --- | --- |    | Show the members of a struct or array. | Click the button with the arrow next to the struct or array. | A second "Select tags" list is added, in which you can see all the members of the struct or array. You can add to the segment any members that have a simple data type, e.g. bool, float or string. |    | Add all members of a struct or array. | Next to the struct or array, click "Select all included data source items". | All members with a simple data type are added to the "Selected data source items" list and marked as selected under "Select tags": |    | Select tags with simple data type. | Under "Select tag", click the required tags. | The tags are added to the "Selected data source items" list and marked as selected under "Select tags":            ![Procedure](images/142128090763_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/142128090763_DV_resource.Stream@PNG-de-DE.png) |       |  |  |  |    | --- | --- | --- |    | **Note**  **Automatic filtering when displaying the members or selection of all members**  If you click the button to display the members of a struct or array or activate the option to select their members, the struct or array is set as a filter: - The list under "Select tags" only shows the struct or array. - A second "Select tags" list is added below this, in which you can see all members of the struct or array.To see all available tags again, delete the filters. |  |  |     |  |  |  |    | --- | --- | --- |    | **Note**  **Change selection criteria** After you have added a tag, you can select a different option or a different filter and add additional data source items. |  |  | 9. To remove tags from the segment, click on the tags in "Selected data source items" and click "Delete". 10. Confirm with "OK". |  |  |

The added tags are added to the segment.

When the report template is updated in the add-in and when the report is generated in runtime, the tag values are inserted into the data table.

---

**See also**

[Creating or editing configurations for tags: (RT Unified)](#creating-or-editing-configurations-for-tags-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Adding contexts (RT Unified)

###### Introduction

To display in a report which contexts are to run during a certain time period, add only contexts to a segment in the report template.

To display which process data has been accumulated during the runtimes of a context, add the context and other data source items, such as logging tags or logging alarms, to the segment.

###### Requirement

- There are contexts in the project that run on the connected Runtime server or are the basis of the configuration file.
- The "Context" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Adding a context to a segment

| Symbol | Meaning |
| --- | --- |
| 1. Click on "Segments" in the "Configuration" group.    The list with the segments already created is loaded. 2. Select a segment.    The segment is extended by the area for the data source items. 3. Click "+". 4. Select the "Context" option. 5. Select a context:    - Under "Select a context definition", select the root of the plant model.       In the next row, you see the top level of the common plant model.    - Navigate through the common plant model to plant objects with contexts.      Plant objects and contexts can be recognized by the following icons:         | Symbol | Meaning |      | --- | --- |      | ![Adding a context to a segment](images/133490847499_DV_resource.Stream@PNG-de-DE.png)      ![Adding a context to a segment](images/133490847499_DV_resource.Stream@PNG-de-DE.png) | Plant object |      | ![Adding a context to a segment](images/133490838923_DV_resource.Stream@PNG-de-DE.png)      ![Adding a context to a segment](images/133490838923_DV_resource.Stream@PNG-de-DE.png) | Context |    - Select the desired contexts.      All selected contexts are included in the "Selected data source items" list     | Symbol | Meaning |    | --- | --- |    | **Note**  **Change selection criteria** After you have added a context, you can select a different option and add additional data source items. For example: Context and logging tags in the same segment. |  | 6. To remove one or more data source items from "Selected data source items", select them and click "Delete". 7. Confirm with "OK". |  |

###### Result

The selected contexts are displayed below the segment and inserted into the data table.

If you do not want a context to use the default configuration, select its configuration next.

**Content of the data table after executing the segment**

In segments to which only contexts or contexts and user-defined columns have been added:

- A line is inserted for each context whose runtime falls within the time period of the segment.
- "Time stamp" column: The time at which the context was started

In segments that combine contexts with logging tags or logging alarms:

- All logged values with the same time stamp are displayed per row.
- "Time stamp" column: The logging event
- "Start time" column: The time at which the context was started
- "Context " &lt;Context name&gt;"" column: The value passed to the context at start
- If no context was started at the time of logging, the context cells remain empty.

**Example**

The following data source items were added to a segment:

- The "Product" context

  Runtime of the context: 15:00:00 to 19:59:59 hours

  The context was started with the "Orange lemonade" value.
- The "Logged_Rotation" logging tag

  Logging cycle: 2s
- The "Logged_Temperature" logging tag

  Logging cycle: 5s
- The user-defined "Unit" column

  It contains the unit for "Logged temperatures".

Content of the data table after execution of the segment:

![Result](images/133584517899_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Lines 2 to 6 | Values were logged for "Logged_Rotation" and "Logged_Temperature", while the "Product" context ran with the "Orange lemonade" value. |
| Line 8 | A value was logged for "Logged_Rotation" while no context was running. |

##### Adding user-defined columns (RT Unified)

###### Introduction

User-defined columns supplement the data of the other data source items of a time series segment with additional information:

- With a fixed string

  The string appears in each cell of the column.

  Example: Display measurement unit of the tag values in report
- With a formula

  The formula is calculated during generation for each cell in the dynamic column.

  Example: The sum of the tag values output in the report.

The configuration of the user-defined column controls which string or formula it uses.

###### Requirement

- The "User-defined column" option was enabled when the connection was set up.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the option "User-defined column".
5. Enter the name of the column under "name".
6. Click "Select" or press &lt;ENTER&gt;.

   The column is included in the list "Selected data source items".
7. Select a configuration for the user-defined column.
8. To remove one or more data source items from "Selected data source items", select them and click "Delete".
9. Confirm with "OK".

**Note**

**Change selection criteria**

After you have added a column, you can select a different option or a different filter and add additional data source items.

The added columns are displayed below the segment and inserted into the data table.

---

**See also**

[Creating and editing configurations for user-defined columns (RT Unified)](#creating-and-editing-configurations-for-user-defined-columns-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

##### Add Audit (RT Unified)

###### Introduction

To output the Runtime device Audit Trail in a report, add an Audit data source item to a report template.

You can find more information about the Audit option in WinCC Unified in the Totally Integrated Automation Portal help.

###### Requirement

- The Audit option was activated in the engineering for the Runtime device.
- The "Audit" option is activated in the connection settings of the Excel add-in.
- The "WinCC Unified" tab is visible in Microsoft Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded.
2. Select a time series segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Audit" option.
5. Select the Audit Trail.
6. (Optional) To undo your selection, select the Audit Trail under "Selected data source items" and click "Delete".
7. Confirm with "OK".

###### Result

The audit data source item is displayed below the segment.

When an Audit Trail is configured for the data source, the Audit data is added to the report when the Runtime data is read into Microsoft Excel and when it is generated in Runtime:

- In the legend table: Identifier of the overall status of the Audit Trail for the queried time range in the "Audit Status" field

  | Value | Description |
  | --- | --- |
  | Green | No manipulations of the Audit Trail were found in the queried time range. |
  | Red | Manipulations of the Audit Trail were found in the queried time range. Single or multiple entries have been deleted, added or changed. |

  Requirement: The "Audit status" option is activated on the segment under "Header properties".

  > **Note**
  >
  > **Overall status for check mode "None"**
  >
  > If the check mode "None" is set in the configuration of the audit data sources item, the "Audit status" field is always green.
- In the data table of the segment: Identifier of manipulations

  | Type of manipulation | Identifier in the data table |
  | --- | --- |
  | Value of entries changed | Directly at the entries |
  | Entries added |  |
  | Entries deleted | The manipulated time range receives a start and end entry. |

First, the data table shows the contents configured in the standard configuration for Audit. To output other contents, select or create a configuration.

#### Setting a display name for standard column (RT Unified)

##### Introduction

You can assign a display name for the standard column of a data source item. When a display name is set, it is used in the data table instead of the default column title and is listed in the table header row.

Display names make reports clearer, for example, when data source items for contexts or tags have very long names.

You set the display name in the local configuration of the data source item.

##### Requirement

- The "WinCC Unified" tab is visible in Excel.
- There is a segment with a matching data source item.

##### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Expand a segment by clicking on it.

   The area for adding and editing data source elements appears.
3. Move the mouse pointer to the data source item and click "Edit".

   The local configuration of the data source item opens.
4. Enter the desired column title in "Display name".

   The column title must be unique within the segment.
5. Confirm your entry with "OK".

**Note**

**Localization**

The column title is stored in the Runtime language currently set in the basic settings of the add-in.

To localize the column title, change the Runtime language and repeat your entry in the new language.

##### Result

- The data table uses the display name as the column title for the standard column of the data source item.
- As long as the following conditions are met, the "Display name" column is inserted into the table header row:

  - Display of the header row in table header row is enabled.

    Make this setting at the segment.
  - A display name is set for at least one data source item of the segment.

  The column lists the display names of all data source items. If no display name is set for a data source item, its cell remains empty.

> **Note**
>
> - If you assign a different configuration to the data source item, the display name is retained.
> - To return to the display of the default column title after assigning a display name, enter the name of the data source item under "Display name".

#### Delete data source elements (RT Unified)

##### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source element is available.

##### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Expand a segment by clicking on it.

   The area for adding and editing data source elements appears.
3. Move the mouse pointer over a data source element and click "Delete".

#### Working with configurations (RT Unified)

This section contains information on the following topics:

- [Basics of configuration (RT Unified)](#basics-of-configuration-rt-unified)
- [Creating or editing configurations for log alarms (RT Unified)](#creating-or-editing-configurations-for-log-alarms-rt-unified)
- [Creating or editing configurations for an alarm statistics (RT Unified)](#creating-or-editing-configurations-for-an-alarm-statistics-rt-unified)
- [Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)
- [Creating or editing configurations for tags: (RT Unified)](#creating-or-editing-configurations-for-tags-rt-unified)
- [Creating or editing configurations for contexts (RT Unified)](#creating-or-editing-configurations-for-contexts-rt-unified)
- [Creating and editing configurations for user-defined columns (RT Unified)](#creating-and-editing-configurations-for-user-defined-columns-rt-unified)
- [Adding or editing configurations for audit (RT Unified)](#adding-or-editing-configurations-for-audit-rt-unified)
- [Select configuration (RT Unified)](#select-configuration-rt-unified)
- [Overwrite a configuration locally (RT Unified)](#overwrite-a-configuration-locally-rt-unified)
- [Delete configuration (RT Unified)](#delete-configuration-rt-unified)
- [Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)
- [Assigning text lists and graphic lists (RT Unified)](#assigning-text-lists-and-graphic-lists-rt-unified)
- [Setting a display name for standard column (RT Unified)](#setting-a-display-name-for-standard-column-rt-unified-1)

##### Basics of configuration (RT Unified)

The configuration of a data source item defines the values of a data source element that are displayed in a segment or how they are calculated and displayed.

There are specific configuration settings for each data-source-item type.

Data source items used in time series segments use a different configuration than data source items used in single-value segments.

You have the following options:

- Use standard configuration.

  There is a standard configuration for all types of data source items. Once added, data source items use the default configuration of their type.

  You can edit the standard configurations.
- Use user-defined configuration.

  You can create any number of user-defined configurations for all types of data source items.

  You can select one of the user-defined configurations on the data source item.
- Overwrite a configuration locally.

  You can overwrite the configuration selected at the data source item locally.

##### Creating or editing configurations for log alarms (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration &gt; Logging alarm configuration".
4. Enter the name of the configuration under "Configuration name".
5. (Optional) Enter texts or graphics from a text list or graphic list in the standard column instead of the alarm IDs.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display the alarm properties.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. (Optional) Filter the logging alarms to be displayed. You define a filter query for this purpose. The filter query can consist of up to two conditions.

   Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an alarm property, an operator, and enter a value.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
8. Enable the option "Use system colors" so that the alarms are highlighted with the same colors as in the alarm control.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for logging alarms.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

---

**See also**

[Select configuration (RT Unified)](#select-configuration-rt-unified)
  
[Calculation modes for data source elements (RT Unified)](#calculation-modes-for-data-source-elements-rt-unified)

##### Creating or editing configurations for an alarm statistics (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration &gt; Alarm statistics configuration".
4. Enter the name of the configuration under "Configuration name".
5. (Optional) Enter texts or graphics from a text list or graphic list in the standard column instead of the alarm IDs.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display the statistical calculations and alarm properties.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. (Optional) Filter the contents to displayed in the alarm statistics. You define a filter query for this purpose. The filter query can consist of up to two conditions.

   Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an alarm property, an operator, and enter a value.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
8. Enable the option "Use system colors" so that the alarms are highlighted with the same colors as in the alarm control.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item.
>
> See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for alarm statistics.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

---

**See also**

[Adding alarm statistics (RT Unified)](#adding-alarm-statistics-rt-unified)

##### Create or edit configurations for logging tags (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration".
4. To create a configuration for logging tags in a time series segment, select the entry "Logging tag configuration".

   To create a configuration for logging tags in a single value segment, select the entry "Single value configuration logging tag".
5. Enter the name of the configuration under "Configuration name".
6. Under "Calculation mode", select the data to be written if no current value is available.
7. (Optional) If the configuration is for logging tags with the numeric data type, you can output texts or graphics from a text list or graphic list in the standard column instead of the tag value.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
8. Set the other settings as described below.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for logging tags.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Additional settings for time series segments

In time series segments, the following additional settings are available for logging tags:

| Setting | Description |
| --- | --- |
| "Interval" | Only for the "Stepped" and "Interpolated" calculation modes. |
| "Columns" &gt; "Quality Code" | (Optional) Change the default settings of the optional "Quality Code" column.  See [Configuring optional columns](#configuring-optional-columns-rt-unified). |

###### Additional settings for single value segments

In single value segments, the following additional settings are available for logging tags:

| Setting | Description |
| --- | --- |
| "Time stamp" | Determine the date and time for which the value is read.   Proceed as described below. |
| "Show captions" | Define whether a header is displayed in the columns for the time stamp, the data source item and the quality code. |
| "Show time stamp" | Determine whether and where this information is displayed in the table. The information is always in relation to the value cell. |
| "Show data source item" |  |
| "Show quality code" |  |

To set the "Time stamp", select one of the following options:

|  |  |  |
| --- | --- | --- |
| ![Additional settings for single value segments](images/129294283275_DV_resource.Stream@PNG-de-DE.png) | Absolute time information | Select a date and a time.  The information is absolute. |
| ![Additional settings for single value segments](images/129293991435_DV_resource.Stream@PNG-de-DE.png) | Relative time information | Select a reference time and a time interval.  The information is relative to the current date. |
| ![Additional settings for single value segments](images/129293995147_DV_resource.Stream@PNG-de-DE.png) | Read time information from cell | Applies the value of the cell currently highlighted in the Excel file.  Make sure that the cell supplies a valid time. |
| ![Additional settings for single value segments](images/129294850187_DV_resource.Stream@PNG-de-DE.png) | Read time information from tag | Applies the value of the set tag.  Make sure that the tag supplies a valid time.  Possible data types:   - DateTime - String - Integer |

---

**See also**

[Calculation modes for data source elements (RT Unified)](#calculation-modes-for-data-source-elements-rt-unified)

##### Creating or editing configurations for tags: (RT Unified)

###### Requirements

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration": ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration&gt; Tag single value configuration".
4. Enter the name of the configuration under "Name".
5. (Optional) If the configuration is for tags with the numeric data type, you can output texts or graphics from a text list or graphic list in the standard column instead of the tag value.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. Set the other settings as described below.
7. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration".
3. Click a configuration for tags.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Settings for single value segments

In single value segments, the following settings are available for tags:

| Setting | Description |
| --- | --- |
| "Show captions" | Select whether a header is displayed in the columns for the time stamp, the data source item and the quality code. |
| "Show time stamp" | Select whether the time stamp is output with the value. |
| "Show data source item" | Select whether the data source element is also output. |
| "Show quality code" | Select whether the quality code is output with the value. |

##### Creating or editing configurations for contexts (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Core statement

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Core statement](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Core statement](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration".
4. Select the entry "Configuration context".
5. Enter the name of the configuration under "Configuration name".
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display important contextual information.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for contexts.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

##### Creating and editing configurations for user-defined columns (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

|  |  |  |  |
| --- | --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group. 2. Click "Data source item configuration":               ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)         ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png) 3. Click "New Configuration &gt; User-defined column configuration". 4. Enter the name of the configuration under "Configuration name". 5. Under "Formula", select one of the following options:    - Enter a fixed string.      The string is transferred into each cell of the column.    - Enter an Excel formula.      The formula is copied into each cell of the user-defined column and adapted to the respective row.       To prevent a part of the formula from being adjusted, place the character "$" in front of it.      Example         |  |  |  |  |      | --- | --- | --- | --- |      | Formula in configuration |  | =B2+C2 | =B$2+C2 |      | Adapting the formula in the report | in line 2 | =B2+C2 | =B2+C2 |      | in line 3 | =B3+C3 | =B2+C3 |  |      | in line 4 | =B4+C4 | =B2+C4 |  |         |  |  |  |  |      | --- | --- | --- | --- |      | **Note**  **No validity check**  The formula is not tested for correctness during either input or dynamic adaptation. |  |  |  | 6. Confirm your entries with "OK". |  |  |  |

##### Adding or editing configurations for audit (RT Unified)

###### Introduction

**Check mode**

The check mode of the configuration of an audit data source item determines

- Whether an integrity check is performed when the Runtime data is read, and what is checked.

  You can output the overall result of the check in the table header row in the "Audit status" field.
- Which audit data records are provided in the data table.

Possible check modes:

| Symbol | Meaning |
| --- | --- |
| "None" | Provides the data for all audit data records that fall within the requested time range. No integrity check is carried out.  Default setting |
| "Check only" | Checks all audit data records that fall within the requested time range without providing their data.   It is tested whether data records have been manipulated, deleted or added. |
| "Check entries" | Checks the audit data records. Provides the data that falls within the queried time range and that was not deleted from the Audit Trail or added later.   It is checked whether data records have been manipulated. |
| "Check all" | Checks all audit data records. Provides the data that falls within the queried time range.   It is tested whether data records were manipulated, deleted from the audit trail or subsequently added. |

**Filter type**

An audit data record consists of two entries:

- An entry for the user expectation
- An entry for the system response.

User expectation and system response may differ. In addition, there are situations in which only one of the two data records is created.

The filter type controls which data records and which entries are included in the report.

Possible filter types:

| Filter type | User expectation equals system response | User expectation does not equal system response | Data record entry for user expectation or system response is missing |
| --- | --- | --- | --- |
| "Show all data in detail" | Both data record entries are inserted. |  | The existing data record entry is inserted. |
| "Show data and conformity errors" | The data record entry with the user expectation is inserted. | Both data record entries are inserted. |  |
| "Show only data with conformity errors" | No data record entry inserted. |  |  |

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration &gt; Audit configuration".
4. Enter the name of the configuration under "Name".
5. Select a check mode:
6. Specify a filter type.

   Preset value: "Show data and conformity errors"
7. (Optional) Change the default settings of the optional columns. The optional columns are used to display the audit attributes.

   You can find more information on configuring the optional columns in the WinCC Unified object model &gt; Creating production logs &gt; Configuring optional columns.
8. (Optional) To further filter the inserted content, define a filter query.

   The filter query can consist of up to two conditions. Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an Audit attribute, an operator and enter the value of the attribute.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. You can find more information on setting the display name in the WinCC Unified object model &gt; Creating production logs &gt; Setting the display name for the standard column.

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for Audit.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Examples of the configuration of the filter type

The following table contains examples of data records that were generated in Runtime through changes to tags monitored by Audit:

| Data record ID | Tag name | Modified by | Old value | New value | Description |
| --- | --- | --- | --- | --- | --- |
| 1A | Motor1_Speed | User1 | 0 | 10 | An operator changes the speed of a motor in an I/O field of an HMI screen.  User expectation and system response are identical. |
| 1B | Motor1_Speed | System | 0 | 10 |  |
| 2A | ValvePercentile | User1 | 0 | 100 | An operator opens a valve using a slider on an HMI screen.  The valve has a physical blockage and cannot be opened. Therefore, no data record entry for the system response is generated. |
| 3A | ValvePercentile | User1 | 0 | 99 | A physical block has been removed and the operator repeats the entry. The valve reacts, but cannot be fully opened.  User expectation and system response differ. |
| 3B | ValvePercentile | System | 0 | 49 |  |
| 4B | Motor2_Speed | System | 0 | 20 | An operator changed the speed of another motor. The resulting data record was manipulated, and the user expectation entry was deleted.  There is only one entry for the system response. |

The following table shows which data record entries are inserted into the data table depending on the filter type selected when generating the report:

| Data record ID | Tag name | Modified by | Old value | New value |
| --- | --- | --- | --- | --- |
| Filter type "Show all data in detail" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 1B | Motor1_Speed | System | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show data and conformity errors" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show only data with conformity errors" |  |  |  |  |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |

---

**See also**

[Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)
  
[Setting a display name for standard column (RT Unified)](#setting-a-display-name-for-standard-column-rt-unified-1)

##### Select configuration (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source item is available.
- There is a user-defined configuration for the type of the data source item.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The segment is extended by the area for the data source items.
3. Select the desired configuration from a data source item in the drop-down list.
4. Click "OK".

###### Result

The changes are applied the next time you read in the runtime data.

##### Overwrite a configuration locally (RT Unified)

A local configuration overwrites the configuration selected at the data source item. It applies only to the data source item for which it was entered.

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source item is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The segment is expanded to include the plant complex for the data source items.
3. Move the mouse over a data source item and click "Edit".

   You create a local configuration that first adopts the values of the original configuration.
4. Enter a name for the local configuration.
5. (Optional) Set a display name. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified-1).
6. Make the remaining settings as required.

   You can make the same settings as in the default and custom configurations.
7. Confirm your entries with "OK".

###### Result

The changes are applied the next time you read in the Runtime data.

##### Delete configuration (RT Unified)

###### Requirement

A configuration is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration".
3. Move the mouse to a configuration.
4. Click "Delete".

**Note**

**Default configurations cannot be deleted**

You can edit default configurations but not delete them.

###### Result

- The configuration is deleted.
- Data source items with this configuration obtain a local configuration with the same settings.

##### Configuring optional columns (RT Unified)

###### Introduction

In time series segments, data source items of the following types have optional columns:

- Logging tag
- Logging alarm
- Alarm statistics
- Audit
- Context

The optional columns of a data source item depend on its type. The configuration of the data source items controls whether and how the data table shows these columns.

This section describes how to configure the optional columns.

###### Requirements

The data source item configuration is open. The configuration must apply to a time series segment.

###### Showing and hiding columns

1. To show an optional column in the data table, enable the option for the desired column in the "Columns" area.
2. To hide a column, disable its option.

###### Changing the column title

The data table uses as default column titles the identifiers you see in the "Columns" area. To change the default column titles, do the following.

1. In the "Columns" area, move the mouse pointer to an optional column.
2. Click the button with the pin.
3. Assign a unique column title.

**Note**

**Localization**

The column title is stored in the Runtime language currently set in the basic settings of the add-in.

To localize the column title, change the Runtime language and repeat your entry in the new language.

###### Changing the column sequence

To change the order of the optional columns in the data table, proceed as described in [Changing the column sequence](#changing-the-column-sequence-rt-unified).

###### Assigning text list or graphic list

The values of numeric columns can be replaced by texts or graphics when the Runtime data is read in.

To assign a suitable text list or graphic list to the property, proceed as described in [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

##### Assigning text lists and graphic lists (RT Unified)

###### Introduction

If standard columns and optional columns of data source items output numerical values, you can assign text lists and graphic lists to these columns. When the Runtime data is read in, the cell values of these columns are replaced by texts or graphics from the assigned lists.

This function improves the readability of the report and helps to draw the reader's attention to important information.

> **Note**
>
> **Restrictions**
>
> - Tags/logging tags
>
>   Assign a text list or graphic list to the standard column of data source items with a Tag or Logging tag type only if the tag or logging tag has a numeric data type.
>
>   You can assign a text list or graphic list to the optional "Quality Code" column regardless of the data type of the tag.
> - User-defined columns
>
>   It is not possible to assign a text list or graphic list for data source items with the User-defined column type.
> - Context and audit
>
>   Usually, the names of context objects and audit objects displayed in the standard column do not contain purely numerical values. It is not recommended to assign a text list or graphic list.

###### Example

Add two data source items with the same logging tag to a time series segment.

For the first data source item, use the default configuration. This causes the report to output the tag value in the standard column.

For the second data source item, select a configuration in which a graphic list is assigned to the standard column. The graphic list contains representational graphics staggered by value range. As a result, the report outputs a graphic in the standard column.

After reading in the Runtime data, the standard column of the second data source item makes readers of the report aware of limit violations. Readers can get the exact tag value from the standard column of the first data source item.

###### Requirements

- A segment with a data source item was created in the add-in.
- Suitable text lists or graphic lists have been configured in engineering for the connected data source.

###### Assigning text lists and graphic lists to the standard column

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The data source items of the segment are displayed.
3. Move the mouse over a data source item and click "Edit".

   The local configuration of the data source item opens.
4. Select a suitable list under "Assign text/graphic list".
5. To preview the selected list and its graphics or texts, click the "i" button.

   To hide the preview, click the "i" button again.

###### Assigning optional columns to text lists and graphic lists

1. Click on "Segments" in the "Configuration" group.
2. Select one of the following options:

   To make the assignment apply to a specific data source item, follow these steps:

   - Select the segment.

     The data source items of the segment are displayed.
   - Move the mouse over the data source item and click "Edit".

     The local configuration of the data source item opens.

   To make the assignment apply to multiple data source items of the same type, follow these steps:

   - Click "Data source item configuration": ![Assigning optional columns to text lists and graphic lists](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     You can see all default and custom configurations.
   - Click on the desired configuration.

     The configuration opens.
3. In the "Columns" area, click the following button next to the desired optional column:

   ![Assigning optional columns to text lists and graphic lists](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   ![Assigning optional columns to text lists and graphic lists](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   An interface for assigning a text list or graphic list is loaded into the add-in.
4. Select the desired graphic list or text list from the drop-down list.
5. To preview the selected list and its graphics or texts, click the "i" button.

   To hide the preview, click the "i" button again.
6. Confirm your entries.

**Note**

If you are connected offline to the data source, no preview of graphic lists is available.

###### Result

When the Runtime data is read in, the assigned lists are searched for an entry that matches the actual cell value:

- If a matching entry is found, the corresponding text or graphic is inserted into the data table.
- If no matching entry is found, the actual cell value is inserted.

> **Note**
>
> The assignment of graphic lists slows down the import of the Runtime data into the Excel add-in.

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)
  
[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)

##### Setting a display name for standard column (RT Unified)

###### Introduction

You can assign a display name for the standard column of a data source item. When a display name is set, it is used in the data table instead of the default column title and is listed in the table header row.

Display names make reports clearer, for example, when data source items for contexts or tags have very long names.

You set the display name in the local configuration of the data source item.

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- There is a segment with a matching data source item.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Expand a segment by clicking on it.

   The area for adding and editing data source elements appears.
3. Move the mouse pointer to the data source item and click "Edit".

   The local configuration of the data source item opens.
4. Enter the desired column title in "Display name".

   The column title must be unique within the segment.
5. Confirm your entry with "OK".

**Note**

**Localization**

The column title is stored in the Runtime language currently set in the basic settings of the add-in.

To localize the column title, change the Runtime language and repeat your entry in the new language.

###### Result

- The data table uses the display name as the column title for the standard column of the data source item.
- As long as the following conditions are met, the "Display name" column is inserted into the table header row:

  - Display of the header row in table header row is enabled.

    Make this setting at the segment.
  - A display name is set for at least one data source item of the segment.

  The column lists the display names of all data source items. If no display name is set for a data source item, its cell remains empty.

> **Note**
>
> - If you assign a different configuration to the data source item, the display name is retained.
> - To return to the display of the default column title after assigning a display name, enter the name of the data source item under "Display name".

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)
  
[Overwrite a configuration locally (RT Unified)](#overwrite-a-configuration-locally-rt-unified)

#### Changing the column sequence (RT Unified)

##### Introduction

For a time series segment, you can change the default column order of the data table.

You have the following options:

- Specify the order which the data source items have in the data table.
- For each data source item: Set the order of its optional columns.

> **Note**
>
> The time stamp column always appears first.

##### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A time series segment has been created.

##### Change the order of data source items

**Procedure**

1. Click on "Segments" in the "Configuration" group.
2. Click the time series segment in the list of time series segments.

   The data source items of the segment are displayed.
3. Left-click a data source item and move it up or down using drag-and-drop operation.

**Result**

The order of data source items in the segment interface is changed.

The next time the Runtime data is read in, the data table outputs the data source items in this order.

##### Changing the order of optional columns

**Procedure**

1. Select one of the following options:

   To change the column order of a particular data source item, follow these steps:

   - Select the segment.

     The data source items of the segment are displayed.
   - Move the mouse over the data source item and click "Edit".

     The local configuration of the data source item opens.

   To change the column order for all data source items that use the same configuration, follow these steps:

   - Click "Data source item configuration":

     ![Changing the order of optional columns](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     ![Changing the order of optional columns](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     You can see all default and custom configurations.
   - Click on the desired configuration.

     The configuration opens.
2. Move the mouse pointer to a column under "Columns".

   The columns you see depend on the type of data source item.
3. Move the column up or down using the arrow buttons or drag-and-drop.

**Result**

The order of the optional columns in the configuration is changed.

The next time the Runtime data is read in, the data table outputs the optional columns in the changed order.

---

**See also**

[Creating or editing configurations for log alarms (RT Unified)](#creating-or-editing-configurations-for-log-alarms-rt-unified)
  
[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)
  
[Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)

#### Reading Runtime data in Excel (RT Unified)

> **Note**
>
> Reading in Runtime data in Excel is used for testing. It is not intended for mass retrieval of data, as is the case when report jobs are executed in Runtime.

##### Requirement

An online connection is established.

##### Reading in all segments

1. Select "WinCC Unified &gt; Segments".
2. Click "Update all":

   ![Reading in all segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

   ![Reading in all segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

##### Reading in individual segments

1. Select "WinCC Unified &gt; Segments".
2. Next to a segment in the list of segments click, "Update":

   ![Reading in individual segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

   ![Reading in individual segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

##### Result

The segment or segments are run. The Runtime data of your data source items are read into Excel.

> **Note**
>
> **Controlling the column width and row height**
>
> When the automatic adjustment of the column width and row height is disabled in the segment properties, the text read in may be truncated or the formula results are replaced with "#" characters.
>
> Check the column widths and row heights and adjust them manually, if required, or select automatic adjustment. Manual adaptations only apply in the Excel add-in. They are not included in the generated reports.

> **Note**
>
> **Removing Runtime data from report template**
>
> Remove the Runtime data from the report template before you save the report template and make it available for uploading to Runtime.
>
> To do this, click the "Delete Runtime data" button ![Result](images/142024787723_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the Excel add-in.

##### Diagnostics during the data query

Successful execution of the data query is documented by the add-in with a status message in the table.

If an error occurs during the data query, a general error message is displayed under status. In addition, detailed error messages are displayed in the "ErrorLog" worksheet.

#### Calculation modes for data source elements (RT Unified)

If there is no current value for a data source item for a requested point in time, the following calculation modes are available.

##### Calculation modes for tags

The following calculation modes are available for tags of a time series segment:

| Calculation mode | Description |
| --- | --- |
| Raw | The actual value available for the specified period. If no data are available, no value is output. |
| Stepped | If no data are available, the last value is used.  With this mode you can also use values with an invalid quality code. |
| Interpolate | The values are interpolated linearly for the specified time period.  With this mode you can only use values with a valid quality code. |

The following calculation modes are available for tags of a single value segment:

| Calculation mode | Description |
| --- | --- |
| Interpolate | The values are interpolated linearly for the specified time period.  With this mode you can only use values with a valid quality code. |
| Left | If no data is available, the last value before the specified period is used. |
| Right | If no data is available, the last value after the specified period is used. |

---

**See also**

[Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)

### Making general settings (RT Unified)

This section contains information on the following topics:

- [Changing the language (RT Unified)](#changing-the-language-rt-unified)
- [Adapting the work area (RT Unified)](#adapting-the-work-area-rt-unified)
- [Zooming in the add-in (RT Unified)](#zooming-in-the-add-in-rt-unified)

#### Changing the language (RT Unified)

##### Changing the add-in language

The Excel add-in automatically uses the same user interface language as Excel. If you are using a language for Excel that is not included in the Unified options, English is used as the default language.

You can select the language for the contents of the report independently of the interface. To select another language, the language must be configured in Runtime.

##### Selecting the language for the report

1. Select "WinCC Unified &gt; Segments".
2. Click "Basic settings":

   ![Selecting the language for the report](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   ![Selecting the language for the report](images/142024587787_DV_resource.Stream@PNG-de-DE.png)
3. Under "Runtime language", select the language of the report content.
4. Under "Query language" you select which language data queries have that require user input, e.g. filter definitions.

#### Adapting the work area (RT Unified)

##### Undocking and moving the add-in

To enlarge your working area, you can undock the Excel add-in:

1. Open the drop-down list in the header of the add-in.
2. Click "Move".
3. Move the mouse pointer to the desired location and click the left mouse button.
4. To move the add-in again, keep the left mouse button pressed in the header of the add-in and move the mouse.
5. To dock the add-in again, double-click in the header of the add-in.

##### Adapting the size of the add-in

1. Open the drop-down list in the header of the add-in.
2. Click "Resize".
3. Move the mouse pointer to the left to make the add-in wider or to the right to make it narrower.
4. Left-click when you have reached the desired size.

#### Zooming in the add-in (RT Unified)

##### Procedure

To zoom in or out of the display in the add-in, press &lt;CTRL&gt; and move the mouse wheel.

### Undo and redo (RT Unified)

The Excel functions "Undo" and "Redo" are not available in the add-in.

### Tips on design and layout (RT Unified)

This section includes tips on the visual design of reports. The apply for:

- Report templates
- Reports that were generated as XLSX file

> **Note**
>
> **Deviating PDF results**
>
> A PDF report created by LibreOffice can deviate in content or layout from a PDF report generated with Excel, for example, if the report template uses common Excel features that LibreOffice does not support, such as special fonts or chart types.

#### Arranging segments

Always place the segments of a report template side by side or each in their own worksheet.

Because the data tables of the segments grow dynamically, tables can overlap when segments are placed one below the other. In the add-in, this causes an error of the OfficeExtension.Error class when reading in the Runtime data.

#### Changing the column sequence

See section [Changing the column sequence](#changing-the-column-sequence-rt-unified).

#### Adapt column width and row height

For each segment of a report template, check whether the column widths and row heights of your data table are wide or high enough for the values to be read. If this is not the case, texts in the generated report are truncated or the formula results are replaced with "#" characters.

To do this, select one of the following options:

- In the properties of the segments, select the options for automatic adjustment of the column width and row height.
- Click "Update all"![Adapt column width and row height](images/142023530251_DV_resource.Stream@PNG-de-DE.png) in the report template.

  Values are imported to Excel from the data source. Check the column widths and row heights and adjust them manually, if required.

  > **Note**
  >
  > The manual adaptations apply only in the Excel add-in. They are not included in the generated reports.

#### Replacing numerical values

If columns of a data source item output numeric values, you can assign text lists and graphic lists to the columns. When the Runtime data is read in, the cell values of these columns are replaced by texts or graphics from the assigned lists. This improves the readability of the report and helps to draw the reader's attention to important information.

Example: Visualizing limit violations of tags with graphics

See section [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

#### Preparing imported Runtime data

Adjust the cell formatting of the Runtime data, for example, font, color, alignment, or number format. The rows inserted when reading the Runtime data adopt the formatting.

Add diagrams, pivot tables or formulas that graphically visualize, structure or evaluate the data imported from Runtime.

> **Note**
>
> If you have read Runtime data into the report template for better data preparation, remove it before saving the report template and making it available for upload to Runtime.
>
> To do this, click the "Delete Runtime data" button ![Preparing imported Runtime data](images/142024787723_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the Excel add-in.

#### Set up page

Use "File &gt; Print &gt; Set up page" to define details for printing the report, for example:

- Alignment of the report (portrait format or landscape format)
- Scaling, for example, to print all columns on one page
- Inserting a user-defined header or footer

The print settings set in the report template are applied in Runtime when a report job is executed for PDF generation.

#### Renaming worksheets and segments

When you add a segment to a report template in the add-in, a table is created in Excel. The add-in addresses the table by the name of the worksheet and segment.

Do not rename worksheets after adding segments.

Do not change the table name of a segment using the Excel property "Table name". Edit the segment in the add-in and rename it there.

## Working with production reports in Runtime (RT Unified)

This section contains information on the following topics:

- [Requirements and restrictions (RT Unified)](#requirements-and-restrictions-rt-unified)
- [Workflow for working with reports in Runtime (RT Unified)](#workflow-for-working-with-reports-in-runtime-rt-unified)
- [The user interface of the "Reports" control (RT Unified)](#the-user-interface-of-the-reports-control-rt-unified)
- [Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified)
- [Configuring task parameters (RT Unified)](#configuring-task-parameters-rt-unified)
- [Configuring report tasks (RT Unified)](#configuring-report-tasks-rt-unified)
- [Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
- [Downloading reports (RT Unified)](#downloading-reports-rt-unified)
- [Exporting an offline configuration file (RT Unified)](#exporting-an-offline-configuration-file-rt-unified)
- [Transferring the control configuration (RT Unified)](#transferring-the-control-configuration-rt-unified)
- [Configuring enable paging (RT Unified)](#configuring-enable-paging-rt-unified)
- [Inconsistencies and error diagnostics (RT Unified)](#inconsistencies-and-error-diagnostics-rt-unified)
- [Dynamic placeholder (RT Unified)](#dynamic-placeholder-rt-unified)

### Requirements and restrictions (RT Unified)

The following requirements and restrictions apply to the configuration of report jobs and to the generation of reports on Unified PCs and Unified Comfort Panels, both in Runtime and during simulation.

#### Enable Reporting

The reporting functionality must be enabled for the Runtime project that is running or being simulated on the HMI device.

You activate the reporting functionality of a Runtime project before loading it into the device in TIA Portal: "Runtime settings" of the HMI device &gt; "Reporting" &gt; "Enable Reporting" option

> **Note**
>
> **Devices with a device version lower than V18**
>
> Reporting is always enabled for HMI devices with a device version lower than V18.

#### Unified Comfort Panel

The following restrictions apply to generating reports on Unified Comfort Panels:

| Symbol | Meaning |
| --- | --- |
| Contexts | Contexts are not supported for Unified Comfort Panel.   When you generate a report on a Unified Comfort Panel whose report template uses this option, error entries are generated in the "ErrorLog" worksheet of the report. |
| Storage location of the Reporting database | Devices as of V18 use the following folder of the SD card inserted on the panel by default: `media/simatic/X51/Reports`  You can configure and load another storage location in TIA Portal in the Runtime settings of the Panel.  Devices with a version lower than V18 always use the following folder of the SD card: `media/simatic/X51` |
| Storage location for reports | By default, the following folder of the SD card inserted on the panel is used as the main local storage location for reports: `media/simatic/X51/Reports`  For devices as of version V18, you have the option to configure and load a different local main storage location in TIA Portal in the Runtime settings of the panel.  Devices with a version lower than V18 always use this folder of the SD card. |

---

**See also**

[Reporting (Unified PC) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-pc-rt-unified)
  
[Reporting (Unified Comfort Panel) (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#reporting-unified-comfort-panel-rt-unified)

### Workflow for working with reports in Runtime (RT Unified)

#### Introduction

The following workflow describes which works are required in the "Reports" control so that production reports are generated in Runtime.

The reports can be stored as file in the file system and sent as an attachment to an e-mail. Alternatively, an e-mail without attachment can also be sent about the generation of the report. In this way, employees from management and production are promptly informed about the production situation, regardless of their location.

You can send the e-mail using a secure SMTP server (authentication with user name and password or via certificate) or an unsecured SMTP server, for example, an internal company mail server.

#### Requirement

- Requirements in TIA Portal:

  - The necessary project data were configured for the HMI device for which reports are to be created.
  - The "Reports" control was placed on an HMI screen of the device.
  - The "Enable Reporting" option was enabled in the Runtime settings of the device.
  - (Optional) The storage locations for reports and the Reporting database were configured in the Runtime settings of the device.
- The HMI device has been compiled, loaded into Runtime and its Runtime project has the status "Running".
- The HMI device has access to report templates.
- Unified PC: If one of the report templates used in Runtime evaluates contexts, contexts must have been configured for the currently running Runtime project and executed in Runtime.
- For cross-project and cross-Runtime use of report templates: The data sources used in the report template can also be found on the HMI device. Make sure that the names and plant hierarchy are consistent.

#### Procedure

1. To send reports by e-mail, configure the global e-mail settings:

   - When one of the servers requires a certificate for sending e-mails, upload the certificate.
   - Create contacts for the e-mail receivers and e-mail senders.
   - Create the required SMTP server configurations.
2. Configure job parameters for report templates, triggers and targets.

   These job parameters will then be available to you for selection when configuring the report jobs.
3. Configure report jobs.

   Reports are generated in Runtime when the report jobs are executed.
4. (Optional) Perform report orders manually.
5. In the control, get an overview of which reports have been generated.
6. Download the reports, if necessary.
7. (Optional) To reuse the configuration of the "Reports" control, such as on a device in another network, transfer the existing configuration from the control from one device to the control of the other device.

#### Configuring job parameters

First, you configure which job parameters are available for selection during the configuration of the report jobs. You configure the following job parameters:

- The available report templates

  The report template defines which data the report outputs. Import and/or delete templates, if required.
- The available triggers

  The trigger defines when a report job is executed. Add triggers, edit triggers or delete them.
- The available targets

  Targets define whether reports are made available to users in the file system or via e-mails. Add targets, edit triggers, or delete them.

You set further job parameters while configuring a report job in the "Report jobs" tab.

#### Configuring a report job

You configure the following for each report job:

- Name of the report job
- Used report template
- Name of the reports generated by this template

  > **Note**
  >
  > **Texts through dynamic placeholders**
  >
  > Placeholders are available to you when defining the report name. The placeholders are evaluated and replaced by text during execution of the report.
  >
  > See also [Dynamic placeholder](#dynamic-placeholder-rt-unified).
- Targets of the generated report

  To send e-mails, select a target of the type "E-mail".
- Per target: The target format of the generated report

  Possible formats: .XLSX and .PDF
- Trigger
- Comment
- Activate

---

**See also**

[Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified-1)
  
[Configuring task parameters (RT Unified)](#configuring-task-parameters-rt-unified)
  
[Configuring report tasks (RT Unified)](#configuring-report-tasks-rt-unified)
  
[Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
  
[Downloading reports (RT Unified)](#downloading-reports-rt-unified)
  
[Transferring the control configuration (RT Unified)](#transferring-the-control-configuration-rt-unified)
  
[Complete workflow for using production reports (RT Unified)](#complete-workflow-for-using-production-reports-rt-unified)
  
[Creating report templates for production reports (RT Unified)](#creating-report-templates-for-production-reports-rt-unified)

### The user interface of the "Reports" control (RT Unified)

> **Note**
>
> **Automatic data transfer**
>
> Changes in the "Reports" control are saved automatically.

#### Layout

You create and manage report jobs in the "Reports" control. You also have access to the reports generated by the report jobs.

The control has the following structure:

![Layout](images/158985390731_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1 | Tab for the configuration and management of reports, report jobs, job parameters and global settings |
| 2 | Toolbar  The buttons you see depend on the tab. |
| 3 | Work area   On the "Reports", "Report jobs" and "Job parameters" tabs: List of elements available on the tab  On the "Global settings" tab: The settings |
| 4 | Options for selecting the elements  You can select elements individually or all at once. |
| 5 | Detail area  Shows the properties of the selected element. |
| 6 | Information bar |

#### Tab

**"Reports" tab**

Here you can see which reports have been generated. You can download or delete reports via the toolbar.

The "Status" column shows Information:

- On the status of the generated report files (XLSX and PDF)
- On the status of the targets (File system and E-mail)

Overview of the status icons:

| Status | Description |
| --- | --- |
| ![Tab](images/136004352139_DV_resource.Stream@PNG-de-DE.png) | Execution has been successfully completed. |
| ![Tab](images/136004343563_DV_resource.Stream@PNG-de-DE.png) | An error occurred during execution. |
| ![Tab](images/136004437771_DV_resource.Stream@PNG-de-DE.png) | Execution is in progress. |

A click on an icon opens a detailed status message.

**"Report jobs" tab**

Here you create new report jobs, manage existing report jobs or start a report job manually.

**"Job parameters" tab**

Here you manage the parameters with which you configure the report jobs in the "Report jobs" tab.

**"Global settings" tab**

Here you make the following settings:

- For sending e-mails
- For transfer of the control configuration
- For creating an offline configuration file
- For configuring paging

#### Toolbar

The following buttons are available in the toolbars of the tab:

| Icon | Button |  |
| --- | --- | --- |
| ![Toolbar](images/129288141323_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the elements whose option is enabled in the work area. |
| ![Toolbar](images/129286967947_DV_resource.Stream@PNG-de-DE.png) | - Add new - Import | - Creates a new element. - "Job parameters &gt; Templates" tab: To import a report template into Runtime |
| ![Toolbar](images/129288760331_DV_resource.Stream@PNG-de-DE.png) | Run | In the "Report jobs" tab.  Manually creates a report for the report job whose option is enabled in the work area. |
| ![Toolbar](images/129288150155_DV_resource.Stream@PNG-de-DE.png) | Export | - In the "Job parameters &gt; Templates" tab: To export report templates - In the "Reports" tab:  To download reports to the client |

#### Information bar

The button in the information bar displays general information sent by the reporting service, for example, on whether a report job has been executed.

### Setting global email settings (RT Unified)

This section contains information on the following topics:

- [Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified-1)
- [Upload certificates (RT Unified)](#upload-certificates-rt-unified)
- [Maintaining contacts (RT Unified)](#maintaining-contacts-rt-unified)
- [Maintenance of the SMTP server configuration (RT Unified)](#maintenance-of-the-smtp-server-configuration-rt-unified)

#### Setting global email settings (RT Unified)

If configured accordingly, an e-mail is sent automatically after a report job is executed. The e-mail can include the report as an attachment.

Maintenance of the basic settings for sending e-mails is carried out in the "Global settings" tab:

- If necessary: The certificates that the e-mail sender uses to authenticate itself at the SMTP servers.
- The contact information of the e-mail senders and e-mail receivers.
- The configuration of the SMTP server via which the e-mails are sent.

#### Upload certificates (RT Unified)

Store the certificates of the SMTP servers that require authentication via certificate.

##### Requirement

- You have access to the storage location of a valid certificate file.

##### Procedure

1. In the "Reports" control, click on the "Global settings &gt; Certificates" tab.
2. Click "Add new" in the toolbar.

   Alternative: In the work area, click "Add new".
3. In the dialog that opens, select the certificate file.
4. Confirm your input.
5. Optional: Select the uploaded certificate in the work area and enter a comment on the certificate in the detail area.

##### Result

The certificates uploaded here are available in the "Contacts" tab.

#### Maintaining contacts (RT Unified)

Store the data of the e-mail senders and email recipients.

##### Procedure

To create a new contact, follow these steps:

1. In the "Reports" control, click on the "Global settings &gt; Contacts" tab.
2. Click "Add new".
3. Enter the name of the contact.
4. Enter the e-mail address of the contact.
5. To use the contact as a sender for an SMTP server that requires authentication with a certificate, select the appropriate certificate under "Certificate".
6. To use the contact as a sender for an SMTP server that requires authentication with a user name and password, enter the password.

   The e-mail address is used as the user name.
7. (Optional) Enter a comment relating to the contact.

##### Result

The contacts configured here are available:

- As the e-mail sender in the SMTP server configuration.
- As an e-mail recipient when configuring "target" job parameters with the target type e-mail

#### Maintenance of the SMTP server configuration (RT Unified)

Store the data of the SMTP servers via which the e-mails are sent.

##### Requirement

Contacts that are suitable as senders have been entered in the "Global Settings &gt; Contacts" tab.

##### Procedure

To create a new SMTP server configuration, follow these steps:

| 1. In the "Reports" control, click on the "Global settings &gt; SMTP" tab. 2. Click "Add new". 3. Specify the following:       | Field | Description |    | --- | --- |    | "Name" | Enter the name of the SMTP server configuration. |    | "Address" | Enter the URL of the SMTP server. Servers without authentication (e.g. company-internal mail servers) and with authentication are permitted. Example: URL of a company mail server: `mail.<``Company name``>.com` |    | "Port" | Enter the port number of the SMTP server. Default setting: 25 |    | "Sender" | In the list, select the contact that is used as the sender for this SMTP server configuration.  All contacts maintained under "Contacts" are offered to you for selection. Select a sender that meets the respective requirements of the server. |    | "Comment" | (Optional) Enter a comment relating to the SMTP server configuration. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The servers configured here are available when configuring the "Target" job parameters with the target type email.

### Configuring task parameters (RT Unified)

This section contains information on the following topics:

- [Configuring job parameters (RT Unified)](#configuring-job-parameters-rt-unified)
- [Importing and exporting report templates (RT Unified)](#importing-and-exporting-report-templates-rt-unified)
- [Deleting templates (RT Unified)](#deleting-templates-rt-unified)
- [Configure trigger (RT Unified)](#configure-trigger-rt-unified)
- [Add target with target type "E-mail" (RT Unified)](#add-target-with-target-type-e-mail-rt-unified)
- [Add a target with "File system" target type (Unified PC) (RT Unified)](#add-a-target-with-file-system-target-type-unified-pc-rt-unified)
- [Add a target with "File system" target type (Unified Panel) (RT Unified)](#add-a-target-with-file-system-target-type-unified-panel-rt-unified)

#### Configuring job parameters (RT Unified)

Job parameters define the details of a report job.

You configure the following parameters on the "Job parameters" tab:

- Templates
- Trigger

  Define trigger when a report job is executed.
- Targets

  Targets define how a report is made available to users. The following target types are available:

  - "E-mail"

    An e-mail is sent after a report job is executed. The report generated by the report job can be included with the e-mail as an attachment.
  - "File system"

    The reports generated by the report job are stored in the file system.

The parameters configured here are available to you for selection when configuring the report jobs in the "Report jobs" tab.

You define the remaining job parameters while configuring a report job in the "Report jobs" tab.

---

**See also**

[Importing and exporting report templates (RT Unified)](#importing-and-exporting-report-templates-rt-unified)
  
[Deleting templates (RT Unified)](#deleting-templates-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)

#### Importing and exporting report templates (RT Unified)

##### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters &gt; Templates" tab is visible in the control.
- Import: You have access to the storage location of the report template.
- Export: Report templates have been imported into the control.

##### Importing report template

1. Click "Add new" in the toolbar.

   Alternative: In the work area, click "Add new".
2. In the dialog that opens, select the file of a report template.
3. Confirm your input.
4. Optional: In the work area, select the imported report template in the work area and enter a comment describing the template in the detail area.

**Note**

**No validation**

The template is not validated during import.

##### Exporting report templates

1. In the work area, select the options next to the report templates you want to export.
2. Click "Export" in the toolbar.

The report templates are downloaded to the download folder or a user-defined directory according to the device settings.

#### Deleting templates (RT Unified)

##### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters &gt; Templates" tab is visible in the control.
- Templates have been imported into the control.

##### Procedure

1. In the work area, select the options next to the templates you want to delete.
2. Click "Delete" in the toolbar.

**Deleting used templates**

The "In use" column shows whether the template is used by a report job.

If you delete a template that is used by a report job, the report job is marked as inconsistent and no longer executed.

#### Configure trigger (RT Unified)

##### Introduction

In the "Job Parameters &gt; Triggers" tab you configure which automatic triggers are available for selection when configuring report jobs.

Report jobs with automatic triggers are executed if the report jobs on the "Report jobs" tab are set to active and their trigger event occurs. Users can also start the execution manually.

##### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters &gt; Trigger" tab is visible in the control.
- To use the trigger type "Context trigger": Contexts are available in the project.

##### Add trigger

| 1. In the work area of the tab, click "Add new".    A new trigger is created and displayed in the detail area. 2. Assign a unique name to the trigger. 3. Select the trigger mode:        | Trigger type | Triggering the trigger |    | --- | --- |    | "Tag trigger" | Automatically when the configured value condition occurs at the tag defined in the trigger. |    | "Serial trigger" | Automatically within the user-defined interval when the time defined by the series has been reached. |    | "Context trigger" | Automatically when the selected context is started or stopped. Optional: By using a condition, you can also limit the triggering of the trigger to specific context values. | 4. Depending on the selected trigger type, set the settings for the new trigger as described below. 5. Optional: Enter a comment for the trigger. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Settings for tag trigger

| Symbol | Meaning |
| --- | --- |
| 1. Click "Select tag". 2. Click "Load". 3. Select the required tag and click "OK". 4. Set the condition and the condition value.    Example:        | Symbol | Meaning |    | --- | --- |    | Set tag | &lt;tag name&gt; |    | Condition | &gt; |    | Condition value | 100 |     The trigger will be initiated when the tag receives a value greater than 100. |  |

##### Settings for serial triggers

| Symbol | Meaning |
| --- | --- |
| 1. Select the serial pattern.    The series pattern defines the occurrence and time at which the trigger is initiated.    Example: Weekly &gt; Every 2 weeks &gt; Fridays 2. Select the series area.    The series range defines the period in which the trigger is initiated.       | Symbol | Meaning |    | --- | --- |    | "Start" | Specify the start date |    | "Time" | Specify the time at which the trigger is initiated. |    | "End on" | Specify the end date. The trigger will be executed for the last time on this day. |    | "End after" | Determine the number of dates after which the series ends. |    | "No end date" | The series runs indefinitely. | |  |

##### Settings for context triggers

| Symbol | Meaning |
| --- | --- |
| 1. Click "Select context". 2. In the "Context selection" dialog, click "Select plant object". 3. In the "Browser view" dialog, select a plant object and confirm your input.    In the "Context selection" dialog you can see all contexts that have been defined for the selected plant object. 4. Select a context and confirm your input. 5. Under "Context status", select when the trigger will be triggered:       | Symbol | Meaning |    | --- | --- |    | "Started" | When starting the context. |    | "Stopped" | When stopping the context. | 6. Optional: To bind the execution of the report order to certain context values, you define a condition:       | Symbol | Meaning |    | --- | --- |    | "Condition" | Select an operator. |    | "Value" | Select a context value. |     Example:       | Symbol | Meaning |    | --- | --- |    | Plant object | "MyPlant.hierarchy::PlantView/Bottling" |    | Context | "Product" |    | Context state | "Started" |    | Condition | = |    | Value | "Orange lemonade" |     Report jobs with this trigger are always executed when the context "Product" defined on the plant object "Bottling" is started with the value "Orange lemonade". |  |

##### Delete trigger

Select the option of the desired trigger in the work area of the "Job Parameters &gt; Triggers" tab and click "Delete" in the toolbar.

##### Edit trigger

1. Enable the option of the desired trigger in the work area of the tab.
2. In the detail area, edit the settings of the trigger.

**Note**

**No change of the trigger type**

The trigger type can only be set when adding the trigger.

#### Add target with target type "E-mail" (RT Unified)

##### Requirement

- The "Reports" control is placed on a screen of the project.
- The receivers of the e-mails are maintained as contacts in the "Global settings &gt; Contacts" tab.
- An SMTP server, with which the e-mail is to be sent, has been configured in the "Global settings &gt; SMTP" tab.

##### Procedure

1. In the "Reports" control, click on the "Job parameters &gt; Targets" tab.
2. In the work area of the tab, click "Add new".
3. Select "E-mail" as target type.

   A new target is created and displayed in the detail area.
4. Assign a unique name to the target.
5. Select an SMTP server configuration.
6. Add the desired receivers and CC receivers:

   - To do so, select a contact from the list "Add receiver" or "Add CC receiver".
   - Add the contact by clicking "+".
7. Enter the e-mail subject.

   To integrate the report name into the subject line, use the placeholder {ReportName}.
8. Enter the e-mail text.

   To integrate the report name into the email text, use the placeholder {ReportName}.
9. (Optional) Enter a comment.

##### Result

The target is available for selection when configuring report jobs.

An e-mail is sent after a report job is executed with this target. The e-mail can include the report as attachment.

---

**See also**

[Dynamic placeholder (RT Unified)](#dynamic-placeholder-rt-unified)

#### Add a target with "File system" target type (Unified PC) (RT Unified)

This section describes how to add a target with the "File system" target type on a Unified PC in Runtime.

##### Introduction

A reporting job with a target of the "File system" target type saves reports to a file system.

When configuring the report jobs, you can choose from pre-configured and user-defined targets of this target type.

**Preconfigured targets**

The following targets with "File system" target type are pre-configured:

| Symbol | Meaning |
| --- | --- |
| Local project storage location | The reports are stored in the following folder: `<Project folder of the Runtime project>\``Reports` |
| Local main storage location | The reports are stored in the local main storage location for reports. The local main storage location is configured in TIA Portal in the Runtime settings of the HMI device.  If this setting has not been set in TIA Portal, the reports are stored in the folder configured during the installation of Runtime or later in the "WinCC Unified Configuration" tool: |

You can select these targets in the "Report jobs" tab. You cannot edit or delete these targets in the "Job parameters &gt; Targets" tab.

**User-defined targets**

In the "Reports" control, you can create user-defined targets of the "File system" target type. These user-defined targets are always subfolders of the local main storage location.

##### Requirement

- The "Reports" control is placed on a process picture.

##### Procedure

To add user-defined targets of the "File system" target type, follow these steps:

1. In the "Reports" control, click on the "Job parameters &gt; Targets" tab.
2. In the work area of the tab, click "Add new".
3. Select "File system" as target type.

   A new target is created and displayed in the detail area.

   Under "Destination path", you can see the path to the local main storage location for reports.
4. Assign a unique name to the target.
5. Under "Subfolder", enter the path to the subfolder in which the report is to be saved.

   Use the following notation: &lt;folder name&gt; or &lt;folder name&gt;\&lt;folder name&gt;\...
6. (Optional) Enter a comment.

**Note**

**Relative path information**

The path specification is relative to the local main storage location for reports.

##### Result

The target is available for selection when configuring report jobs.

When a report job with this target is being executed, the generated report is stored in the subfolder of the local main storage location defined as the target. If the folder entered under "Target path" does not exist, it is created by the system.

> **Note**
>
> **Change of the local main storage location for reports**
>
> When the local main storage location for reports changes, the targets are automatically adapted. New reports are stored relative to the new local main storage location. The old folders are not deleted.

#### Add a target with "File system" target type (Unified Panel) (RT Unified)

This section describes how to add a target with the "File system" target type on a Unified Comfort Panel in Runtime.

##### Introduction

A reporting job with a target of the "File system" target type saves reports to a file system.

When configuring the report jobs, you can choose from pre-configured and user-defined targets of this target type.

**Preconfigured targets**

The following targets with "File system" target type are pre-configured:

| Symbol | Meaning |
| --- | --- |
| Local project storage location | The reports are stored in the following folder: `<Project folder of the Runtime project>\``Reports` |
| Local main storage location | The reports are stored in the local main storage location for reports. The local main storage location is configured in TIA Portal in the Runtime settings of the HMI device.  If this setting has not been made in TIA Portal, the reports are stored in the following folder on the SD card plugged into the panel: `media/simatic/X51/Reports` |

You can select these targets in the "Report jobs" tab. You cannot edit or delete these targets in the "Job parameters &gt; Targets" tab.

**User-defined targets**

In the "Reports" control, you can create user-defined targets of the "File system" target type. These user-defined targets are always subfolders of the local main storage location.

##### Requirement

- The "Reports" control is placed on a process picture.
- The panel contains the storage media configured in the TIA Portal Runtime settings as storage locations for reports and for the reporting database.

##### Procedure

To add user-defined targets of the "File system" target type, follow these steps:

1. In the "Reports" control, click on the "Job parameters &gt; Targets" tab.
2. In the work area of the tab, click "Add new".
3. Select "File system" as target type.

   A new target is created and displayed in the detail area.

   Under "Destination path", you can see the path to the local main storage location for reports.
4. Assign a unique name to the target.
5. Under "Subfolder", enter the path to the subfolder in which the report is to be saved.

   Use the following notation: &lt;folder name&gt; or &lt;folder name&gt;\&lt;folder name&gt;\...
6. (Optional) Enter a comment.

**Note**

**Relative path information**

The path specification is relative to the local main storage location for reports.

##### Result

The target is available for selection when configuring report jobs.

When a report job with this target is being executed, the generated report is stored in the subfolder of the local main storage location defined as the target. If the folder entered under "Target path" does not exist, it is created by the system.

> **Note**
>
> **Change of the local main storage location for reports**
>
> When the local main storage location for reports changes, the targets are automatically adapted. New reports are stored relative to the new local main storage location. The old folders are not deleted.

### Configuring report tasks (RT Unified)

This section contains information on the following topics:

- [Creating a report job (RT Unified)](#creating-a-report-job-rt-unified)
- [Managing report jobs (RT Unified)](#managing-report-jobs-rt-unified)
- [Configuring report names (RT Unified)](#configuring-report-names-rt-unified)
- [Execution of report jobs (RT Unified)](#execution-of-report-jobs-rt-unified)

#### Creating a report job (RT Unified)

##### Introduction

A report job is a job for generating reports in Runtime. The configuration of a report job controls the details of the generation.

##### Requirement

- The "Reports" control is configured on a screen of the project.
- The following job parameters were configured in the control:

  - At least one template has been imported.
  - To automatically execute a report job: Triggers are configured in the "Job parameters &gt; Trigger" tab.
- For sending an email after execution of the report job:

  - Email contacts were configured in the global settings.
  - An SMTP server was configured in the global settings.
  - A target of the target type "E-mail" was configured in the "Job parameters &gt; Targets" tab.
- For a report job with the target format PDF:

  - Microsoft Office Excel or LibreOffice is installed on the runtime server.
  - Depending on whether Excel or LibreOffice is installed, the information required for PDF creation was provided during the Runtime installation or in the "WinCC Unified Configuration" tool.

##### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. Select "Add new" in the work area or click "Add new" in the toolbar.
3. In the detail area, enter a name for the report job.
4. Select a report template.
5. Configure the report name. See section [Configuring report names](#configuring-report-names-rt-unified).

   The configuration is applied to all reports generated by the report job.
6. Under "Targets", you determine how the reports are to be made available to users. Follow these steps:

   - Click "Add target".

     You see the targets configured in the tab "Job parameters &gt; Targets".
   - Select a target.
   - Add the target by clicking "+".

     The target is added to the table to define the target formats.

     ![Procedure](images/134910569739_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/134910569739_DV_resource.Stream@PNG-en-US.png)
   - Determine the formats in which the reports generated by the report job are provided for the target. In the table, activate the options of the desired formats for each target.
   - To remove a target from the report job, click the "Remove" button in the table.
7. Under "Trigger", select which event triggers the execution of the report job:

   - If the report job is only to be executed manually, select "Manual".
   - If the report job is to be executed automatically, select one of the other triggers configured under "Trigger".
8. (Optional) Enter a comment for the report job.
9. Specify whether the automatic execution of the report job is active or paused. To do this, set the slider "Enabled" or "Disabled".

**Note**

**Sending emails without a report**

If you deactivate both options for targets with "E-mail" target type, an email without attachment is sent after the report job has been executed.

**Note**

**PDF as target type**

Generating PDFs with Excel is significantly slower than with LibreOffice. To generate large PDF reports, it is therefore recommended that you install LibreOffice.

A PDF report created by LibreOffice can deviate in content or layout from a PDF report generated with Excel, for example, if the report template uses common Excel features that LibreOffice does not support, such as special fonts or chart types.

**Note**

You can also execute the report job manually.

**Note**

You can still execute disabled report jobs manually.

##### Result

The report job is saved automatically.

When its trigger occurs, the report job is executed. A report is generated and made available as configured under "Targets".

---

**See also**

[Execution of report jobs (RT Unified)](#execution-of-report-jobs-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)
  
[Add target with target type "E-mail" (RT Unified)](#add-target-with-target-type-e-mail-rt-unified)
  
[Add a target with "File system" target type (Unified PC) (RT Unified)](#add-a-target-with-file-system-target-type-unified-pc-rt-unified)
  
[Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)

#### Managing report jobs (RT Unified)

##### Requirement

- The "Reports" control is configured on a screen of the project.
- Report jobs have been configured in the control.

##### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. To edit a report job, proceed as follows:

   - Select the report job in the work area.
   - In the detail area, edit the settings of the report job.

     You have the same options as when creating a report job.
3. To delete report jobs, proceed as follows:

   - In the work area, enable the options next to the report job.
   - Click "Delete" in the toolbar.

#### Configuring report names (RT Unified)

> **Note**
>
> Make sure that the generated report name does not violate the policy of the operating system regarding the maximum length of file names.

##### Introduction

The default name of reports is `Report_{NNN}`.

To use different report names, enter one or more placeholders at the report job. The placeholders are combined to form the report name during execution of the report.

**Placeholder types**

Placeholders have one of the following types:

| Placeholder type | Description |  |
| --- | --- | --- |
| Text | For user-defined fixed texts |  |
| Counter | On automatic numbering | Dynamic placeholders  The placeholders are broken down into values during execution of the report. |
| Date format | For outputting the generation time |  |
| Tag | To output the process value of an online tag |  |

**Unique report names**

If the report name uses counter or date format placeholders, the report job generates unique report names.

##### Requirement

- The "Reports" control contains a screen of the runtime project that is running.

##### Procedure

You can enter the placeholders manually in the "Report name" field or you can have the software help you configure the report name.

To have the software help configure the report name, follow these steps:

|  |  |  |
| --- | --- | --- |
| 1. Select the "Report jobs" tab in the "Reports" control. 2. Select a report job in the work area.    You can see the settings for the report job in the detail area. 3. Next to "Report name", click "Configure".    You see the following operator controls:               ![Procedure](images/148826369803_DV_resource.Stream@PNG-en-US.png)         ![Procedure](images/148826369803_DV_resource.Stream@PNG-en-US.png)        |  |  |  |    | --- | --- | --- |    | ① | List for selection of the placeholder type |  |    | ② | Button for adding a placeholder of the selected type |  |    | ③ | Table for configuring or removing the placeholder |  |       |  |  |  |    | --- | --- | --- |    | **Note**  For the default report name, the "Report name" has the value `Report_{NNN}` and the table shows the placeholders "`Report_`" and "`NNN`". To swap the order of placeholders or to add a placeholder in the center, delete the placeholders and then add them in the desired order. |  |  | 4. Optional: To delete the default placeholders, click "x" in the placeholder table. 5. Select the desired type under "Select placeholder type".      |  |  |  |    | --- | --- | --- |    | **Note**  A report name can contain only one counter. |  |  | 6. Click "+".    An empty placeholder of the corresponding type is added at the end of the table. 7. Enter the placeholder under "Value" in the placeholder table.       | Placeholder type | Description | Example |    | --- | --- | --- |    | "Text" | Enter the text. | `Report_` |    | "Date format" | Enter a date placeholder. | A list of permitted placeholders and examples can be found in section [Dynamic placeholder](#dynamic-placeholder-rt-unified). |    | "Counter" | Enter a counter placeholder. |  |    | "Tag" | Enter the full name of an online tag. | `RT1_Brewery::BatchNo` |       |  |  |  |    | --- | --- | --- |    | **Note**  Enter the dynamic placeholders without any markup characters. |  |  |     Alternatively, you can select an online tag via the user interface. Follow these steps:    - Click the "..." button on the tag placeholder.    - In the "Tag selection" dialog, click the "Search" button.      You can see all the tags of the Runtime project that is running.        |  |  |  |      | --- | --- | --- |      | **Note**   **Scrolling and filtering**  Use the page navigation buttons to scroll forward or backward. To filter the displayed tags, enter a filter string in "Filter" and click "Search". You use the wildcard "*" to filter by partial strings. ​For example: - *T* returns all tags with a "T" in their name. - *T returns all tags that end in "T". - T* returns all tags that start with "T".​When filtering for structures, the separators must be part of the filter string. |  |  |                 ![Procedure](images/149794338187_DV_resource.Stream@PNG-en-US.png)           ![Procedure](images/149794338187_DV_resource.Stream@PNG-en-US.png)    - Click the desired tag.    - Confirm with "OK". |  |  |

In the "Report name" field, the placeholder you added is appended to the end of the report name.

##### Alternative procedure

To enter the placeholders manually, proceed as follows:

1. Select the "Report jobs" tab in the "Reports" control.
2. Select a report job in the work area.

   You can see the settings for the report job in the detail area.
3. Enter the desired combination of fixed texts and dynamic placeholders manually in the "Report name" field.

   Use markup characters for the dynamic placeholders. See section [Dynamic placeholder](#dynamic-placeholder-rt-unified).

Example:

| "Report name" value | Generated report name |
| --- | --- |
| `Report_{yyyymmdd}_{HHMMss}_{@PC1_Brewery::BatchNo}` | `Report_20190101_170001_BatchNo_87002314` |

##### Result

When generating a report, the dynamic placeholders are resolved and all placeholders are merged to form the report name.

If a process value contains a character that is not permitted in file names, it is replaced by an underscore.

If there is an error resolving the name, e.g. because the tag is not found in runtime, the tag placeholder in the name is replaced by `ERR`. The process is logged in the generation status of the report.

#### Execution of report jobs (RT Unified)

##### Automatic and manual execution

**Automatic execution**

Report jobs that have a tag trigger, serial trigger or context trigger and are set to active on the "Report jobs" tab are automatically executed when their trigger occurs.

**Manual execution**

Report jobs with a trigger of the "Manual" type must always be executed manually.

In addition, you can at any time manually execute report jobs that have a tag trigger, serial trigger or context trigger.

##### System response to errors

- Error adding the report job to the queue

  The execution of the report job is discarded. A system alarm documents the error.
- Error executing the job

  In the "Reports" control, "Reports" tab, the status icon indicates the error. A click on the icon opens a detailed status message.

  A system alarm documents the error.

---

**See also**

[Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)

### Running a report job manually (RT Unified)

You can execute report jobs manually at any time, regardless of their trigger type. This also applies to report jobs that were disabled in the "Report Jobs" tab and whose automatic execution is therefore paused.

#### Requirement

Report jobs have been configured in the "Reports" control.

#### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. In the work area, enable the option next to the report job that you want to execute manually.
3. Click "Execute" in the toolbar.

#### Result

The report is generated. You can download it in the "Reports" tab.

### Downloading reports (RT Unified)

You can download the reports stored by the report job in the file system to your device.

Depending on which file formats have been set in the report job, you can download the report as an XLSX file and as a PDF file.

#### Requirement

- Report jobs with the target type "File system" have been configured and executed in the "Reports" control.

#### Procedure

1. Select the "Reports" tab in the "Reports" control.
2. In the work area, select the option in the left column for each report that you want to download.
3. Enable the desired target formats in the "Files" column.
4. Click "Export" in the toolbar.

**Note**

**Generation status**

You are only offered successfully generated formats.

In the "Status" column you can check whether the generation for a format has failed. For a detailed status message click on the icon of a target format.

#### Result

The reports are downloaded into the download directory of the browser.

You can edit, distribute, or log the reports.

### Exporting an offline configuration file (RT Unified)

An offline configuration file is required to configure reporting templates in the Reporting Excel add-in without an online connection to the Runtime server.

#### Requirement

- The "Reports" control is placed on a screen of the project.
- The Runtime project has data that can serve as data source elements in the reporting template, such as alarms and logging tags.

#### Procedure

1. In the "Reports" control, click on the "Global settings &gt; Configuration" tab.
2. Enter the name of the offline configuration file under "Offline-configuration".
3. Click "Export offline configuration".

#### Result

A JSON file with the data source elements of the Runtime project is created. The file is downloaded to the download folder or a user-defined directory according to the device settings.

You can select the configuration file in the Reporting Excel add-in as data source for an offline connection.

### Transferring the control configuration (RT Unified)

You have the option of reusing the settings in the "Reports" control, for example, on a device in another network. To do this, export the existing configuration on the one device from the control to a ZIP file. Then import the file into a "Reports" control on the other device.

#### Scope

The transfer covers the following data:

- Global settings, without passwords and certificates
- Job parameters, including the report templates available in the control
- Report jobs

Reports are not transferred.

#### Requirement

- The "Reports" control is placed on a screen in the project running in Runtime.
- Export: Settings have been made, e.g. contacts maintained, report templates imported, and report jobs created in the "Reports" control.
- Import: You have access to the ZIP file generated by the export on the device on which Runtime is installed.

#### Export configuration

1. In the "Reports" control, select the "Global settings &gt; Configuration" tab.
2. Enter the name of the export file under "Export/import configuration &gt; Export".
3. Click "Export configuration".

The configuration is exported to a ZIP file and downloaded to the default download directory of the device.

#### Import configuration

1. In the "Reports" control, select the "Global settings &gt; Configuration" tab.
2. Click "Select import file" under "Export/import configuration".
3. Select the ZIP file in File Explorer and confirm your selection.
4. Runtime checks whether the control already contains configurations:

   - No: The configuration is imported.
   - Yes:

     Select "OK" to import the configuration. The existing configuration is overwritten.

     Select "Cancel" to cancel the import.

### Configuring enable paging (RT Unified)

To set how many entries the lists in the work area of the "Reports" control display per page, follow these steps:

1. In the "Reports" control, click on the "Global settings &gt; Configuration" tab.
2. Under "List Settings", select the number of entries.

If a list has more entries, these are split over several pages. Use the buttons below the list to switch pages.

> **Note**
>
> The setting is lost through a screen change.

### Inconsistencies and error diagnostics (RT Unified)

> **Note**
>
> Inconsistent report jobs are not executed.
>
> The templates available in the "Reports" control are not validated.

#### Display of inconsistencies and errors

Errors and inconsistencies are displayed as follows:

| Symbol | Meaning |
| --- | --- |
| In the control | If job parameters are affected.  Examples:  - No template is set for a report job. - A tag that triggers a report job is deleted in the engineering system. The project is reloaded into the device. |
| In the "Error log" worksheet of the report | Errors or inconsistencies affecting the content of the report.  Example: The report evaluates data from a tag that is no longer available in runtime. |
| As system alarm | For errors and inconsistencies that do not affect job parameters or the contents of the report.  Example: The ExecuteReport system function transfers a report job that does not exist. |

#### Job parameters

The following values lead to errors and inconsistencies:

| Parameter | Invalid values | Default setting |
| --- | --- | --- |
| "Name" | Zero, empty or already assigned name | "New report job" |
| "Template" | Zero, empty or "None".  Name of a template that is not imported | "None" |
| "Target name" | Zero or empty | "NewReportJob[NN]" |

### Dynamic placeholder (RT Unified)

#### Introduction

Dynamic placeholders are evaluated when the report job is executed and replaced with text in runtime.

The following job parameters can contain placeholders:

- Report name
- Targets with the target type "E-mail": Subject and text of the email

#### Dynamic placeholders for report names

Use dynamic placeholders for counters and/or dates to generate unique report names:

| Counter placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {N} | Automatic numbering | Rep_{N} | Rep_1 | 0...9 |
| {NN} | Rep_{NN} | Rep_01 | 00...99 |  |
| {NNN} | Rep_{NNN} | Rep_001 | 000...999 |  |

| Date placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {yy} | Current year | Rep_{yy} | Rep_18 | Valid year with 2 digits |
| {yyyy} | Rep_{yyyy} | Rep_2018 | Valid year with 4 digits |  |
| {m} | Current month | Rep_{m} | Rep_1 | Valid month, no prefixed 0 for months in single-digit range |
| {mm} | Rep_{mm} | Rep_01 | Valid month, prefixed 0 for months in single-digit range |  |
| {mmm} | Rep_{mm} | Rep_Jan | Month abbreviation with 3 characters |  |
| {mmmm} | Rep_{mmmm} | Rep_January | Month with full name |  |
| {d} | Current day of the month | Rep_{d} | Rep_1 | Valid day, no prefixed 0 for days in single-digit range |
| {dd} | Rep_{dd} | Rep_01 | Valid day, prefixed 0 for days in single-digit range |  |
| {ddd} | Rep_{ddd} | Rep_Mon | Day abbreviation with 3 characters |  |
| {dddd} | Rep_{dddd} | Rep_Monday | Day with full name |  |
| {h} | Current hour | Rep_{h} | Rep_1 | Current hour (12-hour clock), no prefixed 0 for single-digit values |
| {hh} | Rep_{hh} | Rep_01 | Current hour (12-hour clock), prefixed by 0 for single-digit values |  |
| {H} | Rep_{H} | Rep_13 | Current hour (24-hour clock), no prefixed 0 for single-digit values |  |
| {HH} | Rep_{HH} | Rep_13 | Current hour (24-hour clock), prefixed by 0 for single-digit values |  |
| {M} | Current minute | Rep_{M} | Rep_6 | Valid minute, no prefixed 0 for single-digit values |
| {MM} | Rep_{MM} | Rep_06 | Valid minute, prefixed by 0 for single-digit values |  |
| {s} | Current second | Rep_{s} | Rep_41 | Valid second, no prefixed 0 for single-digit values |
| {ss} | Rep_{ss} | Rep_41 | Valid second, prefixed by 0 for single-digit values |  |

Use a dynamic placeholder for tags to integrate process values in the report name:

| Tag placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {@&lt;Full  Tag name&gt;} | Process value of an online tag | Rep_{@PC1_LineA::MyTag1} | Rep_On | Process value of the online tags  If the value contains a character that is not permitted in file names, it is replaced by an underscore.  If there is an error resolving the name, e.g. because the tag is not found in runtime, the tag placeholder in the name is replaced by `ERR`. The process is logged in the generation status of the report. |

Examples:

| Definition with placeholder | Generated report name |
| --- | --- |
| LineA_{yyyymmdd}_{HHMMss} | LineA_20190101_170001 |
| LineA_{yymmmd}_{hhMMss} | LineA_19Jan1_050001 |
| LineA_{NNN} | LineA_014 |
| LineA_{yyyymmdd}_{HHMMss}_BatchNo_{@PC1_Brewery::BatchNo} | LineA_20190101_170001_BatchNo_87002314 |

#### Placeholder for email subject and email text

To integrate the report name into the subject line or the email text, use the following dynamic placeholder {ReportName}.

#### Markup

Use the following markup characters for dynamic placeholders:

- Placeholders for counter and date: `{}`
- Placeholders for tags: `{@}`

> **Note**
>
> There is no markup in the placeholder table for defining the report name. See also section [Configuring report names](#configuring-report-names-rt-unified).
