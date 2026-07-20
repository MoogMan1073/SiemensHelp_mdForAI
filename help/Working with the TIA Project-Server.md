---
title: "Working with the TIA Project-Server"
package: PEProServenUS
topics: 49
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with the TIA Project-Server

This section contains information on the following topics:

- [Introduction to the project server](#introduction-to-the-project-server)
- [Basics of the project server](#basics-of-the-project-server)
- [Settings for working with the project server](#settings-for-working-with-the-project-server)
- [Set network profiles for project server](#set-network-profiles-for-project-server)
- [Supported network configurations for the project server](#supported-network-configurations-for-the-project-server)
- [Installing and uninstalling the project server](#installing-and-uninstalling-the-project-server)
- [Configuring and managing the project server](#configuring-and-managing-the-project-server)

## Introduction to the project server

### Introduction

The TIA Portal enables you to work conveniently with the TIA Project Server, hereinafter referred to as "Project Server".

You can use the functionality of the project server for working with Multiuser Engineering, with Multiuser Commissioning and with Exclusive Engineering.

In addition to the dedicated project server, a local project server with limited functionality is also available.

Using the project server, you manage the server projects and server libraries that you edit with Multiuser Engineering and Exclusive Engineering in the respective local sessions.

### TIA Project Server: Installation

You can install the TIA Project Server from V1.0 as follows:

- Standalone via an independent installation process without the TIA Portal.
- As part of the TIA Portal installation.

  When installing with TIA Portal, the TIA Project Server version released for this purpose is always installed.

  TIA Project Server versions that are released afterwards are also released for this TIA Portal version as long as there are no new TIA Portal versions.

  Information for which TIA Portal versions a TIA Project Server version is released can be found in this section:

  "[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)"

The installation of the server requires specific ettings in the Windows firewall and may require a certificate.

You need administrator rights to install and configure the project server.

After the installation, you configure the project server using the Power-Tools and start the server.

More information:

- "[Installing and uninstalling the project server](#installing-and-uninstalling-the-project-server)"
- "[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)"

### Properties of the project server

The project server has the following properties:

- The project server is configured and administered by an administrator with the supplied power tools.
- The project server is available to all editors of a server project or a server library depending on their rights and it can also be accessed from the outside.
- The project server can be started and administered outside the TIA Portal.
- You configure and manage the connections from the project server to TIA Portal via the settings in the TIA Portal.

  In the TIA Portal, call the settings for the project server via the command "Options > Settings > Project server".
- The "alias" assigned as the name for the project server is used as an identifier and may not be changed at a later point in time.

### Microsoft system account for project server

When the project server is installed, a Microsoft system account is created for the project server.

Microsoft changes the password cyclically for this account.

If the password for this account has expired, the password needs to be changed and then the project server needs to be restarted.

### Quantity structure for the project server

To work efficiently with the project server, you can create up to 100 server connections.

When you have reached this number, you receive a message informing you that you cannot create any new server connections. Once you have deleted any server connections that are no longer required, you can once again create new connections up to the maximum number.

The following configuration limits are available for a project server depending on the respective hardware:

| Projects/libraries and revisions on the project server | Standard project server (use as temporary project server)  Hardware:   **Field PG M5 Advanced (or equivalent)**    **Intel® Core™ i5-6440EQ up to 3.4 GHz·,16 GB RAM (32 GB for large projects)**    **SSD with 50 GB of available disk space**    **Network 1 GBit**    **15.6" Full HD Display (1920 x 1080)** |
| --- | --- |
| Maximum number of server projects and server libraries per server: | 1000 |
| Maximum number of groups per server: | 1000 |
| Maximum number of active projects and libraries per server | 100 |
| Maximum number of active work areas per project | 63 |
| Maximum number of parallel load processes per server | 10 |
| Maximum number of saved revisions per server | Unlimited, number can be configured  Default setting = 10  Ensure there is sufficient memory space to save the revisions. |

> **Note**
>
> **Server hardware**
>
> When more powerful server hardware is used, even higher quantities are possible.
>
> To improve performance, use few folders for the storage structure of the administered projects. The more folders you use for the storage of projects and their objects, the more work memory is in use.

---

**See also**

[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
  
[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)
  
[Installing and uninstalling the project server](#installing-and-uninstalling-the-project-server)

## Basics of the project server

### Introduction

To work with Multiuser Engineering, Multiuser Commissioning or Exclusive Engineering, you need a project server that manages your server projects, server libraries and the local sessions.

Each version of the TIA Portal contains a version-specific project server with corresponding functionality.

With the help of the project server you can:

- Create new server projects and server libraries in which multiple users can work at the same time.
- Show and manage existing server projects and server libraries.
- Sort and manage server projects and server libraries in groups.
- Create and manage local sessions.

**Compatibility of the project server with the TIA Portal**

Communication between the project server and the TIA Portal is supported for various applications.

For more details, see: [Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)

### Requirement

To use the functionality of the project server, you need to install the appropriate software for the project server.

Alternatively, you can use the local project server installed by default with the TIA Portal.

### Possible server constellations

Different server constellations are available in the TIA Portal:

1. The project server as "dedicated server" that is implemented as external server for long-term collaboration.
2. The "temporary project server" in which the server functionality is implemented on a workstation.
3. The "local project server" that is automatically installed in the TIA Portal but only has limited functionality.

The table below provides an overview of working with the possible server constellations.

| Overview of possible server constellations for the project server |  |
| --- | --- |
| **1st project server as dedicated server**   - The project server can be installed with the TIA Portal or as a standalone product. - This configuration is usually the one that is used as "office network configuration". - The project server runs on a separate computer. - This server constellation can be reached at all times and supports integrated working "around the clock" by default. - The project server must be installed and configured. | ![Possible server constellations](images/124904147851_DV_resource.Stream@PNG-en-US.png) |
| **2. Temporary project server:**   - Editors of the server project can apply the server function to their computer. - This configuration is also a possible "office configuration". - You must install and configure the temporary project server. | ![Possible server constellations](images/86476331403_DV_resource.Stream@PNG-en-US.png) |
| **3. Local project server:**   - The local project server runs on the computer of the respective editor. - The local server is available immediately without additional installation and configuration because it is installed with the TIA Portal. - There is no license request for the local project server. - The local project server cannot be accessed from other computers. - The local project server is suitable for learning and testing the functionality of Multiuser Engineering, Multiuser Commissioning and Exclusive Engineering. No server installation and no configuration is required. - The local project server can also be used for separate project management with "rollback" function. | ![Possible server constellations](images/86476313995_DV_resource.Stream@PNG-en-US.png) |

---

**See also**

[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)

## Settings for working with the project server

### Settings in the TIA Portal

You can make the following settings in TIA Portal for working with Multiuser Engineering:

- Server connections
- Network profiles and compression
- Storage settings

To do this, open the "Project server" tab under "Options > Settings".

### Server connections

In the "Connections" area, add new server connections for a selected project server.

- To create this connection, click the "Add server connection" button.
- In the following dialog, enter the server name under "Server name".
- Enter the corresponding host and port number in the "URL" field.
- Click "Add".

The new server connection is added and displayed.

See also [Introduction to the project server](#introduction-to-the-project-server).

### Network profiles and compression

You have the option to select from the drop-down list the required network profile that matches the performance capability of the network you are using

The selected network profile determines the time until a timeout message is generated.

You will find a detailed description of the individual network profiles at [Set network profiles for project server](#set-network-profiles-for-project-server).

Setting the network profile to "Middle" or "Slow" activates compression for the data transfer. With WLAN or with medium data transfer speeds (Fast Ethernet), an improved transfer time is achieved through compression.

No compression is used for the network profile "Fast".

> **Note**
>
> A change to the network profile only takes effect after a restart of the client or the project server.

### Storage settings

Here you can define where your local sessions and your server projects will be saved.

- Storage location currently used

  This option is enabled by default.
- Defining a storage location by default

  Select the respective required storage location here by navigating to the required location.

  Click "Browse" for this purpose. Your settings are applied as default.

You can only select paths on local drives as the storage location for server projects.

---

**See also**

[Introduction to the project server](#introduction-to-the-project-server)
  
[Set network profiles for project server](#set-network-profiles-for-project-server)

## Set network profiles for project server

### Introduction

You can select between three different network profiles, depending on the performance capability of your own network.

The selected network profile determines the time until a timeout message is generated.

### Available network profiles

The following network profiles are available for working with the project server:

| Network profile | Area of application |
| --- | --- |
| "Fast" | - Office environment - Gigabit-Ethernet - Stable and mostly interference-free network environment |
| "Medium" | - Office environment, small workgroup with fixed location - Fast Ethernet, WLAN, VPN connections - Good network environment, rare interference |
| "Slow" | - Commissioning, non-stationary workstations - WLAN connection - Interference possible (machines, electrical installations) |

### Network profiles and compression for the project server

You have the option to select from the drop-down list the required network profile that matches the performance capability of the network you are using.

The selected network profile determines the time until a timeout message is generated.

Setting the network profile to "Middle" or "Slow" activates compression for the data transfer.

No compression is used for the network profile "Fast".

> **Note**
>
> A change to the network profile only takes effect after a restart of the multiuser client or the project server.

### Set network profiles

To set the network profiles for the project server in TIA Portal, follow these steps:

1. In TIA Portal, select the command "Options > Settings > Project server".

   The settings displayed below contain the available options for the network profiles.
2. From the drop-down list for "Network profiles", select the desired profile.
3. Restart either the Multiuser client or the project server so that the changes to the network profile can be applied.

### Result

The selected connection profile is activated.

The compression is activated depending on the profile selected.

> **Note**
>
> The timeout behavior of the current network profile is not affected at the changeover.

## Supported network configurations for the project server

This section contains information on the following topics:

- [Requirements for successful client-server communication](#requirements-for-successful-client-server-communication)
- [Network with dedicated project server](#network-with-dedicated-project-server)
- [Network with temporary project server](#network-with-temporary-project-server)
- [Network in a Windows domain](#network-in-a-windows-domain)
- [Network in a Windows domain with Internet access via VPN](#network-in-a-windows-domain-with-internet-access-via-vpn)
- [Network in a Windows domain with Internet access via proxy](#network-in-a-windows-domain-with-internet-access-via-proxy)

### Requirements for successful client-server communication

#### Introduction

Below is an overview of the requirements for successful client-server communication in the context of Multiuser Engineering and Multiuser Commissioning as well as Exclusive Engineering regarding:

- Network communication
- Certificate management
- Authentication

#### Requirements for network communication

The network used must allow HTTPS communication between client and project server.

There are two ways of doing this:

- Direct TCP communication between client and project server via the enabled server port.

  - No outbound firewall settings blocks communication on the workstations.
  - No incoming firewall settings blocks communication on the project server.
  - Both the project server and all workstations are in the same IP network (without routing).
  - If a router is installed in between, the router should not block communication via the selected server port.
- Indirect communication via an HTTPS proxy server.

  - An HTTPS proxy server is available.
  - The HTTPS proxy server is configured at the client end in the Windows system and enabled for communication.

#### Requirements for certificate management

To establish secure communication, you should use "HTTPS". With "HTTPS", communication is encrypted and a certificate is requested. This means communication has a higher security level than the unencrypted "http" communication.

To establish HTTPS communication, the project server must be configured in such a way that it uses a valid HTTPS certificate for data encryption.

- The certificate in the Windows certificate store is used on the project server.
- The certificate must be currently valid and registered for use with "http.sys".
- The fingerprint of the certificate must be handed over to the client.

#### Requirements for authentication

Windows mechanisms are used for the authentication of the communication with the project server.

Multiuser Engineering supports both authentication through domain accounts and authentication through local Windows accounts.

- Authentication with domain account

  - Both the client and the project server are members of the same Windows domain.
  - A valid user account for this domain is used.
  - Both the client and the project server can establish network communication to the domain server.
  - The requirements for using a secure https communication must be met.

- Authentication with local account

  - A local account on the project server must be used for authentication.
  - The requirements for using a secure HTTPS communication must be met.
  > **Note**
  >
  > **NTLM authentication on the project server**
  >
  > NTLM is used for authentication on the project server. For security reasons, we recommend you activate NTLM V2, which has been used as standard since Windows 2000, and not NTLM V1.
  >
  > NTLM V2 offers a logon method more secure than NTLM V1.

  > **Note**
  >
  > In the following sections, you can find more information about supported network configurations for the project server.

---

**See also**

Network with dedicated project server
  
Network with temporary project server
  
[Network in a Windows domain](#network-in-a-windows-domain)
  
[Network in a Windows domain with Internet access via VPN](#network-in-a-windows-domain-with-internet-access-via-vpn)
  
[Network in a Windows domain with Internet access via proxy](#network-in-a-windows-domain-with-internet-access-via-proxy)

### Network with dedicated project server

#### Introduction

Below, you can find information on a server configuration with a dedicated project server in an office network.

The graph shows the possible structure of such a configuration:

![Introduction](images/124915964427_DV_resource.Stream@PNG-en-US.png)

#### Description of the network configuration with a dedicated project server

The network configuration should meet the following requirements.

| Configuration | Description |
| --- | --- |
| **Network environment** | **Configuration:**   - Various Windows workstations on which the TIA Portal is installed. - A dedicated Windows server, which is installed as a project server. - All workstations and servers are located in the same network. |
| **Network** | **Requirements:**   - There is a direct TCP connection between the workstations and the project server via the selected port. - No outbound firewall settings blocks communication on the workstations. - No incoming firewall settings blocks communication on the server. - Both the project server and all workstations are in the same IP network (without routing). - If a router is installed in between, the router should not block communication via the selected server port. - Either no proxy server is configured, or there is a local bypass. The "Bypass proxy server for local addresses" option should be selected in the Windows settings for a local area network. |
| **Authentication** | **User accounts and Windows workgroups:**   - These must be created locally on the project server. - These must be configured in accordance with the rights and roles for servers, project groups and projects. - Name and password for authentication are queried on all workstations. - Only local accounts of the server system can be used for authentication.    **Note**:  The Windows authentication can be used to query name and password. You have to create local accounts, which are identical to the accounts that exist on the project server. This procedure allows the server to automatically authenticate a local account with identical logon information for an existing server account.   **Restriction:**   User accounts and groups cannot be managed centrally; local users and groups are required for this.  This configuration is therefore unsuitable for enterprise networks. |

### Network with temporary project server

#### Introduction

Below, you can find information on a server configuration with a temporary project server in an office network.

The graph shows the possible structure of such a configuration:

![Introduction](images/124916150283_DV_resource.Stream@PNG-en-US.png)

#### Description of the network configuration with a temporary project server

The network configuration should meet the following requirements.

| Configuration | Description |
| --- | --- |
| **Network environment** | **Configuration:**   - Various Windows workstations on which the TIA Portal is installed. - A temporary Windows server, which is installed as a project server on one of the workstations.   The office environment may be left, for example, to perform commissioning in a factory.  - All workstations and temporary project servers are located in the same network. - With the temporary project server, the office environment can be left and work can still continue. |
| **Network** | **Requirements:**   - There is a direct TCP connection between the workstations and the project server via the selected port. - No outbound firewall settings blocks communication on the workstations. - No incoming firewall settings blocks communication on the server. - Both the project server and all workstations are in the same IP network (without routing). - If a router is installed in between, the router should not block communication via the selected server port. - Either no proxy server is configured, or there is a local bypass. The "Bypass proxy server for local addresses" option should be selected in the Windows settings for a local area network. |
| **Authentication** | **User accounts and Windows workgroups:**   - These must be created locally on the project server. - These must be configured in accordance with the rights and roles for servers, project groups and projects. - Name and password for authentication are queried on all workstations. - Only local accounts of the server system can be used for authentication.    **Note**:  The Windows authentication can be used to query name and password. You have to create local accounts, which are identical to the accounts that exist on the project server. This procedure allows the server to automatically authenticate a local account with identical logon information for an existing server account.   **Restriction:**   User accounts and groups cannot be managed centrally; local groups are required for this.  This configuration is therefore unsuitable for enterprise networks. |

### Network in a Windows domain

#### Introduction

Below, you can find information on a server configuration with a dedicated project server in a Windows domain.

The graph shows the possible structure of such a configuration:

![Introduction](images/124916311307_DV_resource.Stream@PNG-en-US.png)

#### Description of the network configuration in a Windows domain

The network configuration should meet the following requirements.

| Configuration | Description |
| --- | --- |
| **Network environment** | **Configuration:**   - All Windows workstations on which the TIA Portal is installed are members of the same domain. - A dedicated Windows server as a project server is also located in the same domain. - All workstations and project servers use the same LAN (Local Area Network). - All workstations and project servers can connect to the domain controller. |
| **Network** | **Requirements:**   - There is a direct TCP connection between the workstations and the project server via the selected port. - No outbound firewall settings blocks communication on the workstations. - No incoming firewall settings blocks communication on the server. - Both the project server and all workstations are in the same IP network (without routing). - If a router is installed in between, the router should not block communication via the selected server port. - Either no proxy server is configured, or there is a local bypass. The "Bypass proxy server for local addresses" option should be selected in the Windows settings for a local area network. |
| **Authentication** | **User accounts and Windows workgroups:**   - These must be created on the domain controller. - These must be configured in accordance with the rights and roles for servers, project groups and projects. - Users at workstations on which the TIA Portal is running are automatically authenticated with their domain logon information.    **Note**:  You can also log on to the project server with other valid logon data.   **Restriction:**   This configuration is not suitable for temporary server configurations, since they also need access to the domain controller. |

### Network in a Windows domain with Internet access via VPN

#### Introduction

Below, you can find information on a server configuration with a dedicated project server in a Windows domain with VPN (Virtual Private Network).

The graph shows the possible structure of such a configuration:

![Introduction](images/124916561931_DV_resource.Stream@PNG-en-US.png)

#### Description of the network configuration in a Windows domain with VPN

The network configuration should meet the following requirements.

| Configuration | Description |
| --- | --- |
| **Network environment** | **Configuration:**   - All Windows workstations on which the TIA Portal is installed are members of the same domain. - A dedicated Windows server as a project server is also located in the same domain. - All workstations and project servers use the same LAN (Local Area Network). - Both workstations and the project server have access to the domain controller. - Workstations can also be connected to the LAN via VPN. |
| **Network** | **Requirements:**   - There is a direct TCP connection via the selected port between the workstations and the project server. - No outbound firewall settings blocks communication on the workstations. - No incoming firewall settings blocks communication on the server. - Both the project server and all workstations are in the same IP network (without routing). - If a router is installed in between, the router should not block communication via the selected server port. - Either no proxy server is configured, or there is a local bypass. The "Bypass proxy server for local addresses" option should be selected in the Windows settings for a local area network. - For security reasons, we recommend using VPN solutions, such as "Routing and Remote Access Service". - For security reasons, it is strongly recommended to set up a firewall. It is not necessary to open a port in the firewall for the project server when using VPN. |
| **Authentication** | Authentication is performed based on the current configuration selected.   **User accounts and Windows workgroups when configured as an office workgroup:**   - These must be created locally on the project server. - These must be configured in accordance with the multiuser rights and roles for servers, project groups and projects. - Name and password for authentication are queried on all workstations. - Only local accounts of the server system can be used for authentication.    **Note**:  The Windows authentication can be used to query name and password. You have to create local accounts, which are identical to the accounts that exist on the project server. This procedure allows the server to automatically authenticate a local account with identical logon information for an existing server account.   **Restriction:**   User accounts and groups cannot be managed centrally; local users and groups are required for this.  This configuration is therefore unsuitable for enterprise networks.    **User accounts and Windows workgroups with configuration as Windows domain:**   - These must be created on the domain controller. - These must be configured in accordance with the multiuser rights and roles for servers, project groups and projects. - Users at workstations on which the TIA Portal is running are automatically authenticated with their domain logon information.    **Note**:  You can also log on to the project server with other valid logon data.   **Restriction:**   This configuration is not suitable for temporary server configurations, since they also need access to the domain controller.  Communication with a remote computer through a VPN demonstrates typical performance limitations for all client-server applications. The project server is also affected. |

### Network in a Windows domain with Internet access via proxy

#### Introduction

Below, you can find information on a server configuration with a dedicated project server in a Windows domain with intranet/Internet access via a proxy.

The graph shows the possible structure of such a configuration:

![Introduction](images/124916671755_DV_resource.Stream@PNG-en-US.png)

#### Description of the network configuration in a Windows domain with proxy

The network configuration should meet the following requirements.

|  |  |
| --- | --- |
| **Network environment** | **Configuration:**   - All Windows workstations on which the TIA Portal is installed are members of the same domain. - A dedicated Windows server as a project server is also located in the same domain. - All workstations and project servers use the same LAN (Local Area Network). - Both workstations and the project server have access to the domain controller. - Workstations outside the LAN can also be connected to the LAN via a proxy server. |
| **Network** | **Requirements:**   - There is a direct TCP connection between the workstations and the project server via the selected port. - No outbound firewall settings blocks communication on the workstations. - No incoming firewall settings blocks communication on the server. - Both the project server and all workstations are in the same IP network (without routing). - If a router is installed in between, the router should not block communication via the selected server port. - Either no proxy server is configured, or there is a local bypass. The "Bypass proxy server for local addresses" option should be selected in the Windows settings for a local area network. - For security reasons, it is not recommended to make the project server available on the Internet. - For security reasons, it is strongly recommended to set up a firewall to accept the incoming connections to the selected port. - The proxy server must accept HTTPS communication and forward it to the project server on the selected port. |
| **Authentication** | Authentication is performed based on the current configuration selected.   **User accounts and Windows workgroups when configured as an office workgroup:**   - These must be created locally on the project server. - These must be configured in accordance with the multiuser rights and roles for servers, project groups and projects. - Name and password for authentication are queried on all workstations. - Only local accounts of the server system can be used for authentication.    **Note**:  The Windows authentication can be used to query name and password. You have to create local accounts, which are identical to the accounts that exist on the project server. This procedure allows the server to automatically authenticate a local account with identical logon information for an existing server account.   **Restriction:**   User accounts and groups cannot be managed centrally; local users and groups are required for this.  This configuration is therefore unsuitable for enterprise networks.   **User accounts and Windows workgroups with configuration as Windows domain:**   - These must be created on the domain controller. - These must be configured in accordance with the multiuser rights and roles for servers, project groups and projects. - Users at workstations on which the TIA Portal is running are automatically authenticated with their domain logon information.    **Note**:  You can also log on to the project server with other valid logon data.   **Restriction:**   This configuration is not suitable for temporary server configurations, since they also need access to the domain controller.  Communication with a remote computer through a proxy demonstrates typical performance limitations for all client-server applications. The project server is also affected. |
| **Port** | **Note**:  Sometimes it is only possible to use port "443" for an https connection on a proxy server. A port other than "443" for an https connection cannot be set on some proxy servers. In this case, you need to install the project server on port "443" as well. |

## Installing and uninstalling the project server

This section contains information on the following topics:

- [Notes on installing the project server](#notes-on-installing-the-project-server)
- [Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
- [Installing a project server](#installing-a-project-server)
- [Uninstalling a project server](#uninstalling-a-project-server)

### Notes on installing the project server

#### Introduction

The installation of the TIA Project Server allows you to use the functionality of the Multiuser Engineering, from Multiuser Commissioning and from Exclusive Engineering.

You have the following options for installing the "TIA Project Server":

- Together with the installation of the TIA Portal.
- As standalone installation by means of a separate installation process without TIA Portal.

> **Note**
>
> **Requirement: Administrator rights**
>
> Administrator rights are required for the installation of the TIA Project Server.

More information:

- "[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)"

#### Installation of the TIA Project Server with the TIA Portal

The TIA Project Server (referred to as "project server" below) is installed together with the following TIA Portal products:

- SIMATIC STEP 7 Basic
- SIMATIC STEP 7 Professional
- SIMATIC WinCC Basic
- SIMATIC WinCC Comfort/Advanced
- SIMATIC WinCC Professional

The project server is usually activated by default in the product selection and is then installed with the TIA Portal.

Check the settings during installation of the TIA Portal.

You can find the specific default settings for the project server during setup when selecting the product in the "Options" directory.

By selecting or clearing the options, you can specify if the project server is to be installed along with TIA Portal or not.

#### Installation of the project server as a standalone installation

The project server can also be installed as a standalone installation.

A description of automated installation is also available on the product DVD in the directory "Documents\Readme\<language directory>".

#### Identical TIA Portal versions during installation

When installing different TIA Portal products on various clients, make sure that all participants use the same versions of software products for the installation.

For example, if you have installed STEP 7 Professional, WinCC Advanced and Safety as well as the Project Server with version Vx.y, all other devices and clients must also have this software installed in the same versions.

The service packs and updates must be installed for all products at the same time.

> **Note**
>
> **TIA Project Server: Versioning**
>
> As of TIA Portal V18, the TIA Project-Server is supplied with a version number that is independent of the TIA Portal:
>
> - TIA Portal V19 includes TIA Project Server V1.2

#### Installation path

Do not use any UNICODE characters (for example, Chinese characters) in the installation path.

#### Antivirus programs

During the installation, read and write access to installed files is necessary.

Some antivirus programs block this access.

We therefore recommend that you disable antivirus programs during the installation of the project server and enable them again afterwards.

#### Supported security programs

The following security programs are compatible with "SIMATIC STEP 7" and "SIMATIC WinCC":

- Antivirus programs:

  - Symantec Endpoint Protection 14.3
  - Trend Micro Apex One (Trend Micro Office Scan) 14.0
  - McAfee Endpoint Security (ENS) 10.7 (Trellix)
  - Windows Defender
  - Qihoo 360 "Safe Guard 12.1" + "Virus Scanner"
  > **Note**
  >
  > Make sure that your virus scanner and its databases are always up-to-date.

  The last update of the virus pattern was on Sept. 13, 2022.
- Encryption software:

  - Microsoft Bitlocker
- Host-based Intrusion Detection System:

  - McAfee Application Control 8.3.6 (Trellix)

#### Supported virtualization platforms

You can also install the project server as well as the TIA Portal in a virtual machine.

For this purpose, use one of the following virtualization platforms in the specified version or a newer version:

- VMware vSphere Hypervisor (ESXi) 6.7 or higher
- VMware Workstation 12.5.5 (WinCC only)
- VMware Workstation 15.5.0 or higher
- VMware Player 12.5.5 (WinCC only)
- VMware Player 15.5.0 or higher
- Microsoft Hyper-V Server 2019 or higher

> **Note**
>
> Installation of a visualization platform has the same requirements as the installation of the TIA Portal.

---

**See also**

[General software and hardware requirements](Installation.md#general-software-and-hardware-requirements)
  
[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
  
[Installing a project server](#installing-a-project-server)
  
[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)

### Notes on the compatibility of the project server

#### Introduction

To work with Multiuser Engineering, Multiuser Commissioning and Exclusive Engineering, you need a project server that manages your server projects, server libraries and the local sessions.

#### Compatibility of the project server with the TIA Portal

Communication between the project server and the TIA Portal is supported for the following applications:

| Version of the project server | Version of the TIA Portal |
| --- | --- |
| TIA Project Server V1.2 | V19, V18, V17, V16, V15.1, V15 and V14 |
| TIA Project Server V1.1 | V18, V17, V16, V15.1, V15 and V14 |
| Server V17 / TIA Project Server V1.0 | V17, V16, V15.1, V15 and V14 |
| Server V16 | V16, V15.1, V15 and V14 |
| Server V15.1 | V15.1, V15 and V14 |
| Server V15 | V15 and V14 |
| Server V14 | V14 |

> **Note**
>
> **Notes on the compatibility of the project server**
>
> The newly added server functionality for the current version is only available if the current version of TIA Portal is also installed.
>
> If you are still working with an older version of TIA Portal or an older version of the project server, only the functionality included in the respective product version is available.
>
> Multiuser Engineering does not upgrade the project versions.

#### Storage directory of the project server

Each TIA Portal version is delivered with the project server version released for it.

You can define a new storage directory for the new project server or continue using an existing storage directory of an older project server for the new server version, in which you have saved the V15 projects, for example.

The following rules apply:

- To use different servers at the same time and independent of each other, you must configure different ports and storage directories for the different servers during installation of the new server.
- To continue using an older server directory as storage for the newly installed project server, enter the existing directory during configuration of the new project server. The storage path is checked during installation of the project server, and you receive a corresponding message that this storage directory is already being used for a different server.

  You then have the following options:

  - You can cancel the installation and enter a new storage directory for the project server.
  - Or you can upgrade the storage directory for the project server.

  However, the upgraded directory becomes invalid for older server versions and can no longer be started with the older server.

  The upgrade of the storage directory does not impact the TIA Portal projects saved in the directory.

  An internal backup is executed prior to the upgrade so that you can undo any erroneous upgrade.

  If there are no errors during the upgrade, the "Undo" function is not offered.

  > **Note**
  >
  > **Storage directory of the server**
  >
  > The storage directory of the project server is locked during installation of the server.
  >
  > This is intended to prevent changes to a storage directory while it is actively being accessed.

---

**See also**

[Configuring the project server with the administrative tools](#configuring-the-project-server-with-the-administrative-tools)
  
[Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)
  
[Installing a project server](#installing-a-project-server)
  
[Notes on installing the project server](#notes-on-installing-the-project-server)
  
[Using the graphic tools](#using-the-graphic-tools)
  
[Using the command line tools](#using-the-command-line-tools)

### Installing a project server

#### Introduction

You install the TIA Project-Server as part of the TIA Portal installation or standalone, independently of the TIA Portal.

When installing with TIA Portal, the project server version released for this purpose is always installed. Project server versions that are released afterwards are also released for this TIA Portal version as long as there are no new TIA Portal versions.

You can find information on the TIA Portal versions released for a specific project server version in this section:

- "[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)"

A description of automated installation is also available on the product DVD in the directory "Documents\Readme\<language directory>".

More information:

- "[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)"

> **Note**
>
> **TIA Project Server: Versioning**
>
> As of TIA Portal V18, the TIA Project-Server is supplied with a version number that is independent of the TIA Portal:
>
> - TIA Portal V19 includes TIA Project Server V1.2
>
> **New installation replaces existing installation**
>
> Up to TIA Portal V18, project servers from different versions can be used side by side.
>
> As of TIA Portal V18, versions of the TIA Project Server are no longer installed in parallel. The new TIA Project Server version replaces existing installations during installation.
>
> The existing user permissions for the server are applied.

#### TIA Portal versions < V18

Up to TIA Portal V18, it is possible for several versions of the project server that use different project versions of TIA Portal to be installed on the same computer.

However, each version of TIA Portal and the project server has only the functionality contained in that version.

Multiuser Engineering does not upgrade the project versions.

As of TIA Portal V18, TIA Project Server as of V1.0 is supplied. The new installations of the TIA Project Server replace the existing installation in each case. Different versions of the project server can no longer be installed on the same PC as of V1.0.

However, versions of the project server installed with TIA Portal versions prior to V18 can continue to run side-by-side on a PC and parallel to TIA Project Server versions as of V1.0.

#### Requirements for installation

You need administrator rights.

The installation of the server requires specific settings in the Windows firewall and, if needed, a certificate.

System requirements:

- Installation of the project server has the same requirements as the installation of the TIA Portal.

#### Installing the project server with the TIA Portal

Follow these steps for installation:

1. Note the requirements for the installation of the selected software package.
2. Start the setup program of the required product by inserting the installation medium into the respective drive.
3. Select the preferred settings and click the "Install" button.
4. Make sure that the project server is selected in the product selection and observe the notes in the setup dialogs.

#### Result

The project server was installed on your computer together with the TIA Portal.

#### Installing the project server as standalone product

Follow these steps for installation:

1. Note the requirements for the installation of the project server.
2. Start the setup for the standalone installation of the project server with a double-click on the self-extracting .exe file "TIA_Portal_Project_Server_V<x.y>.exe".

   You can find these files in the directory "Support" on the corresponding product DVD.
3. Select the preferred settings and click the "Install" button.
4. Follow the instructions in the setup dialogs.

#### Result

The TIA Project Server has been installed on your computer.

---

**See also**

[Notes on the compatibility of the project server](#notes-on-the-compatibility-of-the-project-server)
  
[Notes on installing the project server](#notes-on-installing-the-project-server)
  
[Industry Online Support: TIA Project Server - Download](https://support.industry.siemens.com/cs/ww/en/view/109810588)
  
[System requirements for installation](Installation.md#system-requirements-for-installation)

### Uninstalling a project server

#### Introduction

The "TIA Project Server" is uninstalled by using the Control Panel.

Installing a new version of the project server replaces an existing installation.

#### Requirements for removal

A project server is installed on your computer.

#### Uninstalling the TIA Project Server

Proceed as follows for removal:

1. Open the Control Panel.
2. Double-click on "Uninstall a program" in the Control Panel.

   The "Uninstall or change a program" dialog opens.
3. In the "Add or Remove Programs" dialog, select the entry for the "TIA Project Server".
4. Click on the "Remove" button.

   A security prompt appears.
5. Click "Yes" to confirm this prompt.

#### Result

The TIA Project Server has been uninstalled from your computer.

## Configuring and managing the project server

This section contains information on the following topics:

- [Options for configuring and administering the project server](#options-for-configuring-and-administering-the-project-server)
- [Using the graphic tools](#using-the-graphic-tools)
- [Using the command line tools](#using-the-command-line-tools)
- [Confirm certificate for project server](#confirm-certificate-for-project-server)
- [Enter access data for project server](#enter-access-data-for-project-server)
- [Transferring server data to other project server](#transferring-server-data-to-other-project-server)
- [Read out error log for project server](#read-out-error-log-for-project-server)
- [Pack error log for project server as Zip file](#pack-error-log-for-project-server-as-zip-file)
- [Information on response of the project server to errors](#information-on-response-of-the-project-server-to-errors)

### Options for configuring and administering the project server

#### Introduction

The following options are also available for configuring and administering the project server:

- Using the graphic tools (Configuration Tool and Administration Tool).
- Using the command line tools (Project Server Administrative Tools and Project Server Power Tools).

You can configure and manage the project server using both methods.

The graphical tools are easier to operate using the graphical user interface. The command line tools have a somewhat wider range of functions with respect to the error log. You can compress and send the error logs as a zip file.

You have the option of using the procedure you prefer.

Administrator rights are required for configuring the project server irrespective of the selected procedure.

You need administrator rights (for user administration) and user rights for some for administrative tasks.

> **Note**
>
> **Available languages**
>
> - The tools for configuring and administering the server project server are available in English only for Server V14.
> - As of Server V15, the tools are available in the user interface languages supported by TIA Portal.

#### Configuration and administration with the graphic tools

The graphic tool provides you with a very convenient way of configuring and administering the project server.

You see at a glance all setting options and can activate these by selecting the corresponding options.

You can find the exact procedure in: [Using the graphic tools](#using-the-graphic-tools)

#### Configuration and administration with the command line tools

The configuration of the project server is performed with the administrative tools.

The power tools are used for administering the project server.

The power tools for performing administration tasks on the project server are also available to you within the TIA Portal.

You can find the exact procedure in: [Using the command line tools](#using-the-command-line-tools)

> **Note**
>
> **Working with the command line tools**
>
> For working with the command line tools, you should have prior experience handling inputs in the command line.
>
> If you lack this experience, you should use the more user-friendly graphical user interface for configuring and administering the project server.

---

**See also**

[Using the command line tools](#using-the-command-line-tools)
  
[Using the graphic tools](#using-the-graphic-tools)

### Using the graphic tools

This section contains information on the following topics:

- [Introduction to the graphic Power Tools](#introduction-to-the-graphic-power-tools)
- [Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)
- [Configuring the project server with the Configuration Tool](#configuring-the-project-server-with-the-configuration-tool)
- [Managing the project server with the graphic Administration Tool](#managing-the-project-server-with-the-graphic-administration-tool)
- [Adding and deleting a new server connection](#adding-and-deleting-a-new-server-connection)
- [Specifying the user administration for a project server](#specifying-the-user-administration-for-a-project-server)
- [Assign access rights for project servers, server projects and server libraries](#assign-access-rights-for-project-servers-server-projects-and-server-libraries)
- [Managing alerts](#managing-alerts)
- [Managing server projects and server libraries](#managing-server-projects-and-server-libraries)
- [Managing groups on the project server](#managing-groups-on-the-project-server)
- [Managing local sessions](#managing-local-sessions)
- [Displaying the history for projects and libraries](#displaying-the-history-for-projects-and-libraries)
- [Manage revisions](#manage-revisions)
- [Switching back and forth between engineering and commissioning mode](#switching-back-and-forth-between-engineering-and-commissioning-mode)
- [Selecting a user interface language](#selecting-a-user-interface-language)
- [Displaying confirmations](#displaying-confirmations)
- [Managing certificates](#managing-certificates)

#### Introduction to the graphic Power Tools

##### Introduction

The project server can be easily configured and managed with the help of the graphic Power Tools.

- To configure the project server, use the "Configuration Tool".
- You use the "AdministrationTool" to administer the multiuser server.

You need administrator rights in some areas to configure the project server.

> **Note**
>
> **Available languages**
>
> - The tools for configuring and administering the server project server are available in English only for Server V14.
> - As of Server V15, the tools are available in the user interface languages supported by TIA Portal.

##### Requirement

The project server is installed.

##### Steps for configuring the project server with the "Configuration Tool"

To configure the project server, the following steps are required:

- Open the graphic tool for the server configuration with administrator rights.
- To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
- Click on the entry "TIA Project Server - Configuration" to open the Configuration Tool .
- Select the language you want from the black highlighted footer.
- Enter the required configuration data and click "Install service".

You can find the exact procedure in: [Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)

##### Steps for administering the project server with the "Administration Tool"

To administer the project server, the following steps are required:

- Open the graphic tool for the multiuser project server administration.
- To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
- Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
- On the "Administration" tab, insert a connection to the desired project server and enter the data for the administration of the server.
- On the "Settings" tab, select the language settings and manage confirmations and certificates.

You can find the exact procedure in: [Managing the project server with the graphic Administration Tool](#managing-the-project-server-with-the-graphic-administration-tool)

---

**See also**

[Managing the project server with the graphic Administration Tool](#managing-the-project-server-with-the-graphic-administration-tool)
  
[Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)

#### Managing a project server with the graphic Configuration Tool

##### Introduction

You use the graphic "Configuration Tool" to configure the project server.

Only one instance of the "Configuration Tool" can be opened in a device.

##### Functionality of the Configuration tool

The following functions can be executed with the "Configuration Tool":

**"Server status" area**

- When the Configuration tool is opened for the first time, the area contains the contents displayed in the graphic. This area is not editable.
- Once the configuration has been successfully completed, the server can be uninstalled, started and stopped in this area.

**"Connection settings" area**

- Allows you to select the connection data.

**"Security" area**

- Offers the option to create a new certificate or to use an existing certificate for a selected https connection.

**"Memory" area**

- Allows you to select the storage location for server projects.
- Allows you to select how many project versions are available as "rollback".

> **Note**
>
> **Memory space on the project server**
>
> For the project management, you need to have sufficient free space on the project server, depending on the number of saved projects, their sizes and the number of retained project revisions.
>
> Basically, the provided space should be at least five times the expected size of the project.
>
> When a greater number of project revisions is used, the available memory space also needs to be increased accordingly. You set the number of project revisions when configuring the project server.
>
> Generally, you should provide sufficient storage capacity and also take into account or evaluate the messages of the operating system as the memory space decreases.

> **Note**
>
> **Working with Multiuser Commissioning**
>
> When you work with Multiuser Commissioning, a new revision of the server project is created automatically after each download to the CPU.
>
> To reduce the memory requirements, limit the number of revisions to a daily maximum. Only keep the important revisions, e.g. when a project milestone has been reached.
>
> Please also note that the oldest revisions are automatically deleted after the maximum set number of revisions has been reached.
>
> **Number of saved project revisions**
>
> You set the number of project revisions to be saved when configuring the project server in the Configuration Tool.
>
> You can select a number between 10 and "unlimited" or enter the required number manually.

##### User interface of the Configuration tool

The figure below shows the user interface of the Configuration Tool:

![User interface of the Configuration tool](images/142294283147_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the project server with the Configuration Tool](#configuring-the-project-server-with-the-configuration-tool)

#### Configuring the project server with the Configuration Tool

##### Introduction

You use the graphic "Configuration Tool" to configure the project server.

##### Requirement

The project server is installed.

##### Configuring the project server with the "Configuration Tool"

To configure the project server, follow these steps:

1. Open the graphic tool for the server configuration with administrator rights.

   To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".

   Click on the entry "TIA Project Server - Configuration" to open the Configuration Tool.

   The user interface of the Configuration Tool then opens.
2. In the "Connection settings" area, select the desired protocol.

   Default selection is "https". As soon as you click on "http", a text with yellow background is displayed that suggests you select an "https" connection.

   With "https", communication is encrypted and a certificate is requested. This means communication has a higher security level than the unencrypted "http" communication.
3. Enter the desired port for the server connection if you do not want to use the default setting.
4. Select the desired "Timeout profile" for the server from the drop-down list.

   This setting defines the timeout behavior for the server.

   You have the option of selecting between three profiles: "Fast", "Medium" and "Slow"; the default is "Fast".
5. "Security" area If you have selected "https" as the protocol, the "Security" area is activated.

   Select the desired option for the certificate.

   You have the option of creating a new certificate or using an existing certificate on your computer.

   If you activate the first option, a new certificate is created after successful completion of the configuration.

   If you activate the second option, you can click on the desired certificate in the displayed list of certificates to select it.
6. Specify the desired storage location for server projects under "Storage".

   You can enter the path directly or navigate to the desired location via "Browse". You can only select paths on local drives.
7. Select the number of project versions to be stored from the subsequent drop-down list.

   Ten project versions are saved by default.

   You can choose to store between "1" and "Unlimited" project versions.
8. Click "Install service" to complete the configuration.

##### Result

A message informs you that the configuration of the project server was successful.

![Result](images/104452469515_DV_resource.Stream@PNG-en-US.png)

In the "Server status" area, you will find the URL for the project server and the fingerprint for the generated certificate under "Client info".

Example:

https://XY12345.ww00X.siemens.net:8735/

C35F81B179062BA92A3EAE4DBF18B0DEA9F50D8A

If you access the server from the client side, you should always check the certificate in order to ensure secure communication with the project server.

The configuration of the project server is now complete.

##### Error correction in the Configuration tool

If warnings or errors occur, you will find specific information about these in ServerConfiguration.log.

![Error correction in the Configuration tool](images/104450304651_DV_resource.Stream@PNG-en-US.png)

Proceed as follows:

1. Click on "Open log" in the yellow highlighted area to open the ServerConfiguration.log.
2. Correct the errors and warnings displayed in the log file.
3. Restart the Configuration tool if it is no longer open.
4. Click "Install service".

##### Result

A message informs you that the configuration of the project server was successful.

The configuration of the project server is now complete.

> **Note**
>
> To apply changes to existing inputs in the Configuration Tool, you must click the "Apply" button.

---

**See also**

[Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)

#### Managing the project server with the graphic Administration Tool

##### Introduction

You use the graphic "Administration Tool" to configure the project server.

> **Note**
>
> **Administration Tool**
>
> - You need administrator rights to work with the Administration Tool.
> - The Administration Tool is also available outside the project server.

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### User interface of the Administration tool

Open the graphic tool for the project server administration.

- To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
- Click on the entry "TIA Project Server - Administration" to open the Administration Tool.

The user interface of the Administration tool has the following appearance:

![User interface of the Administration tool](images/104452972171_DV_resource.Stream@PNG-en-US.png)

##### Functionality of the Administration Tool

The two tabs on the left-hand side of the tool let you switch between "Settings" and "Administration".

Under "Administration", you can find a list of the configured server connections as soon as you have set up a connection to the project server with "Add server connection". On the right side, you receive additional information about the objects selected on the left in a detail view.

Both pages contain their own toolbar for executing the displayed administration functions.

To switch the view, click on the "Administration" button or on the "Settings" button.

On the "Administration" tab you can:

- Add and delete servers and server connections
- Update data
- Set user management for the server connections, multiuser projects, and server libraries.
- Manage existing multiuser projects, server libraries and sessions.

  This includes the following actions:

  - Specify user roles for project groups. projects, libraries and sessions:

    "Manager", "Contributor", "Member"
  - Groups:

    Create, assign projects or libraries, delete
  - Projects, libraries:

    Lock, unlock, delete
  - Sessions:

    Display, delete
- Enabling and disabling commissioning mode for projects
- Display "History":

  History with all data and display of the stored project revisions and library revisions
- Export "History":

  The history with the selected data is exported as an XML file.
- Manage revisions
- Add revision information.
- Export server projects and server libraries
- Import server projects and server libraries

In the "Settings" tab you can:

- Select user interface language.
- Select confirmations
- Managing certificates

The exact procedures for working with the Administration Tool are described below.

> **Note**
>
> **"Reload" button**
>
> Clicking this button updates the display for the selected object in the Administration Tool .

---

**See also**

[Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)

#### Adding and deleting a new server connection

##### Introduction

You can add and delete new project server connections with the graphic "Administration" tool.

These commands can be executed using the commands in the toolbar or from the shortcut menu.

> **Note**
>
> **Administration Tool**
>
> You need administrator rights to work with the Administration tool.

##### Requirement

The project server is installed.

The project server has already been configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Adding a new server connection

Proceed as follows:

1. Open the graphic tool for the project server administration.

   To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".

   Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Click "Add server connection".
3. In the dialog that follows, enter the desired connection data for your server connection as shown by way of example in the graphic:

   ![Adding a new server connection](images/104455924235_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new server connection](images/104455924235_DV_resource.Stream@PNG-en-US.png)
4. Click "Add" to add the server connection.
5. Click the triangle of the new server connection to activate the connection and view the list of projects and libraries.
6. If you use an "https" connection, you are prompted to confirm the validity of the displayed certificate.

   You have already specified the utilized connection protocol when configuring the project server under "Connection settings".

   Compare the fingerprint of the displayed certificate with the certificate generated during configuration.

   Click "OK" when both fingerprints match.
7. If the project server does not recognize the login data you used, you are prompted to enter alternative connection data for access to the server.

   In the displayed dialog, enter alternative login data that the project server recognizes.

**Note**

**Connection information for the local project server**

If you want to connect to the local project server, you must start it first.

The local project server is started automatically when you open a local session in TIA Portal.

Alternatively, you can restart the local project server by double-clicking the file "Siemens.Automation.Portal.LocalServer.exe" under "bin" in the installation directory of TIA Portal.

You can see the connection information for the local project server after opening the displayed command window.

##### Result

The new server connection is displayed in the left part of the Administration tool.

You see the number of existing server projects and server libraries on the right.

If you expand the new server connection in the left area, you see a list of all existing projects and libraries and other setting options.

##### Delete an existing server connection

Proceed as follows:

1. Select the desired server connection on the left side of the Administration tool.
2. Click on the "Remove server" button or select the command "Remove" from the shortcut menu.
3. Confirm the next prompt with "Yes".

##### Result

The selected server connection is deleted.

##### Accessibility of the project server

If the project server is not accessible, you receive a corresponding error message:

If this happens, proceed as follows:

1. Check the displayed connection data.
2. Ensure that the selected server is started.
3. Delete the invalid server connection by clicking on it and then clicking ""Remove server.
4. Confirm the next prompt with "Yes".
5. Click "Add server connection" and create a new server connection to a started project server with valid connection data.

##### Result

The new server connection is displayed with valid connection information.

---

**See also**

[Deleting server projects and server libraries](Using%20Multiuser%20Engineering.md#deleting-server-projects-and-server-libraries)
  
Deleting server projects and server libraries

#### Specifying the user administration for a project server

##### Introduction

With the graphical "Administration Tool" you configure the authorizations and roles for working with the levels of the project server in the "User administration":

- Project server connections
- Project groups / library groups
- Server projects and their local sessions / server libraries and their local sessions

##### Roles and authorizations

The rights concept is based on the Windows access rights for folders and files.

You configure the authorizations and roles in the "User administration" in the Administration Tool below each server connection, project/library group and below each project or each library. Depending on where you call the "User administration", you specify the corresponding authorizations.

You configure explicit personal authorizations for the following roles:

| Role | Authorizations |
| --- | --- |
| Manager | Full access to the assigned level:  - User administration - Project server: Create, manage and delete groups, libraries, projects and local sessions - Group: Create, manage and delete projects, libraries and local sessions |
| Contributor | Partial access  Delete: Only server projects, server libraries and local sessions |
| Member | Read-only |

**Windows user under "BUILTIN\Administrators"**

You cannot use the gray-shaded group "BUILTIN\Administrators" for the user administration of the project server.

Only Windows user entries are displayed and managed with this group.

Adding a user to this group does not affect the rights management of the project server.

> **Note**
>
> **BUILTIN\Administrators: Full access to server connections**
>
> Administrators who are members of the Windows group "BUILTIN\Administrators" have full access to all project server connections and their lower levels.

##### Working in the User administration

You can execute the following functions for each role using the buttons:

| Symbol | Meaning |
| --- | --- |
| "Add" | Adds new users with the corresponding authorizations. |
| "Remove selected user": | Removes the selected user. |
| "Promote selected user" | Moves the selected user up to the next higher authorization group. |
| "Demote selected user" | Moves the selected user down to the next lower authorization group. |

> **Note**
>
> **Change permissions: Restart required**
>
> After changing the permissions, you must restart the project.

> **Note**
>
> **Use user groups**
>
> Preferably create user groups instead of individual users in the user administration.
>
> Example:
>
> In the user administration, a user group of 10 persons takes up less server capacity than 10 individually created users.

##### Inheriting authorizations

Higher-level authorizations can be passed on to the lower levels.

| Configuration level | Behavior |
| --- | --- |
| Project server connection | The assigned rights apply for the following levels:  - Selected project server connection - Contained project groups / library groups - Contained projects, libraries and local sessions   Project server connections for which no authorizations have been assigned for the users are hidden. |
| Group | The assigned rights apply for the following levels:  - Selected group - Contained projects, libraries and local sessions   The users are created as "members" with read permissions for the following level:  - Higher-level project server connection   Under the project server connection, only the groups for which authorizations are assigned to the users are displayed to them. Groups for which they have no authorization are hidden. |
| Server projects / server libraries and their local sessions | The assigned rights apply for the following levels:  - Selected project / selected library - Local sessions of the project / library   The users are created as "members" with read permissions for the following levels:  - Higher-level group   Under the group, only the projects or libraries for which authorizations are assigned to the users are displayed to them. Projects and libraries for which they have no authorization are hidden. - Higher-level project server connection   Under the project server connection, only the groups which contain projects and libraries for which authorizations are assigned to the users are displayed to them. Groups for whose projects and libraries they have not been assigned authorizations are hidden. |

> **Note**
>
> **Assign minimal rights**
>
> Create a roles concept before configuring the user administration.
>
> Assign only authorizations which are necessary for the respective work to users.
>
> Example:
>
> If users are only working with projects, libraries and session, the role "Member" is sufficient for the higher levels. Configure the authorizations for the user directly below the server project or the server library.

---

**See also**

[Assign access rights for project servers, server projects and server libraries](#assign-access-rights-for-project-servers-server-projects-and-server-libraries)

#### Assign access rights for project servers, server projects and server libraries

##### Introduction

With the graphical "Administration Tool" you configure the authorizations and roles for working with the levels of the project server in the "User administration".

- Project server connections
- Project groups / library groups
- Server projects, server libraries and their local sessions

> **Note**
>
> **Change permissions: Restart required**
>
> After changing the permissions, you must restart the project.

> **Note**
>
> **Assign minimal rights**
>
> Create a roles concept before configuring the user administration.
>
> Assign only authorizations which are necessary for the respective work to users.
>
> Example:
>
> If users are only working with projects, libraries and session, the role "Member" is sufficient for the higher levels. Configure the authorizations for the user directly below the server project or the server library.
>
> **Use user groups**
>
> Preferably create user groups instead of individual users in the user administration.
>
> Example:
>
> In the user administration, a user group of 10 persons takes up less server capacity than 10 individually created users.

##### Requirement

You need administrator rights to work with the "User administration".

The project server is installed.

The project server is configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Assigning access rights

Proceed as follows:

1. Open the graphic tool for the project server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the AdministrationTool.
2. Double-click "User administration" below the desired entry on the left side.

   - Server connection:

     You assign the rights for working with the server and all contained groups and projects or libraries.
   - Project group / library group:

     You assign the rights for working with the group and all contained projects and libraries.
   - Server project / server library:

     You assign the rights for working with the project or the library and the lower-level local sessions.
3. The "User administration" editor opens and displays the possible settings on the right side.

   You can already see which rights have been assigned for the associated server connection, server project or server library.

   Server connection rights are inherited for the groups, projects and libraries.

   Group rights are inherited by the projects and libraries.

   ![Assigning access rights](images/104456491787_DV_resource.Stream@PNG-en-US.png)

   ![Assigning access rights](images/104456491787_DV_resource.Stream@PNG-en-US.png)
4. To add new users for the displayed roles, click on "Add".
5. Enter the required data in the subsequent Windows dialog and click "OK".
6. You use the "Promote selected user" and "Demote selected user" buttons to move users up and down to other permission groups.
7. You use the "Remove selected user" button to remove a user.
8. Assign the desired rights and roles via "User administration" for both the server and the lower-level groups and projects or libraries.

---

**See also**

[Specifying the user administration for a project server](#specifying-the-user-administration-for-a-project-server)

#### Managing alerts

##### Introduction

You can use the graphical "Administration Tool" to view and manage existing alerts for the project server in the "Administration" > "Alert" tab. Alerts allow information to be transferred from the server to the administrator.

A number in brackets beside the "Alert" entry means there is that number of alerts.

The entry "Warning" appears both below the server and below the individual projects and libraries.

The following alerts are displayed:

- A server alarm as soon as there is less than 3 GB of free memory on the drive containing the directory.
- A project alarm for each local session that is more than 5 revisions old.

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Managing certificates

Proceed as follows:

1. Open the graphic tool for the project server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. On the left of the "Administration" tab, click on "Alert".

   There are alerts for both the project server and the individual projects.

   All existing alerts for the selected project server are displayed.
3. If you no longer need an alert and wish to delete it, select the alert and click on the "Delete selected alert" button.

   Result: The selected alert is deleted from the list.

#### Managing server projects and server libraries

##### Introduction

You manage the project groups, server projects, server libraries for a server connection and the sessions created for a server project or a server library with the "Administration Tool".

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Managing server projects and server libraries

Proceed as follows:

| Symbol | Meaning |
| --- | --- |
| 1. Open the graphic tool for the project server administration.    - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".    - Click on the entry "TIA Project Server - Administration" to open the AdministrationTool. 2. To display the details on the right side, click the required entry in the navigation area.    The following information about the projects or libraries is displayed:       | Symbol | Meaning |    | --- | --- |    | "Name" | Name of the server project or the server library |    | "Status" | Status: - "Locked" - "Unlocked" |    | "Mode" | Selected mode: - Engineering mode - Commissioning mode |    | "Created by / date" | Creation of the server project or the server library: - User name - Creation date |    | "Last edited by / Date" | Last change in the server project or in the server library: - User name - Date of change |    | "Project version" | TIA Portal version with which the project or the library was created |    | "Number of local sessions" | Number of local sessions which belong to the server project or to the server library |    | "Comment" | Freely editable field for additional information |                ![Managing server projects and server libraries](images/143145424651_DV_resource.Stream@PNG-en-US.png)         ![Managing server projects and server libraries](images/143145424651_DV_resource.Stream@PNG-en-US.png) 3. To delete a project or a library, select the respective entry and click the "Delete" command.    Projects and libraries can only be deleted if no local sessions exist for them.    Confirm the next prompt to delete the project or the library. 4. To unlock a locked project or a locked library, select the entry and then click the "Unlock" command.    Confirm the next prompt to unlock the project or the library. 5. Click the "Multiuser Commissioning" command to switch to "Commissioning mode".    The icon becomes active and has a blue background.    When commissioning mode is activated, the "Check for different data before download (recommended)" option is simultaneously enabled.    Click the "Multiuser Commissioning" command again to exit "Commissioning mode" and switch back to "Engineering mode". 6. To export a server project or a server library, select the entry on the left side.    Click the "Export" command on the right.    In the next dialog, select the desired storage location. 7. To import a server project or a server library, select a server connection on the left side.    Click the "Import" command on the right.    In the next dialog, select the desired server project or server library for the import. |  |

#### Managing groups on the project server

##### Introduction

You manage the project groups or library groups, server projects, server libraries and associated sessions available for a server connection with the "Administration Tool".

If you are working with several projects and libraries, you can create several groups under the server connection and sort the projects and libraries into these groups.

This procedure also simplifies the clear management of different roles and user rights for several projects.

##### Group name

The same requirements apply for the name of a group as for the project name.

**Prohibited characters**

The following special characters are not allowed in the name:

, ; : ! ? " ‘

+ = / \ @ *

[ ] { } < >

Blank

Case matching is relevant.

##### Requirement

The project server is installed and configured.

To create or delete groups, users need the "Manager" role for the project server.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Displaying and managing groups

Proceed as follows:

1. Open the graphic tool for the project server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. To create a new group, select the server connection and click on "Add group".

   The "Add group" dialog opens.
3. Enter the group name.

   Optionally, add a comment to store the purpose of the group or more information about the group. The comment can consist of several lines.
4. To add a project or a library to the group, select the name of the group under the project server and click "Import".

   To display the correct number of server projects and server libraries on the project server, select the project server and click "Reload".
5. To remove a project or a library from a group, select the name of the project or the library under the group and click "Delete project/library".

   Update the display again with "Reload".
6. To delete an empty group, select the name of the group under the project server and click on "Delete group".

   You can only delete groups which do not contain any projects or libraries. If necessary, first delete the local sessions and projects or libraries under the group.

#### Managing local sessions

##### Introduction

You manage the groups, server projects, server libraries and the associated sessions for a server connection with the "Administration Tool".

Under "Sessions", you can see the local sessions existing respectively for the selected server project or the selected server library.

You can find the "Sessions" entry in the "Administration Tool" below each project or each library.

> **Note**
>
> **Number of revisions**
>
> You set the number of project revisions and library revisions when configuring the project server.
>
> For more details, see: [Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

You have created at least a local session.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Show and delete local sessions

Proceed as follows:

1. Open the graphic tool for the project server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the AdministrationTool.
2. Click "Local sessions" under the required server project or the server library on the left side.

   The following information on the existing local sessions is displayed on the right in the "Administration Tool":

   - "ID": Increments the existing sessions.
   - "Local path": Displays the set local disk space for the sessions.
   - "Computer name": Displays the name of the computer where the session is located.
   - "Last used by": Displays the name of the last editor.
   - "Revision": Displays the project revision or library revision to which each session belongs.

   To update the display after changes, click the "Reload" button.

   ![Show and delete local sessions](images/104492038923_DV_resource.Stream@PNG-en-US.png)

   ![Show and delete local sessions](images/104492038923_DV_resource.Stream@PNG-en-US.png)
3. To delete a session, select the desired session and click the "Delete selected session" command.
4. In the following dialog, click "OK" to delete the selected session.

---

**See also**

[Managing a project server with the graphic Configuration Tool](#managing-a-project-server-with-the-graphic-configuration-tool)
  
[Displaying the history for projects and libraries](#displaying-the-history-for-projects-and-libraries)
  
[Manage revisions](#manage-revisions)

#### Displaying the history for projects and libraries

##### Introduction

You can view the history of the created projects and libraries and manage existing project revisions and library revisions with the graphical "Administration Tool".

The following functions are available:

- Roll back to the selected revision
- Export selected revision
- Export History
- Save revision
- Show details
- Delete revision data (via shortcut menu)

You can find the "History" entry in the "Administration Tool" below each project and each library.

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

You have created at least a local session.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Display and managing history

Proceed as follows:

1. Open the graphic tool for the project server administration:

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Click "History" under the desired server project or the server library on the left side.

   The history displays all the existing revisions.

   The following information on the existing revisions is displayed on the right in the "Administration Tool":

   - "Availability": Indicates whether the session on the server is still available.
   - "Revision number": Displays the revision number.
   - "Computer name": Displays the name of the computer on which the revision was created.
   - "Windows user": Displays the Windows login of the creator.
   - "Server user": Displays the creator's server login.
   - "TIA Portal user": Displays the TIA Portal login of the creator.
   - "Creation date": Displays the creation date of the revision.
   - "Version": Displays the version with which the project or the library was created.
   - "Comment": Displays the comment, if any.
   - "Notes": Displays the number of notes on the revision, if any.

     You can display the notes in the details view.

   To update the display after changes, click the "Reload" button.

   ![Display and managing history](images/137149781131_DV_resource.Stream@PNG-en-US.png)

   ![Display and managing history](images/137149781131_DV_resource.Stream@PNG-en-US.png)
3. You can use the "To roll back selected session" button roll back a selected session to the selected revision.

   A new line is then created showing the new revision with the comment "Rolled back to the revision <number>".
4. To export the revision as a single-user project, click on the "Export selected revision" button.

   Select the desired storage path in the subsequent dialog and click "OK".
5. To export the history as an XML file, select the required revisions and click the "Export history" button.

   Enter the required data in the subsequent dialog and click "Save".
6. To save the revision, click on the "Save revision" button.

   In the following dialog, enter a note on the revision to be saved and click on "Save revision".

---

**See also**

[Managing local sessions](#managing-local-sessions)
  
[Manage revisions](#manage-revisions)

#### Manage revisions

##### Introduction

You can manage existing project revisions and library revisions with the graphical "Administration Tool".

The following functions are available:

- Roll back to the selected revision
- Export selected revision
- Save revision
- Show details
- Delete revision data (via shortcut menu)

You can find the "History" entry in the "Administration Tool" below each project and each library.

##### Requirement

The project server is installed and configured.

You have already created projects or global libraries as server projects or server libraries in TIA Portal.

You have created at least a local session.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Roll back to the selected revision

Proceed as follows:

1. Select the desired revision or multiple revisions and click the command "Roll back to the selected revision" in the shortcut menu.

   A new line is then created showing the new revision with the comment "Rolled back to the revision <number>".

##### Export selected revision

Proceed as follows:

1. Select the desired revision or multiple revisions and click the command "Export selected revision" in the shortcut menu.
2. Select the desired storage path in the subsequent dialog and click "OK".

##### Save revision

Proceed as follows:

1. Click "Save Revision".
2. In the following dialog, enter a note on the revision to be saved and click on "Save revision".

##### Display details about a revision

You can use the button "Display details" to show more information about a selected revision in a detail window within the history for versions.

- You can add notes in the "Details" tab.

  To do so, click on the link and enter the required note in the following dialog.

  Click "Add note" to apply the note.
- In the "Changed objects" tab you see all the changes made in the selected project or in the library.

  ![Display details about a revision](images/104501334283_DV_resource.Stream@PNG-en-US.png)

##### Deleting revision data

Proceed as follows:

1. Select the desired revision or revisions and click the command "Delete revision data" in the shortcut menu.
2. Confirm the prompt in the dialog that follows with "OK".

**Result**:

The data of the selected revision is deleted.

All relevant information on the change history of the revision is retained.

The revision is no longer displayed under "Availability" and rollback to this revision is no longer possible.

> **Note**
>
> **The data for the following revisions cannot be deleted:**
>
> - Revisions displayed in the "Availability" column without a symbol.
>
>   Access to these revisions is no longer possible.
> - Revisions with the "Retain" label.
>
>   You have already labeled these revisions as "secured".
> - The last revision of a project or a library.
>
> If you attempt to delete the data for the revisions listed above, you will receive an error message.

---

**See also**

[Managing local sessions](#managing-local-sessions)
  
[Displaying the history for projects and libraries](#displaying-the-history-for-projects-and-libraries)

#### Switching back and forth between engineering and commissioning mode

##### Introduction

You use the graphical "Administration Tool" to switch back and forth between engineering and commissioning mode. You always set the mode for all local sessions of a server project. All local sessions can either be in engineering mode or in commissioning mode. The default setting is engineering mode.

When you switch to commissioning mode, the "Check for different data before download (recommended)" button is also selected automatically. This is a recommended setting for working with Multiuser Commissioning. The check set in this way ensures that no data deviating from the server project is loaded into the CPU. This can be the case, for example, if check-in to a server project from a previous local session took place without a download to the CPU.

If there are deviations between the data available in the server project and the data loaded to the CPU, a dialog is displayed that informs you how to proceed.

Deviating data can be cleaned up in the server project view.

##### Requirement

The project server is installed and configured.

You have already created projects as server projects and have created at least one local session in the TIA Portal.

> **Note**
>
> **Server projects and local sessions**
>
> If you have not yet created server projects and local sessions on the project server in the TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Enabling and disabling commissioning mode

Proceed as follows:

1. Open the graphic tool for the server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Under "Administration", you can find a list of the configured server connections as soon as you have set up a connection to the project server with "Add server connection". On the right side, you receive additional information about the objects selected on the left in a detail view.
3. On the left side, select the server and the project for which you want to set up commissioning mode.
4. On the right side, click the "Multiuser Commissioning" button in the header to activate commissioning mode.

   - As soon as the button is active, it is given a blue background and the project selected on the left side receives the commissioning symbol as overlay.
   - With commissioning mode, the "Check for different data before download (recommended)" option is also activated.

   ![Enabling and disabling commissioning mode](images/115233591051_DV_resource.Stream@PNG-en-US.png)

   ![Enabling and disabling commissioning mode](images/115233591051_DV_resource.Stream@PNG-en-US.png)

   Click the "Multiuser Commissioning" button in the toolbar again to exit "commissioning mode".

   - As soon as the button is deactivated, it has no color and no overlay symbol is displayed for the project selected on the left side.
   - With commissioning mode, the "Check for different data before download (recommended)" button is also deactivated.

##### Result

The "commissioning mode" is switched on by clicking the "Multiuser Commissioning" button and switched off by clicking it again.

#### Selecting a user interface language

##### Introduction

You use the graphical "Administration Tool" to select the required user interface language in the "Settings" > "General" tab.

All six TIA Portal languages are available.

##### Requirement

The project server is installed and configured.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Changing the language

Proceed as follows:

1. Open the graphic tool for the server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Click on the left on the "Settings" > "General" tab.

   In the "Language" section, select the required user interface language from the drop-down list.

##### Result

The interface texts are displayed in the selected language.

#### Displaying confirmations

##### Introduction

In the graphical "Administration Tool", in the "Settings" > "General" tab, select for which actions a confirmation dialog is displayed when working with Multiuser Engineering. To carry out these actions, the operator must confirm the execution.

You can activate confirmations for working in the following areas:

- User administration
- Deleting a server connection
- Deleting a local session
- Unlocking a project / library
- Deleting a project / library
- Exporting a revision to a folder that is not empty
- Deleting a notification
- Publishing a revision
- Deleting revision data
- Exporting a server project / server library
- Deleting a group

##### Requirement

The project server is installed and configured.

> **Note**
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Selecting a confirmation

Proceed as follows:

1. Open the graphic tool for the server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Click on the left on the "Settings" > "General" tab.
3. Go to "Confirmations" and click on the required actions.

   - You enable confirmations for all entries using the "All" button.
   - You disable confirmations for all entries using the "None" button.

#### Managing certificates

##### Introduction

You can use the graphical "Administration Tool" to view and manage existing certificates for the project server on the "Settings" > "Certificate" tab. As soon as you select "https" for the server connection, certificates are used for secure communication.

Certificates that are no longer required can be deleted if not in use.

If you try to delete a certificate that is currently in use in an active server connection, a corresponding message is output.

##### Requirement

The project server is installed and configured.

> **Note**
>
> **Certificate Transparency**
>
> Note that no check of existing digital certificates is performed in the project server.
>
> **No display in Administration Tool**
>
> If you have not yet created server projects or server libraries with local sessions in TIA Portal, no information regarding these will be displayed when you administer the project server.

##### Managing certificates

Proceed as follows:

1. Open the graphic tool for the server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Click on the left on the "Settings" > "Certificates" tab.

   All existing certificates for the selected project server are displayed with the associated data.
3. If you no longer need a certificate and wish to delete it, select the certificate and click on the "Remove selected certificate confirmation" button.

##### Result

The selected certificate is deleted from the list.

If the certificate is currently in use in an active server connection, you receive a message stating that the certificate will not be deleted until the system is restarted.

### Using the command line tools

This section contains information on the following topics:

- [Introduction to the command line tools](#introduction-to-the-command-line-tools)
- [Configuring the project server with the administrative tools](#configuring-the-project-server-with-the-administrative-tools)
- [Commands for configuring the project server](#commands-for-configuring-the-project-server)
- [Managing the project server with the power tools](#managing-the-project-server-with-the-power-tools)
- [Commands for managing the project server](#commands-for-managing-the-project-server)

#### Introduction to the command line tools

##### Introduction

The project server can be configured and managed with the help of the Administrative Tools and the Power Tools .

The Power Tools are also available in the TIA Portal for administrative tasks on the project server.

##### Requirement

The project server is installed.

You need administrator rights to configure the project server with the Administrative Tools.

You require user rights for administrative tasks with the Power Tools.

##### Configuration of the project server with the Administrative Tools

The server is installed and managed using a command line command.

To configure the project server, the following steps are required:

- Open the Project Server Administrative Tools with administrator rights.
- The complete installation is executed with the command:

  `prjsrv install –r d:\TIA\SRV –p 5080 –b https`
- The project directory (repository) is created automatically.
- The definition of the protocol and the port address is already contained in this command, together with the integrated certificate administration for secure HTTPS communication.
- Windows tools are used to create new certificates and select existing certificates.
- You can find additional commands for configuring the project server here: [Commands for configuring the project server](#commands-for-configuring-the-project-server)

> **Note**
>
> **Enabling the firewall port**
>
> The specified port is automatically enabled in the firewall for access to the project server.

##### Managing the project server with the power tools

To manage the project server, the following steps are required after the installation of the server:

- To access the project server, a port may have to be enabled in the firewall.
- To manage the project server, open the server management or the Project Server Power Tools.
- You can find additional commands for managing the project server here: [Commands for managing the project server](#commands-for-managing-the-project-server)

##### User and rights management

The user and rights management for the project server is based on the user management for the Windows user accounts.

- Project-specific rights assignment is possible.
- The use of group guidelines enables simple, fast and clear assignment of rights.

##### Project management

Project management enables clear and convenient management of the existing groups, server projects and server libraries as well as the associated local sessions.

The project management can be automated by scripts (batch files).

##### Error messages

If an action cannot be executed successfully, a corresponding error message is displayed.

You can find the error descriptions in the corresponding tools by calling the help for the tools:

**Calling help in the Administrative Tools**

- Open the Administrative Tools as follows:
- Copy the command "prjsrv" to the command line and press "Enter".

**Calling help in the Power Tools**

- Open the Power Tools as follows:
- Copy the command "pspt" to the command line and press "Enter".

---

**See also**

[Commands for configuring the project server](#commands-for-configuring-the-project-server)
  
[Commands for managing the project server](#commands-for-managing-the-project-server)

#### Configuring the project server with the administrative tools

##### Introduction

Before you can use the installed external project server as part of Multiuser Engineering, the server must be configured.

When you configure the project server using the Administrative Tools, you use the commands described below, which you execute in the command line.

The following actions are automatically executed when you input the "Install" command described below:

- The Windows service for the project server is installed.
- A firewall activation for the specified port is added via a TCP connection.
- Performance monitoring is installed to monitor the project server.
- The storage directory, called "Repository", is created if it does not already exist.
- The "binding" is defined, whether you use "https" (recommended) or "http" as transfer protocol.
- The "fingerprint" to confirm a valid certificate is transferred to the server.

The project server can then be used.

##### TIA Portal versions < V18

Up to TIA Portal V17, the Administrative Tools were referred to as "Multiuser Administrative Tools" and addressed via the command "musrv".

If you are working with project servers from versions prior to TIA Portal V18, replace the command "prjsrv" with "musrv" in the commands.

**TIA Portal V18: Commands from predecessor versions**

You can also address a project server that was created with TIA Portal V18 with the command "musrv".

To use the commands in future TIA Portal versions, replace "musrv" in each case with "prjsrv".

##### Requirement

The project server is installed.

You need administrator rights to configure the project server.

> **Note**
>
> The commands as well as the associated help and information texts within the command line are only available in English.

##### Procedure

To configure the project server, follow these steps:

1. Open the tool for the server configuration with administrator rights.

   Under "bin" in the installation directory of the TIA Portal, double-click on the file "start-prjsrv.bat" to do this.
2. Copy the following command for server configuration with the required parameters to the command line and press "Enter".

   Command:

   - `prjsrv install -r <repository-path> -p <port> -b <binding> -h <certificate-hash>`

   Example of the entry:

   - `prjsrv install -r c:\TIA\SERVER -p 5080 -b https -h <certificate-hash>`
3. If the "prjsrv install" command could not be executed successfully, you receive an error message for which you can view an explanation.

   Once these commands have been executed successfully, the project server is configured.

##### Configuration example

If you do not enter any parameters, the system prompts you for the required parameters.

| Command | Description |
| --- | --- |
| Define "Repository-path"  Used in the above example:   `-r c:\TIA\SERVER` | Enter the name and the path of the directory (Repository) in which the server is to save the files.  If you enter a new directory that does not exist yet, the directory is automatically created by the system.   **Note:**   This directory and the data storage are retained even after deleting the server.  If you reinstall the project server after deleting it and enter an existing directory as "Repository", the data is also available on the new server without any restrictions. |
| Define "Port"  Used in the above example:   `-p 5080` | Enter the port you want to use for communication with the project server. |
| Define "Binding"  Used in the above example:   `-b https` | Define whether you want to use "https" (recommended) or "http" as transfer protocol.  With "https", communication is encrypted and a certificate is requested. This means communication has a higher security level than the unencrypted "http" communication. |
| "Certificate hash" = fingerprint for the certificate used | For secure server communication, enter the fingerprint for the certificate you created or the certificate used.  For more information on creating a certificate, refer to the Help for the respective Windows operating system. |
| "Run service" = Start service  Example:   `prjsrv start` | Use it to start the Windows service for the project server. |

You can find additional commands for configuring the project server here: [Commands for configuring the project server](#commands-for-configuring-the-project-server)

---

**See also**

[Commands for configuring the project server](#commands-for-configuring-the-project-server)

#### Commands for configuring the project server

##### Introduction

Commands for configuring the project server are available in the Administrative Tools.

Observe the basic procedures for configuring the project server: [Configuring the project server with the administrative tools](#configuring-the-project-server-with-the-administrative-tools)

> **Note**
>
> The commands as well as the associated help and information texts within the command line are only available in English.

##### TIA Portal versions < V18

Up to TIA Portal V17, the Administrative Tools were referred to as "Multiuser Administrative Tools" and addressed via the command "musrv".

If you are working with project servers from versions prior to TIA Portal V18, replace the command "prjsrv" with "musrv" in the commands.

**TIA Portal V18: Commands from predecessor versions**

You can also address a project server that was created with TIA Portal V18 with the command "musrv".

To use the commands in future TIA Portal versions, replace "musrv" in each case with "prjsrv".

##### Commands for configuring the project server

The commands listed below are available:

| Command | Description | Possible entries |
| --- | --- | --- |
| "Install" | Installs the project server and enables communication with the server.  A configuration example is available at:   [Configuring the project server with the administrative tools](#configuring-the-project-server-with-the-administrative-tools) | **Parameters:**   - -r, --repository: Directory in which the server data is to be stored. - -p, --port: Port number for the server access - -b, --binding: Specifies the protocol for the communication (http or https) - -d, --debug: (optional): Defines whether runtime debug information is displayed by the server.   Note: If you use the option "-d", no debug logs are displayed. - -h, --certhash: Fingerprint of the certificate which is to be used for secure data transfer (is only required for https). - -t, --timeout: (optional): Definition of the utilized timeout profile ("fast", "middle" or "slow"). Default: "fast". - -f, --force: (optional): Activates the command without further query - -c, --count: Maximum number (1 to 10) of the saved project versions.    **Example**:   `prjsrv install -r <repository-path> -p <port> -b <binding> -h <certificate-hash>` |
| "Config" | Displays the current configuration of the project server and offers optional dynamic configuration parameters. | **Parameters:**   - -t, --timeout: (optional): Definition of the utilized timeout profile ("fast", "middle" or "slow"). - -c, --count: Maximum number (1 to 10) of the saved project versions. - -d, --debug: (optional): Defines whether runtime debug information is displayed by the server.   Note: If you use the option "-d", no debug logs are displayed.    **Example:**   prjsrv config -d |
| "Start" | Starts the project server. | **Parameters:**   - No parameters available    **Example:**   prjsrv start |
| "Stopp" | Stops the project server. | **Parameters:**   - -f, --force: (optional): Activates the command without further query    **Example:**   prjsrv stopp |
| "Uninstall" | Uninstalls the project server.  Uninstallation can also take place with Windows mechanisms. | **Parameters:**   - -f, --force: (optional): Activates the command without further query    **Example:**   prjsrv uninstall |

---

**See also**

[Configuring the project server with the administrative tools](#configuring-the-project-server-with-the-administrative-tools)

#### Managing the project server with the power tools

##### Introduction

To manage server projects, server libraries and local sessions on the project server, use the commands described below that you can execute with the help of the Power Tools in the command line.

The project server can be managed via the Power Tools from any computer on which TIA Portal and Power Tools are installed.

Your entries are stored in a "Session memory" and are then available the next time the Power Tools are opened.

> **Note**
>
> You need user rights to manage the project server.

##### Open Project Server Power Tools

You start the Power Tools using the file "start-pspt.bat".

In the commands, address the Power Tools via "pspt".

Description of the Project Server Power Tools commands:

- [Commands for managing the project server](#commands-for-managing-the-project-server)

**TIA Portal versions < V18**

Up to TIA Portal V17, the "Multiuser Power Tools" were called via the file "start-mupt.bat".

If you are working with project servers from versions prior to TIA Portal V18, use the command "mupt" in the commands.

##### Requirement

The project server is installed.

A port is enabled in the Windows firewall so that the project server is accessible.

You have administrator rights.

##### Procedure

To configure the project server, follow these steps.

1. Open the Power Tool for the server administration with administrator rights.

   Under "bin" in the installation directory of the TIA Portal, double-click on the file "start-pspt.bat" to do this.
2. Copy the command "pspt" to the command line and press "Enter".

   The help for the multiuser power tools is displayed.
3. Enter the required command for server management in the command line and press "Enter".
4. If the command could not be executed successfully, you receive an error message.

---

**See also**

[Commands for managing the project server](#commands-for-managing-the-project-server)

#### Commands for managing the project server

##### Introduction

The commands for managing the project server are available in the Project Server Power Tools.

> **Note**
>
> The commands as well as the associated help and information texts within the command line are only available in English.

##### TIA Portal versions < V18

Up to TIA Portal V17, the Power Tools were referred to as "Multiuser Power Tools" and addressed via the command "mupt".

If you are working with project servers from versions prior to TIA Portal V18, replace the command "pspt" with "mupt" in the commands.

**Functional scope of the commands**

As the functional scope TIA Portal V18 and higher was extended, for example, to include group management, not all commands are available for predecessor versions.

Consult the documentation of the predecessor versions to find out about the functional scope of the project server version used.

**TIA Portal V18: Commands from predecessor versions**

You can also address a project server that was created with TIA Portal V18 with the command "mupt".

To use the commands in future TIA Portal versions, replace "mupt" in each case with "pspt".

##### "User names" and "Role names"

**User names**

All "User names" used must comply with this format:

- <domain-or-machine-name>\<account>

  Examples: ww004\userTIA01, PC17CLTC\tiaengineer01

  If the <domain-or-machine-name> is not assigned, Windows will automatically propose a corresponding domain for the account.

**Role names**

The following "Role names" with the corresponding access rights are available:

| Symbol | Meaning |
| --- | --- |
| Manager | Read  Write  Delete  User administration |
| Contributor | Read  Write  Delete: Only server projects, server libraries and local sessions |
| Member | Read-only |

##### Commands for managing the project server

The commands listed below are available.

> **Note**
>
> **Description / inputs: Server libraries correspond to server projects**
>
> To make the description of the commands clearer the following table does not list libraries as well as projects.
>
> All descriptions for server projects also apply for server libraries.

| Command | Description | Possible entries |
| --- | --- | --- |
| "Show projects" | Lists projects and groups of the selected project server. | **Parameters:**   - -s, --server: Project server URL address - -a, --all: Outputs a list with the full hierarchy of all groups and server projects on the server. - -p, --project: (Optional) Name of the server project.   The parameter is only evaluated if revisions can be displayed for a project.   If the command contains the parameter "all", the parameter "project" is ignored. - -v, --revisions: (Optional) Also lists all revisions for the project.   If the command contains the parameter "all", the parameter "revisions" is ignored. - -l, --page: (Optional) Page by page result display - -d, --display: (Optional) Result display in different form:   - cascade: Displays the results as cascade.   - tabular: Displays the results as table.   - short: Displays the results as summary. - -g, --groupName: Name of the group if the server project is contained in a group.   If the command contains the parameter "all", the parameter "groupName" is ignored.    **Examples:**   Full list of the groups and projects:  %InstallDirectory% > pspt project show --server https://localhost:8735 -a  Server projects of the "MyGroup" group:  %InstallDirectory% > pspt project show --server https://localhost:8735 -g MyGroup   **Help:**   - `pspt project show -?` |
| "Delete project" | Deletes specific projects on the project server.   **Requirements:**   The projects must not contain any local sessions. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project to be deleted. - -f --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt project remove --server https://localhost:8735 --project project155 -g MyGroup   **Help:**   - `pspt project remove -?` |
| "Create group" | Creates a group on the project server.   **Requirements:**   Users need the "Manager" role for the project server | **Parameters:**   - -s, --server: Project server URL address - -g, --groupName: Name of the group to be created - -c, --comment: Comment with information, for example, the purpose of the group.    **Example:**   %InstallDirectory% > pspt group create --server https://localhost:8735 --g MyGroup --c GroupComment   **Help:**   - `pspt group create -?` |
| "Get group" | Lists all groups of the selected project server.  To list both the groups and the contained server projects, use the command "project show" with the parameter "all". | **Parameters:**   - -s, --server: Project server URL address    **Example:**   %InstallDirectory% > pspt group get --server https://localhost:8735   **Help:**   - `pspt group get -?` |
| "Delete group" | Deletes a group on the project server.   **Requirements:**   The group must not contain any server projects.  Users need the "Manager" role for the project server | **Parameters:**   - -s, --server: Project server URL address - -g, --groupName: Name of the group to be deleted - -f, --force: (Optional) Activates the command without further query.   Without the parameter in the command, a confirmation dialog is displayed.    **Example:**   %InstallDirectory% > pspt group delete --server https://localhost:8735 -n MyGroup   **Help:**   - `pspt group delete -?` |
| "Display sessions" | Lists all local sessions of the selected server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project whose sessions are listed. - -l, --page: (Optional) Page by page result display - -d, --display: (Optional) Result display in different form:   - cascade: Displays the results as cascade.   - tabular: Displays the results as table.   - short: Displays the results as summary. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt session show --server https://localhost:8735 --project project155 -g MyGroup   **Help:**   - `pspt session show -?` |
| "Move session" | Updates the storage path of a local session which was moved to another path. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project to which the local session belongs. - -i, --id: ID of the local session to be moved. - -t, --path: Selection of the destination folder to which the local session is to be moved. - -m, --machine: (Optional) Name of computer if the destination folder is on a different PC. - -f, --force: (Optional) Activates the command without further query. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt session move --server https://localhost:8735 -id 1 --project Project1 --path C:\LocalPathForMoving -g MyGroup   **Help:**   - `pspt session move -?` |
| "Delete session" | Deletes the selected local session on the project server | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project whose session is to be deleted. - -i, --id: Identification number of the session to be deleted. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt session remove --server https://localhost:8735 --project project155 --id 5 -g MyGroup   **Help:**   - `pspt session remove -?` |
| "Remove project lock" | Removes the lock for the server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project to be unlocked. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt project unlock --server https://localhost:8735 --project project155 -g MyGroup   **Help:**   - `pspt project unlock -?` |
| "Show check-in history" | Displays the check-in history for the selected server and the selected local session. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project for whose sessions the check-in history is listed.   If no project name is specified, the history of all projects is listed on the project server. - -f, --from: (Optional) Revision number from which the history of the session is to be listed.   The specified revision number is included in the list.   Without the parameter in the command, the check-in history since the creation of the session is displayed. - -t, --to: (Optional) Revision number up to which the history of the session is to be listed.   The specified revision number is included in the list.   Without the parameter in the command, the check-in history up to the current time is displayed. - -i, --id: (Optional) Identification number of the session whose check-in history is to be listed.   If no session identification number is specified, the history for all sessions of the sever project is listed. - -l, --page: (Optional) Page by page result display - -d, --display: (Optional) Result display in different form:   - cascade: Displays the results as cascade.   - tabular: Displays the results as table.   - short: Displays the results as summary. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt checkin show --server https://localhost:8735 --project project155 --from 5 --to 20 --id 5 -g MyGroup   **Help:**   - `pspt checkin show -?` |
| "Show server access rights" | Shows the defined user rights for the users of a server, a group or a server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project for which the access rights are listed.   If no project name is specified, the access rights of all projects are listed on the project server. - -l, --page: Results display in page format - -d, --display: (Optional) Result display in different form:   - cascade: Displays the results as cascade.   - tabular: Displays the results as table.   - short: Displays the results as summary. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example**:  %InstallDirectory% > pspt user show --server https://localhost:8735/ -p MYProject -g MyGroup   **Help:**   - `pspt user show -?` |
| "Modify server access rights" | Changes the access rights for the server, a group or a server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project for which the user is to be granted access rights.   If no project name is specified, the user is granted access rights to the project server. - -u, --users: User names to be used for filtering, separated by commas. - -r, --role: Selecting the role - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt user add --server https://localhost:8735 --project Project1 --users user1,user2 --role Manager -g MyGroup   **Help:**   - `pspt user add -?` |
| "Remove server access rights" | Removes the access rights for the server, a group or a server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project from whose user administration the user is to be removed.   If no project name is specified, the user is removed from the user administration of the server. - -u, --user: User names to be used for filtering, separated by commas. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt user remove --server https://localhost:8735 --users user1,user2 -g MyGroup   **Help:**   - `pspt user remove -?` |
| "Show certificates" | Displays all existing multiuser certificates. | **Parameters:**   - -l, --page: (Optional) Option to divide up the pages to display the results.   -d, --display: (Optional) Result display in different form:   - cascade: Displays the results as cascade.   - tabular: Displays the results as table.   - short: Displays the results as summary.    **Example**:  %InstallDirectory% > pspt certificate show   **Help:**   - `pspt certificate show -?` |
| "Remove certificates" | Removes all certificates from the selected server. | **Parameters:**   - -s, --server: Project server URL address - -f, --force: (Optional) Activates the command without further query    **Example**:  %InstallDirectory% > pspt certificate remove --server https://localhost:8735   **Help:**   - `pspt certificate remove -?` |
| "Confirm certificate" | Saves the certificate for the selected server in the list of valid certificates. | **Parameters:**   - -s, --server: Project server URL address - -f, --force: (Optional) Activates the command without further query    **Example**:  %InstallDirectory% > pspt certificate confirm --server https://localhost:8735   **Help:**   - `pspt certificate confirm -?` |
| "Show alerts" | Displays the alerts for the selected server. | **Parameters:**   - -s, --server: Project server URL address    **Example:**   %InstallDirectory% > pspt alert show --server https://localhost:8735   **Help:**   - `pspt alert show -?` |
| "Remove alerts" | Removes all alerts for the selected server. | **Parameters:**   - -s, --server: Project server URL address - -a, --alert: Name of the alert    **Example:**   %InstallDirectory% > pspt alert remove --server https://localhost:8735 --alert alert1   **Help:**   - `pspt alert remove -?` |
| "Export of server project" | Exports an existing server project to the destination folder in the specified path. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project to be exported.   If no project name is specified, all projects in the specified server repository are exported. - -t, --path: Selection of the destination folder to which the project is to be exported.   The folder must be empty. - -m, --metadata: (Optional) The server project is exported completely with the entire history and all existing revisions.   Default setting: Without the parameter in the command, the last revision version or the version specified with "revision" is exported. - -v, --revision: (Optional) Defines the revision number which is to be exported.   Default setting: Without specification of a version, the last revision is exported.   If a specific revision is specified, the server project is exported as a single-user project.   If the command contains the parameter "metadata", the parameter "revision" is ignored. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example**:  %InstallDirectory% > pspt project export --server net.tcp://localhost:8637 --project Project55 --path "E:\Exp1" -m -g MyGroup   **Help:**   - `pspt project export -?` |
| "Import of server project" | Imports a server project from the specified path to the specified project server repository.   **Requirements:**   Only users with the role "Contributor" or "Manager" are permitted to execute this action.   **Rules:**   - You can only import one server project at a time. - The name of the server project to be imported is also used as the name of the destination folder. | **Parameters:**   - -s, --server: Project server URL address - -t, --path: Selection of the storage path from which the project is to be imported. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example**:  %InstallDirectory% > pspt project import --server https://localhost:8735 --path "E:\Exp1" -g MyGroup   **Help:**   - `pspt project import -?` |
| "Export of server project sessions" | Exports the local sessions of a server project to the specified path. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project whose associated local sessions are to be exported.   If no project name is specified, all projects in the specified server repository are exported. - -t, --path: Selection of the destination folder to which the local sessions of the server project are to be exported.   The folder must be empty. - -i--id: (Optional) ID of the local session which is to be exported. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt session export --server net.tcp://localhost:8637 --project Project55 --path "E:\Exp1\Sessions" [--id] 1 -g MyGroup   **Help:**   - `pspt session export -?` |
| "Import of server project sessions" | Imports the exported local sessions to a selected server project.   **Requirements:**   Only users with the role "Contributor" or "Manager" are permitted to execute this action.   **Rule:**   Only the local sessions known to the associated server project are imported. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project whose associated local sessions are to be imported. - -t, --path: Selection of the storage path from which the local sessions are to be imported. - -a, --alias: (Optional) Alias name of the destination server, if available. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt session import --server https://localhost:8735 --project Project55 --path "E:\Exp1\Sessions" -g MyGroup   **Help:**   - `pspt session import -?` |
| "Export project history as xml" | Exports the existing project history to an existing file in ".xml" format. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project whose associated history is to be exported. - -t, --file: Target file and storage path for exporting the history. - -v, --revision: (Optional) Revision number for which the history is to be exported.   If no revision number is specified, the history for all revisions of the sever project is listed. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt project exportHistory -s http://server.com -p Project1 -t "C:\fileName.xml" -v 1,2,3,4 -f -g MyGroup   **Help:**   - `pspt project exportHistory -?` |
| "Add note to a revision in server project" | Adds a note to a selected revision of a server project. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project. - -v, --revision: Revision to which a note is to be added.   If no revision number is specified, the note is added to all revisions of the sever project. - -n--note: Note to be added to the revision   Use the parameter "\n" in the text to add a line break.   Escape sequence: If the text contains functional characters, use the character "\" as an escape sequence. - -g, --groupName: Name of the group if the server project is contained in a group.    **Example:**   %InstallDirectory% > pspt revisionnote add -s http://server.com -p Project1 -v 1 -n "MyNoteLine1\nLine2Note" -g MyGroup   **Help:**   - `pspt revisionnote add -?` |
| "Project Commissioning" | Activates or deactivates commissioning mode for the selected server project.  This command is not available for server libraries. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project for which the commissioning mode is to be activated or deactivated. - -m, --mode: Activates or deactivates the commissioning mode.   - true: Activates the commissioning mode.   - false: Deactivates the commissioning mode.To activate the commissioning mode, add the "mode" parameter in the command.   Without the parameter in the command, the commissioning mode is deactivated.   You decide whether the synchronous or asynchronous commissioning mode is used in the commissioning configuration in the TIA Portal. - -d, --divergent: Activates or deactivates the option "Check for different data before download".   - true: Activates the consistency check.   - false: Deactivates the consistency check.To activate the consistency check, add the "divergent" parameter in the command.   Without the parameter in the command the consistency check remains deactivated. - -n, --groupName: Name of the group to be created    **Example:**   %InstallDirectory% > pspt project commissioning --server https://localhost:8735 -p Project1 -m true -d true -g MyGroup   **Help:**   - `pspt project commissioning -?` |
| "Project rollback" | Resets the server to an existing older revision.   **Requirements:**   The command can only be executed if the server is not locked. | **Parameters:**   - -s, --server: Project server URL address - -p, --project: Name of the server project that is to be reset to a previous revision. - -v, --revision: Revision number to which the project is to be reset. - -f, --force: (Optional) Activates the command without further query - -g, --groupName: Name of the group if the server project is contained in a group.    **Example**:  %InstallDirectory% > pspt project rollback --server https://localhost:8735 --project projectName --revision 2 --group MyGroup   **Help:**   - `pspt project rollback -?` |

### Confirm certificate for project server

#### Introduction

When working with Multiuser Engineering , you must first specify the SSL Server certificate in order to establish a secure connection to an installed project server. As soon as you start working in a local session for the first time after installation of the server, you are prompted to confirm the displayed certificate.

When an existing certificate has expired, you are prompted to confirm it again.

The mechanisms provided by Windows are used for managing the SSL server certificates.

If you do not confirm the SSL server certificate, a connection to the project server cannot be established.

#### Requirement

You have installed TIA Portal and the required project server software.

The project server must be configured and started with the help of the power tools.

You are working in the local session for the first time.

#### Confirm certificate for project server

To confirm the certificate for the project server, follow these steps:

1. When you are working with a connected project server for the first time, for example, when opening a local session, the operating system automatically prompts you to confirm the server certificate for the project server.
2. Check whether the displayed certificate is trustworthy. If so, click "OK" in the dialog that appears to confirm the certificate for the "TIA_Project_Server".

#### Result

The dialog is closed. The certificate for the project server is considered trustworthy and saved permanently.

### Enter access data for project server

#### Introduction

If you have installed a project server, you must log on to the project server if an authentication is required.

In this case the project server prompts you to log on. A dialog is displayed in which you can enter the access data.

You have two options for logging on:

- Logon with your current Windows-user name and password
- Logon with the access data of a different user

#### Requirement

The TIA Portal and a project server are installed.

The project server must be configured and started with the help of the Power Tools.

#### Enter access data for project server

To enter the user data, follow these steps:

1. Select the required option in the dialog by clicking it.

   - For logon with your current login, the user name is already entered and cannot be edited.
   - Alternatively, you can log on with the access data of a different user.
2. To do so, select the second option and enter the respective data for "User name" and "Password".
3. Click "OK".

#### Result

If authentication was successful, the dialog is closed and the connection to the project server is established.

### Transferring server data to other project server

#### Introduction

If you work with Multiuser Engineering and have installed a project server, you can transfer existing server data to another project server without data loss.

The data can be transferred to the same computer or to a another computer.

> **Note**
>
> **Safe storage location for the server project to be exported**
>
> Make sure that you specify a safe storage location for the server project to be exported to prevent loss or misuse of your data.

#### Transferring server data to other project server

To transfer the project server data of a project server to another project server, follow these steps:

1. Stop the active project server.

   - Open the graphic ConfigurationTool for the project server configuration with administrator rights.
   - Open the start menu by clicking the command "Start" > "All Programs" > "Siemens Automation".
   - Click the "TIA Project Server - Configuration" entry.

     This will open the user interface of the Configuration Tool.
   - Click the "Stop service" button" in the Server status" area.
2. Uninstall the "old" project server.

   For more details, see: Installing and uninstalling the project server
3. Copy the entire repository with the existing server data to the new storage location, for example, to another computer.
4. Install the project server on the new computer.

   For more details, see: Installing and uninstalling the project server
5. Configure the new storage directory for the new project server.

   For more details, see: [Configuring the project server with the Configuration Tool](#configuring-the-project-server-with-the-configuration-tool)
6. Start the new project server. In the Configuration Tool, click on "Start service" in the "Server status" area.

#### Result

The server data was transferred without data loss to the new project server.

---

**See also**

[Configuring the project server with the Configuration Tool](#configuring-the-project-server-with-the-configuration-tool)
  
Installing and uninstalling the project server

### Read out error log for project server

#### Introduction

To check the server functionality of the project server, you can read out the error logs.

When server errors occur, the error logs provide you with additional information on the error messages displayed in the user interface.

A separate log file is created by the server for each day.

The log files are not deleted automatically.

#### Read out error logs for a project server

To read out the error log, follow these steps:

1. Open the directory for the respective project server in your archiving.
2. Select the desired log file under the path <Repository>\logs.
3. Open the requested log file to check the content

#### Read out error logs for server projects / server libraries

To read out the error log, follow these steps:

1. Open the directory for the respective project server in your archiving.
2. Select the desired log file under the following path:

   <Repository>\proj\<Project name or library name>\logs
3. Open the requested log file to check the content.

> **Note**
>
> **Reading out the error log**
>
> Keep in mind that the error log cannot be read out when you are working in debug mode.
>
> Check and/or change the server configuration in the command line via the Administrative Tools using the command "prjsrv config".
>
> Make sure that the option "-d" is not selected.

#### Reading out Windows event view

The event view is a tool with which detailed information about important events can be displayed on the computer. The event view can be helpful for dealing with problems and errors.

The following security relevant events relating to the project server also receive an entry in the Windows event view:

- If a user wants to the start the project server and the project server does not "know" this user; i.e. the user is not logged in on the server.
- If a user with an incorrect password wants to log on to the project server.

To read out the event view, follow these steps:

1. Click "Start" > "Control Panel" > "System and Security" > "Administration".

   Alternatively, click "Start" and enter "Event view" in the search field.
2. Double-click to open the Event view.
3. Under "Windows protocols" click "Security" to display the logged security relevant events related to the project server.

#### Result

The logged security relevant events for the project server are shown in a list.

### Pack error log for project server as Zip file

#### Introduction

To check the server functionality of the project server, you can read out the error logs.

When server errors occur, the error logs provide you with additional information on the error messages displayed in the user interface.

You have the option of packing all existing error logs into a Zip file and forward them to Customer Support, for example.

You cannot execute this action via the TIA Portal or via the Administrative Tools or Power Tools.

#### Requirement

You need administrator rights.

#### Packing error logs as Zip file

To create a Zip file for error logs, follow these steps:

1. Log onto the project server as administrator.
2. Execute the command "prjsrv ziplogs".
3. Alternatively, you can execute the command with the following options:

   - -n, --name: Entering the storage path for the Zip file
   - -f, --force: Overwrites any existing Zip files without prompt.

#### Result

The Zip file with all existing error logs for the project server is created.

### Information on response of the project server to errors

#### Introduction

The response of the project server after the occurrence of an error is described below.

If an error occurs, you receive a corresponding error message.

#### Behavior of the project server after the occurrence of an error

The project server exhibits the following behavior after the occurrence of an error:

**Project lock:**

- Information on which project is locked may get lost after a server error.
- This information is no longer available after a restart.

**Errors that occur during "Upload from device" or "Download to device":**

- The refresh of the local session cannot be performed. The action is aborted with an error message.
- The check-in cannot be executed. The action is aborted with an error message.
- Any already loaded data are removed again from the project server, the server has the same status as before the start of the faulty action.

> **Note**
>
> **Manual restart of the project server**
>
> The project server has to be manually restarted after the occurrence of an error.
>
> An automatic start of the project server only occurs after the next restart of the computer on which the project server is running.
