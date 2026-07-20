---
title: "Using additional diagnostics options (S7-300, S7-400)"
package: HWCDiag34enUS
topics: 33
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using additional diagnostics options (S7-300, S7-400)

This section contains information on the following topics:

- [Hardware diagnostics (S7-300, S7-400)](#hardware-diagnostics-s7-300-s7-400)
- [Connection diagnostics (S7-300, S7-400)](#connection-diagnostics-s7-300-s7-400)

## Hardware diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Displaying non-editable and current values of assignable module properties (S7-300, S7-400)](#displaying-non-editable-and-current-values-of-assignable-module-properties-s7-300-s7-400)
- [Displaying current values of dynamic module properties (S7-300, S7-400)](#displaying-current-values-of-dynamic-module-properties-s7-300-s7-400)
- [Checking a module for defects (S7-300, S7-400)](#checking-a-module-for-defects-s7-300-s7-400)
- [Changing the properties of a module or the programming device/PC (S7-300, S7-400)](#changing-the-properties-of-a-module-or-the-programming-devicepc-s7-300-s7-400)

### Displaying non-editable and current values of assignable module properties (S7-300, S7-400)

This section contains information on the following topics:

- [Showing general properties and system-relevant information for a module (S7-300, S7-400)](#showing-general-properties-and-system-relevant-information-for-a-module-s7-300-s7-400)
- [Showing the communications properties of a module (S7-300, S7-400)](#showing-the-communications-properties-of-a-module-s7-300-s7-400)
- [Show interfaces and interface properties of a module (S7-300, S7-400)](#show-interfaces-and-interface-properties-of-a-module-s7-300-s7-400)
- [Showing the operand areas, organization blocks and system blocks of a CPU (S7-300, S7-400)](#showing-the-operand-areas-organization-blocks-and-system-blocks-of-a-cpu-s7-300-s7-400)
- [Displaying properties of the time system of a module (S7-300, S7-400)](#displaying-properties-of-the-time-system-of-a-module-s7-300-s7-400)

#### Showing general properties and system-relevant information for a module (S7-300, S7-400)

##### Where do I find the information I need?

The general properties and system-relevant information for a module can be found in the "General" group in the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.

##### Structure of the "General" group

The "General" group consists of the following areas:

- Module
- Module information
- Manufacturer information

##### "Module" area

This area displays the following additional module information for S7-300 and S7-400:

- Version of bootloader

##### "Module information" area

This area shows the following additional module information for S7-300 and S7-400 that you have specified during the hardware configuration:

- Device name (you specified this in the network view).
- Plant designation

  If a CPU, a slave, an I/O device, or a module in the device supports the assignment of a plant-wide unique plant designation, then this is shown here. (The plant designation clearly identifies parts of the plant according to functional aspects. It is hierarchically structured in accordance with IEC 1346-1). This allows, for instance, the CPU to be identified from the user program. You can read out the plant designation with the "RDSYSST" instruction.
- Location designation

  If a CPU, a slave, an IO device, or a module in the device supports the assignment of a location designation, then this is shown here (the location designation is part of the equipment identifier that identifies the precise location, e.g., a process tag within a process manufacturing plant, similar to a road in a road map).

##### "Manufacturer information" area

This area displays the following additional module information for S7-300 and S7-400:

- Copyright law entry

#### Showing the communications properties of a module (S7-300, S7-400)

##### Where do I find the information I need?

The communications properties of a module can be found in the "Communication" group of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.

This shows the following properties:

- Cycle load due to communication, configured:

  Set value of the "Cycle loading by communications" parameter, i.e., the proportion of the CPU processing power available for communication in each cycle.
- Connection resources, maximum number:

  Specifies the maximum possible number of available connection resources of the module. A certain number of the available connection resources are reserved for programming device and OP communications and on the S7-300 (with the exception of the 318-2 DP CPU) for S7 basic communications. You can however establish other programming device and OP connections in addition; the number of unassigned connection resources is then reduced accordingly.

#### Show interfaces and interface properties of a module (S7-300, S7-400)

##### Where do I find the information I need?

The interfaces and interface properties of a module can be found in the following groups of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed:

- MPI interface
- MPI/DP interface
- DP interface
- PROFINET interface

##### "MPI interface" group

This group displays the following data:

- Transmission speed:

  Current transmission rate setting at the MPI interface for the automation system

##### "MPI/DP interface" group

This group displays the following data:

- Transmission speed:

  Current transmission rate setting for the MPI/DP interface of the automation system
- DP mode:

  Compatibility mode of the MPI/DP interface whose interface type is set to "PROFIBUS". In the case of modules that support the "DPV1" mode, these can assume the values "S7 compatible" and "DPV1".

  > **Note**
  >
  > If you have set the interface type of the MPI/DP interface to "MPI", then "DP mode" does not contain a valid value.

##### "DP interface" group

This group displays the following data:

- DP mode:

  Compatibility mode of the DP interface. In the case of modules that support the "DPV1" mode, these can assume the values "S7 compatible" and "DPV1".

##### "PROFINET interface" group

This group is divided into the following areas:

- "Ethernet address" with the "Network connection" and "IP Parameters" subareas
- "Ports"
- "Statistics" (this area is not considered here, because it does not deal with the current values of configurable module properties).

> **Note**
>
> The "Ethernet address" and "Ports" areas have already been described outside the chapter "Using additional diagnostics options" as they apply for S7-1200 and S7-300/S7-400.

#### Showing the operand areas, organization blocks and system blocks of a CPU (S7-300, S7-400)

##### Where do I find the information I need?

The operand areas, organization blocks, and system blocks of a CPU can be found in the "Performance data" group in the "Diagnostics" folder of the Online and Diagnostics view of the module to be diagnosed.

##### "Performance data" group

The following information for the respective CPU is shown in the "Performance data" group:

- Operand areas:

  The table gives information regarding

  - The operand type, for example process image input, counters
  - The number of operands or size of their areas
  - The available address range of the operands, for example I0.0 to I127.7
- Organization blocks:

  All organization blocks (OBs) including their function

  You can sort the table rows as follows: Click a column heading to arrange the table rows in such a way that the contents of this column are ordered alphabetically starting from the top.
- System blocks:

  All system functions (SFCs) and system function blocks (SFBs)

  You can sort the table rows as follows: Click a column heading to arrange the table rows in such a way that the contents of this column are ordered alphabetically starting from the top.

#### Displaying properties of the time system of a module (S7-300, S7-400)

##### Where do I find the functions I need?

You can find the properties of the time system of a module in the "Set time of day" group in the "Functions" folder of the Online and Diagnostics view.

##### Structure of the "Set time of day" group

The "Set time of day" group consists of the following areas:

- Area for reading out and setting the time of day (this area is not examined here)
- Time system

##### Structure of the "Time system" area

The "Time system" area consists of the following subareas:

- "Clock"
- "Synchronization"

##### "Clock" subarea

The "Clock" subarea consists of the following elements:

- Resolution:

  States the precision with which the calculation and output of the time is performed
- Real-time clock:

  Displays whether the CPU has a real-time clock: "present" if yes; "not present" if no
- Correction factor:

  Assigned correction factor for the realtime clock of the module. The daily deviation of the clock is compensated with the correction factor.

##### "Synchronization" subarea

Synchronization mechanisms allow creation of synchronicity between the clocks in different sub-systems. The settings for time-of-day synchronization are made when assigning the module parameters.

The integral real-time clock - where present - can thus synchronize the clocks of other modules (master), or it can itself be synchronized by the clocks of other devices (slave), or it can take no part in the synchronization. Synchronization can be performed in the AS or on the MPI.

### Displaying current values of dynamic module properties (S7-300, S7-400)

This section contains information on the following topics:

- [Displaying current status of the LEDs and the mode selector of a CPU (S7-300, S7-400)](#displaying-current-status-of-the-leds-and-the-mode-selector-of-a-cpu-s7-300-s7-400)
- [Showing connection resources and occupied and reserved connections for a CPU (S7-300, S7-400)](#showing-connection-resources-and-occupied-and-reserved-connections-for-a-cpu-s7-300-s7-400)
- [Displaying statistical data of data transmissions made using the Ethernet interface (S7-300, S7-400)](#displaying-statistical-data-of-data-transmissions-made-using-the-ethernet-interface-s7-300-s7-400)
- [Displaying information about the runtime meter of a CPU (S7-300, S7-400)](#displaying-information-about-the-runtime-meter-of-a-cpu-s7-300-s7-400)

#### Displaying current status of the LEDs and the mode selector of a CPU (S7-300, S7-400)

##### Where do I find the information I need?

The current status of the LEDs of the mode selector of a CPU can be found in the display area of the "CPU control panel" pane of the "Online tools" task card.

##### Display area of the "CPU control panel" pane of the "Online Tools" task card

This area contains the following displays:

- Device name and CPU type
- Error (corresponds to the "SF" LED on S7-300 CPUs)

- RUN (corresponds to the "RUN" CPU operating mode)
- STOP (corresponds to the "STOP" CPU operating mode)
- FORCE (corresponds to the "FRCE" LED on the CPU)
- Current position of the mode selector

  > **Note**
  >
  > "RUN-P" may be displayed erroneously for S7-300 CPUs with a mode selector. In this case, the mode selector is set to "RUN".

#### Showing connection resources and occupied and reserved connections for a CPU (S7-300, S7-400)

##### Where do I find the information I need?

The connection resources not yet assigned and the assigned and reserved connections for a CPU can be found in the "Communications" group in the "Diagnostics" folder in the Online and Diagnostics view.

The "Connection resources" area contains the current values of the following dynamic module properties.

- Number of connection resources not yet assigned.

  These are shown under "Not assigned".

  > **Note**
  >
  > If connection resources are already reserved for certain types of communication, the unassigned resources cannot always be used for the various connection types.
- PG communication "reserved" and "assigned":

  Number of connection resources reserved/assigned for connections between the module and programming devices.

  > **Note**
  >
  > The number of connection resources assigned can be larger than the number of connection resources reserved, since - within the overall maximum number - other free connection resources can be used for programming device communication. On S7-300-CPUs with assignable connection resource parameters, you can increase the number of connection resources for programming device communication at the expense of the S7 basic communication.
- OP communication "reserved" and "assigned":

  Number of connection resources reserved/assigned for connections between the module and HMI devices (TDs, OPs).

  > **Note**
  >
  > The number of connection resources assigned can be larger than the number of connection resources reserved, since - within the overall maximum number - other free connection resources can be used for OP communications. On S7-300-CPUs with assignable connection resource parameters, you can increase the number of connection resources for OP communication at the expense of the S7 basic communication.
- S7 communication "reserved" and "assigned":

  This is displayed on S7-400 CPUs, on 318-2 CPUs and on 317-2 PN/DP CPUs.

  Reserved/assigned connection resources for configured S7 connections intended for exchanging data by calling communications function blocks (SFBs) in the user program. These can be regarded as hard wired connections (for instance CPU-CPU connections). They can be automatically established when starting communications or they can be established and broken off under program control. S7 communication can be performed via MPI, PROFIBUS, and Industrial Ethernet.
- S7 basic communication "reserved" and "assigned":

  This is displayed on S7-300 CPUs (but not on 318-2 CPUs and not on 317-2 PN/DP CPUs).

  Reserved/assigned connection resources for non-configured connections intended for exchanging data by calling communications functions (SFCs) in the user program. S7 basic communication can only be performed via MPI or within the automation system.
- Other communication "assigned":

  Additional connection resources for which no connection resources are reserved.

  Examples:

  - Communication by a S7-300 CPU using a CP (can be performed only on CPUs with assignable connection resource parameters)
  - Communication between networks (S7 routing) on S7-400 CPUs

> **Note**
>
> By means of a server function, in the case of assigned connection resources for S7 communication (i.e., if an S7-400 CPU is communicating with an S7-300 CPU via the SFCs "PUT" or "GET") the following resources are displayed for S7-300 CPUs:
>
> - If the CPU has no assignable connection resource parameters: Under "S7 basic communication"
> - If the CPU has assignable connection resource parameters: In the case of CPUs 317-2 PN / DP and 318-2 under "S7 communication", for all others under "Other communication"

#### Displaying statistical data of data transmissions made using the Ethernet interface (S7-300, S7-400)

##### Where do I find the information I need?

Statistical data for the data transmissions that took place via the Ethernet interface can be found in the "Statistics" area under the "PROFINET interface" group in the "Diagnostics" folder of the Online and Diagnostics view.

##### "Statistics" area

- Display

  Displays statistical data for sent and received data packets. This data allows the data transmission quality to be evaluated.

  The start of the recordings of the statistical data is shown in the first line ("Data packets since:"). This time is reset every time the statistical data is reset ("Reset" button).

  The statistical data display is updated continuously.
- "Reset" button

  The "Data packets since" time is reset and the statistical data are reset to "0".

#### Displaying information about the runtime meter of a CPU (S7-300, S7-400)

##### Where do I find the information I need?

Information about the runtime meter can be found in the "Runtime meter" group in the "Diagnostics" folder of the Online and Diagnostics view.

##### "Runtime meter" group

The "Runtime meter" group displays the following information for the active CPU runtime meter:

- No. of the runtime meter including information about whether it is a 16-bit or 32-bit runtime meter.
- Elapsed operating hours
- Status
- Information on whether or not an overflow has occurred

If the CPU has one or more 32-bit runtime meters, the respective symbol is given a red border when the metered value exceeds 32767 (maximum value for a 16-bit runtime meter). The "Overrun" column shows "no" if the runtime meter has not yet exceeded the maximum value for a 32-bit runtime meter.

The 32-bit runtime meter is set, started, stopped, and read out by the "[RTM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rtm-runtime-meters-s7-300-s7-400)" instruction.

### Checking a module for defects (S7-300, S7-400)

This section contains information on the following topics:

- [Performing channel-specific diagnostics of non-CPU modules (S7-300, S7-400)](#performing-channel-specific-diagnostics-of-non-cpu-modules-s7-300-s7-400)
- [Performing communication diagnostics of PROFINET ports (S7-300, S7-400)](#performing-communication-diagnostics-of-profinet-ports-s7-300-s7-400)
- [PROFINET IO component diagnostics (S7-300, S7-400)](#profinet-io-component-diagnostics-s7-300-s7-400)
- [Starting NCM S7 diagnostics (S7-300, S7-400)](#starting-ncm-s7-diagnostics-s7-300-s7-400)
- [Online connections for special diagnostics and firmware loader (S7-300, S7-400)](#online-connections-for-special-diagnostics-and-firmware-loader-s7-300-s7-400)

#### Performing channel-specific diagnostics of non-CPU modules (S7-300, S7-400)

##### Where are channel-specific diagnostic events of non-CPU modules displayed?

The channel-specific diagnostic events of non-CPU modules are displayed in the "Channel diagnostics" group in the Online and Diagnostics view.

##### "Channel diagnostics" group

The display consists of the following elements for each event:

- Slot of faulty module
- Number of faulty channel

  Note that the sequence of channel numbers in this display starts at 0.
- Fault type

  > **Note**
  >
  > **Diagnostic interrupts**
  >
  > A diagnostic interrupt can be reported to the CPU only if the module has diagnostic interrupt capability and the diagnostic interrupt has been enabled.
  >
  > The display of the diagnostic interrupt is a snapshot. Sporadic module defects can be identified in the diagnostics buffer of the respective CPU.

If you select a line in the table containing the channel errors, additional information will be provided for this error (if present).

#### Performing communication diagnostics of PROFINET ports (S7-300, S7-400)

##### Where are port-specific errors of PROFINET ports displayed?

The port-specific errors of PROFINET ports are displayed in the "Communication diagnostics" group of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.

##### Structure of the "Communication diagnostics" group

The "Communication diagnostics" group consists of the following areas:

- Table containing the port-specific errors
- "Details of the event" text field
- "Help on event" text field

##### Structure of the table containing the port-specific errors

Each line of the error table corresponds to one error.

The table consists of the following columns:

- Name: port no. and port designation, as well as diagnostics icon
- Error: description of the error that occurred on this port

##### "Details" text field

If you select a line in the error table, the "Detail" text field will contain detailed information (if available) on the corresponding error.

##### "Help on selected diagnostic line" text field

If you select a line in the error table, the "Help on selected diagnostic line" text field will contain help information (if available) on the corresponding error.

#### PROFINET IO component diagnostics (S7-300, S7-400)

##### Where do I perform PROFINET IO component diagnostics?

You perform the PROFINET IO component diagnostics in the "PROFINET IO diagnostics" group under "PROFINET interface" in the "Diagnostics" folder of the Online and Diagnostics view.

##### "PROFINET IO diagnostics" group

Manufacturer-related diagnostics texts for the IO device or the selected module of the IO device are displayed in this area.

If the diagnostics can be read by the IO controller, then communication errors and configuration errors (online/offline discrepancies) are displayed here.

#### Starting NCM S7 diagnostics (S7-300, S7-400)

##### Requirements

- An online connection to the module is not necessary.

##### Procedure

To start the NCM S7 diagnostics function, follow these steps:

1. Open the module in the Online and Diagnostics view.
2. Select the "Special diagnostics" group in the "Functions" folder.
3. Click the "Start special diagnostics" button in the "Special diagnostics" area.

##### Result

The NCM S7 diagnostics will be started.

#### Online connections for special diagnostics and firmware loader (S7-300, S7-400)

##### Special diagnostics: Establishing an online connection

Some network components (S7-300/400 CPs, PC CPs, gateways) provide expanded diagnostics data in special diagnostics.

**Requirement:**

A PG/PC interface is physically connected to the destination device, e.g. via an Ethernet cable.

**Procedure:**

Follow the steps outlined below to start special diagnostics:

1. Open the online and diagnostics view of the module.
2. In the "Functions" folder, select the group "Special diagnostics",
3. In the "Special diagnostics" area, click the "Start special diagnostics" button.

As of STEP 7 Professional V14 for several CPs only one online connection can be established from the engineering station via the CP. This connection can be established either with STEP 7 or special diagnostics.

If special diagnostics is not started by the steps listed above and an error message is output follow the steps below:

1. Disconnect the existing connection to the station.
2. Open the online and diagnostics view of the module again as described above and start special diagnostics.

**32-bit applications; NCM S7 diagnostics, firmware loader**

If you have established a connection to a PC CP from a 32-bit application and want to establish another online connection via the same interface of the PC CP, you must first terminate the connection of the 32-bit application.

##### Special diagnostics and firmware loader Chinese GUI

When you open the special diagnostics or the firmware loader with a Chinese GUI, you need to set the language for non-Unicode applications in the operating system to Chinese.

### Changing the properties of a module or the programming device/PC (S7-300, S7-400)

This section contains information on the following topics:

- [Special feature for S7-400 CPU operating mode switchover (S7-300, S7-400)](#special-feature-for-s7-400-cpu-operating-mode-switchover-s7-300-s7-400)
- [Loging onto the CPU for alarms and system diagnostics events (S7-300, S7-400)](#loging-onto-the-cpu-for-alarms-and-system-diagnostics-events-s7-300-s7-400)
- [Compressing the memory and copying from RAM to ROM (S7-300, S7-400)](#compressing-the-memory-and-copying-from-ram-to-rom-s7-300-s7-400)
- [Resetting the PROFINET interface parameters of an S7-300 or S7-400 CPU (S7-300, S7-400)](#resetting-the-profinet-interface-parameters-of-an-s7-300-or-s7-400-cpu-s7-300-s7-400)
- [Starting the firmware loader for an S7-300 or S7-400 CP (S7-300, S7-400)](#starting-the-firmware-loader-for-an-s7-300-or-s7-400-cp-s7-300-s7-400)
- [Updating the firmware of a TIM 3V / TIM 4R (S7-300, S7-400)](#updating-the-firmware-of-a-tim-3v-tim-4r-s7-300-s7-400)
- [Assigning an IP address to a PROFINET IO device (S7-300, S7-400)](#assigning-an-ip-address-to-a-profinet-io-device-s7-300-s7-400)

#### Special feature for S7-400 CPU operating mode switchover (S7-300, S7-400)

##### Specifying the startup type of an S7-400 CPU for switchover to "RUN" mode

If you want to switch an S7-400 CPU to "RUN" mode, choose one of the following startup types:

- Warm restart
- Cold restart
- Hot restart

#### Loging onto the CPU for alarms and system diagnostics events (S7-300, S7-400)

##### Requirement

- The PG/PC interface allows access to one or more devices in a subnet.

##### Procedure

1. Open the Online and Diagnostics view of the respective CPU.
2. Select the "Online access" group.
3. Select the "Receive alarms" check box in the "Alarms" area.

##### Result

During the next online connection, your programming device or PC will be logged on for receiving alarms and system diagnostics events from the relevant CPU.

> **Note**
>
> The Alarm view requires a continuous online connection for every CPU from which alarms are to be received.

##### Logging on when an online connection already exists

If the online connection to a CPU has already been established, you can still log on or off as follows for receipt of alarms:

- In the "Online" menu via the "Receive alarms" command
- In project tree using the CPU shortcut menu
- In the device view of the hardware configuration using the CPU shortcut menu
- In the network view of the hardware configuration using the CPU shortcut menu

---

**See also**

[Receiving alarms](Displaying%20alarms.md#receiving-alarms)

#### Compressing the memory and copying from RAM to ROM (S7-300, S7-400)

##### Where do I find the information I need?

The reorganization of the memory and copying from RAM to ROM can be found in the command area of the "Memory" pane in the "Online Tools" task card.

The reorganization of the memory can also be found in the command area of the "Memory" group in the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.

##### Command area of the "Memory" pane on the "Online Tools" task card

This area can contain the following buttons:

- Compress

  Pressing this button reorganizes the memory, to increase the size of the largest continuous free memory area.
- Copy RAM to ROM

  Pressing this button copies the content of the RAM load memory (user program) to a FEPROM:

  - To the memory card inserted into the CPU.
  - To the integral FEPROM.

> **Note**
>
> A button is specifically displayed when the module commands the respective function.

##### Command area of the "Memory" group in the "Diagnostics" folder of the Online and Diagnostics view

This area contains the following buttons:

- Compress

  Pressing this button reorganizes the memory, to increase the size of the largest continuous free memory area.

#### Resetting the PROFINET interface parameters of an S7-300 or S7-400 CPU (S7-300, S7-400)

##### Requirement

- You are using an S7-300 CPU with any firmware version or an S7-400 CPU with firmware version &gt;= V6.0.
- There is no memory card inserted in the CPU.
- There is an online connection to the CPU whose PROFINET interface parameters you want to reset.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the reset operation, you can place it in STOP mode by answering the security prompt with yes.

##### Procedure

To reset the PROFINET interface parameters of an S7-300 or S7-400 CPU, follow these steps:

1. Open the Online and Diagnostics view of the CPU.
2. Select the "Reset of PROFINET interface parameters" group in the "Functions" folder.
3. Click the "Reset" button.
4. Acknowledge the confirmation prompt with "OK".

**Note**

The user interface of the "Reset of PROFINET interface parameters" group of the Online and Diagnostics view depends on how you have opened the Online and Diagnostics view:

- If you opened it from the project tree with "Update accessible devices", the MAC address of the associated module is known and grayed out.
- If you opened it from within the project context, you must enter the relevant MAC address. Otherwise, the "Reset" button remains grayed out.

##### Result

The module is switched to STOP mode, if necessary, and the PROFINET interface parameters are reset. This means:

- The Ethernet interface settings are reset.
- The IP address is deleted.

#### Starting the firmware loader for an S7-300 or S7-400 CP (S7-300, S7-400)

##### Requirements

- The CP to be updated supports a firmware update.
- An online connection to the CP is not necessary.

##### Procedure

To start the firmware loader for an S7-300 or S7-400 CP, follow these steps:

1. Open the CP in the Online and Diagnostics view.
2. Select the "Firmware update" group in the "Functions" folder.
3. Click the "Start firmware loader" button in the "Firmware update" area.

##### Result

The firmware loader will be started.

> **Note**
>
> Updating the firmware with S7-300 and S7-400 CPs using the firmware loader differs from the standard mechanisms for updating firmware.

#### Updating the firmware of a TIM 3V / TIM 4R (S7-300, S7-400)

##### Validity

The information below applies to the following TIM modules for SIMATIC S7‑300 / 400:

- ST7-TIM

  - TIM 3V‑IE
  - TIM 3V‑IE Advanced
  - TIM 4R‑IE
  - TIM 4R‑IE Standalone

- DNP3-TIM

  - TIM 3V‑IE DNP3
  - TIM 4R‑IE DNP3

##### Sequence of the update

Different files are provided for the firmware update of these TIM modules:

- Firmware files
- Driver package

> **Note**
>
> **Sequence of the update**
>
> Adhere to the correct update sequence for a firmware update:
>
> 1. **First update the driver package.(**
>    ***.Z**
>    **).**
> 2. **Then update the firmware files.(**
>    ***.FWL**
>    **).**
>
> If you update the firmware files first and inadvertently select the wrong file, the TIM module may no longer be accessible in certain circumstances.

##### Files for the firmware update

The files for the firmware update are provided as compressed file archives. The archives contain files for the driver package and the firmware as well as readme files, which include information about the firmware version.

One archive is made available for each of the following TIM modules:

- Archive for ST7-TIM 3V..

  - TIM 3V‑IE
  - TIM 3V‑IE Advanced
- Archive for ST7-TIM 4R..

  - TIM 4R‑IE
  - TIM 4R‑IE Standalone

- Archive for TIM 3V‑IE DNP3
- Archive for TIM 4R‑IE DNP3

To save a file archive, follow these steps:

1. Copy the archive to the file system of your engineering station.

   Specify the directory in the online dialog for the update process.

   **Recommendation:**
     
   Copy the archive for the firmware versions of various module types in a separate directory.
2. Unzip the archive after you have copied it into the file system of your engineering station.

---

**See also**

[Online connections for special diagnostics and firmware loader (S7-300, S7-400)](#online-connections-for-special-diagnostics-and-firmware-loader-s7-300-s7-400)

#### Assigning an IP address to a PROFINET IO device (S7-300, S7-400)

This section contains information on the following topics:

- [Basic information on assigning an IP address to a PROFINET IO device (S7-300, S7-400)](#basic-information-on-assigning-an-ip-address-to-a-profinet-io-device-s7-300-s7-400)
- [Starting the address assignment via "Accessible devices" (S7-300, S7-400)](#starting-the-address-assignment-via-accessible-devices-s7-300-s7-400)
- [Starting the address assignment from the project context (S7-300, S7-400)](#starting-the-address-assignment-from-the-project-context-s7-300-s7-400)

##### Basic information on assigning an IP address to a PROFINET IO device (S7-300, S7-400)

###### Overview

You have two basic options for choosing an IP address:

- You assign the IP address yourself.
- You obtain the IP address from a DHCP server. (This option is not available for all IO devices.) In this case, the client ID, the MAC address, or the device name of the IO device is communicated to the DHCP server, depending on the option selected.

###### Requirement

The following assumes that the IP address of the IO device can also be obtained from a DHCP server. This is the case, for example, for some S7-300 CPs.

##### Starting the address assignment via "Accessible devices" (S7-300, S7-400)

###### Requirement

- The devices accessible via the associated interface of the PG/PC are displayed in the project tree (to display these, either double-click "Update accessible devices" in the project tree or select the "Accessible devices..." command in the "Online" menu.).
- You have double-clicked "Online access" -&gt; &lt;Selected interface&gt; -&gt; &lt;PROFINET IO device&gt; -&gt; "Online &amp; Diagnostics" in the project tree to open the Online and Diagnostics view.

###### Procedure for specifying the IP address yourself

To assign the IP address you have specified yourself to the IO device, follow these steps:

1. Open the Online and Diagnostics view of the IO device.
2. Select the "Assign IP address" group in the "Functions" folder.
3. Select the "Use IP parameters" option.
4. Enter the desired IP address.
5. Enter the subnet mask.
6. If a router is to be used, select the "Use router" check box and enter its IP address.
7. Click the "Assign IP address" button.

###### Procedure for obtaining the IP address from a DHCP server

To assign an IP address specified by a DHCP server to the IO device, follow these steps:

1. Open the Online and Diagnostics view of the IO device.
2. Select the "Assign IP address" group in the "Functions" folder.
3. Select the "Obtain IP address from a DHCP server" option.
4. If the DHCP server is to identify the target device using its client ID, choose the "Client ID" option. Enter the client ID in the entry field of the same name.
5. Alternatively: If the DHCP server is to identify the target device using its MAC address, choose the "MAC address" option
6. Alternatively: If the DHCP server is to identify the target device using its device name, choose the "Device name" option.
7. Click the "Assign IP address" button.

**Note**

The client ID is a string with a maximum of 63 characters. Only the following characters may be used: a-z, A-Z, 0-9 and - (hyphen)

**Note**

If you specify that the DHCP server is to identify the target device using its device name, you must have assigned a device name to the target device beforehand.

###### Result

The IP address is permanently assigned to the IO device. It is retained even through a startup or a power failure.

---

**See also**

[Retentivity of IP address parameters and device names](Configuring%20devices%20and%20networks.md#retentivity-of-ip-address-parameters-and-device-names)
  
[Displaying accessible devices](Using%20online%20and%20diagnostics%20functions.md#displaying-accessible-devices)

##### Starting the address assignment from the project context (S7-300, S7-400)

###### Requirement

- An online connection to the PROFINET IO device exists.
- You have opened the Online and Diagnostics view of the PROFINET IO device from the project context.

###### Procedure

1. Open the "Functions" folder and the "Assign IP address" group inside this folder. The "Use IP parameters" option is selected.
2. Click the "Accessible devices" button in order to identify the devices that can be accessed via MAC addresses. After the search is complete, select the IO device with the MAC address known to you.
3. Click the "Assign IP address" button.

###### Result

The IP address is permanently assigned to the IO device. It is retained even through a startup or a power failure.

---

**See also**

[Retentivity of IP address parameters and device names](Configuring%20devices%20and%20networks.md#retentivity-of-ip-address-parameters-and-device-names)

## Connection diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Detailed connection diagnostics (S7-300, S7-400)](#detailed-connection-diagnostics-s7-300-s7-400)

### Detailed connection diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Determining the connection details of an NCM connection (S7-300, S7-400)](#determining-the-connection-details-of-an-ncm-connection-s7-300-s7-400)

#### Determining the connection details of an NCM connection (S7-300, S7-400)

##### Where do I determine the connection details of an NCM connection?

The connection details of an NCM connection can be found in the "Connection details" group. This group is located in the "Diagnostics &gt; Connection information" area of the Inspector window.

##### When is the "Connection details" group filled in?

The following requirements must be met to fill in the "Connection details" group on the "Connection information" tab:

- There is an online connection to the relevant module.
- You have selected a line in the connection table.

##### Structure of the "Connection details" group for an NCM connection

In case of an NCM connection, the "Connection details" group consists of the following elements:

- Local connection ID (hex)
- Connection name
- Connection status
- Send status
- Receive status
- Number of bytes sent
- Number of bytes received
- "Special diagnostics" button

  Click this button to start the NCM connection diagnostics.

---

**See also**

[Starting NCM S7 diagnostics (S7-300, S7-400)](#starting-ncm-s7-diagnostics-s7-300-s7-400)
