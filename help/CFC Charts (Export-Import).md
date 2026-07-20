---
title: "CFC Charts (Export/Import)"
package: ImExCFCOpennessenUS
topics: 10
source: Siemens TIA Portal Information System (offline help, en-US)
---


# CFC Charts (Export/Import)

This section contains information on the following topics:

- [Export/Import of CFC charts](#exportimport-of-cfc-charts)
- [TIA Portal project view: Exporting and importing CFC charts](#tia-portal-project-view-exporting-and-importing-cfc-charts)
- [Exporting CFC charts](#exporting-cfc-charts)
- [Exporting only selected CFC charts](#exporting-only-selected-cfc-charts)
- [Importing CFC charts](#importing-cfc-charts)
- [Setting a password for CFC charts](#setting-a-password-for-cfc-charts)
- [Reading the password from CFC charts](#reading-the-password-from-cfc-charts)
- [Changing a password for CFC charts](#changing-a-password-for-cfc-charts)
- [Removing a password from CFC charts](#removing-a-password-from-cfc-charts)

## Export/Import of CFC charts

The TIA Portal Openness API supports the export and import of charts that are created with STEP 7 CFC ("Continuous Function Chart").

You can export and import all charts as XML files, or export only selected charts.

You call these functions for defined tasks outside the TIA Portal by means of the Public API.

> **Note**
>
> **Recommended PC hardware**
>
> If you are working with large projects, check that the computer meets the TIA Portal hardware requirements:
>
> - RAM:
>
>   32 GB for large projects

### Functions

The following functions are available for CFC charts:

- [Exporting CFC charts](#exporting-cfc-charts)
- [Exporting only selected CFC charts](#exporting-only-selected-cfc-charts)
- [Importing CFC charts](#importing-cfc-charts)
- Configuring chart passwords:

  - [Setting a password for CFC charts](#setting-a-password-for-cfc-charts)
  - [Reading the password from CFC charts](#reading-the-password-from-cfc-charts)
  - [Changing a password for CFC charts](#changing-a-password-for-cfc-charts)
  - [Removing a password from CFC charts](#removing-a-password-from-cfc-charts)

The function descriptions contain code samples that you can adapt to your openness program.

### Security measures for TIA Portal Openness applications

It is recommended

- to install a TIA Portal Openness application with admin rights to the programs folder.
- to avoid the dynamical loading of program parts like assemblies or dlls from the users area.
- to run the TIA Portal Openness application with user rights.

> **Note**
>
> Siemens is not liable for and does not guarantee the compatibility of the data and information transported via these interfaces with third-party software.
>
> We expressly point out that improper use of the interfaces can result in data loss or production downtimes.

> **Note**
>
> There are no obligations or guarantees of any kind associated with using this description to manually modify and evaluate the source file.
>
> Siemens therefore accepts no liability arising from the use of all or part of this description.
>
> If you import externally created configuration data that contains code errors, a wrong structure or unwanted manipulations, this can cause unexpected errors and security risks.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **The API user is responsible for ensuring the security measures of handling passwords through code.** |  |

More information in the TIA Portal Openness documentation:

- "Readme TIA Portal Openness"
- "Basics &gt; Openness tasks &gt; [Introduction](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#introduction)"
- "TIA Portal Openness API &gt; General functions &gt; [TIA Portal Openness firewall](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#tia-portal-openness-firewall)"
- "TIA Portal Openness API &gt; Functions for accessing the data of a PLC device &gt; Functions for downloading data to PLC device &gt; [Downloading to PLC devices](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#downloading-to-plc-devices)"
- "Export/import &gt; Overview &gt; [Basic principles of importing/exporting](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#basic-principles-of-importingexporting)"

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[TIA Portal project view: Exporting and importing CFC charts](#tia-portal-project-view-exporting-and-importing-cfc-charts)

## TIA Portal project view: Exporting and importing CFC charts

You can export and import CFC charts in the TIA Portal project via the "Export / Import CFC" dialog.

The dialog uses the Openness functions for exporting and importing CFC charts. The same constraints apply as when using the Openness functions directly.

Follow the instructions under "[Export/Import of CFC charts](#exportimport-of-cfc-charts)", section "Security measures for TIA Portal Openness applications".

### Data transfer dialog

For the import, you use the "Data transfer - Generate/import" dialog.

More information on this dialog:

- [Industry Online Support: "SIMATIC Process Control System PCS 7 Help on data transfer dialog"](https://support.industry.siemens.com/cs/ww/en/view/109812471)

### Requirements

- "TIA Openness" is installed.
- The PLC is not online.
- The CFC charts to be exported are not password-protected.

  CFC charts with configured passwords are ignored during the export.
- Import: The imported block types have been created and compiled under the PLC in the TIA Portal.

  If the imported XML file contains blocks that have not yet been created, the import is canceled.

### Procedure

1. Select the "Charts" entry or a CFC chart in the project tree.
2. Select the "Tools &gt; Import / Export CFC" entry in the menu bar.

   The "Export / Import CFC" dialog opens.
3. Select the action you want:

   - Export all CFC charts of the PLC

     The block types and the settings for tasks and run sequence are also exported along with the CFC charts.
   - Export individual CFC charts

     The CFC charts are exported without block types, task settings, and run sequence.

     Click "Next" and select the desired charts.
   - Import CFC charts

     You can select the scope of the import in the next "Data transfer - Generate/import" dialog.
4. Click "Next".
5. Select the storage path of the XML file and click "Finish".

   The export or import is started.
6. If you are exporting CFC charts, confirm the message that the XML file has been written.

   The XML file with the exported data is located in the selected storage path.
7. If you are importing CFC charts, the "Data transfer - Generate/import" dialog opens.

   Select the objects to be imported, and click the "Import objects from B to A" button in the "Generate/import" area: ![Procedure](images/161826302347_DV_resource.Stream@PNG-de-DE.png)

   The desired data is imported into the TIA Portal project under the PLC.

   The Inspector window contains information on the import where appropriate.

---

**See also**

[Exporting CFC charts](#exporting-cfc-charts)
  
[Exporting only selected CFC charts](#exporting-only-selected-cfc-charts)
  
[Importing CFC charts](#importing-cfc-charts)

## Exporting CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.
- The CFC charts to be exported are not password-protected.

  CFC charts with a configured password are ignored during export.

### Application

The TIA Portal Openness API supports the export of CFC charts to an XML file with the function "CompleteExport".

The function writes the CFC project data from the chart folder into an XML file:

- All CFC charts created under the selected PLC
- Block types used in the exported charts
- Task assignment for the exported charts
- Run sequence of each exported chart

You find more information on the supported objects in the CFC documentation: "[Instructions and blocks](Configuring%20CFC%20charts.md#instructions-and-blocks)".

If you want to start a selective XML export of CFC charts, use the function "[SelectiveExport](#exporting-only-selected-cfc-charts)".

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| xmlFilePath | String | Folder path and name of the import file |
| modelVersion | String | S7TIA exchange model version to be used |
| filter | Int64 | Filter options for the automation interface |
| unattended | Boolean | Toggle for silent mode |

### Program code

Modify the following program code to export all CFC charts from a PLC with their objects to an XML file.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Export CFC charts:

// XML file information for export

    chartProvider.CompleteExport(@"D:\Users\username1\Documents\Automation\OpennessExample.xml", "V2.0", 0, true);

clipboard

More information in the TIA Portal Openness documentation:

- "Export/import &gt; Overview &gt; [Exporting configuration data](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#exporting-configuration-data)"

---

**See also**

[Export/Import of CFC charts](#exportimport-of-cfc-charts)
  
[TIA Portal project view: Exporting and importing CFC charts](#tia-portal-project-view-exporting-and-importing-cfc-charts)

## Exporting only selected CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.
- The CFC charts to be exported are not password-protected.

  CFC charts with a configured password are ignored during export.

### Application

The TIA Portal Openness API supports the export of specific CFC charts to an XML file with the function "SelectiveExport".

The function writes the project data for only the selected charts into an XML file:

- Specific CFC charts from the selected PLC
- Block types used in the exported charts
- Task assignment for the exported charts
- Run sequence of each exported chart

You find more information on the supported objects in the CFC documentation: "[Instructions and blocks](Configuring%20CFC%20charts.md#instructions-and-blocks)".

If you want to start a complete XML export of all CFC charts, use the function "[CompleteExport](#exporting-cfc-charts)".

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| xmlFilePath | String | Folder path and name of the import file |
| selectedObjects | String[] | Names of the charts that you want to export |
| modelVersion | String | S7TIA exchange model version to be used |
| filter | Int64 | Filter options for the automation interface |
| unattended | Boolean | Toggle for silent mode |

### Program code

Modify the following program code to export only selected CFC charts with their objects to an XML file.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Export selected CFC charts

// XML file information for export of CFC charts "CFC_1" and "CFC_3"

    chartProvider.SelectiveExport(@"D:\Users\username1\Documents\Automation\OpennessExample.xml", new string[] { "CFC_1", "CFC_3" }, "V2.0", 0, true);

clipboard

More information in the TIA Portal Openness documentation:

- "Export/import &gt; Overview &gt; [Exporting configuration data](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#exporting-configuration-data)"

---

**See also**

[Export/Import of CFC charts](#exportimport-of-cfc-charts)
  
[TIA Portal project view: Exporting and importing CFC charts](#tia-portal-project-view-exporting-and-importing-cfc-charts)

## Importing CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.

### Application

The TIA Portal Openness API supports the import of CFC charts from an XML file with the function "Import".

The XML file is created by a complete XML export or by a selective XML export of specific CFC charts.

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| xmlFilePath | String | Folder path and name of the import file |
| modelVersion | String | S7TIA exchange model version to be used |
| filter | Int64 | Filter options for the automation interface  In the current CFC version, the parameter is not evaluated during export and import and has no function. |
| unattended | Boolean | Toggle for silent mode |
| deleteAtTarget | Boolean | Toggle for deleting objects in the TIA project that were not included in the original export file |

### Program code

Modify the following program code to import CFC charts from an XML file.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Import CFC charts

// XML file information for import

    chartProvider.Import(@"D:\Users\username1\Documents\Automation\OpennessExample.xml", "V2.0", 0, true, false);

clipboard

More information in the TIA Portal Openness documentation:

- "Export/import &gt; Overview &gt; [Importing configuration data](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#importing-configuration-data)"

---

**See also**

[Export/Import of CFC charts](#exportimport-of-cfc-charts)
  
[TIA Portal project view: Exporting and importing CFC charts](#tia-portal-project-view-exporting-and-importing-cfc-charts)

## Setting a password for CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.

### Application

To protect a CFC chart or hierarchical CFC chart from unintentional editing, you can protect the chart with a password.

- To configure a password, use the function "AddChartProtection".
- To change an existing password, use the function "[ChangeChartProtection](#changing-a-password-for-cfc-charts)".
- To read the password from a chart as a hash value, use the function "[GetChartProtection](#reading-the-password-from-cfc-charts)".
- To delete the configured password, use the function "[RemoveChartProtection](#removing-a-password-from-cfc-charts)".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password merely protects the CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| chartName | System.String | Name of the chart which is protected with a password. |
| newHashedPassword | System.String | Password  The password is displayed as a hash value. |

**Return value**

The function "AddChartProtection" returns a System.Boolean:

| Symbol | Meaning |
| --- | --- |
| TRUE | The password was set successfully. |
| FALSE | The password could not be set. |

### Program code

Modify the following program code to set a password for a CFC chart.

In this example, the hash value of the new password is included as an abbreviated example value.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Configure CFC chart password

    bool added = chartProvider.AddChartProtection("CFC_1", "AgGUWq...92M=");

clipboard

---

**See also**

[Export/Import of CFC charts](#exportimport-of-cfc-charts)

## Reading the password from CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.

### Application

To read the password from a CFC chart, use the function "GetChartProtection".

You can change or delete that password with the functions "[ChangeChartProtection](#changing-a-password-for-cfc-charts)" and "[RemoveChartProtection](#removing-a-password-from-cfc-charts)".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password merely protects the CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| chartName | System.String | Name of the chart which is protected with a password. |

**Return value**

The function "GetChartProtection" returns a System.Boolean:

| Symbol | Meaning |
| --- | --- |
| TRUE | The password was read successfully. |
| FALSE | The password could not be read. |

### Program code

Modify the following program code to read a password from a CFC chart.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Read CFC chart password

    string passwordHash = chartProvider.GetChartProtection("CFC_1");

clipboard

---

**See also**

[Setting a password for CFC charts](#setting-a-password-for-cfc-charts)
  
[Export/Import of CFC charts](#exportimport-of-cfc-charts)

## Changing a password for CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.

### Application

To change the password that is used to protect a CFC chart or hierarchical CFC chart from unintentional editing, use the function "ChangeChartProtection".

You can read or delete a password with the functions "[GetChartProtection](#reading-the-password-from-cfc-charts)" and "[RemoveChartProtection](#removing-a-password-from-cfc-charts)".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password merely protects the CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| chartName | System.String | Name of the chart which is protected with a password. |
| currentPassword | System.Security.SecureString | Currently used password for the CFC chart. |
| newHashedPassword | System.String | New Password  The password is displayed as a hash value. |

**Return value**

The function "ChangeChartProtection" returns a System.Boolean:

| Symbol | Meaning |
| --- | --- |
| TRUE | The password was changed successfully. |
| FALSE | The password could not be changed. |

### Program code

Modify the following program code to change a password for a CFC chart.

In this example, the password "test" is changed to a new password. The hash value of the new password is included as an abbreviated example value.

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Change CFC chart password

char[] password1 = new char[] {'t', 'e', 's', 't'};

SecureString securePassword1 = new SecureString();

foreach (char ch in password1)

    securePassword1.AppendChar(ch);

bool changed = chartProvider.ChangeChartProtection("CFC_1", securePassword1, "AgGUWq...92M=");

clipboard

---

**See also**

[Setting a password for CFC charts](#setting-a-password-for-cfc-charts)
  
[Export/Import of CFC charts](#exportimport-of-cfc-charts)

## Removing a password from CFC charts

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.

  See "[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)"
- A project is open.

  See "[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)"
- PLC is not online.

### Application

To delete a configured password for a CFC chart, use the function "RemoveChartProtection".

The CFC chart can then be opened and edited again without entering a password.

To set the password again, use the function "[AddChartProtection](#setting-a-password-for-cfc-charts)".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password merely protects the CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

**Parameters**

| Parameter | Data type | Description |
| --- | --- | --- |
| chartName | System.String | Name of the chart which is protected with a password. |
| currentPassword | System.Security.SecureString | Currently used password for the CFC chart. |

**Return value**

The function "RemoveChartProtection" returns a System.Boolean:

| Symbol | Meaning |
| --- | --- |
| TRUE | The password was deleted successfully. |
| FALSE | The password could not be deleted. |

### Program code

Modify the following program code to remove a password for a CFC chart.

In this example, the password "test" was configured for the chart "CFC_1".

plcSoftware = (PlcSoftware) swContainer.Software;

chartProvider = plcSoftware.GetService&lt;ChartProviderS7&gt;();

if (chartProvider == null)    // in case that CFC is not installed

    return;

// Remove CFC chart password

char[] password1 = new char[] {'t', 'e', 's', 't'};

SecureString securePassword1 = new SecureString();

foreach (char ch in password1)

    securePassword1.AppendChar(ch);

bool removed = chartProvider.RemoveChartProtection("CFC_1", securePassword1);

clipboard

---

**See also**

[Changing a password for CFC charts](#changing-a-password-for-cfc-charts)
  
[Reading the password from CFC charts](#reading-the-password-from-cfc-charts)
  
[Export/Import of CFC charts](#exportimport-of-cfc-charts)
