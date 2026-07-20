---
title: "Using controller data from other projects with IPE"
package: PETeamIPEWCCenUS
topics: 24
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using controller data from other projects with IPE

This section contains information on the following topics:

- [Using controller data from other projects in an HMI device](#using-controller-data-from-other-projects-in-an-hmi-device)
- [Communication with device proxies](#communication-with-device-proxies)
- [Integrated configuring with WinCC and SIMATIC Manager](#integrated-configuring-with-wincc-and-simatic-manager)

## Using controller data from other projects in an HMI device

This section contains information on the following topics:

- [Basics on controller data](#basics-on-controller-data)
- [Initializing a device proxy via an IPE file](#initializing-a-device-proxy-via-an-ipe-file)
- [Initializing a device proxy via a project file](#initializing-a-device-proxy-via-a-project-file)

### Basics on controller data

#### Introduction

In the source project of the PLC, you can select which controller data is to be stored as device-proxy data.

To this end, you create a device proxy data from a configured PLC.

#### Which controller data can be exchanged?

The following controller data can be exchanged via IPE:

- Data blocks
- Technology objects
- PLC tags
- PLC supervisions and PLC alarms

The following information is exchanged automatically:

- Interfaces of the PLC
- Configured communication processors and communication modules at the PLC

### Initializing a device proxy via an IPE file

This section contains information on the following topics:

- [Initializing device proxy via an IPE file](#initializing-device-proxy-via-an-ipe-file)
- [Initializing a device proxy via an IPE file](#initializing-a-device-proxy-via-an-ipe-file-1)
- [Updating a device proxy via an IPE file](#updating-a-device-proxy-via-an-ipe-file)

#### Initializing device proxy via an IPE file

##### How does initialization of a device proxy via an IPE file work?

You can exchange controller data between two or more projects using IPE files.

Due to their small data volume, you can send IPE files by e-mail, for example.

You can create multiple IPE files with different device proxy data for each PLC.

A device proxy can only be filled with one device proxy data record in the target project.

![How does initialization of a device proxy via an IPE file work?](images/57917836427_DV_resource.Stream@PNG-en-US.png)

- An IPE file is exported from the source project.

  The IPE file contains device proxy data of the PLC "PLC_A".
- A device proxy is created in the target project.
- In the target project, the device proxy is then initialized with the device proxy data from the IPE file.
- Following initialization, all device proxy data from the IPE file is contained in the device proxy.
- If changes are made in the source project, the device proxy of PLC_A in the target project can be updated via the new IPE file.

#### Initializing a device proxy via an IPE file

##### Introduction

You initialize device proxy data using a dialog on the device proxy in the TIA Portal.

The IPE file contains the device proxy data from the source project.

##### Requirement

IPE file is available.

##### Procedure

1. Double-click "Add new device" in the project tree.
2. Select the device proxy under "Controller".

   ![Procedure](images/74751679371_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74751679371_DV_resource.Stream@PNG-en-US.png)

   A new device is created in the "Devices &amp; Networks" editor.
3. Select the device proxy in the project tree.
4. Click "Initialize device proxy" in the shortcut menu.

   ![Procedure](images/59005650443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/59005650443_DV_resource.Stream@PNG-en-US.png)
5. Select the IPE file and click "Open".

   The "Initialize device proxy" dialog opens.
6. Click "OK".

   Initialization of the device proxy is started.

**Note**

You cannot select the device proxy data before initialization in the target project.

All device proxy data included in the IPE file is transferred.

Initialize the device proxy via project file if you want to select specific device proxy data before initialization: [Initializing a device proxy via a project file](#initializing-a-device-proxy-via-a-project-file-2)

##### Result

Following initialization, all device proxy data from the IPE file is contained in the device proxy.

You can now configure an HMI connection with the device proxy and connect PLC tags from the device proxy with HMI tags, for example.

#### Updating a device proxy via an IPE file

##### Introduction

If changes were made to the device proxy data in the device proxy source project, the device proxy data can be updated in the target project.

> **Note**
>
> When updating the device proxy data in the target project, ensure that in the source project of the device proxy, you work in the same version of TIA Portal or at the most, in a lower version.
>
> If your target project has been created in a higher version of TIA Portal than the source project, the updating of the device proxy data will fail.

##### Requirement

- New IPE file contains the device proxy data from the source project.
- A device proxy has already been initialized using an IPE file in the target project.

##### Procedure

1. Select the device proxy in the project tree.
2. Click "Update device proxy" in the shortcut menu.
3. Select the IPE file.

   ![Procedure](images/88106240907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88106240907_DV_resource.Stream@PNG-en-US.png)
4. Select whether you wish to update the PROFINET or PROFIBUS addresses.
5. Click "OK".

### Initializing a device proxy via a project file

This section contains information on the following topics:

- [Initializing a device proxy via a project file](#initializing-a-device-proxy-via-a-project-file-1)
- [Initializing a device proxy via a project file](#initializing-a-device-proxy-via-a-project-file-2)
- [Updating a device proxy via a project file](#updating-a-device-proxy-via-a-project-file)

#### Initializing a device proxy via a project file

##### How does an initialization via project file work?

You can transfer controller data using a project file in your TIA Portal project:

![How does an initialization via project file work?](images/57922818699_DV_resource.Stream@PNG-en-US.png)

- There are two PLCs in the source project.
- Device proxy data objects of the two PLCs are created in the source project.
- The source project is saved.
- A device proxy is created in the target project.
- The source project (*.ap13) is first selected using the command for the initialization of device proxy in the device shortcut menu.
- The "PLC_A" and "PLC_B" controllers are available for selection and their device proxy data have already been created.
- After selection of device proxy data of "PLC_A", the data is stored in the PLC_Proxy of the target project.
- Changes from the source project can be transferred by an update via the project file.

#### Initializing a device proxy via a project file

##### Introduction

You initialize the device proxy using a project file.

##### Requirement

Project file (*.ap*) is available.

##### Procedure

1. Double-click "Add new device" in the project tree.
2. Select the device proxy under "Controller".

   ![Procedure](images/74751679371_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74751679371_DV_resource.Stream@PNG-en-US.png)

   A new device is created in the "Devices &amp; Networks" editor.
3. Select the device proxy in the project tree.
4. Click "Initialize device proxy" in the shortcut menu.

   ![Procedure](images/59005650443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/59005650443_DV_resource.Stream@PNG-en-US.png)
5. Select the following entry in the "Open device proxy data source" dialog:

   "TIA Portal projects (*.ap*)"
6. Select a project file and click "Open".

   The "Initialize device proxy" dialog opens.
7. Select a device proxy data object already created from an available PLC to initialize the device proxy.
8. Click "OK".

> **Note**
>
> During initialization of the device proxy a check is automatically carried out whether the selected data are consistent and can be imported into the target project. If the source project contains inconsistent data, compile your source project.

##### Result

Following initialization, the controller data from the project file in the selected device proxy data object is stored in the device proxy.

You can now configure an HMI connection with the device proxy and connect PLC tags from the device proxy with HMI tags, for example.

##### Initializing via STEP 7 V5.5 projects

You can find more information about importing control data from projects prior to TIA Portal V11 in the section [Integrated configuration with WinCC and Simatic Manager](#integrated-configuring-with-wincc-and-simatic-manager).

You can find additional information in the FAQ with entry ID: [73502293](http://support.automation.siemens.com/WW/view/en/73502293)

---

**See also**

[Integrated configuring with WinCC and SIMATIC Manager](#integrated-configuring-with-wincc-and-simatic-manager)

#### Updating a device proxy via a project file

##### Introduction

If changes have been made to the controller data in the source project of the device proxy, you can update the device proxy in your TIA Portal project.

##### Requirement

- Project file has been generated from the source project of the device proxy.
- A device proxy that has already been initialized is available in the target project.

##### Procedure

1. Select the device proxy in the project tree.
2. Click "Update device proxy" in the shortcut menu.
3. Select the project file.

   The "Update device proxy" dialog opens.

   ![Procedure](images/88106240907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88106240907_DV_resource.Stream@PNG-en-US.png)
4. Select a device.
5. Select whether you wish to update the PROFINET or PROFIBUS addresses.
6. Click "OK".

**Note**

If you have created several device proxy data objects in the source project, you need to select one device proxy data object.

**Note**

Already initialized device proxies cannot be overwritten with controller data from a different PLC.

## Communication with device proxies

This section contains information on the following topics:

- [Basics of communication with device proxies](#basics-of-communication-with-device-proxies)
- [Configuring a direct connection](#configuring-a-direct-connection)
- [Configuring a routed connection](#configuring-a-routed-connection)

### Basics of communication with device proxies

#### Introduction

Data exchange between the HMI device in your target project and existing controller from the source project is enabled in the TIA Portal using device proxies. You initialize a device proxy with device proxy data from the source project and link the HMI device to the device proxy PLC in the target project.

The HMI device and the device proxy PLCs can communicate with each other directly via a subnet or across multiple subnets. For communication across multiple subnets, you need to configure a device proxy-PLC as a router that connects the HMI device and the target PLC.

The communication between connection partners is possible via the following connections:

- PROFINET
- PROFIBUS
- MPI

#### Setting network parameters

In the TIA Portal, you connect the HMI device and the device proxy PLC in the "Devices &amp; Networks" editor.

Once you have connected an HMI device with the device proxy PLC, adapt the properties of the network parameters. Note the   
network parameters from the source project and enter them in the properties of the network connection between the device proxy PLC and the HMI device.

> **Note**
>
> IPE does not transfer data to the network configuration. You therefore configure the required networks in the target project manually so that the network configuration in the target project corresponds to the configuration in the source project. The subnet IDs of the devices in the target project in particular must correspond to each other and to the IDs of the devices in the source project. Otherwise, communication will not be possible between the source device and the HMI devices in runtime

Depending on the connection, provide the following parameters:

| Connection | Parameters |
| --- | --- |
| Ethernet | S7 subnet ID |
| MPI PROFIBUS | S7 subnet ID  Highest address  Transmission rate  Bus parameters |

#### Communication via S7 routing

To establish a routed connection to these connection partners, a router must be interposed. Configure both the router and the target PLC as device proxies.

The router and the target PLC can be initialized with an IPE file, TIA Portal project file or a STEP 7 V5.5 project file.

Modules with communication capability (CPUs or CPs) used to establish gateways between the subnetworks must have routing capability.

The S7 routing settings can be edited in the relevant interface properties.

You can configure the S7 routing connection in the "Devices &amp; Networks" editor.

> **Note**
>
> A routed connection must be configured in the source project for a routed connection to a connection partner that was loaded with the source project data.

![Communication via S7 routing](images/80383676939_DV_resource.Stream@PNG-en-US.png)

The routing path is determined in Runtime by the system and cannot be influenced by the user. During configuration, it is not possible to generate information about a faulty connection. All relevant routing paths have to be mapped in the TIA Portal exactly as they were configured in STEP 7 source project.

### Configuring a direct connection

#### Introduction

In the target project, configure a direct connection between a device proxy PLC and an HMI device in "Devices &amp; Networks" editor.   
The following configuration describes a network for the following communication partners:

- HMI device
- Device proxy PLC

#### Requirements

- Device proxy data were exported from the source project
- An HMI device has been created in the target project
- A proxy device has been created

#### Procedure

1. Note the subnet ID of the connection in the source project.

   For an MPI or PROFIBUS connection, also note also the highest address, the transmission speed and the bus parameters.
2. Initialize the device proxy in the target project with the device proxy data from your source project.
3. Connect the communication interfaces of the HMI device and of the device proxy PLC.

   The corresponding S7 subnet is automatically generated.

   ![Procedure](images/72089327883_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72089327883_DV_resource.Stream@PNG-en-US.png)
4. Transfer the parameters that you noted from the source project into the parameters of the TIA project:

   - Enter the S7 subnet ID under "Properties &gt; General".
   - Enter the highest address and the transmission rate under "Properties &gt; Network Settings".
   - Enter the bus parameters under "Properties &gt; Bus parameters".

### Configuring a routed connection

#### Introduction

The HMI device and the device proxy PLCs can communicate with each other across multiple subnets. For a routed connection, configure a device proxy PLC as a router between the HMI device and the target PLC.

> **Note**
>
> For a routed connection to the connection partner from the source project, a routed connection must be configured in the source project.

The following configuration describes a network for the following communication partners:

- HMI device
- Device proxy PLC as router
- Device proxy PLC as target PLC

  All subnets that are involved in the routing between the HMI device and the target PLC must be configured in the source project. They must be identically configured in the target project.

  ![Introduction](images/72095015435_DV_resource.Stream@PNG-en-US.png)

#### Requirements

- Device proxy data were exported from the source project
- An HMI device has been created
- Two device proxies have been added

#### Procedure

1. Note the subnet IDs of the connections in the source project.   
   For a PROFIBUS connection, also note also the highest address, the transmission speed and the bus parameters.
2. Initialize the source proxy in the target project with the device proxy data from your source project.
3. Create the network connection between the HMI device and the router as well as between the router and the target PLC as it was configured in the source project.
4. Click the "Connections" button.
5. Connect the communication interfaces of the HMI device and of the router.

   Router and target PLC are connected automatically.
6. Create an HMI connection between the HMI device and the target PLC using drag-and-drop operation.

   The "Connect with subnet" dialog opens.
7. Select "Add S7 routed connection".

   The routing connection is created.

   ![Procedure](images/72095019787_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72095019787_DV_resource.Stream@PNG-en-US.png)
8. Transfer the parameters that you noted from the source project into the parameters of the TIA project:

   - Enter the S7 subnet ID under "Properties &gt; General".
   - Enter the highest address and the transmission rate under "Properties &gt; Network Settings".
   - Enter the bus parameters under "Properties &gt; Bus parameters".

#### Result

The created connection is displayed in the "HMI connections" editor.

![Result](images/72096528011_DV_resource.Stream@PNG-en-US.png)

## Integrated configuring with WinCC and SIMATIC Manager

This section contains information on the following topics:

- [Basic principles for configuring with WinCC and SIMATIC Manager](#basic-principles-for-configuring-with-wincc-and-simatic-manager)
- [Initializing a device proxy via a STEP 7 project file](#initializing-a-device-proxy-via-a-step-7-project-file)
- [Adapting network parameters](#adapting-network-parameters)
- [Checking inconsistent data](#checking-inconsistent-data)
- [Adapting tags and connections](#adapting-tags-and-connections)
- [Updating a device proxy via a STEP 7 project file](#updating-a-device-proxy-via-a-step-7-project-file)
- [Including tags from the SIMATIC Manager](#including-tags-from-the-simatic-manager)
- [Configuring the "Direct keys" system function](#configuring-the-direct-keys-system-function)

### Basic principles for configuring with WinCC and SIMATIC Manager

#### Integrated configuring with WinCC and SIMATIC Manager

The TIA Portal provides the option to create PLC programs and the HMI configurations using a uniform user interface.

In some cases it is still necessary, for technical or customer-specific reasons, to create the PLC program with the "STEP 7 V5.x" software and the HMI configuration with the WinCC software (TIA Portal).

You can directly access the PLCs configured in the SIMATIC Manager and their current data via the device proxy PLC and integrate this into WinCC (TIA Portal).

#### Requirement

- WinCC with version V13 or higher
- SIMATIC Manager STEP 7 with version V5.4 SP3 or higher
- In SIMATIC Manager all required software option packages that are used in the STEP 7 project must be installed.
- The project must be consistent in the SIMATIC Manager.

#### Supported PLCs

- S7-300 PLC
- S7-300F PLC
- S7-400 PLC
- S7-400F PLC
- S7-300 T-PLC
- ET200 PLC (IM 151-x CPU)

#### Supported alarm procedures

- Discrete alarm types
- Analog alarm types
- Signal system fault (SFM)
- Alarm_S, Alarm_SQ, Alarm_D, Alarm_DQ

### Initializing a device proxy via a STEP 7 project file

#### Introduction

A connection to a CPU within the SIMATIC Manager is established through the initialization. After successful initialization the tags and messages contained in the SIMATIC Manager are also available in the WinCC project.

#### Initializing a device proxy PLC

1. Initialize the device proxy via the project file (*.s7p) of your STEP 7 project.

   In the "Initialize device proxy" dialog, select the CPU, program blocks, symbols and PLC messages for the device proxy.
2. After successful initialization the selected data are displayed in the program folders in the project tree.

> **Note**
>
> The data are not processed in WinCC (TIA Portal). Only reading access to the tags is available. Changes to the STEP 7 program are always carried out in the SIMATIC Manager.

> **Note**
>
> **Support of H-PLCs**
>
> IPE functionality in the TIA Portal also supports the use of H-PLCs from STEP 7 as of V5.5. Only the master H-PLC is relevant during the initialization of the device proxy.

#### Display of the original name of the source device

1. Open the device configuration of the device proxy PLC.
2. Select "Device view"".
3. Open "Properties &gt; General &gt; General &gt; Device proxy information".

   The original name is displayed under "Proxy source".

#### Creating a network connection between HMI and PLC

As when using a "Standard PLC", you configure a network connection between the used HMI device and the device proxy PLC.

1. In the device configuration select "Network view".
2. Mark the device proxy PLC and enter the same connection properties under "Properties" that the PLC program has in the SIMATIC Manager.
3. Network and connect the two devices.

> **Note**
>
> **Network connection and addresses**
>
> Irrespective of whether you have created an Ethernet connection or a PROFIBUS connection, check the respective addresses and bus parameters of the modules used and if necessary adapt these. If you use PROFIBUS, observe the additional information under [Adapting network parameters](#adapting-network-parameters).

### Adapting network parameters

#### Introduction

If you have networked an HMI device with the device proxy PLC, you have to adapt the properties of the parameters in the STEP 7 5.x project in the following cases:

- You have a STEP 7 V5.x project. The HMI devices in this project created with WinCC flexible were migrated to WinCC (TIA Portal) and networked with the device proxy PLC.
- You have a STEP 7 V5.x project. The HMI devices were configured only with WinCC (TIA Portal) and are networked with the device proxy PLC.

Depending on the connection, provide the following parameters:

| Connection | Parameters |
| --- | --- |
| Ethernet | S7 subnet ID |
| MPI PROFIBUS | S7 subnet ID  Highest address  Transmission rate  Bus parameters |

Record the parameters in the STEP 7 project and enter these in the TIA Portal at the properties of the network connection.

#### Adapting network parameters

1. Open the hardware configuration of the CPU in the SIMATIC Manager.
2. Open the object properties of the PROFIBUS interface of the CPU.
3. Select the "Properties..." button under "General" in the "MPI/DP properties" dialog.

   The "Properties – PROFIBUS interface" dialog is opens.
4. Select the "Properties..." button under "Parameters" in the "Properties - PROFIBUS interface" dialog.

   The "Properties - PROFIBUS" dialog is opens.
5. Note the S7 subnet ID.

   ![Adapting network parameters](images/71789584779_DV_resource.Stream@PNG-en-US.png)

   ![Adapting network parameters](images/71789584779_DV_resource.Stream@PNG-en-US.png)
6. If you adapt the PROFIBUS connection, record the "Highest address" and "Transmission rate" parameters in the "Network settings" dialog box.
7. If you adapt the PROFIBUS connection, select the "Bus Parameters" button in the "Properties - PROFIBUS" window under "Network settings".

   Note the bus parameters listed there.
8. In "Devices &amp; Networks" editor of the TIA Portal, select the network connection between the device proxy PLC and the HMI device.
9. Select the "User-defined" profile under "Properties &gt; General&gt; Network Settings".

   ![Adapting network parameters](images/74946867595_DV_resource.Stream@PNG-en-US.png)

   ![Adapting network parameters](images/74946867595_DV_resource.Stream@PNG-en-US.png)
10. Transfer the parameters that you noted from the STEP 7 configuration into the parameters of the TIA project:

    - Enter the S7 subnet ID under "Properties &gt; General".
    - Enter the highest address and the transmission rate under "Properties &gt; Network Settings".
    - Enter the bus parameters under "Properties &gt; Bus parameters".

    ![Adapting network parameters](images/71762527627_DV_resource.Stream@PNG-en-US.png)

    ![Adapting network parameters](images/71762527627_DV_resource.Stream@PNG-en-US.png)

### Checking inconsistent data

#### Introduction

During initialization of a device proxy a check is automatically carried out whether the selected data are consistent in the source project and can be imported into the target project. If the source project contains inconsistent data, repair them in the source project in the SIMATIC Manager.

The following tools are available for determining and repairing the inconsistent data in STEP 7 V5.x:

- "Check block consistency" for checking data blocks and alarms
- "Symbol Editor" for checking the symbols

> **Note**
>
> You can find additional information on "Check block consistency" and "Symbol editor" in the STEP 7 V5.x documentation.

#### Checking data blocks and messages

1. Open the source project in the S7 SIMATIC Manager.
2. Mark the block folder in the project window.
3. Select the "Check block consistency..." entry from the shortcut menu.

   The "Check block consistency" editor opens.
4. Select the "Program &gt; Compile" command from the menu.

   Inconsistencies in the blocks are corrected automatically and objects are compiled.
5. If an inconsistency cannot be corrected automatically, an error message is output. By double-clicking the error message you jump to the faulty object. Correct the inconsistencies manually and save the project afterwards.

#### Checking symbols

1. Open the source project in the S7 SIMATIC Manager.
2. Start the Symbol Editor by double-clicking the symbol table.

   The Symbol Editor is opened.
3. Invalid global symbols in the table are marked in red.
4. Repair or delete the invalid symbols.

### Adapting tags and connections

#### Introduction

Adapt the connection names and synchronize the tags for establishing the connection after the migration.

When the HMI device is networked with the device proxy PLC the system creates a connection and assigns a connection name. If an HMI connection already existed, adapt the new connection name.

#### Adapting the connection name

1. Copy the previous connection name.
2. Delete the existing connection.
3. Replace the new connection name by the previous name.

#### Symbolic connection of the tags

1. Call up the tag editor.
2. Select all the tags.
3. Click "Synchronize to compare with PLC tag".  
   The "Options for synchronizing WinCC tags" window opens.
4. Select the options "Data type and absolute address agree" and "Replace WinCC tag name by the PLC tag name" in the window.
5. Click "Synchronize".

   Synchronization of the tags is carried out.

### Updating a device proxy via a STEP 7 project file

#### Introduction

The data of the device proxy PLC have to be updated whenever changes are made in the SIMATIC Manager that affect the HMI device. This is, for example, the case when address area in the data blocks have been changed or extended.

#### Updating device proxy data

1. Update the data of the device proxy via the project file (*.s7p) of your STEP 7 project.
2. In the update dialog. select the same CPU that you also used during the initialization of the device proxy PLC as the data source.  
   An update with a different hardware configuration is not allowed.
3. Through the dialog you have the possibility to select newly created data blocks from the SIMATIC Manager additionally.   
   Only selected objects are imported in the TIA Portal project.
4. Confirm the selection using the "OK" button.

   Updating of the tags is started.
5. The addresses of the tags were adapted automatically through the symbolic connection of the tags.   
   This completes updating of the tags.

**Note**

All the data that were selected during the previous initialization are automatically selected again as well. You should only change this default setting if you consciously want to remove data from the device proxy PLC. If, for example, the DB1 was included in the TIA Portal project through the initialization, and you now deactivate the DB1, the DB1 is deleted from the TIA Portal project during updating.

### Including tags from the SIMATIC Manager

#### Introduction

Through the initialization of the device proxy PLC you have included the tags from the SIMATIC Manager into the WinCC project.

In WinCC, you insert tags of the device proxy PLC directly into an HMI screen or a screen object.

#### Inserting a tag into the HMI configuration

1. Open the folder with the program blocks of the device proxy PLC in the project tree.
2. Select the block that contains the tags.
3. All the tags of the selected block are displayed in the detail view.
4. Drag&amp;drop the tag from the detail view into the working area.

   An I/O field with the selected tag is created. Carry out further settings in the Inspector window.

Alternatively configure an I/O field in the HMI screen and drag&amp;drop the tag into the I/O field.

#### Result

The tag from a block of the device proxy PLC is inserted into the HMI project and connected with the I/O field.

### Configuring the "Direct keys" system function

#### Introduction

If you want to integrate HMI devices that can only be configured with WinCC (TIA Portal), for example SIMATIC HMI Comfort Panels, into the hardware configuration of the SIMATIC Manager, you require the corresponding matching GSD/GSDML files.

The required GSD/GSDM files for WinCC are located in [FAQs mutual configuration with WinCC (TIA Portal) and STEP 7 V5.x](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=4&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&groupid=4000002&extranet=standard&viewreg=WW&nodeid4=20229806&objaction=csopen)

#### Installing GSD files

1. Open the hardware configuration in the SIMATIC Manager.
2. Select the "Options &gt; Install New GSD Files" menu command.   
   The "Install GSD files" dialog is displayed.
3. Use the "Browse" button to select the file folder that contains the GSD files.
4. Mark all the files and click the "Install" command button.

**Note**

**PROFINET / PROFIBUS storage paths in the SIMATIC Manager**

The GSDML files for the HMI devices are located in the hardware catalog under „PROFINET IO &gt; HMI &gt; SIMATIC HMI &gt; GSD &gt; KP/x“.

The GSD files for the HMI devices are located in the hardware catalog under „PROFIBUS DP &gt; Weitere FELDGERÄTE &gt; MMI &gt; SIMATIC_HMI &gt; HMI CP_x“.

#### PROFINET connection: PROFINET IO direct keys

1. Note the properties used for the HMI device to be replaced.   
   Take particular note of I/O addresses, device name, device number and diagnostic addresses if these are evaluated.
2. Remove the existing GSD file.
3. Drag&amp;Drop the configured HMI device type from the hardware catalog onto the displayed PROFINET IO bus.
4. Adapt the properties as noted.
5. Confirm the entries with OK.
6. Save and compile the configuration and transfer the hardware configuration to the controller.

   ![PROFINET connection: PROFINET IO direct keys](images/67707017867_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET connection: PROFINET IO direct keys](images/67707017867_DV_resource.Stream@PNG-en-US.png)
7. Open the device configuration of the TP1200 Comfort and change to the "Device view".
8. Enter the PROFINET device name in the properties of the configured HMI device in WinCC under "Properties &gt; General &gt; PROFINET interface X1 &gt; Ethernet addresses".

   To assign the PROFINET device name, deselect the option "Generate PROFINET device name automatically".

**Note**

Take the rules for the names of PROFINET IO devices into consideration for the device name. Use only lower-case characters and no special characters for the device name.

**Note**

The PROFINET name in the WinCC configuration must correspond to the PROFINET name stored in the SIMATIC Manager.

#### PROFIBUS connection: PROFIBUS DP direct keys

Please note that the direct keys are configured in the SIMATIC Manager.

> **Note**
>
> If direct keys to several CPUs are configured from one panel, the direct keys will only function on one CPU.
>
> The further CPUs display a bus / group error.

1. Note the properties used for the HMI device to be replaced.   
   Take particular note of I/O addresses, device name and diagnostic addresses if these are evaluated.
2. Remove the existing GSD file.
3. Drag-and-drop the GSD module that contains the configured HMI device type from the hardware catalog to the PROFIBUS DP bus displayed.
4. Adapt the properties I/O address, device name, PROFIBUS address and diagnostic address as previously noted.
5. Confirm the entries with OK.
6. Save and compile the configuration and transfer the hardware configuration to the controller.

   ![PROFIBUS connection: PROFIBUS DP direct keys](images/67707949451_DV_resource.Stream@PNG-en-US.png)

   ![PROFIBUS connection: PROFIBUS DP direct keys](images/67707949451_DV_resource.Stream@PNG-en-US.png)
7. Open the device configuration of the HMI device that you want to use and change to the "Device view".
8. Network the PROFIBUS interface in the properties of the configured HMI device under "Properties &gt; General &gt; MPI/DP interface X2 &gt; PROFIBUS address &gt; Network interface with".
9. Specify the PROFIBUS address at "Parameters".

**Note**

The PROFIBUS address in the WinCC configuration must correspond to the PROFIBUS address stored in the SIMATIC Manager.
