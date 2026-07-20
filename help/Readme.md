---
title: "Readme"
package: ReadMePE2MenUS
topics: 8
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Readme

This section contains information on the following topics:

- [Notes on TIA Portal](#notes-on-tia-portal)
- [STEP 7](STEP%207.md#step-7)
- [WinCC](WinCC.md#wincc)
- SIMOCODE ES
- SIMATIC Safe Kinematics (S7-1500, S7-1500T)
- SIMATIC Energy Suite readme
- Readme Building Automation
- [Startdrive](Startdrive.md#startdrive)
- SiVArc Readme
- SINUMERIK
- SINUMERIK WinCC Unified
- SIMOTION SCOUT TIA
- SINAMICS DCC
- [TIA Portal Version Control Interface](TIA%20Portal%20Version%20Control%20Interface.md#tia-portal-version-control-interface)

## Notes on TIA Portal

This section contains information on the following topics:

- [General notes](#general-notes)
- [Notes on libraries](#notes-on-libraries)
- [Notes on memory cards](#notes-on-memory-cards)
- [Notes on using TIA Portal in a virtual environment (private cloud)](#notes-on-using-tia-portal-in-a-virtual-environment-private-cloud)
- [Notes on using the TIA Portal Teamcenter Gateway](#notes-on-using-the-tia-portal-teamcenter-gateway)
- [Information on working with Multiuser Engineering](#information-on-working-with-multiuser-engineering)

### General notes

The information in this readme file supersedes statements made in other documents.

Read the following notes carefully because they include important information for installation and use. Read these notes prior to installation.

#### Information on TIA Portal in online support

Overview of the most important technical information and solutions for TIA Portal in the Siemens Industry online support.

Internet link: [TIA Portal in Siemens Industry online support](https://support.industry.siemens.com/cs/ww/en/view/65601780)

All information on service and support in the Siemens Industry online support:

Internet link: [Service and support in Siemens Industry online support](https://support.industry.siemens.com/cs/ww/en/)

Here, you can also subscribe to the newsletter that provides you with latest information relating to your products.

#### Collection of diagnostic and feedback data

We collect and process licensing information as well as statistical usage and diagnostic data, such as frequency of use of TIA Portal editors or functions to keep the TIA Portal secure and up-to-date, to detect, diagnose and remedy problems, and for product improvements.

The usage and diagnostic data is initially saved locally on your computer in readable format where you can view it. Storage location: "...\ProgramData\Siemens\Automation\TelemetryConnector\EventPersistence". (Note: The Windows administrator can set the folder so that it is visible.)

In a second step, the usage and diagnostic data is transferred to Siemens via secure communication for the purposes listed above.

The collection of usage and diagnostics data can be disabled in the TIA Portal settings.

When the setting is disabled, no data is collected on the computer and transferred to Siemens (except for the message to disable the setting).

When the setting is reactivated, the statistical usage data is collected again and transferred to Siemens. The collection and transmission of statistical usage data only takes place in the corresponding version of the TIA Portal. Data from other TIA Portal installations with disabled setting will not be collected and transferred after reactivation.

#### Improved search function in the information system

The search function has been improved with synonym recognition. When you search for a term, defined synonyms of the term are now also found.

#### Starting TIA Portal

When you start TIA Portal, Windows attempts to update the Certificate Revocation List (CRL) of "windowsupdate.com".

If no Internet access is available and there are multiple DNS servers, a timeout might occur and delay the start of TIA Portal.

#### Minimizing the risk of cyber threats

To minimize the risk of cyber threats, it is recommended to keep the Windows operating system including .NET and the VC++ redistributables up-to-date when working with the TIA Portal.

#### Installing new .Net versions or .Net service packs

- Close TIA Portal before installing a new .Net version or a new .Net service pack on your programming device/PC.
- Restart TIA Portal only after successful installation of the new .Net version or the new .Net service pack.

#### Display of Asian characters in TIA Portal

Texts in TIA Portal might not display correctly if you install a Chinese TIA Portal on another Asian operating system (for example, Korean). To view the texts in TIA Portal correctly, open the Windows Control Panel and select "English" under "Language for non-Unicode programs". Note, however, that this can cause display problems in other programs.

#### Entry of decimal places

With certain Windows language settings, it might occur that the entry of values with a comma as a decimal place is not recognized (entering "1,23" leads to an error). Instead, use the international format ("1.23").

#### Detection of devices in the network

Firewalls can block the PN DCP protocol that is used by the TIA Portal for the detection of devices in the network. Therefore, it is advisable to configure a rule in the firewall to enable the connection.

You can find detailed information on configuring a firewall rule, e.g. for McAfee Endpoint Security, under:

[https://support.industry.siemens.com/cs/ww/en/view/109762832](https://support.industry.siemens.com/cs/ww/en/view/109762832)

#### Opening projects with missing software components

If a project cannot be opened in TIA Portal due to missing software components, you can download and install it as trial software from Siemens Industry online support. You can then open the project. Note that the trial software can only be used for a limited period of time.

Use the following link to open the page in Siemens Industry online support, where the various software products are available to you as trial software: [www.siemens.com/tia-portal-trial](https://support.industry.siemens.com/cs/ww/en/view/109772992)

---

**See also**

[FAQ 109748887](https://support.industry.siemens.com/cs/ww/en/view/109748887)

### Notes on libraries

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Copying library elements

If master copies and types have the same name, the corresponding objects in the project are overwritten when the action "Copy" is used. Note that this takes place without a prompt. The same behavior occurs when the name of the master copy is different to the name of the type, but an object within the master copy has the same name as the type.

### Notes on memory cards

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### SIMATIC Memory Cards

The SIMATIC Memory Cards have been formatted and set up by Siemens for use with S7-1200 and S7-1500 modules. This format must not be overwritten; otherwise, the card will no longer be accepted by the modules. Formatting with Windows tools is therefore not permitted.

#### Behavior in case of open force job

Note that an active force job is retained even after you have loaded a new project to the SIMATIC Memory Card. This means you should first delete the active force job before you remove a SIMATIC Memory Card from the CPU and before you overwrite the card in the PC with a new project. If you use a SIMATIC Memory Card with unknown content, you should format the SIMATIC memory card before the next download.

#### Access protection for memory cards in USB card readers

By improving the security mechanisms for online access and engineering of S7-1500 CPUs, the data storage on memory cards has been changed. For this reason, this version of STEP 7 cannot evaluate the passwords of the configured protection level when reading project data from memory cards that is accessed via a USB card reader. The changed response affects the memory cards for CPUs of the S7-1200/1500 series. Therefore, use physical safeguards to protect critical project data on memory cards for these devices.

> **Note**
>
> This restriction is not related to online access to devices or the know-how protection of program blocks.

#### Removing/inserting the memory card

After removing or inserting a memory card, always perform a memory reset on the CPU in order to restore the CPU to a functional condition.

#### Access to current memory cards with older product versions

The format of memory cards is not backwards compatible with older product versions. This means that if you want to use a memory card from a current product version in an older product version, first delete the data from the memory card.

### Notes on using TIA Portal in a virtual environment (private cloud)

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Instructions for using TIA Portal in a virtual environment (private cloud)

You can find instructions on how to use TIA Portal in a virtual environment (private cloud) on the installation disk in the directory "Documents\Readme\&lt;language directory&gt;". You can open the PDF document "TIAPortalCloudConnectorHowTo&lt;language ID&gt;.pdf" here.

The TIA Portal Cloud Connector can be used with the Windows 7 (64-bit) and Windows 10 (64-bit) operating systems.

#### Environment variables "TiaUserSettingsPath" and "TiaDefaultProjectPath"

The environment variables "TiaUserSettingsPath" and "TiaDefaultProjectPath" can be used to set the location of the user and project settings different from the system default. This can be used, for example, to save the user and project settings at a central location.

You can find additional information on the use of environment variables in the Instructions on Using TIA Portal in a Virtual Environment (Private Cloud).

#### Self-signed certificates using HTTPS as communication protocol

Microsoft regularly checks whether the certificates in the Windows Certificate Store are from a trusted source. Certificates from untrusted sources are deleted. Therefore, ensure that your self-signed certificates are signed with a secure certificate.

### Notes on using the TIA Portal Teamcenter Gateway

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Installing the TIA Portal Teamcenter Gateway

You can find instructions for installing the TIA Portal Teamcenter Gateway in the TIA Portal Teamcenter Gateway online help under "Installing and uninstalling TIA Portal Teamcenter Gateway".

#### Using the TIA Portal Teamcenter Gateway

The installation of the TIA Portal Teamcenter Gateway gives you access to the TIA Portal Teamcenter Gateway function that is available as of TIA Portal V14 and higher.

#### Installing the TIA Portal Teamcenter Gateway - data model

- Teamcenter 12.x: You can find a description of installing the TIA Portal Teamcenter Gateway data model on the installation data medium in the directory "\Support\Teamcenter_12\ServerSetupDocument\" on the STEP 7/WinccA_pro_DVD2. Open the PDF document "Datamodel_Installation_enUS". The instructions for installing the TIA Portal Teamcenter Gateway data model are only available in English.
- Teamcenter 13.x: You can find a description of installing the TIA Portal Teamcenter Gateway data model on the installation data medium in the directory "\Support\Teamcenter_13\ServerSetupDocument\" on the STEP 7/WinccA_pro_DVD2. Open the PDF document "Datamodel_Installation_enUS". The instructions for installing the TIA Portal Teamcenter Gateway data model are only available in English.
- Teamcenter 14.x: You can find a description of installing the TIA Portal Teamcenter Gateway data model on the installation data medium in the directory "\Support\Teamcenter_14\ServerSetupDocument\" on the STEP 7/WinccA_pro_DVD2. Open the PDF document "Datamodel_Installation_enUS". The instructions for installing the TIA Portal Teamcenter Gateway data model are only available in English.

#### Updating the existing TIA Portal Teamcenter Gateway data model

- Restart TIA Portal after updating the existing TIA Portal Teamcenter Gateway data model.
- In the TIA Portal Teamcenter Gateway V19, changes were made to the existing TIA Portal Teamcenter Gateway data model. You can find a description for installing the TIA Portal Teamcenter Gateway data model on the installation medium in the directory "\Support\Teamcenter_14\ServerSetupDocument\" on the STEP 7/WinCC DVD2.
- In the TIA Portal Teamcenter Gateway V17, changes were made to the existing TIA Portal Teamcenter Gateway - data model. You can find a description for installing the TIA Portal Teamcenter Gateway data model on the installation medium in the directory "\Support\Teamcenter_12\ServerSetupDocument\" on the STEP 7/WinCC DVD2.
- In the TIA Portal Teamcenter Gateway V15 and V15.1, no changes were made to the existing TIA Portal Teamcenter Gateway data model and no changes specific to the Teamcenter as well.

#### Notes on Teamcenter

To work with the TIA Portal Teamcenter Gateway, Teamcenter Rich Application Client (RAC) or Teamcenter Client Communication System (TCCS) as of version 12.2 must be installed on your PG/PC.

#### Note on TCCS (Teamcenter Client Communication System)

If you have completed the installation of TCCS (Teamcenter Client Communication System) as a "standalone" installation, you also need to install "Microsoft Visual C++ 2013 – Redistributable".

#### Note on UTF-8

In order to display data from Teamcenter with non-English character sets, e.g. for Asian languages, in TIA Portal, Unicode character sets need to be used.

#### Note on cloud computing

If you run TIA Portal in a Cloud (for example virtual machine), this system has to be integrated into the Teamcenter environment. Direct integration via a remote connection is not supported by TIA Portal Teamcenter Gateway.

#### Basic information on working with TIA Portal Teamcenter Gateway

1. As of TIA Portal Teamcenter Gateway version V19, you can open TIA Portal projects, global libraries, program blocks and PLC data types (UDTs) from the Teamcenter Active Workspace Client (AWC) in TIA Portal.
2. As of TIA Portal Teamcenter Gateway version V18, you can link "Non-TIA objects", e.g. motors, plant objects, etc., to TIA Portal objects.
3. As of TIA Portal Teamcenter Gateway version V18, you can navigate from objects in Teamcenter to TIA Portal.
4. As of TIA Portal Teamcenter Gateway version V18, you can create TIA Portal object structures as new item when saving.
5. As of TIA Portal Teamcenter Gateway version V18, you can save internal data of a TIA Portal project as a separate unit under an item or revision in Teamcenter with "Save as new item..." or "Save as new revision...".
6. As of TIA Portal Teamcenter Gateway version V17, the Teamcenter operation "Open in TIA Portal" is available for TIA Portal projects.
7. As of TIA Portal Teamcenter Gateway version V15, the Teamcenter operation "Teamcenter &gt; Export..." is available for TIA Portal projects and global libraries. With this operation, you create a copy of the current project, which is completely free of any Teamcenter information. If you need to separated from Teamcenter, use this operation instead of the "Save as" operation because "Save as" retains Teamcenter information in the project.

#### Connecting to Teamcenter

As of TIA Portal Teamcenter Gateway V15.1 Update 3, you can establish a connection between TIA Portal and Teamcenter both via HTTP and via HTTPS.

#### Teamcenter version information

In order to work with the TIA Portal Teamcenter Gateway version **V.xx.x.x.x** and Teamcenter version **Vyy or Vyy.y** , Teamcenter version **Vzz.z.z.z** must be installed.

| TIA Portal Teamcenter Gateway version V.xx.x.x.x | Teamcenter version Vyy or Vyy.y | Required Teamcenter version Vzz.z.z.z |
| --- | --- | --- |
| TIA Portal Teamcenter Gateway **V19.0.0.0** | Teamcenter version **V14, V14.1, V14.2.2, V14.3** | Teamcenter version **V14.0.0.0, V14.1.0.0, V14.2.2.0, V14.3.0.0** |
| TIA Portal Teamcenter Gateway **V18.0.0.0** | Teamcenter version **V14** | Teamcenter version **V14.0.0.0** |
| TIA Portal Teamcenter Gateway **V18.0.0.0** | Teamcenter version **V13, V13.1, V13.2, V13.3** | Teamcenter version **V13.0.0.0, V13.1.0.0, V13.2.0.0, V13.3.0.0** |
| TIA Portal Teamcenter Gateway **V18.0.0.0** | Teamcenter version **V12.4, V12.3, V12.2** | Teamcenter version **V12.4.0.0**, **V12.3.0.0**, **V12.2.0.0** |
| TIA Portal Teamcenter Gateway **V17.0.0.0** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0** |
| TIA Portal Teamcenter Gateway **V17.0.0.2** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4,**     **V13, V13.1, V13.2, V13.3** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0,**     **V13.0.0.0, V13.1.0.0, V13.2.0.0, V13.3.0.0** |
| TIA Portal Teamcenter Gateway **V17.0.0.5** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4,**     **V13, V13.1, V13.2, V13.3,**    **V14.0** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0,**     **V13.0.0.0, V13.1.0.0, V13.2.0.0, V13.3.0.0,**    **V.14.0.0.0** |
| TIA Portal Teamcenter Gateway **V16.0.0.0** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4,** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0** |
| TIA Portal Teamcenter Gateway **V16.0.0.3** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4,**    **V13** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0,**     **V13.0.0.0** |
| TIA Portal Teamcenter Gateway **V15.1.0.0** | Teamcenter version **V11.2, V11.3, V11.4, V11.5** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0** |
| TIA Portal Teamcenter Gateway **V15.1.0.3** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,** |
| TIA Portal Teamcenter Gateway **V15.1.0.4** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0** |
| TIA Portal Teamcenter Gateway **V15.1.0.6** | Teamcenter version **V11.2, V11.3, V11.4, V11.5, V11.6.0.5*,**    **V12.2, V12.3, V12.4,**    **V13** | Teamcenter version **V11.2.0.0, V11.3.0.0, V11.4.0.0, V11.5.0.0, V11.6.0.5*,**    **V12.2.0.0, V12.3.0.0, V12.4.0.0**    **V13.0.0.0** |
| TIA Portal Teamcenter Gateway **V15.0.0.0** | Teamcenter version **V11.2, V11.3** | Teamcenter version **V11.2.0.0, V11.3.0.0** |
| TIA Portal Teamcenter Gateway **V14.0.0.0** | Teamcenter version **V11.2** | Teamcenter version **V11.2.0.0** |
| TIA Portal Teamcenter Gateway **V14.0.0.1** | Teamcenter version **V11.2** | Teamcenter version **V11.2.0.0** |
| * To work with the TIA Portal Teamcenter Gateway version V15.1 or the TIA Portal Teamcenter Gateway version V16 and Teamcenter version **V11.6**, it is a prerequisite that you have Teamcenter version **V11.6.0.5** or higher installed. As of the Teamcenter version **V11.6.0.5**, improvements have been that allow it to work smoothly with Teamcenter version **V11.6**. |  |  |

As of the TIA Portal Teamcenter Gateway version V16, working with the Teamcenter version **V12.2.0.0.0** is supported.

From TIA Portal version V18 and higher, Teamcenter version V11 will no longer be supported.

In order to work with Teamcenter version V11.6.0.0, the prerequisite is that you have Teamcenter version V11.6.0.5 or higher installed.

#### Setting the TIA Portal Teamcenter Gateway cache path

By default, the value entered under "Options &gt; Settings &gt; General &gt; Teamcenter Gateway" in the "TIA Portal Teamcenter Gateway Cache Path" area is taken as "TIA Portal Teamcenter Gateway Cache Path".

By default, this value refers to the project directory path.

If you change the value of the "TIA Portal Teamcenter Gateway Cache Path", Teamcenter Gateway checks the validity of the values entered by default and the changed values.

> **Note**
>
> The default value must not be empty.

#### Performing TIA Portal Teamcenter Gateway operations while WinCC Professional Simulation is running

Do not perform Teamcenter Gateway operations, such as "Check in" or "Undo check out" during a started WinCC Professional Simulation.

### Information on working with Multiuser Engineering

#### Contents

Information that could not be included in the online help and important information about product features of Multiuser Engineering and about the project server.

The installation of the project server enables you to use the "Multiuser Engineering", "Multiuser Commissioning" and "Exclusive Engineering" functions available with the corresponding TIA Portal.

#### Multiuser Engineering: Name changes

Compared with predecessor versions, the following name changes have been made in the context of Multiuser Engineering in newer TIA Portal versions:

| Name in predecessor versions | New name | Changed as of |
| --- | --- | --- |
| TIA Project Server | TIA Project Server  Short form: Project server | TIA Portal V18 |
| Multiuser server | TIA Project Server | TIA Portal V16 |
| Local Multiuser server | Local project server | TIA Portal V16 |
| Multiuser server project | Server project | TIA Portal V16 |
| Multiuser network profiles | Network profiles | TIA Portal V16 |
| Multiuser Administrative Tools | Project Server Administrative Tools | TIA Portal V18 |
| Multiuser Power Tools | Project Server Power Tools | TIA Portal V18 |

**TIA Project Server**

The project server can be used for Multiuser Engineering, and also for Multiuser Commissioning and Exclusive Engineering

There are no functionality restrictions between the project server V16 and the Multiuser server V15.1.

The functionality of the server remains unchanged depending on the version.

The project server is backward compatible with the multiuser server V14.

**Command line tools**

In TIA Portal V18 and higher, the "Multiuser Power Tools" and "Multiuser Administrative Tools" have been renamed to "Project Server Power Tools" and "Project Server Administrative Tools", respectively.

Use the "pspt" and "prjsrv" commands in the commands.

If you are working with project servers from versions prior to TIA Portal V18, use the commands "mupt" and "musrv" in the commands.

#### Microsoft system account for project server

When the project server is installed, a Microsoft system account is created for the project server.

Microsoft changes the password cyclically for this account.

If the password for this account has expired, the password needs to be changed and then the project server needs to be restarted.

#### Error message when starting the project server

If you get an error message during or after installing the project server stating that the service for the project server cannot be started, the following procedure is recommended:

1. Open the Windows event view and check whether an error entry with the error number "1069" is present.
2. If this is the case, information on how to proceed is provided below.

   Internet link: [FAQ with ID 109739926](https://support.industry.siemens.com/cs/ww/en/view/109739926)
3. Alternatively, you can contact Customer Support directly.

   Internet link to Customer Support: [TIA Portal in Siemens Industry online support](https://support.industry.siemens.com/cs/ww/en/view/65601780)

#### Working with active monitoring jobs and forcing jobs in the local session

Active monitoring jobs and forcing jobs must be closed before a check-in or update in the local session.

It is not possible to check in or update in the local session while monitoring or forcing jobs are active.

#### Working in the local session with the "Keep local session" option

If the "Keep local session" option is selected after the check-in, all checked-in objects in the local session appear as outdated, even if their content is identical.

#### Working with different versions of TIA Portal

Local sessions created with &lt;x.y&gt; version of TIA Portal can only be worked on with this version.

Example: A local session created with TIA Portal V17 as part of a V17 project cannot be edited with an earlier version of TIA Portal.

#### Working with Multiuser Commissioning

- When you work with Multiuser Commissioning, a new revision of the server project is created after each download to the CPU.

  However, a new revision is not created when objects that cannot be marked have been edited in the local session.

  Changes to objects that cannot be marked are lost during check-in and are not downloaded to the CPU.
- When you start the download to the device from the project tree with the menu command "Download to device &gt; Hardware configuration" in commissioning mode, the dialog informing you that different data exists on the CPU and in the server project is always displayed.
- When you work in Commissioning mode, only S7-1500 CPUs are fully supported.

  When using an S7-300/400 CPU, the dialog which informs you that different data exists on the CPU and in the server project is always displayed in Commissioning mode. The reason is that S7-300/400 CPUs do not support synchronization.

  To prevent this message from being displayed, disable the "Check for different data before download (recommended)" option in the Administration tool.

---

**See also**

[TIA Portal in Siemens Industry online support](https://support.industry.siemens.com/cs/ww/en/view/65601780)
  
[FAQ with ID 109739926](https://support.industry.siemens.com/cs/ww/en/view/109739926)
