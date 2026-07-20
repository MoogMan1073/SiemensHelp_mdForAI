---
title: "CPs for PC station 1.0"
package: HWCSimNetPCCPenUS
topics: 33
source: Siemens TIA Portal Information System (offline help, en-US)
---


# CPs for PC station 1.0

This section contains information on the following topics:

- [PC station](#pc-station)

## PC station

This section contains information on the following topics:

- [SIMATIC NET PC software for PC communications processors](#simatic-net-pc-software-for-pc-communications-processors)
- [Slot rules for a PC station](#slot-rules-for-a-pc-station)
- [Ethernet PC CPs](#ethernet-pc-cps)
- [PROFIBUS PC CPs](#profibus-pc-cps)
- [Networked PC configurations](#networked-pc-configurations)
- [PC CP settings that do not depend on the protocol or the network](#pc-cp-settings-that-do-not-depend-on-the-protocol-or-the-network)

### SIMATIC NET PC software for PC communications processors

#### SIMATIC NET PC software for PC communications processors

The use of the SIMATIC NET PC software versions listed below is recommended for the following communications processors depending on the operating system:

- CP 1613, CP 1613 A2, CP 1623, CP 1628
- CP 5613, CP 5613 A2, CP 5614, CP 5614 A2, CP 5623, CP 5624

You should use the following versions of the SIMATIC NET PC depending on the operating systems:

- Windows 8 (Professional, Enterprise), 32- and 64-bit and Windows Server 2012   
  DVD "SIMATIC NET PC Software" V12
- Windows 7 (Professional, Enterprise, Ultimate), 32- and 64-bit and Windows Server 2008 R2

  DVD "SIMATIC NET PC Software" V12
- Windows XP, Windows Server 2003 and Windows Server 2008, 32-bit

  CD "SIMATIC NET, PC Software", Edition 2008 + SP6, version number V7.1.6

### Slot rules for a PC station

#### Introduction

Components such as CPs, PC-based user programs for connection configuration and OPC servers can be plugged into slots (index) 1 to 32. Certain slot rules apply for PC stations.

#### Inserting an OPC server

In PC stations, OPC servers can be inserted for OPC clients that access remote automation systems via configured connections:

- A maximum of one OPC server can be inserted in a PC station for OPC clients.
- If an OPC server is plugged into a PC station, a CP can be assigned to it.

Other standard applications can be used instead of the OPC server or in addition to an OPC server.

#### Plugging components

The following rules apply to index numbering and plugging components into the PC station:

- The index numbers 1 to 32 can be assigned.
- The first plugged component always gets index 1.
- Additional plugged components get the next free index number.
- If a component is deleted, the index numbers of the other modules remain unchanged. There may be gaps in index numbering for this reason.
- Inserting components between existing components is permissible.
- The following applies for inserting components when components are already present:

  - If free index numbers are available between two components, the first free index will be assigned.
  - If no free index numbers are available between two components, the index of all subsequent components will be incremented by one number until the first free index.

    A component with index 32 can, in this way, be shifted to the area of unplugged modules. You can therefore expand the PC station without losing components with important settings in the event of over-allocation.

#### Inserting submodules

WinLC RTX supports as a sub-module

- a maximum of one CP 5611/21 card or an integrated CP 5611/21 interface
- a maximum of one PROFINET interface (CP 1616, CP 1604, among others)
- a maximum of four sub-modules altogether. From the four submodules, there may be any number of CP 5613 communication interfaces.

The following rules apply when a component has submodules:

- A controller contains a fixed number of free slots.
- Free slots are shown in the graphic and tabular device view.
- Submodules can only be inserted on free sub slots.
- A subslot is freed when a submodule is deleted.
- Subslots do not reserve an index number.

### Ethernet PC CPs

This section contains information on the following topics:

- [Subnet addressing with CP 1613, CP 1623 and CP 1628](#subnet-addressing-with-cp-1613-cp-1623-and-cp-1628)
- [Pulling and plugging Ethernet PC CPs](#pulling-and-plugging-ethernet-pc-cps)
- [OPC configuration (Ethernet CP)](#opc-configuration-ethernet-cp)
- [Ethernet port](#ethernet-port)
- [Web](#web)
- [Options for setting protection](#options-for-setting-protection)
- [Setting parameters for access protection](#setting-parameters-for-access-protection)
- [Customer-specific adaptations for CP 1626](#customer-specific-adaptations-for-cp-1626)
- [Customer-specific adaptations for CP 1604/CP 1616 as of V2.7](#customer-specific-adaptations-for-cp-1604cp-1616-as-of-v27)

#### Subnet addressing with CP 1613, CP 1623 and CP 1628

CP 1613, CP 1623 and CP 1628 are communications modules with a microprocessor. For the secure handling of communications connections these are processed on the module. For diagnostic purposes (SNMP, DCP) the protocol stack in your PC is used. To allow both protocol stacks to communicate with the same partners (IE and NDIS access), we recommend that you place both protocol stacks of a module in the same subnet.

#### Pulling and plugging Ethernet PC CPs

##### Pulling and plugging Ethernet PC CPs

Ethernet modules, for example USB network adapters, must already be plugged and activated when the system starts. If Ethernet modules are deactivated or do not exist when the system starts or they are pulled and plugged again during operation, the "Available devices" functionality does not display all the nodes in STEP 7. This also applies to the change of docking stations when the Ethernet module is not plugged into the notebook but rather into the docking stations.

Activate the deactivated Ethernet modules by using "Control Panel &gt; Network Connection" and reboot the system. Also reboot the system if Ethernet modules were plugged during operation or if the docking station with the Ethernet module was changed during operation.

#### OPC configuration (Ethernet CP)

##### Reference

Setting the OPC configuration for the PC Ethernet CP in the "Properties &gt; General &gt; OPC configuration" parameter group.

The parameter group exists if an OPC server is configured in the PC station.

##### "Access via the OPC server" option

Enable the module for operation via an OPC server configured on the device.

##### "Automatic mode of the PROFINET IO controller" option

If you select this option, the operating mode of the PROFINET IO controller is set automatically to OPERATE.

In the OPERATE mode, the PROFINET IO controller has access to the connected PN IO system.

The option can be selected if the option "Access via the OPC server" was selected.

- Option enabled (default setting)

  If you select this option, the PROFINET IO controller is changed to the OPERATE mode as soon as there is access to an IO device. This access can either be over the OPC Item interface or the IO Base user programming interface.

  No prior calls are required to initialize the operating state.
- Option disabled

  Prior to data access, the PROFINET IO controller needs to be set to the OPERATE mode. To do this, use suitable initialization calls for an interface in the user program.

  The interface in the user program can be an OPC item interface or an IO-Base user programming interface.

#### Ethernet port

This section contains information on the following topics:

- [Time synchronization](#time-synchronization)
- [Advanced options](#advanced-options)

##### Time synchronization

###### Time synchronization

Here, you decide whether or not the CP processes time frames.

The following two options are available depending on where the time master is located

- Master (time transmitter)

  Time messages can come from the PC station and be forwarded to the subnet (LAN). A PC application that performs the time master function transfers the time information to the CP in a job.
- Slave (time recipient)

  Time messages can come from the subnet (LAN) and be forwarded to the station. A PC application can read the transferred time using a suitable job.

If you are running several CPs in your station, you should consider the flow of time frames in relation to the time-of-day master since you can pass time frames from one network to another network using the function described here.

If there are several CPs that are connected to the same network in a station, only **one** of these CPs may forward the time synchronization messages.

##### Advanced options

This section contains information on the following topics:

- [Keep-Alive connection monitoring](#keep-alive-connection-monitoring)
- [Notes on connection release monitoring](#notes-on-connection-release-monitoring)

###### Keep-Alive connection monitoring

###### Reference

Making special settings for the Ethernet interface in the "PROFINET/Ethernet interface &gt; Advanced options &gt; Interface options" parameter group

###### Keep-Alive connection monitoring

If the keepalive mechanism is activated, keepalives are sent for connections via TCP/IP. This ensures that connections are terminated if one of the communication partners fails and that connection resources are released again.

Depending on the module type, there are two options for the setting:

- Enable/disable connection monitoring with a fixed interval time

  You can enable and disable the mechanism for connection monitoring. An interval time of 30 seconds is specified for the module; this is the interval at which the keepalives will be sent to the partner of a communication connection.

  - Keepalive disabled: 0 seconds
  - Keepalive enabled: Interval time permanently set to 30 seconds
- Configurable interval time for monitoring frames

  Here, you can set the interval time in seconds with which keepalives are sent to the communication partner:

  - Range of values: 0 .. 999999
  - Function switched off: 0
  - Default: 30

###### Notes / recommendations:

Note that the keepalive mechanism can cause subordinate connections (for example, an ISDN telephone connection) to be maintained even though user data is not actually being transferred. If this is not desired, follow these steps:

- Disable the monitoring mechanism (interval time = 0)

  or
- Set the interval so high that the underlying connection is terminated before a keepalive frame is sent when there is no data traffic.

> **Note**
>
> **Modules of other manufacturers**
>
> When using modules of other manufacturers, refer to their information regarding keepalive settings.

###### Notes on connection release monitoring

###### Relationship to connection configuration

The possible time monitoring setting in this case relates to the time monitoring that can be set in the connection configuration as follows: The lower value is valid.

Time monitoring can be configured in the connection configuration in "Properties &gt; Details on connection setup".

#### Web

This section contains information on the following topics:

- [Web server on the PC CP](#web-server-on-the-pc-cp)

##### Web server on the PC CP

###### Reference

Configuration of access to the Web server on the PC CP in the "Web server" parameter group

###### "Enable Web server on this module" option

The CP provides you with the functionality of a Web server for access via port 80 using a Web browser. Certain HTML pages with CP information and diagnostic functions are stored in a memory area of the CP for this.

Enable this option in order to be granted access to these HTML pages.

- Option enabled

  Enable this check box so that the Web server of the CP is started after downloading the configuration data. You can then read out all the information available on the CP Web pages using a Web browser.
- Option disabled

  If the check box is disabled, access to information provided by the CP Web pages is restricted. Disabling may be suitable in certain operating situations to keep additional resources free on the CP.

  The following pages are not displayed:

  - Diagnostics buffer
  - Module information
  - Topology

###### Automatic update

If the check box is selected, the Web pages are updated automatically at the interval set in "Update interval".

The Identification Web page is excluded from the automatic update.

###### Selecting languages

Select the languages for language-dependent texts to be downloaded to the CP. The number of selectable languages is CP dependent. The texts in the diagnostics buffer, for example, are language dependent.

You should also remember that the languages you select here must be installed in the project. You will find the selection of project languages in the project tree in "Languages &amp; Resources"

If the languages you select were not previously installed, the Web server can only display texts in your default language.

#### Options for setting protection

##### Protection level

Below, you will see how to use the individual access levels of the CP.

CPs such as the CP 1626 provide various access levels to restrict access to certain functions.

The parameter assignment for the access levels is made in the table. The green check mark in the columns on the right of the particular access level indicate the maximum possible operations without knowing the password for this access level. If you want to use the functions in the check boxes without a check mark, you will need to enter a password.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Configuring an access level does not replace the know-how protection**  Setting the parameters for access levels prevents unauthorized changes to the CP by restricting the download rights. Blocks on the memory card are, however, neither write nor read protected. To protect the code of blocks on the memory card, use the know-how protection. |  |

##### Default reaction

The default access level is "Full access (no protection)". Every user can read and modify the hardware configuration and the blocks. No password has been set and no password is required for online access.

##### The individual access levels

With a CP, you can set the following access levels:

- Full access (no protection): The hardware configuration and the blocks can be read and modified by anybody.
- Read access: With this access level, without entering the password, only read access to the hardware configuration and the blocks is possible; in other words, you cannot download the blocks or hardware configuration to the CP without entering the password. Without the password, writing test functions and firmware updates are also not possible.
- No access (complete protection): If the CP is completely protected, neither read nor write access to the hardware configuration and blocks is possible.

With the legitimization provided by using the password, you once again have full access to the CP.

##### Reaction of a password-protected CP during operation

Protection of the CP is effective after the settings have been loaded on the CP.

Before an online function is executed, a check is made to establish whether or not it is permitted. If there is password protection, you will be prompted to enter the password.

Example: The module parameters were set for read access and you want to use the "Modify tags" function. Since this is write access, the set password must be entered before the function can be executed.

The functions protected by the password can only be executed by one PG/PC at any one time. Another PG/PC cannot log on.

The access rights to the protected data apply for the duration of the online connection or until the access rights are canceled again with "Online &gt; Delete access rights".

Each access level allows unrestricted access to certain functions even without entering a password, for example identification using the "Accessible devices" function.

#### Setting parameters for access protection

Below you will see how to set an access level for a CP and enter passwords.

You can enter several passwords for a CP setting up different access rights for different user groups.

The passwords are entered in the table so that precisely one access level is assigned to each password.

How the password takes effect is shown in the "Access level" column.

**Example:**

You select the access level "No access (complete protection)" and enter your own password for each of the access levels higher up the table.

For users that do not know any of the passwords, the CP is completely protected.

For users who know one of the set passwords the effect depends on the table row in which the password is located:

- The effect of the password in row 1 (full access (no protection)) is as if the CP was unprotected. Users that know this password have unrestricted access to the CP.
- The effect of the password in row 2 (read access) is as if the CP was write-protected. Despite knowing the password, users that know this password only have read access to the CP.
- The effect of the password in row 3 (complete protection) is as if the CP was write and read protected. Users that know this password only have read access to the CP.

**Procedure**

Follow the steps below to set the parameters for the access levels of a CP:

1. Open the properties of the CP in the Inspector window.
2. Open the "Protection" entry in the navigation panel.  
   A table with the possible access levels is displayed in the Inspector window.
3. Select the required access level in the first column of the table. The green check mark in the columns on the right of the particular access level indicate which operations are still possible without entering the password.
4. If you have selected an access level other than "full access":

   - Assign a password for full access in the "Password" column in the first row (full access).
   - Repeat the selected password in the "Confirm password" column to protect against incorrect entries.
   - Make sure that the password is adequately secure; in other words, that it does not include a pattern that can be machine read!
   - The entry of the password in the first row "Full access (no protection)" is obligatory and allows a user who knows the password unrestricted access to the CP regardless of the selected access level.
5. As necessary, assign other passwords to the required access levels if the selected access level permits this.
6. Download the hardware configuration so that the access level takes effect.

**Result**

The hardware configuration and the blocks are protected from unauthorized online access according to the set access level. If an operation cannot be executed without a password due to the set access level, a dialog appears prompting entry of a password.

#### Customer-specific adaptations for CP 1626

##### General

With the "Customer-specific adaptations" a device manufacturer can replace the SIEMENS-specific information with any self-selected information. This information is also exported to the GSDML file.

##### PROFINET vendor ID and PROFINET device ID

These parameters are applied for from the PI (PROFIBUS International) for the specific manufacturer and can then be entered here.

##### Article number

In this input box, you can enter any article number.

##### Product family, vendor name, product name and software version

These parameters are also used in WEB user interfaces and in the SNMP protocol and can be entered here.

##### GSD bitmap file

In this input box, you can specify the name of the GSD bitmap export file that you create with the input. The bitmap format is preset as default and does not need to be entered.

##### Assigning RT or IRT functionality

As of version V1.1 you can select between the two options "RT" and "IRT". The selected option is exported with the GSDML file regardless of the setting in "Parameter assignment of PN interface by higher-level IO controller" in the dialog "Operating mode".

#### Customer-specific adaptations for CP 1604/CP 1616 as of V2.7

##### General

With the "Customer-specific adaptations" a device manufacturer can replace the SIEMENS-specific information with any self-selected information. This information is also exported to the GSDML file.

##### PROFINET vendor ID and PROFINET device ID

These parameters are applied for from the PI (PROFIBUS International) for the specific manufacturer and can then be entered here.

##### Article number

In this input box, you can enter any article number.

##### Product family, vendor name, product name and software version

In this input box, you can enter any names.

##### GSD bitmap file

In this input box, you can specify the name of the GSD bitmap export file that you create with the input. The bitmap format is preset as default and does not need to be entered.

##### Assigning RT or IRT functionality

As of version V2.8 you can select between the two options "RT" and "IRT". The selected option is exported with the GSDML file regardless of the setting in "Parameter assignment of PN interface by higher-level IO controller" in the dialog "Operating mode".

### PROFIBUS PC CPs

This section contains information on the following topics:

- [Operating PROFIBUS CPs in computers with STEP 7 V5.5](#operating-profibus-cps-in-computers-with-step-7-v55)
- [Firmware download for S7-300/400 PROFIBUS CPs](#firmware-download-for-s7-300400-profibus-cps)
- [LSAP configuration](#lsap-configuration)
- [OPC configuration (PROFIBUS CP)](#opc-configuration-profibus-cp)
- [Configuring the LDB file](#configuring-the-ldb-file)

#### Operating PROFIBUS CPs in computers with STEP 7 V5.5

##### Operating PROFIBUS CPs in computers with STEP 7 V5.5

If both STEP 7 V5.5 and STEP 7 Professional are installed on a computer and STEP 7 V5.5 is removed, the setup repair function of STEP 7 Professional must be run before the following communications processors can be used as network adapters for downloading firmware:

- CP 561x, CP 5611 A2, CP 5612, CP 5613 A2, CP 5614 A2
- CP 5621, CP 5622, CP 5623, CP 5624
- CP 5711

#### Firmware download for S7-300/400 PROFIBUS CPs

##### Firmware download for S7-300/400 PROFIBUS CPs via CP 5612 or CP 5622

If the required interface parameter assignment "FWL" or "FWL_FAST_LOAD" is not available for the firmware download, follow these steps:

1. Open the "Set PG/PC interface" program. You can find the program in the Control Panel of your Windows operating system.
2. Select the interface parameter assignment depending on the operating system and then copy this:

   - For 32-bit operating systems:

     "CP5612(PROFIBUS)" / "CP5622(PROFIBUS)"
   - For 64-bit operating systems:

     "CP5612.PROFIBUS.1" / "CP5622.PROFIBUS.1"
3. Depending on your requirements, give the copy one of the following names:

   - For 32-bit operating systems:

     CP5612(FWL) / CP5622(FWL)

     CP5612(FWL_FAST_LOAD) / CP5622(FWL_FAST_LOAD)
   - For 64-bit operating systems:

     "CP5612.FWL.1" / "CP5622.FWL.1"

     "CP5612.FWL_FAST_LOAD.1" / "CP5622.FWL_FAST_LOAD.1"
4. Open the properties of the entry and make the following settings in the "PROFIBUS" tab:

   - Select the check box for "PG/PC is the only master on the bus".
   - Assign the value "0" to the address.
   - Set the value 187.5 Kbps (or the value 1.5 Mbps for FWL_FAST_LOAD) as the transmission speed.
   - Change the "Highest device address" to the value 126.
   - Change the profile to "Universal (DP/FMS)".
5. Exit the "Set PG/PC interface" program.

Result:

The configured interface parameter assignment is created and is then available in the firmware loader.

#### LSAP configuration

##### Reference

Setting the LSAP configuration for the PC PROFIBUS CP in the "Properties &gt; General &gt; LSAP configuration" parameter group.

##### Reserving LSAPs

Reserve LSAPs (Local Service Access Point) for other protocols used on the CP.

Example FDL connections: The FDL protocol uses LSAPs that must not be used by other protocols at the same time.

To reserve an LSAP, select the number belonging to the LSAP in the displayed list.

##### FDL connections

LSAPs that have already been used in FDL connections are shown as being disabled.

Display the local LSAP and the partner LSAP in the connection table to be able to check which connection uses which LSAP.

As default, these values are not displayed. To show them, open the shortcut menu in the header bar of the connection table. Click the Show/hide” menu item and select in the list “Local LSAP” and “Partner LSAP”.

The LSAPs are also shown in the connection properties under “Address details”. Here, you can, when necessary, also change the LSAP used.

#### OPC configuration (PROFIBUS CP)

##### Reference

Setting the OPC configuration for the PC PROFIBUS CP in the "Properties &gt; General &gt; OPC configuration" parameter group.

The parameter group exists if an OPC server is configured in the PC station.

##### "Access via the OPC server" option

Enable the module for operation via an OPC server configured on the device.

##### "Set DP master to OPERATE automatically" option

If you select this option, DP mode starts automatically when the OPC server starts up.

##### Activity monitoring of the CP enabled - "DP watchdog" option

If the OPC server no longer accesses the DP interface (due to an error), the module reacts as follows if the watchdog is activated: Data with the value 0 (substitute values) is sent to all DP slaves assigned to the OPC server.

Selectable parameter:

- Timeout of the DP watchdog

  If the watchdog is activated, the substitute values are transferred if there is no further access to the DP interface within the time set here.

  Default: 6000 ms

##### "Diagnostics monitoring" option enabled

If diagnostics monitoring is enabled, the OPC server itself monitors the diagnostics flag when inputs and outputs are accessed and evaluates the diagnostics data of DP standard slaves. If errors or problems are detected in the diagnostics data, access to the inputs and outputs of the DP slaves is prevented for the lock time set here; read and write jobs are therefore acknowledged with an error.

Selectable parameter:

- Lock time for Read / Write

  Default: 500 ms

##### Error wait time for DP C1 jobs

Here, you specify an error wait time for the DPC1 services (acyclic transfer as DP master class 1).

Default: 15000 ms

##### OPC server functions for DP master class 2

Here, you can enable the OPC server functions for DP master class 2. The settings here relate to the data record functions according to DP master class 2.

A 2-level option is available:

- Enable data record functions

  With the data record functions, device-specific information can be read out or parameters can be written. With this option, you enable the OPC server that supports this function.
- Operate in PROFIdrive mode

  If you select this extra option, the PROFIdrive bus server is enabled. As a result the data record functions can be used (only) in the special PROFIdrive mode.

Selectable parameter:

- Connection establishment timeout

  If the request to establish a connection is not responded to by the communications partner within the time set here, OPC jobs are aborted with an error message.

  Since due to the structure of the network some time may be necessary before a connection can be established successfully, the connection establishment timeout should be longer than the job timeout (refer to the error wait time for asynchronous jobs).

  Default: 15000 ms
- Error wait time for asynchronous jobs

  If a read or write job sent to a partner device is not responded to within the time set here, the pending OPC jobs are aborted with an error message.

  Default: 15000 ms

#### Configuring the LDB file

##### Reference

Setting the LDB configuration for the PC PROFIBUS CP in the "Properties &gt; General &gt; LDB configuration" parameter group.

> **Note**
>
> **Version of the SIMATIC NET PC software**
>
> The LDB file can only be used for CPs with the SIMATIC NET PC software up to the version May 2000.

##### Generating LDB file (applies only to CP is with firmware &lt; V6.0 SP5 or up to SIMATIC NET PC software May 2000)

The configuration of the DP master system must be exported to an LDB file (loadable database) when saving and compiling. This file contains the DP project information. It is required by the DP system attachments for PG/PC such as SOFTNET or CP 5614 in the PC stations.

> **Note**
>
> **LDB file and identifying the input/output addresses of the DP modules**
>
> The addresses of the input/output areas of the DP slaves are acquired automatically in ascending order based on the PROFIBUS address of the DP slaves and on the basis of the inserted DP modules and entered in the LDB file.
>
> Address information or address changes to the input/output addresses of the DP slaves in the DP master system configured here therefore have no effect on the address information stored in the LDB file.

### Networked PC configurations

This section contains information on the following topics:

- [Configuration dialog box](#configuration-dialog-box)
- ["Target computer configuration" dialog box](#target-computer-configuration-dialog-box)
- ["Configure: selected target computer" dialog box](#configure-selected-target-computer-dialog-box)
- [Status symbols during configuring](#status-symbols-during-configuring)

#### Configuration dialog box

##### Reference

You select the " Online &gt; Configure PC station online" menu command for a selected PC station.

You transfer the selected configuration for a PC station or display its current configuration with the highlighted dialog.

##### Requirements

The "SIMATIC NET PC Software" DVD must be installed on your target computer and the configuration computer.

If more than one communication module is present on the configuring computer or the target computer, you must first specify the particular module for the configuration operation. The SIMATIC Shell program is available for this purpose.

If you have specified the module for the configuring computer or if only one communication module is present, the local network connection is already displayed and cannot be changed.

Provided you have selected the target computer in your STEP 7 project and there is an explicit assignment to the accessible computers, the "Accessible target computer" and "Target computer" fields are also preassigned accordingly and do not have to be changed.

> **Note**
>
> **SIMATIC Shell**
>
> The "SIMATIC Shell" program is installed with the SIMATIC NET PC software products. Note the documentation on the SIMATIC NET PC software.

##### Follow these steps:

1. From the drop down list box, select the network connection to be used to address the target computer.
2. Click the "Update" button to determine the accessible computers again.
3. In the "Accessible computers" list, select the desired target computer or enter the name of the target computer directly in the "Target computer" field. The designation of the target computer is the same as the computer name in Windows.
4. Now select one of the following procedures:

   - Display the current configuration of the selected target computer: Click the "Display..." button for this purpose.
   - Download the configured configuration to the target computer: Click the "Configure..." button for this purpose.
5. Note any messages that appear following configuration.

##### Assigning the network connection and target computer

If you do not want to use any preassignments or there is no preassignment, start by following these steps:

1. If necessary, disable the "Use configured target computer" option.
2. From the drop down list box, select the network connection to be used to address the target computer.
3. Click the "Update" button to determine the accessible computers again.
4. In the "Reachable computers" list, select the required target computer. As an alternative, enter the name of the target computer directly in the "Target computer" box. The designation of the target computer is the same as the computer name in Windows.

##### Configuring the target computer

Continue as follows:

1. Choose between the following procedures:

   - Display the current configuration of the selected target computer: Click the "Display..." button for this purpose.
   - Download the configured configuration to the target computer: Click the "Configure..." button for this purpose.
2. Note any messages that appear following configuration.

**Tip:**

You can also access the functions described for the buttons by right-clicking.

**General notes**

Note that after the start of the configuration dialog, changes will not be detected on the local computer. The settings or configuration data detected during the startup are valid. This affects the following actions:

- Enabling or disabling the network adapters.
- Changes in the STEP 7 configuration of the PC station.

#### "Target computer configuration" dialog box

This dialog box shows the current configuration including modules and applications.

Here, you can compare a current configuration with a configured one.

##### Station

The station name is shown here.

The station name can be the same as the computer name of the target computer if the target station has not yet been configured with a new name after installation of the SIMATIC NET PC software. Upon booting, the computer name is initially transferred as the station name.

---

**See also**

[Status symbols during configuring](#status-symbols-during-configuring)
  
[Configuration dialog box](#configuration-dialog-box)

#### "Configure: selected target computer" dialog box

This dialog box shows the configuration, as currently configured, for the selected target computer including modules and applications.

You can initiate the transfer for the initial configuration or configuration change from here.

When the dialog box is opened, a check is made to determine whether the configuration, as configured, is valid for transfer to the target computer and, thus, can be transferred.

##### Station

The station name is shown here.

The station name can be the same as the computer name of the target computer if the target station has not yet been configured with a new name after booting. Upon booting, the computer name is initially transferred as the station name.

##### Checking and adopting the configuration, as configured

Here, you can check the configuration, as configured, before carrying out the final data transfer.

The information bar below the configuration list indicates whether or not the configuration can be performed. For this purpose, the existing physical configuration must match the configuration, as configured.

Note the symbols that indicate special circumstances.

After you have checked the displays and initiated the transfer (OK button), you will be prompted again to confirm the transfer.

##### When the configuration is rejected

The configuration cannot be transferred in the following cases:

- Configured modules are not present in the PC station.
- Configured modules cannot be explicitly assigned (see assignment rules below).
- The configuration, as configured, exceeds the permissible quantity framework for the PC station.
- A connection to the PC station cannot be established.

  This can be due to the fact that a firewall configured in the PC station blocks access to Port 102, which is used by STEP 7. Enable Port 102 in the PC station for TCP.

Review the notes or messages in the "Error" and/or "Status" fields! For example, you receive warnings if the assignment would cause a change in the previous configuration (example: an already configured module is moved to a different index).

If you double-click the message text, a window with further information regarding the message is displayed.

##### Assignment rules

During the import, a check is made to determine whether the modules can be assigned and, thus, transferred.

- The specified modules must be present.
- If multiple modules (e.g., PROFIBUS CPs) are found, an attempt is made to make an assignment:

  - Based on the parameter assignment string assigned to the module (assigned in STEP 7)
  - Based on the address (PB address, MAC/IP address)
  - Based on compatibility (range of functions)

    > **Note**
    >
    > **Softnet-CPs**
    >
    > Note that only 1 Softnet-CP (PROFIBUS or Industrial Ethernet) at a time may be present in the configuration!

---

**See also**

[Status symbols during configuring](#status-symbols-during-configuring)
  
[Configuration dialog box](#configuration-dialog-box)

#### Status symbols during configuring

##### "Status" column

Note the additional information in the "Causes" column.

!["Status" column](images/5773538059_DV_resource.Stream@PNG-de-DE.png)

Error: Component cannot be assigned/transferred or is not installed

!["Status" column](images/5773559179_DV_resource.Stream@PNG-de-DE.png)

Warning: Assignment was adapted or is not unique.

##### Information bar below the configuration list

A group message containing information about the import operation is output in the information bar:

![Information bar below the configuration list](images/5773538059_DV_resource.Stream@PNG-de-DE.png)

Configuration cannot be performed

![Information bar below the configuration list](images/5773559179_DV_resource.Stream@PNG-de-DE.png)

Configuration can be performed, but with warnings: Assignment of individual components was adapted or is not unique.

![Information bar below the configuration list](images/5773567499_DV_resource.Stream@PNG-de-DE.png)

Configuration cannot be performed

---

**See also**

["Configure: selected target computer" dialog box](#configure-selected-target-computer-dialog-box)

### PC CP settings that do not depend on the protocol or the network

This section contains information on the following topics:

- [XDB configuration](#xdb-configuration)
- [Setting the interface parameter assignment](#setting-the-interface-parameter-assignment)

#### XDB configuration

##### Reference

Setting the XDB configuration for the a PC station in the "Properties &gt; General &gt; XDB configuration" parameter group.

##### XDB configuration

- Compatibility - "S7RTM is installed" option

  When you configure a new PC station, the check box is enabled. In this case, a runtime station manager (S7RTM) is required on the target PC station. The target PC station must be configured with the Station Configuration Editor (SIMATIC NET PC software as of approximately 7/2001).

  If the check box is disabled, configuration files are generated that can be interpreted by "older" PC stations.
- Storage location of the configuration file

  The configuration with the connection descriptions for the SIMATIC PC station is stored in a configuration file (*.XDB) when you save and compile. You then install this file on the relevant PC station.

  With the "Browse" button, you can change the default path for the configuration file.

  The relative path information (.\...) relates to the folder in which the current project is stored (&lt;Install dir&gt;\S7proj\&lt;project&gt;\XDB). If you enter an absolute path (for example C:\...), remember that the access only works as long as the project remains in the current environment.

#### Setting the interface parameter assignment

##### Checking the interface parameter assignment

When you take the PC communications card from the hardware catalog and place it in a rack, it is assigned a suitable interface parameter assignment.

The valid parameter assignment can be recognized based on the information on the module type in the module catalog (name of the module and number of configurable modules of the same type) and the existing already configured modules (assignment of the board number).

If several CPs of the same type are configured in the station, the module names have an additional consecutive number added to them – the board number. From the available drop-down list, you can see the permitted entries and, if necessary, select them.

In special cases, for example when you change the module arrangement of identical modules in the PC station, it may be necessary to adapt the interface assignment here; changing the arrangement means the actual hardware and not the "virtual" slot in HW Config.

> **Note**
>
> **Interface parameter assignment on the target system (PC system)**
>
> Make sure that the same interface parameter assignment is used in the target system (PC station) as you specify here. Otherwise, you will have an interface conflict in the station after loading the configuration file.

> **Note**
>
> **Checking on the target system**
>
> Use the Setting the PG/PC Interface function to check the settings on the target system (PC station). You will find this in the Windows Control Panel. In the "Access path" tab, you will see which interfaces are configured and whether conflicts exist.
