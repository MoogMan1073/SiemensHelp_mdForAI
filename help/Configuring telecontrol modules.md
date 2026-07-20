---
title: "Configuring telecontrol modules"
package: HWSimNetCMCP2MenUS
topics: 185
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring telecontrol modules

This section contains information on the following topics:

- [Configuration](#configuration)
- [Additional information on mobile wireless CPs](#additional-information-on-mobile-wireless-cps)
- [Online &amp; diagnostics](#online-diagnostics)
- [Block library Telecontrol ST7](#block-library-telecontrol-st7)

## Configuration

This section contains information on the following topics:

- [Communication types](#communication-types)
- [Basic settings](#basic-settings)
- [Time-of-day synchronization](#time-of-day-synchronization)
- [Ethernet interface](#ethernet-interface)
- [Serial interface](#serial-interface)
- [Web server](#web-server)
- [Partner stations](#partner-stations)
- [Communication with the CPU](#communication-with-the-cpu)
- [Subscriber numbers](#subscriber-numbers)
- [Protection](#protection)
- [Telecontrol connections](#telecontrol-connections)
- [Security](#security)
- [Data point editor](#data-point-editor)
- [Message editor](#message-editor)
- [Protocol-specific parameters](#protocol-specific-parameters)

### Communication types

This section contains information on the following topics:

- [Communication types](#communication-types-1)

#### Communication types

In this parameter group, you enable the communication types you want to use for the particular module.

To minimize the risk of unauthorized access to the station, you need to enable the communications services that you want to use with the module individually.

You can leave all options disabled if you do not need them, for example if you only use a CP to send SMS messages or for Open User Communication.

##### "Communication types" parameter group

- **Enable telecontrol communication**

  In the module, enables the telecontrol communication.

  > **Note**
  >
  > **Full telecontrol functionality only with enabled security functions**
  >
  > If the module supports security functions, you must activate the security functions to use the following functions:
  >
  > - Sending e-mails using the telecontrol functionality
  > - Use of the "TeleControl Basic" (general) protocol
  > - Use of the DNP3 security functions
  > - Use of certificates

  > **Note**
  >
  > **Loss of configuration data when changing the telecontrol protocol**
  >
  > If you change the protocol on a configured module, protocol-specific configuration data is lost. Among other things, this includes the following:
  >
  > - Partner configuration
  > - Data point configuration
  > - Configured messages (e-mails / SMS messages)
  > - Configured time-of-day synchronization
  > - Configured VPN partner

  Depending on the module type, the following protocols can be used:

  - TeleControl Basic *****

    Enables communication with the telecontrol server.
  - ST7

    Enables communication with a control system that supports the ST7 protocol.
  - DNP3 *****

    Enables communication with up to four DNP3 masters.
  - IEC 60870‑5‑104 *****

    Enables communication with up to four IEC masters.

  ***** For telecontrol communication via SINEMA Remote Connect see the following section.

  For configuration of the telecontrol connections for the ST7, DNP3 and IEC protocols, see section [Telecontrol connections](#telecontrol-connections).

  You can find a description of important parameters and functions of the telecontrol protocols in the section [Protocol-specific parameters](#protocol-specific-parameters).
- **Enable online functions**

  In the module enables access to the CPU for the online functions (diagnostics, loading project data etc.). If the function is enabled, the engineering station can access the CPU via the module.

  If the option is disabled, you have no access to the CPU via the module with the online functions. Online diagnostics of the CPU with a direct connection to the interface of the CPU however remains possible.
- **Enable S7 communication to the CPU**

  Enables the functions of S7 communication with the assigned SIMATIC CPU and the S7 routing.

  If you configure S7 connections to the relevant station, and these run via the communications module, you need to enable this option for the communications module.

  S7 routing is supported by the following modules:

  - CP 1243‑1, CP 124x‑7, CP 1243‑8

    As of CP firmware V2.1 with CPU ≥ V4.2
  - CP 1542SP‑1, CP 1542SP‑1 IRC, CP 1543SP‑1

    As of CP firmware V1.0 with CPU ≥ V2.0
- **Enable SMS**

  (only mobile wireless CPs)

  Enables sending and receiving of SMS messages.

  As of firmware version V2, the function can be enabled regardless of whether telecontrol communication is enabled.

##### Remote maintenance with SINEMA Remote Connect (SINEMA RC)

The application "SINEMA Remote Connect" (SINEMA RC) is available for remote maintenance purposes.

SINEMA RC uses OpenVPN for encryption of the data. The center of the communication is SINEMA RC Server via which communication runs between the subscribers and that manages the configuration of the communications system.

**Usable modules and telecontrol protocols**

The following CPs support communication via SINEMA RC:

- CP 1243‑1, CP 1243‑7, CP 1243‑8

  As of firmware V3.1
- CP 1542SP‑1 IRC, CP 1543SP‑1

  As of firmware V2.0

VPN-capable telecontrol CPs can also handle telecontrol communication via the SINEMA RC server. The following telecontrol protocols support communication via SINEMA RC:

- TeleControl Basic
- DNP3
- IEC 60870‑5‑104

**Applications and configuration**

Make the following settings for using SINEMA Remote Connect and telecontrol communication via SINEMA RC:

1. Communication via SINEMA RC: Parameter group "Security &gt; VPN"

   Activate VPN so that the other parameters become visible.
2. Telecontrol communication via SINEMA RC: "Communication types" parameter group

   Communication via SINEMA RC must be enabled beforehand.

The following application cases result from the combination of telecontrol communication and the use of SINEMA RC:

- (1) No telecontrol communication and no SINEMA RC CP for network separation.
- (2) CP only for remote maintenance via SINEMA RC
- (3) CP for telecontrol communication only
- (4) CP uses telecontrol communication, but SINEMA RC only for remote maintenance.
- (5) CP uses SINEMA RC for telecontrol communication and remote maintenance.

The table provides an overview of the applications with the parameter settings.

Use cases and parameters to be activated

| Use case | Parameter settings *   **(parameter abbreviated)** |  |  |
| --- | --- | --- | --- |
| SRC | TC | TC + SRC |  |
| (1) | Off | Off | Off |
| (2) | On | Off | Off |
| (3) | Off | On | Off |
| (4) | On | On | Off |
| (5) | On | On | On |
| ***** Explanation of the parameter abbreviations:   **SRC** ‑ Security &gt; VPN (activated) &gt; "VPN connection type":          "Automatic OpenVPN configuration via SINEMA Remote Connect Server"   **TC** ‑ Communication types &gt; Telecontrol communication enabled   **TC + SRC** ‑ Communication types &gt;                "Activate telecontrol communication via SINEMA Remote Connect" |  |  |  |

##### Telecontrol communication via SINEMA Remote Connect

**Steps in configuration**

Follow the steps below when configuring the CP for use of telecontrol communication via SINEMA RC:

1. In the "Communication types" parameter group activate telecontrol communication and select one of the protocols named above.

   The option for communication via SINEMA RC is not yet visible.
2. Change to the "Security" parameter group and enable the security functions.

   (In the "Communication types" parameter group the SINEMA RC option appears disabled and grayed out)
3. Open the "Security &gt; VPN" parameter group and enable VPN.
4. For the parameter "VPN connection type" select the option "Automatic OpenVPN configuration via SINEMA Remote Connect Server" if this is not preset.

   (In the "Communication types" parameter group the SINEMA RC option becomes usable.)
5. Change to the "Communication types" parameter group and set the checkmark for the option "Activate telecontrol communication via SINEMA Remote Connect".

   The CP is now prepared for telecontrol communication via SINEMA Remote Connect.
6. Create the remaining configuration of the SINEMA RC Server in "Security &gt; VPN".
7. Import the certificate of the SINEMA RC Server in "Security &gt; Certificate manager".

**Configuration of connection establishment**

The connection establishment is configured in the "Security &gt; VPN &gt; Optional settings" parameter group with the parameter "Connection type".

- **Update interval**

  With this parameter you set the interval at which the CP queries the configuration on the SINEMA RC Server.

  Note that with the setting 0 (zero) changes to the configuration of the SINEMA RC Server may result in the CP no longer being capable of establishing a connection to the SINEMA RC Server.
- **"**
  **Connection type**
  **"**

  The two options of the parameter have the following effect:

  - Permanent

    The option is intended for permanent communication.

    This is, for example, the case with telecontrol communication via SINEMA RC. The CP and the communications partner of the CP must be configured in the SINEMA RC Server.
  - PLC trigger

    The option is intended for sporadic communication of the CP via the SINEMA RC Server.

    You can use this option when you sporadically want to establish temporary connections between the CP and the engineering station (PC with the STEP 7 project of the CP), for example for service work.
- **PLC tag for connection establishment**

  If the option "PLC trigger" is selected, the CP establishes a connection when the PLC tag changes to the value 1. During operation the PLC tag can be set when necessary, for example using an HMI panel.

  When the PLC tag is reset to 0, the connection is terminated again.

### Basic settings

This section contains information on the following topics:

- [Configuration](#configuration-1)

#### Configuration

The parameter group is only available for some communication modules of the SINAUT ST7 system.

For the supported modules, see section [Expansion of SINAUT projects](#expansion-of-sinaut-projects).

##### Telecontrol configuration

This is where you define the procedure for configuring the subscriber and SINAUT connection data for the communication module.

- Configure

  The above-mentioned configuration data is configured in the parameter groups of the module and in the connection editor.
- Import

  The above-mentioned configuration data is configured for a proxy module in STEP 7 V5.

  The STEP 7 V5 configuration data of the proxy module is imported into STEP 7 Professional for the module.

  For information on importing and the scope of the imported data, see section [Import partner configuration (ST7 protocol)](#import-partner-configuration-st7-protocol).

> **Note**
>
> **Deletion of configuration data**
>
> Define one of the two options before you continue configuring the module.
>
> If you change the parameter later, all configuration data up to that point will be discarded.

### Time-of-day synchronization

This section contains information on the following topics:

- [Time synchronization](#time-synchronization)
- [Time-of-day synchronization with NTP](#time-of-day-synchronization-with-ntp)

#### Time synchronization

> **Note**
>
> **Recommendation: Time-of-day synchronization only by 1 module**
>
> Only have the time of day of a station synchronized from an external time source by a single module so that a consistent time of day is maintained within the station.
>
> When the CPU takes the time from the CP, disable time-of-day synchronization of the CPU.
>
> **CP 1542SP‑1 IRC**
>
> As of firmware version V2.1 of the CP, only 1 module in the station can be time client. This module distributes the time of day within the station.

##### Time-of-day synchronization and security

If you enable the security functions in modules with security, you will find the parameter group under "Security".

When security functions are enabled, you need to regularly synchronize the time of day of the communications module.

##### Validity

The functions described below apply to:

- S7‑1200

  - CP 1243‑1
  - CP 1242‑7
  - CP 1243‑7 LTE
  - CP 1243‑8
- ET 200SP

  - CP 1542SP‑1
  - CP 1543SP‑1
  - CP 1542SP‑1 IRC
- TIM 1531 IRC

##### Time-of-day concept

Before configuring time-of-day synchronization, specify the following:

- Specify the time source in the network.
- Specify the time server in the network.
- Specify the network or networks via which the time of day will be forwarded by the time server to the time clients.

##### Synchronization method

When an external time source is used, the S7 station can obtain the current time both via the CPU and via a communications module.

There is no forwarding of the time of day from the station to the subnet for CPs.

**Time-of-day synchronization of the CPU**

As the synchronization method, with the CPU only NTP can be selected.

For the time-of-day synchronization of the CPU via a CP see below.

For the following CPs, the time can be taken once during startup (commissioning).

- S7‑1200 as of V3.4
- ET 200SP as of V2.3

You will find the option in the parameter group "Communication with the CPU &gt; CP time".

**Time synchronization of communications modules**

Depending on the device type and the telecontrol protocol, the following synchronization methods can be selected for the modules:

- **NTP**

  The module obtains the time from one or more NTP servers.

  For information on the configuration, see [Time-of-day synchronization with NTP](#time-of-day-synchronization-with-ntp).
- **Time from the CPU**

  If no time source is configured at the CP, the following mechanisms apply.

  - S7‑1200

    If the option "CPU synchronizes the modules of the device" is enabled for the CPU under "PROFINET interface &gt; Time synchronization", all CMs/CPs of the station are synchronized with the CPU time.
  - ET 200SP

    If the time-of-day synchronization of the CP is disabled, CPs with firmware version ≥ V2.1 are automatically synchronized in a cycle of 10 seconds by a CPU with firmware version ≥ V2.0.

    For CPs with firmware version ≤ V2.0, the CP reads the CPU time once during start-up, even if the option "No time source" is selected as Time source. The subsequent time synchronization then depends on the configured synchronization method.

For telecontrol CPs, the following synchronization methods are available when telecontrol communication is enabled:

- **S7‑1200**

  - **From local station**

    Validity: ST7

    The CP adopts the time of day of the CPU.
  - **Time from partner**

    Validity: TeleControl Basic, DNP3, IEC

    The CP adopts the time of day from a communication partner. Under TeleControl Basic, this is always the telecontrol server.
  - **Time from CPU**

    The CP adopts the time of day of the CPU.
- **ET 200SP**

  - **From local station**

    Validity: All supported telecontrol protocols

    The CP adopts the time of day of the CPU.
  - **From WAN**

    Validity: ST7

    The CP adopts the time of day from the WAN.
  - **Time from partner**

    Validity: TeleControl Basic, DNP3, IEC

    The CP adopts the time of day from a communication partner. Under TeleControl Basic, this is always the telecontrol server.
  - **No time source**

    The CP is not synchronized.

  For CPs with firmware version ≤ V2.0, the CP reads the CPU time once during start-up, even if the option "No time source" is selected as Time source. The subsequent time synchronization then depends on the configured synchronization method.
- **TIM 1531 IRC**

  - **From WAN**

    Validity: All supported telecontrol protocols

    The TIM adopts the time of day from the WAN.

    Time servers can be:

    ‑ A synchronized CPU

    ‑ A subscriber with a time receiver

    ‑ A master station PC (e.g. ST7cc/ST7sc) connected to the Ethernet network.
  - **Time from partner**

    Validity: All supported telecontrol protocols

    The CP adopts the time of day from a communication partner.

##### "Time" parameter group

The functions of this parameter group are valid for:

- CP 1242‑7, CP 1243‑1, CP 1243‑7 LTE, CP 1243‑8 as of firmware version V3.5
- CP 154xSP‑1 as of firmware version V2.3
- TIM 1531 IRC as of firmware version V2.4

The communication module can take the time zone from the CPU using the following option:

- Take time zone values with daylight saving time from PLC

  When the option is enabled, the communication module takes the time zone from the CPU.

  When the option is disabled, the time zone of the communication module can be configured independent of the CPU.

  TIM 1531 IRC: The option is activated if the CPU has been assigned to the TIM (parameter group "Subscriber numbers").
- Time zone

  Here you set the local time zone that the communication module will use.

  If the "Take time zone values with daylight saving time from PLC" option is enabled, then this option is disabled and the module takes the values of the CPU.
- Use UTC

  Only when using the ST7 of IEC telecontrol protocol

  When these protocols are used, the time stamps are interpreted as local time.

  The CPU, on the other hand, expects UTC.

  When using the ST7 and IEC telecontrol protocols, enable this option if the module is to use UTC time.

If the communication module does not take the time from the CPU, you can configure the changeover between daylight saving time and standard time.

- Activate daylight saving time

  Activates the time changeover.
- Difference between standard and daylight saving time

  Time difference in minutes between daylight saving time and standard time
- Start of daylight saving time / standard time

  Here you configure when each time changeover starts: week of the month, day of the week, month and time

##### Forwarding the time from the CP to the CPU

> **Note**
>
> **Forwarding the time to the CPU**
>
> Depending on the firmware version of the modules involved, the time-of-day of the CP can be forwarded to the CPU in different ways.
>
> - Optional forwarding of the CP time to the CPU using a PLC tag:
>
>   - S7‑1200
>   - ET 200SP
> - Forwarding of the CP time via the backplane bus to the CPU from the firmware versions mentioned below:
>
>   - S7‑1200
>   - ET 200SP

The forwarding of the CP time to the CPU depends on the firmware version of the CP and the CPU. Note the following behavior.

- **Forwarding of the CP time via PLC tag**

  With the following firmware versions this is the only option for forwarding the clock time from the CP to the CPU:

  - S7‑1200: CP firmware ≤ V2.1.5
  - ET 200SP: CP firmware ≥ V2.0

  With this firmware version the CP can make the time-of-day available to the CPU as an option via a PLC tag. When this PLC tag is read cyclically by the CPU, the CPU adopts the CP time.

  Configure the PLC tag in the parameter group "Communication with the CPU" of the CP.
- The CP time is automatically forwarded to the CPU, when a synchronization method is configured at the CP, and CP and CPU have one of the following firmware versions:

  - S7‑1200: CP firmware ≥ V3.0 and CPU firmware ≥ V4.2

    If the option "CPU synchronizes the modules of the device" is enabled for the CPU in "PROFINET interface &gt; Time synchronization", all smart modules of the station are synchronized with the CPU time.
  - ET 200SP: CP firmware ≥ V2.1 and CPU firmware ≥ V2.0

  Since the CPU automatically adopts the CP time, you no longer require for these firmware versions the forwarding option using the PLC tag.

##### Forwarding time of day by the TIM

The TIM can forward its time of day as follows:

- **To connected networks**

  Configuration with "Time-of-day synchronization" &gt; "Send time" or "Receive time"

  The procedure for configuration differs in Ethernet and classic WAN networks, see below.
- **To the assigned CPU**

  Configuration with "Time-of-day synchronization" &gt; "Send time"

##### Configuration with the TIM and with WAN networks

**Parameter groups for time-of-day synchronization**

For configuring the time-of-day synchronization, the following parameter groups are available:

- **TIM**

  - **Receive time**

    Here you specify the connected network via which the TIM will receive the time of day.

    ‑ Master station TIM: Usually from NTP server or via the control center

    ‑ Node station / Station: Definition of the interface via which the time is received.
  - **Send time**

    ‑ Master station TIM (time server): Definition of the networks to which the TIM forwards the time.

    ‑ Node station: Definition of the interface via which the time is received from the master station TIM.
- **Classic WAN**

  For classic networks, the "Time-of-day synchronization" is enabled in the parameter group of the same name. You also specify the synchronization cycle here.

  The settings for synchronization are then adopted by all connected TIM modules.

  The send direction of the time-of-day frames is derived automatically from the network node type of the connected interfaces:  
  Master station ⇒ Node station ⇒ Station

The settings for the network are not necessary with time-of-day synchronization via Ethernet.

##### Configuration on the Ethernet interface of the TIM

**Time server**

1. In the "Receive time" parameter group, configure the TIM that will be the time server and configure the time source using one of the following options:

   - From NTP server
   - Receive time from WAN

     (take the time from a network)
2. Configure the interface of the TIM via which time frames will be forwarded in the parameter group "WAN settings" as network node type "Master station".
3. In the parameter group "Send time" for the interface from step 2, enable the option "Forward time to WAN".

   Via the connected network, the time frames are forwarded in the network.
4. If necessary, enable the "To local station" option in the "Send time" parameter group if the assigned CPU should also be synchronized.

   **When using TD7onCPU, observe the following:**
     
   Enable forwarding of the time on the interface of the TIM that is networked with the CPU.

**Time clients**

1. Configure the interfaces of the other TIM modules that will be time slaves in the parameter group "WAN settings" as network node type "Node station" or "Station".

   The function is supported for the Ethernet interface and the serial interface.
2. Network the interfaces of the TIM modules involved with each other and with the interface of the time server.
3. For the stations, set the parameters of time-of-day synchronization in the parameter group "Receive time".
4. If necessary, enable the "To local station" option in the "Send time" parameter group if the assigned CPU should also be synchronized.

   **When using TD7onCPU, observe the following:**
     
   Enable forwarding of the time on the interface of the TIM that is networked with the CPU.

##### Configuring the synchronization via classic WAN networks

**TIM modules (time server and clients)**

1. In the "Receive time" parameter group, configure the TIM that will be the time server and configure the time source using one of the following options:

   - From NTP server
   - Receive time from WAN

     (take the time from a network)
2. Configure the interface of the master TIM as network node type "Master station".
3. Configure the interfaces of the other TIM modules (time clients) as network node type "Node station" or "Station".
4. If necessary, enable the "To local station" option in the "Send time" parameter group of the stations if the assigned CPU should also be synchronized.

   **When using TD7onCPU, observe the following:**
     
   Enable forwarding of the time on the interface of the TIM that is networked with the CPU.

**WAN**

1. In the parameter group "Time-of-day synchronization" of the network, enable the option "Activate time synchronization for WAN".
2. There, you configure the required synchronization cycle.
3. Network the interfaces of all TIM modules involved with the WAN.

   The settings configured for the WAN network are adopted in the following parameter groups of the connected TIM modules:

   - For the time server (master station): "Send time" parameter group
   - For the time clients (node stations / station): "Receive time" parameter group

#### Time-of-day synchronization with NTP

##### NTP mode

In NTP mode, the module sends time-of-day queries at regular intervals to one or more NTP servers. If there are multiple configured NTP servers, the module selects the most accurate time of day from the responses of the servers. The advantage of this mode is that it allows the time to be synchronized across subnets.

NTP generally uses UTC (Universal Time Coordinated). This corresponds to GMT (Greenwich Mean Time).

For security CPs, the "NTP (secure)" method can also be used when security functions are enabled.

##### NTP server and synchronization interval

The IP address of at least one NTP server must be configured.

The address of the NTP server can also be entered as a URL, e.g. &lt;ntp.server.com&gt;.

The synchronization interval specifies the cycle of the time-of-day queries to the NTP server. Depending on the selected module, the cycle can be selected from a drop down list or configured within a range of values between 10 seconds and 1 day (86400 seconds).

##### "Accept time of day from non-synchronized NTP servers" option

If the option is supported by the selected module the following behavior applies:

- Enabled

  The module also accepts the time-of-day from non-synchronized NTP servers with stratum ≥ 15.
- Disabled

  If the module receives a time-of-day frame from a non-synchronized NTP server with stratum ≥ 15, the time of day is not set according to the frame.

### Ethernet interface

This section contains information on the following topics:

- [Reconnection delay](#reconnection-delay)
- [Device redundancy of the TIM 1531 IRC](#device-redundancy-of-the-tim-1531-irc)

#### Reconnection delay

##### Validity

The "Connection establishment delay" parameter is only relevant for the "TeleControl Basic" protocol. It can be found under the Ethernet interface in the parameter group "Transmission settings - TeleControl Basic".

##### "Connection establishment delay" parameter

> **Note**
>
> **Mobile wireless connections**
>
> If the partner cannot be reached, connection establishment via the mobile wireless network can take several minutes. This may depend on the particular network and current network load.
>
> Depending on your contract, costs may result from each connection establishment attempt.

The reconnection delay for connections in telecontrol communication is the waiting time between repeated attempts to establish the connection by the CP when the telecontrol server is not reachable or the connection has aborted. This waiting time avoids continuous connection establishment attempts at short intervals if there are connection problems.

A basic value is configured for the waiting time before the next connection establishment attempt. Starting at the basic value, the current waiting time is doubled after every 3 unsuccessful retries up to a maximum value of 900 s. Range of values for the basic value: 10 .. 300 s

Example: The basic value 20 results in the following intervals (waiting times) between the attempts to re-establish a connection.

- three times 20 s
- three times 40 s
- three times 80 s
- etc. up to max. 900 s

> **Note**
>
> **Special characteristics with CP 1242‑7 (6GK7242‑7KX30‑0XE0) together with TELECONTROL SERVER BASIC (V2)**
>
> If a second telecontrol server or a second router of the telecontrol server is configured, the CP attempts to connect to the second partner at the 4th attempt.
>
> If the second partner is also unreachable, the CP attempts to connect to the first partner again the 7th time and so on.

#### Device redundancy of the TIM 1531 IRC

##### Validity of device redundancy

The following explanations of device redundancy apply to:

- Communications module

  - TIM 1531 IRC

    Firmware version: V2.4 or higher

    As station TIM

  together with:
- CPU

  - S7-1500R
  - S7-1500H
- Telecontrol protocols

  - DNP3
  - IEC 60870-5
- Supported process control systems

  - SIMATIC PCS 7

##### Redundancy options

- **Connection redundancy**

  Redundant connections to a partner can be established with a single telecontrol communications module.

  For redundant connections, see:

  - [Telecontrol server (Telecontrol Basic protocol)](#telecontrol-server-telecontrol-basic-protocol)
  - [DNP3 and IEC connections](#dnp3-and-iec-connections)

  The following figure shows a possible configuration.

  ![Example of connection redundancy](images/172562169739_DV_resource.Stream@PNG-en-US.png)

  Example of connection redundancy
- **Device redundancy**

  Starting from the above-named version of the TIM 1531 IRC, device redundancy can be configured in a station for communication with a redundant PCS 7 PC.

  The two TIM modules are connected for data synchronization and monitoring during runtime (synchronization connection). The send buffer in both TIM modules is thus identical.

  The synchronization connection of the two TIM modules can be established over any Ethernet interface of the TIM.

  - The primary TIM is the active module in the normal state.
  - The backup TIM is the passive module in the normal state.

    It takes over the communication only if the connection of the primary TIM is disrupted.

  ![Device redundancy of TIM1531 IRC in a station](images/171950694923_DV_resource.Stream@PNG-de-DE.png)

  Device redundancy of TIM1531 IRC in a station

##### Configuring device redundancy

For the configuration, follow the steps below. Only the most important steps required for redundancy mode are listed below.

**CPU**

1. Create a station with an R-CPU or a H-CPU.
2. Configure the required parameters under "Protection &amp; Security".
3. Assign an IP address to both redundant CPUs.
4. Assign the shared system IP address.

   The redundant TIM modules access the CPU at the system IP address.

   The system IP address must be in the same subnet as the IP addresses of the interfaces of the two CPUs.

**TIM 1531 IRC**

1. Create two TIM 1531 IRC.
2. Connect both TIMs using one interface each to a free interface of the respective R/H-CPU.

   The "Network type" (parameter group "WAN settings") of the interfaces of the two TIMs that are connected with the CPU is "Neutral".

   The TIMs communicate with the CPUs via their system IP address.
3. Connect the two TIM modules to each other using one Ethernet interface each (synchronization connection).
4. Select one of the two TIMs as primary TIM (the TIM active in normal operation).

   To do this, set the "Network type" ("WAN settings" parameter group) of the interface of the synchronization connection to "Primary TIM".
5. If necessary, change the device redundancy port (default setting 5000).

   The Device redundancy ID is assigned automatically by default and displayed for both TIMs of the redundancy group.

   Alternatively, you can configure the Device redundancy ID manually. In this case, however, the consistency is not checked by STEP 7.
6. Configure the other TIM in the redundancy group as backup TIM (the TIM that is passive in normal operation).

   To do this, set the "Network type" ("WAN settings" parameter group) of the interface of the synchronization connection to "Backup TIM".

   Under the number of the device redundancy port, the value that you configured for Primary TIM is shown for the Backup TIM.
7. For the backup TIM, select the primary TIM from the "Primary TIM" drop-down list in the "Device redundancy" parameter group.
8. Configure "WAN type" and "Network type" of the two other Ethernet interfaces of the TIM as follows:

   Interface to the CPU: "IP-based" / "Neutral"

   Interface to the Ethernet CP in the PCS 7 PC or the master:

   - DNP3: "IP-based" / "DNP3", Network node type "Station"
   - IEC: "IP-based" / "IEC 60870-5", Network node type "Station"
9. Assign the primary TIM to your local CPU to which it is connected (parameter group "Subscriber numbers").

   If the redundancy group was created beforehand, the backup TIM is then automatically assigned to the first CPU.

![Configuration in STEP 7](images/171950690955_DV_resource.Stream@PNG-de-DE.png)

Configuration in STEP 7

Then configure the telecontrol connections, the remaining parameters, tags and data points, etc.

##### Points to note when configuring the TIM with device redundancy

The primary TIM is configured in the usual way.

**Identical parameters with primary TIM and backup TIM**

The following data is identical for both TIMs of the redundancy group. When configured on one TIM, this data is taken over by the other redundant TIM:

- Address on the application layer

  - DNP3

    The station address of the redundancy group is identical.
  - IEC 60870-5

    The ASDU address of the redundancy group is identical.

**Takeover of primary TIM data by the backup TIM**

You cannot configure the following functions and parameters for the backup TIM. They are taken over from the configuration data of the primary TIM:

- Basic settings (except IP routing)
- Communication with the CPU (cycle idle time, write/read jobs)
- Subscriber numbers &gt; Assigned CPU
- Log settings
- SNMP
- Protection
- Data point configuration
- Configuration of the messages in the data point editor

**Manual configuration in both TIMs of the redundancy group**

The following data must be configured identically for both TIMs of the redundancy group:

- Communication type
- Basic settings &gt; IP routing
- Settings of interfaces, especially DHCP, IPv6 parameters (except address), routing, etc.
- Web server
- DNS configuration
- Communication with the CPU (other parameters)
- Time-of-day synchronization
- E-mail configuration
- Assigned CPU

  You need to assign the CPU in both redundant TIMs. For the backup TIM, select the CPU of the primary TIM.

##### Telecontrol connections

You configure telecontrol connections between the redundant TIMs and the PCS 7 computer or master under the following protocols:

- DNP3
- IEC 60870-5

![Example of telecontrol connections for the DNP3 protocol](images/171993526027_DV_resource.Stream@PNG-en-US.png)

Example of telecontrol connections for the DNP3 protocol

##### Compiling and loading

> **Note**
>
> **Compiling and loading the redundant TIMs**
>
> Always compile the primary TIM first and then the backup TIM.
>
> Always load the primary TIM first and then the backup TIM.

##### Switchover in redundancy mode

In normal operation, only the primary TIM sends data to the master. The backup TIM holds the frames in its send buffer without sending them. After acknowledgment by the master, the backup TIM also deletes the corresponding frames from the send buffer.

A switchover of send activity from the primary TIM to the backup TIM is only performed in the following cases:

- The connection of the primary TIM to the master fails.

  The backup TIM now becomes the active TIM.
- Only with IEC:

  The master switches over.

> **Note**
>
> **Switchover only in the case of a single error**
>
> The switchover between the primary TIM and backup TIM takes place only when a single error occurs.
>
> When multiple errors occur simultaneously, data may be lost.

As soon as the configured active connection of the primary TIM returns after a failure, a switch back to the normal state takes place.

**Failure of the synchronization connection**

If the synchronization connection fails, both TIMs become active.

If the synchronization connection between the two TIMs fails, this can be indicated by sending an event to the master (data point &gt; "Trigger" tab &gt; Station state event type "Status of redundancy synchronization connection changed").

### Serial interface

This section contains information on the following topics:

- [Activation of the serial interface interface of the CP 1243-8 IRC (V3) for the ST7 protocol](#activation-of-the-serial-interface-interface-of-the-cp-1243-8-irc-v3-for-the-st7-protocol)
- [Parameters of WAN networks (dedicated line / dial-up network)](#parameters-of-wan-networks-dedicated-line-dial-up-network)

#### Activation of the serial interface interface of the CP 1243-8 IRC (V3) for the ST7 protocol

##### Serial interface of the CP 1243‑8 IRC

When you insert the CP from the catalog in the project, the serial interface of the CP is not visible in the network view of STEP 7.

When using the types of communication "DNP3" and "IEC" the serial interface cannot be used.

After activating thde type of communication "ST7", the serial interface is visible but cannot be configured. To use the serial interface of the CP, a TS module is required.

Follow the steps below to insert the TS module and to activate the serial interface for ST7 communication.

1. From the network view, open the device view of the CP (double-click on the module).

   The device view opens.

   At the same time the catalog view changes. Among other things the Communications modules" directory appears.
2. Expand the "Communications modules" directory:

   &gt; Industrial Remote Communication &gt; TS Modules
3. Expand the subdirectory of the required TS module.
4. Select the TS module.

   A vertical blue line appears on the symbol of the CP.
5. Now drag the TS module onto the blue line of the CP in the device view.
6. The TS moduell with the serial interface is inserted in the station.

   At the same time a new WAN interface is inserted in the network view.

You can configure the serial interface directly in the device view with the TS adapter or in the WAN interface of the CP in the network view.

#### Parameters of WAN networks (dedicated line / dial-up network)

##### Interface operating mode

The operating mode of the serial interface specifies the mode of the data transfer.

A maximum of one serial interface of a communications module may be operated in DMA mode.

Range of values:

- Interrupt (block)

  This operating mode applies to the transmit and receive mode. The default mode Interrupt (block) is suitable for all connections. 4 characters are transferred per block. Following this, there is an interrupt. The received characters are checked only after a complete data frame has arrived.
- DMA

  This operating mode applies to the transmit and receive mode. The DMA mode should be used for connections with a high baud rate or a lot of data traffic, however not for GSM networks.
- Interrupt (individual characters)

  This operating mode is used only in the receive direction. In the transmit direction, the block mode continues to the used. The interrupt mode is suitable for extremely bad lines. An interrupt is triggered per transmitted character and each character is analyzed immediately after it is received allowing extremely good diagnostics of transmission errors. This mode is more reliable than the block mode but is slower.

##### Transmission criterion

Only for interfaces with the Connection mode "Station" / "Node station".

The transmission criterion controls connection establishment for the transmission of conditional spontaneous data frames. This reduces the number of connection retries.

Range of values:

- Standard conditions

  No connection will be established due to the existence of conditional spontaneous data frames.

  Only in the following cases will a connection be established to send conditional spontaneous data frames.

  - Threatened overflow of the send buffer
  - Connection establishment by the communications partner
- Degree of filling

  The module only establishes a connection when the configured fill level of the send buffer for conditional spontaneous data frames is exceeded.

  In the input box, enter the fill level (%) of the send buffer at which when exceeded the module establishes a connection.
- Time

  The module sends conditional spontaneous data frames at a time of day, configurable with "Hours" / "Minutes".
- Time scheme

  The module sends conditional spontaneous data frames cyclically at an interval, configurable with "Hours" / "Minutes".

##### Polling monitoring time

Only for WAN networks of the type dedicated line

The communications module monitors the frame traffic via a WAN. If the module is not called after a certain time has elapsed, it signals its CPU that the master station is disrupted. The sequence is as follows:

- Polling monitoring time configured

  After the configured time elapses, the module sends a message to its local CPU.
- Polling monitoring time not configured

  If no monitoring time is configured, the module outputs a disruption message after the following internally calculated times.

  - At a transmission speed of 9,600 bps: After 4 seconds without message traffic
  - At a transmission speed of 1,200 bps: After 32 seconds without message traffic

### Web server

#### The Web server of the module

The communications module makes the HTML pages of its Web server available for access by a PC with Web browser. The HTML pages of the WBM (Web Based Management) provide configuration and diagnostic information of the module.

#### General

- **Enable Web server on this module**

  If the option is activated, data processing is activated in the Web server of the module making access with HTTP/HTTPS possible.

  For modules with multiple interfaces you must also specify the interfaces for access (see below).
- **Allow access only using HTTPS**

  Allows access to the Web server only with the secure protocol HTTPS.

  If the option is enabled only a secure HTTPS connection can be established via the open port 443 of the communications module.

  If the option is disabled, an HTTP connection is established via port 80 of the communications module.

#### Automatic update

- **Enable automatic update**

  Enables automatic updating of the displayed values.

  If the option is disabled, only the values at the time of connecting to the Web server are displayed.
- **Update interval**

  Select the interval at which you require an update of the displayed values.

  Default setting: 30. Permitted range: 5...999

#### Overview of the interfaces

Here by selecting the check boxes you specify the interfaces for which access to the WBM of the module is allowed.

The settings for activating the interfaces for Web server access are exchanged between the two parameter groups "Web server" and "Ethernet interface &gt; Access to the Web server".

If no interface is enabled for access, it is not possible to access the WBM of the module.

### Partner stations

This section contains information on the following topics:

- [Import partner configuration (ST7 protocol)](#import-partner-configuration-st7-protocol)
- [Telecontrol server (Telecontrol Basic protocol)](#telecontrol-server-telecontrol-basic-protocol)

#### Import partner configuration (ST7 protocol)

##### Partner stations

The parameters described below are only available for ST7 modules in which the configuration method "Import" was selected in the "Basic settings" parameter group, see section [Configuration](#configuration-1).

The import options are only available for communications modules that were previously configured as proxy in STEP 7 V5.

For the supported modules, see section [Expansion of SINAUT projects](#expansion-of-sinaut-projects).

##### Import of the proxy configuration data

**Requirements**

Prior to the import, a TIM 1531 IRC must be networked with its CPU and assigned to it ("Subscriber numbers" parameter group).

**Parameters**

- Import partner configuration

  With this button you import the configuration file (SDBs) from the STEP 7 V5 project.

  The configuration file must be located in the file system of the engineering station.
- Reset partner configuration

  With this button, you delete all the configuration data of the module that you previously imported from a text file with the "Import partner configuration" button. With this you reset the partner configuration data to the status of an unconfigured module.

  Exception:  
  If the module configured in STEP 7 used the TD7 variant "TD7onCPU", the created TD7 program blocks are retained after the reset.
- Imported configuration file

  Shows the name of the text file with the configuration data you last loaded.
- Last import

  Shows the time at which you imported the configuration file.

Please note:

- If you import a second time, the data of the first import will be overwritten.

  If you import a second time, always check the configuration, the connections and data points of the module.
- If you change from "Import" to "Configure" following an import, all imported ST7 connections including the corresponding time data will be deleted. Configured data points lose their partners.

##### Imported configuration data

**Imported data**

When importing the configuration data of a proxy module from STEP 7 V5 into the compatible module in STEP 7 Professional, the ST7-specific subscriber data and the SINAUT connections are imported.

The import file generated in STEP 7 V5 contains the data of the following SDBs:

- SDB 3202: WAN data

  Data of a serial interface cannot be adopted in a CP 1542SP‑1 IRC, see also section [Expansion of SINAUT projects](#expansion-of-sinaut-projects).
- SDB 3203: Subscriber data
- SDB 3207: S7 connection data
- SDB 3208: Ethernet data

**Data point information / SINAUT objects**

The transfer of STEP 7 V5 configuration data differs depending on the TD7 version used in STEP 7 V5:

- TD7onTIM

  No configuration data is converted to data points.
- TD7onCPU

  When importing to a TIM 1531 IRC from the information about the blocks assigned in STEP 7 V5 the TD7onCPU blocks of the CPU 1500 are created.

  If you revoke the import ("Reset partner configuration", see above) the TD7onCPU blocks are retained.

**Data of time-of-day synchronization**

Data of time-of-day synchronization is adopted from STEP 7 V5.

With the following modules, the time-of-day data of a serial interface can then be changed in STEP 7 Professional.

- CP 1243‑8 IRC as of firmware version V3
- TIM 1531 IRC

##### Partner stations

After the import, the table shows the following data of all communications partners of the module configured in STEP 7 V5:

- Subscriber number

  Subscriber number of the partner
- Subscriber ID

  Identifier for the subscriber type:

  - 0 = CPU
  - 1 = TIM
  - 4 = WinCC
  - 7 = SMSC
- Subscriber additional identifier

  You can find detailed information in the section of the same name below.
- Number of connections

  Number of connections to the respective partner
- Number of partners

  Number of communications partners configured for the respective partner.

In the following tables, you can view additional data on each of the partners listed in the "Partner stations" table.

##### List of partners and connections

- **Select partner**

  In the drop-down list, select one of the partners listed in the "Partner stations" table.

**"**
**Connections**
**" table**

The table displays the following information for the partner selected in the drop-down list:

- **Partner subscriber number**

  Subscriber numbers of all communications partners configured for this partner.
- **Interface ID**

  Type identifier of the interface used for connection to the respective partner:

  - 0 = Backplane bus (connection partner = CPU)
  - 1 = Ethernet interface 1
  - 2 = Ethernet interface 2
  - 3 = Ethernet interface 3
  - 4 = Serial interface
- **Length of subnet ID**

  Length of the S7 subnet ID: 6 bytes
- **Subnet ID**

  Subnet ID (hexadecimal) of the network used for the connection to the partner:

  - Byte 0..2: Number of the subnet
  - Byte 3..5: Number of the STEP 7 V5 project

  The displayed value may be empty, depending on the imported SDB data.
- **CFB reference**

  Internally assigned index of a configured S7 connection for the transport tunnel to a local subscriber
- **Connection type**

  Connection identifier (binary)

  - 128: PBC connection (programmed block communication)
  - 136: WAN connection

  Byte assignment:

  **Bit 0..6**

  - For Ethernet interfaces:

    Bit 0..3:

     0 = S7 connection

     1 / 2 / 3 = Local connection

     5 = MSC connection

    Bit 5:

     0 = Permanent connection

     1 = Temporary connection

    Bit 6:

     1 = GPRS
  - For serial interfaces:

    Bit 0..3:

     8 = ST7 protocol

  **Bit 7**

  - 0 = Local path
  - 1 = Remote path
- **Length of the address**

  Length of address of the partner (byte)

  - IP addresses: 4
  - WAN addresses: 1
- **Address**

  - For connections via Ethernet interfaces:

    IP address of the partner
  - For connections via serial interfaces:

    WAN address of the partner (0...255)

**"**
**Partner list**
**" table**

Additional data on the partner selected in the "Select partner" drop-down list is displayed in the table.

- **Partner subscriber number**

  Own subscriber number of the partner selected above (partner of the communications module)
- **Connection partner**

  Subscriber number of the target partner with which the selected partner communicates.

##### Subscriber additional identifier

The "Subscriber additional identifier" (32 bits) is displayed in the "Partner stations" table. Depending on the subscriber type of the partner, the subscriber additional identifier contains the following information:

- **CPU**
   **(TD7)**

  Status of bit 0:

  - 0: CPU does not send operating status to partner.
  - 1: CPU sends operating status to partner.

  The remaining bits are not used for the CPU.
- **TIM (ST7)**

  | Bit no. | Meaning |
  | --- | --- |
  | Bit 0 | DCF77 clock - 0: Not available - 1: Available |
  | Bit 1 | Connection establishment from communication module to CPU - 0: Not permitted - 1: Permitted |
  | Bit 2 | Serial interface 1 (WAN driver) - 0: Interface not available - 1: Interface available |
  | Bit 3 | Serial interface 2 (WAN driver) - 0: Interface not available - 1: Interface available |
  | Bit 4...15 | Not used |
  | Bit 16...19 | Serial interface 1: Network type - 0: Dedicated line - 1: Spontaneous network (mobile network) - 2: Dial-up network - 3...4: Not used - 5: MSC network - 6...15: Not used |
  | Bit 20...21 | Serial interface 1: Network node type - 0: Master station - 1: Node station - 2: Station |
  | Bit 22 | Serial interface 1: Frame format - 0: FT1.2 - 1: FT2 |
  | Bit 23 | Not used |
  | Bit 24...27 | Serial interface 2: Network type - 0: Dedicated line - 1: Spontaneous network (mobile network) - 2: Dial-up network - 3...4: Not used - 5: MSC network - 6...15: Not used |
  | Bit 28...29 | Serial interface 2: Network node type - 0: Master station - 1: Node station - 2: Station |
  | Bit 30 | Serial interface 2: Frame format - 0: FT1.2 - 1: FT2 |
  | Bit 31 | Not used |

#### Telecontrol server (Telecontrol Basic protocol)

##### Addressing of the duplicate or redundant telecontrol server

- **TCSB V3: Addressing the TCSB redundancy combination**

  For CPs as of firmware version V2 with the "Telecontrol Basic" protocol

  In the LAN in the master to which the TCSB server PCs and the DSL router (e.g. SCALANCE M) are connected, the Network Load Balancing (NLB) of the computer operating system will assign a common virtual IP address to the two server PCs.

  This IP address is configured depending on the network setup:

  - If CPs without a DSL router are connected, the virtual address assigned by the NLB must be configured in the CPs as the IP address of the telecontrol server.
  - If a DSL router is used, only one IP address will be configured to address the redundant telecontrol server in the stations, the public address of the DSL router.

    Set the port forwarding on the DSL router so that the public IP address (external network) is led to the virtual IP address of the TCSB server PCs (internal network). Only the public IP address is reachable from the Internet. The station does not therefore receive any information telling it which of the two computers of the redundancy group it is connected to.

  If you configure a second IP address, you need to make sure that TCSB is reachable via the IP address of a second router.
- **TCSB V2: Addressing the main and substitute telecontrol server**

  Only for CP 1242‑7 (6GK7 242-7KX30-0XE0)

  With TCSB V2, two independent server PCs can be installed. The address of the substitute telecontrol server also needs to be configured only when these are connected to the Internet via two routers.

### Communication with the CPU

This section contains information on the following topics:

- [CPU scan cycle](#cpu-scan-cycle)
- [Partner status and Path status](#partner-status-and-path-status)
- [Local operator input](#local-operator-input)
- [Manual request](#manual-request)

#### CPU scan cycle

Input data points are assigned to the read cycle of the CPU in the data point configuration in the "General &gt; Read cycle" tab.

##### Parameters of the CPU sampling cycle

Here you specify parameters for the access of the communication module to the CPU within the CPU sampling cycle.

- **Cycle idle time**

  Wait time between two scan cycles of the CPU memory area
- **Max. number of write jobs**

  Maximum number of write jobs to the CPU memory area within a CPU sampling cycle
- **Max. number of read jobs**

  Maximum number of low-priority read jobs from the CPU memory area within a CPU sampling cycle

You will find the structure of the CPU sampling cycle in section [Read cycle](#read-cycle).

#### Partner status and Path status

You will find the parameters described below in the following parameter group of modules with the type of communication "ST7":

"Communication with the CPU" &gt; "Partner status"

The following statuses are monitored and written to PLC tags:

- **Partner status**

  Availability of a communication partner
- **Path status**

  Status of the connections to a communication partner

##### Partners / Partner name

This is where you define the communication partners of the selected module whose reachability status and path status of the telecontrol connections should be monitored. Partners can be CPUs or a control center application (for example, ST7cc).

All partners with which a telecontrol connection has been configured can be selected in the table.

##### Variables with the various communications modules

The variables to which the statuses are written differ depending on the module type:

- **TIM 3V‑IE, TIM 4R‑IE, TIM 3V‑IE DNP3, TIM 4R‑IE DNP3**

  - **Partner status**

    The partner status is written to a variable of the type Bool (DB, bit memory, output).

    For the coding see below.
  - **Path status**

    The path status is written to a variable of the type Byte (DB, bit memory, output).

    See below for information on variable allocation.
- **TIM 1531 IRC / CP 1243‑1 / CP 1243‑7 LTE / CP 1243‑8 IRC / CP 1542SP‑1 IRC**

  - **Partner status / path status**

    The two statuses are stored in a common variable of the type Word or UInt (DB, bit memory, output).

    The two statuses each occupy one byte of the variable. The coding is written separately for byte 0 (partner status) and byte 1 (path status).

##### Partner status

- **TIM 3V‑IE, TIM 4R‑IE, TIM 3V‑IE DNP3, TIM 4R‑IE DNP3**

  The bit for partner status is coded as follows (range of values):

  - 0: Partner not reachable
  - 1: Partner reachable
- **TIM 1531 IRC / CP 1243‑1 / CP 1243‑7 LTE / CP 1243‑8 IRC / CP 1542SP‑1 IRC**

  Byte 0 of the common variable for partner status / path status codes information on the availability of the communications partner, on the existing connections and connection paths and on the status of the send buffer of the TIM.

  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | **Path redundancy** | **Connection mode** | **Temporary connection** ****** | (Reserved) | **Frame memory**  ***** |  | **Path status** | **Partner status** |
  | 0: No redundancy  1: Redundancy exists | 0: Permanent  1: Temporary | 0: Partner not reachable  1: Partner reachable ***** | ‑ | 0: Send buffer OK  1: Memory allocation &gt; 90%  3: Overflow (memory allocation 100%) |  | 0: Not all paths reachable  1: All paths reachable | 0: Partner not reachable  1: Partner reachable |

  ***** Partners that support temporary connections are set to 'reachable' if the partner itself terminates the connection.

  ****** For the behavior of the frame memory, refer to the section "Send buffer" in the section [Process image, type of transmission, event classes](#process-image-type-of-transmission-event-classes).

##### Path status

Byte 1 shows the status of the connection path (configured connection) to the partner from the point of view of the local TIM.

A maximum of 2 paths (main and substitute path) to a partner can be configured, see section [Creating telecontrol connections](#creating-telecontrol-connections).

Both connection paths must start or end on a local TIM.

The PLC tag shows the following:

- The paths via which the partner can be reached.
- The path currently being used
- The TIM interface via which the main path was configured.
- The TIM interface via which the substitute path was configured.

The path of a connection is specified as a combination of the used interfaces of the TIM and the status of the path.

- **Byte assignment**

  The byte is assigned as follows:

  - Two bits for the interface of the main path
  - Two bits for the interface of the substitute path
  - Two bits for the status of the main path
  - Two bits for the status of the substitute path

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Bit 6 + 7** | **Bit 4 + 5** | **Bit 2 + 3** | **Bit 0 + 1** |
  | **Configured interface** |  | **Path status** |  |
  | No. for substitute path | No. for main path | Substitute path (2nd path) | Main path (1st path) |
- **Configured interface**

  In the following table the interfaces of the TIM modules are numbered through from 0 .. 3 and have the following meaning:

  - **"0"**

    TIM 4R‑IE: Ethernet interface 1 (X3)

    TIM 1531 IRC: Ethernet interface 1 (X1)

    CP: Ethernet interface (X1)
  - **"1"**

    TIM 4R‑IE: Ethernet interface 2 (X4)

    TIM 1531 IRC: Ethernet interface 2 (X2)

    CP: WAN interface (X2)
  - **"2"**

    TIM 4R‑IE: WAN interface 1 (X1)

    TIM 1531 IRC: Ethernet interface 3 (X3)
  - **"3"**

    TIM 4R‑IE: WAN interface 2 (X2)

    TIM 1531 IRC: WAN interface 1 (X4)

  For the CP 1243‑8 IRC, the interface numbers "2" and "3" are not relevant.

  |  |  |  |
  | --- | --- | --- |
  | **Status bit 5 / bit 7** | **Status bit 4 / bit 6** | **Meaning** |
  | 0 | 0 | Coding for interface "0" |
  | 0 | 1 | Coding for interface "1" |
  | 1 | 0 | Coding for interface "2" |
  | 1 | 1 | Coding for interface "3" |
- **Path status**

  - Main path = 1st path, coding by bits 0 and 1
  - Substitute path = 2nd path, coding by bits 2 and 3

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Status bit 1 / bit 3** | **Status bit 0 / bit 2** | **Meaning of bit 1 / bit 3** | **Meaning of bit 0 / bit 2** |
  | 0 | 0 | Path not current | Subscriber not reachable |
  | 0 | 1 | Path not current | Subscriber reachable |
  | 1 | 0 | Path current | Subscriber not reachable |
  | 1 | 1 | Path current | Subscriber reachable |

##### Example of coding options for the path status

The following table shows an example of the coding options of the path status for the TIM 1531 IRC.

The abbreviations for the interfaces have the following meaning:

- IE1 = Ethernet interface 1 (X1)
- IE2 = Ethernet interface 2 (X2)
- IE3 = Ethernet interface 3 (X3)
- WAN = serial interface (X4)

Same coding of the configured interface for the main and the substitute path means that there is no path redundancy (only 1 interface configured). The path status is output via the bits of the main path (1st path).

Coding example for the path status.

| Configured interface |  | Path status |  |
| --- | --- | --- | --- |
| **Coding for substitute path** | **Coding for main path** | **Substitute path (2nd path)** | **Main path (1st path)** |
| 0 0 | 0 0 = Coding for IE1 | Irrelevant (not redundant) | Status IE1 |
| 0 0 | 0 1 = Coding for IE2 | Status IE1 | Status IE2 |
| 0 0 | 1 0 = Coding for IE3 | Status IE1 | Status IE3 |
| 0 0 | 1 1 = Coding for WAN | Status IE1 | Status WAN |
| 0 1 | 0 0 | Status IE2 | Status IE1 |
| 0 1 | 0 1 | Irrelevant (not redundant) | Status IE2 |
| 0 1 | 1 0 | Status IE2 | Status IE3 |
| 0 1 | 1 1 | Status IE2 | Status WAN |
| 1 0 | 0 0 | Status IE3 | Status IE1 |
| 1 0 | 0 1 | Status IE3 | Status IE2 |
| 1 0 | 1 0 | Irrelevant (not redundant) | Status IE3 |
| 1 0 | 1 1 | Status IE3 | Status WAN |
| 1 1 | 0 0 | Status WAN | Status IE1 |
| 1 1 | 0 1 | Status WAN | Status IE2 |
| 1 1 | 1 0 | Status WAN | Status IE3 |
| 1 1 | 1 1 | Irrelevant (not redundant) | Status WAN |

#### Local operator input

##### Operator input monitoring

Validity: TIM 3V‑IE / TIM 3V‑IE Advanced / TIM 4R‑IE

The Operator input monitoring is used to monitor operator input (buttons etc.) to protect against incorrect input.

For monitored operator input a minimum and maximum duration is specified. The monitoring status is saved in the "PLC tag for operator input monitoring" (byte).

The PLC tag can be used for entries via the following data point types:

- Command output (Cmd01B_S)
- Setpoint output (Set01W_S)
- Parameter entries (Par12D_S)

The Operator input monitoring is recommended particularly when commands are entered via digital inputs, for example using buttons connected to them. This also applies to transferring setpoint and parameter inputs by triggering of a digital input, e.g. by means of a button.

##### Monitoring incorrect input (input time)

Using Operator input monitoring reduces the risk of incorrect input when the entries are made via digital inputs. The following times and the code bits are relevant only for operator input over digital inputs.

- Min. input time

  For these entries, a minimum input time can be specified, in other words, the button must be pressed for the minimum time. The accidental activation of a button does not then lead to an unwanted transfer. When the minimum input time has elapsed and the button can be released, the "PLC tag for operator input monitoring" shows "entry OK" in bit 0 (see below).

  A time of at least 1 second is recommended.

  If you do not require the parameter, configure 0 (zero).
- Max. input time

  Apart from the minimum duration, a maximum input time can also be set for digital inputs. This allows a button that is sticking or defective digital inputs that supply a permanent 1 signal to be detected in good time. Such errors are written as "input error" to bit 1 of the PLC tag.

  Further hardware entries are not processed as long as the "input error" bit is set.

  If you do not require the parameter, configure 0 (zero).

##### Monitoring for 1 out of n errors.

Generally for all operator input via digital inputs. bit memory or data blocks the PLC tag returns the error status "1 out of n error" in bit 2. The error status is set when more than 1 bit is set at the same time.

The error is output in the following situations:

- 1-out-of-n error with "Cmd01B_S"

  More than 1 bit was set in the input byte of the command data point type "Cmd01B_S". To increase reliability of command input, only 1 bit may ever be set with this object. If two or more bits are set at the same time, the command input is rejected.
- 1-out-of-n errors with all command, setpoint and parameter entries in the fast read cycle

  If increased reliability is required for the input of commands, setpoints and parameters, all objects with which this data is sent should be assigned to the fast read cycle. All command, setpoint and parameter objects in the fast cycle are then subjected to a 1-out-of-n check.

  At the end of the fast cycle there is a check to make sure that there is a command, setpoint or parameter entry for only one of the acquired objects. Only then is the corresponding entry processed and transferred. If there is more than one entry, the entries are rejected. A new command, setpoint or parameter is processed only when previously no entry was acquired in at least one fast cycle.

> **Note**
>
> **Resetting the command bit**
>
> If commands are entered over a memory or data byte, or a setpoint or parameter entry is enabled by a memory or data bit (trigger signal), the set command bit or trigger signal is automatically reset to zero.
>
> If, however, a 1-out-of-n error is detected, the command bits are not automatically reset. They must then be reset by the user program.

##### Assignment of the status byte of "PLC tag for operator input monitoring"

Bit assignment of the status byte

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit:** | **.7 *** | **.6 *** | **.5 *** | **.4 *** | **.3 *** | **.2** | **.1** | **.0** |
| **Status:** | ‑ | ‑ | ‑ | ‑ | ‑ | 1-out-of-n error | Input error | Input OK |
| **For value:** | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| ***** Unused bits are set to 0 |  |  |  |  |  |  |  |  |

#### Manual request

##### Function and requirements

**Validity**

In addition to the requests of the master station or master during startup, the option offers the possibility of a manually initiated request using a tag of the CPU.

The function is supported by:

- TIM 1531 IRC together with the following CPUs:

  - S7‑300
  - S7‑400
  - S7‑1500

**Functions**

Depending on the protocol used, the option supports the following request types:

- ST7

  - General request

    Request of all stations with transfer of the process image and all buffered frames.
  - Xcelerated general request

    Request of all stations with transfer of the process image only
- IEC

  - Single or group requests of communication partners (sequential single requests)
  - General Interrogation (sequential single requests)
- DNP3

  - Single request of a communication partner
  - Request of single objects of a partner
  - Class 0 Poll or Class 1/2/3 Poll (sequential single requests)

**The following applies generally:**
  
Requests can only be made on a station-specific basis. Requesting of multiple stations must be carried out sequentially.

The request is initiated by the tag "Read request". The request type and the addresses are also specified in this tag. The tag contains a user data type, which you must create beforehand.

The result of the request is written to the tag (Byte) "Read result", which can be evaluated by the CPU or the user.

**Requirements**

- The master function is enabled.
- Cyclic polling is disabled.

##### Tags

The following tags are needed for the request function:

- **Partner request**

  A special data type, which you must create as a user data type (UDT), is needed for initiating the request and specifying the request type and the addresses. Proceed as follows:

  - Navigate to the "PLC data types" entry of the assigned CPU in the project tree.
  - Click the "Add new data type" entry.
  - Create the required elements of the UDT (see next section).

    ![Structure of the UDT - in this example for the IEC protocol](images/172485478539_DV_resource.Stream@PNG-de-DE.png)

    Structure of the UDT - in this example for the IEC protocol
  - Create a data block in which you insert the previously created UDT.

    The UDT can be selected in the drop-down list of the data types under the name you assigned.

  For the tag "Partner request", reference the tag of the UDT created for it in the data block you create.
- **Request result**

  For the result of the request, create a tag of type Byte and reference it as the tag "Request result".

##### Structure and coding of the "Partner request" UDT

The structure and contents of the UDT are different for the three protocols:

**ST7**

| Data type | Parameter | Range of values and meaning |
| --- | --- | --- |
| Byte | Start flag | The TIM starts the request at a 0 → 1 change.  After execution of the request, the TIM resets the value to 0. |
| Byte | Request type | - 1: General request - 2: Xcelerated general request |
| Word | Station address | 1 ... 65535 |

**IEC**

| Data type | Parameter | Range of values and meaning |
| --- | --- | --- |
| Byte | Start flag | The TIM starts the request at a 0 → 1 change.  After execution of the request, the TIM resets the value to 0. |
| Byte | Request type | For the range of values, see below |
| Word | Station address | 0 ... 65534 |
| DWord | Object address | 1 ... 16777215  The object address remains empty (value = 0) if it is not needed. |

**DNP3**

| Data type | Parameter | Range of values and meaning |
| --- | --- | --- |
| Byte | Start flag | The TIM starts the request at a 0 → 1 change.  After execution of the request, the TIM resets the value to 0. |
| Byte | Request type | For the range of values, see below |
| Word | Station address | 0 ... 65519 |
| Byte | Group | 1, 2, 3, 4, 10, 11, 20, 21, 22, 23, 30, 31, 32, 33, 34, 40, 41, 42 |
| Byte | Variation | 0 ... 8 |
| Word | Start index | 0 ... 65535 |
| Word | Number of objects | - = 0: Request of all objects with the same Group and Variation   When 0 is set, the start index is irrelevant. - = 1: Request of the object specified by the start index. - &gt; 1: Request of the specified number of objects starting with the start index. |

**Coding of the value range of the "Request type" parameter**

Coding of the "Request type" parameter for the IEC protocol

| Request type | Value |
| --- | --- |
| Global Interrogation | 1 |
| Group 1 Interrogation | 2 |
| Group 2 Interrogation | 3 |
| Group 3 Interrogation | 4 |
| Group 4 Interrogation | 5 |
| Group 5 Interrogation | 6 |
| Group 6 Interrogation | 7 |
| Group 7 Interrogation | 8 |
| Group 8 Interrogation | 9 |
| Group 9 Interrogation | 10 |
| Group 10 Interrogation | 11 |
| Group 11 Interrogation | 12 |
| Group 12 Interrogation | 13 |
| Group 13 Interrogation | 14 |
| Group 14 Interrogation | 15 |
| Group 15 Interrogation | 16 |
| Group 16 Interrogation | 17 |
| Counter Interrogation | 18 |
| Group 1 Counter Interrogation | 19 |
| Group 2 Counter Interrogation | 20 |
| Group 3 Counter Interrogation | 21 |
| Group 4 Counter Interrogation | 22 |
| Selective request of one object ***** | 23 |

***** The single request of count values is not supported.

Coding of the "Request type" parameter for the DNP3 protocol

| Request type | Value |
| --- | --- |
| Class 0 Poll | 1 |
| Class 1 2 3 Poll | 2 |
| Class 1 Poll | 3 |
| Class 2 Poll | 4 |
| Class 3 Poll | 5 |
| Selective request of one object | 6 |

##### Coding of the "Request result" byte

The results of the request are written to the tag "Request result". The values (hexadecimal) have the following meaning:

| Value (hex) | Meaning |
| --- | --- |
| **No result:** |  |
| 0x00 | #define TCH_DATA_REQUEST_RESULT_NO_RESULT |
| **"Result OK":** |  |
| 0x01 | #define TCH_DATA_REQUEST_RESULT_OK |
| **"Partner not OK":** |  |
| 0x88 | #define TCH_DATA_REQUEST_RESULT_STATION_NOT_OK |
| **Error:** |  |
| 0x80 | #define TCH_DATA_REQUEST_RESULT_ERROR |
| 0x81 | #define TCH_DATA_REQUEST_RESULT_STATION_UNDEF |
| 0x82 | #define TCH_DATA_REQUEST_RESULT_TYPE_UNDEF |
| 0x83 | #define TCH_DATA_REQUEST_RESULT_GROUP_UNDEF |
| 0x84 | #define TCH_DATA_REQUEST_RESULT_VARIATION_UNDEF |
| 0x85 | #define TCH_DATA_REQUEST_RESULT_TIMEOUT |
| 0x86 | #define TCH_DATA_REQUEST_RESULT_ALREADY_ACTIVE |
| 0x87 | #define TCH_DATA_REQUEST_RESULT_REFUSED |
| 0x89 | #define TCH_DATA_REQUEST_RESULT_REFUSED_BY_PARTNER |
| 0x90 | #define TCH_DATA_REQUEST_RESULT_REQUEST_INCOMPLETE |

##### Control of requests

You control the requests in the user program of the CPU.

You set the start flag, which initiates a request, and the respective contents of the parameters "Request type", "Station address", "Object address", "Start index", "Group", "Variation" and "Number of objects" from the CPU.

> **Note**
>
> **Recommendation**
>
> Set the start flag after you have set all the other parameters.

For the request of various stations, groups or objects, the relevant contents in each case must be written to the UDT by the user program.

### Subscriber numbers

This section contains information on the following topics:

- [Subscriber numbers](#subscriber-numbers-1)
- [Secure communication between CPU and TIM 1531 IRC](#secure-communication-between-cpu-and-tim-1531-irc)

#### Subscriber numbers

##### Configuring the subscriber numbers

The following description applies to the specific address parameters of the modules that participate in the telecontrol communication. The name depends on the telecontrol protocol:

- TeleControl Basic: Station number
- SINAUT ST7: Subscriber number
- DNP3: Station address
- IEC 60870-5: ASDU address

You configure the address parameters listed above in the following parameter groups.

- CPs up to firmware version V2.x

  - TeleControl Basic

    Parameter group "Security &gt; CP identification"
  - SINAUT ST7

    Parameter group "Ethernet interface &gt; Station address"
  - DNP3 / IEC 60870-5

    Parameter group "Ethernet interface &gt; Station address"
- CPU with firmware version V3.0

  - TeleControl Basic

    Parameter group "Security &gt; CP identification"
  - SINAUT ST7

    Parameter group "Subscriber numbers"
  - DNP3 / IEC 60870-5

    Parameter group "Ethernet interface &gt; CP identification"
- CPs as of firmware version V3.1

  - TeleControl Basic

    Parameter group "Security &gt; CP identification"
  - SINAUT ST7

    Parameter group "Subscriber numbers"
  - DNP3 / IEC 60870-5

    Parameter group "Subscriber numbers"
- TIM modules

  - All supported protocols

    Parameter group "Subscriber numbers"

##### Uniqueness of the addresses

For each protocol, the address within a subnet and the STEP 7 project must be unique.

**Uniqueness of the ASDU address**

For modules with telecontrol connections that are configured via the "Network data" editor, a consistency check determines the uniqueness of the address.

For CPs with a firmware version ≤ V3.0 whose telecontrol connections are configured via the "Partner stations" parameter group, the address cannot be checked for uniqueness with a consistency check. You must ensure uniqueness of the address in this case.

If you want to use subscriber numbers/station addresses twice in different subnets, you must create two STEP 7 projects.

##### Assignment of the CPU and configuration of the subscriber addresses

For modules that communicate via telecontrol connections ("Network data" editor), you assign the CPU and configure the protocol-specific module addresses in the "Subscriber numbers" parameter group.

- **Assigned CPU**

  With the following communication modules, which are located in the same rack as the CPU, the local CPU is automatically assigned to the module:

  - CPs (S7‑1200, ET 200SP)
  - TIM 3V‑IE... / TIM 4R‑IE
  - TIM 3V‑IE DNP3 / TIM 4R‑IE DNP3

  For communication modules that are not in the same rack as a CPU, you must assign the module to a CPU with which it is networked via the drop-down list. This affects:

  - TIM 4R‑IE Standalone
  - TIM 4R‑IE DNP3 Standalone
  - TIM 1531 IRC

    The TIM 1531 IRC can be assigned a CPU of the following SIMATIC families: S7‑300, S7‑400, S7‑1500, ET 200SP

    When you assign the TIM 1531 IRC to an S7‑1500R/H CPU, the system IP address of the S7‑1500R/H CPU is used for communication of the TIM with the CPU.
- **Subscriber number of the assigned CPU**

  You can change the pre-assigned subscriber number of the CPU, which is the endpoint of the Telecontrol connections, for ST7 modules here.

  An S7‑1500R/H CPU (TIM 1531 IRC) receives only one subscriber number.

  Note:  
  The subscriber number is configured in the Telecontrol connection for the ST7 application of the central PC.
- **Subscriber number**
   **/** 
  **Station address**
   **/** 
  **ASDU address**

  The address configured here is used for identification of the communications module in the respective telecontrol network:

  - ST7: Subscriber number
  - DNP3: DNP3 address
  - IEC 60870‑5: Common address of the ASDU

##### Structured addressing of the IEC protocol

The ASDU address can be configured in two input fields with different formats:

- ASDU address

  The address is configured unstructured here as an integer.

  Range of values: 0..65534
- Structured ASDU address

  You can configure the address structured according to IEC 60870‑5‑3 here. Plant-based structuring of the ASDU address is enabled by structured addressing.

  Two address levels (octets) can be configured.

  Range of values: 0.0..255.254

  The configured values of the two fields are linked. A configured value is converted and displayed in the other input field.

Conversion of the values:

The values are designated as follows for the conversion:

- ASDU address

  Designation of the integer value: X
- Structured ASDU address

  Designation of the values of the 2nd octet: A.B

The configured value is applied to the other field according to the following formula:

X = A * 256 + B

##### RTU3000C

The RTU3000C, which can be configured as a placeholder using the ST7 protocol, has the following parameters.

- **Subscriber number (RTU)**

  Here, you assign the subscriber number of the RTU as it was configured in the WBM of the respective RTU.
- **Subscriber number of the CPU (RTU)**

  Here, you assign the subscriber number of the CPU as it was configured in the WBM of the respective RTU.

#### Secure communication between CPU and TIM 1531 IRC

##### Secure communication with certificates

With communications modules that are not in the same rack as the CPU, you need to specify the certificate of the CPU for the communications module in the following cases.

Required for:

- TIM 1531 IRC  
  together with
- CPU 1500 / CPU 1500 SP as of version V2.9
- Additionally for ST7:

  You use TD7onTIM

  See "Basic settings &gt; Configuration &gt; Telecontrol configuration &gt; Configure".

  When TD7onCPU is used, it is not necessary to specify the CPU certificate to the TIM.

##### Creating the CPU certificate and assigning the CPU

For information on requirements and the procedure, see [Telecontrol: Handling certificates for TLS](#telecontrol-handling-certificates-for-tls).

### Protection

This section contains information on the following topics:

- [Protection of the TIM 1531 IRC](#protection-of-the-tim-1531-irc)
- [Configuring access protection](#configuring-access-protection)

#### Protection of the TIM 1531 IRC

##### Protection

Using the "Protection" table you can configure various access levels to restrict access to the configuration data of the module.

The green check mark in the "Access" column indicates which operations are released without knowing the password of this access level.

If you want to use operations that are not released, you will need to enter the configured password.

Exception  
Even without entering a password, each access level allows access to the identification data (name, addresses ...) of the module using the "Accessible devices" function.

##### Default reaction

The default access level is "Full access (no protection)". Every user can read and modify the configuration data of the TIM. No password has been configured and no password is required for online access.

##### The individual access levels

You can configure the following access levels:

- Full access (no protection)

  The hardware configuration and the blocks can be read and modified by anybody.
- Read access

  Without entering the password, only read access is possible.

  Without entering the password, you cannot load any data (configuration, firmware, certificates) on the module and not perform any writing test functions.
- No access (complete protection)

  Neither read nor write access to the module is possible.

With the legitimization provided by using the password, you once again have full access to the module.

##### Behavior of a password-protected module during operation

Protection of the module is effective after the settings have been loaded on the module.

The functions protected by the password can only be executed by the engineering station (STEP 7 PC).

Before an online function is executed, a check is made to establish whether or not it is permitted. If there is password protection, you will be prompted to enter the password.

Example:  
The module was configured for read access and you want to load new firmware. Since this is write access, the configured password must be entered before the function can be executed.

The access rights to the protected data apply for the duration of the online connection or until the access rights are canceled again manually with "Online &gt; Delete access rights".

---

**See also**

[Configuring access protection](#configuring-access-protection)

#### Configuring access protection

For the module you can enter several passwords and therefore set up different access rights for different user groups.

The passwords are entered in the table so that precisely one access level is assigned to each password. How the password takes effect is shown in the "Access level" column.

**Example (No access):**

You select the access level "No access (complete protection)" for the module and enter a separate password for each of the access levels higher up the table.

For users that do not know any of the passwords, the module is completely protected.

For users who know one of the passwords the effect depends on the table row in which the password is located:

- The effect of the password in the row "Full access (no protection)" is that the module is unprotected for users that know this password. They have unrestricted access to the module.
- The password in the row "Read access" brings about write protection for the module. Users that know this password only have read access to the module.

**Procedure**

Follow the steps below to configure the access levels in the "Protection" table:

1. Select the required access level in the first column of the table. The green check mark in the columns on the right of the particular access level indicate which operations are still possible without entering the password.
2. If you have selected an access level other than "Full access":

   - Assign a password for full access in the "Password" cell in the first row (Full access).
   - Repeat the selected password to protect against incorrect entries.

   Make sure that the password is adequately secure; in other words, that it does not include a pattern that can be machine read!

   The entry of the password in the row "Full access (no protection)" is obligatory and allows a user who knows the password unrestricted access to the module regardless of the selected protection level.
3. As necessary, assign other passwords to the required access levels if the selected access level permits this.
4. Download the configuration data to the module so that the access level takes effect.

**Result**

The configuration data is protected from unauthorized online access according to the set access levels. If an operation cannot be executed without a password due to the configured access level, a dialog appears prompting entry of the password.

### Telecontrol connections

This section contains information on the following topics:

- [Telecontrol connections](#telecontrol-connections-1)
- [Creating telecontrol connections](#creating-telecontrol-connections)
- [ST7 connections](#st7-connections)
- [DNP3 and IEC connections](#dnp3-and-iec-connections)

#### Telecontrol connections

##### Telecontrol connections

Telecontrol relationships between the communication modules involved are required for telecontrol communication. Depending on the module type and the firmware version, you perform the configuration in the following parameter groups:

- "Partner stations" parameter group

  or
- "Network data" editor

##### Configuration in the "Partner stations" parameter group

For S7-1200 telecontrol CPs up to V2.1, which only function as stations, the relationships to the master station or to the master are configured in the "Partner stations" parameter group. This is where you define the communication partners of the CPs.

All other settings required for communication with the master station are taken from the other configuration data of the CPs and do not have to be specially configured for the connections.

> **Note**
>
> **Exception: CP 1243‑8 IRC V2.1 (ST7)**
>
> As of STEP 7 V15.1, you can configure a physical CP with firmware V2.1 in the STEP 7 project with firmware version V3.0:
>
> 1. Insert a CP with firmware version V3.0 into the STEP 7 project.
> 2. Select the "Compatibility mode V2.1" option in the "General &gt; Catalog Information" parameter group of the CP.
>
> You can then use the CP in telecontrol connections that you configure using the "Network data" editor.
>
> You can load the V3.0 configuration data into CP V2.1.
>
> The following functions are not supported when this option is selected:
>
> - Switching the protocol type
> - Receive time from local station and via NTP
> - "Communication with the CPU &gt; CP diagnostics"
> - Online &amp; Diagnostics &gt; "Functions &gt; Save service data"

##### Configuration in the "Network data" editor

For all other telecontrol modules that do not fall into the above group, you need to configure telecontrol connections in the "Network data" editor.

The "Network data" editor is used for the following protocols and modules:

- ST7

  Modules without imported configuration data:

  - CP 1243‑8 IRC as of firmware V3.0
  - CP 1542SP‑1 IRC as of firmware V2.0
  - TIM 1531 IRC as of firmware V1.0
  - TIM 3V-IE / TIM 4R-IE as of firmware version V2.7
- DNP3

  - CP 1243‑1 / CP 1243‑8 IRC as of firmware V3.0
  - CP 1542SP‑1 IRC as of firmware V2.0
  - TIM 1531 IRC as of firmware V2.0
  - TIM 3V-IE DNP3 / TIM 4R-IE DNP3 as of firmware V3.2
- IEC 60870-5

  - CP 1243‑1 / CP 1243‑8 IRC as of firmware V3.0
  - CP 1542SP‑1 IRC as of firmware V2.0
  - TIM 1531 IRC as of firmware V2.0

#### Creating telecontrol connections

##### Requirements for creating connections

Check the following requirements before you create Telecontrol connections:

- Networking

  The connection partners involved must be networked.
- Assignment of the CPU

  A CPU must be assigned to the communication module.

  For information on the configuration, refer to the section [Subscriber numbers](#subscriber-numbers-1).
- Network type of the interfaces

  - Interfaces for connections between communication module and associated CPU

    The interfaces have the "Neutral" network type.
  - Interfaces for connections between two communication modules

    Set the network type to the respective communication protocol: ST7 / DNP3 / IEC 60870‑5
- TIM 1531 IRC with S7‑1500R/H CPU

  When you assign the TIM 1531 IRC to an S7‑1500R/H CPU, the system IP address of the S7‑1500R/H CPU is used for communication of the TIM with the CPU. An S7 connection is automatically created after applying a telecontrol connection. You can recognize the use of the system IP address in the "Network data" editor &gt; "Connections" tab in the property dialog of the S7 connection: Here you activate the option to use the system IP address in the default setting.

  Make sure that the system IP address is configured for both CPUs and that the subnet masks of the interfaces are identical.

##### Opening the editor "Network data" &gt; "Telecontrol" tab

To open the editor, follow the steps below:

1. Open the network view of the project.

   On the right you will find the collapsed "Network data" editor.

   ![Opening the editor "Network data" > "Telecontrol" tab](images/98326941963_DV_resource.Stream@PNG-en-US.png)
2. Open the "Network data" editor using the arrow symbol.

   The editor is displayed with several tabs, on the left the "Network overview" tab.
3. Expand the editor until the "TeleControl" tab appears.

   This tab is further divided into the following tabs:

   - ST7
   - DNP3
   - IEC

   Depending on the protocol used, select the corresponding tab to configure the telecontrol connections.

##### Display and show/hide columns

In the "Telecontrol connections" table, you can display or hide the columns, arrange them and optimize the column width. Right-click on a column header to access the shortcut menu.

- Arrange columns

  If you click on a column header and hold down the left mouse button, you can move the column within the table.
- Show/Hide

  You can show or hide individual columns using this function in the shortcut menu.

  This increases the legibility of the table.
- Show all columns

  Shows all columns of the table.
- Optimize width / Optimize width of all columns

  You use these shortcut menus to optimize the width of the selected column or all columns in the table.

  The column width adapts to the widest entry in this column.

##### Creating telecontrol connections

To create a telecontrol connection, follow these steps:

1. In the "Telecontrol connections" table, double-click in a field in the first free row.

   A new empty connection is created. The connection name is preset.
2. Select the starting point of the connection from the drop-down list in the "Starting point" field.

   The drop-down list of the field shows the possible starting points.
3. To change the connection name, click in the "Name" field.

   See also the following section.
4. In the other fields, configure the required parameters, such as interfaces and endpoint of the connection.

Some fields of the table can be edited, in others you configure the parameter via a drop-down list.

Boxes with a missing or bad configuration are shown on a red background, in the example the representation "TC_Connection_3".

!["Network data" editor, "Telecontrol > ST7" tab, example of ST7 connections](images/114989519499_DV_resource.Stream@PNG-en-US.png)

"Network data" editor, "Telecontrol &gt; ST7" tab, example of ST7 connections

The connections are displayed somewhat differently in the "DNP3" and "IEC" tabs, see protocol-specific sections under [DNP3 and IEC connections](#dnp3-and-iec-connections).

##### Names of the connections

You can adapt the default names of the connections.

A maximum of 129 characters from the following ASCII character sets (numbers decimal) are permitted:

- **No.**
   **32..126**

  Space , ! " # $ % &amp; ' ( ) * + , - . / : ; &lt; = &gt; ? @ [ \ ] ^ _ ` { | } ~
- **No.**
   **128, 130..140, 142, 145..156, 158..159, 161..172**

  € ‚ ƒ „ … † ‡ ˆ ‰ Š ‹ Œ Ž ‘ ’ “ ” • – — ˜ ™ š › œ ž Ÿ ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬
- **No.**
   **174..255**

  ® ¯ ° ± ² ³ ´ µ ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ

##### Specification of the connection path

Once a connection has been created, the actual course of the connection is usually not yet defined. Especially with larger networks, several connection paths are often possible.

Specify the actual connection path of the created Telecontrol connection using the "Add new connection path" icon. ![Specification of the connection path](images/96849757195_DV_resource.Stream@PNG-de-DE.png)

The "Add connection paths" dialog opens.

You can find more details in the following protocol-specific chapters of the telecontrol connections.

##### Symbols in the "Add connection paths" dialog

The "Connection path" table supports you in checking the configured connections. For every configured connection, the detailed connection path is shown here.

A station symbol with an identifier for the connection point is displayed in the "Position" column:

The color of the identifier indicates the validity of the connection point:

- Blue: Valid connection point
- Red: Invalid connection point

| Symbol | Meaning |
| --- | --- |
| ![Symbols in the "Add connection paths" dialog](images/111134190475_DV_resource.Stream@PNG-de-DE.png) | Starting point |
| ![Symbols in the "Add connection paths" dialog](images/111134199435_DV_resource.Stream@PNG-de-DE.png) | Node ‑ input |
| ![Symbols in the "Add connection paths" dialog](images/111134259595_DV_resource.Stream@PNG-de-DE.png) | Node ‑ output |
| ![Symbols in the "Add connection paths" dialog](images/111134294155_DV_resource.Stream@PNG-de-DE.png) | Endpoint |
| ![Symbols in the "Add connection paths" dialog](images/98217757451_DV_resource.Stream@PNG-de-DE.png) | Examples of invalid connection points |

##### Error displays

Faulty connection points, networks or parameters are highlighted in red in the tables.

Causes of faulty connections include, for example:

- Starting point and endpoint are identical.
- The connection runs through an impermissible network.
- The connection runs through an invalid subscriber.

Example of representation:

![Redundant connection with incorrectly configured connection path (Route_2)](images/114989564299_DV_resource.Stream@PNG-en-US.png)

Redundant connection with incorrectly configured connection path (Route_2)

The "Route_2" path of an ST7 connection shown in the figure was created via an invalid MSC network. The connection of the PC station to the MSC network was then deleted, so that the telecontrol connection runs over subscribers that are no longer available.

##### General rules for connection configuration

Note the following general rules for connection configuration:

- A connection must run over a single subnet.

  If a "third-party device" is located as a partner in another subnet, the gateway between the subnets is the endpoint for connection configuration.
- All sections of a telecontrol connection must be configured using the same telecontrol protocol.
- A connection via an inconsistent network is invalid.

  Examples:

  - Subscribers with incompatible network node types (e.g.: 2 masters)
  - Connections via nodes that are not configured as node stations.
  - Subscriber with incompatible modems
  - Incompatible settings of two modems in a connection
  - Incompatible settings between modem and network parameters
  - Two connections to a partner via the same interface of a module are not allowed.
  - A connection via a network in which two analog switched network modems (e.g. MD3) communicate with each other via 1200 bps / half-duplex / AT mode is not permitted.

You can find further protocol-specific rules in the following sections.

##### Delete invalid or redundant connections

If there are unauthorized or unwanted redundant connections, you must delete a connection path:

1. In the "Configured connection paths" table, select the unwanted connection path.
2. Click "Delete" in the shortcut menu.

##### "Properties" tab of the connection

If you select a connection in the "Telecontrol connections" table in the "Network data" editor, additional parameter groups for this connection are displayed in the "Properties" tab of the Inspector window. Here you can check and, if necessary, correct the connection configuration and configure additional properties.

Parameter groups:

- **General**

  Shows the basic properties of the telecontrol connection.

  You can change the connection name and the subscriber number / station address of the starting point and endpoint. This affects the configuration data of the subscriber.
- **Other protocol-specific parameters**

  You can find the description below.

#### ST7 connections

This section contains information on the following topics:

- [Telecontrol connections - ST7](#telecontrol-connections---st7)

##### Telecontrol connections - ST7

###### ST7-specific rules for connection configuration

Note the following special rules for connection configuration:

- An MSC connection can only run via the first Ethernet interface [X1] of a TIM or via the serial interface of a module with the setting "IP-based".
- Connections between a PC application and a module can only be of the Network type "Neutral" (S7 connections).
- For connections between a redundant PC application and a module, you need to create two connections.

  For a redundant ST7cc control center, in STEP 7 create two PC stations each with an ST7cc application (see below).

  Only in this way can you configure a connection from each application.

###### Create ST7 connections

For communication between two ST7 stations via classic WAN networks (dedicated line, dial-up network) you need at least one telecontrol connection.

The following configurable starting points are displayed in the "Starting point" field:

- S7 stations: Assigned CPU
- PC stations: Application (for example, ST7cc / ST7 ScadaConnect / ST7sc)

For connections between an application on the master station PC and an S7 station, always select the application as the starting point because it can only be selected in the list of starting points.

Click on the "Add new connection path" icon. ![Create ST7 connections](images/96849757195_DV_resource.Stream@PNG-de-DE.png)

Open the "Add connection paths" dialog opens, in which the possible connection paths are searched for. The connection paths found are displayed in the "Select a connection path ..." table.

For ST7 connections, the "Configured connection paths" table is located below the "Telecontrol connections" table. This contains the added connection path for each selected connection.

For redundant connections, both paths are displayed.

!["Network data" editor, "Telecontrol" tab](images/114989519499_DV_resource.Stream@PNG-en-US.png)

"Network data" editor, "Telecontrol" tab

The third table "Connection path" shows details of the selected path.

###### Specification of the connection path

Specify the actual connection path of the created telecontrol connection as follows.

1. Select a connection in the "Telecontrol connections" table.
2. Click on the "Add new connection path" icon.  
   ![Specification of the connection path](images/96849757195_DV_resource.Stream@PNG-de-DE.png)

   The "Add connection paths" dialog opens.

   The possible connection paths are searched for automatically, which is indicated by the progress bar at the bottom of the dialog. The status and result of the search are displayed in the "Information" field below.

   The connection paths found are displayed in the "Select a connection path ..." table.
3. Select one of the possible connection paths.

   Details about the selected connection path are shown in the "Connection path" table.

   The "Preview" table contains additional details about all connection points involved in the selected connection path.

   - If several connections are displayed in the "Select a connection path ..." table, you can choose one or two redundant connections for selecting the connection path to be used.
   - If no connection is displayed in the table, there is a configuration error in the corresponding stations or networks.

     In this case, close the dialog with the "Close" button and complete the configuration.
4. Select a connection path and click "Add" to add this path to the project as a configured connection.

   "Information" shows whether the connection has been added or whether it has already been configured.
5. If necessary, select a second connection path and click "Add" to add this path as a redundantly configured connection.
6. Close the dialog using the "Close" button if the added connection paths correspond to the project defaults.

###### Creating redundant ST7 connections

If different networks are created between two subscribers in the network configuration, the different connection paths are displayed:

&gt; dialog "Add connection paths" &gt; table "Select a connection path ..."

If you only want to use one connection path, only select the desired path and click "Add".

If you want to use two redundant connection paths for the ST7 connection, select both one after the other and click "Add" for each.

After closing the "Add connection paths" dialog, both paths for this connection are displayed in the "Configured connections" table.

The first of the two is the main path and the second the alternative path. This is displayed in the "Priority" column of the "Configured connections" table:

1. Main path
2. Substitute path

You can change the priority of the two connection paths (main/alternative path) later. The arrow keys serve this purpose: ![Creating redundant ST7 connections](images/98514049803_DV_resource.Stream@PNG-de-DE.png)

###### "Properties" tab of the connections

For the "General" parameter group, see section [Creating telecontrol connections](#creating-telecontrol-connections).

- **Redundant ST7cc/sc**

  If you use a redundant control center in your project (e.g. ST7cc or ST7sc), you must first create two PC stations and the individual connections between the module and the two applications.

  Only afterwards you create a redundancy group here for the connection to the redundancy group.

  - Add redundant ST7cc/cc partner
  - Enable the option for each of the two connections between the redundant application and the module.
  - Redundant application

    Select the required application from the "Redundant application" drop-down list.
- **Destination subscriber properties**

  The parameter group relates to the destination subscriber that was configured as the endpoint of the connection.

  - **General request supervision time**

    This is the maximum time that may be required by a destination subscriber (communications module capable of ST7) to respond fully to a general request (GR).

    If the GR response has not arrived completely at the requesting partner when the supervision time has expired, a message is entered in the diagnostics buffer of the module.

    The general request supervision time is 900 seconds.
  - **Telegrams to destination subscriber with time stamp**

    Regardless of the configuration, all telegrams are sent to the destination subscriber with a time stamp.

#### DNP3 and IEC connections

This section contains information on the following topics:

- [Communications options](#communications-options)
- [Configuring DNP3/IEC connections](#configuring-dnp3iec-connections)
- [Filter of the connection table](#filter-of-the-connection-table)
- [Connection table - DNP3](#connection-table---dnp3)
- [Connection table - IEC](#connection-table---iec)
- [Third-party device parameters](#third-party-device-parameters)
- [Request options (IEC)](#request-options-iec)
- [Redundant DNP3 master group with 3 servers](#redundant-dnp3-master-group-with-3-servers)
- [Security statistics options (IEC 60870-5-104)](#security-statistics-options-iec-60870-5-104)

##### Communications options

###### Communication paths

The following communication channels are possible:

- Connections between master and station
- Redundant connections

  If two subscribers can be reached via different paths or networks, you can create a maximum of two connections between the subscribers to establish path redundancy.

  Some modules support the configuration of a third master when using the DNP3 protocol. For information on the configuration, see [Configuring DNP3/IEC connections](#configuring-dnp3iec-connections).
- Direct communication

  You can configure simple Ethernet connections for the direct communication between two stations. The network node type of the interface is configured in the two communication modules as "Station". The telegrams do not have to be transmitted by a central unit.

  Requirements:

  - Select the "Master function" option in the data point configuration for data points that you want to use for direct communication.

    For addressing, enter the desired data point of the partner station as the partner.
  - The "Unsolicited" option is selected in the Telecontrol connection.

  Direct communication is supported between the communications modules as well as between a communications module and a "Third-party device" connection partner.

##### Configuring DNP3/IEC connections

###### Specific rules for DNP3 and IEC connections

Note the following special rules for connection configuration:

- Connections between STEP 7 devices

  You can create connections between subscribers that are configured in the STEP 7 project.

  The address and interface data of both subscribers is available in the connection table.
- Connections to external devices

  You can create connections between a subscriber that is configured in STEP 7 and a "third-party device" that is not configured in STEP 7.

  The device that is not configured in STEP 7 is displayed in the "Endpoint" field of the connection table as a "third-party device". You configure the address data of this subscriber using the real address data (IP address / telephone number).
- Connections via network transitions

  You can configure single and redundant connections to subscribers in other subnets that can be reached via a gateway. The corresponding fields in the connection table are available for this purpose.
- Connections for direct communication

  You can use simple Ethernet connections for direct communication between two stations.

  A simple or redundant connection between the master station and the station cannot be used for direct communication.

  For further details, see [Communications options](#communications-options)
- Changing endpoints

  A single endpoint must not be changed in the connections created.

  If you want to correct the endpoint of a connection, correct the endpoints of both connection segments consistently or delete the connection and create a new one.

###### Definition of the single or redundant connection path

Specify the actual connection path of the created telecontrol connection as follows.

1. Select a connection in the "Telecontrol connections" table.
2. Click on the "Add new connection path" icon.  
   ![Definition of the single or redundant connection path](images/96849757195_DV_resource.Stream@PNG-de-DE.png)

   The "Add connection paths" dialog opens.

   The possible connection paths are searched for automatically, which is indicated by the progress bar at the bottom of the dialog.

   - The status and result of the search are displayed in the "Information" field below.
   - The connection paths found are displayed in the "Select a connection path ..." upper table.
   - Details for a selected connection path are shown in the "Connection path" table.
   - When selecting a connection path, the "Preview" table shows which connection points of the selected connection path are transferred to the connection editor when you click "Add".
3. Select the desired connection path(s).

   - If one or more connection paths are displayed in the upper table, select the desired connection path and click on "Add".

     "Information" shows whether the connection path has been added or whether it has already been configured.

     If you want to use a redundant connection, select a second path and click on "Add".

     Close the dialog using the "Close" button if the added connection paths correspond to the project defaults.
   - If no connection is displayed in the table, there is a configuration error in the corresponding stations or networks.

     In this case, close the dialog with the "Close" button and complete the configuration.

###### Interface-specific configuration of the connection segments

![Connection table (DNP3 / IEC): "Network data" editor, "Telecontrol" tab](images/114992285707_DV_resource.Stream@PNG-en-US.png)

Connection table (DNP3 / IEC): "Network data" editor, "Telecontrol" tab

**A connection segment with two lines**

The connection segments between the interfaces of two subscribers are displayed in separate lines. Example of a connection between module 1 and module 2:

- Segment 1

  Module 1 ⇒ Module 2
- Segment 2

  Module 2 ⇒ Module 1

You can configure individual settings for the two connection segments.

**A segment for several connections**

DNP3 and IEC connections can run over multiple subscribers. A connection segment between two subscribers can be used for multiple connections.

A connection segment between two subscribers used for multiple connections only appears once in the connection table.

**Node stations**

In the figure above, the "15_3_node" station is a node station, that is located between the master station (15_4) and the station (15_6) in the plant hierarchy. The special features of node stations are described in the "Partner list" parameter in the respective connection table, see below.

**Filter**

The "15_" filter is set in the "Starting point" column in the figure. Only connections whose starting point begins with "15_" are displayed. For the meaning of the filters, see [Filter of the connection table](#filter-of-the-connection-table).

###### DNP3 connections with three masters

A maximum of 2 connections can be set up simultaneously to masters by a DNP3 station module during runtime.

In case of a connection to a redundant control center, some modules that are configured as Outstation can set up a connection to a third master if one of the first two masters of the redundancy group fails.

For information on engineering this specific configuration, see [Redundant DNP3 master group with 3 servers](#redundant-dnp3-master-group-with-3-servers).

###### Parameters of the DNP3 connections

You can find the description of the parameters in the section [Connection table - DNP3](#connection-table---dnp3).

###### Parameters of IEC connections

You can find the description of the parameters in the section [Connection table - IEC](#connection-table---iec).

###### "Properties" tab of the connection

- **General**

  See [Creating telecontrol connections](#creating-telecontrol-connections).
- **TCP connection monitoring**

  You can find information in the tooltips of the parameters.
- **DNP3 security options**

  See [DNP3 security options](#dnp3-security-options).
- **Transmission settings DNP3**

  See [Connection table - DNP3](#connection-table---dnp3).
- **Options 1st Path**
   **/** 
  **Options 2nd Path**

  See [Request options (IEC)](#request-options-iec).
- **Third-party device parameters**

  See [Third-party device parameters](#third-party-device-parameters).

##### Filter of the connection table

###### Filter

![Connection table (here: IEC)](images/114992285707_DV_resource.Stream@PNG-en-US.png)

Connection table (here: IEC)

The first line below the table header serves as a filter in the tables for DNP3 and IEC connections.

You can use the filter function to restrict the selection of configurable subscribers and connection options. Using filters reduces the number of combination possibilities and increases the clarity.

If you have created some connection segments, enable the filter by typing a repeating string (part of the name) into the filter cell.

The cell of the filter is highlighted in color. Only connection segments containing this string in the corresponding column are now displayed in the table.

Filters are applicable to the following columns:

- Connection name
- Starting point / Start subscriber
- Endpoint / End subscriber

The "*****" selection in the filter cell removes the filter. All existing connection segments are displayed again.

**Multiple filters**

- Multiple filters in one column

  You can apply multiple filters to a column (for example, "15_" and "12_"). Then only connection segments containing the strings "15_" and "12_" in the name are displayed.

  Several filters are separated in the filter cell by entering a semicolon. Input example: 12_;15_
- Filter in multiple columns

  You can set filters in multiple columns simultaneously.

  Filters in multiple columns multiply.

###### Example

In a connection table, connections are created with the starting points, which contain the strings "12_...", "PLC_..." and "15_...".

"15_" is entered in the filter cell of the starting point, see figure above.

In the table, the only connection segments displayed are those whose starting points contain this partial string: "15_3...", "15_4...", "15_6" etc.

##### Connection table - DNP3

In the connection table, you configure the parameters of the individual connection segments.

If parameters are already used by the configuration, the values are transferred to the respective columns of the connection table. If there are differences between the configured values, the values of the connection table have priority.

###### Parameters for redundant connection paths

If redundant connection paths are configured, these are configured in the same way as the main paths.

The parameters of the redundant connection paths are distinguished by the following suffix:

- ***** 
  **(red)**

Example:

- **Start interface (red.)**

  Interface of the starting point module through which the redundant connection runs.

The parameters of the redundant connection routes have the same functions as those of the main routes. Only the parameters of the main routes are listed in the following description.

###### Greyed-out parameters

Greyed-out parameters cannot be configured for one of the following reasons:

- A value is preassigned that is either generally valid or configured elsewhere.
- Alternative values are not allowed.

  Example: Endpoint of the connection is the master. You cannot configure the following parameters:

  - Unsolicited

    This is a station parameter.
  - End subscriber

    The station address is taken from the configuration for modules from the project.

###### Parameters

- **Name**

  You can change the default name of the connection segment between two subscribers.

  See section [Creating telecontrol connections](#creating-telecontrol-connections) for information on this.
- **Starting point**

  Select the desired starting point of the connection from the drop-down list.

  - The starting point of a connection is a CPU.
- **Start subscriber**

  Station address of the starting point
- **Start interface**

  Interface of the starting point module through which the connection runs.
- **Endpoint**

  Select the endpoint of the connection.

  Endpoints of a connection can be:

  - A CPU
  - A third-party device

    The network node type of third-party devices is configured in the parameter group of the connection, see section [Third-party device parameters](#third-party-device-parameters).
- **End subscriber**

  Station address of the endpoint
- **Partner list**

  When a connection partner ("Endpoint") is selected that is located in the STEP 7 project, its station address ("End subscriber") is automatically entered in the Partner list.

  > **Note**
  >
  > **Manual entries**
  >
  > You must manually enter the station addresses in the following situations:
  >
  > - **Third-party device**
  >
  >   For a third-party device that is not configured in the STEP 7 project, you must enter the station address manually.
  > - **Node station**
  >
  >   The Partner list of a connection segment that transfers data from or to additional stations must contain the station address of all partners. This is the case for connection segments in which the subscriber is a node station. Here you must enter the station addresses of the additional partners manually.
  >
  >   Enter the station addresses ("End subscriber") separated by commas.

  For an example of a node station, see the figure in section [Configuring DNP3/IEC connections](#configuring-dnp3iec-connections). You configure three stations:

  - Master

    Name: "15_4", station address: "1"
  - Node station

    Name: "15_3_node", station address: "2"
  - Station

    Name: "15_6", station address: "3"

  Explanation:

  - Connection segment "_5"

    The connection segment "_5" runs from the master to the node station. The station address "2" of the node station is automatically entered in the partner list.

    Because the data from and to the station "15_6" is also transferred over the connection segment (see connection "_6"), you must enter the station address "3" manually.
  - Connection segment "_6"

    The same is true for the connection segment "_6" between station and node station over which the data is also to be transferred from and to the master.

    The following station addresses must be entered here:

    ‑ "1" for the End subscriber from connection "_3"

    ‑ "2" for the End subscriber from connection "_3"
- **End interface/address**

  Interface of the endpoint

  For a third-party device that is not configured in the STEP 7 project, you must enter the following manually:

  - Ethernet connection: IP address of the endpoint
  - Dedicated line connection: Station address of the endpoint
  - Dial-up network: Telephone number of the endpoint
- **DNP3 level**

  Specifies the DNP3 conformity level (DNP3 implementation level) supported by the partner: Level 1, 2, 3, 4 and Level 4+

  The conformity level referred to as Level 4+ contains the functional scope of Level 4 and also the support of additional data types / variations; see also data point types in the section [Datapoint types](#datapoint-types).
- **End port**

  Number of the listener port of the partner

  With the default setting, the value 20000 is entered for all partners. The value can be changed. You need to enter the port number for a third-party device.

  Range of values: 0 ... 65535

  Default: 20000
- **Partner monitoring time**

  If the station module does not receive a sign of life from the master on the application layer within the configured time, it classifies the connection as disrupted and terminates it.

  The master module expects a response from the station after sending data within the configured time.

  With the setting 0 (zero), the function is disabled.

  See "Partner monitoring time" parameter, section [Transmission settings – DNP3](#transmission-settings-dnp3).
- **Transport prot.**

  Relevant for all subscriber types

  Select the transport protocol:

  - TCP
  - UDP
- **Unsolicited**

  Transfer mode for events

  - Yes

    Event telegrams are transferred immediately.

    If events are present, the station independently establishes a connection to the master.

    If unsolicited transmission in the master is disabled, the master sends the "DISABLE_UNSOLICITED" function code (unsolicited telegrams cannot be sent by the station). In this case, the station saves the events without sending them immediately.
  - No

    Event telegrams are only transmitted when data is requested from the master.
  > **Note**
  >
  > **Setting for dedicated lines**
  >
  > When connecting a serial interface to a DNP3 dedicated line with the "half-duplex" setting, you must set the parameter to "No".
  >
  > To avoid collisions, you should also use this setting when connecting to full-duplex multidrop dedicated lines.

  You define the number of repetitions and the monitoring time for the respective communications module, see section [Settings DNP3 station](#settings-dnp3-station).
- **Event polling**

  Relevant for master, third-party device (master)

  The "Event polling interval" defines the cycle in which the DNP3 master station polls events of the station. The interval is specified as a multiple of the "Polling basic interval" (seconds) of the master, see [Settings DNP3 master function](#settings-dnp3-master-function).

  The value configured here is the factor for the polling basic interval. The sum of the two values provides the length of the event polling interval in seconds.

  Range of values: 0 ... 65535

  The value configured for the station is overwritten by the parameter at the connection segment.
- **Class 0 polling**

  Relevant for master, third-party device (master)

  The Class 0 polling interval determines the cycle in which the DNP3 master polls class 0 data from the image memory of the station. The interval is specified as a multiple of the parameter "Polling basic interval" (seconds) of the master, see [Settings DNP3 master function](#settings-dnp3-master-function).

  The value configured here is the factor for the polling basic interval. The sum of the two values provides the length of the class 0 polling interval in seconds.

  Range of values: 0 ... 65535

  Default: 1

  With the setting 0 (zero), the function is switched off, class 0 data is not transmitted cyclically.

  The value configured for the station is overwritten by the parameter at the connection segment.
- **Max. polling duration**

  Relevant for master, third-party device (master)

  Specifies the maximum time period during which the master may continuously call this station. Even if data is still pending for transmission in the station after this time, the calls from the master station are canceled. This means that the master station is once again available to other stations.

  Range of values: 0 ... 65535

  Default: 10

  With the setting 0 (zero), the function is disabled; in other words, the calling period is unlimited.

  The value configured for the station is overwritten by the parameter at the connection segment.
- **Polling mode**

  Relevant for master, third-party device (master)

  Mode in which the master station calls the station.

  Range of values:

  - Cyclic

    The station is called cyclically. The duration of the polling cycle is equal to the "Class 0 polling interval", see above.
  - After startup

    The station is only called after the initial startup and after a restart.

    If no unsolicited transmission is enabled for a station, no data is transmitted during operation when this option is selected.

  The value configured for the station is overwritten by the parameter at the connection segment.
- **Temporary**

  Relevant for partners with temporary connections (e.g. RTU)

  Select this option if the partner supports temporary connections that it can terminate itself. The connection termination by the partner is then not interpreted as a connection termination.

  For example, the partner might be an RTU3000C on which the "Temporary connection" option is selected.

###### "Properties" tab of the connection

**Transmission settings DNP3**

- **Form of transfer**

  Relevant for station, third-party device (station)

  Determines the send sequence of events to the DNP3 master station.

  - Type-specific

    Bundled transmission according to data type
  - Chronological

    Chronological transmission by time stamp

##### Connection table - IEC

In the connection table, you configure the parameters of the individual connection segments.

If parameters are already used by the configuration, the values are transferred to the respective columns of the connection table. If there are differences between the configured values, the values of the connection table have priority.

###### Parameters for redundant connection paths

If redundant connection paths are configured, these are configured in the same way as the main paths.

The parameters of the redundant connection paths are distinguished by the following suffix:

- ***** 
  **(red)**

Example:

- **Start interface (red.)**

  Interface of the starting point module through which the redundant connection runs.

The parameters of the redundant connection routes have the same functions as those of the main routes. Only the parameters of the main routes are listed in the following description.

###### Greyed-out parameters

Greyed-out parameters cannot be configured for one of the following reasons:

- A value is preassigned that is either generally valid or configured elsewhere.
- Alternative values are not allowed.

  Example: Endpoint of the connection is the master. You cannot configure the following parameters:

  - Unsolicited

    This is a station parameter.
  - End subscriber

    The station address is taken from the configuration for modules from the project.

###### Parameters

- **Name**

  You can change the default name of the connection segment between two subscribers.

  See section [Creating telecontrol connections](#creating-telecontrol-connections) for information on this.
- **Starting point**

  Select the desired starting point of the connection from the drop-down list.

  - The starting point of a connection is a CPU.
- **Start subscriber**

  ASDU address of the starting point
- **Struct. start address**

  Structured ASDU address of the starting point

  For information on the configuration, see [Subscriber numbers](#subscriber-numbers-1).
- **Start interface**

  Interface of the starting point module through which the connection runs.
- **Endpoint**

  Select the endpoint of the connection.

  Endpoints of a connection can be:

  - A CPU
  - A third-party device

    The network node type of third-party devices is configured in the parameter group of the connection, see section [Third-party device parameters](#third-party-device-parameters).
- **End subscriber**

  Station address of the endpoint
- **Partner list**

  When a connection partner ("Endpoint") is selected that is located in the STEP 7 project, its station address ("End subscriber") is automatically entered in the Partner list.

  > **Note**
  >
  > **Manual entries**
  >
  > You must manually enter the station addresses in the following situations:
  >
  > - **Third-party device**
  >
  >   For a third-party device that is not configured in the STEP 7 project, you must enter the station address manually.
  > - **Node station**
  >
  >   The Partner list of a connection segment that transfers data from or to additional stations must contain the station address of all partners. This is the case for connection segments in which the subscriber is a node station. Here you must enter the station addresses of the additional partners manually.
  >
  >   Enter the station addresses ("End subscriber") separated by commas.

  For an example of a node station, see the figure in section [Configuring DNP3/IEC connections](#configuring-dnp3iec-connections). You configure three stations:

  - Master

    Name: "15_4", station address: "1"
  - Node station

    Name: "15_3_node", station address: "2"
  - Station

    Name: "15_6", station address: "3"

  Explanation:

  - Connection segment "_5"

    The connection segment "_5" runs from the master to the node station. The station address "2" of the node station is automatically entered in the partner list.

    Because the data from and to the station "15_6" is also transferred over the connection segment (see connection "_6"), you must enter the station address "3" manually.
  - Connection segment "_6"

    The same is true for the connection segment "_6" between station and node station over which the data is also to be transferred from and to the master.

    The following station addresses must be entered here:

    ‑ "1" for the End subscriber from connection "_3"

    ‑ "2" for the End subscriber from connection "_3"
- **End interface/address**

  Interface of the endpoint

  For a third-party device that is not configured in the STEP 7 project, you must enter the following manually:

  - Ethernet connection: IP address of the endpoint
  - Dedicated line connection: Station address of the endpoint
  - Dial-up network: Telephone number of the endpoint
- **End port**

  Number of the listener port of the partner

  With the default setting, the value 2404 is entered for all partners. The value can be changed. You need to enter the port number for a third-party device.

  Range of values: 0 ... 65535

  Default: 2404
- **Partner monitoring time**

  If the station module does not receive a sign of life from the master at application level within the configured time, it classifies the connection as faulty. The module terminates the connection and tries to re-establish it.

  Range of values: 0 ... 65535

  Default: 0

  With the setting 0 (zero), the function is disabled.
- **Unsolicited**

  Transfer mode for events

  - Yes: Event telegrams are transferred immediately.
  - No: Event telegrams are only transmitted when data is requested from the master.

  For information on the parameter, see section [IEC-specific parameters](#iec-specific-parameters).
- **Polling mode**

  Relevant for master, third-party device (master)

  This is where you define the mode in which the master station calls the station.

  The value configured for the station is transferred to the master station and stored there.

  Ranges of values:

  - Cyclic

    The station is called cyclically. The duration of the polling cycle is equal to the "Class 0 polling interval", see above.
  - After startup

    The station is only called after the initial startup and after a restart.

    If no unsolicited transmission is enabled for a station, no data is transmitted during operation when this option is selected.
- **Temporary**

  Relevant for partners with temporary connections (e.g. RTU)

  Select this option if the partner supports temporary connections that it can terminate itself. The connection termination by the partner is then not interpreted as a connection termination.

  For example, the partner might be an RTU3000C on which the "Temporary connection" option is selected.

##### Third-party device parameters

###### Third-party device parameters

Only valid for partners that are not configured in the STEP 7 project. These partners are created in the connection table as "Third-party device" for the "Endpoint" parameter.

- **Network node type third-party device**

  Network node type of the third-party device that is accessible via the selected connection path:

  - Master station

    (Master)
  - Node station

    For modules that act as a node station, the following applies:

    The interface in the direction of the master station is configured as a "node station".

    The interface in the direction of the lower-level network is configured as a "Master station".
  - Station
- **Network node type third-party device (red.)**

  Network node type of the third-party device that is accessible via a redundant connection path. The option is available when a "third-party device" is connected via the "Start interface" for the "Start subscriber".

  For the three options, see above.

##### Request options (IEC)

The following parameters can be found in the parameter groups "Options 1st Path" / "Options 2nd Path" of the IEC connections.

###### Call intervals

The following parameters define the intervals of special calls of the master for the station (cause of transmission 20 - 41).

All parameters are configured as multiples of the "polling basic interval" (see master).

- **Interval for general request**

  Defines the interval with which general requests of the master are answered.
- **Interval for group request**

  Defines the interval with which the respective group request of the master is answered.
- **Interval for counter general request**

  Defines the interval with which counter general requests of the master are answered.
- **Interval for counter group request**

  Defines the interval with which the respective counter group request of the master is answered.

You define the setting as to whether a general request is answered and the assignment to a group request for each individual data point in the data point configuration.

##### Redundant DNP3 master group with 3 servers

###### DNP3 connections with three servers

With connection to a redundant control center, a communications module can establish a maximum of 2 connections with a master at the same time.

With a specific connection configuration, the module as outstation can set up a connection to a third server if one of the two connections of the redundancy group fails.

###### Requirements

The function is supported by the following modules and firmware versions:

- TIM 1531 IRC ≥ V2.1
- CP 1542SP-1 IRC ≥ V2.1
- CP 1243-1 ≥ V3.2
- CP 1243-8 IRC ≥ V3.2

###### Configuration

**Configuring the station modules**

- Deactivate the "IP address check" parameter

  - For the communications modules of the stations, open the parameter group "Ethernet interface &gt; Advanced options &gt; Settings DNP3 station".
  - Set the "IP address check" option to "Do not check IP address".

  In this setting, the IP address of the communication partner is not checked. This ensures that any station in the network that is configured with the DNP3 station address of the master may connect to the station module regardless of its IP address.

**Creating connections**

1. Create the station with the communications modules and the networks, connect them and configure the components.

   Do not create any stations for the three masters. These are configured as "Third-party device" in the editor of the telecontrol connections in STEP 7.
2. Create two DNP3 connections with the CP in the "Network data" task card.
3. Create two DNP3 connections with the station module in the "Network data &gt; TeleControl &gt; DNP3" task card.

   The two connection segments are almost identical but differ in the configuration of the "End interface (red.)" parameter:

   The two connection segments are characterized by the following configuration:

- Section_1

  - Starting point: Communications module (outstation)
  - Start interface: Ethernet interface of the module
  - Start interface (red.): Ethernet interface of the module
  - End point: Third-party device
  - End interface: IP address of the interface of master 1
  - End interface (red.): IP address of the interface of master 2
- Section_2

  - Starting point: Communications module (outstation)
  - Start interface: Ethernet interface of the module
  - Start interface (red.): Ethernet interface of the module
  - End point: Third-party device
  - End interface: IP address of the interface of master 1
  - End interface (red.): IP address of the interface of master 3

The figure below shows an example of the connection table with three redundant masters.

![Connection table with three redundant masters](images/127790292619_DV_resource.Stream@PNG-en-US.png)

Connection table with three redundant masters

All three masters are given the same DNP3 station address ("End subscriber"); in the example, this is "0".

The IP addresses shown in the figure are assigned to the following interfaces:

- 192.168.0.1

  IP address of master 1
- 192.168.0.2

  IP address of master 2
- 192.168.0.3

  IP address of master 3

**Editing connections**

1. Select the row of the first connection.
2. In the properties dialog of the connection, select the "Third-party device parameters" tab.
3. There, set the network node type of the third-party device for both routes to "Master station".

Select the same settings for the second connection (second row).

![Configuration](images/127814171915_DV_resource.Stream@PNG-en-US.png)

Configure the remaining connection parameters of the connections as described in the other sections.

##### Security statistics options (IEC 60870-5-104)

###### Security statistics (IEC 60870-5-104)

The following table contains those security statistics options according to IEC/TS 60870-5-7 and IEC/TS 62351-5 that you can configure for the individual telecontrol connection segments.

When the options are enabled, the communications module as station sends security statistics events to the master, where they are available for further evaluation. Based on the frequency of these events, you can reach conclusions on possible attacks or vulnerabilities of your system.

Note that security statistics events are only output if a SCADA system is connected to the master.

###### Security statistics options

When Secure Authentication is used, a station keeps statistics for different values.

The events are transferred via the ASDU type "Information 41" (integrated total for the statistic).

The following table lists the statistics parameters supported by the module according to IEC/TS 62351-5.

- Threshold

  A threshold value can be configured for each statistics value. When this threshold is exceeded, transfer as event to the partner is triggered.

  The range of values is 0...65535.

  With the setting 0 (zero), the function is disabled. No statistics data is transferred for the value in question.
- IOA

  You need to assign an IOA (IOA - Information object address) to each value in the statistics via the configuration.

  The range of values is 0...16777215.

| Parameter | Default |
| --- | --- |
| Unexpected messages threshold | 3 |
| Unexpected messages (IOA) | 0 |
| Authorization failures threshold | 5 |
| Authorization failures (IOA) | 0 |
| Authorization failures (IOA) | 5 |
| Authentication failures (IOA) | 0 |
| Response timeout threshold | 3 |
| Response timeouts (IOA) | 0 |
| Key changes due to authentication failure threshold | 3 |
| Key changes due to authentication failure (IOA) | 0 |
| Sent messages threshold (total) | 100 |
| Total number of sent messages (IOA) | 0 |
| Received messages threshold (total) | 100 |
| Total number of received messages (IOA) | 0 |
| Sent critical messages threshold | 100 |
| Sent critical messages (IOA) | 0 |
| Received critical messages threshold | 100 |
| Received critical messages (IOA) | 0 |
| Discarded messages threshold | 10 |
| Discarded messages (IOA) | 0 |
| Sent error messages threshold | 10 |
| Sent error messages (IOA) | 0 |
| Received error messages threshold | 10 |
| Received error messages (IOA) | 0 |
| Successful authentications threshold | 100 |
| Successful authentications threshold | 0 |
| Session key changes threshold | 10 |
| Session key changes (IOA) | 0 |
| Failed session key changes threshold | 5 |
| Failed session key changes (IOA) | 0 |

### Security

This section contains information on the following topics:

- [Telecontrol: Handling certificates for TLS](#telecontrol-handling-certificates-for-tls)

#### Telecontrol: Handling certificates for TLS

##### Secure communication with telecontrol modules

The communication via TLS described below is supported by the following modules:

- TIM 1531 IRC V2.3 as of firmware version V2.3
- CPU 1500 as of firmware version V2.9
- CP 1542SP-1 IRC as of firmware version V2.2
- ET 200SP CPU as of firmware version V2.9

The communication modules use TLS 1.2; the communication complies with IEC 62351-3.

##### Communication between CPU and telecontrol module

**CP: Communication via backplane bus**

If the CPU and telecontrol CP are in the same rack, communication between them runs via the backplane bus. The CPU is automatically assigned to the telecontrol CP.

**TIM 1531 IRC: TLS communication with the CPU via Ethernet**

The TIM 1531 IRC is not inserted in the rack of the CPU. The connection to the CPU is via Ethernet and supports secure communication via TLS for all usable telecontrol protocols.

For communication via TLS, you need to use a newly created CPU certificate and specify it to the TIM in the "Subscriber numbers" parameter group. When you create a certificate for the CPU and assign the TIM to the CPU, the certificate is entered automatically.

##### Creating the CPU certificate and assigning the CPU

**Requirements**

The following requirements must be met in order to create and assign certificates:

- As STEP 7 project user, you have at least the rights of the "NET Administrator" role.

  For more on this, see "Security settings &gt; Users and roles &gt; Assigned roles".
- The devices have the required minimum firmware version, see above.
- The configuration data of the CPU is protected.

  For more on this, see "Protection &amp; Security &gt; Protection of confidential PLC configuration data"

To be able to assign your local CPU to the TIM 1531 IRC, the following requirement must be met:

- CPU and TIM 1531 IRC are networked.
- The desired telecontrol protocol is enabled for the TIM under "Communication types".

**Certificates of SIMATIC NET devices**

SIMATIC NET communications modules generally use the global certificate manager. You can find this in the project navigation under "Security settings &gt; Security features".

**Creating the certificate of the CPU**

First, you need to create a certificate generated by the system (global certificate manager of the STEP 7 project) for the CPU. The locally created certificate of the CPU cannot be used for communication.

When the CPU is assigned to the TIM (see below), the ID of the newly created CPU certificate is automatically entered at the following locations:

- In the "Subscriber numbers" dialog of the TIM
- In the certificate manager of the TIM as partner certificate

Proceed as follows to create the CPU certificate:

1. For the CPU, select the parameter group "Protection &amp; Security &gt; Certificate manager &gt; Global security settings".
2. Enable the "Use global security settings for certificate manager" option.

   **Note:**
     
   When the option is enabled, existing certificates of the CPU are deleted.
3. Go to "Protection &amp; Security &gt; Connection mechanisms &gt; Communication to TIA Portal and HMI".
4. In the "PLC communication certificate" row, right-click on the icon for the drop-down list.
5. Click the "Create" button under the open drop-down list.

   The "Create certificate" dialog opens. The following options must be selected or are recommended:

   - Usage: TLS Client / Server
   - Certificate authority (CA): Signed by certification authority
   - Common name of subject: Name of the selected CPU
   - Encryption method: EC (recommended)
   - Hash algorithm: sha256 (recommended)

   If necessary, you can add another address type for the CPU under "Subject Alternative Name (SAN)".
6. Retain the settings and click "OK".

   The newly created TLS certificate is shown in the table of device certificates for the device.
7. Open the global certificate manager in the project navigation:

   "Security settings &gt; Security features &gt; Certificate manager &gt; Device certificates"
8. Select the newly created certificate of the CPU (see above for ID) and open the "Assign" shortcut menu.
9. In the list, select the TIM to which the CPU should be assigned.
10. In the "Used as" row in the ("Not assigned") cell, select the "Trusted certificate" option and click on the green checkmark.
11. Close the dialog with OK.

**Assign CPU to TIM 1531 IRC**

1. For the TIM that is to communicate with the CPU, open the "Subscriber numbers" parameter group.
2. Right-click on the icon for the drop-down list in the "Assigned CPU" row.

   The list of networked CPUs opens.
3. Select the CPU to be assigned to the TIM and click on the green checkmark below it.

   The name of the CPU is displayed in the "Assigned CPU" row.

   At the same time, the ID of the certificate created previously for the CPU is automatically displayed in the "Communication certificate" row.

**Further configuration**

Then configure the other stations as communication partners and the corresponding telecontrol connections.

##### TLS for telecontrol connections

**TLS for project-internal telecontrol connections**

You can configure secure communication via TLS for telecontrol connections of communications modules that use one of the following protocols:

- IEC 60870-5
- DNP3

You configure secure communication for the telecontrol connections ("TeleControl" task card).

1. First create the telecontrol connections.
2. Select the main connection and the "Secure Communication (TLS)" parameter group there.
3. Activate the "Enable secure communication" option.

When all certificates of the connection partners are present, the "own certificate ID" and the "partner certificate ID" are automatically applied to the entire connection, including sub-connections, for Siemens devices.

**TLS for telecontrol connections with third-party devices**

If you want to use secure communication via TLS for telecontrol connections with third-party devices, you need to perform some additional steps.

First, set the secure listener port for TLS or check the setting (Basic settings &gt; Secure listener port). The port number is needed for the connection partner.

You must create or import a certificate for the third-party device, apply the ID to the connection parameters, export the certificate and the associated CA certificate and import it into the third-party device.

First create the connection as described above and then activate the "Enable secure communication" option. Proceed as follows.

**Importing a third-party certificate or creating and assigning it**

Alternatively, you can make the third-party certificate available to the STEP 7 project:

- Import

  If required, you can save and import the certificate of the third-party device in the file system of the engineering station.

  To import, open the "Trusted certificates and root certification authorities" tab in the global certificate manager, click in a free row and open the "Import" shortcut menu.

  You must then assign the imported certificate to the communication module (see below).

  Then enter the ID of the imported certificate and own certificate in the connection properties.

  Check the secure listener ports in the connection properties.

  Check the Network node type in the connection properties ("Third-party device parameters" parameter group). If the third-party device is the master, select "Master station".
- Create

  Alternatively, you can create a certificate for the third-party device in STEP 7 and import it into the third-party device.

  Follow these steps:

1. Open the global certificate manager in the project navigation:

   "Security settings &gt; Security features &gt; Certificate manager &gt; Device certificates"
2. Click on the "Create" shortcut menu in a free row.

   The "Create certificate" dialog opens.
3. Select the following options for the certificate of the third-party device:

   - Usage: TLS Client / Server
   - Certificate authority (CA): Self signed
   - Common name of subject: Enter the name of the third-party device.

   Adapt the other parameters to the functionality of the third-party device.

   Recommended settings:

   - Encryption method: RSA
   - Key length: 2048
   - Hash algorithm: sha256
4. Click "OK" to close the dialog.

   The certificate appears in the table.

   You will need the certificate ID for the assignment and the telecontrol connection.
5. Select the newly created certificate and open the "Assign" shortcut menu.
6. In the list, select the module the third-party device will communicate with via the telecontrol connection.
7. In the "Used as" row in the ("Not assigned") cell, select the "Trusted certificate" option and click on the green checkmark.
8. Close the dialog with OK.

   You will need the certificate ID for the telecontrol connection.

**Entering the certificate ID in the telecontrol connection**

1. Switch back to the created telecontrol connection, parameter group "Secure Communication (TLS)".
2. Enter the following values manually for connection with a third-party device:

   - Partner certificate ID: ID of the imported or manually created certificate for the third-party device
   - Own certificate ID: ID of the certificate of the module

   You can find the IDs in the certificate manager of the global security settings.
3. Align the port numbers and third-party device parameters.

**Exporting a certificate for a third-party device and importing it**

When you have imported the device certificate of the third-party device, you only need to export the device certificate of the module and the associated CA certificate.

If you have created the device certificate of the third-party device in STEP 7, you also have to export this.

Follow these steps:

1. Device certificate for the third-party device created in STEP 7

   - In the global certificate manager, open the "Trusted certificates and root certificate authorities" tab.
   - Select the device certificate for the third-party device and click the "Export certificate" shortcut menu.
   - Save the certificate in the file system of the engineering station.

     You can change the default file format "*.der".

     You can find a description of the functions of the certificate file formats in the "Exporting certificates" section in the help system.
2. Device certificate of the module

   - In the global certificate manager, switch to the "Device certificates" tab.
   - Select the device certificate of the module as partner certificate for the third-party device.
   - Make the "Issuer" column fully visible.

     You need the name of the issuer to export the issuing CA certificate.
   - Export the selected device certificate of the module using the "Export certificate" shortcut menu.
3. Issuing CA certificate

   - Change to the "Certificate authority (CA)" tab.
   - Select the CA certificate that signs the device certificate of the module.

     When you expand the CA certificate, all derived device certificates, including that of the module, are displayed below it.
   - Export the selected CA certificate via the "Export certificate" shortcut menu.
4. For communication during runtime, export all saved certificates into the third-party device or its configuration tool.

Continue with the configuration of the other parameters.

### Data point editor

This section contains information on the following topics:

- [Configuring data points and messages](#configuring-data-points-and-messages)
- [Datapoint types](#datapoint-types)
- [Process image, type of transmission, event classes](#process-image-type-of-transmission-event-classes)
- [ST7 data points](#st7-data-points)
- [DNP3 and IEC data points](#dnp3-and-iec-data-points)
- [Status IDs of the data points](#status-ids-of-the-data-points)
- [Data point index](#data-point-index)
- [Read cycle](#read-cycle)
- ["Local setpoint input" tab](#local-setpoint-input-tab)
- ["Trigger“ tab](#trigger-tab)
- [Threshold value trigger](#threshold-value-trigger)
- [Analog value preprocessing](#analog-value-preprocessing)
- [Command options](#command-options)
- [Masks](#masks)

#### Configuring data points and messages

##### Preliminary overview: TIM modules with SINAUT ST7

TIM modules using the SINAUT ST7 telecontrol protocol can use the "Telecontrol ST7" (TD7onCPU) block library as an alternative to the data points (TD7onTIM).

This section applies to "TD7onTIM".

##### Data point-related communication with the CPU

No program blocks need to be programmed for the telecontrol modules with data point configuration to transfer user data between the station and communications partner. The data areas in the memory of the CPU intended for communication with the communications partner are configured data point-related on the module. Each data point is linked to a PLC tag or a DB tag.

##### Requirement: Created PLC tags or DB tags

To configure the data points, the associated tags must have been created in the CPU.

The tags for the data point configuration can be created in a data block (DB), the default tag table or a user-defined tag table.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Writing values to outputs**  - PLC tags   Note that when PLC tags are referenced, a write access causes the values to be written immediately to the outputs of the CPU without first being processed by the user program.   Writing values has a direct influence on the process. - DB variables   When referencing to DB variables, written values are only used when processed by the user program. |  |

All variables intended to be used for data point configuration must have the attribute "Reachable from HMI/OPC UA/Web API".

For writable variables, the "Writable from HMI/OPC UA/Web API" attribute also needs to be enabled.

Address areas of the PLC tags are input, output or bit memory areas on the CPU.

The formats and S7 data types of the tags that are compatible with the protocol-specific data point types of the CP can be found in the section [Datapoint types](#datapoint-types).

##### Access to the memory areas of the CPU

The values of the PLC tags or DBs referenced by the data points are read and transferred by the CP / TIM to the communication partner.

Data received from the communication partner is written by the CP / TIM to the CPU via the tags.

##### Configuring the data points and messages in STEP 7

You configure the data points in STEP 7 in the data point and message editor. You can open both editors alternatively as follows:

- Selection of the communication module in the network view or device view

  Shortcut menu "Open the data point and messages editor"
- Via the project navigation:

  Project &gt; Directory of the station &gt; Local modules &gt; desired communication module

  ![Open the data point and messages editor](images/86752686347_DV_resource.Stream@PNG-en-US.png)

  Open the data point and messages editor

  By double-clicking on the entry, the data point or message editor opens.

After opening the editor window using the two entries to the right above the table, you can switch over between the data point and message editor.

![Switching over between the two editors](images/93771463947_DV_resource.Stream@PNG-en-US.png)

Switching over between the two editors

##### Creating obects

With the data point or message editor open, create a new object (data point / message) by double clicking "&lt;Add object&gt;" in the first table row with the grayed out entry.

A preset name is written in the cell. You can change the name to suit your purposes but it must be unique within the module.

![Data point table - here in a tag table](images/99164227851_DV_resource.Stream@PNG-en-US.png)

Data point table - here in a tag table

You configure the remaining properties of every object using the drop-down lists of the other table columns and using the parameter boxes shown at the bottom of the screen.

##### Assigning data points to their data source

After creating it, you assign a new data point to its data source. Depending on the data type of the data point a PLC tag can serve as the data source.

For the assignment you have the following options:

- Click on the table symbol ![Assigning data points to their data source](images/87213436299_DV_resource.Stream@PNG-de-DE.png) in the cell of the "PLC tag" column.

  All configured PLC tags and the tags of the created data blocks are displayed. Select the required data source with the mouse or keyboard.
- Click the symbol ![Assigning data points to their data source](images/87217252363_DV_resource.Stream@PNG-de-DE.png).

  A selection list of the configured PLC Tags and the blocks is displayed. From the relevant table, select the required data source.
- In the name box of the PLC tag, enter part of the name of the required data source.

  All configured PLC tags and tags of the data blocks whose names contain the letters you have entered are displayed.

  ![Assigning data points to their data source](images/87217261067_DV_resource.Stream@PNG-de-DE.png)

  Select the required data source.

**Alternative method for creating specific data points**

1. Click (multiple times) in the first free row of the table (Add tag).
2. With the keyboard, type in part of the name of a tag.

   All tags that contain the entered string are shown.
3. Select the required tag with a mouse click.

![Assigning data points to their data source](images/154111536395_DV_resource.Stream@PNG-en-US.png)

**Simplified creation of multiple data points**

You can create multiple data points in one step in the following way:

1. Open the data point table.
2. Expand the station in the project navigation and select either:

   - "Program blocks" folder (for the assignment of DB tags)  
     or
   - "PLC tags" folder (for the assignment of PLC tags)
3. Select the relevant DB or the desired tag table.

   The content is displayed in the "Detail view" window under the project navigation.
4. In the detail view, select all tags that you want to use for the assignment to data points.

   (Multiple selection with &lt;Shift&gt; or &lt;Ctrl&gt;)
5. Drag-and-drop the selected tags into the data point table.

![Assigning data points to their data source](images/154105951115_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Assignment of parameter values to PLC tags**
>
> The mechanisms described here also apply if you have to assign the value of a parameter to a tag. The input boxes for the tag (e.g.: PLC tag for partner status support the functions described here for selecting the tag.

##### Arranging columns and rows, showing/hiding columns

As with many other programs, you can arrange the columns and sort the table according to your needs in the data point or message editor:

- Arrange columns

  If you click on a column header with the left mouse button pressed, you can move the column.
- Sorting objects

  If you click briefly with the left mouse button on a column header, you can sort the objects of the table in ascending or descending order according to the entries in this column. The sorting is indicated by an arrow in the column header.

  After sorting in descending order of a column the sorting can be turned off by clicking on the column header again.
- Adapting the column width

  You can reach this function with the following actions:

  - Using the shortcut menu that opens when you click on a column header with the right mouse button.

    "Optimize width", "Optimize width of all columns"
  - If you move the cursor close to the limit of a column header, the following symbol appears:

    ![Arranging columns and rows, showing/hiding columns](images/99164321419_DV_resource.Stream@PNG-en-US.png)

    When it does, double-click immediately on the column header. The column width adapts itself to the broadest entry in this column.
- Showing / hiding columns

  You call this function using the shortcut menu that opens when you click on a column header with the right mouse key. You have the following options:

  - Show/Hide

    If this option is selected, a table opens in which the displayed columns (parameters) are marked. You can select an additional column or deselect a column.

    If you click on "More" at the end of the table, a window opens in which all available columns for selection are listed.
  - Show all columns

    If this option is selected, all columns are displayed.

##### Copy data points and messages

As with many other programs, you can copy and paste objects in the data point or message editor.

If you right-click in the row of an object in the table, you can access this function from the shortcut menu:

- Cut
- Copy
- Paste

  You can paste cut or copied objects within the table or in the first free row below the table.

  You can also paste cut or copied objects into tables of other communication modules of the same type and with the same telecontrol protocol.
- Delete

If you hold down the &lt;Ctrl&gt; key, you can select several rows that are not contiguous.

With the &lt;Shift&gt; key pressed, you can select the beginning and the end of a contiguous area.

##### Automatic cell filling (ST7 data points only)

Automatic cell filling is available for ST7 data points in the following function versions:

- **Overwrite**
- **Paste**

Automatic filling out is particularly useful for the following applications:

- You have copied ST7 data points.

  You want to fill the cells of a column with the same value or in ascending or descending order.
- You have created ST7 data points.

  You want to add more data points of the same type.

Proceed as follows to fill in the form automatically:

1. Select one or more cells (start cells) of a column for the function.
2. Move the cursor to the lower right corner of the selection and drag the cursor down to the target cells.

   ![Automatic cell filling (ST7 data points only)](images/111011833739_DV_resource.Stream@PNG-en-US.png)

   A dialog box opens in which you select the desired function version.
3. Select the desired "Overwrite" or "Paste" option and click "OK".

**Overwrite**

Depending on the desired content of the target cells, proceed as follows:

- Select a single start cell if you want to overwrite the target cells with the value of the start cell.
- Select at least two start cells with numerically ascending values if you want to overwrite the target cells with numerically ascending values. This version is shown above in step 2.

  If you select two cells with different text contents (e.g. Bool[1] and DWord[1] PLC tag), then the target cells are overwritten only with the first value.

  You select multiple cells as you would for copying:

  - &lt;Ctrl&gt; key: Selection of multiple cells. The cells must be contiguous.
  - &lt;Shift&gt; key: Selection of a contiguous area
- Select multiple start cells with any value block if you want to overwrite the target cells with this value block.

  Example: You select three cells with the values 4, 12 and 7. The target cells are then continuously overwritten with blocks of 4, 12 and 7.

Exception: Special rules apply to the names of the data points; see below.

If the start cells are selected as shown in the figure above, the target cells are overwritten with the following values after dragging the cursor.

![Automatic cell filling (ST7 data points only)](images/110985000203_DV_resource.Stream@PNG-en-US.png)

You can also overwrite target cells in numerical descending order if the two start cells contain descending values or if you select two cells with the highest numbers and drag the cursor upwards. If overwritten in descending order, the lowest value is 1, since 0 is an invalid value.

Overwriting can be used in the following columns:

- Name

  When overwriting the names of data points, no consecutive names are assigned. However, a unique name is assigned to each data point.
- PLC tag

  Requirement: The target cells are assigned data point types that are compatible with the start cell.
- Data point type

  Requirement: The data points of the target cells use the same PLC tag.
- Type of transmission

  Requirement: The data points of the target cells use the same PLC tag and have the same transmission direction (input or output).
- Object channel

  The rules for assigning channel numbers apply, see section [ST7 data points](#st7-data-points).
- Object number

  The rules for assigning object numbers apply.

**Paste**

This option inserts new rows at the end of the table.

- Select one or more cells and then drag the cursor to other cells.

  The total number of cells selected after dragging the cursor is inserted.

The function is supported in the following columns:

- Name
- PLC tag
- Data point type
- Type of transmission
- Object channel
- Object number

##### Exporting and importing data points

To simplify the engineering of larger plants, you can export the data points of a configured module and import them into other modules in the project. This is an advantage particularly in projects with many identical or similar stations or modules.

You can also access the export/import function:

- Using the two symbols above the data point list ![Exporting and importing data points](images/112995957899_DV_resource.Stream@PNG-de-DE.png)
- Via the shortcut menu of the module, if you select it in the network or device view.

  ![Part of the shortcut menu of a telecontrol module](images/112996478347_DV_resource.Stream@PNG-en-US.png)

  Part of the shortcut menu of a telecontrol module

The data point information of a module is saved in exactly one CSV file during export.

It is not possible to import data points of an older project into a project that was created in STEP 7 V15.1 because the scope of parameters of certain data point types is not identical. However, the import works when missing parameters are added in the CSV file (see below).

##### Export

When you call the export function, the export dialog opens. Here, you select the CPs or modules of the project whose data point information needs to be exported. When necessary, you can export the data points of all modules of the project at one time.

In the export dialog, you can select the storage location in the file directory. When you export the data of a module you can also change the preset file name.

When you export from several modules, the files are formed with preset names made up of the station name and module name.

The file itself contains the following information in addition to the data point information:

- Module name
- Module type
- CPU name
- CPU type

##### Editing the export files

You can edit the data point information in an exported CSV file. This allows you to use this file as a configuration template for many other stations.

If you have a project with many stations of the same type, you can copy the CSV file with the data points of a fully configured module for other as yet unconfigured stations and adapt individual parameters to the particular station. This saves you having to configure the data points for every module in STEP 7. Instead, you simply import the copied and adapted CSV file to the other modules of the same type. When you import this file into another module, the changed parameter values of the CSV file are adopted in the data point configuration of this module.

The lines of the CSV file have the following content:

- Line 1: ,Name,Type,

  This line must not be changed.
- Line 2: PLC,&lt;CPU name&gt;, &lt;CPU type&gt;,

  Meaning: PLC (designation of the station class), CPU name, CPU type

  Only the elements &lt;CPU name&gt; and &lt;CPU type&gt; may be changed.

  The CPU type must correspond exactly to the name of the CPU in the catalog.
- Line 3: Module,&lt;module name&gt;,&lt;module type&gt;,

  Meaning: Module (Designation of the module class), module type, module name

  Only the elements &lt;module name&gt; and &lt;module type&gt; may be changed.

  Be careful when changing the module names if you want to import data points into several modules (see below).

  The module type must correspond exactly to the name of the module in the catalog.
- Line 4: Parameter names (English) of the data points

  This line must not be changed.
- Lines 5..n: Values of the parameters according to line 4 of the individual data points

  You can change the parameter values for the particular station.

##### Importing into a module

Before importing the data points make sure that the PLC tags required for the data points have been created.

Note that when you import a CSV file all the data points existing on the module will be deleted and replaced by the imported data points.

Select a CP and select the import function from the shortcut menu of the module. The import dialog opens in which you select the required CSV file in the file directory.

If the information for assigning the individual data points to their respective PLC tags corresponds with the assignment in the original module, the data points are assigned to the respective PLC tags.

When you import data points into a CP, but some required PLC tags have not yet been created in the CPU, the corresponding data point information cannot be assigned. In this case, you can subsequently create missing PLC tags and them assign them the imported data point information. The "Assignment repair" function is available for this (see below).

If the names of the PLC tags in the module into which the import is made have different names than in the module that exported, the corresponding data points cannot be assigned to your PLC tags.

##### Importing into several modules

You can import the data points from several modules into the modules of a different project. To do this in the import dialog select all the required CSV files with the control key.

Before importing the data points, make sure that the respective stations have been created with CPUs of the same name, modules of the same name and PLC tags of the same name.

When you import the corresponding stations of the project are searched for based on the module names in the CSV files. If a target station does not exist in the project or the module has a different name, the import of the particular CSV file will be ignored.

##### Restrictions for the import of data points

In the following situations the import of data points will be aborted:

- An attribute required by the module is missing in the CSV file to be imported.

  Example: If a data point to be imported uses a time trigger, the import will be aborted if no time-of-day synchronization was configured for the module.
- The telecontrol protocol used by the module differs from that of the original module.

  Modules with the same telecontrol protocol are compatible with each other:

Only when importing into several modules:

- The import is aborted when a module or CPU name is different from the data in the CSV file.

##### Assignment repair

If you have named the PLC tags differently in a station to which you want to import them than in the station from which the CSV file was exported, the assignment between data point and PLC tag is lost during the import.

You then have the option to either rename the existing PLC tags appropriately or add missing PLC tags. You can then repair the assignment between unassigned data points and PLC tags. This function is available either via the shortcut menu of the CP (see above) or with the following icon to the upper left in the data point editor: ![Assignment repair](images/86766010763_DV_resource.Stream@PNG-de-DE.png)

If a PLC tag with a matching name is found for a data point by the repair function, the assignment is restored. However the data type of the tag is not checked.

After the assignment repair make sure that you check whether the newly assigned PLC tags are correct.

#### Datapoint types

During the configuration of the user data to be transferred by the communications module, each data point is created as a protocol-specific data point type.

Afterwards the protocol-specific data point types along with the compatible S7 data types are listed.

The "Direction" column shows the transmission direction:

- "in": Monitoring direction
- "out": Control direction

> **Note**
>
> **Effect of the change of arrays for data points**
>
> If an array is modified later, the data point must be recreated.

##### Data point types of the "TeleControl Basic" protocol

Supported data point types and compatible S7 data types

| Format (memory requirements) | Data point type | Direction | S7 data types | Operand area |
| --- | --- | --- | --- | --- |
| **Bit** | Digital input | in | Bool | I, Q, M, DB |
| Digital output | in | Bool | Q, M, DB |  |
| **Byte** | Digital input | in | Byte, Char, USInt | I, Q, M, DB |
| Digital output | out | Byte, Char, USInt | Q, M, DB |  |
| **Integer with sign (16 bits)** | Analog input | in | Int | I, Q, M, DB |
| Analog output | out | Int | Q, M, DB |  |
| **Counter (16 bits)** | Counter input <sup>1)</sup> | in | Word, UInt | I, Q, M, DB |
| **Integer with sign (32 bits)** | Analog input | in | DInt | Q, M, DB |
| Analog output | out | DInt | Q, M, DB |  |
| **Counter (32 bits)** | Counter input <sup>1)</sup> | in | UDInt, DWord | I, Q, M, DB |
| **Floating-point number with sign (32 bits)** | Analog input | in | Real | Q, M, DB |
| Analog output | out | Real | Q, M, DB |  |
| **Floating-point number with sign (64 bits)** | Analog input | out | LReal | Q, M, DB |
| Analog output | out | LReal | Q, M, DB |  |
| **Data block (** **1 .. 64** **bytes)** | Data | in / out | ARRAY <sup>2)</sup> | DB |
| Data | in / out | ARRAY <sup>2)</sup> | DB |  |
| <sup>1)</sup> Note the following section "Counter inputs".   <sup>2)</sup> For the possible formats, see the section "ARRAY" below. |  |  |  |  |

**Counter inputs**

The S7 data types for the data point types "Counter input" support incremental (counting up) as well as decremental counters (counting down).

The counter inputs of the telecontrol server (TCSB), however, only count incrementally. When a counter input in TCSB is supplied with a decremental counter, TCSB assigns this variable the OPC quality code "UNCERTAIN".

**ARRAY**

With the ARRAY data type, contiguous memory areas up to a size of 64 bytes can be transferred. The following S7 data types are compatible components of ARRAY:

- Byte, USInt (total of up to 64 per block of data)
- Char (total of up to 64 per block of data)

  CP-1200 as of firmware version V2.1.77
- Int, UInt, Word (total of up to 32 per block of data)
- DInt, UDInt, DWord (total of up to 16 per block of data)
- Real (total of up to 16 per block of data) *****
- LReal (total of up to 8 per block of data) *****

***** CP-1200 as of V3.2, CP 1542SP‑1 IRC as of V2.1

If the array is modified later, the data point must be recreated.

**Time stamp in UTC format**

Time stamps are output by the OPC server applications in UTC format (48 bits) and contain milliseconds.

##### Data point types of the "ST7" protocol

The direction of the data transmission can be seen in the "Object" column:

- Objects sending into the WAN (to the partner) have the suffix "_S".
- Objects receiving from the WAN (from the partner) have the suffix "_R".

Supported data point types and compatible S7 data types

| Format (memory requirements) | Data point type | S7 data type | Operand area | Data points (channels) per object | Object |
| --- | --- | --- | --- | --- | --- |
| **Bit** | Digital input | Bool | I, Q, M, DB | 1 .. 8 | Bin08X_S |
| Digital output | Bool | Q, M, DB | 1 .. 8 | Bin08X_R |  |
| **Byte** | Digital input | Byte, USInt <sup>3)</sup> | I, Q, M, DB | 4 | Bin04B_S |
| Digital output | Byte, USInt <sup>3)</sup> | Q, M, DB | 4 | Bin04B_R |  |
| Command output | Byte, USInt <sup>3)</sup> | Q, M, DB | 1 | Cmd01B_R |  |
| Command input | Byte, USInt <sup>3)</sup> | Q, M, DB | 1 | Cmd01B_S |  |
| **Integer with sign (16 bits)** | Analog input | Int | I, Q, M, DB | 4 | Ana04W_S |
| Mean value input | Int | I, Q, M, DB | 4 | Mean04W_S |  |
| Analog output | Int | Q, M, DB | 4 | Ana04W_R |  |
| Mean value output | Int | Q, M, DB | 4 | Mean04W_R |  |
| Setpoint output <sup>1)</sup> | Int, UInt, Word | Q, M, DB | 1 | Set01W_R |  |
| Setpoint input <sup>1)</sup> | Int, UInt, Word | Q, M, DB | 1 | Set01W_S |  |
| **Counter (16 bits)** | Counter input | UInt, Word <sup>3)</sup> | I, Q, M, DB | 1 | Cnt01D_S |
| Counter input | UInt, Word <sup>3)</sup> | I, Q, M, DB | 4 | Cnt04D_S |  |
| Counter output | UDInt, DWord <sup>3)</sup> | I, Q, M, DB | 1 | Cnt01D_R |  |
| Counter output | UDInt, DWord <sup>3)</sup> | I, Q, M, DB | 4 | Cnt04D_R |  |
| **Floating-point number (32 bits)** | Analog input | Real <sup>3)</sup> | M, DB | 4 | Ana04R_S |
| Analog output | Real <sup>3)</sup> | M, DB | 4 | Ana04R_R |  |
| **Data block (** **4 .. 48** **bytes)** | Data input | ARRAY [0...11] of DInt / UDInt / DWord / Real <sup>2)</sup><sup>3)</sup> | DB | 12 | Dat12D_S |
| Data output | DB | 12 | Dat12D_R |  |  |
| Parameter output <sup>1)</sup> | DB | 12 | Par12D_R |  |  |
| Parameter input <sup>1)</sup> | DB | 12 | Par12D_S |  |  |
| **Data block (** **1 .. 12** **bytes)** | Data input | Byte, USInt, Word; Int, UInt; DWord, DInt; UDInt; DWord <sup>3)</sup> | I, Q, M, DB | 1 .. 12 | Dat12X1_S |
| Data output | I, Q, M, DB | 1 .. 12 | Dat12X1_R |  |  |
| Parameter input | I, Q, M, DB | 1 .. 12 | Par12X1_S |  |  |
| Parameter output | I, Q, M, DB | 1 .. 12 | Par12X1_R |  |  |
| <sup>1)</sup> See below, section "1: Mirroring back”   <sup>2)</sup> See below, section "2: Data block via array"   <sup>3)</sup> USINT, UInt, Real and UDInt are not supported by S7‑300/400. |  |  |  |  |  |

**1: Mirroring**
 **(TIM 3V‑IE / TIM 4R‑IE)**

Mirroring of the current local data to the partner can be configured for the following data point types:

- Setpoint input/output (Set01W_R / Set01W_S)
- Parameter input/output (Par12D_R / Par12D_S)

If the "Setpoint input mode of the partner" option is enabled, the local values are monitored for changes and transferred to the partner when the value changes.

You configure the function via the parameters of the "Local setpoint input" tab; see section ["Local setpoint input" tab](#local-setpoint-input-tab).

**2: Data block via array**

With the ARRAY data type, blocks of data from contiguous memory areas up to a size of 4 .. 48  bytes can be transferred.

Compatible components of ARRAY are DInt, UDint, DWord or Real. The components within an array must be of the same type.

**Format of the time stamp**

For information on the format of the time stamp, refer to the manual of the module.

##### Data point types of the "DNP3" protocol

Supported data point types, DNP3 object groups, variants and compatible S7 data types

| Format (memory requirements) | Data point type | DNP3 object group   **[variations]** | Direction | S7 data types |  | Operand area |
| --- | --- | --- | --- | --- | --- | --- |
| CP | TIM |  |  |  |  |  |
| **Bit** | Binary Input | **1** [1, 2] | in | Bool | Bool | I, Q, M, DB |
| Binary Input Event | **2** [1, 2] | in | Bool | Bool | I, Q, M, DB |  |
| Double-bit Binary Input | **3** [1] | in | Bool | Bool | I, Q, M, DB |  |
| Double-bit Binary Input Event | **4** [1] | in | Bool | Bool | I, Q, M, DB |  |
| Binary Output  <sup>1)</sup> | **10** [2] | out | Bool | Bool | Q, M, DB |  |
| Binary Output Event  <sup>1)</sup> | **11** [1, 2] | out | Bool | Bool | Q, M, DB |  |
| Binary Command | **12** [1] | out | Bool | Bool | Q, M, DB |  |
| **Integer (16 bits)** | Counter | **20** [2] | in | UInt, Word | Word | I, Q, M, DB |
| Frozen Counter  <sup>2)</sup> | **21** [2, 6] | in | UInt, Word | Word | I, Q, M, DB |  |
| Counter Event | **22** [2, 6] | in | UInt, Word | Word | I, Q, M, DB |  |
| Frozen Counter Event  <sup>3)</sup> | **23** [2, 6] | in | UInt, Word | Word | I, Q, M, DB |  |
| Analog Input | **30** [2] | in | Int | Int | I, Q, M, DB |  |
| Analog Input Event | **32** [2] | in | Int | Int | I, Q, M, DB |  |
| Analog Output Status  <sup>4)</sup> | **40** [2] | out | Int | Int | Q, M, DB |  |
| Analog Output | **41** [2] | out | Int | Int | Q, M, DB |  |
| Analog Output Event  <sup>4)</sup> | **42** [2, 4] | out | Int | Int | Q, M, DB |  |
| **Integer (32 bits)** | Counter | **20** [1] | in | DWord | DWord | I, Q, M, DB |
| Frozen Counter  <sup>2)</sup> | **21** [1, 5] | in | DWord | DWord | I, Q, M, DB |  |
| Counter Event | **22** [1, 5] | in | DWord | DWord | I, Q, M, DB |  |
| Frozen Counter Event  <sup>3)</sup> | **23** [1, 5] | in | DWord | DWord | I, Q, M, DB |  |
| Analog Input | **30** [1] | in | DInt | ‑ | Q, M, DB |  |
| Analog Input Event | **32** [1] | in | DInt | ‑ | Q, M, DB |  |
| Analog Output Status  <sup>4)</sup> | **40** [1, 3] | out | DInt | DWord | Q, M, DB |  |
| Analog Output | **41** [1] | out | DInt | DWord | Q, M, DB |  |
| Analog Output Event  <sup>4)</sup> | **42** [1] | out | DInt | DWord | Q, M, DB |  |
| **Floating-point number (32 bits)** | Analog Input | **30** [5] | in | Real | ‑ | Q, M, DB |
| Analog Input Event | **32** [5, 7] | in | Real | ‑ | Q, M, DB |  |
| Analog Output Status  <sup>4)</sup> | **40** [3] | out | Real | ‑ | Q, M, DB |  |
| Analog Output | **41** [3] | out | Real | ‑ | Q, M, DB |  |
| Analog Output Event  <sup>4)</sup> | **42** [5, 7] | out | Real | ‑ | Q, M, DB |  |
| **Floating-point number (64 bits)** | Analog Input | **30** [6] | in | LReal | ‑ | Q, M, DB |
| Analog Input Event | **32** [6, 8] | in | LReal | ‑ | Q, M, DB |  |
| Analog Output | **41** [4] | out | LReal | ‑ | Q, M, DB |  |
| Analog Output Event  <sup>4)</sup> | **42** [6, 8] | out | LReal | ‑ | Q, M, DB |  |
| **Data block (1...64 bytes)**  <sup>5)</sup> | Octet String | **110** [ ‑ ] | in, out | <sup>5)</sup> | <sup>5)</sup> | DB |
| Octet String Event  <sup>5)</sup> | **111** [ ‑ ] | in, out | <sup>5)</sup> | <sup>5)</sup> | DB |  |
| <sup>1)</sup> This object group can be configured in the Data point editor of STEP 7 using the substitute object group 12.   <sup>2)</sup> This object group can be configured in the Data point editor of STEP 7 using the substitute object group 20.   <sup>3)</sup> This object group can be configured in the Data point editor of STEP 7 using the substitute object group 22.   <sup>4)</sup> This object group can be configured in the Data point editor of STEP 7 using the substitute object group 41.   <sup>5)</sup> With these data point types, contiguous memory areas up to a size of 64 bytes can be transferred. All S7 data types with a size between 1 and 64 bytes are compatible. |  |  |  |  |  |  |

**Explanation of the table footnotes** 
<sup>1)</sup>
**,** 
<sup>2)</sup>
**,** 
<sup>3)</sup>
**,** 
<sup>4)</sup>
**: Configuring data points using substitute object groups**

The initial data point types of the following object groups can be configured using the substitute object groups listed above:

- 10 [2]
- 11 [1, 2]
- 21 [1, 2, 5, 6]
- 23 [1, 2, 5, 6]
- 40 [1, 2, 3]
- 42 [1, 2, 4, 5, 6, 7, 8]

To configure the DNP3 CP, use the specified substitute object group.

Assign each data point on the master using the configurable data point index in STEP 7. The data point of the DNP3 CP is then assigned to the corresponding data point on the master.

Example of configuring the data point Binary Output (10  [2])  
The data point is configured as follows:  
On the DNP3 CP as Binary Command (12  [1])  
On the master as Binary Output (10  [2])

With the data point types Binary Output Event (11) and Analog Output Event (42), you also need to enable mirroring.

**Configuration of the mirroring for output events (object groups 11 and 42)**

You first create the data point types Binary Output Event (object group 11) and Analog Output Event (object group 42) as described above as data points of the object groups 12 or 41.

The local values of these two object groups can be monitored for change and the changes transferred to the master. A change to a local value can be caused by manual operator input on site, for example.

To allow the value resulting from local events or interventions to be transferred to the master, the data point in question requires a channel for mirroring back. You configure this mirroring back function is configured using the "Value monitoring" option in data point configuration, General tab.

Remember that to use the mirror back function, you need to interconnect the local values in the controller with the relevant PLC tag of the data point.

**Time stamp of the data with the DNP3 protocol in UTC format**

Time stamps are transferred in UTC format (48 bits) and contain milliseconds.

##### Data point types of the "IEC 60870‑5" protocol

Supported data point types, IEC types and compatible S7 data types

| Format (memory requirements) | Data point type | IEC type | Direction | S7 data types | Operand area |
| --- | --- | --- | --- | --- | --- |
| **Bit** | Single-point information | &lt;1&gt; | in | Bool | I, Q, M, DB |
| Single-point information with time tag CP56Time2a <sup>1)</sup> | &lt;30&gt; | in | Bool | I, Q, M, DB |  |
| Single command <sup>4)</sup> | &lt;45&gt; | out | Bool | Q, M, DB |  |
| Single command with time tag CP56Time2a <sup>1)</sup> | &lt;58&gt; | out | Bool | Q, M, DB |  |
| Double command with time tag CP56Time2a <sup>1)</sup> | &lt;59&gt; | out | Bool | DB <sup>2)</sup> |  |
| **Byte** | Step position information | &lt;5&gt; | in | Byte, USInt | I, Q, M, DB |
| Step position information with time tag CP56Time2a <sup>1)</sup> | &lt;32&gt; | in | Byte, USInt | I, Q, M, DB |  |
| Regulating step command with time tag CP56Time2a <sup>1)</sup> | &lt;60&gt; | out | Byte, USInt | DB <sup>2)</sup> |  |
| **Integer (16 bits)** | Measured value, normalized value | &lt;9&gt; | in | Int | I, Q, M, DB |
| Measured value, normalized value with time tag CP56Time2a <sup>1)</sup> | &lt;34&gt; | in | Int | I, Q, M, DB |  |
| Measured value, scaled value | &lt;11&gt; | in | Int | I, Q, M, DB |  |
| Measured value, scaled value with time tag CP56Time2a <sup>1)</sup> | &lt;35&gt; | in | Int | I, Q, M, DB |  |
| Set point command, normalized value | &lt;48&gt; | out | Int | Q, M, DB |  |
| Set point command, scaled value | &lt;49&gt; | out | Int | Q, M, DB |  |
| Set point command, normalized value with time tag CP56Time2a <sup>1)</sup> | &lt;61&gt; | out | Int | Q, M, DB |  |
| Set point command, scaled value with time tag CP56Time2a <sup>1)</sup> | &lt;62&gt; | out | Int | Q, M, DB |  |
| **Integer (32 bits)** | Bitstring of 32 bits | &lt;7&gt; | in | UDInt, DWord | I, Q, M, DB |
| Bitstring of 32 bits with time tag CP56Time2a <sup>1)</sup> | &lt;33&gt; | in | UDInt, DWord | I, Q, M, DB |  |
| Integrated totals | &lt;15&gt; | in | UDInt, DWord | I, Q, M, DB |  |
| Integrated totals with time tag CP56Time2a <sup>1)</sup> | &lt;37&gt; | in | UDInt, DWord | I, Q, M, DB |  |
| Bitstring of 32 bits | &lt;51&gt; | out | UDInt, DWord | Q, M, DB |  |
| Bitstring of 32 bits with time tag CP56Time2a ‑ control direction <sup>1)</sup> | &lt;64&gt; | out | UDInt, DWord | Q, M, DB |  |
| **Floating-point number (32 bits)** | Measured value, short floating point number | &lt;13&gt; | in | Real | Q, M, DB |
| Measured value, short floating point number with time tag CP56Time2a <sup>1)</sup> | &lt;36&gt; | in | Real | Q, M, DB |  |
| Set point command, short floating point number | &lt;50&gt; | out | Real | Q, M, DB |  |
| Set point command, short floating point with time tag CP56Time2a <sup>1)</sup> | &lt;63&gt; | out | Real | Q, M, DB |  |
| **Data block**  **(1...2 Bit)**  <sup>2)</sup> | Double-point information | &lt;3&gt; | in | <sup>2)</sup> | DB |
| Double-point information with time tag CP56Time2a <sup>1)</sup> | &lt;31&gt; | in | <sup>2)</sup> | DB |  |
| Double command | &lt;46&gt; | out | <sup>2)</sup> | DB |  |
| Regulating step command | &lt;47&gt; | out | <sup>2)</sup> | DB |  |
| Double command with time tag CP56Time2a <sup>1)</sup> | &lt;59&gt; | out | <sup>2)</sup> | DB |  |
| Regulating step command with time tag CP56Time2a <sup>1)</sup> | &lt;60&gt; | out | <sup>2)</sup> | DB |  |
| **Data block**  **(1...32 Bit)**  <sup>3)</sup> | Bitstring of 32 bits <sup>3)</sup> | &lt;7&gt; | in | <sup>3)</sup> | DB |
| Bitstring of 32 bits with time tag CP56Time2a <sup>1)</sup><sup>3)</sup> | &lt;33&gt; | in | <sup>3)</sup> | DB |  |
| Bitstring of 32 bits <sup>3)</sup> | &lt;51&gt; | out | <sup>3)</sup> | DB |  |
| Bitstring of 32 bits with time tag CP56Time2a ‑ control direction <sup>1)</sup><sup>3)</sup> | &lt;64&gt; | out | <sup>3)</sup> | DB |  |
| <sup>1)</sup> For information on the format of the time stamp, see below.   <sup>2)</sup> For these data point types, create an array of 2 bool in the data block.   <sup>3)</sup> With these data point types, contiguous memory areas of 32 bits can be transferred. Create an Array[0..31] of Bool in the data block.   <sup>4)</sup> Mirroring possible, see below. |  |  |  |  |  |

**Time stamp of the data with the IEC protocol**

Time stamps are transferred according to the IEC specification in the "CP56Time2a" format. Note that only the first 3 bytes for milliseconds and minutes are transferred.

**Mirroring with Single Command**

For the following commands, you can activate mirroring of the current value in the station to the master:

- Single Command &lt;45&gt;

The local value of this data point can be monitored for changes and transferred to the master when changed. A change to a local value can be caused by manual operator input on site, for example.

To allow the value resulting from local events or interventions to be transferred to the master, the data point in question requires a channel for mirroring back. For this, a second data point "Single-point information &lt;1&gt;" is required. Follow the steps below to configure the mirroring function.

Create the data points:

- In the master module

  - Single Command &lt;45&gt;
  - Single-point information &lt;1&gt;

  On the master, you need to write the mirrored value into a variable. Therefore, assign the two data points to different variables in the master module.

  Assign the same index for both data points.
- In the station module

  - Single Command &lt;45&gt;
  - Single-point information &lt;1&gt;

  In the station module, assign the two data points to the same variable.

  Assign the same index for both data points.

The value mirrored by the station is written to the "Single-point information &lt;1&gt;" data point type on the master.

**Time stamp of the data with the IEC protocol**

Time stamps are transferred according to the IEC specification in the "CP56Time2a" format. Note that only the first 3 bytes for milliseconds and minutes are transferred.

#### Process image, type of transmission, event classes

##### Introduction

Some of the functions described below differ depending on the communication module or protocol used.

##### Storage of values

As a rulethe values of all data points are stored in the image memory of the module. Values in the image memory are only transferred after being called up by the master station or the DNP3 / IEC master.

Events are also stored in the send buffer and can be transferred unsolicited.

##### The image memory, the process image of the module

The image memory is the process image of the communications module. All the current values of the configured data points are stored in the image memory. New values of a data point overwrite the last stored value in the image memory.

The values are only transferred under the following conditions.

- After querying the communications partner, refer to "Transfer after call" in the section "Types of transmission".
- Along with a data frame from the send buffer that needs to be transferred immediately.

##### The send buffer

The send buffer of the communications module is the memory for the individual values of data points that are configured as an event (frame memory). You will find the size of the send buffer in the manual of the relevant module.

The capacity of the send buffer is divided up equally for all enabled partners.

If the connection to a communications partner is interrupted, the individual values of the events are retained in the buffer. When the connection returns, the buffered values are sent. The frame memory operates chronologically; in other words, the oldest data is sent first (FIFO principle).

If a data frame was transferred to the communications partner, the transferred data is deleted from the send buffer.

If data cannot be transferred for a longer period of time and the send buffer is threatening to overflow, the protocol-dependent response is as follows:

- Telecontrol Basic, ST7

  The forced image mode

  If the send buffer reaches a certain fill level, the module changes to the forced image mode. The fill level for changing to the forced image mode is:

  - Telecontrol Basic: 80% occupation of the send buffer
  - ST7: 90% occupation of the send buffer

  New values from data points configured as an event are no longer added to the send buffer in forced image mode but rather they overwrite older existing values in the image memory.

  When the connection to the communications partner returns, the module changes back to the send buffer mode as soon as the fill level of the send buffer has fallen below 50%.
- DNP3 / IEC

  If the fill level of the send buffer reaches 100%, no more values are saved until the fill level falls below 100% again.

##### Saving the data point values

As a rule, the values of data points are stored in the image memory of the moodule and transferred only when queried by the communications partner.

Events are also stored in the send buffer and can be transferred unsolicited.

Data points are configured as a static value or as an event using the "Type of transmission" parameter (see below):

- **Static value (no event)**

  Static values are entered in the image memory (process image of the CP).

  Static values correspond to the following classes:

  - DNP3: Class 0
  - IEC: Class 2
- **Event**

  The values of data points configured as an event are also entered in the image memory of the communications module. The value of the event is sent unsolicited to the communications partner if this function is enabled by the master.

  The values of events are also entered in the send buffer of the communications module.

  Events correspond to the following classes:

  - DNP3: Class 1 / 2 / 3
  - IEC: Class 1

##### Types of transmission

The following types of transmission are possible:

- **Transfer after call**
   **(class 0)**

  The current value of the data point is entered in the image memory of the CP. New values of a data point overwrite the last stored value in the image memory.

  After being called by the communications partner, the current value at this time is transferred.
- **Triggered (events)**

  The values of data points configured as an event are entered in the image memory and also in the send buffer of the CP.

  The values of events are saved in the following situations:

  - The configured trigger conditions are fulfilled (data point configuration &gt; "Trigger" tab, see below)
  - The value of a status bit of the status identifiers of the data point changes; see section[Status IDs of the data points](#status-ids-of-the-data-points).

    Example:  
    When the value of a data point configured as an event is updated during startup of the station by reading the CPU data for the first time, the status "RESTART" of this data point changes (bit status change 1 → 0). This leads to generation of an event.

  The configurable event classes of the various protocols are described in the following sections.

##### Event classes with the "Triggered" type of transmission

Depending on the protocol used, the following event classes are available:

- **TeleControl Basic / ST7**

  - **Every value triggered**

    Each value change is entered in the send buffer in chronological order.
  - **Current value triggered**

    Only the last, current value is entered in the send buffer. It overwrites the value stored there previously.
- **DNP3**

  The evaluation of the following classification must be handled by the master.

  - **Event class 1**

    Class according to DNP3 protocol: Class 1

    Each value change is entered in the send buffer in chronological order.
  - **Event class 2**

    Class according to DNP3 protocol: Class 2

    Each value change is entered in the send buffer in chronological order.
  - **Event class 3**

    Class according to DNP3 protocol: Class 3

    Only the current value at the time the trigger condition was met is entered in the send buffer and overwrites the last value stored there.
- **IEC**

  Both of the following event classes correspond to the user data class 1 of the IEC protocol

  - **Every value triggered**

    Each value change is entered in the send buffer in chronological order.
  - **Current value triggered**

    Only the current value at the time the trigger condition was met is entered in the send buffer and overwrites the last value stored there.

Various trigger types are available for starting event-driven transfer, see section ["Trigger“ tab](#trigger-tab).

#### ST7 data points

##### Objects of TD7 software

The telecontrol communication of modules that use the SINAUT ST7 telecontrol protocol is handled by the TD7 software.

The data to be transferred from the SINAUT objects is alternatively configured or parameterized:

- Via data points (TD7onTIM)
- Via the program blocks of the "Telecontrol ST7" library (TD7onCPU)

For information on the two variants of the TD7 software, refer to the section [The TD7 software](#the-td7-software).

##### Data objects

The sending and receiving of process data is configured with the aid of standardized data objects. According to the two transmission directions, these are divided into:

- **Send objects**
   **(.._S)**

  Data objects for acquiring and sending data

  Their names have the ending "_S" (send).
- **Receive objects**
   **(.._R)**

  The data objects for receiving and outputting data

  Their names have the ending "_R" (receive).

The names of the data objects are identical in TD7onTIM and TD7onCPU. In terms of functionality, they are compatible with each other.

##### Object numbers

Each data object has an object number. When new data points are created, the numbers are assigned in ascending order by default. The numbers can be changed.

Rules:

- The object numbers of a module must be unique.
- The lowest object number is 1.

##### Object channels

Each data object has one or more object channels, see section [Datapoint types](#datapoint-types).

The send and receive channels of the data objects are responsible for the processing of an individual process value, for example for processing and sending an analog value or receiving and outputting a command byte.

Each data object contains one or more send or receive channels. The number and type of send and receive channels per data object cannot be modified. The data object "Ana04W_S", for example, has 4 send channels of the type "send analog value".

If objects have multiple channels of the same type, not all channels need to be activated if they are not required.

Rules:

- All channels of an object must have the same data point type.
- The channel numbers of an object must begin with 1 and be assigned consecutively without a gap.
- All channels of an object must have the same partner.

#### DNP3 and IEC data points

##### General

You will also the most important parameters in the first tab of the data point editor in the data point table.

- **Data source**

  - Name: Unique name of the data point
  - For the assignment of the PLC tabs, see section [Configuring data points and messages](#configuring-data-points-and-messages).
  - For the data point type, see section [Datapoint types](#datapoint-types).
  - For the data point index, see section [Data point index](#data-point-index).
- **Master function**

  - Option enabled: The values of the data point are sent as for a master:

    **‑** Input data points are received.

    **‑** Output data points are sent.
  - Option disabled: The data point can be used for 'direct communication' between stations:

    **‑** Input data points can be received and sent.

    **‑** Output data points can be sent and received.
- **Value monitoring**

  Only for DNP3 commands and outputs

  When this option is activated, the current value of the data point, which can be set by the master, is mirrored back from the station to the master. Furthermore, the trigger options of the data point can be enabled to configure the triggering of the transmission.
- **Type of transmission**

  For the type of transmission, see section [Process image, type of transmission, event classes](#process-image-type-of-transmission-event-classes).
- **Read cycle**

  Only for inputs

  For the read cycle see section [Read cycle](#read-cycle).
- **Response to general request**

  Enables the data point for the response to a general request. If the function is disabled, the value of the data point is not sent to the communications partner following a general request.
- **Assignment to group request**

  Only IEC data points

  Assigns the data point to a group request.

  For group queries of the master to the respective group, the value of the data point is sent to the master.

#### Status IDs of the data points

##### Status identifiers

The status identifiers of the data points listed in the following tables are transferred along with the value in each data frame to the communications partner. They can be evaluated by the communications partner.

The CP 1243-8 IRC does not supply any status identifiers. The ST7 protocol does not support status identifiers.

The status identifiers differ depending on the protocol used.

The entries in the table row "Significance" relate to the entry in the table row "Bit status".

##### TeleControl Basic

Depending on their status, the status bits (see table) are converted to the OPC quality code by TCSB.

- Quality = BAD

  Bit 2 or 7 = 1
- Quality = UNCERTAIN

  Bit 1 or 3 or 5 = 1
- Quality = GOOD

  Bits 1 and 2 and 3 and 5 and 6 = 0

Bit assignment of status byte 0

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | ‑ | NON_  EXISTENT | Substituted | LOCAL_ FORCED | CARRY | OVER_ RANGE | RESTART | ONLINE |
| **Meaning** | ‑ | Data point does not exist or S7 address unreachable | Substitute value | Local operator control | Counted value overflow before reading the value | Limit value of the analog preprocessing overshot / undershot | Value not yet updated after start | Value is valid |
| **Bit status** | (always 0) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

##### DNP3

The status IDs correspond to the following elements of the specification:

OBJECT FLAGS ‑ DNP3 Specification, Volume 6, Data Object Library - Part 1

Bit assignment of status byte for the different data point types: Group (variations)

Binary inputs 1 (2); 2 (1, 2)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | STATE | ‑ | CHATTER_ FILTER | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | Placeholder for the binary value | ‑ | Filter set, event suppression | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | 1 | (always 0) | 1 | 1 | 1 | 1 | 1 | 1 |

Double bit Binary inputs 3 (2); 4 (1, 2)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | STATE |  | CHATTER_ FILTER | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | Placeholder for the binary value |  | Filter set, event suppression | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | 1 |  | 1 | 1 | 1 | 1 | 1 | 1 |

Binary outputs 10 (2); 11 (1, 2)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | STATE | ‑ | ‑ | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | Placeholder for the binary value | ‑ | ‑ | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | 1 | (always 0) | (always 0) | 1 | 1 | 1 | 1 | 1 |

Counters 20 (1, 2); 21 / 22 / 23 (1, 2, 5, 6)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | ‑ | DISCONTI NUITY | ROLLOVER | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | ‑ | Count value overflow before value is read | ‑ obsolete ‑ | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | (always 0) | 1 | 0/1 | 1 | 1 | 1 | 1 | 1 |

Counters 20 (1, 2); 21 / 22 / 23 (1, 2, 5, 6)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | ‑ | DISCONTI NUITY | ROLLOVER | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | ‑ | Count value overflow before value is read | ‑ obsolete ‑ | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | (always 0) | 1 | 0/1 | 1 | 1 | 1 | 1 | 1 |

Analog values 30 (1, 2, 5, 6); 32 (1, 2, 5, 6, 3, 4, 7, 8); 40 (1, 2, 3, 4); 42 (1, 2, 5, 6, 3, 4, 7, 8)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | ‑ | REFERENCE_ ERR | OVER_ RANGE | LOCAL_ FORCED | REMOTE_ FORCED | COMM_ LOST | RESTART | ONLINE |
| **Meaning** | ‑ | Inaccurate analog value | Limit value of the analog preprocessing overshot / undershot | Local operator control | Remote overwriting of local value | Communication error TIM CPU | Value not yet updated after start | Value is valid |
| **Bit status** | (always 0) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

##### IEC 60870-5

The status IDs correspond to the following elements of the specification:

Quality descriptor ‑ IEC 60870 Part 5-101

Bit assignment of status byte for the different objects: Data point type &lt;IEC type&gt;

Information object &lt;1, 30&gt;

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | IV invalid | NT not topical | SB substituted | BL blocked | ‑ | ‑ | ‑ | SPI |
| **Meaning** | Value is valid | Value not updated | Substitute value | Value blocked | ‑ | ‑ | ‑ | ‑ |
| **Bit status** | 0 | 1 | 1 | 1 | (always 0) | (always 0) | (always 0) | (always 0) |

Double-point information object &lt;3, 31&gt;

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | IV invalid | NT not topical | SB substituted | BL blocked | ‑ | ‑ | DPI |  |
| **Meaning** | Value is valid | Value not updated | Substitute value | Value blocked | ‑ | ‑ | ‑ |  |
| **Bit status** | 0 | 1 | 1 | 1 | (always 0) | (always 0) | (always 0) |  |

Step position &lt;5, 32&gt;, Bitstring &lt;7, 33&gt;, Analog input &lt;9, 11, 13, 34, 35, 36&gt;

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | IV invalid | NT not topical | SB substituted | BL blocked | ‑ | ‑ | ‑ | OV overflow |
| **Meaning** | Value is valid | Value not updated | Substitute value | Value blocked | ‑ | ‑ | ‑ | Value range exceeded, analog value |
| **Bit status** | 0 | 1 | 1 | 1 | (always 0) | (always 0) | (always 0) | 1 |

Counter (Integrated totals) &lt;15, 37&gt;

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Flag name** | IV invalid | CA counter adjusted | CY carry | SB substituted | SQ sequence number |  |  |  |
| **Meaning** | Value is valid | Count value corrected | Count value overflow before value is read | Substitute value |  |  |  |  |
| **Bit status** | 0 | 1 | 1 | 1 |  |  |  |  |

#### Data point index

##### Configuration of the data point index

Below you will find the protocol-dependent configuration rules for the data point index. The data point index is required to address the data point.

No data point index is configured for the ST7 protocol.

On the program side, the indices are in ascending order by default when the data points are created. You can configure the indices according to your requirements and the following protocol-specific rules.

##### TeleControl Basic

Within a CP, the indexes of the data point classes must comply with the following rules:

- Input

  The index of a data point of the type input must be unique over all data point types (e.g. all digital inputs or all analog inputs, etc.).
- Output

  - A data point of the type output can have the same index as a data point of the type input.
  - Several data points of the type output can have the same index.

> **Note**
>
> **Data points for the inter-station communication with a CP in another S7 station**
>
> Note that for inter-station communication, the indexes of the two corresponding data points (data point pair) must be identical for the sending and receiving CP.

##### DNP3

- In a module, data point indexes must be unique within each of the following object groups:

  - Binary Input / Binary Input Event
  - Binary Output / Binary Command
  - Counter / Counter Event
  - Analog Input / Analog Input Event
  - Analog Output
  - Octet String / Octet String Event
- Indexes of two data points in different object groups can be identical.
- The indexes of two data points can be identical if the two data points are configured for different partners.
- The corresponding partner indexes must be identical at the send and receive ends.

##### IEC 60870-5

The index of a data point is the Information object address.

**Rules**

- The indexes per communication partner must be unique in a module.

  Data point indices assigned twice are indicated as errors in the consistency check and prevent the project being compiled.
- The indices of two data points can be identical if the two data points are configured for different partners.
- The corresponding partner indexes must be identical at the send and receive ends.

**Structured addressing**

The index can be configured in two input fields with different formats:

- Data point index

  The index is configured unstructured here as an integer.

  Range of values: 1..16777215
- Structured index

  You can configure the index structured according to IEC 60870‑5‑3 here. Plant-based structuring of the data points is enabled by structured addressing.

  Three address levels (octets) can be configured.

  Range of values: 0.0.1..255.255.255

The configured values of the two fields are linked. A configured value is converted and displayed in the other input field.

The values are designated as follows for the conversion:

- Data point index

  Designation of the integer value: X
- Structured index

  Designation of the values of the 3rd octet: A.B.C

The configured value is applied to the other field according to the following formula:

X = A * 256 * 256 + B * 256 + C

**Index and "sequential transfer"**

Validity:

- Module: TIM 1531 IRC
- Network node type of the interface for telecontrol communication: Station or node station
- Parameter group: Interface &gt; Advanced options &gt; Settings IEC station &gt; Event settings &gt; Transfer behavior

The joint transfer of event frames in one sequence can be configured for data points without time stamp.

The following requirements must be met:

- The data points are of the same type.
- The indices of the data points are in sequence without gaps.

#### Read cycle

You can control the cyclic reading and writing of PLC or DB tags of the CPU by the communication module by limiting the number of tags to be read and written. You make this setting in the "Communication with the CPU" parameter group.

You can prioritize the cyclic reading of values of input data points from their assigned CPU tags. Less important input data points need not be read in each CPU sampling cycle. On the other hand, you can prioritize the updating of important input data points. You make this setting for each individual data point in the data point configuration in the "General" tab with the "Read cycle" parameter.

##### Options of the "Read cycle" parameter

- Normal cycle

  In the normal cycle, a proportion of the values of the tags are read in each scan cycle.
- Fast cycle

  The fast cycle is suitable for data to be acquired quickly (alarms, contact changeover messages, etc.). The value is read in each cycle.

For S7-1200/1500/ET 200SP, additionally:

- Spontaneous

  The data point is registered for monitoring on the CPU and is no longer requested cyclically by the communication module.

  As soon as the value in the CPU changes, it is actively transferred by the CPU to the communication module.

  This ensures timely transfer of all changed values while limiting the load on the backplane bus.
- No monitoring

  The data point is neither monitored nor requested. The value requested from a master station is always equal to zero.

  The option can be useful for outputs that will not be monitored and do not return mirrored-back values.

##### Structure of the CPU scan cycle

The cycle with which the CP scans the memory area of the CPU is made up of the following phases:

- **Read jobs**

  - **High-priority read jobs**

    **(**
    **Fast cycle**
    **)**

    For all data points with the assignment "Fast cycle", the CPU tags are read in each scan cycle.

    The number of high priority read jobs is not limited.

    As a rule, it is sufficient to assign only data to be acquired quickly, such as alarms and contact changeover messages, to the fast cycle.
  - **Low-priority read jobs - proportion**

    **(**
    **Normal cycle**
    **)**

    For data points with the assignment "Normal cycle", a proportion of the values of their tags is read in each scan cycle.

    At most, as many tags are read in a scan cycle as is configured for "Max. number of read jobs" ("Communication with the CPU"). The values of the other low-priority tags that could not be read in a cycle are read in one of the subsequent cycles.
- **Write jobs**

  The values of a configurable number of spontaneous write jobs are written to the CPU in each cycle. You specify the number of values written per cycle in the "Communication with the CPU" parameter group with the "Max. number of write jobs" parameter. The tags that could not be written in a cycle (tags in excess of the configured maximum number) are written in one of the subsequent cycles.
- **Cycle idle time**

  This waiting time between two scan cycles is used to reserve adequate time for other processes that access the CPU via the backplane bus.

Since a fixed time cannot be configured for the cycle and since a fixed number of objects has not been assigned to the individual phases, the duration of the scan cycle is variable and can change dynamically.

#### "Local setpoint input" tab

##### Setpoints and their mirroring

Using the options described below, you can acquire the locally specified values from setpoint outputs and mirror back the current values to the partner upon change. A change to a local value can be caused by, for example, manual operator input on site.

The functions are available for the following modules:

- TIM 3V‑IE / TIM 3V‑IE Advanced
- TIM 4R‑IE

You can configure the functions for the following data point types:

- Setpoint input (Set01W_S)
- Setpoint output (Set01W_R)
- Parameter input (Par12D_S)
- Parameter output (Par12D_R)

The corresponding input and output data points must be created for both communication partners for the functions. For the mirror function, move the local value in the controller to the relevant PLC tag of the data point.

The parameters for local setpoint input mode and mirroring are optional. If you do not require this, leave it disabled.

##### Parameters

The list shows the functions of the data point types as well as the tabs and parameter groups in which the functions are configured.

- **Setpoint/parameter input**

  "General" &gt; "Data source" tab:

  - Send setpoint to partner

    The setpoint is stored in the PLC tag.

  "Local setpoint input" &gt; "Receive" tab:

  - Receipt of the 'Local input' setpoint input mode sent by the partner object

    The input mode is transferred to the PLC tag "Setpoint input mode" (Bool).
  - Reception of the return value from the partner

    The value mirrored by the partner is transferred to the PLC tag "Mirrored value".
- **Setpoint/parameter output**

  "General" &gt; "Data source" tab:

  - Setpoint received from partner

    The setpoint is transferred to the PLC tag.

  "Local setpoint input" &gt; "Send" tab:

  - Send the 'Local input' local setpoint input mode to the partner object

    The information as to whether the locally assigned setpoint or the setpoint received from the partner is valid is read from the PLC tag "Setpoint input mode".

    **‑** 0: The received setpoint is valid.

    **‑** 1: The locally entered setpoint is valid.
  - Send the locally entered setpoint to the partner

    The setpoint is read from the PLC tag "Local setpoint".

##### Local setpoint input ‑ Reception

The parameter group is active for sending data types (*_S).

The following parameters are available for local setpoints of the partner:

- **Setpoint input mode**

  Via the parameter, the feedback is received from the partner data point about its setpoint input mode.

  The information is stored in the PLC tag (Bool).

  - 0 = Data point of the partner in 'Setpoint receipt' mode.
  - 1 = Data point of the partner in 'local' setpoint input mode.

  The parameter is used only for signaling. This parameter and the corresponding parameter of the partner data point do not cause an interlock for the partner with the local setpoint specification. Interlocking must be implemented by the user program.

  After startup of the CPU or partner CPU, or after the return of the connection, a general request ensures that the current, valid status of the partner is displayed at the parameter.
- **Return value**

  The partner data point that receives the setpoint feeds back the currently valid setpoint if the parameter "Setpoint status" is enabled there. This mirrored back setpoint is displayed here.

  If the partner object is set to 'local' and if new input is made there, the setpoint changed there is displayed here if the Local setpoint parameter is enabled for the partner object.

  After startup of the CPU or partner CPU, or after the return of the connection, a general request ensures that the current, valid setpoint of the partner is displayed at the parameter.

##### Local setpoint input ‑ Sending

The parameter group is enabled for receiving data types (*_R).

The following parameters are available for local setpoints of the own station:

- **Setpoint input mode**

  This input can be used to signal whether the locally specified setpoint or the setpoint sent by the partner is valid.

  The information is stored in the PLC tag (Bool).

  - 0 = The setpoint of the partner is valid.
  - 1 = The locally entered setpoint is valid.

    A setpoint sent by the partner (e.g. the master station) can also be accepted by the object if the parameter is set (True).

  The parameter is used only for information. An interlock with the remote setpoint assignment must be implemented in the user program.
- **Local setpoint**

  If this parameter is enabled, the locally entered setpoint is read from the PLC tag and mirrored back to the send data point of the partner.

#### "Trigger“ tab

##### Trigger

Data points are configured as a static value or as an event using the "Type of transmission" parameter.

Storing an event value in the send buffer (telegram memory) is triggered via various trigger types:

- **Threshold value trigger**

  The value of the data point is saved when this reaches a certain threshold. The threshold is calculated as the difference compared with the last stored value, refer to the section [Threshold value trigger](#threshold-value-trigger).
- **Time trigger**

  The value of the data point is saved at configurable intervals or at a specific time of day.
- **Event trigger (**
  **Trigger tag**
  **)**

  The value of the data point is saved when a configurable trigger signal is fired. The edge change (0 → 1) of a trigger tag set by the user program is evaluated as a trigger signal. When necessary, a separate trigger tag can be configured for each data point.

  **Reset of the trigger tag in the memory bit area / DB:**
    
  If the memory area of the trigger tag is in the bit memory or in a data block, the trigger tag is reset to zero when the value is transferred. This can take up to 500 milliseconds.

> **Note**
>
> **Fast setting of triggers**
>
> Triggers must not be set faster than a minimum interval of 500 milliseconds. This also applies to hardware triggers (input area).

> **Note**
>
> **Hardware trigger**
>
> You need to reset hardware triggers via the user program

**Status trigger / Time stamp trigger**

To use these two triggers, you must create a data point whose tag references the UDT specified below.

- **Status trigger**

  The value of the data point is transferred together with the status of the tag formed in the CPU.

  Valid for the following data point types:

  **DNP3:** 
  **Group (variations)**

  - Binaries: 1 (2); 2 (1, 2); 3 (2); 4 (1, 2)
  - Counters: 20 (1, 2); 22 (1, 2, 5, 6)
  - Analog values: 30 (1, 2, 5, 6); 32 (1, 2, 5, 6, 3, 4, 7, 8)

  **IEC 60870‑5: Data point type &lt;IEC type&gt;**

  - Information objects &lt;1, 3, 5, 30, 31, 32&gt;
  - Measured value &lt;9, 11, 13, 34, 35, 36&gt;
  - Integrated totals &lt;15, 37&gt;
  - Bitstring &lt;7, 33&gt;

  For coding of the status byte, see section [Status IDs of the data points](#status-ids-of-the-data-points).

  ST7 does not support the status.
- **Time stamp trigger**

  The value of the data point is transferred together with the time stamp of the CPU.

  Valid for the following data point types:

  **DNP3:** 
  **Group (variations)**

  - Binaries: 2 (2); 4 (2)
  - Counters: 22 (5, 6)
  - Analog values: 32 (3, 4, 7, 8)

  **IEC 60870‑5: Data point type &lt;IEC type&gt;**

  - Information objects &lt;30, 31, 32&gt;
  - Measured value &lt;34, 35, 36&gt;
  - Integrated totals &lt;37&gt;
  - Bitstring &lt;33&gt;

  **ST7:**

  - Bin04B_S / Bin08X_S / Bin04B_R / Bin08X_R
  - Ana04W_S / Ana04R_S / Ana04W_R / Ana04R_R
  - Mean04W_S / Mean04W_R
  - Cnt01D_S / Cnt04D_S / Cnt01D_R / Cnt04D_R
  - Dat12D_S / Dat12x1D_S / Dat12D_R / Dat12x1D_R

**Structure of the common UDT for the "Value", "Status trigger" and "Time stamp trigger" tags**

The values of "Value", "Status trigger" and "Time stamp trigger" are written together to one user data type (UDT) even if only one of the two triggers is used.

The UDT has the following structure:

- "Value" tag

  The data type must correspond to the data point type whose value will be transferred.

  The supported data point types are listed above.
- "Status" tag

  Data type: Byte
- "Status" tag

  Data type: DTL

**Creating the UDT**

For the three tags you must first create a user data type (UDT). Proceed as follows:

1. Navigate to the "PLC data types" entry of the assigned CPU in the project tree.
2. Click the "Add new data type" entry.
3. Then create the needed tags in the UDT.

   The data type of the "Value" tag must correspond to the data type of the data point to be transferred in each case.

   ![Structure of the UDT - in this example for a measured value with data type "Real"](images/172363374091_DV_resource.Stream@PNG-en-US.png)

   Structure of the UDT - in this example for a measured value with data type "Real"
4. Create a data block in which you insert the previously created UDT.

   The UDT can be selected under the name you assigned.

You must create a separate UDT for each data point you want to transfer with the "Status trigger" and "Time trigger" options.

**Archiving of events**

Validity: TIM 1531 IRC

With the TIM 1531 IRC you can save the values of triggered data points on the SD card of the CPU.

- Enable archiving

  Enables retentive storage of the values of events (send buffer) on the SD card in case of connection faults.

  Requirement for enabling the function:

  - Enabling the parameter "Enable retentive saving" ("Basic settings" parameter group)
  - Disabling of the "Master function" (data point editor &gt; "General" tab)

Archiving is possible for the following types of data points:

- ST7

  - Bin04B_S / Bin08X_S
  - Ana04W_S / Ana04R_S
  - Mean04W_S
  - Cnt01D_S / Cnt04D_S
  - Dat12D_S / Dat12x1D_S
  - Cmd01B_S / Cmd08X_S
  - Set01W_S
  - Par12D_S / Par12x1D_S
- DNP3

  - Binary Input Event (2)
  - Counter Input Event (22)
  - Analog Input Event (32)
  - Octet String Event (111)
- IEC 60870‑5

  - Information objects &lt;1/5/30/32&gt;
  - Measured value &lt;9/11/13/34/35/36&gt;
  - Integrated totals &lt;15/37&gt;
  - Bitstring &lt;7/33&gt;

##### Station state events

Only configurable with: TIM 1531 IRC

The "Master function" option must be disabled.

Supported protocols and data types:

- DNP3

  - Binary Input Event (2)
- IEC 60870‑5

  - Single-point information &lt;1&gt;
  - Single-point information with time tag CP56Time2a &lt;30&gt;

Parameters:

- **Station state event type**

  Select the event at which the station sends frames to the defined partner. The frame is transferred together with the object number.

  - No station state event
  - Status of local CPU changed
  - Status of connection to the local CPU changed
  - Status of connection to the substation changed

    Note: This parameter is not exported with the data point export and can therefore also not be reimported.
  - SD card error
  - Status of redundancy synchronization connection changed

    Only if there is device redundancy of TIM 1531 IRC
- **Substation address**

  When the "Connection status to local CPU changed" option is selected:

  Enter the station address of the substation that the changed connection status relates to.

##### Transmission time

Whether the value of an event is transmitted to the communication partner immediately after activating the trigger or delayed depends on the protocol used and the settings:

- DNP3 / IEC

  The spontaneous transfer in these protocols depends on whether spontaneous sending or asymmetric communication is possible in the network.

  For DNP3 modules, this can be set via the "Unsolicited reporting" parameter in the "Settings DNP3 station" parameter group of the interface or via the "Solicited" parameter in the connection editor.
- TeleControl Basic / ST7

  Here you set the time of transmission with the "Transmission mode" parameter at the data point.

##### Transmission mode

The transmission mode of an ST7 telegram is set in the "Trigger" tag of the data point. With the option, you specify whether data telegrams of events are sent immediately or following a delay:

- Unsolicited (direct transfer)

  The value is transferred immediately.
- Conditional spontaneous (buffered transfer)

  The value is transferred only when one of the following conditions is fulfilled:

  - The communications partner queries the station.
  - The value of another event with the transmission mode "Unsolicited" is transferred.
  - The fill level of the send buffer has reached 80% of its maximum capacity.

#### Threshold value trigger

> **Note**
>
> **Threshold value trigger: Calculation only after "Analog value preprocessing"**
>
> Note that the analog value preprocessing is performed before the check for a configured threshold value and before calculating the threshold value. Smoothing factors and any configured integration interval are taken into account in the calculation.
>
> This affects the value that is configured for the threshold value trigger.

> **Note**
>
> **Threshold value trigger with configured mean value generation**
>
> With enabled mean value generation, the absolute method for the calculation of the threshold value deviation is used for analog values with the threshold value trigger.

For the time sequence of the analog value preprocessing refer to the section [Analog value preprocessing](#analog-value-preprocessing).

##### Threshold value trigger

**Function**

If the process value deviates by the amount of the threshold value, the process value is saved.

Two methods are used to calculate the threshold value deviation:

- **Absolute method**

  With binary and counter values as well as with analog values with configured mean value generation, the absolute method is used to calculate the threshold value deviation.
- **Integrative method**

  With analog values without configured mean value generation, the integrating method is used to calculate the threshold value deviation.

  In the integrating threshold value calculation, it is not the absolute value of the deviation of the process value from the last stored value that is evaluated, but rather the integrated deviation.

**Absolute method**

There is a check for each binary value to determine whether the current (possibly smoothed) value is outside the threshold value band. The current threshold value band results from the last saved value and the amount of the configured threshold value:

- Upper limit of the threshold value band: Last saved value + threshold value
- Lower limit of the threshold value band: Last saved value - threshold value

As soon as the process value reaches the upper or lower limit of the threshold value band, the value is saved. The newly saved value serves as the basis for calculating the new threshold value band.

**Integrative method**

The integration threshold value calculation works with a cyclic comparison of the integrated current value with the last stored value. The calculation cycle in which the two values are compared is 500 milliseconds.  
(Note: The calculation cycle must not be confused with the scan cycle of the CPU memory areas).

The deviations of the current process value are totaled in each calculation cycle. The trigger is set only when the totaled value reaches the configured value of the threshold value trigger and a new process value is entered in the send buffer.

The method is explained based on the following example in which a threshold value of 2.0 is configured.

Example of the integration calculation of a threshold value configured with 2.0

| Time [s]  (calculation cycle) | Process value stored in the send buffer | Current process value | Absolute deviation from the stored value | Integrated deviation |
| --- | --- | --- | --- | --- |
| 0 | **20.0** | **20.0** | 0 | 0 |
| 0.5 |  | 20.3 | +0.3 | 0.3 |
| 1.0 |  | 19.8 | -0.2 | 0.1 |
| 1.5 |  | 20.2 | +0.2 | 0.3 |
| 2.0 |  | 20.5 | +0.5 | 0.8 |
| 2.5 |  | 20.3 | +0.3 | 1.1 |
| 3.0 |  | 20.4 | +0.4 | 1.5 |
| 3.5 | **20.5** | **20.5** | +0.5 | **2.0** |
| 4.0 |  | 20.4 | -0.1 | -0.1 |
| 4.5 |  | 20.1 | -0.4 | -0.5 |
| 5.0 |  | 19.9 | -0.6 | -1.1 |
| 5.5 |  | 20.1 | -0.4 | -1.5 |
| 6.0 | **19.9** | **19.9** | -0.6 | **-2.1** |

With the changes in the process value shown in the example, the threshold value trigger configured with 2.0 fires twice:

- At the time 3.5 s: The value of the integrated deviation is at 2.0. The new process value stored in the send buffer is 20.5.
- At the time 6.0 s: The value of the integrated deviation is at 2.1. The new process value stored in the send buffer is 19.9.

In this example, if a deviation of the process value of approximately 0.5 should fire the trigger, then with the behavior of the process value shown here a threshold value of approximately 1.5 ... 2.5 would need to be configured.

#### Analog value preprocessing

Modules with data point configuration support analog value preprocessing. For analog value data points, some or all of the functions described below can be configured.

**Requirements and restrictions**

You will find the requirements for the configuration of the preprocessing options and restrictions in the section relating to the particular function.

> **Note**
>
> **Restrictions due to configured triggers**
>
> The analog value preprocessing options "Fault suppression time", "Limit value calculation" and "smoothing" are not performed if no threshold value trigger is configured for the relevant data point.. In these cases, the read process value of the data point is entered in the image memory of the CP before the preprocessing cycle of the threshold value calculation (500 ms) elapses.

##### Sequence of the analog value preprocessing options

The values of analog inputs configured as an event are processed on the CPU according to the following scheme:

![Sequence of the analog value preprocessing](images/80642098315_DV_resource.Stream@PNG-en-US.png)

Sequence of the analog value preprocessing

The 500 millisecond cycle is started by the integrative threshold value calculation. In this cycle, the values are saved even when the following preprocessing options are enabled:

- Unipolar transfer
- Fault suppression time
- Limit value calculation
- Smoothing

##### Mean value generation

> **Note**
>
> **Restricted preprocessing options if mean value generation is configured**
>
> If you configure mean value generation for an analog value event, the following preprocessing options are not available:
>
> - Unipolar transfer
> - Fault suppression time
> - Smoothing
> - Threshold value calculation only with the absolute method

**Function**

With this parameter, acquired analog values are transferred as mean values.

For the following protocols, averaging is only supported for integers of type "Int":

- TeleControl Basic
- DNP3
- IEC 60870‑5

If mean value generation is active, it makes sense to configure a time trigger..

The current values of an analog data point are read in a 100 millisecond cycle and totaled. The number of read values per time unit depends on the read cycle of the CPU and the CPU scan cycle of the CP.

The mean value is calculated from the accumulated values as soon as the transfer is triggered by a trigger. Following this, the accumulation starts again so that the next mean value can be calculated.

The mean value is formed even if the transmission of the analog value frame is triggered by a call of the communication partner. The duration of the mean value calculation period is then the time from the last transmission (for example initiated by the trigger) to the time of the call. Once again, the accumulation restarts so that the next mean value can be calculated.

**Input modules: Overflow range / underflow range**

As soon as a value is acquired in the overflow or underflow range, mean value generation is stopped. The value 32767 / 7FFF<sub>h</sub> or ‑32768 / 8000<sub>h</sub> is saved as an invalid mean value for the current mean value calculation period and sent with the next data frame.

The calculation of a new mean value is then started. If the analog value remains in the overflow or underflow range, one of the two values named is again saved as an invalid mean value and sent when the next transfer is triggered.

> **Note**
>
> **Fault suppression time &gt; 0 configured**
>
> If you have configured an error suppression time and then enable mean value generation, the value of the error suppression time is grayed out but no longer used. If mean value generation is enabled, the error suppression time is set to 0 (zero) internally.

##### Unipolar transfer

**Restrictions**

Unipolar transfer cannot be configured at the same time as mean value generation. Enabling unipolar transfer has no effect when mean value generation is activated.

**Function**

With unipolar transfer, negative values are corrected to zero. This can be desirable if values from the underrange should not be transferred as real measured values.

Exception: With process data from input modules, the value -32768 / 8000<sub>h</sub> for wire break of a live zero input is transferred.

With a software input, on the other hand, all values lower than zero are corrected to zero.

##### Fault suppression time

**Requirements for the function**

Configuration of the threshold trigger for this data point

**Restrictions**

The fault suppression time cannot be configured at the same time as mean value generation. A configured value has no effect when mean value generation is activated.

**Function**

A typical use case for this parameter is the suppression of peak current values when starting up powerful motors that would otherwise be signaled to the control center as a disruption.

The transmission of an analog value in the overflow (7FFF<sub>h</sub>) or underflow range (8000<sub>h</sub>) is suppressed for the specified time. The value 7FFF<sub>H</sub> or 8000<sub>H</sub> is only sent after the fault suppression time has elapsed, if it is still pending.

If the value returns to the measuring range before the fault suppression time elapses, the current value is transferred.

**Input modules**

The suppression is adjusted to analog values that are acquired directly by the S7 analog input modules as raw values. These modules return the specified values for the overflow or underflow range for all input ranges (also for live zero inputs).

An analog value in the overflow range (32767 / 7FFF<sub>h</sub>) or underflow range (‑32768 / 8000<sub>h</sub>) is not transferred for the duration of the fault suppression time. This also applies to live zero inputs. The value in the overflow/underflow range is only sent after the fault suppression time has elapsed, if it is still pending.

**Recommendation for finished values that were preprocessed by the CPU:**

If the CPU makes preprocessed finished values available in bit memory or in a data block, suppression is only possible or useful if these finished values also adopt the values listed above 32767 / 7FFF<sub>h</sub> or -32768 / 8000<sub>h</sub> in the overflow or underflow range. If this is not the case, the parameter should not be configured for preprocessed values.

For finished values preprocess in the CPU, the limits for the overflow and underflow can be freely assigned.

##### Integration interval

The integration interval is used for threshold value processing according to the integration principle, see also section [Threshold value trigger](#threshold-value-trigger).

The input value determines the time interval in which the analog value is integrated.

With the setting 0 (zero), the threshold value is calculated without integration. This means lower data volume.

##### Smoothing factor

**Requirements for the function**

Configuration of the threshold trigger for this data point

**Restrictions**

The smoothing factor cannot be configured at the same time as mean value generation. A configured value has no effect when mean value generation is activated.

**Function**

Analog values that fluctuate quickly can be evened out using the smoothing function.

The smoothing factors are calculated according to the following formula as with S7 analog input modules.

![Smoothing factor](images/108956126731_DV_resource.Stream@PNG-de-DE.png)

where  
y<sub>n</sub> = smoothed value in the current cycle n  
y<sub>n-1</sub> = smoothed value in the previous cycle n-1  
x<sub>n</sub> = value acquired in the current cycle n  
k = smoothing factor

The following values can be configured for the module as the smoothing factor.

- 1 = No smoothing
- 4 = Weak smoothing
- 32 = Medium smoothing
- 64 = Strong smoothing

##### Set limit value 'low' / Set limit value 'high'

**Requirements for the function**

- Configuration of the threshold trigger for this data point
- Supported variable types of the CPU

  The analog value data point must alternatively be linked to one of the following variables:

  - PLC tag in the bit memory address area
  - DB variable (variable in data block)

  Limit value configuration is not possible for PLC tags that access hardware modules (input/output operand area).

The configuration of limit values is pointless for measured values that have already been preprocessed on the CPU.

**Function**

In these two input boxes, you can set a limit value in the direction of the start of the measuring range or in the direction of the end of the measuring range. You can also evaluate the limit values, for example as the start or end of the measuring range.

**Recommendation for quickly fluctuating analog values:**

If the analog value fluctuates quickly, it may be useful to smooth the analog value first if limit values are configured.

**Status identifier "OVER_RANGE" / "overflow"**

With protocols that support status identifiers, if the limit value is overshot or undershot, the status identifier of the data point is set for measured range violation indicated below as the identifier "OV". This status identifiers are described in the section [Status IDs of the data points](#status-ids-of-the-data-points).

The "OV" bit of the status identifier of the data point is set as follows when the relevant analog value is transferred:

- Limit value 'high':

  - If the limit value is exceeded: OV = 1
  - If the value then falls below the limit value: OV = 0
- Limit value 'low':

  - If the value falls below the limit value: OV = 1
  - If the value then exceeds the limit value: OV = 0

**Configuration of the limit value**

Depending on the data type, a limit value is configured as an integer decimal number or as a floating-point number.

Value ranges of the limit values

| Data type | Range of values |
| --- | --- |
| Int | -32768 ... 32767 |
| DInt | -2147483648 ... 2147483647 |
| Real | 1.175495E-38 ... 3.402823E+38 |
| LReal | 2.225073E-308 ... 1.797693E+308 |

> **Note**
>
> **Limit value 0 (zero)**
>
> - The entry of the value 0 is interpreted as a disabled limit value for most modules.
>
>   Exceptions:
> - The value 0 can also be used as a limit value for the following modules as of the indicated firmware version:
>
>   - CP 1243‑7 LTE V3.3
>   - CP 1542‑1 IRC V2.2
>   - TIM 1531 IRC V2.2

The following table specifies the ranges of a 32-bit number with regard to the ranges of the raw value of an analog input or output module.

Input/output ranges of analog modules

| Range | Raw value (16-bit) |  | Module signal [mA] |  |  | Measuring range [%] |
| --- | --- | --- | --- | --- | --- | --- |
| Decimal | Hexadecimal | 0 .. 20  (unipolar) | -20 .. +20  (bipolar) | 4 .. 20  (life zero) |  |  |
| Overflow | 32767 | 7FFF | &gt; 23.515 | &gt; 23.515 | &gt; 22.81 | &gt; 117.59 |
| Overrange | 32511 ... 27649 | 7EFF ... 6C01 | 23.515 ... 20.001 | 23.515 ... 20.001 | 22.810 ... 20.001 | 117.593 ... 100.004 |
| Nominal range (unipolar / life zero) | 27648 ... 0 | 6C00 ... 0000 | 20 ... 0 |  | 20 ... 4 | 100 ... 0 |
| Nominal range (bipolar) | 27648 ...  0  ... -27648 | 6C00 ...  0000  ... 9400 |  | 20 ...  0  ... -20 |  | 100 ...  0  ... -100 |
| Underrange (unipolar / life zero) | -1 ... -4864 | FFFF ... ED00 | -0.001 ... -3.518 |  | 3.999 ... 1.185 | -0.004 ... -17.59 |
| Underrange (bipolar) | -27649 ... -32512 | 93FF ... 8100 |  | -20.001 ... -23.516 |  | -100.004 ... -117.593 |
| Undershoot / wire break | -32768 | 8000 | &lt; -3.518 |  | &lt; 1.185 | &lt; -17.59 |

***** The value ranges (underflow / overflow) in PLC tags with different data types are as follows:

- Int

  - -32768
  - 32767
- DInt

  - -2147483648
  - 2147483647
- Real

  - -3.4000E+038
  - 3.4000E+038
- LReal

  - -1.7000E+308
  - 1.7000E+308

> **Note**
>
> **Evaluation of the value even when the option is disabled**
>
> If you enable one or both options and configure a value and then disable the option later, the grayed out value is nevertheless evaluated.
>
> To disable the two options, delete the previously configured limit values from the input boxes and then disable the relevant option.

#### Command options

##### "Command functions": Processing options of commands

**Parameters**

The following functions can be alternatively enabled for command data points.

- **LATCH_ON/OFF**

  The function permanently latches a command output to the value 0 or 1.

  **Note:**
    
  The latched value is only canceled by a new command. Alternatively, the command can be reset by the user program.
- **PULSE_ON/OFF**

  The function evaluates the number and length of the signals (pulses) of commands from a master station.

**Data point types**

The functions can be configured for the following data point types:

- ST7

  Command output (Cmd01B_R)
- IEC

  Single command &lt;45, 58&gt;
- DNP3

  Binary Command (12)

**Reference to specifications**

The output options correspond to the following parts of the specification:

- IEC

  Qualifier of command ‑ IEC 60870-5-101, Part 1
- DNP3

  Control Code, Operation Type field (OP Type) ‑ Volume 6, Part 2, Objects

##### Protocol-specific implementation of the processing options

**ST7**

- LATCH_ON/OFF

  The function latches the value of a command as described above.
- PULSE_ON/OFF

  The function evaluates the "command output time" for a single pulse (see below).

**IEC**

- LATCH_ON/OFF

  The function latches the value of a command as described above.
- PULSE_ON/OFF

  The function is coded by the master via a "Qualifier of command". The following codes are evaluated by the communication module in the station:

  - QU (Type 1.1) &lt;0&gt; no additional definition

    Corresponding parameter for the module: "Pulse control"
  - QU (Type 1.1) &lt;1&gt; short pulse duration

    Corresponding parameter for the module: "Short pulse duration"
  - QU (Type 1.1) &lt;2&gt; long pulse duration

    Corresponding parameter for the module: "Long pulse duration"
  - S/E (Type 6) &lt;0&gt; execute

    Corresponding parameter for the module: "Command execution mode"
  - S/E (Type 6) &lt;1&gt; select

    Corresponding parameter for the module: "Command execution mode"

**DNP3**

The two functions are encoded by the master via the Control Code of the object.

- LATCH_ON/OFF

  The function permanently latches a command output to the value 0 or 1.

  The station processes the command according to the Complementary Latch Model.
- PULSE_ON/OFF

  The function evaluates the "PULSE_ON" Control Code in command frames of a master.

  The master sends the information "Trip-Close Count", "On-time", "Off-time" and "Pulse count" with the command frame to the station.

  The station data point evaluates the information and checks it for consistency with the parameters "Max. pulse duration", "Pulse duration replacement time" and "Max. number of pulses".

  The TIM 1531 IRC processes the command according to the Activation Model.

The "Clear" field (CR) is not supported.

The station data point evaluates the coding of the control code as follows.

Decoding of the DNP3 control code by the command data point of the station

| Received control code |  |  | Reaction of the station data point |  |
| --- | --- | --- | --- | --- |
| Control Code | Trip-Close Code | Operation Type Field | Option enabled:  PULSE_ON | Option enabled:  LATCH_ON / OFF |
| 0x01 | NUL | PULSE_ON | The output is set to 1 for the duration of "On-time". | The command is rejected. |
| 0x03 | NUL | LATCH_ON | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 1 for the duration of "On-time". | The output is set to 1. |
| 0x04 | NUL | LATCH_OFF | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 1 for the duration of "On-time". | The output is set to 0. |
| 0x41 | CLOSE | PULSE_ON | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 1 for the duration of "On-time". | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 1. |
| 0x81 | TRIP | PULSE_ON | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 1 for the duration of "On-time". | - CP   The command is rejected. - TIM 1531 IRC   The output is set to 0. |

> **Note**
>
> **Mirroring**
>
> If you want the station data point to mirror the current value back to the master, enable the "Value monitoring" option in the "General" tab of the data point.

##### Parameters of the processing options

| Symbol | Meaning |
| --- | --- |
| Name: | **Control Code** |
| Range of values: | - PULSE_ON - LATCH_ON/OFF |
| Explanation: | Output option of the command output. See above for the meaning. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Pulse control**   (Master only)  - DNP3: Trip-Close Code - IEC: Qualifier of command |
| Range of values: | DNP3:  - NUL - CLOSE - TRIP   IEC:  - No presettings   For additional qualifiers, see the parameters "Short pulse duration / Long pulse duration" below. |
| Explanation: | Trip-Close Code for Control Code "PULSE_ON". The data point sends the configured code to the corresponding data point of the station. See above for the meaning. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Pulse ON duration**   (Master only) |
| Range of values: | 0 ... 4294967295 |
| Default: | 10 |
| Explanation: | Duration (milliseconds) for "On-time". The data point sends the configured time to the corresponding data point of the station. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Pulse OFF duration**   (Master only) |
| Range of values: | 0 ... 4294967295 |
| Default: | 0 |
| Explanation: | Duration (milliseconds) for "Off-time". The data point sends the configured time to the corresponding data point of the station. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Number of pulses**   (DNP3 master only) |
| Range of values: | 1 ... 255 |
| Default: | 1 |
| Explanation: | Number of pulses that the data point sends to the corresponding data point of the station. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Max. number of pulses** |
| Range of values: | - DNP3: 0 ... 255 - ST7 and IEC: Fixed assignment with "1" |
| Default: | 1 |
| Explanation: | Monitors the number of pulses sent by the master (Count). If the number of pulses received from the master exceeds the value configured here, the command is discarded.  If you enter 0 (zero), the monitoring is disabled. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Max. pulse duration**  **(s)**   (DNP3 only) |
| Range of values: | 0 ... 65535 |
| Default: | 0 |
| Explanation: | Monitors the pulse duration transmitted by the master in the command frame (On-time).  If the duration of the pulse received from the master exceeds the value configured here and if no "Pulse duration replacement time" is configured, the command of the master is rejected.  With 0 (zero), the value is not monitored (unlimited pulse duration). |

| Symbol | Meaning |
| --- | --- |
| Name: | **Pulse duration replacement time**  **(s)**   (DNP3 only) |
| Range of values: | 0 ... 65535 |
| Default: | 0 |
| Explanation: | Replacement value for the pulse duration  The replacement value is used if the pulse duration received from the master exceeds the value configured in "Max pulse duration".  The parameter is only used when "Max. pulse duration" &gt; 0 is configured.  If the value is 0 (zero), no replacement value is used. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Short pulse duration**  **(s)**   (IEC only) |
| Range of values: | 0 ... 65535 |
| Default: | 0 |
| Explanation: | Commands from the master with the Qualifier of command (QOC) = &lt;1&gt; (short pulse duration) are output by the communication module for the duration configured here.  With the setting 0 (zero), commands with QOC = &lt;1&gt; are rejected by the module. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Long pulse duration**  **(s)**   (IEC only) |
| Range of values: | 0 ... 65535 |
| Default: | 0 |
| Explanation: | Commands from the master with the Qualifier of command (QOC) = &lt;2&gt; (long pulse duration) are output by the communication module for the duration configured here.  With the setting 0 (zero), commands with QOC = &lt;2&gt; are rejected by the module. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Command output time**  **(s)**   (ST7 only) |
| Range of values: | 0 ... 65535 |
| Default: | 0 |
| Explanation: | Period for which the command is output. The duration is valid for all 8 channels of the SINAUT object.  When the time expires, the output is automatically reset.  With zero, a set command output is not automatically reset. In this case, you need to reset the output via the user program. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Command execution mode**   (DNP3 and IEC only) |
| Range of values: | - Execute directly - Select and operate |
| Default: | Execute directly |
| Explanation: | - Execute directly   The command is immediately transmitted to the CPU of the station for execution. - Select and operate   Procedure:   - Trigger the command in the master module     The "select" frame is sent from the master station to the communication module of the station.   - The station acknowledges receipt.   - The master data point sends the execution frame after receiving the acknowledgment from the station.   - The station only forwards the command to the CPU when it receives the "Execution" frame from the master within the configured "Max. time between Select and Operate".     The station must not receive any other data frame between Select and Operate.Note: "Max. time between Select and Operate" is configured in the transmission settings of the respective interface.   Reference to the specifications:   - DNP3     "Select and Operate" is realized via the function codes 03 and 04.     "Direct Operate" is realized via the function codes 05 and 06.   - IEC (Select and Execute)     The communication module acknowledges receipt of the selection ASDU with the Qualifier "S/E (Type 6) &lt;1&gt; select".     After receiving the acknowledgment, the master sends the execution ASDU with the Qualifier "S/E (Type 6) &lt;1&gt; execute". |

##### Value mirroring

The function is provided for mirroring back the local value of the station to the master station.

For station data points, the "Master function" option ("General" tab) must be enabled.

Validity:

- ST7

  For master station data points and station data points:

  - Parameter input (Par12x1D_S)

  The result is written to the "PLC tag for local value" (Byte, Real) and mirrored back to the master station.
- DNP3

  For master station data points and for station data points with enabled "Master function" option:

  - Binary Command (12)
  - Analog Output (41)

  The result is written to the "PLC tag for local value" (Bool, Real, Int) and mirrored back to the partner.

##### Command result

**Function and validity**

The function is provided for reporting back to the master station whether a command or setpoint from the communication module was received in the station. The execution of the command in the CPU is neither recorded nor evaluated.

Validity: Command and setpoint data points with enabled "Master function" option:

The result is written to the "PLC tag for command result" (Byte) and sent to the corresponding tag of the partner.

- IEC

  - Single / double / regulating step command &lt;45, 46, 47&gt;
  - Single / double / regulating step command with time tag CP56Time2a &lt;58, 59, 60&gt;
  - Set point command, normalized value / scaled value / short floating point value &lt;48, 49, 50&gt;
  - Set point command, normalized value / scaled value / short floating point value   
    with time tag CP56Time 2a &lt;61, 62, 63&gt;
  - Bitstring of 32 bits without/with time tag &lt;51, 64&gt;
- DNP3

  - Binary Command (12)
  - Analog Output (41)

The response must be evaluated in the sending module.

**Coding of the returned "PLC tag for command result"**

- IEC

  The result is returned in the response using "Cause of Transmission"

  The following results are supported:

  - unknown type identification &lt;44&gt;
  - unknown cause of transmission &lt;45&gt;
  - unknown common address of ASDU &lt;46&gt;
  - unknown information object address &lt;47&gt;
- DNP3

  The result is returned in the response using "Internal Indication Byte (IIN)"

  The following results are supported:

  - IIN1.6 DEVICE_TROUBLE
  - IIN2.0 NO_FUNC_CODE_SUPPORT
  - IIN2.1 OBJECT_UNKNOWN
  - IIN2.2 PARAMETER_ERROR
  - IIN2.4 ALREADY_EXECUTING

#### Masks

##### Masking of individual bits in the byte of binary inputs (Bin04B_S)

The "Masks" parameter group provides three options for transferring binary values. The corresponding bits are masked in hexadecimal format.

By entering hexadecimal values you can specify bit-by-bit whether certain bits do not trigger transmission or which bits are transferred in a different transmission mode.

- **Alarm mask**

  Changes in masked bits cause an unconditional spontaneous transmission. Changes from 0 to 1 and from 1 to 0 are evaluated.

  The "alarm mask" is only practical when the data point is transmitted over a dialup network and the option "Conditional spontaneous" was activated.
- **Send buffer principle mask**

  Changes in masked bits cause transmission according to the send buffer principle. Changes from 0 to 1 and from 1 to 0 are evaluated.

  The send buffer mask is only practical with data points that have the "Image memory" option enabled.
- **Disable mask**

  Masked bits are ignored when changes are checked. This means that changes to the masked bits for this data point do not trigger transmission. A masked bit always has the value 0 in the data frame.

##### Example of byte assignment

The following table shows the masking of the bits according to the hexadecimal value "A3" entered in the input box of the parameters.

Byte assignment

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit:** | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |
| **Masked** | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| **Hex mask** | A |  |  |  | 3 |  |  |  |

The bits with the value 1 are masked; in other words bits no. 0, 1, 5 and 7 cause the relevant function in the described masks.

### Message editor

This section contains information on the following topics:

- [Messages](#messages)
- [Processing status of messages (e-mails / SMS messages)](#processing-status-of-messages-e-mails-sms-messages)

#### Messages

##### Configuration of the messages

If important events occur, the communications module can send configured messages.

To transfer messages, telecontrol communication (parameter group "Communication types") no longer needs to be enabled.

The following are configurable:

- E-mails

  The recipient can be a PC with an Internet connection or an S7 station.
- SMS (only mobile wireless CPs or TIM modules)

  The recipient can be a mobile phone or an S7 station.

Up to 10 messages (e-mail or SMS) can be configured per module.

You configure the messages in the message editor of the module. Alternatively, you will find it:

- The shortcut menu of the module
- Via the project navigation: Directory of the station &gt; Local modules &gt; Communications module

##### Configuring e-mails

Required information:

- Access data of the SMTP server: Address, port number, user name, password
- When using STARTTLS or SSL/TLS: Certificate of the e-mail service provider
- E-mail addresses of the recipients
- APN (mobile wireless CPs)

  You obtain the access data for the mobile wireless network and for an APN for transferring e-mails from your network provider. You configure this in the parameter group "Mobile wireless communication settings".

You create the configuration in the following parameter groups.

- Enabling security functions

  To use e-mails, you need to enable the security functions of the CP, parameter group "Security".
- Configuration of the service / protocol:

  "E-mail configuration"
- When using STARTTLS or SSL/TLS:

  - Import of the certificate of the e-mail service provider:

    "Global security settings"
  - Using the imported certificate for the module:

    Parameter group "Security" &gt; "Certificate manager"

##### Configuring SMS messages (mobile wireless CPs)

Required information:

- Number of the SMSC

You create the configuration in the following parameter groups.

- Enabling the SMS function

  "Communication types" &gt; "Enable SMS"
- Configuration of the SMSC

  "Mobile wireless communication settings"
- Configuring the SMS

  Message editor

##### "Message parameter"

Here you configure the phone number or the recipient, the subject (e-mail) and the text of the message.

##### Text: Number of characters

Maximum number of characters that can be transferred in the message text:

- SMS: Max. 160 ASCII characters including any value sent at the same time
- E-mail: 256 ASCII characters including any value sent at the same time

For the value, see below, "Include value" parameter.

##### Character set for message texts

Entry of the following permitted characters as ASCII character sets (hexadecimal value and character name):

- 0x20

  Space
- 0x21 ... 0x5F

  ! " # $ % &amp; ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; &lt; = &gt; ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _
- 0x61 ... 0x7E

  a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~
- 0x7C, 0x7E

  | ~
- Manual line break (↵)

  In message texts, you can insert a line break using &lt;Shift&gt;+&lt;Enter&gt;.

##### "Trigger"

In the "Trigger" parameter group you configure triggering for sending the message and other parameters.

- **E-mail trigger**
   **/** 
  **SMS trigger**

  Specifies the event for which the sending of the message is triggered:

  - **Use PLC tag**

    For the trigger signal to send the message, the edge change (0 → 1) of the trigger bit "PLC tag for trigger" that is set by the user program is evaluated. When necessary, a separate trigger bit can be configured for each message. For information on the trigger bit, see below.

    **Resetting the trigger bit:**
      
    If the memory area of the trigger bit is in the memory area or in a data block, the trigger bit is reset to zero when the message is sent.  
    In all other cases, you need to reset the trigger bit with the user program.

    > **Note**
    >
    > **Fast setting of the diagnostics trigger tag**
    >
    > Trigger should not be set more often than once per second.
    >
    > **Frequent sending of SMS**
    >
    > Depending on the system environment, sending an SMS can take up to 2 minutes. To guarantee secure transmission of SMS in mobile wireless modules, a minimum interval of 10 seconds is recommended for triggering SMS.
  - **CPU changes to STOP**
  - **CPU changes to RUN**
  - **Connection to a partner interrupted**

    Triggers the sending of the message when the telecontrol connection to a partner is interrupted.
  - **Connection to a partner established**

    Triggers the sending of the message when the connection returns.
  - **Connection establishment to partner failed**

    Triggers the sending of the message when the telecontrol connection to a partner could not be established.
  - **Teleservice session started**

    (Mobile wireless CPs)

    Triggers the sending of the message when telecontrol communication is enabled and a TeleService connection is established.
  - **Teleservice session ended**

    (Mobile wireless CPs)

    Triggers the sending of the message when telecontrol communication is enabled and a TeleService connection has been terminated.
  - **Weak mobile wireless network**

    (SMS only)

    If the mobile wireless connection for telecontrol communication is too weak, an SMS message is triggered and sent to the configured recipient.
  - **VPN connection established**

    (CP 1243‑7 LTE, CP 1243‑1, CP 1542SP‑1 IRC)

    Triggers the sending of the message when the VPN connection is established or returns.
  - **VPN connection terminated**

    (CP 1243‑7 LTE, CP 1243‑1, CP 1542SP‑1 IRC)

    Triggers the sending of the message when the VPN connection is interrupted.
  - **SINEMA RC connection established**

    (CP 1243‑7 LTE, CP 1243‑1, CP 1542SP‑1 IRC)

    Triggers the sending of the message when the VPN or OpenVPN connection is established or returns.
  - **SINEMA RC connection terminated**

    (CP 1243‑7 LTE, CP 1243‑1, CP 1542SP‑1 IRC)

    Triggers the sending of the message when the VPN or OpenVPN connection is interrupted.
- **PLC tag for trigger**

  PLC tag for the trigger "Use PLC tag"
- **Enable identifier for processing status**

  If the option is enabled, every attempt to send returns a status with information about the processing status of the sent message.

  The status is written to "PLC tag for processing status". If there are problems delivering messages, you can determine the status via the Web server of the CPU by displaying the value of the PLC tag there.

  For the significance of the status output in hexadecimal, refer to the section [Processing status of messages (e-mails / SMS messages)](#processing-status-of-messages-e-mails-sms-messages).
- **PLC tag for processing status**

  PLC tag of the type DWORD for the processing status
- **Include value**

  When the option is enabled, the module sends a value from the memory area of the CPU for the placeholder in the message. To do this, enter "$$" or "$DATA$" as a placeholder for the value to be sent in the message text, depending on the module type. See below.

  Select a variable whose value will be integrated in the message. The value is entered in the message text instead of the placeholder.

  The placeholder for the value of a variable supports the following data types:

  - TIM 1531 IRC, CP 1200, CP 1542SP‑1 IRC

    ‑ Bool, Byte, Char, USInt, Int, UInt, Word, DWord, UDInt, DInt, Real, String

    ‑ Arrays of these data types

    Input of the placeholder in the message text for these modules: $$
  - TIM 3V‑IE, TIM 3V‑IE Advanced, TIM 4R‑IE

    ‑ Only "Array[2..16] of Char" from tag table

    Input of the placeholder in the message text for these modules: $DATA$

  Note that the number of characters increases with the value. For the maximum number of characters, refer to the configuration limits of the module.
- **PLC tag for value**

  PLC tag in which the value to be sent is written.

##### Error messages

If an error message for the trigger type is displayed when compiling the station, check the configuration.

If you have configured one of the following options as trigger type for the message:

- VPN / IPSec / SINEMA RC
- Check the following:

  - Are the security functions activated?
  - Is VPN activated?
  - Are additional options set correctly?

#### Processing status of messages (e-mails / SMS messages)

##### Enable status identifier / External status

If the option is enabled, the module writes a processing status about the sent e-mail / SMS to a PLC tag.

The processing status is returned by the module itself or the servers of the service after transfer of a message to be sent.

E-mails sent via program blocks of Open User Communication return a different status via the block (see block help).

The returned statuses of the Messages configured in the message editor have the following meaning:

SMS: Meaning of the status ID output in hexadecimal format

| Status | Meaning |
| --- | --- |
| 0000 | Transfer completed free of errors |
| 0001 | Error in the transfer, possible causes:  - SIM card invalid. - No network - Wrong destination phone number (number not reachable) |

E-mails: Meaning of the processing status output in hexadecimal format

| Status | Meaning |
| --- | --- |
| 0000 | Transfer completed free of errors |
| 82xx | Other error message from the e-mail server  Apart from the leading "8", the status corresponds to the three-digit error number of the SMTP protocol. |
| 8401 | No channel available  Possible cause: There is already an e-mail connection via the CP. A second connection cannot be set up at the same time. |
| 8403 | No TCP/IP connection could be established to the SMTP server. |
| 8405 | The SMTP server has denied the login request. |
| 8406 | An internal SSL error or a problem with the structure of the certificate was detected by the SMTP client. |
| 8407 | Request to use SSL was denied. |
| 8408 | The client could not obtain a socket for creating a TCP/IP connection to the mail server. |
| 8409 | It is not possible to write via the connection. Possible cause: The communications partner reset the connection or the connection aborted. |
| 8410 | It is not possible to read via the connection. Possible cause: The communications partner terminated the connection or the connection was aborted. |
| 8411 | Sending the e-mail failed. Cause: There was not enough memory space for sending. |
| 8412 | The configured DNS server could not resolve specified domain name. |
| 8413 | Due to an internal error in the DNS subsystem, the domain name could not be resolved. |
| 8414 | An empty character string was specified as the domain name. |
| 8415 | An internal error occurred in the cURL module. Execution was aborted. |
| 8416 | An internal error occurred in the SMTP module. Execution was aborted. |
| 8417 | Requests to SMTP on a channel already being used or invalid channel ID. Execution was aborted. |
| 8418 | Sending the e-mail was aborted. Possible cause: Execution time exceeded. |
| 8419 | The channel was interrupted and cannot be used before the connection is terminated. |
| 8420 | Certificate chain from the server could not be verified with the root certificate of the CP. |
| 8421 | Internal error occurred. Execution was stopped. |
| 8450 | Action not executed: Mailbox not available / unreachable. Try again later. |
| 84xx | Other error message from the e-mail server  Apart from the leading "8", the status corresponds to the three-digit error number of the SMTP protocol. |
| 8500 | Syntax error: Command unknown.  This also includes the error of having a command chain that is too long. The cause may be that the e-mail server does not support the LOGIN authentication method.  Try sending e-mails without authentication (no user name). |
| 8501 | Syntax error. Check the following configuration data:  Message configuration &gt; Message parameters:  - Recipient address ("To" or "Cc"). |
| 8502 | Syntax error. Check the following configuration data:  Message configuration &gt; Message parameters:  - E­mail address (sender) |
| 8535 | SMTP authentication incomplete. Check the "User name" and "Password" parameters in the CP configuration. |
| 8550 | SMTP server cannot be reached. You have no access rights. Check the following configuration data:  - CP configuration &gt; E-mail configuration:   - User name   - Password   - E­mail address (sender) - Message configuration &gt; Message parameters:   - Recipient address ("To" or "Cc"). |
| 8554 | Transfer failed |
| 85xx | Other error message from the e-mail server  Apart from the leading "8", the status corresponds to the three-digit error number of the SMTP protocol. |

### Protocol-specific parameters

This section contains information on the following topics:

- [TeleControl Basic](#telecontrol-basic)
- [SINAUT ST7](#sinaut-st7)
- [DNP3](#dnp3)
- [IEC 60870-5](#iec-60870-5)

#### TeleControl Basic

This section contains information on the following topics:

- [Naming conventions for TeleControl Basic](#naming-conventions-for-telecontrol-basic)
- [CP identification](#cp-identification)
- [Address and authentication data](#address-and-authentication-data)
- [Acknowledgment](#acknowledgment)

##### Naming conventions for TeleControl Basic

###### Character for data point names

The TeleControl Basic protocol supports the following ASCII characters (hex) for data point names:

- 0x20 ... 0x7e

Note the exceptions listed below.

###### Invalid characters for data point names

The following ASCII characters are prohibited for data point names under TeleControl Basic:

- 0x22 (quotation marks)
- 0x27 (apostrophe)
- 0x2e (period)
- 0x2f (slash)
- 0x5b and 0x5d (square brackets)
- 0x5c (backslash)
- 0x7c (pipe)
- 0x20 (spaces) at the start or end

###### Invalid characters for station names

The following ASCII characters are forbidden for station names under TeleControl Basic:

- 0x2e (period)
- 0x5b and 0x5d (square brackets)
- 0x20 (spaces) at the start or end

##### CP identification

###### Reference

CPs using the "TeleControl Basic" protocol.

"CP identification" parameter group

###### One project number for the entire STEP 7 project

If you change the project number for a CP in the "CP identification" parameter group, this parameter is changed for all CPs in the entire STEP 7 project using the "TeleControl Basic" protocol.

TCSB evaluates project numbers from 1 ... 2000.

###### Configuration of the station number

You need to configure a unique station number for each station in the STEP 7 project that uses a CP using the "TeleControl Basic" protocol.

TCSB evaluates station numbers from 1 ... 8000.

###### Access ID

The access ID displayed in the "CP identification" parameter group is made up of the hexadecimal values of the project number, station number and slot. The parameter of the type DWORD is allocated as follows:

- Bits 0 ‑ 7: Slot
- Bits 8 to 20: Station number
- Bits 21 to 31: Project number

##### Address and authentication data

###### IP address of the CP

Since the CP always establishes the connection with TCSB, a dynamic IP address can be assigned to the CP by the Internet service provider.

###### Address and authentication data for communication with TCSB

The following information is required for the STEP 7 configuration of the CP for communication with TCSB:

- Parameters in the "Partner stations" parameter group

  - Partner IP address

    IP address or host name of the DSL router via which the telecontrol server is connected to the Internet.

    A fixed IP address is recommended.
  - Partner port (port number of the listener port of TCSB)
- Parameters in the "Security &gt; CP identification" parameter group

  - Project number
  - Station number
  - Password (for authentication)

##### Acknowledgment

###### Acknowledgment in TeleControl Basic

The receipt of a sent frame is acknowledged as follows.

- Telecontrol communication

  Frames received from TCSB are acknowledged immediately by the CP.

  Frames sent by the CP are acknowledged by TCSB.
- Inter-station communication

  Received frames are acknowledged immediately by the CP. The acknowledgment frame is forwarded by the telecontrol server to the destination CP.

  For sent frames, this applies in the opposite direction.

#### SINAUT ST7

This section contains information on the following topics:

- [The TD7 software](#the-td7-software)
- [Communication between SINAUT objects](#communication-between-sinaut-objects)
- [Address parameters with the "ST7" protocol](#address-parameters-with-the-st7-protocol)
- [Acknowledgment](#acknowledgment-1)
- [Expansion of SINAUT projects](#expansion-of-sinaut-projects)

##### The TD7 software

###### Tasks of the TD7 software

In communications modules that use the telecontrol protocol SINAUT ST7, the software "SINAUT TD7" handles the communication and process data transfer between the subscribers. Only with TD7 software can data communication via WAN connections between CPs with ST7 capability and TIM modules be implemented.

TD7 provides change-driven process data transfer between the station and the control center (e.g. ST7cc), between individual stations and between the communications module and CPU. Failure of connections from CPUs or the control center are displayed. Once a problem has been corrected and when the CPUs or control center start up, the data is updated automatically.

###### Versions of the TD7 software

The TD7 software is available in two versions. Only one version can be alternatively used in communication modules that support both TD7 versions.

- **TD7onTIM**

  TD7onTIM is configured via the data points of the module. In productive operation, this runs in the communication module.

  The functions and parameters are described in the sections for configuring the data points.

  The version can be used in all ST7-capable modules.

  The advantages of this variant are:

  - Easy to configure
  - Independence of the TD7 software from the CPU program
  - The blocks can run on an S7-1500 CPU as of firmware V2.5.

  With S7-1500, TD7onTIM is supported by the CPU as of firmware V2.1.
- **TD7onCPU**

  TD7onCPU takes the form of a program block library. The blocks are used and parameter assignment in the CPU, which is networked with the TIM. The software runs during productive operation on the CPU.

  TD7onCPU can be used with the following modules:

  - TIM 1531 IRC
  - TIM 3V‑IE Advanced
  - TIM 4R‑IE / TIM 4R‑IE Standalone

  The advantages of this variant are:

  - High speed if data changes

    Changes are detected with every CPU cycle.
  - Larger selection of data typicals for the master station and the station

###### The TD7onCPU libraries

TD7onCPU is available in two block libraries for the following SIMATIC families:

- S7-1500

  The blocks can run on an S7-1500 CPU as of firmware V2.5.
- S7-300 / 400

  The blocks can run on an S7-300 and on an S7-400 CPU. Exceptions will be pointed out explicitly.

  Apart from process data transfer via WAN, the package is also suitable for local communication between CPUs, if they are connected via MPI. Here, as well, local connections and CPUs are constantly monitored and there is an automatic update after starting up or eliminating disruptions.

For a description of TD7onCPU, refer to the section [Block library Telecontrol ST7](#block-library-telecontrol-st7).

##### Communication between SINAUT objects

###### Communication between objects or typicals

- **Object / typical**

  In SINAUT ST7 the term "object" refers to the representation and handling of process variables such as messages, analog values, commands, motors, valves, controllers etc. The TD7 software always processes "objects".

  Objects in the TD7 world consist of processing instructions in the form of program blocks - known as typicals

  An object consists of the following components:

  - A function block (FB)
  - A data block (DB)

    The DB is the object data record that is assigned to the FB as an instance DB.

An object or a typical is always made up of a process part and an operator control and monitoring part (operator part) that operate in different subscribers in the SINAUT network. To be able to process their predetermined function the two parts must communicate with each other.

These two parts are used in the following subscriber types and have the following taks:

- **Operator typicals**

  Used in central stations (operator end)

  These blocks send setpoints, parameters, command and organizational instructions to the process typicals.
- **Process typicals**

  Used in stations (process end)

  These blocks manipulate process values, and return process data, alarm and status messages and organizational information to the operator typicals.

The data that describes the object is exchanged between the two communications partners. The data is located in the object data record in the data indexes 0...n. The extent and composition of this data area depend on the typical involved. It can consist of several identical or a combination of different data types. In the object data record at the process and operator end, the data structure of two typicals that belong together is identical

The data exchange does not necessarily run in both directions.

###### Object addressing

- **Subscriber number**

  Each CPU with TD7 software receives a SINAUT subscriber number that can be assigned in the range from 1 to 32000 and is unique throughout the network.
- **Object number**

  Each typical that is called in one of these CPUs has an instance DB whose number is identical to the SINAUT object number.

With the aid of the SINAUT subscriber number and the SINAUT object number, explicit addressing for the communication between the typicals that belong together can be implemented.

All data point typicals are function blocks (FBs). An instance DB must be specified when an FB is called. The number of this instance DB is identical to the object number of the data point object. At the send and receive ends this object number does not have to be identical.

To specify the communications relation, every typical as the following parameters

- **Partner number**

  "PartnerNo"

  Subscriber number of the partner being communicated with.
- **Partner object number**

  "PartnerObcetcNo"

  Object number (= instance DB no.) of this partner
- **Index**

  For the storage, the index number included in the data frame is taken into account.

###### Types of frame

After the process and operator data has been exchanged, organizational information (Org. frames) is transferred between the two ends. The following frame types (TA) are distinguished:

- TA 0: Spontaneous Org. frames
- TA 1: Requested Org. frames
- TA 2: Spontaneous data frames.
- TA 3: Requested data frames

This data flow of the Org. frames and the data areas in the object data record intended for this (Org. indexes) are not shown in the figure above.

##### Address parameters with the "ST7" protocol

###### Addressing communications partners and network nodes

Communication with the "SINAUT ST7" protocol can run via different paths and subnets. The following two parameters serve to address the individual subscribers in the ST7 network:

- **Subscriber number**

  The subscriber number is unique for every subscriber in a STEP 7 project. The following subscribers require a subscriber number:

  - **Communications module**

    ST7-capable modules (TIM, CP)
  - **CPU**

    The local CPU that is assigned to the communications module as the end point of a telecontrol connection receives a subscriber number via the ST7 protocol.

    With a CP and a TIM 3V‑IE / TIM 4R‑IE, the local CPU is assigned automatically via the rack.

    Assign the CPU to the TIM 1531 IRC in the "Subscriber numbers" parameter group of the TIM.
  - **Application of the master station PC**

    The application that you configure in the PC station of the master station.

  For the TIM and the assigned CPU, the subscriber number is configured in the "Subscriber numbers" parameter group of the TIM.

  For the application of the master station PC, the subscriber number is configured in the telecontrol connection: "Network data" editor &gt; "Telecontrol" tab
- **WAN address**

  For every networked serial interface in a classic ST7 network a WAN address is assigned. It is unique in the respective WAN network.

  Since telecontrol connections can run via several network nodes and node stations, unique addressing of the interfaces involved is necessary throughout the network.

  The WAN address is configured in the parameter group "WAN parameters" of the serial interface.

###### Addressing the data

The process data to be transferred is configured as data points, see section [ST7 data points](#st7-data-points).

##### Acknowledgment

###### Acknowledgment in ST7

- Communication with the master station

  - Data frames sent by the master station are acknowledged immediately by the CP when received.
  - Data frames sent by the communications module are acknowledged by the master station.
- Inter-station communication between stations

  Data frames are acknowledged during communication between station and master station.

  With inter-station communication acknowledgement frames of the receiving module are not forwarded by the master station to the sending communications module.

##### Expansion of SINAUT projects

###### Expansion of existing SINAUT projects

SINAUT projects with TIM modules for the SIMATIC families S7‑300 and 400 that were configured in STEP 7 V5 can be expanded with newer modules that are configured in STEP 7 Professional.

To do this, in STEP 7 V5 projects, TIM modules are configured as placeholders (proxies) for modules that are configured in STEP 7 Professional. The configuration data (SDBs) are exported from STEP 7 V5 and imported into STEP 7 Professional.

Selection of the "Import" configuration procedure in the "Basic settings" parameter group is required for the import of configuration data from STEP 7 V5; see section [Configuration](#configuration-1).

The extension of SINAUT projects is supported by the following modules:

Module migration from STEP 7 V5 to STEP 7 Basic / Professional (TIA Portal)

| Module function for STEP 7 V5 project expansion |  |  | S7-1200/1500 module in STEP 7 Basic / Professional |  |
| --- | --- | --- | --- | --- |
| TIM (function) for expansion | Proxy to be used in the catalog | Compatible module | Required STEP 7 version |  |
| TIM 3V‑IE Advanced | PROXY CP1243‑8 IRC | ⇒ | CP 1243‑8 IRC | STEP 7 Basic |
| TIM 3V‑IE Advanced | PROXY CP1243‑8 IRC | ⇒ | CP 1542SP‑1 IRC | STEP 7 Professional |
| TIM 4R‑IE | PROXY TIM 1531 IRC | ⇒ | TIM 1531 IRC | STEP 7 Professional |
| TIM 4R‑IE Stand-alone | PROXY TIM 1531 IRC | ⇒ | TIM 1531 IRC | STEP 7 Professional |

> **Note**
>
> **TIM 4R‑IE Stand-alone for S7‑400 becomes TIM 1531 IRC**
>
> A TIM 4R‑IE Stand-alone required in STEP 7 V5 that is assigned to a CPU-400 must be replaced by a TIM 1531 IRC for the expansion of classic SINAUT projects in STEP 7 Professional.
>
> A TIM 4R‑IE Stand-alone can only be created in new projects that are configured exclusively in STEP 7 Professional.

> **Note**
>
> **No serial interface for CP 1542SP‑1 IRC**
>
> For a CP 1542SP‑1 IRC, no serial interface can be configured in STEP 7 V5 because the CP does not have a serial interface.

###### Requirements and module update

Requirements for the import are as follows:

- **STEP 7 V5 project**

  A configuration file from a consistent STEP 7 V5 project
- **Firmware version**

  One of the following firmware versions is required for the communication module:

  - TIM 1531 IC: V2.0
  - TIM 1531 IC: V1.1

    A TIM V1.1 can be replaced by a TIM V2.0, not vice versa.

    In STEP 7, the "Telecontrol configuration" method is set to "Configure". Existing configuration data is applied.
  - CP 1542SP‑1 IRC: V2.0

    A CP V1.0 can be replaced by a CP V2.0, not vice versa.

    In STEP 7, the "Telecontrol configuration" method is set to "Configure". Existing configuration data is applied.
  - CP 1243‑8 IRC: V3.1

    Transfer of data from STEP 7 V5 with modification options (see "Imported configuration data" below)

    A CP V3.0 can be replaced by a CP V3.1, not vice versa.
  - CP 1243‑8 IRC: V2.1

    Adoption of the data from STEP 7 V5 without the option of making changes

    A CP V2.1 can be replaced by a CP V3.1, not vice versa. The CP used must have hardware product version 2.

    In STEP 7, the "Telecontrol configuration" method is set to "Import". Existing configuration data is applied.

    > **Note**
    >
    > **Disabling the partner configuration data during migration from STEP 7 V13 SP1**
    >
    > If you migrate a CP 1243‑8 IRC V2.1 from STEP 7 V13 SP1 to STEP 7 V15, the partner configuration data is disabled. You receive a message when compiling the project.
    >
    > In this case, repeat the import of the partner configuration data into the module.
  - TIM 3V... / TIM 4R...: V2.5.5
- **ST7 connections**

  For ST7 connections between a TIM 1531 IRC and a CPU:

  - The firmware of the CPU must have at least version V2.5.
  - Prior to import, the TIM and the CPU must be networked in STEP 7 Professional.
  - When configuring TD7onCPU, the CPU must not be assigned to the TIM in STEP 7 Professional.

  For ST7 connections between a TIM 1531 IRC and a PC application:

  - Prior to import, the TIM and the PC station must be networked in STEP 7 Professional.
- **CPU 1500 / PC station**

  For a CPU 1500 or a PC station with SINAUT application as an ST7 communication partner, the IP address in the STEP 7 V15 project must correspond to the address configured in STEP 7 V5.

###### Configuration in STEP 7 V5

For a description of the configuration, refer to the manuals of the modules involved.

#### DNP3

This section contains information on the following topics:

- [Addressing](#addressing)
- [Connection establishment](#connection-establishment)
- [Acknowledgment with the DNP3 protocol](#acknowledgment-with-the-dnp3-protocol)
- [Transmission settings – DNP3](#transmission-settings-dnp3)
- [Settings DNP3 master function](#settings-dnp3-master-function)
- [Settings DNP3 station](#settings-dnp3-station)
- [DNP3 security options](#dnp3-security-options)

##### Addressing

To configure and commission the communications module, the following information is required:

###### Address information of the stations

For the addressing of SIMATIC NET communications modules with station function, the following parameters must be configured:

- Station address (DNP address of the station)
- Address of the station on the network or data link layer

  Depending on network type:

  - IP address and subnet mask; as an alternative: IP address of a DHCP server
  - Telephone number (for dial-up network)
- Number of the station's own listener port (for connection requests from the master)
- Indices of the data points (Data point index = point index)

###### Address information of the master

For the addressing of SIMATIC NET communications modules with master function, the following parameters must be configured:

- Station address (DNP address of the master)
- Address of the master on the network or data link layer

  Depending on network type:

  - IP address / subnet mask + port number of the listener port of the master

    or

    Name resolvable by DNS  
    (You need the DNS server address, the DNS server must be accessible by the module.)
  - Telephone number (for dial-up network)
- Indices of the data points (Data point index = point index)

###### Redundant DNP3 master

The two devices of a redundant master have an identical station address.

They only require different IP addresses or host names.

For information on configuring a redundancy group with 3 servers, see section [Redundant DNP3 master group with 3 servers](#redundant-dnp3-master-group-with-3-servers).

###### Configurations with connections over the Internet: VPN connections

For connections running via the Internet, dynamic IP addresses can be used.

To allow communication in both directions and to ensure that the data is protected during transfer, a connection with a VPN tunnel is necessary. For this the security modules of the SCALANCE S or SCALANCE M series are available.

Remember the following points when configuring:

- You configure the master IP address as normal.
- When configuring the interface of the module, configure the IP address of the router.
- You create the VPN configuration with SCALANCE S/M both for the station end and for the control center end in STEP 7.

---

**See also**

[Subscriber numbers](#subscriber-numbers-1)
  
[Data point index](#data-point-index)

##### Connection establishment

###### Connection establishment with DNP3

With the DNP3 protocol, the master establishes the connection (call operation / polling).

If an established connection is interrupted, a master module tries to re-establish the connection.

> **Note**
>
> **Connection interrupted by the mobile wireless network provider**
>
> When using mobile wireless services, remember that existing connections can be interrupted by mobile wireless network providers for maintenance purposes.

**Unsolicited mode**

Enabling the "Unsolicited reporting" parameter in the "Unsolicited transfer" parameter group in the "Settings DNP3 station" of an interface enables the unsolicited transmission of data from a station. In this case, dial-up network connections can be established by the communication module as client in order to send data of events spontaneously.

###### Connection establishment in Open User Communication and PG/OP communication

In Open User Communication in an S7 station, the CPU is the connection partner.

Connections are established as soon as the corresponding program blocks are called on the CPU.

This also applies to the situation when a different S7 station sends data. In this case, the receiver station calls the corresponding receiver modules.

##### Acknowledgment with the DNP3 protocol

###### Acknowledgment in DNP3

The basic acknowledgment mechanisms are configured for the data link layer, see section [Transmission settings – DNP3](#transmission-settings-dnp3).

A station module acknowledges a request from the master with its response frames.

The acknowledgment of unsolicited frames that a station module sends to the master is configured in the "Settings DNP3 station" parameter group, see section [Settings DNP3 station](#settings-dnp3-station).

##### Transmission settings – DNP3

###### Transmission settings – DNP3

- **Max. time between Select and Operate**

  Max. time period (seconds) between command preselection (Select) and command input (Operate)

  - Master station:

    If no command input follows a command preselection in the master station within the configured period, the command must be selected again. Having to enter the command twice reduces the risk of accidental operation in the master station.
  - Station:

    In order for a received command to be sent to the CPU and thereby take effect, the device must not receive any further command frames between Select and Operate.

  Range of values: 1..65535

  Default setting: 1

  If a master sends an object with function code 7 "DIRECT_OPERATE" to the station, the station does not evaluate the time period configured here.

  You define the mode of command processing for each individual command data point, see [Command options](#command-options).
- **Form of transfer**

  Defines the form of transfer of events.

  - Type-specific

    This is the bundled transfer of events according to data types typical for DNP3. First the existing binary events are sent, then all analog values and finally all counted value changes. This makes the frames somewhat more compact and transmission more efficient.
  - Chronological

    In this mode, events are transmitted strictly chronologically. The optimizing effect of grouping in blocks of the same data type as described in the DNP3 specification (see above) is lost. This mode is primarily intended for control systems that archive events strictly chronologically.

  Default: Type-specific
- **Connection monitoring time (application layer)**

  (Application layer confirmation timeout)

  Time (seconds) in which the module expects a sign of life on the application layer from its partner.

  - Master (master station):

    Time period in which the master expects a sign of life from the station.

    If the configured time is exceeded, the master sends a frame to the station. If this frame is not acknowledged by the station, the master classifies the station as not accessible, terminates the connection and then re-establishes it.

    Commands:  
    If a connection with a station is interrupted or disrupted, command frames are repeated a maximum of three times before they are discarded by the master.
  - Station:

    In the station, the parameter is used to calculate the waiting times during connection establishment.

  With redundant paths, the following applies: If the acknowledgment is not received, the transmission path is classified as disrupted.

  Range of values: 0 ... 65535 s

  Default: 5

  With the setting 0 (zero), the function is disabled.
- **Partner monitoring time**

  If the station module does not receive a sign of life from the master on the application layer within the configured time, it classifies the connection as disrupted and terminates it.

  The master module expects a response from the station after sending data within the configured time.

  Range of values: 0 ... 65535

  Default: 0

  With the setting 0 (zero), the function is disabled.

###### Data link layer

- **Frame repetition**

  Maximum number of retries to send a frame if no acknowledgment is received from the partner on the data link layer.

  - For serial connections, repetitions can be useful if the connection quality is not good.
  - With Ethernet connections, it is recommended to configure the value 0, since the required repetitions are carried out by the protocol implementation.

  Range of values: 0 ... 255

  Default setting: 0

  With the setting 0 (zero), the function is disabled.
- **Acknowledgment**

  Condition under which the module requests an acknowledgment of receipt from the partner (sending the "CONFIRMED_USER_DATA" function code):

  - Never

    No acknowledgments are requested.
  - Always

    Acknowledgments are always requested.
  - When segmented

    Acknowledgments are only requested for data frames which are divided into several segments due to their length.

  With Ethernet connections, the DNP3 specification recommends that the acknowledgment requests are not used on the data link layer.

  On connections that are liable to disturbances, for example wireless links, the configuration of acknowledgment requests can be useful on the data link layer.
- **Acknowledgment monitoring time**

  Time period (seconds) in which a confirmation (acknowledgment) is expected from the partner on the data link layer. If no acknowledgment is received within the configured time period, data transmission is repeated, see the "frame repetition" parameter above.

  Range of values: 0...65535

  Default setting: 2

  The default value of 2 seconds usually only needs to be increased for slow serial connections.

  With the setting 0 (zero), the function is disabled.

##### Settings DNP3 master function

###### Master-specific DNP3 parameters

The parameters below apply to the following interfaces of communication modules:

- Interfaces whose "Network node type" parameter is configured as "Master station".
- Interfaces of stations that use the master function for "Direct communication" with other stations.

You can find the following parameters in the "Settings DNP3 master function" parameter group:

- **Polling basic interval**

  Here, you define the basic value for station calls by the master station.

  Value range: 0 ... 65535 seconds

  Default: 30

  With the setting 0 (zero), the function is disabled. There is no cyclic polling, not even for the parameters listed below, whose value is calculated as a multiple of the polling basic interval.

  **Basis for further parameters**

  The polling basic interval is used as the calculation base for the following parameters:

  - Event polling interval
  - Class 0 polling interval

  The value configured for these parameters is the factor for the Polling basic interval.

  The parameters are configured in the "Network data &gt; Telecontrol &gt; DNP3" connection editor, see [Connection table - DNP3](#connection-table---dnp3).
- **Max. number of events per call**

  Maximum number of events that can be sent in the response telegram of the station after being called by the master station.

  Range of values: 0 ... 65535

  Default: 0

  With the setting 0 (zero), the function is disabled (no limitation).

##### Settings DNP3 station

###### DNP3 parameters of the station / node station

You can find the following parameters in the "Settings DNP3 station" parameter group of the interfaces of the communications module set on the "Station" or "Node station" network node type.

**General**
 **/** 
**CPU status**

- **IP address check**

  This parameter is used for security when establishing a connection between a station and the master.

  - Check IP address

    When this option is activated, the station checks the partner's IP address in addition to the station address when a connection is requested.

    If the IP address of the partner does not match the address of a configured partner of the station, the station rejects the connection.
  - Do not check IP address

    The station does not check IP addresses for incoming TCP connection requests.
- **Reaction to CPU STOP**

  Here you define the behavior of the communications module on STOP of the assigned CPU:

  - No reaction
  - Notify via disturbance bit (IIN1.6)

    The communications module uses the Internal Indication Byte (IIN1.6) in the Application Response Header in order to indicate a CPU fault to the master.

    The bit is set to "1" when the CPU is in STOP state.
  - Termination of connection with the partner

    The communications module terminates the connection with the partner on STOP of the CPU.

###### Event properties

- **Event class for image memory**

  Selection of an event class in which only the last current values are stored in the send buffer. Older events are overwritten in the send buffer (image memory method).

  The parameter is not available with the TIM 3V‑IE DNP3 / TIM 4R‑IE DNP3. These modules operate according to the "Default" setting.

  - Class x events

    You can select an event class whose values are handled according to the image memory method. The events of this class are not saved in the send buffer. Only the current value is saved and transferred in each case.
  - Standard

    The values of no class are handled according to the image memory method; all values are saved according to their class assignment in the send buffer until they have been transmitted.

  You can find details of how the image memory and send buffer work as well as the options for transferring data in the section [Process image, type of transmission, event classes](#process-image-type-of-transmission-event-classes).
- **Buffer for class**
   **1 / 2 / 3 events**

  For each of the three event classes, this is where you specify the number of events after which the stored events are sent to the communication partner.

  Note that the maximum size of the send buffer is divided over all connected DNP3 master stations.

  Permitted range: 0 ... 65000

  With the setting 0 (zero), the number of events is not checked for the transfer.
- **Delay time class**
   **1 / 2 / 3 events**

  Here, for each of the three event classes you specify the maximum time in seconds for which the events can be stored in the send buffer before they are sent to the communications partner.

  This requires unsolicited transmission to be configured (see below).

  Permitted range: 0 ... 65535

  With the setting 0 (zero), the function is disabled.

###### Polling parameters

The following four parameters are configured for the station module, transferred to the master station and stored there. You can configure individual values of the four parameters for individual segments of the telecontrol connections. You then overwrite the values configured at the station module for the respective segment.

- **Event polling interval**

  Relevant for master, third-party device (master)

  The "Event polling interval" defines the cycle in which the DNP3 master station polls events of the station. The interval is specified as a multiple of the "Polling basic interval" of the master, see [Settings DNP3 master function](#settings-dnp3-master-function).

  The value configured here is the factor for the polling basic interval. The sum of the two values provides the length of the event polling interval in seconds.

  Range of values: 0 ... 65535
- **Class 0 polling interval**

  Relevant for master, third-party device (master)

  The Class 0 polling interval determines the cycle in which the DNP3 master polls class 0 data from the image memory of the station. The interval is specified as a multiple of the "Polling basic interval" parameter of the master, see [Settings DNP3 master function](#settings-dnp3-master-function).

  The value configured here is the factor for the polling basic interval. The sum of the two values provides the length of the class 0 polling interval in seconds.

  Range of values: 0 ... 65535

  Default: 1

  With the setting 0 (zero), the function is switched off, class 0 data is not transmitted cyclically.
- **Max. polling duration**

  Relevant for master, third-party device (master)

  Specifies the maximum time period during which the master may continuously call this station. Even if data is still pending for transmission in the station after this time, the calls from the master station are canceled. This means that the master station is once again available to other stations.

  Range of values: 0 ... 65535

  Default: 10

  With the setting 0 (zero), the function is disabled; in other words, the calling period is unlimited.
- **Polling mode**

  Relevant for master, third-party device (master)

  Mode in which the master station calls the station.

  Range of values:

  - Cyclic

    The station is called cyclically. The duration of the polling cycle is equal to the "Class 0 polling interval", see above.
  - After startup

    The station is only called after the initial startup and after a restart.

    If no unsolicited transmission is enabled for a station, no data is transmitted during operation when this option is selected.

###### Node station

This parameter is only available for interfaces for which the network node type is set to "Node station".

- **Response only with current station image**

  With an interface of the "Node station" network node type, the communications module of the node station keeps the station process image in the image memory for each lower-level DNP3 station.

  - Option enabled

    The module replies to a class 0 call only if the process image in the image memory of the node station is up to date.
  - Option disabled

    The module replies to a class 0 call even if the process image in the image memory of the node station is not up to date. When a master station calls, the data of all connected stations is sent to the master station, even if the data of one or more stations is not up-to-date.

###### Unsolicited transfer

- **Max. number of retries**

  Maximum number of repetitions of unsolicited telegrams if no acknowledgment is received from the master. After reaching the configured number, the station terminates the connection.

  Range of values: 0...255

  Default setting: 3

  You can usually enter the value 0 for Ethernet connections, since repetitions in the event of transmission errors due to collisions are realized by the protocol.
- **Monitoring time for spontaneous telegrams**

  The "Unsolicited Confirmation Timeout period" is the period in which the station expects an acknowledgment of unsolicited telegrams from the master. If no acknowledgment is received within the configured time period, the data transmission is repeated.

  The sent telegrams are deleted from the send buffer only when the station receives the acknowledgment from the master.

  Units depending on module: Seconds or milliseconds

  Range of values: 1...65535 s / 0...65535 ms

  Default setting: 5 / 5000

You define the activation of spontaneous transfer for each connection segment, see "Unsolicited" in the section [Connection table - DNP3](#connection-table---dnp3).

##### DNP3 security options

###### Authentication and key exchange

When the (Secure Authentication) function is enabled, the DNP3 master and station authenticate themselves with a secret key, the pre-shared key.

With the help of the common pre-shared key, after the first connection establishment between master and station, session keys are agreed that are then renewed cyclically. Renewal of the session keys is normally initiated by the master.

The criteria for renewing the key are specified in the following parameters.

- Key exchange interval
- Authentication requests before key exchange

As soon as one of these conditions is met, the session key is renewed.

###### Parameters

- **Enable DNP3 security options**

  Select the option if you want to use Secure Authentication.
- **IKE mode**

  Selection of the mode for key exchange. Range of values:

  - Aggressive Mode

    The Aggressive Mode is somewhat faster but transfers the identity unencrypted.
  - Main Mode

    The Main Mode is the standard mode.

  Default setting: Aggressive Mode
- **Security statistics**

  Specifies whether the statistics of security events are sent to the master. Security events are authentication requests to the module. If this option is activated, all authentication request are stored in the module with date, time and result and sent to the master for further evaluation.

  Security statistics events are only output if a SCADA system is connected to the master.

  Range of values:

  - Do not send security statistics
  - Send security statistics

  Default setting: Do not send security statistics
- **SHA-1 interlock**

  Setting to select whether the CP may use the secure hash algorithm SHA-1 if "SHA-256" was configured as the Secure hash algorithm and the master does not support SHA-256.

  Range of values:

  - SHA-1 mode not allowed

    The module must not use SHA-1. If the master does not support SHA-256, no connection will be established.
  - SHA-1 mode allowed

    The module can use SHA-1 if the master does not support SHA-256.

  Default setting: SHA-1 mode not allowed
- **Secure hash algorithm (SHA)**

  Selection of the Secure Hash Algorithm (SHA)

  Range of values:

  - SHA‑1
  - SHA‑256

  Default setting: 256
- **Key wrap algorithm**

  Selection of the Advanced Encryption Standard (AES)

  Range of values:

  - AES‑128
  - AES‑256

  Default setting: AES‑128
- **Key length**

  Specifies the length of the pre-shared key in bytes.

  The following lengths are used depending on the key wrap algorithm.

  - For AES‑128: 16 bytes
  - For AES‑256: 32 bytes
- **Max. number of statistics queries**

  If the configured number of statistics requests of the master is exceeded within the key exchange interval, the module enters a message in the diagnostics buffer of the CPU.

  Range of values: 2...255. Default setting: 5
- **Authentication requests before key exchange**

  Maximum number of station authentication requests to the master. When this number is reached, the session key is renewed.

  Range of values: 1...10000. Default setting: 1000

  Recommendation: Set the number for the station twice as high as for the master.
- **Key exchange interval**

  Period after which the key is exchanged again between the station and the master. The interval must be matched up on both communications partners.

  Range of values: 0...65535 min. at 0 (zero), the key is never changed (function disabled). Default setting: 15 min.

  Recommendation: Set the key exchange interval for the station twice as high as for the master.
- **Authentication timeout**

  Maximum waiting time for the master to respond to an authentication request from the station.

  Exceeding the waiting time is considered an error by the station. In this case, the station generates a security event and sends it to the master.

  Range of values: 1... 65535 s. Default setting: 5
- **Pre-shared key**

  The pre-shared key can be configured in two ways:

  - Manual configuration

    Enter the pre-shared key in STEP 7 manually as a hexadecimal value.
  - Import as file

    Import the pre-shared key from the file system of the engineering station if the pre-shared key was generated by the master or another system.

  The pre-shared key of a station module must be identical to the pre-shared key of the master.

#### IEC 60870-5

This section contains information on the following topics:

- [Addressing](#addressing-1)
- [Transmission settings - IEC 60870-5](#transmission-settings---iec-60870-5)
- [Acknowledgment with IEC protocol](#acknowledgment-with-iec-protocol)
- [IEC-specific parameters](#iec-specific-parameters)

##### Addressing

To configure and commission the communications module, the following information is required:

###### Address information of the stations

For the addressing of SIMATIC NET communications modules with station function, the following parameters must be configured:

- ASDU address of the module on the application layer

  For information on the configuration, see [Subscriber numbers](#subscriber-numbers-1).
- Address of the station on the network or data link layer

  Depending on network type:

  - IP address and subnet mask; as an alternative: IP address of a DHCP server
  - Telephone number (for dial-up network)
  - WAN address (for dedicated line)
- Number of the station's own listener port (for connection requests from the master)
- Indices of the data points (Data point index = Information object address)

  For information on the configuration, see [Data point index](#data-point-index).

###### Address information of the master

For the addressing of SIMATIC NET communications modules with master function, the following parameters must be configured:

- ASDU address of the master on the application layer
- Address of the master on the network or data link layer

  Depending on network type:

  - IP address / subnet mask + port number of the listener port of the master

    or

    Name resolvable by DNS  
    (You need the DNS server address, the DNS server must be accessible by the module.)
  - Telephone number (for dial-up network)
  - WAN address (for dedicated line)
- Indices of the data points (Data point index = Information object address)

###### Redundant IEC master

The two devices of a redundant master have an identical ASDU address.

They only require different IP addresses or host names.

###### Configurations with connections over the Internet: VPN connections

For connections running via the Internet, dynamic IP addresses can be used.

To allow communication in both directions and to ensure that the data is protected during transfer, a connection with a VPN tunnel is necessary. For this the security modules of the SCALANCE S or SCALANCE M series are available.

Remember the following points when configuring:

- You configure the master IP address as normal.
- When configuring the interface of the module, configure the IP address of the router.
- You create the VPN configuration with SCALANCE S/M both for the station end and for the control center end in STEP 7.

##### Transmission settings - IEC 60870-5

###### Transmission settings - IEC 60870-5

- **ACTTERM**

  Activates the sending of acknowledgments with the cause of transmission ACTTERM (cause of transmission &lt;10&gt;).

  With this, the end of command processing is signaled to the partner.

  With direct communication between two stations, ACTTERM must be configured identically for both partners.
- **Max. time between Select and Operate**

  Max. duration (seconds) between Select and Operate. For a Select command to be transferred to the CPU and to take effect, no other frame may be sent to the station between Select and Operate.

  Permitted range: 1..65535

  Default setting: 1

  You define the mode of command processing for each individual command data point, see [Command options](#command-options).
- **Monitoring time for connection establishment (t**
  <sub>0</sub>
  **)**

  Monitoring time for the connection establishment (t<sub>0</sub>) in seconds. If the communication partner does not confirm connection establishment within the monitoring time, the module attempts to establish the connection again.

  Permitted range: 1..255

  Default setting: 30
- **Frame monitoring time (t**
  <sub>1</sub>
  **)**

  Monitoring time in seconds for the acknowledgement of frames sent by the module by the communication partner. The monitoring time applies to all frames sent by the module in I, S and U format.

  If the partner does not send an acknowledgment during the monitoring time, the module terminates the connection to the partner.

  Permitted range: 1..255

  Default setting: 15

  > **Note**
  >
  > **Settings on the master**
  >
  > When configuring the monitoring times t<sub>1</sub> and t<sub>2</sub> make sure that you make the corresponding settings on the master so that there are no unwanted error messages or connection aborts.
- **Monitoring time for S and U frames (t**
  <sub>2</sub>
  **)**

  Monitoring time in seconds for the acknowledgment of data frames of the master by the module.

  After receiving data from the master, the module acknowledges the received data either:

  - If the module sends data to the master itself within t<sub>2</sub>, it acknowledges the data frames received from the master during t<sub>2</sub> at the same time along with the sent data frame (I format).
  - The module sends an acknowledgment frame (S format) to the master at the latest when t<sub>2</sub> elapses.

  Permitted range: 1 ... 255

  Default setting: 10

  The value of t<sub>2</sub> should be less than that of t<sub>1</sub>.
- **Idle time for test frames (t**
  <sub>3</sub>
  **)**

  Monitoring time in seconds during which the module has not received any frames from the master.

  When t<sub>3</sub> elapses, the module sends a test/control frame (U format) to the master.

  This parameter is intended for situations in which longer idle periods occur; in other words, times when there is no data traffic.

  Permitted range: 1 ... 255

  Default setting: 30
- **Difference (k) between N(S) and N(R)**

  The difference between the send sequence number N(<sub>S</sub>) and receive sequence number N(<sub>R</sub>) of a frame.

  The master returns the send sequence number of a frame from the module as acknowledgment, which the sending module then saves as the receive sequence number. Frames whose send sequence number is lower than the receive sequence number after the difference configured here is added are evaluated as having been successfully transferred and are deleted from the send buffer of the module.

  Permitted range: 1 ... 64

  Default setting: 12
- **Max. no. of unacknowledged data frames (w)**

  w: Maximum number of received data frames (I-APDUs), after which the oldest frame received from the master must be acknowledged.

  Permitted range: 1..8

  Default setting: 8

  The value must be less than the value of "Difference between send and receive sequence number" (k).

##### Acknowledgment with IEC protocol

###### Acknowledgment mechanisms for the protocol IEC 60870‑5‑104

**Configuration: Interface of the module &gt; "**
**Advanced options**
**" &gt;** 
**Transmission settings - IEC 60870-5**
**"**

With each sent data frame, the RTU sends a continuous send sequence number. The data frame initially remains stored in the send buffer of the module.

Upon reception, the master sends the send sequence number from this or (if several data frames are received) the last data frame back to the module as an acknowledgment. The module stores the send sequence number returned by the master as the reception sequence number and uses it as an acknowledgment.

Data frames whose send sequence number is equal to or less than the current receive sequence number are evaluated as successful and deleted from the send buffer of the module.

**Parameters:**

- **k:** 
  **Difference between send sequence number N(S) and receive sequence number N(R)**

  Maximum number of unacknowledged data frames (I‑APDUs) as maximum difference between send sequence number N(S) and receive sequence number N(R).

  If k is reached and t<sub>1</sub> has not yet expired, the module does not send any data frames until all sent data frames have been acknowledged by the master.

  When k is reached and t<sub>1</sub> has elapsed, the TCP connection is terminated.
- **w:** 
  **Max. number of unacknowledged data frames**

  Maximum number of received data frames (I-APDUs), after which the oldest data frame received from the master must be acknowledged.

**Recommendations of the specification:**

- w should not be greater than 2/3<sub> </sub>k.
- Recommended value for k: 12
- Recommended value for w: 8

##### IEC-specific parameters

The following parameters can be found in the parameter groups for the master or station settings.

Some parameters are also displayed in the connection editor of the telecontrol connections and can be edited there in part.

###### IEC master

You can find the following parameters in the "Settings IEC master" parameter group of the interfaces of the communications module configured at the "IEC" network type and the "Master station" and "Station" network node types.

The two following parameters can also be configured at an interface of the network node type "Station" because messages from data points with "Master function" can be sent via these; see [DNP3 and IEC data points](#dnp3-and-iec-data-points).

- **Polling basic interval**

  This is where you define the basic interval for station calls by the master station.

  Value range: 0 ... 65535 seconds

  Default: 30

  With the setting 0 (zero), the function is disabled. No cyclic polling takes place, not even for the parameters listed below, the calculation of which is based on the polling basic interval.

  The basic interval is used for the calculation of the following parameters in the connection configuration:

  - Interval for general request
  - Interval for counter general request
  - Interval for group request
  - Interval for counter group request
- **Max. number of events per call**

  Maximum number of events that can be sent in the response telegram of the station after being called by the master station.

  Range of values: 0 ... 65535

  Default: 0

  With the setting 0 (zero), the function is disabled (no limitation).

###### IEC station

You can find the following parameters in the "Settings IEC station" parameter group of the relevant interfaces of the communication module.

**Station parameters**

- **Transmission mode**

  This parameter determines whether ASDUs (events) of this station may be sent spontaneously to the master station.

  Range of values:

  - Unsolicited transfer

    The module can send spontaneous ASDUs (cause of transmission &lt;3&gt;).
  - No spontaneous transfer

    The module does not send spontaneous ASDUs.

  Default: Unsolicited

  > **Note**
  >
  > **Collisions on full duplex dedicated lines**
  >
  > If you connect a serial interface to a dedicated line with the "half-duplex" connection type, you must disable spontaneous transfer.
  >
  > To avoid collisions, you should also disable Unsolicited transfer when connecting to full duplex multidrop dedicated lines.
- **Polling mode**

  This is where you define the mode in which the master station calls the station.

  The value configured for the station is transferred to the master station and stored there.

  Range of values:

  - Cyclic

    The station is called cyclically.

    The cycle time is determined by the master's "Class 0 polling interval" parameter.
  - Only after startup or connection re-establishment

    The station is only called after the initial startup and after a restart.

###### Other parameters

- General IEC-specific parameters

  See "Transmission settings - IEC 60870-5" for the respective interface of the module.
- Response to general request / Assignment to group request

  In the data point configuration, see section [DNP3 and IEC data points](#dnp3-and-iec-data-points).
- Call intervals

  In the connection configuration, see section [Request options (IEC)](#request-options-iec).

## Additional information on mobile wireless CPs

This section contains information on the following topics:

- [CP 1242‑7 (6GK7 242‑7KX30‑0XE0)](#cp-1242-7-6gk7-242-7kx30-0xe0)
- [Wake-up of cellular CPs](#wake-up-of-cellular-cps)
- [Preferred mobile wireless networks](#preferred-mobile-wireless-networks)

### CP 1242-7 (6GK7 242-7KX30-0XE0)

This section contains information on the following topics:

- [Operating modes of CP 1242-7](#operating-modes-of-cp-1242-7)
- [Connection establishment with a CP 1242-7](#connection-establishment-with-a-cp-1242-7)

#### Operating modes of CP 1242-7

##### Modes of the CP

CP 1242‑7 (6GK7 242‑7KX30‑0XE0) allows an S7‑1200 to communicate as a GPRS station with a master or other remote networks via the GSM network. For communication using GPRS, the CP is set to one of the following operating modes:

- **Telecontrol**

  This operating mode of the CP allows the GPRS station to exchange data with the following partners:

  - Communication with the Telecontrol server

    This CP mode allows the GPRS station to exchange data with a telecontrol server.

    The Telecontrol server is a PC connected to the Internet with the "TCSB" application. It is generally located in the master station and is used for monitoring and control of the remote GPRS stations. Via the integrated OPC interface, data can be exchanged with the OPC client of a central control system.

    The Telecontrol server PC is not configured in STEP 7. The "TCSB" application has its own configuration user interface.
  - Communication with another remote GPRS station

    The data is transmitted via the Telecontrol server.
  - Communication with an engineering station (for TeleService)

  Communication with the Telecontrol server is performed via the GSM network and the Internet.

  This operating mode requires a SIM card with GPRS service enabled and a Telecontrol server that can be reached by the CP.
- **GPRS direct**

  This operating mode of the CP is used for direct communication between remote stations via the GSM network. No Telecontrol server is required.

  To allow network nodes in public wireless networks to be directly accessible, these need to be addressed using a fixed address. Here, SIM cards with a fixed IP address are used that allow the stations to address each other directly.

  The possible communications services and security functions (for example VPN) depend on what is offered by the network provider.

  Possible communications partners of the station with a CP 1242‑7 in "GPRS direct" mode are:

  - A node that can be reached by the CP via an IP address (S7 station with CP 1242‑7)
  - An engineering station (for TeleService)

---

**See also**

[Connection establishment with a CP 1242-7](#connection-establishment-with-a-cp-1242-7)

#### Connection establishment with a CP 1242-7

##### Connection modes of CP 1242‑7 (6GK7 242‑7KX30‑0XE0)

- "GPRS direct" mode

  There are no different connection modes in the "GPRS direct" mode.
- "Telecontrol" mode

  The CP can be configured for the following connection modes.

  - "Permanent" connection mode

    There is a permanent TCP connection to the telecontrol server. Following connection establishment, there is a permanent TCP connection to the telecontrol server even if data is not transferred permanently.
  - "Temporary" connection mode

    A connection is only established to the telecontrol server when required.

If a TCP connection is established, process data is sent as soon as the telecontrol instructions are called on the CPU.

A connection is always established by the CP. If a connection established by the CP is interrupted, the CP automatically attempts to re-establish the connection.

##### Establishing a connection at permanent stations ("Telecontrol" mode)

In the "Telecontrol" mode, the permanent connection to the telecontrol server is established when the station starts up. If there is an interruption on the connection, the establishment of the connection can be triggered by a wake-up SMS (see below).

##### Establishing a connection at temporary stations ("Telecontrol" mode)

With temporary stations, connection establishment can be triggered by the following events:

- Event on the local CPU that needs to be evaluated by the program.

  In terms of the program, two situations need to be distinguished:

  - Events that lead to a single connection establishment (for example alarms or commands from the operator).
  - Expiry of an interval that leads to cyclic connection establishment (for example once daily for data transmission)
- Request by a communications partner (OPC client or S7 station)

  The request from the communications partner leads to the connection being established.
- Request for TeleService by an engineering station

  The request switched by the telecontrol server or TeleService gateway does not need to be evaluated in the program.
- Wake-up SMS of the telecontrol server

  The wake-up SMS can be triggered spontaneously on the telecontrol server. It is also possible to configure cyclic sending on the telecontrol server.
- Telephone wake-up call

  The wake-up call can be sent from a telephone that has a phone number authorized in the STEP 7 project. The telephone must support the CLIP function (transfer of its own call number).

  The connection establishment with the (main) telecontrol server is triggered.
- Telephone wake-up SMS

  The wake-up SMS can be sent from a telephone that has a phone number authorized in the STEP 7 project. The telephone must support the CLIP function (transmission of its own number) and sending of SMS.

  The connection establishment with the telecontrol server specified in the SMS is triggered.

When a temporary station is woken up, all the data is transferred if this has changed since the last data transfer.

##### Wake-up call / wake-up SMS in the "Telecontrol" operating mode

For wake-up call or wake-up SMS, see section [Wake-up of cellular CPs](#wake-up-of-cellular-cps).

##### Establishing a connection in "GPRS direct" mode

In "GPRS direct" mode, a connection establishment is triggered by the following events:

- Event on the local CPU that is evaluated by the program.
- Request by a communications partner (not an engineering station)

  The request from the communications partner is evaluated in the program by calling the telecontrol instructions.
- Request for TeleService by an engineering station

  The request switched by the telecontrol server or TeleService gateway does not need to be evaluated in the program.

### Wake-up of cellular CPs

#### Right to wake-up by "Authorized phone numbers"

The CP only accepts a wake-up SMS or a wake-up call if the sending communication partner is authorized based on its phone number. These numbers are in configured for the CP in STEP 7 in the "authorized phone numbers" list.

> **Note**
>
> **"Authorized phone numbers" in the STEP 7 project**
>
> - A phone number entered here gives the sender who transfers this phone number the right to trigger connection establishment.
> - If an asterisk (*) is entered in the list, the CP accepts SMS messages from all senders.
> - If the list is empty, the CP cannot be woken up for connection establishment.

#### Wake-up SMS

Depending on the connection type and the triggering server or intermediary TeleService server, the following text must be transferred in the wake-up SMS:

- For telecontrol connections:

  - Text for the wake-up SMS message for establishing a connection to the telecontrol server:

    `TELECONTROL`
  - Text for the wake-up SMS message for establishing a connection to the main telecontrol server:

    `TELECONTROL MAIN`
  - Text for the wake-up SMS message for establishing a connection to the substitute telecontrol server:

    `TELECONTROL BACKUP`

  The configuration of the telecontrol server for the GPRS CP is set in STEP 7 in "Telecontrol interface &gt; Operating mode &gt; main or substitute telecontrol server".

  > **Note**
  >
  > **Wake-up with a mobile phone**
  >
  > - One of the texts listed above can be used in a wake-up SMS message.
  > - With a wake-up call, the station always connects to the main telecontrol server.
- For TeleService connections:

  - Text for the wake-up SMS message for establishing a connection to the first configured TeleService server:

    `TELESERVICE`

    or

    `TELESERVICE 1`
  - Text for the wake-up SMS message for establishing a connection to the second configured TeleService server:

    `TELESERVICE 2`

  The configuration of the TeleService server for the GPRS CP is set in STEP 7 in "Telecontrol interface &gt; TeleService authorization &gt; 1st or 2nd TeleService server".

### Preferred mobile wireless networks

#### Selection of the preferred mobile wireless networks

The following options are available to select the networks that the mobile wireless CP should preferably dial up:

- Automatic

  The CP dials with highest priority into the mobile wireless network of the contracted network provider set on the SIM card. If a dialing up the contract network fails, the CP dials up other mobile wireless networks with which the network provider has roaming contracts and whose access data is stored on the SIM card.
- Contract network only

  The CP only dials up the mobile wireless network of the contract network provider whose SIM card is plugged into the CP. No roaming.
- Contract network and preferred networks

  The CP dials up the contracted network with the highest priority. If dialing up the contract network is unsuccessful, the CP dials up alternative mobile wireless networks, in decreasing priority, as entered in the list of preferred network providers.

  The alternative networks are entered in the list as "Public Land Mobile Network" (PLMN). PLMN is a construct of Mobile Country Code (MCC) and Mobile Network Code (MNC).

  Example: 26276  
  This is the PLMN for the test network of Siemens AG with MCC = 262 and MNC = 76.

## Online & diagnostics

This section contains information on the following topics:

- [Download from device with CP 1243-8 IRC (V2.1)](#download-from-device-with-cp-1243-8-irc-v21)
- [Message protocol diagnostics](#message-protocol-diagnostics)
- [TeleService via mobile wireless](#teleservice-via-mobile-wireless)

### Download from device with CP 1243-8 IRC (V2.1)

#### Restrictions when downloading from a CP 1243‑8 IRC

When you download the configuration data from a CP 1243‑8 IRC using the online functions, the following data will not be fully downloaded:

- Partner station data
- Configuration and partner data of the data points
- References to PLC tags related to communication partners

In order to use the STEP 7 project after a complete download from the devices, you need to download the original export files from STEP 7 V5 with the configuration data of proxies into each CP 1243‑8 IRC (Import partner configuration).

### Message protocol diagnostics

This section contains information on the following topics:

- [Message protocol: Structure and functions](#message-protocol-structure-and-functions)
- [Details](#details)

#### Message protocol: Structure and functions

The "Message protocol" function is used to record transferred message frames.

See the "Operation" paragraph below for information on activating the function.

##### Structure of the "Message protocol" dialog

After activation, the columns show the following data:

- No.

  - Symbol for incoming or outgoing message frames
  - Message frame number, consecutive
- Block

  Length of the message frame block in which the message frame was transferred.
- Header fields

  Hexadecimal display of some header data

  For the meaning, see section [Details](#details).
- Subscriber (source / destination)

  Subscriber numbers of the sending (source) and receiving (destination) subscriber
- Object (source / destination)

  Object number of the data object in the message frame for source and destination subscriber
- Index

  Address parameters for net data in data messages (channel number)
- Date, time and status

  Time stamp of message frame and time status from time of transfer

  For information on the display, see section [Details](#details).
- Net Data

  Hexadecimal display of the net data of the message frame

  For the meaning, see section [Details](#details).

##### Operation

You operate the function using the three buttons underneath the dialog described above.

- Enable

  Clicking the button starts logging of the transferred message frames.

  400 message frames are recorded per recording cycle. A maximum of 10000 message frames can be stored in a circular buffer.
- Save

  Saves the recorded message frames in a binary file. You define the storage location using the button.
- Refresh

  Updates the recording; a new recording cycle is started.

#### Details

##### Detailed information

**Header fields**

The 5 fields output in hexadecimal format have the following meaning:

- 1st field: Message counter

  0...7
- 2nd field: Control code
- 3rd field: Function selection

  - 0: Processing in TIM
  - 1: Processing in CPU
- 4th field: Address extension

  - 0: ST1 message without address extension
  - 1: ST1 message with address extension
  - 2: ST7 message
- 5th field: Direction bit

  - 0: Monitoring direction
  - 1: Control direction

**Net Data**

The column shows the net data of the message frame.

The values are displayed in hexadecimal format.

**Date, time and status**

The column shows the time stamp of the message frame in the following format:

Year/Month/Day_Hour:Minute:Second_Time status

Assignment of the time status:

- 2<sup> 0</sup>

  - 0: Time is invalid
  - 1: Time is valid
- 2<sup> 1</sup>

  - 0: Standard time
  - 1: Daylight saving time
- 2<sup> 2</sup>

  Not used
- 2<sup> 3</sup>

  - 0: No meaning
  - 1: Notification time for daylight saving/standard time changeover

    Only in time synchronization message frame

### TeleService via mobile wireless

This section contains information on the following topics:

- [Download using TeleService](#download-using-teleservice)
- [TeleService via telecontrol](#teleservice-via-telecontrol)
- [Establish remote connection via telecontrol](#establish-remote-connection-via-telecontrol)
- [Status](#status)

#### Download using TeleService

The following behavior applies to all mobile wireless CPs:

- CP 1242‑7 (6GK7 242‑7KX30‑0XE0)
- CP 1242‑7 GPRS V2 (6GK7 242‑7KX31‑0XE0)
- CP 1243‑7 LTE‑EU (6GK7 243‑7KX30‑0XE0)
- CP 1243‑7 LTE‑US (6GK7 243‑7SX30‑0XE0)

##### Connection resources for TeleService

The TeleService function occupies a connection resource on the engineering station.

The function download to device or upload from device during a TeleService session occupies a second connection resource on the engineering station.

##### Download to device

Only use the "Download to device" function with the mobile wireless CP via a TeleService connection as follows:

1. Select the CP in STEP 7.
2. Select the "Online" &gt; "Download to device" menu.
3. In the "Extended download" dialog that appears, select the TeleService interface.
4. Download the project data from the "Extended download" dialog.

##### Download from device

The "Download from device" function via a TeleService connection is supported by the mobile wireless CPs with the following TeleService server applications:

- TeleControl Server Basic as of version V3
- TeleService Gateway as of version V3

#### TeleService via telecontrol

##### Communication path for TeleService via telecontrol

With TeleService via telecontrol, the connection between the engineering station and a remote S7 station always runs through a TeleService server as an intermediary.

The request for connection establishment is triggered by the engineering station and forwarded by the TeleService server. Depending on the available communication paths to the station, the TeleService server forwards the request to the next station via LAN or by a wake-up SMS. The telecontrol CP in the S7‑1200 station establishes a connection to the engineering station via the TeleService server.

An alternative intermediary (TeleService server) is:

- A telecontrol server

  The telecontrol server can be a separate PC or installed on the engineering station in the form of the "TCSB" application.
- A TeleService gateway

  A TeleService gateway is used when no telecontrol server is available.

The TeleService server can be connected to the engineering station via LAN or Internet and the TeleService function can be called from there.

##### Requirements for TeleService via telecontrol

- A TeleService server
- The STEP 7 project with the required stations

##### Note on project engineering

The TeleService server is not configured in STEP 7.

#### Establish remote connection via telecontrol

##### Requirements for TeleService via telecontrol

For the requirements and mechanisms, see section [TeleService via telecontrol](#teleservice-via-telecontrol).

##### Start a TeleService session via telecontrol

Start TeleService via telecontrol as follows:

1. In the project on the authorized engineering station, select the remote S7 station with which you want to establish a TeleService connection via WAN.
2. Alternatively, open the "Connect online" dialog box as follows:

   - "Connect online" button
   - "Connect online" shortcut menu (right mouse button)
   - "Online" &gt; "Connect online" menu

   The "Connect online" dialog box opens.
3. Select the interface type "TeleService via Telecontrol" in the "Type of PG/PC interface" drop-down list.
4. In the "PG/PC interface" drop-down list, select the "TeleService board" option if it is not automatically displayed.
5. Click on the "Connect" icon next to the "PG/PC interface" drop-down list.

   The "Establish remote connection via telecontrol" dialog box opens.
6. Make the necessary settings in this dialog.

   Details of this are contained in the tooltip cascade of STEP 7.

The following details are required to successfully establish a connection:

##### Details required to establish a connection with the S7 station

The following information is necessary in the Establish remote connection" dialog:

- IP address or DNS name of the telecontrol server
- TCP port number of the telecontrol server or the DSL router via which the connection between the engineering station and the remote S7 station is running.
- Server password of the ES to authenticate the engineering station at the telecontrol server

  Only required if a group-specific password has been configured in the "TCSB" application.
- TeleService user name

  See CP configuration in STEP 7.
- TeleService password

  See CP configuration in STEP 7.
- Access ID of the CP

  Only required when there are several telecontrol CPs in the station. See CP configuration in STEP 7.

#### Status

##### Connection states with TeleService via telecontrol

The connection states described below can be displayed in the "Establish remote connection via telecontrol" dialog box.

**When opening the dialog**

- Not connected

  There is no connection to the remote S7 station. Connection establishment has not yet started.

**When establishing a connection**

If connection establishment was started by clicking the "Connect" button, the following states are displayed one after the other after the connection has been established:

- Connect to telecontrol server

  The engineering station connects to the telecontrol server.
- Wait for S7 station

  The wake-up SMS has been sent to the remote station. Wait for reply from station.
- Authentication at S7 station

  The S7 station has established an IP connection with the engineering station via GPRS and Internet and is checking the received logon and authentication data.
- Connected

  The station has successfully established the connection to the engineering station.

**If connection establishment is unsuccessful**

The following states may be displayed if the connection cannot be successfully established:

- Telecontrol server not accessible

  Possible causes:

  - The connection between the engineering station and the telecontrol server has been interrupted.
  - The telecontrol server is switched off.
- Wrong server password

  Cause: The wrong server password for logging on and authentication was entered at the telecontrol server.
- S7 station not responding

  Possible causes:

  - The communication between the telecontrol server and the station is disrupted.
  - There is a disrupted connection between the mobile wireless network and the Internet.
  - Faulty Internet connection.
  - The telecontrol server could not send a wake-up SMS.
  - The CP has not received a wake-up SMS.
  - The sender of the SMS was not configured in the list of authorized wake-up call numbers.
- Wrong TeleService user name or TeleService password

  Possible causes:

  - An incorrect TeleService user name or incorrect TeleService password was entered in the authentication dialog for the CP.
  - The TeleService user name or TeleService password was not configured in STEP 7.
- All TeleService access points are in use.
- The CP is not known to the telecontrol server.

  Cause: The CP originates from a STEP 7 project that does not match the project of the telecontrol server.
- No resources available for TeleService on the CP: Please contact the hotline.
- Protocol error

  Cause: Incompatible data or data from incompatible subscriber. Please contact the hotline.

## Block library Telecontrol ST7

This section contains information on the following topics:

- [Creating a library](#creating-a-library)
- [Structure of the library](#structure-of-the-library)
- [Generating, using and calling the blocks](#generating-using-and-calling-the-blocks)
- [Note on the "BasicTask_*" FCs](#note-on-the-basictask_-fcs)
- [Structure of user program for TD7onCPU](#structure-of-user-program-for-td7oncpu)
- [Types](#types)
- [Master copies (S7-300/400, S7-1500)](#master-copies-s7-300400-s7-1500)

### Creating a library

#### Delivery form of the block library

The program blocks of the TD7onCPU library are used as a global library for STEP 7.

The library is available archived and compressed on the Internet at the following address:  
[Link:](https://support.industry.siemens.com/cs/ww/en/ps/24710/dl)

The file name has the following structure: Telecontrol_ST7_&lt;Version&gt;.exe

> **Note**
>
> **Migration of the library**
>
> If you update an older version of the block library to the current version, some error messages may occur in STEP 7 during this process. These are system-related and do not mean that the migration will fail.

#### Creating the library

Proceed as follows:

1. Create a suitable directory in the STEP 7 installation directory of your engineering station, for example with the name "Telecontrol ST7".
2. Save the library in this directory.
3. Run the "*.exe" file.

   The self-extracting library is stored as a zip archive in a selectable directory.
4. Unzip the file.

   The library is now available as an archived global library under the name "Telecontrol ST7.zal&lt;version&gt;" together with the readme files.
5. Open the STEP 7 project.
6. In the "Options" menu, select the command "Global libraries &gt; Retrieve library".

   The "Retrieve archived global library" dialog opens.
7. Select the folder and the library archive.

   Recommendation: Leave the "Open read-only" option activated to download the global library read-only.
8. Click Open.

   The "Select target directory" window opens.
9. Select the target directory (your project) to which the archived global library is to be unpacked (select folder).

   The library is unpacked.

   If you are working with a newer STEP 7 version, you will be asked whether you want to upgrade the library. Confirm this using the "Upgrade" button.

The library is opened after unpacking.

You can find the library in the STEP 7 project in the library view (task card) in the "Global libraries" pane under the name "Telecontrol ST7_&lt;Version&gt;".

### Structure of the library

#### Structure of the global library

The opened library contains the following directories:

- **Types**

  - PLC data types (UDT)

    Here you will find the PLC data types (UDTs) used by the libraries.
  - System data types (SDT)

    Here you will find the system data types used by the libraries.
- **Master copies**

  You can find the following program blocks here:

  - **CPU300/400**

    Program blocks for the S7-300/400 CPU
  - **CPU1500**

    Program blocks for the S7-1500 CPU

**Master copies**

The two libraries under "Master copies" for S7-300/400 and S7-1500 are divided into the following folders:

- Data point typicals

  Data point typicals (blocks) for transferring data
- Optional blocks

  Optional blocks that you can use when necessary.
- System blocks

  Blocks that are used for basic communication.

  Depending on the SIMATIC product series used, you can find the following auxiliary blocks for communication between TIM and CPU in separate folders:

  - BCom

    Blocks for processing the communication mailbox of the S7‑400 and S7‑1500

    Blocks for processing the communication compartment of the S7‑300 (from version V3.0 SP2 of the block library)
  - PCom

    Blocks for processing the communication mailbox of an S7‑300 with P bus (CPU without partyline)
  - XCom

    Blocks for processing the communication mailbox of an S7‑300 with X connections

### Generating, using and calling the blocks

#### Generating TD7onCPU blocks

Once you have opened the TD7 library in the pane "Global libraries" under the name "Telecontrol ST7", you can generate the blocks for basic communication for one or more CPUs.

**Requirements**

The following requirements must be met before generating the blocks:

- The communications modules must be networked with each other.
- Valid telecontrol connections must be created between the communication partners involved.
- A TIM 1531 IRC must be networked with a CPU via Ethernet.
- A TIM 1531 IRC cannot be assigned to a CPU.

  The "Assigned CPU" field in the "Subscriber numbers" parameter group must be empty.
- No data point can be created in the TIM whose CPU is to use TD7onCPU.
- No message can have been created already in the message editor of the TIM.
- The "Telecontrol ST7" library must be open (visible) in the "Global libraries" task card.

**Different requirements for modules with imported configuration data**

Note the other requirements for communications modules whose SINAUT configuration was imported from a STEP 7 V5 project. With these modules, the option "Telecontrol configuration" is set to "Import" in the parameter group "Basic settings &gt; Configuration".

These modules have different requirements for generating the blocks:

- No ST7 telecontrol connections need to be created between the communication partners involved.

  The relevant information is stored in the imported configuration data.
- The CPU of the communications module must have the same IP address as in the STEP 7 V5 project. The CPU is assigned to the communications module via its IP address.

**Procedure for generating**

Generate the blocks for basic communication as follows:

1. Select the desired TIM.
2. Select the shortcut menu command (right mouse button) "Generate TD7onCPU blocks".
3. In the dialog that follows, select one or more CPUs and click "Generate..."

The TD7onCPU blocks are created and compiled in the selected CPUs under the program blocks in a new "TD7onCPU" directory.

#### Using blocks

- **System blocks**

  The required blocks for basic communication are created automatically during the generation in the CPU.

  You do not need to use these blocks manually in the CPU.

  The system blocks handle central tasks such as startup, monitoring of the connections, reachability of the connection partners, entering data in the send mailbox or taking data from the receive mailbox of the communication DBs, general request, time keeping, handling communication etc.

  Communication DBs:

  - S7-300/400

    For each connection a separate communication DB is created automatically: It contains the send and receive mailbox and all the data required for controlling and monitoring this connection.
  - S7-1500

    For the CPU 1500, there is only one communication DB "BConnectData". A connection instance is stored in this DB in the "BConnection" array for each local connection.
- **Data point typicals**

  You need to use data point typicals on the relevant CPU according to the communications tasks.

  Drag the individual blocks with the mouse from the global library to the user program of the CPU. The corresponding instance data block is created automatically when using a data point typical.

  The number of the instance data block is also the source object number, which you need to specify at the corresponding partner object of the communication partner under "PartnerObjectNo". For this reason, each typical needs to use its own instance data block. You can also assign the instance DB number manually.
- **PLC data types (UDT)**

  - Dat256D_S / Dat256D_R

    Copy also the UDT "TransmitBlock" for these typicals from the library (Types &gt; PLC data types (UDT)) into the "PLC data types"directory of the CPU. The UDT is not automatically referenced by the typical.
- **Optional blocks**

  You should also use the optional blocks on the CPU depending on the communications tasks of the station.

  Drag the individual blocks with the mouse from the global library to the user program of the CPU.

#### Call in the user program

- **System blocks**

  Only the two following FCs need to be called in the user program:

  - StartUp

    Call the FC in the startup OB. The block has no parameters.

    To be able to call the FC StartUp, you must first create the startup OB (OB100).
  - BasicTask

    Call the FC in the cyclic OB or user program.

    The DB BasicData is created automatically. The DB contains all the centrally required data including the records of all communication partners and the connections to be managed.

    For information on the various "BasicTask" FCs, see section [Note on the "BasicTask_*" FCs](#note-on-the-basictask_-fcs).
- **Data point typicals**

  Depending on the communication tasks, call up all required data point typicals in the user program.
- **Optional blocks**

  Depending on the communication tasks, call up all required optional blocks in the user program.

See also section [The cyclic SINAUT program](#the-cyclic-sinaut-program) for information on calling the blocks.

> **Note**
>
> **Error display for library conformance**
>
> In the "Compilation" parameter group of blocks, an error can be displayed under the entry "Library conformance" (call of single instances). This is caused by the call of global data blocks, for example, DB BasicData.
>
> Since the "Telecontrol ST7" library has no "know-how protection", you can ignore these error notifications.

### Note on the "BasicTask_*" FCs

#### Versions of the "BasicTask" FC

There are different versions of the "BasicTask" FC in the TD7 block library "Telecontrol ST7" for STEP 7 Professional.

Depending on the SIMATIC product series and the backplane bus, the FCs have a different suffix at the end of the block name:

- **BasicTask_B**

  For S7‑1500 CPU
- **BasicTask_B**

  For S7‑300 and S7‑400 CPU
- **BasicTask_X**

  For S7‑300 PU with partyline
- **BasicTask_P**

  For S7‑300 CPU without partyline

Party line CPUs are: CPU 312.. / 313.. / 314.. / 315.. to CPU 315‑2 DP and C7 devices.

For the block description, see section [BasicTask_* FC](#basictask_-fc).

#### "BasicTask" label for three FCs

References to the respective FC are made in many places in the following sections. Since the description of the different blocks usually applies to several SIMATIC product series, the three FCs are referred to hereafter as "BasicTask". The FC version for the relevant CPU type is meant in each context.

### Structure of user program for TD7onCPU

This section contains information on the following topics:

- [The cyclic SINAUT program](#the-cyclic-sinaut-program)
- [Cyclic interrupt OB](#cyclic-interrupt-ob)
- [Programming error OB](#programming-error-ob)

#### The cyclic SINAUT program

##### Introduction

The structure of the TD7 blocks in the user program (OB1) is explained below.

The TD7 blocks must be proceeded in every OB1 cycle. Keep to the call sequence of the blocks unless instructed otherwise.

Other user-specific parts of the program can be linked in before or after the TD7 blocks in OB1 or, if practical, within the TD7 blocks.

You can structure the SINAUT-specific part in OB1 by calling it in lower-level FCs.

All data point typicals are FBs. An instance DB must be specified when an FB is called. The number of this instance DB is identical to the object number of the data point object.

##### The structure of the TD7 blocks in OB1

| Cyclic OB1 |  |
| --- | --- |
| **BasicTask** | The respective FC BasicTask must always be called at the start. It handles basic SINAUT tasks that are always required. |
| **Optional SINAUT basic functions** | After FC BasicTask, call the following optional blocks (FCs) if you need them:  - ListGenerator   Creation of address lists for received frames with incomplete destination address. - TimeTask   Provides the time of day. |
| If necessary, call additional optional FCs in the subsequent program execution, for example:  - Trigger   Scheduled start of user programs and data frames - PartnerStatus   Display the status of partners - PartnerMonitor   Extended subscriber-specific display and control options. - PulseCounter   Count pulse acquisition - PathStatus   Display the status of the connection path to a partner    **Note:**  The following two blocks may not be called explicitly, since they are activated via an internal interface.  - TestCopy - TestcopyDB |  |
| **Data point typicals** | In the subsequent program execution, call the data point typicals for sending and receiving data. The sequence of the individual typicals is unimportant.  The number of typicals to call and the required types depend on the amount and type of data to be sent and received.   **Note:**  The instance DBs of these FBs are referenced using the partner object number of the communication partner. |

##### Example of a TD7 program for a station

| Cyclic OB1 |  |
| --- | --- |
| **BasicTask** | The respective FC BasicTask must always be called at the start of the cyclic program.  Generally, data is ready for further processing after it has been received.  The FC has only one parameter, "UserFC". Normally 0 can be specified. If you require user-specific processing for received data, specify here the number of an FC containing the program for this processing.  You can also copy received data chronologically to an archive memory via this interface. |
| **TimeTask** | As an option, you can call the FC TimeTask immediately after FC BasicTask. The FC has no parameters. FC TimeTask TimeTask must be included if you need the time of day. This allows data frames to be time-stamped.  However, you can also use the time of day to start program components at a specific point in time or to schedule the transmission of data frames. FC Trigger, described below, is then required.  For this FC Time Task to be used, the CPU must be provided with the time from a local TIM module. You specify this in the configuration. |
| **Trigger** | FC Trigger can be included as an option. The FC sets its output for the duration of one OB1 cycle when the point in time or the time interval set for the FC has been reached.  The FC can be inserted several times if several times or various time intervals are required. Using the FC requires that FC TimeTask must be called first in the OB1 program (see above) and the CPU time must have already been set once. |
| **PartnerStatus** | FC PartnerStatus can be included as an option. The FC shows the reachability for a maximum of 8 communications partners. |
| **ListGenerator** | - ListGenerator300 for S7-300 CPU - ListGenerator400 for S7-400 CPU - ListGenerator1500 for S7-1500 CPU  The FC can be installed as an option. The FC is required if the station receives frames containing no destination address or an incomplete destination address. This happens if the configuration of the destination address has been completely or partially omitted in a partner for data point typicals. ("PartnerNo" and "PartnerObjectNo" were not specified, so transmission to all known destination subscribers takes place.) |
| **PulseCounter**    **PathStatus**    **PartnerMonitor** | When necessary |
| **Data point typicals** | Following the FCs for SINAUT basic tasks, data point typicals for sending and receiving data are called. The sequence of the individual typicals is unimportant. The number of typicals to call and the required types depend on the amount and type of data to be sent and received.  For one station applies:  - The following are typically sent:   - Binary information, such as status messages and alarms   - Analog values   - Counted values   - Additional data if necessary - The following are typically received:   - Commands   - Setpoints, parameters |
| **Bin04B_S** | One or more FBs for the acquisition and transfer of binary information, such as messages, alarms, etc. |
| **Ana04W_S** | One or more FBs for the acquisition and transfer of analog values |
| **Cnt01D_S / Cnt04D_S** | One or more FBs for the acquisition and transfer of counted values  A requirement for the use of the FBs is that FC PulseCounter is included in a cyclic interrupt OB, e.g. OB35. This FC is responsible for the time-driven acquisition of counted pulses in the background. |
| **Cmd01B_R** | One or more FBs for receipt and output of commands. |
| **Set01W_R /  Par12D_R** | One or more FBs for receipt and output of setpoints, limit values or parameters.. |
| **Dat12D_S /  Dat256D_S** | One or more FBs for the acquisition and transmission of 1 to 12 or up to 256 data double words with any informational content  There is no data-specific processing and change control for these typicals. The user program is responsible for this. As an option change control can be activated that triggers a transfer with each bit change. |

##### TD7 programs for master stations and node stations

In principle, the TD7 programs of master stations and node stations look the same as for a station. The corresponding receive typicals are used in a central station for the send typicals of a station, the corresponding send typicals are used in a central station for the receive typicals of the station.

In a node station, both send typicals and the corresponding receive typicals are used according to the transmission direction.

In the master station it is practical to structure the OB1 program according to stations, in other words, all data typicals belonging to the same station are called in one FC. The best overview is provided when the number of the FC is identical to the subscriber number of the station.

#### Cyclic interrupt OB

##### Introduction

Only include time-controlled TD7 blocks in a CPU if fast count pulses must be detected in this CPU which could not be reliably detected within an OB1 cycle due to an excessively long cycle time.

The count pulses are acquired via any digital input module. To acquire the pulses reliably, the digital inputs use must be queried for change at a fixed time interval. The time interval is based on the duration of the shortest count pulse. The minimum count pulse duration may be 50 ms. The same applies to the duration of the pause. This results in a maximum count frequency of 10 Hz.

The time interval in which the count pulse acquisition is performed must be approximately half the count pulse duration, this means at an interval of approximately 25 ms for 50 ms.

For this time-controlled count pulse acquisition, OB35 needs to be configured for an S7-300 CPU, one of the available cyclic interrupt OBs OB30 to OB38 for an S7-400 CPU, and a cyclic interrupt OB with a number from 30..38 for an S7-1500 CPU.

All cyclic interrupt OBs have a preset time interval, for OB35, for example, 100 ms. This can be changed in steps of 1 ms. This makes it possible to set a cyclic interrupt OB, for example, to 25 ms.

You change the time interval for a cyclic interrupt OB in the Properties dialog (S7‑400/1500), or in the Properties dialog of the CPU with S7-300.

In highly time-critical applications, count pulses can also be recorded in a process alarm OB of an alarm module, e.g. in OB40.

Calling FC PulseCounter in the alarm OB

| OB |  |
| --- | --- |
| **PulseCounter** | One or more FC PulseCounters can be integrated in an alarm OB for the acquisition of count pulses if several count pulses can occur during an OB1 cycle and are to be acquired.  FC PulseCounter processes up to 8 pulse inputs of any digital input. The acquired count pulses are added together in programmable SIMATIC counters. These access the function blocks that put together the count value frames (FB-Cnt0x_S). |

#### Programming error OB

##### Validity

Only for S7-300/400

##### Function

When a block that does not exist is called in an S7​‑300/400 CPU, the CPU normally changes to STOP. The diagnostics buffer indicates which FB, FC or DB was missing. You can then reload the missing block and restart the CPU.

If, however, you do not want the CPU to change to STOP if there is a missing block or only changes to STOP when certain block types or block numbers are missing, you can specify the reaction you require in OB121.

Even if you have loaded OB121 as an empty block on the CPU, this is enough to have the CPU continue running if a block is missing. If you want to decide more selectively when the CPU should continue running or change to STOP, include OB121 in the user program.

In conjunction with SINAUT ST7 it is possible that a CPU changes to STOP when it receives data from another CPU that it does not (or not yet) know. This is, for example, the case when you add a data point typical to a station and give it a complete destination address (destination subscriber no. plus destination object no.). The specified destination object no. can lead to a stop on the destination subscriber in the following situation:

- As soon as you have installed a new data point typical in a station, the data is transferred to the destination.
- If there is no corresponding receive typical installed on the destination CPU, the destination object no. (= instance DB of the received typical) does not exist.

The result is that the CPU changes to STOP as soon as the data is received.

To avoid this it is advisable to call FC ST7ObjectTest in OB121.

Call of FC ST7ObjectTest in the programming error OB

| OB121 |  |
| --- | --- |
| **ST7ObjectTest** | Calling FC ST7ObjectTest in OB121 prevents a CPU STOP, if the CPU receives data with an unknown destination object no.  Other calls can be included at any point in OB121 regardless of the FC ST7ObjectTest call.  FC ST7ObjectTest has a parameter "StopInOtherCases". Here you can specify what happens in other situations (STOP or continue running) if OB121 was called because another data block or an FB or FC is missing. |

### Types

This section contains information on the following topics:

- [Note on data types](#note-on-data-types)
- [PLC data types (UDT)](#plc-data-types-udt)
- [System data types (SDT)](#system-data-types-sdt)

#### Note on data types

The following data types are used in blocks of the S7-300/400 and S7-1500.

#### PLC data types (UDT)

This section contains information on the following topics:

- [UDT](#udt)

##### UDT

###### UDTs used

The following PLC data type (UDT) is used by the block library:

- TransmitBlock

  UDT for the data transfer between the CPU and TIM

  When using the "Dat256D_S / Dat256D_R" typical, copy the UDT into the "PLC data types" directory of the respective CPU. The UDT is not automatically referenced by the typical.

  The UDT does not require any parameter assignment.

#### System data types (SDT)

This section contains information on the following topics:

- [SDTs](#sdts)

##### SDTs

###### SDTs used

The following system data types (SDTs) are used by the DB BasicData and stored automatically in the directory "PLC data types" of the CPU when generating/compiling the TD7 blocks:

- ConnectionDescription

  SDT is part of the "BasicData" DB and has an "Array[1..1] of ConnectionDescription" data type. It contains the following details for the connection description:

  - Number of the configuration DB
  - Connection type
  - CFB number in the case of an S7 connection
  - Subscriber number of the local TIM.
- SubscriberObject

  SDT is part of the "BasicData" DB and has an "Array[1..1] of SubscriberObject" data type. It contains the following information about the communication partner:

  - Subscriber number of the partner
  - Array index of the connection description
  - Subscriber type
  - Information whether the partner is local or remote.

### Master copies (S7-300/400, S7-1500)

This section contains information on the following topics:

- [Note on master copies](#note-on-master-copies)
- [Data point typicals](#data-point-typicals)
- [Optional blocks](#optional-blocks)
- [System blocks](#system-blocks)

#### Note on master copies

##### Validity

The following program blocks are located in the master copies of the global library:

- **CPU300/400**

  Program blocks for the S7-300/400 CPU
- **CPU1500**

  Program blocks for the S7-1500 CPU

The blocks are largely identical. Unless otherwise stated, the description applies equally to the blocks of the S7-300/400 and S7-1500.

If individual blocks cannot be used for all SIMATIC product series mentioned or if functions for the SIMATIC product series differ, this is expressly indicated.

#### Data point typicals

This section contains information on the following topics:

- [Types and overview of the data point typicals](#types-and-overview-of-the-data-point-typicals)
- [Reoccurring parameters](#reoccurring-parameters)
- [Time stamp](#time-stamp)
- [Analog value typical Ana04R_S](#analog-value-typical-ana04r_s)
- [Analog value typical Ana04R_R](#analog-value-typical-ana04r_r)
- [Analog value typical Ana04W_S](#analog-value-typical-ana04w_s)
- [Analog value typical Ana04W_R](#analog-value-typical-ana04w_r)
- [Binary value typical Bin04B_S](#binary-value-typical-bin04b_s)
- [Binary value typical Bin04B_R](#binary-value-typical-bin04b_r)
- [Command typical Cmd01B_S](#command-typical-cmd01b_s)
- [Command typical Cmd01B_FS](#command-typical-cmd01b_fs)
- [Command typical Cmd01B_R](#command-typical-cmd01b_r)
- [Command typical Cmd01B_FR](#command-typical-cmd01b_fr)
- [Command typical Cmd08X_S](#command-typical-cmd08x_s)
- [Command typical Cmd08X_R](#command-typical-cmd08x_r)
- [Counted value typicals Cnt01D_S / Cnt04D_S](#counted-value-typicals-cnt01d_s-cnt04d_s)
- [Counted value typicals Cnt01D_R / Cnt04D_R](#counted-value-typicals-cnt01d_r-cnt04d_r)
- [Data typical Dat12D_S](#data-typical-dat12d_s)
- [Data typical Dat12D_R](#data-typical-dat12d_r)
- [Data typical Dat12x1D_S](#data-typical-dat12x1d_s)
- [Data typical Dat12x1D_R](#data-typical-dat12x1d_r)
- [Data typical Dat256D_S](#data-typical-dat256d_s)
- [Data typical Dat256D_R](#data-typical-dat256d_r)
- [Parameter typical Par12D_S](#parameter-typical-par12d_s)
- [Parameter typical Par12D_FS](#parameter-typical-par12d_fs)
- [Parameter typical Par12D_S](#parameter-typical-par12d_s-1)
- [FC Safe](#fc-safe)
- [Setpoint typical Set01W_S](#setpoint-typical-set01w_s)
- [Setpoint typical Set01W_FS](#setpoint-typical-set01w_fs)
- [Setpoint typical Set01W_R](#setpoint-typical-set01w_r)

##### Types and overview of the data point typicals

###### Types of the data point typicals

Data point typicals process one or more data points of the same information type, e.g. 4 bytes of binary information, 4 analog values or 1 byte commands, etc.

When a data point typical (FB) is called the corresponding instance DB needs to be specified in which the data will be written or from which the data to be transferred will be read.

###### Transfer direction of the typicals

A data point typical for a specific type or amount of information always come in two versions:

- A typical for acquiring and sending
- A typical for receiving and outputting

When using data point typicals a distinction is therefore made according to the transfer direction:

- **Sending typicals**

  Sending typicals process data and send it to the remote partner.

  They have the ending "_S" Examples: Bin04B_S, Ana04W_S
- **Receiving typicals**

  Receiving typicals receive the data from their remote partner.

  They have the ending "_R" Examples: Bin04B_R, Ana04W_R

When transferring data on the two communicating partners there is always a corresponding pair of typicals involved.

Examples:

- Monitoring direction

  - The station sends binary data with the typical Bin04B_S.
  - The central station receives the data with the typical Bin04B_R.
- Control direction

  - The central station sends a command with the typical Cmd01B_S.
  - The station receives the command with the typical Cmd01B_R.

###### Structure of typical names

> **Note**
>
> **No SMS blocks**
>
> Unlike the block library for STEP 7 V5, there are no blocks for sending SMS in the global library "Telecontrol ST7".
>
> You configure the sending of e-mails and/or SMS in STEP 7 Professional in the TIA Portal via the message editor, see section [Configuring data points and messages](#configuring-data-points-and-messages).

The names of the data point typicals are assigned according to the following scheme:

Structure of typical names

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data point type** | **Number of values**   Maximum number of values sent per data frame | **Data format**    **X** = bit   **B** = byte   **W** = word   **D** = double word   **R** = real | **Underscore** | **Function**    **S**  Send   **R**  Receive   **FS**   Sending without 1-out-of-n check   **FR**   Receiving without 1-out-of-n check |
| **Bin =** Binary information |  |  |  |  |
| **Ana =** Analog value |  |  |  |  |
| **Cnt =** Count value |  |  |  |  |
| **Cmd =** Command |  |  |  |  |
| **Set =** Setpoint, parameter |  |  |  |  |
| **Par =** Parameter |  |  |  |  |
| **Dat =** Data (any mixture of information types) |  |  |  |  |

###### Overview of the data point typicals

The following table provides an overview of the data point typicals.

Overview of the data point typicals

| Data format | Symbolic block name | Function |
| --- | --- | --- |
| **Binary value typicals** |  |  |
| Byte | Bin04B_S | Send 4 byte binary values |
| Byte | Bin04B_R | Receive 4 byte binary values |
| **Analog value typicals** |  |  |
| Int | Ana04W_S | Send 4 analog values |
| Int | Ana04W_R | Receive 4 analog values |
| Real | Ana04R_S | Send 4 analog values as floating point number (CPU 1500 only) |
| Real | Ana04R_R | Receive 4 analog values as floating point number (CPU 1500 only) |
| **Counted value typicals** |  |  |
| UInt, Word ***** | Cnt01D_S | Send 1 counted value |
| UInt, Word ***** | Cnt01D_R | Receive 1 counted value |
| UInt, Word ***** | Cnt04D_S | Send 4 counted values |
| UInt, Word ***** | Cnt04D_R | Receive 4 counted values |
| **Command typicals** |  |  |
| Byte, USInt ***** | Cmd01B_S | Send 1-byte commands |
| Byte, USInt * | Cmd01B_FS | Send 1 byte commands without (1-out-of-n) control |
| Byte, USInt ***** | Cmd01B_R | Receive 1 byte commands (1-out-of-8) |
| Byte, USInt * | Cmd01B_FR | 1 byte commands received without 1-out-of-8 control |
| Bit | Cmd08X_S | Send 8 commands for specific bits (only CPU 1500) |
| Bit | Cmd08X_R | Receive 8 commands for specific bits (only CPU 1500) |
| **Setpoint and parameter typicals** |  |  |
| Word | Set01W_S | Send 1 setpoint and receive current local setpoint. Transmission is subject to 1-out-of-n control (via FC Safe). |
| Word | Set01W_FS | Send 1 setpoint (without 1-out-of-n control) and receive current local setpoint. |
| Word | Set01W_R | Receive 1 setpoint and send current local setpoint |
| ARRAY [1...12] of DInt / UDInt / DWord / Real ***** | Par12D_S | Send max. 12 double words with parameters and receive current local parameters Transmission is subject to 1-out-of-n control (via FC Safe). |
| ARRAY [1...12] of DInt / UDInt / DWord / Real * | Par12D_FS | Send max. 12 double words (without 1-out-of-n control) with parameters and receive current local parameters |
| ARRAY [1...12] of DInt / UDInt / DWord / Real ***** | Par12D_R | Receive max. 12 double words with parameters and send current local parameters |
| **Typicals for variable data types and amounts** |  |  |
| ARRAY [1...12] of DInt / UDInt / DWord / Real ***** | Dat12D_S | Send maximum of 12 double words with any data |
| ARRAY [1...12] of DInt / UDInt / DWord / Real ***** | Dat12D_R | Receive maximum of 12 double words with any data |
| Div. data types ****** | Dat12x1D_S | Send any data to max. 12 channel (only CPU 1500) |
| Div. data types ****** | Dat12x1D_R | Receive any data at max. 12 channels (only CPU 1500) |
| DWord | Dat256D_S | Send maximum of 256 double words with any data |
| DWord | Dat256D_R | Receive maximum of 256 double words with any data |
| *****USINT, UInt and UDInt are not supported at the same time by S7‑300/400.   ******For the supported data types, refer to the block description. |  |  |

###### Parameters not required

Parameters not required in data point typicals can be left open.

##### Reoccurring parameters

###### Description of the typical parameters

In the following description data point typicals that are identical except for the number of data points to be processed are described together.

In the tables of the data point typicals you will find the following information about the individual parameters:

- Parameter

  Name of the parameter
- Declaration

  Parameter type

  - INPUT

    Input parameter
  - OUTPUT

    Output parameter
  - IN_OUT

    In-out parameter
- Data type

  Data type supported for this parameter
- Range of values
- Default

  Preset value of the parameter

  If you do not configure individual parameters of a data point typical, the default value is used.
- Explanation

  Description of the function and the typical-specific properties of the parameter

###### Parameters used by many typicals

The following parameters are used by many of the typicals of the TD7onCPU library. These parameters are described here once and are not repeated in each instance in the following sections of the individual data point typicals.

Depending on the use of the typicals, some parameters are configured differently. Note the typical use described below.

###### PartnerNo

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 / 1 ... 32000 |
| Default: | 0 |
| Explanation: | Subscriber number of the partner  The subscriber number of the partner with which the block communicates must be specified..  - In a station typical, this is normally the subscriber number of the central station or the application of the control station (e.g. ST7cc). - For a typical that is used in a central station, this is normally the subscriber number of a station. |
| **Effects of the value 0 (zero) on various typical classes** |  |
|  | - **Sending typicals**    **(1)**    (Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Dat12D_S, Dat256D_S)   With the value 0 the data is sent to all subscribers to which an ST7 connection is configured. In this case, the parameter "PartnerObjectNo" is automatically sent with the value zero by the process typical.   If PartnerNo is not found in the administration (DB BasicData), an entry to this effect is made in the diagnostics buffer (event ID B101). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.    **Notes**    - If the"PartnerObjectNo" is missing, there must be a list on the partner CPU from which the missing object number can be recognized (see [ListGenerator1500/300/400 FC](#listgenerator1500300400-fc)).   - Use of the block in a node station     If the CPU of the node station maintains both connections to higher-level subscribers as well as to lower-level stations, a data frame with PartnerNo = 0 is transferred to all subscribers in the direction master station and in the direction stations. |
|  | - **Sending typicals**    **(2)**    (Cmd01B_S, Set01W_S, Par12D_S)   The value 0 is not permitted!   If "PartnerNo" is &lt; 1 or &gt; 32000, an error message is entered in the diagnostic buffer (event ID B100).   If the configured value is permitted and correct but "PartnerNo" is not found in the administration (DB BasicData), an entry is also made in the diagnostics buffer (event ID B101). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |
|  | - **Receiving typicals**    **(1)**    (Bin04B_R, Ana04W_R, Cnt01D_R/Cnt04D_R, Dat12D_R, Dat256D_R)   The value 0 is not permitted!   If PartnerNo is &lt; 1 or &gt; 32000, an error message is entered in the diagnostic buffer (event ID B100).   If the configured value is permitted and correct but "PartnerNo" is not found in the administration (DB BasicData), an entry is also made in the diagnostics buffer (event ID B101). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.   If the CPU receives a data frame for this typical, a check is made to establish whether the source subscriber number in the data frame is identical to the "PartnerNo" configured here. If the two subscriber numbers are different, the received information is discarded and an error message is entered in the diagnostic buffer (Event ID B130). |
|  | - **Receiving typicals**    **(2)**    (Cmd01B_R, Set01W_R, Par12D_R)   Set the value 0 if the typical is to receive data from more than one partner, e.g. if it is to receive data from several control centers.   If the CPU receives data for this typical and "PartnerNo" is &gt; 0, a check is made to establish whether the source subscriber number in the data frame is identical to the "PartnerNo" configured here. If the two are different, the received information is discarded and an error message is entered in the diagnostic buffer (Event ID B130).   This check is not made if "PartnerNo" is = 0. Regardless of the sender, each data frame addressed to the typical is passed on to the typical.   If "PartnerNo" is &gt; 0 and this number is not found in the administration (in DB-BasicData), an entry is made in the diagnostic buffer (event ID B101). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.    **Notes**    - If "PartnerNo = 0" is set, make sure that each partner sends the data with a complete destination address (target subscriber no. and target object no.).   - Use of the block in a node station     If the CPU of the node station maintains both connections to higher-level subscribers as well as to lower-level stations, a data frame with PartnerNo = 0 is transferred to all subscribers in the direction master station and in the direction stations. |

###### PartnerObjectNo

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerObjectNo** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 / 1 ... 32000 |
| Default: | 0 |
| Explanation: | Object number of the partner  The number of the object (= DB number) on the partner with which the block communicates. |
| **Effects of the value 0 (zero) on various typical classes** |  |
|  | - **Sending typicals**    **(1)**    (Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Dat12D_S, Dat256D_S)   Setting the parameter to 0 makes sense if PartnerNo = 0 was set for the preceding parameter. If the"PartnerObjectNo" is missing, there must be a list on the partner CPU from which the missing object number can be recognized (see FC-ListGenerator).   If the partner is an ST7cc control center specifying the "PartnerObjectNo" for this block can be omitted because in ST7cc there are no DBs as target objects. ST7cc decodes its data solely based on the source address in the data frame. |
|  | - **Sending typicals**    **(2)**    (Cmd01B_S, Set01W_S, Par12D_S)   The value 0 is not permitted!   If the parameter assignment is incorrect (&lt; 1 or &gt; 32000), an error message is entered in the diagnostic buffer (event ID B102). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |
|  | - **Receiving typicals**    **(1)**    (Bin04B_R, Ana04W_R, Cnt01D_R/Cnt04D_R, Dat12D_R, Dat256D_R)   The value 0 is not permitted!   If the parameter assignment is incorrect (&lt; 1 or &gt; 32000), an error message is entered in the diagnostic buffer (event ID B102). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.   If the CPU receives data for the object configured here, there is a check to establish whether the source object number in the data frame is identical to the "PartnerObjectNo" configured here. If they are different, the received information is discarded. An error message is entered in the diagnostic buffer (event ID B131). |
|  | - **Receiving typicals**    **(2)**    (Cmd01B_R, Set01W_R, Par12D_R)   0 must be set in the following situations:   - The partner is not an S7 CPU, i.e. there is no DB number as object. This is, for example, the case when the partner is an ST7cc control center.   - There is more than one partner (PartnerNo = 0) from which the typical is to receive data. The corresponding objects of these partners will then generally have different numbers; in other words, no unique number can be specified here.If the CPU receives data for the object configured here and "PartnerObjectNo" is &gt; 0, there is a check to establish whether the source object number in the data frame is identical to the "PartnerObjectNo" configured here. If they are different, the received information is discarded. An error message is entered in the diagnostic buffer (event ID B131).   This check is not made if "PartnerObjectNo" is = 0. Regardless of the sender object, each data frame addressed to the object is also passed on to the receiving object. |

###### Enabled

|  |  |  |
| --- | --- | --- |
| Parameter: | **Enabled** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | TRUE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Enable block processing  - If processing is enabled, all the functions of the block execute. - The response is different if processing has not been enabled: |  |
| **Processing not enabled** |  |  |
|  | - **Sending typicals**    (Bin04B_S, Ana04W_S, Cnt01D_S, Cnt04D_S, Dat12D_S, Dat256D_S)   Also applies to the mirror-image value of: Set01W_R, Par12D_R   If processing is not enabled, the block can only communicate at the organizational level; in other words, Org frames can be sent and received.   Please note: A general query is answered, but the response frame contains the data valid at the time of the lock.    **Note**    The response described here does not apply to Cmd01B_R, (see [Command typical Cmd01B_R](#command-typical-cmd01b_r))! |  |
|  | - **Receiving typicals**    (Bin04B_R, Ana04W_R, Cnt01D_R, Cnt04D_R, Dat12D_R, Dat256D_R)   Also applies to the mirror-image value of: Set01W_S, Par12D_S   If processing is not enabled, the block can only communicate at the organizational level; in other words, Org frames can be sent and received.   Please note: A request can still be sent and the answer received, the received information is, however, not output to the outputs. You will find the relevant outputs in the description of the appropriate data point typicals.    **Note**    The response described here does not apply to Cmd01B_S, see [Command typical Cmd01B_S](#command-typical-cmd01b_s)! |  |

###### ImageMemory

|  |  |  |
| --- | --- | --- |
| Parameter: | **ImageMemory** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | TRUE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Using in typicals | Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Set01W_R, Par12D_R, Dat12D_S |  |
| Explanation: | Image memory principle for spontaneous data transmission  - TRUE   The data is transferred according to the image memory principle.   The image memory principle reduces the memory required for storing data frames and produces as little data traffic on the WAN as possible. The default TRUE is the correct choice in most cases. - FALSE   The data is transferred according to the send buffer principle.   The send buffer principle is only required with data points whose individual data changes will be saved and transferred to the partner, for example alarms with time stamps. |  |

###### Conditional

|  |  |  |
| --- | --- | --- |
| Parameter: | **Conditional** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | TRUE |  |
| Address range: | Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Using in typicals | Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Set01W_R, Par12D_R, Dat12D_S |  |
| Explanation: | Conditional spontaneous data transfer  You will information on this below with the parameter "Unconditional". |  |

###### Unconditional

|  |  |  |
| --- | --- | --- |
| Parameter: | **Unconditional** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Using in typicals | Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Set01W_R, Par12D_R, Dat12D_S, Dat256D_S |  |
| Explanation: | Unconditional spontaneous data transfer  With the two parameters "Conditional" and "Unconditional" you decide whether a data frame is transferred immediately by the module if the value changes (unconditional spontaneous) or at a later point in time (conditional spontaneous).  The two parameters are configured as follows:  - **Conditional spontaneous transfer (not necessarily immediately)**    - Conditional = TRUE   - Unconditional = FALSE - **Unconditional spontaneous transfer (immediately)**    - Conditional = FALSE   - Unconditional = TRUE   The default of the two parameters was chosen so that a data frame is not transmitted immediately.  The decision whether a data frame is transferred immediately or later only relates to dial-up networks.  In a dial-up network you must decide from case to case whether a change to the value of the data point requires immediate transfer and therefore the immediate establishment of a connection. This can, for example, be required for data points with alarms.  On a dedicated line, the transmission is always immediate even if the combination of "Conditional" and "Unconditional" is set to "not immediately". On dedicated lines, you do not need to make changes to the two parameter settings. |  |
|  |  |  |

###### Permanent

> **Note**
>
> **Parameter irrelevant**
>
> The parameter (INPUT, Bool) only appears in blocks for S7-300/400.
>
> It is no longer supported functionally with S7-300/400, the value is always = FALSE.

###### TimeStamp

| Symbol | Meaning |
| --- | --- |
| Parameter: | **TimeStamp** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Using in typicals | Bin04B_S, Ana04W_S, Cnt01D_S/Cnt04D_S, Dat12D_S, Dat256D_S, Set01W_R, Par12D_R |
| Explanation: | Time stamp  - TRUE   The data frame will be transferred with a time stamp.   The prerequisite is that the time provided by the local TIM is available in the CPU. For more detailed information, refer to the description of FC TimeTask.    **Note**    With Ana04W_S remember the dependency of the time stamp on the parameter "MeanValueGeneration", see [Analog value typical Ana04W_S](#analog-value-typical-ana04w_s). - FALSE   The data frame is transferred without a time stamp.   For information on the format of the time stamp, refer to the section [Time stamp](#time-stamp). |

> **Note**
>
> **Re-initialization**
>
> This parameter requires re-initialization of the CPU.
>
> **Recommendation:**
>
> Do not change the parameter in runtime or after the restart.

###### NewData

|  |  |  |
| --- | --- | --- |
| Parameter: | **NewData** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL  (Dat256D_R : DWORD) |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Using in typicals | Bin04B_R, Ana04W_R, Cnt01D_R/Cnt04D_R, Cmd01B_R, Set01W_S, Set01W_R, Par12D_S, Par12D_R, Dat12D_R, Dat256D_R  With Dat256D_R, the output occupies a double word with one status per segment. |  |
| Explanation: | Receive new data  The NewData output is intended for user-specific further processing, for example to react in a specific way to receipt of new data.  Whenever the block has received new data and has output it to the outputs for the specific typical, NewData is set to TRUE for one OB1 cycle.  You will find the specific outputs in the description of the individual data point typicals.  With the data point typicals "Set01W_R" and "Par12D_R", NewData is also set to TRUE for one OB1 cycle if there is a new local value entered in the Local = 1 state.  If you do not require the parameter, simply leave it open. |  |

##### Time stamp

###### Format of the SINAUT time stamp

For many data point typicals you can use the TimeStamp parameter to instruct that the data of the object should be transferred with a time stamp.

However for the receiving data point typicals there is no output parameter with which to output the received time stamp. The time stamp is only saved in the instance DB which you have specified when calling the respective receive typical. To further process the time stamp, the data must be read out of the DB by the user program.

The time stamp is saved in two data double words that have the same name in all object DBs:

| Name of the double word | Contents |
| --- | --- |
| RecTimeStamp_1 | Year, month, day and hour |
| RecTimeStamp_2 | Minute, second, millisecond and time status |

With the exception of the half byte with the time status, the date and time are coded in BCD format.

Assignment of the structure of the time stamp

| Name of the double word | Byte no. | Contents |  |
| --- | --- | --- | --- |
| High nibble | Low nibble |  |  |
| RecTimeStamp_1 | 0 | Year * 10 | Year * 1 |
| 1 | Month * 10 | Month * 1 |  |
| 2 | Day * 10 | Day * 1 |  |
| 3 | Hour * 10 | Hour * 1 |  |
| RecTimeStamp_2 | 0 | Minute * 10 | Minute * 1 |
| 1 | Second * 10 | Second * 1 |  |
| 2 | Millisecond * 100 | Millisecond * 10 |  |
| 3 | Millisecond * 1 | Time status |  |

The bit assignment of the half byte "time status" (low nibble of byte 3 of RecTimeStamp_2)

| Bit no. | Value | Meaning |
| --- | --- | --- |
| 0 | 0 | Time is invalid |
| 1 | Time is valid |  |
| 1 | 0 | Standard time |
| 1 | Daylight saving time |  |
| 2 |  | Not used |
| 3 |  | Not used |

The time double words occupy different addresses depending on the typical. Look in the instance DB or in the declaration header of the FB to find the absolute address of both double words.

It is more convenient to give the instance DBs symbolic names. You can then use the symbolic addresses to read out the information. In this case, you do not need to worry about the actual absolute addresses. These are used automatically by STEP 7. The following example clarifies this procedure.

**Example**

Symbolic name of instance DB: `ObjectDB27`

The STEP 7 program for reading the date and time of day and for saving in DB20 beginning with data byte 100 may appear as follows programmed in STL:

`L "ObjectDB27".RecTimeStamp_1`

`T DB 20.DBD 100`

`L "ObjectDB27".RecTimeStamp_2`

`T DB 20.DBD 104`

##### Analog value typical Ana04R_S

###### Validity

S7-1500 only

###### Function

Send 4 analog values as 32-bit floating-point number

Ana04R_S transfers the 4 analog values as instantaneous values. At the time of the transfer, the currently pending analog value is acquired and transferred to the partner.

> **Note**
>
> **Common processing of the four analog values**
>
> The processing parameters such as threshold, smoothing factor etc. exist only once in a typical. These parameters apply to all 4 analog values in common; in other words, it is not possible to set the parameters for the individual analog values. For this reason, each typical should only acquire analog values that should be processed in the same way.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ThresholdIntegration** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Threshold processing according to the integration principle  With this parameter, you can specify whether the integration principle is used in threshold value processing.  With the default FALSE the threshold value is calculated without integration. In this case, you can expect less data traffic on the telecontrol line and locally between CPU and TIM. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ZeroLimitation** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | TRUE |
| Explanation: | Zero limitation  If this parameter is activated negative values are be suppressed and replaced with the value 0. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of the "TriggerInput" input the transfer of the analog value frame can be triggered at a required time.  Example: Time-driven analog value transfer with time stamp for supplying an analog value archive in the control center.  Make sure that you set the "ImageMemory" parameter to FALSE to prevent these data frames with time stamps from being overwritten when saving on the station TIM.  The FC Trigger block can be used for time-driven triggering of a transmission over "TriggerInput".  If you do not require the parameter, simply leave it open. The transfer should then be triggered based on the "ThresholdValue" and "ThresholdIntegration" threshold parameters. |  |
|  | "TriggerInput" actually only triggers transmission indirectly. With a 0 → 1 edge change at "TriggerInput", the data frame is put together with its current values and transferred to the local TIM. The TIM is responsible for the actual transmission to the partner. With dedicated lines or wireless networks the transfer is immediate. With a dial-up connection, it is possible that the data frame is saved first on the TIM and sent at a later point in time. The reason can, for example, be that the data frame is marked as "Conditional spontaneous", see parameter "Conditional". |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **AnalogInput_1 ... _4** |  |
| Declaration: | INPUT |  |
| Data type: | REAL |  |
| Range of values: | See address range |  |
| Default: | 0.0 |  |
| Address range: | Bit memory address | MD0 ... MDn |
| Data address | LD0 ... LDn DBm.DBD0 ... DBDn |  |
| Explanation: | Analog input word  For each analog value to be transmitted in the data frame, you can specify from where the FB will take the analog information. Any combination of a data block and the bit memory address area can be used.  If you do not require parameters, simply leave them open. The value 0 is transferred for these analog inputs in the data frame. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SamplingPeriod** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 32767 [ms] |
| Default: | 500 |
| Explanation: | Acquisition interval for analog inputs in milliseconds  The acquisition interval is required for the following parameters:  - Threshold formation according to the integration principle (ThresholdIntegration) - Smoothing the analog input value (SmoothingFactor)   The value must be selected high enough so that it is certain that a new value was acquired within the encryption time of the analog input. The interval to be specified has to be at least as long as the encoding time of the analog input module being used at the selected resolution (8 ... 15 bits).  The value must also be selected generously so that analog values are acquired even with the highest resolution and with analog modules with the highest number of inputs.  Specifying a "SamplingPeriod" that is too short may lead to an overflow of the internal accumulation counter. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ThresholdValue** |
| Declaration: | INPUT |
| Data type: | REAL |
| Range of values: | +1.175495e-38 ... +3.402823e+38 |
| Default: | 1.0 |
| Explanation: | Threshold value  Without configuration, the default value 1.0 is used.  Point to note with "ThresholdValue" = 0: Changes are not checked based on the threshold value. The analog value frame will only be sent in the following situations:  - When there is a trigger via the "TriggerInput" input, typically a time-driven or event-driven trigger. - When there is a general request to the station or a single request for the data frame. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SmoothingFactor** |
| Declaration: | INPUT |
| Data type: | REAL |
| Range of values: | 1.0 (no smoothing)  4.0 (weak smoothing)  32.0 (medium smoothing)  64.0 (strong smoothing) |
| Default: | 1.0 |
| Explanation: | Smoothing factor  Using the smoothing factor, quickly fluctuating analog values can be smoothed to a greater or lesser extent depending on the factor. This may allow a narrower threshold band to be selected (ThresholdValue).  The smoothing factors are identical to the smoothing factors that are configured for some S7 analog input modules. The smoothing is calculated using the same formula as on the input module:    ![Parameters](images/108702037003_DV_resource.Stream@PNG-de-DE.png)   y<sub>n</sub> = smoothed value in the current cycle n  y<sub>n-1</sub> = smoothed value in previous cycle n-1  x<sub>n</sub> = acquired value in the current cycle n  k = smoothing factor |

##### Analog value typical Ana04R_R

###### Validity

S7-1500 only

###### Function

Receive 4 analog values as 32-bit floating-point number

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **AnalogOutput_1 … _4** |  |
| Declaration: | OUTPUT |  |
| Data type | REAL |  |
| Range of values: | See address range |  |
| Default: | 0.0 |  |
| Address range: | Bit memory address | MD0 ... MDn |
| Data address | LD0 ... LDn DBm.DBD0 ... DBDn |  |
| Explanation: | You can select where the individual analog values received by the FB are output. Addresses of a data block and in the bit memory address area can be mixed as required.  If you do not require parameters, simply leave them open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData**   For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Whenever the FB has received new data and has output it to the outputs "AnalogOutput_1" to "AnalogOutput_4", the "NewData" output is set to TRUE for one OB1 cycle. |

##### Analog value typical Ana04W_S

###### Function

Send 4 analog values as 16 bit values

Ana04W_S transfers the 4 analog values alternatively:

- As instantaneous values

  At the time of the transfer, the currently pending analog value is acquired and transferred to the partner.
- As mean values

  The pending analog value is accumulated at selectable intervals. At the time of the transmission, a mean value is formed from the total value and transferred to the partner.

> **Note**
>
> **Common processing of the four analog values**
>
> The processing parameters such as threshold, smoothing factor etc. exist only once in a typical. These parameters apply to all 4 analog values in common; in other words, it is not possible to set the parameters for the individual analog values. For this reason, each typical should only acquire analog values that should be processed in the same way.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **TimeStamp** |
| For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |  |
| Typical-specific functions | With the setting TRUE the time stamp depends on the setting of the parameter "MeanValueGeneration":  - MeanValueGeneration = FALSE   Instantaneous values are transferred in the data frame.   The time stamp in the data frame is identical to the time of acquisition of the instantaneous values contained in the data frame. - MeanValueGeneration = TRUE   The data frame contains mean values.   The time stamp is identical to the time at which the mean value calculation period was completed.   The start of the mean value calculation period is not included in the data frame. This is, however, identical to the time stamp of the previously transferred mean value frame. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ThresholdIntegration** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Threshold processing according to the integration principle  With this parameter, you can specify whether the integration principle is used in threshold value processing.  With the default FALSE the threshold value is calculated without integration. In this case, you can expect less data traffic on the telecontrol line and locally between CPU and TIM.  When MeanValueGeneration = TRUE, (analog values are sent as mean values), the "ThresholdIntegration" parameter has no meaning. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ZeroLimitation** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | TRUE |
| Explanation: | Zero limitation  If this parameter is activated negative values are be suppressed and replaced with the value 0. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of the "TriggerInput" input the transfer of the analog value frame can be triggered at a required time.  Example: Time-driven analog value transfer with time stamp for supplying an analog value archive in the control center.  Make sure that you set the "ImageMemory" parameter to FALSE to prevent these data frames with time stamps from being overwritten when saving on the station TIM.  If the block calculates mean values, the duration of the calculation period is decided by the "TriggerInput" input. The current period is ended and a new period begun each time a transmission is triggered by this input. The interval between triggering a data frame twice determines the duration of the mean value calculation period.  The FC Trigger block can be used for time-driven triggering of a transmission over "TriggerInput".  If you do not require the parameter, simply leave it open. The transfer should then be triggered based on the "ThresholdValue" and "ThresholdIntegration" threshold parameters. |  |
|  | "TriggerInput" actually only triggers transmission indirectly. With a 0 → 1 edge change at "TriggerInput", the data frame is put together with its current values/mean values and transferred to the local TIM. The TIM is responsible for the actual transmission to the partner. With dedicated lines or wireless networks the transfer is immediate. With a dial-up connection, it is possible that the data frame is saved first on the TIM and sent at a later point in time. The reason can, for example, be that the data frame is marked as "Conditional spontaneous", see parameter "Conditional". |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **MeanValueGeneration** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Mean value generation  If the parameter is enabled the analog values to be acquired are transferred as mean values.  If you select mean value generation, the currently pending analog value is acquired cyclically and accumulated. The acquisition cycle depends on the "SamplingPeriod" parameter (for example 500 ms, see also the description of this parameter). The mean value is calculated from the accumulated values as soon as a transmission is triggered via the "TriggerInput" input. Following this, the accumulation starts again so that the next mean value can be calculated.  The mean value can also be calculated if the transmission of the analog value frame is triggered by a general or single request. The duration of the mean value calculation period is then the time from the last transmission (for example triggered via TriggerInput) to the time of the general or single request. Once again, the accumulation restarts so that the next mean value can be calculated.  If the acquired analog value is above or below the permitted range (7FFFH bzw. 8000H), this value can either be taken into account immediately in the calculation of the mean value or it can be suppressed for a specific period for the calculation of the mean value. The required response can be decided with the "FaultSuppressionTime" parameter: |
|  | - **FaultSuppressionTime = 0**    Acquisition of a value above or below the over- or underrange results in immediate cancellation of the mean value calculation. The value 7FFF<sub>H</sub> or 8000<sub>H</sub> is saved as an invalid mean value for the current mean value calculation period and sent when the next analog value frame is triggered. The calculation of a new mean value is then started. If the analog value remains in the overshoot or undershoot range, this new value is again saved immediately as an invalid mean value and sent when the next frame is triggered. - **FaultSuppressionTime &gt; 0**    If the acquired analog value is in the overshoot or undershoot range, the bad values are excluded from the calculation of the mean value for a maximum duration as defined by the FaultSuppressionTime. If this time is exceeded, the value 7FFF<sub>H</sub> or 8000<sub>H</sub> is saved as an invalid mean value and sent when the next analog value frame is triggered. The procedure is identical in each new mean value calculation period averaging period; in other words, bad values are again suppressed for the duration of the "FaultSuppressionTime".   The duration of the "FaultSuppressionTime" also indirectly decides the proportion of invalid values per mean value calculation period. For example, if the mean value is calculated every 15 minutes and "FaultSuppressionTime" is set to 5 minutes, the mean value is only sent as invalid when more than 1/3 of the analog values acquired are above or below the overshoot or undershoot range in the current mean value calculation period. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **AnalogInput_1 ... _4** |  |
| Declaration: | INPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | I/O words | PIW0 ... PIWn |
| Memory words | MW0 ... MWn |  |
| Data words | LW0 ... LWn DBm.DBW0 ... n |  |
| Explanation: | Analog input word  For each analog value to be transmitted in the data frame, you can specify from where the FB will take the analog information. I/O words from analog input modules, data words from a data block and memory words can be mixed as required.  If you do not require parameters, simply leave them open. The value 0 is transferred for these analog inputs in the data frame. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SamplingPeriod** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 32767 [ms] |
| Default: | 500 |
| Explanation: | Acquisition interval for analog inputs in milliseconds  The acquisition interval is required for the following parameters:  - Threshold formation according to the integration principle (Threshold Integration) - Smoothing of the analog input value (Smoothing Factor) - Mean value generation   The value must be selected high enough so that it is certain that a new value was acquired within the encryption time of the analog input. The interval to be specified has to be at least as long as the encoding time of the analog input module being used at the selected resolution (8 ... 15 bits).  The value must also be selected generously so that analog values are acquired even with the highest resolution and with analog modules with the highest number of inputs.  If mean values are calculated, SamplingPeriod should not be less than 500 ms. If mean values are calculated over very long periods, the time must be increased as follows:  - Mean value calculation period 12 h: SamplingPeriod = 1000 [ms] - Mean value calculation period 24 h: SamplingPeriod = 2000 [ms]   Specifying a "SamplingPeriod" that is too short may lead to an overflow of the internal accumulation counter. The maximum value of 2 147 483 647 of a double integer must not be exceeded. When an overflow is detected, the invalid mean value of 8000<sub>H</sub> is transferred for the current mean value calculation period. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ThresholdValue** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 / 1 ... 32767 |
| Default: | 270 |
| Explanation: | Threshold value  When specifying the threshold value, take the encryption range of the analog values into account. Raw values from S7 analog inputs are always encoded in the range from 0 ... 27648 (= 0 ... 100 %) or + 27648 (= + 100%). Depending on the resolution of the analog input, the value jumps from 128 (with 8-bit resolution) or 1 (with 15-bit resolution). If the acquired analog values have a different encoding range, specify a threshold value oriented toward this.  If the parameter is not configured, the default value of 270 is used. This corresponds to approximately 1% of the normal S7 analog raw value range.  Point to note with "ThresholdValue" = 0  Changes are not checked based on the threshold value. The analog value frame will only be sent in the following situations:  - When there is a trigger via the "TriggerInput" input, typically a time-driven or event-driven trigger. - When there is a general request to the station or a single request for the data frame. - When the analog value moves into the overshoot or undershoot range (7FFF<sub>H</sub> or 8000<sub>H</sub>) (possibly after the suppression time set for "FaultSuppressionTime" has elapsed).   When MeanValueGeneration = TRUE, i.e. the analog values are sent as mean values, the "ThresholdValue" parameter has no meaning. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SmoothingFactor** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 1 (no smoothing)  4 (weak smoothing)  32 (medium smoothing)  64 (strong smoothing) |
| Default: | 1 |
| Explanation: | Smoothing factor  When MeanValueGeneration = TRUE, i.e. the analog values are sent as mean values, the "ThresholdValue" parameter has no meaning.  Using the smoothing factor, quickly fluctuating analog values can be smoothed to a greater or lesser extent depending on the factor. This may allow a narrower threshold band to be selected (ThresholdValue).  The smoothing factors are identical to the smoothing factors that are configured for some S7 analog input modules. The smoothing is calculated using the same formula as on the input module:    ![Parameters](images/108702037003_DV_resource.Stream@PNG-de-DE.png)   y<sub>n</sub> = smoothed value in the current cycle n  y<sub>n-1</sub> = smoothed value in previous cycle n-1  x<sub>n</sub> = acquired value in the current cycle n  k = smoothing factor |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **FaultSuppressionTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 32767 |
| Default: | 0 |
| Explanation: | Fault suppression time in seconds.  Transmission of an analog value located in the overshoot or undershoot range (7FFF<sub>H</sub> or 8000<sub>H</sub>) is suppressed for the time period specified here. The value 7FFF<sub>H</sub> or 8000<sub>H</sub> is only sent after this time has elapsed, if it is still pending. If the value returns to below 7FFF<sub>H</sub> or above 8000<sub>H</sub> again before this time elapses, it is immediately sent again as normal. The suppression time is started again for the full duration the next time 7FFF<sub>H</sub> or 8000<sub>H</sub> is acquired.  This is typically used for temporary suppression of current values that may occur when powerful pumps and motors are started. The analog input may exceed the maximum range several times under some circumstances. Suppression prevents these values from being signaled as faults in the control center system.  The suppression is adjusted to analog values that are acquired by the S7 analog input modules as raw values. These modules return the specified values for the overflow or underflow range for all input ranges (also for life-zero inputs). With provided ready values, fault suppression is only possible if these also adopt the values 7FFF<sub>H</sub> or 8000<sub>H</sub> when there is overshoot or undershoot. If this is not the case, the parameter does not need to have a value entered.  The parameter can also be used in combination with the mean value calculation for temporary suppression of the values 7FFF<sub>H</sub> or 8000<sub>H</sub> (see parameter MeanValueGeneration).  If no parameter is specified, the default of 0 seconds applies. An acquired value of 7FFF<sub>H</sub> or 8000<sub>H</sub> is then sent immediately when it is first detected or, with mean value calculation, as an invalid mean value for the current mean value calculation period. |

##### Analog value typical Ana04W_R

###### Function

Receive 4 analog values as 16-bit values

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter: | **AnalogOutput_1 … _4** |  |  |
| Declaration: | OUTPUT |  |  |
| Data type | WORD |  |  |
| Default: | TRUE |  |  |
| Explanation | 0 (W#16#0) |  |  |
|  | Range of values: | I/O words  Memory words   Data words | PQW0 ... PQWn  MW0 ... MWn LW0 ... LWn  DBm.DBW0 ... n |
|  | You can select where the individual analog values received by the FB are output. I/O words from analog output modules, data words from a data block and memory words can be mixed as required.  If you do not require parameters, simply leave them open. |  |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData**   For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Whenever the FB has received new data and has output it to the outputs "AnalogOutput_1" to "AnalogOutput_4", the "NewData" output is set to TRUE for one OB1 cycle. |

##### Binary value typical Bin04B_S

###### Function

Send 4 bytes of binary information

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **InputByte_1 … _4** |  |
| Declaration: | INPUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Input bytes | IB0 ... IBn PIB0 ... PIBn |
| Memory bytes | MB0 ... MBn LB0 ... LBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Explanation: | Input byte  Specify the memory area (1 to 4 bytes) of the binary information to be transferred by the FB.  Input bytes from the process input image, I/O bytes directly from digital input modules, data bytes from a data block and memory bytes can be mixed.  If you do not require parameters, simply leave them open.  For unconfigured bytes, the value 0 (zero) is transferred. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DisableMask** |
| Declaration: | INPUT |
| Data type: | DWORD |
| Range of values: | 0 ... 2147483647  - As 32 bit binary number   2#0 ... 2#11111111_11111111_11111111_11111111 - As 32 bit hexadecimal number   DW#16#0 ... DW#16#FFFF_FFFF |
| Default: | 0 (2#0) |
| Explanation: | Disable mask  - For every input to be blocked enter a 1 at the relevant position in the bit pattern. - For the other inputs enter a 0.   A disabled input always has the value 0 (zero) during the transfer.  For the assignment of the 32 inputs from "InputByte_1" to "InputByte_4" to the 32 bits of the blocking mask, see the following table. |

|  | InputByte_1 |  |  |  |  |  |  |  | InputByte_2 |  |  |  |  |  |  |  | InputByte_3 |  |  |  |  |  |  |  | InputByte_4 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |
| **2#** | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
| **DW#16#** | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **InversionMask** |
| Declaration: | INPUT |
| Data type: | DWORD |
| Range of values: | 0 ... 2147483647  - As 32 bit binary number   2#0 ... 2#11111111_11111111_11111111_11111111 - As 32 bit hexadecimal number   DW#16#0 ... DW#16#FFFF_FFFF |
| Default: | 0 (2#0) |
| Explanation: | Inversion mask  The inversion of input signals can, for example, be useful when using a mixture of sensors operating on the open and closed circuit principle.  - For every input to be inverted enter a 1 at the relevant position in the bit pattern. - For the other inputs enter a 0.   For the assignment of the 32 inputs from "InputByte_1" to "InputByte_4" to the 32 bits of the inversion mask, see the following table. |

|  | InputByte_1 |  |  |  |  |  |  |  | InputByte_2 |  |  |  |  |  |  |  | InputByte_3 |  |  |  |  |  |  |  | InputByte_4 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |
| **2#** | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
| **DW#16#** | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  | _ |  |  |  |

##### Binary value typical Bin04B_R

###### Function

Receive 4 bytes of binary information

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **OutputByte_1 … _4** |  |
| Declaration: | OUTPUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range. |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Output bytes | QB0 ... QBn PQB0 ... PQBn |
| Memory bytes | MB0 ... MBn LB0 ... LBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Explanation: | Output byte  Specify the memory area (1 to 4 bytes) of the binary information to be output in the binary information.  Output bytes from the process image output, I/O bytes directly to digital output modules, data bytes from a data block and memory bytes can be mixed.  If you do not require parameters, simply leave them open.  For information on reading out the time stamp received with the data using the user program, see the section [Time stamp](#time-stamp). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  The output "NewData" is always set to TRUE for one OB1 cycle when the FB has received new data and output it to the output bytes "OutputByte_1" to "OutputByte_4" |

##### Command typical Cmd01B_S

###### Function

Send 1 byte commands with 1-out-of-8 check.

The 1-out-of-8 check is performed by the data point typical.

The 1-out-of-n check is performed by FC Safe.

> **Note**
>
> **FC Safe required**
>
> With Cmd01B_S, data can only be transmitted when FC Safe is linked in cyclic program.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **Enabled** |
|  | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the disabled status has been canceled. The block cannot communicate at the organizational level in this status because it cannot send any org. frames. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **CommandInputByte_HW** |  |
| Declaration: | INPUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Input bytes | IB0 ... IBn PIB0 ... PIBn |
| Memory bytes | MB0 ... MBn LB0 ... LBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Explanation: | Command input byte for hardware input.  This command input byte is specially designed for entering commands using hardware, i.e. via digital inputs. Input using memory or data bytes is also possible, but you must then make sure that the command pending at the input byte is reset, which occurs during hardware input when the command button is released.  When input is detected, if no error is detected during the 1-out-of-8 and 1-out-of-n check, and if the central enable memory bit is set, the command is transferred. This is automatically set by FC Safe following a selected time delay set there (see FC Safe, "InputDelayTime" parameter).  If a 1-out-of-8 or 1-out-of-n error is detected, the entered command is no longer processed. A new command is only read in again if previously for the time of one OB1 cycle no hardware command was detected in the CPU at this or another command input block with a hardware input.  The FB enters a detected 1- out-of-8- or 1-out-of-n error in the diagnostic buffer (event ID B171 or B172). The error status is also indicated via the "InputError" output of FC Safe (see FC Safe, "InputError" parameter) and continues to be indicated as long as the error remains. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **CommandInputByte_SW** |  |
| Declaration: | IN_OUT |  |
| Data type | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Memory bytes | MB0 ... MBn |
| Data bytes | DBm.DBB0 ... n |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation | Command input byte for software input  This command input byte is specially designed for entering commands using software, i.e. by the user program or an operator panel (OP). When an input is detected and if no error is detected during the 1-out-of-8 and 1-out-of-n check, the command id reset at the input byte and transferred. The central enable memory bit is ignored here because it is only intended for command input over hardware (see "CommandInputByte_HW").  If a 1-out-of-8 or 1-out-of-n error is detected, the entered command is no longer processed. A new command is only read in again if previously for the time of one OB1 cycle no software command was detected in the CPU at this or another command input block with a software input.  The FB enters a detected 1- out-of-8- or 1-out-of-n error in the diagnostic buffer (event ID B171 or B172). Appropriate error bits are also set in the central data block BasicData where they can be queried by the software. For further details, refer to the description of FC Safe.  In principle it is possible to create a new command at "CommandInputByte_SW" in every OB1 cycle. However, only one command per OB1 cycle is allowed and this applies to all command input blocks with software input (1-out-of-n check). An ’empty cycle’ between two consecutive software commands is therefore not necessary. |  |

> **Note**
>
> **CommandInputByte_HW / CommandInputByte_SW**
>
> If the same commands need to be entered over the hardware and software, the two command inputs "CommandInputByte_HW" and "CommandInputByte_SW" can also be used at the same time.
>
> If a command is entered at the same time over both input bytes, this is only accepted when exactly the same command is entered over the hardware as well as the software input. The hardware input is then processed further.
>
> In all other cases the input is rejected and an error message is entered in the diagnostic buffer (Event ID B170). The error status is also indicated via the InputError output of FC Safe. Appropriate error bits are set in the central data block BasicData where they can be queried by the software (see FC Safe).

##### Command typical Cmd01B_FS

###### Validity

S7-1500 only

###### Function

Send 1 byte commands without 1-out-of-8 test This means that it is not necessary to call the FC Safe in the cyclic program.

There is less transmission security due to the lack of a 1-out-of-8 check.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **Enabled** |
|  | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the disabled status has been canceled. The block cannot communicate at the organizational level in this status because it cannot send any org. frames. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **HWmode** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Explanation: | The parameter specifies whether the block works in hardware mode (TRUE) or software mode (FALSE). Depending on the selected mode, the CommandInputByte is available for hardware input or for software input.  In hardware mode, sending of commands is edge-controlled (edge transition from 0 to 1), the commands are not automatically reset. If a command is recognized, it is only included in the frame to be sent and sent when it has been continuously pending for the configured delay time (InputDelayTime). A possible delayed second command, for which the input delay time has not yet been reached, is ignored, but is only sent when its input delay time has also expired. At the same time is entered in the send buffer, the „InputOK" is set for 1 cycle. The same command can only be sent again if it has been reset to "0" beforehand. The „InputDelayTime", "MaxInputTime" and "InputError" parameters apply to all eight commands of the command byte together and are only relevant in hardware mode. |

| Symbol | Meaning |
| --- | --- |
| Name: | **InputDelayTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   When the parameter is not required - 1 ... 32000   Value range for delay time, only relevant in hardware mode |
| Explanation: | Delay time in ms for commands entered via hardware.  A delay time of at least 1000 ms is recommended.  The parameter applies to all eight commands of the command byte. The parameter is irrelevant when the parameter   HWmode = FALSE is set. |

| Symbol | Meaning |
| --- | --- |
| Name: | **MaxInputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   When the parameter is not required - 1 ... 32000   Range of values for monitoring time |
| Explanation: | Monitoring time in ms for commands and setpoints that are input via hardware.  A monitoring time of at least 30 s is recommended.  The parameter applies to all eight commands of the command byte.  If you do not require the parameter, specify 0 (zero). |

|  |  |  |
| --- | --- | --- |
| Name: | **InputOK** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | The "InputOK" display is also set for one cycle with the entry in the send buffer. The display is independent of the "HWmode" parameter. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **InputError** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Display of input errors for hardware commands  The parameter applies to all eight commands of the command byte.  The output is set to 1 if at least one command is pending longer than the value configured under "MaxInputTime".  The output is only reset to 0 if all 8 possible commands are free of errors.  If a timeout occurs, you have to reset the respective command manually. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **CommandInputByte** |  |
| Declaration: | IN_OUT |  |
| Data type | BYTE |  |
| Range of values: | See address range |  |
| Address range: | Memory bytes | MB0 ... MBn |
| Data bytes | DBm.DBB0 ... n |  |
| Address range for hardware inputs: |  |  |
| Input bytes | IB0 ... IBn |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation | **Command input byte for hardware input**   When the HWmode parameter has the value TRUE, this command input byte is specially designed for entering commands using hardware, i.e. via digital inputs.  The command is only entered in the send buffer if the partner can be reached.  You have to reset the command pending at the input byte yourself.   **Command input byte for software input**   When the HWmode parameter has the value FALSE, this command input byte is specially designed for entering commands using software, i.e. by the user program or an operator panel (OP).  The command is only entered in the send buffer if the partner can be reached.  Commands that have been entered are automatically reset. |  |

##### Command typical Cmd01B_R

###### Function

Receive 1 byte commands (1-out-of-8 format)

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **Enabled**   For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the disabled status has been canceled. Any commands that are still received are not output. The FB cannot communicate at the organizational level in this status because Cmd01B_R cannot send or receive org. frames.  If the "Enabled" input should be made operable by a switch, this local disable means received commands are no longer output. Since the block is, however, not capable of sending org. frames, it cannot report this local block back to the partner itself. This must be done with another typical, e.g. Bin04B_S. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **MultipleOutput** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Simultaneous output of multiple commands permitted  With this parameter, you can specify whether or not several (consecutively received) commands can be output simultaneously; in other words, you specify how the block reacts when a new command is received and the previously received command still needs to be output.  Requirement: The command output time has not yet elapsed and the user program has not yet reset this command.  - FALSE   Multiple output is not permitted. The newly received command overwrites the output byte. Any command still pending is therefore reset to 0 unless the new command is identical to the old one. - TRUE   Multiple output is permitted. A newly received command is written to the current output byte. The command output time is restarted and applies to all pending commands. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **CommandOutputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 500 |
| Default: | 500 |
| Explanation: | Command output time for command outputs in milliseconds  The specified time applies to all command outputs.  If more than one output can be set at the same time (MultipleOutput = TRUE), the output time is restarted with each newly received command. This means retriggering for already pending commands. All the command outputs are reset at the same time onöy when the output time elapses.  With the value 0 a set command output is not reset by the command typical. You need to do this via the user program. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  The output "NewData" is always set to TRUE for one OB1 cycle when the FB has received new data and output it to the output byte "CommandOuputByte". |

|  |  |  |
| --- | --- | --- |
| Parameter: | **CommandOutputByte** |  |
| Declaration: | IN_OUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | (process image) output bytes | QB0 ... QBn |
| Memory bytes | MB0 ... MBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Since the parameter is an IN_OUT parameter, direct I/O output of the command byte to PQB0 ... PQBn is not permitted. It is also difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Command output byte  To allow the command outputs to be reset both by the command typical itself as well as by the user program (when output time = 0), the parameter was declared as an IN_OUT parameter. |  |

##### Command typical Cmd01B_FR

###### Validity

S7-1500

###### Function

1 byte commands received without 1-out-of-8 check. There is less transmission security due to the lack of a 1-out-of-8 check.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **Enabled**   For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the disabled status has been canceled. Any commands that are still received are not output.  If the "Enabled" input is operated via a switch, this local disable has the effect that received commands are no longer output. Since the block is, however, not capable of sending org. frames, it cannot report this local block back to the partner itself. This must be done with another typical, e.g. Bin04B_S. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **CommandOutputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 500 |
| Default: | 500 |
| Explanation: | Command output time for command outputs in milliseconds  The specified time applies to all command outputs.  The output time is restarted with each newly received command. This means retriggering for already pending commands. All the command outputs are reset at the same time onöy when the output time elapses.  With the value 0 a set command output is not reset by the command typical. You need to do this via the user program. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  The output "NewData" is always set to TRUE for one OB1 cycle when the FB has received new data and output it to the output byte "CommandOuputByte". |

|  |  |  |
| --- | --- | --- |
| Parameter: | **CommandOutputByte** |  |
| Declaration: | IN_OUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | (process image) output bytes | QB0 ... QBn |
| Memory bytes | MB0 ... MBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Since the parameter is an IN_OUT parameter, direct I/O output of the command byte to PQB0 ... PQBn is not permitted. It is also difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Command output byte  To allow the command outputs to be reset both by the command typical itself as well as by the user program (when output time = 0), the parameter was declared as an IN_OUT parameter. |  |

##### Command typical Cmd08X_S

###### Validity

S7-1500

###### Function

Sending 8-byte commands over 8 channels for specific bits

No 1-out-of-n test is performed because the FC Safe is not required by the typical.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| General parameters: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **Enabled** |
|  | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the processing lock has been canceled. The block cannot communicate at the organizational level in this status because it cannot send any org. frames. |

|  |  |  |
| --- | --- | --- |
| Name: | **CommandInput01..08** |  |
| Declaration: | IN_OUT |  |
| Data type: | Bool |  |
| Range of values: | See address range |  |
| Default: | 0 |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Since the parameter is an in/out parameter (IN_OUT declaration), a direct I/O output of command bits to PQ0 ... PQn is not permitted. In addition, the specification of local memories should not be used. |  |  |
| Explanation: | Command input bit  The parameter exists eight times, once per channel.  When the input of a command is detected, the command is immediately transferred. Each command is transferred to bit 0 of a byte and transferred in a copy of the byte.  When a command is detected, the entire command byte and its copy are always transferred.  The command inputs are not reset automatically and are not monitored for a permanently pending value 1. Make sure you reset the pending command. |  |

##### Command typical Cmd08X_R

###### Validity

S7-1500

###### Function

Receiving 8-byte commands over 8 channels for specific bits

For 1-out-of-8 check see below.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| General parameters: | **PartnerNo**    **PartnerObjectNo** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **Enabled**   For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters). |
| Typical-specific response: | Enable block processing  If processing is disabled the FB only checks to see if the processing lock has been canceled. Any commands that are still received are not output. The FB cannot communicate at the organizational level in this status because it cannot send or receive org. frames.  If the "Enabled" input is operable by a switch, this local disable means received commands are no longer output. Since the block does not send org. frames, it cannot report this local disable back to the partner itself. This must be done with another typical, e.g. Bin04B_S. |

| Symbol | Meaning |
| --- | --- |
| Name: | **CommandOutputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 500 |
| Default: | 500 |
| Explanation: | Command output time for command outputs in milliseconds  The specified time applies to all command outputs.  The output time is started separately for each command channel. Only if the same command is received again within the output, is its output time restarted. The output times of the other commands are not affected.  With the value 0 a set command output is not reset by the command typical. You need to do this via the user program. |

| Symbol | Meaning |
| --- | --- |
| Name: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  The output "NewData" is always set to TRUE for one OB1 cycle when the FB has received new data and output it to the respective "CommandOuputXX" output. |

|  |  |  |
| --- | --- | --- |
| Name: | **CommandOutput01..08** |  |
| Declaration: | IN_OUT |  |
| Data type: | Bool |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Output bits | Q 0.0 ... Q n.7 |
| Memory | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Since the parameter is an in/out parameter (IN_OUT declaration), a direct I/O output of command bits to PQ0 ... PQn is not permitted. In addition, the specification of local memories should not be used. |  |  |
| Explanation: | Command output bit  The parameter exists eight times, once per channel.  To allow the command outputs to be reset both by the command typical itself and by the user program (when output time = 0), the parameter is declared as an in/out parameter (IN_OUT). |  |
|  | An internal 1-out-of-8 check is performed in each byte.  - If more than 1 bit is received in one byte, the following error is output:   0xB174 ‑ 1-out-of-8 error - If the copy of the command byte is not identical, the following error is output:   0xB173 ‑ Command and control byte not identical   The command is deleted in both cases. |  |

##### Counted value typicals Cnt01D_S / Cnt04D_S

###### Function

- Cnt01D_S: Send 1 counted value (32 bits).
- Cnt04D_S: Send 4 counted values (32 bits).

  Note that the parameter "DifferenceValue" for forming the difference value can only be activated at the same time for all four counted values.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **GeneralTriggerCommand** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Restore collective command  The restore collective command as a central system memory bit belongs to the organizational SINAUT system commands.  Set the parameter to TRUE if the counted value transfer is to be triggered by a restore collective command.  - When the destination subscriber no. (PartnerNo) = 0 (transfer to all), the restore collective command is taken into account.   When the restore collective command is detected, the currently accumulated counted value is transferred regardless of other triggers for transfer. The restore bit is inverted in this counted value. - If in the typical an explicit destination subscriber no. (PartnerNo &gt; 0) is configured, the restore collective command is evaluated in the corresponding subscriber object in the central administration.   You can use the parameters "GeneralTriggerCommand" and "TriggerInput" at the same time. In this case the transfer is triggered both by an edge change 0 → 1 at "TriggerInput" and when a restore collective command is received. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of the "TriggerInput" input the triggered transfer can be triggered at a required time regardless of other criteria for a transfer.. The currently accumulated counted value is transmitted. The restore bit (see above) is inverted in this counted value.  Example: Time-driven transmission with time stamp for supplying an archive in the control center.  You can use the parameters "GeneralTriggerCommand" and "TriggerInput" at the same time. In this case the transfer is triggered both by an edge change 0 → 1 at "TriggerInput" and when a restore collective command is received.  With the setting FALSE no restoring and no transfer via the "TriggerInput" input is triggered. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **Counter_1 (Cnt01D_S)**    **Counter_1 ... _4 (Cnt04D_S)** |
| Declaration: | INPUT |
| Data type: | COUNTER |
| Range of values: | 0 ... 32767  - Z0 as placeholder   or - Z1 ... Zn   n depends on the CPU type. |
| Default: | ‑ |
| Explanation: | Number of the SIMATIC counter  Here, you specify the SIMATIC counter in which the pulses were counted time-driven. This counting takes place in the background using FC PulseCounter that is called in a cyclic interrupt OB (for example in OB35). See also section [FC PulseCounter](#fc-pulsecounter) and [Cyclic interrupt OB](#cyclic-interrupt-ob).  The COUNTER data type cannot be preassigned a value.  If you configure the Z0 placeholder, the corresponding counted value is not processed. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DifferenceValue** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 ... 31767 |
| Default: | 0 |
| Explanation: | Difference value  - When a value between 1 and 31767 is configured, the counted value is transferred as soon as the difference between the current and most recently transferred counted value reaches the value specified here. - If the default value 0 is configured, a counted value is transferred only in the following situations:   - On an edge change 0 → 1 at the "TriggerInput" input   - On receipt of a restore command when "GeneralTriggerCommand" = TRUE.   Select the difference value dependent on the maximum pulse rate per second.  Do not select a value that is too low so that the counted value is not constantly transferred to the TIM. This would put load on the communications path to the CPU and the send queue of the CPU.   **Note on Cnt04D_S**  In the typical this processing parameter for forming the difference value only exists once. It applies to all 4 counted values together. It is not possible to set the parameter for the individual counted values. When using this parameter, each typical should therefore only acquire counted values that can be processed identically. |

##### Counted value typicals Cnt01D_R / Cnt04D_R

###### Function

- Cnt01D_S: Receive 1 counted value (32 bits)
- Cnt04D_S: Receive 4 counted values (32 bits)

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **BCD_Format** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | TRUE |
| Explanation: | Counted value output in BCD format  - If the parameter is activated the received counted value is output as a positive BCD value at the "CountedValueOutput_n" output. - If the parameter is deactivated the counted value is output as a positive 32-bit integer value.   For the different value ranges of the two formats, see the parameter "CountedValueOutput_n".  If the maximum counted value that can be represented is exceeded, the counted value starts again at 0 and counting continues in the positive numeric range.   **Note on Cnt04D_R**  The parameter exists only one in the typical and it applies to all 4 counted values together. It is not possible to make an individual setting per counted value. When using this parameter, per typical only counted values with an identical output format should be output. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **CntValInvalid** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Counted value invalid  When evaluating "CntValInvalid" remember that the bit might only be set for one OB1 cycle.  The CntValInvalid output indicates whether the last received counted value was invalid. . With "Cnt04D_R", this counts as a group display for all 4 counted values, see the note below.  The output shows the validity status of the most recently received counted value in inverted form.  The output serves the following purposes:  - Error display - Signal for user-specific further processing   You can, for example, react to the lack of up-to-dateness, by correcting the counted value output at "CountedValueOutput_n" with possibly lost counting pulses.   If you do not require the parameter, simply leave it open.   **Note on Cnt04D_R**  Although all 4 counted values have their own status bit in the data frame, for the status at the output "CntValInvalid" only the bit of the first counted value in the previously received data frame is evaluated. This status, however, applies to all 4 counted values. (All counted values in the data frame always have the same status.) |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **RestoreStatus** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Status of the restore bit in the received counted value.  The "RestoreStatus" output indicates the current status of the restore bit from the last received counted value frame.  You can use the output for user-specific further processing.  Example: You can only access the information at "CountedValueOutput_n" when a change has been detected at the "RestoreStatus" output; in other words, when the counted value has been received due to a restore, such as a local time-driven restore.  If you do not require the parameter, simply leave it open.   **Note on Cnt04D_R**  Although all 4 counted values have their own restore bit in the data frame, for the status at the "RestoreStatus" output only the restore bit of the first counted value in the previously received data frame is evaluated. This status, however, applies to all 4 counted values. (All counted values in the data frame always have the same status.) |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  The output "NewData" is always set to TRUE for one OB1 cycle when the FB has received new data and output it to the output / outputs "CountedValueOutput_1" to "CountedValueOutput_4" |

|  |  |  |
| --- | --- | --- |
| Parameter: | **CountedValueOutput_1 (Cnt01D_S)**    **CountedValueOutput_1 ... _4 (Cnt04D_S)** |  |
| Declaration: | IN_OUT |  |
| Data type: | DWord, UDInt |  |
| Range of values: | - Integer: - BCD: | 0 ... 2<sub> </sub>147<sub> </sub>483<sub> </sub>647  0 ... 9<sub> </sub>999<sub> </sub>999 |
| Default: | 0 |  |
| Address range: | Output (DWORD) | QD0 … QDn |
| Bit memory (DWORD) | MD0 ... MDn |  |
| Data (DWORD) | DBm.DBB0 … n |  |
| Since the parameter is an in-out parameter (declaration IN_OUT), direct I/O output of the counted value to PQD0 ...PQDn is not permitted.  It is also difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Counted value output  The counted value typical always adds the newly formed difference value (difference between the new and last received counted value) to the value currently output at the counted value output.  The counted value output is a double word in which the counted value is stored in BCD format or as a 32-bit integer value (depending on the "BCD_Format" parameter, see above).  The counted value id always output as a positive number. If the maximum counted value that can be represented is exceeded, the counted value starts again at 0 and counting continues in the positive numeric range.  Since the parameter is an in-out parameter (IN_OUT), the value can be reset to 0 or another value at the counted value output by the user program at any time. |  |

##### Data typical Dat12D_S

###### Function

Send maximum of 12 double words with any data content.

The content of each double word may be a value in double word (DWORD, DINT, REAL) format, it can also be a mixture of other data types which together form a double word, for example:

- 4 bytes
- 2 words
- 2 bytes + 1 word

Sending the data area can be triggered in two ways:

- By a change check

  The data is transferred as soon as a bit changes ("SendOnChange" = TRUE).
- By the user program

  The transfer can be triggered by an edge change 0 → 1 at the "TriggerInput" input

  For time-driven transfer FC Trigger can be used.

With "SendAll" you can also specify whether the transfer always includes all data or only the data double words that have changed.

> **Note**
>
> **Remember double word boundaries**
>
> When changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 12 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendOnChange** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Send on change  With the setting TRUE, the block runs a change check within the acquired data area "DataInput". The block checks whether at least one bit has changed. If a change is detected, a transfer of the data area is started automatically. You specify whether the entire area is transferred or only the changed part with the "SendAll" parameter.  If the setting is FALSE, you need to trigger the transfer via the input parameter "TriggerInput". |

|  |  |  |
| --- | --- | --- |
| Parameter: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of the "TriggerInput" input, the transfer of the data frame can be triggered at a required time.  Example: Time-driven analog value transfer with time stamp for supplying an analog value archive in the control center.  Make sure that you set the "ImageMemory" parameter to FALSE to prevent this data with time stamps from being overwritten when saving on the station TIM.  The FC Trigger block can be used for time-driven triggering of a transmission over "TriggerInput".  "TriggerInput" actually only triggers transmission indirectly. With a 0 → 1 edge change at "TriggerInput", the data frame is put together with its current values and transferred to the local TIM. The TIM is responsible for the actual transmission to the partner. With dedicated lines or wireless networks the transfer is immediate. With a dial-up connection, it is possible that the data frame is saved first on the TIM and sent at a later point in time. The reason can, for example, be that the data frame is marked as "Conditional spontaneous", see parameter "Conditional". |  |
|  | If you do not require the parameter, simply leave it open. You should, however, then set the "SendOnChange" parameter to TRUE so that the data is transmitted automatically at every change.  For the triggering you can also select a combination of "SendOnChange" plus "TriggerInput". This means that a transfer is triggered both when a change is detected and at every edge change from 0 to 1 at the "TriggerInput" input.  If you use neither "SendOnChange" nor "TriggerInput" to trigger data transfer, the data will only be transferred when there is a single request for this data object or within the framework of a general request. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendAll** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | TRUE |
| Explanation: | Send all data with every transfer  With the parameter, you specify whether the block will always transfer all data of the area specified with "DataInput" or only changed data. The transfer can be triggered by the activated change check (SendOnChange = TRUE) or by "TriggerInput".  - SendAll = TRUE   Always send all data - SendAll = FALSE   Send only changed data   Exception: If "SendAll" is set to = FALSE, the transfer is triggered by "TriggerInput" and if no data has changed at this time, the complete area will be transferred. For this exception this corresponds to "SendAll" = TRUE.   When only the changed data area is transferred ("SendAll" = FALSE), this area consists of the first and the last double word in which a change was detected and all words located in between, even if these have not changed.   If there is a single request for this data object or within the framework of a general request, all data words of the area specified by "DataInput" are always transferred. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DataInput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Data input area  The ANY pointer addresses the data area in which the data to be acquired is located. This data area must be within a data block and its length can vary between 1 and 12 data double words.  For information on the content and formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

##### Data typical Dat12D_R

###### Function

Receive maximum of 12 double words with any data content.

The content of each double word may be a value in double word (DWORD, DINT, REAL) format, it can also be a mixture of other data types which together form a double word, for example:

- 4 bytes
- 2 words
- 2 bytes + 1 word

Dat12D_R stores the received data without further processing in the data area specified by "DataOutput". You need to evaluate and process the received data with the user program.

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DataOutput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Data output area  The ANY pointer addresses the data area in which the received data is saved. This data area must be within a data block and its length can vary between 1 and 12 double words.  For information on the content and formats, refer to the section "Function" above.  Dat12D_R stores the received data without further processing in the data area specified by "DataOutput". You need to evaluate and process the received data with the user program.  When only changed data is sent by the partner object Dat12D_S, it is possible that only part of the data output area is newly written. this is the area in which the changes were detected at the acquisition end  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | Receive new data  For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new data values from the partner object and has output them to the output field "DataOutput", the "NewData" output is set to TRUE for one OB1 cycle. |

##### Data typical Dat12x1D_S

###### Validity

S7-1500

###### Function

Send data a maximum of 12 times with any data content via 12 channels for specific double words

You define the number of channels of the object used (1..12) in the "ChnCnt" parameter.

One data type is permitted per channel. You specify the data type for the content of a channel in the "DataInputXX" parameter using the respective ANY pointer.

The number of transferred data per channel must not exceed the length of 1 double word (32 bits). If you specify the number of data for one channel with 3 CHAR, for example, the fourth byte is not read and will not be evaluated for the transfer time (SendOnChange).

**Associated instance data block**

> **Note**
>
> **DB with standard access**
>
> The typical uses ANY pointers in the "DataInputXX" parameters. Disable the "Optimized block access" attribute in the properties of the DB.

**Triggering transfer and transferred data areas**

As a maximum, the telegram is sent completely with all channels specified in "ChnCnt". Depending on the parameter assignment, not all data of all channels are transferred.

Sending the data can be triggered in the following ways:

- **Time-driven**

  The transfer can be triggered via the user program.

  With an edge change 0 → 1 at the "TriggerInput", all data specified under "DataInputXX" is always transferred.

  For time-driven transfer FC Trigger can be used.
- **On change**

  The transfer is triggered via the change control ("SendOnChange" = TRUE).

  - On change in only one channel:

    Only the data of the changed channel is transferred.
  - On change in multiple channels:

    The transferred data comprises a contiguous area from the first changed channel to the last changed channel.

    Unchanged channels that may be before or after the transferred area are not transferred.
- **Requests**

  If there is a single request for this data object or within the framework of a general request, all data of the typical is always transferred.

To trigger the data transfer, you can also select a combination of "SendOnChange" plus "TriggerInput". This means that a transfer is triggered both when a change is detected and at every edge change from 0 → 1 at the "TriggerInput" input.

If you use neither "SendOnChange" nor "TriggerInput" to trigger data transfer, the data is only transferred when there is a single request for this data object or within the framework of a general request.

**Two parameter sets for different prioritization of the channels**

The typical provides the possibility to handle channels differently with respect to saving and the transfer time by means of two parameter sets. Both parameter sets contain the following parameters:

| Symbol | Meaning |
| --- | --- |
| **Parameter set 1** | **Parameter set 2** |
| - ImageMemory01 - Conditional01 - SendOnChange01 | - ImageMemory02 - Conditional02 - SendOnChange02 |

Function of the parameters:

- ImageMemory

  Determines whether the data is transferred according to the image memory principle or the send buffer principle.
- Conditional

  Determines whether the data is transferred "Conditional spontaneous" or "Unconditional spontaneous".
- SendOnChange

  Determines whether the data is transferred on change.

You can prioritize the channels as follows, for example, using the different parameter assignment of the respective parameters:

- Channels for parameter set 1

  Important events to be saved individually and transferred immediately.
- Channels for parameter set 2

  Operating data whose values may be overwritten and which does not need to be transferred immediately.

Each channel is assigned to one of the two parameter sets using the "ChnSets" parameter. You will find a parameter assignment example below.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| General parameters: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory01..02 ***    **Conditional01..02 ***    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters).   ***** Parameter one time each for parameter set 1 and 2 |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **SendOnChange01..02 *** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Parameter assignment: | ***** Parameter once for parameter set 1 and 2 |
| Explanation: | Send on change  The parameter exists two times, once per channel.  With the setting TRUE, the block runs a change check within the acquired data area "DataInput". The block checks whether at least one bit has changed. If a change is detected, a transfer of the data area is started automatically. See above for information on the transferred area.  If the setting is FALSE, you need to initiate the transfer via the input parameter "TriggerInput". |

|  |  |  |
| --- | --- | --- |
| Name: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of this input, the transfer of the data telegram can be triggered at a selected time.  Example: Time-driven analog value transfer with time stamp for supplying an archive in the control center.  Make sure that you set the "ImageMemory" parameter to FALSE to prevent this data with time stamps from being overwritten when saving on the station TIM. |  |
|  | The FC Trigger block can be used for time-driven triggering of transmission over "TriggerInput".  "TriggerInput" actually only triggers transmission indirectly. With a 0 → 1 edge change at "TriggerInput", the data telegram is put together with its current values and transferred to the local TIM.  With dedicated lines or wireless networks, the TIM transfers the data immediately.  With a dial-up connection, the transfer depends on the setting of the parameter "Conditional":  - "Conditional" = TRUE (conditional spontaneous)   The data telegram is first saved on the TIM and transferred on the next connection establishment. - "Conditional" = FALSE (unconditional spontaneous)   The data telegram is transferred immediately. |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **ChnCnt** |
| Declaration: | INPUT |
| Data type: | Int |
| Range of values: | 1..12 |
| Explanation: | Number of transfer channels  Of the max. 12 channels of the object, between 1 and 12 channels can be defined. |

| Symbol | Meaning |
| --- | --- |
| Name: | **ChnSets** |
| Declaration: | INPUT |
| Data type: | WORD |
| Format: | Bit sequence of 16 bits |
| Default: | 0000000000000000 |
| Explanation: | Assignment of transfer channels to parameter set 1 or 2  Assign each channel via its bit to one of the two parameter sets, beginning with bit 1 for channel 1. Bit 0 always needs to be occupied with 0 (null) (reserved).  Coding of the individual bits:  - **0 =**    **Assignment of a channel to parameter set 1** - **1 =**    **Assignment of a channel to parameter set 2**   With the two parameter sets, you can transfer the channels differently. |
|  | **Example:**   - Parameter set 1   Important events, possible parameter assignment:   - ImageMemory01 = FALSE (Send buffer principle)   - Conditional01 = FALSE (Unconditional spontaneous)   - SendOnChange01 = TRUE (Transfer to TIM on change) - Parameter set 2   Operating data, possible parameter assignment:   - ImageMemory02 = TRUE (Image memory principle)   - Conditional02 = TRUE (Conditional spontaneous)   - SendOnChange02 = TRUE (Transfer to TIM on change) |
|  | **Note:**   "ImageMemory" and "Conditional" apply to the entire telegram.  - If sending of the telegram is triggered via "TriggerInput", then the entire telegram is sent as unconditional spontaneous send buffer telegram as soon as "ImageMemory" and "Conditional" are set to FALSE for a channel. - If sending of the telegram is triggered via "SendOnChange" to multiple channels, then the entire telegram is sent as unconditional spontaneous send buffer telegram as soon as "ImageMemory" and "Conditional" are set to FALSE for a channel. - If a change is only detected at one channel ("SendOnChange" = TRUE), then the telegram is sent in the mode that is specified by the "ImageMemory" and "Conditional" parameters of this channel. |

Assignment of the bits of the "ChnSets" parameter to the channels

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | **.15** | **.14** | **.13** | **.12** | **.11** | **.10** | **.9** | **.8** | **.7** | **.6** | **.5** | **.4** | **.3** | **.2** | **.1** | **.0** |
| **Channel** | **‑** | **‑** | **‑** | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | **‑ *** |
| ***** Bit 0 is reserved. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Parameter assignment example for "ChnSets": Assignment of seven channels to parameter set 1 or 2

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | .15 | .14 | .13 | .12 | .11 | .10 | .9 | .8 | **.7** | **.6** | **.5** | **.4** | **.3** | **.2** | **.1** | .0 |
| **Assignment** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 ***** |
| ***** Bit 0 is reserved.  Seven channels are assigned in the example. Channels 8..12 are not used.   **Coding of the individual bits:**   - 0 = Assignment to parameter set 1   In the example, the channels 2, 3 and 6 are assigned to parameter set 1. - 1 = Assignment to parameter set 2   In the example, the channels 1, 4, 5 and 7 are assigned to parameter set 2. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **DataInput01..12** |
|  | The parameter exists twelve times, once per channel. |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBXyy.0 TYPE zz  - xx: Data block number - yy: Byte number - TYPE: Data type   Permitted data types are: Bool, Byte, Char, SInt, USInt, Int, UInt, Word, DInt, DWord, Real, UDInt - zz: Length as number (specified data type) as of byte no. yy   Max. length: 1 DWord   Example: `P#DB20.DBX100.0 BYTE 3` Area with 3 bytes in DB20 as of DBB100 |
| Explanation: | Data input area  The ANY pointer addresses the data area in which the data to be acquired is located. The occupied null pointer is not permitted. Specify a pointer with a real address.  The data area must be in a data block and can have a maximum length of 4 bytes (max. 1 double word). |
|  | If not all 4 bytes are transferred for a channel or if they are not to be evaluated for triggering of the telegram (SendOnChange), make sure you observe the correct parameter assignment.  For information on the content and formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 4, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

##### Data typical Dat12x1D_R

###### Validity

S7-1500

###### Function

Receive data a maximum of 12 times with any data content via 12 channels for specific double words

You define the number of channels of the object used (1..12) in the "ChnCnt" parameter.

One data type is permitted per channel. You specify the data type for the content of a channel in the "DWxx_DataOut" parameter using the respective ANY pointer.

Dat12x1D_R saves the received data without further processing for specific channels in the respective data area specified at "DWxx_DataOut". You need to evaluate and process the received data with the user program.

> **Note**
>
> **DB with standard access**
>
> The typical uses an ANY pointer in the "DWx_DataOut" parameter. Therefore, disable the "Optimized block access" attribute in the properties of the DB.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| General parameters: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **ChnCnt** |
| Declaration: | INPUT |
| Data type: | Int |
| Range of values: | 1..12 |
| Explanation: | Number of transfer channels  Of the max. 12 channels of the object, between 1 and 12 channels can be defined. |

| Symbol | Meaning |
| --- | --- |
| Name: | **DW1_DataOut .. DW12_DataOut** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBXyy.0 TYPE zz  - xx: Data block number - yy: Byte number - TYPE: Data type   Permitted data types are: Bool, Byte, Char, SInt, USInt, Int, UInt, Word, DInt, DWord, Real, UDInt - zz: Length as number (specified data type) as of byte no. yy   Max. length: 1 DWord   Example: `P#DB20.DBX100.0 BYTE 3` Area with 3 bytes in DB20 as of DBB100 |
| Explanation: | Data output area  The parameter is available once for each channel (max. 12).  The ANY pointer addresses the data area in which the received data is saved. The occupied null pointer is not permitted. Specify a pointer with a real address.  The data area must be in a data block and can have a maximum length of 4 bytes (max. 1 double word).  If not all 4 bytes are to be output for a channel, make sure you observe the correct parameter assignment.  For information on the content and formats, refer to the section "Function" above. |
|  | Dat121xD_R stores the received data without further processing in the data area specified at "DataOutput". You need to evaluate and process the received data with the user program.  When only changed data is sent by the partner object Dat121xD_S, it is possible that only part of the data output area is re-written. this is the area in which the changes were detected at the acquisition end You can identify changed areas by "NewData".  If the parameter assignment is incorrect (null pointer, length &gt; 4, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

|  |  |  |
| --- | --- | --- |
| Name: | **NewData** |  |
| Declaration: | OUTPUT |  |
| Data type: | Array [0..11] of BOOL |  |
| Format: | Bit sequence of 16 bits |  |
| Range of values: | See address range |  |
| Default: | 0000000000000000 |  |
| Address range: | Output words | QW0 ... QWn PQW0 ... PQWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Receive new data  Whenever the block receives new data segments, the display of status bits 1 to 12 according to the received data segments 1 to 12 appears in "NewData".  If at least one data segment of the received data contains changes, bit 0 of "NewData" is set to TRUE for one OB1 cycle.  When receiving a sequence of several data segments (data telegrams), the status bits 1 to 12 in the "NewData" parameter are set to TRUE one after the other and remain set to TRUE until the last segment has been received.  The output is intended for user-specific further processing, for example to react in a specific way to receipt of new data.  If you do not require the parameter, simply leave it open. |  |

##### Data typical Dat256D_S

###### Function

Send a maximum of 256 double words with any data content

The content of each double word can be a value in double word format (DINT, REAL etc.). A combination of other formats is permitted that together result in a double word again, for example

- 32 Bool
- 4 bytes
- 2 words
- Any combination such as 2 bytes plus 1 word etc.

> **Note**
>
> **Remember double word boundaries**
>
> When changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 256 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

Sending the data area can be triggered in two ways:

- By a change check

  The data is transferred as soon as a bit changes ("SendOnChange" = TRUE).
- By the user program

  The transfer can be triggered by an edge change 0 → 1 at the "TriggerInput" input

  For time-driven transfer FC Trigger can be used.

With "SendAll" you can also specify whether the transfer always includes all data or only the data double words that have changed.

With S7-300 CPUs with X communication, the maximum length of a data frame is 76 bytes. 1024 bytes of net data are transferred using a serial transfer process consisting of a sequence of at least 22 data frames (segments). Each data frame apart from the last contains a segment of 48 bytes of net data of the input data area.

To ensure data consistency when the "SendAll" parameter is activated or during a general or single request, the data is transferred in consecutive segments. During the transfer process, the status is indicated by "SendAllBusy". On the recipient, the status is indicated at the "DataStatus" output.

> **Note**
>
> **TriggerInput ‑ SendAllBusy**
>
> If "TriggerInput" is triggered when "SendAllBusy" = TRUE, this leads to the "DataLoss" error message (status in the frame header) if the transfer is triggered again.
>
> Only when "SendAllBusy" = FALSE is set is the edge change 0 → 1 triggered at "TriggerInput".

If the transfer is interrupted, "SendAllError" is indicated. An entry is also made in the diagnostics buffer with the event ID B14DTD7_Diagnostics.

If the transfer is incomplete, the data status at the recipient is also "invalid". This is indicated on the recipient in the DataStatus parameter. Apart from this an entry with the event ID B13BTD7_Diagnostics is written to the diagnostics buffer.

> **Note**
>
> **Availability of the partner**
>
> If the status of the partner changes from "available" to "unavailable", the transfer of all data is stopped immediately. All object data is deleted from the TIM buffer. This can lead to loss of data.
>
> As soon as the partner is available again, the automatic general request ensures that the data of the partner is up-to-date again for the next transfer.

> **Note**
>
> **Dat256D_S and Dat256D_R require the UDT "TransmitBlock".**
>
> When using the typical, copy the UDT from the global library into the "PLC data types" directory of the CPU. The UDT is automatically referenced by the typical from the block directory of the CPU, but not from the global library.

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendOnChange** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Send on change  With the setting TRUE, the block runs a change check within the acquired data area "DataInput". The block checks whether at least one bit has changed. If a change is detected, a transfer of the data area is started automatically. You specify whether the entire area is transferred or only the changed part with the "SendAll" parameter.  If the setting is FALSE, you need to trigger the transfer via the input parameter "TriggerInput". |

|  |  |  |
| --- | --- | --- |
| Parameter: | **TriggerInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Trigger input  With the edge change 0 → 1 of the "TriggerInput" input, the transfer of the data frame can be triggered at a required time.  Example: Time-driven analog value transfer with time stamp for supplying an analog value archive in the control center.  The FC Trigger block can be used for time-driven triggering of a transmission over "TriggerInput".  "TriggerInput" actually only triggers transmission indirectly. With a 0 → 1 edge change at "TriggerInput", the data frame is put together with its current values and transferred to the local TIM. The TIM is responsible for the actual transmission to the partner. With dedicated lines or wireless networks the transfer is immediate. With a dial-up connection, it is possible that the data frame is saved first on the TIM and sent at a later point in time. The reason can, for example, be that the data frame is marked as "Conditional spontaneous", see parameter "Conditional". |  |
|  | Select suitable trigger points so that the data on the TIM is not overwritten by buffer overflow (intervals too long).  If you do not require the parameter, simply leave it open. You should, however, then set the "SendOnChange" parameter to TRUE so that the data is transmitted automatically at every change.  For the triggering you can also select a combination of "SendOnChange" plus "TriggerInput". This means that a transfer is triggered both when a change is detected and at every edge change from 0 to 1 at the "TriggerInput" input.  If you use neither "SendOnChange" nor "TriggerInput" to trigger data transfer, the data will only be transferred when there is a single request for this data object or within the framework of a general request.  Do not transfer any analog values for which the "SendOnChange" parameter = TRUE is set without first preprocessing the process data. You will find more detailed information on this with the analog value typical Ana04W_S, parameter "ThresholdValue". |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendAll** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | TRUE |
| Explanation: | Send all data with every transfer  With the parameter, you specify whether the block will always transfer all data of the area specified with "DataInput" or only changed data. The transfer can be triggered by the activated change check (SendOnChange = TRUE) or by "TriggerInput".  - SendAll = TRUE   Always send all data - SendAll = FALSE   Send only changed data   Exception: If "SendAll" is set to = FALSE, the transfer is triggered by "TriggerInput" and if no data has changed at this time, the complete area will be transferred. For this exception this corresponds to "SendAll" = TRUE.   If there is a single request for this data object or within the framework of a general request, all data words of the area specified by "DataInput" are always transferred. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DataInput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...256 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 200`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Data input area  The ANY pointer addresses the data area in which the data to be acquired is located. This data area must be within a data block and its length can vary between 1 and 256 data double words. For information on the possible double word formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 256, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.   **Data consistency;**  If a data segment to be transferred consists of a maximum of 48 bytes, data consistency during the transfer is assured. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendAllBusy** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Block being processed with "SendAll" = TRUE  This output indicates that the block is currently transferring the data specified by "DataInput". The procedure is activated either by a remote single or general request or by a local internal or external trigger.  If "SendAll" is set to TRUE, the transfer of all data is triggered either by internal change control (SendOnChange = TRUE) or by the external "TriggerInput" (edge change 0 → 1).  The edge change 0 → 1 has no effect whatsoever with an external "TriggerInput" as long as "SendAllBusy" indicates TRUE. The edge change 0 → 1 of "TriggerInput" only takes effect when "SendAllBusy" = FALSE. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **SendAllError** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Error when processing "SendAll"  "SendAllError" is set to TRUE when the connection is interrupted during processing of "SendAll". Apart from this an entry is written to the diagnostics buffer.  "SendAllError" remains set to TRUE until it is reset by the user program or by the next CPU restart. |

##### Data typical Dat256D_R

###### Function

Receive maximum of 256 double words with any data content.

The content of each double word may be a value in double word format (e.g. DINT, REAL etc.); it can also be a mixture of other formats which together form a double word, for example,

- 32 Bool
- 4 bytes
- 2 words
- Any combination such as 2 bytes plus 1 word etc.

> **Note**
>
> **Remember double word boundaries**
>
> When changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 256 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

Dat256D_R stores the received data without further processing in the data area defined by "DataOutput". Evaluate the received data with the user program.

With S7-300 CPUs with X communication, the maximum length of a data frame is 76 bytes (net 48 bytes). 1024 bytes of net data are transferred using a serial transfer process consisting of a sequence of at least 22 data frames (segments). Each data frame apart from the last contains a segment of 48 bytes of net data of the output data area.

Each time a detected data segment is received, this is indicated by a corresponding status (bit 1 to 22) of the "NewData" output parameter.

If a change was detected in the data segment, the status bit 0 is also set to TRUE in "NewData" for one CPU cycle. This makes it possible to recognize which segment of the output data area has changed.

> **Note**
>
> When receiving a sequence of several data segments (data frames), the status bits 1 to 22 in the "NewData" parameter are set to TRUE one after the other and remain set to TRUE until the last segment has been received.
>
> If a data segment (data frame) is not part of a received sequence (SendAll = FALSE), the status remains set to TRUE for only one CPU cycle.

To ensure data consistency when "SendAll"= TRUE or during a general or single request, the data area is updated in consecutive individual segments.

During receipt, the status is indicated by the "DataStatus" output byte ("SequenceState" status). If the receive sequence was completed successfully, the data output area is up-to-date and the output data is consistent. This is indicated by "DataStatus" ("DataValid" = TRUE status).

> **Note**
>
> The consistency of the data segments or the limit segments cannot be guaranteed if the "SendAll" parameter was set to FALSE on the sender.

Receipt of a sequence can be disrupted by the following causes:

- The receive sequence was interrupted when communication to the partner fails during an active sequence (event ID B13BTD7_Diagnostics).
- The monitoring time was exceeded. Not all segments could be received within the time set for the "MonitoringTime" parameter (event ID B13CTD7_Diagnostics).
- Other receiving errors occur (event ID B13DTD7_Diagnostics), for example:

  - A new receive sequence is registered during an active, error-free sequence.
  - A spontaneous segment (data frame) is received during an active sequence.

> **Note**
>
> **Dat256D_S and Dat256D_R require the UDT "TransmitBlock".**
>
> When using the typical, copy the UDT from the global library into the "PLC data types" directory of the CPU. The UDT is automatically referenced by the typical from the block directory of the CPU, but not from the global library.

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **SingleRequest** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | TRUE |  |
| Address range: | Input | I 0.0 … I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | A single request is sent to the partner object.  If the partner is available, you can send a single request to the partner object. If a reply is returned, the information is forwarded to the data area specified in "DataOutput".  In terms of transfer sequences, there are priorities:  - Lowest priority: TriggerInput   An active transfer triggered, for example, by "TriggerInput" on the sender can be interrupted by a single request or a general request. - Medium priority: Single request   An active transfer triggered, for example, by "TriggerInput" on the sender can be interrupted by a single request or a general request.   The interrupted or restarted request leads to a restart of the active sequences without an error message. - Highest priority: General request   A general request can interrupt itself or a single request.   The interrupted or restarted request leads to a restart of the active sequences without an error message.   The request interrupted or restarted by a single or general request leads to a restart of the active sequences without an error message. If a sequence was completed successfully, the "DataValid" status of the "DataStatus" output byte remains set to TRUE.  The time taken for the response to the single request is evaluated by the "MonitoringTime" parameter.   **Note:**  Consistency of the data output area across segments is only assured if the receive sequence was completed successfully. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **MonitoringTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 0 (no limit) / 1 … 32000 (seconds) |
| Default: | 0 |
| Explanation: | Maximum time for a complete response to a single request  Each time a single request starts (see SingleRequest parameter), the time specified here is started in "SingleRequest".  If a value higher than 0 is entered and the time for the response sequence is exceeded, an error is indicated via the "DataStatus" output byte (status bits "SequenceState"). Apart from this an entry is written to the diagnostics buffer (event ID B13CTD7_Diagnostics).  Each time a single request starts, "MonitoringTime" is reactivated. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **DataOutput** |
| Declaration: | INTPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...256 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 200`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Data output area  The ANY pointer addresses the data area in which the received data is saved. This data area must be within a data block and its length can vary between 1 and 256 data double words. For information on the possible double word formats, refer to the section "Function" above.  Dat256D_R stores the received data without further processing in the data area specified by "DataOutput". You need to evaluate and process the received data with the user program.  When only changed data is sent by the partner object Dat256D_S, it is possible that only part of the data output area is newly written. this is the area in which the changes were detected at the acquisition end  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **NewData** |  |
| Declaration: | OUTPUT |  |
| Data type: | DWORD |  |
| Range of values: | See address range |  |
| Default: | 0 (DW#16#0) |  |
| Address range: | Output (DWORD) | QD0 … QDn PQD0 … PQDn |
| Bit memory (DWORD) | MD0 … MDn LD0 … LDn |  |
| Data (DWORD) | DBm.DBB0 … n |  |
| Explanation: | Receive new data  Whenever the block receives new data segments, the display of status bits 1 to 22 according to the received data segments 1 to 22 appears in "NewData".  If at least one data segment of the received data contains changes, bit 0 of "NewData" is set to TRUE for one OB1 cycle.  When receiving a sequence of several data segments (data frames), the status bits 1 to 22 in the "NewData" parameter are set to TRUE one after the other and remain set to TRUE until the last segment has been received.  If a data segment (data frame) is not part of a received sequence ("SendAll" = FALSE), the status remains set to TRUE for only one CPU cycle.  The output is intended for user-specific further processing, for example to react in a specific way to receipt of new data.  If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **DataStatus** |  |
| Declaration: | OUTPUT |  |
| Data type: | BYTE |  |
| Range of values: | See address range |  |
| Default: | 0 (B#16#0) |  |
| Address range: | Output | QB0 … QBn PQB0 … PQBn |
| Memory bit | MB0 … MBn LB0 … LBn |  |
| Data | DBm.DBB0 … n |  |
| Explanation: | Currentness status of a received data segment  During receipt of a sequence, the current status is indicated by the "DataStatus" output byte:  - If the receipt of the sequence was completed successfully, the "DataOutput" data output area is up-to-date. The status bit "DataValid" is set to TRUE.   If "SendAll" is set to TRUE on the sender, the data is consistent. - If the receipt of a sequence is disrupted, the "DataOutput" data output area is not up-to-date and "DataStatus" indicates an error.   - The status bit "DataValid" is set to FALSE and an entry is written to the diagnostics buffer.   - The "SequenceState" status shows the error (see table). |  |

Bit assignment of "DataStatus"

| Bit | Name | Value | Meaning |
| --- | --- | --- | --- |
| 0 | **DataValid** | FALSE | Data invalid |
| TRUE | Data valid |  |  |
| 1 ... 5 | Reserved | ‑ (FALSE) | Not used |
| 7, 6 | **SequenceState** | 0 | No data being received or receipt completed without error. |
| 1 | First segment of a sequence received |  |  |
| 2 | Second or higher segment of a sequence received |  |  |
| 3 | Errors:  - Transmission sequence aborted - Monitoring time exceeded - Other error receiving |  |  |

##### Parameter typical Par12D_S

###### Function

Send 1 to 12 parameter values (each 1 double word) and receive the current, locally valid parameter values from the partner.

The block operates with 1-out-of-n test. The 1-out-of-n check is performed by FC Safe.

> **Note**
>
> **FC Safe required**
>
> With Par12D_S, data can only be transmitted when FC Safe is linked in the end of cyclic program, see Section [FC Safe](#fc-safe).

The content of each double word may be a value in double word (DWORD, DINT, REAL) format, it can also be a mixture of other data types which together form a double word, for example:

- 4 bytes
- 2 words
- 2 bytes + 1 word

See also the note "Note word boundaries" below.

The data area to be transferred is specified for the "ParameterInput" parameter in the form of an Any pointer. This data area must be within a data block and its length can vary between 1 and 12 double words. The data area sent to the partner or the parameter values entered locally at the partner are returned from there and output here at the "ReturnedParameter" parameter. This output area (Any pointer) must also be within a data block and its length must match that specified for "ParameterInput".

Separate data areas are normally specified for "ParameterInput" and "ReturnedParameter". This makes it easy to recognize what was most recently entered and what is locally valid. However, it is also possible to specify the same data area for both parameters. The two areas then overlap 100% and therefore always match. In this case, you can no longer distinguish the difference between what has been entered most recently and what is locally valid.

Even when separate areas are specified for "ParameterInput" and "ReturnedParameter", it is still possible to ensure that the "ParameterInput" input area is always synchronized with the mirrored back values of "ReturnedParameter". This can be done manually from case to case with the "ApplyRemoteParamMan" input or automatically by setting the "ApplyRemoteParamAuto" parameter to TRUE.

A parameter can also be set locally at the partner object that receives the parameter. The partner object must then be set to ’local’ at the "Local" input parameter (see block Par12D_R). The current status of the "Local" input parameter is reported by the partner object and indicated here at the "LocalOperation" output. As long as the partner object is set to 'local', no parameters are accepted there from other nodes.

The sending of the data area defined by "ParameterInput" can be triggered via the following parameters:

- EnterInput

  You should use this input parameter when the data area defined at "ParameterInput" is entered over hardware (digital and analog input modules). "EnterInput" must then be connected to a button on a console or panel via a digital input. The transmission of the entered values is then triggered by pressing this button.

  The entire data area specified by "ParameterInput" is transferred.
- ContinuousEnterFunct

  Set the parameter to TRUE if you enter the parameters using software, for example via an operator panel (OP). There is a constant check for changes. When a change is detected in the data area defined with "ParameterInput", the data double words that have changed since the last transfer are transferred.

  Only the changed data is transferred (see note "Changed data areas" below).
- Release

  Use this input parameter if you enter the parameters using software, for example via an OP. The "Release" input should then be set using a function key on the OP. Changes are checked when a 1 signal is detected at the "Release" input. The data double words from the data area specified with "ParameterInput" that have changed since the last transfer are transferred.

  Only the changed data is transferred (see note "Changed data areas" below).
- RetransmitAll

  Use this input parameter if you enter the parameters using software, for example via an OP. The "RetransmitAll" input should then be set using a function key on the OP. When a 1 signal is detected at the "RetransmitAll" input, the data area configured in "ParameterInput" is transferred without checking for changes.

  The entire data area specified by "ParameterInput" is transferred.

> **Note**
>
> **Changed data areas**
>
> When only the changed data area is transferred, this area consists of the first and the last double word in which a change was detected and all words located in between, even if these have not changed.
>
> Example:  
> The area to be read in is 10 double words long. In this case, changes were detected in the second, fifth and eighth double words. The transferred area is therefore from the 2nd to the 8th double word.
>
> **Remember word boundaries**
>
> When only changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 12 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **EnterInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Enter input  The transfer of the parameter values at the "ParameterInput" input can be triggered vis this input by a signal edge change.  A signal change at "EnterInput" is only taken into account when "ContinuousEnterFunct" = FALSE. If this condition is fulfilled, an edge change 0 → 1 causes the parameter values entered in "ParameterInput" to be adopted and transferred. There is no change check. The entire data area specified in "ParameterInput" is always transferred.  This method of triggering transfer is suitable for input vis hardware, for example via a console or control panel. For further information and related parameters, refer to the section "Function" above.  If you do not require the parameter, simply leave it open. |  |
|  | Data checks:  - The parameters that are read in are then transferred f no error is detected during the 1-out-of-n check, and if the central enable memory bit is set. This is automatically set by FC Safe following a selected time delay set there (see FC Safe, "InputDelayTime" parameter). The input area is then only read in again by the FB when a 0 signal was detected at EnterInput for at least one OB1 cycle. - When a 1-out-of-n error is detected at the hardware input, the entered parameters are no longer processed. New parameters are read in again only when previously for the length of an OB1 cycle, no hardware input via a command, setpoint or parameter block was detected.   The FB enters the detected 1-out-of-n error in the diagnostic buffer (event ID B172). As long as the error remains, the error status is indicated via the "InputError" output of FC Safe (see FC Safe, "InputError" parameter). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Continuous change check  With this parameter, you can decide whether the parameter values at the "ParameterInput" input should be continuously read in and checked for changes. The change check is made by comparison with the last values that were transferred. Only changed values are sent. If more than one change is detected, the block sends the data area in which all changed parameter values are located.  The changed data area that is transferred consists of the first and the last double word in which a change was detected and all words located in between, even if these have not changed.  A new transfer of the parameter values can be triggered via the "RetransmitAll" input (see below) even when the parameter entries have not changed.  This method of transmission triggering is suitable when the parameter values are entered in the ParameterInput area by software, but can also be used for entering the parameters from an operator panel (OP).  For further information refer to the section "Function" above.  If you do not require the parameter, simply leave it open. |
|  | Data checks:  The parameters read in are only transmitted if no error is detected during the 1-out-of-n check.  - While for hardware input (see EnterInput) an empty cycle must be detected before new parameter values can be transferred from the block. - For software input new parameter values can be transferred in every OB1 cycle. This assumes that there is no other software entry by another block pending in this cycle. Otherwise a 1-out-of-n error is detected.   When a 1-out-of-n error is detected during the software input, the entered parameters are no longer processed. The FB enters the detected 1-out-of-n error in the diagnostic buffer (event ID B172).   New parameters are read in again only when previously for the length of an OB1 cycle in the CPU, no software input via a command, setpoint or parameter block was detected. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ApplyRemoteParamAuto** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Automatic synchronization of the input area with the returned area.  With the parameter all the parameter values from the "ReturnedParameter" mirror back area are then copied to the "ParameterInput" area.  In addition to this the mirrored back parameter values are written the send mailbox of the communications DB.  Automatic synchronization is then always performed when new data is received from the partner object (Par12D_R).  If you do not require the parameter, simply leave it open. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ParameterInput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Parameter input area.  The ANY pointer addresses the data area in which the parameter values to be acquired are located. This data area must be within a data block and its length can vary between 1 and 12 data double words.  For information on the content and formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.  How the parameters at ParameterInput are processed depends on whether they are hardware or software entries and how the transfer of this data area is triggered. You will find more information on this in the section "Function" above. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ReturnedParameter** |
| Declaration: | OUTPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the preset value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Parameter output area  The partner object receiving the parameter values reports back the valid parameter values there. These values are displayed at the "ReturnedParameter" output. If the partner object is set to 'local' and a new input is made there, the parameters changed locally are indicated here by "ReturnedParameter".  The ANY pointer defines the data area in which the received parameter values are output. This data area must be within a data block and its length can vary between 1 and 12 data double words. The length must be identical with the length set for ParameterInput.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the current, local, valid parameters are indicated at "ReturnedParameter".  If the parameter setting is incorrect (data area not a data block, length greater than 12 or length different from the length set for ParameterInput), an error message to this effect is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The FB is then no longer processed, however, until the error has been corrected. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **LocalOperation** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Return message from partner object: Object is set to local operation.  At the partner object that receives the parameters a local setpoint entry can also be made.. The partner object Par12D_R must then be set to ’local’ at the "Local" input parameter. The current status of the "Local" input parameter is reported by the partner object and indicated here at the "LocalOperation" output.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the local currently valid status is displayed at "LocalOperation". |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new data and has output it to the output "ReturnedSetpoint" or "LocalOperation", the "NewData" output is set to TRUE for one OB1 cycle. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **Release** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Memory bit | M 0.0 ... M n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Trigger input for sending the currently pending parameter values  You can use this input parameter when the parameter is entered by software, for example at an operator panel (OP). "Release" should then be set using a function key on the OP. You can then enter several parameters initially on the OP. The parameters are transferred only when the Release function key is activated.  A change check is performed only with signal 1 at the Release input. The data double words from the data area configured with "ParameterInput" that have changed since the last transfer are transferred.  If you always want to transfer the entire data area specified with "ParameterInput" and not only the changed parameter values, you should use the "RetransmitAll" input parameter instead of "Release".  The "Release" input is reset automatically. You should therefore only specify memory bits or data bits as the input. The automatic reset would not work with a digital input.  Data checks: The same safety checks are carried out as with ContinuousEnterFunct, see above.  If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **RetransmitAll** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | TRUE |  |
| Address range: | Memory bit | M 0.0 ... M n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Trigger input for retransferring the entire data area specified by "ParameterInput".  You can use this input parameter when the parameter is entered by software, for example at an operator panel (OP). "RetransmitAll" should then be set using a function key on the OP. When a 1 signal is detected at the "RetransmitAll" input, the entire data area specified by "ParameterInput" is transferred. A change check is not performed  The "RetransmitAll" input is reset automatically. You should therefore only specify memory bits or data bits as the input. The automatic reset would not work with a digital input. Since there is no change check, this would lead to continuous transfer of all parameter values as long as the input has a 1 signal.  "RetransmitAll" can also be used as an option in addition to "Release" or "ContinuousEnterFunct" when new parameter values were entered but could not be transferred to the partner (disrupted connection or the partner object is set to ’local’). In this case you can then trigger repeated transfer of the entire data area specified by "ParameterInput" using "RetransmitAll". All changes that were previously entered but are not yet available at the partner are consistently included.  "RetransmitAll" can also be used as an independent transfer trigger when you always want to send all entries and not just those that have changed. In this case you can use "RetransmitAll" instead of "Release" that only sends the changed parameter values.  Data checks: The same safety checks are carried out as with "ContinuousEnterFunct", see above.  If you do not require the parameter, simply leave it open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ApplyRemoteParamMan** |
| Declaration: | IN_OUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Address range: | This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |
| Explanation: | Trigger input for synchronization of the input area with the returned area.  The input triggers a one-time synchronization of the ParameterInput input area with the "ReturnedParameter" mirror back area. All the parameter values from the "ReturnedParameter" mirror back area are then copied to the "ParameterInput" input area.  The send mailbox of the communications DB is also synchronized with the returned parameter values.  "ApplyRemoteParamMan" is reset automatically. You should therefore only specify memory bits or data bits as the input. The automatic reset would not work with a digital input. The result would be a constant synchronization as long as the parameter has a 1 signal.  If you do not require the parameter, simply leave it open. |

##### Parameter typical Par12D_FS

###### Validity

- S7-1500

###### Function

Send 1 to 12 parameter values (each 1 double word) without a 1-out-of-n check and receive the current, locally valid parameter values from the partner. This means that it is not necessary to call the FC Safe in the cyclic program.

There is less transmission security due to the lacking 1-out-of-n check.

No parameters are sent to subscribers that cannot be reached.

Frames of this block can be received and evaluated with the Par12D_R block.

The content per double word can be a value in double word format (DWORD, DINT, REAL).

> **Note**
>
> **Remember word boundaries**
>
> When only changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 12 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

The data area to be transferred is specified for the "ParameterInput" parameter in the form of an Any pointer. This data area must be within a data block and its length can vary between 1 and 12 double words. The data area sent to the partner or the parameter values entered locally at the partner are returned from there and output here at the "ReturnedParameter" parameter. This output area (Any pointer) must also be within a data block and its length must match that specified for "ParameterInput".

**Mirroring**

Separate data areas are normally specified for "ParameterInput" and "ReturnedParameter". This makes it easy to recognize what was most recently entered and what is locally valid.

However, the same data area can also be specified for both parameters. Both areas then overlap completely and are then always synchronized. In this case, you can no longer distinguish the difference between what has been entered most recently and what is locally valid.

Even when separate areas are specified for "ParameterInput" and "ReturnedParameter", it is still possible to ensure that the "ParameterInput" input area is always synchronized with the mirrored back values of "ReturnedParameter". You can perform this synchronization automatically by setting the "ApplyRemoteParam" parameter to TRUE.

A parameter can also be set locally at the partner object that receives the parameter. The "Local" input parameter must then be set to TRUE at the partner object. The locally valid parameters can be created by the partner object at the "LocalParameterInput" input parameter; they are then output here to "ReturnedParameter". The local status can be reported by the partner object via the "Local" parameter and displayed here at the "LocalOperation" output. The partner object can be set so that it does not accept any parameters from Remote when it is working in local mode (see Par12D_R block).

**Triggering sending**

Sending the data area defined at "ParameterInput" can be triggered by the following parameters:

- ContinuousEnterFunct

  Automatic transmission in case of a change in the area "ParameterInput" in the software mode of the block (HWmode = FALSE)
- Release

  Single triggered transmission in hardware and software mode of the block

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **HWmode** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | The parameter specifies whether the block works in hardware mode (TRUE) or software mode (FALSE).  - **Hardware mode**    Transmission can be triggered by a digital input module connected to the "Release" input.   The parameter value is applied in hardware mode when the signal at the release input changes from 0 to 1. Changes at the "ParameterInput" input while "InputDelayTime" is running are not sent. In hardware mode, the complete data area defined with "ParameterInput" is sent.   In hardware mode, an empty cycle must be detected at the "Release" input before new parameter values can be sent by the block. - **Software mode**    Sending can be triggered via the "Release" input or via the "ContinuousEnterFunct" function in software mode.   New parameter values can be sent in each OB1 cycle with a software input. The "ContinousEnterFunct" function can be switched on and off as required in the cycle.    **Note: Changed data areas**    In software mode, the block transmits selectively, that is, it only transmits the area of double words in which a change was detected. Exception: If no change is detected when the "Release" input is actuated, it sends the complete parameter area.   The changed data area consists of the first and the last double word in which a change was detected and all words located in between, even if these have not changed.   Example: The area to be read in is 10 double words long. In this case, changes were detected in the second, fifth and eighth double word. The transferred area is therefore from the 2nd to the 8th double word.   The "**HWmode**" parameter is applied during startup and cannot be changed in the cycle. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Continuous change check  The parameter is not evaluated if HWmode equals TRUE.  Set the parameter to TRUE if you enter the parameters using software or, for example, via an operator panel (OP).  There is a constant check for changes. The change check is made by comparison with the last values that were transferred.  As soon as a change is detected in the data area defined with "ParameterInput", this results in a transmission. The changed values are sent. If several changes are detected, the block sends the data area from the first to the last double word in which a change was detected.  A new transfer of the parameter values can be triggered via the "Release" input (see below) even when the parameter entries have not changed.  If you do not require the parameter, simply leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **ApplyRemoteParam** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | If the parameter has the value "TRUE", an automatic synchronization of the input area with the returned area is performed.  With the parameter all the parameter values from the "ReturnedParameter" mirror back area are then copied to the "ParameterInput" area.  In addition to this the mirrored back parameter values are written the send mailbox of the communications DB.  Automatic synchronization is then always performed when new data is received from the partner object (Par12D_R). Synchronization can also be triggered once with a signal transition from 0 to 1, for example, manually via a pushbutton.  If the parameter has the value "FALSE" or the parameter is not specified, no automatic synchronization of the input area with the returned area is performed. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ParameterInput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Parameter input area.  The ANY pointer addresses the data area in which the parameter values to be acquired are located. This data area must be within a data block and its length can vary between 1 and 12 data double words.  For information on the content and formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 7). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.  The way in which the values present at "ParameterInput" are subsequently processed depends on whether it is a hardware or a software input and how the transmission is triggered. You can find more information on this in the "Function" section above and under the "HWmode" parameter. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ReturnedParameter** |
| Declaration: | OUTPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the preset value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Parameter output area  The partner object receiving the parameter values reports back the valid parameter values there. These values are displayed at the "ReturnedParameter" output. If the partner object is set to 'local' and a new input is made there, the parameters changed locally are indicated here by "ReturnedParameter".  The ANY pointer defines the data area in which the received parameter values are output. This data area must be within a data block and its length can vary between 1 and 12 data double words. The length must be identical with the length set for ParameterInput.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the current, local, valid parameters are indicated at "ReturnedParameter".  If the parameter setting is incorrect (data area not a data block, length greater than 12 or length different from the length set for ParameterInput), an error message to this effect is entered in the diagnostics buffer (event ID B114, [Info2/3] = 8). The CPU does not change to STOP. The FB is then no longer processed, however, until the error has been corrected. |

| Symbol | Meaning |
| --- | --- |
| Name: | **InputDelayTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   When the parameter is not required - 1 ... 32000   Value range for delay time (milliseconds) in hardware mode |
| Explanation: | Delay time in milliseconds for the "Release" input when the block is operating in hardware mode.  A delay time of at least 1000 ms is recommended.  Changes to "ParameterInput" while "InputDelayTime" is running are not sent in the current cycle. |

| Symbol | Meaning |
| --- | --- |
| Name: | **MaxInputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   When the parameter is not required. - 1 ... 32000   Value range for monitoring time (seconds) when "HWmode" = TRUE. |
| Explanation: | Monitoring time in seconds for the "Release" input when the block is operating in hardware mode.  A monitoring time of at least 30 s is recommended.  If you do not require the parameter, leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **Release** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Trigger input for sending the currently pending parameter values  You can use the parameter in software or hardware mode of the block.  - **Hardware mode**    When you use the input via an OP, it should be operated via a function key of the OP. You can then enter several parameters initially on the OP. The parameters are transferred only when the Release function key is activated.   In hardware mode, the "Release" input is not automatically reset. You should therefore only specify memory bits or data bits as the input. The automatic reset would not work with a digital input.   The "Release" input is subject to the "InputDelayTime" and is monitored via "MaxInputTime". If the input is set longer than "MaxInputTime", the timeout is output at "InputError". The "InputError" output does not change back to "0" until the "Release" input is also = 0. (See also "InputError") - **Software mode**    A change check is performed only with signal 1 at the Release input. The data from the "ParameterInput" area that has changed since the last transmission is sent. If no change is detected when activating the "Release" input, the block transmits the complete parameter area.   In software mode, the "Release" input is automatically reset. You should therefore only specify memory bits or data bits as the input.   If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **LocalOperation** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Return message from partner object: Object is set to local operation.  A parameter can also be set locally at the partner object that receives the parameter. The partner object Par12D_R must then be set to 'local' at the "Local" input parameter. The current status of the "Local" input parameter is reported by the partner object and indicated here at the "LocalOperation" output.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the local currently valid status is displayed at "LocalOperation". |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new data and has output it to the output "ReturnedParameter" or "LocalOperation", the "NewData" output is set to TRUE for one OB1 cycle. |

|  |  |  |
| --- | --- | --- |
| Name: | **InputOK** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | The display "InputOK" is set for one cycle at the entry of the data frame into the send buffer. The display is independent of the "HWmode" parameter.  If you do not require the parameter, leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **InputError** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Display of input errors at the "Release" input, if "HWmode" equals TRUE.  The output has a 1 signal as soon as the "Release" command lasts longer than defined via MaxInputTime. The "InputError" output is only set to 0 again when the release input has a 0 signal. This can be used, for example, to detect that the input is defective.  If you do not require the parameter, leave it open. |  |

##### Parameter typical Par12D_S

###### Function

Receive 1 to 12 parameter values (each 1 double word) or enter locally and send back the current, locally valid parameter values to the partner.

The block can receive and output data of the "Par12D_S" and "Par12D_FS" typicals.

The content of each double word may be a value in double word (DWORD, DINT, REAL) format, it can also be a mixture of other data types which together form a double word, for example:

- 4 bytes
- 2 words
- 2 bytes + 1 word

See also the note "Note word boundaries" below.

The data area to be transferred is specified for the "ParameterOutput" parameter in the form of an Any pointer. This data area must be within a data block and its length can vary between 1 and 12 double words.

You can also use the block to enter the parameter values locally. The input area for this is specified as an Any pointer with the "LocalParameterInput" parameter. It must be located within a data block and its length must be identical to the length configured in the "ParameterOutput" parameter.

The block only processes the changed data area. In response to a general or single request, on the other hand, the entire parameter set is transferred or mirrored back..

Bumpless switchover between the "Local" and "Remote" operating modes is guaranteed.

> **Note**
>
> **Changed data areas**
>
> The changed data area consists of the first and the last double word in which a change was detected and all words located in between, even if these have not changed.
>
> Example:  
> The area to be read in is 10 double words long. In this case, changes were detected in the second, fifth and eighth double words. The transferred area is therefore from the 2nd to the 8th double word.
>
> **Remember word boundaries**
>
> When only changed data is transferred and the data area contains values in double word format, make sure that the double word values are actually located in one of the maximum 12 double words of the data area to be acquired.
>
> Distribution over two consecutive data double words could lead to the transfer of only one word of the double word value (high or low word) because a change has occurred in only that particular word. In this case, the missing word can lead to a data error on the receiving partner (applies to ST7cc, not for an S7 CPU).

> **Note**
>
> **DB with standard access**
>
> The block has parameters of the "ANY" type. Therefore, leave the "Optimized block access" attribute in the properties of the DB disabled.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **Local** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Local parameter input released  Release of the local parameter input of the data area specified by "LocalParameterInput".  A setpoint sent by the partner (master station) is not accepted by the object as long as "Local" = TRUE.  The current status of the "Local" input is transferred to the partner.  Bumpless switchover:  - When there is a switchover from "Local" = 0 to 1, the last values output at the "ParameterOutput" output are retained until new parameter values are entered via the local input area "LocalParameterInput". - When there is a switchback from Local = 1 to 0, the last values at the "ParameterOutput" output are retained until the block receives new parameter values from the partner.   Read the note on the "ContinuousEnterFunct" parameter.   **Special situation:**   You can also enter the parameter values during local input directly in the output area specified by "ParameterOutput". Either you do not specify an input area for "LocalParameterInput" or you specify the same data area both for "LocalParameterInput" and "ParameterOutput".  This type of parameter input cannot be prevented by the "Local" input. Regardless of the status of the "Local" parameter, the values entered in the output area are sent immediately by the block to the partner.  Local parameter entries can therefore be made regardless of the status of the "Local" input. "Local" only influences the acceptance of parameters sent by the partner:  - Local = 0   The parameters sent by the partner are accepted and output to the "ParameterOutput" data area. - Local = 1   The parameters sent by the partner are rejected.   In this special situation, the "Release" and "ContinuousEnterFunct" have no function.  A status change of the "Local" parameter is always transferred by the module according to the send buffer principle, even when the parameter "ImageMemory" = TRUE. This ensures that the optional synchronization of the input and output area on the partner is always performed correctly (see Par12D_S, parameters "ApplyRemoteParamMan" and "ApplyRemoteParamAuto"). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Continuous local parameter acquisition.  With this parameter, you can decide whether the values in the "LocalParameterInput" input area should be continuously read in and checked for changes. The change is checked by comparing the current values at the "ParameterOutput" output.  Changes in the input area are copied immediately to the output area and transferred to the partner object. Only changed values are sent. If there is more than one change, the block sends the data area in which all changed parameter values are located.  The "ContinuousEnterFunct" = TRUE setting only takes effect when the following conditions are met:  - An input area is defined by "LocalParameterInput" and this is not identical to the output area set for "ParameterOutput".   and - there is a 1 signal at the "Local" input (= TRUE).   With the setting "ContinuousEnterFunct" = TRUE, when the signal 1 is detected at the "Local" input, the values pending at "LocalparameterInput" are adopted immediately and output at the "ParameterOutput" output. The condition is that the local input values differ from the currently output values at this time.  This method of acquisition of local values is suitable when the values are entered in the "LocalParameterInput" area by software.  If you do not require the parameter, simply leave it open. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **LocalParameterInput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the default value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Local parameter input area  The ANY pointer addresses the data area in which the parameter values to be acquired are located. This data area must be within a data block and its length can vary between 1 and 12 data double words. The length must be identical to the length specified for" ParameterOutput".  For information on the content and formats, refer to the section "Function" above.  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected.  If you do not require the parameter, simply leave it open. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ParameterOutput** |
| Declaration: | INPUT |
| Data type: | ANY |
| Range of values: | See address range |
| Default: | P#P 0.0 VOID 0 (null pointer) |
| Address range: | P#DBxx.DBX yy.0 DWORD zz  - xx: Data block number 1...32767 - yy: Byte number - zz: Number of double words 1...12 starting at byte number yy   Example: `P#DB20.DBX 100.0 DWORD 4`  Remember the periods and spaces when entering the pointer!  Note that the preset value (null pointer) is not permitted. A pointer with a real address must be specified. |
| Explanation: | Parameter output area  The ANY pointer addresses the data area in which the locally entered parameter values or those received from the partner are output. This data area must be within a data block and its length can vary between 1 and 12 double words.  For information on the content and formats, refer to the section "Function" above.  Par12D saves the received data without further processing in the data area specified by "ParameterOutput". You need to evaluate and process the received data with the user program.  When only changed data is sent by the partner object Par12D_S, it is possible that only part of the data output area is newly written. this is the area in which the changes were detected at the acquisition end  If the parameter assignment is incorrect (null pointer, length &gt; 12, data area not a DB), an error message is entered in the diagnostics buffer (event ID B114, [Info2/3] = 11). The CPU does not change to STOP. The block is then no longer processed, however, until the error has been corrected. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new parameter values from the partner object and has output them to the output field "ParameterOutput", the "NewData" output is set to TRUE for one OB1 cycle. This also applies when there is new local input in the status "Local" = 1. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **Release** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Input for the acceptance of local parameter input.  The acceptance of the parameter values at the "LocalParameterInput" parameter input can be triggered via this input by a signal edge change.  A change from 0 to 1 at the "Release" input is taken into account only when the following conditions are met:  - An input area is specified by the "LocalParameterInput" parameter and this is not identical to the output area specified by "ParameterOutput"   and - The "Local" input is set to TRUE. |  |
|  | You can use "Release" for parameter input via software, e.g. via an operator panel (OP). The "Release" input should then be set using a function key on the OP. You can then enter several parameters initially on the OP. The parameter values are read in and checked for changes only when the Release function key is activated.  The change is checked by comparing the current parameter values at the "ParameterOutput" output. Changes in the input area are then copied immediately to the output area and transferred to the partner.  Only changed values are sent. If there is more than one change, the block sends the data area in which all changed parameter values are located.  The "Release" input is reset automatically. Instead of a memory bit or data bit, a digital input can also be specified as the input. The automatic reset would not work with a digital input. This does not, however, have negative effects. Acquisition via "Release" is edge triggered, in other words only once.  If you do not require the parameter, simply leave it open. |  |

##### FC Safe

###### Function

The FC Safe ensures reliable input of commands and setpoints by using the 1-out-of-n check.

The FC Safe checks th einput for the following data point typicals:

- Cmd01B_S
- Set01W_S
- Par12D_S

If an input is pending, the FC checks whether there is only one entry pending in the current OB1 cycle and then enables the block reading in. As soon as two (or more) entries are pending in an OB1 cycle, both entries are ignored.

> **Note**
>
> **Follow the call sequence when using FS blocks**
>
> If you want to use, in addition to the Cmd01B_S, Set01W_S or Par12D_S blocks, also the Cmd01B_FS, Set01W_FS or Par12D_FS blocks, you have to call these blocks after the FC Safe.

In every CPU in which commands and/or setpoints are acquired, the FC Safe needs to be called once in OB1 to complete all command and setpoint FBs Cmd01B_S, Set01W_S or Par12D_S.

The FC has separate monitoring for entries via different system memory areas. They are divided into hardware entries and software entries:

- Hardware entries

  - Input modules (I)
  - Peripheral inputs (PI)
- Software entries

  - Bit memory (M)
  - Data blocks (DB)
  - Local data (L)
  - Operator panels

The two types of entry "hardware entries" and "Software entries" are checked separately by the block. The FC enables the hardware and software entries separately. For each type of entry, only one command or setpoint entry may be detected.

If a single hardware entry and a single software entry are pending at the same time both entries are enabled.

For hardware entries, the following additional condition applies: The entry must be pending constantly for the duration of "InputDelayTime". Only when an entered command or setpoint is pending unchanged for this time and during this time no other command or setpoint entry is detected is the block processing enabled.

The actual putting together of the command or setpoint frame is handled by the block that read in the command or setpoint.

For the hardware entry the FC Safe provides the following two display bits:

- InputOK

  Display of the enabling of hardware commands and setpoints
- InputError

  Display of entry errors with hardware commands and setpoints

FC-Safe shows a command output error detected in a station via the following output:

- GlobalCmdOutputError

  Group message: Command output error in a station

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Name: | **InputDelayTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0   Value for unrequired parameter - 1 ... 32000   Range of values for delay time |
| Explanation: | Delay time in ms for commands and setpoints that are input via hardware.  A delay time of at least 1000 ms is recommended. |

| Symbol | Meaning |
| --- | --- |
| Name: | **MaxInputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0   Value for unrequired parameter - 1 ... 32000   Range of values for monitoring time |
| Explanation: | Monitoring time in ms for commands and setpoints that are input via hardware.  A monitoring time of at least 30 s is recommended.  If you do not require the parameter, specify 0 (zero). |

|  |  |  |
| --- | --- | --- |
| Name: | **ResetError** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Input for resetting the output GlobalCmdOutputError.  If you do not require the parameter, specify a memory or data bit that always has signal 0. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **InputOK** |  |
| Declaration: | - S7‑300 - S7‑1500 | - OUTPUT - IN_OUT |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Display of the enabling of hardware commands and setpoints  Has a 1 signal as soon as the current entry was enabled, i.e. when the hardware command or setpoint was entered correctly.  The display bit goes off when the entry is reset, in other words when the command key is released or the setpoint entry key "EnterInput" input is released.  If you do not require the parameter, specify a memory or data bit in the memory area of the local data. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **InputError** |  |
| Declaration: | - S7‑300 - S7‑1500 | - OUTPUT - IN_OUT |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Display of entry errors with hardware commands and setpoints  The output has a 1 signal when one of the following hardware entry errors is detected within the monitoring time "MaxInputTime":  - Two or more command and/or setpoint entries were detected at the same time. - At one of the inputs a 1 signal was detected over a longer period of time (for example when the input is defective).   If you do not require the parameter, specify a memory or data bit in the memory area of the local data. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **GlobalCmdOutputError** |  |
| Declaration: | - S7‑300 - S7‑1500 | - OUTPUT - IN_OUT |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Group message: In a station a command output error was detected.  A command output error can occur at the receive end only in the following cases:  - The content of the two command bytes in the received frame is not identical. - More than one bit is set in the command byte (1-out-of-8 error).   If such an error is detected, this is sent by the station with an organizational frame to the subscriber that sent the commands. FC Safe on the sending subscriber then indicates the disruption at the output GlobalCmdOutputError.  When an error is detected, the output remains set to the 1 signal until you request the group signal to be reset via the "ResetError" input.  If you do not require the parameter, specify a memory or data bit in the memory area of the local data. |  |

##### Setpoint typical Set01W_S

###### Function

Send 1 setpoint as a 16 bit value and receive local setpoint from partner

The 1-out-of-n check is performed by FC Safe.

> **Note**
>
> **FC Safe required**
>
> With Set01W_S, data can only be transferred when the block FC Safe is linked in the end of the cyclic program, see section [FC Safe](#fc-safe).

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **EnterInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Enter input for hardware setpoint  The adoption of a setpoint at the "SetpointInput" can be triggered by a signal edge change.  A signal change at "EnterInput" is only taken into account when "ContinuousEnterFunct" = FALSE. If this condition is fulfilled, an edge change 0 → 1 causes the setpoint entered in "SetpointInput" to be adopted and transferred. This also applies when the newly entered setpoint is identical to the last setpoint transferred.  This method of setpoint adoption is suitable for input vis hardware, for example via a console or control panel.  It can also be used for entering setpoints at an operator panel (OP). In this the adoption must be triggered by a function key on the OP.  If you do not require the parameter, simply leave it open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Apply setpoint continuously for software setpoint  With this parameter, you specify whether the setpoint at "SetpointInput" should be continuously read in and checked for changes. Changes are checked by comparison with the last setpoint that was transferred.  This method of setpoint adoption is suitable for input via suitable software. It can, however, also be used for entering setpoints at an operator panel (OP) if the OP does not have a separate function key that can be used to trigger the input.  If you do not require the parameter, simply leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **SetpointInput** |  |
| Declaration: | INPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Input words | IW0 ... IWn PIW0 ... PIWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Setpoint input  How a setpoint available at SetpointInput is processed depends on whether it is a hardware or software input. You specify the type of input with the "ContinuousEnterFunct" parameter:  - **ContinuousEnterFunct = FALSE**    **(hardware input)**    A setpoint at "SetpointInput" is only read in as long as the signal is 1 at "EnterInput". The setpoint that is read in is then transferred if no error is detected during the 1-out-of-n check, and if the central enable memory bit is set. This is automatically set by FC Safe following a selected time delay set there (see FC Safe, "InputDelayTime" parameter).   A further setpoint is then only read in again by the FB when a 0 signal was detected at EnterInput for at least one OB1 cycle.   When a 1-out-of-n error is detected at the hardware input, the entered setpoint is no longer processed. A new setpoint is read in again only when previously for the length of an OB1 cycle in the CPU, no hardware input via a command, setpoint or parameter block was detected.   The FB enters the detected 1-out-of-n error in the diagnostic buffer (event ID B172). As long as the error remains, the error status is indicated via the "InputError" output of FC Safe (see FC Safe, "InputError" parameter). |  |
|  | - **ContinuousEnterFunct = TRUE**    **(software input)**    A setpoint at SetpointInput is read in continuously and checked for changes. Changes are checked by comparison with the last setpoint that was transferred. The setpoint is sent immediately every time a change occurs unless the 1-out-of-n check detects an error.   - With hardware input (see EnterInput) an empty cycle must be detected before a new setpoint can be transferred by the block.   - With software input a new setpoint can be transferred in every OB1 cycle. This assumes that there is no other software entry by another block pending in this cycle. Otherwise a 1-out-of-n error is detected.     A new transfer of the software setpoint can be triggered via the "SendSoftSetpoint" input even when the software input has not changed (see below).     When a 1-out-of-n error is detected at the software input, the entered setpoint is no longer processed.     A new setpoint is read in again only when previously for the length of an OB1 cycle in the CPU, no software input (command or setpoint) was detected. The block enters detected 1-out-of-n errors in the diagnostics buffer (event ID B172). Appropriate error bits are also set in the central data block BasicData where they can be queried by the software. For further details, refer to the description of FC Safe. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **ReturnedSetpoint** |  |
| Declaration: | OUTPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Output words | QW0 ... QWn PQW0 ... PQWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Output for a returned setpoint  The partner object receiving the setpoint reports back the currently valid setpoint there. This value is displayed at the "ReturnedSetpoint" output.  If the partner object is set to 'local' and a new input is made there, the setpoint changed locally is indicated here by "ReturnedSetpoint".  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the locally valid setpoint is indicated by "ReturnedSetpoint".  If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **LocalOperation** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Return message from the partner object: The object is set to local operation.  A setpoint can also be set locally at the partner object that receives the setpoint. The partner object Set01W_R must then be set to ’local’ at the "Local" input parameter. The current status of the "Local" input parameter is reported by the partner object and indicated here at the "LocalOperation" output.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the local currently valid status is displayed at "LocalOperation".  If you do not require the parameter, simply leave it open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new data and has output it to the output "ReturnedSetpoint" or "LocalOperation", the "NewData" output is set to TRUE for one OB1 cycle. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **SendSoftSetpoint** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Memory bit | M 0.0 ... M n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Trigger input for resending the last software setpoint.  For further details, refer to the "SetpointInput" parameter.  If you do not require the parameter, simply leave it open. |  |

##### Setpoint typical Set01W_FS

###### Function

Send 1 setpoint as a 16 bit value and receive local setpoint from partner

Frames of this block can be received and evaluated with the Set01W_R block.

Sending the setpoint can be triggered by the following parameters:

- ContinuousEnterFunct

  Automatic transmission in case of a change in the area "ParameterInput" in the software mode of the block (HWmode = FALSE)
- Release

  Single triggered transmission in hardware and software mode of the block

No setpoints are sent to stations which cannot be reached.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **HWmode** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | The parameter specifies whether the block works in hardware mode (TRUE) or software mode (FALSE).  - **Hardware mode**    Transmission can be triggered by a digital input module connected to the "Release" input.   The setpoint is applied in hardware mode when the signal at the release input changes from 0 to 1.   Changes made to the setpoint input "SetpointInput" while the "InputDelayTime" is running are not sent.   In hardware mode, an empty cycle must be detected before new parameter values can be sent by the block. - **Software mode**    Sending can be triggered via the "Release" input or via the "ContinuousEnterFunct" function in software mode.   New parameter values can be sent in each OB1 cycle with a software input. The "ContinousEnterFunct" function can be switched on and off as required in the cycle.   The "**HWmode**" parameter is applied during startup and cannot be changed in the cycle. |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Apply setpoint continuously for software setpoint  The parameter is not evaluated if HWmode equals TRUE.  With this parameter, you specify whether the setpoint at "SetpointInput" should be continuously read in and checked for changes. Changes are checked by comparison with the last setpoint that was transferred. Sending occurs even if the value at "SetpointInput" has not changed since the last transmission.  This method of setpoint adoption is suitable for input via suitable software. It can, however, also be used for entering setpoints at an operator panel (OP) if the OP does not have a separate function key that can be used to trigger the input.  If you do not require the parameter, simply leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **SetpointInput** |  |
| Declaration: | INPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Input words | IW0 ... IWn PIW0 ... PIWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Setpoint input  The way in which the value at "SetpointInput" is subsequently processed depends on whether it is a hardware or a software input and how transmission is triggered. You can find more information on this in the "Function" section above and under the "HWmode" parameter. |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **InputDelayTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   Value for unrequired parameter - 1 ... 32000   Value range for delay time (milliseconds) in hardware mode |
| Explanation: | Delay time in milliseconds for the "Release" input when the block is operating in hardware mode.  A delay time of at least 1000 ms is recommended.  Changes to "SetpointInput" while "InputDelayTime" is running are not sent in the current cycle. |

| Symbol | Meaning |
| --- | --- |
| Name: | **MaxInputTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 or open   When the parameter is not required. - 1 ... 32000   Value range for monitoring time (seconds) when "HWmode" = TRUE. |
| Explanation: | Monitoring time in seconds for the "Release" input when the block is operating in hardware mode.  A monitoring time of at least 30 s is recommended.  If you do not require the parameter, leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameters: | **Release** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter type and this should not be used. |  |  |
| Explanation: | Trigger input for sending the current setpoint  You can use the parameter in software or hardware mode of the block.  - **Hardware mode**    When you use the input via an OP, it should be operated via a function key of the OP. You can then first enter the setpoint at the OP. The value is only sent when you press the release function key.   In hardware mode, the "Release" input is not automatically reset. You should therefore only specify memory bits or data bits as the input. The automatic reset would not work with a digital input.   The "Release" input is subject to the "InputDelayTime" and is monitored via "MaxInputTime". If the input is set longer than "MaxInputTime", the timeout is output at "InputError". The "InputError" output does not change back to "0" until the "Release" input is also = 0. (See also "InputError") - **Software mode**    A change check is performed only with signal 1 at the Release input. Sending occurs even if the value at "SetpointInput" has not changed since the last transmission.   In software mode, the "Release" input is automatically reset. You should therefore only specify memory bits or data bits as the input.   If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **ReturnedSetpoint** |  |
| Declaration: | OUTPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Output words | QW0 ... QWn PQW0 ... PQWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Output for a returned setpoint  The partner object receiving the setpoint reports back the currently valid setpoint there. This value is displayed at the "ReturnedSetpoint" output.  If the partner object is set to 'local' and a new input is made there, the setpoint changed locally is indicated here by "ReturnedSetpoint".  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the locally valid setpoint is indicated by "ReturnedSetpoint".  If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **LocalOperation** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Return message from the partner object: The object is set to local operation.  A setpoint can also be set locally at the partner object that receives the setpoint. The partner object Set01W_R must then be set to ’local’ at the "Local" input parameter. The current status of the "Local" input parameter is reported by the partner object and indicated here at the "LocalOperation" output.  After startup of the local or partner CPU, or after restoring a connection, an automatic general request ensures that the local currently valid status is displayed at "LocalOperation".  If you do not require the parameter, simply leave it open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received new data and has output it to the output "ReturnedSetpoint" or "LocalOperation", the "NewData" output is set to TRUE for one OB1 cycle. |

|  |  |  |
| --- | --- | --- |
| Name: | **InputOK** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | The "InputOK" display is also set for one cycle with the entry in the send buffer. The display is independent of the "HWmode" parameter. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **InputError** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... Q n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Display of input errors at the "Release" input, if "HWmode" equals TRUE.  The output has a 1 signal as soon as the "Release" command lasts longer than defined via MaxInputTime. The "InputError" output is only set to 0 again when the release input has a 0 signal. This can be used, for example, to detect that the input is defective.  If you do not require the parameter, leave it open. |  |

##### Setpoint typical Set01W_R

###### Function

Receive 1 setpoint in the station as a 16 bit value or enter locally and return the local setpoint to the master station

The block can receive and output data of the "Set01W_S" and "Set01W_FS" typicals.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Parameter: | **PartnerNo**    **PartnerObjectNo**    **Enabled**    **ImageMemory**    **Conditional**    **Unconditional**    **TimeStamp** |
| For a description, see section [Reoccurring parameters](#reoccurring-parameters). |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **Local** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Release of the local setpoint input of the data area specified by "LocalSetpointInput".  A setpoint sent by the partner (master station) is not accepted by the object as long as "Local" = TRUE.  The current status of the "Local" input is transmitted to the partner together with a copy of the setpoint which is currently being output at "SetpointOutput" (setpoint mirroring).  Bumpless switchover:  - When there is a switchover from "Local" = 0 to 1, the last values output at the "SetpointOutput" output are retained until a new setpoint is entered via the local input area "LocalSetpointInput". - When there is a switch back from "Local" = 1 to 0, the last value output at the "SetpointOutput" output is retained until the block receives a new setpoint from the partner.   Read the note on the "ContinuousEnterFunct" parameter. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **EnterInput** |  |
| Declaration: | INPUT |  |
| Data type: | BOOL |  |
| Range of values: | TRUE / FALSE |  |
| Default: | FALSE |  |
| Address range: | Input | I 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation: | Enter input for local setpoint input.  Edge triggered, the parameter triggers adoption of the setpoint at the setpoint input "LocalSetpointInput".  A signal change at "EnterInput" is only taken into account when the value TRUE is set at the "Local" input parameter and "ContinuousEnterFunct" = FALSE. If these conditions are fulfilled, a signal change from 0 to 1 at the causes the setpoint entered at "LocalSetpointInput" to be adopted and output at "SetpointOutput".  This method of setpoint adoption is suitable for hardware input, for example via a console, control panel or an operator panel (OP). With an OP, the adoption must be triggered by a function key.  If you do not require the parameter, simply leave it open. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **ContinuousEnterFunct** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Default: | FALSE |
| Explanation: | Continuous local setpoint acquisition  When "Local" = TRUE and "ContinuousEnterFunct" = TRUE the setpoint at "LocalSetpointInput" is continuously read in and checked for changes.  The setpoint read in at "LocalSetpointInput" is output at the "SetpointOutput" output if at this time the local input value differs from the last returned setpoint.  If an array is detected at the setpoint input "LocalSetpointInput" this is output immediately at "SetpointOutput" (without a change check).  This method of setpoint adoption is suitable for software input.  It can, however, also be used for entering setpoints at an operator panel (OP) if the OP does not have a function key.  If you do not require the parameter, simply leave it open. |

|  |  |  |
| --- | --- | --- |
| Parameter: | **LocalSetpointInput** |  |
| Declaration: | INPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Input words | IW0 ... IWn PIW0 ... PIWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Local setpoint input  A value at "LocalSetpointInput" is only adopted if "Local" = TRUE. If this condition is met, how a pending setpoint is processed depends on whether it is a hardware or software input. The type of input is decided by the "ContinuousEnterFunct" parameter: |  |
|  | - ContinuousEnterFunct = FALSE   Hardware input   A setpoint at "LocalSetpointInput" is only read in when a signal change 0 → 1 is detected at "EnterInput". The setpoint entered locally is output via the "SetpointOutput" output and transferred to the partner.   A further setpoint is then only read in again by the block when a 0 signal was detected at "EnterInput" for at least one OB1 cycle. |  |
|  | - ContinuousEnterFunct = TRUE   Software input   A setpoint at "LocalSetpointInput" is read in continuously and checked for changes. The change check is achieved by comparison with the last valid setpoint; in other words, the value stored as the returned setpoint. With each change, the setpoint is output via the output set at "SetpointOutput" and transferred to the partner.   With software input a new setpoint can be entered in every OB1 cycle.   With hardware input an empty cycle must be detected before a new setpoint can be read in by the block.  If you do not require the parameter, simply leave it open. |  |

|  |  |  |
| --- | --- | --- |
| Parameter: | **SetpointOutput** |  |
| Declaration: | OUTPUT |  |
| Data type: | WORD |  |
| Range of values: | See address range |  |
| Default: | 0 (W#16#0) |  |
| Address range: | Output words | QW0 ... QWn PQW0 ... PQWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation: | Setpoint output word.  The setpoint sent by the partner object or entered locally at "LocalSetpointInput" is output at the "SetpointOutput" output. |  |

| Symbol | Meaning |
| --- | --- |
| Parameter: | **NewData** |
| Explanation: | For the declaration, data type, range of values, default and function, refer to the section [Reoccurring parameters](#reoccurring-parameters).  Whenever the block has received a new setpoint from the partner object and has output it to "SetpointOutput", the "NewData" output is set to TRUE for one OB1 cycle. This also applies when there is a new local setpoint input (Local = 1). |

#### Optional blocks

This section contains information on the following topics:

- [ListGenerator1500/300/400 FC](#listgenerator1500300400-fc)
- [FC PartnerMonitor](#fc-partnermonitor)
- [FC PartnerStatus](#fc-partnerstatus)
- [FC PathStatus](#fc-pathstatus)
- [FC PulseCounter](#fc-pulsecounter)
- [FC ST7ObjectTest](#fc-st7objecttest)
- [FC TestCopy](#fc-testcopy)
- [DB TestCopyData](#db-testcopydata)
- [Operation of TestCopyMonitor](#operation-of-testcopymonitor)
- [FC TimeTask](#fc-timetask)
- [FC Trigger](#fc-trigger)

##### ListGenerator1500/300/400 FC

The ListGenerator FC is available in three versions with the following symbolic names:

- For S7-300

  ListGenerator300
- For S7-400

  ListGenerator400
- For S7-1500

  ListGenerator1500

###### Function

The FC ListGenerator is required in a CPU that receives data containing either an incomplete destination address or no destination address at all. The lack of the destination object number is the most important factor here because this points to the instance DB in which the received information should be stored.

Missing or incomplete destination addresses can occur when no or incomplete parameters are set for them in the station. This is permitted for typicals that send binary information, analog values or counted values. If these typicals send data to more than one destination, no destination address is set for them. Due to the missing destination information, the send frame is automatically transmitted to all destinations for which a connection was set up during configuration. This data is therefore received without a destination address at the various destinations.

> **Note**
>
> **Supplement to destination subscriber no.**
>
> Data frames to be sent without a destination address have the destination subscriber number added by the sending TIM, and sometimes several if there are several destinations.
>
> The TIM enters 0 in the address field for the destination object number, since the TIM does not have the relevant information. The only destination subscribers it knows are those to which it has a configured connection.
>
> At the receiving end, the data frame therefore contains the destination subscriber number but the destination object number is 0.

If the destination object number is not contained in the received data frame, FC Distribute, which is responsible for distributing the received frames, references an object reference list.

Using the source address (source subscriber no. + source object no.) contained in every data frame, FC Distribute searches through the list for an entry that specifies the missing destination object number for the given source address; in other words, it searches for the number of the local instance DB.

This object reference list is created by FC ListGenerator. The FC has no parameters. It is linked into the cyclic user program (OB1) following the FC BasicTask.

When creating the list, FC ListGenerator uses the addresses set in the parameters for the receiving typicals. Specification of "PartnerNo" and "PartnerObjectNo" is mandatory for these typicals. These parameters are identical to the source address in the corresponding receive frame. Since the typical also knows the number of its instance DB, it therefore knows all the addresses required for an entry in the reference list.

During startup, FC ListGenerator arranges that all receiving typicals enter the addresses from their parameter assignment with the number of the instance DB in the reference list. The object reference list therefore does not require special parameter settings, it is simply created from the existing parameters of the receive typicals and is therefore always consistent.

###### How it works

FC ListGenerator creates the lists after startup in three consecutive OB1 cycles:

- In the first cycle, it determines how many entries will be required in the first and, if applicable, in the second object reference list. The typicals involved only increment a counter during this run.
- In the second cycle, FC ListGenerator generates the data block for the first and, if applicable, the second object reference list with the required length and enters 0 in all the data words. During the same cycle, all typicals involved enter their addresses and the number of the corresponding instance DB in the list.
- In the third and final cycle, FC ListGenerator sorts all the entries in ascending order. Sorting speeds up the search in the list during actual operation.

When generating the data block, FC ListGenerator does the following:

If no list has yet been created, a search is made for a free DB number.

- S7-1500

  The FC searches in descending order in the range from 60999 to 60000 (reserved area) for a free DB number.
- S7-300/400

  Starting with the number of DB BasicData, the number of the next lowest free DB is taken.

If a list already exists, FC ListGenerator checks to see whether the existing DB is long enough for the currently required number of references. If the length is adequate, 0 is entered as the content and the addresses are written again and sorted.

The object reference list 1 can be used in full length (65532 bytes) for max. 10922 receive objects. The maximum number of objects without a target object number is 10922.

If the existing data block is too short, different procedures are used for the various SIMATIC product series:

- For S7-300

  A new DB is generated. The old DB remains in memory because S7-300 has no delete function for data blocks.

  With the 300 CPU, you have to delete the old DBs with the programming device.

  Note:  
  Without generating a new DB, you would need to delete this DB with the programming device. If there is not enough memory on the CPU to be able to generate a new DB, you need to delete the existing DB before restarting.
- For S7-400

  The existing DB is deleted, the memory is compressed and the DB is then generated with the same number in the new length.

  With the 400 CPU, you may be able to manually compress the memory or reload the CPU.
- For S7-1500

  The existing DB is deleted and generated in the new length with the same number.

  With the 1500 CPU, the memory is automatically compressed, just like with the 300 CPU.

If the ListGenerator FC can no longer generate a DB, an error message is written to the diagnostic buffer of the CPU:

- 0xB107 "Error generating the object reference list"

  - DB[Info1] cannot be created.
  - Cause: [Info2].

    In Info2, the return value of the SFC Create_DB function is output, refer to the description there.

##### FC PartnerMonitor

###### Function

FC PartnerMonitor has the following functions:

- It displays important status information about a SINAUT subscriber (see "PartnerStatus" parameter).
- The FC can also be used to trigger a general request of the subscriber, except to a control center (e.g. ST7cc/ST7sc).
- It can also be used to establish and terminate a permanent connection to the subscriber.

The FC can be called at any point in the cyclic user program (in OB1).

If you want to monitor and control more than one subscriber, include an appropriate number of FC PartnerMonitor in the user program.

A SINAUT subscriber (partner) can only be an ST7 CPU or an ST7cc to which a connection was configured. TIMs cannot be monitored or controlled by FC PartnerMonitor.

> **Note**
>
> **FC PartnerMonitor in a station**
>
> FC PartnerMonitor can also be used in a station. However, the control inputs for establishing and terminating a permanent connection can then no longer be used. This only works in the master station when the local TIM is a master station TIM.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Name: | **PartnerNo** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 1 ... 32000 [ms] |
| Explanation | SINAUT subscriber no. of the subscriber to be monitored and controlled.  If the set "PartnerNo" is not found in the administration (DB BasicData), then (only during startup) an entry is written to the diagnostics buffer (event ID B101). The CPU does not change to STOP.  The status of a subscriber with correct parameter settings is indicated in the "PartnerStatus" output word and the control inputs are processed.  An unknown subscriber is not processed until the error is eliminated. The "PartnerStatus" output word remains set to 0 during this time. |
|  |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **MaxConnectTime** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0 (no limitation) - 1 … 480 [minutes] |
| Explanation | Maximum duration of a permanent connection  The time specified here (&gt; 0) is activated at the start of a permanent connection (see "PermanentCall_On" parameter).  If the time elapses before the permanent connection is reset, it is automatically disconnected. The time is retriggered as long as the signal 1 is present at the "PermanentCall_On" input.  The time specified here applies to a permanent connection in a dial-up network as well as to a permanent connection (continuous polling) on a dedicated line. |
|  |  |

|  |  |  |
| --- | --- | --- |
| Name: | **PartnerStatus** |  |
| Declaration: | OUTPUT |  |
| Data type: | WORD |  |
| Range of values: | Output words | QW0 ... QWn PQW0 ... PQWn |
| Memory words | MW0 ... MWn LW0 ... LWn |  |
| Data words | DBm.DBW0 ... n |  |
| Explanation | Output word to indicate the status of the subscriber to be monitored.  If you do not require the parameter, simply leave it open. |  |

**The meaning of the status bits in the "PartnerStatus" output word:**

| Bit | .0 | Status of the subscriber |
| --- | --- | --- |
|  | 0 | 0 = Subscriber disrupted |
| 1 | 1 = Subscriber OK |  |

| Bit | .1 | Status of the redundant connection |
| --- | --- | --- |
|  | 0 | 0 = Redundant connection is disrupted |
| 1 | 1 = All connections OK. |  |

| Bit | .3 | .2 | Status of the general request (GR) |
| --- | --- | --- | --- |
|  | 0 | 0 | 0 = GR complete without error |
| 0 | 1 | 1 = GR started |  |
| 1 | 0 | 2 = GR start received |  |
| 1 | 1 | 3 = GR finished with error (GR incomplete or cannot be executed, e.g. due to fault at subscriber) |  |

| Bit | .6 | .5 | .4 | Status of the dial-up connection |
| --- | --- | --- | --- | --- |
|  | 0 | 0 | 0 | 0 = No connection |
| 0 | 0 | 1 | 1 = Outgoing call activated |  |
| 0 | 1 | 0 | 2 = Incoming call established |  |
| 0 | 1 | 1 | 3 = Outgoing call established |  |
| 1 | 0 | 0 | 4 = Permanent connection registered |  |
| 1 | 0 | 1 | 5 = Permanent connection established |  |
| 1 | 1 | 0 | 6 = Permanent connection disconnected |  |

| Bit | .7 | Status of the dial-up connection |
| --- | --- | --- |
|  | 0 | 0 = No dial-up connection check in background |
| 1 | 1 = Dial-up connection check in background is activated |  |

| Bit | .8 | Status of continuous polling (on dedicated line) |
| --- | --- | --- |
|  | 0 | 0 = No continuous polling |
| 1 | 1 = Continuous polling activated |  |

| Bit | .9 | Status of the WAN connection resources |
| --- | --- | --- |
| *) | 0 | 0 = Sufficient resources on partner |
| 1 | 1 = Insufficient resources on partner |  |

| Bit | .10 | Time status |
| --- | --- | --- |
|  | 0 | 0 = Date/time not available / not OK on partner |
| 1 | 1 = Date/time OK on partner |  |

| Bit | .11 | Time-of-day synchronization |
| --- | --- | --- |
|  | 0 | 0 = The partner CPU received a plausible time during the last synchronization or no time of day has been received since startup. |
| 1 | 1 = The partner CPU has received an implausible time of day; the last valid time will continue to be used.  (Display only with TimeMask &gt; V1.6) |  |

> **Note**
>
> **In-out parameters**
>
> The following parameters are in/out parameters (declaration IN_OUT):
>
> - GeneralRequest
> - PermanentCall_On
> - PermanentCall_Off
>
> It is difficult to specify local bit memory with this parameter type and this should not be used.

|  |  |  |
| --- | --- | --- |
| Name: | **GeneralRequest** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | Input  Memory bit  Data bit | I 0.0 ... I n.7  M 0.0 ... M n.7  DBm.DBX 0.0 ... n.7 |
| Explanation | Input for triggering a general request to the subscriber specified with PartnerNo.  A general request to the subscriber is triggered with a 1 signal at this input if no request is active for this subscriber at this time. The input is then automatically reset by the FC.  If an input of a digital input is specified (I 0.0 ... I n.7), you are responsible for resetting the signal at the input. Reset the signal before ending the currently running general request so that another general request is not triggered immediately. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **PermanentCall_On** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | Input  Memory bit  Data bit | I 0.0 ... I n.7  M 0.0 ... M n.7  DBm.DBX 0.0 ... n.7 |
| Explanation | Input for triggering a permanent connection to the subscriber specified with PartnerNo.  A permanent connection to the subscriber is triggered with a 1 signal at this input if there is currently no permanent connection to this subscriber. The input is then automatically reset by the FC. If an input of a digital input is specified (I 0.0 ... I n.7), you are responsible for resetting the signal at the input at the latest before the termination of the existing permanent connection.  A 1 signal at the input "PermanentCall_On" also activates the time specified with "MaxConnectTime" if it is greater than 0.  Depending on whether the subscriber can be reached over a dial-up connection or a dedicated line, the command to establish the permanent connection is processed as follows and indicated at the "PartnerStatus" output:  - **For a dial-up connection:**    A dial-up connection is established by the master TIM to the appropriate subscriber and, regardless of the data traffic, maintained until the terminate command is sent. The current status of the permanent connection is indicated in the PartnerStatus output word with the bits 4 ... 6 (see PartnerStatus parameter). - **For a dedicated line:**    In this case the master TIM operates in polling mode with the stations. A permanent connection is implemented in this case by ’continuous polling’ of the subscriber. This is actually an intermittent poll to the subscriber; in other words, the other subscribers on the dedicated line network are still polled but the preferred subscriber is polled again after every poll to a ’normal’ subscriber . The current status of the continuous polling is indicated by bit 8 in the "PartnerStatus" output parameter.    **Special feature with stations:**   A permanent connection cannot be established from a station. This control input cannot therefore be used when FC PartnerMonitor is used in a station. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **PermanentCall_Off** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | Input  Memory bit  Data bit | I 0.0 ... I n.7  M 0.0 ... M n.7  DBm.DBX 0.0 ... n.7 |
| Explanation | Terminating an existing permanent connection  The input serves to trigger termination of an existing permanent connection to the subscriber specified with "PartnerNo".  A permanent connection to the subscriber is terminated with a 1 signal at this input if there is currently a permanent connection to this subscriber. The input is then automatically reset by the FC. If an input of a digital input is specified (I 0.0 ... I n.7), you are responsible for resetting the signal at the input via the user program. This should be done at the latest before establishing a permanent connection again.  Depending on whether the subscriber can be reached over a dial-up connection or a dedicated line, the command to terminate the permanent connection is processed as follows and indicated at the "PartnerStatus" output:  - **For a dial-up connection:**    The existing dial-up connection is terminated by the master TIM but only after any pending data has been sent. The current status of the permanent connection is indicated in the PartnerStatus output word with the bits 4 ... 6 (see PartnerStatus parameter). - **For a dedicated line:**    The master TIM deletes the registration for continuous polling of the corresponding subscriber. The polling cycle for all connected subscribers continues in normal mode. The current status of the continuous polling is indicated by bit 8 in the "PartnerStatus" output parameter.   Continuous polling can also be canceled on a dedicated line by instructing the master TIM to start continuous polling of another subscriber. The existing job is then replaced by the new one.    **Special feature with stations:**   A permanent connection cannot be terminated by a station. This control input cannot therefore be used when FC PartnerMonitor is used in a station. |  |

##### FC PartnerStatus

###### Function

The FC PartnerStatus can show the current status ’disrupted’ or ’OK’ for a maximum of 8 SINAUT subscribers.

The FC can be called at any point in the cyclic user program (in OB1).

If you want to monitor more than 8 subscribers, include the appropriate number of FCs PartnerStatus in the user program.

The partner can be an ST7 CPU or an ST7cc to which a connection was configured, or a local TIM.

One bit per subscriber is reserved in the "PartnerStatus" output byte to indicate the status of the respective subscriber:

- FALSE (0):

  - Subscriber disrupted
  - Corresponding input parameter not used (= 0)
  - Subscriber unknown
- TRUE (1): Subscriber OK

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Name: | **Partner1 ... Partner8** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 0   Value for unrequired parameter - 1 ... 32000   Number of the subscriber to be monitored |
| Explanation | SINAUT subscriber number of the subscriber to be monitored  If a set subscriber number is not found in the administration (DB BasicData), then (only during startup) an entry is written to the diagnostics buffer (event ID B101). The CPU does not change to STOP.  The status of a subscriber with a correct parameter assignment is indicated in the "PartnerStatus" output byte.  An unknown subscriber is not processed until the error is eliminated. Their status bits are set to 0. |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name: | **PartnerStatus** |  |  |  |  |  |  |  |  |
| Declaration: | OUTPUT |  |  |  |  |  |  |  |  |
| Data type: | BYTE |  |  |  |  |  |  |  |  |
| Range of values: | Output bytes |  |  | QB0 ... QBn PQB0 ... PQBn |  |  |  |  |  |
| Memory bytes |  |  | MB0 ... MBn LB0 ... LBn |  |  |  |  |  |  |
| Data bytes |  |  | DBm.DBB0 ... n |  |  |  |  |  |  |
| Explanation: | Indication of the status of the subscriber to be monitored. |  |  |  |  |  |  |  |  |
|  | Assignment of the status bits in the "PartnerStatus" output byte depending the parameters Partner1 ... "Partner8": |  |  |  |  |  |  |  |  |
| **Bit** | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |  |
| **Partner** | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Value:  - 0 = partner disrupted, not set in the parameters or unknown - 1 = partner OK |  |  |  |  |  |  |  |  |  |

##### FC PathStatus

###### Function

The block (FC) shows the status of the path to a partner from the perspective of the local TIM.

A maximum of 2 paths (main and substitute path) to a partner can be configured. Both paths must begin or end on a local TIM.

The block shows the following:

- The paths via which the partner can be reached.
- The path currently being used
- The TIM interface via which the main path was configured.
- The TIM interface via which the substitute path was configured.

The path of a connection is specified as a combination of the used interfaces of the TIM and the status of the path.

In the output byte PathStatus the following bits are reserved:

- Two bits for the interface of the main path
- Two bits for the interface of the substitute path

- Two bits for the status of the main path
- Two bits for the status of the substitute path

The FC can be called at any point in the cyclic user program (OB1) after calling the FC BasicTask.

If the status of the path to more than one subscriber is to be shown, a corresponding number of FC calls need to be programmed in the user program program.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Name: | **Partner** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | 1 ... 32000 (subscriber number) |
| Explanation: | SINAUT subscriber no. of the partner |

|  |  |  |
| --- | --- | --- |
| Name: | **PathStatus** |  |
| Declaration: | OUTPUT |  |
| Data type: | BYTE |  |
| Range of values: | Output bytes | QB0 ... QBn PQB0 ... PQBn |
| Memory bytes | MB0 ... MBn LB0 ... LBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| Explanation: | Display of the path status of the connection to the partner |  |

###### PathStatus ‑ Coding

Coding of the status bits in the "PathStatus" output byte

| Bits 6 + 7 | Bits 4 + 5 | Bits 2 + 3 | Bits 0 + 1 |
| --- | --- | --- | --- |
| **Configured interface** |  | **Path status** |  |
| No. for substitute path | No. for main path | Substitute path (2nd path) | Main path (1st path) |

**Configured interface (bits 4..7)**

The TIM interfaces in the block are consecutively numbered decimally from 0 to 3, see "No." column in the table. The table shows the coding of the bits for the different TIM types.

Coding of bits 4 + 5 (interface of the main path) or bits 6 + 7 (interface of the substitute path)

| Status bit 5 (7) | Status bit 4 (6) | Interfaces |  |  |  |
| --- | --- | --- | --- | --- | --- |
| No. | TIM 3V‑IE | TIM 4R‑IE | TIM 1531 IRC |  |  |
| 0 | 0 | 0 | Ethernet "IE1" (X2) | Ethernet "IE1" (X3) | Ethernet "IE1" (X1) |
| 0 | 1 | 1 | **‑** | Ethernet "IE2" (X4) | Ethernet "IE2" (X2) |
| 1 | 0 | 2 | Serial "WAN1" (X1) | Serial "WAN1" (X1) | Ethernet "IE3" (X3) |
| 1 | 1 | 3 | **‑** | Serial "WAN2" (X2) | Serial "WAN" (X4) |

**Path status (bits 0..3)**

- Main path = 1. Path (bits 0 + 1)
- Substitute path = 2nd path (bits 2 + 3)

Status table: Coding of bits 0 + 1 or bits 2 + 3

| Status bit 1 (3) | Status bit 0 (2) | Meaning bit 1 | Meaning bit 0 |
| --- | --- | --- | --- |
| 0 | 0 | Path not current | Subscriber not reachable |
| 0 | 1 | Path not current | Subscriber reachable |
| 1 | 0 | Path current | Subscriber not reachable |
| 1 | 1 | Path current | Subscriber reachable |

##### FC PulseCounter

###### Function

The FC PulseCounter is responsible for count pulse acquisition.

A maximum of 8 pulse strings are detected via digital inputs and fed to the function blocks with the aid of SIMATIC counters that put together the counted value frames (Cnt01D_S, Cnt04D_S).

The acquisition of the count pulses is time-controlled To do this the FC PulseCounter must be included in a cyclic interrupt OB, e.g. OB35. The call interval of the cyclic interrupt OB must be matched to the pulse duration of the count pulses. You will find more information on count pulse acquisition with the cyclic interrupt OB in the section [Cyclic interrupt OB](#cyclic-interrupt-ob).

###### Parameters

|  |  |  |
| --- | --- | --- |
| Name: | **InByte** |  |
| Declaration: | INPUT |  |
| Data type: | BYTE |  |
| Range of values: | Input bytes | PEB0 ... PEBn |
| Memory bytes | MB0 ... MBn LB0 ... LBn |  |
| Data bytes | DBm.DBB0 ... n |  |
| If an input byte of a digital input is specified, this must be the address of the I/O byte (PIB) directly from the digital input modules. The current status of the count input can only be detected reliably by direct access.  When reading out from the process image of the inputs (PII) count pulses could remain undetected. |  |  |
| Explanation: | Input byte for count pulses.  The parameters for inputs for count pulse acquisition can can be set in bytes. |  |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name: | **EnableMask** |  |  |  |  |  |  |  |  |
| Declaration: | INPUT |  |  |  |  |  |  |  |  |
| Data type: | BYTE |  |  |  |  |  |  |  |  |
| Range of values: | B#16#00 ... B#16#FF |  |  |  |  |  |  |  |  |
| Explanation | Enable mask for the counting inputs  With this parameter, it is possible to specify in the form of a bit mask at which inputs in the input byte count pulses are actually connected. The following applies to every bit in the bit mask:  - 0 = Input bit blocked for acquisition - 1 = Input bit enabled for acquisition   The input of the mask is only permitted in hexadecimal format B#16#00 to B#16#FF.  Input as an 8-bit binary number from 2#0 to 2#1111 1111 is not possible with the data type BYTE. |  |  |  |  |  |  |  |  |
|  | The assignment of the bits in the mask to the inputs in the input byte "InByte": |  |  |  |  |  |  |  |  |
| InByte | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |  |
| EnableMask B#16# | 0 … F |  |  |  | 0 … F |  |  |  |  |
|  | Example: | EnableMask B#16#83  Enabled are: Inputs .7, .1 and .0  Blocked are: Inputs .6 to .2 |  |  |  |  |  |  |  |

| Symbol | Meaning |
| --- | --- |
| Name: | **CntIn_0 ... CntIn_7** |
| Declaration: | INPUT |
| Data type: | COUNTER |
| Range of values: | C0 or C1 ... Cn (n depends on the CPU) |
| Explanation | Pulse counter  For each of the enabled counting inputs a SIMATIC counter needs to be specified for the corresponding parameter CntIn_0 ... . "CntIn_7". With each pulse acquired, the SIMATIC counter is incremented.  The counters set here must be specified as input counters (parameter Counter_1 ... _4) in the actual counted value function blocks "Cnt01D_S" and "Cnt04D_S". These function blocks out read the assigned counter and then reset it.  As the placeholder for parameters that are not required, it is recommended to specify the counter C0. |
|  | Example of the parameter assignment of "CntIn_0" ... "CntIn_7" starting at "EnableMask" = B#16#83:  CntIn_0 : = Z10 CntIn_1 : = Z11 CntIn_2 : = Z0 CntIn_3 : = Z0 CntIn_4 : = Z0 CntIn_5 : = Z0 CntIn_6 : = Z0 CntIn_7 : = Z12 |

##### FC ST7ObjectTest

###### Validity

S7-300/400 CPU

###### Function

Calling FC ST7ObjectTest in programming error OB121 prevents a CPU STOP, if the CPU receives data with an unknown destination object no.

FC ST7ObjectTest checks why OB121 was called, i.e. which block type is missing.

- If the missing block is a data block and this data block is an instance DB of a SINAUT object, the CPU does not change to STOP.
- If no SINAUT instance DB is missing but rather another block (DB, FB, FC), you can specify the reaction with the parameter "StopInOtherCases".

  - CPU changes to STOP.
  - CPU continues to run.

For more information on the programming error OB121 and background information relating to the use of FC ST7ObjectTest, see section [Programming error OB](#programming-error-ob).

###### Parameter

| Symbol | Meaning |
| --- | --- |
| Name: | **StopInOtherCases** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Explanation: | The CPU should change to STOP in other error situations.  For details of the parameter see above, section "Function".  - TRUE: CPU changes to STOP. - FALSE: CPU continues to run. |

##### FC TestCopy

###### Function

Using FC TestCopy, extracts of the data traffic between ST7 subscribers can be recorded or the entire traffic can be recorded. With search masks to be set in the control field of DB TestCopyData individual frame types can be filtered out and then copied from the send or receive buffer for further evaluation in the DB TestCopyData. For details, see below.

Send and receive frames are all stored in the same data block DB TestCopyData. This makes it simple to track the chronological order of the copied send and receive frames.

**Requirements**

To use the TestCopy function, the user program must meet the following conditions:

- The FC TestCopy function must be available on the CPU.
- DB TestCopyData must be present on the CPU and have a sufficient length.

  - To achieve this, copy DB TestCopyData (DB99) from the TD7 library to your CPU.
  - If necessary, change the length of the buffer area in the DB by increasing or decreasing the size of the array "TestCopyBuffer" in DW40, which has the default length of [0..240] WORD.
- Make the following entries in the respective communication DB of the CPU 300/400 (BComData / XComData / PComData) whose send and/or receive frames you want to write:

  - In DW32 (TestCopyDBNo) of the communication DB, enter the number of the DB TestCopyData.
  - In DW34 (TestCopyFCNo) of the communication DB, enter the number of the FC TestCopy.

  Proceed in the same way for the communication DB of CPU 1500. The tags in DB BConnectData have the same names.

**Linking FC TestCopy into the user program**

If the above-mentioned conditions are fulfilled, the test function is processed cyclically by the respective communication FB of the CPU.

FC TestCopy cannot be called in the user program.

**Monitoring the written data**

Use the ready-made watch table "TestCopyMonitor", which you can copy from the TD7 library into the "Watch and force tables" directory of the CPU.

If the settings are to be retained even after CPU startup, they can also be stored directly in the start values of the individual BConnection instances of the DB BConnectData.

##### DB TestCopyData

###### Structure of the TestCopyData DB

**Areas of the TestCopyData DB**

The DB for the TestCopy function is divided into the following areas (after Offset in the DB):

- **0 ... 27: User interface**

  Interface for setting the TestCopy mode and functions. The area is divided into:

  - 1 ... 13  
    Filter settings for RecvCopy function and number of counted received frames
  - 15 ... 25  
    Filter settings for SendCopy function and number of counted sent frames
- **28: Error display**
- **31 ... 39: Internal management pointer**
- **40 ... (Default: 523): Buffer range**

  Buffer area for storing frames that match the filter criteria.

  The buffer area must be configured as an array [0...xxxx] of WORD.

The following table shows the structure of the DB TestCopyData:

| Data type / (offset) |  | Tag name | Format | Explanation |
| --- | --- | --- | --- | --- |
| **User interface** |  |  |  |  |
| DBB | 0 | OperationMode | BYTE | Mode |
| DBW | 12 | Recv_TgramCounter | INT | Number of copied receive frames |
| DBW | 26 | Send_TgramCounter | INT | Number of copied send frames |
| RecvCopy function |  |  |  |  |
| DBB | 1 | Recv_TgrmType | BYTE | Receive filter: Message type (MT) |
| DBW | 2 | Recv_DestSubscr | INT | Receive filter: Destination subscriber no. |
| DBW | 4 | Recv_DestObject | INT | Receive filter: Destination object no. |
| DBW | 6 | Recv_SourceSubscriber | INT | Receive filter: Source subscriber no. |
| DBW | 8 | Recv_SourceObject | INT | Receive filter: Source object no. |
| DBW | 10 | Recv_StartIndex | INT | Receive filter: Start index no. |
| DBB | 14 | SpareDBB14 | BYTE | Reserve |
| SendCopy function |  |  |  |  |
| DBB | 15 | Send_TgrmType | BYTE | Send filter: Message type (MT) |
| DBW | 16 | Send_DestSubscr | INT | Send filter: Destination subscriber no. |
| DBW | 18 | Send_DestObject | INT | Send filter: Destination object no. |
| DBW | 20 | Send_SourceSubscriber | INT | Send filter: Source subscriber no. |
| DBW | 22 | Send_SourceObject | INT | Send filter: Source object no. |
| DBW | 24 | Send_StartIndex | INT | Send filter: Start index no. |
| **Error display** |  |  |  |  |
| DBB | 28 | FC_RetVal | BYTE | Error information:  0 = No error  1 = DB TestCopyData too short  10 = Unknown mode |
| DBB | 29 | SpareDBB29 | BYTE | Reserve |
| DBB | 30 | SpareDBB30 | BYTE | Reserve |
| **Internal management pointer** |  |  |  |  |
| DBB | 31 | TestCopyStatus | BYTE | Status byte for TestCopy operation |
| DBB | 32 | TestCopyCmdByte | BYTE | Command byte for TestCopy operation |
| DBB | 33 | TestCopyDelCount | BYTE | Loop counter for TestCopy delete function |
| DBW | 34 | NextFreeCopyByte | INT | Address of the next free TestCopyBuffer byte |
| DBD | 36 | StartTimeSFC64 | DINT | SFC64 time at the start of the copy procedure |
| **Buffer range** |  |  |  |  |
| DBB | 40 | TestCopyBuffer[0] | BYTE | Copy area, byte 0 |
| DBB | 41 | TestCopyBuffer[1] | BYTE | Copy area, byte 1 |
| DBB | 42 | TestCopyBuffer[2] | BYTE | Copy area, byte 2 |
| DBB | 43 | TestCopyBuffer[3] | BYTE | Copy area, byte 3 |
| DBB | n | TestCopyBuffer[n] | BYTE | Copy area, byte n |

**Structure of a copied message block**

A frame block can contain several frames. The frames are saved in the DB TestCopyData according to the following rules:

1. The first entry indicates the time difference in milliseconds (7 decade BCD plus sign) since the last selection of an operating mode &gt; 0.
2. This is followed by a separation sign AAAA for sent messages, EEEE for received messages.
3. Storage of the first message from the frame block.
4. Separation identifier AAAA, or EEEE:
5. Storage of the last frame from the message block.
6. Block end identifier FFFF.

**Example**

- All received frames will be stored in DB TestCopyData.
- Communication via X blocks, i.e. max. 76 bytes per receive block.
- The receive buffer of the DB XComData is the source for FC TestCopy.
- The current receive block contains 3 messages.

![Example of filling the DB TestCopyData](images/102090095371_DV_resource.Stream@PNG-en-US.png)

Example of filling the DB TestCopyData

###### Length calculation

FC TestCopy uses the following parameters for determining the minimum length for the DB TestCopyData:

| Parameter | Parameter name | Length |
| --- | --- | --- |
| Length of communication buffer | Len<sub>ComBuffer</sub> | 76 or 202 bytes ***** |
| Minimum frame length | Len<sub>MinTgrm</sub> | 14 bytes |
| Offset management area | Offset | 40 bytes |
| Length of the time difference | Len<sub>dt</sub> | 4 bytes |
| Length of the block separators | Len<sub>Trenner</sub> | 2 bytes |
| ***** 76 with X communication, 202 with B communication |  |  |

The formula used for the actual calculation is the same for X communication and B communication. The results differ only due to different lengths for the communication buffer for X and B communication:

- **Length with X communication**

  | Symbol | Meaning |
  | --- | --- |
  | Len<sub>Min_Xcom</sub> | =Len<sub>ComBuffer</sub> + Offset + Len<sub>dt</sub> + (Len<sub>ComBuffer</sub> / Len<sub>MinTgrm</sub> + 1) * Len<sub>Trenner</sub> |
  |  | = 76 + 40 + 4 + (76 / 14 + 1) * 2 |
  |  | = 120 + 12 = 132 bytes minimum |
- **Length with B communication**

  | Symbol | Meaning |
  | --- | --- |
  | Len<sub>Min_Bcom</sub> | =Len<sub>ComBuffer</sub> + Offset + Len<sub>dt</sub> + (Len<sub>ComBuffer</sub> / Len<sub>MinTgrm</sub> + 1) * Len<sub>Trenner</sub> |
  |  | = 202 + 40 + 4 + (202 / 14 + 1) * 2 |
  |  | = 236 + 40 = 276 bytes minimum |

If FC TestCopy determines that the DB TestCopyData does not have the calculated minimum length an error message to this effect is entered in data byte DBB28.

##### Operation of TestCopyMonitor

###### Operating modes and transfer directions of DB TestCopyData

In byte 0 (OperationMode) of the DB TestCopyData, the mode of the FC is coded. The values 0 ... 3 identify the mode:

- Mode 0

  Function blocked
- Mode 1

  Frame entry as of the start of DB TestCopyData
- Mode 2

  Write to DB TestCopyData endlessly as circulating buffer
- Mode 3

  Fill DB TestCopyData once, then set mode 0.

You will find the detailed coding in the table below.

Along with the mode the coding of DBB0 also includes the transfer direction of the logged data. The following assignment applies for the coding:

- Bit 0...3

  Modes (0, 1, 2, 3) for the direction "RecvCopy" (copy receive frames)
- Bit 4...7

  Modes (0, 1, 2, 3) for the direction "SendCopy" (copy send frames)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit | .7 | .6 | .5 | .4 | .3 | .2 | .1 | .0 |
| Direction | SendCopy |  |  |  | RecvCopy |  |  |  |

The functions "SendCopy" and "RecvCopy" can be activated individually or at the same time, however only a common mode is possible for both communication directions.

When a mode &gt; 0 is set in the less significant half byte, this always applies to both communication directions.

Only if mode 0 is coded in bit 0...3 (RecvCopy), does the value in bit 4...7 apply (SendCopy).

Exception:  
To delete the DB TestCopyData, DBB0 must be written with FF, 0F is not enough.

Examples of coding of DBB0:

- 00<sub>h</sub>

  No TestCopy function enabled
- 03<sub>h</sub>

  Only RecvCopy function (OperationMode = 3), no SendCopy function.
- 30<sub>h</sub>

  Only SendCopy function (OperationMode = 3), no RecvCopy function.
- 33<sub>h</sub>

  RecvCopy function and SendCopy function (OperationMode = 3)
- FF<sub>h</sub>

  Delete content of DB TestCopyData

###### Filter settings via TestCopyMonitor

Run FC TestCopy via a watch table which is available in finished form as "TestCopyMonitor" in the TD7 library.

The following settings are possible using the watch table in the DB TestCopy:

| Name (symbol) | Permitted values (hex.) | Meaning |
| --- | --- | --- |
| OperationMode | 00 | Mode 0: Function blocked |
| 11 | Mode 1: Frame entry always as of the start of DB TestCopyData |  |
| 22 | Mode 2: Write to DB TestCopyData endlessly as circulating buffer |  |
| 02  20 | - Write for SendCopy function - Write for RecvCopy function |  |
| 33 | Mode 3: Fill DB TestCopyData once, then set mode 0. |  |
| 03  30 | - Fill for SendCopy function - Fill for RecvCopy function |  |
| FF | Delete the entire DB TestCopyData and reset to default |  |

As the output value, FC TestCopy returns a count value in DBW12 (Recv_TgramCounter) of the DB TestCopyData for the frames received since setting mode 1, 2 or 3 that match the filter criteria.

The number of send frames is entered in DBW26 (Sendcv_TgramCounter).

In DBB28, you receive a return value that indicates the errors that occurred during processing of the FC:

- FC_RetVal = 0

  No error
- FC_RetVal = 1

  The specified DB TestCopyData is too short.
- FC_RetVal = 10d

  The mode entered in DBB0 is not defined.

In addition, the following special filters are available for the RecvCopy or SendCopy function:

| Name (symbol) * | Permitted values (hex.) | Meaning |
| --- | --- | --- |
| Xxxx_TgrmType | FF | Copy all frame types (TA) to DB TestCopyData |
| 00 | Copy only spontaneous Org. frames (TA = 0) |  |
| 11 | Copy only queried Org. frames (TA = 1). |  |
| 22 | Copy only spontaneous data frames (TA = 2). |  |
| 33 | Copy only queried data frames (TA = 3). |  |
| 01 | Copy Org. frames with TA = 0 or 1 |  |
| 23 | Copy data frames with TA = 2 or 3 |  |
| Any combination | Copy any 0, 1, 2, 3 combinations. |  |
| Xxxx_DestSubscr | All permitted subscribers | Filter for the dest. subscriber no. in the frame |
| -1 | Copy all frames regardless of the dest. subscriber no. |  |
| Xxxx_DestObject | All permitted objects | Filter for the dest. object no. in the data frame. |
| -1 | Copy all frames regardless of the dest. object no. |  |
| Xxxx_SourceSubscr | All permitted subscribers | Filter for the source subscriber no. in the frame |
| -1 | Copy all frames regardless of the source subscriber no. |  |
| Xxxx_SourceObject | All permitted objects | Filter for the source object no. in the data frame |
| -1 | Copy all data frames regardless of the source object no. |  |
| Xxxx_StartIndex | All permitted indexes | Filter for the start index no. in the data frame |
| -1 | Copy all data frames regardless of the start index no. |  |
| ***** "Xxxx": Placeholder for "Recv" or "Send" |  |  |

The desired filter tags can be easily added using the tag names of the TestCopy DB.

**Notes on operator input**

When changing from one mode to the next, the content of DB TestCopyData is not deleted. Only internal pointers and frame counters in the management area of the DB TestCopyData are reset. When there is a mode change it is therefore recommended to use the delete function "FF" to preset the frame buffer area with 0. The makes the copied frame blocks easier to read.

If send and receive frames are to be copied, in the left half byte of the "OperationMode" parameter, the same mode must be entered as in the right half byte.

The following scheme applies to mode 0, 1, 2 and 3:

- If the buffer is deleted, FF<sub>h</sub> must always be entered.
- Separate deletion of the receive and send frames is not possible.

##### FC TimeTask

###### Function

The FC TimeTask keeps a continuous date and time on a CPU The FC has no parameters.

Link the FC into the cyclic user program (in OB1) following the FC BasicTask.

FC TimeTask can only be used when the CPU is synchronized by a local TIM. Activate the time-of-day synchronization for the relevant TIM modules.

After the CPU has started up, the TIM supplies the date and current time the first time with an Org. frame. After this, time-of-day synchronization is performed at the interval specified in the configuration of the TIM. For time-of-day synchronization on MPI/partyline an interval of one minute is recommended. FC TimeTask sets the clock of the CPU with the time provided by the TIM.

The FC reads out the time in every OB1 cycle. The read time is entered in the first two double words of the DB BasicData and marked as valid or invalid and with an indication whether it is daylight saving or standard time.

From DB BasicData all blocks take the current time if they need it. For example the data point typicals do this to time stamp their data or FC Trigger to check whether a time set for the FC has been reached or a preset interval has elapsed. This time of day is also available to the user program.

Assignment of the data words with date, time and time status

|  |  |  |  |
| --- | --- | --- | --- |
| CurrentDate | Data byte 0 | Year * 10 | Year * 1 |
| Data byte 1 | Month * 10 | Month * 1 |  |
| Data byte 2 | Day * 10 | Day * 1 |  |
| Data byte 3 | Hour * 10 | Hour * 1 |  |
| CurrentTime | Data byte 4 | Minute * 10 | Minute * 1 |
| Data byte 5 | Second * 10 | Second * 1 |  |
| Data byte 6 | Milliseconds * 100 | Milliseconds * 10 |  |
| Data byte 7 | Milliseconds * 1 | Time status |  |

Assignment of the half byte "time status"

| Symbol | Meaning |
| --- | --- |
| 0 | 0 = date/time invalid 1 = date/time valid |
| 1 | 0 = standard time 1 = daylight saving time |
| 2 | (not used) |
| 3 | (not used) |

Apart from the time status, whether or not the date/time is valid can also be determined based on data bit 16.1 "CpuClockOk". As soon as the time on the CPU is valid, this bit is set to 1 by FC TimeTask. In the user program this bit can be queried directly under the symbolic name "BasicData.CpuClockOk".

##### FC Trigger

###### Function

The FC sets an output (memory bit, data bit or digital output) at a time that can be configured by the user or at a preset time interval.

The FC resets this output after one OB1 cycle.

The FC can be called at any point in the cyclic user program (OB1) also more than once.

If the running of a program section or a software function is to be triggered using FC Trigger we recommend that FC Trigger is called directly before execution of this function. Applications for triggering functions due to the memory bit set by FC Trigger are, for example, as follows:

- Running through a function
- Calling a block
- Triggering transfer of a counted value every 2 hours

If several functions need to be activated at the same time this can be implemented by one FC Trigger block if all functions query the same memory bit set by the FC. This works, however, only when the triggered functions do not reset this memory bit themselves.

Remedy if triggered blocks reset the memory bit:

- You call FC Trigger often, always with the same time but a different output memory bit.
- After calling FC Trigger you reproduce the set output memory bit in an appropriate number of further memory bits.

The FC accesses the SINAUT time of day in the first two data double words of the DB BasicData. These are constantly supplied if an FC TimeTask is included in the user program and this is synchronized at regular intervals by a local TIM. FC Trigger compares the time set for it with the current time only when the time in DB BasicData, data byte 7 (time status byte, bit 0 = 1) is marked as being valid.

The accuracy with which FC Trigger operates depends on the accuracy of the time and on the OB1 cycle time.

If the OB1 cycle time is lower than 1 second (this is normal) the output is set exactly at the programmed second value with the inaccuracy of the OB1 cycle time of less than 1 s.

If the OB1 cycle time is higher than 1 seconds, the FC works with a tolerance of 4 seconds. If the FC is processed too late but still within 4 seconds of the configured time, the output is still set.

The edge memory bit "Flag" configured for the FC is set at the same time as the output and reset 5 seconds after the configured time.

No placeholder parameter may be used for the edge memory bit and it must not be reset by the user program.

You can find examples of the parameter assignment for FC Trigger further below.

###### Parameters

| Symbol | Meaning |
| --- | --- |
| Name: | **IntervalMode** |
| Declaration: | INPUT |
| Data type: | BOOL |
| Range of values: | TRUE / FALSE |
| Explanation | Point in time / time interval  - FALSE = point in time - TRUE = time interval   You will find examples of the parameter assignment for a time or time interval after this explanation of the parameters. |

| Symbol | Meaning |
| --- | --- |
| Name: | **Hour_Minute** |
| Declaration: | INPUT |
| Data type: | WORD |
| Explanation | Specifies the values for hours and minutes.  Further explanation: Refer to the parameter "Month_Year". |

| Symbol | Meaning |
| --- | --- |
| Name: | **Second_Day** |
| Declaration: | INPUT |
| Data type: | WORD |
| Explanation | Specifies the values for seconds and day.  Further explanation: Refer to the parameter "Month_Year". |

| Symbol | Meaning |
| --- | --- |
| Name: | **Month_Year** |
| Declaration: | INPUT |
| Data type: | WORD |
| Range of values: | - 00 ... 99 - FF |
| Explanation | Specifies the values for month and year  Each parameter is in two parts. Each of the two values per parameter is specified with two digits as a BCD-coded value.  - The first two digits specify the value for hours, seconds or month. - The two other digits specify the value for minutes, day or year.   For parts of the parameter that are not needed FF is entered.  Which parameters are permitted depends on the particular parameter and on the "IntervalMode" parameter. You will find further information following the explanation of the parameters. |

|  |  |  |
| --- | --- | --- |
| Name: | **TriggerOutput** |  |
| Declaration: | OUTPUT |  |
| Data type: | BOOL |  |
| Range of values: | Output | Q 0.0 ... I n.7 |
| Memory bit | M 0.0 ... M n.7 L 0.0 ... L n.7 |  |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| Explanation | Trigger output  The output is set for the duration of one OB1 cycle when the time or time interval set for "Hour" to "Year" is reached. |  |

|  |  |  |
| --- | --- | --- |
| Name: | **Flag** |  |
| Declaration: | IN_OUT |  |
| Data type: | BOOL |  |
| Range of values: | Memory bit | M 0.0 ... M n.7 |
| Data bit | DBm.DBX 0.0 ... n.7 |  |
| This is an in/out parameter (declaration IN_OUT). It is difficult to specify local bit memory with this parameter and this should not be used. |  |  |
| Explanation | Edge memory bit for the "TriggerOutput" output.  No placeholder memory bit may be specified!  The edge memory bit must not be reset by the user program. |  |

###### Examples of the parameter assignment of a time or time interval

**IntervalMode = FALSE (or 0)**

The FC operates according the time principle. When the time set is reached, the output "TriggerOutput" is set for one OB1 cycle.

All time parameters can be used to specify the point in time. Parameters not required should be assigned FF. They are ignored during the check for reaching the time.

Even when "IntervalMode" = 0, time intervals can be set in certain ranges, see the following examples.

Permitted values for the time parameters:

|  |  |  |  |
| --- | --- | --- | --- |
| Hours | 00-23 | Day | 01-31 |
| Minutes | 00-59 | Month | 01-12 |
| Seconds | 00-59 | Year | 00-99 |

Examples:

- IntervalMode = FALSE

  The output "TriggerOutput" is set once on 04.02.91 at 06:45:12:

  - Hour_Minute : W#16#0645
  - Second_Day : W#16#1204
  - Month_Year : W#16#0291
- IntervalMode = FALSE

  The output "TriggerOutput" is set every day at 06:00:00:

  - Hour_Minute : W#16#0600
  - Second_Day : W#16#00FF
  - Month_Year : W#16#FFFF
- IntervalMode = FALSE

  The output "TriggerOutput "is set on the 1st of every month at 06:00:00:

  - Hour_Minute : W#16#0600
  - Second_Day : W#16#0001
  - Month_Year : W#16#FFFF
- IntervalMode = FALSE

  The output "TriggerOutput" is set every year on October 1, at 06:00:00:

  - Hour_Minute : W#16#0600
  - Second_Day : W#16#0001
  - Month_Year : W#16#10FF

**IntervalMode = TRUE (or 1)**

The FC operates according the time interval principle. When the time value set or a multiple of it is reached, the output "TriggerOutput" is set for one OB1 cycle.

Only the specifications for hours, minutes and seconds are relevant. The date parameters are ignored. A time interval can also only be set in hours or in minutes or in seconds. Time parameters not required should be assigned FF.

The following time intervals are permitted:

- Hours: 01, 02, 03, 04, 06, 08, 12, 24
- Minutes: 01, 02, 03, 04, 05, 06, 10, 12, 15, 20, 30, 60
- Seconds: 10, 12, 15, 20, 30, 60

Examples:

- IntervalMode : TRUE

  The output "TriggerOutput" is set as follows:

  - Hour_Minute : W#16#06FF (every 6 hours)
  - Second_Day : W#16#FFFF (at 00:00:00, 06:00:00, 12:00:00 o'clock and ...)
  - Month_Year : W#16#FFFF (... at 18:00:00 o'clock)
- IntervalMode : TRUE

  The output "TriggerOutput" is set as follows:

  - Hour_Minute : W#16#FF30
  - Second_Day : W#16#FFFF (at 00:00:00, 00:30:00, 01:00:00 o'clock and ...)
  - Month_Year : W#16#FFFF (... at 01:30:00, 02:00:00, 02:30:00 o'clock etc.)

###### Error message during startup

The FC checks the parameters Hour_Minute, Second_Day and Month_Year in every cycle to ensure that they keep to the permitted range of values. What is permitted is also dependent on the "IntervalMode" parameter.

If the parameter assignment is incorrect, an error message is entered in the diagnostics buffer (event ID B113) only during startup. The CPU does not change to STOP. Afterwards, the FC checks the parameters without outputting error messages until the error has been eliminated.

The diagnostics message provides a precise identification of the incorrect parameter (continuous number of the parameter, i.e. 2, 3 or 4). The causes of the diagnostics message can be depend on the parameter "IntervalMode".

**IntervalMode = FALSE (or 0)**

The permitted ranges of values for the parameters Hours, Minutes, Seconds, Day, Month and Year were not kept to. Apart from FF, the following can be configured:

|  |  |  |  |
| --- | --- | --- | --- |
| Hours | 00-23 | Day | 01-31 |
| Minutes | 00-59 | Month | 01-12 |
| Seconds | 00-59 | Year | 00-99 |

**"IntervalMode" = TRUE (or 1)**

In this case the error can have two different causes:

- The permitted ranges of values for the parameters Hours, Minutes and Seconds were not kept to. Apart from FF, the following can be configured:

  - Hours: 01, 02, 03, 04, 06, 08, 12, 24
  - Minutes: 01, 02, 03, 04, 05, 06, 10, 12, 15, 20, 30, 60
  - Seconds: 10, 12, 15, 20, 30, 60
- A time interval can only be set in hours or in minutes or in seconds. The two unused parameters must have FF written to them. Even if FF was entered for all three named parameters, an error exists.

#### System blocks

This section contains information on the following topics:

- [BasicTask_* FC](#basictask_-fc)
- [DB BasicData](#db-basicdata)
- [FC Create](#fc-create)
- [Diagnose / Diagnostics FC](#diagnose-diagnostics-fc)
- [FC Distribute](#fc-distribute)
- [FC Search](#fc-search)
- [FC Startup](#fc-startup)
- [System blocks - BCom](#system-blocks---bcom)
- [System blocks - PCom](#system-blocks---pcom)
- [System blocks - XCom](#system-blocks---xcom)

##### BasicTask_* FC

###### Block versions

> **Note**
>
> **Only 1 FC type per CPU**
>
> You may only use one FC type in one CPU. A mixture of several communication types with different "BasicTask_*" FCs is not permitted.

The block is available in the following versions for the different CPU types:

- **BasicTask_B**

  For S7‑1500 CPU

  The block for the S7‑1500 CPU cannot be used for the S7‑300 or S7‑400 CPU.
- **BasicTask_B**

  For S7‑400 CPU

  The block for the S7‑400 CPU cannot be used for the S7‑300 or S7‑1500 CPU.
- **BasicTask_Bnn**

  For S7‑300 CPU

  The blocks for the S7‑300 CPU cannot be used for the S7‑400 or S7‑1500 CPU.

  As of version V3.0 + SP2 of the block library, 16 versions of the "BasicTask_B" FC are provided for an S7‑300 CPU. These are provided for the configured number of local TIM 1531 IRC via which the CPU communicates. According to the number (nn) of local TIM modules, the FC receives the suffix "nn", for example, "BasicTask_B03".

  When generating the TD7onCPU in the CPU, a suitable "BasicTask_B" FC is generated. The block version from which the number of local TIM 1531 IRC is determined can be taken from the "Comment" block property of the "BasicTask_B" FC in the "TD7onCPU" directory of the CPU.
- **BasicTask_X**

  For S7‑300 PU with partyline
- **BasicTask_P**

  For S7‑300 CPU without partyline

For information on "Partyline", see Glossary.

The tasks of the various "BasicTask_*" FCs for handling basic communication tasks are the same in the respective CPU type. The only parameter of the FC is identical in each case.

When the TD7onCPU is generated, the correct FC is automatically created in the respective CPU.

###### Function

The block is required in every CPU. It handles the following tasks:

- Central tasks during startup
- The processing of all communication mailboxes
- Central organizational tasks such as starting, monitoring and answering general requests.

Call FC BasicTask as the first block in OB1.

###### Parameter

| Symbol | Meaning |
| --- | --- |
| Name: | **UserFC** |
| Declaration: | INPUT |
| Data type: | INT |
| Range of values: | - 1 ... 32000   Number of the FC   The maximum possible number depends on the CPU. - 0   Substitute value if there is no FC present for the specified purpose. |
| Explanation: | Number of a user FC for specific further processing of the received data.  If an FC is specified, this FC is called automatically by the user program with all received data. At the time of the call, the receive frame is still in the receive mailbox of the communication DB.  The program in the user FC can read the receive frame from the receive mailbox and process it further in any way required, e.g. write the received data to an intermediate buffer.  Using the user program, the required information on the communication DB can be read from the DB BasicData via the "CurrentComDB" tag in DW60. CurrentComDB contains the following information:  - S7‑1500   Index of the current BConnection instance in the DB BConnectData - S7‑300/400   Number of the current communication DB   In the opened communication DB, the start of the current receive frame in the receive mailbox can be found via the "CurrentReceivedMessage" tag in DW10. |

##### DB BasicData

This data block provides the central data management. It contains information that must be maintained centrally for all blocks. Among other things, the data block contains the subscriber records and the connection descriptions.

DB BasicData is automatically generated in the required length preset with the subscriber and connection specific data and then saved in the block directory of the CPU.

DB BasicData exists once on every CPU.

> **Note**
>
> **Number of DB BasicData**
>
> In the TD7 library, DB BasicData has the number DB127 and is also saved there under this number when the DB is generated for the various CPUs In principle it would be possible to change the number, but this involves a lot of work and can cause errors in the further creation of the user program.
>
> It is therefore recommended to keep the DB number 127 free for the DB BasicData.

##### FC Create

Auxiliary block for putting together the data to be sent and its entry in the relevant instances of the send mailbox(es) (SendBuffer array) in the respective communication DB. These are the following DBs:

- **S7‑1500**

  DB BConnectData &gt; BConnection[n]
- **S7‑400**

  DB BComDataXX
- **S7‑300**

  - DB BComDataXX

    or
  - DB XComDataXX

    or
  - DB PComDataXX

XX is a placeholder for the sequential number (01, 02, etc.).

FC Create is required by the data point typicals for data and organizational frames and by FC BasicTask for organizational frames only.

##### Diagnose / Diagnostics FC

Name of the block:

- For S7-300: FC Diagnose
- For S7-1500: FC Diagnosis

Auxiliary block for entering SINAUT system messages in the diagnostics buffer of the CPU.

##### FC Distribute

Auxiliary block for distribution of the data located in the receive mailbox to the data point typicals responsible or to the node objects in the subscriber records.

##### FC Search

Auxiliary block for the following search tasks:

- Search for the initial address of a subscriber object within the subscriber records
- Search for the local object no. (Instance DB) from one of the two object reference lists for a received message with an incomplete destination address

The auxiliary block is required by almost all blocks.

##### FC Startup

The block is required in every CPU. It must be linked into the startup program OB100.

The block has the task of setting the startup memory bit in the DB BasicData and to reset the corresponding edge memory bit if this is still set.

The block has no parameters.

##### System blocks - BCom

This section contains information on the following topics:

- [FB BCom](#fb-bcom)
- [DB BComData](#db-bcomdata)
- [BConnect FB](#bconnect-fb)
- [DB BConnectData](#db-bconnectdata)

###### FB BCom

###### Validity

- S7-1500
- S7-300 / S7-400

The blocks for the S7-300/400 CPUs cannot be used for the S7-1500 CPU and vice versa. The tasks of the FBs are the same.

###### Function

- S7-1500

  Auxiliary block for FC BasicTask_B for processing a communication mailbox of the type DB BConnectData (S7‑1500).

  Via the DB, a configured PBK (programmed block communication) connection is handled using the SFBs "BSEND" and "BRCV".

  FB BCom also ensures that received frames are distributed immediately to the receive objects responsible in the CPU. To do this, FB BCom calls FC Distribute as an auxiliary block.
- S7-300 / S7-400

  Auxiliary block for FC BasicTask_B for processing a communication mailbox of the type DB BComData (S7‑300/S7‑400).

  A configured PBK connection (programmed block communication) is handled via the DB using the "BSEND" and "BRCV" SFBs of an S7-400 CPU or the function blocks (FBs) of the same name of an S7-300 CPU.

  FB BCom also ensures that received frames are distributed immediately to the receive objects responsible in the CPU. To do this, FB BCom calls FC Distribute as an auxiliary block.

###### S7-300

**Availability and function**

The BCom FB can only be used as of block version V1.5 for an S7-300 CPU. The block is included in the "Telecontrol ST7" library as of version V3.0 SP2.

The block is required for an S7-300 CPU especially for communication via a local TIM1531-IRC.

**Number of configurable S7 connections**

S7-300 CPU supports up to 16 S7 connections for TD7onCPU. The configurable number of S7 connections depends on the respective CPU type and cannot be exceeded even by CPUs with more connection resources.

###### DB BComData

###### Validity

S7-300

S7-400

###### Function

Instance data block for the communication block FB BCom. The instance DB represents the communication mailbox and contains the following, among other things:

- The receive mailbox (ReceiveBuffer)
- A send mailbox (SendBuffer)

It also contains central data required to control and manage the PBK connection that runs via this mailbox.

The data block is required in every CPU in which FB BCom is used. If the CPU has several PBK connections the DB is required more than once.

DB BComData is automatically generated in the required length preset with the connection specific data and then saved in the block directory of the CPU.

###### BConnect FB

###### Validity

S7-1500

###### Function

Auxiliary block for FC BasicTask for processing connections to the communication partners.

###### DB BConnectData

###### Validity

S7-1500

###### Function

Instance data block for the communication block FB BCom. The instance DB represents the communication mailbox and contains the following, among other things:

- The receive mailbox (ReceiveBuffer)
- A send mailbox (SendBuffer)

It also contains central data required to control and manage the PBK connection that runs via this mailbox.

The data block is required in every CPU in which FB BCom is used. If the CPU has several PBK connections the DB is required more than once.

DB BComData is automatically generated in the required length preset with the connection specific data and then saved in the block directory of the CPU.

##### System blocks - PCom

This section contains information on the following topics:

- [FB PCom](#fb-pcom)
- [DB PComData](#db-pcomdata)

###### FB PCom

###### Validity

S7‑300 CPU without partyline

FB PCom is used only with communication via the P bus. This affects the communication between a TIM and a CPU with P bus.

###### Function

Auxiliary block for FC BasicTask_P for processing a communication mailbox of the type DB PComData using the SFCs WR_REC and RD_REC.

Received frames are also distributed immediately to the receive objects responsible in the CPU. To do this FB PCom calls FC Distribute as an auxiliary block.

###### DB PComData

Instance data block for the communication block FB PCom. The instance DB makes the communication mailbox available and contains the following:

- The receive mailbox (ReceiveBuffer)
- A send mailbox (SendBuffer)

It also contains central data required to control and manage the connection that runs via this mailbox.

The data block is required in every CPU in which FB PCom is used. If the CPU has several corresponding connections the DB is required more than once.

##### System blocks - XCom

This section contains information on the following topics:

- [FB XCom](#fb-xcom)
- [DB XComData](#db-xcomdata)

###### FB XCom

###### Validity

S7‑300 CPU with partyline

###### Function

Auxiliary block for FC BasicTask_X for processing a communication mailbox of the type DB XComData.

Via DB BComData a configured connection (PBK connection) is handled using the SFCs "X_SEND" and "X_RCV".

The FB XCom also ensures that received frames are distributed immediately to the receiving objects responsible in the CPU. To do this the FB XCom calls the FC Distribute as an auxiliary block.

###### DB XComData

Instance data block for the communication block FB XCom. The instance DB makes the communication mailbox available and contains the following:

- The receive mailbox (ReceiveBuffer)
- A send mailbox (SendBuffer)

It also contains central data required to control and manage the X connection that runs via this mailbox.

The data block is required in every CPU in which FB XCom is used. If the CPU has several X connections the DB is required more than once.

DB XComData is automatically generated in the required length preset with the connection specific data and then saved in the block directory of the CPU.
