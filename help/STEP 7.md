---
title: "STEP 7"
package: ReadMeSTEP734enUS
topics: 44
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# STEP 7

This section contains information on the following topics:

- [Security information](#security-information)
- [Notes on use](#notes-on-use)
- [Parallel online connections](#parallel-online-connections)
- [Editing devices and networks](#editing-devices-and-networks)
- [Programming a PLC](#programming-a-plc)
- [Using online and diagnostics functions](#using-online-and-diagnostics-functions)
- [Inter Project Engineering (IPE)](#inter-project-engineering-ipe)
- [Technological functions](Technological%20functions.md#technological-functions)
- [STEP 7 CFC](STEP%207%20CFC.md#step-7-cfc)

## Security information

### Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines and networks.

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For additional information on industrial cybersecurity measures that may be implemented, please visit [https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates, subscribe to the Siemens Industrial Cybersecurity RSS Feed under [https://new.siemens.com/global/en/products/services/cert.html](https://new.siemens.com/global/en/products/services/cert.html).

### Network settings

The following tables show the network settings of each product you need to analyze the network security and to configure external firewalls:

| STEP 7 Professional |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| ALM | 4410* | TCP | Inbound/outbound | License service | This service provides the complete functionality for software licenses and is used by both the Automation License Manager as well as all license-related software products. |
| RFC 1006 | 102 | TCP | Outbound | S7 communication | Communication to the S7 controller via Ethernet/PROFINET for programming and diagnostic purposes. |
| DCP | --- | Ethernet | Outbound | PROFINET | The DCP protocol (Discovery and Basic Configuration Protocol) is used by PROFINET and provides the basic functionality for locating and configuring PROFINET devices. |
| SNMP | 161 | UDP | Outbound | PROFINET | The SNMP client functionality is used by STEP 7 to read status information from PROFINET devices. |
| * Default port that can be changed by user configuration |  |  |  |  |  |

| WinCC ES Basic (without simulation) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| ALM | 4410* | TCP | Inbound/outbound | License service | This service provides the complete functionality for software licenses and is used by both the Automation License Manager as well as all license-related software products. |
| HMI Load | 1033 | TCP | Outbound | HMI Load (RT Basic) | This service is used to transmit images and configuration data to Basic Panels. |
| * Default port that can be changed by user configuration |  |  |  |  |  |

| Simulation RT Basic |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Name** | **Port number** | **Transport protocol** | **Direction** | **Function** | **Description** |
| HMI Load | 1033 | TCP | Inbound | HMI Load (RT Basic) | This service is used to transmit images and configuration data to Basic Panels. |
| EtherNet/IP | 44818 | TCP | Outbound | Ethernet/IP channel | The Ethernet/IP protocol is used for connections to Allen Bradley PLCs. |
| 2222 | UDP | Inbound | Ethernet/IP channel | The Ethernet/IP protocol is used for connections to Allen Bradley PLCs. |  |
| Modbus TCP | 502 | TCP | Outbound | Modbus TCP channel | The Modbus TCP protocol is used for connections to Schneider PLCs. |
| RFC 1006 | 102 | TCP | Outbound | S7 channel | Communication to the S7 controller via Ethernet/PROFINET |
| Mitsubishi MC | 5002 | TCP | Outbound | Mitsubishi MC channel | The Mitsubishi protocol is used for connections to Mitsubishi PLCs. |

### Security note on know-how-protected blocks

When protecting blocks, note that full password protection is not provided until you have archived the project.

After archiving, only the archived project no longer contains any unprotected blocks.

Optimization of project data during archiving removes older, possibly unprotected, blocks.

If you want to distribute protected blocks, only pass on the archived project, or copy the building blocks to a new global library.

## Notes on use

### Contents

Information that could not be included in the online help and important information about product characteristics.

### Removing and inserting Ethernet modules

If Ethernet modules are removed and re-inserted during operation, you must boot the PC; otherwise, the "Accessible devices" functionality in STEP 7 or NCM PC will not display all devices. While the PC boots, Ethernet modules must be activated.

### Compatibility (S7-1200)

The device configuration and program of an S7-1200 CPU must always be configured with the same STEP 7 version. Usually, TIA Portal makes sure that no version conflicts occur by outputting appropriate notifications during loading to the device.

This automatic verification is not possible with S7-1200 CPUs with firmware version V1.x. In this case, users themselves must ensure that no version conflicts occur.

---

**See also**

[Addressing tags in global data blocks](Programming%20basics.md#addressing-tags-in-global-data-blocks)

## Parallel online connections

### Contents

Information that could not be included in the online help and important information about product characteristics.

### Online connections on a S7-1200 CPU

Simultaneous online connections from multiple instances of the TIA Portal to the same S7-1200 CPU are not possible.

### Online connections to an S7-300/S7-400 CPU

Simultaneous online connections from multiple instances of the TIA Portal to the same S7-300/S7-400 CPU are not approved. Multiple accesses to the same CPU from this family can lead to errors.

Simultaneous online connections of STEP 7 V5.6 or earlier and STEP 7 (TIA Portal) have also not been approved and can result in errors.

## Editing devices and networks

This section contains information on the following topics:

- [General information on devices and networks](#general-information-on-devices-and-networks)
- [Notes on the hardware configuration](#notes-on-the-hardware-configuration)
- [Information about OPC UA functions](#information-about-opc-ua-functions)
- [Certificate checks during connection establishment (S7-1500 CPU)](#certificate-checks-during-connection-establishment-s7-1500-cpu)
- [Online access to a CPU with access protection via accessible nodes](#online-access-to-a-cpu-with-access-protection-via-accessible-nodes)
- [HW ID of type "Hw_SubModule" for an HMI Panel IO device](#hw-id-of-type-hw_submodule-for-an-hmi-panel-io-device)
- [Use of modules on the S7-1200](#use-of-modules-on-the-s7-1200)
- [CP 343-2 on SIMATIC S7 Embedded Controller EC31-RTX](#cp-343-2-on-simatic-s7-embedded-controller-ec31-rtx)
- [Loading of S7-1500 CPUs (temporarily not possible)](#loading-of-s7-1500-cpus-temporarily-not-possible)
- [Loading of S7-1500 CPUs (SIPLUS)](#loading-of-s7-1500-cpus-siplus)
- [Module change for I-devices (S7-1500 CPU FW versions &lt; V3.1 and V3.1)](#module-change-for-i-devices-s7-1500-cpu-fw-versions-v31-and-v31)
- [ET 200MP (IM 155-5 DP ST) on a WinLC RTX](#et-200mp-im-155-5-dp-st-on-a-winlc-rtx)
- [Elimination of TS adapters](#elimination-of-ts-adapters)
- [Network components](Network%20components.md#network-components)

### General information on devices and networks

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### SIMATIC S7-PCT (Port configuration tool)

If you use the PCT tool, make sure that you always use the current version that is available free of charge with the following link:

[http://support.automation.siemens.com/WW/view/32469496](http://support.automation.siemens.com/WW/view/en/32469496)

#### Verified external access

Contrary to the description in the information system, the "Verified external access" function is not available for the current S7-1500 CPUs (firmware version V3.0). The described settings, which determine the behavior of the CPU in relation to external read/write access, are not available.

### Notes on the hardware configuration

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Editing a device IP address

Do not use the address range from 192.168.x.241 to 192.168.x.250 when editing a device IP address. If necessary, this address range is automatically assigned by the system to a programming device. Depending on the subnet mask, this applies also for all network classes.

### Information about OPC UA functions

This section contains information on the following topics:

- [New in V19: Handling of dynamic arrays](#new-in-v19-handling-of-dynamic-arrays)
- [Information about OPC UA functions](#information-about-opc-ua-functions-1)

#### New in V19: Handling of dynamic arrays

##### Contents

Information that could not be included in the online help and important information about product features.

##### Dynamic arrays

As of TIA Portal V19 and S7-1500 CPU FW version V3.1, you can use so-called "dynamic arrays" for your OPC UA server and OPC UA client interfaces. The following description explains the principle and functionality of the server interface. The structure of the structure/UDT for a dynamic array is identical for client and server applications.

With dynamic arrays, it is possible to define data structures whose number of elements can be changed at runtime on the server interface side. On the CPU side, the dynamic array is mapped to a fixed-size structure.

**Example**: Process data from production for quality assurance purposes is transferred to a higher-level management system. The number of process data elements is different, depending on the product type. If the product type is changed during runtime, the number of process data elements needed also changes.

In STEP 7 (TIA Portal), an array is a data type that you can assign to a tag. An array represents a data structure that consists of a fixed number of components of the same data type. All data types except ARRAY are permitted for the components.

By contrast, OPC UA does not define an array as a data type. Any variable value (Value) can be an array. The following attributes and properties of Variable NodeClass are used in OPC UA to define how a variable is structured with respect to its "geometry" as an array (except from [https://reference.opcfoundation.org/Core/Part3/v104/docs/5.6](https://reference.opcfoundation.org/Core/Part3/v104/docs/5.6/)):

| Attribute / Property | Data type | Possible values, meaning |
| --- | --- | --- |
| ValueRank (Mandatory) | Int32 | - n &gt; 1: Value is an array with dimension n. - 1: Value is an array with one dimension - 0: Value is an array with one or more dimensions - -1: Value is a scalar (not an array) - -2: Value is a scalar or an array with any number of dimensions - -3: Value can be a scalar or a one-dimensional array |
| ArrayDimensions (Optional) | UInt32[] | Maximum supported length of each dimension.   0 or empty: Unknown length. |
| MaxArrayLength (Optional) | UInt32 | For DataVariables with ValueRank attribute not set to scalar:  Maximum length of the array.   Example: A three-dimensional array with lengths 2x3x10 has the length 60. |

The name "dynamic array" is used here to establish a counterpart on the SIMATIC data type end for the dynamics of the variable geometry defined in OPC UA, so that mapping of array data is possible. You can change the geometry of a mapped array during runtime using your STEP 7 program. On the OPC UA end, you define a node in the OPC UA server interface via which a client can access the mapped CPU data (the dynamic array).

##### Principle

In order for OPC UA variables to be mapped to CPU tags of Array type, you use a structure or UDT with the new system data type "OPC_UA_ArrayBoundaries".

The structure or UDT has the following structure elements and is structured as follows:

- The first structure element (array size) is itself an array and defines the current size of the dynamic array. The system data type "OPC_UA_ArrayBoundaries" defines the index range available in the server interface for each dimension (with lower and higher boundary elements in each case).
- The second structure element (array data) contains all array elements with a selectable data type permitted for OPC UA.

STEP 7 (TIA Portal) automatically ensures that, for example, negative indexes on the SIMATIC end are converted to non-negative indexes (starting at "0") on the OPC UA end (server interface).

##### Example of one-dimensional array

The following example shows the structure for a simple, one-dimensional array with a maximum of 10 elements. The current size of the array is set to 3 elements [0..2].

| Name | Data type | Possible values / Description |
| --- | --- | --- |
| 1-Dim-Struct | Struct (UDT) |  |
| - **ArraySizeAct** | Array [0..0] of OPC_UA_ArrayBoundaries | **Current array size** |
| - - ArraySizeAct[0] | OPC_UA_Boundaries | One dimension |
| - - - Lower | DInt | 0 (lower index) |
| - - - Upper | DInt | 2 (possible upper index values: 0..9) |
| - **MyDataArray** | Array[**0**..9] of Byte | **Array data (all array elements)** |
| - - MyDataArray[0] | Byte | First element |
| ... | ... | ... |
| - - MyDataArray[9] | Byte | Last element |

##### Example of two-dimensional array

The following example shows the structure for a two-dimensional array with 10x6 = 60 elements. The lower indexes of both dimensions are not "0" in this case. The current size of the array is set to 2x6 = 12 elements.

| Name | Data type | Possible values / Description |
| --- | --- | --- |
| 2-Dim-Struct | Struct (UDT) |  |
| - **ArraySizeAct** | Array [0..1] of OPC_UA_ArrayBoundaries | **Current array size** |
| - - ArraySizeAct[0] | OPC_UA_Boundaries | First dimension |
| - - - Lower | DInt | **-9** (lower index) |
| - - - Upper | DInt | -8 (possible upper index values: -9..0) |
| - - ArraySizeAct[1] | OPC_UA_Boundaries | Second dimension |
| - - - Lower | DInt | **5** (lower index) |
| - - - Upper | DInt | 10 (possible upper index values: 5..10) |
| - **MyDataArray** | Array[-**9**..0, **5**..10] of Byte | **Array data (all array elements)** |
| - - MyDataArray[-9,5] | Byte | First element |
| - - MyDataArray[-9,6] | Byte | Second element |
| ... | ... | ... |
| - - MyDataArray[0,9] | Byte | Second to last element |
| - - MyDataArray[0,10] | Byte | Last element |

##### Effects on the server interface

Appearance in the server interface: If you drag a dynamic array (e.g. 2-Dim-Struct) and drop it onto the server interface in the editor for the server interface, STEP 7 (TIA Portal) creates a node of the same name without the subelements. The node indicates type "ARRAY" in the "Node type" column with the maximum possible lengths of the array.

Browse: The dynamic array is available as a node in the OPC UA address space. Unlike for static arrays, the subelements of the array are not visible as child nodes.

Read: The dynamic array can be read with the Read service. The client can specify whether it wants to read the entire array or only parts of it (IndexRange). Only the read parts that lie within the boundaries of the current array range return the status "Good". If the array size is "0" in every dimension, an empty array is returned with status "Good".   
If an array of size "0" is read in a dimension, then an empty array with status "Good" is returned.

Write: If the range to be written is less than or equal to the maximum array size, all elements are written (status "Good"). If the range to be written is greater than the maximum array size, nothing is written and status 8074_0000 is returned (OpcUa_BadTypeMismatch). If part of an array is written (IndexRange), the behavior is exactly the same: All dimensions of the array range to be written must lie completely within the maximum array size. Only then is the data written and the status "Good" returned.   
If an array of size "0" is written in at least one dimension, then this value is set correctly in the CPU data. The elements "Lower" and "Upper" in the corresponding OPC_UA_ArrayBoundaries structure are adjusted accordingly ("Upper" = "Lower-1").

##### Rules and specific features

- You can also use dynamic arrays for input parameters and output parameters in methods.
- Avoid inconsistencies caused by changing the current size of the array while a client is accessing the array. The result of the access is undefined in this case.   
  Use the uninterruptible instruction UMOVE_BLK for changing the current array size.
- In contrast to the SIMATIC data type Array, there can be "empty" arrays in OPC UA. You define an array with 0 elements in one dimension with OPC_UA_ArrayBoundaries by setting the highest index value (Upper) less than the lowest index value (Lower), e.g. with the following values: Upper = Lower-1.

  If you define a multidimensional array in the server interface (or client interface) and at least one dimension is "0" (empty), then by definition it is an empty array (all dimensions are 0).
- The values for the current array size and the values for the array data must be consistent. Otherwise, error code 803A_0000 (OpcUa_BadNotReadable) is output.

  - The values you set for "Lower" for the current array size in a dimension must also be set as the lower index value in the range of the array data in the corresponding dimension.
  - The values you have set for "Upper" for the current array size for a dimension must also lie within the range of the array data for this dimension.
- If an OPC UA client writes a dynamic array in the server, the client must write an array with the same dimension (ValueRank). Otherwise, the status 8074_0000 is returned (OpcUa_BadTypeMismatch).

#### Information about OPC UA functions

##### Contents

Information that could not be included in the online help and important information about product features.

##### Used nodeset and schema files for OPC UA functionality

The OPC Foundation provides its members with schemes that manufacturers can use for their respective server/client implementations. These files are used, for example, to validate imported information models / nodesets.

In addition, the OPC Foundation provides basic information models via nodesets, which are integrated into the firmware of the S7-1200/1500 CPUs as well as in the TIA Portal via SDKs (System Development Kits). These are Core Model Nodeset (namespace 0) and the DI Model Nodeset (device integration). The DI information model functions like a companion standard, but is maintained exclusively by the OPC Foundation. It forms the basis for other companion standards for modeling a wide variety of devices.

The following schema and nodeset files are used for TIA Portal version V19 and S7-1500 CPU firmware version V3.1 / S7-1200 CPU firmware version V4.7:

| Schema/Nodeset | Explanation |
| --- | --- |
| https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.xml  https://opcfoundation.org/UA/schemas/1.04/UANodeSet.xsd | OPC UA ("CORE") Model Version 1.04.9 (2021-01-21)   XML scheme for NodeSet files (UANodeSet.xsd and Opc.Ua.Types.xsd) |
| https://opcfoundation.org/UA/schemas/DI/1.1/Opc.Ua.Di.NodeSet2.xml | OPC UA for Devices ("DI") Model Version 1.01 (2018-06-07) |

##### Useful information about the core or base information model

The Core information model (nodeset) is a requirement for every OPC UA server and is integrated in the OPC UA server of the S7-1200/1500 CPU.

The nodes of this information model are thus known to the CPU. The version of this nodeset is tied to the firmware version of the CPU and cannot be changed at this time.   
The Core information model is also integrated in the TIA Portal.

When an OPC UA server configuration is loaded, this nodeset is not loaded because it is already known to the CPU (integrated).   
The Core Information Model is also integrated in the SiOME modeling editor.

Recent versions of the Core information model may contain nodes that were not present in previous versions. Loading a server configuration in CPUs with older firmware versions may cause problems in rare cases. When exporting the SIMATIC OPC UA address space from TIA Portal and also from SiOME, the Core information model is not exported as well.

##### Useful information about the DI information model

The DI information model is also integrated in the CPUs and in the TIA Portal.

To configure the CPU, you may have to load the current DI information model (DI nodeset). You download a current DI nodeset from the OPC Foundation website (https://opcfoundation.org/UA/schemas/DI/) and import it into your TIA project as a reference namespace.

Make sure that the DI information model matches the Core model – in the nodeset file Opc.Ua.Di.NodeSet2.xml it is documented via the "RequiredModel" element which version the Core model must have.

**Example**: The DI information model version "1.03.1" requires at least Core Information Model version="1.04.4":

&lt;Model ModelUri="http://opcfoundation.org/UA/DI/" Version="1.03.1" PublicationDate="2021-09-07T00:00:00Z"&gt;

&lt;RequiredModel ModelUri="http://opcfoundation.org/UA/" Version="1.04.4" PublicationDate="2020-01-08T00:00:00Z"/&gt;

When loading a server configuration with the newer DI nodeset, the following happens:

- The nodes already present in the CPU are not overwritten.
- New nodes (for example, new data types or structures) are instantiated.

This "mixture" is not expected to cause any problems in the CPU, as DI nodesets of the OPC UA Foundation are downward-compatible.

When exporting the DI information model, the following cases must be distinguished:

- Standard SIMATIC server interface (CPU properties: OPC UA &gt; Server &gt; Export): The exported OPC UA XML file does not contain the DI information model, only references to it. If you use the XML export e.g. for OPC UA clients, then you have to add the used DI information model additionally for this, so that the OPC UA address space is consistent.
- OPC UA communication &gt; Server interface of type "Interface": The exported OPC UA XML file does not contain either the DI information model or references to it.
- OPC UA communication &gt; Server interface of type "Companion Specification": The exported OPC UA XML file still corresponds to the import nodeset. If the imported nodeset contained nodes from the DI information model, then these nodes are also contained in the exported file.

The DI information model is not integrated in the SiOME modeling editor. In SiOME, you must import the appropriate nodeset as described above. When exporting, SiOME exports all non-nodeset 0 nodesets, unless you have excluded the corresponding namespace from the export.

##### OPC UA server starts during start-up although it was deactivated in the configuration

Requirements:

- An S7-1500 CPU or SIMATIC S7-1200 CPU is running with an activated OPC UA server.
- You deactivate the OPC UA server in the TIA Portal.
- You load the changed hardware configuration to the CPU.

Result:

During start-up of the CPU, the OPC UA server starts for a short time before it is finally shut down in accordance with the newly loaded configuration.

This possibly irritating process is recorded in the diagnostic buffer.

##### Global Discovery Push (GDS Push) function

**Rejected certificates are not stored**

Unlike the description in section "Address model for push certificate management", rejected certificates are not currently stored by the OPC UA server of the S7-1500 CPUs. The "GetRejectedList" method therefore always returns an empty array (RejectedList).

**Update problem with downloaded certificates**

Under certain conditions, the CPU does not register a downloaded certificate (e.g. a new OPC UA server certificate, or an updated web server certificate). A certificate error may be signaled during a connection attempt in this case.

The update problem occurs only when the CPU still manages certificates that were provided during runtime (GDS Push) and when certificates are then transferred by loading the hardware configuration to the CPU. The certificates loaded via the hardware configuration are not registered by the CPU under these conditions.

Examples:

- You have initially enabled the GDS Push function and selected the option "... use certificates provided during runtime" for the certificate settings and loaded this configuration. The required server certificate as well as the trust lists/CRLs are provided exclusively via GDS Push methods in this case.
- You then change the hardware configuration by adding new certificates or changing existing certificates (e.g. web server certificates or certificates for secure PG/HMI communication). During loading, you have **not** deleted existing certificates provided during runtime so that you can use them later.  **Result**: The loaded server certificates are not registered by the CPU.
- The problem also occurs when you have disabled the GDS Push function and selected the option "... use configured and downloaded certificates" for the certificate settings and loaded this configuration. During loading, you have **not** deleted existing certificates provided during runtime so that you can use them later.  **Result**: The newly loaded OPC UA server certificate is not registered by the CPU.

Solution: When the CPU still has certificates that were provided during runtime and you want to transfer new/changed certificates by loading the hardware configuration to the CPU, proceed as outlined below:

- After loading the configuration, perform a "Memory reset" or restart the CPU (POWER OFF &gt; POWER ON). After these measures, the CPU reorganizes the loaded configuration and uses the current certificates.

##### PLC object not visible in the server address space

With very large projects, it can happen in rare cases that, despite successful compiling of the project and successful downloading to the CPU, the CPU node or PLC object is not visible in the address space of the OPC UA server. In this case the memory reserved for OPC UA in the CPU is insufficient.

Diagnostics, e.g. using UaExpert, returns the "Failed" server status.

Solution**:**

- Disable the standard SIMATIC server interface in the CPU properties if it is not required.
- Reduce the quantity or size of the elements that contribute towards the consumption of OPC UA resources. Reduce the number of nodes for server interfaces to fewer than 30000.

Additional measures:

- If you do not disable the standard SIMATIC server interface:   
  Reduce the number of tags in the address space of the OPC UA server, in particular, of tags with the data type structure.

  To remove tags from the address space, disable the option "Accessible from HMI/OPC UA" in the PLC tag table or in the data blocks.

  With data blocks, you also have the possibility to remove the DB with all tags completely from the address space. To do this, disable the option "DB accessible from OPC UA" in the properties of the DB.
- Reduce the length of names of the elements in extensive data structures.
- Shorten the descriptions of the nodes.
- Reduce the number of implemented methods.

##### Copying SCL program examples from the information system

SCL program code from the OPC UA programming examples, which was copied using the "Copy" icon in the information system and pasted in the program editor, cannot be compiled.

To copy the program code without errors, select the program code in the information system and use the "Copy" command in the shortcut menu or the key combination "Ctrl+C". Insert the program code in the program editor using the "Paste" command in the shortcut menu or using the key combination "Ctrl+V".

---

**See also**

[LocalizedText and ByteString data types](Configuring%20automation%20systems.md#localizedtext-and-bytestring-data-types-s7-1500-s7-1500t)

### Certificate checks during connection establishment (S7-1500 CPU)

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Certificate checks when establishing encrypted connections (e.g. OPC UA)

An S7-1500 CPU with firmware version V3.1 has an extended certificate check compared with predecessor versions.

Consequently, additional warnings/errors may appear in the diagnostics buffer (BadSecurityChecksFailed), which did not occur in predecessor versions. However, these messages do not prevent the connection from being established.

The following messages are involved:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 2852_0000 | Key Usage Certificate Sign invalid for non CA | In a CA-derived certificate, the keyCertSign bit has been set in the KeyUsage field despite not being permitted. |
| 2859_0000 | Basic constraints not critical | The BasicContraints field of the CA of a certificate is not set as "critical" despite always being required in CA certificates. |
| 2017_0000 | CA-Signed Application Instance CA Certificate | In a CA-derived certificate, the CA bit has been set despite not being permitted. |
| 2018_0000 | Self-Signed Application Instance CA Certificate | In a self-signed certificate, the CA bit has been set despite not being permitted. |

### Online access to a CPU with access protection via accessible nodes

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Password transfer to the CPU using an untrusted connection for CPU access via accessible nodes

Affected devices: S7-1500 CPU (firmware version V2.9), S7-1200 CPU (firmware version V4.5) and SW Controller (firmware version V21.9).

When you use the TIA Portal to access one of the CPUs listed above online via the "Accessible nodes" function and access to the CPU is protected by a password "no access (full protection)", the encrypted password may be transferred via an untrusted connection to the CPU during connection setup.

Only when a connection is made with a fully protected CPU from the list of accessible nodes is the password for the required access level requested and possibly transferred via an untrusted connection.

Solution:

- Only connect online via accessible nodes with CPUs in a protected environment that cannot be accessed externally.
- Make sure that you are connected to the correct CPU.
- For online access to accessible nodes use the password for the access level with the lowest access rights: In case of full protection, use the password for HMI access. This requires the configuration of a password for HMI access.

### HW ID of type "Hw_SubModule" for an HMI Panel IO device

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Determination of the HW ID with the "Hw_SubModule" type for an HMI Panel IO device

The "ID" parameter of the PROFIenergy "PE_START_END" program block must be supplied with the hardware identifier (HW ID) with the type "Hw_SubModule" of the IO device. The hardware ID with the "Hw_SubModule" type of the HMI Panel IO device is not displayed in the system constants on an S7-1500/S7-1200/ET200SP CPU, but it can be determined. To do this, the symbol for the IO device in the HMI panel with the type "Hw_Device" is determined in the list of PLC tags in the "System constants" tab and reduced by one, for example, "HMI_1_IE_CP_1~PROFINET_Interface_1~IODevice -1".

### Use of modules on the S7-1200

#### Content

Information that could not be included in the online help and important information about product characteristics.

#### Use of modules on the S7-1200

The modules listed below are not supported on the S7-1200.

| Family | Module | Order number |
| --- | --- | --- |
| S7-300 FMs | SM 338 | 6ES7 338-4BC01-0AB0 |
| FM 350-1 | 6ES7 350-1AH03-0AE0 |  |
| FM 350-2 | 6ES7 350-2AH00-0AE0, 6ES7 350-2AH01-0AE0 |  |
| FM 351 | 6ES7 351-1AH01-0AE0, 6ES7 351-1AH02-0AE0 |  |
| FM 352 | 6ES7 352-1AH02-0AE0 |  |
| FM 355 S | 6ES7 355-1VH10-0AE0 |  |
| FM 355 C | 6ES7 355-0VH10-0AE0 |  |
| FM 355-2 C | 6ES7 355-2CH00-0AE0 |  |
| FM 355-2 S | 6ES7 355-2SH00-0AE0 |  |
| S7-300 PtP-CP | CP 340 | 6ES7 340-1AH02-0AE0, 6ES7 340-1BH02-0AE0, 6ES7 340-1CH02-0AE0 |
| CP 341 | 6ES7 341-1AH01-0AE0, 6ES7 341-1AH02-0AE0, 6ES7 341-1BH01-0AE0, 6ES7 341-1BH02-0AE0, 6ES7 341-1CH01-0AE0, 6ES7 341-1CH02-0AE0 |  |
| Network component | Diagnostics repeater | 6ES7 972-0AB01-0XA0 |
| ET 200M | SIWAREX | 7MH4900-2AA01, 7MH4900-3AA01, 7MH4950-1AA01, 7MH4950-2AA01 |

#### Loading S7-1200 module comments to the PG/PC

In central configurations with S7-1200, comments of modules, submodules and signal boards are not loaded. With CPs/CMs, only the comments of the IE interface or DP interface are loaded. In distributed configurations with ET 200SP or ET 200MP, only the comment of the channels is loaded from the I/O modules.

### CP 343-2 on SIMATIC S7 Embedded Controller EC31-RTX

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### CP 343-2 on SIMATIC S7 Embedded Controller EC31-RTX

The module AS-Interface CP 343-2 (article no.: 6GK7 343-2AH01) can be inserted in an expansion rack of the SIMATIC S7 Embedded Controller EC31-RTX (article no.: 6ES7 677-1DDxx-0BB0), but the CP 343-2 cannot be operated with the EC31-RTX.

### Loading of S7-1500 CPUs (temporarily not possible)

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Error when loading (temporary error)

The loading of the CPU is denied with an error message (temporary error).

Possible cause: The OPC UA server of CPU is just starting. As soon as the server can be accessed again, loading is possible again.

### Loading of S7-1500 CPUs (SIPLUS)

#### Contents

Information that could no longer be included in the online help and important information about product features.

#### Behavior of a SIMATIC S7-1500 CPU SIPLUS (6AG1...) FW &lt;V2.5 with formatted memory card

Components involved:

- CPU 151x SIPLUS (6AG1...) with firmware version prior to V2.5
- SIMATIC memory card

If you load a SIPLUS CPU to a formatted SIMATIC memory card and then set the CPU to RUN, the CPU runs without errors. But once the power supply has been switched off and on again or if a memory reset (MRES) has been performed, the SIPLUS CPU goes into STOP with an error message. The error message states that the memory card is not recognized because it is missing, is of an incorrect type, contains incorrect data or is protected.

This behavior does not occur with a CPU 151x SIPLUS (6AG1...) with firmware version V2.5 or higher or if a configuration with a S7-1500 SIMATIC CPU (6ES7...) already exists on the memory card and is overwritten by a configuration with a SIPLUS CPU (6AG1...) of the same type.

Remedy:

1. A configuration with SIMATIC CPU must be loaded on the SIMATIC memory card. Only a CPU of the corresponding type must be available; the I/O is not required in this case.
2. The SIPLUS CPU is loaded to the card. The existing SIMATIC configuration on the memory card is overwritten with the SIPLUS configuration.

This procedure prevents an error message of the TIA Portal.

> **Note**
>
> The procedure ONLY works for online loading to the CPU. The error remains if the card is programmed by means of an external card reader.

If you want to load a CPU 1511-1 PN SIPLUS (6AG1 511-1AK00...), for example, do the following.

1. Insert a blank memory card with sufficient available memory into the SIPLUS CPU.
2. Configure a SIMATIC CPU of the same type, here an S7-1511-1 PN (6ES7 511-1AK00...). I/O modules are not required for the first load step.
3. Load the configuration onto the SIPLUS CPU.
4. Replace the SIMATIC CPU in STEP 7 with the SIPLUS CPU (6AG1 511-1AK00...) and complete the configuration with the planned I/O modules and distributed I/O devices.
5. Load the changed configuration onto the SIPLUS CPU.

### Module change for I-devices (S7-1500 CPU FW versions < V3.1 and V3.1)

#### Contents

Information that could no longer be included in the online help and important information about product features.

#### I-device and assigned IO controllers in a project: Module change

If you have configured an I-device (S7-1500 CPU) and want to change from this I-device to another S7-1500 CPU, this gives rise to the following scenarios, depending on the firmware versions used (valid for TIA Portal version V19):

| Current device | New device | Explanations |
| --- | --- | --- |
| S7-1500 CPU FW V3.1 | S7-1500 CPU FW V3.1 | Module can be changed |
| S7-1500 CPU FW &lt; V3.1 | S7-1500 CPU FW V3.1 | Module can be changed; the new I-device can **not** be used as a shared I-device within the project.  If you want to use the new I-device as a shared I-device within the project, you must deselect the "IO device" option at the relevant PROFINET interface of the current device before changing the module. |
| S7-1500 CPU FW V3.1 | S7-1500 CPU FW &lt; V3.1 | Module can be changed. You must deselect the "IO device" option at the relevant PROFINET interface of the current device before changing the module. |

### ET 200MP (IM 155-5 DP ST) on a WinLC RTX

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### ET 200MP (IM 155-5 DP ST) can currently not be operated on a WinLC RTX via PROFIBUS.

Components involved:

- PC systems with logic controller functionality WinLC RTX as DP master (all versions: EC31-RTX (F), WinAC RTX (F) software PLC), referred to as "WinLC RTX" below.
- ET 200MP (IM 155-5 DP ST) as DP slave

If you configure standard modules or F-modules in an ET 200MP and use a WinLC RTX as DP master, these modules are not configured by the DP master in the ET 200MP. After loading the configuration and startup of the components involved, the modules in the ET 200MP signal the missing parameter assignment by means of flashing green LEDs.

STEP 7 does not show the readiness for operation of the modules online (status "OK").

Remedy:

- Recommendation: Use an IM 155-5 PN interface module to connect the ET 200MP to a WinLC RTX via PROFINET IO.

  or
- If no F-modules are inserted in the ET 200MP: Use the GSD version of the ET 200MP on an WinLC RTX to configure the standard modules.

### Elimination of TS adapters

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Elimination of TS adapters

With the release of TIA Portal version V19, the following TeleService (TS) adapters are no longer supported:

- TS ADAPTER IE BASIC SIMATIC TELESERVICE (**6ES7972-0EB00-0XA0**)
- TS ADAPTER IE ADV. SIMATIC TELESERVICE (**6ES7972-0EA00-0XA0**)

These products have been discontinued since **October 1, 2023** and, consequently, they can no longer be configured in the TIA Portal user interface.

As a successor product, we recommend our SINEMA Remote Connect solution – the management platform for remote networks. It enables simple remote access via TeleService for remote maintenance applications.

Further information can be found at: [SINEMA Remote Connect](http://www.Siemens.com/sinema-remote-connect)

## Programming a PLC

This section contains information on the following topics:

- [General notes on PLC programming](#general-notes-on-plc-programming)
- [Note on software units](#note-on-software-units)
- [Information on named value data types](#information-on-named-value-data-types)
- [Notes on CEM (S7-1200, S7-1500)](#notes-on-cem-s7-1200-s7-1500)
- [Testing the user program](#testing-the-user-program)
- [Upgrading blocks](#upgrading-blocks)
- [Compatibility of PLC programs from older versions](#compatibility-of-plc-programs-from-older-versions)

### General notes on PLC programming

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Instance-specific attributes when importing blocks via TIA Portal Openness

In certain situations, the import rules can mean the loss of instance-specific attributes, such as start values.

#### Modifying the application cycle of an isochronous mode interrupt OB

When you change the "Application cycle (ms)" parameter of an isochronous mode interrupt OB, you implicitly also modify the hardware configuration. To ensure that the modified value for the application cycle duration becomes effective after the next loading process of the CPU you have to explicitly include the hardware configuration in loading. To this purpose select either the menu command "Load to device &gt; Hardware and software" or the command "Load to device &gt; Hardware configuration".

#### Information about network security

For communications access between TIA Portal and CPU or between HMI (except for HMI access using "GET/PUT communication") and CPU, there are integrated security functions. These provide greater protection from manipulation and higher access protection. To protect against unauthorized network access to a CPU with standardized communications access such as "GET/PUT", "TSEND/TRCV", "Modbus", "FETCH/WRITE", you should also take suitable additional measures (e.g. cell protection concept).

#### Functions from the global library "Long Functions" with PLCSIM (S7-1500)

The compilation process links the functions of the S7-1500 CPU family to the CPU to protect them from manipulation. Function from the global library "Long Functions" that are used in the CPU and have such a link cannot be loaded to a simulation. However, it is possible to replace such elements with their originals from the global library. These are not linked to a CPU.

#### Loading inconsistent programs to an S7-1500 CPU (S7-1500)

In TIA Portal, it is not possible to download inconsistent programs to an S7-1500 CPU without a consistency check. During the loading process, all blocks of the program are implicitly checked and are compiled again in the event of inconsistencies. If, however, there are programs on your CPU which were loaded with earlier versions of STEP 7, these programs could demonstrate inconsistencies.

In this case, note the following:

If you load an inconsistent program from a device, you will not be able to load the program back to an S7-1500 CPU unchanged afterwards, because a consistency check always takes place during the loading process and existing inconsistencies are corrected.

#### Data exchange between standard and F-program when using Team Engineering

To ensure data consistency between standard and safety program, you should:

- Do not exchange data via bit memory, use global data blocks instead.
- Limit access between safety programs and standard user programs to two standard data blocks.

You can find additional information on this in section 5.13 of the Programming Guidelines under: [https://support.industry.siemens.com](https://support.industry.siemens.com/cs/document/81318674/programming-guideline-and-programming-styleguide-for-s7-1200-and-s7-1500?dti=0&lc=en-WW)

### Note on software units

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Version Control Interface (VCI)

Versioning of Software Units via the Version Control Interface is not supported. You can, however, version the individual elements of a software unit in VCI.

#### Technology objects

Since technology objects cannot be contained in software units, it is not possible to define namespaces for technology objects.

#### Loading software units

In the following case, you cannot load a software unit into the device individually:

- You have created a new organization block in a software unit.
- The organization block is assigned to an event that has already been assigned another OB in another software unit.

In this case, load the entire PLC program into the device.

#### Namespaces for PLC tags

It is not possible to define namespaces for PLC tags.

#### Namespaces in libraries

Libraries have the following restrictions regarding namespaces:

- Namespaces are not considered when harmonizing names and path structures.
- When you export types from libraries via Openness, namespaces are not included in the export.

#### Display of namespaces according to IEC 61131-3

Program elements located in namespaces are represented in IEC-compliant notation:

- The name of the program element is not in quotation marks.
- The namespace precedes the program element name, separated by a dot.

Some editors in the TIA Portal, e.g. the cross-reference list, do not yet show namespaces in V18.

---

**See also**

[Introduction to software units](Using%20software%20units%20%28S7-1500%29.md#introduction-to-software-units-s7-1500)
  
[Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

### Information on named value data types

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Named value data types in F-programs

You can use named value data types in F-programs that do not have know-how protection. In know-how-protected F-programs, the use of named value data types is not possible.

#### Online functions: HMI, online monitoring, tracing and web server

In V19, you cannot yet display the declared names of the named values online. Online functions such as HMI, monitoring, tracing and web server therefore only display the basic data type and its current value.

Example: For the following named value data type, only values 1, 2, or 3 are displayed online. The declared names "RED", "YELLOW", "GREEN" cannot be displayed.

`TYPE`

`nvtTrafficLight : INT`

`(`

`RED := 1,`

`YELLOW := 2,`

`GREEN := 3`

`);`

`END_TYPE`

#### Named value data types in the online view

Named value data types that exist only online cannot be displayed in the project tree or opened via the "Online access" folder.

Load the named value data type from the device instead and open it in the offline project.

#### Uploading from device

If you select a CPU or a Software Unit when using the "Upload from device" function, the named value data types in use are also uploaded. However, in V19 it is no longer possible to upload individual named value data types from the device to the offline project.

#### Downloading with synchronization

In team engineering, several users can work on one project with several engineering systems at the same time and access one S7-1500 CPU. To ensure consistency within the shared project, the changed data is synchronized prior to loading so that nothing is overwritten unintentionally. In V19, named value data types are not taken into account during synchronization.

#### Cross-references and program information

Cross-references and program information cannot yet be displayed for named value data types in V19.

#### Detailed comparison

No detailed comparison is carried out for documents in the TIA Portal. However, you can compare the documents with standard tools.

#### Namespaces

If you change the namespace default of a software unit, you cannot apply the change to underlying named value data types using the "Apply namespace to underlying elements" button. Change the namespace manually instead.

#### Textual block interface

In the textual block interface of an SCL block, you cannot use named value as default values for block parameters or as ARRAY limits.

Example:

The following declaration is not possible:

myInt: nvtTrafficLight := nvtTrafficLight#GREEN;

The following declaration is possible:

myInt: nvtTrafficLight := 3;

#### Libraries

Named value data types cannot be used as types in libraries. However, you can define it as a master copy and insert it into your program.

#### Copying named value data types between TIA Portal instances

If you copy named value data types to another instance of the TIA Portal, you should save the project beforehand. Always use the saved version of a named value data type when copying. Unsaved changes to named value data types cannot be copied.

---

**See also**

[Basics of named value data types](Data%20types.md#basics-of-named-value-data-types-s7-1500)

### Notes on CEM (S7-1200, S7-1500)

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Tutorial

> **Note**
>
> **Video tutorial on CEM**
>
> [Automate in less than 10 minutes: Efficient engineering with Cause Effect Matrix (CEM)](https://youtu.be/FaR9rVXUkJo)

#### CEM in F-programs

It is not possible to generate fail-safe blocks with CEM. Therefore, you cannot use CEM blocks in F-programs.

#### Modifying operands during monitoring

It is not possible to modify operands during monitoring in the CEM Editor.

Insert the operands that you wish to modify into a watch table. Alternatively, you can also modify the operands in the open data block or in the PLC tag table.

#### Search

The local and global search is not supported in the CEM editor.

#### Implicit data type conversion

No implicit data type conversion is performed at the inputs and outputs of the CEM instructions. Only interconnect the operand of the required data type there.

#### Block comparison

The detailed comparison of CEM blocks is not supported.

#### Print

CEM blocks cannot be printed. A print preview is also not available.

#### Multilingual project texts

It is not possible to export and import project texts for translation.

#### Openness

CEM blocks cannot be exported and imported via Openness.

#### Multiple instance capability

CEM blocks do not have multiple instance capability.

#### Version Control Interface

Versioning via the Version Control Interface is not supported.

---

**See also**

[CEM programming language](Creating%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#cem-programming-language-s7-1200-s7-1500)

### Testing the user program

This section contains information on the following topics:

- [Information on testing with the watch table](#information-on-testing-with-the-watch-table)
- [Information on testing with the force table](#information-on-testing-with-the-force-table)
- [Information on testing with breakpoints](#information-on-testing-with-breakpoints)

#### Information on testing with the watch table

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Loading data blocks during an active control job

Loading changed data blocks during an active control job can result in unforeseen operating states. The control job continues to control the specified address, although the address assignment might have changed in the data block. Complete active control jobs before loading data blocks.

##### "Enable peripheral outputs" function

The function "Enable peripheral outputs" in not available for CPUs of the S7-1500 series in TIA Portal.

This function can only be executed with an S7-300, S7-400 or S7-1200 CPU in TIA Portal.

##### Testing of programs that were migrated into the TIA Portal from older STEP 7 versions.

To monitor and test a program migrated from an older STEP 7 version, you first need to compile and download the program with the current STEP 7 version.

#### Information on testing with the force table

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Forcing tags for direct I/O access (S7-300)

If you use direct I/O access for an S7-300 CPU in your user program, forcing this I/O address is not permitted.

##### Example

If I/O access to the address "IB0:P" takes place in the user program, it is not permitted to force the following I/O address areas: I0.0:P, IB0:P, IW0:P and ID0:P.

#### Information on testing with breakpoints

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Setting breakpoints in the standard user program at S7-1500 F-CPUs

When a breakpoint is reached and the program is stopped for longer than the maximum F-scan cycle monitoring time, the CPU goes into STOP. It is not possible to continue the program. If you want to change back to RUN mode after the "HOLD" in order to continue testing your default user program, use S7 PLCSIM for your test, or test your program without F-components.

Further information about testing with breakpoints at F-CPUs is available in the "SIMATIC Safety – Configuring and Programming" manual.

### Upgrading blocks

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Upgrading know-how-protected blocks (S7-1200/1500)

When upgrading to the current version, know-how protected blocks that were set up with an older version of TIA Portal can be loaded in the controller without entering a password and are executable.

To open and edit these blocks in the current version, proceed as follows:

- For blocks with know-how protection set up using version V13 SP1 or higher:

  - Remove the know-how protection in the current version, edit the block and reset the know-how protection.
- For blocks with know-how protection set up using a version earlier than V13 SP1:

  - Remove the know-how protection in V13 SP1 and then update the block to the current version. Now edit the block and reset the know-how protection in the current version.

#### Upgrading of GRAPH blocks (S7-300, S7-400, S7-1500)

After upgrading a project from a version lower than V15, check whether repaired GRAPH blocks are listed in the log file and test whether these blocks are executable in your program.

If a project that contains GRAPH blocks is upgraded from V15.x, the program blocks must be compiled before they can be monitored.

#### Upgrading of blocks that contain alarms

If you are upgrading a project from a TIA Portal version V15.1 or earlier, you must re-compile all the blocks containing alarms and load them to the PLC before monitoring is possible again. Under certain circumstances, this means that the PLC has to be put into stop mode.

#### Updating device specifications

When upgrading your project, internal device specifications of the used employed CPUs are updated in certain cases.

The following message indicates that an update is being performed: "The device configuration of the PLCs in the project has been updated."

The update has no effect on the program running in the CPU.

---

**See also**

[Compatibility of PLC programs from older versions](#compatibility-of-plc-programs-from-older-versions)

### Compatibility of PLC programs from older versions

This section contains information on the following topics:

- [Compatibility of PLC programs from versions prior to V19](#compatibility-of-plc-programs-from-versions-prior-to-v19)
- [Compatibility of PLC programs from versions prior to V18](#compatibility-of-plc-programs-from-versions-prior-to-v18)
- [Compatibility of PLC programs from versions prior to V17](#compatibility-of-plc-programs-from-versions-prior-to-v17)
- [Compatibility of PLC programs from versions prior to V16](#compatibility-of-plc-programs-from-versions-prior-to-v16)
- [Compatibility of PLC programs from versions prior to V15.1](#compatibility-of-plc-programs-from-versions-prior-to-v151)
- [Compatibility of PLC programs from versions prior to V15](#compatibility-of-plc-programs-from-versions-prior-to-v15)
- [Compatibility of PLC programs from versions prior to V14 SP1](#compatibility-of-plc-programs-from-versions-prior-to-v14-sp1)
- [Compatibility of PLC programs from versions prior to V14](#compatibility-of-plc-programs-from-versions-prior-to-v14)
- [Compatibility of PLC programs from versions prior to V13 SP1](#compatibility-of-plc-programs-from-versions-prior-to-v13-sp1)

#### Compatibility of PLC programs from versions prior to V19

##### Compatibility

In V19, you can generally continue to use all PLC programs that were created with older versions of TIA Portal. However, because improvements and bug fixes to the compiler were made in V19, in a few cases the program may behave differently after the upgrade or you may have to adapt the program code manually. These cases are described in detail below.

##### **SCL: Name conflicts between data blocks and elements from system libraries**

If a data block was given a name that was already assigned for an element from the system library, this could result in compile errors. This behavior has been corrected.

Nevertheless, it is still not recommended to assign a code block, data block, data type, tag or constant a name that is a keyword or has been assigned for an element from the system library.

##### **Session log of the program editor**

The technology for storing the session log for the program editor has been revised in V19. Therefore, when upgrading to V19, individual information cannot be retrieved from the session log of the V18 project. However, if you continue to work with V19, the session log is still available to you as usual.

#### Compatibility of PLC programs from versions prior to V18

##### Compatibility

In V18, you can generally continue to use all PLC programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected in V18, there may be some rare cases in which the program reacts differently after the upgrade or that you may have to adjust the program code manually. These cases are described in detail below.

##### Online/offline differences after upgrading to V18

If no changes were made to the PLC program in an upgraded project, an online/offline difference is usually not indicated. The right column in the project tree shows the following symbol: ![Online/offline differences after upgrading to V18](images/20569116683_DV_resource.Stream@PNG-de-DE.png)

If an online/offline difference is shown when programs were not modified, the problem is most likely a checksum inconsistency. The right column in the project tree shows the following symbol: ![Online/offline differences after upgrading to V18](images/20569197579_DV_resource.Stream@PNG-de-DE.png)

For more information, refer to the Compare editor:

- Online/offline differences in the following categories are caused by checksum inconsistencies. The program is compatible despite the checksum inconsistency, that is, the program execution is not affected by the upgrade. You can establish an online connection and start monitoring immediately after upgrading:

  - "Program code" checksum
  - "Event" checksum
  - Checksum "Interface of published blocks without comments (software units)"
- Online/offline differences in the following categories, however, indicate actual differences in the program code and mean that you must recompile and reload the program.

  - All checksums in the "Target data" category

See also: [Overview of the compare editor](Editing%20project%20data.md#overview-of-the-compare-editor)

##### Inverted result of logic operation at the enable input EN (FBD, S7-1200/S7-1500)

Under the following conditions, an inversion at the enable input EN was not correctly evaluated:

- In an FBD network, a multiple instruction is directly connected to the negated EN input of an instruction.
- The instruction has additional Boolean inputs.
- At least one of the Boolean inputs is not directly supplied with an operand.

This behavior has been corrected in V18. If you use inversions at the enable input EN, ensure that the program flow is correct after upgrading.

##### **SCL: Math instructions with untyped constants (S7-1200/S7-1500)**

The behavior of a math instruction in which one of the operators is a typed LReal expression and another operator is an untyped 2#, 8# or 16# constant has been changed in SCL. The untyped constant is always interpreted as an unsigned integer.

---

**See also**

[Upgrading blocks](#upgrading-blocks)
  
[General information on upgrading projects](Editing%20projects.md#general-information-on-upgrading-projects)

#### Compatibility of PLC programs from versions prior to V17

##### Compatibility

In principle, you can continue to use in V17 all PLC programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected there in V17, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

##### Compatibility of data blocks after upgrading to V17

After upgrading data blocks that are derived from a PLC data type (UDT), online/offline differences may be displayed, even though the online and offline programs are identical.

These differences are mostly due to a checksum inconsistency. The blocks or PLC data types are compatible despite the checksum inconsistency, i.e. the program execution is not affected by the upgrade. You can establish an online connection and start monitoring immediately after upgrading.

For more information, refer to the Compare editor:

- Online/offline differences in the "Block properties" category are due to checksum inconsistency. The blocks or PLC data types are compatible.
- On the other hand, online/offline differences in the "Target data" category indicate actual differences in the program code and mean that you have to recompile and reload the program.

See also: [Overview of the compare editor](Editing%20project%20data.md#overview-of-the-compare-editor)

##### Loading and monitoring changed data blocks (S7-1200/S7-1500)

The following rule has been in effect when loading blocks:

If the block in the offline project had a newer interface time stamp than in the online project, the block always had to be reloaded. As a result, the tag values were always reinitialized. Inconsistencies in the running plant operation could result.

Starting with V17, the time stamps are no longer compared, the structure of the online and offline blocks is compared instead. Data blocks are only reinitialized when downloaded if their structure has actually changed. Another advantage is that in these cases the program status can be continuously monitored, even if differences are displayed in the online-offline program.

Note:

Changes to the program code in the blocks of the GRAPH, CEM or CFC languages can result in a change of internal interface data. These changes require a reinitialization even if no structural changes are visible at the block interface.

**Examples**:

You can download a data block without reinitialization in the following cases:

- You generate a data block with the same structure multiple times from an external source, via the Openness function or via the Version Control Interface.

  Note: When you generate a GRAPH block or a block, whose memory reserve is activated, via the functions mentioned, the block must be reloaded and reinitialized.
- You add a parameter to the interface and then delete it again.

> **Note**
>
> **Use of the function for blocks created with a version prior to V17 or with an S7-300/400 CPU.**
>
> The new function is only available for blocks whose interface has already been changed and loaded in V17 with an S7-1200/1500 CPU. Only then is the information about the online block structure available and can be used for a comparison during loading in the future.

##### Open data blocks

When opening data blocks, it is tested whether a block contains inconsistent snapshots of actual values. These will be deleted and you will be informed with a message. Running the program in the CPU is not influenced by this.

##### SCL: Derived data types in arithmetic expressions or Boolean operations

The rules for derived data types have been standardized. It is now no longer permitted to use these data types in arithmetic expressions or Boolean operations in SCL.

**Example:**

The following expressions are no longer permissible in V17:

`#myWord := #myHW_IO AND 100;`

or

`#myInt := #myHW_IO + 5;`

In such cases, use a temporary tag of the basic data type:

`#myTempUInt := #myHW_IO;`

`#myINt := #myTempUInt + 5;`

Alternatively, you can also convert the operand explicitly to the basic data type:

`#myInt := UINT_TO_INT(#myHW_IO) + 5;`

##### **Actual parameters of data type REMOTE (S7-1200/S7-1500)**

The parameter passing rules for the REMOTE data type have been unified. It is no longer allowed to pass an operand of the REMOTE data type as an actual parameter if it is in an instance.

**Example:**

The actual parameter "myRemote" of the REMOTE data type must no longer be passed in V17 because it is in an instance.

`"Block_2"("Block_1_DB".myRemote);`

In addition, it is no longer permitted to interconnect a formal parameter of the data type VARIANT with an actual parameter of the data type REMOTE.

**Example:**

The actual parameter "myRemote" of the REMOTE data type must no longer be passed in V17 to an actual parameter of the DATA type VARIANT.

`"Block_1_DB"(myVariant:=myRemote);`

##### FBD: CMP== (equal) and CMP&lt;&gt; (unequal) with data type VARIANT (S7-1200/S7-1500)

It is no longer permissible in the FBD to negate the output of the instructions "CMP==" and "CMP&lt;&gt;" with the function "Invert RLO" when "VARIANT" is selected as data type. If you have used one of the two instructions with the data type "VARIANT" and a negated output, an error is signaled during compilation. Use the function "Software (rebuild all)" to locate all uses in your program.

To remedy the error, use the instruction "CMP&lt;&gt;" instead of "CMP==" and vice versa. Remove the negation of the output.

##### ARRAY access error (S7-1200/S7-1500)

In rare cases, no check was performed for ARRAY access errors if the access was performed in a loop. This behavior has been corrected. In case of ARRAY access errors, the CPU goes to STOP or performs a programmed error handling operation.

##### **Importing source files (S7-1200/S7-1500)**

Blocks, instructions or PLC data types may contain write-protected parameters with start values that must not be initialized. For example, certain parameters of IEC timers must not be initialized as otherwise their function would be disturbed. As of V17, the import of external source files is therefore rejected when they contain initializations for write-protected parameters.

If the maximum number of 600 errors is reached during the import of an SCL file, the import is aborted. The source file cannot be imported.

##### Serialize (S7-1500)

In V17, it is once again possible to link to the parameter "DEST_ARRAY" an operand whose access path contains an ARRAY with a variable index.

Example:

`DEST_ARRAY => "myDB".buffersArray[#fieldNo].receiveBuffer`

##### Serialize and Deserialize (S7-1200/S7-1500)

The optimized versions of the Serialize and Deserialize instructions as of V2.1 require more work memory than their predecessor versions due to the complexity of the processed data.

With Serialize/Deserialize version 2.2, it is no longer permissible to interconnect an element of a technology object (e.g. TO_SpeedAxis.Statusword) to input or output parameters for serialize (SRC_VARIABLE/DEST_ARRAY) or deserialize (SRC_ARRAY/DEST_VARIABLE).

##### SCL: Implicit data type conversion

When the SCL block was called, the data type of the in/out parameter (InOut) was not implicitly converted to the target data type. This behavior has been corrected. If you use SCL blocks in your program and transfer in-out parameters, check that the program is running correctly after upgrading.

##### Transfer of an ARRAY to the VARIANT data type

In rare cases, an ARRAY that was part of a structure and whose access path had a dereferencing, returned an incorrect length when it was transferred to a VARIANT. This behavior was corrected in V15.0.1.

**Example**

#ArrayLength := "myFC"(myVARIANT := #ref_to_mySTRUCT^.myARRAY);

//"myFC" calculates the length of the array that is transferred at the "myVariant" input.

---

**See also**

[Upgrading blocks](#upgrading-blocks)
  
[General information on upgrading projects](Editing%20projects.md#general-information-on-upgrading-projects)

#### Compatibility of PLC programs from versions prior to V16

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

In principle, you can continue to use in V16 all PLC programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected there in V16, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

##### Compatibility after upgrading a project to V16

After upgrading a project to V16, online/offline differences might be indicated although the online and offline programs are identical. These differences are due to optimization of the calculation of checksums in V16. But the blocks are still compatible in most cases.

In some rare cases, however, you might have to recompile and download the project again due to the changes in the checksum calculation before you can monitor and test the project online.

You can find more information in the log files for upgrading in the project properties. If a checksum inconsistency is reported in the log files, then the online/offline differences are due to the changed checksum calculation.

You can find additional information in section: "[Online connection after upgrading a project](Editing%20projects.md#general-information-on-upgrading-projects)".

##### Upgrading of GRAPH blocks (S7-300, S7-400, S7-1500)

After upgrading a project to V16 from a version lower than V15, check whether repaired GRAPH blocks are listed in the log file and test whether these blocks are executable in your program.

If a project contains GRAPH blocks and is upgraded from V15.x to V16, the program blocks have to be compiled before they can be monitored.

##### Software units

As of V16, the following rules apply for the name of a software unit:

- Permissible characters are all alphanumeric characters and the underscore.
- The maximum number of characters is 125.
- The name of a software unit must be unique for the entire CPU and no block with the same name must exist in the CPU.

If the software unit in your program does not conform to these rules, a syntax error is displayed after the upgrade. In this case, change the property of the software unit and recompile the program.

##### Syntax check for instances (LAD, FBD, STL, GRAPH)

A more thorough check is now performed when calling a function block to determine whether the specified instance data block is of the type of the called FB. In addition to the block number and the block structure, the block name is now also being checked.

A syntax error is output after the upgrade in case of inconsistencies. In this case, check the type of the instance data block in the "General" section of the block properties. If the type does not match the called FB, you must change the block call and specify a matching instance.

##### Instructions "UPPER_BOUND" and "LOWER BOUND" (LAD, S7-1200/S7-1500)

The enable input "EN" of the two instructions "UPPER_BOUND" and "LOWER BOUND" is now evaluated correctly. If the input "EN" has the signal state "0", the instruction is not executed and the enable output "ENO" has the signal state "0". When you use one of the two instructions, check whether your program sequence is still the same after the upgrade.

##### Instruction "S_CONV" (LAD)

The enable input "EN" of the "S_CONV" instruction was not evaluated in older TIA Portal versions during conversion from (W)Char to (W)String when no parameter was interconnected at the enable output "ENO". This behavior has been corrected. When you use "S_CONV", check whether your program sequence is still the same after the upgrade.

##### Initialization of STRUCT data type when importing external source files (SCL)

The initialization rules for STRUCT have been made uniform. The initialization lists are now always evaluated according to the same rules, regardless of whether you are working in the tabular form or in the textual block interface.

If you use a different syntax in an initialization list and initialize some elements by specifying the element name and others only by specifying the value, for example, check your program after importing it into TIA Portal V16.

The following example shows how the structure elements in V16 are evaluated both in tabular form and in the textual block interface:

`myStruct : Struct`

`member_1 : Int;`

`member_2 : Int;`

`member_3 : Int;`

`member_4 : Int;`

`member_5 : Int;`

`End_Struct:=(1,mem_3:=33,2,3);`

`//The structure elements are initialized as follows:`

`//mem_1 := 1;`

`//mem_3 := 33;`

`//mem_4 := 2;`

`//mem_5 := 3;`

##### AT declaration

In rare cases, incorrect values were written to block parameters that immediately followed an AT declaration in the interface. This behavior has been corrected.

It is no longer possible to overlay block parameters of the data types BOOL, BYTE, SINT, USINT or CHAR with tags of the data types STRUCT and UDT. Overlays with ARRAY type tags are only possible as long as the array size does not exceed the data size of the overlaid type.

If you use AT declarations, check your program after the upgrade.

##### "MOVE" instruction

With the "MOVE" instruction you can only copy all the tags of a data block into another data block ("DA a" := "DB b") if both blocks have the same structure, i.e. the number, the data type and the declaration sequence of the declared tags are identical. In addition, both data blocks must have the same storage format (optimized or non-optimized).

If both blocks are available in an optimized storage format, all tags of both blocks must be either retentive or non-retentive.

##### "MOVE" instruction (AWL)

As of TIA Portal V16, it is no longer possible in AWL to supply the OUT output of a MOVE instruction with a tag of the VARIANT data type from the sections InOut or Out of the block interface.

##### Instructions "SCATTER_BLK" and "GATHER_BLK" (SCL)

As of V16 the permissible data types have been restricted: When using structures (STRUCT or PLC data type) as parameters, these must only contain tags of the data type BOOL.

##### Non-typed constants (SCL)

The semantics check for non-typed constants has been adapted to the other programming languages: If a non-typed constant is not compatible with the assigned operand, a compilation error is always reported if the IEC check is activated.

##### Addressing ARRAYs via variable index and I/O access (S7-1200)

In a CPU of the S7-1200 series, addressing ARRAYs via a variable index in combination with the I/O access identifier ":P" is no longer possible.

Example of an invalid ARRAY addressing:

`#array[0, #myIndexTag, 2]:P`

Examples of permissible ARRAY addressing with I/O access:

`#array[0, #myConstant, 2]:P`

`#array[0, 1, 2]:P`

Examples of permissible ARRAY addressing with variable index:

`#array[0, #myIndexTag, 2]`

##### Block size when using ARRAYs in structures

When using structures (STRUCT) that contain more than one ARRAY element, the following error can occur:

If multiple ARRAY accesses were outside the valid range, the CPU did not switch to STOP but an ARRAY element was accessed.

This behavior has been corrected in V16: The CPU switches to STOP in this case or runs a local or global troubleshooting if it is programmed.

This correction allows for the respective blocks to be larger.

##### Assignment of non-typed constants (SCL)

An error message is generated for assignments of non-typed constants to tags of the "Real" type when the IEC Check is enabled, and when the constant is also located within the value range of an LReal and outside the value range of a Real.

---

**See also**

[Upgrading blocks](#upgrading-blocks)

#### Compatibility of PLC programs from versions prior to V15.1

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

Basically, you can continue to use all PLC programs that were created with older versions of TIA Portal in V15.1. However, because improvements were made to the compiler and errors corrected there in V15.1, in rare cases the program may react differently after the upgrade or you may have to adapt the program code manually. These cases are described in detail below.

##### Processing sequence of function calls in SCL (S7-1200/S7-1500)

In older versions of the TIA Portal, the processing sequence of assignments containing expressions or function calls was not always clear. Processing was not carried out consistently from right to left; rather, in certain cases, parts of the expression on the left side were evaluated first.

This behavior was corrected in V15.1 so that the right side of the assignment is always calculated first and then the left side is determined.

Example:

`#myArr["FC_1"()]:= #x + #y;`

In earlier versions, the "FC1" was run here first in order to determine an ARRAY element. Then, #x + #y was calculated.

As of V15.1, the program is now correctly processed from right to left: First, #x + #y is calculated and then "FC1" is run.

This correction can have the result that your program behaves differently after upgrade, e.g. when the tags #x or #y are set in "FC1". Therefore, please check your program after upgrading.

##### **Comparators (SCL S7-1200 &gt;= 4.2 and S7-1500 &gt;= 2.0)**

When comparing two instance data blocks via comparison instructions in SCL, not the structure of the blocks but only the block numbers are compared. As of V15.1, an error message during compiling notifies you that this instruction may not return the desired result (FALSE is generally returned because the numbers of the blocks are different).

Example:

The result of the following comparison instruction is FALSE even if the structure of the two blocks is identical.

IF "MyDBofFB" = "MyDBofSameFB" THEN …

##### Importing IEC timers (S7-1200/S7-1500)

IEC timers contain read-only parameters, e.g. ET (current time value). In older versions of the TIA Portal, the start values of these read-only parameters were overwritten in some cases when external source files were imported. This behavior was corrected with V15.1: Start values for read-only parameters are now ignored when source files are imported. Instead, the default values of the data type are used. Therefore, please check your program after an import.

##### **Replacing invalid Unicode characters during upgrade**

Invalid Unicode characters in your program are corrected when upgrading to V15.1. For example, invalid characters in string constants are replaced with the escape sequences defined by IEC. This can change the checksum of the program and indicate differences between the online and offline program. Compile your program and reload it in this case.

##### Instructions "SCATTER" / "SCATTER_BLK" and "GATHER" / "GATHER_BLK" (SIMATIC S7-1200/1500)

You can use the "SCATTER" / "SCATTER_BLK" instructions to parse the bit sequence into individual bits. You can use the "GATHER" / "GATHER_BLK" instructions to combine individual bits into a bit string.

The values with which the instructions work must not be in the I/O area or in the DB of a technology object, since data consistency cannot be guaranteed in these areas.

As of V15.1, this rule undergoes a more precise syntax check. If you have the above-mentioned instructions with invalid input parameters in your program, an error is now reported during compiling.

As a remedy, you can first copy the tags to a temporary memory area and transfer them from there to "SCATTER" or "GATHER" instructions.

##### Instructions "BLKMOV" / "UBLKMOV" and "FILL" / "UFILL"

Use the "BLKMOV" / "UBLKMOV" and "FILL" / "UFILL" instructions to copy the contents of a memory area (source range) to another memory space (target range). If these instructions access a memory area that does not exist, a programming error is output. In previous versions, in rare cases an error code was generated at the "RET_VAL" parameter instead of a programming error. This behavior has been corrected for S7-1500 CPUs as of firmware version 2.6.

##### "RUNTIME" instruction (SCL/STL S7-1200/S7-1500)

The "Mem" parameter of the "RUNTIME" instruction has the data type "LREAL" and can only be used with a tag of this data type. Implicit conversion is not possible here. In V15.1, this rule undergoes a more precise syntax check. If you have provided the "Mem" parameter of the "RUNTIME" instruction with an invalid data type in your program, an error is now reported during compiling.

#### Compatibility of PLC programs from versions prior to V15

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

In principle, you can continue to use in V15 all PLC programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected there in V15, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

##### S7-GRAPH: Implicit conversions "Hardware data type &lt;&gt; INT"

As of TIA Portal V15 it is no longer possible to program implicit conversions of hardware data types (for example INT -&gt; DB_ANY or DB_ANY -&gt; INT), as is already the case in LAD, FBD, STL and SCL.

Please use either the UINT data type or an explicit conversion instead.

##### Subcategories in ProDiag (S7-1500)

From TIA Portal V14 SP1 update 2 the individual subcategories for ProDiag are no longer added manually, but activated or deactivated in the "Activation" column.

This results in the fact that following the upgrade of a project &lt;V14 SP1 Update 2, which uses already existing subcategories in at least one monitoring, the "Repair" button must first be selected before you can create new subcategories.

##### Instructions "(U)MOVE_BLK" and "(U)FILL_BLK" (S7-1500)

The instructions "(U)MOVE_BLK" and "(U)FILL_BLK" only accessed the process image in TIA Portal &lt;= V15 when directly accessing the I/O.

This behavior has been corrected and now causes a runtime error because direct I/O access is not permitted for BLK instructions.

##### Program loops in SCL (S7-1200/S7-1500)

In S7-1200/S7-1500 it is not possible to change the index of a program loop from within the loop with SCL.

The following program example would therefore be invalid:

FOR #i := 1 TO 10 DO

#i := #i + 1;

END_FOR;

As of TIA Portal V15, a more exact syntax check is conducted in this regard during compilation and a compilation error is output.

##### Return values for functions in SCL

The behavior for functions whose return values have a structured data type has been adjusted. Structured data types are e.g. PLC data types or STRING.

Regardless of whether or not the ENO output uses the function, until now, it could happen that a temporary working copy of the function value was created although no working copy was created by the same call without ENO. The assignment of these temporary copies to the interconnected tag is made when the function is exited.

This behavior was changed as follows:

Using the output parameter ENO now no longer has any influence on whether the return value is transferred with a copy or with a reference. If the return value has a structured data type, it is generally transferred as a reference. The transfer rules are described in detail in the section "Transfer parameter as copy or as pointer".

##### LDT_TO_DATE in SCL (S7-1500)

The reaction of LDT_TO_DATE to a conversion error in runtime was corrected.

##### Comparison of an ARRAY element with a variable of the data type "VARIANT" in SCL (S7-1200/1500)

In the past the comparison of a variably indexed ARRAY element with a VARIANT was not carried out correctly in some cases. Instead of the ARRAY element the complete ARRAY was used for the comparison.

This behavior has been corrected in V15: The indexed ARRAY element is now evaluated for the comparison. If you use such comparisons in your program, you have to check the respective block after upgrading.

Example:

`IF (#my_Array[#1] = #my_variant) THEN…`

In the past "my_variant" was compared with "my_Array". As of V15 the comparison is carried out correctly and "my_variant" is compared with Element #1 of "my_Array".

##### Instruction "GetSymbolPath" (S7-1200/S7-1500)

If an FB interconnects a static variable to a formal parameter of a call and a nested block uses "GetSymbolPath" V1.0 or V1.1 for the parameter, compiling this block results in an additional display of the DB name before the name of the static variable, however, without a period as a delimiter and without replacement of the #. Version V1.2 of "GetSymbolPath" shows the path correctly with a period as a delimiter and without #.

If you use the "GetSymbolPath" instruction in your program, you should use the "GetSymbolPath" V1.2 instruction after upgrading to &gt;=V15.

##### Instruction "GetInstancePath" (S7-1200/S7-1500)

If an FB interconnects a static variable to a formal parameter of a call and a nested block uses "GetInstancePath", compiling this block results in an additional display of the DB name before the name of the static variable.

##### Additions and subtractions with DTL/LDT/DT

In additions and subtractions with the data types DTL/LDT/DT, non-typed constants can no longer be used. A syntax error is signaled.

The following arithmetic operations, for example, are no longer possible:

`#myDTL + 1`

`#myLDT + 1`

`#myDate_And_Time +1`

Use constants of the data type "Time" or "LTime" instead

`#myDTL + TIME#1d`

`#myLDT + TIME#1ms`

`#myDate_And_Time + LTIME#1ns`

##### Runtime information (S7-1200/S7-1500)

The extended instructions "GetInstanceName", "GetInstancePath", "GetSymbolName", "GetSymbolPath" and "GetBlockName" now behave in the same way in all programming languages: If the character string to be output does not fit in the output parameter on account of size restrictions, the name is truncated and the character "..." is displayed at the end of the character string.

##### ARRAYs of multi-instances

In the past ARRAYs of multi-instances could not be addressed correctly when variables were used to address the index of a multi-instance that was in turn instantiated in a further multi-instance, that in turn was an element of an ARRAY of multi-instance.

Example:

`#MyMultiArray[#index].MyMultiMember := 10;`

This behavior has been corrected in V15:

If you have used such accesses in your program, you may have to check the affected block after upgrading and possibly recompile it.

##### Block parameters of the data type "VARIANT" (S7-1200/1500)

As is already the case in LAD, FBD, STL and GRAPH, it is now no longer possible either in SCL to assign and instance DB as the actual parameter to a formal parameter of the data type "VARIANT".

An exception is formed by instance DBs that are derived from a PLC data type or a system data type. You assign these to a block parameter of the data type "VARIANT" in all programming languages.

It is no longer possible to assign a write-protected tag for a block parameter of the data type "VARIANT" as an actual parameter.

If possible, remove the write protection of the variable. If this is not possible, check how you can change your program to prevent access to the write-protected variable. If you only want to have read access, for example, you can copy the content of the write-protected variable in the calling block into a different variable without write protection. Subsequently you can hand over this variable as an actual parameter.

##### Importing external sources

When importing an external source in which an instruction is used as a multi- or single-instance, the entire program was changed to the instruction version used in the source in the past. As of Version V15 of TIA Portal this behavior has been corrected: The instructions already contained in the project are no longer changed over, but rather retain the instruction version configured by you.

If the project contains different versions of an instruction after the import, a syntax error is reported. In this case compile the complete project again. To do so, select the "Program blocks" folder in the project tree and select the command "Compile &gt; Software (only changes)" or "Compile &gt; Software (compile all)" from the shortcut menu.

##### Size of ARRAY of BOOL/BYTE/CHAR (S7-1500)

In the past ARRAYS of the data types BOOL, BYTE or CHAR had different sizes depending on whether they were used within a structure or not. As of V15 the size of the ARRAYs has been standardized. If you access absolutely in your program, for example by using an ANY pointer to an ARRAY of the type of BOOL, BYTE or CHAR, you have to check the program after upgrading.

#### Compatibility of PLC programs from versions prior to V14 SP1

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

In V14 SP1 you can generally continue to use all programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected there in V14 SP1, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

In addition, you have the option of editing the project in compatibility mode. You can find additional information on the compatibility under "Compatibility of projects".

##### Total size of the associated values for program messages

The alarm procedure of the S7-1500 CPU allows a maximum of 512 bytes for associated values (SD parameters) of the instruction "Program_Alarm".

You will only see a warning regarding this number in TIA Portal &lt;= V14 during compilation. There is a stricter check as of TIA Portal V14 SP1. If this number is exceeded, an error is output during compilation to rule out error scenarios during runtime. This check from now on no longer refers to the actual size of the SD parameters at the time the instruction "Program_Alarm" is called, but to the maximum possible size of the SD parameters. This means you must decide beforehand with what length you declare the character string tags you are transferring, as these take up a large number of bytes.

This must be taken into account in the migration of projects from version &lt;= V14 to version V14 SP1 Update 1.

##### Program loops in SCL (S7-1200/S7-1500)

In S7-1200/S7-1500 it is not possible to change the index of a program loop from within the loop with SCL.

The following program example would therefore be invalid:

FOR #i := 1 TO 10 DO

#i := #i + 1;

END_FOR;

As of TIA Portal V14.0.1, a more exact syntax check is conducted in this regard during compilation and a compilation error is output.

##### CASE statements in SCL

Labels without associated "GOTO" instruction are no longer permitted in a CASE statement. A syntax error is signaled.

##### ARRAYs of multi-instances

In some cases ARRAYs of multi-instances could not be correctly be addressed in V14 when individual tags within a multi-instance had the retentivity setting "Set in IDB". This behavior has been corrected in V14 SP1.

If you have used such tags in your program, you may have to recompile the affected block after upgrading.

##### Parameter type "Block_DB" for entry of the instance DB

In LAD and FBD, you cannot enter the instance DB of an instruction using an input of the data type "BLOCK_DB". This behavior has been made uniform for all CPU families and all block types.

As of TIA Portal V14 SP1, a syntax error is output.

If you have transferred instance DBs in your program with the help of the "Block_DB" data type, you change your program. Instead use a parameter instance to transfer the instance during runtime.

##### **I/O accesses as input parameters of blocks (S7-1500 as of FW V2.1)**

In the event of an I/O access error, direct I/O accesses which are interconnected as input parameters to blocks no longer result in the block being run through. Instead of this, the system uses the replacement value of the signal in the block.

For CPUs S7-1500 with FW smaller than V2.1 and all CPUs S7-1200, system behavior is unchanged:

The block is not called as a result of the I/O access error. Program execution is continued after the block call. If OB 122 exists or local error handling is enabled, these are executed.

#### Compatibility of PLC programs from versions prior to V14

##### Contents

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

In principle, you can continue to use in V14 all PLC programs that were created with older versions of TIA Portal. However, because improvements were made to the compiler and errors corrected there in V14, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

##### STL: Instructions "SRW", "SLW" and "SSI" (S7-300, S7-400, S7-1500)

The permitted value range of the offset number of these instructions has changed in TIA Portal V14 from TIA Portal V13 SP1.

In version V13 SP1, it is possible to specify a number in the range 0 to 31 as an offset number on a CPU of the S7-1200/1500 series and a number in the range 0 to 15 as an offset number on a CPU of the S7-300/400 series.

As of Version V14, the value ranges for all CPU series (S7-300/400/1200/1500) was set to the uniform value from 0 to 15.

##### Representation of the BCD format

The representation of the BCD format has changed in regard to the sign from TIA Portal V13 SP1 to TIA Portal V14.

The values in BCD format are show without signs in version V13 SP1.

As of version V14, the values in BCD format are show with sign. This can lead to an altered representation of the values in BCD format.

| Integers (decimal system) | Hexadecimal numbers | Representation in V13 SP1 | Representation in V14 |
| --- | --- | --- | --- |
| 0 | 16#0000 | BCD#0 | BCD#0 |
| -26215 | 16#9999 | BCD#9999 | BCD#-999 |
| 1365 | 16#0555 | BCD#555 | BCD#555 |
| 21845 | 16#5555 | BCD#5555 | BCD#555 |
| 4096 | 16#1000 | BCD#1000 | BCD#0 |
| -28672 | 16#9000 | BCD#9000 | BCD#0 |

##### Instructions "SET_BF: Set bit field" and "RESET_BF: Reset bit array" (S7-1200, S7-1500)

The response of the instruction in regard to the structures has changed from TIA Portal V13 SP1 to TIA Portal V14.

In version V13 SP1, the number of bits that set or reset are always indicated at the input. This also applies, for example, if you have specified a structure of data type of the STRUCT or ARRAY PLC data type. If you want, for example, you want set or reset 10 bits and the structure contains only 5 bits, then the following 5 bits within the address sequence is also set or reset.

With structures of the type PLC data type, as of version V14 STRUCT or ARRAY the number of bits contained in the structure represents the maximum number of bits that can be reset: If you specify the value "20", for example, and the structure only contains 10 bits, only these 10 bits are set. If you specify the value "5", for example, and the structure contains 10 bits, then exactly 5 bits are set.

##### Instructions "SCALE: Scale" and "UNSCALE: Unscale" (S7-1500)

The response of the instruction has changed from TIA Portal V13 SP1 to TIA Portal V14 in regard to specifying the limits (LO_LIM&gt; HI_LIM).

In version V13 SP1, you received an error message when the low limit was greater than the high limit.

As of version V14, this value is allowed and the result is inversely proportional to the input value.

On CPUs of the S7-300/400 series, the instruction has always scaled the result inversely proportional to the input value.

##### Unused bits of PLC data types (UDT) with firmware &gt;= V1.8.1

The unused bits of PLC data types in standard memory areas are occupied or overwritten, for example, for a PLC data type that contains 4 bits.

With firmware versions &lt; V1.8.1, you could not use the unused bits of a PLC data type elsewhere.

With firmware version &gt;= V1.8.1, all bits are occupied or overwritten even if only 4 bits are used.

> **Note**
>
> **Address assignments**
>
> Ensure you do not assign the same absolute address twice to different symbolic address assignments.

##### Explicit data type conversion in SCL (S7-1200) with firmware &gt;= V4.2

With firmware versions &lt; V4.2, the string was transferred aligned to the right and filled with leading spaces during explicit data type conversion of SINT/INT/DINT/REAL_TO_STRING/WSTRING in SCL.

Example: REAL_TO_WSTRING(12) = ' 1.200000E+1'

As of TIA Portal V13, the string is displayed with a leading sign during explicit data type conversion of SINT/INT/DINT/REAL_TO_STRING/WSTRING in SCL and transferred aligned to the left.

Example: REAL_TO_WSTRING(12) = '+1.200000E+1'

##### SCL: EN/ENO mechanism with block parameters of data type (W)STRING (S7-1200/1500)

As of TIA Portal V14, it is checked whether block parameters of data type (W)STRING are truncated when parameters are transferred during runtime. This can occur if formal and actual parameters have different declared lengths. If the declared length of the target parameter during runtime is insufficient to accept the (W)STRING, the (W)STRING is truncated and the enable output ENO is set to "FALSE".

If you evaluate the enable output ENO in your program, the semantics of your program may change.

##### Forwarding STRING parameters between optimized blocks and standard blocks (S7-1200/1500)

Prior to TIA Portal V14, no length information about STRINGs was transferred when parameters were transferred between optimized and non-optimized blocks. This meant that access errors not detected by the ENO mechanism could occur during the further processing of the STRING. The enable output ENO remained at TRUE despite an access error.

As of TIA Portal V14, the STRING length information is transferred and access errors are monitored by the ENO mechanism. If you evaluate the enable output ENO in your program, the semantics of your program may change.

##### Length declaration for constants of the "STRING" or "WSTRING" data type

Length declarations are no longer permitted for local and global (W)STRING constants. If your program includes length declarations, for example, "MyStringConst [7]", these are automatically removed during the upgrade. This change has no semantic effect on your program, however.

##### Changing the base data type for HW_ANY from WORD to UINT

The hardware data type "HW_ANY" is used to identify any hardware component, such as a module. In V14, the base data type of "HW_ANY" was changed from WORD to UINT. After the conversion to V14, compiling errors can therefore occur if you have assigned an explicit WORD constant (such as W#16#1) or a tag of data type WORD at a parameter of data type "HW_ANY".

In this case, change the notation of the constant (e.g. to 16#1) or change the data type of the tag to UINT.

##### Length of block comments

As of TIA Portal V14, the block comments must not exceed a length of 32767 Unicode characters.

##### **Syntax check of the instructions "** **SR: Set/reset flip-flop** **" and "** **RS: Reset/set flip-flop** **"**

Inputs, outputs, bit memories as well as static or local data can be used as operands at the "S" input. Use of constants is not permitted. So far, the use of the constants "0" and "1" was not rejected by the syntax check. As of TIA Portal V14 the syntax check was improved so that the use of "0" or "1" is now rejected at the "S" input. You may now receive an error message during the compiling of a program that has been compiled without errors up to this point. Change your program in this case and use a permitted operand.

##### Any pointer: Access to optimized data

For a CPU of the S7-1500 series, the ANY pointer can also only point to memory areas with "Standard" access mode. Access to optimized data is not permitted with an ANY pointer.

A more detailed syntax check of ANY pointers is performed as of TIA Portal V14. Access to optimized data is now rejected. You may now receive an error message during the compiling of a program that has been compiled without errors up to this point.

##### "(L)REAL" data type

With 64-bit Windows versions, the LREAL data type is sometimes evaluated differently than with the previous 32-bit versions of Windows. A difference may occur when rounding and (L) real values of constants in the least significant bit.

The potential difference is in the last digit of the mantissa and in most cases therefore only has a slight effect on the accuracy.

If you evaluate the last digit of the mantissa, the semantics of your STEP 7 program may change after the conversion.

##### "ST" parameter for IEC timers

The "ST" parameter of an IEC timer is used internally and it is prohibited to write it. This why this parameter is no longer visible as of TIA Portal V14. If you have write access in your program to the "ST" parameter, an error message is generated during compiling after the upgrade.

If you exchange data with Inter Project Engineering and you have access to the "ST" parameter with HMI, you must first export the project and then re-import it into the proxy CPU. Only then does the "ST" parameter disappear in the HMI configuration.

##### Associated values for messages (S7-1500)

Projects created with an older version of the TIA Portal can contain embedded associated values with different structures in the different project languages. The associated values may have a different order or may be missing in a different language. When a project of this type is upgraded, the order of the associated values is harmonized. It is based on the reference language set in the original project. In this case, it is recommended to have the translated texts checked and corrected.

##### Implicit data type conversion for block parameters of the "DB_ANY" data type

When accessing a block parameter of the "DB_ANY" data type with the syntax DB_ANY.%DB(B|W|D), no implicit data type conversion was performed previously. The bit pattern of the source value was simply converted into the target data type. If the target data type was smaller than the source data type, an overflow occurred and the written value may have been wrong or inaccurate. The enable output ENO is not set to "FALSE" when accuracy is lost or runtime errors occur.

As of V14, conversion is performed according to the rules of implicit data type conversion when parameters are passed with the syntax DB_ANY.%DB(B|W|D). Note that after the upgrade a different value may be written and the semantics of your program may change. In addition, the enable output ENO is set to "FALSE" when a runtime error occurs.

##### Interface of organization blocks with standard access

The interface of organization blocks with standard access must have a minimum size of 20 bytes. In older versions of TIA Portal, only the interface of OB1 was checked with regard to the minimum size during the compilation run. As of V14, interfaces of all organization blocks are checked. You may now receive an error message during the compiling of a program that has been compiled without errors up to this point.

##### Comparing tags of WORD data type to tags of the S5TIME data type (S7-1500)

As of TIA Portal V14, both variables are converted to the TIME data type when comparing a variable of WORD data type to a variable of S5TIME data type. The WORD tag is interpreted as an S5TIME value. If one of the variables cannot be converted, the comparison is not performed and the result is FALSE. After successful conversion, the comparison is performed based on the selected comparison expression.

#### Compatibility of PLC programs from versions prior to V13 SP1

##### Content

Information that could not be included in the online help and important information about product characteristics.

##### Compatibility

You can continue to use in V13 SP1 all programs that were created with TIA Portal V12 SP1 or V13. However, because improvements were made to the compiler and errors corrected there (compilation of the program code) in V13 SP1, it can occur in rare cases that the program reacts differently after the upgrade or that you have to adjust the program code manually. These cases are described in detail below.

##### Unused bits of PLC data types (UDT) with firmware &gt;= V1.8.1

The unused bits of PLC data types in standard memory areas are occupied or overwritten, for example, for a PLC data type that contains 4 bits.

With firmware versions &lt; V1.8.1, you could not use the unused bits of a PLC data type elsewhere.

With firmware version &gt;= V1.8.1, all bits are occupied or overwritten even if only 4 bits are used.

> **Note**
>
> **Address assignments**
>
> Ensure you do not assign the same absolute address twice to different symbolic address assignments.

##### Explicit data type conversion in SCL (S7-1200) with firmware &gt;= V4.2

With firmware versions &lt; V4.2, the string was transferred aligned to the right and filled with leading spaces during explicit data type conversion of SINT/INT/DINT/REAL_TO_STRING/WSTRING in SCL.

Example: REAL_TO_WSTRING(12) = ' 1.200000E+1'

As of TIA Portal V13, the string is displayed with a leading sign during explicit data type conversion of SINT/INT/DINT/REAL_TO_STRING/WSTRING in SCL and transferred aligned to the left.

Example: REAL_TO_WSTRING(12) = '+1.200000E+1'

##### Reading an invalid peripheral input

In the TIA Portal as of version 12, the error code 16#2942 for the reading of an invalid peripheral input is only output if you have programmed the faulty access in such a way that this becomes effective, for example %MW10 := “InvalidWordAccess":P, and does not lie within an irrelevant sequence. For example, this would be #tmp := “InvalidWordAccess":P, if the tag #tmp is not used in the rest of the program block.

##### Instruction "S_CONV: Convert character string"

The EN/ENO mechanism behaves differently in TIA Portal V13 SP1 than in TIA Portal V13.

In version V13, the ENO enable output returns the signal state "0" in case of error, even if you have deactivated the ENO enable output. If you have switched an additional instruction to the ENO enable output, this is then not executed.

In version V13 SP1, the ENO enable output returns the signal state "1" in case of error, if you have deactivated the ENO enable output. If you have switched an additional instruction to the ENO enable output, this is then executed as expected.

##### Instruction "SET: Set bit array" (S7-300/S7-400)

In the TIA Portal, you can also interconnect an element of a data block at the N parameter of the SET instruction.

##### Instruction "MUX: Multiplex" (SCL)

Up to and including TIA Portal V13, the value of the tag at the input parameter was output unchanged as a function value, even if the K parameter had a negative integer. This behavior has changed in TIA Portal V13 SP1.

In TIA Portal V13 SP1, if you use a tag with a valid data type at the input parameters of the MUX instruction and the K parameter is a negative integer, the value of the tag is changed. You can find the valid data types in the description of the MUX instruction in the information system.

##### Instruction "DEMUX: Demultiplex" (SCL)

Up to and including TIA Portal V13, no value was output at the OUTELSE output parameter if the value of the K parameter was &lt; 0. In contrast, the value of the IN input parameter was output at the OUTELSE output parameter if the value of the K parameter was &gt; available outputs. This behavior has changed in TIA Portal V13 SP1.

In the TIA Portal V13 SP1, if you specify at the K parameter a value that is outside the available outputs (K &lt; 0 or K &gt; available outputs), then the value of the IN input parameter is output at the OUTELSE output parameter.​

##### Instruction "MOVE: Move value" (STL) (S7-1500)

As of the TIA Portal V13 SP1, a stricter syntax rule applies to the "MOVE" instruction in STL:

Up to and including TIA Portal V13. it was possible to specify non-typed constants, such as "0" at the input parameter IN.

If you want to copy, for example, the value "0" in the TIA Portal V13 SP1, you need to specify a typed constant according to the data type of the output parameter (e.g. INT#0, DINT#0, etc.).

##### Instruction "Program_Alarm: Generate program alarm with associated values" (S7-1500)

As of TIA Portal V13 SP1 the data type INT is no longer permitted for use for the associated values or an index tag of a text list. Use the UINT data type instead.

##### Instructions "READ_DBL: Read from data block in the load memory" and "WRIT_DBL: Write to data block in the load memory"

TIA Portal V13 SP1 reports a compilation error if you use "READ_DBL" V1.0 or "WRIT_DBL" V1.0 and access a data block with the attribute "Only store in load memory" using the parameter DSTBLK.

Instead, use version 1.2 of both instructions.

##### "READ_DBL instructions: Read from data block in the load memory" and "WRIT_DBL: Write to data block in the load memory" (SCL)

As of TIA Portal V​13 SP1, the "READ_DBL" and "WRIT_DBL" instruction in SCL are subject to the same strict syntax rules as all other programming languages:

In TIA Portal V13, it was possible to specify "standard" data blocks at the SRCBLK and DSTBLK parameters that contained tags with different data types.

As of TIA Portal V13 SP1, the individual tags contained must have the same data type for both "standard" as well as for "optimized" data blocks; otherwise, compiling errors are reported.

##### Function values (Return)

As of TIA Portal V13 SP1, more stringent syntax rules apply to function call:

It is checked that the function value (Return) is written in any case, even if multiple possible program paths can be run through in the function. Therefore, there is no longer any risk that the function values will accidentally not be written during runtime.

However, you may possibly receive syntax errors in functions during compiling, which it was still possible to compile without errors in V13. In such cases change the program code so that the function valve is written in all possible program paths.

Example:

SCL

IF #MyIn1 = #MyIn2 THEN

#Block_3 := #MyIn1 + 1;

END_IF;

In this example, the function value of "Block_3" is not written if the condition of the IF instruction is not fulfilled. The function value then contains an undefined value.

SCL

#Block_3 := #MyIn1;

IF #MyIn1 = #MyIn2 THEN

#Block_3 := #MyIn1 + 1;

END_IF;

In this example the function valve of "Block_3" is definitely written in the program, since "MyIn1" is set as default before the IF loop is completed.

##### Comparing the hardware data types HW_IO and HW_DEVICE

As of TIA Portal V13 SP1, there is a stricter syntax rule that is valid for the comparison of the data types HW_IO and HW_DEVICE:

Up until and including TIA Portal V13 it was possible to compare the data types HW_IO and HW_DEVICE directly with each other.

If you want to compare these data types in TIA Portal V13 SP1 you have to first create a tag of the data type HW_ANY in the section "Temp" for the block interface and then copy the LADDR (from data type HW_DEVICE) to the tag. It is then possible to compare HW_ANY and HW_IO.

##### Implicit conversion of floating-point numbers to DWORD (GRAPH) (S7-1500)

As of TIA Portal V13 SP1 stricter syntax rules apply for the implicit conversion of floating-point numbers to DWORD:

Up to and including TIA Portal V13, it was possible to convert a non-typed constant (e.g. 1.0) implicitly to the data type DWORD if the value was less than 32 bits.

With TIA Portal V13 SP1, if you want to convert a floating-point number implicitly to the data type DWORD, you can only use typed constants (e.g. REAL#1.0) since a non-typed constant (e.g. 1.0) is interpreted as data type LREAL and can no longer be converted implicitly to DWORD.

##### Assigning a value to a LTIME constant (S7-1500)

As of the TIA Portal V13 SP1, a stricter syntax rule applies to the definition of a value to a LTIME constant:

Up until and including TIA Portal V13 it was possible to assign a TIME value (e.g. T#10s) to a LTIME constant.

If you want to assign a value to a LTIME constant in TIA Portal V13 SP1, you have to use LTIME syntax (e.g. LT#10s).

Please note that the corresponding TIA Portal projects from previous versions already had to have been adjusted before the upgrade to TIA Portal V13 SP1.

##### Indirect indexing of ARRAY components of data type bit string in SCL (S7-1200/S7-1500)

In TIA Portal V13, you can address the components of an ARRAY for a CPU of the S7-1200/1500 series in SCL with a tag of the data type BYTE, WORD, DWORD or LWORD as index in addition to a tag of the integer data type if the IEC check is not set. This is not possible for a CPU of the S7-300/400 series.

The result is an incompatibility with TIA Portal V12 SP1 in which indirect indexing with the data type bit string is also permitted on a CPU of the S7-300/400 series.

##### EN/ENO mechanism for STRING conversion (S7-1200/S7-1500)

| Conversion | Description |
| --- | --- |
| Strg_TO_Chars: Convert character string to Array of CHAR | The ENO enable output returns the signal state "0" even if you have deactivated the ENO enable output:  - For an invalid character at the CHARS parameter - For an invalid ARRAY index at the PCHARS parameter - If the sum of the PCHARS and STRG parameters exceeds the length of the target ARRAY. |
| Chars_TO_Strg: Convert Array of CHAR to character string | The ENO enable output returns the signal state "0" even if you have deactivated the ENO enable output:  - If the sum of the PCHARS and CNT parameters exceeds the length of the source ARRAY. |

##### Overflow of the local data stack (S7-300/S7-400)

As of TIA Portal V13 SP1, the size of the local data stack is checked to ensure it does not exceed what you have defined for the OB priorities in the hardware configuration.

This means that you may get error messages during compilation in projects that could be compiled without errors in V13. If this happens, change the maximum size of the local data stack in the hardware configuration.

## Using online and diagnostics functions

This section contains information on the following topics:

- [Notes on online and diagnostics](#notes-on-online-and-diagnostics)

### Notes on online and diagnostics

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Interruption of long-term trace recording when the long-term trace editor window is closed

Do not close the long-term trace editor window during a long-term trace recording!

If you close the long-term trace editor window during a long-term trace recording, the recording will be interrupted and no data will be saved in the csv file.

To resume the interrupted long-term trace recording, open the respective long-term trace configuration and start recording again.

The missing data appears as a gap in the time diagram.

#### Recommendation: Limited number of long-term traces in V18

Due to the essential connection between TIA Portal and the CPU, we recommend limiting the use of the long-term trace as follows in version V18:

- Simultaneous recording of max. two long-term traces installed on the CPU
- Max. 32 signals of the "LReal" data type per long-term trace
- Minimum recording cycle 1 ms

#### Hardware detection followed by online connection

When the "Online &gt; Hardware detection" command is performed for an unspecified CPU, the online configuration is not loaded from the CPU. If you do not load the configuration resulting from the hardware detection to the CPU, the device and network views will always show a difference between the offline and online configurations. It will appear that there are different configurations in the online and diagnostic views, although the article numbers are identical in the actual CPU and the offline CPU.

## Inter Project Engineering (IPE)

This section contains information on the following topics:

- [Notes on IPE](#notes-on-ipe)

### Notes on IPE

#### Contents

Information that could not be included in the online help and important information about product characteristics.

#### Using system diagnostics in the device proxy

To use the "system diagnostics" function in an IPE device proxy, for example, a system diagnostics view, insert the PLC alarms as content of a device proxy.

#### Connections to the SIMATIC S7-1500 software controller

Connections to the SIMATIC S7-1500 software controller as device proxy are only possible via the interfaces assigned to the software PLC.

#### Support of Alarm_S alarms

The integrated configuration with WinCC and SIMATIC Manager support the Alarm_S alarms, which are available via data blocks and Continuous Function Chart (CFC).

#### Compatibility

With TIA Portal V15.1, you can open the IPE files of the same version and earlier versions from V13 SP1.

IPE files created with TIA Portal version V15.1 cannot be opened with earlier versions.
