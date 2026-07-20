---
title: "Configuring security for SCALANCE S-600"
package: HWSimNetScalSenUS
topics: 235
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring security for SCALANCE S-600

This section contains information on the following topics:

- [Supported devices](#supported-devices)
- [Hardware equipment and system functions](#hardware-equipment-and-system-functions)
- [Legal notice](#legal-notice)
- [Useful information](#useful-information)
- [Special features of user management for security functions](#special-features-of-user-management-for-security-functions)
- [Special features when downloading security configurations (SC-600)](#special-features-when-downloading-security-configurations-sc-600)
- [Certificates for security functions](#certificates-for-security-functions)
- [Editing properties and parameters](#editing-properties-and-parameters)
- [Showing information](#showing-information)
- [Configuring system functions](#configuring-system-functions)
- [Configuring interfaces](#configuring-interfaces)
- [Configuring layer 2 functions](#configuring-layer-2-functions)
- [Configuring layer 3 functions for IPv4](#configuring-layer-3-functions-for-ipv4)
- [Configuring layer 3 functions for IPv6](#configuring-layer-3-functions-for-ipv6)
- [Configuring security functions](#configuring-security-functions)

## Supported devices

### Supported devices

The security functions described in this help section are supported y the following products:

- SCALANCE S615 7.1
- SCALANCE SC-600:

  - SCALANCE SC622-2C V2.1
  - SCALANCE SC632-2C V2.1
  - SCALANCE SC636-2C V2.1
  - SCALANCE SC642-2C V2.1
  - SCALANCE SC646-2C V2.1

### General terminology "device"

In this section of the information system the term "device" is used instead of the product names listed above. You will finf the functional differences in the section [Hardware equipment and system functions](#hardware-equipment-and-system-functions) Depending on the selected device, different parameters are available on the individual configuration pages.

## Hardware equipment and system functions

### Availability of hardware

The following table shows the hardware of the devices.

We reserve the right to make technical changes.

|  | SCALANCE S615 | SCALANCE SC622-2C  SCALANCE SC632-2C  SCALANCE SC642-2C | SCALANCE SC636-2C  SCALANCE SC646-2C |
| --- | --- | --- | --- |
| Total usable ports | 5 RJ-45 ports | 2 RJ-45 ports | 6 RJ-45 ports |
| SFP transceiver slots | - | 2 | 2 |
| Electrical connectors | 5 | 2 | 6 |
| Combo ports | - | 2 | 2 |
| PLUG slot | 1 | 1 | 1 |

### Availability of the system functions

The following table shows the availability of the system functions on the devices.

We reserve the right to make technical changes.

|  |  | SCALANCE  S615 | SCALANCE SC-600 |
| --- | --- | --- | --- |
| **Information** | Versions | ✓ | ✓ |
| I&M | ✓ | - |  |
| ARP Table | ✓ | ✓ |  |
| Log tables | ✓ | ✓ |  |
| Error | ✓ | ✓ |  |
| SNMP | ✓ | ✓ |  |
| LLDP | ✓ | ✓ |  |
| Routing table | ✓ | ✓ |  |
| IPsec VPN | ✓ | ✓ (only SCALANCE SC64x-2C) |  |
| SINEMA RC | ✓ (only with KEY-PLUG) | ✓ |  |
| OpenVPN Client | ✓ | - |  |
| Redundancy | ✓ | - |  |
| VRRPv3 statistics | ✓ | ✓ (under "Redundancy") |  |
| Security | ✓ | ✓ |  |
| **System** | Configuration | ✓ | ✓ (no Telnet server, no SMTP client) |
| General | ✓ | ✓ |  |
| DNS | ✓ | ✓ |  |
| TFTP | ✓ | ✓ |  |
| SFTP | ✓ | ✓ |  |
| Events | ✓ | ✓ |  |
| SMTP client | ✓ | ✓ |  |
| PLUG | ✓ | - |  |
| DHCP client | ✓ | ✓ (only IPv4) |  |
| DHCP server | ✓ | ✓ |  |
| SNMP | ✓ | ✓ |  |
| System time | ✓ | ✓ |  |
| Auto logout | ✓ | ✓ |  |
| Button | ✓ (no fault mask) | ✓ |  |
| Syslog client | ✓ | ✓ |  |
| Ports | ✓ (under "Interfaces") | ✓ |  |
| Fault Monitoring | ✓ (only Link Change) | ✓ |  |
| Port diagnostics (only available online) | - | ✓ |  |
| cRSP / SRS | ✓ | ✓ |  |
| DCP Discovery | ✓ | - |  |
| Cloud Connector | ✓ | - |  |
| Configuration Backup | ✓ | - |  |
| Proxy Server | ✓ | ✓ |  |
| SINEMA RC | ✓ (only with KEY-PLUG) | ✓ |  |
| TCP Event | ✓ | - |  |
| Connection Check | ✓ | - |  |
| **Interfaces** | Ethernet | ✓ | - |
| PPP | ✓ | - |  |
| **Layer 2** | Port Based VLAN | ✓ | ✓ |
| Dynamic MAC aging | ✓ | ✓ |  |
| Ring redundancy | - | ✓ |  |
| LLDP | ✓ | ✓ |  |
| Spanning Tree | ✓ | ✓ |  |
| Unicast/Multicast | - | ✓ |  |
| Inter-VLAN Bridge | - | ✓ |  |
| **Layer 3 (IPv4)** | Static routes | ✓ | ✓ |
| Subnets | ✓ | ✓ |  |
| NAT | ✓ | ✓ |  |
| VRRPv3 | ✓ | ✓ |  |
| **Layer 3 (IPv6)** | Subnets | ✓ | - |
| **Security** | User | ✓ (only in the WBM) | ✓ |
| AAA (Authentication, Authorization, Accounting) | ✓ | - |  |
| Certificates | ✓ | ✓ |  |
| Firewall | ✓ | ✓ |  |
| IPsec VPN | ✓ | ✓ |  |
| OpenVPN | ✓ | ✓ |  |

## Legal notice

### Qualified personnel

The product/system belonging to this documentation may only be handled by qualified personnel for the intended purpose taking into account the documentation relating to the intended purpose and, in particular, the safety and warning notices it contains. Due to training and experience, **qualified personnel** is capable of recognizing risks and avoiding possible dangers when handling these products/systems.

## Useful information

This section contains information on the following topics:

- [Structure of an IPv4 address](#structure-of-an-ipv4-address)
- [ICMP](#icmp)
- [VLAN](#vlan)
- [SNMP](#snmp)
- [Security functions](#security-functions)

### Structure of an IPv4 address

The IPv4 address consists of 4 decimal numbers separated by a dot. Each decimal number can have a value from 0 to 255.

Example: 192.168.16.2

The IPv4 address is composed of:

- Address of the (sub)network
- The address of the node (generally also called end node, host or network node)

#### Subnet mask

The subnet mask consists of four decimal numbers with the range from 0 to 255, each number separated by a period; example: 255.255.0.0

The binary representation of the 4 subnet mask decimal numbers must contain a series of consecutive 1s from the left and a series of consecutive 0s from the right.

The "1" values determine the network address within the IPv4 address. The "0" values determine the device address within the IPv4 address.

Example:

Correct values

255.255.0.0 D =     1111 1111.1111 1111.0000 0000.0000 0000 B

255.255.128.0 D = 1111 1111.1111 1111.1000 0000.0000 0000 B

255.254.0.0 D =     1111 1111.1111 1110.0000 0000.0000.0000 B

Incorrect value:

255.255.1.0 D =     1111 1111.1111 1111.0000 0001.0000 0000 B

Subnet mask: 255.255.0.0 = 11111111.11111111.00000000.00000000

In the example for the IP address mentioned above, the subnet mask shown here has the following meaning:

The first 2 bytes of the IP address determine the subnet - i.e. 192.168. The last two bytes address the device, i.e. 16.2.

The following applies in general:

- The network address results from the AND combination of IPv4 address and subnet mask.
- The device address results from the AND-NOT combination of IPv4 address and subnet mask.

#### Classless Inter-Domain Routing (CIDR)

CIDR is a method that groups several IPv4 addresses into an address range by representing an IPv4 address combined with its subnet mask. To do this, a suffix is appended to the IPv4 address that specifies the number of bits of the network mask set to 1. Using the CIDR notation, routing tables can be reduced in size and the available address ranges put to better use.

**Example:**

IPv4 address 192.168.0.0 with subnet mask 255.255.255.0

The network part of the address covers 3 x 8 bits in binary representation; in other words 24 bits.

This results in the CIDR notation 192.168.0.0/24.  
The host part covers 1 x 8 bits in binary notation. This results in an address range of 2 to the power 8, in other words 256 possible addresses.

#### Masking additional subnets

Using the subnet mask, you can further structure a subnet assigned to one of the address classes A, B or C and form "private" subnets by setting further lower-level digits of the subnet mask to "1". For each bit set to "1", the number of "private" networks doubles and the number of nodes contained in them is halved. Externally, the network still looks like a single network.

Example:

You change the default subnet mask for a subnet of address class B (e.g. IP address 129.80.xxx.xxx) as follows:

| Masks | Decimal | Binary |
| --- | --- | --- |
| Default subnet mask | 255.255.0.0 | 11111111.11111111.00000000.00000000 |
| Subnet mask | 255.255.128.0 | 11111111.11111111.10000000.00000000 |

Result:

All devices with addresses from 129.80.001.xxx to 129.80.127.xxx are on one IP subnet, all devices with addresses from 129.80.128.xxx to 129.80.255.xxx are on another IP subnet.

#### Network gateway (router)

The task of the network gateways (routers) is to connect the IP subnets. If an IP datagram is to be sent to another network, it must first be sent to a router. For make this possible, you need to enter the router address for each member of the IP subnet.

The IP address of a device in the subnet and the IP address of the network gateway (router) may only be different at the points where the subnet mask is set to "0".

### ICMP

The acronym ICMP stands for Internet Control Message Protocol (RFC792) and is used to exchange error and information messages.

- Error message

  Informs the sender of the IP frame that when forwarding the frame an error or a parameter problem occurred.
- Information message

  Can contain information about the time measurement, the address mask, the reachability of the destination or for finding the router.

#### Structure of the ICMP data packet

| 0 | 4 | 8 | 12 | 16 | 20 | 24 | 28 | 31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ICMP packet type  Type of message |  | Code  Further details of the message |  | Checksum |  |  |  |  |
| Data (optional) |  |  |  |  |  |  |  |  |

- **ICMP packet type**

  The most important ICMP packet types are as follows:

  - Redirect

    The router informs the host in one of its subnets that there is a better route to the destination. This ICMP packet type is dealt with in more detail in the following description.
  - Destination Unreachable

    IP frame cannot be delivered.
  - Time Exceeded

    Time limit exceeded
  - Echo-Request

    Echo request, better known as ping.
- **Code**

  The code describes the ICMP packet type in greater detail. The selection depends on the selected ICMP packet type. With "Destination Unreachable,", for example "Code 1" host cannot be reached.

You will find a full list of the ICMP packet types and codes on the website of [IANA](http://www.iana.org/assignments/icmp-parameters).

#### ICMP packet type 5 - Redirect

Host A wants to send an IP frame to host C. Host C is not located in the same subnet as host A. For this reason host A sends the IP frame to its default gateway. The default gateway of host A is interface 1 of router A. Router A cannot forward the IP frame because it does not know the destination network. Via its routing table, however, router A knows that subnet C is reachable via router B. Router B connects subnet A with subnet C. Router A sends a redirect message to host A. In this, router A instructs host A in future to send IP frames to host C via router B whose IP address is contained in the redirect message. The initial IP frame is sent by router A directly to router B that forwards it to Host C.

![ICMP packet type 5 - Redirect](images/126345527691_DV_resource.Stream@PNG-en-US.png)

**Conditions for sending redirect messages**

- The IP frame is received and sent via the same interface of router A.
- The source IP address (host A) is from the same subnet as the next hop address (router B) in the routing table.
- The IP frame is not affected by a source NAT rule (masquerading, source NAT or NETMAP).
- So that router A forwards the initial IP frame to router B, a firewall rule vlanX → vlanX is required.

### VLAN

This section contains information on the following topics:

- [VLAN](#vlan-1)
- [VLAN tagging](#vlan-tagging)

#### VLAN

##### Network definition regardless of the spatial location of the nodes

VLAN (Virtuelles Local Area Network) divides a physical network into several logical networks that are shielded from each other. Here, devices are grouped together to form logical groups. Only nodes of the same VLAN can address each other. Since multicast and broadcast frames are only forwarded within the particular VLAN, they are also known as broadcast domains.

The particular advantage of VLANs is the reduced network load for the nodes and network segments of other VLANs.

To identify which packet belongs to which VLAN, the frame is expanded by 4 bytes, refer to [VLAN tagging](#vlan-tagging). Apart from the VLAN ID, this expansion also includes priority information.

##### Options for the VLAN assignment

There are various options for the assignment to VLANs:

- Port-based VLAN

  Each port of a device is assigned a VLAN ID. You configure port-based VLAN in "[Layer 2 > VLAN > Port-based VLAN](#port-based-vlan)".
- Protocol-based VLAN  
  Each port of a device is assigned a protocol group.
- Subnet-based VLAN  
  The IP address of the device is assigned a VLAN ID.

#### VLAN tagging

##### Expansion of the Ethernet frames by four bytes

For CoS (Class of Service, frame prioritization) and VLAN (virtual network), the IEEE 802.1Q standard defined the expansion of Ethernet frames by adding the VLAN tag.

> **Note**
>
> The VLAN tag increases the permitted total length of the frame from 1518 to 1522 bytes.  
> The end nodes on the networks must be checked to find out whether they can process this length / this frame type. If this is not the case, only frames of the standard length may be sent to these nodes.

The additional 4 bytes are located in the header of the Ethernet frame between the source address and the Ethernet type / length field:

The additional bytes contain the Tag Protocol Identifier (TPID) and the Tag Control Information (TCI).

![Expansion of the Ethernet frames by four bytes](images/126334567179_DV_resource.Stream@PNG-en-US.png)

##### Tag Protocol Identifier (TPID)

The first 2 bytes form the Tag Protocol Identifier (TPID) and always have the value 0x8100. This value specifies that the data packet contains VLAN information or priority information.

##### Tag Control Information (TCI)

The 2 bytes of the Tag Control Information (TCI) contain the following information:

**CoS**
 **prioritization**

The tagged frame has 3 bits for the priority that is also known as Class of Service (CoS), see also IEEE 802.1Q.

| CoS bits | Priority | Type of the data traffic |
| --- | --- | --- |
| 000 | 0 (lowest) | Background |
| 001 | 1 | Best Effort |
| 010 | 2 | Excellent Effort |
| 011 | 3 | Critical Applications |
| 100 | 4 | Video, < 100 ms delay (latency and jitter) |
| 101 | 5 | Voice (language), < 10 ms delay (latency and jitter) |
| 110 | 6 | Internetwork Control |
| 111 | 7 (highest) | Network Control |

The prioritization of the data packets is possible only if there is a queue in the components in which they can buffer data packets with lower priority.

The device has multiple parallel queues in which the frames with different priorities can be processed. As default, first, the frames with the highest priority are processed. This method ensures that the frames with the highest priority are sent even if there is heavy data traffic.

**Canonical Format Identifier**
 **(**
**CFI**
**)**

The CFI is required for compatibility between Ethernet and the token Ring.  
The values have the following meaning:

| Value | Meaning |
| --- | --- |
| 0 | The format of the MAC address is canonical. In the canonical representation of the MAC address, the least significant bit is transferred first. Standard-setting for Ethernet switches. |
| 1 | The format of the MAC address is not canonical. |

**VLAN ID**

In the 12-bit data field, up to 4096 VLAN IDs can be formed. The following conventions apply:

| VLAN ID | Meaning |
| --- | --- |
| 0 | The frame contains only priority information (priority tagged frames) and no valid VLAN identifier. |
| 1- 4094 | Valid VLAN identifier, the frame is assigned to a VLAN and can also include priority information. |
| 4095 | Reserved |

### SNMP

This section contains information on the following topics:

- [SNMP](#snmp-1)
- [SNMPv3 user migration](#snmpv3-user-migration)

#### SNMP

##### Introduction

With the aid of the Simple Network Management Protocol (SNMP), you monitor and control network components from a central station, for example routers or switches. SNMP controls the communication between the monitored devices and the monitoring station.

Tasks of SNMP:

- Monitoring of network components
- Remote control and remote parameter assignment of network components
- Error detection and error notification

In versions v1 and v2c, SNMP has no security mechanisms. Each user in the network can access data and also change parameter assignments using suitable software.

For the simple control of access rights without security aspects, community strings are used.

The community string is transferred along with the query. If the community string is correct, the SNMP agent responds and sends the requested data. If the community string is not correct, the SNMP agent discards the query. Define different community strings for read and write permissions. The community strings are transferred in plain text.

Standard values of the community strings:

- public

  Has only read permissions
- private

  Has read and write permissions

  > **Note**
  >
  > Because the SNMP community strings are used for access protection, do not use the standard values "public" or "private". Change these values following the initial commissioning.

Further simple protection mechanisms at the device level:

- Allowed Host

  The IP addresses of the monitoring systems are known to the monitored system.
- Read Only

  If you assign "Read Only" to a monitored device, monitoring stations can only read out data but cannot modify it.

SNMP data packets are not encrypted and can easily be read by others.

The central station is also known as the management station. An SNMP agent is installed on the devices to be monitored with which the management station exchanges data.

The management station sends data packets of the following type:

- GET

  Requests a data record from the SNMP agent
- GETNEXT

  Calls up the next data record.
- GETBULK (available as of SNMPv2c)

  Requests multiple data records at once, for example several rows of a table.
- SET

  Contains parameter assignment data for the relevant device.

The SNMP agent sends data packets of the following type:

- RESPONSE

  The SNMP agent returns the data requested by the manager.
- TRAP

  If a certain event occurs, the SNMP agent itself sends traps.
- INFORM

  Like a trap except that it is acknowledged by the receiver.

SNMPv1/v2c/v3 use UDP (User Datagram Protocol) and use the UDP ports 161 and 162. The data is described in a Management Information Base (MIB).

##### SNMPv3

Compared with the previous versions SNMPv1 and SNMPv2c, SNMPv3 introduces an extensive security concept.

SNMPv3 supports:

- Fully encrypted user authentication
- Encryption of the entire data traffic
- Access control of the MIB objects at the user/group level

#### SNMPv3 user migration

With the introduction of SNMPv3, you can no longer transfer user configurations to other devices without taking special action, e.g. loading a configuration file.

According to the standard, the SNMPv3 protocol uses a unique SNMP engine ID as an internal identifier for an SNMP agent. This ID must be unique in the network. It is used to authenticate access data of SNMPv3 users and to encrypt it.

Depending on whether you have enabled or disabled the "SNMPv3 User Migration" function, the SNMP engine ID is generated differently.

**Restriction when using the function**

Use the "SNMPv3 User Migration" function only to transfer configured SNMPv3 users to a substitute device when replacing a device.  
Do not use the function to transfer configured SNMPv3 users to multiple devices. If you load a configuration with created SNMPv3 users on several devices, these devices use the same SNMP engine ID. If you use these devices in the same network, your configuration contradicts the SNMP standard.

**Compatibility with predecessor products**

You can only transfer SNMPv3 users to a different device if you have created the users as migratable users. To create a migratable user the "SNMPv3 User Migration" function must be activated when you create the user.

### Security functions

This section contains information on the following topics:

- [User management (WBM or CLI)](#user-management-wbm-or-cli)
- [Firewall](#firewall)
- [NAT](#nat)
- [NAT and firewall](#nat-and-firewall)
- [Certificates](#certificates)
- [VPN](#vpn)

#### User management (WBM or CLI)

##### Overview of user management

Access to the device is managed by configurable user settings. Set up users with a password for authentication. Assign a role with suitable rights to the users.

The authentication of users can either be performed locally by the device or by an external RADIUS server. You configure how the authentication is handled on the "Security > AAA > General" page.

##### Local logon

The local logging on of users by the device runs as follows:

1. The user logs on with user name and password on the device.
2. The device checks whether an entry exists for the user.

   → If an entry exists, the user is logged in with the rights of the associated role.

   → If no corresponding entry exists, the user is denied access.

##### Login via an external RADIUS server

RADIUS (Remote Authentication Dial-In User Service) is a protocol for authenticating and authorizing users by servers on which user data can be stored centrally.

Depending on the RADIUS authorization mode you have selected on the "Security > AAA > RADIUS Client" page, the device evaluates different information of the RADIUS server.

**RADIUS authorization mode "Standard"**

If you have set the authorization mode "conventional", the authentication of users via a RADIUS server runs as follows:

1. The user logs on with user name and password on the device.
2. The device sends an authentication request with the login data to the RADIUS server.
3. The RADIUS server runs a check and signals the result back to the device.

   - The RADIUS server reports a successful authentication and returns the value "Administrative User" to the device for the attribute "Service Type".

     → The user is logged in with administrator rights.
   - The RADIUS server reports a successful authentication and returns a different or even no value to the device for the attribute "Service Type".

     → The user is logged in with read rights.
   - The RADIUS server reports a failed authentication to the device:

     → The user is denied access.

**RADIUS authorization mode "SiemensVSA"**

**Requirement**

For the RADIUS authorization mode "Siemens VSA" the following needs to be set on the RADIUS server:

- Manufacturer code: 4196
- Attribute number: 1
- Attribute format: Character string (group name)

**Procedure**

If you have set the authorization mode "SiemensVSA", the authentication of users via a RADIUS server runs as follows:

1. The user logs on with user name and password on the device.
2. The device sends an authentication request with the login data to the RADIUS server.
3. The RADIUS server runs a check and signals the result back to the device.

   **Case A**: The RADIUS server reports a successful authentication and returns the group assigned to the user to the device.

   - The group is known on the device and the user is not entered in the table "External User Accounts"

     → The user is logged in with the rights of the assigned group.
   - The group is known on the device and the user is entered in the table "External User Accounts"

     → The user is assigned the role with the higher rights and logged in with these rights.
   - The group is not known on the device and the user is entered in the table "External User Accounts"

     → The user is logged in with the rights of the role linked to the user account.
   - The group is not known on the device and the user is not entered in the table "External User Accounts"

     → The user is logged in with the rights of the role "Default".

   **Case B:** The RADIUS server reports a successful authentication but does not return a group to the device.

   - The user is entered in the table "External User Accounts":

     → The user is logged in with the rights of the linked role.
   - The user is not entered in the table "External User Accounts":

     → The user is logged in with the rights of the role "Default".

   **Case C:** The RADIUS server reports a failed authentication to the device:

   - The user is denied access.

#### Firewall

This section contains information on the following topics:

- [Firewall](#firewall-1)
- [Firewall rules](#firewall-rules)

##### Firewall

The security functions of the device include a stateful inspection firewall. This is a method of packet filtering or packet checking.

The IP packets are checked based on firewall rules in which the following is specified:

- The permitted protocols
- IP addresses and ports of the permitted sources
- IP addresses and ports of the permitted destinations

If an IP packet fits the specified parameters, it is allowed to pass through the firewall. The rules also specify what is done with IP packets that are not allowed to pass through the firewall.

Simple packet filter techniques require two firewall rules per connection.

- One rule for the query direction from the source to the destination.
- A second rule for the response direction from the destination to the source

###### Stateful Inspection Firewall

You only need to specify one firewall rule for the query direction from the source to the destination. The second rule is added implicitly. The packet filter recognizes when, for example, computer "A" is communicating with computer "B" and only then does it allow replies. A query by computer "B" is therefore not possible without a prior request by computer "A".

You configure the firewall in "[Security > Firewall](#firewall-2)".

> **Note**
>
> **IP packets via layer 2 (within the same VLAN)**
>
> If the IP packets from the device are sent via a switch port (layer 2), these IP packets are not checked based on firewall rules. The firewall has no effect on packets forwarded at the layer 2 level.

###### Communication directions

| from | to | Meaning |
| --- | --- | --- |
| vlan x | vlan x | Access from IP subnet vlan x to IP subnet vlan x.  Example:   vlan1 (INT) → vlan2 (EXT)  Access from the local IP subnet to the external IP subnet. |
| ppp2 | Access from the IP subnet to the WAN interface of the device. |  |
| Device | Access from the IP subnet to the device. |  |
| SINEMA RC | Access from the IP subnet to the SINEMA RC connection. |  |
| IPsec (all)   IPsec <Connection Name>  OpenVPN (all)  OpenVPN <Connection Name> | Access from the IP subnet to the VPN tunnel partners that can be reached via all VPN connections (all) or via a certain VPN connection <Connection Name>. |  |
| Device | vlan x | Access from the device to the IP subnet. |
| ppp2 | Access from the device to the WAN interface of the device. |  |
| SINEMA RC | Access from the device to the SINEMA RC connection. |  |
| IPsec (all)   IPsec <Connection Name>  OpenVPN (all)   OpenVPN <Connection Name> | Access from the device to the tunnel partners that can be reached via all VPN connections (all) or via a certain VPN connection (<Connection Name>). |  |
| SINEMA RC | vlan x | Access from SINEMA RC connections to the IP subnet. |
| ppp2 | Access from the IP subnet to the WAN interface of the device. |  |
| Device | Access from SINEMA RC connections to the device. |  |
| IPsec (all)   IPsec <Connection Name>  OpenVPN (all)   OpenVPN <Connection Name> | Access from the SINEMA RC server to the VPN tunnel partners that can be reached via all VPN connections (all) or via a certain VPN connection <Connection Name>. |  |
| IPsec (all)   IPsec <Connection Name>  OpenVPN (all)   OpenVPN <Connection Name> | vlan x | Access via VPN tunnel partners to the IP subnet. |
| ppp2 | Access from the IP subnet to the WAN interface of the device. |  |
| Device | Access via VPN tunnel partners to the device. |  |
| SINEMA RC | Access via VPN tunnel partners to the SINEMA RC connection. |  |
| ppp0/usb | vlan x | Access from the mobile wireless interface to the IP subnet. |
| Device | Access from the mobile wireless interface to the device. |  |
| SINEMA RC | Access from the mobile wireless interface to the SINEMA RC connection. |  |
| IPsec (all)   IPsec <Connection Name>  OpenVPN (all)  OpenVPN <Connection Name> | Access from the mobile wireless interface to the VPN tunnel partners that can be reached via all VPN connections (all) or via a certain VPN connection <Connection Name>. |  |

##### Firewall rules

Firewall rules are automatically created, predefined or specially configured IP rules for data traffic.

###### Automatically created firewall rules

The "Auto firewall rules" setting is available for the following functions:

- System > [SINEMA RC](#sinema-rc-1)
- Security > IPsec VPN> [Phase 2](#phase-2)
- Security > OpenVPN Client > [Connections](#connections-1)

The automatically created firewall rules allow packets in the following direction:

| From | To | SINEMA RC | IPsec VPN | OpenVPN |
| --- | --- | --- | --- | --- |
| Internal | External | ✓ | ✓ | ✓ |
| External | Internal | ✓ | ✓ | ✓ |
| Device | External | -- | -- | ✓ |
| External | Device | Predefined IPv4 rules  When the connection is created, the following IPv4 services are enabled: |  |  |
| HTTP  HTTPS  SSH   Ping | Ping | Ping |  |  |

###### Predefined firewall rules

The firewall contains predefined IPv4 rules that enable specific IPv4 services on the device.

Specify the interface via which access takes place under "Security > Firewall > [Predefined IPv4](#predefined-ip-rules)".

The following options are available:

- VLANx: VLANs with configured subnet
- WAN interface of the device: pppx, usb0
- VPN connection: SINEMA RC, IPsec and OpenVPN

**Factory setting**

The firewall is enabled by default. In the delivery state (factory setting), the configuration of the predefined IPv4 rules is as follows:

| Service | Access |  |
| --- | --- | --- |
| Local access (vlan1) to the device | External access (vlan2) to the device |  |
| Cloud Connector | ✓ | - |
| DHCP | ✓ | ✓ |
| DNS | ✓ | -- |
| HTTP | ✓ | -- |
| HTTPS | ✓ | -- |
| IPsec VPN | -- | ✓ |
| Ping | ✓ | -- |
| SMS relay (only with M87x) | ✓ | -- |
| SNMP | ✓ | -- |
| SSH | ✓ | -- |
| System Time | -- | -- |
| Telnet | ✓ | -- |
| VRRP | -- | -- |

#### NAT

NAT (Network Address Translation) is a method of translating IP addresses in data packets. With this, two different networks (internal and external) can be connected together.

A distinction is made between source NAT in which the source IP address is translated and destination NAT in which the destination IP address is translated.

You will find information on NAT scenarios that are implemented with the device at the following [address:](https://support.industry.siemens.com/cs/gb/en/view/109744660)

##### IP masquerading

IP masquerading is a simplified source NAT. With each outgoing data packet sent via this interface, the source IP address is replaced by the IP address of the interface. The adapted data packet is sent to the destination IP address. For the destination host it appears as if the queries always came from the same sender. The internal nodes cannot be reached directly from the external network. By using NAPT, the services of the internal nodes can be made reachable via the external IP address of the device.

IP masquerading can be used if the internal IP addresses cannot or should not be forwarded externally, for example because the internal network structure should remain hidden.

You configure masquerading in "Layer 3" > "NAT" > "IP Masquerading".

##### NAPT

NAPT (Network Address and Port Translation) is a form of destination NAT and is often called port forwarding. This allows the services of the internal nodes to be reached from external that are hidden by IP masquerading or source NAT.

Incoming data packets are translated that come from the external network and are intended for an external IP address of the device (destination IP address). The destination IP address is replaced by the IP address of the internal node. In addition to address translation, port translation is also possible.

The options are available for port translation:

| from | to | Response |
| --- | --- | --- |
| a single port | the same port | If the ports are the same, the frames will be forwarded without port translation. |
| a single port | a single port | The frames are translated to the port. |
| a port range | a single port | The frames from the port range are translated to the same port (n:1). |
| a port range | the same port range | If the port ranges are the same, the frames will be forwarded without port translation. |
| a port range | another port range | The frames are translated to any free port from the target range.   With individual connection, they are normally translated to the first port in the target range.   If there are connections at the same time, the round robin method is used to translate to a free port in the target range. |
| a single port | a port range | The frames are translated to any free port from the target range. With individual connection, they are normally translated to the first port in the target range. If there are connections at the same time, the round robin method is used to translate to a free port in the target range. |

Port forwarding can be used to allow external nodes access to certain services of the internal network e.g. FTP, HTTP.

You configure NAPT in "Layer 3" > "NAT" > "NAPT".

##### Source NAT

As with masquerading, in source NAT the source address is translated. In addition to this, the outgoing data packets can be restricted. These include limitation to certain IP addresses or IP address ranges and limitation to certain interfaces.

Source NAT can be used if the internal IP addresses cannot or should not be forwarded externally, for example because a private address range such as 192.168.x.x is used.

You configure source NAT in "Layer 3" > "NAT" > "Source NAT".

##### NETMAP

With NETMAP it is possible to translate complex subnets to a different subnet. In this translation, the subnet part of the IP address is changed and the host part remains. For translation with NETMAP only one rule is required. NETMAP can translate both the source IP address and the destination IP address. To perform the translation with destination NAT and source NAT, numerous rules would be necessary. NETMAP can also be applied to VPN connections.

You configure NETMAP in "Layer 3" > "NAT" > "NETMAP".

#### NAT and firewall

The firewall and NAT router support the "Stateful Inspection" mechanism. If the IP data traffic from internal to external is enabled, internal notes can initiate a communications connection into the external network.

The reply frames from the external network can pass through the NAT router and firewall without it being necessary for their addresses to be included extra in the firewall rule and the NAT address translation. Frames that are not a reply to a query from the internal network are discarded without a matching firewall rule.

##### NAT translation and firewall rules

You will find an example of NAT translations on the Internet pages of Siemens Industry Online Support.

[Link:](https://support.industry.siemens.com/cs/ww/en/view/109744660)

#### Certificates

##### Certificate types

The device uses different certificates to authenticate the various nodes.

| Certificate |  | Is used in... |
| --- | --- | --- |
| CA certificate | The CA certificate is a certificate issued by a Certificate Authority from which the server, device and partner certificates are derived. To allow a certificate to be derived, the CA certificate has a private key signed by the certificate authority.  The key exchange between the device and the VPN gateway of the partner takes place automatically when establishing the connection. No manual exchange of key files is necessary. | [IPsec VPN](#ipsec-vpn-2) |
| Server certificate | Server certificates are required to establish secure communication (e.g. HTTPS, VPN...) between the device and another network participant. The server certificate is an encrypted SSL certificate. The server certificate is derived from the oldest valid CA, even if this is "out of service". The crucial thing is the validity date of the CA. | [SINEMA RC](#sinema-rc-1) |
| Device certificate | Certificates with the private key (key file) with which the device identifies itself. | [IPsec VPN](#ipsec-vpn-2) |
| Partner certificate | Certificates with which the VPN gateway of the partner identifies itself with the device. | [IPsec VPN](#ipsec-vpn-2) |

##### File types

| File type | Description |
| --- | --- |
| *.crt | File that contains the certificate. |
| *.p12 | In the PKCS12 certificate file, the private key is stored with the corresponding certificate and is password protected.  The CA creates a certificate file (PKCS12) for both ends of a VPN connection with the file extension ".p12". This certificate file contains the public and private key of the local station, the signed certificate of the CA and the public key of the CA. |
| *.pem | Certificate and key as Base64-coded ASCII text. |

#### VPN

This section contains information on the following topics:

- [Overview](#overview)
- [IPsec VPN](#ipsec-vpn)
- [OpenVPN](#openvpn)
- [VPN connection establishment](#vpn-connection-establishment)

##### Overview

The device supports the following VPN systems

- IPsec VPN (only for SCALANCE S615 and SCALANCE SC64x-2C)
- OpenVPN (only for SCALANCE S615)

##### IPsec VPN

You configure the IPsec connections in "Security" > " [IPsec VPN](#ipsec-vpn-2)".

With IPsec VPN, the frames are transferred in tunnel mode. To allow the device to establish a VPN tunnel, the remote network must have a VPN gateway as the partner.

For the VPN connections, the device distinguishes two modes:

- **Roadwarrior mode**

  In this mode either the address of the partner is fixed or an IP range is entered from which the connections are taken. The device learns the reachable remote subnets from the partner.
- **Standard mode**

  In this mode the address of the partner or the remote subnet is entered permanently. The device can either establish the connection actively as a VPN client or wait passively for connection establishment by the partner.

###### The IPsec method

The device uses the IPsec method in the tunnel mode for the VPN tunnel. Here, the frames to be transferred are completely encrypted and provided with a new header before they are sent to the VPN gateway of the partner. The frames received by the partner are decrypted and forwarded to the recipient.

To provide security, the IPsec protocol suite uses various protocols:

- The IP Authentication Header (**AH**) handles the authentication and identification of the source.
- The Encapsulation Security Payload (**ESP**) encrypts the data.
- The Security Association (**SA**) contains the specifications negotiated between the partners, e.g. about the lifetime of the key, the encryption algorithm, the period for new authentication etc.
- Internet Key Exchange (**IKE**) is a key exchange method. The key exchange takes place in two phases:

  - Phase 1

    In this phase, no security services such as encryption, authentication and integrity checks are available yet since the required keys and the IPsec SA still need to be created. Phase 1 serves to establish a secure VPN tunnel for phase 2. To achieve this, the communications partners negotiate an ISAKMP Security Association (ISAKMP SA) that defines the required security services (algorithms, authentication methods used). The subsequent messages and phase 2 are therefore secure.
  - Phase 2

    Phase 2 serves to negotiate the required IPsec SA. Similar to phase 1, exchanging offers achieves agreement about the authentication methods, the algorithms and the encryption method to protect the IP packets with IPsec AH and IPsec ESP.

    The exchange of messages is protected by the ISAKMP SA negotiated in phase 1. Due to the ISAKMP SA negotiated in phase 1, the identity of the nodes is known and the method for the integrity check already exists.

###### Authentication method

- CA certificate, device and partner certificate (digital signatures)

  The use of certificates is an asymmetrical cryptographic system in which every node (device) has a pair of keys. Each node has a secret, private key and a public key of the partner. The private key allows the device to authenticate itself and to generate digital signatures.
- Pre-shared key

  The use of a pre-shared key is a symmetrical cryptographic system. Each node has only one secret key for decryption and encryption of data packets. The authentication is via a common password.

###### Local ID and remote ID

The local ID and the remote ID are used by IPsec to uniquely identify the partners (VPN end point) during establishment of a VPN connection.

###### Encryption methods

The following encryption methods are supported. The selection depends on the phase and the key exchange method (IKE):

|  | Phase 1 |  | Phase 2 |  |
| --- | --- | --- | --- | --- |
| IKEv1 | IKEv2 | IKEv1 | IKEv2 |  |
| 3DES | x | x | x | x |
| AES128 CBC | x | x | x | x |
| AES192 CBC | x | x | x | x |
| AES256 CBC | x | x | x | x |
| AES128 CTR | - | x | x | x |
| AES192 CTR | - | x | x | x |
| AES256 CTR | - | x | x | x |
| AES128 CCM 16 | - | x | x | x |
| AES192 CCM 16 | - | x | x | x |
| AES256 CCM 16 | - | x | x | x |
| AES128 GCM 16 | - | x | x | x |
| AES192 GCM 16 | - | x | x | x |
| AES256 GCM 16 | - | x | x | x |
| x: is supported  -: is not supported |  |  |  |  |

###### Default Ciphers

During connection establishment a preset list can be transferred to the VPN connection partners. The list contains combinations of the three algorithms (Encryption, Authentication, Key Derivation). To establish a VPN connection, the VPN connection partner must support at least one of these combinations. The combinations depend on the phase and the key exchange method (IKE).

| Combination |  |  | Phase 1 |  | Phase 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
| Encryption | Authentication | Key derivation | IKEv1 | IKEv2 | IKEv1 | IKEv2 |
| AES128 | SHA1 | DH Group 14 | x | x | x | x |
| AES256 | SHA512 | DH Group 16 | x | x | x | x |
| AES128 CCM 16 | SHA256 | DH Group 14 | - | x | x | x |
| AES256 CCM 16 | SHA512 | DH Group 16 | - | x | x | x |
| AES128 | SHA1 | none | - | - | x | x |
| AES256 | SHA512 | none | - | - | x | x |
| AES128 CCM 16 | SHA256 | none | - | - | x | x |
| AES256 CCM 16 | SHA512 | none | - | - | x | x |
| x: Combination is part of the default cipher  -: Combination is not part of the default cipher  none: For phase 2, no separate keys are exchanged. This means that Perfect Forward Secrecy (PFS) is disabled. |  |  |  |  |  |  |

###### Requirements of the VPN partner

The VPN partner must support IPsec with the following configuration to be able to establish an IPsec connection successfully:

- Authentication with partner certificate, CA certificates or pre-shared key
- IKEv1 or IKEv2
- Support of at least one of the following DH groups: Diffie-Hellman group 1, 2, 5 and 14 - 18
- 3DES or AES encryption
- MD5, SHA1, SHA256, SHA384 or SHA512
- Tunnel mode

If the VPN partner is downstream from a NAT router, the partner must support NAT-T. Or, the NAT router must know the IPsec protocol (IPsec/VPN passthrough).

###### NAT traversal (NAT-T)

There may be a NAT router between the device and the VPN gateway of the remote network. Not all NAT routers allow IPsec frames to pass through. This means that it may be necessary to encapsulate the IPsec frames in UDP packets to be able to pass through the NAT router.

###### Dead peer detection

This is only possible when the VPN partner supports DPD. DPD checks whether the connection is still operating problem free or whether there has been an interruption on the line. Without DPD and depending on the configuration, it may be necessary to wait until the SA lifetime has expired or the connection must be reinitiated manually. To check whether the IPsec connection is still problem-free, the device itself sends DPD queries to the VPN partner station. If the VPN partner station does not reply after a certain time has elapsed, the connection to the VPN partner station will be declared invalid. You configure the settings for DPD in phase 1.

##### OpenVPN

With OpenVPN, virtual private networks (VPN) can be established. As an OpenVPN client, the device can establish a VPN connection to a remote network.

You configure the OpenVPN client in "Security" > " [OpenVPN Client](#openvpn-2)".

The VPN connection is established via virtual device drivers, the TAP and TUN device. During this, virtual network interfaces are created that act like a physical interface of the device and represent the endpoint of the VPN tunnel.

The device supports the following:

- TUN device: Routing mode

  The LAN Interface and the virtual network interface are located in different IP subnets. The virtual tunnel interface is assigned a virtual IP address from a devised subnet by the OpenVPN server. The IP packets (layer 3) are routed between the virtual tunnel interface and the LAN interface.

###### Authentication method

- Certificates: CA certificate and device certificate

  The use of certificates is an asymmetrical cryptographic system. Each node (device) has a secret, private key and a public key of the partner. The private key allows the device to authenticate itself and to generate digital signatures.
- User name / password

  Access is restricted by a user name and a password.

###### Encryption methods

The device also supports the following methods:

- BF CBC
- AES128 CBC
- AES192 CBC
- AES256 CBC
- DES EDE3

##### VPN connection establishment

The device supports the following options for establishing a VPN connection.

- OpenVPN: Security > OpenVPN > [Connections](#connections)
- IPsec VPN: Security > IPsec VPN > [Connections](#connections-1)
- SINEMA RC: System > [SINEMA RC](#sinema-rc-1)

| Options | Use |  |  | Description |
| --- | --- | --- | --- | --- |
| OpenVPN | IPsec VPN | SINEMA RC <sup>1)</sup> |  |  |
| start | x | x | - | The device is "active", in other words, it attempts to establish a connection to a partner. The partner is addressed using its configured WAN IP address or the configured FQDN. |
| wait | - | x | - | The device is "passive", in other words, it waits for the partner to initiate the connection. |
| on demand | - | x | - | The device attempts to establish a connection to a partner when necessary. The receipt of requests for VPN connection establishment is also possible.  For the configured local and remote subnets, an entry is created in the routing table. If a node attempts to send data packets via the VPN tunnel from one of the networks, the VPN connection is established. The settable timeout has the effect that after this time without any further data packets the VPN tunnel is terminated again. |
| start on DI | x | x | x | Connection establishment is controlled via the digital input (DI). |
| Wait on DI | - | x | - |  |
| Auto | - | - | x | The device adopts the settings of the SINEMA RC server. You configure the settings on the SINEMA RC Server in "Remote Connections > Devices". You will find further information on this topic in the operating instructions "SINEMA RC Server". |
| Permanent | - | - | x | The device establishes a VPN connection to the SINEMA RC Server. The VPN tunnel is established permanently |
| <sup>1)</sup> For SCALANCE S615: KEY-PLUG SINEMA REMOTE CONNECT required |  |  |  |  |

###### Digital input (DI)

The establishment of the VPN tunnel can also be controlled via the digital input, e.g. using a button. When the button is closed, voltage is applied to the digital input and the LED of the digital input lights up. The lit LED indicates that signal 1 (TRUE / HIGH) is applied. Signal 1 triggers an event on the device with which the establishment of the VPN tunnel is controlled. You will find information on connecting and the maximum current load in the operating instructions of the devices.

![Digital input (DI)](images/85339106955_DV_resource.Stream@PNG-de-DE.png)

**Requirement**

- In "[System > Events > Configuration](#configuration-2)" for the "Digital Input" event "VPN Tunnel" is activated.

  If this setting is not activated, the event is not passed on to the VPN connection.

**Options**

The device supports the following options for controlling the VPN tunnel via the digital input:

- start on DI

  If the event "Digital Input" occurs, the device becomes "active". The device tries to establish a VPN connection to a remote station (OpenVPN, IPsec, SINEMA RC).
- Wait on DI

  If the event "Digital Input" occurs, the device becomes "passive". The device waits for the partner to initiate the connection.

###### Notification options

If the status of the digital input or a VPN tunnel (IPsec, OpenVPN, SINEMA RC) changes, the device provides several options for notification on the "[Events](#configuration-2)" page.

| Type of notification | Digital In | VPN tunnel | Behavior if there is a status change |
| --- | --- | --- | --- |
| E-mail | x | x | The device sends an e-mail. The e-mail contains the identification of the sending device, a description of the cause of the alarm in plain language, and a time stamp.  Requirement:  - An SMTP server is set up. - In "System > SMTP Client" the function is activated, a recipient and the IP address of the SMTP server are configured. |
| Trap | x | x | The device sends an SNMP trap.   Requirement:  - "SNMPv1 traps" is enabled in "System > Configuration". - In "System > Configuration > Traps" a recipient is configured to which the device sends the SNMP traps. |
| Log table | x | x | The device writes an entry in the event log table. The content of the event log table is displayed in "Information > Log Table". |
| Syslog | x | x | The device writes an entry to the Syslog server.  Requirement:  - A Syslog server has been set up. - In "System > Syslog Client" the function is activated and the IP address of the Syslog server is configured. |
| Fault LED | x | - | The fault LED lights up on the device. |
| Digital Input | x | x | Controls the digital output or signals the status change with the "DO" LED.  A consumer can be connected to the digital output. You will find information on connecting in the operating instructions of the devices. The consumer signals a status change.     ![Notification options](images/86812203275_DV_resource.Stream@PNG-de-DE.png)    **Note**   You can control the digital output directly via CLI or SNMP. In the WBM and CLI, you can configure the use of the digital output in "Events". Do not control the digital output directly when you use this in the WBM and CLI. |
| Read out the status of the MIB variable | x | - | Using the private MIB variable snMspsDigitalInputLevel, you can read out the status of the digital input.  - OID of the private MIB variable snMspsDigitalInputLevel:    `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).siemens(4329).industrialComProducts(20).iComPlatforms(1).simaticNet(1).snMsps(1).snMspsCommon(1).snMspsDigitalIO(39).snMspsDigitalIOObjects(1).snMspsDigitalInputTable(2).snMspsDigitalInputEntry(1).snMspsDigitalInputLevel(6)` - values of the MIB variable   - 1: Signal 0 at the digital input (DI)   - 2: Signal 1 at the digital input (DI) |

## Special features of user management for security functions

### Access to security functions

You can only access security functions after activating project protection and after a user has successfully logged on. The logged on user must also have the required engineering and runtime rights.

You will find basic information on user management in STEP 7 in the "Using user management" section of the information system.

### Engineering rights for security devices

These engineering rights allow diagnostics and configuration of security devices:

- View security device configuration: Display of the global security functions and the local security settings of the security devices.
- Edit security device configuration: Configuration of the global security functions and the local security settings of the security devices and perform diagnostics of the security devices.

### Roles with runtime rights for SCALANCE S 600

As default, some system-defined roles with the prefix "NET" are assigned runtime rights for SCALANCE S-600. Runtime rights provide the rights to execute certain tasks on the devices. Just as with engineering rights you cannot change runtime rights for system-defined roles. For user-defined roles you can change the runtime rights as required. You can specify the runtime rights of a user-defined role for each device.

There must be at least one user assigned a role with full runtime rights for a security module. e.g. the system-defined role "NET Administrator".

The system-defined roles with the prefix "NET" are assigned engineering rights:

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| Open the project read only | **x** | **x** | **x** |
| Open the project with write rights | **x** | **x** | - |
| Edit security settings: "Settings" and "Users and roles" | **x** | - | - |
| View security device configuration | **x** | **x** | **x** |
| Edit security device configuration | **x** | **x** | - |

### Runtime rights for SCALANCE S 600

The following runtime rights are available:

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| Download the configuration files | **x** | **x** | - |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |

## Special features when downloading security configurations (SC-600)

### Special features when downloading

The loading of project data is described in the section "Download project data to a device".

In addition, you can select the data you want to download to the device in the "Load preview" dialog:

- Complete download (with restart): All data is loaded to the device and the device is restarted.
- Firewall (without restart): The action is available if you have already performed a complete download. If selected, only the data differing to the firewall will be loaded without restarting the device. If an error occurs during loading, you must perform a complete download with restart to prevent incorrect project data from being loaded to the device.

In the "Action" column, select the desired function you want to download. If "No action" is displayed no deviating data exist.

---

**See also**

[Downloading a configuration](Configuring%20security.md#downloading-a-configuration)

## Certificates for security functions

During configuration only certificates generated by the TIA Portal can be used, for example VPN group certificates. Certificates not generated by the TIA Portal. for example CA certificates for SINEMA Remote Connect, cannot be used. You need to add such certificates later via the WBM and download them to the device. You will find more information in the relevant WBM configuration manual.

## Editing properties and parameters

### Editing options

You have the following options for editing properties and parameters:

- Hardware and network editor

  Once you have inserted the network component, you can edit the properties and parameters, for example the device name. You will find more detailed information in "Hardware and network editor".
- Web Based Management (WBM)

  The parameters and properties are accessible using the supplied HTML pages (WBM pages). Each WBM page has its own help page that describes the properties and parameters. For further information, refer to the configuration manuals of the devices. You will find these on the pages of Siemens Industry Online Support.
- Command Line Interface

  All the configuration settings for the device can be made using the CLI. The CLI provides the same options as Web Based Management (WBM). For further information, refer to the configuration manuals of the devices. You will find these on the pages of Siemens Industry Online Support.

### Operating modes

The following operating modes are available:

- Offline configuration mode

  In this mode only the settings that require no connection to the device are available.
- Online diagnostics mode

  If there is an online connection to the device, additional pages are available in "Online & Diagnostics". The documentation of these pages includes the note "This page is only available if there is an online connection to the device". With some settings, the additional information "only available online" is included.

### Creating and deleting an entry

As an example, an entry will be created and deleted on the Syslog client. The procedure is valid on all pages.

**Creating a new entry**

1. Select the device in the network or device view.
2. Open the properties of the device in the Inspector window.
3. In the Inspector window go to System > Syslog client.
4. Enter the IP address for the Syslog server.
5. Click in the table.
6. Select the entry "New entry" in the shortcut menu.

   A new entry is created in the table.

**Deleting an entry**

1. Select the required entry in the table.
2. Select the "Delete" entry in the shortcut menu.

### Buttons you require often

- **Refresh the display with "**
  **Refresh**
  **"**Pages that display current parameters have a "Refresh" button at the lower edge of the page. Click this button to request up-to-date information from the device for the current page.
- **Save settings for all ports with "**
  **Transfer to table**
  **"**Pages on which you can configure several ports have 2 tables. In the first table, you can make the settings for all ports and transfer these to the second table. In the last column of the first table, there is the "Transfer to table" button. Click this button to save the settings you have made for all ports.

## Showing information

This section contains information on the following topics:

- [Versions](#versions)
- [I&M](#im)
- [ARP / Neighbors](#arp-neighbors)
- [Log tables](#log-tables)
- [Fault](#fault)
- [DHCP Server](#dhcp-server)
- [SNMP](#snmp-2)
- [LLDP](#lldp)
- [Fiber Monitoring Protocol](#fiber-monitoring-protocol)
- [IPv4 Routing](#ipv4-routing)
- [IPv6 Routing (S615)](#ipv6-routing-s615)
- [IPsec VPN](#ipsec-vpn-1)
- [SINEMA RC](#sinema-rc)
- [Redundancy](#redundancy)
- [Unicast](#unicast)
- [Multicast](#multicast)
- [Security](#security)
- [OpenVPN](#openvpn-1)
- [VXLAN (SC63x/SC64x)](#vxlan-sc63xsc64x)

### Versions

This page shows the versions of the hardware and software of the device.

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Description of the displayed values

The table has the following columns:

- **Hardware**

  - Basic Device  
    Shows the basic device
  - PX.X  
    X.X = port in which the SFP module is inserted.
  - SlotX  
    "X" = slot number: Module plugged into this slot.
- **Name**
  Shows the name of the device or module.
- **Revision**Shows the hardware version of the device.
- **Article number**Shows the article number of the device or described module.
- **Software**

  - Firmware  
    Shows the current firmware version. If a new firmware file was downloaded and the device has not yet restarted, the firmware version of the downloaded firmware file is displayed here. After the next restart, the loaded firmware is activated and used.
  - Bootloader  
    Shows the version of the boot software stored on the device.
  - Firmware_Running  
    Shows the firmware version currently being used on the device.
- **Description**Shows the short description of the software.
- **Version**Shows the version number of the software version.
- **Date**Shows the date on which the software version was created.

### I&M

> **Note**
>
> The page is only available if there is an online connection to the device.

This page contains information about device-specific vendor and maintenance data such as the article number, serial number, version number etc. You cannot configure anything on this page.

#### Description

The table has the following rows:

- **Manufacturer ID**
    
  Shows the manufacturer ID.
- Article number

  Shows the article number.
- **Basic MAC address**

  Shows the MAC address of the IPv4 interface.
- **Serial number**
    
  Shows the serial number.
- **Hardware revision**
    
  Shows the hardware version.
- **Software version**
    
  Shows the software version.
- **Revision Counter**
    
  Regardless of a version change, this box always displays the value "0".
- **Revision Date**
    
  Date and time of the last revision
- **Function tag**

  Shows the function tag (plant designation) of the device. The plant designation (HID) is created during configuration of the device with HW Config of STEP 7.
- **Location tag**
    
  Shows the location tag of the device. The location identifier (LID) is created during configuration of the device with HW Config of STEP 7.
- **Date**
    
  Shows the date created during configuration of the device with HW Config of STEP 7.
- **Description**
    
  Shows the description created during configuration of the device with HW Config of STEP 7.

### ARP / Neighbors

This section contains information on the following topics:

- [ARP table](#arp-table)
- [IPv6 Neighbor Table](#ipv6-neighbor-table)

#### ARP table

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Assignment of MAC address and IP address

With the Address Resolution Protocol (ARP), there is a unique assignment of MAC address to IPv4 address. This assignment is kept by each network node in its own separate ARP table. The page shows the ARP table of the device.

##### Description

The table has the following columns:

- **Interface**Shows the interface via which the row entry was learnt.
- **MAC Address**Shows the MAC address of the destination or source device.
- **IP address**Shows the IP address of the target device.
- **Media Type**
  Shows the type of connection.

  - Dynamic  
    The device recognized the address data automatically.
  - Static  
    The addresses were entered as static addresses.

#### IPv6 Neighbor Table

##### Assignment of MAC address and IPv6 address

Via the IPv6 neighbor table, there is a unique assignment of MAC address to IPv6 address. This assignment is kept by each network node in its own separate neighbor table.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description

The table has the following columns:

- **Interface**

  Displays the interface via which the row entry was learnt.
- **MAC Address**

  Shows the MAC address of the destination or source device.
- **IP Address**

  Shows the IPv6 address of the destination device.
- **Media Type**

  Shows the type of connection.

  - Dynamic  
    The device recognized the address data automatically.
  - Static

    The addresses were entered as static addresses.

### Log tables

This section contains information on the following topics:

- [Event log](#event-log)
- [Security log](#security-log)
- [Firewall log](#firewall-log)

#### Event log

##### Logging events

> **Note**
>
> The page is only available if there is an online connection to the device.

The page shows the system events that have occurred in the form of a table. Some of the system events can be configured in "System > Events", for example if the connection status of a port has changed.

The content of the table is retained even when the device is turned off. The event log file can be downloaded using HTTP, TFTP or SFTP.

##### Description of the displayed values

- **Severity Filters**
    
  You can filter the entries in the table in the WBM according to severity. To display all the entries, enable or disable all parameters.

  > **Note**
  >
  > A maximum of 800 entries in the table are possible for each severity. If the maximum number of entries is reached for a severity, the oldest entries of this severity are overwritten in the  
  > table. The table remains permanently in the memory.

  - Info

    Informative
  - When this parameter is enabled, all entries of the category "Info" are displayed.
  - Warning

    Warning

    When this parameter is enabled, all entries of the category "Warning" are displayed.
  - Critical

    Critical

    When this parameter is enabled, all entries of the category "Critical" are displayed.

  The table has the following columns:

  - **Restart**
      
    Counts the number of restarts since you last reset to factory settings and shows the device restart after which the corresponding event occurred.
  - **System Up Time**
      
    Shows the time the device has been running since the last restart when the described event occurred.
  - **System Time**

    If the system time is set, the date and time at which the event occurred are also displayed.

    If no system time is set, the box displays "Date/time not set".
  - **Severity**

    Sorting of the entry into the categories above.
  - **Log Message**
      
    Displays a brief description of the event that has occurred.

#### Security log

> **Note**
>
> The page is only available if there is an online connection to the device.

The page shows the events that occurred during communication via a secure VPN tunnel in the form of the table.

##### Description of the displayed values

- **Severity Filters**

  You can filter the entries in the table in the WBM according to severity. To display all the entries, enable or disable all parameters.

  > **Note**
  >
  > A maximum of 800 entries in the table are possible for each severity. If the maximum number of entries is reached for a severity, the oldest entries of this severity are overwritten in the  
  > table. The table remains permanently in the memory.

  - Info

    Informative

    When this parameter is enabled, all entries of the category "Info" are displayed.
  - Warning

    Warning

    When this parameter is enabled, all entries of the category "Warning" are displayed.
  - Critical

    Critical

    When this parameter is enabled, all entries of the category "Critical" are displayed.

The table has the following columns:

- **Restart**Counts the number of restarts since you last reset to factory settings and shows the device restart after which the corresponding event occurred.
- **System Up Time**Shows the time the device has been running since the last restart when the described event occurred.
- **System Time**

  If the system time is set, the date and time at which the event occurred are also displayed. If no system time is set, the box displays "Date/time not set".
- **Severity**
    
  Sorts the entry into the categories above.
- **Log Message**Displays a brief description of the event that has occurred.

##### Buttons

**"**
**Clear**
**" button**

Click this button to delete the content of the event log file. All entries are deleted regardless of what you have selected in "Severity Filters".

The display is also cleared. The restart counter is only reset after you have restored the device to the factory settings and restarted the device.

#### Firewall log

> **Note**
>
> The page is only available if there is an online connection to the device.

The firewall log logs the events that occurred on the firewall. When you create firewall rules, you can specify the event severity with which they are logged.

##### Description of the displayed values

- **Severity Filters**

  You can filter the entries in the table in the WBM according to severity. To display all the entries, enable or disable all parameters.

  > **Note**
  >
  > A maximum of 800 entries in the table are possible for each severity. If the maximum number of entries is reached for a severity, the oldest entries of this severity are overwritten in the  
  > table. The table remains permanently in the memory.

  - Info

    Informative

    When this parameter is enabled, all entries of the category "Info" are displayed.
  - Warning

    Warning

    When this parameter is enabled, all entries of the category "Warning" are displayed.
  - Critical

    Critical

    When this parameter is enabled, all entries of the category "Critical" are displayed.

The table has the following columns:

- **Restart**Counts the number of restarts since you last reset to factory settings and shows the device restart after which the corresponding event occurred.
- **System Up Time**Shows the time the device has been running since the last restart when the described event occurred.
- **System Time**

  If the system time is set, the date and time at which the event occurred are also displayed. If no system time is set, the box displays "Date/time not set".
- **Severity**
    
  Sorts the entry into the categories above.
- **Log Message**Displays a brief description of the event that has occurred.

##### Description of the buttons and input boxes

**"**
**Clear**
**" button**

Click this button to delete the content of the event log file. All entries are deleted regardless of what you have selected in "Severity Filters".

The display is also cleared. The restart counter is only reset after you have restored the device to the factory settings and restarted the device.

### Fault

#### Error status

If an error occurs, it is shown on this page. On the device errors are signaled by the fault LED lighting up.

Internal errors of the device and errors that you configure on the following pages are indicated:

- "System > Events"
- "System > Fault Monitoring"

Errors of the "Cold/Warm Start" event can be deleted by a confirmation.

The calculation of the time of an error always begins after the last system start.

If there are no errors present, the fault LED switches off.

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Displayed values

- **No. of Signaled Faults**

  Number of errors displayed since the last startup.
- **"**
  **Reset counters**
  **" button**

  Click "Reset Counters" to reset the counter. The counter is reset when there is a restart.

The table contains the following columns:

- **Fault Time**

  Shows the time the device has been running since the last restart when the described fault occurred.
- **Fault Description**

  Displays a brief description of the error that has occurred.
- **Clear Fault State**

  If the "Clear Fault State" button is enabled, you can delete the error.

### DHCP Server

This page shows which IPv4 addresses were assigned to the devices by the DHCP server.

#### Description of the displayed values

- **IP Address**

  Shows the IPv4 address assigned to the DHCP client.
- **Pool ID**

  Shows the number of the IPv4-DHCP-Pool.
- **Identification Method**

  Shows the method with which the DHCP client is identified.

  - Remote ID

    Shows the remote ID of the DHCP client.
  - Circuit ID

    Shows the circuit ID of the DHCP client.
- **Identification Value**

  Shows the value that is assigned to the identification method.
- **Allocation Method**

  Shows whether the IPv4 address was assigned statically or dynamically. You configure the static entries in "System > DHCP > Static Leases".
- **Binding State**
    
  Shows the status of the assignment.

  - Associated  
    The assignment is used.
  - not used  
    The assignment is not used.
  - probing  
    The assignment is being checked.
  - unknown  
    The status of the assignment is unknown.
- **Expire Time**
    
  Shows how long the assigned IPv4 address is still valid. When half the period of validity has elapsed. the DHCP client can extend the period of the assigned IPv4 address. When the entire time has elapsed, the DHCP client needs to request a new IPv4 address.

### SNMP

> **Note**
>
> The page is only available if there is an online connection to the device.

This page displays the created SNMPv3 groups. You configure the SNMPv3 groups in "System" > SNMP"..

#### Description

The table has the following columns:

- **Group Name**

  Shows the group name.
- **User Name**

  Shows the user that is assigned to the group.

### LLDP

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Status of the neighborhood table

This page shows the current content of the neighborhood table. This table stores the information that the LLDP agent has received from connected devices. You set the interfaces via which the LLDP agent receives or sends information in the following section: "Layer 2 > LLDP".

#### Description

The table contains the following columns:

- **System Name**

  System name of the connected device.
- **Device ID**

  Device ID of the connected device. The device ID corresponds to the device name assigned via SINEC PNI (STEP 7). If no device name is assigned, the MAC address of the device is displayed.
- **Local Interface**

  Port at which the device received the information
- **Hold Time**

  Hold time in seconds

  An entry remains stored on the device for the time specified here. If the device does not receive any new information from the connected device during this time, the entry is deleted.
- **Capability**

  Shows the capabilities of the connected device:

  - Router
  - Bridge
  - Telephone
  - DOCSIS Cable Device
  - WLAN Access Point
  - Repeater
  - Station
  - Other
- **Port ID**

  Port of the device with which the device is connected. If no port ID is assigned, the MAC address of the connected device is shown.

### Fiber Monitoring Protocol

#### Monitoring optical links

With Fiber Monitoring, you can monitor optical links. The table shows the current status of the ports.

You set the values to be monitored on the following page: "Layer 2 > FMP".

#### Description of the displayed values

**Port**

Shows the optical ports that support Fiber Monitoring. This depends on the transceivers.

**Rx Power State**

- **disabled**

  Fiber monitoring is disabled.
- **ok**

  The value for the received power of the optical link is within the set limits.
- **maint. req.**

  Check the link.

  A warning is signaled.
- **maint. dem.**

  The link needs to be checked.

  An alarm is signaled and the fault LED is lit.
- **link down**

  The connection to the communications partner is down. No link is detected.

**Rx Power [dBm]**

Shows the current value of the received power. The value can have a tolerance of +/- 3 dB.

If there is no connection (link down) or fiber monitoring is disabled, "-" is displayed. If fiber monitoring is not enabled on the partner port, the value 0.0 is displayed.

**Power Loss State**

To be able to monitor the power loss of the connection the function fiber monitoring must be enabled for the optical port of the connection partner.

- **disabled**

  Fiber monitoring is disabled.
- **ok**

  The value for the power loss of the optical link is within the defined limits.
- **maint. req.**

  Check the link.

  A warning is signaled.
- **maint. dem.**

  The link needs to be checked.

  An alarm is signaled and the fault LED is lit.
- **idle**

  The port has no connection to another port with fiber monitoring enabled.

  If no diagnostics information is received from the optical port of the connection partner for 5 cycles, the fiber monitoring connection is assumed to be interrupted. A cycle lasts 5 seconds.

**Power Loss [dB]**

Shows the current value of the power loss. The value can have a tolerance of +/- 3 dB.

If there is no connection (link down), Fiber Monitoring is disabled or the partner port does not support Fiber Monitoring, "-" is displayed.

### IPv4 Routing

#### Introduction

> **Note**
>
> The page is only available if there is an online connection to the device.

This page shows the routes currently being used.

#### Description of the displayed values

The table has the following columns:

- **Destination Network**Shows the destination address of this route.
- **Subnet Mask**Shows the subnet mask of this route.
- **Gateway**Shows the gateway for this route.
- **Interface**Shows the interface for this route.
- **Metric**Shows the metric of the route. The higher value, the longer packets require to their destination.
- **Routing Protocol**Shows the routing protocol from which the entry in the routing table originates. The following entries are possible:

  - Connected: Connected routes
  - Static: Static routes
  - DHCP: Routes via DHCP

### IPv6 Routing (S615)

#### Overview

This page shows the IPv6 routes currently being used.

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Description

The table has the following columns:

- **Destination Network**

  Shows the destination address of this route.
- **Prefix Length**

  Shows the prefix length of this route.
- **Gateway**

  Shows the gateway for this route.
- **Interface**

  Shows the interface for this route.
- **Metric**

  Shows the metric of the route. The higher value, the longer packets require to their destination.
- **Routing Protocol**

  Shows the routing protocol from which the entry in the routing table originates. The following entries are possible:

  - connected: Connected routes
  - Static: Static routes
  - RIPng: Routes via RIPng
  - OSPFv3: Routes via OSPFv3
  - other: Other routes

### IPsec VPN

The page shows the status of the activated VPN connections.

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Description of the displayed values

This table contains the following columns:

- **Name**

  Shows the name of the VPN connection.
- **Local Host**

  Shows the IP address of the device.
- **Local DN**

  Shows the Distinguished Name (DN) of the device that was signaled to the remote station during connection establishment. The entry is adopted from the "Local ID" box, the device certificate or the IP address of the device.
- **Local Subnet**

  Shows the local subnet.
- **Remote Host​**

  Shows the IP address or the host name of the remote device.
- **Remote DN**

  Shows the Distinguished Name (DN) signaled by the remote device during connection establishment.
- I**Remote Subnet**

  Shows the remote subnet.
- **Rekey Time**

  Shows when the validity of the key expires.
- **Status**

  Shows the status of the VPN connection.

### SINEMA RC

> **Note**
>
> The page is only available if there is an online connection to the device.

Shows information on SINEMA RC Server.

> **Note**
>
> For SCALANCE S615 this function can only be used with a KEY-PLUG.

#### Description of the displayed values

- **Status**

  Shows the status of the connection to SINEMA RC Server.
- **Device Name**

  If configured, the name of the device is displayed.
- **Device Location**

  If configured, the location of the device is displayed.
- **GSM Number**

  If configured, the phone number of the device is displayed.
- **Vendor**

  If configured, the entry is displayed.
- **Comment**

  If configured, the comment is displayed.
- **Type of Connection (Server)**

  Shows which type of connection is set on the SINEMA RC Server.
- **Type of Connection (device)**

  Shows which type of connection is set on the device.
- **Fingerprint**

  Shows the fingerprint of the server certificate. Is only displayed when the fingerprint is used for verification.
- **Remote Address**

  Shows the IP address of the SINEMA RC Server.
- **Connected Local Subnet (s)**

  Shows the IP addresses of the local subnets. Is only displayed when the option "Connected local subnets" is enabled on the SINEMA RC Server. You will find further information on this in the Operating Instructions of the SINEMA RC Server.
- **Connected Local Host (s)**

  Shows the destination IP address of the hosts that can be reached.
- **Tunnel Interface Address**

  Shows the IP address of the virtual tunnel interface.
- **Connected Remote Subnet (s)**

  Shows the subnets of the SINEMA RC Server that are reachable for the device. Which subnets are reachable for the device depends on the communications relations on the SINEMA RC Server. You will find further information on this in the Operating Instructions of the SINEMA RC Server.

### Redundancy

This section contains information on the following topics:

- [Spanning Tree](#spanning-tree)
- [VRRPv3 statistics](#vrrpv3-statistics)
- [Sync Firewall State](#sync-firewall-state)
- [Ring redundancy](#ring-redundancy)

#### Spanning Tree

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Introduction

The page shows the current information about the spanning tree and the settings of the root bridge.

##### Description of the displayed values

The following fields are displayed:

- **Spanning Tree Mode**
    
  Shows the set mode. You specify the mode in "Layer 2 > Configuration" and in "Layer 2 > Spanning Tree > General".  
  The following values are possible:

  - '-'
  - RSTP
- **Bridge Priority / Root Priority**
    
  Which device becomes the root bridge is decided by the bridge priority. The bridge with the highest priority (in other words, with the lowest value for this parameter) becomes the root bridge. If several devices in a network have the same priority, the device whose MAC address has the lowest numeric value will become the root bridge. Both parameters, bridge priority and MAC address together form the bridge identifier. Since the root bridge manages all path changes, it should be located as centrally as possible due to the delay of the frames. The value for the bridge priority is a whole multiple of 4096 with a range of values from 0 to 32768.
- **Bridge Address / Root Address**The bridge address shows the MAC address of the device and the root address shows the MAC address of the root switch.
- Root Cost

  Shows the path costs from the device to the root bridge.
- Bridge Status

  Shows the status of the bridge, e.g. whether or not the device is the root bridge.

The table has the following columns:

- **Port**Shows the interfaces via which the device communicates.
- **Role**

  Shows the status of the port. The following values are possible:

  - Disabled  
    The port was removed manually from the spanning tree and will no longer be taken into account by the spanning tree.
  - Designated  
    The ports leading away from the root bridge.
  - Alternate  
    The port with an alternative route to a network segment
  - Backup  
    If a switch has several ports to the same network segment, the "poorer" Port becomes the backup port.
  - Root  
    The port that provides the best route to the root bridge.
  - Master  
    This port points to a root bridge located outside the MST region.
- **Status**

  Shows the current status of the interface. The values are only displayed. The parameter depends on the configured protocol.

  - Discarding  
    The port receives BPDU frames. Other incoming or outgoing frames are discarded.
  - Listening  
    The port receives and sends BPDU frames. The port is involved in the spanning tree algorithm. Other outgoing and incoming frames are discarded.
  - Learning  
    The port actively learns the topology; in other words, the node addresses. Other outgoing and incoming frames are discarded.
  - Forwarding  
    Following the reconfiguration time, the port is active in the network. The port receives and sends data frames.
- **Oper. Version**
    
  Shows the compatibility mode of Spanning Tree used by the port.
- **Priority**
    
  If the path calculated by the spanning tree is possible over several ports of a device, the port with the highest priority (in other words the lowest value for this parameter) is selected. A value between 0 and 240 can be entered for the priority in steps of 16. If you enter a value that cannot be divided by 16, the value is automatically adapted. The default is 128.
- **Path Cost**
    
  This parameter is used to calculate the path that will be selected. The path with the lowest value is selected. If several ports of a device have the same value, the port with the lowest port number is selected.  
  If the value in the "Cost Calc" field is "0", the automatically calculated value is displayed. Otherwise, the value of the "Cost Calc" field is displayed.  
  The calculation of the path costs is largely based on the transmission speed. The higher the achievable transmission speed is, the lower the value of the path costs.

  Typical values for path costs with rapid spanning tree:

  - 10,000 Mbps = 2,000
  - 1000 Mbps = 20,000
  - 100 Mbps = 200,000
  - 10 Mbps = 2,000,000
- **Edge Type**
    
  Shows the type of the connection. The following values are possible:

  - Edge Port  
    There is an end device at this port.
  - No Edge Port  
    There is a spanning tree or rapid spanning tree device at this port.
- **P.t.P. Type**
    
  Shows the type of point-to-point link. The following values are possible:

  - P.t.P.  
    With half duplex, a point-to-point link is assumed.
  - Shared Media  
    With a full duplex connection, a point-to-point link is not assumed.

#### VRRPv3 statistics

##### Introduction

This page shows the statistics of the VRRPv3 protocol and all configured virtual routers.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description of the displayed values

The following fields are displayed:

- **VRID Errors**

  Shows how many VRRPv3 packets containing an unsupported VRID were received.
- **Version Errors**

  Shows how many VRRPv3 packets containing an invalid version number were received.
- **Checksum Errors**

  Shows how many VRRPv3 packets containing an invalid checksum were received.

The table has the following columns:

- **Interfaces**

  Interface to which the settings relate.
- **VRID**

  Shows the ID of the virtual router. Valid values are 1 ... 255.
- **Address Type**

  Shows the version of the IP protocol.
- **Become Master**

  Shows how often this virtual router changed to the "Master" status.
- **Advertisements Received**

  Shows how many VRRPv3 packets were received.
- **Advertisement Interval Errors**

  Shows how many bad VRRPv3 packets were received whose interval does not match the value set locally.
- **IP TTL Errors**

  Shows how many bad VRRPv3 packets were received whose TTL (Time to live) value in the IP header is incorrect.
- **Prio 0 received**

  Shows how many VRRPv3 packets with priority 0 were received. VRRPv3 packets with priority 0 are sent when a master router is shut down. These packets allow a fast handover to the relevant backup router.
- **Prio 0 sent**

  Shows how many VRRPv3 packets with priority 0 were sent. Packets with priority 0 are sent when a master router is shut down. These packets allow a fast handover to the relevant backup router.
- **Invalid Type**

  Shows how many bad VRRPv3 packets were received whose value in the "Type" field of the IP header is invalid.
- **Address List Errors**

  Shows how many bad VRRPv3 packets were received whose address list does not match the locally configured list.
- **Packet Length Errors**

  Shows how many bad VRRPv3 packets were received whose length is not correct.

#### Sync Firewall State

##### Information on the Firewall State Sync

On this page, you obtain the following information about the Firewall State Sync.

##### Description of the displayed values

The table has the following columns:

- **Sync State**

  Shows the status of the Firewall State Sync:

  - running: Valid messages from the synchronization partner are being received.
  - no receive: No messages were received from the synchronization partner during the valid period (5 seconds).
  - error: The message could not be sent due to an internal error.
  - disabled: The function is disabled.
- **Sent Messages**

  Number of sent synchronization messages.
- **Received Messages**

  Number of valid messages that were transferred by the synchronization partner.
- **Invalid Messages**

  Number of invalid messages that were transferred by the synchronization partner.
- **Reset Counters**

  Click this button to reset the counters on this page.

  **Refresh**

  Refreshes the display of the values. The result is shown in the table.

#### Ring redundancy

This page informs you about the values currently set for the device.

##### Description of the displayed values

The following fields are displayed:

- **Redundancy Function**
    
  The "Redundancy Function" column shows the role of the device within the ring:

  - no Ring Redundancy

    The device is operating without redundancy function.
  - HRP Client

    The IE switch is operating as an HRP client.
  - MRP Client

    The IE switch is operating as an MRP client.
- **Ring Port 1/Ring Port 2**

  The "Ring Port 1" and "Ring Port 2" columns show the ports being used as ring ports. If media redundancy in ring topologies is completely disabled, ring ports configured last are displayed.

### Unicast

This table shows the unicast addresses entered statically by the user during parameter assignment. Entries can be made statically through parameter assignment by the user.

#### Description of the displayed values

- **VLAN ID**Shows the VLAN ID assigned to this MAC address.
- **MAC Address**Shows the MAC address of the node that the device has learned or the user has configured.
- **Status**Shows the status of each address entry:

  - Static  
    Configured by the user. Static addresses are stored permanently; in other words, they are not deleted when the aging time expires or on a restart.
  - Invalid

    These values are not evaluated.
- **Port**
    
  Shows the port via which the node with the specified address can be reached. Frames received by the device whose destination address matches this address will be forwarded to this port.

### Multicast

This table shows the multicast frames currently entered in the multicast filter table and their destination ports. The entries are configured statically by the user.

#### Description of the displayed values

- **VLAN ID**

  Shows VLAN ID of the VLAN to which the MAC multicast address is assigned.
- **MAC Address**

  Shows the MAC multicast address that the device has learned or the user has configured.
- **Status**

  Shows the status of each address entry. The following information is possible:

  - Static  
    The address was entered statically by the user. Static addresses are stored permanently; in other words, they are not deleted when the aging time expires or when the device is restarted. These must be deleted by the user.

### Security

This section contains information on the following topics:

- [Overview](#overview-1)
- [Supported Function Rights](#supported-function-rights)
- [Roles](#roles)
- [Groups](#groups)
- [802.1X Port Status](#8021x-port-status)
- [MAC Authentication](#mac-authentication)

#### Overview

This page shows the security settings and the local and external user accounts.

> **Note**
>
> The page is only available if there is an online connection to the device.
>
> The values displayed depend on the rights of the logged-on user.

##### Description of the displayed values

**Services**

The "Services" list shows the security settings.

- **Telnet Server** (S615)

  You configure the setting in "System > Configuration".

  - Enabled: Unencrypted access to the CLI.
  - Disabled: No unencrypted access to the CLI.
- **SSH Server**

  You configure the setting in "System > Configuration".

  - Enabled: Encrypted access to the CLI.
  - Disabled: No encrypted access to the CLI.
- **SSH Fingerprint x**

  The following SSH fingerprints are displayed:

  - MD5
  - SH256
- **Web Server**

  You configure the setting in "System > Configuration".

  - HTTP/HTTPS: Access to the WBM is possible with HTTP and HTTPS.
  - HTTPS: Access to the WBM is now only possible with HTTPS.
- **SNMP**

  You can configure setting in "System > SNMP > General".

  - "-" (SNMP disabled)  
    Access to device parameters via SNMP is not possible.
  - SNMPv1/v2c/v3  
    Access to device parameters is possible with SNMP versions 1, 2c or 3.
  - SNMPv3  
    Access to device parameters is possible only with SNMP version 3.
- **Login Authentication**

  You configure the setting in "Security > AAA > General".

  - Local

    The authentication must be made locally on the device.
  - RADIUS

    The authentication must be handled via a RADIUS server.
  - Local and RADIUS

    The authentication is possible both with the users that exist on the device (user name and password) and via a RADIUS server.

    The user is first searched for in the local database. If the user does not exist there, a RADIUS query is sent.
  - RADIUS and fallback local

    The authentication must be handled via a RADIUS server.

    A local authentication is performed only when the RADIUS server cannot be reached in the network.
- **Password Policy**

  Shows which password policy is currently being used.

**Local and external user accounts**

You configure local user accounts and roles in "Security > User Accounts"

When you create a local user account an external user account is generated automatically. Local user accounts involve users each with a password for logging in on the device.

In the table "External User Accounts" a user is linked to a role, for example the user "Observer" with the role "user" In this case, the user is defined on a RADIUS server. The roll is defined locally on the device. When a RADIUS server authenticates a user, the corresponding group however is unknown or does not exist, the device checks whether or not there is an entry for the user in the table "External User Accounts". If an entry exists, the user is logged in with the rights of the associated role. If the corresponding group is known on the device, both tables are evaluated. The user is assigned the role with the higher rights.

> **Note**
>
> The table "External User Accounts" is only evaluated if you have set "Vendor Specific" in the RADIUS Authorization Mode.

With CLI you can access external user accounts.

The table "Local User Accounts" has the following columns:

- **User Account**

  Shows the name of the local user.
- **Role**

  Shows the role of the user. You can obtain more information on the function rights of the role in "Information > Security > Roles".

#### Supported Function Rights

The page shows the function rights available locally on the device.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description of the displayed values

- **Function Right**

  Shows the number of the function right. Different rights relating to the device parameters are assigned to the numbers.
- **Description**

  Shows the description of the function right.

#### Roles

The page shows the roles valid locally on the device.

> **Note**
>
> The page is only available if there is an online connection to the device.
>
> The values displayed depend on the role of the logged-on user.

##### Description

The table contains the following columns:

- **Role**

  Shows the role.
- **Function Right**

  Shows the function rights of the role:

  - 1

    Users with this role can read device parameters but cannot change them.
  - 15

    Users with this role can both read and change device parameters.
  - 0

    This is a role that the device assigns internally when the user could not be authenticated. The user is denied access to the device.
- **Description**

  Shows a description of the role.
- **Remote Access**

  Shows which remote access is currently being used.

---

**See also**

DCT__IROLES__DCT_ID_UROLES_LBL_REMOTE_ACCESS_TOOLTIP

#### Groups

This page shows which group is linked to which role. The group is defined on a RADIUS server. The roll is defined locally on the device.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description of the displayed values

The table has the following columns:

- **Group**

  Shows the name of the group. The name matches the group on the RADIUS server.
- **Role**

  Shows the role. Users who are authenticated with the linked group on the RADIUS server receive the rights of this role locally on the device.
- **Description**

  Shows a a description for the link.

#### 802.1X Port Status

This page shows the status of 802.1X authentication as well as the MAC authentication for the individual ports.

##### Description

The table has the following columns:

- **Port**

  All ports of the device are displayed in this column.
- **802.1X Auth. Status**

  The authentication status of the node. The following options are possible:

  - Authorized

    Data traffic via the port is possible after successful authentication with the "802.1X" method.
  - Unauthorized

    Data traffic via the port is not possible because no authentication has taken place with the "802.1X" method yet or the authentication method was not successful.
- **MAC Auth. Port Status**

  Shows the status of the MAC authentication for the port. The following options are possible:

  - -

    MAC authentication was disabled for the port.
  - Individual

    MAC authentication is configured for the port. Clients can be authenticated individually with their MAC address.
  - Blocked

    MAC authentication is configured for the port. Clients are not authenticated individually. The first client that is authenticated opens the port for all clients. No client is authenticated yet.
  - Open

    MAC authentication is configured for the port. Clients are not authenticated individually. The first client that is authenticated opens the port for all clients. The port was opened after successful authentication of a client.
- **MAC Auth. Actual Allowed Addresses**

  Shows the number of nodes that are allowed access after successful MAC authentication.
- **MAC Auth. Actual Blocked Addresses**

  Shows the number of nodes that are allowed access after failed MAC authentication.

#### MAC Authentication

This page shows the MAC addresses for which MAC authentication was performed.

##### Description

The table has the following columns:

- **VLAN ID**

  Shows the VLAN ID assigned to this MAC address.
- **MAC Address**

  Shows the MAC address of the node for which the authentication status is displayed.
- **Status**

  The authentication status of the node. The following options are possible:

  - **Authorized**
      
    Data traffic via the port is possible after successful authentication with the "MAC Authentication" method.
  - **Unauthorized**
      
    Data traffic via the port is not possible because no authentication has taken place with the "MAC Authentication" method yet or the authentication method was not successful.
- **Port**

  Shows the port via which the node with the specified address can be reached.

### OpenVPN

This section contains information on the following topics:

- [Client](#client)
- [Server](#server)

#### Client

The page shows the status of the activated OpenVPN connections.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description of the displayed values

The table contains the following columns:

- **Name**

  Shows the name of the OpenVPN connection.
- **Remote Server**

  Shows the IP address or the hostname of the OpenVPN server.
- **Tunnel Interface IP**

  Shows the IP address of the virtual tunnel interface.
- **Exported Subnets**

  Shows the IP address of the local subnets.
- **Routed Subnets**

  Shows the subnets of the OpenVPN server.
- **Status**

  Shows the status of the OpenVPN connection.

#### Server

The WBM page shows the status of the activated OpenVPN server.

##### Description of the displayed values

The table contains the following columns:

- **Name**

  Shows the name of the OpenVPN connection.
- **Server Port**

  Shows the port via which the OpenVPN server sends data.
- **Certificate CN**

  Shows the "Common Name" of the certificate used. The Common Name designates the domain for which the certificate is issued.
- **Client IP address**

  Shows the IP address of the OpenVPN server.
- **Bytes received**

  Shows how many bytes were received.
- **Bytes sent**

  Shows how many bytes were sent.
- **Connected since**

  Shows how long a connection has been present.

### VXLAN (SC63x/SC64x)

> **Note**
>
> The page is only available if there is an online connection to the device.

This page shows the current content of the VXLAN NVE Peer table.

#### Description of the displayed values

The table contains the following columns:

- **Interface**

  Displays the NVE interface via which the row entry was learned.
- **Remote VTEP IP Address**

  Shows the IPv4 address of the remote VTEP.
- **VNI ID**

  Shows the VNI segment of which the remote VTEP is a member.
- **Remote MAC Address**

  Shows the MAC address of the remote VTEP that the device learned or that was configured.
- **MAC Type**

  Shows how the MAC address of the remote VTEP is obtained.

  - Static:

    The MAC and IP addresses were configured under "Layer 2 > VXLAN > Static MAC Addresses". The static addresses are stored permanently; in other words, they are not deleted when the aging time expires or when the device is restarted.
  - Dynamic:

    The VTEP of the device obtains the MAC address from the received frame.
- **ARP Suppression**

  This function is not supported.

## Configuring system functions

This section contains information on the following topics:

- [Configuration](#configuration)
- [General](#general)
- [Restart](#restart)
- [Load & save](#load-save)
- [Events](#events)
- [SMTP Client](#smtp-client)
- [SNMP](#snmp-3)
- [System time](#system-time)
- [Auto logout](#auto-logout)
- [Button](#button)
- [Syslog Client](#syslog-client)
- [Ports](#ports)
- [Fault Monitoring](#fault-monitoring)
- [PLUG](#plug)
- [Port diagnostics](#port-diagnostics)
- [DNS](#dns)
- [DHCP](#dhcp)
- [cRSP/SRS](#crspsrs)
- [Proxy Server](#proxy-server)
- [SINEMA RC](#sinema-rc-1)
- [Ping](#ping)
- [DCP Discovery](#dcp-discovery)
- [Configuration Backup (S615)](#configuration-backup-s615)
- [Connection Check (S615)](#connection-check-s615)
- [TCP event](#tcp-event)

### Configuration

This section contains information on the following topics:

- [Configuration](#configuration-1)

#### Configuration

##### System configuration

The page contains the configuration overview of the access options of the device.

Specify the services that access the device. With some services, there are further configuration pages on which more detailed settings can be made.

The standard port can also be changed for some services.

> **Note**
>
> **Change standard port**
>
> Some programs can only access the service over the standard port, e.g. TIA Portal accesses HTTPS over standard port 443. Before you change the port, check which port the program uses. When you change the standard port, you must access the service over the changed port.
>
> **Firewall**
>
> The firewall is reinitialized after the ports are changed. This means that the changed ports are applied in the firewall rules. Existing connections, e.g. via the dynamic firewall, can be used with restrictions during this time.

##### Description

The page contains the configuration overview of the access options of the device

- **Telnet Server**

  Enable or disable the "Telnet Server" service for unencrypted access to the CLI.
- **Telnet Port**

  Specify the port for Telnet access to the CLI.
- **SSH Server**

  Enable or disable the "SSH Server" service for encrypted access to the CLI.
- **SSH Port**

  Specify the port for SSH access to the CLI
- **SSH Key Exchange Algorithm Level**

  Configure the level of SSH key exchange algorithm for SSH access to the CLI.

  High (default)

  - Curve25519-sha256
  - Curve25519-sha256@libssh.org
  - Ecdh-sha2-nistp256
  - Ecdh-sha2-nistp384
  - Ecdh-sha2-nistp521
  - Diffie-hellman-group16-sha512
  - Diffie-hellman-group18-sha512

  Low

  - Curve25519-sha256
  - Curve25519-sha256@libssh.org
  - Ecdh-sha2-nistp256
  - Ecdh-sha2-nistp384
  - Ecdh-sha2-nistp521
  - Diffie-hellman-group16-sha512
  - Diffie-hellman-group18-sha512
  - Diffie-hellman-group14-sha256
  - Diffie-hellman-group14-sha1
- **HTTP Server**

  Enable or disable HTTP access to the WBM.
- **HTTP Port**

  Specify the port for HTTP access to the WBM.
- **HTTPS Server**

  Enable or disable HTTP access to the WBM.
- **HTTPS Port**

  Specify the port for HTTPS access to the WBM.
- **HTTP Services**

  Specify how the WBM is accessed:

  - HTTPS

    Access to the WBM is only possible with HTTPS.
  - HTTP/HTTPS

    Access to the WBM is only possible with HTTP and HTTPS.
  - Redirect HTTP to HTTPS

    Access via HTTP is automatically diverted to HTTPS.
- **Minimum TLS Version**

  Specify which minimum TLS version is used.
- **Default Login Page**

  Specify the login page with which the WBM starts by default.

  - Firewall

    Logging into the WBM page for dynamic firewall.
  - Configuration

    Logging into the WBM.
- **SMTP Client**
    
  Enable or disable the SMTP client. You can configure other settings in "System > SMTP Client".
- **Syslog Client**
    
  Enable or disable the Syslog client. You can configure other settings in "System > Syslog Client".
- **DCP Server**
    
  Specify whether or not the device can be accessed with DCP (Discovery and Configuration Protocol):

  - "-" (disabled)  
    DCP is disabled. Device parameters can neither be read nor modified.
  - Read/Write  
    With DCP, device parameters can be both read and modified.
  - Read Only  
    With DCP, device parameters can be read but cannot be modified.
- **Time**
    
  Select the setting from the drop-down list. The following settings are possible:

  - Manual  
    The system time is set manually. You can configure other settings in "System > System Time > Manual Setting".
  - SIMATIC Time  
    The system time is set using a SIMATIC time transmitter. You can configure other settings in "System > System Time > SIMATIC Time Client".
  - SNTP Client  
    The system time is set via an SNTP server. You can configure other settings in "System > System Time > SNTP Client".
  - NTP Client  
    The system time is set via an NTP server. You can configure other settings in "System > System Time > NTP Client".
- **SNMP**
    
  Select the protocol from the drop-down list. The following settings are possible:

  - "-" (SNMP disabled)  
    Access to device parameters via SNMP is not possible.
  - SNMPv1/v2c/v3  
    Access to device parameters is possible with SNMP versions 1, 2c or 3. You can configure other settings in "System > SNMP > General".
  - SNMPv3  
    Access to device parameters is possible only with SNMP version 3. You can configure other settings in "System > SNMP > General".
- **SNMPv1/v2 Read Only**
    
  Enable or disable write access to SNMP variables with SNMPv1/v2c.
- **SNMPv1 Traps**
    
  Enable or disable the sending of SNMPv1 traps (alarm frames). You can configure other settings in "System > SNMP > Traps".
- **SINEMA Configuration Interface**
    
  If the SINEMA configuration interface is enabled, you can download configurations to the device using STEP 7 Basic / Professional.
- **DHCP Client**

  Enable or disable the DHCP client. You can configure other settings in "System > DHCP".
- **DUID-Type**

  Specify which DUID type is used. The DUID types are defined in RFC 3315.

  - DUID-LLT

    DUID is based on the link layer address of the interface and a time stamp
  - DUID-EN

    DUID is assigned by the vendor (EN = enterprise number)
  - DUID-LL

    DUID is based on the link layer address of the interface
- **Link-layer Address Plus Time (LLT)**

  The value is based on the link layer address of the interface and a time stamp. The value is regenerated each time the factory settings are restored.
- **Vendor Enterprise Number (EN)**

  The value is based on the enterprise number specific to the vendor. The value is regenerated each time the factory settings are restored.
- **Link-layer address (LL)**

  The link-layer address is based on the MAC address. The value is regenerated each time the factory settings are restored.
- **Configuration Mode**

  Select the mode from the drop-down list. The following modes are possible:

  - Automatic Save

    Automatic backup mode. Approximately 1 minute after the last parameter change or before you restart the device, the configuration is automatically saved.

    In addition to this, the following message appears in the display area "Changes will be saved automatically in x seconds. Press 'Write Startup Config' to save the changes immediately."

    > **Note**
    >
    > **Interrupting the save**
    >
    > Saving starts only after the timer in the message has elapsed. How long saving takes depends on the device.
    >
    > During the save, the message "Saving configuration data in progress. Please do not switch off the device" is displayed.
    >
    > - Do not switch off the device immediately after the timer has elapsed.
  - Trial

    Trial mode. In Trial mode, although changes are adopted, they are not saved in the configuration file (startup configuration).   
    To save changes in the configuration file, use the "Write Startup Config" button. The display area also shows the message "Trial Mode Active – Press "Write Startup Config" button to make your settings persistent" as soon as there are unsaved modifications. This message can be seen on every WBM page until the changes made have either been saved or the device has been restarted.

### General

This section contains information on the following topics:

- [Device](#device)
- [Coordinates](#coordinates)

#### Device

This page contains the general device information.

##### Description

The page contains the following boxes:

- **Current System Time**(Only available online)  
  Shows the current system time. The system time is either set by the user or by a time-of-day frame: either SINEC H1 time-of-day frame, NTP or SNTP. (read­only)
- **System Up Time**(only available online)  
  Shows the operating time of the device since the last restart. (read­only)
- **Device Type**(only available online)  
  Shows the type designation of the device. (read­only)
- **System Name**

  You can enter the name of the device. The entered name is displayed in the selection area. A maximum of 255 characters are possible. The system name is also displayed in the CLI input prompt. The number of characters in the CLI input prompt is limited. The system name is truncated after 16 characters.
- **System Contact**

  You can enter the name of a contact person responsible for managing the device. A maximum of 255 characters are possible.
- **Location**

  You can enter the location of the device. The entered installation location is displayed in the selection area. A maximum of 255 characters are possible.

  > **Note**
  >
  > **Permitted characters**
  >
  > The following printable ASCII characters (0x20 to 0x7e) are permitted in the input fields **"****System Name****"**, **"****System Contact****"** and **"****Device Location****"**:
  >
  > - 0123456789
  > - A...Z a...z
  > - !"#$%&'()*+,-./:;<=>?@ [\]_{|}~^`
- **Cyclic WBM status update** (S615 / only available online)

  When this is disabled, automatic update of the WBM is switched off. This is suitable for slow 2G connections or contracts with very limited  
  data volume.   
  The following must be taken into account here:

  - No status display update
  - No automatic logoff after user inactivity
  - No message in trial mode
  - No message on automatic saving
  - No progress display when saving or uploading files
  - No automatic forwarding to the changed IP address

#### Coordinates

On this page, you can enter information about the geographic coordinates (latitude, longitude and the height above the ellipsoid according to WGS84).

**Getting the coordinates**

Use suitable maps for obtaining the geographic coordinates of the device.

The geographic coordinates can also be obtained using a GPS receiver. The geographic coordinates of these devices are normally displayed directly and only need to be entered in the input boxes of this page.

##### Description

The page contains the following input boxes with a maximum length of 32 characters.

- **"Latitude" input box**

  Enter the north or south latitude for the location of the device.

  E. G. +49° 1´ 31.67" means that the device is located at 49 degrees, 1 arc minute and 31.67 arc seconds north latitude.  
  A south latitude is shown by a preceding minus character.  
  You can also append the letters N (north latitude) or S (south latitude) to the numeric information (49° 1´ 31.67" N).
- **"Longitude" input box**

  Enter the eastern or western longitude for the location of the device.  
  E. G. +8° 20´ 58.73" means that the device is located at 8 degrees, 20 arc minutes and 58.73 arc seconds eastern longitude.  
  A western longitude is indicated by a preceding minus sign.  
  You can also add the letter E (eastern longitude) or W (western longitude) to the numeric information (8° 20´ 58.73" E).
- **"Height" input box**

  Enter the value of the height above sea level in meters.  
  For example, 158 m means that the device is located at a height of 158 m above sea level.  
  Heights below sea level (for example the Dead Sea) are indicated by a preceding minus sign.

### Restart

Using this page, you can restart the device based on a schedule or manually. In addition, there are various options for resetting to the device defaults.

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Restart

Note the following points about restarting a device:

- You can only restart the device with administrator privileges.
- A device should only be restarted with the buttons of this menu or with the appropriate CLI commands and not by a power cycle on the device.
- If the device is in "Trial" mode, configuration modifications must be saved manually before a restart. Any modifications you have made only become active on the device after clicking the "Set values" button on the relevant WBM page.
- If the device is in "Automatic Save" mode, the last changes are saved automatically before a restart.

#### Description

To restart the device, the buttons on this page provide you with the following options:

- **Restart**Click this button to restart the system. You must confirm the restart in a dialog box. During a restart, the device is reinitialized, the internal firmware is reloaded, and the device runs a self-test. The settings of the start configuration are retained, e.g. the IP address of the device. The learned entries in the address table are deleted. You can leave the browser window open while the device restarts. After the restart you will need to log in again.
- **Restore Memory Defaults and Restart**
  Click this button to restore the factory defaults of the device with the exception of the following parameters and to restart the device:

  - IP addresses
  - Subnet Mask
  - IP address of the default gateway
  - DHCP client ID
  - DHCP
  - System name
  - System location
  - System contact
  - User names and passwords
  - Mode of the device
  - DHCPv6 Rapid Commit
- **Restore Factory Defaults and Restart**Click this button to restore the factory configuration settings and to restart the device. You must confirm the restart in a dialog box.

  > **Note**
  >
  > By resetting all the defaults to the factory configuration settings, the IP address is also lost. The device can then only be addressed via SINEC PNI or via DHCP.
  >
  > With the appropriate attachment, a previously correctly configured device can cause circulating frames and therefore the failure of the data traffic.
- **Restart in: seconds**

  This field is used to set the timer. The field can no longer be edited when the timer is running.

  Specify the amount of time in seconds after which the device restarts.

  Value range 300 ... 86400 seconds
- **Backup**

  The configuration backups under "System **>** Configuration Backup" are available for selection. Before the scheduled restart, the device applies the configurations of the selected backup and continues working with them after the restart.

  All configurations made up to this point that have not been saved in a backup are lost.
- **Schedule restart**

  When you click this button, a timer starts and runs backwards with the defined time. When the timer has expired, the device restarts.

  The following message is also displayed in the display area: "The automatic restart starts in [..] minutes. Click 'Cancel scheduled restart' to cancel the restart". This message can be seen on every WBM page until you cancel the restart or the SCALANCE W device is restarted.

  > **Note**
  >
  > **Unsaved configuration is lost after reboot**
  >
  > The scheduled restart is performed after the time has elapsed without any further message. Unsaved configuration changes are lost.
  >
  > Save the current configuration via "System > Backup of configuration" before setting the timer for the restart.
- **Cancel scheduled restart**

  With this button, you disable the timer for the scheduled restart.

### Load & save

This section contains information on the following topics:

- [Uploading and saving using TFTP](#uploading-and-saving-using-tftp)
- [Uploading and saving using SFTP](#uploading-and-saving-using-sftp)
- [Passwords](#passwords)

#### Uploading and saving using TFTP

##### Loading and saving data via a TFTP server

On this page, you can configure the TFTP server and the file names. You can also store device data in an external file on a TFTP server or load such data from an external file from the TFTP server to the devices. This means, for example, that you can also load new firmware from a file located on a TFTP server.

**Firmware**

The firmware is signed and encrypted. This ensures that only firmware created by Siemens can be downloaded to the device.

> **Note**
>
> **Incompatibility with previous firmware versions with/without PLUG inserted**
>
> During the installation of a previous version, the configuration data can be lost. In this case, the device starts up with the factory settings after the firmware has been installed.
>
> In this situation, if a PLUG is inserted in the device, following the restart, this has the status "NOT ACCEPTED" because the PLUG still has the configuration data of the previous more up-to-date firmware. This allows you to return to the previous, more up-to-date firmware without any loss of configuration data. If the original configuration on the PLUG is no longer required, the PLUG can be deleted or rewritten manually using the WBM page "System > PLUG".

**Configuration files**

> **Note**
>
> **Configuration files and Trial mode /Automatic Save**
>
> In "Automatic Save" mode, the data is saved automatically before the configuration files (ConfigPack and Config) are transferred.  
> In "Trial" mode, although the changes are adopted, they are not saved in the configuration files (ConfigPack and Config). Use the "Write Startup Config" button on the "System > Configuration" WBM page to save changes in the configuration files.

**CLI script file**

You can download existing CLI configurations (RunningCLI) and upload your own CLI scripts (Script).

> **Note**
>
> The downloadable CLI script is not intended to be uploaded again unchanged.
>
> CLI commands for saving and loading files cannot be executed with the CLI script file (Script).

**Exchange of configuration data with STEP 7 Basic/Professional using a file**

You use the two file types "RunningSINEMAConfig" and "SINEMAConfig" to exchange configuration data between a device (WBM) and STEP 7 Basic/Professional via a file.

Requirements:

- Same article number
- Same firmware version
- Password

  You assign the password in the WBM under "System > Load&Save > Passwords".

You can use the file types as follows:

- For offline diagnostics

  You can save the faulty configuration of a device as "RunningSINEMAConfig" via the WBM and import it in STEP 7 Basic/Professional. No connection to a real device is required for the diagnostics in STEP 7 Basic/Professional. You can export a corrected configuration and load it as "SINEMAConfig" again using the WBM.
- For configuration

  No connection to a real device is required to configure a device in STEP 7 Basic/Professional. You can export the configuration and load it as "SINEMAConfig" to the real device using the WBM.

##### Description

- **TFTP Server Address**

  Enter the IP address or the FQDN of the TFTP server with which you exchange data.
- **TFTP Server Port**

  Here, enter the port of the TFTP server via which data exchange will be handled. If necessary, you can change the default value 69 to your own requirements.

The table has the following columns:

- **File type**

  Shows the file type.

  > **Note**
  >
  > **Size of certificate files**
  >
  > With certificate files, only certificates with a maximum of 8192 bits are supported.
- **Description**

  Shows the short description of the file type.
- **File name**

  Enter a file name.
- **Action** (only available online)

  Select the required action. The selection depends on the selected file type, for example you can only save the log file.

  The following actions are possible:

  - **Save file**

    With this selection, you save a file on the TFTP server.
  - **Load file**

    With this selection, you load a file from the TFTP server, e.g. certificates required to establish a secure connection.

> **Note**
>
> Configuration data has a checksum. If you edit the files, you can no longer upload them to the device.
>
> **Password-protected config file**
>
> If the file is password-protected, you cannot load the file via DHCP with options 66 and 67.

#### Uploading and saving using SFTP

##### Loading and saving data via an SFTP server

SFTP (SSH File Transfer Protocol) transfers the files encrypted. On this page, you configure the access data for the SFTP server.

The WBM also allows you to store device data in an external file on your client PC or to load such data from an external file from the PC to the devices. This means, for example, that you can also load new firmware from a file located on your Admin PC.

On this page, the certificates required to establish a secure VPN connection can also be loaded.

**Firmware**

The firmware is signed and encrypted. This ensures that only firmware created by Siemens can be downloaded to the device.

**Configuration files**

> **Note**
>
> **Configuration files and Trial mode /Automatic Save**
>
> In "Automatic Save" mode, the data is saved automatically before the configuration files (ConfigPack and Config) are transferred.  
> In "Trial" mode, although the changes are adopted, they are not saved in the configuration files (ConfigPack and Config). Use the "Write Startup Config" button on the "System > Configuration" WBM page to save changes in the configuration files.

**CLI script file**

You can download existing CLI configurations (RunningCLI) and upload your own CLI scripts (Script).

> **Note**
>
> The downloadable CLI script is not intended to be uploaded again unchanged.
>
> CLI commands for saving and loading files cannot be executed with the CLI script file (Script).

**Exchange of configuration data with STEP 7 Basic/Professional using a file**

You use the two file types "RunningSINEMAConfig" and "SINEMAConfig" to exchange configuration data between a device (WBM) and STEP 7 Basic/Professional via a file.

Requirements:

- Same article number
- Same firmware version
- Password

  You assign the password in the WBM under "System > Load&Save > Passwords".

You can use the file types as follows:

- For offline diagnostics

  You can save the faulty configuration of a device as "RunningSINEMAConfig" via the WBM and import it in STEP 7 Basic/Professional. No connection to a real device is required for the diagnostics in STEP 7 Basic/Professional. You can export a corrected configuration and load it as "SINEMAConfig" again using the WBM.
- For configuration

  No connection to a real device is required to configure a device in STEP 7 Basic/Professional. You can export the configuration and load it as "SINEMAConfig" to the real device using the WBM.

##### Description

The page contains the following boxes:

- **SFTP Server Address**
  Enter the IP address or the FQDN of the SFTP server with which you exchange data.
- **SFTP Server Port**Enter the port of the SFTP server via which data exchange will be handled. If necessary, you can change the default value 22 to your own requirements.
- **SFTP User**Enter the user for access to the SFTP server. This assumes that a user with the corresponding rights has been created on the SFTP server.

  The name must meet the following conditions:

  - It must be unique.
  - It must be between 1 and 250 characters long.
  - The following characters must not be included: § ? " ; :

    The characters for Space and Delete also cannot be included.
- **SFTP Password**

  Enter the password for the user
- **SFTP Password Confirmation**Confirm the password.

The table has the following columns:

- **Type**
    
  Shows the file type.
- **Description**
    
  Shows the short description of the file type.
- **Filename**
    
  A file name is preset here for every file type.

  > **Note**
  >
  > **Changing the file name**
  >
  > You can change the file name preset in this column. After clicking the "Set Values" button, the changed name is saved on the device and can also be used with the Command Line Interface.
- **Actions**
    
  Select the required action. The selection depends on the selected file type, for example you can only save the log file.  
  The following actions are possible:

  - **Save file**With this selection, you save a file on the SFTP server.
  - **Load file**With this selection, you load a file from the SFTP server, e.g. certificates required to establish a secure connection.

#### Passwords

##### Password for files

There are files to which access is password protected. For example to be able to use the HTTPS certificate, you need to specify the corresponding password on this WBM page.

##### Description

The table has the following columns:

- **Type**
    
  Shows the file type.
- **Description**
    
  Shows the short description of the file type.
- **Setting**
- When enabled, the file is used. Can only be enabled if the password is configured.
- **Password**
    
  Enter the password for the file.
- **Password Confirmation**
    
  Confirm the new password.
- **Status**
    
  Shows whether the password corresponds to the file on the device.

  - Valid  
    The "Enabled" check box is selected and the password matches the file.
  - Invalid  
    The "Enabled" check box is selected but the password does not match the file, or no file has been loaded yet.
  - '-'  
    The password cannot be evaluated or is not yet being used. The "Enabled" check box is not selected.
  - Required

    A password is required for loading or saving.

### Events

This section contains information on the following topics:

- [Configuration](#configuration-2)
- [Severity Filters](#severity-filters)

#### Configuration

##### Selecting system events

On this page, you specify which system events are logged and how.

The following messages are always entered in the event log table and cannot be deselected:

- Changing the admin password
- Starting the device
- Operational status of the device, e.g. whether or not a PLUG is inserted
- Status of errors not yet dealt with

For SCALANCE S615, you can send these messages to a Syslog server as well. To do this, select the "Syslog" check box for the "System General Logs" event.

##### Description

Table 1 has the following columns:

- **All Events**
  Shows that the settings are valid for all events of table 2.
- **E-mail**
   **/** 
  **Trap**
   **/** 
  **Log Table**
   **/** 
  **Syslog**
   **/** 
  **Fault**
   **/** 
  **Digital Output**
   **/**
  **VPN Tunnel**
   **/** 
  **Cloud Connector** (S615) **/** **Firewall**Enable or disable the required type of notification for all events. If "No Change" is selected, the entries of the corresponding column in table 2 remain unchanged.
- **Copy To Table**
    
  If you click the button, the setting is adopted for all events of table 2.

Table 2 has the following columns:

- **Event**

  The "Event" column contains the following:

  - Cold/Warm Start   
    The device was turned on or restarted by the user. In the error memory of the device a new entry is generated with the type of restart performed.
  - Link Change This event occurs only when the port status is monitored and has changed, see "System > Fault Monitoring > Link Change".
  - Authentication FailureThis event occurs when access is attempted with an incorrect password.
  - Power Change

    This event occurs only when power supply lines 1 and 2 are monitored. It indicates that there was a change to line 1 or line 2. See "System > Fault Monitoring > Power Supply".
  - Fault State Change

    For a fault to also be signaled by the fault LED "F", you must enable "Fault State Change" for the "Digital Out". In this case, the fault LED "F" lights up when an internal error occurs and the digital input is closed.
  - Security Logs  
    An entry is made in the security log if the IPsec method is used for VPN or a SINEMA RC connection is enabled.
  - Firewall Logs  
    Each time individual firewall rules are applied, this is recorded in the firewall log. To do this, the LOG function must be enabled for the various firewall functions.
  - DDNS Client Logs  
    The event occurs when the DDNS client synchronizes the assigned IP address with the hostname registered at the DDNS provider.
  - Digital Input

    The event occurs when the status of the digital input has changed.
  - System Connection Status (S615)  
    The connection status has changed.
  - System General Logs (S615)   
    Connection establishment, change to the configuration.
  - Digital In  
    The event occurs when the status of the digital input has changed.
  - VPN Tunnel  
    The event occurs when the status of VPN (IPsec, OpenVPN, SINEMA RC) has changed.
  - NTP (secure)

    The event occurs when the status of the secure NTP server has changed.
  - Configuration Change  
    This event occurs when the configuration of the device has changed.
  - Service Information

    For certain events, entries are made in the log table even without configuration. For these events, you can configure additional subsequent actions here (e-mail, trap, syslog).
  - Connection Check (S615)

    This event occurs when connections are being monitored, see "System > Connection Check".
  - TCP Event Log (S615)

    The device has received a TCP packet. The prerequisite is that the "TCP Event" function is enabled.
- **E-mail**The device sends an e-mail. This is only possible if the SMTP server is set up and the "SMTP Client" function is enabled.
- **Trap**
  The device sends an SNMP trap. This is only possible if "SNMPv1 Traps" is enabled in "System > Configuration".
- **Log Table**The device writes an entry in the event log table, see "Information > Log Table".
- **Syslog**
  The device writes an entry to the system log server. This is only possible if the system log server is set up and the "Syslog Client" function is enabled.
- **Fault**
    
  The device triggers a fault. The fault LED lights up
- **Digital Out**

  Controls the digital output or signals the status change with the "DO" LED. By default, the digital output is closed. The digital output is opened when you activate at least one event for the digital output. It also is no longer automatically connected to the fault LED. You connect the digital output with the fault LED under "Fault State Change".
- **VPN Tunnel**
    
  Controls the forwarding of an event to a VPN connection (IPsec, OpenVPN, SINEMA RC). As long as the event is present, the VPN connection is switched to active.
- **Cloud Connector** (S615)   
  Controls the forwarding of an event to the TIA Portal Cloud Connector communication. The communication connection is active as long as the event is present.
- **Firewall**
    
  Controls application of the user-defined rule set. This requires a rule set to be assigned to the digital input under "Security > Firewall > ".

#### Severity Filters

On this page, you configure the severity for the sending of system event notifications.

##### Description

The table has the following columns:

- **Client Type** 
    
  Select the client type for which you want to make settings:

  - **E-mail**
      
    Sending system event messages by e-mail.
  - **Log Table**
      
    Entry of system events in the log table.
  - **Syslog**
      
    Entry of system events in the Syslog file
- **Severity**
    
  Select the required level. The following settings are possible:

  - **Info**
      
    The messages of all levels are sent or logged.
  - **Warning**
      
    The message of this level and the "critical" level are sent or logged.
  - **Critical**
      
    Only the messages of this level are sent or logged.

### SMTP Client

This section contains information on the following topics:

- [General](#general-1)
- [Recipient](#recipient)

#### General

##### Network monitoring with e-mails

If events occur, the device can automatically send an e-mail, e.g. to the service technician. The e-mail contains the identification of the sending device, a description of the cause in plain text, and a time stamp. This allows centralized network monitoring to be set up for networks with few nodes based on an e-mail system.

The setting "E-mail" must be enabled in the events for e-mails to be sent. The messages that can be sent depend on the set severity. You configure the associated e-mail addresses to which the device sends an e-mail during testing or if a fault occurs in the "Recipient" tab.

##### Requirements for sending e-mails

- "E-mail" is activated for the relevant event in "System > Events > Configuration".
- The desired severity is configured under "System > Events > Severity level".
- At least one entry exists under "System > SMTP Client > Recipient" and the setting "Send" is activated.

##### Description

The page contains the following boxes:

- **SMTP Client**

  Enable or disable the SMTP client.
- **SMTP Server Address**

  Enter the IP address or the FQDN (Fully Qualified Domain Name) of the SMTP server.

The table contains the following columns:

- **Status**

  Specify whether this SMTP server will be used.
- **SMTP Server Address**

  Shows the IP address or the FQDN (Fully Qualified Domain Name) of the SMTP server.
- **Sender Email Address**

  Enter the e-mail address of the sender that is specified in the e-mail.
- **User Name**

  If necessary, enter the user name used for authentication on the SMTP server.
- **Password**

  If necessary, enter the password used for authentication on the SMTP server.
- **Password Confirmation**

  Repeat the password.
- **Port**

  Enter the port via which your SMTP server can be reached.

  Factory settings:

  - 25 (None)
  - 465 (SSL/TLS and StartTLS)
- **Security**

  Specify whether transfer of the e-mail from the device to the SMTP server is encrypted. This is only possible when the SMTP server supports the selected setting.

  > **Note**
  >
  > **2-factor authentication (2FA)**
  >
  > 2-factor authentication is not supported.

  - SSL/TLS
  - StartTLS
  - None  
    The e-mail is transferred unencrypted.
- **Test**
  (only available online)

  Sends a test e-mail to the configured recipients.
- **Test result** (only available online)

  Shows whether the e-mail was sent successfully or not. If sending was not successful, the message contains possible causes.

#### Recipient

On this page, you specify who receives an e-mail when an event occurs.

##### Description

The page contains the following boxes:

- **SMTP Server**

  Specify the SMTP server via which the e-mail is sent.
- **E­mail address of the SMTP recipient**

  Enter the e-mail address to which the device sends an e-mail.

The table contains the following columns:

- **SMTP Server**

  Shows the IP address or the FQDN (Fully Qualified Domain Name) of the SMTP server to which the entry relates.
- **Send**

  When enabled, the device sends an e-mail to this recipient.
- **E­mail address of the SMTP recipient**

  Shows the e-mail address to which the device sends an e-mail if a fault occurs.

### SNMP

This section contains information on the following topics:

- [General](#general-2)
- [SNMPv3 Access](#snmpv3-access)
- [SNMPv3 Views](#snmpv3-views)
- [SNMPv3 User to Group mapping](#snmpv3-user-to-group-mapping)
- [SNMPv3 Users](#snmpv3-users)
- [Notifications](#notifications)

#### General

##### Configuration of SNMP

On this page, you make the basic settings for SNMP. Enable the check boxes according to the function you want to use.

##### Description

The page contains the following boxes:

- **SNMP**
    
  Select the SNMP protocol from the drop-down list. The following settings are possible:

  - "-" (Disabled)  
    SNMP is disabled.
  - SNMPv1/v2c/v3  
    SNMPv1/v2c/v3 is supported.

    > **Note**
    >
    > Note that SNMP in versions 1 and 2c does not have any security mechanisms.
  - SNMPv3  
    Only SNMPv3 is supported.
- **SNMPv1/v2c Read-Only**
    
  If you enable this option, SNMPv1/v2c can only read the SNMP variables.

  > **Note**
  >
  > **Community String**
  >
  > For security reasons, do not use the standard values "public" or "private". Change the community strings following the initial installation.
  >
  > The recommended minimum length for community strings is 6 characters.
  >
  > For security reasons, only limited access to objects of the SNMPCommunityMIB is possible with the SNMPv1/v2c Read Community String. With the SNMPv1/v2c Read/Write Community String, you have full access to the SNMPCommunityMIB.
- **SNMPv1/v2c Read Community String**
    
  Enter the community string for read access of the SNMP protocol.
- **SNMPv1/v2c Read/Write Community String**
    
  Enter the community string for read and write access of the SNMP protocol.
- **SNMPv3 User Migration**

  - **Enabled**

    If the function is enabled, an SNMP engine ID is generated that can be migrated. You can transfer configured SNMPv3 users to a different device.

    If you enable this function and load the configuration of the device on another device, configured SNMPv3 users are retained.
  - **Disabled**

    If the function is disabled, a device-specific SNMP engine ID is generated. To generate the ID, the agent MAC address of the device is used. You cannot transfer this SNMP user configuration to other devices.

    If you load the configuration of the device on another device, all configured SNMPv3 users are deleted.
- **SNMP Engine ID**

  Shows the SNMP engine ID.
- **SNMP Agent Listen Port**

  Specify the port at which the SNMP agent waits for the SNMP queries. Standard port 161 is the default.

  You can optionally enter the standard port 162 or a port number in the range 1024 … 49151 or 49500 ... 65535.

#### SNMPv3 Access

##### Security settings and assigning permissions

SNMP version 3 allows permissions to be assigned, authentication, and encryption at protocol level. The security level and read/write permissions are defined according to groups. The settings automatically apply to every member of a group.

> **Note**
>
> Different access permissions for different security levels can be assigned to a group. If no access permission is defined for a security level, no access to the device is possible for members of the group using this security level.

##### Description

The page contains the following boxes:

- **Group Name**

  Select the name of the group.
- **Security Level**

  Select the security level (authentication, encryption) for which you want to define the access permissions of the group.

  - **No Auth/no Priv**
    **.**

    No authentication enabled / no encryption enabled.
  - **Auth/no Priv**.

    Authentication enabled / no encryption enabled.
  - **Auth/Priv**
    **.**

    Authentication enabled / encryption enabled.

The table has the following columns:

- **Select**
    
  Select the row you want to delete.
- **Group Name**

  Shows the defined group names.

  > **Note**
  >
  > Once a group name and the security level have been specified, they can no longer be modified after the group is created. If you want to change the group name or the security level, you will need to delete the group and recreate it and reconfigure it with the new name.
- **Security Level**

  Shows the configured security level.
- **Read View Name**
    
  Enter an SNMPv3 view that grants read access to members of the group with the specified Security Level.
- **Write View Name**
    
  Enter an SNMPv3 view that grants write access to members of the group with the specified Security Level.

  > **Note**
  >
  > For write access to work, you also need to enable read access.
- **Notify View Name**

  Enter an SNMPv3 view to be used for SNMP notifications to members of the group with the defined security level.

#### SNMPv3 Views

##### Configuration of SNMPv3 views

You configure the parameters of SNMP views on this page.

> **Note**
>
> **Controlling the SNMPv1 and SNMPv2c access**
>
> The preconfigured **SIMATICNETRD** and **SIMATICNETWR** views are used internally to control the SNMPv1 and SNMPv2c access. If you delete or change these views, this directly affects the SNMPv1 and SNMPv2c access.

##### Description

The page contains the following boxes:

- **View Name**Select the name of the view that you want to configure. An SNMPv3 view always needs to be assigned to an SNMPv3 access. For this reason, you need to enter a new SNMPv3 view in the table in the "SNMP Access" tab.
- **MIB Tree**Select the Object Identifier (OID) of the MIB area that is to be used for the SNMPv3 view. The available options are as follows:

  - **iso**
  - **std**
  - **member-body**
  - **org**
  - **mgmt**
  - **private**
  - **snmpV2**

  The drop-down list only contains the OIDs that are usually used. If the configuration of a specific OID that is not listed is necessary, you can configure this via the CLI with the `snmp view` command. This OID is then also displayed in the WBM in the overview table.

The table has the following columns:

- **Select**
    
  Select the row you want to delete.
- **View Name**
    
  The name of the SNMPv3 view.
- **MIB Tree**The OID of the MIB area for the SNMPv3 view.
- **View Type**
    
  The available options are as follows:

  - **Included**
      
    The MIB OID and its lower-level nodes are part of the SNMPv3 view. Access to the corresponding MIB objects is possible.
  - **Excluded**
      
    The MIB OID and its lower-level nodes are not part of the SNMPv3 view. Access to the corresponding MIB objects is not possible.

#### SNMPv3 User to Group mapping

##### Configuration of group members

You assign users to SNMPv3 groups on this WBM page. Each user can only be a member of one group.

##### Description

The page contains the following boxes:

- **Group Name**

  Enter the group that will be assigned to the user.
- **User Name**

  Select the user to be a member of the specified group. The drop-down list only contains users that are not yet assigned to a group.

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **Group Name**

  Displays the SNMPv3 group. A group name can only be changed later if no access rights have been defined for the group yet.
- **User Name**

  Shows the user that is a member of this group.

#### SNMPv3 Users

##### User-specific security settings

On the page, you can create new SNMPv3 users and modify or delete existing users. The user-based security model works with the concept of the user name; in other words, a user ID is added to every frame. This user name and the applicable security settings are checked by both the sender and recipient.

##### Description

The page contains the following boxes:

- **User Name**
  Enter a freely selectable user name. After you have entered the data, you can no longer modify the name.

The table has the following columns:

- **Select**
    
  Select the row you want to delete.
- **User Name**
    
  Shows the created users.
- **Authentication Protocol**

  Specify the authentication protocol for which a password will be stored.

  The following settings are available:

  - None
  - MD5
  - SHA
- **Encryption Protocol**

  Specify the encryption protocol for which a password will be stored. This drop-down list is only enabled when an authentication protocol has been selected.

  The following settings are available:

  - None
  - DES
  - AES
- **Authentication Password**
    
  Enter the authentication password in the first input box. This password must have at least 1 character, the maximum length is 32 characters.

  > **Note**
  >
  > **Length of the password**
  >
  > As an important measure to maximize security, we recommend that the password has a minimum length of 6 characters and that it contains special characters, uppercase/lowercase letters and numbers.
- **Authentication Password Confirmation**
    
  Confirm the password by repeating the entry.
- **Privacy Password**
    
  Enter your encryption password. This password must have at least 1 character, the maximum length is 32 characters.

  > **Note**
  >
  > **Length of the password**
  >
  > As an important measure to maximize security, we recommend that the password has a minimum length of 6 characters and that it contains special characters, uppercase/lowercase letters and numbers.
- **Privacy Password Confirmation**
    
  Confirm the encryption password by repeating the entry.

#### Notifications

If an alarm event occurs, a device can send SNMP notifications (traps and inform notifications) to up to ten different management stations at the same time. Notifications are only sent for events that were specified in the "Events" menu.

##### Description

The page contains the following boxes:

- **SNMPv1 Traps**

  Enable or disable the sending of SNMPv1 traps. This setting affects all recipients of SNMPv1 traps and has no effects on recipients of SNMPv2c or SNMPv3 notifications.
- **SNMPv1/v2c Trap Community String**

  Enter the community string for sending SNMPv1/v2c notifications.
- **SNMPv3 Notify User**

  Select the user who is to receive SNMPv3 notifications.
- **SNMPv3 Notify Security Level**

  Select the security level (authentication, encryption) that is to be used for the SNMPv3 notification. A user and the access must be configured for this.

  The available options are as follows:

  - no Auth/no Priv

    No authentication enabled / no encryption enabled.
  - Auth/no Priv

    Authentication enabled / no encryption enabled.
  - Auth/Priv

    Authentication enabled / encryption enabled.
- **Notification Receiver Type**

  The recipient type specifies the SNMP version and the type of notification. SNMP Inform notifications must be acknowledged by the recipient, SNMP traps do not. The available options are as follows:

  - SNMPv1 Trap
  - SNMPv2c Trap
  - SNMPv2c Inform
  - SNMPv3 Trap
  - SNMPv3 Inform
- **Notification Receiver Address**

  Enter the IP address of the receiver station to which the device sends SNMP notifications. You can specify up to ten different recipients.

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **Notification Receiver Address**

  If necessary, change the IP address of the stations.
- **Notification Receiver Type**

  Shows the specified recipient type.
- **SNMP Engine ID**

  The ID of the SNMP Engine to which the SNMPv3 Inform notifications are sent. You can only configure this parameter for the recipient type "SNMPv3 Inform".
- **Notification**

  Enable or disable the sending of SNMP notifications. Stations that are entered but not selected do not receive SNMP notifications.

  > **Note**
  >
  > If a table row is grayed out, the corresponding notification was configured via the CLI and can only be deleted via the CLI.

### System time

This section contains information on the following topics:

- [Overview](#overview-2)
- [Manual setting](#manual-setting)
- [DST overview](#dst-overview)
- [DST configuration](#dst-configuration)
- [SNTP client](#sntp-client)
- [NTP client](#ntp-client)
- [SIMATIC time client](#simatic-time-client)
- [NTP server](#ntp-server)

#### Overview

There are different methods that can be used to set the system time of the device. Only one method can be active at any one time.

If one method is activated, the previously activated method is automatically deactivated.

#### Manual setting

##### Manual setting of the system time

On this page, you set the date and time of the system. For this setting to be used, enable "Time Manually".

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description

The page contains the following boxes:

- **Time Manually**Enable the manual time setting. If you enable the option, the "System Time" input box can be edited.
- **System Time**
  Enter the date and time in the format "MM/DD/YYYY HH:MM:SS".

  After a restart, the time of day begins at 01/01/2000 00:00:00.
- **Use PC Time**
    
  Click the button to use the time setting of the PC.
- **Last Synchronization Time**
    
  Shows when the last time-of-day synchronization took place. If no time-of-day synchronization was possible, the box displays "Date/time not set".
- **Last Synchronization Mechanism**
    
  Shows how the last time synchronization was performed.

  - Not set  
    The time was not set.
  - Manual  
    Manual time setting
  - SNTP  
    Automatic time-of-day synchronization using SNTP
  - NTP  
    Automatic time-of-day synchronization using NTP
  - SIMATIC  
    Automatic time-of-day synchronization using the SIMATIC time frame
- **Daylight Saving Time (DST)**Shows whether the daylight saving time changeover is active.

  - active (offset +1 h)

    The system time was changed to daylight saving time; in other words, an hour was added. You can see the current system time at the top right in the selection area of the WBM.

    The current time including daylight saving time is displayed in the "System Time" box.
  - inactive (offset +0 h)  
    The current system time is not changed.

#### DST overview

##### Daylight saving time switchover

On this page, you can create new entries for the daylight saving time changeover. The table provides an overview of the existing entries.

##### Description

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **DST No.**

  Shows the number of the entry.

  If you create a new entry, a new line with a unique number is created.
- **Name**

  Shows the name of the entry.
- **Year**

  Shows the year for which the entry was created.
- **Start Date**

  Shows the month, day and time for the start of daylight saving time.
- **End Date**

  Shows the month, day and time for the end of daylight saving time.
- **Recurring Date**

  With an entry of the type "Rule", the period in which daylight saving time is active is displayed consisting of week, day, month and time of day. With an entry of the type "Date" a "-" is displayed.
- **State**

  Shows the state of the entry:

  - Enabled

    The entry was created correctly.
  - Invalid

    The entry was created new and the start and end date are identical.
- **Type**
    
  Shows how the daylight saving time changeover is made:

  - Date

    A fixed date is entered for the daylight saving time changeover.
  - Recurring

    A rule was defined for the daylight saving time changeover.

#### DST configuration

##### Configuring the daylight saving time switchover

On this page, you can configure the entries for the daylight saving time changeover. As result of the changeover to daylight saving or standard time, the system time for the local time zone is correctly set. You can define a rule for the daylight saving time changeover or specify a fixed date.

##### Description

> **Note**
>
> The content of this page depends on the selection in the "Type" box.
>
> The boxes "DST No.", "Type" and "Name" are always shown.

- **DST No.**

  Select the type of the entry.
- **Type**
    
  Select how the daylight saving time changeover is made:

  - Date

    You can set a fixed date for the daylight saving time changeover. This setting is suitable for regions in which the daylight saving time changeover is not governed by rules.
  - Recurring

    You can define a rule for the daylight saving time changeover. This setting is suitable for regions in which the daylight saving time always begins or ends on a certain weekday.
- **Name**

  Enter a name for the entry. The name can be a maximum of 16 characters long.

**Settings with "Date" selected**

You can set a fixed date for the start and end of daylight saving time.

- **Year**

  Enter the year for the daylight saving time changeover.
- **Start Date**

  Enter the following values for the start of daylight saving time:

  - Day

    Specify the day.
  - Hour

    Specify the hour.
  - Month

    Specify the month.
- **End Date**

  Enter the following values for the end of daylight saving time:

  - Day

    Specify the day.
  - Hour

    Specify the hour.
  - Month

    Specify the month.

**Settings with "Recurring" selected**

You can create a rule for the daylight saving time changeover.

- **Start Date**

  Enter the following values for the start of daylight saving time:

  - Hour

    Specify the hour.
  - Month

    Specify the month.
  - Week

    Specify the week.

    You can select the first to fourth or the last week of the month.
  - Weekday

    Specify the weekday.
- **End Date**

  Enter the following values for the end of daylight saving time:

  - Hour

    Specify the hour.
  - Month

    Specify the month.
  - Week

    Specify the week.

    You can select the first to fourth or the last week of the month.
  - Weekday

    Specify the weekday.

#### SNTP client

There are different methods that can be used to set the system time of the device. Only one method can be active at any one time. If one method is activated, the previously activated method is automatically deactivated.

SNTP (Simple Network Time Protocol) is used for synchronizing the time in the network. The appropriate frames are sent by an SNTP server in the network.

> **Note**
>
> To avoid time jumps, make sure that there is only one time server in the network.

##### Description

- **SNTP Client**

  Enable or disable automatic time-of-day synchronization using SNTP.
- **Current System Time** (only available online)

  Shows the current date and current normal time received by the device. If you specify a time zone, the time information is adapted accordingly.
- **Last Synchronization Time** (only available online)  
  Shows when the last time-of-day synchronization took place.
- **Last Synchronization Mechanism** (only available online)  
  Shows how the last time-of-day synchronization was performed. The following methods are possible:

  - Not set  
    The time was not set.
  - Manual  
    Manual time setting
  - SNTP  
    Automatic time-of-day synchronization using SNTP
  - NTP  
    Automatic time-of-day synchronization using NTP
  - SIMATIC  
    Automatic time-of-day synchronization using the SIMATIC time frame
- **Time Zone**

  Enter the time zone you are using in the format "+/- HH:MM". The time zone relates to UTC standard world time.

  The time in the "Current System Time" box is adapted accordingly.
- **Daylight Saving Time** (only available online)Shows whether the daylight saving time changeover is active.

  - active (offset +1 h)

    The system time was changed to daylight saving time; in other words, an hour was added. You can see the current system time at the top right in the selection area of the WBM.

    The set time continues to be displayed in the "System Time" box.
  - inactive (offset +0 h)  
    The current system time is not changed.
- **SNTP Mode**

  Select the synchronization mode. The following types of synchronization are possible:

  - Poll  
    If you select this protocol type, the input boxes "SNTP Server Address", "SNTP Server Port" and "Poll Interval[s]" are displayed to allow further configuration. With this type of synchronization, the device is active and sends a time query to the SNTP server.
  - Listen  
    With this type of synchronization, the device is passive and receives SNTP frames that deliver the time of day.

    Enable the entry "System Time" under "Security > Firewall > Pre-defined IPv4 rules".
- **Poll Interval[s]**Enter the interval between two-time queries. In this box, you enter the query interval in seconds. Possible values are 16 to 16284 seconds.
- **SMTP Server Address**

  Enter the IP address or the FQDN (Fully Qualified Domain Name) of the SNTP server.
- **SNTP Server Port**

  Enter the port of the SNTP server.

  The following ports are possible:

  - 123 (standard port)
  - 1025 to 36564

  Only for S615: The table has the following columns:
- **SMTP Server Address**
  Shows the IP address, the FQDN (Fully Qualified Domain Name) or the host name of the SMTP server.
- **SNTP Server Port**
  Enter the port of the SNTP server.   
  The following ports are possible:

  - 123 (standard port)
  - 1025 to 36564
- **Primary**
  The check mark is set for the SNTP server that you create first. If several SNTP servers have been created, the primary server is queried first.

#### NTP client

If you require time-of-day synchronization using NTP, you can make the relevant settings here.

> **Note**
>
> To avoid time jumps, make sure that there is only one time server in the network.

##### Description

- **NTP Client**

  When enabled, the device receives the system time from an NTP server.
- **NTP Client only (secure)**When enabled, the device receives the system time from a secure NTP server. The setting applies to all server entries.

  To enable the secure NTP client, the parameters for authentication (key ID, hash algorithm, key) must be configured. These entries must be present on the secure NTP server.
- **Current System Time** (only available online)

  Shows the current date and current normal time received by the device. If you specify a time zone, the time information is adapted accordingly.
- **Last Synchronization Time** (only available online)  
  Shows when the last time-of-day synchronization took place.
- **Last Synchronization Mechanism** (only available online)  
  Shows how the last time-of-day synchronization was performed. The following methods are possible:

  - Not set  
    The time was not set.
  - Manual  
    Manual time setting
  - SNTP  
    Automatic time-of-day synchronization using SNTP
  - NTP  
    Automatic time-of-day synchronization using NTP
  - SIMATIC  
    Automatic time-of-day synchronization using the SIMATIC time frame
- **Time Zone**

  Enter the time zone you are using in the format "+/- HH:MM". The time zone relates to UTC standard world time.

  The time in the "Current System Time" box is adapted accordingly.
- **Daylight Saving Time** (only available online)Shows whether the daylight saving time changeover is active.

  - active (offset +1 h)

    The system time was changed to daylight saving time; in other words, an hour was added. You can see the current system time at the top right in the selection area of the WBM.

    The set time continues to be displayed in the "System Time" box.
  - inactive (offset +0 h)  
    The current system time is not changed.
- **NTP Server Index**Select the index of the NTP server. The server with the lowest index is queried first.
- **NTP Server Address**
    
  Enter the IP address or the FQDN (Fully Qualified Domain Name) of the NTP server.
- **NTP Server Port**Enter the port of the NTP server.  
  The following ports are possible:

  - 123 (standard port)
  - 1025 to 36564
- **Poll Interval**Specify the interval between two-time queries. The greater the interval, the less accurate the time of the device. Possible values are 64 to 2592000 seconds (30 days).
- **Key ID**
  Enter the ID of the authentication key.
- **Hash Algorithm**Specify the format for the authentication key.
- **Key**Enter the authentication key. The length depends on the hash algorithm.

  - DES: ASCII 8 characters
  - MD5: ASCII 16 – 128 characters
  - SHA1: ASCII 20 – 128 characters
- **Key Confirmation**

  Repeat the authentication key.

#### SIMATIC time client

##### Time setting via SIMATIC time client

On this page, you configure time synchronization with the SIMATIC Time Client.

> **Note**
>
> To avoid time jumps, make sure that there is only one time server in the network.

##### Description

- **SIMATIC Time Client**

  Select this check box to enable the device as a SIMATIC time client.
- **Current System Time** (only available online)

  Shows the current system time.
- **Last Synchronization Time** (only available online)  
  Shows when the last time-of-day synchronization took place.
- **Last Synchronization Mechanism** (only available online)  
  Shows how the last time-of-day synchronization was performed. The following methods are possible:

  - Not set  
    The time was not set.
  - Manual  
    Manual time setting
  - SNTP  
    Automatic time-of-day synchronization using SNTP
  - NTP  
    Automatic time-of-day synchronization using NTP
  - SIMATIC  
    Automatic time-of-day synchronization using the SIMATIC time frame
  - PTP  
    Automatic time-of-day synchronization with PTP
- **Daylight Saving Time** (only available online)  
  Shows whether the daylight saving time changeover is active.

  - active (offset +1 h)

    The system time was changed to daylight saving time; in other words, an hour was added. You can see the current system time at the top right in the selection area of the WBM.

    The set time continues to be displayed in the "System Time" box.
  - inactive (offset +0 h)  
    The current system time is not changed.

#### NTP server

On this page, you configure the device as an NTP server. The other devices can call up the current time via this NTP server. This means that the supplied devices are not dependent on a connection to an external time server.

##### Requirement

To receive the NTP frames, enable the entry "System Time" under "Security > Firewall > Pre-defined IPv4 rules".

##### Description

The page contains the following boxes:

- **NTP Server**

  Enable or disable the service NTP server.

> **Note**
>
> "Listen" SNTP mode of the SNTP client and NTP server cannot be enabled at the same time.

Table 1 has the following columns

- **At all interfaces**

  Shows that the settings are valid for all interfaces of table 2.
- **Listen**

  In the drop-down list, select the setting for all interfaces. If "No Change" is selected, the entries of the corresponding column in table 2 remain unchanged.
- **Copy to Table**

  If you click the button, the setting is adopted for all interfaces of table 2.

Table 2 has the following columns

- **Interface**

  Via this interface the time is transferred using NTP.
- **Listen**

  When enabled, the other devices can call up the time via this interface.
- **Server Port**Enter the port of the NTP server.  
  The following ports are possible:

  - 123 (standard port)
  - 1025 to 36564
- **Secure**

  When this is enabled, the NTP server becomes an NTP server of the type "NTP (secure)".

The following columns are only relevant for "NTP (secure)". Otherwise, these boxes cannot be edited:

- **Key ID**
  Enter the ID of the authentication key.
- **Hash Algorithm**Specify the format for the authentication key.
- **Key**Enter the authentication key. The length depends on the hash algorithm.

  - DES: ASCII 8 characters
  - MD5: ASCII 16 – 128 characters
  - SHA1: ASCII 20 – 128 characters
- **Key Confirmation**

  Repeat the authentication key.

### Auto logout

On this page, set the times after which there is an automatic logout from the WBM or the CLI following user inactivity.

If you have been logged out automatically, you will need to log in again.

> **Note**
>
> **No automatic logout from the CLI**
>
> If the connection is not terminated after the set time, check the "Keep alive" setting on the Telnet client.
>
> If the interval for "Keep alive" is shorter than the configured time, the connection is maintained although no user data is transferred. You have set, for example, 300 seconds for the automatic logout and the "keepalive" function is set to 120 seconds. In this case, a packet is sent every 120 seconds that keeps the connection up.
>
> - Disable the keepalive mechanism (interval time = 0)
>
>   or
> - Set the interval high enough so that the underlying connection is terminated when there is inactivity.

#### Description

- **Web Based Management**

  Enter the time in seconds for the automatic logout from WBM. If you enter the value 0, the automatic logout is disabled.
- **CLI (TELNET, SSH)**

  Enter the time in seconds for the automatic logout from the CLI. If you enter the value 0, the automatic logout is disabled.

### Button

#### Functionality SCALANCE S615

The SET button is used for:

- Restart
- Loading new firmware,
- Resetting to factory settings.

You will find a detailed description of the functions in the device operating instructions.

On this page, the functionality of the button can be restricted.

#### Description SCALANCE S615

The following functionality is possible:

- **Restart / Restore Factory Defaults**

  When disabled, the SET button cannot be used for a restart or to restore factory defaults.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Caution** |
  | **Button function "Restart / Restore Factory Defaults" active during startup**  If you have disabled this function in your configuration, disabling is only valid during operation. When restarting, for example after power down, the function is active until the configuration is loaded so that the device can inadvertently be reset to the factory settings. This may cause unwanted disruption in network operation since the device then needs to be reconfigured. An inserted PLUG is also deleted and returned to the status as shipped. |  |

#### Functionality SCALANCE SC63x-2C/SC64x-2C

The SET button is used for:

- Resetting to factory settings,
- Defining the fault mask and the LED display.

You will find a detailed description of the functions in the device operating instructions.

On this page, the functionality of the button can be restricted.

#### Description SCALANCE SC63x-2C/SC64x-2C

The following functionality is possible:

- **Restore Factory Defaults**

  When disabled, the SET button cannot be used to restore factory defaults.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Caution** |
  | **Button function "Restore Factory Defaults" active during startup**  If you have disabled this function in your configuration, disabling is only valid during operation. When restarting, for example after power down, the function is active until the configuration is loaded so that the device can inadvertently be reset to the factory settings. This may cause unwanted disruption in network operation since the device then needs to be reconfigured. An inserted PLUG is also deleted and returned to the status as shipped. |  |
- **Set Fault Mask**

  Enable or disable the function "Define fault mask via the LED display" with the SELECT/SET button.

### Syslog Client

#### System event agent

Syslog according to RFC 3164 is used for transferring short, unencrypted text messages over UDP in the IP network. This requires a Syslog server.

#### Requirements for sending log entries

- The Syslog function is enabled on the device.
- In "System > Events > Configuration", "Syslog" is activated for the relevant event.
- There is a Syslog server in your network that receives the log entries. Since this is a UDP connection, there is no acknowledgment to the sender.
- The IP address or the FQDN (Fully Qualified Domain Name) of the Syslog server is entered in the device.

#### Description

The page contains the following boxes:

- **Syslog Client**

  Enable or disable the Syslog function.
- **Syslog Server Address**

  Enter the IP address or the FQDN (Fully Qualified Domain Name) of the Syslog server.

The table contains the following columns:

- **Syslog Server Address**

  Shows the IP address or the FQDN (Fully Qualified Domain Name) of the Syslog server.
- **Server Port**

  Enter the port of the Syslog server being used.
- **TLS**

  - Enabled

    Syslog messages are sent using TLS encryption over TCP.
  - Disabled

    Syslog messages are sent unencrypted over UDP.

### Ports

This section contains information on the following topics:

- [Overview (SC-600)](#overview-sc-600)
- [Configuration (SC-600)](#configuration-sc-600)

#### Overview (SC-600)

The page shows the configuration for the data transfer for all ports of the device. You cannot configure anything on this page.

##### Description

The table has the following columns:

- **Port**

  Shows the configurable ports. The port is made up of the module number and the port number, for example port 0.1 is module 0, port 1.
- **Port Name**

  Shows the name of the port.
- **Port Type** (only with routing)  
  Shows the type of the port. The following types are possible:

  - Switch Port VLAN Hybrid
  - Switch Port VLAN Trunk
- **Combo Port Media Type** (only available online)

  This column contains a value only with combo ports.

  Shows the mode of the combo port:

  - auto
  - rj45
  - sfp
- **Status**

  Shows whether the port is on or off. Data traffic is possible only over an enabled port.
- **Operational State** (only available online)

  Displays the current operational status. The operational status depends on the configured "Status" and the "Link". The available options are as follows:

  - Up  
    You have configured the status "enabled" for the port and the port has a valid connection to the network.
  - Down  
    You have configured the status "disabled" or "Link down" for the port or the port has no connection.
- **Mode** (only available online)  
  Shows the transfer parameters of the port.
- **MTU (Maximum Transmission Unit)**

  Shows the packet size.
- **Negotiation**

  Shows whether the automatic configuration is enabled or disabled.
- **Flow Ctrl. Type**

  Shows whether flow control is enabled or disabled for the port.
- **Flow Ctrl.**

  Shows whether or not flow control is working on this port.
- **MAC Address** (only available online)

  Shows the MAC address of the port.
- **Blocked by** (only available online)

  Shows why the port is in the "blocked" status:

  - -

    The port is not blocked.
  - Admin down

    The status "disabled" is configured for the port, see "System > Ports > Configuration".
  - Link down

    The status "enabled" is configured for the port but there is no connection, see "System > Ports > Configuration".
  - Power down

    The status “Link down" is configured for the port, see "System > Ports > Configuration".

##### Deviating display of the transmission parameters with combo ports

In the connection status "down", the displayed transmission parameters do not match the actual values of the combo port. In the connection status "up", the correct values are displayed.

**Initial situation**

A pluggable transceiver is plugged into the combo port with the following settings:

- Combo Port Media Type: auto
- Status: enabled
- Link: down

**Display of the transmission parameters**

With 100 Mbps pluggable transceivers

- Actual response: Mode: 100M HD
- Expected response: Mode: 100M FD

With 1 Gbps pluggable transceivers

- Actual response: Mode: 1G HD
- Expected response: Mode: 1G FD

#### Configuration (SC-600)

##### Configuring ports

With this page, you can configure all the ports of the device.

##### Description

- **Port**

  Select the port to be configured from the drop-down list.
- **Status**

  Specify whether the port is enabled or disabled.

  - enabled  
    The port is enabled. Data traffic is possible only over an enabled port.
  - disabled  
    The port is disabled but the connection remains.

    > **Note**
    >
    > Turn off unused ports.
  - Link down  
    The port is disabled and the connection to the partner device is terminated.
- **Port Name**

  Here, enter a name for the port.
- **MAC Address** (only available online)

  Shows the MAC address of the port.
- **Mode Type**

  From this drop-down list, select the transmission speed and the transfer mode of the port. If you set the mode to "Auto negotiation", these parameters are automatically negotiated with the connected end device or network component. This must also be in the "auto negotiation" mode.

  > **Note**
  >
  > Before the port and partner port can communicate with each other, the settings must match at both ends.

  > **Note**
  >
  > **"Mode Type" with combo ports**
  >
  > To be able to set the "Mode Type" of a combo port, change the "Combo Port Media Type" to "rj45". If "auto" is set for the "Combo Port Media Type" and the RJ-45 port is used, you cannot set the "Mode Type".
- **Mode** (only available online)

  Shows the transmission speed and the transmission mode of the port. The following settings are possible:

  - 10 Mbps full duplex (FD) or half duplex (HD)
  - 100 Mbps full duplex (FD) or half duplex (HD)
  - 1000 Mbps (full duplex)
- **Negotiation**

  Shows whether the automatic configuration of the connection to the partner port is enabled or disabled.

  > **Note**
  >
  > **Turning flow control on/off with auto negotiation**
  >
  > Flow control can only be enabled or disabled if the "auto negotiation" function is turned off. The function can be enabled again afterwards.
- **Flow Ctrl. Type**

  Enable or disable flow control for the port.
- **MTU**

  Enter the packet size.
- **Flow Ctrl.**

  Shows whether flow control is working on this port.
- **Port Type**

  Select the type of port from the drop-down list.

  - Switch Port VLAN Hybrid

    The port sends tagged and untagged frames. It is not automatically a member of a VLAN.
  - Switch-Port VLAN Trunk

    The port only sends tagged frames and is automatically a member of all VLANs.
- **Combo Port Media Type**

  Specify the mode of the combo port:

  - auto

    If you select this mode, the pluggable transceiver port has priority.

    As soon as a pluggable transceiver is plugged in, an existing connection at the fixed RJ-45 port is terminated. If no Pluggable transceiver is plugged in, a connection can be established via the fixed RJ-45 port.
  - rj45

    If you select this mode, the fixed RJ-45 port is used regardless of the pluggable transceiver port.

    If a pluggable transceiver is plugged in, it is disabled and the power turned off.
  - sfp

    If you select this mode, the pluggable transceiver port is used regardless of the fixed RJ-45 port.

    If an RJ-45 connection is established, it is terminated because the power of the RJ-45 port is turned off.

  The factory setting for the combo ports is the auto mode.

  > **Note**
  >
  > **Automatic adaptation due to PROFINET configuration**
  >
  > When establishing a PROFINET connection, the setting of the combo port media type is adapted automatically:
  >
  > - If a pluggable transceiver is configured, the combo port media type will be set to "sfp".
  > - If the fixed RJ-45 port is configured, the combo port media type will be set to "rj45".
  >
  > So that the automatic adaptation can be made, the combo port media type must be set to "auto".
  >
  > Configure the combo port media type accordingly using the WBM or CLI.
- **Operational State** (only available online)

  Displays the current operational status. The operational status depends on the configured "Status" and the "Link". The available options are as follows:

  - Up  
    You have configured the status "enabled" for the port and the port has a valid connection to the network.
  - Down  
    You have configured the status "disabled" or "Link down" for the port or the port has no connection.
  - not present  
    With modular devices, this status is displayed when, for example, no media module is inserted.
- **Blocked by** (only available online)
- Shows why the port is in the "blocked" status:

  - -

    The port is not blocked.
  - Admin down

    The status "disabled" is configured for the port, see "System > Ports > Configuration".
  - Link down

    The status "enabled" is configured for the port but there is no connection, see "System > Ports > Configuration".
  - Power down

    The status “Link down" is configured for the port, see "System > Ports > Configuration".

##### Changing the port configuration

Click the appropriate box to change the configuration.

> **Note**
>
> Optical ports always work with the full duplex mode and at maximum transmission speed. As a result, the following settings cannot be made for optical ports:
>
> - Automatic configuration
> - Transmission speed
> - Transmission technique

> **Note**
>
> With various automatic functions, the device prevents or reduces the effect on other ports and priority classes (Class of Service) if a port is overloaded. This can mean that frames are discarded even when flow control is enabled.
>
> Port overload occurs when the device receives more frames than it can send, for example as the result of different transmission speeds.

### Fault Monitoring

This section contains information on the following topics:

- [Power supply](#power-supply)
- [Link Change](#link-change)

#### Power supply

##### Settings for monitoring the power supply

Configure whether or not the power supply should be monitored by the messaging system. With a redundant power supply, configure the monitoring separately for each individual feed-in line.

A fault is then signaled by the message system when there is no power on a monitored connection (supply 1 or supply 2) or when the applied voltage is too low.

> **Note**
>
> You will find the permitted operating voltage limits in the compact operating instructions of the device.

A fault causes the signaling contact to trigger and the fault LED on the device to light up and, depending on the configuration, can trigger a trap or an entry in the event log table.

Select the check box in front of the connection name you want to monitor to enable or disable the monitoring function.

#### Link Change

##### Configuration of fault monitoring of status changes on connections

On this page, you configure whether or not an error message is triggered if there is a status change on a network connection.

If connection monitoring is enabled, an error is signaled

- when there should be a link on a port and this is missing.
- or when there should not be a link on a port and a link is detected.

An error causes the signaling contact to trigger and the fault LED to light up on the device. Depending on the configuration, the error may trigger a trap, an e-mail or an entry in the event log table.

##### Description of the displayed boxes

Table 1 has the following columns:

- **1st column**

  Shows that the settings are valid for all ports.
- **Setting**

  Select the required setting. The available options are as follows:

  - "-" (disabled)
  - Up
  - Down
  - No Change: The setting in table 2 remains unchanged.
- **Transfer to table**

  If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns

- **Port**
    
  Shows the available ports. The port is made up of the module number and the port number, for example port 0.1 is module 0, port 1.
- **Setting**
  Select the setting. You have the following options:

  - Up  
    Error handling is triggered when the port changes to the active status.

    (From "Link down" to "Link up")
  - Down  
    Error handling is triggered when the port changes to the inactive status.

    (From "Link up" to "Link down")
  - "-" (disabled)  
    The error handling is not triggered.

### PLUG

This section contains information on the following topics:

- [Configuration](#configuration-3)
- [License](#license)

#### Configuration

> **Note**
>
> If there is no online connection to the device only the check box "Firmware on PLUG" (see below) is available.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Do not remove or insert a C-PLUG / KEY-PLUG during operation!**  A PLUG may only be removed or inserted when the device is turned off.  The device checks whether or not a PLUG is inserted at one second intervals. If it is detected that the PLUG was removed, there is a restart. If a valid PLUG was inserted in the device, the device changes to a defined error state following the restart.  If the device was configured at some time with a PLUG, the device can no longer be used without this PLUG. To be able to use the device again, reset the device to the factory settings. |  |

##### Information about the configuration of the C-PLUG

This page provides detailed information about the configuration stored on the C-PLUG. It is also possible to reset the PLUG to factory defaults or to load it with new contents.

> **Note**
>
> **Incompatibility with previous versions with PLUG inserted**
>
> During the installation of a previous version, the configuration data can be lost. In this case, the device starts up with the factory settings after the firmware has been installed. In this situation, if a PLUG is inserted in the device, following the restart, this has the status "NOT ACCEPTED" since the PLUG still has the configuration data of the previous more up-to-date firmware. This allows you to return to the previous, more up-to-date firmware without any loss of configuration data.
>
> If the original configuration on the PLUG is no longer required, the PLUG can be deleted or rewritten manually using "System > PLUG".

##### Description

The table has the following rows:

- **Status**
    
  Shows the status of the PLUG. The following are possible:

  - ACCEPTED  
    There is a PLUG with a valid and suitable configuration in the device.
  - NOT ACCEPTED  
    Invalid or incompatible configuration on the inserted PLUG.
  - NOT PRESENT  
    There is no C-PLUG or KEY-PLUG inserted in the device.
  - FACTORY  
    PLUG is inserted and does not contain a configuration. This status is also displayed when the PLUG was formatted during operation.
  - MISSING  
    There is no PLUG inserted. Functions are configured on the device for which a license is required.
- **Device Group**
    
  Shows the SIMATIC NET product line that used the C-PLUG or KEY-PLUG previously.
- **Device Type**
    
  Shows the device type within the product line that used the C-PLUG or KEY-PLUG previously.
- **Configuration Revision**
    
  The version of the configuration structure. This information relates to the configuration options supported by the device and has nothing to do with the concrete hardware configuration. This revision information does not therefore change if you add or remove additional components (modules or extenders), it can, however, change if you update the firmware.
- **File System**
    
  Displays the type of file system on the PLUG.
- **File System Size [bytes]**
    
  Shows the maximum storage capacity of the file system on the C-PLUG.
- **File System Usage**
    
  Displays the storage space in use in the file system of the C-PLUG.
- **Firmware on PLUG**
    
  When enabled, the firmware will be stored on the PLUG. This means that automatic firmware updates/downgrades can be made with the PLUG.
- **Info String**
    
  Shows additional information about the device that used the PLUG previously, for example, article number, type designation, and the versions of the hardware and software. The displayed software version corresponds to the version in which the configuration was last changed. With the "NOT ACCEPTED" status, further information on the cause of the problem is displayed.

  If a PLUG was configured as a PRESET PLUG this is shown here as additional information in the first row.
- **Modify PLUG**
    
  Select the required setting. You have the following options for changing the configuration on the C-PLUG or KEY-PLUG:

  - Write current configuration to PLUG   
    This option is available only if the status of the PLUG is "NOT ACCEPTED" or FACTORY.  
    The configuration in the internal flash memory of the device is copied to the PLUG.
  - Erase PLUG to factory default  
    Deletes all data from the C-PLUG and triggers low-level formatting.

#### License

> **Note**
>
> The page is only available if there is an online connection to the device.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Do not remove or insert a C-PLUG / KEY-PLUG during operation!**  A PLUG may only be removed or inserted when the device is turned off. The device checks whether or not a PLUG is present at one second intervals. If it is detected that the PLUG was removed, there is a restart. If a valid PLUG was inserted in the device, the device changes to a defined error state following the restart.  If the device was configured at some time with a PLUG, the device can no longer be used without this PLUG. To be able to use the device again, reset the device to the factory settings. |  |

> **Note**
>
> **Incompatibility with previous versions with PLUG inserted**
>
> During the installation of a previous version, the configuration data can be lost. In this case, the device starts up with the factory settings after the firmware has been installed. In this situation, if a PLUG is inserted in the device, following the restart, this has the status "NOT ACCEPTED" since the PLUG still has the configuration data of the previous more up-to-date firmware. This allows you to return to the previous, more up-to-date firmware without any loss of configuration data.
>
> If the original configuration on the PLUG is no longer required, the PLUG can be deleted or rewritten manually using "System > PLUG".

##### Information about the license of the KEY-PLUG

A C-PLUG can only store the configuration of a device. In addition to the configuration, a KEY-PLUG also contains a license that enables certain functions of your SIMATIC NET device.

This page provides detailed information about the license on the KEY-PLUG.

##### Description

- **Status**
  Shows the status of the KEY-PLUG. The following are possible:

  - ACCEPTED  
    The KEY-PLUG in the device contains a suitable and valid license.
  - NOT ACCEPTED  
    The license of the inserted KEY-PLUG is not valid.
  - NOT PRESENT  
    No KEY-PLUG is inserted in the device.
  - MISSING  
    There is no KEY-PLUG or a C-PLUG with the status "FACTORY" inserted in the device. Functions are configured on the device for which a license is required.
  - WRONG  
    The inserted KEY-PLUG is not suitable for the device.
  - UNKNOWN  
    Unknown content of the KEY-PLUG.
  - DEFECTIVE  
    The content of the KEY-PLUG contains errors.
- **Article number**
    
  Shows the article number of the KEY-PLUG. The KEY-PLUG is available for various functional enhancements and for various target systems.
- **Serial Number**
    
  Shows the serial number of the KEY-PLUG.
- **Info String**Shows additional information about the device that used the KEY-PLUG previously, for example, article number, type designation, and the versions of the hardware and software. The displayed software version corresponds to the version in which the configuration was last changed. With the "NOT ACCEPTED" status, further information on the cause of the problem is displayed.

  > **Note**
  >
  > When you save the configuration, the information about whether or not a KEY-PLUG was inserted in the device at the time is also saved. This configuration can then only work if a KEY-PLUG with the same article number / license is inserted.

### Port diagnostics

This section contains information on the following topics:

- [SFP diagnostics](#sfp-diagnostics)

#### SFP diagnostics

On this page, you run independent error diagnostics for each individual SFP port. This test is performed without needing to remove the cable, connect a cable tester or install a loopback module at the other end.

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Description

The page contains the following boxes:

- **Port**
    
  Select the required port from the drop-down list.

The values are shown in the following boxes:

- **Name**
    
  Shows the name of the interface.
- **Model**
    
  Shows the type of interface.
- **Revision**
    
  Shows the hardware version of the SFP.
- **Serial**

  Shows the serial number of the SFP.
- **Nominal Bit Rate [Mbps]**

  Shows the nominal bit rate of the interface.
- **Max. Link (50.0/125um) [m]**

  Shows the maximum distance in meters that is possible with this medium.
- **Max. Link (62.5/125um) [m]**

  Shows the maximum distance in meters that is possible with this medium.

The following boxes show the values of the SFP transceiver used in this port:

- **Temperature [°C]**

  Shows the temperature of the interface.
- **Voltage [V]**

  Shows the voltage applied to the interface [V].
- **Current [mA]**

  Shows the current consumption of the interface [mA].
- **Rx Power [μW]/Rx Power [dBm]**

  Shows the receive power of the interface [μW]/[dBm].
- **Tx Power [μW]/Tx Power [dBm]**

  Shows the transmit power of the interface [μW]/[dBm].
- **Range** 
  **Current**

  Shows the current value.
- **Range** 
  **Low**

  Shows the lowest value.
- **Range** 
  **High**

  Shows the highest value.

### DNS

This section contains information on the following topics:

- [DNS client](#dns-client)
- [DNS proxy](#dns-proxy)
- [DNS Record](#dns-record)
- [DDNS client](#ddns-client)

#### DNS client

On this page, you specify whether the device uses the DNS server of the network provider or another DNS server.

The DNS server (Domain Name System) assigns a domain name to an IP address so that a device can be uniquely identified. If this setting is enabled, the device can communicate with a DNS server as a DNS client.

##### Description

The page contains the following boxes:

- **DNS Client**

  Enable or disable depending on whether the device should operate as a DNS client.
- **Used DNS Servers**

  - learned only

    The device uses only the DNS servers assigned by DHCP.
  - manual only

    The device uses only the manually configured DNS servers. The DNS servers must be connected to the Internet. A maximum of two DNS servers can be configured.
  - all

    The device uses all available DNS servers.
- **DNS Server Address**

  Enter the IP address of the DNS server.

The table has the following columns:

- **Select**
    
  Select the check box in the row to be deleted
- **DNS Server Address**

  Shows the IP address of the DNS server.
- **Origin**

  Shows whether the DNS server was configured manually or was assigned by DHCP.

#### DNS proxy

The device provides a DNS server for the local network. If you enter the IP address of the device in the local application as a DNS server, then the device answers the DNS requests from its cache.

If the device does not know the IP address for a domain address, it forwards the query to an external DNS server. How long the device keeps a domain address in the cache depends on the host being addressed. In addition to the IP address, a DNS request to an external DNS server also supplies the life span of this information.

##### Description

The page contains the following boxes:

- **Enable DNS Proxy**

  Enable or disable the proxy of the DNS server.
- **Cache Name Errors (NXDOMAIN)**

  Enable or disable the caching of NXDOMAIN replies. If you enable the option, the domain names that were unknown to the DNS server remain in the cache.

#### DNS Record

On this page, you configure a DNS address directory. To do this, enter the IPv4 address associated with an FQDN.

The device checks if there is an entry for DNS requests and converts the URL into the corresponding IPv4 address.

##### Description

The page contains the following boxes:

- **Enable DNS Records**
    
  When this is enabled, the address directory is used.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Domain**

  Enter the FQDN (Fully Qualified Domain Name).
- **IP Address**

  Enter the corresponding IPv4 address.
- **Comment**

  If needed, enter a comment.

#### DDNS client

The DDNS (Dynamic Domain Name System) is an Internet service that allows a fixed hostname to be set up as a pseudonym for a dynamically changing IP address.

The DDNS client synchronizes the assigned IP address with the hostname registered at the DDNS provider. This means that the device can always be reached using the same hostname.

**Requirement**:

- User name and password that gives you the right to use the DDNS service.
- Registered hostname, e.g. example.no-ip.com
- UDP port 53 for DNS is enabled and is not used for NAT.

##### Description

The table has the following columns:

- **Service**

  Shows which providers are supported.
- **Enabled**

  When enabled, the device logs on to the DDNS server.

- **Host**

  Enter the host name that you have agreed with your DDNS provider for the device, e.g. example.no-ip-com.
- **User Name**

  Enter the user name with which the device logs on to the DDNS server.
- **Password**

  Enter the password assigned to the user.
- **Password Confirmation**

  Confirm the password**.**

### DHCP

This section contains information on the following topics:

- [DHCP client](#dhcp-client)
- [DHCP server](#dhcp-server-1)
- [DHCP options](#dhcp-options)
- [Static Leases](#static-leases)

#### DHCP client

If the device is configured as a DHCP client, it starts a DHCP request. As the reply to the query the device receives an IPv4 address from the DHCP server. The server manages an address range from which it assigns IPv4 addresses. It is also possible to configure the server so that the client always receives the same IPv4 address in response to its request.

##### Description

The page contains the following boxes:

- **Keep Alive**

  When this is enabled, the IP address is retained in the event of a connection breakdown and is not reset to 0.0.0.0. Keep Alive is enabled by default. When Keep Alive is disabled, the IP address is reset to 0.0.0.0 in the event of a communication breakdown.
- **DHCP Client Configuration Request (Opt. 66, 67)**When enabled, the DHCP client uses the options to download the configuration file (option 67) from the TFTP server (option 66). After the restart, the device uses the data from the configuration file.

  > **Note**
  >
  > **Configuration file and firmware version**
  >
  > The configuration file is used to store and read in configuration data within a firmware version, e.g. 4.3. Configuration files created with a firmware version <4.2 cannot be read in to a device with a firmware version 4.3.

  > **Note**
  >
  > If a configuration file is downloaded, this can trigger a system restart. If the currently running configuration and the configuration in the downloaded configuration file differ, the system restarts.
  >
  > Make sure that the option "DHCP Client Configuration Request (Opt. 66, 67)" is no longer set.
- **DHCP Mode**
  Specify the type of identifier with which the DHCP client logs on with its DHCP server.

  - via MAC Address  
    Identification is based on the MAC address.
  - via DHCP Client ID  
    Identification is based on a freely defined DHCP client ID.
  - via System Name  
    Identification is based on the system name. If the system name is 255 characters long, the last character is not used for identification.
  - via Iaid and Duid

    With this the DHCP client can log on with DHCP servers that support parallel operation of IPv4 and IPv6.

    The identification is via the IAID and the DUID and identifies precisely one IP interface of the device.

    IAID (Interface Association Identifier): At least one IAID is generated for each IP interface The IAID remains unchanged when the DHCP client restarts

    DUID (DHCP Unique Identifier): Uniquely identifies server and clients and applies to all IP interfaces of the device. The DUID remains unchanged when there is a restart.

The table has the following columns:

- **Interface**
    
  Interface to which the setting relates.
- **DHCP**
  Enable or disable the DHCP client for the relevant interface.
- **IAID Value**

  Value with which the interface (DHCP client) identifies itself with the DHCP server.

#### DHCP server

You can operate the device as a DHCP server. This allows IP addresses to be assigned automatically to the connected devices. The IP addresses are either distributed dynamically from an address band (pool) you have specified or a specific IP address is assigned to a particular device.

On this page, specify the address band from which the device receives any IP address. You configure the static assignment of the IP addresses in "Static Leases".

> **Note**
>
> **Deleting DHCP server bindings**
>
> If you deactivate or delete an IPv4 address band or turn the DHCP server off and on again, the DHCP server bindings are deleted see "Information > DHCP Server".

The structure of this page depends on how many VLAN IP interfaces the device has.

##### Requirement

The connected devices are configured so that they obtain the IP address from a DHCP server.

##### Devices with one VLAN IP interface

On this page, you specify tIPv4 addresses that are assigned via certain ports.

##### Description

The page contains the following boxes:

- **DHCP Server**

  Enable or disable the DHCP server on the device**.**

  > **Note**
  >
  > To avoid conflicts with IPv4 addresses, only one device may be configured as a DHCP server in the network.
- **Probe address with ICMP echo before offer**

  When selected, the DHCP server checks whether or not the IP address has already been assigned. To do this the DHCP server sends ICMP echo messages (ping) to the IPv4 address. If no reply is received, the IPv4 address is assigned.

  > **Note**
  >
  > This check is not made with static assignments.

  > **Note**
  >
  > If there are devices in your network on which the echo service is disabled as default, there may be conflicts with the IPv4 addresses. To avoid this, assign these devices an IPv4 address outside the IPv4 address band.

The table has the following columns:

- **Pool ID**

  Shows the number of the IPv4 address band. If you click the "Create" button, a new row with a unique number is created (pool ID).
- **Interface**

  Select a VLAN IP interface. The IPv4 addresses are assigned dynamically via this interface. The requirement for the assignment is that the IPv4 address of the interface is located in the subnet of the IPv4 address band. If this is not the case, the interface does not assign any IPv4 addresses.
- **Enable**

  Specify whether or not this IPv4 address band will be used.

  > **Note**
  >
  > If you enable the IPv4 address band, its settings in this and the other DHCP tabs are grayed out and can no longer be edited.
- **Subnet**

  Enter the network address range that will be assigned to the devices. Use the CIDR notation.
- **Lower IP Address**

  Enter the IPv4 address that specifies the start of the dynamic IPv4 address band. The IPv4 address must be within the network address range you configured for "Subnet".
- **Upper IP address**

  Enter the IPv4 address that specifies the end of the dynamic IPv4 address band. The IPv4 address must be within the network address range you configured for "Subnet".
- **Lease Time (sec)**
    
  Specify for how many seconds the assigned IPv4 address remains valid. When half the period of validity has elapsed. the DHCP client can extend the period of the assigned IPv4 address. When the entire time has elapsed, the DHCP client needs to request a new IPv4 address.

##### Devices with several VLAN IP interfaces

On this page, specify the address band from which the connected device receives any IP address. You configure the static assignment of the IP addresses in "Static Leases".

#### DHCP options

On this page you specify which DHCP options the DHCP server supports. The various DHCP options are defined in RFC 2132.

##### Description

The page contains the following boxes:

- **Pool ID**

  Select the required address band.
- **Option Code**

  Enter the number of the required DHCP option.

  > **Note**
  >
  > **DHCP options supported**
  >
  > SCALANCE S615: 1, 2, 3. 4. 5, 6, 42, 66, 67
  >
  > SCALANCE SC-600: 3, 6, 12, 66, 67

  The DHCP options 1, 3, 6, 66 and 67 are created automatically when the IPv4 address band is created. With the exception of option 1, the options can be deleted.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted
- **Pool ID**

  Shows the number of the address band.
- **Option Code**

  Shows the number of the DHCP option.
- **Description**

  Text describing the value of the option.
- **Use Interface IP**

  Specify whether or not the internal IP address of the device will be used.
- **Value**
    
  Enter the DHCP parameter that is transferred to the DHCP client. The content depends on the DHCP option.

  | Value | Option name |  |  |
  | --- | --- | --- | --- |
  | 1 | Subnet Mask | The subnet mask is entered automatically. | Option cannot be deleted. |
  | 2 | Offset time | Offset time to the coordinated universal time UTC. | Enter the offset time in seconds in hexadecimal format. |
  | 3 | Router | The IPv4 address for router in the subnet of the DHCP client. If the device itself is the router, the IPv4 address of the interface is used. | You can specify several IPv4 addresses separated by commas. |
  | 4 | Time server | The IPv4 address of the time server available to the DHCP client. |  |
  | 5 | Name server | The IPv4 address of the name server available to the DHCP client. |  |
  | 6 | DNS Server | The IPv4 address of the DNS server available to the DHCP client.  If the device itself is the DNS server, the IPv4 address of the interface is used. |  |
  | 12 | Host name | Enter the host name in the string format. |  |
  | 42 | NTP Server | The IPv4 address of the NTP server available to the DHCP client. |  |
  | 66 | TFTP server | The IPv4 address or the hostname of the TFTP server available to the DHCP client. | Enter the address of the TFTP server. |
  | 67 | Name of the boot file | The name of the boot file that the client downloads from the TFTP server. | Enter the name of the boot file in the string format. |

#### Static Leases

On this page you specify that certain devices will be assigned a certain IP address. The address assignment is made based on the MAC address, the client ID or the DUID.

##### Description

The page contains the following boxes:

- **Pool ID**

  Select the required address band.
- **Client Identification Method**

  Select the method according to which a client is identified.

  - Ethernet MAC  
    Identification is based on the MAC address. Enter the MAC address in "Value". A MAC address consists of six byes separated by hyphens in hexadecimal notation, e.g. 00-ab-1d-df-b4-1d.
  - Client ID  
    Identification is based on a freely defined DHCP client ID. Enter the required designation in "Value".
  - DUID

    Identification is based on the DUID and IAID. Enter the required designation in "Value", e.g. 00-00-01-C2-00-01-00-01-00-00-00-72-00-1B-1B-B6-32-9D.
- **Value**

  Enter the required value. The entry depends on the selected identification method of the client.

  > **Note**
  >
  > The maximum is 128 entries.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Pool ID**

  Shows the number of the address band.
- **Identification Method**

  Shows the method with which the client identifies itself with the DHCP server.
- **Value**
    
  Shows the MAC address or client ID or DUID of the client.
- **IP Address**

  Specify the IPv4 address that will be assigned to the client. The IPv4 address must be within the address band.
- **Comment**

  Enter a description for the address assignment.

  The maximum is 32 characters.

### cRSP/SRS

> **Note**
>
> Common Remote Service Platform (cRSP) / Siemens Remote Service (SRS) is a remote maintenance platform via which remote maintenance access is possible.
>
> To use the platform, additional service contracts are necessary and certain constraints must be kept to. If you are interested in cRSP / SRS, call your local Siemens contact or visit [Web page](http://www.industry.siemens.com/topics/global/en/service/remote-service/seiten/home.aspx).

On this page, you configure the access data for the SRS / cRSP acc. to URI syntax. The Uniform Resource Identifier (URI) is defined in RFC 3986.

#### Description

The page contains the following boxes:

- **Enable DDNS for cRSP / SRS**

  Enable or disable the use of cRSP / SRS.
- **Update Interval**

  Enter the time interval.
- **Validate Server Certificate**

  When enabled, the device checks the validity of the received server certificate.

The table has the following columns:

- **Index**

  The number of the entry.
- **Select**

  Select the check box in the row to be deleted.
- **Scheme**

  Identifies the access method and the resource type.

  https: Secure access to a Web page.
- **Authority**

  Contains the address of the destination server
- **Path**

  Contains the target path to the resource. The target path can correspond to a directory name or file name.
- **Query**

  A query can contain parameter values for an application.

  - WAN_IP (keyword): Replaces WAN_IP with current external IP address of the device to the destination server.
- **Frag**.

  Addresses local parts of the resource, e.g. the anchor attribute of a Web page.
- **Status** (only available online)

  Shows the status of the last cRSP / SRS access of the entry.
- **Enabled**

  When enabled, this entry is used.

### Proxy Server

On this page, you configure the proxy server that is used by various components, for example SINEMA RC.

#### Description

The page contains the following boxes:

- **Proxy Name**

  Enter a name for the proxy server.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the proxy server.
- **Address**

  Enter the IPv4 address of the proxy server.
- **Type**

  Specify the type of the proxy server.

  - HTTP: Proxy server only for access using HTTP.
  - SOCKS: Universal proxy server
- **Port**

  Enter the port on which the proxy service runs.
- **Auth. Method**

  Specify the authentication method.

  - None  
    No authentication
  - Basic  
    Standard authentication. User name and password are sent unencrypted.
  - NTLM (NT LAN Manager)  
    Authentication according to the NTLM standard (Windows user login)
- **User Name**

  Enter the user name for access to the proxy server.
- **Password**

  Enter the password for access to the proxy server.
- **Password Confirmation**

  Enter the password again to confirm it.

### SINEMA RC

On this page, you configure the access to the SINEMA RC Server.

> **Note**
>
> For SCALANCE S615 this function can only be used with a KEY-PLUG.

#### Description

The page contains the following:

- **Enable SINEMA RC**

  - Enabled:

    A connection to the configured SINEMA RC Server is established. These boxes cannot be edited.
  - Disabled:

    The boxes can be edited. Any existing connection is terminated.

**"**
**Server settings**
**" area**

- **SINEMA RC Address**

  Enter the IPV4 address or the FQDN (Fully Qualified Domain Name) of the SINEMA RC Server.
- **SINEMA RC Port**

  Enter the port via which the SINEMA RC Server can be reached.

**"**
**Server Verification**
**" area**

- **Verification Type**

  - Fingerprint: The identity of the server is verified based on the fingerprint.
  - CA certificate: The identity of the server is verified based on the CA certificate.
- **Fingerprint**

  Only necessary with the setting "Fingerprint". Enter the fingerprint of the device. The fingerprint is assigned during commissioning of the SINEMA RC Server. Based on the fingerprint, the device checks whether the correct SINEMA RC Server is involved. You will find further information on this in the Operating Instructions of the SINEMA RC Server.
- **CA Certificate**

  Only necessary with the setting "CA Certificate". Select the CA certificate of the server used to sign the server certificate. Only loaded CA certificates can be selected.

**"**
**Device Credentials**
**" area**

- **Device ID**

  Enter the device ID. The device ID is assigned when configuring the device on the SINEMA RC Server. You will find further information on this in the Operating Instructions of the SINEMA RC Server.
- **Device Password**

  Enter the password with which the device logs on to the SINEMA RC Server. The password is assigned when configuring the device on the SINEMA RC Server. You will find further information on this in the Operating Instructions of the SINEMA RC Server.
- **Device Password Confirmation**

  Repeat the password to confirm it.

**"**
**Optional Settings**
**" area**

- **Auto Firewall/NAT Rules**

  - Enabled

    The firewall and NAT rules are created automatically for the VPN connection. The connections between the configured exported subnets and the subnets that can be reached via the SINEMA RC Server are allowed. The NAT settings are implemented as configured in the SINEMA RC Server.
  - Disabled

    You will need to create the firewall and NAT rules yourself.
- **Type of connection**

  Specify the type of VPN connection. For more detailed information, refer to the section "VPN connection establishment".

  - Auto

    The device adopts the settings of the SINEMA RC Server. You configure the settings on the SINEMA RC Server in "Remote connections > Devices". You will find further information on this topic in the operating instructions "SINEMA RC Server".
  - Permanent

    The settings of the SINEMA RC Server are ignored. The device establishes a VPN connection to the SINEMA RC Server. The VPN tunnel is established permanently
  - Digital Input

    The settings of the SINEMA RC Server are ignored. If the "Digital In" event occurs, the device attempts to establish a VPN connection to the SINEMA RC Server. This is on condition that the event "Digital Input" is forwarded to the VPN connection. To do this in "System > Events> Configuration" activate "VPN Tunnel" for the "Digital In" event.
- **Use Proxy**

  Specify whether the connection to the defined SINEMA RC Server is established via a proxy server. Only the proxy servers can be selected that you configured in "System > Proxy Server".
- **Autoenrollment Interval [min]**

  Specify the period of time in minutes after which queries are sent to the SINEMA RC Server. With this query, the device checks whether there is a newer firmware file on the SINEMA RC server or whether the configuration data has changed.

  If you enter the value 0, this function is disabled.
- **Timeout [min]** (S615)

  Specify the period of time in minutes. If no data exchange takes place, when this time has elapsed the VPN tunnel is automatically terminated.

### Ping

#### Reachability of an address in an IP network

> **Note**
>
> The page is only available if there is an online connection to the device.

With the ping function, you can check whether a certain address is reachable in the network.

#### Description

The page contains the following boxes:

- **Dest. address**
    
  Enter the IPV4, IPv6 address or the FQDN (Fully Qualified Domain Name) of the device.
- **Repeat**
    
  Enter the number of ping requests.
- **DNS Resolution**

  Select the IP address type in which an entered FQDN will be resolved.

  - Auto  
    In this mode, the IP address type is selected automatically.
  - IPv4  
    The entered FQDN will be resolved in an IPv4 address.
  - IPv6  
    The entered FQDN will be resolved in an IPv6 address.
- **Out Interface for IPv6**

  This selection is only required when the destination address is a multicast or a link local address.

  - "-" (factory setting)
  - Select the relevant IPv6 interface.
- **Ping**
    
  Click this button to start the ping function.
- **Ping Output**
    
  This box shows the output of the ping function.
- **Delete**

  Click this button to delete the ping output.

### DCP Discovery

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Search for devices reachable via the selected interface

On this page, you can select an interface and search for devices that are reachable via the interface and support DCP. DCP Discovery only searches for devices located in the same subnet as the interface. The reachable devices are listed in a table. In the table, you can check and adapt the network parameters of the devices. To identify and configure the devices, the Discovery Configuration Protocol (DCP) is used.

> **Note**
>
> **DCP Discovery**
>
> The function is only available in the VLAN associated with the TIA interface. You can configure the TIA interface under "Layer 3 > Subnets > Configuration".

**Requirement**:

To adapt network parameters, DCP requires write access to the device. If access is write-protected, the network parameters cannot be configured.

On the SCALANCE devices, you configure the access in "System > Configuration".

#### Description

The page contains the following boxes:

- **Timeout**

  Specify the time for flashing. When the time elapses, flashing stops.
- **Blink Own LEDs**

  Makes the LEDs of your own device flash.
- **Interface**

  Select the required interface.
- **Browse**

  Starts the search for devices reachable via the selected interface.

  On completion of the search, the reachable devices are listed in the table. The table is limited to 100 entries.

The table has the following columns:

- **Port**

  Shows the port via which the device can be reached.
- **MAC Address**

  Shows the MAC address of the device.
- **Device Type**

  Shows the product line or product group to which the device belongs.
- **Device Name**

  Adapt the PROFINET device name if necessary.

  The device name must be DNS-compliant. If the device name is not used, the box is empty.
- **IP Address**

  If necessary, adapt the IPv4 address of the device.

  The IPv4 address should be unique within your network and should match the network. The IPv4 address 0.0.0.0 means that no IPv4 address has yet been set.
- **Subnet mask**

  If necessary, adapt the subnet mask of the device.
- **Gateway Address**

  Adapt the IPv4 address of the gateway if necessary.
- **Status Device Name**

  - None: The device name is not used.
  - Discovered: The set device name is used.
  - Configured: The device was assigned a new device name.
- **Status IP address**

  - Discovered/IP: The device uses a static IPv4 address.
  - Discovered/DHCP: The device has obtained the IPv4 address from a DHCP server.
  - Configured: The device was assigned a new IPv4 address.
- **Timeout**

  Specify the time for flashing. When the time elapses, flashing stops.
- **Flash**

  Makes the port LEDs of the selected device flash.

### Configuration Backup (S615)

> **Note**
>
> The page is only available if there is an online connection to the device.

#### Configuration Package Backup

On this page, you can save backups of your configuration. Depending on the available memory and the file size of the backup, you can create multiple backups.

The created backups are saved under the "ConfigPackBackup" file type. On the "System > Load&Save > HTTP/TFTP" page you can save configuration backups as ZIP file on your client PC or load them from there.

#### Description

The page contains the following boxes:

- **Name**

  Enter a name for the backup.

The table contains the following columns:

- **Select**

  Select the row you want to delete.
- **Name**

  Shows the name of the backup.
- **Size [bytes]**

  The first row "Available memory" shows how much memory is available for backups on the device. When you create a backup, the available memory space is reduced accordingly. The other rows show the size of each backup.
- **Restore**

  Click the "Restore" button to load the relevant backup on the device.

### Connection Check (S615)

On this page, you activate a ping test that monitors connections. During the ping test, the device sends ICMP echo request packets (pings) to the configured destination address at regular intervals. If this destination address does not respond, the device tries to reach the destination address again. If all ping attempts (retries) are unsuccessful, the ping test is considered to have failed or the group is considered unreachable. If the group is not reachable, the device initiates the configured action on the selected interface. If all 5 actions have been executed or after a restart, the device starts again with the first action.

#### Description

- **Enable Connection Check**

  Enable or disable the ping test for connection monitoring.

The "Group" table contains the following columns:

- **Group Identifier**

  Index of the group.
- **Name**

  Specify a name for the group. The entry is displayed in the "Action" table as column name.
- **Source Interface**

  Specify the interface via which reachability of the destination addresses is monitored.
- **Interval**

  Specify the interval at which the ping tests take place.
- **TTL (Time to live)**

  Specify the TTL value.
- **Retries**

  Specify how often the ping attempt is repeated.

  The time interval between the ping attempts is 100 ms. With a large number of ping attempts, this can result in a time delay.

  If none of the configured addresses responds, the ping test is considered to have failed (error). In the "Action" table, you define whether a specific action is executed.
- **1st - 3rd Ping Target**

  Specify the destination address that is used as reference for the reachability.

The "Group" table contains the following columns:

- **Group 1 - 5**

  If a name if configured, it is used as column name. Assign the groups to the desired interface. The interface is considered reachable when all assigned groups are reachable. If only one of the groups is not reachable, the configured action is executed on the selected interface.
- **Action for**

  Indicates the interface on which the action is executed.
- **1st Action - 5th Action**

  The following actions are possible:

  - None (default)
  - Restart

    Restart the device. After the restart, the device waits for 10 minutes and then sends a ping to the first destination address.

### TCP event

If you enable the "TCP Event" function on the page, the device waits for incoming TCP packets on the configured port. Authorization is performed by comparing the user data.

You have the following options with TCP packets:

- Trigger the "Sleep Mode" function.
- Switch the digital output on or off.

If the incoming TCP packet contains comformant data, the command contained in it is executed.

**Format of the TCP packet**

The command is sent in a TCP packet that conforms to the following format:

`User name`
`#`
`Password`
`#CommandCode#Seq-Num;Time;`

> **Note**
>
> **Permitted characters for user name and password**
>
> The following characters are permitted:
>
> - 0123456789
> - A...Z a...z
> - . -_
>
> Additionally allowed in the password:
>
> - Space
> - ! " % & / ( ) = ? * + < > ' ,

#### Description

The page contains the following:

- **Enable**

  Enable or disable reception of the TCP packets. To log this, activate the "TCP Event Log" event under "System > Event".
- **User Name**

  Enter the user name to check the reception of the TCP packet. The user name and password are entered in the TCP packet.
- **Password**

  Enter the password belonging to the user name.
- **Password Confirmation**

  Repeat the password to confirm it.
- **Port number**

  Define the port at which the device waits for the TCP packets. Standard port 26864 is the default.

  Optionally, you can enter the default port 26864 or a port number in the 1 … 65535 range.

  > **Note**
  >
  > **Reserved ports**
  >
  > Some ports are permanently reserved. Make sure that the specified port is not already in use. You can find the ports used in the "List of available services".

The table contains the following columns:

- **Enable**

  Enable or disable the event.
- **Event**

  - Digital output

    Switch the digital output on or off. The digital output is reset on restart (switched off).

    Power on:

    `User name`
    `#`
    `Password`
    `#106#1`:

    Power off:

    `User name`
    `#`
    `Password`
    `#106#2`:
  - Sleep Mode

    Trigger the "Sleep Mode" function:

    `User name`
    `#`
    `Password`
    `#107#1;10:`

    The last number specifies the sleep time in minutes. In this example, sleep mode is triggered for 10 minutes.

## Configuring interfaces

This section contains information on the following topics:

- [Ethernet](#ethernet)
- [PPP](#ppp)

### Ethernet

This section contains information on the following topics:

- [Overview (S615)](#overview-s615)
- [Configuration (S615)](#configuration-s615)

#### Overview (S615)

The page shows the configuration for the data transfer for all ports of the device. You cannot configure anything on this page.

##### Description

The table has the following columns:

- **Port**

  Shows the configurable ports. The entry is a link. If you click on the link, the corresponding configuration page is opened.
- **Port name**

  Shows the name of the port.
- **Port Type** (only with routing)

  Shows the type of the port. The following types are possible:

  - Switch port VLAN hybrid
  - Switch port VLAN trunk
- **Status**

  Shows whether the port is on or off. Data traffic is possible only over an enabled port.
- **Operational State** (only available online)

  Displays the current operational status. The operating status depends on the configured "Status" and the "Link".

  The available options are as follows:

  - up

    You have configured the status "enabled" for the port and the port has a valid connection to the network.
  - down

    You have configured the status "disabled" or "Link down" for the port or the port has no connection.
- **Link** (only available online)

  Shows the connection status to the network. With the connection status, the following is possible:

  - up  
    The port has a valid connection to the network, a "Link Integrity Signal" signal is being received.
  - down  
    The link is down, for example because the connected device is turned off.
- **Mode** (only available online)

  Shows the transmission parameters of the port.
- **Negotiation**

  Shows whether the automatic configuration is enabled or disabled.
- **MAC Address** (only available online)

  Shows the MAC address of the port.

#### Configuration (S615)

On this page, you configure the Ethernet ports of the device.

##### Description

The page contains the following:

- **Port**

  Select the port to be configured.
- **Status**

  Specify whether the port is enabled or disabled.

  - enabled

    The port is enabled. Data traffic is possible only over an enabled port.
  - disabled

    The port is disabled but the connection remains.

    > **Note**
    >
    > Turn off unused ports.
  - Link down

    The port is disabled and the connection to the partner device is terminated.
- **Port name**

  Enter a name for the port.
- **MAC Address** (only available online)

  Shows the MAC address of the port.
- **Mode Type**

  Shows the transmission speed and the transmission mode of the port.

  The following settings are possible:

  - 10 Mbps full duplex (FD) or half duplex (HD)
  - 100 Mbps full duplex (FD) or half duplex (HD)
  - Auto negotiation

  If you set the mode to "Auto negotiation", these parameters are automatically negotiated with the connected end device or network component. This must also be in the "Auto negotiation" mode.

  > **Note**
  >
  > Before the port and partner port can communicate with each other, the settings must match at both ends.
- **Mode** (only available online)

  Shows the transmission speed and the transmission mode of the port. The display depends on the set "Mode Type".
- **Negotiation**

  Shows whether the automatic configuration of the connection to the partner port is enabled or disabled.
- **Port Type** (only with routing)

  Select the type of the port:

  - Switch-Port VLAN Hybrid

    The port sends tagged and untagged frames. It is not automatically a member of a VLAN.
  - Switch-Port VLAN Trunk

    The port only sends tagged frames and is automatically a member of all VLANs.
- **Operational State** (only available online)

  Displays the current operational status. The operating status depends on the configured "Status" and the "Link".

  The available options are as follows:

  - up

    You have configured the status "enabled" for the port and the port has a valid connection to the network.
  - down

    You have configured the status "disabled" or "Link down" for the port or the port has no connection.
- **Link** (only available online)

  Shows the connection status to the network. With the connection status, the following is possible:

  - Up  
    The port has a valid link to the network, a link integrity signal is being received.
  - Down  
    The link is down, for example because the connected device is turned off.

### PPP

This section contains information on the following topics:

- [Overview](#overview-3)
- [Configuration](#configuration-4)

#### Overview

The page shows the status of the PPP connection.

##### Description

This table contains the following columns:

- **Interface**

  Shows the PPP interface. The entry is a link. If you click on the link, the corresponding configuration page is opened.
- **Name**

  Shows the name of the PPP interface.
- **Type**

  Shows the protocol of the PPP connection.
- **Operation**

  Shows whether the PPP connection is activated or deactivated.
- **Status**

  Shows the status of the PPP connection.

  - Ready

    The PPP connection can be configured and enabled.
  - connecting

    The PPP connection is configured, enabled and the connection is being established.
  - Connected

    The PPP connection is established.
  - Error

    Error status in which operator intervention is required, e.g. wrong password.
  - Stopped

    Error message of the server, e.g. incorrect login data. There is a wait time before login is attempted again.

#### Configuration

On this page, you configure the PPP connection. The point-to-point protocol (PPP) allows the connection of an external ADSL modem to an Ethernet interface and via this then a connection to the Internet. The interface is also called PPP interface.

The device acts as a router and logs in with the user name and password. All connected devices can use the PPP connection.

##### Description

The page contains the following:

- **Interface**

  Select the PPP interface to be configured.
- **Name**

  Shows the name of the PPP interface. You can change the name in "Layer 3 > Subnets".
- **Type**

  Specify the protocol for the PPP connection.

  - PPPoE (Point-to-Point over Ethernet)

    The PPP data is encapsulated in an Ethernet frame.
- **Operation**

  Specify whether the PPP connection is activated or deactivated.
- **L2 Interface**

  Specify the interface via which the PPP connection is established. Only VLANs with configured subnet can be selected.
- **User Name**

  Enter the user name. You will receive the user name from the DSL provider.
- **Password**

  Enter the password. You will receive the password from the DSL provider.
- **Password Confirmation**

  Repeat the password.
- **Forced Disconnect**

  After a certain time, the DSL provider terminates the connection. Enable this option if you want to shift the forced disconnect of your provider to a specific time of day, for example at night outside normal office hours.
- **Time for Forced Disconnect**

  Specify the time of day to which you want to shift the forced disconnect of the DSL provider. This is only possible if the correct system time is set on the device.

  Input format: HH:MM

## Configuring layer 2 functions

This section contains information on the following topics:

- [Configuration (SC-600)](#configuration-sc-600-1)
- [Configuration (S615)](#configuration-s615-1)
- [VLAN](#vlan-2)
- [VXLAN](#vxlan)
- [Dynamic MAC aging](#dynamic-mac-aging)
- [Ring redundancy](#ring-redundancy-1)
- [Spanning Tree](#spanning-tree-1)
- [LLDP](#lldp-1)
- [Fiber Monitoring Protocol (SC600)](#fiber-monitoring-protocol-sc600)
- [Unicast (SC-600)](#unicast-sc-600)
- [Multicast (SC-600)](#multicast-sc-600)
- [Inter-VLAN Bridge (SC-600)](#inter-vlan-bridge-sc-600)

### Configuration (SC-600)

#### Configuring layer 2

On this page, you create a basic configuration for the functions of layer 2.

#### Description

**Dynamic MAC Aging**
Enable or disable the "Aging" mechanism. You can configure other settings under "Layer 2 > Dynamic MAC Aging".

**Redundancy Type**
  
The following settings are available:

- **"-" (disabled)**The redundancy function is disabled.
- **Ring**

  If you select this option, you specify the required redundancy mode in the "Redundancy Mode" drop-down list.
- **Spanning Tree**

  If you select this option, you specify the required redundancy mode in the "Redundancy Mode" drop-down list.

**Redundancy Mode**

If you select "Ring" in the "Redundancy Type" drop-down list, the following options are then available:

- **MRP-Client**The device adopts the role of MRP client.
- **HRP-Client**The device adopts the role of HRP client.

If you select "Spanning Tree" in the "Redundancy Type" drop-down list, the following options are then available:

- **STP**Enabled Spanning Tree Protocol. Typical reconfiguration times with Spanning Tree are between 20 and 30 seconds. You can configure other settings in "Layer 2 > Spanning Tree".
- **RSTP**Enabled Rapid Spanning Tree Protocol (RSTP). If a Spanning Tree frame is detected at a port, this port reverts from RSTP to Spanning Tree. You can configure other settings in "Layer 2 > Spanning Tree".

  > **Note**
  >
  > When using RSTP (Rapid Spanning Tree Protocol), loops involving duplication of frames or frames being overtaken may occur briefly. If this is not acceptable in your particular application, use the slower standard Spanning Tree mechanism.

**Passive Listening**

Enable or disable the Passive Listening function.

### Configuration (S615)

#### Configuring layer 2

On this page, you configure passive listening.

#### Description

- **Passive Listening**

  When enabled the function ensures that the BPDUs from the RSTP network are forwarded transparently and return again. If this was not the case, loops would form at the connection point between RSTP and the ring.

### VLAN

This section contains information on the following topics:

- [General (SC-600)](#general-sc-600)
- [General (S615)](#general-s615)
- [Port-based VLAN](#port-based-vlan)

#### General (SC-600)

On this page, you can define VLANs and specify the use of the ports. The device takes VLAN information into account (IEEE 802.1Q/VLAN-aware mode). If the device is in the "802.1Q VLAN Bridge" mode, you can define VLANs and specify the use of the ports .

> **Note**
>
> **Changing the agent VLAN ID**
>
> If the configuration PC is connected directly to the device via Ethernet and you change the agent VLAN ID, the device is no longer reachable via Ethernet following the change.

##### Description

The page contains the following boxes:

- **Base Bridge-**
  **Mode**
    
  Select the required mode. The following modes are possible:

  - 802.1 Q VLAN Bridge  
    Sets the mode "VLAN-aware" on the device. In this mode, VLAN information is taken into account.
- **VLAN ID**

  Enter the VLAN-ID (a number between 1 and 4094).

The table has the following columns:

- **VLAN ID**

  Shows the VLAN ID. The VLAN ID (a number between 1 and 4094) can only be assigned once when creating a new data record and can then no longer be changed. To make a change, the entire data record must be deleted and created again.
- **Name**

  Enter a name for the VLAN. The name only provides information and has no effect on the configuration. The length is a maximum of 32 characters.
- **Status**

  Shows the status type of the entry in the internal port filter table. Here, "Static" means that the VLAN was entered statically by the user.
- **List of ports**

  Specify the use of the port. The following options are available:

  - "-"
  - The port is not a member of the specified VLAN.

    With a new definition, all ports have the identifier "-".
  - M

    The port is a member of the VLAN. Frames sent in this VLAN are forwarded with the corresponding VLAN tag.
  - R

    The port is a member of the VLAN. A GVRP frame is used for the registration.
  - U (upper case)

    The port is an untagged member of the VLAN. Frames sent in this VLAN are forwarded without the VLAN tag. Frames without a VLAN tag are sent from this port.
  - u (lower case)

    The port is an untagged member of the VLAN, but the VLAN is not configured as a port VLAN. Frames sent in this VLAN are forwarded without the VLAN tag.
  - F

    The port is not a member of the specified VLAN and cannot become a member of this VLAN even if it is configured as a trunk port.
  - T

    This option is only displayed and cannot be selected.

    This port is a trunk port making it a member in all VLANs.

##### 802.1Q VLAN Bridge: Important rules for VLANs

Make sure you keep to the following rules when configuring and operating your VLANs:

- Frames with the VLAN ID "0" are handled as untagged frames but retain their priority value.
- As default, all ports on the device send frames without a VLAN tag to ensure that the end node can receive these frames.
- If an end node is connected to a port, outgoing frames should be sent without a tag (static access port). If, however, there is a further switch at this port, the frame should have a tag added (trunk port).

#### General (S615)

On this page you specify whether or not the device forwards frames with VLAN tags transparently (IEEE 802.1D/VLAN-unaware mode) or takes VLAN information into account (IEEE 802.1Q/VLAN-aware mode). If the device is in the "802.1Q VLAN Bridge" mode, you can define VLANs and specify the use of the ports .

> **Note**
>
> **Changing the agent VLAN ID**
>
> If the configuration PC is connected directly to the device via Ethernet and you change the agent VLAN ID, the device is no longer reachable via Ethernet following the change.

##### Description

The page contains the following boxes:

- **Base Bridge Mode**
    
  Select the required mode. The following modes are possible:

  > **Note**
  >
  > **Changing Base Bridge Mode**
  >
  > Note the section "Changing Base bridge mode". This section describes how a change affects the existing configuration.

  - 802.1 D Transparent Bridge  
    Sets the mode "VLAN-unaware" for the device. In this mode, VLAN tags are not changed but are forwarded transparently. The VLAN priority is evaluated for CoS. In this mode, you cannot create any VLANs. Only a management VLAN is available: VLAN 1.
  - 802.1 Q VLAN Bridge  
    Sets the mode "VLAN-aware" on the device. In this mode, VLAN information is taken into account.
- **VLAN ID**

  Enter the VLAN ID.

  Range of values: 1 ... 4094

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **VLAN ID**

  Shows the VLAN ID. The VLAN ID (a number between 1 and 4094) can only be assigned once when creating a new data record and can then no longer be changed. To make a change, the entire data record must be deleted and created again.
- **Name**

  Enter a name for the VLAN. The name only provides information and has no effect on the configuration. The length is a maximum of 32 characters.
- **Status**

  Shows the status type of the entry in the internal port filter table. Here, "Static" means that the VLAN was entered statically by the user.
- **List of ports**

  Specify the use of the port. The following options are available:

  - "-"

    The port is not a member of the specified VLAN.

    With a new definition, all ports have the identifier "-".
  - M

    The port is a member of the VLAN. Frames sent in this VLAN are forwarded with the corresponding VLAN tag.
  - U (upper case)

    The port is an untagged member of the VLAN. Frames sent in this VLAN are forwarded without the VLAN tag. Frames without a VLAN tag are sent from this port.
  - u (lower case)

    The port is an untagged member of the VLAN, but the VLAN is not configured as a port VLAN. Frames sent in this VLAN are forwarded without the VLAN tag.
  - F

    The port is not a member of the specified VLAN and cannot become a member of this VLAN, even if it is configured as a trunk port.
  - T  
    This option is only displayed and cannot be selected in the WBM.   
    This port is a trunk port, making it a member in all VLANs.  
    You configure this function in the CLI (Command Line Interface) using the "`switchport mode trunk`" command or in the WBM under "Interfaces > Ethernet > Configuration".

##### Changing Base bridge mode

**VLAN-unaware (802.1D transparent bridge) → VLAN-aware (802.1Q VLAN bridge)**

If you change the Base Bridge Mode from VLAN-unaware to VLAN aware, this has the following effects:

- All static and dynamic unicast entries are deleted.

**VLAN-aware (802.1Q VLAN bridge) → VLAN-unaware (802.1D transparent bridge)**

If you change the Base Bridge Mode from VLAN-aware to VLAN-unaware, this has the following effects:

- All VLAN configurations are deleted.
- A management VLAN is created: VLAN 1.
- All static and dynamic unicast entries are deleted.

##### 802.1Q VLAN Bridge: Important rules for VLANs

Make sure you keep to the following rules when configuring and operating your VLANs:

- Frames with the VLAN ID "0" are handled as untagged frames but retain their priority value.
- As default, all ports on the device send frames without a VLAN tag to ensure that the end node can receive these frames.
- You can find the factory assignment of the ports in the section "VLAN".
- The VLANs are in different IP subnets. To allow these to communicate with each other, the route and firewall rule must be configured on the device.
- If an end node is connected to a port, outgoing frames should be sent without a tag (static access port). If there is a further switch at this port, the frame should have a tag added (trunk port).

#### Port-based VLAN

##### Processing received frames

On this page, you specify the configuration of the port properties for receiving frames.

##### Description of the displayed boxes

Table 1 has the following columns:

- **All ports**

  Shows that the settings are valid for all ports of table 2.
- **Priority**
   **/**
   **Port VID**
   **/** 
  **Acceptable Frames**
   **/** 
  **Ingress Filtering**

  In the drop-down list, select the setting for all ports. If "No Change" is selected, the entries of the corresponding column in table 2 remain unchanged.
- **Transfer to table**

  If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**

  Shows the available ports and link aggregations. The port is made up of the module number and the port number, for example port 0.1 is module 0, port 1.
- **Priority**

  Select the priority assigned to untagged frames.

  The CoS priority (Class of Service) used in the VLAN tag. If a frame is received without a tag, it will be assigned this priority. This priority specifies how the frame is further processed compared with other frames. There are a total of eight priorities with values 0 to 7, where 7 represents the highest priority (IEEE 802.1p Port Priority).
- **Port VID**

  Select the VLAN ID. Only VLAN IDs defined on the "VLAN > General" page can be selected.  
  If a received frame does not have a VLAN tag, it has a tag with the VLAN ID specified here added to it and is sent according to the rules at the port.
- **Acceptable Frames**

  Specify which types of frames will be accepted. The following alternatives are possible:

  - Tagged Frames Only  
    The device discards all untagged frames. Frames tagged with "0" are treated like untagged frames. The device forwards all tagged frames. Otherwise, the forwarding rules apply according to the configuration.
  - All  
    The device forwards all frames
- **Ingress Filtering**

  Specify whether the VID of received frames is evaluated. The following options are available:

  - Enabled  
    The VLAN ID of received frames decides whether they are forwarded: To forward a VLAN tagged frame, the receiving port must be a member in the same VLAN. Frames from unknown VLANs are discarded at the receiving port.
  - Disabled  
    All frames are forwarded.

### VXLAN

This section contains information on the following topics:

- [VXLAN](#vxlan-1)
- [VTEP](#vtep)
- [Ingress Replication](#ingress-replication)
- [Static MAC](#static-mac)
- [VLAN assignment](#vlan-assignment)

#### VXLAN

On this page, you define VXLANs (Virtual eXtensible LAN). VXLAN is a virtual network technology for extending VLAN and allows the transmission of Layer 2 packets via Layer 3 networks.

The maximum size of a packet (MTU) for VXLAN is 1500 bytes. Larger packets are fragmented.

##### Description

The page contains the following boxes:

- **VXLAN**

  Enables the VXLAN function.
- **UDP port**

  If necessary, change the UDP default port 4789 for VXLAN.

  Range of values: 1000 ... 65535
- **Network Virtual Endpoint Interface (NVE)**

  In this area, you configure the virtual interface via which the VXLAN tunnel is established.

  - **NVE ID**

    Enter a number for the NVE interface.

    Range of values: 1 ... 65535
- The table contains the following columns.

  - **Select**

    Select the row you want to delete.
  - **NVE Interface**

    Shows the NVE interface. The label is automatically composed of "nve" and the entered number.

#### VTEP

On this page, you make settings relating to the source VTEP (VXLAN Tunnel End Point). The VTEPS form the endpoints of the VXLAN tunnel. The source VTEP encapsulates the Ethernet frame and its tunnel end partner (remote VTEP) decapsulates it again.

##### Description

The page contains the following boxes:

- **NVE Interface**

  Select the required NVE interface. Only the interfaces that you created in the "VXLAN" tab can be selected.

  The source VTEP can have multiple NVE interfaces.
- **VTEP Source IP Address**

  Enter the IPv4 address of the source VTEP. The requirement is that the IPv4 address is created on the device. You configure the IPv4 address under "Layer3 > Subnets".

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **NVE Interface**

  Shows the NVE interface.
- **VTEP Source IP Address**

  Shows the IPv4 address of the source VTEP.

#### Ingress Replication

If there are multiple VTEPs in a VNI segment, the source VTEP does not know which remote VTEP the receiver of the Ethernet frame is behind.

On this page, you configure the remote VTEPs that should contain the Ethernet frame. The source VTEP replicates the received Ethernet frame and sends the encapsulated Ethernet frame to the remote VTEPs.

##### Description

The page contains the following boxes:

- **NVE Interface**

  Select the required NVE interface.
- **VNI ID**

  Enter the required VNI. Only VXLAN networks with the same VNI ID can communicate with one another.

  Range of values: 1 ... 16777215

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **NVE Interface**

  Shows the selected NVE interface.
- **VNI ID**

  Shows the VNI ID.
- **Remote VTEP IP Address**

  Enter the IPv4 address of the remote VTEP.

  The replicated Ethernet frame is encapsulated and sent to this remote VTEP. The prerequisite is that the remote VTEP is a member of the VNI segment.

#### Static MAC

On this page, you specify the NVE interface via which remote VTEPs can be reached. The entry is displayed under "Information > VXLAN".

##### Description

The page contains the following boxes:

- **NVE Interface**

  Select the NVE interface via which the remote VTRP can be reached. Only the interfaces that you created in the "VXLAN" tab can be selected.
- **VNI ID**

  Enter the VNI ID (VXLAN Network Identifier). Only VTEPs that are members of the same VXLAN segment can communicate with one another.
- **Remote MAC Address**

  Enter the MAC address of the remote VTEP.

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **NVE Interface**

  Shows the NVE interface.
- **Remote MAC Address**

  Shows the MAC address of the remote VTEP.
- **Remote VTEP IP Address**

  Enter the IPv4 address of the remote VTEP**.**

#### VLAN assignment

To ensure that the VTEP forwards the Ethernet frame into the right VLAN or VXLAN, an assignment of VLAN ID to VNI is configured.

##### Description

The page contains the following boxes:

- **VLAN ID**

  Select the required VLAN ID. Only VLANs with a configured subnet can be selected.
- **VNI ID**

  Enter the VNI ID that will be assigned to the VLAN ID. The VNI ID can be assigned to multiple VLAN IDs.

The table has the following columns:

- **Select**

  Select the row you want to delete.
- **VLAN ID**

  Shows the VLAN ID.
- **VNI**

  Shows the VNI assigned to the VLAN.
- **Tag**

  Ethernet frame contains a VLAN tag.

### Dynamic MAC aging

The device automatically learns the source addresses of the connected nodes. This information is used to forward data frames to the nodes specifically involved. This reduces the network load for the other nodes. If a device does not receive a frame whose source address matches a learned address within a certain time, it deletes the learned address. This mechanism is known as "Aging". Aging prevents frames being forwarded incorrectly, for example when an end device is connected to a different port. If the check box is not enabled, a device does not delete learned addresses automatically.

#### Description

- **Dynamic MAC Aging**

  Enable or disable the function for automatic aging of learned MAC addresses.
- **Aging Time[s]**
    
  Enter the time in seconds in steps of 15. After this time, a learned address is deleted if the device does not receive any further frames from this sender address.

  Range of values: 15 - 630 seconds

  > **Note**
  >
  > **Rounding of the values, deviation from desired value**
  >
  > When you input the Aging Time, note that it is rounded to correct values. If you enter a value that cannot be divided by 15, the value is automatically rounded down.

### Ring redundancy

This section contains information on the following topics:

- [Ring](#ring)

#### Ring

##### Rules for ring redundancy

**Factory settings**

- The factory setting defines ports P0.1 and P0.2 as ring ports.

##### Configuration of ring redundancy

- **Ring Redundancy**
  If you enable the "Ring Redundancy" check box, you turn ring redundancy on. The Ring Ports set on this page are used.
- **Ring redundancy mode**

  Here, you set the mode of the ring redundancy.

  The following modes are available:

  - MRP Client

    The device adopts the role of MRP client.
  - HRP Client

    The device adopts the role of HRP client.
- **Ring ports**

  Here, you set the ports to be used as ring ports in ring redundancy.

##### Restoring factory settings

If the factory settings are restored (Reset to Factory Defaults), ring redundancy is disabled and the default ports are used as the ring ports. This can lead to circulating frames and failure of the data traffic if other settings were used in a previous configuration.

### Spanning Tree

This section contains information on the following topics:

- [General (S615)](#general-s615-1)
- [General (SC-600)](#general-sc-600-1)
- [ST general](#st-general)
- [ST Port](#st-port)

#### General (S615)

##### Description

The page contains the following boxes:

- **Spanning Tree**
  Enable or disable spanning tree.
- **Protocol Compatibility**

  The following setting is available:

  - RSTP

#### General (SC-600)

##### Description

On this page, you can enable Spanning Tree and select the protocol compatibility:

- **Spanning Tree**
  Enable or disable spanning tree.

  > **Note**
  >
  > **No operation of Spanning Tree with enabled ring redundancy**
  >
  > If ring redundancy is enabled under "Layer 2", Spanning Tree cannot be used.
- **Protocol Compatibility**

  The following setting is available:

  - RSTP
  - STP

#### ST general

The page consists of the following parts:

- The left-hand side of the page shows the configuration of the device.
- The right-hand part shows the configuration of the root bridge that can be derived from the Spanning Tree frames received by a device.

##### Description

The page contains the following boxes:

- **Bridge Priority**
   **/** 
  **Root Priority** (only available online)  
  Which device becomes the root bridge is decided by the bridge priority. The bridge with the highest priority (in other words, with the lowest value for this parameter) becomes the root bridge. If several devices in a network have the same priority, the device whose MAC address has the lowest numeric value will become the root bridge. Both parameters, bridge priority and MAC address together form the bridge identifier. Since the root bridge manages all path changes, it should be located as centrally as possible due to the delay of the frames.

  The value for the bridge priority is a whole multiple of 4096 with a range of values from: 0 - 61440
- **Bridge Address** (only available online)**/** **Root Address**  (only available online)The bridge address shows the MAC address of the device and the root address shows the MAC address of the root bridge.
- **Root Port**  (only available online)Shows the port via which the switch communicates with the root bridge.
- **Root Cost** (only available online)The path costs from this device to the root bridge.
- **Topology Changes** (only available online) **/** **Last Topology Change** (only available online)The entry for the device shows the number of reconfigurations due to the spanning tree mechanism since the last startup. For the root bridge, the time since the last reconfiguration is displayed as follows:

  - Seconds: Supplement "sec" after the number
  - Minutes: Supplement "min" after the number
  - Hours: Supplement "hr" after the number
- **Bridge hello time [s]**
   **/** 
  **Root hello time [s]**  (only available online)Each bridge sends configuration frames (BPDUs) regularly. The interval between two configuration frames is the "Hello Time".

  Factory setting: 2 seconds
- **Bridge Forward Delay[s]**
   **/** 
  **Root Forward Delay[s]** (only available online)New configuration data is not used immediately by a bridge but only after the period specified in the "Forward Delay" parameter. This ensures that operation is only started with the new topology after all the bridges have the required information.

  Factory setting: 15 seconds
- **Bridge Max Age[s]**
   **/** 
  **Root Max Age[s]**  (only available online)

  If the BPDU is older than the specified "Max Age" it is discarded.

  Factory setting: 20 seconds
- **Reset Counter** (only available online)

  Click this button to reset the counters on this page.

#### ST Port

When the page is called, the table displays the current status of the configuration of the port parameters.

To configure them, click the relevant cells in the port table.

##### Description

Table 1 has the following columns:

- **All ports**

  Shows that the settings are valid for all ports of table 2.
- **Spanning Tree Status**

  In the drop-down list, select the setting for all ports. If "No Change" is selected, the entries of the corresponding column in table 2 remain unchanged.
- **Copy to Table**

  If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**Shows the available ports.
- **Spanning Tree Status**
    
  Specify whether or not the port is integrated in the spanning tree.

  > **Note**
  >
  > If you disable the "Spanning Tree Status" option for a port, this may cause the formation of loops. The topology must be kept in mind.
- **Priority**Enter the priority of the port. The priority is only evaluated when the path costs are the same.  
  The value must be divisible by 16. If the value that cannot be divided by 16, the value is automatically adapted.  
  Range of values: 0 - 240.   
  The default is 128.
- **Cost Calc.**Enter the path cost calculation. If you enter the value "0" here, the automatically calculated value is displayed in the "Path costs" box.
- **Path Cost**  (only available online)This parameter is used to calculate the path that will be selected. The path with the lowest value is selected as the path. If several ports of a device have the same value for the path costs, the port with the lowest port number is selected.  
  If the value in the box "Cost Calc." is "0", the automatically calculated value is shown. Otherwise, the value of the "Cost Calc." box is displayed.  
  The calculation of the path costs is largely based on the transmission speed. The higher the achievable transmission speed is, the lower the value of the path costs.

  Typical values for path costs with rapid spanning tree:

  - 10,000 Mbps = 2,000
  - 1000 Mbps = 20,000
  - 100 Mbps = 200,000
  - 10 Mbps = 2,000,000

  The values can, however, also be set individually.
- **Status** (only available online)Displays the current status of the port. The values are only displayed and cannot be configured. The "Status" parameter depends on the configured protocol. The following values are possible:

  - Disabled  
    The port only receives and is not involved in STP, MSTP and RSTP.
  - Discarding  
    In the "Discarding" mode, BPDU frames are received. Other incoming or outgoing frames are discarded.
  - Listening  
     In this status, BPDUs are both received and sent. The port is involved in the spanning tree algorithm.
  - Learning  
    Stage prior to the "Forwarding" status, the port is actively learning the topology (in other words, the node addresses).
  - Forwarding  
    Following the reconfiguration time, the port is active in the network; it receives and forwards data frames.
- **Fwd. Trans** (only available online)Specifies the number of changes from the "Discarding" status to the "Forwarding" status.
- **Edge Type**
  Specify the type of the "Edge Port". You have the following options:

  - "-"  
    Edge port is disabled. The port is treated as a "no Edge Port".
  - Admin  
    Select this option when there is always an end device on this port. Otherwise a reconfiguration of the network will be triggered each time a connection is changed.
  - Auto  
    Select this option if you want a connected end device to be detected automatically at this port. When the connection is established the first time, the port is treated as a "no Edge Port".
  - Admin/Auto  
    Select these options if you operate a combination of both on this port. When the connection is established the first time, the port is treated as an "Edge Port".
- **Edge** (only available online)  
  Shows the status of the port.

  - Enabled  
     An end device is connected to this port.
  - Disabled  
    There is a Spanning Tree or Rapid Spanning Tree device at this port.

  With an end device, a switch can change over the port faster without taking into account spanning tree frames. If a spanning tree frame is received despite this setting, the port automatically changes to the "Disabled" setting.
- **P.t.P. Type**
  Select the required option from the drop-down list. The selection depends on the port that is set.

  - "-"  
    Point to point is calculated automatically. If the port is set to half duplex, a point-to-point link is not assumed.
  - P.t.P.  
     Even with half duplex, a point-to-point link is assumed.
  - Shared Media  
    Even with a full duplex connection, a point-to-point link is not assumed.

    > **Note**
    >
    > Point-to-point connection means a direct connection between two devices. A shared media connection is, for example, a connection to a hub.
- **P.t.P.**  (only available online)

  - Enabled

    Shows that a point-to-point connection exists.
  - Disabled

    Shows that a point-to-point connection exists.
- **Restr. Role** (SC-600)

  If this check box is selected, the corresponding port is not selected as root port, regardless of the priority value. If the check box is selected, the port with the lowest priority also does not become the root port. Only activate this option if you wish to restrict the impact of bridges outside of the administered range to the Spanning Tree topology.
- **Restr. TCN** (SC-600)

  If this check box is selected, the corresponding port does not forward either received or detected topology changes (Topology Change Notifications) to other ports. Only activate this option if you wish to restrict the impact of bridges outside of the administered range to the Spanning Tree topology.

### LLDP

#### Identifying the network topology

LLDP (Link Layer Discovery Protocol) is defined in the IEEE 802.AB standard.

LLDP is a method used to discover the network topology. Network components exchange information with their neighbor devices using LLDP.

Network components that support LLDP have an LLDP agent. The LLDP agent sends information about itself and receives information from connected devices at periodic intervals. The received information is stored in the MIB.

#### Applications

PROFINET uses the LLDP protocol for topology diagnostics. In the default setting, LLDP is enabled for all ports; in other words, LLDP frames are sent and received on all ports.

The information sent is stored on every device with LLDP capability in an LLDP MIB file. Network management systems can access these LLDP MIB files using SNMP and therefore recreate the existing network topology. In this way, an administrator can find out which network components are connected to each other and can localize disruptions.

On this page, you have the option of enabling or disabling sending and/or receiving per port.

#### Description of the displayed boxes

Table 1 has the following columns:

- **1st column**Shows that the setting is valid for all ports of table 2.
- **Setting**
    
  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.
- **Transfer to table**
    
  If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**Shows the available ports. The port is made up of the module number and the port number, for example port 0.1 is module 0, port 1.
- **Setting**Select whether or not the port will send or receive LLDP frames. The following options are available:

  - Rx  
    This port can only receive LLDP frames.
  - Tx  
    This port can only send LLDP frames.
  - Rx & Tx  
    This port can receive and send LLDP frames.
  - "-" (disabled)  
    This port can neither receive nor send LLDP frames.

### Fiber Monitoring Protocol (SC600)

#### Requirements

- You can only use Fiber Monitoring with transceivers capable of diagnostics. Note the documentation of the devices.
- To be able to use the Fiber Monitoring function, enable LLDP. The Fiber Monitoring information is appended to the LLDP packets.

#### Monitoring optical links

With Fiber Monitoring, you can monitor the received power and the loss of power on optical links between two devices.

If you enable Fiber Monitoring on an optical port, the device sends the current transmit power of the port to its connection partner using LLDP packets. In addition to sending, the device also checks whether corresponding information is received from the connection partner.

Regardless of whether the device receives diagnostics information from its connection partner, it monitors the received power measured at the optical port for the set limit values.

If Fiber Monitoring is enabled on the connection partner, the connection partner transfers the current value for the transmit power of the port to the device. The device compares the value it has received for the transmit power with the actually received power. The difference between the received power and the transmit power represents the power loss on the link. The calculated power loss is also monitored for the set limit values.

If the value of the received power or the power loss falls below or exceeds the set limit values, an event is triggered. You can set limit values in two stages for messages with the severity levels "Warning" and "Critical".

In "System > Events > Configuration", you can specify how the device indicates the event.

> **Note**
>
> If you have enabled Fiber Monitoring and a pluggable transceiver with diagnostics capability is pulled, Fiber Monitoring is automatically disabled for this port and the set limit values and a possibly pending error status are deleted.

#### Description of the displayed boxes

In the table you can specify the limit values for the measured received power too be monitored and the calculated power loss.

- **Port**

  Shows the optical ports that support Fiber Monitoring. This depends on the transceivers.
- **Status**

  Enable or disable Fiber Monitoring.

  As default, the function is disabled.
- **Rx Power [dBm] Maintenance Required**
   **(**
  **Warning**
  **)**

  Specify the value at which you are informed of the deterioration of the received power by a message of the severity level "Warning".

  If you enter the value "0", the received power is not monitored.

  The default value depends on the relevant transceiver.
- **Rx Power [dBm] Maintenance Demanded** 
  **(**
  **Critical**
  **)**

  Specify the value at which you are informed of the deterioration of the received power by a message of the severity level "Critical".

  If you enter the value "0", the received power is not monitored.

  The default value depends on the relevant transceiver.
- **Power Loss [dB] Maintenance Required** 
  **(**
  **Warning**
  **)**

  Specify the value at which you are informed of the power loss of the connection by a message of the severity level "Warning".

  If you enter the value "0", the power loss is not monitored.

  Default: -50 dB
- **Power Loss [dB] Maintenance Demanded** 
  **(**
  **Critical**
  **)**

  Specify the value at which you are informed of the power loss of the connection by a message of the severity level "Critical".

  If you enter the value "0", the power loss is not monitored.

  Default: -55 dB

#### Configuration procedure

**Activating fiber monitoring**

Follow the steps below to activate the monitoring of a port:

1. Select the appropriate check box in the "Status" column.
2. For your setup, enter practical values value at which you want to be informed of deterioration of the received power and the power loss of the connection.
3. Click the "Set Values" button.

**Deactivating fiber monitoring**

Follow the steps below to deactivate the monitoring of a port:

1. Deselect the appropriate check box in the "Status" column.
2. Click the "Set Values" button.

Follow the steps below to deactivate the monitoring of the Rx power or power loss:

1. Enter the value "0" in the appropriate box.
2. Click the "Set Values" button.

### Unicast (SC-600)

This section contains information on the following topics:

- [Filtering](#filtering)
- [Locked Ports](#locked-ports)
- [Blocking](#blocking)

#### Filtering

##### Address filtering

This table shows the unicast addresses entered statically by the user during parameter assignment.

On this page, you also define the static unicast filters.

##### Description of the displayed boxes

The page contains the following boxes:

- **VLAN ID**Select the VLAN ID in which you configure a new static MAC address. If nothing is set, "VLAN1" is set as the basic setting.
- **MAC Address**
  Enter the MAC address here.

The table contains the following columns:

- **VLAN ID**Shows the VLAN ID assigned to this MAC address.
- **MAC Address**Shows the MAC address of the node that the device has learned or the user has configured.
- **Status**Shows the status of each address entry:

  - Static  
    Configured by the user. Static addresses are stored permanently; in other words, they are not deleted when the Aging Time expires or on a restart.
  - Invalid  
    These values are not evaluated.
- **Port**

  Shows the port via which the node with the specified address can be reached. Frames received by the device whose destination address matches this address will be forwarded to this port.

  > **Note**
  >
  > You can only specify **one** port for unicast addresses.

#### Locked Ports

##### Activating the access control

On this page, you can block individual ports for unknown nodes.

If the Port Lock function is enabled, packets arriving at this port from unknown MAC addresses are discarded immediately. Packets from known nodes are accepted by the port.

Since ports with the port lock function enabled cannot learn any MAC addresses, learned addresses on these ports are automatically deleted after the port lock function is enabled. The port accepts only static MAC addresses that were created manually previously.

##### Description of the displayed boxes

Table 1 has the following columns:

- **1st column**Shows that the settings are valid for all ports of table 2.
- **Setting**Select the setting from the drop-down list. You have the following setting options:

  - Enabled  
    Enables the port lock function.
  - Disabled  
    Disables the port lock function.
  - No change  
    Table 2 remains unchanged.
- **Copy to Table**If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port** This column lists all the ports available on this device.
- **Setting**
  Enable or disable access control for the port.

#### Blocking

##### Blocking forwarding of unknown unicast frames

On this page, you can block the forwarding of unknown unicast frames for individual ports.

##### Description of the displayed values

Table 1 has the following columns:

- **1st column**Shows that the settings are valid for all ports of table 2.
- **Setting**
    
  Select the setting from the drop-down list. You have the following setting options:

  - Enabled  
    Blocking of unicast frames is enabled.
  - Disabled  
    Blocking of unicast frames is disabled.
  - No change  
    Table 2 remains unchanged.
- **Copy to Table**If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**All available ports are listed in this column. Unavailable ports are not displayed.
- **Setting**
    
  Enable or disable the blocking of unicast frames.

### Multicast (SC-600)

This section contains information on the following topics:

- [Groups](#groups-1)
- [Blocking](#blocking-1)

#### Groups

##### Multicast applications

In the majority of cases, a frame is sent with a unicast address to a particular recipient. If an application sends the same data to several recipients, the amount of data can be reduced by sending the data using one multicast address. For some applications (e.g. NTP), there are fixed multicast addresses.

##### Description of the displayed boxes

The page contains the following boxes:

- **VLAN ID**If you click on this text box, a drop-down list is displayed. Here you can select the VLAN ID of a new MAC address you want to configure.
- **MAC address**
  Here you enter a new MAC multicast address you want to configure.

The table has the following columns:

- **Select**
  Select the row you want to delete.
- **MAC address**Here, the multicast address is displayed that the device has learned or the user has configured.
- **Status -** StaticShows the status of each address entry. The address was entered statically by the user. Static addresses are stored permanently; in other words, they are not deleted when the Aging-Time expires or when the device is restarted. These must be deleted by the user.

##### Configuration procedure

**Creating a new entry**

1. Select the required VLAN ID from the ""drop-down list.
2. Enter the MAC address in the "MAC address" input box.
3. Click the "Create" button. A new entry is generated in the table.
4. Assign the relevant ports to the MAC address.
5. Click the "Set Values" button.

#### Blocking

##### Disabling the forwarding of unknown multicast frames

On this page, you can block the forwarding of unknown multicast frames for individual ports.

##### Description of the displayed values

Table 1 has the following columns:

- **1st column**Shows that the settings are valid for all ports of table 2.
- **Setting**Select the setting from the drop-down list. You have the following setting options:

  - Enabled  
    Blocking of multicast frames is enabled.
  - Disabled  
    Blocking of unknown multicast frames is disabled.
  - No change  
    Table 2 remains unchanged.
- **Copy to Table**If you click the button, the setting is adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**All available ports are listed in this column. Unavailable ports are not displayed.
- **Setting**
    
  Enable or disable the blocking of multicast frames.

##### Configuration procedure

**Enabling blocking for an individual port**

1. Select the check box in the relevant row in table 2.
2. To apply the changes, click the "Set Values" button.

**Enabling blocking for all ports**

1. In the "Setting" drop-down list, select the "Enabled" entry.
2. Click the "Copy to table" button. The check box is enabled for all ports in table 2.
3. To apply the changes, click the "Set Values" button.

### Inter-VLAN Bridge (SC-600)

This section contains information on the following topics:

- [Overview](#overview-4)
- [Configuration](#configuration-5)

#### Overview

##### Overview

You can create one bridge per device and add a maximum of six VLANs to the bridge.

##### Description

The page contains the following boxes:

- **Bridge-ID**

  Enter the bridge ID in the "Bridge-ID" text box. The Bridge-ID (a number between 1 and 255) can only be assigned once when creating a new data record and can then no longer be changed. To make a change, the entire data record must be deleted and created again.

The table has the following columns:

- **Bridge-ID**

  Shows the bridge ID.
- **Transparent**

  When you enable this option, the Inter-VLAN Bridge and the associated VLANs are switched to transparent mode when the bridge is activated. Ports belonging to the bridge become transparent ports. This means the following:

  - Tagged frames that are received at these ports are not evaluated and are forwarded to all other ports of the Inter-VLAN Bridge with unchanged tag. No frames are forwarded from ports that do not belong to the Inter-VLAN Bridge to ports that belong to the Inter-VLAN Bridge.
  - Untagged frames that are received at these ports are also forwarded to all other ports of the Inter-VLAN Bridge without tag.
  - As long as the transparent bridge is enabled, you cannot change the port associations of the affected VLANs.

  The prerequisite for this is that the port VLAN ID of all ports belonging to the VLAN is set to the VLAN ID.

  If you disable this option, the VLAN tags are evaluated.
- **Enable**

  Enables the bridge between the VLANs specified in the "Configuration" tab. After it has been enabled, the bridge adopts the IP address configuration of the VLANs for which the Type "Master" was selected in the "Configuration" tab. The devices of the VLANs can no longer be reached at their own IP addresses after the bridge has been enabled but only over the IP address of the bridge.

#### Configuration

##### Configuration

On this page you specify the VLANs between which a bridge is to be set up and which VLAN is to be used as master VLAN. You select the bridge you want to use by using its Bridge-ID that was created in the "Overview" tab.

##### Description

The page contains the following boxes:

- **Interface**

  VLAN to which the setting relates. The list of VLANs is dynamic and is based on the settings from "Layer 3 > Subnets".
- **Bridge-ID**

  Select the ID of the bridge that is to be used for the selected VLAN.
- **Type**

  Select the type of the interface.

  - Member: The IP address configuration of the VLAN is not used for the bridge.
  - Master: The IP address configuration of the VLAN is used for the bridge. Use this setting for the VLAN / interface that is used by the TIA Portal for access to the devices of the VLANs.

  **Special features of the TIA interface**

  If one of the interfaces is configured as TIA interface, you must set the type "Master" for it. Otherwise, the bridge cannot be enabled.

## Configuring layer 3 functions for IPv4

This section contains information on the following topics:

- [Static routes](#static-routes)
- [Subnets](#subnets)
- [NAT](#nat-1)
- [VRRPv3](#vrrpv3)

### Static routes

#### Static route

On this page you specify the routes via which a data exchange can take place between the various subnets. Dynamic routing protocols are not supported, for example RIP, OSPF.

#### Description

The page contains the following boxes:

- **Destination Network**

  Enter the network address of the destination that can be reached via this route.
- **Subnet Mask**

  Enter the corresponding subnet mask.
- **Gateway**

  Enter the IPv4 address of the gateway via which this network address is reachable.
- **Interface**

  Specify whether the network address can be reached via a certain interface or via the gateway (auto).
- **Administrative Distance**

  Enter the metric for the route. The metric corresponds to the quality of a connection, for example speed, costs. If there are several equal routes, the route with the lowest metric value is used.

  If you do not enter anything, "not used" is entered automatically. The metric can be changed later.

  Range of values: 1 - 255 or -1 for "not used".

  Here, 1 is the value for the best possible route. The higher value, the longer packets need to get to their destination.

The table has the following columns:

- **Select**
    
  Select the row you want to delete.
- **Destination Network**

  Shows the network address of the destination.
- **Subnet Mask**

  Shows the corresponding subnet mask.
- **Gateway**

  Shows the IPv4 address of the next gateway.
- **Interface** (only available online)

  Shows the Interface of the route.
- **Administrative Distance**

  Enter the metric for the route. When creating the route, "not used" is entered automatically. The metric corresponds to the quality of a connection, based for example on speed or costs. If there are several equal routes, the route with the lowest metric value is used.

  Range of values: 1 - 255

  Here, 1 is the value for the best possible route. The higher value, the longer packets need to get to their destination.
- **State** (only available online)

  Shows whether or not the route is active.

### Subnets

This section contains information on the following topics:

- [Overview](#overview-5)
- [Configuration](#configuration-6)

#### Overview

The page shows the subnets for the selected interface. A subnet always relates to an interface and is created in the "Configuration" tab.

##### Description

The page contains the following box:

- **Interface**

  Select the interface on which you want to configure another subnet.

The table has the following columns:

- **Interface**Shows the interface.
- **TIA Interface**
    
  Shows whether the interface is a TIA interface.
- **Status** (SC-600)

  Shows whether or not the interface is enabled.
- **Interface Name**Shows the name of the interface.
- **MAC Address** (only available online)Shows the MAC address.
- **IP Address**Shows the IPv4 address of the subnet.
- **Subnet Mask**Shows the subnet mask.
- **Address Type**Shows the address type. The following values are possible:

  - Primary  
    The first IPv4 address that was configured on an IPv4 interface.
  - Secondary

    All other IPv4 addresses that were configured on an IPv4 interface.
- **IP Assignment Method**Shows how the IPv4 address is assigned. The following values are possible:

  - Static  
    The IPv4 address is static. You enter the settings in "IP Address" and "Subnet Mask".
  - Dynamic (DHCP)  
    The device obtains a dynamic IPv4 address from a DHCPv4 server.
- **Address Collision Detection Status** (only available online)

  If new IPv4 addresses become active in the network, the "Address Collision Detection" function checks whether this can result in address collisions. The allows IPv4 addresses that would be assigned twice to be detected.

  > **Note**
  >
  > The function does not run a cyclic check.

  This column shows the current status of the function. The following values are possible:

  - Idle

    The interface is not enabled and does not have an IPv4 address.
  - Starting

    This status indicates the start-up phase. In this phase, the device initially sends a query as to whether the planned IPv4 address already exists. If the address is not yet been assigned, the device sends the message that it is using this IP address as of now.
  - Conflict

    The interface is not enabled. The interface is attempting to use an IPv4 address address that has already been assigned.
  - Defending

    The interface uses a unique IPv4 address. Another interface is attempting to use the same IPv4 address.
  - Active

    The interface uses a unique IPv4 address. There are no collisions.
  - Not supported

    The function for detection of address collisions is not supported.
  - Disabled

    The function for detection of address collisions is disabled.
- **MTU** (S615)  
  Shows the packet size.

#### Configuration

On this page, you configure the subnet for the interface.

##### Description

The page contains the following:

- **Interface (Name)**
    
  Select the interface from the drop-down list.
- **Status** (SC-600)

  Enable or disable the interface.
- **Interface Name**
  Enter the name of the interface.
- **MAC Address** (only available online)

  Displays the MAC address of the selected interface.
- **DHCP** (for VLAN interface)

  The VLAN interface obtains the IPv4 address from a DHCP server.
- **Dynamic** (for PPP interface with S615)

  The PPP interface obtains the IP address from the provider.

  > **Note**
  >
  > **Note the following points:**
  >
  > - If you want to operate the device as a router with several interfaces, disable DHCP on all interfaces.
  > - Only 1 dynamic client can be enabled.
- **IP Address**
  Enter the IPv4 address of the interface. The IPv4 addresses must not be used more than once.
- **Subnet Mask**
  Enter the subnet mask of the subnet you are creating. Subnets on different interfaces must not overlap.
- **Broadcast IP Address** (S615)  
  If a specific IP address is to be used as the broadcast IP address of the subnet, enter it. Otherwise the last IP address of the subnet will be used.
- **Address Type**Shows the address type. The following values are possible:

  - Primary  
    The first subnet of the interface.
  - Secondary  
    All further subnets of the interface.
- **TIA Interface**

  Select whether or not this interface should become the TIA Interface.

  The following conditions apply to the TIA interface:

  - Only interfaces with the address type "Primary" can be enabled as the TIA interface.
  - There must only ever be one TIA interface.
  - There can only be one TIA interface.
  - A TIA interface is always a VLAN interface.
- **MTU** (S615)  
  MTU (Maximum Transmission Unit) specifies the maximum size of the packet. If packets are longer than the set MTU, they are fragmented.

### NAT

This section contains information on the following topics:

- [NAT General](#nat-general)
- [Masquerading](#masquerading)
- [NAPT](#napt)
- [Source NAT](#source-nat)
- [NETMAP](#netmap)

#### NAT General

On this page, you enable Gratuitous ARP for alias IP addresses.

##### Description

On this page, you can enable the following option:

- **Announce alias IP addresses**

  When the option is enabled, a Gratuitous ARP is sent for each alias IP address. This announces the IP address in the network, and the other devices can update their ARP cache. The Gratuitous ARP is only sent at the time of configuration, that is, during device startup or when an NAT rule (NAPT) is being configured.

#### Masquerading

On this page, you enable the rules for IP masquerading.

##### Description

The table has the following columns:

- **Interface**

  Interface to which the setting relates. Only interfaces with a configured subnet are available.
- **Enable Masquerading**

  When enabled, with each outgoing data packet sent via this interface, the source IP address is replaced by the IP address of the interface.

#### NAPT

On this WBM page, you can configure a port translation in addition to the address translation.

The following port translations are possible:

- From a single port to the same port:

  If the ports are the same, the frames are forwarded without port translation.
- From a single port to a single port

  The frames are translated to the port.
- From a port range to a single port

  The frames from the port range are translated to the same port (n:1).
- From a port range to the same port range

  If the port ranges are the same, the frames are forwarded without port translation.

##### Description

The page contains the following boxes:

- **Source Interface**

  Select the interface on which the queries will arrive.
- **Traffic Type**

  Specify the protocol for which the address assignment is valid.
- **Use Interface IP from Source Interface**

  When enabled, the IP address of the selected interface is used for "Dest IP Address".

- **Destination IP Address**

  Enter the destination IP address. The frames are received at this IP address. Can only be edited if "Use Interface IP from Source Interface" is disabled.
- **Destination Port**

  Enter the destination port. Incoming frames with this port as the destination port are forwarded. If the setting is intended to apply to a port range, enter the range with start port "-" end port, for example 30 - 40.
- **Translated Destination IP**

  Enter the IP address of the node to which this frame will be forwarded.
- **Translated Destination Port**

  Enter the number of the port. This is the new destination port to which the incoming frame will be forwarded. If the setting is intended to apply to a port range, enter the range with start port "-" end port, for example 30 - 40.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Source Interface**

  Shows the interface from which the packets need to come. Only these packets are considered for port forwarding.
- **Traffic Type**

  Shows the protocol for which the address assignment applies.
- **Interface IP**

  Shows whether the IP address of the interface is used.
- **Destination IP**

  Shows the destination IP address. The frames are received at this IP address.
- **Destination Port**

  Shows the destination port. Incoming frames with this port as the destination port are forwarded.
- **Translated Destination IP**

  Shows the IP address of the node to which the packets will be forwarded.
- **Translated Destination Port**

  Shows the destination port to which the packets are translated.

#### Source NAT

On this page, you configure the rules for source NAT.

> **Note**
>
> **Firewall rules with source NAT**
>
> Address translation with source NAT was only performed after the firewall; the non-translated addresses are therefore used.
>
> Security > Firewall > IP rules
>
> - Source (Range): Input from "Source IP Addresses"
> - Destination (Range): Input from "Destination IP Addresses"

##### Description

- **Source Interface**
  **/** 
  **Destination Interface**

  Specify the direction of the connection establishment. Only connections established in this specified direction are taken into account.

  The virtual interfaces of VPN connections can also be selected:

  - VLANx: VLANs with configured subnet
  - ppp2: WAN interface
  - SINEMA RC: Connection to SINEMA RC Server
  - IPsec:Either all IPsec VPN connections (all) or a specific IPsec VPN connection
  - OpenVPN: Either all OpenVPN connections (all) or a specific OpenVPN connection
  > **Note**
  >
  > When you configure a NAT address translation to or from the direction of the VPN tunnel, only the IP addresses involved in the NAT address translation rules can be reached via the VPN tunnel.
- **Source IP Address(es)**

  Specify the source IP addresses for which this source NAT rule is valid. Only the packets that correspond to the addresses entered are taken into account.

  The following entries are possible:

  - IP address: Applies precisely to the specified IP address.
  - IP address range: Applies to a certain IP address range: Start IP address "-" End IP address, e.g. 192.168.100.10 - 192.168.100.20
  - IP subnet: Applies to several IPv4 addresses grouped together to form an IP address range: IP address/number of bits of the network part (CIDR notation)
- **Use Interface IP from Destination Interface**

  When enabled, the IP address of the selected destination interface is used in "Translated Source IP Address".
- **Translated Source IP Address**

  Enter the IP address with which the IP address of the sender is replaced. Can only be edited if "Use Interface IP from Destination Interface" is disabled.
- **Destination IP Address(es)**

  Specify the destination IP addresses for which this source NAT rule is valid. Only the packets whose destination IP address is in the range of entered addresses are taken into account.

  - IP address: Applies precisely to the specified IP address.
  - IP address range: Applies to a certain IP address range: Start IP address "-" End IP address, e.g. 192.168.100.10 - 192.168.100.20
  - IP subnet: Applies to several IPv4 addresses grouped together to form an IP address range: IP address/number of bits of the network part (CIDR notation)

The table has the following columns:

- Source Interface

  Shows the source interface.
- Destination Interface

  Shows the destination interface.
- Source IP Address(es)

  Shows the IP addresses of the senders for which address translation is required.
- Translated Source IP Address  
  Shows the IP address with which the IP address of the sender is replaced.
- Destination IP Address(es)  
  Shows the IP addresses of the recipients for which address translation is required.

#### NETMAP

On this page, you specify the rules for NETMAP. NETMAP is static 1:1 mapping of network addresses in which the host part is retained. For more information, refer to the section "NAT and firewall".

> **Note**
>
> **Firewall rule with source NAT**
>
> Address translation with source NAT was only performed after the firewall; the non-translated addresses are therefore used.
>
> Security > Firewall > IP rules
>
> - Source (Range): Input from "Source IP Subnet"
> - Destination (Range): Input from "Destination IP Subnet"
>
> **Firewall rule with destination NAT**
>
> Address translation with NAT was already performed before the firewall; the translated addresses are therefore used in the firewall.
>
> Security > Firewall > IP rules
>
> - Source (Range): Input from "Source IP Subnet"
> - Destination (Range): Input from "Translated Destination IP Subnet"

##### Description

- **Type**

  Specify the type of address translation.

  - Source: Replacement of the source IP address
  - Destination: Replacement of the destination IP address
- **Source Interface**

  Specify the source interface.

  - VLANx: VLANs with configured subnet
  - SINEMA RC: Connection to SINEMA RC Server
  - IPsec: Either all IPsec VPN connections (all) or a specific IPsec VPN connection
  - ppp2: WAN interface
  - OpenVPN: Either all OpenVPN connections (all) or a specific OpenVPN connection
- **Destination Interface**

  Specify the destination interface.

  - VLANx: VLANs with configured subnet
  - SINEMA RC: Connection to SINEMA RC Server
  - IPsec: Either all IPsec VPN connections (all) or a specific IPsec VPN connection
  - ppp2: WAN interface
  - OpenVPN: Either all OpenVPN connections (all) or a specific OpenVPN connection
- **Source IP Subnet**

  Enter the subnet of the sender.   
  The subnet can also be a single PC or another subset of the subnet. Use the CIDR notation.
- **Translated Source IP Subnet**

  Enter the subnet with which the subnet of the sender will be replaced. Can only be edited in the "SourceNAT" settings.  
  The subnet can also be a single PC or another subset of the subnet. Use the CIDR notation.
- **Destination IP Subnet**

  Enter the subnet of the recipient.  
  The subnet can also be a single PC or another subset of the subnet. Use the CIDR notation.
- **Translated Destination IP Subnet**

  Enter the subnet with which the subnet of the recipient will be replaced. Can only be edited in the "DestinationNAT" settings.  
  The subnet can also be a single PC or another subset of the subnet. Use the CIDR notation.

The table has the following columns:

- Type

  Shows the direction of the address translation.
- Source Interface

  Shows the source interface.
- Destination Interface

  Shows the destination interface.
- Source IP Subnet

  Shows the subnet of the sender.
- Translated Source IP Subnet

  Shows the subnet of the sender with which the subnet of the sender is replaced.
- Destination IP Subnet

  Shows the subnet of the recipient.
- Translated Destination IP Subnet

  Shows the subnet of the recipient with which the subnet of the recipient is replaced.

### VRRPv3

This section contains information on the following topics:

- [Router](#router)
- [Configuration](#configuration-7)
- [Addresses Overview](#addresses-overview)
- [Addresses Configuration](#addresses-configuration)
- [Interface Tracking](#interface-tracking)
- [Address monitoring](#address-monitoring)

#### Router

##### Introduction

On this page, you create new virtual routers. A maximum of two virtual routers can be configured. You can configure other parameters in "Layer 3 (IPv4) > VRRPv3 > Configuration".

> **Note**
>
> - You can use VRRPv3 on VLAN interfaces. Router ports are not supported.

##### Requirement

For the incoming packets to be forwarded to the device, enable the predefined IPv4 rule "VRRP".

##### Description

The page contains the following:

- **VRRPv3**

  Enable or disable routing using VRRPv3.
- **Track**

  Enable or disable VRID tracking.

  When enabled, all VRRP instances are monitored. If the status of a VRRP instance changes to "Initialize", the priority of all VRRP instances is reduced to the value "1".

  If the status of a VRRP instance changes, the original priority of all VRRP instances is restored.
- **Interface**

  Select the required VLAN interface operating as virtual router.
- **VRID**

  Enter the ID of the virtual router. This ID defines the group of routers that form a virtual router (VR). In the group, this is the same. It can no longer be used for other groups.

  Valid values are 1 to 255.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Interface**

  Shows the IPv4 interface that functions as the virtual router.
- **VRID**

  Shows the ID of the virtual router.
- **Virtual MAC Address** (only available online)

  Shows the virtual MAC address of the virtual router.
- **Primary IP Address**

  Shows the numerically lowest IPv4 address in this VLAN. The entry 0.0.0.0 means that the "Primary" address on this VLAN is used. Otherwise, all IPv4 addresses configured on this VLAN in the "Layer 3 > Subnets" menu are valid values.
- **Router State** (only available online)

  Shows the current status of the virtual router. Possible values are:

  - Master

    The router is the master router and handles the routing functionality for all assigned IPv4 addresses.
  - Backup

    The router is the backup router. If the master router fails, the backup router takes over the tasks of the master router.
  - Initialize

    The virtual router has just been turned on. It will soon change to the "Master" or "Backup" status.
- **Master IP Address**  (only available online)

  Shows the IPv4 address of the master router.
- **Priority** (only available online)

  Shows the priority of the virtual router.

  Valid values are 1-254.

  If an IPv4 address is assigned to the VRRP router that is also actually configured on the local IPv4 interface, the value 255 is entered automatically. All other priorities can be distributed freely among the VRRP routers. The higher the priority, the earlier the VRRP router becomes "Master".
- **Advert. Interval**

  Shows the interval at which the master router sends VRRPv3 packets.
- **Preempt**

  Shows the precedence of a router when changing roles between backup and master.

  - yes

    This router has precedence when changing roles.
  - no

    This router does not have precedence when changing roles.

##### VRRP and DHCP server

If you want to operate a DHCP server on the devices of a VRRP group, the DHCP server must be configured on the master router. Backup routers do not react to DHCP queries. Make sure that the master router is statically configured and that after a failure, becomes the master of the VRRP group again.

#### Configuration

##### Introduction

On this page, you configure the virtual router.

##### Description

The page contains the following:

- **Interface / VRID**

  Select the ID of the virtual router to be configured.
- **Primary Address**

  Select the primary IPv4 address. If the router becomes master router, the router uses this IPv4 address.

  > **Note**
  >
  > If you only configure one subnet on this VLAN, no entry is necessary. The entry is then 0.0.0.0.   
  > If you configure more than one subnet on the VLAN and you want a specific IPv4 address to be used as the source address for VRRP packets, select the IPv4 address. Otherwise, the numerically lowest IPv4 address will be used.
- **Priority**

  Enter the priority of this virtual router. Valid values are 1-254.   
  If an IPv4 address is assigned to the VRRPv3 router that is also actually configured on the local IPv4 interface, the value 255 is entered automatically. All other priorities can be distributed freely among the VRRPv3 routers. The higher the priority, the earlier the VRRPv3 router becomes "Master".
- **Advertisement interval**

  Enter the interval in seconds after which a master router sends a VRRPv3 packet again.
- **Preempt lower priority Master**.

  Allow precedence when changing roles between backup and master based on the selection process.
- **Track ID**
    
  Select a track ID.
- **Decrement Priority**
    
  Enter the value by which priority of the VRRP interface will be reduced.
- **Current Priority**
    
  Shows the priority of the VRRP interface after the monitored interface has changed to the "down" status.

#### Addresses Overview

##### Overview

This page shows which IPv4 addresses the virtual router monitors. Each virtual router can monitor a maximum of one IPv4 address.

##### Settings

The table has the following columns:

- **Interface**

  Shows the Interface that functions as the virtual router.
- **VRID**

  Shows the ID of this virtual router.
- **Number of Addresses**

  Shows the number of IPv4 addresses.
- **Associated IP Address (1) ... Associated IP Address (4)**

  Shows the router IPv4 addresses monitored by this virtual router. If a router takes over the role of master, the routing function is taken over by this router for all these IPv4 addresses.

#### Addresses Configuration

##### Creating or changing the monitored IP addresses

On this page, you can create, modify or delete the IPv4 addresses to be monitored.

##### Description

The page contains the following:

- **Interface / VRID**

  Select the ID of the virtual router.
- **Associated IP Address**

  Enter the IPv4 address that the virtual router will monitor.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted**.**
- **Associated IP Address**

  Shows the IPv4 addresses that the virtual router monitors.

#### Interface Tracking

On this page, you configure the monitoring of interfaces.

When the link of a monitored interface changes from "up" to "down", the priority of the assigned VRRP interface is reduced. You configure the value by which the priority is reduced on the page "Layer 3 > VRRP/VRRPv3 > Configuration".

When the link of the interface changes back from "down" to "up", the original priority of the VRRP interface is restored.

##### Description

The page contains the following boxes:

- **Interface**

  Select the required interface to be monitored.
- **Track ID**

  Enter a track ID.
- **Track ID**

  Select a track ID.
- **Track Interface Count**

  Enter how many monitored interfaces need to change to the "down" status, before the priority is changed.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Track ID**

  Shows the track ID.
- **Interface**

  Shows the interface that is being monitored.

#### Address monitoring

You configure the monitoring of IPv4 addresses on this page. The router sends a ping request to each of the configured IPv4 addresses within the specified time period. If no response is received within a specified time period, the VRRP priority of the corresponding interface is reduced.

##### Description

The page contains the following boxes:

- **Track ID**
    
  Enter the track ID.
- **IP Address**
    
  Enter the IPv4 address to be monitored. You can enter a maximum of five IPv4 addresses.

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Track ID**
    
  Shows the track ID.
- **IP Address**
    
  Show the IPv4 address to be monitored.
- **Ping Period**
    
  Shows the cycle time in seconds between two ping requests.
- **Ping Timeout**
    
  Shows the time in seconds that the router waits for a ping response. The minimum duration is three times the ping period.

## Configuring layer 3 functions for IPv6

This section contains information on the following topics:

- [Subnets (S615)](#subnets-s615)

### Subnets (S615)

#### Connected Subnets

On this page, you can enable IPv6 on the interface. The interface is also called an IPv6 interface. An IPv6 interface can have several IPv6 addresses.

#### Description

The page contains the following:

- **Interface**

  Select the IP interface on which IPv6 will be enabled.
- **IPv6 Enable**

  Enable or disable IPv6 on the interface.

  > **Note**
  >
  > **Disabling IPv6**
  >
  > If IPv6 is enabled on an interface, you can only disable IPv6 by deleting interface.
- **IPv6 Address**

  Enter the IPv6 address. The entry depends on the selected address type.
- **Prefix Length**

  Enter the number of left-hand bits belonging to the prefix.
- **IPv6 Address Type**

  Select the address type.

  - Unicast
  - Anycast
  - Link Local: IPv6 address is only valid on the link
- **Address Autoconfiguration (SLAAC)**

  Enable or disable the SLAAC (Stateless Address Auto Configuration) mechanism for the address configuration.

  If SLAAC is enabled, there will be stateless auto configuration via NDP (Neighbor Discovery Protocol).

The table has the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Interface Name**

  Shows the name of the interface.
- **IPv6 Address**

  Shows the IP address of the subnet.
- **Prefix Length**

  Shows the prefix length.
- **IPv6 Address Type**

  Displays the address type. The following values are possible:

  - Unicast
  - Anycast
  - Link Local
- **Duplicate Address Detection Status**

  In Address Autoconfiguration (SLAAC), the "Duplicate Address Detection Status" function prevents IPv6 addresses from being assigned twice. The device can only use free IPv6 addresses during autoconfiguration.

  When the function is enabled, the check via NDP takes place automatically.

  > **Note**
  >
  > The function does not run a cyclic check.

  This column shows the current status of the function. The following values are possible:

  - **Tentative**This status indicates that the selected IPv6 address is being checked. The device sends a neighbor solicitation message to the selected IPv6 address.
  - **Conflict**This status indicates that the IPv6 address is already being used. In this case, a neighbor advertisement message with the selected IPv6 address is returned to the device.
  - **Complete**This status indicates that the selected IPv6 address can be used. In this case, the device did not receive feedback within a period of time and assumes that the IPv6 address is not yet assigned.
  - **Down**This status indicates that the interface is not active. No check is carried out.

## Configuring security functions

This section contains information on the following topics:

- [Passwords](#passwords-1)
- [Users](#users)
- [AAA](#aaa)
- [Certificates](#certificates-1)
- [Firewall](#firewall-2)
- [IPsec VPN](#ipsec-vpn-2)
- [OpenVPN](#openvpn-2)
- [Brute Force Prevention](#brute-force-prevention)

### Passwords

This section contains information on the following topics:

- [Passwords](#passwords-2)
- [Options (S615)](#options-s615)

#### Passwords

##### Configuration of the device passwords

> **Note**
>
> The page is only available if there is an online connection to the device.

> **Note**
>
> If you are logged in via a RADIUS server, you cannot change any local device passwords.

On this page, you can change passwords. If you are logged on with read/write rights, you can change the passwords for all user accounts. If you are logged in with read rights, you can only change your own password.

> **Note**
>
> When you log in for the first time or following a "Restore Factory Defaults and Restart" with the preset user "admin" you will be prompted to change the password.
>
> The factory settings for the passwords when the devices ship are as follows:
>
> - admin: admin

> **Note**
>
> **Changing the password in Trial mode**
>
> Even if you change the password in "Trial" configuration mode, this change is saved immediately.

##### Description of the displayed boxes

- **Current User**
    
  Shows the user that is currently logged in.
- **Current User Password**

  Enter the password for the currently logged in user.
- **User Account**

  Select the user whose password you want to change.
- **Password Policy**

  Shows which password policy is being used when assigning new passwords.

  - High

    Password length: at least 8 characters, maximum 128 characters

    At least 1 uppercase letter

    At least 1 special character

    At least 1 number
  - Low

    Password length: at least 6 characters, maximum 128 characters
  - User defined

    Custom Password Policy

  You configure the password policy on the page "Security > Passwords > Options".
- **New name for the Admin user account**

  You can change the name the default user "admin" once. Afterwards, renaming "admin" is no longer possible.
- **New Password**
    
  Enter the new password for the selected user.

  It may not contain any of the following characters: | § ? " ; : ß \

  The space and the character for "remove" must also not be included.
- **Password Confirmation**
    
  Enter the new password again to confirm it.

#### Options (S615)

> **Note**
>
> The page is only available if there is an online connection to the device.

On this page you specify which password policy will be used when assigning new passwords.

##### Description

- **Password Policy**

  Shows which password policy is currently being used
- **New Password Policy**

  Select the required setting from the drop-down list.

  - High

    Password length: at least 8 characters, maximum 128 characters

    At least 1 number

    At least 1 special character

    At least 1 uppercase letter
  - Low

    Password length: at least 6 characters, maximum 128 characters
  - Custom

    Configure the desired password requirements under "Password Policy Details".
- **Password Policy Details**

  When you have selected the "High" or "Low" password policy, the relevant password requirements are displayed.

  When you have selected the "User-defined" password policy, you can configure the relevant password requirements.

  - Minimum Password Length

    Specifies the minimum length of a password.
  - Minimum Number of Numeric Characters

    Specifies the minimum number of numeric characters in a password.
  - Minimum Number of Special Characters

    Specifies the minimum number of special characters in a password.
  - Minimum Number of Uppercase Letters

    Specifies the minimum number of uppercase characters in a password.
  - Minimum Number of Lowercase Letters

    Specifies the minimum number of lowercase characters in a password.

### Users

This section contains information on the following topics:

- [Local users](#local-users)
- [Roles](#roles-1)
- [Groups](#groups-2)

#### Local users

> **Note**
>
> The page is only available with some devices if there is an online connection to the device.

##### Local users

On this page, you create local users for WBM and CLI with the corresponding rights.  To create a user account, the logged in user must have the "admin" role.

> **Note**
>
> The values displayed depend on the rights of the logged-in user.

##### Description

The page contains the following:

- **User Account**

  Enter the name for the user. The name must meet the following conditions:

  - It must be unique.
  - It must be between 1 and 250 characters long.
  - The following characters must not be included: | § ? " ; : ß
  - The characters for Space and Delete also cannot be contained.
  > **Note**
  >
  > **User name cannot be changed**
  >
  > After creating a user, the user name can no longer be modified.
  >
  > If a user name needs to be changed, the user must be deleted and a new user created.

  > **Note**
  >
  > **User names: admin**
  >
  > You can configure the device with this user name.
  >
  > When you log in for the first time or log in after a "Restore Factory Defaults and Restart", you are prompted to change the pre-defined password "admin". You can also rename the "admin" user preset in the factory once. Afterwards, renaming "admin" is no longer possible.
- **Password Policy**

  Shows which password policy is being used.

  - High

    Password length: at least 8 characters, maximum 128 characters

    At least 1 uppercase letter

    At least 1 special character

    At least 1 number
  - User-defined

    The password must meet the configured requirements. You configure the requirements under "Security > Passwords > Options".
- **Password**

  Enter the password. The strength of the password depends on the set password policy.

  It must not contain any of the following characters: | § ? " ; : ß \
- **Password Confirmation**

  Enter the password again to confirm it.
- **Role**

  Select a role.

  You can choose between system-defined and self-defined roles, refer to the page "Security > Users > Roles.".

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.

  > **Note**
  >
  > The users preset in the factory as well as logged in users cannot be deleted or changed.
- **User Account**

  Shows the user name.
- **Role**

  Shows the role of the user.
- **Description**

  Displays a description of the user account. The description text can be up to 100 characters long.
- **Remote Access**

  - Only

    Only remote access, i.e. no rights other than logging into the WBM page for dynamic firewall.
  - None

    No remote access. The user cannot log in to the dynamic firewall, but only to the WBM of the device.
  - Additional

    The user can log in to both the WBM of the device and the dynamic firewall.

#### Roles

> **Note**
>
> The page is only available if there is an online connection to the device.

##### Roles

On this page, you create roles that are valid locally on the device.

> **Note**
>
> The values displayed depend on the rights of the logged-in user.

##### Description of the displayed boxes

The page contains the following:

- **Role Name**

  Enter the name for the role. The name must meet the following conditions:

  - It must be unique.
  - It must be between 1 and 64 characters long.
  > **Note**
  >
  > **Role name cannot be changed**
  >
  > After creating a role, the name of the role can no longer be changed.
  >
  > If a name of a role needs to be changed, the role must be deleted and a new role created.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.

  > **Note**
  >
  > Predefined roles and assigned roles cannot be deleted or modified.
- **Role**

  Shows the name of the role.
- **Function Right**

  Select the function rights of the role.

  - 1

    Users with this role can read device parameters but cannot change them. Users with this role can change their own password.
  - 15

    Users with this role can both read and change device parameters.
  > **Note**
  >
  > **Function right cannot be changed**
  >
  > If you have assigned a role, you can no longer change the function right of the role.
  >
  > If you want to change the function right of a role, follow the steps outlined below:
  >
  > 1. Delete all assigned users.
  > 2. Change the function right of the role:
  > 3. Assign the role again.
- **Description**

  Enter a description for the role. With predefined roles a description is displayed. The description text can be up to 100 characters long.
- **Remote Access**

  - None

    No remote access. The user cannot log in to the dynamic firewall, but only to the WBM of the device.
  - Additional

    The user can log in to both the WBM of the device and the dynamic firewall.
  - Only

    The user can only log in to the dynamic firewall.

#### Groups

> **Note**
>
> The page is only available if there is an online connection to the device.

##### User Groups

On this page you link a group with a role.

In this example, the group "Administrators" is linked to the "admin" role. The group is defined on a RADIUS server. The role is defined locally on the device. When a RADIUS server authenticates a user and assigns the user to the "Administrators" group, this user is given rights of the "admin" role.

> **Note**
>
> The values displayed depend on the rights of the logged-in user.

##### Description of the displayed boxes

The page contains the following:

- **Group Name**

  Enter the name of the group. The name must match the group on the RADIUS server.

  The name must meet the following conditions:

  - It must be unique.
  - It must be between 1 and 64 characters long.
  - The following are not permitted: § ? " ; :

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Group**

  Shows the name of the group.
- **Role**

  Select a role. Users who are authenticated with the linked group on the RADIUS server receive the rights of this role locally on the device. You can choose between system-defined and self-defined roles, refer to the page "Security > Users > Roles".
- **Description**

  Enter a description for the link of the group.to a role. The description text can be up to 100 characters long.

### AAA

This section contains information on the following topics:

- [General](#general-3)
- [RADIUS client](#radius-client)
- [802.1X Authenticator (SC600)](#8021x-authenticator-sc600)

#### General

##### Login of network nodes

The designation used "AAA" stands for "Authentication, Authorization, Accounting". This feature is used to identify and allow network nodes, to make the corresponding services available to them and to specify the range of use.

On this page, you configure the login.

##### Description

The page contains the following boxes:

> **Note**
>
> To be able to use the login authentication "RADIUS", "Local and RADIUS" or "RADIUS and fallback Local", a RADIUS server must be stored and configured for user authentication.

- **Login Authentication**
    
  Specify how the login is made:

  - Local

    The authentication must be made locally on the device.
  - RADIUS

    The authentication must be handled via a RADIUS server.
  - Local and RADIUS

    The authentication is possible both with the users that exist on the device (user name and password) and via a RADIUS server.

    The user is first searched for in the local database. If the user does not exist there, a RADIUS query is sent.
  - RADIUS and fallback Local

    The authentication must be handled via a RADIUS server.

    A local authentication is performed only when the RADIUS server cannot be reached in the network.

#### RADIUS client

##### Authentication over an external server

The concept of RADIUS is based on an external authentication server.

Each row of the table contains access data for one server. In the search order, the primary server is queried first. If the primary server cannot be reached, secondary servers are queried in the order in which they are entered. If no server responds, there is no authentication.

##### Description

The page contains the following boxes:

- **RADIUS Authorization Mode**

  For the login authentication, the RADIUS authorization mode specifies how the rights are assigned to the user with a successful authentication.

  - conventional

    In this mode the user is logged in with administrator rights if the server returns the value "Administrative User" to the device for the attribute "Service Type". In all other cases the user is logged in with read rights.
  - Vendor specific

    In this mode the assignment of rights depends on whether and which group the server returns for the user and whether or not there is an entry for the user in the table "External User Accounts".
- **Disconnect Packet**

  When you select this check box, the device evaluates the Disconnect messages of the RADIUS server.

The table has the following columns:

- **Auth. Server Type**

  Select which authentication method the server will be used for.

  - Login

    The server is used only for the login authentication.
  - 802.1X

    The server is used only for the 802.1X authentication.
  - Login & 802.1X

    The server is used for both authentication procedures.
- **RADIUS Server Address**
    
  Enter the IPv4 address or the FQDN (Fully Qualified Domain Name) of the RADIUS server.
- **Server Port**

  Here, enter the input port on the RADIUS server. As default, input port 1812 is set. The range of values is 1 ... 65535.
- **Shared Secret**

  Enter your access ID. The range of values is 1 ... 128 characters.
- **Confirm Shared Secret**

  Enter your access ID again as confirmation.
- **Max. Retrans**

  Here, enter the maximum number of retries for an attempted request. The initial connection attempt is repeated the number of times specified here before another configured RADIUS server is queried or the login counts as having failed. As default 3 retries are set, this means 4 connection attempts. The range of values is 1 ... 5.
- **Timeout[s]**
    
  Here you enter the time for which the client waits for a reply from the RADIUS server.
- **Primary Server**

  Specify whether or not this server is the primary server. You can select one of the options "yes" or "no".
- **Test** (only available online)  
  With this button, you can test whether or not the specified RADIUS server is available. The test is performed once and not repeated cyclically.
- **Test result** (only available online)

  Shows whether or not the RADIUS server is available:

  - Failed, no test packet sent

    The IP address is not reachable.

    The IP address is reachable, the RADIUS server is, however, not running.
  - Reachable, key not accepted

    The IP address is reachable, the RADIUS server does not, however accept the shared secret.
  - Reachable, key accepted

    The IP address is reachable, the RADIUS server accepts the specified shared secret.

  The test result is not automatically updated. To delete the test result click the "Refresh" button.

#### 802.1X Authenticator (SC600)

##### Setting up network access

An end device can only access the network after the device has verified the login data of the device with the authentication server. The authentication can be via 802.1X or the MAC address.

When authenticating using 802.1X both the end device and the authentication server must support the EAP protocol (Extensive Authentication Protocol).

##### Enabling authentication for individual ports

By enabling the relevant options, you specify for each port whether or not network access protection according to IEEE 802.1X is enabled on this port.

![802.1x Authenticator - first part of the table](images/149799206539_DV_resource.Stream@PNG-en-US.png)

802.1x Authenticator - first part of the table

![802.1X Authenticator - second part of the table](images/149798235659_DV_resource.Stream@PNG-en-US.png)

802.1X Authenticator - second part of the table

##### Description of the displayed boxes

The page contains the following boxes:

- **MAC Authentication**

  Enable or disable MAC Authentication for the device.
- **802.1X Fallback Timeout [s]**

  Specify the time interval in seconds after which the device is reinitialized for 802.1X authentication at the relevant port after MAC authentication fails. The default value is 0 seconds, i.e. there is no fallback timeout and no reinitialization for the 802.1X authentication.
- **802.1X Fallback Retry Count**

  Specify how often the port is reinitialized for 802.1X authentication after MAC authentication fails.

Table 1 has the following columns:

- **1st column**

  Shows that the settings are valid for all ports of table 2.
- **802.1X Auth. Control**

  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.
- **802.1X Re-Authentication**

  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.
- **Re-Authentication Timeout**

  Specify the time interval in seconds after which the device is reauthenticated at the relevant port. The default value is 3600 seconds. If "No Change" is selected, the entry in table 2 remains unchanged.
- **Tx Timeout**

  The value specifies the period of time in seconds after which an EAP request packet is sent if no client responds. If MAC authentication is enabled, a switch is made from 802.1X authentication to MAC authentication after the third EAP request packet. The default value is 5 seconds. If "No Change" is selected, the entry in table 2 remains unchanged.
- **MAC Authentication**

  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.
- **MAC Auth only on Timeout**

  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.
- **RADIUS VLAN Assignment Allowed**

  Select the required setting. If "No Change" is selected, the entry in table 2 remains unchanged.

  > **Note**
  >
  > The VLAN assignment of RADIUS is only applied if the port has not already been configured for this VLAN. If the port VLAN ID matches the VLAN ID assigned by RADIUS, the type of membership in this VLAN must be preconfigured.
- **MAC Auth. Max Allowed Addresses**

  Specify how many MAC addresses can communicate on the port at the same time.  
  If "No Change" is selected, the entry in table 2 remains unchanged.
- **Copy to Table**
    
  When you click the button, the settings are adopted for all ports of table 2.

Table 2 has the following columns:

- **Port**

  This column lists all the ports available on this device.
- **802.1X Auth. Control**

  Specify the authentication of the port:

  - Force Unauthorized

    Data traffic via the port is blocked.
  - Force Authorized

    Data traffic via the port is allowed without any restrictions.

    Default setting
  - Auto

    End devices are authenticated on the port with the "802.1X" method.

    The data traffic via the port is permitted or blocked depending on the authentication result.
- **802.1X Re-Authentication**

  Enable this option if you want reauthentication of an already authenticated end device to be repeated cyclically.
- **Re-Authentication Timeout**

  Specify the time interval in seconds after which the device is reauthenticated at the relevant port. The default value is 3600 seconds.
- **Tx Timeout**

  The value specifies the period of time in seconds after which an EAP request packet is sent if no client responds. If MAC authentication is enabled, a switch is made from 802.1X authentication to MAC authentication after the third EAP request packet. The default value is 5 seconds.
- **MAC Authentication**

  Enable this option if you want end devices to be authenticated with the "MAC Authentication" method.

  If "Auto" is configured for "802.1x Auth. Control" and the "MAC Authentication" is enabled, the timeout for the "802.1X" procedure is 5 seconds. If manual input is necessary at a port for the authentication with the "802.1X" procedure, the 5 seconds may not be adequate. To be able to run authentication using "802.1X", disable the MAC authentication on this port.
- **MAC Auth only on Timeout**

  If this check box is selected, MAC authentication is only possible after a 802.1X timeout, but not after a failed 802.1X authentication. When the check box is not selected, MAC authentication is possible both after an 802.1X timeout and after a failed 802.1X authentication.
- **Adopt RADIUS VLAN Assignment**

  The RADIUS server informs the IE switch of the VLAN to which the port will belong. Enable this option if you want the information of the server to be taken into account.

  The port can only be assigned to the VLAN, if the VLAN has been created on the device. Otherwise Authentication is rejected.

  If during authentication a port is assigned to a VLAN dynamically using this function, assignment using the VLAN-ID or the VLAN name is possible. Configure the following values on the RADIUS server:

  - Tunnel-Type = VLAN
  - Tunnel-Medium-Type = IEEE-802
  - Tunnel-Private-Group-Id = VLAN-ID or VLAN-Name

  The IE switch distinguishes as follows:

  - VLAN ID: The RADIUS server transfers a numeric string for the parameter "Tunnel-Private-Group-Id".
  - VLAN-Name: The RADIUS server transfers an alphanumeric string for the parameter "Tunnel-Private-Group-Id".
- **Default VLAN ID**

  If a VLAN ID is transmitted to the RADIUS server during a successful authentication and the "RADIUS VLAN Assignment Allowed" check box is selected, the current PVID of the port is changed to the value transmitted by the RADIUS server. Otherwise, an "Untagged membership" of the port may be set up in the relevant VLAN to enable communication in the respective VLAN.

  The Default VLAN ID determines the assignment of the VLAN ID when the "RADIUS VLAN Assignment Allowed" check box is selected, but the RADIUS server does not send a VLAN ID after successful authentication. You have two options:

  - **The value "0" is configured for the** 
    **default VLAN ID**

    The PVID currently configured for the port continues to be used.
  - **A value in the range from "1 ... 4094" is configured for the** 
    **Default VLAN ID**

    The PVID of the port is changed to the "Default VLAN ID" configured in this column as if it had been transmitted by the RADIUS server.

  In all cases, a changed PVID is reset to the originally configured value after the device logs out. Any "Port membership" that has been set up is deleted again. This applies to both 802.1X authentication and MAC authentication.
- **MAC Auth. Max Allowed Addresses**

  - 1 - 200

    Specify how many MAC addresses can communicate on the port at the same time.

    > **Note**
    >
    > If a device uses several MAC addresses, all MAC addresses must be authenticated. Store all the MAC addresses to be authenticated on the RADIUS server. Enter the number in the "MAC Auth. Max Permitted Addresses" box.
  - 0

    You can set the value "0". This setting has the effect that after the first successful authentication of a MAC address, the port is released for all MAC addresses.

##### Configuration procedure

**Enable authentication for an individual port**

1. Select the required options in the relevant row in table 2.
2. To apply the changes, click the "Set Values" button.

**Enable authentication for all ports**

1. Select the required options in table 1.
2. Click the "Copy to Table" button. The relevant settings are adopted for all ports in table 2.
3. To apply the changes, click the "Set Values" button.

### Certificates

This section contains information on the following topics:

- [Overview](#overview-6)
- [Certificates](#certificates-2)

#### Overview

The loaded files (certificates and keys) are shown on this page. You have the following options for loading files on the device:

- System > Load&Save > HTTP
- System > Load&Save > TFTP
- System > Load&Save > SFTP

##### Description

- **Type**
    
  Shows the type of the loaded file.

  - CA Cert  
    The CA certificate is signed by a CA (Certification Authority).
  - Machine certificate
  - Key File
  - Remote Cert  
    Partner certificate
- **Filename**

  Shows the file name.
- **Status**

  Shows whether the certificate is valid or has already expired.
- **Subject DN**

  Shows the name of the applicant.
- **Issuer DN**

  Shows the name of the certificate issuer.
- **Issue Date**

  Shows the start of the period of validity of the certificate
- **Expiry Date**

  Shows the end of the period of validity of the certificate.
- **Used**

  Shows which function uses the certificate.

#### Certificates

The format of the certificate is based on X.509, a standard of the ITU-T for creating digital certificates. This standard describes the schematic structure of X509 certificates. You will find further information on this on the Internet at "http://www.itu.int".

On this page, the content of the following structure elements can be displayed. If the structure element does not exist or is not completed in the selected certificate, nothing is shown in the box on the right. Certain entries can only be edited if they are supported.

##### Description

- **Information** (SC-600)

  Shows whether a certificate is loaded; if this is the case, the information on the respective certificate is displayed.
- **Filename**

  Select the required certificate.
- **Type**
    
  Shows the type of the loaded file.

  - CA Cert  
    The CA certificate is signed by a CA (Certification Authority).
  - Machine certificate
  - Key File
  - Remote Cert  
    Partner certificate
- **Subject DN**

  Shows the name of the applicant.
- **Issuer DN**

  Shows the name of the certificate issuer.
- **Subject Alternate Name**

  If it exists, an alternative name of the applicant is displayed.

- **Issue Date**

  Shows the start of the period of validity of the certificate
- **Expiry Date**

  Shows the end of the period of validity of the certificate.
- **Serial Number**

  Shows the serial number of the certificate.
- **Used**

  Shows which function uses the certificate.
- **Crypto Algorithm**

  Shows which cryptographic method is used.
- **Key Usage**

  Shows the purpose that the key belonging to the certificate is used for, e.g. to verify digital signatures.
- **Extended Key Usage**

  Shows whether the purpose is additionally restricted, e.g. only to verify signatures of the CA certificate.
- **Key File**

  Shows the key file.
- **Certificate Revocation List 1st URL**

  Enter the URL with which the revocation list can be called up. Can only be edited if supported by the certificate.
- **Certificate Revocation List 2nd URL**

  Enter an alternative URL. If the revocation list cannot be called up using the 1st URL, the alternative URL is used. Can only be edited if supported by the certificate.
- **Certificate**

  Shows the name of the certificate.
- **Passphrase**
    
  Enter the password for the certificate. Can only be edited if the encrypted file is password protected.
- **Passphrase Confirmation**
    
  Enter the password again. Can only be edited if the encrypted file is password protected.

### Firewall

This section contains information on the following topics:

- [General](#general-4)
- [Predefined IP rules](#predefined-ip-rules)
- [Dynamic Rules](#dynamic-rules)
- [IP Services](#ip-services)
- [ICMP Services](#icmp-services)
- [IP Protocols](#ip-protocols)
- [IP Rules](#ip-rules)
- [Pre-defined MAC rules (SC-600)](#pre-defined-mac-rules-sc-600)
- [MAC services (SC-600)](#mac-services-sc-600)
- [MAC rules (SC-600)](#mac-rules-sc-600)
- [State Synchronization (SC600)](#state-synchronization-sc600)

#### General

On this page, you activate the firewall.

> **Note**
>
> Please remember that if you disable the firewall, your internal network is unprotected.

##### Description

The page contains the following:

- **Activate Firewall**

  When enabled, the firewall is active.
- **TCP Idle Timeout [s]**

  Enter the required time in seconds. If no data exchange takes place, the TCP connection is terminated automatically when this time has elapsed.

  The range of values is 1 to 21474836.

  Default setting: 86400 seconds
- **UDP Idle Timeout [s]**
    
  Enter the required time in seconds. If no data exchange takes place, the UDP connection is terminated automatically when this time has elapsed.

  The range of values is 1 to 21474836.

  Default setting: 300 seconds
- **ICMP Idle Timeout [s]**
    
  Enter the required time in seconds. If no data exchange takes place, the ICMP connection is terminated automatically when this time has elapsed.

  The range of values is 1 to 21474836.

  Default setting: 300 seconds
- **Strict State Check** (SC600)

  When enabled, the firewall only forwards packets to the communication partner that can be assigned to a connection. Packets that cannot be assigned to a connection are discarded. To this end, the firewall checks the status of the connection, for example, whether a three-way handshake has been performed.

  When disabled, the firewall also forwards packets that cannot be assigned to a connection if the corresponding firewall rule has been created. This can be used, for example, in "Asymmetric routing" when the firewall does not recognize all packets of a connection.

#### Predefined IP rules

The page contains predefined IP packet filter rules. If you create your own IP packet filter rules, these have a higher priority than the predefined IP packet filter rules.

Here, you can set which services of the device should be reachable from which interface/subnet.

##### Description

- **Interface**

  The list is dynamic.

  Interface to which the setting relates.

  - VLANx

    Allows access from the IP subnet to the device. VLANs with configured IP subnet are available.
  - ppp2 (S615)

    Allows access from the WAN interface to the device.
  - SINEMA RC

    Allows access from the SINEMA RC server to the device. For S615: Only available with KEY-PLUG SINEMA RC.
  - OpenVPN connection, IPsec VPN connection (S615)

    Allows the VPN tunnel partners reachable via the VPN connection to access the device. If you have created a VPN connection, the connection name is displayed in the list.
- **IP Version** (S615)

  Shows the IP version to which the firewall rules apply.
- Access to the following IP services is permitted:

  - All  
    All predefined IP services
  - HTTP  
    For access to Web Based Management.
  - HTTPS  
    For secure access to Web Based Management.

    > **Note**
    >
    > **HTTP and HTTPS disabled**
    >
    > If you disable HTTP and HTTPS, the WBM of the device can no longer be reached.
    >
    > **HTTPS disabled**
    >
    > When you disable HTTPS, you can only access the WBM using HTTP. This assumes that "HTTP & HTTPS" is set in "System > Configuration > HTTP Services". If "Redirect HTTP to HTTPS" is set, for example, access via HTTP cannot be redirected to HTTPS. This means that the WBM of the device can no longer be reached.
  - DNS  
    DNS queries to the device. Necessary only if the "DNS-Relay" function is enabled on the device.
  - SNMP  
    Incoming SNMP connections. Required, for example, to access the SNMP information of the device using a MIB browser.
  - Telnet (S615)  
    For unencrypted access to the CLI.
  - IPsec VPN   
    Allows IKE (Internet Key Exchange) data transfer from the external network to the device. Necessary if an IPsec VPN remote station needs to establish a connection to this device.
  - SSH  
    For encrypted access to the CLI.
  - DHCP   
    Access to the DHCP server or the DHCP client.
  - Ping   
    Access to the ping function.
  - System Time

    Access to NTP and SNTP.
  - Cloud Connector (S615)

    Access to the integrated TIA Portal Cloud Connector Server and the devices accessible via the interface.
  - VRRP

    Access to VRRPv3.
  - TCP Event (S615)

    For incoming TCP packets. Required to trigger the "Sleep Mode" function, for example.
  - VXLAN

    To establish the VXLAN tunnel and receive the frames. Necessary if the tunnel endpoint establishes a connection to this device.

#### Dynamic Rules

On this page, you define dynamic rule sets. Firewall rules that are required for remote access, for example, can be summarized with a rule set.

You can assign a rule set to one or more users. If login of this user was successful, the firewall rule set intended for this user is enabled.

A timer is started after login. When the time expires, the user is automatically logged out from the device.

You can also control the rule sets over time. A start time and an end time are configured. Between these times, the firewall rules assigned to the rule set are enabled.

##### Description

**"Rule set" area**

- **Name**

  Define a unique name for the rule set. If you click the "Create" button, a new row with a unique number is created.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **No.**

  Shows the unique number of the entry.
- **Name**

  Name of the rule set. The name can be changed if required.
- **Comment**

  Comment that describes the rule set in more detail.
- **Timeout**

  Access is time-limited. Specify the duration of the access. If needed, the user can extend the access time via the "Reset Timeout" button on the "Dynamic Firewall Rules Information" page.

**"Rule Set Assignment" area**

- **Type**

  Specify which rule set will be assigned to whom. The display of the following table depends on the selection for "Type".

  - User Accounts

    The rule set is enabled through a local user account.
  - Digital Input

    The rule set is executed by controlling the digital input. The prerequisite for this is that the entry "Digital In" is enabled for the "Firewall" event under "System > Events > Configuration".
  - RADIUS role

    The rule set is enabled through a RADIUS role.
  - RADIUS user

    The rule set is enabled through a RADIUS user.
  - Time triggered

    Enforcement of the rule set is time-triggered.

The "User Account" table contains the following columns:

- User Account

  Only users with the remote access "only" or "additional" are displayed.
- Role

  Shows the role of the user.
- Rule Set

  Define the rule set that is valid for this user.
- Combined with

  Combines the user login with an event, for example, the "Digital Input" event. To log in to the WBM page for the dynamic firewall, voltage must be present at the digital input and user login must be successful.
- Remaining Time (only available online)

  When this user is logged on, the remaining time for access is displayed.
- Force Deactivate (only available online)

  A user with administrator rights can log off the active user with this button.

The "Digital Input" table contains the following columns:

- Digital In

  The available digital inputs
- Rule Set

  Define the rule set that is controlled via the digital input.
- Dynamic Source (Range)

  Enter the IP address or an IP range that is allowed to send IP packets.
- State (only available online)

  Shows the remaining time for access.

The "RADIUS role" table contains the following columns:

- Role

  Shows the role name. Only roles with the remote access "additional" are displayed. The prerequisite is that the role was created on the RADIUS server and RADIUS users were assigned to the role.
- Rule Set

  Define the rule set that is valid for this RADIUS role.
- Combined with

  Combines the login with an event, e.g. the "Digital In" event. To log in to the WBM page for the dynamic firewall, voltage must be present at the digital input and login must be successful.
- Counter (only available online)

  After successful login, the number of users active via RADIUS that are assigned to the RADIUS role is displayed.
- Force Deactivate (only available online)

  A user with administrator rights can log out the RADIUS role with this button.

The "RADIUS User" table contains the following columns:

- Users

  Shows the users assigned to the role.

  A role with the remote access "additional" is created on the device and assigned to a group. The names of the group must match exactly the names of the user groups on the RADIUS server.
- Role

  The role assigned to the RADIUS user.
- Remaining Time (only available online)

  When this user is logged on, the remaining time for access is displayed.
- Force Deactivate (only available online)

  A user with administrator rights can log out the RADIUS role with this button.

The "Time triggered" table contains the following columns:

- Time triggered

  Index of the entry
- Rule Set

  Define the rule set that is time triggered.
- Combined with

  Combines the time triggering with an event, for example, the "Digital In" event. To log in to the WBM page for the dynamic firewall, voltage must be present at the digital input and login must be successful.
- Cycle

  Specify the enforcement cycle for the time triggering.

  - Daily
  - Weekly
  - Monthly
- Days

  If "Weekly" or "Monthly" is set for the cycle, specify the days.

  Enter the days separated by commas, e.g. 1,3,4

  - Weekly: 1 - 7
  - Monthly: 1 - 31
- Dynamic Source (Range)

  - Individual IP address: Specify the IP address.
  - IP range: Specify the range with start address "-" end address, e.g.

    IPv4:192.168.100.10 - 192.168.100.20

    IPv6: fe80:: - febf::
  - All IP addresses:

    IPv4: " 0.0.0.0/0"

    IPv6: "::"
  - If the rule set is enabled by a user, the placeholder DYNAMIC is replaced by the IP address of the end device used.
- Start time

  Enter the start time in the format HH:MM.
- End time

  Enter the end time in the format HH:MM.
- Activate (only available online)

  When enabled, the rule set is time-triggered. The connection is briefly interrupted when the time-triggered firewall rules are initiated.

#### IP Services

On this page, you define the IP services. Using the IP service definitions, you can define firewall rules for specific services. You select a name and assign the service parameters to it. When you configure the IP rules, you simply use this name.

##### Description

The page contains the following:

- **Service Name**

  Enter the name of the IP service. The name must be unique.

The table contains the following columns:

- **Select**
    
  Select the check box in the row to be deleted.
- **Service Name**

  Shows the name of the IP service.
- **Transport**
    
  Specify the protocol type.

  - UDP  
    The rule applies only to UDP frames.
  - TCP  
    The rule applies only to TCP frames.
- **Source Port (Range)**
    
  Enter the source port. The rule applies specifically to the specified port.

  - If the rule is intended to apply to a port range, enter the range with start port "-" end port, for example 30 - 40.
  - If the rule is intended to apply to all ports, enter "*".
- **Destination Port (Range)**
    
  Enter the destination port. The rule applies specifically to the specified port.

  - If the rule is intended to apply to a port range, enter the range with start port "-" end port, for example 30 - 40.
  - If the rule is intended to apply to all ports, enter "*".

#### ICMP Services

On this page, you define ICMP services. Using the ICMP service definitions, you can define firewall rules for specific services. You select a name and assign the service parameters to it. When you configure the IP rules, you simply use this name.

##### Description

The page contains the following:

- **Service Name**

  Enter a name for the ICMP service. The name must be unique.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Service Name**

  Shows the name of the ICMP service.
- **Protocol**

  Shows the version of the ICMP protocol.
- **Type**
    
  Specify the ICMP packet type. A few examples are shown below:

  - Destination Unreachable  
    IP frame cannot be delivered.
  - Time Exceeded  
    Time limit exceeded
  - Echo-Request  
    Echo request, better known as ping.
- **Code**
    
  The code describes the ICMP packet type in greater detail. The selection depends on the selected ICMP packet type.   
  With "Destination Unreachable", for example "Code 1" host cannot be reached.

#### IP Protocols

On this page, you can configure user-defined protocols, e.g. IGMP for multicast groups. You select a protocol name and assign the service parameters to it. When you configure the IP rules, you simply use this protocol name.

##### Description

The page contains the following:

- **Protocol Name**

  Enter a name for the protocol.

The page contains the following check boxes:

- **Select**

  Select the check box in the row to be deleted.
- **Protocol Name**

  Shows the protocol name.
- **Protocol Number**

  Enter the protocol number, for example 2. You will find list of the protocol numbers on the Internet pages of iana.org

#### IP Rules

On this page you specify your own IP packet filter rules for the firewall.

The IP packet filer rules set here have priority:

- over the predefined IP packet filter rules (predefined IP) and
- over the IP packet filter rules created automatically due to a connection configuration (SINEMA RC).

##### Description of the displayed boxes

- **IP Version**

  The version of the IP protocol.

  S615: Specify the IP version for which the firewall rule is valid.
- **Rule set**

  Select the required rule set. Only the IP rules that are assigned to this rule set are then displayed in the table, provided that "Show all" is disabled.
- **Show all**

  When enabled, all available IP rules are displayed. With the "Assign" setting, you assign an IP rule to the selected rule set.

The table contains the following columns:

- **Select**
    
  Activate the check box in the row to be deleted.
- **Protocol**
    
  Shows the version of the IP protocol.
- **Action**

  Select how incoming IP packets are handled:

  - "Accept" – The data packets can pass through.
  - "Reject" – The data packets are rejected, and the sender receives a corresponding message.
  - "Drop" – The data packets are discarded without any notification to the sender.
- **From / To**
    
  Specify the communications direction of the IP rule.

  - VLANx: VLANs with configured subnet
  - Device: Connection to the device
  - SINEMA RC: Connection to SINEMA RC Server
  - IPsec: Either all IPsec VPN connections (all) or a specific IPsec VPN connection
  - ppp2: WAN interface (S615)
  - OpenVPN: Either all OpenVPN connections (all) or a specific OpenVPN connection (S615)
- **Source (Range)**

  Enter the IP address or an IP range that is allowed to receive IP packets.

  - Individual IP address

    Specify the IP address.
  - IP range

    IPv4: Specify the range with the start address "-" end address, e.g. 192.168.100.10 - 192.168.100.20.

    IPv6 (S615): fe80:: - febf::
  - All IP addresses

    IPv4: Specify "0.0.0.0/0".

    IPv6 (S615): "::"
  - DYNAMIC

    If the rule set is activated by a user, the DYNAMIC placeholder is replaced by the IP address of the terminal device used.

    > **Note**
    >
    > **Digital input and DYNAMIC placeholder**
    >
    > If the rule set is executed by controlling the digital input, the DYNAMIC placeholder is replaced by the setting for "Dynamic Source (Range)". You configure the setting in "Security > Firewall > Dynamic Rules".
- **Destination (Range)**

  Enter the IP address or an IP range that is allowed to receive IP packets.

  - Individual IP address

    Specify the IP address.
  - IP range

    IPv4: Specify the range with the start address "-" end address, e.g. 192.168.100.10 - 192.168.100.20.

    IPv6 (S615): fe80:: - febf::
  - All IP addresses

    IPv4: Specify "0.0.0.0/0".

    IPv6 (S615): "::"
- **Service**
    
  Select the service or the protocol name for which this rule is valid.
- **Log**
    
  Specify whether or not there should be a log entry every time the rule comes into effect and specify the severity of the event.  
  The following settings are available:

  - none  
    The rule coming into effect is not logged.
  - info / warning / critical  
    The rule coming into effect is logged with the selected event severity. The log file is displayed in "Information" > "Log Tables" > "Firewall Log".
- **Precedence**
    
  In ascending order starting with 0, you define the sequence in which the IP rules of the firewall are processed.
- **Bandwidth (kbps)** (SC-600)

  Set options for bandwidth limitation. Can only be set if "Accept" is selected as action. A packet passes through the firewall if the Accept rule applies and the permitted bandwidth for this rule has not yet been exceeded.

- **Assign**

  To assign the IP rules to the selected rule set, activate the setting for the desired IP rules and click the "Set Values" button.
- **Assigned**

  Shows the rule set to which this IP rule is assigned. The IP rules can also be assigned to multiple rule sets. If the IP rule is assigned to all rule sets, "all" is displayed.
- **Name**

  Shows who created the IP rule.

  - NETMAP - automatically created firewall rule

#### Pre-defined MAC rules (SC-600)

The WBM page contains pre-defined MAC packet filter rules. If you create your own MAC packet filter rules, these have a higher priority than the pre-defined MAC packet filter rules. On this page, you can set which MAC services of the device should be reachable from which interface.

##### Description

- **Interface**

  Interface to which the settings relate. The list of interfaces/subnets is dynamic and is based on the settings from "Layer 3 > Subnet".
- Access to the following MAC services is permitted:

  - All  
    All predefined MAC services, no filtering.
  - ARP

    Access via ARP to the device or bridged subnets is permitted.

    Changes to this setting can have the result that the device is no longer reachable.
  - DCP

    Access via DCP to the device or bridged subnets is permitted.
  - IPv4

    Access via IPv4 to the device, bridged or routed subnets is permitted.

#### MAC services (SC-600)

On this page, you define MAC services. Using the MAC service definitions, you can define firewall rules for specific services. You select a name and assign the service parameters to it. Simply use this name when you configure the MAC rules.

##### Description

The page contains the following:

- **Name**

  Enter a name for the MAC service. The name must be unique.
- **Protocol**

  Selection of the protocol type:

  | Protocol | Description |
  | --- | --- |
  | ARP | Frames with the following property: Ethertype=0x0806 |
  | DCP | The DCP protocol is used by SINEC PNI to set the IP parameters (node initialization) of SIMATIC NET network components. |
  | PNIO | Frames with the following property: Ethertype = 0x8892 |
  | ISO | Frames with the following properties: Lengthfield <= 05DC (hex), DSAP=userdefined, SSAP=userdefined, CTRL=userdefined |
  | SNAP | Frames with the following properties: Lengthfield <= 05DC (hex), DSAP=0xAA (hex), SSAP=0xAA (hex), CTRL=0x03 (hex), OUI=userdefined, OUI-Type=userdefined |
  | Users | User-specific rules with the following inputs:  Type: >=0x0600  Length: <= 0x05DC |
  | SICLOCK | For filtering SiCLOCK time-of-day frames. |
  | IPv4 | Frames with the following property: Ethertype=0x0800 |

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the MAC service.
- **Protocol**

  Shows the name of the MAC protocol.

Depending on the protocol, the following inputs are necessary:

- For Ethernet protocols:

  - Type/length
- For ISO-LLC protocols:

  - DSAP: Destination Service Access Point: LLC recipient address
  - SSAP: Source Service Access Point: LLC sender address
  - CTRL: LLC Control Field
- For SNAP:

  - OUI: Organizationally Unique Identifier: the first three bytes of the MAC address = Manufacturer identification
  - OUI Type: Protocol type/identification

#### MAC rules (SC-600)

By default, MAC packet filter rules exist on the device that permit the exchange of ARP frames between device and vlan1 or vlan2. You can define your own ARP rules by selecting the entry "ARP" as protocol in a MAC packet filter rule. Your own ARP rules should also take into account the PC with which the device is configured.

##### Meaning

MAC packet filter rules are processed based on the following evaluations:

- Parameters entered in the rule
- Sequence of the rule within the rule set

##### Description of the displayed boxes

The table contains the following columns:

- **Select**
    
  Activate the check box in the row to be deleted.
- **Protocol**
    
  Shows the version of the MAC protocol.
- **Action**

  Select how incoming MAC packets are handled:

  - "Accept" – The data packets can pass through.
  - "Drop" – The data packets are discarded without any notification to the sender.
- **From / To**
    
  Specify the communications direction of the MAC rule.

  - VLANx: VLANs with configured subnet
- **Source**

  Enter the source address of the MAC packets.
- **Destination**

  Enter the destination address of the MAC packets.
- **Service**
    
  Select the service or the protocol name for which this rule is valid.
- **Log**
    
  Specify whether or not there should be a log entry every time the rule comes into effect and specify the severity of the event.  
  The following settings are available:

  - none  
    The rule coming into effect is not logged.
  - info / warning / critical  
    The rule coming into effect is logged with the selected event severity. The log file is displayed in "Information > Log Tables > Firewall Log".
- **Precedence**
    
  In ascending order starting with 0, you define the sequence in which the MAC rules of the firewall are processed.
- **Bandwidth (kbps)**

  Option for setting a bandwidth limitation. Can only be entered if "Accept" is selected for the action. A packet passes through the firewall if the Accept rule applies and the permitted bandwidth for this rule has not yet been exceeded.
- **Comment**

  If needed, enter a comment.

#### State Synchronization (SC600)

On this WBM page, you set the firewall states of two SC600 that are synchronized with each other via the network.

When the firewall permits passage of a network packet, a firewall state is created for this event. This firewall state is required so that the reply to a packet can pass through the firewall without having to create an additional rule for it. Synchronization of the firewall state transfers this information to another device. In connection with VRRP, this ensures that an established connection must not be set up again but that the existing firewall state is being used.

The outgoing queries are logged by the firewall in dynamic state tables. Direct queries from the external network without previous query, that is, without corresponding entry in the state table, are automatically blocked.

> **Note**
>
> **Protect connections to the Firewall State Sync**
>
> The Firewall State Sync does not use any encryption or authentication. The connection to the synchronization between the two firewalls therefore needs to be specifically protected.
>
> If possible, connect the two firewalls directly via dedicated VLAN interfaces. If this connection cannot be protected from external access, create an IPsec VPN connection for synchronization.

![Figure](images/148067502219_DV_resource.Stream@PNG-en-US.png)

##### Description of the displayed boxes

The table contains the following columns:

- **Activate State Sync**
    
  Activates the Firewall State Sync. When you enable this option, a firewall rule is automatically created.
- **Local Interface**

  Select the interface via which the firewall state is being sent in case of a change.
- **Local IP Address**

  Enter the IP address of the node in the local network.
- **Sync Partner IP**
    
  Enter the IP address of the synchronization partner.
- **Port Number Sync Partner**

  Enter the port of the synchronization partner.  
  Port 3780 is assigned as default.

### IPsec VPN

This section contains information on the following topics:

- [Overview](#overview-7)
- [General](#general-5)
- [Remote End](#remote-end)
- [Connections](#connections)
- [Authentication](#authentication)
- [Phase 1](#phase-1)
- [Phase 2](#phase-2)

#### Overview

In "Security > IPsec VPN" you can configure the parameters for establishing IPsec VPN connections manually.

##### Alternative configuration via VPN groups

As an alternative, you can configure IPsec connections via VPN groups, see section [IPsec VPN tunnel: Creating and assigning VPN groups](Configuring%20security.md#ipsec-vpn-tunnel-creating-and-assigning-vpn-groups). During the configuration via VPN groups the remote addresses and remote subnets are determined by STEP 7 based on the interface names:

- Interface name "INT": STEP 7 handles the interface as an internal interface.
- Interface name "EXT": STEP 7 handles the interface as an external interface.

When adding devices to VPN groups STEP 7 only creates VPN connections between the external interfaces. Only the local subnets on the internal interfaces are therefore connected together via VPN. Additional VPN connections need to be configured manually.

##### Points to note when configuring via VPN groups

Compared with SCALANCE S-600 V3 devices, the following special features apply:

- You specify permission to initiate connection establishment with the assignment to VPN groups.
- In the connection-specific VPN settings the device is displayed as a connection partner but cannot be edited. When the device is selected, the interface can be adapted to other partner devices.
- In terms of the VPN mode, the device always behaves as a routing device.
- The properties of a VPN group are adopted in the local properties of VPN group members. Related to the following parameters, the properties of a VPN group can be overwritten locally.

  - Phase 1: Keying Tries, DPD, DPD Period, DPD Timeout
  - Phase 2: Lifebytes, Protocol, Port (Range), Auto Firewall Rules

#### General

On the page, you configure the basic settings for VPN.

##### Description

The page contains the following:

- **Activate IPsec VPN**

  Enable or disable the IPsec protocol for VPN.
- **Enforce strict CRL Policy**

  When enabled, the validity of the certificates is checked based on the CRL (Certificate Revocation List). The certificate revocation list lists the certificates issued by the certification authority that have lost their validity before the set expiry date. You configure the certificate revocation list to be used on the page "[Certificates](#certificates-2)".
- **NAT Keep Alive Time Interval**

  Specify the time interval at which Keep Alive frames are sent. If there is a NAT device between two VPN endpoints, when there is inactivity, the connection is deleted from its dynamic NAT table. To prevent this, keepalives are sent.
- **IKEv2 DPD Retries**

  Specify the number of allowed failed attempts after which the IKEv2 connection is considered disrupted. The setting applies to all IKEv2 connections.
- **IKEv2 DPD Retry Interval[s]**

  Specify the interval at which the failed attempts are sent.

#### Remote End

On this page, you configure the remote partner (VPN end point).

##### Description

The page contains the following:

- **Remote End Name**

  Enter the name of the remote station and click "Create" to create a new remote station.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the partner.
- **Remote Mode**

  Specify the role the remote stations will adopt.

  - Roadwarrior  
    The reachable remote addresses are entered. The reachable remote subnets are learned from the partner.
  - Standard   
    The reachable remote address and the reachable remote subnets are entered permanently.
- **Remote Type**

  Specify the type of remote station address.

  - Manual

    The address of the partner is known. The device can either establish the VPN connection actively as a VPN client or wait passively for connection establishment by the partner.
  - Any

    Accepts the connection from remote stations with any IP address. The device can only wait for VPN connections but cannot establish a VPN tunnel as the active partner.
- **Remote Address**

  Can only be edited with the remote type "Manual".

  - In standard mode, enter the WAN IP address or the DDNS host name of the partner. The network mask is always 32
  - In Roadwarrior mode, you can specify either the address of the partner or enter an IP range from which connections will be accepted.
- **Remote Subnet**

  - In standard mode, enter the remote subnet of the remote station. Use the CIDR notation.

    Multiple subnets can be used only with IKv2. Then enter the subnets separated by a comma.
  - In Roadwarrior mode, the remote station informs the device of its accessible subnets and the device learns them.
- **Virtual IP Mode**

  Specify whether or not the remote station is offered a virtual IP address.

  The following options are available:

  - None  
    No virtual IP address. The VPN tunnel is established dynamically to the internal IP address of the remote station.
  - User defined IPv4  
    The virtual IP address is from the band specified in "Virtual IP".
- **Virtual IP**
    
  Specify the subnet (CIDR) from which the remote station is offered a virtual IP address.   
  Can only be edited if "user defined IPv4" is selected in "Virtual IP Mode".

#### Connections

On this page, you configure the basic settings for the VPN connection. With these settings, the device (local endpoint) can establish a secure VPN tunnel to the partner. You specify the security settings on the WBM page "Authentication".

> **Note**
>
> If you use "NETMAP"
>
> - only auto firewall rules are supported
> - for "Operation" the setting "on demand" cannot be selected.

> **Note**
>
> **Several IPsec VPN connections via the same VPN endpoint**
>
> If you have created IPsec VPN connections to different remote subnets via the same VPN endpoint, the first VPN connection configured (lowest index) is the main connection (parent).
>
> Via the main connection all other IPsec VPN connections (children) ate created and established. If all VPN tunnels are now established and the main connection is terminated, all child connections are interrupted. When the DPD timeout has elapsed, all IPsec VPN connections are re-established via the main connection.
>
> If only one child connection is terminated, the main connection and the other child connections are retained.

##### Description

The page contains the following boxes:

- **Connection name**

  Enter a name for the VPN connection and click "Create" to create a new connection.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**
    
  Shows the name of the VPN connection.
- **Operation**
  Specify who establishes the VPN connection.

  - Disabled

    The VPN connection is disabled.
  - start  
    The device attempts to establish a VPN connection to the partner.
  - wait

    The device waits for the remote station to initiate the connection establishment.
  - on demand

    The VPN connection is established when necessary.
  - start on DI

    If the event "Digital In" occurs the device attempts to establish a VPN connection to the remote station.

    This is on condition that the event "Digital In" is forwarded to the VPN connection. To do this in "System > Events> Configuration" activate "VPN Tunnel" for the "Digital In" event.
  - wait on DI

    If the event "Digital In" occurs, the device waits for the remote station to initiate connection establishment.

    This is on condition that the event "Digital In" is forwarded to the VPN connection. To do this in "System > Events> Configuration" activate "VPN Tunnel" for the "Digital In" event.
- **Keying Protocol**

  Specify whether IKEv2 or IKEv1 will be used.
- **Tunnel Interface**

  Select the interface via which the VPN tunnel is established. With the default value "auto", the interface is automatically determined via the routing.
- **Remote End**

  Select the required remote station. Only partners can be configured that have been configured on the "Remote End" WBM page.
- **Local Subnet**

  Enter the local subnet. Use the CIDR notation. The local network can also be a single PC or another subset of the local network.
- **Request Virtual IP**

  When enabled, a virtual IP address is requested from the remote station during connection establishment.
- **Timeout [sec]**

  Only necessary with the "on demand" setting. Enter the interval after which the VPN connection will be terminated. If no packets are sent during this time, the VPN connection is automatically terminated.

#### Authentication

On this page, you specify how the VPN connection partners authenticate themselves with each other.

##### Description

The table contains the following columns:

- **Name**
    
  Shows the name of the VPN connection to which the settings relate.
- **Authentication**
    
  Select the authentication method. For the VPN connection, it is essential that the partner uses the same authentication method.

  - Disabled  
    No authentication method is selected. Connection establishment is not possible.
  - Remote Cert  
    The remote certificate is used for authentication. You specify the certificate in "Remote Certificate"
  - CA Cert  
    The certificate of the certification authority is used for authentication. You specify the certificate in "CA Certificate". If you want to establish an IPsec connection to SINEMA RC, you need to add the certificate later via the WBM and download it to the device.
  - PSK  
    A key is used for authentication. You configure the key in "PSK".

    > **Note**
    >
    > For this "PSK" authentication method, specify the "Local ID" and "Remote ID". If the entries remain empty, IPSec uses the IP address of the interface as the ID and prevents the VPN tunnel from being set up.
- **CA Certificate**
    
  Select the certificate. Only loaded certificates can be selected.
- **Local Certificate**
    
  Select the machine certificate. Only the device certificates generated by the TIA Portal can be selected.

  You load the certificates onto the device with "System > Load&Save". The loaded certificates and key files are shown on the WBM page "Security > Certificates".
- **Local ID**
    
  Enter the local ID from the partner certificate. Only when you use the partner certificate can you leave the box empty. The box is automatically filled with the value from the partner certificate.
- **Remote Certificate**
    
  Select the remote station certificate. Only the partner certificates generated by the TIA Portal can be selected.

  You load the certificates onto the device with "System > Load&Save". The loaded certificates and key files are shown on the WBM page "Security > Certificates".
- **Remote ID**
    
  Enter the "Distinguished Name" or "Alternate Name" from the partner certificate. Only when you use the partner certificate can you leave the box empty. The box is automatically filled with the value from the partner certificate.
- **PSK**
    
  Enter the key.
- **PSK Confirmation**
    
  Repeat the key.

#### Phase 1

##### Phase 1: Encryption agreement and authentication (IKE = Internet Key Exchange)

On this page, you set the parameters for the protocol of the IPsec key management. The key exchange uses the standardized IKE method for which you can set the following protocol parameters.

##### Description

The table contains the following columns:

- **Name**

  Shows the name of the VPN connection to which the settings relate.
- **Default Ciphers**

  When enabled, a preset list is transferred to the VPN connection partner during connection establishment. The list contains combinations of the three algorithms (Encryption, Authentication, Key Derivation). To establish a VPN connection, the VPN connection partner must support at least one of these combinations. The selection depends on the key exchange method. Further information can be found in the section "IPsec VPN"
- **Encryption**

  For phase 1, select the required encryption algorithm. Can only be selected if "Default Ciphers" is disabled.   
  The selection depends on the key exchange method. Further information can be found in the section "IPsec VPN".

  > **Note**
  >
  > The AES modes CCM and GCM contain separate mechanisms for authenticating data. If you use a mode AES x CCM for "Encryption", this is also used for authentication. Then only the pseudo random function will be derived from the "Authentication" parameter. So that a VPN connection can be established, all devices need to use the same settings.
- **Authentication**

  Specify the method for calculating the checksum. Can only be selected if "Default Ciphers" is disabled.   
  The following methods are supported:

  - MD5
  - SHA1
  - SHA512
  - SHA256
  - SHA384
- **Key derivation**

  Select the required Diffie-Hellmann group (DH) from which a key will be generated. Can only be selected if "Default Ciphers" is disabled.

  The following DH groups are supported:

  - DH Group 1
  - DH Group 2
  - DH Group 5
  - DH Group 14
  - DH Group 15
  - DH Group 16
  - DH Group 17
  - DH Group 18
- **Keying Tries**

  Enter the number of repetitions for a failed connection establishment. If you enter the value 0, the connection establishment will be attempted endlessly.
- **Lifetime [min]**

  Enter a period in minutes to specify the lifetime of the authentication. When the time has elapsed, the VPN endpoints involved must authenticate themselves with each other again and generate a new key.
- **DPD**

  When enabled, DPD (Dead Peer Detection) is used. Using DPD, it is possible to find out whether the VPN connection still exists or whether it has aborted.

  > **Note**
  >
  > Sending DPD queries increases the amount of data sent and received. This can lead to increased costs.
- **DPD Period [sec]**

  Enter the period after which DPD requests are sent. These queries test whether or not the remote station is still available
- **DPD Timeout [sec]**

  Only adjustable for IKEv1. For IKEv2, configure the setting under "Security > IPsec > General".

  Enter a period. If there is no response to the DPD queries, the connection to the remote station is declared to be invalid after this time has elapsed.

  > **Note**
  >
  > To avoid unwanted connection breakdowns, set the DPD timeout significantly higher than the DPD period. We recommend setting it at least 2 minutes longer than the DPD period.
- **Aggressive Mode**

  - Disabled  
    Main Mode is used
  - Enabled   
    Aggressive Mode is used

  The difference between main and aggressive mode is the "identity protection" used in main mode. The identity is transferred encrypted in main mode but not in aggressive mode.

#### Phase 2

##### Phase 2: Data exchange (ESP = Encapsulating Security Payload)

On this page, you set the parameters for the protocol of the IPsec data exchange. The entire communication during this phase is encrypted using the standardized security protocol ESP for which you can set the following protocol parameters.

##### Description

The table contains the following columns:

- **Name**

  Shows the name of the VPN connection to which the settings relate.
- **Default Ciphers**

  When enabled, a preset list is transferred to the VPN connection partner during connection establishment. The list contains combinations of the three algorithms (Encryption, Authentication, Key Derivation). To establish a VPN connection, the VPN connection partner must support at least one of these combinations. Further information can be found in the section "IPsec VPN".
- **Encryption**

  For phase 2, select the required encryption algorithm. Can only be selected if "Default Ciphers" is disabled.   
  Further information can be found in the section "IPsec VPN".

  > **Note**
  >
  > The AES modes CCM and GCM contain separate mechanisms for authenticating data. If you use a mode AES x CCM or AES x GCM for "Encryption", this will also be used for authentication. Then only the pseudo random function will be derived from the "Authentication" parameter.
- **Authentication**

  Specify the method for calculating the checksum. Can only be selected if "Default Ciphers" is disabled.   
  The following methods are supported:

  - MD5
  - SHA1
  - SHA512
  - SHA256
  - SHA384
- **Key Derivation (PFS)**

  The device supports Diffie-Hellmann key exchange (DH) with the Perfect Forward Secrecy (PFS) property.

  Select the desired DH group from which a key is generated. Can only be selected if "Default Ciphers" is disabled.

  The following DH groups are supported:

  - None: For phase 2, no separate keys are exchanged. This disables PFS.
  - DH Group 1
  - DH Group 2
  - DH Group 5
  - DH Group 14
  - DH Group 15
  - DH Group 16
  - DH Group 17
  - DH Group 18
  > **Note**
  >
  > So that a VPN connection can be established, all devices need to use the same settings or provide compatible key procedures..
- **Lifetime [min]**

  Enter a period in minutes to specify the lifetime of the agreed keys. When the time expires, the key is renegotiated.
- **Lifebytes**
    
  Enter the data limit in bytes that specifies the lifetime of the agreed key. When the data limit is reached, the key is renegotiated.
- **Protocol**

  Specify the protocol for which the VPN connection is valid e.g. UDP, TCP, ICMP. If the setting is intended to apply to all protocols, enter "*".
- **Port (Range)**

  Specify the port via which the VPN tunnel can communicate. The setting applies specifically to the specified port

  - If the setting is intended to apply to a port range, enter the range with start port "-" end port, for example 30 - 40.
  - If the setting is intended to apply to all ports, enter "*".

  The setting is only effective for port-based protocols.
- **Auto Firewall Rules**

  - Enabled  
    For the VPN connection, the firewall rules for access from "External" to "Internal" and vice versa are created automatically. You can enable access to specific services of the device under "Security > Firewall > Predefined IPv4". Ping is enabled by default.
  - Disabled  
    You need to create the firewall rules yourself.

### OpenVPN

This section contains information on the following topics:

- [General](#general-6)
- [Connections](#connections-1)
- [Client (SC-600)](#client-sc-600)
- [Remote (S615)](#remote-s615)
- [Authentication](#authentication-1)
- [Server (SC-600)](#server-sc-600)

#### General

On this page, you activate the OpenVPN client.

##### Description

The page contains the following:

- **Enable OpenVPN**

  Enable or disable the OpenVPN client.

#### Connections

On this page, you configure the basic settings for the OpenVPN connection. You specify the security settings on the WBM page "Authentication".

##### Description

- **Connection name**

  Enter a unique name for the OpenVPN connection and click "Create" to create a new connection.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the OpenVPN connection.
- **Operation**

  Specify how the connection is established. You will find more detailed information in "[VPN connection establishment](#vpn-connection-establishment)".

  - start

    The device attempts to establish a VPN connection to the partner.
  - start on DI

    If the event "Digital In" occurs the device attempts to establish a VPN connection to the remote station.

    This is on condition that the event "Digital In" is forwarded to the VPN connection. To do this in "System > Events> Configuration" activate "VPN Tunnel" for the "Digital In" event.
  - Disabled

    The VPN connection is disabled.
- **Encryption**

  Select the required encryption algorithm.

  - AES-128-CBC (Default)
  - AES-192-CBC
  - AES-256-CBC
  - DES-EDE3
  - BF-CBC
- **Authentication**

  Specify the method for calculating the checksum.

  - SHA256 (default)
  - SHA384
  - SHA512
  - SHA224
  - SHA1
  - MD5
- **LZO Comp.**

  - disabled (-)

    The compression is disabled. The server can no longer enable compression.
  - No

    The compression is disabled as default. The server can enable compression
  - Yes

    The compression is enabled as default. The server can disable compression
  - Self-adjusting

    As default, compression is enabled adaptively. Only when there is data that is good for compression, otherwise the compression is disabled for a certain time.
- **Bridged** (SC600)

  Select the bridge ID with the IP address with which the OpenVPN connection should run. One bridge ID can be used for multiple connections.
- **Auto Firewall Rules**

  - Enabled

    The firewall rules are created automatically for the VPN connection.
  - Disabled

    You will need to create the suitable firewall rules yourself.
- **Enable NAT**

  With this setting, you enable automatic IP masquerading for this interface. The local devices are not directly reachable from the outside, but only via the IP address of the interface. The local devices can, however, connect to the devices downstream from the OpenVPN server. You will find more information on NAT in "[NAT](#nat)"
- **Timeout [min]**

  Specify the period of time in minutes. If no data exchange takes place, when this time has elapsed the VPN tunnel is automatically terminated.

#### Client (SC-600)

On this page, you configure the counterpart station (OpemVPN end point). Per connection, you can specify several OpenVPN partners. The device tries all configured OpenVPN partners one after the other until a connection is successfully established.

##### Description

The page contains the following:

- **Name**

  Enter a name for the OpenVPN client.

The table contains the following columns:

- **Name**

  Shows the name of the Open VPN partner.
- **Connection**

  Select the corresponding connection. Only connections can be configured that you configured on the "Connections" page.
- **Server address**

  Enter the WAN IP address or the DNS host name of the OpenVPN partner.
- **Port**

  Specify the port via which the OpenVPN tunnel can communicate. The setting applies specifically to the specified port.
- **Protocol**

  Specify the protocol for which the OpenVPN connection will be used.
- **Proxy**

  Specify whether the OpenVPN tunnel to the defined client is established via a proxy server. Only the proxy servers that you created in "System > Proxy Server" can be selected.

#### Remote (S615)

On this page, you configure the remote partner (OpenVPN end point). Per connection, you can specify several OpenVPN partners. The device tries all configured OpenVPN partners one after the other until a connection is successfully established.

##### Description

The page contains the following:

- **Remote name**

  Enter a name for the OpenVPN remote partner and click "Create" to create a new partner.

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the Open VPN partner.
- **Connection**

  Select the corresponding connection. Only connections can be configured that you configured on the "Connections" page.
- **Remote Address**

  Enter the WAN IP address or the DNS host name of the OpenVPN partner.
- **Port**

  Specify the port via which the OpenVPN tunnel can communicate. The setting applies specifically to the specified port.
- **Protocol**

  Specify the protocol for which the OpenVPN connection will be used.
- **Proxy**

  Specify whether the OpenVPN tunnel to the defined OpenVPN partner is established via a proxy server. Only the proxy servers can be selected that you configured in "System > Proxy Server".

#### Authentication

On this page, you specify how the VPN connection partners authenticate themselves with each other.

##### Description

The table contains the following columns:

- **Name**

  Shows the name of the VPN connection to which the settings relate.
- **TLS Auth. Key**

  Select the key file used to sign the TLS packets. If the incoming TLS packets are not signed with this key, they are discarded.
- **Direction**

  Specify the direction. If you select 0, 1 must be set on the partner and vice versa. With this setting, you restrict the clients that can authenticate themselves.

  Select "none" if nothing is set on the OpenVPN server. With "none", this setting is disabled.
- **Method**

  Select the authentication method. For the VPN connection, it is essential that the partner uses the same authentication method.

  - Disabled

    No authentication method is selected. Connection establishment is not possible.
  - Certificates

    Certificates are used for the authentication. The certificates need to be added later via the WBM and downloaded to the device.
  - Username/Password  
    The user name/password are used for the authentication. The certificate needs to be added later via the WBM and downloaded to the device.
  - Cert/Username/Password

    For authentication, a user name and password are required in addition to the certificate. The VPN connection is established only if both operations are successful.
- **CA Certificate**

  Select the CA certificate via the WBM and load it onto the device.

  You load the certificates onto the device with "System > Load&Save". The loaded certificates and key files are shown on the WBM page "Security > Certificates".
- **Machine Certificate**

  Select the machine certificate. Only loaded certificates can be selected.

  You load the certificates onto the device with "System > Load&Save". The loaded certificates and key files are shown on the WBM page "Security > Certificates".
- **User Name**

  Specify the user name.
- **Password**

  Enter the password.
- **Password Confirmation**

  Confirm the password.

#### Server (SC-600)

On this WBM page, you can create multiple OpenVPN servers per connection.

##### Description

The page contains the following:

- **Name**

  Enter a name for the OpenVPN server and click "Create".

The table contains the following columns:

- **Select**

  Select the check box in the row to be deleted.
- **Name**

  Shows the name of the OpenVPN server.
- **Connection**

  Select the corresponding connection. Only connections can be configured that have been configured on the "Connections" WBM page.
- **Max. Clients**

  Select the maximum number of clients to which the server can establish a connection at the same time.
- **Port**

  Specify the port via which the OpenVPN tunnel can communicate. The setting applies specifically to the specified port.
- **Protocol**

  Specify the protocol for which the OpenVPN connection will be used.

### Brute Force Prevention

#### Description of configuration

Brute Force Prevention refers to the protection of the device from unauthorized access by trying a sufficiently large number of passwords. The number of incorrect login attempts within a specific time period is limited for this purpose.

#### Description

The page contains the following boxes:

- **User Specific BFP is Enabled / User Specific BFP is Disabled**

  Shows whether the user-specific Brute Force Prevention is enabled.

  You configure login authentication in the menu "Security > AAA > > General" in the "Login Authentication" drop-down list. The login authentication determines whether you can enable user-specific Brute Force Prevention.

  - Enabled:

    With login authentication, the "Local" or "Local and RADIUS" mode is set and the maximum number of invalid login attempts is greater than 0.
  - Disabled:

    With login authentication, the "RADIUS" or "RADIUS and fallback Local" mode is set, or the maximum number of invalid login attempts is 0.
- **Acceptable Invalid Login Attempts Per User**

  The maximum number of invalid login attempts for a user after which login is blocked. All users that are not configured as local users for the device are summarized under the user name "UnknownUser".

  If you configure the value "0", user-specific Brute Force Prevention is disabled.

  The default value is "12".
- **IP Specific BFP is Enabled**

  Shows whether the IP-specific Brute Force Prevention is enabled.
- **Acceptable Invalid IP Login Attempts Per IP**

  The maximum number of invalid login attempts for an IP address after which login is blocked.

  If you configure the value "0", IP-specific Brute Force Prevention is disabled.

  The default value is "10".
- **BFP Trigger Interval [min]**

  The time in minutes that is relevant for counting invalid login attempts. If the number of permitted invalid login attempts is reached during this time (per user and per IP address), the device blocks login for a specific period of time. Invalid login attempts per user and per IP address are handled independently of one another. You can enter a value between 5 and 255 minutes. The default value is 5 minutes.
- **BFP Automatic Reset Timer[min]**

  Time in minutes for which the device blocks login because the maximum number of invalid login attempts was exceeded. You can enter a value between 0 and 255 minutes.

  If you configure the value "0", login is blocked indefinitely after the maximum number of invalid login attempts is reached.

  The default value is 12 minutes.

The **User Specific BFP** table has the following columns:

- **User**

  The user who attempted to log in.
- **Failed Logins**

  The number of failed login attempts.
- **Last Failed[s]**

  Time in seconds since the last failed login attempt. To display the current value, click the "Refresh" button.
- **Blocked**

  Shows the status of the user:

  - Not blocked

    Login with this user name is possible.
  - Duration

    Time in seconds for which login with this user name is blocked. To display the current value, click the "Refresh" button.

    If blocking has been lifted due to expiry of the time configured in the "BFP Automatic Reset Timer" box, the status of the user changes to "Not blocked".
  - Indefinitely blocked

    Login with this user name is blocked until you manually delete the blocking or restart the device.
- **Delete**

  Ends blocking for the user and resets the following displays:

  - The value in the "Last Failed" box is set to "0".
  - The status of the user in the "Blocked" box is set to "Not blocked".

The **IP Specific BFP** table has the following columns:

- **IP**

  The IP address of the device for the login attempt.
- **Failed Logins**

  The number of failed login attempts.
- **Last Failed[s]**

  Time in seconds since the last failed login attempt. To display the current value, click the "Refresh" button.
- **Blocked**

  Shows the status of the IP address:

  - Not blocked

    Login with this IP address is possible.
  - Duration

    Time in seconds for which login with this IP address is blocked. To display the current value, click the "Refresh" button.

    If blocking has been lifted due to expiry of the time configured in the "BFP Automatic Reset Timer" box, the status of the IP address changes to "Not blocked".
  - Indefinitely blocked

    Login with this IP address is blocked until you manually delete the blocking or restart the device.
- **Delete**

  Ends blocking for the IP address and resets the following displays:

  - The value in the "Last Failed" box is set to "0".
  - The status of the IP address in the "Blocked" box is set to "Not blocked".
