---
title: "STEP 7 CFC"
package: ReadMeCFCS7enUS
topics: 8
source: Siemens TIA Portal Information System (offline help, en-US)
---


# STEP 7 CFC

This section contains information on the following topics:

- [Cybersecurity information](#cybersecurity-information)
- [Scope of delivery for SIMATIC STEP 7 CFC](#scope-of-delivery-for-simatic-step-7-cfc)
- [What's new in SIMATIC STEP 7 CFC in TIA Portal V19?](#whats-new-in-simatic-step-7-cfc-in-tia-portal-v19)
- [System requirements for SIMATIC STEP 7 CFC](#system-requirements-for-simatic-step-7-cfc)
- [SIMATIC STEP 7 CFC licensing](#simatic-step-7-cfc-licensing)
- [General information about SIMATIC STEP 7 CFC](#general-information-about-simatic-step-7-cfc)
- [Notes on exporting/importing CFC charts (TIA Portal Openness)](#notes-on-exportingimporting-cfc-charts-tia-portal-openness)

## Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines and networks.

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For additional information on industrial cybersecurity measures that may be implemented, please visit   
[https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates, subscribe to the Siemens Industrial Cybersecurity RSS Feed under   
[https://new.siemens.com/global/en/products/services/cert.html](https://new.siemens.com/global/en/products/services/cert.html).

## Scope of delivery for SIMATIC STEP 7 CFC

The scope of delivery includes:

- SIMATIC STEP 7 CFC V19

## What's new in SIMATIC STEP 7 CFC in TIA Portal V19?

### Stability and performance

With SIMATIC STEP 7 CFC V19, further improvements have been made to the stability and performance.

Overview of important performance improvements:

- Configuring of CFC charts
- Editing of CFC charts in groups
- Compiling and downloading of CFC charts
- Opening of CFC charts in runtime

### CFC tag interconnections

The new list of CFC tag interconnections in the "Chart sequence &amp; extras" editor supports you in searching for interconnected operands.

As in the cross-reference list, you can filter and sort the list of interconnected tags and global data blocks.

### TIA Portal Openness: Exporting and importing CFC charts

Stability and performance when exporting and importing CFC charts have been improved.

### Changed icon: Add input parameters

In the "Data flow" tab of the CFC editor, you can add additional input parameters at a block instance with a mouse click.

The icon for this has been adapted to be consistent with the representation in other editors of the TIA Portal:

- Icon up to CFC V18: ![Changed icon: Add input parameters](images/173863735435_DV_resource.Stream@PNG-de-DE.png)
- New icon as of CFC V19: ![Changed icon: Add input parameters](images/173863540875_DV_resource.Stream@PNG-de-DE.png)

### CFC editor: Additional functions

Screen resolution:

- Support for high-resolution screen settings

Zoom function in the data flow:

- When you zoom in on the view, the input boxes for editing interconnection paths are also zoomed in on.

  The font size remains the same, so that the boxes provide more space for editing long interconnection paths.

Highlighting of interconnections:

- The color highlighting of connected and unconnected interconnections has been optimized.

Sheet bar view:

- To adapt the width of fixed sheet bars to the text length of the interconnections, double-click the boundary line of the sheet bar.

Opening a CFC chart:

- When you close a CFC chart after editing and then reopen it, the preceding settings, e.g. zoom factor and position of scroll bar, are applied.

---

**See also**

[Basics of CFC](Configuring%20CFC%20charts.md#basics-of-cfc)
  
[Export/Import of CFC charts](CFC%20Charts%20%28Export-Import%29.md#exportimport-of-cfc-charts)
  
[General information about SIMATIC STEP 7 CFC](#general-information-about-simatic-step-7-cfc)
  
[Notes on exporting/importing CFC charts (TIA Portal Openness)](#notes-on-exportingimporting-cfc-charts-tia-portal-openness)
  
[Displaying points of use of interconnections](Configuring%20CFC%20charts.md#displaying-points-of-use-of-interconnections)

## System requirements for SIMATIC STEP 7 CFC

### Hardware requirements

- Requirements of TIA Portal V19

### Software requirements

- TIA Portal V19

### Supported systems

CFC in the TIA Portal supports CPUs of the following product groups.

Requirement:

- Firmware version ≥ V2.8

**Advanced Controllers**

- Standard CPUs
- Technology CPUs
- Fail-safe CPUs <sup>1)</sup>
- Fail-safe technology CPUs <sup>1)</sup>
- Redundant CPUs <sup>2)</sup>

1) Only with deactivated fail-safe functionality.

2) In the compatibility tool you find detailed information on which CPUs are supported.

**Distributed Controllers**

- ET 200SP CPUs
- Fail-safe ET 200SP CPUs <sup>1)</sup>

1) Only with deactivated fail-safe functionality.

**Software Controllers**

- Standard CPUs:

  - CPU 1507S
  - CPU 1508S

**Restrictions**

- STEP 7 Safety and F-CPUs with enabled F-function are not supported.

  You can use either CFC or the fail-safe functionality on a CPU.

**Compatibility tool**

With the compatibility tool, Industry Online Support gives you a function you can use to put together a compatible selection of software products or to check existing configurations for compatibility.

In the following entry you can call the compatibility tool and find additional information on the operation of the tool:

- [Internet: "Compatibility Tool for Automation and Drive Technology" (entry ID: 64847781)](https://support.industry.siemens.com/cs/ww/en/view/64847781)

---

**See also**

CFC charts for S7 target systems
  
[Adding an unspecified CPU](Configuring%20devices%20and%20networks.md#adding-an-unspecified-cpu)

## SIMATIC STEP 7 CFC licensing

For CFC, you need an engineering license as well as runtime licenses for each CPU.

### License types

**Engineering license**

A license key must be installed on the PC to configure CFC charts.

**Runtime licenses**

You need a license key for each PLC.

Depending on the number of instance data blocks which are created during configuration with CFC, you either need a limited or unlimited license:

- A limited license allows you to create a limited number of instance DBs and load them to the PLC.
- With an unlimited license, you can create and upload an unlimited number of instance DBs.

You can find information on the instance DBs in the "Chart sequence and extras" editor in the "Statistics" tab. The number of instance DBs is displayed which have been created in all CFC charts under the PLC.

More information in the TIA Portal Information System:

- "Configuring technologically &gt; Configuring CFC charts &gt; Working with CFC charts for S7 &gt; "Chart sequence &amp; extras" editor for S7"

**Trial license**

If you do not have a valid license, the system alerts you that you are working in a non-licensed mode.

You have the one-time option of activating a Trial License.

However, this Trial License is valid for a limited period only and expires after 21 days.

### Licenses for SIMATIC STEP 7 CFC V19.0

| License | Display in the Automation Licence Manager | Comment |
| --- | --- | --- |
| SIMATIC STEP 7 CFC V19.0 Software Media Package | SIMATIC STEP 7 CFC Advanced 19.0 | Trial license  The license is already included in the TIA Portal installation. |
| SIMATIC STEP 7 CFC 19.0 Advanced Engineering | SIMATIC STEP 7 CFC Advanced 19.0 | Engineering license |
| SIMATIC STEP 7 CFC Runtime CPU (limited) | - | Runtime license:  - Unlimited runtime - Limited number of instance DBs |
| SIMATIC STEP 7 CFC Runtime CPU (unlimited) | - | Runtime license:  - Unlimited runtime - Unlimited number of instance DBs |

### More information

**Online catalog (Industry Mall)**

- [Internet: "STEP 7 (TIA Portal) options: STEP 7 CFC (TIA Portal)"](https://mall.industry.siemens.com/mall/en/WW/Catalog/Products/10414342?tree=CatalogTree)

**TIA Portal Information System**

- "Installation &gt; [Licensing](Installation.md#notes-on-licenses)"

**Automation License Manager (ALM)**

To open the manual, in the Windows program group "Siemens Automation", select the entry "Documentation".

The "Manuals" folder contains the link to the manual in the respective language folder.

---

**See also**

CFC charts for S7 target systems

## General information about SIMATIC STEP 7 CFC

### Content

The information in this readme file supersedes statements made in other documents.

- Important information on product properties
- Information that could no longer be included in the online help.

Read the following notes carefully because they include important information for installation and use.

Read these notes prior to installation.

### TIA Portal projects: Restrictions

The following functions are not supported when using CFC in the TIA Portal:

- Software units

  Do not create software units on controllers for which CFC charts are configured.

  The configuration of software units can lead to the TIA Portal project no longer being compiled for this controller.
- UMAC-protected projects
- Downloading blocks generated by CFC from the device
- Load CFC charts on memory cards
- Interconnect PLC tags with complex data types

### Global data blocks in CFC

To improve performance, create the block structure for global data blocks according to TIA Portal recommendations.

More information:

- [Industry Online Support: "How can you program efficiently and performantly in STEP 7 (TIA Portal) for the S7-1200/S7-1500?"](https://support.industry.siemens.com/cs/ww/en/view/67582299)
- [Industry Online Support: "Programming guideline and style guide for SIMATIC S7-1200 and S7-1500"](https://support.industry.siemens.com/cs/ww/en/view/81318674)

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Avoid changing the structure**  When interconnecting global data blocks in CFC, the following constraints apply:  - Avoid subsequent modification of interconnected global data blocks. - Avoid changing the structure of global data blocks.   Loading after a structure change causes the PLC to stop.   Download of changes during operation is not possible. |  |

### Password: No authorization, no know-how protection of the charts

To protect a CFC chart or hierarchical CFC chart from unintentional editing, you can protect the chart with a password.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Activating password for CFC chart**  The password serves only to protect a CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

### Instructions: "LBCFC" library for download

The "LBCFC" block library supplements the instruction library installed with SIMATIC STEP 7 CFC V17.

More information:

- [Industry Online Support: SIMATIC STEP 7 CFC V17 - "LBCFC" block library (ID 109800972)](https://support.industry.siemens.com/cs/ww/en/view/109800972)

### Instructions: No version update

Always use the current version of the application library.

After the first import of an instruction in CFC you can no longer change the version. All further instances of the instruction are created with the same version.

When you change an instruction version in the library later, the instruction is marked as "not supported" with an asterisk.

### GRAPH blocks: Using only in a block shell

You cannot insert GRAPH blocks as instances in a CFC chart. Any change of a GRAPH block would then eliminate the ability to perform an online delta download and would require a complete download in CPU Stop.

To work with a GRAPH block in CFC, create an organization block (OB) that uses a GRAPH block.

Even if you change and re-initialize the GRAPH block, you can then update the CPU using a delta download.

**Using an FB as a call block**

If, for example, a GRAPH block affects the CFC run sequence, create a function block (FB) as a "call block" that calls an instance of the GRAPH block.

If input parameters and output parameters have been configured at the call block, you can pass these values to the called instance of the GRAPH block.

Ensure that the interface of the GRAPH block is no longer changed. Interface changes eliminate the ability to perform an online delta download.

Procedure:

1. Create a GRAPH block.
2. To create an instance of the GRAPH block, create a new data block (DB).
3. Select the GRAPH block as "Type".
4. Create a function block (FB) as call block.
5. In the FB, configure the call of the DB that you have created as the GRAPH instance.
6. To exchange values with the called GRAPH instance, configure the corresponding input parameters and output parameters at the FB.
7. Drag the FB into your CFC chart.

   The FB instance in the CFC chart gives you access to the called instance of the GRAPH block.

### Data types

**Data types supported to a limited extent**

The following data types of the S7-1500 are supported to a limited extent:

- ARRAY

  All data types are permitted for the ARRAY components, except:

  - ARRAY
  - Reference data types:

    Pointer: ANY, POINTER, VARIANT

    Parameter types: COUNTER, TIMER

  More information in the TIA Portal Information System:

  "Configuring CFC charts &gt; Data types in CFC &gt; Compound data types &gt; [ARRAY](Configuring%20CFC%20charts.md#array)".
- VARIANT

  No blocks with output parameters of the VARIANT data type

**Unsupported data types**

The following data types of the S7-1500 are not supported:

- WString

  Exception: The WString data type is used with OPC UA.
- Block_FB
- Block_FC

### Do not change internal CFC blocks

CFC creates system blocks that are displayed in a number of views or lists, for example, under "Program information".

You may not change these objects.

Only edit your own blocks and instructions using the STEP 7 editors.

### Redundant CPUs: Downloading changes

You can only download changes in CFC to the redundant CPU that was also used for the previous download. The time stamps are compared internally for this purpose.

Take this special feature into account, especially when switching over the redundant partner and when using the "Download to backup CPU" function.

**"Download to backup CPU"**

Once you have executed the "Download to backup CPU" function, you can no longer download the changed CFC data to the primary CPU. After loading the backup CPU, the primary CPU has an outdated time stamp.

To download CFC changes, switch the roles of the primary CPU and backup CPU.

More information in the TIA Portal information system:

- "Editing devices and networks &gt; Configuring devices and networks &gt; Creating configurations &gt; Configuring automation systems &gt; Principle of operation of S7-1500R/H CPUs &gt; Loading an S7-1500R/H CPU &gt; Downloading project data to the backup CPU"

### Full compilation: Reinitialization of runtime values

When you perform a full compilation of the CPU, a subsequent delta download may result in reinitialization of runtime values, e.g. in instances of functions (FCs).

However, the runtime values are retained in instances of function blocks (FBs).

### Deleting CFC charts and deactivating CFC

When you delete all CFC charts, the option "SIMATIC STEP 7 CFC" remains active in the TIA Portal.

Downloading to the PLC therefore causes the project to be saved.

To deactivate CFC in TIA Portal, delete all CFC components:

1. Select the entry "Charts" in the project tree.
2. Select the "Delete" entry from the shortcut menu and confirm with "OK".

   The full contents of the "Charts" folder are deleted.
3. To reactivate the "CFC" option, double-click the entry "Add new chart" under "Charts".

### Tooltips in the sheet bar: Avoid overlaps

Tooltips may show the complete interconnection path for interconnections in the sheet bar of the data flow.

These tooltips can impede editing of the interconnection path because they are shown over the text box.

To avoid this behavior when editing long interconnection paths, increase the zoom factor for the view of the CFC chart to over 100%.

This also zooms in on the input boxes in the chart and in the sheet bar. At 200%, input boxes in the sheet bar are enlarged up to the edge of the area.

The text size in the input box is not affected by the zoom factor. The larger input boxes therefore allow convenient editing of even long interconnection paths.

**Disable tooltips**

Alternatively, disable tooltips in the TIA Portal settings:

- "General &gt; General settings &gt; Tooltips: Show truncated texts completely"

---

**See also**

[Notes on exporting/importing CFC charts (TIA Portal Openness)](#notes-on-exportingimporting-cfc-charts-tia-portal-openness)

## Notes on exporting/importing CFC charts (TIA Portal Openness)

### Notes on CFC Openness applications

### Openness: "filter" parameter

The "filter" parameter is not evaluated during export and import in the current CFC version and has no function.

### Openness: Error message when importing

If the import using the TIA Portal Openness API is aborted with an error message regarding the work memory, check the work memory on the PC.

If necessary, increase the work memory according to the hardware requirements for large projects:

- RAM: 32 GB for large projects

### Import of function blocks: Alarm data comparison always reports difference

Function blocks show an alarm data attribute, which is always exported and imported. This may also apply if no alarms are configured.

When matching the imported data in the "Data Transfer - Generate/Import" dialog, a difference is always displayed for this attribute, even if the import was completed correctly.

If necessary, check your instance-specific messages.

---

**See also**

[General information about SIMATIC STEP 7 CFC](#general-information-about-simatic-step-7-cfc)
  
[Export/Import of CFC charts](CFC%20Charts%20%28Export-Import%29.md#exportimport-of-cfc-charts)
  
[Industry Online Support: "SIMATIC Process Control System PCS 7 Help on data transfer dialog"](https://support.industry.siemens.com/cs/ww/en/view/109812471)
