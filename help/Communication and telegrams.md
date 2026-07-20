---
title: "Communication and telegrams"
package: StdrComTelegrammUIenUS
topics: 42
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communication and telegrams

This section contains information on the following topics:

- [Operating drives on the PROFIBUS](#operating-drives-on-the-profibus)
- [Operating drives on the PROFINET](#operating-drives-on-the-profinet)
- [Telegram configuration via PROFIdrive](#telegram-configuration-via-profidrive)
- [Interface parameters](#interface-parameters)
- [Linking drives via GSD](#linking-drives-via-gsd)

## Operating drives on the PROFIBUS

This section contains information on the following topics:

- [Operating a drive on the PROFIBUS](#operating-a-drive-on-the-profibus)
- [Editing DP master systems and interfaces](#editing-dp-master-systems-and-interfaces)
- [Configuring an isochronous DP master system](#configuring-an-isochronous-dp-master-system)

### Operating a drive on the PROFIBUS

#### Introduction

A drive should be operated via PROFIBUS in a DP master system with a controller. To create a PROFIBUS DP master system, you need to have one DP master and at least one DP slave. As soon as you connect a DP master to a DP slave via their PROFIBUS DP interfaces, a master-slave coupling is established. As a rule, you use the controller as a DP master and the drive as a DP slave here.

#### Requirements

- The controller (PLC) and drive (SINAMICS CU 320-DP) are created in a project.
- The network view of the project is opened.

#### Procedure

1. Click the link on the unassigned device in the network view (in the example, a SINAMICS drive) which is to be used as a DP slave.  
   All possible DP masters in the project are displayed.

   ![DP master-slave](images/133891664651_DV_resource.Stream@PNG-en-US.PNG)

   ![DP master-slave](images/133891664651_DV_resource.Stream@PNG-en-US.PNG)

   DP master-slave
2. Assign the drive, e.g. to a SIMATIC S7-1500 controller. A DB master system is automatically created together with the two nodes. If there is not yet a subnet between the DP master and DP slave, a new subnet is created between the DP master and DP slave.

   ![DP master-slave](images/133891698827_DV_resource.Stream@PNG-en-US.PNG)

   ![DP master-slave](images/133891698827_DV_resource.Stream@PNG-en-US.PNG)

   DP master-slave

   The name of the connected DP master is displayed as a link in the DP slave.

> **Note**
>
> You require a telegram for the communication between a controller and a drive.

#### More information on PROFIBUS in the DP master system

For detailed information on various PROFIBUS connections in the DP master system, see the following help page: [Configurations involving PROFIBUS DP](Configuring%20PROFIBUS%20DP.md#configuring-profibus-dp).

### Editing DP master systems and interfaces

Once you have created a DP master system, you also have the option of disconnecting the DP master system and its components. This can result in subnets with DP slaves but no DP master.

Generally, there is no need to edit the interfaces of a DP master. You can change the name and number on the DP master system.

#### Requirements

- The controller (PLC) and drive (SINAMICS CU 320-DP) are created in a project.
- The network view of the project is opened.
- There has to be a DP master system with one DP master and at least one DP slave.

#### Configuring the address of a DP slave

When a new DP master system is created, the DP address of the DP slave still must be set.

1. Right-click on the DP slave's DP interface.

   The PROFIBUS address of the DP slave is displayed in the Inspector window. The address is usually highlighted in light red, which shows that a further setting is required here.
2. Click in the "Address" input field.

   The possible setting range of the address is displayed in a popup window.
3. Enter the required PROFIBUS address.

   ![Configuring the DP address](images/133889521931_DV_resource.Stream@PNG-en-US.PNG)

   ![Configuring the DP address](images/133889521931_DV_resource.Stream@PNG-en-US.PNG)

   Configuring the DP address
4. Optional: If available, select an existing subnet under "Subnet".

#### Disconnecting the DP master from the DP master system

To disconnect the DP master system, proceed as follows:

1. Right-click on the DP interface of the DP master (in most cases, of the controller).
2. Select "Disconnect from master system" from the shortcut menu.

   The selected DP master is disconnected from the DP master system. A subnet with the DP slaves is retained.

#### Adding a DP master to the DP master system

To reassign a DP master to a subnet, proceed as follows:

1. Right-click on the DP interface of a DP master.
2. Select "Create master system" from the shortcut menu.
3. Drag-and-drop the new DP master system onto the DP interfaces of the DP slaves.

   The DP master combines with the DP slaves to recreate a DP master system.

#### Adding additional DP slaves to the DP master system

1. Select a DP slave from the hardware catalog.
2. Drag-and-drop the DP slave from the hardware catalog into the network view.
3. Draw a connecting line between the DP master's DP interface or the highlighted DP master system and the DP interface of the new DP slave.

### Configuring an isochronous DP master system

When a DP master system is created, the isochronous mode (or constant bus cycle time) is automatically activated. I.e. all DP slaves connected to the DP master are isochronous with the DP master. With this basic setting, the Ti/To times are the same for all slaves because they are obtained from the network. If required, you can manually configure the settings for each DP slave.

#### Requirements

- The controller (PLC) and drive (SINAMICS CU 320-DP) are created in a project.
- The network view of the project is opened.
- There has to be a DP master system with one DP master and at least one DP slave.

#### Setting the isochronous mode manually

1. Right-click on the DP interface of a selected DP slave.

   The Inspector window of the DP slave is displayed.
2. In the secondary navigation, activate the "Isynchronous mode" menu if it has not yet been selected.

   ![DP isochronous mode](images/133891707403_DV_resource.Stream@PNG-en-US.PNG)

   ![DP isochronous mode](images/133891707403_DV_resource.Stream@PNG-en-US.PNG)

   DP isochronous mode
3. Ensure that the "Synchronize DP slave to DP constant bus cycle time" option is active.

   All DP slaves obtain identical times from the PROFIBUS subnet with the "From subnet" setting.
4. To configure the times for the selected slave manually, select the "Manual" setting in the "Ti/To values" drop-down list.
5. Correct the time values in the "Time Ti (import process values)" and "Time To (import process values)" fields.

#### Deactivating the isochronous mode

1. Right-click on the DP interface of a selected DP slave.

   The Inspector window of the DP slave is displayed.
2. In the secondary navigation, activate the "Isynchronous mode" menu if it has not yet been selected.
3. Deactivate the preset option "Synchronize DP slave to DP constant bus cycle time".

   The selected DP slave is therefore no longer isochronous with the other DP slaves and with the DP master.

#### Editing constant bus cycle time settings

1. In the network view, click on the PROFIBUS connection between the DP master and a DP slave.

   The Inspector window of the DP slave is displayed.
2. In the secondary navigation, activate the "PROFIBUS > Constant bus cycle time" menu if it has not yet been selected.

   ![DP constant bus cycle time](images/133889531275_DV_resource.Stream@PNG-en-US.PNG)

   ![DP constant bus cycle time](images/133889531275_DV_resource.Stream@PNG-en-US.PNG)

   DP constant bus cycle time

   The following options are automatically activated:

   - Enable constant bus cycle time
   - DP cycle
   - Ti/To values ​​of the PROFIBUS
3. To change the default values of these options, deactivate the respective option and then correct the presettings in the input fields of the deactivated option.

## Operating drives on the PROFINET

This section contains information on the following topics:

- [Operating a drive (IO device) on the PROFINET IO](#operating-a-drive-io-device-on-the-profinet-io)
- [Configure sync domains and send clock](#configure-sync-domains-and-send-clock)
- [Set up the sync master and sync slave.](#set-up-the-sync-master-and-sync-slave)
- [Configuring the topology, interconnecting ports](#configuring-the-topology-interconnecting-ports)
- [Configure isochronous IO device](#configure-isochronous-io-device)

### Operating a drive (IO device) on the PROFINET IO

#### Introduction

A drive is to be operated as IO device via PROFINET IO on the PROFINET subnet of a controller.

> **Note**
>
> **IRT mode**
>
> If drives that cannot be operated with IRT are located between two IRT-capable devices, IRT operation is not possible. Therefore, when you insert a drive that is not IRT-capable, the drive must be inserted at the end of the bus.

#### Requirements

- The controller (PLC, e.g. a SIMATIC S7-1500) and drive (e.g. SINAMICS CU 320-2 PN) are created in a project.
- The network view of the project is opened.

#### Procedure

To operate a drive as an IO device, proceed as follows:

1. Select a SINAMICS drive in the hardware catalog at "Drives & starters > SINAMICS drives" and drag and drop it in the network view.
2. Click the link on the unassigned device in the network view (in the example, a SINAMICS S120).  
   All possible IO controllers in the project are displayed.

   ![Assigning an IO device to an IO controller](images/90655273739_DV_resource.Stream@PNG-en-US.png)

   Assigning an IO device to an IO controller
3. Assign the drive, e.g. to a SIMATIC S7-1500 controller. A PROFINET IO system and a sync domain with the two nodes are created automatically. If you assign another IO device to the IO system of the IO controller, the IO device is assigned automatically to the sync domain of the IO controller.

   ![SINAMICS drive unit on SIMATIC S7-1500 via PROFINET](images/119870748683_DV_resource.Stream@PNG-en-US.png)

   SINAMICS drive unit on SIMATIC S7-1500 via PROFINET

> **Note**
>
> You require a telegram for the communication between a controller and a drive.

After inserting the IO device, you can configure the sync domain and the isochronous mode of the IO device. Isochronous mode is required for typical motion control applications.

### Configure sync domains and send clock

#### Configuring sync domains

A sync domain is needed for synchronizing PROFINET IO devices. The sync domain ensures that all nodes that belong to it are synchronized. After being inserted, the nodes of the sync domain are not synchronized.

After inserting a controller and a SINAMICS S120 drive unit, they must first be assigned to a subnet. Unassigned devices are displayed as "Not assigned".

**To configure the sync domain, proceed as follows:**

1. Select the PROFINET IO system in the network view.
2. In the Inspector window, click the "General" tab and select "Domain management > Sync domain > Sync domain_1". You can set the parameters in the tab.
3. You can set a new name at "Sync domain". It is converted automatically to a conformant name that is displayed at "Converted name".
4. Select the sync master (SIMATIC S7-1500F-3 PN in the example) and select the RT class for the IO device (SINAMICS S120 in the example). When you select IRT, the synchronization role of the IO device is set automatically to sync slave.
5. Select the "send clock" for the sync domain.

   > **Note**
   >
   > You can set the send clock only when you have configured the synchronization role and the RT class at "IO devices".

![Configuring the sync domain](images/90655334539_DV_resource.Stream@PNG-en-US.png)

Configuring the sync domain

**Explanation of the parameters**

| Parameter | Description |
| --- | --- |
| ③ Sync domain | Name of the sync domain. This name is converted automatically if it does not conform with the DNS conventions. |
| ④ IO devices | Here, you can see a list of the IO devices of the sync domain. You can select the following parameters for the nodes:  - RT class: Select either RT (Real Time) or IRT (Isochronous Real Time). - Synchronization role: Select sync master or sync slave. The synchronization role is displayed as "Unsynchronized" per default, e.g. for devices in RT networks.   Information on RT classes and synchronization roles can be found in the SINAMICS S120 Communication Function Manual. |
| ⑤ Send clock | Select the send clock for the sync domain here. |
| ⑥ Node | The nodes of the PROFINET IO system are listed here. |

### Set up the sync master and sync slave.

#### Requirement

You have performed the following configuration steps:

- IO controller and IO device configured with RT
- Port interconnections are configured

#### Configuring the sync master

To configure a sync master, proceed as follows:

1. Select the PROFINET interface of the sync master in the network view.

   The interface settings are displayed in the Inspector window.
2. In the "General" tab, click "Advanced options > Real time settings > Synchronization".
3. Select the "Sync master" entry at "Synchronization role".

![Configuring the sync master](images/90655389195_DV_resource.Stream@PNG-en-US.png)

Configuring the sync master

#### Configuring the IO device as a sync slave

To configure a device within a PROFINET IO system as a sync slave, proceed as follows:

1. Select the PROFINET interface for the sync slave in the network view.  
   The interface settings are displayed in the Inspector window.
2. In the "General" tab, click "Advanced options > Real time settings > Synchronization".
3. Select "IRT" as RT class. In the example, the "Sync slave" entry is automatically selected as "Synchronization role".

![IO device as a sync slave](images/90655415435_DV_resource.Stream@PNG-en-US.png)

IO device as a sync slave

### Configuring the topology, interconnecting ports

#### Interconnecting ports

Prerequisite for IRT is the topology configuration with the specification of which device is connected via which port to which other devices.

There are two options for defining the properties of the cables between the ports of the switches:

- Via the topology view
- Via the object properties

#### Using the topology view

With the topology view you have an overview of all ports in the project and can interconnect them centrally.

**To configure the topology, proceed as follows:**

1. Click the "Topology view" tab.

   You can perform the following in the topology view:

   - Interconnect ports
   - Modify the properties of the interconnection
   - Insert passive components
   - Arrange for an offline/online comparison to be displayed in online mode
2. If you hover the mouse over the ports, port names are displayed in the tooltip. In the Inspector window, the properties for each selected port/device are displayed.
3. Click on the source port and drag-and-drop the connection to the target port.

   The topology view then shows the connection between the two ports.

![Topology view](images/90655355275_DV_resource.Stream@PNG-en-US.png)

Topology view

#### Port interconnection via the properties

After the selection of a device or an interface, the entries for the ports are displayed in the Inspector window in the "General" tab at "PROFINET PN / IO interface > Advanced options" or "Advanced options".

1. Select the interface, whose ports you want to edit, from the Inspector window.
2. Select the interface you wish to interconnect.
3. Select the "Port interconnection" entry.

   The "Local port" and "Partner port" dialogs open.
4. Open the "Partner port" drop-down menu.

   All devices with their PROFINET interfaces are shown.
5. Below the respective interface, select the port you want to connect to the selected port.

   Ports that you cannot connect are marked in red. Ports that are already assigned are not displayed.

   The connection between the ports is displayed in the topology view.
6. If necessary, edit the other parameters of the port.

#### Additional references

For more information on this topic, refer to the Online Help of the TIA Portal.

### Configure isochronous IO device

#### Configuring isochronous mode for IO devices

The drive and controller together form a sync domain. You must parameterize the IRT operating mode (for isochronous drives) and the PROFINET settings for motion control applications of the PROFINET IO system. Isochronous mode for the application on the bus is only possible for PROFINET IO with IRT. In the case of PROFINET IO with IRT, a sync master generates a synchronization telegram to which all sync slaves synchronize themselves. To use isochronous mode, you must configure it for the IO device.

> **Note**
>
> Isochronous mode only applies if isochronous submodules are configured in the IO device so that the IO controller has isochronous IO submodules. Otherwise, the Save and compile in the TIA Portal will be terminated with an error message.
>
> In order to configure the isochronous mode in the TIA Portal, you should therefore already have configured the drive and an axis for the controller in Startdrive and assigned them to a drive object.

**To configure isochronous mode, proceed as follows:**

1. Select the IO device in the network view and click the PN interface.

   The interface properties are displayed in the Inspector window.
2. In the secondary navigation of the "General" tab, click on "Advanced options > Isochronous mode".
3. Activate the "isochronous mode" option.
4. In the "detailed overview", the drive objects with the appropriate telegrams are displayed.   
   You must already have configured the objects and telegrams in Startdrive.
5. If necessary, activate the "isochronous mode" option besides the drive object with the appropriate telegram. This cannot be changed for telegrams for which isochronous mode is mandatory (e.g. telegram 105).

![Configure isochronous IO device](images/119857837963_DV_resource.Stream@PNG-en-US.png)

Configure isochronous IO device

#### Parameterizing isochronous mode

Isochronous mode can be activated and deactivated for each IO device or module in the IO device. You will find a more detailed description of the possible settings for isochronous mode in the following table.

| Parameter | Description |
| --- | --- |
| Isochronous mode | Activate this option if you want to operate the drive (IO device) in isochronous mode with the PROFINET IO. |
| Send clock | Shows the send clock of the PROFINET IO system. Click the link to edit the setting. |
| Application cycle | Shows the application cycle (multiple of the data cycle). |
| Ti/To values | Three settings are possible for the Ti/To values:  - Automatic: Ti/To is automatically calculated. - Manual: Ti/To can be edited. - Task: Ti/To values are transferred to the OB.   Ti, To: can only be edited if "manual" is set.  Ti<sub>Min</sub>/Ti<sub>Max</sub>: minimum or maximum time for Ti.  To<sub>Min</sub>/To<sub>Max</sub>: minimum or maximum time for To.  Interval: defined interval for Ti/To values. |
| Time Ti (actual value) | Specifies at what time Ti, the actual value will be read in before the cycle starts. |
| Intervals | Indicates in which interval the value will be read in. The value should not be changed. |
| Time To (setpoint) | Specifies at what time To, the setpoint will be read out after the end of the cycle. |
| Interval | Indicates in which interval the value will be read in. The value should not be changed. |

## Telegram configuration via PROFIdrive

This section contains information on the following topics:

- [Overview of telegram configuration](#overview-of-telegram-configuration)
- [Displaying telegram configuration](#displaying-telegram-configuration)
- [Detail settings of various drives](#detail-settings-of-various-drives)
- [Telegram overviews](#telegram-overviews)
- [Parameterizing sending (actual value/safety actual value)](#parameterizing-sending-actual-valuesafety-actual-value)
- [Parameterizing receiving (setpoint/safety setpoint)](#parameterizing-receiving-setpointsafety-setpoint)
- [Editing telegrams](#editing-telegrams)
- [Sorting telegrams (CU3x0-2 only)](#sorting-telegrams-cu3x0-2-only)
- [Structure of the telegrams, control and status words](#structure-of-the-telegrams-control-and-status-words)
- [PROFIdrive overview](#profidrive-overview)

### Overview of telegram configuration

#### Description

If the communication between the drive and the higher-level controller is via fieldbus (PROFIBUS DP, PROFINET IO), the data (setpoints and actual values) is transferred cyclically via PROFIdrive telegrams.

To configure a cyclic data transfer, proceed as follows:

- Insert the drive and controller
- Insert a PROFIBUS/PROFINET subnet
- Assign the drive to the controller
- Check the bus settings
- Parameterize the drive

  - Standard drives (SINAMICS G110/G115D/G120)

    You can already parameterize the telegrams in the drive wizard (drive operation on the SIMATIC motion control axis).
  - SINAMICS S210 drives

    You have to create telegrams for the drive control in the telegram configuration.
  - Multi-axis drives (SINAMICS S120, S150, G150, G130, MV with CU320-2; SIMATIC Drive Controller with CU320-2)

    You have to create telegrams for the relevant drive objects in the telegram configuration, e.g. drive axes, drive control, or infeed.
- Check and edit the telegram settings
- If you are controlling a drive with safety functions via PROFIsafe, you must insert the appropriate PROFIsafe telegram.

### Displaying telegram configuration

The "Telegram configuration" screen form is part of the device configuration and is displayed in the inspector window.

You can open this screen form either in the project navigator or, for Startdrive S drives, also by using direct links in the communication screen forms.

#### Calling telegram configuration via project navigator

1. Open the drive unit in the project navigator and double-click the entry "Device configuration".

   The device configuration opens.
2. Select the entry "Telegram configuration" in the "Properties" tab of the inspector window.

   The settings for the telegram configuration are shown under the respective fieldbus interface

### Detail settings of various drives

This section contains information on the following topics:

- [Settings for SINAMICS G110/G115D/G120](#settings-for-sinamics-g110g115dg120)
- [Settings for SINAMICS S120/S150/G150/G130/MV](#settings-for-sinamics-s120s150g150g130mv)
- [Settings for SIMATIC Drive Controller](#settings-for-simatic-drive-controller)
- [Settings for SINAMICS S210](#settings-for-sinamics-s210)
- [Settings for SINAMICS G220](#settings-for-sinamics-g220)
- [Settings for SINAMICS S200](#settings-for-sinamics-s200)

#### Settings for SINAMICS G110/G115D/G120

##### Telegram configuration for standard drives (1 drive object)

The dialog box for the telegram configuration is structured as follows:

![Telegram configuration](images/117096629259_DV_resource.Stream@PNG-en-US.png)

Telegram configuration

| Number | Description |  |
| --- | --- | --- |
| A | Area for the drive objects (setpoints, actual values and safety components) |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Display of the drive object |  |
| ② | Link to the communication screen forms of the respective drive object |  |
| ③ | Drop-down list with the available telegrams |  |
| ④ | Length of the telegram |  |
| ⑤ | Telegram extension |  |
| ⑥ | Communication direction (send direction ![Telegram configuration for standard drives (1 drive object)](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration for standard drives (1 drive object)](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑦ | Type of communication |  |
|  |  | MS = Master - Slave for PROFIBUS DP |
|  | CD = Controller - Device for PROFINET IO |  |
|  | F_ = PROFIsafe-specific extension (safety telegram) |  |
| ⑧ | Name of the partner (controller) |  |
| ⑨ | Partner data area |  |

#### Settings for SINAMICS S120/S150/G150/G130/MV

##### Telegram configuration for drives based on the CU 320-2

The dialog box for the telegram configuration is structured as follows:

![Example: Telegram configuration S120 with multiple drive objects](images/116919102475_DV_resource.Stream@PNG-en-US.png)

Example: Telegram configuration S120 with multiple drive objects

| Number | Description |  |
| --- | --- | --- |
| A | Area for the drive objects (setpoints, actual values and safety components). A telegram is assigned to each drive object for setpoints and actual values. "Free telegram" is selected by default. |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Header of a drive object  Using the header, you can move the drive object in the list with drag and drop (in the first column). This changes the sorting in the table and at the same time in the secondary navigation of the telegram configuration. |  |
| ② | Display of the drive object |  |
| ③ | Number of the drive object  This number is generated automatically according to the order in which a drive object was created in the device configuration and cannot be changed afterwards. Resorting in the table does not change this number. |  |
| ④ | Link to the communication screen forms of the respective drive object |  |
| ⑤ | Drop-down list with the available telegrams |  |
| ⑥ | Length of the telegram |  |
| ⑦ | Telegram extension |  |
| ⑧ | Communication direction (send direction ![Telegram configuration for drives based on the CU 320-2](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration for drives based on the CU 320-2](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑨ | Type of communication |  |
|  | MS = Master - slave for PROFIBUS DP |  |
| CD = Controller - Device for PROFINET IO |  |  |
| F_ = PROFIsafe-specific extension (safety telegram) |  |  |
| ⑩ | Name of the partner (controller) |  |
| ⑪ | Partner data area |  |

#### Settings for SIMATIC Drive Controller

##### Telegram configuration with SIMATIC Drive Controller

The dialog box for the telegram configuration is structured as follows:

![Cyclic data traffic control module "S120 for the CPU 150xD"](images/124693211147_DV_resource.Stream@PNG-en-US.png)

Cyclic data traffic control module "S120 for the CPU 150xD"

| Number | Description |  |
| --- | --- | --- |
| A | Area for the drive objects (setpoints, actual values and safety components). A telegram is assigned to each drive object for setpoints and actual values. "Free telegram" is selected by default. |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Header of a drive object  Using the header, you can move the drive object in the list with drag and drop (in the first column). This changes the sorting in the table and at the same time in the secondary navigation of the telegram configuration. |  |
| ② | Display of the drive object |  |
| ③ | Number of the drive object  This number is generated automatically according to the order in which a drive object was created in the device configuration and cannot be changed afterwards. Resorting in the table does not change this number. |  |
| ④ | Link to the communication screen forms of the respective drive object |  |
| ⑤ | Drop-down list with the available telegrams |  |
| ⑥ | Length of the telegram |  |
| ⑦ | Telegram extension |  |
| ⑧ | Communication direction (send direction ![Telegram configuration with SIMATIC Drive Controller](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration with SIMATIC Drive Controller](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑨ | Type of communication |  |
|  | MS = Master - Slave for PROFIBUS DP |  |
|  |  |  |
| F_ = PROFIsafe-specific extension (safety telegram) |  |  |
| ⑩ | Name of the partner (controller) |  |
| ⑪ | Partner data area |  |
| ⑫ | Hardware identifier for programming SIMATIC function blocks |  |

#### Settings for SINAMICS S210

##### Telegram configuration for S210 drives

The dialog box for the telegram configuration is structured as follows:

![Example: Telegram configuration S210](images/117055005707_DV_resource.Stream@PNG-en-US.png)

Example: Telegram configuration S210

| Number | Description |  |
| --- | --- | --- |
| A | Area for the drive objects (setpoints, actual values and safety components) |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Display of the drive object |  |
| ② | Link to the communication screen forms of the respective drive object |  |
| ③ | Drop-down list with the available telegrams |  |
| ④ | Length of the telegram |  |
| ⑤ | Telegram extension |  |
| ⑥ | Communication direction (send direction ![Telegram configuration for S210 drives](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration for S210 drives](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑦ | Type of communication |  |
|  |  |  |
| CD = Controller - Device for PROFINET IO |  |  |
| F_ = PROFIsafe-specific extension (safety telegram) |  |  |
| ⑧ | Name of the partner (controller) |  |
| ⑨ | Partner data area |  |

#### Settings for SINAMICS G220

##### Telegram configuration for standard drives (1 G220 drive)

The dialog box for the telegram configuration is structured as follows:

![Telegram configuration](images/149184348171_DV_resource.Stream@PNG-en-US.png)

Telegram configuration

| Number | Description |  |
| --- | --- | --- |
| A | Area for the drive objects (setpoints, actual values and safety components) |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Display of the drive object |  |
| ② | Link to the communication screen forms of the respective drive object |  |
| ③ | Drop-down list with the available telegrams |  |
| ④ | Length of the telegram |  |
| ⑤ | Telegram extension |  |
| ⑥ | Communication direction (send direction ![Telegram configuration for standard drives (1 G220 drive)](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration for standard drives (1 G220 drive)](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑦ | Type of communication |  |
|  |  |  |
|  | CD = Controller - Device for PROFINET IO |  |
|  | F_ = PROFIsafe-specific extension (safety telegram) |  |
| ⑧ | Name of the partner (controller) |  |
| ⑨ | Partner data area |  |

#### Settings for SINAMICS S200

##### Telegram configuration for S200 drives

The dialog box for the telegram configuration is structured as follows:

![Telegram configuration in S200](images/162111555851_DV_resource.Stream@PNG-en-US.png)

Telegram configuration in S200

| Number | Description |  |
| --- | --- | --- |
| A | Area for drive objects (setpoints, actual values) |  |
| B | Area for the interfaces |  |
| C | Area for the communication partners of the drive (e.g. controller or another drive) |  |
| ① | Display of the drive object |  |
| ② | Link to the communication screen forms of the respective drive object |  |
| ③ | Drop-down list with the available telegrams |  |
| ④ | Length of the telegram |  |
| ⑤ | Telegram extension |  |
| ⑥ | Communication direction (send direction ![Telegram configuration for S200 drives](images/83776001163_DV_resource.Stream@PNG-de-DE.png)/receive direction ![Telegram configuration for S200 drives](images/83775992331_DV_resource.Stream@PNG-de-DE.png)) |  |
| ⑦ | Type of communication |  |
|  |  | CD = Controller - Device for PROFINET IO |
| ⑧ | Name of the partner (controller) |  |
| ⑨ | Partner data area |  |

### Telegram overviews

This section contains information on the following topics:

- [Telegram overview for SINAMICS G120G/G115D/G110M](#telegram-overview-for-sinamics-g120gg115dg110m)
- [Telegram overview for SINAMICS S120/S150/G150/G130/MV](#telegram-overview-for-sinamics-s120s150g150g130mv)
- [Telegram overview SIMATIC Drive Controller](#telegram-overview-simatic-drive-controller)
- [Telegram overview for SINAMICS S210](#telegram-overview-for-sinamics-s210)
- [Telegram overview for SINAMICS G220](#telegram-overview-for-sinamics-g220)
- [Telegram overview for SINAMICS S200](#telegram-overview-for-sinamics-s200)

#### Telegram overview for SINAMICS G120G/G115D/G110M

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

G120, G115D and G110M telegrams

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 1 | Speed setpoint, 16-bit |
| 2 | Speed setpoint, 32-bit |
| 3 | Speed setpoint, 32-bit with 1 position encoder |
| 4 | Speed setpoint, 32-bit with 2 position encoders |
| 7 | Basic positioner with selection of the traversing block |
| 9 | Basic positioner with direct setpoint specification (MDI) |
| 20 | 16-bit speed setpoint for VIK-NAMUR |
| 110 | Basic positioner with direct setpoint specification (MDI), override, and actual position value |
| 111 | Basic positioner with direct setpoint specification (MDI), override, actual position value, and actual speed value |
| 350 | Speed setpoint, 16-bit with torque limitation |
| 352 | 16-bit speed setpoint for PCS7 |
| 353 | 16-bit speed setpoint to read and write parameters |
| 354 | 16-bit speed setpoint for PCS7 to read and write parameters |
| 999 | Unassigned interconnection and length |

#### Telegram overview for SINAMICS S120/S150/G150/G130/MV

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

S120, S150, G150, G130, MV telegrams

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 1 | Speed setpoint, 16-bit |
| 2 | Speed setpoint, 32-bit |
| 3 | Speed setpoint, 32-bit with 1 position encoder |
| 4 | Speed setpoint, 32-bit with 2 position encoders |
| 5 | Speed setpoint, 32-bit with 1 position encoder and Dynamic Servo Control |
| 6 | Speed setpoint, 32-bit with 2 position encoders and DSC Dynamic Servo Control |
| 7 | Basic positioner with selection of the traversing block |
| 9 | Basic positioner with direct setpoint specification (MDI) |
| 20 | 16-bit speed setpoint for VIK-NAMUR |
| 81 | Standard encoder |
| 82 | Standard encoder with actual speed value 16-bit |
| 83 | Standard encoder with actual speed value 32-bit |
| 102 | Speed setpoint, 32-bit with 1 position encoder and torque reduction |
| 103 | Speed setpoint, 32 bit with 2 position encoders and torque reduction |
| 105 | Speed setpoint, 32-bit with 1 position encoder, torque reduction, and Dynamic Servo Control |
| 106 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, and Dynamic Servo Control |
| 110 | Basic positioner with direct setpoint specification (MDI), override, and actual position value |
| 111 | Basic positioner with direct setpoint specification (MDI), override, actual position value, and actual speed value |
| 116 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, DSC, and other actual values |
| 118 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, DSC, other actual values, and 2 external encoders |
| 125 | Dynamic Servo Control with torque feedforward control, 1 position encoder (encoder 1) |
| 126 | Dynamic Servo Control with torque feedforward control, 2 position encoders (encoder 1 and encoder 2) |
| 136 | Dynamic Servo Control with torque feedforward control, 2 position encoders (encoder 1 and encoder 2), 4 trace signals |
| 138 | Dynamic Servo Control with torque feedforward control, 2 external position encoders (encoder 2 and encoder 3), 4 trace signals |
| 139 | Speed/position control with Dynamic Servo Control and torque feedforward control, 1 position encoder, clamping status, supplementary actual values |
| 166 | Hydraulic axis (HLA) with two encoder channels and HLA supplementary signals |
| 220 | Speed setpoint, 32-bit for metal industry |
| 350 | Speed setpoint, 16-bit with torque limitation |
| 352 | 16-bit speed setpoint for PCS7 |
| 353 | 16-bit speed setpoint to read and write parameters |
| 354 | 16-bit speed setpoint for PCS7 to read and write parameters |
| 370 | Infeed |
| 371 | Infeed, metal industry |
| 390 | Control Unit with digital inputs DI 0 … DI 15 and digital outputs DO 8 … DO 15 |
| 391 | Control Unit with digital inputs DI 0 … DI 15, DO 8 … DO 15 and 2 measuring inputs |
| 392 | Control Unit with digital inputs DI 0 … DI 15, digital outputs DO 8 … DO 15, and 6 measuring inputs |
| 393 | Control Unit with digital inputs DI 0 … DI 22, digital outputs DO 8 … DO 16, 8 measuring inputs, and analog input |
| 394 | Control Unit with digital inputs DI 0 … DI 22 and digital outputs DO 8 … DO 16 |
| 395 | Control Unit with digital inputs DI 0 … DI 22, digital outputs DO 8 … DO 16, and 16 measuring inputs |
| 700 | Additional PZD-0/3 |
| 701 | Additional PZD-2/5 |
| 750 | Additional PZD-0/3 for torque control |
| 999 | Unassigned interconnection and length |
| 1100 | Supplementary telegram process monitoring (actual value) |

> **Note**
>
> **Supplementary telegram 1100**
>
> Supplementary telegram 1100 is a 32-word free actual value telegram. It does not take the PZDs from the normal PZD range, but has its own parameters. It is only available for the Control Unit, and must be the last telegram in the list.
>
> The following parameters can also be parameterized if this supplementary telegram is included in list "Telegram configuration":
>
> - p8966
> - p8967
> - r8977
> - r8978

##### Assignment of Safety Integrated Functions to PROFIsafe telegrams

The following table provides an overview of which Safety Integrated Function you can control with which PROFIsafe telegram.

| Safety function | PROFIsafe telegram |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 30 | 31 | 901 | 902 | 903 |  |
| STO | x | x | x | x | x |
| SS1 | x | x | x | x | x |
| SOS | x | x | x | x | x |
| SS2 | x | x | x | x | x |
| SS2E | - | x | x | x | x |
| SLS | x | x | x | x | x |
| SSM<sup>1)</sup> | x | x | x | x | x |
| SDI | x | x | x | x | x |
| SLP | x<sup>2)</sup> | x | x | x | x |
| SCA | - | - | - | - | x |
| SLA | x | x | x | x | x |
| SP | - | - | x | x | - |
| <sup>1) </sup>As feedback in S_ZSW1 and S_ZSW2   <sup>2)</sup> Without safe switchover between 2 different position ranges |  |  |  |  |  |

##### Overview of the PROFIsafe telegrams in Startdrive (does not apply to MV)

The following table provides an overview of the available telegrams. For the various drives (S120, S150, G150, G130), only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 30 | Transfers the Safety control word 1 (S_STW1) and the Safety status word 1 (S_ZSW1). |
| 31 | Transfers the Safety control word 2 (S_STW2) and the Safety status word 2 (S_ZSW2). |
| 901 | Transfers the S_STW2, the variable SLS limit (S_SLS_LIMIT_A), the S_ZSW2, the active SLS value of stage 1 (S_SLS_LIMIT_A_ACTIVE), a counter value (S_CYCLE_COUNT) and the safe position value in 16-bit format (S_XIST16). |
| 902 | Transfers the S_STW2, the variable SLS limit (S_SLS_LIMIT_A), S_ZSW2, the active SLS value of stage 1 (S_SLS_LIMIT_A_ACTIVE), counter value (S_CYCLE_COUNT) and the safe position value in 32-bit format (S_XIST32). |
| 903 | Transfers S_STW2, S_SLS_LIMIT_A, S_ZSW2, S_ZSW_CAM1 and S_SLS_LIMIT_A_ACTIVE. |

#### Telegram overview SIMATIC Drive Controller

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

Drive Controller telegrams

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 1 | Speed setpoint, 16-bit |
| 2 | Speed setpoint, 32-bit |
| 3 | Speed setpoint, 32-bit with 1 position encoder |
| 4 | Speed setpoint, 32-bit with 2 position encoders |
| 5 | Speed setpoint, 32-bit with 1 position encoder and Dynamic Servo Control |
| 6 | Speed setpoint, 32-bit with 2 position encoders and DSC Dynamic Servo Control |
| 20 | 16-bit speed setpoint for VIK-NAMUR |
| 81 | Standard encoder |
| 82 | Standard encoder with actual speed value 16-bit |
| 83 | Standard encoder with actual speed value 32-bit |
| 102 | Speed setpoint, 32-bit with 1 position encoder and torque reduction |
| 103 | Speed setpoint, 32 bit with 2 position encoders and torque reduction |
| 105 | Speed setpoint, 32-bit with 1 position encoder, torque reduction, and Dynamic Servo Control |
| 106 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, and Dynamic Servo Control |
| 116 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, DSC, and other actual values |
| 118 | Speed setpoint, 32-bit with 2 position encoders, torque reduction, DSC, other actual values, and 2 external encoders |
| 125 | Dynamic Servo Control with torque feedforward control, 1 position encoder (encoder 1) |
| 126 | Dynamic Servo Control with torque feedforward control, 2 position encoders (encoder 1 and encoder 2) |
| 136 | Dynamic Servo Control with torque feedforward control, 2 position encoders (encoder 1 and encoder 2), 4 trace signals |
| 138 | Dynamic Servo Control with torque feedforward control, 2 external position encoders (encoder 2 and encoder 3), 4 trace signals |
| 139 | Speed/position control with Dynamic Servo Control and torque feedforward control, 1 position encoder, clamping status, supplementary actual values |
| 146 | Speed/position control with Dynamic Servo Control and torque precontrol, 2 position encoders (encoder 1 and encoder 2), additional actual values, adaptation parameters |
| 148 | Speed/position control with Dynamic Servo Control and torque precontrol, 1 position encoder, clamping status, additional actual values, adaptation parameters |
| 166 | Hydraulic axis (HLA) with two encoder channels and HLA supplementary signals |
| 220 | Speed setpoint, 32-bit for metal industry |
| 350 | Speed setpoint, 16-bit with torque limitation |
| 352 | 16-bit speed setpoint for PCS7 |
| 353 | 16-bit speed setpoint to read and write parameters |
| 354 | 16-bit speed setpoint for PCS7 to read and write parameters |
| 370 | Infeed unit; standard telegram for infeed units of SINAMICS Integrated |
| 371 | Infeed, metal industry |
| 390 | Control Unit with digital inputs DI 0 … DI 15 and digital outputs DO 8 … DO 15 |
| 391 | Control Unit with digital inputs DI 0 … DI 15, DO 8 … DO 15 and 2 measuring inputs |
| 392 | Control Unit with digital inputs DI 0 … DI 15, digital outputs DO 8 … DO 15, and 6 measuring inputs |
| 393 | Control Unit with digital inputs DI 0 … DI 22, digital outputs DO 8 … DO 16, 8 measuring inputs, and analog input  Standard telegram for SINAMICS Integrated Control Units |
| 394 | Control Unit with digital inputs DI 0 … DI 22 and digital outputs DO 8 … DO 16 |
| 395 | Control Unit with digital inputs DI 0 … DI 22, digital outputs DO 8 … DO 16, and 16 measuring inputs |
| 700 | Additional PZD-0/3 |
| 701 | Additional PZD-2/5 |
| 750 | Additional PZD-0/3 for torque control |
| 999 | Unassigned interconnection and length |
| 1100 | Supplementary telegram process monitoring (actual value) |

> **Note**
>
> **Supplementary telegram 1100**
>
> Supplementary telegram 1100 is a 32-word free actual value telegram. It does not take the PZDs from the normal PZD range, but has its own parameters. It is only available for the Control Unit, and must be the last telegram in the list.
>
> The following parameters can also be parameterized if this supplementary telegram is included in list "Telegram configuration":
>
> - p8966
> - p8967
> - r8977
> - r8978

##### Assignment of Safety Integrated Functions to PROFIsafe telegrams

The following table provides an overview of which Safety Integrated Function you can control with which PROFIsafe telegram.

| Safety function | PROFIsafe telegram |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 30 | 31 | 901 | 902 | 903 |  |
| STO | x | x | x | x | x |
| SS1 | x | x | x | x | x |
| SOS | x | x | x | x | x |
| SS2 | x | x | x | x | x |
| SS2E | - | x | x | x | x |
| SLS | x | x | x | x | x |
| SSM<sup>1)</sup> | x | x | x | x | x |
| SDI | x | x | x | x | x |
| SLP | x<sup>2)</sup> | x | x | x | x |
| SCA | - | - | - | - | x |
| SLA | x | x | x | x | x |
| SP | - | - | x | x | - |
| <sup>1) </sup>As feedback in S_ZSW1 and S_ZSW2   <sup>2)</sup> Without safe switchover between 2 different position ranges |  |  |  |  |  |

##### Overview of PROFIsafe telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

| Symbol | Meaning |
| --- | --- |
| **Telegram** | **Description** |
| 30 | Transfers the Safety control word 1 (S_STW1) and the Safety status word 1 (S_ZSW1). |
| 31 | Transfers the Safety control word 2 (S_STW2) and the Safety status word 2 (S_ZSW2). |
| 901 | Transfers the S_STW2, the variable SLS limit (S_SLS_LIMIT_A), the S_ZSW2, the active SLS value of stage 1 (S_SLS_LIMIT_A_ACTIVE), a counter value (S_CYCLE_COUNT) and the safe position value in 16-bit format (S_XIST16). |
| 902 | Transfers the S_STW2, the variable SLS limit (S_SLS_LIMIT_A), S_ZSW2, the active SLS value of stage 1 (S_SLS_LIMIT_A_ACTIVE), counter value (S_CYCLE_COUNT) and the safe position value in 32-bit format (S_XIST32). |
| 903 | Transfers S_STW2, S_SLS_LIMIT_A, S_ZSW2, S_ZSW_CAM1 and S_SLS_LIMIT_A_ACTIVE. |

#### Telegram overview for SINAMICS S210

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available per drive.

The telegram descriptions can be found in the function diagrams of the individual drives:

Telegrams for S210 drives

| Telegram | Description | Transfers the following signals: |
| --- | --- | --- |
| 3 | Speed setpoint, 32-bit with 1 position encoder | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 4<sup> 2)</sup> | Speed setpoint, 32-bit with 2 position encoders | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G2_STW, G1_XIST1, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 5 | Speed setpoint, 32-bit with 1 position encoder and Dynamic Servo Control  Transfers the following signals: | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, XERR, G1_XIST1, KPC, G1_XIST2 |
| 6<sup> 2)</sup> | Speed setpoint, 32-bit with 2 position encoders and DSC Dynamic Servo Control | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G2_STW, XERR, G1_XIST1, KPC, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 7 <sup>1)</sup> | Basic positioner with selection of the traversing block | STW1, ZSW1, SATZANW, AKTSATZ |
| 9 <sup>1)</sup> | Basic positioner with direct setpoint specification (MDI) | STW1, ZSW1, SATZANW, AKTSATZ, STW2, ZSW2, MDI_TARPOS, XIST_A, MDI_VELOCITY, MDI_ACC, MDI_DEC, MDI_MOD |
| 102 | Speed setpoint, 32-bit with 1 position encoder and torque reduction | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 103<sup> 2)</sup> | Speed setpoint, 32 bit with 2 position encoders and torque reduction | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G2_STW, G1_XIST1, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 105 | Speed setpoint, 32-bit with 1 position encoder, torque reduction, and Dynamic Servo Control | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, XERR, G1_XIST1, KPC, G1_XIST2 |
| 106<sup> 2)</sup> | Speed setpoint, 32-bit with 2 position encoders, torque reduction, and Dynamic Servo Control | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G2_STW, XERR, G1_XIST1, KPC, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 111<sup>1)</sup> | Basic positioner with direct setpoint specification (MDI), PZD length 12/12 words | STW1, ZSW1, POS_STW1, POS_ZSW1, POS_STW2, POS_ZSW2, STW2, ZSW2, OVERRIDE, MELDW, MDI_TARPOS, XIST_A, MDI_VELOCITY, NIST_B, MDI_ACC, FAULT_CODE, MDI_DEC, WARN_CODE |
| 112<sup>1)</sup> | Basic positioner with 32-bit physical units and length unit, PZD length 17/12 words  Preset as standard for EPOS. | STW1, ZSW1, POS_STW1, POS_ZSW1, POS_STW2, POS_ZSW2, STW2, ZSW2, OVERRIDE, Res. POS_ZSW3, MDI_TARPOS_F, XIST_F, MDI_VELOCITY_F, VIST_F, MDI_ACC_F, MELDW, FAULT_CODE, MDI_DEC_F, WARN_CODE, REF_COORDINATE |
| 700 | Supplementary PZD-0/3 for the status of Safety Integrated functions | S_ZSW1B, S_V_LIMIT_B |
| 701 | Additional PZD-2/5 | S_STW1B, S_ZSW1B, S_STW3B, S_ZSW2B, S_V_LIMIT_B, S_ZSW3B |
| 750 | Additional PZD-0/3 for torque control | M_ADD1, M_LIMIT_POS, M_LIMIT_NEG, M_ACT |
| <sup>1)</sup> When using the EPOS function: The telegrams 3, 4, 5, 6, 102, 103, 105 and 106 are omitted in this case.   <sup>2)</sup> As of firmware V6.3 with speed control |  |  |

Telegrams for S210 Safety Integrated

| Telegram | Description | Transfers the following signals: |
| --- | --- | --- |
| 30 | Transfers safety control word 1 and safety status word 1. | S_STW1, S_ZSW1 |
| 901 | Transfers safety control word 2 as well as safety status word 2, plus the variable SLS limit, the active SLS value of stage 1. | S_STW2, S_ZSW2, S_SLS_LIM_A, S_SLS_LIM_A_ACT |
| 902 | Transfers the safety control word 2, the variable SLS limit, the safety status word 2, the active SLS value of level 1, the counter value. | S_STW2, S_SLS_LIMIT_A, S_ZSW2, S_SLS_LIMIT_A_ACTIVE, S_CYCLE_COUNT, S_XIST32 |

#### Telegram overview for SINAMICS G220

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available for each drive or each drive object.

The telegram descriptions can be found in the function diagrams of the individual drives:

Telegrams G220

| Telegram | Description | Transfers the following signals: |
| --- | --- | --- |
| 1 | Speed setpoint, 16-bit | STW1, ZSW1, NSOLL_A, NIST_A |
| 2 | Speed setpoint, 32-bit | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2 |
| 3 | Speed setpoint, 32-bit with 1 position encoder | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 4 | Speed setpoint, 32-bit with 2 position encoders | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G2_STW, G1_XIST1, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 20 | 16-bit speed setpoint for VIK-NAMUR | STW1, ZSW1, NSOLL_A / FSOLL, NIST_A_GLATT / FIST_GLATT, IAIST_GLATT, MIST_GLATT / ITIST_GLATT, PIST_GLATT, MELD_NAMUR |
| 102 | Speed setpoint, 32-bit with 1 position encoder and torque reduction | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 103 | Speed setpoint, 32 bit with 2 position encoders and torque reduction | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G2_STW, G1_XIST1, G1_XIST2, G2_ZSW, G2_XIST1, G2_XIST2 |
| 352 | 16-bit speed setpoint for PCS7 | STW1, ZSW1, NSOLL_A / FSOLL, NIST_A_GLATT / FIST_GLATT, IAIST_GLATT, MIST_GLATT, WARN_CODE, FAULT_CODE  The output signals from PZD3 to PZD6 can be freely assigned. |
| 999 | Unassigned interconnection and length | - |

##### Overview of PROFIsafe telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available per drive.

The telegram descriptions can be found in the function diagrams of the individual drives:

| Telegram | Description | Transfers the following signals: |
| --- | --- | --- |
| 31 | Transfers the safety control word 2 and the safety status word 2. | S_STW2, S_ZSW2 |
| 902 | Transfers the safety control word 2, the variable SLS limit, the safety status word 2, the active SLS value of level 1, the counter value. | S_STW2, S_SLS_LIMIT_A, S_ZSW2, S_SLS_LIMIT_A_ACTIVE, S_CYCLE_COUNT |

#### Telegram overview for SINAMICS S200

##### Overview of the telegrams in Startdrive

The following table provides an overview of the available telegrams. For the various drives, only one selection of telegrams is ever available per drive.

The telegram descriptions can be found in the function diagrams of the individual drives:

Telegrams for S200 drives

| Telegram | Description | Transfers the following signals: |
| --- | --- | --- |
| 1 | Speed setpoint, 16-bit | STW1, ZSW1, NSOLL_A, NIST_A |
| 2 | Speed setpoint, 32-bit | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2 |
| 3 | Speed setpoint, 32-bit with 1 position encoder | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 5 | Speed setpoint, 32-bit with 1 position encoder and Dynamic Servo Control | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, G1_STW, G1_ZSW, XERR, G1_XIST1, KPC, G1_XIST2 |
| 7 <sup>1)</sup> | Basic positioner with selection of the traversing block | STW1, ZSW1, SATZANW, AKTSATZ |
| 9 <sup>1)</sup> | Basic positioner with direct setpoint specification (MDI) | STW1, ZSW1, SATZANW, AKTSATZ, STW2, ZSW2, MDI_TARPOS, XIST_A, MDI_VELOCITY, MDI_ACC, MDI_DEC, MDI_MOD |
| 102 | Speed setpoint, 32-bit with 1 position encoder and torque reduction | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, G1_XIST1, G1_XIST2 |
| 105 | Speed setpoint, 32-bit with 1 position encoder, torque reduction, and Dynamic Servo Control | STW1, ZSW1, NSOLL_B, NIST_B, STW2, ZSW2, MOMRED, MELDW, G1_STW, G1_ZSW, XERR, G1_XIST1, KPC, G1_XIST2 |
| 111<sup>1)</sup> | Basic positioner with direct setpoint specification (MDI), PZD length 12/12 words | STW1, ZSW1, POS_STW1, POS_ZSW1, POS_STW2, POS_ZSW2, STW2, ZSW2, OVERRIDE, MELDW, MDI_TARPOS, XIST_A, MDI_VELOCITY, NIST_B, MDI_ACC, FAULT_CODE, MDI_DEC, WARN_CODE |
| 112<sup>1)</sup> | Basic positioner with 32-bit physical units and length unit, PZD length 17/12 words  Preset as standard for EPOS. | STW1, ZSW1, POS_STW1, POS_ZSW1, POS_STW2, POS_ZSW2, STW2, ZSW2, OVERRIDE, Res. POS_ZSW3, MDI_TARPOS_F, XIST_F, MDI_VELOCITY_F, VIST_F, MDI_ACC_F, MELDW, FAULT_CODE, MDI_DEC_F, WARN_CODE, REF_COORDINATE |
| 750 | Additional PZD-0/3 for torque control | M_ADD1, M_LIMIT_POS, M_LIMIT_NEG, M_ACT |
| <sup>1)</sup> When using the EPOS function: The telegrams 1, 2, 3, 5, 102 and 105 are omitted in this case. |  |  |

> **Note**
>
> SINAMICS S200 does not use PROFIsafe telegrams.

### Parameterizing sending (actual value/safety actual value)

#### Description

Edit the following parameters for the setpoints of the communication between the drive and the controller. The communication direction is from the drive to the partner (e.g. a controller). The settings relevant for PROFIsafe are marked in yellow and are only shown when you add a safety telegram.

> **Note**
>
> **Check of the PROFIsafe telegrams**
>
> By default, the setting of the PROFIsafe telegrams under "Telegram configuration" is not password-protected.
>
> - Use the TIA Portal project protection for the entire project to protect the telegram settings from unintentionally or intentionally being overwritten.
> - When working with PROFIsafe telegrams, check the setting of the PROFIsafe telegrams again during the safety acceptance process in order to ensure that the selected PROFIsafe telegram corresponds to the requirements of your application.

| Parameter | Drive | Controller |
| --- | --- | --- |
| Name | Name of the drive in the project | Name of the assigned controller in the network view. The assignment can only be changed there. |
| Role (for DP drives) | Slave | Master |
| Role (for PN drives) | Device | Controller |
| Telegram | Drop-down list to select the telegram (default setting is telegram 1), see also [Structure of the telegrams, control and status words](#structure-of-the-telegrams-control-and-status-words). |  |
| Telegram (PROFIsafe​) | Drop-down list to select the PROFIsafe telegram (default setting is telegram 30). |  |
| PROFIBUS address (DP drives) | PROFIBUS address of the slave | PROFIBUS address of the master |
| IP address (PN drives) | IP address of the drive | IP address of the IO controller (cannot be changed) |
| F address (only for PROFIsafe) | PROFIsafe address of the destination (F_Dest_Add). The address uniquely identifies the destination. | PROFIsafe address of the source (F_Source_Add). The address uniquely identifies the source. |
| Slot | Slot of the device | - |
| Start address | Drop-down list to select the process data word (PZD) | Next free start address for the configured module. You can accept or change the address.​ |
| Length | Length of the selected telegram |  |
| Extension | Enter the telegram extension here for the transfer of the actual value. If you have entered an extension at "Telegram configuration", it is also displayed here. |  |
| Consistency | The use of various consistency areas is useful to optimize the performance of an S7-CPU. Consistency areas that are longer than two words must be edited with system functions. You can use the effective Load/Transfer commands for consistency areas up to two words.   **Total length:**   The consistency applies for all data of this slot. This default entry should usually be sufficient.   **Unit**:   The consistency applies for one process data word. You must configure at least a "2" word "Total length" for the transfer of a double word. |  |
| Organization block | Select the organization block from the drop-down list.   If you have assigned the drive to a controller, you require an organization block for the communication between the drive and the controller. If, for example, you create for an S7-1500, a technology object of the "Positioning axis" type and assign it to a drive axis, you then require an organization block of the "MC-Servo [OB91]" type. The communications must then be isochronous. Further OBs are, for example, Main [OB1] or for safety functions, an FOB_RTG1 [OB123]. |  |
| Process image | Select the process image partition that you want to use in the drop-down list in order to transfer the data consistently, e.g. OB1-PI. For information on process images, please enter the term in the online help search. |  |
| Interrupt OB number | Use the interrupt OB to output diagnostic information. |  |
| F-watchdog time | Monitoring time in the fail-safe DP standard slave / IO standard device / PA field device.  A valid, current safety telegram must arrive from the F-CPU within the monitoring time. This ensures that failures and errors are detected and the appropriate reactions triggered to keep the F system in a safe state or to transfer it to a safe state. |  |
| F-I/O DB number | The number of the block that controls the F-I/O. |  |
| F-I/O DB name | The name of the block that controls the F-I/O. |  |

### Parameterizing receiving (setpoint/safety setpoint)

#### Description

Edit the following parameters for the setpoints of the communication between the drive and the controller. The communication direction is from the partner (e.g. a controller) to the drive. The settings relevant for PROFIsafe are marked in yellow and are only shown when you add a safety telegram.

> **Note**
>
> **Check of the PROFIsafe telegrams**
>
> By default, the setting of the PROFIsafe telegrams under "Telegram configuration" is not password-protected.
>
> - Use the TIA Portal project protection for the entire project to protect the telegram settings from unintentionally or intentionally being overwritten.
> - When working with PROFIsafe telegrams, check the setting of the PROFIsafe telegrams again during the safety acceptance process in order to ensure that the selected PROFIsafe telegram corresponds to the requirements of your application.

| Parameter | Drive | Controller |
| --- | --- | --- |
| Name | Name of the drive in the project | Name of the assigned controller in the network view. The assignment can only be changed there. |
| Role (for DP drives) | Slave | Master |
| Role (for PN drives) | Device | Controller |
| Telegram | Drop-down list to select the telegram (default setting is telegram 1), see also [Structure of the telegrams, control and status words](#structure-of-the-telegrams-control-and-status-words). |  |
| Telegram (PROFIsafe​) | Drop-down list to select the PROFIsafe telegram (default setting is telegram 30). |  |
| PROFIBUS address (DP drives) | PROFIBUS address of the slave | PROFIBUS address of the master (cannot be changed). |
| IP address (PN drives) | IP address of the drive | IP address of the IO controller (cannot be changed) |
| F address (only for PROFIsafe) | PROFIsafe address of the destination (F_Dest_Add) | PROFIsafe address of the source (F_Source_Add) |
| Slot | Slot of the device | - |
| Start address | Drop-down list to select the process data word (PZD) | Next free start address for the configured module that you can accept or change.​ |
| Length | Length of the telegram |  |
| Extension | Enter the telegram extension here for the transfer of the setpoint. If you have entered an extension at "Telegram configuration", it is also displayed here. |  |
| Consistency | The use of various consistency areas is useful to optimize the performance of an S7-CPU. Consistency areas that are longer than two words must be edited with system functions. You can use the effective Load/Transfer commands for consistency areas up to two words.   **Total length:**   The consistency applies for all data of this slot. This default entry should usually be sufficient.   **Unit**:   The consistency applies for one process data word. You must configure at least a "2" word "Total length" for the transfer of a double word. |  |
| Organization block | Select the organization block from the drop-down list.   If you have assigned the drive to a controller, you require an organization block for the communication between the drive and the controller. If, for example, you create for an S7-1500, a technology object of the "Positioning axis" type and assign it to a drive axis, you then require an organization block of the "MC-Servo [OB91]" type. The communications must then be isochronous. Further OBs are, for example, Main [OB1] or for safety functions, an FOB_RTG1 [OB123]. |  |
| Process image | Select the process image partition that you want to use in the drop-down list in order to transfer the data consistently, e.g. OB1-PI. For information on process images, please enter the term in the online help search. |  |
| Interrupt OB number | Use the interrupt OB to output diagnostic information. |  |
| F-watchdog time | Monitoring time in the fail-safe DP standard slave / IO standard device / PA field device.  A valid, current safety telegram must arrive from the F-CPU within the monitoring time. This ensures that failures and errors are detected and the appropriate reactions triggered to keep the F system in a safe state or to transfer it to a safe state.  Activate the "Manual assignment of the F-I/O DB number" option if you want to enter the monitoring time manually. |  |
| F-I/O DB number | The number of the block that controls the F-I/O. |  |
| F-I/O DB name | The name of the block that controls the F-I/O. |  |

### Editing telegrams

#### Overview

You can edit telegrams in the following way:

- Extending standard or Siemens telegrams
- Adding telegrams

#### Requirement

- In the project a drive and a partner have been created and connected via a fieldbus. The drive has been selected and the parameterization editor is open.

#### Extending telegrams

> **Note**
>
> **Extension not possible**
>
> The following telegram types cannot be extended:
>
> - Free telegrams 999
>
>   However, the length of these telegrams can be changed.
> - Safety Integrated telegrams:
>
>   - PROFIsafe telegrams 30, 31
>   - Siemens telegrams 901, 902, 903
>
> If a selected telegram cannot be extended, then the field "Extension" is grayed out.

Send and receive telegrams can be extended in the same way. A send telegram is extended in the send direction and a receive telegram is extended in the receive direction. You can set the extension either in the table "Telegram configuration" or in the telegram detail screen form.

To extend a telegram, proceed as follows:

1. Use the secondary navigation of the Inspector window to open the "Telegram configuration" screen form.

   - PROFIBUS menu: "Properties > Telegram configuration"
   - PROFINET menu: "Properties > PROFINET interface > Telegram configuration"

   Telegrams that you have created are displayed for each existing drive object in the "Telegram configuration " screen form.
2. In the table "Telegram configuration", select the required telegram. In the field "Extension", enter the number of words by which you wish to extend the telegram.

   - Or -

   In the secondary navigation under "Telegram configuration", select the required telegram. The parameterizing screen form of the telegram is displayed on the right. In the field "Extension", enter the number of words by which you wish to extend the telegram.
3. Click in another field to accept the input.

   The telegram is extended by the entered number of words.
4. You can display additional telegram details in a communication screen form. Click the ![Extending telegrams](images/156370766219_DV_resource.Stream@PNG-de-DE.png) icon to open the screen form.

   Generally, you can interconnect additional signals in this communication screen form (not for S210 drives; see "AUTOHOTSPOT").
5. Save the project.

#### Adding telegrams

You can add the following telegrams once as long as they are not yet included in the telegram list of the drive object:

- Safety Integrated telegram

  only for "Drive axis" drive object
- Supplementary telegram

  only for "Drive axis" drive object
- Torque telegram

  only for "Drive axis" drive object
- Actual value
- Setpoint

To add a telegram, proceed as follows:

1. Use the secondary navigation of the Inspector window to open the "Telegram configuration" screen form.

   - PROFIBUS menu: "Properties > Telegram configuration".
   - PROFINET menu: "Properties > PROFINET interface > Telegram configuration"
2. Click the "Add telegram" entry (at the required drive object).

   A drop-down list opens. All telegram types that have not been assigned yet can be used.
3. Select the required telegram type.

   The entries for the telegram are created.
4. If required, change the telegram type now, e.g. from telegram 30 to telegram 900. An actual value slot or a setpoint slot are created for the additional data with a "Free telegram".
5. Save the project.

#### Result

The telegram has been extended by the entered number of words or a new telegram has been added.

### Sorting telegrams (CU3x0-2 only)

#### Description

In the telegram configuration, the created telegrams are assigned to the respective drive objects. There are telegrams for drive control, the infeed, the created drive axes, and for the input and output objects used. When a drive is created in the project, the sort sequence of the telegrams is taken over from the project tree:

- Drive control
- Infeed
- Drive axis x
- Input/output object x

![Example: Standard telegram sorting](images/134987266187_DV_resource.Stream@PNG-en-US.PNG)

Example: Standard telegram sorting

You can change this specified sorting in the telegram configuration (Inspector window).

#### Requirement

- A Control Unit (CU3x0-2) with all required drive objects (infeed, Motor Module...) is created in the project.

#### Procedure

1. Use the secondary navigation of the Inspector window to open the "Telegram configuration" screen form.

   - PROFIBUS menu: "Properties > Telegram configuration"
   - PROFINET menu: "Properties > PROFINET interface > Telegram configuration"

   The telegrams that have been created are displayed for each existing drive object in the "Telegram configuration" screen form.
2. Right-click on the drive object to be moved in the telegram list.
3. Select the "Up" shortcut menu to move the telegrams of this drive object upwards by one step in the telegram list.

   - Or -

   Select the "Down" shortcut menu to move the telegrams of this drive object down one step in the telegram list.
4. Repeat step 3 for each step you want to move the telegrams of the drive object in the telegram list.
5. Save the project.

#### Result

The telegrams of the drive object are resorted in the telegram list. The secondary navigation located in the "Telegram configuration" menu of the Inspector window takes over this new sort sequence.

![Example: Modified telegram sorting](images/134989591563_DV_resource.Stream@PNG-en-US.PNG)

Example: Modified telegram sorting

### Structure of the telegrams, control and status words

#### Structure of the telegrams

The selection of a telegram determines the process data of the drive unit (Control Unit) that is transferred.  
From the drive unit view, the received process data represents the receive words and the process data to be sent represents the send words.

The receive and send words consist of the following elements:

- Receive words: Control words or setpoints
- Send words: Status words or actual values

To maintain the PROFIdrive profile, the following must apply:

- Interconnect PZD receive word 1 as control word 1 (STW1).
- Interconnect PZD send word 1 as status word 1 (ZSW1). (The WORD format must be used for PZD1)

One PZD (process data item) corresponds to one word.

The signals of the control and status words are connected via BICO to the corresponding signals of the drive.

### PROFIdrive overview

#### The PROFIdrive profile

The PROFIdrive profile defines the device behavior and the access procedure to drive data for electrical drives on PROFIBUS and on PROFINET, from simple frequency converters up to high-performance servo controllers.

PROFIdrive is divided into a general part and a bus-specific part. The following properties are defined in the general part:

- Base model
- Parameter model
- Application model

The following assignments are made in the bus-specific part:

- PROFIdrive to PROFIBUS
- PROFIdrive to PROFINET

Details of where to find a precise description of the PROFIdrive profile are given below.

#### Reference note

PROFIdrive profile

PROFIBUS Profile PROFIdrive – Profile Drive Technology  
Version V4.1, May 2006,  
PI Support Center/PROFIBUS User Organization e. V.  
Haid-und-Neu-Strasse 7, 76131 Karlsruhe (Germany)  
[https://www.profibus.com/](https://www.profibus.com)  
Order number 3.172, specifically Chap. 6

Standards

IEC 61800 standard

#### PROFIdrive base/parameter model

The PROFIdrive base model describes an automation system as a number of devices and their relationships to each other (applications interfaces, parameter access). A distinction is made between the following device classes in the base model:

| PROFIdrive | PROFIBUS DP | PROFINET IO |
| --- | --- | --- |
| Controller (higher-level controller or host of the automation system) | DP master class 1 | IO controller |
| Peripheral device (P-device) | DP slave (I-slave) | IO device |
| Supervisor (engineering station) | DP master class 2 | IO supervisor |
| PROFIdrive device classes |  |  |

#### Communications services

Two communications services are defined in the PROFIdrive profile, the cyclic data exchange and the acyclic data exchange.

- Cyclic data exchange via the cyclic data channel

  Motion control systems require cyclically updated data during operation for open-loop and closed-loop control. This must be sent as setpoints to the drive units or received as actual values from the drive units via the communication system. The transfer of this data is normally time-critical.
- Acyclic data exchange via the acyclic data channel

  In addition to the cyclic data exchange, there is an acyclic parameter channel for the exchange of parameters between the controller/supervisor and the drive units. Access to this data is not time-critical.
- Alarm channel

  The alarms are issued event-driven and show the coming and going of error states.

## Interface parameters

This section contains information on the following topics:

- [HW identifier](#hw-identifier)
- [Module parameter](#module-parameter)
- [Diagnostics channels](#diagnostics-channels)

### HW identifier

#### Requirement

- The drive is assigned to a PLC.

#### Description

Each hardware object, e.g. a module, an interface or a module port, or even transfer areas of I-devices, has a HW identifier that is assigned automatically when a hardware component is configured. For drives, the HW identifier is assigned when you use the drive as I-slave or IO device.

These HW identifiers have the same function as the diagnostic addresses of HW components and are displayed in the Inspector window in the "General" tab of the drive.

You require the HW identifiers for the programming of drive blocks. Additional information on HW identifiers can be found in the TIA Portal online help at "Useful information on HW identifiers".

![HW identifier](images/72207051403_DV_resource.Stream@PNG-en-US.png)

HW identifier

A detailed description of the HW identifier can be found in the online help of the TIA Portal.

#### Display in the system constants of the controller

For better visualization, the HW identifiers are displayed together with the names and interfaces in the system constants of the controller.

![HW identifier in the system constants](images/72207143307_DV_resource.Stream@PNG-en-US.png)

HW identifier in the system constants

### Module parameter

The messages from SINAMICS drives cannot be displayed via Startdrive / TIA Portal. After activation of the diagnostic function, the messages are transferred to the higher-level controller via the standardized PROFIdrive error classes. The messages are evaluated there or passed on to the appropriate user interfaces for user friendly display. In this way, problems or faults can be located immediately and directly corrected irrespective of the tool being used.

For further information, see [Diagnostics channels](#diagnostics-channels).

#### Procedure

To activate the channel diagnostics, proceed as follows:

1. Open the "Activate channel diagnostics" drop-down list.
2. Select "PROFIdrive standard diagnostics" from the drop-down list.

You must then program the access to the diagnostic messages in your application.

### Diagnostics channels

SINAMICS drives provide the standard diagnostics for PROFIBUS and PROFINET. This allows the PROFIdrive classes of the SINAMICS drive to be integrated into the system diagnostics of a higher-level controller and automatically displayed on an HMI.

The information transferred is saved for the drive objects in the following parameters:

| Symbol | Meaning |
| --- | --- |
| r0947[0...63] | Fault number |
| r2122[0...63] | Alarm code |
| r9747[0...63] | SI message code (with safety messages) |
| r3120[0..63] | Component fault |
| r3121[0..63] | Component alarm |
| r9745[0..63] | SI component (with safety message) |

The messages entered in these parameters are combined to create PROFIdrive message classes for diagnostics. Determining the source of a message is realized by transferring the component number as channel number.

The channel diagnostics are activated at "[Module parameters](#module-parameter)".

The functional scope of the diagnostic channels depends on the bus system.

|  |  | PROFIdrive message classes |  |  |
| --- | --- | --- | --- | --- |
| Faults | Alarms | Component assignment |  |  |
| PN | GSDML | X | X | X |
| TIA | X | X | X |  |
| DP | GSD | X | ‑ | ‑ |
| TIA | X | ‑ | ‑ |  |

- SINAMICS transfers the messages in the sequence in which they occurred.
- The time stamps are generated from the higher-level controller when the messages are received
- Alarms or faults are acknowledged using the already known acknowledgment routes.

> **Note**
>
> **Additional information**
>
> The PROFIdrive message classes of the individual SINAMICS faults and alarms can be found in the SINAMICS Function Manuals and List Manuals. For a description of the bus-specific diagnostic data for channel diagnostics, refer to the help page "Explanation of fault and warning information".

#### Additional parameters

Pxxxx

## Linking drives via GSD

This section contains information on the following topics:

- [Overview](#overview)
- [Configuring GSD drives for PROFIBUS DP](#configuring-gsd-drives-for-profibus-dp)
- [Configuring GSD/GSDML drives for PROFINET IO](#configuring-gsdgsdml-drives-for-profinet-io)

### Overview

#### Description

SINAMICS drives which are not included in the "SINAMICS Startdrive" option package and drives from third-party suppliers can be integrated in the TIA Portal via device master files and controlled via the SIMATIC S7-1500 user program. Device master files are divided into so-called GSD or GSDML files. The integration and use of these GSD or GSDML files can be found in the following online help pages:

[Configuring GSD drives for PROFIBUS DP](#configuring-gsd-drives-for-profibus-dp)

[Configuring GSD/GSDML drives for PROFINET IO](#configuring-gsdgsdml-drives-for-profinet-io)

> **Note**
>
> The term "GSD file" is used for PROFIBUS and "GSDML file" is used for PROFINET. Further on in the online help, the term "GSD file" is used synonymously for both terms.

### Configuring GSD drives for PROFIBUS DP

#### Overview

The higher-level controller serves as DP master. The drives are then operated as DP slaves on the DP master system. Configure the drive in the "Network view" and the "Device view". You will find the required GSD drives in the catalog:

![GSD devices](images/157528821515_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The field devices that are integrated in the TIA Portal via a GSD file are entered here. |
| ② | Devices for the PROFINET I/O fieldbus which are integrated via GSDML files. |
| ③ | Devices for the PROFIBUS DP fieldbus which are integrated via GSD files. |

GSD devices

#### Inserting a drive and assigning it to a controller

To insert a drive and assign it to a controller, proceed as follows:

1. Insert a higher-level controller, e.g. a SIMATIC S71500.
2. Change to the "Network view".
3. Select the GSD drive in the hardware catalog.
4. Drag the drive to the "Network view".
5. Drag a DP master system from the DP interface of the controller to the DP interface of the drive.

   The DP master system is created and the drive assigned to the controller.

   ![Example S120: Controller with drive on the DP master system](images/157528533003_DV_resource.Stream@PNG-en-US.PNG)

   ![Example S120: Controller with drive on the DP master system](images/157528533003_DV_resource.Stream@PNG-en-US.PNG)

   Example S120: Controller with drive on the DP master system

#### Configuring telegrams for the communication

The cyclic communication between the controller (DP master) and the drive (DP slave) is performed with PROFIdrive telegrams. Different telegrams are available, depending on the task.

To insert a telegram, proceed as follows:

1. Double-click the drive in the "Network view".

   The "Device view" opens and shows the drive. The hardware catalog shows the telegrams available for this drive.
2. Select a telegram and drag it to the "Device overview". The possible positions are indicated by blue lines.

   The telegram is inserted in the "Device overview".

   ![Example S120: Inserting a PROFIdrive telegram](images/43852638219_DV_resource.Stream@PNG-en-US.png)

   ![Example S120: Inserting a PROFIdrive telegram](images/43852638219_DV_resource.Stream@PNG-en-US.png)

   Example S120: Inserting a PROFIdrive telegram

   The I/O addresses are assigned automatically.
3. If required, adapt the I/O addresses for the motion control applications.

   You have then inserted a telegram for the communication between controller and drive.

#### Insert telegrams for controller with several axes

If you have a drive with which several axes can be operated on the controller, you must insert a telegram for each axis.

To configure a controller with several axes, proceed as follows:

1. First insert an axis delimiter in the "Device overview" of the drive for the second axis.
2. Then drag a further telegram to the "Device overview".

   ![Axis delimiter for several telegrams](images/43852647051_DV_resource.Stream@PNG-en-US.png)

   ![Axis delimiter for several telegrams](images/43852647051_DV_resource.Stream@PNG-en-US.png)

   Axis delimiter for several telegrams

   A separate telegram is now used for each drive axis.

### Configuring GSD/GSDML drives for PROFINET IO

#### Overview

The higher-level controller functions as the IO controller. The drives are then inserted as IO device in the SyngDomain of the PROFINET IO system. Configure the drive in the "Network view" and the "Device view".

#### Inserting a drive and assigning it to a controller

To insert a drive and assign it to a controller, proceed as follows:

1. Insert a higher-level controller, e.g. a SIMATIC S7-1500.
2. Change to the "Network view".
3. Select the GSD drive in the hardware catalog.
4. Drag the drive to the "Network view".
5. Drag a connection from the PN IO interface of the controller to the PN IO interface of the drive. The PROFINET IO system is created and the drive assigned to the controller.

   ![Example S120: Inserting a drive as IO device](images/43855882763_DV_resource.Stream@PNG-de-DE.png)

   ![Example S120: Inserting a drive as IO device](images/43855882763_DV_resource.Stream@PNG-de-DE.png)

   Example S120: Inserting a drive as IO device

#### Configuring a telegram for the communication

The cyclic communication between the controller (IO controller) and the drive (IO device) is performed with PROFIdrive telegrams. Different telegrams are available, depending on the task. For SINAMICS drives that comprise several drive objects (DO, Drive Object) (multi-axis drives), such as a SINAMICS S120 CU320-2, first insert the drive object with which the controller is to communicate, e.g. a "DO servo". Then insert a telegram for each DO. For drives that only have one drive object (single-axis drives), drag the telegram to the "Device view" as for PROFIBUS DP.

To insert a telegram, proceed as follows:

1. Double-click the drive in the "Network view".

   The "Device view" opens and shows the drive. The hardware catalog shows the telegrams available for this drive.
2. Select the drive object and drag it to the "Device overview".
3. Select the telegram and drag it to the "Device overview". The possible positions are indicated by blue lines. The telegram is inserted in the "Device overview".

   ![Example S120: Inserting a telegram for PROFINET IO](images/43856262795_DV_resource.Stream@PNG-en-US.png)

   ![Example S120: Inserting a telegram for PROFINET IO](images/43856262795_DV_resource.Stream@PNG-en-US.png)

   Example S120: Inserting a telegram for PROFINET IO

   The I/O addresses are assigned automatically.
4. If required, adapt the I/O addresses for the motion control applications.

You have then inserted a telegram for the communication via PROFINET IO between controller and drive.

**Controller with several axes**

If you operate several axes on the controller, you must insert a telegram for each axis.

1. First insert an axis delimiter in the "Device overview" of the drive for the second axis.
2. Then drag a further telegram to the "Device overview".

#### Drives with several drive objects

If you want to operate several axes or want to access the signals of other drive objects, you must create a telegram for each DO. Read the relevant descriptions to see which telegrams are possible.

To configure a drive with several drive objects, proceed as follows:

1. Insert a further DO in the "Device overview" of the drive.
2. Then drag a further telegram to the "Device overview".
3. Then insert a telegram for each DO that you want to control.

   ![Example S120: Inserting telegrams for several DOs](images/43857654027_DV_resource.Stream@PNG-en-US.png)

   ![Example S120: Inserting telegrams for several DOs](images/43857654027_DV_resource.Stream@PNG-en-US.png)

   Example S120: Inserting telegrams for several DOs

#### Connecting the PROFINET cable to the Control Unit

You can use the converter to either communicate via Ethernet or to integrate the converter into a PROFINET network.

- The converter as an Ethernet node

  ![Example: Profinet with controller, devices and supervisor](images/156370775051_DV_resource.Stream@PNG-de-DE.png)

  Example: Profinet with controller, devices and supervisor
- PROFINET IO mode

  ![Example G120: Converter with Profinet interface on Ethernet](images/156371624075_DV_resource.Stream@PNG-de-DE.png)

  Example G120: Converter with Profinet interface on Ethernet

The converter supports the following functions in PROFINET IO mode:

- RT
- IRT  
  The converter passes on the isochronous mode, but does not support the isochronous mode.
- MRP  
  Media redundancy, with 200 ms latency  
  Requirement: Ring topology
- MRP  
  Media redundancy, without latency  
  Requirement: IRT and a ring topology created in the controller
- Diagnostic interrupts  
  corresponding to the error classes defined in the PROFIdrive profile
- Device replacement without exchangeable medium  
  Requirement: topology created in the controller
- Shared device  
  only for Control Units with fail-safe functions
