---
title: "WinCC Server / WinCC Client (RT Professional)"
package: ClientServerWCCPenUS
topics: 44
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Server / WinCC Client (RT Professional)

This section contains information on the following topics:

- [Plant configurations (RT Professional)](#plant-configurations-rt-professional)
- [Configuring a multiple-station system (RT Professional)](#configuring-a-multiple-station-system-rt-professional)
- [Characteristics in runtime (RT Professional)](#characteristics-in-runtime-rt-professional)
- [WinCC RT Start (RT Professional)](#wincc-rt-start-rt-professional)
- [SIMATIC Shell (RT Professional)](#simatic-shell-rt-professional)
- [Guide to client server systems (RT Professional)](#guide-to-client-server-systems-rt-professional)
- [Clients and servers (RT Professional)](#clients-and-servers-rt-professional)

## Plant configurations (RT Professional)

This section contains information on the following topics:

- [Single-user system (RT Professional)](#single-user-system-rt-professional)
- [Multi-user system (RT Professional)](#multi-user-system-rt-professional)

### Single-user system (RT Professional)

#### Definition

An operator station has a view of its own project.

#### Application

Single-station systems are usually operated at the production level. They are used for operator control and monitoring of relatively small applications, but also for independent subprocesses or plant components within larger plants. A single-station system operates autonomously with its own screens and logs: all data are stored locally on one PC.

#### Structure

![Single-station system](images/21476557067_DV_resource.Stream@PNG-de-DE.png)

Single-station system

Single-station systems are based on the client-server principle:

- Runtime station: The WinCC data is stored in the integrated Microsoft SQL Server database on the operator station.
- The various Runtime components, including third-party components can access the Microsoft SQL Server database.
- Configuration PC: You can choose to use the actual operator station, or a different PC to configure your project.

### Multi-user system (RT Professional)

#### Definition

Up to 32 coordinated operator stations (WinCC clients) have a view of the same server project.

All WinCC data is stored in the integrated Microsoft SQL Server database on the WinCC server. Since the WinCC clients do not have their own WinCC project, they access the WinCC project on the WinCC server.

#### Application

The same plant processes can be monitored on several operator stations (clients). Any user intervention on an operator station, e.g. value changes, is immediately visible on all other operator stations. A multiple-station system is typically configured for small and mid-sized plants in which distribution of data to several servers is not required.

**Distribution of clients**

- With different tasks: You operate and monitor different views of the same process, for example, process screens on one operating station and alarms on another operating station.
- With similar tasks: You monitor and control the same view of the process from several locations, for example, along a production line.

You use access rights to specify exactly which functions or plant sections are available to a given user on which operator stations.

#### Structure

![Multiple-station system](images/21476683915_DV_resource.Stream@PNG-de-DE.png)

Multiple-station system

The client-server technology makes it possible to easily separate WinCC clients from the WinCC server: Configure your project centrally in the TIA Portal on the engineering station and download it to the WinCC server with process connection. The WinCC clients do not need a project planning, but merely a configuration:

- Networking with the WinCC server using drag-and-drop.
- Separately for each WinCC client:

  - Start screen

    Select a screen configured on the WinCC server as start screen.
  - Runtime language
  - Toolbar
  - Navigation buttons
  - Deactivation of shortcuts
  - Window properties

The WinCC server automatically assumes the task of supplying the WinCC clients:

- Runtime environment
- Screens, process values, alarms, log data, and reports
- Interface with the automation system
- Communication and coordination of clients
- Logging

Process specifications or alarm acknowledgments on one operator station are consistently available to other operator stations.

## Configuring a multiple-station system (RT Professional)

This section contains information on the following topics:

- [Requirement (RT Professional)](#requirement-rt-professional)
- [Configuration guidelines (RT Professional)](#configuration-guidelines-rt-professional)
- [Configuring the server (RT Professional)](#configuring-the-server-rt-professional)
- [Configuring the operator authorizations (RT Professional)](#configuring-the-operator-authorizations-rt-professional)
- [Configuring clients (RT Professional)](#configuring-clients-rt-professional)
- [Downloading the project to the server (RT Professional)](#downloading-the-project-to-the-server-rt-professional)
- [Settings for the multi-user system (RT Professional)](#settings-for-the-multi-user-system-rt-professional)

### Requirement (RT Professional)

#### Requirement

- All HMI devices on a client-server system are interconnected via network (LAN) or ISDN and standard TCP/IP protocol.

  You can also log on as client or server with PCs in adjacent subnets that are interconnected via router.

**Server PC**

- The server PC is connected to the automation systems via process bus.
- WinCC Runtime Professional is installed.
- Operating system on the server PC:

  - Microsoft Windows 10 maximum 3 clients
  - Microsoft Windows 11 maximum 3 clients
  - Microsoft Windows Server 2019 maximum 32 clients
  - Microsoft Windows Server 2022 maximum 32 clients
- Licenses:

  - "WinCC Server for RT Professional" for the WinCC Server
  - "WinCC RT Professional" for the project

**Client PC**

- A "WinCC Client for RT Professional" license on all WinCC clients.
- The "WinCC Server for RT Professional" license on the WinCC server.
- The "WinCC Client for RT Professional" license on the WinCC clients.

---

**See also**

[Settings for the multi-user system (RT Professional)](#settings-for-the-multi-user-system-rt-professional)

### Configuration guidelines (RT Professional)

#### Introduction

This chapter shows the basic procedure for setting up a multiple-station system. The multiple-station system consists of a WinCC server and two WinCC clients.

#### Procedure

1. Configuring servers.
2. Configuring clients: Start screen, menus & toolbars, language & font
3. To enable users access to the WinCC server project from a WinCC client: Configure operator authorizations
4. Download the project to the server.

### Configuring the server (RT Professional)

#### Introduction

Set up a project as the WinCC server.

#### Procedure

1. Create a project.
2. Add "WinCC RT Professional" to the HMI device.
3. Enter "WinCC Server" as the device name.
4. Configure the required screens, logs, tags, alarms, custom toolbars, project languages, etc. for the "WinCC Server".
5. In the Runtime settings under "General", select the start screen, a configuration and design for "Menus & Toolbars".
6. Under "Services", activate the server Runtime services you need for the specific configuration. Example: If the server screen displays recipes, select "Recipes".
7. Go to "Screens" to select the corresponding properties.
8. Under "Language & Font" select the Runtime languages required on the WinCC server.

#### Result

A project is set up and displayed on the WinCC clients. The project only becomes the server project when you link the "WinCC Server" with the WinCC clients.

### Configuring the operator authorizations (RT Professional)

#### Authorizations in WinCC

To enable access of a WinCC client to a server project, configure the appropriate operator authorizations for this WinCC client in the server project. The WinCC server provides the following operator authorizations:

- "Operate" The WinCC client is granted access to the WinCC server.
- "Enable remote control": A remote WinCC client can activate a server project, i.e. include it in runtime.

The computers on the network are not notified of a change to operator authorizations. This change is activated the next time a WinCC client wants to log on to a WinCC server.

The operator authorization "Enable remote control" is requested from the WinCC client as soon as the WinCC client requests activation of a project on a WinCC sever. If the corresponding operator authorization is not available on the WinCC server, the WinCC client is denied access to the project. Once the server project was closed on the WinCC client, a new logon is necessary at the next request to open the project.

> **Note**
>
> The operator authorizations configured are user-related, not computer-related. An operating authorization assigned is therefore valid for all operating stations with the same login.

#### Permissions in the operating system

To enable access of the WinCC clients to the server project, the corresponding project folder must be released for network access on the WinCC server. Set up authorizations in the operating system with all rights (write, read, modify) for the users who should have access to the projects.

> **Note**
>
> Different Windows permissions can be assigned for the shared project directories to enhance network security.

Detailed information on the assignment of permissions is provided in the Windows documentation.

#### Procedure

1. Open the WinCC user administration.
2. Select the user group of the user you want to edit.
3. To grant this user full access to the server project, activate the "Operate" and "Enable remote control" operator authorizations.

   ![Procedure](images/7692167563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/7692167563_DV_resource.Stream@PNG-en-US.png)

### Configuring clients (RT Professional)

#### Introduction

You create two WinCC clients and link them with the WinCC server.

#### Procedure

1. Add the following HMI devices to the project:

   - WinCC client, device name "WinCC Client1"
   - WinCC client, device name "WinCC Client2"
2. In the "Devices & Networks" editor, "Relations" tab, link the two WinCC clients with the WinCC server by means of drag-and-drop. A multiple-station system will be created.

   ![Procedure](images/7693912203_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/7693912203_DV_resource.Stream@PNG-de-DE.PNG)
3. Select "WinCC-Client1".
4. In the inspector window, select Properties > Computer name" and enter the physical computer name of the HMI device.

   The computer name identifies the HMI device in the network.
5. In the Runtime settings, "General" tab, select a screen as the "Start screen" of the WinCC server. In the multiple-station system, the WinCC client then displays this server screen in runtime.
6. Select a "Menus & Toolbars" configuration that was made on the WinCC server.
7. At "Services", activate the client Runtime services you need for the specific configuration, e.g. the scheduler.
8. Select additional design features under "Screens".
9. Select a Runtime language for the WinCC server under "Language & Font". For example, you can configure a separate Runtime language for each WinCC client.
10. Repeat steps 3 to 9 for "WinCC Client2".

    ![Procedure](images/24538352267_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/24538352267_DV_resource.Stream@PNG-en-US.png)

**Note**

In contrast to connections, the physical connection (network) and logic connection (client-server relation) are always created and deleted jointly. When you configure a relation, the devices will be linked automatically.

#### "Network data" editor

Using the arrow buttons below the network view, open the "Network data" editor. The "Network data" editor displays the relations you created. You can edit and delete these relations. If you first select a device and then select "Project overview" from the shortcut menu in the "Network data" editor, only the relations of the selected device are displayed.

#### Result

You have configured a multiple-station system with a WinCC server and two WinCC clients.

---

**See also**

[Configuring an integrated connection in the "Devices & Networks" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-an-integrated-connection-in-the-devices-networks-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Downloading the project to the server (RT Professional)

#### Procedure

1. Compile the project using the "Compile" icon in the toolbar.
2. Once you successfully compiled your project, select "Project tree > WinCC Server" and then select "Download to device" from the shortcut menu of "WinCC RT Professional".

For the initial transfer, enter the computer's's target address "\\computer name\<shared folder>" in the next dialog and exit the dialog using the "Transfer" button.

A transfer to the WinCC clients is not necessary because the WinCC server provides all necessary data to the WinCC clients.

---

**See also**

[Overview of compiling and loading projects (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-compiling-and-loading-projects-rt-professional)

### Settings for the multi-user system (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
- [Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)
- [Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
- [Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
- [Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)

#### Basics (RT Professional)

##### Introduction

Several requirements must be met in the configuration of your Windows environment for the multi-station system. If the required settings for this are not correct, it cannot be ensured that the multi-station system will function properly.

Redundant single-station systems must also be configured in the same network, so that they can be loaded by the engineering system and work together.

To download projects, the PC with the engineering system and the target device must be located in the same network.

##### Requirements for a multi-station system

To meet the requirements for a multi-station system, perform the following steps:

- IP addressing (TCP/IP): Develop a concept for the network architecture before assigning the IP addresses.
- Name resolution: Configure correct PC names for all PCs in the network.
- Operating system: Observe the compatibility of WinCC versions and operating systems.
- Terminal bus: Configure the terminal bus in the Simatic Shell.
- Order of network adapters: Select the correct order for the network adapters.
- Firewall: Adapt the security settings for operation with the Windows Firewall.

---

**See also**

[Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
  
[Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)
  
[Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
  
[Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
  
[Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)

#### Structure IP addressing (RT Professional)

##### Introduction

IP addressing is the basis for a functioning logical network. Keep in mind that the PCs to be networked are located in a physical and a logical network.

To meet this requirement, you need to have a concept for the network architecture ready when assigning IP addresses.

You need to use a router for two computers from different logical networks or subnetworks to communicate with each other.

The association of a PC to a logical network is defined by the network address and the subnet mask.

##### Valid network addresses

The network address is the address of the network and therefore only a portion of the string and not the IP address of the PC.

The following table shows the available classes of network addresses:

| Class | Available networks | Available hosts | Area | Example of a network address in the relevant range | Standard subnet mask |
| --- | --- | --- | --- | --- | --- |
| A | 126 | 16777214 | 1-126 | 5.0.0.0 | 255.0.0.0 |
| B | 16384 | 65534 | 128-191 | 129.10.0.0 | 255.255.0.0 |
| C | 2097151 | 254 | 192-223 | 198.10.20.0 | 255.255.255.0 |

> **Note**
>
> The range of 127.XYZ is reserved for loop tests and interprocess communication and does not constitute a permissible network address.

##### Example: Network address

The following network address is a valid network address: 142.16.x.y | network | host |

This example shows a Class B address. You can recognize the class membership by the address range, which extends from 128 to 191 for Class B. The first two tetrads correspond to the IP network address in this case.

With different network IP addresses (for example 142.16.xy and 142.11.xy), you need to make additional preparations for the client-server mode because a router (gateway) is required for different network addresses.

##### Test PC addressing

Test the correct PC addressing with the ping command.

1. To do so, open the command prompt with "Start > Run > cmd".
2. Run the command "ping +IP address" (e.g. "ping 128.0.0.1") for each of the other PCs.
3. If you get no response, you need to check the entire network configuration and parameter assignment.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)
  
[Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)
  
[Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
  
[Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
  
[Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)
  
[https://support.industry.siemens.com/cs/ww/en/view/2073614](https://support.industry.siemens.com/cs/ww/de/view/2073614)

#### Configure name resolution (RT Professional)

##### Introduction

If you are not using the DHCP service in conjunction with DNS in your network, which automatically assume this task, you must configure the "lmhosts" file for name resolution. When using a DNS and WINS server, the name resolution is also applied by the system.

The "lmhosts" file is located in the following path in Windows: "<Drive>\Windows\system32\drivers\etc\".

> **Note**
>
> All SIMATIC WinCC stations must be logged on either in the same workgroup or in the same domain.

##### Configure name resolution in the "lmhosts" file

1. Open the file in the text editor.
2. Enter all PCs accessible in the network according to the example in the file.
3. Delete the comments above the entries.
4. Save your changes.
5. Make these changes on all PCs.

   > **Note**
   >
   > To further optimize the name resolution in the network, write the keyword "#PRE" after each entry (maximum of 100 entries by default).
   >
   > The entries marked with this keyword are already stored in a cache when the system starts. For the IP address resolution, the cache is read first and then the "lmhosts" file if not all PC names can be resolved.

   > **Note**
   >
   > In large networks, configure the "hosts" file in the same directory parallel to the "lmhosts" file to speed up name resolution.

##### Test name resolution

Use the ping command to test if the changes of the name resolution have been successfully applied.

1. Open the command prompt with "Start > Run > cmd".
2. Run the command "ping+PC name" (e.g. "ping WINCCPC01") for all PCs which you have entered in the "lmhosts" file in the previous step.

   If you get a response and the PC name is resolved to its IP address, the file is configured correctly and the name resolution in the network works.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)
  
[Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
  
[Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
  
[Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
  
[Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)
  
<https://support.microsoft.com/en-us/kb/102725>

#### Configure terminal bus (RT Professional)

##### Introduction

The terminal bus must be configured for the correct network adapter in the SIMATIC Shell. When using multiple network adapters, there is a risk of selecting the wrong network adapter over which the WinCC communication should run.

Another indicator of a functioning network (accessibility of other PCs) is when you can see the projects of the other PCs in the network in the SIMATIC Shell.

##### Procedure

1. In Windows Explorer, select the "Simatic Shell" folder (last entry under "My Computer").
2. In the navigation window, the PCs appear in the tree view under the "Simatic Shell" entry.

   > **Note**
   >
   > If no PCs are displayed under "Simatic Shell", check the order of the network adapters in the Control Panel under "Network Connection > Advanced > Advanced Settings".
   >
   > The network adapter for terminal bus communication must always be first in the "Connections" list, even if you are using multiple network adapters in your target station.
3. Right-click in the "Simatic Shell" navigation window on the entry "Simatic Shell" and select "Settings..." in the shortcut menu.

   The "Selection of the terminal bus" dialog opens.
4. Make sure that the correct network adapter is set as the access point for the terminal bus.

   > **Note**
   >
   > By selecting another network adapter, you simultaneously change the assignment of the network adapter for the terminal bus.
   >
   > If you press the "OK" button to close the window, the "Re-initialization" dialog opens. Here you press the "Yes" button to accept the currently selected network adapter as access point for the terminal bus. The originally selected network adapter for the terminal bus is retained with the "No" button.

##### General information

- The network adapter configured for the terminal bus is displayed in blue in the "Network adapters" list when you click on a different network adapter.
- After opening the "Selection of the terminal bus" window, the network adapter with access to the terminal bus is shown in the "Network adapters" list with a bar in the background (selected). The network adapter configured as terminal bus therefore does not appear in blue. For this reason it is not clear at first glance which network adapter is assigned to the terminal bus. If now you select a different network adapter in the "Network adapters" list, the network adapter originally configured for the terminal bus appears in blue.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)
  
[Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
  
[Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
  
[Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)
  
[Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)

#### Setting the order of the network adapters (RT Professional)

##### Introduction

The order of network adapters defines the order in which the network services access the network adapter. Therefore, the network adapter or the connection that you have selected as terminal bus should be at the top.

##### Setting the order of the network adapters

1. Open the setting for the order of the network adapters with "Control Panel > Network Connections > Advanced > Advanced Settings > Adapters and Bindings".
2. Set the order of the network adapters.

If you have installed Windows or Windows Server on your PC, follow these steps:

1. Open Windows Explorer.
2. Show the menu bar with "Organize > Layout".
3. In the Control Panel, switch to the Network and Sharing Center.

   In the left window area, click "Change adapter settings".
4. Open the setting for the order of the network adapters with "Advanced > Advanced Settings > Adapters and Bindings".
5. Set the order of the network adapters.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)
  
[Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
  
[Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
  
[Adapt the security settings for the firewall (RT Professional)](#adapt-the-security-settings-for-the-firewall-rt-professional)
  
[Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)

#### Adapt the security settings for the firewall (RT Professional)

##### Basics

A firewall is often installed on the PCs of a plant for security reasons. Only the Windows Firewall is approved for operation with WinCC. If you enable this firewall, you must run the SIMATIC Security Control once again and adapt the settings.

The port filters are also not enabled.

---

**See also**

[Basics (RT Professional)](#basics-rt-professional)
  
[Structure IP addressing (RT Professional)](#structure-ip-addressing-rt-professional)
  
[Configure terminal bus (RT Professional)](#configure-terminal-bus-rt-professional)
  
[Setting the order of the network adapters (RT Professional)](#setting-the-order-of-the-network-adapters-rt-professional)
  
[Configure name resolution (RT Professional)](#configure-name-resolution-rt-professional)

## Characteristics in runtime (RT Professional)

This section contains information on the following topics:

- [Characteristics (overview) (RT Professional)](#characteristics-overview-rt-professional)
- [Reaction to system errors (RT Professional)](#reaction-to-system-errors-rt-professional)
- [Delta compile in runtime (RT Professional)](#delta-compile-in-runtime-rt-professional)
- [Characteristics of the server (RT Professional)](#characteristics-of-the-server-rt-professional)
- [Characteristics of the client (RT Professional)](#characteristics-of-the-client-rt-professional)

### Characteristics (overview) (RT Professional)

#### Editor characteristics in runtime

**Logs**

The Runtime database records and logs the process data on the WinCC server and simultaneously operates as log server. The WinCC clients receive their log data from the log server and display the data as table or graphics. All operations on the WinCC client are forwarded to the WinCC server. Processing results are returned to the WinCC client.

**Screens**

Data with other subsystems, for example, the log system are always exchanged locally. A screen can be opened and processed by several operating stations in runtime.

**Alarms**

The "Alarms" Runtime database, which generates alarms on the WinCC server and logs these alarms, functions as an alarm server. The WinCC clients receive their alarms from the alarm server and display them together with log data in the alarm view or alarm window.

When an operating acknowledges an alarm, the acknowledgement is transferred to the alarm server. The alarm server enters the change of status in the log and distributes the notification to all participating WinCC clients. The same process applies to the locking of alarms.

If an alarm server is temporarily unavailable in Runtime, an alarm window will open with a corresponding warning. When the alarm server becomes available again, alarms will be displayed in the alarm window once again.

**Reports**

The report system includes only print jobs which show log or process data based on Runtime.

The report system is started automatically on all clients during startup. The WinCC server functions as a report server. During startup, the WinCC clients log on to the report server and obtain the latest information on available print jobs and their status. When a print job is started on a client (always local), it receives the corresponding data from the report server. The report server, on the other hand, receives the status of the print job from the WinCC client. The report server then forwards this information to the other WinCC clients.

**Runtime scripts**

Project functions and standard functions of the WinCC server are always loaded and executed locally on the WinCC client.

**Runtime user administration**

The operator authorizations are checked by the Runtime component of the user administration. The Runtime component is automatically started on every computer when WinCC starts. On changes to the login, the current operating rights list is loaded.

**Text library (project texts)**

The Runtime text library runs on the WinCC server as a text server. The texts are always read from the database on the WinCC server.

### Reaction to system errors (RT Professional)

The WinCC clients are not provided any data if no WinCC server is available. All graphic objects that can be operated are grayed out and a connection error is displayed in the controls.

Scripts can be used to configure the display of connection errors on the WinCC client.

Once the WinCC server was recovered, the WinCC client will be reconnected.

### Delta compile in runtime (RT Professional)

You create, change and test large, distributed projects with numerous operating stations mostly on a configuration computer. The finished and tested project is then transferred to the respective HMI device. The project is compiled or delta-compiled depending on whether or not the HMI device is in Runtime.

#### Compiling

The entire project is compiled, downloaded to the HMI device and it will replace the existing project.

#### Delta-compile (download changes) in Runtime

Instead of downloading the entire project or changing it locally, with a delta download the changes will be applied directly and locally in Runtime.

At any given time during, only the changed or added Runtime objects, e.g. tags, screens, alarms, and logs will be downloaded online to the active runtime of an HMI device, without stopping Runtime on that station.

If you change a screen at runtime and download it to the HMI devices, for example, the modified screen is displayed automatically at the next screen selection in Runtime.

The offline project on the configuration PC and the online project on the HMI device must be consistent.

#### Field of application

Delta compile (download changes) offers the following options:

- During commissioning, operation, or maintenance, you edit the current project, download it to the HMI devices and immediately test it.
- You edit and download the project online at a central configuration station, instead of taking time-consuming local actions.
- You can first test the proposed changes on the configuration computer offline in a protected environment. Only then do you apply the changes in active operation. This approach helps you eliminate possible configuration errors before they result in downtime.
- Changes can be transferred consistently and take effect at the same time: Configuration changes are often interrelated and mutually dependent: they recalculate a value, create a corresponding tag and add it to a log and a trend display. These changes are completely closed and applied in full during operation. This approach prevents error states and instabilities in Runtime.

### Characteristics of the server (RT Professional)

This section contains information on the following topics:

- [Starting servers (RT Professional)](#starting-servers-rt-professional)
- [Server shutdown (RT Professional)](#server-shutdown-rt-professional)

#### Starting servers (RT Professional)

##### General procedure

The WinCC servers of a client-server system start independently of the WinCC clients. As soon as it has completed its startup, the WinCC makes its services available to the WinCC clients and informs itself about all the nodes on the network.

Communication with the automation system will be started.

If a WinCC server fails in runtime, the data on the WinCC client can no longer be updated. The WinCC clients will be informed of the absent WinCC server.

---

**See also**

[Reaction to system errors (RT Professional)](#reaction-to-system-errors-rt-professional)
  
[Activating and deactivating projects on the WinCC server (RT Professional)](#activating-and-deactivating-projects-on-the-wincc-server-rt-professional)

#### Server shutdown (RT Professional)

##### General procedure

When you shut down a WinCC server, it will no longer provide process data to the connected WinCC clients. The missing link is, for example, displayed in the alarm window or trend window of the active client projects. All fields with missing process values are displayed in gray in the process screen.

---

**See also**

[WinCC RT Start (RT Professional)](#wincc-rt-start-rt-professional)

### Characteristics of the client (RT Professional)

This section contains information on the following topics:

- [Starting the Client (RT Professional)](#starting-the-client-rt-professional)
- [Shutting down a client (RT Professional)](#shutting-down-a-client-rt-professional)

#### Starting the Client (RT Professional)

##### General procedure

A WinCC client always remains in runtime, for example, regardless of whether the WinCC server is briefly unavailable. When using WinCCStart to start a WinCC client, the server project is also activated if the WinCC server is not in runtime.

---

**See also**

[Activating and deactivating a project from the WinCC client (RT Professional)](#activating-and-deactivating-a-project-from-the-wincc-client-rt-professional)

#### Shutting down a client (RT Professional)

##### General procedure

Runtime is closed on the WinCC client, while runtime of the server project continues.

---

**See also**

[Activating and deactivating a project from the WinCC client (RT Professional)](#activating-and-deactivating-a-project-from-the-wincc-client-rt-professional)

## WinCC RT Start (RT Professional)

This section contains information on the following topics:

- [Overview of WinCCStart (RT Professional)](#overview-of-winccstart-rt-professional)
- [Activating and deactivating projects on the WinCC server (RT Professional)](#activating-and-deactivating-projects-on-the-wincc-server-rt-professional)
- [Activating and deactivating a project from the WinCC client (RT Professional)](#activating-and-deactivating-a-project-from-the-wincc-client-rt-professional)
- [Enabling time synchronization on the client (Professional) (RT Professional)](#enabling-time-synchronization-on-the-client-professional-rt-professional)
- [Additional settings: Autostart and language (RT Professional)](#additional-settings-autostart-and-language-rt-professional)
- [Configuring service mode (RT Professional)](#configuring-service-mode-rt-professional)
- [Remote access and Remote Desktop Protocol (RDP) (RT Professional)](#remote-access-and-remote-desktop-protocol-rdp-rt-professional)
- [Displaying products and components (RT Professional)](#displaying-products-and-components-rt-professional)

### Overview of WinCCStart (RT Professional)

#### Application area

Using WinCC RT Start, you enable and disable Runtime on the WinCC server and display information about the installed product and components.

#### Procedure

To open WinCC RT Start, follow these steps:

1. In the Windows Start menu, select "Start > All Programs > Siemens Automation > Runtime Systems > WinCC Runtime Professional V... > WinCC RT Start".

#### Functions

- Activating and deactivating a project
- Autostart of WinCC Runtime
- Displaying installed products and components
- Configuring service mode

---

**See also**

[Activating and deactivating projects on the WinCC server (RT Professional)](#activating-and-deactivating-projects-on-the-wincc-server-rt-professional)
  
[Additional settings: Autostart and language (RT Professional)](#additional-settings-autostart-and-language-rt-professional)

### Activating and deactivating projects on the WinCC server (RT Professional)

#### Application area

You activate and deactivate Server Runtime on the WinCC server using WinCC RT Start.

To enable access from a WinCC client to the server project, the server project must be located in a shared folder. The "WinCCProjects" folder is released by default during installation:

| Operating system | Path |
| --- | --- |
| Windows 10 | C:\Users\Public\Public Documents\Siemens\WinCCProjects |
| Windows 11 | C:\Users\Public\Public Documents\Siemens\WinCCProjects |
| Windows Server 2019 | C:\User\Public\Public Documents\Siemens\WinCCProjects |
| Windows Server 2022 | C:\User\Public\Public Documents\Siemens\WinCCProjects |

> **Note**
>
> You can also use your own folders and release these with corresponding authorizations.

#### Requirements

- The WinCC client and WinCC server are interconnected via network.
- The server project is stored in the "WinCCProjects" folder, or in a different shared folder.

- WinCCStart is opened via the Windows Start menu, "Start > All Programs > Siemens Automation > Runtime Systems > WinCC Runtime Professional V... > WinCC RT Start".

  ![Requirements](images/110863141387_DV_resource.Stream@PNG-en-US.png)

#### Procedure for activating a project

To activate the server project, proceed as follows:

1. Select the "File > Open" menu command. You can also click the file selection button in the "Project" field.
2. Select the server project. The name consists of the project name in the engineering system, e.g. "Project1", and the server name, e.g. "HMI_1".
3. You can select different diagnostic sources in the "Diagnostics" tab.
4. Activate the project using the toolbar icon ![Procedure for activating a project](images/23989783179_DV_resource.Stream@PNG-de-DE.png). You can also activate the project using the "File > Start RT" menu. Activation of runtime is indicated by a checkmark leading the "File > Start RT" menu command.

The WinCC server is started and provides all necessary data to the WinCC clients.

#### Procedure for deactivating a project

1. Deactivate the current project using the toolbar icon ![Procedure for deactivating a project](images/23989979403_DV_resource.Stream@PNG-de-DE.png). The checkmark leading the "File > Start RT" menu command is cleared.

The modules for the execution of Runtime will be deactivated. The "WinCC Runtime" program window will be closed.

The WinCC clients are not provided any data if no WinCC server is available. All graphic objects that can be operated are grayed out and a connection error is displayed in the controls. Once the WinCC server was recovered, the WinCC client will be reconnected.

---

**See also**

[Loading a project (Panels, Comfort Panels, RT Advanced)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#loading-a-project-panels-comfort-panels-rt-advanced)
  
[Downloading the project to an HMI device (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#downloading-the-project-to-an-hmi-device-rt-professional)
  
[Compiling a project (Panels, Comfort Panels, RT Advanced)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#compiling-a-project-panels-comfort-panels-rt-advanced)
  
[Overview of WinCCStart (RT Professional)](#overview-of-winccstart-rt-professional)

### Activating and deactivating a project from the WinCC client (RT Professional)

#### Application area

Use WinCCStart to activate and deactivate runtime on the WinCC clients.

#### Requirement

- The WinCC client and WinCC server are interconnected via network.
- The is stored in a shared folder on the WinCC server. The "WinCCProjects" folder is released by default and displayed on the network.

- WinCCStart is opened via the Windows Start menu, "Start > All Programs > Siemens Automation > Runtime Systems > WinCC Runtime Professional V... > WinCC RT Start".

  ![Requirement](images/110863141387_DV_resource.Stream@PNG-en-US.png)

#### Procedure for activating a project

To activate the server project, proceed as follows:

1. You can select different diagnostic sources in the "Diagnostics" tab.
2. Select the "File > Open" menu command. You can also click the file selection button in the "Project" field. The WinCC server "\\computer name\<shared folder>" is visible on the network.
3. Select the server project in the shared folder. The name consists of the project name in the engineering system, e.g. "Project1", and the server name, e.g. "HMI_1". A logon dialog opens when you connect to the WinCC server.
4. Enter the user name and password. Once you're successfully connected, the "Activate" toolbar icon is displayed if the WinCC server is not in runtime.

   If the WinCC-Server is in runtime, the runtime of the WinCC client is started automatically. In this case, skip the next step.
5. Activate the server project using the toolbar icon ![Procedure for activating a project](images/23989783179_DV_resource.Stream@PNG-de-DE.png). You can also activate the server project using the "File > Start RT" menu. Activation of runtime is indicated by a checkmark leading the "File > Start RT" menu command.

Runtime of the WinCC server is started. Runtime of the WinCC client then starts automatically. The WinCC server provides all necessary data to the WinCC clients.

#### Procedure for deactivating a project

1. Deactivate the current runtime of the WinCC client using the toolbar icon ![Procedure for deactivating a project](images/23989979403_DV_resource.Stream@PNG-de-DE.png). The checkmark leading the "File > Start RT" menu command is cleared.

The modules for the execution of Runtime will be deactivated. The "WinCC Runtime" program window will be closed.

> **Note**
>
> When working on the WinCC client, you can only terminate runtime on the WinCC client, but not the project on the WinCC server.

---

**See also**

[Shutting down a client (RT Professional)](#shutting-down-a-client-rt-professional)

### Enabling time synchronization on the client (Professional) (RT Professional)

#### Introduction

You configure client-server systems with multiple clients and servers as needed in WinCC. You can efficiently operate and monitor large plants in this way.

You have several options to ensure time synchronization in this system.

The following shows how a client without its own project synchronizes the time via the server.

#### Requirement

- A multi-station system is set up.
- Time synchronization is set up on the server.
- No further time synchronization is enabled on the client.

#### Procedure

Set up the startup list as follows:

1. Open the "Runtime settings > Services" editor.

   ![Procedure](images/59164540939_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/59164540939_DV_resource.Stream@PNG-en-US.png)
2. Under "Additional tasks/applications", enter the "CCTMTimeSync.exe" application and the associated drive path.

   The file is stored in your Siemens installation directory.
3. Disable "Use project directory".
4. Specify the startup size of the task or application window in the "Window style" column, for example, minimized, maximized or standard size.

#### Result

When you start Runtime, the application is loaded. The time of the client is automatically synchronized with the server.

### Additional settings: Autostart and language (RT Professional)

#### Introduction

The "Autostart" function automatically starts the server project at the time the server PC starts. Moreover, you can prevent users from canceling the start of runtime in order to gain unauthorized access to the operating system. To run this setup, you need a corresponding operator authorization in WinCC.

You can change the runtime language.

#### Procedure for Autostart

![Procedure for Autostart](images/110863707019_DV_resource.Stream@PNG-en-US.png)

1. Go to the "Autostart" tab.
2. Activate "Autostart".
3. Select a server project in the "Settings" area under "Autostart project".

   If you restart the computer with a project, the automatic start of runtime is initiated at the end of the load operation. You can prematurely cancel the automatic start and return to the operating system by pressing the "Cancel" button.
4. If you wish to start a client without its own project with redundant servers via autostart, select the check box "Alternative/redundant project" and select the alternative or redundant project.
5. To prevent an operator from canceling the automatic start, deactivate "Allow cancelling of activation".
6. Click "Apply". A Logon dialog opens.
7. Log on.

**Note**

If the server is not available, the alternative project is started after a certain time.

After you have successfully logged on, server runtime is started automatically at the next restart of the WinCC server.

#### Language change procedure

1. Select the "View > Language" menu command. A dialog that displays all user interface languages available for WinCCStart opens.
2. Select a user interface language.

---

**See also**

[Configuring service mode (RT Professional)](#configuring-service-mode-rt-professional)
  
[Overview of WinCCStart (RT Professional)](#overview-of-winccstart-rt-professional)

### Configuring service mode (RT Professional)

#### Introduction

Service mode provides you with the option of running WinCC Runtime Professional as service. As service, WinCC Runtime Professional can also be active when no interactive user is logged onto the computer.

#### Procedure for service mode

1. Go to the "Operating mode" tab.
2. Select the "Start as service" check box.
3. Enter the logon data in the "Operating mode" area.
4. Confirm with "Apply".

   ![Procedure for service mode](images/110921949323_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for service mode](images/110921949323_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Additional settings: Autostart and language (RT Professional)](#additional-settings-autostart-and-language-rt-professional)

### Remote access and Remote Desktop Protocol (RDP) (RT Professional)

#### Introduction

The following options are available to remotely access WinCC stations:

- NC (Real VNC)
- RDP (Remote Desktop Protocol)

Use the RealVNC software for remote access to the other computers of a widely distributed WinCC system (e.g. WinCC servers).

The use of the Remote Desktop Protocol (RDP) is only permitted for remote maintenance of WinCC clients. In addition, no server services (e.g. WebNavigator Server, DataMonitor Server, OPC Server) must be active on these computers. The reason for this is the handling of remote desktop sessions by the Microsoft operating system.

#### Remote maintenance of WinCC systems

The use of the Remote Desktop Protocol (RDP) is only permitted if the WinCC server or the single-station system is running in service mode.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss when the Remote Desktop connection is interrupted**  When the Remote Desktop connection is interrupted, e.g. by disconnecting the network cable on the computer of the Remote Desktop client, the archives and the OPC server, for example, no longer receive any values from the data manager.   The state lasts until the connection is re-established or the timeout of approx. 35 seconds has elapsed. |  |

#### Using RealVNC

You can find information on using "RealVNC" on the Customer Support pages on the Internet: Entry ID [55422236](https://support.industry.siemens.com/cs/document/55422236/how-do-you-access-wincc-and-pcs-7-plants-with-realvnc-?dti=0&lc=en-WW).

Note that the keyboard lock is not supported with "RealVNC". The keyboard lock is only effective for a Remote Desktop Protocol connection.

The following scenarios have been tested:

- WinCC as single-station system
- WinCC as distributed system
- WinCC in redundant mode
- WinCC/WebUX Server

In the released scenarios, you can also use communication via OPC.

#### Start Remote Desktop

Access to WinCC systems with a Remote Desktop client is only possible using a console session.

Access via the Remote Desktop Protocol may only take place through console transfer with the same user or initial login.

> **Note**
>
> **User groups and access rights**
>
> All "Remote Desktop" users must be included in the "SIMATIC HMI" user group on the target PC.

1. To start a console session, open the "Run" dialog, for example, with <Windows key+R>.
2. Enter the following command:- `mstsc /v:<Server> /admin`.
3. Enter the computer name or the IP address as server.
4. To obtain information on additional parameters, enter the following command: `- mstsc /?`.

#### Notes on using RDP

Note the following:

- Not all services are started when operating via the remote console.

  Start the WinCC project by means of the local user on the PC.
- If there was an RDP connection to a WinCC station, you should then restart the computer on which WinCC is installed. This is true for both the computer with WinCC engineering and with WinCC Runtime software. Restarting Runtime is not sufficient.
- Avoid loading the engineering or Runtime system via RDP because this can result in the load process being aborted or negatively affect Runtime.
- You should restrict configuration work in the engineering system via an RDP connection because this has not been tested.

### Displaying products and components (RT Professional)

#### Introduction

You can view your installed product software and options on the products tab:

![Introduction](images/25624899339_DV_resource.Stream@PNG-en-US.png)

The "Component" tab displays the following installed objects:

- Add-on software WinCC tools
- Interfaces
- Drivers
- Databases
- Logs

  ![Introduction](images/23990050955_DV_resource.Stream@PNG-en-US.png)

#### Procedure

1. Select "Help > About". The "About WinCC RT Professional" dialog opens.
2. Select a tab.

## SIMATIC Shell (RT Professional)

This section contains information on the following topics:

- [Remote access and encrypted communication (RT Professional)](#remote-access-and-encrypted-communication-rt-professional)
- [Accessing a computer outside a subnet (RT Professional)](#accessing-a-computer-outside-a-subnet-rt-professional)
- [Activating a project (RT Professional)](#activating-a-project-rt-professional)
- [Deactivating a project (RT Professional)](#deactivating-a-project-rt-professional)

### Remote access and encrypted communication (RT Professional)

#### Principle

Clients provided with the corresponding operator authorizations can operate a server project from a remote station, e.g.:

- Enable a server project
- Disable a server project

For remote configuration, the "Simatic Shell" dialog is available which you access through Windows Explorer.

![Principle](images/63347737483_DV_resource.Stream@PNG-en-US.png)

#### Function of Simatic Shell

In the "Simatic Shell" dialog you can view your configuration PC as well as the enabled servers and projects of your client-server system available through the network. These include all projects which run under a demo license.

You have the option of establishing an encrypted communication between computers, in addition to the unencrypted communication.

If you are using encrypted communication, connections are made only to computers for which the same pre-shared key has been set. You can communicate only with these computers. With unencrypted computers, no connection is possible. For the same network you can specify various environments with you your own PSK keys. You can find information on configuration at [Accessing a computer outside a subnet](#accessing-a-computer-outside-a-subnet-rt-professional).

For upgrading during operation, migration mode is also available. The mode allows encrypted and unencrypted connections side-by-side in the network. Only use migration mode as transitional solution to encrypted communication throughout the entire plant.

Depending on the configuration of the encrypted communication, only the corresponding computers are displayed in the Simatic Shell. In migration mode, all computers are visible with encrypted and unencrypted connection in the network (see figure above).

| Symbol | Meaning |
| --- | --- |
| ![Function of Simatic Shell](images/63347387275_DV_resource.Stream@PNG-de-DE.PNG) | The computer alllows only encrypted connections |
| ![Function of Simatic Shell](images/63347728907_DV_resource.Stream@PNG-de-DE.PNG) | The computer allows encrypted and unencrypted connections (migration mode) |
| ![Function of Simatic Shell](images/63346418443_DV_resource.Stream@PNG-de-DE.PNG) | The computer allows unencrypted connections |

The window is used to access an enabled server project from a client:

- To enable a project remotely
- To disable a project remotely

  > **Note**
  >
  > **Different names with WinCC Start and SIMATIC Shell**
  >
  > When WinCC Start opens, the name of a client-server project is fully displayed. The name of the server PC is used as the ending, for example, ClientServerProjectBuild11_1_A-Server_1".
  >
  > SIMATIC Shell shows under "Object" the name of the server PC on which the client-server project is running, for example, "A-Server_1". This means different client-server projects can be referred to with the same object name.

#### Setting up encrypted communication

For information on how to set up encrypted communication between the WinCC server/WinCC client and the configuration PC, please see [Accessing a computer outside a subnet](#accessing-a-computer-outside-a-subnet-rt-professional).

### Accessing a computer outside a subnet (RT Professional)

#### General procedure

Computers located behind a router in a network are introduced to the system by using the "Simatic Shell" dialog.

> **Note**
>
> You use the "Simatic Shell" dialog for central maintenance and diagnostics of all computers integrated in your client/server system.

Using the settings in "Simatic Shell", you introduce a computer within your subnet behind your router as an "Agent". The agent distributes the information from other computers to the computers within the subnet.

After having logged this computer on, all participating computers in the system can communicate even beyond the router limits. Each computer added to an existing group is informed of the current status of all computers, including those beyond the router limits. When the status of a computer changes, a alarm is issued to all participants, e.g.:

- If a computer has enabled a project
- If a computer is shut down
- If a computer is started up and thus enters the group.

> **Note**
>
> **Communication across network borders**
>
> The following adaptations must be made at the local Windows firewall in order that WinCC computers from various network can communicate with each other.
>
> With all WinCC specific firewall rules, you have to supplement the area with the IP addresses of the computers from the other networks or the complete IP address of the other networks.
>
>
>
> 1. In Windows, go to "Control Panel/System and Security/Windows Firewall".
> 2. Click "Advanced settings". The "Windows Firewall with Advanced Security" dialog opens.
> 3. Under "Inbound rules", successively select all relevant firewall rules, such as CCAgent, WinCC ProjectManager, etc.
> 4. In the properties on the "Area" tab, supplement the "Remote-IP address" with the IP addresses or IP areas of the communication participants.

#### Procedure

1. Click on the folder "My Computer > Simatic Shell" in the Windows Explorer of the client computer. The "Simatic Shell" dialog opens.
2. In the navigation window of the "Simatic Shell" dialog, select the first entry. In the shortcut menu of this entry, select the menu item "Settings...".

   The "Communication Settings" dialog opens.

   If no entry is displayed in the navigation window of the "Simatic Shell" dialog, you can also open the shortcut menu in the empty window.

   ![Procedure](images/66142779787_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/66142779787_DV_resource.Stream@PNG-en-US.png)
3. Check the setting in the field "Multicast Lifetime (TTL)". The value gives the maximum number of route jumps between various subnets (IP Parameters TTL).
4. Under "Multicast Proxy", enter the address of the computer that is the "Agent" for the subnet. This can be any computer of the subnet (client or server).
5. Add the computer to the list of network partners with the "Add" button.
6. If you want to set up an encrypted communication for the computer, activate the "Encrypted communication" option.

   To enter the PSK key, click the "Define" button.

   ![Procedure](images/66614122251_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/66614122251_DV_resource.Stream@PNG-en-US.png)
7. For the key, enter characters with high key strength.

   The key must be at least 8 characters long and include numbers and special characters in addition to uppercase and lowercase letters.

   Click "OK" to confirm your input.
8. If you do not want to use the freely available ports assigned with the default setting, define the assignment of the incoming ports.
9. If you want to leave encrypted and unencrypted connections side by side, activate the "Migration mode" option. This option is advisable, for example, for upgrading during operation.
10. Confirm your entry with "OK".

### Activating a project (RT Professional)

#### General procedure

A client/server system makes it possible to enable and disable projects remotely.

If you enable a server project from a client by using the "Simatic Shell" dialog, only the server project is enabled.

#### Requirements

In order to activate a server project on a client, the following conditions must be fulfilled:

- The user logged onto the client has the operator authorization to "Activate remote" in the WinCC project on the server.
- The project has been enabled for network access

#### Procedure

1. In Windows Explorer of the client, select the "Simatic Shell" entry. The "My Computer > Simatic Shell" window will be displayed.   
   All the servers and projects available in the network with their current status will be displayed.
2. Select the project to be enabled.
3. Select the "Activate remote" command from the shortcut menu.   
   A Login dialog appears.
4. Enter the user name and password for the current computer. The project is enabled on the server.

### Deactivating a project (RT Professional)

#### General procedure

A client/server system makes it possible to enable and disable projects remotely.

If you disable a server project from a client by using the "Simatic Shell" dialog, only the server project is disabled.

#### Requirements

In order to deactivate a server project on a client remotely, the following conditions must be fulfilled:

- The user logged onto the client has the operator authorization to "Activate remote" in the WinCC project on the server.
- The project has been enabled for network access

#### Procedure

1. In Windows Explorer of the client, select the "My Computer > Simatic Shell". The "Simatic Shell" window is displayed.   
   All computers and projects available in the network will be displayed with their current status.
2. Select the project to be enabled.
3. Select the "Deactivate remote" command from the shortcut menu. A Login dialog appears.
4. Enter the user name and password for the current computer. The project is disabled on the server.

## Guide to client server systems (RT Professional)

### Content

You can efficiently distribute operation and monitoring of your plant to multiple operator stations and servers. A WinCC Server with process connection records process data and logs alarms and process values. Moreover, a WinCC Server performs the following tasks in a WinCC network:

- Providing clients with the configuration data
- Providing clients with data from the process

Moreover, you can precisely map technologically or topologically complex systems.

This section shows you:

- The system configurations you can implement with WinCC.
- How to configure the server and clients in the client/server system.
- How the client/server system reacts in runtime.

## Clients and servers (RT Professional)

### Introduction

All process data of a WinCC project, e.g. alarms or trend values, is saved to different Runtime databases. Instead of being stored on each HMI device, these Runtime databases are located on the central WinCC server. The operator stations, i.e. the WinCC clients, access the WinCC server accordingly.

WinCC clients and WinCC servers are independent systems. You can activate WinCC clients at any time. It is also possible to activate and deactivate projects when you work on a WinCC client.

### Multiple-station system

You can user the server option to expand a WinCC single-station system to a high-performance multiple-station system with up to 32 coordinated operator control and monitoring stations.

![Multiple-station system with up to 32 clients on one WinCC server](images/21477954187_DV_resource.Stream@PNG-de-DE.png)

Multiple-station system with up to 32 clients on one WinCC server

WinCC clients display the data of precisely one WinCC server with process connection. WinCC clients operating on a multiple-station system do not have an own project ("Client without project"). For this reason, it is not necessary to configure the clients. The WinCC server provides the process and log data, alarms, screens, and reports to its online WinCC clients.

### Licenses required

- A WinCC license on the WinCC server.
- On the WinCC server, the " WinCC Server for RT Professional" license.
- On the WinCC clients, the "WinCC Client for RT Professional" license.

> **Note**
>
> **Licensing when upgrading to V14 or higher**
>
> If you upgrade from an older version to version V14 or higher, you need new licenses for WinCC Runtime Professional and WinCC Client for RT Professional.
