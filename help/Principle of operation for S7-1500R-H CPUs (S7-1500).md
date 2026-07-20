---
title: "Principle of operation for S7-1500R/H CPUs (S7-1500)"
package: ProgCPU15RHenUS
topics: 42
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Principle of operation for S7-1500R/H CPUs (S7-1500)

This section contains information on the following topics:

- [Operating principle of the redundant system S7-1500R/H (S7-1500)](#operating-principle-of-the-redundant-system-s7-1500rh-s7-1500)
- [Configuration of the redundant system S7-1500R/H (S7-1500)](#configuration-of-the-redundant-system-s7-1500rh-s7-1500)
- [Operating modes and system states (S7-1500)](#operating-modes-and-system-states-s7-1500)
- [Basics of program execution (S7-1500)](#basics-of-program-execution-s7-1500)
- [Loading an S7-1500R/H CPU (S7-1500)](#loading-an-s7-1500rh-cpu-s7-1500)
- [Communication with the R/H system (S7-1500)](#communication-with-the-rh-system-s7-1500)
- [Diagnostics of the redundant system S7-1500R/H (S7-1500)](#diagnostics-of-the-redundant-system-s7-1500rh-s7-1500)

## Operating principle of the redundant system S7-1500R/H (S7-1500)

### Special features of the redundant system S7-1500R/H

Redundant automation systems are used to reach higher availability. For high availability systems, the probability of production losses is reduced by the parallel operation of two systems. The redundant system S7-1500R/H has the following special features compared to the S7-1500 automation system:

- For the redundant system S7-1500R/H, the CPUs are duplicated, meaning they are redundant. If one of the two CPUs fails, the other CPU takes over the process control at the interruption point. The failure of the CPU has no effect on the controlled process. To ensure takeover of the process control, the process-controlling CPU (primary CPU) synchronizes itself via a redundant synchronization connection (redundancy connection) with the non-process-controlling CPU (backup CPU).

  You can find information on the configuration of the S7-1500R/H system in the section "[Configuration of the redundant system S7-1500R/H](#configuration-of-the-redundant-system-s7-1500rh-s7-1500)".
- The I/O is connected in an S7-1500R/H system to the CPUs via a PROFINET ring and is configured as a media redundancy ring.

  You can find additional information on the media redundancy ring in the section "[Configuring media redundancy](Special%20PROFINET%20configurations.md#configuring-media-redundancy)".
- There are new operating and system states in the S7-1500R/H systems.

  You can find additional information in the section "[Operating and system states](#operating-modes-and-system-states-s7-1500)".
- There are special instructions and organization blocks (OBs) for the S7-1500R/H CPUs.

  You can find additional information in the section "[Basics of program execution](#basics-of-program-execution-s7-1500)".
- Project data can be downloaded to the primary CPU or to the backup CPU.

  You can find additional information in the section "[Loading an S7-1500R/H CPU](#loading-an-s7-1500rh-cpu-s7-1500)".
- In addition to supporting device IP addresses, redundant systems support a system IP address.

  You can find additional information in the section "[Communication with the R/H System](#communication-with-the-rh-system-s7-1500)".
- New diagnostic options are available for the redundant system S7‑1500R/H.

  You can find information in the section "[Diagnostics of the redundant system S7-1500R/H](#diagnostics-of-the-redundant-system-s7-1500rh-s7-1500)".

The complete documentation on the S7-1500R/H redundant system is available in the system manual of the S7-1500R/H redundant system and in the linked documents.

### Restrictions and special features (hardware)

When using the redundant system S7-1500R/H there are restrictions for the hardware compared to the S7-1500 automation system. Below you can find examples for some restrictions:

- Support for central I/O and central communications modules in the hardware configuration of the redundant system S7-1500R/H is limited to the CP 1543-1

  Exceptions: Load current supply (PM), system power supply (PS)
- Fail-safe modules are only supported by the HF CPUs
- No support of series machine projects, configuration control (options handling)
- Longer cycle and reaction times

A complete overview of all restrictions for the redundant system S7-1500R/H compared to the S7-1500 automation system can be found in the section "Operational planning &gt; Restrictions" in the "Redundant System S7-1500R/H" system manual.

### Restrictions and special features (software)

When using the redundant system S7-1500R/H there are restrictions for the software compared to the S7-1500 automation system. Below you can find examples for some restrictions:

- No support or restrictions for specific instructions
- Firmware update via accessible devices is not supported
- No support of hardware detection in STEP 7 (read out configuration)
- The direct entry of tag names on the HMI device is only possible in the RUN-Solo system state
- The S7-1500R/H redundant system cannot be used as an I-device
- Temporary local data for functions (FCs): The system initialization for standard access is identical for S7-1500R/H-CPUs as for optimized access, for the description of the system initialization for optimized access see [Parameter assignment to functions](Programming%20basics.md#parameter-assignment-to-functions)
- No support of IRT, MRPD
- No support of isochronous operation
- Motion Control functions are not supported in the CPUs
- No support of multiuser engineering
- SIMATIC Automation Tool (SAT tool) not supported
- No support of shared device
- You can only test with breakpoints in the STARTUP (startup OB) or RUN-Solo system state
- The storage of measurements on the SIMATIC memory card (measurements in the device) is not supported

A complete overview of all restrictions for the redundant system S7-1500R/H compared to the S7-1500 automation system can be found in the section "Operational planning &gt; Restrictions in comparison to the S7-1500 automation system" in the "Redundant System S7-1500R/H" system manual.

### Communication restrictions

- Programming device communication:

  - Is not possible to access both CPUs at the same time. You can access either the primary CPU either backup CPU.
  - No loading of objects (e.g. blocks) possible in redundant mode (RUN-Redundant state); neither a "Download to device" nor an "Upload from device" is possible. Furthermore, working with snapshots for tags of a data block is not possible in this system state.
  - The function "Upload device as new station" is not supported.
- Open User Communication:

  - No configured connections
  - Instruction TMAIL_C can only be used up to and including V4.1
  - No FDL connections
  - Connection establishment (instruction TCON) not possible with connection description DB with a structure to TCON_Param
- No OPC UA client
- No S7 communication as client
- No S7 routing between the PROFINET interface X1 and the PROFINET interface X2 of the CPUs

---

**See also**

[System IP addresses (S7-1500)](#system-ip-addresses-s7-1500)

## Configuration of the redundant system S7-1500R/H (S7-1500)

This section contains information on the following topics:

- [Creating R/H CPUs (S7-1500)](#creating-rh-cpus-s7-1500)
- [Configuring R/H CPUs (S7-1500)](#configuring-rh-cpus-s7-1500)
- [Creating IO devices for R/H systems (S7-1500)](#creating-io-devices-for-rh-systems-s7-1500)
- [Creating an MRP ring configuration (S7-1500)](#creating-an-mrp-ring-configuration-s7-1500)
- [MRP interconnection with the redundant system S7-1500R/H (S7-1500)](#mrp-interconnection-with-the-redundant-system-s7-1500rh-s7-1500)

### Creating R/H CPUs (S7-1500)

You can configure the redundant system S7-1500R/H in different versions. A PROFINET ring is mandatory for all configuration versions.

For the configuration versions of the S7-1500R/H system the redundancy exists for the following components:

- R/H CPUs
- Synchronization interfaces
- Network in the PROFINET ring

This section describes a possible configuration version. You can find a description of additional configuration versions in the section "Configuration versions" in the "Redundant System S7-1500R/H" system manual.

#### Creating R/H CPUs

In the network view, you select an R/H-CPU from the hardware catalog and create it together with a rack. Drag the desired modules from the hardware catalog to this device; the modules are arranged automatically on the rack.

To select an R/H CPU from the hardware catalog, follow these steps:

1. In the hardware catalog navigate to the folder with the desired R/H CPUs.
2. Open the folder with the R/H CPU type you are looking for. You will see all article numbers for the selected R/H CPU type.
3. Click an R/H CPU article number to get information about the selected R/H CPU in the "Information" pane.
4. Set the matching firmware version of your R/H CPU in the "Version" drop-down list.
5. Set up the R/H CPU and a rack. You have the following options:

   - Drag-and-drop the R/H CPU from the hardware catalog into the network view.
   - Double-click the R/H CPU item in the hardware catalog.

#### Representation in the network view

STEP 7 automatically creates both R/H CPUs of the redundant system. STEP 7 displays both R/H CPUs in the network view graphically:

![Representation in the network view](images/109736697995_DV_resource.Stream@PNG-de-DE.png)

#### Representation in the project tree

In the STEP 7 project tree, each of the two R/H CPUs of the redundant system is displayed in its own tree. The project tree contains all elements and editors of the project.

| Symbol | Meaning |
| --- | --- |
| ![Representation in the project tree](images/109709323403_DV_resource.Stream@PNG-en-US.png) | For each redundant system in the project there is a separate folder which has an internal project name. Below this folder you find the device configuration and diagnostic options that apply to the overall system. |
| ![Representation in the project tree](images/109718568715_DV_resource.Stream@PNG-en-US.png) | There is one folder each for both CPUs of the redundant system, each having an internal project name.  The CPU displayed in the project tree above has the redundancy ID "1". Below the CPU its properties are displayed.  In addition this contains further properties of the redundant system, the user program and additional system-relevant project items.  In the "Distributed I/O" folder you find links to the distributed I/O devices assigned to the CPU. |
| ![Representation in the project tree](images/109718572427_DV_resource.Stream@PNG-en-US.png) | The CPU displayed in the project tree below has the redundancy ID "2". Below the CPU its properties are displayed. |
| ![Representation in the project tree](images/109718576139_DV_resource.Stream@PNG-en-US.png) | All distributed I/O devices in the project are collected together in the "Ungrouped devices" folder. |

You can find additional information in the section "Function and structure of the project tree" of the information system.

#### Redundant IDs and IP addresses

Each CPU of the redundant system has a redundancy ID. With the redundancy ID, a project tree is assigned to the real CPU in STEP 7. The top CPU in the tree (in this example: PLC_1) is always the CPU with the redundancy ID "1". The CPU below this (in this example: PLC_2) has the redundancy ID "2".

![Redundant IDs and IP addresses](images/112320247435_DV_resource.Stream@PNG-en-US.png)

If a CPU has a valid hardware configuration and you change the redundancy ID of this CPU, you also change the name and IP addresses of this CPU. You can find additional information in the section "Redundancy ID" of the "Redundant System S7-1500R/H" system manual.

### Configuring R/H CPUs (S7-1500)

#### Assigning an IP address

STEP 7 automatically assigns an IP address to each PROFINET interface of a CPU. You can also assign the IP addresses manually, for example in case of a conflict.

For the PROFINET interface X1 of the CPUs, the IP addresses must be located in the same subnet.

The IP address is displayed in the CPU properties, in the "PROFINET interface [X1]" area of the "IP protocol" section.

![Assigning an IP address](images/109751275147_DV_resource.Stream@PNG-en-US.png)

#### Assigning system IP address

In addition to the device IP addresses of the CPUs, you can also assign system IP addresses for the redundant system S7‑1500R/H; for each PROFINET interface you can assign a system IP address for switched communication in addition to the "normal" (devices) IP addresses.

You use the system IP address for communication with other devices (for example, HMI devices, CPUs, PG/PC). The devices always communicate over the system IP address with the primary CPU of the redundant system. This ensures, for example, that the communication partner can communicate with the new primary CPU (previously backup CPU) in the RUN-Solo system state after failure of the original primary CPU in redundant operation.

Follow these steps to activate the system IP address for the PROFINET interfaces X1 of both CPUs:

1. Select a CPU in the network view. Select the "Properties" tab in the Inspector window.
2. Select the area "PROFINET interface [X1]" and the section "System IP address for switched communication" in the area navigation.
3. Make sure that the check box "Enable the system IP address for switched communication" is selected for the interface X1. Apply or assign the system IP address in the "IP address" field.   
   The subnet mask cannot be modified and corresponds to the subnet mask of the IP protocol.
4. Then apply or assign a virtual MAC address to the system IP address.   
   The virtual MAC address is six bytes long. The assignment of the bytes is hexadecimal.
5. The other CPU applies the settings automatically.

   ![Assigning system IP address](images/109751283723_DV_resource.Stream@PNG-en-US.png)

   ![Assigning system IP address](images/109751283723_DV_resource.Stream@PNG-en-US.png)

**Note**

**Virtual MAC address**

Ensure that all MAC addresses stored in the Ethernet broadcast domain are unique. This applies in particular to systems with third-party devices consisting of VRRP and redundant systems that are configured through several STEP 7 projects.

For additional information on the system IP address, refer to the "Communication function manual".

#### Setting the cycle monitoring time

STEP 7 assigns default values for the minimum and maximum scan cycle times.

The default values are displayed in the "Cycle" area of the CPU properties.

> **Note**
>
> **Setting the cycle time as large as possible**
>
> Select the minimum scan cycle time and the maximum cycle time as large as your process allows.
>
> - The time for the ongoing synchronization of the two CPUs in redundant operation is included in the cycle time.
> - At a system state transition SYNCUP → RUN Redundant, a temporary increase of the cycle time can occur.
>
> If only one CPU controls the process (RUN-Solo system status), the cycle time is significantly shorter than during redundant operation.

### Creating IO devices for R/H systems (S7-1500)

To best use the advantages of the redundant R/H system, you must use IO devices with S2 system redundancy or R1 system redundancy and connect them accordingly. You can also use standard IO devices, but this limits the extent to which you can use the possibilities of the R/H system with switched S1 devices ("S1 system redundancy").

#### Redundancy terminology

You must be familiar with the following terms and meanings in the context of redundancy:

- NAP = Network Access Point.   
  The PN interface of an IO device is referred to as NAP. For the PROFINET redundancy functions S1/S2 and R1/R2, the letter stands for the number of NAPs used. If one NAP is used for the IO device, it is called an S = Single NAP. If two NAPs are used, they are referred to as R = Redundant NAPs.
- AR = Application Relation.   
  An AR is a communication relationship between IO controller and IO device. An AR exists when an IO device is connected to an IO controller. Two ARs exist if there is a communication relationship to both IO controllers in a redundant system with one primary CPU and one backup CPU.
- S1 = System redundancy with a single NAP and 1 AR.  
  The PROFINET node of the IO device supports one communication relationship with the R/H system using a single network access point. Each standard IO device supports S1. This is not a true system redundancy: When the primary CPU fails, there is a brief interruption of the PROFINET communication until the former backup CPU continues operation as new primary CPU.
- S2 = System redundancy with a single NAP and 2 ARs.  
  The PROFINET node of the IO device supports two communication relationships with the R/H system using a single network access point. Only IO devices with S2 capability support S2 system redundancy: When the primary CPU fails, PROFINET communication is continued without interruption by the previous backup CPU.
- R1 = System redundancy with 2 (redundant) NAPs with 1 AR each.   
  Both PROFINET nodes of the IO device support one communication relationship to the R/H system each. If a PROFINET node fails, the PROFINET communication to the R/H system is continued by the IO device via the redundant node.

#### System redundancy S2

IO devices with S2 system redundancy enable uninterrupted process data exchange with the S7-1500R/H redundant system in the event of a CPU failure.

An IO device with S2 system redundancy supports a redundant application relation, so-called system redundancy ARs. In a redundant system, an IO device with S2 system redundancy has a system redundancy AR with each of the two CPUs (IO controllers). An IO device thus supports ARs of two IO controllers simultaneously (for the same modules).

A system redundancy AR can be the primary AR or the backup AR. An IO device activates the data of the primary AR at the outputs. The data of the backup AR is merely saved.

- Behavior in the RUN-Redundant system state:

  Both CPUs are IO controllers. PROFINET communication runs on both system redundancy ARs simultaneously, in each case between one of the CPUs (IO controller) and the IO device. If the primary CPU then fails, the backup CPU becomes the primary CPU and also switches the backup AR to primary AR. The data of this AR then becomes active at the outputs.
- Behavior in the RUN-Solo system state:

  Only the primary CPU is the IO controller. PROFINET communication runs on the primary AR between the primary CPU and the IO device. There is no AR between the backup CPU and the IO device.

In STEP 7, you configure an IO device connected system-redundant by assigning an IO device with S2 system redundancy to both CPUs of the redundant system S7‑1500R/H.

#### Switched S1 device

As of firmware version V2.8, the S7-1500R/H redundant system supports the switched S1 device function.

The "Switched S1 device" function of the CPU enables the operation of standard IO devices on the redundant S7-1500R/H system. This also allows you to operate existing PROFINET IO configurations on the S7-1500R/H redundant system. Standard IO devices are always assigned to both CPUs of the S7-1500R/H redundant system. In contrast to an IO device with S2 system redundancy, a standard IO device supports only one AR. The AR is always available to the primary CPU of the S7-1500R/H redundant system.

- Behavior in the RUN-Redundant system state:  
  PROFINET communication runs on the AR between the primary CPU (IO controller) and the standard IO device. There is no AR between the backup CPU and the standard IO device.  
  If the primary CPU fails or is switched to STOP, the S7‑1500R/H redundant system responds as follows:

  - The AR between the primary CPU and the standard IO device is disconnected.
  - The previous backup CPU becomes the new primary CPU.
  - The S7-1500R/H redundant system temporarily has no access to the inputs and no control over the outputs of the standard IO device. During this time, the configured substitute value behavior applies to the modules of the standard IO device.
  - The new primary CPU builds an AR to the standard IO device.
  - As soon as the new primary CPU has set up the AR, the S7-1500R/H redundant system has access to the inputs again and control over the outputs of the standard IO device.
- Behavior in the RUN-Solo system state:  
  Only the primary CPU is the IO controller. PROFINET communication runs on the AR between the primary CPU (IO controller) and the standard IO device. There is no AR between the backup CPU and the standard IO device.

In STEP 7 you configure an IO device connected via the "Switched S1 device" function by assigning a standard IO device to both CPUs of the redundant S7‑1500R/H system.

#### System redundancy R1

As of firmware version V3.0, the redundant S7-1500H system supports the R1 system redundancy function.

IO devices that support the system redundancy R1 function - called "R1 devices" for short - are equipped with two interface modules compared to S2 devices. If one interface module fails, the R1 device can still be reached by the H CPUs via the second interface module.  
This means that R1 devices have higher availability than S2 devices.

If you configure the redundant system with R1 devices, two separate PROFINET rings are then required.

#### Creating and assigning IO devices with S2 system redundancy

Add IO devices with S2 system redundancy to the configuration with R/H CPUs. To do so, follow these steps:

1. In the hardware catalog, look for IO devices with S2 system redundancy under Distributed I/O or

   click on the IO device article number in the catalog to find IO devices with the note on S2 system redundancy in the "Information" pane.
2. If necessary, set the matching firmware version of your IO device in the "Version" drop-down list.
3. Drag-and-drop the IO device from the hardware catalog into the network view or

   double-click the IO device item in the hardware catalog.
4. Drag-and-drop the desired modules on the respective slots of the IO device.

   If necessary, add additional IO devices.
5. To assign IO devices to the redundant system S7‑1500R/H, connect every IO device to each CPU:

   - Drag-and-drop a line between the PROFINET interface of the IO device and the PROFINET interface X1 of the left CPU.
   - Drag-and-drop a line between the PROFINET interface of the IO device and the PROFINET interface X1 of the right CPU.
6. If necessary, assign further IO devices to both CPUs in the same way.

   The IO devices are connected system-redundantly to the S7‑1500R/H system.

![Creating and assigning IO devices with S2 system redundancy](images/109752252299_DV_resource.Stream@PNG-en-US.png)

#### Creating and assigning IO devices with R1 system redundancy

If you want to connect an R1 device to an S7-1500H system via a ring topology, the communication occurs via two separate PROFINET rings. You have to create another MRP domain in STEP 7 for this.

![Creating and assigning IO devices with R1 system redundancy](images/157020684171_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPU 1 |
| ② | CPU 2 |
| ③ | Two fiber-optic cables (redundancy connections) |
| ④ | PROFINET cable (PROFINET ring 1, corresponds to the first MRP domain) |
| ⑤ | PROFINET cable (PROFINET ring 2, corresponds to the second MRP domain) |
| ⑥ | IO device ET 200SP HA (with R1 system redundancy) |
| ⑦ | IO device ET 200SP (with R1 system redundancy) |

Instead of the ET 200SP HA shown in the picture, two ET 200SP (IM 155-6 PN R1) are to be used for the configuration. Proceed as follows for configuration with STEP 7:

1. Place an S7-1500H system (as of firmware V3.0) in the network view.
2. Click on the PN/IE_1 connection between the PROFINET interfaces X1 of the two H CPUs and create a new MRP domain.  
   To do this, navigate to the properties of the PROFINET interface in the Inspector window ("Domain management &gt; MRP domains" area).
3. Drag an ET 200SP (IM 155-6 PN R1) from the hardware catalog as an R1 device into the network view.
4. Connect the left interface module of the R1 device to the H CPU with redundancy ID 1 (PROFINET interface X1 of the left H CPU).
5. Connect the right interface module of the R1 device to the H CPU with redundancy ID 2 (PROFINET interface X1 of the right H CPU).
6. Switch to the device view of the IM 155-6 PN R1 and set the watchdog timer for both interface modules. To do this, navigate in the Inspector window to "Properties &gt; PROFINET interface [X1] &gt; Advanced options &gt; Real time settings &gt; IO cycle".
7. Drag an additional ET 200SP (IM 155-6 PN R1) from the hardware catalog as an R1 device into the network view.
8. Repeat steps 4 to 6 for this second R1 device.

   Result:

![Creating and assigning IO devices with R1 system redundancy](images/156963096715_DV_resource.Stream@PNG-en-US.png)

As soon as you create an S7‑1500H redundant system in STEP 7, STEP 7 automatically assigns the MRP role "Not device in the ring" for the PROFINET interfaces X1 of the two CPUs. You have to change the MRP role to "Manager (auto)" for the configuration as PROFINET ring:

1. Switch to the device view of the S7-1500H redundant system. The two redundant CPUs are displayed one above the other.
2. Select the PROFINET interface X1 of the upper H CPU of the S7 1500H redundant system.
3. In the Inspector window, navigate to "Properties &gt; General &gt; Advanced options &gt; Media redundancy".
4. Change the MRP domain to "mrpdomain-1" (if required) and the media redundancy role for the H CPU to "Manager (auto)".
5. Select the PROFINET interface X1 of the lower H CPU of the S7‑1500H redundant system.
6. Change the MRP domain to "mrpdomain-2" (if required) and the media redundancy role for the H CPU to "Manager (auto)".
7. Enable the "Diagnostic interrupts" option.

If the option "Diagnostic interrupts" is enabled, diagnostic interrupts are generated when the following wiring or port errors occur at the ring ports:

- A neighbor of the ring port does not support media redundancy MRP.
- A ring port is connected to a non-ring port.
- A ring port is connected to the ring port of a different MRP domain.

You then need to set the MRP role and MRP domain for the R1 devices of the S7-1500H redundant system.

To set the media redundancy for the R1 devices as nodes of the rings, proceed as follows:

1. Switch to the device view of the first IM 155-6 PN R1.
2. Click on the PROFINET interface X1 of the left interface module.
3. Change the MRP domain to "mrpdomain-1" (if required) and the media redundancy role to "Client".
4. Click on the PROFINET interface X1 of the right interface module.
5. Change the MRP domain to "mrpdomain-2" and the media redundancy role to "Client".
6. Repeat steps 2 to 5 in the device view for the second IM 155-6 PN R1.
7. If there are additional stations in the PROFINET ring that are not configured in STEP 7: Set the MRP role "Client" for these nodes of the PROFINET rings.

#### Configuring line topology for S7-1500H

As of firmware version V3.0, you can connect both S2 devices and R1 devices to an S7-1500H system in a line topology.

For example, a configuration with R1 devices in a line topology looks like this:

![Configuring line topology for S7-1500H](images/157020726667_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPU 1 |
| ② | CPU 2 |
| ③ | Two fiber-optic cables (redundancy connections) |
| ④ | PROFINET cable (line topology 1) |
| ⑤ | PROFINET cable (line topology 2) |
| ⑥ | IO device ET 200SP HA (with R1 system redundancy) |
| ⑦ | IO device ET 200SP (with R1 system redundancy) |

Line topology requires less wiring work compared to ring topologies. Only one PROFINET line is connected to each of the PROFINET interfaces X1 of the H CPUs.

It is **not** necessary to configure MRP domains and the MRP roles.

The reconfiguration times of the R1 devices are significantly reduced and shorter monitoring times are therefore possible.

#### Configuring routers in R/H systems

When using routers in R/H systems, you must pay attention to a consistent configuration in the router settings of the CPUs and IO devices. You avoid an error in the consistency check of the router addresses by not confusing the following configuration options:

- If the interface setting "Synchronize router settings with IO controller" is enabled in an assigned IO device, use of the router must be activated, and the same router address must be set in the primary CPU and backup CPU of the S7-1500R/H system under "PROFINET interface &gt; Ethernet addresses &gt; IP protocol".
- If different router addresses are set in the primary CPU and backup CPU of the S7-1500R/H system under "PROFINET interface &gt; Ethernet addresses &gt; IP protocol" with activated use of the router, the interface setting "Synchronize router settings with IO controller" must be disabled in the IO device.

Below you will find the description of an inconsistent configuration of an R/H system:

- Router A is configured for the primary CPU.
- Router B is configured for the backup CPU.
- The IO device has been configured with "Synchronize router settings with IO controller".

![Configuring routers in R/H systems](images/125205149707_DV_resource.Stream@PNG-de-DE.png)

1. During startup of the primary CPU, the primary communication relationship to the IO device is established; the primary CPU also transmits the address of Router A in the process.
2. During startup of the backup CPU, the backup communication relationship to the IO device is established; the backup CPU also transmits the address of Router B in the process.

A consistency error occurs in the IO device because it has already received the address of Router A that is different from the address of Router B. This prevents that a backup communication relationship is established. The IO device does not behave like an S2 device, and the cyclic IO data exchange would not be smooth if the primary CPU were to fail in case of redundancy.

#### Tip: Check consistency

If you also use STEP 7 to configure the topology of the S7-1500R/H system with the IO devices, the consistency is checked by STEP 7. Error messages indicate an incorrect configuration.

---

**See also**

[Specifying the router for a PROFINET IO device](Configuring%20devices%20and%20networks.md#specifying-the-router-for-a-profinet-io-device)

### Creating an MRP ring configuration (S7-1500)

#### Connecting IO devices to S7-1500R/H via ring topology

A configuration with an S7-1500R system and IO devices connected to a PROFINET ring is required.

The redundant system continues to operate following a cable interruption anywhere in the PROFINET ring.

![Connecting IO devices to S7-1500R/H via ring topology](images/157020756363_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPU 1 |
| ② | CPU 2 |
| ③ | PROFINET cable (redundancy connections, PROFINET ring) |
| ④ | IO device ET 200MP (with S2 system redundancy) |
| ⑤ | IO device ET 200SP (with S2 system redundancy) |

#### Setting the MRP role of the R/H CPU

As soon as you create a redundant system S7-1500R/H in STEP 7, STEP 7 automatically assigns the MRP role "Manager (auto)" for the PROFINET interfaces X1 of both CPUs.

#### Defining the MRP role for additional stations of the ring

Follow these steps to determine the media redundancy for additional stations in the ring:

1. In the network view of STEP 7, select the PROFINET interface X1 of one of the two CPUs of the redundant system S7-1500R/H.
2. In the Inspector window navigate to "Properties" &gt; "General" &gt; "Advanced options" &gt; "Media redundancy".

   ![Defining the MRP role for additional stations of the ring](images/109752350475_DV_resource.Stream@PNG-en-US.png)

   ![Defining the MRP role for additional stations of the ring](images/109752350475_DV_resource.Stream@PNG-en-US.png)
3. Click the "Domain settings" button.

   In the Inspector window STEP 7 displays the properties of the MRP domain in which the PROFINET interface X1 of the CPU is located.
4. In the "MRP role" column of the "Devices" table assign the MRP role "Client" to all additional stations.

   ![Defining the MRP role for additional stations of the ring](images/109752359051_DV_resource.Stream@PNG-en-US.png)

   ![Defining the MRP role for additional stations of the ring](images/109752359051_DV_resource.Stream@PNG-en-US.png)

#### Parameterizing stations outside the STEP 7 project

Set the MRP role "Client" for the stations of the ring that are not located in STEP 7.   
For a switch, for example, set the MRP role "Client" via the web interface of the switch.

### MRP interconnection with the redundant system S7-1500R/H (S7-1500)

The S7-1500R/H CPUs support MRP interconnection as of firmware version V2.9.

MRP interconnection enables the redundant data exchange via S7-1500R/H across two or more MRP rings.

MRP interconnection implements the redundancy on the network level. S7-1500R/H implements the redundant PROFINET communication.

#### Requirements for S7-1500R/H

In addition to the requirements for S7-1500, the following requirements are in effect for S7-1500R/H:

- The two CPUs of the redundant S7-1500R/H system are located in the same ring.
- You have configured the media redundancy role of the two CPUs as "Manager(Auto)" in the ring with the two R/H-CPUs.

  You have configured the following in the other rings:

  - For one or more PROFINET devices the media redundancy role "Manager(Auto)" or
  - For exactly one PROFINET device the media redundancy role "Manager"

  You have assigned the MRP client role to the other devices in all rings.

#### Topology

You can find the description of possible topologies (two rings and multiple rings) in the PROFINET Function Manual.

#### Tool for setting the watchdog timer

For the correct setting of the watchdog timer, you can use the "[S7-1500R/H AddIn](https://support.industry.siemens.com/cs/de/en/view/109769093)" which available on the Internet and can also be used for MRP interconnections.

---

**See also**

[MRP interconnection (S7-1500, S7-1500T)](Special%20PROFINET%20configurations.md#mrp-interconnection-s7-1500-s7-1500t)

## Operating modes and system states (S7-1500)

This section contains information on the following topics:

- [Overview (S7-1500)](#overview-s7-1500)
- [STARTUP mode (S7-1500)](#startup-mode-s7-1500)
- [STOP mode (S7-1500)](#stop-mode-s7-1500)
- [SYNCUP operating mode (S7-1500)](#syncup-operating-mode-s7-1500)
- [RUN operating modes (S7-1500)](#run-operating-modes-s7-1500)
- [SYNCUP system status (S7-1500)](#syncup-system-status-s7-1500)

### Overview (S7-1500)

The S7-1500R/H CPUs have the same operating modes as S7-1500 standard CPUs and additional operating modes.

System states map a state that results from the operating modes of the two CPUs in the redundant system.

You can find additional information in the section "Operating modes and system states" in the "Redundant system S7-1500R/H" system manual.

#### Operating modes

Operating modes describe the behavior of a single CPU at a specific time. The knowledge about the operating modes of the CPUs is useful for programming the startup, the test and the error diagnostics. The status LEDs on the front of the CPU and the CPU display indicate the current operating mode.

Like the S7-1500 standard CPUs, the S7-1500R/H CPUs have the operating modes STOP, STARTUP and RUN. For operation as redundant system, one of the two CPUs can have on an additional operating mode, SYNCUP, for synchronizing the two subsystems. The operating mode RUN is divided into RUN, RUN-Syncup and RUN-Redundant for redundant systems.

#### System states

The system states enable the direct assessment of the behavior of a redundant system. They result from the combination of the operating modes of the individual CPUs.

#### Overview of operating modes and system states

The following figure shows the possible operating modes of the CPUs and the resulting system states.

In general, both CPUs have equal status so that each CPU can be either primary or backup CPU. The CPU that you first switched fromSTOP to RUN becomes the primary CPU.

![Overview of operating modes and system states](images/112187700747_DV_resource.Stream@PNG-en-US.png)

The following table provides you with an overview of how the redundant system powers up and at the same time runs through the various operating modes and system states. The following starting situation and the action steps are an example.

The operating modes and system states are described in detail in the following sections.

Startup of the redundant system

| No. in the screen | Primary CPU | System state | Backup CPU |
| --- | --- | --- | --- |
| Initial situation: Both CPUs are in STOP mode. The mode selector is also in STOP position. |  |  |  |
| 1st step: Switch the mode selector on the CPU which is to be the **primary CPU** from STOP to RUN. |  |  |  |
| ① | The CPU goes into STARTUP and processes the startup OB 100 and any additional startup OBs. | STOP → STARTUP | The CPU remains in STOP. |
| ② | After successful STARTUP the CPU switches to RUN.  The CPU runs in RUN, like a standard CPU and processes your user program. | STARTUP → RUN-Solo | The CPU remains in STOP. |
| 2nd step: Switch the mode selector on the **Backup CPU** from STOP to RUN. |  |  |  |
| ③ | RUN → RUN-Syncup | RUN-Solo → SYNCUP | STOP → SYNCUP |
| Both user programs are synchronized for redundant operation. The primary CPU copies the load memory and work memory content to the backup CPU. The backup CPU syncs up with the user program processing of the primary CPU. After successful synchronization, both CPUs have identical memory content. |  |  |  |
| ④ | RUN-Syncup → RUN-Redundant | SYNCUP → RUN-Redundant | SYNCUP → RUN-Redundant |
| After the SYNCUP CPUs go to RUN-Redundant mode. Both CPUs process the user program synchronously. |  |  |  |

### STARTUP mode (S7-1500)

#### Startup processing (the primary CPU only)

The STARTUP is only executed by the primary CPU.

In STARTUP mode, the CPU behaves like an S7-1500 standard CPU.

#### Behavior

Before the CPU starts to execute the cyclic user program, a startup program is executed.

In STARTUP the CPU compares the existing I/O configuration with the hardware configuration that you created with STEP 7.

By suitably programming startup OBs, you can specify initialization tags for your cyclic program in the startup program. You have the option of programming no Startup OB, one Startup OB, or several Startup OBs.

#### Special features

- All outputs are disabled or react according to the parameter settings for the respective module: They provide a substitute value as set in the parameters or retain the last value output and bring the controlled process to a safe operating state.
- The process image is initialized.
- The process image is not updated.  
  In order to read the current state of inputs during STARTUP, you can access inputs by direct I/O access.  
  In order to initialize outputs during STARTUP, you can write the values via the process image or via direct I/O access. The values are output at the outputs during the transition to the RUN mode.
- The CPU always starts up in a warm restart.

  - If you define data as retentive, its content is retained for the startup of a program after STOP or a voltage failure.
  - The non-retentive bit memory, timers and counters are initialized.
  - The non-retentive tags in data blocks are initialized.
- During STARTUP no cycle time monitoring is running yet.
- The CPU processes the startup OBs in the order of the startup OB numbers. The CPU processes all programmed startup OBs irrespective of the selected startup mode (see figure below "Setting the startup behavior").
- If a corresponding event occurs, the CPU can start the following OBs in startup:

  - OB 82: Diagnostics interrupt
  - OB 83: Removal/insertion of modules
  - OB 86: Rack error
  - OB 121: Programming error (only for global error handling)
  - OB 122: I/O access error (only for global error handling)

  The CPU starts all other OBs after the transition to the RUN mode.

---

**See also**

[Overview (S7-1500)](#overview-s7-1500)

### STOP mode (S7-1500)

#### Behavior

CPUs of the redundant system behave in STOP exactly as S7-1500 standard CPUs.

The CPU does not execute the user program in STOP mode.

If both CPUs are in STOP mode, all outputs are disabled or react according to the parameter settings for the respective module: They provide a substitute value as set in the parameters or retain the last value output and thus hold the controlled process in a safe operating state.

#### Special features

In STOP mode, the backup CPU does not establish any connections to the IO devices.

In STOP mode, the primary CPU establishes connections to the IO devices. The primary CPU also enables the system IP address in STOP mode, provided the system IP address has been configured.

If both CPUs are in STOP and you load a configuration in the CPU, make sure to note the following:

- You must start the CPU in which you have loaded the configuration first, in order that it is/remains the primary CPU.
- When you load to the primary CPU, connected IO devices are also parameterized according to the loaded hardware configuration in STOP mode.

---

**See also**

[Overview (S7-1500)](#overview-s7-1500)

### SYNCUP operating mode (S7-1500)

#### Behavior

In the SYNCUP operating mode, the operating system synchronizes the backup CPU with the primary CPU. The primary CPU is in the RUN-Syncup operating mode and controls the process.

In contrast to the primary CPU, the backup CPU does not go through the STARTUP operating mode.

You can find additional information in the section [SYNCUP system status](#syncup-system-status-s7-1500).

---

**See also**

[Overview (S7-1500)](#overview-s7-1500)

### RUN operating modes (S7-1500)

#### RUN operating modes

The primary CPU goes through multiple operating modes on the way to the system status RUN-Redundant:

- RUN
- RUN-Syncup
- RUN-Redundant

The backup CPU only has the RUN-Redundant operating mode.

#### RUN operating mode

In the RUN operating mode, the primary CPU behaves like an S7-1500 standard CPU. It performs the cyclic, time-driven and interrupt-driven program execution on its own.

Addresses in the "Automatic update" process image are automatically updated in each program cycle. You can find additional information in the section "Process image and process image partitions" of the "Redundant system S7-1500R/H" system manual.

Once the CPU has written the outputs and has read the inputs, the cyclic program is executed from the first instruction to the last instruction. Events with higher priority, such as hardware interrupts, diagnostic interrupts and communication, can interrupt the cyclic program flow and prolong the cycle time.

If you have configured a minimum cycle time, the CPU does not terminate the cycle until after this minimum cycle time has expired, even if the user program is completed sooner.

The operating system monitors the runtime time of the cyclic program for a configurable upper limit known as the maximum cycle time. You can restart this time monitoring at any point in your program by calling the RE_TRIGR instruction.

If the cyclic program exceeds the cycle monitoring time, the timeout OB (OB 80) may be started. You can find additional information in the section "Start events" of the "Redundant system S7-1500R/H" system manual.

#### Special features in the RUN operating mode

During non-redundant operation the CPUs are independent of each other. They can have different projects.

#### RUN-Syncup operating mode

In the RUN-Syncup operating mode the backup CPU synchronizes with the primary CPU. The SYNCUP that temporarily has an effect on the primary CPU (for example delay of asynchronous services, cycle time extension through compilation of the load memory contents) runs simultaneously in the backup CPU. You can find additional information in the section "System status SYNCUP" of the "Redundant system S7-1500R/H" system manual.

The operating system synchronizes the work memory contents of the primary CPU consistently at a cycle control point. During synchronization the program cycle in the primary CPU is extended depending on the amount of data to be synchronized and in addition to the other cycle time of the application.

#### RUN-Redundant operating mode

Both CPUs operate the user program synchronously in RUN-Redundant operating mode.

In RUN-Redundant operating mode it is not possible to load objects (e.g. blocks); neither a "Download to device" nor an "Upload from device" is possible. Furthermore, working with snapshots for tags of a data block is not possible in this system state.

---

**See also**

[Overview (S7-1500)](#overview-s7-1500)

### SYNCUP system status (S7-1500)

#### SYNCUP system state

In the SYNCUP system status the operating system synchronizes the user programs in both CPUs for redundant operation. In the SYNCUP system state, the operating system synchronizes the backup CPU with the primary CPU. The backup CPU is in SYNCUP mode; the primary CPU is in RUN-Syncup mode and controls the process. With the SYNCUP system status the redundant system changes from RUN-Solo to the RUN-Redundant system status. Afterwards, both CPUs synchronously process the same user program. In the case of a failure of the primary CPU in redundant operation, the backup CPU takes over control of the process as the new primary CPU at the interruption point.

#### Properties

- An existing online connection between the primary CPU and the PG/PC at the beginning of the system state SYNCUP is terminated during the SYNCUP. The SYNCUP is not automatically re-established after it is terminated.
- If you call the instructions RDREC and WRREC during the SYNCUP system state, the error codes 0x7001 and 0x7002 are always returned. In the case of error as well, no other error code is returned even if, for example, the data record source or the data record target is not available. In this case, the correct error code is only returned after SYNCUP has been terminated.

  If you call the instructions RDREC and WRREC during the SYNCUP system state, no data record job is initiated. The data record job is not initiated until you call the instruction again after the termination of the SYNCUP. It is therefore recommended to always call RDREC and WRREC cyclically.

You can find additional properties and effects of the SYNCUP in the "SYNCUP system state" section of the "SIMATIC S7-1500R/H" system manual.

---

**See also**

[Overview (S7-1500)](#overview-s7-1500)

## Basics of program execution (S7-1500)

This section contains information on the following topics:

- [Programming of S7-1500R/H CPUs (S7-1500)](#programming-of-s7-1500rh-cpus-s7-1500)
- [Organization blocks (S7-1500)](#organization-blocks-s7-1500)

### Programming of S7-1500R/H CPUs (S7-1500)

#### User program for the redundant system S7‑1500R/H

During the design and programming of the user program the same rules apply for the redundant S7‑1500R/H system as for the S7‑1500 automation system.

The user program is stored identically in both CPUs during redundant operation. Both CPUs process the user program event-synchronously.

From the point of view of the user program execution, the redundant S7‑1500R/H system behaves like the S7‑1500 automation system. The synchronization is integrated into the operating system and runs automatically and hidden between the primary and backup CPU.

#### Specific instructions and blocks for the redundant system S7-1500R/H

Specific instructions and OBs are available for the redundant system S7-1500R/H.

Use the instruction "RH_CTRL" to influence the processes for R/H systems. With the firmware version V2.6, you disable the SYNCUP system state or enable SYNCUP system state again. The goal is to only permit the SYNCUP system status in less critical process phases (see the section "Enabling/disabling the SYNCUP system status with the instruction RH_CTRL" in the "Redundant system S7-1500R/H" system manual).

You use the instruction "RH_GetPrimaryID" in the user program to read out which CPU is currently the primary CPU. You can find additional information in the section "Using the instruction 'RH_GetPrimaryID' to detect the primary CPU" in the "Redundant system S7-1500R/H" system manual.

In addition to the OBs of the S7-1500 CPU, you can use OB 72. With OB 72 you handle, for example, redundancy errors.

#### Special features during program execution

- You create the user program for the redundant system S7-1500R/H in the top CPU (e.g. PLC_1) of the STEP 7 project tree.
- The redundant system S7-1500R/H does not support some of the instructions the S7-1500 CPUs. Instructions that are not supported by the S7‑1500R/H redundant system are grayed out in STEP 7 in the "Instructions" task card.  
  STEP 7 shows the instructions that are not supported in the program code in red. If you compile with instructions that are not supported, STEP 7 issues a corresponding error message.  
  The instructions that are not supported are specified in the section "Basics of program execution &gt; Restrictions" in the "Redundant System S7-1500R/H" system manual.
- In the case of instructions with the "LADDR" block parameter, you use this parameter to determine which of the two CPUs is the target of this instruction.  
  Example: To read out the I &amp; M data of the CPU with the redundancy ID 1, enter the hardware identifier 65149 (or system constant "Local1") at the "LADDR" block parameter of the Get_IM_Data instruction.
- Behavior of asynchronous instructions

  - Normally, asynchronous instructions delay the SYNCUP process until their execution is completed.
  - If an asynchronous instruction is started while the SYNCUP process is running, it is put into a waiting state. It remains in this waiting state until the SYNCUP process is completed. When the SYNCUP process is completed, the asynchronous instruction goes into the active state.
- Response of S7-1500R/H redundant system when the maximum cycle time is exceeded, if you have not created any time error interrupt OB

  The first time the maximum cycle time is exceeded in the Run Redundant and SYNCUP system states leads to a loss of redundancy: The primary CPU goes to Run mode and the backup CPU goes to Stop mode.

  The second high-limit violation within the same program cycle causes the primary CPU to go to Stop mode.

  You can find additional information in the "Basics of program execution" section of the S7-1500 R/H system manual.
- Response of S7-1500R/H redundant system when the maximum cycle time is exceeded, if you have created a time error interrupt OB

  When the maximum cycle time is first exceeded in the Run Redundant and SYNCUP system states, the R/H system remains in its system state; the OB80 is called and the cycle time is reset.

  The second time the maximum cycle time is exceeded within the same program cycle leads to redundancy loss: The primary CPU goes to Run mode and the backup CPU goes to Stop mode. OB 80 is called and the cycle time is reset.

  The third time the maximum cycle time is exceeded within the same program cycle causes the primary CPU to go to stop mode.

  You can find additional information in the "Basics of program execution" section of the S7-1500 R/H system manual.

---

**See also**

[Basics of program execution (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#basics-of-program-execution-s7-1500)
  
[Organization blocks (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#organization-blocks-s7-1500)
  
[Organization blocks (S7-1500)](#organization-blocks-s7-1500)

### Organization blocks (S7-1500)

This section contains information on the following topics:

- [IO redundancy error OB (S7-1500)](#io-redundancy-error-ob-s7-1500)
- [CPU redundancy error OB (S7-1500)](#cpu-redundancy-error-ob-s7-1500)

#### IO redundancy error OB (S7-1500)

##### Description

The I/O redundancy error OB (OB 70) is included in the S7-1500-H and S7-1500-HF CPUs as of firmware version V3.0.

The operating system of the CPUs of an S7-1500-H or HF system calls the I/O redundancy error OB (OB 70) if, in system state RUN-Redundant, a loss of redundancy or a return of redundancy occurs in at least one of the following hardware components:

- IO device that is connected to the CPUs via PROFINET system redundancy S2

  In this configuration, the IO device is connected via an interface module. This establishes both a communication relationship (Application Relationship) to an IO controller of the primary CPU and a communication relationship to an IO controller of the backup CPU of the H or HF system.
- IO device that is connected to the CPUs via the PROFINET system redundancy R1

  In this configuration, the IO device is connected via two interface modules. One interface module establishes a communication relationship with an IO controller of the primary CPU, the other interface module establishes a communication relationship with an IO controller of the backup CPU of the H or HF system.

OB 70 is only called in the system state RUN-Redundant. It is not called when the H or HF system leaves the system state RUN-Redundant.

##### Behavior of OB 70 and OB 86 when an IO device returns in the RUN-Redundant system state

In the following, the return of an IO device is understood to mean reaching the state of the IO device in which data can be exchanged.

When an IO device that is connected to the CPUs via PROFINET system redundancy S2 or R1 returns, the rack error OB (OB86) is called (outgoing). If the communication relationships to both IO controllers can be set up on the return, OB 70 is also called (outgoing). If, on the other hand, only the communication relationship to an IO controller can be established, no additional OB is called.

##### Behavior of OB 70 and OB 86 if an IO device fails in the RUN-Redundant system state

In the following, failure of an IO device is understood to mean leaving the state of the IO device in which data can be exchanged.

If an IO device that is connected to the CPUs via PROFINET system redundancy S2 or R1 fails, the rack error OB (OB 86) is called (incoming). If there were two communication relationships to both IO controllers before the failure and these are lost in the event of failure, the I/O redundancy error OB (OB 70) is called (incoming) before OB 86 is called. If, on the other hand, there was only one communication relationship with an IO controller and this is lost, no further OB is called.

##### Priority of OB 70 and OB 86

> **Note**
>
> **Priority of OB 70 and OB 86**
>
> Select the same priority for OB 70 and OB 86. This prevents the OBs from interrupting each other.

##### Behavior of OB 70 after the synchronization process

For each IO device considered here, OB 70 is called after the system status RUN-Redundant has been reached if the IO device improves its redundancy status (for example, by establishing the communication relationship with an IO controller of the backup CPU).

If an IO device considered here can only be reached by the backup CPU (i.e. it was not accessible at all before the synchronization process), OB 86 is called in the system state RUN-Redundant. This indicates the return of the IO device.

##### Structure of the start information

An I/O redundancy error OB has the following start information:

- As for S7-400 CPUs:

  | Tag | Data type | Description |
  | --- | --- | --- |
  | OB70_EV_CLASS | BYTE | Event class and identifiers: - B#16#72: Outgoing event - B#16#73: Incoming event |
  | OB70_FLT_ID | BYTE | Error code (possible value: B#16#A5) |
  | OB70_PRIORITY | BYTE | Priority class |
  | OB70_OB_NUMBR | BYTE | OB number (70) |
  | OB70_RESERVED_1 | WORD | Reserved |
  | OB70_INFO_1 | WORD | Hardware identifier of the affected IO system  Examples: - Local1∼PROFINET_IO system - Local2∼PROFINET_IO system |
  | OB70_INFO_2 | WORD | Hardware identifier of the affected IO device (LADDR) |
  | OB70_INFO_3 | WORD | Geographical address of the affected IO system (using the IO system number of the affected IO system) |
  | OB70_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |
- Optimized start information:

  | Name | Data type | Meaning |
  | --- | --- | --- |
  | LADDR | HW_ANY | Hardware identifier of the affected IO device |
  | Event_Class | BYTE | Identical to the tag OB70_EV_CLASS in the table above |
  | Fault_ID | BYTE | Identical to the tag OB70_FLT_ID in the table above |
  | OB70_INFO_1 | HW_ANY | Hardware identifier of the affected IO system |
  | OB70_INFO_2 | HW_ANY | Hardware identifier of the hardware component via which the affected IO system is connected |

##### Start events of OB 70

| OB70_EV_CLASS or Event_Class | OB70_FLT_ID or Fault_ID | Start event |
| --- | --- | --- |
| B#16#73 | B#16#A5 | Loss of redundancy on the IO device |
| B#16#72 | B#16#A5 | Redundancy restored on the IO device |

---

**See also**

[Events and OBs (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#events-and-obs-s7-1500)

#### CPU redundancy error OB (S7-1500)

##### Description

The operating system of the CPUs of an R/H system calls the CPU redundancy error OB (OB72) in the following cases:

- The R/H system has entered the RUN-Redundant system state (OB72_FLT_ID = B#16#03 or B#16#06).
- The R/H system has left the RUN-Redundant system state (OB72_FLT_ID = B#16#01 or B#16#02).
- In the RUN-Redundant system state the synchronization of both R/H CPUs changes from redundant to non-redundant or vice versa (OB72_FLT_ID = B#16#04 or B#16#05).

##### Structure of the start information

A CPU redundancy error OB has the following start information:

- As for S7-400 CPUs:

  | Tag | Data type | Description |
  | --- | --- | --- |
  | OB72_EV_CLASS | BYTE | Event class and identifiers: - B#16#73: Incoming event |
  | OB72_FLT_ID | BYTE | Error code  Possible values: - B#16#01: Loss of redundancy due to a CPU failure - B#16#02: Loss of redundancy due to a CPU transition to STOP mode (triggered by the user or the system) - B#16#03:   - For configured firmware version up to V2.8: The R/H system has entered the RUN-Redundant system state.   - For configured firmware version as of V2.9: The R/H system has entered RUN-Redundant system state and the synchronization of the two CPUs is running redundantly. - B#16#04 (as of configured firmware version V2.9): The R/H system is still in the RUN-Redundant system state, the synchronization of both CPUs is now no longer running redundantly. - B#16#05 (as of configured firmware version V2.9): The R/H system is still in the RUN-Redundant system state, the synchronization of both CPUs is now running for the first time or again redundantly. - B#16#06 (as of configured firmware version V2.9): The R/H system has entered RUN-Redundant system state and the synchronization of the two CPUs is not running redundantly. |
  | OB72_PRIORITY | BYTE | Priority class |
  | OB72_OB_NUMBER | BYTE | OB number (72) |
  | OB72_RESERVED_1 | WORD | - High byte: B#16#00 - Low byte: Reserved |
  | OB72_INFO_1 | WORD | W#16#0000 |
  | OB72_INFO_2 | WORD | W#16#0000 |
  | OB72_INFO_3 | WORD | W#16#0000 |
  | OB72_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |
- Optimized start information:

  | Name | Data type | Meaning |
  | --- | --- | --- |
  | LADDR | HW_ANY | HW identifier of the defective hardware object  When the RUN-Redundant system state is reached, this is the hardware identifier of the device object of the backup CPU.  When leaving the RUN-Redundant system state this is the hardware identifier of the device object of the CPU that failed or transitioned to STOP operating state: - 65132 ("Local1~Device") for the CPU with the redundancy ID 1 - 65332 ("Local2~Device") for the CPU with the redundancy ID 2 If the synchronization is now redundant for the first time or redundant again or no longer redundant, this is the hardware identifier of the redundant system: - 34 ("Local1~RHSystem") |
  | Event_Class | BYTE | Identical to the tag OB72_EV_CLASS in the table above |
  | Fault_ID | BYTE | Identical to the tag OB72_FLT_ID in the table above |

##### Start events of OB72

| OB72_EV_CLASS or Event_Class | OB72_FLT_ID or Fault_ID | Start event |
| --- | --- | --- |
| B#16#73 | B#16#01 | Loss of redundancy due to a CPU failure |
| B#16#73 | B#16#02 | Loss of redundancy due to a CPU transition to STOP mode |
| B#16#73 | B#16#03 | - For configured firmware version up to V2.8: The R/H system has entered the RUN-Redundant system state. - For configured firmware version as of V2.9: The R/H system has entered RUN-Redundant system state and the synchronization of the two CPUs is running redundantly. |
| B#16#73 | B#16#04 | (As of configured firmware version V2.9):* The R/H system is still in the RUN-Redundant system state, the synchronization of both CPUs is now no longer running redundantly. |
| B#16#73 | B#16#05 | (As of configured firmware version V2.9):* The R/H system is still in the RUN-Redundant system state, the synchronization of both CPUs is now running for the first time or again redundantly. |
| B#16#73 | B#16#06 | (As of configured firmware version V2.9):* The R/H system has entered RUN-Redundant system state and the synchronization of the two CPUs is not running redundantly. |

---

**See also**

[Events and OBs (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#events-and-obs-s7-1500)

## Loading an S7-1500R/H CPU (S7-1500)

This section contains information on the following topics:

- [Downloading project data to the CPUs (S7-1500)](#downloading-project-data-to-the-cpus-s7-1500)
- [Downloading project data to the primary CPU (S7-1500)](#downloading-project-data-to-the-primary-cpu-s7-1500)
- [Starting the primary CPU after a download (S7-1500)](#starting-the-primary-cpu-after-a-download-s7-1500)
- [Downloading project data to the backup CPU (S7-1500)](#downloading-project-data-to-the-backup-cpu-s7-1500)
- [Loading a user program to the primary CPU (S7-1500)](#loading-a-user-program-to-the-primary-cpu-s7-1500)

### Downloading project data to the CPUs (S7-1500)

Project data can be downloaded via an online connection from the PG/PC or HMI device into the CPUs of the S7-1500R/H system. The project data can either be downloaded into the primary CPU or the backup CPU, simultaneous access to both CPUs is not possible.

By default, the project data is downloaded to the primary CPU. In the SYNCUP system state, the project data is then transferred from the primary CPU to the backup CPU.

Project data can also be downloaded to the backup CPU. This makes sense if the backup CPU is to be the primary CPU at a restart.

The complete project data (all configuration data and the complete user program) can only be downloaded to a CPU in STOP operating state.

In the RUN-Solo system status the user program can also be loaded into the primary CPU that is in the RUN state. During downloading, the primary CPU maintains control of the process. There is no standstill of the plant.

---

**See also**

[Downloading project data to the primary CPU (S7-1500)](#downloading-project-data-to-the-primary-cpu-s7-1500)
  
[Starting the primary CPU after a download (S7-1500)](#starting-the-primary-cpu-after-a-download-s7-1500)
  
[Downloading project data to the backup CPU (S7-1500)](#downloading-project-data-to-the-backup-cpu-s7-1500)
  
[Loading a user program to the primary CPU (S7-1500)](#loading-a-user-program-to-the-primary-cpu-s7-1500)

### Downloading project data to the primary CPU (S7-1500)

By default, the project data is downloaded to the primary CPU. To load the complete project data (all configuration data and the complete user program), the CPU must be in the operating state STOP. In the SYNCUP system state, the project data is then transferred from the primary CPU to the backup CPU.

#### Requirements

- The IP addresses have been assigned.
- The primary CPU is in the STOP operating state.

#### Procedure

To download the project data to the primary CPU, follow these steps:

1. Select the S7-1500R/H system in the project navigation.
2. Right-click to call up the shortcut menu.
3. Select the "Download to device &gt; Hardware and software (only changes)" command from the shortcut menu.

   The "Extended download to device" dialog opens.
4. Select the subnet from the "Type of the PG/PC interface" drop-down list.
5. Select the adapter used from the "PG/PC interface" drop-down list:
6. Select the interface to which the PG/PC is connected from the "Connection to interface/subnet" drop-down list.

   Alternatively, select the entry "Try all interfaces".
7. Click the "Start search" button.

   The "Choose target device" table shows the CPUs in the S7-1500R/H system and their roles. As a default the primary CPU is selected.
8. Click "Load".

#### Result

If necessary, the project data is compiled before the download.

The "Results of loading" dialog displays the results of the loading process.

### Starting the primary CPU after a download (S7-1500)

After downloading the project data start the primary CPU.

#### Requirements

- It has been compiled without errors, consistent project data loaded.
- The primary CPU mode selector is in the RUN position.

#### Procedure

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Primary CPU startup with user program with errors**  Before starting the primary CPU ensure that a potentially faulty user program cannot damage property or people and cannot cause dangerous states. |  |

To start the primary CPU after loading, follow these steps:

1. Select the "Start module" entry in the "Action" column in the "Results of the load process" dialog.
2. Click "Finish".

   The primary CPU switches to the RUN operating state.
3. Switch the backup CPU to the RUN operating state.

**Note**

**Role change during loading**

Beware of a possible role change between primary and backup CPU shortly before, during or after loading.

A role change can occur during loading if the primary CPU fails (power failure, hardware defect) or is in the STOP operating state and one of the following conditions occurs:

- You switch the backup CPU to RUN operating state during this time.
- You switch the backup CPU to POWER ON during this time and the startup characteristics were configured in STEP 7 so that the CPU automatically goes into the RUN operating state after the POWER ON.

In the event of a role change, the new primary CPU starts up with the old project data. The new project data in the current backup CPU is overwritten with the old project data during synchronization of the two CPUs for redundant operation.

#### Result

After successful SYNCUP, the S7-1500R/H system switches to redundant mode.

### Downloading project data to the backup CPU (S7-1500)

By default, the project data is downloaded to the primary CPU. You can also download the project data to the backup CPU. This makes sense if the backup CPU is to be primary CPU with its project data upon a restart.

While the project data is downloaded the primary CPU continues to control the process.

After downloading you must switch the primary CPU to the STOP operating state and the backup CPU to the RUN operating state. This means the previous backup CPU becomes the new primary CPU.

> **Note**
>
> **Loading to the backup CPU**
>
> If the project uses retentive data, the backup CPU runs with data which may be outdated.

#### Requirement

The backup CPU is in STOP operating state.

#### Downloading project data to the backup CPU

To download project data to the backup CPU, follow these steps:

1. Right-click to select the S7-1500R/H system in the project navigation.
2. Select "Hardware and software (only changes)" under "Download to backup CPU".

   The backup CPU is now selected instead of the primary CPU in the "Extended download" dialog.
3. Select the subnet from the "Type of the PG/PC interface" drop-down list.
4. Select the adapter used from the "PG/PC interface" drop-down list:
5. Select the interface to which the PG/PC is connected from the "Connection to interface/subnet" drop-down list.
6. Alternatively, select the entry "Try all interfaces".
7. Click the "Start search" button.

   The "Choose target device" table shows the CPUs in the S7-1500R/H system and their roles. By default the backup CPU is selected.
8. Click "Load".

   The "Results of loading" dialog displays the results of the loading process.

#### Switching primary and backup CPU

After downloading the project data into the backup CPUs switch the CPUs so that the backup CPU becomes the new primary CPU. To do this, follow these steps:

1. Switch the primary CPU to the STOP operating state.
2. Switch the backup CPU to the RUN operating state.

   The previous backup CPU becomes the new primary CPU and controls the process on its own in the RUN-Solo system status.

#### Result

The S7-1500R/H system switches back to the RUN-Redundant system status after SYNCUP with the modified user program.

### Loading a user program to the primary CPU (S7-1500)

The user program can be downloaded into a CPU in the operating state RUN. During downloading, the primary CPU maintains control of the process. There is no standstill of the plant.

#### Requirement

The primary CPU is in the RUN operating state.

#### Procedure

Proceed as follows to download a changed user program into the primary CPU:

1. Switch the backup CPU to the STOP operating state.

   The S7-1500R/H system switches from the RUN-Redundant system state to the RUN-Solo system state.
2. Download the modified user program to the primary CPU with "Download to device" &gt; "Software (only changes)".

   The primary CPU continues to control the process.
3. Switch the backup CPU to the RUN operating state.

#### Result

The primary CPU remains in the RUN operating state and synchronizes the modified user program with the backup CPU in SYNCUP.

The S7-1500R/H system switches back to the RUN-Redundant system status with the modified user program.

## Communication with the R/H system (S7-1500)

This section contains information on the following topics:

- [System IP addresses (S7-1500)](#system-ip-addresses-s7-1500)
- [Setting up HMI connection via the system IP address (S7-1500)](#setting-up-hmi-connection-via-the-system-ip-address-s7-1500)
- [Setting up Open User Communication (S7-1500)](#setting-up-open-user-communication-s7-1500)
- [Connection resources of the redundant system S7-1500R/H (S7-1500)](#connection-resources-of-the-redundant-system-s7-1500rh-s7-1500)
- [Behavior of connections during Syncup (S7-1500)](#behavior-of-connections-during-syncup-s7-1500)
- [Behavior of connections at primary-backup switchover (S7-1500)](#behavior-of-connections-at-primary-backup-switchover-s7-1500)
- [OPC UA server support for S7-1500R/H systems (S7-1500)](#opc-ua-server-support-for-s7-1500rh-systems-s7-1500)

### System IP addresses (S7-1500)

For information on the limitations of the R/H system with regard to communication functions, see [Operating principle of the redundant system S7-1500R/H](#operating-principle-of-the-redundant-system-s7-1500rh-s7-1500).

The following explanations describe the possibilities of maintaining the communication to the R/H system, even if, for example, the CPU that is controlling the process fails.

#### System IP addresses of the redundant system S7-1500R/H

In addition to the "normal" IP addresses of the PROFINET interfaces. the redundant system S7-1500R/H also supports **system IP addresses**.

System IP addresses are used to communicate with other devices (for example, HMI devices, CPUs, PG/PC). These devices always communicate over the system IP address with the primary CPU of the redundant system. This ensures, for example, that the communication partner can communicate with the new primary CPU (previously backup CPU) in the RUN-Solo system state after failure of the original primary CPU in redundant operation.

To differentiate between "normal" and "system" IP address, the normal IP address is referred to as "devices IP address" – only in connection with R/H systems.

The following system IP addresses exist:

- System IP address for the PROFINET interfaces X1 of both CPUs (system IP address X1)
- System IP address for the PROFINET interfaces X2 of both CPUs (system IP address X2)

A virtual MAC address belongs to each system IP address.

#### System IP addresses for communications processors

As of STEP 7 V19, you can add CP 1543‑1 communications processors FW version V3.0 or higher to a S7‑1500R/H redundant system FW version V3.1 or higher. When CP 1543‑1 communications processors are added, R/H CPUs support the configuration of a W1 virtual interface with device and system IP addresses. The communication partners connected to the CPs communicate with the R/H CPUs via these IP addresses.

You activate the system IP address of W1 in STEP 7.

A virtual MAC address belongs to each system IP address.

You can find a description of the behavior following a communications processor failure and the configuration of IP addresses of the S7-1500R/H system in the Communication function manual.

#### Advantages of the system IP addresses compared to the device IP addresses

- Communication partners communicate specifically with the primary CPU.
- The communication of the redundant system S7-1500R/H via system IP address continues to work even after the failure of the primary CPU (primary-backup switchover).

#### Applications

Use the system IP addresses for the following locations:

- HMI communication with the redundant system S7‑1500R/H: With a HMI you control and monitor the process on the redundant system S7-1500R/H.
- Open User Communication with the redundant system S7‑1500R/H:

  - Another CPU or an application on the PC is accessing the data of the redundant system S7-1500R/H.
  - The redundant system S7-1500R/H accesses another device.

  TCP, UDP and ISO‑on‑TCP connections are possible.

#### Requirements

- Communication partner is connected to both CPUs, in each case be the same interface (for example, X2).
- The system IP address is enabled.

> **Note**
>
> For an easier IP configuration in the devices, you can use system IP addresses that are in the IP subnet of the interface addresses.

#### Communication via the system IP address X2

If the CPUs of the redundant system S7-1500R/H have two PROFINET interfaces, it is recommended to use PROFINET interface X2 four communication with other devices.

Following figure shows a configuration in which the communication partners are connected via the respective PROFINET interfaces X2 the CPUs of the redundant system S7-1500R/H.

![Communication via the system IP address X2](images/112318098443_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Open User Communication between another CPU and the redundant system S7‑1500R/H |
| ② | HMI communication with the redundant system S7‑1500R/H |
| ③ | Open User Communication between the redundant system S7‑1500R/H and a PC |

#### Communication via the system IP address X1

The following figure shows a configuration in which the communication partners are connected with a switch to the PROFINET ring of the redundant system S7-1500R/H. The PROFINET ring connects the connection partners with the respective PROFINET interfaces X1 of both CPUs.  
Since CPU 1513R only has one PROFINET interface, the connection via the PROFINET ring the only option to connect via the system IP address X1.

![Communication via the system IP address X1](images/112317024395_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Open User Communication between the redundant system S7‑1500R/H and another CPU. |
| ② | HMI communication with the redundant system S7‑1500R/H |
| ③ | Open User Communication between the redundant system S7‑1500R/H and a PC |

#### Communication via the system IP addresses X1 and X2

If the CPUs of the redundant system S7-1500R/H have two PROFINET interfaces (X1 and X2), you can use respective system IP addresses from both PROFINET interfaces. PROFINET devices which are connected with the interfaces X1 of the CPUs, communicate via the system IP address X1. PROFINET devices which are connected with the interfaces X2 of the CPUs, communicate via the system IP address X2.

![Communication via the system IP addresses X1 and X2](images/112318086027_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Open User Communication between the redundant system S7‑1500R/H and another CPU. |
| ② | HMI communication with the redundant system S7‑1500R/H |
| ③ | Open User Communication between the redundant system S7‑1500R/H and a PC |

#### Enabling system IP addresses

If the CPUs of the redundant system S7-1500R/H have two PROFINET interfaces (X1 and X2), you can use a system IP address from both PROFINET interfaces. The section below describes how to enable the system IP address for the interface X1.

To enable the system IP address for your redundant system S7-1500R/H, proceed as follows:

1. In the network view of STEP 7, select the interface X1 of one of the two CPUs.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "Ethernet addresses" in the area "System IP address for switched communication".
3. Select the check box "Enable the system IP address for switched communication".

   STEP 7 automatically creates a system IP address.
4. If necessary, adjust the system IP address.
5. If required, adjust the virtual MAC address. To do this, assign a subnet-wide (Ethernet broadcast domain) unique value (value range 01<sub>H</sub> to FF<sub>H</sub>) for the last byte at "Virtual MAC address".

   > **Note**
   >
   > **Uniqueness of the virtual MAC address**
   >
   > The redundant system S7-1500R/H uses the Virtual Router Redundancy Protocol (VRRP) for the system IP address and associated virtual MAC address.   
   > If you use other devices VRRP, for example switches, make sure that the MAC addresses are unique within an Ethernet broadcast domain.

---

**See also**

[Behavior of connections at primary-backup switchover (S7-1500)](#behavior-of-connections-at-primary-backup-switchover-s7-1500)
  
[Communication function manual](https://support.industry.siemens.com/cs/ww/en/view/59192925)

### Setting up HMI connection via the system IP address (S7-1500)

#### Requirements

- Redundant system S7-1500R/H, for example, CPU 1513R-1PN is positioned in the network view
- System IP address is enabled
- HMI device with PROFINET interface is located in the network view

#### Procedure

To set up a HMI connection to a redundant system S7-1500R/H, follow these steps:

1. In the network view of STEP 7, select a PROFINET interface of the HMI device.
2. Using drag-and-drop operation, drag a line between the PROFINET interface of the HMI device and a PROFINET interface of the redundant system S7‑1500R/H.  
   The HMI device and the redundant system S7‑1500R/H are interconnected.
3. On the toolbar, click the "Connections" icon. This activates connection mode.
4. Using drag-and-drop operation, drag a line between the HMI device and a CPU of the redundant system S7‑1500R/H.  
   The "Connection partners" list opens.
5. Select the redundant system S7-1500R/H from the "Connection Partners" list.

Result: You have set up a HMI connection between the HMI device and the redundant system S7-1500R/H. The HMI connection uses the system IP address.

#### Converting HMI connection to the devices IP address

To convert the HMI connection permanently to the selected CPU, clear the check box "Use system IP address for switched communication" in the properties of the HMI connection. The HMI connection then uses the devices IP address of the PROFINET interface. If this CPU fails, then the HMI connection to this CPU fails permanently.

> **Note**
>
> **Automatic setup of HMI connection**
>
> As soon as you drag-and-drop a tag from the redundant system S7‑1500R/H to a HMI screen or to a HMI tag table, STEP 7 automatically sets up an HMI connection. By default, this HMI connection exists between the PROFINET interface the HMI device and the PROFINET interface X1 of the CPU with redundancy ID 1. Connection users the devices IP address of the PROFINET interface X1.
>
> The properties of the HMI connection you can convert HMI connection to a system IP address.

### Setting up Open User Communication (S7-1500)

The redundant system S7-1500R/H can communicate with other devices via Open User Communication.

- Setup the connections the user program, for example, with the instruction "TSEND_C".

  > **Note**
  >
  > Configured connections do not support the redundant system S7-1500R/H.
- You can set up the connections either via the devices IP addresses or via the system IP addresses of the PROFINET interfaces.

  - When you set up connection via a system IP address, communication is always routed through the primary CPU.  
    Recommendation: Always use the system IP address for Open User Communication.
  - In redundant mode, the redundant system can establish or terminate IP address connections and send or receive data using any device.  
    If you set up the connection via a device IP address, communication runs via the corresponding CPU. If the CPU fails, then the entire communication via the device IP addresses of this CPU fails.

#### Support of communications processors and Secure Open User Communication

S7‑1500R/H systems FW version V3.1 or higher also support Secure Open User Communication (Secure OUC).

If you add CP 1543‑1 communications processors to an S7‑1500R/H system FW version V3.1 or higher, you can also use Secure OCU via these connected CPs.

Requirements:

- STEP 7 V19 or higher
- CP 1543‑1 FW version V3.0 or higher

You can find information about the extended connection options for OUC and how to created a (secure) connection in the [Communication function manual](https://support.industry.siemens.com/cs/ww/en/view/59192925).

#### Usable protocols / connection types

In addition to the TCP protocol explained below as example (set up by means of the connection parameterization for the instructions TSEND_C and TRCV_C), you can also use the ISO-ON-TCP, UDP and Modbus TCP protocols with the corresponding system data types and instructions, see table.

The system data type TCON_Param is not supported.

| Protocol | System data type | instructions |
| --- | --- | --- |
| TCP | - TCON_IP_v4 - TCON_QDN - TCON_IP_v4_SEC* - TCON_QDN_SEC* | Establish connection and send/receive data via:  - TSEND_C/TRCV_C or - TCON, TSEND/TRCV or - TCON, TUSEND/TURCV  (connection can be terminated via TDISCON) |
| ISO-on-TCP | - TCON_IP_RFC |  |
| UDP | - TCON_IP_v4 - TCON_IP_QDN - TADDR_Param - TADDR_SEND_QDN - TADDR_RCV_IP - TCON_QDN_SEC* - TCON_IP_v4_SEC* | Establish connection and send/receive data via:  - TSEND_C/TRCV_C - TUSEND/TURCV/TRCV (connection can be terminated via TDISCON) |
| Modbus TCP | - TCON_IP_v4 - TCON_QDN - TCON_IP_v4_SEC* - TCON_QDN_SEC* | - MB_CLIENT - MB_SERVER |

* The S7‑1500R/H redundant system supports Secure Open User Communication as of FW version V3.1. If you use the system data types TCON_IP_v4_SEC or TCON_QDN_SEC in the S7‑1500R/H redundant system (&lt; FW version V 3.1), their ActivateSecureConn parameter must have the value FALSE. This means that the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.

#### Example: Setting up connection via the system IP address

The following section describes how to set up the connection from the redundant system S7-1500R/H to another CPU via the system IP address.

- In the user program of the redundant system S7-1500R/H, establish the connection with the instruction TSEND_C.
- In the user program of the partners CPU, create a corresponding instruction TRCV_C.

The procedure is described using the example of a TCP connection between the redundant system S7-1500R/H and a CPU 1516-3 PN/DP.

#### Requirements

- Local connection partners: Redundant system S7‑1500R with two CPUs 1513‑1 PN

  System IP address of the PROFINET interface X1 is enabled.
- Remote connection partner: CPU 1516‑3 PN/DP
- PROFINET interfaces X1 of the CPUs 1513R and the PROFINET interface X2 of the CPU 1516‑3 PN/DP are located in the same subnet.

#### Setting up a TCP connection in the redundant system S7-1500R/H (send)

To set up a TCP connection to another CPU, proceed as follows:

1. Create an instruction TSEND_C in the user program.
2. Select the instruction "TSEND_C".
3. In the Inspector window, go to "Properties" &gt; "Configuration" &gt; "Connection parameters".  
   On the left side you see the redundant system S7-1500R/H is local end point of the connection:

   - "Interface:": The interface X1 is preset.
   - "Subnet:": If the interface X1 is assigned to an S7 subnet, in STEP 7 displays the name of the S7 subnet.
   - **The option "Use System IP address" is enabled**.
4. For "Partner", select the CPU 1516‑3 PN/DP as communication partner under "End point:".
5. For "Partner", select the PROFINET interface X2 of the CPU 1516‑3 PN/DP under "Interface:".
6. For "Local", select the setting &lt;new&gt; under "Connection data".

   STEP 7 creates a data block for the connection data in the user program of the redundant system S7-1500R/H.
7. For "Partner", select the setting "TCP" under "Connection type:".

   STEP 7 creates a data block for the connection data in the user program of the other CPU.

#### Setting up a TCP connection in the connection partner CPU 1516 (receive)

Create an instruction TRCV_C in the user program of the CPU 1516‑3PN/DP and configure this suitably ("complementary") for the connection partner.

#### Setting up connection via the device IP address

To set up an OUC connection via a device IP address of one of the two CPUs:

1. Select a suitable PROFINET interface of the redundant system S7-1500R/H.
2. Disable the option "Use address of the H system".

### Connection resources of the redundant system S7-1500R/H (S7-1500)

#### Maximum number of connection resources of the redundant system S7-1500R/H

The redundant S7‑1500R/H system supports a maximum number of connection resources.

The CPU used defines the maximum number of resources for an S7-1500R/H station:

- CPU 1513R: max. 88 connection resources
- CPU 1515R: max. 108 connection resources
- CPU 1517H: max. 160 connection resources

#### Assignment of connection resources

Communication connections occupy connection resources in the redundant system S7-1500R/H.

Each communication connection to the redundant system S7-1500R/H occupies connection resources in the S7-1500R/H station.

Depending on the IP address used, a communication connection also occupies resources in one or both CPUs of the S7‑1500R/H redundant system.

The following table shows in which CPU the communication connection occupies connection resources in dependence on the IP address used.

| Connection via... | Connection resources of the station | Connection resources of CPU with redundancy ID 1 | Connection resources of CPU with redundancy ID 2 |
| --- | --- | --- | --- |
| A system IP address | X | X | X |
| A device IP address of the CPU with redundancy ID 1 | X | X | - |
| A device IP address of the CPU with redundancy ID 2 | X | - | X |

#### Display of the assigned connection resources in STEP 7

Requirement: Online connection to the S7-1500R/H redundant system

You will find the connection resources in the Inspector window in the properties of the CPUs. STEP 7 always indicates the connection resources the selected CPU and the S7-1500R/H station.

![Display of the assigned connection resources in STEP 7](images/112317015947_DV_resource.Stream@PNG-de-DE.png)

### Behavior of connections during Syncup (S7-1500)

#### Behavior of communication connections via the system IP address in SYNCUP system state

- HMI, PG and S7 connections are closed temporarily. For a short period during the SYNCUP is not possible to establish connections to the redundant system S7-1500R/H.
- All existing connections of Open User Communication are terminated:

  - Connections with the CPUs of the redundant system have established as active connection partner re-established after the SYNCUP.
  - The redundant system S7-1500R/H sets up new connection end points the passive connection establishment after the SYNCUP.
- The processing of running instances of the instructions TSEND and TRCV is stopped. The block parameter STATUS returns 80C4<sub>H</sub> (temporary communication error).

### Behavior of connections at primary-backup switchover (S7-1500)

#### Behavior of communication connections via the system IP address during the primary-backup switchover

- Running instances of the instructions TSEND and TRCV are stopped and return the status 80C4<sub>H</sub> (temporary communication error).
- The new primary CPU re-establishes the connections which the redundant system S7-1500R/H had successfully actively established.
- The new primary CPU sets up new connection end points for the passive connection establishment.

---

**See also**

[System IP addresses (S7-1500)](#system-ip-addresses-s7-1500)

### OPC UA server support for S7-1500R/H systems (S7-1500)

#### S7-1500R/H with OPC UA server

S7-1500R/H CPUs firmware version 3.1 or higher have an OPC UA server. You can find all further information on this after the delivery release of this version here: [Product information for S7-1500/ET 200MP, S7-1500R/H documentation](https://support.industry.siemens.com/cs/ww/en/view/68052815).

## Diagnostics of the redundant system S7-1500R/H (S7-1500)

This section contains information on the following topics:

- [Obtaining an overview of the current state of the R/H system (S7-1500)](#obtaining-an-overview-of-the-current-state-of-the-rh-system-s7-1500)
- [Extensions of the online and diagnostics view for the R/H system (S7-1500)](#extensions-of-the-online-and-diagnostics-view-for-the-rh-system-s7-1500)
- [Dependencies of the diagnostics views in the project tree and in the online and diagnostics view (S7-1500)](#dependencies-of-the-diagnostics-views-in-the-project-tree-and-in-the-online-and-diagnostics-view-s7-1500)
- [Extensions of the "Online tools" task card for the R/H system (S7-1500)](#extensions-of-the-online-tools-task-card-for-the-rh-system-s7-1500)
- [Connection diagnostics in the R/H system (S7-1500)](#connection-diagnostics-in-the-rh-system-s7-1500)
- [Comparison functions for an R/H system (S7-1500)](#comparison-functions-for-an-rh-system-s7-1500)
- [Where can you find additional information? (S7-1500)](#where-can-you-find-additional-information-s7-1500)

### Obtaining an overview of the current state of the R/H system (S7-1500)

#### Introduction

You obtain an overview of the current status of the R/H system in the project tree.

The following sections explain how you determine this information from the symbols displayed there:

- The current system status of the R/H system
- The current operating modes of the CPUs of the R/H system
- The current roles of the CPUs of the R/H system
- To which of the two CPUs an online connection currently exists

Information about the system states of the R/H systems as well as the operating modes and roles of the CPUs of an R/H system is available in the "S7-1500 Redundant System S7-1500R/H" system manual.

#### Determining the current system status of the R/H system

The current system status of the R/H system is indicated by the two square overlay icons located on the right-hand side of the R/H system folder icon.

The following table contains the available folder icons and their meaning.

| Folder icon of the R/H system | System status of the R/H system |
| --- | --- |
| ![Determining the current system status of the R/H system](images/109492558091_DV_resource.Stream@PNG-de-DE.png) | STOP |
| ![Determining the current system status of the R/H system](images/109495895947_DV_resource.Stream@PNG-de-DE.png) | RUN-Solo |
| ![Determining the current system status of the R/H system](images/109496275723_DV_resource.Stream@PNG-de-DE.png) | RUN-Redundant |

> **Note**
>
> **Folder icon and CPU roles**
>
> You cannot determine the roles of the individual CPUs from the folder icon for the system states RUN-Solo and RUN-Redundant.

#### Determining the current operating modes of the CPUs of the R/H system

The current operating mode of a CPU of the R/H system is indicated by the overlay icon that is located at the top right in the folder icon of this CPU.

The following table contains the available folder icons and their meaning using the primary CPU as an example.

| Folder symbol of the primary CPU | Primary CPU operating mode |
| --- | --- |
| ![Determining the current operating modes of the CPUs of the R/H system](images/109496591499_DV_resource.Stream@PNG-de-DE.png) | STARTUP |
| ![Determining the current operating modes of the CPUs of the R/H system](images/109496600075_DV_resource.Stream@PNG-de-DE.png) | STOP |
| ![Determining the current operating modes of the CPUs of the R/H system](images/109498541451_DV_resource.Stream@PNG-de-DE.png) | RUN |

> **Note**
>
> **Dependency of the operating mode display of a CPU on the existing online connection**
>
> In the system states STOP and RUN-Solo you can only determine the current operating mode of the respective CPU for which an online connection currently exists.

The CPU to which an online connection does not currently exist does not have an overlay icon in its CPU folder icon at the top right.

The fact that a CPU currently does not have an online connection to the programming device / PC is indicated by the following icon in the second to last column of the CPU row:

| Symbol | Meaning |
| --- | --- |
| ![Determining the current operating modes of the CPUs of the R/H system](images/109498703883_DV_resource.Stream@PNG-de-DE.png) | "Online via partner": The other CPU of the R/H system is connected online to the programming device / PC. |

#### Determining the current roles of the CPUs of the R/H system

The current role of a CPU in the R/H system is indicated by the overlay icon that is located at the bottom right in the folder icon of the CPU. It either consists of the character "P" or the character "B":

- "P" means that the CPU in the R/H system is a primary CPU.
- "B" means that the CPU in the R/H system is a backup CPU.

#### Determining to which CPU an online connection currently exists

- In the system states STOP and RUN-Solo the following icon is displayed in the second to last column of the CPU row for the respective CPU to which no online connection currently exists:

  | Symbol | Meaning |
  | --- | --- |
  | ![Determining to which CPU an online connection currently exists](images/109498703883_DV_resource.Stream@PNG-de-DE.png) | "Online via partner": The other CPU of the R/H system is connected online to the programming device / PC. |

  You therefore know that an online connection to the other CPU exists.
- In the RUN-Redundant system state the "Online via partner" icon is not displayed. It is superfluous because in RUN-Redundant mode each CPU has all the diagnostic information of the other CPU.

### Extensions of the online and diagnostics view for the R/H system (S7-1500)

#### Overview

There are three online and diagnostics views:

- One for the S7-1500R/H system
- One each for the two CPUs of the S7-1500R/H system

#### Online and diagnostics view of the S7-1500R/H system

This online and diagnostics view has been newly introduced for the R/H system.

It consists of the following elements:

- "Online access" group with the "Online access" area
- "Diagnostics" group with the "Diagnostics" area

In "Online access" the following extensions exist compared to the online and diagnostics view of a standard CPU:

- In the case of an existing online connection between the programming device /PC and one of the CPUs, the "Status" also indicates the role of the CPU connected online in the R/H system:

  - "Online (via primary CPU)" means the CPU connected online is the primary CPU
  - "Online (via backup CPU)" means the CPU connected online is the backup CPU
- The "Information" provides general information about the R/H system and information to which CPU an online connection is being established when going online.

In "Diagnostics" you get an overview of the current status of the R/H system. The following are displayed:

- The system state of the R/H system
- The pairing state of the two CPUs
- The operating modes of the primary and backup CPU
- The names of the primary and backup CPU (preset or assigned by you) This way you know which CPU is the primary CPU and which CPU is the backup CPU.

#### Online and diagnostics views of both CPUs of the S7-1500R/H system

First the dependency of the display from the system status is discussed:

- In the RUN-Redundant system state, both the online and diagnostics view of the primary CPU as well the the online and diagnostics view of the backup CPU diagnostics data is displayed. This applies regardless of which CPU has an online connection.
- In all other system states, diagnostics data is only displayed in the online and diagnostics view of the CPU connected online.

The online and diagnostics view of a CPU of the R/H system corresponds almost completely to the display for standard CPUs. The only difference is in the "Online access" group: In case of an existing online connection, the "Status" also indicates the role of the CPU connected online in the R/H system: Primary CPU or backup CPU

### Dependencies of the diagnostics views in the project tree and in the online and diagnostics view (S7-1500)

#### Introduction

The following factors determine which diagnostics are displayed in the project tree and in the online and diagnostics view:

- What is the role of the CPU to which the programming device / PC is connected online? Primary CPU (shortened to "P" in the following table) or backup CPU (shortened to "B" in the following table)?
- What is the system state of the R/H system?

#### Detailed description of the dependencies

When an online connection exists between the programming device / PC and primary CPU, the following applies:

| System state of the R/H system (and operating modes of the CPUs) | Possible diagnostics/diagnostics displays |
| --- | --- |
| STOP (P=STOP, B=STOP) | - Diagnostics of the primary CPU is possible. - Diagnostics of the backup CPU is not possible. - Diagnostics of the distributed I/Os is not possible. |
| RUN-Solo (P=RUN, B=STOP) | - Diagnostics of the primary CPU is possible. - Diagnostics of the backup CPU is not possible. - Diagnostics of the distributed I/Os is possible. |
| RUN-Redundant (P=RUN-Redundant, B=RUN-Redundant) | - Diagnostics of the primary CPU is possible. - Diagnostics of the backup CPU is possible. - Diagnostics of the distributed I/Os is possible. |

If an online connection exists between the programming device / PC and the backup CPU, the following applies:

| System state of the R/H system (and operating modes of the CPUs) | Possible diagnostics/diagnostics displays |
| --- | --- |
| STOP (P=STOP, B=STOP) | - Diagnostics of the primary CPU is not possible. - Diagnostics of the backup CPU is possible. - Diagnostics of the distributed I/Os is not possible. |
| RUN-Solo (P=RUN, B=STOP) | - Diagnostics of the primary CPU is not possible. - Diagnostics of the backup CPU is possible. - Diagnostics of the distributed I/Os is not possible. |
| RUN-Redundant (P=RUN-Redundant, B=RUN-Redundant) | - Diagnostics of the primary CPU is possible. - Diagnostics of the backup CPU is possible. - Diagnostics of the distributed I/Os is possible. |

#### Summary

The dependencies detailed above can be summarized in the following rules:

- In the STOP and RUN-Solo system states only the CPU to which an online connection exists can be diagnosed.
- In the system status RUN-Redundant both CPUs can be diagnosed, regardless to which CPU an online connection exists.
- In the STOP system state the distributed I/Os cannot be diagnosed.
- In the RUN-Solo system state the distributed I/Os can only be diagnosed when an online connection to the primary CPU exists.
- In the RUN-Redundant system status the distributed I/Os can always be diagnosed, regardless to which CPU an online connection exists.

### Extensions of the "Online tools" task card for the R/H system (S7-1500)

#### Overview

The "Online tools" task card shows information of the S7-1500R/H system if an online connection exists to one of the two CPUs.

It consists of the following panes:

- R/H system operator panel
- One CPU operator panel each for both CPUs
- Cycle time
- Memory

#### R/H system operator panel

The "R/H system operator panel" provides an overview of the current state of the R/H system. The following information is displayed:

- The name of the R/H system
- The current states of the LEDs of the primary CPU
- The system state of the R/H system
- The names and operating modes of the primary CPU and backup CPU

If you click the "STOP R/H-System" button, the effect depends on the current system status:

- In the system states RUN Redundant and RUN-Solo, clicking results in a change to the STOP system state.
- In other system states this button is grayed out.

The "RUN R/H system" button is currently grayed out and therefore without a function.

#### CPU operator panel for both CPUs

There is an individual CPU operator panel for each of the two CPUs of the R/H system.

First the operator panel of the CPU with redundancy ID 1 is displayed (corresponds to the top CPU in the project tree), then the operator panel of the CPU with redundancy ID 2 is displayed (corresponds to the bottom CPU in the project tree).

In the operator panel of each CPU the following is displayed:

- The name of the CPU and its role in the R/H system (primary or backup CPU)
- The current states of the LEDs of the CPU
- The position of the mode selector of the CPU

The "RUN" and "STOP" buttons are used to switch the CPU operating mode.

> **Note**
>
> **Switchover of the operating mode**
>
> A switchover of the CPU operating mode using the "RUN" and "STOP" buttons results in the system status changing.

The "MRES" button is used to perform a full memory reset of the CPU.

In contrast to the operator panel of a standard CPU the following extension is available: The role of the CPU in the R/H system (primary or backup CPU) is displayed additionally after the CPU name.

#### Cycle time

The "Cycle time" pane corresponds to the pane of the standard CPUs of the same name. It shows the values of the CPU to which an online connection currently exists.

The extension compared to a standard CPU is solely that the role of the CPU connected online is displayed in square brackets right at the top in the pane behind the "Cycle time": "Primary" or "Backup"

#### Memory

The "Memory" pane corresponds to the pane of standard CPUs of the same name. It shows the values of the CPU to which an online connection currently exists.

The extension compared to a standard CPU is solely that the role of the CPU connected online is displayed in square brackets right at the top in the pane behind the "Memory": "Primary" or "Backup"

### Connection diagnostics in the R/H system (S7-1500)

#### Display of the connection resources of a connection which the system IP address of the R/H system uses

Connections to an R/H system that use its system IP address behave differently than in the case of standard connections to exactly one CPU of the R/H system with regard to the used connection resources: Connections via the system IP address use resources in each of the two CPUs and in the R/H station.

The display of the connection resources ("Diagnostics" &gt; "Connection information" of the Inspector window, "Connection resources" group) behaves accordingly.

For more information, please refer to the "Communication" function manual.

### Comparison functions for an R/H system (S7-1500)

You can perform an offline/offline comparison and a offline/online comparison for this purpose.

The special features when comparing in the connection with R/H systems are described below.

#### Compare offline/offline (software)

With an R/H system you can only use an R/H CPU for the comparison (software) with another CPU.

The execution of the offline/offline comparison is basically no different from the offline/offline comparison with standard CPUs.

Since SW objects are only displayed for the R/H-CPU with the redundancy ID "1" (top CPU in the project tree), you can also only use this CPU for a comparison.

If you drag the icon for the R/H system (both CPUs) from the project tree to the compare editor, STEP 7 automatically selects the CPU with the redundancy ID "1".

An offline/offline comparison (software) of the two R/H CPUs (comparison of primary CPU with backup CPU) is **not** possible.

#### Offline/offline comparison (hardware)

You can perform a hardware comparison between two S7 CPUs.

Examples:

- Comparison of two complete R/H systems:   
  Drag the respective R/H stations to the compare editor to place them there. The hardware structure of both stations including the local modules and distributed I/O devices is compared.
- Comparison of the two CPUs of the same R/H system
- Comparison of first or second CPU of two R/H systems in each case
- Any CPU of an R/H system with any other S7-1500 CPU

For example, you cannot compare an R/H CPU with PC systems (other design).

#### Offline/online comparison

The execution of the offline/online comparison is basically no different from the offline/online comparison with standard CPUs:

As a starting point for this comparison, you can either select the R/H station or one or both CPUs of the R/H station in the project tree and then select the shortcut menu command "Compare &gt; Offline/Online" as usual. STEP 7 compares with the online CPU that has the role "Primary".

There is no separate menu command for the offline/online comparison with the backup CPU. If you want to compare an offline CPU (R/H system) with the backup CPU as the target device, you must first establish an online connection to the backup CPU using the shortcut menu command "Online connection to backup CPU" and then start the offline/online comparison.

**R/H system is offline**

If both R/H CPUs of the system are offline, the comparison of the R/H system with the primary CPU starts.

STEP 7 then establishes a connection to the primary CPU. If no online path has yet been set, the Online Connect dialog opens and suggests the primary CPU as the target device. After acknowledging the dialog ("Connect" button), the compare editor starts and shows the differences between offline and online devices of the primary CPU.

**R/H system is online**

If one of the two R/H CPUs is online, STEP 7 uses the corresponding target device, to which the online connection exists, for the offline/online comparison.

---

**See also**

[Comparing project data](Editing%20project%20data.md#comparing-project-data)

### Where can you find additional information? (S7-1500)

You will find more information on the diagnostics of S7-1500R/H redundant systems in the "Diagnostics" function manual.
