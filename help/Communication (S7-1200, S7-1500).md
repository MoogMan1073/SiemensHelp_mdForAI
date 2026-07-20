---
title: "Communication (S7-1200, S7-1500)"
package: ProgTecCom2MenUS
topics: 58
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communication (S7-1200, S7-1500)

This section contains information on the following topics:

- [S7 communication (S7-1200, S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#s7-communication-s7-1200-s7-1500)
- [Open User Communication (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#open-user-communication-s7-1200-s7-1500)
- [OPC UA (S7-1200, S7-1500)](#opc-ua-s7-1200-s7-1500)
- [Web server (S7-1200, S7-1500)](Web%20server%20%28S7-1200%2C%20S7-1500%29.md#web-server-s7-1200-s7-1500)
- [Communications processor (S7-1200, S7-1500)](#communications-processor-s7-1200-s7-1500)
- [TeleService (S7-1200)](TeleService%20%28S7-1200%29.md#teleservice-s7-1200)
- Failsafe HMI Mobile Panels (S7-1200, S7-1500)

## OPC UA (S7-1200, S7-1500)

This section contains information on the following topics:

- [Client instructions (S7-1500)](#client-instructions-s7-1500)
- [Server instructions (S7-1200, S7-1500)](#server-instructions-s7-1200-s7-1500)

### Client instructions (S7-1500)

This section contains information on the following topics:

- [OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)
- [Compact instructions (S7-1500)](#compact-instructions-s7-1500)
- [Preparing data exchange (S7-1500)](#preparing-data-exchange-s7-1500)
- [Data exchange (S7-1500)](#data-exchange-s7-1500)
- [Ending data exchange (S7-1500)](#ending-data-exchange-s7-1500)
- [Diagnostics (S7-1500)](#diagnostics-s7-1500)
- [Methods (S7-1500)](#methods-s7-1500)
- [System data types for OPC UA client instructions (S7-1500)](#system-data-types-for-opc-ua-client-instructions-s7-1500)
- [Error codes (S7-1500)](#error-codes-s7-1500)
- [Example programs for OPC UA clients (S7-1500)](#example-programs-for-opc-ua-clients-s7-1500)

#### OPC UA instructions for client programs (S7-1500)

##### Introduction

Based on program examples, the following sections are showing you how to use the OPC UA instructions for client programs.

The program examples are based on a plant in which an S7-1500 CPU serves as server and another S7-1500 CPU as client:

- The server provides PLC tags for reading and writing as well as a server method.
- The client accesses the values provided and calls the server method.

STEP 7 helps you in supplying the parameters of the instructions when you create a client interface and use the connection parameter assignment for OPC UA. This means you will not have to create many tags manually for supplying the parameters. To find out how to work manually, read the example in [the section on the "OPC_UA_TranslatePathList" instruction](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500).

How to use the convenient parameter assignment for OPC UA is described in the following sections for the OPC UA instructions.

##### Program examples in SCL

The program examples use the Structured Control Language (SCL) programming language.

The complete source code is available for each program example.

##### Standardized instructions according to PLCopen

The OPC UA instructions for clients have mostly been implemented according to the specification "PLCopen OPC-UA-Client for IEC 61131-3".

Standardization makes it easier to port a user program to a controller of a different manufacturer that also provides the OPC UA instructions according to the PLCopen specification.

If you already know the basic structures and processes of OPC UA clients, you can find your way around more easily.

##### Many client instructions are working with lists

Many OPC UA client instructions process not only a value but lists.

This means the instruction "OPC_UA_NamespaceGetIndexList", for example, receives a list with namespaces and returns a list with the indexes for these namespaces.

##### Even easier with compact instructions

As of TIA Portal V17, you can use compact instructions which are similar to the compact instructions for Open User Communication. The compact instructions ensure that the establishment of the connection or sessions required for the execution of the read/write method is executed at the same time. The following instructions are available:

- OPC_UA_ReadList_C: Set up session and read tags
- OPC_UA_WriteList_C: Set up session and write tags
- OPC_UA_MethodCall_C: Set up session and call method

##### Performance capability of a OPC UA server

OPC UA servers themselves provide information on their performance capability.

The figure below shows the address space of an S7 CPU of the type 1516-3 PN/DP.

In the node "MaxNodesPerRead" you specify, for example, how many PLC tags can be read simultaneously with one call of the "OPC_UA_ReadList" instruction.

The high field limit of the array with which you can supply the "NodeHdls" parameter is limited by the properties of the OPC UA client that is used (see technical specifications of the client).

The following limits apply across all client interfaces (i.e. across all lists):

- 1000 nodes for CPU 1510SP (F), CPU 1511 (C/F/T/TF), CPU 1512C, CPU 1512SP (F), CPU 1513 (F)
- 2000 nodes for CPU 1505 (S/SP/SP F/SP F/SP T/SP TF), CPU 1515 (F/T/TF), CPU 1515 SP PC (F/T/TF), CPU 1516 (F/T/TF)
- 5000 nodes for CPU 1507S (F), CPU 1517 (F/T/TF), CPU 1518 (F)

![Performance capability of a OPC UA server](images/104301540875_DV_resource.Stream@PNG-de-DE.png)

The figure shows a section of the address space of an OPC UA server, shown with the "UaExpert" from Unified Automation.

##### Error numbers

The error numbers for the instructions are divided up as follows:

- If the error number starts with "16#B0" or "16#C0", it was assigned by Siemens, see [Siemens error codes](#siemens-error-codes-s7-1500).

  **Example**: The following error numbers are general numbers that can basically occur for any of the client instructions:

  |  |  |  |
  | --- | --- | --- |
  | B080_C400 | ClientNotEnabled | Client disabled.  Enable the client in the TIA Portal. |
  | B080_C500 | ClientNotAvailable | Error during initialization of the client |
  | C080_C300 | Simatic_OutOfResources | Error at memory allocation or too many instances of the instruction |
- If the error number starts with "16#80" it was assigned by the OPC Foundation see [Error codes of the OPC Foundation](#error-codes-of-the-opc-foundation-s7-1500).
- If the error number starts with "16#A0" it was assigned by PLCopen, see [PLCopen error codes](#plcopen-error-codes-s7-1500).

  You can also find a list with error numbers of the PLCopen in section 4 of the specification "PLCopen OPC UA Client for IEC 61131-3". The specification is available from PLCopen.

---

**See also**

[Number of client instructions that can be used simultaneously (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t)
  
[Using OPC UA communication (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#using-opc-ua-communication-s7-1200-s7-1500-s7-1500t)
  
[Error codes (S7-1500)](#error-codes-s7-1500)
  
[Compact instructions (S7-1500)](#compact-instructions-s7-1500)

#### Compact instructions (S7-1500)

This section contains information on the following topics:

- [OPC_UA_ReadList_C: Set up session and read tags (S7-1500)](#opc_ua_readlist_c-set-up-session-and-read-tags-s7-1500)
- [OPC_UA_WriteList_C: Set up session and write tags (S7-1500)](#opc_ua_writelist_c-set-up-session-and-write-tags-s7-1500)
- [OPC_UA_MethodCall_C: Set up session and call method (S7-1500)](#opc_ua_methodcall_c-set-up-session-and-call-method-s7-1500)
- [Status parameter (S7-1500)](#status-parameter-s7-1500)
- [Useful information about the OPC UA compact instructions (S7-1500)](#useful-information-about-the-opc-ua-compact-instructions-s7-1500)

##### OPC_UA_ReadList_C: Set up session and read tags (S7-1500)

###### On which CPUs can you use the "OPC_UA_ReadList_C" instruction?

The "OPC_UA_ReadList_C" instruction is contained in S7-1500 CPUs as of firmware version V2.8.

###### Description

The "OPC_UA_ReadList_C" instruction sets up a session with an OPC UA server and reads specified values from its NodeSet.

###### Difference to the "OPC_UA_ReadList" instruction

The "OPC_UA_ReadList_C" instruction belongs to the so-called compact instructions in the OPC UA client library, which is indicated by "_C" in the instruction name.

Like every compact instruction in the OPC UA client library, it is characterized by the fact that only this one instruction must be parameterized and executed to fulfill its actual task as an OPC UA client. The user does not have to call further instructions as required when using "OPC_UA_ReadList" (for example, to establish a connection and determine the current indexes of the namespaces in an OPC UA server).

###### Functional description

The "OPC_UA_ReadList_C" instruction works asynchronously. Processing extends over multiple calls.

The mode of operation depends on the parameter "REQ":

- Call without rising edge at REQ

  If MaintainSession=TRUE, a session is set up if none already exists. If MaintainSession=FALSE, an existing session is terminated if no job is active.
- Call with rising edge at REQ

  The job is activated: A session is set up, if one does not already exist, and the read process is carried out. If MaintainSession=FALSE, the session is ended after the read operation; if MaintainSession=TRUE, it is maintained.

The parameters "Busy" and "Done" indicate the status of the job.

The "Status" parameter can contain information about the current processing step, a warning or an error:

- As long as "Busy" has the value TRUE, "Status" provides information about the current processing step.
- When the job has been processed ("Done" has the value TRUE) and "Error" has the value FALSE, it still makes sense to check the "Status" parameter. It may contain a warning.

  When the job has been processed and "Error" has the value TRUE, "Status" contains the error that has occurred.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Parameter

The following table shows the parameters of the "OPC_UA_ReadList_C" instruction. Parameters whose names are written in bold are mandatory parameters; they must be assigned to compile the instruction successfully.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | Bool | Control parameter Request  Activates the job on a positive edge: Setting up a session, if one does not already exist, and starting the reading process |
| MaintainSession | Input | Bool | Influences the OPC UA transport session with the remote server:  - TRUE: If a session does not yet exist, the instruction tries to set up a session and maintain it. - FALSE: If a session exists and no job is active, the instruction terminates the session.   Note: If "MaintainSession" has the value FALSE and "REQ" detects a rising edge, a session is set up and a job is activated. If "MaintainSession" still has the value FALSE after the job is finished, the session is terminated. |
| **ServerEndpointUrl** | Input | String[254] | String with the address (URL) of the OPC UA server  IPv4 addresses as well as FQDN (Fully Qualified Domain Names) are permitted, provided you have configured a DNS server in the CPU properties. |
| **SessionConnectInfo** | Input | OPC_UA_SessionConnectInfo | Session description  See: [OPC_UA_SessionConnectInfo](#opc_ua_sessionconnectinfo-s7-1500) |
| NamespaceUrisCount | Input | UInt | Determines the number of namespaces to be considered from the array "NamespaceUris".  If you assign the value 0 to this parameter, the "OPC_UA_ReadList_C" instruction uses the size of the array that was specified using the "NamespaceUris" InOut parameter. |
| NodeIDCount | Input | UInt | Determines the number of elements (nodes) to be considered in the array "NodeIDs". This is the number to be read from the server.  If you assign the value 0 to this parameter, the "OPC_UA_ReadList_C" instruction uses the size of the array that was specified using the "NodeIDs" InOut parameter. |
| Done | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still being processed. - 1: Job completed without error. This state is only displayed for one call. |
| Busy | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started. |
| Error | Output | Bool | Status parameter with the following values:  - 0: No error occurred. - 1: Error occurred during processing. This state is only displayed for one call. |
| Status | Output | DWord | Return value or error information of the "OPC_UA_ReadList_C" instruction, see below |
| **NamespaceUris** | InOut | Variant | Pointer to an array of the type STRING or WSTRING.  Provided list of namespace URIs |
| NamespaceStatusList | InOut | Variant | Pointer to an array of the type DWORD.  Status of the list with the resolved namespaces |
| **NamespaceIndexes** | InOut | Variant | Pointer to an array of the type UINT.  Cache into which the instruction writes the namespace indexes when the session is set up and which it uses again later when reading the tags |
| **NodeIds** | InOut | Variant | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  Provided list of nodes to be read |
| **NodeHdls** | InOut | Variant | Pointer to an array of the type DWORD.  Cache into which the "OPC_UA_ReadList_C" instruction writes the NodeHandles when the session is set up and which it uses again later when reading the tags |
| NodeStatusList | InOut | Variant | Pointer to an array of the type DWORD.  Storage location for the status list in which the statuses of the read nodes are saved |
| TimeStamps | InOut | Variant | Storage location for the time stamps of the nodes |
| **Tag** | InOut | Variant | Structure with the suitable data types of the requested tags   Storage location for node data |

###### Status parameter

See: [Status parameter](#status-parameter-s7-1500)

---

**See also**

[Useful information about the OPC UA compact instructions (S7-1500)](#useful-information-about-the-opc-ua-compact-instructions-s7-1500)

##### OPC_UA_WriteList_C: Set up session and write tags (S7-1500)

###### On which CPUs can you use the "OPC_UA_WriteList_C" instruction?

The "OPC_UA_WriteList_C" instruction is contained in S7-1500 CPUs as of firmware version V2.8.

###### Description

The "OPC_UA_WriteList_C" instruction sets up a session with an OPC UA server and describes the tags of this OPC UA server.

###### Difference to the "OPC_UA_WriteList" instruction

The "OPC_UA_WriteList_C" instruction belongs to the so-called compact instructions in the OPC UA client library, which is indicated by "_C" in the instruction name.

Like every compact instruction in the OPC UA client library, it is characterized by the fact that only this one instruction must be parameterized and executed to fulfill its actual task as an OPC UA client. The user does not have to call further instructions as required when using "OPC_UA_WriteList" (for example, to establish a connection and determine the current indexes of the namespaces in an OPC UA server).

###### Functional description

The "OPC_UA_WriteList_C" instruction works asynchronously. Processing extends over multiple calls.

The mode of operation depends on the parameter "REQ":

- Call without rising edge at REQ

  If MaintainSession=TRUE, a session is set up if none already exists. If MaintainSession=FALSE, an existing session is terminated if no job is active.
- Call with rising edge at REQ

  The job is activated: A session is set up, if one does not already exist, and the write operation is carried out. If MaintainSession=FALSE, the session is ended after the write operation; if MaintainSession=TRUE, it is maintained.

The parameters "Busy" and "Done" indicate the status of the job.

The "Status" parameter can contain information about the current processing step, a warning or an error:

- As long as "Busy" has the value TRUE, "Status" provides information about the current processing step.
- When the job has been processed ("Done" has the value TRUE) and "Error" has the value FALSE, it still makes sense to check the "Status" parameter. It may contain a warning.

  When the job has been processed and "Error" has the value TRUE, "Status" contains the error that has occurred.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Parameter

The following table shows the parameters of the "OPC_UA_WriteList_C" instruction. Parameters whose names are written in bold are mandatory parameters; they must be assigned to compile the instruction successfully.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | Bool | Control parameter Request  Activates the job on a positive edge: Setting up a session, if one does not already exist, and starting the writing process |
| MaintainSession | Input | Bool | Influences the OPC UA transport session with the remote server:  - TRUE: If a session does not yet exist, the instruction tries to set up a session and maintain it. - FALSE: If a session exists and no job is active, the instruction terminates the session.   Note: If "MaintainSession" has the value FALSE and "REQ" detects a rising edge, a session is set up and a job is activated. If "MaintainSession" still has the value FALSE after the job is finished, the session is terminated. |
| **ServerEndpointUrl** | Input | String[254] | String with the address (URL) of the OPC UA server  IPv4 addresses as well as FQDN (Fully Qualified Domain Names) are permitted, provided you have configured a DNS server in the CPU properties. |
| **SessionConnectInfo** | Input | OPC_UA_SessionConnectInfo | Session description  See: [OPC_UA_SessionConnectInfo](#opc_ua_sessionconnectinfo-s7-1500) |
| NamespaceUrisCount | Input | UInt | Determines the number of namespaces to be considered from the array "NamespaceUris".  If you assign the value 0 to this parameter, the "OPC_UA_WriteList_C" instruction uses the size of the array that was specified using the "NamespaceUris" InOut parameter. |
| NodeIDCount | Input | UInt | Determines the number of elements (nodes) to be considered in the array "NodeIDs". This is the number to be written in the server.  If you assign the value 0 to this parameter, the "OPC_UA_WriteList_C" instruction uses the size of the array that was specified using the "NodeIDs" InOut parameter. |
| Done | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still being processed. - 1: Job completed without error. This state is only displayed for one call. |
| Busy | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started. |
| Error | Output | Bool | Status parameter with the following values:  - 0: No error occurred. - 1: Error occurred during processing. This state is only displayed for one call. |
| Status | Output | DWord | Return value or error information of the "OPC_UA_WriteList_C" instruction, see below |
| **NamespaceUris** | InOut | Variant | Pointer to an array of the type STRING or WSTRING.  Provided list of namespace URIs |
| NamespaceStatusList | InOut | Variant | Pointer to an array of the type DWORD.  Status of the list with the resolved namespaces |
| **NamespaceIndexes** | InOut | Variant | Pointer to an array of the type UINT.  Cache into which the instruction writes the namespace indexes when the session is set up and which it uses again later when writing the tags |
| **NodeIds** | InOut | Variant | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500)  Provided list of nodes to be written |
| **NodeHdls** | InOut | Variant | Pointer to an array of the type DWORD.  Cache into which the "OPC_UA_WriteList_C" instruction writes the NodeHandles when the session is set up and which it uses again later when writing the tags |
| NodeStatusList | InOut | Variant | Pointer to an array of the type DWORD.  Storage location for the status list in which the statuses of the read nodes are saved |
| **Tag** | InOut | Variant | Structure with the suitable data types of the requested tags   Storage location for node data |

###### Status parameter

See: [Status parameter](#status-parameter-s7-1500)

---

**See also**

[Useful information about the OPC UA compact instructions (S7-1500)](#useful-information-about-the-opc-ua-compact-instructions-s7-1500)

##### OPC_UA_MethodCall_C: Set up session and call method (S7-1500)

###### On which CPUs can you use the "OPC_UA_MethodCall_C" instruction?

The "OPC_UA_MethodCall_C" instruction is contained in S7-1500 CPUs as of firmware version V2.8.

###### Description

The "OPC_UA_MethodCall_C" instruction sets up a session with an OPC UA server and calls a method on this server.

###### Difference to the "OPC_UA_MethodCall" instruction

The "OPC_UA_MethodCall_C" instruction belongs to the so-called compact instructions in the OPC UA client library, which is indicated by "_C" in the instruction name.

Like every compact instruction in the OPC UA client library, it is characterized by the fact that only this one instruction must be parameterized and executed to fulfill its actual task as an OPC UA client. The user does not have to call further instructions as required when using "OPC_UA_MethodCall" (for example, to establish a connection and determine the current indexes of the namespaces in an OPC UA server).

###### Functional description

The "OPC_UA_MethodCall_C" instruction works asynchronously. Processing extends over multiple calls.

The mode of operation depends on the parameter "REQ":

- Call without rising edge at REQ

  If MaintainSession=TRUE, a session is set up if none already exists. If MaintainSession=FALSE, an existing session is terminated if no job is active.
- Call with rising edge at REQ

  The job is activated: A session is set up, if one does not already exist, and the call of a method is carried out. If MaintainSession=FALSE, the session is ended after the method call; if MaintainSession=TRUE, it is maintained.

The parameters "Busy" and "Done" indicate the status of the job.

The "Status" parameter can contain information about the current processing step, a warning or an error:

- As long as "Busy" has the value TRUE, "Status" provides information about the current processing step.
- When the job has been processed ("Done" has the value TRUE) and "Error" has the value FALSE, it still makes sense to check the "Status" parameter. It may contain a warning.

  When the job has been processed and "Error" has the value TRUE, "Status" contains the error that has occurred.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Parameter

The following table shows the parameters of the "OPC_UA_MethodCall_C" instruction. Parameters whose names are written in bold are mandatory parameters; they must be assigned to compile the instruction successfully.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | Bool | Control parameter Request  Activates the job on a positive edge: Setting up a session, if one does not already exist, and starting the method call |
| MaintainSession | Input | Bool | Influences the OPC UA transport session with the remote server:  - TRUE: If a session does not yet exist, the instruction tries to set up a session and maintain it. - FALSE: If a session exists and no job is active, the instruction terminates the session.   Note: If "MaintainSession" has the value FALSE and "REQ" detects a rising edge, a session is set up and a job is activated. If "MaintainSession" still has the value FALSE after the job is finished, the session is terminated. |
| **ServerEndpointUrl** | Input | String[254] | String with the address (URL) of the OPC UA server  IPv4 addresses as well as FQDN (Fully Qualified Domain Names) are permitted, provided you have configured a DNS server in the CPU properties. |
| **SessionConnectInfo** | Input | OPC_UA_SessionConnectInfo | Session description  See: [OPC_UA_SessionConnectInfo](#opc_ua_sessionconnectinfo-s7-1500) |
| NamespaceUrisCount | Input | UInt | Determines the number of namespaces to be considered from the array "NamespaceUris".  If you assign the value 0 to this parameter, the "OPC_UA_MethodCall_C" instruction uses the size of the array that was specified using the "NamespaceUris" InOut parameter. |
| MethodHdlCount | Input | UInt | Determines the number of elements (method handles) to be considered in the array "MethodHdls".  If you assign the value 0 to this parameter, the "OPC_UA_MethodCall_C" instruction uses the size of the array that was specified using the "MethodHdls" InOut parameter. |
| MethodHdl | Input | DWord | Handle for the method to be called |
| Done | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still being processed. - 1: Job completed without error. This state is only displayed for one call. |
| Busy | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started. |
| Error | Output | Bool | Status parameter with the following values:  - 0: No error occurred. - 1: Error occurred during processing. This state is only displayed for one call. |
| Status | Output | DWord | Return value or error information of the "OPC_UA_MethodCall_C" instruction, see below |
| **NamespaceUris** | InOut | Variant | Pointer to an array of the type STRING or WSTRING.  Provided list of namespace URIs |
| NamespaceStatusList | InOut | Variant | Pointer to an array of the type DWORD.  Status of the list with the resolved namespaces |
| **NamespaceIndexes** | InOut | Variant | Pointer to an array of the type UINT.  Cache into which the instruction writes the namespace indexes when the session is set up and which it uses again later when the method is called |
| **ObjectNodeIDs** | InOut | Variant | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the node IDs (NodeIDs) of the objects (folders) in which the methods are located. |
| **MethodNodeIDs** | InOut | Variant | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the node IDs (NodeIDs) of the methods for which handles are requested from the server. |
| **MethodHdls** | InOut | Variant | Pointer to an array of the type DWORD.  Cache into which the "OPC_UA_MethodCall_C" instruction writes the MethodHandles returned by the OPC UA server when the session is set up and which it uses again later when the method is called |
| StatusList | InOut | Variant | Pointer to an array of the type DWORD.   Storage location for the status list in which the status of the individual methods is saved. |
| MethodResult | InOut | Variant | Pointer to a tag of the type DWORD.  Error code (result) of the called server method.   This error code is provided by the user program of the OPC UA server or by the system (e.g. if input parameters are incorrect). |
| InputArguments | InOut | Variant | Pointer to a tag with the PLC data type (UDT) or STRUCT, the name, number, order and data type of which correspond to the expected input parameters. |
| OutputArguments | InOut | Variant | Pointer to a tag with the PLC data type (UDT) or STRUCT, the name, number, order and data type of which correspond to the expected output parameters. |

###### Status parameter

See: [Status parameter](#status-parameter-s7-1500)

---

**See also**

[Useful information about the OPC UA compact instructions (S7-1500)](#useful-information-about-the-opc-ua-compact-instructions-s7-1500)

##### Status parameter (S7-1500)

###### Status parameter

The values of the Status parameter are based on OPC 30001 - UA Companion Specification for IEC61131-3 Client FBs.

They are classified as follows:

- 16#38xx_xxxx: Information
- 16#78xx_xxxx: Warnings
- 16#B8xx_xxxx: Error

| Error code  (16#...) | Description |
| --- | --- |
| 3800_0000 | Job completed successfully |
| 3800_0100 | Connection to the OPC UA server successfully established |
| 3800_0300 | Connection to the OPC UA server successfully terminated |
| 3870_0000 | No job active, no connection established |
| 3870_0100 | Initial call for establishing a connection |
| 3870_0200 | A connection is currently being established |
| 3870_0300 | A connection is currently being terminated |
| 3870_0400 | A connection has been established and is being monitored. No ReadList job is active. |
| 3870_0500 | The requested job is being processed. |
| 3870_0600 | The session could not be set up. The instruction waits 30 seconds before trying to set up the session again. |
| 7800_0000 | The function was completed successfully. The NodeStatusList contains additional information. |
| 7800_0100 | Connection to the OPC UA server successfully set up. The NodeStatusList parameter (for OPC_UA_ReadList_C and OPC_UA_WriteList_C) or the parameter StatusList (for OPC_UA_MethodCall_C) contains additional information. |
| 7870_0200 | A connection is being set up The NamespaceStatusList parameter contains supplementary information. |
| B880_0100 | Error when executing an internal system function. The static tag s_OPC_UA_Connect_Instance.Status contains the specific error code. |
| B880_0200 | Error when executing an internal system function. The static tag s_OPC_UA_ NamespaceGetIndexList_Instance.Status contains the specific error code. |
| B880_0300 | Error when executing an internal system function.  - OPC_UA_ReadList_C: The static tag s_OPC_UA_NodeGetHandleList_Instance.Status contains the specific error code. - OPC_UA_WriteList_C: The static tag s_OPC_UA_NodeGetHandleList_Instance.Status contains the specific error code. - OPC_UA_MethodCall_C: The static tag s_OPC_UA_MethodGetHandleList_Instance.Status contains the specific error code. |
| B880_0400 | Error when executing an internal system function.  - OPC_UA_ReadList_C: The static tag s_OPC_UA_ReadList_Instance.Status contains the specific error code. - OPC_UA_WriteList_C: The static tag s_OPC_UA_WriteList_Instance.Status contains the specific error code. - OPC_UA_MethodCall_C: The static tag s_OPC_UA_MethodCall_Instance.Status contains the specific error code. |
| B880_0500 | Error when executing an internal system function.  - OPC_UA_ReadList_C: The static tag s_OPC_UA_NodeReleaseHandleList_Instance.Status contains the specific error code. - OPC_UA_WriteList_C: The static tag s_OPC_UA_NodeReleaseHandleList_Instance.Status contains the specific error code. - OPC_UA_MethodCall_C: The static tag s_OPC_UA_MethodReleaseHandleList_Instance.Status contains the specific error code. |
| B880_0600 | Error when executing an internal system function. The static tag s_OPC_UA_Disconnect_Instance.Status contains the specific error code. |
| B880_0700 | Error when executing an internal system function. The static tag s_OPC_UA_ConnectionGetStatus_Instance.Status contains the specific error code. |

##### Useful information about the OPC UA compact instructions (S7-1500)

###### Setting up and terminating sessions

If you want to set up a session with the OPC UA server with the properties that are specified in the "SessionConnectInfo" input parameter, set the "MaintainSession" parameter to TRUE. The compact instruction then calls the required instructions to establish and maintain the session. As long as the "MaintainSession" parameter has the value TRUE, the compact instruction will continue to maintain the session and you can initiate additional jobs. If you want to terminate the session, set the "MaintainSession" parameter to FALSE.

If several jobs are to be executed, you save CPU resources by maintaining the session using the "MaintainSession" parameter: Instead of setting up and terminating a session with the server for each job, the session remains set up and the jobs are executed faster.

If an error occurs when setting up or terminating a session without the execution of a job being requested, the "Error" output parameter is not set. This means you should monitor the "Status" output parameter when setting "MaintainSession" to identify problems when setting up or terminating a session.

###### Request a read or write operation or a method call

A job is activated with a rising edge at the "REQ" input parameter, regardless of the value of the "MaintainSession" parameter.

If a session already exists ("MaintainSession" = TRUE), the read or write process or the method call is started immediately. If a session does not already exist, the compact instruction tries to set up one and then starts the read or write process or the method call. In case of an error, the session is closed.

###### Monitor the status list with the error codes of the tags read

After several internally called instructions have been successfully completed, the compact instruction checks the status list of the internal instruction.

- If the status list is empty, the output parameter "Status" contains an information (16#38xx_xxxx).
- If the status list is not empty, the compact instruction checks each list element. If an error code occurs, the check is stopped and the output parameter "Status" contains a warning (16#78xx_xxxx). In this case you should check the static tag s_StatusList_CurrentElement of the instance DB of the compact instruction. Its value is the number of the element in the status list array that contains the first error code.

###### Interactions between the OPC UA compact instructions and the other OPC UA instructions

The connection handles and node handles that were obtained from the OPC UA compact instructions can also be used by the other OPC UA instructions. You can, for example, call the "OPC UA-ReadList_C" instruction to get a connection handle and node handles. You can use this connection handle, which is available to you as a static tag, and the node handles for calling the "OPC_UA_WriteList" instruction; there is no need to call additional OPC UA instructions to set up the connection and to obtain the node handles.

This concept is based on the fact that the handles do not come from the instruction but are made available by the firmware of the CPU. Therefore, the OPC UA instructions can use these handles together as long as they are available in the CPU.

You may not call the OPC UA instructions to terminate the data exchange using a connection handle that comes from an OPC UA compact instruction. In the case of the compact instructions, this leads to errors in processing the job and in closing the session. If you set up a session with a compact instruction, this session must be closed by the same instance of the compact instruction.

You must not set up a session with the "OPC_UA_Connect" instruction and use this session with an OPC UA compact instruction.

###### Reconnect if the connection was interrupted

The compact instructions try to maintain the connection to the server as long as the "MaintainSession" parameter has the value TRUE. The instructions check the connection as follows: You monitor whether the "Error" parameter is set to TRUE when instructions are called internally. If this is not the case, the compact instructions assume that the connection still exists.

If the error code of the internally called instruction indicates a connection or server problem that requires the connection to be closed and reopened, the compact instruction does not display an error. If a node handle is available, it first calls "OPC_UA_NodeReleaseHandleList". Then, it calls "OPC_UA_Disconnect". After the connection has been terminated, the compact instruction tries to re-establish the connection the next time it is called with "MaintainSesion" = TRUE.

If an error occurs without the execution of a job being requested via the "REQ" input, the "Error" output parameter of the compact instruction is not set. This means you must monitor the "Status" output parameter to identify difficulties in setting up a session.

If an error occurs while the compact application is trying to set up a session ("Status" has the value 16#3870_0100 or 16#3870_0200) and the "MaintainSession" parameter has the value TRUE, the compact instruction will try to establish the session again after a delay of 30 seconds. The "Status" parameter has the value 16#3870_0600 as long as the delay is active. You can cancel the delay by setting the "MaintainSession" parameter to FALSE. In this case, the instruction immediately starts a new attempt to set up the session.

#### Preparing data exchange (S7-1500)

This section contains information on the following topics:

- [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection)
- [Programming recommendation: Monitor connections. (S7-1500)](#programming-recommendation-monitor-connections-s7-1500)
- [OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)
- [OPC_UA_NodeGetHandleList: Get handles for read and write access (S7-1500)](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500)
- [OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500)

##### OPC_UA_Connect: Create connection

###### Validity

The following description of the "OPC_UA_Connect" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

The "OPC_UA_Connect" instruction establishes a connection to an OPC UA server.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112207566475_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction is used to prepare the data exchange between an OPC UA server and an OPC UA client, see explanation for ① in the figure below:

The instruction returns a connection handle (a numerical reference) which uses the following instructions to refer to the connection.

![Description](images/103730274315_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions (call the instructions repeatedly depending on the application) |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_Connect"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ServerEndpointUrl | InOut | VARIANT | Pointer to a tag of the type STRING or WSTRING with the address (URL) of the OPC UA server. IPv4 addresses as well as FQDN (Fully Qualified Domain Names) are permitted, provided you have configured a DNS server in the CPU properties. |
| SessionConnectInfo | InOut | VARIANT | Pointer to the connection description in a tag with the system data type "[OPC_UA_SessionConnectInfo](#opc_ua_sessionconnectinfo-s7-1500)". |
| Timeout | Input | TIME | Maximum time for the establishment of the connection in milliseconds.   The "Timeout" parameter defines the service timeout for lower-level OPC UA service requests that the client is sending to the server.   Timeout values smaller than 100 ms or negative values are set to 100 ms, as smaller values are not useful. |
| Done | Output | BOOL | Execution status parameter:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below. |
| ConnectionHdl | Output | DWORD | Unique identifier for a connection established.   This handle is required by other OPC UA instructions as an input parameter. |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. - General: Reduce the number of registered OPC UA elements. Use an OPC UA Server diagnostics tool (such as UaExpert from Unified Automation) to ensure that there are no inactive sessions and subscriptions. As countermeasure you can select corresponding timeouts (Subscription Timeout <= Session Timeout) in the client. |
| 8005_0000 | OpcUa_BadCommunicationError | Connection timeout.  Possible causes:   - The server address (ServerEndpointURL) is incorrect or incomplete, or the server returns a value that differs from the addressed address. A difference between the addressed and returned address occurs in the following cases:   - The server is located in another subnet and is reached via NAT (Network Address Translation)   - The server responds with its name rather than its IP addressFor an associated application example, see: [How do you configure the OPC UA client of a SIMATIC S7-1500 to establish a connection via FQDN or to bypass the FQDN?](https://support.industry.siemens.com/cs/ww/en/view/109771693) - The server does not accept the buffer size sent by the client during connection establishment.   Remedies:  - Check and correct the ServerEndpointURL. If this error is caused by a difference between the addressed and returned address, change the server configuration so that the server responds with the same ServerEndpointURL with which it is addressed by the client. If the behavior of the server cannot be changed, enter the ServerEndpointURL in the "ConnectInfo.ServerUri" tag ("SessionConnectInfo" parameter). The address returned by the server is then overwritten by this value. This value must also be in the server certificate. - Check the permitted buffer size. The client of the S7-1500 CPU provides 8192 bytes. The server must accept this value. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow. - The network load is too high. - The OPC UA server is not available. - The server might not accept the buffer size sent by the client during connection establishment.   Remedies:  - Check the URL of the OPC UA server. - Increase the timeout value of the instruction OPC_UA_Connect. - Check the permitted buffer size. The client of the S7-1500 CPU provides 8192 bytes. The server must support this value. |
| 803D_0000 | OpcUa_BadNotSupported | Possible causes**:**  - The server address (ServerEndpointURL) is incorrect or incomplete. - Server does not support the requested operation. |
| 8054_0000 | OpcUa_BadSecurityModeInsufficient | The server sets higher security requirements (security policy).  Possible remedy:  - Use a higher security setting for the connection to the server. |
| 8055_0000 | OpcUa_BadSecurityPolicyRejected | Server does not support requested Security Policy or Transport Profile |
| 8056_0000 | BadTooManySessions | The server has reached the maximum number of sessions. |
| 8081_0000 | BadTcpNotEnoughResources | The client's connection resources required to establish the connection are used up.  Possible remedy:  - If the connection is established and terminated in rapid succession, the frequency must be reduced. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "ServerEndpointUrl". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "SessionConnectInfo". |
| B080_2200 | Simatic_BadValue_VariantInput2 | Incorrect value of the tags "SessionConnectInfo". |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled.  Solution: Activate the OPC UA client in the properties of the CPU (OPC UA > Client area). |
| B080_C500 | Simatic_NothingToDo | Error during initialization of the client. |
| B080_C600 | Simatic_ClientNotAvailable | Error during initialization of the client. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see:  [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500) |  |  |

###### Description of connection establishment and connection termination

If an error message indicates that there is a shortage of resources, you can determine the currently allocated connection resources for the "OPC UA client/server communication" service using the connection diagnostics. In it, you can see how many resources are still available.

The OPC UA client/server communication is based on the TCP protocol. Note that connection resources are still tied up for a specific wait time during connection termination due to the TCP protocol even though the connection has already been terminated. Before the productive connection is established, a connection is set up for OPC UA to determine the endpoint for the connection with the desired connection partner (Discovery).

**Recommendation**: If the number of required connections is close to the limit of available connection resources, you should set up OPC UA connections over a longer period of time. If the CPU OPC UA connections are set up in short-term intervals, you might experience a resource shortage.

The following figures show how connections are established and terminated with the corresponding wait times and the resultant resource allocation.

See also: [Details about OPC UA client/server connections](Configuring%20devices%20and%20networks.md#details-about-opc-ua-clientserver-connections-s7-1500)

###### This is how you use this instruction

The following sections show you how to use the instruction "OPC_UA_Connect" in a program that exchanges data with an OPC UA server.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have configured a connection to an OPC UA server in the properties of this client interface.

###### Configuring secure connections

You can use the instruction "OPC_UA_Connect" to establish an unsecure connection to an OPC UA server. But you should always use a secure connection.

###### How to use a client interface

1. In the "Project tree" area, select the CPU that acts as the client.
2. Add a new function block to the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Used language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_Connect" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_Connect_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_Connect_Instance" instruction.

   ![How to use a client interface](images/113866502027_DV_resource.Stream@PNG-de-DE.png)

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA connection" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline".

   ![How to use a client interface](images/113869633675_DV_resource.Stream@PNG-en-US.png)

   STEP 7 automatically supplies the parameters of the instruction with the values you have configured for the client interface.
7. Click on "Block parameters" and assign tags manually to the remaining parameters (REQ, Busy, Done, Error, Status).

   STEP 7 adds the selected tags to the function call.

###### Calling the instruction

The following source code shows you how to use the instruction "OPC_UA_Connect" to establish a connection to an OPC UA server.

You can find the complete program in the section "[Example programs for OPC UA clients](#example-programs-for-opc-ua-clients-s7-1500)".

The example program is divided into multiple program sections (cases) by a CASE instruction. The #State tag controls which program section is being executed.

In the first program section, a connection is established:

SCL

1: // case 1, connect to server

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

#OPC_UA_Connect_Instance(REQ := #Req,

          ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

          SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

          ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl,

          Done => #Done,

          Busy => #Busy,

          Error => #Error,

          Status => #Status);

IF #Done = TRUE THEN

    #State := #State + 1;

END_IF;

IF #Error = TRUE THEN

// Did we get a connection handle?

    IF "Productionline_Configuration".Connection.ConnectionHdl <> 0 THEN

    // We have to release all resources in the server and disconnect

    #State := 100;

    //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    ELSE

    #State := 99;

    END_IF;

#Mem_Status := #Status;

// set parameter REQ of OPC_UA_Connect to FALSE

#OPC_UA_Connect_Instance(ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

          SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

          REQ := FALSE,

          ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout);

END_IF;

The example program calls the "OPC_UA_Connect" instruction for the following reasons:

- To establish the connection to an OPC UA server.
- If an error occurs, the REQ parameter is set to the value "FALSE".

**Asynchronous execution**

The instruction "OPC_UA_Connect" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction

This program part establishes a connection to the OPC UA server that you have entered during the configuration of the client interface.

The tag "#State" contains the value "1" at the start of the program.

If the "OPC_UA_Connect" instruction is not yet executed, #Busy is FALSE, so that #Req is set to TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

If the output parameter "Done" is TRUE, a connection could be established. The success status increases the value of the #State tag by one. This means the next program section (2:) is executed in the next cycle, see [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500). The success status also indicates the numerical reference for the established connection at the "ConnectionHdl" output parameter.

If an error has occurred, the "Error" output parameter has the value TRUE.

- If a connection handle is returned in the event of an error, resources must be released in the server. The #State tag is assigned the value 100 for this.
- If no connection handle is returned in the event of an error, the #State tag is assigned the value 99.

The program sections 99 and 100 are reserved for error handling.

---

**See also**

[OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500)
  
[Siemens error codes (S7-1500)](#siemens-error-codes-s7-1500)
  
[OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)
  
[Program example for reading PLC tags (S7-1500)](#program-example-for-reading-plc-tags-s7-1500)

##### Programming recommendation: Monitor connections. (S7-1500)

###### Recommendations for monitoring the connections

We recommend monitoring the connections created with the instruction "OPC_UA_Connect" cyclically in order to be able to react specifically to connection aborts and to be able to establish a new connection immediately in the event of an error.

The following description of the S7 user block for the OPC UA client of an S7-1500 CPU contains a description of how to integrate connection monitoring.

[S7 user block for the OPC UA client of a SIMATIC S7-1500](https://support.industry.siemens.com/cs/ww/en/view/109762770)

**Changes as of CPU firmware version V2.8**

With OPC UA, connection handles reference a connection. As of firmware version 2.8, you must explicitly release the relevant connection handle in the event of a faulty or interrupted connection by calling the "OPC_UA_Disconnect" instruction. It cannot be used until the connection handle is released; it is invalid.

After the release of the connection handle, the CPU can reuse it for a new connection (OPC_UA_Connect).

---

**See also**

[OPC_UA_ConnectionGetStatus: Read connection status (S7-1500)](#opc_ua_connectiongetstatus-read-connection-status-s7-1500)

##### OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)

###### Validity

The following description of the "OPC_UA_NamespaceGetIndexList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the "OPC_UA_NamespaceGetIndexList" instruction to request the current indexes of the namespaces in an OPC UA server.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112207570187_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_NamespaceGetIndexList" is used to prepare the data exchange with an OPC UA server, see ① in the figure below.

To read or write a PLC tag or to call a method, you must know the index of the namespace in which the PLC tag is located. The index is a part of the address (NodeId) of this PLC tag in the address space of the OPC UA server.

The instruction returns a list with the indices for the namespaces of the OPC UA server.

This list is necessary to request the NodeIDs that can be used to send the read and write jobs with the "OPC_UA_NodeGetHandleList" instruction.

![Description](images/100765702155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_NamespaceGetIndexList"

The parameters of the instruction "OPC_UA_NamespaceGetIndexList"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.  You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NamespaceUrisCount | Input | UINT | Number of namespaces in the NamespaceUris parameter |
| NamespaceUris | InOut | VARIANT | Pointer to an array of the type STRING or WSTRING.  The array contains the URIs of the individual namespaces whose indexes are to be requested. |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| StatusList | InOut | VARIANT | Pointer to an array of the type DWORD (optional).  The array contains the error codes for the individual namespaces.  For each namespace, the system specifies whether or not a corresponding index could be found. |
| NamespaceIndexes | InOut | VARIANT | Pointer to an array of the type UINT.  The array contains the indexes of the individual namespaces that have been requested from the OPC UA server. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | Server does not respond with the expected number of namespace array elements |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | NamespaceUrisCount is 0 |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_NamespaceGetIndexList" instructions that can be called at the same time per connection has been exceeded (> 1), see:    [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 809E_0000 | OpcUa_BadDataUnavailable | The indexes of the namespaces are not currently available. |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| A000_0105 | PLCopenUA_Bad_ConnectionInvalidHdl | The connection handle (ConnectionHdl) is invalid / unknown.   See [OPC_UA_ConnectionGetStatus: Read connection status](#opc_ua_connectiongetstatus-read-connection-status-s7-1500) |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "NamenspaceUris". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "StatusList". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "NamenspaceIndexes". |
| B080_1100 | Simatic_ArrayElements_TooMany | NamespaceUrisCount > MAX_ELEMENTS_NAMESPACES |
| B080_3100 | BadNumElements_VariantInput1 | NamespaceUrisCount > Number of array elements of the "NamespaceUris" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | NamespaceUrisCount > Number of array elements of the "StatusList" parameter. |
| B080_3300 | BadNumElements_VariantInput3 | NamespaceUrisCount > Number of array elements of the "NamespaceIndexes" parameter. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements (namespaces). |
| C080_C300 | Simatic_InsufficientResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "StatusList"

The parameter contains an error code for each individual namespace.

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | The namespace is found.  The index of the namespace is entered in the array to which the "NamespaceIndexes" parameter is pointing. |
| 806F_0000 | OpcUA_BadNoMatch | The namespace is not found. |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_NamespaceGetIndexList" in a program that exchanges data with an OPC UA server.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have configured a connection to an OPC UA server in the properties of this client interface, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirement must be met for the instruction "OPC_UA_NamespaceGetIndexList":

- A handle for connection to an OPC UA server is available.

  You get the connection handle by calling the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).

###### Function of the instruction

For the exchange of data, you require the indexes of the namespaces that contain the tags that you want to read or write using your program.

You also need the current indexes of the namespaces that contain the methods for calling methods.

With an OPC UA server, the assignment, according to the OPC UA specification, between the namespace and associated index is not fixed and can change, for example, if new namespaces are added or namespaces are omitted.

You therefore need to request the current indexes from the OPC UA server before you get the node handle using the instruction OPC_UA_NodeGetHandleList. You do this with the instruction "OPC_UA_NamespaceGetIndexList".

**What information does the instruction return?**

The instruction returns the following information:

- A list of the indexes for the individual namespaces ("NamespaceIndexes" parameter). The order of the indexes corresponds to the order of the namespaces in the "NamespaceUris" parameter.
- A list of error messages ("StatusList" parameter).

  Each error message in this list relates to the corresponding namespace in the "NamespaceUris" parameter.

  For each individual namespace, you can to check whether the index for that namespace can be successfully returned.

###### Determining namespaces and their indexes with UaExpert

To use the instruction, the namespace URI (Uniform Resource Indentifier) must be known. You can determine namespace URIs and namespace indexes with UaExpert, as the following example shows:

![Determining namespaces and their indexes with UaExpert](images/114401048459_DV_resource.Stream@PNG-de-DE.png)

###### How to use a client interface

1. In the "Project tree" area, select the CPU that acts as the client.
2. Select the function block that is to contain the client instruction in the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Selected language: SCL
3. Use drag-and-drop to move the instruction "OPC_UA_NamespaceGetIndexList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_NamespaceGetIndexList_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_NamespaceGetIndexList_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is named "Productionline", see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
7. Click on "Block parameters" and assign tags manually to the remaining parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction

The following source code shows you how to use the instruction "OPC_UA_NamespaceGetIndexList" to request the indexes for the namespaces that currently used by the OPC UA server.

You can find the complete program in the section "[Program example for reading PLC tags](#program-example-for-reading-plc-tags-s7-1500)".

The example program is divided into multiple sections (cases) by a CASE instruction.

In the second program section, the indexes of the namespaces are requested:

SCL

2: // case 2, get index for namespace

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

#OPC_UA_NamespaceGetIndexList_Instance(NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

          ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

          NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

          StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

          NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

          REQ := #Req,

          Done => #Done,

          Busy => #Busy,

          Error => #Error,

          Status => #Status);

IF #Done = TRUE THEN

    IF "Productionline_Configuration".Namespaces.NamespaceStatusList[0] = 0 THEN

        #State := #State + 1;

    ELSE

        #State := 100;

        #Mem_Status := #Status;

        #Output_Error_Message := WString#'Error at NamespaceGetIndexList';

    END_IF;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #Mem_Status := #Status;

    #OPC_UA_NamespaceGetIndexList_Instance(NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

          StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

          NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

          REQ := FALSE);

END_IF;

The example program calls the "OPC_UA_NamespaceGetIndexList" instruction for the following reasons:

- To request the index for a namespace.
- If an error occurs, the REQ parameter is set to the value FALSE.

**Asynchronous execution**

The instruction "OPC_UA_NamespaceGetIndexList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction

The figure above shows case 2. This part of the program requests the indexes for the namespaces.

If the #State tag is 2, then case 2 is executed.

If the "OPC_UA_NamespaceGetIndexList" instruction is not yet executed, #Busy is FALSE an the "#Req" tag is set to TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

If the output parameter "Error" is TRUE, an error occurred during execution of the instruction. This sets the #State tag to the value 100. This case is reserved for troubleshooting.

If the output parameter "Done" is TRUE, the instruction was executed successfully. The success status increases the value of the "#State" tag by one. This means the next program section - case 3 (get handles for read access and write access) - is executed in the next cycle.

Case 3 is described in [OPC_UA_NodeGetHandleList: Get handles for read and write access](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500).

> **Note**
>
> **Execution of the instruction**
>
> It is possible that the instruction is successfully executed ("Error" parameter not set, "Done" parameter set) but no index can be returned for a specific namespace.
>
> Therefore, there is a check in the example to determine whether an index has been found for the namespace to be queried. If an index is found, the first element of the array to which the "StatusList" parameter is pointing contains the value 0.

---

**See also**

[OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500)

##### OPC_UA_NodeGetHandleList: Get handles for read and write access (S7-1500)

###### Validity

The following description of the "OPC_UA_NodeGetHandleList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the "OPC_UA_NodeGetHandleList" instruction to register PLC tags on an OPC UA server.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112215061899_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_NodeGetHandleList" is used to prepare the data exchange with an OPC UA server, see ① in the figure below:

You use this instruction to register PLC tags on the server that you want to read or write.

This step optimizes later access with the instructions "OPC_UA_ReadList" and "OPC_UA_WriteList".

The instruction returns a list with numerical references (handles) for the registered PLC tags.

![Description](images/103724873611_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_NodeGetHandleList"

The parameters of the instruction "OPC_UA_NodeGetHandleList"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeIDCount | Input | UINT | Number of elements in the NodeIDs parameter |
| NodeIDs | InOut | VARIANT | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the NodeIds of the tags for which the OPC UA server is to provide numeric references (handles) (see "Function of the block" above). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in[OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NamespaceIndexCount | Input | UINT | Number of elements in the "NamespaceIndexes" parameter. |
| NamespaceIndexes | InOut | VARIANT | Pointer to an array of the type UINT.  This parameter is not required if there are no elements in the NamespaceIndexCount parameter (NamespaceIndexCount = 0).  The array is used to assign new indexes to the namespace indexes in the NodeIDs parameter.  Example:   If there is a value of 10 in NamespaceIndexes[4], all NodeIDs in the "NodeIDs" parameter that previously had the namespace index 4 are assigned the namespace index 10. |
| NodeStatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error codes for the NodeIds of the individual tags; see "Error numbers for NodeStatusList" below.  It is specified whether a handle could be assigned to each NodeId.  It is possible that the function block was successfully executed (Error parameter not set) but no handle could be found for a specific NodeId (tag).  A NodeId consists of a namespace index, a tag name (identifier) and an identifier type. See [OPC_UA_NodeID](#opc_ua_nodeid-s7-1500). |
| NodeHdls | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the handles of the individual NodeIds that have been requested from the OPC UA server (see "Function of the block" above). |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | The server has sent has response that could not be recognized. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_NodeGetHandleList" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 8033_0000 | OpcUa_BadNodeIdInvalid | The syntax of the node is invalid. |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The ID of the node (NodeId) refers to a node that does not exist in the address space of the server. |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "NodeIDs". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "NamenspaceIndexes". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "NodeStatusList". |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for parameter "NodeHdls". |
| B080_1100 | Simatic_ArrayElements_TooMany | NodeIDCount > MAX_ELEMENTS_NODELIST |
| B080_3100 | BadNumElements_VariantInput1 | NodeIDCount > Number of array elements of the "NodeIDs" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | NamespaceIndexCount > Number of array elements of the "NamespaceIndexes" parameter. |
| B080_3300 | BadNumElements_VariantInput3 | NodeIDCount > Number of array elements of the "NodeStatusList" parameter. |
| B080_3400 | BadNumElements_VariantInput4 | NodeIDCount > Number of array elements of the "NodeHdls" parameter. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "NodeStatusList"

The "NodeStatusList" parameter contains an error code for each individual NodeId (tag).

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | The PLC tag (NodeId) was found.  The Handle of the tags was entered in the Array to which the "NodeHdls" parameter is pointing. |
| 8033_0000 | OpcUa_BadNodeIdInvalid | The syntax of the NodeId is incorrect. |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The NodeId refers to a node (tag) that does not exist on the OPC UA server. |
| A000_0309 | PLCopenUA_Bad_OutOfHandles | The NodeId was not registered because the maximum number of nodes (PLCOPEN_MAXREGISTEREDNODES) was reached. |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_NodeGetHandleList" in a program that exchanges data with an OPC UA server.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have configured a connection to an OPC UA server in the properties of this client interface, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirements must be met for the instruction "OPC_UA_NodeGetHandleList":

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).
- Indexes of the namespaces in which the tags that you want to read or write with the client are located.

  You get the indexes from the instruction [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500).

###### Function of the instruction

To optimize access to tags, OPC UA offers the "RegisterNodes" service for repeated accesses.

Servers can use this service to prepare optimized access to tags. The "OPC_UA_NodeGetHandleList" instruction implicitly calls this service to prepare the server for optimized access ("Registered Read/Write" in OPC UA language).

This is how you obtain numerical references (handles) from the OPC UA server through the call of the "OPC_UA_NodeGetHandleList" instruction. You use these handles with the "OPC_UA_ReadList" or "OPC_UA_WriteList" instructions, which correspond to an optimized access with "Registered Read/Write".

**What information is required?**

The instruction requires the following information to request the numeric references (handles):

- A list of the tags that are to be read or set ("NodeIDs" parameter, see system data type "[OPC_UA_NodeId](#opc_ua_nodeid-s7-1500)").

  This list contains the following information for each tag:

  - Index of the namespace in which the tag is located.
  - Tag identifier (tag name).
  - Type of identifier

**What information does the instruction return?**

The instruction returns the following information:

- A list of the handles for the tags ("NodeHdls").

  The order of the handles corresponds to the order of the tags in the NodeIDs parameter.
- A list of error messages ("NodeStatusList" parameter).

  Each error message in this list relates to the corresponding tag in the NodeIDs parameter.

  For each individual tag, you need to check whether the OPC UA server was able to return a handle.

###### How to use a client interface

1. In the "Project tree" area, select the CPU that acts as the client.
2. Select the function block that is to contain the client instruction in the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_NodeGetHandleList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_NodeGetHandleList_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_NodeGetHandleList_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface "Productionline" is selected, which was created for the example plant.
7. Click "Data access" and select a read list.

   In the example: Read list "ReadListProduct".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
8. Click on "Block parameters" and assign tags manually to the remaining parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

You can find the complete program in the section "[Program example for reading PLC tags](#program-example-for-reading-plc-tags-s7-1500)".

The program example uses the read list "ReadListProduct", which contains the following PLC tags:

- NewProduct
- ProductNumber

The program receives numerical references (handles) from the server for these tags.

The example program is divided into multiple sections (cases) by a CASE instruction.

In the third program section, the handles of the nodes (PLC tags) that are to be read or written are requested:

SCL

3: // case 3, get handles for nodes

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

#OPC_UA_NodeGetHandleList_Instance(REQ := #Req,

          ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

          NodeIDCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

          NodeIDs := "Productionline_Configuration".ReadLists."ReadListProduct".Nodes,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

          NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

          NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

          NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

          NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

          Done => #Done,

          Busy => #Busy,

          Error => #Error,

          Status => #Status);

**Asynchronous execution**

The instruction "OPC_UA_NodeGetHandleList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The program part in the figure above calls the "OPC_UA_NodeGetHandleList" instruction to request handles for PLC tags.

If the instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

IF #Done = TRUE THEN

    IF "Productionline_Data"."ReadListProduct".NodeStatusList[0] = 0 AND "Productionline_Data"."ReadListProduct".NodeStatusList[1] = 0

    THEN

          #State := #State + 1;

    ELSE

          #State := 100;

          #Mem_Status := #Status;

          #Output_Error_Message := WString#'Error at NodeGetHandleList';

    END_IF;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #OPC_UA_NodeGetHandleList_Instance(REQ := FALSE,

          ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

          NodeIDCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

          NodeIDs := "Productionline_Configuration".ReadLists."ReadListProduct".Nodes,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

          NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

          NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

          NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

          NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls);

END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the value of the "Error" output parameter is set to TRUE. This sets the value of the "#State" tag to 100. This case is reserved for troubleshooting. The example program also calls the instruction "OPC_UA_NodeGetHandleList" to set the REQ parameter to FALSE.

If the output parameter "Done" is TRUE, the instruction was executed successfully.

Note: It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but no handle could be returned for a specific PLC tag.

In the example program, therefore, there is a check to determine whether a handle is returned for each PLC tag.

- If a handle returns for the first tag, then the first element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.
- If a handle returns for the second tag, then the second element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

If both conditions are met, the output parameter "NodeHdls" points to a valid list with the handles for the registered PLC tags.

The value of the "#State" tag is increased by one. This means the next program section - case 4 - is executed in the next cycle.

Case 4 is described in [OPC_UA_Readlist](#opc_ua_readlist-reading-tags-s7-1500).

> **Note**
>
> If you register a large number of tags in your application with OPC_UA_NodeGetHandleList, it can be useful always to increase #State by one when #Done = TRUE. You should then check when using the requested values whether the individual values are valid.

###### Tip: Programming general error handling

In order to keep the example program above (calling the instruction "error handling") clear and easy to understand, only the handles for two PLC tags were queried and there was checked whether a handle was returned for each tag. This type of query is quite inflexible.

If you scan the handles for more than two PLC tags in your program or if you want to write your program independent of the number of PLC tags, you should use the following program code to evaluate "NodeStatusList" in a loop:

IF #Done = TRUE THEN

         FOR #i := 0 TO UINT_TO_INT("Productionline_Configuration".ReadLists."ReadListProduct".NodeCount) - 1 DO

             IF NOT ("Productionline_Data"."ReadListProduct".NodeStatusList[#i] = 0) THEN

                #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at NodeGetHandleList, Index: ',

                         IN2 := INT_TO_WSTRING(#i));

             END_IF;

         END_FOR;

         #State := #State + 1;

END_IF;

###### What is the purpose of the parameter "NamespacesIndexes"?

The parameter "NamespaceIndexes" implements the indexes for the namespaces.

Implementation of indexes is necessary, for example, when you read the node identifiers in your user program from an external list, for example, from an exported OPC UA XML file.

In this case you must enter the index that the OPC UA server is currently using for the namespace for all identifiers in the list.

Besides, the indexes of the namespaces might change so that you have to adapt the list each time.

**Automatic change of the indexes**

You can automatically implement the indexes of the namespaces: To do so, use the parameters "NamespaceIndexes" and "NamespacesIndexCount" of the "OPC_UA_NodeGetHandleList" instruction.

Follow these steps:

1. Check which namespace is assigned to the NodeIds that you read in from a list.

   In the example, the NodeIds are assigned to namespace index 0.

   In the example, the NodeIds are in the Siemens namespace "http://www.siemens.com/simatic-s7-opcua".
2. Create an array of the type "WString".

   In the example, the array is named "myNamespaces".
3. Enter the Siemens namespace "http://www.siemens.com/simatic-s7-opcua" under "myNamespaces[0]" (also in array element 0).
4. Provide the "NamespaceUris" parameter with the new array "myNamespaces".

   The instruction provides the result (the current index) at the parameter "NamespaceIndexes".
5. Create an array of the type "UInt" for the result.

   In the example, the array is named "myNamespaceIndexes".
6. Provide the "NamespaceIndexes" parameter with the new array "myNamespaceIndexes".
7. Also assign this array "myNamespaceIndexes" to the "NamespacesIndexes" parameter of the instruction "OPC_UA_NodeGetIndexList".

   This instruction then reads the current index of the Siemens namespace from "myNamespaceIndexes[0]" and uses it (instead of the original namespace index 0). This implements the index.
8. Assign the value 1 to the "NamespacesIndexCount" parameter of the instruction "OPC_UA_NodeGetIndexList" (we are using only one namespace in the example).

The following program code shows an implementation of the example:

SCL

#OPC_UA_NodeGetHandleList_Instance(REQ := #Req,

            ConnectionHdl := #ConnectionHdl,

            NodeIDCount := 2,

            NodeIDs := #TargetNodeIds,

            Timeout := T#6S,

            NamespaceIndexCount := 1,

            NamespaceIndexes := #myNamespaceIndexes,

            NodeStatusList := #NodeStatusList,

            NodeHdls := #NodeHdls,

            Done => #Done,

            Busy => #Busy,

            Error => #Error,

            Status => #Status);

**The parameters "NamespaceIndexes" and "NamespaceIndexCount" are optional.**

If index conversion is not required, the "NamespaceIndexes" and "NamespaceIndexCount" parameters do not need to be supplied.

Index conversion is not required when the NodeIds are specified directly with the correct namespace, e.g. when the NodeIds are determined using the "OPC_UA_TranslatePathList" instruction.

---

**See also**

[OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500)
  
[OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)
  
[OPC_UA_ConnectionGetStatus: Read connection status (S7-1500)](#opc_ua_connectiongetstatus-read-connection-status-s7-1500)

##### OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)

###### Validity

The following description of the "OPC_UA_TranslatePathList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the "OPC_UA_TranslatePathList" instruction to navigate (browse) in the address space of an OPC UA server and determine the node ID (NodeId) of a node that the OPC UA server uses for this node.

The instruction is used for use cases in which BrowseNames and the paths of the nodes are defined, but the NodeIds are not known and can therefore differ from server to server.

In principle, the following applies: Start the navigation at a node whose NodeId is known. For example, the nodes from the "http:\\opcfoundation.org/UA/" namespace of the OPC Foundation are known.

Example of a start node: "Objects". Other possible start nodes are "DeviceSet" or an underlying root node of the information model used in the address space of the server whose NodeId you have determined.

The "Objekts" node is used in the example below. Starting from this start node, you use the existing BrowseNames to navigate from node to node until you finally arrive at the destination node. At the target node, you read out the sought after NodeId ("NodeID" attribute).

**Example**

An OPC UA server of a device publishes a server interface that meets the Companion specification AutoID. The Companion specification defines the BrowseNames of OPC UA nodes. This means that you know the BrowseNames of these nodes. However, you do not know which NodeIds the OPC UA server that you are querying uses for these nodes. In this case, use the "OPC_UA_TranslatePathList" instruction.

**Alternative**

STEP 7 (TIA Portal) offers you an alternative to the "OPC_UA_TranslatePathList" instruction. You can create a client interface in STEP 7 under "Project tree", <CPU name>, "OPC UA communication" and configure read, write or method lists. STEP 7 then automatically determines the NodeIds of the node.

However, this alternative requires that you can reach the OPC UA server of this device online or that you use the OPC UA XML file of the device.

**Symbol of the instruction**

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112215065611_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

OPC_UA_TranslatePathList is used to prepare the data exchange, see ① in the figure below.

To do this, provide the instruction with the browse paths; the instruction returns the NodeIds of the nodes you are looking for.

![Description](images/103724861707_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_TranslatePathList"

The parameters of the instruction "OPC_UA_TranslatePathList"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| BrowsePathsCount | Input | UINT | Number of elements in BrowsePaths (max. 10). |
| BrowsePaths | InOut | VARIANT | Pointer to an array of the type [OPC_UA_BrowsePath](#opc_ua_browsepath-s7-1500).   The array contains the individual browse paths you want to follow. |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.   See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NamespaceIndexCount | Input | UINT | Number of elements in NamespaceIndexes. |
| NamespaceIndexes | InOut | VARIANT | Pointer to an array of the type UINT.  This parameter is ignored if NamespaceIndexCount is 0.  The array is used to convert the indexes for the namespaces that are passed in the BrowsePaths parameter.  Example:  If there is a value of 10 in NamespaceIndexes[4], all NodeIds in the "BrowsePaths" parameter that previously had the namespace index 4 are assigned the namespace index 10. |
| TargetNodeIDs | InOut | VARIANT | Pointer to an array of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the NodeIds found. |
| TargetStatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error numbers for the individual browse paths.  The first element in the array refers to the first element in the BrowsePaths parameter, etc.; see "Error numbers for TargetStatusList" |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### "NamespacesIndexes" parameter

The "NamespaceIndexes" parameter for converting the namespace indexes is optional.

- If you use this parameter ("NamespaceIndexCount" > 0), the namespace indexes of the parameter "BrowsePaths" are converted (to references, BrowseNames and start nodes).
- If you **do not** use this parameter as in the example below ("NamespaceIndexCount" = 0), the namespace indexes in the "BrowsePaths" must be set correctly. This means the instruction "OPC_UA_TranslatePathList" does not evaluate the "NamespaceIndexes"" parameter. If you call the "OPC_UA_NodeGetHandleList" instruction in the next step, you also must not convert the namespace indexes, since they are up to date. Therefore, set the "NamespaceIndexCount" parameter of the instruction "OPC_UA_NodeGetHandleList" to 0. Then you do not have to supply the "NamespaceIndexes" parameter.

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8002_0000 | OpcUa_BadInternalError | An error occurred as a result of an internal programming error in the function block.   Contact Support. |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA - Reduce the number of OPC UA clients that are currently connected to the server - Set up fewer subscriptions |
| 8009_0000 | OpcUa_BadUnknownResponse | Server did not respond with the expected number of results |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_TranslatePathList" instructions that can be called at the same time per connection has been exceeded  (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "BrowsePaths". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "NamespaceIndexes". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "TargetNodeIDs". |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for parameter "TargetStatusList". |
| B080_1100 | Simatic_ArrayElements_TooMany | BrowsePathscount > MAX_ELEMENTS_RELATIVEPATH |
| B080_3100 | BadNumElements_VariantInput1 | BrowsePathsCount > Number of array elements of the "BrowsePaths" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | NamespaceIndexCount > Number of array elements of the "NamspaceIndexes" parameter. |
| B080_3300 | BadNumElements_VariantInput3 | BrowsePathsCount > Number of array elements of the "TargetNodeIDs" parameter. |
| B080_3400 | BadNumElements_VariantInput4 | BrowsePathsCount > Number of array elements of the "TargetStatusList" parameter. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: Parameter "BrowsePathsCount" is not supplied or "BrowsePathsCount" = 0. |
| B080_C600 | Simatic_ClientNotAvailable | Error during initialization of the client |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of this type running in parallel, see:[Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "TargetStatusList"

The "TargetStatusList" parameter contains an error code for each individual NodeId (tag).

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Value successfully read. |
| 8033_0000 | OpcUa_BadNodeIdInvalid | The syntax of the NodeId is incorrect. |
| 8034_0000 | OpcUa_BadNodeUnknown | The node handle transferred is not known. |
| 8035_0000 | OpcUa_BadAttributeInvalid | The attribute required is not supported for the specified node. |
| 8037_0000 | OpcUa_BadIndexRangeNoD | There is no data in the index range. |
| 8039_0000 | OpcUa_BadDataEncodingUnsupported | The OPC UA server does not support the required data decoding for this node. |
| 803A_0000 | OpcUa_BadNotReadable | No rights for reading or subscribing (Subscribing) this node. |
| 803C_0000 | OpcUa_BadOutOfRange | The index value specified in the NodeAddInfos parameter is outside the permitted range. |
| 803D_0000 | OpcUa_BadNotSupported | The OPC UA server does not support one of the requested functions. Some OPC UA servers do not allow access to the index ranges of an array. |
| 8060_0000 | OpcUa_BadBrowseNameInvalid | The NamespaceIndex of the QualifiedName does not exist. |
| 806F_0000 | OpcUa_BadNoMatch | The specified path does not lead to a node. |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on an example, this section shows you how to use the instruction "OPC_UA_TranslatePathList" in a program.

**Example**

Let us assume that RFID readers scan the outgoing goods at the gates of a plant.

In the example, the first reader is called "RfidReader_Door_1".

The RFID readers are OPC UA servers that make their data and methods available to OPC UA clients.

**Specification AutoID**

The RFID readers come with a standardized interface according to the Companion Specification "AutoID".

The names of the properties and methods of the RFID readers are specified by the standardization.

The figure below shows a section of the address space of the reader "FfidReaderDoor_1" in UAExpert, a tool from Unified Automation.

The node "RfidReader_Door_1" is located under "DeviceSet".

Below it, you can see the released properties and methods of the reader according to the AutoId:

![This is how you use this instruction](images/103430747275_DV_resource.Stream@PNG-de-DE.png)

The properties and methods of the reader are known because the reader adhere to the AutoID specification.

**Not** known are the following elements:

- The name "RfidReader_Door_1". The name can be freely selected or is specified in the respective plant.
- The NodeId of the "RfidReader_Door_1" node in the address space of the reader
- The NodeIds of the properties and methods of the reader, which means all nodes below "RfidReader_Door_1", see figure above.

**Procedure for determining NodeIds**

- You work with a client interface and configure a read, write or method list via drag-and-drop.

  To do this access the OPC UA server online or use the OPC UA XML file of the server that contains the NodeIds of the tags you are looking for. STEP 7 (TIA Portal) then automatically determines the NodeIDs of the tag.

  It is not necessary to call the "OPC_UA_TranslatePathList" instruction here.
- You are using a tool such as UAExpert:

  - Read the NodeId from "RfidReader_Door_1".
  - Read the NodeIds of all lower-level properties and methods of this reader that you want to use in your user program.

  The next step in your program is the call of "OPC_UA_NodeGetHandleList".
- You are working with the instruction "OPC_UA_TranslatePathList".

  You first define the browse path (BrowsePath) for this instruction. This path can start at the "Objects" node but also any other node whose NodeId you are familiar with.

  The NodeId "i=85" is always assigned to the "Objects" node (according to the OPC UA specification). The following example uses a BrowsePath that originates from the "Objects" node. After you have determined the NodeIds of the tags you are looking for with "OPC_UA_TranslatePathList", use these NodeIDs in the next step when calling the "OPC_UA_NodeGetHandleList" instruction.

###### Introduction to the program example

The following program example shows you how to use the "OPC_UA_TranslatePathList" instruction to determine the NodeIds for two tags.

The tags sought after in the example are "DeviceInfo" and "DeviceStatus", the path used (BrowsePath) starts at the "Objects" node (NodeId: i=85) and leads to the tags searched for via "productionline", "DataBlocksGlobal" and "RfidReader_Door_1", see figure below.

![Introduction to the program example](images/119980411147_DV_resource.Stream@PNG-de-DE.png)

###### Requirement

The following requirement must be fulfilled for the "OPC_UA_TranslatePathList" instruction:

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).

  You can use the connection configuration for OPC UA in TIA Portal to configure a connection to an OPC UA server.

  If you do not use this connection configuration, you have to set the connection parameters in your user program. How to proceed is shown in the section "Establishing a connection to an OPC UA server" in the further course of this description.

###### Calling the instruction (initial call)

This section describes the function block "Read_from_RfidReader_Door_1". The function block shows you how to use the instruction "OPC_UA_TranslatePathList".

You can find the complete example in the section "[Example program for OPC_UA_TranslatePathList](#example-program-for-opc_ua_translatepathlist-s7-1500)".

**Declaration of tags**

Declare an instance of the instruction "OPC_UA_TranslatePathList" and the tags with which you are supplying the instruction parameters.

The program example uses the following declaration:

![Calling the instruction (initial call)](images/104324059531_DV_resource.Stream@PNG-de-DE.png)

**User program**

The following excerpt from the user program defines the browse path for the PLC tag "DeviceInfo". The definition for "DeviceStatus" is not shown.

First, the start node (StartingNode) is defined. This leads to the browse path of the node you are looking for. The path to the node (RelativePath) you are looking for is defined below.

The first browse path (BrowsePaths[0]) starts at the "Objects" node (NodeId i=85) and leads to the searched "DeviceInfo" tag via "productionline", "DataBlocksGlobal" and "RfidReader_Door_1".

**Define start nodes**

The following user program first sets the start node to "Objects".

The "Objects" node was defined by the OPC Foundation in the namespace "http://opcfoundation.org/UA/". The index 0 in the namespace array of an OPC UA server is always assigned to this namespace.

OPC UA servers publish this namespace array in their address space so that OPC UA clients can use the index instead of the namespace to address a node.

The "Objects" node has the NodeId "i=85", with the namespace index 0 (namespace index 0 is not specified to simplify the NodeId).

The NodeId "i=85" also indicates the type of identifier: This NodeId is a numeric identifier (an integer).

The following program lines pass the identifier "85", determine the type of the identifier and set the namespace index:

#BrowsePaths[0].StartingNode.Identifier := WString#'85';

#BrowsePaths[0].StartingNode.IdentifierType := 0;

#BrowsePaths[0].StartingNode.NamespaceIndex := 0;

**Define RelativePath**

The first stage of the navigation in the following program example leads to the node with the BrowseName "productionline".

Then the navigation continues to the nodes with the BrowseNames "DataBlocksGlobal", "RfidReader_Door_1" and finally "DeviceInfo".

In the program example, these nodes are all in the namespace "http://www.siemens.com/simatic-s7-opcua". The index of this namespace is stored in the local tag "#NamespaceIndexes[0]" and is set directly in the program code.

**References for OPC UA**

The address space of an OPC UA server consists of OPC UA nodes that refer to each other. These pointers from one node to another are called references. OPC UA defines several types of references.

The following program example uses the hierarchical reference to determine the NodeIds of OPC UA nodes located below another OPC UA node.

Reference used in the example: The node with the BrowseName "DeviceInfo" is arranged below "RfidReader_Door_1". This means that the two nodes have a hierarchical relationship to each other.

SCL

//Sets the first BrowsePath, BrowsePath[0]

//This BrowsePath starts at node "Objects" and leads to node "DeviceInfo"

//First, we assign "Objects" to "StartingNode".

//"Objects" has always NodeId i=85. It is a numerical NodeId with namespaceindex 0.

#BrowsePaths[0].StartingNode.Identifier := WString#'85';

#BrowsePaths[0].StartingNode.IdentifierType := 0;

#BrowsePaths[0].StartingNode.NamespaceIndex := 0;

//Second, we set "RelativePath".

//Our BrowsePath goes to "productionline", "DataBlocksGlobal", "RfidReader_Door_1",

//and finally to "DeviceInfo".

//Therefore, we set "NoOfElements" to four elements.

#BrowsePaths[0].RelativePath.NoOfElements := 4;

//The first element of our RelativePath is "productionline'.

//Therefore, we set "TargetName.Name" to "productionline'

//In our example code, the namespaceindex of "productionline' is stored

//in our local variable "#NamespaceIndexes[0]";

//The node "productionline' is conntected to our starting node

//"Objects" via a HierarchicalReference.

//This reference always has the numerical NodeId i=33 assigned to it, with namespaceindex 0.

//This reference is set by default.

//Therefore, you can skip the following three lines of code.

#BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.Identifier := WString#'33';

#BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.IdentifierType := 0;

#BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.NamespaceIndex := 0;

#BrowsePaths[0].RelativePath.Elements[1].TargetName.Name := WString#'productionline';

#BrowsePaths[0].RelativePath.Elements[1].TargetName.NamespaceIndex := #NamespaceIndexes[0];

//The second element of our RelativePath is "DataBlocksGlobal'.

#BrowsePaths[0].RelativePath.Elements[2].TargetName.Name := WString#'DataBlocksGlobal';

#BrowsePaths[0].RelativePath.Elements[2].TargetName.NamespaceIndex := #NamespaceIndexes[0];

//The third element of our RelativePath is "RfidReader_Door_1'.

#BrowsePaths[0].RelativePath.Elements[3].TargetName.Name := WString#'RfidReader_Door_1';

#BrowsePaths[0].RelativePath.Elements[3].TargetName.NamespaceIndex := #NamespaceIndexes[0];

//The fourth element of our RelativePath is "DeviceInfo'.

#BrowsePaths[0].RelativePath.Elements[4].TargetName.Name := WString#'DeviceInfo';

#BrowsePaths[0].RelativePath.Elements[4].TargetName.NamespaceIndex := #NamespaceIndexes[0];

###### Establishing a connection to an OPC UA server

The following section of the example program shows you how to manually (with a program) configure a connection to an OPC UA server in your user program without using the connection configuration provided by STEP 7 (TIA Portal).

The SCL program assigns corresponding values to the parameters for this purpose.

The program example first defines the server endpoint "opc.tcp://192.168.1.1:4840", because the "opc.tcp" protocol is used for OPC UA and the server has the IP address "192.168.1.1".

Security mode "2" (SecurityMsgMode) is set so that messages are transmitted signed. The value "Basic128Rsa15" is set as the procedure for signing (SecurityPolicy). The number of the client certificate (CerificateID) is also specified. The number 6 is used in the example.

SCL

CASE #State OF

1: // case 1, connect to server

IF #FirstCall = TRUE THEN

    #FirstCall := FALSE;

    //set ServerEndPointUrl of the server we want to connect to

    #SeverEndpointUrl := WString#'opc.tcp://192.168.1.1:4840';

    //set Securtiy Message Mode

    // 1 = None, 2 = Sign, 3 = Sign & Encrypt

    #SessionConnectInfo.SecurityMsgMode := 1;

    //set Security Policy

    // 1 = None, 2 = Basic128Rsa15,, 3 = Basic256, 4 = Basic256Sha256

    #SessionConnectInfo.SecurityPolicy := 2;

    //set the number of the client certificate you are using

    //in our case, this is 6

    //#SessionConnectInfo.CertificateID := 6;

END_IF;

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

#OPC_UA_Connect_Instance(REQ:=#Req,

          ConnectionHdl=>#ConnectionHdl,

          ServerEndpointUrl:=#SeverEndpointUrl,

          SessionConnectInfo:=#SessionConnectInfo,

          Timeout:=T#8S,

          Done=>#Done,

          Busy=>#Busy,

          Error=>#Error,

          Status=>#Status);

###### Determining the NodeIds of the DeviceInfo and DeviceStatus nodes

The following excerpt from the example program "Read_From_RfidReader_Door_1" queries the OPC UA server for NodeIds of nodes with the BrowseName "DeviceInfo" and "DeviceStatus".

You can find the complete example in the section "[Example program for OPC_UA_TranslatePathList](#example-program-for-opc_ua_translatepathlist-s7-1500)".

SCL

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

#OPC_UA_TranslatePathList_Instance(REQ := #Req,

          ConnectionHdl := #ConnectionHdl),

          BrowsePathsCount := 2,

          BrowsePaths := #BrowsePaths,

          Timeout := T#6S,

          NamespaceIndexCount := 0,

          TargetNodeIDs := #TagetNodeIds,

          TargetStatusList := #TargetStatusList,

          Done => #Done,

          Busy => #Busy,

          Error => #Error,

          Status => #Status);

IF #Done = TRUE THEN

    IF #TargetStatusList[0] = 0 AND #TargetStatusList[1] = 0 THEN

          #State := #State + 1;

    ELSE

          #State := 100;

          #Mem_Status := #Status;

          #Output_Error_Message := WString#'Error at TranslatePathList';

    END_IF;

          #FirstCall := TRUE;

END_IF;

IF #Error = TRUE THEN

    //In case 100, to set REQ of instruction "OPC_UA_TranslatePathList" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #State := 100;

    #Mem_Status := #Status;

    #OPC_UA_TranslatePathList_Instance(REQ := FALSE,

          ConnectionHdl := #ConnectionHdl,

          BrowsePathsCount := 2,

          BrowsePaths := #BrowsePaths,

          TargetNodeIDs := #TagetNodeIds,

          TargetStatusList := #TargetStatusList);

    #FirstCall := TRUE;

END_IF;

The example program calls the "OPC_UA_TranslatePathList" instruction for the following reasons:

- To request the NodeId for the nodes with BrowseName "DeviceInfo" and "DeviceStatus".
- To set the REQ parameter to FALSE, if an error has occurred.

**Asynchronous execution**

The instruction "OPC_UA_TranslatePathList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of how to determine the NodeIds

If the "OPC_UA_TranslatePathList" instruction is not yet executed, #Busy is FALSE so that the "#Req" tag is set to TRUE. This starts the instruction.

In the next cycle, #Req is FALSE.

If the output parameter "Error" is TRUE, an error occurred during execution of the instruction. This sets the "#State" tag to the value 100. This case is reserved for troubleshooting.

If the output parameter "Done" is TRUE, the instruction was executed successfully.

Note: It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but no NodeId could be returned for a PLC tag.

Therefore, there is a check in the example to determine whether the program has obtained a NodeId for each PLC tag:

- If a NodeId is returned for the first tag, the first element of the array to which the "TargetStatusList" parameter is pointing contains the value 0.
- If a NodeId is returned for the second tag, the first element of the array to which the "TargetStatusList" parameter is pointing contains the value 0.

If both conditions are met, the output parameter "TargetNodeHdls" points to a valid list with the NodeIds. This increases the value of the "#State" tag by one. The next program section - Case 4 - is then executed in the next cycle.

Case 4 is described in [OPC_UA_NodeGetHandleList: Get handles for read and write access](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500).

---

**See also**

[OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)
  
[OPC_UA_NodeAdditionalInfo (S7-1500)](#opc_ua_nodeadditionalinfo-s7-1500)
  
[OPC_UA_NodeAdditionalInfoExt (S7-1500)](#opc_ua_nodeadditionalinfoext-s7-1500)
  
[OPC_UA_ConnectionGetStatus: Read connection status (S7-1500)](#opc_ua_connectiongetstatus-read-connection-status-s7-1500)

#### Data exchange (S7-1500)

This section contains information on the following topics:

- [OPC_UA_ReadList: Reading tags (S7-1500)](#opc_ua_readlist-reading-tags-s7-1500)
- [Reading array range information with OPC_UA_ReadList (S7-1500)](#reading-array-range-information-with-opc_ua_readlist-s7-1500)
- [OPC_UA_WriteList: Write tags (S7-1500)](#opc_ua_writelist-write-tags-s7-1500)
- [Writing an array section with OPC_UA_WriteList (S7-1500)](#writing-an-array-section-with-opc_ua_writelist-s7-1500)
- [Set OPC UA-DataValue with OPC_UA_WriteList (S7-1500)](#set-opc-ua-datavalue-with-opc_ua_writelist-s7-1500)

##### OPC_UA_ReadList: Reading tags (S7-1500)

###### Validity

The following description of the "OPC_UA_ReadList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_ReadList" to read the values of PLC tags.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112216442507_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_ReadList" is used to read tags from a OPC UA server, see ② in the figure below.

The instruction returns a list with values of tags.

In addition to the tag values, you can also read other tag attributes. This is specified by the AttributeID, see [OPC_UA_NodeAdditionalInfo](#opc_ua_nodeadditionalinfo-s7-1500).

![Description](images/110504988939_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

> **Note**
>
> **Firmware dependency when reading OPC UA arrays**
>
> Up to and including firmware version V2.9, the size of an array that is part of a structure in your program must exactly match the size of the OPC UA array that is read. As of firmware version V3.0, the array size in the PLC program may be larger than the size of the read OPC UA array. It is recommended that you completely reset the values in your program before the read operation, because the firmware of the PLC does not do this. If the currently read array is smaller than the previously read one, there is a risk that you are accessing old or invalid values in your program.
>
> The following applies in regard to compatibility: Accesses that have worked so far will continue to work. Accesses that were previously incorrect may now return values.

###### Parameters for "OPC_UA_ReadList"

The parameters of the instruction "OPC_UA_ReadList"

| Parameters | Declaration | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeHdlCount | Input | UINT | Number of elements in the array that points to the NodeHdls parameter. |
| NodeHdls | InOut | VARIANT | Pointer to an array of the type DWORD.   The array contains the node handles of the tags whose values are to be read. |
| NodeAddInfos | InOut | VARIANT | Pointer to an array of the type [OPC_UA_NodeAdditionalInfo](#opc_ua_nodeadditionalinfo-s7-1500) or [OPC_UA_NodeAdditionalInfoExt](#opc_ua_nodeadditionalinfoext-s7-1500).  The array defines which attribute is to be read in the node (in a tag).  The first element in this array refers to the first element in the array to which the "NodeHdls" parameter points.  The parameter is optional. If it is not set, the values of all nodes (tags) are read.  When reading arrays, you can limit which elements of the array are to be read, see [Reading array range information with OPC_UA_ReadList](#reading-array-range-information-with-opc_ua_readlist-s7-1500). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in[OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeStatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error codes for the individual tags (see "Error numbers for NodeStatusList" below).  For each tag, it is specified whether its value could be read.  It is possible that the instruction was successfully executed (Error parameter not set) but no value could be read for a specific NodeId (tag). |
| TimeStamps | InOut | VARIANT | Pointer to an array of the type LDT.  The first element in this array refers to the first element in the array to which the NodeHdls parameter points.  The parameter is optional. If it is not set, the OPC UA server does not return a time stamp. |
| Variable | InOut | VARIANT | Pointer to a tag that saves the values to be read.  You must create a PLC data type (UDT) or a structure (STRUCT) for this tag. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Function block executed successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | Server did not respond with the expected number of results |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_ReadList" instructions that can be called at the same time per connection has been exceeded (> 5), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 8074_0000 | OpcUa_BadTypeMismatch | You are using a data type that does not correspond to the data type in the server. |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "NodeHdls". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "NodeAddInfos". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "NodeStatusList". |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for parameter "TimeStamps". |
| B080_0500 | Simatic_BadType_VariantInput5 | Incorrect data type for parameter "Variable" (not UDT). |
| B080_1100 | Simatic_ArrayElements_TooMany | NodeHdlCount > MAX_ELEMENTS_NODELIST  NamespaceIndexCount > MAX_ELEMENTS_NAMESPACES |
| B080_3100 | BadNumElements_VariantInput1 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeHdls" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeAddInfos" parameter. |
| B080_3300 | BadNumElements_VariantInput3 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeStatusList" parameter. |
| B080_3400 | BadNumElements_VariantInput4 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "TimeStamps" parameter. |
| B080_3500 | BadNumElements_VariantInput5 | The PLC data type/structure for the parameter "Variable" has too few or too many elements as specified by the value for the parameter "NodeHdlCount".   Example: If "NodeHdlCount" has the value 5, then the array "NodeHdls" must also contain 5 elements. The structure for the parameter "Variable" must also consist of 5 elements. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see:  [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "NodeStatusList"

The "NodeStatusList" parameter contains an error code for each individual node handle (tag).

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Value successfully read. |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The node handle transferred is not known. |
| 8035_0000 | OpcUa_BadAttributeInvalid | The attribute required is not supported for the specified node. |
| 8037_0000 | OpcUa_BadIndexRangeNoD | There is no data in the index range. |
| 8039_0000 | OpcUa_BadDataEncodingUnsupported | The OPC UA server does not support the required data decoding for this node. |
| 8074_0000 | OpcUa_BadTypeMismatch | Double / Float value in ReadResponse is NaN  UDT Member tag has incorrect type |
| 803A_0000 | OpcUa_BadNotReadable | No rights for reading or subscribing (Subscribing) this node. |
| 803C_0000 | OpcUa_BadOutOfRange | The index value specified in the NodeAddInfos parameter is outside the permitted range. |
| 803D_0000 | OpcUa_BadNotSupported | The OPC UA server does not support one of the requested functions.  Some OPC UA servers do not allow access to the index ranges of an array. |
| 80AB_0000 | OpcUa_BadInvalidArgument | StartIndex > EndIndex |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_ReadList" in a user program that reads the values of PLC tags.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".
- If the CPU is to read and write **structures** in the OPC UA server as an OPC UA client: The OPC UA server supports version V1.04 of the OPC UA specification.

The following requirements must also be met for the "OPC_UA_ReadList" instruction:

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the following instruction: [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).
- A list of the handles for the individual tags whose values you want to read from the OPC UA server.

  You get the handle list from the following instruction: [OPC_UA_NodeGetHandleList: Get handles for read and write access](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500)

###### Function of the instruction

You use the instruction "OPC_UA_ReadList", for example, to read the values of tags from an OPC UA server (see above).

**What information is required?**

The instruction requires the following information:

- The handles for the tags whose values you want to read ("NodeHdls" parameter).

**What information does the instruction return?**

The instruction returns the following information:

- The current values of the tags the ("Variable" parameter).

  The order of the values corresponds to the order of the handles in the "NodeHdls" parameter.

  Refer to the following cases for this purpose:

  - When you use a client interface with a read list, STEP 7 automatically creates a system data type with the tags that need to be read.
  - If you are not using a client interface, you must create a PLC data type (UDT) or a structure (STRUCT) for the "Variable" parameter.

    You define the components of this UDT according to the tags that have to be read.

    Use the SIMATIC data type compatible with the respective OPC UA data type, see [Mapping SIMATIC data types to OPC UA data types](Configuring%20automation%20systems.md#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t).
- A list of error messages ("NodeStatusList" parameter).

  Each error message in this list relates to the corresponding handle in the "NodeHdls" parameter, NodeStatusList[0] refers to NodeHdls[0].

  For each individual tag (each individual "NodeHdl"), you need to check whether the OPC UA server was able to return a valid value.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU that acts as the client.
2. Select the function block that is to contain the client instruction in the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_ReadList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction: "OPC_UA_ReadList_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_ReadList_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is named "Productionline".
7. Click "Data access" and select a read list.

   In the example, the read list is named "ReadListProduct".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
8. Click on "Block parameters" and assign tags manually to the remaining parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

You can find the complete program in the section "[Program example for reading PLC tags](#program-example-for-reading-plc-tags-s7-1500)".

The program example uses the read list "ReadListProduct", which contains the following PLC tags:

- NewProduct
- ProductNumber

The program reads the values of these tags from the server.

The section [Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t) shows you how to create a client interface and how to add a read list with PLC tags to it.

The example program is divided into multiple sections (cases) by a CASE instruction.

In the fourth program section, the tag values are read:

SCL

4: // case 4, read from nodes

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

OPC_UA_ReadList_Instance(REQ := #Req,

             ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

             NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

             NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

             Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

             NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

             TimeStamps := "Productionline_Data"."ReadListProduct".TimeStamps,

             Variable := "Productionline_Data"."ReadListProduct".Variable,

             Done => #Done,

             Busy => #Busy,

             Error => #Error,

             Status => #Status);

**Asynchronous execution**

The instruction "OPC_UA_ReadList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The figure above shows case 4.

This part of the program calls the "OPC_UA_ReadList" instruction to read the values of PLC tags.

If the instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

IF #Done = TRUE THEN

    FOR #i := 0 TO UINT_TO_INT("Productionline_Configuration".ReadLists."ReadListProduct".NodeCount) - 1 DO

        IF NOT ("Productionline_Data"."ReadListProduct".NodeStatusList[#i] = 0) THEN

              #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at Readlist "ReadListProduct", Index: ',

              IN2 := INT_TO_WSTRING(#i));

        END_IF;

    END_FOR;

    #State := #State + 1;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #Mem_Status := #Status;

    #OPC_UA_ReadList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

              NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

              TimeStamps := "Productionline_Data"."ReadListProduct".TimeStamps,

              Variable := "Productionline_Data"."ReadListProduct".Variable);

END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the "Error" output parameter is set to the value TRUE. This sets the value of the "#State" tag to 100. This case is reserved for troubleshooting. The example program also calls the "OPC_UA_ReadList" instruction to set the REQ parameter to FALSE.

If the TRUE value is in the "Done" output parameter, the instruction is successfully executed.

Note: It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but no PLC tag could be read.

Therefore, there is a check in the example for each PLC tag to determine whether the program has obtained a valid value:

- If the server is sending a valid value for the first PLC tag, the first element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

  In the example, the status code is listed in "Productionline_Data"."ReadListProduct".NodeStatusList[0].
- If the server is sending a valid value for the second PLC tag, the second element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

  In the example, the status code is listed in "Productionline_Data"."ReadListProduct".NodeStatusList[1].

The program outputs an error message when it recognizes an invalid value.

Even if one or two invalid values are detected, the value of the "#State" tag is increased by one. This means the next program section - case 5 - is executed in the next cycle.

Case 5 is described in [OPC_UA_NodeReleaseHandleList: Release handles for read and write access](#opc_ua_nodereleasehandlelist-release-handles-for-read-and-write-access-s7-1500).

---

**See also**

[OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)
  
[OPC_UA_NodeId (S7-1500)](#opc_ua_nodeid-s7-1500)
  
[OPC_UA_TranslatePathList: Determine current NodeIds (S7-1500)](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500)
  
[OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)

##### Reading array range information with OPC_UA_ReadList (S7-1500)

###### Introduction

This section is based on "OPC_UA_ReadList"; see [OPC_UA_ReadList: Reading tags](#opc_ua_readlist-reading-tags-s7-1500).

The section describes how to read parts of an array with the "OPC_UA_ReadList" instruction.

Reading parts of an array from an OPC UA server basically works as follows:

![Introduction](images/115339028875_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Reading parts of an array from an OPC UA server |

###### Requirements

The following description assumes that:

- You have configured a CPU as **OPC UA server**.

  The server provides an array that can be read by OPC UA clients.

  In the example, the CPU is called "Productionline", which provides the data block "Data_for_OPC_UA_Clients" for OPC UA clients:

  ![Requirements](images/110600119051_DV_resource.Stream@PNG-de-DE.png)
- You have configured a CPU as **OPC UA client**.

  You have created a client interface in the client.

  The client interface contains a read list with an array of which you want to read a part.

  In the example, the client interface is called "Productionline" with the read list "ReadListProduct":

  ![Requirements](images/110513388427_DV_resource.Stream@PNG-de-DE.png)

  The values in "Temperature[5]" to "Temperature[9]" are read from the "Temperature" array of the server.

###### Providing additional information

"OPC_UA_ReadList" shows how to read out entire scalars (tags with a value) or arrays (tags with multiple values) using the "OPC_UA_ReadList" instruction.

The following section provides additional details to "OPC_UA_ReadList" that are required for using "OPC_UA_ReadList" to read part of an array.

**OPC_UA_NodeAdditionalInfo**

First create a local tag of the type "OPC_UA_NodeAdditionalInfo", see "[OPC_UA_NodeAdditionalInfo](#opc_ua_nodeadditionalinfo-s7-1500)".

This tag is used to tell the "OPC_UA_ReadList" instruction which part of the array is to be read.

Proceed as follows:

1. Create an array tag of the type "OPC_UA_NodeAdditionalInfo".

   In the example, the tag is created in the declaration section of the function block, which calls the "OPC_UA_ReadList" instruction.

   The new local tag is called "NodeAdditionalInformation":

   ![Providing additional information](images/110546887179_DV_resource.Stream@PNG-de-DE.png)

   The new local tag "NodeAdditionalInformation" contains three components of the type OPC_UA_AdditionalInfo, because the read list "ReadListProduct" contains three nodes.

   NodeAdditionalInformation[0] provides additional information on the first tag to be read (in the example, "NewProduct")

   NodeAdditionalInformation[1] provides additional information on the second tag to be read (in the example, "ProductNumber")

   NodeAdditionalInformation[2] provides additional information on the third tag to be read (in the example, "Temperature")
2. Assign values to the new tag (in the "Default values" column of the declaration section).

   In the example, the third tag (Temperature is partially read.

   NodeAdditionalInformation[2].AttributeId is therefore assigned 13 (i.e. the values of the array are read).

   NodeAdditionalInformation[2].StartIndex is assigned a value of 5, as the reading starts at (and includes) index 5.

   NodeAdditionalInformation[2].EndIndex is assigned a value of 9, as the reading starts at (and includes) index 9.

   NodeAdditionalInformation[0] NodeAdditionalInformation[1] are set to default values.

   The "#ignore" constant contains the value 4_294_967_295. The server ignores this value for StartIndex and EndIndex and reads scalars and arrays completely.

   ![Providing additional information](images/110724812555_DV_resource.Stream@PNG-de-DE.png)

   Alternative:

   You can also set the values for NodeAdditionalInformation in the user program:

   `// set additonal information to Array-Index 0`

   `// we set default values here`

   `#NodeAdditionalInformation[0].AttributeID := 13;`

   `#NodeAdditionalInformation[0].StartIndex := 4_294_967_295;`

   `#NodeAdditionalInformation[0].EndIndex := 4_294_967_295;`

   `// set additonal information to Array-Index 1`

   `// we set default values here`

   `#NodeAdditonalInformation[1].AttributeID := 13;`

   `#NodeAdditonalInformation[1].StartIndex := 4_294_967_295;`

   `#NodeAdditonalInformation[1].EndIndex := 4_294_967_295;`

   `// set additonal information to Array-Index 2`

   `// because we want to read only five values from an array in the OPC UA server`

   `#NodeAdditonalInformation[2].AttributeID := 13;`

   `#NodeAdditonalInformation[2].StartIndex := 5;`

   `#NodeAdditonalInformation[2].EndIndex := 9;`

   **Note**:

   The array NodeAdditionalInformation of the type "OPC_UA_NodeAdditionalInfo" must contain as many components as the read list (3 in the example).
3. Assign NodeAdditionalInformation to the parameter "NodeAddInfos" of the instruction "OPC_UA_ReadList".

   The following figure shows the call of OPC_UA_ReadList with the new supply of the "NodeAddInfos" parameter:

   `#OPC_UA_ReadList_Instance(REQ := #Req,`

   `NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,`

   `NodeStatusList := "myProductionline_Data"."ReadListProduct".NodeStatusList,`

   `Variable := "myProductionline_Data"."ReadListProduct".Variable,`

   `ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,`

   `Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,`

   `NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,`

   `NodeAddInfos := #NodeAddtionalInformation,`

   `TimeStamps := "myProductionline_Data".ReadListProduct.TimeStamps,`

   `Done => #Done,`

   `Busy => #Busy,`

   `Error => #Error,`

   `Status => #Status);`

###### Result in the client

The "OP_UA_ReadList" instruction now reads only part of the "Temperature" array from the OPC UA server.

The figure below shows the array "Temperature". The client assigns the read values as of Index 0:

![Result in the client](images/110723225867_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> To read a section of a multi-dimensional array (up to six dimensions), use the "OPC_UA_NodeAdditionalInfoExt" data type.

##### OPC_UA_WriteList: Write tags (S7-1500)

###### Validity

The following description of the "OPC_UA_WriteList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_WriteList" to write new values to PLC tags.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112216663819_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_WriteList" is used to assign new values to PLC tags, see ② in the figure below.

The instruction returns a list with status information for each PLC tag.

![Description](images/103731480331_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for OPC_UA_WriteList

The parameters of the instruction OPC_UA_WriteList

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeHdlCount | Input | UINT | Number of elements in the array that points to the NodeHdls parameter. |
| NodeHdls | InOut | VARIANT | Pointer to an array of the type DWORD.   The array contains the node handles of the tags whose values are to be written. |
| NodeAddInfos | InOut | VARIANT | Pointer to an array of the type [OPC_UA_NodeAdditionalInfo](#opc_ua_nodeadditionalinfo-s7-1500) or [OPC_UA_NodeAdditionalInfoExt](#opc_ua_nodeadditionalinfoext-s7-1500).  The array defines which attribute is to be set in a node (in a tag).  The first element in this array refers to the first element in the array to which the NodeHdls parameter points.  The parameter is optional. If it is not set, the value is set in all nodes (tags).  When writing arrays, you can limit which elements of the array are to be written, see [Writing an array section with OPC_UA_WriteList](#writing-an-array-section-with-opc_ua_writelist-s7-1500). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.   See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeStatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error codes for the individual tags (see "Error numbers for NodeStatusList" below).  Whether or not the value could be set is indicated for each tag.  It is possible that the instruction was successfully executed (Error parameter not set) but a specific tag could not be assigned a value.   NodeStatusList[0] relates to NodeHdls[0], etc. |
| Variable | InOut | VARIANT | Pointer to a tag that contains the values to be written.  You must create a PLC data type (UDT) for this tag. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Function block executed successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | The server sends a response, that cannot be recognized. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_WriteList" instructions that can be called at the same time per connection has been exceeded (> 5), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "NodeHdls". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "NodeAddInfos". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "NodeStatusList". |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for parameter "Variable" (not UDT). |
| B080_1100 | Simatic_ArrayElements_TooMany | General error code. Occurs when an array has too many elements. |
| B080_3100 | BadNumElements_VariantInput1 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeHdls" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeAddInfos" parameter. |
| B080_3300 | BadNumElements_VariantInput3 | The "NodeHdlCount" parameter is greater than the number of ARRAY elements in the "NodeStatusList" parameter. |
| B080_3400 | BadNumElements_VariantInput4 | The PLC data type/structure for the parameter "Variable" has too few or too many elements as specified by the value for the parameter "NodeHdlCount".   Example: If "NodeHdlCount" has the value 5, then the array "NodeHdls" must also contain 5 elements. The structure for the parameter "Variable" must also consist of 5 elements. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see:  [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "NodeStatusList"

The "NodeStatusList" parameter contains an error code for each individual node handle (tag).

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Value successfully read. |
| 8034_0000 | OpcUa_BadNodeUnknown | The node handle transferred is not known. |
| 8035_0000 | OpcUa_BadAttributeInvalid | The attribute required is not supported for the specified node. |
| 8037_0000 | OpcUa_BadIndexRangeNoD | There is no data in the index range. |
| 8039_0000 | OpcUa_BadDataEncodingUnsupported | The OPC UA server does not support the required data decoding for this node. |
| 803B_0000 | OpcUa_BadNotWritable | No rights for writing for this node. |
| 803C_0000 | OpcUa_BadOutOfRange | The index value specified in the NodeAddInfos parameter is outside the permitted range. |
| 803D_0000 | OpcUa_BadNotSupported | The OPC UA server does not support one of the requested functions.  Some OPC UA servers do not allow access to the index ranges of an array. |
| 80AB_0000 | OpcUa_BadInvalidArgument | One or more arguments are invalid. |
| For more error codes, see[Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_WriteList" in a user program that sets new values in PLC tags.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".
- If the CPU is to read and write **structures** in the OPC UA server as an OPC UA client: The OPC UA server supports version V1.04 of the OPC UA specification.

The following requirements must also be met for the "OPC_UA_WriteList" instruction:

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).
- Indexes of the namespaces that contain the tags that you want to write with the client.

  You get the indexes from the instruction [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500).
- A list of the handles for the individual tags whose values you want to set in the OPC UA server.

  You get this handle list from the instruction [OPC_UA_NodeGetHandleList: Get handles for read and write access](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500).

In the program example below, the instruction is called once to send an enable signal to the OPC UA server.

###### Function of the block

You use the instruction "OPC_UA_WriteList" to write the values of tags in an OPC UA server.

**What information is required?**

The function requires the following information:

- The handles for the tags whose values you want to write ("NodeHdls" parameter)
- The values to be transferred for the individual tags ("Variable" parameter)

  Refer to the following cases for this purpose:

  - If you use a client interface with a write list, STEP 7 automatically creates a system data type with the tags that need to be transferred.
  - If you are not using a client interface, you must create a PLC data type (UDT) or a structure (STRUCT) for the "Variable" parameter.

    You define the components of this UDT according to the tags that have to be transferred.

    Use the SIMATIC data type compatible with the respective OPC UA data type, see [Mapping SIMATIC data types to OPC UA data types](Configuring%20automation%20systems.md#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t).

**What information does the instruction return?**

The instruction returns the following information:

- A list of error messages ("NodeStatusList" parameter).

  Each error message in this list relates to the corresponding handle in the "NodeHdls" parameter.

  For each individual tag ("NodeHdl"), you need to check whether the OPC UA server was able to accept the new value.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU that acts as the client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "WriteToProductionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_WriteList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_WriteList_Instance".
5. Click "OPC_UA_WriteList_Instance".

   STEP 7 opens the "Configuration".
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is named "Productionline",   
   (see [Example configuration for OPC UA](Configuring%20automation%20systems.md#example-configuration-for-opc-ua-s7-1500-s7-1500t) and "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)").
7. Click "Data access" and select a write list.

   In the example, the read list is named "WriteListStatus".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
8. Click on "Block parameters" and assign tags manually to the remaining parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

You can find the complete program in the section "[Example program for writing PLC tags](#example-program-for-writing-plc-tags-s7-1500)".

The program example uses the write list "WriteListStatus" which contains the following PLC tag:

- ProductionEnabled

The program writes the new value of this tag to the server.

The section "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)" shows you how to create a client interface and how to add a write list with PLC tags to it.

The example program is divided into multiple sections (cases) by a CASE instruction.

In the fourth program section, the tag values are written:

SCL

4: // case 4; write value to PLC variable "ProductionEnabled"

IF #SetProductionEnabled = TRUE THEN

    #SetProductionEnabled := FALSE;

    //set new value to true

    "Productionline_Data"."WriteListStatus".Variable.ProductionEnabled := TRUE;

END_IF;

IF #Busy = FALSE THEN

    #Req := TRUE;

ELSE

    #Req := FALSE;

END_IF;

OPC_UA_WriteList_Instance(REQ := #Req,

             ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

             NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

             NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

             Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

             NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

             Variable := "Productionline_Data"."WriteListStatus".Variable,

             Done => #Done,

             Busy => #Busy,

             Error => #Error,

             Status => #Status);

**Asynchronous execution**

The instruction "OPC_UA_WriteList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The example above shows case 4.

In the example program, this case only assigns one PLC tag a new value. In your application, you can assign new values to a large number of PLC tags.

The new value is set to TRUE, if the "#SetProductionEnabled" tag contains the value "TRUE".

"#SetProductionEnabled" is then set to FALSE as the initialization is only to be run once (in the first cycle).

The "OPC_UA_WriteList" instruction writes the new value to the PLC tag "ProductionEnabled" in the OPC UA server.

If the instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

IF #Done = TRUE THEN

    FOR #i := 0 TO UINT_TO_INT("Productionline_Configuration".WriteLists.WriteListStatus.NodeCount) - 1 DO

         IF NOT ("Productionline_Data"."WriteListStatus".NodeStatusList[#i] = 0) THEN

         #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at Writelist "WriteListStauts", Index: ',

         IN2 := INT_TO_WSTRING(#i));

         END_IF;

    END_FOR;

    #State := #State + 1;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #Mem_Status := #Status;

    #OPC_UA_WriteList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              Variable := "Productionline_Data"."WriteListStatus".Variable);

END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the "Error" output parameter is set to the value TRUE. This sets the "#State" tag to the value 100. This case is reserved for troubleshooting. The example program also calls the "OPC_UA_WriteList" instruction to set the REQ parameter to FALSE.

If the output parameter "Done" is TRUE, the instruction was executed successfully.

Note: It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but no PLC tag could be set.

Therefore, there is a check in the example for the PLC tag to determine whether the program was able to set a valid value:

- If the server was able to assign the new value to the first PLC tag, the first element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

  In the example, only one tag is used. Your status code is available in "Productionline_Data"."WriteListStatus".NodeStatusList[0]".

The program outputs an error message when a PLC tag could not be set.

The value of the "#State" tag is increased by 1. This means the next program section - case 5 - (Release Handle List) is executed in the next cycle.

---

**See also**

[OPC_UA_NodeId (S7-1500)](#opc_ua_nodeid-s7-1500)
  
[OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)
  
[OPC_UA_NodeReleaseHandleList: Release handles for read and write access (S7-1500)](#opc_ua_nodereleasehandlelist-release-handles-for-read-and-write-access-s7-1500)

##### Writing an array section with OPC_UA_WriteList (S7-1500)

###### Introduction

This section is based on "OPC_UA_WriteList"; see [OPC_UA_WriteList: Write tags](#opc_ua_writelist-write-tags-s7-1500).

The section describes how to assign new values to (write) a part of an array with the "OPC_UA_WriteList" instruction.

Writing to a part of an array of an OPC UA server basically works as follows:

![Introduction](images/110908859275_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Writing array elements to a part of an array of an OPC UA server |

###### Requirements

The following description assumes that:

- You have configured a CPU as **OPC UA server**.

  The server provides an array that can be written by OPC UA clients.

  In the example, you use the CPU "Productionline", which provides the data block "Data_from_OPC_UA_Clients" for OPC UA clients:

  ![Requirements](images/110600110475_DV_resource.Stream@PNG-de-DE.png)
- You have configured a CPU as **OPC UA client**.

  You have created a client interface in the client, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".

  The client interface contains a write list with an array.

  Only a part of this array is to be used for writing the array on the server.

  The example uses the client interface "Productionline" with the write list "WriteListStatus":

  ![Requirements](images/110515732875_DV_resource.Stream@PNG-de-DE.png)

  In the "Serial_Number" array of the server, new values are to be written to "Serial_Number[5]" to "Serial_Number[9]".

###### Adapting write list data type and write list DB

"OPC_UA_WriteList" shows how to write new values to entire scalars (tags with a value) and arrays (tags with multiple values) using the "OPC_UA_WriteList" instruction.

The following section provides additional details to "OPC_UA_WriteList" that are required for using OPC_UA_WriteList to write new values to part of an array.

**Step 1: Copying and adjusting write list data type**

First, you change the data type of the tag that provides the values that you are writing to the OPC UA server.

This change is required because the data type generated by STEP 7 is too long.

The data type is too long because you only want to assign new values to part of the array (and not to the entire array).

In the example, you access the array "Serial_Number", which contains ten elements.

STEP 7 therefore generates a data type with ten elements.

Proceed as follows to shorten this data type:

1. Open the "PLC data types" folder in the "Project tree".
2. Open the "System data types" folder.
3. Copy the data type "<client interface>.<write list>".

   In the example, the data type is named ""Productionline.WriteListStatus".
4. Paste the copied data type to the "PLC data types" folder.
5. Change the name of the data type inserted so that it is meaningful in your project.

   In the example, we are changing the name to "myUDTProductionline.WriteListStatus".
6. Change the data type of the array.

   In the example, we want to write the values from Serial_Number[5] to Serial_Number[9] to the OPC UA server.

   We therefore shorten the data type from "Array[0..9] of Lint" to "Array[0..4] of Lintl".

   In the example:

   ![Adapting write list data type and write list DB](images/110591956747_DV_resource.Stream@PNG-de-DE.png)

**Step 2: Copy write list DB and apply new write list data type to it**

In this step, you use the new data type in a new data block.

This step is required because the data block generated by STEP 7 contains the original data type for the array.

It is not possible to change the data type: Each time the data block is compiled, the original data type is restored. The changes are lost.

Proceed as follows to create a new data block:

1. In the "Project tree" area, select the CPU that acts as the client.
2. Open the "Program blocks" folder
3. Copy the data type <client interface>_Data

   In the example, the data block is named "Productionline_Data"
4. Paste the copied data block to the "Program blocks" folder.
5. Change the name of the data block inserted so that it is meaningful in your project.

   In the example, we change the name to "myProductionline_Data"
6. Now use the new data type that we created in Step 1.

   In the example, we assign the new data type to the tag "Variable" in the write list "WriteListStatus":

   ![Adapting write list data type and write list DB](images/110591965579_DV_resource.Stream@PNG-de-DE.png)
7. Supply the "Tag" parameter of the instruction "OPC_UA_WriteList" with the new data block (in the example "myProductionline_Data").

   `Variable := "myProductionline_Data"."WriteListStatus".Variable,`

**Step 3: Create tag for OPC_UA_ReadList parameter "NodeAddInfos"**

In this step, you create a local tag of the type "OPC_UA_NodeAdditionalInfo".

This tag is used to tell the "OPC_UA_WriteList" instruction which part of the array is to be assigned new values.

Proceed as follows:

1. Create an array tag of the type "OPC_UA_NodeAdditionalInfo".

   In the example, you create the tag in the declaration section of the function block that calls the instruction "OPC_UA_WriteList".

   You name the new local tag "NodeAdditionalInformation":

   ![Adapting write list data type and write list DB](images/110600166795_DV_resource.Stream@PNG-de-DE.png)

   The new local tag "NodeAdditionalInformation" contains two elements of the type "OPC_UA_AdditonalInfo".

   NodeAdditionalInformation[0] provides additional information on the first tag to be written (in the example, "ProductionEnabled")

   NodeAdditionalInformation[1] provides additional information on the second tag to be written (in the example, "Serial_Number")
2. Assign values to the new tag (in the "Default values" column of the declaration section).

   In the example you do not write all elements of the second tag (Serial_Number).

   You therefore assign NodeAdditionalInformation[1].AttributeId the value of 13 (which means the values of the array are written).

   NodeAdditionalInformation[1].StartIndex is assigned the value of 5, as you are writing from (and including) index 5.

   NodeAdditionalInformation[1].EndIndex is assigned the value of 9, as you are writing from (and including) index 9.

   You set the following values for NodeAdditionalInformation[0] which signal to the server that the first element of the write list is not a part of an array but a scalar or an array that is to be written completely.

   The constant "#ignore" contains the value 4_294_967_295. The server ignores this value for StartIndex and EndIndex and writes scalars and arrays completely.

   ![Adapting write list data type and write list DB](images/110724816267_DV_resource.Stream@PNG-de-DE.png)

   Alternative:

   You can also set the values for NodeAdditionalInformation in the user program:

   `// set additonal information to Array-Index 0`

   `// we set default values here`

   `#NodeAdditonalInformation[0].AttributeID := 13;`

   `#NodeAdditonalInformation[0].StartIndex := 4_294_967_295;`

   `#NodeAdditonalInformation[0].EndIndex := 4_294_967_295;`

   `// set additonal information to Array-Index 1`

   `// because we want to write only five values to the array in the OPC UA server`

   `#NodeAdditonalInformation[1].AttributeID := 13;`

   `#NodeAdditonalInformation[1].StartIndex := 5;`

   `#NodeAdditonalInformation[1].EndIndex := 9;`

   Note:

   The array NodeAdditionalInformation of the type "OPC_UA_NodeAdditionalInfo" must contain as many elements as the write list (2 in the example).
3. Assign the local tag NodeAdditionalInformation to the "NodeAddInfos" parameter of the "OPC_UA_WriteList" instruction.

   The following figure shows the call of OPC_UA_WriteList with the new supply of the parameters "Variable" and "NodeAddInfos":

   `#OPC_UA_WriteList_Instance(REQ := #Req,`

   `NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,`

   `NodeStatusList := "myProductionline_Data"."WriteListStatus".NodeStatusList,`

   `Variable := "myProductionline_Data"."WriteListStatus".Variable,`

   `ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,`

   `Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,`

   `NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,`

   `NodeAddInfos := #NodeAdditonalInformation,`

   `Busy => #Busy,`

   `Error => #Error,`

   `Status => #Status,`

   `Done => #Done);`

###### Result in the server

The "OP_UA_WriteList" instruction now writes only part of the "Serial_Number" array to the OPC UA server.

The figure below shows the array "Serial_Number". The server assigns the written values as of the index that you specify with NodeAdditionalInformation (as of index 5 in the example):

![Result in the server](images/110723324043_DV_resource.Stream@PNG-de-DE.png)

###### Note

Use the data type "OPC_UA_NodeAdditionalInfoExt" to write to a section of a multi-dimensional array (up to six dimensions).

##### Set OPC UA-DataValue with OPC_UA_WriteList (S7-1500)

###### Validity

The following description is valid for S7-1500 CPUs as of firmware version V3.0.

###### Requirements

- You have activated the OPC UA server on your S7-1500 CPU.

> **Note**
>
> **Set OPC UA-DataValue with OPC_UA_WriteList**
>
> The instruction "OPC_UA_WriteList" belongs to the OPC UA client instructions. However, if you use it to set one or more OPC UA-DataValues on the OPC UA server of the local CPU, it works independently of any client functionality. This means that there is no handling of connections and the OPC UA client on your CPU does not have to be activated. If you have activated it, the call of "OPC_UA_WriteList" used in this way is not part of the client program.

###### Description

You may also use the instruction "OPC_UA_WriteList" under the above-mentioned conditions to consistently overwrite the value and the associated additional information of one or more OPC UA tag nodes on the OPC UA server of the local CPU (localhost connection).

For reasons of consistency, the tags nodes whose values are to be set locally must not be set by a remote OPC UA client. Therefore, the "AccessLevel" or "UserAccessLevel" attributes of the affected tag nodes must not have the "CurrentWrite" component.

The value including the associated additional information is referred to here as OPC UA-DataValue.

The additional information is StatusCode, SourceTimestamp and SourcePicoseconds.

Only the data values of nodes from user-defined server interfaces can be set. The nodes must not have any mapping to local data. Constants are overwritten.

###### Difference to the previous use of OPC_UA_WriteList

For S7-1500 CPUs with firmware version < V3.0, the instruction "OPC_UA_WriteList" can only be used to write PLC tags of a remote OPC UA server. To do this, other instructions must be called beforehand, including those to establish a connection. In addition, further instructions must be called after the write operation to release resources again.

These preparations and post-processing are not necessary if you use the instruction "OPC_UA_WriteList" to set one or more OPC UA-DataValues on the OPC UA server of the local CPU. In this case, "OPC_UA_WriteList" works completely independently.

When using "OPC_UA_WriteList" to set OPC UA-DataValues on the OPC UA server of the local CPU, some parameters have a different meaning than when writing PLC tags of a remote OPC UA server. This is especially true for the "ConnectionHdl" parameter. With it you define how you want to use the instruction.

The changed meaning of the parameters is explained in detail in the parameter table.

###### Functional description

The "OPC_UA_WriteList" instruction works asynchronously. Processing extends over multiple calls. You start processing with a rising edge at the "Req" parameter.

The parameters "Busy" and "Done" indicate the status of the job.

If an error occurs during execution, this is signaled by the parameters "Error" and "Status".

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Parameters

The following table shows the parameters of the instruction "OPC_UA_WriteList" if you want to use it to set one or more OPC UA-DataValues on the OPC UA server of the local CPU.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Req | Input | Bool | Control parameter Request  Activates the job on a positive edge. |
| ConnectionHdl | Input | DWord | Note: This parameter has a different meaning than when writing PLC tags of a remote OPC UA server.  Decimal value -42 (16#FFFFFFD6)  This value causes "OPC_UA_WriteList" to set OPC UA-DataValues on the OPC UA server of the local CPU. |
| NodeHdlCount | Input | UINT | Number of elements in the array pointed to by the "NodeHdls" parameter. |
| NodeHdls | InOut | Variant | Note: This parameter has a different meaning than when writing PLC tags of a remote OPC UA server.  Pointer to an array with elements of the OPC_UA_NodeId type.  The array contains the node IDs of the OPC UA tags whose values and additional information are to be set. These are located under the local server interfaces. |
| NoteAddInfos | InOut | Variant | Note: This parameter has a different meaning than when writing PLC tags of a remote OPC UA server.  This parameter is not supported. It must be ZERO or you do not interconnect it. |
| Timeout | Input | Time | Note: This parameter has a different meaning than when writing PLC tags of a remote OPC UA server.  This parameter is not evaluated. |
| Done | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still being processed. - 1: Job completed without error. This state is only displayed for one call. |
| Busy | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started. |
| Error | Output | Bool | Status parameter  - 0: No error occurred. - 1: Error occurred during processing.   The "Status" parameter provides detailed information on the type of error. This state is only displayed for one call. |
| Status | Output | DWord | Return value or error information of the "OPC_UA_WriteList" instruction, see below. |
| NodeStatusList | InOut | Variant | Pointer to an array with elements of the DWord type.  The array contains the error codes for the individual OPC UA-DataValues, see below.  Each element indicates whether the OPC UA-DataValue could be set successfully for the associated NodeId. NodeStatusList is valid only if Done is 1. Array elements whose index is >= NodeHdlCount are invalid. |
| Tag | InOut | Variant | Note: This parameter has a different meaning than when writing PLC tags of a remote OPC UA server.  Pointer to a structure or PLC data type (UDT) or to an array of a structure or a PLC data type (UDT). The pointer points to the OPC UA-DataValues to be written.  The rules applicable to the OPC UA-DataValues are described below. |

You can find more information on valid data types under [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

###### Rules for the OPC UA-DataValues

The OPC UA-DataValues must comply with the following rules:

- Each OPC UA-DataValue is a structure or PLC data type (UDT) and consists of two, three or four elements.
- The first element always corresponds to the value of the OPC UA tags, addressed by their node ID of the user-defined server interface. The data type of the first element can be any valid data type. The "Union" data type is not supported.  
  See [Data types for companion specifications](Configuring%20automation%20systems.md#data-types-for-companion-specifications-s7-1500-s7-1500t)
- The elements two to four stand for the additional information StatusCode, SourceTimestamp and SourcePicoseconds. Their order is arbitrary.

  Only the data types DWORD, UINT and LDT (DATE_AND_LTIME) are permitted. Each data type may only be present once.

  Which element corresponds to which metadata is determined by the data type:

  - An element of data type DWORD is interpreted as a status code.

    If it does not exist or has the value 0, this is interpreted as the status code "Good".

    If you preset the status code "Bad" (bit 31 set), the firmware of the CPU sets the value to ZERO.
  - An element of the LDT data type (DATE_AND_LTIME) is interpreted as SourceTimestamp.

    If it does not exist or the value has LDT#1970-01-01-00:00:00.000000000 (preset value), it is set to the current system time by the firmware of the CPU.
  - An element of the UINT data type is interpreted as SourcePicoseconds.

    If the element does not exist, it is interpreted as 0.

    The numerical value of the element is not checked by the firmware of the CPU, which means you are responsible for its default setting.

###### "Status" parameter

When the "Error" parameter has the value 1, you can use the "Status" parameter to determine the cause of the error that occurred.

The following table contains the possible error codes.

| Error code (16#...) | Name of the error | Explanation |
| --- | --- | --- |
| 8003_0000 | OpcUa_BadOutOfMemory | The memory allocation during the preparation of the call was not successful. This may have several sporadic causes. |
| 8010_0000 | OpcUa_BadTooManyOperations | The number of "OPC_UA_WriteList" instructions that can be called simultaneously per connection has been exceeded (max. 5). |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for the "NodeHdls" parameter |
| B080_0200 | Simatic_BadType_VariantInput2 | A value has been assigned to the "NoteAddInfos" parameter. |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for the "NodeStatusList" parameter |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for the "Tag" parameter |
| B080_1100 | Simatic_ArrayElements_TooMany | NodeHdlCount > MAX_ELEMENTS_NODELIST (300) |
| B080_C300 | Simatic_InsufficientResources | The OPC UA server cannot be reached, for example, due to insufficient memory space. |
| B080_C500 | Simatic_NothingToDo | NodeHdlCount has the value 0. |
| B080_C700 | Simatic_ServerNotEnabled | The OPC UA server is not activated. |
| B080_C800 | Simatic_ServerNotAvailable | The OPC UA server is activated but not yet available. |
| B080_C900 | Simatic_ServerNotInitialized | The OPC UA server is activated and available but not yet initialized. |

###### "NodeStatusList" parameter

Each element in the "NodeStatusList" parameter indicates whether the data value for the associated NodeId could be set successfully.

The following table explains the error codes.

| Error code (16#...) | Name of the error | Explanation |
| --- | --- | --- |
| 8003_0000 | OpcUa_BadOutOfMemory | The memory allocation during the preparation of the call was not successful. This may have several sporadic causes. |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The OPC_UA_NodeId points to a node that does not exist with this NamespaceIndex in the address space of the server. |
| 803B_0000 | OpcUa_BadNotWritable | The OPC_UA_NodeId points to a ServerInterface node that is defined with the property "writable for an OPC UA client". |
| 803D_0000 | OpcUa_BadNotSupported | The OPC UA DataValue for this NodeId cannot be changed. Possible causes:  - The OPC_UA_NodeId refers to a ServerInterface node that is assigned to a PLC tag. - The OPC_UA_NodeId is part of namespace 3 (standard SIMATIC server interface) - The OPC_UA_NodeId is part of namespace 0. - The OPC_UA_NodeId does not correspond to a ServerInterface node or is not a tag. |
| 803E_0000 | OpcUa_BadNotFound | The NamespaceIndex in the OPC_UA_NodeId could not be resolved. |
| 8074_0000 | OpcUa_BadTypeMismatch | The data type of the element "Value" in the provided OPC UA-DataValue does not match the data type of the associated node. |
| B080_2400 | BadValue_VariantInput4 | The definition of the OPC UA DataValue in the corresponding element of the "Tag" parameter is incorrect. It does not satisfy the rules for OPC UA DataValues described above. |

###### Good-Overload Scenario

An OPC UA server can transmit the status code "GoodOverload" when using subscriptions if an overload of the CPU occurs while sampling the items. See [Subscription diagnostics](Configuring%20automation%20systems.md#subscription-diagnostics-s7-1500-s7-1500t)

If the OPC UA server of the local CPU uses subscriptions, you must consider this when setting OPC UA-DataValues by means of OPC_UA_WriteList.

If you have set a status code with the property "Severity = Good" with OPC_UA_WriteList, it will always be overwritten by the status code "GoodOverload". After the end of the CPU overload, the status code applies the last value that you set with OPC_UA_WriteList. A status code with the property "Severity = Bad" or "Severity = Uncertain" is not changed by "GoodOverload".

Bits 14 "SemanticsChanged" and 15 "StructureChanged" are set in case of "GoodOverload". Likewise, the overflow bit can be set on "GoodOverload".

###### More information

An application example provides additional support on the topic "Set OPC UA-DataValues on the OPC UA server of the local CPU": [Setting OPC UA DataValue attributes](https://support.industry.siemens.com/cs/ww/en/view/109820694)

---

**See also**

[Client accesses and local accesses to the OPC UA server (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#client-accesses-and-local-accesses-to-the-opc-ua-server-s7-1500-s7-1500t)

#### Ending data exchange (S7-1500)

This section contains information on the following topics:

- [OPC_UA_NodeReleaseHandleList: Release handles for read and write access (S7-1500)](#opc_ua_nodereleasehandlelist-release-handles-for-read-and-write-access-s7-1500)
- [OPC_UA_Disconnect: Close the connection (S7-1500)](#opc_ua_disconnect-close-the-connection-s7-1500)

##### OPC_UA_NodeReleaseHandleList: Release handles for read and write access (S7-1500)

###### Validity

The following description of the "OPC_UA_NodeReleaseHandleList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_NodeReleaseHandleList" to release handles.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112216944267_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_NodeReleaseHandleList" is used to release handles for PLC tags that were previously registered with the instruction "OPC_UA_NodeGetHandleList", see ③ in the figure below.

The instruction "OPC_UA_NodeReleaseHandleList" is not required when you want to disconnect the connection to the OPC UA server. In this case, call the "[OPC_UA_Disconnect: Close the connection](#opc_ua_disconnect-close-the-connection-s7-1500)" instruction immediately. This instruction automatically releases all handles.

![Description](images/103731602827_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_NodeReleaseHandleList"

The parameters of the function block "OPC_UA_NodeReleaseHandleList"

| Parameters | Declaration in area | S7 data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the block. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established: Connection handle.  You get the connection handle by calling the function block OPC_UA_Connect. |
| NodeHdlCount | Input | UINT | Number of elements in the NodeHdls parameter |
| NodeHdls | InOut | VARIANT | Pointer to an array of the type DWORD.   The array contains the handles for the tags that you no longer want to read or set in your program. |
| Timeout | Input | TIME | Maximum time for execution of the function block.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeStatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error codes for the individual node handles (tags); see "Error numbers in the NodeStatusList parameter".  For each node handle, you can see whether or not it could be released. |
| Done | Output | BOOL | Status parameter for block processing  - **0**: Block processing aborted, not yet completed or not yet started - **1**: Block processing completed without errors |
| Busy | Output | BOOL | Status parameter for block processing  - **0**: Block not being executed - **1**: Block currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | see "Error numbers in the Status parameter" below |

###### Error numbers for Status

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Function block executed successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_NodeReleaseHandleList" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 80AE_0000 | BadConnectionClosed | The connection with the corresponding ConnectionHdl is in "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout).  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and release the connection resources again. In your user program, you must reset the ConnectionHdl that has become invalid for this connection.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect"). |
| 80AF_0000 | BadInvalidState | The connection with the corresponding ConnectionHdl is has the "ConnectinError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed in the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU could reach the OPC UA server to check whether or not the session is still active. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "NodeHdls". |
| B080_1100 | Simatic_ArrayElements_TooMany | NodeHdlCount > MAX_ELEMENTS_NODELIST |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "NodeStatusList". |
| B080_3100 | BadNumElements_VariantInput1 | NodeHdlCount > Number of array elements of the "NodeHdls" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | NodeHdlCount > Number of array elements of the "NodeStatusList" parameter. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see:  [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "NodeStatusList"

The "NodeStatusList" parameter contains an error code for each individual node handle (tag).

The following table explains the error codes:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Handle released successfully. |
| 8034_0000 | OpcUa_BadNodeUnknown | The node handle transferred is not known. |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_NodeReleaseHandleList" in a program that exchanges data with an OPC UA server.

###### Requirements

The following description assumes that:

- You have created a client interface.
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirements must be met for the instruction "OPC_UA_NodeReleaseHandleList":

- A handle for connection to an OPC UA server is available.

  You get the connection handle by calling the function block "[OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection)".
- A list of the handles for the individual tags whose values you no longer want to read or write in your program.

  You get this handle list by calling the function block "[OPC_UA_NodeGetHandleList: Get handles for read and write access](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500)".

###### Function of the instruction

You call the instruction "OPC_UA_NodeReleaseHandleList" to release node handles that you no longer require in your program.

Node handles are numeric references to nodes (for example PLC tags) on the OPC UA server.

**What information is required for the function block?**

The function block requires the following information:

- A list of the handles for the tags (or other nodes) whose values you no longer want to read or write (in the "NodeHdls" parameter).

**What information does the function block return?**

The function block returns the following information:

- A list of error messages (in the "NodeStatusList" parameter).

  Each error message in this list relates to the corresponding handle in the "NodeHdls" parameter.

  For each individual node handle, you need to check whether the OPC UA server was able to release it.

  If a node handle could not be released, you user program must catch this error: For example, call this instruction once again in a troubleshooting session.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU you want to use as a client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_NodeReleaseHandleList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_NodeReleaseHandleList_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_NodeReleaseHandleList_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline", which we created for our [Example configuration for OPC UA](Configuring%20automation%20systems.md#example-configuration-for-opc-ua-s7-1500-s7-1500t).
7. Click "Data access" and select a read list.

   In the example, the read list "ReadListProduct".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
8. Click on "Block parameters" and assign tags manually to the parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

You can find the complete program in the section "[Program example for reading PLC tags](#program-example-for-reading-plc-tags-s7-1500)".

The program example uses the read list "ReadListProduct", which contains the following PLC tags:

- NewProduct
- ProductNumber

The handles for these PLC tags are released by the following program example.

**CASE instruction**

The example program is divided into multiple sections (cases) by a CASE instruction.

Case 5 is shown here:

SCL

5:  // case 5, release node handles

            IF #Busy = FALSE THEN

                  #Req := TRUE;

            ELSE

                #Req := FALSE;

            END_IF;

            #OPC_UA_NodeReleaseHandleList_Instance(REQ := #Req,

                  ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                  NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                  NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                  Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                  NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                  Done => #Done,

                  Busy => #Busy,

                  Error => #Error,

                  Status => #Status);

**Asynchronous execution**

The instruction "OPC_UA_NodeReleaseHandleList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The figure above shows case 5.

This part of the program calls the instruction "OPC_UA_NodeReleaseHandleList". This releases handles for PLC tags. The tags are listed in the "ReadListProduct" read list.

If the instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

            IF #Done = TRUE THEN

                IF "Productionline_Data"."ReadListProduct".NodeStatusList[0] = 0 AND

                   "Productionline_Data"."ReadListProduct".NodeStatusList[1] = 0

                THEN

                    #State := #State + 1;

                ELSE

                    #State := 100;

                    //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

                    #Set_REQ_To_FALSE := TRUE;

                    #Mem_Status := #Status;

                    #Output_Error_Message := WString#'Error at NodeReleaseHandleList';

                END_IF;

            END_IF;

            IF #Error = TRUE THEN

                #State := 100;

                //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

                #Set_REQ_To_FALSE := TRUE;

                #Mem_Status := #Status;

                #OPC_UA_NodeReleaseHandleList_Instance(REQ := FALSE,

                      ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                      NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                      NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                      Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                      NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList);

            END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the "Error" output parameter is set to the value TRUE. This sets the #State tag to the value 100. This case is reserved for troubleshooting. The example program also calls the instruction "OPC_UA_NodeReleaseHandleList" to set the REQ parameter to FALSE.

If the TRUE value is in the "Done" output parameter, the instruction was successfully executed.

Note: It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but a handle could not be released for a PLC tag.

Therefore, there is a check in the example to determine whether the handles for both tags have been released:

- If the server releases the handle for the first PLC tag, the first element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

  In the example, the status code is available in "Productionline_Data"."ReadListProduct".NodeStatusList[0].
- If the server releases the handle for the second PLC tag, the second element of the array to which the "NodeStatusList" parameter is pointing contains the value 0.

  In the example, the status code is available in "Productionline_Data"."ReadListProduct".NodeStatusList[1].

If both conditions are met, the value of tag "#State" is increased by one. This means the next program section - case 6 (close connection) - is executed in the next cycle.

Case 6 is described in [OPC_UA_Disconnect: Close the connection](#opc_ua_disconnect-close-the-connection-s7-1500).

> **Note**
>
> Case 6 is for enabling the connection to the OPC UA server. This also releases all other resources that the client program has occupied in the server. If you want to terminate the connection to the server, your user program can execute case 6 immediately and skip case 5.

---

**See also**

[OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)
  
[OPC UA instructions for client programs (S7-1500)](#opc-ua-instructions-for-client-programs-s7-1500)
  
[Example programs for OPC UA clients (S7-1500)](#example-programs-for-opc-ua-clients-s7-1500)

##### OPC_UA_Disconnect: Close the connection (S7-1500)

###### Validity

Unless otherwise specified, the following description of the "OPC_UA_Disconnect" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_Disconnect" to disconnect the connection to a OPC UA server.

> **Note**
>
> **Handling of connection handles (ConnectionHdl) as of firmware version V2.8**
>
> As of firmware version V2.8, after a connection error (error code "BadConnectionClosed"), you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and thus release the connection resources again. You must reset the ConnectionHdl for this invalid connection in your user program.

The following figure shows the icon of the instruction in the editor (FBD).

![Description](images/112216947979_DV_resource.Stream@PNG-de-DE.png)

In the figure above, the parameters of the instruction are not supplied yet.

The instruction "OPC_UA_Disconnect" is used to disconnect the connection to an OPC UA server and terminate the session, see ③ in the figure below:

![Description](images/103731606539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for releasing resources after completed read or write operations |

###### Parameters for "OPC_UA_Disconnect"

The parameters of the function block "OPC_UA_Disconnect"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the block. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established: Connection handle.  You get the connection handle by calling the function block OPC_UA_Connect. |
| Timeout | Input | TIME | Maximum time for execution of the function block.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| Done | Output | BOOL | Status parameter for block processing  - **0**: Block processing aborted, not yet completed or not yet started - **1**: Block processing completed without errors    **Note**: Even if the processing of the "OPC_UA_Disconnect" instruction is finished with Done=1, the connection resource remains occupied for about 60 seconds, see [Details about OPC UA client/server connections](Configuring%20devices%20and%20networks.md#details-about-opc-ua-clientserver-connections-s7-1500). |
| Busy | Output | BOOL | Status parameter for block processing  - **0**: Block not being executed - **1**: Block currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | see "Error numbers in the Status parameter" below |

###### Error numbers in the Status parameter

The "Status" parameter provides information about errors that occurred during execution of the instruction.

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Function block executed successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_Disconnect" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C600 | Simatic_ClientNotAvailable | Error during initialization of the client |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### This is how you use this instruction

Based on a program example, this section shows you how to use the instruction "OPC_UA_Disconnect" in a program that exchanges data with an OPC UA server.

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirement must be met for the instruction "OPC_UA_Disconnect":

- A handle for connection to an OPC UA server is available.

  You get the connection handle by calling the instruction, see [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).

###### Function of the instruction

You call the instruction "OPC_UA_Disconnect" to disconnect the connection to an OPC UA server.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU you want to use as a client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "ReadFromProductionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_Disconnect" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_Disconnect_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_Disconnect_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline", which was created for the [Example configuration for OPC UA](Configuring%20automation%20systems.md#example-configuration-for-opc-ua-s7-1500-s7-1500t), see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".

   STEP 7 now automatically supplies the parameters of the instruction with the values you have configured for the client interface.
7. Click on "Block parameters" and assign tags manually to the remaining parameters REQ, Busy, Done, Error, Status.

   STEP 7 adds the selected tag to the call of the instruction.

###### Calling the instruction

You can find the complete program in the section "[Program example for reading PLC tags](#program-example-for-reading-plc-tags-s7-1500)".

The example program terminates the connection to an OPC UA server and the session:

SCL

6: // case 6, disconnect from server

            IF #Busy = FALSE THEN

                  #Req := TRUE;

            ELSE

                  #Req := FALSE;

            END_IF;

            #OPC_UA_Disconnect_Instance(REQ := #Req,

                  ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                  Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                  Done => #Done,

                  Busy => #Busy,

                  Error => #Error,

                  Status => #Status);

The example program calls the "OPC_UA_Disconnect" instruction for the following reasons:

- To terminate the connection to the OPC UA server.
- To set the REQ parameter to FALSE, if an error has occurred.

**Asynchronous execution**

The instruction "OPC_UA_Disconnect" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction

The figure above shows case 6. This part of the program terminates the connection to the connected OPC UA server and the session.

If the #State tag is 6, then case 6 is executed.

If the "OPC_UA_Disconnect" instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

If the output parameter "Done" is TRUE, the handle for the connection could be released and the connection could be terminated. This increases the value of the "#State" tag by one. This means the next program section - case 7 - is executed in the next cycle. This case sets the status information for the function block (Output_Busy = FALSE, Output_Done = TRUE).

If the instruction cannot be executed without errors, the output parameter "Error" is TRUE and the tag #State gets the value 100. This case is reserved for troubleshooting.

#### Diagnostics (S7-1500)

This section contains information on the following topics:

- [OPC_UA_ConnectionGetStatus: Read connection status (S7-1500)](#opc_ua_connectiongetstatus-read-connection-status-s7-1500)
- [Diagnosing the OPC UA server with OPC_UA_ReadList (S7-1500)](#diagnosing-the-opc-ua-server-with-opc_ua_readlist-s7-1500)

##### OPC_UA_ConnectionGetStatus: Read connection status (S7-1500)

###### Validity

Unless otherwise specified, the following description of the "OPC_UA_ConnectionGetStatus" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_ConnectionGetStatus" to monitor a connection, i.e. to get information about the quality of the connection to an OPC UA server.

The instruction returns the following information:

- Status of the connection
- Status and service level of the connected OPC UA server

  (Node identifier of status: i=2259, node identifier of ServiceLevel: i=2267)

![Description](images/103604109835_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of read and write operations |
| ② | Read and write instructions |
| ③ | Instructions for "clean-up" after a completed read or write operation |

###### Parameters for "OPC_UA_ConnectionGetStatus"

The parameters of the function block "OPC_UA_ConnectionGetStatus"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |
| ConnectionStatus | Output | UDINT | Status of the connection that is identified by the ConnectionHdl parameter.  Valid when Done=1.  Meaning:  - **0**: Connection to the OPC UA server has been established. - **1**: Incorrect connection to the OPC UA server ("ConnectionError"). In this state, the CPU tries to "reactivate" the connection. - **2**: The connection to the OPC UA server could not be reactivated. The CPU has disconnected from the server ("ShutDown"). You have to close the connection (OPC_UA_Disconnect) and then establish a new connection to the OPC UA server (OPC_UA_Connect). |
| ServerState | Output | UDINT | Information about the OPC UA server. Valid when Done=1 and ConnectionStatus=0  Meaning of the values:  - **0**: The server is running normally. - **1**: An error has occurred in the server. The server is no longer operating reliably. - **2**: The server is running. However, no configuration has been loaded and data is therefore not being exchanged. - **3**: The server is temporarily unavailable. - **4**: The server has been or is in the process of being shut down. - **5**: The server is running in test mode. Outputs are not interconnected. - **6**: The server is running normally. However, there are problems with reading the PLC tags. - **7**: Server status is not known.   This value is set if there is no connection to the server. |
| ServiceLevel | Output | Byte | Information on the power of the connected OPC UA server. Valid when Done=1 and ConnectionStatus=0.  The server returns a number between 0 and 255 to indicate its power: The higher the number, the more powerful the server. |

###### Error numbers for Status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table shows a summary of error codes for this instruction:

| Error code   (hexadecimal values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | The server sends an unknown or invalid response. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_ConnectionGetStatus" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 8074_0000 | OpcUa_BadTypeMismatch | ServerState / ServiceLevel have unexpected type. |
| A000_0105 | PLCopenUA_Bad_ConnectionInvalidHdl | The connection handle (ConnectionHdl) is invalid / unknown. You need to establish a new connection. When a connection is released with the "OPC_UA_Disconnect" instruction, the Connection Handle for this connection also becomes invalid. **Note**: For S7-1500 CPUs as of firmware version V2.8, the connection handle is **only** released or invalid when the OPC_UA_Disconnect instruction is called. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Requirement

The following requirement must be met for the instruction "OPC_UA_ConnectionGetStatus":

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).

###### Calling the instruction

This section describes the function block "Analyze_Connection". The function block shows you how to use the instruction "OPC_UA_ConnectionGetStatus".

You can find the complete example in the section "[Example program for OPC_UA_ConnectionGetStatus](#example-program-for-opc_ua_connectiongetstatus-s7-1500)".

**Declaration of tags**

Declare an instance of the instruction "OPC_UA_ConnectionGetStatus" and the tags with which you are supplying the instruction parameters.

The program example uses the following declaration:

![Calling the instruction](images/103604118411_DV_resource.Stream@PNG-de-DE.png)

**User program**

The figure below shows the section from the example program "Analyze_Connection" that determines the quality of the connection to the server.

The example program is divided into multiple sections (cases) by a CASE instruction.

Case 2 (analysis of the connection) is shown here:

SCL

2: // case 2, analyse connection

    IF #Busy = FALSE THEN

            #Req := TRUE;

    ELSE

            #Req := FALSE;

    END_IF;

    #OPC_UA_ConnectionGetStatus_Instance(REQ := #Req,

                  ConnectionHdl := #ConnectionHdl,

                  Timeout := T#6S,

                  Done => #Done,

                  Error => #Error,

                  Busy => #Busy,

                  Status => #Status,

                  ConnectionStatus => #ConnectionStatus,

                  ServerState => #ServerState,

                  ServiceLevel => #ServiceLevel);

    IF #Done = TRUE THEN

            #State := #State + 1;

    END_IF;

    IF #Error = TRUE THEN

            #State := 100;

            #Mem_Status := #Status;

            #OPC_UA_ConnectionGetStatus_Instance(REQ := FALSE, ConnectionHdl := #ConnectionHdl);

    END_IF;

If an error occurs, the instruction "OPC_UA_ConnectionGetStatus" (#Error has the value "TRUE"), the parameter REQ is set to the value FALSE.

**Asynchronous execution**

The instruction "OPC_UA_ConnectionGetStatus" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction

The figure above shows case 2 of the example program "Analyze_Connection".

This part of the program requests the current values for "ConnectionStatus", "ServerState" and "ServiceLevel" from the connected OPC UA server, which are not evaluated further however.

If the #State tag is 2, then case 2 is executed.

If the "OPC_UA_ConnectionGetStatus" instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

If the output parameter "Error" is TRUE, an error occurred during execution of the instruction. This sets the "#State" tag to the value 100. This case is reserved for troubleshooting.

If the output parameter "Done" is TRUE, the instruction was executed successfully. This increases the value of the "#State" tag by one. This means the next program section - case 3 - is executed in the next cycle. Case 3 is described in [OPC_UA_Disconnect: Close the connection](#opc_ua_disconnect-close-the-connection-s7-1500).

---

**See also**

[Using the S7-1500 CPU as an OPC UA client (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#using-the-s7-1500-cpu-as-an-opc-ua-client-s7-1500-s7-1500t)

##### Diagnosing the OPC UA server with OPC_UA_ReadList (S7-1500)

###### Validity

The following description is valid for S7-1500 CPUs as of firmware version V3.0.

###### Requirements

- You have activated the OPC UA server on your S7-1500 CPU.

> **Note**
>
> **Diagnosing the OPC UA server with OPC_UA_ReadList**
>
> The "OPC_UA_ReadList" instruction belongs to the OPC UA client instructions. However, if you use it to run diagnostics on the OPC UA server of the local CPU, it works independently of any client functionality. This means that there is no handling of connections and the OPC UA client on your CPU does not have to be activated. If you have activated it, the call of "OPC_UA_ReadList" used this way is not part of the client program.

###### Description

You may use the "OPC_UA_ReadList" instruction under the above mentioned conditions to read tag nodes of the server address space of the OPC UA server of the local CPU (localhost connection). You can thereby access those nodes that are available when the standard SIMATIC server interface is deactivated.

Your program has the same access rights as a remote OPC UA client with guest authentication (anonymous user) and security policy "None". This means, for example, that the SessionSecurityDiagnosticsArray cannot be read by your user program.

###### Difference to the previous use of OPC_UA_ReadList

For S7-1500 CPUs with firmware version < V3.0, the "OPC_UA_ReadList" instruction can only be used to read PLC tags of a remote OPC UA server. To do this, other instructions must be called beforehand, including those to establish a connection. In addition, further instructions must be called after the read operation in order to release resources again.

These pre-processing and post-processing steps are not required if you use the instruction "OPC_UA_ReadList" to diagnose the OPC UA server of the local CPU. In this case, "OPC_UA_ReadList" works completely independent.

When using "OPC_UA_ReadList" to run diagnostics on the OPC UA server of the local CPU, some parameters have a different meaning than when reading PLC tags of a remote OPC UA server. This is especially true for the "ConnectionHdl" parameter. With it you define how you want to use the instruction.

The changed meaning of the parameters is explained in detail in the parameter table.

###### Functional description

The "OPC_UA_ReadList" instruction is an asynchronous working instruction. Processing extends over multiple calls. You start processing with a rising edge at the "Req" parameter.

The parameters "Busy" and "Done" indicate the status of the job.

If an error occurs during execution, this is signaled by the parameters "Error" and "Status".

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

###### Parameters

The following table shows the parameters of the "OPC_UA_ReadList" instruction if you want to use it to run diagnostics on the OPC UA server of the local CPU.

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| Req | Input | Bool | Control parameter Request  Activates the job on a positive edge. |
| ConnectionHdl | Input | DWord | Note: This parameter has a different meaning than when reading PLC tags of a remote OPC UA server.  Decimal value -42 (16#FFFFFFD6)  This value causes "OPC_UA_ReadList" to read nodes on the OPC UA server of the local CPU. |
| NodeHdlCount | Input | UINT | Number of elements in the array pointed to by the "NodeHdls" parameter. |
| NodeHdls | InOut | Variant | Note: This parameter has a different meaning than when reading PLC tags of a remote OPC UA server.  Pointer to an array with elements of the OPC_UA_NodeId type, see [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500)  The array contains the nodes of the local server interfaces.  All nodes can be read that are available when the standard SIMATIC server interface is deactivated. |
| NodeAddInfos | InOut | Variant | Pointer to an array of the type [OPC_UA_NodeAdditionalInfo](#opc_ua_nodeadditionalinfo-s7-1500) or [OPC_UA_NodeAdditionalInfoExt](#opc_ua_nodeadditionalinfoext-s7-1500)  The array defines which attribute is to be read in the node (in a tag).  The first element of this array refers to the first element in the array pointed to by the "NodeHdls" parameter.  The parameter is optional. If it is not set, the values of all nodes (tags) are read.  When reading arrays, it is possible to restrict the elements of the array to be read, see Read array area with [Reading array range information with OPC_UA_ReadList](#reading-array-range-information-with-opc_ua_readlist-s7-1500). |
| Timeout | Input | Time | Note: This parameter has a different meaning than when reading PLC tags of a remote OPC UA server.  This parameter is not evaluated. |
| Done | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still being processed. - 1: Job completed without error. This state is only displayed for one call. |
| Busy | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started. |
| Error | Output | Bool | Status parameter  - 0: No error occurred. - 1: Error occurred during processing.   The "Status" parameter provides detailed information on the type of error. This state is only displayed for one call. |
| Status | Output | DWord | Return value or error information of the "OPC_UA_ReadList" instruction, see below. |
| NodeStatusList | InOut | Variant | Pointer to an array of the type DWORD.  The array contains the error codes for the individual tags (see below "Error numbers for NodeStatusList").  For each tag, it is specified whether its value could be read.  It may happen that the instruction was successfully executed ("Error" parameter not set), but no value could be read for a particular NodeId (tag). |
| TimeStamps | InOut | Variant | Pointer to an array of the type LDT.  The first element of this array refers to the first element of the array to which the "NodeHdls" parameter points.  The parameter is optional. If it is missing, the OPC UA server does not provide a time stamp. |
| Variable | InOut | Variant | Pointer to a structure or PLC data type (UDT).  The pointer points to the target area (for the read values). |

You can find additional information on valid data types under [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

###### "Status" parameter

When the "Error" parameter has the value 1, you can use the "Status" parameter to determine the cause of the error that occurred.

The following table contains the possible error codes.

| Error code (16#...) | Name of the error | Explanation |
| --- | --- | --- |
| 8003_0000 | OpcUa_BadOutOfMemory | The memory allocation during the preparation of the call was not successful. This may have several sporadic causes. |
| B080_0100 | Simatic_BadType_VariantInput1 | The value assigned to the NodeHdls parameter points to an element of wrong type. NodeHdls must be a pointer to an array with elements of the OPC_UA_NodeId type. |
| B080_0200 | Simatic_BadType_VariantInput2 | The value assigned to the NodeAddInfos parameter points to an element of wrong type. NodeAddInfos must be a pointer to an array of type OPC_UA_NodeAdditionalInfo or OPC_UA_NodeAdditionalInfoExt. |
| B080_0300 | Simatic_BadType_VariantInput3 | The value assigned to the NodeStatusList parameter points to an element of wrong type. NodeStatusList must be a pointer to an array of the DWORD type. |
| B080_0400 | Simatic_BadType_VariantInput4 | The value assigned to the TimeStamps parameter points to an element of wrong type. TimeStamps must be a pointer to an array of the LDT type. |
| B080_0500 | Simatic_BadType_VariantInput5 | The value assigned to the Tag parameter points to an element of wrong type. Tag must be a pointer to a structure or a PLC data type (UDT). |
| B080_1100 | Simatic_ArrayElements_TooMany | NodeHdlCount > MAX_ELEMENTS_NODELIST (300) |
| B080_3100 | BadNumElements_VariantInput1 | The value of NodeHdlCount is greater than the size of the array pointed to by NodeHdls. |
| B080_3200 | BadNumElements_VariantInput2 | The value of NodeHdlCount is greater than the size of the array pointed to by NodeAddInfos. |
| B080_3300 | BadNumElements_VariantInput3 | The value of NodeHdlCount is greater than the size of the array pointed to by NodeStatusList. |
| B080_3400 | BadNumElements_VariantInput4 | The value of NodeHdlCount is greater than the size of the array pointed to by TimeStamps. |
| B080_3500 | BadNumElements_VariantInput5 | The value of NodeHdlCount is greater or less than the number of value elements pointed to by the "Tag" parameter. |
| B080_C300 | Simatic_InsufficientResources | The OPC UA server cannot be reached, for example, because there is not enough memory. |
| B080_C500 | Simatic_SimaticNothingToDo | NodeHdlCount has the value 0. |
| B080_C700 | Simatic_ServerNotEnabled | The OPC UA server is not activated. |
| B080_C800 | Simatic_ServerNotAvailable | The OPC UA server is activated but not yet available. |
| B080_C900 | Simatic_ServerNotInitialized | The OPC UA server is activated and available but not yet initialized. |

###### "NodeStatusList" parameter

Each element in the "NodeStatusList" parameter indicates whether the value for the associated NodeId in NodeHDls could be successfully read. NodeStatusList is only valid if "Done" has the value TRUE. Elements whose index is >= NodeHdlCount are ignored and are invalid.

> **Note**
>
> **NodeStatusList**
>
> It is strongly recommended to always use and evaluate the "NodeStatusList" parameter.

The following table explains the error codes.

| Error code (16#...) | Name of the error | Explanation |
| --- | --- | --- |
| 8003_0000 | OpcUa_BadOutOfMemory | The memory allocation during the preparation of the call was not successful. This may have several sporadic causes. |
| 801F_0000 | OpcUa_BadUserAccessDenied | The user program does not have the required rights to read the requested node, e.g. SessionSecurityDiagnosticsArray |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The OPC_UA_NodeId refers to a node that does not exist in the server's address space. |
| 803D_0000 | OpcUa_BadNotSupported | The attribute cannot be read for this NodeId. Possible causes:  - The OPC_UA_NodeId belongs to the standard SIMATIC server interface. - The OPC_UA_NodeId is an OPC UA_node that does not support the attribute to be read. - The value of the attribute is read at an object node. |
| 803E_0000 | OpcUa_BadNotFound | The NamespaceIndex in the OPC_UA_NodeId could not be resolved. |
| 8074_0000 | OpcUa_BadTypeMismatch | The data type of the element at the "Tag" parameter does not match the data type of the associated OPC UA node. |

###### Applications

The following table lists some important use cases.

The following designations are used:

- ns: NamespaceIndex of the node in the OPC UA server
- i: Numeric identifier of the node
- s: String identifier of the node

You can determine the data specified in the "Comment" column (e. g. "ServerDiagnosticsSummary"), for example with this tool: [Siemens OPC UA Modeling Editor (SiOME)](https://support.industry.siemens.com/cs/ww/en/view/109755133)

| Use case | Source | Comment |
| --- | --- | --- |
| Determine NamespaceIndex | NamespaceArray (ns=0; i=2255) | Namespaces have a unique name. The server assigns a namespace index to each namespace when the namespace is created at runtime. When reading the "NamespaceArray" of the server, this namespace index can be accessed and evaluated. |
| Determine number of connected clients | CurrentSessionCount (ns=0; i=2277) | Each client creates at least one session. This information could help to determine if all partners of the machine are properly connected. All nodes below (ns=0; i=2275) "ServerDiagnosticsSummary" (of which "CurrentSessionCount" is a component) have a fixed NodeId in ns=0. |
| Check overall status of the server | ServerState (ns=0; i=2259) | The OPC UA server has an overall status (e.g. failed, running, etc.) that may be of interest to the user program. |
| Session diagnostics | SessionDiagnosticsArray (ns=0; i=3707) | The OPC UA server keeps track of all sessions. Several parameters can be of interest, e.g. ClientConnectionTime, ClientLastContactTime.  An entry is created in the SessionDiagnosticsArray for each session. In other words, the size of this array is variable. You must either provide a sufficiently large array in your user program or access a subset of this array using the NodeAddInfos parameter (see [Reading array range information with OPC_UA_ReadList](#reading-array-range-information-with-opc_ua_readlist-s7-1500)). To determine the current number of sessions, you read the CurrentSessionCount node (ns=0; i=2277) in the same read job. This allows you to determine how many values in the array are currently valid. You can specify the maximum number of sessions via the device configuration in TIA Portal.  See also below "Additional notes on session diagnostics". |
| Subscription diagnostics | SubscriptionDiagnosticsArray  (ns=0; i=2290) | The OPC UA server keeps track of all subscriptions and monitored objects. Several parameters can be of interest, e.g. LateSubscriptions, expired subscriptions.  An entry is created in the SubscriptionDiagnosticsArray for each subscription. In other words, the size of this array is variable. You must either provide a sufficiently large array in your user program or access a subset of this array using the NodeAddInfos parameter (see [Reading array range information with OPC_UA_ReadList](#reading-array-range-information-with-opc_ua_readlist-s7-1500)). To determine the current number of subscriptions, read the node CurrentSubscriptionCount (ns=0; i=2285) in the same read job. This allows you to determine how many values in the array are currently valid. If you want to access a single element of the SubscriptionDiagnosticsArray in your program, you need the Subscription ID, because it is part of the NodeId, e.g. ns=1; s=Subscription_<SubscriptionId>.MonitoredItemCount. The Subscription ID is not known at the time of configuration. |
| Static nodes of namespace 3 (standard SIMATIC interface) | - ns=3; s=DeviceManual - ns=3; s=DeviceRevision - ns=3; s=EngineeringRevision - ns=3; s=HardwareRevision - ns=3; s=Manufacturer - ns=3; s=Model - ns=3; s=OperatingMode - ns=3; s=OrderNumber - ns=3; s=RevisionCounter - ns=3; s=SerialNumber - ns=3; s=SoftwareRevision | You can read in your program those nodes that are available if the standard SIMATIC server interface has been deactivated in TIA Portal. |

###### Additional notes on session diagnostics

The SessionDiagnosticsArray (ns=0; i=3707) is of the OPC UA data type "SessionDiagnosticsDataType". This data type contains two "dynamic" arrays: "LocalIds" and "Client.Description.DiscoveryUrls". This means that the size of these arrays is not known at the time of configuration.

Up to and including firmware version V2.9, the size of an array that is part of a structure in your program must exactly match the size of the OPC UA array that is read. As of firmware version V3.0, the array size in the PLC program may be larger than the size of the read OPC UA array. This applies for read accesses on the OPC UA server of the local CPU as well as for read accesses of an OPC UA client on a remote OPC UA server. It is recommended that you completely reset the values in your program before the read operation, because the firmware of the PLC does not do this. If the currently read array is smaller than the previously read one, there is a risk that you are accessing old or invalid values in your program.

The following applies in regard to compatibility: Accesses that have worked so far will continue to work. Accesses that were previously incorrect may now return values.

If you want to access a single element of the SessionDiagnosticsArray (ns=0;i=3707) in your program, you have to determine the session ID first. The session ID is part of the NodeId and not yet known at the time of configuration. For example, if you want to determine the "ClientLastContactTime" for a certain session, the NodeId looks like this: ns=1; s=Session_<SessionId>. SessionDiagnostic. ClientLastContactTime. One way to determine the session ID is to read the SessionDiagnosticsArray (ns=0; i=3707) and use, for example, the session name to identify the session you are looking for. Both the session name and the session ID are part of the OPC UA "SessionDiagnosticsDataType" and are therefore contained in the SessionDiagnosticsArray (ns=0; i=3707) for each session.

###### More information

You are supported by an application example on the topic "Diagnosing the OPC UA server with OPC_UA_ReadList": [OPC UA server SIMATIC S7-1500 self-diagnostics](https://support.industry.siemens.com/cs/ww/en/view/109818073)

---

**See also**

[Diagnostics of the OPC UA server (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#diagnostics-of-the-opc-ua-server-s7-1500-s7-1500t)
  
[OPC_UA_SessionConnectInfo (S7-1500)](#opc_ua_sessionconnectinfo-s7-1500)
  
[Running diagnostics for OPC UA servers in the program (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#running-diagnostics-for-opc-ua-servers-in-the-program-s7-1200-s7-1500-s7-1500t)

#### Methods (S7-1500)

This section contains information on the following topics:

- [OPC_UA_MethodGetHandleList: Get handles for method calls (S7-1500)](#opc_ua_methodgethandlelist-get-handles-for-method-calls-s7-1500)
- [OPC_UA_MethodCall: Call method (S7-1500)](#opc_ua_methodcall-call-method-s7-1500)
- [OPC_UA_MethodReleaseHandleList: Release handles for method calls (S7-1500)](#opc_ua_methodreleasehandlelist-release-handles-for-method-calls-s7-1500)

##### OPC_UA_MethodGetHandleList: Get handles for method calls (S7-1500)

###### Validity

The following description of the "OPC_UA_MethodGetHandleList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

A programming example shows how to use the instruction in SCL.

This section assumes that you are creating and configuring a client interface for OPC UA communication; see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)". The efficient procedure ensures that most parameters for the client instruction are supplied automatically.

You use the instruction "OPC_UA_MethodGetHandleList" in your user program to receive numerical references (handles) from the server for methods that the server provides for OPC UA clients. OPC_UA_MethodGetHandleList is used to prepare method calls, see ① in the figure below.

The instruction returns the handles for the server methods.

![Description](images/103748017163_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of method calls |
| ② | Method calls |
| ③ | Instructions for "clean-up" after completed method calls |

###### Parameters for "OPC_UA_MethodGetHandleList"

The parameters of the instruction "OPC_UA_MethodGetHandleList"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| NodeIDCount | Input | UINT | Number of elements in the ObjectNodeIDs or MethodeNodeIDs parameter |
| ObjectNodeIDs | InOut | VARIANT | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the node IDs (NodeIDs) of the objects (folders) in which the methods are located. |
| MethodNodeIDs | InOut | VARIANT | Pointer to an array with elements of the type [OPC_UA_NodeId](#opc_ua_nodeid-s7-1500).  The array contains the node IDs (NodeIDs) of the methods for which handles are requested from the server. |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds. See also explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection) |
| NamespaceIndexCount | Input | UINT | Number of array elements in the parameter NamespaceIndexes. |
| NamespaceIndexes | InOut | VARIANT | Pointer to an array of the type UINT.  This parameter is not required if there are no elements in the NamespaceIndexCount parameter (NamespaceIndexCount = 0).  The array is used to assign new indexes to the namespace indexes in the NodeIDs parameter.  Example:   If there is a value of 10 in NamespaceIndexes[4], all NodeIds in the "NodeIDs" parameter that previously had the namespace index 4 are assigned the namespace index 10. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |
| StatusList | InOut | VARIANT | Pointer to an array of the type DWORD.   The array contains the error codes for the individual methods; see "Error numbers for NodeStatusList" below.   For each method, the system specifies whether or not a corresponding handle could be found. |
| MethodHdls | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the handles for the individual methods (NodeIDs) returned by the OPC UA server. |

###### Determining the "ObjectNodeIDs" and "MethodNodeIDs" parameters

**ObjectNodeIDs**

You can determine OPC_UA_NodeId, which must be entered at the "ObjectNodeIDs" parameter, for example with UaExpert:

![Determining the "ObjectNodeIDs" and "MethodNodeIDs" parameters](images/114504227339_DV_resource.Stream@PNG-de-DE.png)

![Determining the "ObjectNodeIDs" and "MethodNodeIDs" parameters](images/114504247819_DV_resource.Stream@PNG-de-DE.png)

**MethodNodeIDs**

You can find the OPC_UA_NodeId at the "MethodNodeIDs" parameter here:

![Determining the "ObjectNodeIDs" and "MethodNodeIDs" parameters](images/114506098955_DV_resource.Stream@PNG-de-DE.png)

![Determining the "ObjectNodeIDs" and "MethodNodeIDs" parameters](images/114506107147_DV_resource.Stream@PNG-de-DE.png)

###### Error numbers for Status

The following table shows a summary of error codes for this instruction:

| Error code (hex. values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8009_0000 | OpcUa_BadUnknownResponse | Server does not respond with the expected number of results |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_MethodGetHandleList" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 8074_0000 | OpcUa_BadTypeMismatch | You are using a data type that does not correspond to the data type in the server. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "ObjectNodeIDs". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "MethodNodeIDs". |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "NamenspaceIndexes". |
| B080_0400 | Simatic_BadType_VariantInput4 | Incorrect data type for parameter "StatusList". |
| B080_0500 | Simatic_BadType_VariantInput5 | Incorrect data type for parameter "MethodHdls". |
| B080_1100 | Simatic_ArrayElements_TooMany | Maximum number allowed for method list (Max_ELEMENTS_METHODLIST) exceeded. |
| B080_3100  B080_3200  B080_3300  B080_3400  B080_3500  General:  B080_3N00(N=Nth VARIANT of the instruction) | Simatic_BadNumElements_VariantInput1  Simatic_BadNumElements_VariantInput2  Simatic_BadNumElements_VariantInput3  Simatic_BadNumElements_VariantInput4  Simatic_BadNumElements_VariantInput5  General:   Simatic_BadNumElements_VariantInputN  (N=nth version of the instruction) | - Incorrect number of array elements at the 1st VARIANT parameter (VariantInput1):    NodeIDCount > Number of array elements from ObjectNodeIDs - Incorrect number of array elements at the 2nd VARIANT parameter (VariantInput2):   NodeIDCount > Number of array elements from MethodNodeIDs - Incorrect number of array elements at the 3rd VARIANT parameter (VariantInput3):    NamespaceIndexCount > Number of array elements from NamespaceIndexes - Incorrect number of array elements at the 4th VARIANT parameter (VariantInput4):    NodeIDCount > Number of array elements from StatusList - Incorrect number of array elements at the 5th VARIANT parameter (VariantInput5):    NodeIDCount > Number of array elements from MethodHdls   General: Wrong number of elements for the Nth VARIANT parameter. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for StatusList

The StatusList parameter contains an error code for each individual node ID (method).

The following table explains the error codes:

| Error code (hex.  values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | No error |
| 8033_0000 | OpcUa_BadNodeIdInvalid | The syntax of the node ID (NodeId) is incorrect. |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The NodeId refers to a node (method) that does not exist on the OPC UA server. |
| 8074_0000 | OpcUa_BadTypeMismatch | InputArguments / OutputArguments have incorrect type |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirements must also be met for the instruction "OPC_UA_MethodGetHandleList" (cf diagram above):

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction OPC_UA_Connect.
- Indexes of the namespaces in which the methods you want to call are located.

  You get the indices from the instruction [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500).

###### Function of the instruction

To speed up method calls, OPC UA servers use numeric references (handles) for methods.

You get these handles from the OPC UA server with the instruction "OPC_UA_MethodGetHandleList".

You need these handles for the OPC UA instruction for calling methods, "OPC_UA_MethodCall".

###### How to use a configured connection

1. In the "Project tree" area, select the CPU you want to use as a client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "Call_OpenDoor_On_Productionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_MethodGetHandleList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_MethodGetHandleList_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_MethodGetHandleList_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline", see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
7. Click "Data access" and select a method list.

   In the example, the method list is named "MethodListOpenDoor".

   STEP 7 now automatically supplies most parameters of the instruction with the correct tags.
8. Click on "Block parameters" and assign tags manually to the remaining parameters.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

The following excerpt from the program "Call_OpenDoor_On_Productionine" shows how to use the instruction "OPC_UA_MethodGetHandleList".

You can find the complete example program in the section [Example program for calling a method of an OPC UA server](#example-program-for-calling-a-method-of-an-opc-ua-server-s7-1500)

The example program is divided into multiple sections (Cases) by a CASE instruction.

Case 3 is shown here:

SCL

3: // case 3, get an handle for server method OpenDoor

    IF #Busy = FALSE THEN

            #Req := TRUE;

    ELSE

            #Req := FALSE;

    END_IF;

    #OPC_UA_MethodGetHandleList_Instance(REQ := #Req,

                  ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                  NodeIDCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

                  ObjectNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".ObjectNodes,

                  MethodNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodNodes,

                  Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                  NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

                  NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

                  Done => #Done,

                  Busy => #Busy,

                  Error => #Error,

                  Status => #Status,

                  StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

                  MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls);

**Asynchronous execution**

The instruction "OPC_UA_MethodGetHandleList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The figure above shows case 3. This part of the program registers the "OpenDoor" method on the OPC UA server. The "OPC_UA_MethodGetHandleList" method is called for this.

If the instruction is not yet executed, #Busy is FALSE, so that the "#Req" tag is set to the value TRUE. This starts the instruction. In the next cycle, #Req is FALSE.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

    IF #Done = TRUE THEN

            IF "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0] = 0 THEN   //one method

                  #State := #State + 1;

            ELSE

                  #State := 100;

                  //In case 100, set REQ of instruction "OPC_UA_Disconnect" to FALSE

                  #Set_REQ_To_FALSE := TRUE;

                  #Mem_Status := #Status;

                  #Output_Error_Message := WString#'Error at MethodGetHandleList';

            END_IF;

    END_IF;

    IF #Error = TRUE THEN

            #State := 100;

            //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

            #Set_REQ_To_FALSE := TRUE;

            #Mem_Status := #Status;

            #OPC_UA_MethodGetHandleList_Instance(REQ := FALSE,

                  ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                  NodeIDCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

                  ObjectNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".ObjectNodes,

                  MethodNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodNodes,

                  Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                  NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

                  NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

                  StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

                  MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls);

    END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the value TRUE is set at the "Error" output parameter. This sets "#State" to the value 100. This case is reserved for troubleshooting.

If the output parameter "Done" is TRUE, the instruction was executed successfully.

It is possible that the instruction was successfully executed ("Error" parameter not set, "Done" parameter set) but no handle could be returned for a method.

Therefore, there is a check in the example to determine whether the handle for the "OpenDoor" method has been returned:

- If the condition is met, the value of the "#State" tag is increased by one. This means the next program section - case 4 (Call method) - is executed in the next cycle. Case 4 is described in [OPC_UA_MethodCall: Call method](#opc_ua_methodcall-call-method-s7-1500).
- If the condition is not met, this is assessed as an error and #State has a value of 100. The error case is run through in the next cycle.

> **Note**
>
> If you register a multiple methods with OPC_UA_MethodGetHandleList in your application, it can be useful always to increase #State by one when #Done = TRUE and only check whether a valid handle was returned for a given method in question before the individual methods are called with "OPC_UA_MethodCall" (in case 4).

##### OPC_UA_MethodCall: Call method (S7-1500)

###### Validity

The following description of the "OPC_UA_MethodCall" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

You use the instruction "OPC_UA_MethodCall" in your user program to call a method on the server.

The figure below shows the structure of a user program. The "OPC_UA_MethodCall" instruction is located in section ②:

![Description](images/103767048971_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of method calls |
| ② | Method calls |
| ③ | Instructions for "clean-up" after completed method calls |

###### Parameters for "OPC_UA_MethodCall"

The parameters of the instruction "OPC_UA_MethodCall"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| MethodHdl | Input | DWORD | Handle for the method to be called. |
| InputArguments | InOut | VARIANT | Pointer to a tag with the PLC data type (UDT) or STRUCT, the name, number, order and data type of which correspond to the expected input parameters. |
| OutputArguments | InOut | VARIANT | Pointer to a tag with the PLC data type (UDT) or STRUCT, the name, number, order and data type of which correspond to the expected output parameters. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |
| MethodResult | InOut | VARIANT | Pointer to a tag of the type DWORD that contains the error code (result) of the server method called.   This error code is provided by the user program of the OPC UA server. In the case of an S7-1500 CPU as OPC UA server, it is the "UAMethod_Result" parameter of the server instruction "OPC_UA_ServerMethodPost" that you can read out with the client instruction "OPC_UA_MethodCall".  If the instruction "OPC_UA_MethodCall" was not executed (Error = true, Status <> 0), no value is set for MethodResult. |

###### Error numbers for Status

The Status parameter provides information about errors that occur during execution of the instruction.

The following table explains the error codes:

| Error code (hex. values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 8006_0000 | OpcUa_BadEncodingError | Error decoding the output argument |
| 8009_0000 | OpcUa_BadUnknownResponse | Server does not respond with the expected number of results |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_MethodCall" instructions that can be called at the same time per connection has been exceeded (> 5), see:   [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| 8034_0000 | BadNodeIdUnknown | The node id refers to a node that does not exist in the server address space.  The NamespaceIndex of the specified NodeId might not exist. If the error code is displayed when the instruction "OPC_UA_MethodCall" is called:   Another possible cause is the use of invalid ObjectIDs in the preceding call of OPC_UA_MethodGetHandleList. The instruction "OPC_UA_MethodGetHandleList" does not evaluate the ObjectIDs. |
| 8074_0000 | OpcUa_BadTypeMismatch | Argument variant has incorrect type. |
| 8075_0000 | OpcUa_BadMethodInvalid | No registered method for the specified MethodHdl |
| 8076_0000 | BadArgumentsMissing | The client has not specified all specified input arguments. |
| 80AB_0000 | OpcUa_BadInvalidArgument | Input arguments have incorrect type. |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "MethodResult" to which the 1st variant parameter of the instruction points. |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "InputArguments" to which the 2nd variant parameter of the instruction points. |
| B080_0300 | Simatic_BadType_VariantInput3 | Incorrect data type for parameter "OutputArguments" to which the 3rd variant parameter of the instruction points. |
| B080_1100 | Simatic_ArrayElements_TooMany | General error code. Occurs when an array has too many elements. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirements must also be met for the instruction "OPC_UA_MethodCall" (cf diagram above):

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction, see [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).
- Indexes of the namespaces that contain the methods that you want to call with the client.

  You get the indexes from the instruction "OPC_UA_NamespaceGetIndexList".

  A handle for the method that you want to call in your user program.

  You get the handle from the instruction, see [OPC_UA_MethodGetHandleList: Get handles for method calls](#opc_ua_methodgethandlelist-get-handles-for-method-calls-s7-1500).

###### Function of the instruction

You use the instruction "OPC_UA_MethodCall" to call a method that has been released in an OPC UA server.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU you want to use as a client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "Call_OpenDoor_On_Productionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_MethodCall" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_MethodCall_Instance".
5. Click on the icon for "Start configuration" at the "OPC_UA_MethodCall_Instance" instruction.

   STEP 7 opens the "Configuration" tab in the Inspector window.
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline".
7. Click "Data access" and select a method list.

   In the example, the method list is called "MethodListOpenDoor".

   STEP 7 automatically supplies most parameters of the instruction with tags, but not the parameters Busy, Done, Error.
8. Create the local tags for the parameters yet to be supplied.
9. Click on "Block parameters" and assign the local tags to the remaining parameters.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

The following excerpt from the program "Call_OpenDoor_On_Productionine" shows how to use the instruction "OPC_UA_MethodCall".

You can find the complete example program in the section [Example program for calling a method of an OPC UA server](#example-program-for-calling-a-method-of-an-opc-ua-server-s7-1500).

The example program is divided into multiple sections (Cases) by a CASE instruction.

Case 4 is shown here:

SCL

4: // case 4, call method OpenDoor

IF #Init_Method_InputParameter = TRUE THEN

       #Init_Method_InputParameter := FALSE;

       //for our server method at Productionline, we set input parameters to 1

       "Productionline_Data".MethodListOpenDoor.Method.Inputs.Number := 1;

END_IF;

IF #Busy = FALSE THEN

       #Req := TRUE;

ELSE

       #Req := FALSE;

END_IF;

#OPC_UA_MethodCall_Instance(REQ := #Req,

           ConnectionHdl:="Productionline_Configuration".Connection.ConnectionHdl,

           Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

           MethodHdl := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls[0],

           Status => "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0],

           InputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Inputs,

           OutputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Outputs,

           MethodResult := "Productionline_Data"."MethodListOpenDoor".MethodResultList[0],

           Done => #Done,

          Busy => #Busy,

           Error => #Error);

   //"Productionline_Data"."MethodListOpenDoor".MethodResultList[0]] contains

   //the status/error codes of the server method

   //which was run on the connected CPU as user program

   //These codes are defined as follows:   //

   //     Good: 0x0000_0000 TO 0x3FFF_ FFFF

   //     Uncertain: 0x4000_0000 TO 0x7FFF_FFFF

   //     Bad: 0x8000_0000 TO 0xFFFF_FFFF

**Asynchronous execution**

The instruction "OPC_UA_MethodCall" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The figure above shows case 4. This part of the program calls the server method "OpenDoor" on the OPC UA server.

The "OPC_UA_MethodCall" instruction receives the handle for the server method and the input parameters.

In the example, only the "Number" input parameter is used. The value is set to 1, so that the server method can be fully executed.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

IF #Done = TRUE THEN  
    IF "Productionline_Data".MethodListOpenDoor.MethodResultList[0] < 16#8000_0000 THEN

        #State := #State + 1;

    ELSE

        //server method did not run successfully

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #Output_Error_Message := WString#' Error at server method';

    END_IF;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #Mem_Status := "Productionline_Data".MethodListOpenDoor.MethodStatusList[0];

    #OPC_UA_MethodCall_Instance(REQ := #Req,

          ConnectionHdl:="Productionline_Configuration".Connection.ConnectionHdl,

          Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

          MethodHdl := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls[0],

          Status => "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0],

          InputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Inputs,

          OutputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Outputs,

          MethodResult := "Productionline_Data"."MethodListOpenDoor".MethodResultList[0],

          Done => #Done,

          Busy => #Busy,

          Error => #Error);

END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If the output parameter "Done" is TRUE, the "OPC_UA_MethodCall" instruction was executed successfully.

Also check whether the method called on the OPC UA server, "Productionline", was executed successfully. This is the case if the parameter "MethodResult" contains a value that is less than 16#8000_0000.

If executed successfully, the value of the "#State" tag is increased by one. This means the next program section - case 5 - is executed in the next cycle.

Case 5 is described in [OPC_UA_MethodReleaseHandleList: Release handles for method calls](#opc_ua_methodreleasehandlelist-release-handles-for-method-calls-s7-1500).

If an error occurs, the "OPC_UA_MethodCall" instruction at the "Error" output parameter is set to the value TRUE. This sets the value of the "#State" tag to 100. This case is reserved for troubleshooting.

---

**See also**

[OPC_UA_NamespaceGetIndexList: Read namespace indexes (S7-1500)](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500)

##### OPC_UA_MethodReleaseHandleList: Release handles for method calls (S7-1500)

###### Validity

The following description of the "OPC_UA_MethodReleaseHandleList" instruction applies to S7-1500 CPUs with firmware version V2.6 and higher.

###### Description

A programming example shows how to use the instruction manually in SCL programming language.

This section assumes that you are creating and configuring a client interface for OPC UA communication; see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)". The efficient procedure ensures that most parameters for the client instruction are supplied automatically.

You use the instruction "OPC_UA_MethodReleaseHandleList" in your user program to release numerical references (handles) for methods.

OPC_UA_MethodReleaseHandleList is used to release method handles, see ③ in the figure below.

![Description](images/103761167755_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Instructions for preparation of method calls |
| ② | Method calls |
| ③ | Instructions for "clean-up" after completed method calls |

###### Parameters for "OPC_UA_MethodReleaseHandleList"

The parameters of the instruction "OPC_UA_MethodReleaseHandleList"

| Parameters | Declaration in area | Data type | Meaning |
| --- | --- | --- | --- |
| REQ | Input | BOOL | A rising edge 0 → 1 at the parameter triggers execution of the instruction. |
| ConnectionHdl | Input | DWORD | Unique identifier for a connection established.   You get the handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| Timeout | Input | TIME | Maximum time for execution of the instruction in milliseconds.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| MethodHdlCount | Input | UINT | Number of elements in the MethodHdls parameter |
| MethodHdls | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the handles for the individual methods (NodeIds) that are to be released. |
| StatusList | InOut | VARIANT | Pointer to an array of the type DWORD.  The array contains the error codes for the individual methods; see "Error numbers for NodeStatusList" below.  For each method, it is specified whether a handle was successfully released. |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error numbers for Status" below |

###### Error numbers for Status

The following table shows a summary of error codes for this instruction:

| Error code (hex. values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | Instruction finished successfully. |
| 0070_0000 | - | First call without rising edge at REQ, which means job execution is not started |
| 0070_0100 | - | First call with start of job execution |
| 0070_0200 | - | Subsequent call |
| 8003_0000 | OpcUa_BadOutOfMemory | No memory available for the OPC UA client.   As the OPC UA client and OPC UA server share a memory area, you should reduce the memory requirement of the server.  You have the following options:  - Release fewer PLC tags for OPC UA. - Reduce the number of OPC UA clients that are currently connected to the server. - Set up fewer subscriptions. |
| 800A_0000 | OpcUa_BadTimeout | A network timeout occurred.   Possible causes:  - Connection to the OPC UA server is too slow (insufficient capacity) - The network load is too high. - The OPC UA server is not available.   Possible remedy:  - Check the URL of the OPC UA server - Increase the timeout setting (higher value for the Timeout parameter of the function block OPC_UA_Connect). |
| 800D_0000 | OpcUa_BadServerNotConnected | The server is not connected or the connection handle is incorrect or invalid. |
| 800F_0000 | OpcUa_BadNothingToDo | Nothing to do: The OPC UA server received an empty list with no instructions from the OPC UA client. |
| 8010_0000 | OpcUa_BadTooManyOperations | Number of "OPC_UA_MethodReleaseHandleList" instructions that can be called at the same time per connection has been exceeded (> 1), see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| B080_0100 | Simatic_BadType_VariantInput1 | Incorrect data type for parameter "MethodHdls". |
| B080_0200 | Simatic_BadType_VariantInput2 | Incorrect data type for parameter "StatusList". |
| B080_1100 | Simatic_ArrayElements_TooMany | MethodHdlCount > MAX_ELEMENTS_METHOD |
| B080_3100 | BadNumElements_VariantInput1 | MethodHdlCount > Number of array elements of the "MethodHdls" parameter. |
| B080_3200 | BadNumElements_VariantInput2 | MethodHdlCount > Number of array elements of the "StatusList" parameter. |
| B080_C400 | Simatic_ClientNotEnabled | The OPC UA client is disabled. |
| B080_C500 | Simatic_NothingToDo | Nothing to do: The instruction is using a list that contains no elements. |
| C080_C300 | Simatic_OutOfResources | The maximum number of client instructions that can be used at the same time has been exceeded.  Possible remedy:  - Reduce the number of client instructions of the type running parallel, see: [Number of client instructions that can be used simultaneously](Configuring%20automation%20systems.md#number-of-client-instructions-that-can-be-used-simultaneously-s7-1500-s7-1500t) |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Error numbers for "StatusList"

The "StatusList" parameter contains an error code for each individual handle.

The following table explains the error codes:

| Error code (hex.  values) | Name of the error | Explanation |
| --- | --- | --- |
| 0000_0000 | OpcUa_Good | No error |
| 8034_0000 | OpcUa_BadNodeIdUnknown | The method handle transferred is not known. |
| For more error codes, see [Error codes](#error-codes-s7-1500). |  |  |

###### Requirements

The following description assumes that:

- You have created a client interface, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
- You have created and configured a connection to an OPC UA server, see "[Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t)".

In addition, the following requirements must also be met for the instruction "OPC_UA_MethodReleaseHandleList" (cf diagram above):

- A handle for connection to an OPC UA server is available.

  You get the connection handle from the instruction [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection).
- A list of method handles that you no longer want to call in your user program.

  You get this handle list from the instruction [OPC_UA_MethodGetHandleList: Get handles for method calls](#opc_ua_methodgethandlelist-get-handles-for-method-calls-s7-1500).
- Optional (not needed here): Indexes of the namespaces that contain the methods.

  You get the indexes from the instruction [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500).

###### Function of the instruction

You call the instruction "OPC_UA_MethodReleaseHandleList" to release handles for methods that you no longer require in your program.

###### How to use a configured connection

1. In the "Project tree" area, select the CPU you want to use as a client.
2. Select the function block that is to execute the client instruction in the "Program blocks" folder.

   In the example, the function block is called "Call_OpenDoor_On_Productionline".

   Selected language: SCL.
3. Use drag-and-drop to move the instruction "OPC_UA_MethodReleaseHandleList" from the folder "Instructions > Communication > OPC UA > OPC UA Client" to the editor.
4. Select the call as multi-instance.

   STEP 7 creates an instance of this instruction and calls it "OPC_UA_MethodReleaseHandleList_Instance".
5. Click "OPC_UA_MethodReleaseHandleList_Instance".

   STEP 7 opens the "Configuration".
6. Under "Select client interface for OPC UA interface" you select the client interface that you want to use for the instruction.

   In the example, the client interface is called "Productionline", which was created, see "[Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t)".
7. Click "Data access" and select a method list.

   In the example, the method list is named "MethodListOpenDoor".

   STEP 7 automatically supplies most parameters of the instruction with tags, but not the parameters Busy, Done, Error.
8. Create the local tags for the parameters yet to be supplied.
9. Click on "Block parameters" and assign tags manually to the remaining parameters.

   STEP 7 adds the selected tag to the function call.

###### Calling the instruction (initial call)

The following excerpt from the program "Call_OpenDoor_On_Productionine" shows how to use the instruction "OPC_UA_MethodReleaseHandleList".

You can find the complete example program in the section [Example program for calling a method of an OPC UA server](#example-program-for-calling-a-method-of-an-opc-ua-server-s7-1500)

The example program is divided into multiple sections (Cases) by a CASE instruction.

Case 5 is shown here:

SCL

5: // case 5, release method handle

    IF #Busy = FALSE THEN

             #Req := TRUE;

    ELSE

             #Req := FALSE;

    END_IF;

    #OPC_UA_MethodReleaseHandleList_Instance(REQ := #Req,

             ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

             Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

             MethodHdlCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

             MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls,

             StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

             Done => #Done,

             Busy => #Busy,

             Error => #Error,

             Status => #Status);

**Asynchronous execution**

The instruction "OPC_UA_MethodReleaseHandleList" runs asynchronously to the user program and requires multiple program cycles.

You can check the job status with the "Busy", "Done", "Error" and "Status" parameters.

Asynchronous program execution is described in the section "[Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)".

###### Explanation of the call of the instruction (initial call)

The figure above shows case 5. This part of the program releases the handle for a server method again.

In the example, the handle for the "OpenDoor" server method is passed to the "MethodHdls" parameter.

If this handle cannot be released, the "StatusList" parameter contains an error code.

###### Calling the instruction (troubleshooting)

The figure below shows evaluation of the "Done" and "Error" parameters.

SCL

IF #Done = TRUE THEN

#Mem_Status := #Status;

    IF "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0] = 0 THEN

    #State := #State + 1;

ELSE

    #State := 100;

    //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    Mem_Status := #Status;

    #Output_Error_Message := WString#'Error at MethodGetHandleList';

    END_IF;

END_IF;

IF #Error = TRUE THEN

    #State := 100;

    //In case 100, to set REG of instruction "OPC_UA_Disconnect" to FALSE

    #Set_REQ_To_FALSE := TRUE;

    #Mem_Status := #Status;

    #OPC_UA_MethodReleaseHandleList_Instance(REQ := FALSE,

             ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

             Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

             MethodHdlCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

             MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls,

             StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList);

END_IF;

###### Explanation of the call of the instruction (troubleshooting)

If an error occurs, the "OPC_UA_MethodReleaseHandleList" instruction at the "Error" output parameter is set to the value TRUE. This sets the value of the "#State" tag to 100. This case is reserved for troubleshooting. The example program also calls the instruction "OPC_UA_MethodReleaseHandleList" to set the REQ parameter to FALSE.

If the output parameter "Done" is TRUE, the "OPC_UA_MethodReleaseHandleList" instruction was executed successfully.

In the example, there is also a check to determine of the handle for the "OpenDoor" server method has been released.

If executed successfully, the value of the "#State" tag is increased by one. This means the next program section - case 6 - is executed in the next cycle.

Case 6 is described in [OPC_UA_Disconnect: Close the connection](#opc_ua_disconnect-close-the-connection-s7-1500).

> **Note**
>
> Case 6 is for enabling the connection to the OPC UA server. This also releases all other resources that the client program has occupied in the server. If you want to terminate the connection to the server, your user program can execute case 6 immediately and skip case 5.

#### System data types for OPC UA client instructions (S7-1500)

This section contains information on the following topics:

- [OPC_UA_SessionConnectInfo (S7-1500)](#opc_ua_sessionconnectinfo-s7-1500)
- [OPC_UA_NodeId (S7-1500)](#opc_ua_nodeid-s7-1500)
- [OPC_UA_NodeAdditionalInfo (S7-1500)](#opc_ua_nodeadditionalinfo-s7-1500)
- [OPC_UA_NodeAdditionalInfoExt (S7-1500)](#opc_ua_nodeadditionalinfoext-s7-1500)
- [OPC_UA_BrowsePath (S7-1500)](#opc_ua_browsepath-s7-1500)
- [OPC_UA_RelativePath (S7-1500)](#opc_ua_relativepath-s7-1500)
- [OPC_UA_RelativePathElement (S7-1500)](#opc_ua_relativepathelement-s7-1500)
- [OPC_UA_QualifiedName (S7-1500)](#opc_ua_qualifiedname-s7-1500)

##### OPC_UA_SessionConnectInfo (S7-1500)

###### OPC_UA_SessionConnectInfo

See the following table for the meaning of the connection information for the "SessionConnectInfo" parameter of the "OPC_UA_Connect" instruction.

Parameters of system data type "OPC_UA_SessionConnectInfo"

| Parameter | S7 data type | Meaning |
| --- | --- | --- |
| SessionName | WSTRING[64] | Name of the session, which you can enter here. The parameter can be empty.  If you do not enter a name, the OPC UA server assigns one.  The session name is used, for example, to identify the connection for diagnostic purposes. |
| ApplicationName | WSTRING[64] | Name of the OPC UA client. The application name is a component of the client description, which in turn is a component of the session (see SessionName). It is not possible to set a unique ApplicationName for each session. The STRING **must** be empty, otherwise error code "Simatic_BadValue_VariantInput2 (0xB080_2200)" is returned. The configured application name is used as the ApplicationName for SIMATIC (CPU parameters in the OPC UA area). |
| SecurityMsgMode | UDINT | Security process  - 0 = Best possible procedure Note: This setting is not permitted! - 1 = None - 2 = Sign - 3 = Sign&Encrypt |
| SecurityPolicy | UDINT | Securityprofile  - 0 = Best possible security profile Note: This setting is not permitted! - 1 = No security profile - 2 = Basic128Rsa15 - 3 = Basic256 - 4 = Basic256Sha256 |
| ServerUri | STRING[254] | Only relevant for connections to an OPC UA server via a gateway server.  CPUs with firmware versions ≤ V2.6 do not support gateway servers. This parameter therefore must be supplied with an empty string. |
| CheckServerCertificate | BOOL | If this bit is set, the client checks the certificate sent by the server against the configured trustworthy certificates. You can access the list of trusted certificates via the properties of the Client CPU > "Protection & Security" area > Certificate Manager. There you can find the "Certificates of the partner devices" table, which you have to fill out.  The requirement for filling is that you have imported the required certificates via the global certificate manager (Project tree > Certificate manager > "Trusted Certificates and Root Certification Authorities" tab).   If the bit is not set, the client does not check the server certificate. |
| TransportProfile | UDINT | 1 = UATP_UATcp  According to the PLCopen specification, only this transport profile is supported. |
| UserIdentityTokenType | UDINT | For user authentication data, see the explanation below this table. |
| UserTokenParam1 | WSTRING[64] | The meaning depends on UserIdentityTokenType (for example user name). |
| UserTokenParam2 | WSTRING[64] | The meaning depends on UserIdentityTokenType (for example password). |
| CertificateID | UDINT | The ID of the certificate that you use for the OPC UA client.  You can find the ID in STEP 7 (TIA Portal) under "Global security settings" > "Certificate manager" > "Device certificates" and also in the CPU properties ("Protection & Security" > "Certificate Manager" area). There you can find the "Device certificates" table with the IDs of the certificates.   Proceed as follows to generate a certificate for the client:  1. In the TIA Portal, select the properties of the CPU that is used as the client. 2. If a self-signed certificate is sufficient for you, skip this step. If you want to use a certificate signed by a CA, then select the "Use global security settings for certificate manager" option under "Security" > "Certificate manager" > "Global security settings". 3. Navigate to the "Device certificates" table and double-click on an empty field in the "Certificate holder" column.  A certificate icon appears at the left edge of the row. 4. Click on the "Certificate holder" field again.  A drop-down list opens showing the existing device certificates. 5. Click on the "Add" button. A dialog with setting options for the certificate is displayed. 6. Select "OPC UA Client" or "OPC UA Client & Server" for the use and then "OK". |
| SessionTimeout | TIME | Maximum time for which a session is maintained after the connection to the OPC UA server has been interrupted (in milliseconds).  Default setting: 20000 (20 seconds) |
| MonitorConnection | TIME | Connection monitoring time (in milliseconds)  Time interval for checking a connection over which no data is currently being transferred.  Default setting: 5000 (5 seconds) |
| LocaleIDs | ARRAY[1..5] of STRING[6] | Optional language and regional identifier acc. to RFC 3066.  0 = no or unknown LocaleID. |

###### "UserIdentityTokenType" parameter

The following table shows the values possible for "UserIdentityTokenType" for S7-1500 CPUs and the relationship between the "UserIdentityTokenType", "UserTokenParam1" and "UserTokenParam2" parameters of the system data type "UASessionConnectInfo":

| UserIdentityTokenType | UserTokenParam1 | UserTokenParam2 | Description |
| --- | --- | --- | --- |
| **0** | Ignored | Ignored | Guest authentication, which means access without authentication.  (Anonymous user) |
| **1** | User name | Password | Authentication by means of user name and password.  The password is stored in plain text in the corresponding global data block or instance data block and can be read out.  However, an S7-1500 CPU as OPC UA client only permits connection establishment when the security policies ensure that the user name and password are only transmitted encrypted.   Recommendation: Use users from the user administration of the project. |
| **42** | User name from the user administration of the project (Security settings) | Ignored | Simatic-specific value for UserIdentityTokenType. Authentication only for users from the user administration of the project.  For users from the user administration of the project, you download the password together with the other user data and the configuration data to the client CPU.   This way you protect the password from being accessed from the outside. You must have assigned the function right "User authentication of the OPC UA client" to the user in the project tree (Security settings > Users and roles).  When you make the settings for user authentication in the OPC UA client interface, select the option "User (TIA Portal – Security settings)" and enter a previously configured user name. |
| **65** | User name | Password | Simatic-specific value for UserIdentityTokenType.   The password is stored in plain text in the corresponding global data block or instance data block and can be read out.  An S7-1500 CPU as OPC UA client with this UserIdentityTokenType also permits connection establishment when no encrypted connection is set, and the password is therefore transmitted unencrypted.   **Only use this**  **UserIdentityTokenType**  **when the OPC UA server requires unencrypted transmission and make sure that the transmission takes place in a secured environment.**    Recommendation: Use users from the user administration of the project. |

---

**See also**

[OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection)

##### OPC_UA_NodeId (S7-1500)

###### OPC_UA_NodeId

See the following table for the meaning of the "OPC_UA_NodeId" parameters for identifying the destination node in the OPC UA server. "OPC_UA_NodeId" supplies the "NodeIDs" parameter of the "OPC_UA_NodeGetHandleList" instruction.

Parameters of system data type "OPC_UA_NodeId"

| Parameter | S7 data type | Meaning |
| --- | --- | --- |
| NamespaceIndex | UINT | Namespace index of the node in the OPC UA server.  A node can, for example, be an object or a tag. |
| Identifier | WSTRING[254] | The designation of the node (object or tag) depends on the identifier type:  - Numeric identifier: The node is labeled with a number, for example "12345678" (STRING with converted DWORD). - String identifier: The node is labeled with a name, for example "MyTag". Names are case-sensitive. - For the names of nodes of "GUID" and "Opaque" type, see below. |
| IdentifierType | UDINT | Type of identifier  - 0: Numeric identifier - 1: String identifier - 2: GUID - 3: Opaque |

###### Identifier of IdentifierType "GUID"

Format: {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}

Example for entering the format of IdentifierType GUID (2) in STEP 7:

WSTRING#'5ce9dbce-5d79-434c-9ac3-1cfba9a6e92c'

###### Identifier of IdentifierType "Opaque"

Opaque identifiers are identifiers with an apparently random sequence of characters without immediately recognizable semantics.

With OPC UA, you can generate an identifier of Opaque type by encoding any byte array of defined length (e.g. ASCII string 'abcd' or the HEX counterpart (0x61626364) Base64. Numerous tools are available for Base64 encoding.

Example for the format of IdentifierType Opaque (3) in STEP 7 after coding the HEX value:

WSTRING#'YWJjZA=='

The server displays the uncoded value of the identifier, in this case the HEX value.

---

**See also**

[OPC_UA_NodeGetHandleList: Get handles for read and write access (S7-1500)](#opc_ua_nodegethandlelist-get-handles-for-read-and-write-access-s7-1500)

##### OPC_UA_NodeAdditionalInfo (S7-1500)

###### OPC_UA_NodeAdditionalInfo

Specifies attribute types and index range of nodes for the "NodeAddInfos" parameter of the "OPC_UA_ReadList" and "OPC_UA_WriteList" instructions.

- The data type is used for scalar values and one-dimensional arrays.

  To read a section of a multi-dimensional array (up to six dimensions, (matrix)), use the "OPC_UA_NodeAdditionalInfoExt" data type.

  Read the information on [Mapping SIMATIC data types to OPC UA data types](Configuring%20automation%20systems.md#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t).
- The StartIndex must be greater than or equal to "0" and less than or equal to EndIndex.
- Settings for the full reading of reading lists consisting of scalars and arrays:

  If both StartIndex and EndIndex have the value 4_294_967_295 (UDINT_MAX), the server ignores the value for StartIndex and EndIndex and fully reads scalars and arrays, see. [Reading array range information with OPC_UA_ReadList](#reading-array-range-information-with-opc_ua_readlist-s7-1500).

Parameters of system data type "OPC_UA_NodeAdditionalInfo"

| Parameters | Data type | Meaning |
| --- | --- | --- |
| AttributeId | UDINT | Specifies which attribute of a node (tag) is to be read.  The IDs of the attributes are defined in the OPC UA enumeration type "UAAttributeId".  Examples:   - 5: Description (Description) - 13: Value (value) - 14: DataType (Data type) - 15: ValueRank (number of dimensions in the Value attribute) - 16: ArrayDimensions (length of a dimension, number of elements)   The default is 13 (Value). |
| StartIndex | UDINT | When AttributeId = 13: The start index of an array. Values are read starting at this index. |
| EndIndex | UDINT | When AttributeId = 13: The end index of an array. Values are read to this index. |

---

**See also**

[OPC_UA_NodeAdditionalInfoExt (S7-1500)](#opc_ua_nodeadditionalinfoext-s7-1500)

##### OPC_UA_NodeAdditionalInfoExt (S7-1500)

###### OPC_UA_NodeAdditionalInfoExt

Specifies the attribute of the node and the index are for the "NodeAddInfos" parameter ("OPC_UA_ReadList" and "OPC_UA_WriteList" instructions).

Parameters of system data type "OPC_UA_NodeAdditionalInfoExt"

| Parameter | S7 data type | Meaning |
| --- | --- | --- |
| AttributeID | UDINT | Specifies which attribute of a node (tag) is to be read or written.  The default is 13 (Value). |
| IndexRangeCount | UDINT | Number of the following index ranges.  You do not need to specify all six index ranges. |
| StartIndex1 | UDINT | The index from which values for array dimension 1 are to be read or written. |
| EndIndex1 | UDINT | The index up to which values for array dimension 1 are to be read or written. |
| StartIndex2 | UDINT | The index from which values for array dimension 2 are to be read or written. |
| EndIndex2 | UDINT | The index up to which values for array dimension 2 are to be read or written. |
| StartIndex3 | UDINT | The index from which values for array dimension 3 are to be read or written. |
| EndIndex3 | UDINT | The index up to which values for array dimension 3 are to be read or written. |
| StartIndex4 | UDINT | The index from which values for array dimension 4 are to be read or written. |
| EndIndex4 | UDINT | The index up to which values for array dimension 4 are to be read or written. |
| StartIndex5 | UDINT | The index from which values for array dimension 5 are to be read or written. |
| EndIndex5 | UDINT | The index up to which values for array dimension 5 are to be read or written. |
| StartIndex6 | UDINT | The index from which values for array dimension 6 are to be read or written. |
| EndIndex6 | UDINT | The index up to which values for array dimension 6 are to be read or written. |

---

**See also**

[OPC_UA_NodeAdditionalInfo (S7-1500)](#opc_ua_nodeadditionalinfo-s7-1500)

##### OPC_UA_BrowsePath (S7-1500)

###### OPC_UA_BrowsePath

See the following table for the structure of the system data type "OPC_UA_BrowsePath":

Parameters of system data type "OPC_UA_BrowsePath"

| Name | Data type | Meaning |
| --- | --- | --- |
| StartingNode | OPC_UA_NodeId | NodeId of the node (or tag) at which the path starts.  Browsing is to be from this node on. |
| RelativePath | OPC_UA_RelativePath | The relative path for browsing; see [OPC_UA_RelativePath](#opc_ua_relativepath-s7-1500). |

##### OPC_UA_RelativePath (S7-1500)

###### OPC_UA_RelativePath

See the following table for the structure of the system data type "OPC_UA_RelativePath":

Parameters of system data type "OPC_UA_RelativePath"

| Name | Data type | Meaning |
| --- | --- | --- |
| NoOfElements | UINT | Number of elements in Elements |
| Elements | Array [4] of OPC_UA_RelativePathElement | Array with up to four elements of the type [OPC_UA_RelativePathElement](#opc_ua_relativepathelement-s7-1500) |

##### OPC_UA_RelativePathElement (S7-1500)

###### OPC_UA_RelativePathElement

See the following table for the structure of the system data type "OPC_UA_RelativePathElement":

Parameters of system data type "OPC_UA_RelativePathElement"

| Name | Data type | Meaning |
| --- | --- | --- |
| ReferenceTypeId | OPC_UA_NodeId | The reference type to be followed in this RelativePathElement.   ReferenceTypeId is set by default for hierarchical references. |
| IsInverse | BOOL | If TRUE, the inverse direction is followed.  The default is FALSE. |
| IncludeSubtypes | BOOL | If TRUE, the reference types derived from the type specified under ReferenceTypeId are also followed.  The default is TRUE. |
| TargetName | OPC_UA_QualifiedName | See system data type [OPC_UA_QualifiedName](#opc_ua_qualifiedname-s7-1500) |

##### OPC_UA_QualifiedName (S7-1500)

###### OPC_UA_QualifiedName

See the following table for the structure of the system data type "OPC_UA_QualifiedName":

Parameters of system data type "OPC_UA_QualifiedName"

| Name | Data type | Meaning |
| --- | --- | --- |
| NamespaceIndex | UINT | The namespace index of the name. |
| Name | WSTRING[64] | BrowseName of the node (or tag). |

#### Error codes (S7-1500)

This section contains information on the following topics:

- [Siemens error codes (S7-1500)](#siemens-error-codes-s7-1500)
- [Error codes of the OPC Foundation (S7-1500)](#error-codes-of-the-opc-foundation-s7-1500)
- [PLCopen error codes (S7-1500)](#plcopen-error-codes-s7-1500)

##### Siemens error codes (S7-1500)

###### SIMATIC status codes for OPC UA instructions

The table below lists the Siemens error codes for the OPC UA client instructions:

| Status code | Meaning |
| --- | --- |
| B080_0100 | BadType_VariantInput1:   The data type of the tag to which the first variant parameter of the instruction is pointing is incorrect.   **An example:**   For the instruction "OPC_UA_Connect", the parameter "ServerEndpointUrl" is the first variant parameter.  The order of VariantInput1 to VariantInput5 corresponds to the order of the variant parameters in the documentation for the respective OPC UA instruction.  If the first variant parameter points to a tag that has the incorrect data type, the status code "B080_0100" is returned.  The correct data type is listed in the "Parameter" table of the respective instruction.  In the example, you can find the data type of the 'Parameter for "OPC_UA_Connect"' table in the section on the instruction "[OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection)". |
| B080_0200 | BadType_VariantInput2.  The data type of the tag to which the second variant parameter of the instruction is pointing is incorrect. |
| B080_0300 | BadType_VariantInput3:  The data type of the tag to which the third variant parameter of the instruction is pointing is incorrect. |
| B080_0400 | BadType_VariantInput4:  The data type of the tag to which the fourth variant parameter of the instruction is pointing is incorrect. |
| B080_0500 | BadType_VariantInput5:  The data type of the tag to which the fifth variant parameter of the instruction is pointing is incorrect. |
| B080_3100 | BadNumElements_VariantInput1:  Number of array elements in variant 1 is smaller than the number stored in the count parameter of the instruction (e.g. NodeIDCount for OPC_UA_NodeGetHandleList or NamespaceUrisCount for OPC_UA_NamespaceGetIndexList, etc.). |
| B080_3200 | BadNumElements_VariantInput2:  Number of array elements in variant 2 is smaller than the number stored in the count parameter of the instruction. |
| B080_3300 | BadNumElements_VariantInput3:  Number of array elements in variant 3 is smaller than the number stored in the count parameter of the instruction. |
| B080_3400 | BadNumElements_VariantInput4:  Number of array elements in variant 4 is smaller than the number stored in the count parameter of the instruction. |
| B080_3500 | BadNumElements_VariantInput5:  Number of array elements in variant 5 is smaller than the number stored in the count parameter of the instruction. |
| B080_C400 | Simatic_ClientNotEnabled:  The OPC UA client is disabled. |
| B080_C500 | SimaticNothingToDo:  Error during initialization of the client |
| B080_C600 | ClientNotAvailable  Error during initialization of the client |
| B080_0B00 | ArrayElements_TooMany:  The array has too many elements. |
| B080_1100 | ArrayElements_TooMany:  General error code. Occurs when an array has too many elements:  NamespaceUrisCount > MAX_ELEMENTS_NAMESPACES  NodeIDCount > MAX_ELEMENTS_NODELIST  BrowsePathscount > MAX_ELEMENTS_RELATIVEPATH  MethodHdlCount > MAX_ELEMENTS_METHODLIST    MAX_ELEMENTS_NAMESPACES = 20  MAX_ELEMENTS_NODELIST = 300  MAX_ELEMENTS_METHODLIST = 100  MAX_ELEMENTS_BROWSEPATH = 10 |
| B080_1200 | ArrayElements_TooFew |
| B080_2100 | BadValue_VariantInput1:  The value of the tag to which the first variant of the instruction is pointing is incorrect. |
| B080_2200 | BadValue_VariantInput2:  The value of the tag to which the second variant of the instruction is pointing is incorrect. |
| B080_2300 | BadValue_VariantInput3:  The value of the tag to which the third variant of the instruction is pointing is incorrect. |
| B080_2400 | BadValue_VariantInput4:  The value of the tag to which the fourth variant of the instruction is pointing is incorrect. |
| B080_2500 | BadValue_VariantInput5:  The value of the tag to which the fifth variant of the instruction is pointing is incorrect. |
| B080_B000 | TooManyMethods:  Maximum number of server methods or max. number of server method instances exceeded.  (Calls of the instructions OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPost):  Refer to the technical specifications of the CPUs (number of server methods, max.) |
| C080_C300 | InsufficientResources:  Insufficient resources. Either (a) error upon memory allocation or (b) too many SFB instances |

##### Error codes of the OPC Foundation (S7-1500)

Error codes

The following table contains error codes of the OPC Foundation.

The names and explanations of the errors are listed in the original (English) and are selectively supplemented with additional information.

###### Error codes

| Status "Good" (0000_0000 - 3FFF_FFFF) |  |  |
| --- | --- | --- |
| Error code (hex) | Name | Meaning |
| 0000_0000 | Good | Success, no error. |
| 002D_0000 | GoodSubscriptionTransferred | The subscription was transferred to another session. |
| 002E_0000 | GoodCompletesAsynchronously | The processing will complete asynchronously. |
| 002F_0000 | GoodOverload | Sampling has slowed down due to resource limitations. |
| 0030_0000 | GoodClamped | The value written was accepted but was clamped. |
| 0096_0000 | GoodLocalOverride | The value has been overridden. |
| 00A2_0000 | GoodEntryInserted | The data or event was successfully inserted into the historical database. |
| 00A3_0000 | GoodEntryReplaced | The data or event field was successfully replaced in the historical database. |
| 00A5_0000 | GoodNoData | No data exists for the requested time range or event filter. |
| 00A6_0000 | GoodMoreData | The data or event field was successfully replaced in the historical database. |
| 00A7_0000 | GoodCommunicationEvent | The communication layer has raised an event. |
| 00A8_0000 | GoodShutdownEvent | The system is shutting down. |
| 00A9_0000 | GoodCallAgain | The operation is not finished and needs to be called again. |
| 00AA_0000 | GoodNonCriticalTimeout | A non-critical timeout occurred. |
| 00BA_0000 | GoodResultsMayBeIncomplete | The server should have followed a reference to a node in a remote server but did not. The result set may be incomplete. |
| 00D9_0000 | GoodDataIgnored | The request pecifies fields which are not valid for the EventType or cannot be saved by the historian. |
| 00DC_0000 | GoodEdited | The value does not come from the real source and has been edited by the server. |
| 00DD_0000 | GoodPostActionFailed | There was an error in execution of these post-actions. |
| 00E0_0000 | GoodDependentValueChanged | A dependent value has been changed but the change has not been applied to the device. |

| Status "Uncertain" (4000_0000 - 7FFF_FFFF) |  |  |
| --- | --- | --- |
| Error code (hex) | Name | Meaning |
| 406C_0000 | UncertainReferenceOutOfServer | One of the references to follow in the relative path references to a node in the address space in another server. |
| 408F_0000 | UncertainNoCommunicationLastUsableValue | Communication to the data source has failed. The variable value is the last value that had a good quality. |
| 4090_0000 | UncertainLastUsableValue | Whatever was updating this value has stopped doing so. |
| 4091_0000 | UncertainSubstituteValue | The value is an operational value that was manually overwritten. |
| 4092_0000 | UncertainInitialValue | The value is an initial value for a variable that normally receives its value from another variable. |
| 4093_0000 | UncertainSensorNotAccurate | The value is at one of the sensor limits. |
| 4094_0000 | UncertainEngineeringUnitsExceeded | The value is outside of the range of values defined for this parameter. |
| 4095_0000 | UncertainSubNormal | The value is derived from multiple sources and has less than the required number of Good sources. |
| 40A4_0000 | UncertainDataSubNormal | The value is derived from multiple values and has less than the required number of Good values. |
| 40BC_0000 | UncertainReferenceNotDeleted | The server was not able to delete all target references. |
| 40C0_0000 | UncertainNotAllNodesAvailable | The list of references may not be complete because the underlying system is not available. |
| 40DE_0000 | UncertainDominantValueChanged | The related EngineeringUnit has been changed but the Variable Value is still provided based on the previous unit. |
| 40E2_0000 | UncertainDependentValueChanged | A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is uncertain. |

| Status "Bad" (8000_0000 - FFFF_FFFF) |  |  |
| --- | --- | --- |
| Error code (hex) | Name | Meaning |
| 8001_0000 | BadUnexpectedError | An unexpected error occurred |
| 8002_0000 | BadInternalError | An internal error occurred as a result of a programming or configuration error.   **Possible cause**:   You have write-accessed a single element of a tag of data type DTL. Write access to tags of data type DTL is only possible to the complete structure. |
| 8003_0000 | BadOutOfMemory | Not enough memory to complete the operation.   **Possible cause:**   The maximum quantity structure of the OPC UA server has been exceeded.   **Solution:**   Reduce the number of registered OPC UA elements.  Use an OPC UA Server diagnostics tool (such as UaExpert from Unified Automation) to ensure that there are no inactive sessions and subscriptions. As countermeasure you can select corresponding timeouts (Subscription Timeout <= Session Timeout) in the client.  See also the description to the error messages [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| 8004_0000 | BadResourceUnavailable | An operating system resource is not available |
| 8005_0000 | BadCommunicationError | A low level communication error occurred.   **Possible cause:**    The server address (ServerEndpointURL) is incorrect or incomplete.  See also the explanation for this parameter in [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| 8006_0000 | BadEncodingError | Encoding halted because of invalid data in the objects being serialized. |
| 8007_0000 | BadDecodingError | Decoding halted because of invalid data in the stream. |
| 8008_0000 | BadEncodingLimits­Exceeded | The message encoding/decoding limits imposed by the stack have been exceeded. |
| 8009_0000 | BadUnknownResponse | An unrecognized response was received from the server. |
| 80B8_0000 | BadRequestTooLarge | The request message size exceeds limits set by the server. |
| 80B9_0000 | BadResponseTooLarge | The response message size exceeds limits set by the client. |
| 800A_0000 | BadTimeout | The operation timed out.  See also error message at [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| 800B_0000 | BadServiceUnsupported | The server does not support the requested service. |
| 800C_0000 | BadShutdown | The operation was cancelled because the application is shutting down. |
| 800D_0000 | BadServerNotConnected | The operation could not complete because the client is not connected to the server. |
| 800E_0000 | BadServerHalted | The server has stopped and cannot process any requests. |
| 800F_0000 | BadNothingToDo | There was nothing to do because the client passed a list of operations with no elements. |
| 8010_0000 | BadTooManyOperations | The request could not be processed because it specified too many operations.  See also error message at [OPC_UA_NamespaceGetIndexList: Read namespace indexes](#opc_ua_namespacegetindexlist-read-namespace-indexes-s7-1500). |
| 8011_0000 | BadDataTypeIdUnknown | The extension object cannot be (de)serialized because the data type id is not recognized. |
| 8012_0000 | BadCertificateInvalid | The certificate provided as a parameter is not valid. |
| 8013_0000 | BadSecurityChecksFailed | An error occurred verifying security. The certificate provided as a parameter is not valid. |
| 8014_0000 | BadCertificateTimeInvalid | The Certificate has expired or is not yet valid. |
| 8015_0000 | BadCertificateIssuer TimeInvalid | An Issuer Certificate has expired or is not yet valid. |
| 8016_0000 | BadCertificateHost NameInvalid | The HostName used to connect to a Server does not match a HostName in the Certificate. |
| 8017_0000 | BadCertificateUriInvalid | The URI specified in the Application Description does not match the URI in the Certificate. |
| 8018_0000 | BadCertificateUseNotAllowed | The Certificate may not be used for the requested operation. |
| 8019_0000 | BadCertificateIssuerUse NotAllowed | The Issuer Certificate may not be used for the requested operation. |
| 801A_0000 | BadCertificateUntrusted | The Certificate is not trusted. |
| 801B_0000 | BadCertificateRevocation Unknown | It was not possible to determine if the Certificate has been revoked. |
| 801C_0000 | BadCertificateIssuer RevocationUnknown | It was not possible to determine if the Issuer  Certificate has been revoked. |
| 801D_0000 | BadCertificateRevoked | The Certificate has been revoked. |
| 801E_0000 | BadCertificateIssuerRevoked | The Issuer Certificate has been revoked. |
| 801F_0000 | BadUserAccessDenied | User does not have permission to perform the requested operation. |
| 8020_0000 | BadIdentityTokenInvalid | The user identity token is not valid. |
| 8021_0000 | BadIdentityTokenRejected | The user identity token is valid but the server has rejected it. |
| 8022_0000 | BadSecureChannelIdInvalid | The specified secure channel is no longer valid. |
| 8023_0000 | BadInvalidTimestamp | The timestamp is outside the range allowed by the server. |
| 8024_0000 | BadNonceInvalid | The nonce does appear to be not a random value or it is not the correct length. |
| 8025_0000 | BadSessionIdInvalid | The session id is not valid. |
| 8026_0000 | BadSessionClosed | The session was closed by the client. |
| 8027_0000 | BadSessionNotActivated | The session cannot be used because ActivateSession has not been called. |
| 8028_0000 | BadSubscriptionIdInvalid | The subscription id is not valid. |
| 802A_0000 | BadRequestHeaderInvalid | The header for the request is missing or invalid. |
| 802B_0000 | BadTimestampsTo ReturnInvalid | The timestamps to return parameter is invalid. |
| 802C_0000 | BadRequestCancelled ByClient | The request was cancelled by the client. |
| 8031_0000 | BadNoCommunication | Communication with the data source is defined, but not established, and there is no last known value available. |
| 8032_0000 | BadWaitingForInitialData | Waiting for the server to obtain values from the underlying data source. |
| 8033_0000 | BadNodeIdInvalid | The syntax of the node id is not valid. |
| 8034_0000 | BadNodeIdUnknown | The node id refers to a node that does not exist in the server address space.  The NamespaceIndex of the specified NodeId may not exist. If the error code is displayed when the instruction "OPC_UA_MethodCall" is called:   Another possible cause is the use of invalid ObjectIDs in the preceding call of OPC_UA_MethodGetHandleList. The instruction "OPC_UA_MethodGetHandleList" does not evaluate the ObjectIds. |
| 8035_0000 | BadAttributeIdInvalid | The attribute is not supported for the specified Node. |
| 8036_0000 | BadIndexRangeInvalid | The syntax of the index range parameter is invalid. |
| 8037_0000 | BadIndexRangeNoData | No data exists within the range of indexes specified. |
| 8038_0000 | BadDataEncodingInvalid | The data encoding is invalid. |
| 8039_0000 | BadDataEncoding Unsupported | The server does not support the requested data encoding for the node. |
| 803A_0000 | BadNotReadable | The access level does not allow reading or subscribing to the Node. |
| 803B_0000 | BadNotWritable | The access level does not allow writing to the Node. |
| 803C_0000 | BadOutOfRange | The value was out of range.  Possible remedy for arrays: Check whether you can access elements of an array that are undefined. |
| 803D_0000 | BadNotSupported | The requested operation is not supported.    **Possible cause:**    The server address (ServerEndpointURL) is incorrect or incomplete. |
| 803E_0000 | BadNotFound | A requested item was not found or a search operation ended without success. |
| 803F_0000 | BadObjectDeleted | The object cannot be used because it has been deleted. |
| 8040_0000 | BadNotImplemented | Requested operation is not implemented. |
| 8041_0000 | BadMonitoringModeInvalid | The monitoring mode is invalid. |
| 8042_0000 | BadMonitoredItemIdInvalid | The monitoring item id does not refer to a valid monitored item. |
| 8043_0000 | BadMonitoredItem FilterInvalid | The monitored item filter parameter is not valid. |
| 8044_0000 | BadMonitoredItem FilterUnsupported | The server does not support the requested monitored item filter. |
| 8045_0000 | BadFilterNotAllowed | A monitoring filter cannot be used in combination with the attribute specified. |
| 8046_0000 | BadStructureMissing | A mandatory structured parameter was missing or null. |
| 8047_0000 | BadEventFilterInvalid | The event filter is not valid. |
| 8048_0000 | BadContentFilterInvalid | The content filter is not valid. |
| 8049_0000 | BadFilterOperandInvalid | The operand used in a content filter is not valid. |
| 804A_0000 | BadContinuation PointInvalid | The continuation point provide is longer valid. |
| 804B_0000 | BadNoContinuationPoints | The operation could not be processed because all continuation points have been allocated. |
| 804C_0000 | BadReferenceTypeIdInvalid | The operation could not be processed because all continuation points have been allocated. |
| 804D_0000 | BadBrowseDirectionInvalid | The browse direction is not valid. |
| 804E_0000 | BadNodeNotInView | The node is not part of the view. |
| 804F_0000 | BadServerUriInvalid | The ServerUri is not a valid URI. |
| 8050_0000 | BadServerNameMissing | No ServerName was specified |
| 8051_0000 | BadDiscoveryUrlMissing | No DiscoveryUrl was specified. |
| 8052_0000 | BadSempahoreFileMissing | The semaphore file specified by the client is not valid. |
| 8053_0000 | BadRequestTypeInvalid | The security token request type is not valid. |
| 8054_0000 | BadSecurityModeRejected | The security mode does not meet the requirements set by the Server.  Server is setting higher security requirements. Possible remedy: Use a higher security setting for the connection to the server. |
| 8055_0000 | BadSecurityPolicyRejected | The security policy does not meet the requirements set by the Server. |
| 8056_0000 | BadTooManySessions | The server has reached its maximum number of sessions. |
| 8057_0000 | BadUserSignatureInvalid | The user token signature is missing or invalid. |
| 8058_0000 | BadApplicationSignature Invalid | The signature generated with the client certificate is missing or invalid. |
| 8059_0000 | BadNoValidCertificates | The client did not provide at least one software certificate that is valid and meets the profile requirements for the server. |
| 805A_0000 | BadRequestCancelled ByRequest | The request was cancelled by the client with the Cancel service. |
| 805B_0000 | BadParentNodeIdInvalid | The parent node id does not to refer to a valid node. |
| 805C_0000 | BadReferenceNotAllowed | The reference could not be created because it violates constraints imposed by the data model. |
| 805D_0000 | BadNodeIdRejected | The requested node id was reject because it was either invalid or server does not allow node ids to be specified by the client. |
| 805E_0000 | BadNodeIdExists | The requested node id is already used by another node. |
| 805F_0000 | BadNodeClassInvalid | The node class is not valid. |
| 8060_0000 | BadBrowseNameInvalid | The browse name is invalid. |
| 8061_0000 | BadBrowseNameDuplicated | The browse name is not unique among nodes that share the same relationship with the parent. |
| 8062_0000 | BadNodeAttributesInvalid | The node attributes are not valid for the node class. |
| 8063_0000 | BadTypeDefinitionInvalid | The type definition node id does not reference an appropriate type node. |
| 8064_0000 | BadSourceNodeIdInvalid | The source node id does not reference a valid node. |
| 8065_0000 | BadTargetNodeIdInvalid | The target node id does not reference a valid node. |
| 8066_0000 | BadDuplicateReference NotAllowed | The reference type between the nodes is already defined. |
| 8067_0000 | BadInvalidSelfReference | The server does not allow this type of selfreference on this node. |
| 8068_0000 | BadReferenceLocalOnly | The reference type is not valid for a reference to a remote server. |
| 8069_0000 | BadNoDeleteRights | The server will not allow the node to be deleted. |
| 806A_0000 | BadServerIndexInvalid | The server index is not valid. |
| 806B_0000 | BadViewIdUnknown | The view id does not refer to a valid view node. |
| 806D_0000 | BadTooManyMatches | The requested operation has too many matches to return. |
| 806E_0000 | BadQueryTooComplex | The requested operation requires too many resources in the server. |
| 806F_0000 | BadNoMatch | The requested operation has no match to return. |
| 8070_0000 | BadMaxAgeInvalid | The max age parameter is invalid. |
| 8071_0000 | BadHistoryOperationInvalid | The history details parameter is not valid. |
| 8072_0000 | BadHistoryOperation Unsupported | The server does not support the requested operation. |
| 8073_0000 | BadWriteNotSupported | The server not does support writing the combination of value, status and timestamps provided. |
| 8074_0000 | BadTypeMismatch | The value supplied for the attribute is not of the same type as the attribute's value. |
| 8075_0000 | BadMethodInvalid | The method id does not refer to a method for the specified object. |
| 8076_0000 | BadArgumentsMissing | The client did not specify all of the input arguments for the method. |
| 8077_0000 | BadTooManySubscriptions | The server has reached its maximum number of subscriptions.   **Possible cause:**   Maximum number of subscriptions is exceeded   **Solution:**   Create a subscription in a new session. |
| 8078_0000 | BadTooManyPublish Requests | The server has reached the maximum number of queued publish requests. |
| 8079_0000 | BadNoSubscription | There is no subscription available for this session. |
| 807A_0000 | BadSequenceNumber Unknown | The sequence number is unknown to the server. |
| 807B_0000 | BadMessageNotAvailable | The requested notification message is no longer available. |
| 807C_0000 | BadInsufficientClientProfile | The Client of the current Session does not support one or more Profiles that are necessary for the Subscription. |
| 80BF_0000 | BadStateNotActive | The sub-state machine is not currently active. |
| 807D_0000 | BadTcpServerTooBusy | The server cannot process the request because it is too busy. |
| 807E_0000 | BadTcpMessageTypeInvalid | The type of the message specified in the header invalid. |
| 807F_0000 | BadTcpSecureChannel Unknown | The SecureChannelId and/or TokenId are not currently in use. |
| 8080_0000 | BadTcpMessageTooLarge | The size of the message specified in the header is too large. |
| 8081_0000 | BadTcpNotEnough Resources | There are not enough resources to process the request.  See also error message at [OPC_UA_Connect: Create connection](#opc_ua_connect-create-connection). |
| 8082_0000 | BadTcpInternalError | An internal error occurred. |
| 8083_0000 | BadTcpEndpointUrlInvalid | The Server does not recognize the QueryString specified. |
| 8084_0000 | BadRequestInterrupted | The request could not be sent because of a network interruption. |
| 8085_0000 | BadRequestTimeout | Timeout occurred while processing the request. |
| 8086_0000 | BadSecureChannelClosed | The secure channel has been closed. |
| 8087_0000 | BadSecureChannelToken Unknown | The token has expired or is not recognized. |
| 8088_0000 | BadSequenceNumberInvalid | The sequence number is not valid. |
| 8089_0000 | BadConfigurationError | There is a problem with the configuration that affects the usefulness of the value. |
| 808A_0000 | BadNotConnected | The variable should receive its value from another variable, but has never been configured to do so. |
| 808B_0000 | BadDeviceFailure | There has been a failure in the device/data source that generates the value that has affected the value. |
| 808C_0000 | BadSensorFailure | There has been a failure in the sensor from which the value is derived by the device/data source. |
| 808D_0000 | BadOutOfService | The source of the data is not operational. |
| 808E_0000 | BadDeadbandFilterInvalid | The dead band filter is not valid. |
| 8097_0000 | BadRefreshInProgress | This Condition refresh failed, a Condition refresh operation is already in progress. |
| 8098_0000 | BadConditionAlreadyDisabled | This condition has already been disabled. |
| 8099_0000 | BadConditionDisabled | Property not available, this condition is disabled. |
| 809A_0000 | BadEventIdUnknown | The specified event id is not recognized. |
| 809B_0000 | BadNoData | No data exists for the requested time range or event filter. |
| 809D_0000 | BadDataLost | Data is missing due to collection started/stopped/lost. |
| 809E_0000 | BadDataUnavailable | Expected data is unavailable for the requested time range due to an unmounted volume an off-line archive or tape or similar reason for temporary unavailability. |
| 809F_0000 | BadEntryExists | The data or event was not successfully inserted because a matching entry exists. |
| 80A0_0000 | BadNoEntryExists | The data or event was not successfully updated because no matching entry exists. |
| 80A1_0000 | BadTimestampNotSupported | The client requested history using a timestamp format the server does not support (i. e. requested ServerTimestamp when server only supports SourceTimestamp). |
| 80AB_0000 | BadInvalidArgument | One or more arguments are invalid.   **Possible cause:**    The server address (ServerEndpointURL) is incorrect or incomplete. |
| 80AC_0000 | BadConnectionRejected | Could not establish a network connection to remote server. |
| 80AD_0000 | BadDisconnect | The server has disconnected from the client. |
| 80AE_0000 | BadConnectionClosed | The network connection has been closed.  The connection with the corresponding ConnectionHdl has the "ShutDown" status (connection terminated). The connection/session could not be "reactivated" automatically. Possible cause: Session deleted on the server, e.g. due to restart or timeout.  In this case, you must explicitly close the connection with the instruction "OPC_UA_Disconnect" and thereby release the connection resources again. In your user program, you must reset the ConnectionHdl for this connection which has become invalid.   Then you have to establish a new connection to the server (see instruction "OPC_UA_Connect").  The error code can occur in all client instructions except the OPC_UA_Connect, OPC_UA_Disconnect, and OPC_UA_ConnectionGetStatus instructions. |
| 80AF_0000 | BadInvalidState | The operation cannot be completed because the object is closed uninitialized or in some other invalid state.  The connection with the corresponding ConnectionHdl has the "ConnectionError" status (temporary connection error, connection interrupted). The CPU tries to "reactivate" the connection. If this does not succeed within the set timeout interval (OPC UA Session Timeout), the connection goes into the "Shutdown" state. Requirements for the state transition: The CPU was able to reach the OPC UA server to check whether or not the session is still active.   The error code can occur in all client instructions except the OPC_UA_Connect, OPC_UA_Disconnect, and OPC_UA_ConnectionGetStatus instructions. |
| 80B0_0000 | BadEndOfStream | Cannot move beyond end of the stream. |
| 80B1_0000 | BadNoDataAvailable | No data is currently available for reading from a non-blocking stream. |
| 80B2_0000 | BadWaitingForResponse | The asynchronous operation is waiting for a response. |
| 80B3_0000 | BadOperationAbandoned | The asynchronous operation was abandoned by the caller. |
| 80B4_0000 | BadExpectedStreamToBlock | The stream did not return all data requested (possibly because it is a non-blocking stream). |
| 80B5_0000 | BadWouldBlock | Non-blocking behavior is required and the operation would block. |
| 80B6_0000 | BadSyntaxError | A value had an invalid syntax. |
| 80B7_0000 | BadMaxConnections Reached | The operation could not be finished because all available connections are in use. |
| 80BB_0000 | BadEventNot Acknowledgeable | The event cannot be acknowledged. |
| 80BD_0000 | BadInvalidTimestamp Argument | The defined timestamp to return was invalid. |
| 80BE_0000 | BadProtocolVersion Unsupported | The applications do not have compatible protocol versions. |
| 80C1_0000 | BadFilterOperatorInvalid | An unrecognized operator was provided in a filter. |
| 80C2_0000 | BadFilterOperator Unsupported | A valid operator was provided, but the server does not provide support for this filter operator. |
| 80C3_0000 | BadFilterOperandCount Mismatch | The number of operands provided for the filter operator was less than expected for the operand provided. |
| 80C4_0000 | BadFilterElementInvalid | The referenced element is not a valid element in the content filter. |
| 80C5_0000 | BadFilterLiteralInvalid | The referenced literal is not a valid value. |
| 80C6_0000 | BadIdentityChangeNotSupported | The Server does not support changing the user identity assigned to the session. |
| 80C8_0000 | BadNotTypeDefinition | The provided NodeId was not a type definition NodeId. |
| 80C9_0000 | BadViewTimestampInvalid | The view timestamp is not available or not supported. |
| 80CA_0000 | BadViewParameterMismatch | The view parameters are not consistent with each other. |
| 80CB_0000 | BadViewVersionInvalid | The view version is not available or not supported. |
| 80CC_0000 | BadConditionAlready Enabled | This condition has already been enabled. |
| 80CD_0000 | BadDialogNotActive | The dialog condition is not active. |
| 80CE_0000 | BadDialogResponseInvalid | The response is not valid for the dialog. |
| 80CF_0000 | BadConditionBranch AlreadyAcked | The condition branch has already been acknowledged. |
| 80D0_0000 | BadConditionBranch AlreadyConfirmed | The condition branch has already been confirmed. |
| 80D1_0000 | BadConditionAlreadyShelved | The condition has already been shelved. |
| 80D2_0000 | BadConditionNotShelved | The condition is not currently shelved. |
| 80D3_0000 | BadShelvingTimeOutOfRange | The shelving time not within an acceptable range. |
| 80D4_0000 | BadAggregateListMismatch | The requested number of Aggregates does not match the requested number of NodeIds. |
| 80D5_0000 | BadAggregateNotSupported | The requested Aggregate is not support by the server. |
| 80D6_0000 | BadAggregateInvalidInputs | The aggregate value could not be derived due to invalid data inputs. |
| 80DB_0000 | BadTooManyMonitoredItems | The request could not be processed because there are too many monitored items in the subscription.   **Possible cause:**   The maximum number of supervised elements has been reached in a subscription.   **Solution:**   To register additional elements, you must create a new subscription.   For projects as of TIA Portal V15 and higher, you can also set the maximum number of supervised elements in the CPU configuration.   **Additional possible cause:**   Request with too many elements    **Solution:**   Note the maximum values specified on the server in the "ServerCapabilities" object. |
| 80D7_0000 | BadBoundNotFound | No data found to provide upper or lower bound value. |
| 80D8_0000 | BadBoundNotSupported | The server cannot retrieve a bound for the variable. |
| 80DA_0000 | BadAggregateConfiguration Rejected | The aggregate configuration is not valid for specified node. |
| 80E1_0000 | BadDominantValueChanged | The related EngineeringUnit has been changed but this change has not been applied to the device. The Variable Value is still dependent on the previous unit but its status is currently bad. |
| 80E3_0000 | BadDependentValueChanged | A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is bad. |
| 80E4_0000 | BadRequestNotAllowed | The request was rejected by the server because it did not meet the criteria set by the server. |
| 80E5_0000 | BadTooManyArguments | Too many arguments were provided. |
| 80E6_0000 | BadSecurityModeInsufficient | The operation is not permitted over the current secure channel. |
| 810D_0000 | BadCertificateChainIncomplete | The certificate chain is incomplete. |
| 810E_0000 | BadLicenseExpired | The server requires a license to operate in general or to perform a service or operation, but existing license is expired. |
| 810F_0000 | BadLicenseLimitsExceeded | The server has limits on number of allowed operations / objects, based on installed licenses, and these limits where exceeded. |
| 8110_0000 | BadLicenseNotAvailable | The server does not have a license which is required to operate in general or to perform a service or operation. |
| 8111_0000 | BadNotExecutable | The executable attribute does not allow the execution of the method. |
| 8112_0000 | BadNumericOverflow | The number was not accepted because of a numeric overflow. |
| 8113_0000 | BadRequestNotComplete | The request has not been processed by the server yet. |

##### PLCopen error codes (S7-1500)

###### Error codes

The following table contains PLCopen error codes.

The names and explanations of the errors are listed in the original. They are only available in English.

###### PLCopen error codes

| ErrorID (hex) | Name | Meaning |
| --- | --- | --- |
| A000_0001 | PLCopenUA_Bad_FW_ PermanentError | Internal, permanent error. |
| A000_0002 | PLCopenUA_Bad_FW_ TempError | Temp. Error; FB could retry to reach FW. |
| A000_0100 | PLCopenUA_Bad_ ConnectionError | Connection could not be established. |
| A000_0101 | PLCopenUA_Bad_ HostNotFound | The requested hostname could not be found. |
| A000_0102 | PLCopenUA_Bad_ AlreadyConnected | Connection was already established. |
| A000_0103 | PLCopenUA_Bad_ SecurityFailed | Connection failed due to security setup. |
| A000_0104 | PLCopenUA_Bad_ Suspended | Connection is suspended. |
| A000_0105 | PLCopenUA_Bad_ ConnectionInvalidHdl | Provided ConnectionHdl is not known.  The connection handle (ConnectionHdl) is invalid / unknown.   The error code can occur in all client instructions except the OPC_UA_Connect instruction.  Additional information can be found in the description of the error codes of the instruction "OPC_UA_ConnectionGetStatus" |
| A000_0200 | PLCopenUA_Bad_ NSNotFound | A namespace with the requested name cannot be found on server. |
| A000_0300 | PLCopenUA_Bad_ ResultTooLong | Target PLC variable is too short for retrieved data. |
| A000_0301 | PLCopenUA_Bad_ InvalidType | Invalid or unsupported Type. |
| A000_0302 | PLCopenUA_Bad_ NodeInvalidHdl | Provided NodeHdl is not known. |
| A000_0303 | PLCopenUA_Bad_ MethodInvalidHdl | Provided MethodHdl is not known. |
| A000_0304 | PLCopenUA_Bad_ ReadFailed | Read failed for unknown reason. |
| A000_0305 | PLCopenUA_Bad_ WriteFailed | Write failed for unknown reason. |
| A000_0306 | PLCopenUA_Bad_ CallFailed | Method Call failed for unknown reason. |
| A000_0307 | PLCopenUA_Bad_ InParamFailed | Method Call Input parameter conversion failed. |
| A000_0308 | PLCopenUA_Bad_ OutParamFailed | Method Call Output parameter conversion failed. ATTENTION: this means the MethodCall was executed successfully but the returned values could not be converted. |
| A000_0500 | PLCopenUA_Bad_ SubscriptionInvalidHdl | Provided SubscriptionHdl is not known. |
| A000_0501 | PLCopenUA_Bad_ MonitoredItemInvalidHdl | Provided MonitoredItemHdl is not known. |

#### Example programs for OPC UA clients (S7-1500)

This section contains information on the following topics:

- [Preliminary remarks (S7-1500)](#preliminary-remarks-s7-1500)
- [Example program for OPC_UA_ConnectionGetStatus (S7-1500)](#example-program-for-opc_ua_connectiongetstatus-s7-1500)
- [Program example for reading PLC tags (S7-1500)](#program-example-for-reading-plc-tags-s7-1500)
- [Example program for writing PLC tags (S7-1500)](#example-program-for-writing-plc-tags-s7-1500)
- [Example program for OPC_UA_TranslatePathList (S7-1500)](#example-program-for-opc_ua_translatepathlist-s7-1500)
- [Example program for calling a method of an OPC UA server (S7-1500)](#example-program-for-calling-a-method-of-an-opc-ua-server-s7-1500)

##### Preliminary remarks (S7-1500)

The example function blocks "Call_OpenDoor_On_Productionline", "ReadFromProductionline" and "WriteToProductionline" only illustrate the individual functions and are not designed for common use. They can therefore only run individually.

Each FB establishes its own connection with the OPC_UA_Connect instruction and accesses the same client interface and thus the DB "Productionline_Configuration".

The connection handles of the three connections are stored in the same tag when used together and overwrite each other.

Take this fact into account when using all the functions described in your project.

##### Example program for OPC_UA_ConnectionGetStatus (S7-1500)

###### Example program for analyzing connections

This section includes the complete program code for the example program "Analyze_Connection".

The example shows you how a user program uses the instruction "OPC_UA_ConnectionGetStatus" to get information about a connection to an OPC UA server.

You can find a description of the "OPC_UA_ConnectionGetStatus" instruction in section [OPC_UA_ConnectionGetStatus: Read connection status](#opc_ua_connectiongetstatus-read-connection-status-s7-1500).

**Program structure**

The program operates as OPC UA client and comprises the following sections:

1. Establishing a connection to an OPC UA server.
2. Analyzing the connection.
3. Terminating the connection to the OPC UA server.

You start the program with a positive edge at "Input_REQ".

###### Declaration

The following figure shows the declaration of local tags of a function block that uses the instruction "OPC_UA_ConnectionGetStatus":

![Declaration](images/115328671371_DV_resource.Stream@PNG-de-DE.png)

###### Program

SCL

IF #Run = FALSE THEN

    #Started := #Input_REQ AND NOT #Mem_Input_REQ;

    #Mem_Input_REQ := #Input_REQ;

    IF #Started THEN

        #Output_Busy := TRUE;

        #Output_Done := FALSE;

        #Output_Error := FALSE;

        #State := 1;

        #Run := TRUE;

        #ResetREQ_For_OPC_UA_Disconnect := TRUE;

        #SetServerEndpoint := TRUE;

    END_IF;

END_IF;

IF #Run = TRUE THEN

    CASE #State OF

        1: // case 1, connect to server

        IF #SetServerEndpoint = TRUE THEN

           #SetServerEndpoint := FALSE;

           //set ServerSendpoint

           #ServerEndpointUrl := WSTRING#'opc.tcp://192.168.1.1:4840';

           //setting for SecurityMsgMode

           //1 = None

           //2 = Sign

           //3 = Sign & Encrypt

           #OPC_UA_SessionConnectInfo_Instance.SecurityMsgMode := 3;

           //setting for SecurityPolicy

           //1 = None

           //2 = Basic128Rsa15

           //3 = Basic256

           //4 = Basic256Sha256

           #OPC_UA_SessionConnectInfo_Instance.SecurityPolicy := 4;

           //set TransportProfile to 1

           #OPC_UA_SessionConnectInfo_Instance.TransportProfile := 1;

           //we are using our Client-Certificate Nr. 10

           //because Nr. 10 is the lastest Certificate we created for our client application

           //please look into Certificate manager for the number of your Client certificate

           //Certificate manager is located at

           // "Project tree > Security settings > Security features"

           #OPC_UA_SessionConnectInfo_Instance.CertificateID := 10;

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_Connect_Instance(REQ := #Req,

                ServerEndpointUrl := #ServerEndpointUrl,

                SessionConnectInfo := #OPC_UA_SessionConnectInfo_Instance,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status,

                ConnectionHdl => #ConnectionHdl);

        IF #Done = TRUE THEN

           #State := #State + 1;

           #ResetREQ_For_OPC_UA_Disconnect := TRUE;

        END_IF;

        IF #Error = TRUE THEN

           // Did we get a connection handle?

           IF #ConnectionHdl <> 0 THEN

              // We have to release all resources in the server and disconnect

              #State := 100;

           ELSE

              #State := 99;

           END_IF;

           #Mem_Status := #Status;

           #OPC_UA_Connect_Instance(REQ := FALSE,

                ServerEndpointUrl := #ServerEndpointUrl,

                SessionConnectInfo := #OPC_UA_SessionConnectInfo_Instance);

           #ResetREQ_For_OPC_UA_Disconnect := TRUE;

           END_IF;

        2: // case 2, analyse connection

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_ConnectionGetStatus_Instance(REQ := #Req,

               ConnectionHdl := #ConnectionHdl,

               ConnectionStatus => #ConnectionStatus,

               ServerState => #ServerState,

               ServiceLevel => #ServiceLevel,

               Timeout := T#6S,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

        IF #Done = TRUE THEN

              #State := #State + 1;

        END_IF;

        IF #Error = TRUE THEN

              #State := 100;

              #Mem_Status := #Status;

              #OPC_UA_ConnectionGetStatus_Instance(REQ := FALSE,

                       ConnectionHdl := #ConnectionHdl);

        END_IF;

        3: // case 3, disconnect from server

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_Disconnect_Instance(REQ := #Req,

               ConnectionHdl := #ConnectionHdl,

               Timeout := T#6S,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

        IF #Done = TRUE THEN

            #State := #State + 1;

        END_IF;

        IF #Error = TRUE THEN

            #State := 100;

            #Mem_Status := #Status;

            #OPC_UA_Disconnect_Instance(REQ := FALSE,

            ConnectionHdl := #ConnectionHdl);

        END_IF;

        4: //case = 4, function block has run successfully

            #Output_Done := TRUE;

            #Output_Busy := FALSE;

            #State := 0;

            #Mem_Input_REQ := FALSE;

            #Run := FALSE;

            #Started := FALSE;

        99: // ERROR handling

            #Output_Error := TRUE;

            #Output_Status := #Mem_Status;

            #State := 0;

            #Output_Busy := FALSE;

            #Run := FALSE;

            #Mem_Input_REQ := FALSE;

            #Started := FALSE;

    100: // ERROR handling, disconnect from server to release resources (handles)

            IF #ResetREQ_For_OPC_UA_Disconnect = TRUE THEN

               #ResetREQ_For_OPC_UA_Disconnect := FALSE;

            //set REQ to FALSE

               #OPC_UA_Disconnect_Instance(REQ := FALSE,

               ConnectionHdl := #ConnectionHdl);

            END_IF;

            IF #Busy = FALSE THEN

               #Req := TRUE;

            ELSE

               #Req := FALSE;

            END_IF;

            #OPC_UA_Disconnect_Instance(REQ := #Req,

                 ConnectionHdl := #ConnectionHdl,

                 Timeout := T#6S,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

            IF #Done = TRUE THEN

                 #Output_Error := TRUE;

                 #Output_Status := #Mem_Status;

                 #State := 0;

                 #Output_Busy := FALSE;

                 #Run := FALSE;

                 #Mem_Input_REQ := FALSE;

                 #Started := FALSE;

            END_IF;

            IF #Error = TRUE THEN

                 #Output_Error_Message := WString#'Error handling: Resources cannot be released!';

                 #Output_Error := TRUE;

                 #Output_Status := #Mem_Status;

                 #State := 0;

                 #Output_Busy := FALSE;

                 #Run := FALSE;

                 #Mem_Input_REQ := FALSE;

                 #Started := FALSE;

            END_IF;

    END_CASE;

END_IF;

##### Program example for reading PLC tags (S7-1500)

###### Example program for reading PLC tags

This section includes the complete program code for the example program "ReadFromProductionline".

The example shows you how a user program reads the values of PLC tags.

**Program structure**

The program operates as OPC UA client and comprises the following steps:

1. Establishing a connection to the OPC UA server of the CPU from which the values are to be read.
2. Reading the values.
3. Terminating the connection to the OPC UA server.

You start the program with a positive edge at "Input_REQ".

###### Requirements

The example program assumes that you have configured a client interface called "Productionline" and that the following data blocks are available:

- Productionline_Configuration
- Productionline_Data

STEP 7 (TIA Portal) generates these data blocks automatically if you have created a client interface, see [Creating client interfaces](Configuring%20automation%20systems.md#creating-client-interfaces-s7-1500-s7-1500t).

In addition, the example program requires that you have created and configured a connection to the OPC UA server, see [Creating and configuring connections](Configuring%20automation%20systems.md#creating-and-configuring-connections-s7-1500-s7-1500t).

###### Declaration

The following figure shows the declaration of local tags for the function block "ReadFromProductionline".

![Declaration](images/110396460555_DV_resource.Stream@PNG-de-DE.png)

###### Program

SCL

IF #Run = FALSE THEN

    Started := #Input_REQ AND NOT #Mem_Input_REQ;

    #Mem_Input_REQ := #Input_REQ;

    IF #Started THEN

        #Output_Busy := TRUE;

        #Output_Done := FALSE;

        #Output_Error := FALSE;

        #Output_Status := 0;

        #State := 1;

        #Run := TRUE;

        #Set_REQ_To_FALSE := TRUE;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    END_IF;

END_IF;

IF #Run = TRUE THEN

CASE #State OF

    1: // case 1, connect to server

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_Connect_Instance(REQ := #Req,

                 ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

                 SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status,

                 ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

    IF #Done = TRUE THEN

             #State := #State + 1;

    END_IF;

    IF #Error = TRUE THEN

        // Did we get a connection handle?

        IF "Productionline_Configuration".Connection.ConnectionHdl <> 0 THEN

        // We have to release all resources in the server and disconnect

               #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

        ELSE

               #State := 99;

        END_IF;

        #Mem_Status := #Status;

        // set parameter REQ of OPC_UA_Connect to FALSE

        #OPC_UA_Connect_Instance(REQ := FALSE,

               ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

               SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

    END_IF;

    2: // case 2, get index for namespace

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_NamespaceGetIndexList_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

                 NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

                 NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

    IF #Done = TRUE THEN

        IF "Productionline_Configuration".Namespaces.NamespaceStatusList[0] = 0 THEN

               #State := #State + 1;

        ELSE

               #State := 100;

               #Mem_Status := #Status;

               #Output_Error_Message := WString#'Error at NamespaceGetIndexList';

        END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_NamespaceGetIndexList_Instance(REQ := FALSE,

                 NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

                 StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

                 NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes);

    END_IF;

    3: // case 3, get handles for nodes

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_NodeGetHandleList_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeIDCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeIDs := "Productionline_Configuration".ReadLists."ReadListProduct".Nodes,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

                 NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

    IF #Done = TRUE THEN

        IF "Productionline_Data"."ReadListProduct".NodeStatusList[0] = 0 AND   
        "Productionline_Data"."ReadListProduct".NodeStatusList[1] = 0

        THEN

        #State := #State + 1;

        ELSE

        #State := 100;

        #Mem_Status := #Status;

        #Output_Error_Message := WString#'Error at NodeGetHandleList';

        END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #OPC_UA_NodeGetHandleList_Instance(REQ := FALSE,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeIDCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeIDs := "Productionline_Configuration".ReadLists."ReadListProduct".Nodes,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

                 NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls);

    END_IF;

    4: // case 4, read from nodes

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_ReadList_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                 TimeStamps := "Productionline_Data"."ReadListProduct".TimeStamps,

                 Variable := "Productionline_Data"."ReadListProduct".Variable,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

    IF #Done = TRUE THEN

        FOR #i := 0 TO UINT_TO_INT("Productionline_Configuration".ReadLists."ReadListProduct".NodeCount) - 1 DO

                 IF NOT ("Productionline_Data"."ReadListProduct".NodeStatusList[#i] = 0) THEN

                 #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at Readlist "ReadListProduct",

                 Index: ',IN2 := INT_TO_WSTRING(#i));

                 END_IF;

        END_FOR;

        #State := #State + 1;

    END_IF;

        IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_ReadList_Instance(REQ := FALSE,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                 TimeStamps := "Productionline_Data"."ReadListProduct".TimeStamps,

                 Variable := "Productionline_Data"."ReadListProduct".Variable);

    END_IF;

    5: // case 5, release node handles

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_NodeReleaseHandleList_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList,

                 Done => #Done,

                 Error => #Error,

                 Busy => #Busy,

                 Status => #Status);

    IF #Done = TRUE THEN

        IF "Productionline_Data"."ReadListProduct".NodeStatusList[0] = 0 AND

        "Productionline_Data"."ReadListProduct".NodeStatusList[1] = 0

        THEN

                 #State := #State + 1;

        ELSE

                 #State := 100;

                 //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

                 #Set_REQ_To_FALSE := TRUE;

                 #Mem_Status := #Status;

                 #Output_Error_Message := WString#'Error at NodeReleaseHandleList';

        END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_NodeReleaseHandleList_Instance(REQ := FALSE,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 NodeHdlCount := "Productionline_Configuration".ReadLists."ReadListProduct".NodeCount,

                 NodeHdls := "Productionline_Configuration".ReadLists."ReadListProduct".NodeHdls,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 NodeStatusList := "Productionline_Data"."ReadListProduct".NodeStatusList);

    END_IF;

    6: // case 6, disconnect from server

    IF #Busy = FALSE THEN

#Req := TRUE;

    ELSE

#Req := FALSE;

    END_IF;

    #OPC_UA_Disconnect_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

    IF #Done = TRUE THEN

#State := #State + 1;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

    END_IF;

    7: //case = 7, function block has run successfully

        #Output_Done := TRUE;

        #Output_Busy := FALSE;

        #State := 0;

        #Mem_Input_REQ := FALSE;

        #Run := FALSE;

        #Started := FALSE;

    99: // ERROR handling

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;

    100: // ERROR handling, disconnect from server to release resources (handles)

    IF #Set_REQ_To_FALSE = TRUE THEN

        #Set_REQ_To_FALSE := FALSE;

        //set REQ to FALSE

        #OPC_UA_Disconnect_Instance(REQ := FALSE,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout);

    END_IF;

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_Disconnect_Instance(REQ := #Req,

                 ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                 Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

                 Done => #Done,

                 Busy => #Busy,

                 Error => #Error,

                 Status => #Status);

    IF #Done = TRUE THEN

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;

    END_IF;

    IF #Error = TRUE THEN

        #Output_Error_Message := WString#'Error handling: Resources cannot be released!';

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;

    END_IF;

END_CASE;

END_IF;

##### Example program for writing PLC tags (S7-1500)

###### Example program for writing PLC tags

This section includes the complete program code for the example program "WriteToProductionline".

The example shows you how a user program writes the values of PLC tags.

**Program structure**

The program operates as OPC UA client and comprises the following steps:

1. Establishing a connection to the OPC UA server of the CPU to which the values are to be written.
2. Writing the values
3. Terminating the connection to the OPC UA server

You start the program with a positive edge at "Input_REQ".

###### Declaration

The following figure shows the declaration of local tags for the function block "WriteToProductionline".

![Declaration](images/110392497675_DV_resource.Stream@PNG-de-DE.png)

The example program also uses the following data blocks:

- Productionline_Configuration
- Productionline_Data

These data blocks are automatically created by STEP 7 (TIA Portal) because the example program uses the parameter assignment for OPC UA.

###### Program

SCL

IF #Run = FALSE THEN

    #Started := #Input_REQ AND NOT #Mem_Input_REQ;

    #Mem_Input_REQ := #Input_REQ;

    IF #Started THEN

        #Output_Busy := TRUE;

        #Output_Done := FALSE;

        #Output_Error := FALSE;

        #Output_Status := 0;

        #State := 1;

        #Run := TRUE;

        #Set_REQ_To_FALSE := TRUE;      //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    END_IF;

END_IF;

IF #Run = TRUE THEN

    CASE #State OF

    1: // case 1, connect to server

    IF #Busy = FALSE THEN

              #Req := TRUE;

    ELSE

              #Req := FALSE;

    END_IF;

    #OPC_UA_Connect_Instance(REQ := #Req,

              ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

              SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status => #Status,

              ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

    IF #Done = TRUE THEN

        #State := #State + 1;

    END_IF;

    IF #Error = TRUE THEN

    // Did we get a connection handle?

        IF "Productionline_Configuration".Connection.ConnectionHdl <> 0 THEN

        // We have to release all resources in the server and disconnect

              #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

              #Set_REQ_To_FALSE := TRUE;

        ELSE

              #State := 99;

        END_IF;

        #Mem_Status := #Status;

        #OPC_UA_Connect_Instance(REQ := FALSE,

              ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

              SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

    END_IF;

    2: // case 2, get index for namespace

    IF #Busy = FALSE THEN

              #Req := TRUE;

    ELSE

              #Req := FALSE;

    END_IF;

    #OPC_UA_NamespaceGetIndexList_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

              NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

              NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

              Done => #Done,

              Busy => #Busy,

              Error => #Error);

    IF #Done = TRUE THEN

              IF "Productionline_Configuration".Namespaces.NamespaceStatusList[0] = 0 THEN

                    #State := #State + 1;

              ELSE

                    #State := 100;

                    #Mem_Status := #Status;

                    #Output_Error_Message := WString#'Error at NamespaceGetIndexList';

              END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_NamespaceGetIndexList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

              NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

              NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes);

    END_IF;

    3: // case 3, get handles for nodes

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_NodeGetHandleList_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeIDCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeIDs := "Productionline_Configuration".WriteLists."WriteListStatus".Nodes,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

              NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status =>#Status);

    IF #Done = TRUE THEN

        IF "Productionline_Data"."WriteListStatus".NodeStatusList[0] = 0

        THEN

              #State := #State + 1;

        ELSE

              #State := 100;

              #Mem_Status := #Status;

              #Output_Error_Message := WString#'Error at NodeGetHandleList';

        END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_NodeGetHandleList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeIDCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeIDs := "Productionline_Configuration".WriteLists."WriteListStatus".Nodes,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

              NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls);

    END_IF;

    4: // case 4; write value to PLC variable "ProductionEnabled"

    IF #SetProductionEnabled = TRUE THEN

        #SetProductionEnabled := FALSE;

        //set new value to true

        "Productionline_Data"."WriteListStatus".Variable.ProductionEnabled := TRUE;

    END_IF;

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_WriteList_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              Variable := "Productionline_Data"."WriteListStatus".Variable,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status => #Status);

    IF #Done = TRUE THEN

        FOR #i := 0 TO UINT_TO_INT("Productionline_Configuration".WriteLists.WriteListStatus.NodeCount) - 1 DO

              IF NOT ("Productionline_Data"."WriteListStatus".NodeStatusList[#i] = 0) THEN

              #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at Writelist "WriteListStauts", Index: ',

                          IN2 := INT_TO_WSTRING(#i));

              END_IF;

        END_FOR;

        #State := #State + 1;

    END_IF;

   IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_WriteList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              Variable := "Productionline_Data"."WriteListStatus".Variable);

   END_IF;

    5: // case 5, release node handles

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_NodeReleaseHandleList_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status => #Status);

    IF #Done = TRUE THEN

        IF "Productionline_Data"."WriteListStatus".NodeStatusList[0] = 0

        THEN

              #State := #State + 1;

        ELSE

              #State := 100;

              #Mem_Status := #Status;

              #Output_Error_Message := WString#'Error at NodeReleaseHandleList';

        END_IF;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

        #OPC_UA_NodeReleaseHandleList_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              NodeHdlCount := "Productionline_Configuration".WriteLists."WriteListStatus".NodeCount,

              NodeHdls := "Productionline_Configuration".WriteLists."WriteListStatus".NodeHdls,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              NodeStatusList := "Productionline_Data"."WriteListStatus".NodeStatusList);

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

    END_IF;

    6: // case 6, disconnect from server

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_Disconnect_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status => #Status);

    IF #Done = TRUE THEN

#State := #State + 1;

    END_IF;

    IF #Error = TRUE THEN

        #State := 100;

        //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

        #Set_REQ_To_FALSE := TRUE;

        #Mem_Status := #Status;

    END_IF;

    7: //case = 7, function block has run successfully

        #Output_Done := TRUE;

        #Output_Busy := FALSE;

        #State := 0;

        #Mem_Input_REQ := FALSE;

        #Run := FALSE;

        #Started := FALSE;

    99: // ERROR handling

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;

    100: // ERROR handling, disconnect from server to release resources (handles)

    IF #Set_REQ_To_FALSE = TRUE THEN

        #Set_REQ_To_FALSE := FALSE;

        //set REQ to FALSE

        #OPC_UA_Disconnect_Instance(REQ := FALSE,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout);

    END_IF;

    IF #Busy = FALSE THEN

        #Req := TRUE;

    ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_Disconnect_Instance(REQ := #Req,

              ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              Done => #Done,

              Busy => #Busy,

              Error => #Error,

              Status => #Status);

    IF #Done = TRUE THEN

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;

    END_IF;

    IF #Error = TRUE THEN

        #Output_Error_Message := WString#'Error handling: Resources cannot be released!';

        #Output_Error := TRUE;

        #Output_Status := #Mem_Status;

        #State := 0;

        #Output_Busy := FALSE;

        #Run := FALSE;

        #Mem_Input_REQ := FALSE;

        #Started := FALSE;  
    END_IF;

    END_CASE;

END_IF;

##### Example program for OPC_UA_TranslatePathList (S7-1500)

###### Example program for the instruction "OPC_UA_TranslatePathList"

This section includes the complete program code for the example program "Read_From_RfidReader_Door_1".

The example shows you how a user program uses the instruction "OPC_UA_TranslatePathList" to get the NodeIds of nodes and then read the values of these nodes.

You can find a description of the "OPC_UA_TranslatePathList" instruction in section [OPC_UA_TranslatePathList: Determine current NodeIds](#opc_ua_translatepathlist-determine-current-nodeids-s7-1500).

**Program structure**

The program operates as OPC UA client and comprises the following steps:

1. Establishing a connection to the OPC UA server of the CPU from which the values are to be read.
2. Reading the values.
3. Terminating the connection to the OPC UA server.

You start the program with a positive edge at "Input_REQ".

###### Declaration

The following figure shows the declaration of local tags of the function block "Read_From_RfidReader_Door_1" that uses the instruction "OPC_UA_TanslatePathList":

![Declaration](images/114224587275_DV_resource.Stream@PNG-de-DE.png)

![Declaration](images/114224591243_DV_resource.Stream@PNG-de-DE.png)

###### "UDT_Variable" data type for the values read

The local tag "Variable" (see line 43 in the picture above) uses the data type "UDT_Variable".

To enable the example program to insert the values for "DeviceInfo" and "DeviceStatus" into the "Variable" tag, you need to create the user-defined data type "UDT_Variable" in your TIA Portal project.

The following figure shows the structure of the "UDT_Variable" data type:

!["UDT_Variable" data type for the values read](images/119995364491_DV_resource.Stream@PNG-de-DE.PNG)

###### Program

The following example shows you how to use the instruction "OPC UA-TranslatePathList":

SCL

IF #Run = FALSE THEN

    #Started := #Input_REQ AND NOT #Mem_Input_REQ;

    #Mem_Input_REQ := #Input_REQ;

    IF #Started THEN

        #Output_Busy := TRUE;

        #Output_Done := FALSE;

        #Output_Error := FALSE;

        #Output_Status := 0;

        #State := 1;

        #Run := TRUE;

        #FirstCall := TRUE;

        #Set_REQ_To_FALSE := TRUE; //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

    END_IF;

END_IF;

IF #Run = TRUE THEN

    CASE #State OF

        1: // case 1, connect to server

        IF #FirstCall = TRUE THEN

           #FirstCall := FALSE;

           //set ServerEndPointUrl of the server we want to connect to

           #SeverEndpointUrl := WString#'opc.tcp://192.168.1.1:4840';

           //set Securtiy Message Mode

           // 1 = None, 2 = Sign, 3 = Sign & Encrypt

           #SessionConnectInfo.SecurityMsgMode := 1;

           //set Security Policy

           // 1 = None, 2 = Basic128Rsa15,, 3 = Basic256, 4 = Basic256Sha256

           #SessionConnectInfo.SecurityPolicy := 1;

           //set the number of the client certificate you are using

           //in our case, this is 6

           //#SessionConnectInfo.CertificateID := 6;

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_Connect_Instance(REQ:=#Req,

                ConnectionHdl=>#ConnectionHdl,

                ServerEndpointUrl:=#SeverEndpointUrl,

                SessionConnectInfo:=#SessionConnectInfo,

                Timeout:=T#8S,

                Done=>#Done,

                Busy=>#Busy,

                Error=>#Error,

                Status=>#Status);

        IF #Done = TRUE THEN

           #State := #State + 1;

           #FirstCall := TRUE;

        END_IF;

        IF #Error = TRUE THEN

           // Did we get a connection handle?

           IF #ConnectionHdl <> 0 THEN

                // We got a connection handle

                // We have to release all resources in the server and disconnect

                #State := 100;

                //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

                #Set_REQ_To_FALSE := TRUE;

           ELSE

                // We did not get a connection handle

                #State := 99;

           END_IF;

           #Mem_Status := #Status;

           // set parameter REQ of OPC_UA_Connect to FALSE

           #OPC_UA_Connect_Instance(REQ := FALSE,

                ServerEndpointUrl := #SeverEndpointUrl,

                SessionConnectInfo := #SessionConnectInfo);

           #FirstCall := TRUE;

        END_IF;

        2: // case 2, get index of Siemens namespace

        IF #FirstCall = TRUE THEN

           #FirstCall := FALSE;

           //set Simatic namespace

           #NamespaceUris[0] := WString#'http://www.siemens.com/simatic-s7-opcua';

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_NamespaceGetIndexList_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                NamespaceUrisCount := 1,

                NamespaceUris := #NamespaceUris,

                Timeout := T#6S,

                StatusList := #NamespaceStatusList,

                NamespaceIndexes := #NamespaceIndexes,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           IF #NamespaceStatusList[0] = 0 THEN //one namespace

                #State := #State + 1;

           ELSE

                #State := 100;

                #Mem_Status := #Status;

                #Output_Error_Message := WString#' Error at NamespaceGetIndexList, Index 0';

           END_IF;

           #FirstCall := TRUE;

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_NamespaceGetIndexList_Instance(REQ := FALSE,

                NamespaceUris := #NamespaceUris,

                StatusList := #NamespaceStatusList,

                NamespaceIndexes := #NamespaceIndexes);

           #FirstCall := TRUE;

        END_IF;

        3: // case 3, get NodeIds from server

        IF #FirstCall = TRUE THEN

           //set BrowsePath[0] for DeviceInfo

           //set BrowsePath.StartingNode

           #BrowsePaths[0].StartingNode.Identifier := WString#'85';

           #BrowsePaths[0].StartingNode.IdentifierType := 0;

           #BrowsePaths[0].StartingNode.NamespaceIndex := 0;

           //set BrowsePath.RelativePath

           #BrowsePaths[0].RelativePath.NoOfElements := 4;

           #BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[0].RelativePath.Elements[1].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[0].RelativePath.Elements[1].TargetName.Name := WString#'productionline';

           #BrowsePaths[0].RelativePath.Elements[1].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[0].RelativePath.Elements[2].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[0].RelativePath.Elements[2].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[0].RelativePath.Elements[2].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[0].RelativePath.Elements[2].TargetName.Name := WString#'DataBlocksGlobal';

           #BrowsePaths[0].RelativePath.Elements[2].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[0].RelativePath.Elements[3].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[0].RelativePath.Elements[3].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[0].RelativePath.Elements[3].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[0].RelativePath.Elements[3].TargetName.Name := WString#'RfidReader_Door_1';

           #BrowsePaths[0].RelativePath.Elements[3].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[0].RelativePath.Elements[4].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[0].RelativePath.Elements[4].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[0].RelativePath.Elements[4].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[0].RelativePath.Elements[4].TargetName.Name := WString#'DeviceInfo';

           #BrowsePaths[0].RelativePath.Elements[4].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           //set BrowsePath[1] for DeviceStatus

           //set BrowsePath.StartingNode

           #BrowsePaths[1].StartingNode.Identifier := WString#'85';

           #BrowsePaths[1].StartingNode.IdentifierType := 0;

           #BrowsePaths[1].StartingNode.NamespaceIndex := 0;

           //set BrowsePath.RelativePath

           #BrowsePaths[1].RelativePath.NoOfElements := 4;

           #BrowsePaths[1].RelativePath.Elements[1].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[1].RelativePath.Elements[1].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[1].RelativePath.Elements[1].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[1].RelativePath.Elements[1].TargetName.Name := WString#'productionline';

           #BrowsePaths[1].RelativePath.Elements[1].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[1].RelativePath.Elements[2].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[1].RelativePath.Elements[2].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[1].RelativePath.Elements[2].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[1].RelativePath.Elements[2].TargetName.Name := WString#'DataBlocksGlobal';

           #BrowsePaths[1].RelativePath.Elements[2].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[1].RelativePath.Elements[3].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[1].RelativePath.Elements[3].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[1].RelativePath.Elements[3].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[1].RelativePath.Elements[3].TargetName.Name := WString#'RfidReader_Door_1';

           #BrowsePaths[1].RelativePath.Elements[3].TargetName.NamespaceIndex := #NamespaceIndexes[0];

           #BrowsePaths[1].RelativePath.Elements[4].ReferenceTypeId.Identifier := WString#'33';

           #BrowsePaths[1].RelativePath.Elements[4].ReferenceTypeId.IdentifierType := 0;

           #BrowsePaths[1].RelativePath.Elements[4].ReferenceTypeId.NamespaceIndex := 0;

           #BrowsePaths[1].RelativePath.Elements[4].TargetName.Name := WString#'DeviceStatus';

           #BrowsePaths[1].RelativePath.Elements[4].TargetName.NamespaceIndex := #NamespaceIndexes[0];

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_TranslatePathList_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                BrowsePathsCount := 2,

                BrowsePaths := #BrowsePaths,

                Timeout := T#6S,

                NamespaceIndexCount := 0,

                TargetNodeIDs := #TagetNodeIds,

                TargetStatusList := #TargetStatusList,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           IF #TargetStatusList[0] = 0 AND #TargetStatusList[1] = 0 THEN

                #State := #State + 1;

           ELSE

                #State := 100;

                #Mem_Status := #Status;

                #Output_Error_Message := WString#'Error at TranslatePathList';

           END_IF;

           #FirstCall := TRUE;

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_TranslatePathList_Instance(REQ := FALSE,

                ConnectionHdl := #ConnectionHdl,

                BrowsePaths := #BrowsePaths,

                TargetNodeIDs := #TagetNodeIds,

                TargetStatusList := #TargetStatusList);

           #FirstCall := TRUE;

        END_IF;

        4: // case 4, get handles for the NodeIds we have got in case 3

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_NodeGetHandleList_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                NodeIDCount := 2,

                NodeIDs := #TagetNodeIds,

                Timeout := T#6S,

                NodeStatusList := #NodeStatusList,

                NodeHdls := #NodeHdls,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           IF #NodeStatusList[0] = 0 AND #NodeStatusList[1] = 0

           THEN

                #State := #State + 1;

           ELSE

                //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

                #Set_REQ_To_FALSE := TRUE;

                #State := 100;

                #Mem_Status := #Status;

                #Output_Error_Message := WString#'Error at NodeGetHandleList';

           END_IF;

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_NodeGetHandleList_Instance(REQ := FALSE,

                NodeIDs := #TagetNodeIds,

                NodeStatusList := #NodeStatusList,

                NodeHdls := #NodeHdls);

        END_IF;

        5: // case 5, read the values of the NodeIds

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_ReadList_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                NodeHdlCount := 2,

                NodeHdls := #NodeHdls,

                Timeout := T#6S,

                NodeStatusList := #NodeStatusList,

                Variable := #Variable,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           FOR #i := 0 TO 1 DO

                IF NOT (#NodeStatusList[#i] = 0) THEN

                    #Output_Error_Message := CONCAT_WSTRING(IN1 := WSTRING#'Error at Readlist, Index: ',

                    IN2 := INT_TO_WSTRING(#i));

                END_IF;

           END_FOR;

           #State := #State + 1;

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_ReadList_Instance(REQ := FALSE,

                NodeHdls := #NodeHdls,

                NodeStatusList := #NodeStatusList,

                Variable := #Variable);

        END_IF;

        6: // case 6, release the node handles

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_NodeReleaseHandleList_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                NodeHdlCount := 1,

                NodeHdls := #NodeHdls,

                Timeout := T#6S,

                NodeStatusList := #NodeStatusList,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #NodeStatusList[0] = 0 AND #NodeStatusList[1] = 0

        THEN

           #State := #State + 1;

        ELSE

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #Output_Error_Message := WString#'Error at NodeReleasetHandleList';

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_NodeReleaseHandleList_Instance(REQ := FALSE,

                NodeHdls := #NodeHdls,

                NodeStatusList := #NodeStatusList);

        END_IF;

        7: // case 7; disconnect form server

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_Disconnect_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                Timeout := T#6S,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           #State := #State + 1;

        END_IF;

        IF #Error = TRUE THEN

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #State := 100;

           #Mem_Status := #Status;

           #OPC_UA_Disconnect_Instance(REQ := FALSE,

                ConnectionHdl := #ConnectionHdl);

        END_IF;

        8: //case = 8, function block has run successfully

           #Output_Done := TRUE;

           #Output_Busy := FALSE;

           #State := 0;

           #Mem_Input_REQ := FALSE;

           #Run := FALSE;

           #Started := FALSE;

        99: // ERROR handling

           #Output_Error := TRUE;

           #Output_Status := #Mem_Status;

           #State := 0;

           #Output_Busy := FALSE;

           #Run := FALSE;

           #Mem_Input_REQ := FALSE;

           #Started := FALSE;

        100: // ERROR handling, disconnect from server to release resources (handles)

        IF #Set_REQ_To_FALSE = TRUE THEN

           #Set_REQ_To_FALSE := FALSE;

           //set REQ to FALSE

           #OPC_UA_Disconnect_Instance(REQ := FALSE,

                ConnectionHdl := #ConnectionHdl);

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_Disconnect_Instance(REQ := #Req,

                ConnectionHdl := #ConnectionHdl,

                Timeout := T#6S,

                Done => #Done,

                Busy => #Busy,

                Error => #Error,

                Status => #Status);

        IF #Done = TRUE THEN

           #Output_Error := TRUE;

           #Output_Status := #Mem_Status;

           #State := 0;

           #Output_Busy := FALSE;

           #Run := FALSE;

           #Mem_Input_REQ := FALSE;

           #Started := FALSE;

        END_IF;

        IF #Error = TRUE THEN

           #Output_Error_Message := WString#'Error handling: Resources cannot be released!';

           #Output_Error := TRUE;

           #Output_Status := #Mem_Status;

           #State := 0;

           #Output_Busy := FALSE;

           #Run := FALSE;

           #Mem_Input_REQ := FALSE;

           #Started := FALSE;

        END_IF;

    END_CASE;

END_IF;

##### Example program for calling a method of an OPC UA server (S7-1500)

###### Example program for calling a server method

This section includes the complete program code for the example program "Call_OpenDoor_On_Productionline".

The example shows you how a user program uses the instruction "OPC_UA_MethodCall" to call a server method.

You can find a description of the "OPC_UA_MethodCall" instruction in section [OPC_UA_MethodCall: Call method](#opc_ua_methodcall-call-method-s7-1500).

**Program structure**

The program operates as OPC UA client and comprises the following steps:

1. Establishing a connection to an OPC UA server.
2. Calling the server method.
3. Terminating the connection to the OPC UA server.

You start the program with a positive edge at "Input_REQ".

###### Declaration

The following figure shows the declaration of local tags for the function block "Call_OpenDoor_On_Productionline".

![Declaration](images/110392489995_DV_resource.Stream@PNG-de-DE.png)

###### Program

SCL

IF #Run = FALSE THEN  
    #Started := #Input_REQ AND NOT #Mem_Input_REQ;

    #Mem_Input_REQ := #Input_REQ;

    IF #Started THEN

        #Output_Busy := TRUE;

        #Output_Done := FALSE;

        #Output_Error := FALSE;

        #Output_Status := 0;  
        #Output_Error_Message := WSTRING#'';

        #State := 1;

        #Run := TRUE;

        #Init_Method_InputParameter := TRUE;

        #Set_REQ_To_FALSE := TRUE;

    END_IF;

END_IF;

IF #Run = TRUE THEN

    CASE #State OF

    1: // case 1, connect to server

    IF #Busy = FALSE THEN

        #Req := TRUE;

     ELSE

        #Req := FALSE;

    END_IF;

    #OPC_UA_Connect_Instance(REQ := #Req,

        ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

        SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

        Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

        Done => #Done,

        Busy => #Busy,

        Error => #Error,

        Status => #Status,

        ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

        IF #Done = TRUE THEN

           #State := #State + 1;

        END_IF;

        IF #Error = TRUE THEN

           // Did we get a connection handle?

           IF "Productionline_Configuration".Connection.ConnectionHdl <> 0 THEN

               // We have to release all resources in the server and disconnect

               #State := 100;

               //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

           ELSE

               #State := 99;

           END_IF;

        #Mem_Status := #Status;

        #OPC_UA_Connect_Instance(REQ := FALSE,

              ServerEndpointUrl := "Productionline_Configuration".Connection.ServerEndpointUrl,

              SessionConnectInfo := "Productionline_Configuration".Connection.ConnectInfo,

              Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

              ConnectionHdl => "Productionline_Configuration".Connection.ConnectionHdl);

        END_IF;

        2: // case 2, get index of Siemens namespace

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_NamespaceGetIndexList_Instance(REQ := #Req,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

               NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

               NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

        IF #Done = TRUE THEN

           IF "Productionline_Configuration".Namespaces.NamespaceStatusList[0] = 0 THEN //one namespace

               #State := #State + 1;

           ELSE

               #State := 100;

               //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

               #Mem_Status := #Status;

               #Output_Error_Message := WString#' Error at NamespaceGetIndexList, Index 0';

           END_IF;

        END_IF;

        IF #Error = TRUE THEN

           #State := 100;

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #Mem_Status := #Status;

           #OPC_UA_NamespaceGetIndexList_Instance(REQ := FALSE,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               NamespaceUrisCount := "Productionline_Configuration".Namespaces.NamespaceCount,

               NamespaceUris := "Productionline_Configuration".Namespaces.NamespaceURIs,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               StatusList := "Productionline_Configuration".Namespaces.NamespaceStatusList,

               NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes);

        END_IF;

        3: // case 3, get an handle for server method OpenDoor

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_MethodGetHandleList_Instance(REQ := #Req,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               NodeIDCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

               ObjectNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".ObjectNodes,

               MethodNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodNodes,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

               NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status,

               StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

               MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls);

        IF #Done = TRUE THEN

           IF "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0] = 0 THEN //one method

               #State := #State + 1;

           ELSE

               #State := 100;

               //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

               #Mem_Status := #Status;

               #Output_Error_Message := WString#'Error at MethodGetHandleList';

           END_IF;

        END_IF;

        IF #Error = TRUE THEN

           #State := 100;

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #Mem_Status := #Status;

           #OPC_UA_MethodGetHandleList_Instance(REQ := FALSE,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               NodeIDCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

               ObjectNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".ObjectNodes,

               MethodNodeIDs := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodNodes,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               NamespaceIndexCount := "Productionline_Configuration".Namespaces.NamespaceCount,

               NamespaceIndexes := "Productionline_Configuration".Namespaces.ServerNamespaceIndexes,

               StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

               MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls);

        END_IF;

        4: // case 4, call method OpenDoor

        IF #Init_Method_InputParameter = TRUE THEN

           #Init_Method_InputParameter := FALSE;

           // for our server method at Productionline, we set input parameters to 1

           "Productionline_Data".MethodListOpenDoor.Method.Inputs.Number := 1;

        END_IF;

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        OPC_UA_MethodCall_Instance(REQ := #Req,

               ConnectionHdl:="Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               MethodHdl := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls[0],

               InputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Inputs,

               OutputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Outputs,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0],

               MethodResult := "Productionline_Data"."MethodListOpenDoor".MethodResultList[0]);

        //"Productionline_Data"."MethodListOpenDoor".MethodResultList[0]] contains

        //the status/error codes of the server method

        //which was run on the connected CPU as user program

        //These codes are defined as follows:

        //     Good: 0x0000_0000 TO 0x3FFF_ FFFF

        //     Uncertain: 0x4000_0000 TO 0x7FFF_FFFF

        //     Bad: 0x8000_0000 TO 0xFFFF_FFFF

        #Output_MethodResult := "Productionline_Data".MethodListOpenDoor.MethodResultList[0];

        IF #Done = TRUE THEN

           IF #MethodResult < 16#8000_0000 THEN

               #State := #State + 1;

           ELSE

               //server method did not run successfully

               #State := 100;

               //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

               #Mem_Status := #Status;

               #Output_Error_Message := WString#' Error at server method';

           END_IF;

        END_IF;

        IF #Error = TRUE THEN

           #State := 100;

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #Mem_Status := "Productionline_Data".MethodListOpenDoor.MethodStatusList[0];

           #OPC_UA_MethodCall_Instance(REQ := #Req,

               ConnectionHdl:="Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               MethodHdl := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls[0],

               InputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Inputs,

               OutputArguments := "Productionline_Data"."MethodListOpenDoor"."Method".Outputs,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0],

               MethodResult := "Productionline_Data"."MethodListOpenDoor".MethodResultList[0]);

        END_IF;

        5: // case 5, release method handle

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

        #OPC_UA_MethodReleaseHandleList_Instance(REQ := #Req,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               MethodHdlCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

               MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls,

               StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

        IF #Done = TRUE THEN

           #Mem_Status := #Status;

           IF "Productionline_Data"."MethodListOpenDoor".MethodStatusList[0] = 0 THEN

               #State := #State + 1;

           ELSE

               #State := 100;

               //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

               #Set_REQ_To_FALSE := TRUE;

               #Mem_Status := #Status;

               #Output_Error_Message := WString#'Error at MethodGetHandleList';

           END_IF;

        END_IF;

        IF #Error = TRUE THEN

           #State := 100;

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #Mem_Status := #Status;

           #OPC_UA_MethodReleaseHandleList_Instance(REQ := FALSE,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               MethodHdlCount := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodCount,

               MethodHdls := "Productionline_Configuration".MethodLists."MethodListOpenDoor".MethodHdls,

               StatusList := "Productionline_Data"."MethodListOpenDoor".MethodStatusList);

        END_IF;

        6: // case 6, disconnect from server

        IF #Busy = FALSE THEN

           #Req := TRUE;

        ELSE

           #Req := FALSE;

        END_IF;

           #OPC_UA_Disconnect_Instance(REQ := #Req,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

        IF #Done = TRUE THEN

           #State := #State + 1;

           #Mem_Status := #Status;

        END_IF;

        IF #Error = TRUE THEN

           #State := 100;

           //In case 100, to set REQ of instruction "OPC_UA_Disconnect" to FALSE

           #Set_REQ_To_FALSE := TRUE;

           #Mem_Status := #Status;

           #OPC_UA_Disconnect_Instance(REQ := FALSE,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout);

        END_IF;

        7: //case = 7, function block has run successfully

           #Output_Done := TRUE;

           #Output_Busy := FALSE;

           #State := 0;

           #Mem_Input_REQ := FALSE;

           #Run := FALSE;

           #Started := FALSE;

        99: // ERROR handling

           #Output_Error := TRUE;

           #Output_Status := #Mem_Status;

           #State := 0;

           #Output_Busy := FALSE;

           #Run := FALSE;

           #Mem_Input_REQ := FALSE;

           #Started := FALSE;

        100: // ERROR handling, disconnect from server to release resources (handles)

           IF #Set_REQ_To_FALSE = TRUE THEN

               #Set_REQ_To_FALSE := FALSE;

               //set REQ to definitely to FALSE

               #OPC_UA_Disconnect_Instance(REQ := FALSE,

                  ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

                  Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout);

           END_IF;

           IF #Busy = FALSE THEN

               #Req := TRUE;

           ELSE

               #Req := FALSE;

           END_IF;

           #OPC_UA_Disconnect_Instance(REQ := #Req,

               ConnectionHdl := "Productionline_Configuration".Connection.ConnectionHdl,

               Timeout := "Productionline_Configuration".Connection.ConnectInfo.SessionTimeout,

               Done => #Done,

               Busy => #Busy,

               Error => #Error,

               Status => #Status);

           IF #Done = TRUE THEN

               #Output_Error := TRUE;

               #Output_Status := #Mem_Status;

               #State := 0;

               #Output_Busy := FALSE;

               #Run := FALSE;

               #Mem_Input_REQ := FALSE;

               #Started := FALSE;

           END_IF;

           IF #Error = TRUE THEN

               #Output_Error_Message := WString#'Error handling: Resources cannot be released!';

               #Output_Error := TRUE;

               #Output_Status := #Mem_Status;

               #State := 0;

               #Output_Busy := FALSE;

               #Run := FALSE;

               #Mem_Input_REQ := FALSE;

               #Started := FALSE;

           END_IF;

    END_CASE;

END_IF;

### Server instructions (S7-1200, S7-1500)

This section contains information on the following topics:

- [Methods (S7-1200, S7-1500)](#methods-s7-1200-s7-1500)

#### Methods (S7-1200, S7-1500)

This section contains information on the following topics:

- [OPC_UA_ServerMethodPre: Preparing the server method call (S7-1200, S7-1500)](#opc_ua_servermethodpre-preparing-the-server-method-call-s7-1200-s7-1500)
- [OPC_UA_ServerMethodPost: Post preparation of the server method call (S7-1200, S7-1500)](#opc_ua_servermethodpost-post-preparation-of-the-server-method-call-s7-1200-s7-1500)
- [Example program for providing a method for OPC UA clients (S7-1200, S7-1500)](#example-program-for-providing-a-method-for-opc-ua-clients-s7-1200-s7-1500)

##### OPC_UA_ServerMethodPre: Preparing the server method call (S7-1200, S7-1500)

###### Validity

The following description of the "OPC_UA_ServerMethodPre" instruction applies to S7-1200-CPUs firmware version V4.5 and higher and for S7-1500-CPUs firmware version V2.5 and higher.

###### New instruction version V1.1 from firmware version V3.1

As of firmware version V3.1, the new instruction version V1.1 is supported. You can find all other information under:

[Product information on documentation S7-1500/ET 200MP, S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/68052815)

###### Description

This section describes the instruction "OPC_UA_ServerMethodPre".

Because the instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" always have to be called up in pairs in the user program, please also take into account the section on the instruction "OPC_UA_ServerMethodPost".

###### Parameters for "OPC_UA_ServerMethodPre"

The parameters of the instruction "OPC_UA_ServerMethodPre"

| Parameter | Declaration | Data type | Meaning |
| --- | --- | --- | --- |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error codes for the status" below. |
| UAMethodCalled | Output | BOOL | The method provided has been called by an OPC UA client. |
| UAMethod_InParameters | InOut | VARIANT | Pointer to a tag that contains the input parameters for the method provided. |

###### Error codes for the status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table describes the different categories of error codes.

Error codes for the status

| Error code   (hexadecimal values) | Explanation |
| --- | --- |
| 0000_0000 | Instruction finished successfully. |
| 8xxx_xxxx | OPC UA specific error |
| Axxx_xxxx | PLCopen specific error |
| B080_C300 | Insufficient resources |
| B08x_yz00 | SIMATIC-specific error |
| e.g. B080_B000 | TooManyMethods:  Maximum number of server methods or max. number of server method instances exceeded.  (Calling the instructions OPC_UA_ServerMethodPre, OPC_UA_ServerMethodPost):  Example for S7-1510 to S7-1513 ...: Max. 20 (FW V3.0)  Example for S7-1515, S7-1516...: Max. 50 (FW V3.0)  Example for S7-1517, S7-1518, S7-1507S...: Max. 100 (FW V3.0)  Refer to the technical specifications of the CPUs (number of server methods, max.) |
| For more error codes, see [Error codes](#error-codes-s7-1500) |  |

###### Number of server methods

The number of methods that can be registered is limited depending on the CPU. When these limits are violated, calling this instruction results in the "TooManyMethods" error code specified above.

Violation of the configuration limit is also indicated by the fact that the instances of the methods are displayed in the address space of the OPC UA server but shown as not callable.

The following figure shows the representation of the methods in the UaExpert in the "good case" and in the case of exceeded quantity structures.

![Number of server methods](images/165418953611_DV_resource.Stream@PNG-de-DE.png)

###### Declaration of tags

Declare an instance of the instruction "OPC_UA_ServerMethodPre" and the tags with which you supply the instruction parameters, see also [Example program for providing a method for OPC UA clients](#example-program-for-providing-a-method-for-opc-ua-clients-s7-1200-s7-1500).

The following points are important for the declaration:

- Create the instruction "OPC_UA_ServerMethodPre" as a multi-instance in the calling function block.

  > **Note**
  >
  > **Name of the multiple instance**
  >
  > The multiple instance has to be named "OPC_UA_ServerMethodPre_Instance", otherwise no method is created on the server.

  Use drag-and-drop to move the instruction from the folder "Instructions > Communication > OPC UA > OPC UA Server" to the editor.

  Next, click "Multi-instance".
- When the server method has one or more input parameters, you must declare a tag with the name "**UAMethod_InParameters**".

  First, create a PLC data type (UDT) for the input parameters of the server method.

  Then use this UDT for the tag "UAMethod_InParameters".

  In the example, the data type is called "UDT_OpenDoorInArguments" and includes the element Number.

  Alternative:

  You can also assign the data type "Struct" to the tag "**UAMethod_InParameters**". Then create the components of this data type according to the input parameters of the server method (same names and data types).

  ![Declaration of tags](images/106267511691_DV_resource.Stream@PNG-de-DE.png)

###### Calling the instruction

The instruction "OPC_UA_ServerMethodPre" queries the operating system to determine whether or not the server method was called.

If the server method was called by the client, the instruction "OPC_UA_ServerMethodPre" provides the input parameters for the server method.

###### Assignment of data types (SIMATIC – OPC UA)

For the input and output parameters of methods, note the explanations on the rules for usable data types (S7-1500: [Boundary conditions for using server methods](Configuring%20automation%20systems.md#boundary-conditions-for-using-server-methods-s7-1500-s7-1500t), S7-1200: [Boundary conditions for using server methods](Configuring%20automation%20systems.md#boundary-conditions-for-using-server-methods-s7-1200)).

> **Note**
>
> **Supply of structured data types with nested arrays**
>
> If a structured data type (Struct/UDT) contains an array, the OPC UA server does not provide information about the length of this array.
>
> If you use such a structure as the input or output parameter of a server method, for example, you must ensure that the nested array is supplied with the correct length when the method is called.
>
> If you do not adhere to this rule, the method fails with the error code "BadInvalidArgument".

##### OPC_UA_ServerMethodPost: Post preparation of the server method call (S7-1200, S7-1500)

###### Validity

The following description of the "OPC_UA_ServerMethodPost" instruction applies to S7-1200-CPUs firmware version V4.5 and higher and for S7-1500-CPUs firmware version V2.5 and higher.

###### New instruction version V1.1 from firmware version V3.1

As of firmware version V3.1, the new instruction version V1.1 is supported. You can find all other information under:

[Product information on documentation S7-1500/ET 200MP, S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/68052815)

###### Description

This section describes the instruction "OPC_UA_ServerMethodPost".

Because the instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" always have to be called up in pairs in the user program, please also take into account the section on the instruction "OPC_UA_ServerMethodPre".

###### Parameters for "OPC_UA_ServerMethodPost"

The parameters of the instruction "OPC_UA_ServerMethodPost"

| Parameter | Declaration | Data type | Meaning |
| --- | --- | --- | --- |
| Done | Output | BOOL | Status of execution:  - **0**: Execution of the instruction aborted, not yet complete or not yet started - **1**: Execution of instruction completed without errors |
| Busy | Output | BOOL | Execution status parameter:  - **0**: Instruction not being executed - **1**: Instruction currently being executed |
| Error | Output | BOOL | Error display  - **0**: No error - **1**: An error has occurred. See "Status" parameter. |
| Status | Output | DWORD | Cause of the error, see "Error codes for the status" below. |
| UAMethod_Result | Input | DWORD | Error codes for the OPC UA server, provided by the user program.  Recommendation: Use the feedback message of error codes that begin with 0xFF. For OPC UA the following areas are defined:   - Good: 0x0000_0000 to 0x3FFF_ FFFF - Uncertain: 0x4000_0000 to 0x7FFF_FFFF - Bad: 0x8000_0000 to 0xFFFF_FFFF   Depending on the client it is possible that the codes of the areas "Good" and "Uncertain" are not output. |
| UAMethod_Finished | Input | BOOL | Set the value of the parameter to TRUE if the method provided has been executed. |
| UAMethod_OutParameters | InOut | VARIANT | Pointer to a tag that contains the output parameters of the method provided. |

###### Error codes for the status

The "Status" parameter provides information about errors that occurred during execution of the instruction.

The following table describes the different categories of error codes.

Error codes for the status

| Error code   (hexadecimal values) | Explanation |
| --- | --- |
| 0000_0000 | Instruction finished successfully. |
| 8xxx_xxxx | OPC UA specific error |
| Axxx_xxxx | PLCopen specific error |
| B080_C300 | Insufficient resources |
| B08x_yz00 | SIMATIC-specific error |
| For more error codes, see [Error codes](#error-codes-s7-1500) |  |

###### Declaration of tags

Declare an instance of the instruction "OPC_UA_ServerMethodPost" and the tags with which you supply the instruction parameters, see also [Example program for providing a method for OPC UA clients](#example-program-for-providing-a-method-for-opc-ua-clients-s7-1200-s7-1500).

The following points are important for the declaration:

- Create the instruction "OPC_UA_ServerMethodPost" as a multi-instance in the calling function block.

  > **Note**
  >
  > **Name of the multiple instance**
  >
  > The multiple instance has to be named "OPC_UA_ServerMethodPost_Instance", otherwise no method is created on the server.

  Use drag-and-drop to move the instruction from the folder "Instructions > Communication > OPC UA > OPC UA Server" to the editor. Next, click "Multi-instance".
- When the server method has one or more output parameters, you must declare a tag with the name "**UAMethod_OutParameters**".

  First, create a PLC data type (UDT) for the output parameters of the server method.

  Then use this UDT for the tag "UAMethod_OutParameters".

  In the example, the data type is called "UDT_OpenDoorOutArguments"; the only output parameter is Result.

  Alternative:

  You can also assign the data type "Struct" to the tag "**UAMethod_OutParameters**". Then create the components of this data type according to the output parameters of the server method (same names and data types).

  ![Declaration of tags](images/106267537803_DV_resource.Stream@PNG-de-DE.png)

  Declaration of tags

###### Calling the instruction

You use the "OPC_UA_ServerMethodPost" instruction to inform the operating system that the server method has been executed and that the values of the output parameters are valid.

###### Assignment of data types (SIMATIC – OPC UA)

For the input and output parameters of methods, please note the explanations regarding the rules on usable data types in the section "[Mapping SIMATIC data types to OPC UA data types](Configuring%20automation%20systems.md#mapping-simatic-data-types-to-opc-ua-data-types-s7-1500-s7-1500t)".

> **Note**
>
> **Supply of structured data types with nested arrays**
>
> If a structured data type (Struct/UDT) contains an array, the OPC UA server does not provide information about the length of this array.
>
> If you use such a structure as the input or output parameter of a server method, for example, you must ensure that the nested array is supplied with the correct length when the method is called.
>
> If you do not adhere to this rule, the method fails with the error code "BadInvalidArgument".

##### Example program for providing a method for OPC UA clients (S7-1200, S7-1500)

###### New instruction version V1.1 from firmware version V3.1

As of firmware version V3.1, the new instruction version V1.1 is supported.

The example program described below cannot run with instruction version V1.1. Therefore, do not use it anymore from instruction version V1.1.

You can find more information under: [Product information on documentation S7-1500/ET 200MP, S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/68052815)

###### Example program for a server method

This section includes the complete program code for the example program "OpenDoor".

The example shows you how a user program uses the instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost".

The instructions are described in the sections [OPC_UA_ServerMethodPre: Preparing the server method call](#opc_ua_servermethodpre-preparing-the-server-method-call-s7-1200-s7-1500) and [OPC_UA_ServerMethodPost: Post preparation of the server method call](#opc_ua_servermethodpost-post-preparation-of-the-server-method-call-s7-1200-s7-1500).

The program provides a server method for OPC UA clients: The program sets the output parameter "Result" to the value 1 when the input parameter "Number" has the value "1".

In order to keep the example easy and simple, a detailed error evaluation ("Status" parameter) is not included.

###### Program structure

The program is divided into the following sections:

1. Calling the "OPC_UA_ServerMethodPre" instruction to determine if the server method was called by a client.
2. If the server method was called, the server method is executed. It defines the actual functionality when the method is called by an OPC UA client.
3. When the server method has been completed, the instruction "OPC_UA_ServerMethodPost" is called. This section informs the operating system that the server method has been executed.

###### Declaration

The following figure shows the declaration of local tags for the example program:

![Declaration](images/114147496843_DV_resource.Stream@PNG-de-DE.png)

###### Program

The following program shows how you use OPC UA instructions to provide a method for OPC UA clients that is executed in your user program (server method).

**Calling the "OPC_UA_ServerMethodPre" instruction**

First, the instruction "OPC_UA_ServerMethodPre" is called to query the operating system whether the server method was called by an OPC UA client.

If the server method was called, the tag "#Method_Called" is "TRUE".

If the "OPC_UA_ServerMethodPre" instruction was also executed successfully (#Pre_Done = TRUE), the tag "#Started" is set to the value "TRUE".

**Server method**

When the tag "#Started" has the value "TRUE", this starts the actual user program.

You have all kinds of programming options in this section: You can read in or output process values, access global data blocks, call functions and function blocks, etc.

The application program may take several cycles.

To signal the end of the user program set the tag "#Method_Finished" to "TRUE".

With "#Method_Result" you transfer a self-defined error code that is used at the block parameter "UAMethod_Result" of the instruction "OPC_UA_ServerMethodPost".

**Calling the "OPC_UA_ServerMethodPost" instruction**

The tag "#Method_Finished" is set to save the state that the user program was executed.

This tag is used in the instruction "OPC_UA_ServerMethodPost" to inform the operating system whether the server method was executed or not.

The operating system then takes over the acknowledgment to the client that called the method.

SCL

REGION PRE

IF #Started = FALSE AND #Method_Finished = FALSE THEN

#OPC_UA_ServerMethodPre_Instance(Done => #Pre_Done,

Error => #Pre_Error,

UAMethod_Called => #Method_Called,

UAMethod_InParameters := #UAMethod_InParameters);

IF #Pre_Error THEN

#Error_Message := WString#'Error at OPC_UA_ServerMethodPre';

END_IF;

IF #Pre_Done AND #Method_Called THEN

#Started := TRUE;

#Error_Message := WString#'';

END_IF;

END_IF;

END_REGION

REGION FUNCTIONALITY

// The purpose of this demo method is to demonstrate the basic structure of a server method

IF #Started = TRUE THEN

// This demo server method just checks if input parameter #UAMethod_InParameters.Number is 1

// If this is the case, the server method sets the output parameter.

IF #UAMethod_InParameters.Number = 1 THEN

//set doorLocked to false, so that the door can be opened

#doorLocked := FALSE;

//set values for output parameters

//this is just an example

#UAMethod_OutParameters.Result := 1;

#Method_Result := 16#0000_0000;

#Method_Finished := TRUE;

#Started := FALSE;

ELSE

#Error_Message := WString#'Input-Parameter Number must be 1 to run this example server method';

//we send back an error code to the calling OPC UA client

//for our example, we define 16#FFFF_FFFF = "Input-Parameter Number must be 1"

#Method_Result := 16#FFFF_FFFF;

#Started := FALSE;

#Method_Finished := TRUE;

END_IF;

END_IF;

END_REGION

REGION POST

#OPC_UA_ServerMethodPost_Instance(UAMethod_Result := #Method_Result,

UAMethod_Finished := #Method_Finished,

Done => #Post_Done,

Error => #Post_Error,

UAMethod_OutParameters := #UAMethod_OutParameters);

IF #Post_Error = TRUE THEN

#Error_Message := WString#'Error at OPC_UA_ServerMethodPost';

#Method_Finished := FALSE;

END_IF;

IF #Post_Done = TRUE THEN

#Method_Finished := FALSE;

END_IF;

END_REGION

###### Deleting method

If you no longer make a server method available and want to delete it, you not only have to remove the call of the corresponding FB, but also delete the instance data block.

If the instance data block is not deleted, the method is visible in the address space. The tags are not supplied.

## Communications processor (S7-1200, S7-1500)

This section contains information on the following topics:

- [SIMATIC NET CM/CP (S7-1200, S7-1500)](SIMATIC%20NET%20CM-CP.md#simatic-net-cmcp)
- [Point-to-point (S7-1200, S7-1500)](Point-to-point%20%28S7-1200%2C%20S7-1500%29.md#point-to-point-s7-1200-s7-1500)
- [USS (S7-1200, S7-1500)](USS%20%28S7-1200%2C%20S7-1500%29.md#uss-s7-1200-s7-1500)
- [MODBUS (RTU) (S7-1200, S7-1500)](MODBUS%20%28RTU%29%20%28S7-1200%2C%20S7-1500%29.md#modbus-rtu-s7-1200-s7-1500)
- [ET 200S serial interface (S7-1200, S7-1500)](ET%20200S%20serial%20interface%20%28S7-1200%2C%20S7-1500%29.md#et-200s-serial-interface-s7-1200-s7-1500)
- [Point-to-point (S7-1200)](Point-to-point%20%28S7-1200%29.md#point-to-point-s7-1200)
- [USS (S7-1200)](USS%20%28S7-1200%29.md#uss-s7-1200)
- [MODBUS (RTU) (S7-1200)](MODBUS%20%28RTU%29%20%28S7-1200%29.md#modbus-rtu-s7-1200)
- [MODBUS (TCP) (S7-1200, S7-1500)](MODBUS%20%28TCP%29%20%28S7-1200%2C%20S7-1500%29.md#modbus-tcp-s7-1200-s7-1500)
