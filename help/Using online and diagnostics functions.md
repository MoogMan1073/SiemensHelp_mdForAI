---
title: "Using online and diagnostics functions"
package: PEOnline2MenUS
topics: 35
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using online and diagnostics functions

This section contains information on the following topics:

- [Displaying accessible devices](#displaying-accessible-devices)
- [Changing the device configuration online](#changing-the-device-configuration-online)
- [Connecting devices online](#connecting-devices-online)
- [Creating a backup of an S7 CPU](Creating%20a%20backup%20of%20an%20S7%20CPU.md#creating-a-backup-of-an-s7-cpu)
- [Configuring the PG/PC interface](#configuring-the-pgpc-interface)
- [Using the trace and logic analyzer function](Using%20the%20trace%20and%20logic%20analyzer%20function.md#using-the-trace-and-logic-analyzer-function)
- [Establishing a remote connection with TeleService](Establishing%20a%20remote%20connection%20with%20TeleService.md#establishing-a-remote-connection-with-teleservice)
- [Simulating devices with S7-PLCSIM](#simulating-devices-with-s7-plcsim)

## Displaying accessible devices

Accessible devices are all devices connected to an interface of the programming device / PC that are turned on. Devices that allow only restricted configuration using the currently installed products or that cannot be configured at all can also be displayed.

To speed up the display in large networks with many network devices, the PROFINET device names are displayed in a slightly adapted form for PROFINET devices. Unicode-specific characters in the PROFINET device name are converted into ASCII-compatible characters using the Punycode method (according to RFC 3492).

### Displaying accessible devices in the project tree

To display accessible devices at an interface of the programming device / PC, follow these steps:

1. Open the "Online access" folder in the project tree.
2. Click on the arrow to the left of the interface to show all the objects arranged below the interface.
3. Double-click "Update accessible devices" below the interface.

   You can see the progress of the search in the status bar. If you have found the desired device before the search is completed, you can cancel the search. To do this, click on the cross to the right of the progress bar.

   The network stations that have been found through the search are displayed below the interface.
4. Optional: Select the interface in the project tree. Then open the overview window in the detail view to display more details for the respective devices. More details include, for example, the device type, the MAC address or the configured device name.

   The detailed display of the devices in the overview window can take some time in networks with many devices because each individual device must submit the details.

### Displaying accessible devices in a table

To display accessible devices in an easy to read table outside the project tree, follow these steps:

1. Select the "Accessible devices" command in the "Online" menu.

   The "Accessible devices" dialog is displayed.
2. Select the type of interface from the "Type of the PG/PC interface" drop-down list.
3. Select the required interface of the programming device / PC from the "PG/PC interface" drop-down list.
4. Click the "Start Search" button.

   The accessible devices at the selected interface of the programming device/PC are displayed in the table. The connection line between PG/PC and the network is closed and displayed in green in the graphic. If no devices are accessible at an interface, the connection line is displayed as a dashed line.
5. To go to a device in the project tree, select the device from the list of accessible devices and click the "Show" button.

   The selected device is highlighted in the project tree.

### Displaying additional information about the devices in the project tree

To display additional information on the individual accessible devices in the project tree, follow these steps:

1. Click on the arrow to the left of one of the accessible devices in the project tree.

   All data available online, for example blocks and system data, is displayed for known devices. If additional editing options are available for a device with the shortcut menu, the device is shown in black text. You have only read access to the objects with a gray background, such as blocks.

### Display additional information about the devices in the detailed view

Follow these steps to display additional information about the devices in the detailed view of the overview window:

1. Double-click the entry "Update accessible devices" in the "Online access" folder in the node of the network card.

   All the devices accessible in the network are listed below the interface.
2. Double-click the entry "Display more information".

   More information is displayed in the detailed view of the overview window.

---

**See also**

[Changing the device configuration online](#changing-the-device-configuration-online)
  
[Default setting online connection data](#default-setting-online-connection-data)
  
[Overview window](Introduction%20to%20the%20TIA%20Portal.md#overview-window-1)

## Changing the device configuration online

You can assign parameters to some devices, preferably in small hardware setups, directly online. You do not need to create a project or have offline data to do this. In this way, you can quickly and easily change the device configuration. You do not need to compile the hardware configuration or perform a download. Depending on the device, either all changes become active immediately or they are written to the device only after confirmation.

### Requirement

- The device must support online parameter assignment. You can learn whether or not your specific devices support this function in the device manual.
- The device must be connected to the PG/PC and available in the list of accessible devices.

### Procedure

To change the device configuration online, follow these steps:

1. Show the accessible devices on the interface via which the device is connected. To learn how to show the accessible devices, see the chapter "[Showing accessible devices](#displaying-accessible-devices)".
2. Expand the device to display the lower-level elements.
3. Double-click the "Parametrize device" item.

   A configuration page for the device opens in the work area.
4. Make all required settings.

   With some devices, the new settings take effect immediately.
5. Optionally, depending on the device: Click on the "Upload to device" button.

   The settings are transferred to the device.

## Connecting devices online

This section contains information on the following topics:

- [General information about online mode](#general-information-about-online-mode)
- [View in online mode](#view-in-online-mode)
- [Default setting online connection data](#default-setting-online-connection-data)
- [Establishing or changing an online connection](#establishing-or-changing-an-online-connection)
- [Canceling an online connection](#canceling-an-online-connection)
- [Connecting online with several devices](#connecting-online-with-several-devices)
- [Disconnecting online connections of multiple devices](#disconnecting-online-connections-of-multiple-devices)

### General information about online mode

#### Online mode

In online mode, there is an online connection between your programming device / PC and one or more devices.

An online connection between the programming device/PC and the device is required, for example, for the following tasks:

- Testing user programs
- Displaying and changing the operating mode of the CPU
- Displaying and setting the date and time of day of the CPU
- Displaying module information
- Comparing blocks
- Hardware diagnostics

Before you can establish an online connection, the programming device/PC and the device must be physically or remotely connected. As an alternative, some devices support a simulation mode. In this case, a connection to the device is simulated via the PLCSIM virtual interface.

After establishing a connection, you can use the Online and Diagnostics view or the "Online tools" task card to access the data on the device. The current online status of a device is indicated by an icon to the right of the device in the project tree. You will find the meaning of the individual status icons in the relevant tooltip.

> **Note**
>
> Some online functions depend on the scope of the installed software or whether a project is open.

#### Standby or hibernation of the programming device / PC

If the programming device / PC is changed to the standby or hibernation mode when there is an online connection, all online connections are terminated. When the programming device / PC wakes up from hibernation, the online connections are not automatically re-established.

Note that suddenly terminating an online connection can lead to loss of data or a connected device may interrupt program execution.

#### Performing an LED flash test

In many online dialogs you can perform an LED flash test, if the device connected online supports this feature. If you select the "Flash LED" check box, an LED flashes on the currently selected device. This feature is useful, for example, when you are not sure which device in the hardware configuration corresponds to the station currently selected in the software.

Read any additional information and learn about the possible limitations to the LED flash test in the respective device documentation.

---

**See also**

[View in online mode](#view-in-online-mode)
  
[Overview of the online and diagnostic settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-online-and-diagnostic-settings)

### View in online mode

#### Online displays

After the online connection has been established successfully, the user interface changes. If a device is unavailable, this is indicated by a symbol. The following figure shows a device connected online and the corresponding user interface:

![Online displays](images/90328129803_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The title bar of the active window gets an orange background as soon as at least one of the devices currently displayed in the editor has been successfully connected online. If one or more devices are unavailable, a symbol for a broken connection appears in the title bar of the editor. |
| ② | The title bars of inactive windows for the relevant station now have an orange line below them. |
| ③ | An orange, pulsing bar appears at the right-hand edge of the status bar. If the connection has been established but is functioning incorrectly, an icon for an interrupted connection is displayed instead of the bar. You will find more information on the error in "Diagnostics" in the Inspector window. In addition, the status line indicates if there is an online connection to the SIMATIC hardware via the TIA Portal Cloud Connector. |
| ④ | The left column in the project tree indicates the diagnostics status for hardware objects in online mode through symbols. |
| ⑤ | The right column in the project tree indicates the comparison status for software objects in online mode through symbols. A comparison of the online and offline state is performed automatically. Differences between online and offline objects are displayed in the form of symbols. |
| ⑥ | The "Diagnostics > Device information" area is brought to the foreground in the Inspector window. |

#### Online connection abort

The online mode and its display are retained as long as at least one device is connected online. If the online connection of one or more devices breaks, the TIA Portal remains in online mode. The display of the TIA Portal changes to offline mode only when there is no longer an online connection for any device.

#### Online connection via the TIA Portal Cloud Connector

If you use the TIA Portal in a virtual environment, you have the opportunity to create an online connection via the TIA Portal Cloud Connector to SIMATIC hardware that is connected to a user device. If the online connection is made via the TIA Portal Cloud Connector, the following symbol is displayed in the status bar:

![Online connection via the TIA Portal Cloud Connector](images/85416131339_DV_resource.Stream@PNG-de-DE.png)

You can find instructions on how to use the TIA Portal in a virtual environment (private cloud) on the installation disk in the directory "Documents\Readme\<language directory>". You can open the PDF document "TIAPortalCloudConnectorHowTo<Sprachkennung>.pdf" here.

---

**See also**

[General information about online mode](#general-information-about-online-mode)
  
[Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)

### Default setting online connection data

If you prefer to use a specific network interface of your programming device/PC to establish an online connection, you can preset this interface. The specified connection path is then already selected in the dialogs for online connection.

#### Procedure

To specify a default connection path, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The settings of the TIA Portal are opened.
2. Select the "Online & Diagnostics" entry in the area navigation.
3. In the "Preset connection path for online access" area, specify the type of the PG/PC interface as well as the interface itself.
4. Enable or disable the check box "Display dialog for setting the default connection path for online access".

   - If you select the check box, a dialog is displayed when establishing an online connection. In this dialog, you can select whether a new connection path should be preset.
   - If you clear the check box, the dialog is not displayed when establishing an online connection.

---

**See also**

[Establishing or changing an online connection](#establishing-or-changing-an-online-connection)
  
[Displaying accessible devices](#displaying-accessible-devices)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Online access](#online-access)
  
[Overview of the online and diagnostic settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-online-and-diagnostic-settings)

### Establishing or changing an online connection

To use the online functions of a device, specify the connection path the first time you establish the connection.

#### Requirement

At least one PG/PC interface is installed and is physically connected to a device, for example, with an Ethernet cable. As an alternative, it is also possible to establish virtual online connections using PLCSIM.

#### Procedure

To establish or change an online connection, follow these steps:

1. Select one or more devices for the online connection in the project tree.
2. Select the "Go online" command in the "Online" menu.

   - If the device has already been connected online, the online connection is automatically established using the previously specified connection path.
   - If there was no previous connection or if the device address is not located in the same subnet of the programming device/PC, the "Go online" dialog opens.

   If you want to change a specified connection path, select the "Extended go online" command instead in the "Online" menu. The "Go online" dialog box is opened again in this case.
3. Select the connection path:

   - Select the type of interface from the "Type of the PG/PC interface" drop-down list.
   - Select the interface of your programming device/PC from the "PG/PC interface" drop-down list.

     No selection is necessary if you have already defined a programming device/PC interface in the settings.
   - Select the interface or the subnet for the connection from the "Connection to interface/subnet" drop-down list. Select a direct connection if no S7 gateway is connected in between. Select the matching subnet for the connection to the programming device or PC if the device can be accessed via an S7 gateway. Select the item "Try all interfaces" if the device has several interfaces and you do not know by which of the interfaces the device is connected to the programming device/PC.

     If you selected an MPI or PROFIBUS subnet, the bus parameters configured in the programming device/PC interface are applied at this point.
   - If the device is accessible via a gateway, select the gateway that connects the two subnets involved in the "1st gateway" drop-down list.
4. Optional: If no devices can be accessed by the selected connection path, a dashed connecting line is displayed between the programming device/PC and the device. This is the case, for example, when the device is connected with the network by a NAT router.

   To display all devices that are switched on and connected to an interface of the programming device/PC, select the entry "Show accessible devices" from the drop-down list and click "Start search" again.
5. Optional: You have two options to access the device despite a different subnet: Use the two options in administered networks only after consultation with the administrator.

   - Assign a static address to the programming device/PC interface under Windows.
   - During the creation of the online connection, an additional IP address in the same subnet as the device is temporarily assigned to the interface of the programming device/PC. Click "Go online" and confirm the next prompt.
6. Click the "Start search" button.

   Devices which can be reached by the set connection path are displayed in the table of the target devices. The connection line in the graphic on the left is displayed as solid.
7. Optional: Run a flash test. Select the "Flash LED" check box on the left in the graphic. You use the flash test to check that you have selected the correct device. The flash test is not supported by all devices.
8. Select the target device in the table and confirm the selection with "Go online".

   The online connection to the selected target device is established.

#### Result

After the online connection has been established, the title bars of the editors change to orange. An orange progress bar is also shown in the title bar of an editor and in the status bar. In the project tree, status symbols show the difference between online and offline objects.

The set connection path is stored for future connection attempts.

With automatic assignment of the programming device/PC address the dialog reappears when the computer is restarted. The connection must be re-established in this case.

> **Note**
>
> **Undoing actions**
>
> You cannot undo actions once you have established an online connection.

> **Note**
>
> **Using direct connections or subnets**
>
> An online connection between programming device/PC and connected devices is possible either via direct connection or via subnet.
>
> Simultaneous connection of the devices over different subnets is not possible if these are physically connected through the same interface. Simultaneous connections to different subnets are only possible through routed connections.
>
> Simultaneous connection of devices through a subnet and through direct connections using the same interface is not possible.

---

**See also**

[Overview of the online and diagnostic settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-online-and-diagnostic-settings)
  
[Default setting online connection data](#default-setting-online-connection-data)
  
[Online connections for special diagnostics and firmware loader (S7-300, S7-400)](Using%20additional%20diagnostics%20options%20%28S7-300%2C%20S7-400%29.md#online-connections-for-special-diagnostics-and-firmware-loader-s7-300-s7-400)
  
[Canceling an online connection](#canceling-an-online-connection)
  
[Connecting online with several devices](#connecting-online-with-several-devices)
  
[View in online mode](#view-in-online-mode)
  
[Utilization of temporary IP addresses](#utilization-of-temporary-ip-addresses)
  
[Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights)

### Canceling an online connection

#### Procedure

To terminate the existing online connection, follow these steps:

1. Select the device for which you want to disconnect the online connection in the project tree.
2. Select the "Go offline" command in the "Online" menu.

   The online connection is disconnected.

> **Note**
>
> **Undoing actions**
>
> You cannot undo actions once you have disconnected an online connection.

---

**See also**

[Establishing or changing an online connection](#establishing-or-changing-an-online-connection)

### Connecting online with several devices

You can establish an online connection to several devices at the same time without needing to select individual devices previously in the network view.

#### Requirement

- No device must be selected
- At least one PG/PC interface is installed and is physically connected to a device, for example with an Ethernet cable. As an alternative, it is also possible to establish a virtual online connection using PLCSIM or a remote connection.

#### Procedure

To establish an online connection to several devices at the same time, follow these steps:

1. Select the project in the project tree.
2. Select the "Go online" command in the "Online" menu.

   The "Select device for opening the online connection" dialog opens with a table of all available devices.
3. Select the devices to which you want to establish an online connection in the "Go online" column.
4. Click the "Go online" button.

#### Result

Without any further prompt for confirmation, a connection is established to all selected devices if a connection was already established to the selected devices at least once. If there was no previous online connection, the "Go online" dialog opens. In this case, first configure the online connection as described in the section "[Go online and Go offline](#establishing-or-changing-an-online-connection)".

---

**See also**

[Establishing or changing an online connection](#establishing-or-changing-an-online-connection)
  
[Utilization of temporary IP addresses](#utilization-of-temporary-ip-addresses)

### Disconnecting online connections of multiple devices

You can disconnect the online connections to multiple devices at one time without needing to select individual devices beforehand in the network view.

#### Requirement

- No device is selected.
- There is currently an online connection to at least one device.

#### Procedure

To terminate the online connections to multiple devices at one time, follow these steps:

1. Select the "Go offline" command in the "Online" menu.

   The "Select devices" dialog opens with a table of all available devices.
2. Select the device for which you want to terminate the online connection in the "Go offline" column.
3. Click the "Go offline" button.

#### Result

The online connection to the all the selected devices is terminated.

## Configuring the PG/PC interface

This section contains information on the following topics:

- [Online access](#online-access)
- [Basics of assigning parameters for the PG/PC interface](#basics-of-assigning-parameters-for-the-pgpc-interface)
- [Showing or hiding interfaces](#showing-or-hiding-interfaces)
- [Displaying and modifying interface properties](#displaying-and-modifying-interface-properties)
- [Adding interfaces](#adding-interfaces)
- [Setting parameters for the Ethernet interface](#setting-parameters-for-the-ethernet-interface)
- [Setting parameters for the MPI and PROFIBUS interfaces](#setting-parameters-for-the-mpi-and-profibus-interfaces)

### Online access

#### Online access of the project

In the "Online access" folder of the project tree, you will find all active interfaces of your programming device/PC. Each interface icon provides you with information on the status. You can also display the accessible devices and display and edit the properties of an interface using the shortcut menu.

The following figure shows the "Online access" folder in the project tree:

![Online access of the project](images/102524522763_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | "Online access" folder in the project tree  All interfaces installed in the programming device/PC are displayed in the "Online access" folder. |
| ② | Show/hide interfaces  Use the function "Show/hide interfaces" to show or hide individual interfaces. |
| ③ | Status display for the interfaces  The current status of an interface is indicated by an icon to the right of the name. You can see the meaning of the icon in the tooltip. |
| ④ | Updating the list of accessible devices.  This function is available for each hardware interface of the programming device/PC. Software interfaces, such as a remote connection, do not offer this function. |
| ⑤ | Display more information  This function is available for each hardware interface of the programming device/PC after you have executed the function "Update accessible devices". You can find additional information in the detailed view of the overview window. |
| ⑥ | Devices connected via the respective interface with the programming device/PC  The type of the device and its status are displayed by the preceding icon. |

#### Displaying or updating accessible devices

You have the following options if you want to display all devices accessible online on your programming device/PC:

- Display of the accessible devices on a single interface of the programming device / PC in the project tree. In the project tree, you can also display additional information about the individual accessible devices.
- Display of the accessible devices of all interfaces in a list.

See also:[Displaying accessible devices](#displaying-accessible-devices)

#### Overview of icons for accessible devices

The accessible devices are identified with an icon according to their type and status. The following is an overview of all icons and their meaning.

| Symbol | Meaning |
| --- | --- |
| ![Overview of icons for accessible devices](images/30576997259_DV_resource.Stream@PNG-de-DE.png) | Icon for unidentified modules  This icon is displayed whenever the identification of a module is not yet complete or when the identification of a module was not successful, for example, because the required online data could not be read. |
| ![Overview of icons for accessible devices](images/30577005963_DV_resource.Stream@PNG-de-DE.png) | Icon for the following device types:  - PLCs - SIMOCODE pro devices - IE/PB links - CPs of PC systems - SCALANCE head modules - S7-300 and S7-400 CPs - PROFINET IO devices and PROFINET CPs - SCALANCE modules and gateways that could not be identified |
| ![Overview of icons for accessible devices](images/30578409739_DV_resource.Stream@PNG-de-DE.png) | PROFINET IO devices, encoders, switchgear, sensors and identification systems that were replaced by similar devices because these could not be identified |
| ![Overview of icons for accessible devices](images/30578688139_DV_resource.Stream@PNG-de-DE.png) | Icon for the following device types:  - HMI devices - PROFINET IO devices of the HMI type if these could not be identified and were therefore replaced by a similar device |
| ![Overview of icons for accessible devices](images/30578696843_DV_resource.Stream@PNG-de-DE.png) | PROFINET IO devices of the drive type that could not be identified and were therefore replaced by a similar device |
| ![Overview of icons for accessible devices](images/30582685835_DV_resource.Stream@PNG-de-DE.png) | PROFINET IO devices of the type development kit and network components that could not be identified and were therefore replaced by a similar device |
| ![Overview of icons for accessible devices](images/30582758027_DV_resource.Stream@PNG-de-DE.png) | PROFINET IO devices of the type TeleService adapter that could not be identified and were therefore replaced by a similar device |

---

**See also**

[Displaying accessible devices](#displaying-accessible-devices)
  
[Displaying and modifying interface properties](#displaying-and-modifying-interface-properties)

### Basics of assigning parameters for the PG/PC interface

#### Options for connecting to target systems

If the devices of the project are connected via different subnets, you assign a suitable network access to each PG/PC interface to be able to establish online connections to the target systems. The following interfaces are automatically supported:

- MPI
- PROFIBUS
- Industrial Ethernet (ISO and TCP/IP)

You can make various settings for the interfaces. The following sections explain the parameter settings you can make.

> **Note**
>
> Note that changes to interface parameters have a direct influence on the operating system and the programming device / PC. Remember that some parameter settings can only be changed if you have adequate user rights.

---

**See also**

[Setting parameters for the Industrial Ethernet interface](#setting-parameters-for-the-industrial-ethernet-interface)
  
[Setting parameters for the MPI and PROFIBUS interfaces](#setting-parameters-for-the-mpi-and-profibus-interfaces-1)

### Showing or hiding interfaces

To improve clarity, it is possible to hide individual interfaces of the PG/PC in the project tree and to show them again when necessary.

#### Procedure

To show or hide individual interfaces, follow the steps below:

1. Open the "Online access" folder in the project tree.
2. Double click on the "Display/hide interfaces" icon.

   The "Display/hide interfaces" dialog opens.
3. Enable or disable the required interfaces in the "Display in the project tree" column.
4. Click the "Apply" button.

   The changes are applied. The view of the interfaces in the "Online access" folder is refreshed.

### Displaying and modifying interface properties

#### Introduction

For each interface, you can display and, in some cases, modify properties, for example the network type, address, and status.

#### Procedure

To open the properties, follow these steps:

1. Right-click on the required interface below "Online access" in the project tree.
2. Select the "Properties" command from the shortcut menu.

   A dialog containing the properties of the interface opens. On the left of the dialog, you will see the area navigation. You can view the current parameter settings in the individual entries in the area navigation and, if necessary, change them.

### Adding interfaces

You have the option of installing additional interfaces after installation of the TIA Portal.

#### Procedure

To install an interface at a later time and add it to the TIA Portal, follow these steps:

1. Install or update the drivers in the operating system once you have installed the interface hardware.
2. Close the TIA Portal if it is still open.
3. Open the Windows control panel.
4. Open the entry "Setting the PG/PC Interface" in the Control Panel.

   The "Setting the PG/PC Interface" dialog opens.
5. Make any necessary changes to the interface configuration and confirm them with "OK". You have to click "OK", even if you have not made any changes.
6. Restart the TIA Portal.

#### Result

The newly installed interface is now displayed in the project tree under the "Online access" folder.

### Setting parameters for the Ethernet interface

This section contains information on the following topics:

- [Setting parameters for the Industrial Ethernet interface](#setting-parameters-for-the-industrial-ethernet-interface)
- [Displaying operating system parameters](#displaying-operating-system-parameters)
- [Connecting the PG/PC interface to a subnet](#connecting-the-pgpc-interface-to-a-subnet)
- [Setting parameters for the Ethernet interface](#setting-parameters-for-the-ethernet-interface-1)
- [Utilization of temporary IP addresses](#utilization-of-temporary-ip-addresses)
- [Managing temporary IP addresses](#managing-temporary-ip-addresses)
- [Resetting the TCP/IP configuration](#resetting-the-tcpip-configuration)

#### Setting parameters for the Industrial Ethernet interface

##### Options in the parameter settings for the Industrial Ethernet interface

When setting parameters for the Industrial Ethernet interface, you have the following options:

- Parameters dependent on the operating system

  The Industrial Ethernet interface has parameters that are set in the operating system and are valid for all connected devices. These parameter settings are only displayed here, they can, however, be changed in the network settings of the operating system.
- Parameters that can be set in the software

  > **Note**
  >
  > Note that changes to interface parameters have a direct influence on the operating system and the programming device / PC. Remember that some parameter settings can only be changed if you have adequate user rights.

##### Parameters for the Industrial Ethernet interface

The following table contains an overview of the parameters of the Industrial Ethernet interface that are set by the operating system and can be changed by the user.

| Parameter settings that cannot be changed | Parameters that can be set |
| --- | --- |
| MAC address | Fast acknowledge at the IE-PG access and for TCP/IP |
| DHCP server activated/deactivated | Timeout at the IE-PG access and for TCP/IP |
| APIPA activated/deactivated | LLDP |
| IP address | Additional, dynamic IP addresses for the network adapter |
| Subnet mask | - |
| DNS addresses | - |
| DHCP addresses | - |

---

**See also**

[Basics of assigning parameters for the PG/PC interface](#basics-of-assigning-parameters-for-the-pgpc-interface)
  
[Displaying operating system parameters](#displaying-operating-system-parameters)
  
[Connecting the PG/PC interface to a subnet](#connecting-the-pgpc-interface-to-a-subnet)
  
[Setting parameters for the Ethernet interface](#setting-parameters-for-the-ethernet-interface-1)
  
[Utilization of temporary IP addresses](#utilization-of-temporary-ip-addresses)
  
[Managing temporary IP addresses](#managing-temporary-ip-addresses)
  
[Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights)

#### Displaying operating system parameters

The Ethernet interface is part of the operating system. All parameters of the network adapter can therefore be adapted in the network settings of the operating system.

You can display the following parameters in the software:

- Physical address of the network adapter
- Assignment of the IP address by a DHCP server activated or deactivated
- Assignment of a private IP address by the operating system activated or deactivated
- Current static IP address
- Assigned subnet mask
- DNS addresses
- DHCP addresses

If you want to modify the parameter settings, please refer to the documentation of the operating system or the network adapter.

##### Displaying current parameters of the Ethernet interface

To display the current parameters of the Ethernet interface, follow these steps:

1. Select the Ethernet interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Select "Configurations > Industrial Ethernet" in the area navigation.

---

**See also**

[Setting parameters for the Ethernet interface](#setting-parameters-for-the-ethernet-interface-1)

#### Connecting the PG/PC interface to a subnet

If you have created several subnets, you can specify the subnet to which the Ethernet interface is connected.

##### Procedure

To select the subnet to which the Ethernet interface is connected, follow these steps:

1. Select the Ethernet interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Go to "General > Assignment" and select the subnet to which you want to connect the Ethernet interface of the programming device / PC in the "Connection to subnet" drop-down list.
4. Close the dialog with "OK".

#### Setting parameters for the Ethernet interface

You can adapt some parameter settings relating to the network protocol directly in the software.

##### Requirement

You must have adequate user rights.

See also: [Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights).

##### Procedure

To change parameter settings relating to the network protocol, follow these steps:

1. Select the Ethernet interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Select "Configurations > IE-PG access" to adapt the protocol settings relevant for network management.

   - Select the "Fast acknowledge" check box to achieve faster reaction times with smaller network packets.
   - From the "Timeout" drop-down list, select the maximum time that can elapse before a network node is detected.
4. To activate the LLDP protocol and discover the network topology more accurately, set the "LLDP active" check box in "Configurations > LLDP".
5. Select "Configurations > TCP/IP" to adapt the TCP/IP protocol for network traffic during runtime.

   - Select the "Fast acknowledge" check box to achieve faster reaction times with smaller network packets.
   - From the "Timeout" drop-down list, select the maximum time that can elapse before there is a timeout during communication with a network node.

---

**See also**

[Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights)
  
[Displaying operating system parameters](#displaying-operating-system-parameters)

#### Utilization of temporary IP addresses

##### Adding a temporary IP address

If the IP address of a device is located in a different subnet from the IP address of the network adapter, you will first need to assign an additional IP address with the same subnet address as the device. Only then is communication between the device and the programming device / PC possible.

The assignment of an additional temporary IP address is also proposed automatically if you want to perform an online action and the current IP address of the programming device/PC is not yet in the correct subnet.

A temporarily assigned IP address remains valid until the next time the programming device/PC is restarted or until you delete it manually. See also: [Managing temporary IP addresses](#managing-temporary-ip-addresses)

> **Note**
>
> You require adequate permissions to be able to assign a temporary IP address.
>
> See also: [Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights)

#### Managing temporary IP addresses

If the IP address of a device is located in a different subnet from the current permanently assigned IP address of the network adapter, a suitable IP address from the subnet of the device is temporarily assigned to the network adapter.

You can display all temporarily assigned addresses and delete them. Note that IP addresses that you manually assigned in the operating system are not displayed in the TIA Portal.

##### Requirement

To delete, you require adequate permissions.

##### Procedure

To display and delete temporarily assigned addresses, follow these steps:

1. Select the Ethernet interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Select "Configurations > IE-PG access".

   A table with the assigned IP addresses is displayed.
4. Click the "Delete project-specific IP addresses" button to delete all the IP addresses at one time.

---

**See also**

[Influence of user rights](Introduction%20to%20the%20TIA%20Portal.md#influence-of-user-rights)

#### Resetting the TCP/IP configuration

If you have changed the TCP/IP protocol settings, you can reset them to the defaults.

##### Procedure

To restore the TCP/IP configuration to the default settings, follow these steps:

1. Select the Ethernet interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Select "Configurations > TCP/IP".
4. Click the "Standard" button to reset all the settings.

### Setting parameters for the MPI and PROFIBUS interfaces

This section contains information on the following topics:

- [Setting parameters for the MPI and PROFIBUS interfaces](#setting-parameters-for-the-mpi-and-profibus-interfaces-1)
- [Setting MPI or PROFIBUS interface parameters automatically](#setting-mpi-or-profibus-interface-parameters-automatically)
- [Setting parameters for the MPI interface](#setting-parameters-for-the-mpi-interface)
- [Setting parameters for the PROFIBUS interface](#setting-parameters-for-the-profibus-interface)
- [Overview of the bus parameters for PROFIBUS](#overview-of-the-bus-parameters-for-profibus)
- [Resetting the MPI or PROFIBUS configuration](#resetting-the-mpi-or-profibus-configuration)

#### Setting parameters for the MPI and PROFIBUS interfaces

##### Possible parameter settings for the MPI and PROFIBUS interfaces

The following parameter settings can be made for the MPI and PROFIBUS interfaces:

- Automatic configuration: You can use automatic detection functions to find out whether a device is connected to the PG/PC interface over PROFIBUS or MPI.
- Selecting a default configuration for PROFIBUS or MPI that can be adapted later.

##### Device- and network-related settings for MPI and PROFIBUS

You can set device- and network-related parameters for MPI and PROFIBUS interfaces. Device-related parameters are local settings for the interface. Network-related parameters, on the other hand, must match up on all devices.

##### MPI interface parameters you can modify

You can adapt the following default parameters for the MPI interface:

**Device-related parameters**

- Is only master
- Own address
- Timeout

**Network-related parameters**

- Highest address
- Transmission rate

##### PROFIBUS interface parameters you can modify

You can adapt the following default parameters for the PROFIBUS interface:

**Device-related parameters**

- Is only master
- Own address
- Timeout

**Network-related parameters**

- Highest address
- Transmission rate
- Profile
- Bus parameters
- Number of masters on bus
- Number of slaves on bus

> **Note**
>
> **Behavior when a subnet is assigned**
>
> If you permanently assign a subnet from the project to the interface, the subnet settings of the project take precedence. In this case, the settings for the respective interface cannot be changed.

---

**See also**

[Basics of assigning parameters for the PG/PC interface](#basics-of-assigning-parameters-for-the-pgpc-interface)

#### Setting MPI or PROFIBUS interface parameters automatically

##### Setting up automatic bus parameter detection

If you select an interface with automatic detection of the bus parameters (for example CP 5611 (Auto)), you can connect the programming device or PC to MPI or PROFIBUS without needing to set bus parameters. At a transmission speed lower than 187.5 Kbps, you may, however, have waiting times of up to one minute.

##### Requirement

- Masters that distribute bus parameters cyclically are connected to the bus.
- In PROFIBUS networks, the cyclic distribution of bus parameters is enabled.
- The interface is not assigned to a subnet. If you assign a subnet in the properties of the interface, the settings for the subnet in the project take precedence. In this case, the settings for the automatic interface configuration cannot be changed.

##### Procedure

To enable automatic bus parameter detection, follow these steps:

1. Select the interface in the project tree.
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Go to "General > Configurations > Active configuration" and select the setting "Automatic protocol detection".
4. Go to "Configurations > Auto configuration > Local settings" and select the address of the PG/PC interface in the "Own address" drop-down list.
5. If you then want to display the current bus settings, click the "Network detection" button.

---

**See also**

[Setting parameters for the MPI interface](#setting-parameters-for-the-mpi-interface)
  
[Setting parameters for the PROFIBUS interface](#setting-parameters-for-the-profibus-interface)

#### Setting parameters for the MPI interface

##### Changing the parameter settings of the MPI interface

The network-related parameters and bus parameters for the MPI network can be adapted. You should first select a default setting and then adapt this to the specific situation.

##### Requirement

The interface is not assigned to a subnet. If you assign a subnet in the properties of the interface, the settings for the subnet in the project take precedence. In this case, the interface configuration cannot be changed.

##### Setting defaults for the MPI interface

To adapt the parameters of the MPI interface, follow these steps:

1. Select the interface in the project tree.
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Go to "General > Assignment" and select the subnet with which you want to connect the interface in the "Connection to subnet" drop-down list.
4. Under "General > Configuration", select a default for the device and network-related parameters. The defaults are suitable for most configurations. Select one of the following settings:

   - Automatic protocol detection

     You can connect the programming device to MPI or PROFIBUS without having to set bus parameters. At a transmission speed lower than 187.5 Kbps, you may, however, have waiting times of up to one minute. Prerequisite for the automatic detection is a connection to the bus master, which distributes the bus parameters cyclically. With PROFIBUS subnets, cyclic distribution of bus parameters may not be deactivated (default PROFIBUS network setting).
   - MPI

     The "MPI" transmission protocol is selected. Typical parameters are set that are adequate for most configurations. You can change the parameters to your needs, however.
   - PROFIBUS

     The "PROFIBUS" transmission protocol is selected. Typical parameters are set that are adequate for most configurations. You can change the parameters to your needs, however.

##### Changing the default parameter settings

To adapt the default settings to your requirements, change the parameter setting where necessary in "Configurations > MPI".

You can set the following device-related parameters:

- Is only master

  An additional verification function to prevent bus disruptions when connecting the PG/PC to the network is disabled because the programming device or PC is the only master on the bus.

  - Do not enable this option unless you have only connected slaves to your programming device or PC.
  - If the "Is only master" check box is enabled, it is not possible to identify the directly connected device in the "Accessible devices" window.
- Own address

  This setting relates to the programming device or PC on which you call up the parameter settings of the interface. Set the local device address of your programming device or PC here.

  - This address must be unique throughout the network.
  - The programming device or PC is addressed using this address in the MPI network.
- Check

  This enables an additional safety function to prevent bus disruptions when connecting the PG/PC to the network. The driver checks whether the local address is already being used by another station. Active as well as passive stations are taken into consideration in this case. The driver monitors this on the PROFIBUS. The connection of the PG/PC to the network will take longer with the automatic check. To use the check, the driver must support the function. Furthermore, the "Is only master" option must not be selected.
- Timeout

  Set a higher timeout value if, for example, you have problems with long response times on the network.

You can set the following network-related parameters:

- Highest address:

  Select the configured highest device address. Make sure that the same highest device address is set for all devices of a PROFIBUS or MPI network.
- Transfer rate:

  Here, you select the transmission speed to be used on the MPI network.

---

**See also**

[Setting MPI or PROFIBUS interface parameters automatically](#setting-mpi-or-profibus-interface-parameters-automatically)

#### Setting parameters for the PROFIBUS interface

##### Changing the parameter settings of the PROFIBUS interface

The network-related parameters and bus parameters for the PROFIBUS network can be adapted more precisely. You should first select a default setting and then adapt this to the specific situation.

##### Requirement

The interface is not assigned to a subnet. If you assign a subnet in the properties of the interface, the settings for the subnet in the project take precedence. In this case, the interface configuration cannot be changed.

##### Setting defaults for the PROFIBUS interface

To adapt the parameters of the PROFIBUS interface, follow these steps:

1. Select the interface in the project tree.
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Go to "General > Assignment" and select the subnet with which you want to connect the interface in the "Connection to subnet" drop-down list.
4. Under "General > Configuration", select a default for the device and network-related parameters. The defaults are suitable for most configurations. Select one of the following settings:

   - Automatic protocol detection

     You can connect the programming device to MPI or PROFIBUS without having to set bus parameters. At a transmission speed lower than 187.5 Kbps, you may, however, have waiting times of up to one minute. Prerequisite for the automatic detection is a connection to the bus master, which distributes the bus parameters cyclically. With PROFIBUS subnets, cyclic distribution of bus parameters may not be deactivated (default PROFIBUS network setting).
   - MPI

     The "MPI" transmission protocol is selected. Typical parameters are set that are adequate for most configurations. You can change the parameters to your needs, however.
   - PROFIBUS

     The "PROFIBUS" transmission protocol is selected. Typical parameters are set that are adequate for most configurations. You can change the parameters to your needs, however.

##### Changing the default parameter settings

To adapt the default settings to your requirements, change the parameter setting where necessary in "Configurations > PROFIBUS".

You can set the following device-related parameters:

- Is only master

  An additional verification function to prevent bus disruptions when connecting the PG/PC to the network is disabled because the programming device or PC is the only master on the bus.

  - Do not enable this option unless you have only connected slaves to your programming device or PC.
  - If the "Is only master" check box is enabled, it is not possible to identify the directly connected device in the "Accessible devices" window.
- Own address

  This setting relates to the programming device or PC on which you call up the parameter settings of the interface. Set the local device address of your programming device or PC here.

  - This address must be unique throughout the network.
  - The programming device or PC is addressed using this address in the PROFIBUS network.
- Check

  This enables an additional safety function to prevent bus disruptions when connecting the PG/PC to the network. The driver checks whether the local address is already being used by another station. Active as well as passive stations are taken into consideration in this case. The driver monitors this on the PROFIBUS. The connection of the PG/PC to the network will take longer with the automatic check. To use the check, the driver must support the function. Furthermore, the "Is only master" option must not be selected.
- Timeout

  Set a higher timeout value if, for example, you have problems with long response times on the network.

You can set the following network-related parameters:

- Highest address:

  Select the configured highest device address. Make sure that the same highest station address is set for all devices of a PROFIBUS network.
- Transfer rate:

  Here, you select the transmission speed to be used on the PROFIBUS network.
- Profile:

  You have a choice of four alternatives for the PROFIBUS settings. "DP", "Standard" and "Universal (DP/FMS)" are predefined settings that you cannot change. If you select "User-defined", you can adapt the bus parameters yourself.

  - If you have selected "User-defined", go to "Configurations > PROFIBUS > Bus parameters" in area navigation.
  - If you have selected one of the defaults (DP, Standard or Universal (DP/FMS)), you should select the "Include" check box in "Configurations > PROFIBUS > Bus parameters > Additional parameters". You can then set the number of masters and slaves on the bus. This allows a more precise calculation of the bus parameters and potential bus disruptions can be prevented. The option cannot be selected with a user-defined profile.

---

**See also**

[Overview of the bus parameters for PROFIBUS](#overview-of-the-bus-parameters-for-profibus)
  
[Setting MPI or PROFIBUS interface parameters automatically](#setting-mpi-or-profibus-interface-parameters-automatically)

#### Overview of the bus parameters for PROFIBUS

##### Introduction

The PROFIBUS subnet will only function problem-free if the parameters for the bus profile are matched to one another. You should therefore only change the default values if you are familiar with how to configure the bus profile for PROFIBUS.

It may be possible for the bus parameters to be adjusted depending on the bus profile. The offline values of the bus parameters are always shown even if you are online and linked to the target system.

The displayed parameters are valid for the entire PROFIBUS subnet.

##### Meaning of the individual parameters

- Tslot: Wait-to-receive time (slot time)

  The wait-to-receive time (slot time) defines the maximum time the sender will wait to receive a response from the addressed partner.
- Max. Tsdr: maximum protocol processing time (max. station delay responder)

  The maximum protocol processing time defines the time after which the responding device must have processed the protocol.
- Min. Tsdr: minimum protocol processing time (min. station delay responder)

  The minimum protocol processing time specifies the minimum time required by the responding device to process the protocol.
- Tset: Trigger time (setup time)

  The trigger time is the time that may lapse between the reception of a data frame frame and the reaction to it.
- Tqui: Quiet time for modulator

  The quiet time for modulator specifies the time required to change from sending to receiving.
- GAP factor: GAP update factor (GAP factor)

  The GAP update factor specifies the number of token rotations before a new device is included in the token ring.
- Retry limit: maximum number repeated calls (retry limit)

  This parameter defines the maximum number of attempts (message frame repeats) made to reach a node.
- Trdy: Ready time

  The ready time is the time for an acknowledgment or response.
- Tid1: Idle time 1

  Idle time 1 specifies the delay time after receiving a response.
- Tid2: Idle time 2

  Idle time 2 specifies the delay time after sending a call without a response.
- Ttr: Target rotation time

  The target rotation time is the maximum time made available for a token rotation. During this time, all active devices (masters) receive the token once. The difference between the desired token round-trip time and the actual token round-trip time decides how much time is left for masters to send data message frames to the slaves.

  As the minimum target rotation time (Ttr), select a value = 5000 times the HSA (Highest Station Address).
- Watchdog: Watchdog

  The watchdog time specifies the time after which a device must be addressed.

  As the minimum watchdog time, select a value = 6250 times the HSA.

> **Note**
>
> If you want to create a user-defined bus profile, note that the minimum target rotation time (Ttr) should be 5000 times the HSA (highest PROFIBUS address). The minimum watchdog time should also be 6250 times the HSA.

---

**See also**

[Setting parameters for the PROFIBUS interface](#setting-parameters-for-the-profibus-interface)

#### Resetting the MPI or PROFIBUS configuration

If you have changed the MPI or PROFIBUS protocol settings, you can reset them to the defaults.

##### Requirement

The interface is not assigned to a subnet. If you assign a subnet in the properties of the interface, the settings for the subnet in the project take precedence. In this case, the interface configuration cannot be reset to the default values.

##### Procedure

To restore the MPI or PROFIBUS configuration to the default settings, follow these steps:

1. Select the MPI/PROFIBUS interface in the project tree in "Online access".
2. Select the "Properties" command in the shortcut menu of the interface.

   The dialog for configuring the interface opens.
3. Select "Configurations > MPI" or "Configurations > PROFIBUS", depending on the interface properties you want to reset.
4. Click the "Standard" button to reset all the settings.

## Simulating devices with S7-PLCSIM

This section contains information on the following topics:

- [Simulation of devices](#simulation-of-devices)
- [Starting the simulation](#starting-the-simulation)

### Simulation of devices

#### Introduction

You can use the TIA Portal to run and test the hardware and software of the project in a simulated environment. The simulation is performed directly on the programming device or PC. No additional hardware is required.

The simulation software provides a graphical user interface for monitoring and changing the configuration. It differs according to the currently selected device.

#### Integration in the TIA Portal

The simulation software is fully integrated in the TIA Portal but is only supported by certain devices. Therefore, the button for calling the simulation software is only active if the selected device supports simulation.

The simulation software for some devices requires its own virtual interface to communicate with the simulated devices. The virtual interface can be found in the project tree under the "Online access" entry next to the physical interfaces of the programming device/PC.

Once you have opened the software, additional help on the simulation software is available via a separate link.

---

**See also**

[Starting the simulation](#starting-the-simulation)

### Starting the simulation

Some devices can be simulated with additional software. You therefore do not have to have the actual devices to perform comprehensive testing of your project.

#### Procedure

To start the simulation software, follow these steps:

1. Select the device you want to simulate, for example, in the project tree.
2. Select the "Simulation > Start" command in the "Online" menu.

   This calls the simulation software.

---

**See also**

[Simulation of devices](#simulation-of-devices)
