---
title: "Special PROFINET configurations"
package: HWCPNIRT34enUS
topics: 106
devices: [PC, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Special PROFINET configurations

This section contains information on the following topics:

- [Special features for S7-300/400/1500 and PC stations (S7-300, S7-400, S7-1500, PC)](#special-features-for-s7-3004001500-and-pc-stations-s7-300-s7-400-s7-1500-pc)
- [Configuring IRT communication (S7-1500, S7-1500T)](#configuring-irt-communication-s7-1500-s7-1500t)
- [Configuring I-devices](#configuring-i-devices)
- [Changing IO devices during operation](#changing-io-devices-during-operation)
- [Optimizing startup time](#optimizing-startup-time)
- [Configuring media redundancy](#configuring-media-redundancy)
- [Configuring PROFIenergy (S7-300, S7-400, S7-1500)](#configuring-profienergy-s7-300-s7-400-s7-1500)
- [Configuring Shared Devices (S7-300, S7-400, S7-1500)](#configuring-shared-devices-s7-300-s7-400-s7-1500)
- [Creating a standard machine project](#creating-a-standard-machine-project)
- [Performance upgrade](#performance-upgrade)
- [Maintenance with asset management data records](#maintenance-with-asset-management-data-records)
- [Configuring direct data exchange between S7-1500 CPUs](#configuring-direct-data-exchange-between-s7-1500-cpus)
- [Configuring PROFINET Security Class 1 functions](#configuring-profinet-security-class-1-functions)

## Special features for S7-300/400/1500 and PC stations (S7-300, S7-400, S7-1500, PC)

This section contains information on the following topics:

- [Address and name assignments for PROFINET devices (S7-300, S7-400, S7-1500, PC)](#address-and-name-assignments-for-profinet-devices-s7-300-s7-400-s7-1500-pc)
- [What you should know about the send clock (S7-300, S7-400, S7-1500, PC)](#what-you-should-know-about-the-send-clock-s7-300-s7-400-s7-1500-pc)
- [Setting the send clock (S7-300, S7-400, S7-1500, PC)](#setting-the-send-clock-s7-300-s7-400-s7-1500-pc)
- [Adjusting odd send clocks (S7-300, S7-400, S7-1500, PC)](#adjusting-odd-send-clocks-s7-300-s7-400-s7-1500-pc)
- [Configuration with external IO controller (S7-300, S7-400, S7-1500, PC)](#configuration-with-external-io-controller-s7-300-s7-400-s7-1500-pc)
- [Configuration with SIMATIC PC Station (S7-300, S7-400, S7-1500, PC)](#configuration-with-simatic-pc-station-s7-300-s7-400-s7-1500-pc)
- [IO routing with CP 1604 / 1616 / 1626 and CP 1616 onboard (S7-300, S7-400, S7-1500, PC)](#io-routing-with-cp-1604-1616-1626-and-cp-1616-onboard-s7-300-s7-400-s7-1500-pc)
- [PROFINET device diagnostics (S7-300, S7-400, S7-1500, PC)](#profinet-device-diagnostics-s7-300-s7-400-s7-1500-pc)

### Address and name assignments for PROFINET devices (S7-300, S7-400, S7-1500, PC)

In this chapter you will learn which address and naming conventions are valid for the PROFINET devices.

#### IP addresses

All PROFINET devices work with the TCP/IP protocol and therefore require an IP address for Ethernet operation.

You can set the IP addresses in the module properties. If the network is part of an existing company Ethernet network, ask your network administrator for this data.

The IP addresses of the IO devices are assigned automatically, usually at CPU startup. The IP addresses of the IO devices always have the same subnet mask as the IO controller and are assigned in ascending order, starting at the IP address of the IO controller.

#### Device names

Before an IO device can be addressed by an IO controller, it must have a device name. This procedure was chosen for PROFINET because names are easier to administer than complex IP addresses.

The device name is automatically derived from the name configured for the device (CPU, CP or IM):

- The PROFINET device name is made up of the name of the device (for example, the CPU), the name of the interface (only with multiple PROFINET interfaces) and optionally the name of the IO system:

  &lt;CPU name&gt;.&lt;Name of the interface&gt;.&lt;IO system name&gt;

  You cannot change this name directly. You change the PROFINET device name indirectly, by changing the name of the affected CPU, CP or IM in the general properties of the module. This PROFINET device name is also displayed, for example, in the list of accessible devices. If you want to set the PROFINET device name independently of the module name, you have to deactivate the "Generate PROFINET device name automatically" option.
- A "converted name" is generated from the PROFINET device name. This is the device name that is actually loaded into the device.

  The PROFINET device name is only converted if it does not comply to the rules of IEC 61158-6-10. You cannot change this name directly either.

#### Device number

In addition to the device name, a device number is also automatically assigned when an IO device is plugged in. You can change this number.

An IO device can be identified in the user program with this device number, for example, with the instruction "[LOG_GEO](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#log_geo-determine-the-slot-belonging-to-a-logical-address-s7-300-s7-400)". The device name, unlike the device number, is not visible in the user program.

#### Devices in the PROFINET subnet

In a PROFINET subnet the maximum allowable number of devices is monitored during configuration.

### What you should know about the send clock (S7-300, S7-400, S7-1500, PC)

#### Send clock - the smallest possible update interval

The send clock shows the time between two successive communication cycles. It is the shortest possible transmission interval for data exchange. The update times are calculated as multiples of the send clock.

#### Requirements for changing the send clock

For unsynchronized devices or when the device is an IO controller as sync master, the send clock is configured on the device. For synchronized devices (sync master, sync slave), the send clock can be configured in the sync domain.

The send clock cannot be changed on the device if it is not an IO controller as sync master and at least one device is sync slave or sync master in the IO system. In this case, only the send clock which was selected in the properties of the respective synchronization domain is displayed. To change this you must call the properties of the respective sync domain ("Domain Settings" button).

The send clock can be changed on the device if all devices on the IO system are unsynchronized or when the device is an IO controller as sync master. You can see the resulting update times for the individual IO devices in the IO communication table or in the properties of the individual IO devices.

#### Effect of the send clock on the maximum possible bandwidth for cyclical IO data

The following table shows how the send clock affects the maximum available bandwidth for cyclical IO data:

| Send clock | Maximum bandwidth for cyclic IO data |
| --- | --- |
| 250 µs – 468.75 µs | &lt;&lt; 125 µs |
| 500 µs – 968.75 µs | = send clock / 2 |
| 1 – 4 ms | = 500 µs |

The send clock influences the update time of IO devices for which the "Automatic" and "Can be set" option is selected (with "Adapt update time when send clock changes" option selected).

When the "Can be set" option is selected for IO devices, this can lead to inconsistencies in the configuration. On these IO devices you must subsequently adjust the update time, if necessary.

---

**See also**

[Setting the send clock](Configuring%20devices%20and%20networks.md#setting-the-send-clock)

### Setting the send clock (S7-300, S7-400, S7-1500, PC)

#### Requirements to change the send clock at the PROFINET device

The PROFINET device must be an IO controller as sync master or IRT (Isochronous Realtime) must not be configured in the IO system.

If the PROFINET device is not an IO controller as sync master, the following requirements must be met for the setting of the send clock:

- No device must be configured at the IO system as a sync slave or sync master.
- All devices at the IO system must be unsynchronized.

When IRT is configured with an IO controller as sync master, the send clock can be set at the device or in the sync domain.

#### Procedure

To set the send clock on the PROFINET device, follow these steps:

1. Select the PROFINET IO controller in the device or network view.
2. Change the value for the shortest possible update interval in the properties of the PROFINET interface under "PROFINET Interface &gt; Advanced options &gt; Real-time settings &gt; IO communication &gt; Send clock".

The send clock is valid for all PROFINET devices at the IO system. If the synchronization role is set to a value other than "Unsynchronized", you can also set the send clock in the sync domain, in other words, centrally at the PROFINET IO system.

1. Select the IO system using the PROFINET subnet.
2. Change the value for the send clock in the properties of the sync domain under "Domain management &gt; Sync domains &gt; Sync_domain_1 &gt; Send clock".

---

**See also**

[Configuring PROFINET IO with IRT (S7-1500, S7-1500T)](#configuring-profinet-io-with-irt-s7-1500-s7-1500t)

### Adjusting odd send clocks (S7-300, S7-400, S7-1500, PC)

S7-1500 CPUs support both even and odd send clocks.

Even send clocks: 0.25 ms, 0.5 ms, 1 ms, 2 ms, etc.

Odd send clocks: 0.375 ms, 0.75 ms, 1.125 ms, etc.

For IO devices that do not support the fast send clock of the CPU (i.e., of the IO controller) or that do not support odd send clocks, the CPU "adapts" the send clock of the IO device. Thus, for example, it is possible that the CPU (IO controller) and a connected IO device both operate with an 875 μs send clock, while another IO device operates with a 2 ms send clock.

#### Rules

- The send clock adaptation only works for unsynchronized IO devices (RT class "RT").
- For synchronized IO devices (RT class "IRT"), a uniform send clock that is set in the sync domain applies. The update time corresponds to the send clock in this case.
- For IO devices whose update time option is set to "Automatic," an update time of 2 ms or greater is set by STEP 7, i.e., update times of less than 2 ms are not possible with this option.

#### Example

A PROFINET IO master system consists of the following components:

- IO controller: CPU 1516-3 PN/DP (6ES7 516-3AN00-0AB0)
- IO device 1: ET 200MP (6ES7 155-5AA00-0AB0) with one DI module
- IO device 2: ET 200S (6ES7 151-3BA23-0AB0 V6.0) with one DI module

IO device 2 does not support the odd send clock (here: 0.875 ms).

1. Assign the IO devices to the IO controller.
2. Set the "Sync slave" synchronization role for IO device 1 (inspector window, PROFINET interface area &gt; Advanced options &gt; Realtime settings &gt; Synchronization).
3. For the IO controller, you set the synchronization role "sync master" in the same way.
4. Interconnect the ports of the IO controller and IO device 1 (e.g., in the topology view).
5. IO device 2 remains unsynchronized; the update option is set to "Automatic".
6. Specify the 0.875 ms send clock in the sync domain (subnet properties). All devices in the sync domain then have this send clock or update time.

The unsynchronized IO device 2 automatically receives the update time of 2 ms.

### Configuration with external IO controller (S7-300, S7-400, S7-1500, PC)

#### Configuration with external IO controller

CPs which can be used as an external IO controller have a number of communications options and are therefore not designed for use as an IO controller.

If you use an external IO controller (such as CP 443-1 Advanced), you must integrate an IO system after inserting the IO controller.

![Configuration with external IO controller](images/25656690187_DV_resource.Stream@PNG-de-DE.png)

You can then drag the desired IO devices from the hardware catalog to the PROFINET IO system.

![Configuration with external IO controller](images/25656813579_DV_resource.Stream@PNG-de-DE.png)

### Configuration with SIMATIC PC Station (S7-300, S7-400, S7-1500, PC)

#### Configuration with SIMATIC PC Station

A "PC Station" is a PC with communications modules and software components within a SIMATIC automation solution.

By using corresponding communications modules and software components you can operate a PC station as a PROFINET IO controller.

Your PC applications on the PC Station have the following access options to the PROFINET IO controller:

- As OPC client via the OPC server PROFINET IO
- Directly via the PROFINET IO user interface (IO base programming interface)

PC applications can only ever use one of these access possibilities at a time (open/close sequence)

| Functions | OPC Server | RTE-base programming interface |
| --- | --- | --- |
| Reading and writing IO data | Yes | Yes |
| Reading and writing data records | Yes | Yes |
| Receiving and acknowledging interrupts | No | Yes |

The following figure shows a PC Station with the components described.

![Configuration with SIMATIC PC Station](images/44739480715_DV_resource.Stream@PNG-en-US.png)

#### Configuration in the network view

The following figure shows a PC Station with an OPC server and a PC application. The CP 1612 Ethernet interface added converts the PC station into an IO controller with connected IO devices. IE/PB link has also been used as a gateway from PROFINET to PROFIBUS.

![Configuration in the network view](images/25656873483_DV_resource.Stream@PNG-de-DE.png)

### IO routing with CP 1604 / 1616 / 1626 and CP 1616 onboard (S7-300, S7-400, S7-1500, PC)

#### CP as PROFINET IO router - what this means in practice

You can operate a PC station with the CP 1604 / 1616/ 1626 as PROFINET IO router by employing the relevant CP as PROFINET IO device and PROFINET IO controller simultaneously. This IO routing allows process data to be exchanged between two PROFINET IO systems. If the configuration is set up correctly the CP can, for example, allow certain process level inputs or outputs to be accessed at control level.

In a typical configuration the CP then simultaneously satisfies the following functions:

- PROFINET IO Device for a higher-level PROFINET IO controller of the control level
- PROFINET IO controller with connected IO devices for the subordinate process level

#### Assign configuration - transfer area "TM" (IO routing area)

In the configuration, select the "IO device" option under "Operating mode" .

The additional "I-device communication" configuration area appears, in which you can make the settings for the IO routing. In the "Transfer area" table there, assign the data areas for data exchange with the higher-level IO controller.

In this case, you have the following options in the "Type" column:

- CD: Controller Device

  Select this option to specify a transfer area between the IO controller and IO device. Refer to additional information on this in the online help under "Configuration for PROFINET IO".
- TM: IO routing (transfer module mapping)

  Select this option for the IO router application. An additional configuration area with the name specified appears in the Inspector window under "Operating mode / I-device communication". In this configuration area, make the assignment for the IO routing in the IO routing table.
- F-PS: PROFIsafe

  Select this option for the configuration of a PROFIsafe transfer area. The PROFIsafe transfer area is bidirectional and occupies two rows in the table of transfer areas. The length of the PROFIsafe transfer areas is limited to 8 bytes of user data each for input and output.

#### IO routing table

In the higher-level IO system, IO routing areas represent the data routed between the lower-level IO system and the higher-level IO system.

Enter the IO devices from the lower-level IO system in the IO routing table according to the transfer areas.

The table contains the following columns:

| Parameter | Meaning |
| --- | --- |
| TM offset | Offset in relation to the first bit in the IO routing area.  The specification has the form &lt;Byte&gt;.&lt;Bit&gt;.  Example: 0.5 |
| Device/module (slot) | Specification of the PROFINET device name of the IO device and its module and slot.  The displayed dialog shows the transfer areas of the IO devices configured in the lower-level IO system. |
| IO type | Select the IO type from the drop-down list.  This selection is only possible with an IO routing area of the type "Input", and only if a mixed module is selected as "Device/module (slot)".   In this case, you can select whether the inputs are read (Input) or the outputs are read back (Output). |
| Start | Start address (offset) in the data area of the transfer area in the lower-level IO system.  The specification has the form &lt;Byte&gt;.&lt;Bit&gt;.  Example: 0.0 |
| End | End address (offset) in the data area of the transfer area in the lower-level IO system.  The specification has the form &lt;Byte&gt;.&lt;Bit&gt;.  Example: 8.0 |
|  |  |

### PROFINET device diagnostics (S7-300, S7-400, S7-1500, PC)

#### PROFINET device diagnostics

The diagnostic methods available for PROFIBUS DP are the same as those for PROFINET IO. The procedure is identical. The evaluation of diagnostic information is somewhat different with the extended instructions for the distributed I/O in the S7-300/400 CPU user program.

In PROFINET IO the structure for data records and diagnostic information is manufacturer-independent. Diagnostic information is provided only for defective channels.

By using the system status lists (SSLs) and the extended instructions "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" and "[RDREC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdrec-read-data-record-s7-300-s7-400)" you can make the PROFINET IO system status and the S7 user program diagnostic information available:

- In order to get a complete overview of the PROFINET IO system status, read SSL 0x0X91 with "[RDSYSST](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdsysst-read-system-status-list-s7-300-s7-400)".
- To read diagnostic data records directly from a defective module, use the extended instruction "RDREC" (Read data record). You will receive status-related, detailed error information.
- To read event-related diagnostic data records (triggered by error OB), use the extended instruction "RALRM" (read additional alarm info) in the corresponding error OB.

The extended instruction "RALRM" and "RDREC" can also be used for PROFIBUS DP.

You can find information as to which SSLs and which diagnostic data records are defined for PROFINET IO and how the diagnostic data records are structured [here](http://support.automation.siemens.com/WW/view/en/19289930).

## Configuring IRT communication (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Introduction: Isochronous Realtime Ethernet (S7-1500, S7-1500T)](#introduction-isochronous-realtime-ethernet-s7-1500-s7-1500t)
- [Basic procedures for configuring IRT (S7-1500, S7-1500T)](#basic-procedures-for-configuring-irt-s7-1500-s7-1500t)
- [Configuring PROFINET IO with IRT (S7-1500, S7-1500T)](#configuring-profinet-io-with-irt-s7-1500-s7-1500t)
- [Sync domain (S7-1500, S7-1500T)](#sync-domain-s7-1500-s7-1500t)
- [Working with sync domains (S7-1500, S7-1500T)](#working-with-sync-domains-s7-1500-s7-1500t)
- [Editing properties of sync domains (S7-1500, S7-1500T)](#editing-properties-of-sync-domains-s7-1500-s7-1500t)
- [Bandwidth use for synchronized IO controllers (S7-1500, S7-1500T)](#bandwidth-use-for-synchronized-io-controllers-s7-1500-s7-1500t)
- [Defining devices of a sync domain (S7-1500, S7-1500T)](#defining-devices-of-a-sync-domain-s7-1500-s7-1500t)
- [Configuring a redundant sync master (S7-1500, S7-1500T)](#configuring-a-redundant-sync-master-s7-1500-s7-1500t)
- [Rules and information for IRT configurations (S7-1500, S7-1500T)](#rules-and-information-for-irt-configurations-s7-1500-s7-1500t)
- [Configuring isochronous mode (S7-1500, S7-1500T)](#configuring-isochronous-mode-s7-1500-s7-1500t)

### Introduction: Isochronous Realtime Ethernet (S7-1500, S7-1500T)

#### Introduction: Isochronous Realtime Ethernet

IRT is a transmission method by which PROFINET devices are synchronized with very high accuracy.

A sync master specifies the clock to which sync slaves are synchronized. An IO controller or an IO device can have the role of sync master.

Sync master and sync slaves are always devices in a sync domain. Bandwidth is reserved within the sync domain for IRT communication. Real-time and non-real-time communication (TCP/IP communication) is possible outside of the reserved bandwidth.

#### Time ranges of communication cycles

The communication cycle is divided into three time ranges, which are represented in the following chart:

![Time ranges of communication cycles](images/22848778251_DV_resource.Stream@PNG-en-US.png)

- IRT data (synchronized communication)

  This area can be reserved in specific steps, depending on the send clock. Within this time range the IRT data is transmitted.
- RT data (real-time communication)

  In this time range the cyclic RT date is transmitted. RT data has a higher priority than "normal" TCP/IP data. TCP/IP data or Ethernet frames can have a priority between 1 and 7. RT data has a priority of 6.
- TCP/IP data (standard communication)

  Standard communication (TCP/IP, etc.) is transmitted in the remaining interval of the communication cycle.

#### Applications of IRT

PROFINET with IRT is especially suited for:

- High performance and deterministics for large quantity structures with regard to user data communications (productive data)
- High performance even with many devices in the line topology with regard to user data communications (productive data).
- Parallel transmission of production and TCP/IP data over wire, and securing the forwarding of production data when data volume is high by reserving transmission bandwidth.

---

**See also**

[Basic procedures for configuring IRT (S7-1500, S7-1500T)](#basic-procedures-for-configuring-irt-s7-1500-s7-1500t)
  
[Configuring PROFINET IO with IRT (S7-1500, S7-1500T)](#configuring-profinet-io-with-irt-s7-1500-s7-1500t)
  
[Sync domain (S7-1500, S7-1500T)](#sync-domain-s7-1500-s7-1500t)

### Basic procedures for configuring IRT (S7-1500, S7-1500T)

#### Basic procedures for configuring IRT

If you want to upgrade equipment with PROFINET IO to IRT, follow these three steps:

1. Configure the PROFINET IO device. The PROFINET device must support IRT.
2. Set which device acts as the sync master and synchronizes the other devices. For this you must configure a sync domain with a sync master and at least one sync slave.
3. Download the configuration to all involved devices.

#### Creating PROFINET IO configuration for IRT

As a prerequisite for IRT configuration, there must be an existing PROFINET IO configuration, i.e., one or more stations must be configured with an IO controller and IO devices.

You can read which components are suitable for IRT communication in the task card "Information", once you have selected the corresponding components in the hardware catalog.

The requirements for functioning IRT communication are met simply by configuring a PROFINET IO system with components that support IRT.

### Configuring PROFINET IO with IRT (S7-1500, S7-1500T)

#### Introduction

If you want to increase the precision of cyclic data exchange via PROFINET IO with IRT, you must first configure the PROFINET IO devices. These PROFINET devices must support IRT. Now set which device is to act as sync master and synchronize the other devices. This is done by configuring a sync domain with a sync master and at least one sync slave.

#### Requirement

- There is an IO system with an IO controller and at least one IO device.
- All devices involved support IRT.

#### Procedure

Proceed as follows to configure IRT for an existing IO system:

1. Select the PROFINET interface of the **IO controller**.
2. Navigate to "Advanced options &gt; Realtime settings &gt; Synchronization" in the inspector window.
3. Assign the IO controller the role of sync master under "Synchronization role".
4. Now select the PROFINET interfaces of an associated **IO device**.
5. Navigate to "Advanced options &gt; Realtime settings &gt; Synchronization" in the inspector window.
6. Activate the RT class "IRT". The IO device is then automatically assigned the synchronization role "sync slave".
7. You can check and correct your settings at any time using the "Sync domain" button.
8. Interconnect the ports between the sync slaves and sync master.

Or

1. Highlight the PROFINET IO system in the network view.
2. Click on the PROFINET IO system.
3. Navigate to the node of the required sync domain in the inspector window.
4. Enter all necessary settings in the tables:

   - Select an IO system.
   - Set the synchronization role "sync master" for the IO controller.
   - Set the RT class for the IO devices to "IRT". The IO devices is then automatically assigned the synchronization role "sync slave".
5. Interconnect the ports between the sync slaves and sync master.

You can now load the configuration to the relevant devices with PROFINET IRT.

> **Note**
>
> **Automatic assignment of a sync master**
>
> You can also simply configure an I-device or IO device as sync slave by switching the RT class from RT to IRT. The IO controller that has been assigned to the I-device or IO device is automatically configured as sync master.
>
> If you have configured the IO controller as a sync slave, this setting is not overwritten. The IO controller is thus not switched automatically from sync slave to sync master.
>
> If you assign more than one IO controller to the IO device as a Shared Device, the IO controller automatically selected as the sync master is the one that is assigned to the interface of the IO device.

> **Note**
>
> **Switching between RT and IRT**
>
> In hierarchical IO systems, IRT communication can be combined with RT communication but cannot run simultaneously in both IO systems: If the option "Parameter assignment for the PN interface and its ports on the higher-level IO controller" is selected on the I-device, the I-device can use IRT communication on the higher-level IO controller. If the option is disabled, the lower-level IO system can use IRT communication but you cannot switch between RT and IRT on the I-device.

### Sync domain (S7-1500, S7-1500T)

#### Sync domain

A sync domain is required for synchronization of PROFINET IO devices. The sync domain assures that all devices belonging to it communicate synchronously.

Prerequisite for IRT communication is a synchronization cycle to distribute a common time base for all PROFINET devices in a sync domain. With this base synchronization, a synchronous transmission cycle of PROFINET devices within a sync domain is achieved. The sync master (usually an IO controller) generates the common synchronization clock and specifies the time basis on which all other sync slaves (usually IO devices) are synchronized.

If the sync master fails and no redundant sync master was configured, the communication between the IRT devices reverts to RT quality.

#### Background processes during configuration of an IO system

If you configure an IO controller and network it with an Ethernet subnet, it will automatically be added to the default sync domain of the Ethernet subnet. The default sync domain is always available. The IO controller operates unsynchronized.

If you assign an additional IO device to the IO system of the IO controller, the IO device automatically assigns the IO controller's sync domain.

---

**See also**

[Working with sync domains (S7-1500, S7-1500T)](#working-with-sync-domains-s7-1500-s7-1500t)
  
[Configuring a redundant sync master (S7-1500, S7-1500T)](#configuring-a-redundant-sync-master-s7-1500-s7-1500t)

### Working with sync domains (S7-1500, S7-1500T)

#### Working with sync domains

All components that take part in IRT communication must belong to a sync domain.

A sync domain is a group of PROFINET devices that are synchronized to a common clock. Exactly one device has the role of sync master (clock); all other devices have the role of sync slaves.

#### Default sync domain

If you have applied an Ethernet subnet, a special sync domain is automatically applied: the default sync domain. All PROFINET devices configured for the Ethernet subnet automatically belong to this sync domain.

The following figures illustrate the interaction:

![Default sync domain](images/11462936587_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Default domain; always present |

![Default sync domain](images/11517456651_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Default domain; always present |
| ② | Newly configured PROFINET IO systems are first located in the default domain. |

### Editing properties of sync domains (S7-1500, S7-1500T)

#### Editing properties of sync domains

Details of how to define the name and the send clock in a sync domain are given below. In addition, you will learn how to set a sync domain as default domain.

#### Requirement

- At least one IO device is created in the project.
- At least one sync domain already exists.

#### Editing a sync domain

To change the name of a sync domain, adjust the send clock, or set up a default domain, follow these steps:

1. Select the Ethernet subnet in the network view in which the sync domain is set up.
2. Open the Ethernet subnet properties.
3. In the local navigation, choose the entry "Domain management &gt; Sync domains &gt; &lt;Name of sync domain&gt; ".
4. Enter the changes.

   - Enter the desired name of the sync domain in the field "Sync domain name".
   - Choose the send clock from the drop-down menu "Send clock".
   - Select the "Default domain" check box if you wish to set the sync domain as the default domain.

#### Bandwidths for the various RT classes

Available and calculated bandwidths for the various RT classes within a sync domain are displayed in addition to the name and send clock settings.

Select the "Details" section in the area navigation under the sync domain name.

---

**See also**

[Bandwidth use for synchronized IO controllers (S7-1500, S7-1500T)](#bandwidth-use-for-synchronized-io-controllers-s7-1500-s7-1500t)

### Bandwidth use for synchronized IO controllers (S7-1500, S7-1500T)

#### Use of the bandwidth

Here you set how much send time there is for the cyclic IO data (real-time data by IRT) and the other data (data by TCP/IP or UDP/IP, RT data).

With this, you specify how the bandwidth (transmission capacity) is used.

**Cyclic IO data by IRT**

Cyclic IO data is sent using IRT (isochronous real time).

Certain periods are exclusively available for IRT.

**Reserved period for IRT**

You decide the duration of these reserved periods (time slices) by selecting them in the drop-down list.

All other data is transferred in the time remaining until the beginning of the next send clock.

Select from the following options:

- Maximum 25% cyclic IO data. Focus on non-cyclic data (data using TCP/IP or UDP/IP)
- Maximum 37.5% cyclic IO data. Focus on non-cyclic data (data using TCP/IP or UDP/IP)
- Maximum 50% cyclic IO data. Balanced proportion
- Maximum 90% cyclic IO data. Focus on cyclic data (data using IRT)

---

**See also**

[Configuration of IRT with high performance](#configuration-of-irt-with-high-performance)

### Defining devices of a sync domain (S7-1500, S7-1500T)

#### Defining devices of a sync domain

All components that take part in IRT communication must belong to a sync domain. Instructions on how to define the nodes of a sync domain are given below.

#### Requirement

PROFINET IO systems are already configured and are in the default domain.

#### Adding a new device to the sync domain

To assign a sync domain to a device, follow these steps:

1. Select the Ethernet subnet in the network view in which the sync domain is set up.
2. Open the Ethernet subnet properties.
3. In the local navigation, select the entry "Domain management &gt; Sync domains &gt; &lt;Name of sync domain&gt; &gt; Devices".
4. Click "Add devices" in the "Station / IO System" table.

   The "Select IO system" dialog opens.
5. Select all devices you want to assign to the sync domain and click "OK".

The selected IO system will be removed from the original sync domain and assigned to the current sync domain.

#### Removing devices from the sync domain

To remove a device from a sync domain, follow these steps:

1. Select the Ethernet subnet in the network view in which the sync domain is set up.
2. Open the Ethernet subnet properties.
3. In the local navigation, select the entry "Domain management &gt; Sync domains &gt; &lt;Name of sync domain&gt; &gt; Devices".
4. Select the devices in the table "Station / IO-System" which you would like to remove and press &lt;DEL&gt;.

The devices will be deleted and reassigned to the default domain.

### Configuring a redundant sync master (S7-1500, S7-1500T)

You can configure a redundant sync master for PROFINET IO devices in IRT operation.

Example: An S7-1500 CPU can be configured as a sync master, a Scalance 6GK5 201-3BH00-2BA3 V5.0 can be configured as a redundant sync master.

#### Principle of operation

A redundant sync master belongs to the same sync domain as the "primary" sync master. It prevents a communication failure in the sync domain in the event the primary sync master fails.

Both the sync master and the redundant sync master send sync frames. A sync slave is synchronized to the sync frame of the sync master. If the sync master fails, a sync slave is synchronized automatically to the sync frames of the redundant sync master.

#### Rules

- The redundant sync master role is assigned to only one device in the sync domain.
- The sync domain contains only IRT devices with "IRT with high performance" option.
- There are a maximum of 2 nodes between the sync master and the redundant sync master.

#### Procedure

To configure a redundant sync master, follow these steps:

1. In the device view or network view, select the device that you want to configure as a redundant master.
2. Under "PROFINET interface &gt; Advanced options &gt; Real time settings &gt; Synchronization &gt; Synchronization role", select the "Redundant sync master" option.

### Rules and information for IRT configurations (S7-1500, S7-1500T)

The following rules and information apply to PROFINET configurations. Additional system recommendations for optimizing your PROFINET system can be found [here](Configuring%20devices%20and%20networks.md#connecting-existing-bus-systems).

#### Setting up PROFINET with IRT

Keep in mind the following rules for the set up and operation of a PROFINET IO system in IRT operation. They serve to insure an optimal operation of your PROFINET IO system.

- When using IRT, you must configure the topology. This will enable exact calculation of the update time, bandwidth, and additional parameters.
- If you would like to use multiple sync domains, configure a sync domain boundary for the port which is currently connected to the PROFINET device of another sync domain.
- In a sync domain you can only configure one sync master at a time.
- A PROFINET IO system may only be part of a single sync domain.
- If you configure a PROFINET device in a sync domain and want to synchronize with IRT, the PROFINET devices concerned must support IRT communication.
- Wherever possible, use the same PROFINET device as the PROFINET IO controller and sync master.
- If only some of the PROFINET devices in a PROFINET IO system are synchronized, please keep in mind the following: PROFINET devices which are not part of IRT communication are placed outside of the sync domain.
- Higher-level and lower-level IO systems can use RT communication simultaneously. IRT communication can be combined with RT communication but cannot run simultaneously in both IO systems: If the option "Parameter assignment for the PN interface and its ports on the higher-level IO controller" is selected on the I-device, the I-device can use IRT communication on the higher-level IO controller. If the option is disabled, the lower-level IO system can use IRT communication.

---

**See also**

[Configuration of IRT with high performance](#configuration-of-irt-with-high-performance)

### Configuring isochronous mode (S7-1500, S7-1500T)

This section contains information on the following topics:

- [What is isochronous mode? (S7-1500, S7-1500T)](#what-is-isochronous-mode-s7-1500-s7-1500t)
- [Use of isochronous mode (S7-1500, S7-1500T)](#use-of-isochronous-mode-s7-1500-s7-1500t)
- [Time sequence of synchronization (S7-1500, S7-1500T)](#time-sequence-of-synchronization-s7-1500-s7-1500t)
- [The Ti Value (S7-1500, S7-1500T)](#the-ti-value-s7-1500-s7-1500t)
- [The To Value (S7-1500, S7-1500T)](#the-to-value-s7-1500-s7-1500t)
- [Isochronous interrupt OB (OB 6x) (S7-1500, S7-1500T)](#isochronous-interrupt-ob-ob-6x-s7-1500-s7-1500t)
- [Program Execution According to the IPO Model with Long Time (S7-1500, S7-1500T)](#program-execution-according-to-the-ipo-model-with-long-time-s7-1500-s7-1500t)
- [Configuring isochronous mode (S7-1500)](#configuring-isochronous-mode-s7-1500)
- [Configuring isochronous mode](#configuring-isochronous-mode)
- [Setting isochronous mode on the subnet (S7-1500, S7-1500T)](#setting-isochronous-mode-on-the-subnet-s7-1500-s7-1500t)
- [Rules, requirements, and supplemental conditions (S7-1500, S7-1500T)](#rules-requirements-and-supplemental-conditions-s7-1500-s7-1500t)

#### What is isochronous mode? (S7-1500, S7-1500T)

##### Objectives of isochronous operation

Assuming public transport were to operate at maximum speed while reducing stop times at the passenger terminals to absolute minimum, the last thing many potential passengers would notice of the departing contraption are its red tail lights. The overall travel time is, however, decided by the train, bus or underground clock, because well adjusted timing is essential to a good service. This also applies to distributed automation engineering. Not only fast cycles but also the adaptation and synchronization of the individual cycles result in optimum throughput.

##### Just-In-Time

![Just-In-Time](images/40080164235_DV_resource.Stream@PNG-en-US.png)

The high speed and reliable reaction time of a system operating in isochronous mode is based on the fact that all data are provided just-in-time. The constant PROFINET IO cycle beats the time here.

---

**See also**

[Information about the Oversampling function](Configuring%20devices%20and%20networks.md#information-about-the-oversampling-function)

#### Use of isochronous mode (S7-1500, S7-1500T)

##### Use of isochronous mode

With the "Isochronous mode" system property, measured values and process data can be acquired in a fixed system clock. The signal processing up to the switching-through to the "output terminal" occurs within the same system clock. Isochronous mode thus contributes to high-quality control and hence to greater manufacturing precision. With isochronous mode, the possible fluctuations of process response times are drastically reduced. The time-assured processing can be utilized to improve machine cycle times.

In principle, isochronous mode is worthwhile whenever measured values must be acquired synchronously, movements must be coordinated, and process responses must be defined and simultaneously executed, as in the following example.

#### Time sequence of synchronization (S7-1500, S7-1500T)

##### From reading-in or input data to outputting of output data

The basic time sequence of all components involved in synchronization is explained in the following:

- Reading-in of input data in isochronous mode
- Transport of input data to the IO controller (CPU) via the PROFINET subnet
- Further processing in the isochronous application of the CPU
- Transport of output data to the outputting IO device via the PROFINET subnet
- Outputting of output data in isochronous mode

  ![From reading-in or input data to outputting of output data](images/40088341003_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | T_DC | Data cycle (Time_DataCycle) |
  | T<sub>I</sub> | Time for reading in the input data |
  | T<sub>O</sub> | Time for outputting the output data |

To ensure that all input data is ready for transportation via the PROFINET IO line when the next PROFINET IO cycle begins, the IO read cycle has a lead time T<sub>I</sub> so that it starts earlier. T<sub>I</sub> is the "flashbulb" for the inputs; at this instant, all synchronized inputs are read in. T<sub>I</sub> is necessary in order to compensate for analog-to-digital conversion, backplane bus times, and the like. The lead time T<sub>I</sub>can be set automatically by STEP 7, taken from the settings of the associated isochronous mode interrupt OB, or configured by the user. We recommend allowing STEP 7 to automatically assign the lead time T<sub>I</sub>.

The PROFINET IO line transports the input data to the IO controller. The isochronous mode interrupt OB (OB 61, OB 62, OB 63, or OB 64) is called after a parameterizable delay time. The user program in the isochronous mode interrupt OB decides the process reaction and provides the output data in time for the start of the next data cycle. The length of the data cycle is always configured by the user.

T<sub>O</sub> is the compensation arising from the backplane bus and the digital-to-analog conversion within the device. T<sub>O</sub> is the "flashbulb" for the outputs; at this instant, the synchronized outputs are output. The time T<sub>O</sub> can be set automatically by STEP 7, taken from the settings of the associated isochronous mode interrupt OB, or configured by the user. We recommend allowing STEP 7 to automatically assign the time T<sub>O</sub>.

##### Isochronous mode and non isochronous mode distributed I/O

It is possible to combine isochronous mode distributed I/O with non isochronous mode distributed I/O on one IO controller.

#### The Ti Value (S7-1500, S7-1500T)

##### Effect of T<sub>I</sub>

The effect of T<sub>I</sub> is illustrated by the following figure:

![Effect of TI](images/40193293323_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| T_DC | Data cycle |
| T<sub>I</sub> | Time for reading in the input data |

##### Sequence

So that a consistent state of the inputs can be transferred to the IO controller at the start of the new system clock cycle, the import must be brought forward by the time T<sub>I</sub>. The time T<sub>I</sub> for a particular input module includes at least the signal conditioning and conversion time on the electronics modules and the time for transfer to the interface module on the IO device backplane bus.

In the plant, the values are imported at the same time because the T<sub>I</sub> of the various input modules is set to the same value and this value is greater than or equal to the highest minimum T<sub>I</sub> of all input modules. With the default setting, Step 7 makes sure that the smallest possible mutual T<sub>I</sub> is set.

#### The To Value (S7-1500, S7-1500T)

##### Effect of T<sub>O</sub>

The effect is illustrated by the following figure:

![Effect of TO](images/40193324939_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| T_DC | Data cycle |
| T<sub>O</sub> | Time of data output |

##### Sequence

To ensure that a consistent status of the outputs can be transferred to the process at the start of the new system clock cycle, the data is output at the time T<sub>o</sub> following the last clock beat. The time T<sub>O</sub> records the time of the transfer from the IO-controller to the IO device (through PROFINET IO) for a certain output module and in the IO device, the transfer of the outputs from the interface module to the electronic module (backplane bus)(if applicable, plus time for the digital-analog conversion).

The system makes sure that the values are written simultaneously by setting the T<sub>O</sub> of all isochronous output modules to the same value. This value must be greater than or equal to the largest minimal T<sub>O</sub> of all isochronous output modules. STEP 7 automatically calculates the shared smallest possible T<sub>O</sub>.

#### Isochronous interrupt OB (OB 6x) (S7-1500, S7-1500T)

You use the isochronous mode interrupt OB (e.g., OB 61) for the isochronous connection of the user program.

##### Call of isochronous mode interrupt OB

The isochronous interrupt OB is triggered by the system clock, or more precisely by an adjustable delay time after the system clock. The effect is illustrated by the following figure:

![Call of isochronous mode interrupt OB](images/40193625611_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| T_DC | Data cycle |

##### Delay time

STEP 7 initially automatically calculates a suitable value for the delay time. The delay time compensates the transfer time of the inputs of the isochronous IO devices to the IO controller through the PROFINET IO-network. The execution of OB 6x is linked to the system clock and the specified delay time. The delay time can also be manually corrected, if necessary. For example, you can shorten the delay time in order to process program sections that do not access the isochronous I/O at the start of OB 6x. This gains you runtime for the isochronous user program.

##### Connection of isochronous I/O to the isochronous mode interrupt OB

You access the isochronous I/O via a process image partition, i.e., the addresses of isochronous modules must be in a process image partition.

Any access to isochronous I/O must be programmed by the SYNC_PI and SYNC_PO instructions within the isochronous mode interrupt OB.

You call SYNC-PI at the start of OB 6x, provided you have selected the automatic setting for the delay time. You call SYNC_PO at the end of OB 6x.

##### T_DC, application cycle, and send clock

The time T_DC designates the time for one data cycle, i.e., this time is the shortest possible time for reading in, processing, and outputting the data (IPO model). T_DC is always a multiple of the send clock.

If IRT is activated for an IO device, T_DC is then equal to the send clock. The update time corresponds to the send clock.

The application cycle is a multiple of the data cycle. It can be identical to the data cycle if the runtime of the isochronous mode interrupt OB is correspondingly short.

##### Program processing according to the IPO model with short time

The IPO model with application cycle factor = 1 is characterized by the fact that the I/O data are completely processed within one system clock T_DC. This model is used to achieve the shortest response times.

#### Program Execution According to the IPO Model with Long Time (S7-1500, S7-1500T)

##### Label of the IPO-model with application cycle factor &gt; 1

If the runtime of the isochronous mode OB is longer than one data cycle T_DC, the output must be delayed by one application cycle (OB 6x). For this reason, data output occurs before data input in this model.

The SYNC_PI and SYNC_PO instructions must then be called during the execution window of the first data cycle (only available there when application cycle factor &gt; 1).

The execution window refers to the time period during which a call of the SYNC_PI and SYNC_PO instructions is possible, i.e., after transfer of cyclic data via PROFINET up to the time shortly before the end of data cycle T_DC.

The other user program processing in OB 6x then occurs in the next data cycle or over the following data cycles.

![Label of the IPO-model with application cycle factor > 1](images/94165892875_DV_resource.Stream@PNG-en-US.png)

The figure shows the signal sequence with application cycle factor = 2 (application cycle = 2x data cycle) from the time of acquisition (E) through the processing (V) in the IO controller until output (A) of the process values. STEP 7 calculates the delay time. In this time, the read input data is on its way on PROFINET IO.

This model is especially well-suited for large I/O configurations with one extensive user program in OB 6x. With this model, longer calculation times are possible when processing the input data and obtaining the corresponding output data.

The constant processing time from the "input terminal" to the "output terminal" is T<sub>I</sub> + (application cycle factor + 1) x T_DC + T<sub>O</sub>. T<sub>I</sub> + (2 x application cycle factor + 1) x T_DC + T<sub>O</sub> can be guaranteed as a process reaction time.

#### Configuring isochronous mode (S7-1500)

##### Introduction

The configuring of isochronous mode of a module is described as IO device in the following based on the new ET 200MP distributed I/O series. The procedure described also applies to other distributed I/O systems (e.g., ET 200S or ET 200SP).

The IO controller is an S7-1500 CPU.

##### Requirement

- The network view is open.
- An S7-1500 CPU is placed (e.g., CPU 1516-3 PN/DP).
- A distributed I/O device is placed (e.g., IM 155-5 PN HF) and networked with the CPU.
- All requirements for an IRT configuration are met, namely:

  - The ports of the CPU and the IM are interconnected.
  - The RT class of the IM is set to "IRT" (area "Advanced options &gt; Real-time settings &gt; Synchronization").

##### Procedure

To create an isochronous connection between the I/O and user program, follow these steps:

1. Select the distributed I/O device (the IM 155-5 PN HF) in the network view, and switch to the device view.
2. Insert an I/O module with isochronous mode capability (module with name extension "HF", e.g., DI 16x24VDC HF - 6ES7 521-1BH00).
3. Go to "I/O addresses" area in the inspector window of the selected I/O module.
4. Make the following settings in the I/O addresses area:

   - Select the "Isochronous mode" option.
   - Select a process image partition, e.g., process image partition 1.
   - Click on the "Assigned organization block" drop-down list and click the "Add object" button.

     A dialog box for selecting organization blocks opens.
   - Select the "Synchronous Cycle" OB and confirm the selection with "OK".

     In the case of automatic number assignment, OB 61 will be generated and opened. The "Isochronous mode" area is selected in the inspector window, and you can continue directly with the setting of the application cycle and delay time and start the programming of the OB in the instruction section.
5. Add other IO devices as required, network and interconnect these devices, and adapt the configuration and the isochronous mode settings.
6. To retrieve information about calculated bandwidths or to adapt the send clock, select the subnet and navigate to the corresponding area of the sync domain management in the inspector window.

#### Configuring isochronous mode

##### Introduction

The configuring of isochronous mode of a module is described as IO device in the following based on the new ET 200MP distributed I/O series. The procedure described also applies to other distributed I/O systems (e.g., ET 200S or ET 200SP).

The IO controller is an S7-300/400 CPU.

##### Requirement

- The network view is open.
- An S7-300/400 CPU is placed (e.g., CPU 319-3 PN/DP).
- A distributed I/O device is placed (e.g., IM 155-5 PN HF) and networked with the CPU.
- All requirements for an IRT configuration are met, namely:

  - The ports of the CPU and the IM are interconnected.
  - The synchronization role of the PROFINET interface is set to "sync master" (properties of the CPU, area "PROFINET interface&gt; Advanced options &gt; Real-time settings &gt; Synchronization").
  - The RT class of the IM is set to "IRT" (area "PROFINET interface &gt; Advanced options &gt; Real-time settings &gt; Synchronization").

##### Procedure

To create an isochronous connection between the I/O and user program, follow these steps:

1. Select the CPU, and navigate to the "Interrupts &gt; Isochronous mode interrupts" area in the inspector window.
2. Select the distributed I/O device (the IM 155-5 PN HF) in the network view, and switch to the device view.
3. Insert at least one I/O module with isochronous mode capability (module with name extension "HF", e.g., DI 16x24VDC HF - 6ES7 521-1BH00).
4. Assign a process image partition to the I/O module (inspector window, "I/O addresses" area).
5. Select the IM in the device view or network view and navigate in the inspector window to the "PROFINET interface &gt; Advanced options &gt; Isochronous mode" area.

   - Select the "Isochronous mode" option.
   - If you want to change the send clock or the application cycle, click the green link next to the appropriate fields. This takes you to the sync domain where these settings can be centrally changed.
   - For the Ti/To times, select whether their minimum times are to be automatically calculated or whether you want to set them manually. The Ti/To values can only be changed with manual setting.
   - In the detail overview of modules: Select the "Isochronous mode" option for modules that are to be operated in isochronous mode.
6. Add other IO devices as required, network and interconnect these devices, and adapt the configuration and the isochronous mode settings.
7. To retrieve information about calculated bandwidths or to adapt the send clock, select the subnet and navigate to the corresponding area of the sync domain management in the inspector window.

#### Setting isochronous mode on the subnet (S7-1500, S7-1500T)

##### Introduction

The subnet properties include not only the sync domain properties and MRP properties but also provide an overview of the isochronous mode settings.

##### Requirement

A PROFINET IO system with IO controller and IO devices is configured.

##### Procedure

To display the isochronous mode properties of the subnet, follow these steps:

1. Select the subnet.
2. Select the "Overview of isochronous mode" area in the properties.

##### Settings in the overview of isochronous mode

| Symbol | Meaning |
| --- | --- |
| CPU | Selection of a CPU (IO controller) of the subnet |
| Isochronous application | Selection of an OB of the selected CPU that is assigned to an IO system. |
| **Details of the isochronous application** |  |
| Application cycle | Indicates the application cycle (multiple of data cycle). For S7-300/400, you specify the time in the CPU properties, while for S7-1500, you specify the time in the isochronous mode OB properties. |
| Delay time | Indicates the time between the system clock and start of the isochronous mode interrupt OB (e.g., OB 61). |
| Send clock | Indicates the time period between two consecutive intervals for IRT or RT communication. |
| IO system no. | Indicates the no. of the PROFINET IO system assigned to the OB. |
| Process image partition | Indicates all process image partition numbers that are assigned to the PROFINET IO system. |
| **Ti/To values for OB** |  |
| Ti/To values automatic | If this option is selected, STEP 7 then calculates one Ti value and one To value suitable for all modules that will be operated in isochronous mode and are assigned to the OB. You can reference these common Ti/To values in the IO devices/Modules table (Ti/To values = from the OB). |
| Time Ti | Time for reading-in the isochronous input data. |
| Time To | Time for outputting the isochronous output data. |
| **IO devices/Modules** |  |
| Table with Ti/To values: | Isochronous mode can be activated and deactivated for each IO device/module in the IO device.   Ti/To values: Three settings are possible:  - Automatic: Ti/To will be calculated automatically. - Manual: Ti/To can be edited. - From the OB: Ti/To values will be taken from the OB.   Ti, To: Can only be edited when "manual" setting is selected.  TiMin/TiMax: Minimum or maximum time for Ti.  ToMin/ToMax: Minimum or maximum time for To.  Interval: Specified interval for Ti/To values. |

#### Rules, requirements, and supplemental conditions (S7-1500, S7-1500T)

##### What you need to be aware of for configuring isochronous mode is

Take into consideration the following notes on configuring isochronous mode.

##### Components and PROFINET interfaces

- Isochronous mode is only possible with the interfaces integrated in the CPU. For S7-1500 CPUs with two PROFINET interfaces, only the X1 interface can be used for isochronous mode. Isochronous mode is not possible with S7-1500-CPs/S7-1500-CMs.
- A full isochronous mode from "terminal" to "terminal" is only possible if all components participating in the chain support the "isochronous mode" system property. When selecting in the catalog, make sure you check the "isochronous mode" or "processing in isochronous mode" entry in the information field of the module.
- If you operate an IO device in isochronous mode (i.e., you have assigned it the sync slave role, for example), the IO device must contain at least one module or submodule operated in isochronous mode.

##### Subnet-overlapping isochronous mode

- Subnet-overlapping isochronous mode is not currently possible.

##### Process image partitions

- Isochronous I/O can only be processed in process image partitions. Without the use of process image partitions isochronous consistent data transfer is not possible. Compliance with configuration limits is monitored because there is a limit on the number of IO devices and the number of bytes on the DP System per process image partition.
- The addresses of the isochronous I/O have to lie in a process image partition.
- The process image partition for isochronous I/O may also contain non-isochronous I/O.
- S7-300/400: More than one process image partition is possible per isochronous mode interrupt OB or IO system.
- S7-1500: Exactly one process image partition is possible per isochronous mode interrupt OB or IO system. Only modules or submodules of the same IO system or the same isochronous mode interrupt OB may be contained in the same process image partition.

##### Times

- If isochronous mode is active, the update time in the IO devices calculated by STEP 7 must always be identical to the send clock. It is not possible to manually change the update time.
- The time for the application cycle is limited to 32 ms.
- The delay time for the isochronous mode interrupt OB must be between 0 and (data cycle - 1 μs).

## Configuring I-devices

This section contains information on the following topics:

- [I-Device Functionality](#i-device-functionality)
- [Properties and Advantages of the I-Device](#properties-and-advantages-of-the-i-device)
- [Data Exchange between Higher- and Lower-level IO System](#data-exchange-between-higher--and-lower-level-io-system)
- [Configuring diagnostics addresses (S7-300, S7-400)](#configuring-diagnostics-addresses-s7-300-s7-400)
- [Configuring the I device](#configuring-the-i-device)
- [Rules for creating transfer areas](#rules-for-creating-transfer-areas)
- [Exporting an I-device as a GSD file](#exporting-an-i-device-as-a-gsd-file)
- [Multiple assignment of IO controllers](#multiple-assignment-of-io-controllers)
- [Constraints on the Use of I-Devices](#constraints-on-the-use-of-i-devices)
- [Diagnostics and interrupt characteristics](#diagnostics-and-interrupt-characteristics)
- [Online diagnostics for I devices](#online-diagnostics-for-i-devices)
- [Disabling I-device in the user program of the I-device CPU](#disabling-i-device-in-the-user-program-of-the-i-device-cpu)

### I-Device Functionality

#### I-Device Functionality

The "I-device" functionality (intelligent IO device) of a CPU allows data to be exchanged with an IO controller and therefore to use the CPU, for example, as an intelligent preprocessing unit of subprocesses. The I-device is linked as an IO device to a "higher-level" IO controller.

The preprocessing is handled by the user program on the CPU. The process values acquired in the central or distributed (PROFINET IO or PROFIBUS DP) I/O are preprocessed by the user program and made available via a PROFINET IO device interface to the CPU or the CP of a higher-level station.

![I-Device Functionality](images/23137656075_DV_resource.Stream@PNG-en-US.png)

#### "I-device" naming conventions

In the remainder of this description, a CPU or a CP with the I-device functionality is simply called an "I-device".

### Properties and Advantages of the I-Device

#### Fields of application

Areas of application of the I-device:

- Distributed processing

  A complex automation task can be divided into smaller units/subprocesses. This makes the process easier to handle because the subtasks are simpler.
- Separating subprocesses

  Complicated, widely distributed and extensive processes can be subdivided into several subprocesses with manageable interfaces by using I-devices. These subprocesses can be stored in individual projects if necessary, which can later be merged to form one master project.
- Know-how protection

  Components can only be delivered with a GSD file for the I-device interface description instead of with a project. The know-how of the user program must no longer be published.

#### Properties

Properties of the I-device:

- Unlinking projects

  Creators and users of an I-device can have completely separated automation projects. The interface between the projects forms the GSD file. This allows a link to standard IO controllers via a standardized interface.
- Real-time communication

  The I device is provided with a deterministic PROFINET IO system via a PROFINET IO interface and therefore supports RT (real-time communication).

#### Advantages

The I-device offers the following advantages:

- Simple linking of IO controllers without additional software tools
- Real-time communication between SIMATIC CPUs and to standard IO controllers.
- By distributing the computing power among several I devices, the required computing power of the individual CPUs and the IO controller can be reduced.
- Lower communications load by processing process data locally.
- Clarity by processing the subtasks in separate CPUs or projects.

### Data Exchange between Higher- and Lower-level IO System

#### Introduction

The next section shows the data exchange between a higher- and lower-level IO system.

#### Transfer areas

The data for communication between IO controller and I device is made available in the transfer areas. A transfer area contains an information unit that is exchanged consistently between IO controller and I device.

Application transfer areas are an interface to the user program of the I-device CPU. Inputs are processed in the user program and outputs are the result of the processing in the user program.

The following figure shows the data exchange between a higher- and lower-level IO system. The individual communication relations are explained below based on the numbers.

![Transfer areas](images/23141445131_DV_resource.Stream@PNG-en-US.png)

**① Data exchange between higher-level IO-controller and normal IO-device**

In this way, the IO controller and IO device exchange data through PROFINET.

**② Data exchange between the higher-level IO controller and I-device**

In this way, the IO controller and the I-device exchange data through PROFINET.

The data exchange between a higher-level IO controller and an I-device is based on the conventional IO controller / IO device relationship.

For the higher-level IO controller, the transfer areas of the I-devices represent submodules of a preconfigured station.

The output data of the IO controller is the input data of the I-device. Analogously, the input data of the IO controller is the output data of the I-device.

**③ Transfer relationship between the user program and the transfer area**

In this way, the user program and the application transfer area exchange input and output data.

**④ Transfer relationship between the transfer area and the I/O of the I-device**

This is not currently supported in the configuration.

**⑤ Data exchange between the user program and the I/O of the I-device**

In this way, the user program and the central / distributed I/O exchange input and output data.

**⑥ Data exchange between the I-device and a lower-level IO device**

In this way, the I-device and its IO devices exchange data. The data transfer is via PROFINET.

### Configuring diagnostics addresses (S7-300, S7-400)

#### Introduction

When assigning diagnostics addresses for PROFIBUS IO, you must ensure that IO diagnostics addresses are assigned to both the IO controller and the I-device.

![Introduction](images/96640350859_DV_resource.Stream@PNG-en-US.png)

#### Diagnostics addresses

A distinction is made between diagnostics addresses on the IO controller and those on the I-device:

- Diagnostics addresses on the IO controller

  The IO controller receives information about the status of the IO device or a bus interruption via the diagnostics addresses assigned to the IO controller.
- Diagnostics addresses on the I-device

  The I-device receives information about the status of the IO controller or a bus interruption via the diagnostics addresses assigned to the I-device.

STEP 7 automatically assigns diagnostics addresses for the respective CPUs when the controller-I-device configuration is specified. The following describes how to change the specified diagnostics addresses.

Tip: In order to obtain an overview of all addresses assigned for the CPU, including diagnostics addresses, select the "Address overview" area in the inspector window of the selected CPU.

#### Diagnostics addresses of the I-device communication

A table with the diagnostics addresses of the I-device communication is displayed on the I-device. The identifier for the diagnostics address is the name of the PLC and the transfer area with the lowest subslot number. When you activate the parameter assignment of the PN interface by the higher-level IO controller for the operating mode of the PROFINET interface on the I-device, the diagnostics addresses for the PROFINET interface and its ports are displayed as well. You can edit the diagnostics addresses used in the table.

![Diagnostics addresses of the I-device communication](images/96685277451_DV_resource.Stream@PNG-en-US.png)

The table is only displayed when the IO controller is a CPU 300/400:

| IO controller | Display of the diagnostics addresses |
| --- | --- |
| CPU 300/400 | Local addresses of the I-device |
| CPU 1200/1500 | No display |

#### Requirement

- You must be in the network view.
- You have created an IO system with IO controller and I-device.

#### Procedure

To edit the diagnostics addresses for the I-device communication, follow these steps:

1. Select the IO controller or the I-device.
2. In the I/O communication table, select the line showing "I-device" mode.
3. Edit the diagnostics addresses under "Properties &gt; I-device communication &gt; Diagnostics address of communication" in the Inspector window.

Or:

1. Select the I-device.
2. Edit the diagnostics addresses under "Properties &gt; PROFINET interface &gt; Mode &gt; I-device communication &gt; Diagnostics address of communication" in the Inspector window.

You can select and edit the fields containing the values of the diagnostics addresses both for the device and the controller.

#### Additional information

For further information on diagnostics addresses, refer to the manuals for the individual S7 CPUs.

### Configuring the I device

#### Introduction

There are basically two possibilities for configuration:

- Configuration of an I-device within a project
- Configuration of an I-device that is used in another project or engineering system.

STEP 7 allows to you configure an I-device for another project or for another engineering system by exporting a configured I-device to a GSD file. You import the GSD file in the other project or the other engineering system as with other GSD files. The transfer areas for the data exchange, among other data, is stored in this GSD file.

#### Configuration of an I-device within a project

1. Drag and drop a PROFINET IO controller from the hardware catalog into the network view.
2. Drag and drop a PROFINET IO controller which can also be configured as IO device from the hardware catalog into the network view. This device is configured as an I-device (for example, CPU 319-3 PN/DP, FW 3.2).
3. Select the PROFINET interface for the I-device.
4. In the area navigation of the Inspector window, select the "Operating mode" entry and select the "IO device" check box.
5. For S7-1500 CPUs as of FW Version V3.1:  
   Click in the table "Assigned IO Controllers" on "Assign new IO Controller" and in the selection list, select the PROFINET interface of an IO Controller which you want to assign to the I Device.  
   For S7-1500 CPUs up to FW Version V3.0:  
   In the drop-down list "Assigned IO Controller" you now have the possibility to select the IO Controller.

   Once you have chosen the IO controller, the networking and the IO system between both devices are displayed in the network view.
6. With the "Parameter assignment of PN interface by higher-level IO controller" check box, you can specify whether the interface and its ports are set by the I-device itself or a higher-level IO controller.

   If you operate the I-device with a lower-level IO system, then the parameters of the I-device PROFINET interface (for example, port parameters) cannot be set by the higher-level IO controller.
7. Configure the transfer areas. Those are the I/O areas over which the I-device exchanges data with the higher-level IO controller. The transfer areas are found in the area navigation section "I-device communication".

   - Click in the first field of the "Transfer areas" column. STEP 7 assigns a default name which you can change.
   - Select the type of communication relation, for example, CD for "Controller-device communication relation".
   - Addresses are automatically preset; you can correct addresses if necessary and determine the length of the transfer area which is to be consistently transferred.
8. A separate entry is created in the area navigation for each transfer area. If you select one of these entries, you can adjust the details of the transfer area, or correct them and comment on them.

   If the CPU supports it, you can also activate the "Bi-directional address mapping" function. In this case the automatic address areas will be arranged "in the opposite direction", so that CPU input and output areas are occupied symmetrically.

> **Note**
>
> **Device replacement in the configuration (V19)**
>
> To replace the configured CPU (I device) by a different CPU you may have to deactivate the operating mode "IO device".

#### Configuring an I-device with a GSD file

If you use an I-device in another project, or if the I-device is used in another engineering system, then configure the higher-level IO controller and the I-device as described above. The I-device must be exported as GSD file afterward. The generated GSD file represents the configured I-device in another project.

To do this, follow the description for [Export of GSD files](#exporting-an-i-device-as-a-gsd-file).

> **Note**
>
> **PROFIsafe transfer module of the type "F-PS"**
>
> If you have inserted a PROFIsafe transfer module of the type "F-PS", the I-device must not be assigned to an IO controller in this project. A GSD file must be exported. You can use this GSD file to set all PROFIsafe parameters in the other project, and to operate the I-device on an IO controller with PROFIsafe capability.

---

**See also**

[Configuring an I-device as a shared device (S7-300, S7-400, S7-1500)](#configuring-an-i-device-as-a-shared-device-s7-300-s7-400-s7-1500)
  
[Multiple assignment of IO controllers](#multiple-assignment-of-io-controllers)
  
[Rules for creating transfer areas](#rules-for-creating-transfer-areas)

### Rules for creating transfer areas

#### Transfer areas

Transfer areas are the I/O areas over which the I-device exchanges data with a higher-level IO controller. The transfer areas are found in the area navigation in the section "I-device communication".

The following rules apply to configuring transfer areas:

- A transfer area has a maximum length of 1024 bytes.
- Each input transfer area forms a submodule. The length of all input transfer areas, i.e. the data length of all submodules (input) cannot exceed 1440 bytes.
- Each output transfer area forms a submodule. The length of all output transfer areas, i.e. the data length of all submodules (output) cannot exceed 1440 bytes.

What is **not** represented when transfer areas are configured in the TIA Portal: In addition to the payload, a submodule also has payload flags of 1 byte in the send direction and 1 byte in the receive direction respectively. These payload flags transport status information relating to the payload, e.g. whether the sent/received data is valid.

The payload flags are usually transparent for PROFINET users and are managed by the system. However, in the case of very long or numerous transfer areas, incomprehensible error messages can occur during compilation of the configuration. The following sections explain the technical reason for this behavior.

#### Payload flags (IOPS and IOCS)

Payload flags are used during PROFINET data exchange to allow the state of the payload to be diagnosed.

A byte that codes the quality of this payload is assigned to each I/O module or transfer area in the input and output data frame: In PROFINET jargon, this is the IO provider status (IOPS) and IO consumer status (IOCS). PROFINET distinguishes between data provider and data consumer here, rather than between inputs and outputs. The advantage of this model: No I/O data areas are required for the status information.

A provider can be:

- An IO controller that sends its output data to an IO device or I-device
- An IO device or I-device that sends its input data to an IO controller

A consumer can be:

- An IO controller that receives its input data from an IO device or I-device
- An IO device or I-device that receives its output data from an IO controller

The figure shows how the transfer of process data (payload) is accompanied by an IO provider status (1 byte IOPS) and how the IO consumer status (1 byte IOCS) is transmitted in the opposite direction.

In summary: For transferring the data of a transfer area, 1 byte in the send direction and 1 byte in the receive direction is required respectively in addition to the payload.

![Payload flags (IOPS and IOCS)](images/149585594507_DV_resource.Stream@PNG-de-DE.png)

#### Example for long transfer areas

The following configuration generates an error message, although the maximum data length of 1440 bytes is not exceeded at first glance. This is because only the lengths of the input data and output data are visible in the I/O address area in the configuration ("net data" without payload flag).

The error message after the compilation of this configuration indicates that the data length of the input data of 1441 bytes incl. payload flag exceeds the maximum permitted data length of 1440 bytes.

Although only 1438 bytes are occupied in the address area of the inputs, the required data length is 3 bytes larger due to the payload flags in the receive direction for each transfer area. The receive area therefore exceeds the maximum permissible data length of 1440 bytes.

Only 4 bytes are occupied in the address area of the outputs; therefore, an error messages does not occur and there is no indication of the existence of payload flags.

![Example for long transfer areas](images/149600395659_DV_resource.Stream@PNG-en-US.png)

The following table includes all transmitted data incl. the payload flags.

| Transfer area / Payload flag | Length in bytes (I/Q) |
| --- | --- |
| MyArea-Input-1 | 1000 (I) |
| MyArea-Input-2 | 438 (I) |
| MyArea-Output-1 | 1 (Q) |
| Payload flag MyArea-Input-1 | 1 (I) + 1(Q) |
| Payload flag MyArea-Input-2 | 1 (I) + 1(Q) |
| Payload flag MyArea-Output-1 | 1 (I) + 1(Q) |
| **Total input data length incl. payload flags** | = 1000 + 438 + 3 = **1441** |
| **Total output data length incl. payload flags** | = 1+ 3 = **4** |

### Exporting an I-device as a GSD file

#### Introduction

If you want to use an I-device in another project or if the I-device is used in another engineering system, you must export the I-device as GSD file. The GSD file contains the description of the I-device and can subsequently be imported and used in the new project.

#### Requirement

- An I-device with I-device communication and transfer area was configured.
- The changes to the hardware were compiled.

#### Procedure

To export an I-device as GSD file, follow these steps:

1. Select the I-device or its PROFINET interface in the hardware and network editor.
2. In the Inspector window, select the "Export" command at the PROFINET interface "Operating mode &gt; I-device communication". The dialog for export of the I-device as GSD file opens.
3. You can now specify the name and a description for the I-device representative and change the storage path of the GSD file.

   ![Procedure](images/96922872843_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/96922872843_DV_resource.Stream@PNG-en-US.png)

   **Designation**: The designation stands for a text that is used as part of the name of the GSD file. This designation will help you identify your GSD file more easily later. The default setting is the PLC name from the current project.

   **Description**: Here you can edit the description. After import of the GSD file to another project, this text is displayed in the hardware catalog at the I-device in the "Description" box. The default is the description of the PLC from the current project.

   **Path**: Here you can enter where you want to store the GSD file. Select a path that is easy for you to remember.
4. Click the "Export" button. The I-device is now exported as a GSD file.

**Note**

With a later import of the GSD file into another project, each imported I-device is created with a new designation as new entry in the hardware catalog. If the designation already exists in the hardware catalog, the I-device is merely added as additional version of an already existing I-device.

Now you have exported the I-device as a GSD file and can use it in another project.

#### Composition of the name of the exported GSD file

You cannot freely select the name of the GSD file because it is subject to a specified scheme. You can only influence the part of the name under which you can find the I-device in the hardware catalog after an import of the GSD file. The structure of the name for the exported GSD file is explained using the following example:

The name of an exported GSD file for I-devices can look as follows:

"GSDML-V2.32-#Siemens-PreConf_PLC_23-20170208-140313.xml"

| Name component | Can be edited? | Description |
| --- | --- | --- |
| GSDML | No | String at the start of each GSD file for I-devices |
| V2.32 | No | Version of the GSDML schema |
| Siemens | No | Manufacturer |
| PreConf | No | Identifier for the GSD file from the export function |
| PLC_23 | Yes | Device designation can be changed. The I-device can be found under this name after import in the hardware catalog of the other project. |
| 20170208 | No | Identifier of the version as date in the format year-month-day (YYYYMMDD). The system data is used as reference. |
| 140313 | No | Identifier of the version as time in the format hour-minute-second (hhmmss). The UTC system time is used as reference. |
| .xml | No | File extension |

#### Import of the exported GSD file in another project

You import the GSD file with the exported I-device by installing the GSD file [as described here](Configuring%20devices%20and%20networks.md#installing-the-gsd-file). After you have selected and installed the GSD file with the I-slave under "Options &gt; "Manage general station description files (GSD) &gt; Installed GSDs", you can find the I-device under "Additional field devices &gt; PROFINET IO" in the hardware catalog under the name that you have specified as designation in the export dialog. I-devices with the same name are set as versions of the same device in the hardware catalog. You can identify these different versions with the identifier of the version in the file name or by means of a different description. To display these versions, use the "Version" drop-down list after selection of the I-device.

Selected I-devices can be dragged into the configuration just like other devices of the hardware catalog.

GSD files are always saved together with the project, which means all information relevant for display of the device (including symbols) is also available in the saved project.

---

**See also**

[Configuring the I device](#configuring-the-i-device)

### Multiple assignment of IO controllers

#### Introduction

If several PROFINET IO interfaces with I-device functionality exist in an S7-1500 PLC, you can also assign several IO controllers to this device.

As of STEP 7 V14, the fact that more than one higher-level IO controller is available for an I-device is also visible: The link "Multiple assignment" is displayed at such devices in the network view.

Examples of PROFINET IO interfaces with I-device functionality:

- S7-1500 CPU, in particular with two PROFINET IO interfaces (for example, CPU 1518-4 PN/DP, CPU 1517-3 PN/DP support PROFINET IO (and I-device functionality) at the interfaces X1 and X2)
- CM 1542-1

The effects of a multiple assignment are described below.

#### Configuring a device with assignments to several IO controllers

The following section uses an example configuration to show the effect of the assignment of an I-device to several IO controllers.

1. Drag-and-drop several PROFINET IO controllers (for example, CPU 1518-4 PN/DP) from the hardware catalog into the network view.
2. Drag-and-drop a PROFINET IO controller which can also be configured as IO device from the hardware catalog into the network view (for example, CPU 1518-4 PN/DP). You can also insert a CM 1542-1 into this station and also configure the PROFINET interface as an IO device.
3. Select the PROFINET interface of a module.
4. In the area navigation of the Inspector window, select the "Operating mode" entry and select the "IO device" check box.
5. You now have the option of selecting the IO controller in the "Assigned IO controller" drop-down list.
6. Repeat steps 3 and 4 for additional PROFINET interfaces.

   Once you have chosen the IO controller or the PROFINET IO interface of the IO controller, the networking and the IO system between both devices are displayed in the network view.

   As soon as you assign a further PROFINET IO interface to a different IO controller, the "Multiple assignment" link is displayed in the device instead of the name of the higher-level IO controller.

   When you click this link, the selection of assigned IO controllers is displayed and you can place the focus on this device by clicking one of these IO controllers.

   ![Configuring a device with assignments to several IO controllers](images/90699687947_DV_resource.Stream@PNG-en-US.png)

The remaining settings (further parameter assignment of the IO interface, configuration of the transfer areas) are only affected by this function extension in as far as the selection of the devices or of the IO systems is facilitated by a unique ID, also in the case of CPUs with several PROFINET IO interfaces.

If you have assigned the interfaces to exactly one S7 subnet, several IO systems exist on this subnet.

If you click the subnet, the display for selecting the IO systems to be highlighted is shown.

![Configuring a device with assignments to several IO controllers](images/90699703691_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Rules for CPUs with several PROFINET interfaces (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#rules-for-cpus-with-several-profinet-interfaces-s7-1500)

### Constraints on the Use of I-Devices

#### Boundary conditions

When using I-devices, certain constraints must be taken into account in certain situations.

#### Bandwidth

The number of addresses of the configured transfer areas is reflected in the usable bandwidth of the I-device:

Bandwidth of the transfer areas + bandwidth of the lower-level IO system = total bandwidth used on the I-device.

If the address space of the transfer areas is too large, there is not enough bandwidth for the lower-level IO system to achieve fast update times.

**Tip**: Keep the address space of the transfer area as small as possible.

#### Rules for RT and IRT communication

IO systems with I-devices are also suitable for setting up real-time applications with RT communication. In the following, a hierarchical system is required, consisting of a higher-level IO controller to which an I-device is assigned (higher-level IO system). IO devices are, in turn, assigned to the I-device (lower-level IO system). The following rules apply:

Both the higher-level and the lower-level IO system support RT communication. You can use RT communication for both IO systems at the same time.

IRT communication can be combined with RT communication. However, IRT communication cannot take place in both IO systems at the same time.

Example:

- If the option "Parameter assignment for the PN interface and its ports on the higher-level IO controller" is **activated** on the I-device, the I-device can be operated on the higher-level IO controller with the RT class "IRT". IRT communication is not possible for the lower-level IO system of the I-device in this case.
- If the option "Parameter assignment for the PN interface and its ports on the higher-level IO controller" is **deactivated** on the I-device, the I-device can be operated on the higher-level IO controller with the RT class "RT". IRT communication is possible for the lower-level IO system.

If you configure the I-device on an IO system with the RT class "RT", you cannot set odd send clocks.

#### Rules for data access

- The higher-level IO controller can access transfer areas when the I-device is in RUN.
- Only the application transfer areas may be accessed in the I-device CPU:

  - Access to input-application transfer areas possible if the higher-level IO-controller is in RUN.
  - Access to output application transfer areas possible independent of the operating state of the higher-level IO controller.

#### IP address parameters and device name

Just like every other IO device, an I-device also requires IP address parameters / device name to be able to communicate via PROFINET. IP address parameters consist of three parts, the IP address itself, the subnet mask and the address of the router (gateway).

The IP address parameters / device name for an I-device can be assigned in two ways - via the project or directly on the device.

IP address/device name is set in the project:

- The IP address parameters / device name are permanently assigned during configuration (in the I-device project) in STEP 7. This is the standard method.

Set IP address/device name on the device:

- IP address parameter / device name via DCP: The IP-address parameters / device name are assigned via DCP (Discovery and Configuration Protocol). This can happen in two ways:

  - Through a setup tool such as SINEC PNI Basic or STEP 7 (via accessible devices).
  - Through the higher-level I/O controller
- IP address parameter / device name via user program: The assignment of the IP address parameters occurs in the user program of the I-device CPU (via the instruction "IP_CONFIG").

  > **Note**
  >
  > **Topology illustration**
  >
  > If the device name and the IP address parameters are adapted for an I-device directly on the device, the I-device can be displayed multiple times in the topology editor.

### Diagnostics and interrupt characteristics

#### Diagnostics and interrupt characteristics

S7 CPUs have numerous diagnostics and interrupt functions that can, for example, report errors/faults or failures of underlying IO systems. These diagnostics alarms reduce down times and simplify localization and elimination of problems.

#### Diagnostics of the I-device on the higher-level IO controller and in the I-device

The following mechanisms are available in the higher-level IO controller and the I-device CPU for diagnosing the state of the respective partner:

- Pull/plug interrupt OB (OB 83) for "Return of submodule" interrupt
- Program execution error OB (OB 85) for, for example, process image transfer errors (only S7-300/400)
- Rack failure OB (OB 86) for the failure of expansion units, IO systems or distributed I/O devices (station failure, station return)
- I/O access error OB (OB 122), optional for S7-1500
- Local troubleshooting (only S7-1500)

  > **Note**
  >
  > The diagnostics alarms of the I/O can be processed in the user program of the I-device CPU and passed on from there to the higher-level IO controller via transfer areas.

#### Operating state changes and station failures / station returns

In the following tables, you can see the effects which the operating state change or the failure of individual CPUs (I device, IO controller) have on each other.

Please note that an S7-1500 CPU calls the OB 122, if it exists, in the event of errors due to direct I/O access to the transfer areas (for example, because the other CPU goes into STOP). However, in contrast to an S7-300/400 CPU, the CPU does not go into STOP if the OB 122 does not exist. With an S7-1500 CPU, local troubleshooting within the block in which the error occurred is also possible. This situation is indicated in the table with the abbreviated wording "Call of OB 122".

#### Events

| Initial status | Event | I device response | Response of higher-level controller |
| --- | --- | --- | --- |
| Both CPUs are in RUN operating state (higher-level IO controller and I-device). | The I device CPU changes to STOP. | / | **S7-300/400/1500:** Error code in RET_VAL at updating of the process image with the instruction UPDAT_PI or UPDAT_PO.  OB 122 is called in the case of direct access to the transfer areas to the I-device (optional for S7-1500).    **S7-300/400**: With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer to the I-device by the system. |
| I-device CPU is in STOP mode, higher-level IO controller is in RUN mode. | The I device CPU is starting up. | **S7-300/400/1500:** Call of OB 100 (startup).   Call of OB 83 for input transfer areas to the higher-level IO controller.  Until OB 83 is called, access errors occur in the event of direct access to the input transfer areas to the higher-level IO controller: Call of OB 122.   **S7-300/400:** With a configured OB85 call if I/O access error occurs, OB 85 continues to be called at a process image transfer to the higher-level IO controller by the system until OB 83 is called. | **S7-300/400/1500:** Call of OB 83: For all transfer areas to the I-device.  Until OB 83 is called, OB 122 continues to be called in the event of direct access to the transfer areas to the I-device.   **S7-300/400:** With a configured OB85 call if I/O access error occurs, OB 85 continues to be called at a process image transfer to the I-device by the system until OB 83 is called. |
| Both CPUs are in RUN mode (higher-level IO controller and I-device). | The higher-level IO controller changes to STOP | **S7-300/400/1500:** Error code in RET_VAL at updating of the process image with the instruction UPDAT_PI or UPDAT_PO.  OB 122 is called in the event of direct access to the input transfer areas to the higher-level IO controller.  Note: Output transfer areas can still be accessed.   **S7-300/400**: With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the input transfer areas to the higher-level IO controller by the system. | / |
| Higher-level IO controller is in STOP mode, I-device CPU is in RUN mode. | The higher-level IO controller starts up. | **S7-300/400/1500**: Call of OB 83 for input transfer areas to the higher-level IO controller.  Until OB 83 is called, OB 122 continues to be called in the event of direct access to the input transfer areas to the higher-level IO controller.    **S7-300/400**: With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the input transfer areas to the higher-level IO controller by the system. | Call of OB 100 (startup). |
| Both CPUs are in RUN (higher-level IO controller and I-device). | Station failure I device, for example, through bus disruption | **S7-300/400/1500**: If the I device continues to run without a bus connection: Call of OB86 (station failure).  Error code in RET_VAL at updating of the process image with the instruction UPDAT_PI or UPDAT_PO.  OB 122 is called in the event of direct access to the transfer areas to the higher-level IO controller    **S7-300/400**: With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the transfer areas to the higher-level IO controller by the system. | **S7-300/400/1500**: Call of OB86 (station failure).  Error code in RET_VAL at updating of the process image with the instruction UPDAT_PI or UPDAT_PO.  OB 122 is called in the case of direct access to the transfer areas to the I-device.   **S7-300/400**: With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the transfer areas to the I-device by the system. |
| Both CPUs are in RUN (higher-level IO controller and I-device).   The communication connection between the IO-controller and I-device is disrupted (bus disruption). | The bus connection between the IO-controller and I device is reestablished and the I device is recorded in the usage data traffic again. | **S7-300/400/1500**: Please note the information under this table about the special considerations when the I-device is powered up.  Call of OB 86 (station return).   Call of OB 83 for input transfer areas to the higher-level IO controller.  Until OB 83 is called, OB 122 continues to be called in the event of direct access to the input transfer areas to the higher-level IO controller.    **S7-300/400:** With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the input transfer areas to the higher-level IO controller by the system. | **S7-300/400/1500**: Call of OB86 (station return)   Until OB 86 is called, OB 122 continues to be called in the event of direct access to the transfer areas to the I-device.   **S7-300/400:** With a configured OB85 call if I/O access error occurs, OB 85 is called at a process image transfer of the transfer areas to the I-device by the system. |
|  |  |  |  |

> **Note**
>
> **Special feature when starting up the I device**
>
> In contrast to the station return alarm from IO devices in the IO controller, which is covered by calling OB86, the station return alarm of a higher-level IO controller in the I device is divided into 2 parts:
>
> 1. Call of OB 86: The initial values for the outputs of the I device are set. The input values, however, are not yet valid; they will first be valid when opening the OB86 in the higher-level IO controller.
> 2. Call of OB 83 for each input transfer area. The validity of an input transfer area is shown with this call. I-device startup is not complete until OB 83 is called for the input transfer areas. This step can be delayed or not occur at all in the following situations:
>
>    - Higher level IO controller is in STOP: OB 83 is not called until the STOP → RUN transition of the higher-level IO controller.
>    - The IRT communication is faulty, for example, because the sync master has failed due to topology errors, etc.: The OB 83 is not started until the IRT communication has been established again.

---

**See also**

[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)
  
[Insert/remove module interrupt organization block (OB 83) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#insertremove-module-interrupt-organization-block-ob-83-s7-300-s7-400)
  
[Pull/plug interrupt OB (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#pullplug-interrupt-ob-s7-1500)
  
[Rack failure organization block (OB 86) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#rack-failure-organization-block-ob-86-s7-300-s7-400)
  
[Rack error OB (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#rack-error-ob-s7-1500)
  
[I/O access error organization block (OB 122) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#io-access-error-organization-block-ob-122-s7-300-s7-400)
  
[I/O access error OB (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#io-access-error-ob-s7-1500)
  
[Priority class error organization block (OB 85) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#priority-class-error-organization-block-ob-85-s7-300-s7-400)

### Online diagnostics for I devices

I device online diagnostics is basically similar to online diagnostics of "normal" IO devices.

#### Displaying diagnostic status by going online

You will receive a selection of the following information depending on which device you selected when you went online:

- If you have selected a higher-level IO controller:

  The diagnostics status of the I device is shown in the project navigation below the IO controller in the "Distributed I/O" folder. No diagnostics status will be shown in the project navigation for the I device itself.
- You have selected the I device that this IO controller is assigned to.

  The diagnostics status of the I device is shown in project navigation. No diagnostics status of the I device is shown in the project navigation below the IO controller in the "Distributed I/O" folder.

#### Online and diagnostics view

You will receive a selection of the following information depending on which device you selected in the online and diagnostics view:

- You have selected a higher-level IO controller and are connected online with this device:

  The online and diagnostic view displays the I device diagnostics data from the higher-level IO controller. The display corresponds to the display of a "normal" IO controller.
- You have selected the I-device that this IO controller is assigned to and are connected online with this device.

  The online and diagnostics view displays I device diagnostics data from the local view, that is, the view of the I device. The display corresponds to the display of a "normal" IO device.

#### Display in the list of accessible devices

In the list of accessible devices the I device will be displayed as a "normal" CPU.

### Disabling I-device in the user program of the I-device CPU

When a PROFINET interface of a CPU was configured as an I-device in STEP 7, the I-device function is active after a status transition of the CPU from STOP &gt; RUN. If no higher-level IO controller can be reached in this case, the I-device CPU signals an error using its ERROR LED.

As of firmware version 2.9 of an S7-1500/ET 200SP/ET 200pro CPU, you can locally disable or enable the I-device function in the user program of the I-device CPU. You use the "D_ACT_DP" instruction for this. After disabling the function, the I-device CPU no longer signals an error using its ERROR LED.

You can enable/disable the function with the user program at the CPU-internal PROFINET interfaces and for S7-1500 CM 1542-1 as of firmware version V3.0.

#### Application options

From a manufacturer's point of view, there are numerous device options possible in series production of machines. However, each delivered machine includes only one combination of selected options. All possible machine options can be configured as I-devices by the manufacturer to create and maintain a common user program having all possible options.

A higher-level IO controller used for line control, for example, is not necessary in every machine. In this case, the user program disables the I-device function in the I-device CPU with the instruction "D_ACT_DP", for example, during startup.

Two production lines are shown schematically in the figure below. The same user program runs in both CPUs with I-device configuration. The S7-1500 CPU as I-device in line 1 is controlled by a higher-level IO controller; the S7-1500 CPU in line 2 with disabled I-device function does not have a higher-level IO controller.

![Application options](images/136377045131_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Higher-level IO controller |
| ② | ... controls I-device CPU S7-1500 in the line |
| ③ | I-device function is enabled in the user program of this CPU |
| ④ | I-device function is disabled in the user program of this CPU |
| ⑤ | IO devices |

Another application is, for example, the coordination of transport vehicles.

The vehicles are temporarily in the area of a station where they are controlled or monitored by a higher-level IO controller. When the vehicles travel outside the station, they act without a higher-level IO controller. Because operation outside the station is permitted, a missing IO controller must not result in an error message.

#### Requirements

- You operate the CPU as an I-device on one or multiple IO controllers or you have configured the CPU as I-device ("IO device" check box in the "Operating mode" area of the corresponding PROFINET interface is selected).
- You use the "D_ACT_DP" instruction to disable the I-device function. You can use the same instruction to enable the I-device function again.

#### Disabling the I-device function at a PROFINET interface

> **Note**
>
> Only disable the I-device function in the I-device CPU when the I-device is not operated on a higher-level IO controller.

You disable the I-device function with the instruction "D_ACT_DP":

- Parameter LADDR: symbolic name or hardware ID of the system constant of the type "Hw_Device" of the respective PROFINET interface
- Parameter MODE = 2

**Result:** The CPU is no longer available for the data exchange with a higher-level IO controller. The higher-level IO controller can be reached again when the I-device function was enabled in the user program of the I-device CPU.

When an I-device that has been active on an IO controller disables itself, all application relations (ARs) that were set up between the I-device and the IO controller in the network are terminated, which means the connection no longer exists:

- An IO device failure is signaled at the IO controller end.
- In the diagnostics buffer of the I-device CPU, "IO device user disable" is displayed with information on the associated PROFINET interface or the name of the IO controller.

#### Enabling the I-device function at a PROFINET interface

You also use the instruction "D_ACT_DP" to enable an inactive I-device function:

- Parameter LADDR: symbolic name or hardware ID of the system constant of the type "Hw_Device" of the respective PROFINET interface
- Parameter MODE = 1

**Result:** After enabling, the I-device can exchange data with a higher-level IO controller.

If at least one IO controller is missing or the connection does not exist, "Hardware component removed or missing" is entered in the diagnostics buffer of the I-device CPU.

> **Note**
>
> **Temporary access errors**
>
> Enabling the I-device function in the user program can result in temporary access errors "I/O data failure in hardware component", for example, because access to the I/O data of the I-device is already possible even though the data has not been declared as valid by the IO controller yet.
>
> These messages are incoming and outgoing error events that can be neglected.

---

**See also**

[D_ACT_DP: Activate/deactivate DP slaves (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#d_act_dp-activatedeactivate-dp-slaves-s7-1200-s7-1500)

## Changing IO devices during operation

This section contains information on the following topics:

- [Docking station - changing IO devices during operation (S7-300, S7-400, S7-1500)](#docking-station---changing-io-devices-during-operation-s7-300-s7-400-s7-1500)
- [Configuring docking units in a docking system (S7-300, S7-400, S7-1500)](#configuring-docking-units-in-a-docking-system-s7-300-s7-400-s7-1500)
- [Interconnecting ports by changing partner ports](#interconnecting-ports-by-changing-partner-ports)

### Docking station - changing IO devices during operation (S7-300, S7-400, S7-1500)

#### Using changing IO devices during operation ("changing partner ports") in a docking station

The following Figure shows an automation cell with a docking system and several docking units.

![Changing IO devices (partner ports) in a docking station](images/22898606987_DV_resource.Stream@PNG-en-US.png)

Changing IO devices (partner ports) in a docking station

#### Applicative conditions

The following points should be observed when realizing a docking system with changing IO devices during operation:

- The IO devices of all docking units must be deactivated as default in the configuration.
- Only one docking unit may be active at any given time, in other words only the IO devices of one docking unit can be activated. All IO devices of other docking units must be deactivated or become deactivated before the IO devices of a docking unit can be activated. This is done with the instruction "D_ACT_DP".
- A physical connection to this docking unit and its IO devices must be created in order to activate a docking unit. The IO devices are then switched on (power on). All the IO devices of this docking unit must at the same time be activated in the user program with "D_ACT_DP".
- After the message "IO device activated" you can access the IO device by using the command "Direct I/O access".
- Call the instruction "D_ACT_DP" to activate and deactivate the IO device as close as possible to the start of the OB 1 cycle.

#### Area of application for changing IO devices during operation

You can use the PROFINET functionality "Changing IO devices during operation" ("changing partner ports"), e.g. for tool change for robots. Typical tools are, for example:

- welding guns and
- holding tools for production parts.

  > **Note**
  >
  > **Number of changing IO devices during operation ("changing partner ports") - number of docking units**
  >
  > If you wish to achieve the shortest possible tool-change times, you must observe the following points that are dependent on the CPU or the CP that is being used:
  >
  > - Only those IO devices that have been configured with the PROFINET function "Prioritized startup" can run in an optimized fashion. The number of IO devices with configuration for this PROFINET function is restricted.
  > - Only a specific number of IO devices can be enabled at the same time (number depends on the available resources for instruction "D_ACT_DP"). A docking unit should therefore not include more than this number of IO devices. If more IO devices are operated in a docking unit, the IO devices must be enabled one after the other, which takes correspondingly longer.
  >
  > Example: An S7 CPU 319-3 PN/DP can operate a maximum of 32 IO devices with prioritized startup and can simultaneously activate 8 IO devices with the instruction "D_ACT_DP".
  >
  > Therefore, for a scheduled optimum use, a docking unit should include no more than 8 IO devices and no more than 32 IO devices should be used in all the changing docking units.

#### Restriction in the interconnection

The interconnection with a partner port is not possible in the following cases:

- The partner port does not have a suitable type of cable. In this case, a media convertor from the catalog must be inserted.
- The partner port is locked (disabled).
- The two ports that are to be interconnected belong to the same interface (it is possible only to interconnect the ports from different interfaces in a station).
- You are trying to create a ring connection with a module that is not redundant-capable.
- The two ports that are to be interconnected belong to different Ethernet subnets.
- The port of a PROFINET interface of an IO controller cannot be directly configured with the function "Changing IO devices during operation" ("changing partner port").

---

**See also**

[D_ACT_DP: Enable/disable DP slaves (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)

### Configuring docking units in a docking system (S7-300, S7-400, S7-1500)

#### Configuring docking units in a docking system

To configure more docking units in a docking system, follow these steps:

1. Configure your hardware configuration as usual; first, consider the IO devices which correspond to the changing partners to be normal IO devices.
2. In the inspector window, open the properties of the ports on which you would like to operate the changing IO devices (changing partner ports).
3. Under "General &gt; PROFINET interface &gt; Advanced settings &gt; RJ45 100 Mbit Port [Xn Pm] &gt; Port interconnection", select the check box "Alternative partner".
4. Insert the alternative partner in the table, as described in the "Interconnecting ports" chapter.

---

**See also**

[Interconnecting ports by changing partner ports](#interconnecting-ports-by-changing-partner-ports)
  
[Optimizing startup time](#optimizing-startup-time)

### Interconnecting ports by changing partner ports

#### Requirement

- All devices involved support topology configuration
- The IO controller, the changing IO devices (docking unit) and the switch (docking system) to which the changing IO devices are to be operated, must support this feature.
- The docking unit must be connected with a switch that supports the PROFINET function "prioritized startup" (e.g., from the SCALANCE X200IRT family).

#### Example

- IO controller: CPU 416-3 PN/DP, CPU 1516‑3 PN/DP
- Docking system: Scalance X-200IRT
- Docking units (changing IO devices): for example, 2 x ET 200pro (IM 154-4)

#### Procedure

In the description of the procedure, it is assumed that the configuration matches that of the above-described example. To interconnect ports, follow these steps:

1. Connect all PROFINET interfaces of the devices to each other in the network view.
2. In the network view or device view, select the docking system (Scalance X200 IRT) whose port you want to interconnect.
3. Open the device properties in the Inspector window.
4. Under "Properties &gt; PROFINET interface &gt; Advanced settings &gt; RJ45 100-megabit port [Xn Pm] &gt; Port interconnection" choose the partner port for the CPU (IO controller) from the "Partner port" drop-down list.

   The ports of the CPU and the docking system (Scalance) are interconnected.
5. The docking system is still selected: For any other unconnected port, now select the partner ports for the IO devices:

   - Select the "Alternative partner" check box.

     A table for the partner port is displayed.
   - Within the table, click the line &lt;Add alternative partner...&gt; to open a drop-down list.

     The drop-down list shows all devices with their unconnected ports for selection.
   - Select the port of the first docking unit.
   - Click the next line in the table and select another alternative partner port.
   - Repeat the steps outlined above until all required partner ports are recorded in the table.

> **Note**
>
> **Use of a CP 1243-1 (WAN-CP)**
>
> When a CPU S7-1200 with CP 1243-1 is used, the procedure is the same as above, except the Ethernet interface of the CP is used instead of the PROFINET interface of the IO controller.

> **Note**
>
> **CAx export of a PROFINET configuration for tool changer projects**
>
> When you have a PROFINET configuration in which the "Alternative partner" check box selected, you must observe the following when exporting CAx files: The setting "Alternative partner" is not supported during the export. This means that this setting or the topological connection is missing in the subsequent reimport.

#### Interconnecting several IO devices with changing IO devices during operation

Configure IO devices on a docking unit which are interconnected in line with IO devices changing during operation ("Alternative partner") with the port of the changing IO device as usual; this means the IO device interconnected in line then has no changing partner port.

#### Deleting the partner port

To remove the interconnection of the partner port that changes during operation, follow these steps:

1. In the table of alternative partners, click the row that contains the alternative partner port that is to be deleted and open the drop-down list for the partner port (black triangle).
2. Select "Any partner" from the list.

   The alternative partner port is removed from the table.

---

**See also**

[Enabling device replacement without exchangeable medium](Configuring%20devices%20and%20networks.md#enabling-device-replacement-without-exchangeable-medium)
  
[What is prioritized startup?](#what-is-prioritized-startup)

## Optimizing startup time

This section contains information on the following topics:

- [What is prioritized startup?](#what-is-prioritized-startup)
- [Setting prioritized startup](#setting-prioritized-startup)
- [Optimizing port settings on the IO device and IO controller](#optimizing-port-settings-on-the-io-device-and-io-controller)

### What is prioritized startup?

#### Definition

Prioritized startup, also known as "fast startup", describes the PROFINET functionality for accelerating the startup of IO devices in a PROFINET IO system with RT and IRT communication. It reduces the time that the correspondingly configured IO devices require in order to return to cyclic user data exchange in the following cases:

- After the supply voltage has returned
- After a station has returned
- After IO devices have been activated

#### Benefits

The PROFINET functionality "prioritized startup" enables PROFINET IO applications in which machine parts or tools and their IO devices have been permanently replaced. Waiting times of several seconds between the scheduled processes of the restart are reduced to a minimum by this optimization. This accelerates the production process with removable IO devices, e.g. in tool-changer applications and enables a greater throughput in production.

The PROFINET functionality "prioritized startup" also offers a considerable increase in performance for applications where a quick startup time of the IO devices after "power on" or after station failure / station return is required or when activating IO devices.

#### Properties

You can realize the following properties with the PROFINET function "Prioritized startup":

- Communication readiness of the IO devices (distributed I/O) up to minimum 500 ms.
- You can use the prioritized startup for IO devices (distributed I/O) both with RT as well as with IRT communication.

#### Startup times

The length of the startup time of an IO device (distributed I/O) with the PROFINET function "Prioritized startup" is dependent on the following points:

- IO devices used (distributed I/O)
- IO structure of the IO devices (distributed I/O)
- Used modules of the IO devices (distributed I/O)
- Used IO controller
- Used switch
- Port setting
- Cabling
- Configured RT class of the IO device

> **Note**
>
> **Prioritized startup after a startup for the first time**
>
> A prioritized startup of the IO device is always available to you after the first configuration of this IO device in the very first startup of the PROFINET IO system. Even in the case of spare parts or a reset to factory settings, the first startup is a standard startup for the respective configured IO devices.

> **Note**
>
> In the following situations, despite prioritized startup, there may be startup times of up to 8 s:
>
> - An IO/device is disconnected and reconnected within 8 seconds.
> - On a docking point, you can dock multiple physical IO devices as an IO device with a certain device name and a certain IP configuration (for example, docking point for automatic transport system).

If you wish to achieve a shortest possible startup time of 500 ms, you must perform the following measures:

- Port setting on the IO device
- Wiring dependent on the interconnected PROFINET device
- Measures in the user program

### Setting prioritized startup

#### Requirement

You can enable the PROFINET function "Prioritized startup" for the IO devices (distributed I/O) only in the following cases:

- The IO controller used can prioritize selected IO devices during startup.
- The IO device used supports prioritization.

> **Note**
>
> **Prioritized startup**
>
> In the case of an accelerated startup (prioritized startup), you must observe special conditions when setting up the PROFINET interface and when wiring if you wish to achieve the shortest possible startup times.

#### Procedure

1. Select the IO device in the network view or device view for which you wish to accelerate startup.
2. Open the IO device properties in the inspector window.
3. Select "PROFINET interface &gt; Advanced options &gt; Interface options".
4. Select the "Enable prioritized startup" check box.
5. Download the configuration to the IO controller.

Note:

For devices whose DP mode can be selected, the previously described check box can be found under "PROFINET interface &gt; Operating mode". The CP 1616 for PC stations is one example of this type of device.

> **Note**
>
> **Number of IO devices (distributed I/O) with prioritized startup**
>
> You can only start up a set maximum number of IO devices with PROFINET functionality "Prioritized startup" within one IO system. This maximum number depends on the IO controller used.

---

**See also**

[Optimizing port settings on the IO device and IO controller](#optimizing-port-settings-on-the-io-device-and-io-controller)

### Optimizing port settings on the IO device and IO controller

#### Optimizing port settings on the IO device and IO controller

The transfer medium and the duplex option are checked during startup of the IO device in the case of control unit cabling.

These checks require time, but with specific presets of these options you can save time. Make certain that the settings made correspond to the actual conditions (using the correct wiring).

#### Synchronizing the properties of local port and partner port

To synchronize the properties for the local port and partner port, follow these steps:

1. First, select the relevant local port and then the partner port and perform the following steps for both ports.
2. Synchronize the "Transmission medium/duplex" setting of the respective ports in the properties under "Port options". Use the setting "TP 100 Mbps full duplex".
3. Under "Port options", clear the check box "Enable autonegotiation" for both ports.

---

**See also**

[Wiring rules for disabled autonegotiation](Configuring%20devices%20and%20networks.md#wiring-rules-for-disabled-autonegotiation)

## Configuring media redundancy

This section contains information on the following topics:

- [What you should know about media redundancy](#what-you-should-know-about-media-redundancy)
- [Media Redundancy Protocol (MRP)](#media-redundancy-protocol-mrp)
- [Configuring media redundancy](#configuring-media-redundancy-1)
- [Media Redundancy with Planned Duplication of frames (MRPD) (S7-1500, S7-1500T)](#media-redundancy-with-planned-duplication-of-frames-mrpd-s7-1500-s7-1500t)
- [Managing MRP domains](#managing-mrp-domains)
- [Configuring multiple rings](#configuring-multiple-rings)
- [MRP interconnection (S7-1500, S7-1500T)](#mrp-interconnection-s7-1500-s7-1500t)

### What you should know about media redundancy

#### Media redundancy options

To increase the network availability of an industrial Ethernet network with optical or electrical line topology, the following options are available:

- Meshing networks
- Parallel switching of transmission modes
- Consolidation of a line topology to a ring topology

#### Media redundancy in ring topologies

Devices in ring topologies can be the external switches and/or integrated switches of communication modules.

To set up a ring topology with media redundancy you must join both free ends of a line-shaped network topology to one device. Consolidation of a line topology to a ring takes place over 2 ports (ring ports) in a device in the ring. This device is the redundancy manager. All other devices in the ring are the redundancy clients.

The following figure shows the ring-shaped interconnection of the IO devices:

![Media redundancy in ring topologies](images/101236793995_DV_resource.Stream@PNG-en-US.png)

The two ring ports in a device are the ports which create the connection to both of its neighboring devices in a ring topology. The selection and set up of the ring ports takes place during configuration of the respective device.

Download the configuration in the individual devices before physically connecting the ring.

#### Functions of media redundancy in a ring topology

If a part of the ring is disconnected, then the data paths between the individual devices is automatically reconfigured. After the reconfiguration the devices are once again accessible in the newly created topology.

In the redundancy manager, 2 ring ports will be separated from each other during interruption-free network operation, so that no data frames circulate. The ring topology is a line when viewed from the standpoint of data transfer. The redundancy manager monitors the ring topology. To do so, it sends a test frame not only from ring port 1 but also from ring port 2. The test frames pass through the ring in both directions until they arrive at the other ring port on the redundancy manager.

An interruption in the ring can occur from connection failure between two devices or device failure in the ring.

If the redundancy manager's test telegram does not reach the other ring port because of interruption in the ring, the redundancy manager connects via both ports. With this alternate route a functioning connection is again created among all remaining devices in a line-shaped topology.

As soon as the interruption is eliminated, the original transmission routes are used again, the two ring ports on the redundancy manager are separated from each other, and the redundancy clients are notified of the change. Data traffic now runs again as before the interruption.

#### Media redundancy processes

In STEP 7 you can use the media redundancy process MRP (Media Redundancy Protocol) for ring topologies; up to 50 devices per ring can be included.

In addition, the real-time capable media redundancy process MRPD (Media Redundancy with Planned Duplication of frames) is also available.

#### Reconfiguration time

The time between ring interruption and re-establishment of a functional line topology (with resetting up of the address tables) is called the reconfiguration time. It typically amounts to less than 200 ms.

If the watchdog time of an IO device is shorter than the reconfiguration time of the ring, there is a danger that communication with the IO device will be interrupted (station failure).

Recommendation: When configuring the watchdog time of an IO device, select a time longer than 200 ms (in the properties of the IO device: PROFINET interface &gt; Advanced options &gt; Real time settings).

---

**See also**

[Media Redundancy Protocol (MRP)](#media-redundancy-protocol-mrp)
  
[Configuring media redundancy](#configuring-media-redundancy-1) 
  
[Media Redundancy with Planned Duplication of frames (MRPD) (S7-1500, S7-1500T)](#media-redundancy-with-planned-duplication-of-frames-mrpd-s7-1500-s7-1500t)
  
[Managing MRP domains](#managing-mrp-domains)

### Media Redundancy Protocol (MRP)

#### Media Redundancy Protocol (MRP)

The "MRP" process works in conformity with the Media Redundancy Protocol (MRP) that is specified in the standard IEC 62439-2.

> **Note**
>
> **Devices with "Media redundancy" functionality**
>
> As of V17, CPUs of the S7-1200 (1215/1217) family with firmware version V4.5 or higher also have the "Media redundancy" functionality.
>
> The S7-1215/1217 CPUs can be used as Manager and as Client in a ring with MRP.
>
> The same rules and requirements apply as for the devices of the S7-1500 family.

#### Requirements

- All devices in the ring support MRP.
- You have complied with the rules for topology set out below. STEP 7 monitors compliance with the rules in compilation and outputs corresponding messages.

#### Topology

The following schematic shows a possible topology for devices in a ring with MRP. The devices inside the shaded oval are in the redundancy domain.

Example of a ring topology with the MRP media redundancy protocol:

![Topology](images/86335159819_DV_resource.Stream@PNG-de-DE.png)

The following rules apply to a ring topology with media redundancy using MRP:

- All devices must be connected to each other via their ring ports.
- All devices in the ring belong to the same redundancy domain.
- A device within the ring is the redundancy manager.

  - One device only has the role of "Manager". No other device may have the role of "Manager". Or
  - Several devices in the ring have the role of "Manager (auto)". The devices with the role of "Manager (auto)" then negotiate between themselves which device is to take on the role of redundancy manager. In this case, no device may have the role of "Manager".
- All other devices in the ring are redundancy clients.
- You can connect up to 50 devices in a ring.

Non MRP-compliant devices can, for example, be connected to the ring via a SCALANCE X switch or via a PC with a CP 1616.

#### Rules for loading the devices of an MRP domain.

When devices of an MRP domain are loaded, circulating frames and thus failure of the network can occur if there is an invalid MRP configuration.

Example: You change the MRP roles of several devices and consecutively load the configuration into the devices involved. Configurations can arise that contradict the roles named above, for example devices with the "Manager" and "Manager (auto)" role can exist simultaneously in the ring.

In order to ensure that an invalid MRP configuration does not result in the failure of the network, dissolve the ring before loading. Follow these steps:

1. Dissolve the ring.
2. Load the error-free and consistent MRP configuration from your project into all the devices involved and ensure that the devices are in data exchange mode (i.e. the application relations (ARs) are set up).
3. Close the ring.

#### Constraints

**MRP and RT**

RT operation is possible with the use of MRP.

> **Note**
>
> The RT communication is disrupted (station failure) if the reconfiguration time of the ring is greater than the selected response monitoring time of the IO device. This is why you should select a response monitoring time of the IO devices that is sufficiently large.

**MRP and IRT**

IRT mode is not possible together with MRP.

If you want to use media redundancy together with IRT in a ring, only use devices that support MRPD.

**MRP and TCP/IP (Open User Communication via, for example, TSEND, Web access via HTTP, etc.)**

The TCP/IP communication with MRP is possible, because lost data packages are resent, if applicable.

**MRP and prioritized startup**

If you configure MRP in a ring, you cannot use the "prioritized startup" function in PROFINET applications on the devices involved.

If you want to use the "Prioritized startup" function for a device, the device may not be a participant in the ring.

---

**See also**

[Configuring media redundancy](#configuring-media-redundancy-1) 
  
[What you should know about media redundancy](#what-you-should-know-about-media-redundancy)
  
[Configuring multiple rings](#configuring-multiple-rings)

### Configuring media redundancy

#### Configuring MRP

Proceed as follows to create a PROFINET IO configuration with MRP in STEP 7:

1. Generate a ring via the port interconnections in the topology view.
2. First interconnect the devices to a line topology. Connect the unassigned port of the last device in the line with the unassigned port of the first device.  
   The following example shows one CPU 1516‑3 PN/DP and two interface modules IM 155‑6 PN HF that are interconnected in a ring in the topology view of STEP 7.

   ![Configuring MRP](images/90699884683_DV_resource.Stream@PNG-de-DE.png)

   ![Configuring MRP](images/90699884683_DV_resource.Stream@PNG-de-DE.png)
3. Select the PROFINET IO system in the network view.
4. In the Inspector window, navigate to "Properties" &gt; "General" &gt; "PROFINET" &gt; "MRP domains" in the "Ring interconnection" field.  
   This field shows you all the topological rings in the IO system with the associated MRP domains.
5. Select the ring generated above in the "Ring interconnection" field.  
   The table below it shows all PROFINET devices in the ring.
6. Set the media redundancy role for the PROFINET devices in the MRP role column.

   If you interconnect the devices, the MRP roles are initially set to "Not device in the ring" for all devices. This configuration is not consistent.

   You have the following options: You can manually assign MRP roles according to the rules of MRP configurations (see setting options "Media redundancy"). You can have the MRP roles assigned automatically by STEP 7, see next paragraph.

   ![Configuring MRP](images/90699892619_DV_resource.Stream@PNG-en-US.png)

   ![Configuring MRP](images/90699892619_DV_resource.Stream@PNG-en-US.png)

**Note**

**Devices with "Media redundancy" functionality**

As of V17, CPUs of the S7-1200 (1215/1217) family with firmware version V4.5 or higher also have the "Media redundancy" functionality.

The S7-1215/1217 CPUs can be used as Manager and as Client in a ring with MRP.

The same rules and requirements apply as for the devices of the S7-1500 family.

#### Automatic MRP configuration

You can also have the media redundancy roles assigned automatically for your PROFINET devices in the ring.

To have the media redundancy roles assigned automatically, click the "Configure MRP automatically" button. STEP 7 automatically assigns the media redundancy role for each device in the ring. After the automatic MRP configuration, you can make modifications to the media redundancy roles in the "MRP role" column.

#### "Media redundancy" setting options

**Media redundancy role**

Depending on the device used, the roles "Manager", "Manager (Auto)", "Client" and "Not device in the ring" are available.

Rules:

- A ring must have precisely one device with the role "Manager". No additional devices with the role "Manager" or "Manager (Auto)" are permissible. All the other devices may only have the "Client" role.
- If a ring has no device with the "Manager" role, the ring must at least have a device with the role "Manager (Auto)". Any number of devices with the "Client" role may exist.

**Ring port 1 / Ring port 2**

Select one at a time those ports you want to configure as ring port 1 or ring port 2. The drop-down list box shows the selection of possible ports for each device type. If the ports are set at the factory, then the fields are unavailable.

If you use single-stage commissioning (only Siemens devices with automatically assigned MRP roles in the ring after clicking "Configure MPR automatically"), use the ring ports preset in STEP 7.

#### Diagnostic interrupts

If diagnostic interrupts to the MRP state are to be output in the local CPU, select the "Diagnostic interrupts" check box. The following diagnostic interrupts can be configured:

- Wiring or port error

  Diagnostic interrupts will be generated for the following errors in the ring ports:

  - A neighbor of the ring port does not support MRP.
  - A ring port is connected to a non-ring port
  - A ring port is connected to the ring port of a different MRP domain
- Interruption / return (redundancy manager only)

  The redundancy manager generates diagnostic interrupts when the ring is interrupted and when the original configuration returns. If both of these interrupts occur within 0.2 seconds, this indicates an interruption of the ring.

You can respond to these events in the user program by programming the appropriate response in the diagnostic error interrupt OB (OB 82).

#### Tip: Delete the unneeded MRP domains

If you want to delete unneeded MRP domains, for example, because they no longer contain any devices, select the PROFINET IO system and then select the "MRP domains" area:

1. Navigate to the first table. This is the table in which you select the default domain.
2. Select the row with the MRP domain to delete and press the &lt;Del&gt; key.

You can delete any MRP domain except the default domain.

---

**See also**

[Configuring multiple rings](#configuring-multiple-rings)
  
[Media Redundancy Protocol (MRP)](#media-redundancy-protocol-mrp)
  
[What you should know about media redundancy](#what-you-should-know-about-media-redundancy)
  
[Managing MRP domains](#managing-mrp-domains)

### Media Redundancy with Planned Duplication of frames (MRPD) (S7-1500, S7-1500T)

#### MRP extension "Media Redundancy with Planned Duplication of frames" (MRPD)

The MRP extension "Media Redundancy with Planned Duplication of frames" (MRPD) provides the advantage that, in the case of a failure of a device or a line in the ring, all other devices continue to be supplied with IO data without interruption and with short update times.

MRPD is based on IRT and MRP. To realize media redundancy with short update times, the PROFINET devices participating in the ring send their data in both directions. The devices receive this data at both ring ports so that there is no reconfiguration time.

#### Requirements for media redundancy with MRPD

- All the devices of the ring must support MRPD, for example interface module IM 155‑6 PN HS as of firmware version 4.0, SCALANCE X300 as of V4.0. (Terminal) devices at the switch that cyclically exchange IRT data with a ring component must also support MRPD.

  Whether or not a device supports MRPD can be seen in the infotext for the device in the STEP 7 hardware catalog (Devices &amp; networks).
- You have configured MRP for all the devices of the ring. You have assigned the MRP role "Not device in the ring" to devices that are not located in the ring.
- You have configured IRT for all the involved components.

#### Configuring MRPD

You do not have to explicitly activate MRPD in STEP 7. The function is available automatically as soon as all the requirements for MRPD are fulfilled.

#### Redundancy levels of IO devices with MRPD

The redundancy level of an IO device specifies how strongly the real-time communication is influenced in the case of a power interruption between an IO device and its IO controller.

- Full redundancy: No influence, because the IO controller and IO device are located in the same ring.
- Partial redundancy:

  - If the interruption takes place on a non-redundant part (line) between the IO device and IO controller, real-time communication is influenced.
  - If the interruption takes place on a redundant part (ring), real-time communication is not influenced.
- No redundancy: No redundant path between the IO device and its IO controller, communication is always influenced.

The figure below shows the redundancy levels of the IO devices for an example configuration with MRPD. The three IO devices in the ring and the switch have the redundancy level "Full redundancy". Device 4 has the redundancy level "Partial redundancy", because the connection between the switch and the IO device is not redundant.

![Redundancy levels of IO devices with MRPD](images/89155840139_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | IO controller in the ring |
| ② | IO device in the ring with redundancy level "Full redundancy" |
| ③ | Switch in the ring with redundancy level "Full redundancy" |
| ④ | IO device with spur line connected to the ring with "Partial redundancy" redundancy level |

The redundancy levels are displayed in addition to other properties of the Sync domain in STEP 7:

"Domain management &gt; Sync domains &gt;... &gt; Devices".

#### Application example: Structure of a ring topology based on "MRPD"

Use the following link to download an application example for the structure of a ring topology based on MRPD:

[https://support.industry.siemens.com/cs/ww/en/view/109744035](http://support.automation.siemens.com/WW/view/en/109744035)

---

**See also**

[What you should know about media redundancy](#what-you-should-know-about-media-redundancy)

### Managing MRP domains

You can monitor and adjust the media redundancy settings centrally.

#### Requirements

- The components involved must support the media redundancy protocol (MRP).
- The devices are configured and topologically interconnected.

#### Procedure

To open the MRP domain, follow these steps:

1. Select any PROFINET interface, and select the "Advanced options &gt; Media redundancy" area in the inspector window.
2. Click the "Domain settings" button.

or

1. Select the subnet or the IO system.
2. Navigate to the "PROFINET &gt; Domain management &gt; MRP domains" area in the inspector window.

Here, you can specify centrally which MRP domain is to be the default domain. You can change the names of all domains and check redundancy roles and ring ports.

For each MRP domain, you receive an overview of how many PROFINET interfaces are interconnected in the ring, how many PROFINET interfaces are located outside the ring, and the number of redundancy managers and redundancy clients.

You can have the devices in the ring, including device name, associated MRP domain, media redundancy role, and utilized ring ports, displayed in groups:

- MRP domains

  The list shows you the existing MRP domains of the selected IO system.
- &lt;Name of MRP domain&gt;

  The list shows you the number of PROFINET interfaces and devices with the respective redundancy roles for the selected MRP domain.
- Devices

  The list shows you all configured devices of the selected IO system.

---

**See also**

[What you should know about media redundancy](#what-you-should-know-about-media-redundancy)
  
[Configuring media redundancy](#configuring-media-redundancy-1)

### Configuring multiple rings

#### Multiple rings

Use multiple rings to achieve higher availability for PROFINET IO networks with star topology.

In a multiple ring configuration, several PROFINET lines lead from a switch (star topology). The individual PROFINET lines lead from IO device to IO device. PROFINET lines run back to the switch from the last IO device on each individual line, thus forming several rings.

The switch operates as a manager. The manager must have two ring ports for each ring. Several rings are possible. For example, a SCALANCE X414 as of firmware version 3.10 supports up to 4 rings.

The manager monitors all the rings individually: It checks for each particular ring (an MRP domain) whether the transmission path is intact. To do this, it uses an MRP instance in each case. An MRP instance is required for each connected ring (set up automatically by STEP 7).

![Multiple rings](images/90700002443_DV_resource.Stream@PNG-en-US.png)

#### Requirements

The following devices support multiple rings as a manager:

- SCALANCE X300 as of version 4.0
- SCALANCE X414 as of version 3.10

#### Rules for the configuration of multiple rings

- MRP role at multiple rings:

  - The device that belongs to all the rings must have the MRP role in every instance that is entered in the GSD file in the "SupportedMultipleRole" attribute.
  - The switches from the SCALANCE X300 series V4.0 and higher (only via GSDML) and the X414 switch Version 3.10 and higher support the MRP role "Manager" for multiple rings.
- If the device that belongs to all rings has the "Manager" role in one ring, no devices with the "Manager (Auto)" role may exist in this ring.

#### Configuring multiple rings

To configure an MRP configuration with multiple rings, follow these steps:

1. In the topology view, interconnect the ring ports of the devices that are intended to belong to an MRP domain to form a ring.
2. Select the PROFINET IO system in the network view.
3. In the Inspector window, navigate to "Properties" &gt; "General" &gt; "PROFINET" &gt; "MRP domains" in the "Ring interconnection" field.   
   This field shows you all the topological rings in the IO system with the associated MRP domains.
4. Select one of the rings generated above in the "Ring interconnection" field.  
   The table below it shows all PROFINET devices in the selected ring.
5. Set the media redundancy role for the PROFINET devices in the MRP role column.

#### Adapting preset MRP roles

If you interconnect the devices of the example configuration as described below, the MRP roles are initially set to "Not device in the ring" for all devices.

This configuration is not consistent.

You have the following options:

- You can manually assign MRP roles according to the rules described for MRP configurations. To do this, edit the properties of the PROFINET IO system, in the area "MRP Domains &gt; Ring interconnection".
- You can have the MRP roles assigned automatically by STEP 7.

In both cases, select a configured MRP ring (in the area "MRP domains &gt; Ring interconnection") and click the "Configure MRP automatically" button. Repeat the process for each configured MRP ring.

The rings are then are assigned new MRP domains and the MRP roles and MRP instances are set. The configuration is consistent.

#### Example of multiple rings

The following figure shows an example configuration for multiple rings with two rings ① and ②.

![Example of multiple rings](images/90699900555_DV_resource.Stream@PNG-de-DE.png)

In the example, Switch 1 belongs to two MRP rings. Ring 1 is formed by Switch 1 and PLC 1, Ring 2 by Switch 1 and IO device 1.

The manager is located at the point of intersection of the two rings 1 and 2. The manager monitors the two rings separately. To do this, it uses two MRP instances.

One MRP instance checks whether all devices in ring 1 are reachable, another instance monitors whether all devices in ring 2 are reachable (only one device in each case in the example).

You can configure each MRP instance separately.

The following figure shows the two MRP instances in the manager (PROFINET interface of the switch). Here in the example, MRP instance 1 checks whether the devices in the MRP domain "mrpdomain-1" can be reached. The MRP instance 2 is responsible for monitoring the devices of the MRP domain "mrpdomain-2".

![Example of multiple rings](images/91047872779_DV_resource.Stream@PNG-en-US.png)

The following figure shows Ring 1 (mrpdomain-1). The participants of the mrpdomain‑1 are the PROFINET interface of the CPU as the "Client" and the MRP interface 1 of the PROFINET interface of the switch as the "Manager".

![Example of multiple rings](images/90699922187_DV_resource.Stream@PNG-en-US.png)

The following figure shows Ring 2 (mrpdomain-2). The participants of the mrpdomain‑2 are the PROFINET interface of the IO device as the "Client" and the MRP instance 2 of the PROFINET interface of the switch as the "Manager".

![Example of multiple rings](images/90699930891_DV_resource.Stream@PNG-en-US.png)

#### Tip: Delete the unneeded MRP domains

If you want to delete unneeded MRP domains, for example, because they no longer contain any devices, select the PROFINET IO system and then select the "MRP Domains" area.

1. Navigate to the first table. This is the table in which you select the default domain.
2. Select the row with the MRP domain to delete and press the &lt;Del&gt; key.

You can delete any MRP domain except the default domain.

---

**See also**

[Configuring media redundancy](#configuring-media-redundancy-1) 
  
[Media Redundancy Protocol (MRP)](#media-redundancy-protocol-mrp)

### MRP interconnection (S7-1500, S7-1500T)

S7-1500 CPUs as of firmware version V2.9 support MRP interconnection. This means they can be used as MRP managers in the coupled rings.

#### Definition

The process MRP interconnection is an enhancement of MRP and allows the redundant coupling of two or more rings with MRP in PROFINET networks. MRP interconnection is - like MRP - specified in the standard IEC 62439-2 (Edition 3).

#### Constraints

- You can couple a maximum of 11 MRP rings redundantly.
- You can operate a maximum of 50 devices per MRP ring.

#### Advantages

MRP interconnection allows the monitoring of larger topologies with ring redundancy. With MRP interconnection you are not limited to the maximum number of 50 devices in a ring when setting up redundant network topologies. The number of ring redundancy devices can be extended from 1 ring x 50 devices to a maximum of 11 rings x 50 devices.

#### Requirements

- The media redundancy procedure MRP is used in the participating rings.
- Each ring has its own MRP domain with an MRP manager and MRP clients.
- As MRP managers in the rings, the PROFINET devices support MRP interconnection (see technical specifications of the devices).

  CPUs S7-1500 firmware version V2.9 or higher support MRP interconnection.
- If you use PROFINET devices with more than 2 ports as MRP clients in the ring, then MRP interconnection is binding for these devices. For a device without MRP interconnection, telegrams leave the ring. This results in an additional load on the network.
- If you use PROFINET devices with only 2 ports in the ring as MRP clients, then MRP interconnection is recommended for all devices in the ring.

#### 4 devices for MRP interconnection connections

2 MRP-interconnection connections provide redundant coupling between 2 MRP rings. Four devices are required for the 2 connections:

- A Media Redundancy Interconnection Manager (MIM)
- 3 media-redundancy interconnection clients (MIC):

  - Primary MIC
  - Primary Coupled MIC
  - Secondary Coupled MIC

Since each of the four devices is part of an MRP ring, each device also assumes a media redundancy role.

Each of the 4 devices can take over the MRP manager role or MRP client role.

#### Topology and operating principle

You can find the description of the topology and the operating principle, for example, in the SCALANCE X help (redundancy method) or in the PROFINET Function Manual.

#### Configuring and assigning MRP interconnection parameters

> **Note**
>
> MRP interconnection is not integrated into the TIA Portal. This means you cannot configure, parameterize and diagnose MRP interconnection in STEP 7.

You configure and assign MRP interconnection parameters via the integrated web pages (Web Based Management) of the SCALANCE switches used as MIM and MIC (e.g. SCALANCE XC200, XM-400, XR-500).

For the configuration, follow the step-by-step instruction in the configuration manual [SCALANCE XM-400/XR-500 Web Based Management (WBM)](https://support.industry.siemens.com/cs/ww/en/view/109760840).

#### Reconfiguration and watchdog timer

The reconfiguration time of the rings is typically less than 200 milliseconds, but may be greater than 200 milliseconds.

In order for the data exchange to work after a reconfiguration, the watchdog timers of the IO devices must be set sufficiently large. Therefore, when using MRP interconnection, set the watchdog timer of the IO devices to 256 milliseconds.

---

**See also**

[MRP interconnection with the redundant system S7-1500R/H (S7-1500)](Principle%20of%20operation%20for%20S7-1500R-H%20CPUs%20%28S7-1500%29.md#mrp-interconnection-with-the-redundant-system-s7-1500rh-s7-1500)
  
[MRP Interconnection](Configuring%20SCALANCE%20X%20-%20W%20-%20M.md#mrp-interconnection)

## Configuring PROFIenergy (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Overview of PROFIenergy (S7-300, S7-400, S7-1500)](#overview-of-profienergy-s7-300-s7-400-s7-1500)
- [Configuring PROFIenergy for ET 200S (S7-300, S7-400, S7-1500)](#configuring-profienergy-for-et-200s-s7-300-s7-400-s7-1500)
- [Configuring PROFIenergy with I-devices (S7-300, S7-400, S7-1500)](#configuring-profienergy-with-i-devices-s7-300-s7-400-s7-1500)

### Overview of PROFIenergy (S7-300, S7-400, S7-1500)

#### Saving energy with PROFlenergy

PROFIenergy is a PROFINET-based data interface for switching off consumers centrally and with full coordination during pause times regardless of the manufacturer or device type. Through this, the process should only be provided with the energy that is absolutely required. The majority of the energy is saved by the process; the PROFINET device itself only contributes a few watts of savings potential.

![Energy savings during pauses with PROFIenergy](images/42134257547_DV_resource.Stream@PNG-en-US.png)

Energy savings during pauses with PROFIenergy

#### Basic information

Turning off the PROFINET devices or the power modules occurs through special commands in the user program of the PROFINET IO Controller. No additional hardware is needed, the PROFlenergy commands are directly interpreted by the PROFINET devices.

#### Principle of operation

At the beginning and end of pauses, the system manager enables or disables the pause function of the system; then the IO controller sends the PROFlenergy command "Start_Pause" / "End_Pause" to the PROFINET device. The device interprets the contents of the PROFlenergy command and turns on / off.

Through other PROFlenergy functions, device information can be accessed during pauses. The user can use this information in order to punctually transfer the "Start_Pause" / "End_Pause" command.

#### PROFlenergy instructions for IO controller

Two instructions are needed for controlling and monitoring the PROFlenergy functions.

The PE_START_END instruction allows you to easily activate and deactivate the idle state of PROFINET devices. This occurs by means of an incoming edge or outgoing edge. The PE_START_END instruction provides a simple interface for realizing PROFIenergy commands Start_Pause and End_Pause.

The PE_CMD instruction allows you to transmit all PROFIenergy commands, including Start_Pause and End_Pause. With the other commands, for example, the current status of the PROFINET device or the behavior during the pauses can be inquired. The PE_CMD instruction is a convenient means for handling all PROFIenergy functions.

#### PROFIenergy instruction for I-devices

The PE_I_DEV instruction allows you to realize PROFIenergy on I-devices, as well. The instruction receives PROFIenergy commands on the I-device and forwards these to the user program for processing. After processing the command, the user program calls the PE_I_DEV instruction again in order to send the acknowledgment to the IO controller. For these replies, each command offers you a helper instruction that supplies the reply data to the instruction.

The instructions can be found in the "Instructions" task card of the STEP 7 program editor.

An application example can be found on the [Internet](http://support.automation.siemens.com/WW/view/en/41986454) in the Service and Support portal.

#### Configuration and programming

The functions can be comfortably integrated into existing systems. Usually, no configuration is required for the use of PROFIenergy (exceptions under "See also"). However, amendments to the user program are required:

- Before the "Start_Pause" command, you must ensure that your system is brought into a condition that is suitable for a pause.
- A sequential control system for the beginning of the pause of the devices and for the punctual restarting of the device on break must be programmed (depending on the required startup times that the respective PROFINET device demands).
- The error messages of the PE_CMD instruction must be evaluated, and the required reaction must be programmed (for example, cancellation or continuation of further commands on lower-level PROFINET devices).

---

**See also**

[Description of PROFIenergy (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-of-profienergy-s7-300-s7-400)
  
[Description of PROFIenergy (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#description-of-profienergy-s7-1200-s7-1500)
  
[Configuring PROFIenergy for ET 200S (S7-300, S7-400, S7-1500)](#configuring-profienergy-for-et-200s-s7-300-s7-400-s7-1500)
  
[PROFIenergy (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#profienergy-s7-1200-s7-1500)
  
[Application example for PROFIenergy](https://support.industry.siemens.com/cs/us/en/view/109478388)
  
[Saving energy with SIMATIC S7 and SIMATIC HMI (TIA Portal)](https://support.industry.siemens.com/cs/ww/en/view/58235225)

### Configuring PROFIenergy for ET 200S (S7-300, S7-400, S7-1500)

The ET 200S distributed I/O system offers a special feature: for certain interface modules you can specify which potential groups or power modules of the IO device are activated for PROFIenergy.

#### Special features for ET 200S HF V7.0 and ET 200S FO V7.0 interface modules

You can configure the initial behavior of the power modules (e.g., the switchable power module (PM-E DC24V/8A RO)) for the above-named IO devices so that you do not have to bring the device to the energy saving state in the startup program with the PROFIenergy PE_Start_End_Pause instructions.

You activate the energy saving function in the properties of the power module (module parameters area, section "PROFIenergy").

Note that provisions are necessary in the user program for the use of PROFIenergy functions.

#### Rules

The configuration option described above is not available for ET 200S devices that were incorporated in the hardware catalog using GSDML files.

---

**See also**

[Overview of PROFIenergy (S7-300, S7-400, S7-1500)](#overview-of-profienergy-s7-300-s7-400-s7-1500)

### Configuring PROFIenergy with I-devices (S7-300, S7-400, S7-1500)

The requirement for program-controlled pauses for saving energy with PROFINET devices is that the PROFINET devices support the PROFIenergy protocol.

Only if a PROFINET device (IO device) supports the PROFIenergy protocol does an IO controller actually send PE commands to this IO device, for example to start or stop pauses.

If an IO device supports the PROFIenergy protocol, this property is saved in its PROFINET GSD file and is available for configuration in an engineering system.

For S7-1500 CPUs as intelligent IO devices (I-devices), you have the option with STEP 7 V13 service pack 1 or later to set PROFIenergy support for each transfer area.

If you have selected the option "Enable PROFIenergy communication" for a transfer area and import the generated PROFINET GSD file into another project, you can handle an I-device as a PE entity there.

#### Requirement

- STEP 7 as of V13 service pack 1
- S7-15XX-CPU as of firmware version 1.7 configured as I-device with transfer areas
- The user program on the I-slave handles PROFIenergy commands

  Background: You need to program PROFIenergy functions with I-devices in the user program using the "PE_I_DEV" instruction and corresponding auxiliary blocks; this is different compared with IO devices for which this functionality is made available by the firmware. This means that you can only enable PROFIenergy support for transfer areas if the user program on the I-slave is suitably designed.

#### Enabling PROFIenergy for transfer areas of I-devices

Proceed as follows to configure support of PROFIenergy:

1. Select the PROFINET interface (X1) of the CPU.
2. Select the required transfer area in the area navigation, for example:

   Operating mode &gt; I-device communication &gt; Transfer_area_1.
3. Select the "Enable PROFIenergy communication" check box.

Once the I-device is fully configured, generate the GSD file for the I-device and import this file in the project for the I/O controller. The GSD file generated is compatible with GSD version 2.31 and contains an entry that specifies that the I-device supports the PROFIenergy profile.

To address the I-device, for example for the PE command "PE_START_END", use the hardware identifier of the "PROFIenergy supporting" transfer area in the I-device.

To address the IO controller for the PE command "PE_I_DEV", use the hardware identifier of the transfer area that is supplied with the data for PROFIenergy on the IO controller.

## Configuring Shared Devices (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Useful information on Shared Devices (S7-300, S7-400, S7-1500)](#useful-information-on-shared-devices-s7-300-s7-400-s7-1500)
- [Basic information on project-internal shared devices. (S7-300, S7-400, S7-1500)](#basic-information-on-project-internal-shared-devices-s7-300-s7-400-s7-1500)
- [Configuring a project-internal shared device (S7-300, S7-400, S7-1500)](#configuring-a-project-internal-shared-device-s7-300-s7-400-s7-1500)
- [Configuring Shared Device (GSD configuration) (S7-300, S7-400, S7-1500)](#configuring-shared-device-gsd-configuration-s7-300-s7-400-s7-1500)
- [Configuring an I-device as a shared device (S7-300, S7-400, S7-1500)](#configuring-an-i-device-as-a-shared-device-s7-300-s7-400-s7-1500)
- [Module-internal shared input/shared output (MSI/MSO) (S7-300, S7-400, S7-1500)](#module-internal-shared-inputshared-output-msimso-s7-300-s7-400-s7-1500)

### Useful information on Shared Devices (S7-300, S7-400, S7-1500)

#### Shared device functionality

Numerous IO controllers are often used in larger or widely distributed systems.

Without the "Shared device" function, each I/O module of an IO device is assigned to the same IO controller. If sensors that are physically close to each other must provide data to different IO controllers, several IO devices are required.

The "Shared device" function allows the modules or submodules of an IO device to be divided up among different IO controllers. Thus allowing flexible automation concepts. You have, for example, the possibility of combining I/O modules lying near other into an IO device. Drives such as SINAMICS S120 also support the shared device functionality.

![Shared device functionality](images/53313140107_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PROFINET |
| ② | logical assignment |

#### Principle

Access to the submodules of the shared device is divided up among the individual IO controllers. Each submodule of the shared device is assigned exclusively to one IO controller.

#### Requirement

- STEP 7 as of V12 Service Pack 1
- S7-1500 CPU as of firmware 1.1 / ET 200SP CPU as IO controller or S7-300/400 CPU as IO controller
- S7-1200 CPU FW 4.1 or higher.
- S7-300/400 CPU (STEP 7 TIA Portal as of V13 SP1)
- IO device supports the "Shared device" function, e.g., IM 155-5 PN ST interface module
- With GSD configuration of the IO device: GSD file for configuring the IO device is installed
- For information on the requirements for a configuration of IO controller and IO devices in one project see the next section.

Comments:

- An S7-1500 CPU configured as an I-device can be used as a shared device as of firmware version V1.5. The I-device must be integrated by GSD import into the IO system of the IO controller.
- An S7-300 CPU or S7-400 CPU configured as an I-device can be used as a shared device under the following condition:

  You must export the PROFINET GSD file for the I-device from STEP 7 (V5.5 or higher) or STEP 7 (TIA Portal) and then import it into STEP 7 (TIA Portal).

#### Configuration options for shared devices

If a maximum of two IO controllers access a shared device, it is preferable to configure the shared device in a common project together with the IO controllers that access it. As a result, all components of a shared device configuration are known to the project. Therefore, configuration in a common project offers the following advantages compared to configuration in multiple projects:

Using a shared device and its IO controllers in a common project:

- Since STEP 7 V18: You can configure a shared device and two CPUs accessing it (IO controllers) in a single project.
- From STEP 7 V19: You can also configure a shared I-device and two CPUs accessing it (IO controllers) in a single project.

  - Requirement: Use an S7-1500 CPU with FW version V3.1 or higher as the shared I-device

As compared to the existing shared devices, a project-internal shared device has the following advantages:

- Reduction in the possible error sources: The complete consistency is examined by STEP 7 in a project.
- Less configuration effort: No use of different STEP 7 projects.
- Improved diagnostics: Complete diagnostics in one project.

To configure access to a shared device by more than two IO controllers, you need to use the shared device in multiple projects. The shared device must be configured in every project that contains IO controllers accessing it.

Using a shared device in multiple projects:

- Since STEP 7 V12 SP1, the S7-1500 CPUs as well as the distributed I/O devices of SIMATIC support the "Shared device" function. The shared device must be present in every project, although it is present only once in the system. A separate project is required for every CPU that accesses the shared device. For information on which components support the "Shared device" function see the following [FAQ](https://support.industry.siemens.com/cs/us/en/view/102325771).

#### Setting of the real-time properties

If, apart from the CPUs in the project, other CPUs outside the project have access to the shared device, you must input the number of project-external IO controllers at the PROFINET interface of the shared devices. Only then does STEP 7 correctly calculate the communication load and thus the resulting update times.

The maximum possible number of IO controllers for the shared device depends on the device. This number is stored in the GSD file of the shared device.

You can set a very short send clock with a CPU as IO controller. The send clock can be shorter than the shortest send clock supported by the project-internal shared device. In this case, the project-internal shared device is operated by the IO controller with a send clock that it supports (send clock adaptation).

Example:

A CPU supports send clocks starting from 0.25 ms. A configured IO device also supports send clocks starting at 0.25 ms; another IO device supports send clocks starting at 1 ms. In this case, you have the option of setting the short send clock of 0.25 ms for the CPU. The CPU operates the "slow" IO device with the send clock of 1 ms, for example.

#### Response in the event of a fault

You can find out how PROFINET IO controllers behave in the event of an error when accessing the data of a shared device in this [FAQ](https://support.industry.siemens.com/cs/ww/en/view/109572804).

---

**See also**

[Displaying IO controllers that access modules of a Shared Device (S7-1500)](Device%20and%20network%20diagnostics.md#displaying-io-controllers-that-access-modules-of-a-shared-device-s7-1500)
  
[Configuring an I-device as a shared device (S7-300, S7-400, S7-1500)](#configuring-an-i-device-as-a-shared-device-s7-300-s7-400-s7-1500)
  
[Configuring Shared Device (GSD configuration) (S7-300, S7-400, S7-1500)](#configuring-shared-device-gsd-configuration-s7-300-s7-400-s7-1500)

### Basic information on project-internal shared devices. (S7-300, S7-400, S7-1500)

#### Requirements

In project-internal shared devices, there are up to 2 IO controllers and the shared device in the same subnet. The project-internal shared device must be assigned to every IO controller. Likewise, at least 1 module or submodule must be assigned to each connected IO controller, otherwise the configuration as shared device is inconsistent. If an inconsistent configuration is compiled in STEP 7, a corresponding error message is displayed.

#### Restrictions

- Only IO devices that have been installed in the hardware catalog via GSD files are permitted as project-internal shared devices.
- You cannot use I-devices as project-internal shared devices.
- In a project, maximum 2 IO controllers (CPUs) may access a project-internal shared device.
- The project-internal shared device does not support system redundancy.
- Fail-safe applications are not supported
- "TIA Portal Openness" does not support project-internal shared devices.
- Loading the device as a new station is not supported. In TIA Portal V18, both the CPUs that share the project-internal shared device must be loaded into 2 different projects. The configuration must be manually completed or restored.

#### Access to modules and submodules

Every IO controller has access only to the modules and submodules assigned to it, which means, in detail:

- Data exchange only with the assigned modules or submodules
- Receiving alarms and diagnostics only of assigned modules or submodules
- Parameter assignment only of assigned modules or submodules

#### Rules for the configuration

The following rules apply to a configuration with a project-internal shared device and are automatically validated at the time of compilation by STEP 7:

- All IO controllers that access the project-internal shared device must be located in the same subnet as the IO device.
- The project-internal shared device must be an IO device that was installed in the hardware catalog via a GSD file.
- There must be at least 1 module or submodule assigned to every IO controller that is connected to the project-internal shared device.
- Only 1 IO controller may have access to 1 submodule.
- I/O addresses of a module or submodule can only be edited in the address area of the IO controller to which the project-internal shared device is assigned.
- The send clock must be identical for all IO controllers that have access to the project-internal shared device.
- The following functions are only possible in conjunction with the IO controller to which the interface module of the project-internal shared device is assigned:

  - Isochronous mode (IRT)
  - Prioritized startup
  - Parameter assignment of the port properties
- If the "Use name as extension for device names" option is selected for an IO system, this option must also be selected for the IO system of the second CPU.
- If you change the name of the project-internal shared device, then you must subsequently load all the CPUs that share this IO device.
- The maximum total of the communication relationships (ARs) for the project-internal shared device may not be exceeded. The maximum total of the communication relationships may be found, for example, in the "Information" tab in the hardware catalog.

  Example:   
  An ET 200SP interface module supports up to 4 communication relationships as a project-internal shared device. The project-internal shared device is already assigned to 2 IO controllers. A maximum of 2 more IO controllers, which are configured project-externally, may access modules or submodules of the project-internal shared device.

### Configuring a project-internal shared device (S7-300, S7-400, S7-1500)

Below, you will find a description of how to configure a distributed I/O system as a project-internal shared device with STEP 7 version V18 or higher.

If one of the following cases applies to your project, continue reading in the section "[Configuring Shared Device (GSD configuration)](#configuring-shared-device-gsd-configuration-s7-300-s7-400-s7-1500)":

- Your project contains a shared device that is accessed by more than 2 IO controllers. These IO controllers are configured either in another TIA Portal project or with another engineering tool.
- You do not want to use any IO devices that are integrated via GSD files.

A "distributed" configuration with different engineering tools for different IO controller families is always possible. However, the description of the procedure is based solely on STEP 7 version as of V18.

The following description is limited to 2 IO controllers of the S7-1500 family that share a project-internal shared device.

As of STEP 7 V18, only one project is required for a shared device configuration. The project contains the project-internal shared device and maximum 2 IO controllers that access it.

#### Requirements

- STEP 7 (TIA Portal) as of V18
- The IO controllers support the shared device function, for example CPU 1513-1 PN as of firmware version V3.0.
- The IO device supports shared device functionality, for example, interface module IM 155-5 PN ST.
- The GSD file for the IO device was installed in STEP 7 V18 and used for the configuration.

#### Procedure - Creating a project

To create a project with a project-internal shared device, follow these steps:

1. Start STEP 7.
2. Create a new project, for example, with the name "Shared Device".
3. In the network view, add an IO controller (for example, CPU 1513-1 PN) from the hardware catalog.
4. Assign a name, for example, "PLC_1".
5. Add another IO controller (for example, CPU 1513-1 PN) from the hardware catalog.
6. Assign a name, for example, "PLC_2".
7. Connect the PROFINET interface X1 of "PLC_1" and "PLC_2" to one another. As a result, the PROFINET interfaces of the CPUs are in the same subnet.
8. Insert an IO device (for example, IM 155-6 PN ST) from the hardware catalog. You can find the IO devices installed from the GSD files under "Other field devices &gt; PROFINET IO &gt; IO &gt; SIEMENS AG"
9. Double-click the added IO device; the device view opens.
10. Double-click all the required modules and submodules from the hardware catalog in the device overview table. Also use the modules and submodules installed from the GSD files.
11. Assign parameters to the individual I/O modules.
12. Switch to the network view.
13. Assign the IO device in succession to the IO controllers "PLC_1" and "PLC_2".
14. Save the project.

    ![Procedure - Creating a project](images/158708542091_DV_resource.Stream@PNG-en-US.png)

    ![Procedure - Creating a project](images/158708542091_DV_resource.Stream@PNG-en-US.png)

#### Procedure - assigning parameters to the shared devices

After the first assignment of the project-internal shared devices to an IO controller, all the modules or submodules are assigned to that IO controller.

Newly added modules or submodules are assigned to that IO controller to which the interface module is also assigned. If a project-internal shared device is disconnected from an IO controller, the assigned modules or submodules obtain the "unknown" access status.

To change the assignment, follow these steps:

1. In the network view or the device view of the project, select the interface module of the project-internal shared device.
2. In the Inspector window, select the "Shared Device" tab under "Properties &gt; General".

   A table shows which IO controller has access to the respective module or submodule. The default setting for all modules and submodules is the IO controller to which the project-internal shared device was first assigned.
3. For all modules and submodules that are to remain in this address area, leave the setting "PLC_1" as it is.

   For all modules or submodules that you wish to assign to the address area of the other IO controller, select the setting "PLC_2".

   Special consideration: With the "Outside of project" option, select other IO controllers that are already connected to the PROFINET IO system.

   ![Procedure - assigning parameters to the shared devices](images/158420423307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure - assigning parameters to the shared devices](images/158420423307_DV_resource.Stream@PNG-en-US.png)

#### Procedure - Adjusting the real-time settings

By adjusting and validating the settings given below, the following properties are ensured:

- All IO controllers and shared devices are operated with the appropriate send clock.
- Update times are calculated correctly based on the communications load.

To adjust and validate these settings, follow these steps:

1. Select the interface module of the project-internal shared device in the network view.
2. In the Inspector window, navigate to the "PROFINET interface &gt; Advanced options &gt; Real time settings &gt; IO cycle" area.
3. If project-external IO controllers also access this shared device: In the "Shared Device" tab, set the number of project-external IO controllers. The maximum number depends on the IO device (specification in GSD file).
4. For every IO controller that has access to modules or submodules of the project-internal shared device, you need to adjust the real-time settings on a CPU-specific basis in each case.
5. You must set the same send clock for each IO controller that has access to modules and submodules of the project-internal shared device:

   - If you configure another project-external IO controller with STEP 7 (TIA Portal):

     Open the corresponding project.

     Select the PROFINET interface of the IO controller.

     Select the "Advanced options &gt; Real time settings &gt; IO communication" area in the Inspector window and set the shared send clock.
   - If you configure another project-external IO controller with a different engineering tool:

     Select the PROFINET interface of the shared device in STEP 7 (TIA Portal) and read out the send clock on the shared device ("Advanced options &gt; Real time settings" area)

     Enter the read send clock in the engineering tool.
   - Special consideration: If you configure **all** IO controllers that have access to the shared device in STEP 7 (TIA Portal or V5.5), you can set shorter send clocks on the IO controller than supported by the shared device (send clock adaptation).

#### Compiling and loading

When you select the project-internal shared device and click on "Compile" in the toolbar, the configuration of both the IO controllers is checked for data consistency.

You must load the configurations for the different IO controllers in succession into the IO controllers.

### Configuring Shared Device (GSD configuration) (S7-300, S7-400, S7-1500)

Below, you will find a description of how to configure a distributed I/O system as a shared device with STEP 7 V12, Service Pack 1 or higher.

A "distributed" configuration with different engineering tools for different IO controller families is always possible. However, the description of the procedure is exclusively based on STEP 7 V12, Service pack 1. The description is limited to two IO controllers of the S7-1500 family that share a shared device.

Two projects are created (Shared-Device-1 and Shared-Device-2), each with one IO controller (PLC1 and PLC2). You must create the shared device in both projects, even though it is physically one and the same IO device.

#### Requirements

- STEP 7 as of V12 Service Pack 1
- In the context of STEP 7 V12, Service Pack 1: Only CPU 15XX as of FW 1.1 can be configured as IO controller (no CPU 31X, CPU 41X or CPU 12XX).
- In the context of other IO controllers that are to have access to a shared device: Corresponding engineering tool, for example, STEP 7 V5.5, Service Pack 3 for CPU 31x-3 PN/DP.
- IO device supports shared device functionality, e.g., interface module IM 155-5 PN ST V2.0.
- GSD file for configuring the IO device as shared device is installed.

#### Procedure - Creating project 1

To create the first project with a shared device, follow these steps:

1. Start STEP 7.
2. Create a new project with the name "Shared-Device-1".
3. Insert a CPU 1513-1 PN from the hardware catalog in the network view. Name it "PLC1".
4. Insert an IO device with the "Shared device" function from the hardware catalog (hardware catalog: Other field devices &gt; PROFINET IO &gt; I/O).
5. Assign the IO controller "PLC1" to the IO device.
6. Double-click the IO device and insert all required modules and submodules from the hardware catalog in the device overview table.
7. Assign the module parameters.
8. Save the project.

#### Procedure - Creating project 2

To create the second project with a shared device, follow these steps:

1. Start STEP 7 once again.

   A new instance of STEP 7 opens.
2. In the new instance, create a new project with the name "Shared-Device-2".
3. Insert a CPU 1513-1 PN in the network view. Name it "PLC2".
4. Copy the IO device from the project "Shared-Device-1" and insert it in the network view of project "Shared-Device-2".
5. Assign the IO controller "PLC2" to the IO device.
6. Save the project.

Both projects now have an identically structured IO device that must be configured in the next step for the different types of IO controller access.

#### Procedure - Configuring access to the shared device

The modules and submodules you insert in the shared device are automatically assigned to the local CPU. To change the assignment, follow these steps:

1. Select the interface module in the network or device view of project "Shared-Device-1".
2. Select the "Shared device" area in the Inspector window.

   A table shows which CPU has access to the respective module or submodule for all configured modules. The default setting is that the local CPU has access to all modules and submodules.
3. Keep the "PLC1" setting for all modules and submodules that are to remain in the address range of the local CPU

   Select the setting "---" for all modules and submodules that are to be located in the address range of the CPU from the "Shared-Device-2" project (PLC2). This means that an IO controller outside the project is to have access to the module or submodule.
4. Select the interface module in the network or device view of project "Shared-Device-2".
5. Select the "Shared device" area in the Inspector window.

   A table shows which CPU has access to the respective module or submodule for all configured modules.
6. Select the setting "---" for all modules and submodules that are to be located in the address range of the CPU from the "Shared-Device-1" project (PLC1).
7. Finally, check whether the settings for access are "complementary" for each module or submodule in both projects. This means that if the local CPU has access in one project, the option "---" must be set in the other project and vice versa.

   Special note: The option "---" for the PROFINET interface and therefore for the ports has the effect that the associated parameters are deactivated and cannot be changed. Parameters of the PROFINET interface and port parameters can only be edited in the project in which the PROFINET interface is assigned to the local CPU. The ports can be interconnected in both projects regardless of this.
8. Check whether the same IP address parameters and device name are set for the shared device in all projects.

   Check whether the same S7 subnet ID is set in all projects for the subnet to which the shared device is connected (subnet properties, "General" area in the Inspector window).

**Note**

If you make changes to the shared device: Make the same changes in each project on the shared device. Make sure that only one IO controller has access to a module or submodule.

#### Procedure - Adjusting the real-time settings

To ensure that all IO controllers and shared devices are operated with the appropriate send clock and that the update times are calculated correctly based on the communication load, you must adjust and check the following settings:

1. Select the project whose IO controllers have access to the PROFINET interface and the ports of the shared device.
2. Select the interface module of the shared device in the network view.
3. In the Inspector window, navigate to the "PROFINET interface &gt; Advanced options &gt; Real time settings &gt; IO cycle" area.
4. In the "Shared device" area, set the number of project-external IO controllers. The maximum number depends on the IO device (default in GSD file).
5. You must set the same send clock for each IO controller that has access to modules and submodules of the shared device:

   - If you configure the IO controller with STEP 7 (TIA Portal):

     Open the corresponding project.

     Select the PROFINET interface of the IO controller.

     Select the "Advanced options &gt; Real time settings &gt; IO communication" area in the Inspector window and set the shared send clock.
   - If you configure the IO controller with a different engineering tool:

     Select the PROFINET interface of the shared device in STEP 7 (TIA Portal) and read out the send clock on the shared device ("Advanced options &gt; Real time settings" area)

     Enter the read send clock in the engineering tool.
   - Special note: If you configure **all** IO controllers that have access to the shared device in STEP 7 (TIA Portal or V5.5), you can set shorter send clocks on the IO controller than supported by the shared device (send clock adaptation).

#### Compiling and loading

You must compile the configurations for the different IO controllers and load them to the CPUs one after the other.

Due to the distributed configuration with separate projects, STEP 7 does not output consistency errors in the case of incorrect access parameter assignment. Examples for incorrect access parameter assignment:

- Several IO controllers have access to the same module
- IP address parameters or send clocks are not identical

These errors do not have an effect until operation and are signaled as configuration errors, for example.

### Configuring an I-device as a shared device (S7-300, S7-400, S7-1500)

Below, you will find a description of how you configure an S7-1500 as an I-device with STEP 7 Version V13 or higher and then use it in two projects as a shared device.

A "distributed" configuration with different engineering tools for different IO controller families is generally also possible here. The procedure described below is based on STEP 7 V13 and is limited to a configuration with two IO controllers of the S7-1500 family that share the transfer areas of an I-device as a shared device. The I-device itself is also an S7-1500 CPU.

First, the general concept is described.

The following sections explain the step-by-step procedure using an example: Three projects are created with one IO controller each (PLC-I-Device, PLC_1, and PLC_2).

PLC-I-Device is used to configure the I-device. The PROFINET GSD variant of PLC-I-Device is used in the PLC_1 and PLC_2 projects in order to assign the transfer areas in the respective higher-level IO controller.

#### Shared I-device concept

For the introduction of the shared I-device concept, two roles are distinguished:

- The role of manufacturer (e.g., machine manufacturer): The manufacturer configures and programs an I-device that performs a particular automation task. Transfer areas are defined as the I/O interface to the operator of the machine. These transfer areas can be assigned to different IO controllers. For the connection to higher-level IO controllers, the manufacturer provides a PROFINET GSD file and discloses the transfer areas via which the I-device can be accessed.
- The role of the operator: The operator uses the I-device as a PROFINET GSD variant during configuration of the PROFINET IO system and, in this process, specifies the I/O addresses under which the IO controllers access the transfer areas.

#### Manufacturer view

When assigning parameters, you specify the S7-1500 CPU as an I-device with central and distributed I/O. The following settings are important:

- Required transfer areas
- Number of IO controllers with access to this I-device (with shared device always greater than 1!)

Special note: The I-device is configured without a higher-level IO controller. As a result, only the local I/O addresses of the transfer area are available (= "Address in the I-device") in order to create the user program for editing the addresses from the transfer area.

The I-device that has been completely configured except for the connection to the higher-level IO controller is loaded to the S7-1500 CPU.

You export a PROFINET GSD file from the I-device configuration.

![Manufacturer view](images/104729173131_DV_resource.Stream@PNG-en-US.png)

#### Operator view

You must install the PROFINET GSD file created from the I-device configuration in all engineering systems that are involved in configuring a PROFINET IO system with this shared I-device. If all uses of this I-device will be configured with STEP 7 V13, it is sufficient to install the GSD file in STEP 7.

**Each higher-level IO controller with assigned shared I-device transfer area in its own project.**

You configure the I-device as a GSD variant on the PROFINET IO system in the projects involved. In STEP 7 V13, this I-device can be found under "Other field devices &gt; PROFINET IO &gt; PLCs &amp; CPs" following installation.

You need a separate project for each assignment between the shared I-device and one of the higher-level IO controllers that share the transfer areas.

The following figure shows the assignment of the shared I-device to the higher-level IO controller PLC_1.

For each higher-level IO-Controller you must create a separate project with the same shared I-device and grant the IO controller access to the desired partial transfer area.

![Operator view](images/104729114379_DV_resource.Stream@PNG-en-US.png)

In each of the projects involved, you define which transfer areas are assigned exclusively to the higher-level IO controller (default setting: all). You set the other transfer areas to "---" (not assigned). As a result of this setting, the local IO controller has no access to this transfer area and it can therefore be assigned to another IO controller in another project.

![Operator view](images/104729191179_DV_resource.Stream@PNG-en-US.png)

You adapt the addresses from the view of the IO controller in the device overview. To open the device overview, double-click on the I-device.

![Operator view](images/104729409931_DV_resource.Stream@PNG-en-US.png)

#### Requirement

- STEP 7 V13 or higher
- In the context of STEP 7 V13 or higher: Only CPU 15XX FW 1.5 or higher can be configured as a shared I-device (no CPU 31X, CPU 41X, or CPU 12XX).
- In the context of other IO controllers that are to have access to a shared I-device: Corresponding engineering tool, for example, STEP 7 V5.5, Service Pack 3 for CPU 31x-3 PN/DP.

#### Procedure - Creating the PLC-I-device project

To create the project with a shared I-device, follow these steps:

1. Start STEP 7.
2. Create a new project with the name "PLC-I-device".
3. Insert a CPU 1518-4 PN/DP from the hardware catalog in the network view. Assign the name "PLC-I-device".
4. Double-click the IO device and configure all required modules and submodules.
5. Assign the module parameters.

   In particular, the following settings for the CPU are necessary in the area of the PROFINET interface [X1]:

   - Enable the "IO device" option in the "Operating mode" area.
   - Configure the transfer areas in the "Operating mode" &gt; "I-device configuration" area. The "Address in IO controller" column remains empty because no IO controller is assigned.

     Note: To change an input area to an output area, and vice versa, you must navigate to the area of the corresponding transfer area.

     ![Procedure - Creating the PLC-I-device project](images/104729195787_DV_resource.Stream@PNG-en-US.png)

     ![Procedure - Creating the PLC-I-device project](images/104729195787_DV_resource.Stream@PNG-en-US.png)
   - Select the number of IO controllers that will access the shared I-device during operation ("Mode" &gt; "Real time settings" area, "Shared Device" section).
6. Save the project.
7. Click the "Export" button ("Mode" &gt; "I-device configuration" area, "Export general station description file (GSD)" section).

   If you do not change the name in the Export dialog, the GSD file has a name in the form "GSDML-V2.31-#Siemens-PreConf_PLC-I-Device-20130925-123456", for example.

#### Procedure - Creating the PLC_1 project

To create the first project with a shared I-device, follow these steps:

1. Start STEP 7.
2. Install the PROFINET GSD file from the export of the I-device CPU (PLC-I-Device).
3. Create a new project with the name "PLC_1".
4. Insert a CPU 1516-3 PN/DP in the network view. The name of the CPU should be "PLC_1".
5. Insert the I-device from the hardware catalog (Hardware catalog: Other field devices &gt; PROFINET IO &gt; PLCs &amp; CPs).
6. Assign the IO controller "PLC_1" to the I-device.
7. Select the "Shared Device" area in the properties of the I-device.

   In the table, all transfer areas and the PROFINET interface are assigned to the local IO controller (PLC_1).
8. Define the transfer areas to which the PLC_1 CPU should **not** have access. Select the "---" entry for these areas. These transfer areas are provided for PLC_2.
9. Save the project.

#### Procedure - Creating the PLC_2 project

To create the second project with a shared device, follow these steps:

1. Start STEP 7 once again.

   A new instance of STEP 7 opens.
2. In the new instance, create a new project with the name "PLC_2".
3. Insert a CPU 1516-3 PN/DP in the network view. Assign the name "PLC_2".
4. Insert the I-device from the hardware catalog (Hardware catalog: Other field devices &gt; PROFINET IO &gt; PLCs &amp; CPs).
5. Assign the IO controller "PLC_2" to the I-device.
6. Adapt the access to the transfer areas as in the PLC_1 project. Ensure that no duplicate assignments result.
7. Adapt the parameters of the subnet and PROFINET interface. Because the shared I-device involves the same device in different projects, these data must match.
8. Save the project.

Both projects now have an identically configured shared I-device. The IO controller access and the parameters of the PROFINET interface should still be checked in the different projects during the next step.

#### Summary - Assigning accesses to the shared device

The transfer areas are automatically assigned to the local IO controller. To change the assignment, follow these steps:

1. Click the "PLC_I-Device" device in the network view of the "PLC_1" project, and select the "Shared Device" area.
2. A table shows which CPU has access to each of the configured transfer areas. The default setting is that the local CPU has access to all modules and submodules.
3. Keep the setting "PLC_1" for all transfer areas that are to remain in the address range of the local CPU

   Select the setting "---" for all transfer areas that are to be located in the address range of the "PLC_2" CPU from the "PLC_2" project. This means that an IO controller outside the project is to have access to the transfer area.
4. Follow the same procedure for the remaining projects.
5. Finally, check whether the settings for access are "complementary" for each module or submodule in both projects. This means that if the local CPU has access in one project, the option "---" must be set in the other project and vice versa.

   Special note: The option "---" for the PROFINET interface and therefore for the ports has the effect that the associated parameters are deactivated and cannot be changed. Parameters of the PROFINET interface and port parameters can only be edited in the project in which the PROFINET interface is assigned to the local CPU. The ports can be interconnected in both projects regardless of this.
6. Check whether the same IP address parameters and device name are set for the shared device in all projects.

   Check whether the same S7 subnet ID is set in all projects for the subnet to which the shared device is connected (subnet properties, "General" area in the Inspector window).

**Note**

If you make changes to the I-device (e.g., change the number or length of the transfer areas):

Export the I-device as a GSD file again. Re-install the GSD file in each project that uses the I-device as a shared device. Make sure that only one IO controller has access to a transfer area.

#### Procedure - Adjusting the real-time settings

To ensure that all IO controllers and shared devices are operated with the appropriate send clock and that the update times are calculated correctly based on the communication load, you must adjust and check the following settings:

1. You must set the same send clock for each IO controller that has access to modules and submodules of the shared device:

   - If you configure the IO controller with STEP 7 (TIA Portal):

     Open the corresponding project.

     Select the PROFINET interface of the IO controller.

     Select the "Advanced options &gt; Real time settings &gt; IO communication" area in the Inspector window and set the shared send clock.
   - If you configure the IO controller with a different engineering tool:

     Select the PROFINET interface of the shared device in STEP 7 (TIA Portal) and read out the send clock on the shared device ("Advanced options &gt; Real time settings" area)

     Enter the read send clock in the engineering tool.
   - Special note: If you configure **all** IO controllers that have access to the shared I-device in STEP 7 (TIA Portal or V5.5), you can set shorter send clocks on the IO controller than supported by the shared device (send clock adaptation).

#### Compiling and loading

You must compile the configurations for the different IO controllers and load them to the CPUs one after the other.

Due to the distributed configuration with separate projects, STEP 7 does not output consistency errors in the case of incorrect access parameter assignment. Examples for incorrect access parameter assignment:

- Several IO controllers have access to the same module
- IP address parameters or send clocks are not identical

These errors do not have an effect until operation and are signaled as configuration errors, for example.

---

**See also**

[Configuring the I device](#configuring-the-i-device)
  
[Useful information on Shared Devices (S7-300, S7-400, S7-1500)](#useful-information-on-shared-devices-s7-300-s7-400-s7-1500)

### Module-internal shared input/shared output (MSI/MSO) (S7-300, S7-400, S7-1500)

#### Introduction

This section describes the module-internal shared input/shared output (MSI/MSO) functionality for the S7-1500 I/O modules that are operated in an ET 200MP on PROFINET.

#### Module-internal shared input/shared output functionality

The module-internal shared input (MSI) function allows an input module to make its input data available to up to four IO controllers. Each controller has read access to the same channels.

The module-internal shared output (MSO) function allows an output module to make its output data available to up to four IO controllers. One IO controller has write access. The other IO controllers have read access to the same channels.

The following figure shows the MSI/MSO functionality.

![Module-internal shared input/shared output functionality](images/59407166987_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPU 1516-3 PN/DP as IO controller |
| ② | CPU 1511-1 PN as IO controller |
| ③ | I/O module with MSI/MSO |
| ④ | Read access to the channels of the I/O module |
| ⑤ | Write access to the channels of the I/O module (only with MSO) |

#### Advantages of MSI/MSO

Module-internal shared input/shared output (MSI/MSO) offers the following advantages:

- Real-time acquisition in multiple CPUs
- Lower costs due to saving on additional IO devices and modules
- Lower space requirements due to saving on additional IO devices and modules
- Reduced communication load because no CPU-CPU communication is needed
- No additional programming effort is needed for CPU-CPU communication

#### Requirements for the use of MSI/MSO

Observe the following requirements:

- MSI/MSO can only be used with PROFINET IO
- Configuration software: STEP 7 (TIA Portal) V12 SP1 or higher with GSD file.
- The IM 155-5 PN ST interface module and the modules support MSI/MSO firmware version V2.0.0 or higher.

#### Boundary conditions for the use of MSI/MSO

Note the following boundary conditions:

- MSI/MSO cannot be used for modules with channel groups.
- Modules with MSI/MSO cannot be operated in isochronous mode.

#### MSI submodules

The input values of all channels are copied to a basic submodule and up to three other MSI submodules during MSI configuration of an input module. The channels of the module are then available with identical input values in the basic submodule and the MSI submodules. The submodules can be assigned to up to four IO controllers when the module is used in a shared device. Each IO controller has read access to the same channels.

The following figure shows a digital input module with the basic submodule and three MSI submodules. Each submodule is assigned to an IO controller. Diagnostics and parameter assignment of the digital input module can be performed from the IO controller 1 via the basic submodule.

![MSI submodules](images/61585292683_DV_resource.Stream@PNG-en-US.png)

#### Value status of the MSI submodule (Quality Information, QI)

The meaning of the value status depends on the submodule to which it pertains.

For the basic submodule (first submodule), the value status 0 indicates that the value is incorrect.

For an MSI submodule (submodules 2 to 4), the status value 0 indicates that the value is incorrect or the basic submodule parameters have not yet been assigned (not ready for operation).

#### MSO submodules

The output values of all channels of the module are copied from a basic submodule to up to three other MSO submodules during MSO configuration of an output module. The channels of the module are then available with identical values in the basic submodule and the MSO submodules. The MSO submodules can be assigned to up to four IO controllers when the module is used in a shared device:

- The IO controller to which the basic submodule is assigned has write access to the outputs of the module. The basic submodule therefore occupies output addresses in the process image of the IO controller.
- The IO controllers to which the MSO submodules are assigned have read access to the outputs of the module. MSO submodules therefore occupy input addresses in the process image of the IO controller.

The following figure shows a digital output module with the basic submodule and three MSO submodules. Each submodule is assigned to an IO controller. Diagnostics and parameter assignment of the digital output module can be performed from IO controller 1 via the basic submodule.

![MSO submodules](images/61585310475_DV_resource.Stream@PNG-en-US.png)

#### Value status of the MSO submodule (Quality Information, QI)

The meaning of the value status depends on the submodule to which it pertains.

For the basic submodule (first submodule), the value status 0 indicates that the value is incorrect.

For an MSO submodule (submodules 2 to 4), the status value 0 indicates that the value is incorrect or one of the following errors has occurred:

- The basic submodule parameters have not yet been assigned (not ready for operation).
- The connection between the IO controller and the basic submodule has been interrupted.
- The IO controller of the basic submodule is in STOP or POWER OFF state.

#### Configuring I/O modules with MSI/MSO submodules

**Requirement**

- Configuration software STEP 7 V12 Service Pack 1 or higher
- GSD file for I/O modules with MSI/MSO.
- IO device supports MSI/MSO (e.g., IM 155-5 PN ST firmware version V2.0.0 or higher)

**Procedure**

1. In the network view of STEP 7, insert an interface module as of IM 155-5 PN ST V2.0.
2. Double-click the IO device.

   You are now in the device view.
3. Place the modules with MSI/MSO from the hardware catalog in a suitable slot.
4. Configure the modules as described in the product information for the module.

## Creating a standard machine project

This section contains information on the following topics:

- [Overview](#overview)
- [Multiple use PROFINET IO systems](#multiple-use-profinet-io-systems)
- [Configuration control (option handling) for PROFINET IO systems](#configuration-control-option-handling-for-profinet-io-systems)

### Overview

#### Introduction

Standard machine projects are STEP 7 projects that use a set of innovative functions allowing simple configuration and commissioning of flexible automation solutions for standard machines or for machines with a modular structure.

A hardware configuration consisting of an S7-1500 CPU as the IO controller and any connected IO devices represents a "PROFINET IO system master". This master is configured with a maximum configuration based on which various options can be derived for different standard machines, for example with different configuration variants of the IO system.

#### Greater flexibility at all levels

Standard machine projects have the following central characteristics:

- From one project (IO system master) with an engineered maximum configuration, different variants of a standard machine can be loaded (IO system options). The standard machine project covers all variants (options) of the IO system.
- An IO system option can be integrated in an existing network locally using simple tools.

Flexibility is provided in more ways than one:

- With suitable configuration, adaptation of the IP address parameters of the IO controller is possible locally using simple tools. This allows a standard machine to be integrated in different plants with little effort or to be included in a network several times.  
  IO systems with this property are known as **multiple use IO systems**.
- With suitable configuration and programming, different setups of IO system options can be operated locally that differ in terms of the selection of IO devices used or in terms of the arrangement of the IO devices.  
  Since the specific configuration of the IO system is controlled by the user program, this is known as **configuration control for IO systems**.
- Independently of the functions described above, with suitable configuration and programming, you can use different station options of central devices or distributed I/O devices in one project. The devices can be different in terms of the selection and arrangement of the modules.  
  Since the concrete configuration of the station is controlled by the user program, this is also known as **configuration control**.

### Multiple use PROFINET IO systems

This section contains information on the following topics:

- [What you should know about multiple use IO systems](#what-you-should-know-about-multiple-use-io-systems)
- [Configuring a multiple use IO system](#configuring-a-multiple-use-io-system)
- [Adapting the IO system locally](#adapting-the-io-system-locally)
- [Permit overwriting of PROFINET device name](#permit-overwriting-of-profinet-device-name)

#### What you should know about multiple use IO systems

##### Multiple use automation solutions

For a flexible reusable automation solution as is the case with series machines, the following use cases are typical:

- The machine (and therefore also the PROFINET IO system) is used more than once by the customers.
- The machine is used in different plants by various customers.

For this to be possible, the automation solution must meet the following requirements:

- A configuration and program can be loaded on various machines of the same type without changes.
- Only a few easy adaptations are needed locally to integrate the machine into an existing network infrastructure.

The following figure shows how an automation solution with a multiple use IO system is loaded on different automation systems and then one automation system is adapted to the existing network infrastructure locally.

![Multiple use automation solutions](images/61585622923_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Load configuration with multiple use IO system |
| ② | Set IP address and device name locally on the IO controller |

##### Principle

The automation components for a machine include a PROFINET IO system, consisting of an IO controller (PROFINET interface of a CPU) and the IO devices assigned to it.

With the "Multiple use IO system" setting for the IO system, you turn a STEP 7 project into a "Standard machine project".

The "Multiple use IO system" setting triggers various settings and checks of the configuration by STEP 7. The settings ensure that the IO system is self-contained and there are no dependencies on components outside the IO system.

##### Requirement

- STEP 7 V13 or higher
- S7-1500 CPU or ET 200SP CPU as of firmware version V1.5 as IO controller

##### Rules

The following rules apply to a multiple use IO system:

- No IO device can be configured as Shared Device.
- The ports of the devices must be interconnected.

  Devices for which no port interconnection is configured, for example, interface module IM 154-6 IWLAN (ET200pro PN), cannot be operated with STEP 7 V13 as IO devices on a multiple use IO system.
- If an IO device in a multiple use IO system is an I-device (CPU as an "intelligent" IO device):

  If the I-device has a lower-level IO system, this lower-level IO system can be connected to the same PROFINET interface as the higher-level IO controller. However, only one of the two IO systems supports multiple use according to the following rule:

  "Parameter assignment of PN interface by higher-level controller" (on I-device) = **yes**: Multiple use higher-level IO system.

  "Parameter assignment of PN interface by higher-level controller" (on I-device) = **no**: Multiple use lower-level IO system.

  ![Rules](images/70929311115_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | I-device in multiple use IO system. The PROFINET interface is operated as IO device. |
  | ② | A lower-level IO system on the I-device is also connected to this PROFINET interface. |
- If MRP (Media Redundancy Protocol) is configured:

  - All IO devices on the multiple use IO system must belong to the same MRP domain.
- If IRT (Isochronous Real Time) is configured:

  - All IO devices in multiple use IO systems must belong to the same sync domain.
  - The sync domain must not include any other IO devices.
- IE/PB links cannot be operated as IO device with STEP 7 V13 in a multiple use IO system.

  IE/PB Links with firmware version V3 or higher can be operated in a multiple use IO system with STEP 7 V13 SP1 or higher.

##### Configuration

You specify whether or not a configuration can be used multiple times in the properties of the IO system.

All other parameter settings for the configured devices are then set automatically by STEP 7 and checked during compilation.

##### Boundary conditions

To prevent a standard machine project from having dependencies on other devices outside of the machine, observe the following:

- A standard machine project consists of an IO controller and the corresponding IO devices. You should therefore configure only one CPU as IO controller and the corresponding IO devices in the standard machine project.
- Do not use two-ended connections for the communication. Instead, use only one-ended connections or unspecified connections if necessary.

  Background: To configure the communication in a STEP 7 project, it is always possible to set the IP address parameters in the project. For multiple use IO systems, however, this strategy is not possible since the IP address parameters of the IO controller and the assigned IO devices are assigned locally. At the time of the configuration, the IP address parameters are therefore unknown.

  If you nevertheless want to configure communication with devices on PROFINET, for example with a central coordinator, you can only use communications mechanisms that allow dynamic assignment of the IP address parameters in the user program.

  Example: Open User Communication

  If, for example, the device is configured as an active end point (initiator of the connection), the IP address parameters can be stored, for example, in a data block. You then supply the data block with the currently valid IP address parameters during commissioning. For this dynamic type of IP address parameter assignment, there is no system support; in other words, if you change the configuration of the system, the IP address parameters are not automatically adapted.

  You will find a description of handling instructions for Open User Communication under this keyword in the STEP 7 online help.

---

**See also**

[Unspecified connections (S7-300, S7-400, S7-1500)](Connections%20-%20Purpose%20and%20selection.md#unspecified-connections-s7-300-s7-400-s7-1500)
  
[Basic information on communication via the PUT/GET instruction](Configuring%20devices%20and%20networks.md#basic-information-on-communication-via-the-putget-instruction)
  
[Specifying an unspecified connection](Configuring%20connections.md#specifying-an-unspecified-connection)
  
[Creating a new connection - overview](Configuring%20connections.md#creating-a-new-connection---overview)

#### Configuring a multiple use IO system

##### Requirement

- S7-1500 CPU firmware version V1.5 or higher as IO controller

##### Procedure

To create a standard machine project, follow these steps:

1. Create a project.
2. Configure an S7-1500 CPU firmware version V1.5 or higher as IO controller.
3. Configure the required IO devices and assign the IO devices to the IO controller.
4. Configure the port interconnection between the devices.
5. Select the IO system so that you can edit the properties in the inspector window.
6. Select the "Multiple use IO system" check box in the "General" area of the inspector window.

![Procedure](images/60445257483_DV_resource.Stream@PNG-en-US.png)

**Result**: The following settings are made by STEP 7:

- The device name of the IO controller (CPU) in the standard machine project is set to "Permit setting of PROFINET device name directly on the device". The IO controller (CPU) has no PROFINET device name initially.
- The IP protocol of the IO controller (CPU) is permanently set to "IP address is set directly at the device". The CPU has no IP address initially.
- The "Support device replacement without exchangeable medium" option is selected automatically. This option enables automatic commissioning. A commissioning engineer does not have to assign device names to the IO devices locally. The IO controller assigns the device name and IP address to the IO devices based on the preset topology and other settings during startup.
- The device name of the IO devices is set to "Generate PROFINET device name automatically" (from the configured name of the IO device).
- The IP protocol of the IO devices is set to "IP address is set by the IO controller during runtime". The IO devices have no IP address initially. If an IO device is not a typical distributed I/O system (e.g., ET 200 systems), but rather another device such as an HMI device, change the option to "IP address is set directly at the device"; see below.
- The device number for the IO devices is automatically assigned and is used locally for making the IP address unique.

To allow the IO controller to make later changes to the device name for the operator, you must enable the CPU option "Permit overwriting of device names of all assigned IO devices" ("Advanced options &gt; Interface options" in the PROFINET interface properties).

This option is disabled by default.

The following figure shows the above-described settings for the IP address and PROFINET device name.

![Procedure](images/59287010443_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | After the configuration is loaded from the standard machine project, the IO controller has no device name and no IP address. |
| ② | Following loading, the IO devices have a device name and a device number but no IP address. |

##### How an IO device obtains an IP address locally

Below, you will find an explanation of the "IP address is set by the IO controller during runtime" and "IP address is set directly at the device" options, which can generally be configured for a multiple use IO system.

If you have set the "Multiple use IO system" option for the IO system, STEP 7 automatically sets the "IP address is set by the IO controller during runtime" option for the IO devices.

In this case, the IO controller assigns the IO device an IP address that results from the locally assigned IP address of the IO controller (see next section). This option is appropriate if the IO device is a field device, e.g., ET 200MP, ET 200SP, or another distributed I/O system.

If the IO device is not a "standard" field device, for example, an HMI device for a Windows operating system, the "IP address is set by the IO controller during runtime" option described above does not work. In this case, choose the "IP address is set directly at the device" option. You must then assign the IP address to the device locally and take steps to ensure that this address is suitable for the IP addresses of the other IO devices and the IP address of the IO controller.

---

**See also**

[Adapting the IO system locally](#adapting-the-io-system-locally)

#### Adapting the IO system locally

A few steps are needed to adapt the machine that was loaded with the standard machine project.

Only the device name and IP address of the IO controller must be adapted locally. The device names and IP addresses of the IO devices result from these adaptations. In this example, the effects of local settings are described for two specific machine modules.

The on-site settings are possible, for example, with the CPU display, commissioning tools such as SINEC PNI Basic (Primary Network Initialization) or PRONETA. You do not need a programming device with STEP 7 to make these settings.

##### Requirement

- The machine was loaded with a standard machine project (see [Configuring a multiple use IO system](#configuring-a-multiple-use-io-system)).
- The display is ready for operation or the required tool for assigning the IP address and device name is available (e.g. SINEC PNI Basic, STEP 7).
- The ports of the IO controller and IO devices are interconnected according to the configuration.

##### Procedure

Observe the boundary conditions and instructions for commissioning an S7-1500. Refer to "See also" for a reference to the S7-1500 system manual in which commissioning is described.

To adapt a standard machine locally, follow these steps:

1. Integrate the machine into the network.
2. Connect the device for assigning the IP address and device name to the CPU, for example a PG/PC with the appropriate software.
3. Assign the desired device name and IP address to the IO controller.

The IO controller (CPU) then assigns the adapted PROFINET device name and a unique IP address to the IO devices.

The following rules apply to the assignment:

- The device names of the IO devices are formed by chaining together the following name components, separated by a period:

  &lt;configured name of the IO device from the standard machine project&gt;.&lt;name of the associated IO controller set on the device&gt;
- The IP addresses of the IO devices result from the locally configured IP address of the associated IO controller and the device number (sum).

> **Note**
>
> Make sure that duplicate IP addresses cannot be created on the subnet during the assignment. The IO controller does not assign a new IP address in this case.

In the following figure, the device name "m1" and the IP address 192.168.1.10 have been assigned to the IO controller of the first machine.

The device name "m2" and the IP address 192.168.1.20 has been assigned for the second machine.

Refer to the figure for the resulting device names and IP addresses.

![Procedure](images/59287013643_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Set device name and IP address on the IO controller |
| ② | After startup, the IO devices have an updated device name (&lt;configured device name&gt;.&lt;device name of IO controller&gt;) and an adapted IP address (= &lt;IP address of IO controller&gt; + &lt;device number&gt;) |

---

**See also**

[Configuring a multiple use IO system](#configuring-a-multiple-use-io-system)
  
[S7-1500 system manual](http://support.automation.siemens.com/WW/view/en/59191792)

#### Permit overwriting of PROFINET device name

With S7-1500 CPUs as of firmware version V1.5, you can overwrite PROFINET device names of IO devices during the startup of the CPU. This option reduces the effort during automatic commissioning, for example, when replacing a device.

##### How the "Permit overwriting of device names of all assigned IO devices" option works

The IO controller (CPU) can overwrite the PROFINET device names of IO devices in the IO system when the "Permit overwriting of PROFINET device names of all assigned IO devices" option is enabled.

Multiple use IO systems can only be operated when this option is enabled. The IO controller checks prior to overwriting if the type of the IO device matches the configured type.

If the option is not selected, the IO controller cannot overwrite the device names of the IO devices. In this case, you must manually assign the PROFINET device name on the IO device if the PROFINET device name changes in the configuration or when a device is replaced, or delete the device names of the IO devices prior to an automatic commissioning.

If the "Permit overwriting of device names of all assigned IO devices" option is not selected, the IO controller cannot overwrite the device names of the IO devices. In this case, you must manually assign the PROFINET device name on the IO device if the PROFINET device name changes in the configuration or when a device is replaced, or delete the device names of the IO devices prior to an automatic commissioning.

##### Response during commissioning

Select the option "Permit overwriting of PROFINET device names of all assigned IO devices" only if the following requirements are fulfilled:

- All configured IO devices are available.
- All IO devices are wired correctly in accordance with the topology configuration.
- No IO device is jumpered.

If configured IO devices are missing or are jumpered (partial commissioning), do not use the option.

You can also use this option for serial machine projects, where you afterwards adapt the configuration via ReconfigIOSystem. Note that the valid configuration is always the one that was transferred to the IO controller in the control data set using the ReconfigIOSystem Mode:=2 instruction. As soon as you activate reconfiguration with ReconfigIOSystem Mode:=3, the PROFINET device names are overwritten as defined in the data record.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Error after partial commissioning**  If device names are assigned incorrectly during partial commissioning or incorrect wiring, these have to be deleted manually after a correction of the wiring in order to attain correct assignment of the device names. |  |

##### Behavior during operation

As soon as you exchange a device, the new device is overwritten with the configured PROFINET device name.

The PROFINET device name is not overwritten if the MAC address of the IO device is already actively used in the project.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Wrong PROFINET device name**  When the "Permit overwriting of PROFINET device names of all assigned IO devices" option is enabled, incorrectly connected devices can be assigned an incorrect PROFINET device name from the configuration.  Depending on the connected I/O, there is risk of death, severe injuries or damage caused by malfunctions.  To rule out any danger, check whether the right replacement device has been connected in the case of a device replacement and whether the port interconnection matches the configured preset topology. |  |

##### Typical source of danger

When replacing an IO device ("standard case"), it is almost guaranteed that the replaced device will be connected according to the configured port interconnection.

The figure below shows a scenario whereby the connections of two identical PROFINET cables are swapped at two switch ports. Because the IO controller assigns the device names according to the preset topology, the incorrect connection of the devices has serious effects on the naming.

Due to the control of different actuators, the plant could become hazardous in this case.

![Typical source of danger](images/60814181131_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Switch with connected PROFINET cables |
| ② | Device A, device name "IOD-1": controls motor 1 |
| ③ | Device B, device name "IOD-10": controls motor 10 |
| ④ | Device A controls motor 10 |
| ⑤ | Device B controls motor 1 |

##### Procedure

Proceed as follows to change the "Permit overwriting of device names of all assigned IO devices" option:

1. Select the PROFINET interface of the CPU for which you want to change the option in the network view or in the device view.
2. Select "Advanced options &gt; Interface options".
3. Change the option.

---

**See also**

[Enabling device replacement without exchangeable medium](Configuring%20devices%20and%20networks.md#enabling-device-replacement-without-exchangeable-medium)

### Configuration control (option handling) for PROFINET IO systems

This section contains information on the following topics:

- [Information about configuration control of IO systems](#information-about-configuration-control-of-io-systems)
- [Configuring IO devices as optional](#configuring-io-devices-as-optional)
- [Enabling optional IO devices in the program](#enabling-optional-io-devices-in-the-program)
- [Configuring flexible order of IO devices](#configuring-flexible-order-of-io-devices)
- [Customizing arrangement of IO devices in the program](#customizing-arrangement-of-io-devices-in-the-program)
- [System behavior and rules](#system-behavior-and-rules)

#### Information about configuration control of IO systems

Configuration control of IO systems makes it possible to generate several concrete versions of a standard machine from a standard machine project.

You are given the flexibility to vary the configuration of an IO system for a specific application as long as the real configuration can be derived from the set configuration. The configured configuration therefore represents the superset of all real configurations that can be derived from it.

The following figure shows an example of how two PROFINET IO systems with a different number of IO systems arise from one standard machine project.

![Figure](images/71430583947_DV_resource.Stream@PNG-en-US.png)

In the following sections, you find a description of how to configure and program a PROFINET IO system to commission, for example, a standard machine on-site without using configuration software.

##### Concept

The principle of configuration control is already known at the device level for the flexible use of submodules/modules ("option handling"). Different configurations can be derived from one engineering project both for central as well as for distributed I/O.

With S7-1500 CPUs as of firmware version V1.7, this principle can also be applied at the IO system level. You have the option of omitting, adding or changing the order of stations (IO devices) of a PROFINET IO system in a specific plant.

Configuration control for devices and configuration control for IO systems can be combined; the functions are independent of each other.

It is possible to operate variants deviating from a maximum configuration of an IO system. In a standard machine project, you can prepare a kit of IO devices which can be flexibly customized for various configurations using configuration control.

The following variations are available:

- Variation of the number of IO devices involved

  You include optional IO devices for the configuration control in the configuration by transferring a suitable data record with the required configuration in the user program.
- Variation of the order of IO devices involved

  You adapt the port interconnection of the IO devices to the topology being used by transferring a suitable data record with the required topology in the user program.

The following figure shows how you operate two different configurations with an IO device marked as optional in the network view of STEP 7:

- Configuration without the optional IO device:

  In this case, you use the instruction "ReconfigIOSystem" to transfer a data record to the PROFINET interface containing the information that no optional IO device is to be included in the configuration.
- Configuration with the optional IO device:

  In this case, you use the instruction "ReconfigIOSystem" to transfer a data record to the PROFINET interface adding the optional IO device to the configuration.

![Concept](images/71336997515_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Determined through parameter assignment: IO Device_2 is optional IO device |
| ② | Configuration without the optional IO device |
| ③ | Configuration with the optional IO device |

##### Summary: The procedure in principle

The following phases are distinguished when it comes to the implementation of a standard machine concept:

1. Engineering phase: Creating a standard machine project and loading into specific machine or plant:

   - Completely configuring all IO devices (options) ever required in a specific machine or plant
   - Configuring as optional those IO devices that will be omitted in specific machines or plants
   - Preparing user program with the possibility of selecting on-site the actually existing configuration via switch or HMI device
2. Commissioning phase: Preparing specific machine or plant for operation:

   - Integrating machine or plant in the on-site network (see [Adapting the IO system locally](#adapting-the-io-system-locally))
   - Selecting the currently existing configuration of the IO system via configured option

---

**See also**

[ReconfigIOSystem: Reconfigure IO system (S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#reconfigiosystem-reconfigure-io-system-s7-1500)
  
[Important information regarding configuration control (option handling) (S7-1200)](Configuring%20automation%20systems.md#important-information-regarding-configuration-control-option-handling-s7-1200)
  
[Configuration control (option handling) for central S7-1500 (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#configuration-control-option-handling-for-central-s7-1500-s7-1500-s7-1500t)

#### Configuring IO devices as optional

##### Requirement

- S7-1500 CPU firmware version V1.7 or higher as IO controller
- STEP 7 V13 SP1 or higher
- The [rules](#system-behavior-and-rules) for the establishment and operation of a standard machine project have been considered.

##### Port interconnection for optional IO devices

As of STEP 7 V15.1, port interconnection is not necessary for optional IO devices.

A port interconnection between the devices of the IO system that you want to customize with the user program is mandatory in the following cases.

- You have configured IRT.
- You have configured MRP.
- You are using STEP 7 &lt;= V15.

##### Procedure

To configure an IO device as optional IO device, proceed as follows:

1. Create a project.
2. Configure an S7-1500 CPU firmware version V1.7 or higher as IO controller.
3. Configure the required IO devices and assign the IO devices to the IO controller.
4. Select the IO device you want to mark as optional.
5. Select the area "PROFINET interface [X1] &gt; Advanced options".
6. Enable the "Optional IO device" option.

   ![Procedure](images/70435156235_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70435156235_DV_resource.Stream@PNG-en-US.png)
7. Repeat steps 4 to 6 for all IO devices to be configured as optional.
8. Load the configuration onto the CPU.

**Result**: Once this configuration is loaded, the system behavior is as follows:

- The CPU is prepared for the configuration control of the IO system.
- All IO devices are disabled.
- Irrespective of whether you customize the configuration with the user program (adding optional IO devices) or make no changes to the loaded configuration: You must call the instruction "ReconfigIOSystem" in the user program and notify the current configuration to the system!

  The system will not be operational without calling the instruction "ReconfigIOSystem".

  For further information on the proceeding see [Enabling optional IO devices in the program](#enabling-optional-io-devices-in-the-program).

##### Fast parameter assignment in the "I/O communication" table

You can also specify whether or not an IO device is optional in the "I/O communication" tab.

In an additional "Optional IO-Device" column, a selectable check box is available for each IO device that indicates whether or not an IO device is optional. Here, you can adjust the setting centrally.

---

**See also**

[ReconfigIOSystem: Reconfigure IO system (S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#reconfigiosystem-reconfigure-io-system-s7-1500)

#### Enabling optional IO devices in the program

##### Requirement

- CPU S7-1500 firmware version V1.7 or higher as IO controller.
- STEP 7 V13 SP1.
- At least one IO device was configured as optional IO device.
- The [rules](#system-behavior-and-rules) for the establishment and operation of a standard machine project have been considered.

##### Procedure

Please note the information on and rules for commissioning an S7-1500 system in the documentation for SIMATIC S7-1500!

The following description of the proceeding only includes steps required to understand the program-controlled activation of an optional IO device.

To activate or deactivate optional IO devices, include them in the configuration and activate them in the user program, follow these steps:

1. Create a data record as described [here](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#reconfigiosystem-reconfigure-io-system-s7-1500).
2. Call the instruction "ReconfigIOSystem" and select mode 1 to deactivate all IO devices.

   If you set the CPU to STOP or POWER OFF state in order to modify the plant in this status (for example to add an optional IO device), explicit deactivation using "ReconfigIOSystem" with mode 1 is not necessary. In this case, i.e. following a STOP-RUN transition and following a POWER-OFF &gt; POWER-ON transition, all IO devices are deactivated automatically.
3. When you have brought the plant to a safe status that allows restructuring without any danger:

   Put the plant together according to your intended application. Add the required optional IO devices at the points at which you planned this in the configuration (observe the order!) or remove optional IO devices that you no longer require.
4. Cable the IO devices.
5. Startup the S7-1500 system and call again the instruction "ReconfigIOSystem". Select mode 2 to transfer the data record CTRLREC.
6. Following successful transfer of the data record, call again the instruction "ReconfigIOSystem". Select mode 3 to activate all IO devices forming part of the current configuration.

##### Result

The CPU activates the following IO devices:

- All IO devices that you have not set as optional IO devices.
- All optional IO devices listed in the control data record (CTRLREC).

The following IO devices remain disabled:

- Docking units (IO devices changing during operation).
- Optional IO devices that are not listed in the control data record.

> **Note**
>
> Call the instruction "ReconfigIOSystem" in all modes with the same control data record (CTRLREC)!
>
> If you use different data records in the different modes, this results in an inconsistent customization of the configuration and thus to rather incomprehensible error messages.

##### Example: Data record structure for the activation of an IO device

The IO device "IO-Device_2" is to be activated as the only IO device in the user program. To do this, you only require the hardware identifier of "IO-Device_2.

Recommendation: Use the system constants of the hardware identifiers instead of the absolute values as shown in this example. With this procedure, the content of the DB is not influenced by changes to the hardware identifiers as the result of changes to the configuration.

The data record is to be stored in a data block and to be transmitted to the PROFINET interface of the IO controller in the user program using the instruction "ReconfigIOSystem".

![Example: Data record structure for the activation of an IO device](images/71337009419_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | IO device_2 is configured as optional IO device. |
| ② | Once the data record is transmitted and the configuration is activated using the instruction "ReconfigIOSystem" IO device_2 is included in the configuration and participates in the data exchange with the IO controller. |

##### Creating data block

In this example, the control data record is created in a data block. The data block is structured as follows:

Line 2: Array definition: Array of type Word with 4 elements. Array of Word is permitted as the data type.

Line 3: Version of the data record (currently: V1.0).

Line 4: Number of optional IO devices to be activated (here: 1).

Line 5: List of the hardware identifiers of the IO devices, inserted here as a system constant.

Line 6: Number of port interconnections that are set in the user program (here: 0).

Line 7: Additional data records (optional).

![Creating data block](images/71339017867_DV_resource.Stream@PNG-de-DE.png)

##### Rules for the call sequence of "ReconfigIOSystem"

- Always supply the instruction "ReconfigIOSystem" with the same control data record (CTRLREC input parameter)!
- Call sequence following POWER OFF -&gt; POWER ON transition:

  - ReconfigIOSystem call with mode 1 (optional).
  - ReconfigIOSystem call with mode 2 (mandatory, even without previous reconfiguration!).
  - ReconfigIOSystem call with mode 3 (mandatory).
- Call sequence following STOP &gt; RUN transition:

  - ReconfigIOSystem call with mode 1 (optional).
  - ReconfigIOSystem call with mode 2 (mandatory, even when configuration was modified in STOP state). Otherwise not required).
  - ReconfigIOSystem call with mode 3 (mandatory).
- Call sequence for reconfiguration in RUN state:

  - ReconfigIOSystem call with mode 1 (mandatory).
  - ReconfigIOSystem call with mode 2 (mandatory).
  - ReconfigIOSystem call with mode 3 (mandatory).

##### Explanations and recommendations concerning the rules

- If you do not list an IO device to be configured as optional IO device in the control data record or data block, this IO device does not form part of the configuration and does not take part in data exchange with the CPU.
- If you do not activate any optional IO device at all and work with the loaded configuration without reconfiguration, you still have to follow the proceeding described in the above section and transmit the control data record to the CPU.

  The control data record has the simple structure with the following tags:

  - Version (High Byte =1, Low Byte = 0)
  - Number of optional devices to be activated = 0
  - Number of port interconnections that are set in the user program = 0
- Following a STOP &gt; RUN transition and following a POWER-OFF &gt; POWER-ON transition, all IO devices are deactivated automatically. For this reason, no ReconfigIOSystem call with mode 1 is required for configuration control to function properly.

  If you use your project as a universally valid sample for programming the configuration control, we still recommend to perform the ReconfigIOSystem call with mode 1 prior to any reconfiguration. This way, the sample can also be used for reconfigurations in RUN mode.
- Commissioning extensive I/O systems (more than 8 optional IO devices) while using IRT at the same time:

  To keep the startup times short when activating the optional IO devices (ReconfigIOSystem, mode 3), note the following tip: Check the device numbers of the IO devices. The device numbers should follow the topological interconnection starting at the IO controller in ascending order. The further an IO device is from the IO controller topologically, in other words the more IO devices there are between the IO controller and the IO device in question, the higher the device number should be.

  You set the device numbers in the "Ethernet addresses - PROFINET" area in the Inspector window with the PROFINET interface selected.

  Example of the assignment of device numbers with a linear topology:

  ![Explanations and recommendations concerning the rules](images/71972797067_DV_resource.Stream@PNG-de-DE.png)
- The CPU processes the "ReconfigIOSystem" instruction for asynchronous transfer of the control data record.

  When you call the instruction in the startup program, you must therefore call "ReconfigIOSystem" repeatedly in a loop repeatedly until the "BUSY" or "DONE" output parameter indicates that the data record is transferred.

  Tip: Use the SCL programming language with the REPEAT ... UNTIL instruction for programming the loop.

  `REPEAT`

  `"ReconfigIOSystem"(REQ := "start_config_ctrl",`

  `MODE := 1,`

  `LADDR := 64,`

  `CTRLREC := "myCTRLREC".ArrMachineConfig0,`

  `DONE => "conf_DONE",`

  `BUSY => "conf_BUSY",`

  `ERROR => "conf_ERROR",`

  `STATUS => "conf_STATUS");`

  `UNTIL NOT "conf_BUSY"`

  `END_REPEAT;`

##### Additional information

For information on the basic structure of the data record and on using the instruction "ReconfigIOSystem" see [here](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#reconfigiosystem-reconfigure-io-system-s7-1500).

---

**See also**

[Configuring IO devices as optional](#configuring-io-devices-as-optional)

#### Configuring flexible order of IO devices

The following section shows how you can create the conditions required to change the order of IO devices in a PROFINET IO system.

This function is also supported with optional IO devices. For simplicity, a maximum configuration without optional IO devices is shown below.

##### Concept

A typical application for a standard machine project consists of composing an entire plant from a set of various plant units which only differ with respect to the different arrangement of the units, e.g. in the case of transport systems. Each plant unit consists of a functional unit of mechanics (rails or conveyor belts) and electrics (power supply, IO device with IO modules, sensors, actuators, motors, PROFINET port for data exchange with central control ...).

The following figure shows how, simply by exchanging two rail segments, a new transport system is created that is adapted with an upstream points to the local conditions.

![Concept](images/68659536523_DV_resource.Stream@PNG-de-DE.png)

Interesting from the automation viewpoint is the implementation of a flexible order of individual IO devices in a project that is not to be modified any more on-site.

The order of the IO devices is determined by the port interconnection. For each IO device, you define in the port properties the partner port and thus the neighboring device connected at the respective local port. If the partner port is to be defined by the user program, the option "Partner set by user program" is to be selected as partner port.

The figure below shows the initial configuration of the transport system shown above, which is to permit the order of the connected IO devices to be changed via the user program. In the example, the order of IO-Device_2 and IO-Device_3 is to be controlled via the user program.

![Concept](images/71339116683_DV_resource.Stream@PNG-de-DE.png)

To determine how the partner port settings are to be selected, you must note for each device and each port of a device which partner can be interconnected.

- If the partner is always the same in the different configurations provided, you select the partner port for this partner.
- If the partners vary in the different configurations, you select "Setting partner by user program".

For the example in the figure above, the following port settings result:

| Device | Local port | Partner port setting | Explanation |
| --- | --- | --- | --- |
| PLC_1 | p1 | p1 (IO device_1) | Partner of PLC_1 at port 1 is IO device_1 (always) |
| IO device_1 | p1 | p1 (PLC_1) | Partner of IO device_1 at port 1 is PLC_1 (always) |
| IO device_1 | p2 | Partner is set by user program | Partner of IO device_1 at port 2 is either IO device_2 or IO device_3 =&gt; Setting partner by user program |
| IO device_2 | p1 | Partner is set by user program | Partner of IO device_2 at port 1 is either IO device_1 or IO device_3 =&gt; Setting partner by user program |
| IO device_2 | p2 | Partner is set by user program | Partner of IO device_2 at port 2 is either IO device_3 or IO device_4 =&gt; Setting partner by user program |
| IO device_3 | p1 | Partner is set by user program | Partner of IO device_3 at port 1 is either IO device_2 or IO device_1 =&gt; Setting partner by user program |
| IO device_3 | p2 | Partner is set by user program | Partner of IO device_3 at port 2 is either IO device_4 or IO device_2 =&gt; Setting partner by user program |
| IO device_4 | p1 | Partner is set by user program | Partner of IO device_4 at port 1 is either IO device_3 or IO device_2 =&gt; Setting partner by user program |
| IO device_4 | p2 | any partner | no partner planned at port 2 |

##### Requirement

- S7-1500 CPU firmware version V1.7 or higher as IO controller.
- STEP 7 V13 SP1 or higher.
- The [rules](#system-behavior-and-rules) for the establishment and operation of a standard machine project have been considered.

##### Procedure

To set the partner port for a program controlled interconnection, proceed as follows:

1. Select the PROFINET interface of the device (IO controller or IO device) whose port you want to set.
2. In the properties of the PROFINET interface, select the area "Port interconnection" (Extended options &gt; Port [...] &gt; Port interconnection).
3. From the drop-down list, select "Setting partner by user program" as partner port.
4. Repeat steps 1 to 3 for each port to be interconnected via the user program.

---

**See also**

[Customizing arrangement of IO devices in the program](#customizing-arrangement-of-io-devices-in-the-program)

#### Customizing arrangement of IO devices in the program

##### Requirement

- CPU S7-1500 firmware version V1.7 or higher as IO controller.
- At least one partner port was configured as "Partner set by user program".
- The [rules](#system-behavior-and-rules) for the establishment and operation of a standard machine project have been considered.

##### Procedure

The proceedings corresponds to the proceeding for activating optional IO devices.

Only the structure of the data record must be extended for the program-controlled assignment of the ports. The extension is described in the following sections.

##### Example: Data record structure for the assignment of partner ports

For the data record structure, you need the HW identifications of the ports.

The data record is to be stored in a data block and to be transmitted to the PROFINET interface of the IO controller in the user program using the instruction "ReconfigIOSystem".

As the input parameter RECORD of the instruction "ReconfigIOSystem" is of the VARIANT data type, you first have to create a data type for the data block.

In the following sections, you find a description of the structure of the PLC data type as well as of the structure of the data block based on this type.

##### Selecting derived configuration

For the following selected configuration it is shown below what the data record must look like so that the IO devices are interconnected in the planned order by the user program.

![Selecting derived configuration](images/71340792587_DV_resource.Stream@PNG-de-DE.png)

This example is based on the flexible configuration from the [previous section](#configuring-flexible-order-of-io-devices)  with the settings for the respective partner ports described there.

The partner ports in the specific derived configuration have been defined so that it is possible to name the HW identifications of the ports involved.

The following table only contains those devices whose ports can be defined by the user program. Only these devices are relevant for the data record structure.

| Device | Local port | Partner port setting | Partner port of the selected configuration |
| --- | --- | --- | --- |
| IO device_1 | p2 = Port 2   HW identifier: 251 | Partner is set by user program | Port 1 of IO device_3  HW identifier: 261 |
| IO device_2 | p1 = Port 1  HW identifier: 281 | Partner is set by user program | Port 2 of IO device_3   HW identifier: 291 |
| IO device_2 | p2 = Port 2  HW identifier: 311 | Partner is set by user program | Port 1 of IO device_4   HW identifier: 321 |

##### Creating data block

For the derived configuration, the structure of the data block "DB-IO-SYSTEM-Port-Interconnections" is explained as an example.

This data block is used when calling the instruction "ReconfigIOSystem" at input parameter "CTRLREC".

Instead of the absolute values for the hardware identifiers of the ports, the system constants of the hardware identifiers are used here.

The data block is structured as follows:

Line 2: Declaration of an Array of Word (only this data type is possible).

Line 3: Version of the control data record: V1.0.

Line 4: Number of optional IO devices: 0.

Line 5: Number of specified port interconnections: 3.

Line 6: Port interconnection 1, local port.

Line 7: Port interconnection 1, partner port.

Line 8: Port interconnection 2, local port.

Line 9: Port interconnection 2, partner port

Line 10: Port interconnection 3, local port.

Line 11: Port interconnection 3, partner port.

![Creating data block](images/71920426379_DV_resource.Stream@PNG-de-DE.png)

##### Interconnection not listed in data block

If the partner port was configured as "Setting partner by user program" in the port properties and this port is not listed in the data record or data block resp., then the CPU sets this port to the setting "any partner". If no data record is transmitted at all, the CPU sets this "any partner" setting for all program-controlled assignments.

The "any partner" setting is not valid for IRT configurations.

##### Additional information

For information on the basic structure of the data record and on using the instruction "ReconfigIOSystem" see [here](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#reconfigiosystem-reconfigure-io-system-s7-1500).

#### System behavior and rules

Below, you find a description of how an IO system whose configuration is controlled by the user program behaves in operation.

In addition, rules and restrictions are listed here which must be considered when configuring the maximum structure of the configuration in a standard machine project.

##### System behavior

- System diagnostics:

  From the system diagnostics viewpoint (online view or Online &amp; Diagnostics) a deactivated IO device is shown as "deactivated".
- Topology view:

  Offline view: As configured. No interconnection is shown for ports with partner ports configured as "Setting partner by user program".

  Online view: Ports and interconnections with deactivated IO devices are shown in a different shade of green as error-free ports and interconnections of activated IO devices.
- Representation in the Web server:

  The names of devices are shown as configured (Properties &gt; General &gt; Project information).

  The assigned PROFINET device name for the CPU is shown on the "Communication" website, at the "Parameter" tab.

  IP address parameters: Currently assigned IP address parameters are shown on the site "Module state".

  Topology: The current topology resulting from any customizations via user program is shown in the Web server. IO devices configured as optional are shown as "deactivated" IO devices in the Web server.

##### Rules

The rules for standard machine projects as described [here](#what-you-should-know-about-multiple-use-io-systems) apply.

For configuration-controlled IO systems, the following additional rules apply:

- When configuring MRP (Media Redundancy Protocol):

  The ports configured as ring ports must not be interlinked via user program.

  However, devices with ring ports (devices of an MRP domain) can be optional IO devices.
- When configuring docking stations (= IO devices changing during operation):

  Neither the docking station nor the first IO device of a docking unit may be optional IO devices.

  The ports of the docking units must not be interlinked via user program.
- When configuring IRT:

  The order of synchronized IO devices ("IRT devices") must be defined by the configuration and must not be changed in the different variants of a standard machine. For this reason, the ports of the IRT devices must not be interlinked via user program.

  However, you have the possibility to configure IRT devices as optional IO devices.

  You also have the option to interconnect, by user program, RT devices that are, for example, separated from this line by a switchport (see figure).

  ![Rules](images/71936679307_DV_resource.Stream@PNG-de-DE.png)
- If you configure fixed port connections to its partners for the optional IO device:   
  An optional IO device can have max. 2 fixed port connections.   
  If you configure more fixed port connections, the resulting port connection is no longer clearly defined with disabled IO device.   
  Example: An optional IO device "Optional_IOD" has fixed port connections to "PLC_1", to "IO-Device_3" and to "IO-Device_4" (invalid configuration). If the IO device "Optional-IOD" is omitted, there are 2 port connection possibilities (① and ②) through bridging of the disabled optional IO device; see the following figures.

  ![Rules](images/149272207371_DV_resource.Stream@PNG-de-DE.png)

  ![Rules](images/149272216331_DV_resource.Stream@PNG-de-DE.png)

  ![Rules](images/149237581579_DV_resource.Stream@PNG-de-DE.png)

## Performance upgrade

This section contains information on the following topics:

- [Introduction](#introduction)
- [Dynamic frame packing](#dynamic-frame-packing)
- [Fragmentation](#fragmentation)
- [Fast forwarding](#fast-forwarding)
- [Configuration of IRT with high performance](#configuration-of-irt-with-high-performance)
- [Sample configuration for IRT with high performance](#sample-configuration-for-irt-with-high-performance)

### Introduction

#### Performance upgrade

The performance upgrade implements the application class "High Performance" of the PROFINET specification V2.3.

The performance upgrade provides a series of measures that lead to the following improvements for PROFINET with IRT:

- Reduction of runtime delays in the IO devices
- Increase in the bandwidth for cyclic IO data
- Reduction of the bandwidth used for PROFINET frames
- Reduction of the send clocks

The improvements achieved with the performance upgrade mean that you can operate your PROFINET IO system with more devices with the same send clock or the same number of devices with a shorter send clock.

With PROFINET, it was previously possible to reach a send clock of 250 µs.

With the performance upgrade, it is now possible to reach isochronous send clocks of up to 125 µs with the fast forwarding, dynamic frame packing and fragmentation procedures. With short send clocks, standard communication remains possible.

The performance upgrade will help you to implement applications with high speed and send clock requirements.

### Dynamic frame packing

#### Dynamic frame packing

Previously, individual PROFINET IO frames were sent for every PROFINET IO device.

The performance upgrade uses the dynamic frame packing procedure that is based on the summation frame method. With the summation frame method, a frame contains the user data for all nodes on a bus. With dynamic frame packing, every IO device takes its data from the frame and forwards the rest. The frame is shortened from IO device to IO device. Dynamic frame packing improves the use of the bandwidth in a line topology.

The following figure shows how dynamic frame packing works based on the example of a frame containing the user data for 3 IO devices.

![Dynamic frame packing](images/88100290827_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The PROFINET IO frame contains the user data for all 3 IO devices (green, blue and orange). |
| ② | The PROFINET IO frame reaches the first IO device. The IO device takes its user data (green) from the frame and forwards the remaining frame. |
| ③ | The PROFINET IO frame contains the user data for two IO devices (blue and orange). |
| ④ | The PROFINET IO frame reaches the second IO device. The IO device takes its user data (blue) from the frame and forwards the remaining frame. |
| ⑤ | The PROFINET IO frame contains the user data for one IO device (orange). |
| ⑥ | The PROFINET IO frame reaches the last IO device. The IO device saves the entire frame including user data (orange). |

#### DFP groups

Dynamic frame packing automatically groups IO devices that support the performance upgrade into DFP groups. To be grouped together in a DFP group. the IO devices must be located one after the other in a line and must have the same update time and watchdog time. As soon as a maximum frame size for the DFP group is exceeded or a maximum number of members for a DFP group is reached, dynamic frame packing automatically opens a new DFP group.

STEP 7 shows the DFP groups in "Domain management" &gt; "Sync domains" &gt; "Name of the sync domain" &gt; "Device" in the "IO devices" box.

![DFP groups](images/90655231371_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Dynamic frame packing with high watchdog times**
>
> If you set the parameter "Accepted update cycles without IO data" higher than 31, dynamic frame packing does not place this IO device in a DFP group.

### Fragmentation

#### Fragmentation

The transfer of a complete standard Ethernet frame with TCP/IP data takes up to 125 µs. This means that the cycle time for PROFINET IO data cannot be reduced by any desired amount.

The performance upgrade uses the fragmentation procedure, which breaks down TCP/IP frames into sub-frames. These frame segments are transferred to the target device over multiple send clocks; there they are reassembled to the original TCP/IP frame.

Fragmentation will reduce the cycle time to values of less than 250 µs. The bandwidth required for TCP/IP data is less in the shorter send clocks. The bandwidth use for cyclic IO data increases, which means you can transfer more cyclic IO data in the same time.

The following figure shows how fragmentation works.

![Fragmentation](images/88100304523_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | A standard Ethernet frame with TCP/IP data is at least 125 µs. |
| ② | In fragmentation, the standard Ethernet frame is divided into frame segments. |
| ③ | The frame segments are divided into multiple short send clocks. |

### Fast forwarding

#### Fast forwarding

To be able to decide whether a frame should be forwarded or used, a PROFINET IO device requires the frame ID. It previously took 1440 ns until the frame ID was present in the IO device.

The performance upgrade uses the fast forwarding procedure in which the frame ID is located nearer the front of the frame. The throughput time in the device is reduced to 320 ns.

With fast forwarding, the throughput time of the frame is reduced in your PROFINET IO system. This results in decisive performance advantages, particularly in line topologies, ring topologies and tree topologies.

The figure below compares the throughput of a PROFINET IO frame in an IO device with and without fast forwarding.

![Fast forwarding](images/88100318219_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start:  - Both PROFINET frames reach the IO device. The IO devices start to check the frames for the frame ID |
| ② | After 320 ns:  - Without fast forwarding: The IO device is still checking the PROFINET frame for the frame ID. - With fast forwarding: The IO device receives the frame ID from the PROFINET frame and forwards the frame. |
| ③ | After 1440 ns:  - Without fast forwarding: The IO device receives the frame ID from the PROFINET frame and forwards the frame. - The PROFINET frame with fast forwarding is "ahead" of the PROFINET frame without fast forwarding. |

### Configuration of IRT with high performance

High-end applications with IO communication require excellent performance in IO processing, for example in the control of wind turbines (converter control).

To use IRT communication with the highest performance in your PROFINET IO system, enable the option "Make 'high performance' possible".

When you enable the "Make 'high performance' possible" option, this has the following effects:

- You can set send clocks of 188 µs and 125 µs (with the CPU 1518).
- You can set more bandwidth use for cyclic IO data.
- You can use the option "Allows the use of 'fast forwarding'".

#### Requirements

- S7-1500 CPU as of firmware version V2.0

#### Enable the "Make 'high performance' possible" option.

Follow these steps to activate the "Make 'high performance' possible" option:

1. Select the PROFINET IO system in the network view of STEP 7.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "PROFINET" &gt; "Domain management" &gt; "Sync domains" &gt; "Name of the sync domain".
3. Enable the "Make 'high performance' possible" option.

   ![Enable the "Make 'high performance' possible" option.](images/90655235211_DV_resource.Stream@PNG-en-US.png)

#### Using more bandwidth for cyclic IO data

Requirement: The "Make 'high performance' possible" option is enabled.

To set more bandwidth for cyclic IO data for your PROFINET IO system, follow these steps:

1. Select your IO system in the network view of STEP 7.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "PROFINET" &gt; "Domain management" &gt; "Sync domains" &gt; "Name of the sync domain" &gt; "Details".
3. In the drop-down list, select "Maximum 90% cyclic IO data. Focus on cyclic IO data".

   ![Using more bandwidth for cyclic IO data](images/90655239051_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Bandwidth usage in isochronous mode**
>
> If you operate your PROFINET IO system in isochronous mode, avoid using the setting for the bandwidth usage "Maximum 90% cyclic IO data. Focus on cyclic IO data."

#### Setting low send clocks

Requirement: The "Make 'high performance' possible" option is enabled.

1. Select the PROFINET IO system in the network view of STEP 7.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "PROFINET" &gt; "Domain management" &gt; "Sync domains" &gt; "Name of the sync domain".
3. Select the send clock for "Send clock" in the drop-down list.

   ![Setting low send clocks](images/90655242763_DV_resource.Stream@PNG-en-US.png)

#### Requirements for the fragmentation process (CPU 1518-4 PN/DP)

If you use the following combinations for send clock and bandwidth settings, the devices in the IO system use the fragmentation process:

- Send clock cycle 125 µs: Always fragmentation irrespective of the bandwidth setting.
- Send clock cycle 188 µs: Fragmentation with the bandwidth settings "Maximum 50% cyclic IO data. Balanced proportion." and "Maximum 90% cyclic IO data. Focus on cyclic IO data."

The PROFINET IO interface of the controller supports fragmentation if all the ports except one are deactivated.

#### Allow fast forwarding

Requirements:

- The PROFINET IO device has to support the fast forwarding procedure.
- The "Make 'high performance' possible" option is enabled.
- The PROFINET IO interface supports fast forwarding if all the ports except one are deactivated.

Follow these steps to allow fast forwarding:

1. Select the PROFINET IO system in the network view of STEP 7.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "PROFINET" &gt; "Domain management" &gt; "Sync domains" &gt; "Name of the sync domain".
3. Enable the "Allows the use of ‘fast forwarding'" option.

> **Note**
>
> **Fast forwarding and IPv6**
>
> The operation of fast forwarding in combination with IPv6 is not supported.
>
> As soon as an IO device in the subnet uses an IPv6 address, you must not activate "fast forwarding".

#### Optimizing port settings for low send clocks

You can further optimize the bandwidth use in your PROFINET IO system by using cables with a length of &lt; 20 m between the devices or by setting a low signal delay (max. 0.12 µs).

To configure lines with a length &lt; 20 m in STEP 7 or to configure the corresponding signal delay, follow these steps:

1. Select the port in the topology view of STEP 7.
2. Navigate in the Inspector window to "Port interconnection" in the "Partner port" box.
3. Enable the "Cable length" option (default setting) or "Signal delay".
4. Select "&lt; 20 m" in the drop-down list or enter the signal delay.

---

**See also**

[Rules and information for IRT configurations (S7-1500, S7-1500T)](#rules-and-information-for-irt-configurations-s7-1500-s7-1500t)
  
[Bandwidth use for synchronized IO controllers (S7-1500, S7-1500T)](#bandwidth-use-for-synchronized-io-controllers-s7-1500-s7-1500t)

### Sample configuration for IRT with high performance

The figure below shows a sample configuration with which you can achieve maximum performance.

![Figure](images/88100226443_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/88100264459_DV_resource.Stream@PNG-de-DE.png) | Port 2 of the X1 interface and the ports of the interface modules in the line use the following setting: Medium copper, cable length &lt; 20 m. |
| ![Figure](images/88100239115_DV_resource.Stream@PNG-de-DE.png) | Port 2 of the X1 interface and the ports of the interface modules on the bus use the following setting: Medium copper, cable length &lt; 20 m. |
| ![Figure](images/88100251787_DV_resource.Stream@PNG-de-DE.png) | Via the interfaces X2 and X3 of the CPU, a PG connection can be established to the CPU. |

Use the following settings for the Sync domain:

- Enable the "Make 'high performance' possible" option.
- Set the send clock to 125 µs.
- Set the bandwidth use to "Maximum 90% cyclic IO data. Focus on cyclic IO data".
- Enable the "Allows the use of ‘fast forwarding'" option.

#### Standard Ethernet communication for IRT with high performance

Standard Ethernet communication is still possible even in a PROFINET IO system with high performance. Keep in mind that you first arrange the IRT nodes, as seen from the IO controller, and arrange the standard Ethernet nodes at the end of the line.

With a large volume of data through standard Ethernet communication, it makes sense to reduce the load on your network by separating standard Ethernet communication and cyclic real-time communication. Example: Use the X1 interface for the fast PROFINET IO system and the X2 interface for standard Ethernet communication.

## Maintenance with asset management data records

This section contains information on the following topics:

- [Further information about asset management at PROFINET](#further-information-about-asset-management-at-profinet)
- [Content and structure of an asset management record](#content-and-structure-of-an-asset-management-record)
- [Asset management data record for I-devices (S7-1500, S7-1500T)](#asset-management-data-record-for-i-devices-s7-1500-s7-1500t)

### Further information about asset management at PROFINET

Operation of machines and plants without a detailed knowledge of devices and assets is difficult to imagine.

Maintenance requires data for this – data that is extensive and up-to-date as far as possible.

The requirement of greater transparency with regard to the data made available by plant components has been fulfilled by PROFIBUS &amp; PROFINET International (PI): The identification and maintenance data familiar since PROFIBUS times have been extended.

The current PROFINET fulfills this requirement through the definition of a special data record: the Asset Management Record (AMR).

The aim of this definition is to enable you to acquire **all** the components to be maintained online - and not only those components that can be addressed and accessed through the PROFINET device model (Device / Module / Submodule). PROFINET now also reaches non-PROFINET components!

#### Assets general and asset management data records

**Assets** are components (hardware and software / firmware) of a machine, for example a laser welding machine, or a plant.

A large number of these device components can already be identified through tried-and-tested I&amp;M functions or corresponding data records (I&amp;M0 to I&amp;M5) in the PROFINET context: The device itself as well as its modules and submodules. Meaning all components that can be addressed through the PROFINET device model.

Components that **cannot** be addressed via the PROFINET device model, but whose data it should be possible to acquire online for operation and maintenance, can be identified through **asset management** functions. This asset management data (short: AM data) is stored in a defined structure in a special data record, the **asset management record** (AMR) mentioned above.

The PROFINET Guideline "Identification &amp; Maintenance Functions" differentiates here between I&amp;M functions (I&amp;M data) and asset management functions (AM data): The following sections only deal with the AM data.

The components that can be read additionally online through asset management data records include both hardware components, such as backplane bus modules of a device as well as firmware components such as a drive control unit with own versioning.

#### Application examples

Importing asset management records enables you to read the following information during installation or operation, for example:

- Are only approved devices being used (whitelist check)?
- A firmware update is due. Obtain a fast overview: Which devices or components are affected and have to be upgraded?

#### Making asset management data available

The concept for the asset management of PROFINET devices stipulates that the manufacturers of PROFINET devices have to ensure that non-PROFINET automation components are made available through an asset management record. This data record is assigned to the PROFINET device.

In contrast to a "standard" IO device, with an I-device the project engineer has to make the asset management record available. In this case, the central modules of the I-device are assets. From the perspective of PROFINET, these central modules are not visible from the point of view of the higher-level IO controller. The higher-level IO controller only "sees" the transfer areas through which it exchanges IO data with the I-device.

The principle of this provision is explained in the section.

#### Reading asset management data

The asset management record has the index 0xF880 and is read with standard PROFINET mechanisms by the user of the records, for example a tool or program for evaluating these data.

A user program in the S7-1500 IO controller, for example, can read out the AMR of an IO device with the RDREC instruction (Index 0xF880).

It is not possible to write to this data record.

#### Further information

Whether and to which extent a PROFINET device supports asset management data, meaning whether it makes an AMR available, is specified in the documentation of the respective device.

### Content and structure of an asset management record

#### Basic structure of the asset management record

You are first provided with an overview of the general structure of the record. The following table describes the framework within which the asset management data blocks are embedded. Each data block represents an asset, a terminal block for example.

| Element of the data structure | Designation according to IEC 61158-6-10 | Code | Data type / length in bytes |
| --- | --- | --- | --- |
| Header AssetManagementData | BlockType | 0x0035 | UINT / 2 |
| BlockLength | Number of bytes without counting the bytes for BlockType and BlockLength | UINT / 2 |  |
| BlockVersion | 0x0100 | UINT / 2 |  |
| AssetManagementInfo  AssetManagementBlocks (n) | NumbersOfEntries | Number of AssetManagementBlocks | UINT / 2 |
| AssetManagementBlock 1 | See the table below |  |  |
| AssetManagementBlock 2 |  |  |  |
| ... |  |  |  |
| AssetManagementBlock n |  |  |  |

#### Structure of asset management blocks

Each AssetManagementBlock contains identification data and localization information for an asset. An AssetManagementBlock has a substructure with basic characteristics described below.

The header of an AssetManagementBlocks contains the coded information about which of the three possible AM data compilations the record contains. Devices make a suitable BlockType available in accordance with the various device types:

- Complex devices with information about the hardware and firmware (BlockType "AM_Fullinformation")
- Complex devices with information about the hardware (BlockType "AM_HardwareOnlyInformation")
- Devices with information about the firmware (BlockType "AM_FirmwareOnlyInformation")

The differentiation provides an efficient data structure below the header. Nevertheless, the data record can have a considerable size (maximum of 64 KB, depending on the number of assets that the IO device supplies).

Structure of AssetManagementBlock

| Element of the data structure | Designation according to IEC 61158-6-10 | Code | Data type / length in bytes |
| --- | --- | --- | --- |
| Header AssetManagementBlock | BlockType | 0x0036 (AM_FullInformation)  0x0037 (AM_FirmwareOnlyInformation)  0x0038 (AM_HardwareOnlyInformation) | UINT / 2 |
| BlockLength | Number of bytes without counting the bytes for BlockType and BlockLength | UINT / 2 |  |
| BlockVersion | 0x0100 | UINT / 2 |  |
| Padding | 0x0000 (padding byte) | USINT / 1 |  |
| Padding | 0x0000 (padding byte) | USINT / 1 |  |
| AssetManagementBlock  (Structure depends on the BlockType. Here it is shown using AM_Fullinformation as an example) | IM_UniqueIdentifier | Manufacturer-generated Universal Unique Identifier (UUID) conforming to ISO/IEC 9834-8. Used as a reference key to uniquely identify this asset.  Example: 550c5300-d34a-22b4-11d3-5533991111b3 | Array of Byte / 16 |
| AM_Location | Description of the location of the asset:  Either slot-oriented ("Slot and SubslotNumber format") or hierarchical ("Twelve level tree format").  See following description | Array of Byte / 16 |  |
| IM_Annotation | Manufacturer-specific notation  Example: "Terminal block, Type xyz123 ".  64 bytes are always used. Spaces are used for padding if the string is shorter. | Array of Char / 64 |  |
| IM_OrderID | Manufacturer-specific article number  Example: "6ES7 131-6BF00-0BA0 ".  64 bytes are always used. Spaces are used for padding if the string is shorter. | Array of Char / 64 |  |
| AM_SoftwareRevision  (not at AM_HardwareOnlyInformation) | Manufacturer-specific SW version  Example: "V6.3.8 ".  64 bytes are always used. Spaces are used for padding if the string is shorter.  If the asset supports IM_Software_Revision, the AM_SoftwareRevision is padded with spaces. | Array of Char / 64 |  |
| AM_HardwareRevision  (not at AM_FirmwareOnlyInformation) | Manufacturer-specific hardware version  Example: "A4 ".  64 bytes are always used. Spaces are used for padding if the string is shorter. | Array of Char / 64 |  |
| IM_Serial_Number | Manufacturer-specific unique production-related number.  The characters come from the visible range (0x20 ... 0x7E), no control characters.  Example: "A78C-1C82 ".  16 bytes are always used. Spaces are used for padding if the string is shorter. | Array of Char / 16 |  |
| IM_Software_Revision  (not at AM_HardwareOnlyInformation) | Software version, follows a strict structure (SW version prefix, for example "V", digits for functional extension, digits for BugFix, digits for internal change).  Example: 'V' 0x01 0x2 0x3  If AM_SoftwareRevision is padded with spaces, you should evaluate IM_Software_Revision.  If the asset does not support any hardware, the coding 'V' 0x00 0x00 0x00. | Array of Byte / 4   Prefix (character "V", "R", "P", "U", or "T"), then 3 digits "0" to "9" |  |
| AM_DeviceIdentification | Identification of the device. The structure is as follows:  AM_DeviceIdentification.DeviceSubID  (for SIEMENS e.g. 0x0000)  AM_DeviceIdentification.DeviceID  (Device ID from manufacturer, 0x0000 to 0xFFFF)  AM_DeviceIdentification.VendorID  (Example for Siemens assets: 0x002A)  AM_DeviceIdentification.Organization: Example for Siemens assets: 0x0000 (PROFINET) | Array of Byte / 8 |  |
| AM_TypeIdentification | Manufacturer-allocated type identification:  0x0000: Unspecified  0x0001: Controller (PLC)  0x0002: PC-based  0x0003: IO module, IO submodule  0x0004: Communications module / submodule  0x0005: Interface module / submodule  0x0006: Active network component  0c0007: Media attached unit (bus adapter)  0x0100 to 0x7FF: Manufacturer-specific | UINT / 2 |  |
| IM_Hardware_Revision  (not at AM_FirmwareOnlyInformation) | Version of the hardware (0x0000 to 0xFFFF)  Example: 0x0003  If AM_HardwareRevision is padded with spaces, you should evaluate IM_Hardware_Revision. | UINT / 2 |  |

#### AM_Location

Asset management at PROFINET supports two formats for coding the location of an asset:

- Slot-oriented format ("Slot and SubslotNumber format")
- Hierarchical format ("Twelve **L**evel **T**ree format" abbreviated **LT** format)

Assets that are part of the PROFINET device use the slot-oriented format. These assets are bound completely to the PROFINET modules and submodules.

Assets that are located outside the PROFINET device use the hierarchical format (LT format) for coding the location of an asset.

These assets are localized by their tree level. The tree level begins with Level 0. The value of Level 0 provides information about the proximity to the PROFINET device:

- If the asset is connected to a module that can be addressed through the PROFINET device model, Level 0 has the value 0. The subsequent levels (Level 1 to Level 3) then have the meaning of slot address, subslot address and channel number. If further assets are connected to this asset, the next Level 4 is used. The limit is reached at Level 11.
- If the asset belongs to a PROFINET device but is not connected to a module that can be addressed through the PROFINET device model, Level 0 has a value between 1 and 0x1FF. An example of such an asset is a power supply unit in the PROFINET device. If a further asset is connected to this power supply unit, for example a sensor, the next tree level is used to localize this sensor (Level 1).
- If the asset is located outside the PROFINET device, but, for example, belongs to a machine into which the PROFINET device is installed, Level 0 has a value between 0x200 and 0x3FE.

The value 0x3FF for a tree level shows that this tree level is not used. This means that no further asset is connected. In this case, all the lower tree levels down to Level 11 must also have this value.

#### Example AM_Location slot-oriented

A rack and the terminal blocks located on it each supply AM data. The slot assignments are shown in the figure.

![Example of assets with slot-oriented AM_Location coding.](images/103644305675_DV_resource.Stream@PNG-en-US.png)

Example of assets with slot-oriented AM_Location coding.

Code the AM_Location as an asset for each module as follows:

Bit 0 – 7: AM_Location.Structure = 0x02 (coding "Slot and SubslotNumber format")

Bit 8 – 15: AM_Location.Reserved1 = 0x00 (padding byte)

Bit 16 – 31: AM_Location.BeginSlotNumber = 2 (the "Rack" asset begins from Slot 2 on)

Bit 32 – 47: AM_Location.BeginSubslotNumber = 0xFFFF (the asset encompasses all the subslots of Slot 2. Otherwise you specify the no. of the subslot at which the asset begins)

Bit 48 – 63: AM_Location.EndSlotNumber = 4 (the asset ends at Slot 4)

Bit 64 – 79: AM_Location.EndSubslotNumber = 0xFFFF (the asset encompasses all the subslots of Slot 4. Otherwise you specify the no. of the subslot at which the asset ends)

Bit 80 – 95: AM_Location.Reserved2 = 0x0000 (padding byte)

Bit 96 – 111: AM_Location.Reserved3 = 0x0000

Bit 112 – 127: AM_Location.Reserved4 = 0x0000

#### Example AM_Location level-oriented

A complex sensor is connected to an IO module (Slot 5, Subslot 1, Channel 1). Two simple sensors, in turn, are connected to the complex sensor. The module can be addressed within the PROFINET device model. Level 0 therefore has the value 0x0000. The next level (Level 1) is specified by the assigned slot. This is followed by the further levels for the subslot and channel and, if appropriate, further subordinate layers.

![Example of assets with hierarchical AM_Location coding.](images/103644318603_DV_resource.Stream@PNG-en-US.png)

Example of assets with hierarchical AM_Location coding.

Detailed coding for the example:

Bit 0 – 7: AM_Location.Structure = 0x01 (LT format)

Bit 8 – 17: AM_Location.Level0 = 0x000 (assets that are assigned to modules always have the Level 0 value 0x000)

Bit 18 – 27: AM_Location.Level1 = 0x005 (Slot 5)

Bit 28 – 37: AM_Location.Level2 = 0x001 (Subslot 1)

Bit 38 – 47: AM_Location.Level3 = 0x001 (Channel 1)

Bit 48 – 57: AM_Location.Level4 = 0x3FF (coding for "Level not used")

Bit 58 – 67: AM_Location.Level5 = 0x3FF (coding for "Level not used")

...

Bit 118 – 127: AM_Location.Level11 = 0x3FF (coding for "Level not used")

Notation used in the screen for the LT coding of complex sensors: 0.5.1.1

The following correspondingly applies for the remaining sensors:

LT coding for simple Sensor 1 at complex sensor: 0.5.1.1.1

LT coding for second simple Sensor 2 at complex sensor: 0.5.1.1.2

### Asset management data record for I-devices (S7-1500, S7-1500T)

With STEP 7 (TIA Portal) as of V15 and with S7-1500 CPUs as of Firmware V2.5, you have the possibility to compile an asset management record via a user program. Configured as an I-device, these CPUs then supply the data from centrally plugged modules to a requesting IO controller as assets.

"S7-1500 CPUs" also refers to the CPU variants S7-1500F, S7-1500T, S7-1500C, S7‑1500 SW Controller, S7-1500pro CPUs and ET 200SP CPUs.

#### Asset management records for I-devices

I-devices often represent machines. The PROFINET IO controller to which the I-device is assigned only sees the PROFINET interface (also configured as an IO device) and the transfer areas of the I-device configured by the machine manufacturer. The local modules of the I-device are not visible or cannot be accessed.

The assigned IO controller can read the central modules as assets of the I-device by means of an asset management record that the user program of the I-device compiles.

![Assets of an I-device](images/103644331531_DV_resource.Stream@PNG-en-US.png)

Assets of an I-device

#### Requirement

- S7-1500-CPU as of firmware V2.5, configured as an I-device
- STEP 7 (TIA Portal) as of V15
- If an IO controller is to read the asset management record:

  The PROFINET IO controller is programmed correspondingly to read an asset management record.

  For a SIMATIC IO controller, for example, you call a read instruction (RDREC) with record index 0xF880. The instruction addresses any submodule of the I-device, for example the first configured transfer area submodule.

#### Basic procedure

The following steps are fundamentally required to create the requirements so that an I-device can make its local modules available as an asset management record to a requesting IO controller:

1. Make the settings in the properties of the PROFINET interface of the CPU.

   - Activate "IO device" operating mode
   - Activate the "Activate asset management using user program" option

     PROFINET interface forwards a request of an IO controller to the user program of the I-device for reading the asset management record only if the option is selected.

     ![Activating asset management using a data record](images/103644287627_DV_resource.Stream@PNG-en-US.png)

     Activating asset management using a data record
2. Configure the program routine for compiling the asset management record. The program part collects the required I&amp;M0 data of the plugged central modules and stores them in the corresponding fields of the data record structure of the asset management record.
3. Configure the program part for coordinating the data record provision:   
   For this, call the instruction PRVREC (Provide Record) in accordance with the following templates in the corresponding modes:

   - Cyclic calling (for example in the cycle OB) of the PRVREC instruction with Mode 0, in order to recognize the AMR request.
   - When the AM record request is recognized, the PRVREC program has to acknowledge within one second that the request has been recognized. This means that PRVREC must be called with the Mode 2, and with the required AM record. If the I-device does not adhere to the time frame, the I-device acknowledges the record request of the IO controller as negative!

     Particular aspect for configuration of the PRVREC call: PRVREC has to be called with **F_ID = 0**. This codes that this is an IO-device-specific data record. The SLOT and SUBSLOT output parameters therefore also return the value 0.
   - Within 10 seconds the AM record now has to be completed and PRVREC be called with Mode 3 (positive response to the IO controller with provision of the AM record). If the I-device does not adhere to the time frame, the I-device acknowledges the record request of the IO controller as negative!

   A detailed description of the PRVREC instruction and possible error codes for evaluating the function can be found in the online help of STEP 7 (TIA Portal).

#### Compilation of the asset management record

You have various possibilities for compiling the asset management record for an I-device:

- Recommendation: Recommendation: The Siemens Industry Online Support makes an application available to you that helps you to compile the asset management record.   
  The data area of the asset management record is divided in two. The first part consists of an automatically determined area that packages the IM0 data of the slots of the I-device into an asset management block. The second part consists of the user-specific asset management blocks. You configure the user-specific asset management blocks based on pre-configured asset management record structures, fill them with information and make them available to the application.  
  The application performs the following:

  - The application determines the required size of all the asset management blocks and generates a new data block in the load memory of the CPU.
  - The application assigns parameters to the data block in accordance with the specifications of an asset management record and fills it with the automatically determined asset management blocks and those transferred by you.
  - The application makes this asset management record available to the higher-level IO controller.

  The application is described in this application example
- You create the asset management record yourself.  
  The following section describes how you can compile an asset management record for an I-device yourself.  
  The concept assumes you yourself determine the I&amp;M data for each centrally plugged module and fill the asset management record with this information. The I&amp;M0 data of a module contains basic information about the module such as the manufacturer's code, article number, serial number, hardware and firmware version. These are the data that are also required in the AM record for an asset.

#### Determine the I&amp;M data of centrally plugged modules

The central structure consists of an optionally plugged power supply unit (Slot 0), followed by the I-device CPU (Slot 1), and then followed by the further modules, such as digital modules, analog modules, etc. (as of Slot 2).

You determine the I&amp;M data with the "Get_IM_Data" instruction for the plugged modules with exception of the CPU:

To assign parameters for the "Get_IM_Data" instruction, you require the hardware identifier (LADDR input parameter). You determine the hardware identifier for each occupied slot with the "GEO2LOG" instruction (Determine hardware identifier from slot).

Summary of the theoretical steps:

1. In a loop, determine the hardware identifiers of the plugged modules with the "GEO2LOG" instruction.
2. For each hardware identifier found, determine the I&amp;M data by using the "Get_IM_Data" instruction and store these data in a data block that you address with the input parameter DATA. Use ARRAY of BYTE for the data storage. This corresponds to the description of the AM record contents in the preceding section.

#### Forming an AM record with the determined I&amp;M data

The following sections are based on the description of the fundamental structure of the AM record, see the preceding section.

Since each module of an S7-1500 contains hardware and firmware information, select the coding for "AM_Fullinformation" for the assigned BlockType.

For the data types used:

- IM_Annotation, IM_OrderID, AM_SoftwareRevision and AM_HardwareRevision: Characters (UTF-8)
- IM_SeriaNumber: Characters ("ASCII characters") with the exception of the characters for DEL (0x7F)
- Do not use String data types. They require additional bytes and therefore do not conform to the conventions of the PROFINET standard 61158-6-10 "Application layer protocol specification"

Form the AM_FullInformationBlock for each module as follows:

AM_FullInformationBlock for modules

| Data record element | Description |
| --- | --- |
| IM_UniqueIdentifier | Generate a (pseudo) random UUID (hash value) in accordance with ISO 9834-8 as follows:  - Generate an 8-byte hash value across the I&amp;M0 data of the module (as of Slot 2).  Use the algorithm Fowler-Noll-Vo (in short: FNV); an algorithm for generating variance coefficients (hash values) across data field, see corresponding example code in the Internet or online support. - Generate an 8-byte hash value across the I&amp;M0 data of the CPU.  (Use the algorithm Fowler-Noll-Vo (in short: FNV) as described above) - IM_UniqueIdentifier  Byte 0 to 7: Hash value of module I&amp;M0 data Bytes 8 to 15: Hash value for CPU-I&amp;M0 data Required customizations to ISO 9834-8:  Byte 8, Bit 7 has to be set to 1, and Byte 8, Bit 6 to 0 (result of the AND operator with **00**11 1111, subsequent OR operator with **10**00 0000) Byte 6, Bit 4 to 7 have to be set to 0100 (result of the AND operation with 0000 1111, then OR operation with 0001 0000)   Since this algorithm is based on the I&amp;M0 data of the CPU as well as of the modules, it generates a constant IM_UniqueIdentifier for an individual module. When the configuration changes the IM_UniqueIdentifier also changes. |
| AM_Location | Byte 0 = 0x02 (slot-oriented coding), see description in the preceding section. |
| IM_Annotation | Example: "S7-1500 module" and pad the remaining bytes of IM_Annotation with spaces (0x20). |
| IM_OrderID | Copy 20 bytes of the I&amp;M0 data of the module (beginning with offset 2 of the I&amp;M0 data). Pad the remaining 44 bytes with spaces (0x20) |
| AM_SoftwareRevision | Pad the field with 64 spaces (0x20) |
| AM_HardwareRevision | Pad the field with 64 spaces (0x20) |
| IM_Serial_Number | Copy 16 bytes of the I&amp;M0 data of the module (beginning with offset 22 of the I&amp;M0 data) |
| IM_SoftwareRevision | Copy 4 bytes of the I&amp;M0 data of the module (beginning with offset 40 of the I&amp;M0 data) |
| AM_DeviceIdentification | Byte 0, 1, 2, 6, 7 = 0x00 Byte 3 = 0x2A (Vendor = Siemens) Byte 4 = 01, Byte 5 = DeviceID (e.g. CPU 15xx = 0x0E) |
| AM_TypeIdentification | Copy 2 bytes of the I&amp;M0 data of the module (beginning with offset 48 of the I&amp;M0 data) |
| IM_HardwareRevision | Copy 2 bytes of the I&amp;M0 data of the module (beginning with offset 38 of the I&amp;M0 data) |

---

**See also**

[RCVREC: Receive data record (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rcvrec-receive-data-record-s7-1200-s7-1500)
  
[PRVREC: Make data record available (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#prvrec-make-data-record-available-s7-1200-s7-1500)

## Configuring direct data exchange between S7-1500 CPUs

This section contains information on the following topics:

- [Introduction](#introduction-1)
- [Configuring direct data exchange between two S7-1500 CPUs](#configuring-direct-data-exchange-between-two-s7-1500-cpus)
- [Configuring direct data exchange between multiple IO controllers](#configuring-direct-data-exchange-between-multiple-io-controllers)

### Introduction

This section describes the direct data exchange function.

#### Principle of operation

Starting with firmware version V2.8, the S7-1500​ CPU supports direct data exchange with other S7‑1500 CPUs.

In the case of direct data exchange, an S7‑1500 CPU provides cyclic user data from the I/O area to one or more partners. The direct data exchange is based on PROFINET with IRT and isochronous mode.

The data exchange takes place via transfer areas.

#### Direct data exchange between two S7‑1500 CPUs (1:1)

The figure below shows the direct data exchange between two S7‑1500 CPUs. The output transfer areas of the sending S7‑1500 CPU correspond to the input transfer areas of the receiving S7‑1500 CPU.

![Direct data exchange between two S7‑1500 CPUs (1:1)](images/127101473163_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Transfer relation between the user program and the transfer area. The user program and the transfer areas exchange input and output data via this path. |
| ② | Communication relation for direct data exchange You configure the communication relations in STEP 7. You create transfer areas for direct data exchange in the properties of the communication relations. |

Direct data exchange between two S7‑1500 CPUs (1:1)

#### Direct data exchange with multiple receivers (1:n)

The following figure shows the direct data exchange with multiple S7‑1500 CPUs. In this case, the sending S7‑1500 CPU provides the data of its output transfer areas to multiple S7‑1500 CPUs. Each receiving S7‑1500 CPU has its own input transfer areas.

![Direct data exchange with multiple receivers (1:n)](images/127101485579_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Transfer relation between the user program and the transfer area. The user program and the transfer areas exchange input and output data via this path. |
| ② | Communication relation for direct data exchange You configure the communication relations in STEP 7. You create transfer areas for direct data exchange in the properties of the communication relations. |

Direct data exchange with multiple receivers (1:n)

#### Applications

- Deterministic, isochronous I/O communication between multiple S7‑1500 CPUs

#### Properties of direct data exchange

- Always isochronous
- Support of MRPD for MRP configuration
- No acyclic data exchange via PROFINET data record mechanisms
- No PROFINET alarms
- Configuration limits:

  - Maximum data length for direct data exchange 3075 bytes including user data qualifier
  - Maximum data length for a transfer area: 1024 bytes without user data qualifier
  - Maximum number of transfer areas of sender: 128
  - Maximum number of transfer areas of receiver: 512, distributed among a maximum of 64 receivable PROFINET frames and thus up to 64 sender CPUs

#### Diagnostics options of the receiver

Operating state change of sender:

- When the sender goes from RUN to STOP, the receiver behaves as follows:

  - The "SYNC_PI" and "SYNC_PO" instructions return an error message in parameter RET_VAL during synchronization of the process image.
  - With direct I/O access to the input transfer areas of the direct data exchange, OB 122 "I/O access error" is called, if present.
  - Incoming diagnostic message "I/O data failure in hardware component"
- When the sender goes from STOP to RUN, the receiver behaves as follows:

  - Call of OB 83 "Pull/plug interrupt" for input transfer areas of the direct data exchange
  - Up until the call of OB 83, OB 122 is called if present.
  - Outgoing diagnostic message "User data failure of hardware component"

Station failure/station recovery of the sender:

- When the sender fails, e.g. due to a bus interruption, the receiver behaves as follows:

  - Call of OB86 "Rack failure"
  - The "SYNC_PI" and "SYNC_PO" instructions return an error message in parameter RET_VAL during synchronization of the process image.
  - With direct I/O access to the input transfer areas of the direct data exchange, OB 122 "I/O access error" is called, if present.
- When the sender recovers after a station failure, e.g. because the bus connection is re-established, the receiver behaves as follows:

  - Call of OB86 "Rack failure"

### Configuring direct data exchange between two S7-1500 CPUs

The procedure for configuring direct data exchange between two IO controllers is described below.

First, you create the communication relation for direct data exchange. You then configure transfer areas for the connection.

#### Requirements

- STEP 7 V16 or higher
- Two S7‑1500 CPUs firmware version V2.8 or higher
- IRT is configured:

  - Both CPUs are in one sync domain.
  - One CPU is the sync master, and the other CPU is the sync slave.
  - Ports are interconnected.

#### Setting up the communication relation for direct data exchange

To set up the communication relation for direct data exchange between two S7‑1500 CPUs, follow these steps:

1. Select the PROFINET interface X1 of the sending S7‑1500 CPU.
2. Change to the table view of the network view, tab "I/O communication".  
   The PROFINET interface X1 of the CPU is shown in the "Partner 1" column.
3. In the "Partner 2" column at "&lt;Drop or select the device here&gt;", select the PROFINET interface of the communication partner from the drop-down list as the connection partner.  
   Note the communication direction:

   - ←: Communication partner is sender
   - →: Communication partner is receiver

The communication relation for direct data exchange between the two S7‑1500 CPUs is set up.

![Communication relation for direct data exchange](images/127188724747_DV_resource.Stream@PNG-en-US.png)

Communication relation for direct data exchange

#### Configuring transfer areas for direct data exchange

To configure a transfer area for direct data exchange, follow these steps:

1. Select the communication relation for direct data exchange.

   ![Communication relation for direct data exchange](images/127101620619_DV_resource.Stream@PNG-en-US.png)

   Communication relation for direct data exchange
2. Navigate to the properties of the communication relation to "General" &gt; "Direct data exchange" &gt; "Transfer areas".
3. Create a new transfer area by double-clicking on "&lt;Add new&gt;". Assign a meaningful name for the transfer area.

A transfer area for direct data exchange is created.

![Transfer area for direct data exchange](images/127101431179_DV_resource.Stream@PNG-en-US.png)

Transfer area for direct data exchange

The communication direction of the transfer area is specified by the communication relation. You cannot change the communication direction of the transfer area.

#### Editing the transfer area

Set the properties of the transfer area under "General" &gt; "Direct data exchange" &gt; "Name of transfer area" &gt; "Detail of the transfer area".

![Properties of the transfer area](images/127101464971_DV_resource.Stream@PNG-en-US.png)

Properties of the transfer area

Overview of the settings of the transfer area

| Parameter | Local | Partner |
| --- | --- | --- |
| Start address | Set the start address of the input or output transfer areas in the local CPU. | Set the start address of the input or output transfer areas in the partner CPU. |
| Organization block | Assign the transfer area to an isochronous mode interrupt OB or the "MC-Servo" OB. | Assign the transfer area to an isochronous mode interrupt OB or the "MC-Servo" OB. |
| Process image | Select a process image partition, e.g. PIP 1. If you have assigned "MC-Servo" as the organization block, STEP 7 automatically sets "PIP OB Servo" as the process image. | Select a process image partition, e.g. PIP 1. If you have assigned "MC-Servo" as the organization block, STEP 7 automatically sets "PIP OB Servo" as the process image. |
| Data length [bytes] | Set the size of the transfer area. | - |

#### Downloading the configuration to devices

Rules:

- Download the configuration to all CPUs involved.
- If you make changes to the configuration of the direct data exchange, download these changes to all CPUs involved.

### Configuring direct data exchange between multiple IO controllers

The procedure for configuring direct data exchange between multiple S7‑1500 CPUs is described below.

First, you set up the communication relations for direct data exchange. You then configure transfer areas for the communication relations.

#### Requirements

- STEP 7 V16 or higher
- S7‑1500 CPUs firmware version V2.8 or higher
- IRT is configured:

  - All CPUs are in one sync domain.
  - One CPU is the sync master, and the other CPUs are sync slaves.
  - Ports are interconnected.

#### Setting up the communication relations for direct data exchange

To set up the connection for direct data exchange between multiple S7‑1500 CPUs, follow these steps:

1. Select the PROFINET interface X1 of the sending CPU.
2. Change to the table view of the network view, "I/O communication" tab.  
   The PROFINET interface X1 of the CPU is shown in the "Partner 1" column.
3. In the "Partner 2" column at "&lt;Drop or select the device here&gt;", select the PROFINET interface of the communication partner from the drop-down list as the connection partner.  
   Note the transfer direction:

   - ←: Connection partner is sender
   - →: Connection partner is receiver

   The connection for direct data exchange between the two S7‑1500 CPUs is set up.
4. Repeat step 3 for every other receiving IO controller.

The connections for direct data exchange between the sending CPU and the receiving CPUs are set up.

![Connection for direct data exchange with multiple S7‑1500 CPUs](images/127188605835_DV_resource.Stream@PNG-en-US.png)

Connection for direct data exchange with multiple S7‑1500 CPUs

#### Configuring transfer areas for direct data exchange

The following graphic shows the order for configuration of the transfer areas.

![Order of configuration of transfer areas in the case of multiple receivers](images/127101595403_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | First, you configure the transfer area between the sender and one receiver. You configure this transfer area at the PROFINET interface of the sender. |
| ② | You then configure the transfer areas between the sender and the other receivers. You configure these transfer areas at the PROFINET interfaces of the receivers. |

Order of configuration of transfer areas in the case of multiple receivers

To configure a transfer area for direct data exchange, follow these steps:

1. Select the PROFINET interface X1 of the sending CPU and change to the table view, "I/O communication" tab.
2. In the table view of the network view, select a communication relation for direct data exchange between the sender and receiver 1.
3. Navigate to the properties of the I/O connection to "General" &gt; "Direct data exchange" &gt; "Transfer areas".
4. Create a new transfer area by double-clicking on "&lt;Add new&gt;". Assign a meaningful name for the transfer area.

   A transfer area for direct data exchange between the sender and receiver 1 is configured.

   ![Transfer area for direct data exchange](images/127101431179_DV_resource.Stream@PNG-en-US.png)

   Transfer area for direct data exchange
5. Now, select the PROFINET interface of a receiver for which a transfer area is not yet set up, e.g. receiver 2.
6. Change to the table view of the network view to "I/O communication"  
   The communication relation for direct data exchange with the sender is displayed.

   ![Connection for direct data exchange in receiver 2](images/127101628811_DV_resource.Stream@PNG-en-US.png)

   Connection for direct data exchange in receiver 2
7. Select the communication relation.
8. Navigate to the properties to "General" &gt; "Direct data exchange" &gt; "Transfer areas".
9. Create a new transfer area by double-clicking on "&lt;Add new&gt;". Assign a meaningful name for the transfer area.

   A transfer area for direct data exchange is configured.
10. Select the transfer area.
11. For "Partner address", select the existing address area in the sender as the output transfer area.

    ![Transfer area for direct data exchange of multiple IO controllers](images/127101561611_DV_resource.Stream@PNG-en-US.png)

    Transfer area for direct data exchange of multiple IO controllers

    A transfer area for direct data exchange between receiver 2 and the sender is configured.

#### Editing the transfer area

Set the properties of the transfer area under "General" &gt; "Direct data exchange" &gt; "Name of transfer area" &gt; "Detail of the transfer area".

![Properties of the transfer area](images/127101713803_DV_resource.Stream@PNG-en-US.png)

Properties of the transfer area

Overview of the settings of the transfer area

| Parameter | Local | Partner |
| --- | --- | --- |
| Start address | Set the start address of the input or output transfer areas in the local CPU. | Set the start address of the input or output transfer areas in the partner CPU. |
| Organization block | Assign the transfer area to an isochronous mode interrupt OB or the "MC-Servo" OB. | Assign the transfer area to an isochronous mode interrupt OB or the "MC-Servo" OB. |
| Process image | Select a process image partition, e.g. PIP 1. If you have assigned "MC-Servo" as the organization block, STEP 7 automatically sets "PIP OB Servo" as the process image. | Select a process image partition, e.g. PIP 1. If you have assigned "MC-Servo" as the organization block, STEP 7 automatically sets "PIP OB Servo" as the process image. |
| Data length [bytes] | Set the size of the transfer area. | - |

#### Downloading the configuration to the device

Rules:

- Download the configuration to all CPUs involved.
- If you make changes to the configuration of the direct data exchange, download these changes to all CPUs involved.

## Configuring PROFINET Security Class 1 functions

This section contains information on the following topics:

- [PROFINET Security Class 1](#profinet-security-class-1)
- [Configuring the SNMP](#configuring-the-snmp)
- [Configuring DCP](#configuring-dcp)

### PROFINET Security Class 1

#### Introduction

With the introduction of PROFINET Security Class 1, additional security settings have been integrated into the PROFINET communication. They provide for protection of the PROFINET network at the protocol level, for example. Consequently, the individual components are also protected from unauthorized or inadvertent access.

Like in other areas of IT security, PROFINET security is based on the Defense‑in‑Depth concept. Multiple independent methods provide multi-layered protection against attacks or inadvertent changes.

PROFINET Security Class 1 includes the following security mechanisms for protecting your PROFINET network:

- Configuration options for the SNMP and DCP protocols
- Digital signature of PROFINET GSD files

These introductory sections provide information on which configuration options have been modified for the PROFINET Security Class 1.

#### Simple Network Management Protocol (SNMP)

SNMP is used for simple, network-based device management. For example, PROFINET devices support the following SNMP functions:

- Monitoring and diagnostics of the network topology through network management services
- Provision of network-specific information, such as details about the IP stack

Since STEP 7 V18, SNMP has been disabled in the basic settings of a CPU. You can enable or disable SNMP via the configuration or by writing a data record from the user program. You enter the community strings for read and write access via the configuration.  
Starting from STEP 7 V19, you can configure SNMP both for CPUs and for IO devices for the following access types:

- Read and write access
- Read access only

To determine whether IO devices support the new configuration of SNMP, refer to the respective Equipment Manuals. IO devices that support the new configuration of SNMP behave as follows during configuration or initial loading of the hardware configuration:

- STEP 7 as of V19: SNMP is disabled by default. Changed SNMP settings do not take effect until the hardware configuration has been loaded.
- STEP 7 &lt; V19: The IO device adopts the setting "SNMP enabled". When SNMP is enabled, the community strings are set to the following default values:

  - Read-only (read-only community string): public
  - Read and write access (read-write community string): private

See also: [Configuring the SNMP](#configuring-the-snmp)

#### Discovery Configuration Protocol (DCP)

The DCP protocol detects PROFINET devices and enables the basic settings, e.g. assignment of IP address or PROFINET device name.

Starting from STEP 7 V19, the "Activate DCP write protection" option is available for DCP. This "PROFINET Security Class 1" function prevents write access to PROFINET devices during IO data exchange and thus, for example, provides protection from the following dangers:

- Takeover of devices by attackers
- Undesired interruption of communication relations (ARs)

If an IO controller and IO device support the write protection function for DCP, this option is enabled by default for the corresponding communication relationship. An enabled DCP write protection function takes effect in the following cases:

- On the IO controller side: An IO controller establishes the communication relation with a corresponding IO device (the IO device does not need to be reachable for this purpose).
- On the IO device side: There is an active communication relation between the IO controller and the IO device.

During an effective write protection function of DCP, for example, Set commands (DCP Set) are rejected.

When the write protection option of DCP is enabled, the ongoing operation is secured as follows:

- DCP only has read access to the device information of the IO device.
- Changes to the basic settings of IO devices are no longer possible.

See also: [Configuring DCP](#configuring-dcp)

#### Digital signatures of PROFINET GSD files

The manufacturer provides a general station description file (GSD file) for each PROFINET device. The GSD file describes the properties of the device in a machine readable XML format and contains all properties of a PROFINET‑device that are needed for configuring.

With the introduction of PROFINET Security Class 1, GSD files together with other related files, such as images or text files, are provided in a GSDX file with a verified manufacturer signature. A GSDX file can also contain multiple GSD files, such as all GSD files of a device family.  
The included signature confirms the integrity and authenticity of the contained files. This ensures that the files contained in the GSDX file originate from the expected manufacturer and have not been altered.

If your engineering system does not support the import of GSDX files, continue using GSD files as up to now.

#### More information

You can find detailed information on SNMP in the "Communication" Function Manual.

You can find detailed information on PROFINET functions in the "PROFINET with STEP 7" Function Manual.

### Configuring the SNMP

#### Component interaction

PROFINET networks use the SNMP protocol for managing devices and the network infrastructure.

For information exchange, authentication must take place through the transfer of community strings. When SNMP is used, a community string must always have been assigned. Empty community strings are not allowed.

You can find configuration options for SNMP in the properties of the following devices:

- S7‑1500 CPU as an IO controller/I-device
- IO devices that support the configuration of SNMP

To learn how to configure SNMP for the various components, see the following sections.

> **Note**
>
> **Avoidance of erroneous access attempts**
>
> Inform maintenance personnel about the SNMP‑configuration in your plant.

#### Configuring SNMP for an IO controller

To configure SNMP for an IO controller, follow these steps:

1. Open the Properties of the IO controller in the network view or device view.
2. Navigate to the "Advanced configuration &gt; SNMP" area in the Inspector window.
3. If you want to use SNMP, select the "SNMP " option in the "SNMP" area.  
   Once you enable SNMP, a warning message appears informing you of the reduced protection against unauthorized access to functions and data of this device.
4. If you only need read access for SNMP, also select the option "Enable read-only access for SNMP".
5. Change the Read-only and Read-write community strings.  
   This increases the security of your system against cyberattacks. Empty community strings are not allowed.

Result: You have configured SNMP in the properties of your IO controller.

#### Configuring SNMP for an IO device

If an IO device supports the configuration of SNMP, you have the option of defining a separate SNMP configuration for this IO device as of STEP 7 V19. You can also modify the SNMP configuration in STEP 7 as of V19 or with other tools for IO devices which are imported as a GSD file.

To configure SNMP for an IO device in your PROFINET network, follow these steps:

1. Open the properties of the IO device in the network or device view.
2. Select "Advanced configuration" in the Inspector window.
3. Configure SNMP in the "Simple Network Management Protocol (SNMP)" area using the following options:

   - If you want to use SNMP, select the "Enable SNMP" option.  
     Once you enable SNMP, a warning message appears informing you of the reduced protection against unauthorized access to functions and data of this device.
   - If you only need read access for SNMP, also select the option "Enable read-only access for SNMP".
   - Change the Read-only and Read-write community strings.  
     This increases the security of your system against cyberattacks. Empty community strings are not allowed.

#### Configuring SNMP for an I-device (IO controller and I-device in the same project)

Since STEP 7 V18 you have the option of enabling SNMP in the CPU properties of an IO controller. When a CPU assumes the role of an I-device, you can also define the setting for SNMP in the CPU properties.

You configure SNMP when creating an I-device the same as for an IO controller. To access the SNMP configuration options for an I-device, follow these steps:

1. Open the Properties of the CPU that has been configured as an I-device in the network or device view.
2. Navigate to "Advanced configuration &gt; SNMP" in the Inspector window.
3. Select one of the following options from the drop-down list next to "SNMP configuration":

   - Set directly in the project:  
     The I‑Device adopts the SNMP‑configuration which is loaded from the I‑Device configuration onto the I‑Device at its PROFINET‑interface X1. Changes to the SNMP configuration by a higher-level IO controller are prevented.
   - Via PROFINET interface ... (e.g. X1) of the higher-level IO controller:  
     The I-device takes over the SNMP configuration from the higher-level IO controller at its PROFINET interface X1.  
     Requirements:  
     The option "Parameter assignment of PN interface by higher-level IO controller" is enabled at the I-device.  
     An IO controller has been selected in the drop-down list "Higher-level IO controller of the PN interface".
4. Configure SNMP using the following options:

   - If you want to use SNMP, select the "Enable SNMP" option.  
     Once you enable SNMP, a warning message appears informing you of the reduced protection against unauthorized access to functions and data of this device.
   - If you only need read access for SNMP, also select the option "Enable read-only access for SNMP".
   - Change the Read-only and Read-write community strings.  
     This increases the security of your system against cyberattacks. Empty community strings are not allowed.

Result: You have configured SNMP in the properties of your project-integrated I-device.

#### Configuring SNMP for an I-device as a GSD file

To use an I-device in another project or Engineering System, export the configured I-device as a general station description file (GSD file) in STEP 7. When you import the GSD file in the desired project, STEP 7 shows the configured I-device as a GSD device (DP standard device) in the device or network view.

Before the GSD file export, define how you want to use SNMP on the DP standard device. Starting from STEP 7 V19, you have the following options in the settings of SNMP:

- Configuring of SNMP in the local settings of the I-device:  
  The exported GSD file prevents changes from being made to the SNMP configuration in another project. The SNMP configuration options are not displayed on the inserted DP standard device.
- Configuring of SNMP by a higher-level IO controller in another project:  
  The SNMP configuration must be created in the other project in the same way as for a standard IO device.  
  Requirement:  
  The option "Parameter assignment of PN interface by higher-level IO controller" is enabled at the I-device.

If you want to configure SNMP on the DP standard device in another project, make the following settings on the I-device CPU:

1. At the PROFINET interface of the CPU that is configured as an I-device:

   - Activate the "Parameter assignment of PN interface by higher-level IO controller" option in the Inspector window under "Properties &gt; Operating mode".
2. In the SNMP settings of the I-device CPU:

   - Select the entry "via PROFINET interface ... (e.g. X1) from higher-level IO controller" from the drop-down list next to "SNMP configuration".  
     In this case, the I-device takes over the SNMP configuration from the higher-level IO controller at its PROFINET interface X1.

Result: If using the I-device in another project as a DP standard device, you can configure SNMP the same as for a standard IO device.

If using the I-device as a shared I-device in multiple projects, the following applies: Configure SNMP only in the project with the controller to which the interface of the I-device was assigned.

---

**See also**

[PROFINET Security Class 1](#profinet-security-class-1)

### Configuring DCP

#### Component interaction

DCP is a protocol for automatic detection and basic configuration of PROFINET devices. Consequently, DCP needs read and write access to the individual components in a PROFINET network.

To protect the components from malicious or inadvertent write access, the "Activate DCP write protection" function is available starting from STEP 7 V19.   
When the "Activate DCP write protection" function is enabled on an IO device, the DCP write protection operates as follows on the individual components:

- The DCP write protection takes effect on both the IO device and the IO controller when an active communication relation exists between the IO device and the IO controller.
- The DCP write protection takes effect on the associated IO controller of the IO device when the IO controller establishes a communication relation with the IO device.

When configuring DCP, consider the communication relationships in the entire PROFINET network.

- An IO device has only one communication relation with its IO controller.
- A Shared Device/I‑Device has a communication relationship with all higher-level IO‑Controllers.
- An IO‑Controller has a communication relationship to all assigned IO‑Devices and Shared Devices/I‑Devices.

Consequently, DCP write accesses by the IO controller are only permitted again after all communication relations with DCP write protection to devices have been terminated and disabled (e.g. with each respective call of D_ACT_DP).

To learn how to configure DCP, see the following sections.

> **Note**
>
> **Avoidance of erroneous access attempts**
>
> Specific settings, such as editing of device names via DCP, only function for devices that are not currently participating in cyclic data exchange.

#### Configuring DCP for a communication relation on an IO device

To configure DCP for a communication relation between IO controller and IO device, follow these steps:

1. Open the Properties of the IO device in the network or device view.
2. Select the entry "Advanced configuration" under "General" in the Inspector window.

The "Activate DCP write protection" option is enabled by default on all IO devices that support this function. The option cannot be changed in the following cases:

- The IO device is not assigned to any IO controller.
- The IO controller to which the IO device is assigned does not support the "Activate DCP write protection" function.

#### Configuring DCP for a communication relation on an I-device

To configure DCP for a communication relation between an IO controller and I-device in a common project with the assigned IO controllers, follow these steps:

1. Open the properties of the required PROFINET interface, e.g. X1, in the network or device view.
2. Select the entry "Operating mode" under "General" in the Inspector window.

The "Activate DCP write protection" option is enabled by default on all I-devices that support this function. The option cannot be changed in the following cases:

- The I-device is not assigned to any IO controller.
- The IO controller to which the I-device is assigned does not support the "Activate DCP write protection" function.

If you use an I-device as a shared I-device for IO controllers in different projects, the I-device will be inserted into other projects as a DP standard device. In this case, you therefore configure the DCP the same as for a standard IO device. The DCP write protection takes effect on each IO controller that has a communication relation with the shared I-device and supports the DCP write protection function.

---

**See also**

[PROFINET Security Class 1](#profinet-security-class-1)
