---
title: "Communications modules and network components"
package: HWCNCMCP34enUS
topics: 66
devices: [PC, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communications modules and network components

This section contains information on the following topics:

- [Industrial Ethernet / PROFINET](#industrial-ethernet-profinet)
- [PROFIBUS (S7-300, S7-400, PC)](#profibus-s7-300-s7-400-pc)
- [CM/CP PROFIBUS (S7-1500)](#cmcp-profibus-s7-1500)
- [CPs settings that do not depend on the protocol or the network](#cps-settings-that-do-not-depend-on-the-protocol-or-the-network)
- [Background on connections](#background-on-connections)
- [IE/PB LINK](#iepb-link)

## Industrial Ethernet / PROFINET

This section contains information on the following topics:

- [Settings](#settings)
- [Ethernet / PROFINET interface](#ethernet-profinet-interface)
- [Maximum frame size / volume of data for PROFINET IO devices](#maximum-frame-size-volume-of-data-for-profinet-io-devices)
- [DNS configuration](#dns-configuration)
- [IP access protection](#ip-access-protection)
- [Editing access permissions in the user management](#editing-access-permissions-in-the-user-management)
- [Tag declaration - Edit tag list](#tag-declaration---edit-tag-list)
- [Tag declaration - Edit tag list (ERPC)](#tag-declaration---edit-tag-list-erpc)
- [FTP configuration for FTP server mode](#ftp-configuration-for-ftp-server-mode)
- [I/O addresses](#io-addresses)
- [Web](#web)
- [SNMP](#snmp)
- [OPC UA Security (CP)](#opc-ua-security-cp)
- [CP 1545-1](CP%201545-1.md#cp-1545-1)

### Settings

This section contains information on the following topics:

- [Module access protection / UDP buffering / file system](#module-access-protection-udp-buffering-file-system)
- [Data transfer &gt; 240 bytes](#data-transfer-240-bytes)

#### Module access protection / UDP buffering / file system

##### Reference

Making special settings in the "Properties &gt; General &gt; Settings" parameter group

Depending on the CP type, you will find settings relating to the following areas and these are described below:

- Module protection
- UDP buffering
- File system

##### Module access protection - "Protection level" option

With this option, you can protect the CP from accidental or unauthorized access. The following options can be selected in the drop-down list:

- Not locked
- Status-dependent

  With this setting, it is only possible to access the CP when the CPU is in STOP mode.

##### Switch off UDP frame buffering

UDP frames are buffered by the CP depending on the communication load between the CP and the CPU.

You can select between the following using the UDP buffering (switch off UDP frame buffering) option:

- Disabled (default setting)

  Buffering of UDP frames is enabled. UDP frames received by the CP are buffered until they have been transferred to the CPU.
- Enabled

  The CP always transfers the last received, in other words, the current frame to the CPU. As long as no new UDP frame can be transferred between the CP and the CPU due to the current communication load, only the last frame received is buffered in the CP.

Turning off the UDP frame buffering achieves the shortest possible reaction time between the arrival of the UDP frame and its evaluation on the CPU. The characteristics associated with enabling the option can be critical in certain applications with high frame traffic. Buffering of a lot of frames may result in an undesired time offset between the frames accumulated in the CPU and the current frames at the Ethernet interface.

##### File system - Match case (case sensitive) - option for CPs with IT functions

Enabled: When files are placed in RAM, the CP distinguishes between upper- and lower-case characters in the file names.

#### Data transfer > 240 bytes

##### Reference

Making special settings in the "Properties &gt; General &gt; Settings" parameter group

Depending on the CP type, you will find setting "Data transfer &gt; 240 bytes"

##### Notes on data transfer &gt; 240 bytes

- Data transfer &gt; 240 bytes is supported by the newer versions of the CPs. Refer to the information in the documentation of your Ethernet CP.
- With the S7-300 series, remember that this configuration uses one connection resource (free connection for S7 functions) on the S7-300 CPU. CPU connection resources are also used, for example, by S7-300 CPs in FMS mode or by programming devices or OPs.

### Ethernet / PROFINET interface

This section contains information on the following topics:

- [Advanced options](#advanced-options)
- [IP configuration](#ip-configuration)
- [Time-of-day synchronization](#time-of-day-synchronization)
- [Time-of-day synchronization with S7-1200](#time-of-day-synchronization-with-s7-1200)
- [Time-of-day synchronization - IE/PB LINK PN IO (V3)](#time-of-day-synchronization---iepb-link-pn-io-v3)
- [Additional information](#additional-information)

#### Advanced options

This section contains information on the following topics:

- [Keepalive frames for TCP and ISO-on-TCP connections](#keepalive-frames-for-tcp-and-iso-on-tcp-connections)

##### Keepalive frames for TCP and ISO-on-TCP connections

###### Reference

Making special settings for the PROFINET interface in the "Properties &gt; General &gt;PROFINET interface &gt; Advanced options &gt; Interface options" parameter group

###### Keepalive frames (only with TCP and ISO-on-TCP connections)

Here, you can set the interval at which keepalives are sent to the partner of a communications connection.

The Ethernet CP is configured for all connection-oriented services so that keepalive frames are sent. This ensures that connections are terminated if one of the communication partners fails and the connection resources are released again. The setting made here applies to all TCP and ISOonTCP connections operated via the CP. A connection-oriented setting is not possible.

**Range of values**

- Default setting: 30 seconds
- Maximum value: see information displayed in the input box
- Function turned off: 0 seconds

> **Note**
>
> Note that the keepalive mechanism can cause subordinate connections (for example, an ISDN telephone connection) to be maintained even though user data is not actually being transferred. If this is unwanted, proceed according to one of the following alternatives:
>
> - Disable the keepalive mechanism (interval time = 0).
> - Set the interval so high that the underlying connection is terminated before a keepalive frame is sent when there is no data traffic.

#### IP configuration

##### Reference

Configuration of the IP parameters in the parameter group of the PROFINET or Ethernet interface

##### Meaning

You can decide the route and the method with which the IP address of the local interface is obtained and assigned.

With the options available here, it is possible to assign IP addresses "dynamically" outside the configuration.

The selection you make also decides whether communication connections are set up by the project engineering or via the interface in the user program (IP_CONFIG instruction).

The following options are available:

- **Set IP address in the project**

  This is the default setting for PLCs. You specify the IP address when the device is networked. The IP address CP is therefore fixed.

  Communications connections must be configured when using this option.
- **Obtain an IP address from a DHCP server**

  With this option you specify that the IP address is obtained from a DHCP server when the device starts up.

  - IPv4

    The DHCP server is informed of the MAC address of the interface or the optionally configurable client ID.

    Length of the client ID: 2.. 63 printable ASCII characters
  - IPv6

    The DHCP server is informed of the client ID and must be configured.

    Length of the client ID: 1.. 128 printable ASCII characters

  When configuring of the connections, note the following:   
  If you are using DHCP, it is initially not possible to create a fully specified connection in the project because the local IP address is not known. You therefore select "unspecified" with passive connection establishment as the connection type.
- **Set IP address in the user program**

  With this option, you specify that the IP address is set over the user program interface (function block IP_CONFIG). This allows the IP address to be supplied dynamically during operation.

  In this case, communications connections are set up only via the interface of the user program. Connection configuration is no longer possible (relates to connections via TCP, ISO‑on‑TCP, UDP, ISO-Transport).
- **Set IP address on the device**

  With this option, you specify that the IP address is set by other services outside the configuration.

  In this case, connection configuration is no longer possible (relates to connections via: TCP, ISO‑on‑TCP, UDP, ISO-Transport).

> **Note**
>
> If you have already configured communications connections via the interface configured here and you select a setting other than "Set IP address in the project", a message will then be displayed indicating that the configured connections no longer function.

#### Time-of-day synchronization

This section contains information on the following topics:

- [Time-of-day synchronization - mode](#time-of-day-synchronization---mode)
- [SIMATIC mode - configuration](#simatic-mode---configuration)
- [NTP method - configuration](#ntp-method---configuration)

##### Time-of-day synchronization - mode

###### Reference

Configuration of the time-of-day synchronization method of the module in the parameter group "Time-of-day synchronization" under the PROFINET interface or in the Security settings.

For time-of-day synchronization of the S7-1200, see section [Time-of-day synchronization with S7-1200](#time-of-day-synchronization-with-s7-1200).

For configuration of the time-of-day synchronization of the IE/PB Link PN IO (V3) see section [Time-of-day synchronization - IE/PB LINK PN IO (V3)](#time-of-day-synchronization---iepb-link-pn-io-v3).

###### How the time synchronization modes work

- **SIMATIC mode**

  If the SIMATIC mode is enabled, the module sets its time-of-day according to MMS time-of-day messages (MMS ‑ Manufacturing Message Specifaction).

  The MMS time-of-day messages originate from a SIMATIC time transmitter or a CPU configured as time master. The time-of-day messages can be received by the module (e.g. CP) either from the local CPU or via a LAN. It is possible to set whether the module will forward the received time of day.

  The advantage of the SIMATIC mode is that it is generally more accurate than the NTP mode.

  See also [SIMATIC mode - configuration](#simatic-mode---configuration)
- **NTP method**

  (NTP ‑ Network Time Protocol)

  With the NTP method, the module sends time-of-day queries to one or more NTP servers in the subnet (LAN). Based on the replies from the server, the most reliable and most accurate time is determined and the time of day on the querying module is synchronized. In this case, any MMS time messages that are received will be ignored.

  In NTP mode, it is generally UTC (Universal Time Coordinated) that is transferred. This corresponds to GMT (Greenwich Mean Time).

  The advantage of NTP mode is that it allows the time to be synchronized across subnets.

  See also [NTP method - configuration](#ntp-method---configuration)

##### SIMATIC mode - configuration

###### Time-of-day synchronization in SIMATIC mode:

In "SIMATIC" mode, the CP forwards MMS time-of-day messages when it receives them from a SIMATIC time transmitter. The time-of-day messages can either be received via the backplane bus or via the communications bus (S7-400 CPU) or via LAN.

###### "Apply time in CP"

The time of day can either be simply received by the CP or received and forwarded.

When the time-of-day is forwarded, you need to specify the direction in which it is forwarded.

###### "Direction"

Depending on where the time master is located, the direction of the time-of-day forwarding must be taken into account.:

If you have several CPs in your station, take into account the flow of time-of-day messages depending on the time-of-day master since you can forward time-of-day messages from one network to another network using the function described here. In a station there must only be one time master.

If there are several CPs that are connected to the same subnet and if forwarding of the time of day is activated for these, the following applies: The CP with the lowest slot number handles the forwarding of the messages. All other CPs configured for forwarding time-of-day messages, automatically stop forwarding.

You can make the following settings for the direction of time-of-day forwarding:

- Automatic

  The CP receives the time­of­day message from the LAN or from the station and forwards it to the station or to the LAN.

  If several CPs are being operated in the station, this automatic setting can lead to collisions. To avoid this, you can specify the direction of forwarding with the following options:
- From station

  The CP receives the time-of-day message from the station and forwards it to the LAN.

  In this case, a local CPU must be configured as the time master or another CP 400 forwards time messages to the K bus.
- From LAN

  The CP receives the time-of-day message from LAN and forwards it to the station.

  In this case, the local CPU must be configured as a time slave.  
  Exception: CPU 318

###### "Use corrected time"

With the this option, you can decide whether a correction factor in the time-of-day frame is taken into account.

The correction factor that can be set in a central clock SICLOCK in units of ½ hours specifies a time offset for example to correct a time zone setting or standard/daylight saving time.

If this option is enabled, the CP calculates the correction factor in the time of day to be forwarded this so that systems to which the time is forwarded do not need to take the factor into account.

Example:

The time 9:21 is transferred in the time-of-day frame. In addition, the time-of-day frame contains the correction factor +2 x 0,5 (= 1h). The time forwarded by the CP is therefore 10:21.

##### NTP method - configuration

Where possible create a concept for the time-of-day synchronization before the configuration. Make sure that you only use one time source for every station. It makes sense to have only one time source per subnet.

Note the mechanisms of time-of-day synchronization of the S7-1200 in the section [Time-of-day synchronization with S7-1200](#time-of-day-synchronization-with-s7-1200).

###### NTP ‑ Network Time Protocol

With the NTP method, the CP or the CPU sends time-of-day queries to one or more NTP servers in the subnet (LAN). Based on the replies from the server, the most reliable and most accurate time is determined and the time of day on the querying module is synchronized. Any MMS time-of-day messages received are then ignored.

The advantage of NTP mode is that it allows the time to be synchronized across subnets.

In NTP mode, it is generally UTC (Universal Time Coordinated) that is transferred. This corresponds to GMT (Greenwich Mean Time).

The parameters described below are not available for all modules.

###### NTP server

You can configure the IP addresses of up to four NTP servers.

> **Note**
>
> **S7-1500 CPUs as of version V1.8: Changing the NTP servers fro the user program**
>
> For S7-1500 CPUs as of firmware version V1.8 you can change the addresses of 4 NTP servers with the instruction T-CONFIG (SFB 105) at runtime. The requirement for this is that you have configured at least one NTP server in the "Time-of-day synchronization" parameter group.
>
> The configured addresses of the NTP servers are overwritten by the IP addresses of the NTP servers in the instruction T_CONFIG. Even if only 1 NTP server was configured, up to 4 NTP servers can be programmed using the SFB. When necessary, the addresses of the NTP servers can be changed several times with T_CONFIG.
>
> The firmware version V1.8 for S7‑1500 CPUs is available with STEP 7 V13.0 SP1 Update 3.

###### "Time zone"

The time offset from UTC can be set by configuring the local time zone.

###### "Update interval"

The interval specifies the time cycle of the time queries (in seconds). The value of the interval ranges between 10 seconds and one day.

If the "Time-of-day synchronization on the full minute" option is enabled, the cycle is automatically set to 60 seconds.

###### "Time-of-day synchronization on the full minute"

If the option is enabled, the synchronized time of day that the CP forwards to the CPU is adopted by the CPU precisely on the full minute.

If the "Time-of-day synchronization on the full minute" option is enabled, the parameter "Update interval" is automatically set to 60 seconds.

###### "Accept time of day from non-synchronized NTP servers"

If the option is enabled, the CP also accepts the time-of-day from non-synchronized NTP servers with stratum ≥ 15.

If the option is disabled, the CP does not accept the time-of-day from NTP servers with stratum ≥ 15. If the CP receives a time of day frame from an NTP server with stratum ≥ 15, the time of day of the CP is not set according to the frame. In this case, none of the NTP servers is displayed as "NTP master" in the diagnostics; but rather only as being "reachable".

###### "Forward time of day to station"

With CP 300/400 this option is enabled as default.

Some CPUs provide the option of requesting the time of day automatically from an NTP server. If the time-of-day synchronization is used by the CPU, you should disable the option described here on the CP. This avoids the time of day acquired by the CPU from the NTP server being overwritten again by the time of day received by the CP. Due to forwarding the time of day from the CP to the CPU there could be less accuracy in this case.

#### Time-of-day synchronization with S7-1200

##### Module and synchronization method

When using an external time source, the S7-1200 station can obtain the current time of day both via the CPU as well as via a CP.

With the S7-1200 there is no forwarding of the time of day from the station to the subnet.

**Time-of-day synchronization using the CPU**

As the synchronization method, with the CPU only NTP can be selected.

With the "CPU synchronizes the modules of the device" option, you can cause all intelligent modules of the station (CMs, CPs) to be synchronized with the CPU time in a configurable synchronization cycle of between 10 and 86400 seconds (24 hours).

> **Note**
>
> **Time-of-day synchronization when using Secure Open User Communication (Secure OUC)**
>
> If the S7-1200 uses Secure OUC blocks and uses the PROFINET interface of the CP for communication, the "CPU synchronizes the modules of the device" option must be enabled.
>
> This data can only be validated against the validity period of a certificate if the date and time are current. If the date and time are outside the validity period, no communication takes place via Secure OUC.

**Time-of-day synchronization using a telecontrol CP**

The following synchronization methods are available:

- **NTP**

  NTP can only be used when the telecontrol communication is disabled. In this case, the telecontrol CP is used as an extended PROFINET interface of the CPU.
- **Time from partner**

  When telecontrol communication is enabled, the CP automatically takes the time-of-day from the communications partner.

> **Note**
>
> **Forwarding the time to the CPU**
>
> Depending on the firmware version of the modules involved, the time-of-day of the CP is forwarded to the CPU in different ways:
>
> - Optional forwarding of the CP time to the CPU using a PLC tag
> - Obligatory forwarding of the CP time to the CPU via the backplane bus

##### Forwarding the time from the CP to the CPU

> **Note**
>
> **Recommendation: Time-of-day synchronization only by 1 module**
>
> Only have the time of day of the station from an external time source synchronized by a single module so that a consistent time of day is maintained within the station.
>
> When the CPU takes the time from the CP, disable time-of-day synchronization of the CPU.

The forwarding of the CP time to the CPU depends on the firmware version of the CP and the CPU. Note the following behaviour.

- **CP firmware**
   **≤ V2.1.5**

  With this firmware version the CP can make the time-of-day available to the CPU as an option via a PLC tag. When this PLC tag is read cyclically by the CPU, the CPU adopts the CP time.
- **CP firmware**
   **≥ V2.1.7**
   **and CPU firmware**
   **≥ V4.2**

  If both modules in a station have one of the mentioned firmware versions, the time of the CP can be forwarded automatically to the CPU.

  A condition for this is: The "CPU synchronizes the modules of the device" option is selected for the CPU under "PROFINET Interface &gt; Time-of-day synchronization".

  Then all intelligent modules of the station are synchronized with the CPU time.

  Since the CPU automatically adopts the CP time, you no longer require the forwarding option using the PLC tag.

#### Time-of-day synchronization - IE/PB LINK PN IO (V3)

##### Reference

Configuring time-of-day synchronization of the IE/PB LINK PN IO V3

The requirement is that the time of day is made available by a node on the relevant network.

##### Procedure for time-of-day synchronization

The following methods can be selected with various options:

- **SIMATIC mode**

  If the SIMATIC mode is enabled, the LINK sets its time-of-day according to MMS time-of-day messages (MMS ‑ Manufacturing Message Specifaction).

  The MMS time-of-day messages originate from a SIMATIC time transmitter or a CPU configured as time master. The time-of-day messages can be received by the CP either from the local CPU or via a LAN. You can set whether and in which direction the LINK will forward the time-of-day frames.

  The advantage of the SIMATIC mode is that it is generally more accurate than the NTP mode.
- **NTP method**

  (NTP ‑ Network Time Protocol)

  With the NTP method, the LINK sets its time according to time-of-day messages originating from an NTP server and made available by a node on the Ethernet network. You can set whether the LINK simply adopts the time-of-day frames from the LAN or adopts it and forwards them.

  In NTP mode, it is generally UTC (Universal Time Coordinated) that is transferred. This corresponds to GMT (Greenwich Mean Time).

  The advantage of NTP mode is that it allows the time to be synchronized across subnets.

##### Configuring time-of-day synchronization

Meaning of the options:

- **Use SIMATIC method - forward from Ethernet to PROFIBUS**

  The LINK adopts the time of day from the LAN and forwards it to the PROFIBUS network.
- **Use SIMATIC method - forward from PROFIBUS to Ethernet**

  The LINK adopts the time of day from the PROFUBUS network and forwards it to the LAN.
- **SIMATIC method - take time of day from the Ethernet network**

  The LINK adopts the time of day from the LAN but does not forward it.
- **SIMATIC method - take time of day from the PROFIBUS network**

  The LINK adopts the time of day from the PROFIBUS network but does not forward it.
- **Use NTP method - forward from Ethernet to PROFIBUS**

  The LINK adopts the time of day from the LAN and forwards it to the PROFIBUS network.
- **NTP method - take time of day from the Ethernet network**

  The LINK adopts the time of day from the LAN but does not forward it.

#### Additional information

This section contains information on the following topics:

- [Individual network settings](#individual-network-settings)
- [Range of values and example of the IP address](#range-of-values-and-example-of-the-ip-address)
- [Range of values and example of the subnet mask](#range-of-values-and-example-of-the-subnet-mask)
- [Relationship between the IP address and address of the gateway](#relationship-between-the-ip-address-and-address-of-the-gateway)
- [Port parameters](#port-parameters)

##### Individual network settings

###### Individual network settings

Here you can make fixed network settings as required. The "Automatic setting" is selected by default. In normal situations, this guarantees problem-free communication.

If problems do occur in communication (such as when connections cannot be established or frequent network faults occur), this may be caused by an unsuitable selected or automatic network setting. In this case, you should select a network setting that is suitable for your network configuration.

##### Range of values and example of the IP address

###### Range of values for the IP address

The IP address consists of four decimal numbers from the range 0 to 255 separated by a period.

Notation: xxx.yyy.zzz.www

###### Example:

141.80.0.16

- The following addresses have special meanings (*stands for any number between numeric 0 and 255):

  - 127.*.*.* Loopback
  - 0.0.0.0 unspecified network
  - 255.255.255.255 broadcast to all devices (permitted only when "All broadcast devices" was selected as the connection peer)
  - Host address 255 broadcast address for all devices of a network:

    For class A: xxx.255.255.255

    For class B: xxx.yyy.255.255

    For class C: xxx.yyy.zzz.255
- The following are not permitted:

  - Host address 0

    For class A: xxx.0.0.0

    For class B: xxx.yyy.0.0

    For class C: xxx.yyy.zzz.0

##### Range of values and example of the subnet mask

###### Range of values for subnet mask

To separate the network ID from the host address in the IP address, the subnet mask was introduced.

The subnet mask consists of four decimal numbers from the range 0 to 255 separated by a period, for example 255.255.0.0.

In their binary representation, the four decimal numbers of the subnet mask must include a continuous series of "1" values without any gaps from the left and a series of "0" values without any gaps from the right.

The "1" values decide the network number within the IP address. The "0" values decide the host address within the IP address.

###### Example:

Correct values: 255.255.0.0 D = 1111 1111.1111 1111.0000 0000.0000 0000 B

255.255.128.0 D = 1111 1111.1111 1111.1000 0000.0000 0000 B

255.254.0.0 D = 1111 1111.1111 1110.0000 0000.0000.0000 B

Incorrect value: 255.255.1.0 D = 1111 1111.1111 1111.0000 0001.0000 0000 B

###### Relationship between the IP address and subnet mask

The first decimal number of the IP address (from the left) decides the structure of the subnet mask in terms of the number of "1" values (binary) as follows ("x" stands for the host address or "0" in the subnet mask):

- First decimal number of the IP address subnet mask

  Class A: 0 to 126 255.x.x.x

  Class B: 128 to 191 255.255.x.x

  Class C: 192 to 223 255.255.255.x

  > **Note**
  >
  > You can also enter a value between 224 and 255 for the first decimal number of the IP address. This is, however, not advisable since STEP 7 does not check these addresses.

##### Relationship between the IP address and address of the gateway

###### Relationship between IP address and gateway address

The only points in the IP address and gateway address that may differ are those in which "0" appears in the subnet mask.

###### Example:

You have entered the following: 255.255.255.0 for the subnet mask; 141.30.0.5 for the IP address and 141.30.128.1 for the gateway address.

|  | Usual decimal representation | Binary representation |
| --- | --- | --- |
| Subnet mask | 255.255.255.0 | 1111 1111.1111 1111.1111 1111.0000 0000 |
| IP address | 141.30.0.5 | 1000 1101.0001 1110.0000 0000.0000 0101 |
| Gateway | 141.30.128.1 | 1000 1101.0001 1110.1000 0000.0000 0001 |

Only the fourth decimal number of the IP address and gateway address may have a different value. In the example, however, the 3rd position is different.

You must, therefore, change one of the following in the example:

The subnet mask to: 255.255.**0**.0 or

the IP address to: 141.30.**128**.5 or

the gateway address to: 141.30.**0**.1

##### Port parameters

###### Individual network settings for each port

When necessary, you can make fixed network settings for the transmission characteristics of each available interface (port). The "Automatic setting" is selected by default. In normal situations, this guarantees problem-free communication.

If problems do occur in communication (such as when connections cannot be established or frequent network disruptions occur), this may be the result of unsuitable network settings, either selected or automatic. In this case, you should select a network setting that is suitable for your network configuration.

###### Functional description of the automatic switchover

All ports of the CP provide a 10/110 Mbps full duplex connection with autosensing and autonegotiation of the network settings. These functions run as follows after turning on the CP:

- The CP attempts to detect the transmission speed used by the partner.
- If detection is possible, the CP attempts to negotiate the optimum duplex mode with the partner.
- If no negotiation is possible, the CP uses the previously detected transmission speed and half duplex.

This takes approximately 2 seconds.

The "Automatic setting" also includes an autocrossing mechanism; this means that you can use a crossover or straight-through cable for the connection regardless of the properties of the partner device.

###### Changing to individual network settings

If you create any configuration manually, automatic switchover is no longer effective. This also applies to the autocrossing mechanism integrated in the CP. If the connected partner device does not support the autocrossing mechanism, you will need to use a crossover cable (for a switch) or a straight-through cable (for an end device).

###### "Disable" port option:

Depending on the module type, the drop-down list includes the "- Disable -" option. This option, for example, allows you to prevent access to an unused port for security reasons.

See also

###### Further information

Please read the manual on the relevant CP for further information.

### Maximum frame size / volume of data for PROFINET IO devices

#### Size of the user data with the CP 1616

The size of the user data (process data) is calculated from the maximum frame size (gross volume of data) minus the values for the modules plugged into this IO device. This results in the net volume of data.

Example of the calculation of the user data (bytes) of the CP 1616 as an IO device with homogeneous modules (for example only DI modules)

| Bytes | Explanation |
| --- | --- |
| 1434 | Gross size of the frame |
| -16 | for the maximum number of pluggable modules |
| = 1418 | Net size of the user data |

Example of the calculation of the user data (bytes) of the CP 1616 as an IO device with heterogeneous modules (for example DI/DO)

| Bytes | Explanation |
| --- | --- |
| 1434 | Gross size of the frame |
| -32 | for twice the maximum number of pluggable modules |
| = 1370 | Net size of the user data |

#### Size of the user data with the CP 343-1 (Lean/Standard/Advanced)

The size of the user data (process data) is calculated from the maximum frame size (gross volume of data) minus the values for the CP and the interface itself, for the number of ports and the modules plugged into this IO device. This results in the net volume of data.

Example of calculating the user data (bytes) of the CP 343-1 as an IO device

| Bytes | Explanation |
| --- | --- |
| 548 | Gross size of the frame |
| -1 | for the CP itself |
| -1 | for the Interface |
| -2 | for 2 ports |
| -32 | for the maximum number of pluggable modules |
| = 512 | Net size of the user data ***** |
| * By using fewer but larger modules, the volume of user data can be increased. |  |

### DNS configuration

#### Reference

Configuration of the DNS server address in the "DNS configuration" parameter group

A DNS server may be required when the module itself, a communications partner, or for example an e-mail server should be reachable via the host name (FQDN).

#### DNS server for e-mail connections

When configuring an e-mail connection, the address of the e-mail server via which the e-mails are sent must be specified. The address of the mail server can be specified as an IP address or as an FQDN.

If you specify the server address as an FQDN you need to configure a DNS server. In this case the IP address of the mail server is determined via the configured DNS server.

### IP access protection

This section contains information on the following topics:

- [IP access protection](#ip-access-protection-1)
- [Entering access permissions in the IP access control list (IP-ACL)](#entering-access-permissions-in-the-ip-access-control-list-ip-acl)

#### IP access protection

##### Reference

Making settings for the interface properties in the "Properties &gt; General &gt; IP access protection" parameter group.

##### Overview

The following options can be assigned for IP access protection according to the CP type:

- "Enable web server" option

  The CP provides you with the functionality of a web server for access by means of a web browser. Certain HTML pages with CP information and diagnostic functions are stored in a memory area of the CP for this.

  Enable this option in order to be granted access to these HTML pages. Port 80 of the CP is thereby enabled.

  Web server access is enabled by default.
- "Enable FTP server" option

  Select this option if you want to allow FTP access to the S7 station via Port 20/21 of the CP.

  If you configure FTP access to file DBs in the CPU in the "FTP" tab, access is only possible if you select the option here.

  FTP server access via Port 20/21 is enabled by default.
- "Enable access protection for IP communication" option

  The Ethernet interface allows you to restrict access to the local device to partners with specified IP addresses. Partners you have not authorized then have no access to data on the local device via this interface.

  Here, you can enable or disable IP access protection and can also enter certain IP addresses in an IP address control list (IP-ACL).

  As default, IP access protection is deactivated.

  Blocked access attempts are registered on the CP and can be viewed with special diagnostics in the "IP access protection" diagnostic object. If the CP has IT functionality, a LOG file is also created in the file system of the CP that you can view with a WEB browser.

  Please refer to the instructions on handling the LOG file and the notes on loading the configuration data below.

##### IP access protection for configured communication partners

If you want to restrict access so that only the communication partners you specified in the configuration have access to the local device, you simply need to enable access protection. In this case, you do not need to enter any IP addresses in the list.

These communication partners include:

- Stations to which communication connections are configured;

  With the exception of S7 connections, this also applies to connections on which the connection partner is located in a different subnet.

  You should, however, remember that where you have unspecified connections whose partner addresses are unknown; all IP addresses that are not entered are unauthorized and will be rejected. Even connections in PROFINET CBA will be treated as unspecified connections. You will need to enter the IP addresses of such connections explicitly in the IP access control list.
- PROFINET IO devices when the Ethernet CP is used as a PROFINET IO controller;

  The IP addresses of PROFINET IO devices are entered dynamically in the IP access control list when the CPU is in RUN mode.

  If the CPU changes to STOP mode, the IP addresses of the PROFINET IO devices are deleted from the access list.
- NTP servers, SMTP servers, DNS servers and DHCP servers.

  The IP addresses of NTP servers, SMTP servers, DNS servers and DHCP servers are also entered and removed dynamically when there are requests to these servers.

IP access protection relates to all connection types that use the IP protocol (TCP, ISO-on-TCP, UDP, S7)

Note on dynamically assigned IP addresses:  
Since each service manages its dynamic entry in the ACL itself, it is perfectly possible for the same IP address to appear several times in module diagnostics.

##### IP access protection for partners with specific IP addresses

To allow access only by certain IP addresses, enter these IP addresses in the IP access control list. These can, for example, be the IP addresses of connection partners that remained unspecified in the connection configuration, of individual programming devices or of connection partners on PROFINET CBA.

The IP addresses you specified in the connection configuration always belong to the permitted IP addresses and do not therefore need to be entered explicitly in the IP-ACL.

##### Viewing the LOG File with a Web browser

On CPs with IT functionality, a LOG file is created in the file system of the CP and this can be viewed with a Web browser. Compared with the recording made in the special diagnostics, the LOG file provides space for up to 512 entries.

The LOG file is available only after activating IP access protection the first time.

You will find the LOG file as an HTML file in the file system of the CP in the following directory:

·ram/security/IPLogFile.htm

Further properties:

The LOG file is created as a ring buffer. When more than 512 entries have been recorded, the oldest entries are then overwritten.

Entries are made chronologically and there are no other criteria for sorting.

Note that this function is supported only by the newer firmware versions of the CPs; you will find more detailed information in the CP device documentation.

With Advanced CPs as of CP 343-1 Advanced (GX30) and CP 443-1 Advanced (GX20) the LOG file is not created. On these CPs, you can view the blocked access attempts directly with Web diagnostics.

#### Entering access permissions in the IP access control list (IP-ACL)

##### Reference

Making settings for the interface properties in the "Properties &gt; General &gt; IP access protection" parameter group.

##### Rules for entering the IP addresses:

Keep to the following rules when entering IP addresses:

- You can enter the IP address singly or as a range.
- You can also enter comments.
- The maximum number of addresses you can enter is: 32
- The maximum number of address ranges you can enter is: 10
- The system does not check whether addresses that have already been entered singly are also included in an address range.
- The system does not check whether a range includes invalid addresses (for example, broadcast addresses can be specified here although they cannot occur as the IP address of a sender).
- Comments begin with the "#" character

##### Examples:

- Individual IP address with comment: 141.80.0.16 #address of partner x
- Range of IP addresses with comment: 141.80.0.16 - 141.80.0.25 #address range for control level

##### Rights

The access permissions described here can be selected in the IP access control list with their short designations.

All tables
Access permissions and short designations

Access permissions and short designations

| Access right | Short designation | Meaning / remark |
| --- | --- | --- |
| Access to station | **A** | **Access**   Communications partners with addresses in the specified range have access to the station (CP / CPU) belonging to the CP.  This access permission is set implicitly for IP addresses you have specified in the connection configuration. |
| Modifying the IP access control list | **M** | **Modify**   Communications partners with addresses in the specified range, have the right to access the IP access control list. These communications partners can send entries for the IP access control list to the CP using HTTP.  If you select this permission, the permission "A" is also set.  Notes on the entries sent using HTTP:  - With each list transferred using HTTP, a previous list sent using HTTP becomes invalid. - The access permissions sent using HTTP can be added to entries configured in STEP 7, but the entries cannot be deleted. - A list transferred using HTTP is deleted if there is a power down on the CP (power OFF).   You will find information on the syntax of a list transferred using HTTP in the documentation of the CP. |
| IP routing access to the another IP subnet | **R** | **Routing**   Communications partners with addresses in the specified range have access to other subnets connected to the CP.  This access permission is not set automatically for IP addresses you have specified in the connection configuration. Where necessary, this access permission must be set here explicitly. |

> **Note**
>
> - **Loading configuration data via TCP/IP**
>
>   When downloading via TCP/IP with access protection enabled, note that you will need to include the IP address of the programming device / PC from which the configuration is downloaded in the IP-ACL. The programming device / PC would otherwise be detected as unauthorized during the loading and the loading routine would be aborted
> - **Loading S7 connections later**
>
>   If you want to load individual S7 connections to the S7 station later, these are not included automatically in the IP-ACL. In this case, you will need to load the entire station configuration again.
> - **Adopting and editing a configuration by loading to the programming device / PC**
>
>   If you want to edit the connection configuration and have enabled IP access protection, you will require the full connection information on the programming device / PC. This means that you will need to upload the current connection data. When you then load the data to the S7 station again, you will need to load the entire connection data and station data.

> **Note**
>
> Using special diagnostics, you can view the current IP-ACL on the S7 station and, if required, compare it with the configured IP-ACL.

### Editing access permissions in the user management

#### Reference

Setting user permissions in the "Properties &gt; General &gt; User management" parameter group

#### Meaning of user management

In user management, you specify which users have which permissions when accessing the S7 station via a Web browser or as an FTP client.

In an alphabetical list, under user name you will find the users that have already been entered for which passwords have been stored.

The "All" entry is present as default. This cannot be modified. It is also not possible to assign a password to this entry.

User entries are always linked to a password. Exception: The "All" entry is not password protected.

> **Note**
>
> As default, no rights whatsoever are assigned to the "All" entry. For service purposes, however, it is possible to assign permissions.
>
> You should, however, remember that any permissions assigned to the "All" user are also available to every other user. If you do assign permissions for service purposes, remember to cancel these again afterwards! Otherwise, you allow services to be executed without authorization with every access.
>
> If an access right is set for the "All" user, this is recognizable by the filled check box when you assign rights to other users.

#### Entering new users

1. Select the first free row in the user list.

   A new user entry is created with the access level "Minimum".
2. Adapt the proposed user name in the "Name" column.
3. Double-click in the "Access level" column of the newly created row.

   The icon for the drop-down list becomes visible.
4. Click on the icon of the drop-down list.
5. In the dialog that then opens, set specific user permissions.
6. Confirm your entries with "OK".
7. Assign a new password in the password dialog that opens.

#### Changing user permissions or a password:

1. Double-click in the "Access level" column of the row of the required user entry.

   The icon for the drop-down list becomes visible.
2. Click on the icon of the drop-down list.
3. In the next dialog, modify the specific user permissions or click on the "Password" button to assign a new password.
4. Confirm your entries with "OK".
5. Enter the password in the password dialog that opens.

#### Deleting user entries

1. Select "Delete" in the context menu of the row of the required user entry.

### Tag declaration - Edit tag list

#### Reference

Setting the tags configured on the CPU in the "Properties &gt; General &gt; Tag declaration" parameter group.

#### Meaning of the tag declaration

To access tags of the CPU using a Web browser and Java applet, the CP must be aware of the names, addresses, and access rights of these tags.

In the symbol list in the tag declaration, you can see the currently known tags with their symbolic names, the corresponding operands and the assigned access rights.

#### Adding a new tag entry

1. Double click on the first free row in the table.

   The symbol becomes visible for selection from the drop-down list.
2. Select the symbol to open the structure display of the tags on the current device.
3. Select the symbols of the tags or the structure elements to which access will be possible using a Web browser.

   Note: You must first store the symbols in the Symbol Editor!

#### Deleting a tag entry

1. Select "Delete" in the shortcut menu of the row of the tag to be deleted.

   Caution:

**Note**

There is no prompt for confirmation, the entry is deleted immediately. Multiple selections are not possible.

#### Setting access permissions - "Writable" option

The default permissions for the tags are read-only.

To assign write/read rights for the tags entered here, follow the steps below:

1. Select one or more tags in the symbol list.
2. Set the "Only reading allowed" option as required for the selected tags.

### Tag declaration - Edit tag list (ERPC)

#### Reference

Configuration of the tags created on the CPU for the ERPC application

You select the tags you want to make accessible to the ERPC application.

#### Table of the ERPC tags

The table shows the PLC tags configured in the STEP 7 project that are available for the ERPC application. Any ERPC tags that may have been downloaded to the station previously are not displayed.

The following information is displayed in the table of tags configured for ERPC:

- Info

  Additional information from the check of changes made

  ERPC tags that you have changed in the STEP 7 project since the last time you saved have additional information displayed in the "Info" column by the check changes function (see below).
- Tag

  Name of the tag
- Writable

  The permissions configured for ERPC communication (reading from the CPU, writing to the CPU), as default only read permissions are assigned.
- Comment

  Comments on the ERPC tags specifically for ERPC communication.

Below the table:

- Writable

  By enabling the option "Writable", you cancel the write protection of the selected ERPC tags and release them for write jobs of the ERPC application.
- Number of tags:

  The total number of tags used for ERPC

#### Multiple selection of tags

You can select more than one tag using the &lt;Shift&gt; and &lt;Ctrl&gt; keys.

#### Check for changes

When you open the tag declaration, a check is made for any changes. The tags selected for the ERPC application are compared with the those in the tag table of the assigned CPU in the STEP 7 project (offline tag table).

> **Note**
>
> There is no comparison of ERPC tags you may have downloaded previously from the STEP 7 project to the station.

The "Info" column displays the relevant information on differences between the ERPC tags and those of the tag table of the CPU.

| Display in the "Info" column | Status / information |
| --- | --- |
|  | Tag unchanged |
| ACC | The tag cannot currently be edited. Reason: The data block in which the tag is used is currently open. |
| DEL | Tag deleted in the tag table of the CPU |
| ADR | Address changed in the tag table of the CPU |
| TYP | Data type changed in the tag table of the CPU  Note: If the address and the data type of a tag are changed in the tag table, the "ADR" information is overwritten by the "TYP" info. |
| DEF | Tag type not supported |
| UPL | Tag uploaded from the station (after using the STEP 7 function "Upload to PG") |

If entries of the type "DEL", "ADR" and "TYP" exist, you will need to make suitable corrections before you save the STEP 7 project.

### FTP configuration for FTP server mode

This section contains information on the following topics:

- [Ethernet CP as FTP server for the CPU data](#ethernet-cp-as-ftp-server-for-the-cpu-data)
- [Layout and structure of the FTP configuration list](#layout-and-structure-of-the-ftp-configuration-list)
- [Structure of the data blocks (file DBs) for FTP services - FTP server mode](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-server-mode)

#### Ethernet CP as FTP server for the CPU data

##### Reference

Data acquisition for automatic creation of a file allocation table in the "Properties &gt; General &gt; FTP configuration" parameter group.

With the information in the file allocation table, it is possible to address data blocks in one or more CPUs (up to 4) in an S7 station.

##### "Activate FTP server" option (only with certain CP types)

Select this option to allow FTP access to the S7 station via port 20/21 of the CP.

This option needs to be enabled to enable FTP access to file DBs on the CPU with the option described below.

FTP server access via Port 20/21 is enabled by default.

##### "Use FTP server for S7 CPU data" option

If you select this option, the file allocation table configured here is created on the CP when you download the project engineering data and store it in the /config folder of the file system of the CP.

An existing file_db.txt file is overwritten.

> **Note**
>
> **With security and the "Allow access only via FTPS" enabled, the following applies:**
>
> - The files are transferred encrypted.
> - For the user, the rights "FTP: Read files (DBs) from the S7 CPU" or "FTP: Write files (DBs) from the S7 CPU" must be activated.
> - If the firewall is activated, the FTP/FTPS protocols must be allowed.

##### Ethernet CP as FTP server for the S7 CPU data

To transfer data using FTP, you create data blocks on the CPU of your S7 station; due to their special structure, these are known here as file DBs.

When operating as an FTP server, if the Ethernet CP receives an FTP command, it checks a file allocation table (file file_db.txt) to find out how the data blocks used in the S7 station for file transfer are mapped to files.

You can create the file allocation table and transfer it to the CP as follows:

- With an entry in the parameter group "Properties &gt; FTP configuration" described here

  The file allocation table is then created in the FTP configuration based on this information and downloaded automatically to the CP along with the configuration data.
- By creating a file_db.txt file directly

  If you create the file allocation table in this way, you will need to load it to the CP using an FTP command.

The file allocation table file_db.txt is stored in the file system of the Ethernet CP in the /config directory.

---

**See also**

[Layout and structure of the FTP configuration list](#layout-and-structure-of-the-ftp-configuration-list)
  
[Structure of the data blocks (file DBs) for FTP services - FTP server mode](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-server-mode)

#### Layout and structure of the FTP configuration list

##### Layout and structure of the FTP configuration list for generating the file allocation table

The fields of the table in the FTP configuration have the following meaning and syntax:

| Titles in the table for FTP configuration | "CPU" | "DB" | File name | Comment |
| --- | --- | --- | --- | --- |
| **Meaning** | Rack/slot assignment of the CPU  Can be selected from a drop-down list; cannot be typed in. | Number of the data block  Entry can be typed in | File name assigned to the file DB  Automatic name proposal; entry can be typed in / modifiable. | Informal comment |
| **Example 1** | cpu1 [PLC_1] | 20 | cpu1_db20.dat | Measured values in the Plant1 area |
| **Example 2** | cpu2 [PLC_2] | 35 | Cpu2_db35.dat | Measured values in the Plant2 area |

##### Notes on the syntax

- Valid delimiters for the entries are "spaces".
- The following applies to the file name of a file DB:

  - The file name begins with "cpuX" (where X=1, 2, 3 or 4);
  - "cpuX" must first be defined in the rack/slot assignment;
  - Length: Maximum of 64 characters (including "cpuX");
- Maximum of 100 entries;
- Permitted characters: Letters "A-Z, a-z"; numbers "0-9", "_", "."

  > **Note**
  >
  > Keep to the notation (lower case for "cpu" and no leading spaces at the start of the row). Otherwise, the files will not be recognized.
  >
  > The tabulator is **not** permitted as the delimiter.

---

**See also**

[Ethernet CP as FTP server for the CPU data](#ethernet-cp-as-ftp-server-for-the-cpu-data)

#### Structure of the data blocks (file DBs) for FTP services - FTP server mode

##### How it works

To transfer data with FTP, create data blocks (file DBs) on the CPU of your S7 station. These data blocks must have certain structure to allow them to be handled as transferable files by the FTP services. They consist of the following sections:

- Section 1: File DB header (has a fixed length (20 bytes) and structure)
- Section 2: User data (has a variable length and structure) data type "FILE_DB_HEADER

##### Data type "FILE_DB_HEADER"

Using the "Add new block" function, you assign the type "FILE_DB_HEADER" to a data block directly.

##### File DB header for FTP server mode

Note: The file DB header described here is largely identical to the file DB header for client mode. The differences relate to the following parameters:

- WRITE_ACCESS
- FTP_REPLY_CODE

| Parameter | Type | Value / meaning | Supply |
| --- | --- | --- | --- |
| EXIST | BOOL | The EXIST bit indicates whether the user data area contains valid data.  The retrieve FTP command executes the job only when EXIST=1.  - 0:  The file DB does not contain valid user data ("file does not exist"). - 1: The file DB contains valid user data ("file exists"). | The dele FTP command sets EXIST=0;  The store FTP command sets EXIST=1; |
| LOCKED | BOOL | The LOCKED bit is used to restrict access to the file DB.  - 0: The file DB can be accessed. - 1: The file DB is locked. | The stor and retr FTP commands set LOCKED=1 when they are executed.  The following function is also possible when writing from the user program:  The user program on the S7 CPU can set or reset LOCKED during write access to achieve data consistency.  Recommended sequence in the user program:  1. Check LOCKED bit;  if = 0 2. Set WRITEACCESS bit = 0 3. Check LOCKED bit;  if = 0 4. Set LOCKED bit = 1 5. Write data 6. Set LOCKED bit = 0 |
| NEW | BOOL | The NEW bit indicates whether data has been modified since the last read access.  - 0: The content of the file DB is unchanged since the last write access. The user program of the S7 CPU has registered the last modification. - 1: The user program of the S7 CPU has not yet registered the last write access. | After execution, the stor FTP command sets NEW=1  After reading the data, the user program on the S7-CPU must set NEW=0 to allow store to be used again or to be able to delete the file with the dele FTP command. |
| WRITE_ACCESS | BOOL | 0: The FTP client on the PG/PC has no write access right for the file DBs on the S7 CPU.  1: The FTP client the PG/PC has the write access right for the file DBs on the S7 CPU. | During the configuration of the DB, the bit is set to an initialization value.  Recommendation:  Whenever possible, the bit should remain unchanged! In special situations, adaptation during operation is possible. |
| ACT_LENGTH | DINT | Current length of the user data area. The content of this field is only valid when EXIST = 1. | The current length is updated following write access. |
| MAX_LENGTH | DINT | Maximum length of the user data area (length of the entire DB less 20 bytes header). | The maximum length should be specified during configuration of the DB. The value can also be modified by the user program during operation. |
| FTP_REPLY_CODE | INT | This parameter is irrelevant in FTP server mode. | Is set to "0" by the FTP server. |
| DATE_TIME | DATE_AND_TIME | Date and time of the last modification to the file.  The content of this field is only valid when EXIST = 1. | The current date is updated following a write access. If the function for forwarding the time of day is used, the entry corresponds to the time that was passed on. If the function for forwarding the time of day is not used, a relative time is entered. This time relates to the startup of the IT-CP (the initialization value is 1.1.1994 0.0 (midnight)). |

---

**See also**

[Ethernet CP as FTP server for the CPU data](#ethernet-cp-as-ftp-server-for-the-cpu-data)

### I/O addresses

#### Reference

Setting the input/output addresses in the "Properties &gt; General &gt; I/O addresses" parameter group

#### Meaning

- Inputs, outputs

  Assign a start address to the module. (Outputs only if the option "Address setting for LOCK/UNLOCK with FETCH/WRITE" is selected)
- "Address setting for LOCK/UNLOCK with FETCH/WRITE" option

  Select this option if you want to use the access coordination function with the FCs LOCK/UNLOCK in FETCH/WRITE mode.

  This function uses process output via the backplane/P bus. As a result, the output addresses can be set as soon as this option is selected.

### Web

This section contains information on the following topics:

- [Web server of the module](#web-server-of-the-module)
- [Web diagnostics on the module](#web-diagnostics-on-the-module)

#### Web server of the module

##### "Activate Web server" option

The CP provides you with the functionality of a web server for access by means of a web browser. HTML pages with information and diagnostics functions are stored in the memory area of the CP for this.

Enable this option in order to obtain access to these HTML pages in the Web server of the CPU. When you enable the function, port 80 of the CP is released.

Web server access is enabled by default.

##### Web diagnostic options (availability depends on the CP type)

- "Display topology" option

  The option allows the display of topology information for the networked PROFINET IO interfaces of the CP in the Web server.

  To collect and store the topology information, additional memory is taken up on the CP. With complex project configurations making high demands on the memory resources, it may therefore be advisable to activate the option only temporarily for service purposes.
- "Download firmware via Web" option

  By enabling the option, the function for downloading the firmware of the CP from the download center is enabled in the Web server.

  This option is not restricted by the user administration if security is disabled. It is therefore recommended that the option is enabled only when required.
- "Reload of language files for the diagnostics displays via Web" option

  Diagnostics displays of the CPs are shown in plain language in the Web diagnostics buffer. These displays are language-specific.

  If you enable the option, the function for reloading missing language files from the download center is enabled in the Web server.

##### Automatic update / "Update interval"

If you select the "Enable" option, the CP updates the displayed Web pages at the selected intervals.

Range of values for the update interval 1 to 999 s

#### Web diagnostics on the module

##### Requirement:

Establish a physical connection between the programming device and the SIMATIC S7 station and set the PG/PC interface so that the module is accessible. Further help is available in the "Set PG/PC Interface" dialog box.

##### "Start of Web diagnostics"

Click the "Web diagnostics" button to display the result of the module diagnostics in the Web browser. The content is supplied by the integrated HTTP server of the module.

Start diagnostics in the Web browser in the "Properties &gt; General &gt; Web diagnostics" parameter group.

- "Access via" option

  From the "Access via" list, select the interface via which the CP is addressed.

  - Available interfaces can be selected in the drop-down list.
  - You can also enter an IP address.

> **Note**
>
> **With security functions enabled (if available)**
>
> If the option "Allow access only using HTTPS" is enabled, note the following:
>
> - The data is transferred encrypted.
> - The "Access to Web diagnostics" right must be activated for the user.
> - If the firewall is activated, the HTTP/HTTPS protocols must be allowed.

### SNMP

#### "Activate SNMP" option

If the "Activate SNMP" option is selected, communication using SNMP is enabled allowing read and write access to the module.

You can only select communication according to the SNMPv1 or SNMPv3 specification with modules that support Security functions:

- SNMPv1

  The SNMPv1 agent is enabled on the module. You can change the community strings for read and write access for SNMPv1 for modules that support Security functions.

- SNMPv3

  The SNMPv3 agent is enabled on the module. Further configuration options for encryption, authentication and the assignment of rights for STEP 7 users are available.

### OPC UA Security (CP)

This section contains information on the following topics:

- [Security profiles and certificate validation](#security-profiles-and-certificate-validation)

#### Security profiles and certificate validation

##### Security profiles of the OPC UA application

Depending on the CP type, the following security profiles of the OPC UA specification are supported by the OPC UA application of the CP:

- **SecurityPolicy**

  - SecurityPolicy ‑ None
  - SecurityPolicy ‑ Basic128Rsa15

    Signing and 128-bit encryption
  - SecurityPolicy ‑ Basic256

    Signing and 256-bit encryption
  - SecurityPolicy [A] ‑ Aes128-Sha256-RsaOaep

    Signing and 256-bit encryption with RSA-OAEP
  - SecurityPolicy [B] ‑ Basic256Sha256

    Signing and 256-bit encryption (SHA‑256)
  - SecurityPolicy ‑ Aes256-Sha256-RsaPss

    Signing with PSS and 256-bit encryption with RSA-OAEP

  The supplementary Conformance Units (Signing / Encryption) mean:

  - Sign

    The CP only allows communication with signed frames.
  - Sign and encrypt

    The CP only allows communication with signed and encrypted frames.

##### Certificate validation

In this parameter group you set the options for checking the certificates of the communications partner for the server or client application.

- **Checking the certificates**

  The CP generally checks the certificate of the communications partner, except when "SecurityPolicy ‑ None" is selected.

  If the partner certificate is invalid or is not trustworthy, communication is aborted.

  If the option is enabled, the two following options for restricting the checking routines can be activated.
- **No strict certificate validation**

  If the option is enabled, the CP allows communication in the following situations:

  - The IP address of the communications partner is not identical to the IP address in its certificate.
  - The use stored in the certificate (OPC UA client/server) differs from the function (OPC UA client/server) of the communications partner.
  - The current time on the CP is outside the period of validity of the partner certificate.

  Regardless of these exceptions, to establish a connection, at least the following requirements must be met:

  - The application URI sent by the requesting client must match the URI of the server application of the CP.
  - If the partner certificate is not trustworthy, the CP must at least have stored a self-signed certificate of the partner.
  - If the partner certificate was issued by several CAs, all CAs must be saved in the certificate store of the CP.
- **Do not check period of validity**

  If the options is enabled the CP checks the certificate of the communications partner. The CP also allows communication in the following situation:

  - The current time on the CP is outside the period of validity of the partner certificate.

If none of the options is enabled, no certificates are checked.

In particular for the establishment of the communication with third-party applications, note the information in the certificate management on importing certificates.

##### Special features for the client application of the CP 443-1 OPC UA

If you use the client function of the CP, note the following:

The value of the parameter "CheckServerCertificate" that you programmed in the connection information (UASessionConnectInfo) for the client program block "UA_Connect" is overwritten by the configured settings in the "Certificate validation" parameter group. If the client is to check the certificates of the communications partner (server), you can ignore the parameter in the UDT "UASessionConnectInfo". For the certificate check only the configured values of "Certificate validation" parameter group are relevant.

## PROFIBUS (S7-300, S7-400, PC)

This section contains information on the following topics:

- [Time-of-day synchronization (S7-300, S7-400, PC)](#time-of-day-synchronization-s7-300-s7-400-pc)
- [Field device parameter settings (data record routing) (S7-300, S7-400, PC)](#field-device-parameter-settings-data-record-routing-s7-300-s7-400-pc)
- [Configuring DP mode (S7-300, S7-400, PC)](#configuring-dp-mode-s7-300-s7-400-pc)
- [CP supports several DP slave types (S7-300, S7-400, PC)](#cp-supports-several-dp-slave-types-s7-300-s7-400-pc)

### Time-of-day synchronization (S7-300, S7-400, PC)

#### Reference

Configuring the time-of-day synchronization of PROFIBUS CPs.

#### Time-of-day synchronization

Decide whether or not the CP will forward time-of-day frames.

Depending on where the time master is located, the following two situations must be distinguished:

- Time-of-day frames come from the subnet and are forwarded to the station.
- Time-of-day frames come from the station and are forwarded to the subnet (LAN).

With some modules, specify the direction in which the time-of-day frames are forwarded. With modules for which forwarding can only be globally enabled or disabled, the CP can forward time-of-day frames in any direction.

If you have several CPs in your station, take into account the flow of time-of-day frames depending on the time-of-day master because you can forward time-of-day frames from one network to another network using the function described here making conflict situations possible.

If there is more than one CP in a station connected to the same network, only a single CP is allowed to forward time-of-day synchronization messages.

### Field device parameter settings (data record routing) (S7-300, S7-400, PC)

#### Reference

Setting the properties for PROFIBUS CPs in the "Properties &gt; Settings &gt; Field device parameter settings" parameter group.

#### Field device parameter settings (data record routing)

if you select this option, you can use the CP as a router for data records intended for field devices (DP slaves). Data records transferred by devices that are not connected directly to PROFIBUS and that therefore have no direct access to the field devices (DP slaves) can then be forwarded by the CP to the field devices.

SIMATIC PDM (Process Device Manager) is a tool that creates data records of this type for assigning parameters to field devices.

As default, this function is enabled. Since the function requires additional memory resources, you can turn off the option if you are putting a high load on the memory resources of the CP as a whole (connections etc.) and do not require the "Data record routing" function.

### Configuring DP mode (S7-300, S7-400, PC)

#### Reference

Depending on the module type, you configure the PROFIBUS mode in the following parameter group:

- S7-300/400 CPs, PC-CPs: Parameter group "Operating mode" (or "Properties &gt; General &gt; Operating mode".
- S7-1200/1500 CPs: Parameter group "PROFIBUS interface / DP interface &gt; Operating mode"
- LINK modules: Parameter group "DP/MPI interface &gt; Operating mode"

#### Relationship between CP mode and function of the module

The configurable DP modes and the functions made possible by them can be found in this table:

| Operating mode | Possible functions of the module |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | PG/OCM via PROFIBUS | FDL via PROFIBUS | DP master | DP slave | Configured S7 connections |
| No DP | X | X | ‑ | ‑ | X |
| DP master | X | X | X | ‑ | X |
| DP slave active (see below) | X | X | ‑ | X | ‑ |
| DP slave passive (see below) | ‑ | ‑ | ‑ | X | ‑ |

Key: "X" = Function supported; "-" = Function not supported

#### "Delay time"

For some modules in DP Master mode, you can set an additional delay for updating the DP I/O data. This delay time is used by the module to process other protocols such as FDL.

#### DP master class 2 (only some PC-CPs and IE/PB LINK HA)

In this operating mode, the module can read input and output data from any DP slaves that are not assigned to it.

This means, for example, that a process signal can be acquired by several DP masters and can help to save sensors in the field (shared input / shared output). Programming, diagnostic or management devices typically operate as DP class 2 masters.

#### IE/PB LINK HA

You can assign the "DP master class 2" mode to the LINK.

When this option is enabled, you can use the functions "Read data record" and "Write data record" for DP slaves of another DP master in the user program as well as access the cyclic input data of the external slaves.

The output data sent in the user program of the IE/PB LINK HA controller are discarded by the LINK in this operating mode.

- "DP master class 2"

  You can enable the option under the following conditions:

  - As with the external DP master system, the DP slaves of the external DP master system are additionally configured identically on the LINK, if necessary also via a GSD file. The external slaves are configured as if they were operated directly on the LINK as DP master.

    If the external DP master is a SIEMENS DP master, it must be configured on another PROFIBUS master system.
  - The PROFIBUS profile must be changed to "User-defined". You must enter exactly the bus parameters that the external DP master has calculated for its master system (taking into account an additional active station).

  CiR is not allowed in the "DP master class 2" mode. The LINK cannot be reloaded as "DP master class 2" in RUN mode.
- "Enable reading of the input data from DP slaves"

  You can optionally enable the reading of the input data of the external DP slaves.

  - Option disabled (default)

    If you do not need reading, disabling the option increases the communication speed.
  - Option enabled

    When enabled, the LINK can access the cyclic input data of the external DP slaves.

#### DP slave mode: Option "Test, Commissioning, Routing"

The name of the function varies depending on the CP type.

- Option enabled: DP slave active

  Select the check box if, for example, you want to use PG functions regularly over this interface for commissioning and testing. This selects the "DP slave active" mode. The interface is then involved in the token circulation of the PROFIBUS.

  The following functions are then possible (the name of the function can vary depending on the CP type):

  - Programming (for example loading)
  - Testing (status/modify)
  - S7 routing (I slave as gateway)
  - S5-compatible communication (SEND/RECEIVE interface)
  - S7 communication (only in server mode on connections configured at one end without communication blocks, configuration on partner)

  Note the following effects of "DP slave active" mode:

  - S7 connections for data exchange using communication blocks cannot be configured in this mode
  - This can extend the token rotation time.

    In time-critical applications and when S7 routing and client functionality are not required for communication, this option should therefore not be enabled.
- Option disabled: DP slave passive

  If the "Test, commissioning, routing" box is not checked, the "DP slave passive" CP mode is selected and the interface only operates as a server for communication services and is not involved in the token rotation on PROFIBUS.

  Server functionality means that only the partner (for example PG, OP or automation system) can initiate communication. Note the following features when the option is not enabled:

  - S7 routing is not possible.
  - Programming and testing are possible but slow (no extension of the bus token rotation time).

---

**See also**

[CP supports several DP slave types (S7-300, S7-400, PC)](#cp-supports-several-dp-slave-types-s7-300-s7-400-pc)

### CP supports several DP slave types (S7-300, S7-400, PC)

#### Reference

Setting the DP slave type for PROFIBUS DP in the "Properties &gt; General &gt; Operating mode" parameter group.

#### DP mode

On CPs that support different DP slave types, you can select the following DP modes depending on the CP type:

- DPV1 functionality (default mode)

  This includes DP slaves complying with the PROFIBUS DPV0 and DPV1 standard as well as Siemens DP slaves.

  This mode is only possible with certain CPU types. Refer to the information in the S7-CP manual for your PROFIBUS CP.
- DPV0 compatible

  This includes DP slaves complying with the PROFIBUS DPV0 standard; DP slaves complying with the DPV1 standard can only be used with restricted functionality.
- S7-compatible

  This includes DP slaves complying with the PROFIBUS DPV0 standard and Siemens DP slaves; DP slaves complying with the DPV1 standard can only be used with restricted functionality.

## CM/CP PROFIBUS (S7-1500)

This section contains information on the following topics:

- [Configuring time-of-day synchronization (S7-1500)](#configuring-time-of-day-synchronization-s7-1500)

### Configuring time-of-day synchronization (S7-1500)

#### Time-of-day synchronization roles of the communications module

With the time-of-day synchronization parameters, you specify the role of the communications module in the forwarding of time-of-day frames.

Depending on the mode of the module on PROFIBUS, the following synchronization roles can be set:

- The communications module is passive node on PROFIBUS (for example DP slave):

  - Slave
  - None
- The communications module is an active node on PROFIBUS:

  - Master
  - Slave
  - None

#### Meaning of the parameters

The parameters of the time-of-day synchronization have the following meaning.

- **Type of synchronization**

  The parameter specifies the synchronization role:

  - Slave

    The CM clock is synchronized with another clock. The synchronization frames come from PROFIBUS. With this type of synchronization, the CM forwards the time-of-day frames to the station at a fixed interval.

    Within the S7 station, there may be only one time-of-day slave.
  - Master

    The clerk of the communications module as master sends time-of-day frames to the PROFIBUS network.

    If the synchronization type "Master" is set, the interval for outputting time-of-day frames can be selected.
  - None

    There is no synchronization.

  If more than one module with a clock is present within a network, you need to specify which module will act as the time master and which as the time slave for time-of-day synchronization purposes. There can only be one time-of-day master.

- **Update cycle**

  With the synchronization role "Master", the parameter defines the update interval at which the time-of-day frames are output to the network.

## CPs settings that do not depend on the protocol or the network

This section contains information on the following topics:

- [Replacing a module without a PG](#replacing-a-module-without-a-pg)
- [Multiplexing OP connections / occupying internal CPU connection resources (S7-300)](#multiplexing-op-connections-occupying-internal-cpu-connection-resources-s7-300)

### Replacing a module without a PG

#### Reference

Making special settings in the "Properties &gt; General &gt; Settings" parameter group

Depending on the CP type, you will see the option "Module replacement without PG"

#### Effect - nonvolatile, long-term storage on the CPU

If you have selected this option, your configuration data is stored long-term in nonvolatile memory on the CPU instead of on the EEPROM of the CP. Remember, however, that even on the CPU such data is only retained long-term in the event of a failure if the CPU has a backup battery or a SIMATIC memory card is used.

#### Resource requirements on the CPU

If you select this option, you occupy additional resources on your CPU. When you load the user programs and the configuration data, you will be informed if there is not enough storage space available. Resource bottlenecks can be avoided by using a SIMATIC memory card.

> **Note**
>
> If you are faced with a lack of resources and do not want to use a SIMATIC memory card, you can also deselect this option and store the configuration data on the CP. Later, you can then create a SIMATIC memory card with the configuration data so that the "Module replacement without PG" option is enabled. If you then insert the SIMATIC memory card in the CPU, you can replace the CP at any time. The configuration data is then loaded from the CPU or from the SIMATIC memory card automatically when the CP starts up.

### Multiplexing OP connections / occupying internal CPU connection resources (S7-300)

#### Reference

Making special settings in the "Properties &gt; General &gt; Settings" parameter group

Depending on the CP type, you will see the option "Multiplex OP connections"

#### Multiplex mode

To connect TD/OPs and/or HMI devices, you can optimize the connection resources in the S7-300 CPU by allowing up to 16 such devices to communicate on a single CPU connection resource (multiplex mode).

If you do not use multiplex mode, the number of TD/OPs and/or HMI devices that can be used will depend on the number of available connection resources of the CPU used.

#### Use of internal CPU connection resources

Configured S7 connections via the CP use the same multiplex channel that you use in multiplex mode for HMI connections. This means that when you configure S7 connections, you already occupy one CPU connection resource.

> **Note**
>
> PG connections are not operated via the multiplexer; one connection resource is always occupied when you operate a PG.

> **Note**
>
> **Addressing in multiplex mode**
>
> In multiplex mode, the rack/slot assignment of the CP must be specified instead of the rack/slot assignment of the CPU when assigning addresses for TD/OP/HMI connections.
>
> Applications (for example ProAgent) that require block-related alarms (Alarm_S: SFC 17, SFC 18, SFC 19) are not supported in multiplex mode.

## Background on connections

This section contains information on the following topics:

- [Window Time and Inactivity Time - relation](#window-time-and-inactivity-time---relation)
- ["Immediate response when interrupted connection is detected" option](#immediate-response-when-interrupted-connection-is-detected-option)
- [Address information - E-mail connection](#address-information---e-mail-connection)
- [Symbols in offline status](#symbols-in-offline-status)
- [ISO-on-TCP connection: TSAP](#iso-on-tcp-connection-tsap)
- [Connection setup for FETCH/WRITE (S7-300, S7-400, PC)](#connection-setup-for-fetchwrite-s7-300-s7-400-pc)
- [S7 connection](#s7-connection)

### Window Time and Inactivity Time - relation

#### Relevance

ISO transport connections configuration in the parameter group "Properties &gt; General &gt; Dynamics".

#### Avoid connection abort with appropriate update

The partner station replies to keepalives with a frame. These are sent to the partner station at the intervals specified by the Window Time.

To avoid unwanted connection aborts, the Inactivity Time should be at least three times longer than the Window Time.

### "Immediate response when interrupted connection is detected" option

#### Meaning

If you set the "Immediate response when interrupted connection is detected" option, this means that if the connection is not available, the application immediately receives a code indicating that a communication job (FETCH or WRITE) cannot be executed. The code is sent regardless of whether or not a current attempt to establish the connections succeeds.

If you do not select this option, the application is informed of the nonavailability of a connection only when the connection times out.

The option described here is relevant and available only when the two modes listed below are used:

- The connection is configured as a permanent connection.

  Connections can be configured as permanently established connections (option in the "Details of connection establishment" tab). This means that jobs can be forwarded to the partner with the shortest possible reaction time without needing to establish the connection first.

  If there is a disruption on the connection, the system automatically attempts to re-establish the connection. In this situation, there may be delays before a message can be forwarded to the application.
- You are using the FETCH or WRITE job types (can be selected in the "Options" tab).

An immediate reaction is necessary only in certain situations with these job types if there is no connection.

### Address information - E-mail connection

#### Parameters for E-mail delivery

In "Properties &gt; Address details", you enter the parameters required for the delivery of the E-mail. You can set the following parameters:

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **Example** |
| E-mail server (SMTP) | Address of the mail server via which the E-mails are sent.   The IP address can be entered as an absolute address or symbolic name.   The following applies to symbolic names:   A valid name has 1 to 64 characters of which at least one character must be a letter.  If one or more "." characters are used, the following constraint also applies: A valid name must have 1 to 63 further characters after the last "."; here only the characters [a-z], [A-Z], [0-9] or [-] are permitted and at least one of these characters must be a letter.  A symbolic name can only be used if the Internet CP knows the address of the Domain Name System (DNS). A suitable entry is required in the configuration of the Internet CP in HW Config. For more detailed information, refer to the HW Config online help.  A maximum of 64 characters can be entered. | absolute: 140.80.0.4  symbolic name: t-online.de |
| Default sender name | Specifies an address that is always included in the E-mail as the sender address if the sender information (FROM parameter) is empty in the header of the E-mail.  This information is normally irrelevant for delivery of the mail. It is simply information for the mail recipient. Since some mail servers do not forward jobs if there is no sender information, **it is advisable to enter information here!**  A maximum of 126 characters can be entered.   **Note:**  Remember that a default sender name must be specified if you want a test mail to be initiated by diagnostics. | Station2.CPU412@xy.factory2.de |

### Symbols in offline status

#### Symbols in the offline status

The offline status of a connection is shown as follows:

| Symbol | Meaning / connection status |
| --- | --- |
| ![Symbols in the offline status](images/9840317451_DV_resource.Stream@PNG-de-DE.png) | Consistent - connection configuration can be loaded |
| ![Symbols in the offline status](images/9840180747_DV_resource.Stream@PNG-de-DE.png) | Inconsistent - connection configuration cannot be loaded |

### ISO-on-TCP connection: TSAP

#### TSAP format

ISO-on-TCP connections have a TSAP length of 1 to 16 bytes. When you are entering values, the current length is displayed automatically. You can enter local TSAPs and partner TSAPs as a hexadecimal value or as an ASCII string. If you opt for ASCII, the characters you enter are also displayed in hexadecimal format. If you enter them in hexadecimal, any printable characters are displayed as ASCII values (8 hexadecimal characters are visible). If you enter non-printing characters, the ASCII display is disabled (ASCII entry is no longer possible), and the non-printing characters appear as dots.

> **Note**
>
> **TSAP length**
>
> Do not use length 1 or 2 TSAPs, as these TSAPs are already used for internal purposes.

#### Local TSAPs and partner TSAPs

Partner and local TSAPs may be the same, since the connection is unique due to the different IP addresses. If you have to set up more than one connection between two devices, then the TSAPs must also be different.

#### Default TSAPs

For configuring the local and partner TSAPs, there is an "ISO-on-TCP-1" default value for the first connection between two partners (can be changed). The default value "ISO-on-TCP-2" is then suggested for a new connection between the same partners. ISO-on-TCP-1 is then suggested for a new connection with a new partner.

### Connection setup for FETCH/WRITE (S7-300, S7-400, PC)

#### Relevance

ISO transport connections / ISO-on-TCP connections / TCP connections configuration in the parameter group "Properties &gt; General &gt; Options".

#### How connection establishment affects FETCH/WRITE

Please note the following points for FETCH/WRITE mode:

- For S7 stations:

  If you want to use FETCH/WRITE mode (see the "Options" parameter group), clear the "Active connection establishment" option.
- For PC stations / OPC servers:

  If you want to use FETCH/WRITE mode (see the "Options" parameter group), enable the "Active connection establishment" option.

### S7 connection

This section contains information on the following topics:

- [OPC connection parameters for time monitoring](#opc-connection-parameters-for-time-monitoring)
- [OPC connection parameters for the connection state](#opc-connection-parameters-for-the-connection-state)
- [Optimizing write access, optimizing read access](#optimizing-write-access-optimizing-read-access)
- [One-way S7 connection option](#one-way-s7-connection-option)
- [OPC server - alarms](#opc-server---alarms)

#### OPC connection parameters for time monitoring

##### Connection timeout

If there is no reply to a request for a connection from a communication partner within the time set here, OPC jobs are cancelled with an error message. Values from 2,000 to 100,000 ms can be set.

Since successful establishment of a connection can take some time depending on the network structure, the connection establishment timeout should be longer than the job timeout.

The connection timeout starts with the start of the request for the connection. This time depends on the configuration of the connection characteristics (see above). Two cases are possible:

- **Keeping the connection established permanently:** In this case, the connection establishment request begins with the start of the OPC server for the S7 protocol. This start is triggered by connecting an OPC client to the OPC server and searching the S7 namespace and/or by adding and actively monitoring an S7 item.
- **Connection when required:** The request for connection establishment starts with the first access to tags of this S7 connection.

If the S7 connection is interrupted in running operation, an attempt is made to reestablish the connection. This resets and restarts the connection timeout.

##### Job timeout

Network jobs directed to the partner device are monitored by the job timeout. If no response is issued to a network job within the job timeout, the corresponding OPC jobs are cancelled with an error message. Values from 1 to 100,000 ms can be set.

The job timeout starts at the time a network job is sent in the OPC server. In general, there is only an indirect relationship between write/read/monitor jobs at the OPC interface. Several OPC items can be handled for each network job. Additionally, several OPC clients can request the same OPC item for each network job.

Furthermore, the "Optimize write access" and "Optimize read access" parameters play a role because several OPC jobs can be assembled there on the network level.

#### OPC connection parameters for the connection state

##### Immediate response when interrupted connection is detected

Can only be enabled if the "Maintain connection permanently" option is selected. The immediate reporting of S7 connections that have not been established with OPC jobs, means that you avoid repeated job timeouts.

Functional description: An interrupted connection is detected and the connection stored. If the connection has not yet been established or it is currently being attempted to re-establish an uninterrupted connection, OPC jobs are replied to immediately with an error message to this effect. The error message is sent without waiting for the job or connection timeout.

#### Optimizing write access, optimizing read access

##### Principle

When accessing variables over S7 connections, the OPC Server for SIMATIC NET provides an optimization algorithm to increase the data transmission speed.

Several simultaneous jobs to access individual variables are converted internally to create a single access to an array on the communication partner. This reduces the number of data packets transported over the network. Utilization of single packets is improved and the payload of a packet is increased.

This optimization is used for both read and write access and is enabled as the default setting. For the OPC client, for example an OPC-compliant HMI device, this optimization algorithm is invisible.

In order to be able to ensure the read or write processing of the S7OPT data within a CPU cycle, you must set the value for the parameter "Buffer size for optimization" in the OPC properties of the S7 connection less than or equal to 64 bytes for an S7-1200 CPU (firmware version V4.0 or higher) or less than or equal to 512 bytes for an S7-1500 CPU (firmware version V2.0 or higher). For an S7-1500 CPU where the firmware version is less than V2.0, you must set the parameter less than or equal to 64 bytes.

##### Further information

Additional details are contained in the documentation for the OPC server:

- Industrial communication with the PG/PC Band 1 under the entry ID: [42783968](http://support.automation.siemens.com/WW/view/en/42783968)
- Industrial communication with the PG/PC Band 2 under the entry ID: [42783660](http://support.automation.siemens.com/WW/view/en/42783660)

#### One-way S7 connection option

##### Meaning

If the "One-way" check box is selected, only one-way communication blocks can be used on this connection ("PUT" and "GET" instructions) in the user program of an S7 CPU. One-way means that the connection partner functions as a server on this connection and cannot send or receive actively.

Communications instructions used at both ends (with "pairs of blocks") cannot be used on connections configured at one end; for example [USEND](S7%20communication%20%28S7-300%2C%20S7-400%29.md#usend-send-data-uncoordinated-s7-300-s7-400) and [URCV](S7%20communication%20%28S7-300%2C%20S7-400%29.md#urcv-receive-data-uncoordinated-s7-300-s7-400), [BSEND](S7%20communication%20%28S7-300%2C%20S7-400%29.md#bsend-send-data-in-segments-s7-300-s7-400) and [BRCV](S7%20communication%20%28S7-300%2C%20S7-400%29.md#brcv-receive-data-in-segments-s7-300-s7-400) or [USTATUS](S7%20communication%20%28S7-300%2C%20S7-400%29.md#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400).

Since communication options are generally clearly defined based on the connection end points, the check box is preset and it may not be possible to change it.

##### Example 1:

The check box is grayed out (cannot be changed) and enabled in the following configuration:

- The local connection end point is an S7-400 CPU or an S7-300 CPU with loadable S7 communication (via CP) and the partner connection end point is an S7-300 CPU without loadable S7 communication.

##### Example 2:

The check box is grayed out (cannot be changed) and not enabled in the following configuration:

- The local connection end point and the partner connection end point are S7-400 CPUs.

  In this case, STEP 7 automatically creates a two-way connection. An ID (local ID and partner ID) is entered for both the local end point and the end point of the connection partner.

---

**See also**

[GET: Read data from a remote CPU (S7-1200, S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#get-read-data-from-a-remote-cpu-s7-1200-s7-1500)
  
[PUT: Write data to a remote CPU (S7-1200, S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#put-write-data-to-a-remote-cpu-s7-1200-s7-1500)
  
[GET: Read data from a remote CPU (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#get-read-data-from-a-remote-cpu-s7-300-s7-400)
  
[PUT: Write data to a remote CPU (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#put-write-data-to-a-remote-cpu-s7-300-s7-400)

#### OPC server - alarms

##### Block-related alarms and diagnostic alarms

The options act as filters so that you can set the specific type of alarm that can arrive via the S7 connection.

The communication partner generates block-related alarms with the Alarm_8, Alarm_S or Alarm_SQ blocks.

Block-related alarms can be signaled

- As conditional events
- As simple events (simple events for compatibility with older applications that do not generally expect conditional events).

If you select "Block-related alarms", the OPC server then registers for alarm messages on this connection. The received alarms are transferred via the Alarms&amp;Events OPC interface.

Diagnostic alarms are derived from the system status list (SSL) of the S7 device. Diagnostic events that have not yet been reported to the OPC client are reported if it has registered for diagnostic alarms. Diagnostic events have no status and do not therefore need to be acknowledged.

Functions to set the priority for single alarm messages and diagnostics alarms can be reached via the area navigation.

##### Further information

Additional details are contained in the documentation for the OPC server:

- Industrial communication with the PG/PC Volume 1 in contribution ID: [42783968](http://support.automation.siemens.com/WW/view/en/42783968)
- Industrial communication with the PG/PC Volume 2 in contribution ID: [42783660](http://support.automation.siemens.com/WW/view/en/42783660)

## IE/PB LINK

This section contains information on the following topics:

- [PROFINET device number](#profinet-device-number)
- [Operating modes of the IE/PB LINK](#operating-modes-of-the-iepb-link)

### PROFINET device number

#### Reference

Display and setting of the properties for PROFINET IO devices on the DP master system of an IE/PB LINK PN IO in the "Properties &gt; General &gt; PROFINET device number" parameter group.

#### Parameters

To allow you to recognize the assignment better, STEP 7 attempts to assign the same digits for the device number and the PROFIBUS address when the DP slave is placed in the DP master system. As default, the "Use PROFIBUS address as device number" option is therefore active as long as no device number has yet been assigned that corresponds to the current PROFIBUS address.

> **Note**
>
> **Unique device numbers**
>
> Remember that the device numbers assigned in a PROFINET IO system must be unique. The IO devices (DP slaves) connected to the DP master system of the IE/PB LINK PN IO must also be included.

- **PROFIBUS address**

  Display of the PROFIBUS addresses of the DP slaves connected to the DP master system.
- **Name**

  Display of the device names of the DP slaves connected to the DP master system. Cannot be changed here.
- **PROFINET device number**

  Display or selection of the PROFINET device numbers of the DP slaves connected to the DP master system. As default, the PROFINET device number is adopted from the PROFIBUS address.

  If the option "Use PB address as device number" is deactivated, the PROFINET device number can be changed. The range of values depends on the IO controller being used.

  If you activate the "Use PROFIBUS address as device number" option again after specifying the device number, the value will be reset accordingly.
- **Use PB address as device number**

  If the option is deactivated, the PROFINET device number can be changed.
- **Prioritized startup**

  Speeds up the startup of the PROFINET IO device (here of the DP slave as PROFINET IO device). The option can only be selected if the controller supports prioritized startup.

  You can select the option for a maximum of eight DP slaves connected to the DP master system.

### Operating modes of the IE/PB LINK

#### Validity and module name

The information provided below applies to the following modules:

- IE/PB LINK PN IO
- IE/PB LINK HA
- IWLAN/PB LINK

If functions apply to all of these modules, they are referred to in the short form "LINK".

If a function applies to only one module, the entire module name is named.

#### Configuring the type of gateway

Configuration in the "Gateway" parameter group

You can use the LINK in the following operating modes:

- **Network gateway as PROFINET IO proxy**

  From the perspective of the PROFINET IO controller on Industrial Ethernet, there is no difference in the access to PROFINET IO devices connected to Industrial Ethernet and to PROFIBUS DP slaves connected to PROFIBUS DP.

  The LINK adopts the role of a proxy for the DP slaves connected to PROFIBUS DP (DP mode "DP master" is active).
- **Network gateway in standard mode**

  In this operating mode, you have the following connection options:

  - PG/OP communication

    PG/OP communication is used to download programs and configuration data, to execute test and diagnostics functions and for operator control and monitoring (HMI systems) of a plant.
  - Field device parameter settings (data record routing)

    You can use the LINK as a router for data records intended for field devices (DP slaves). This allows devices that are not directly connected to PROFIBUS network and that therefore do not have direct access to the field devices (DP slaves) to transfer data records to the field devices via the LINK.

    A tool that generates such data records for configuring field devices is, for example, SIMATIC PDM (Process Device Manager).
  - Gateway to a DP master system with constant bus cycle time

    The LINK serves as a gateway between Ethernet and the field devices of a DP master system. The LINK is operated as an active node along with a DP master on PROFIBUS configured for a constant bus cycle time.
  - Cross-subnet S7 connections for HMI operation

    The LINK forwards communication via S7 connections.

    This service is used, for example, by HMI applications (PC stations).

#### Configuring DP mode

Configuration of the operating mode of the IE/PB LINK in the parameter group "DP/MPI interface &gt; Operating mode"

For additional details, see [Configuring DP mode](#configuring-dp-mode-s7-300-s7-400-pc).

#### S7 routing via IE/PB LINK PN IO V2.1 (6GK1411‑5AB00)

Routing via the IE/PB LINK PN IO is not possible in the following situations:

- S7 routing between two S7-1500 CPUs
- S7 routing of PG connections to S7-1200/1500 CPUs
- S7 routing of HMI connections to S7-1200/1500 CPUs

This behavior affects the IE/PB LINK PN IO with firmware version V2.1 (6GK1 411-5AB00).

---

**See also**

[Configuration with IE/PB LINK](Configuring%20devices%20and%20networks.md#configuration-with-iepb-link)
