---
title: "Readme TIA Portal Openness"
package: ReadmeTIAPortalOpennessenUS
topics: 5
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Readme TIA Portal Openness

This section contains information on the following topics:

- [Deprecated features in TIA Portal Openness](#deprecated-features-in-tia-portal-openness)
- [Readme](#readme)
- [Major changes for long-term stability in TIA Portal Openness V19](#major-changes-for-long-term-stability-in-tia-portal-openness-v19)
- [Hints for writing long-term stable code](#hints-for-writing-long-term-stable-code)

## Deprecated features in TIA Portal Openness

### Introduction

In general, TIA Portal Openness follows a long-term stable API strategy. There are isolated situations where APIs must be reworked:

**Terminology:**

| Product release | TIA Portal Openness version |  |
| --- | --- | --- |
| TIA Portal V18 | API V15.1 | old API |
| API V16 | old API |  |
| API V17 | old API |  |
| APIV18 | new API |  |
| TIA Portal V19 | API V16 | old API |
| API V17 | old API |  |
| API V18 | old API |  |
| APIV19 | new API |  |

### Static object model parts

Deprecated features are announced for an API version and will be removed in the next API version of the product. The old APIs in the next product release are not affected.  
For static object model parts, deprecated features are marked as obsolete. Using those features in code generates a compiler warning, but they still work in that version.  
Example of a compiler warning:

![Static object model parts](images/170499684491_DV_resource.Stream@PNG-en-US.png)

Example of highlighted obsolete features in code:

private static void ExportCertificate(Siemens.Engineering.Security.Certificate certificate)

{

FileInfo fileInfo = new FileInfo($"C:\\Temp\\{certificate.SubjectCommonName}.cer");

certificate.Export(fileInfo, Siemens.Engineering.Security.CertificateExportFormat.Cer);

}

clipboard

Consider adapting deprecated code as follows.

### Deprecated in API V18

- Class: Siemens.Engineering.AddIn.VersionControl.InitialPreExportInfo  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.PreExportInfo
- Class: Siemens.Engineering.AddIn.VersionControl.InitialPostExportInfo  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.PostExportInfo
- Class: Siemens.Engineering.AddIn.VersionControl.SyncPreExportInfo  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.PreExportInfo
- Class: Siemens.Engineering.AddIn.VersionControl.SyncPostExportInfo  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.PostExportInfo
- Class: Siemens.Engineering.AddIn.VersionControl.VciInitialExportAddInContext  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.ExportContext
- Class: Siemens.Engineering.AddIn.VersionControl.VciSyncExportAddInContext  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.ExportContext
- Class: Siemens.Engineering.AddIn.VersionControl.VciRepositoryAddIn  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.VciWorkspaceRepositoryAddIn
- Class: Siemens.Engineering.AddIn.VersionControl.VciRepositoryAddInProvider  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.VciWorkspaceRepositoryAddInProvider
- Class: Siemens.Engineering.AddIn.VersionControl.VciInitialExportSupport  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.ExportWorkflowSupport
- Class: Siemens.Engineering.AddIn.VersionControl.VciSyncExportSupport  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.ExportWorkflowSupport
- Class: Siemens.Engineering.AddIn.VersionControl.VciWorkflowAddInSupport  
  Deprecated and substituted by Siemens.Engineering.AddIn.VersionControl.VciWorkspaceRepositoryWorkflowAddIn
- Class: Siemens.Engineering.HmiUnified.RuntimeSettings.HmiRuntimeSetting

| Deprecated property | Relocated |
| --- | --- |
| OperateAsOpcServer { get; set; } | Moved to class Siemens.Engineering.HmiUnified.RuntimeSettings.HmiOpcUaServerRuntimeSettings |

- Class: Siemens.Engineering.HmiUnified.UI.Parts.HmiTrendPartBase

| Deprecated property | Relocated |
| --- | --- |
| TrendMode { get; set; } | Moved from base class to derived classes Siemens.Engineering.HmiUnified.UI.Parts.HmiTrendPart and Siemens.Engineering.HmiUnified.UI.Parts.HmiFunctionTrendPart |

- Class: Siemens.Engineering.SiVArc.ScreenRule

| Deprecated property | Deprecated |
| --- | --- |
| ScreenLibraryItem { get; set; } | Deprecated without substitution. |

### Deprecated in API V19

- Class: Siemens.Engineering.HW.MulticastableTransferArea

| Deprecated property | Substituted by |
| --- | --- |
| Siemens.Engineering.HW.Address Address { get; } | Siemens.Engineering.HW.AddressComposition Addresses { get; } |

- Class: Siemens.Engineering.Security.Certificate

| Deprecated method | Substituted by |
| --- | --- |
| System.Void Export(System.IO.FileInfo filePath, Siemens.Engineering.Security.CertificateExportFormat exportFormat) | System.Void Export(System.IO.FileInfo filePath) |

- Enum: Siemens.Engineering.Security.CertificateExportFormat  
  Deprecated without substitution
- Enum: Siemens.Engineering.HW.WebserverUserPermissions2  
  Deprecated without substitution
- Enum: Siemens.Engineering.HW.MaximumBufferedReceivedFrames  
  Deprecated without substitution
- Enum: Siemens.Engineering.HW.PortType  
  Deprecated and substituted by Siemens.Engineering.HW.PortConfiguration
- Exception class: Siemens.Engineering.SimaticMLVersionNotSupportedException  
  Deprecated without substitution

### Dynamic API parts

Deprecated features are announced for a TIA Portal version and will be removed in the next TIA Portal version. The old APIs and new API in the next product release are affected.  
For dynamic API parts, a compiler warning cannot be generated for technical reasons. Consider the system manual for deprecated features in that area.  
Example of a dynamic API part:

private static ulong GetPortValue(Siemens.Engineering.HW.DeviceItem item)

{

const string attributeName = "PortType";

ulong attributeValue = (ulong)item.GetAttribute(attributeName);

return attributeValue;

}

clipboard

Consider adapting deprecated code as follows

### Deprecated in TIA Portal V18 (all API versions)

**Hardware parameter in 6ES7148-6JG00-0BB0/V5.1**

| Deprecated attribute name | Substituted by |
| --- | --- |
| PortType | PortConfiguration |

## Readme

### Security measures for TIA Portal Openness applications

It is recommended

- to install a TIA Portal Openness application with admin rights to the programs folder.
- to avoid the dynamical loading of program parts like assemblies or dlls from the users area.
- to run the TIA Portal Openness application with user rights.

### Hardware parameters

A description of hardware parameters is available in the installation folder of TIA Portal at Siemens\Automation\Portal V*\PublicAPI\V*\HW Parameter Description\Openness_hardware_parameter_description.pdf

Attributes can have dependencies and influence each other. Therefore, if an attribute of a device item or channel has been changed, all attributes of the device item or channel must be verified.

> **Note**
>
> V* refers to adapted path according to the installed version of TIA Portal.

### Copying a TIA Portal Openness application

When you copy an executable TIA Portal Openness application, it may occur under certain circumstances that the directory path in which the TIA Portal Openness application was originally created is read out by the TIA Portal Openness application.

**Remedy:**

If you have copied the TIA Portal Openness application to a new directory, open and close the properties dialog to update the Windows cache.

### Support of specific features in a TIA Portal project

**Failsafe**

When you are using TIA Portal Openness there are restrictions regarding failsafe. Please consider the documentation "SIMATIC Safety - Configuring and Programming" for further information.

**Test Suite**

Openness Support for TIA Portal Test Suite is documented in the respective online help from Test Suite V19

### Improvement of the TIA Portal Openness performance

To achieve the maximum performance of TIA Portal Openness you can switch off the global search feature of the TIA Portal. To switch off the global search use the GUI or the TIA Portal Openness API call. When the TIA Portal Openness application is finished the global search could be switched on again. Although this is improving the performance, all TIA Portal Openness features work fine even with global search switched on.

### Thread-safe program code

Take care that your code is thread-safe, an event appears in a different thread.

### Export behaviour of screen items with style enabled

Export of a screen items with style enabled will not export the attributes of the style item, but those of the screen item before activating the style. If a style is selected and UseDesignColorSchema for the screen item is checked, the screen item fetches the attribute values from the style in the user interface but the attribute values of the screen item that were set before selecting the style are still stored in the database for this screen item. TIA Portal Openness exports these actual values that are stored in the database.

After disabling and enabling the style and exporting the screen item again, the same attribute values will be exported for the screen item like in the style item. If UseDesignColorSchema is unchecked, the attribute values of the selected style item are saved to the database for that screen item.

This problem can be solved by following the steps below:

1. Associate the screen item to the style item:

   - The database contains the attribute values before activating the style.
   - The user interfaces fetches attributes from the style item directly.
2. Export the screen item associated to the style item:

   - The XML file contains the attribute values from the database which are those before activating style.
3. Disable the UseDesignColorSchema:

   - The attribute values of style item are written in the attributes of the screen item in the database.
4. Enable the UseDesignColorSchema:

   - The attribute values of the screen item in the database are not changed and are still the ones from 3.
   - The user interfaces fetches attributes from the style item directly.
5. Export the screen item associated to the style item:

   - The XML file contains the attribute values from the database which were set at step 3, which are the same as the values in the style item.

### Importing ASi slaves via AML

If one of the following ASi slaves is imported via an aml-file the firmware version of the device item will be set to V13.0 in all cases:

- ASIsafe FS400 RCV-B: 3SF7 844-*B***-***1
- ASIsafe FS400 RCV-M: 3SF7 844-*M***-***1
- ASIsafe FS400 TRX-M: 3SF7 844-*M***-**T0
- ASIsafe FS400 RCV-C: 3SF7 844-*T***-***1

### Exporting and importing function keys

Function keys are synchronized during the import. If a function key is created in the global screen and the key is empty in the screen, the corresponding function key will use the global definition in all screens.

If you want to disable the global use of function keys after the import, define empty keys in the screens and import the screen types in the following order: Global screen, templates, screens.

If you want to ensure when exporting the screens that the global definition of a function key is not used by the template or by the global screen, create an empty function key in the screen. Select the required function key in the screen, then enable the "Use global assignment" property and disable it again.

### Accessing a device while Online

Writing attributes of a device that is Online is not supported. Reading attributes is supported.

Disconnecting a subnet is not supported when the device is online.

### Instance-specific attributes when importing blocks via TIA Portal Openness

In certain situations, the import rules can mean the loss of instance-specific attributes, such as start values, for example.

### Writing access for OB block priority attribute

The Priority attribute name for write access for OB block is changed to PriorityNumber.

### **Information on specific features**

Please See FAQ entries in Siemens Industry Online Support for further information concerning the following Openness functionalities:

- Archive/retrieve project
- Export/import watch tables

---

**See also**

[Test Suite V18](https://support.industry.siemens.com/cs/ww/en/view/109813414)

## Major changes for long-term stability in TIA Portal Openness V19

### Changes

If you have considered the hints concerning programming across versions and do not rebuild your Openness application to V19, your application will run without any restrictions on any computer even if only a TIA Portal V19 is installed.

If you rebuild your Openness application to V19, it is necessary to recompile your application using the Siemens.Engineering.dll of V19. In some cases, it might be necessary to adapt the code of your application.

### CAx/AML Data exchange

**Changes in behaviour of command line facility**

With TIA Portal V19 onwards, the command line facility for CAx export and import is no longer available to the user.

**Change in behaviour of Profinet / Ethernet port handling**

With TIA Portal V19 onwards, Label value for Profinet / Ethernet interface ports would be exported without space irrespective its value in TIA Portal. For example: If Label = P1 R, AML file would have Label = P1R

**Change in behavior of IO Link port handling**

With the TIA Portal V18 Update 2 onwards, IO Link port shall be exchanged with Label value as 'C/Q&lt;n&gt;' where n is the port number. for example: C/Q1, C/Q2 etc.,   
For AML exchange of IO Link configuration in TIA Portal V18 Update 2 (via S7-PCT), use "S7-PCT 3.5 SP3 Update 3" version or higher.

### WebServerUserManagement

**Changes in behaviour of removal/disable of existing Openness services**

With the TIA Portal V19, the Centralized UMAC functionality will be active, but the WebServerUserManagement will be disabled for all PLC firmware versions from V3.1 onwards.

However, until TIA Portal V18, the WebServerUserManagement will be operational, while the Centralized UMAC functionality will be inactive for PLC firmware versions up to V3.0.

### UMAC on PLC

**Changes in behaviour of online legitimation call via UMAC on PLC**

If the Openness application is running with a TIA Portal Openness API &lt;= 18, the online legitimation via Openness is still possible via the download and upload configurations. But only if the used PLC is protected by a legacy ProtectionLevel legitimation.

With TIA Portal Openness API &gt;= V19, all legitimation calls, especially the new UMAC on PLC, will be delivered to the event handler of the online legitimation event of the ConnectionConfiguration class. In case the OnlineAuthenticationConfiguration type is not handled there by the user code, there will be a second call to the callback method of the particular feature (e.g., download or upload). But there only the old protection mechanisms (until V18) can be handled.

### Enforcement of strict password policies

**Changes in behaviour of strict password policies for know how protection of blocks**

With TIA Portal V19, the Strict password policies are applied while setting a password. This also applies to TIA Portal Openness calls, especially setting know-how protection. An exception will be thrown if the password does not follow the policy.

### WinCC Unified Screen Editor

**Changes in behaviour of MultilingualText items in context to WinCC Unified Screen Editor**

All MultilingualText items are changed from unformatted to formatted in scope of the WinCC Unified Screen Editor since TIA Portal V18.  
This means all texts must be set formatted from now on. Plain text will be rejected by throwing an exception. for example:

Language language = project.LanguageSettings.Languages.Find(new CultureInfo("en-US"));

MultilingualText multilingualToolTipText1 = ((HmiButton)screenItem1).ToolTipText;

MultilingualTextItem multilingualTextItem1 = multilingualToolTipText1.Items.Find(language);

multilingualTextItem1.Text = "&lt;body&gt;&lt;p&gt;Modified button text from Openness&lt;/p&gt;&lt;/body&gt;";

clipboard

### Support of Blocks/UDTs

**Changes in schema to support NamedValueTypes usage in Blocks**

In TIA Portal V19, the support for Named Value Types has been introduced (only for Software Units in S7-1500 PLCs).  
In Openness, a new scope "NamedValueConstant" is introduced in the SimaticML schema from V19 to support the usage of a Named Value Type in Program Blocks or PLC Data Types.  
The Named Value Types which are used in PLC programming artifacts (Program Blocks, PLC Data Types) are visible in the new scope "NamedValueConstant" during import/export via SimaticML.

&lt;Access Scope="NamedValueConstant" UId="27"&gt;

&lt;Constant Name="_.siemens.simatic.Named_value_type_1#UNDEFs" UId="28"/&gt;

&lt;/Access&gt;

&lt;Token Text=";" UId="31"/&gt;

&lt;NewLine Num="2" UId="32"/&gt;

clipboard

## Hints for writing long-term stable code

### Version change

If you consider some hints for writing long-term stable code you will be able to use your application with other versions of the TIA Portal without modifying the code of your application.

> **Note**
>
> V* and *.ap* in document refer to the adapted path and extension according to the installed version of the TIA Portal.

### Registry path and appconfig file

Modifications are necessary to change registry path and application configuration file, for instance:   
“C:\Program Files\Siemens\Automation\Portal V14\PublicAPI\V14 SP1\Siemens.Engineering.dll”   
has to be changed to  
“C:\Program Files\Siemens\Automation\Portal V*\PublicAPI\V*\Siemens.Engineering.dll”

To write long-term stable code, the registry path should be configurable and the application configuration file must be updated.

### Installation path

Modifications are necessary to change the installation path of TIA Portal, for instance:  
“C:\Program Files\Siemens\Automation\Portal V14\PublicAPI\V14 SP1\Siemens.Engineering.dll”  
has to be changed to   
“C:\Program Files\Siemens\Automation\Portal V*\PublicAPI\V*\Siemens.Engineering.dll”

To write long-term stable code, the installation path should be configurable.

### Extensions of TIA Portal project files and libraries

Modifications are necessary to change the extensions of TIA Portal project file and of libraries, for instance:  
*.ap14  
has to be changed to   
*.ap*

To write long-term stable code, the extensions of TIA Portal project files and libraries should be configurable.

### Opening a project

To write long-term stable code, the `Projects.OpenWithUpgrade` method should be used instead of the `Projects.Open` method.

### Hierarchy of results

The hierarchy and/or the order of result classes e.g. compile result, might change across versions.

To write long-term stable code, you should avoid making assumptions about the depth and order of specific results.

The class layout is actually considered long term stable, mention explicit type names CompilerResult, CompareResult, DownloadResult, UploadResult. There is also a new results class: TransferResult. Content, hierarchy and order follow what is presented on the TIA Portal user interface of the currently executed or installed TIA Portal.
