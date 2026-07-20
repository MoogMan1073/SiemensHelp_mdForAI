---
title: "Configuring PROFIBUS DP"
package: HWCPB34enUS
topics: 67
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring PROFIBUS DP

This section contains information on the following topics:

- [Configuring distributed I/O](#configuring-distributed-io)
- [The basics of configuring a DP master system](#the-basics-of-configuring-a-dp-master-system)
- [DP slaves within the hardware catalog](#dp-slaves-within-the-hardware-catalog)
- [DP/DP coupler in the hardware catalog](#dpdp-coupler-in-the-hardware-catalog)
- [Configurations involving PROFIBUS DP](#configurations-involving-profibus-dp)
- [Configuring distributed I/O systems](#configuring-distributed-io-systems)
- [Example: Configuring ET 200S as DP slave](#example-configuring-et-200s-as-dp-slave)
- [Configuring intelligent DP slaves](#configuring-intelligent-dp-slaves)
- [Configuring direct data exchange](#configuring-direct-data-exchange)
- [Using GSD files](#using-gsd-files)
- [Using PROFIBUS DPV1](#using-profibus-dpv1)
- [Constant and isochronous modes](#constant-and-isochronous-modes)

## Configuring distributed I/O

In the chapter below you will learn how to configure distributed I/O. This chapter will also provide you with basic information on configuring a DP master system.

### Basic information

- [Basics of configuring a DP master system](#the-basics-of-configuring-a-dp-master-system)
- [DP slaves in the hardware catalog](#dp-slaves-within-the-hardware-catalog)
- [Structure of a configuration with simple DP slaves (mono master system)](#configurations-involving-simple-dp-slaves)
- [Installation of a configuration with intelligent slaves (I-slaves)](#configurations-involving-several-dp-master-systems)
- [Installation of a configuration with two master systems](#configurations-involving-intelligent-dp-slaves)

### Overview for configuring distributed I/O

| Step | Description |
| --- | --- |
| 1 | [Create a DP master system](#creating-a-dp-master-system). |
| 2 | [If needed configure the interfaces of the DP master system](#editing-dp-master-systems-and-interfaces). |
| 3 | [Add a DP slave and configure it](#adding-dp-slaves-to-the-master-system-and-configuring-them). |
| 4 | [If necessary, assign DP slaves to a SYNC/FREEZE group](#assigning-a-dp-slave-to-a-syncfreeze-group). |

---

**See also**

[Configuring DPV1 devices](#configuring-dpv1-devices)
  
[Configuring direct data exchange](#configuring-direct-data-exchange-1)

## The basics of configuring a DP master system

### Distributed I/O

DP master systems that consist of a DP master and DP slaves which are connected via a bus and communicate with one another via the PROFIBUS DP protocol are referred to as distributed I/O.

### Configuring distributed I/O

The fact that the type of device may vary as far as DP masters/DP slaves are concerned means that these instructions deal only with the basic configuration procedure. However, the process for configuring distributed I/O is practically identical to that of non-distributed configuration.

### Creating the DP master system in the network view

After you have used dragged a DP master and a DP slave (for example, a CPU 315‑-2 and an IM 153‑-1) from the hardware catalog to the network view, connect them both to a PROFIBUS subnet.

As the network view only allows you to configure devices (not modules), you will need to switch to the device view in order to configure the DP master and slaves.

### Configuring a DP slave

Switch to the device view to configure the DP slave. In the device view, populate the DP slave rack with modules and parameterize DP identifiers and I/O addresses. You can check and edit the settings in the device overview and in the inspector window.

### Slot numbering for distributed I/O

Depending on the type of DP slave used, you should start the DP slave slot numbers at either "0" or "4".

The numbering of DP slave slots, on an ET 200M for example, is based on the structure for an S7-300:

![Slot numbering for distributed I/O](images/6004643723_DV_resource.Stream@PNG-en-US.png)

### DP slave slot rules in accordance with the S7-300 structure

The following slot rules apply to DP slaves that are structured in accordance with the S7-300 scheme:

- The actual I/O (inputs/outputs) always start at slot 4.
- Slot 1 is always reserved for a power supply module (PS) even if the actual configuration does not happen to include a PS.
- Slot 2 is always reserved for the DP interface.
- Slot 3 is always reserved for an extension interface module (IM) regardless of whether or not the actual I/O is capable of being expanded.

This scheme applies to all modular and compact DP slave types that are structured in accordance with the S7-300 model. The manner in which the slots are assigned is significant from the point of view of evaluating diagnostics messages ("Slot triggering diagnostics").

### Additional information

Please note the additional information relating to the scope of available functions, access methods, etc. that can be found in the manuals for the relevant devices or in the online help for specific FCs (for example, DP-SEND and DP-RECEIVE for CP 342-5).

## DP slaves within the hardware catalog

### DP slaves in the hardware catalog

You will find the DP slaves in the "Distributed I/O" folder of the hardware catalog. Compact and modular slaves are located there:

- Compact DP slaves  
  Modules with integrated digital/analog inputs and outputs, for example, ET 200L
- Modular DP slaves  
  (Interface modules with S7 modules assigned, for example, ET 200M

The available DP master and the desired functionality will determine which DP slaves can be used.

### I-slaves within the hardware catalog

You will find devices that you can configure as intelligent DP slaves in the "PLC" folder of the hardware catalog. The following are examples of devices that you can configure as I-slaves:

- CP 342-5 DP  
  in the hardware catalog under "PLC &gt; SIMATIC S7-300 &gt; CP &gt; PROFIBUS".
- CPU 315-2 DP, CPU 317-2 DP, CPU 319-3 PN/DP  
  in the hardware catalog under "PLC &gt; SIMATIC S7-300 &gt; CPU".
- IM 151-7 CPU  
  in the hardware catalog under "PLC &gt; SIMATIC ET200 PLC &gt; ET 200S &gt; CPU".

---

**See also**

[Browsing the hardware catalog](Configuring%20devices%20and%20networks.md#browsing-the-hardware-catalog)

## DP/DP coupler in the hardware catalog

### Introduction

A DP/DP coupler connects two PROFIBUS DP networks as a gateway so that the DP master from one network can transfer data to the DP master of the other network.

The maximum amount of data that can be transferred is 244 bytes input data and 244 bytes output data.

### DP/DP coupler in the hardware catalog

Details of a DP/DP coupler as gateway between two DM master systems are contained in the hardware catalog in the folder "Other field devices &gt; PROFIBUS-DP &gt; Gateways".

### Configuring the DP/DP coupler

DP/DP couplers are configured in both PROFIBUS networks, each in their own master systems.

The input and output areas of both networks must thereby be matched to one another. The output data from one end of the DP/DP coupler are accepted as input data at the other respective end and vice versa.

---

**See also**

[Installing the GSD file](#installing-the-gsd-file)
  
[Creating a DP master system](#creating-a-dp-master-system)

## Configurations involving PROFIBUS DP

This section contains information on the following topics:

- [Configurations involving "simple" DP slaves](#configurations-involving-simple-dp-slaves)
- [Configurations involving several DP master systems](#configurations-involving-several-dp-master-systems)
- [Configurations involving intelligent DP slaves](#configurations-involving-intelligent-dp-slaves)

### Configurations involving "simple" DP slaves

#### Communication between DP master and DP slave

In the case of a configuration involving simple DP slaves, data is exchanged between the DP master and simple DP slaves, i.e. with I/O modules via the DP master. The DP master polls each of the configured DP slaves in its polling list within the DP master system in succession and sends the output data/receives the input values from the slaves.

#### Mono-master system

The configuration with only one DP master is also described as mono-master system. A single DP master with its associated DP slaves is connected to a physical PROFIBUS DP subnet.

![Mono-master system](images/5864398987_DV_resource.Stream@PNG-en-US.png)

### Configurations involving several DP master systems

#### Configuration methods involving two or more DP master systems

When more than one DP master system is connected to a physical PROFIBUS DP subnet it is sometimes called a multi-master system.

You can use various methods to connect these DP master systems via PROFIBUS DP:

- Without logical connection of the DP master systems to each other
- Direct DP slave &gt; DP master data exchange
- Direct DP slave &gt; I-slave data exchange

#### Direct DP slave &gt; DP master data exchange

For the configuration of multi-master systems, input data of DP slaves of DP masters can be read on the same physical PROFIBUS DP subnet.

![Direct DP slave > DP master data exchange](images/26174319115_DV_resource.Stream@PNG-en-US.png)

#### Direct DP slave &gt; I-slave data exchange

This means that an intelligent DP slave (I-slave), such as a CPU 315-2 DP, can support the direct transfer of input data from DP slaves with different DP master systems to its input data area.

In principle, DP slaves of a certain version or higher can make selected input data available for the purpose of direct data exchange. However, only intelligent DP slaves are able to make further use of this input data.

![Direct DP slave > I-slave data exchange](images/26174393867_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[What you need to know about direct data exchange](#what-you-need-to-know-about-direct-data-exchange)
  
[Configuring direct data exchange](#configuring-direct-data-exchange-1)

### Configurations involving intelligent DP slaves

#### Definition

DP slaves that feature their own preprocessing program are referred to as intelligent DP slaves (I-slaves). Examples of intelligent DP slaves include:

- CPU 315-2 DP
- CPU 317-2 DP
- CPU 319-3 PN/DP

#### Configurations involving intelligent DP slaves

There are two methods for configuring intelligent DP slaves using PROFIBUS DP:

- I-slave &lt;&gt; DP master data exchange
- Direct DP slave &gt; I-slave data exchange

#### I-slave &lt;&gt; DP master data exchange

A higher-level automation system processes the automation task, which is broken down into sub-tasks. The necessary control tasks are processed separately and efficiently in a CPU as preprocessing programs. This CPU can be implemented in the form of an intelligent DP slave.

In the case of configurations involving intelligent DP slaves, for example CPU 315-2 DP, the DP master merely accesses the address area of the I-slave CPU, rather than the I/O modules of the intelligent DP slave. The address area must not be assigned to any actual I/O modules on the I-slave. The assignment must be made during I-slave configuration.

![I-slave &lt;> DP master data exchange](images/5873551627_DV_resource.Stream@PNG-en-US.png)

#### Direct DP slave &gt; I-slave data exchange

With this configuration, input data from simple DP slaves can be transferred to intelligent DP slaves on the PROFIBUS DP subnet at high speed.

In principle, all simple DP slaves (of a certain version or higher) and intelligent DP slaves can make their input data available for the purpose of direct data exchange. Intelligent DP slaves can be used as recipients of this data.

![Direct DP slave > I-slave data exchange](images/5873910283_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Adding an I-slave to a DP master system](#adding-an-i-slave-to-a-dp-master-system)
  
[What you need to know about direct data exchange](#what-you-need-to-know-about-direct-data-exchange)
  
[Example of how to configure an ET 200 CPU as an I-slave](#example-of-how-to-configure-an-et-200-cpu-as-an-i-slave)

## Configuring distributed I/O systems

This section contains information on the following topics:

- [Creating a DP master system](#creating-a-dp-master-system)
- [Editing DP master systems and interfaces](#editing-dp-master-systems-and-interfaces)
- [Adding DP slaves to the master system and configuring them](#adding-dp-slaves-to-the-master-system-and-configuring-them)
- [Hint: Quick configuration of master systems](#hint-quick-configuration-of-master-systems)
- [Assigning a DP slave to a SYNC/FREEZE group](#assigning-a-dp-slave-to-a-syncfreeze-group)

### Creating a DP master system

#### Introduction

To create a PROFIBUS DP master system, you need to have one DP master and at least one DP slave. As soon as you connect a DP master to a DP slave via their PROFIBUS DP interfaces, a master-slave link is established.

#### DP master and DP slave

As the DP master, you can use the following devices with a DP interface:

- CPU with a permanently integrated or plug-in DP master interface
- CP in conjunction with a CPU
- Interface module assigned to a CPU/FM
- Interface module with a DP master interface

As DP slave, you can use head modules of the distributed I/O with PROFIBUS DP interface or CPUs as intelligent DP slaves.

With some devices, you can switch between the possible modes (such as "DP master" or "DP Slave") under "Operating mode" in the Inspector window of the DP interface. Select the option button with the required mode.

#### Requirement

- You are in the network view.
- The hardware catalog is open.

#### Procedure

To create a DP master system for example with a CPU 319-3 PN/DP , follow these steps:

1. Select a CPU 319-3 PN/DP as a potential DP master from the hardware catalog.
2. Drag the CPU onto the free area within the network view.
3. Right click on the DP interface of the CPU.
4. Select "Create master system" from the shortcut menu.

A DP master system with a CPU 319-3 PN/DP as DP master will be created as the only node.

If you connect the DP interface of a DP slave to the DP interface of the DP master, the DP slave will be added automatically to the DP master system. If there is not yet a subnet between the DP master and DP slave, a new subnet is created between the DP master and DP slave.

To include an IM 155-6 DP HF as a DP slave in the DP master system, for example, follow the steps below:

1. Click the DP interface of either the DP master or DP slave.
2. Hold down the mouse button and draw a connecting line between this DP interface and that of the desired communication partner.

or

1. Click on the hyperlink of the DP slave IM 155-6 DP HF.
2. Select the required DP master from the list of possible DP masters displayed.

The DP slave IM 155-6 DP HF is included in the DP master system with the CPU 319-3 PN/DP as DP master.

![Procedure](images/78486345611_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drag between the DP interfaces of DP slave to DP master. |
| ② | Click on the link of an unassigned DP slave, and a selection of possible DP masters opens. |

If necessary, adapt the properties of the PROFIBUS subnet or of the DP master (e.g. PROFIBUS address) in the Inspector window under "Properties".

> **Note**
>
> If you use the mouse to draw a connecting line between the MPI interface of a DP master and the PROFIBUS interface of a DP slave, the MPI interface of the DP master will automatically be configured as a PROFIBUS interface and a DP master system will be created.

#### DP master display on the DP slave

When a DP slave is connected to a DP master, the name of the DP master is displayed on the DP slave as a hyperlink. Click the hyperlink to select the associated DP master.

![DP master display on the DP slave](images/78499354891_DV_resource.Stream@PNG-de-DE.png)

#### Highlighting applied to the DP master system

When you create a new DP master system, highlighting will be applied to it. This enables you to identify quickly which devices belong to the DP master system. You can also highlight a DP master system yourself by moving the mouse pointer over a subnet. This will result in the names of the available DP master systems being displayed. Click the required DP master system to highlight it.

![Highlighting applied to the DP master system](images/78499359755_DV_resource.Stream@PNG-en-US.png)

There are various ways of removing the highlighting from a DP master system:

- Highlight a different DP master system.
- Click the drawing pin with the name of the DP master system in the top right-hand corner of the network view.

---

**See also**

[DP/DP coupler in the hardware catalog](#dpdp-coupler-in-the-hardware-catalog)
  
[The basics of configuring a DP master system](#the-basics-of-configuring-a-dp-master-system)

### Editing DP master systems and interfaces

#### Introduction

Once you have created a DP master system, you also have the option of disconnecting the DP master system and its components. This can result in subnets with DP slaves but no DP master.

Generally, there is no need to edit the interfaces of a DP master.

You can change the name and number on the DP master system.

#### Disconnection from DP master systems

If you have configured either a CPU with an integrated PROFIBUS DP interface or a PROFIBUS CP (that can be configured as an intelligent DP slave) as a DP master with master system, then you will be able to disconnect the DP master from the DP master system. After this, the device will no longer be connected to the DP master system.

Disconnecting the subnet for a DP master effectively eliminates the master system in the sense that it is no longer assigned to a DP master. However, the individual DP slaves remain interconnected via the subnet and any direct data exchange that has been configured remains unaffected.

If you delete the DP slaves or detach them from the master system, the master system is retained on the DP master.

#### Requirement

- You must be in the network view.
- There has to be a DP master system with one DP master and at least one DP slave.

#### Disconnecting the DP master from the DP master system

To disconnect the DP master system, proceed as follows:

1. Right-click on the DP master's DP interface.
2. Select "Disconnect from master system" from the shortcut menu.

The selected DP master will be disconnected from the DP master system. A subnet with the DP slaves will be retained.

#### Adding a DP master to the DP master system

To reassign a DP master to a subnet, proceed as follows:

1. Right-click on the DP master's DP interface.
2. Select "Create master system" from the shortcut menu.
3. Draw connecting lines between the new DP master system and the DP interfaces of the DP slaves.

The DP master combines with the DP slaves to recreate a DP master system.

#### Ensuring the online capability of PROFIBUS DP interfaces

To enable a CPU's integrated MPI/DP interface to actively participate in PROFIBUS DP communication, proceed as follows:

1. Select the CPU interface symbol in the device or network views.
2. In the inspector window, select the parameter "Interface type: PROFIBUS" under "MPI address"..
3. If necessary change the suggested PROFIBUS address.
4. If required and available, select an existing subnet under "Subnet".

**Note**

If you use the mouse to draw a connecting line from the PROFIBUS interface of a DP slave to the MPI interface of a DP master, the MPI interface of the DP master will automatically be configured as a PROFIBUS interface and a DP master system will be created.

#### Editing the properties of a DP master system

To edit the properties of a DP master system, proceed as follows:

1. Move the mouse pointer over a subnet with a DP master system.
2. A message will appear displaying the available DP master systems. Click the one you want to edit. The DP master system will now be color-highlighted.
3. Now click the DP master system that has been color-highlighted.
4. In the inspector window, edit the DP master system attributes under "Properties &gt; General".

**Note**

If you click a subnet when no DP master system is highlighted, you will be able to edit the properties of the entire subnet under "Properties" in the inspector window.

### Adding DP slaves to the master system and configuring them

In the network view, you can add various DP slaves from the hardware catalog directly by using the drag-and-drop function or by double-clicking.

#### Types of DP slaves

For configuration purposes, DP slaves are broken down into the following categories:

- Compact DP slaves  
  (Modules with integrated digital/analog inputs and outputs, for example, ET 200L)
- Modular DP slaves  
  (interface modules with S5 or S7 modules assigned, for example ET 200M)
- Intelligent DP slaves (I-slaves)  
  (SIMATIC S7-300 with, for example, CP 342-5, CPU 315-2 DP, or ET 200S with IM 151-7 CPU)

#### Slot rules

- Your DP master system should only contain one DP master, but it may contain one or or more DP slaves.
- Your DP master system must not exceed the number of DP slaves specified on the DP master.

  > **Note**
  >
  > When configuring the DP master system, remember to observe the DP master technical data (max. number of nodes, max. number of slots, max. quantity of user data). Slot or user data restrictions may prevent you from being able to use the maximum number of nodes that is theoretically possible.

#### Requirements

- You are in the network view.
- A DP master system must have been created.

#### Adding a DP slave to the DP master system

To add a DP slave from the hardware catalog to the DP master system, follow these steps:

1. Select a modular DP slave (for example ET 200M) from the hardware catalog.
2. Drag-and-drop the DP slave from the hardware catalog into the network view.
3. Draw a connecting line between the DP master's DP interface or a highlighted DP master system and the DP interface of the new DP slave.

A DP master system will be generated and the DP slave will be connected to the DP master automatically.

> **Note**
>
> When a DP master system is highlighted, you can double-click the required DP slave in the hardware catalog. This will result in the DP slave being added to the highlighted DP master system automatically.

#### Disconnecting a DP slave from the DP master system

To disconnect a DP slave from the DP master system, follow these steps:

1. In the network view, right-click on the DP slave's DP interface.
2. From the shortcut menu, select the method for disconnecting from the DP master system:

   - "Disconnect from subnet": The PROFIBUS connection is broken and the device is no longer connected to the DP master system or a subnet.
   - "Disconnect from master system": The DP slave remains connected to the subnet, but is no longer assigned to the DP master system as a DP slave.

The selected DP slave will be disconnected from the DP master system.

You can also disconnect directly using the shortcut menu of the DP slave:

1. In the network view, right-click on the DP slave.
2. Select "Disconnect from DP master/IO system" from the shortcut menu.

The DP slave remains connected to the subnet, but is no longer assigned to the DP master system as a DP slave.

#### Assigning a DP slave to a new DP master system

To assign an existing DP slave to a new DP master system, follow these steps:

1. Right-click on the DP slave's DP interface.
2. From the shortcut menu, select "Assign to new master".

   It does not matter whether the DP slave concerned is already assigned to another DP master system.
3. From the selection list, select the DP master with the DP master system to which you want to connect the DP slave.

   The selected DP slave is now assigned to a new DP master system.

The "Assign to new subnet" function works in a similar way in that it allows you to connect a DP slave to a new subnet. However, in this case, the DP slave will not be connected to an existing DP master system.

You can also make the assignment directly using the shortcut menu of the DP slave:

1. Right-click the DP slave.
2. From the shortcut menu, select "Assign new DP master/IO system".
3. Select the DP master from the list of available DP masters.

The selected DP slave has now been assigned to a new DP master system.

> **Note**
>
> If there is only one DP master on a subnet, you only have to connect the interface of the DP slave to the subnet of this DP master with drag-and-drop. The DP slave is then connected to the subnet of the DP master immediately, and the DP slave is assigned to this DP master.

#### Configuring a DP slave

To configure a DP slave, follow these steps:

1. Switch to the DP slave's device view.
2. Select the desired modules from the hardware catalog. In the case of modular DP slaves, the possible modules can be found within the hardware catalog underneath the relevant DP slave "family". You should, therefore, use the hardware catalog's filter function to facilitate the process of locating them.
3. Drag-and-drop the required modules from the hardware catalog onto the rack of the DP slave.
4. Configuring the DP slave and inserted modules in the inspector window.

---

**See also**

[Creating a DP master system](#creating-a-dp-master-system)
  
[DP slaves within the hardware catalog](#dp-slaves-within-the-hardware-catalog)
  
[Browsing the hardware catalog](Configuring%20devices%20and%20networks.md#browsing-the-hardware-catalog)
  
[Rack: Basics](Configuring%20devices%20and%20networks.md#rack-basics)
  
[Rack: Inserting a module](Configuring%20devices%20and%20networks.md#rack-inserting-a-module)

### Hint: Quick configuration of master systems

If the DP master system has several DP slaves, use drag-and-drop operation to assign to the master in one step all DP slaves that were placed.

#### Requirement

DP master and DP slaves are placed in the network view.

#### Assigning DP slaves to a DP master system

To do this, follow these steps:

1. Select an appropriate zoom factor so that you can see as many DP slaves as possible in the network view.
2. Arrange the DP slaves in a maximum of two rows.
3. Select all DP interfaces with the mouse cursor (not all devices!). This only works if you begin to drag the mouse cursor outside of the first DP slave and release the mouse button at the last DP slave (selection with the lasso).

   ![Assigning DP slaves to a DP master system](images/26008497675_DV_resource.Stream@PNG-en-US.png)

   ![Assigning DP slaves to a DP master system](images/26008497675_DV_resource.Stream@PNG-en-US.png)
4. Select the shortcut menu "Assign to new master" and select the corresponding DP interface for the DP master in the subsequent dialog.

   ![Assigning DP slaves to a DP master system](images/26008506123_DV_resource.Stream@PNG-en-US.png)

   ![Assigning DP slaves to a DP master system](images/26008506123_DV_resource.Stream@PNG-en-US.png)
5. The DP slaves are automatically networked with the DP master and combine with it to form a DP master system.

**Note**

When a DP master system is highlighted, you can double-click on a DP slave in the hardware catalog and thereby quickly add additional DP slaves. This will result in the DP slave being added to the highlighted DP master system automatically.

### Assigning a DP slave to a SYNC/FREEZE group

#### Introduction

Assuming that it supports this function, a DP master can send the SYNC and/or FREEZE control commands to a group of DP slaves simultaneously in order to synchronize them. If you require this, you will need to assign the DP slaves to SYNC/FREEZE groups.

#### Requirement

A DP master system must have been created.

#### Procedure

To assign a DP slave to a SYNC/FREEZE group, follow these steps:

1. In the device or network views, select the DP slave interface that you want to assign to a group.
2. In the inspector window under "Sync/Freeze" group, select the check box for the Sync/Freeze group you want.

**Note**

You can assign a DP slave to a maximum of one SYNC/FREEZE group.

Exception: If you are using a CP 342-5 as the DP master, you can assign up to eight SYNC/FREEZE groups to each assigned DP slave.

Please also note the documentation relating to the CP 342-5.

#### What you need to know about the SYNC and FREEZE control commands

Using the SYNC and FREEZE control commands on the DP master, you can synchronize the DP slaves on an event-driven basis. The DP master simultaneously sends the control commands to all the DP slaves that make up a group within its master system. Any DP slaves that have failed or currently have diagnostics pending will be ignored.

Before DP slaves can be synchronized using control commands, you must first assign the DP slaves to SYNC/FREEZE groups.

For an S7 CPU, use the instruction DPSYC_FR (SFC 11) to synchronize the DP slaves.

When you select the DP master, a list of the eight SYNC/FREEZE groups is displayed in the Inspector window under "Properties &gt; DP interface &gt; SYNC/FREEZE" or "Properties&gt; MPI/DP interface &gt; SYNC/FREEZE" (when operating as a PROFIBUS interface).

> **Note**
>
> There are DP slaves which are only SYNC-capable or only FREEZE-capable. Refer to the "SYNC/FREEZE" area in the DP interface properties to find out which of these functions a DP slave supports.
>
> In order to be able to assign to such a DP slave of a SYNC or FREEZE group, you need to restrict the affected group to the function that the DP slave supports in the DP master interface properties.
>
> Example: For a slave that is only FREEZE-capable, you need to clear the "SYNC" checkbox in the SYNC/FREEZE group of the DP master.

#### The SYNC control command

The DP master sends the SYNC command to freeze the output states on a group of DP slaves so that they retain the current value.

When subsequent message frames arrive, the DP slaves will store the output data from the DP master. However, the DP slave output states will remain unchanged.

Then, when a new SYNC control command is sent, each DP slave will align its outputs with the values of the output data from the DP master.

Cyclic updating of the outputs will only resume when the DP master sends the UNSYNC control command.

#### The FREEZE control command

When they receive the FREEZE control command from the DP master, the DP slaves within the relevant group will freeze the current state of their inputs The DP slaves send this frozen input data to the DP master in the following cyclic frames.

Whenever they receive a new FREEZE control command, the DP slaves will freeze the current state of their inputs again.

Cyclic transfer of the state of the DP slave inputs from the DP slave to the DP master will only resume when the DP master sends the UNFREEZE control command.

---

**See also**

[Creating a DP master system](#creating-a-dp-master-system)
  
[Setting PROFIBUS properties](#setting-profibus-properties)

## Example: Configuring ET 200S as DP slave

This section contains information on the following topics:

- [Configuring an ET 200S](#configuring-an-et-200s)
- [Packing addresses](#packing-addresses)
- [Configuring option handling with standby modules](#configuring-option-handling-with-standby-modules)
- [Configuring option handling without standby modules](#configuring-option-handling-without-standby-modules)
- [Configuring the ET 200S in DPV1 mode](#configuring-the-et-200s-in-dpv1-mode)
- [Additional configurations](#additional-configurations)

### Configuring an ET 200S

#### Introduction

DP slaves and I/O devices from the ET 200S family are configured in the same way as other modular DP slaves and I/O devices. The modules for the ET 200S are available in the hardware catalog under "Distributed I/O".

#### Slot rules for configuring an ET 200S

The following rules apply when configuring an ET 200S:

- Do not leave any gaps when inserting the ET 200S modules.
- Slot 1: only for PM-E or PM-D Power Modules.
- To the left of an Electronics Module (EM): an EM or a Power Module (PM-E or PM-D) only.
- To the left of Motor Starter (MS): an MS, a PM-D, PM-D Fx (1..x..4) Power Module or a PM-X Power Module only.
- To the left of a PM-X: a motor starter or a PM-D only
- Up to 63 modules and one IM Interface Module are permitted

  > **Note**
  >
  > Remember to ensure that the correct PM-E and EM voltage ranges are assigned.

#### Operation when expected and actual configurations do not match

This parameter controls the response during startup, and when modules are removed and inserted during operation (cyclical data exchange).

Check box is selected (operation is permitted if preset configuration is not the same as actual configuration):

- The module will start up even if the preset configuration is not equal to the actual configuration.
- The module remains in cyclical data exchange following removal and insertion (not a CPU stop).

Check box is cleared (operation is not permitted if preset configuration is not the same as actual configuration):

- The module will not start up (does not switch over to cyclical data exchange) if the preset configuration is different from the actual configuration.
- If modules are removed and inserted during operation, this causes a CPU stop, and the module no longer participates in the cyclical data exchange.

Refer to the manual for the respective module for information on which constraints cause a CPU stop, or prevent the data exchange starting, even if operation is enabled when preset configuration is not the same as the actual configuration.

#### Interference frequency suppression

The frequency of your alternating current network can interfere with the measured value in the following cases in particular: measurement in small voltage ranges and measurement with thermocouples. Set the frequency of the power for the entire ET 200S to that which predominates in your plant.

The analog electronic modules AI set their integration time or conversion time in relation to the selected interference frequency suppression.

#### Configuring reference junctions

A reference junction is the connection of a thermocouple to a supply line (generally in the terminal box). The voltage that occurs due to the effects of temperature falsifies the temperature value measured by the module.

On the ET 200S, one channel of the AI RTD module can be programmed as a reference junction. Other AI TC modules can correct their measured values using the temperature at the reference junction as measured by this module.

![Configuring reference junctions](images/26458899339_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  |  |
| ① | Configuring the AI TC: → Selection of the reference junction used |
| ② | Configuring of the AI RTD:  → Activation of the reference junction → Specifying the slot and channel of the AI RTD |

#### Special characteristics to be noted when assigning parameters for reference junctions

The process of assigning parameters for reference junctions will be explained based on the example of a resistance thermometer with a Pt 100 climatic range that is used for measuring the reference junction temperature.

To assign parameters for the reference junction, follow these steps:

1. In the ET 200S device view, insert an analog RTD electronics module, for example a 2AI RTD HF. The module must support the "thermal resistor" measuring type (linear, 4-wire) and the "Pt 100 climatic range" measuring range.
2. Select the module on the rack.
3. Under "Properties &gt; General &gt; Inputs" in the inspector window, set a channel for the reference junctions function.

   Measuring type: Thermal resistor (linear, 4-wire)

   Measuring range: Pt 100 climatic range
4. Select the ET 200S (that is, the interface module).
5. Under "Properties &gt; General &gt; Module parameters &gt;Reference junctions" in the inspector window, select the "Reference junction" check box and specify the slot and the channel number of the relevant RTD module.
6. Insert the analog electronics module for measuring the temperature using a thermocouple (TC module) and select the option "RTD" as a reference junction under "Properties &gt; General &gt; Inputs &gt; Channel x" in the inspector window.

#### Additional information

For additional information on the various types and uses of ET 200S modules, please refer to the operating instructions and the manual titled "ET 200S Distributed I/O System".

For additional information on analog value processing, please see the documentation for the ET 200S distributed I/O system.

---

**See also**

[Configuring the ET 200S in DPV1 mode](#configuring-the-et-200s-in-dpv1-mode)
  
[Documentation on ET 200S](http://support.automation.siemens.com/WW/view/en/1144348)

### Packing addresses

#### Introduction

DP slaves and I/O devices from the ET 200S family are configured in the same way as other modular DP slaves and I/O devices. As well as supporting all the standard modular DP slave and I/O device functions, the ET 200S also offers the "Pack addresses" function:

When digital electronics modules requiring an address space of 2 or 4 bits are inserted into the device view, they will initially be spread over a total area of 1 byte. However, the address area actually occupied can be compressed after configuration using the "Pack addresses" function.

|  | Initial state | After "Pack addresses" |
| --- | --- | --- |
| Module | I address | I address |
| 2DI (2-bit) | Byte 10 | 10.0 to 10.1 |
| 4DI (4-bit) | Byte 11 | 10.2 to 10.5 |

#### Requirement

- You are in the device view.
- An ET 200S, for example an IM 151-1, must be present.
- A pair of digital electronics modules, for example 2DI AC120V ST, must be inserted into the slots.

#### Packing addresses

To pack addressed, follow these steps:

1. Select the electronics modules whose addresses are to be packed. The following options are available for selecting multiple electronics modules:

   - Press and hold down &lt;Shift&gt; or &lt;Ctrl&gt; while clicking the relevant electronics modules.
   - Click off the rack and select the required electronics modules by drawing round them with the mouse.
2. Click "Pack addresses" in the shortcut menu for the selected electronics modules.

The address areas for inputs, outputs and motor starters are packed separately. The packed addresses will be displayed in the I address and Q address columns of the device overview.

#### How packed addresses are generated and structured

If you make use of the "Pack addresses" function, the addresses of the selected electronics modules will be packed in accordance with the following rules:

- The start of the address area is determined by the lowest address of the selected electronics modules: X.0
- If the bit address is not "0", then the next (free) byte address as of which the selected area can be compacted will be selected automatically: (X+n).0
- If no coherent area exists, the addresses will be automatically packed into any available address gaps.

Electronics modules with packed addresses and the same byte address form a packing group.

#### Unpacking addresses

To unpack addressed, follow these steps:

1. Select one or more electronics modules with packed addresses.
2. Click "Unpack addresses" in the shortcut menu for the selected electronics modules.

The packing groups of the selected electronics modules will be disbanded and the packed addresses for the relevant electronics modules unpacked.

The packing group will also be disbanded and the packed addresses unpacked in the following cases: if you delete electronics modules from a packing group, move electronics modules out of a packing group or insert electronics modules on a free slot within a packing group.

The start addresses of the unpacked electronics modules will be assigned to the next available byte addresses in each case.

#### Special characteristics of electronics modules with packed addresses

The following special characteristics apply to electronics modules with packed addresses:

- As far as the CPU is concerned, there is no way of assigning a slot for the electronics module. Consequently, the instruction GADR_LGC (SFC 5) outputs error information W#16#8099 "Slot not configured" for the actual slot of the electronic module.
- The instruction LGC_GADR (SFC 49) and SZL-ID W#16#xy91 "module status information" cannot be evaluated for an electronics module.
- The electronics module receives an additional diagnostics address via the DPV1 function, because otherwise the packed addresses would prevent interrupts from being assigned as far as the CPU is concerned.
- The "Insert/remove interrupt" is not possible. This is because the "Pack addresses" and "Insert/remove interrupt" functions are mutually exclusive.

### Configuring option handling with standby modules

You can use the option handling function to prepare the ET 200S with PROFIBUS interface for future expansions (options). This section describes option handling with standby modules.

You do this by assembling, wiring, configuring, and programming the maximum configuration envisaged for the ET 200S and by using cost-effective standby modules (138-4AA00 or 138-4AA10) during assembly until it becomes time to replace them with the necessary electronics modules.

> **Note**
>
> The ET 200S can be completely factory-wired with the master cabling, as no connection exists between a standby module and the terminals of the terminal module (and, in turn, to the process).

#### Requirement

- ET 200S interface module

  - IM 151-1 STANDARD (6ES7 151-1AA03-0AB0 or higher)
  - IM 151-1 FO STANDARD (6ES7 151-1AB02-0AB0 or higher)
- Power module with option handling

  - PM-E DC24..48V
  - PM-E DC24..48V/AC24..230V

#### Procedure

To activate option handling, follow these steps:

1. Select the IM 151-1 in the device view and enable it in "Option handling" check box under "Properties &gt; General &gt; Option handling" in the inspector window.
2. Select the numbered check boxes for the slots that are initially to accommodate the standby modules prior to the future electronics modules.
3. Select the power module in the device view and enable it in the "Option handling" check box under "Properties &gt; Addresses" in the inspector window. Reserve the necessary address space for the control and check-back interface in the process image output (PIQ) and process image input (PII).

The assembled standby modules can be replaced with the configured modules at a later date without having to modify the configuration.

> **Note**
>
> The addresses for these interfaces are reserved as soon as you activate option handling on the power module. The "Option handling" function must also be activated on the DP slave (IM 151-1 STANDARD Interface Module). If it is not activated, the addresses reserved for the control and check-back interface will be released again.
>
> Note that activating and deactivating the option handling function repeatedly can change the address of the control and check-back interface.
>
> Option handling may be activated for one PM-E DC24..48V or one PM-E DC24..48V/AC24..230V Power Module only.

#### Additional information

For additional information on the assignment and significance of bytes within the process image, option handling with PROFIBUS and the use of standby modules, please refer to the documentation for the ET 200S distributed I/O system.

#### How option handling works during startup

If "Startup when expected/actual config. differ" is not available, the ET 200S will still start up if a standby module is inserted instead of the configured electronics module and option handling has been activated for the slot concerned.

#### How option handling works during operation

During operation, the option handling mode varies in accordance with the following:

- Option handling enabled for a slot:   
  Either the standby module (option) or the configured electronics module can be plugged into this slot. If any other kind of module is present on this slot, diagnostics will be signaled (no module/incorrect module).
- Option handling disabled for a slot:   
  Only the configured electronics module can be plugged into this slot. If any other kind of module is present, diagnostics will be signaled (no module/incorrect module).

#### Standby module substitute values

- Substitute value for digital inputs: 0
- Substitute value for analog inputs: 0x7FFF

#### Control and evaluation in the user program

The ET 200S is equipped with a control and feedback interface for the "Option handling" function.

The control interface is located in the process image output (PIQ). Each bit in this address area controls one of the slots from 2 to 63:

- Bit value = 0: Option handling parameterized. Standby modules are permitted.
- Bit value = 1: Option handling canceled. Standby modules are not permitted on this slot.

The check-back interface is located in the process image input (PII). Each bit in this address area provides information about the modules that are actually plugged into slots 1 to 63:

- Bit value = 0: This slot has the standby module, an incorrect module or no module plugged into it.
- Bit value = 1: The configured module is plugged into this slot.

---

**See also**

[Which modules support option handling?](http://support.automation.siemens.com/WW/view/en/22564754)

### Configuring option handling without standby modules

You can use the option handling function to prepare the ET 200S for future expansions (options) without installing standby modules. This section describes option handling without standby modules.

> **Note**
>
> **ET 200S with PROFINET interface**
>
> This description refers to the ET 200S with PROFIBUS interface. In principle, option handling for ET 200S with PROFINET interface functions as described here without standby modules. PN interface modules are to be used instead of the DP interface modules listed here. You can find additional information about option handling for ET 200S with PROFINET interface in the corresponding manuals.

#### Requirement

- ET 200S interface module

  - IM 151-1 HIGH FEATURE (6ES7151-1BA02 or higher)
  - IM 151-1 STANDARD (6ES7 151-1AA05-0AB0 or higher)
- Power module with option handling

  - PM-E DC24..48V
  - PM-E DC24..48V/AC24..230V

#### Procedure

To activate option handling, follow these steps:

1. Select the IM 151-1 in the device view and enable it in "Option handling" check box under "Properties &gt; General &gt; Option handling" in the inspector window.
2. Select the power module in the device view and enable it in the "Option handling" check box under "Properties &gt; Addresses" in the inspector window. Reserve the necessary address space for the control and check-back interface in the process image output (PIQ) and process image input (PII).
3. Configure the slave's maximum configuration. The selection/clearing of options is controlled via the user program.

**Note**

The addresses for these interfaces are reserved as soon as you activate option handling on the power module. The "Option handling" function must also be activated on the DP slave (IM 151-1 interface module). If it is not activated, the addresses reserved for the control and check-back interface will be released again.

Note that activating and deactivating the option handling function repeatedly can change the address of the control and check-back interface.

Option handling may be activated for one PM-E DC24..48V or one PM-E DC24..48V/AC24..230V Power Module only.

#### Additional information

For additional information on the assignment and significance of bytes within the process image, option handling with PROFIBUS and the use of standby modules, please refer to the documentation for the ET 200S distributed I/O system.

#### Control and evaluation in the user program

The ET 200S is equipped with a control and feedback interface for the "Option handling" function.

The control interface is located in the process image output (PIQ). Each bit in this address area controls one of the slots from 1 to 63:

- Bit value = 0: Slot is not available in the actual configuration.
- Bit value = 1: Slot is available in the actual configuration.

The check-back interface is located in the process image input (PII). Each bit in this address area provides information about the modules that are actually plugged into slots 1 to 63:

- Bit value = 0: Slot belongs to an option that is not available or module status is faulty.
- Bit value = 1: The configured module is plugged into this slot.

---

**See also**

[Sample applications for ET 200S, option handling without standby module](http://support.automation.siemens.com/WW/view/en/29430270)

### Configuring the ET 200S in DPV1 mode

PROFIBUS DPV1 enables you to access extended PROFIBUS functions.

#### Requirement

- You must be in the network view.
- An DP master with DPV1 functionality must be available.
- A master-slave connection must be established with PROFIBUS.

#### Procedure

To switch the DP slave over to DPV1, follow these steps:

1. Select the DP slave.
2. Under "Properties &gt; Module parameters" in the inspector window, select "DPV1" mode from the "DP interrupt mode" drop-down list box.

or

1. Select the DP master.
2. In the I/O communications table select the row with the connection between the DP master and the desired DP slave.
3. Under "Properties &gt; Module parameters" in the inspector window, select "DPV1" mode from the "DP interrupt mode" drop-down list box.

#### Special characteristics

The parameters are subject to interdependencies, which are outlined below:

| Parameter | DPV0 mode | DPV1 mode |
| --- | --- | --- |
| Operation when target configuration does not match actual configuration | Fully available | Fully available |
| Diagnostics interrupt (OB 82) | Not available, not set | Fully available |
| Hardware interrupt (OB 40 to 47) | Not available, not set | Fully available |
| Insert/remove interrupt (OB 83) | Not available, not set | Only available when addresses are not packed.  "Startup when target configuration does not match actual configuration" is activated automatically along with an insert/remove interrupt. |

#### Interrupts in the case of modules with packed addresses

If the module is capable of triggering interrupts and the bit address is not equal to 0 because of packed addresses, you will need to assign a diagnostics address in the ET 200S address dialog.

The diagnostics address is required for the purpose of assigning a DPV1 interrupt to the module as an interrupt trigger. The CPU will only be able to assign an interrupt correctly and store information on the interrupt in the interrupt OB start information/in the diagnostics buffer if the module concerned has this "unpacked" address. In this context, the CPU cannot make use of "packed" addresses.

From the point of view of interrupt processing (interrupt OB), this means the module will have the assigned diagnostics address, but from the point of view of processing the input and output data in the user program, the module will have the packed addresses.

> **Note**
>
> When the module addresses are packed, the insert/remove interrupt for the ET 200S is unavailable.

---

**See also**

[Introduction to PROFIBUS DPV1](#introduction-to-profibus-dpv1)
  
[Configuring DPV1 devices](#configuring-dpv1-devices)
  
[Configuring an ET 200S](#configuring-an-et-200s)

### Additional configurations

#### Configuring additional functions

The ET 200S distributed I/O system has numerous additional functions that are available via plug-in modules (e.g. communication module). You can find the descriptions for these in the sections "Using technology functions" and "Configuration for point-to-point connections".

#### Additional distributed I/O systems

Information on additional distributed I/O systems is available by following further links under "See also".

---

**See also**

[Configuring and assigning parameters to 1Count24V (S7-300, S7-400)](Using%20ET%20200S%201Count24V%20%28S7-300%2C%20S7-400%29.md#configuring-and-assigning-parameters-to-1count24v-s7-300-s7-400)
  
[Configuring and assigning parameters to 1Count5V (S7-300, S7-400)](Using%20ET%20200S%201Count5V%20%28S7-300%2C%20S7-400%29.md#configuring-and-assigning-parameters-to-1count5v-s7-300-s7-400)
  
[Configuring and assigning parameters to 1SSI (S7-300, S7-400)](Using%20ET%20200S%201SSI%20%28S7-300%2C%20S7-400%29.md#configuring-and-assigning-parameters-to-1ssi-s7-300-s7-400)
  
[Configuring and assigning parameters to 1PosU (S7-300, S7-400)](Using%20ET%20200S%201PosU%20%28S7-300%2C%20S7-400%29.md#configuring-and-assigning-parameters-to-1posu-s7-300-s7-400)
  
[1STEP 5V configuration and parameter assignment (S7-300, S7-400)](Using%20ET%20200S%201STEP%205V%20%28S7-300%2C%20S7-400%29.md#1step-5v-configuration-and-parameter-assignment-s7-300-s7-400)
  
[Distributed I/O](Configuring%20devices%20and%20networks.md#distributed-io)

## Configuring intelligent DP slaves

This section contains information on the following topics:

- [Adding an I-slave to a DP master system](#adding-an-i-slave-to-a-dp-master-system)
- [Configuring diagnostics addresses (S7-300, S7-400)](#configuring-diagnostics-addresses-s7-300-s7-400)
- [Interrupts on the I-slave](#interrupts-on-the-i-slave)
- [Example of how to configure a CP as an I slave](#example-of-how-to-configure-a-cp-as-an-i-slave)
- [Example of how to configure a CPU as an I slave](#example-of-how-to-configure-a-cpu-as-an-i-slave)
- [Example of how to configure an ET 200 CPU as an I-slave](#example-of-how-to-configure-an-et-200-cpu-as-an-i-slave)
- [Example: Configuring an I-slave (S7-1500, ET 200SP CPU)](#example-configuring-an-i-slave-s7-1500-et-200sp-cpu)
- [Example: Configuring transfer areas](#example-configuring-transfer-areas)
- [Diagnostics and interrupt behavior (S7-1500, ET 200SP CPU)](#diagnostics-and-interrupt-behavior-s7-1500-et-200sp-cpu)

### Adding an I-slave to a DP master system

#### Introduction

One of the key characteristics of intelligent DP slaves (I-slaves) is that the DP master is not provided with I/O data directly by a real I/O, but by a preprocessing CPU. Together with the CP, this preprocessing CPU forms the I-slave.

![Introduction](images/9783621387_DV_resource.Stream@PNG-en-US.png)

#### Difference: DP slave v. intelligent DP slave

In the case of a DP slave, the DP master accesses the distributed I/O directly.

In the case of an intelligent DP slave, the DP master actually accesses a transfer area in the I/O address space of the preprocessing CPU instead of accessing the connected I/O of the intelligent DP slave. The user program running on the preprocessing CPU is responsible for ensuring data exchange between the address area and I/O.

> **Note**
>
> The I/O areas configured for data exchange between the DP master and DP slaves must not be used by I/O modules.

#### Applications

Configurations involving intelligent DP slaves:

- I-slave &lt;&gt; DP master data exchange
- Direct DP slave &gt; I-slave data exchange

#### Procedure

To add an I-slave to a DP master system, proceed as follows:

1. From the hardware catalog, drag two devices with PROFIBUS DP interface for configuration as DP master and I-slave (e.g. CPU 317-2 DP) into the network view.
2. Switch the device that is to be used as the I-slave over to "Slave" mode under "Properties &gt; DP interface" in the Inspector window. The device will now operate as an intelligent DP slave.
3. Draw a connecting line between the DP interfaces of both devices. This way you connect the I-slave with a DP master in a DP master system.

#### Result

You have now set up a DP master system with one DP master and one I-slave.

Please note the following I-slave configuration examples:

- [Configuring a CP as an I-slave](#example-of-how-to-configure-a-cp-as-an-i-slave)
- [Configuring a CPU as an I-slave](#example-of-how-to-configure-a-cpu-as-an-i-slave)
- [Configuring a DP slave as an I-slave](#example-of-how-to-configure-an-et-200-cpu-as-an-i-slave)

---

**See also**

[Interrupts on the I-slave](#interrupts-on-the-i-slave)
  
[Configuring diagnostics addresses (S7-300, S7-400)](#configuring-diagnostics-addresses-s7-300-s7-400)

### Configuring diagnostics addresses (S7-300, S7-400)

#### Introduction

When assigning diagnostics addresses for PROFIBUS DP, you must ensure that DP diagnostics addresses are assigned to both the DP master and the I-slave.

![Introduction](images/96639996811_DV_resource.Stream@PNG-en-US.png)

#### Diagnostics addresses

A distinction is made between diagnostics addresses on the DP master and those on the I-slave:

- Diagnostics addresses on the DP master

  The DP master receives information about the status of the DP slave or a bus interruption via the diagnostics addresses assigned to the DP master.
- Diagnostics addresses on the I-slave

  The I-slave receives information about the status of the DP master or a bus interruption via the diagnostics addresses assigned to the I-slave.

STEP 7 automatically assigns diagnostics addresses for the respective CPUs when the master-I-slave configuration is specified. The following describes how to change the specified diagnostics addresses.

Tip: In order to obtain an overview of all addresses assigned for the CPU, including diagnostics addresses, select the "Address overview" area in the inspector window of the selected CPU.

#### Diagnostics addresses of the I-slave communication

A table with the diagnostics addresses of the I-slave communication is displayed on the I-slave. The identifier for the diagnostics address is the name of the PLC and the transfer area with the lowest subslot number. You can edit the diagnostics addresses used in the table.

![Diagnostics addresses of the I-slave communication](images/96685281803_DV_resource.Stream@PNG-en-US.png)

The table is only displayed when at least the DP master or the I-slave is a CPU 300/400:

| DP master | I-slave | Display of the diagnostics addresses |
| --- | --- | --- |
| CPU 300/400 | CPU 300/400 | Local and remote addresses of the I-slave |
| CPU 300/400 | CPU 1200/1500 | Remote addresses of the I-slave |
| CPU 1200/1500 | CPU 300/400 | Local addresses of the I-slave |
| CPU 1200/1500 | CPU 1200/1500 | No display |

#### Requirement

- You must be in the network view.
- You must have set up a DP master system with a DP master and an I-slave.

#### Procedure

To edit the diagnostics addresses for the I-slave communication, follow these steps:

1. Select the DP master or the I-slave.
2. In the I/O communication table, select the line showing "I-slave" mode.
3. Edit the diagnostics addresses under "Properties &gt; I-slave communication &gt; Diagnostics address of communication" in the Inspector window.

Or:

1. Select the I-slave.
2. Edit the diagnostics addresses under "Properties &gt;DP interface &gt; Operating mode &gt; I-slave communication &gt; Diagnostics address of communication" in the Inspector window.

You can select and edit the fields containing the values of the diagnostics addresses both for the slave and the master.

#### Additional information

For further information on diagnostics addresses, refer to the manuals for the individual S7 CPUs.

---

**See also**

[Addressing modules (S7-300, S7-400)](Configuring%20automation%20systems.md#addressing-modules-s7-300-s7-400)

### Interrupts on the I-slave

#### Types of interrupt according to DPV1 and DPV0 modes

I-slaves with the advanced instruction "SALRM" (SFB 75) can trigger interrupts on the associated DP master. The following table lists the possible types of interrupt according to the PROFIBUS DPV1 and DPV0 modes:

| Type of interrupt | DPV0 | DPV1 |
| --- | --- | --- |
| Diagnostic interrupt (OB 82) | Yes | Yes |
| Hardware interrupt (OB 40 to 47) | Yes | Yes |
| Pull/plug interrupt (OB 83) | Yes (if I-slave supports this interrupt) | Yes |
| Status interrupt (OB 55) | No | Yes |
| Update interrupt (OB 56) | No | Yes |
| Manufacturer-specific interrupt (OB 57) | No | Yes |

#### Addresses for triggering interrupts

Use the addresses configured in the I-slave's inspector window under "Properties &gt; DP interface &gt; Mode &gt; I-slave communication" to trigger interrupts with advanced instruction "SALRM". Rather than being assigned to physical modules, these addresses correspond to virtual "slots".

You cannot use the addresses relating to operating mode transitions and device diagnostics for the purpose of triggering interrupts.

#### How interrupt generation works

The principle of interrupt generation can be explained using the example of a diagnostics interrupt.

- On the I-slave, the output address 0 is assigned to a virtual slot.
- In the example, the output address 0 is used to trigger a diagnostics interrupt (OB 82) on the DP master.

Diagnostics interrupts are accompanied by data relating to individual user programs (AINFO). This data must correspond to the basic structure for supplementary interrupt information.

For example, the following simplified structure is possible:

![How interrupt generation works](images/6662043147_DV_resource.Stream@PNG-en-US.png)

#### Additional information

Note the additional information on the structure presented above in the reference manual for the S7-300/400 system and standard functions, Volume 2, "Diagnostic data" section, and in the manuals for the system and diagnostic functions of the S7-1500.

> **Note**
>
> The supplementary interrupt information affects the module status data and the group error LED of the I-slave (S7-300/400). The interrupt also affects the module status data and error LEDs of the associated DP master. Therefore, you will need to take account of what the diagnostic data records mean (data record 0 and data record 1) when compiling data for the supplementary interrupt information.

The figure below illustrates the interrupt generation process:

![Additional information](images/6669121419_DV_resource.Stream@PNG-en-US.png)

The advanced instruction "SALRM" can be called as follows:

STL

CALL FB SALRM , DB75

REQ :=M0.0

ID :=DW#16#8000 //Output address 0

ATYPE :=1 //Diagnostics interrupt

ASPEC :=1 //Incoming interrupt, EG faulty

LEN :=4 //Interrupt info is 4 bytes in length

DONE :=M1.3

BUSY :=M1.4

ERROR :=M1.5

STATUS:=MD50

AINFO :=P#M 8.0 BYTE 4 //Area for interrupt info

---

**See also**

[Introduction to PROFIBUS DPV1](#introduction-to-profibus-dpv1)
  
[Configuring DPV1 devices](#configuring-dpv1-devices)

### Example of how to configure a CP as an I slave

In this example, you are going to configure a station with a CP 342-5 as an I-slave. In order to do this, you will need to turn the CP 342-5 into an intelligent DP slave by means of the "DP slave" mode.

#### Requirements

- You must be in the network view.
- There must be a CP 342-5 available in the network view.
- The CP 342-5 must have been populated with I/O modules in the device view.
- A DP master (CPU with integrated PROFIBUS DP interface or CP with PROFIBUS DP interface) is available in the network view.

#### Procedure

To configure a CP as an I-slave, proceed as follows:

1. Select the CP 342-5.
2. In the Inspector window, switch the CP 342-5 to "DP slave" mode under "Properties &gt; Mode".
3. Draw a connecting line between the CP 342-5's DP interface and the DP interface of the DP master.
4. Select the CP 342-5.
5. Click on "I-slave communication" under "Properties &gt; Mode" in the Inspector window.
6. Edit the address assignment between the DP master and I-slave.

Alternatively, after selecting the CP 342-5 in the I/O communications table, you can call the line with the "I-slave" mode in order to edit the address assignment under "Properties" and "I-slave communication" in the Inspector window.

#### Additional information

For additional information on data exchange between the preprocessing CPU and the DP slave's internal CP 342-5 DP, please refer to the manual that deals with NCM S7 Industrial Ethernet.

### Example of how to configure a CPU as an I slave

In this example, you are going to configure a station with a CPU 31X-2 DP featuring an integrated DP interface (a CPU 315-2 DP, for example) as an I-slave. The CPU 31X-2 DP must have an integrated DP interface, and you will need to turn it into an intelligent DP slave by activating "DP slave" mode.

#### Requirements

- You must be in the network view.
- There must be a CPU 315-2 DP available in the network view.
- The CPU 315-2 DP must have been populated with I/O modules in the device view.
- A DP master (CPU with integrated PROFIBUS DP interface or CP with PROFIBUS DP interface) is available in the network view.

#### Procedure

To configure a CPU as an I-slave, proceed as follows:

1. Select the CPU 315-2 DP.
2. In the Inspector window, switch the CPU 315-2 DP to "DP slave" mode under "Properties &gt; DP interface &gt; Mode".
3. Draw a connecting line between the DP interface of the CPU 315-2 DP and the DP interface of the DP master.
4. Select the CPU 315-2 DP.
5. Click on "I-slave communication" under "Properties &gt; DP interface &gt; Mode" in the Inspector window.
6. Edit the address assignment between the DP master and I-slave.

Alternatively, after selecting the CPU 315-2 DP in the I/O communications table, you can call the line with the "I-slave" mode in order to edit the address assignment under "Properties &gt; I-slave communication" in the Inspector window.

#### Additional information

For additional information on configuring CPUs as I-slaves, please see the reference manuals for the relevant CPUs.

### Example of how to configure an ET 200 CPU as an I-slave

In this example, you are going to configure an ET 200S with Interface Module IM 151-7 CPU as an I-slave.

> **Note**
>
> You can find the interface module of the ET 200S in the hardware catalog under "PLC &gt; SIMATIC ET 200 PLC &gt; ET 200S &gt; CPU".

#### Requirements

- You must be in the network view.
- An ET 200S with IM 151-7 CPU is available in the network view.
- The ET 200S has been fitted with I/O expansion modules in the device view.
- A DP master (CPU with integrated PROFIBUS DP interface or CP with PROFIBUS DP interface) is available in the network view.

#### Procedure

To configure a DP slave as an I-slave, proceed as follows:

1. Select the IM 151-7 CPU.
2. Draw a connecting line between the DP interface of the IM 151-7 CPU and the DP interface of the DP master.
3. Select the IM 151-7 CPU.
4. In the I/O communications table, select the line showing "I-slave" mode.
5. Edit the address assignment between the DP master and I-slave under "Properties &gt; I-slave communication" in the Inspector window.

**Note**

Some stations have permanently specified interfaces for master or slave. Under "Properties &gt; MPI/DP interface" and/or "Properties &gt; DP interface" you will find the settings for the respective mode.

#### Additional information

For additional information on configuring DP slaves as I-slaves, please refer to the manuals and operating instructions for the ET 200 distributed I/O systems.

### Example: Configuring an I-slave (S7-1500, ET 200SP CPU)

#### Requirements for configuring an I-slave

The I-slave consists, for example, of the following:

- A CPU from S7-1500 and a communications module CM 1542-5/CP 1542-5 (STEP 7 as of V12)
- A CPU from ET 200SP and a communications module CM DP (STEP 7 as of V13 SP1)

#### Procedure for configuring an I-slave

This section shows how to configure an I-slave based on the example of a CPU 1512SP-1 PN. The procedure for the CPUs from S7-1500 with CM 1542-5/CP 1542-5 and for the CPU 1510SP-1 PN with CM DP is the same.

To configure an I-slave, follow these steps:

1. Drag a CPU 1512SP-1 PN from the hardware catalog to the network view.
2. Open the device view of the CPU.
3. Double-click on the CM DP communications module in the hardware catalog.  
   STEP 7 creates the CM DP in the device view.
4. Select the PROFIBUS interface of the CM DP communications module.
5. In the Inspector window in the area navigation, select the "Operating mode" entry and enable the "DP slave" check box.
6. Now you have the option of selecting the DP master in the "Assigned DP Master" drop-down list.

   Once you have selected the DP master, the networking and the DP master system between both devices are displayed in the network view.

   ![Procedure for configuring an I-slave](images/72027926667_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for configuring an I-slave](images/72027926667_DV_resource.Stream@PNG-en-US.png)

**Note**

**Operation using a GSD file**

If you operate an I-slave using a GSD file, you should not enable the "Test, commissioning and routing" check box.

Create a DP subnet on the PROFIBUS interface of the I-slave.

### Example: Configuring transfer areas

#### Requirements for configuring transfer areas

- You have configured an I-slave in STEP 7.
- You are in the device view of the I-device and have selected the PROFIBUS interface of the communications module.

#### Procedure for configuring transfer areas

To configure transfer areas for an I-slave, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. In the area navigation, go to the section "Operating mode" &gt; "I-slave communication" &gt; "Transfer areas". 2. Create transfer areas. Set the properties of the created transfer areas.               ![Procedure for configuring transfer areas](images/72031306763_DV_resource.Stream@PNG-en-US.png)         ![Procedure for configuring transfer areas](images/72031306763_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    | ① | Click in the first cell of the "Transfer area" column. STEP 7 assigns a default name that you can change. |    | ② | Select the type of communication relation: Currently, you can only select MS for "master-slave communications relation". |    | ③ | STEP 7 assigns the addresses for the transfer area automatically. Correct the addresses if necessary. |    | ④ | Set the length and unit of the transfer area. Specify the length of the transfer area in the following format: [1...64] bytes/word. Examples: "32 Byte", "64 Word" |    | ⑤ | Specify whether the transfer area is exchanged in units of bytes or words or consistently over the entire length between the DP master and I-slave. | |  |

A separate entry is created in the area navigation for each transfer area. If you select one of these entries, you can adjust the details of the transfer area, or correct them and comment on them.

### Diagnostics and interrupt behavior (S7-1500, ET 200SP CPU)

#### Diagnostics and interrupt behavior

S7 CPUs have numerous diagnostics and interrupt functions that can, for example, report errors/faults or failures of underlying DP systems. These diagnostics alarms reduce downtimes and simplify localization and elimination of problems.

#### Diagnostics options in the higher-level DP master and in the I-slave

The following diagnostics mechanisms are available to the higher-level DP master and the I-slave:

- OB 82 (diagnostics interrupt)

  When the I-slave changes mode, the DP master calls OB 82 (diagnostics interrupt).

  When the DP master changes mode, the I-slave calls OB 82 (diagnostics interrupt).
- OB 86 (rack failure)

  If the bus connection to the I-slave is interrupted, the DP master calls OB 86 (rack failure).

  If the bus connection to the DP master is interrupted, the I-slave calls OB 86 (rack failure).
- OB 122 (I/O access error)

  If you have not set the attribute "Handle errors within block" for OB 122, the following applies:

  - If the bus connection to the I-slave is interrupted, the DP master calls OB 122 (I/O access error) if there is direct access to the relevant transfer areas.
  - If the bus connection to the DP master is interrupted, the I-slave calls OB 122 (I/O access error) if there is direct access to the relevant transfer areas.

#### Reaction of the transfer areas to mode changes

| DP master | I-slave | Reaction of input transfer areas DP master | Reaction of input transfer areas I-slave |
| --- | --- | --- | --- |
| RUN→STOP | RUN | No updating of the process image | The input transfer areas retain their current values. (no access error) |
| STOP→RUN | RUN | The input transfer areas are updated by the cyclic user program via the process image. | The input transfer areas are updated via the process image. |
| RUN | RUN→STOP | The I-slave sets the input transfer areas on the DP master to "0". | No updating of the process image |
| RUN | STOP→RUN | The I-slave sets the input transfer areas on the DP master to "0".  After the startup program of the I-slave, the input transfer areas of the DP master are updated via the process image. | Prior to processing of the startup program, the input transfer areas are updated via the process image. |

## Configuring direct data exchange

This section contains information on the following topics:

- [What you need to know about direct data exchange](#what-you-need-to-know-about-direct-data-exchange)
- [Configuring direct data exchange](#configuring-direct-data-exchange-1)
- [Example of how to configure direct data exchange](#example-of-how-to-configure-direct-data-exchange)

### What you need to know about direct data exchange

#### Introduction

Direct data exchange (data exchange broadcast) is another form of I/O communication, which is not restricted to the context of a DP master system. With direct data exchange, the receiver has read-only access (in other words it cannot write data).

In a DP master system, a DP master only controls the DP slaves that have been assigned to it. With direct data exchange, a DP master or a DP slave configured as a receiver on the PROFIBUS subnet can "listen in" to find out what input data another DP slave is sending to its DP master in a sender capacity. This method of transferring data between DP slaves is referred to as direct data exchange.

#### Principle of operation

In a direct data exchange configuration, local input address areas of an intelligent DP slave or of a DP master are assigned to the input address areas of a PROFIBUS DP partner.

The intelligent DP slave or DP master can then use these input address area assignments to receive data from its PROFIBUS DP partner.

![Principle of operation](images/6111038091_DV_resource.Stream@PNG-en-US.png)

#### Configuration options

Possible applications of direct data exchange include:

- A configuration involving intelligent DP slaves: DP slave &gt; I slave
- A configuration involving two DP master systems: DP slave &gt; DP master

#### Number of PROFIBUS DP partners that can be connected

The total number of PROFIBUS DP partners that can be connected directly to a DP interface or that can be addressed via this interface using direct data exchange depends on the specific interface concerned. A maximum of 32 PROFIBUS DP partners can be addressed on the MPI/DP interface.

---

**See also**

[Configurations involving several DP master systems](#configurations-involving-several-dp-master-systems)
  
[Configurations involving intelligent DP slaves](#configurations-involving-intelligent-dp-slaves)

### Configuring direct data exchange

#### Requirement

- You must be in the network view.
- A DP master system with input modules is available on the DP slave.
- A DP master or DP slave is linked with the DP master system as a "receiver".

#### Setting up direct data exchange

To set up direct data exchange, proceed as follows:

1. Click on the required communications partner (sender or receiver) to select it.
2. Press and hold down the left mouse button and then drag the second communications partner into the "Place device here" field, or select the "Partner 2" column of the I/O communications table.

   ![Setting up direct data exchange](images/69135960075_DV_resource.Stream@PNG-en-US.png)

   ![Setting up direct data exchange](images/69135960075_DV_resource.Stream@PNG-en-US.png)

   Alternatively, click directly on the "Place device here..." and select the connection partner you want from the drop-down list box.

Using drag-and-drop, you have now managed to set up a relationship in the table between two nodes for the purpose of communication. In a new line of the I/O communications table, "Direct data exchange" will now be displayed.

> **Note**
>
> The sender is always selected first in the case of a direct data exchange between two I-slaves. Subsequently, the receiver is dragged to the "Place device here or select" field or select from the drop-down list box. The communication direction of the direct data exchange determines the order in this case.
>
> If you use the drop-down list in the "Partner 2" column of the I/O communication table to create the direct data exchange, you can select the communication direction of the direct data exchange directly by selecting it in the drop-down list.

#### Configuring direct data exchange

To configure direct data exchange, proceed as follows:

1. Select a direct data exchange partner.
2. In the I/O communications table, select the line showing "Direct data exchange" mode.
3. Select "Properties &gt; Direct data exchange" in the Inspector window.
4. Create a new transfer area under "Direct data exchange" in the transfer area table:

   In the "Transfer area" column, click on "&lt;Add new&gt;" and select the "DX" communication type for direct data exchange in the "Type" drop-down list box. You can also create the new transfer area by setting the communication type in a new column only under "Type". The transfer area is then created automatically.
5. Under "Direct data exchange", click on the newly created transfer area.

   The detail view of the transfer area is opened.
6. Edit the properties for the sender and receiver and the general parameters of the direct data exchange.

You have now configured direct data exchange.

#### Deleting direct data exchange

To delete the direct data exchange, proceed as follows:

1. In the I/O communications table, select the line showing "Direct data exchange" mode.
2. Press "Del" or select the "Delete" command from the shortcut menu.

### Example of how to configure direct data exchange

#### Introduction

In this example, you are going to configure three CPUs in a master-slave configuration for direct data exchange. You are then going to assign meaningful names and configure the address areas.

Use the CPUs below, which should be configured as follows:

| CPU | Task | Address | Data |
| --- | --- | --- | --- |
| 317-2 PN/DP | DP master | I 200 | 8 words from sender |
| 315-2 DP | Sender | Q 100 | 8 words to master |
| 317-2 DP | Receiver | I 120 | First 2 bytes of the 8 words from the sender |

#### Requirement

- You must be in the network view.
- The hardware catalog is open.

#### Setting up a PROFIBUS DP master system

To set up a PROFIBUS DP master system, proceed as follows:

1. Drag and drop the following CPUs from the hardware catalog into the network view: 315-2 DP, 317-2 DP and 317-2 PN/DP.
2. Give the CPUs meaningful names:

   - Select the CPU 317-2 PN/DP.
   - Assign the name "DP master" to the CPU under "Properties &gt; General" in the Inspector window.

   Now repeat the naming process for the other CPUs, calling them "Sender" and "Receiver" respectively.
3. Select the CPU 317-2 PN/DP and then, if necessary, change the interface type from "MPI" to "PROFIBUS" under "Properties &gt; MPI/DP interface &gt; MPI address" in the Inspector window.

   Note: If the MPI/DP interface is set to "PROFIBUS" type, the entry is no longer "MPI address" but rather "PROFIBUS address".
4. Select CPUs 315-2 DP and 317-2 DP one after the other and in both cases select "Slave" mode under "Properties &gt; DP interface &gt; Mode" in the Inspector window.

   The two CPUs 315-2 DP "Sender" and 317-2 "Receiver" are now being operated as I-slaves.
5. While holding down the mouse button, draw the PROFIBUS connections between the master CPU and the two slave CPUs.

You have now successfully set up a PROFIBUS master system with the CPU 317-2 PN/DP as DP master and the 315-2 DP "Sender" and 317-2 DP "Receiver" as I-slaves. New lines for the communications partners will have been created in the I/O communications table relating to the CPUs. "I-slave" will be displayed in the "Mode" column.

#### Setting up direct data exchange

To set up direct data exchange within the PROFIBUS master system, proceed as follows:

1. Select the "Sender".
2. Press and hold down the left mouse button and then drag the "Receiver" to the "Place device here" field, which appears in the "Partner 2" column of the I/O communications table.

   Note: You can also open the drop-down list box in the "Place device here" field of the "Partner 2" column, and select the "Receiver" from this list.

You have now successfully set up a direct data exchange between the two I-slaves. A new line will have been created in the I/O communications table relating to the two I-slaves. "Direct data exchange" will be displayed in the "Mode" column.

> **Note**
>
> The arrow symbols in the I/O communication table between the "Peer 1" and "Peer 2" columns indicate the directions of the communication relations. The arrows point in both directions for master-slave and slave-I-slave relations. The arrows point from the sender to the receiver in the case of communication relations between I-slaves or during direct data exchange.

#### Configuring master-slave communication

To select master-slave communication, proceed as follows:

1. Select one of the two communication partners of master-slave communication (DP master CPU 317-2 PN/DP or I-slave CPU 315-2 DP "sender")
2. In the I/O communications table, click on the line with the respective second partner and "I-slave" mode.
3. Select "Properties &gt; I-slave communication" in the Inspector window.

Or:

1. Select the CPU 315-2 DP "sender" I-slave.
2. Select "Properties &gt; DP interface &gt; Mode &gt; I-slave communication" in the Inspector window.

To configure master-slave communication, proceed as follows:

1. Create a new transfer area under "I-slave communication" in the transfer area table:  
   In the "Transfer area" column, click on "&lt;Add new&gt;" and select the "MS" communication type for master-slave communication in the "Type" drop-down list box. You can also create the new transfer area by setting the communication type in a new column only under "Type". The transfer area is then created automatically.
2. Under "I-slave communication", click on the newly created transfer area.

   The detail view of the transfer area is opened.
3. Make the following entries:

   for "DP master":

   - Address type I
   - Start address 200
   - Length 8
   - Unit WORD
   - Consistency total length

   for "Sender":

   - Address type Q
   - Start address 100

Once the data length has been specified, the slave and master addresses for the required data space are completed. If you click on "I-slave communication" in the Inspector window, you will see an overview of the updated configuration of master-slave communication.

#### Configuring direct data exchange

To configure direct data exchange, proceed as follows:

1. Select one of the two communication partners of direct data exchange (I-slave CPU 315-2 DP "Sender" or I-slave CPU 317-2 DP "Receiver")
2. In the I/O communications table, click on the line showing "Direct data exchange" mode.
3. Select "Properties &gt; Direct data exchange" in the Inspector window.

To configure direct data exchange, proceed as follows:

1. Create a new transfer area under "Direct data exchange" in the transfer area table:  
   In the "Transfer area" column, click on "&lt;Add new&gt;" and select the "DX" communication type for direct data exchange in the "Type" drop-down list box. You can also create the new transfer area by setting the communication type in a new column only under "Type". The transfer area is then created automatically.
2. Under "Direct data exchange", click on the newly created transfer area.

   The detail view of the transfer area is opened.
3. Make the following entries:

   for "Sender":

   - Address 100
   - Data length 1
   - Unit WORD

   for "Receiver":

   - Address 120

> **Note**
>
> If the sender in the direct data exchange is a normal DP slave, no transfer areas will be configured. Instead, an input module has to be added to the sender.

#### Particularity

In theory, you can also set an start address higher than 200 (202, for example). The length of consistent data will be adapted automatically. Furthermore, you can set a shorter length than that specified by the sender (1 byte, for example).

> **Note**
>
> If a consistent length of 3 bytes or more than 4 bytes is set for the sender and the data is to be transferred with the extended instruction of system function "DPWR_DAT" (SFC 15), the receiver will always need to use extended instruction "DPRD_DAT" (SFC 14) even if only 1 byte is actually being read, for example!
>
> If you are using a loading operation (L IB..) instead of the DPRD_DAT to read 1 byte, a "0" is read in (incorrect value).

#### DPWR_DAT call on sender (CPU 315-2 DP)

STL

CALL "DPWR_DAT"

LADDR :=W#16#64 //Start address Q 100

RECORD :=P#M 10.0 BYTE 16 //User data source area

RET_VAL:=MW100 //Return value

#### DPRD_DAT call on receiver (CPU 317-2 DP)

STL

CALL "DPRD_DAT"

LADDR :=W#16#78 //Start address I 120

RET_VAL:=MW100 //Return value

RECORD :=P#M 10.0 BYTE 2 //User data target area

## Using GSD files

This section contains information on the following topics:

- [GSD revisions](#gsd-revisions)
- [Installing the GSD file](#installing-the-gsd-file)
- [Deleting GSD file](#deleting-gsd-file)
- [Finding unused GSD files](#finding-unused-gsd-files)
- [Configuring GSD-based DP slave](#configuring-gsd-based-dp-slave)

### GSD revisions

#### What you need to know about GSD revisions

The properties of DP slaves are made available to configuration tools by means of GSD files. Functional enhancements in the area of the distributed I/O will have an effect on the GSD specification, for example, they will require the definition of new keywords. This results in the versioning of the specification. In the case of GSD files, the version of the specification on which a GSD file is based is called a "GSD revision". From GSD revision 1, the GSD revision must be included as a keyword "GSD_revision" in GSD files. GSD files without this keyword will therefore be interpreted by configuration tools as GSD revision "0".

GSD files can be interpreted up to GSD revision 5. This means that DP slaves that support the following functions, for example, will be supported:

- Diagnostic alarms for interrupt blocks
- Isochronous mode and constant bus cycle time
- SYNC/FREEZE
- Clock synchronization for DP slaves

### Installing the GSD file

#### Introduction

A GSD file (generic station description file) contains all the DP slave properties. If you want to configure a DP slave that does not appear in the hardware catalog, you must install the GSD file provided by the manufacturer. DP slaves installed via GSD files are displayed in the hardware catalog and can then be selected and configured.

You can also install components for PROFIBUS PA using GSD files.

#### Requirement

- The hardware and network editor is closed.
- You have access to the required GSD files in a directory on the hard disk.

#### Procedure

To install a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD files are stored.
3. Choose one or more files from the list of displayed GSD files.
4. Click on the "Install" button. The selected GSD files are now being installed.
5. To create a log file for the installation, click on the "Save log file" button.

   Any problems during the installation can be tracked down using the log file.
6. Click "Close". You are notified that the DP slaves or potential equalization components from the installed GSD files are entered into the hardware catalog. This process can take a few seconds.

By installing a GSD file, you have added the DP slave or the potential equalization components described in the file to the hardware catalog.

#### Result

You will find the new DP slaves installed by means of GSD files in the hardware catalog under "Additional field devices &gt; PROFIBUS DP". New potential equalization components installed via GSD files can be found there under "Other field devices &gt; PROFIBUS PA".

GSD files are always saved together with the project, which means all information relevant for display of the device (including symbols) is also available in the saved project.

---

**See also**

[Overview of hardware and network editor](Configuring%20devices%20and%20networks.md#overview-of-hardware-and-network-editor)

### Deleting GSD file

#### Introduction

You can delete installed DP slaves using GSD files. These DP slaves are then no longer displayed in the hardware catalog.

#### Requirement

- The hardware and network editor is closed.
- The hardware catalog contains DP slaves installed using GSD files.

#### Procedure

To delete a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD file is stored.
3. Select the file that is to be deleted from the list of displayed GSD files.
4. Click the "Delete" button.

The selected GSD file was deleted and the DP slave is no longer located in the hardware catalog.

### Finding unused GSD files

#### Introduction

When you add a GSD-based hardware component to your hardware configuration, different GSD files are added to the project data. If the GSD-based hardware component is once again deleted from the configuration, the GSD files remain in the data inventory of the project. The GSD files are no longer needed in the project if the corresponding GSD-based hardware component is not used in the hardware configuration again. You can find files that are no longer needed in the project with a search function and delete them.

#### Requirement

- A project must be open.
- The project must not be online.
- The project must not be write-protected.

#### Procedure

To find and delete unused GSD files, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. Click on the "Find unused GSDs" button in the "GSDs in the project" tab.
3. If GSD files that are no longer needed were found in the project data, you can now delete them. To do so, click the "Delete" button.

**Note**

Unused GSD files are only available if at least one GSD-based hardware component was added to the configuration and then removed from the configuration. Unused GSD files in the project libraries are included in the search. GSD-based hardware components that are still being used in the configuration are not considered to be unused.

Installed GSD-based hardware components that are included in the hardware catalog but have not been used in the hardware configuration of the project yet, could not have stored unused GSD data in the project.

GSD files that are no longer needed are deleted from the project data. The GSD-based hardware component is still available in the hardware catalog and, if necessary, can be added to the configuration once again. The necessary GSD data are once again copied to the project data in this case.

> **Note**
>
> If you delete a GSD-based hardware component with "Options &gt; Manage general station description files (GSD) &gt; Installed GSDs", it is deleted from the hardware catalog. However, unused GSD files of this hardware component can still be a part of the project data and can be deleted with the function for finding the unused GSD files.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Actions that cannot be undone**  When you delete GSD files that are not being used as an action, the action stack for actions that can be undone is deleted. This means the action of deleting unused GSD files as well as all previous actions can no longer be undone. |  |

---

**See also**

[Basics of undoing and redoing actions](Introduction%20to%20the%20TIA%20Portal.md#basics-of-undoing-and-redoing-actions)

### Configuring GSD-based DP slave

DP slaves that you have inserted through installation of a GSD file can be selected as usual via the hardware catalog and inserted in the network view. If you want to insert the modules of the GSD-based DP slaves, you must take into account some particular details.

#### Requirement

- You have installed a DP slave using a GSD file.
- You have inserted the head module in the network view in the usual manner.
- The device overview opens in the device view.
- The hardware catalog is open.

#### Procedure

To add the modules of a GSD-based DP slave, proceed as follows:

1. In the hardware catalog, navigate to the modules of the GSD-based DP slave.

   GSD-based DP slaves, also referred to as DP standard slaves, can be found in the "Other field devices" folder of the hardware catalog.
2. Select the desired module.
3. Use drag-and-drop to move the module to a free space in the device overview.
4. Select the module in the device overview to edit parameters.

You have now inserted the module in a free slot of the GSD-based DP slave and can edit its parameters.

> **Note**
>
> You can see only the GSD-based DP slave in the graphic area of the device view. The added modules of GSD-based DP slaves are only found in the device overview.

#### Preset configuration

For modules with an adjustable preset configuration, you can change this configuration in the inspector window under "Properties &gt; Preset configuration".

---

**See also**

[Device view: Objects in the device view](Configuring%20devices%20and%20networks.md#device-view-objects-in-the-device-view)
  
[Rack: Inserting a module](Configuring%20devices%20and%20networks.md#rack-inserting-a-module)
  
[Adding a device to the hardware configuration](Configuring%20devices%20and%20networks.md#adding-a-device-to-the-hardware-configuration)

## Using PROFIBUS DPV1

This section contains information on the following topics:

- [Introduction to PROFIBUS DPV1](#introduction-to-profibus-dpv1)
- [Configuring DPV1 devices](#configuring-dpv1-devices)
- [Programming DPV1 devices](#programming-dpv1-devices)
- [Example for analyzing interrupt information](#example-for-analyzing-interrupt-information)
- [Example for analyzing diagnostic data](#example-for-analyzing-diagnostic-data)
- [Slot model of the DPV1 slaves for I slaves](#slot-model-of-the-dpv1-slaves-for-i-slaves)

### Introduction to PROFIBUS DPV1

#### General

The DPV1 functionality is an extension of the PROFIBUS standard for distributed I/O. Relative to the functionality in the DPV0 predecessor, the DPV1 functionality has several extensions and simplifications:

- PROFIBUS DPV0 handles the cyclic exchange of data and the diagnostics.
- PROFIBUS DPV1 handles acyclic and cyclic data exchange plus interrupt handling.

#### Additional functionality for DPV1 devices (DP masters/DP slaves)

DP masters and DP slaves that support DPV1 have the following additional functions compared to devices that only support DPV0:

- The acyclic data exchange between master and slave is supported (read/write data record, e.g. to reassign parameters to a slave in operation). The data records of a module and the structure of these data records is provided in the documentation of the respective module.
- Interrupts can be set by a DPV1 slave that ensure handling of the interrupt triggering event in the master CPU. Even in "STOP" mode the interrupt data will be analyzed in the CPU (update of the diagnostic buffer and module status). However, OB processing does not take place in STOP.  
  In addition to the interrupts that are known from SIMATIC, such as diagnostic interrupt for ET 200M, now the interrupt, status interrupt, update interrupt and vendor-specific interrupt are also supported.

---

**See also**

[S7 integration of DPV1 slaves](http://support.automation.siemens.com/WW/view/en/10259221)

### Configuring DPV1 devices

Some devices, such as the DP interface IM 151-1 HF, can toggle between DPV0 and DPV1.

#### Requirement

- You must be in network view.
- A DP master with DPV1 functionality must be available.
- A master-slave connection must be established with PROFIBUS.

#### Procedure

To switch the DP slave mode from DPV1 to DPV0 functionality, proceed as follows:

1. Select the DP slave.
2. Under "Properties &gt; General &gt; Module parameters" in the Inspector window, select "DPV0" or "DPV1" mode from the "DP interrupt mode" drop-down list.

or

1. Select the DP master.
2. In the I/O communications table, select the row with the connection between the DP master and the desired DP slave.
3. Under "Properties &gt; General &gt; Module parameters" in the Inspector window, select "DPV0" or "DPV1" mode from the "DP interrupt mode" drop-down list.

#### Using devices with different PROFIBUS functionality

The following rules apply to the mixed use of devices with DPV0 and DPV1 functionality:

- In principle, DPV0 slaves can also be operated on a DP interface with DPV1 functionality.
- In principle, DPV1 slaves can also be operated on a DP interface with DPV0 functionality. In this case, DPV1 functionality will be switched off. However, vendor-specific configuration rules for certain DP slaves can force DPV1 operation, so that these DP slaves cannot operate with the DP master system.

#### Assigning the diagnostics address

In the case of DPV1 slaves, the diagnostics address is automatically assigned to the virtual slot 0 as station proxy.

The following assignment basically applies:

- Diagnostics and interrupts that only refer to the entire DP slave are assigned to the virtual slot 0 and its diagnostics address: For example interrupts for modules in non-configured slots, station failure/station recovery ([OB86](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#rack-failure-organization-block-ob-86-s7-300-s7-400)).
- Diagnostics and interrupts that originate from this module (for example, from a DP connection IM 153-2 in slot 2) are assigned to the remaining slots with their respective start addresses.

---

**See also**

[Interrupts on the I-slave](#interrupts-on-the-i-slave)

### Programming DPV1 devices

For DPV1 functionality, there are OBs and SFBs/SFCs that cannot be used for DPV0.

#### Interrupt OBs for DPV1 events

DPV1 slaves can trigger interrupts. For diagnostics interrupts, hardware interrupts and remove/insert interrupts, you can use the appropriate OBs made available by the operating system of the S7-CPUs.

The interrupt OBs for DPV1 are presented in the table below. Detailed information is provided in the description of the OBs.

| DPV1 interrupt | OB | Explanation |
| --- | --- | --- |
| Status interrupt | [OB55](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#status-interrupt-ob-ob-55-s7-300-s7-400) | The status interrupt can be triggered if the operating state of a device or a module changes, for example, from RUN to STOP.  A precise description of the events for which a status interrupt is triggered is provided in the documentation provided by the manufacturer of the respective DPV1 slave. |
| Update interrupt | [OB56](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#update-interrupt-ob-ob-56-s7-300-s7-400) | An update interrupt can be triggered when new parameters are assigned to a slot. This may have been caused, for example, by local access or partner access to the parameters.  A precise description of the events for which an update interrupt is triggered is provided in the documentation provided by the manufacturer of the respective DPV1 slave. |
| Vendor-specific interrupt | [OB57](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#ob-for-manufacturer-specific-alarms-ob-57-s7-300-s7-400) | The event that triggers the vendor-specific interrupt can be specified by the manufacturer of a DPV1 slave. |

#### Instructions for access to DPV1 slaves

The DPV1 interfaces with their functions are presented in the table below. Detailed information is provided in the description of the extended instructions.

| Function | Interface (DPV1) | Comments |
| --- | --- | --- |
| Read data record | [RDREC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdrec-read-data-record-s7-300-s7-400) | - |
| Write data record | [WRREC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wrrec-write-data-record-s7-300-s7-400) | - |
| Receive interrupt from a DP slave | [RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400) | The instruction must be called in the OB that triggers the interrupt. |

> **Note**
>
> If a DPV1 slave is used and the DP interface of the DP master is set to "DPV0", no data records may be read from or written to the I/O modules using "WR_REC"/"RD_REC" or "WRREC"/"RDREC" instructions in the user program. In this case the DP master addresses the wrong slot (configured slot+3).
>
> Solution: Change the interface of the DP master to "DPV1".

#### Check list for changing from DPV0 to DPV1

The following sections of the existing user program must be observed when you have edited the configuration and changed the interface from "DPV0" to "DPV1".

| Function | What do I need to observe? |
| --- | --- |
| Address conversions | If you have used address conversions in the user program, for example, with extended instructions of system functions "[GADR_LGC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#gadr_lgc-query-logical-start-address-of-a-module-s7-300-s7-400)" (SFC 5), "[LGC_GADR](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#lgc_gadr-determine-the-slot-belonging-to-a-logical-address-s7-300-s7-400)" (SFC 49), "[RD_LGADR](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_lgadr-determine-all-logical-addresses-of-a-module-s7-300-s7-400)" (SFC 50), you must check the slot &lt;-&gt; logical start address assignment for the DPV1 slaves. In addition, slot 0 has an address.  DPV1 slave:  Whereas previously the first I/O module of the DP slave was assigned to slot 4 by the extended instructions, now the first I/O module is assigned to slot 1 (as shown in the hardware configuration).  DPV1 slave integrated in the hardware catalog (for example, ET 200M):  Interface module (slot 2) has its own address. |
| Reading diagnostics information using the system function "[DPNRM_DG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)" | The originally assigned diagnostics address will also continue to function. Internally this address is assigned to slot 0.  The diagnostic data record of the DPV1 slave is structured differently than it is with DPV0 (see description of the DP slave for ET 200M, for example, also under the keyword "Extended diagnostics"). |
| Reading/writing data records | If you transfer data records to a DPV1 slave using extended instruction "[WR_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400)" (SFC 58) or read data records from a DPV1 slave using extended instruction "[RD_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)" (SFC 59) and this slave is working in DPV1 mode, the DP master analyzes the error information received from the slave as follows: If the error information is in the areas W#16#8000 to W#16#80FF or W#16#F000 to W#16#FFFF, the DP master will forward the error information to the SFC. If it is outside of these areas it gives the value W#16#80A2 to the SFC and suspends the slave.  For the description of the error information originating from the DPV1 slave, see the description of the "RALRM" (SFB 54) instruction.  Additional information is available in the descriptions on jumps in language descriptions, module help and system attributes. |
| Reading out system status lists | If you use the extended instruction "[RDSYSST](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdsysst-read-system-status-list-s7-300-s7-400)", for example to read module status information or rack/station status information, you must also take the changed meaning of the slots and the additional slot 0 (see above) into consideration. |

### Example for analyzing interrupt information

#### Introduction

A distributed S7 digital input module (start address 288) triggers a hardware interrupt. In [OB40](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#hardware-interrupt-organization-blocks-ob-40-to-ob-47-s7-300-s7-400), the additional interrupt information of this module can be read using the advanced instruction "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)". The system checks whether the first channel has triggered a hardware interrupt.

In the case of S7 modules, additional interrupt information could also be directly read from the start information of the OB40. However, the DPV1 functionality allows up to 59 bytes of additional interrupt information, which is far too much for the start information of the OB40.

#### Analyzing interrupt information from OB40 with "RALRM"

STL

// ...

// ...

//Switch for interrupt triggering address (288)

L DW#16#120

T "MD10"

CALL "RALRM" , "DB54"

MODE :=1 //Function mode: 1=set all output parameters (i.e. F_ID has no effect)

F_ID :="MD10" //Start address of the slot from which an interrupt is permitted

MLEN :=8 //Max. length of the additional interrupt info in bytes (for example, for channel status of the module)

NEW :="Alarm_neu" //Interrupt received? (Yes = 1)

STATUS:="DP_RALRM_STATUS" //Return value with function result/error message

ID :="Slotaddress_Interrupt" //Start address of the slot from which an interrupt was received

LEN :="Length_Alarminfo" //Length of the additional interrupt info (4-byte header info + for example, 4 bytes for S7 I/O modules)

TINFO :=P#M 100.0 BYTE 28 //Pointer for OB start info +management info: 28 bytes from MB 100

AINFO :=P#M 130.0 BYTE 8 //Pointer for target area of the header info + supplemental interrupt info (max. 59 bytes)

A M 124.0 //Is input 1 (bit 0) the interrupt triggerer?

JC Alrm

BEU

Alrm: S Q 0.0 // interrupt processing

// ...

### Example for analyzing diagnostic data

#### Introduction

The target area for diagnostic data should suffice for standard diagnostics (6 bytes), for identifier-specific diagnostics (3 bytes for 12 slots) and for analyzing the device-specific diagnostics (module status only, which is an additional 7 bytes). Extended instruction "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" in [OB82](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#diagnostic-interrupt-ob-ob-82-s7-300-s7-400) is used for this.

For more extensive analysis (channel-specific diagnostics), additional bytes would be reserved if the DP slave supports this function.

#### Analyzing diagnostic data in OB82 with "RALRM" (SFB 54)

STL

// ...

// ...

L 120 //Specify start address for device/module,

T "Slotadress_Diag" //from which diagnostics must be fetched

CALL "RALRM" , "DB54"

MODE :="Alle_Params" // 1 = All output parameters are set

F_ID :="Slotadresse_Diag" //Start address of the slot from which the diagnostics will be fetched

MLEN :=20 //Max. length of the diagnostic data in bytes

NEW :="new" //irrelevant

STATUS:="RET_VAL" //Function result, error message

ID :="Slotadresse_Alarm" //Start address of the slot from which an interrupt was received

LEN :="Laenge_Alarminfo" //Length of additional interrupt info (4-byte header info +16 bytes diagnostic data)

TINFO :=P#M 100.0 BYTE 28 //Pointer for OB start info +management info: 28 bytes from MB 100

AINFO :=P#M 130.0 BYTE 20 //Pointer on target area in which the diagnostic data will be stored

// ...

//Structure of the stored diagnostic data:

// MB 130 to MB 133: Header info (length, identifier, slot)

// MB 134 to MB 139: Standard diagnostics (6 bytes)

// MB 140 to MB 142: Identifier-specific diagnostics (3 bytes)

// MB 143 to MB 149: Module status (7 bytes)

// ...

A M 141.0 //Slot 1 with error?

JC stp1

BE

stp1: L MB 147 //Module status slot fetch 1 to 4

AW W#16#3 //Filter out slot 1

L W#16#2 //2-bit status "wrong module" inserted

==I

S Q 0.1 //Response to wrong module

L MB 147 //Module status slot fetch 1 to 4

AW W#16#3 //Filter out slot 1

L W#16#1 //2-bit status "invalid data"

==I

S Q 0.2 //Response to invalid user data

// ...

### Slot model of the DPV1 slaves for I slaves

#### Introduction

This section describes how to make the assignments of I/O addresses and diagnostics addresses to the slots visible for DPV1. In particular, it deals with addresses that do not transport user data and their configuration.

#### The slot model for DPV1

With DPV1, a DP slave is formed by slots in precisely the same manner as DPV0. The numbers of the slots are 0, 1, ...n. Slot 0 applies only for DPV1 and has prominent significance because it is the proxy of the entire DP slave.

For example, proxy means that interrupts that have been triggered from slot 0 originate from the entire DP slave and not from a specific slot within the DP slave. Diagnostics that come from this slot are assigned to the entire DP slave and not to a specific slot or individual module.

#### Addresses for DP interfaces

From the CPU perspective, there is a separate logical address for each of its interfaces. The address for the respective DP interface is displayed in various ways:

- When you select a device or a DP interface in the Inspector window under "Properties &gt; PROFIBUS address (Xn)" or "Properties &gt; MPI/DP interface &gt; PROFIBUS address (Xn)".
- With an enabled "Display addresses" in the toolbar in the network view: You will then see the name of any connected subnets for each interface, followed by the assigned PROFIBUS address.

These addresses have nothing to do with the slot model of DP slaves; they serve merely as internal CPU identification, for example, in the event of a failure of the interface. This address is of minor significance for the user program.

#### Slots and addresses for user data

Every manufacturer of a DP slave can freely determine which data will come from which slot.

As opposed to DPV1 slaves with user data starting with slot 1, DPV0 slaves are subject to a restriction in that the first I/O module must always be located in slot 4. DP slaves that are installed via a GSD file, can have user data starting with slot 1. Because distributed I/O data is usually accessed via its addresses, in the same way as central I/O data, user data of the DPV0 slaves must be addressed from the start address of slot 4. This also applies to intelligent DP slaves.

In the case of intelligent DP slaves, you can allocate I/O memory areas of the I-slaves to I/O memory areas of the DP master by means of the "I-slave communication" transfer areas. During operation (cyclic data exchange), the data that you transfer into the I/O memory areas in the user program of the intelligent DP slave are transferred via the transfer area into the I/O memory area of the DP master. You will find the table for the assignment of the I/O memory areas to the transfer areas by selecting the I-slave connection in the I/O communications table under "Properties &gt; I-slave communication" in the Inspector window. After creating a transfer area, you can carry out the rest of the configuration under "Details of the transfer area".

When configuring the addresses under "Details of the transfer area", slot numbers are also displayed. The slots are not generated by real modules, as is the case with ET 200M, for example, but rather by freely definable lengths of the respective I/O areas. In this case they are also referred to as virtual slots.

The following points are important for an understanding of the address assignments:

- In addition to its real slots, the intelligent DP slave has virtual slots that are located in the I/O memory area.
- Like the real slots, the virtual slots are accessed via logical addresses. In the case of a DP slave, such as ET 200M, the virtual slots are accessed via the start address of a module; in the case of I-slaves via the configured address of the "I-slave communication".
- The addresses of the virtual slots are different from the perspective of the DP master and that of the DP slave. The assignment can be configured. Thus, the same DP slave will usually be accessed by the DP master under a different address from the one with which it is addressed by the DP slave.

#### Example of an address assignment for user data

The following table shows the assignment of the virtual slots in the transfer area:

| Sample address from the perspective of the DP slave | Significance for the DP slave | Slot | Significance for the DP master | Sample address from the perspective of the DP master |
| --- | --- | --- | --- | --- |
|  |  | 0 |  |  |
|  |  | 1 |  |  |
|  |  | 2 |  |  |
|  |  | 3 |  |  |
| I 2 | Via input byte 2, you can read ... | 4 | ... what the master has written in output byte 4. | Q 4 |
| Q 5 | what was written to output byte 5 in the slave... | 5 | ... can be read in the master as input byte 6 | I 6 |
| I 8 | ... | 6 | ... | Q 8 |
|  |  | ... |  |  |
|  |  | 35 |  |  |

> **Note**
>
> In the network view, you will find slot assignment for the selected I-slave connection in the I/O communications table under "I-slave communication &gt; Transfer areas" in the Inspector window.

#### Addresses for system information

Addresses for system information are used to handle diagnostics information, for example, or information about operating state transitions.

#### Addresses of the DP slave

The system information of a DP slave is assigned to modifiable addresses. In this context, the following addresses are relevant for DPV1:

- Addresses for device diagnostics:

  - The DP master diagnoses a failure or recovery of the I-slave.
  - The I-slave diagnoses a failure or recovery of the DP master.
- Addresses for operating state transitions:

  - The DP master can determine a change in operating state of the DP slave.
  - The intelligent DP slave can determine a change in operating state of the DP master.

The addresses are automatically assigned from top to bottom so that a conflict with user data does not arise. The recommended addresses should be accepted even if they can be changed. If the user program is to run on different CPUs, check whether the addresses are also in the address area of the "smallest" CPU.

The following table shows the assignment of the addresses in I-slave communication:

| Sample address from the perspective of the DP slave | Significance for the DP slave | Sample address from the perspective of the DP master | Significance for the DP master |
| --- | --- | --- | --- |
| 8189 | Station failure/station recovery of the DP master | 16381 | Station failure/station recovery of the DP slave |
| 8188 | Operating state  transition of the DP master | 16380 | Operating state  transition of the DP slave |

#### Summary

With virtual slots in the transfer area, the I-slave configuration looks like this:

![Summary](images/26501749387_DV_resource.Stream@PNG-en-US.png)

#### Triggering a hardware interrupt with the DP_PRAL instruction

Using the system instruction in the extended instruction "[DP_PRAL](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dp_pral-trigger-hardware-interrupt-from-dp-standard-slave-s7-300-s7-400)", you can trigger a hardware interrupt for each configured address from the user program of the I-slave CPU. This applies both to user data addresses from the I/O area and to the address of virtual slot 2.

In the user program of the I-slave, for example, use the I/O addresses configured in the "Local..." column for instruction "DP_PRAL".

A hardware interrupt will then be triggered in the user program of the master. In the start information of the hardware interrupt OB (for example, [OB40](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#hardware-interrupt-organization-blocks-ob-40-to-ob-47-s7-300-s7-400)), the address that you have configured in the "PROFIBUS DP partner" column will also be provided as the interrupt triggering address.

## Constant and isochronous modes

This section contains information on the following topics:

- [Information about constant bus cycle time and isochronous modes](#information-about-constant-bus-cycle-time-and-isochronous-modes)
- [Configuring and assigning parameters to isochronous mode](#configuring-and-assigning-parameters-to-isochronous-mode)
- [Ti/To overlap](#tito-overlap)

### Information about constant bus cycle time and isochronous modes

This section contains information on the following topics:

- [Same length bus cycles for PROFIBUS subnets](#same-length-bus-cycles-for-profibus-subnets)
- [Synchronized execution cycles](#synchronized-execution-cycles)
- [Example for isochronous capture of multiple measuring points](#example-for-isochronous-capture-of-multiple-measuring-points)
- [Rules, requirements, and supplemental conditions](#rules-requirements-and-supplemental-conditions)

#### Same length bus cycles for PROFIBUS subnets

##### Introduction

The PROFIBUS properties "Isochronous mode" and "Constant bus cycle time" are the basis for synchronized processing cycles.

Constant bus cycle time ensures a precise same length time span for bus cycles. "Same length bus cycles" mean that the PROFIBUS-DP master always starts the DP bus cycle after the same time span. Thus the connected slaves also get their data from the master in time intervals that stay precisely the same. This is also referred to as a "Clocking of the bus cycle".

Constant bus cycle time is the prerequisite for isochronous mode.

![Introduction](images/9720195339_DV_resource.Stream@PNG-en-US.png)

##### Composition of bus cycle time

The following figure shows how time is composed for a bus cycle.

![Composition of bus cycle time](images/9782902923_DV_resource.Stream@PNG-en-US.png)

The "variable pause" shown in the figure is always minimal, if communication jobs are still pending, e.g. for additional active stations. The master, or to more precise the constant bus cycle time master, controls the communication proportions in such a manner that the same duration for a bus cycle is always achieved.

##### Requirements

Constant bus cycle times have the following requirements:

- The DP master must support the "Constant bus cycle time" function.
- The constant bus cycle time master must be a class 1 DP master. A programming device/PC is not suitable as a constant bus cycle time master.
- The constant bus cycle time master must be the only active station on the PROFIBUS DP. Only one DP master system should be present on the PROFIBUS subnet. Programming devices or PCs may be connected in addition.
- No SYNC/FREEZE groups should be configured.
- Constant bus cycle time is only possible for the "DP" and "user-defined" bus profiles.
- Do not configure CiR (Configuration in Run).
- A H-CPU cannot be connected on the PROFIBUS subnet.

##### Time for constant bus cycle time DP cycle

The time for the constant bus cycle time for DP cycle is calculated automatically:

- From the PROFIBUS configuration (number of configured stations).
- From additional information for the calculation that is optionally entered: For example programming devices that must be taken into consideration, but that are outside of the project.

The calculated time for the constant bus cycle time for DP cycle takes the user data traffic of the PROFIBUS DP master into account. If errors occur then constant bus cycle time violations can occur.

You can change the calculated time within the displayed interval.

##### Influence of connected active stations (programming devices/PCs and I slaves)

A programming device/PC must only be taken into consideration if it is directly connected on the PROFIBUS with its PROFIBUS interface. If the programming device is connected via the MPI interface of the CPU, then it does not need to be taken into account as is shown in the figure below.

![Influence of connected active stations (programming devices/PCs and I slaves)](images/5640022923_DV_resource.Stream@PNG-en-US.png)

If intelligent DP slaves, e.g. CPU 315-2 DP, are connected then the time for constant bus cycle time for DP cycle must be more generously measured.

---

**See also**

Synchronous cycle interrupt OBs (OB 61 to OB 64)

#### Synchronized execution cycles

##### PROFIBUS supports isochronous mode

Isochronous PROFIBUS is the essential basis for synchronized process cycles. The PROFIBUS system provides a reliable basic clock. The "isochronous mode" system property couples an automation solution with the constant bus cycle time PROFIBUS.

That is:

- Input data is read in synchronism with the DP cycle; all input data is read simultaneously.
- The user program which processes the I/O data is synchronized with the DP cycle by means of isochronous mode interrupt OBs OB 61 to OB 64.
- Data output is synchronized with the DP cycle; all output data take effect simultaneously.
- All input and output data is transferred consistently. That is, all data of the process image are associated logically and based on the same timing.

##### Synchronization of the single cycles

The following figure shows the bandwidth of possible response times for a processing cycle from a series of isochronous single cycles that occur due to synchronization of the input data read-in.

![Synchronization of the single cycles](images/6074297739_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| TDP | System cycle |
| Ti | Time of data input |
| To | Time of data output |

Synchronization of single cycles makes it possible to read input data within cycle "n-1", to process and transfer the data within cycle "n", and to transfer the calculated output data to the "terminals" at the start of cycle "n+1". Resultant process reaction time: from "Ti + TDP + To" to "Ti + (2 x TDP) + To".

The "isochronous mode" system property enables constant cycle times within the SIMATIC system; the SIMATIC system is strictly deterministic on the bus system.

##### Just in time

The fast and reliable response time of a system operating in isochronous mode is based on the fact that all data is provided just-in-time. The constant bus cycle time (isochronous) DP cycle specifies the cycle for this.

![Just in time](images/6074196619_DV_resource.Stream@PNG-en-US.png)

##### Bias time Ti

The start of the I/O read cycle is advanced by the amount of a bias time Ti in order to make all input data available for transfer on the DP subnet at the start of the next DP cycle. The bias time Ti is configured by the user or it is specified automatically.

![Bias time Ti](images/6074285707_DV_resource.Stream@PNG-en-US.png)

##### Processing the input data

PROFIBUS transfers the input data to the DP master via the DP subnet. The isochronous mode interrupt OB (OB 61, OB 62, OB 63 or OB 64) is called. The user program in the isochronous mode interrupt OB determines the process reaction and provides the output data in time for the start of the next DP cycle. You can have the length of the DP cycle calculated automatically or you can configure it yourself.

##### Making the output data available

The following applies for the output data:

- It will be made available promptly at the start of the next DP cycle.
- Is transmitted via the DP subnet to the DP slaves.
- It is isochronously, i.e. simultaneously forwarded to the process at the time To.

The result is a total reproducible reaction time of "Ti + (2 x TDP) + To" for the transfer from the input to the output terminal.

##### Characteristics of isochronous mode

Isochronous mode is based on three essential characteristics:

- The user program is synchronized with I/O processing, i.e. all operations are coordinated on a time basis. All input data is logged at a defined time. The output data also take effect at a defined time. The I/O data is synchronized with the system cycle up to the terminals.   
  The data of one cycle are always processed within the next cycle, and take effect at the terminals within the subsequent cycle.
- I/O data is processed in isochronous mode, that is, input data is always read at constant intervals, and are always output at constant intervals.
- All I/O data is transferred consistently, that is, all data of a process image is associated logically and based on the same timing.

#### Example for isochronous capture of multiple measuring points

##### Introduction

With the "Isochronous mode" system property, measured values and process data can be captured in a fixed system clock. The signal processing until switching on the output terminal occurs in the same system clock. Isochronous mode thus contributes to high quality of the controller and thus to greater manufacturing precision. With isochronous mode the possible fluctuations of process response times are drastically reduced. Time-assured processing can be used for a higher machine clock/cycle.

Basically isochronous mode is an advantage wherever measured values must be captured synchronously, movements coordinated, and process responses must be defined and simultaneously executed as in the following example.

##### Task

QC requires precise measurement of dimensions within a camshaft production process.

![Task](images/6088023691_DV_resource.Stream@PNG-en-US.png)

##### Conventional workflow

1. Machining of the cam shaft on the lathe
2. Stop
3. Measurement of the angular position
4. Measurement of all cam gradients
5. Continue machining, stop, measurement...

##### Isochronous mode workflow

Implementation of the "isochronous mode" system property and the resultant synchronization of measured value acquisition forms the basis of continuous and accelerated measuring processes. Resultant workflow:

1. Continuous machining of the camshaft
2. Synchronous measurement of the camshaft positions and gradients within a continuous rotation.
3. Machining of the next camshaft

All camshaft positions and the corresponding measured values (red in the figure) are measured synchronously within a single rotation of the camshaft. This increases machine output and maintains or enhances precision of the measurement.

#### Rules, requirements, and supplemental conditions

##### What you need to be aware of for configuring isochronous mode is

- Isochronous mode cannot be used on optical PROFIBUS networks.
- Constant bus cycle time and isochronous mode are only possible for the "DP" and "user-defined" bus profiles.
- Isochronous mode is only possible with the DP interfaces integrated in the CPU. Isochronous operation with CPs is not possible for PROFIBUS.
- Only the constant bus cycle time master is allowed as active station on isochronous PROFIBUS-DP. OPs and programming devices (or PCs with programming device functionality) influence the dynamic response of the constant bus cycle time for the DP cycle and thus are not recommended.
- Isochronous mode across subnets is not possible.
- The addresses of the isochronous I/O have to be located in the address area of the process image partitions since the isochronous I/O can only be processed in process image partitions. Without the use of process image partitions isochronous consistent data transfer is not possible. Compliance with configuration limits is monitored because the number of slaves and the number of bytes on the DP master system are limited per process image partition.
- In addition, non-isochronous I/O may be located along with isochronous I/O in the same process image partition. An isochronous module/submodule has to be located in the process image partition.
- A full isochronous mode from "terminal" to "terminal" is only possible if all components participating in the chain support the "isochronous mode" system property. When selecting in the catalog, make sure you check the "isochronous mode" or "processing in isochronous mode" entry in the information field of the module.
- When you configure isochronous mode, you cannot assign a SYNC/FREEZE group to the slave.

---

**See also**

[Assigning a DP slave to a SYNC/FREEZE group](#assigning-a-dp-slave-to-a-syncfreeze-group)
  
[Isochronous mode manual](http://support.automation.siemens.com/WW/view/en/15218045)

### Configuring and assigning parameters to isochronous mode

This section contains information on the following topics:

- [Optimizing dynamic response by selecting a suitable topology](#optimizing-dynamic-response-by-selecting-a-suitable-topology)
- [Assigning constant bus cycle time and isochronous mode parameters](#assigning-constant-bus-cycle-time-and-isochronous-mode-parameters)

#### Optimizing dynamic response by selecting a suitable topology

##### Influence of the DP topology

The dynamic response of isochronous mode can be enhanced by selecting a suitable DP topology.

##### Separation of isochronous and non-isochronous I/O

Isochronous and non-isochronous I/O can be combined in a DP master system.

It is advisable to distribute isochronous and non-isochronous I/O to different DP master systems for good performance.

If TDs, OPs or programming devices are used then you should not operate them on the isochronous DP master system.

##### Practical distribution of the I/O submodules

Reduce Ti and To times to minimum by setting the focus on a practical distribution of I/O submodules to the interface modules (ET 200M, ET 200S) when you design the DP topology.

> **Note**
>
> Vary the different configurations and calculate the temporal behavior. Select the most favorable configuration.

##### Additional information

Additional instructions for optimization of the constant bus cycle time are available in the operating instructions of the ET 200M and ET 200S DP slave families.

#### Assigning constant bus cycle time and isochronous mode parameters

This section contains information on the following topics:

- [Configuring constant bus cycle time and isochronous mode parameters](#configuring-constant-bus-cycle-time-and-isochronous-mode-parameters)
- [Setting CPU properties](#setting-cpu-properties)
- [Setting PROFIBUS properties](#setting-profibus-properties)
- [Setting the isochronous mode of DP slaves](#setting-the-isochronous-mode-of-dp-slaves)
- [Creating a user program](#creating-a-user-program)

##### Configuring constant bus cycle time and isochronous mode parameters

###### Configuration for isochronous mode

A configuration for isochronous mode consists of the following isochronous components:

- CPU with integrated DP interface (for example, CPU 319-3 PN/DP)
- DP interface modules (for example ET 200S interface IM 151-1 High Feature)
- Distributed input/output modules (for example DI 2xDC24V, High Feature [131-4BB00], DO 2xDC24V/2A, High Feature [132-4BB30])

A current list of isochronous components is available in the [Service &amp; Support Portal](http://support.automation.siemens.com/WW/view/en/14747677).

###### Procedure

To configure a constant bus cycle time and isochronous mode, follow these basic steps:

1. Configure a CPU capable of isochronous mode and set the properties for isochronous mode:

   - Isochronous mode interrupt
   - Assigned DP master system
   - Process image partition
   - Delay time
2. Configure isochronous DP slaves with isochronous modules and set the properties for isochronous mode centrally in the PROFIBUS properties or for the specific DP slaves (slave properties). Here, these are essentially the Ti/To values and how they are calculated.
3. Write the user program with accesses to the isochronous I/O.

**Note**

You can set all properties for the isochronous I/O centrally in the PROFIBUS properties. Here, you also have an overview of all slaves and their settings on PROFIBUS at the same time.

You will find a detailed description of the procedure in the next sections.

---

**See also**

[Setting CPU properties](#setting-cpu-properties)
  
[Setting PROFIBUS properties](#setting-profibus-properties)
  
[Setting the isochronous mode of DP slaves](#setting-the-isochronous-mode-of-dp-slaves)
  
[Creating a user program](#creating-a-user-program)

##### Setting CPU properties

The CPU settings for isochronous mode interrupts link the user program into isochronous mode processing using the relevant organization blocks (for example, isochronous mode interrupt OBs).

###### Requirement

The CPU must support isochronous mode and the constraints must not exclude isochronous mode.

###### Procedure

To set the CPU properties, proceed as follows:

1. Select the CPU in the device view or the network view.
2. Select the "Isochronous mode interrupts" CPU properties.
3. Make the following settings for each isochronous mode interrupt OB:

   - DP master system used
   - Required process image partition or partitions
   - Delay time

###### Additional information about the process image partitions

The assigned process image partitions must be updated in the isochronous mode interrupt OB by calling extended instructions "SYNC_PI" (SFC 126) and "SYNC_PO" (SFC 127). The "SYNC_PI" call updates the process image input partition and the "SYNC_PO" call updates the process image output partition.

If the distributed I/O addresses have been assigned to different process image partitions, enter the numbers of the process image partitions separated by commas (for example, 1,2,3).

###### Additional information on the delay time

- The delay time is the time between the global control frame and the start of OB 6x. During this time, the DP master performs the cyclic data exchange with the DP slaves.

  > **Note**
  >
  > Recommendation: There is a check box "Automatic minimum" next to the input box for the delay time. If you have selected this check box, you do not need to set the delay time again after configuration changes!
- The delay time can then only be set when the "Automatic minimum" check box is deselected.

  > **Note**
  >
  > If the delay time is 0, OB 6x starts with the global control frame. In this case, access to isochronous I/O by means of the advanced instruction "SYNC PI" (SFC 26) will very probably fail because the I/O data is not yet available at the start time of the OB.
  >
  > If a too large delay time were selected, access to the isochronous I/O would have been possible earlier. A delay time that is too large leads to an unnecessarily long OB runtime.

---

**See also**

[Configuring constant bus cycle time and isochronous mode parameters](#configuring-constant-bus-cycle-time-and-isochronous-mode-parameters)
  
[Rules, requirements, and supplemental conditions](#rules-requirements-and-supplemental-conditions)

##### Setting PROFIBUS properties

###### Introduction

To edit the properties of isochronous mode on PROFIBUS, you will need to change the settings on the subnet/DP master system.

The constant bus cycle time for isochronous mode in a PROFIBUS subnet with a constant bus cycle time is activated automatically if the following conditions are met:

- Assignment of a DP master system to the isochronous mode interrupt OB in the CPU properties for isochronous mode interrupts.
- Isochronous mode setting for a DP slave on PROFIBUS.

You only need to edit the PROFIBUS properties if you want to change the times manually. Otherwise all times will be calculated automatically.

###### Requirement

PROFIBUS subnet with constant bus cycle time.

###### Procedure

To change the properties of isochronous mode in PROFIBUS, follow these steps:

1. In the network view, select the PROFIBUS subnet, and in the Inspector window select "Constant bus cycle time" under "Properties".
2. Set the properties for the isochronous mode. You will find explanations of the specific settings in the sections below.

**Note**

Make sure that you do not select a highlighted master system. The PROFIBUS properties and the isochronous mode properties can only be changed if the PROFIBUS subnet is selected.

###### Properties for the isochronous mode are not selectable

If the properties for isochronous mode cannot be selected, check the following:

- Attachment of only one DP master on the PROFIBUS subnet. Isochronous mode is not possible if multiple DP masters are attached.
- Support of isochronous mode by the DP master (for example a CPU with an integrated DP interface).
- Configurability of the SYNC/FREEZE groups. SYNC/FREEZE groups and isochronous mode are mutually exclusive.

###### Setting DP cycle time and Ti/To values manually

If you want to set the DP cycle time manually, first clear the "Automatic minimum DP cycle time" check box. Now you can enter a higher value than the automatically calculated minimum DP cycle time.

If you want to set Ti and To values manually, first clear the "Automatic Ti/To values" check box.

###### Isochronous mode and Ti/To settings in the detailed overview

The detailed overview allows you to set the following properties for each suitable slave and/or for each suitable module in the slave:

- Isochronous mode
- Ti/To values

The detailed overview is a table. You can use the shortcut menu of the title bar of the table to adapt the tabular display, e.g. to display the values for TDPMin.

It is not possible to manually select or clear the check box "Isochronous mode" for a CPU (PLC). The check box is selected automatically if an isochronous mode interrupt is assigned to the DP master system in the "Interrupts" section of the CPU properties.

###### Possible settings for calculating the Ti/To values in the detailed overview

You can make the following settings for calculating the Ti/To values:

- From subnet  
  If you activate isochronous mode, then the option Ti/TO values "From subnet" is automatically the default. With this option, all slaves that obtain their Ti/To values from the network have identical Ti/To times (those of the PROFIBUS subnet).
- Automatic minimum  
  If, for example, you change the DP cycle time manually or change Ti/To of other slaves values manually and this change affects the Ti/To times of the slave, then all necessary adjustments will be made automatically. With this option, the Ti/To values of the slaves can deviate from each other.
- Manual  
  With this option you can enter Ti/To values for the slave manually. Errors can occur with this setting:

  - Times selected too short
  - Ti/To of other DP slaves can no longer be calculated automatically due to the settings you made

###### Display "-" for time Ti (To)

If no value is displayed for Ti or To for the PROFIBUS subnet (display "-") then this is due to the following cause: The common parts of all Ti/To value ranges of all DP slaves is used for automatic calculation of the Ti/To time for the PROFIBUS subnet. The smallest value from these common ranges is selected. If no common range can be formed then "-" is displayed. In this case, a DP slave cannot obtain a Ti/To value from the network!

---

**See also**

[Configuring constant bus cycle time and isochronous mode parameters](#configuring-constant-bus-cycle-time-and-isochronous-mode-parameters)
  
[Ti/To overlap](#tito-overlap-1)
  
[Setting the isochronous mode of DP slaves](#setting-the-isochronous-mode-of-dp-slaves)
  
[Assigning a DP slave to a SYNC/FREEZE group](#assigning-a-dp-slave-to-a-syncfreeze-group)

##### Setting the isochronous mode of DP slaves

###### Settings on the DP slave

Except for the constant bus cycle time for the DP cycle and the Ti/To times for the PROFIBUS subnet, you can make the same settings in the DP slave properties that you make in the PROFIBUS properties.

###### Procedure

To set the isochronous mode for modules, follow these steps:

1. In network view, select the DP slave whose properties you want to edit.
2. Under "Properties &gt; Isochronous mode", adapt the parameters to suit your requirements.

###### Setting Ti/To times the same for all slaves

The default behavior after adding DP slaves in network view is: Ti/To values are obtained from the network and are therefore automatically the same.

You can either set the same Ti/To times manually in an edited configuration or set all slaves so that they obtain their Ti/To values from the network.

---

**See also**

[Configuring constant bus cycle time and isochronous mode parameters](#configuring-constant-bus-cycle-time-and-isochronous-mode-parameters)
  
[Setting PROFIBUS properties](#setting-profibus-properties)

##### Creating a user program

###### Procedure

To create the user program for the isochronous mode, proceed as follows:

1. Create the necessary isochronous mode interrupt OBs (for example, OB 61).
2. In the isochronous mode interrupt OB, call the following extended instructions to update the process image partition:

   - "SYNC_PI" (SFC 126) to update the process image input partition
   - "SYNC_PO" (SFC 127) to update the process image output partition

Use the process image partition that is set on the CPU (parameter area "Isochronous mode interrupts").

> **Note**
>
> The following situation can occur, particularly with very short DP cycle times: The execution time of the user program (OB 6x with SYNC_PI/SYNC_PO called) is greater than the shortest cycle (see technical specifications of the CPU, section "Isochronous mode"). In this case, you will need to increase the automatically calculated DP cycle time manually.

---

**See also**

[Configuring constant bus cycle time and isochronous mode parameters](#configuring-constant-bus-cycle-time-and-isochronous-mode-parameters)

### Ti/To overlap

This section contains information on the following topics:

- [Ti/To overlap](#tito-overlap-1)
- [Operating principle of Ti/To overlapping](#operating-principle-of-tito-overlapping)
- [Setting isochronous mode with overlap of Ti and To](#setting-isochronous-mode-with-overlap-of-ti-and-to)

#### Ti/To overlap

##### Reduction of the system cycle and of the process reaction time

The TDP system cycle and process response time are reduced by overlapping Ti and To, that is, overlap reduces the accumulated time that includes generation and detection of an event, plus the processing time, plus the time required to return a response signal at the outputs.

##### Requirement of Ti /To overlap

Condition of overlapping Ti/To:

ET 200M: Interface module IM 153-2; article number 6ES7 153-2BAx2-0XB0 or higher

ET 200S: Interface module IM 151-1; article number 6ES7 151-2BAx2-0XB0 or higher

> **Note**
>
> Modules which handle input conversion times (TCI) and output conversion times (TCO) (depending on the operating mode of the I/O submodule) cannot be operated in isochronous mode with Ti/To overlap. Overlap of Ti and To is only possible if these modules **are not** activated for isochronous mode.

---

**See also**

[Setting PROFIBUS properties](#setting-profibus-properties)
  
[Operating principle of Ti/To overlapping](#operating-principle-of-tito-overlapping)
  
[Setting isochronous mode with overlap of Ti and To](#setting-isochronous-mode-with-overlap-of-ti-and-to)

#### Operating principle of Ti/To overlapping

##### Overlapping processes

The function principle of Ti/To overlap is based on the fact that the peripheral input module already reads its inputs while the peripheral output module is still busy transferring the process reactions of the user program to its outputs. This functionality reduces the TDP system cycle and process reaction times.

##### DP bus cycle without Ti/To overlap

The diagram below shows a constant DP bus cycle time in isochronous mode without Ti/To overlap.

![DP bus cycle without Ti/To overlap](images/6584422795_DV_resource.Stream@PNG-en-US.png)

##### DP bus cycle with Ti/To overlap

The diagram below shows a constant bus cycle time in isochronous mode with Ti/To overlap.

![DP bus cycle with Ti/To overlap](images/6584426507_DV_resource.Stream@PNG-en-US.png)

##### Rules for Ti, To and TDP

Rules for Ti, To and TDP:

- Ti + To ≤ TDP without overlap, that is: TDP ≥ Ti + To
- The conditions Ti + To &gt; TDP or TDP &lt; Ti + To may develop with overlap

---

**See also**

[Ti/To overlap](#tito-overlap-1)

#### Setting isochronous mode with overlap of Ti and To

##### Configuring isochronous mode with Ti/To overlap

For isochronous mode with Ti/To overlap you must be aware of the following:

The DP slave for which Ti/To overlap is possible should not get its Ti/To values from the PROFIBUS subnet. For this DP slave select the option "Ti/To values automatic".

The best-possible values for Ti and To are set automatically, depending on the current set constant bus cycle time for DP cycle.

##### Rules for Ti/To overlap

Rules for operation in isochronous mode with Ti/To overlap:

- Ti ≤ TDP
- To ≤ TDP

##### Finding system reserves

Visualize the sequences using a [calculation table](http://support.automation.siemens.com/WW/view/en/23876584) to determine system reserves and use the result to optimize these sequences in STEP 7.

> **Note**
>
> **Disclaimer of liability**
>
> Siemens AG shall not be liable for material or immaterial damage caused by the use of the calculation table. Any liability of Siemens AG in particular for direct or consequential injury, damage to assets and financial losses sustained as a result of the use of the calculation table shall be ruled out.
>
> Siemens does not provide support for the calculation table.

> **Note**
>
> Remember the rules governing the optimization of the constant bus cycle times and Ti/To overlap.

##### Additional information

Additional information for optimizing the constant bus cycle time are provided in the ET 200M operating instructions and in the ET 200S operating instructions.

---

**See also**

[Ti/To overlap](#tito-overlap-1)
