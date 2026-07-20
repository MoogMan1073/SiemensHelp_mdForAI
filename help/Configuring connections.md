---
title: "Configuring connections"
package: HWCEstablCon34enUS
topics: 15
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring connections

This section contains information on the following topics:

- [Creating a new connection - overview](#creating-a-new-connection---overview)
- [Views containing information about the configured connections](#views-containing-information-about-the-configured-connections)
- [Creating a new connection graphically](#creating-a-new-connection-graphically)
- [Interactively creating a new connection](#interactively-creating-a-new-connection)
- [Working in the network view](#working-in-the-network-view)
- [Working with the connection table](#working-with-the-connection-table)
- [Changing the connection partner](#changing-the-connection-partner)
- [Setting or changing the connection path](#setting-or-changing-the-connection-path)
- [Creating an unspecified connection](#creating-an-unspecified-connection)
- [Creating UDP / FDL connections with broadcast / multicast](#creating-udp-fdl-connections-with-broadcast-multicast)
- [Specifying an unspecified connection](#specifying-an-unspecified-connection)
- [Deleting a connection](#deleting-a-connection)
- [Copying a connection](#copying-a-connection)
- [Inconsistent connections - connections without assignment](#inconsistent-connections---connections-without-assignment)

## Creating a new connection - overview

### Creating a connection - alternatives

You have the following options for creating a connection in the network view:

- Graphic connection configuration

  You drag a connection line to the connection partner or assign a new connection to the previously selected connection partners. This is a simple method for creating individual connections in the network view.   
  Missing networking is completed automatically or interactively.
- Interactive connection configuration

  Select the connecting partner you need from the list. This method is better than the graphic method if a large number of connections are to be configured.

You'll find the individual steps for this in the following chapters.

### Assigning connection path

Depending on the application, a distinction should be made between the following procedures:

- Selecting the connection endpoint in the source and target device

  The software automatically identifies the best connection path to the target device. This connection can then be called the "standard connection path". The software considers the available connection resources when selecting the path.

  The endpoint can be a CPU or a PC application.

  Note: This variant is only possible with graphic connection configuration.
- Selecting connection paths in the source and target devices

  If intended for the purpose of splitting load between several components (CPs) and possibly also different subnets, you can also specifically configure the path of a connection. You specify a connection path via the connection endpoint and the interface to the subnet.

### Requirement and result

You have created the devices with CPUs and PC applications and, if applicable, modules with communication capability (CPs) in the network view.

The result of configuration depends on the current configuration of the devices and networking in the project. You will therefore achieve the following results with the methods described in the following sections:

- Connection specified

  If both partners selected are networked in the same subnet, create a fully-specified connection using graphic or interactive selection.

  This fully-specified connection is automatically entered in the connection table of both the local device and that of the partner. The local ID and the partner ID are assigned for this connection. You will need these IDs when programming the communication instructions (value for the block parameter "ID") and the PC applications.

  Exceptions:

  - Unilateral S7 connections

    The connection partner acts as a server on an S7 connection configured at both ends. There is therefore no entry in the connection table for the partner. A connection ID is only issued for the local partner.

  The figure below shows a specified connection:

  ![Requirement and result](images/22195699083_DV_resource.Stream@PNG-de-DE.png)
- Connection unspecified

  Create unspecified connections in the following cases by only selecting the local connection partner graphically or interactively:

  - If certain connection properties need an unspecified connection. Examples: E-mail connection, FTP connection, FDL connection with free layer 2 access.
  - If one of the two partners for the selected connection type is not (yet) available, but you want to reserve a connection resource.

    ![Requirement and result](images/47041940491_DV_resource.Stream@PNG-en-US.png)

### Influence of the networking - response when networking is missing

Networking the connection partners it is necessary to ensure the uniqueness and consistency of the assigned connection parameters. If one or both partners is not networked on the same subnet, the following reactions in the graphic connection configuration must be distinguished.

> **Note**
>
> **Dialog-guided connection configuration - no automatic networking**
>
> In dialog-guided connection configuration, there is no automatic networking.

- Interfaces of the partners you want to connect are not networked, or do not have the same subnet

  The "Connect to subnet" dialog that appears provides the following options for selection:

  - Assign existing subnet

    You select a subnet from the list of existing subnets. The connection can be created consistently and can be specified.
  - "Connect to new subnet"

    The interfaces of the connection partners are connected via a new subnet. The connection can be created consistently and can be specified.
  - "Do not connect to a subnet"

    The connection is created as a specified connection, due to the missing networking the consistency cannot be assured which is why the entry appears red in the connection table. Connections are shown as dashed lines in the network view;
- Multiple interfaces / CPs on the partner - at least one of the available interfaces on the partner is not networked

  The following applies depending on how you create the connection in this case:

  - If you specify the connection only by selecting the CPU / OPC server as the connection endpoint, the connection path is specified regardless of the networking. This can lead to the response described in Case b and the selection dialog is displayed.
  - If you deliberately select the free interface on the partner that is not yet networked as the connection endpoint, the response is as described in Case a.

    The interfaces of the connection partners are connected via a new subnet. The connection can be created consistently and can be specified.

## Views containing information about the configured connections

The views described below will provide you with comprehensive access to all the information and functions regarding configuring and checking communication connections.

The view is accessed via the project navigation under "Devices &amp; Networks".

![Figure](images/47041944331_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Connection display in the network view |
| ② | Connection table |
| ③ | "Properties" tab for a connection in the inspector window |

### Benefits

The information shown in these views are always up-to-date in terms of the current user actions. This means:

- If you have selected a CPU, for example in the network view, the connection table shows all the connections created for this CPU.

  Note: You can use the connection table shortcut menu to choose between displaying all connections in the project and displaying the connections for a selected component.
- If you have selected a connection in the connection table:

  - The connection path in the network view will be shown in a graphic display when connection mode is activated.
  - The properties view in the inspector window displays the parameters of this connection.

### Connection display in the network view

The network view shows devices and their components as well as networks and communications connections.

In relation to connections, in the network view you see:

- The devices between which connections have been created.
- The devices that have unspecified connections.

The network view offers the following functions:

- Creating connections graphically
- Selecting connection paths when creating graphically

### The connection table

The connection table offers the following functions:

- Listing of the connections to an object selected in the network view (network, CPU, CP)
- Listing of all connections in the project
- Selecting a connection and the associated display of the connection in the network view and the display of the properties of a selected connection in the Inspector window;
- Changing connection partners
- Option of entering central parameters
- Display of status information;
- Starting point for interactive creation of new connections (possible if the "Display all connections" option is disabled).

### "Properties" tab for a connection in the inspector window

The properties dialog has the following meaning:

- Display and option of setting all connection parameters
- Setting the connection path automatically or manually
- Later specification of unspecified connections

## Creating a new connection graphically

### Graphically configuring connections

- In the simplest case, you only need to select the devices you want to connect. A possible connection path in the current configuration is selected and marked as "Standard connection path". The connection path is then selected such that the resources available are used as best as possible. The definition is based on the following behavior:

  - Non-networked components are networked when possible automatically to be able to create fully specified connections immediately.
  - The resources of one component are fully used up before switching to another component.
  - With connection types independent of networks (S7 connections), network types are subject to the following rule of preference: Industrial Ethernet before PROFIBUS.
- Alternatively, you can define the specific connection path - connection endpoint and interface to the subnet.

> **Note**
>
> **Creating S7 connections on the CPU 1515SP PC graphically**
>
> If you want to create an S7 connection on a CPU 1515SP PC , use the right interface of the CPU 1515SP PC "PROFINET onboard [X1]" when creating the connection graphically. This interface is connected directly to the CPU 150xS .
>
> The left interface of the CPU 1515SP PC "PROFINET onboard [X2]" is connected to the SIMATIC PC station or a Windows application and cannot be used during graphic creation of an S7 connection.

### Automatically determining connection path

To graphically create a connection via a default connection path, proceed as follows:

1. On the toolbar, click the "Connections" icon. This activates connection mode.

   ![Automatically determining connection path](images/21377330955_DV_resource.Stream@PNG-en-US.png)

   ![Automatically determining connection path](images/21377330955_DV_resource.Stream@PNG-en-US.png)
2. Select the required connection type in the drop-down list next to the icon.  
   You will then see the following response:

   - The components which can be used in your project as connection endpoints in the selected connection type are highlighted in color in the network view. These components may be CPUs or PC applications.

     ![Automatically determining connection path](images/22183517707_DV_resource.Stream@PNG-en-US.png)

     ![Automatically determining connection path](images/22183517707_DV_resource.Stream@PNG-en-US.png)
3. Select the component for the origin of the connection.
4. There are two options when creating the connection:

   - Click on the component from which the connection will originate and drag the mouse cursor to the target components in connection mode. Confirm the connection endpoint with another mouse click.

     ![Automatically determining connection path](images/22183521291_DV_resource.Stream@PNG-en-US.png)

     ![Automatically determining connection path](images/22183521291_DV_resource.Stream@PNG-en-US.png)
   - While holding down the shift button, select the target component and select the "Add new connection" command with the right mouse button.

**Note**

If you wish to exit connection mode before, press &lt;Esc&gt;, right-click the mouse or double-click into the background of the network view.

### Result

- A specified connection is created.
- The connection path is highlighted. The connection path has been set automatically in line with the available connection resources and interfaces.
- The connection is entered in the connection tables for the components (CPU/PC application).

  ![Result](images/47088548875_DV_resource.Stream@PNG-en-US.png)

### Selecting specific connection path

Proceed as follows to create a connection with an individually selected connection path:

1. On the toolbar, click the "Connections" icon. This activates connection mode.

   ![Selecting specific connection path](images/21377330955_DV_resource.Stream@PNG-en-US.png)

   ![Selecting specific connection path](images/21377330955_DV_resource.Stream@PNG-en-US.png)
2. Select the connection type you need from the drop-down list.
3. Click on the subnet interface in the device from which the connection is to be created.
4. In connection mode, hold down the mouse button, drag the cursor to the relevant interface in the target device and then release the mouse button.

   ![Selecting specific connection path](images/22196384395_DV_resource.Stream@PNG-de-DE.png)

   ![Selecting specific connection path](images/22196384395_DV_resource.Stream@PNG-de-DE.png)

   Result:

   - A specified connection is created.
   - The connection created between the endpoints will use the selected interfaces for its connection path.
   - The connection path is highlighted.
   - The connection is entered in the connection tables for the devices (CPU/PC application).

**Note**

If you wish to exit connection mode before, press &lt;Esc&gt;, right-click the mouse or double-click into the background of the network view.

### Configuring a connection when there is no or no clear network assignment

Any networking not in place will if possible be created automatically when a connection is created. A query will be made upon completion of connection configuration if unique network assignment is not possible. You will be able to choose from the existing subnets.

Example below: A query is made upon creation of a connection between stations PLC2 and PLC3, which are not yet networked.

![Configuring a connection when there is no or no clear network assignment](images/22197878667_DV_resource.Stream@PNG-en-US.png)

## Interactively creating a new connection

### Interactively configuring connections

Interactive connection configuration is a useful way to create multiple connections in one process within a station.

On the one hand, you have complete control over the selection of the connection path as the system displays all interface variants. At the same time, you have the option of leaving evaluation of available resources and thus selection of the connection path to the system.

> **Note**
>
> **Dialog-guided connection configuration - no automatic networking**
>
> In dialog-guided connection configuration, there is no automatic networking.

### The "Create new connection" dialog

The structure of the "Create new connection" dialog is shown below. The example shows networking between several stations. Connection mode is active and the first station in the list has been selected.

![The "Create new connection" dialog](images/69353012235_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drop-down list for selecting the connection type. |
| ② | Shows the possible connection partners for the connection type selected.  Choose from the following options:  - A special connection configuration in line with the connection type:   - "unspecified"   - "Broadcast"   - "Multicast" - The connection partner |
| ③ | Content area for selecting interfaces.  You will see interface combinations suitable for the configuration. Shows only those interfaces possible for the connection type selected. The status display provides additional information on whether the connection can be set up as a function of networking and the available resources. You can still create a connection even if the interfaces are not networked.   See also [Configuration limits in the connection configuration](Configuring%20devices%20and%20networks.md#configuration-limits-in-the-connection-configuration)  Example shown:  Between PLC1 and PLC4, the Gbit ports are networked, as are the PROFINET interfaces. Only these two combinations are therefore shown as completely assignable. |
| ④ | Drop-down list for selecting or entering the local ID. |
| ⑤ | Check box for display of the active connection establishment.  When you create a connection, the check box for active connection establishment is always enabled for the local side. Not every device is capable of handling the connection establishment. In this case, the partner must take over connection establishment. The check box always indicates the capability of the selected connection. |
| ⑥ | Check box for display of a connection configured at one end.  A connection configured at one end refers to a client-server relationship. The client knows the server whereas the server has no information whatsoever about the client. On a connection configured at both ends, information on the partner is available on both end points. The check box always indicates the information about the selected connection. |
| ⑦ | Shows the confirmation for setting up a new connection.  The type of connection and the two connection partners are indicated. Yellow icons indicate that the connection has been established but is not consistent. In this case, check the connection parameters. |

### Status display

| Icon | Meaning |
| --- | --- |
| ![Status display](images/69353032843_DV_resource.Stream@PNG-de-DE.png) | Interfaces are networked and connection resources are available for the selected partners. |
| ![Status display](images/69353029259_DV_resource.Stream@PNG-de-DE.png) | Interfaces are disconnected or not connected to the same subnet. |

### Procedure

Proceed as follows to interactively create a connection:

1. On the toolbar, click the "Connections" icon. This activates connection mode.

   ![Procedure](images/21377330955_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/21377330955_DV_resource.Stream@PNG-en-US.png)
2. Select the command "Add connection" in the shortcut menu of the component which is to be the connection endpoint (CPU or PC application).

   or

   With the "Display all connections" option disabled and the CPU or application selected, select the "Add connection" command in the shortcut menu of the connection table.

   The "Create new connection" dialog opens.
3. Select the connection type you want, for example "FDL connection" from the "Type" drop-down list.
4. Check the default setting for the other connection parameters displayed in the footer and correct them in line with your requirements.
5. Select the connection partner (device or CPU) in the left of the dialog.

   The interface combinations possible for the configuration together with status information will be displayed in the content area. The first interface combination to which a connection of the selected type can be assigned will be selected.
6. Leave the selection as it is or select the connection path you require.
7. Confirm the selection with the "Add" button.

   A connection is created and can be seen in the connection table.
8. If you have not yet closed the dialog, you have the alternative of continuing as follows:

   - You can create another connection of the same type to the same target device by clicking the "Add" button again.
   - Repeat the steps described above by selecting another connection type from the drop-down list or another connection partner.

**Note**

You can also change these parameters later on in the connection table or in the properties for the connection.

**Note**

Depending on the connection type selected, special connection types such as "unspecified", "broadcast" or "multicast" may be available in addition to the possible connection partners.

### Configuring connection without networking

Any networking not in place will if possible be created automatically when a connection is created. The relevant interface will be displayed as networked in the network view once the dialog is completed provided unique network assignment is possible.

Networking will not be displayed in the case of interactive connection configuration if unique network assignment is not possible. Connections created in this way are therefore not fully specified and are highlighted in red in the connection table.

## Working in the network view

### Meaning of the network view in connection mode

The network view shows devices and their components with interfaces to the subnets. In connection mode, you can make the communication paths of configured connections visible.

The following information about connections is then available:

- The devices between which connections have been created
- Which connection types have been created for a device
- The devices that have unspecified connections

The network view offers the following functions in connetion mode:

- Graphically creating connections; see also [Creating a new connection graphically](#creating-a-new-connection-graphically)
- Highlighting selected connections of a subnet;
- Highlighting connection partners.

### Highlighting connection path and partner in the network view

To display the connection partners for all or certain connection types in the network view, proceed as follows:

1. Select the "Highlight connection partners" command in the shortcut menu of the connection endpoint (CPU or PC application) whose connection partners you want to display in the network view.
2. In the following menu, select either "All connection partners" or "Select connection type..."

   The local endpoint and the endpoints of the target devices relevant for all or the selected connection type are selected. In addition, the devices display an arrow.
3. You can open a list with information on the target devices by right-clicking on the arrow in the footer of the local device. This additional function is useful in complex network configurations in which some devices are not visible.

   ![Highlighting connection path and partner in the network view](images/22076328075_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> You can display one of the connection partners which cannot be seen in the current display range of the network view. Click on the communication partner in the list that appears. Result: The display is moved such that the connection partner becomes visible.

### Highlighting/selecting the connection

You can select and highlight individual connections. This means:

- The connection is highlighted in the connection table where you can set certain properties.
- The connection is displayed in the inspector window together with all parameter assignment options.

Follow these steps:

1. Place the cursor on the subnet.
2. Select and highlight the relevant connection in the "Highlight connection" dialog that appears.

   The connection path will be displayed as a light blue dotted line.

   ![Highlighting/selecting the connection](images/22076337675_DV_resource.Stream@PNG-en-US.png)
3. Click on the dotted line.

   The color of the line will change to dark blue and the connection will be displayed in the connection table and in the inspector window.

   ![Highlighting/selecting the connection](images/47089191563_DV_resource.Stream@PNG-en-US.png)

## Working with the connection table

### Functions

As well as allowing you to create new connections interactively, the connection table provides other functions:

- List of connections to an object selected in the network view (network, CPU, CP)
- List of all connections in the project
- Selection of a connection and display of connections associated with it in the network view
- Changing connection partners
- Option for entering central parameters
- Display showing status information

### Creating new connections interactively

[Interactively creating a new connection](#interactively-creating-a-new-connection)

### Content of the connection table

You can use the connection table to display the details for all communication connections created in the project:

- Show all connections (default setting - can be selected via the shortcut menu)

  The connection table displays all connections created for the project.
- Show selected connections (recommended setting for complex projects)

  To access this display, clear the "Show all connections" option in the shortcut menu.

  The connection table shows the connections belonging to a selected subnet or selected CPU and/or CP. In other words, it's empty when none of these named objects are selected in the network view.

  Multiple objects of the same type (multiple subnets, multiple CPUs/CPs or multiple interfaces) can also be selected at the same time. The connection table then shows you all associated connections.

### Basic functions for tables

The connection table supports the following basic functions for editing a table:

- Showing and hiding specific table columns

  Select the "Show/hide columns" command in the table header in the shortcut menu.
- Changing column width manually

  Move the dividing line in the header on the right of the column.
- Optimizing column width automatically

  Select the shortcut menu command "Optimize column width" in the table header.
- Showing column meaning using tooltips.

If you want to store the layout, width and visibility of the table columns, click on the "Remember layout" function in the top right-hand of the network view.

| Icon | Meaning |
| --- | --- |
| ![Basic functions for tables](images/25385115915_DV_resource.Stream@PNG-de-DE.png) | Remember layout  Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

### Using cursor keys to move within the connection table

You can use the UP and DOWN cursor keys to select a connection from the connection table; the selected connection will be marked and highlighted in the network view when connection mode is activated.

### Changing properties of connection

You can directly edit some of the parameters displayed in the connection table. The name of the connection can, for example, only be changed in the connection table.

### Changing connection partners

You can change the connection partner of a connection as follows:

1. Select the connection.
2. Select the new connection partner from the open drop-down list in the "Partner" column.

---

**See also**

[Overview of connection diagnostics](Device%20and%20network%20diagnostics.md#overview-of-connection-diagnostics)
  
[Displaying the connection status using icons](Device%20and%20network%20diagnostics.md#displaying-the-connection-status-using-icons)
  
[Detailed connection diagnostics](Device%20and%20network%20diagnostics.md#detailed-connection-diagnostics)

## Changing the connection partner

Follow the procedure below if you need to change the connection partner for a connection already configured. The local ID and the connection type will be maintained.

Changes can only be made to connection endpoints in the connection table or in the inspector window.

### Changing connections interactively

To reach a different connection partner on a default connection path proceed as follows:

1. In the network view, select the local endpoint to which you wish to assign a new connection partner.

   The endpoint connections will be displayed in the connection table.
2. Select the desired connection in the connection table.
3. Select the new target device for the connection from the drop-down list in the "Partner" table column.

   You can alternatively select the new target device under "Connection path" in the inspector window.

**Note**

**Effect on previously configured properties**

Note that when changing the connection partner the parameter assigned properties of the connection must be reset to the pre-select.

Use the entry possibilities in the connection table or in the Inspector window if you want to change the "Properties" of the connection.

**Note**

**Effect on networking**

Subnets will not automatically be created in the absence of networking to the new connection endpoint in procedures for changing the connection partner.

## Setting or changing the connection path

Depending on the components and interfaces available within a device, connections can take different paths within the device.

Connections in the configuration will have one of the following configuration statuses in line with the status of the device configuration and will be displayed accordingly:

- Connection path closed

  Both endpoints (CPU or PC application) and the interfaces required for communication (local interface in the CPU or additional CPU) are available.

![Figure](images/22075934987_DV_resource.Stream@PNG-en-US.png)

- Connection path open

  - The connection path is not fully assignable as interfaces are missing.
  - The connection path is only specified at one endpoint because it is an unspecified connection.

![Figure](images/22060541835_DV_resource.Stream@PNG-en-US.png)

The procedure for changing or reassigning a configured connection path in a local or partner device is described below.

You can set or change the connection path in the following views:

- Inspector window - "Properties &gt; General"

### Changing the connection path in the Inspector window

To assign a different connection path to an existing connection:

1. In the network view, select the endpoint (CPU or PC application) for which a connection is to be changed.
2. In the connection table select the connection for which you want to change the connection path.

   Hint: The current connection path is highlighted in the network view if you have set the "Highlight connection" view.
3. Select the new interface in the Inspector window under " Properties &gt; General &gt; Interface". The partner is offered the interfaces that can be considered in the context of the local interface (Note: S7 connections can be established via different subnet types).

   In the network view the new connection path is highlighted.

### Assigning connection path

To assign a closed connection path to an existing open connection path:

1. Expand the device configuration to that the interfaces required for the connection type are available for both partners.
2. In the connection table, select the connection for which you want to change the connection path.

   Hint: The current connection path will be highlighted in the network view if you have set the "Highlight connection" view accordingly.
3. Activate the "Find connection path" button under "Properties &gt; General &gt; Interface" in the inspector window.

   In the network view the new connection path is highlighted.

## Creating an unspecified connection

Create unspecified connections in the following cases by only selecting the local connection partner graphically or interactively:

- When certain service or connection properties require an unspecified connection (examples: E-mail connection, FTP connection, FDL connection with the "Free layer 2 access" property).
- If you want to set up a connection to be available for communication with any connection partner.
- If one of the two partners for the selected connection type is not (yet) available, but you want to reserve a connection resource.
- If the connection partner is located outside of the project (e.g. third-party stations).
- UDP connection with broadcast / multicast:

  - See [UDP with broadcast and multicast](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#udp-with-broadcast-and-multicast-s7-300-s7-400-s7-1500)
  - See [Free UDP connection](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#free-udp-connection-s7-300-s7-400-s7-1500)

### Requirement

You must be in the network view.

### Configuring an unspecified connection graphically

To create an unspecified connection graphically, proceed as follows:

1. In connection mode, select the required connection type in the drop-down list box, for example "TCP connection".  
   ![Configuring an unspecified connection graphically](images/9324234635_DV_resource.Stream@PNG-en-US.png)

   The CPUs available for the selected connection type are selected and highlighted.
2. Click on the CPU from which a connection will be set up.
3. Move the mouse cursor within the CPU or on the interface of the CPU and confirm the connection endpoint by double-clicking the mouse.

### Result

- An unspecified connection is created. Depending on the selected endpoint - CPU or CP - the following applies for path selection:

  - endpoint CPU: The best possible local connection path will be selected automatically. See also [Creating a new connection graphically](#creating-a-new-connection-graphically)
  - endpoint CP interface: The connection path is determined by the entry.
- The unspecified connection is highlighted in the display by a short dotted line.

  ![Result](images/22195705611_DV_resource.Stream@PNG-de-DE.png)
- The unspecified connection is entered in the connection table of the device and "Unknown" is entered in the "Partner" column.

### Configuring the unspecified connection interactively

To interactively create an unspecified connection, proceed as follows:

1. Select the "Add connection" menu command in the context menu of the device (CPU) for which you want to create a connection.

   or

   With the "Display all connections" option disabled, select the "Add connection" command in the shortcut menu of the connection table.

   Result: The "Create new connection" dialog will open.
2. In the "Create new connection" dialog box select the desired connection type, e.g. "FDL connection".
3. In the top of the dialog box select the entry "Unspecified".
4. If several local interfaces are available, you can select the required interface from a list. The first row of the list displays the interface the system detected as the most suitable and this is selected.
5. Confirm the selection with the "Add" button.

   An unspecified connection will be created and will be visible in the connection table.
6. Repeat the process or exit the dialog via "OK".

### Result

- One or more unspecified connections are created.
- The unspecified connections are entered in the connection table.

  > **Note**
  >
  > Note that you can still assign parameters for special properties for each connection.

## Creating UDP / FDL connections with broadcast / multicast

### Meaning

Multicast and broadcast are special connection options that are supported by Industrial Ethernet CPs on UDP connections and by PROFIBUS on FDL connections and can be configured.

As of TIA Portal V14, the S7-1500 CPUs with firmware version V2.0.1 and higher support UDP multicast via the integrated CPU ports as well.

### Creating a connection interactively - procedure

To create a multicast / broadcast connection interactively, follow these steps:

1. Select the "Add connection" command in the shortcut menu of the component that will be the connection endpoint.

   or

   With the "Display all connections" option disabled, select the "Add connection" command in the shortcut menu of the connection table.

   The "Create new connection" dialog opens.
2. Select the connection type UDP connection/FDL connection from the "Type" drop-down list.
3. Select the connection type broadcast or multicast in the left-hand part of the dialog.

   The local interfaces possible for the configuration together with status information are displayed in the content area. The first interface to which a connection of the selected type can be assigned is selected.
4. Leave the selection as it is or select the connection path you require.
5. Confirm the selection with the "Add" button.

   A connection is created and can be seen in the connection table.
6. If you have not yet completed the dialog, you have the alternative of continuing as follows:

   - You can create another connection of the same type to the same target device by clicking the "Add" button again.
   - Repeat the steps described above by selecting another connection type from the drop-down list or another connection partner.

### Creating a connection graphically - procedure

1. First, create an unspecified UDP connection / FDL connection using the graphic connection configuration tool; [Creating a new connection graphically](#creating-a-new-connection-graphically)
2. Now make the address settings for the connection partner according to the requirements for multicast or broadcast. As an alternative, follow these steps:

   - In to the connection table, go to the "Partner" column and select the required connection type from the drop-down list; address parameters are assigned automatically.

     or
   - For UDP, enter the IP address or port directly in "General &gt; Address details". For FDL, set the PROFIBUS station address 63.

---

**See also**

[UDP with broadcast and multicast (S7-300, S7-400, S7-1500)](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#udp-with-broadcast-and-multicast-s7-300-s7-400-s7-1500)
  
[FDL connection with broadcast (S7-300, S7-400)](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#fdl-connection-with-broadcast-s7-300-s7-400)
  
[FDL connection with multicast (S7-300, S7-400)](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#fdl-connection-with-multicast-s7-300-s7-400)

## Specifying an unspecified connection

### Characteristics of the unspecified connection

For an unspecified connection depending on the connection type either some or all of the parameters that are necessary for local access to the network and for addressing the partner, will be missing.

An unspecified connection is shown as follows:

- Network view:

  The unspecified connection will be displayed in the network view as a dotted line once it has been created or selected in the connection table.
- Connection table:

  - Display in the "Partner" column: "Unknown"

An unspecified connection occurs as described below: See also [Creating an unspecified connection](#creating-an-unspecified-connection)

Below are the main two different scenarios when specifying the connection later:

- The connection partner is in the same project

  You specify the connection by the subsequent selection of components available in the project.
- The connection partner is not in the project

  You specify the connection by entering the address parameters of the communication partner available outside the project.

### Automatic supplementing of missing connection parameters

If the missing resources have been supplemented by adding components then connections will be assigned automatically if possible, and if necessary to an unspecified connection.

### Requirement

- The components of both devices have free resources for the connection type.

### Procedure in the connection table

Proceed as follows to provide an unspecified connection with the address parameters of a target device already in the project:

1. Select the CPU for which you want to specify a connection.  
   In the connection table, all unspecified connections configured for the CPU have the entry "Unknown" in the "Partner" column.
2. Select the required target device in the "Partner" column of the connection table.

### Result

- The connection is specified with the relevant address details for the connection partner.
- The new connection path is highlighted in the network view as a dotted line.

The figure below shows a specified connection:

![Result](images/22195699083_DV_resource.Stream@PNG-de-DE.png)

## Deleting a connection

You can delete configured connections via the network view or the connection table.

In the network view you can delete a highlighted connection. In the connection table you can delete one or more connections.

### Procedure in the network view

You can delete individual connections in the network view via the shortcut menu. Follow these steps:

1. Switch to connection mode.
2. Place the cursor on the subnet.

   The "Highlight connection" dialog will show the connections currently configured.
3. Select the connection to be deleted.
4. Place the cursor on the subnet again.
5. Open the shortcut menu with a right mouse click.
6. Select the "Delete" command.  
   The selected connection will be deleted in full. If the partner for a specified connection is within the project, the connection will also be deleted from the connection table of the partner.

**Note**

**Downloading connection data to a module**

Download the connection table with the deleted connection to the programmable modules affected by it.

### Procedure in the connection table / network view

You can delete one or more selected connections in the connection table via the shortcut menu. Follow these steps:

1. In the connection table, select the connections that you want to delete.
2. Open the shortcut menu with a right mouse click.
3. Select the "Delete" command**.**

   Each connection selected will be deleted in full. If the partner for a specified connection is within the project, the connection will also be deleted from the connection table of the partner.
4. Load the connection table with the deleted connections into the appropriate programmable module.

**Note**

**Downloading connection data to a module**

Download the connection table with the deleted connection to the modules affected by it.

**Note**

To delete all connections of the module you must load an empty connection table.

## Copying a connection

### Introduction

Connections are not copied singly but always in context along with the project or the device.

You can copy:

- Entire projects
- One or more devices within a project or from one project to another

### Copying a project

When you copy a project all configured connections will also be copied. No new settings are required for the copied connections as the connections remain consistent.

### Copying devices

- Copying a device within a project

  Copying individual devices produces unspecified connections and you will need to reassign the connection partners to the local node.

  If you copy a group of devices, the connections within the group will also be copied. Duplicating will however also produce duplicate connection names. Change the duplicate connection names after copying.

  You will need to network the copied devices again.
- Copying devices to another project

  You can copy one or more devices to another project. To continue editing the other project, restart the TIA Portal.

  Connections configured between the copied devices remain in the target project. You need only reassign networking in the target project.

  Copying the devices to the target project individually will produce temporarily unspecified connections. However, the communication partners will be assigned again if this is possible when the next device is added.

### Additional information

See also [Specifying an unspecified connection](#specifying-an-unspecified-connection)

## Inconsistent connections - connections without assignment

An inconsistent connection is one in which the connection data is incomplete or inconsistent; the connection is not functional in the context with the project.

Inconsistent connections cannot be loaded - operation is not possible with such connections.

In the connection table inconsistent connections are marked in red.

> **Note**
>
> **Unspecified connections**
>
> Unspecified connections are not necessarily inconsistent although they are always highlighted in red in the connection table.
>
> [Creating an unspecified connection](#creating-an-unspecified-connection)

### Possible causes for inconsistent connections

- Deletion or change of the hardware configuration.
- Missing interface network links in the project, which are necessary for a connection.
- Connection resources are exceeded
- Connections to an unspecified connection partner without partner address information.

Detailed information about the cause of the inconsistency is provided in the inspector window in the properties page of a connection; inconsistent parameters are shown in red. You can get supplemental information about these parameters by placing the cursor on the parameter.

### Examples of and remedies for inconsistencies associated with typical configuration actions

Actions are explained below that can cause configured connections to lose their assignment or be deleted.

> **Note**
>
> Note that as opposed to the S7 connections, a CP-dependent ID is assigned to the connections of the SEND/RECEIVE interface. Consequently the actions described below may require customizing of the ID, which means that the interface must also be customized in the user program.
>
> If a CP is replaced by a different CP then it must provide at least the same services and have at least the same version. This is the only way to ensure that the connections configured via the CP remain consistent and can be used.

Actions for a CP interface that can cause changes in configured connections.

| Action | Consequence for the connections | What you must do to restore the connection |
| --- | --- | --- |
| Delete the CP (module). | The connections remain intact in the connection table without assignment to a CP.  The assignment to the CPU / PC application remains. | After you have placed and networked a CP in the hardware configuration:  1. Assign the CP to the connection; 2. Check the module start address LADDR and customize if necessary in the user program. 3. Customize the connection IDs in the user program. 4. Reload the connection configuration into the CP. |
| Delete the device. | All the connections to this device are canceled in the project.  - Connections remain as unspecified connections on the partner. - Connections without a connection partner are completely deleted. | Reconfigure the device and connections.  Either reassign unspecified connections or delete them. |
| Change the subnet assignment of the CP. | The connections that were assigned via the CP remain but may be inconsistent. | Where necessary, reassign connections. |
