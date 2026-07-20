---
title: "SIMOCODE ES"
package: SiriusSMCenUS
topics: 212
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMOCODE ES

This section contains information on the following topics:

- [What's new?](#whats-new)
- [General information](#general-information)
- [Device configuration](#device-configuration)
- [Openness for SIMOCODE pro](#openness-for-simocode-pro)
- [Online & diagnostics](#online-diagnostics)
- [Parameterization of the modules](#parameterization-of-the-modules)
- [Commissioning](#commissioning)
- [Configuring the communication interface](#configuring-the-communication-interface)
- [CFCs](#cfcs)
- [Migrating project files, upgrading a SIMOCODE pro project](#migrating-project-files-upgrading-a-simocode-pro-project)
- [Mass engineering](#mass-engineering)
- [Taking over the standard connection path of SIRIUS PROFINET & Ethernet/IP devices in the project](#taking-over-the-standard-connection-path-of-sirius-profinet-ethernetip-devices-in-the-project)
- [Importing and exporting parameters](#importing-and-exporting-parameters)
- [Device comparison with the TIA Portal comparison editor](#device-comparison-with-the-tia-portal-comparison-editor)
- [Default print settings](#default-print-settings)
- [Additional information](#additional-information)

## What's new?

The following new features are available for SIMOCODE ES V18 in the TIA Portal:

- With the Compare Editor of the TIA Portal, you compare the parameterization of two configured SIMOCODE pro devices in the offline project.
- SIMOCODE ES supports the CAx export (*.aml file format) in the TIA Portal for the device parameters.
- In the function charts, you can set the signal states of inputs for the active function test "cold start" and, in this way, test the device function.
- The parameter editor now provides you with text boxes for notes for the logic functions (truth tables, signal conditioning, and calculators), which are also considered during printing.
- For SIMOCODE ES, set the standard connection path for all devices in the project in the TIA settings under Online & Diagnostics. A fast bulk download or online mode is achieved.
- The SIMOCODE pro V PROFIBUS devices are now designated as SIMOCODE pro V PB.
- General improvement of tooltips and labeling
- Editorial improvements in the help system of SIMOCODE ES.
- The stability when working with the TIA Portal has been improved, among other things based on feedback from returned crash reports.

## General information

This section contains information on the following topics:

- [Manual Collection](#manual-collection)
- [SIMOCODE ES - Online Help](#simocode-es---online-help)
- [Security information](#security-information)
- [Information on data protection](#information-on-data-protection)

### Manual Collection

A [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951), a collection of the following five SIMOCODE pro manuals is at your disposal in Industry Online Support:

- SIMOCODE pro - 1 Getting Started
- SIMOCODE pro - 2 System Manual
- SIMOCODE pro - 3 Parameterization
- SIMOCODE pro - 4 Applications
- SIMOCODE pro - 5 Communication

### SIMOCODE ES - Online Help

SIMOCODE ES is a TIA Portal-based software tool for configuring, parameterizing, commissioning and diagnosing SIMOCODE pro switching devices.

For every SIMOCODE ES dialog box, there is a help topic in the Online Help. Some of the topics are very extensive. Reference is made to further information at many points.

#### Representation of default values

1. Default values are displayed in bold type  
   Range: 5, **10**, 15, 20, 25, 30, 35, 40
2. Default values have an additional "Default" line  
   Range: 0 to 100%  
   Default setting: **40 %**

#### "Additional information" folder

The Online Help contains an "Additional information" folder that includes the following information:

- Configuring example: reversing starter
- Table of the active control stations, contactor controls and lamp controls
- Different examples
- Different data sets

#### Manual Collection SIMOCODE pro and SIMOCODE pro manuals

> **Note**
>
> Observe the operating instructions / manuals for the components used.
>
> You will find the Manual Collection SIMOCODE pro and SIMOCODE pro manuals in the Internet:
>
> [Operating instructions / manuals](http://support.automation.siemens.com/WW/view/en/20369671/133300)

### Security information

Siemens provides products and solutions with industrial security functions that support the secure operation of plants, systems, machines and networks.

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial security concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For additional information on industrial security measures that may be implemented, please visit   
https://www.siemens.com/industrialsecurity.

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates, subscribe to the Siemens Industrial Security RSS Feed under   
https://www.siemens.com/cert.

### Information on data protection

Siemens observes standard data protection principles, in particular the principle of privacy by design.

For SIMOCODE ES this means:

SIMOCODE ES does not process or store any personal data, only technical function data (e.g. time stamps). If you link this data with other data (e.g. shift schedules) or store personal data on the same storage medium (e.g. hard disk), and thus establish a link to a person or persons, then you are responsible for ensuring compliance with the relevant data protection regulations.

## Device configuration

This section contains information on the following topics:

- [Device configuration dialog box](#device-configuration-dialog-box)
- [Updating the module description](#updating-the-module-description)

### Device configuration dialog box

This dialog box gives you an overview of the device configuration. You can use this for system documentation purposes, for example.

#### Basic unit

Select a basic unit from the following versions:

- SIMOCODE pro C basic unit: Select V1.0 or V2.0
- SIMOCODE pro S basic unit: Select V1.0
- SIMOCODE pro V PB basic unit: Select V1.1, V2.0, V3.0, V3.1, V3.2, V4.0 or V4.1
- SIMOCODE pro V MR basic unit: Select V1.0 or V2.0
- SIMOCODE pro V PN basic unit: Select V1.0, V1.1, V1.2, V2.0, or V2.1
- SIMOCODE pro V PN GP basic unit: Select V2.1
- SIMOCODE pro V EIP basic unit: Select V1.0 or V1.1

In doing so, you define the supported range of functions/parameters of the basic unit, and any additional modules.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Replacing a basic unit**  You can replace a basic unit with another basic unit using the shortcut menu.  It is not possible to delete a basic unit used in the device configuration. |  |

#### Thermistor

The basic units provide the option of connecting thermistor sensors (binary PTC) for monitoring the motor temperature. Activate the checkbox ☑ when you want to use this option. If the checkbox is activated, the [Thermistor](#thermistor-protection) dialog box is additionally set up in the "Motor protection" folder. You can edit the thermistor parameters there.

#### Modules

The planned modules can be selected here if, for example, you create a parameter file prior to commissioning without SIMOCODE pro. If you have already established a connection with SIMOCODE pro, you can read in the existing configuration. The modules are thus set accordingly in this dialog.

- Current measurement: Select the current measuring module with the correct current range here, if applicable.
- Digital module 1: Specify here whether a digital module with monostable, bistable or safety outputs (DM-F Local or DM-F PROFIsafe) is to be used.

  > **Note**
  >
  > The fail-safe digital modules DM-F Local and DM-F PROFIsafe can be activated from firmware version V3.0 of the SIMOCODE pro V PB basic unit or from firmware version V1.0 of the SIMOCODE pro V PN basic unit.

  > **Note**
  >
  > Only in the device configuration must a DM-F module always be inserted in Slot 2. The hardware configuration can vary.

  > **Note**
  >
  > **Parameter assignment of F parameters for the DM-F PROFIsafe**
  >
  > Requirement for parameter assignment of F parameters for DM-F PROFIsafe:
  >
  > - STEP7
  > - SIMATIC STEP7 Safety package.
  >
  > Note:
  >
  > - If the SIMATIC Step7 Safety package is not installed, a corresponding notice appears under the "General" tab in the inspector window. In this case:
  >
  >   - The "F Parameters" menu is not available
  >   - The DM-F PROFIsafe can be configured like a standard digital module.
  > - If you would like to load a SIMOCODE pro device configuration with the DM-F PROFIsafe digital module without this device being networked with a F-PLC, set "Safety mode" under the "General" tab to "0" in order to load this configuration into SIMOCODE pro. In this case the DM-F PROFIsafe operates in standard mode. By deactivating "Safety mode" the following settings are performed automatically:
  >
  >   - The F destination address is set to 0
  >   - The F parameter signature (without address) is set to 0
  >   - The manual assignment of the DB number is set to 0
  >   - The F-I/O DB number is set to 0
  >   - The fail-safe icon next to the DM-FP disappears
- Digital module 2: Specify here whether a digital module with monostable or bistable outputs is to be used.
- Operator panel: Specify here whether an operator panel is to be used.
- Voltage measurement: Specify here whether a current / voltage measuring module is to be used for monitoring the voltage, the frequency, the output, the power factor (cos phi) or the active power.
- Voltage display: Select "Phase voltage" or "Line-to-line voltage" here (default setting: phase voltage). Can only be activated:

  - From firmware version = V3.0 of the SIMOCODE pro V basic unit or
  - From firmware version = V1.0 of the SIMOCODE pro V PN basic unit and
  - If a current/voltage acquisition module has been selected.
- Temperature module 1/2. Choose here whether or not a temperature module is to be used for temperature monitoring (e.g. for monitoring the motor windings, motor bearings, coolant temperature, or gearbox temperature). Temperature module 2 can only be activated if temperature module 1 has been configured.
- Analog module 1/2: Choose here whether the analog signals of a transducer (standardized output signal 0/4 - 20 mA) are to be monitored. Analog module 2 can only be activated if analog module 1 has been configured.
- Ground-fault module: Select here whether external ground-fault monitoring is to be used via a residual current transformer and a ground-fault module. External ground-fault monitoring is normally used for networks that are grounded with high impedance.
- Ground-fault module. Select here whether external ground-fault monitoring is to be used via a residual current transformer and a ground-fault module. If yes, select

  - The 3UF500 ground-fault module (in conjunction with the 3UL22 residual current transformer)
  - The 3UF7510 ground-fault module (in conjunction with the 3UL23 residual current transformer)
  - The multifunctional module (only with SIMOCODE pro S basic unit in conjunction with the 3UL23 residual current transformer).
  > **Note**
  >
  > - The 3UL23 residual current transformer is suitable for detecting pure AC fault currents and AC fault currents with a pulsating direct current component.
  > - Requirement for using a 3UF7510 ground-fault module: Use of this ground-fault module requires a SIMOCODE pro V PB basic unit with at least product version *E10* (from 09/2013), or a SIMOCODE pro V PN basic unit with at least product version *E04* with firmware version V1.1.
  > - Requirements for using a 3UF7500 ground-fault module: Use of this ground-fault module requires a SIMOCODE pro V PB basic unit with at least product version *E02* (from 04/2005), or a SIMOCODE pro V PN basic unit with at least product version *E04* with firmware version V1.1.

  The external ground-fault monitoring is normally used in the following cases:

  - Where power systems are grounded with high impedance
  - Where precise measurement of the ground fault current is necessary, e.g. for the purpose of condition monitoring

  | Symbol | Meaning |
  | --- | --- |
  |  | **Danger** |
  | **No personal or fire protection!**  The 3UF75* ground-fault modules monitor that devices and systems are functioning correctly.  They are not suitable for personnel protection and fire protection. |  |

#### Configuration error because of missing operator panel

Normally, a missing configured operator panel results in the error message "Configuration error". If the operator panel is only periodically connected with the system, for example, you can prevent the error message by deactivating the checkbox ☑. The operator panel can be disconnected during operation without tripping.

> **Note**
>
> If the operator panel is the motor's only active control station, it may be the case that the motor can no longer be shut down.

#### Application (control function)

Select the application (control function) for which parameters are to be set (see [Application selection](#application-selection)).

> **Note**
>
> If you modify the application (control function) at a later date, this can, under certain circumstances, result in indirect parameter changes, in other words, parameters that do not exist for the newly selected control function will be set to "not connected" or to default values.

### Updating the module description

Updating the module description means upgrading devices to the latest version while keeping the current parameterization and device configuration.

- In the device configuration, select the module for which you would like to change the module description
- In the inspector window select the "General" tab
- Click on the button "Update module description".

You will also find general information about this topic in the information system under "Editing devices and networks → Configuring devices and networks → Configuring devices → Update module description".

## Openness for SIMOCODE pro

This section contains information on the following topics:

- [Openness - Fundamentals](#openness---fundamentals)
- [Openness - detailed information](#openness---detailed-information)

### Openness - Fundamentals

Basic information on the topic of TIA Portal Openness can be found in the TIA information system (via key F1) under "Openness: Automating creation of projects".

In addition to basic functions such as the creation of projects and the adding and configuring of SIMOCODE pro devices, you can also access all the device-specific parameters of SIMOCODE pro with Openness.

This gives users who have already specified the configuration and parameterization of the devices using other engineering tools outside the TIA Portal the opportunity to completely configure them via the Openness interface, and to access all or selected device parameters such as communication settings, motor protection, control function, assignment of the device inputs and outputs, etc.

### Openness - detailed information

You can detailed information about TIA Portal Openness in the Industry Online Support:

- **Application example "Automatically configuring hardware parameters with TIA Portal Openness"** ([Automatically configuring hardware parameters with TIA Portal Openness](https://support.industry.siemens.com/cs/ww/en/view/109771601)**):**
- **Manual "TIA Portal Openness Hardware parameters"**

  This manual (Openness_hardware_parameter_description.pdf) is stored in the following installation directories: Programs\Siemens\Automation\Portal V[Version]\PublicAPI\V[Version]\HW Parameter Description

  You can find the SIMOCODE pro hardware parameters in chapter "Head modules 3UF7 0** - any Version".
- **System Manual "SIMATIC Openness: Automating creation of projects".** 
  [SIMATIC Openness: Automating creation of projects](https://support.industry.siemens.com/cs/ww/en/view/109477163)
- **System Manual "SIMATIC Automating projects with scripts":**
  [SIMATIC Automating projects with scripts](https://support.industry.siemens.com/cs/pl/en/view/109755218)

You can request an example project for SIMOCODE pro in the Industry Online Support using a Support Request form (subject: TIA Portal Openness request):

| Symbol | Meaning |
| --- | --- |
| **Support Request** **:** | [Internet](https://support.industry.siemens.com/My/ww/en/requests) |

## Online & diagnostics

This section contains information on the following topics:

- [Diagnostics status](#diagnostics-status)
- [Diagnostic and comparison status display](#diagnostic-and-comparison-status-display)

### Diagnostics status

#### Status of the device diagnostics

Select **Devices > Project → S​IMOCODE​ → Commissioning** in the Project navigation view.

Diagnostics dialog boxes:

- Control/status information
- Faults
- Warnings
- Status information
- Measured values
- Service data/statistical data
- Error buffer/error protocol
- Test
- Command
- Password
- Actual configuration
- Analog value recording
- Hardware inputs and outputs
- Live trend
- Parameter comparer

#### Structure of the diagnostics dialog boxes

- Faults and warnings are indicated using colored icons.   
  The colors are defined according to system technology (e.g. red for fault/error).
- Status information is output in the form of lists
- Service data / statistical data are output in edit fields
- Recorded values are displayed under live trend in a curve control
- Faults and warnings that belong together are grouped

---

**See also**

[Live trend (display online values)](#live-trend-display-online-values)
  
[Parameter comparer](#parameter-comparer)

### Diagnostic and comparison status display

When setting up the online connection to a device, the following diagnostic/operating states are displayed using various symbols:

- The diagnostic status of the device
- The diagnostic status of its subordinate components
- If necessary, the operating state of the device

These symbols can be found in chapter [Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons).

If SIMOCODE ES and STEP7 are installed in parallel, two further diagnostic symbols are available:

- Split symbol ![Figure](images/148918551563_DV_resource.Stream@PNG-de-DE.png) : This is displayed if only the PLC is online via the TIA Portal
- Discrepancy symbol ![Figure](images/148918560267_DV_resource.Stream@PNG-de-DE.png) : This is displayed if both the PLC and the SIMOCODE device are online and their diagnostic information does not match on the SIMOCODE device

## Parameterization of the modules

This section contains information on the following topics:

- [Identification](#identification)
- [Device parameters](#device-parameters)
- [Device configuration](#device-configuration-1)
- [Motor protection](#motor-protection)
- [Dry-running protection of centrifugal pumps based on active power monitoring](#dry-running-protection-of-centrifugal-pumps-based-on-active-power-monitoring)
- [Motor control](#motor-control)
- [Monitoring functions](#monitoring-functions)
- [Inputs](#inputs)
- [3UF50 compatibility mode](#3uf50-compatibility-mode)
- [Analog value recording](#analog-value-recording)
- [Outputs](#outputs)
- [Standard functions](#standard-functions)
- [Logic modules](#logic-modules)
- [Libraries](#libraries)
- [Display of all parameters](#display-of-all-parameters)
- [Display of the basic parameters](#display-of-the-basic-parameters)
- [Expert list](#expert-list)
- [Device wizard, Parameter wizard](#device-wizard-parameter-wizard)
- [Automatic generation of I/O variables](#automatic-generation-of-io-variables)

### Identification

This section contains information on the following topics:

- [Device](#device)
- [Marking](#marking)

#### Device

The dialog box provides you with an overview of device-specific information. You can use the overview for system documentation purposes, for example.

In the Project Navigation Devices view, you call up the device data with the menu command **"Project → S​IMOCODE​ → Parameter → Identification**".

Device

| Information | Meaning |
| --- | --- |
| Article number | Article number (MLFB) of the device (MLFB = machine-readable product designation) |
| Short code | Short code of the device |
| Vendor | SIEMENS AG |
| Device family | Name of the higher-level device family, e.g. switching devices |
| Device subfamily | Name of the subfamily subordinate to the device family, e.g. motor management system |

#### Marking

You can freely edit the following product descriptions:

- Plant identifier
- Location designation
- Installation date
- Description.

You can use these descriptions for system documentation purposes, for example. The data is read out directly from the switching device, or from the device via online connection.

You have a total of 124 characters available.

### Device parameters

This section contains information on the following topics:

- [Fieldbus interface](#fieldbus-interface)
- [PROFIBUS address](#profibus-address)
- [Modbus parameters](#modbus-parameters)
- [PROFINET parameters](#profinet-parameters)
- [Ethernet IP parameters](#ethernet-ip-parameters)
- [F parameters for the fail-safe digital module DM-F PROFIsafe](#f-parameters-for-the-fail-safe-digital-module-dm-f-profisafe)

#### Fieldbus interface

> **Note**
>
> An address reassignment is active immediately following the download to the device!

##### Station address

The addresses of all devices connected to the bus must be unique, i.e. each address can be assigned only once to a single unit. A device with factory settings has the address 126.

Range: 1 to 126

##### PROFIsafe address

Displays the set PROFIsafe address.

> **Note**
>
> At this point, only the PROFIsafe address set on the module is displayed in the online representation.  
> The PROFIsafe address must be set directly via the DIP switch of the PROFIsafe digital module!

The Profisafe address for the DM-FP module is configured under "Devices & Networks".

##### Transmission speed

Possible baud rates:

- With SIMOCODE pro V up to 12 Mbit/s
- With SIMOCODE pro S up to 1.5 Mbit/s

The device automatically detects the baud rate on PROFIBUS DP.

##### Startup parameter block

Activate this parameter with the checkbox ☑.

With this parameter, you instruct SIMOCODE pro to ignore all parameter data sent to the individual devices at startup of the IO controller. The current parameter data that SIMOCODE pro has saved are not overwritten in this case. When "Startup parameter block" is activated, you can only change the parameter data by transferring new parameters directly to the device with SIMOCODE ES.

Default setting:

Activated

- When parameterizing directly in SIMOCODE ES

Not activated

- After executing the "Factory settings" command in the online "Command" dialog
- When integrating via STEP 7

##### Diagnostics

By selecting the corresponding checkbox, you can specify which diagnostics data are to be signaled via PROFIBUS:

- Diagnostics triggered by device faults
- Diagnostics triggered by trips
- Diagnostics triggered by warnings
- Diagnostics triggered by events

---

**See also**

[Configuring the diagnostics response](#configuring-the-diagnostics-response)

#### PROFIBUS address

##### Bus parameters

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Assigning a new address**  When changing the PROFIBUS address, the online connection to PROFIBUS is interrupted. Restore the online connection after changing the address. The new address is active after downloading to the device. |  |

##### Station address

The addresses of all devices on the bus must be unique. Each address can only be assigned once to one device.

> **Note**
>
> **Factory settings - address 126**
>
> - A device with factory settings has the address 126
> - PROFIBUS address 126 is not a valid address.
> - Downloading with PROFIBUS address 126 is not possible.
>
> Change the address after prompting.
>
> Setting range: 1 to 125**.**

> **Note**
>
> **Changing the address with PROFIBUS connection**
>
> - Search for the device under online accesses with your PROFIBUS adapter
> - Change PROFIBUS address 126 in the Parameter Editor
> - Click on the ![Station address](images/148918651403_DV_resource.Stream@PNG-de-DE.png) button "Transfer online data to the hardware"
>
> Otherwise:
>
> - Go online with the SIMOCODE pro in the project
> - Change address 126
> - Click on the ![Station address](images/148918651403_DV_resource.Stream@PNG-de-DE.png) button "Transfer online data to the hardware".

##### Transmission speed

Baud rates up to 12 Mbit/s are possible. The device automatically detects the baud rate on PROFIBUS DP.

#### Modbus parameters

**Baud rate**

The baud rate of SIMOCODE pro V Modbus can be set in the range from 0.3 ... 57.6 kBit/ s. With the "auto" parameter setting the automatic baud rate detection is activated with which the device autonomously determines the setting selected by the controller. The automatic baud rate search covers baud rates in the range from 4.8 ... 57.6 kBaud.

> **Note**
>
> **Automatic baud rate detection**
>
> Use of this function is only possible when the "Watchdog" function is activated.

**Baud rate (detected)**

Information about the detected baud rate if automatic baud rate detection (baud rate = auto) is set.

**Modbus address**

Sets the Modbus address for the SIMOCODE device. The address can be set in the range from 1 ... 247. When the SIMOCODE pro devices leave the factory, the address is set to the default value of 126.

**Interface configuration**

The number of stop bits and the selected parity of the Modbus interface can be set here. The following settings are possible:

- 8E1 - 1 stop bit, even parity
- 8O1 - 1 stop bit, odd parity
- 8N2 - 2 stop bit, no parity
- 8N1 - 1 stop bit, no parity

**Wait time / Wait time (default value)**

With the "wait time" and "wait time (default value)" parameters you can set the duration of the pause between a received request and the response by SIMOCODE pro. If the default value of the Modbus specification is to be used, it is recommended to choose the "wait time (default value)" parameter. The "wait time" parameter is available for free setting. The setting is in ms. The smallest value that can be set corresponds to the default value of the Modbus specification. If longer wait times are required these can be defined with the "wait time" parameter.

**Watchdog / Watchdog time**

With these parameters you can activate monitoring of the bus communication. This is necessary if automatic baud rate detection is selected or if the SIMOCODE device is to go into the fault state when the bus communication of the SIMOCODE device fails. If the watchdog is activated, SIMOCODE monitors whether a valid read or write access to the device takes place within the set watchdog time. If this is not the case, SIMOCODE starts a new search for a valid baud rate in the case of automatic baud rate detection. What is more, a "Fault - bus" is generated if the "Watchdog → Bus monitoring" parameter is also activated.

#### PROFINET parameters

**PROFINET parameters (settings under Parameter → PROFINET parameters)**

****MAC address****

Each PROFINET device is assigned a globally unique device identification at the factory. This 6-byte device identifier is the MAC address.

The MAC address is divided up as follows:

- 3-byte manufacturer identification and
- 3-byte device identification (consecutive number).

The MAC address can generally be read from the front of the device, e.g.: 08-00-06-6B-80-C0.

The device can be reached via LAN using this address.

##### **IP parameters**

The IP parameters, consisting of IP address, subnet mask, and gateway (router) can also be assigned in various ways and transferred to the IO Device.

Possibilities for this are:

- The IO controller assigns the IP parameters to the IO device. In this case, "Overwrite IP parameters in device" must not be selected.
- The IP parameters are obtained from a DHCP server and assigned to the IO Device. In this case, "Overwrite IP parameters in device" must not be selected.
- The IP parameters are configured with SIMOCODE ES and transferred to the device. In this case, the "Overwrite IP parameters in device" checkbox must be selected. Choose the IP parameters to match the configuration in the automation system. If the IP parameters are assigned by the IO controller in the automation system, no setting is necessary here and the "Overwrite IP parameters in device" checkbox must not be selected.

  > **Note**
  >
  > **Initial transfer of device name**
  >
  > The initial transfer of the device name must take place via the SIMOCODE pro system interface, since the device cannot be reached via PROFINET as address settings are missing.

**IP address, subnet mask**

To enable a PROFINET device to be addressed as a node on Industrial Ethernet, this device also requires an IP address that is unique within the network.

The IP address is made up of 4 decimal numbers with a range of values from 0 through 255. The decimal numbers are separated by a decimal point. The IP address is composed of the address of the (sub)net and the address of the node (generally also called a host or network node).

**Gateway:**

- No: Do not use a router
- Yes: Use a router
- Address (gateway): Router address

##### Station

> **Note**
>
> **Initial transfer of device name**
>
> The initial transfer of the device name must take place via the SIMOCODE pro system interface, since the device cannot be reached via PROFINET as address settings are missing.

- Device name: Select the PROFINET device name to match the configuration in the automation system.
- Station type: Shows the station type, e.g. motor mgmt. system
- Baud rate: Settable.

##### **OPC-UA server - Web server**

- OPC-UA server activated: In the default setting, the OPC-UA server is "not active". To activate the OPC-UA server, the checkbox "OPC-UA server activated" must be selected.
- Web server activated: The default setting of the web server is "not active." To activate the web server, the checkbox "Web server activated" must be selected.
- User name: Enter a user name when web server is activated
- Password: Enter a password when web server is activated
- Password confirmation: Confirm the password.

##### NTP procedure - Synchronization

- Activate NTP synchronization: Select this checkbox if you want to synchronize the unbuffered real-time clock of SIMOCODE pro V PN using the NTP procedure.
- NTP server address: Enter the NTP server address when the "Activate NTP synchronization" checkbox is selected
- Time shift: Enter a value for the time shift: -1440 min to +1440 min (default setting: 0 min).
- Cyclic update interval: Enter a value for the cyclic update interval when the "Activate NTP synchronization" check box is selected: 10 to 86400 s (default setting: 10 s)

##### Startup parameter block

The startup parameter block prevents transfer of SIMOCODE pro parameters that can be transferred from the IO controller during startup.

Activate/deactivate the startup parameter block via the "Startup parameter block" checkbox.

- **Parameterization with SIMOCODE ES:** The startup parameter block must always be set for this form of parameterization to avoid the device parameters from being overwritten by any existing parameter data during startup.
- **Parameter data during startup:** To enable device parameterization to be carried out during startup, the startup parameter block must not be set. SIMOCODE pro is then parameterized with the device-specific parameters stored. Any parameters already in the device will be overwritten.

  > **Note**
  >
  > **The startup parameter block is not active in the following cases:**
  >
  > - Device is as supplied
  > - Following execution of the command "Factory settings" under "Commissioning → Command"

##### Diagnostics

By selecting the corresponding checkbox, you can specify which diagnostic data are to be signaled via PROFINET:

- Diagnostics triggered by device faults
- Diagnostics triggered by trips
- Diagnostics triggered by warnings
- Diagnostics triggered by events.

---

**See also**

[Configuring the diagnostics response](#configuring-the-diagnostics-response)

#### Ethernet IP parameters

##### **IP parameters**

The IP parameters, consisting of IP address, subnet mask, and gateway (router) can also be assigned in various ways and transferred to the IO Device.

Possibilities for this are:

- The IO controller assigns the IP parameters to the IO device. In this case, "Overwrite IP parameters in device" must not be selected.
- The IP parameters are obtained from a DHCP server and assigned to the IO Device. In this case, the "Use BOOT/DHCP" checkbox must be selected. If the DHCP mode is selected, SIMOCODE pro immediately receives an IP address if the DHCP server is available in the same network. Otherwise the device searches for an IP address. If SIMOCODE pro finds no IP address when setting up an online connection or during a loading operation, because no DHCP server is available in the network, SIMOCODE ES assigns the device a temporary IP address. If the DHCP mode is selected, SIMOCODE pro accepts this temporary address as if it came from a DHCP server. There are two options for deactivating a temporary IP address again:

  - Restart the device by means of "Commissioning → Command → Restart/Cold start"
  - Switch the device off and on again. After the restart, the device runs in the DHCP mode and looks for an IP address again.
- The IP parameters are configured with SIMOCODE ES and transferred to the device. In this case, the "Overwrite IP parameters in device" checkbox must be selected. Choose the IP parameters to match the configuration in the automation system. If the IP parameters are assigned by the IO controller in the automation system, no setting is necessary here and the "Overwrite IP parameters in device" checkbox must not be selected.

  > **Note**
  >
  > **Initial transfer of device name**
  >
  > The initial transfer of the device name must occur via the SIMOCODE pro system interface, since the device is not yet accessible via EtherNet/IP due to the missing address settings.

**IP address, subnet mask**

To enable an EtherNet/IP device to be addressed as a node on Industrial Ethernet, this device also requires an IP address that is unique within the network.

The IP address is made up of 4 decimal numbers with a range of values from 0 through 255. The decimal numbers are separated by a decimal point. The IP address is composed of the address of the (sub)net and the address of the node (generally also called a host or network node).

**Gateway:**

- No: Do not use a router
- Yes: Use a router
- Address (gateway): Router address

##### Station

> **Note**
>
> **Initial transfer of device name**
>
> The initial transfer of the device name must occur via the SIMOCODE pro system interface, since the device is not yet reachable via EtherNet/IP due to the missing address settings.

- Device name: Select the EtherNet/IP device name to match the configuration in the automation system.
- Station type: Shows the station type, e.g. motor mgmt. system
- Baud rate: Settable.

##### **Web server**

- Web server activated: The default setting of the web server is "not active." To activate the web server, the checkbox "Web server activated" must be selected.

##### NTP procedure - Synchronization

- Activate NTP synchronization: Select this checkbox if you want to synchronize the unbuffered real-time clock of SIMOCODE pro V EIP using the NTP procedure.
- NTP server address: Enter the NTP server address when the "Activate NTP synchronization" check box is selected.
- Time shift: Enter a value for the time shift: -1440 min to +1440 min (default setting: 0 min).
- Cyclic update interval: Enter a value for the cyclic update interval when the "Activate NTP synchronization" checkbox is selected: 10 to 86400 s (default setting: 10 s)

#### F parameters for the fail-safe digital module DM-F PROFIsafe

The settings of the F parameters for the fail-safe digital module DM-F PROFIsafe are made in the Inspector window under the "General" tab.

Procedure: See [Device configuration dialog box](#device-configuration-dialog-box).

### Device configuration

This section contains information on the following topics:

- [Application selection](#application-selection)

#### Application selection

If you select and load a preset application (e.g. the reversing starter) in SIMOCODE ES, all protective functions, links and interlocks for the reversing starter are set up in the basic unit.

You can choose here between the following control functions depending on the basic unit used:

| Symbol | Meaning |
| --- | --- |
| **Control function** | **Brief description** |
| Overload relay | SIMOCODE pro behaves like an overload relay. |
| Direct starter | Switching motors on and off |
| Reversing starter | Controlling the direction of rotation of motors (clockwise, counter-clockwise) |
| Molded case circuit breaker (MCCB) | Switching a circuit breaker on and off (e.g. 3WL, 3VL) |
| Star-delta starter | To limit the starting current, SIMOCODE pro initially starts the motor with a star-connected stator winding and then switches it to delta. |
| Star-delta reversing starter | Star-delta starter with both directions of rotation (clockwise, counter-clockwise) |
| Dahlander starter | Controlling motors with only one stator winding in two speed stages (fast, slow) |
| Dahlander reversing starter | Dahlander starter with both directions of rotation (clockwise, counter-clockwise) |
| Pole-changing starter | Controlling motors with two stator windings in two speed stages (fast, slow) |
| Pole-changing reversing starter | Pole-changing starter with both directions of rotation (clockwise, counter-clockwise) |
| Solenoid valve | Activation of a solenoid valve |
| Positioner (1, 2, 3, 4, 5) | Activation of positioners or actuators. Versions 1 to 5 |
| Soft starter | Activation of the 3RW soft starter |
| Soft starter with reversing contactor | Activation of the 3RW soft starter including an additional reversing contactor. |

---

**See also**

[Control stations](#control-stations)
  
[Control function](#control-function)
  
[Libraries](#libraries)

### Motor protection

This section contains information on the following topics:

- [Motor protection introduction](#motor-protection-introduction)
- [Overload protection](#overload-protection)
- [Unbalance protection](#unbalance-protection)
- [Blocking protection](#blocking-protection)
- [Thermistor protection](#thermistor-protection)

#### Motor protection introduction

Topics and information on motor protection include:

- [Overload protection](#overload-protection-1)
- [Unbalance protection](#unbalance-protection)
- [Blocking protection](#blocking-protection)
- [Thermistor protection](#thermistor-protection)

##### Schematic:

The following schematic shows the "Extended Protection" function block ("Overload protection", "Unbalance protection" and "Stalled rotor protection") with optional parameter settings and events.

![Schematic:](images/152637438859_DV_resource.Stream@PNG-en-US.png)

1) Adjustable transformation ratio when using interposing transformers with SIMOCODE pro V for the SIMOCODE pro V PB basic unit, version *E03* and higher

##### Adjustable responses "Overload protection", "Unbalance protection" and "Stalled rotor protection"

| Response | Prewarning level "overload protection" | Trip level "overload protection" | Level "unbalance" | Level "stalled rotor protection" |
| --- | --- | --- | --- | --- |
| Deactivated | X | X | X | **X** |
| Signal | X | X | X | X |
| Warn | **X** | X | **X** | X |
| Trip | — | **X** | X | X |
| Delay | 0 - 25.5 s (**0.5 s**) | — | 0 - 25.5 s (**0.5 s**) | 0 - 25.5 s (**0.5 s**) |

> **Note**
>
> Deactivate unbalance protection in SIMOCODE ES when the load type is set to single-phase!

#### Overload protection

This section contains information on the following topics:

- [Overload protection](#overload-protection-1)
- [Set current Is1](#set-current-is1)
- [Set current Is2](#set-current-is2)
- [Application example](#application-example)
- [Further overload protection parameters](#further-overload-protection-parameters)

##### Overload protection

SIMOCODE pro protects three-phase or AC motors in accordance with IEC 60947-4-1 requirements. The trip class can be set to eight different settings ranging from Class 5E to Class 40E. Thus, the tripping time can be adapted precisely to the power-up behavior of the motor, improving utilization of the motor capacity. Additionally, the "Thermal motor model" and time to overload trip are calculated and made available to the control system. After an overload trip, the remaining cooling down period is displayed (see Class). The motor current is saved in the case of an overload trip.

Depending on the control function, the set current I<sub>s</sub> is separately parameterizable for one or two speeds (I<sub>s</sub>1 and I<sub>s</sub>2).

The rated motor current is usually set with **set current I**<sub>s</sub>**1**. This value can be found on the rating plate of the motor. The overload trip characteristic is calculated based on this value.

The **set current I**<sub>s</sub>**2** is only required for motors with two speeds to guarantee the appropriate overload protection for the higher speed too. Generally, I<sub>s</sub>2 should be set higher than I<sub>s</sub>1.

##### Set current Is1

###### Setting ranges for current setting l<sub>s</sub>1

Range: Depends on the selected current measuring module or current / voltage measuring module.

Current setting I<sub>s</sub>1 when using a current measuring module or a 1st generation current / voltage measuring:

- 0.3 to 3 A (default: 0.3)
- 2.4 to 25 A
- 10 to 100 A
- 20 to 200 A
- 63 to 630 A

Current setting I<sub>s</sub>1 when using a 2nd generation current / voltage measuring module:

- 0.3 to 4 A (default: 0.3)
- 3 to 40 A
- 10 to 115 A
- 20 to 200 A
- 63 to 630 A

###### Transformation ratio - active

When using an interposing transformer, or if the main supply cable is looped several times through the current measuring module or the current / voltage measuring module, you can enter the transformation ratio of the interposing transformer. Activate the checkbox if you wish to use this option. The parameterized current setting continues to correspond here to the actual rated motor current and does not have to be converted.

The transformation ratio is calculated from the ratio between the rated motor current [A] and the measured current [A] or any multiple of the ratio.

> **Note**
>
> This parameter is available only when SIMOCODE pro V PB product version *E03* or higher is used.

###### Transformation ratio - primary

Enter the primary current here, with the "Transformation ratio - active" checkbox activated. Range: 0 to 8191.875 (default: 0).

###### Transformation ratio - secondary

Enter the secondary current here, with the "Transformation ratio - active" checkbox activated. Range: 0 to 15 (default: 0).

##### Set current Is2

###### Setting ranges for current setting I<sub>s</sub>2

Range: Depends on the selected current measuring module or current / voltage measuring module.

Current setting I<sub>s</sub>2 when using a current measuring module or a 1st generation current / voltage measuring module:

- 0.3 to 3 A (default: 0.3)
- 2.4 to 25 A
- 10 to 100 A
- 20 to 200 A
- 63 to 630 A

Current setting I<sub>s</sub>1 when using a 2nd generation current / voltage measuring module:

- 0.3 to 4 A (default: 0.3)
- 3 to 40 A
- 10 to 115 A
- 20 to 200 A
- 63 to 630 A

###### Transformation ratio - active

When using an interposing transformer, or if the main supply cable is looped several times through the current measuring module or the current / voltage measuring module, you can enter the transformation ratio.

Activate the checkbox if you wish to use this option. The parameterized current setting continues to correspond here to the actual rated motor current and does not have to be converted.

The transformation ratio is calculated from the ratio between the rated motor current [A] and the measured current [A] or any multiple of the ratio.

> **Note**
>
> This parameter is only available when using SIMOCODE pro V PB above version *E03*.

###### Transformation ratio - primary

Enter the primary current here, with the "Transformation ratio - active" checkbox activated. Range: 0 to 8191.875 (default: 0).

###### Transformation ratio - secondary

Enter the secondary current here, with the "Transformation ratio - active" checkbox activated. Range: 0 to 15 (default: 0).

> **Note**
>
> In the case of motors with two speeds, the same or different transformation ratios can be set for each speed, depending upon whether the same or two different interposing transformers is/are used for each speed.

##### Application example

###### Example 1:

Rated motor current: 700 A.  
A 3UF18 68‑3G current transformer (205 to 820 A) is used as interposing transformer (transformation ratio 820 : 1), the secondary side is looped once through a current measuring module (0.3 A to 3 A):  
Transformation ratio for I<sub>s</sub> = 820 : 1; I<sub>s</sub> = 700 A

Settings (primary and secondary)

- Set current I<sub>s</sub>1: 700 A
- I<sub>s</sub>1 Transformation ratio primary: 820
- I<sub>s</sub>1 Transformation ratio secondary: 1

###### Example 2:

Rated motor current: 225 A.  
A 3UF1868‑3G current transformer (205 to 820 A) is used as interposing transformer (transformation ratio 820 : 1), the secondary side is looped twice through a current measuring module (0.3 A to 3 A):  
Transformation ratio for I<sub>s</sub> = 820 : 2; I<sub>s</sub> = 225 A

Settings (primary and secondary)

- Set current I<sub>s</sub>1: 225 A
- I<sub>s</sub>1 Transformation ratio primary: 820
- I<sub>s</sub>1 Transformation ratio secondary: 2

###### Example 3:

The motor cable is looped twice through a current measuring module (0.3 to 3 A, for a motor with a rated current of 0.25 A):  
Transformation ratio for I<sub>s</sub> = 1 : 2; I<sub>s</sub> = 0.25 A

Settings (primary and secondary)

- Set current I<sub>s</sub>1: 0.25 A
- I<sub>s</sub>1 Transformation ratio primary: 1
- I<sub>s</sub>1 Transformation ratio secondary: 2

##### Further overload protection parameters

###### Class

The Class (trip class) defines the maximum time within which SIMOCODE pro must trip from cold at 7.2 times the current setting I<sub>s</sub> (motor protection to IEC 60947). SIMOCODE pro meets the requirements of tolerance band E according to IEC / EN 60947-4-1 in respect of the accuracy of the tripping times. Please note that with startups > "Class 10E", the permissible AC3 current of the contactor may have to be reduced (derated), i.e. you must select a larger contactor.

**Overload characteristics for 2nd generation current / voltage measuring modules (e.g. 3UF7110-1AA01-0) and dry-running protection (e.g. 3UF712.-1.A01-0)**

The following graph shows the trip classes 5E, 7E, 10E (d), 15E, 20E, 25E, 30E, 35E and 40E for 3-pole balanced loads:

![Trip classes for 3-pole loads, 2nd generation current / voltage measuring modulesTrip classes for 3-pole loads, 2nd generation current / voltage measuring modules](images/144214688267_DV_resource.Stream@PNG-de-DE.png)

Trip classes for 3-pole loads, 2nd generation current / voltage measuring modules

The following graph shows the trip classes 5E, 7E, 10E (d), 15E, 20E, 25E, 30E, 35E, and 40E for 2-pole loads:

![Trip classes for 2-pole loads, 2nd generation current / voltage measuring modulesTrip classes for 2-pole loads, 2nd generation current / voltage measuring modules](images/144214692107_DV_resource.Stream@PNG-de-DE.png)

Trip classes for 2-pole loads, 2nd generation current / voltage measuring modules

**Overload characteristics for current measuring modules, 1st generation current / voltage measuring modules (e.g. 3UF7110-1AA00-0) and 2nd generation current / voltage measuring modules in compatibility mode (e.g. 3UF7110-1AA01-0)**

The following graph shows the trip classes 5E, 10E (d), 15E, 20E, 25E, 30E, 35E and 40E for 3-pole balanced loads:

![Trip classes for 3-pole balanced loads, current measuring modules and 1st generation current / voltage measuring modulesTrip classes for 3-pole balanced loads, current measuring modules and 1st generation current / voltage measuring modules](images/145230011147_DV_resource.Stream@PNG-de-DE.png)

Trip classes for 3-pole balanced loads, current measuring modules and 1st generation current / voltage measuring modules

The following graph shows the trip classes 5E, 10E (d), 15E, 20E, 25E, 30E, 35E, and 40E for 2-pole loads:

![Trip classes for 2-pole loads, current measuring modules and 1st generation current / voltage measuring modulesTrip classes for 2-pole loads, current measuring modules and 1st generation current / voltage measuring modules](images/145230014731_DV_resource.Stream@PNG-de-DE.png)

Trip classes for 2-pole loads, current measuring modules and 1st generation current / voltage measuring modules

> **Note**
>
> **Type of tripping characteristic**
>
> If a 1st generation 3UF711*-1AA00-0 current / voltage measuring module is configured in a parameterization, but a 2nd generation 3UF711*-1AA01-0 current / voltage measuring module is used, the tripping characteristic remains that of the 1st generation current / voltage measuring module.
>
> Merely replacing the measuring module hardware does not change the tripping behavior.

> **Note**
>
> **Tripping characteristics**
>
> The latest tripping characteristics for SIMOCODE pro can be found in [Siemens Industry Online Support (SIOS)](https://support.industry.siemens.com/cs/ww/en/ps). Enter the search term "3UF7" and filter for "characteristic" in the search area.

###### Response to overload

The SIMOCODE pro response to overload can be additionally adjusted here.

See "Tables of responses of SIMOCODE pro" in Chapter [Motor protection introduction](#motor-protection-introduction).

> **Note**
>
> With motors for Ex e applications, the response must remain set to "trip"!

###### Cooling down period

The cooling down period is the amount of time that must elapse before an overload trip can be reset. This is usually 5 minutes. The thermal memory (motor model – see below) is deleted after the cooling down period elapses. Supply voltage failures of SIMOCODE pro during this time extend the specified time correspondingly.

Range: 60 to 6553.5 s (default: 300 s).

###### Thermal motor model (thermal memory)

**"At operating temperature" state**

In the "at operating temperature" state, the tripping times are reduced by the factors listed in the table. These factors apply to 3-pole balanced loads, Class 5E to Class 40E.

Factors for trip times at operating temperature for 2nd generation current/voltage measuring modules

| x I<sub>s</sub> | Preload as a percentage of the current setting I<sub>s</sub> |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **20** | **40** | **60** | **80** | **100** |
| 2 | 0.97 | 0.89 | 0.75 | 0.54 | 0.24 |
| 3 | 0.97 | 0.88 | 0.73 | 0.51 | 0.22 |
| 4 | 0.97 | 0.88 | 0.72 | 0.51 | 0.22 |
| 5 | 0.97 | 0.88 | 0.72 | 0.51 | 0.21 |
| 6 | 0.96 | 0.87 | 0.72 | 0.50 | 0.21 |
| 7.2 | 0.96 | 0.88 | 0.72 | 0.50 | 0.22 |
| 8 | 0.97 | 0.87 | 0.72 | 0.50 | 0.22 |
| 9 | 0.98 | 0.87 | 0.72 | 0.51 | 0.21 |
| 10 | 0.97 | 0.87 | 0.74 | 0.50 | 0.21 |
|  |  |  |  |  |  |

When the rated motor current (Ie) is at 100%, the value "thermal motor model" is 79% in a steady state, and 100% at the moment of an overload trip.

Factors for trip times at operating temperature for current measuring modules and 1st generation current/voltage measuring modules and 2nd generation current/voltage measuring modules in compatibility mode.

| x I<sub>s</sub> | Preload as a percentage of the current setting I<sub>s</sub> |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **0** | **20** | **40** | **60** | **80** | **100** |
| 2 | 1 | 0.88 | 0.74 | 0.58 | 0.40 | 0.19 |
| 4 | 1 | 0.85 | 0.69 | 0.52 | 0.35 | 0.16 |
| 6 | 1 | 0.84 | 0.68 | 0.51 | 0.34 | 0.15 |
| 7.2 | 1 | 0.84 | 0.68 | 0.51 | 0.33 | 0.15 |
| 8 | 1 | 0.84 | 0.67 | 0.51 | 0.33 | 0.15 |

For the 1st generation, the following applies:

When the rated motor current (I<sub>s</sub>) is at 100%, the value "thermal motor model" is 87% in a steady state and 100% at the moment of an overload trip.

**Example of 1st generation devices:**

You have operated and switched off a motor with current setting 100 % I<sub>s</sub>.

You immediately switch the motor back on. This causes an overload trip with 2 x I<sub>s</sub>, Class 10E.

- Tripping time in cold state: approximately 40 s (acc. to tripping characteristic)
- Factor for tripping time with preload 100 % I<sub>s</sub>: 0.19 (see Table)
- Reduced tripping time: 0.19 x 40 s = 7.6 s.

###### Pause time

The pause time is the specified time for the cooling down response of the motor when tripped under normal operating conditions (not in the case of an overload trip). After this interval, the thermal memory in SIMOCODE pro is erased and a new cold restart is possible. This means that many startups can be performed in a short space of time.

The following schematic shows the cooling down response with and without pause time:

![Pause time](images/153049822219_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Both the motor and the switching devices must be dimensioned specifically for this load!

| Symbol | Meaning |
| --- | --- |
| Pause time: | 0 to 6553.5 s (default: 0) |

###### Load type

You can select whether SIMOCODE pro is to protect a 1-phase or a 3-phase load. For a 1-phase type of load, the internal ground-fault monitoring and the unbalance protection must be deactivated. Phase failure monitoring is deactivated automatically.

| Symbol | Meaning |
| --- | --- |
| Load type | 1-phase, 3-phase (default) |

> **Note**
>
> **Decoupling module**
>
> When using a 1st generation current / voltage measuring module a decoupling module may be necessary.
>
> See table "Decoupling module requirements for star networks" in Chapter 8.6 "Decoupling module (DCM) for 1st generation current/voltage measuring modules (e.g. 3UF711.1AA000)" in [SIMOCODE pro – System Manual](https://support.industry.siemens.com/cs/ww/en/view/109743957).

###### Delay prewarning

The "Delay" parameter (default: 0.5 s) defines the length of time for which the prewarning level (1.15 x I<sub>s</sub>) must be permanently exceeded before SIMOCODE pro will execute the desired response. If no setting is made, there will be no response. In the event of a loss of phase or an unbalance > 50%, the prewarning level will be reached earlier, at approximately 0.85 x I<sub>s</sub>.

###### Reset

If the "Reset" parameter is set to "Auto," the "Overload," "Overload + Unbalance," and "Thermistor" faults will be acknowledged automatically:

- If the cooling time has expired
- If the thermistor value has dropped back down to the specified resetting value

If the "Reset" parameter is set to "Manual", the faults must be acknowledged by a reset signal:

- "TEST/RESET" button on the basic unit
- "TEST/RESET" button on operator panel
- Standard functions "Reset"

For this, the "Reset - Input" (plugs) must be connected to the corresponding sockets, e.g. using reset via bus.

| Symbol | Meaning |
| --- | --- |
| Reset: | Manual, Auto (default: manual). |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected restart of the motor**  The "Auto-Reset" mode must not be used for applications where an unexpected motor restart may cause personal injury or damage to property. |  |

#### Unbalance protection

The extent of the phase unbalance can be monitored and transmitted to the control system. If a specified limit value is violated, a defined and delayable response can be initiated. If the phase unbalance is larger than 50%, the tripping time is also automatically reduced in accordance with the overload characteristic since the heat generation of the motors increases in asymmetrical conditions.

The phase unbalance is calculated using the following equation:

![Figure](images/148918965259_DV_resource.Stream@PNG-de-DE.png)

##### Level

The level of unbalance to which SIMOCODE pro should react is set here:

100 % (**40 %**)

##### Response

Here you can select the response of SIMOCODE pro to phase unbalance:

Deactivated, signal, **warn**, trip

##### Delay time

The unbalance level must be exceeded for the period of the set delay time before SIMOCODE pro executes the desired response. If no setting is made, there will be no response.

Setting range: 0 - 25.5 s (**0.5 s**)

#### Blocking protection

If the motor current rises above an adjustable stalled rotor protection level (current level), a definable and delayable response can be configured for SIMOCODE pro. In this case, for example, the motor can be shut down independently of the overload protection. The stalled rotor protection is only active after the parameterized class time has elapsed, e.g. for Class 10 after 10 seconds, and prevents unnecessarily high thermal and mechanical loads as well as premature aging of the motor.

##### Stalled rotor level

Here you can enter the value % of I<sub>s</sub> when the stalled rotor level is exceeded:

**0** – 1020% of I<sub>s</sub>

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Intermediate values**  Intermediate values are automatically rounded. |  |

##### Response to exceeding the stalled rotor level

You can select the response to overshoot of the stalled rotor level here:

**Deactivated**, signal, warn, trip

##### Delay

The "Delay" parameter determines the amount of time that the stalled rotor level must be permanently exceeded before SIMOCODE pro executes the desired response. If no setting is made, there will be no response.

Setting range: 0 – 25.5 s (**0.5 s**)

#### Thermistor protection

Thermistor protection is based on a direct temperature measurement in the motor via binary PTC thermistors which can be connected to the SIMOCODE pro C or SIMOCODE pro V basic unit.

Thermistor protection is used for:

- Motors with high switching frequencies
- Converter operation
- Motors with heavy starting
- Intermittent duty and/or braking operation
- Hampered air infeed
- Speeds below the rated speed.

In this case, the sensors are mounted in the winding slot or bearing of the motor.

##### Schematic

The following schematic shows the Thermistor logic module:

![Schematic](images/152638357643_DV_resource.Stream@PNG-en-US.png)

##### Response to overtemperature

Here you can select how SIMOCODE pro should respond when the temperature has overshot the trip level.

Signal, warn, **trip**

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Motors for EEx e applications**   With motors for EEx e applications, the response must be set to "Tripping"! |  |

##### Response to sensor fault

Here you can select the SIMOCODE pro response in the case of a short-circuit or a break in the thermistor sensor cable.

Deactivated, signal, **warn**, trip

### Dry-running protection of centrifugal pumps based on active power monitoring

With the function shown here, you can implement dry-running protection for centrifugal pumps with a radial-flow impeller, even in hazardous areas, based on active-power monitoring. You can use this protection function either alone or in addition to the general "active-power monitoring" described in [Active power monitoring](#active-power-monitoring). The general function "active-power monitoring" is not approved for use in hazardous areas. SIMOCODE pro can indirectly monitor the state of a device or system via the active power. By monitoring the active power of a pump motor, conclusions can be drawn about the flow rate from the active power level. As the flow rate (delivery rate) decreases, the active power decreases in centrifugal pumps with a radial-flow impeller (progressive delivery characteristic). For dry-running protection, the motor and therefore the pump is disconnected when the active power falls below a minimum value. In addition to avoiding damage to the pump, SIMOCODE pro can contribute, in particular, to explosion protection of centrifugal pumps that handle flammable media or are installed in hazardous areas. In this case, the explosion protection conforms with type of protection b by "ignition source monitoring", ignition protection system b1, e.g. acc. to DIN EN 80079‑37. The response of SIMOCODE pro on reaching the freely selectable trip level can be delayed. A start-up bridging time can also be parameterized.

The protective function "dry-running protection of centrifugal pumps by active-power monitoring" requires the use of a basic unit combined with a current/voltage measuring module and is implemented in the following device types:

Basic units with PTB 18 ATEX 5003 X:

- 3UF7010-1A.00-0 (from product version *E16*)
- 3UF7011-1A.00-0 (from product version *E13*)
- 3UF7013-1A.00-0 (from product version *E04*)
- Current/voltage measuring modules: 3UF712.-1.A01-0.

> **Note**
>
> **Use exclusively with the control function "direct starter" (direct-on-line starter)**
>
> The function "dry-running protection of centrifugal pumps by active power monitoring" can be used exclusively with the control function "direct starter" (direct-on-line starter).

When the motor contactor is closed, the function "dry-running protection of centrifugal pumps by active power monitoring" is activated. In the current/voltage measuring module, the measured values for the active power are calculated from the rms values of the measured currents and voltages of the 3 phases and transferred to the basic unit. There, the measured values are compared with the stored trip level. If the system is not in the start-up bridging phase, the delay time starts on undershooting. If the undershooting is pending for the entire delay time, after the delay time expires a signal for "motor off" is generated and sent to the motor contactor. This disconnects the motor from the line power supply. At the same time, the error message "dry running pump" appears.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Interposing transformers are not permissible**  Use of interposing transformers in conjunction with the function dry-running protection is not permissible. |  |

> **Note**
>
> **Measuring range of the current/voltage measuring module**
>
> The measuring range of the current/voltage measuring module selected for the "dry-running protection of centrifugal pumps by active power monitoring" function must include the currents both at the minimum delivery flow rate Q<sub>MIN</sub> / P<sub>MIN</sub> / I<sub>MIN</sub> and at the working point Q<sub>OPT</sub> / P<sub>OPT</sub> / I<sub>OPT</sub> (as well as the rated motor current I<sub>N</sub>).
>
> If necessary, you can modify the use range of a module by mounting multiple primary windings (see Chapter "Measuring current with an external current transformer (interposing transformer)") in the SIMOCODE pro System Manual or the SIMOCODE pro Manual Collection.

> **Note**
>
> **An additional warning level can be set**
>
> You can optionally configure an additional warning level for when the active power is undershot using the function "active-power monitoring" (see [Active power monitoring](#active-power-monitoring)) that is already active before the trip level P<sub>TRIP</sub> is undershot.
>
> However, this warning level is not relevant to approval for use in hazardous areas.

#### Schematic

The following schematic shows the "dry-running protection" function block:

![Schematic](images/152639490443_DV_resource.Stream@PNG-en-US.png)

#### Trip level P<sub>TRIP</sub>

For dry-running protection of centrifugal pumps by active power monitoring, a trip level can be parameterized for the lower limit:

Trip level:

- P<sub>TRIP</sub> < (lower limit): 0 - 750000 W (default setting: 0)

#### Trip level active status

The trip level is active only if the motor is running (the criterion being contactor control), the start-up procedure has been completed, and there is no test position feedback (TPF) (run+).

#### Response to trip level P<sub>TRIP</sub> < (lower limit):

Here, you can set how SIMOCODE pro will respond if the set trip level is undershot:

"Trip level" response for dry-running protection by active power monitoring

| Response | Trip level |
| --- | --- |
| Deactivated | X (d) |
| Signal | - |
| Warn | - |
| Trip | X |
| Delay (running operation, including regular switch-off) | 0 to 10 s (default: 0.5 s, in steps of: 0.1 s) |
| Start-up bridging (starting operation) | 0 to 60 s (default: 0 s, in steps of: 0.5 s) |

> **Note**
>
> **Delay time**
>
> The delay time (running operation, including regular switch-off) is used to increase reliability by avoiding false tripping (e.g. due to measured-value noise or transient voltage dips) or on undershooting P<sub>TRIP</sub> on regular switch-off of the pump and prior closure of the shutoff valve on the discharge side.
>
> Specify a start-up bridging time if the trip level P<sub>TRIP</sub> is undershot while the pump is starting (depending on the procedure for opening the shutoff valve on the discharge side).

#### Reset

You must acknowledge the faults with a reset signal, after checking and remedying the fault where applicable.

- "TEST/RESET" button on the basic unit
- "TEST/RESET" button on the operator panel
- Standard function "Reset"

For this purpose, you must connect the inputs "reset input" (connector) to the corresponding sockets, e.g. on reset via the bus.

#### Application areas

SIMOCODE pro can be used for dry-running protection of centrifugal pumps with a sufficiently progressive pump characteristic curve (sufficiently steep). This chapter provides some example pump characteristic curves for various types of impeller. A characteristic curve is progressive when the active power P increases continuously as the flow rate Q increases (see radial-flow impeller; in practice, most centrifugal pumps have a radial-flow impeller).

A pump characteristic curve is progressive when the ratio of the active power P<sub>MIN</sub> with the minimum flow rate Q<sub>MIN</sub> to the active power P<sub>OPT</sub> at the optimum flow rate (working point) Q<sub>OPT</sub> meets the following condition:

P<sub>MIN</sub> / P<sub>OPT</sub> < 0.80

This condition is met on nearly all centrifugal pumps with a radial-flow impeller.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Test before installation of SIMOCODE pro for dry-running protection of centrifugal pumps**  Before installing SIMOCODE pro for dry-running protection of centrifugal pumps, check whether the condition for a sufficiently progressive pump characteristic curve is met based on the medium-specific pump characteristics of the pump manufacturer. For approximation, you can assume that the ratio of the pump shaft outputs (P<sub>P,MIN</sub> / P<sub>P,OPT</sub>) is similar in magnitude to the ratio of the active powers (P<sub>MIN</sub> / P<sub>OPT</sub>). |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Coordination of the "pump + motor" combination is required**  Coordinate the "pump + motor" combination in a suitable way.  In particular, you must not overdimension the motor too much.  In the partial load range, the efficiency of the motor decreases disproportionately. The characteristic of the pump + motor combination is therefore less steep. |  |

#### Example types of impeller, example pump characteristic curve

![Example types of impeller of centrifugal pumps (source: SIHI Group)Example types of impeller of centrifugal pumps](images/152639494667_DV_resource.Stream@PNG-de-DE.png)

Example types of impeller of centrifugal pumps (source: SIHI Group)

① Vane-type impeller

② Radial-flow impeller

③ Mixed-flow impeller

④ Axial-flow impeller (propeller)

![Example pump characteristic curve for different types of impeller of centrifugal pumps (source: SIHI Group)Example pump characteristic curve for different types of impeller of centrifugal pumps](images/152639498891_DV_resource.Stream@PNG-de-DE.png)

Example pump characteristic curve for different types of impeller of centrifugal pumps (source: SIHI Group)

① Vane-type impeller

② Radial-flow impeller

③ Mixed-flow impeller

④ Axial-flow impeller

SIMOCODE pro can be used, in particular, also for dry-running protection of centrifugal pumps that handle combustible media or are installed in a hazardous area.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Ex applications**  Before using SIMOCODE pro for Ex applications check whether the Ex approvals of SIMOCODE pro cover the relevant use case (see [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951), Chapter "Safety and commissioning information for Ex areas" and the labeling on the device). |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Example evaluation of ignition hazards**  You will find information on the possible contribution of SIMOCODE pro to the Ex protection concept for centrifugal pumps in the example ignition hazard evaluation at the end of his chapter. |  |

> **Note**
>
> **Sealing system**
>
> For centrifugal pumps that are monitored for dry running with SIMOCODE pro, there are no restrictions with respect to the sealing system. For example, simple and double-acting mechanical seals, magnetic drive pumps, and canned motor pumps are conceivable.

#### Parameter input

The parameters used for the "dry-running protection of centrifugal pumps by active power monitoring" function

- P<sub>TRIP</sub>: Trip value for the active power on undershooting (trip level)
- t<sub>V,TRIP</sub>: Delay time for tripping during operation
- t<sub>BRIDGE</sub>: Start-up bridging time

can be set either by direct input into the device via the engineering software SIMOCODE ES or via the menu-guided input sequence during teach-in with the dry-running protection wizard. With direct input you additionally have to set the "Behavior" parameter manually to "Trip". With teach-in this is done automatically after leaving the last dialog window.

At the start of the dry-running protection wizard, you open the commissioning editor in the project for the SIMOCODE device in question in the online view. You will find the wizard there under [Dry-running protection wizard](#dry-running-protection-wizard).

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **The conditions for sufficient distance from dry running and a sufficiently progressive pump characteristic curve must be met**  If you enter the trip level directly via the engineering software, you must take the following measures:  - Check that the conditions for sufficient distance of the trip level from the dry-run state (P<sub>Trip</sub> > 1.1*P<sub>MIN</sub>) are met. - Check that the conditions for a sufficiently progressive pump characteristic curve (P<sub>MIN</sub> / P<sub>OPT</sub> < 0.80) are met by active power measurement - Manually check that the permissible range of current (I<sub>U</sub> < I < I<sub>O</sub>) and voltage (93 V < U < 794 V) have been met using the relevant 3UF7 system   External measuring equipment is not approved for determining the working point parameters. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Access/authorization concept for input or modification of parameter values**  When using SIMOCODE pro for Ex applications, ensure a suitable access/authorization concept for input or modification of parameter values. |  |

#### Parameter trip value P<sub>TRIP</sub>

No simple mathematical relation can be stated between the flow rate of a centrifugal pump and the active power on the motor. The influencing factors include material data and installation and operating and ambient conditions.

For a certain installed arrangement of the pump, motor, and surrounding plant, a phenomenological, reproducible relationship can be established between the flow rate Q and the active power P. If the operating points are not sufficiently known, the ratios can be determined at the operating point (Q<sub>OPT</sub>/P<sub>OPT</sub>) and at the minimum flow rate (Q<sub>MIN</sub> / P<sub>MIN</sub>) specified by the pump manufacturer as part of a so-called teach‑in (see separate description in this chapter).

Via the menu-guided input sequence (dry-running protection wizard), you can set the threshold value for the active power P<sub>TRIP</sub> (trip value) during the teach‑in. It is formed from the measured active power P<sub>MIN</sub> at minimum flow rate Q<sub>MIN</sub> multiplied by factor 1.1. This factor is used to establish a sufficient distance between the active power at the trip level and in the dry running state, taking account of the measurement uncertainties.

Alternatively, direct input of the trip value is also possible. Procedure:

- Read off the active power P<sub>OPT</sub> at the operating point
- Read off the active power P<sub>MIN</sub> at minimum flow rate, set P<sub>TRIP</sub> ≥ 1.1 P<sub>MIN</sub>

  - Read off an alternative active power P<sub>a</sub> at alternative flow rate Q<sub>a</sub> below P<sub>opt</sub> during running operation and derive the trip value while meeting the condition P<sub>opt</sub> > P<sub>trip</sub> > 1.1*P<sub>a</sub> at Pa ≥ P<sub>min</sub>.
- Manually check for sufficient scope for progression of the active power characteristic (P<sub>MIN</sub> / P<sub>OPT</sub> < 0.80)
- Set P<sub>TRIP</sub> ≥ 1.1*P<sub>MIN</sub>.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Partial load operating states of the pump.**  When defining the trip level, note any partial load operating states of the pump. |  |

#### Parameter delay time t<sub>V,TRIP</sub>

The delay time t<sub>V,TRIP</sub> during running operation of the centrifugal pump (including switch-off) is used to increase the reliability by avoiding false tripping on transient undershooting of the trip value during running operation (e.g. due to measured value noise or transient voltage dips).

With parameter t<sub>V TRIP</sub>, false tripping is also avoided during normal switch-off of the pump. Depending on the procedure for closing the shutoff valve on the discharge side, the trip level P<sub> TRIP</sub> may possibly be undershot.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Preventing back flow of the content of the pipe on the discharge side**  Prevent back flow of the content of the pipe on the discharge side with suitable measures.  Reason: Back flow of pumps with permanent-magnet motors can result in a generator effect with the danger of sparking on the terminal board. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Signal "motor off" is pending**  As soon as the signal "motor off" is pending (the criterion being contactor control), the dry-running protection no longer triggers a fault. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Delay time**  Select the delay time t<sub>V,TRIP</sub> to be sufficiently short so that the dry-running protection function is retained for the specific "pump + motor" system. |  |

#### Start-up bridging time parameter t<sub>BRIDGE</sub>

SIMOCODE pro is suitable for the dry-running protection of centrifugal pumps during operation.

> **Note**
>
> **Minimum active power threshold**
>
> During starting, the following effect can occur: Undershooting a minimum active power threshold by starting the pump against a (partially) closed shutoff valve on the discharge side.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Start-up bridging time t<sub>BRIDGE</sub>**  Provide a start-up bridging time t<sub>BRIDGE</sub> against false tripping during which the dry-running protection is suppressed by active power monitoring.  If the trip level is still undershot after expiry of t<sub>BRIDGE </sub>, then the delay time t<sub>V,TRIP</sub> starts to run from this instant.  As part of a safety assessment, you must decide on a case-by-case basis whether additional measures for dry-running protection are required based on the start-up bridging time t<sub>BRIDGE</sub> for the starting procedure and how they should be handled (e.g. organizationally or by devices). |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Manufacturer specifications**  Note any data of the manufacturer of the centrifugal pump on the length of the starting operation against a (partially) closed shutoff valve on the discharge side. |  |

The following effects may also occur during starting of the pump:

- Transient (< 1 s) undershooting of the active power threshold because starting is performed based on active power = 0 and based on electrical effects (e.g. inertia of the motor contactor). False trips are avoided by a start suppression of 500 ms that is permanently in the device and cannot be modified.
- Transient (< 1 s) starting overcurrent (inrush) during which no dry running can be detected by undershooting a minimum active power threshold. Does not result in false tripping and is therefore non-critical in respect of the Ex protection because of the short duration.

#### Logging of the set parameter values

After input or modification of parameter values, we recommend recording the defined numeric values, including the time of input, and archiving the log file. This is important, in particular, when using SIMOCODE pro as part of a an Ex protection concept.

To generate a log file, use the print function of SIMOCODE ES. The log file also contains the parameters set for the "dry-running protection" function.

> **Note**
>
> **Log reset**
>
> If you modify the dry-running parameters without using a wizard, an existing log from a wizard is reset.

#### Checking and changing the set parameter values

If necessary, check and correct the set parameter values for suitability for the dry running protection function. This applies, in particular, to the trip value P<sub>TRIP</sub>. Checking may be necessary, for example, in the following cases:

- After changes (e.g. impeller replacement) or repairs on the pump, on the pump motor or on the surrounding plant (pipes, valves, vessels, etc. in the intake path and in the discharge path)
- On changing the medium being pumped
- On changes to the operating conditions
- At regular intervals, in accordance with legal requirements (e.g. test cycle for Ex protection)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Measuring devices**  Ensure that the measuring devices used are functioning correctly when inspected (e.g. flow meter). Calibrate them, if necessary. |  |

#### Procedure for teach‑in using the dry-running protection wizard

**Requirements:**

Perform the teach‑in with the real medium to be pumped under real operating conditions (e.g. temperatures, pressures).

Requirements:

- The starting phase of the pump must have been completed.
- As a prerequisite in the plant, we recommend flow rate measurement on the discharge side.

> **Note**
>
> **Automation**
>
> To reduce manual interventions, you can store the relevant sequences for a (partially) automated teach-in in your process control system, if required.

> **Note**
>
> **Password protection must have been deactivated**
>
> If password protection is activated, you must deactivate it.

> **Note**
>
> **Setting a temporary trip level**
>
> In teach‑in, the plant is temporarily operated with minimum flow rate Q<sub>MIN</sub>, which results in minimum active power P<sub>MIN</sub>.
>
> To avoid false tripping, but still ensure basic protection against dry running, you should set a temporary trip level before teach‑in, the value of which is smaller than the expected minimum active power P<sub>MIN</sub>.
>
> We recommend the following settings:
>
> - Temporary trip level: At least 30% above the pump shaft output during zero delivery (see pump characteristic curve)
> - Delay time t<sub>V,TRIP</sub> = 0 or as short as possible
>
> As the trip level, enter this value by direct input using the SIMOCODE ES engineering software and transfer the change to the device. You will find the parameters in the project for the SIMOCODE pro device in question in the parameter editor under "Parameters → Dry-running protection".

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Using and resetting the temporary trip level**  The temporary trip level only provides basic protection and does not afford dry-running protection for applications in hazardous areas.  Reset this temporary trip level before resuming production if the teach‑in sequence is not completed! |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Qualified personnel required**  The teach-in has to be carried out by qualified responsible specialist personnel.  Failure to follow proper procedures results in **personal injury and damage to property**. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Information provided by the pump manufacturer**  The manufacturer's instructions must be observed. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Device parameterization during starting (only affects system in which SIEMENS process controls are used)**  If the startup parameter block is deactivated (for PROFINET, "Fieldbus interface→ Startup parameter block" has the default setting "deactivated"), the SIMOCODE pro device parameters are stored in the CPU of the automation system and transferred to SIMOCODE pro via PROFIBUS or PROFINET when the system starts. Parameters that were transferred directly to the device during the teach-in would then be overwritten.   Therefore ensure before teach-in starts that the startup parameter block is activated and effective in the device.  If you want to use the device parameterization during startup nevertheless, proceed as follows:  - Compile the control hardware after completion of the teach-in and load it into the CPU. In this way, the SIMOCODE pro device parameters with the up-to-date settings for the dry-running protection function are loaded into the CPU - Now deactivate the startup parameter block in the SIMOCODE pro device parameters and transfer this change to the SIMOCODE pro basic unit. This procedure ensures that the device parameters transferred to SIMOCODE pro during system startup contain the up-to-date settings for the dry-running protection function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Use of a memory module**  If a memory module is used, you must ensure that the parameter settings are updated on the memory module after the teach-in process. |  |

**Performing the "teach-in" with the dry-running protection wizard**

The procedure of a teach-in is illustrated in the example pump characteristic curve (see below). Flow rate measurement on the discharge side is assumed.

At the start of the menu-guided input sequence, you open the commissioning editor in the project for the SIMOCODE device in question in the online view. You will find the wizard there under "dry-running protection".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Time monitoring of the teach-in**  The teach-in is monitored by a timer in the device's firmware, which becomes active when inactivity is detected.  If no progress to the next step takes place for a period of 10 min, or the timer is reset manually, SIMOCODE pro goes into the fault condition; an error message to that effect is displayed and the motor is switched off.  You can restart the timer manually at any time on each input page of the wizard with the "Reset Timer" button. |  |

First start the pump (according to the instructions provided in the documentation of the pump manufacturer) and ensure that the pump has attained operating conditions (especially temperature).

Next, perform the following steps as you are prompted in the input sequence:

1. Start the dry-running protection wizard: Start the dry-running protection wizard in the online view of the commissioning editor of SIMOCODE ES (see [Dry-running protection wizard](#dry-running-protection-wizard)).
2. Check the currently active settings during teach-in: After the wizard has been started, the parameters of the dry-running protection function currently active in the device are displayed:

   - Response
   - Trip level
   - Tripping delay time
   - Start-up bridging time

   Check the settings for use of a temporary trip level (see instruction "Setting a temporary trip level" at the beginning of this chapter)

   | Symbol | Meaning |
   | --- | --- |
   |  | **Notice** |
   | **Changing the currently active setting**  You can only change the currently active setting by entering the parameters directly in the engineering software. Close the dry-running protection wizard to do this.  Remember that the pump is still in operation (limited by the timer that monitors during inactivity). |  |
3. Setting the flow rate to the working point Q<sub>opt</sub>: Set the usual flow rate on your process system and manually enter the numeric value for the working point Q<sub>OPT</sub> that you can read off the flow rate measuring device on the discharge side (SIMOCODE pro records the associated active power P<sub>OPT</sub>).
4. Setting of the flow rate to Q<sub>MIN</sub>: Set the minimum flow rate on your process system and manually enter the numeric value for the minimum flow rate Q<sub>MIN</sub> that you can read off the flow rate measuring device on the discharge side (SIMOCODE pro records the associated active power P<sub>MIN</sub>).
5. Display of the calculated trip level: The trip value determined by the system P<sub>TRIP</sub> = 1.1*P<sub>MIN</sub> for the active power is displayed.
6. Setting the delay times:

   - Enter the delay time t<sub>V,TRIP</sub> for running operation of the centrifugal pump (default value: 0.5 s)
   - Enter the start-up bridging time t<sub>BRIDGE</sub> (default value: 0 s)
7. Display the summary, check and activate the dry-running protection function: Check the displayed parameter values (P<sub>TRIP</sub>, t<sub>V,TRIP</sub>, t<sub>BRIDGE</sub>) for the dry-running protection by active-power monitoring and the set values pairs P<sub>OPT</sub> / Q<sub>OPT</sub> and P<sub>MIN</sub><sup> </sup>/ Q<sub>MIN</sub>.

After confirmation, the input sequence is exited and the modified parameter values are activated in the device by the teach-in.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Delivery flow rate must be sufficiently large**  Before activation of the parameter values, make sure that the delivery flow rate is sufficient at this instant.  This avoids unwanted tripping. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Tests performed by the device**  In SIMOCODE pro, the preconditions for the use of the function "dry-running protection" are checked during the teach-in. A check is made to see whether the following conditions are met:  - Progressive pump characteristic curve (P<sub>MIN</sub> / P<sub>OPT</sub> < 0.80) - Current in the permissible range (I<sub>U</sub> < I < I<sub>o</sub>) - Voltage in the permissible range (93 V < U < 794 V)   If one of the above conditions is not met, an error message is output. In this case you must  - close the dry-running protection wizard - eliminate the error and then restart the dry-running protection wizard - if necessary also restart the pump beforehand.   Check the determined absolute values for P<sub>OPT</sub> and P<sub>MIN</sub> for plausibility irrespective of this (where applicable by comparing the pump characteristics). Determine the cause for obvious deviations before activating the dry-running protection function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Check after manual direct input of the trip level**  If you entered the trip level manually with the engineering software, check for the following conditions:  - the conditions for a sufficiently progressive pump characteristic curve - the conditions for sufficient distance of the trip level from the dry-run state - the conditions for the permissible range of current and voltage |  |

> **Note**
>
> **Log file**
>
> For documentation purposes, we recommend generating and printing out a log file after parameter setting by teach-in.

![Example monitoring parameters for the teach‑in illustrated in the characteristic curve of a centrifugal pump with a radial-flow impeller for water at a speed of 1450 rpm (example); source: KSB SE & Co. KGaAExample monitoring parameters for the teach‑in illustrated in the characteristic curve of a centrifugal pump with a radial-flow impeller for water at a speed of 1450 rpm (example); source: KSB SE & Co. KGaA](images/152639682315_DV_resource.Stream@PNG-de-DE.png)

Example monitoring parameters for the teach‑in illustrated in the characteristic curve of a centrifugal pump with a radial-flow impeller for water at a speed of 1450 rpm(example); source: KSB SE & Co. KGaA

**Alternatives when a flow measurement is missing on the discharge side**

If no stationary flow rate measurement is provided, we recommend the following alternatives, for example:

- Mobile flow rate measurement by ultrasound in clamp‑on technology (calibration required)
- Determine the flow rate via level change in a vessel
- Procedure as for hydraulic acceptance tests for centrifugal pumps acc. to DIN EN ISO 9906

### Motor control

This section contains information on the following topics:

- [Control stations](#control-stations)
- [Operating modes](#operating-modes)
- [Mode selector](#mode-selector)
- [Enables](#enables)
- [Schematic for enables and enabled control command in the control unit](#schematic-for-enables-and-enabled-control-command-in-the-control-unit)
- [Control function](#control-function)
- [Contactor controls](#contactor-controls)
- [Lamp controls and status information](#lamp-controls-and-status-information)
- [Non-maintained command mode](#non-maintained-command-mode)
- [Saving change-over command](#saving-change-over-command)
- [DM-F LOCAL/DM-F PROFIsafe - Separate function from control function](#dm-f-localdm-f-profisafe---separate-function-from-control-function)
- [Load type](#load-type)
- [Feedback time](#feedback-time)
- [Execution time](#execution-time)
- [Interlocking time](#interlocking-time)
- [Change-over pause](#change-over-pause)
- [Max. star time](#max-star-time)
- [Current measuring module built into the delta circuit or the supply cable](#current-measuring-module-built-into-the-delta-circuit-or-the-supply-cable)
- [Overview of control functions](#overview-of-control-functions)

#### Control stations

Control stations are places from which control commands are issued to the motor. The "Control Stations" function block is used for administration, switching and prioritization of these different control stations.

SIMOCODE pro allows the parallel administration of up to four different control stations.

Dependent on the set control function, up to five different control commands can be transmitted from every control station to SIMOCODE pro.

##### Control stations:

- **Local** control (in the direct vicinity of the motor). Control commands via pushbuttons.
- **PLC/PCS** or **PLC/PCS [PN]**, switching commands are issued by the automation system (remote).
- **PC** or **PC/OPC-UA [HMI]**, control commands are issued via an operator control station or via PROFIBUS DPV1, OPC-UA, orPROFINET.
- **Operator panel**, control commands are issued via the buttons of the operator panel in the switchgear cabinet door.

Examples of control commands:

- Motor ON (ON>), Motor OFF (OFF) for a direct starter
- Motor LEFT (ON<), Motor OFF (OFF), Motor RIGHT (ON>) for a reversing starter
- Motor SLOW (ON>), Motor FAST (ON>>), Motor OFF (OFF) for a Dahlander circuit.

The plugs of the "Control Stations" function block must be connected to any sockets (e.g. binary inputs on the basic unit, control bits from the communication bus, etc.) for the control commands to take effect.

Up to five different control commands can come from each control station. Up to five plugs (plug ON<<, ON<, OFF, ON>, ON>>) are available on the function block for each control station. The number of active plugs depends on the control function selected. With a direct starter, for example, only the plugs "ON>" and "OFF" are active.

##### Control stations:

- Local: In this case, the command devices are usually in the immediate vicinity of the motor and are wired to the inputs of SIMOCODE pro. The plugs of the "Control Stations" function block must be connected to any sockets (normally the function blocks for the basic units or the digital module inputs – BU Inputs, DM Inputs) for the control commands to take effect.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Safe motor disconnection**  The OFF command "LC OFF" is 0-active. This ensures that SIMOCODE pro shuts the motor down safely if an open circuit occurs in the supply cable, for example. The precondition is that the control station is active. |  |
- PLC/PCS or PLC/PCS [PN]: This control station is primarily intended for control commands from the automation system (PLC/PCS) via the cyclic receive telegram of the communication bus. The plugs of the "Control Stations" function block must be connected to any sockets, typically with cyclic receive, for the control commands to take effect.
- PC or PC/OPC-UA [HMI]: This control station is primarily intended for switching commands on an arbitrary PC that, along with the automation system, is used as a second master on PROFIBUS DP or that, as a client, accesses the data made available by SIMOCODE pro, as server, via OPC-UA. The control commands are sent via the Acyclic receive telegram from PROFIBUS DPV1 or are transferred using a client-server connection via OPC-UA.

  > **Note**
  >
  > If the SIMOCODE ES or SIMATIC PDM PC software is connected to SIMOCODE pro via communication bus, its control commands automatically take effect via the PC [DPV1] or "PC/OPC-UA" control station. At the same time, the enabled commands for this control station also take effect for SIMOCODE ES.
- Operator panel: This control station is primarily intended for control commands issued via the buttons on the 3UF72 operator panel, which is mounted in a control cabinet door, for example. The plugs of the "Control Stations" function block must be connected to any sockets (normally to the function block for the buttons of the operator panel - OP buttons) for the control commands to take effect.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Control commands for speeds and directions of rotation**  Since the operator panel only has four buttons for controlling the motor feeder, one button must be used as a speed changeover button for control functions with two speeds and two directions of rotation. For this purpose, this button must be assigned to the internal control command "[OP]<>/<<>>". |  |

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Control commands via the operator panel**  If the SIMOCODE ES PC software on a programming device is connected to SIMOCODE pro via the system interface, its control commands automatically take effect via the "Operator panel [OP]" control station. At the same time, the enabled commands for this control station also take effect for SIMOCODE ES. |  |

#### Operating modes

You can use the control stations either individually or in combination. There are four different operating modes available for selection:

- Local 1
- Local 2
- Local 3
- Remote/Automatic: In this operating mode, the system must communicate via PLC.

Not all control stations are usually connected. If more than one control station (e.g. local and PLC/PCS) is connected, it makes sense and is also mandatory to operate the control stations selectively. Four operating modes are provided for this purpose which can be selected via two control signals (mode selectors). For each individual control station in every operating mode, you can define whether "ON commands" and/or "OFF commands" are to be accepted. In multiplex mode, the operating modes are controlled in such a way that only one operating mode is active at any one time.

Example: There are three operating modes in a system:

| Symbol | Meaning |
| --- | --- |
| Operating mode | Description |
| Keyswitch operation, e.g. Local 1 | Only local control inputs are permitted! All other control stations are disabled. |
| Manual operation, e.g. Local 3 | Only operator panel control commands and local control commands can be issued. |
| Remote operation, e.g. remote/automatic | Only control commands from the PLC/PCS are permitted. |

The keyswitch must be read in via an input to select these operating modes. The remote switching operation should be controlled via the bus. Keyswitch operation has priority over all other operating modes.

#### Mode selector

The S1/S2 mode selectors are used to switch between the operating modes "Local 1", "Local 2", "Local 3" and "Remote/Automatic".

To do this, plugs S1 and S2 must be connected to any sockets (e.g. device inputs, communication bus control bits, etc.).

The table below shows the operating modes depending on the signal states of mode selectors S1 and S2:

| Input | Operating mode |  |  |  |
| --- | --- | --- | --- | --- |
|  | Local 1 | Local 2 | Local 3 | Remote/Automatic |
| S1 | 0 | 0 | 1 | 1 |
| S2 | 0 | 1 | 0 | 1 |

The different operating modes for enabling the control stations can be used to specify the switch authorizations for the individual control stations

- Local control [LC]
- PLC/PCS [DP] or PLC/PCS [PN]
- PC [DPV1] or PC/OPC-UA [HMI]
- Operator panel (OP)

Only the following are active:

- The operating mode set by plugs S1 and S2 of the "Control Stations" function block and
- the enables selected there

#### Enables

Enables, which must be activated, are assigned to the "ON" and "OFF" control commands for each control station in every operating mode.

This means, depending on the operating mode, you can define for every control station whether the motor may be switched on only, off only, or on and off from the control station.

The corresponding checkbox ☑ is activated in the "Control stations" dialog in SIMOCODE ES.

#### Schematic for enables and enabled control command in the control unit

Example of enabled commands in the control unit:

The following diagram shows an example of enabled commands for the "Local 2" operating mode, "Dahlander reversing starter" control function:

![Enables and enabled control command schematic](images/148919666315_DV_resource.Stream@PNG-en-US.png)

Enables and enabled control command schematic

In the example, the motor can only be switched on and off in the "Local 2" operating mode via the buttons (local) connected to the inputs of the basic unit and the digital module.

#### Control function

Control functions (e.g. direct starters, reversing starters) are used for controlling load feeders.

They are characterized by the following important features:

- Monitoring the switch-on/switch-off process
- Monitoring the ON/OFF status
- Tripping if a fault occurs.

SIMOCODE pro monitors these statuses using the "Feedback ON" auxiliary control input, which is usually derived directly from the current flow in the main circuit, via the current measuring modules.

All the necessary interlocks and logic operations for the respective applications are already implemented in the control functions.

Control functions include:

- Plugs for control commands ON <<, ON <, OFF, ON >, ON >> that are usually connected with the "Enabled control command" sockets.
- Auxiliary control inputs (plugs), e.g. Feedback ON
- Sockets for

  - Contactor controls QE1 to QE5.
  - Displays (lamp controls) QL*, QLS.
  - Status, e.g. "Status - ON <<, Status - ON >>".
  - Faults, e.g. "Fault - Feedback (FB) On", "Fault - Antivalence"
- Settings, e.g. interlocking time, non-maintained command mode ON/OFF, etc.
- A logic component with all necessary interlocks and connections for the control function.
- Like control functions, the motor protection with its parameters and signals is active "at a higher level in the background". Motor protection and thermistor protection are independent functions that switch off the motor when activated via the control function.

##### Control function schematic

The schematic below shows the general representation of the control function ("Protection/Control" function block):

![Control function schematic](images/152640008715_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Control stations](#control-stations)
  
[Application selection](#application-selection)

#### Contactor controls

The QE contactor controls are switched dependent on the incoming control commands and taking the specified control function into consideration, including all corresponding interlocks, feedbacks, corresponding parameters and the higher-level motor protection. In general, the QE contactor controls are directly connected to the outputs of the basic unit or the digital modules, and they switch the connected contactors using relays. The number of usable QE contactor controls is directly dependent on the set control function.

#### Lamp controls and status information

The feeder status feedback is signaled via the status information or the QL lamp controls. They are all directly dependent on the status of the auxiliary control input "FB ON". The number of usable lamp controls and status information is directly dependent on the specified control function.

Feeder status feedback:

- Status information, e.g. "Status ON<": These are transmitted, for example, via PROFIBUS DP to the automation system and signal the status of the feeder there.
- Displays (lamp control) "Display - QLE<": These can, for example, activate a signal lamp or a pushbutton lamp for status display.

  > **Note**
  >
  > If the motor is running in test operation, the indicators show a different response (e.g. flashing).
- In addition to the status signals, the "QL..." lamp controls additionally indicate the following:

  - Unacknowledged fault (lamp output general fault QLS is flashing)
  - Saved change-over command (QLE **lamp outputs** are flickering)
  - Lamp test: All QL outputs are activated for approx. 2 s.
- Additional status information:

  - Start active: If "Motor" has been selected as the load type, this signal is present during the start process of the motor for the duration of the specified class time (e.g. 10 s for Class 10). Exceptions are the "Overload relay" and "Solenoid valve" control functions.
  - Interlocking time active: For control functions with a change in the direction of rotation, the signal remains present until the specified interlocking time has elapsed.
  - Change-over pause active: For the "Dahlander starter," "Pole-changing starter," and "Star-delta" control functions, the signal is present after changeover until the specified time has elapsed.
- Additional status information for the "Positioner" or "Solenoid valve" control function:

  - Feedback Closed (FC)
  - Feedback Open (FO)
  - Torque Closed (TC)
  - Torque Open (TO).

These feedback signals specify the present status of the corresponding limit switch and/or torque switch. The amount of usable status information is directly dependent on the selected control function.

- Additional fault messages for the "Positioner" or "Solenoid valve" control function:

  - Stalled positioner: The torque switch has been activated before the corresponding limit switch. The positioner may have stalled.
  - Double 0: Both torque switches have responded
  - Double 1: Both limit switches have responded
  - End position: Positioner has left the end position without receiving a control command
  - Antivalence: The changeover contacts of the limit switches do not issue an antivalent signal (only for the "Positioner 5" control function).

#### Non-maintained command mode

- **Deactivated**
    
  The control command on the corresponding plug of the control stations "ON <, ON <<, ON >, ON >>" is saved. It can only be revoked by an "OFF" control command from the corresponding control station. An auxiliary contact for locking the contactor is not required. Motor feeders are usually operated in locking mode. Locking is preset.
- Activated  
  Depending on the control function chosen, non-maintained command mode acts on the plugs of all control stations "ON <, ON <<, ON >, ON >>". A control command is only effective as long as there is a "high signal".

#### Saving change-over command

- **Deactivated**
    
  Commands for switching from one direction of rotation/speed to the other are only implemented via a previous "OFF" and after the interlocking time/change-over pause has elapsed.  
  This setting is used under normal conditions and is the default setting.
- Activated  
  Change-over commands for switching from one direction of rotation/rotational speed to the other are implemented without a previous "OFF" once the interlocking time/change-over pause has elapsed. If the selected direction/speed cannot be executed immediately due to a parameterized interlocking time/change-over pause, the selection is signaled by flickering QLE displays. Your selection can be canceled at any time with "OFF".

#### DM-F LOCAL/DM-F PROFIsafe - Separate function from control function

- **Deactivated**
    
  Safety-related tripping via the DM-F modules also affects the SIMOCODE pro control function, so that the contactor control is also always switched off.  
  This setting is selected for applications where safety-related tripping directly affects the motor controlled by SIMOCODE pro.
- Activated:  
  Safety-related tripping via the DM-F modules does not affect the SIMOCODE pro control function, so that the contactor control is not switched off.  
  This setting is selected for applications where safety-related tripping does not affect the motor controlled by SIMOCODE pro.

#### Load type

You can choose between

- **Motor** and
- Resistive load (e.g. heater):

Since overcurrent generally does not flow during startup on a resistive load, the "Start active" status is not signaled. In this case, the start-up override does not occur for the "Signaling", "Warning" and "Tripping" functions.

#### Feedback time

SIMOCODE pro monitors the status of the feeder (ON or OFF) via FB ON.  
If the status of FB ON changes without a corresponding switching command, "Fault - Feedback (FB)" switches off the feeder.  
Default: **0.5** s.  
The feedback time can be used to suppress such "feedback faults" for a defined period of time, e.g. in the case of network switches.  
When the motor is switched off, SIMOCODE pro continuously checks if FB ON = 0.  
If the current flows longer than the set feedback time without the "ON" control command being issued, a fault message "Fault - Feedback (FB) ON" is issued. The contactor controls can only be re-connected after the fault has been rectified.  
When the motor is switched on, SIMOCODE pro continuously checks if FB ON = 1. If no current flows for longer than the set feedback time without the "OFF" control command being issued, a fault message "Fault - feedback (FB) OFF" is issued. The contactor controls are deactivated.

#### Execution time

SIMOCODE pro monitors the switch-on and switch-off process. The switch-on or switch-off process must be completed within this time.  
Default: **1.0**s.  
After the "ON" control command is issued, SIMOCODE pro must be able to measure current in the main circuit within the execution time. Otherwise, the fault message  
"Fault - execution ON command" will be issued. SIMOCODE pro deactivates the contactor controls.  
After the "OFF" control command is issued, SIMOCODE pro must not be able to measure any current in the main circuit after the execution time has elapsed. Otherwise, the fault message   
"Fault - Execution STOP cmmand" is issued.  
The contactor controls can only be re-connected after the fault has been rectified.

#### Interlocking time

SIMOCODE pro prevents both contactors from switching on at the same time, in the case of reversing starters, for example. Switching from one direction of rotation to the other can be delayed via the interlocking time.  
Default: **0** s.

#### Change-over pause

In the "Dahlander starter" and "Pole-changing starter" control functions, switching from FAST to SLOW can be delayed by the time configured.  
In the "Star-delta starter" control function, the change-over pause extends the time between switching off the star contactor and switching on the delta contactor by the time configured.  
Default: **0.00** s.

#### Max. star time

With the control functions "Star-delta starter" or "Star-delta reversing starter":  
Time-dependent switching from star to delta.  
Max. star time: 0 - 255 s (default: **20** s)

#### Current measuring module built into the delta circuit or the supply cable

With the control functions "Star-delta starter" or "Star-delta reversing starter":  
The set current and the change-over levels for star-delta switching depend on the installation location of the current measuring module:

- **In the delta circuit:** Set current I<sub>s</sub> is reduced to   
  I<sub>rated</sub> x 1/√3
- In supply cable: Set current I<sub>s</sub> = I<sub>n</sub> (rated current of the motor).

#### Overview of control functions

Depending on the device series, the system provides the following control functions:

| Control function | SIMOCODE pro |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | C | S | V PB | V MB RTU | V PN | V EtherNet/IP |
| Overload relay | ● | ● | ● | ● | ● | ● |
| Direct starter | ● | ● | ● | ● | ● | ● |
| Reversing starter | ● | ● | ● | ● | ● | ● |
| Circuit breaker | ● | ● | ● | ● | ● | ● |
| Star-delta starter | — | ● | ● | ● | ● | ● |
| Star-delta reversing starter | — | — | ● | ● | ● | ● |
| Dahlander starter | — | — | ● | ● | ● | ● |
| Dahlander reversing starter | — | — | ● | ● | ● | ● |
| Pole-changing starter | — | — | ● | ● | ● | ● |
| Pole-changing reversing starter | — | — | ● | ● | ● | ● |
| Solenoid valve | — | — | ● | ● | ● | ● |
| Positioner 1 to Positioner 5 | — | — | ● | ● | ● | ● |
| Soft starter | — | ● | ● | ● | ● | ● |
| Soft starter with reversing contactor | — | — | ● | ● | ● | ● |

### Monitoring functions

This section contains information on the following topics:

- [Ground fault monitoring](#ground-fault-monitoring)
- [Internal ground-fault monitoring when using a current measuring module or a 2nd generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-2nd-generation-current-voltage-measuring-module)
- [Internal ground-fault monitoring when using a current measuring module or a 1st generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-1st-generation-current-voltage-measuring-module)
- [External ground-fault monitoring](#external-ground-fault-monitoring)
- [External ground-fault monitoring with a 3UF7500 ground-fault module and 3UL22 differential current transformer](#external-ground-fault-monitoring-with-a-3uf7500-ground-fault-module-and-3ul22-differential-current-transformer)
- [External ground-fault monitoring with a 3UF7510 ground-fault module and 3UL23 residual current transformer](#external-ground-fault-monitoring-with-a-3uf7510-ground-fault-module-and-3ul23-residual-current-transformer)
- [Current limits](#current-limits)
- [Current limits I> (upper limit)](#current-limits-i-upper-limit)
- [Current limits I< (lower limit)](#current-limits-i-lower-limit)
- [Voltage monitoring](#voltage-monitoring)
- [Cos phi monitoring](#cos-phi-monitoring)
- [Active power monitoring](#active-power-monitoring)
- [0 / 4 - 20 mA monitoring](#0-4---20-ma-monitoring)
- [Hysteresis 0 / 4 - 20 mA](#hysteresis-0-4---20-ma)
- [Operation monitoring](#operation-monitoring)
- [Operating hours monitoring](#operating-hours-monitoring)
- [Stop time monitoring](#stop-time-monitoring)
- [Number of starts monitoring motor](#number-of-starts-monitoring-motor)
- [Temperature monitoring (analog)](#temperature-monitoring-analog)
- [Hysteresis for temperature](#hysteresis-for-temperature)
- [Monitoring interval for mandatory testing](#monitoring-interval-for-mandatory-testing)

#### Ground fault monitoring

SIMOCODE pro acquires and monitors all three phase currents. By evaluating the residual current of the three current values, the motor feeder can be monitored for a possible fault current or ground fault.

---

**See also**

[Internal ground-fault monitoring when using a current measuring module or a 2nd generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-2nd-generation-current-voltage-measuring-module)
  
[Internal ground-fault monitoring when using a current measuring module or a 1st generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-1st-generation-current-voltage-measuring-module)
  
[External ground-fault monitoring](#external-ground-fault-monitoring)
  
[External ground-fault monitoring with a 3UF7500 ground-fault module and 3UL22 differential current transformer](#external-ground-fault-monitoring-with-a-3uf7500-ground-fault-module-and-3ul22-differential-current-transformer)
  
[External ground-fault monitoring with a 3UF7510 ground-fault module and 3UL23 residual current transformer](#external-ground-fault-monitoring-with-a-3uf7510-ground-fault-module-and-3ul23-residual-current-transformer)

#### Internal ground-fault monitoring when using a current measuring module or a 2nd generation current / voltage measuring module

##### Description

**Internal ground-fault monitoring** via current measuring modules or current/voltage measuring modules is only possible for motors with a 3-phase connection in networks that are either grounded directly or with low impedance. You can activate internal ground-fault monitoring by parameterization.

It covers two different operating conditions:

- Normal stationary use case up to 2x rated motor current I<sub>s</sub>: Residual currents greater than the value of the set trip/warning levels are detected. Ground-fault monitoring fulfills the accuracy requirements of IEC 60947-1 Class II-B.
- Temporary starting or overload operation greater than 2x rated motor current I<sub>s</sub>: Responsiveness in the overload range of > 2x rated motor current is reduced to reduce false tripping. Residual currents of > 1/2 * I_trip level/I_s * I_max (of the effective motor current) are detected.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **False tripping in the case of internal ground-fault monitoring**  False tripping can occur if you use internal ground-fault monitoring for star-delta circuits. During delta operation, the residual current is non-zero due to harmonics. |  |

##### Schematic

The following schematic shows the "Ground fault monitoring" function block:

![Schematic](images/152641297547_DV_resource.Stream@PNG-en-US.png)

##### Trip level activity, warning level

Unless deactivated, this function is always active, independent of whether the motor is running or not (operating state "ON").

Here you can specify in which motor operating states the trip level/warning level will be active:

- Always (on): Trip level / warning level is always active, regardless of whether the motor is running or at a standstill
- if motor is running, except TPF (run): Trip level / warning level is only active when the motor is running
- If motor is running, except with TPF, with startup override (run+): Trip level / warning level is only active when the motor is running and starting has been completed

##### Response to trip level

**Deactivated**, signal, trip

**Delay**

Setting range: 0 - 25.5 s (**0.5 s**)

##### Response to warning level

Deactivated, **signal**, warn

**Delay**

Setting range: 0 - 25.5 s (**0.1 s**)

##### Hysteresis

0 to 15 % (5 %) of the level value in steps of 1%.

#### Internal ground-fault monitoring when using a current measuring module or a 1st generation current / voltage measuring module

##### Description

**Internal ground-fault monitoring** via current measuring modules or current/voltage measuring modules is only possible for motors with a 3-phase connection in networks that are either grounded directly or with low impedance. You can activate internal ground-fault monitoring by parameterization.

It covers two different operating conditions:

- Normal operation to 2x I<sub>s</sub>. The actual operating current must be less than twice the set current I<sub>s</sub>. Fault currents of > 30 % of the set current ls will be detected.
- Start-up or overload operation to 2x I<sub>s</sub>. The actual operating current is greater than twice the set current I<sub>s</sub>. Residual currents of >15 % of the effective motor current will be detected.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **False tripping in the case of internal ground-fault monitoring**  False tripping can occur if you use internal ground-fault monitoring for star-delta circuits. During delta operation, the residual current is non-zero due to harmonics. |  |

##### Schematic

The following schematic shows the "Ground fault monitoring" function block:

![Schematic](images/152642110091_DV_resource.Stream@PNG-en-US.png)

##### Response to internal ground-fault monitoring

**Deactivated**, signal, warn, trip

**Delay**

Setting range: 0 - 25.5 s (**0.5 s**)

#### External ground-fault monitoring

The external ground-fault monitoring is normally used in the following cases:

- In cases in which power systems are grounded with high impedance
- Where precise measurement of the ground-fault current is necessary, e.g. for the purpose of condition monitoring.

With ground-fault detection using the residual current transformer 3UL23, it is possible to determine the precise residual current as a measured value to define freely selectable warning and trip levels in a wide range 30 mA to 40 A.

Principle of operation:

The main conductors and, if present, the neutral conductor to which the load is connected, are routed through the opening of the residual current transformer 3UL23. Its secondary winding is connected to the ground-fault module.

If an insulation fault occurs, for example, a residual current arises between the incoming and the outgoing currents that is evaluated via the residual current transformer.

For maximum plant availability, the ground-fault module 3UF7 510-1AA00-0 and the residual current transformer 3UL23 were developed with the following design goals:

- High measuring accuracy: The ground-fault module in conjunction with the residual current transformer 3UL23 achieves a measuring accuracy of ±7.5%. This enables set limit values to be monitored very precisely. Spurious tripping caused by measuring errors is minimized. The combination of ground-fault module and residual current transformer 3UL23 is designed so that a warning or alarm is triggered at the latest upon exceeding the set limit values. To achieve this, slightly higher residual currents than those actually measured are displayed and compared with the set limit values. The measuring accuracy is -15% to 0% of the value displayed. This takes into account the measuring accuracy of monitoring relay and residual current transformer.
- Settable prewarning and trip levels: The threshold levels for the residual current are defined over a very wide range of 30 mA to 40 A. The response of SIMOCODE pro on reaching a prewarning level or trip level can be freely parameterized, including a delay.
- Permanent self-monitoring: The permanent self-monitoring of the ground-fault module 3UF7 510-1AA00-0 and the connected transformer ensures reliable monitoring of the function. The connected 3UL23 residual current transformer is also permanently monitored for open-circuit or short-circuit. This means cyclic manual tests to verify the function are obsolete.
- Settable active status and delay times of the residual current protection. Depending on the application, the monitoring function can be active permanently, only when the motor is running, or only after the motor has started. This permits the suppression of residual currents that are only measured during motor starting due to high starting currents. Short-term residual currents or immitted interference can be easily suppressed by means of the adjustable tripping delay time.

Use of the residual current transformers 3UL22 and 3UL23:

- Use the residual current transformer 3UL23 to detect residual currents with the ground-fault module 3UF7 510-1AA00-0. The residual current transformer 3UL23 is suitable for detecting pure AC residual currents and AC residual currents with a pulsating DC component.

> **Note**
>
> **Precondition for using a 3UF7 510-1AA00-0 ground-fault module**
>
> Use of this ground-fault module requires a SIMOCODE pro V PB basic unit, with at least product version *E10* (from 09/2013) or a SIMOCODE pro V PN basic unit with at least product version E04*.

- Use the 3UL22 residual current transformer to detect residual currents with the 3UF7 500-1AA00-0 ground-fault module.

> **Note**
>
> **Only monitoring of the residual current trip level possible**
>
> With this combination, it is only possible to monitor a trip level of the residual current. Measured values are then not available for the residual current.

> **Note**
>
> **Precondition for using a 3UF7 500-1AA00-0 ground-fault module**
>
> Use of this ground-fault module requires a SIMOCODE pro V PB basic unit, at least version *E02* or later (from 04/2005).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Open-circuit voltage may result in death, serious injury or material damage!**  The current transformer output is a constant current power supply. In accordance with U = R * I, the output voltage increases with an increasing resistance. If the connecting terminals of the current transformer are open, the output voltage may become high enough for you to put your life at risk or permanently damage the current transformer.  Avoid operating the unit when open. Operating a network for monitoring safely and without faults requires that the ground-fault module and the 3UL23 residual current transformer have been installed completely. It is absolutely necessary to short-circuit previously installed 3UL23 residual current transformers when the units are not connected to a ground-fault module. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **No personal or fire protection!**  The 3UF75* ground-fault modules monitor that devices and systems are functioning correctly.  They are not suitable for personal protection or protection from fires. |  |

A definable and delayable response can be parameterized in the event a ground fault is detected. A message is output if the ground fault limit is exceeded.

You can define additional trips by parameterization. If the rated fault currents are exceeded, SIMOCODE pro V responds either

- by turning off the contactor controls QE*, or
- by issuing a warning.

---

**See also**

[External ground-fault monitoring with a 3UF7500 ground-fault module and 3UL22 differential current transformer](#external-ground-fault-monitoring-with-a-3uf7500-ground-fault-module-and-3ul22-differential-current-transformer)
  
[External ground-fault monitoring with a 3UF7510 ground-fault module and 3UL23 residual current transformer](#external-ground-fault-monitoring-with-a-3uf7510-ground-fault-module-and-3ul23-residual-current-transformer)

#### External ground-fault monitoring with a 3UF7500 ground-fault module and 3UL22 differential current transformer

##### Schematic

The following schematic shows the Ground-fault monitoring function block when using the 3UF7500 ground-fault module with 3UL22 residual current transformer:

![Schematic](images/152642216715_DV_resource.Stream@PNG-en-US.png)

##### External ground-fault monitoring response

- **Signal**, (the event "External ground fault" is generated)
- Warn, (the event "External ground fault warning" is generated)
- Trip

**Delay**

Setting range: 0 to 25.5 s <sup>1)</sup> (**0.5 s**)

1) Extension of the residual current transformer delay

#### External ground-fault monitoring with a 3UF7510 ground-fault module and 3UL23 residual current transformer

##### Schematic

The following schematic shows the Ground-fault monitoring function block when using the 3UF7510 ground-fault module with 3UL23 residual current transformer:

![Schematic](images/152643372043_DV_resource.Stream@PNG-en-US.png)

##### Trip level, warning level

You can parameterize two different response levels (trip level, warning level) for monitoring the ground-fault current.

If the ground-fault current exceeds the response level, the current limit monitoring will respond.

- Trip level: 30 mA to 40 A in 10 mA increments (default setting: **1000** mA)
- Warning level: 30 mA to 40 A in 10 mA increments (default setting: **500** mA)

##### Trip level activity, warning level

Here you can specify in which motor operating states the trip level/warning level is to be active.

- Always (on): Trip level/warning level always takes effect, regardless of whether the motor is running or at a standstill
- If motor is running, except TPF (run): Trip level/warning level only active when the motor is running
- If motor is running, except with TPF, with startup override (run+): Trip level/warning level is only active when the motor is running and starting has been completed

##### Response to trip level

- **Signal**
- Trip

**Delay**

Setting range: 0 to 25.5 s <sup>1)</sup> (**0.5 s**)

1) Extension of the residual current transformer delay

##### Response to warning level

- **Deactivated**
- Signal
- Warn

**Delay**

Setting range: 0 to 25.5 s <sup>1)</sup> (**0.1 s**)

1) Extension of the residual current transformer delay

##### Hysteresis

Here you can set the hysteresis for the ground-fault current:

Hysteresis ground-fault current: 0 to 15 % of the level value in increments of 1% (**5** %).

##### Response to sensor fault

- **Deactivated**
- Signal
- Warn
- Trip

#### Current limits

Monitoring of current limits is used for process monitoring independent of overload protection.

SIMOCODE pro supports two-phase monitoring of the motor current for freely selectable upper and lower current limit.   
The response of SIMOCODE pro can be freely configured and delayed if it reaches a prewarning or trip level.

The motor current is measured using current measuring modules or current/voltage measuring modules.

---

**See also**

[Current limits I> (upper limit)](#current-limits-i-upper-limit)
  
[Current limits I< (lower limit)](#current-limits-i-lower-limit)

#### Current limits I> (upper limit)

##### Trip level, warning level

When monitoring current limits I> (upper limit), two different response levels, I> (upper limit) trip level and I> (upper limit) warning level, can be parameterized and monitored. If the current of one or more phases exceeds the response level, current limit monitoring responds.

- Trip level: **0** to 1020% of l<sub>s</sub> in 4% increments
- Warning level: **0** to 1020% of l<sub>s</sub> in 4% increments

##### Schematic

The following schematic shows the "Current limits" function block:

![Schematic](images/152644335371_DV_resource.Stream@PNG-en-US.png)

##### Trip level activity, warning level

The trip level/warning level is active only when the motor is running, the start-up procedure has been completed, and there is no test position feedback (TPF) (run+).

##### Response to exceeding the trip level

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Response to exceeding the warning level

- **Deactivated**
- Signal
- Warn

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Hysteresis for current limits I> (upper limit)

Setting range: 0 to 15% of the level value in 1% increments (**5%**)

---

**See also**

[Current limits](#current-limits)
  
Monitoring current limits - Response when warning level I> reached

#### Current limits I< (lower limit)

##### Trip level, warning level

When monitoring current limits I< (lower limit), two different response levels (trip level, warning level) can be parameterized and monitored. If the current of the phases (I<sub>max</sub>) drops below the response level, the current limit monitor responds.

- Trip level: **0** to 1020% of l<sub>s</sub> in 4% increments
- Warning level: **0** to 1020% of l<sub>s</sub> in 4% increments

##### Schematic

The following schematic shows the "Current limits" function block:

![Schematic](images/152644335371_DV_resource.Stream@PNG-en-US.png)

##### Trip level activity, warning level

The trip level/warning level is active only when the motor is running, the start-up procedure has been completed, and there is no test position feedback (TPF) (run+).

##### Response to trip level undershoot

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Response to warning level undershoot

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Hysteresis for current limits I< (lower limit)

Setting range: 0 to 15% of the level value in 1% increments (**5%**)

---

**See also**

[Current limits](#current-limits)

#### Voltage monitoring

SIMOCODE pro supports two-phase undervoltage monitoring of either a three-phase network or a single-phase network for freely selectable limits. The response of SIMOCODE pro on reaching a prewarning level or trip level can be freely parameterized and delayed. Voltage measuring is carried out using current/voltage measuring modules. This is based on the minimum voltage of all voltages U<sub>min</sub>.

> **Note**
>
> Please note that only phase voltages are available with SIMOCODE pro V basic units up to version *E06*. If required, the line-to-line voltage can be calculated from the phase voltage using the logic module "Calculator 1/2" as follows: Line-to-line voltage = phase voltage * 1.73. From version *E07* onward, either phase voltage or line-to-line voltage can be used as the basis for monitoring.

Furthermore, even when the motor is switched off, SIMOCODE pro can determine and signal the further availability of the feeder by measuring the voltage directly at the circuit breaker or at the fuses in the main circuit.

##### Schematic

The following schematic shows the "Voltage monitoring" function block:

![Schematic](images/152645017099_DV_resource.Stream@PNG-en-US.png)

##### Trip level, warning level

You can parameterize two different response levels (trip level/warning level). If the current of one or more phases undershoots the response level or the warning level, voltage monitoring responds.

- Trip level: **0** to 2040 V in 8 V increments
- Warning level: **0** to 2040 V in 8 V increments

##### Trip level activity, warning level

Here you can specify in which motor operating states the trip level/warning level is to take effect:

- Always, except TPF (on+)

  Trip level/warning level always effective, regardless of whether the motor is running or at a standstill; exception: "TPF", i.e. motor feeder is in test position
- If motor runs, except TPF (run)

  Trip level/warning level only active if the motor is ON and not in the test position
- Always (on)<sup> 1)</sup>

  Trip level/warning level always takes effect, regardless of whether the motor is running or at a standstill

1) When using the SIMOCODE pro V basic unit (product version *E03* and higher) with a current/voltage measuring module

##### Response to trip level undershoot

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Response to warning level undershoot

- **Deactivated**
- Signal
- Warn

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Hysteresis for voltage, cos phi, power

Range: 0 to 15% of the level value in 1% increments (**5%**)

##### Voltage measurement - Load type for voltage, cos phi, power

Here you can specify whether 1-phase or 3-phase loads are to be displayed.

#### Cos phi monitoring

Cos phi monitoring monitors the load condition of inductive loads. The main field of application is for asynchronous motors in 1-phase or 3-phase networks with loads that fluctuate significantly. If the set trip level or warning level is undershot, a signal is generated or the motor is switched off, depending upon the setting.

##### Schematic

The following schematic shows the "Cos phi monitoring" function block:

![Schematic](images/152645621515_DV_resource.Stream@PNG-en-US.png)

##### Trip level, warning level

You can parameterize two different response levels (trip level/warning level) for cos phi monitoring.

- Trip level: **0** to 100%
- Warning level: **0** to 100%

##### Trip level activity, warning level

The trip level/warning level is active only when the motor is running, the start-up procedure has been completed, and there is no test position feedback (TPF) (run+).

##### Response to undershooting the set trip level

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Response to undershooting the set warning level

- **Deactivated**
- Signal
- Warn

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

#### Active power monitoring

SIMOCODE pro can indirectly monitor the state of a device or system via the active power. For example, by monitoring the active power of a pump motor, conclusions can be drawn from the active power level about the flow rate or fluid fill levels.

SIMOCODE pro supports two-phase monitoring of the active power for freely selectable upper and lower current limits. The response of SIMOCODE pro can be freely configured and delayed if it reaches a prewarning or trip level.

Active power measuring is carried out using current/voltage measuring modules.

##### Schematic

The following schematic shows the "Active power monitoring" function block:

![Schematic](images/152645829131_DV_resource.Stream@PNG-en-US.png)

##### Trip level, warning level

With active power monitoring, you can parameterize two different response levels (trip level/warning level) for the upper and lower limits:

**Trip level:**

- P> (upper limit)
- P < (lower limit)

**Range: 0** to 4294967.295 kW

**Warning level:**

- P> (upper limit) **0** to 4294967.295 kW
- P < (lower limit)

**Range: 0** to 4294967.295 kW

##### Trip level activity, warning level

The trip level/warning level is active only when the motor is running, the start-up procedure has been completed, and there is no test position feedback (TPF) (run+).

##### Response to trip level P> (upper limit), P< (lower limit)

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

##### Response to warning level P> (upper limit), P< (lower limit)

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**)

#### 0 / 4 - 20 mA monitoring

SIMOCODE pro supports two-phase monitoring of the analog signals of a transducer (standardized 0 / 4 - 20 mA output signal). The analog signals are routed via the analog module to the "0/4 - 20 mA (AM1 and AM2) monitoring" function blocks (AM2 only in conjunction with the SIMOCODE pro V PN and pro V EIP basic units).

##### Schematic

The following schematic shows the "0/4 - 20 mA (AM1 and AM2) monitoring" function blocks:

![Schematic](images/152646331147_DV_resource.Stream@PNG-en-US.png)

##### Trip level, warning level

With 0/4 - 20 mA monitoring, you can parameterize two different response levels (trip level/warning level) for the upper and lower limits:

**Trip level:**

- 0/4-20> (upper limit)
- 0/4 - 20< (lower limit)

Setting range: 0.0 to 23.6 mA / 4.0 to 22.9 mA (0.0 / 4.0 mA)

**Warning level:**

- 0/4-20> (upper limit)
- 0/4 - 20< (lower limit)

Setting range 0.0 to 23.6 mA / 4.0 to 22.9 mA (0.0 / 4.0 mA)

##### Trip level activity, warning level

Here you can specify in which motor operating states the trip level/warning level is to take effect:

- **Always (on):** Trip level/warning level always takes effect, regardless of whether the motor is running or at a standstill
- Always, except TPF (on+): Trip level/warning level is always active regardless of whether the motor is running or at a standstill, with the exception of "TPF," i.e. motor feeder is in the test position
- If motor is running, except TPF (run): Trip level/warning level only active if the motor is ON and not in the test position
- If motor is on, except TPF, with startup override (run+) Trip level/warning level only active if the motor is running, the startup procedure has been completed, and no test position (TPF) is detected.

##### Response to trip level 0/4 to 20 mA> (upper limit), 0/4 to 20 mA< (lower limit)

- **Deactivated**
- Signal
- Trip

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**).

##### Response to warning level 0/4 to 20 mA> (upper limit), 0/4 to 20 mA< (lower limit)

- **Deactivated**
- Signal
- Warn

**Delay**

Setting range: 0 to 25.5 s (**0.5 s**).

##### Marking

The marking is saved in the device and assigned and displayed in the Faults/Warnings online dialog. Optional marking for identifying the message, e.g. "0/4 to 20 >". Range: maximum 10 characters.

##### Hysteresis for 0/4 - 20 mA

Here you can set the fluctuation range for the analog signal:

0 to 15 % of the level value in increments of 1 % (**5 %**).

> **Note**
>
> Monitoring of a second process variable via input 2 of the analog module can be done, for example, by free limit monitors.

#### Hysteresis 0 / 4 - 20 mA

Here you can set the fluctuation range for the analog signal:

0 to 15 % of the level value in increments of 1 % (**5 %**).

#### Operation monitoring

SIMOCODE pro can monitor the operating hours and stop times of a motor and restrict the number of start-ups in a defined time frame in order to avoid plant downtimes due to failed motors caused by running or being stopped for too long.

When an adjustable limit is violated, a message or alarm can be generated which can indicate that the corresponding motor must be serviced or replaced. After the motor has been replaced, the operating hours and stop times can be reset, for example.

To avoid excessive thermal loads and premature wear of the motor, it is possible to limit the number of motor startups for a specifiable period. The number of still possible starts is available in the SIMOCODE pro for further processing.

The limited number of possible starts can be indicated by prewarnings.

> **Note**
>
> Operating hours, motor stop times and the number of motor starts can be monitored completely in the device and / or transmitted to the automation system via PROFIBUS or PROFINET.

##### Schematic

The following schematic shows the "Operation monitoring":

![Schematic](images/152647229963_DV_resource.Stream@PNG-en-US.png)

##### Response

| Response | Operating hours monitoring level | Stop time monitoring - level | Number of starts overshoot | Number of starts prewarning |
| --- | --- | --- | --- | --- |
| Deactivated | **X** | **X** | **X** | **X** |
| Signal | X | X | X | X |
| Warn | X | X | X | X |
| Trip | -- | -- | X | -- |

---

**See also**

[Operating hours monitoring](#operating-hours-monitoring)
  
[Stop time monitoring](#stop-time-monitoring)
  
[Number of starts monitoring motor](#number-of-starts-monitoring-motor)
  
Stop time monitoring - level

#### Operating hours monitoring

The motor operating hours monitoring function enables the operating hours (service life) of a motor to be recorded so that motor maintenance prompts can be generated in good time.

##### Level

If the operating hours exceed the set response level, the monitoring function responds.

Level: **0** - 1193046 hours

##### Activity

Unless deactivated, this function is always active, regardless of whether the motor is running or not (operating state "ON").

##### Response

You can define the response to overshoot here.

---

**See also**

[Operation monitoring](#operation-monitoring)

#### Stop time monitoring

System parts for important processes often have dual drives (A and B drives). Ensure that these are always operated alternately. This prevents long stop times and reduces the risk of non-availability.

The stop time monitoring function can be used, for example, to generate an alarm, thus initiating connection of the motor.

##### Level

The length of the permissible stop time is stipulated here; if exceeded, the monitoring function responds.

Level: **0** - 65535 hours

##### Activity

Unless deactivated, this function is always active, regardless of whether the motor is running or not (operating state "ON").

##### Response

You can define the response to overshoot of the permissible stop time here.

---

**See also**

[Operation monitoring](#operation-monitoring)
  
Stop time monitoring - level

#### Number of starts monitoring motor

Monitoring the number of motor starts can protect system parts (motor and switching devices such as soft starters and converters) from too many start processes within a parameterizable time frame and thus prevent damage. This is particularly useful for commissioning or manual control.

##### Schematic

The schematic below illustrates the principle of monitoring the number of starts:

![Schematic](images/149976465291_DV_resource.Stream@PNG-en-US.png)

##### Permissible starts

The maximum permissible number of starts is set here. The time interval "Time range for starts" commences to run after the first start. After the second to last permissible start has been executed, the "Just one start possible" prewarning is generated.

Permissible starts: **1** to 255

##### Time range for starts

The time range for permissible start processes is set here. The maximum number of starts is only available again after the parameterized time range for starts has elapsed. The number of available starts is shown by the analog value "Permissible starts - actual value".

Time range for starts: **00:00:00** to 18:12:15 hh:mm:ss

##### Active status

Unless deactivated, this function is always active, regardless of whether the motor is running or not (operating state "ON").

##### Response to overshoot

You can define the response to overshoot of the number of starts within the time range for starts here.

##### Response to prewarning

You can define the response after the penultimate start here.

##### Interlocking time

If a new start command is issued within the time range for starts after the last permissible start, this new start command will no longer be executed if the setting "Response to overshoot - trip" has been set. "Fault - No. of starts >" is generated and the set interlocking time activated.

Interlocking time:**00:00:00** to 18:12:15 hh:mm:ss

---

**See also**

[Operation monitoring](#operation-monitoring)

#### Temperature monitoring (analog)

Temperature monitoring of, for example, motor windings, motor bearings, coolant and gearbox temperature, can be carried out via up to three analog temperature sensors such as NTC, KTY 83/84, PT100, PT1000. SIMOCODE pro supports two-phase monitoring for overtemperature: Separate levels for warning and tripping temperature can be set.

Temperature monitoring takes into account the highest temperature of all the sensor measuring circuits of the temperature module.

##### Schematic

The following schematic shows the "Temperature TM1 and TM2 monitoring" function block (TM2 only in conjunction with SIMOCODE pro V PN and pro V EIP):

![Schematic](images/152649439499_DV_resource.Stream@PNG-en-US.png)

##### Settings trip level T>

- Range:  **- 273 °C** up to 65262 °C
- Response to trip level T >: Defining the response when the temperature is overshot (see below)
- Marking for trip level T >: No parameters. Optional marking for identifying the message, e.g. "Temperature>"; range: Maximum. 10 characters

##### Settings warning level T>

- Range:  **- 273 °C** up to 65262 °C
- Response to warning level T >: Defining the response when the temperature is overshot (see below)
- Marking warning level T >: No parameters. Optional marking for identifying the message, e.g. "Temperature>"; range: Maximum 10 characters

##### Trip level activity/warning level

The trip level/warning level is always active, regardless of whether the motor is running or not (operating state "ON").

##### Response to overshoot of the trip level/warning level for the temperature

Response to trip level T >:

- **Signal**
- Trip

Response to warning level T >:

- **Deactivated**
- Signal
- Warn

> **Note**
>
> The sensor type, the number of measuring circuits in use and the response to a sensor fault must be set in the "Temperature module inputs (TM1/2 inputs)" function block if temperature monitoring is used.

> **Note**
>
> To monitor several sensor measuring circuits individually and independently, a suitable number of free limit monitors can be connected to the "Temperature module inputs (TM1/2 inputs)" function block and differing limits set for the individual temperature sensors, instead of the "Temperature monitoring" function block.

#### Hysteresis for temperature

##### Setting the temperature

Here you can set the fluctuation range for the temperature:

0 to 255 °C in 1 °C increments (**5 °C**).

#### Monitoring interval for mandatory testing

Function for monitoring the interval between the connection and the tripping of the enabling circuit (actuator tripping). Each time the enabling circuit is closed, the monitoring time starts again.  
This function supports you in complying with test intervals that require verification.  
In the enabling circuit of the DM-F Local and the DM-F PROFIsafe, relay contacts perform safety-related tripping. You can only determine whether or not the relay contacts of the enabling circuit actually open by changing the switching state of the contacts.

The function "Monitoring interval for mandatory testing" supports plant operators in monitoring the time that has elapsed since the enabling circuit was last switched in. When the set limit is reached, the set response is triggered (deactivated, signaling, warning; see response). This is logged in the event memory.  
This monitoring function is an organizational measure that supports the system operator in detecting faults by carrying out regular tests, see information in the operating instructions on regularly testing the function of a safety device. The monitoring function itself need not be safety-related.

##### Schematic

The following schematic shows the "Monitoring interval for mandatory testing" function block:

![Schematic](images/152649443723_DV_resource.Stream@PNG-en-US.png)

##### Response to monitoring interval for mandatory testing

Response when the set limit is reached:

- **Deactivated**
- Signal
- Warn

##### Test interval:

Adjustable limit for the interval for mandatory testing: **0** to 255 weeks.

### Inputs

This section contains information on the following topics:

- [Basic unit inputs](#basic-unit-inputs)
- [Operator panel buttons](#operator-panel-buttons)
- [Digital module inputs](#digital-module-inputs)
- [Temperature module inputs](#temperature-module-inputs)
- [Analog module inputs](#analog-module-inputs)
- [Cyclic receive](#cyclic-receive)
- [Acyclic receive](#acyclic-receive)
- [OPC-UA Receive](#opc-ua-receive)

#### Basic unit inputs

SIMOCODE pro has a "BU inputs" function block with four binary inputs connected to common potential. You can connect, for example, the buttons for a local control station to the inputs. These signals can be further processed in SIMOCODE pro by internally connecting the sockets of the "BU inputs" function blocks.

The "BU inputs" function block consists of:

- Input terminals located on the outside of the basic unit, corresponding to the sockets "BU input 1" to "BU input 4"
- Sockets in SIMOCODE pro that can be connected to any plugs, e.g. to the "Control stations" function block
- A socket for the "TEST/RESET" button  
  The function of the "TEST/RESET" button is generally dependent upon the operating state of the device:

  - Reset function for the acknowledgement of pending faults
  - Test function for carrying out device tests.

  In addition, other functions can be assigned to the "TEST/RESET" button (e.g., operation of the memory module and of the addressing plug).

One BU inputs function block is provided.

##### Schematic

The following schematic shows the "BU inputs" function block:

![Schematic](images/149731193995_DV_resource.Stream@PNG-en-US.png)

##### Application examples

You can wire the start and stop buttons of the local control station, for example, to the inputs. These can then be assigned to "Local control stations". If assigned accordingly, the input signals also can be used to activate, for example, function blocks such as "Reset" or "External fault".

##### Basic unit settings

- Debouncing time for inputs

  You can set a debouncing time for the inputs, if required.   
  Range: 6, **16**, 26, 36 ms

#### Operator panel buttons

The operator panel contains buttons 1 to 4 as well as the "TEST/RESET" button. Correspondingly, the "OP buttons" function block is available in SIMOCODE pro with five sockets.

> **Note**
>
> The "OP Buttons" function block can only be used if the operator panel (OP) is connected and configured in the device configuration!

> **Note**
>
> The operator panel with display does not have a TEST/RESET button. The allocated functions can be carried out via the operator panel menu or via softkeys. Similarly, the corresponding status signal will then be available at the "OP Test / Reset Button" socket.

- Buttons 1 to 4, operator panel:  
  Buttons 1 to 4 are usually intended for input of control commands for the motor feeder. Control commands can be, for example:

  - Motor ON (ON>), Motor OFF (OFF) for a direct starter
  - Motor LEFT (ON <), Motor OFF (OFF), Motor RIGHT (ON >) for a reversing starter
  - Motor SLOW (ON >), Motor FAST (ON >>), Motor OFF (OFF) for a Dahlander circuit.

  However, buttons 1 to 4 are not rigidly assigned to the above mentioned control commands, and can be assigned to other functions via different internal connection of the respective function block socket in SIMOCODE pro.
- "TEST/RESET" button, Operator panel:  
  The function of the "TEST/RESET" button is generally assigned to fixed functions:

  - Reset function for the acknowledgement of pending faults
  - Test function for carrying out device plugs
  - Operation of the memory module or the addressing plug.

  Nevertheless, the status of the "TEST/RESET" button is picked off at the corresponding socket of the function block and assigned to further functions in SIMOCODE pro.

##### Schematic

The following schematic shows the "OP buttons" function block:

![Schematic](images/152650581771_DV_resource.Stream@PNG-en-US.png)

#### Digital module inputs

SIMOCODE pro has two "DM Inputs" function blocks, each with four binary inputs connected to common potential. You can connect, for example, the buttons for a local control station to the inputs. These signals can be further processed in SIMOCODE pro by internally connecting the sockets of the "DM Inputs" function blocks.

> **Note**
>
> "DM inputs" function blocks can only be used if the corresponding digital modules (DM) are connected and configured in the device configuration.

> **Note**
>
> When using DM‑F Local and DM‑F PROFIsafe fail-safe digital modules, the input signals are available as non-safety-related information.

Each "DM Inputs" function block consists of:

- Input terminals located on the outside of the digital module, corresponding to the sockets "DM Input 1" to "DM Input 4"
- Sockets in SIMOCODE pro that can be connected to any plugs, e.g. to the "Control stations" function block.

The following are available:

- 1 "DM1 Inputs" function block on the SIMOCODE pro S basic unit <sup>1</sup>
- 1 "DM1 Inputs" function block and 1 "DM2 Inputs" function block on the SIMOCODE pro V and SIMOCODE pro V PN basic units.

> **Note**
>
> 1) For the SIMOCODE pro S basic unit, the DM1 inputs and the temperature input are located on the multifunction module.

##### Schematic (1)

The following schematic shows the "DM1/DM2 Inputs" function blocks:

![Schematic (1)](images/152678219659_DV_resource.Stream@PNG-en-US.png)

##### Schematic (2)

The following schematic shows the "DM1 Inputs" function block as a DM-F Local fail-safe digital module:

![Schematic (2)](images/152678223883_DV_resource.Stream@PNG-en-US.png)

Meaning of the inputs:

Input: 1 - "tripped" state

Start: Start input state (Y33)

Feedback: Feedback circuit state (Y34): 1 - closed; 0 - open

Cascading: Cascading input state (1)

Sensor 1: Sensor circuit 1 state (Y12)

Sensor 2: Sensor circuit 2 state (Y22).

##### Schematic (3)

The following schematic shows the DM1 Inputs function block as fail-safe digital module DM-F PROFIsafe:

![Schematic (3)](images/152678228235_DV_resource.Stream@PNG-en-US.png)

Meaning of the inputs:

Input 1: IN1 (83) state

Input 2: IN2 (85) state

Input 3: IN3 (89) state

Input 4: Feedback circuit state FBC (91): 1 - closed; 0 - open

##### Application examples

Digital modules allow the number of binary inputs and binary outputs on the SIMOCODE pro V basic unit to be increased in increments. The SIMOCODE pro V basic unit can thus be extended to a maximum of twelve binary inputs and seven binary outputs. If assigned accordingly, the input signals can be also used to activate, for example, function blocks such as "Reset" or "External Fault".

##### Digital module settings

- Debouncing time for inputs

  You can set a debouncing time for the inputs, if required.  
  Range: 6, **16**, 26, 36 ms

  These values apply to digital modules with a 24 V DC input supply. The values are approximately 40 ms higher for digital modules with input supplies of 110 to 240 V AC/DC.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Debouncing time**   Debouncing time for the digital module inputs can only be set, or are only relevant, if "monostable" or "bistable" is set for digital module 1.  If digital module 1 is a DM-F PROFIsafe, the debouncing time cannot be set.  If digital module 1 is a DM-F Local, the debouncing times are set using the DIP switch on the front of the DM-F Local. |  |

#### Temperature module inputs

SIMOCODE pro has two function blocks "TM1 Inputs" and "TM2 Inputs" (TM2 inputs only in conjunction with SIMOCODE pro V PN) with three analog sockets corresponding to the three sensor measuring circuits of the temperature module. The temperature (in K) of the three measuring circuits can be read from these sockets and processed internally. An additional analog socket always supplies the maximum temperature of all three measured temperatures.

Furthermore, the two binary sockets of the function block represent the status of the sensor measuring circuits. The temperatures can be processed internally and/or transmitted cyclically to the automation system via the "Cyclic Send" function blocks.

> **Note**
>
> The "TM1 / TM2 Inputs" function blocks can only be used if the corresponding temperature modules (TM1 and / or TM2) have been connected and configured in the device configuration.

##### Schematic

The following schematic shows the "TM1/TM2 Inputs" function block:

![Schematic](images/152678571659_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Wiring**
>
> You can connect up to three 2-wire or 3-wire temperature sensors to a temperature module.
>
> You can connect a 2-wire or 3-wire temperature sensor to a multifunction module.

##### Application examples

Among other things, you can monitor the following motor components:

- Motor windings
- Motor bearings
- Motor coolant temperature
- Motor gearbox oil temperature

The individual temperatures of the three sensor measuring circuits can also be monitored independently of each other by connecting free limit monitors.

##### Temperature module settings

- Sensor type:

  - **PT100**
  - PT1000
  - KTY83
  - KTY84
  - NTC
- Response to sensor fault/out of range as follows:

  - Deactivated
  - Signal
  - **Warn**
  - Trip
- Number of active sensors:

  - 1 sensor
  - 2 sensors
  - **3** sensors

#### Analog module inputs

SIMOCODE pro has two function blocks, "AM1 Inputs" and "AM2 Inputs" (AM2 inputs only in conjunction with SIMOCODE pro V PN / pro V EIP), with two analog sockets each, corresponding to the two analog inputs of the analog module. The effective analog value of each input can be read from these sockets and processed internally.

An additional binary socket of the function block represents the status of the analog measuring circuits. The analog values can be processed internally and/or transmitted cyclically to the automation system via the "Cyclic Send" function blocks.

> **Note**
>
> The AM1/AM2 Inputs function blocks can only be used if the analog modules (AM1 and/or AM2) have been connected and configured in the device configuration!

##### Schematic

The following schematics show the AM1/AM2 Inputs function blocks:

![Schematic](images/152697193483_DV_resource.Stream@PNG-en-US.png)

##### Application examples

Typical applications are, for example:

- Fill-level monitoring for implementing dry running protection for pumps
- Monitoring of pollution in a filter using a differential pressure transducer

##### Analog module settings

- Input signal

  - **0 - 20**mA
  - 4 - 20 mA
- Response to open circuit

  - Signal
  - **Warn**
  - Trip
- Active inputs

  - **1**input
  - 2 inputs

> **Note**
>
> The value of the analog module inputs is in S7 format.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Setting the inputs and output of the analog module**  The inputs of the analog module are passive inputs, i.e. to configure an analog input circuit, each input will require an additional, isolated external current source connected in series. If the output of the analog module is not being used by another application, it can also be used as a current source for an analog module input circuit. The "Start value of value range" and the "End value of value range" of the analog module output have to be set to 65535 for this. Thus, the maximum possible current will always be available via the analog module output. |  |

#### Cyclic receive

With the "Cyclic Receive" function block, you can specify which cyclic data from the automation system will be further processed via the communication bus in SIMOCODE pro. These will normally be PLC/PCS binary control commands. Connection with the "Control Stations" function block in SIMOCODE pro will allow the motor to be controlled via communication bus. Direct connection of the analog value with the "AM Output" function block will result in, for example, the cyclic output of the value sent via PROFIBUS DP or PROFINET at the output of the analog module.

The "Cyclic Receive" function blocks consist of:

- Eight bits each (= 2 bytes, byte 0 and byte 1 for binary information)
- Two words (= 2 bytes, byte 2 to 3 and 4 to 5 for an analog value, freely parameterizable)

Overall there are four "Cyclic Receive" function blocks (0, 1, 2/3, 4/5).

##### Schematic

The following schematic shows the "Cyclic Receive" function blocks:

![Schematic](images/152698534027_DV_resource.Stream@PNG-en-US.png)

##### Cyclic services

PROFIBUS DP:

The cyclic data is exchanged between DP master and DP slave in every DP cycle. The DP master sends the cyclic receive data (Cyclic Receive) to SIMOCODE pro each time. SIMOCODE pro responds by sending the cyclic send data (Cyclic Send) to the DP master.

PROFINET:

The cyclic send data are exchanged between the IO Device (SIMOCODE pro) and the IO Controller (automation system). The IO Controller sends the cyclic receive data to SIMOCODE pro in each case. In response, SIMOCODE pro returns the cyclic send data.

#### Acyclic receive

In addition to "Cyclic Receive", it is possible to transfer further data acyclically to SIMOCODE pro via PROFIBUS DP.

With the "Acyclic Receive" function block, you can specify which acyclic information from PROFIBUS DP will be further processed in SIMOCODE pro. For this, you only have to connect the sockets of the "Acyclic Receive" function blocks to any other function blocks in SIMOCODE pro.

The "Acyclic Receive" function blocks consist of:

- Eight bits each (= 2 bytes, byte 0 and byte 1 for binary information)
- One word (= 2 bytes, byte 2 to 3 for an analog value, freely parameterizable)
- One input each from PROFIBUS DP

Overall there are three "Acyclic Receive" function blocks (0, 1, 2/3).

##### Schematic

The following schematic shows the "Acyclic Receive" function blocks:

![Schematic](images/152698939915_DV_resource.Stream@PNG-en-US.png)

1) Only in case of SIMOCODE pro V PROFIBUS basic unit

##### Acyclic services

Acyclic services will only be transferred on request. The information (4 bytes) can be found in data record 202. This data record can be read by every master (PLC or PC) that supports the acyclic services of PROFIBUS DPV1. Connection monitoring is activated every time the data set is received. The content of the data set is deleted after a 5-second time-out has elapsed.

#### OPC-UA Receive

In addition to "Cyclic Receive," it is possible to transfer further data to SIMOCODE pro via OPC-UA.

With the "OPC-UA Receive" function block, you can specify which information will be further processed in SIMOCODE pro. For this, you only have to connect the sockets of the "OPC-UA Receive" function blocks to any other function blocks in SIMOCODE pro.

The "OPC-UA Receive" function blocks consist of:

- Eight bits each (= 2 bytes, byte 0 and byte 1 for binary information)
- One word (= 2 bytes, byte 2 to 3 for an analog value), freely parameterizable.

A total of 3 OPC-UA Receive function blocks (0, 1, 2/3) are provided.

##### Schematic

The following schematic shows the "OPC-UA Receive" function blocks:

![Schematic](images/152699781387_DV_resource.Stream@PNG-en-US.png)

### 3UF50 compatibility mode

This section contains information on the following topics:

- [3UF50 compatibility mode – function](#3uf50-compatibility-mode-function)
- [3UF50 compatibility mode - diagram of the data](#3uf50-compatibility-mode---diagram-of-the-data)

#### 3UF50 compatibility mode – function

Activate 3UF50 compatibility mode if a SIMOCODE DP device is to be used by a SIMOCODE pro device without changing the configuration. If 3UF50 compatibility mode is activated, you can operate a SIMOCODE pro V basic unit with a 3UF50 configuration. In this case, communication with SIMOCODE pro is the same as communication with SIMOCODE DP from the point of view of the PLC (master class 1). SIMOCODE DP supports cyclic communication (basic types 1-3), diagnostics, as well as DPV1 data sets (DS 130, DS 131, DS 133).

##### 3UF50 operating mode

You can specify here whether SIMOCODE pro V is to be operated on PROFIBUS DP with DPV0 functions (standard) or DPV1 functions (including acyclic services and interrupts).

##### Win SIMOCODE DP Converter

In order for the technical functions (parameterization) of SIMOCODE DP to be integrated into the technical functions of SIMOCODE pro V, the device parameters must be adjusted accordingly. The "Win SIMOCODE DP Converter" software supports you in this process. This software enables you to convert the parameter files (smc files) created with Win SIMOCODE DP into SIMOCODE ES parameter files (sdp files).

##### 3UF50 basic type

You can set here the basic type (1, 2, or 3) used to configure the 3UF50.

##### Safety notices

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Communication with a DP master**  Communication with a DP master (class 2 master), e.g. with the Win SIMOCODE DP Professional software via PROFIBUS DP, is not covered by the 3UF50 compatibility mode. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **3UF50 compatibility mode - transfer of the device parameters**  In the 3UF50 compatibility mode, the startup parameter block is always set, i.e. the transmission of the device parameters created using the SIMOCODE DP GSD or the SIMOCODE DP object manager cannot be integrated into SIMOCODE pro V. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **3UF50 compatibility mode - SIMOCODE DP projects**  The 3UF50 compatibility mode supports SIMOCODE DP projects in which SIMOCODE DP is integrated via GSD SIEM8031.gs?, SIEM8069.gs? or via the SIMOCODE DP Object Manager (OM). |  |

*)  Only for SIMOCODE pro V basic unit with PROFIBUS

#### 3UF50 compatibility mode - diagram of the data

##### Diagram of receive and send data

Control

|  | Basic type 1   SIMOCODE DP | Basic type 1 SIMOCODE pro V |  | Basic type 2   SIMOCODE DP | Basic type 2 SIMOCODE pro V |  | Basic type 3   SIMOCODE DP | Basic type 3 SIMOCODE pro V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Receive data | Cyclic receive bit 0 ... 1.7 | 0 | Receive data | Cyclic receive bit 0 ... 1.7 | 0 | Receive data | Cyclic receive bit 0 ... 1.7 |
| 1 | 1 | 1 |  |  |  |  |  |  |
| 2 | Not supported | 2 | Not supported | 2 | Not supported |  |  |  |
| 3 | 3 | 3 |  |  |  |  |  |  |

Send

|  | Basic type 1   SIMOCODE DP | Basic type 1 SIMOCODE pro V |  | Basic type 2   SIMOCODE DP | Basic type 2 SIMOCODE pro V |  | Basic type 3   SIMOCODE DP | Basic type 3 SIMOCODE pro V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Send data | Cyclic send bit 0.0 .. 1.7 | 0 | Send data | Cyclic send bit 0.0 .. 1.7 | 0 | Send data | Cyclic send bit 0.0 .. 1.7 |
| 1 | 1 | 1 |  |  |  |  |  |  |
| 2 | Motor current | Specified: Max. current I_max | 2 | Motor current | Specified: Max. current I_max | 2 | Cyclic send bit 0.0 ... 1.7 |  |
| 3 | 3 | 3 |  |  |  |  |  |  |
| 4 | Number of starts | Number of starts (bytes 0 ... 3) |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |  |
| 7 | Counter 1 value | Counter 1 value - actual value |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |  |  |
| 9 | Counter 2 value | Counter 2 value - actual value |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |  |  |
| 11 | Sensor value | TM - max. temperature |  |  |  |  |  |  |

##### Diagram of diagnostics data

The following table shows the diagnostics data in 3UF50 compatibility mode:

| Byte, bit | Structure of 3UF50 device-specific diagnostics in accordance with the DP standard of SIMOCODE-DP | Byte, bit | Structure of 3UF50 device-specific diagnostics in accordance with DPV1 SIMOCODE-DP | Equivalent in SIMOCODE pro V |
| --- | --- | --- | --- | --- |
|  |  | 6 | 0x0B | Same as 3UF50 diagnostics |
|  |  | 7 | 0x81 |  |
|  |  | 8 | 0x04 |  |
| 6 | 0x0E | 9 | 0x00 |  |
| 7.0 | Free | 10.0 | Free |  |
| 7.1 | Event: DP block | 10.1 | Event: DP block | Event - startup parameter block active |
| 7.2 | Event: Emergency start | 10.2 | Event: Emergency start | Status - emergency start executed |
| 7.3 | Event: HW test o.k. | 10.3 | Event: HW test o.k. | - No fault - HW fault basic unit - No fault - module fault - No fault - temporary components |
| 7.4 | Free | 10.4 | Free | --- |
| 7.5 | Event: Ext. message 1 | 10.5 | Event: Ext. message 1 | Event: Ext. fault 5 |
| 7.6 | Event: Ext. message 2 | 10.6 | Event: Ext. message 2 | Event: Ext. fault 6 |
| 7.7 | Event: Ext. message 3 | 10.7 | Event: Ext. message 3 | --- |
| 8.0 | Warning: Ext. warning | 11.0 | Warning: Ext. warning | Warning: Ext. fault 3 |
| 8.1 | Warning: Unbalance > 40% | 11.1 | Warning: Unbalance > 40% | Warning. Unbalance |
| 8.2 | Event: Failure PLC-CPU | 11.2 | Event: Failure PLC-CPU | Status - PLC/PCS (inverted) |
| 8.3 | Warning: Sensor short circuit | 11.3 | Warning: Sensor short circuit | Warning - thermistor short circuit |
| 8.4 | Event: Cooling down period active | 11.4 | Event: Cooling down period active | Status - cooling down period active |
| 8.5 | Status TPF | 11.5 | Status: TPF | Status - test position (TPF) |
| 8.6 | Free | 11.6 | Free | --- |
| 8.7 | Free | 11.7 | Free | --- |
| 9.0 | Warning: Ground fault | 12.0 | Warning: Ground fault | - Warning - int. ground fault or - Warning - ext. ground fault |
| 9.1 | Warning: Overload | 12.1 | Warning: Overload | Warning: Overload |
| 9.2 | Warning: Overload + unbalance | 12.2 | Warning: Overload + unbalance | Warning: Overload + unbalance |
| 9.3 | Warning: I1 response level overshot | 12.3 | Warning: I1 response level overshot | Warning - Warning level I> |
| 9.4 | Warning: I1 response level undershot | 12.4 | Warning: I1 response level undershot | Warning - Warning level I< |
| 9.5 | Warning: I2 response level overshot | 12.5 | Warning: I2 response level overshot | --- |
| 9.6 | Warning: I2 response level undershot | 12.6 | Warning: I2 response level undershot | --- |
| 9.7 | Warning: Thermistor | 12.7 | Warning: Thermistor | - Warning - thermistor overload - Warning - thermistor open circuit - Warning - TM warning T> - Warning - TM sensor fault - Warning - TM out of range |
| 10.0 | Trip: Ground fault | 13.0 | Trip: Ground fault | - Fault - int. ground fault or - Fault - ext. ground fault |
| 10.1 | Trip: Overload | 13.1 | Trip: Overload | Fault - overload |
| 10.2 | Trip: Overload + unbalance | 13.2 | Trip: Overload + unbalance | Fault - overload + phase failure |
| 10.3 | Trip: I1 response level overshot | 13.3 | Trip: I1 response level overshot | Fault - trip level I> |
| 10.4 | Trip: I1 response level undershot | 13.4 | Trip: I1 response level undershot | Fault - trip level I< |
| 10.5 | Trip: I2 response level overshot | 13.5 | Trip: I2 response level overshot | --- |
| 10.6 | Trip: I2 response level undershot | 13.6 | Trip: I2 response level undershot | --- |
| 10.7 | Trip: Thermistor | 13.7 | Trip: Thermistor | - Fault - thermistor overload - Fault - thermistor short circuit - Fault - thermistor open circuit - Fault - TM trip T> - Fault - TM sensor fault - Fault - TM out of range |
| 11.0 | Trip: FB ON | 14.0 | Trip: FB ON | Fault - feedback ON |
| 11.1 | Trip: FB OFF | 14.1 | Trip: FB OFF | Fault - feedback OFF |
| 11.2 | Trip: Stalled rotor | 14.2 | Trip: Stalled rotor | Fault - stalled rotor |
| 11.3 | Trip: Stalled positioner | 14.3 | Trip: Stalled positioner | Fault - stalled positioner |
| 11.4 | Trip: Double 0 | 14.4 | Trip: Double 0 | Fault - double 0 |
| 11.5 | Trip: Double 1 | 14.5 | Trip: Double 1 | Fault - double 1 |
| 11.6 | Trip: End position | 14.6 | Trip: End position | Fault - end position |
| 11.7 | Trip: Antivalence | 14.7 | Trip: Antivalence | Fault - antivalence |
| 12.0 | Trip: ESB | 14.0 | Trip: ESB | Fault - ext. fault 4 |
| 12.1 | Trip: OPO | 15.1 | Trip: OPO | Fault - Operational Protection Off (OPO) |
| 12.2 | Trip: UVO | 15.2 | Trip: UVO | Fault - undervoltage (UVO) |
| 12.3 | Trip: Ext. fault 1 | 15.3 | Trip: Ext. fault 1 | Fault - ext. fault 1 |
| 12.4 | Trip: Ext. fault 2 | 15.4 | Trip: Ext. fault 2 | Fault - ext. fault 2 |
| 12.5 | Trip: TPF fault | 15.5 | Trip: TPF fault | Fault - cold start (TPF) fault |
| 12.6 | Trip: Runtime On | 15.6 | Trip: Runtime On | Fault - execution ON command |
| 12.7 | Trip: Runtime OFF | 15.7 | Trip: Runtime OFF | Fault - execution OFF command |
| 13.0 | Trip: Parameter fault 0 | 16.0 | Trip: Parameter fault 0 | Fault - parameterization |
| 13.1 | Trip: Parameter fault 1 | 16.1 | Trip: Parameter fault 1 | --- |
| 13.2 | Trip: Parameter fault 2 | 16.2 | Trip: Parameter fault 2 | --- |
| 13.3 | Trip: Parameter fault 3 | 16.3 | Trip: Parameter fault 3 | --- |
| 13.4 | Trip: Parameter fault 4 | 16.4 | Trip: Parameter fault 4 | Fault - configuration error |
| 13.5 | Trip: Parameter fault 5 | 16.5 | Trip: Parameter fault 5 | --- |
| 13.6 | Trip: Parameter fault 6 | 16.6 | Trip: Parameter fault 6 | --- |
| 13.7 | Trip: Parameter fault 7 | 16.7 | Trip: Parameter fault 7 | Fault - HW fault basic unit |
| 14 ... 15 | Number of overload trips |  |  | Number of overload trips |
| 16 ... 17 | I of the overload trip [%/IE] |  |  | Last trip current |
| 18 ... 19 | Operating hours [10 h] |  |  | Motor operating hours |

### Analog value recording

With the "Analog value recording" function, you record any analog values (2 bytes/1 word) in SIMOCODE pro.

You can create different recordings (traces) that are also stored device-specifically.

- Establish the online connection in the project navigation via Online accesses (Update accessible devices), or via the "Connect Online" button. All stations (devices) accessible via PROFIBUS, PROFINET and point-to-point (PtP) are listed in the "Online accesses" folder.
- Open the menu item "Traces" in the project tree.
- Create a recording by double-clicking on the button "Add new trace", or select a recording by double-clicking
- Select "Analog value recording" as the active configuration.
- In the line "Assigned signal (analog)", select the analog signal to be recorded
- Select the relevant digital trigger signal in the line "Trigger signal (digital)"
- Select a pre-trigger value
- Select a sampling rate
- Transfer the trace configuration to the device using the relevant buttons.

Up to 60 values can be recorded, displayed graphically, and saved as csv files.

You can export the trace configuration and the measurement with the settings of the current view.

"Trigger event occurred" display: After the defined trigger event has occurred, and the edge is simultaneously present, the status is indicated via status messages (e.g. Wait for trigger event, Recording, Recording completed). After the trigger event, 60 values are recorded again.

The recording is made direct in SIMOCODE pro, related to the motor feeder, and independently of PROFIBUS or the automation system.

Each value present at the analog output "assigned analog value" is recorded and saved. Recording starts on the basis of the edge (positive/negative) via any binary signal at the trigger input of the function block. Up to 60 values can be saved internally in the device. The time frame of the recording is indirectly determined by the selected sampling rate.

You can add the recordings to the measurements using the button "Add to measurements".

You can also manually add a measurement to the measurements, export the trace configuration, and export with the settings of the current view. To do this, click on the relevant symbols.

> **Note**
>
> **Information system**
>
> You reach the detailed Help via the Tooltip Help of the symbols (information system). You will also find the corresponding help topics there under "Using online and diagnostics functions → Using the trace and logic analyzer function"

#### Sampling time = sampling rate [s] x 60 values

The pre-trigger is used to specify how far in advance the recording should commence before the trigger signal is issued. The pre-trigger is set as a percentage of the total sampling time.

#### Schematic

The following schematic shows the "Analog value recording" function block:

![Schematic](images/152700344459_DV_resource.Stream@PNG-en-US.png)

#### Signal/value settings

- Trigger input: Start of analog value recording with any signal (any outputs, e.g. device inputs, current flowing)
- Assigned analog value: Any value (1 word/2 bytes) in SIMOCODE pro
- Trigger edge: **Positive**/ negative
- Sampling rate: **0.1** to 50 seconds in 0.1-s increments
- Pre-trigger: **0** to 100 % in 5-% increments

#### Setting options for scales and measured curves

The y‑axis shows the measured values or signals, and the x‑axis shows the time.

A separate y‑scale with a specific color is shown for each measured curve.

**Scale:**

The scales of the x‑axis and the y‑axis can be adjusted dynamically and infinitely using the mouse (while holding down the left mouse key) as follows:

- Changing the maximum upper scale value: Drag the mouse cursor upwards in the scale range while holding the mouse key pressed.
- Changing the maximum lower scale value: Drag the mouse cursor downwards in the scale range while holding the mouse key pressed.

This changes the mouse pointer to the symbol ![Setting options for scales and measured curves](images/148921714955_DV_resource.Stream@PNG-de-DE.png) in the scale range.

By double-clicking with the left mouse key in the scale range, a scale is reset to its default setting.

The upper and lower scale value of the y axis can each be blocked with a ![Setting options for scales and measured curves](images/148921732107_DV_resource.Stream@PNG-de-DE.png) button.

The left and right scale value of the x axis can each be blocked with a ![Setting options for scales and measured curves](images/148921732107_DV_resource.Stream@PNG-de-DE.png) button.

Each measured curve can be shown and hidden via its own checkbox.

**Zooming:**

You can zoom the measured curves using the following buttons:

- Zoom in horizontally: ![Setting options for scales and measured curves](images/148921770635_DV_resource.Stream@PNG-de-DE.png)
- Zoom out horizontally: ![Setting options for scales and measured curves](images/148921813387_DV_resource.Stream@PNG-de-DE.png)
- Zoom in vertically: ![Setting options for scales and measured curves](images/148921843339_DV_resource.Stream@PNG-de-DE.png)
- Zoom out vertically: ![Setting options for scales and measured curves](images/148921860491_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Information system**
>
> You will find the corresponding help for symbols in the information system under "Using online and diagnostics functions → Using the trace and logic analyzer function → Software interface → Work area → Interface - Diagram tab → Interface → Curve diagram".

### Outputs

This section contains information on the following topics:

- [Basic unit outputs](#basic-unit-outputs)
- [Operator panel LED](#operator-panel-led)
- [Digital module outputs](#digital-module-outputs)
- [Analog module output](#analog-module-output)
- [Cyclic send data](#cyclic-send-data)
- [Acyclic send data](#acyclic-send-data)
- [Acyclic send](#acyclic-send)
- [OPC-UA Send](#opc-ua-send)

#### Basic unit outputs

In this dialog you can connect the three inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

SIMOCODE pro has a "BU Outputs" function block with two or three relay outputs. You can, for example, switch contactors or lamps via these relay outputs. For this, the inputs (plugs) of the function block must be connected to the respective sockets (usually the QE. contactor controls of the control function).

The "BU Outputs" function block consists of:

- Three plugs corresponding to the relay outputs Out1 to Out3
- Three relays
- Output terminals

One "BU Outputs" function block is available for the SIMOCODE pro C, pro S, pro V, pro V MB RTU, pro V PN and pro V EIP basic units.

##### Schematic

The schematic below shows the "BU Outputs" function block for the SIMOCODE pro C, pro V, pro V MB RTU, pro V PN and pro V EIP basic units.

![Schematic](images/152701719435_DV_resource.Stream@PNG-en-US.png)

The following schematic shows the "BU Outputs" function block on the SIMOCODE pro S basic unit:

![Schematic](images/152701736459_DV_resource.Stream@PNG-en-US.png)

##### Application examples

- Activation of the main contactor in the motor feeder: You can, for example, define which relay output is used for activating the motor contactor in the motor feeder. To do this, connect the desired relay output to the respective "QE." contactor control of the control function.
- Activation of lamps for displaying operating states: You can define, for example, which relay outputs are to be used for displaying lamps/LEDs (Fault, ON, OFF, FAST, SLOW, ...). To do this, connect the desired relay output to the respective "QE..." contactor control of the control function. These are provided specially for controlling lamps and LEDs.

In addition to the status signals, the "QL..." lamp controls automatically signal the following using a 2-Hz flashing frequency:

- Test mode (QLE.../QLA lamp outputs are flashing)
- Unacknowledged fault (lamp output general fault QLS is flashing)
- Transfer of any other information, status information, warnings, faults, etc. to the relay outputs
- Lamp test: All QL outputs are activated for approx. 2 s.

In most cases, the outputs of the basic unit will be connected to the QE or QL outputs.

##### BU outputs settings

- Outputs 1 to 3: Control of the "BU Outputs" function block via any signal (any socket, e.g., device inputs, PROFIBUS DP control bits, etc.), usually from the QE contactor controls

#### Operator panel LED

In this dialog, you can connect each of the seven inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

SIMOCODE pro has an "OP LED" function block for controlling the seven freely usable LEDs. The LEDs are located in the operator panel and can be used for any status displays. For this, the inputs (plugs) of the "OP LED" function block must be connected to the respective sockets (e.g. to the sockets for the status information of the control function).

> **Note**
>
> The "OP LED" function block can only be used if the operator panel (OP) is connected and configured in the device configuration!

The "OP LED" function block consists of:

- Four plugs, "OP LED green 1" to "OP LED green 4", corresponding to the green LEDs. The green LEDs are assigned visually/mechanically to the buttons on the operator panel. They normally display feedback concerning the motor operating state.
- Three plugs, "OP LED yellow 1" to "OP LED yellow 3", corresponding to the yellow LEDs
- Four green LEDs
- Three yellow LEDs (not for the operator panel with display).

One OP LED function block is available for the SIMOCODE pro C, pro S, pro V, pro V MB RTU, pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "OP LED" function block:

![Schematic](images/152702178571_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The three yellow LEDs mentioned in this section are not available for the operator panel with display. Status information can be read out here directly via the display. While it is still possible to connect the corresponding three plugs via the software, they remain non-functional.

##### Application examples

- Display of operating states: You can define, for example, which LEDs are to be controlled to display the operating states of the motor (Fault, ON, OFF, FAST, SLOW...). To do this, connect the desired LED to the respective "QL." lamp control of the control function. In many cases, the LEDs are connected with the QL outputs.
- Transfer of any other information, status information, warnings, faults, etc. to the yellow LEDs.

##### Operator panel LED settings

In this dialog, you can connect each of the seven inputs (plugs) to a socket. To do so, choose the appropriate socket ☑ in the scroll boxes.

- Green 1 to Green 4: The "OP-LED" function block can be activated by any signal (any sockets, e.g., feedback, motor operating state)
- Yellow 1 to yellow 3: The "OP-LED" function block can be activated by any signal (any sockets, e.g., displays for status, events, faults)

#### Digital module outputs

In this dialog, you can connect each of the two inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

SIMOCODE pro has two "DM1 Outputs" and "DM2 Outputs" function blocks, which are each equipped with two relay outputs. You can, for example, switch contactors or lamps via these relay outputs. For this, the inputs (plugs) of the "DM Outputs" function blocks must be connected to the respective sockets (e.g. of the control function).

> **Note**
>
> "DM Outputs" function blocks can only be used if the corresponding digital modules (DM) are connected and configured in the device configuration!

Each function block has

- Two plugs, corresponding to relay outputs Out1, Out2
- Two relays
- Output terminals.

The following are available:

- One "DM1 Outputs" function block on the SIMOCODE pro S basic unit <sup>1)</sup>
- Two "DM1 Outputs" and "DM2 Outputs" function blocks for the SIMOCODE pro V, pro V MB RTU, pro V PN and pro V EIP basic units.

> **Note**
>
> 1) For the SIMOCODE pro S basic unit, the DM1 outputs are on the multifunction module.

> **Note**
>
> In addition to the two jointly-switched fail-safe enabling circuits, the fail-safe DM-F Local and DM-F PROFIsafe digital modules are equipped with two standard relay outputs, the common potential of which is switched off for safety reasons via an enabling circuit.
>
> From a logical connection point of view, the standard relay outputs are always switched. The state of the fail-safe enabling circuits is not affected by the logical wiring.

##### Schematic

The following schematic shows the "DM1 Outputs" and "DM2 Outputs" function blocks:

![Schematic](images/152703029899_DV_resource.Stream@PNG-en-US.png)

##### Application examples

- Activation of the motor contactor in the motor feeder: You can, for example, define which relay output is to be used for activating the main contactor in the motor feeder. To do this, connect the desired relay output to the respective "QE" contactor control of the control function.
- Activation of lamps for displaying operating states: You can define, for example, which relay outputs are to be used for controlling the lamps/LEDs that display the operating states of the motor (Fault, ON, OFF, FAST, SLOW...). To do this, connect the desired relay output to the respective "QL..." lamp control of the control function.
- Transfer of any other information, status information, warnings, faults, etc. to the relay outputs.

In many cases, the outputs of the digital module will be connected to the QE outputs.

##### "DM1/DM2 outputs" settings

- Outputs 1 to 2: Control of the "DM1 Outputs" and "DM2 Outputs" function blocks via any signal (any socket, e.g. device inputs, PROFIBUS DP control bits etc., usually from the QE contactor controls).

---

**See also**

[Application selection](#application-selection)
  
[Contactor controls](#contactor-controls)
  
[Lamp controls and status information](#lamp-controls-and-status-information)

#### Analog module output

You can use analog modules 1 and 2 (SIMOCODE pro V PN / EIP only) to expand the basic unit with one analog output in each case. The corresponding function blocks "AM1 Output" and "AM2 Output" (in conjunction with the SIMOCODE pro V PN and pro V EIP basic units) allow every analog value (2 bytes/1 word) in SIMOCODE pro to be output as a 0/4 A - 20 mA signal to a connected pointer instrument, for example. By activating the function block via the "Assigned analog output value" plug with any integer value between 0 and 65535, an equivalent analog signal of 0 to 20 mA will be sent to the output terminals of the analog module.

> **Note**
>
> The "AM1 Output" and "AM2 Output" function blocks can only be used if the respective analog module (AM) is connected and configured in the device configuration.

##### Schematic

The following schematic shows the "AM1 Output" and "AM2 Output" function blocks:

![Schematic](images/152703331339_DV_resource.Stream@PNG-en-US.png)

##### Signal/value settings

- Assigned analog output value: Any value (1 word/2 bytes) in SIMOCODE pro
- Output signal: **0 to 20 mA**, 4 to 20 mA
- Start value of value range: **0** to 65535
- End value of value range: **0** to 65535

##### Application examples 1)  Output of the effective motor current - across the entire motor current range

The motor current of a motor is within the range 0 to 8 A.

The rated current I<sub>N</sub> of the motor at rated load is 2 A.

The set current in SIMOCODE ES I<sub>s</sub> corresponds to the rated current I<sub>N</sub> (2 A). The effective phase currents or the maximum current (current IL_1, IL_2, IL_3, max. current I_max) are represented in SIMOCODE pro in accordance with the selected range as a percentage of the parameterized set current I<sub>s</sub>:

- 0 A motor current corresponds to 0% of I<sub>s</sub>
- 8 A motor current corresponds to 400% of I<sub>s</sub>
- The smallest unit for the effective motor current in SIMOCODE pro is 1%

As a result,

- the "Start value of value range" to be selected is: 0
- The "End value of value range" to be selected is: 400

If "Output signal = 0 - 20 mA" is parameterized, the following applies:

- 0% motor current: 0 mA at the analog module output
- 400% motor current: 20 mA at the analog module output

If "Output signal = 4 - 20 mA" is parameterized, the following applies:

- 0% motor current: 4 mA at the analog module output
- 400% motor current: 20 mA at the analog module output

##### 2) Output of the effective motor current - only part of the motor current range (overload range)

The motor current of a motor is within the range 0 to 8 A.

The rated current I<sub>N</sub> of the motor at rated load is 2 A.

The set current in SIMOCODE ES I<sub>s</sub> corresponds to the rated current I<sub>N</sub>

(2 A). However, only the overload range (2 A - 8 A) is to be displayed on an instrument via the analog module output.

The effective phase currents or the maximum current (current IL_1, IL_2, IL_3, max. current I_max) are represented in SIMOCODE pro in accordance with the selected range as a percentage of the parameterized set current I<sub>s</sub>

- 2 A motor current corresponds to 100% of I<sub>s</sub>
- 8 A motor current corresponds to 400% of I<sub>s</sub>
- The smallest unit for the effective motor current in SIMOCODE pro is 1%

As a result,

- the "Start value of value range" to be selected is: 100.
- the "End value of value range" to be selected is: 400.

If "Output signal = 0 - 20 mA" is parameterized, the following applies:

- 100% motor current: 0 mA at the analog module output
- 400% motor current: 20 mA at the analog module output

If "Output signal = 4 - 20 mA" is parameterized, the following applies:

- 100% motor current: 4 mA at the analog module output
- 400% motor current: 20 mA at the analog module output

##### 3) Output of any analog value from the automation system (cyclically via PROFIBUS)

One word (2 bytes) can be transmitted cyclically from the automation system to SIMOCODE pro via PROFIBUS. Any value can be output as a 0/4 to 20mA signal by directly connecting this cyclic control word from the PROFIBUS to the analog module output. If the transmitted value is in S7 Format (0 to 27648), this must be taken into consideration when parameterizing.

As a result,

- the "Start value of value range" to be selected is: 0
- the "End value of value range" to be selected is: 27648.

If "Output signal = 0 - 20 mA" is parameterized, the following applies:

- 0: 0 mA at the analog module output
- 27648: 20 mA at the analog module output

If "Output signal = 4 - 20 mA" is parameterized, the following applies:

- 0: 4 mA at the analog module output
- 27648: 20 mA at the analog module output

##### 4)  Output of any analog value from the automation system via PROFINET

Two words (2 x 2 bytes) can be transmitted from the automation system to SIMOCODE pro via PROFINET, depending on the basic type. Any value can be output as a 0/4 - 20 mA signal by directly connecting this cyclic control word to the analog module output. If the transmitted value is in S7 Format (0 to 27648), this must be taken into consideration when parameterizing:

As a result,

- the "Start value of value range" to be selected is: 0
- the "End value of value range" to be selected is: 27648.

If "Output signal = 0 - 20 mA" is parameterized, the following applies:

- 0: 0 mA at the analog module output
- 27648: 20 mA at the analog module output

If "Output signal = 4 - 20 mA" is parameterized, the following applies:

- 0: 4 mA at the analog module output
- 27648: 20 mA at the analog module output

#### Cyclic send data

In this dialog, you can connect each of the inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

The "Cyclic Send" function blocks allow you to specify the information to be transferred cyclically to the automation system via the communication bus.

"Cyclic Send" function blocks consist of

- Eight bits each (two bytes, byte 0 and byte 1 for binary information)
- Nine words (= 18 bytes, bytes 2 to 19 for nine analog values, freely parameterizable)

A total of nine Cyclic Send function blocks (0, 1, 2/3, 4/9, 10/19, 2-5, 6-9, 10-13, 14-17) are available.

##### Schematic

The following schematic shows the "Cyclic Send" function blocks:

![Schematic](images/152703991051_DV_resource.Stream@PNG-en-US.png)

##### Cyclic PROFIBUS DP services

Cyclic send data is exchanged between the controller and the SIMOCODE once in every DP cycle. The controller sends the cyclic receive data to SIMOCODE pro in each case. SIMOCODE pro responds by sending the cyclic send data to the controller.

You access the cyclic data in the PLC software via the inputs (send data) and the outputs (receive data). The length of the cyclic data which is to be transferred is set when SIMOCODE pro is integrated into the control system. This is achieved by selecting the basic type which in turn determines the structure and the length of the cyclic data.

The following basic types are available:

- Cyclic data from the PROFIBUS controller to SIMOCODE pro
- Cyclic data from SIMOCODE pro to the PROFIBUS controller.

##### Cyclic services for PROFINET / EtherNet/IP

The cyclic send data are exchanged between the IO‑Device / Adapter (SIMOCODE pro) and the IO‑Controller / Scanner (automation system). The IO controller sends the cyclic receive data to SIMOCODE pro in each case. In response, SIMOCODE pro returns the cyclic send data.

##### Cyclic send data settings

The cyclic send data is divided up into the following ranges:

- Byte 0/1, bit 0 - bit 7: For assignment of the bits with any signals (e.g. device inputs, events, faults)
- Bytes 2-19: For assignment with any analog values (length: 2 bytes, e.g. maximum current I_max in %, remaining cooling down period, actual value of timers) or floating-point values (length: 4 bytes, only with current/voltage measuring module UM+, e.g. maximum current I_max in A).

The number of available bytes depends on the basic type selected.

The following basic types are available for the following device series:

| Basic type | SIMOCODE pro |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| C | S | V PN GP | V PB | V PN |  |
| **1** (byte 2-9) | — | ✓ | ✓ | ✓ | ✓ |
| **2** (byte 2/3) | ✓ | ✓ | ✓ | ✓ | ✓ |
| **3** (byte 2-19) | — | — | ✓ | — | ✓ |

Byte 0 of the send data is already pre-assigned; byte 2/3 is pre-assigned with the max. current I_max.

#### Acyclic send data

In this dialog, you can connect each of the inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

In addition to "Cyclic Send" it is also possible to transfer a further 16 bits of binary information to the PLC/PC via acyclic services.

The "Acyclic Send" function blocks allow you to specify the information to be transferred acyclically to the automation system via PROFIBUS DP. The inputs (plugs) of the function blocks must be connected to the respective sockets.

"Acyclic Send" function blocks consist of

- Eight bits each (= two bytes, byte 0 and byte 1 for binary information)
- One output to PROFIBUS DP each.

A total of 2 Acyclic Send function blocks are available for the SIMOCODE pro C, SIMOCODE pro S, and SIMOCODE pro V PB basic units.

##### Schematic

The following schematic shows the "Acyclic Send" function blocks:

![Schematic](images/152704497163_DV_resource.Stream@PNG-en-US.png)

##### Acyclic services

Acyclic send data will only be transferred on request. The information (two bytes) can be found in data record 203. This data record can be read by every master (PLC or PC) that supports the acyclic services of PROFIBUS DPV1.

##### Acyclic send data settings

Bytes 0 to 1, bits 0 to 7:

Setting and resetting of bits by means of any signal (any socket, e.g. device inputs, send data, status information, events, etc.)

#### Acyclic send

In this dialog, you can connect each of the inputs (plugs) to a socket. To do so, choose the appropriate socket in the scroll boxes.

In addition to "Cyclic Send" it is also possible to transfer a further 16 bits of binary information to the PLC / PC via acyclic services. The "Acyclic Send" function blocks allow you to specify the information to be transferred acyclically to the automation system via the communication bus. The inputs (plugs) of the function blocks must be connected to the respective sockets.

The "Acyclic send" function blocks comprise 8 bits each (2 bytes, byte 0 and byte 1 for binary information).

Overall there are 2 "Acyclic send (0, 1)" function blocks.

##### Schematic

The following schematic shows the "Acyclic send" function blocks:

![Schematic](images/152729437451_DV_resource.Stream@PNG-en-US.png)

##### Acyclic send data settings

Bytes 0 to 1, bits 0 to 7 Setting and resetting of bits by means of any signal (any socket, e.g. device inputs, send data, status information, events, etc.)

#### OPC-UA Send

In addition to "Cyclic Send," it is possible to transfer a further 16 bits of binary information via OPC-UA.

With the "OPC-UA Send" function block, you can specify which information is to be transferred. The inputs (plugs) of the function blocks must be connected to the respective sockets

The "OPC-UA Send" function blocks comprise 8 bits each (2 bytes, byte 0 and byte 1 for binary information).

Overall there are 2 "OPC-UA Send (0, 1)" function blocks.

##### Schematic

The following schematic shows the "OPC-UA Send" function blocks:

![Schematic](images/152738827403_DV_resource.Stream@PNG-en-US.png)

##### OPC-UA Send data settings

Bytes 0 to 1, bits 0 to 7 Setting and resetting of bits by means of any signal (any socket, e.g. device inputs, send data, status information, events, etc.)

> **Note**
>
> Data record 203 can continue to be read by every Master (PLC or PC) as acyclic send data.

### Standard functions

This section contains information on the following topics:

- [Test/Reset](#testreset)
- [Test position feedback (TPF)](#test-position-feedback-tpf)
- [External fault (1 to 6)](#external-fault-1-to-6)
- [Operational protection OFF (OPO)](#operational-protection-off-opo)
- [Power failure monitoring (UVO)](#power-failure-monitoring-uvo)
- [Emergency start](#emergency-start)
- [Safety-related tripping](#safety-related-tripping)
- [Watchdog (Bus monitoring, PLC/PCS monitoring)](#watchdog-bus-monitoring-plcpcs-monitoring)
- [Time stamping](#time-stamping)

#### Test/Reset

The function of the "TEST/RESET" button on the basic unit or operator panel is generally dependent upon the operating state of the device:

- Reset function: If a fault occurs
- Test function: In other operating states

In addition to the TEST/RESET buttons, SIMOCODE pro allows internal Test/Reset tripping via the "Test" function blocks. The "Test" function block consists of one plug.

In total, two function blocks, "Test 1" and "Test 2," are provided, each function block having a slightly different function:

- Test 1: Tests/trips of the output relays
- Test 2: Does not trip the output relays (normally for testing via the bus)

##### Schematic

The following schematic shows a general representation of the "Test/Reset" function blocks:

![Schematic](images/152743265291_DV_resource.Stream@PNG-en-US.png)

##### Testing

Testing can be carried out as follows:

- Via the "TEST/RESET" button on the basic unit and on the operator panel (can be deactivated), as well as via PC with the SIMOCODE ES software
- Via the plugs of the internal "Test 1" or "Test 2" function blocks
- Via the menu of the operator panel with display (e.g. the "Commands" menu item)

Testing can be terminated at any time - it does not influence the thermal motor model of the overload function, i.e. after switching off via test, the system can be shut down immediately. Tripping only occurs for the "Test 1" function block when the operating mode is set to "Remote".

##### Reset function

Resetting can be carried out as follows:

- Via the "TEST/RESET" button on the basic unit and on the operator panel (can be deactivated), as well as via PC with the SIMOCODE ES software
- Via the plugs of the internal "Reset 1", "Reset 2" or "Reset 3" function blocks
- Via the menu of the operator panel with display (e.g. the "Commands" menu item)

The "Reset" function block consists of one plug.

A total of three function blocks, Reset 1 to 3, are available All reset inputs (sockets) are equal (OR function).

##### Test function

A SIMOCODE pro function test can also be initialized via the test function.

The test function comprises the following steps:

- Lamp / LED test (test function activated for < 2 s)
- Test of the device functionality (test function activated for 2 s - 5 s)
- For "Test 1" function block only: Switching off the QE (test function activated > 5 s).

##### Settings for test 1 to 2

- Input: Activation of the "Test" function block by any signal (any sockets, e.g. device inputs, communication bus control bits, etc.)
- TEST/RESET buttons blocked: The blue TEST/RESET buttons on the basic unit and the operator panel are usually intended for acknowledging faults and for performing a device test. The buttons can be disabled with "TEST/RESET keys disabled". These can then be used for other purposes. On the operator panel with display, blocking is carried out via the corresponding menu function (default: not blocked)

##### Acknowledgment of faults

Generally, the following applies to the acknowledgement of faults:

- Faults can only be acknowledged

  - if the cause of the fault has been eliminated
  - if there is no "On" control command pending
- A reset will not be possible if the cause of the fault has not been eliminated and/or if an "ON" control command is pending. The reset will be saved depending on the type of fault. Saving a reset is indicated by the "GEN. FAULT" LED on the basic unit and on the operator panel. The LED changes from flashing to continuous signal.

##### Automatic acknowledgement of faults

Faults are automatically acknowledged in the following cases:

- A reset has been saved and the cause of the fault is no longer present (user has previously acknowledged the fault)
- Auto reset of an overload trip or thermistor trip if motor protection reset = Auto (an automatic acknowledgment is issued here after expiry of the cooling down period). The motor cannot start immediately since reset cannot be performed when an ON command is pending.
- If a configured module fails, all related faults will be acknowledged automatically. However, a configuration error will be generated (exception: operator panel, if parameterized accordingly).
- If a function or module is deactivated in the device configuration (via parameterization), all related faults are acknowledged automatically.
- If a parameter of a function is changed from "Trip" to "Warn", or to "Signal" or "Deactivated".
- For an external fault: With its own parameter: "Auto reset"

##### Settings for reset 1 to 3

- Input: Activation of the "Reset" function block by any signal (any sockets, e.g. device inputs, communication bus control bits, etc.).
- TEST/RESET buttons blocked: The blue TEST/RESET buttons on the basic unit and the operator panel are usually intended for acknowledging faults and for performing a device test. The buttons can be disabled with "TEST/RESET keys disabled". These can then be used for other purposes. For the operator panel with display, activating the "Test/Reset keys disabled" function means that the "Execute test/reset" function in the "Commands" menu can no longer be executed.

#### Test position feedback (TPF)

You can carry out the "Cold run" function test using the "Test Position Feedback (TPF)" function block. For this purpose, the function block input (plug) must be connected to the respective socket. The active test position is signaled by flashing QL of the control function.

The "Test Position Feedback (TPF)" function block comprises:

- One plug
- One "Status - test position" socket. The output is set if a signal is pending at the input.
- One "Fault - test position feedback error" socket. The output is set when

  - "TPF" is activated although current is flowing in the main circuit
  - "TPF" is activated and current is flowing in the main circuit.

In total, one "Test Position Feedback" function block is available.

In this dialog, you can:

- Connect the input (plug) with a socket. To do so, choose the appropriate socket in the scroll boxes.
- Select the input logic (NO/NC contact) under "Type".

  > **Note**
  >
  > When the test position is enabled, the QLE/QLA sockets of the control function are activated to indicate test operation of the motor feeder via a flashing button LED, for example.

##### Schematic

The following schematic shows the "Test Position Feedback" function block:

![Schematic](images/152745865611_DV_resource.Stream@PNG-en-US.png)

##### Cold run

If the motor feeder is in the test position, its main circuit is isolated from the network. However, the control voltage is connected.

The "cold run" function test is performed with the feeder in this state. This means the motor feeder is tested without a current in the main circuit.

To enable this function to be differentiated from normal operation, it must be activated via the socket on the function block.

The feedback that the motor feeder is disconnected from the line voltage on the primary current side can be made, for example, via an auxiliary contact of the main switch in the motor feeder, wired to any device input (terminal). This is then internally connected to the "Test position feedback (TPF) - Input" plug of the function block.

When using current/voltage measuring modules, this type of auxiliary contact is entirely unnecessary. The "TPF" function block can be activated by monitoring for undervoltage ("Voltage Monitoring" function block).

##### "Fault - Test Position Feedback (TPF)" fault message and acknowledgement

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Generate "Fault - Test position feedback (TPF)"**  "Fault - Test Position Feedback (TPF)" will be generated if:  • "TPF" is activated, although current is flowing in the motor feeder  • "TPF" is activated and current is flowing in the motor feeder. |  |

Acknowledge with "Reset".

##### Test position feedback (TPF) settings

- Input: Activation of the "Test Position Feedback (TPF)" function block by any signal (any sockets, e.g., device input)
- Type: Specification of the input logic

  - **NO contact (1-active)**
  - NC contact (0-active)

#### External fault (1 to 6)

The "External Fault 1-6" function blocks can be used to monitor any statuses and/or external devices, to generate fault messages and, if necessary, to switch off the motor. To do this, the inputs (plugs) of the "External Fault" function blocks must be connected to any sockets (e.g. device inputs, PROFIBUS DP control bits, etc.). External faults can also be marked in SIMOCODE pro. This facilitates their allocation to the actual malfunction.

Example: monitoring the rotational speed of the motor using an external speed monitor.

The "External Fault" function block consists of:

- Two plugs (1 plug for setting, 1 plug for resetting)
- One "Event - external fault" socket. It is set if a signal is pending at the input.

The following are available:

- Four "External Faults 1 to 4" function blocks for the SIMOCODE pro C and pro S basic units
- Six "External Faults 1 to 6" function blocks for the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units

##### Schematic

The following schematic shows the "External Fault" function blocks:

![Schematic](images/152747801227_DV_resource.Stream@PNG-en-US.png)

##### Special reset options

A specific reset input is also available in addition to the other reset options (remote reset, Test/Reset buttons, OFF command reset).

Furthermore, auto reset can also be activated (see "Settings").

##### External fault 1 to 6 settings

- Input  
  Activation of the "External Fault" function block by the monitored signal (any sockets, e.g. device inputs, PROFIBUS DP control bits, etc.)
- Type: Specification of the input logic:

  - **NO contact (1-active)**
  - NC contact (0-active)
- Activity Specify in which motor operating state the external fault is to be evaluated:

  - **Always**: Always evaluate, regardless of whether the motor is running or at a standstill
  - Only if motor is ON: Evaluation only if motor is switched ON
- Response: Specification of the response to an external fault when activated via the input (see the "Response" table)
- Reset: Acknowledge the "external fault" fault via any signal (any sockets, e.g., device inputs, PROFIBUS DP control bits, etc.)
- Reset also by specifying further (common) acknowledgement options using additional reset types:

  - TEST/RESET buttons on the basic unit and the operator panel or, in the case of the operator panel with display, via the menu (panel reset)
  - Remote reset: Acknowledgment via reset 1-3, DPV1, "Reset" command
  - Auto reset: The fault resets itself after the cause has been eliminated (after removal of the activation signal)
  - Auto command reset: "OFF" control command, resets the fault
- Labeling: No parameters. Optional marking for designating the event, e.g. "Speed >," e.g. with SIMOCODE ES. Range: Maximum 10 characters.

  > **Note**
  >
  > **Changing the marking**
  >
  > Each change to the marking requires that the communication interface be restarted when the web
  >
  > server is active.
  >
  > A new start interrupts all Ethernet and PROFINET connections and re-establishes
  >
  > them afterward.

##### "External fault" response

- Fault/trip
- Warn
- **Signal**

#### Operational protection OFF (OPO)

The "Operational Protection OFF" (OPO) function block returns the positioner to a safe position. To do this, the input (plug) must be connected to any socket (e.g. device inputs, PROFIBUS DP control bits, etc.).

The "Operational Protection OFF" function block consists of

- one plug
- one "Status - OPO" socket. It is set if a signal is pending at the input
- one "Fault - OPO Fault" socket. It is set when the respective safe end position has been reached.

In total, one "Operational Protection Off (OPO)" function block is available for the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "Operational Protection OFF (OPO)" function block:

![Schematic](images/152748156043_DV_resource.Stream@PNG-en-US.png)

##### Operational protection OFF (OPO) settings

- Input  
  Activation of the "Operational Protection OFF" function block by the monitored signal (any sockets, e.g. device inputs, etc.)
- Positioner response: Specification of the response for the "Positioner" control function when activated via the input:

  - **CLOSED**: Positioner runs in "CLOSED" direction
  - OPEN: Positioner runs in "OPEN" direction
- Type: Specification of the input logic

  - **NO contact (1-active)**
  - NC contact (0-active)

##### Safety notices

> **Note**
>
> A "Fault - Operational protection OFF (OPO)" fault message is not generated if the "OPO" command attempts to run the positioner to the end position if it is approaching or has already reached this end position.

> **Note**
>
> No other control command (counter command or stop command) is performed while "Operational protection Off (OPO)" is active.

> **Note**
>
> The "Fault - Operational protection OFF (OPO)" fault message must be acknowledged by the open or closed control commands, depending on the present "OPO" end position.

> **Note**
>
> Acknowledgment is performed even if the desired end position has not yet been reached.

> **Note**
>
> The fault message is available as diagnosis via the communication bus.

##### Response to other control functions

For other control functions, the following scenarios can be differentiated between for OPO:

- Motor is on: The motor is switched Off with a "Fault - Operational Protection Off (OPO)" fault.
- The motor is off. Initially no fault. "Fault - Operational protection OFF (OPO)" only occurs when an "ON command" is issued.

#### Power failure monitoring (UVO)

The "Power Failure Monitoring (UVO)" function block is activated via the plug. This is carried out via an external voltage relay that is connected to the function block via the binary inputs of SIMOCODE pro.

In total, one "Power failure monitoring (UVO)" function block is available for the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units.

##### Power failure monitoring (UVO) sequence charts

![Power failure monitoring (UVO) sequence charts](images/153024721419_DV_resource.Stream@PNG-en-US.png)

##### Schematic

The following schematic shows the "Power failure monitoring (UVO)" function block:

![Schematic](images/152949783051_DV_resource.Stream@PNG-en-US.png)

##### Power failure monitoring (UVO) settings

- Input: Activation of the "Power Failure Monitoring (UVO)" function block by the monitored signal (any socket, e.g. device inputs, PROFIBUS DP control bits, etc.)
- Type: Specification of the type of power failure monitoring:

  - **Deactivated**
  - No interruption of device power supply. The SIMOCODE pro control voltage is maintained. The failure of the line voltage must be detected, for example, by a separate voltage relay.
- Power failure time: Time that starts when the power fails.

  - If the line voltage is restored within the power failure time, all drives that were running prior to the power failure are reconnected automatically taking the signals of the control stations into account.
  - If the line voltage is not restored within the power failure time, the drives remain disconnected and the "Fault - Power failure (UVO)" message is generated. Once the line voltage has been restored, this fault message can be acknowledged with "Reset".

  Range:

  - **0** to25.5 s in steps of 0.1 s
  - 26 to 255 s, in steps of 1 s
  - 256 to 2550 s in steps of 10 s.
- Restart time delay (staggered) The restart time delay can be set so that not all motors restart simultaneously (line voltage would otherwise dip again). Range: **0** to 255 seconds.
- Activation of external power failure monitoring: Activation of the "Power Failure Monitoring (UVO)" function block by the monitored signal (any socket, e.g. device inputs, communication bus control bits, etc.)

#### Emergency start

Emergency start deletes the thermal memory from SIMOCODE pro each time it is activated. This allows the motor to be immediately restarted after an overload trip. This function can be used to

- Enable an immediate reset and restart after an overload trip
- Delete the thermal memory (motor model) during operation, if required.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Caution** |
  | **Thermal overload**  If emergency starts are performed too frequently this may result in thermal overloading of the motor! |  |

An emergency start is carried out as follows:

- Using the plug of the function block. To do this, the input (plug) must be connected to any socket (e.g. device inputs, communication bus control bits, etc.).

The "Emergency start" function block consists of:

- One plug
- One "Status - emergency start executed" socket. The output is set when an emergency start has been executed.

Overall, there is one "Emergency start" function block available.

##### Schematic

The following schematic shows the "Emergency start" function block:

![Schematic](images/152956537739_DV_resource.Stream@PNG-en-US.png)

##### Emergency start settings

- Input; activation of the "Emergency Start" function block by any signal (any socket, e.g. device inputs, communication bus control bits, etc.).

#### Safety-related tripping

> **Note**
>
> Please note that the information made available for further processing is in the form of non-safety-related signals.

> **Note**
>
> Please note that the "Safe Tripping" function block does not itself represent a safety-related function.
>
> The safety function of the DM-F Local is determined exclusively by the setting of the DIP switch on the module.
>
> The safety function of the DM-F PROFIsafe is determined by the fail-safe program in the F-CPU.

In total, one "Safety-related tripping" function block for SAFETY (Local) or PROFIsafe is available for the SIMOCODE pro V basic unit.

Further information: See Manual [SIMOCODE pro fail-safe digital modules](http://support.automation.siemens.com/WW/view/en/50564852).

##### DM-F Local schematic

The DM-F Local "Safety-related tripping" function block consists of three sockets:

- Event - DM-F LOCAL OK: The DM-F Local is ON.
- Event - "Safety-related tripping": Safety-related tripping has been carried out.
- Status - enabling circuit closed: The enabling circuit is closed.

The following schematic shows the "Safety-related tripping" function block and the setting of the DIP switches, DM‑F Local:

##### Schematic

The following schematic shows the "Safety-related tripping" function block:

![Schematic](images/152956842507_DV_resource.Stream@PNG-en-US.png)

##### Settings of the DIP switches (DM-F Local)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **DIP switches target setting**  The target setting of the DIP switches in the SIMOCODE ES user interface (can be made using the mouse pointer) is transferred to the basic unit on download but does not affect the function of the DM‑F Local. The desired function is thus saved as soon as the parameterization has been created.  You must set the effective parameterization via the DIP switches on the front of the DM‑F Local (see tables below and/or the manual [SIMOCODE pro fail-safe digital modules](http://support.automation.siemens.com/WW/view/en/50564852).  The basic unit compares the target setting (from the download) with the actual setting on the DM‑F Local. If these differ "Configuration deviation" is output! |  |

| DM-F Local | Description |
| --- | --- |
| With/without cross-circuit detection | Cross-circuit detection is only possible with floating sensors. The sensors must be connected between T1 - Y12, Y33 and T2 – Y22, Y34. The device expects the test signal of terminal T1 at the terminals Y12 and Y33, and the test signal of T2 at the terminals Y22 and Y34. The device detects a sensor fault if the signal at the terminals Y12, Y33 or Y22, Y34 does not agree with the test signals T1, T2.  Cross-circuit detection must be deactivated if electronic sensors such as light arrays or laser scanners are connected. In this case, the DM-F Local no longer monitors the sensor inputs for cross-circuits. Usually, the outputs of safety sensors (OSSD) are already monitored for cross-circuits in the sensor itself.  If "Without cross-circuit detection" is set on the device, the test outputs T1, T2 are deactivated and may no longer be connected. At the Y12, Y22, Y33, and Y34 inputs, the DM-F Local expects a +24 V DC signal from the same current source as the one from which the device receives its power supply (possible only in the case of DM-F Local-*1AB00) or from T3 (static +24 V DC).  In the case of the DM-F Local-*1AU00 device version, it is imperative to connect the T3 terminal to the floating sensor contacts due to the electrical isolation between the input circuit and the sensor power supply. |
| 1 NC + 1 NO evaluation / 2 NC evaluation | In addition to 2-channel connection of the same types of sensor contacts (NC/NC), sensors with opposite types of contacts (NC/NO), such as are frequently used for magnetically-operated switches, can also be evaluated. Make sure that the normally closed contact is connected to Y12, and the normally open contact to Y22. |
| 2x 1-channel / 1x 2-channel | - Two sensors with one contact each (2x 1-channel) (NC/NC). It is expected that both sensors are AND-connected. Simultaneity is not monitored. - One sensor with two contacts each (1x 2-channel) (NC/NC). It is expected that both contacts are opened simultaneously. |
| Debouncing time for sensor inputs 50 ms / 10 ms | Any change in the sensor signal during the debouncing time is not evaluated.  - Debouncing time 50 ms: Changes in the switch position of strongly bouncing contacts are suppressed (e.g. position switches on heavy protective doors). - Debouncing time 10 ms: The shorter debouncing time permits faster tripping in the case of bounce-free sensors (e.g. light arrays). |
| Sensor input automatic start / monitored start | - Automatic start: The enabling circuits are switched to the active position as soon as the switch-on condition is satisfied at the Y12, Y22, Y34 and 1 sensor inputs. The start button connection terminal Y33 is not queried. - Monitored start: The enabling circuits are switched to the active position as soon as the switch-on condition is satisfied at the Y12, Y22, Y34, and 1 sensor inputs, and the start button at the Y33 terminal is actuated (start at falling edge). |
| Cascade input automatic start / monitored start | - Automatic start: The enabling circuits are switched to the active position as soon as the switch-on condition at cascading input 1 is satisfied, i.e. as soon as a static +24 V DC signal is present (e.g. from T3). - Monitored start: The enabling circuits are switched to the active position as soon as the switch-on condition at cascade input 1 is satisfied, i.e. as soon as a static +24 V DC signal is present (e.g., from T3), and the START button at the terminal Y33 is actuated (start at falling edge). |
| With / without startup testing | After a power failure, startup testing requires that the system operator actuates the sensors at Y12 and Y22 once. |
| With automatic starting / without automatic starting after power failure | The parameters of the DM-F Local can be defined so that the enabling circuits are automatically switched to the active position after a power failure, i.e. without actuation of the Y33 start button.  Requirements:  - Y12, Y22 or the cascading input 1 are set to "monitored start". - The switch-on condition at the sensor inputs and at the cascading input is satisfied. - The START button was actuated before the power failure and this was valid, i.e. the enabling circuits were in the active position. |

##### DM-F PROFIsafe schematic

The "Safety-related tripping" DM-F PROFIsafe function block consists of three sockets:

- Event - PROFIsafe active: Fail-safe communication between the F-CPU and the DM-F PROFIsafe is active.
- Event - "Safety-related tripping": Safety-related tripping has been carried out.
- Status - enabling circuit closed: The enabling circuit is closed.

The following schematic shows the DM‑F PROFIsafe "Safety-related tripping" function block:

![DM-F PROFIsafe schematic](images/152956842507_DV_resource.Stream@PNG-en-US.png)

The PROFIsafe address is set using the DIP switches on the DM-F PROFIsafe:

##### Settings of the DIP switches (DM-F PROFIsafe)

Use the DIP switches to set the PROFIsafe address on the DM‑F PROFIsafe:

Settings of the DIP switches (DM-F Local)

| Switch setting |  | OFF / ON |
| --- | --- | --- |
| 1 | ![Settings of the DIP switches (DM-F PROFIsafe)](images/148922810507_DV_resource.Stream@PNG-de-DE.png) | With / without cross-circuit detection |
| 2 | 1 NC + 1 NO evaluation / 2 NC evaluation |  |
| 3 | 2x 1-channel / 1x 2-channel |  |
| 4 | Debouncing time for sensor inputs 50 ms / 10 ms |  |
| 5 | Sensor input automatic start / monitored start |  |
| 6 | Cascading input automatic start / monitored start |  |
| 7 | With / without startup testing |  |
| 8 | With automatic starting / without automatic starting after power failure |  |

If a DIP switch is at ON, the respective value is active. If more than one DIP switch is at ON, the respective values must be added.

##### "Safety-related tripping" response

Here, you set the SIMOCODE pro response to safety-related tripping via DM-F Local or DM-F PROFIsafe.

> **Note**
>
> The response of the modules is not influenced by this setting. If the conditions for safety-related disconnection are met, the enable circuits are always disabled!

- **Trip**
- Deactivated
- Signal
- Warn

> **Note**
>
> In the event that the option "DM-F Local/PROFIsafe - separate function from control function" has been activated under "Motor control → Control function → Operating mode", only "Deactivated", "Signal" or "Warn" can be set and not "Trip".

##### "Safety-related tripping" reset

Here, you can select manual or automatic acknowledgment of SIMOCODE pro faults caused by safety-related tripping (default: **Manual**).

#### Watchdog (Bus monitoring, PLC/PCS monitoring)

The "Watchdog" function block monitors communication with the PLC via communication bus, as well as the operating state of the PLC in the "Remote" operating mode.

##### Bus monitoring

With this type of monitoring, the "Störung ‑ Bus" fault is generated if

- "Bus monitoring" is active
- Cyclic data transfer between the PLC and SIMOCODE pro is interrupted in the "Remote" operating mode (mode selector S1=1 and S2=1), e.g., as a result of interruption of the bus connection.

"Status - bus o.k." can always be evaluated. If SIMOCODE pro is cyclically exchanging data with the PLC, "Status ‑ Bus o.k." is set to "1".

##### PLC/PCS monitoring

With this type of monitoring, the "Fault - PLC/PCS" message is generated if

- "PLC/PCS monitoring" is activated
- The PROFIBUS DP switches to the "CLEAR" state when in "Remote" mode (mode selector S1=1 and S2=1), or PROFINET switches to the "Hold/Stop" state

The "Status ‑ PLC/PCS in Run" can always be evaluated. If the PROFIBUS DP is in the "CLEAR" state, or PROFINET is in the "Hold/Stop" state, "Status - PLC/PCS in Run" is set to "0".

If the "PLC/PCS monitoring - input" is connected primarily to the "Cyclic receive - bit 0.7" bit, the status of the PLC is deduced from this bit only.

##### Schematic

The following schematic shows the "Watchdog" (PLC/PCS monitoring) function block:

![Schematic](images/152957478795_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **PROFIBUS DP**  "Bus monitoring" and "PLC/PCS monitoring" can only be effective if the DP slave watchdog function is activated in the DP master system. |  |

##### Watchdog settings

- PLC/PCS monitoring - Input: Activation of the "Watchdog" function block by the monitored signal (any sockets, e.g. PROFIBUS DP or PROFINET control bits, etc.).
- Bus monitoring

  - **Activated**: If a bus fault occurs, the "Fault - Bus" fault message is generated and must be acknowledged
  - Deactivated: No fault message; however, the "Status - Bus o.k." information can be evaluated at any time.
- PLC/PCS monitoring

  - **Activated**: If a PLC fault occurs, the "PLC/PCS fault" fault message is generated and must be acknowledged
  - Deactivated: No fault message; however, the "Status - SPS/PLS in Run" information can be evaluated at any time.
- Bus/PLC fault - reset You can select whether faults are to be acknowledged automatically or manually. Range: **Manual**/Auto

##### "Fault - bus" / "Fault - PLC / PCS" response

- **Fault**
- Deactivated

#### Time stamping

SIMOCODE pro V can timestamp up to eight digital signals with high temporal precision (10 ms). In the process, every change in the state of the digital signal will be recorded.

Possible areas of application are:

- Precise chronological recording of faults in a process plant
- Analysis of system-wide interrelationships
- Recording and signaling of time-critical signal changes

##### Precondition

To use SIMOCODE pro V time stamping, the DP master being used must support time synchronization functions via Profibus (e.g. DP master connections for SIMATIC S7-400), or a master clock must be used (e.g. SICLOCK).

##### Process in Step 7

Time-of-day synchronization for SIMOCODE pro V is activated in the STEP 7 device configuration in the slave properties under "Time Synchronization".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Synchronization interval**  The set synchronization interval must correspond to the configuration of the clock master. |  |

For SIMOCODE pro, transmission of time stamped information is analogous to transmission with SIMATIC S7 IM 153-2. Therefore, the "FB 62 TIMESTMP" function block can be used for further processing of time stamped information in the CPU, to transmit time stamped messages from the "Standard Library → Miscellaneous Blocks" library.

> **Note**
>
> The "LADDR" parameter contains the diagnostic address of the DP slave from STEP 7 HW Config.
>
> In the DP mode "DPV1" of the DP master - integrated via OM SIMOCODE pro - LADDR2 contains the diagnostics address of Slot 2 of SIMOCODE pro. For all other configurations, LADDR2 will contain the same address as LADDR.
>
> The "LADDR2" parameter contains the diagnostic address of the DP slave from STEP 7 HW Config. In DP mode "DPV1" of the DP master – integrated via SIMOCODE pro – LADDR2 contains the diagnostic address of slot 2 of SIMOCODE pro. For all other configurations, LADDR2 will contain the same address as LADDR.

In contrast to the STEP 7 Online Help of FB 62, when integrating via GSD, the slot number of the module is transmitted with Slot 1 for signal messages, and with Slot 0 for special messages.

For further information on FB 62, refer to the STEP 7 Online Help system.

##### Schematic

The following schematic shows the "Time stamping" function block:

![Schematic](images/154759435659_DV_resource.Stream@PNG-en-US.png)

### Logic modules

This section contains information on the following topics:

- [Truth table 2I/1O](#truth-table-2i1o)
- [Truth table 3I/1O](#truth-table-3i1o)
- [Truth table 5I/2O](#truth-table-5i2o)
- [Counter](#counter)
- [Timer](#timer)
- [Signal conditioning](#signal-conditioning)
- [Non-volatile element](#non-volatile-element)
- [Flashing](#flashing)
- [Flicker](#flicker)
- [Limit monitor](#limit-monitor)
- [Calculators](#calculators)
- [Operator panel with display](#operator-panel-with-display)
- [Analog multiplexer](#analog-multiplexer)
- [Pulse width modulator](#pulse-width-modulator)
- [PROFIenergy](#profienergy)

#### Truth table 2I/1O

The truth table 2I/1O consists of:

- Two plugs
- One logic component
- One socket.

You can choose which of the four possible input conditions an output signal should be generated for.

In total, two truth tables (7 to 8) are available.

##### Schematic

The following schematic shows the "Truth table 2I/1O" logic modules:

![Schematic](images/152958380555_DV_resource.Stream@PNG-en-US.png)

#### Truth table 3I/1O

The truth table 3I/1O consists of:

- Three plugs
- One logic component
- One socket.

You can choose which of the eight possible input conditions an output signal should be generated for.

The following are available:

- Three truth tables (1 to 3) for the SIMOCODE pro C basic unit
- Four truth tables (1 to 4) for the SIMOCODE pro S basic unit
- Six truth tables (1 to 6) for the SIMOCODE pro V PB and pro V MB RTU basic units
- Eight truth tables (1 to 6, 10, 11) for the SIMOCODE pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "Truth Table for 3I/1O" logic modules:

![Schematic](images/152958530443_DV_resource.Stream@PNG-en-US.png)

##### Settings for truth table 1 to 11, 3I/1O

- Input 1 to 3  
  Activation of the truth table by any signal (any sockets, e.g. device inputs, PROFIBUS DP or PROFINET control bits, etc.).

#### Truth table 5I/2O

The truth table 5I/2O consists of:

- Five plugs
- One logic component
- Two sockets.

You can choose which of the 32 possible input conditions a maximum of two output signals should be generated for.

One truth table 9 each is available for the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "Truth table 5I/2O" logic module:

![Schematic](images/152958885131_DV_resource.Stream@PNG-en-US.png)

##### Truth table 9, 5I/2O settings

Input 1 to 5: Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)

#### Counter

Counters are integrated in the SIMOCODE pro system. These are controlled via the plugs "+" or "-".

The counter output switches to "1" when the preset limit is reached. The counter is reset with "Reset".

The current actual value is available as a socket for further internal processing and can also be transmitted to the automation system.

- Plug +: Increase actual value by 1 (maximum: limit).
- Plug -: Reduce the actual value by 1 (minimum: 0)
- Reset: Resets the actual value to 0.

The counter consists of:

- Three plugs (input +, input -, reset)
- One logic component
- One socket
- One "Actual value" analog socket with the current value in the range between 0 and the limit. The value is retained even in the event of a power failure.

The following are available:

- two counters (1 to 2) for the SIMOCODE pro C and pro S basic units
- four counters (1 to 4) for the SIMOCODE pro V PB and pro V MR basic units
- six counters (1 to 6) for the SIMOCODE pro V PN (GP) and pro V EIP basic units.

##### Schematic

The following schematic shows the "Counter" logic modules:

![Schematic](images/152958990347_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The time between the events to be counted depends on
>
> - The input delay
> - The device cycle time.

> **Note**
>
> The actual value remains the same
>
> - During parameterization or failure of the supply voltage
> - If there are simultaneous input signals at input + and input -.

> **Note**
>
> The output is always 0 if a reset is pending.

> **Note**
>
> Since the counter sets the output as soon as the actual value has reached the preset value, the output is permanently set at a value = 0 as long as no reset is applied.

##### Settings of counters 1 to 6

- Input +: Increments actual value by 1. Activation by any signal (any sockets, e.g., device inputs, PROFIBUS DP control bits, etc.)
- Input –: Decrements the actual value by 1. Activation by any signal (any sockets, e.g., device inputs, PROFIBUS DP control bits, etc.)
- Reset: Reset the actual value to 0 (count value and output). Activation by any signal (any sockets, e.g., device inputs, PROFIBUS DP control bits, etc.)
- Threshold: Value that can be reached when counting and at which the counter issues an output signal. Range: **0** to 65535.

#### Timer

The timer consists of:

- Two plugs (input and reset)
- One socket
- One "Actual value" analog socket with the actual value.

The current actual value is available as a socket for further internal processing and can also be transmitted to the automation system.

If an input signal is pending, the timer issues an output signal according to the chosen timer type:

- With closing delay
- With closing delay with memory
- With opening delay
- With fleeting closing.

The following are available:

- two timers 1 to 2 for the SIMOCODE pro C and pro S basic units
- four timers (1 to 4) for the SIMOCODE pro V PB and pro V MR basic units
- six timers (1 to 6) for the SIMOCODE pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "Timer" logic modules:

![Schematic](images/152959247755_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The output is always 0 if a reset is pending.

> **Note**
>
> The response of the inputs of all timers (input, reset) has been completely changed to level-active for the SIMOCODE pro C basic unit from product version *E05* or the SIMOCODE pro V PB basic unit from version *E03*. Use of an unchanged parameter file utilizing integrated timers may thus result in a different response if such basic units are used. For example, if "Fixed level - '1'" is set at the timer input, the timer function is automatically restarted after the timer reset occurs. However, in timers with the parameterized type = "Fleeting closing" there is no change in the response.

##### Output response of the timer

For

- SIMOCODE pro C basic unit **up to** version *E05*
- SIMOCODE pro V PB basic unit **up to** version *E03*

![Output response of the timer](images/153024802443_DV_resource.Stream@PNG-en-US.png)

For

- SIMOCODE pro C basic unit **from** version *E05*
- SIMOCODE pro V PB basic unit **from** version *E03*
- SIMOCODE pro S basic unit
- all other SIMOCODE pro V basic units

![Output response of the timer](images/153025625867_DV_resource.Stream@PNG-en-US.png)

##### Settings of timers 1 to 6

- Input: Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)
- Reset: Resetting the actual value to 0. Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)
- Type: Different output responses. Range: **With closing delay**, closing delay with memory, with opening delay, with fleeting closing
- Value: Time during which the timer provides an output signal when activated, depending on the output response (type). Range: **0** to 6553.5, unit 100 ms

#### Signal conditioning

If an input signal is pending, the signal conditioning issues an output signal according to the selected signal conditioning type:

- Non-inverting
- Inverting
- Edge rising with memory
- Edge falling with memory

You can set the output response.

The signal conditioning consists of:

- Two plugs (input and reset)
- One logic component
- One socket

The following are available:

- two signal conditionings (1 to 2) for the SIMOCODE pro C basic unit
- four signal conditionings (1 to 4) for the SIMOCODE pro S, pro V PB, and pro V MR basic units
- six signal conditionings (1 to 6) for the SIMOCODE pro V PN and pro V EIP basic units.

##### Schematic

The following schematic shows the "Signal conditioning" logic modules:

![Schematic](images/152959487243_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The output is always 0 if a reset is pending.

##### Types of signals / output responses

![Types of signals / output responses](images/153047648523_DV_resource.Stream@PNG-en-US.png)

##### NOR function

You can implement a NOR function with the "inverting" type of signal:

| Input | Reset | Output | Schematic |
| --- | --- | --- | --- |
| 0 | 0 | 1 | ![NOR function](images/153602930315_DV_resource.Stream@PNG-de-DE.png) |
| 1 | 0 | 0 |  |
| 0 | 1 | 0 |  |
| 1 | 1 | 0 |  |

##### Settings of signal conditioners 1 to 6

- Input: Activation by any signal (any sockets, e.g. device inputs, PROFIBUS DP control bits, etc.).
- Reset: Resetting of the signal conditioning to 0. Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)

  Type: Different output responses:

  - **Level non-inverting**
  - Level inverting
  - Edge rising with memory
  - Edge falling with memory

#### Non-volatile element

Non-volatile elements behave like signal conditioners. However, these output signals are retained after a power supply failure.

If an input signal is pending, the signal conditioning issues an output signal according to the selected signal conditioning type:

- Non-inverting
- Inverting
- Edge rising with memory
- Edge falling with memory

You can set the output response.

The non-volatile element consists of

- Two plugs (input and reset)
- One logic component
- One socket

The following are available:

- Two non-volatile elements (1 to 2) for the SIMOCODE pro C and pro S basic units
- four non-volatile elements 1 to 4 for the SIMOCODE pro V PB, pro V MR, pro V PN, and pro V EIP basic units

##### Schematic

The following schematic shows the "Non-volatile elements" logic modules:

![Schematic](images/152962043531_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The output is always 0 if a reset is applied.

##### Types of signals / output responses

![Types of signals / output responses of non-volatile elements](images/153047166475_DV_resource.Stream@PNG-en-US.png)

Types of signals / output responses of non-volatile elements

##### NOR function

You can implement a NOR function with the "inverting" type of signal:

| Input | Reset | Output | Schematic |
| --- | --- | --- | --- |
| 0 | 0 | 1 | ![NOR function](images/153047388299_DV_resource.Stream@PNG-en-US.png) |
| 1 | 0 | 0 |  |
| 0 | 1 | 0 |  |
| 1 | 1 | 0 |  |

##### Settings of non-volatile elements 1 to 4

- Input: Activation by any signal (any sockets, e.g., device inputs, PROFIBUS DP control bits, etc.)
- Reset: Resetting of the signal conditioning to 0. Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)
- Type: Different output responses; Range:

  - **Level not inverted**
  - Level inverted
  - Edge rising with memory
  - Edge falling with memory

#### Flashing

If an input signal is pending, the "Flashing" logic component issues an output signal with a fixed frequency of 1 Hz between binary 0 and 1. This makes the LEDs on the operator panel flash.

The logic module consists of:

- One plug
- One logic component
- One socket.

A total of three logic modules, "Flashing" (1 to 3), are available.

##### Schematic

The following schematic shows the "Flashing" logic modules:

![Schematic](images/152966225419_DV_resource.Stream@PNG-en-US.png)

##### Flashing 1 to 3 settings

Input: Activation by any signal (any sockets, e.g. device inputs, events, status, etc.)

#### Flicker

You can use the "Flicker" logic modules to assign the "Flicker" function to the operator panel LEDs.

If an input signal is pending, the "Flicker" logic module issues an output signal with a frequency of 4 Hz.

The logic module consists of:

- One plug
- One logic component
- One socket.

A total of three logic modules, "Flicker" (1 to 3), are available.

##### Schematic

The following schematic shows the "Flicker" logic modules:

![Schematic](images/152971136907_DV_resource.Stream@PNG-en-US.png)

##### Settings of flicker 1 to 3

Input: Activation by any signal (any sockets, e.g. events, etc.)

#### Limit monitor

With the limit monitor, any analog values (2 bytes/1 word) can be monitored for limit overshooting or limit undershooting.

The limit monitor issues the "Limit" signal at its socket. In addition, limit monitors can be "marked" according to their function.

Example: Monitoring the individual sensor measuring circuits of the temperature module (temperature 1-3) for overtemperature.

The limit monitor consists of:

- One analog plug
- One logic component
- One socket

The following are available:

- four limit monitors (1 to 4) for the SIMOCODE pro V PB and pro V MR basic units
- six limit monitors (1 to 6) for the SIMOCODE pro V PN (GP) and pro V EIP basic units

##### Schematic

The following schematic shows the "Limit monitor" logic modules:

![Schematic](images/152971414795_DV_resource.Stream@PNG-en-US.png)

##### Response for limit 1 to 6

- Signal
- Delay - Range: 0 to 25, 5 s (**0.5** s)

##### Functional principle

The limit signal issued depends on

- The operating state of the motor
- The TPF function
- The parameterized "activity":

  - **on**,
  - on+
  - run
  - run+.

The following display shows a flow chart with the different "active status" parameters.

![Functional principle](images/153026643851_DV_resource.Stream@PNG-en-US.png)

##### Limit monitor settings

- Input: Analog plug of the limit monitor for linking to the analog value to be monitored (2 bytes), e.g. maximum current I<sub>max</sub>, remaining cooling down period, actual value of timers, etc.
- Type: Specifies if the limit has to be monitored for overshooting or undershooting
- Active status: Determines in which motor operating state the limit monitor is to be evaluated:

  - **ON**, i.e. always evaluate, regardless of whether or not the motor is running,
  - on+, i.e. always evaluate, regardless of whether or not the motor is running. Exception: "TPF", i.e. motor feeder is in test position;
  - run, i.e. evaluate only if the motor is in the ON state and not in the test position (TPF).
  - run+, i.e. evaluate only if the motor is running and the start-up procedure is finished (i.e. the "Start active" message is no longer active) and there is no test position feedback (TPF); example: Cos phi monitoring
- Threshold: Monitor response value. The return value is always determined by the "Limit monitor - Delay" parameter. Range: **0** to 65535
- Delay - Specifies the time period for which the limit must be constantly overshot before the "Event - Limit" output is set. Range: 0 to 25.5 s (**0.5** s)
- Labeling: No parameters. Optional marking for identifying the message, e.g. "Limit>"; range: Max. 10 characters.

  > **Note**
  >
  > When using limit monitors, always ensure that the correct range and unit are used for the analog value connected to the limit input. These always have a direct influence on the unit of the limit to be set.

##### Examples of typical units and ranges in SIMOCODE pro:

|  | Unit | Range |
| --- | --- | --- |
| Temperatures (e.g. max. temperature) | 1 K | 0 to 65535 |
| Operating hours | 1 s | 0 to 1193046 |
| Stop time | 1 h | 0 to 65535 |
| Active power | 1 W | 0 to 4294967295 |
| Apparent power | 1 VA | 0 to 4394967295 |
| Timer actual value | 100 ms | 0 to 65535 |
| Currents (e.g. max. current_I<sub>max</sub>) | 1% l<sub>s</sub> | 0 to 66535 |
| Analog module inputs | -- | 0 to 27648 (S7 format) |

Thus, for example, a limit of 473 (K) must be parameterized for a limit monitor to monitor a maximum temperature of 200 °C.

#### Calculators

This section contains information on the following topics:

- [Calculator 1](#calculator-1)
- [Calculator 2](#calculator-2)
- [Calculators 3, 4](#calculators-3-4)

##### Calculator 1

The two logic modules "Calculator 1" and "Calculator 2" integrated in the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units are capable of the standard calculation modes and enable all analog values featured in SIMOCODE pro to be adapted, calculated, and converted, for example:

- Conversion of the measured temperature from K (Kelvin) to °F or °C
- Conversion of the motor current from [%] to [A]
- Conversion of the 0 / 4 - 20‑mA signals of the analog module directly into fill levels, pressures and flow rates.

The analog value (2 bytes/1 word) present at the analog sockets is calculated using a defined formula and using freely-selectable parameters (numerators, denominators, operators, offsets). The result of the calculation is output as an analog value (2 bytes/1 word) at the analog socket of the logic module for further processing.

Each calculator consists of:

- One analog plug (Calculator 1) or two analog plugs (Calculator 2)
- One logic component
- One analog socket

###### Schematic

The following schematic shows the "Calculator 1" logic module:

![Schematic](images/152971801227_DV_resource.Stream@PNG-en-US.png)

###### Settings

| Calculator 1 | Description |
| --- | --- |
| Input | Any value (2 bytes/1 word)  Range: 0 to 65535 |
| Output | Calculated value (2 bytes/1 word)  Range: 0 to 65535 |
| Numerator | Range: -32768 to +32767, increment 1 |
| Denominator | Range: 0 to 255, increment 1 |
| Offset | Range: -32768 to +32767, increment 1 |

> **Note**
>
> **Special aspect**
>
> If the numerator and/or the denominator have the value "0", these values are treated as "1" inside the device.

###### Formula

![Formula](images/162808963851_DV_resource.Stream@PNG-en-US.png)

Output: Calculated value (2 bytes/1 word): Range: 0 - 65535

###### Example 1:

![Example 1:](images/152972165515_DV_resource.Stream@PNG-en-US.png)

###### Example 2:

Conversion of the maximum temperature of the temperature module from K to °F

![Example 2:](images/152972360331_DV_resource.Stream@PNG-en-US.png)

###### Example 3:

![Example 3:](images/152972670347_DV_resource.Stream@PNG-en-US.png)

##### Calculator 2

The two logic modules "Calculator 1" and "Calculator 2" integrated in the SIMOCODE pro V PB, pro V MB RTU, pro V PN and pro V EIP basic units are capable of the standard calculation modes and enable all analog values featured in SIMOCODE pro to be adapted, calculated, or converted, for example:

- Conversion of the measured temperature from K (Kelvin) to °F or °C
- Conversion of the motor current from [%] to [A]
- Conversion of the 0 / 4 - 20‑mA signals of the analog module directly into fill levels, pressures and flow rates.

The analog value (2 bytes/1 word) present at the analog sockets is calculated using a defined formula and using freely-selectable parameters (numerators, denominators, operators, offsets). The result of the calculation is output as an analog value (2 bytes/1 word) at the analog socket of the logic module for further processing.

Each calculator consists of:

- One analog plug (Calculator 1) or two analog plugs (Calculator 2)
- One logic component
- One analog socket

###### Schematic

The following schematic shows the "Calculator 2" logic module:

![Schematic](images/152973263371_DV_resource.Stream@PNG-en-US.png)

###### Operating mode 1 and operating mode 2

The mode of the "Calculator 2" logic module can be changed via the "Operating mode" parameter:

- Operating mode 1: The analog value at input 1 is combined with the analog value at input 2 using a predefined formula and taking into account the specified parameters (numerators, denominators, offsets, operators). The result is available as an analog value (1 word / 2 bytes) at the output of the function block for further processing.
- Operating mode 2: The analog values at input 1 and input 2 are processed together as a double word. Input 1 represents the high word and input 2 the low word. The result is calculated by means of the formula defined for this operating mode using the specified parameters (numerators, denominators, offsets) and is output by the function block as 1 word/2 bytes. In mode 2, it is also possible to process double words (e.g., active power, apparent power) and to display them (2 bytes / 1 word).

###### Settings

| Calculator 2 | Description |
| --- | --- |
| Input 1 | Any value (2 bytes/1 word)  Range: 0 to 65535 |
| Input 2 | Any value (2 bytes/1 word)  Range: 0 to 65535 |
| Output | Calculated value (2 bytes/1 word)  Range: 0 to 65535 |
| Numerator 1 | Range: -128 to +127, increment 1 |
| Denominator 1 | Range: 0 to 255, increment 1 |
| Numerator 2 *) | Range: 0 to 255, increment 1 |
| Denominator 2 *) | Range: -128 to +127, increment 1 |
| Offset | Range: -2147483648 to +2147483647, increment 2 |
| Operating mode | 1 or 2 |
| Operator *) | +, - , *, / |
| *) Only relevant when operating mode =1 |  |

> **Note**
>
> **Special aspect**
>
> If the numerator and/or the denominator have the value "0", these values are treated as "1" inside the device.

###### Equations

- Operating mode 1: Both inputs of word type.

![Equations](images/152973026315_DV_resource.Stream@PNG-en-US.png)

- Operating mode 2:

Both inputs 1 and 2 correspond to a D word input.

![Equations](images/162791173899_DV_resource.Stream@PNG-en-US.png)

##### Calculators 3, 4

Using the "Calculator 3" and "Calculator 4" function blocks (for SIMOCODE pro V PN (GP) and pro V EIP basic units only), analog values can be processed according to the following arithmetic:

Output = Input 1 [Operator 1] Input 2 [Operator 2] Input 3 [Operator 3] Input 4.

You can interconnect corresponding analog signals to the 4 inputs.  
You can select one of the four standard operators ("+", "-", "*" or "/") as operators 1-3.

With "Calculator - Priority 1-3", you can specify the processing sequence (high, medium, low). You must clearly define a priority for each operator. The priority determines the processing sequence comparable to the placement of a term inside parentheses.

Example:

Output = I1 OP1 I2 OP2 I3 OP3 I4, where

- OP1 = "*"; Medium,
- OP2 = "+"; High,
- OP3 = "-"; Low

Associated equation: Output = (I1 * (I2 + I3)) - I4.

If you interconnect the input to the device-internal analog output data element "Output 1 - Fixed level", the input is assigned the constant "Const x" (x = 1 - 4). In this case, the respective edit field for the constant is activated. You can enter a value between 0 and 65535.

The "Calculator 3" and "Calculator 4" function blocks each consist of:

- four analog plugs
- one analog socket
- logic.

###### Schematic

The following schematic shows the "Calculator 3" and "Calculator 4" logic modules:

![Schematic](images/152973605771_DV_resource.Stream@PNG-en-US.png)

###### Settings

| Calculators 3/4 | Description |
| --- | --- |
| Input | Any analog value |
| Output | Calculated analog value |
| Constant 1 to 4 | Any analog value  Range: **0** ... 65535 |
| Operator 1 to 3 | - "+": Addition - "-": Subtraction - "*": Multiplication - "/": Division |
| Priority 1 to 3 | - OP1 = "*"; Medium, - OP2 = "+"; High, - OP3 = "-"; Low |

> **Note**
>
> **Special aspect**
>
> If the numerator and/or the denominator have the value "0", these values are treated as "1" inside the device.

###### Formula

Output = Input 1 [Operator 1] Input 2 [Operator 2] Input 3 [Operator 3] Input 4.

###### Principle of operation

With calculation block 3 and 4 you can link four outputs/values together via three freely selectable operands (+, -, *, /). This enables relatively complex calculations.

The sequence of calculation steps is specified by the use of brackets that can enclose one or more operations.

If the prioritization does not wok, a warning is output (e.g., open bracket not followed by closed bracket).

When the input is correct, a preview of the formula is displayed.

If the calculation contains fixed values, these are also input.

#### Operator panel with display

Here you can make the following user-specific settings for the operator panel with display (only when using the SIMOCODE pro V PN and pro V EIP basic units):

##### Settings

- Return to main display (after)

  - Manual
  - 3 seconds
  - **10 seconds**
  - 1 minute
  - 5 minutes
- Language

  - **English**
  - German
  - French
  - Polish
  - Spanish
  - Portuguese
  - Italian
  - Finnish
- Contrast

  - 10 - 90 % (**50** %)
- Profile

  - **IL1, IL2, IL3 [A]**
  - IL1, IL2, IL3 [%]
  - I max [A]
  - I max [%]
  - I max, Cos
  - I max, U L1N, Cos, S
  - I max, UL1L2, Cos, S
  - I max, U L1N, Cos, P
  - I max, U L1L2, Cos, P
  - [mA] In1 / Output AM1
  - [mA] In2 / Output AM1
  - [mA] Inputs AM1
  - [mA] In1 / Output AM2
  - [mA] In2 / Output AM2
  - [mA] Inputs AM2
  - Max. temp. °C TM1
  - Temp. °C TM1
  - Max. temp. °F TM1
  - Temp. °F TM1
  - Max. temp. °F TM1
  - Temp. °F TM1
  - Max. temp. °F TM2
  - Temp. °F TM2
  - Max. temp. °F TM2
  - Temp. °F TM2
  - U L1N, U L2N, U L3N
  - U L1L2, U L2L3, U L3L1
  - I max, U L1N, Cos
  - I max, U L1L2, Cos
  - I max, U L1N, °C
  - I max, U L1L2, °C
  - I max, U L1N, °F
  - I max, U L1L2, °F
  - Calculator_1
  - Calculator_2
  - Consumed energy [kWh]
- Lighting automatically OFF (after)

  - Off (= never)
  - 3 seconds
  - **10 seconds**
  - 1 minute
  - 5 minutes
- Warnings

  - **Do Not Display**
  - Display
- Faults

  - **Display**
  - Do Not Display

#### Analog multiplexer

The analog multiplexer (for SIMOCODE pro V PN (GP) /pro V EIP basic units only) outputs one of 4 possible analog values at the inputs 1 to 4, depending on control signals S1 and S2.

If you interconnect the input to "Fixed level," the input is assigned the constant "Const x" (x = 1 to 4). In this case, the respective edit field for the constant is activated.

You can enter a value between 0 and 65535.

The "Analog Multiplexer" function block consists of:

- two digital plugs (control signal 1 and 2)
- four analog plugs (Input 1 to 4)
- one analog socket
- logic.

Connection of the control signals with the inputs is shown graphically.

##### Schematic

The following schematic shows the Analog Multiplexer logic module:

![Schematic](images/152985047435_DV_resource.Stream@PNG-en-US.png)

##### Analog multiplexer settings

- Control signal S1 to S4: Activation by any signal (any sockets, e.g. device inputs, control bits from the communication bus, etc.)
- Input 1 to 4: Any analog value or "Fixed level"
- Output: Output value according to panel (see below)
- Constant 1 to 4: Any analog value; range: 0 to 65535

#### Pulse width modulator

The pulse width modulator (PWM) (for SIMOCODE pro V PN (GP) /pro V EIP basic units only) modulates the analog input value into a digital output signal "PWM Output" with a variable duty factor that is proportional to the analog input value.

If you interconnect the input to "Fixed level," the input is assigned the parameterized constant "Input (Const)". In this case, the edit field for the constant is activated. You can enter a value between 1 and 65535.

The "Pulse Width Modulator" function block consists of:

- one analog plug (input)
- one digital socket (PWM output)
- logic.

##### Schematic

The following schematic shows the Pulse Width Modulator (PWM) logic module:

![Schematic](images/152985723403_DV_resource.Stream@PNG-en-US.png)

##### Settings Pulse Width Modulator

- Input: Activation by any analog signal or "Fixed value"
- Constant input: Any constant; range: **0** to 65535
- Minimum input: Any constant; range: **0** to 65534
- Maximum input: Any constant; range: 1 to **65535**
- PWM duration: 0.2 to 6553.5 s (**2** s)

##### Equations

- Length of 1-signal = PWM period * (PWM Input - PWM Input Minimum) / (PWM Input Maximum - PWM Input Minimum)
- Length of 0-signal = PWM period - Length of 1-signal.

  > **Note**
  >
  > The shortest signal duration for 0 and 1 is 0.1 s in each case.
  >
  > If a duration for the 1 signal that is shorter than 0.1 s results from calculation, the output will remain permanently 0, while for a duration for the 0 signal shorter than 0.1 s the output remains permanently 1.

##### Example - Pulse width modulator

A load will be switched on and off with a duration of 60 minutes, dependent on a measured value (e.g., temperature).

- If the measured value exceeds a maximum value of 50 ℃ (323 K), the load will be switched on permanently, and if it falls below 20 °C (293 K), it will be switched off permanently.
- If the measured value falls within the range between the minimum and maximum value, the On duration will be proportional to the measured value.

![Example - Pulse width modulator](images/152986007819_DV_resource.Stream@PNG-en-US.png)

- Duration: 60 min (3600 s)
- Lower limit: 20 ℃ (293 K)
- Upper limit: 50 °C (323 K).

![Example - Pulse width modulator](images/152986919947_DV_resource.Stream@PNG-en-US.png)

- At 20 ℃ (293 K): OFF
- At 30 ℃ (303 K): 20 min ON and 40 min OFF
- At 40 ℃ (313 K): 40 min ON and 20 min OFF
- At 50 ℃ (323 K): ON.

#### PROFIenergy

PROFIenergy, a protocol defined by the PROFINET User Organization, lays the foundations for a vendor-neutral, universal system for flexible, short-term, and intelligent shutdown of individual loads or whole production units.

SIMOCODE pro V PN supports the functions defined in the protocol in the form of a switchgear with switching and measuring functions

##### Settings

Here you can set the minimum pause time for the motor (0.0 to 65.5 s (**0.1** s)).

### Libraries

#### General information

The libraries help you to create and re-use entire device configurations and charts, and to exchange them with other users.

Programming of the statements and objects is not necessary so the likelihood of errors is reduced.

#### Project libraries

For each project, there is a project library that is integrated into the project. The project library contains objects that can be re-used within the project.

Copying a device or a chart:

1. Select the "Project library" button on the right-hand side. The "Project library" window opens.
2. On the left-hand side of the project navigation, select a device or a chart.
3. Keep the mouse button pressed and drag the project or the chart to the "Master copies" folder of the project library, or copy the project or the chart to the "Master copies" folder using "Copy" and "Paste".

The project library is always opened, saved and closed together with the current project.

**Copying charts to the project library and from the project library**

You can copy charts only to the "Master copies" folder of the project library (see "Master copies" below).

> **Note**
>
> **Copying charts**
>
> If you use more than one chart in a project, you must assign different names.

**Conflicts when using charts stored in the "Master copies" folder:**

If you want to use a chart stored in the "Master copies" folder in the current project by means of drag&drop, an automatic check is made to establish whether there are any function blocks and blocks in this chart that are not supported in the current project. In this case, the "Copy conflict" window opens, offering you the following information in the form of a table:

- Block type: Types of function blocks and blocks that cannot be used in the current project
- Names of the function blocks and blocks that are not supported and that are used in the master copy
- Names of the function blocks and blocks that are not supported and that are used in the current project
- Names of the charts that are used in the current project with which there is a conflict.

To eliminate the conflict, use two option fields to select whether you want to use the function blocks and blocks of the master copy or of the current project. SIMOCODE ES then attempts to reconfigure the connections of the automatically removed function blocks and blocks. It is possible that some parameters are not supported in the target device, or that the maximum/minimum limit of the possible parameters has been overshot/undershot. In these cases, detailed message texts appear in the Inspector window. There are three types of messages:

- Message about which function block or block has been removed from which chart
- Message when a parameter is not supported by the target device
- Message when the maximum/minimum limit of the possible parameters has been overshot/undershot.

#### Global libraries

As well as the project library, any number of global libraries can be created independently of any specific project. The libraries are compatible with each other and can be used across project boundaries. The library elements can be copied and moved between libraries. Other users have access to global libraries stored centrally.

Copying a device:

1. Select the "Global libraries" button on the right-hand side. The "Global libraries" window opens.
2. Open an existing library. If no library is available, create a new one.
3. On the left-hand side of the project navigation, select a device and drag it while pressing the mouse key to the "Master copies" folder of the global libraries.
4. You can now save the library, and close it if no longer required.

#### Master copies

The objects can be saved as master copies and re-inserted into the project later. You can, for example, save entire devices with their contents or cover sheets as master copies for the system documentation.

> **Note**
>
> **Avoid complex master copy structures**
>
> Avoid complex master copies to prevent name conflicts and conflicts with regard to the folder structure when using master copies later. Complex master copies include, for example, master copies comprising several elements and nested folders.

See also "Using libraries → Using master copies → Adding master copies" in the information system.

### Display of all parameters

In the menu item "All parameters" in the Parameterization Editor, all parameters are shown clearly in one window.

### Display of the basic parameters

#### Key statement

In the menu item "Basic parameters" in the Parameterization Editor, the most important parameters are shown clearly in one window, e.g.

[Device configuration](#device-configuration)

[Control stations](#control-stations)

[Basic unit outputs](#basic-unit-outputs).

### Expert list

The expert list shows all device parameters (excluding Web server user name and password) in a compact way.

Every device has its own specific parameterization. However, a large number of the parameters are identical across different projects. In the expert list, you can create favorite parameter sets from all the parameters displayed on tab card "All parameters" (except Web server user name and password). You can also hide certain parameters from the expert list to generate an even more compact view based on your needs.

**Marking parameters as favorites**

Using the shortcut menu, you can mark parameters as follows:

- one or more parameters as favorites. Mark multiple parameters using the shift key.
- All parameters belonging to a particular higher-level node.

The parameters that are marked as favorites are indicated by a blue favorites symbol. If you have marked all parameters below a higher-level node, the higher-level node also gets a blue symbol. If only some of the parameters below a higher-level node have been marked, the higher-level node gets a half-filled blue symbol.

**Undoing the marking of parameters as favorites**

Using the shortcut menu, you can undo the favorites mark as follows:

- for one or more parameters: Mark multiple parameters using the shift key.
- All parameters belonging to a particular higher-level node.

**Exporting the definition of favorite parameters**

You can export favorite parameters in a Sirius favorite data (*.sfd) file using the "Export definition of favorite parameters" button.

**Importing the definition of favorite parameters**

You can import favorite parameters in a Sirius favorite data (*.sfd) file using the "Import definition of favorite parameters" button.

After the import, the result is displayed in the inspector window. Three different import results are possible:

- Favorite parameters successfully imported
- Favorite parameters unsuccessfully imported Probable cause: The imported file was generated from the parameterization of a completely different device, for example, a SIRIUS soft starter.
- Favorite parameters partially imported Probable cause: The imported file contains information about the parameters that are not supported by the hardware configuration of this device.

You can either undo or restore the import.

**Flat view of parameter favorites**

With the "Flat view" button, you can display parameters as a list.

**Hierarchical view of favorite parameters**

With the "Hierarchical View" button, you can display parameters as a list.

In this view, you can display the parameters as follows:

- With the "Collapse all" button, to show the parameter categories only
- With the "Expand all" button, to show parameter names and parameter values

**Filtering parameters**

You can filter the parameter view using a list box:

- All parameters
- Favorite parameters
- Parameters that are not favorites

**Saving the favorites status:**

Your current favorites status is stored together with the project. When you close the project, the favorites status is retained. When the project is next opened, the stored favorites status is loaded.

**Setting parameter values to default values**

The parameter default value is the initial value of the actual device configuration.

Using the shortcut menu, you can set parameter values to their default values:

- A single parameter value
- All parameter values below a particular group node or under a tree node
- All parameter values of the expert list

**Marking the parameters that can be adjusted during operation**

Parameters that can be adjusted during operation are indicated by a motor symbol in front of the parameter name.

> **Note**
>
> **Expert list in online mode**
>
> In online mode, the expert list is subject to some constraints:
>
> - Adding and removing favorite parameters is deactivated.
> - Importing favorite parameters is deactivated.

### Device wizard, Parameter wizard

The **device wizard** provides preconfigured applications in the standard and safety environment.

**Sequence:**

- Double-click the "Add new device" button
- Select the "Call Device Assistant" check box.
- Select a basic unit, for example, 3UF7 010-1A*00-0
- Select an application from the standard or safety environment, for example, Star-delta starter
- Activate the "Start Parameter Wizard" check box
- Click the "Finish" button
- The "**Parameter Wizard** - Control device_*, Category "Fieldbus interface" window opens
- Enter the basic type and clear the "Startup parameter block" check box, if necessary
- Click the "Next <<" button.
- The Category "Configuration" opens.

  - Make the necessary settings
  - Change the application (control function) as required.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the preconfigured application**  If you modify the pre-configured application, you may have to modify many protective functions, links and interlocks again manually.  You can select an application in the device wizard, and then receive a new SIMOCODE device with the corresponding sample configuration using the "Add new device" command. |  |

- Click the "Next <<" button.
- The category "Motor protection" opens

  - Set the parameters for Overload / Unbalance / Stalled rotor
- Click the "Next <<" button.
- The category "Motor monitoring" opens

  - Set the parameters for the monitoring functions
- Click the "Finish" button.

The configuration is not complete. Before completing the configuration, you can

- move one step forward or back with the "<< Previous" and "Next >>" buttons.
- cancel the configuration with the "Cancel" button.

### Automatic generation of I/O variables

If a SIMOCODE device is connected to a programmable logic controller (PLC), a check box will appear in the I/O Addresses dialog box with which you can activate automatic I/O variable generation.

If the feature is activated, the I/O variables will be generated for the inputs and outputs of all connected devices. The variables appear in the inspector window of the device and in the variables table of the connected PLC.

The following content is covered by automatic generation:

- Cyclic send data digital
- Cyclic send data analog
- Cyclic receive digital
- Cyclic receive analog

Changes to these parameters will result in updates to the variables table as long as the feature is active. Existing entries are not affected by this function.

> **Note**
>
> **Display of digital and analog variables**
>
> Only digital I/O variables are displayed in the inspector window of the SIMOCODE device.
>
> You must consult the variables table of the PLC to check the analog variables.

## Commissioning

This section contains information on the following topics:

- [Diagnostics - General](#diagnostics---general)
- [Marking](#marking-1)
- [Control/status information](#controlstatus-information)
- [Faults](#faults)
- [Warnings](#warnings)
- [Status information](#status-information)
- [Measured values](#measured-values)
- [Service Data / Statistical Data](#service-data-statistical-data)
- [Error buffer/error protocol](#error-buffererror-protocol)
- [Test](#test)
- [Command](#command)
- [Module firmware update](#module-firmware-update)
- [Password](#password)
- [Actual configuration](#actual-configuration)
- [Hardware inputs and outputs](#hardware-inputs-and-outputs)
- [Live trend (display online values)](#live-trend-display-online-values)
- [Parameter comparer](#parameter-comparer)
- [Dry-running protection wizard](#dry-running-protection-wizard)

### Diagnostics - General

SIMOCODE ES is a TIA Portal-based software tool for configuring, parameterizing, commissioning and diagnosing SIMOCODE pro switching devices.

Select **Devices → Project → S​IMOCODE​ → Commissioning** in the Project navigation view.

The **Diagnostics → General** button contains the information on the modules and the manufacturer.

Module

| Information | Meaning |
| --- | --- |
| Short code | Short code of the device |
| Article number | Article number (MLFB) of the device (MLFB = machine-readable product designation) |
| HW version | Corresponds to the I&M 0 value: Hardware_Revision <sup>1)</sup> |
| Firmware version | Corresponds to the I&M 0 value: Software_Revision <sup>1)</sup> |

1) Manufacturer-internal information

**Manufacturer information**

The manufacturer information contains the name of the manufacturer.

### Marking

The **Diagnostics → General** button contains the marking for the modules and the manufacturer.

In the Project navigation view, select **Devices → Project → Parameters →****Identification → Marking:**

Marking

| Information | Meaning |
| --- | --- |
| Plant ID | Plant designation |
| Location designation | Location specifications |
| Installation date | Date of installation / commissioning |
| Description | Additional Information |

### Control/status information

#### Controlling the feeder

The feeder is controlled with the "ON<<, ON<, OFF, ON>, ON>>" buttons.

The number of buttons depends on the control function selected. The buttons are not present on the overload relay. On the direct starter, only the "OFF" and "ON" buttons are shown. The buttons are only active when

- The operator enables for the operator panel [OP] are set when the connection is made via the system interface
- The operator enables for PC [DPV1] are set when the connection is made via the fieldbus.

#### Acknowledging faults

Faults are acknowledged and the device is made ready for operation again with the "Reset" button.

#### Hardware test

A hardware test is initiated with the "Test" button.

> **Note**
>
> The different messages are indicated by the lamp symbols.

### Faults

#### Displaying faults

Different fault messages concerning the following topics are indicated by lamp symbols:

- Control system
- Protection
- Safety technology
- Monitoring
- Other - General

#### Control system

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Execution ON command | The motor feeder could not be switched on after an ON command was issued. Possible causes of the fault:  - Main circuit is interrupted (fuse, circuit breaker) - The motor contactor or contactor control is defective - "Execution time" parameter too short.   Acknowledge with "Reset" or OFF command/counter-command. |
| Execution OFF command | The motor feeder could not be switched off after an OFF command was issued. Possible causes of the fault:  - The contactor contact is welded - "Execution time" parameter too short - The "OPEN" end position has not been reached during the parameterized runtime (only for the "Positioner" and "Solenoid valve" control functions).   Acknowledge with "Reset" or a counter-command. |
| Feedback ON | Current is flowing in the motor feeder without the motor feeder being switched on. Possible causes of the fault:  - Contactor contacts have been manually activated - Contactor was not activated using the corresponding SIMOCODE QE output - The "CLOSED" end position has not been reached during the parameterized runtime (only for the "Positioner" and "Solenoid valve" control functions).   Acknowledge with "Reset" or a counter-command. |
| Feedback OFF | The current flow in the motor feeder has been interrupted without the motor feeder being turned off. The positioner may be blocked. Possible causes of the fault:  - The main circuit has been interrupted (fuse, circuit breaker, main switch) - The motor contactor or contactor control is defective.   Acknowledge with "Reset". |
| Test position feedback | Current is flowing in the motor feeder although the motor feeder is in the test position (TPF).  The main circuit is not interrupted in test operation.  Acknowledge with "Reset". |
| Power failure (UVO) | The power failure lasted longer than the set power failure time.  Acknowledge with "Reset". |
| Stalled positioner | "Positioner" control function:  The torque switch has activated before or without the respective limit switch.  Possible cause of the fault: The positioner is blocked.  Acknowledge by "releasing" with the counter-command "OPEN/CLOSED".  Check the positioner application and the limit switches. |
| Double 0 | "Positioner" control function:  If both torque switches respond at the same time (FO=0 and FC=0), the positioner is immediately switched off with the fault message "Fault - double 0". Possible causes of the fault:  - Open circuit torque switch - Torque switch is defective. |
| Double 1 | "Positioner" control function:  If both limit switches respond at the same time (FO=1 and FC=1), the positioner is immediately switched off with the fault message "Fault - double 1".  Possible cause of the fault: Limit switch is defective. |
| End position | "Positioner" control function:  Positioner/solenoid valve has left the end position without a command being issued. The motor feeder has been turned off.  Acknowledge by "releasing" with the counter-command "OPEN/CLOSED". |
| Antivalence | "Positioner" control function:  The limit switches are not reporting any antivalent signals.  Possible cause of the fault: Limit switch open circuit.  Check the positioner application and the limit switches.  Acknowledge with the counter-command "OPEN/CLOSED" |

#### Protection

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Overload | The motor feeder has been overloaded.  Check the motor and the application that is being driven by the motor.  The motor can be switched on again after the cooling down period has expired or after an emergency start.  Acknowledge with "Reset", if auto reset is not active.  Further information: See [Overload protection](#overload-protection-1). |
| Overload + phase failure | The motor feeder has been overloaded.  Possible cause: Phase failure.  Check the motor and the motor feeder.  The motor can be switched on again after the cooling down period has expired or after an emergency start.  Acknowledge with "Reset", if auto reset is not active.  Further information: See [Overload protection](#overload-protection-1) and [Unbalance protection](#unbalance-protection). |
| Unbalance | The unbalance level has been exceeded.  Check the motor and the motor feeder.  The motor can be switched on again after the cooling down period has expired or after an emergency start.  Acknowledge with "Reset", if auto reset is not active.   Further information: See [Unbalance protection](#unbalance-protection). |
| Stalled rotor | The maximum motor current has exceeded the threshold for stalled rotor protection.  Possible cause of the fault: The motor is blocked.  Check the application that is being driven by the motor.  Acknowledge with "Reset".   Further information: See [Blocking protection](#blocking-protection). |
| Thermistor trip level | Thermistor protection has activated. The temperature of the motor is too high.  Check the motor and the application that is being driven by the motor.  The motor cannot be switched on again until the temperature has reached the reset point of the thermistor.  Acknowledge with "Reset", if auto reset is not active.   Further information: See [Thermistor protection](#thermistor-protection). |

#### Dry-running protection

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Dry running – pump | Dry running of the pump was prevented by switching off the pump motor.  Possible cause: The permissible limit value of the minimum flow rate Q<sub>min </sub>of the pump was undershot or the set limit value of the active power P<sub>min</sub> of the pump motor is not correct.  Solution: Make sure that the minimum flow rate specified for the pump is not undershot and that the monitored limit value of the active power P<sub>min</sub> has been set correctly. |
| Dry-running protection – error | An error was detected in the measured value acquisition of the active power of the pump motor or the teach process was interrupted with a timeout. The pump motor was switched off.  Possible causes:  - Fault in current/voltage measuring module - Unbalance in voltage or current of at least 30 % - Timeout in teach process.   Solution:  - Replace the faulty components - Check the power supply - Repeat the teach-in process |

#### Safety technology

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| DM-F safety-related tripping​ | The DM-F has tripped the enabling circuit for safety reasons.   The motor cannot be switched on again until the enabling circuits of the DM-F are reclosed.  Acknowledge with "Reset", if auto reset is not active.   Further information: See [Safety-related tripping](#safety-related-tripping). |
| DM-F wiring | A wiring error has occurred on the DM-F (short-circuit to ground in the sensor/feedback circuit).   Check the wiring of the sensor circuits/feedback circuit and correct the fault.   Acknowledge with "Reset".   Further information: See [Safety-related tripping](#safety-related-tripping). |
| DM-FL cross circuit | A cross-circuit fault has occurred in the sensor circuit of the DM-F Local.   Check the wiring of the two sensor circuits for cross-circuit faults and correct the fault.   Acknowledge with "Reset".   Further information: See [Safety-related tripping](#safety-related-tripping). |

#### Monitoring

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Trip level I> | The maximum current has overshot the trip level.  Check the application that is being driven by the motor.   Further information: See [Current limits I> (upper limit)](#current-limits-i-upper-limit). |
| Trip level I< | The maximum current has undershot the trip level.  Check the application that is being driven by the motor.   Further information: See [Current limits I< (lower limit)](#current-limits-i-lower-limit). |
| Internal ground fault | Internal ground-fault monitoring has activated. An impermissibly high fault current is flowing.  Check the motor connection cable for damage.  Acknowledge with "Reset".   Further information: See [Internal ground-fault monitoring when using a current measuring module or a 1st generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-1st-generation-current-voltage-measuring-module). |
| External ground fault | External ground-fault monitoring has activated. An impermissibly high fault current is flowing.  Check the motor connection cable for damage.  Acknowledge with "Reset".   Further information: See [External ground-fault monitoring](#external-ground-fault-monitoring). |
| Trip level P> | The active power of the motor has overshot the trip level.  Check the application that is being driven by the motor.   Further information: See [Active power monitoring](#active-power-monitoring). |
| Trip P< | The active power of the motor has undershot the trip level.  Check the application that is being driven by the motor.   Further information: See [Active power monitoring](#active-power-monitoring). |
| Trip level U< | The voltage in the motor feeder has undershot the trip level.  Possible causes:  - Undervoltage in the network - Fuse has tripped.   Check the motor feeder.   Further information: See [Voltage monitoring](#voltage-monitoring). |
| Trip level cos phi< | The power factor cos phi has undershot the trip level.  Possible cause: The motor is being operated without a load.  Check the application that is being driven by the motor.   Further information: See [Cos phi monitoring](#cos-phi-monitoring). |
| Trip level 0 / 4 ‑ 20 mA> | The measured value at the analog input has overshot the trip level.  Check the measuring station.   Further information: See [0 / 4 - 20 mA monitoring](#0-4---20-ma-monitoring). |
| Trip level 0 / 4 ‑ 20 mA< | The measured value at the analog input has undershot the trip level.  Check the measuring station.   Further information: See [0 / 4 - 20 mA monitoring](#0-4---20-ma-monitoring). |
| No. of starts > | The permissible number of starts in the monitoring timeframe has already been exceeded. The next start should not be carried out until the interlocking time has expired.   Further information: See [Number of starts monitoring motor](#number-of-starts-monitoring-motor). |
| Temperature at trip level T> | The temperature warning level has been exceeded.  Check the temperature measuring station.   Further information: See [Temperature monitoring (analog)](#temperature-monitoring-analog). |

#### Other - General

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| External fault 1 to 6 | A signal is pending at the input (socket) of the "External fault 1, 2, 3, 4, 5 or 6" standard function.  Check the motor feeder.  Acknowledgment depending on parameterization.   Further information: See [External fault (1 to 6)](#external-fault-1-to-6). |
| Bus | PROFIBUS DP communication has been interrupted or is interrupted.  Check the PROFIBUS connection (plugs, cables, etc.).  Acknowledge with "Reset", if auto reset is not active.   Further information: See [Watchdog (Bus monitoring, PLC/PCS monitoring)](#watchdog-bus-monitoring-plcpcs-monitoring) and [Diagnostics via LED display](#diagnostics-via-led-display). |
| PLC/PCS | The PLC that controls the feeder was or is in STOP mode.  Check the operating state of the PLC.  Acknowledge with "Reset", if auto reset is not active.   Further information: See [Watchdog (Bus monitoring, PLC/PCS monitoring)](#watchdog-bus-monitoring-plcpcs-monitoring). |
| Hardware fault basic unit | The SIMOCODE pro basic unit hardware is defective.  Replace the basic unit.   Further information: See [Replacing the basic unit](#replacing-the-basic-unit) and [Diagnostics via LED display](#diagnostics-via-led-display). |
| Module fault | At least 1 SIMOCODE pro module is not ready for use.  Possible causes:  - Connecting cable defective or incorrectly connected - Module defective. Replace the module.   Acknowledge with "Reset".   Further information: See  [Replacing the basic unit](#replacing-the-basic-unit) [Replacing the expansion module](#replacing-the-expansion-module) [Replacing the current measuring module and the current/voltage measuring module](#replacing-the-current-measuring-module-and-the-currentvoltage-measuring-module) [Diagnostics via LED display](#diagnostics-via-led-display). |
| Temporary components | Fault - temporary components (addressing plug, memory module or PC cable).  Replace the defective components.  Acknowledge with "Reset". |
| Configuration error | The configured device configuration does not match the actual configuration.  Measures:  - Check whether all the configured components are available - Check the actual configuration with "Configuration".   Acknowledge with "Reset".   Further information: See [Actual configuration](#actual-configuration). |
| Analog modules 1/2 open circuit | An open circuit has occurred in the analog value measuring circuit.  Check the measured value sensor and the measuring circuit.  Acknowledge with "Reset".   Further information: See [Analog module output](#analog-module-output). |
| Thermistor short circuit | A short circuit has occurred in the thermistor sensor cable.  Check the thermistor sensor cable and the thermistor.  Acknowledge with "Reset" after correcting the fault.   Further information: See [Thermistor protection](#thermistor-protection). |
| Thermistor open circuit | An open circuit has occurred in the thermistor sensor cable.  Check the thermistor sensor cable and the thermistor.  Acknowledge with "Reset" after correcting the fault.   Further information: See [Thermistor protection](#thermistor-protection). |
| Temperature module 1/2 sensor fault | Either a short circuit or an open circuit has occurred in the temperature sensor circuit.  Check the temperature sensor and the sensor cable.  Acknowledge with "Reset". |
| Temperature module 1/2 out of range | Temperature sensor is delivering impermissible values.  Check the temperature sensor.  Acknowledge with "Reset". |
| Parameterization | Incorrect parameters:  1. Set new parameters 2. Switch the control voltage off and on again. |
| Test trip | The motor feeder has been checked and switched off by a test trip.  Acknowledge with "Reset". |
| Operational Protection OFF (OPO) | An "Operational protection OFF (OPO)" signal is pending. A switched-on motor feeder has been switched off. The feeder cannot be switched on while the OPO signal is active.   Further information: See [Operational protection OFF (OPO)](#operational-protection-off-opo). |

### Warnings

#### Displaying warnings

Different warnings concerning the following topics are indicated by lamp symbols.

- Protection
- Safety technology
- Monitoring
- Other - General

#### Protection

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Prewarning overload (I>115%Is) | The motor feeder is in overload operation. If this condition continues to persist, the motor feeder will trip within a short period of time due to overload.  Check the motor and the application that is being driven by the motor. |
| Unbalance | The unbalance level has been exceeded.  Check the motor and the motor feeder.  The motor can be switched on again after the cooling down period has expired or after an emergency start.   Further information: See [Unbalance protection](#unbalance-protection). |
| Overload | The motor feeder has been overloaded.  Check the motor and the application that is being driven by the motor.  The motor can be switched on again after the cooling down period has expired or after an emergency start.   Further information: See [Overload protection](#overload-protection-1). |
| Overload + phase failure | The motor feeder has been overloaded.  Possible cause: Phase failure.  Check the motor and the motor feeder.  The motor can be switched on again after the cooling down period has expired or after an emergency start.   Further information: See overload protection and [Unbalance protection](#unbalance-protection). |
| Stalled rotor | The maximum motor current has exceeded the threshold for stalled rotor protection.  Possible cause of the fault: The motor is blocked.  Check the application that is being driven by the motor.   Further information: See [Blocking protection](#blocking-protection). |
| Thermistor trip level | Thermistor protection has activated. The temperature of the motor is too high.  Check the motor and the application that is being driven by the motor.  The motor cannot be switched on again until the temperature has reached the reset point of the thermistor.   Further information: See [Thermistor protection](#thermistor-protection). |

#### Safety technology

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Monitoring interval for mandatory testing | The enabling circuits of the DM-F Local / DM-F PROFIsafe have not been opened and closed again within the configured time period.  The function of the enabling circuit relay contacts can only be tested when they are switched.   Further information: See [Monitoring interval for mandatory testing](#monitoring-interval-for-mandatory-testing). |
| DM-F safety-related tripping | The DM-F has tripped the enabling circuit for safety reasons.  The motor cannot be switched on again until the enabling circuits of the DM-F module are reclosed.   Further information: See [Safety-related tripping](#safety-related-tripping). |
| DM-FL simultaneity | The DM-F Local has detected a discrepancy error in the two-channel sensor circuit.  Check the switching elements in the sensor circuit. |
| DM-F feedback circuit | The DM-F has detected a fault in the feedback circuit.  The feedback circuit must be closed at the time of switching on the enabling circuit.  Check the feedback circuit of the DM-F Local or DM-F PROFIsafe. |

#### Monitoring

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Warning level I> | The maximum current has overshot the warning level.  Check the application that is being driven by the motor.   Further information: See [Current limits I> (upper limit)](#current-limits-i-upper-limit). |
| Warning level I< | The maximum current has undershot the warning level.  Check the application that is being driven by the motor.   Further information: See [Current limits I< (lower limit)](#current-limits-i-lower-limit). |
| Internal ground fault | Internal ground-fault monitoring has activated. An impermissibly high fault current is flowing.  Check the motor connection cable for damage.   Further information: See [Internal ground-fault monitoring when using a current measuring module or a 1st generation current / voltage measuring module](#internal-ground-fault-monitoring-when-using-a-current-measuring-module-or-a-1st-generation-current-voltage-measuring-module). |
| External ground fault | External ground-fault monitoring has activated. An impermissibly high fault current is flowing.  Check the motor connection cable for damage.   Further information: See [External ground-fault monitoring](#external-ground-fault-monitoring). |
| Warning level P> | The active power of the motor has overshot the warning level.  Check the application that is being driven by the motor.   Further information: See [Active power monitoring](#active-power-monitoring). |
| Warning level P< | The active power of the motor has undershot the warning level.  Check the application that is being driven by the motor.   Further information: See [Active power monitoring](#active-power-monitoring). |
| Warning level U< | The voltage in the motor feeder has undershot the warning level.  Possible causes:  - Undervoltage in the network - Fuse has tripped.   Check the motor feeder.   Further information: See [Voltage monitoring](#voltage-monitoring). |
| Warning level cos phi < | The power factor cos phi has undershot the warning level.  Possible cause: The motor is being operated without a load.  Check the application that is being driven by the motor.   Further information: See [Cos phi monitoring](#cos-phi-monitoring). |
| Warning level 0 / 4 ‑ 20 mA> (analog module 1/2) | The measured value at the analog input has overshot the warning level.  Check the measuring station.   Further information: See [0 / 4 - 20 mA monitoring](#0-4---20-ma-monitoring). |
| Warning level 0 / 4 ‑ 20 mA< (analog module 1/2) | The measured value at the analog input has undershot the warning level.  Check the measuring station.   Further information: See [0 / 4 - 20 mA monitoring](#0-4---20-ma-monitoring). |
| No. of starts > | The permissible number of starts in the monitoring timeframe has already been exceeded. The next start should not be carried out until the interlocking time has expired.   Further information: See [Number of starts monitoring motor](#number-of-starts-monitoring-motor). |
| Just one start possible | The start after the next one should not be carried out until the interlocking time has expired. |
| No start permitted | The permissible number of starts in the monitoring timeframe has been attained. The next start should not be carried out until the interlocking time has expired. |
| Motor operating hours > | The configured limit value for motor operating hours monitoring has been exceeded.  Apply the maintenance measures intended for the feeder. |
| Stop time > | The configured limit value for stop time monitoring has been exceeded.  Apply the maintenance measures intended for the feeder. If possible, switch on the feeder. |
| Warning level T > | The temperature warning level (temperature module 1/2) has been exceeded.  Check the temperature measuring station.  Further information: See [Temperature monitoring (analog)](#temperature-monitoring-analog). |
| DM-F test requirement | The enabling circuits of the DM-F Local / DM-F PROFIsafe have not been opened and closed again within the configured time period.   The function of the enabling circuit relay contacts can only be tested when they are switched.   Apply the maintenance measures prescribed for this scenario. |

#### Other - General

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| External fault 1 to 6 | A signal is pending at the input (socket) of the "External fault 1, 2, 3, 4, 5 or 6" standard function.  Check the motor feeder.  Further information: See [External fault (1 to 6)](#external-fault-1-to-6). |
| Analog modules 1/2 open circuit | An open circuit has occurred in the analog value measuring circuit.  Check the measured value sensor and the measuring circuit.   Further information: See [Analog module output](#analog-module-output). |
| Thermistor short circuit | A short circuit has occurred in the thermistor sensor cable.  Check the thermistor sensor cable and the thermistor.   Further information: See [Thermistor protection](#thermistor-protection). |
| Thermistor open circuit | An open circuit has occurred in the thermistor sensor cable.  Check the thermistor sensor cable and the thermistor.   Further information: See [Thermistor protection](#thermistor-protection). |
| Temperature module 1/2 sensor fault | Either a short circuit or an open circuit has occurred in the temperature sensor circuit.  Check the temperature sensor and the sensor cable. |
| Temperature module 1/2 out of range | Temperature sensor is delivering impermissible values.  Check the temperature sensor. |

### Status information

#### Display of messages

| Display | Meaning/possible fault cause/acknowledgment/fault correction |
| --- | --- |
| Startup parameter block active | The startup parameter block prevents transfer of SIMOCODE pro parameters that can be saved in the DP master.  The block **must** be set if SIMOCODE ES or SIMATIC PDM is used for parameterization.  The block **must not** be set if SIMOCODE pro is integrated into STEP 7 via the SIMOCODE pro Object Manager (OM), or if SIMOCODE pro C has been parameterized via the GSD. |
| Configuration error | The configured device configuration does not match the actual configuration.  - Check whether all the configured components are available - Check the actual configuration with "Configuration". |
| Required function is not supported | At least one parameterized function is not supported by the version of the basic unit.  Activate only the functions that are supported by the version of the basic unit. For example, SIMOCODE pro V basic units with the version *E01* do not support voltage measurement, the temperature module, or the analog module. |
| Wrong parameter | The parameter data transferred to the unit is incorrect. Errors in the parameter data can occur, for example, if the device has not been parameterized with SIMOCODE ES or SIMATIC PDM.  Check the parameter data (data sets 130 - 133) that has been transmitted to the device for the correct content. |
| Parameter changes not allowed in the current operating state | You attempted to change at least one parameter that cannot be changed in the current operating state. Many parameters can only be changed if the motor feeder is switched off and not in "Remote" mode. |
| Password wrong | The SIMOCODE pro parameters are protected by a password. An attempt has been made to change the parameters without entering the password.  Please use the correct password for changing the parameters. If you do not know the password, new parameters can only be entered after the factory settings have been restored.   Further information: See [Restoring factory settings](#restoring-factory-settings). |
| DM-F safety-related tripping | The DM‑F Local / DM‑F PROFIsafe has tripped the enabling circuits for safety reasons.  The motor cannot be switched on again until the enabling circuits of the DM-F module are reclosed.   Further information: See [Safety-related tripping](#safety-related-tripping). |
| Monitoring interval for mandatory testing | The enabling circuits of the DM-F Local / DM-F PROFIsafe have not been opened and closed again within the configured time period.  The function of the enabling circuit relay contacts can only be tested when they are switched.   Further information: See [Monitoring interval for mandatory testing](#monitoring-interval-for-mandatory-testing). |
| DM‑F Local o.k. | The DM-F Local is ready for operation. |
| PROFIsafe active | The DM-F PROFIsafe is in the "PROFIsafe active" status. |
| DM-F Local configuration mode | The DM-F Local is in "Configuration mode" status.  Complete the configuration. |
| DM-F Local Actual and set configuration are different | The actual configuration of the DM-F Local does not correspond to the parameterized set configuration.  Check whether the effective configuration actually agrees with the parameterized set configuration, and if necessary, correct the effective configuration by setting the DIP switches or the parameterized set configuration. |
| DM-F Local waiting for start-up test | The DM-F Local is in the "Waiting for start-up test" status. |
| DM‑F incorrect PROFIsafe address or incorrect PROFIsafe parameters | The parameter settings of the PROFIsafe profile are incorrect or the set PROFIsafe address is not identical to the configured address.  Check the PROFIBUS/PROFIsafe parameters of SIMOCODE pro that were set on the DP master system. (Modify text) |
| Status - enabling circuit closed | The enabling circuits of the DM‑F Local / DM‑F PROFIsafe are closed. |
| No module voltage | Supply voltage on the DM‑F is either too low or there is no voltage.  Check whether the terminals are correctly wired.  The DM‑F module is possibly defective. Replace the module. |
| Initialization module write-protected | The initialization module is completely write-protected.  Deactivate write protection of the initialization module. |
| Initialization module write-protected, parameter changes not allowed | The initialization modules is completely or partially write-protected. Reparameterization of SIMOCODE pro is denied because the initialization module is write-protected.  Deactivate write protection of the initialization module. |
| Initialization module identification data write-protected | The device addressing and the I&M data in the initialization module are write-protected. Parameterization will only be accepted by SIMOCODE if the new parameter set is identical to the data stored in the initialization module at that time.  - Select a parameterization with identical addressing and I&M data - Deactivate the partial write protection of the initialization module. |
| Initialization module read in | The parameters of the initialization module were read into SIMOCODE. |
| Initialization module programmed | The reparameterization was accepted in the initialization module. |
| Initialization module deleted | The initialization module was deleted and is now back in the as-delivered state. |
| Memory module read in | The parameters of the memory module were read into SIMOCODE. |
| Memory module erased | The memory module was deleted and is now back in the as-delivered state. |
| Memory module programmed | The reparameterization was accepted in the memory module. |
| Memory module write-protected | The memory module is completely write-protected.  Deactivate write protection of the memory module. |

### Measured values

#### Displaying measured values

| Frequency | Range | Unit | Float value range |
| --- | --- | --- | --- |
| Frequency | 0 to 65535 | Hz | -3.40282347 x 10<sup>38</sup> ... +3.40282347 x 10<sup>38</sup> |

| Current | Range | Unit | Float value range | Float unit |
| --- | --- | --- | --- | --- |
| Average current I_ave | 0 to 65535 | A | in each case  -3.40282347 x 10<sup>38</sup> ... +3.40282347 x 10<sup>38</sup> | - |
| Max. current I_max | 0 to 65535 | % of Ie | A |  |
| Current I_L1 | 0 to 65535 | % of Ie | A |  |
| Current I_L2 | 0 to 65535 | % of Ie | A |  |
| Current I_L3 | 0 to 65535 | % of Ie | A |  |
| Last trip current | 0 to 65535 | % of Ie | - |  |
| Phase unbalance | 0 to 100 | % (100% corresponds to the failure of one phase) | - |  |

For more information on the set current I<sub>s</sub>, go to [Overload protection](#overload-protection-1).

| Voltage | Range | Unit | Float value range |
| --- | --- | --- | --- |
| Voltage U_L1 | 0 to 65535 | V | in each case  -3.40282347 x 10<sup>38</sup> ... +3.40282347 x 10<sup>38</sup> |
| Voltage U_L2 | 0 to 65535 | V |  |
| Voltage U_L3 | 0 to 65535 | V |  |

For voltage measurements, you require SIMOCODE pro V with a current/voltage measuring module.

| Thermal motor model | Range | Unit |
| --- | --- | --- |
| Thermal memory | 0 to 254 | %, related to the symmetrical trip level;  Representation in steps of 2% in bits 6 to 0 (value range: 0 to 254%);  Bit 7 indicates unbalance (fixed level 50%) |
| Remaining cooling down period | 0 to 65535 | s |
| Time to trip | 0 to 65535 | s (the motor is currently not in an overload situation. However, under the current load conditions, the motor will be switched off in x seconds due to overload.) |

For further information, refer to [Overload protection](#overload-protection-1).

| Power/power factor | Range | Unit | Float value range |
| --- | --- | --- | --- |
| Active power P | 0 to 4294967.295 | kW | in each case  -3.40282347 x 10<sup>38</sup> ... +3.40282347 x 10<sup>38</sup> |
| Apparent power S | 0 to 4294967.295 | kVA |  |
| Cos phi | 0 to 100 | Power factor is 100% if no motor current is flowing or no voltage is measured |  |

For power considerations, you require SIMOCODE pro V with a current/voltage measuring module.

| Temperature module 1/2 | Range | Unit |
| --- | --- | --- |
| Max. temperature | - 273 to 65262 | °C |
| Temperature 1 | - 273 to 65262 | °C |
| Temperature 2 | - 273 to 65262 | °C |
| Temperature 3 | - 273 to 65262 | °C |

For temperature measurements, you require SIMOCODE pro V with a temperature module and the corresponding temperature sensor.

| Analog module 1/2 | Range | Unit |
| --- | --- | --- |
| Analog module - input 1 | 0 to 27648 | S7 format: 0/4 mA = 0, 20 mA = 27648 |
| Analog module - input 2 | 0 to 27648 | S7 format: 0/4 mA = 0, 20 mA = 27648 |
| Analog module - output | 0 to 27648 | S7 format: 0/4 mA = 0, 20 mA = 27648 |

| Internal ground fault current | Range | Unit |
| --- | --- | --- |
| Ground-fault current | 0 to 65535 | mA |
| Last trip current | 0 to 65535 | mA |

### Service Data / Statistical Data

#### Displaying statistical data

| **Motor** | **Range** |
| --- | --- |
| Motor operating hours | 0 to 1193046 h |
| Motor operating hours > | See [Warnings](#warnings) |
| Number of overload trips | 0 to 65535 |
| Number of starts | 0 to 4294967295 |
| Permissible starts - actual value | 0 to 255 |
| Just one start possible | See [Warnings](#warnings) |
| No start permitted | See [Warnings](#warnings) |
| Stop time | 0 to 65535 h |
| Stop time > | See [Warnings](#warnings) |
| Consumed energy | 0 to 4294967295 kWh |
| Time until test required | 0 to 255 w (weeks) |
| Test required | See [Warnings](#warnings), DM-F test requirement |

For example, via "Motor operating hours" and "Number of starts", you can decide whether the motor and/or the motor contactors should be replaced. You can modify these values by entering a new value in the right input field and then clicking on "Set". The value is adopted by the device.

| **Basic unit** | **Range** | **Meaning** |
| --- | --- | --- |
| Time shift UTC + | h | Configured time difference between the module time and UTC (Universal Time Coordinated) (only in conjunction with the SIMOCODE pro V PN and SIMOCODE pro V EIP basic units) |
| Device operating hours | 0 to 1193046 | Specifies for how long the power supply of the SIMOCODE pro was switched on.   For further information, refer to [Error buffer/error protocol](#error-buffererror-protocol). |
| Number of parameterizations | 0 to 65535 |  |
| Parameter assignments  - Date - Time |  | Time information for the unbuffered real-time clock (only in conjunction with the SIMOCODE pro V PN and SIMOCODE pro V EIP basic units).  The real-time clock can be synchronized using an NTP server or set via Target System → [Command](#command). |

#### Setting ranges for timers, counters and calculators

- Timer 1-6 - actual value; Range: 0 to 6553.5 s
- Counter 1-6 - actual value; Range: 0 to 65535
- Calculators 1-4 - output; Range: 0 to 65535
- Analog multiplexer output (0/1)

### Error buffer/error protocol

Timestamping in the error buffer is based on the operating hours (resolution: 1 s) of SIMOCODE pro.

The "Error/Fault" and "Power - On" events are logged. Each of these events is given a time stamp.

- Error/Fault: The last 21 errors are stored in a ring buffer; the incoming error (rising edge) is always logged. An outgoing error (falling edge) will not be logged.
- Power on: If the most recent entry is "Power - On," this is not logged multiple times. Instead, the error number is used as a power-on counter. Thus, the error buffer cannot be deleted by frequent on/off operations.

Entry 1 is the most recent entry and entry 21 the oldest.

When using a DM-F, the events "Enabling circuit closed" and "Enabling circuit open" are logged for the DM-F Local and/or the DM-F PROFIsafe in a separate window:

- Time
- Event: "Enabling circuit closed" or "Enabling circuit open"
- Number:

  - Line 1 200 or 202
  - Line 2 201 or 203
- Text:

  - Line 1: "DM‑F Local enabling circuit 0 → 1" or "DM‑F PROFIsafe enabling circuit 0 → 1
  - Line 2: "DM-F Local enabling circuit 1 → 0" or "DM-F PROFIsafe enabling circuit 1 → 0.

The current DIP switch position of the "DM-F Local" and/or the "DM-F PROFIsafe" is displayed under "DIP switch position DM-F during the last event".

### Test

#### Testing functions

1. Select the device-internal outputs (digital and analog sockets) and display the logic states.
2. Select the device-internal inputs (digital and analog plugs) and set their input signals to 0 or 1 by clicking on the corresponding buttons.
3. Display the logic states of the device-internal inputs (digital and analog plugs). You can use this procedure to test the functioning of the truth tables, for example.

> **Note**
>
> **Changing an input**
>
> Changing an input is only possible in the test position, in other words, the standard function "[Test position feedback (TPF)](#test-position-feedback-tpf)" (![Testing functions](images/148925064075_DV_resource.Stream@PNG-de-DE.png) digital input,![Testing functions](images/148925073035_DV_resource.Stream@PNG-de-DE.png) analog input) must be active (blue plug on the symbol on the left)!

### Command

> **Note**
>
> A command is executed immediately!

| Command | Meaning |
| --- | --- |
| Addressing plug - adopt station address | Read in the station address from the addressing plug. The addressing plug must be plugged into the system interface for this purpose. |
| Program memory module | Parameters are transferred to the memory module. The memory module must be plugged into the system interface for this purpose. |
| Clear memory module | Parameters in the memory module are deleted. The memory module must be plugged into the system interface for this purpose. |
| Read memory module | Transfer of the parameters from the memory module to the basic unit. The memory module must be plugged into the system interface for this purpose. |
| Write protection of the memory module is switched on | All contents of the memory module are write-protected. This prevents any inadvertent changes to the contents of the memory module and any parameter changes to the connected SIMOCODE pro basic unit.  An inadvertent change of parameters for a motor feeder is prevented.  SIMOCODE pro signals the successful execution of the command with the event "Memory module write-protected". |
| Write protection of the memory module is switched off | With this command you can cancel the write protection of the memory module. |
| Initialization module write protection on | All contents of the initialization module are write-protected. This prevents any inadvertent changes to the contents of the initialization module and any parameter changes to the connected SIMOCODE pro basic unit.  An inadvertent change of parameters for a motor feeder is prevented.  SIMOCODE pro signals the successful execution of the command with the event "Initialization module write-protected". |
| Initialization module write protection off | With this command, you can remove the write protection of the initialization module. |
| Initialization module write protection for identification data on | (Identification & Maintenance) are write-protected. With this command, you can  - prevent inadvertent changes to the parameters (e.g. device names) and the I&M data for the motor feeder. - continue to make parameter changes in the initialization module as well as in the SIMOCODE basic unit if the address data and I&M data are identical to the data already contained in the device when parameters are downloaded.   SIMOCODE pro signals the successful execution of the command with the event "Initialization module identification data write-protected". |
| Initialization module identification data write protection off | With this command, you can remove the write protection of the identification data of the initialization module. |
| Clear initialization module | With this command  - all contents of the initialization module are deleted - The initialization module is reset to the as-delivered state.   SIMOCODE pro signals the successful deletion with the "Initialization module cleared" event.  On startup with an empty initialization module, the basic unit signals "Fault - parameterization". The "General Fault" LED of the basic unit flashes red.  Reparameterization of the device, e.g. with SIMOCODE ES, writes valid parameters to the basic unit and the initialization module again. You can then acknowledge the fault message. |
| Restart/cold start | Initialization of SIMOCODE pro. New start. |
| Factory settings | All parameters have their factory setting again, except for the password. Only possible if password protection is not active or the password is known. |
| Set time (= PC time) | If an NTP server address has not been configured or a server was not found on the network, you can set the time of day here. The system time of the PC is then calculated and transferred to the device in the format "NTP clock".  If a valid time of day is available (either synchronized by NTP or set via SIMOCODE ES), the entries in the error buffer / error protocol (i.e. log) will be additionally displayed with the time of day. In addition, the "Clock set (NTP)" and "Clock synchronized (NTP)" messages are displayed. |
| Test | [Execute](#testreset) test function. Same function at "TEST/RESET" button on the basic unit and operator panel. |
| Reset | Performing a reset operation. Acknowledging faults. Same function as "TEST/RESET" button on the basic unit and on the operator panel. |

### Module firmware update

You can use this function to update the firmware of the following SIMOCODE pro basic units. You can download the firmware versions on the Support page:

- [Firmware update for SIMOCODE pro V PB basic unit from product version *E15*](https://support.industry.siemens.com/cs/ww/en/view/109767656)
- [Firmware update for SIMOCODE pro V MR basic unit from product version *E03*](https://support.industry.siemens.com/cs/ww/en/view/109771740)
- [Firmware update for SIMOCODE pro V PN basic unit from product version *E08*](https://support.industry.siemens.com/cs/de/en/view/109749989)
- [Firmware update for SIMOCODE pro V EIP basic unit](https://support.industry.siemens.com/cs/de/en/view/109756912)

> **Note**
>
> The parameterization of the device is retained after the firmware has been updated.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Connection to the device**  The connection by USB PC cable or Ethernet must not be interrupted during the update procedure. |  |

**Requirements:**

- The basic unit must be connected to SIMOCODE ES via online connection, USB PC cable (PtP) or Ethernet.
- The supply voltage must be present on the basic unit at the start of and during the firmware update.
- A firmware update is only possible if:

  - The motor is in the "off" state and there is no motor current
  - The control station is in "Local manual" status
  - The device is not protected by a password

**Firmware update**

You can perform the firmware update via the SIRIUS PC USB cable (SIRIUS PtP) with the assistance of the SIMOCODE ES (TIA Portal) software, all versions Basic / Standard / Premium V15 or higher or Professional V16 or higher.

Firmware update via Ethernet has been supported since software version SIMOCODE ES V13 SP1.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Risk of impermissible system states.**  Installation of the firmware update switches the basic unit into "station failure" state. This state can affect the operation of an online process or a machine.  Unexpected operation of a process or a machine can lead to fatal or severe injuries and/or to property damage.  Before installing the firmware update, ensure that the basic unit is not involved in an active process. |  |

**Update procedure:**

1. Select the module in the device configuration
2. Select the "Online & diagnostics" command from the shortcut menu
3. Select the "Firmware update" group in the "Functions" folder
4. Click the "Browse" button to select the path to the firmware update files
5. Select the firmware file from the folder into which you previously unpacked the download file. The table in the "Firmware update" area lists those modules under "Suitable for modules" for which an update is possible with the selected firmware file.
6. Click the "Run update" button. If the module can interpret the selected file, the file is downloaded to the module

**Updating the firmware**

The "Run firmware after update" check box is always selected. When the loading process is complete, the module works with the new firmware.

> **Note**
>
> **Avoid interrupting the firmware update**
>
> If you interrupt a firmware update, the device is not ready for use. In this case, the "BUS" and "GEN FAULT" LED indicators flash alternately and the "DEVICE" LED lights up red.

Note the following behavior during the firmware update:

The "BUS" and "GEN FAULT" LED indicators flash alternately and the "DEVICE" LED lights up red.

**Checking behavior after the firmware update**

After the firmware update, check the firmware version of the basic device for which you performed the firmware update.

### Password

Assign a password for SIMOCODE pro. This allows the protection in the basic unit to be activated or deactivated. Only if protection is deactivated can parameters be saved in or exported to the basic unit.

> **Note**
>
> If the password is not known, parameter changes can only be carried out after "Establish factory settings with TEST/RESET on the basic unit"!
>
> The current device parameters (including the password) are thus restored to the factory settings.

---

**See also**

[Restoring factory settings](#restoring-factory-settings)

### Actual configuration

- Establish a connection with SIMOCODE pro.
- Select **Devices > Project → S​IMOCODE​ → Commissioning → Actual configuration** in the Project navigation view.
- Establish whether or not the set device configuration agrees with the actual device configuration. The following is displayed:

  - Which modules are connected
  - How the modules are configured
  - The configuration of the modules and the offline project.
- Check DIP switch position (if DM1 = DM-F Local or DM-F PROFIsafe):

  The "Actual configuration" shows the actual DIP switch position from data set 105 (see [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951) SIMOCODE pro).

  The configured DIP switch position comes from data set 130 (see [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951)).

  Meaning of the individual DIP switches: See [Manual Fail-safe Digital Modules SIMOCODE pro](http://support.automation.siemens.com/WW/view/en/50564852) and [Safety-related tripping](#safety-related-tripping).

---

**See also**

[Device configuration dialog box](#device-configuration-dialog-box)
  
[System manuals](http://support.automation.siemens.com/WW/view/en/20369671/133300)

### Hardware inputs and outputs

In the Project Navigation Devices view, you call up the device data with the menu command **"Project → Commissioning → Diagnostics → Hardware inputs and outputs**".

The state of the digital inputs and outputs of the SIMOCODE pro basic unit and the proportion of the current in terms of the rated current flowing in the cables as a percentage.

The color of the LEDs of the non-interconnected inputs/outputs is gray. If the inputs/outputs are interconnected, the LEDs show a green light.

### Live trend (display online values)

#### Functional principle

With the "Live Trend“ function, you can display the course of various measured values over time once you have already established an online connection with SIMOCODE pro. The following measured values can be displayed simultaneously:

- maximum eight digital measured values at the inputs

- maximum four analog measured values at the inputs

- any number of measured values at the outputs.

You can create different recordings (traces) that are also stored device-specifically.

#### Setting the update interval

The update interval can be set under "**Options → Settings → SIRIUS ES → Cyclic update interval**".

Enter the cyclic update interval for measuring the limit values and the options.

Range: 500 to 32500 ms.

> **Note**
>
> **Influences on the update rate**
>
> The cyclic update interval also influences the update rate in all menus of the commissioning editor.

#### Select configuration, set recording duration and sampling rate

- Select "Live Trend" as the active configuration.

  Set the recording duration (range: 0:00:00.000 to 24:00:00.000 h:mm:ss.xxx)
- Set the sampling rate (frequency with which a signal is sampled and converted to a time-discrete signal during the specified recording duration) (range: 0:00:00.000 to 24:00:00.000 h:mm:ss.xxx)

#### Selection of the measured values and signals

- Open the menu item "Traces" in the project navigation.
- Create a recording by double-clicking on the button "Add new trace", or select a recording by double-clicking
- Select "Live Trend" as the configuration.
- Choose what you want to display (measured values, binary signals) in the table "Monitor signals".
- Select the color for the trace curve(s)
- Enter a comment for each trace curve (optional)
- Transfer the trace configuration to the device using the relevant buttons.

The recording is started automatically. The values are updated cyclically.

#### Recording measured values and exporting signals/measured values

At the intersections of the black vertical line with the measured curves, you can read the current interpolated values for each measured curve.

If you want to execute another operation at the same time as recording, you can split the window vertically ![Recording measured values and exporting signals/measured values](images/148925184139_DV_resource.Stream@PNG-de-DE.png) or horizontally ![Recording measured values and exporting signals/measured values](images/148925192843_DV_resource.Stream@PNG-de-DE.png) via "Window" in the main menu.

You can also manually add a measurement to the measurements, export the configuration, and export with the settings of the current view. To do this, click on the relevant symbols. You reach the detailed Help via the Tooltip Help of the symbols.

> **Note**
>
> Only the last selected measuring points are saved.

#### Setting options for scales and measured curves

The y axis shows the measured values or signals, and the x axis shows the time.

A separate y scale with a specific color is shown for each measured curve.

**Scale:**

The scales of the x axis and the y axis can be adjusted dynamically and infinitely using the mouse (while holding down the left mouse key) as follows:

- Changing the maximum upper scale value: Drag the mouse cursor upwards in the scale range while holding the mouse key pressed.
- Changing the maximum lower scale value: Drag the mouse cursor downwards in the scale range while holding the mouse key pressed.

This changes the mouse pointer to the symbol ![Setting options for scales and measured curves](images/148921714955_DV_resource.Stream@PNG-de-DE.png) in the scale range.

By double-clicking with the left mouse key in the scale range, a scale is reset to its default setting.

The upper and lower scale value of the y axis can each be blocked with a ![Setting options for scales and measured curves](images/148921732107_DV_resource.Stream@PNG-de-DE.png) button.

The left and right scale value of the x axis can each be blocked with a ![Setting options for scales and measured curves](images/148921732107_DV_resource.Stream@PNG-de-DE.png) button.

Each measured curve can be shown and hidden via its own checkbox.

**Zooming:**

You can zoom the measured curves using the following buttons:

- Zoom in horizontally: ![Setting options for scales and measured curves](images/148921770635_DV_resource.Stream@PNG-de-DE.png)
- Zoom out horizontally: ![Setting options for scales and measured curves](images/148921813387_DV_resource.Stream@PNG-de-DE.png)
- Zoom in vertically: ![Setting options for scales and measured curves](images/148921843339_DV_resource.Stream@PNG-de-DE.png)
- Zoom out vertically: ![Setting options for scales and measured curves](images/148921860491_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Information system**
>
> You will find the corresponding help for symbols in the information system under "Using online and diagnostics functions → Using the trace and logic analyzer function → Software interface → Work area → Interface - Diagram tab → Interface → Curve diagram".

### Parameter comparer

#### Function

The parameter comparer indicates the differences between the values at different storage locations. It is only active in online mode.

The online data is downloaded once from the device when you go online.

The dialog displays the following in the form of a table:

- The names of the parameters whose values differ
- The values in the project (offline)
- The current values in the software (online)
- The current values in the device

#### Example: Differences between project and device

| Parameter name | Value in the project (offline) | Value in the software (online) | Value in the device |
| --- | --- | --- | --- |
| Set current Is1 | 0.30 A |  | 3.00 A |
| Class | 10 |  | 5 |

#### Procedure

1. In the project tree, select the device whose parameters you wish to compare
2. Establish an online connection to the device
3. Open the "Commissioning" editor and select "Parameter comparer".

The table shows differences between the values of individual parameters in the device and the equivalent values in the project. If the table is empty, there are no differences between the project and the devices.

#### How do the differences occur?

You make changes to the values in the parameter editor in offline mode. You then select "Connect online", without first having performed an "Download to device".

You make changes to values in the parameter editor in offline mode without performing the following two actions:

- "Transfer online data to the hardware" and
- "Transfer online data to the offline project"

### Dry-running protection wizard

#### Prerequisites for starting the dry-running protection wizard

- Use of one of the following basic units with PTB 18 ATEX 5003 X:

  - 3UF7010-1A.00-0 (from product version *E16*)
  - 3UF7011-1A.00-0 (from product version *E13*)
  - 3UF7013-1A.00-0 (from product version *E04*)
- One of the following 2nd generation current / voltage measuring modules

  - 3UF7120-1AA01-0 (DRP)
  - 3UF7121-1AA01-0 (DRP)
  - 3UF7122-1AA01-0 (DRP)
  - 3UF7123-1AA01-0 (TLS)
  - 3UF7123-1BA01-0 (DRP)
  - 3UF7124-1BA01-0 (DRP)
- Under "Device configuration", set control function "direct starter" (direct-on-line starter)
- The commissioning editor must have been switched to online mode
- Under "Motor protection → Overload protection", the load type must be set to "three phase"
- Under "Motor protection → Overload protection", check box "Transformation ratio - active" must be selected and Transformation ratio - primary must be set to "1" and Transformation ratio - secondary must be set to ">0"
- Password protection must be deactivated. If password protection is activated, you must deactivate it.
- If you are using an in initialization module, it must not be write-protected.
- The startup parameter block under "PROFINET parameters" in the parameter editor must be activated

#### Sequence of operation for dry-running protection wizard

First start the pump (according to the instructions provided in the documentation of the pump manufacturer) and ensure that the pump has attained operating conditions (especially temperature)

Next, perform the following steps as you are prompted in the input sequence:

- In the commissioning editor, open the "Dry-running protection" menu.
- Click the button "Start Dry Running Wizard". The "Dry-running protection wizard" window opens.
- Select the menu "Temporary parameters for teach-in". The currently active parameters are displayed.

  - Response
  - Trip level
  - Tripping delay time
  - Start-up bridging time.
- Check the settings for use of a temporary trip level [Dry-running protection of centrifugal pumps based on active power monitoring](#dry-running-protection-of-centrifugal-pumps-based-on-active-power-monitoring)

  - Observe the reports and messages

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Changing the currently active setting**  You can only change the currently active setting by entering the parameters directly. Close the dry-running protection wizard to do this.  Remember that the pump is still in operation (limited by the timer that monitors during inactivity). |  |
- Click "Next". The menu "Find optimum active power value" opens
- Set the numeric value for the flow rate to the operating point Q<sub>opt</sub> that you can read off the flow rate measuring device on the discharge side in field " Q<sub>opt</sub> (m<sup>3</sup>/h)"
- Observe the status message
- Click "Next". The menu "Find minimum active power value" opens
- Set the minimum flow rate on your process system and manually enter the numeric value for the minimum flow rate Q<sub>MIN</sub> that you can read off the flow rate measuring device on the discharge side (SIMOCODE pro records the associated active power P<sub>MIN</sub>).
- Click "Next". The menu "Set active power level" opens. The calculated trip level is displayed. The trip value determined by the system P<sub>TRIP</sub> = 1.1*P<sub>MIN</sub> for the active power is displayed.
- Observe the status messages
- Click "Next". The menu "Set delay parameters" opens.
- Enter the delay time t<sub>V, TRIP</sub> for running operation of the centrifugal pump (default value: 0 s) on.
- Enter the start-up bridging time t<sub>BRIDGE</sub> (default value: 0 s)
- Observe the status messages
- Click "Next". The "Summary" menu opens. Check the displayed parameter values (P<sub>TRIP</sub>, t<sub>V,TRIP</sub>, t<sub>BRIDGE</sub>) for the dry-running protection by active-power monitoring and the set values pairs P<sub>OPT</sub> / Q<sub>OPT</sub> and P<sub>MIN</sub><sup> </sup>/ Q<sub>MIN</sub>. Make sure that all parameter values are displayed and that the displayed configuration is suitable
- Observe the status messages
- Click "Exit". You have now completed the input sequence. The parameter values will be activated in the device.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Delivery flow rate must be sufficiently large**  Before activation of the parameter values, make sure that the delivery flow rate is sufficient at this instant.  This avoids unwanted tripping. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Tests performed by the device**  In SIMOCODE pro, the preconditions for the use of the function "dry-running protection" are checked during the teach-in. A check is made to see whether the following conditions are met:  - Progressive pump characteristic curve (P<sub>MIN</sub> / P<sub>OPT</sub> < 0.80) - Current in the permissible range (I<sub>U</sub> < I < I<sub>o</sub>) - Voltage in the permissible range (93 V < U < 794 V)   If one of the above conditions is not met, an error message is output. In this case you must  - close the dry-running protection wizard - eliminate the error and then restart the dry-running protection wizard.   Check the determined absolute values for P<sub>OPT</sub> and P<sub>MIN</sub> for plausibility irrespective of this (where applicable by comparing the pump characteristics). Determine the cause for obvious deviations before activating the dry-running protection function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Check after manual direct input of the trip level**  If you entered the trip level manually with the engineering software, check for the following conditions:  - the conditions for a sufficiently progressive pump characteristic curve - the conditions for sufficient distance from the dry-run state - the conditions for the permissible range of current and voltage. |  |

**Printing out the log file**

All dry-running protection settings are logged in the (offline) project. You can print them out together with the other device parameters. To do that, go offline, mark the device, and print out the log file.

## Configuring the communication interface

See also Chapter "Setting up or changing online connection". Confirm by pressing the F1 key and search for this chapter.

### Create new project

In the Project view, select "Project → New ...".

### Add new device

Double-click "Add new device" in the project navigation. The "Add new device" window opens.

- Select "SIRIUS Monitoring and Control Devices"
- Select the basic unit being used (pro C, pro S, pro V PB, pro V MR, pro V PN, pro V EIP)
- Select the basic unit version. The "Add new device" window opens.
- Activate the checkbox "Call device wizard" if you want to use the device wizard with selection of the use and the application
- When using the device wizard: Select the use for the device (Standard, PCS7 or Safety) and the application (control function).
- Click the "Finish" button.

> **Note**
>
> **Changing pre-configured applications**
>
> If you modify the pre-configured application, you may under certain circumstances have to modify many protective functions, links and interlocks again manually. You can select an application in the device wizard, and then receive a new SIMOCODE device with the corresponding sample configuration using the "Add new device" command.

### Select the station address in the device configuration (PROFIBUS DP)

The PROFIBUS station address of a node must be unique within a PROFIBUS-DP network. Select a unique address here.

A device with factory settings is generally assigned the address 126. Do not use this.

There are two options for setting:

- Via "Parameters → Fieldbus interface"
- Via "Properties → PROFIBUS Address"

### Activate/deactivate startup parameter block (PROFIBUS DP, PROFINET)

The startup parameter block prevents transfer of SIMOCODE pro parameters that can be transferred from the IO controller during startup.

Activate/deactivate the startup parameter block via the "Startup parameter block" checkbox under "Parameters → Fieldbus interface".

- Parameterization with SIMOCODE ES: The startup parameter block must always be set for this form of parameterization to avoid the device parameters from being overwritten by any existing parameter data during startup.
- Parameter data during startup: To enable device parameterization to be carried out during startup, the startup parameter block must not be set. SIMOCODE pro is then parameterized with the device-specific parameters stored in the DP master. Any parameters already in the device will be overwritten.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Inactive startup parameter block**  The startup parameter block is not active in the following cases:  - Device is as supplied - Following execution of the "Factory settings" command under "Commissioning → Command" |  |

### Select basic type (PROFIBUS DP, PROFINET)

SIMOCODE pro supports a number of I/O configurations which define the structure and length of the I/O data that is cyclically transferred between the IO controller (PLC) and the IO device (SIMOCODE pro). In the case of SIMOCODE pro, these configurations are termed basic types.

**Selection of basic type PROFIBUS DP**

Under "Parameters → Fieldbus interface", select the basic type (1 or 2).

You access the cyclic data in the PLC software via the inputs (send data) and the outputs (receive data). The length of the cyclic data which is to be transferred is set when SIMOCODE pro is integrated into the DP master system. This is achieved by selecting the basic type which in turn determines the structure and the length of the cyclic data.

The following basic types are available:

- Cyclic data from the PROFIBUS DP master to SIMOCODE pro: Basic type 1, 4 bytes of control data, basic type 2, 2 bytes of control data
- Cyclic data from SIMOCODE pro to the PROFIBUS DP master: Basic type 1, 10 bytes of message data, basic type 2, 4 bytes of message data

**Selection of basic type PROFINET**

Under "PROFINET parameters" select the basic type (1, 2 or 3).

The following basic types are available:

- Cyclic data to SIMOCODE pro V (PN): Basic type 1, 4 bytes, basic type 2, 2 bytes, basic type 3, 6 bytes
- Cyclic data from SIMOCODE pro V (PN): Basic type 1, 10 bytes, basic type 2, 4 bytes, basic type 3, 20 bytes

### Select module

Selection of the required modules in the catalog under "SIRIUS monitoring and control devices" by double-clicking or by dragging and dropping:

- Select the SIMOCODE pro basic unit. Double-click the selected SIMOCODE pro basic unit, or double-click "Device configuration" in the project navigation. The "Device configuration" window opens
- Select a current measuring module or a current / voltage measuring module
- Select the required digital modules (DM monostable, DM bistable, DM-F Local or DM-F PROFIsafe)
- Select an operator panel (OP) or an operator panel with display (OPD)
- Select the required expansion modules (analog module AM, ground-fault module EM, temperature module TM, multifunction module MM).

### Display firmware version

Select the chosen SIMOCODE pro basic unit. In the inspector window, the firmware version of the selected basic unit is displayed under "Properties → General → Catalog information".

### Upload the project data to the device

Select "Online → Load to device".

> **Note**
>
> A change of address is active immediately after downloading to the device!

### Load project data from device

Select "Online → Load from device (software)".

### Accessible devices

Under "Online → Accessible devices ..."

- select the type of the PG/PC interface (e.g. PROFIBUS, PN/IE or SIRIUS PtP)
- select the PG/PC interface.

### Extended loading to device

Under "Online → Extended loading to device", click on the "Start search" button. The compatible stations in the target subnet are displayed.

Select a station and click the "Load" button. The configuration is compiled. The "Load preview" window appears. Click "Load". The result of the load operation is shown at bottom right (e.g. load operation completed).

> **Note**
>
> This load operation is required every time a change is made to the device configuration.

> **Note**
>
> In this window, you can select the PG/PC interface type (e.g. PROFIBUS, PN/IE or SIRIUS PtP) and the PG/PC interface in the same way as in the "Online → Accessible devices" window.

### Go online

- Select "Online → Connect online" or click the "Connect online" button
- Select

  - the type of the PG/PC interface (e.g. PROFIBUS, PROFINET/Industrial Ethernet (PN/IE) or SIRIUS PtP)
  - the PG/PC interface
  - the connection with interface/subnet (PROFIBUS and PROFINET only)
  - the 1st gateway (PROFIBUS and PROFINET only)

| Settings | Communication interface |  |  |  |
| --- | --- | --- | --- | --- |
| Serial interface | PROFIBUS DP | PROFINET | EtherNet/IP |  |
| PG/PC interface type | SIRIUS PtP | PROFIBUS, PROFINET/Industrial Ethernet (PN/IE), TeleService |  |  |
| PG/PC interface | COM<x> | e.g. Intel(R) Centrino(R) Advanced-N 6205 |  |  |
| Connection with interface/subnet | - | From the drop-down list "Connection with interface/subnet", select the interface or the subnet for the connection. Select a direct connection if no S7 gateway is connected in between. Select the appropriate subnet for the connection to the PG/PC, if the device is accessible via an S7 gateway. Select the entry "Try all interfaces", if the device has several interfaces and you do not know which interface is used for connecting the device to the PG/PC.  If you have selected an MPI or Profibus subnet, the bus parameters that have been set are accepted into the PG/PC interface at this point. |  | - |
| 1st gateway | - | If the device is accessible via a gateway, select from the "1st Gateway" drop-down list the gateway which interconnects the subnets affected. |  | - |

- Click the "Start search" button. A search is made for compatible stations.
- Select a suitable station. You can show the following devices/stations:

  - devices with the same addresses
  - all compatible stations
  - accessible stations
- Click the "Connection..." button.

### Disconnecting the online connection

Select "Online → Disconnect online connection" or click the "Disconnect online connection" button.

### Adding a subnet

- Select the menu item "PROFIBUS address or Profinet interface → Ethernet addresses" in the inspector window under "General"
- Select "Not networked" as the subnet
- Click "Add new subnet".

### Displaying the available interfaces

The available interfaces are displayed under "Online accesses".

### Updating the accessible devices

Under "Online accesses", double-click "Update accessible devices".

### Acknowledging a flashing "GEN.FAULT" LED on the basic unit

When the "GEN.FAULT" LED on the basic unit flashes, press the "TEST/RESET" button on the basic unit. If this LED shows a continuous light, a specific waiting time is required until it goes out again.

This fault is also displayed under "Commissioning → Faults" (e.g. configuration error).

It is also possible to acknowledge a flashing "GEN.FAULT" LED via the "Commissioning → Control/status information" → "Reset" button.

## CFCs

This section contains information on the following topics:

- [Call CFC editor](#call-cfc-editor)
- [Overview - Toolbar - Menu commands](#overview---toolbar---menu-commands)
- [Select view](#select-view)
- [Move plan](#move-plan)
- [Switching the grid on/off](#switching-the-grid-onoff)
- [Set colors](#set-colors)
- [Selecting a function block or connection block and using it in the plan](#selecting-a-function-block-or-connection-block-and-using-it-in-the-plan)
- [Select all](#select-all)
- [Insert/remove/edit text field](#insertremoveedit-text-field)
- [Deleting objects and connections](#deleting-objects-and-connections)
- [Connecting function blocks.](#connecting-function-blocks)
- [CFC partitions](#cfc-partitions)
- [Monitoring](#monitoring)
- [Highlight signal flow](#highlight-signal-flow)
- [Position blocks according to data flow](#position-blocks-according-to-data-flow)
- [Show/hide unused connections](#showhide-unused-connections)
- [Transferring the online data to the hardware](#transferring-the-online-data-to-the-hardware)
- [Transferring the online data to the offline project](#transferring-the-online-data-to-the-offline-project)
- [Editing parameters](#editing-parameters)
- [Further information on CFCs](#further-information-on-cfcs)

### Call CFC editor

There are two methods of opening the CFC editor:

1. Go to the Project view and open your project. In the project navigation window, click on **"SIMOCODE → Charts →****Chart_1"** to open the CFC editor.
2. Alternatively, change to the **"Portal view** (lower left corner of the screen) **→ Control devices configuration → Chart_1**".

> **Note**
>
> **Starting the CFC editor with Professional or Basic license**
>
> The graphic editor is always installed.
>
> - With the Basic license, the fact that the license suitable for starting the CFC editor is not available is indicated.
> - The CFC editor can only be started with a Professional license.

### Overview - Toolbar - Menu commands

The following table shows the different Toolbar buttons and the associated commands:

| Button | Command |
| --- | --- |
| ![Figure](images/148925479307_DV_resource.Stream@PNG-de-DE.png) | Transfer online data to the hardware |
| ![Figure](images/148925488011_DV_resource.Stream@PNG-de-DE.png) | Transfer online data to the offline project |
| ![Figure](images/148925311371_DV_resource.Stream@PNG-de-DE.png) | Position blocks according to data flow |
| ![Figure](images/148925320331_DV_resource.Stream@PNG-de-DE.png) | Grid on/off |
| ![Figure](images/148925329291_DV_resource.Stream@PNG-de-DE.png) | Insert text field |
| ![Figure](images/148925457547_DV_resource.Stream@PNG-de-DE.png) | Highlight for signal flow |
| ![Figure](images/148925338251_DV_resource.Stream@PNG-de-DE.png) | View → Show all |
| ![Figure](images/148925347211_DV_resource.Stream@PNG-de-DE.png) | View → Zoom in |
| ![Figure](images/148925426315_DV_resource.Stream@PNG-de-DE.png) | View > Zoom dialog |
| ![Figure](images/148925381771_DV_resource.Stream@PNG-de-DE.png) | View → Zoom out |
| ![Figure](images/148925390731_DV_resource.Stream@PNG-de-DE.png) | Show/hide unused connections |
| ![Figure](images/148925399691_DV_resource.Stream@PNG-de-DE.png) | Monitoring On/Off |
| ![Figure](images/148925408395_DV_resource.Stream@PNG-de-DE.png) | Charts folder |
| ![Figure](images/148925417355_DV_resource.Stream@PNG-de-DE.png) | Start CFC editor |
| ![Figure](images/148925435275_DV_resource.Stream@PNG-de-DE.png) | Delete |
| ![Figure](images/148925496715_DV_resource.Stream@PNG-de-DE.png) | Add CFC partition |

### Select view

Select a button to structure the desired view of the chart.

Buttons:

![Figure](images/148925515147_DV_resource.Stream@PNG-de-DE.png)

Selection:

- Zoom in
- Show all
- Adapting the selection to the size of the work area
- Zoom out

### Move plan

The view of the chart can be moved up, down, to the right, and to the left using the scroll bars.

### Switching the grid on/off

Click on the ![Figure](images/148925320331_DV_resource.Stream@PNG-de-DE.png) "Grid on/off" button to switch the grid on/off in the chart. For manual optimization of the graphical display, objects are aligned with the grid or with other objects.

### Set colors

In the CFC, the interconnection lines are color-coded depending on the data type. Different color adaptations are possible. The colors can be modified later.

The colors are assigned to the interconnection lines using the menu command **"Options → Settings → General → Charts → CFC →** **General"**.

The data type of the data source is always relevant to the color shown. With interconnections to operands with undefined data type, the standard value "black" is used.

Define in the menu the colors of the interconnection lines for data type:

- Bool
- Byte
- Word / DWord
- Int / Dint
- Real
- Times

> **Note**
>
> **Changes in color assignment**
>
> Color assignments have an immediate effect on the display of the interconnection lines in an opened CFC.
>
> The color settings are stored and are available for further sessions. They apply for all projects.
>
> With the "Standard values" button, you restore the settings to the standard values.

### Selecting a function block or connection block and using it in the plan

You can drag & drop function blocks and blocks to the chart and then interconnect them.

The function blocks are stored hierarchically in the "Function blocks" folder.

The color of the symbol ![Figure](images/148925571723_DV_resource.Stream@PNG-de-DE.png) indicates whether the function block is already used in the chart (gray), or can be inserted in the chart (black).

Alternatively, you can transfer function blocks and blocks to the chart by double-clicking.

### Select all

You can select all function blocks, connections and comments with the menu command **"Edit" → Select all"**, or with the key combination "Ctrl +A".

Alternatively, you can draw a rectangle over all objects with the mouse.

The marked elements can then be moved or deleted.

### Insert/remove/edit text field

Click the ![Figure](images/148925329291_DV_resource.Stream@PNG-de-DE.png) button to insert a text field.

- Open a text frame at any point in the chart while holding the left mouse key pressed
- Left-click on the text field and enter your comment.

**Moving the text field**

- Select the text field
- Press and hold the left mouse button to position the text field to the desired location in the chart.

**Changing the size of the text field**

- Select the text field
- Press and hold the left mouse button to position the text field to the desired location in the chart.

**Copying and inserting a text field**

- Select the text field
- Press the right mouse button and select "Copy Ctrl.+C" in the shortcut menu
- Press the right mouse button and select "Insert Ctrl.+V" in the shortcut menu
- Press and hold the left mouse button to move the text field to the desired location in the chart.

**Edit text field**

- Click in the text field for write mode
- Enter, change or delete the text.

**Delete text field**

- Select the text field
- Press the right mouse button and select "Delete Del." in the shortcut menu.   
  Alternatively you can delete the selected text field with the "Del" key.

### Deleting objects and connections

Use the menu command **"Edit → Delete"** to delete one or more selected objects and connections.

Otherwise:

- Press the "Del" button
- Click the ![Figure](images/148925435275_DV_resource.Stream@PNG-de-DE.png) symbol
- Right mouse button **→** "Delete"
- Right mouse button **→** "Del" key

> **Note**
>
> By deleting an object, you delete all connections and open connections leading to this block.

### Connecting function blocks.

#### Drawing a connection

You can connect function block terminals with each other. To do so, proceed as follows:

| Step | Description |
| --- | --- |
| 1 | Move the cursor over an unconnected input. It is then highlighted. |
| 2 | - Press the left mouse button and keep it pressed. - Keep the mouse button pressed and draw a connection to the output until it is highlighted in blue. |
| 3 | Release the mouse button. |
| 4 | A connection is established between the two terminals.   **Note:**   You can also draw the connection from the output to the input. |

#### Drawing a connection to several charts

You can connect the function blocks of several charts with each other. To do so, proceed as follows:

| Step | Description |
| --- | --- |
| 1 | Open all charts to which you want to draw connections. The opened charts are visible as a button in the lower menu bar. You can switch between the individual charts with a click. |
| 2 | Move the cursor over an unconnected input (e.g. in Chart 1). It is then highlighted. |
| 3 | Connecting using drag and drop:  - Press the left mouse button and keep it pressed. - Keep the mouse button pressed and drag the cursor to the button of the desired chart (e.g. Chart 2). - The second chart opens. - Keep the mouse button pressed and drag the cursor to the output of the block in Chart 2. The connection is highlighted in blue.   Connection via the shortcut menu:  - with "Interconnection to operand...":   - Click on the button with the triangle symbol. The "Picker" window opens. All elements from the catalog of function blocks and blocks are offered for selection, regardless of whether or not an element is already being used in a chart.   - To confirm, click on the button with the green check mark. - with "Interconnection to chart...":   - Click on the button with the triangle symbol. The "Picker" window opens. Only those function blocks and blocks that are already used in a created chart are offered for selection.   - To confirm, click on the button with the green check mark. |
| 4 | Release the mouse button. |
| 5 | The link between the connection in Chart 1 and the connection in Chart 2 is established.   **Note:**   - You can also draw the connection from the output to the input. - If you have opened two charts next to each other, you can link the connection of Chart 1 with the connection of the opened Chart 2 while holding the mouse button pressed. |

The connections and signals between several charts are shown by means of cross-references.

****Example: Chart 1 with "Cyclic send" block byte 0, Chart 2 with "BU outputs" block****

If a connection is established between bit 0.7 (cyclic send, byte 0) and output 1 (BU output), the cross-references are shown as follows:

- Cross-reference Chart1: \Chart_2\BU_outputs_1.output 1
- Cross-reference Chart2: \Chart_1\cyclic send byte0_1.bit7.

Connecting function blocks using auto completion: See below.

#### Connecting function blocks using auto completion

You can also connect two function blocks to each other by manually entering the name of the function block to be connected. To do so, move the mouse pointer to a connection (input or output) until it is active (blue background). Right-click and select the "Interconnect with" function. An editing field opens in which you can enter the name of the function block to be connected, either manually or with the help of an auto-complete function. Alternatively, you can also select an input or output from a list of suitable connections using the button to the right of the editing field (Object Picker).

To connect function blocks from different charts (e.g. Chart 1 and Chart 2), enter a "P" in the editing field and select the other chart. Enter an additional backslash (\) and in this case all the suitable connections (inputs or outputs) from Chart 2 are displayed. Alternatively, you also select an input or output from a list of suitable connections of the other chart using the Object Picker.

You can find detailed help for connecting function blocks in the information system under "Configuring technologically"→ Configuring CFCs → Configuring and adapting CFCs → Configuring and interconnecting input and output parameters".

#### Rules for drawing connections:

- Several connections can originate from one output.
- Only one connection can be connected to one input.
- Binary outputs can only be connected to binary inputs, and analog outputs can only be connected to analog inputs.

#### Selecting the function block or connection

You can use the mouse to select both function blocks and connections. Multiple selections are possible by clicking on multiple elements with the mouse and holding down the Ctrl key.

#### Moving the function block or connection

Keep the mouse button pressed to move function blocks and connections. When function blocks are moved, the start and end points of connections are fixed, since they are linked to the terminals of function blocks.

#### Deleting the function block or connection

If you delete function blocks, all connections emanating from the function block will also be deleted. Deleting a function block means it will not be used in the current chart; in other words, all inputs and outputs of the function block are not connected.

### CFC partitions

#### Splitting into chart partitions when using earlier CFCs

In earlier CFCs with 6 or fewer sheets, a single chart partition is created that contains the complete contents of the chart. The layout settings remain unchanged for these charts.

In earlier CFCs with more than 6 sheets (maximum: 20) the content of these sheets is split during conversion into several chart partitions (3x2 sheets per chart partition). The first 6 sheets (from left to right and from top to bottom) are moved into the first partition. The next 6 sheets are moved into the next partition, and so on.

#### Display of chart partitions

The data flow view of the CFC Editor shows one chart partition at a time. The name of the current chart partition is shown in a selection box. The names of the chart partitions are listed there in alphabetic order.

As long as a CFC editor window is open, the last scroll bar position and the last zoom setting are saved.

The first time a CFC is opened in a session, Partition_1 is displayed. After closing and reopening the same CFC, the last opened partition is displayed.

The signal flow view of a CFC is not affected by chart partitions.

The signal flow view shows the execution sequence of all blocks of a CFC. The execution sequence can be edited as before, regardless of the chart partitions.

#### Adding a chart partition

By default, each new CFC is created with a single chart partition.

Insert partitions using the "Add partition" icon (![Adding a chart partition](images/148925496715_DV_resource.Stream@PNG-de-DE.png)). Each CFC can have as many as 6 chart partitions.

#### Configuring the chart layout in a chart partition

Set the chart layout using the Properties window of the CFC.

The layout settings apply uniformly to all chart partitions of the CFC. Individual settings for individual partitions are not possible.

Each chart partition can have up to 6 sheets, i.e. one CFC can contain up to 36 sheets.

#### Adding function blocks and text fields in a chart partition

You can copy and move existing function blocks and text fields in a CFC from one partition to another using the "Copy" and "Cut" options.

In "No sheet bars" mode, you can only move free connectors within the same partition.

When you add function blocks to a CFC via the signal flow view, they are automatically positioned and inserted into the first partition.

#### Connecting function blocks between chart partitions

To create a connection between different chart partitions of a CFC, proceed as follows:

- Click on the source pin
- Switch to connection mode.
- Switch to the target chart partition.
- Complete the connection in the target chart partition

Alternatively, you can use the object selection. The object selection lists all function blocks of a chart, regardless of chart partitions.

An interconnection is displayed in the Properties window under "General → Interconnection" with source and target of the interconnection when the interconnection is selected (blue highlighting).

#### Navigation with sheet bar connectors

When you double-click on a sheet bar connector (or a free connector in "No sheet bar connectors" mode), the target chart partition opens and the connection target is selected.

If the connection target is in another chart or chart partition, the partition name and sheet number of the target are displayed in the connector (write-protected).

The sheets are numbered consecutively (1 ... 6) from left to right and top to bottom

#### Navigation using the quick overview

Double-click on any point in the background of the chart partition.

If the chart is not in the "Fit to screen" zoom mode, the chart will be adjusted to the size of the work area. Another double-click on any sheet also zooms the chart partition to 100 % while scrolling to the selected sheet.

#### Renaming a chart partition

In the signal flow view, the name of the displayed chart partition is shown in the Properties window under "Displayed chart partition". In this view you can rename the current chart partition. The maximum length is 15 characters. The names are not multilingual. They must be unique within a CFC.

#### Deleting a chart partition

Remove partitions by means of the "Delete" icon (![Deleting a chart partition](images/148925626123_DV_resource.Stream@PNG-de-DE.png)). All elements of this partition are then deleted.

When a partition is deleted, a new empty partition is automatically created.

### Monitoring

With the "Monitoring" function, you can monitor the inputs and outputs of function blocks online.

- Change to **"Project navigation → Devices → SIMOCODE_1 → Charts → Chart_1"**.
- Click the ![Figure](images/148925399691_DV_resource.Stream@PNG-de-DE.png) "Monitoring on/off" button to switch the function on. The objects interconnected in the chart are monitored online according to their settings and specifications. Display of the connecting lines:

  - Connecting lines of logic values are shown in light green ("TRUE") throughout.
  - Blue broken connecting lines are "FALSE".
- Set the properties for **"General"** and **"Parameters"** for monitoring in the inspector window. Selection by activating checkboxes.
- Select individual inputs, outputs or objects.
- In the shortcut menu, select "For Test" to monitor the connection or the object. The value of the connection is displayed next to the connection
- Click the ![Figure](images/148925399691_DV_resource.Stream@PNG-de-DE.png) "Monitoring on/off" button to switch the function off.

### Highlight signal flow

Click the ![Figure](images/148925457547_DV_resource.Stream@PNG-de-DE.png) button to highlight the signal flow.

The following objects are indicated in color:

- All blocks and connections that indirectly send signals to an input of the selected block (signal flow on the input side)
- All blocks and connections to which the signals of all outputs of the selected block are sent directly or indirectly (signal flow on the output side).

Display of the signal flow deactivates following:

- Selection of another function block in the chart
- Deletion of a function block in the highlighted chart
- Selection or deletion of a connection
- Click the ![Figure](images/148925457547_DV_resource.Stream@PNG-de-DE.png) button.

### Position blocks according to data flow

Click on the ![Figure](images/148925311371_DV_resource.Stream@PNG-de-DE.png) "Position blocks according to data flow" button in the graphic editor. The function blocks and connections arrange themselves automatically. This function is also executed when the CFC editor is first called if there is existing parameterization.

The following rules are observed when automatically arranging function blocks and connections:

- No overlapping of function blocks.
- Function blocks are displayed in a regular column grid
- Function blocks containing exclusively outputs are placed in the column on the extreme left
- Function blocks containing exclusively inputs are placed in the column on the extreme right
- Function blocks with inputs and outputs are arranged so as to result in minimum feedback
- By using the three last-named rules, a signal flow from left to right is achieved
- The page layout is automatically adapted. The required number of pages is set automatically. It is also guaranteed that no function blocks are positioned on page margins.

### Show/hide unused connections

Click on the ![Figure](images/148925390731_DV_resource.Stream@PNG-de-DE.png) "Show/hide unused connections" button. All unused connections are hidden. A second click on the button shows the connections again.

### Transferring the online data to the hardware

Click on the ![Figure](images/148925479307_DV_resource.Stream@PNG-de-DE.png) button to transfer the online data to the hardware.

> **Note**
>
> **Parameterization changes**
>
> In test mode, changes in the input/output parameters of the blocks and instructions are transferred directly to the device and also adopted into the project.
>
> Such changes do not necessitate renewed loading.

### Transferring the online data to the offline project

Click on the ![Figure](images/148925488011_DV_resource.Stream@PNG-de-DE.png) button to transfer the online data to the offline project.

During commissioning or when testing a CFC, it is possible to execute and test different parameter changes online in the device.

When these changes have been successfully tested, they can be read back to the offline program.

> **Note**
>
> **Reading back parameterization changes**
>
> Prerequisites:
>
> - Online mode is activated.
> - Parameter changes were made in online mode.

### Editing parameters

You can edit some input parameters of a function block directly in the function block itself. You no longer have to switch to the parameter editor or to the inspector window.

Double-click the relevant text field. The entry has a blue background. Replace the current value with a new value.

The values provided for selection can be modified via list boxes.

Other values are analyzed and converted for the relevant data type.

Default values are displayed in gray, modified values are displayed in blue.

### Further information on CFCs

You can find more information in the information system under [Configuring and adapting CFC charts](Configuring%20CFC%20charts.md#configuring-and-adapting-cfc-charts).

## Migrating project files, upgrading a SIMOCODE pro project

This section contains information on the following topics:

- [Migrating project files](#migrating-project-files)
- [Upgrading a SIMOCODE pro project](#upgrading-a-simocode-pro-project)

### Migrating project files

Project files can be migrated from SIRIUS ES classic (Version 2007 and higher) . The project data is converted to a TIA project. The converted project data can be further processed in the SIRIUS ES Client.

Migration of classic project files for a device (sdp files) as well as migration of group files (grp files) are supported.

The migration can take place in two different ways:

- In the Portal view using the menu item "Migrate project"
- In the Project view using the command "Project → Migrate project".

A "Migrate project" window opens.

- Select a project name and a destination path under "Destination"
- Assign a name for the author (optional)
- Enter a comment (optional)
- Click on the Selection button (...) in the "Source path" line. The window "Open a project you would like to migrate" opens.
- Select either a SIR​IUS Engineering project file (*.sdp file SIRIUS ES classic) or a SIRIUS Engineering group file (*.grp file). If you select a grp file, the associated sdp files are read out.
- Click on the "Migrate" button.

A new project is always created.

> **Note**
>
> - Direct import to an existing TIA project is not possible.
> - Information on progress and status is displayed during the migration.
> - On completion of the migration, you will find the information "Migration successfully finished" in the inspector window.
> - If the device to be migrated is not supported in the TIA Client, information is displayed in the inspector window and the migration is canceled.
> - If, for example, a specific module is not supported for the SIMOCODE header module, only this component is not migrated. All other supported modules are migrated. Information is displayed.

You will also find further information in Industry Online Support: [Migrating projects in a TIA portal project.](http://support.automation.siemens.com/WW/view/en/56314959)

### Upgrading a SIMOCODE pro project

If you open a project created in a previous version of SIMOCODE ES it will be upgraded with user guidance.

You must then

- close any previously opened editors (device configuration, parameters, commissioning)
- update the module description for every module. See [Updating the module description](#updating-the-module-description).

## Mass engineering

You can transfer the parameter values of one device to other devices in the same project using the "Mass Engineering" button, i.e. you can combine these devices into a group.

- In the expert list menu bar, click the "Mass Engineering" button. The "Mass Engineering with Parameter Source ..." window opens. All configured and compatible SIMOCODE devices in your currently open project are listed in this window.
- Using the check box, select the devices to which you want to transfer the parameter values. The current device (source) and the marked target devices together form a single group.
- Using a list box, select which parameter values you wish to transfer to other devices:

  - The values of all parameters
  - The values of all favorites parameters
  - The values of all parameters that are not favorites
- As soon as you have configured a new group using the checkbox, we recommend saving them with the "Save" button. In addition, all currently defined and saved groups are saved for every device in the project.
- The group definitions that you saved for each device are loaded when you open a project.
- Click the "Copy" button. A window "Status Mass Engineering" opens, in which you can see how the mass engineering process is progressing

> **Note**
>
> **Write-protected parameters**
>
> Write-protected parameters in the target device cannot be transferred to the target device.

> **Note**
>
> **Restrictions regarding group membership**
>
> Currently, a device can only belong to one group. Therefore, if you have added a device to a group, you cannot subsequently add it to another group.
>
> Example: A group consists of 4 devices. Devices 1 and 2 have been combined into a single group.
>
> In this case, it is not possible to access device 1 or 2 from device 3 or 4 using the mass engineering function.

The result of the mass engineering action is displayed in the inspector window after the copy command has been executed. Once all the parameters have been successfully copied to every device, the message "Mass engineering completed" is displayed.

However, if one or more parameters was not successfully copied, the failed copy actions are listed together with the parameter name, date, and time.

## Taking over the standard connection path of SIRIUS PROFINET & Ethernet/IP devices in the project

### Objective

You can define a shared online access for multiple PROFINET (PN) and EtherNet/IP (EIP) devices. The online access defines the PG/PC interface to be used for online connections to the device in question.

### Requirements

- A project has been set up.
- At least one PN and/or EIP device is present in the project.

### Procedure

1. Select "Online > Accessible nodes" in the menu. A dialog box opens.
2. Set "PN/IE" as the type of PG/PC interface.
3. Select the required "PG/PC interface" from your local system.
4. With the "Apply standard connection path to all SIRIUS devices" button, you apply the setting to the Ethernet-based devices in your project.

### Result

After taking over the line accesses, you can also go online to multiple Ethernet-based SIRIUS devices or download the parameter settings.

In the inspector window, the message "Selected default connection path settings has been applied to following devices" is displayed.

### More information

You will find more detailed information in the following help topics:

[PROFINET parameters](#profinet-parameters)

[Ethernet IP parameters](#ethernet-ip-parameters)

[Configuring the communication interface](#configuring-the-communication-interface)

## Importing and exporting parameters

### Activating the add-in for exporting and importing parameters

The add-in for exporting and importing parameters is activated as follows:

- In the toolbar on the right, click on "Add-Ins". The "Add-Ins" window opens. "SimocodeExportImport.addin" is displayed.
- Via the shortcut menu, select "Activate".
- Following activation, a green checkmark appears in the status area. In the drop-down list, activate or deactivate the add-in
- By clicking on "Details", the following information is displayed:

  - Name of the add-in
  - Storage path of the add-in
  - Author of the add-in
  - Date and time of last change
  - Product label of the add-in (SIMOCODE ES)
  - Version of the add-in
  - Status. In the drop-down list, activate or deactivate the add-in
  - Issued by: Indicates the issuer of the certificate with which the add-in is signed
  - Display certificate: TIA Add-in for Simocode export/import parameters

### Export/import parameter wizard

You can open the wizard for exporting or importing SIMOCODE parameters as follows:

- In the project navigation:

  - In the project navigation, Select project → Shortcut menu → Export/Import Simocode device parameters → Export or Import
  - In the project navigation, Select device → Shortcut menu → Export/Import Simocode device parameters → Export or Import
- In the "Devices and Networks" view:

  - Select a Device → Shortcut menu → Shortcut menu → Export/Import Simocode device parameters → Export or Import

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Restrictions**  - If there is no SIMOCODE device in a project, the export/import parameter wizard is disabled. - For combined products, the export/import parameter wizard is active in the shortcut menus in each case. - The export/import parameter wizard is not available for STEP7 integration. - The export/import parameter wizard is only available in the offline engineering status "Offline". In the online engineering status the export/import parameter wizard is deactivated. |  |

**Export parameter wizard**

The export parameter wizard dialog includes the following operator control and display elements:

- A selection area for the devices
- A selection window for the folder path
- An "Export" button
- A "Select All" button and a "Deselect All" button
- A log area
- A "Close" button

A device list is displayed containing all devices in one project. You can select single or multiple devices for exporting your parameters. Using the "Select all" and "Deselect all" buttons, you can apply the selection or deselection to all devices.

You can select single or multiple devices. By pressing the "Select all" button you select all devices, by pressing the "Deselect all" button you deselect all devices.

In the "Folder path" field, specify the storage location for the files to be exported. The following path is pre-set: "Siemens Automation File Path". Click "..." to specify an individual directory. Another directory with the project name is created in this directory when the export is started.

Start the export by clicking the "Export" button. For each device to be exported, a csv file with the device name is created in the directory with the project name.

Write-protected parameters are identified accordingly.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Restrictions**  Safety-related parameters are not exported. |  |

If the export was successful, the message "Export was successful" appears in the "Logs" area, as well as a "Log file" link, which opens a txt file. This txt file is likewise stored in the same folder as the csv file.

Click on the "Close" button to exit the export parameter wizard.

**Import parameter wizard**

The import parameter wizard dialog includes the following operator control and display elements:

- A selection area for the files to be imported
- An area containing the names of the devices to be imported
- A setting range
- An "Import" button
- A log area
- A "Close" button

You can use the "Add file" button to import a single or multiple csv files. After the files to be imported have been selected, they are listed. You can import csv files from various different storage locations.

Using the "Remove" and "Remove All" buttons you can remove individual or all csv files from the file selection area.

The devices are displayed in the device list area.

The device names are generated from the csv file names. If there are conflicts concerning the device names, these devices will be marked in red and the "Import" button will be disabled.

Settings of the import parameter wizard:

- Network settings
- Device configuration

You can activate and deactivate these settings by means of checkboxes (Default: Activated).

Start the import by clicking the "Import" button. All parameters (except write-protected) of the selected devices are imported into the existing devices. The import process can only be executed for devices that already exist. When the import process has been completed, a corresponding message is displayed.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Restrictions**  - The firmware version of the existing devices must be equal to or higher than the firmware version of the devices whose files are imported. - If there are configuration differences between devices, the import process is not carried out. - Inconsistent files are not imported. In the event of inconsistencies the import process is aborted. Detailed information on these files is displayed in the log area. For example, if there are two files, one consistent and the other inconsistent, only the consistent file is imported completely, while the inconsistent file is not imported completely. - Safety-related parameters are not imported. |  |

If the import was successful, the message "Import was successful" appears in the "Logs" area, as well as a "Log file" link, which opens a txt file. This txt file is likewise stored in the same folder as the csv file.

Click on the "Close" button to exit the import parameter wizard.

## Device comparison with the TIA Portal comparison editor

This section contains information on the following topics:

- [Offline/offline comparison](#offlineoffline-comparison)

### Offline/offline comparison

#### Objective

You can compare two SIRIUS devices with identical article numbers.

This provides you with a clear comparison of the device configuration and the device parameters and you can see at a glance what the differences are.

#### Requirements

- A project is open.
- At least 2 devices contain an identical article number.

#### Procedure

1. In the project navigation, select a device that you want to compare.
2. Run the command "Compare > Offline/Offline" via the shortcut menu **or** via "Tools" on the menu bar
3. The comparison editor opens and the selected device is displayed in the left-hand area.
4. Drag a further device into the drop area "Drag the comparison object here..." in the right-hand area.

   - Click on the "Start detailed comparison" button **or**
   - Double-click the green status icon in the middle of the window "Detailed hardware comparison" **or**
   - Select a device and start the detailed comparison via the shortcut menu.

   The following table shows an overview of the icons used in the comparison editor. You will find a detailed description in the tooltips of the user interface.

   | Symbol | Meaning |
   | --- | --- |
   | ![Procedure](images/162077086859_DV_resource.Stream@PNG-de-DE.png) | Refresh display |
   | ![Procedure](images/162077095435_DV_resource.Stream@PNG-de-DE.png) | Start detailed comparison |
   | ![Procedure](images/162096688011_DV_resource.Stream@PNG-de-DE.png) | Display non-hierarchically |
   | ![Procedure](images/162097067787_DV_resource.Stream@PNG-de-DE.png) | Question mark symbol |
   | ![Procedure](images/162097076363_DV_resource.Stream@PNG-de-DE.png) | Filtered (this comparison criterion is deactivated) |
   | ![Procedure](images/162100118539_DV_resource.Stream@PNG-de-DE.png) | Display hierarchically |
   | ![Procedure](images/162101023115_DV_resource.Stream@PNG-de-DE.png) | Display identical and different objects |
   | ![Procedure](images/162101031691_DV_resource.Stream@PNG-de-DE.png) | Display only different objects |
   | ![Procedure](images/162102013067_DV_resource.Stream@PNG-de-DE.png) | Objects are identical |
   | ![Procedure](images/162102456843_DV_resource.Stream@PNG-de-DE.png) | Objects are different |
   | ![Procedure](images/162102465419_DV_resource.Stream@PNG-de-DE.png) | Display available assignment criteria |
   | ![Procedure](images/162102857995_DV_resource.Stream@PNG-de-DE.png) | Back |
   | ![Procedure](images/162103096971_DV_resource.Stream@PNG-de-DE.png) | Switch between automatic and manual comparison |

#### Result

A further window is opened in which the parameters of the two devices are listed.

From the status icons in the central area, you can see what the differences are: Expand the relevant groups until you can see the settings that are different.

The "Detailed hardware comparison" window contains a one-to-one comparison of the device configuration and parameters of each device. In this window, you can click on the black triangle icon to list the device configuration and all parameters, or click on the "Display only objects with differences" icon to list only those parameters that differ by value.

You can update the comparison results by clicking on the "Refresh display" icon on the toolbar.

If you want to change the assignment criterion, click on the arrow of the "Display available assignment criteria" button on the toolbar. Then select the assignment criterion that you want to use.

If you want to perform a manual comparison, click above the status area on the "Switch between automatic and manual comparison" button. Then select the objects that you want to compare.

#### More information

If you want to display the differences between values at different storage locations, you can display the differences using the parameter comparer ([Parameter comparer](#parameter-comparer)).

## Default print settings

In the main menu bar, select "Project" and then "SIMOCODE pro Print Settings". The "SIMOCODE pro Print Settings" window opens.

> **Note**
>
> The print settings relate directly to compact printing (see "Project → Print" dialog).

> **Note**
>
> It is also possible to open the SIMOCODE pro print settings and carry out changes in the online status.
>
> However, printing is not possible in the online status.

> **Note**
>
> The "SIMOCODE pro Print Settings" setting is only visible if a SIMOCODE device is configured in the project (displayed in the device configuration) and a module is selected.

Select one of the following options: "Adapt for all device types" or "Adapt for specific device types".

By activating the "Adapt for specific device types" option button, you can select one device type from the following:

- SIMOCODE pro C (default)
- SIMOCODE pro S
- SIMOCODE pro V PB
- SIMOCODE pro V EIP
- SIMOCODE pro V MR
- SIMOCODE pro V PN
- SIMOCODE pro V PN GP

The selection area for parameter categories is updated according to the selected device type.

In the "Parameters" window, select those parameters that you would like to print.

All parameters can be selected and deselected using the "Select All" and "Deselect All" buttons.

If a user-specific setting has already been made, the last setting to be made appears when the window is opened.

Clicking on the "Apply" button saves the current settings.

Clicking the "OK" button saves the current settings and closes the "SIMOCODE pro Print Settings" window.

When the settings are saved, the message "Changes to SIMOCODE pro Print Settings were successfully saved" appears in the inspector window. The configuration is saved in a log file and remains in the offline project.

If you exit the "SIMOCODE pro Print Settings" window using the "Cancel" button without saving, a pop-up message appears with the following information text: "The SIMOCODE print settings have been modified. You have made some changes. Do you want to save them?".

If you click "Yes", the settings you have made are saved and this window closes. The message "Changes to SIMOCODE pro Print Settings were successfully saved" appears in the inspector window.

If you click the "No" button, the changes are not saved and the window closes. The message "Unsaved changes to SIMOCODE pro print settings will be discarded" appears in the inspector window.

Click the "Cancel" button or the "Close window (X)" symbol if you would like to close the "Print settings" window.

## Additional information

This section contains information on the following topics:

- [Service](#service)
- [Examples](#examples)

### Service

This section contains information on the following topics:

- [Upgrading a SIMOCODE pro project](#upgrading-a-simocode-pro-project-1)
- [Active control stations, contactor controls and lamp controls](#active-control-stations-contactor-controls-and-lamp-controls)
- [Diagnostics via LED display](#diagnostics-via-led-display)
- [Restoring factory settings](#restoring-factory-settings)
- [Setting the PROFIBUS station address](#setting-the-profibus-station-address)
- [Setting IP parameters and PROFINET device name](#setting-ip-parameters-and-profinet-device-name)
- [Setting IP parameters and EIP device name](#setting-ip-parameters-and-eip-device-name)
- [Backing up and saving parameters](#backing-up-and-saving-parameters)
- [Configuring the diagnostics response](#configuring-the-diagnostics-response)
- [Setting the safety relay functions](#setting-the-safety-relay-functions)
- [Replacing SIMOCODE pro components](#replacing-simocode-pro-components)
- [Data sets](#data-sets)

#### Upgrading a SIMOCODE pro project

If you open a project created in a previous version of SIMOCODE ES it will be upgraded with user guidance.

You must then

- close any previously opened editors (device configuration, parameters, commissioning)
- update the module description for every module. See [Updating the module description](#updating-the-module-description).

#### Active control stations, contactor controls and lamp controls

See [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951).

#### Diagnostics via LED display

##### Diagnostics via LED display on the basic unit and on the operator panel (PROFIBUS)

The basic units and the operating panel have three LEDs for displaying specific device states:

| LED | Status | Display | Description | Corrective measures for faults |
| --- | --- | --- | --- | --- |
| Device | Device status | Green | Device ON | — |
| Green – flickering | Internal error | Send back the basic unit |  |  |
| Yellow | Memory module or addressing plug recognized, TEST/RESET buttons control the memory module or addressing plug | — |  |  |
| Yellow flashing | Memory module/addressing plug read in; factory settings configured   (duration: 3 s) | — |  |  |
| Yellow – flickering | Memory module programmed  (duration: 3 s) | — |  |  |
| Red | Incorrect parameterization (also GEN. FAULT on) | Parameterize again and switch the control voltage off and on again |  |  |
|  | Basic unit defective (also GEN. FAULT on) | Replace the basic unit! |  |  |
| Red flashing | Memory module, addressing plug or expansion modules defective (also GEN. FAULT on - flashing) | Reprogram/replace the memory module, replace the expansion modules |  |  |
| Off | Supply voltage too low | Check whether the supply voltage is connected/switched on |  |  |
| Bus | Bus status | Off | Bus not connected or bus fault | Connect the bus or check bus parameters |
| Green flashing | Baud rate recognized / communication with PC / programming device | — |  |  |
| Green | Communication with PLC/PCS | — |  |  |
| GEN. FAULT | Fault status | Red | Fault pending; reset has been saved | Rectify fault, e.g. overload |
| Red flashing | Fault pending; reset has not been saved | Rectify fault, e.g. overload |  |  |
| Off | No error | — |  |  |

##### Diagnostics via LED display on the basic unit and on the operator panel (PROFINET)

The basic unit and the operating panel have LEDs for displaying specific device states:

| LED | Status | Display | Description | Corrective measures for faults |
| --- | --- | --- | --- | --- |
| Device | Device status | Green | Device ON | - |
| Green flickering | Internal error | Send back the basic unit |  |  |
| Yellow | Memory module recognized, TEST/RESET buttons control the memory module | — |  |  |
| Yellow flashing | Memory module read in; factory settings configured (duration: 3 s) | — |  |  |
| Yellow flickering | Memory module programmed  (duration: 3 s) | — |  |  |
| Red | Device defective (also GEN. FAULT on) | Replace the basic unit! |  |  |
| Red flashing | Memory module or expansion modules defective (also GEN. FAULT on - flashing) | Reprogram/replace the memory module, replace the expansion modules |  |  |
| Off | Supply voltage too low | Check whether the supply voltage is connected/switched on |  |  |
| Green flashing | PE energy saving mode active | — |  |  |
| Bus | Bus status | Off | No communication with the IO Controller of the PLC/PCS | Connect the bus or check parameters (IP parameters, device name) |
| Green | Communication with the IO Controller of the PLC/PCS is active | — |  |  |
| GEN. FAULT | Fault status | Red | Fault pending; reset has been saved | Rectify fault, e.g. overload |
| Flashing red | Fault pending; reset has not been saved | — |  |  |
| Off | No error | — |  |  |
| PORT1 (only on basic unit) | Bus status | Green | Ethernet connection available | — |
| Off | No Ethernet connection available | Check the Ethernet connection and the wiring |  |  |
| Flashing | Station flash test for device location active | — |  |  |
| PORT2 (only on basic unit) | Bus status | Green | Ethernet connection available | — |
| Off | No Ethernet connection available | Check the Ethernet connection and the wiring |  |  |
| Flashing | Station flash test for device location active | — |  |  |

##### Diagnostics via LED display on the basic unit and on the operator panel (EtherNet/IP)

The basic unit and the operating panel have LEDs for displaying specific device states:

| LED | Status | Display | Description | Corrective measures for faults |
| --- | --- | --- | --- | --- |
| Device | Device status | Green | Device ON | _ |
| Green flickering | Internal fault | Send back the basic unit! |  |  |
| Yellow | Memory module recognized, TEST/RESET buttons control the memory module | _ |  |  |
| Yellow flashing | Memory module read in; factory settings configured (duration: 3 s) | _ |  |  |
| Yellow flickering | Memory module programmed (duration: 3 s) | _ |  |  |
| Red | Device defective (also GEN. FAULT on) | Replace the basic unit! |  |  |
| Red flashing | Memory module or expansion modules defective (also GEN. FAULT on - flashing) | Reprogram/replace the memory module, replace the expansion modules |  |  |
| Off | Supply voltage too low | Check whether the supply voltage is connected/switched on |  |  |
| Green flashing | PE energy saving mode active | _ |  |  |
| Bus | Bus status | Off | No communication with a controller active | Connect the bus or check Ethernet parameters (IP parameters, device name) |
| Green flashing | Communication with a controller active (e.g. Rockwell Automation controller) | _ |  |  |
| GEN. FAULT | Fault status | Red | Fault pending; reset has been saved | Rectify fault, e.g. overload |
| Flashing red | Fault pending; reset has not been saved | _ |  |  |
| Off | No error | _ |  |  |
| PORT1 (only on basic unit) | Bus status | Green | Ethernet connection available | _ |
| Off | No Ethernet connection available | Check the Ethernet connection and the wiring |  |  |
| Flashing | Station flash test for device location active | _ |  |  |
| PORT2 (only on basic unit) | Bus status | Green | Ethernet connection available | _ |
| Off | No Ethernet connection available | Check the Ethernet connection and the wiring |  |  |
| Flashing | Station flash test for device location active | _ |  |  |

##### Diagnostics via LEDs on DM-F Local

The DM-F Local has more than 10 LEDs that display specific device states:

| LED display | Color | Meaning |
| --- | --- | --- |
| READY | OFF  Green  Green flashing | System interface not connected/supply voltage too low/device defective  Device ON/system interface OK  Device ON/system interface not active or not OK |
| DEVICE | OFF  Green  Green flashing  Yellow  Yellow flashing  Red | Supply voltage too low  Device ON  Self-test  Configuration mode  Error in configuration  Device defective or faulty |
| OUT | OFF  Green  Green flashing | Safety-related output not active  Safety-related output active  Feedback circuit not closed although start condition satisfied |
| IN | OFF  Green  Green flashing | Input not active  Input active  Fault detected (e.g. cross-circuit at input, sensor simultaneity not fulfilled) |
| 1 | OFF  Yellow  Yellow flashing  Yellow flickering | Cross-circuit detection off  Cross-circuit detection ON  Configuration mode, waiting for confirmation  Error in configuration |
| 2 | OFF  Yellow  Yellow flashing  Yellow flickering | NC contact/NO contact  NC contact/NC contact  Configuration mode, waiting for confirmation  Error in configuration |
| 3 | OFF  Yellow  Yellow flashing  Yellow flickering | 2 x single-channel  1 x two-channel  Configuration mode, waiting for confirmation  Error in configuration |
| 4 | OFF  Yellow  Yellow flashing  Yellow flickering | Debouncing time Y12, Y22, Y34 approx. 50 ms  Debouncing time Y12, Y22, Y34 approx. 10 ms  Configuration mode, waiting for confirmation  Error in configuration |
| 5 | OFF  Yellow  Yellow flashing  Yellow flickering | Sensor circuit, automatic start  Sensor circuit, monitored start  Configuration mode, waiting for confirmation  Error in configuration |
| 6 | OFF  Yellow  Yellow flashing  Yellow flickering | Cascading input 1, automatic start  Cascading input 1, monitored start  Configuration mode, waiting for confirmation  Error in configuration |
| 7 | OFF  Yellow  Yellow flashing  Yellow flickering | With start-up testing  Without start-up testing  Configuration mode, waiting for confirmation  Error in configuration |
| 8 | OFF  Yellow  Yellow flashing  Yellow flickering | Automatic starting after power failure  No automatic starting after power failure  Configuration mode, waiting for confirmation  Error in configuration |

##### Diagnostics via LEDs on DM-F PROFIsafe

The DM-F PROFIsafe has more than 10 LEDs that display specific device states:

| LED display | Color | Meaning |
| --- | --- | --- |
| READY | OFF  Green  Green flashing | System interface not connected/supply voltage too low/device defective  Device ON/system interface OK  Device ON/system interface not active or not OK |
| DEVICE | OFF  Green  Green flashing  Red | Supply voltage too low  Device ON  Self-test  Device defective or faulty |
| OUT | OFF  Green  Green flashing | Safety-related output not active  Safety-related output active  Feedback circuit not closed although start condition satisfied |
| SF | OFF  Red | No group fault  Group fault (PROFIsafe not active, incorrect PROFIsafe address, wiring error, device defective) |
| 1 | Yellow | PROFIsafe address 1 |
| 2 | Yellow | PROFIsafe address 2 |
| 3 | Yellow | PROFIsafe address 4 |
| 4 | Yellow | PROFIsafe address 8 |
| 5 | Yellow | PROFIsafe address 16 |
| 6 | Yellow | PROFIsafe address 32 |
| 7 | Yellow | PROFIsafe address 64 |
| 8 | Yellow | PROFIsafe address 128 |
| 9 | Yellow | PROFIsafe address 256 |
| 10 | Yellow | PROFIsafe address 512 |

#### Restoring factory settings

With the factory settings, all parameters are reset to the factory values.

**Restoring the factory settings with the "TEST/RESET" button on the basic unit**

Proceed as follows:

1. Switch off the supply voltage for the basic unit.
2. Press the "TEST/RESET" button on the basic unit and keep it pressed.
3. Switch on the supply voltage for the basic unit. The Device LED is yellow.
4. Release the "TEST/RESET" button after approx. two seconds.
5. Press the "TEST/RESET" button again after approx. two seconds.
6. Release the "TEST/RESET" button after approx. two seconds.
7. Press the "TEST/RESET" button again after approx. two seconds.
8. The factory setting is restored.

> **Note**
>
> If any of the steps are not carried out correctly, the basic unit will revert to normal operation.

> **Note**
>
> This function is always active, irrespective of the "TEST/RESET keys disabled" parameter.

##### Restoring the factory settings with the SIMOCODE ES software

Prerequisites: SIMOCODE pro is connected to the PC / programming device via PROFIBUS DP or via the system interface, and SIMOCODE ES is started.

Proceed as follows:

1. In the Project navigation view, select **"Online accesses → COM [Sirius PtP] → Update accessible stations → SIMOCODE → Commissioning → Command"**.
2. Click on the **"Factory settings"** button. The factory settings are restored.
3. **"Factory settings OK"** is displayed in the inspector window.

#### Setting the PROFIBUS station address

##### Setting the PROFIBUS station address with the addressing plug

Proceed as follows:

1. Set the desired valid address on the DIP switch. The switches are numbered. For example, address 21: Put the "16" + "4" + "1" switches in the "ON" position.
2. Plug the addressing plug into the system interface. The "Device" LED is yellow.
3. Briefly press the TEST/RESET button. The address you set is now stored. The "Device" LED flashes yellow for approx. 3 seconds.
4. Remove the addressing plug from the system interface.
5. After transferring the data to the basic unit, you will receive the message "Download to device successfully accomplished".

##### Setting the PROFIBUS station address with SIMOCODE ES

Proceed as follows:

1. Plug the PC cable into the system interface.
2. In the Project navigationDevices view, select**"Online accesses → COM [Sirius PtP] → Update accessible stations → SIMOCODE → Parameters → Fieldbus interface"**.
3. Specify the station address. After entering a new station address, the ![Setting the PROFIBUS station address with SIMOCODE ES](images/148918651403_DV_resource.Stream@PNG-de-DE.png) button "Transfer online data to the hardware" becomes active.
4. Click on the ![Setting the PROFIBUS station address with SIMOCODE ES](images/148918651403_DV_resource.Stream@PNG-de-DE.png) button. The online data is transferred to the hardware. The station address is set.

#### Setting IP parameters and PROFINET device name

##### Setting IP parameters and PROFINET device name on a plant-specific basis

The setting of IP parameters and the PROFINET device name is a mandatory step for communication via PROFINET.

These parameters can be set in different ways, depending on the needs of the plant configuration.

A detailed description of these options can be found in the section on "Configuration of further properties of SIMOCODE pro V PN as IO device" in the [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951).

##### Setting IP parameters and PROFINET device name with SIMOCODE ES via PC cable

Proceed as follows:

1. Plug the PC cable into the system interface.
2. Start SIMOCODE ES.
3. Open the "Switchgear → Open Online" menu.
4. In the "Local device interface" tab, select the associated COM interface.   
   Confirm with OK.
5. Open the "PROFINET parameters" dialog box.
6. Select "Overwrite IP parameters" and set the IP address, subnet mask, and router as appropriate.
7. Select "Overwrite device name in device" and assign the device name.
8. Save the data in the basic unit with "Target System → Load to Device". IP parameters and device name are now set.

#### Setting IP parameters and EIP device name

##### Setting IP parameters and device name on a plant-specific basis

For communication via EtherNet/IP it is mandatory to set the IP parameters and the device name.

These parameters can be set in different ways, depending on the needs of the plant configuration.

##### Setting IP parameters and EtherNet/IP device name with SIMOCODE ES via PC cable

Proceed as follows:

Setting IP parameters and EtherNet/IP device name with SIMOCODE ES via PC cable

| Step | Description |  |
| --- | --- | --- |
| 1 | Plug the PC cable into the system interface |  |
| 2 | Start SIMOCODE ES (TIA Portal) |  |
| 3 | 1st option: Create new project  - In the Project view, create a new project via "Project → New" - Add a new device by double-clicking the button "Add new device" in the project navigator and select the application in the device wizard. See [Application selection](#application-selection) - Check the device configuration and adapt it to the actual configuration, if applicable - Select the communication settings under "Parameters → Ethernet parameters" and set the IP parameters and the device name - Under "Parameters → Motor protection", set the current setting and, if applicable, other parameters - Adapt other parameters in the parameter editor if necessary - Save the project and transfer the device parameters to the device | 2nd option: Do not create a new project  - In the portal view, click on the button "Online & Diagnostics" - Click "Accessible devices". The "Accessible devices" window opens - Click the "Start search" button - Select a station |
| 4 | Select the type of the PG/PC interface (SIRIUS PtP in this case) |  |
| 5 | Select the PG/PC interface via which the USB PC cable is connected to the computer. |  |
| 6 | Click on the "Start search" button and load the parameterization into the device.  After successfully transferring the parameters into the device (see message in inspector window), the device is ready to operate. |  |
| 7 | Select a suitable station. You can show the following devices/stations:  - devices with the same addresses - all compatible stations - accessible stations |  |
| 8 | Click the "Connect..." button. |  |
| 9 | Open the "Ethernet parameters" dialog box in the parameter editor |  |
| 10 | Select "Use BOOTP/DHCP" if the IP parameters are obtained from a DHCP server and assigned to the IO Device.  If the DHCP mode is selected, SIMOCODE pro immediately receives an IP address if the DHCP server is available in the same network. Otherwise the device searches for an IP address. If SIMOCODE pro finds no IP address when setting up an online connection or during a loading operation, because no DHCP server is available in the network, SIMOCODE ES assigns the device a temporary IP address. If the DHCP mode is selected, SIMOCODE pro accepts this temporary address as if it came from a DHCP server. There are two options for deactivating a temporary IP address again:  - Restart the device by means of "Commissioning → Command → Restart/Cold start" - Switch the device off and on again. After the restart, the device runs in the DHCP mode and looks for an IP address again. |  |
| 11 | Activate/deactivate "Overwrite IP parameters in device" and set the IP address, subnet mask, and router as appropriate.  The IP parameters are configured with SIMOCODE ES and transferred to the device. In this case, the "Overwrite IP parameters in device" checkbox must be selected. Choose the IP parameters to match the configuration in the automation system. If the IP parameters are assigned by the IO controller in the automation system, no setting is necessary here and the "Overwrite IP parameters in device" checkbox must not be selected <sup>1)</sup> |  |
| 12 | Enter the IP address. |  |
| 13 | Activate the check box "Use router" if you want to use a router |  |
| 14 | Enter the IP address (gateway) of the router |  |
| 15 | Select the EtherNet/IP device name to match the configuration in the automation system. |  |
| 16 | Activate the "Overwrite device name in device" check box if you want to transfer the device name to the device. |  |
| 17 | If necessary, select the "Web server activated" check box |  |
| 18 | Select the "Activate NTP synchronization" check box if you want to synchronize the unbuffered real-time clock of SIMOCODE pro V EIP using the NTP procedure. |  |
| 19 | Enter the NTP server address when the "Activate NTP synchronization" check box is selected. |  |
| 20 | Enter a value for the time shift: -1440 min to +1440 min (default setting: 0 min) |  |
| 21 | Enter a value for the cyclic update interval when the "Activate NTP synchronization" check box is selected: 10 to 86400 s (default setting: 10 s) |  |
| 22 | Load the data to the basic unit via "Online → Load to device" or click the corresponding button in the menu bar |  |

1)

> **Note**
>
> **Initial transfer of device name**
>
> The initial transfer of the device name must occur via the SIMOCODE pro system interface, since the device is not yet accessible via EtherNet/IP due to the missing address settings.

#### Backing up and saving parameters

Always save the parameters in the memory module or in the project. This particularly applies if you replace a basic unit, or if you wish to transfer data from one basic unit to another.

##### Saving parameters from the basic unit to the memory module

Proceed as follows:

1. Plug the memory module into the system interface. The "Device" LED lights up yellow for approx. 10 seconds. During this time, press the "TEST/RESET" button for approx. 3 seconds. The parameters will be saved in the memory module. After successful data transfer, the "Device" LED flickers yellow for approx. 3 seconds.
2. If necessary, unplug the memory module from the system interface

##### Saving parameters from the basic unit to the project

Proceed as follows:

1. Plug the PC cable into the system interface.
2. Start SIMOCODE ES.
3. Select the menu command **Online → Download from device**. The parameters are loaded into the main memory from the basic unit.
4. Open the menu command **Project → Save as ....** The parameters will be saved to the project from the main memory.

##### Saving parameters from the memory module to the basic unit

Proceed as follows:

1. Plug the memory module into the system interface. The "Device" LED lights up yellow for approx. 10 seconds. During this time, briefly press the "TEST/RESET" button. The parameters will be transferred to the basic unit. After successful data transfer, the "Device" LED flashes yellow for approx. 3 seconds.
2. If necessary, unplug the memory module from the system interface

> **Note**
>
> If the memory module is plugged in, the parameters will be transferred from the memory module to the basic unit when the supply voltage is switched on.

##### Saving parameters from a project to the basic unit

Proceed as follows:

1. Plug the PC cable into the system interface.
2. Start SIMOCODE ES.
3. Select the menu command **Online → Download from device**. The parameters are loaded into the project from RAM.
4. Select the menu command **Online → Load to device**. The parameters will be saved to the basic unit from RAM.

#### Configuring the diagnostics response

See Manual [SIMOCODE pro - Communication](https://support.industry.siemens.com/cs/ww/en/view/109743960) or[Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951).

#### Setting the safety relay functions

See [Safety-related tripping](#safety-related-tripping).

#### Replacing SIMOCODE pro components

This section contains information on the following topics:

- [Replacing the basic unit](#replacing-the-basic-unit)
- [Replacing the expansion module](#replacing-the-expansion-module)
- [Replacing a DM-F](#replacing-a-dm-f)
- [Replacing the current measuring module and the current/voltage measuring module](#replacing-the-current-measuring-module-and-the-currentvoltage-measuring-module)

##### Replacing the basic unit

###### Replacing SIMOCODE pro C, pro S and pro V PB / pro V MB RTU basic units

Proceed as follows:

1. [Save the parameters](#backing-up-and-saving-parameters).
2. Switch off the main power for the unit feeder and the power supply for the basic unit.
3. Withdraw the PC cable if necessary, then remove the cover or the connecting cable from the system interface.
4. Withdraw the removable terminals. You do not need to detach the wiring.
5. Dismantle the basic unit.
6. Withdraw the removable terminals from the new basic unit.
7. Mount the new basic unit.
8. Connect the wired, removable terminals.
9. Connect the cables to the system interfaces.
10. Switch on the supply voltage for the basic unit.
11. [Save](#backing-up-and-saving-parameters) the parameters into the basic unit.
12. Switch on the main power for the unit feeder.

###### Replace SIMOCODE pro V PN / pro V EIP basic units

Proceed as follows:

1. [Save the parameters](#backing-up-and-saving-parameters).
2. Switch off the main power for the unit feeder and the power supply for the basic unit.
3. Withdraw the PC cable if necessary, then remove the cover or the connecting cable from the system interface.   
   Note which interface the cables are connected to.
4. Withdraw the removable terminals. You do not need to detach the wiring.
5. Dismantle the basic unit.
6. Withdraw the removable terminals from the new basic unit.
7. Mount the new basic unit.
8. Connect the wired, removable terminals.
9. Plug the connecting cables into the system interfaces.  
   Connect the cable(s). Make sure the connector(s) is/are connected to the same interface again.
10. Switch on the supply voltage for the basic unit.
11. [Save](#backing-up-and-saving-parameters) the parameters to the basic unit.
12. Switch on the main power for the unit feeder.

##### Replacing the expansion module

Proceed as follows:

1. Switch off the main power for the unit feeder and the power supply for the basic unit.
2. Withdraw the PC cable if necessary, then remove the cover or the connecting cable from the system interface.
3. Withdraw the removable terminals. You do not need to detach the wiring.
4. Dismantle the expansion module.
5. Withdraw the removable terminals from the new basic expansion module.
6. Mount the new expansion module.
7. Connect the wired, removable terminals.
8. Connect the cables to the system interfaces.
9. Switch on the supply voltage for the basic unit.
10. Switch on the main power for the unit feeder.

##### Replacing a DM-F

See manual "[Fail-safe Digital Modules SIMOCODE pro Safety](http://support.automation.siemens.com/WW/view/en/50564852)".

##### Replacing the current measuring module and the current/voltage measuring module

###### Safety notices

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Replacing current measuring modules and current/voltage measuring modules**  The main power for the feeder and the supply voltage for the basic unit must be switched off before replacing current measuring modules and current/voltage measuring modules. |  |

> **Note**
>
> Please observe the information contained in the operating instructions!

> **Note**
>
> It is not necessary to detach the wiring from the removable terminals to replace the components!

Proceed as follows:

1. Switch off the main power for the unit feeder and the power supply for the basic unit.
2. Pull out the connecting cable from the system interface.
3. Withdraw the removable terminal from the module as illustrated below (current/voltage measuring modules only).
4. Disconnect the 3 cables of the 3 phases of the main circuit.
5. Replace the module.
6. Connect the 3 cables of the main circuit, running them through the feed-through openings.
7. Plug the removable terminals onto the module (current/voltage measuring modules only).
8. Connect the cable to the system interface.
9. Switch on the supply voltage for the basic unit.
10. Switch on the main power for the unit feeder.

#### Data sets

See Manual [SIMOCODE pro - Communication](https://support.industry.siemens.com/cs/ww/en/view/109743960) or [Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/109743951).

### Examples

This section contains information on the following topics:

- [Examples for the conversion factor](#examples-for-the-conversion-factor)
- [Limit monitor example](#limit-monitor-example)
- [Example of Calculator 1](#example-of-calculator-1)

#### Examples for the conversion factor

##### Example 1: Rated motor current 700 A

A 3UF18 68-3G current transformer (205 to 820 A) is used as interposing current transformer (transformation ratio 820 : 1) and the secondary side is executed once by a current measuring module 0.3 to 3 A.

Transformation ratio for I<sub>s</sub> = 820 : 1; I<sub>s</sub> = 700 A

Settings:

Set current I<sub>s</sub>1: 700 A

I<sub>s</sub>1 - conversion factor - numerator: 820  
I<sub>s</sub>1 - conversion factor - denominator: 1

##### Example 2: Rated motor current is 225 A

A 3UF18 68-3G current transformer (205 to 820 A) is used as interposing current transformer (transformation ratio 820 : 1) and the secondary side is executed twice by a current measuring module 0.3 to 3 A. Transformation ratio for I<sub>s</sub> = 820 : 2; I<sub>s </sub> = 225 A

Settings:

Set current I<sub>s</sub>1: 225 A

I<sub>s</sub>1 - conversion factor - numerator: 820  
I<sub>s</sub>1 - conversion factor - denominator: 2

##### Example 3: Rated motor current is 0.25 A

The motor cable is 2x by a current measuring module 0.3 to 3 A for a motor with rated current 0.25 A: transformation ratio for I<sub>s</sub> = 1 : 2; I<sub>s </sub> = 0.25 A

Settings:

Set current I<sub>s</sub>1: 0.25 A

I<sub>s</sub>1 - conversion factor - numerator: 1  
I<sub>s</sub>1 - conversion factor - denominator: 2

> **Note**
>
> In the case of motors with two speeds, the same or different transformation ratios can be set for each speed, depending upon whether the same or two different interposing transformers is/are used for each speed.

#### Limit monitor example

##### Example

The temperature sensors of the temperature module (TM) are to be monitored individually. If the temperature exceeds 60 °C, the limit monitor is to generate a message.

> **Note**
>
> Please note that the measured values of the temperature sensors are in Kelvin. For this reason, 273 must be added.

##### Settings

- Limit monitor - input:  
  TM - temperature 1
- Type:   
  **Overshoot**, undershoot
- Limit value:  
  333 (temperature available in Kelvin, for this reason, add 273)

#### Example of Calculator 1

##### Example 1

- Conversion of the maximum temperature of the temperature module from K to °C.

  ![Example 1](images/152972165515_DV_resource.Stream@PNG-en-US.png)

##### Example 2

- Conversion of the maximum temperature of the temperature module from K to °F

  ![Example 2](images/152972360331_DV_resource.Stream@PNG-en-US.png)

##### Example 3

- Conversion of motor current I<sub>max</sub> from % to A (e.g. set current I<sub>s</sub>= 3.36 A)

  ![Example 3](images/152972670347_DV_resource.Stream@PNG-en-US.png)
