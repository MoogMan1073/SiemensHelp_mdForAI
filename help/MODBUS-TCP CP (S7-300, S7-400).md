---
title: "MODBUS/TCP CP (S7-300, S7-400)"
package: ModbusTCPCPenUS
topics: 34
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# MODBUS/TCP CP (S7-300, S7-400)

This section contains information on the following topics:

- [MODBUSCP: Communicate as Modbus/TCP client or Modbus/TCP server (S7-300, S7-400)](#modbuscp-communicate-as-modbustcp-client-or-modbustcp-server-s7-300-s7-400)

## MODBUSCP: Communicate as Modbus/TCP client or Modbus/TCP server (S7-300, S7-400)

This section contains information on the following topics:

- [MODBUSCP V2 (S7-300, S7-400)](#modbuscp-v2-s7-300-s7-400)
- [MODBUSCP V1 (S7-300, S7-400)](#modbuscp-v1-s7-300-s7-400)

### MODBUSCP V2 (S7-300, S7-400)

This section contains information on the following topics:

- [General Information (S7-300, S7-400)](#general-information-s7-300-s7-400)
- [Commissioning (S7-300, S7-400)](#commissioning-s7-300-s7-400)
- [Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400)
- [Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400)
- [Licensing with the parameters IDENT_CODE and REG_KEY (S7-300, S7-400)](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400)
- [Address mapping (S7-300, S7-400)](#address-mapping-s7-300-s7-400)
- [id, db_param, and Init parameters (S7-300, S7-400)](#id-db_param-and-init-parameters-s7-300-s7-400)
- [ERROR, STATUS, STATUS_FUNC and Init_Status parameters (S7-300, S7-400)](#error-status-status_func-and-init_status-parameters-s7-300-s7-400)
- [DONE_NDR, DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT parameters (S7-300, S7-400)](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400)
- [ENQ_ENR and MONITOR parameters (S7-300, S7-400)](#enq_enr-and-monitor-parameters-s7-300-s7-400)

#### General Information (S7-300, S7-400)

##### General

The MODBUSCP instruction is a software product for the communication processors CP 343-1 and CP 443-1.

This instruction establishes communication between a CP 443-1 or CP 343-1 and a partner that supports the Modbus/TCP protocol.

The TCP/IP connections over the CP are static connections that are not terminated during error-free operation.

With the TCP stack used on the CP, the STEP 7 connection configuration only allows one use of a particular port number. Certain CP types can maintain and operate connections to multiple clients simultaneously through the local port 502.

The technical details of this topic are explained in the section "[Using connections on port 502](#using-connections-on-port-502-s7-300-s7-400)".

Data transmission takes place according to the client-server principle.

The SIMATIC S7 can be operated as client as well as server during the transmission.

##### Step-by-step instructions

1. Configuration of the CP as [server](#configuring-cp-as-modbustcp-server-s7-300-s7-400) or [client](#configuring-cp-as-modbustcp-client-s7-300-s7-400).
2. Calling the MODBUSCP instruction in the necessary OB.

   - see [Commissioning](#call-of-the-modbuscp-instruction-s7-300-s7-400)
3. Parameter assignment of the parameter DB according to the requirements (ID, client/server, Modbus register, DB areas, etc.).

   - see [Parameter data block](#parameter-data-block-s7-300-s7-400)
4. Parameter assignment of the Modbus block for initialization and for runtime.

   - see [Operating principle of the instruction](#description-of-modbuscp-s7-300-s7-400)
5. Download of the user program to the CPU and licensing of the Modbus block for this CPU.

   - see [Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400)

#### Commissioning (S7-300, S7-400)

This section contains information on the following topics:

- [Configuring CP as Modbus/TCP client (S7-300, S7-400)](#configuring-cp-as-modbustcp-client-s7-300-s7-400)
- [Configuring CP as Modbus/TCP server (S7-300, S7-400)](#configuring-cp-as-modbustcp-server-s7-300-s7-400)
- [Call of the MODBUSCP instruction (S7-300, S7-400)](#call-of-the-modbuscp-instruction-s7-300-s7-400)
- [Using connections on port 502 (S7-300, S7-400)](#using-connections-on-port-502-s7-300-s7-400)
- [Startup behavior of the CP 343-1 and CP 443-1 (S7-300, S7-400)](#startup-behavior-of-the-cp-343-1-and-cp-443-1-s7-300-s7-400)

##### Configuring CP as Modbus/TCP client (S7-300, S7-400)

###### Requirements

- "Devices &amp; Networks" editor is open.
- The following hardware is available in the "Device view":

  - S7 300/400, e.g. 315-2 DP or 414-2 DP
  - Communication processor CP 343-1/443-1

###### Assigning CP parameters

1. Select the CP.
2. Add a subnet to the PROFINET interface of the CP in the Inspector window under "Properties &gt; General &gt; Ethernet addresses".
3. Enter the IP address as well as the subnet mask.

![Assigning CP parameters](images/85864937611_DV_resource.Stream@PNG-en-US.png)

###### Add TCP connection

1. In the network view, click "Connections".
2. Select the connection type "TCP connection".
3. In the shortcut menu of the CPU, select the "Create new connection" command.
4. Select "Unspecified" as connection partner.
5. Select the communication module as local interface.
6. Select the function "Establish active connection".
7. Click "Add" and close the dialog.

![Add TCP connection](images/85882083211_DV_resource.Stream@PNG-en-US.png)

###### Assigning TCP connection parameters

1. Enter the IP address of the partner in the Inspector window under "Properties &gt; General &gt; General".

   ![Assigning TCP connection parameters](images/85867097739_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85867097739_DV_resource.Stream@PNG-en-US.png)
2. Under "Properties &gt; General &gt; Local ID", enter the local ID that you are configuring for the Modbus/TCP connection at the "MODBUSCP" block.

   You also need the value of the "LADDR" parameter for the parameter assignment of the "MODBUSCP" block; see [Parameter data block](#parameter-data-block-s7-300-s7-400).

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)
3. Under "Properties &gt; General &gt; Address details" enter "502" as partner port.

   Apply the default value for the local CP port, e.g. 2000.

![Assigning TCP connection parameters](images/85909676683_DV_resource.Stream@PNG-en-US.png)

##### Configuring CP as Modbus/TCP server (S7-300, S7-400)

###### Requirements

- "Devices &amp; Networks" editor is open.
- The following hardware is available in the "Device view":

  - S7 300/400, e.g. 315-2 DP or 414-2 DP
  - Communication processor CP 343-1/443-1

###### Assigning CP parameters

1. Select the CP.
2. Add a subnet to the PROFINET interface of the CP in the Inspector window under "Properties &gt; General &gt; Ethernet addresses".
3. Enter the IP address as well as the subnet mask.

![Assigning CP parameters](images/85864937611_DV_resource.Stream@PNG-en-US.png)

###### Add TCP connection

1. In the network view, click "Connections".
2. Select the connection type "TCP connection".
3. In the shortcut menu of the CPU, select the "Create new connection" command.
4. Select "Unspecified" as connection partner.
5. Select the communication module as local interface.
6. Deactivate the function "Establish active connection".
7. Click "Add" and close the dialog.

![Add TCP connection](images/85867088907_DV_resource.Stream@PNG-en-US.png)

###### Assigning TCP connection parameters

1. In the Inspector window under "Properties &gt; General &gt; Local ID", enter the local ID that you are configuring for the Modbus/TCP connection at the "MODBUSCP" block.

   You also need the value of the "LADDR" parameter for the parameter assignment of the "MODBUSCP" block; see [Using connections on port 502](#using-connections-on-port-502-s7-300-s7-400).

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)
2. Under "Properties &gt; General &gt; Address details" enter "502" as local CP port.

   ![Assigning TCP connection parameters](images/85909685771_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85909685771_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400)
  
[Add-on blocks for Modbus/TCP communication](http://support.automation.siemens.com/WW/view/en/62830463)

##### Call of the MODBUSCP instruction (S7-300, S7-400)

###### Requirement and basics

The MODBUSCP V2.0 instruction can be used as of **STEP7 V14 SP1 Update 2 (TIA Portal)**.

The MODBUSCP instruction is based on the Modbus Application Protocol Specification V1.1b3, April 26, 2012 - see [Modbus home page](http://www.modbus.org).

###### Call of the instruction

For correct program execution, the MODBUSCP instruction must be called in a cyclic OB (OB1 or in a time-controlled OB, e.g. OB35).

It is not permitted to call the MODBUSCP instruction in OB1 and in a time-controlled OB (e.g., OB35) at the same time. The OB121 must be present in the CPU. For more detailed information on this, see [Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400).

###### Inserting the Modbus block

Open the "Main [OB1]" block or a cyclic block. The MODBUSCP instruction is in the Task Card, palette and "Instructions &gt; Communication &gt; Communication processor" folder. In it, open the "MODBUS TCP" folder and drag the MODBUSCP instruction to the OB block.

Under "System blocks &gt; Program resources", the lower-level instructions MB_CPCLI (FB76) and MB_CPSRV (FB77) are displayed in addition to MODBUSCP (FB75). The lower-level instructions may not also be called in an OB. In addition, the internally called communication instructions AG_(L)SEND (FC5/FC50), AG_(L)RECV (FC6/FC60), and AG_CNTRL (FC10) are displayed.

###### Versions of the PLC blocks

If you are using the migrated blocks in V14, the following versions are used:

- Use of an S7-300:

  - AG_SEND V4.2
  - AG_RECV V4.7
  - AG_CNTRL V1.4
- Use of an S7-400:

  - AG_LSEND V3.1
  - AG_LRECV V3.1
  - AG_CNTRL V1.0

If you are using the integrated blocks in V14, you need the following versions in the "SIMATIC NET CP" library:

- Use of an S7-300:

  - AG_SEND V1.2
  - AG_RECV V1.2
  - AG_CNTRL V1.1
- Use of an S7-400:

  - AG_LSEND V1.1
  - AG_LRECV V1.1
  - AG_CNTRL V1.1

##### Using connections on port 502 (S7-300, S7-400)

Some CPs can multiplex TCP connections. This means that several Modbus/TCP clients can connect to port 502 of the CP. The CP functions as a Modbus/TCP server.

> **Note**
>
> For older firmware versions: Note that only one connection is configured regardless of how many clients access the CP as server.
>
> For newer CPs or firmware versions: You can configure multiple connections for port 502.

You will find more information in the CP data and in the firmware or at the link: [SIMATIC Modbus/TCP](https://support.industry.siemens.com/cs/de/en/view/104946406)

###### Requirements

To be able to use this function, the following settings need to be made in the connection parameter assignment:

- CP is server
- Port 502 as local port
- Unspecified TCP connection in "Devices &amp; Networks"
- Passive connection establishment

###### Number of connections

Via port 502, the CP can communicate with a maximum of 4 clients at any one time.

###### Displaying the status of the connection

The status of the connection can be displayed in the "Devices &amp; Networks" editor in the Inspector window under "Diagnostics &gt; Device information" and in the special diagnostics of the CP.

Because only one connection is configured in the "Devices &amp; Networks" editor, the display represents the status of all TCP connections to the various clients.

If no client has yet established a connection, "Passive connection establishment in progress" is displayed. As soon as a client has established a connection, "Connection established" is displayed. It is not possible to determine how many clients are currently connected to the CP.

###### Response to errors

In certain error situations, the CP needs to terminate and then re-establish the connection to be able to return to the basic status. This action is handled by the MODBUSCP instruction. All existing connections via port 502 are then terminated.

###### Tips for the user program

If there are multiple connections via port 502, it is not possible to tell in the user program which client sent the current Modbus/TCP request. If the clients use different UNIT numbers, a distinction can be made by evaluating these in the program.

---

**See also**

[Configuring CP as Modbus/TCP server (S7-300, S7-400)](#configuring-cp-as-modbustcp-server-s7-300-s7-400)

##### Startup behavior of the CP 343-1 and CP 443-1 (S7-300, S7-400)

The startup of the CP is divided into the following phases:

- Initialization (CP network on)

  As soon as power is applied to the CP, the firmware on the CPU is prepared for operation after running through a hardware test program.
- Parameter assignment

  During the parameter assignment, the CP receives the module parameters assigned to the current slot. The CP is now ready for operation.

#### Parameter data block (S7-300, S7-400)

##### Parameter assignment of the Modbus communication

For communication over a CP 343 and a CP 443, the connection must be configured in the "Devices &amp; Networks" editor.

Several connections to different communications partners can be configured and established at the same time. The number of simultaneously established connections depends on the CPU and the CP being used.

**Parameter data block**

The data required for assignment of the connections and processing of the Modbus/TCP frames is defined in the PLC data type MB_CP_PARAM. This PLC data type includes a structure for the connection-specific data and the Modbus parameters. Each instance of the "MODBUSCP" instruction requires a unique connection. Therefore, you create a separate connection to the respective communication partner in the "Devices &amp; Networks" editor for each instance of the instruction.

Each of these connections requires one instance of the PLC data type in a data block. The connection data and the Modbus parameters are defined in this instance. The data block can be expanded for each additional connection or you can create a new data block.

The parameter data block can contain the configuration data of all connections. You can also create a separate parameter data block for each connection. This data block or these data blocks are intended for connection and Modbus Data only; do not use it/them to save any other data.

> **Note**
>
> If there is more than one CP in a station and Modbus/TCP connections are configured via these, connections with the same ID cannot be saved in the same parameter data block. In this case, a separate parameter data block must be created for each CP.

Each parameter begins with the prefix "ID_x_", whereby x stands for the number of the connection ID. In this online help, this prefix is omitted to improve clarity.

![MODBUS_PARAM_CP](images/107022197259_DV_resource.Stream@PNG-en-US.PNG)

MODBUS_PARAM_CP

**Configuration**

![Parameter assignment of the Modbus communication](images/54763499531_DV_resource.Stream@PNG-en-US.png)

- Connection parameters

  In the first block, the connection-specific parameters "id" and "laddr" are defined. Based on these parameters, the connection configured in the "Devices &amp; Networks" editor can be assigned.
- Modbus/TCP parameters

  The data required for the mode and address reference is saved in the Modbus/TCP parameters, for example the mode of the S7 as Modbus/TCP server or Modbus/TCP client, the Modbus/TCP register addresses and the numbers of the DBs in which the data is mapped. You must keep to the data structure of the Modbus/TCP parameters because they cannot be processed correctly otherwise.

**Configuration options**

You have two options for configuring the connection and Modbus/TCP parameters.

1. Option:  
   Create an object of type MB_CP_PARAM under Technology Objects with "Insert new object" under Modbus. A parameter data block is created. Parameters can be assigned using an editor called via "Configuration". Due to the clear graphic user interface it is recommended to use the editor for editing the parameter data block.
2. Option:

   Create a new global data block and open it. Add a parameter and select the data type **MB_CP_PARAM** for this parameter. If this data type is not displayed in the drop-down list, enter it manually.

   You can insert several instances in one data block with this option.

**Changing the values**

The values in the parameter data block must not be changed during runtime. After the parameters have been changed, the Modbus block must be reinitialized with "Init" = TRUE.

##### Connection parameters

The first two parameters of the block are connection parameters that are used internally in the MODBUSCP instruction for the AG_SEND/AG_RECV or AG_LSEND/AG_LRECV calls.

| Parameter | Description |
| --- | --- |
| id | A connection ID is assigned for each configured connection in the TIA Portal ("Devices &amp; Networks" editor). The connection ID uniquely describes the connection from the CPU via the CP to the link partner. The number from the connection configuration is entered here. The range of values for this parameter is 1 to 64. |
| laddr | The "laddr" parameter is the base address of the CP from the "device view" (I address). The configured value is entered here. The range of values for this parameter depends on the CPU. The "id" and "laddr" parameters can also be taken from the "Properties &gt; General &gt; Local ID" mask of the TCP connection. |

##### Modbus/TCP parameters

The remaining parameters specify the mode of the Modbus/TCP communication and the mapping of the Modbus/TCP addresses to the SIMATIC addresses. Up to 8 data areas can be set. At least the first of these data areas must be defined; the other 7 are optional.

| Parameter | Description |  |  |
| --- | --- | --- | --- |
| server_client | This parameter distinguishes between client and server mode. If the input is TRUE, the "S7 is server" mode is used. If the setting is FALSE, the "S7 is client" mode is used. |  |  |
| single_write | In "S7 is client" mode, the function codes 5 and 6 are used with the "single_write" = TRUE parameter for write jobs with length 1. If "single_write" = FALSE, function codes 15 and 16 are used for all write jobs. |  |  |
| data_type_x | The "data_type_x" parameter specifies which Modbus/TCP data type is mapped in this DB. If the value 0 is entered in data_type_x, the corresponding data area is not used. |  |  |
| **Identifier** | **Data type** | **Data width** |  |
| 0 | Area not used | – |  |
| 1 | Coils | Bit |  |
| 2 | Inputs | Bit |  |
| 3 | Holding register | Word |  |
| 4 | Input register | Word |  |
| db_x | The "db_x" parameter specifies the data block in which Modbus/TCP registers or bit values defined below are mapped. When using a global DB, the DB number 0 is not permitted because it is reserved for the system.   DB number 1 to 65535 (W#16#0001 to W#16#FFFF) |  |  |
| start_x, end_x | "start_x" specifies the first Modbus/TCP address that is mapped in data word 0 of the DB. The "end_x" parameter defines the address of the last Modbus/TCP address.  - When accessing registers, the data word number in the S7 DB in which the last Modbus/TCP address is entered is calculated as follows:   DBW number = (end_x – start_x) ∗ 2 - With bit access, the data byte number in the S7 DB in which the last Modbus/TCP address is entered is calculated as follows:   DBB number = (end_x – start_x) / 8   The defined data areas must not overlap. The "end_x" parameter must not be lower than "start_x". In case of an error, startup of the FB is aborted with an error. If both values are identical, one Modbus/TCP address (1 register or 1 bit value) is assigned.   Under "[Address mapping](#address-mapping-s7-300-s7-400)", there is an example of the mapping of the Modbus/TCP addresses to S7 memory areas. |  |  |

#### Description of MODBUSCP (S7-300, S7-400)

##### Description

The MODBUSCP instruction allows communication to be established between a CP 443-1 or CP 343-1 and a partner that supports the Modbus/TCP protocol. The function codes 1, 2, 3, 4, 5, 6, 15 and 16 are supported.

Depending on the parameter assignment, the instruction can be operated both as client and server. It is also possible to operate a CP as client and server at the same time. To do so, two connections configured in the "Devices &amp; Networks" editor and two calls of the instruction are required.

In terms of the library, there is no limitation regarding the maximum number of Modbus/TCP blocks running at the same time. There is, however, a CPU- and CP-dependent maximum number of PLC function calls that can run at the same time. The maximum number of PLC calls can be found in the CPU manual in "Technical specifications &gt; Communication". The CP manual specifies how many AG_SEND/AG_RECV or AG_LSEND/AG_LRECV blocks can be processed simultaneously by the CP.

**Tasks of the blocks**

- Calling the standard functions for data transfer between CPU and CP
- Generating Modbus/TCP-specific frame headers
- Checking the Modbus/TCP-specific frame headers when receiving
- Checking whether the addressed data areas exist
- Generating exception telegrams if an error has occurred (only when the S7 is the server)

  | Exception code | Meaning |
  | --- | --- |
  | 1 | The sent function code is not supported. |
  | 2 | There was access to an address that is non-existent or is not permitted. |
  | 3 | An invalid length was specified for this function code. |
- Data transfer from/to the set DB
- Time monitoring of the receipt of data
- License check

The MODBUSCP instruction can be used for the S7-300 as well as for the S7-400.

##### Operating principle of the instruction

**Initialization**

The instruction MODBUSCP is initialized with a positive edge at the "Init" input.

- The initialization parameters must be assigned according to the plant configuration.
- The initialization parameters are checked for plausibility and entered in the instance DB.
- The runtime parameters are not evaluated during startup.
- The data from the parameter data block are checked for validity.

If a positive edge is detected at the Init parameter, the above-mentioned actions are performed. If the check was completed without errors, Init is reset, Init_Error and Init_Status show 0.

If errors occur during the check, this is displayed at the outputs Init_Error and Init_Status. Modbus/TCP communication via this block is not possible as long as there is an Init error. The Init error must first be corrected.

**Cyclic mode**

In cyclic operation, the MODBUSCP instruction is called in OB1 or in a cyclic interrupt OB.

- The block functions are activated based on the runtime parameters.
- Changes to the runtime parameters are not evaluated while a job is in progress.
- Initialization parameters are not evaluated as long as initialization is not performed.

**Response to programming errors OB121**

If the Modbus/TCP instruction is not yet licensed for this CPU, OB121 is called.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **CPU STOP if OB121 is missing**  If OB121 is missing, the CPU changes to STOP mode and unforeseeable plant statuses can arise.  Before putting the plant into operation, make sure that OB121 exists. |  |

**Connection termination by the communication partner**

When the TCP connection is terminated by the communication partner due to system properties in the "S7 is server" mode, the next frame can only be received after 1 second.   
In this case, data can only be sent again after 150 ms in the "S7 is client" mode. This delay time is implemented by the instruction.

##### Job initialization for "S7 is client" or activation of the instruction for "S7 is server"

The output parameters are **displayed dynamically** and are therefore only pending for **1 CPU cycle**. This means they have to be copied to other memory areas for further processing or display in the monitoring table.

**S7 is client: Job initialization**

A positive edge at the trigger input ENQ initiates a job. Depending on the input parameters UNIT, DATA_TYPE, START_ADDRESS, LENGTH and WRITE_READ, a Modbus/TCP request is generated and sent to the partner station over the TCP/IP connection. The client waits for a reply from the server for the set MONITOR time.  
If there is a timeout (no reply from the server), the activated job is ended with an error. A new job can be initiated.

A validity check is performed after the reply has been received. If this check is successful, the required actions are performed and the job is ended without error and the output DONE_NDR is set. If errors were detected during the check, the job is ended with error, the ERROR bit is set and an error number is displayed in STATUS.

**S7 is server: Activation of the instruction**

The instruction is ready to receive a request from the client with a positive level at the ENQ_ENR trigger input. The server is passive in this case and waits for a frame from the client.

When the server receives a request, it checks the received frame. If the check is successful, the server sends a reply. The server signals the end of frame exchange with the bit DONE_NDR = TRUE. At this time, the executed function is indicated at the outputs UNIT, DATA_TYPE, START_ADDRESS, LENGTH and WRITE_READ.

A request with an error results in an error message. The ERROR bit is set, the error number is indicated in STATUS and the request from the client is not replied to.

**Data transfer CPU - CP**

Data is transferred between the CP and CPU using the standard blocks AG_SEND and AG_RECV or AG_LSEND and AG_LRECV.

If the user activates a job (S7 is client) or if the user receives a frame from the client (S7 is server), the FB calls the standard blocks for the CP in the required number and order.

If the CP receives a frame, 6 bytes are read initially with an AG_(L)RECV. These 6 bytes contain the length of the remainder of the frame. AG_(L)RECV is then called a second time with the remaining length. The user data is evaluated only after the frame has been fully received.

##### Parameters

The parameters of the MODBUSCP instruction are divided into two groups:

- Initialization parameters

  The initialization parameters are only evaluated with Init = TRUE and applied to the instance DB. The initialization parameters are identified with "Yes" in the "Init" column of the table.  
  A change of the initialization parameters during operation has no effect. After these parameters have been changed, for example in test mode, the instance DB must be reinitialized with "Init" = TRUE.
- Runtime parameters

  Runtime parameters can be changed during cyclic operation.

  In the "S7 is client" mode, however, it does not make any sense to change input parameters while a job is running. Preparations for the next job and the associated changes to the parameters should only start after the previous job was ended with DONE_NDR or ERROR.

  In the "S7 is server" mode, the output parameters may only be evaluated when DONE_NDR is set.

  The output parameters are displayed dynamically and are therefore only pending for 1 CPU cycle. This means they have to be copied to other memory areas for further processing or display in the variable table.

With the ranges of values of the various parameters, CPU-specific restrictions may need to be taken into account.

| Parameter | Decl. | Type | Description | Range of values | Init |
| --- | --- | --- | --- | --- | --- |
| [id](#id-db_param-and-init-parameters-s7-300-s7-400) | IN | WORD | Connection ID from the "Devices &amp; Networks" editor | 1 to 64 | Yes |
| [db_param](#id-db_param-and-init-parameters-s7-300-s7-400) | IN | BLOCK_DB | Number of the parameter DB | Depends on CPU | Yes |
| [REG_KEY_DB](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400) | IN | BLOCK_DB | Data block with the registry key for licensing | Depends on CPU | No |
| [MONITOR](#enq_enr-and-monitor-parameters-s7-300-s7-400) | IN | TIME | Monitoring time for receiving data from the link partner The minimum time that can be set is 20 ms | T#20ms to T#+24d20h31 m23s647ms | No |
| [ENQ_ENR](#enq_enr-and-monitor-parameters-s7-300-s7-400) | IN | BOOL | S7 is client: Job triggered on positive edge S7 is server: Ready to receive if positive level | TRUE/FALSE | No |
| LICENSED | OUT | BOOL | License status of block Block is licensed Block is not licensed | TRUE FALSE | No |
| BUSY | OUT | BOOL | Processing status of the AG_(L)SEND or AG_(L)RECV functions being processed not being processed | TRUE FALSE | No |
| DONE_NDR | OUT | BOOL | S7 is client: TRUE: Activated job completed without errors S7 is server: TRUE: Request from client was executed and reply was sent | TRUE/FALSE | No |
| [ERROR](#error-status-status_func-and-init_status-parameters-s7-300-s7-400) | OUT | BOOL | An error occurred No error occurred | TRUE FALSE | No |
| [STATUS](#error-status-status_func-and-init_status-parameters-s7-300-s7-400) | OUT | WORD | Error code | 0 to FFFF | No |
| [STATUS_FUNC](#error-status-status_func-and-init_status-parameters-s7-300-s7-400) | OUT | STRING[8] | Name of the function that caused the error at STATUS | Character | No |
| [IDENT_CODE](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400) | OUT | STRING[18] | Identification for licensing Request the license with this identification string. | Character | No |
| [Init_Error](#error-status-status_func-and-init_status-parameters-s7-300-s7-400) | OUT | BOOL | TRUE: An error occurred during initialization. | TRUE/FALSE | No |
| [Init_Status](#error-status-status_func-and-init_status-parameters-s7-300-s7-400) | OUT | WORD | Status of initialization | 0 to FFFF | No |
| [UNIT](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BYTE | Unit identifier (INPUT for CLIENT function, OUTPUT for SERVER function) | 0 to 255 | No |
| [DATA_TYPE](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BYTE | Data type to be processed (INPUT for CLIENT function, OUTPUT for SERVER function) |  | No |
| Coils | 1 |  |  |  |  |
| Inputs | 2 |  |  |  |  |
| Holding register | 3 |  |  |  |  |
| Input register | 4 |  |  |  |  |
| [START_ADDRESS](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | WORD | MODBUS start address (INPUT for CLIENT function, OUTPUT for SERVER function) | 0 to 65535 | No |
| [LENGTH](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | WORD | Number of values to be processed (INPUT for CLIENT function, OUTPUT for SERVER function) |  | No |
| Coils: Read function | 1 to 2000 |  |  |  |  |
| Coils: Write function | 1 to 1968 |  |  |  |  |
| Inputs: Read function | 1 to 2000 |  |  |  |  |
| Holding register: Read function | 1 to 125 |  |  |  |  |
| Holding register: Write function | 1 to 123 |  |  |  |  |
| Input register: Read function | 1 to 125 |  |  |  |  |
| [WRITE_READ](#done_ndr-data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BOOL | INPUT for CLIENT function, OUTPUT for SERVER function  Write access or read access | TRUE/FALSE | No |
| [Init](#id-db_param-and-init-parameters-s7-300-s7-400) | IN/OUT | BOOL | Initialization at positive edge | TRUE/FALSE | No |

You can find additional information on this topic in the Siemens Industry Online Support in the [FAQ with entry ID: 75312612](https://support.industry.siemens.com/cs/ww/en/view/75312612)

---

**See also**

[Call of the MODBUSCP instruction (S7-300, S7-400)](#call-of-the-modbuscp-instruction-s7-300-s7-400)

#### Licensing with the parameters IDENT_CODE and REG_KEY (S7-300, S7-400)

##### Description

The MODBUSCP instruction must be licensed on each CPU individually. Licensing takes place in two steps:

- Reading out the IDENT_CODE and
- Entering the registration key REG_KEY.

OB121 must be present in the CPU.

Proceed as follows to read out the IDENT_CODE:

1. Assign parameters to the MODBUSCP instruction in line with your requirements in a cyclic OB. Download the program to the CPU and set it to RUN.
2. Open the instance DB of the Modbus instruction and click the "Monitor all" button.
3. An 18-digit character string is displayed at the IDENT_CODE output.

   ![Modbus/TCP CP: IDENT_CODE in the DB](images/100126534539_DV_resource.Stream@PNG-en-US.png)

   Modbus/TCP CP: IDENT_CODE in the DB
4. Copy this string using copy/paste from the data block and paste it in the SOFTWARE REGISTRATION FORM. This form is included on the installation CD.

   Enter the license number from the product packaging in the form.

   ![Modbus/TCP CP: IDENT_CODE and license form](images/100126544267_DV_resource.Stream@PNG-en-US.png)

   Modbus/TCP CP: IDENT_CODE and license form
5. Send the form to [Customer Support](https://support.industry.siemens.com/my/ww/en/requests/#createRequest) using a service request. You will then receive the registration key for your CPU.

The registration key REG_KEY must be specified at each MODBUSCP instruction. You should save the REG_KEY in a global data block via which all MODBUSCP instructions receive the necessary registration key.

Proceed as follows to enter the registration key REG_KEY:

- Insert a new global data block with a unique symbolic name, for example "License_DB", using "Add new block…".
- Create a REG_KEY parameter in this block with the data type STRING[17].

  ![REG_KEY in DB](images/66691684107_DV_resource.Stream@PNG-en-US.png)

  REG_KEY in DB
- Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
- In the cyclic OB, enter the name "License_DB" at the parameter REG_KEY_DB of the MODBUSCP instruction.
- Download the modified blocks to the CPU. The registration key can be entered during runtime; a change from STOP -&gt; RUN is not necessary.

The Modbus/TCP communication using the MODBUSCP instruction is now licensed for this CPU, the output bit LICENSED is TRUE.

****Missing or incorrect licensing****

If you enter an incorrect registration key or none at all, the SF-LED (for S7-300) or INTF-LED (for S7-400) of the CPU flashes and a cyclic entry is made in the diagnostics buffer regarding the missing license. The error number for a missing license is W#16#A090.

![Diag buffer with A090](images/66709766283_DV_resource.Stream@PNG-en-US.png)

Diag buffer with A090

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **If OB121 is missing in the controller, the CPU is set to STOP.** |  |

In the case of a missing or incorrect registration key, the Modbus/TCP communication is processed but W#16#A090 "No valid license available" is always displayed at the STATUS output. The output bit LICENSED is FALSE.

#### Address mapping (S7-300, S7-400)

##### Interpretation of the MODBUS/TCP addresses

The MODBUS data model includes the following areas:

- Coils
- Inputs
- Holding register
- Input register

These memory areas are distinguished in some systems, for example, MODICON PLCs, by means of the register address or bit address. The holding register with offset 0, for example, is referred to as register 40001 (memory type 4xxxx, reference 0001).

This often causes confusion because some manuals describe and mean the register address of the application layer and others the register/bit address actually transferred in the protocol.

The MODBUSCP instruction uses the Modbus/TCP address actually transferred in its parameters start_x, end_x and START_ADDRESS. This means that register/bit addresses from 0000H to FFFFH can be transferred with each function code.

##### Example

The Modbus addresses can be specified in decimal or hexadecimal format in the parameter DB.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter** | **Decimal notation** | **Hexadecimal notation** | **Meaning** |
| data_type_1 | 1 | B#16#1 | Coils |
| db_1 | 10 | W#16#A | DB 10 |
| start_1 | 640 | W#16#280 | Start address: 640 |
| end_1 | 1250 | W#16#4E2 | End address:      1250 |
| data_type_2 | 3 | B#16#3 | Holding register |
| db_2 | 11 | W#16#B | DB 11 |
| start_2 | 0 | W#16#0 | Start address: 0 |
| end_2 | 499 | W#16#1F3 | End address:      499 |
| data_type_3 | 3 | B#16#3 | Holding register |
| db_3 | 12 | W#16#C | DB 12 |
| start_3 | 720 | W#16#2D0 | Start address: 720 |
| end_3 | 900 | W#16#384 | End address:      900 |

The figure below shows a comparison of the SIMATIC memory areas with the register-oriented and bit-oriented memory allocation of the Modbus/TCP devices. The figure references the parameter assignment described above.

**In the Modbus device**

The Modbus addresses shown in black relate to the data link layer; those shown in gray to the application layer.

**In SIMATIC**

The SIMATIC addresses shown in the "Offset" column are the offset in the DB. The Modbus register numbers are in the square brackets.

![Modbus/TCP: Address mapping](images/86974695435_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Address mapping

#### id, db_param, and Init parameters (S7-300, S7-400)

##### Description

**id**

A connection ID is assigned for each configured connection in STEP 7 ("Devices &amp; Networks" editor). The connection ID uniquely describes the connection from the CPU via the CP to the link partner. This connection ID is configured in the connection parameter block included in the parameter data block. This ID must be entered here.

The range of values for this parameter is 1 to 64.

**db_param**

The db_param parameter refers to the number of the parameter data block, which contains the MB_CP_PARAM PLC data type. The connection-specific and Modbus-specific parameters required for communication between the CPU and the link partner are stored in this parameter data block.

The range of values for this parameter depends on the CPU. The DB number 0 is not permitted because it is reserved for the system. The DB number is entered in plain text as "DBxy".

If you want to implement several connections, the parameter data block can include the necessary parameters of all connections in sequence. You can also create a separate parameter data block for each connection.

**Init**

The Modbus block is initialized with a positive edge at the parameter. Initialization can only be performed if no job is currently running. This must be ensured in the program with ENQ_ENR = FALSE and BUSY = FALSE.

> **Note**
>
> **On initialization, the configured connections are terminated and established again.**

---

**See also**

[Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400)
  
[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400)

#### ERROR, STATUS, STATUS_FUNC and Init_Status parameters (S7-300, S7-400)

##### Error evaluation

The MODBUSCP instruction has three status outputs for error diagnostics: STATUS, STATUS_FUNC and Init_Status.

**ERROR**

An error is detected when this output is set.

In "S7 is client" mode, the active job was completed with errors. The corresponding error number is indicated at the STATUS output.

In "S7 is server" mode, an error was detected in the request of the client or when sending the response. The corresponding error number is indicated at the STATUS output.

**STATUS**

If ERROR is set, the STATUS output indicates the error number. Status information continues to be indicated at this output.

The instructions MODBUSCP, MB_CPCLI and MB_CPSRV use the standard blocks SFC20, SFC24, SFC51 and SFC52 as well as AG_SEND/AG_LSEND and AG_RECV/AG_LRECV. The error messages of these instructions are passed unchanged to STATUS.

**STATUS_FUNC**

The name of the function which has caused the error is displayed at this parameter.

**Init_Status**

The output Init_Status displays error messages and status information during initialization.

Below is a listing of the error messages for specific instructions.

**Parameter STATUS for STATUS_FUNC = 'MODBUSCP' and parameter Init_Status**

| Status (hex) | Event text |  | Remedy |
| --- | --- | --- | --- |
| A001 | The parameter DB is too short. |  | Correct the length of the parameter DB. |
| A002 | The end_x parameter is lower than start_x. |  | Correct the information in start_x and end_x. |
| A003 | A DB to which Modbus addresses are to be mapped is too short. Minimum length:  For registers:  (end_x - start_x + 1) * 2 + 2 - For bit values: (end_x - start_x ) / 8 + 3 Other possible causes: • S7 is client: wrong call parameter • S7 is server: incorrect address range in the client request. The CP replies with an exception telegram. |  | Lengthen the DB. S7 is client:  Correct the job parameters START_ ADDRESS or LENGTH. S7 is server:  Change the client request. |
| A004 | Only S7 is client:  An invalid combination of DATA_TYPE and WRITE_READ was specified. |  | Correct the call parameters. Only data types 1 and 3 can be written. |
| A005 | S7 is client:  An invalid value was specified at the LENGTH parameter. S7 is server:  The number of registers/bits in the request is invalid. The CP replies with an exception telegram. |  | S7 is client:  Correct the LENGTH parameter. S7 is server:  Change the number in the request. |
| Ranges of values: |  |  |  |
| Read coils/inputs | 1 to 2000 |  |  |
| Write coils | 1 to 1968 |  |  |
| Read registers | 1 to 125 |  |  |
| Write holding registers | 1 to 123 |  |  |
| A006 | The area specified with DATA_TYPE, START_ADDRESS and LENGTH does not exist in data_type_1 to data_type_8.  S7 is server: The CP replies with an exception telegram. |  | S7 is client: Correct the parameter assignment combination DATA_TYPE, START_ ADDRESS and LENGTH. S7 is server: Change the client request or correct the parameter assignment for data_type_x. |
| A007 | S7 is client: An invalid monitoring time was set for MONITOR. A value &gt;= 20 ms must be entered. |  | Correct the parameter assignment. |
| A008 | The activated AG_RECV does not signal receipt within the configured monitoring time MONITOR, for example, partner is not ready. The connection is terminated and reestablished. |  | Check the settings and, if applicable, the error messages of the link partner. Check whether the link partner requires a specific UNIT identifier. |
| A009 | S7 is client: The received Transaction Identifier TI does not match the one sent. The connection is terminated and reestablished. |  | Record frames to check the data of the link partner. |
| A00A | S7 is client: The received UNIT does not match the one sent. The connection is terminated and reestablished. |  |  |
| A00B | S7 is client: The received function code is not the same as the one sent. S7 is server: An invalid function code was received. The CP responds with an exception message frame. |  | S7 is client:  Record frames to check the data of the link partner. S7 is server:  Change the client request. The MODBUSCP instruction processes the function codes 1, 2, 3, 4, 5, 6, 15 and 16. |
| A00C | The received byte count does not match the number of registers/bits. S7 is server: The CP sends an exception message frame. The connection is terminated and reestablished. |  | Record frames to check the data of the link partner. |
| A00D | Only for S7 is client: The register address/bit address or the number of registers/bits in the response is not the same as in the request. |  |  |
| A00E | The length information in the Modbus-specific frame header does not match the specified number of registers/bits or the byte count in the frame. The instruction discards the data. The connection is terminated and reestablished. |  | Record frames to check the data of the link partner |
| A00F | A Protocol Identifier unequal 0 has been received. The connection is terminated and reestablished. |  |  |
| A010 | A DB number was assigned twice in the parameters db_1 to db_8. |  | Correct the parameter assignment at db_x. |
| A011 | An invalid value was specified for the DATA_TYPE input parameter (valid values are 1, 2, 3 and 4). |  | Correct the call parameters. |
| A012 | The areas data_type_1 and data_type_2 set in the parameters overlap. |  | Correct the parameter assignment, The data areas must not contain any overlapping register areas. |
| A013 | The areas data_type_1 and data_type_3 set in the parameters overlap. |  |  |
| A014 | The areas data_type_1 and data_type_4 set in the parameters overlap. |  |  |
| A015 | The areas data_type_1 and data_type_5 set in the parameters overlap. |  |  |
| A016 | The areas data_type_1 and data_type_6 set in the parameters overlap. |  |  |
| A017 | The areas data_type_1 and data_type_7 set in the parameters overlap. |  |  |
| A018 | The areas data_type_1 and data_type_8 set in the parameters overlap. |  |  |
| A019 | One of the db_x parameters was set to 0 even though the associated data_type_x is set to &gt; 0. DB0 must not be used because it is reserved for the system. |  | Correct the parameter setting at db_x to &gt; 0. If you use a data collector FB, check the parameter assignment in CFC. |
| A01A | Incorrect length in the header: 3 to 253 bytes are permitted. The connection is terminated and reestablished. |  | Record frames to check the data of the link partner. |
| A01B | S7 is server and function code 5:  An invalid status for Coil was received. An exception telegram is sent. |  |  |
| A01E | Invalid data has been received that cannot be assigned. The connection is terminated and reestablished. |  | Check the error message of the link partner. If necessary, check the data by recording frames. |
| A01F | The MODBUSCP instruction is in an illegal operating state. |  | Contact Product Support. |
| A023 | The areas data_type_2 and data_type_3 set in the parameters overlap. |  | Correct the parameter assignment.  The data areas must not contain any overlapping register areas. |
| A024 | The areas data_type_2 and data_type_4 set in the parameters overlap. |  |  |
| A025 | The areas data_type_2 and data_type_5 set in the parameters overlap. |  |  |
| A026 | The areas data_type_2 and data_type_6 set in the parameters overlap. |  |  |
| A027 | The areas data_type_2 and data_type_7 set in the parameters overlap. |  |  |
| A028 | The areas data_type_2 and data_type_8 set in the parameters overlap. |  |  |
| A034 | The areas data_type_3 and data_type_4 set in the parameters overlap. |  |  |
| A035 | The areas data_type_3 and data_type_5 set in the parameters overlap. |  |  |
| A036 | The areas data_type_3 and data_type_6 set in the parameters overlap. |  |  |
| A037 | The areas data_type_3 and data_type_7 set in the parameters overlap. |  |  |
| A038 | The areas data_type_3 and data_type_8 set in the parameters overlap. |  |  |
| A045 | The areas data_type_4 and data_type_5 set in the parameters overlap. |  |  |
| A046 | The areas data_type_4 and data_type_6 set in the parameters overlap. |  |  |
| A047 | The areas data_type_4 and data_type_7 set in the parameters overlap. |  |  |
| A048 | The areas data_type_4 and data_type_8 set in the parameters overlap. |  |  |
| A056 | The areas data_type_5 and data_type_6 set in the parameters overlap. |  |  |
| A057 | The areas data_type_5 and data_type_7 set in the parameters overlap. |  |  |
| A058 | The areas data_type_5 and data_type_8 set in the parameters overlap. |  |  |
| A067 | The areas data_type_6 and data_type_7 set in the parameters overlap. |  |  |
| A068 | The areas data_type_6 and data_type_8 set in the parameters overlap. |  |  |
| A078 | The areas data_type_7 and data_type_8 set in the parameters overlap. |  |  |
| A079 | The connection ID specified for the id parameter is not included in the parameter DB. |  | Correct the parameter assignment at the id input. |
| A07A | An invalid value was specified for the id parameter (value range from 1 to 64). |  |  |
| A07B | The specified ID is included twice in the parameter DB. |  | Correct the parameter assignment in the parameter DB. |
| A07C | An invalid value was specified for the data_type_x parameter (valid values are 0 to 4). |  |  |
| A07D | The data_type_1 parameter does not contain an entry. The parameter area "_1" is the initial area and must be set. |  | Correct the parameter assignment in the parameter DB. |
| A07E | The number of the instance DB of the MODBUSCP instruction was specified in db_x. |  |  |
| A080 | The Modbus block has not yet been initialized. |  | After transfer of the IDB to the CPU, the Modbus block must be initialized with Init = TRUE. Check whether an error occurred during initialization. |
| A081 | Only for S7 is client and function code 5:  The data of the response is not the echo of the request. |  | Record frames to check the data of the link partner. |
| A082 | Only for S7 is client and function code 6:  The received register value is not the same as the one sent. |  | Record frames to check the data of the link partner. |
| A083 | S7 is client: A job was triggered while the previous job is still in progress. The job is not executed. This is a status information. The ERROR bit is not set.   An attempt was made to initialize the block while a job was running or while ENQ_ENR was set. |  | Only start a new job when the previous job ended with DONE_ NDR = TRUE or ERROR = TRUE.  Do not start initialization until no job is running any longer. Set ENQ_ENR = FALSE. |
| A085 | Due to illegal write access, an internal error occurred during the license check. |  | Check that there is no illegal write access to the license DB in the S7 program. The structure of REG_KEY must not be modified. If necessary, contact Product Support. |
| A086 | An attempt was made to write to a write-protected data block. |  | Remove the write protection or use a different DB. |
| A090 | The MODBUSCP instruction has not yet been licensed for this CPU. This is status information. The ERROR bit is not set. MODBUS communication is running even without a license. |  | Read out the identification code for this CPU at the IDENT_CODE output and request the registration key. Refer to the section "[Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400)". |
| A091 | Only for S7 is client: An exception telegram with exception code 1 was received as the reply. |  | The link partner does not support the requested function. |
| A092 | Only for S7 is client: An exception telegram with exception code 2 was received as the reply. There was access to a non-existent or illegal address on the link partner. |  | Correct LENGTH or START_ADDRESS in the FB call. |
| A093 | Only for S7 is client: An exception telegram with exception code 3 was received as the reply. |  | The link partner cannot process the received frame (for example, it does not support the requested length). |
| A094 | Only for S7 is client: An exception telegram with exception code 4 was received as the reply. |  | The link partner is in a status in which it cannot process the received frame. |
| A095 | Only for S7 is client: An exception telegram with an unknown exception code was received as the reply. |  | Check the error messages of the link partner and if necessary record the frames to check the data. |

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400)

#### DONE_NDR, DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT parameters (S7-300, S7-400)

##### Description

In "S7 is client" mode, these parameters are input parameters; in "S7 is server" mode, these parameters are output parameters.

**DATA_TYPE**

The DATA_TYPE parameter indicates which Modbus/TCP data type is processed with the current frame. The following values are permitted:

| Symbol | Meaning |
| --- | --- |
| Coils | B#16#1 |
| Inputs | B#16#2 |
| Holding register | B#16#3 |
| Input register | B#16#4 |

The different data types are directly related to the used function codes.

| Data type | DATA_TYPE | Function | Length | single_write | Function code |
| --- | --- | --- | --- | --- | --- |
| Coils | 1 | read | any | irrelevant | 1 |
| Coils | 1 | write | 1 | TRUE | 5 |
| Coils | 1 | write | 1 | FALSE | 15 |
| Coils | 1 | write | &gt; 1 | irrelevant | 15 |
| Inputs | 2 | read | any | irrelevant | 2 |
| Holding register | 3 | read | any | irrelevant | 3 |
| Holding register | 3 | write | 1 | TRUE | 6 |
| Holding register | 3 | write | 1 | FALSE | 16 |
| Holding register | 3 | write | &gt; 1 | irrelevant | 16 |
| Input register | 4 | read | any | irrelevant | 4 |

**START_ADDRESS**

The START_ADDRESS parameter determines the first Modbus/TCP address that is written or read.

**LENGTH**

The LENGTH parameter determines the number of Modbus/TCP values that are written or read.

With read functions, a maximum of 125 registers are possible per frame for holding and input registers. For coils and inputs, a maximum of 2000 bits are possible. With write functions, the maximum number of registers is 123 for holding registers and 1968 bits for coils. The registers or bit values processed with a request frame must be located within one DB.

**WRITE_READ**

This parameter defines whether a read or write function is to be performed. If the input/output has the value FALSE, it is a read function. The value TRUE defines a write function.

Only holding registers and coils can be written to. Input registers and inputs can only be read.

**UNIT**

In the "S7 is client" function, the UNIT parameter is an input parameter. This input needs to be set according to the requirements. The instruction applies this value to the request and checks the value when it receives the reply.

The UNIT parameter is typically used with protocol converters to address serial slaves concealed behind a common IP address.

Most devices can be addressed with UNIT = 1.

In the "S7 is server" function, the UNIT parameter is an output parameter. The instruction applies the value from the request to the response. When the job is completed, the output is set to the received value.

**DONE_NDR**

In "S7 is client" operating mode, the active job was completed without errors. In case of a reading function, the response data from the server has already been entered in the data block; for a writing function, the response to the request message was received by the server.

In "S7 is server" operating mode, the output displays a message traffic completed without errors with the client. The job parameters of the client are displayed in the parameters DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT. These output are only valid as long as DONE_NDR is set.

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400)

#### ENQ_ENR and MONITOR parameters (S7-300, S7-400)

##### Description

**ENQ_ENR**

"S7 is client" operating mode:  
The data transfer is initiated with a positive edge at ENQ_ENR. The request is generated with the values of the input parameters DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT. A new message frame can only be sent if the previous message frame was completed with DONE_NDR or ERROR.

"S7 is server" operating mode:  
The instruction is activated with a positive level at the ENQ_ENR input. Frames can be received from the client.  
If the ENQ_ENR input is not set and a connection exists, the received data is discarded.

**MONITOR**

The monitoring time MONITOR monitors the incoming data from the link partner. The monitoring time is specified in the time format T#... A monitoring time of approximately 1.5 s is recommended.

In "S7 is client" mode, the MONITOR time monitors the arrival of the complete response from the server. If the monitoring time is exceeded, the activated job is ended with an error. The time is started after the request has been sent and stopped after the response has been entirely received.

In "S7 is server" mode, the input of the second part of the frame is monitored with the MONITOR time. If the monitoring time is exceeded, an error is reported. The time is started after receipt of the MODBUS/TCP-specific telegram header and stopped after the request has been entirely received.

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400)

### MODBUSCP V1 (S7-300, S7-400)

This section contains information on the following topics:

- [General Information (S7-300, S7-400)](#general-information-s7-300-s7-400-1)
- [Commissioning (S7-300, S7-400)](#commissioning-s7-300-s7-400-1)
- [Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400-1)
- [Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400-1)
- [Licensing with the parameters IDENT_CODE and REG_KEY (S7-300, S7-400)](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1)
- [Address mapping (S7-300, S7-400)](#address-mapping-s7-300-s7-400-1)
- [ID and DB_PARAM parameters (S7-300, S7-400)](#id-and-db_param-parameters-s7-300-s7-400)
- [DONE_NDR, ERROR, STATUS and STATUS_FUNC parameters (S7-300, S7-400)](#done_ndr-error-status-and-status_func-parameters-s7-300-s7-400)
- [DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT parameters (S7-300, S7-400)](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400)
- [ENQ_ENR and MONITOR parameters (S7-300, S7-400)](#enq_enr-and-monitor-parameters-s7-300-s7-400-1)

#### General Information (S7-300, S7-400)

##### General

The MODBUSCP instruction is a software product for the communication processors CP 343-1 and CP 443-1.

This instruction establishes communication between a CP 443-1 or CP 343-1 and a partner that supports the Modbus/TCP protocol.

The TCP/IP connections over the CP are static connections that are not terminated during error-free operation.

With the TCP stack used on the CP, the STEP 7 connection configuration only allows one use of a particular port number. Certain CP types can maintain and operate connections to multiple clients simultaneously through the local port 502.

The technical details of this topic are explained in the section "[Using connections on port 502](#using-connections-on-port-502-s7-300-s7-400-1)".

Data transmission takes place according to the client-server principle.

The SIMATIC S7 can be operated as client as well as server during the transmission.

##### Step-by-step instructions

1. Configuration of the CP as [server](#configuring-cp-as-modbustcp-server-s7-300-s7-400-1) or [client](#configuring-cp-as-modbustcp-client-s7-300-s7-400-1).
2. Call of the MODBUSCP instruction in the necessary OBs.

   - see [Commissioning](#call-of-the-modbuscp-instruction-s7-300-s7-400-1)
3. Parameter assignment of the parameter DB according to the requirements (ID, client/server, Modbus register, DB areas, etc.).

   - see [Parameter data block](#parameter-data-block-s7-300-s7-400-1)
4. Parameter assignment of the Modbus block for initialization and for runtime.

   - see [Operating principle of the instruction](#description-of-modbuscp-s7-300-s7-400-1)
5. Download of the user program to the CPU and licensing of the Modbus block for this CPU.

   - see [Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1)

#### Commissioning (S7-300, S7-400)

This section contains information on the following topics:

- [Configuring CP as Modbus/TCP client (S7-300, S7-400)](#configuring-cp-as-modbustcp-client-s7-300-s7-400-1)
- [Configuring CP as Modbus/TCP server (S7-300, S7-400)](#configuring-cp-as-modbustcp-server-s7-300-s7-400-1)
- [Call of the MODBUSCP instruction (S7-300, S7-400)](#call-of-the-modbuscp-instruction-s7-300-s7-400-1)
- [Using connections on port 502 (S7-300, S7-400)](#using-connections-on-port-502-s7-300-s7-400-1)
- [Startup behavior of the CP 343-1 and CP 443-1 (S7-300, S7-400)](#startup-behavior-of-the-cp-343-1-and-cp-443-1-s7-300-s7-400-1)

##### Configuring CP as Modbus/TCP client (S7-300, S7-400)

###### Requirements

- "Devices &amp; Networks" editor is open.
- The following hardware is available in the "Device view":

  - S7 300/400, e.g. 315-2 DP or 414-2 DP
  - Communication processor CP 343-1/443-1

###### Assigning CP parameters

1. Select the CP.
2. Add a subnet to the PROFINET interface of the CP in the Inspector window under "Properties &gt; General &gt; Ethernet addresses".
3. Enter the IP address as well as the subnet mask.

![Assigning CP parameters](images/85864937611_DV_resource.Stream@PNG-en-US.png)

###### Add TCP connection

1. In the network view, click "Connections".
2. Select the connection type "TCP connection".
3. In the shortcut menu of the CPU, select the "Create new connection" command.
4. Select "Unspecified" as connection partner.
5. Select the communication module as local interface.
6. Select the function "Establish active connection".
7. Click "Add" and close the dialog.

![Add TCP connection](images/85882083211_DV_resource.Stream@PNG-en-US.png)

###### Assigning TCP connection parameters

1. Enter the IP address of the partner in the Inspector window under "Properties &gt; General &gt; General".

   ![Assigning TCP connection parameters](images/85867097739_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85867097739_DV_resource.Stream@PNG-en-US.png)
2. Under "Properties &gt; General &gt; Local ID", enter the local ID that you are configuring for the Modbus/TCP connection at the "MODBUSCP" block.

   You also need the value of the "LADDR" parameter for the parameter assignment of the "MODBUSCP" block; see [Parameter data block](#parameter-data-block-s7-300-s7-400-1).

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)
3. Under "Properties &gt; General &gt; Address details" enter "502" as partner port.

   Apply the default value for the local CP port, e.g. 2000.

![Assigning TCP connection parameters](images/85909676683_DV_resource.Stream@PNG-en-US.png)

##### Configuring CP as Modbus/TCP server (S7-300, S7-400)

###### Requirements

- "Devices &amp; Networks" editor is open.
- The following hardware is available in the "Device view":

  - S7 300/400, e.g. 315-2 DP or 414-2 DP
  - Communication processor CP 343-1/443-1

###### Assigning CP parameters

1. Select the CP.
2. Add a subnet to the PROFINET interface of the CP in the Inspector window under "Properties &gt; General &gt; Ethernet addresses".
3. Enter the IP address as well as the subnet mask.

![Assigning CP parameters](images/85864937611_DV_resource.Stream@PNG-en-US.png)

###### Add TCP connection

1. In the network view, click "Connections".
2. Select the connection type "TCP connection".
3. In the shortcut menu of the CPU, select the "Create new connection" command.
4. Select "Unspecified" as connection partner.
5. Select the communication module as local interface.
6. Deactivate the function "Establish active connection".
7. Click "Add" and close the dialog.

![Add TCP connection](images/85867088907_DV_resource.Stream@PNG-en-US.png)

###### Assigning TCP connection parameters

1. In the Inspector window under "Properties &gt; General &gt; Local ID", enter the local ID that you are configuring for the Modbus/TCP connection at the "MODBUSCP" block.

   You also need the value of the "LADDR" parameter for the parameter assignment of the "MODBUSCP" block; see [Parameter data block](#parameter-data-block-s7-300-s7-400-1).

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85864928779_DV_resource.Stream@PNG-en-US.png)
2. Under "Properties &gt; General &gt; Address details" enter "502" as local CP port.

   ![Assigning TCP connection parameters](images/85909685771_DV_resource.Stream@PNG-en-US.png)

   ![Assigning TCP connection parameters](images/85909685771_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Using connections on port 502 (S7-300, S7-400)](#using-connections-on-port-502-s7-300-s7-400-1)
  
[Add-on blocks for Modbus/TCP communication](http://support.automation.siemens.com/WW/view/en/62830463)

##### Call of the MODBUSCP instruction (S7-300, S7-400)

###### Requirement and basics

The MODBUSCP instruction can be used as of **STEP7 V14 (TIA Portal)**.

The MODBUSCP instruction is based on the Modbus Application Protocol Specification V1.1b3, April 26, 2012 - see [Modbus home page](http://www.modbus.org).

###### Call of the instruction

The MODBUSCP instruction must be installed in two OBs for correct program execution:

- In the startup OB100 and
- in a cyclic OB (OB1 or in a time-controlled OB, e.g., OB35)

The same instance data block must be used in both. It is not permitted to call the MODBUSCP instruction in OB1 and in a time-controlled OB (e.g., OB35) at the same time. The OB121 must be present in the CPU. For more detailed information on this, see [Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1).

###### Inserting the Modbus block

Open the "COMPLETE RESTART [OB100]" block. If this block does not exist in the program blocks, insert it with "Insert new block &gt; Organization block &gt; Startup &gt; COMPLETE RESTART [OB 100]".  
The MODBUSCP instruction exists in the Task Card, pane and "Instructions &gt; Communication &gt; Other" folder. In it, open the "MODBUS TCP" folder and drag the MODBUSCP instruction into the OB100 block.

Under "System blocks &gt; Program resources", the lower-level instructions MB_CPCLI (FB76) and MB_CPSRV (FB77) are displayed in addition to MODBUSCP (FB75). The lower-level instructions may not also be called in an OB. In addition, the internally called communication instructions AG_(L)SEND (FC5/FC50), AG_(L)RECV (FC6/FC60), and AG_CNTRL (FC10) are displayed.

Open the "Main [OB1]" block or a cyclic block and drag the MODBUSCP [FB75] instruction into the OB. Select the MODBUSCP_DB data block from the OB100 call as instance data block. Do not create a new instance data block.

###### Versions of the PLC blocks

If you are using the migrated blocks in V14, the following versions are used:

- Use of an S7-300:

  - AG_SEND V4.2
  - AG_RECV V4.7
  - AG_CNTRL V1.4
- Use of an S7-400:

  - AG_LSEND V3.1
  - AG_LRECV V3.1
  - AG_CNTRL V1.0

If you are using the integrated blocks in V14, you need the following versions in the "SIMATIC NET CP" library:

- Use of an S7-300:

  - AG_SEND V1.2
  - AG_RECV V1.2
  - AG_CNTRL V1.1
- Use of an S7-400:

  - AG_LSEND V1.1
  - AG_LRECV V1.1
  - AG_CNTRL V1.1

##### Using connections on port 502 (S7-300, S7-400)

Some CPs can multiplex TCP connections. This means that several Modbus/TCP clients can connect to port 502 of the CP. The CP functions as a Modbus/TCP server.

> **Note**
>
> For older firmware versions: Note that only one connection is configured regardless of how many clients access the CP as server.
>
> For newer CPs or firmware versions: You can configure multiple connections for port 502.

You will find more information in the CP data and in the firmware or at the link: [SIMATIC Modbus/TCP](https://support.industry.siemens.com/cs/de/en/view/104946406)

###### Requirements

To be able to use this function, the following settings need to be made in the connection parameter assignment:

- CP is server
- Port 502 as local port
- Unspecified TCP connection in "Devices &amp; Networks"
- Passive connection establishment

###### Number of connections

Via port 502, the CP can communicate with a maximum of 4 clients at any one time.

###### Displaying the status of the connection

The status of the connection can be displayed in the "Devices &amp; Networks" editor in the Inspector window under "Diagnostics &gt; Device information" and in the special diagnostics of the CP.

Because only one connection is configured in the "Devices &amp; Networks" editor, the display represents the status of all TCP connections to the various clients.

If no client has yet established a connection, "Passive connection establishment in progress" is displayed. As soon as a client has established a connection, "Connection established" is displayed. It is not possible to determine how many clients are currently connected to the CP.

###### Response to errors

In certain error situations, the CP needs to terminate and then re-establish the connection to be able to return to the basic status. This action is handled by the MODBUSCP instruction. All existing connections via port 502 are then terminated.

###### Tips for the user program

If there are multiple connections via port 502, it is not possible to tell in the user program which client sent the current Modbus/TCP request. If the clients use different UNIT numbers, a distinction can be made by evaluating these in the program.

---

**See also**

[Configuring CP as Modbus/TCP server (S7-300, S7-400)](#configuring-cp-as-modbustcp-server-s7-300-s7-400-1)

##### Startup behavior of the CP 343-1 and CP 443-1 (S7-300, S7-400)

The startup of the CP is divided into the following phases:

- Initialization (CP network on)

  As soon as power is applied to the CP, the firmware on the CPU is prepared for operation after running through a hardware test program.
- Parameter assignment

  During the parameter assignment, the CP receives the module parameters assigned to the current slot. The CP is now ready for operation.

#### Parameter data block (S7-300, S7-400)

##### Parameter assignment of the Modbus communication

For communication over a CP 343 and a CP 443, the connection must be configured in the "Devices &amp; Networks" editor.

Several connections to different communications partners can be configured and established at the same time. The number of simultaneously established connections depends on the CPU and the CP being used.

**Parameter data block**

The data required for assignment of the connections and processing of the Modbus/TCP frames is defined in the PLC data type MB_CP_PARAM. This PLC data type includes a structure for the connection-specific data and the Modbus parameters. Each instance of the "MODBUSCP" instruction requires a unique connection. Therefore, you create a separate connection to the respective communication partner in the "Devices &amp; Networks" editor for each instance of the instruction.

Each of these connections requires one instance of the PLC data type in a data block. The connection data and the Modbus parameters are defined in this instance. The data block can be expanded for each additional connection or you can create a new data block.

The parameter data block can contain the configuration data of all connections. You can also create a separate parameter data block for each connection. This data block or these data blocks are intended for connection and Modbus parameters only; do not use it/them to save any other parameters.

> **Note**
>
> If there is more than one CP in a station and Modbus/TCP connections are configured via these, connections with the same ID cannot be saved in the same parameter data block. In this case, a separate parameter data block must be created for each CP.

Each parameter begins with the prefix "ID_x_", whereby x stands for the number of the connection ID. In this online help, this prefix is omitted to improve clarity.

![MODBUS_PARAM_CP](images/86146006411_DV_resource.Stream@PNG-de-DE.png)

MODBUS_PARAM_CP

**Configuration**

![Parameter assignment of the Modbus communication](images/54763499531_DV_resource.Stream@PNG-en-US.png)

- Connection parameters

  In the first block, the connection-specific parameters "id" and "laddr" are defined. Based on these parameters, the connection configured in the "Devices &amp; Networks" editor can be assigned.
- Modbus/TCP parameters

  The data required for the mode and address reference is saved in the Modbus/TCP parameters, for example the mode of the S7 as Modbus/TCP server or Modbus/TCP client, the Modbus/TCP register addresses and the numbers of the DBs in which the data is mapped. You must keep to the data structure of the Modbus/TCP parameters because they cannot be processed correctly otherwise.

**Configuration options**

You have two options for configuring the connection and Modbus/TCP parameters.

1. Option:

   Create a new global data block and open it. Add a parameter and select the data type **MB_CP_PARAM** for this parameter. If this data type is not displayed in the drop-down list, enter it manually.

   You can insert several instances in one data block with this option.
2. Option:

   Create a new data block with "Add new block" and select **MB_CP_PARAM** as "Type". The new data block with the inserted connection and Modbus structure opens.

   This block is read-only. You cannot add any additional parameters. Existing parameters can be edited.

**Changing the values**

The values in the parameter data block must not be changed during runtime. The CPU must be restarted with STOP -&gt; RUN after the parameters have been changed.

##### Connection parameters

The first two parameters of the block are connection parameters that are used internally in the MODBUSCP instruction for the AG_SEND/AG_RECV or AG_LSEND/AG_LRECV calls.

| Parameter | Description |
| --- | --- |
| id | A connection ID is assigned for each configured connection in the TIA Portal ("Devices &amp; Networks" editor). The connection ID uniquely describes the connection from the CPU via the CP to the link partner. The number from the connection configuration is entered here. The range of values for this parameter is 1 to 64. |
| laddr | The "laddr" parameter is the base address of the CP from the "device view" (I address). The configured value is entered here. The range of values for this parameter depends on the CPU. The "id" and "laddr" parameters can also be taken from the "Properties &gt; General &gt; Local ID" mask of the TCP connection. |

##### Modbus/TCP parameters

The remaining parameters specify the mode of the Modbus/TCP communication and the mapping of the Modbus/TCP addresses to the SIMATIC addresses. Up to 8 data areas can be set. At least the first of these data areas must be defined; the other 7 are optional.

| Parameter | Description |  |  |
| --- | --- | --- | --- |
| server_client | This parameter distinguishes between client and server mode. If the input is TRUE, the "S7 is server" mode is used. If the setting is FALSE, the "S7 is client" mode is used. |  |  |
| single_write | In "S7 is client" mode, the function codes 5 and 6 are used with the "single_write" = TRUE parameter for write jobs with length 1. If "single_write" = FALSE, function codes 15 and 16 are used for all write jobs. |  |  |
| data_type_x | The "data_type_x" parameter specifies which Modbus/TCP data type is mapped in this DB. If the value 0 is entered in data_type_x, the corresponding data area is not used. |  |  |
| **Identifier** | **Data type** | **Data width** |  |
| 0 | Area not used | – |  |
| 1 | Coils | Bit |  |
| 2 | Inputs | Bit |  |
| 3 | Holding register | Word |  |
| 4 | Input register | Word |  |
| db_x | The "db_x" parameter specifies the data block in which Modbus/TCP registers or bit values defined below are mapped. When using a global DB, the DB number 0 is not permitted because it is reserved for the system. If a data collector block is used in CFC, the DB number 0 must be specified.  DB number 1 to 65535 (W#16#0001 to W#16#FFFF) |  |  |
| start_x, end_x | "start_x" specifies the first Modbus/TCP address that is mapped in data word 0 of the DB. The "end_x" parameter defines the address of the last Modbus/TCP address.  - When accessing registers, the data word number in the S7 DB in which the last Modbus/TCP address is entered is calculated as follows:   DBW number = (end_x – start_x) ∗ 2 - With bit access, the data byte number in the S7 DB in which the last Modbus/TCP address is entered is calculated as follows:   DBB number = (end_x – start_x) / 8   The defined data areas must not overlap. The "end_x" parameter must not be lower than "start_x". In case of an error, startup of the FB is aborted with an error. If both values are identical, one Modbus/TCP address (1 register or 1 bit value) is assigned.   Under "[Address mapping](#address-mapping-s7-300-s7-400-1)", there is an example of the mapping of the Modbus/TCP addresses to S7 memory areas. |  |  |

#### Description of MODBUSCP (S7-300, S7-400)

##### Description

The MODBUSCP instruction allows communication to be established between a CP 443-1 or CP 343-1 and a partner that supports the Modbus/TCP protocol. The function codes 1, 2, 3, 4, 5, 6, 15 and 16 are supported.

Depending on the parameter assignment, the instruction can be operated both as client and server. It is also possible to operate a CP as client and server at the same time. To do so, two connections configured in the "Devices &amp; Networks" editor and two calls of the instruction are required.

In terms of the library, there is no limitation regarding the maximum number of Modbus/TCP blocks running at the same time. There is, however, a CPU- and CP-dependent maximum number of PLC function calls that can run at the same time. The maximum number of PLC calls can be found in the CPU manual in "Technical specifications &gt; Communication". The CP manual specifies how many AG_SEND/AG_RECV or AG_LSEND/AG_LRECV blocks can be processed simultaneously by the CP.

**Tasks of the blocks**

- Calling the standard functions for data transfer between CPU and CP
- Generating Modbus/TCP-specific frame headers
- Checking the Modbus/TCP-specific frame headers when receiving
- Checking whether the addressed data areas exist
- Generating exception telegrams if an error has occurred (only when the S7 is the server)

  | Exception code | Meaning |
  | --- | --- |
  | 1 | The sent function code is not supported. |
  | 2 | There was access to an address that is non-existent or is not permitted. |
  | 3 | An invalid length was specified for this function code. |
- Data transfer from/to the set DB
- Time monitoring of the receipt of data
- License check

The MODBUSCP instruction can be used for the S7-300 as well as for the S7-400.

##### Operating principle of the instruction

**Startup characteristics of the instruction**

The MODBUSCP instruction is called once unconditionally in OB100.

- The initialization parameters must be assigned according to the plant configuration.
- The initialization parameters are checked for plausibility and entered in the instance DB.
- The runtime parameters are not evaluated during startup.

**Cyclic operation of the instruction**

In cyclic operation, the MODBUSCP instruction is called in OB1 or in a cyclic interrupt OB.

- The block functions are activated based on the runtime parameters.
- Changes to the runtime parameters are not evaluated while a job is in progress.
- Initialization parameters are not evaluated.

**Restart during commissioning**

A repeated CPU restart after changing the initialization parameters can be rather time-consuming during commissioning. The restart program part of the Modbus block can be run through by manually setting the "Init_Start" parameter in the static area. A job may not be in progress during manual initialization. All initialization parameters must be configured in the cyclic OB for correct initialization.

**Response to programming errors OB121**

If the Modbus/TCP instruction is not yet licensed for this CPU, OB121 is called.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **CPU STOP if OB121 is missing**  If OB121 is missing, the CPU changes to STOP mode and unforeseeable plant statuses can arise.  Before putting the plant into operation, make sure that OB121 exists. |  |

**Connection termination by the communication partner**

When the TCP connection is terminated by the communication partner due to system properties in the "S7 is server" mode, the next frame can only be received after 1 second.   
In this case, data can only be sent again after 150 ms in the "S7 is client" mode. This delay time is implemented by the instruction.

##### Job initialization for "S7 is client" or activation of the instruction for "S7 is server"

The output parameters are **displayed dynamically** and are therefore only pending for **1 CPU cycle**. This means they have to be copied to other memory areas for further processing or display in the monitoring table.

**S7 is client: Job initialization**

A positive edge at the trigger input ENQ initiates a job. Depending on the input parameters UNIT, DATA_TYPE, START_ADDRESS, LENGTH and WRITE_READ, a Modbus/TCP request is generated and sent to the partner station over the TCP/IP connection. The client waits for a reply from the server for the set MONITOR time.  
If there is a timeout (no reply from the server), the activated job is ended with an error. A new job can be initiated.

A validity check is performed after the reply has been received. If this check is successful, the required actions are performed and the job is ended without error and the output DONE_NDR is set. If errors were detected during the check, the job is ended with error, the ERROR bit is set and an error number is displayed in STATUS.

**S7 is server: Activation of the instruction**

The instruction is ready to receive a request from the client with a positive level at the ENQ_ENR trigger input. The server is passive in this case and waits for a frame from the client.

When the server receives a request, it checks the received frame. If the check is successful, the server sends a reply. The server signals the end of frame exchange with the bit DONE_NDR = TRUE. At this time, the executed function is indicated at the outputs UNIT, DATA_TYPE, START_ADDRESS, LENGTH and WRITE_READ.

A request with an error results in an error message. The ERROR bit is set, the error number is indicated in STATUS and the request from the client is not replied to.

**Data transfer CPU - CP**

Data is transferred between the CP and CPU using the standard blocks AG_SEND and AG_RECV or AG_LSEND and AG_LRECV.

If the user activates a job (S7 is client) or if the user receives a frame from the client (S7 is server), the FB calls the standard blocks for the CP in the required number and order.

If the CP receives a frame, 6 bytes are read initially with an AG_(L)RECV. These 6 bytes contain the length of the remainder of the frame. AG_(L)RECV is then called a second time with the remaining length. The user data is evaluated only after the frame has been fully received.

##### Parameters

The parameters of the MODBUSCP instruction are divided into two groups:

- Initialization parameters

  The initialization parameters are only evaluated and entered in the instance DB when called in OB100. The initialization parameters are identified with "Yes" in the "INIT" column in the table.  
  A change to the initialization parameters during operation has no effect. The instance DB must to be re-initialized with "STOP &gt; RUN" of the CPU after these parameters have been changed, e.g. in test mode.
- Runtime parameters

  Runtime parameters can be changed during cyclic operation.

  In the "S7 is client" mode, however, it does not make any sense to change input parameters while a job is running. Preparations for the next job and the associated changes to the parameters should only start after the previous job was ended with DONE_NDR or ERROR.

  In the "S7 is server" mode, the output parameters may only be evaluated when DONE_NDR is set.

  The output parameters are displayed dynamically and are therefore only pending for 1 CPU cycle. This means they have to be copied to other memory areas for further processing or display in the variable table.

With the ranges of values of the various parameters, CPU-specific restrictions may need to be taken into account.

| Parameter | Decl. | Type | Description | Range of values | Init |
| --- | --- | --- | --- | --- | --- |
| [id](#id-and-db_param-parameters-s7-300-s7-400) | IN | WORD | Connection ID from the "Devices &amp; Networks" editor | 1 to 64 | Yes |
| [db_param](#id-and-db_param-parameters-s7-300-s7-400) | IN | BLOCK_DB | Number of the parameter DB | Depends on CPU | Yes |
| [MONITOR](#enq_enr-and-monitor-parameters-s7-300-s7-400-1) | IN | TIME | Monitoring time for receiving data from the link partner The minimum time that can be set is 20 ms | T#20ms to T#+24d20h31 m23s647ms | No |
| [REG_KEY](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1) | IN | STRING[17] | Registration key for licensing | Character | No |
| [ENQ_ENR](#enq_enr-and-monitor-parameters-s7-300-s7-400-1) | IN | BOOL | S7 is client: Job triggered on positive edge S7 is server: Ready to receive if positive level | TRUE/FALSE | No |
| LICENSED | OUT | BOOL | License status of block Block is licensed Block is not licensed | TRUE FALSE | No |
| BUSY | OUT | BOOL | Processing status of the AG_(L)SEND or AG_(L)RECV functions being processed not being processed | TRUE FALSE | No |
| DONE_NDR | OUT | BOOL | S7 is client: TRUE: Activated job completed without errors S7 is server: TRUE: Request from client was executed and reply was sent | TRUE/FALSE | No |
| [ERROR](#done_ndr-error-status-and-status_func-parameters-s7-300-s7-400) | OUT | BOOL | An error occurred No error occurred | TRUE FALSE | No |
| [STATUS](#done_ndr-error-status-and-status_func-parameters-s7-300-s7-400) | OUT | WORD | Error code | 0 to FFFF | No |
| [STATUS_FUNC](#done_ndr-error-status-and-status_func-parameters-s7-300-s7-400) | OUT | STRING[8] | Name of the function that caused the error at STATUS | Character | No |
| [IDENT_CODE](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1) | OUT | STRING[18] | Identification for licensing Request the license with this identification string. | Character | No |
| [UNIT](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BYTE | Unit identifier (INPUT for CLIENT function, OUTPUT for SERVER function) | 0 to 255 | No |
| [DATA_TYPE](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BYTE | Data type to be processed (INPUT for CLIENT function, OUTPUT for SERVER function) |  | No |
| Coils | 1 |  |  |  |  |
| Inputs | 2 |  |  |  |  |
| Holding register | 3 |  |  |  |  |
| Input register | 4 |  |  |  |  |
| [START_ADDRESS](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | WORD | MODBUS start address (INPUT for CLIENT function, OUTPUT for SERVER function) | 0 to 65535 | No |
| [LENGTH](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | WORD | Number of values to be processed (INPUT for CLIENT function, OUTPUT for SERVER function) |  | No |
| Coils: Read function | 1 to 2000 |  |  |  |  |
| Coils: Write function | 1 to 1968 |  |  |  |  |
| Inputs: Read function | 1 to 2000 |  |  |  |  |
| Holding register: Read function | 1 to 125 |  |  |  |  |
| Holding register: Write function | 1 to 123 |  |  |  |  |
| Input register: Read function | 1 to 125 |  |  |  |  |
| [WRITE_READ](#data_type-start_address-length-write_read-and-unit-parameters-s7-300-s7-400) | IN/OUT | BOOL | INPUT for CLIENT function, OUTPUT for SERVER function  Write access or read access | TRUE/FALSE | No |

---

**See also**

[Call of the MODBUSCP instruction (S7-300, S7-400)](#call-of-the-modbuscp-instruction-s7-300-s7-400-1)

#### Licensing with the parameters IDENT_CODE and REG_KEY (S7-300, S7-400)

##### Description

The MODBUSCP instruction must be licensed on each CPU individually. Licensing takes place in two steps:

- Reading out the IDENT_CODE and
- Entering the registration key REG_KEY.

OB121 must be present in the CPU.

Proceed as follows to read out the IDENT_CODE:

1. Assign the parameters of the MODBUSCP instruction according to your requirements in a cyclic OB and in OB100. Download the program to the CPU and set it to RUN.
2. Open the instance DB of the Modbus instruction and click the "Monitor all" button.
3. An 18-digit character string is displayed at the IDENT_CODE output.

   ![Modbus/TCP CP: IDENT_CODE in the DB](images/86974051339_DV_resource.Stream@PNG-en-US.png)

   Modbus/TCP CP: IDENT_CODE in the DB
4. Copy this string using copy/paste from the data block and paste it in the SOFTWARE REGISTRATION FORM. This form is included on the installation CD.

   Enter the license number from the product packaging in the form.

   ![Modbus/TCP CP: IDENT_CODE and license form](images/86974062091_DV_resource.Stream@PNG-en-US.png)

   Modbus/TCP CP: IDENT_CODE and license form
5. Send the form to [Customer Support](https://support.industry.siemens.com/my/ww/en/requests/#createRequest) using a service request. You will then receive the registration key for your CPU.

The registration key REG_KEY must be specified at each MODBUSCP instruction. You should save the REG_KEY in a global data block via which all MODBUSCP instructions receive the necessary registration key.

Proceed as follows to enter the registration key REG_KEY:

- Insert a new global data block with a unique symbolic name, for example "License_DB", using "Add new block…".
- Create a REG_KEY parameter in this block with the data type STRING[17].

  ![REG_KEY in DB](images/66691684107_DV_resource.Stream@PNG-en-US.png)

  REG_KEY in DB
- Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
- Enter the value "License_DB.REG_KEY" in the cyclic OB at the REG_KEY parameter of the MODBUSCP instruction.
- Download the modified blocks to the CPU. The registration key can be entered during runtime; a change from STOP -&gt; RUN is not necessary.

The Modbus/TCP communication using the MODBUSCP instruction is now licensed for this CPU, the output bit LICENSED is TRUE.

****Missing or incorrect licensing****

If you enter an incorrect registration key or none at all, the SF-LED (for S7-300) or INTF-LED (for S7-400) of the CPU flashes and a cyclic entry is made in the diagnostics buffer regarding the missing license. The error number for a missing license is W#16#A090.

![Diag buffer with A090](images/66709766283_DV_resource.Stream@PNG-en-US.png)

Diag buffer with A090

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **If OB121 is missing in the controller, the CPU is set to STOP.** |  |

In the case of a missing or incorrect registration key, the Modbus/TCP communication is processed but W#16#A090 "No valid license available" is always displayed at the STATUS output. The output bit LICENSED is FALSE.

#### Address mapping (S7-300, S7-400)

##### Interpretation of the MODBUS/TCP addresses

The MODBUS data model includes the following areas:

- Coils
- Inputs
- Holding register
- Input register

These memory areas are distinguished in some systems, for example, MODICON PLCs, by means of the register address or bit address. The holding register with offset 0, for example, is referred to as register 40001 (memory type 4xxxx, reference 0001).

This often causes confusion because some manuals describe and mean the register address of the application layer and others the register/bit address actually transferred in the protocol.

The MODBUSCP instruction uses the Modbus/TCP address actually transferred in its parameters start_x, end_x and START_ADDRESS. This means that register/bit addresses from 0000H to FFFFH can be transferred with each function code.

##### Example

The Modbus addresses can be specified in decimal or hexadecimal format in the parameter DB.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter** | **Decimal notation** | **Hexadecimal notation** | **Meaning** |
| data_type_1 | 1 | B#16#1 | Coils |
| db_1 | 10 | W#16#A | DB 10 |
| start_1 | 640 | W#16#280 | Start address: 640 |
| end_1 | 1250 | W#16#4E2 | End address:      1250 |
| data_type_2 | 3 | B#16#3 | Holding register |
| db_2 | 11 | W#16#B | DB 11 |
| start_2 | 0 | W#16#0 | Start address: 0 |
| end_2 | 499 | W#16#1F3 | End address:      499 |
| data_type_3 | 3 | B#16#3 | Holding register |
| db_3 | 12 | W#16#C | DB 12 |
| start_3 | 720 | W#16#2D0 | Start address: 720 |
| end_3 | 900 | W#16#384 | End address:      900 |

The figure below shows a comparison of the SIMATIC memory areas with the register-oriented and bit-oriented memory allocation of the Modbus/TCP devices. The figure references the parameter assignment described above.

**In the Modbus device**

The Modbus addresses shown in black relate to the data link layer; those shown in gray to the application layer.

**In SIMATIC**

The SIMATIC addresses shown in the "Offset" column are the offset in the DB. The Modbus register numbers are in the square brackets.

![Modbus/TCP: Address mapping](images/86974695435_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Address mapping

#### ID and DB_PARAM parameters (S7-300, S7-400)

##### Description

**ID**

A connection ID is assigned for each configured connection in STEP 7 ("Devices &amp; Networks" editor). The connection ID uniquely describes the connection from the CPU via the CP to the link partner. This connection ID is configured in the connection parameter block included in the parameter data block. This ID must be entered here.

The range of values for this parameter is 1 to 64.

**DB_PARAM**

The db_param parameter refers to the number of the parameter data block, which contains the MB_CP_PARAM PLC data type. The connection-specific and Modbus-specific parameters required for communication between the CPU and the link partner are stored in this parameter data block.

The range of values for this parameter depends on the CPU. The DB number 0 is not permitted because it is reserved for the system. The DB number is entered in plain text as "DBxy".

If you want to implement several connections, the parameter data block can include the necessary parameters of all connections in sequence. You can also create a separate parameter data block for each connection.

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400-1)
  
[Parameter data block (S7-300, S7-400)](#parameter-data-block-s7-300-s7-400-1)

#### DONE_NDR, ERROR, STATUS and STATUS_FUNC parameters (S7-300, S7-400)

##### Description

**DONE_NDR**

In "S7 is client" mode, the active job was completed without errors. With a read function, the response data from the server has already been entered in the DB; with a write function, the response to the request message was received from the server.

In "S7 is server" mode, the output displays a frame exchange completed without errors with the client. The job parameters of the client are displayed in the DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ, and UNIT parameters. These outputs are only valid as long as DONE_NDR is set.

**ERROR**

An error is detected when this output is set.

In "S7 is client" mode, the active job was completed with errors. The corresponding error number is indicated at the STATUS output.

In "S7 is server" mode, an error was detected in the request of the client or when sending the response. The corresponding error number is indicated at the STATUS output.

**STATUS**

If ERROR is set, the STATUS output indicates the error number.

Status information continues to be indicated at this output.

The instructions MODBUSCP, MB_CPCLI and MB_CPSRV use the standard blocks SFC6, SFC20, SFC24, SFC51 and SFC52 as well as AG_SEND/AG_LSEND and AG_RECV/AG_LRECV. The error messages of these instructions are passed unchanged to STATUS.

**STATUS_FUNC**

This parameter indicates the name of the function that caused the error in the form of a character string.

| Status (hex) | Event text |  | Remedy |
| --- | --- | --- | --- |
| A001 | The parameter DB is too short. |  | Correct the length of the parameter DB. |
| A002 | The end_x parameter is lower than start_x. |  | Correct the information in start_x and end_x. |
| A003 | A DB to which Modbus addresses are to be mapped is too short. Minimum length:  For registers:  (end_x - start_x + 1) * 2 + 2 - For bit values: (end_x - start_x ) / 8 + 3 Other possible causes: • S7 is client: wrong call parameter • S7 is server: incorrect address range in the client request. The CP replies with an exception telegram. |  | Lengthen the DB. S7 is client:  Correct the job parameters START_ ADDRESS or LENGTH. S7 is server:  Change the client request. |
| A004 | Only S7 is client:  An invalid combination of DATA_TYPE and WRITE_READ was specified. |  | Correct the call parameters. Only data types 1 and 3 can be written. |
| A005 | S7 is client:  An invalid value was specified at the LENGTH parameter. S7 is server:  The number of registers/bits in the request is invalid. The CP replies with an exception telegram. |  | S7 is client:  Correct the LENGTH parameter. S7 is server:  Change the number in the request. |
| Ranges of values: |  |  |  |
| Read coils/inputs | 1 to 2000 |  |  |
| Write coils | 1 to 1968 |  |  |
| Read registers | 1 to 125 |  |  |
| Write holding registers | 1 to 123 |  |  |
| A006 | The area specified with DATA_TYPE, START_ADDRESS and LENGTH does not exist in data_type_1 to data_type_8.  S7 is server: The CP replies with an exception telegram. |  | S7 is client: Correct the parameter assignment combination DATA_TYPE, START_ ADDRESS and LENGTH. S7 is server: Change the client request or correct the parameter assignment for data_type_x. |
| A007 | S7 is client: An invalid monitoring time was set for MONITOR. A value &gt;= 20 ms must be entered. |  | Correct the parameter assignment. |
| A008 | Within the set monitoring time MONITOR, the activated AG_RECV signals no reception, e.g. partner not ready. All connections over port 502 are terminated and re-established. |  | Check the settings and, if applicable, the error messages of the link partner. Check whether the link partner requires a specific UNIT identifier. |
| A009 | S7 is client: The received Transaction Identifier TI does not match the identifier sent. All connections over port 502 are terminated and re-established. |  | Record frames to check the data of the link partner. |
| A00A | S7 is client: The received UNIT does not match the one that was sent. All connections over port 502 are terminated and re-established. |  |  |
| A00B | S7 is client: The received function code is not the same as the one sent. S7 is server: An invalid function code was received. The CP replies with an exception telegram. All connections over port 502 are terminated and re-established. |  | S7 is client:  Record frames to check the data of the link partner. S7 is server:  Change the client request. The MODBUSCP instruction processes the function codes 1, 2, 3, 4, 5, 6, 15 and 16. |
| A00C | The received byte count does not match the number of registers/bits. S7 is server: The CP sends an exception telegram. All connections over port 502 are terminated and re-established. |  | Record frames to check the data of the link partner. |
| A00D | Only for S7 is client: The register address/bit address or the number of registers/bits in the response is not the same as in the request. |  |  |
| A00E | The length information in the Modbus-specific frame header does not match the specified number of registers/bits or the byte count in the frame. The instruction discards the data. All connections over port 502 are terminated and re-established. |  | Record frames to check the data of the link partner |
| A00F | A Protocol Identifier other than 0 was received. All connections over port 502 are terminated and re-established. |  |  |
| A010 | A DB number was assigned twice in the parameters db_1 to db_8. |  | Correct the parameter assignment at db_x. |
| A011 | An invalid value was specified for the DATA_TYPE input parameter (valid values are 1, 2, 3 and 4). |  | Correct the call parameters. |
| A012 | The areas data_type_1 and data_type_2 set in the parameters overlap. |  | Correct the parameter assignment, The data areas must not contain any overlapping register areas. |
| A013 | The areas data_type_1 and data_type_3 set in the parameters overlap. |  |  |
| A014 | The areas data_type_1 and data_type_4 set in the parameters overlap. |  |  |
| A015 | The areas data_type_1 and data_type_5 set in the parameters overlap. |  |  |
| A016 | The areas data_type_1 and data_type_6 set in the parameters overlap. |  |  |
| A017 | The areas data_type_1 and data_type_7 set in the parameters overlap. |  |  |
| A018 | The areas data_type_1 and data_type_8 set in the parameters overlap. |  |  |
| A019 | One of the db_x parameters was set to 0 even though the associated data_type_x is set to &gt; 0. DB0 must not be used because it is reserved for the system. |  | Correct the parameter setting at db_x to &gt; 0. If you use a data collector FB, check the parameter assignment in CFC. |
| A01A | Incorrect length in the header: 3 to 253 bytes are permitted. All connections over port 502 are terminated and re-established. |  | Record frames to check the data of the link partner. |
| A01B | S7 is server and function code 5:  An invalid status for Coil was received. An exception telegram is sent. |  |  |
| A01E | Invalid data was received that could not be assigned. All connections over port 502 are terminated and re-established. |  | Check the error message of the link partner. If necessary, check the data by recording frames. |
| A01F | The MODBUSCP instruction is in an illegal operating state. |  | Contact Product Support. |
| A023 | The areas data_type_2 and data_type_3 set in the parameters overlap. |  | Correct the parameter assignment.  The data areas must not contain any overlapping register areas. |
| A024 | The areas data_type_2 and data_type_4 set in the parameters overlap. |  |  |
| A025 | The areas data_type_2 and data_type_5 set in the parameters overlap. |  |  |
| A026 | The areas data_type_2 and data_type_6 set in the parameters overlap. |  |  |
| A027 | The areas data_type_2 and data_type_7 set in the parameters overlap. |  |  |
| A028 | The areas data_type_2 and data_type_8 set in the parameters overlap. |  |  |
| A034 | The areas data_type_3 and data_type_4 set in the parameters overlap. |  |  |
| A035 | The areas data_type_3 and data_type_5 set in the parameters overlap. |  |  |
| A036 | The areas data_type_3 and data_type_6 set in the parameters overlap. |  |  |
| A037 | The areas data_type_3 and data_type_7 set in the parameters overlap. |  |  |
| A038 | The areas data_type_3 and data_type_8 set in the parameters overlap. |  |  |
| A045 | The areas data_type_4 and data_type_5 set in the parameters overlap. |  |  |
| A046 | The areas data_type_4 and data_type_6 set in the parameters overlap. |  |  |
| A047 | The areas data_type_4 and data_type_7 set in the parameters overlap. |  |  |
| A048 | The areas data_type_4 and data_type_8 set in the parameters overlap. |  |  |
| A056 | The areas data_type_5 and data_type_6 set in the parameters overlap. |  |  |
| A057 | The areas data_type_5 and data_type_7 set in the parameters overlap. |  |  |
| A058 | The areas data_type_5 and data_type_8 set in the parameters overlap. |  |  |
| A067 | The areas data_type_6 and data_type_7 set in the parameters overlap. |  |  |
| A068 | The areas data_type_6 and data_type_8 set in the parameters overlap. |  |  |
| A078 | The areas data_type_7 and data_type_8 set in the parameters overlap. |  |  |
| A079 | The connection ID specified for the id parameter is not included in the parameter DB. |  | Correct the parameter assignment at the id input. |
| A07A | An invalid value was specified for the id parameter (value range from 1 to 64). |  |  |
| A07B | The specified ID is included twice in the parameter DB. |  | Correct the parameter assignment in the parameter DB. |
| A07C | An invalid value was specified for the data_type_x parameter (valid values are 0 to 4). |  |  |
| A07D | The data_type_1 parameter does not contain an entry. The parameter area "_1" is the initial area and must be set. |  | Correct the parameter assignment in the parameter DB. |
| A07E | The number of the instance DB of the MODBUSCP instruction was specified in db_x. |  |  |
| A080 | Different instance DBs were used for the MODBUS instruction in OB100 and in the cyclic OB. |  | The MODBUS block must be called with the same instance DB in the startup OB and in the cyclic OB. |
| A081 | Only for S7 is client and function code 5:  The data of the response is not the echo of the request. |  | Record frames to check the data of the link partner. |
| A082 | Only for S7 is client and function code 6:  The received register value is not the same as the one sent. |  | Record frames to check the data of the link partner. |
| A083 | S7 is client: A job was triggered while the previous job is still in progress. The job is not executed. |  | Only start a new job when the previous job ended with DONE_ NDR = TRUE or ERROR = TRUE. |
| A085 | Due to illegal write access, an internal error occurred during the license check. |  | Check that there is no illegal write access to the license DB in the S7 program. The structure of REG_KEY must not be modified. If necessary, contact Product Support. |
| A086 | An attempt was made to write to a write-protected data block. |  | Remove the write protection or use a different DB. |
| A090 | The MODBUSCP instruction has not yet been licensed for this CPU. This is status information. The ERROR bit is not set. MODBUS communication is running even without a license. |  | Read out the identification code for this CPU at the IDENT_CODE output and request the registration key. Refer to the section "[Licensing](#licensing-with-the-parameters-ident_code-and-reg_key-s7-300-s7-400-1)". |
| A091 | Only for S7 is client: An exception telegram with exception code 1 was received as the reply. |  | The link partner does not support the requested function. |
| A092 | Only for S7 is client: An exception telegram with exception code 2 was received as the reply. There was access to a non-existent or illegal address on the link partner. |  | Correct LENGTH or START_ADDRESS in the FB call. |
| A093 | Only for S7 is client: An exception telegram with exception code 3 was received as the reply. |  | The link partner cannot process the received frame (for example, it does not support the requested length). |
| A094 | Only for S7 is client: An exception telegram with exception code 4 was received as the reply. |  | The link partner is in a status in which it cannot process the received frame. |
| A095 | Only for S7 is client: An exception telegram with an unknown exception code was received as the reply. |  | Check the error messages of the link partner and if necessary record the frames to check the data. |

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400-1)

#### DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT parameters (S7-300, S7-400)

##### Description

In "S7 is client" mode, these parameters are input parameters; in "S7 is server" mode, these parameters are output parameters.

**DATA_TYPE**

The DATA_TYPE parameter indicates which Modbus/TCP data type is processed with the current frame. The following values are permitted:

| Symbol | Meaning |
| --- | --- |
| Coils | B#16#1 |
| Inputs | B#16#2 |
| Holding register | B#16#3 |
| Input register | B#16#4 |

The different data types are directly related to the used function codes.

| Data type | DATA_TYPE | Function | Length | single_write | Function code |
| --- | --- | --- | --- | --- | --- |
| Coils | 1 | read | any | irrelevant | 1 |
| Coils | 1 | write | 1 | TRUE | 5 |
| Coils | 1 | write | 1 | FALSE | 15 |
| Coils | 1 | write | &gt; 1 | irrelevant | 15 |
| Inputs | 2 | read | any | irrelevant | 2 |
| Holding register | 3 | read | any | irrelevant | 3 |
| Holding register | 3 | write | 1 | TRUE | 6 |
| Holding register | 3 | write | 1 | FALSE | 16 |
| Holding register | 3 | write | &gt; 1 | irrelevant | 16 |
| Input register | 4 | read | any | irrelevant | 4 |

**START_ADDRESS**

The START_ADDRESS parameter determines the first Modbus/TCP address that is written or read.

**LENGTH**

The LENGTH parameter determines the number of Modbus/TCP values that are written or read.

With read functions, a maximum of 125 registers are possible per frame for holding and input registers. For coils and inputs, a maximum of 2000 bits are possible. With write functions, the maximum number of registers is 123 for holding registers and 1968 bits for coils. The registers or bit values processed with a request frame must be located within one DB.

**WRITE_READ**

This parameter defines whether a read or write function is to be performed. If the input/output has the value FALSE, it is a read function. The value TRUE defines a write function.

Only holding registers and coils can be written to. Input registers and inputs can only be read.

**UNIT**

In the "S7 is client" function, the UNIT parameter is an input parameter. This input needs to be set according to the requirements. The instruction applies this value to the request and checks the value when it receives the reply.

The UNIT parameter is typically used with protocol converters to address serial slaves concealed behind a common IP address.

Most devices can be addressed with UNIT = 1.

In the "S7 is server" function, the UNIT parameter is an output parameter. The instruction applies the value from the request to the response. When the job is completed, the output is set to the received value.

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400-1)

#### ENQ_ENR and MONITOR parameters (S7-300, S7-400)

##### Description

**ENQ_ENR**

"S7 is client" mode:  
The data transfer is initiated on a positive edge. The request is generated with the values of the input parameters DATA_TYPE, START_ADDRESS, LENGTH, WRITE_READ and UNIT. A new job can only be sent if the previous job has been completed with DONE_NDR or ERROR.

"S7 is server" mode:  
The instruction is activated with a positive level at the input. Frames can be received from the client.  
If the ENQ_ENR input is not set and a connection exists, the received data is discarded.

**MONITOR**

The monitoring time MONITOR monitors the incoming data from the link partner. The monitoring time is specified in the time format T#... A monitoring time of approximately 1.5 s is recommended.

In "S7 is client" mode, the MONITOR time monitors the arrival of the complete response from the server. If the monitoring time is exceeded, the activated job is ended with an error. The time is started after the request has been sent and stopped after the response has been entirely received.

In "S7 is server" mode, the input of the second part of the frame is monitored with the MONITOR time. If the monitoring time is exceeded, an error is reported. The time is started after receipt of the MODBUS/TCP-specific telegram header and stopped after the request has been entirely received.

---

**See also**

[Description of MODBUSCP (S7-300, S7-400)](#description-of-modbuscp-s7-300-s7-400-1)
