---
title: "WinCC Redundancy (RT Professional)"
package: RedundancyWCCPenUS
topics: 43
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Redundancy (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Configuring the redundant system (RT Professional)](#configuring-the-redundant-system-rt-professional)
- [Upgrading redundant plants (RT Professional)](#upgrading-redundant-plants-rt-professional)
- [System behavior in the event of a fault (RT Professional)](#system-behavior-in-the-event-of-a-fault-rt-professional)
- [Reference (RT Professional)](#reference-rt-professional)

## Basics (RT Professional)

This section contains information on the following topics:

- [Overview (RT Professional)](#overview-rt-professional)
- [How Redundancy Works (RT Professional)](#how-redundancy-works-rt-professional)
- [Standard server and preferred server (RT Professional)](#standard-server-and-preferred-server-rt-professional)
- [HMI system without redundancy (RT Professional)](#hmi-system-without-redundancy-rt-professional)
- [HMI system with redundancy (RT Professional)](#hmi-system-with-redundancy-rt-professional)
- [Requirements (RT Professional)](#requirements-rt-professional)
- [Setting up the servers (RT Professional)](#setting-up-the-servers-rt-professional)

### Overview (RT Professional)

#### Introduction

WinCC Redundancy offers considerably increased availability of WinCC and the plant as a whole with parallel operation of two interconnected servers.

![Introduction](images/7665705355_DV_resource.Stream@PNG-en-US.png)

To allow for an early detection of a failing partner server, the servers monitor each other in runtime.

If one server fails, the clients will automatically be switched from the failed server to the still active server. This ensures that all clients will always be available for monitoring and operating the process.

During the failure, the active server will continue to log all alarms and process data of the WinCC project. After the failed server comes back online, the contents of all alarm, process value and user logs will automatically be copied to the returned server. This will fill the log data gaps of the failed server. This action is also called synchronization after return.

The WinCC Redundancy Option offers:

- The automatic synchronization of alarm, process value and user logs after a failed server comes back online.
- The automatic synchronization of alarm, process value and user logs after a process connection error.
- The online synchronization of internal alarms.
- The online synchronization of internal tags (tag synchronization).
- The online synchronization of user logs.
- The automatic switching of clients between the redundant servers if one of the servers fails.
- The automatic switching of clients if the process connection fails.
- The "Application Health Check" function to monitor the WinCC applications.

#### The "Application Health Check" function

The expression "Application Health Check" refers to the cyclic lifebeat monitoring of important applications. The function increases the sensitivity of the redundancy, since the lifebeat monitoring is extended via the servers themselves to the individual applications. All important WinCC applications are automatically monitored.

The lifebeat monitoring detects a software error, sets the server status in the "@RedundantServerState" system tag to "Fault" and switches the linked clients to the redundant server.

A process control message warns the user about the software error.

> **Note**
>
> If a software error was detected by the "Application Health Check" function and client switching was initiated, the relevant server must then be restarted. Only then can the clients be reconnected to the server. The redundant servers must be equipped with Windows Server 2019 or Windows Server 2022.
>
> The client PCs must be equipped with Windows 10 or Windows 11.

---

**See also**

[Upgrading redundant plants during operation (RT Professional)](#upgrading-redundant-plants-during-operation-rt-professional)
  
[Settings for the multi-user system (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#settings-for-the-multi-user-system-rt-professional)

### How Redundancy Works (RT Professional)

#### WinCC Logging in Normal Operation

Normally, the master servers run completely in parallel with one another in Runtime. Each server computer has its own process driver connection and has its own data logs. The process data and alarms from the AS are sent to both servers simultaneously where they are processed accordingly.

The servers monitor each other during runtime to allow early recognition of the failure of a partner, which is then indicated by an alarm to the instrumentation and control.

User logs, internal alarms and internal tags can be continuously synchronized online (Online Synchronization).

Both servers have equal rights and work independently of each other. Both are available to the user. Should one server fail, the partner server is always available for equivalent redundancy.

![WinCC Logging in Normal Operation](images/7669324299_DV_resource.Stream@PNG-en-US.png)

The redundant servers communicate via the terminal bus to monitor the status and synchronize the logs. The network is a PC-LAN network with TCP/IP protocol. If there is an additional connection via a network adapter and/or a serial connection between the servers, this is used to monitor the status but not to synchronize the logs.

#### Failure of a Server

Server failure refers to the physical failure of a server, for example, due to a power failure or by turning off the server without shutting it down properly.  
If one of the servers fails, the server which is still operating receives and logs the process values and alarms from the AS. This guarantees data integrity with no gaps.

The clients will automatically be switched from the failed server to the redundant partner server. All operator stations are thus available again after a short switchover time.

#### Factors Triggering the Client Switch

The switch of the clients from the default (master) server to the partner server during a server failure is performed automatically by the system. The following factors cause a switch of servers:

- Network connection to server failed
- Server failure
- Process connection error
- The "Application Health Check" function has detected a defective WinCC application and triggers a switchover.
- The project is deactivated.

#### Factors triggering log synchronization after the server returns

The synchronization of the logs between the servers is initiated after the following errors have been corrected:

- Process connection error. Process connection monitoring may be turned off. For further information see "Configuration".
- Network connection failure to the partner server
- Server failure
- Project is not activated

#### Synchronization after the server returns

After the failed server comes back online, the redundancy performs a log synchronization for the down time. The gap in the logs caused by the failure is closed by transferring the missing data to the filed server. This action equalizes and makes both servers available again.

The following logs are synchronized:

- Alarm log
- Process value log
- User log
- Internal tags

The failed server receives its data after a slight time delay (caused by the failure). The log synchronization runs in the background, parallel to WinCC process management and logging. This guarantees the operator control and monitoring of the plant at all times.

**Synchronizing internal tags**

The internal tags must have the property "Tag synchronization".

Internal tags are compared on partner computers as soon as one of the tags is modified on one of the redundant servers.

The internal tags also include the system tags that start with the "@" character, e.g., @Current_User or @RM_Master. No online comparison should be configured for system tags.

#### Synchronization after process connection error

If there is a network error during running operation between a server and one or multiple AS, synchronization is automatically started, if this was configured, after the error was handled.

#### Online Synchronization

A direct server-to-server synchronization (online synchronization) takes place during alarm logging for internal alarms, in user logs and with internal tags with tag synchronization.

### Standard server and preferred server (RT Professional)

#### Standard server

In distributed systems, WinCC Controls receive their data with server prefix from specific servers to display alarms and process data.

You configure a standard server to clients in distributed systems so that data without unique server prefix are requested from this standard server. If no standard server is specified, an attempt is made to access the corresponding data locally. If there is no local data (e.g., alarms and archives), access is denied with an error message.

#### Preferred server

If you are using redundant servers in your multi-station system or distributed system, you can configure a preferred server for the clients.

A preferred server is the server of a redundant server pair with which the client in a multi-station system or distributed system primarily interconnects. The preferred server can be selected separately for each client so that the system can be permanently operated.

### HMI system without redundancy (RT Professional)

#### WinCC project

A WinCC project consists of a group of automation systems, a server computer and one or more client computers. The project also includes all programs, configuration data and miscellaneous settings.

The tasks of the control level are thus distributed over multiple PCs. The tasks are distributed following to a client server structure.

![WinCC project](images/7668785931_DV_resource.Stream@PNG-en-US.png)

The figure above shows the typical structure of the WinCC control level, with the corporate level above and the process level below.

Tasks performed by the servers:

- Servers acquire process images and alarms from the automation systems.
- To acquire data, the servers are connected to the automation systems via industrial networks.
- The servers provide the process data to the clients and control the processing states.

Tasks performed by the clients:

- The client stations operate and monitor the entire plant.
- Clients retrieve the currently needed states from the corresponding server via PC networks.
- In general, all clients are equal and have the same rights.

### HMI system with redundancy (RT Professional)

#### WinCC project

A WinCC project consists of a group of automation systems, a server computer and one or more client computers. The project also includes all program data, configuration data and other settings.

#### Redundant WinCC Project

![Redundant WinCC Project](images/7669125259_DV_resource.Stream@PNG-en-US.png)

The figure above shows the typical structure of a redundant WinCC control level, with the corporate level above and the process level below.

A project with a redundant configuration is realized with two configured servers which run in parallel and are functionally identical. The two servers are connected to each other, the AS and the clients. Both servers are configured and displayed as a redundant system in the TIA Portal. The users must make sure that both servers are configured identically.

For further information see "Configuring an identical function".

### Requirements (RT Professional)

- Only PCs with the following server operating systems can be used for redundant WinCC servers with multi-station mode:

  - Microsoft Windows Server Version 2019 and Version 2022
- The servers are connected via the network.
- The servers are time-synchronized. We recommend a time synchronization of the entire system (WinCC computer, automation systems, etc.).
- Alarms and acknowledgments from the AS and clients must always contain a time stamp in the frame to avoid double entries (chronological reporting). A way to achieve this is by using alarm blocks from the ASs.
- Process values, alarms and active alarm blocks from the lower-level automation systems are sent to both servers in parallel.
- The "Redundancy" license is available on each of the two servers.
- The redundancy servers must be configured functionally identical.
- At least one of the following additional connections should exist between the redundant servers:

  - Serial cable
  - Additional network connection via LAN card or via serial connection  
    This additional connection ensures a precise definition of the "Master" or "Standby" status. You can also use both connection options at the same time.  
    Configure the additional LAN connection via network card or serial connection in the redundancy settings of SIMATIC Shell. Use the TCP/IP protocol with the appropriate IP address or a serial port.

> **Note**
>
> To safely exit WinCC in the event of a power failure, the use of an uninterruptible power supply - UPS - is recommended.

#### Comparing blocked alarms

When a failed server is restored, currently blocked alarms are searched and compared with the general AS scan in Alarm Logging.

If an alarm is blocked passively, i.e. only on one server, the blocking information is compared.

If an alarm class is blocked on one server, the selection of the block is not compared on the redundant server.

---

**See also**

[Activating time synchronization (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#activating-time-synchronization-rt-professional)

### Setting up the servers (RT Professional)

This section contains information on the following topics:

- [Structure of a redundant project (RT Professional)](#structure-of-a-redundant-project-rt-professional)
- [Configuring an Identical Function (RT Professional)](#configuring-an-identical-function-rt-professional)
- [Redundant recipe data (RT Professional)](#redundant-recipe-data-rt-professional)
- [Online Synchronized Messages (RT Professional)](#online-synchronized-messages-rt-professional)

#### Structure of a redundant project (RT Professional)

##### Requirement

You must set up and configure two technically identical PCs for a redundant project. You can link up both PCs to each other by means of an additional interface, for example, Ethernet. Configure this link via Simatic Shell on both PCs.

##### Operating systems

The following operating systems are permitted in a redundant project:

- Single-station system: Windows 10 or Windows Server 2016/2019
- Multi-station system: Windows Server 2016/2019

##### User authorizations in the operating system

1. All users must be added to the "SIMATIC HMI" user group. This also applies to users who want to open WinCC projects remotely.
2. The storage folders of the projects must have the NTFS authorizations "SIMATIC HMI" with full access and "SIMATIC HMI Viewer" with read access. The authorizations must be inherited for all subordinate objects.
3. Members of the Windows user group "SIMATIC HMI" should not simultaneously be members of the Windows user group "SQLServerMSSQLUser$<Computername>$WINCC". The members of this group have administrator rights to the SQL server. You should therefore remove from this group all Windows users for whom restricted access to the WinCC database is sufficient.

#### Configuring an Identical Function (RT Professional)

##### Tag logs and alarm logs

Archives must be configured with identical function for the redundant servers. Functionally identical means:

- Identical logs, where additions can be made in the form of additional measurement points or logs.

The following logs are synchronized by WinCC:

- Archives held on hard disk, i.e. process value logs, compressed logs and alarm logs.
- On the other hand, no synchronization of main memory logs is performed.

##### Implementing configuration with identical functions

1. Create a project.
2. Configure this project for redundant servers.
3. Load the project to the redundant server using the "Download to device" function.  
   During this process, the project is compiled and automatically transferred to the master server and the standby server.

This ensures that the project was saved with identical functions on both servers.

#### Redundant recipe data (RT Professional)

User logs can be edited by operations, standalone programs, ASs or other functions.

##### Requirements

The configuration of the logs must be identical on both servers. The projects are always identical when downloaded via the TIA Portal.

##### Editing user logs in parallel

Note the following when adding data records to redundant user logs in parallel:

- On the server that previously failed, data records can only be added after the server has been restored and the synchronization completed. Otherwise, an error message appears in the script or in the User Archive Control.
- Even during the online synchronization, some time will pass before the data record has been synchronized in the redundant log.

> **Note**
>
> If both servers failed, the computer that was in operation last must be restarted first. Otherwise, changes that have not been saved could be lost.

#### Online Synchronized Messages (RT Professional)

All internal alarm tags and alarms without tag connections are synchronized online. This also includes system operator alarms of alarm logging and alarms of Batch-Flexible.

## Configuring the redundant system (RT Professional)

This section contains information on the following topics:

- [Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)
- [Creating a project (RT Professional)](#creating-a-project-rt-professional)
- [Configuring redundant servers (RT Professional)](#configuring-redundant-servers-rt-professional)
- [Configuring redundant clients (RT Professional)](#configuring-redundant-clients-rt-professional)
- [Loading the project to a device (RT Professional)](#loading-the-project-to-a-device-rt-professional)
- [Compiling a project (RT Professional)](#compiling-a-project-rt-professional)

### Overview of configuration steps (RT Professional)

This section describes the configuration of a redundant project using an example. The sample project consists of two identical servers and three clients. In the redundant project, one server is defined as master server and the other as standby server. During the configuration in the TIA Portal, both redundant servers are mapped as one server, symbolic for the redundant system.

#### Configuration steps

1. [Creating a project](#creating-a-project-rt-professional-1)

   - [Configuring master servers](#configuring-master-servers-rt-professional)
   - [Configuring redundancy for clients](#configuring-redundancy-for-clients-rt-professional-1)
   - Controlling the plant
2. [Configuring redundant servers](#configuring-redundant-servers-rt-professional)

   - [Configuring master servers](#configuring-master-servers-rt-professional)
   - [Configuring the standby server](#configuring-the-standby-server-rt-professional)
3. [Configuring server reaction](#configuring-server-reaction-rt-professional)

   - Client switchover
   - Synchronization selection
4. [Configuring redundancy for clients](#configuring-redundancy-for-clients-rt-professional-1)

   - Setting up clients
   - Connecting clients with servers
   - Configuring clients
5. [Loading the project to a device](#loading-the-project-to-a-device-rt-professional)
6. [Compiling a project](#compiling-a-project-rt-professional)

---

**See also**

[Creating a server (RT Professional)](#creating-a-server-rt-professional)
  
[Creating clients (RT Professional)](#creating-clients-rt-professional)
  
[Creating a project (RT Professional)](#creating-a-project-rt-professional)

### Creating a project (RT Professional)

This section contains information on the following topics:

- [Creating a project (RT Professional)](#creating-a-project-rt-professional-1)
- [Creating a server (RT Professional)](#creating-a-server-rt-professional)
- [Creating clients (RT Professional)](#creating-clients-rt-professional)
- [Control (RT Professional)](#control-rt-professional)

#### Creating a project (RT Professional)

##### Configuration sequence

The TIA Portal is open.

1. Click "Create new project".  
   A new project is created.
2. Change to project view.

You have created a project. You can now create devices in the project.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

#### Creating a server (RT Professional)

> **Note**
>
> In a redundant project you only map the master server as device in the "Devices & Networks" editor. You perform the division into a redundant system of master server and standby server in the section "Configuring redundant servers".

1. Double-click "Add new device" in the project tree.  
   The "Add new device" dialog box opens.
2. Enter the required device name in the text box.
3. Click the "PC systems" selection.
4. In the selection list, click "WinCC RT Professional" under "SIMATIC HMI application".
5. Confirm your selection by clicking "OK".  
   The server is created. The work area is opened with the device view and the new device is displayed.  
   In the project tree, the new device is created under the selected name.
6. Click in the device view on the newly created station and enter the physical name of the server under "Computer name" in the Inspector window.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

#### Creating clients (RT Professional)

Three clients are created to display the various options with the preferred servers:

1. Double-click "Add new device" in the project tree.  
   The "Add new device" dialog box opens.
2. Enter the required device name in the text box.
3. In the selection list, click "WinCC RT Client" under "SIMATIC HMI application".
4. Confirm your selection by clicking "OK".  
   The client is created. The work area opens in the device view and the new device is displayed.  
   In the project tree, the new device is created under the selected name.
5. Click in the device view on the newly created station and enter the physical name of the client under "Computer name" in the Inspector window.
6. Repeat these steps twice, until three clients have been created.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

#### Control (RT Professional)

Switch the work area to "Network view". In the work area, you must have four devices displayed next to each other in the order in which they were created.

The new devices are displayed one below the other in the project navigation.

### Configuring redundant servers (RT Professional)

This section contains information on the following topics:

- [Configuring redundancy for clients (RT Professional)](#configuring-redundancy-for-clients-rt-professional)
- [Configuring master servers (RT Professional)](#configuring-master-servers-rt-professional)
- [Configuring the standby server (RT Professional)](#configuring-the-standby-server-rt-professional)
- [Configuring server reaction (RT Professional)](#configuring-server-reaction-rt-professional)

#### Configuring redundancy for clients (RT Professional)

##### Requirement

- Clients have been configured.

##### Procedure

Proceed as follows to configure redundant clients:

1. Double-click the name of the client in the project tree.  
    The project tree offers the following additional options:

   - Device configuration
   - Online & diagnostics
   - HMI_RT_2 [WinCC RT Professional]
2. Double-click "HMI_RT_2 [WinCC RT Client]".  
   The project tree is extended by additional setting options.
3. Double-click "Runtime settings".  
   The Runtime editor of the server opens in the work area. The "General" setting is opened by default.
4. Click "Redundancy" in the navigator of the Runtime editor.  
   Here you can specify the preferred server of the client.

   - None: The current master is always used. After a change of master because of a failure, the client remains with the must recent current master, also after the return of the failed server.
   - Master: The redundant server set as master is always preferred. After a failure of the master, the client switches back to the master server after its return.
   - Standby: The redundant server set as standby is always preferred. After a failure of the standby, the client switches back to the standby server after its return.
5. Click the appropriate text box to specify the required option of the client.
6. Save the project.

The configuration of the redundant system has now been completed.

An additional activation of the redundant system is not necessary.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)
  
[Configuring clients (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#configuring-clients-rt-professional)
  
[Configuring clients (RT Professional)](#configuring-clients-rt-professional)

#### Configuring master servers (RT Professional)

1. In the network view, click the server that has been created.  
   The inspector window opens below the work area.
2. In the inspector window, click the "General" selection under the "General" tab.  
   The window shows the server name you have specified.

   ![Figure](images/75134323339_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/75134323339_DV_resource.Stream@PNG-en-US.png)
3. Double-click the name of your server in the project navigation.  
   The project navigation offers the following additional options:

   - Device configuration
   - Online & diagnostics
   - HMI_RT_1 [WinCC RT Professional]
4. Double-click "HMI_RT_1 [WinCC RT Professional]".  
   The project navigation is expanded by additional setting options.
5. Double-click "Runtime settings".  
   The Runtime editor of the server opens in the work area. The "General" setting is opened by default.
6. Click "Redundancy" in the navigator of the Runtime editor.  
   The Runtime editor window opens.

   ![Figure](images/75134319371_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/75134319371_DV_resource.Stream@PNG-en-US.png)
7. Activate redundancy by clicking in the "Configure redundant server" check box.
8. As option, you can define the server as "Standard master" by clicking the check box.

Information on configuring the standby server can be found in the next section.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

#### Configuring the standby server (RT Professional)

1. Open "Runtime settings" and click "Redundancy".
2. Enter a name for the redundant partner server in the "Redundant Partner" text box.
3. The configuration of the redundant server has now been completed.

> **Note**
>
> Only one device is displayed in the work area. This device includes the redundant server, comprising the master server and standby server.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

#### Configuring server reaction (RT Professional)

##### Client switchover

The reaction of the client to communication errors is selected in the "Client switchover" box.

1. By selecting the check box "Automatic client switchover in the case of a PLC error", you activate the automatic switchover of the client to the partner server when communication errors occur in the system.

   ![Client switchover](images/62136956555_DV_resource.Stream@PNG-en-US.png)

   ![Client switchover](images/62136956555_DV_resource.Stream@PNG-en-US.png)
2. Save the project.

##### Synchronization

In the "Synchronization" field, you specify which actions are to take place during synchronization of the servers if an error occurs:

1. Click "Synchronize all data in failure time period".  
   All data that was saved during the failure of a server is synchronized when the failed server returns.

   ![Synchronization](images/62136960267_DV_resource.Stream@PNG-en-US.png)

   ![Synchronization](images/62136960267_DV_resource.Stream@PNG-en-US.png)
2. Click "Synchronize data only for the following time period:"   
   In the text box, enter the required time interval for periodic synchronization.  
   The data is synchronized periodically independently of server failures.
3. By clicking the four following check boxes, you select the data you want to synchronize after a failure.
4. The recipes used from your recipe log are entered in the "Recipes" list. By selecting the check box in the "Synchronized" column, you select the recipes that you you want to synchronize after a server failure.

   ![Synchronization](images/118740080651_DV_resource.Stream@PNG-en-US.png)

   ![Synchronization](images/118740080651_DV_resource.Stream@PNG-en-US.png)
5. Save the project.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

### Configuring redundant clients (RT Professional)

This section contains information on the following topics:

- [Configuring clients (RT Professional)](#configuring-clients-rt-professional)
- [Configuring redundancy for clients (RT Professional)](#configuring-redundancy-for-clients-rt-professional-1)

#### Configuring clients (RT Professional)

##### Introduction

You create two WinCC clients and link them with the WinCC server.

##### Procedure

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

##### "Network data" editor

Using the arrow buttons below the network view, open the "Network data" editor. The "Network data" editor displays the relations you created. You can edit and delete these relations. If you first select a device and then select "Project overview" from the shortcut menu in the "Network data" editor, only the relations of the selected device are displayed.

##### Result

You have configured a multiple-station system with a WinCC server and two WinCC clients.

#### Configuring redundancy for clients (RT Professional)

##### Requirement

- Clients have been configured.

##### Procedure

Proceed as follows to configure redundant clients:

1. Double-click the name of the client in the project tree.  
    The project tree offers the following additional options:

   - Device configuration
   - Online & diagnostics
   - HMI_RT_2 [WinCC RT Professional]
2. Double-click "HMI_RT_2 [WinCC RT Client]".  
   The project tree is extended by additional setting options.
3. Double-click "Runtime settings".  
   The Runtime editor of the server opens in the work area. The "General" setting is opened by default.
4. Click "Redundancy" in the navigator of the Runtime editor.  
   Here you can specify the preferred server of the client.

   - None: The current master is always used. After a change of master because of a failure, the client remains with the must recent current master, also after the return of the failed server.
   - Master: The redundant server set as master is always preferred. After a failure of the master, the client switches back to the master server after its return.
   - Standby: The redundant server set as standby is always preferred. After a failure of the standby, the client switches back to the standby server after its return.
5. Click the appropriate text box to specify the required option of the client.
6. Save the project.

The configuration of the redundant system has now been completed.

An additional activation of the redundant system is not necessary.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)
  
[Configuring clients (RT Professional)](WinCC%20Server%20-%20WinCC%20Client%20%28RT%20Professional%29.md#configuring-clients-rt-professional)
  
[Configuring clients (RT Professional)](#configuring-clients-rt-professional)

### Loading the project to a device (RT Professional)

As soon as the "Download to device" function is activated, the project is generally compiled before the actual loading process.

1. For this purpose, open the work area with the devices in the network view.
2. Right-click in the required device to open the shortcut menu.
3. Four options are offered under the menu command "Download to device\":

   - Hardware and software (only changes)
   - Hardware configuration
   - Software (only changes)
   - Software (rebuild all)  
     If only the software has been changed, the hardware correction options cannot be selected.
4. Click the required action to select it.  
   A dialog window opens.
5. Set the type and the PG/PC interface.

   ![Figure](images/88793426571_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/88793426571_DV_resource.Stream@PNG-en-US.png)
6. Set the path of the destination folder. Click the field at the end of the destination path.  
   A dialog window for setting the destination path opens. The destination path is displayed after this:

   ![Figure](images/88803718411_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/88803718411_DV_resource.Stream@PNG-en-US.png)
7. Click the "Load" button.  
   The "Load preview" window and a progress window open.   
   The project is compiled. The project is transferred to the device after the successful compilation.

An additional reloading of the changes is possible retrospectively, for example, after changes have been made in the hardware or software of the device.

In the case of the first three options, only the changed part is recompiled. In the case of the fourth option, the entire project is recompiled.

> **Note**
>
> **Different logon data on the computers.**
>
> If different logins are required for the different computers involved, create the connections to those computers manually before loading. In Windows Explorer, for example, navigate to the standby computer and log on.

> **Note**
>
> **Loading redundant projects into the file system**
>
> It is not possible to load projects in a redundant server into the file system. You always load redundant projects onto the server from an engineering system.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

### Compiling a project (RT Professional)

#### Compiling data without "Download to device"

Alternatively, the changed data can be compiled using the "Compile" command, without downloading it immediately to the device.

1. Open the work area with the changed devices.
2. Right-click in the required device to open the shortcut menu.
3. Four options are offered under the menu command "Compile\":

   - Hardware and software (only changes)
   - Hardware (only changes)
   - Software (only changes)
   - Software (rebuild all)
4. Click the required action to select it.  
   In the bottom window, the result of the compilation is displayed in the "Info" tab.

---

**See also**

[Overview of configuration steps (RT Professional)](#overview-of-configuration-steps-rt-professional)

## Upgrading redundant plants (RT Professional)

This section contains information on the following topics:

- [Upgrading redundant plants during operation (RT Professional)](#upgrading-redundant-plants-during-operation-rt-professional)

### Upgrading redundant plants during operation (RT Professional)

#### Introduction

Redundant plants can be upgraded during operation. The automation system remains in runtime continuously during this period. All processes can be operated without interruption.

To upgrade redundant plants during operation, a separate download must be performed on both the master server and on the standby server of a redundant plant.

> **Note**
>
> System stability is not guaranteed during the download. After the download of individual servers, it cannot be guaranteed that both servers have the same project. Delta loading is not possible in this phase.

To avoid faults and redundancy losses, it is advisable to perform a complete download to both systems after the separate downloads. To perform a complete download to both systems, select the setting "Server and redundant partner" in the "Load preview" dialog under "Options for loading".

> **Note**
>
> If both servers are being shut down and upgraded simultaneously, redundancy is also retained. However, ongoing operation must be interrupted.

If you upgrade your plant from an older version to version V14 or higher, you need the following licenses:

- License for WinCC Runtime Professional
- License for WinCC Client for WinCC Runtime Professional
- License for WinCC WebNavigator and WinCC DataMonitor (if you use these options)

#### Requirement

- Autostart and Service mode must be disabled on the master server and the standby server.
- A preferred server must be configured for each client.
- Master server and standby server must be error-free.

#### Procedure

Proceed as follows to upgrade redundant plants during operation:

1. Close your project on the Engineering System and restart your PC.
2. Upgrade the TIA Portal.
3. Upgrade the project and compile the project.
4. Disable all clients that are configured for the master server.
5. Close the project on the clients.
6. Restart the clients.
7. Upgrade all disabled clients.
8. Disable the master server.
9. Close the WinCC application on the master server.
10. Restart the master server.
11. Upgrade the master server.
12. Run a complete download via the dialog "Load preview > Options for loading" for the master server only.
13. Configure the Web server and DataMonitor server, if necessary.
14. Enable the master server.
15. Enable all upgraded clients by connecting them to the master server project.
16. Wait until the Runtime data has been synchronized.
17. To upgrade the standby server and the clients connected to it, repeat steps 4 to 16 for the standby server.
18. Run a complete download for the master server and the standby server via the dialog "Load preview > Options for loading" with the setting "Server and redundant partner".

    Running the download with the option "Server and redundant partner" ensures that the same project is running on both partner servers.

**Note**

Create a backup before upgrading the master server.

**Note**

Synchronization of the Runtime data starts after approx. 10 minutes. The system events indicate the current status of the synchronization.

**Note**

While you carry out steps 4 to 16, your system is only running on a single server. Steps 4 to 7 and 8 to 13 can be carried out simultaneously.

**Note**

After download with the option "Server and redundant partner", subsequent delta loading is once again possible for the two servers.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Procedure**  You must adhere to the sequence described to ensure there is no disruption to plant operation. |  |

If you want to perform the download only for one plant of a redundant server pair, proceed as follows:

1. In the project tree, right-click on the relevant Runtime Professional device.
2. Select "Download to device > Software (all)".
3. Select the appropriate option in the "Load preview" dialog under "Options for loading".

---

**See also**

[Overview (RT Professional)](#overview-rt-professional)
  
[Configuring redundant servers (RT Professional)](#configuring-redundant-servers-rt-professional)
  
[Configuring redundant clients (RT Professional)](#configuring-redundant-clients-rt-professional)

## System behavior in the event of a fault (RT Professional)

This section contains information on the following topics:

- [Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)
- [Server not in Runtime (RT Professional)](#server-not-in-runtime-rt-professional)
- [Connection Fault to Partner Server (RT Professional)](#connection-fault-to-partner-server-rt-professional)
- [Faulty network connection to client (RT Professional)](#faulty-network-connection-to-client-rt-professional)
- [Faulty Process Connection (RT Professional)](#faulty-process-connection-rt-professional)
- [Software Error (RT Professional)](#software-error-rt-professional)
- [Changing the client in case of a process coupling error (RT Professional)](#changing-the-client-in-case-of-a-process-coupling-error-rt-professional)

### Failure scenarios (RT Professional)

#### Introduction

Some failures that might occur will be used to illustrate how WinCC Redundancy works. The following failures will be discussed:

1. Project is on the redundant [Server not in Runtime](#server-not-in-runtime-rt-professional)
2. [Connection Fault to Partner Server](#connection-fault-to-partner-server-rt-professional)
3. [Faulty network connection to client](#faulty-network-connection-to-client-rt-professional)
4. [Faulty Process Connection](#faulty-process-connection-rt-professional)
5. [Software Error](#software-error-rt-professional)
6. [Changing the client in case of a process coupling error](#changing-the-client-in-case-of-a-process-coupling-error-rt-professional)

WinCC Redundancy recognizes the current error itself or reacts to error or fault alarms with the following actions:

- Saving times and events
- Log synchronization
- Changing "Master"/"Standby" identifiers
- Switching clients
- Issuing alarms

#### Startup of the Server PCs

When the server PCs are starting up, the redundancy component establishes whether the partner server is already active. If the partner server is active, a Standby identifier is set in the server PC. If the partner server is not active during startup, a master identifier is set in the server PC. Upon disruption of the network connection between servers or if the partner server has been turned off, the "Master" code is reset.

In order to identify that the server computer is set as "Master", the system tag @RM_MASTER is set. If the server computer is "Standby", the @RM_MASTER tag is reset. The @RM_MASTER_NAME tag contains the name of the server PC that has the "Master" status, for example, "SERVER1". The tag @RedundantServerState displays on each redundant server its redundancy status, for example, "Standby". These tags can be evaluated by other applications or by scripts. However, the only tag that can be changed is @RM_MASTER.

Redundancy only sets the above tags. Both servers are always completely equal.

If neither a client nor the redundant partner server can be reached for the master server (e.g. project not activated on the PCs, or the network connection between the PCs is interrupted), this then becomes the standby server. This behavior is necessary to ensure that both redundancy servers do not receive the "Master" state.

If there is an additional connection between the two partner servers, the redundancy status is controlled via this connection. This will prevent that redundant partner servers assume the identical status.

> **Note**
>
> Please note that no log synchronization is performed via the serial interface.

#### Activating the redundancy server

1. Activate the configured master server.
2. Commission the connected clients.
3. Once the clients are active, activate the second server and its connected clients.

The initial synchronization is now carried out. The failure time for this synchronization is the time between activation of the first server and the second server

> **Note**
>
> Make sure when you boot redundant servers that the first server is completely booted before you activate the redundancy partner. The clients cannot be active yet when you activate the server for the first time.
>
> If you have deactivated a redundant server pair completely, you must adhere to a specific order when you activate them again. You start by activating the server that was deactivated last. Once this server has completely booted, you can activate the redundancy partner.

### Server not in Runtime (RT Professional)

#### Introduction

This scenario discusses the behavior of redundancy, if the project has been deactivated on Server 2.

The following actions will be triggered:

- Server 1 stores the failure time (date and time) of Server 2.
- Server 1 will report the failure of Server 2 through a system alarm.
- If Server 1 is the standby server, this takes over the role of the master by setting the @RM_MASTER tag. Correspondingly the @RM_MASTER_NAME and @RedundantServerState tags are changed.
- The clients connected to Server 2 switch over to Server 1.

#### Server 2 Comes Back Online

The downtime means that there is a gap in the logs of Server 2. This gap is filled by the following measures:

- Server 1 stores the return time (date and time) of Server 2.
- Server 1 will report the return of Server 2 through a system alarm.
- A redundancy match is carried out for alarm data, process data and user logs from Server 1 to Server 2.
- The @RM_MASTER tags remain unchanged in both servers, i.e., the @RM_MASTER tag in Server 1 remains set and the @RM_MASTER tag in Server 2 is reset. The @RM_MASTER_NAME and @RedundantServerState tags also remain unchanged.
- Clients which are configured with Server 2 as their preferred server switch back to that server.

Compared to online synchronization, log synchronization following a server failure can take noticeably longer depending on the number of data records to be synchronized and the computer/network loads.

If failures alternate between the two servers (see diagram), they will be synchronized one after the other. After the synchronization, all data will be available in both logs.

![Server 2 Comes Back Online](images/7674718731_DV_resource.Stream@PNG-en-US.png)

In the case above, Server 1 first passes all values to Server 2 for failure A, then Server 1 synchronizes itself from Server 2 for downtime B. Synchronization always occurs on the "Standby" server based on the "Master" server.

All these processes run automatically and in the background, independently of the process value logging and alarm logging from the subordinate automation systems running in parallel.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

### Connection Fault to Partner Server (RT Professional)

#### Introduction

This scenario discusses the behavior of redundancy in case of connection failures to Server 2. Prior to the occurrence of this event, both servers run in Runtime without failures.

The described connection failure occurs if, for example, the terminal bus at Server 1 is pulled.

#### Initial Situation 1

Upon connection failure, Server 1 has the "Master" status and Server 2 the "Standby" status.

**Connection failure occurs**

The following reactions are triggered upon occurrence of the connection failure:

- Server 2 becomes the master server and saves the time of failure (date and time).
- Server 2 indicates by means of a system alarm that the partner server has failed and Server 2 has switched to the "Master" status.
- Server 1 indicates by means of a system alarm that a failure has occurred in redundancy mode and that Server 1 has switched to "Standby" status.
- Tags @RM_MASTER, @RM_MASTER_NAME and @RedundantServerState are reset on both servers according to the switchover.

**Connection is restored**

During the connection fault, the alarms of Alarm Logging and the user logs could not be synchronized.

This situation is remedied by the following measures:

- Server 2, which is now the master, saves the time of the restoration (date and time).
- Server 2 indicates, by means of a system alarm, the return of the partner server.
- Redundancy synchronization from master server to standby server.
- Through the online synchronization of Alarm Logging, the system alarm concerning the return of the partner server is also displayed on Server 1.
- The @RM_MASTER, @RM_MASTER_NAME and @RedundantServerState tags remain unchanged in both servers.

#### Initial Situation 2

Upon connection failure, Server 1 has the "Standby" status and Server 2 the "Master" status.

**Connection failure occurs**

The following reactions are triggered upon occurrence of the connection failure:

- Server 2 becomes the master server and saves the time of failure (date and time).
- Server 2 displays, by means of a system alarm, the failure of the partner server.
- Server 1 indicates, by means of a system alarm, that a failure occurred during redundancy mode and remains the standby server.
- The @RM_MASTER, @RM_MASTER_NAME and @RedundantServerState tags remain unchanged in both servers.

**Connection is restored**

During the connection fault, the alarms of Alarm Logging and the user logs could not be synchronized.

This situation is remedied by the following measures:

- Server 2 saves the time of return (date and time)
- Server 2 displays, by means of a system alarm, the return of the partner server
- Redundancy synchronization from master server to standby server
- Through the online synchronization of Alarm Logging, the system alarm concerning the return of the partner server is also displayed on Server 1
- The @RM_MASTER, @RM_MASTER_NAME and @RedundantServerState tags remain unchanged in both servers.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

### Faulty network connection to client (RT Professional)

#### Introduction

In this third scenario, a disturbance occurs in the network connection between Server 2 and the client "CL5" that belongs to Server 2.

The following actions will be triggered:

- Client "CL5" automatically switches over from disturbed Server 2 to running Server 1.

#### End of the Network Disturbance to the Client

The following reactions are triggered at the end of the network disturbance:

- The @RM_MASTER, @RM_MASTER_NAME and @RedundantServerState tags remain unchanged in both servers.
- If Server 2 is configured as the preferred server for client "CL5", then client "CL5" switches back to that server once more.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

### Faulty Process Connection (RT Professional)

#### Introduction

In scenario 4, on Server 2 there is a fault on the process link due to an interrupted network connection to the automation systems.

An AS connection error is only recognized by Redundancy as a failure, if the connection is interrupted to only one server. If there is a connection fault from one AS to both servers (e.g. caused by an AS failure), this will not be recognized as a failure by Redundancy.

If WinCC recognizes a failure, the following actions will be triggered:

- The disturbance of the process link is reported on Server 2.
- Server 1 receives a message that partner Server 2 has failed.
- Server 1 stores the failure time (date and time) of Server 2.
- If in the server project "Client change with disturbance in the process link" is configured, the clients linked to this server are changed to the partner server.
- In Server 1, the @RM_MASTER tag is set to Master, in Server 2 to "Standby". Correspondingly the @RM_MASTER_NAME and RedundantServerState tags are adapted. In sever 1, @RedundantServerState is set to "Fault".

#### Correction of the Process Link Error on Server 2

Provided process connection monitoring has been activated, the gap in the archive of Server 2 will be filled by the following measures:

- Server 1 stores the return time (date and time) of Server 2.
- A redundancy match is carried out from Server 1 to Server 2, since no faults were found for process connection at Server 1. The data of all ASs will be synchronized. This means that the data of ASs that have not failed will also be synchronized.
- On Server 2 the @RedundantServerState tag is changed from "Fault" to "Standby".
- The correction of the process link error on Server 2 is announced by a system message.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

### Software Error (RT Professional)

#### Introduction

In scenario 5, an error occurs on Server 2 in software that is being monitored. When the error occurs, Server 2 is "Master" and Server 1 is on "Standby" status. There are several clients connected to each server.

If the "Application Health Check“ function detects an error in the WinCC software, the following actions are initiated:

- Application Health Check reports the error to redundancy. The status of Server 2 is set in the @RedundantServerState tag to "Fault". The @RM_Master tag is set to "Standby".
- The @RM_Master tag in Server 1 is set to the "Master". Correspondingly the @RM_MASTER_NAME and RedundantServerState tags are adapted.
- The clients connected to Server 2 switch over to Server 1.
- A process control message warns the user about the software error.

#### Correction of the Software Error on Server 2

The software error can be cleared by deactivating the server project and restarting server. When the project is activated on Server 2 the archives are automatically synchronized.

- On Server 2 the @RedundantServerState tag is set to "Standby". Server 1 remains at "Master" status.
- Server 1 stores the return time (date and time) of Server 2.
- A redundancy match is carried out for the user archive from Server 1 to Server 2.

> **Note**
>
> When a software error is detected by the "Application Health Check" function resulting in a client switching process and process control message, the server affected must be deactivated and the computer restarted. Only then can the clients be reconnected to the server. An archive synchronization is only performed backdated to the moment a software error is detected by the server.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

### Changing the client in case of a process coupling error (RT Professional)

#### Introduction

A redundant system consists of two functionally identical servers. One server is the "Master" server and the other is the redundant partner server. In the normal, undisturbed operating state the "Master" server has the status of "Master" and the redundant partner server has the status of "Standby". Clients are connected to the "Master" server unless a preferred server has been configured, in which case they are connected to the preferred server.

As soon as both servers are in Runtime, the processes coupling monitoring is activated. The number of defective logical connections to the "Master" server and the redundant partner server is cyclically determined. If the "Master" server has more defective logical connections than the redundant partner server, the status of the server becomes invalid ("Fault"). The clients are switched over to the redundant partner server, which now has the "Master" status.

> **Note**
>
> The "Fault" status is not displayed in the "@RM_MASTER" system tag but in the "@RedundantServerState" tag.

#### Normal operating state

The plant consists of the redundant servers A and B. There are also three clients. Client 1 has entered server A as its preferred server, client 2 has entered no preference and client 3 has entered server B as its preferred server.

> **Note**
>
> The example below shows the logical connections, not the physical connections. In other words, the connection is shown as separated when the connection is terminated, because the data transfer is interrupted. The physical connection can remain intact at the same time.

![Normal operating state](images/7671189387_DV_resource.Stream@PNG-en-US.png)

#### Process connection error on server A

There is a process connection error on server A. The error is not present on server B. The number of defective logical connections on server A is greater than on server B. Server A therefore receives the "Fault" status. As a result, clients 1 and 2 switch over to redundant server B.

![Process connection error on server A](images/7674384907_DV_resource.Stream@PNG-en-US.png)

#### End of the process connection error

When the process connection error on server A has been cleared, server A then has the status "Standby". As a result client 1 switches over to server A, since it has indicated this as its preferred server. Client 2 stays connected to server B because this has now become the "Master" server since the Redundancy switchover and client 2 has indicated no preferred server.

![End of the process connection error](images/7674660491_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The OPC couplers are not monitored. Therefore, there will be no client switching in case of an error in the OPC couplers.

---

**See also**

[Failure scenarios (RT Professional)](#failure-scenarios-rt-professional)

## Reference (RT Professional)

This section contains information on the following topics:

- [WinCC Redundancy System Tags (RT Professional)](#wincc-redundancy-system-tags-rt-professional)
- [System messages WinCC Redundancy (RT Professional)](#system-messages-wincc-redundancy-rt-professional)

### WinCC Redundancy System Tags (RT Professional)

#### Overview of the redundancy tags

The @RM_MASTER and @RM_MASTER_NAME system tags are used by WinCC Redundancy for master/standby control for the two redundant servers and for client toggling. These system tags can also be read and changed with other applications and with scripts.

| System tags | Meaning |
| --- | --- |
| @LocalMachineName | This tag contains the local computer name. |
| @RedundantServerState | This tag indicates the redundancy of this server.  Value range:  0: Undefined status (start value)  1: Server is master  2: Server is standby  3: Server is fault  4: Server is standalone (no redundant operation) |
| @RM_MASTER | This tag @RM_MASTER is set to identify that the server computer is master. If the server computer is "Standby", the @RM_MASTER tag is reset. |
| @RM_MASTER_NAME | The @RM_MASTER_NAME tag contains the name of the master server, for example "SERV_4". |
| @RM_SERVER_NAME | This tag contains the name of the server on which a client is connected. |
| @RM_UA_ONL_"Log name" | For diagnostics purposes only. A separate tag with a corresponding log name is created for each user log.  On the standby side, @RM_UA_ONL_"Log name" is set to 0 when synchronization has been successfully completed. The value remains set to 1 on the master because a feedback mechanism from the standby does not exist. |
| @RM_OFFLINE_UA_NAME | For diagnostics purposes only. This tag contains the name of the user log currently being synchronized. |

#### Overview of performance tags

The performance tags @PRF_REDUNDANCY_... map the states of the redundant servers.

| System tag | Description |
| --- | --- |
| @PRF_REDUNDANCY_IS_SYNCHRONIZED | Synchronization status:  - 0: Redundant applications are not synchronized. - 1: Redundancy synchronization of all applications is complete.   In addition to WinCC, the status can be influenced by other applications registered for the redundancy, for example, SIMATIC BATCH. |
| @PRF_REDUNDANCY_VALIDATION | Validation points of the server. The validation value determines which server will be the primary server.  The validation value depends, for example, on the connection and runtime status.  If the redundancy was configured correctly, the validation value is the same on both redundant servers.  When the validation values are not identical, the server with the greater value will become the primary server.  Typical values:  - 37: The server status is good.   - Runtime is active.   - Redundant connection over serial interface - 35: The server status is good.   - Runtime is active.   - Redundant connection over LAN - < 35: The server has the internal status "FAULT".   Check the connection status or the server status. The "FAULT" status is set for a critical operating state, for example, when a server application no longer responds.   When a server takes on the "FAULT" status, the partner server becomes the primary server.   Example calculations:  - When runtime is disabled on the server, the validation is reduced by four points. - When the terminal bus cannot be reached, validation is reduced by 20 points. |
| @PRF_REDUNDANCY_PARTNER_VALIDATION | Validation points of the redundant partner server  If the redundancy was configured correctly, this value is the same on both redundant servers. |
| @PRF_REDUNDANCY_AS_COUNT | Number of AS connections on the server  If the redundancy was configured correctly, this value is the same on both redundant servers.  The following conditions will cause a redundancy switchover:  - The validation values are identical on the redundant servers. - The number of AS connections is different.   In this case, the server with more AS connections will become the primary server. |
| @PRF_REDUNDANCY_PARTNER_AS_COUNT | Number of AS connections on the redundant partner server  If the redundancy was configured correctly, this value is the same on both redundant servers. |
| @PRF_REDUNDANCY_CURRENT_STATE | Redundancy status of the server:  - 0: Undefined status - 1: Server is primary server - 2: Server is standby - 3: Server is in "FAULT" status - 4: Server is standalone or no redundant operation |
| @PRF_REDUNDANCY_PARTNER_CURRENT_STATE | Redundancy status of the redundant partner server |
| @PRF_REDUNDANCY_FAULT_POSTPONED | Tag value = 1: The server has the status "FAULT_POSTPONED".  The internal status of the local server is "FAULT", but the partner server cannot take on the "Master" status. A redundancy switchover is not possible. The cause is, for example, an ongoing redundancy synchronization.  As soon as the conditions for a redundancy switchover are met, the server changes to the "FAULT" status. The tag "@PRF_REDUNDANCY_CURRENT_STATE" takes on the value "3". |
| @PRF_REDUNDANCY_PARTNER_FAULT_POSTPONED | Tag value = 1: The redundant partner server has the status "FAULT_POSTPONED". |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT | Number of redundancy switchovers since activation of runtime or since the last reset with "@PRF_REDUNDANCY_SWITCHOVER_COUNT_RESET". |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT_PERIOD | Number of redundancy switchovers in a defined period  Default setting:  - Time period: 1 calendar day - The value is reset every day at midnight (0:00). |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT_RESET | The reset tag resets the value of the following performance tag:  - @PRF_REDUNCANCY_SWITCHOVER_COUNT |

---

**See also**

[System messages WinCC Redundancy (RT Professional)](#system-messages-wincc-redundancy-rt-professional)

### System messages WinCC Redundancy (RT Professional)

#### Introduction

The "WinCC Redundancy" option provides the following system messages. You can read these system messages on the "System messages" tab in the "HMI Messages" editor.

| Message No. | WinCC Message Text |
| --- | --- |
| 1012200 | REDRT:@100%s@:Partner station has failed WinCC was exited on the partner server. |
| 1012201 | REDRT:@100%s@: Partner station restarted   WinCC was started again on the partner server |
| 1012203 | REDRT:@100%s@:Archive synchronization failed |
| 1012204 | REDRT:@100%s@:Internal redundancy error |
| 1012205 | REDRT:@100%s@:Connection to the partner has been interrupted The connection to the partner server is interrupted |
| 1012206 | REDRT:@100%s@:Connection to the partner has been reestablished The connection to the partner server has been reestablished |
| 1012207 | REDRT:@100%s@:Partner server - WinCC is not started It was determined at startup that WinCC is not started. |
| 1012208 | REDRT:@100%s@:Synchronization launched This message is output at the start of the archive synchronization |
| 1012209 | REDRT:@100%s@:Synchronization finished This message is output at the end of the archive synchronization |
| 1012214 | REDRT:@100%s@:User archive is being synchonized |
| 1012215 | REDRT:@100%s@: User Archive synchronization finished |
| 1012216 | REDRT:@100%s@:Archive synchronization canceled Synchronization was canceled by an additional failure |
| 1012217 | REDRT:@100%s@:Partner server project has not been activated It was determined at startup that WinCC is not activated on the partner server or is not in runtime |
| 1012220 | REDRT:@100%s@: Synchronization is not ready for all User Archives. The synchronization is not ready for all locally configured user archives, because the archive structure of the partner is different for at least one archive or synchronization is not activated on the partner. |
| 1012221 | REDRT:@100%s@: Synchronization is ready for all User Archives. The synchronization is ready for the locally configured user archives and the archive structure matches that of the partner. |
| 1012226 | REDRT:@100%s@:Partner server project has been activated It was determined at startup that WinCC is active on the partner server. |
| 1012227 | REDRT:@100%s@:Error: Partner server is not a server It was determined at startup that the configured partner server is not a server. |
| 1012240 | REDRT:@100%s@:RedundancyControl Error @1%s@ in @2%s@ causes state switch |
| 1012241 | REDRT:@100%s@:RedundancyControl: Switchover to status @1%s@ |
| 1012244 | REDRT:@100%s@: Overload during Alarm Logging online update Number of messages to be synchronized is too large. |
| 1012247 | REDRT:@3%s@:OS server (Master) @1%s@ OS server (Standby) @2%s@ Redundancy error |
| 1012248 | REDRT:@3%s@:OS server (Master) @1%s@ OS server (Standby) @2%s@ Redundancy recovered |
| 1012349 | REDRT:@1%s@:RedundancyControl: Loss of connection via network card with MAC address @ 2%s@. |
| 1012350 | REDRT:@1%s@:RedundancyControl: Connection via network card with MAC address @2%s@ has been reestablished. The connection to the partner server has been reestablished via redundant LAN. |
| 1012351 | REDRT:@100%s@:RedundancyControl: System blockage detected. Switch to Fault status. |
| 1012352 | REDRT:@100%s@:RedundancyControl: System blockage detected. Restart your computer as soon as possible. |
| 1012353 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT. However partner server is not available. |
| 1012354 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT. However server isolation is not activated. |
| 1012355 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT. However server isolation is locked by @1%s@. Reason: @2%s@ |
| 1012356 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT => server is isolated |
| 1012357 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT. However automatic restart is not activated. |
| 1012358 | REDRT:@100%s@:RedundancyControl: Status changed to FAULT. However automatic restart is locked. The network adapter is disconnected and DHCP is released. |
| 1012359 | REDRT:@100%s@:RedundancyControl: Reboot of computer disabled by @1%s@. Reason: @2%s@ |
| 1012360 | REDRT:@100%s@:RedundancyControl: Restart of the computer is canceled. The last restart took place less than @1%s @ s ago. |
| 1012361 | REDRT:@100%s@:RedundancyControl: Restart of the computer is canceled. After @1%s@ restarts no further restarts are permitted for @2%s@ s. |
| 1012362 | REDRT:@100%s@:RedundancyControl: Rebooting computer in @1%s@ s |
