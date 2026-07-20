---
title: "Principle of operation of SIMATIC Drive Controllers"
package: ProgCPU15DCenUS
topics: 30
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Principle of operation of SIMATIC Drive Controllers

This section contains information on the following topics:

- [Functionality of the SIMATIC Drive Controller](#functionality-of-the-simatic-drive-controller)
- [PROFINET, PROFIBUS, PROFIdrive Integrated](#profinet-profibus-profidrive-integrated)
- [Configuring](#configuring)
- [I/O - Properties - X142](#io---properties---x142)

## Functionality of the SIMATIC Drive Controller

### SIMATIC Drive Controller

The SIMATIC Drive Controller is a drive-based controller in the SIMATIC S7-1500 range.

A SIMATIC Drive Controller combines the following functionalities in a SINAMICS S120 Booksize Compact housing:

- Fail-safe SIMATIC S7-1500 technology CPU with integrated technology I/Os
- SINAMICS S120 drive control

The two components are referred to as "CPU" and "SINAMICS Integrated" in this documentation.

The integrated SINAMICS S120 drive control is based on a CU320-2 Control Unit. It can control

- a maximum of 6 servo drives,
- a maximum of 6 drives with vector control, or
- a maximum of 12 drives with U/f control

Fail-safe technology CPUs are available in two performance classes. Safety Integrated on the CPU side and drive side allows use in fail-safe applications.

The SIMATIC Drive Controller supports PROFINET and PROFIBUS DP communication.

### Drive Controller-specific hardware properties

As a component of the SINAMICS S120 drive system, the configuration conditions and rules of SINAMICS S120 apply to the SIMATIC Drive Controller.

### Drive Controller-specific properties of the CPU

The SIMATIC Drive Controller is optimized for automation solutions with motion control in which SINAMICS S120 high-performance converters are used.

With its extensive field bus interfaces, the SIMATIC Drive Controller is ideal for modular machine concepts.

**Service functions**

The SIMATIC Drive Controller does not have an integrated display. You can alternatively run service functions over the integrated Web server, for example.

Using the FUNCT button, you can:

- Save service data on the SIMATIC Memory Card
- Set whether the SIMATIC Memory Card is to work as a program card (PROGRAM) or as a firmware update card (FWUPDATE).

**S7-1500 I/O**

The SIMATIC Drive Controller has no S7-1500 backplane bus. You can connect S7-1500 I/O modules using the ET 200MP distributed I/O system. Note that CM/CP communication modules for PROFINET/PROFIBUS in particular cannot be used in the ET 200MP distributed I/O system. Only communication modules for point-to-point connection (CM PtP) can be used. Alternatively, other I/O systems are available for installation in the control cabinet (e.g. ET 200SP) or for cabinet-free installation (e.g. ET 200pro, ET 200AL and ET 200eco PN).

**Time-based IO**

The function blocks for the use of time-based IO (TIO instructions) are not supported by the digital inputs/outputs of the X142 interface. Recommendation: Use the measuring input, output cam or cam track technology objects for the timer DI/DQ.

Recommendation: Use the measuring input, output cam or cam track technology objects for the timer DI/DQ.

**Device replacement**

The SIMATIC Drive Controller supports replacement of the SIMATIC Drive Controller CPU with the modular SIMATIC S7-1500 CPUs. Replacement with controllers of other designs (e.g. ET 200SP, ET 200pro) is not possible.

### Drive Controller-specific properties of SINAMICS Integrated

The drive control integrated into the SIMATIC Drive Controller only supports a functional subset of the drive functions of SINAMICS S120 CU320-2. For example, free function blocks (FBLOCKS) are not supported by SINAMICS Integrated.

A complete overview of the functional subset compared with the S7-1500 automation system can be found in the SIMATIC Drive Controller System Manual.

**Online functions on SINAMICS Integrated**

SINAMICS Integrated is connected to the CPU over an internal PROFIdrive subnet. Since SINAMICS Integrated is connected to a lower-level network from the point of view of an external PROFINET/PROFIBUS interface, the following aspects must be taken into account:

- Online functions on SINAMICS Integrated are only possible when the SIMATIC Drive Controller (CPU and SINAMICS Integrated) is configured in the TIA Portal and the network configuration has been loaded onto the CPU for the first time.
- SINAMICS Integrated can be configured offline only if Startdrive is installed (no STEP 7 Professional). Online functions are not possible. For this, STEP 7 Professional and Startdrive must be installed.
- A subnet needs to be configured for the interface to which you are connecting the programming device. Routing to the SINAMICS Integrated is only possible with an existing subnet.

Note that SINAMICS Startdrive can only establish an online connection to the SINAMICS Integrated or a SINAMICS S120 CU when the configured firmware version matches the firmware version of the device.

**Device replacement**

Device swapping is not possible, neither between different firmware versions nor with other SINAMICS S120 CUs. Individual drive objects can only be copied and pasted:

- Between SINAMICS Integrated with the same firmware versions
- Between SINAMICS S120 CU320-2 with the same firmware versions
- Between SINAMICS S120 CU310-2 with the same firmware versions

**SINAMICS Drive Control Chart (DCC)**

SINAMICS Drive Control Chart (DCC) extends the functionality of the SINAMICS Integrated with freely available control, calculation and logic blocks. SINAMICS DCC offers you the possibility to configure your own technological functions in the drive system using graphical configuration.

Requirements:

- SINAMICS DCC as of V17 (add-on package for Startdrive)
- CPU firmware version as of V2.9
- SINAMICS Integrated Firmware version as of V5.2 SP3

To define the open-loop and closed-loop control functionality, you select multi-instance-capable drive control blocks (DCB) from a library (DCB library) and graphically link them using drag-and-drop. The DCB libraries are divided into DCB Standard and DCB Extension.

The DCB standard library, which is included in the scope of delivery of SINAMICS DCC, comprises approx. 140 block types for the configuration of logic and technology functions. These can be calculated at different SINAMICS sampling times starting at 1 ms.

Additions to the DCB standard library can be made via DCB Extension libraries. A runtime license is required to use the blocks from DCB Extension libraries. You can find more information on licenses in the SIMATIC Drive Controller System Manual.

> **Note**
>
> Due to the system, the startup, download and RAM to ROM times are longer for the SINAMICS Integrated than for a SINAMICS S120 CU320-2.
>
> Recommendation to minimize these times:
>
> - Reduce the number of DCC charts to a minimum (e.g. use only for different sampling times).
> - Use sub-charts.

**Diagnostics**

To evaluate diagnostic information of the SINAMICS Integrated, you can use, for example, the function block FB LAcycCom_ReadDriveMessagesDateTime (FB 30518) of the LAcycCom library.

With this function block, you can read active messages (alarms, errors and SIMessages) from a drive object (DO) sorted by time (latest first). The information provided comprises the code, info, date and time of occurrence of the message. More information on the LAcycCom library is available [here](https://support.industry.siemens.com/cs/ww/en/view/109479553). The diagnostic information cannot be evaluated over the system diagnostics integrated in the SIMATIC S7-1500.

**Restrictions**

The following functions are not supported by SINAMICS Integrated:

- Upload to an empty project
- Reset via parameter p0972 (parameter does not exist)

  A warm restart (p0009 = 30, p0976 = 2, 3) is possible.
- Transfer of PROFIenergy commands to SINAMICS Integrated

  An energy management system for drives on the SINAMICS Integrated must be implemented using an application.
- Application library "SIMATIC Alarm Handling for SINAMICS Drives", LAlarmHdl_DriveAlarmsIOSystem (autonomous solution)

  The SINAMICS Integrated only supports the FB LAlarmHdl_AddSINADriveAlarms (modular approach).

You can find more information in the SINAMICS S120/S150 List Manual.  
The list of drive parameters indicates which drive objects (function modules) are supported by SINAMICS Integrated (CU_I) or CU320-2 (CU_S120_DP and CU_S120_PN).

## PROFINET, PROFIBUS, PROFIdrive Integrated

Interfaces for PROFINET and PROFIBUS DP communication are integrated in the SIMATIC Drive Controller. The following communication options are available for your automation task:

SIMATIC Drive Controller communication options

| Communication option | PN | DP |
| --- | --- | --- |
| PG communication for commissioning, testing and diagnostics | X | X |
| HMI communication for operator control and monitoring | X | X |
| Open User Communication | X | - |
| Secure Open User Communication | X | - |
| Data exchange via OPC UA as server | X | - |
| Data exchange via OPC UA as client | X | - |
| Direct data exchange between IO controllers | X | - |
| Communication via Modbus TCP | X | - |
| Communication via UDP Multicast | X | - |
| Sending process messages via e-mail | X | - |
| S7 communication | X | X |
| S7 routing | X | X |
| Web server of the CPU  Data exchange via HTTP(S), for example for diagnostics | X | - |
| SNMP (Simple Network Management Protocol) | X | - |
| Time-of-day synchronization | X | X |
| Coupling with the clock pulse system of the technology I/Os X142 and with SINAMICS Integrated | X | - |

Furthermore, the SIMATIC Drive Controller has 2 USB interfaces 3.0 (without function, no connection permitted).

### PROFIdrive Integrated

Communication between CPU and SINAMICS Integrated is based on PROFIdrive mechanisms. The communication services used for this are based on PROFIBUS DP and are processed over an internal, high-performance interface that allows cycle times as low as 250 μs.

## Configuring

This section contains information on the following topics:

- [Configuration of the SIMATIC Drive Controller](#configuration-of-the-simatic-drive-controller)
- [Configuration procedure](#configuration-procedure)
- [Configuration of digital inputs/outputs (X142)](#configuration-of-digital-inputsoutputs-x142)
- [Configuring the digital inputs and digital inputs/outputs (X122/X132)](#configuring-the-digital-inputs-and-digital-inputsoutputs-x122x132)
- [Configuring the clock system](#configuring-the-clock-system)

### Configuration of the SIMATIC Drive Controller

By configuring, parameterizing and connecting the individual hardware components, you communicate the preset configuration and the functionality of the CPU and the integrated SINAMICS Integrated drive unit to the SIMATIC Drive Controller. You perform the steps needed for this in the device and network views in the TIA Portal and in SINAMICS Startdrive (SINAMICS Integrated).

The complete configuration of the SIMATIC Drive Controller is described in the SIMATIC Drive Controller system manual. The following sections focus on the most important steps and the specifics of configuring in the TIA Portal:

[Configuration procedure](#configuration-procedure)

[Configuration of digital inputs/outputs (X142)](#configuration-of-digital-inputsoutputs-x142)

[Configuring the digital inputs and digital inputs/outputs (X122/X132)](#configuring-the-digital-inputs-and-digital-inputsoutputs-x122x132)

[Configuring the clock system](#configuring-the-clock-system)

### Configuration procedure

This section contains information on the following topics:

- [Configuration procedure](#configuration-procedure-1)

#### Configuration procedure

Proceed as follows to create a new project in the TIA Portal and add a SIMATIC Drive Controller:

##### Creating a project

1. Start TIA Portal.
2. Select the action "Start" > "Create new project" in the portal view.
3. Assign a name for the new project under "Project name".
4. Set the storage location with the "..." button.
5. If required, enter comments in the Comment field.
6. Click the "Create" button to create the project.

You have created the project and are currently in the portal view. To continue with the configuration, switch to the project view.

##### Adding a SIMATIC Drive Controller to the project

1. Select "Add new device" in the project tree.
2. In the "Add new device" dialog, select the device version you are using under "Controller" > "SIMATIC Drive Controller" and the firmware version of the device under "Version".
3. You use the "Open device view" checkbox to specify whether the hardware configuration view is to be opened once the device has been created. Keep the checkbox selected if you want to configure the CPU next.
4. Click OK to confirm the new device.

You have added the SIMATIC Drive Controller to the project and can now continue with configuration, parameter assignment and programming.

##### Display of the SIMATIC Drive Controller

When you add a SIMATIC Drive Controller to the project, by default:

- A "Drive Controller_n" group is generated
- Two devices are added to the group, for example:

  - PLC_n [CPU 1504D TF] and
  - Integrated_n [S120, CPU 150xD]

![SIMATIC Drive Controller in the project tree, device collapsed](images/122694866443_DV_resource.Stream@PNG-de-DE.png)

SIMATIC Drive Controller in the project tree, device collapsed

SINAMICS Integrated is only created if the following conditions are met:

- Startdrive is installed
- The option "Create including SINAMICS Integrated (Requirement: Startdrive is installed)" is activated, in the "Options" menu under "Settings" > "Hardware configuration" > "Device-specific settings".

Both devices are networked via the PROFIdrive Integrated_n subnet.

![SIMATIC Drive Controller network view](images/138356580363_DV_resource.Stream@PNG-en-US.png)

SIMATIC Drive Controller network view

When a new SIMATIC Drive Controller is created, all objects are assigned a uniform instance number (n).

CPU PLC_n and integrated automatic speed control Integrated_n are modeled as separate devices. You can also move the devices as required to other groups and delete the "Drive Controller" group. You can also add other devices to the "Drive Controller" group, for example a CU320-2 PN, if you require more than six servo drives.

> **Note**
>
> **Adding SIMATIC Drive Controller directly to group**
>
> You can add the SIMATIC Drive Controller directly to a group folder in the project tree even if the group folder is a subfolder:
>
> 1. Select the required group.
> 2. Go to the menu bar or shortcut menu and select "Add" > "Device".

##### Creation options

The CPU and SINAMICS Integrated are by default created in a shared group folder in the project tree.

To change this behavior, activate or deactivate the relevant options for the SIMATIC Drive Controller in the "Options" menu under "Settings" -> "Hardware configuration" -> "Device-specific settings".

![Creation options for creating a SIMATIC Drive Controller](images/128351040779_DV_resource.Stream@PNG-en-US.png)

Creation options for creating a SIMATIC Drive Controller

The table below sets out the benefits of configuration with or without grouping.

Guide to grouping

| With "Drive Controller" grouping | Without grouping or user-specific grouping |
| --- | --- |
| - Actions apply to all devices in a group, for example    - Go online   - Load to/from device   - Copy - You can add additional devices to the group as required, for example    - with CU320-2   - with I/O system | - Greater flexibility in project structure in the project tree, for example    - by machine/plant modules   - by CPUs and drives, in separate groups |

If you want to create the SIMATIC Drive Controller **without the integrated drive**, deselect the "Including SINAMICS Integrated" option.

Deselecting this option can, for example, be useful in the following cases:

- You are copying a previously configured SINAMICS Integrated drive control from another project.
- The project is to be processed by another user without SINAMICS Startdrive.
- SINAMICS Integrated is not to be configured until later.
- SINAMICS Integrated is not being used, for example, because another drive system is being used.

##### "Drive Controller" group

For the "Drive Controller" group, you have a range of functions to choose from in the menu bar, toolbar and shortcut menu. With "Go online", for example, you can go online with all devices in the group.

The functionality supported by a given device depends on the device and state. For example, the function "Download to device" is supported by the SINAMICS Integrated but not by the CPU when there is an active online connection. The "Load preview" dialog provides relevant information and suggestions for actions for loading.

![Load preview](images/129715580427_DV_resource.Stream@PNG-en-US.png)

Load preview

##### Subsequently configuring SINAMICS Integrated

**Requirements:** STEP 7 Professional and SINAMICS Startdrive are installed.

Proceed as follows if your project only contains the CPU of a SIMATIC Drive Controller and you want to configure the missing SINAMICS Integrated.

1. Select "Add new device" in the project tree.
2. In the "Add new device" dialog, go to "Drives" > "Drives & starters" > "SINAMICS drives" > "SINAMICS S120 Integrated for SIMATIC" and select SINAMICS Integrated, and select the firmware version of the device under "Version".
3. Click OK to confirm.

Result: SINAMICS Integrated has been added to the project tree and can be networked with the CPU.

##### Subsequently configuring a CPU

**Requirements:** STEP 7 Professional and SINAMICS Startdrive are installed.

Proceed as follows if your project only contains a SINAMICS Integrated of a SIMATIC Drive Controller and you want to configure the missing CPU.

1. To ensure that only the CPU (without SINAMICS Integrated) is created, deselect the "Including SINAMICS Integrated" option under "Settings" > "Hardware configuration" > "Device-specific settings" in the "Options" menu. Also deselect the "Create Drive Controller with group folder" option if you do not want a group folder to be created. Alternatively, you will need to delete the components you do not require.
2. Select "Add new device" in the project tree.
3. In the "Add new device" dialog, select the relevant device version under "Controller" > "SIMATIC Drive Controller" and the firmware version of the device under "Version".
4. Click OK to confirm.

Result: The CPU has been added to the project tree and can be connected to the SINAMICS Integrated .

##### Replacing devices in STEP 7

The following section explains how to replace a SIMATIC S7-1500 CPU with a SIMATIC Drive Controller in an existing project or vice versa.

1. Select the device to be replaced in the project tree and right-click to open the shortcut menu.
2. Select the "Replace device..." option
3. Select the module you want to use in the right-hand column. The "Compatibility information" section indicates whether the devices to be replaced are compatible and whether or not and, if so, which configurations will be lost in the process.
4. Click "OK" to confirm.

When replacing devices, remember that the SIMATIC Drive Controller consists of two networked devices – a CPU and a SINAMICS Integrated.

##### Replacing a modular SIMATIC S7-1500 CPU with a SIMATIC Drive Controller (CPU)

If you replace a modular SIMATIC S7-1500 CPU with a SIMATIC Drive Controller, the configurations at the integrated PROFINET interfaces and at the integrated PROFIBUS interface are retained. In other words, the interfaces are mapped to an interface of the same type.

Configurations of the onboard I/O of S7-1500 compact CPUs are not applied. Please also note the compatibility information in the device replacement dialog.

Examples of alarms:

| Message | Explanation   (Difference compared to modular SIMATIC S7-1500 CPUs) |
| --- | --- |
| The 'CPU display' object is not supported in the new configuration and is removed. | Drive Controller has no display |
| The 'Virtual communication interface' object is not supported in the new configuration and is removed. | Drive Controller has no backplane bus, and communications processors (e.g. CP 1543-1) can therefore not be used. The communication interface required for this is removed. |
| 'DI/DQ 8x24VDC' is created | Drive Controller has technology I/Os |
| 'Port' is created | The PROFINET IO IRT interface for the Drive Controller has an additional third port |
| 'PROFIdrive interface' is created | Drive Controller has a SINAMICS Integrated. The communication with the PLC takes place via a 'PROFIdrive interface' |

The centralized I/O in the S7-1500 automation system is moved to the "unplugged modules" area. If required, copy the I/O to a distributed I/O ET 200MP system before device replacement.

A connected SINAMICS S120 CU320-2 remains connected – it is not swapped out for a SINAMICS Integrated. If you require a SINAMICS Integrated, you need to create it manually.

##### Replacing a SIMATIC Drive Controller (CPU) with a modular SIMATIC S7-1500 CPU

For the device replacement, PROFIdrive Integrated is removed and SINAMICS Integrated remains as a non-networked device in the project. You can connect SINAMICS Integrated to a SIMATIC Drive Controller CPU again at a later time.

If you no longer need SINAMICS Integrated, manually delete it from the configuration.

Configurations at interface X142 are not applied.

> **Note**
>
> Device replacement with other CPU classes (for example ET 200SP CPUs or ET 200pro CPUs) is not possible.

##### Replacing SINAMICS Integrated with SINAMICS S120 CU320-2 and vice versa

Device replacement is currently not supported

##### Changing the firmware version of the CPU

You change the firmware version of the SIMATIC Drive Controller CPU by replacing the device. Replace the CPU with a CPU with the preferred firmware version.

##### Changing the firmware version of the SINAMICS Integrated

You can only change the firmware version of the SINAMICS Integrated by deleting and reconfiguring the SINAMICS Integrated (see also paragraph above "Subsequently configuring SINAMICS Integrated ").

For additional information, refer to the following [FAQ on the Internet](https://support.industry.siemens.com/cs/ww/en/view/109782271).

If you want to change the firmware version of connected SINAMICS S120 CUs, you must also start a new configuration with SINAMICS Startdrive .

> **Note**
>
> **Firmware versions must match**
>
> SINAMICS Startdrive can only establish an online connection to SINAMICS Integrated or a SINAMICS S120 CU when the configured firmware version matches the firmware version of the device.
>
> For information on how to determine the firmware version of the device, refer to the section Determining the SINAMICS Integrated version.

### Configuration of digital inputs/outputs (X142)

This section contains information on the following topics:

- [Configuring digital input/outputs](#configuring-digital-inputoutputs)
- [Configuring the DI operating mode](#configuring-the-di-operating-mode)
- [Configuring the DQ operating mode](#configuring-the-dq-operating-mode)
- [Configuring Timer DI operating mode](#configuring-timer-di-operating-mode)
- [Configuring Timer DQ operating mode](#configuring-timer-dq-operating-mode)
- [Configuring Oversampling DI operating mode](#configuring-oversampling-di-operating-mode)
- [Configuring Oversampling DQ operating mode](#configuring-oversampling-dq-operating-mode)
- [Configuring event/period measurement operating mode](#configuring-eventperiod-measurement-operating-mode)
- [Configuring Pulse width modulation (PWM) operating mode](#configuring-pulse-width-modulation-pwm-operating-mode)
- [Assignment of the control interface](#assignment-of-the-control-interface)
- [Assignment of the feedback interface](#assignment-of-the-feedback-interface)
- [Programming example](#programming-example)

#### Configuring digital input/outputs

You configure the required digital input/outputs and operating modes over interface X142.

##### Overview of supported operating modes

You can configure the following operating modes for the individual channels of the X142 interface:

Overview of operating modes

| Operating mode of X142 I/Os  (8 channels) | Functionality | Use with technology objects (TOs) | Use via I/O area (without TO) | Isochronous mode |
| --- | --- | --- | --- | --- |
| DI | Digital input  - Input delay (1 µs/125 µs) - Hardware interrupt (optional)   Hardware interrupt at rising and/or falling edge | - Hardware limit switch for positioning and synchronous axes - Reference mark - ... | No OB restrictions | Optional |
| DQ | Digital output | - Output cam - Cam track - ... | No OB restrictions | Optional |
| Timer DI | Acquisition of the switching time of a digital input signal with up to two edges per application cycle (e.g. for use as measurement sensing input) | Measuring input (OB 91 required) | OB 91/OB 6x  required | Required |
| Timer DQ | Precisely timed output of a digital output signal with up to two edges per application cycle (e.g. for use as an output cam output) | - Output cam (OB 91 required) - Cam track (OB 91 required) | OB 91/OB 6x  required | Required |
| Oversampling DI | Acquisition of 32 states of a digital input signal at equal intervals per application cycle | --- | OB 91/OB 6x  required | Required |
| Oversampling DQ | Output of 32 states of a digital output signal at equal intervals per application cycle | --- | OB 91/OB 6x  required | Required |
| Event/period duration measurement | Measurement of number of edges and period duration (e.g. for simple speed measurement with hole mask and light barrier) | --- | OB 91/OB 6x  required | Required |
| Pulse width modulation PWM | Output of a configurable pulse-pause ratio with a configurable frequency | --- | No OB restrictions | Optional |

##### Procedure

1. Select the Device configuration entry in the project tree under the CPU. The device view opens.
2. In the device view, click the DI/DQ 8x24VDC [X142] interface. You can now edit the configurable properties under Properties in the Inspector window.

Under Channel parameters, you can find an overview of all channels and your selected settings.

![Channel parameters](images/156622432779_DV_resource.Stream@PNG-en-US.png)

Channel parameters

Via links (arrow symbols) you will get to the parameter assignment of the respective channel or to the interconnected technology object.

> **Note**
>
> **Multi-links**
>
> If you have linked a channel to several technology objects, you can select the link of the required technology object via the drop-down list.
>
> You update the drop-down lists via the Refresh button next to "Interconnections". Updating may be required, for example, if changes were made to technology objects elsewhere in the project while the channel configuration was open.

#### Configuring the DI operating mode

##### DI operating mode

1. Select the operating mode DI for the required channel at interface X142.

![DI operating mode](images/142461595019_DV_resource.Stream@PNG-en-US.png)

DI operating mode

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**Input delay**

To suppress faults, you can set an input delay of 1 µs or 125 µs for the input filter of the digital inputs. Changes to the signal are only detected if they are constantly pending for longer than the set input delay time. When an input delay of 1 µs is set, the use of shielded cables is recommended for optimum interference immunity.

**Hardware interrupts**

In the Hardware interrupts section, you can assign a hardware interrupt to a rising and/or falling edge.

**Interconnections**

The technology objects that are interconnected with the channel are listed in the Interconnections area.

If technology objects are interconnected, you can reach the respective technology object through links (arrow icons).

Use the corresponding button to update the selection list. Updating may be required, for example, if changes have been made to technology objects elsewhere in the project while the channel configuration is open.

##### Further information

You can find more information on the DI operating mode in [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Configuring the DQ operating mode

##### DQ operating mode

1. Select the DQ operating mode for the required channel at interface X142.

![DQ operating mode](images/142461598731_DV_resource.Stream@PNG-en-US.png)

DQ operating mode

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**High-speed output (0.4 A)**

If you select the high-speed output option, the digital output is switched alternately to 24 V DC and ground. Allows for extremely steep edges (output delay in the 1 μs range).

The rated load is reduced from 0.5 A to 0.4 A with this operating mode.

**Interconnections**

The technology objects that are interconnected with the channel are listed in the Interconnections area.

If technology objects are interconnected, you can reach the respective technology object through links (arrow icons).

Use the corresponding button to update the selection list. Updating may be required, for example, if changes have been made to technology objects elsewhere in the project while the channel configuration is open.

##### Further information

You can find more information on the DQ operating mode in [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Configuring Timer DI operating mode

##### Timer DI

Timer DI operating mode allows you to acquire the switching time of up to two edges per application cycle (for example OB 91, OB 6x), for example for use as a measuring output.

- Select the Timer DI operating mode for the required channel.

![Operating mode: Timer DI](images/142470703243_DV_resource.Stream@PNG-en-US.png)

Operating mode: Timer DI

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**Input delay**

To suppress faults, you can set an input delay of 1 µs or 125 µs for the input filter of the digital inputs. Changes to the signal are only detected if they are constantly pending for longer than the set input delay time.

To allow signals pending very briefly to be detected with timer DI (for example level of 100 µs), set an input delay of 1 µs.

When an input delay of 1 µs is set, the use of shielded cables is recommended for optimum interference immunity.

**Interconnections**

The technology objects that are interconnected with the channel are listed in the Interconnections area.

If technology objects are interconnected, you can reach the respective technology object through links (arrow icons).

Use the corresponding button to update the selection list. Updating may be required, for example, if changes have been made to technology objects elsewhere in the project while the channel configuration is open.

##### Assigning the measuring input technology object

The measuring input technology object must always be assigned to another technology object whose position is evaluated by the measuring input.

You can assign the measuring input technology object to the following technology objects:

- Synchronous axis
- Positioning axis
- External encoder

You can assign the measuring input technology object precisely one axis or one external encoder.

You can assign multiple measuring input technology objects to one axis or one external encoder.

##### Configuring the measuring input technology object

- Select the configuration of the measuring input in the Technology objects folder in the project tree.
- Configure the basic properties of the technology object in the Basic parameters configuration window.

![Basic parameters](images/128369688715_DV_resource.Stream@PNG-en-US.png)

Basic parameters

**Name**

- Define the name of the measuring input in this field. The technology object is listed under this name in the project tree. The tags of the measuring input can be used in the user program under this name.

**Assigned axis or external encoder**

STEP 7 displays the axis or external encoder assigned to the measuring input. You can use the link to directly access the basic parameters of the higher-level technology object.

**Unit of measurement**

The unit of measure shown for the position of the measuring input corresponds to the unit of measure of the higher-level technology object.

**Hardware interface**

- In the Hardware interface configuration window, assign the Timer DI measuring input type and the selected channel to the technology object.

![Hardware interface](images/128370495755_DV_resource.Stream@PNG-en-US.png)

Hardware interface

**Measuring input type: Measuring using Timer DI**

- Select a measurement input for a measurement using a Timer DI. The selection box displays all channels that have been configured correctly.

> **Note**
>
> **Extending the configuration limits**
>
> A maximum of eight timer DI can be configured at the X142 interface. If the timer DI at X142 are not sufficient for your needs, you can configure a further eight measuring inputs at interface X122/X132. You can also extend the configuration limits using time-based I/O modules:
>
> - ET 200SP distributed I/O system: [TM Timer DIDQ 10x24V](https://support.industry.siemens.com/cs/ww/en/view/95153951)
> - ET 200MP distributed I/O system: [TM Timer DIDQ 16x24V](https://support.industry.siemens.com/cs/ww/en/view/95153313)

> **Note**
>
> **Unsupported instructions for X142**
>
> The function blocks for the use of time-based IO (TIO instructions) are not supported by the X142 interface.
>
> Recommendation: Use the measuring input technology object for timer DI.

**Adjustment for measuring range activation time**

- To adjust the activation time defined in the system, enter an additional activation time in the Extended parameters configuration window.

##### Lost Edge Counter (LEC)

Timer DI support Lost Edge Counter. If more than two edges to be detected occur within one position control cycle, a measured value cannot be evaluated for the other edges to be detected. The LEC records the number of edges lost.

Which lost edges are recorded in the LEC depends on the mode set in the Motion Control instruction. For example, if you only want to measure rising edges, the LEC only records the rising edges not measured. The LEC can count and display a maximum of seven lost edges. The number of lost edges is displayed in the function block and in the technology data block.

##### Further information

You can find additional information on the following topics in the [S7-1500T Motion Control function manuals](https://support.industry.siemens.com/cs/ww/en/view/109751049):

- Measuring input type: Timer DI
- Measuring input type: SINAMICS (central measuring input)
- Measuring input type: PROFIdrive telegram (drive or external encoder)
- Lost Edge Counter (LEC)

#### Configuring Timer DQ operating mode

##### Timer DQ

Timer DQ operating mode allows you to output up to two edges per application cycle (for example OB 91, OB 6x) at a specific time, for example, for use as a cam output.

1. Select the Timer DQ operating mode for the required channel.

![Mode of operation: Timer DQ](images/142470706955_DV_resource.Stream@PNG-en-US.png)

Mode of operation: Timer DQ

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**High-speed output (0.4 A)**

If you select the high-speed output option, the digital output is switched alternately to 24 V DC and ground.

Advantages of the high-speed output:

- Extremely steep edges (output delay in the 1 μs range)
- Extremely high switching frequencies
- Maximum switching precision, for example, for use as a cam output

The rated load is reduced from 0.5 A to 0.4 A with this operating mode.

**Interconnections**

The technology objects that are interconnected with the channel are listed in the Interconnections area.

If technology objects are interconnected, you can reach the respective technology object through links (arrow icons).

Use the corresponding button to update the selection list. Updating may be required, for example, if changes have been made to technology objects elsewhere in the project while the channel configuration is open.

##### Assigning the output cam technology object

The output cam technology object must always be assigned to another technology object whose position is evaluated.

You can assign the output cam technology object to the following technology objects:

- Synchronous axis
- Positioning axis
- External encoder

You can assign exactly one axis or one external encoder to the output cam.

You can assign multiple output cams to one axis or one external encoder.

##### Configuring the output cam technology object

1. Select the configuration of the output cam in the Technology objects folder in the project tree.
2. Configure the basic properties of the technology object in the Basic parameters configuration window.

![Basic parameters](images/128371993611_DV_resource.Stream@PNG-en-US.png)

Basic parameters

**Name**

1. Define the name of the output cam in this field. The technology object is listed under this name in the project tree. The tags of the output cam can be used in the user program under this name.

**Assigned axis or external encoder**

STEP 7 displays the axis or external encoder assigned to the output cam. You can use the link to directly access the basic parameters of the higher-level technology object.

**Output cam type**

1. Select an output cam type on the basis of the required switching behavior:

- Position-based cam (position-dependent switch-on/switch-off)
- Time-based cam (position-dependent switch-on and position-independent or time-dependent switch-off)

**Output cam reference**

1. In this selection, configure whether the switching points of the output cams are to reference the actual position or the position setpoint.

**Unit of measurement**

The unit of measurement shown for the position of the output cam corresponds to the unit of measurement of the higher-level technology object.

When a time-based cam is selected as the output cam type, the unit of measurement for the switch-on duration and other times is also indicated. The unit of measurement for output cams is always ms.

**Hardware interface**

Select the type of cam output in the Hardware interface configuration window.

![Hardware interface](images/128374528651_DV_resource.Stream@PNG-en-US.png)

Hardware interface

1. Select whether you want to output the switching signals generated at the digital output.

- Activate output

  Select one of the following two output options for outputting the cam track:

  - Output via Timer DQ

    For output by Timer DQ, select a cam output in the Output field. The selection box displays all channels that have been configured correctly.

    > **Note**
    >
    > **Extending the configuration limits**
    >
    > A maximum of eight timer DQ can be configured at the X142 interface. If the Timer DQ at X142 are not sufficient for your needs, you can increase the configuration limits with time-based IO modules:
    >
    > - ET 200SP distributed I/O system: [TM Timer DIDQ 10x24V](https://support.industry.siemens.com/cs/ww/en/view/95153951)
    > - ET 200MP distributed I/O system: [TM Timer DIDQ 16x24V](https://support.industry.siemens.com/cs/ww/en/view/95153313)

    > **Note**
    >
    > **Unsupported instructions for the X142 interface**
    >
    > The function blocks for the use of time-based IO (TIO instructions) are not supported by the X142 interface.
    >
    > Recommendation: For the timer DQ, use the output cam or cam track technology object.
  - Output by digital output module

    For output by a digital output module, select a digital output in the Output field. Only the digital outputs with previously defined PLC tags are displayed for selection.

    > **Note**
    >
    > **Output via the X122, X132 or X142 interface**
    >
    > Also use the "Output by digital output module" setting in the following cases:
    >
    > - The output occurs at the X142 interface by a DQ instead of a Timer DQ.
    > - The output occurs by a digital output of the X122 or X132 interface (configured telegram 39x required)
    >
    > In both cases you must define a PLC tag for the respective I/O address.

  You can assign several output cam technology objects to an output, linking the cam signal with a logical AND or logical OR at the output.
- Output deactivated  
  When output is deactivated, the cam track is evaluated only in the software.

**Extended parameters > Activation time**

![Activation time](images/128375412491_DV_resource.Stream@PNG-en-US.png)

Activation time

The specified output cam type is indicated at the top of the Activation time configuration window.

1. For a time shift of the switch-on and switch-off times of the output cams, enter an activation time and a deactivation time.

**Extended parameters Parameter > Hysteresis**

![Hysteresis](images/128377411339_DV_resource.Stream@PNG-en-US.png)

Hysteresis

1. To prevent unwanted changes in the switching state of the output cams of a cam track, enter a hysteresis value.

When using output cams that reference the actual position, it is advisable to enter a hysteresis value (> 0.0).

##### Cam track technology object

In addition to the output cam technology object already described, the cam track technology object is also available.

You can find a detailed description of how to configure the cam track technology object in the [S7-1500T Motion Control function manuals](https://support.industry.siemens.com/cs/ww/en/view/109751049).

#### Configuring Oversampling DI operating mode

##### Oversampling DI

The Oversampling DI function detects 32 signal states of a given digital input at equal intervals per application cycle (for example OB 91, OB 6x). The 32 states are returned together as a 32-bit value in the feedback interface. The value is read in synchronously to Ti (actual value acquisition).

> **Note**
>
> **Isochronous mode**
>
> Oversampling requires isochronous mode.

The figure below shows an example of Oversampling DI4:

![Oversampling DI](images/121036447371_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| T<sub>APP</sub> | Application cycle |
| MSB | Most significant bit |
| LSB | Least significant bit |

Oversampling DI

##### Configuring Oversampling DI

1. Select the Oversampling DI operating mode for the required channel.

![Oversampling DI](images/128385347723_DV_resource.Stream@PNG-en-US.png)

Oversampling DI

> **Note**
>
> **Extending the configuration limits**
>
> A maximum of eight oversampling DI can be configured at the X142 interface. If the Oversampling DI at X142 are not sufficient for your needs, you can increase the configuration limits with time-based IO modules, for example:
>
> - ET 200SP distributed I/O system: [TM Timer DIDQ 10x24V](https://support.industry.siemens.com/cs/ww/en/view/95153951)
> - ET 200MP distributed I/O system: [TM Timer DIDQ 16x24V](https://support.industry.siemens.com/cs/ww/en/view/95153313)

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**Input delay**

To suppress faults, you can set an input delay of 1 µs or 125 µs for the input filter of the digital inputs. Changes to the signal are only detected if they are constantly pending for longer than the set input delay time.

To allow signals pending very briefly to be detected by oversampling DI (for example level of 100 µs), set an input delay of 1 µs.

When an input delay of 1 µs is set, the use of shielded cables is recommended for optimum interference immunity.

##### Further information

You can find more information on the Oversampling DI operating mode in [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Configuring Oversampling DQ operating mode

##### Oversampling DQ

The Oversampling DQ function outputs 32 signal states at equal intervals per application cycle (for example OB 91, OB 6x). Up to 32 edges are therefore possible per application cycle at a given digital output. The 32 states are set over the control interface. The output occurs synchronously with time T<sub>O</sub> (setpoint transfer).

> **Note**
>
> **Isochronous mode**
>
> Oversampling requires isochronous mode.

The image below is an example of oversampling of DQ5:

![Oversampling DQ](images/120989302667_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| T<sub>APP</sub> | Application cycle |
| MSB | Most significant bit |
| LSB | Least significant bit |

Oversampling DQ

> **Note**
>
> **Output frequency with the Oversampling function**
>
> The combination of application cycle and the 32-bit string output must not result in an output frequency that exceeds the maximum switching frequency for the digital outputs.

##### Configuring an oversampling DQ

1. Select the operating mode Oversampling DQ for the required channel.

![Oversampling DQ](images/142470710667_DV_resource.Stream@PNG-en-US.png)

Oversampling DQ

> **Note**
>
> **Extending the configuration limits**
>
> A maximum of eight oversampling DQ can be configured at the inputs/outputs of the X142 interface. If the oversampling DQ at X142 are not sufficient for your needs, you can increase the configuration limits with time-based IO modules, for example:
>
> - ET 200SP distributed I/O system: [TM Timer DIDQ 10x24V](https://support.industry.siemens.com/cs/ww/en/view/95153951)
> - ET 200MP distributed I/O system: [TM Timer DIDQ 16x24V](https://support.industry.siemens.com/cs/ww/en/view/95153313)

**Inversion**

You can invert the 24 V signal to adjust it to the process. By default, the signal is not inverted.

**High-speed output (0.4 A)**

If you select the high-speed output option, the digital output is switched alternately to 24 V DC and ground. Allows for extremely steep edges (output delay in the 1 μs range).

To allow signals pending very briefly to be output by oversampling DQ (for example level of 0.1 ms), you must operate the output as a high-speed output.

The rated load is reduced from 0.5 A to 0.4 A with this operating mode.

##### Further information

You can find more information on the Oversampling DQ operating mode in [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Configuring event/period measurement operating mode

##### Event/period duration measurement

In isochronous mode, you can use the event/period duration measurement operating mode to acquire the number of rising edges at the digital input and at the same time determine the period duration.

> **Note**
>
> **Isochronous mode**
>
> The event/period duration measurement requires isochronous mode.

##### Event counter

With the event measurement, you count the number of rising edges at the digital input. The current count (16-bit value) is updated on the feedback interface with each application cycle (e.g. servo clock).

- The event counter is a rotary counter.
- An event counter overflow is not displayed.
- To determine the number of rising edges per application cycle, the difference between the current count and the previous count must be calculated by the application, taking into account any overflow.

##### Period duration measurement

Two methods are available for the period duration measurement.

- "Single period" measurement method

  The period duration is determined based on the last period in a measuring cycle. This method provides the most current value.

  ![Period duration measurement](images/156677628427_DV_resource.Stream@PNG-de-DE.png)
- "Multiple periods" measurement method

  The period duration is determined based on all periods in a measuring cycle, whereby the measuring cycle length corresponds to one application cycle (e.g. servo clock). This method provides a more accurate measurement for short periods.

  ![Period duration measurement](images/156677637003_DV_resource.Stream@PNG-de-DE.png)

**"Single period" measurement method**

With this measurement method, you determine the period duration by counting the number of 41.67 ns increments between the last two incoming rising edges in the measuring cycle. The current count (32-bit value) is updated on the feedback interface with each application cycle (e.g. servo clock).

Period duration = 41.67 ns • N<sub>INC</sub>

N<sub>INC</sub>: Number of increments of 41.67 ns each (41.67 ns = 1/24 MHz)

> **Note**
>
> Always use the exact (not rounded) value for your calculations.

Since the last two incoming rising edges in the measuring cycle are used for the measurement, the "Single period" measurement method provides the most current value.

**"Multiple periods" measurement method**

Requirement:

- CPU firmware version V3.0 or higher
- Hardware function version FS 11 or higher

In this measurement method, the period duration is determined based on all periods in a measuring cycle, whereby the measuring cycle length corresponds to one application cycle (e.g. servo clock).  
The number of 41.67 ns increments between the last rising edge of the last measuring cycle and the last rising edge of the current measuring cycle is counted.  
The current count (32-bit value) is updated on the feedback interface with each application cycle (e.g. servo clock).

- The event counter and the period duration counter are circular counters.
- A counter overflow is not displayed.
- To determine the count, the difference between the current count and the previous count must be calculated by the application, taking into account any overflow.

![Period duration measurement](images/156693927307_DV_resource.Stream@PNG-de-DE.png)

N<sub>P(new)</sub>: Period duration counter, current (new) count

N<sub>P(old)</sub>:  Period duration counter, previous (old) count

N<sub>E(new)</sub>: Event counter, current (new) count

N<sub>E(old)</sub>:   Event counter, previous (old) count

If current count < old count is true for the counters, then an overflow has occurred. In this case, the value 2<sup>16</sup> must be added to the new count for the event counter, and the value 2<sup>32</sup> must be added to the new count for the period duration counter. A maximum of one overflow is possible.

The "Multiple periods" measurement method yields a more accurate measurement.

- For short periods (i.e. a few 41.67 ns increments per period), in particular, the sampling jitter (1 increment) has less effect because the period duration is determined over many periods.
- Measured value fluctuations are averaged. For example, if rotational speeds are acquired using a slotted disk and fork light barrier, the tolerances of individual slots have less of an effect because the measurement is not based on a single period (of an individual slot).

##### Example 1: "Single period" measurement method

For an injection molding machine, the rotational speed of the extruder screw is to be determined using a simple encoder based on a rotating slotted disk.

The pulses are to be acquired on the SIMATIC Drive Controller using a digital input/output (X142) in the event/period duration measurement operating mode.

The rotational speed of the screw is determined from the time interval between 2 pulses.

![Simple encoder on a shaft, single period measurement method](images/156750226955_DV_resource.Stream@PNG-en-US.png)

Simple encoder on a shaft, single period measurement method

In the "Single period" measurement method, the period duration is determined by counting the number of 41.67 ns increments between the last two incoming rising edges in the measuring cycle. The number of rising edges is additionally counted (circular counter).

Period duration t<sub>P</sub> = 41.67 ns • N<sub>Inc</sub>

If you know the number of pulses that the encoder generates per revolution of the extruder screw, you can calculate the speed at which the extruder screw turns.

**Calculation example**

NS = 16 pulses are generated per revolution of the extruder screw (NS is also referred to as the pulse-per-revolution count of the encoder).

The distance between 2 pulses is N<sub>Inc</sub> = 500,000 counted 41.67 ns increments.   
Thus, the rotational speed of the extruder screw is calculated as follows:

Period duration t<sub>P</sub> = 41.67 ns • N<sub>Inc</sub>

![Example 1: "Single period" measurement method](images/156751327755_DV_resource.Stream@PNG-de-DE.png)

The period duration counter provides a 32-bit count value. As a result, values up to FFFFFFFF (232 = 4,294,967,296 decimal) can be represented. For a time base of 41.67 ns for NS = 1, this yields the minimum measurable speed:

![Example 1: "Single period" measurement method](images/156751336331_DV_resource.Stream@PNG-en-US.png)

The maximum measurable speed for encoders with passive deactivation (encoder output is open in inactive state) is the result of the maximum frequency of the input signals at the counter inputs of 32 kHz.

![Example 1: "Single period" measurement method](images/156752048907_DV_resource.Stream@PNG-en-US.png)

If the encoder generates 1 pulse per revolution (NS = 1), this yields a maximum speed of 1,920,000 rpm.

If you use encoders that generate multiple pulses per revolution, you must reconsider the limit frequencies.

The table below shows a few examples.

Limits for various pulse-per-revolution counts NS with a time base of 41.67 ns. (Encoder with  
passive deactivation)

| **N** | **Lower limit** | **Upper limit** |
| --- | --- | --- |
| 1 | 0.3352 rpm | 1,920,000 rpm |
| 4 | 0.0838 rpm | 960,000 rpm |
| 8 | 0.0419 rpm | 480,000 rpm |
| 16 | 0.0209 rpm | 120,000 rpm |

##### Example 2: "Multiple periods" measurement method

For a winding head of a textile machine, the spindle speed is to be determined using a simple encoder based on a rotating slotted disk.

The pulses are to be acquired on the SIMATIC Drive Controller using a digital input/output (X142) in the event/period duration measurement operating mode.

Due to the accuracy requirements and the high speed, the spindle speed is determined over multiple periods.

![Simple encoder on a shaft, multiple periods measurement method](images/156752646283_DV_resource.Stream@PNG-en-US.png)

Simple encoder on a shaft, multiple periods measurement method

In the "Multiple periods" measurement method, the period duration is determined by counting the number of 41.67 ns increments between the last rising edge of the last measuring cycle and the last rising edge of the current measuring cycle with the period duration counter NP.   
In addition, the number of rising edges NE for the same time period is determined.   
The period duration is calculated based on the count values, taking into account counter overflows, as follows:

![Example 2: "Multiple periods" measurement method](images/156752654859_DV_resource.Stream@PNG-en-US.png)

If you know the number of pulses that the encoder generates per spindle revolution, you can calculate the speed at which the spindle turns.

**Calculation example**

NS = 48 pulses are generated per revolution of the spindle (NS is also referred to as the pulse-per-revolution count of the encoder).

![Example 2: "Multiple periods" measurement method](images/156756580235_DV_resource.Stream@PNG-en-US.png)

Thus, the rotational speed of the spindle is calculated as follows:

![Example 2: "Multiple periods" measurement method](images/156757241611_DV_resource.Stream@PNG-de-DE.png)

##### Configuring event/period duration measurement

1. Select the required channel for the Event/period duration measurement operating mode.

![Event/period duration measurement](images/156803769099_DV_resource.Stream@PNG-en-US.png)

Event/period duration measurement

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**Input delay**

To suppress faults, you can set an input delay of 1 µs or 125 µs for the input filter of the digital inputs. Changes to the signal are only detected if they are constantly pending for longer than the set input delay time.

To allow signals pending very briefly to be detected at high counting frequencies, you need to set an input delay of 1 µs.

When an input delay of 1 µs is set, the use of shielded cables is recommended for optimum interference immunity.

**Measurement method**

Depending on the selected measurement method, the period duration is determined based on the "last period" or "all periods" in a measuring cycle.

> **Note**
>
> **"Multiple periods" measurement method when using unsupported hardware**
>
> If a SIMATIC Drive Controller does not meet the hardware function version (FS 11 or higher) requirement, the CPU remains in startup inhibit state.

##### Additional information

You can find more information on the Event/period duration measurement operating mode in [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Configuring Pulse width modulation (PWM) operating mode

##### Areas of application

You can use pulse width modulation (PWM) to generate periodic pulses with a constant rated voltage and a variable pulse duration.

Possible applications for pulse width modulation (PWM):

- Control of proportional valves and directional valves

  - Energy savings as a result of a reduction in holding current or for controlling the valve position
- Heating control, for example, via an external additional power unit

##### Principle of operation

With pulse width modulation, a signal with defined time period and variable pulse duration is output at the digital output. You use pulse width modulation to vary the mean value of the output voltage. This allows you to control the load current or the power in line with the connected load. The pulse duration can be between 0 (no pulse, always off) and full-scale deflection (no pulse, always on).

![Principle of operation](images/121333679243_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Period |
| ② | Pulse duration |

Pulse width modulation (PWM) is based on the specification of a base frequency of 1, 2, 4, 8 or 16 kHz. You can alter the base frequency in terms of period and pulse-pause ratio over the control interface (32-bit value). The bit pattern is shown in each base period. The base period is defined on the basis of the base frequency. A "0" is LOW and a "1" is HIGH.

##### Examples

**Base frequency: 1 kHz → Base period: 1 ms**

1111 0000 0000 0000 1111 0000 0000 0000

Time period: 500 µs; 375 µs LOW; 125 µs HIGH

![Pulse width modulation](images/123102496395_DV_resource.Stream@PNG-en-US.png)

Pulse width modulation

**Base frequency: 1 kHz**

1111 1111 1111 1111 0000 0000 0000 0000

Time period: 1 ms; 500 µs LOW; 500 µs HIGH

1111 1111 0000 0000 0000 0000 0000 0000

Time period: 1 ms; 750 µs LOW; 250 µs HIGH

1111 0000 1111 0000 1111 0000 1111 0000

Time period: 250 µs; 125 µs LOW; 125 µs HIGH

**Base frequency: 2 kHz**

1010 1010 1010 1010 1010 1010 1010 1010

Time period: 31.25 µs; 15.625 µs LOW; 15.625 µs HIGH

##### Configuring Pulse width modulation PWM

To configure PWM operating mode, first define the required base frequency of pulse width modulation. You can configure the base frequency as 1, 2, 4, 8 or 16 kHz. The selected base frequency then applies to all channels of interface X142.

![Base frequency of pulse width modulation](images/128388763531_DV_resource.Stream@PNG-en-US.png)

Base frequency of pulse width modulation

Now select the channels for PWM operating mode. If you want to configure very short pulses, enable the high-speed output function.

![Pulse width modulation channel](images/142470931979_DV_resource.Stream@PNG-en-US.png)

Pulse width modulation channel

The selected digital output is switched with the selected base frequency and the switching pattern from the control interface.

**Inversion**

You can invert the 24 V signal to adjust it to your process. By default, the signal is not inverted.

**High-speed output (0.4 A)**

If you select the high-speed output option, the digital output is switched alternately to 24 V DC and ground. Allows for extremely steep edges (output delay in the 1 μs range).

To allow signals pending very briefly to be output with pulse width modulation (for example, level duration of 0.1 ms), you must operate the output as a high-speed output.

The rated load is reduced from 0.5 A to 0.4 A with this operating mode.

##### Further information

You can find more information on the pulse width modulation operating mode in the sections [Assignment of the control interface](#assignment-of-the-control-interface) and [Assignment of the feedback interface](#assignment-of-the-feedback-interface).

#### Assignment of the control interface

##### Control interface

The user program uses the control interface to influence the behavior of the technology inputs and technology outputs at interface X142.

The following table shows the control interface assignment:

Assignment of the control interface

| Offset from start address | Parameter |  | Meaning |  |
| --- | --- | --- | --- | --- |
| Byte 0 | SET_DQ (DQ0 to DQ7) |  | Set DQ (DQ0 to DQ7) |  |
| Byte 1 to 3 | Reserved |  | Must not be used |  |
| Byte 4 to 7 | TEC_OUT (DQ0) |  | Timer DQ:   Byte 0, 1: OFF TIME (output time stamp for DQ reset)   Byte 2, 3: ON TIME (output time stamp for setting DQ) |  |
| Oversampling DQ:   Byte 0 to 3: 32 states for oversampling |  |  |  |  |
| Pulse width modulation (PWM):   Byte 0 to 3: PWM bit pattern |  |  |  |  |
| Byte 8 to 11 | TEC_OUT (DQ1) |  | See Byte 4 to 7 |  |
| Byte 12 to 15 | TEC_OUT (DQ2) |  |  |  |
| Byte 16 to 19 | TEC_OUT (DQ3) |  |  |  |
| Byte 20 to 23 | TEC_OUT (DQ4) |  |  |  |
| Byte 24 to 27 | TEC_OUT (DQ5) |  |  |  |
| Byte 28 to 31 | TEC_OUT (DQ6) |  |  |  |
| Byte 32 to 35 | TEC_OUT (DQ7) |  |  |  |
| Byte 36 | SEL (DI0, DI1) |  | SEL DI1 | Bit 5 to 7: Edge selection for time stamp acquisition DI1   001 Rising edges only   010 Falling edges only   011 Rising and falling edges   (in order of occurrence)   101 First rising, then falling edge   110 First falling, then rising edge   000, 100, 111 reserved |
| Bit 4: Cyclical time stamp acquisition for DI1 |  |  |  |  |
| SEL DI0 | Bit 0 to 3: see SEL DI1 |  |  |  |
| Byte 37 | SEL (DI2, DI3) |  | See byte 36 |  |
| Byte 38 | SEL (DI4, DI5) |  |  |  |
| Byte 39 | SEL (DI6, DI7) |  |  |  |
| Byte 40, 41 | STW | MSL | Bit 12 to 15: Sign of life counter (master sign of life) |  |
| --- | Bit 1 to 11: Reserved; bits must be set to 0 |  |  |  |
| SYN | Bit 0: Synchronization of X142 interface with the user program |  |  |  |

#### Assignment of the feedback interface

##### Feedback interface

The user program receives current values and status information from the X142 interface technology I/Os over the feedback interface.

The following table shows the feedback interface assignment:

Assignment of the feedback interface

| Offset from start address | Parameter |  | Meaning |  |
| --- | --- | --- | --- | --- |
| Byte 0 | STS_DI (DI0 to DI7) |  | State DI (DI0 to DI7) |  |
| Byte 1 to 3 | Reserved |  | Must not be used |  |
| Byte 4 to 7 | TEC_IN (DI0) |  | Timer DI:   Byte 0, 1: 2nd TIME/OFF TIME (second input time stamp)  Byte 2, 3: 1st TIME/ON TIME (first input time stamp) |  |
| Oversampling DI:   Byte 0 to 3: Oversampling value |  |  |  |  |
| Event/period duration measurement | Event measurement:   Byte 0, 1: Reserved   Byte 2, 3: Counter value |  |  |  |
| Byte 8 to 11 | TEC_IN_EXT (DI0) |  | Time period measurement:   Byte 0 to 3: Measured time period |  |
| Byte 12 to 15 | TEC_IN (DI1) |  | See byte 4 to 11 |  |
| Byte 16 to 19 | TEC_IN_EXT (DI1) |  |  |  |
| Byte 20 to 23 | TEC_IN (DI2) |  |  |  |
| Byte 24 to 27 | TEC_IN_EXT (DI2) |  |  |  |
| Byte 28 to 31 | TEC_IN (DI3) |  |  |  |
| Byte 32 to 35 | TEC_IN_EXT (DI3) |  |  |  |
| Byte 36 to 39 | TEC_IN (DI4) |  |  |  |
| Byte 40 to 43 | TEC_IN_EXT (DI4) |  |  |  |
| Byte 44 to 47 | TEC_IN (DI5) |  |  |  |
| Byte 48 to 51 | TEC_IN_EXT (DI5) |  |  |  |
| Byte 52 to 55 | TEC_IN (DI6) |  |  |  |
| Byte 56 to 59 | TEC_IN_EXT (DI6) |  |  |  |
| Byte 60 to 63 | TEC_IN (DI7) |  |  |  |
| Byte 64 to 67 | TEC_IN_EXT (DI7) |  |  |  |
| Byte 68 | LEC (DI0, DI1) |  | Bit 4 to 6: Lost Edge Counter for DI1   Bit 0 to 2: Lost Edge Counter for DI0  Bit 3, 7: Reserved (must not be used) |  |
| Byte 69 | LEC (DI2, DI3) |  | Bit 4 to 6: Lost Edge Counter for DI3   Bit 0 to 2: Lost Edge Counter for DI2  Bit 3, 7: Reserved (must not be used) |  |
| Byte 70 | LEC (DI4, DI5) |  | Bit 4 to 6: Lost Edge Counter for DI5   Bit 0 to 2: Lost Edge Counter for DI4  Bit 3, 7: Reserved (must not be used) |  |
| Byte 71 | LEC (DI6, DI6) |  | Bit 4 to 6: Lost Edge Counter for DI7   Bit 0 to 2: Lost Edge Counter for DI6  Bit 3, 7: Reserved (must not be used) |  |
| Byte 72 | Reserved |  | Must not be used |  |
| Byte 73 | Layout property |  | Specific value |  |
| Byte 74, 75 | ZSW | SSL | Bit 12 to 15: Sign of life counter (slave sign of life) |  |
| --- | Bit 10, 11: Reserved (must not be used) |  |  |  |
| SYNC | Bit 8: X142 interface is synchronized with user program |  |  |  |
| Channel address | Bit 4 to 7 and 9: Number of the respective DI or DQ |  |  |  |
| Channel mode | Bit 0 to 3: Operating mode of the respective DI or DQ |  |  |  |

##### Substitute value behavior

If the CPU is in STOP, the digital outputs (irrespective of any inversion set) return "0" (LOW level) as a substitute value.

##### Reading back the terminal state

STS_DI (offset byte 0 of the feedback interface) represents the logical channel status, taking account of any inversion configured.

**Digital inputs**

With digital inputs (DI, Timer DI, oversampling DI, event/period measurement), the value corresponds to the logical state of the digital input.

**Digital outputs**

With digital outputs (DQ, Timer DQ, oversampling DQ, pulse width modulation PWM), the value corresponds to the actual terminal state of the digital output. If the terminal state deviates from the controlled state, there may be an output driver short-circuit or defect.

> **Note**
>
> **STS_DI**
>
> Signals are only reliably acquired over STS_DI if the level is significantly longer than the input delay + acquisition cycle of the digital inputs/outputs (X142).
>
> Example: If you operate the digital inputs/outputs (X142) as isochronous to the MC Servo in a cycle of 2 ms and a set input delay of 125 µs, the level duration must be > 2.125 ms.

#### Programming example

You can find a programming example for the use of the integrated digital inputs/outputs in the following [FAQ on the Internet](https://support.industry.siemens.com/cs/ww/en/view/109782269).

### Configuring the digital inputs and digital inputs/outputs (X122/X132)

This section contains information on the following topics:

- [SINAMICS digital inputs and digital inputs/outputs (X122/X132)](#sinamics-digital-inputs-and-digital-inputsoutputs-x122x132)

#### SINAMICS digital inputs and digital inputs/outputs (X122/X132)

The digital inputs and digital inputs/outputs (X122/X132) are assigned to SINAMICS Integrated. Through configuration (frames 39x), you can, however, also use the digital inputs and digital inputs/outputs (X122/X132) for the CPU. The following applies:

- A digital output is always only available exclusively to SINAMICS Integrated or to the CPU.
- If you use a digital input for the CPU, you can also interconnect the digital input at the drive end.

You can configure the digital inputs and digital inputs/outputs (X122/X132) channel by channel. To do so, go to the function view in the project tree under "Automatic speed control" > "Parameter assignment" and set the configuration under "Inputs/outputs".

Bidirectional inputs/outputs are configured in the following configuration mask.

![Bidirectional inputs/outputs](images/128392005771_DV_resource.Stream@PNG-en-US.png)

Bidirectional inputs/outputs

You can assign the SINAMICS digital inputs and digital inputs/outputs (X122/X132) using frame 39x of the PU. The status information of the digital inputs and digital outputs is then transferred at the PROFIdrive PZD sampling rate (p2048). The inputs/outputs are also sampled in the configured sampling time for the digital inputs and digital inputs/outputs (p0799). The application of the output values and return of the input values are therefore subject to dead times and jitter.

> **Note**
>
> Telegram 393 is set by default during configuration of the SINAMICS Integrated.

![Configuration of frame 393 for automatic speed control](images/129760178187_DV_resource.Stream@PNG-en-US.png)

Configuration of frame 393 for automatic speed control

You can find further information on the various different frame types in AUTOHOTSPOT.

> **Note**
>
> **Interface X142**
>
> If you have particularly strict requirements for the digital input/outputs, use the digital input/outputs at interface X142. The digital inputs/outputs can be operated in isochronous mode and allow very short response times.

##### Programming example

You can find a programming example in the following [FAQ on the Internet](https://support.industry.siemens.com/cs/ww/en/view/109782269).

### Configuring the clock system

This section contains information on the following topics:

- [Overview of isochronous mode](#overview-of-isochronous-mode)
- [Configuring drives with SINAMICS Integrated isochronously](#configuring-drives-with-sinamics-integrated-isochronously)
- [Configuring technology I/Os (X142) as isochronous](#configuring-technology-ios-x142-as-isochronous)
- [Configuring additional drives on PROFINET (X150) as isochronous](#configuring-additional-drives-on-profinet-x150-as-isochronous)
- [Configuring the PROFIBUS interface as isochronous](#configuring-the-profibus-interface-as-isochronous)
- [Setting the clock system](#setting-the-clock-system)

#### Overview of isochronous mode

##### Introduction

The SIMATIC Drive Controller supports isochronous mode for the following clock systems:

- PROFINET IO interface X150
- PROFIBUS DP interface X126
- Technology I/Os X142
- SINAMICS Integrated with PROFIdrive Integrated (always isochronous)

You can operate the clock systems separately or coupled on an isochronous basis.

Exception: Isochronous coupling of the PROFIBUS DP interface is not possible.

##### Independent isochronous mode

If you want to operate the clock systems separately in isochronous mode, configure a cycle time for each clock system and assign the clock systems to different process images, for example:

- SINAMICS Integrated → PIP OB Servo [OB 91]
- PROFIBUS DP interface X126 → PIP 1 of isochronous mode interrupt OB [OB 6x]

The clock systems are in this case not isochronous **to each other**.

> **Note**
>
> You cannot operate the X142 technology I/Os in isochronous mode separately from SINAMICS Integrated.
>
> If you want to operate technology I/Os X142 and SINAMICS Integrated isochronously at the same time, the coupled isochronous mode must be set.

##### Coupled isochronous mode

In coupled isochronous mode, the relevant clock systems use a shared system clock.

The leading clock system provides its own system clock to the other clock systems.

The following table shows the possible combinations for coupled isochronous mode on the SIMATIC Drive Controller. The leading clock system for each combination is indicated.

Possible combinations for coupled isochronous mode

| PROFINET IO interface X150 | Technology I/Os X142 (local send clock) | SINAMICS Integrated (PROFIdrive Integrated) | PROFIBUS DP interface X126 |
| --- | --- | --- | --- |
| **X (leading)** | X | X | - |
| **X (leading)** | - | X | - |
| **X (leading)** | X | -<sup>1</sup> | - |
| - | **X (leading)** | X | - |
| <sup>1</sup> SINAMICS Integrated is not configured. |  |  |  |

You configure coupled isochronous mode in STEP 7; see [Setting the clock system](#setting-the-clock-system).

> **Note**
>
> Isochronous coupling of the PROFIBUS interface with other clock systems is not possible.
>
> If you want to expand the drive configuration limits with distributed drive systems, connect those distributed drive systems over the PROFINET IO interface X150. Only the PROFINET IO interface X150 can be connected isochronously alongside the MC Servo to the clock system of SINAMICS Integrated and the X142 technology I/Os.

#### Configuring drives with SINAMICS Integrated isochronously

##### Requirements

- STEP 7 , V16 or higher
- SINAMICS Startdrive , V16 or higher

##### Procedure

1. Add a SIMATIC Drive Controller to your project.  
   The network view displays the components of a SIMATIC Drive Controller: SIMATIC S7-1500 CPU and SINAMICS Integrated, networked through PROFIdrive Integrated.

   ![SIMATIC Drive Controller in the network view](images/138360958859_DV_resource.Stream@PNG-en-US.png)

   SIMATIC Drive Controller in the network view
2. Open the device view of SINAMICS Integrated. Configure the SINAMICS S120 drive system with its drive objects.  
   You can find the relevant details in the [SINAMICS S120 with Startdrive commissioning manual](https://support.industry.siemens.com/cs/ww/en/view/109763294).

   ![Configuring the SINAMICS S120 drive system](images/139296277899_DV_resource.Stream@PNG-en-US.png)

   Configuring the SINAMICS S120 drive system
3. Select the drive control in the SINAMICS Integrated device view.  
   Check the default PROFIdrive telegrams In the properties, under "Integrated_1" > "Telegram configuration" in the "General" tab. Make changes if required.  
   The following default settings are made automatically:

   - Automatic speed control: Frame 393
   - Supply: Frame 370
   - Drive axes: Frame 105

   ![Configuring PROFIdrive frames](images/128446766347_DV_resource.Stream@PNG-en-US.png)

   Configuring PROFIdrive frames
4. Create the axis technology objects. You create the axis technology objects under "Technology objects > Add new object" in the project tree.
5. Assign the configured drives to the axis technology objects.

   - Open the configuration of the technology object.
   - Navigate to "Hardware interface" > "Drive".
   - Select the "PROFIdrive" entry from the "Drive type" drop-down list.
   - Select the "Drive" entry from the "Data connection" drop-down list.
   - Select a SINAMICS Integrated drive axis from the "Drive" list.

   Only drives for which a suitable PROFIdrive frame has been configured are available for selection in the "Drive" list. You can find which PROFIdrive frames are supported by the SINAMICS Integrated in the [S7‑1500T Motion Control function manuals](https://support.industry.siemens.com/cs/ww/en/view/109751049).

   ![Assigning drives to the technology objects](images/128449186187_DV_resource.Stream@PNG-en-US.png)

   Assigning drives to the technology objects

   The technology object is connected to the drive. When the drives are assigned to the axis technology objects, the following takes place:

   - MC-Servo is created (if not already present)
   - The TPA OB Servo is entered as the process image for all PROFIdrive telegrams
6. Once you have configured all axis technology objects, switch back to the drive configuration if necessary. You can use the "Device configuration" button.

   !["Device configuration" button](images/128452118027_DV_resource.Stream@PNG-en-US.png)

   "Device configuration" button

   > **Note**
   >
   > With SINAMICS Integrated, all frames must be operated in isochronous mode on OB Servo (OB 91) or isochronous mode interrupt OB (OB 6x). STEP 7 checks compliance with this rule when compiling the SIMATIC Drive Controller.
   >
   > Exception: If you insert a SIMATIC Drive Controller in your project from the module catalog, "--- (none)" is entered as the organization block for the drive control. If you do not configure any other drive objects, you can also compile and download to the device without isochronous mode.

   ![Configuring telegrams as isochronous](images/128452822667_DV_resource.Stream@PNG-en-US.png)

   Configuring telegrams as isochronous

##### Setting the clock system for independent and coupled isochronous mode

You have configured SINAMICS Integrated as isochronous. Next, set the clock system.

Make the following settings in accordance with whether you are operating SINAMICS Integrated in independent or coupled isochronous mode:

- For independent isochronous mode:

  - Set the required cycle time.
  - Assign the "MC Servo" OB the clock system of SINAMICS Integrated.
- For coupled isochronous mode:

  - Assign the clock system of SINAMICS Integrated the leading clock system.  
    You can find details of how to assign the leading clock system in [Setting the clock system](#setting-the-clock-system).

#### Configuring technology I/Os (X142) as isochronous

##### Requirements

- STEP 7, V16 or higher
- SIMATIC Drive Controller has been configured.
- At least one axis technology object has been created at the CPU of the SIMATIC Drive Controller.  
  See for example [Configuring drives with SINAMICS Integrated isochronously](#configuring-drives-with-sinamics-integrated-isochronously).

##### Procedure

1. Open the device view of the CPU.
2. Configure the operating modes of the technology I/Os in the CPU properties under "General" > "DI/DQ 8x24VDC[X142]" > "Channel parameters", for example, a timer DQ for later use as a cam output for channel 3.

   ![Setting the operating mode for technology I/O X142](images/128460987787_DV_resource.Stream@PNG-en-US.png)

   Setting the operating mode for technology I/O X142
3. In the project tree under the axis technology object, add an output cam technology object under "Output cam" > "Add new output cam".
4. Open the configuration of the output cam.
5. Under "Hardware interface", select the "Activate output" checkbox and the option "Output over Timer DQ".
6. Assign the configured output under "Output".

   ![Assigning a channel to the output cam](images/128475592715_DV_resource.Stream@PNG-en-US.png)

   Assigning a channel to the output cam
7. Use the "Device configuration" button to switch back to the CPU settings and check the settings under "DI/DQ 8x24VDC [X142]" > "I/O addresses".

   The following settings must be configured for the input and output addresses:

   - "Isochronous mode" is enabled.
   - The organization block "MC Servo" is selected.
   - The process image "OB Servo PIP" is selected.

##### Automatic settings

Isochronous mode is mandatory for certain operating modes of the X142 technology I/O channels.

As soon as you set one of the following operating modes for a technology I/O channel, STEP 7 automatically selects the option "isochronous mode".

- Timer DI
- Timer DQ
- Oversampling DI
- Oversampling DQ
- Event/period measurement

If you assign an output cam, cam track or measuring input technology object to an X142 I/O, STEP 7 automatically sets the process image "OB Servo PIP".

In all other cases, you set the process image manually. If isochronous mode is mandatory for at least one technology I/O, you must set the process image of the "MC Servo" OB (OB91) or an isochronous mode interrupt OB (OB6x).

##### Setting the clock system

You have configured the technology I/Os as isochronous. Next, set the clock system.

Make the following settings in accordance with whether you are operating the X142 technology I/Os in independent or coupled isochronous mode:

- For independent isochronous mode or if the X142 technology I/Os are the leading clock system

  - Set the required cycle time.
  - Assign the "MC Servo" OB the clock system of the technology I/Os.
  > **Note**
  >
  > You cannot operate the X142 technology I/Os in isochronous mode separately from SINAMICS Integrated. If you want to operate technology I/Os X142 and SINAMICS Integrated isochronously at the same time, the coupled isochronous mode must be set.
- For coupled isochronous mode:

  - Assign the leading clock system to the clock system of the technology I/Os.  
    You can find details of how to assign the leading clock system in [Setting the clock system](#setting-the-clock-system).

#### Configuring additional drives on PROFINET (X150) as isochronous

##### Requirement

- STEP 7, V16 or higher
- SINAMICS Startdrive, V16 or higher

You can import drives that are not integrated in the TIA Portal via Startdrive using GSD files (generic station description). To do so, install the drive in the "Options" menu as a device description file (GSD).

##### Adding a drive and frame to the device configuration

1. Add the required drive system in the network view, for example, SINAMICS S120 CU320-2 PN.
2. Open the device view of the drive system and configure the drive objects.  
   You can find the relevant details in the [SINAMICS S120 with Startdrive commissioning manual](https://support.industry.siemens.com/cs/ww/en/view/109763294).
3. Open the network view. Assign the drive system to the PROFINET interface [X150] of the CPU.
4. Open the topology view. Interconnect the port of the drive system as in the real configuration with the port of the CPU.
5. Configure the PROFIdrive frames for the drive axes, for example, frame 105.

> **Note**
>
> If you use a PROFINET IO drive system other than SINAMICS S120, adding and configuring may differ from the description in certain respects. The frame is automatically preassigned in line with the drive system.

##### Activating isochronous mode in the device configuration

You can operate PROFINET drives in isochronous or non-isochronous mode. Isochronous mode, however, increases the quality of the position control of the drive and is therefore recommended for drives such as SINAMICS S120.

Proceed as follows to activate isochronous mode for the drive:

1. Select the device view of the drive system.
2. In the properties window, select the tab "PROFINET Interface [X150]" > "Advanced options" > "Isochronous mode".
3. Select the "Isochronous mode" check box.
4. In the properties window, select the tab "PROFINET Interface [150]" > "Advanced options" > "Real-time settings" > "Synchronization".
5. Select "IRT" as the RT class.

> **Note**
>
> If you have configured a PROFIdrive frame at the drive that requires isochronous mode, STEP 7 automatically sets "Isochronous mode" and the RT class "IRT".

##### Configuring the CPU as sync master and setting the send clock

1. Select the device view of the CPU.
2. In the properties window, select the tab "PROFINET interface [X150]" > "Advanced options" > "Real-time settings" > "Synchronization".
3. Select "IRT" as the RT class if it has not already been set automatically.
4. Select "Sync master" from the "Synchronization role" drop-down list.
5. Click the "Domain settings" button.
6. Set the required send clock.

##### Selecting the drive in the configuration of the technology object

1. Add a new axis technology object.
2. Open the configuration "Hardware interface" > "Drive".
3. Select the "PROFIdrive" entry from the "Drive type" drop-down list.
4. Select a drive axis of the PROFINET drive unit from the "Drive" list.  
   Only drives for which you have configured a suitable PROFIdrive frame are available for selection. You can find out which PROFIdrive frames are supported by the SIMATIC Drive Controller in the [S7‑1500T Motion Control function manuals](https://support.industry.siemens.com/cs/ww/en/view/109751049).

   Using the "Device configuration" button, you can switch to the drive device view, for example, to configure drives or set other PROFIdrive frames (for example 39x frame for the X122/X132 IOs of a CU320‑2).

##### Setting the clock system

You have configured an external drive as isochronous on PROFINET using the example of the SINAMICS S120 CU320‑2 PN. Next, set the clock system.

- Choose between independent and coupled isochronous mode.
- Set the required send clock.
- Assign the "MC Servo" OB the clock system of the PROFINET interface X150.

You can find more information in [Setting the clock system](#setting-the-clock-system).

#### Configuring the PROFIBUS interface as isochronous

You can find out how to configure isochronous mode for distributed I/O on the PROFIBUS DP in the [Isochronous Mode](https://support.industry.siemens.com/cs/ww/en/view/109755401) function manual.

> **Note**
>
> Isochronous coupling of the PROFIBUS interface with other clock systems is not possible.
>
> If you want to expand the drive configuration limits with distributed drive systems, connect those distributed drive systems over the PROFINET IO interface X150. Only the PROFINET IO interface X150 can be connected isochronously alongside the MC Servo to the clock system of SINAMICS Integrated and the X142 technology I/Os.

#### Setting the clock system

The SIMATIC Drive Controller supports isochronous mode for the following clock systems:

- PROFINET IO interface X150
- PROFIBUS DP interface X126
- Technology I/Os X142
- SINAMICS Integrated with PROFIdrive Integrated (always isochronous)

You can operate the clock systems separately or coupled on an isochronous basis. Exception: Isochronous coupling of the PROFIBUS DP interface is not possible. You can find information on the combinations in which you can couple the clock systems in [Overview of isochronous mode](#overview-of-isochronous-mode).

You make the required settings in the relevant clock systems.

Once you have set and, if necessary, coupled the clock systems, you need to couple the OB servo with the clock system in which you wish to operate the drives / that is the leading clock system. Depending on the configuration, these settings are made by the system.

##### Use of clock cycles < 500 μs

You can only use clock cycles < 500 μs in the CPU 1507D TF with the following restrictions:

- Limited quantities are available.
- The vulnerability for level overflows increases, for example, with MC Servo [OB91] and MC Interpolator [OB92]. This may result in an involuntary STOP of the CPU, especially in case of additional loads caused by the user program, traces and large watch tables.
- A down-scaling from the application cycle of the MC-Servo [OB91] to the selected clock system, results in an additional load and should be avoided with small clocks.

You should, therefore, only use clock cycles < 500 μs in exceptional cases and test your application very intensely.

For small position controller clock cycles, you can also use the position controller in the drive (Dynamic Servo Control function, DSC). This allows for position controller clock cycles of 125 μs, for example.

##### Dynamic Servo Control (DSC)

In drives that support Dynamic Servo Control (DSC), you can optionally use the position controller in the drive.

If you use telegrams that support DSC, DSC is automatically enabled (setting "Position control in the drive (DSC enabled)" is enabled at the axis TO under control loop / Dynamic Servo Control (DSC)). The position controller in the drive is usually implemented with a rapid speed-control cycle. This improves the control quality of the drive.

For drives on the SINAMICS Integrated, the Siemens telegram 105 is sent with DSC by default.

> **Note**
>
> Isochronous mode is essential on the controller and on the drive side for the operation of DSC.

You can find further information in the [S7-1500T Motion Control function manuals](https://support.industry.siemens.com/cs/ww/en/view/109751049).

##### SINAMICS Integrated clock system

Proceed as follows to set the clock system of the SINAMICS Integrated:

1. Switch to the network view.
2. Click on PROFIdrive Integrated in the network view.
3. Make the settings for the SINAMICS Integrated under "Constant bus cycle time".  
   The SINAMICS Integrated is always isochronous (option is always selected).

   ![SINAMICS Integrated (PROFIdrive Integrated) clock system](images/128486138635_DV_resource.Stream@PNG-en-US.png)

   SINAMICS Integrated (PROFIdrive Integrated) clock system

   Adjust other settings if required – for example times Ti/To for reading in/outputting data in isochronous mode.

Setting options for "Cycle time" in the SINAMICS Integrated clock system

| Setting options | Note |
| --- | --- |
| Manual | With these settings, you operate the SINAMICS Integrated as an independent clock system. |
| Automatic minimum |  |
| Use local send clock [X142] | With this setting, you operate the SINAMICS Integrated in isochronous mode coupled with the clock system of the X142 technology I/Os.   Use this setting if you want to use the technology I/Os isochronously with the OB servo, for example, for measuring input or output cam applications.   Please note the following:  - You cannot operate the X142 technology I/Os in isochronous mode separately from SINAMICS Integrated. - If you want to operate technology I/Os X142 and SINAMICS Integrated isochronously at the same time, the coupled isochronous mode must be set.   Consistency checks ensure that the setting is correct. |
| Using the send clock of the PROFINET interface [X150] | With this setting, you operate SINAMICS Integrated in isochronous mode coupled with PROFINET interface X150. SINAMICS Integrated uses the system clock of PROFINET interface X150.  Use this setting if you need to operate the SIMATIC Drive Controller in isochronous mode at PROFINET IO interface X150, for example, for the connection of drives or for synchronous operation across PLC. |

##### X142 technology I/Os clock system

Proceed as follows to set the clock system of the X142 technology I/Os:

1. In the device view of STEP 7, select the CPU of the SIMATIC Drive Controller.
2. Navigate to "Advanced configuration" > "Isochronous mode" in the properties of the CPU.
3. Select the required settings from the "Source of send clock" drop-down list in the "Isochronous mode for local modules" section.

   ![Technology I/O clock system](images/128487767307_DV_resource.Stream@PNG-en-US.png)

   Technology I/O clock system

Setting options for "Source of send clock" in the clock system of the technology I/Os

| Setting options | Note |
| --- | --- |
| Local send clock | With this setting, you operate the X142 technology I/Os as an independent clock system, or as the leading clock system if you couple the clock system of the SINAMICS Integrated. |
| Using the send clock of the PROFINET interface [X150] | With this setting, you operate X142 technology I/Os in isochronous mode coupled with PROFINET interface X150. The X142 technology I/Os use the system clock of PROFINET interface X150. |

##### PROFINET IO interface X150 clock system

Proceed as follows to set the clock system of PROFINET interface X150:

1. Select the PROFINET IO system in the network view of STEP 7.
2. Make the settings for the send clock, etc. under "PROFINET subnet" > "Domain management" > "Sync domains".

In coupled isochronous mode with other clock systems, the clock system of the PROFINET interface is always leading.

You can find additional information on configuring isochronous mode on PROFINET IO in the [Isochronous mode](https://support.industry.siemens.com/cs/ww/en/view/109755401) function manual.

##### PROFIBUS interface X126 clock system

You must follow the rules below during configuration if you want to operate the PROFIBUS DP interface in isochronous mode:

Rules for configuring isochronous mode for PROFIBUS DP interface

| If ... | The configured cycle time of the PROFIBUS DP interface must... |
| --- | --- |
| A SINAMICS Integrated is configured | Be equal to or an integer multiple of the configured cycle time of the SINAMICS Integrated (PROFIdrive Integrated) |
| The X142 technology I/Os are operated in isochronous mode | Be equal to or an integer multiple of the configured cycle time of the X142 technology I/Os |
| The clock system of the PROFINET IO interface is coupled with one of the two clock systems. | Be equal to or an integer multiple of the configured cycle time of the PROFINET IO interface |

Consistency checks ensure that the setting is correct.

Proceed as follows to set the clock system of the PROFIBUS interface:

1. Select the DP master system in the network view of STEP 7.
2. Make the settings for the DP cycle under "Constant bus cycle time".

> **Note**
>
> Isochronous coupling of the PROFIBUS interface with other clock systems is not possible.
>
> If you want to expand the drive configuration limits with distributed drive systems, connect those distributed drive systems over the PROFINET IO interface X150. Only the PROFINET IO interface X150 can be connected isochronously alongside the MC Servo to the clock system of SINAMICS Integrated and the X142 technology I/Os.

##### Synchronizing MC Servo with clock system

Proceed as follows to synchronize the MC Servo with a clock system:

1. Open the "Program blocks" folder in the project tree.
2. Select the "MC Servo" organization block.
3. Select the "Properties" command in the shortcut menu.
4. Select the "Cycle time" entry in the area navigation.
5. The option "Synchronous to the bus" must be selected in the dialog box.
6. In the "Source of send clock" drop-down list, select the clock system to be synchronized with the OB MC‑Servo.

   ![Synchronizing MC Servo with clock system](images/138466289291_DV_resource.Stream@PNG-en-US.png)

   Synchronizing MC Servo with clock system

Setting options for synchronization with a clock system

| Setting options<sup>1)</sup> | Note |
| --- | --- |
| PROFIdrive system (1) | With this setting, you synchronize MC Servo with the clock system of SINAMICS Integrated. |
| PROFINET IO system (100) | With this setting, you synchronize MC Servo with PROFINET interface X150. |
| Central (0) | With this setting, you synchronize MC Servo with the clock system of technology I/Os X142. |
| DP master system (2) | With this setting, you synchronize MC Servo with PROFIBUS interface X126. |
| <sup>1) </sup>The designations may vary depending on the names assigned. |  |

For coupled isochronous mode, the leading clock system must always be selected.

If the leading clock system is not set as the source of the send clock in the case of a coupled clock system, then the leading clock system is automatically set when compiling the project data and a corresponding note is displayed.

##### Setting the application cycle

The application cycle of MC Servo is derived from the send clock and a configurable factor. The adjustable factors depend on the coupled clock system.

## I/O - Properties - X142

You can configure the following operating modes for the individual channels of the X142 interface:

Overview of operating modes

| Operating mode of X142 I/Os  (8 channels) | Functionality | Use with technology objects (TOs) | Use via I/O area (without TO) | Isochronous mode |
| --- | --- | --- | --- | --- |
| DI | Digital input  - Input delay (1 µs/125 µs) - Hardware interrupt (optional)   Hardware interrupt at rising and/or falling edge | - Hardware limit switch for positioning and synchronous axes - Reference mark - ... | No OB restrictions | Optional |
| DQ | Digital output | - Output cam - Cam track - ... | No OB restrictions | Optional |
| Timer DI | Acquisition of the switching time of a digital input signal with up to two edges per application cycle (e.g. for use as measurement sensing input) | Measuring input (OB 91 required) | OB 91/OB 6x  required | Required |
| Timer DQ | Precisely timed output of a digital output signal with up to two edges per application cycle (e.g. for use as an output cam output) | - Output cam (OB 91 required) - Cam track (OB 91 required) | OB 91/OB 6x  required | Required |
| Oversampling DI | Acquisition of 32 states of a digital input signal at equal intervals per application cycle | --- | OB 91/OB 6x  required | Required |
| Oversampling DQ | Output of 32 states of a digital output signal at equal intervals per application cycle | --- | OB 91/OB 6x  required | Required |
| Event/period duration measurement | Measurement of number of edges and period duration (e.g. for simple speed measurement with hole mask and light barrier) | --- | OB 91/OB 6x  required | Required |
| Pulse width modulation PWM | Output of a configurable pulse-pause ratio with a configurable frequency | --- | No OB restrictions | Optional |
